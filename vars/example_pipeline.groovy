import java.text.SimpleDateFormat
import hudson.tasks.test.AbstractTestResultAction
import hudson.model.Actionable
def call(body)
{
    def config = [:]

    body.resolveStrategy = Closure.DELEGATE_FIRST
    body.delegate = config
    body()

    def applicationName = config.applicationName ?: 'SAMPLE'
    def buildNode = config.buildNode
    // ?: 'Built-In Node'
    def dateFormat = new SimpleDateFormat("yyyyMMddHHmm")
    def gitDateFomat = new SimpleDateFormat("yyyy-MM-dd")
    def gitCurrentDate = gitDateFomat.format(new Date())
    def date = dateFormat.format(new Date())

    
    try
    {
        
        node("${buildNode}")
        {     
            currentBuild.result = 'SUCCESS'
            stage("Git Check out"){     
                
                            pipelineStage = "${STAGE_NAME}"
                            branch = "${BRANCH_NAME}"  
                            echo " ℹ️ We are in ${pipelineStage} Stage"
                            echo "The build will take place for ${branch} Branch"
                            cleanWs()
                            checkout scm
                            sh 'ls -al'
                            echo "${pipelineStage} is complete now ✅"

                             } // End of git checkout 
             
                            stage("Hello World 🌍"){ 
                            sh 'uname -r'
                             sh 'ls -al'
                            pipelineStage = "${STAGE_NAME}"
                            branch = "${BRANCH_NAME}"   
                            echo " ℹ️ We are in ${pipelineStage}🏠"
                            // docker.image('node:18.18.2-alpine3.18').inside('--net=host'){
                            sh '''
                            touch index.html
                            echo " <!DOCTYPE html>
                            <html>
                                <head>
                                    <title>Hello world</title>
                                </head>
                                <body>
                                    <p>Success does not count but the Journey 🛫 Counts !!!</p>
                                </body>
                            </html> " >> index.html
                            '''
                            publishHTML (target : [allowMissing: false,
                            alwaysLinkToLastBuild: true,
                            keepAll: true,
                            reportDir: '/var/jenkins_home/jobs/Demo-job-dsl/branches/master/builds/5/htmlreports/Hello_20World_20_21',
                            reportFiles: 'index.html',
                            reportName: 'Hello World !',
                            reportTitles: 'Hello Welcome to the world of jenkins 🌎'])
                            echo "${pipelineStage} is complete now ✅"   

                            } // End of Node Build stage

        } //End of BuildNode

    } // End of Try

    catch (Exception err){

                failedStage = "${pipelineStage}"
                echo "Oo..h Snap! There ia a failure at ${pipelineStage}🤔"
                currentBuild.result = 'FAILURE'
                echo "Error seems to be : ${err}"
                echo " No worries, we believe you'll succeed in the next attempt! 🚀"
           } // End of catch block
           
    finally{

        stage("Notify"){
            
        echo "Finished your Job...✅"

                } 

            } // End of finally block

      }

