def call(body)
{
    def config = [:]
    body.resolveStrategy = Closure.DELEGATE_FIRST
        body.delegate = config
        body()
    def reportDir = config.reportDir
        def reportFiles = config.reportFiles
        def reportName = config.reportName
        publishHTML([allowMissing: false,
             alwaysLinkToLastBuild: true,
             keepAll: true,
             reportDir: "${reportDir}",
             reportFiles: "${reportFiles}",
             reportName: "${reportName}"
             ])

}
