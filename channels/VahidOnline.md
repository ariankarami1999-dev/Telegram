<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn1.telesco.pe/file/D3Ti3WrVoa4zLz8GN82OwgjBOpdvZMf44AXPf-7DcwL-IcdnZaX_li9O6R8zUudiZX6p3nWL6NHXEHxAFyWnPq13JNGrj3IaDxgVFMJUHzhrWxpF1FJ6VmtDRHRRUrqdVjjnn0iiZvrmQQ7LI3HVa5D_En29D_LKCevjHNsJE5UfgppPphIvh8pV4ygRYfTEnNwy8S3PFpJqvQNAc4V_81-bm5hVYSdHHzq6tU7BQnIwA5kJYFRL9ChIpRgdw9hE3bFa9Lw4slbYXsMmOpxFOcyve8mXjlVB2OX2hIjU01pjye1rAyPMkXtU1Xy0pzU0N80cVW7-aOgMTQNarnOd3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 02:57:47</div>
<hr>

<div class="tg-post" id="msg-77519">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r7awIUrq7c0VdEZc3NO23ZTE11pYwqMv-rI-mW7JrFtrmPQinpFqmlTDAkEzIPoydahLEl7WuB0UJ8vhXaN42rrK9m16LmejJ5gBIiuivNF4lXQzU77Z5jTLbUGX_9S9EGcv8K0p8kditQaUxOT5YQ4e4vk_kEoyemB3RgVSwR_Dti6QgxlaFS2RT-Vdj4yRo3YsunqIE3uZ3ybaR-Olj_PxVdUMAAqaULdKIRRXEGRLcbKsTJ0wX56iGb3JCryFQumMd_eWsl9O_kA9X2ud7tRlThJQLXXNcb8mId9MFoyR3AngCl7kLpeQjmJ2CLDLL4AKLFZRH0QGzFJMC6gEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNj_L_LNVG39nkmGMuPQ4slTtny-eN3wvuBUglRnV4y7BdPWjmEQuZmvapvO3LLHCwPDm0ZVQ5nCpfcIByXJ5BChMtd9gC3LNEf7FqrzerD5G9jj0YA9Hyp4cOhBp0ybPem9vmJf2_-VEWhelhL_ib50eq2lepihe2ILKaZDfwJgvWFNYBeHhPgJfMZDojaqnzEDPTnIIlaSJ3jL4jGRlHifoo4QcdMBpCn4My8V2LyjW1WMqYirr9_EJkCVvn58fY9s1EI1gV_viaJ8l7hh1MU0tYi3cYifq5dkziFhPJHaYaKVuauApQIeFWDNEi2_JaTlGvnLfUE6FJlGdGLomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hMaamAnjuQtesIgKeUtLhnkh4N6EAAKhpeMC3zPwUdyXu9g0zM-G40ejJMHcdqgzGRpA0kHOS9m68HiPc2z-Wg6_jEEQfy8guelssgwZv75ncnI3r6DTbYII7JfqEQPQ55kv-8a4vi_k3uJzJRWDoE3O3onOZzkznIKyqs5pScSfAvvxImXin0w3GURP2jkGf8ihXP9ZIv9TNeoRTGBvwG1bxxeOaeU8Blc1Bkh4C7WPZC8qwVrrVP1azoJhws8tACtkflL2vyo5vI7OqDVs54_eqYBP625AKc5wHqi_4Uikjn89JnSXeAN9kmni4G081ewBy9NupVckOMk8V4QjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NTUkJZhoLNQPLiYHW5qJSpcijyD2LMvfEbPDzV0cvIbece8Y1rBa-AOonyEfp6YmA4D43uoaf3hSaLvCNyrv5cUH1dsiwv0Nkdi2eRKidgB8Q_bwmCh040uIJylTXslKl2BhuxpWSbdRLW50F0guUpnT5-zKr5dNKNricuCizFYo4ajVCTWuNqM7W1XhrVvcOkWg8jdQzIz6CYV_-sPolQN9LLiJ6VSn-aE6YUOTi0is_hICNMcehKVMfpOwBgPZNRNDYs74l6Gfjk1X5zO4F9GK5oMMeRrrl9Lad_dlr6rQXNAPyBy9NT5SZtR-mu0b5HGxun2vQwhEjkPj_dqb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EyqWKuTKy3VZ3lHuizrfsEqACLsk7AAsobJIzKNdnFv0JPdln5ogIdfEy9U1wc68wG8_Yoj-E-zN_5tcamVeYfP3oGTU0B3qQ9OPiQ1ooMdOLhob3BVfEklVnAnSPI3gMGtnxTp6pe2ca6O9DbvMtdtxDipHOQc6Rw2FuUPTnESCVGuMP8_uCzAr-KppDVvKCXiNeNfpEqvkKX_5e2gm-bUdR0n8jLPVq38gEfCyb423RMCCKNL5dlzrz1aNiIJEbUdLDnq8SPOZtP7EhL1keqy5xc1efFdOxU_JlCs-4NZkIGShObqyTkzk3VA9KPx1KpHlhVwx-RzYQrgfKdU8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nQpOwvXBPgRiDKKpvxcmRceQpFX_rqgJSITtN5kV0Y0Gf0XAW9YYZSO5g_EJYMYB6fqVJFLeVGlOdk7T992yttZua6tDHR5P4bcH9DegQex94rl3XtarzQa2PJLFmbK0z_sHpfNXw59SWzzWqa9b7dO_nAPFOOZEDNx1cpFTGjJlsfjwr1ak6dXaViQhaZZr9QMEpgMU7FNWzCryDtmGpaypqc5dkQcxi26wEDOZUrSwm_ipRjklT4cO2KoyCQLXy89iImqPIP1WTBcVlKUC2sJAj8AKkR70u5xE-GipeKJBnHmkd4U5NLBkDVl0-FqWHP58eWQt4SPKIho33-zB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L9sQ-LUq-cDayPzRP5N0hv_qE_75CgkuH2aEayMetL2qcVCJNWdP9LhMUSLmtRaGNsvcrpSs2AWYZG2dJyLav3mbKrbn2zX0Hi2yByTyCv_4-eeCJWAiQbOpzeZLYEqGkLLpWfD81Pgm_T5-OlYIO8z9NtIagoPCS_huIAmNNX_c2BbZ05V558yC7UurPup3gEhEfxli_8eu4Eb9vwK3XVy8HPtv-X6EsF8xcZCjlNVodu9MssdNhaPXLf3hhtAvAqSBbdFbWQ7xFRQj7iCfUDaL4IulPUBJ2WfzCsUIjmJChci1hkIxuxP29K92RSTN8HetZ3IYzL9dME3S7eHPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s9SCyobMPCTGTWYh_XrLyrYkOXxYM9mXcQqOZUzHG-jhzI2NkjN5a_R-5mI1BF5iTX7YgG3hqbL9HCkW_OWXoZ5rnUPHy6hR17bioxqMmtr16rkYahFp446gi5mmwDyUcOSNXjJH0NGPDjKWj6JIa64fU4JazS19Q-V38N9rzHPDJSZW4aRZPlfAo1vooXA7WzGis4gMrSLblnk6u7UDIZ4MFbxz3ViEMtWlgcB7UvK1eavCwypDB-vubVseqdVKNRVzutTNOotEoBSohQumZ6Lkx4Ir21lEAddBRshXIRbjkOUHD2OBu0oyvn0Pv2GuJtSoI659X3ClNcqedHxiKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B8ODDnjduGjnVyyOPaBi_EdMZeoeQyPiG3yFMiOqdlPYTQWqsi0cN4DW6asq79ixUWAOjrUUK3stf-jcNvsjV8oWGYULmDR8h9MVqOQCVRepuK-oOUNKT9tG2lNNeuTq8W27Xve9OWUIT9W6lBcSgV-GCFdJPs7tqsK116s0FqKoMN21bgph2PILql32v4YhaBzWXwYYsW1HJdjhc6eYorsR33-pzbQ4QOLIeoM6nVQFn1U_BtkNnsfwQo19Sv57a4SdwzDJtOf_xYDeEpHAnZpWzwfnqxNG3ZkWGxomig0_KQDBUCgprYvF_oVJyqa1MD7FQe0AbvmFz1Yg5HFPaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه تصاویری ساخته‌شده با هوش مصنوعی را در «تروث سوشال» منتشر کرد.
در این طرح‌های گرافیکی که با عبارت‌هایی نظیر «این نفتکش اکنون متعلق به ماست»، «خداحافظ اتاق موتور» و «دیگر موتوری در کار نیست» همراه شده‌اند، صحنه‌هایی از انهدام و آتش‌سوزی ناوها و نفتکش‌های جمهوری اسلامی ایران و حضور نمادین او به همراه نیروهای آمریکایی بر روی شناورهای توقیف‌شده شبیه‌سازی شده است.
او پیش از این نیز تصویری گرافیکی از «حمله به خارگ» منتشر کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/VahidOnline/77519" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jfh8v18IEMeQckN_4U9fYjlKWJG9d9doOVaV3zx6qqy_Sidva8xiyOHEzODW-4OJiLnQWiSNacTN6M1liH5c1Zro4S6Soafamog8DKE1p_a37nb-Y7LPgxKuM8TttY4rdbBvDBTjCPcBw0SwS9NI1zb-Q-KrA0JQVcEFgKST-W0t-oUAkUg1fJ2aqPNuMG5S72OqR3zC9kAqKCGZndS-UhMyHrApFNBlnyFjIij5V-nk1FY9KYRg66W96VWOdfsOtpqV_n-NopKavKHgwEL99QMwU63oTCI9OzZ73FH-0A-iTEJTBpkX2OUQ2iZGROqsef-WOmC5RenQ8U_2Br0grA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbXs4PD1SqFdwPKADvDF202G2H7qAZV56XQCgEM3d6FnlIxHvs5C5tZUe4D5lQVcluvQDRQD-mEhSFmxFP4pYX7KMb9ogTXnNEgWLNhwIJ3RPmxBdhfuDy_jRMETi5kg-8IlVTDbLiGBw1aWoE9mAlcSwnw5hSj6PJWxi1Y8N_rNYhNEafYG7BzWWKaKEgLNye2wqHt51AQ-8SwPPrc9umIbqgBSkOB30nA3fBkx3EkJusjUz2a1P4zQbfrMEy6zvS9L2jyq5gfy60nztJ36VUlW103X0Dq-DRp-HKHAC5ovr5uoYStg6TKH3z5V_qwesfIr86MxfXW4lWmvOixYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ewBH5CTOHLi8AOGc7qmouzgURYDAzAbYl9KOa0uQ8t1rjKzTMyMT1tdNVcZ4Z3qao8HOzN8aEz9fm-uWAXm8bF4NXt010SIYKXSRG5JWLDofk4Ypjp0JnkdiYCYdNKlp0cj037RSdFtk2A1KGEA67BjToRqaU-s0KHzUhWM0R6OnkzK4MBQNyXH2SXK6pDjoHl9498EjuWEF3JMrhcCuhPInnaypw_d5QmlQLKxTiPBkDxy-Sv6U4HQ86FaHiLo1I_hwn3YO-RzofM3ixlXtiJb6LxzHKa2805yn92CGI5ipx9GzWw3zmHrhyPScm52oiRaOXY-3wgSaoey17THtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UUX03o05Ur7TctnUUlW00ZP8WhpAZgNRn5FG-7FU7sBKB_4gF6PQAwimW102vTTgszAFm6nVCOoMrcsqUcT8gXip6fJTyWxsf88leWB9sNStY0LkszNaHlqOqwxkHOcEon3aPR8dbTxVnq5C3OqU7JFmn4JGQQPGU9uI_zYMrON4a-ljTpyjIFNtaHpU5dJ7ZQ7PN1nstmw_V0W-PAeSI2oi2vCgDRKO345nlQgCS0GaVlpNrczGg_ao4yFe6DliM3Ly9VU7bjPsnlfA5fbPaMLPQyy3_wLBMg9M1BfXZLexCOOVNuio_-6ysqIEiUXZmM61sb5axdwsf3CMVItjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eaAlSFH86QV6-Y7VZy7YIeXSKmOEonJ9dd_VWmbCkZ9NvaXIAX9vWuhCNPk6uld4gL5ox-7Le0GQG5V09qhNyhIklUN_dJlW9WpHGv_h-mfTbYxOuev0_y_QVNtK9iQHVPZ0Zf71j3EyBGY1RsTpPCLtciUCFpspfCTto4SSHDAikD_DbDs5LDpvEzdRe3QE9GuYL31zLCQpBamBgMABeTGSBCBAEOoXO9pWMdAH022bTf69pmg5w7HVUNHhviZaqYrMPwg1iEGxlAmimvz9j_CgeQlTfZ_WD6VeyVXN-kB0KLncFz7pGAywuE_0H68w2iwZ443WnZNQlIwP-iTJTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حساب کاربری خود در شبکه اجتماعی «تروث سوشال» تصویری ساخته‌شده با هوش مصنوعی منتشر کرد که یک جزیره شلوغ و ویران‌شده در میان آتش و دود را نشان می‌دهد.
روی این تصویر عبارت «حمله به خارگ» درج شده بود.
ترامپ تصاویر دیگری هم منتشر کرد که با هوش مصنوعی ساخته شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/VahidOnline/77514" target="_blank">📅 00:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_pm8z-w1khRiPd84w0r7Xm-qPsbeU3dAv11iybWhc_7mWP4fa8Mo5hBeqQ2_NrQJTgHzCn7Udgw1YxYL5VRHzw26Zuj1r7Fiqa2I0y7FlIoxT3Eea_y4OnSo7fiIETz6ur-uxkcQHleB_BggeclAx5Oql641XK3DiMSh8z0h5PR8Wxkm6alNizZnjF5D90QiGqRzABpa5_oHu3eSRYv3dq_mlXaGlGjKU33aTfNk25zl6RHdUJMrh1FWRCH5KBxOvWSbrWIP8cCoMbBLS8GVHg5PDKrSq8TIX9aoAPKn5PTUu-5JzTnx7qfZoA_SIk11hubfrXa2If7uXX7wQ9N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از منابع آگاه گزارش داد برد کوپر، فرمانده فرماندهی مرکزی ارتش آمریکا (سنتکام)، به دولت دونالد ترامپ توصیه کرده است کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا به اعتقاد او این عملیات به سقف اثربخشی خود رسیده است.
به گفته این منابع، کوپر ارزیابی کرده است حملات دو هفته گذشته توانایی جمهوری اسلامی برای هدف قرار دادن کشتی‌ها در منطقه تنگه هرمز را به میزان قابل توجهی کاهش داده و بیشتر اهداف تعیین‌شده برای حملات هوایی نیز از بین رفته‌اند.
منابع آگاه افزودند کوپر به مقام‌های آمریکایی گفته است در صورت تصمیم برای از سرگیری عملیات گسترده نظامی، آمریکا می‌تواند ۲۰ درصد از اهدافی را که در عملیات «خشم حماسی» هدف قرار نگرفتند، مورد حمله قرار دهد. با این حال، او تاکید کرده است اگر تصمیمی برای بازگشت به عملیات گسترده گرفته نشود، ادامه کارزار بمباران دو هفته گذشته توجیهی نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77511" target="_blank">📅 21:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opWiAgFA37eqJe8YJyMJY2CgI-Rxz2r0-9aqcJXWd9unmKLGzH7U5pccWbizQvsZkHIBHQsuwYY-aJM4KHs3yhq8t2Ytr5rDua6lRFvzsIDaMre40TqWSOJqpFD8-dKAG6xHlXNjDPr7HbYoOJAbrtSdDq_lrYRvfxkcyrWQNQHfR-w-MCe9hl-c6QzWDKCA7k5bzueate0OYGP6dF5nMe1YDd-bwyfeRov_g7OkZXraEFN3y3cuwml4yrcdTcrkB_0hXUjdHLeYgjWSS0F09T9G433iIDnE46aG_ct9fwPANYMDySWjdOtz6YKs5C7NTw-24wY_hMM_Af1PUYNqcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران با انتشار پیامی در شبکه اجتماعی اکس، حمله اوکراین به یک شناور «تجاری» ایرانی در دریای خزر را «نقض آشکار منشور سازمان ملل متحد» خواند و اعلام کرد این اقدام «نمی‌تواند بی‌پاسخ بماند.»
عراقچی در این پیام نوشت که ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، با حمله به یک کشتی «تجاری» ایران که به کشته شدن یک ملوان ایرانی انجامید، به گفته او «به خواست اسرائیل» تلاش کرده است اروپا را وارد جنگ کند. وزیر خارجه اسلامی افزود که در گفتگوهای تلفنی خود با کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا و سرگئی لاوروف، وزیر خارجه روسیه، تاکید کرده است که این اقدام نباید بدون پاسخ باقی بماند.
ولودیمیر زلنسکی پیش‌تر اعلام کرده بود که نیروهای اوکراینی در عملیات‌های دوربرد در دریای خزر، کشتی‌هایی را هدف قرار داده‌اند که به گفته او برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77510" target="_blank">📅 19:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWOnm0fw0pPilaJD_ps0LwmixbTegm2JtSVhA93evQ5mMP15P88U7LrVGxAQiCIBvseqLMqkR7AKkq9GXCn-DHNFvgWW6UPxC1dbyzRa1OPcPsbaGb-zRo2lNEb6frxh3LGXqvd8AEX9ee0dCERP-uvs5YF0muLz0pUn8xi6L3ACVXoTAtqSDBvvO4dMSJSI2mPaurct5-iPSZmqqiUZl9GbA018Us9o4atpSPJtqfl5SRJCcGRnod9YCThocM0WyQCiR3jsx9XuZxGWg0eyitiqC_1PdkbWY3utbjCC5xWZuTmEHrwTjgckbueCvrC-glKtVgq7rrpWah_iEh9JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، گفت درگیری با ایران زمانی پایان خواهد یافت که حکومت جمهوری اسلامی سقوط کند یا آن‌قدر تضعیف شود که برنامه هسته‌ای خود را متوقف کند.
او در گفت‌وگو با شبکه فاکس نیوز مدعی شد جمهوری اسلامی باید به این نتیجه برسد که ادامه ایجاد «آشوب اقتصادی در جهان، کشتن هزاران شهروند خود و حمله به دیگران» هزینه سنگینی دارد. نتانیاهو تاکید کرد که برنامه هسته‌ای ایران «چه با توافق و چه بدون توافق» باید پایان یابد.
نخست‌وزیر اسراییل همچنین هشدار داد اگر ایران یا گروه‌های هم‌پیمانش به اسراییل حمله کنند، با پاسخی «بسیار قاطع» روبه‌رو خواهند شد و افزود تهران در صورت انجام چنین اقدامی «اشتباه بزرگی» مرتکب خواهد شد.
نتانیاهو درباره سفر پیش روی خود به واشینگتن و دیدار با دونالد ترامپ، رییس‌جمهوری آمریکا، گفت قصد ندارد اطلاعات تازه‌ای ارایه کند، زیرا به گفته او، همکاری اطلاعاتی میان دو کشور بسیار نزدیک است. او افزود مشتاق است دیدگاه ترامپ را درباره آینده درگیری با ایران بشنود و گفت: «در بسیاری از جنبه‌ها، این تصمیم اوست.»
او همچنین اعلام کرد که «قطعا» برای شرکت در نشست مجمع عمومی سازمان ملل در ماه سپتامبر به نیویورک خواهد رفت و گفت قصد دارد از تریبون این سازمان درباره اسراییل و ایتلاف اسراییل و آمریکا سخنرانی کند.
نتانیاهو در ادامه از زهران ممدانی، شهردار نیویورک، انتقاد کرد و او را به دامن زدن به نفرت علیه یهودیان و حمایت از حماس متهم کرد.
او همچنین گفت از کاهش حمایت حزب دموکرات از اسراییل «بسیار نگران» است و مدعی شد شماری از چهره‌های اصلی این حزب تحت فشار فعالان سیاسی به مواضع جریان‌های ضد اسراییلی نزدیک شده‌اند.
نخست‌وزیر اسراییل در بخش دیگری از سخنانش از موضع دونالد ترامپ درباره عربستان سعودی حمایت کرد و گفت ترامپ به درستی تاکید کرده که در صورت عادی‌سازی روابط ریاض با اسراییل، تنها باید با یک برنامه هسته‌ای «غیرنظامی» برای عربستان موافقت شود. او افزود آخرین چیزی که اسراییل و آمریکا خواهان آن هستند، شکل‌گیری یک برنامه هسته‌ای نظامی در عربستان سعودی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/77509" target="_blank">📅 19:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77508">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1x12IRZqMGr3nkrww-AVGPKH5mVyscrMUmJrRg8gNm8cByh0nZzCgot6j4tXtpc6-A3VsQZdWfdrbCqo5zwdNWBcsAHVhIESrX_8Cc2csN35uF03Ky7t-VPihl7oDuA7psjX0YPO2xiHuvY-OtjMcKpsYX-Kvxea_Wxu-0muFfha8Az5-W46AY0TvRtmnqaP3crN8YGr94LHg8_4Frqt0sR4_k8kIAERrT_ARLTlizpBi_zk64TeEQORNBUkGcwbCfL6bQbWobOUsj9jwHtqji9wVKtAZI9zMt2eMK4LWLFN-IPDzOPKPsDavlMOxHQ-WlICBbG4OVPH4bxgXVTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک والتز، سفیر ایالات متحده در سازمان ملل، اعلام کرد که دونالد ترامپ، رئیس‌جمهور آمریکا، حملات علیه ایران را به‌طور موقت متوقف کرده تا فرصت بیشتری برای پیشبرد دیپلماسی فراهم شود.
والتز روز یکشنبه در گفت‌وگو با شبکه فاکس نیوز گفت: «او دارد به مذاکرات فرصت می‌دهد؛ کمی فضا برای پیش رفتن گفت‌وگوها فراهم کرده است.»
سخنگوی ارتش جمهوری اسلامی نیز گفته که در پی توقف حملات آمریکا، ایران نیز حمله به متحدان واشینگتن در خاورمیانه را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77508" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEyKao7SQkfTeSGEFu2oyUds-gJli5dbSoX2C4xF4fjg83kqD0I-DELdJXpNmtbcx-MO4KMfsKQ5xm0fvfY_zoipkufUvA_Okfr0Y-krjuV-NPAPB24pRse-V726Ovo3KAKHoe_U6eKzz2BId3o497fnnnKDDHAAcQ8tYpse7K54HRsQpbn9zd_OQBxPe8GJcVEk91glP3RCq2WbEUlWjJKxH3GoNMYWcvCZ3VG935mXINUAvpaGWuVZCMfDgUKXAhGB0ROgIy9qk5g4hTjMRwpkE2a_g4E0FAWsfidkUBeL5Su5r9xBF9gwsJLXEXb5heOnugCd4L3kJ9dKKWw_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز یکشنبه مدعی شد که یک نفتکش در تنگه هرمز پس از برخورد با یک مین دریایی منفجر شده است.
بنابر گزارش تسنیم، این نفتکش پس از خروج از مسیر دریانوردی مشخص‌شده از سوی ایران در این آبراه راهبردی، با مین دریایی برخورد کرده است.
بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد که اواخر خرداد بین ایران و آمریکا برای تمدید آتش‌بس امضا شد، ایران متعهد شده بود طی ۳۰ روز در تنگه هرمز مین‌روبی کند تا تردد کشتی‌ها آزاد شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77507" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bw1boaHOvqKqcpTF9pkYj8S-rawNuwel6rhZIr9LcykaIHn-LIVQ-szUW-wnq5V2H_gY7poV2qRnR1B7QrgZD6DLB-zgn1RUDaLNTVrFI_h2-cQk0CkyzNn88NR8j9chRpP9TGhaJneoeJljuL8UfpP3nya0Yvk0UMHnb6xmHcSrEKjTN959EhaW6KJzfVdlhl75PwlUdvedNrs6lR-YRpd2lBFBFhslPK3Mwr_-rBpuvZli4t8O9z-b15d34AggpbeAyOIH13eNVa3zTEh_xPmiEm8hCwC64JnQGznH6hBCa_oHxyGBBRa2Gm2pGuFUBVX88gi5YOXO9XqZs92Fhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری العربیه، روز یکشنبه چهارم مرداد ماه گزارش کرد ایالات متحده آمریکا و جمهوری اسلامی ایران پاسخ‌ خود به پیشنهاد مشترک پاکستان و قطر را که با هدف ازسرگیری مذاکرات میان دو کشور ارائه شده بود، تحویل دادند.
بر اساس این گزارش، منابع آگاه در گفتگو با العربیه تایید کرده‌اند که کشورهای قطر، مصر، پاکستان و دیگر میانجی‌گران منطقه‌ای طرح جدیدی برای برقراری یک آتش‌بس ۱۰ روزه به واشنگتن و تهران ارائه داده‌اند. این طرح با هدف ایجاد فضای مناسب جهت حل بحران در تنگه هرمز و احیای توافقات پیشین تنظیم شده است.
العربیه نوشت، این پیشنهاد دو شرط اصلی برای بازگرداندن دو طرف به مسیر گفتگو دارد که شامل توقف فوری اقدامات خصمانه و بازگشایی کامل و ایمن تنگه هرمز به روی رفت‌وآمد کشتیرانی بین‌المللی است.
بر اساس جزئیات این طرح، مقرر شده است که مسیر جنوبی دریانوردی از طریق آب‌های عمان از حملات نیروهای مسلح جمهوری اسلامی در امان بماند و مسیر شمالی از طریق آب‌های ایران نیز از محاصره دریایی آمریکا خارج شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77506" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JtovlGTAuvNTsP3OwLEnxdEissCKsMYLyJPosgCcuLuU8YsUCsB5fBMJTg7-ClGql6HpOQeDQNHBT4OeuOEzAun6yVnDW1zp7Mc4xGtPAUVivmFoKl2yY1WVhJPIJPxp8tagHR5c-DpkJsPvDVV8R4flVk74dhk8qy_silXjPZXL5aHMUYPtvOA_Stmk9hKBxBSL4R6Hterm8bNugOlNVYL2Fh4GYjePEi06w_YUlZqbUoy85bpR2Qj3ERl9zw-yIEE23-hwcTPJ_URv8HBbkmyPQq_5KtEL5lNVXQJrWnOZO5BWP5M2TEiAIuRbTjXcXEMXcVWGG9ifIdUW8SC7eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان اویس‌قَرَن، پژوهشگر ایرانی علوم رایانه و استاد دانشگاه واشینگتن، مدال آباکوس سال ۲۰۲۶ اتحادیه بین‌المللی ریاضیات را دریافت کرده است؛ جایزه‌ای که به دستاوردهای برجسته پژوهشگران جوان در بخش‌های ریاضی علوم رایانه تعلق می‌گیرد.
کمیته این جایزه می‌گوید اویس‌قرن با وارد کردن ابزارهایی از شاخه‌هایی چون هندسه چندجمله‌ای‌ها، نظریه احتمال و نظریه طیفی گراف‌ها، شیوه تحلیل الگوریتم‌ها را گسترش داده و برای حل چند مسئله قدیمی علوم رایانه راه‌های تازه‌ای گشوده است.
پژوهش‌های او به‌ویژه در دو زمینه مورد توجه قرار گرفته‌اند: یافتن مسیرهای نزدیک به بهینه و نمونه‌گیری تصادفی از مجموعه‌های بسیار بزرگ و پیچیده.
مدال آباکوس هر چهار سال یک‌بار اهدا می‌شود و ادامه جایزه‌ای است که تا سال ۲۰۱۸ به نام رولف نوانلینا شناخته می‌شد. نامزد دریافت آن باید در آغاز سال برگزاری کنگره جهانی ریاضی‌دانان هنوز به ۴۰ سالگی نرسیده باشد. این جایزه از مهم‌ترین افتخارات بین‌المللی در علوم رایانه نظری به شمار می‌رود.
اما اهمیت کار اویس‌قرن تنها با فهرست کردن اصطلاح‌های تخصصی روشن نمی‌شود. بخش مهمی از مسیر علمی او به یکی از مشهورترین پرسش‌های علوم رایانه بازمی‌گردد: چگونه می‌توان کوتاه‌ترین مسیر ممکن را برای سفر میان چندین شهر پیدا کرد و در پایان به نقطه آغاز بازگشت؟
این پرسش که «مسئله فروشنده دوره‌گرد» نام دارد، در ظاهر ساده است. یک فروشنده، راننده یا مأمور توزیع باید از چند شهر یا مقصد عبور کند، هر کدام را یک بار ببیند و به نقطه نخست بازگردد. با افزایش شمار مقصدها، تعداد مسیرهای ممکن چنان سریع زیاد می‌شود که بررسی همه آنها عملاً ممکن نیست.
در چنین مواردی، پژوهشگران به جای یافتن پاسخ دقیق، الگوریتمی می‌خواهند که در مدت معقول مسیری نزدیک به بهترین مسیر را پیدا کند و بتوان تضمین کرد که نتیجه آن از حد معینی بدتر نخواهد بود.
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77505" target="_blank">📅 16:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPJAq--8Fe-FRJbDeKuJEgN_lmziE_1JHCWpQf901nYjBLB6sqonYC9pkPgaU43FMQ8dV_AfaPxe90zlXF5A-UNPBtD0PpwFn_w3pO3B8sjM5B7Xvjh46DUpCISrtr2DOAJo88Od751kG76PtCSOBtPDqaeb-eQFqoj-oBT5_pwOj0rfc42lcGUr4em8cY7YqOe--Z0GlqH0loJEIhySGn6lUnCOGjYD7FsSH2qE3QmKZTDRWd1T1bYaOzMus92vv7GxY7a94yMeFn-hLLbA_RZWqj-TtXv3wZFMviUBIBQW8Y0SE5gMuOz-u5Ik8ErpNiPkZOeXlP8UfeQ93wf6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید
گزارش نیویورک‌تایمز
درباره کنارگذاشتن طرح تشدید عملیات نظامی علیه جمهوری اسلامی را رد کرد.
استیون چانگ، مدیر ارتباطات کاخ سفید گفت دونالد ترامپ، رئیس‌جمهوری آمریکا، همواره گفته است راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر جمهوری اسلامی به اقدامات تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همه گزینه‌ها را حفظ می‌کند.
چانگ افزود پس از تحریم‌هایی که اقتصاد جمهوری اسلامی را فلج کرده و سیزده روز پیاپی حمله به اهداف نظامی، عاقلانه است که این حکومت به سمت توافق حرکت کند. او گفت در غیر این صورت، طرف مقابل می‌داند چه اتفاقی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77504" target="_blank">📅 16:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77503">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEcu-YqvXMJqG-MItDNUUBYnb_RIj1OKvU2g4uQCiFILJv3GGVLeRg3iYzitiq6dzUytI4tBW5ayQeF5YQCMr_Xm5iuA5krQcTG8riNsRzqQCsATC3AuuMNrzhHNxDynt0fXqa-o2OqHXVVnIU3Nz2ejweyYB5l_1w-Toy6Dcez1m1fcNqidcQcOoYYHlYyCzcwCNZ0b23Du7C4OpMTGktzLh9D-RBx9Q6xaor-9oM0aElt8osFMt9plk59nKNPM77eKqnbX1z0Bour-ie97cAwaj9lKH4bH5KL_GMpPHl8OUL_ng2qzkWlAYoakKupTxgzAu6Mt3yPEJf2hiKXRKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، روز یک‌شنبه چهارم مرداد بدون اشاره به جزئیات از «پیشرفت‌هایی» در مذاکرات و تبادل نظر تهران و مسقط خبر داد.
این مقام جمهوری اسلامی پس از آن در این باره اظهار نظر کرده است که یک هیئت عمانی که برای گفت‌وگو درباره مدیریت تنگه هرمز به تهران آمده بود شنبه عصر ایران را ترک کرد.
بقایی درباره این مذاکرات این طور توضیح داد: «روزهای جمعه و شنبه چند دور گفت‌وگو بین ایران و عمان در سطح معاونان وزرای امور خارجه در تهران برگزار شد که طی آن دو طرف در مورد اصول مشترک و سازوکارهای عملیاتی برای مدیریت تردد ایمن کشتیرانی در تنگه هرمز با رعایت حقوق حاکمیتی دو دولت ساحلی تبادل نظر کردند.»
مقام وزارت خارجه در ادامه اضافه کرده است که «در حال حاضر تغییری در وضعیت تردد در تنگه ایجاد نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77503" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77502">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iFFnYi-8FOW1hf86LJ5W8n0C-VVpMcTn2PrCvlxz8KB0oix2bGpNTHBBU9MhpoG8w7aSK_cT6SZeXtxmrt3HQfKwP_Z2N4NHfUCx9YXSlPBF8DOwKiE3-t4CisquWi1EH7VVGeQFnBhson2CEAmOTbRje2lvYxJ8EJEYYgtWGXyA6ARuagL_JTmktosVkHOQKyKo_09ji9elGTDzPZgjJsgTfTCUAxM-j2AgkF99cpICvBrbvYBDJyg1hrGA_0_uqyTUAPfsrUUCB0pncqeuM5DvYAKEIF_gZun8n8wVpfeEOorfIMkeST4cmiQ4_sP-telVeUMdKp7oBdoBaUqX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که سال گذشته دختر ۱۷ ساله خود به نام فاطمه سلطانی را مقابل آرایشگاه محل کارش در اسلامشهر با ضربات چاقو به
#قتل
رسانده بود، با حکم دادگاه کیفری تهران به هشت سال حبس و پرداخت دیه محکوم شد.
در قوانین جمهوری اسلامی ایران، مقرراتی وجود دارد که پدرانی را که مرتکب قتل فرزند خود می‌شوند، از مجازات‌های سنگین معاف می‌کند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77502" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Isu3FIwjn1ggsU1j-GtzfLrdO3GWNSjL5hwH-2elfC9FNb_1u33LKivhgCGd7eJpg5zHyIc2R0yw6GEhR3qoZv__yj_9S-C_xyj6wvIS2GLaWUNwutrj_RW6adSzVFUo7iCentCVrdKrBwMy1vd-rb0E4OeqHwAGpS_t9JDkCvh_sNVtzvl-vUSs95Sm4z9HWsOAH0OjKTZiFkvOOAgFo-JEj_VjgYWimPhlrb8jNlllPKOiIsN1c4AqZr7rGoAa6L8EnR7F3JiB_iAQfcMu5XhNvXCg2KqtSaH2W4Id63Ze9twNnk048znQqeumt5OjEPGUjriZEdpIGmkMK9RTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: منابع می‌گویند ونس و کین درباره تشدید جنگ در ایران ابراز نگرانی کردند
ترجمه ماشین:
یک منبع آگاه از موضوع و یک مقام آمریکایی به سی‌ان‌ان گفتند که در حالی که دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست روز جمعه کاخ سفید احتمال تشدید جنگ در ایران را بررسی می‌کرد، جی‌دی ونس، معاون رئیس‌جمهوری، و ژنرال دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا، هر دو درباره این اقدام ابراز نگرانی کردند.
جمعه‌شب، پس از نزدیک به دو هفته حملات هوایی پیاپی شبانه، به نظر می‌رسید آمریکا کارزار بمباران ایران را متوقف کرده است. یک منبع در وزارت دفاع آمریکا روز شنبه به سی‌ان‌ان گفت: «عملیات فعلاً متوقف شده است.»
به گفته منابع، کین روز جمعه به‌طور مشخص درباره ذخایر مهمات آمریکا و دیگر پیامدهای منفی احتمالی ابراز نگرانی کرد. یکی از منابع گفت کین به ترامپ اعلام کرد که ارتش آمریکا می‌تواند گزینه‌های پیش روی او را اجرا کند و موفق شود، اما سپس درباره پیامدهای احتمالی آن هشدار داد.
هر دو منبع گفتند نگرانی درباره ذخایر مهمات، یکی از چندین نگرانی مطرح‌شده با ترامپ در این نشست بود. در حال حاضر مشخص نیست که آیا این نگرانی یا هشدار درباره تشدید جنگ، دلایل اصلی توقف حملات پیاپی شبانه آمریکا بوده‌اند یا اینکه این توقف ادامه خواهد یافت.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت: «با توجه به تحریم‌های موفقی که اقتصاد ایران را فلج کرده و ۱۳ روز پیاپی حمله به اهداف نظامی در پاسخ به تجاوزهای مکرر این کشور، عاقلانه است که ایران برای دستیابی به توافقی از طریق مذاکره تلاش کند. در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77501" target="_blank">📅 06:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lpLwDAzrf2xvwOHCMvvXWFDfimN4_vPnZPtf31-02ewTbC3e617FNLcNxdtfh52s_CLgWQT99_rYcosvWfmkfYbaoqk8rLifBE_WisSpAHzYO_-ceZ1UJGfeI539rXtEc67ru653Op2x_hUmFaOUoz7l8rYxMk7SxO2Brkq9oL8Czhz2L91oR4xSgTp9xiP_xZv7LKR0vB2sQH3HlrlPZnxojgaQGULnmJ1TtLWq7u3knYcY6-wUmYuAl7mzShatzomspvKAJtIkz6ISAKf3GFdxFaDsGvDhPpoYLr0lAW92hlaVJwpTz5FvxkTZoHfjhnOv935TJxSUykh3Pj9kzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز:
ترامپ در پی ابراز نگرانی مشاوران، فعلاً از تشدید گسترده حملات علیه ایران خودداری کرد
یکی از نگرانی‌ها این است که گسترش درگیری‌ها ممکن است ذخایر کاهش‌یافته مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
ترجمه ماشین:
رئیس‌جمهوری ترامپ، دست‌کم فعلاً، برنامه‌های تشدید شدید حمله نظامی آمریکا علیه ایران را کنار گذاشته است؛ به‌ویژه به این دلیل که نگران است تشدید جنگ، ذخایر از پیش کاهش‌یافته پنتاگون از موشک‌های رهگیر ضدبالستیک پاتریوت و دیگر مهمات پدافند هوایی در خاورمیانه را به‌طرز خطرناکی تحلیل ببرد.
به گفته مقام‌های دولت، تهدید متوجه ذخایر موشک‌های رهگیر یکی از ملاحظات متعددی است که بازگشت به عملیات رزمی گسترده را به اقدامی بسیار پرخطر تبدیل کرده است. آقای ترامپ و دستیاران ارشدش همچنین از احتمال گسترش جنگ در خاورمیانه، دور شدن متحدان کلیدی در خلیج فارس که در برابر حملات ایران آسیب‌پذیرند، فشار اقتصادی جهانی و تشدید بحران‌های انرژی و پناه‌جویان نگران‌اند.
به گفته دو نفری که در جریان این گفت‌وگو قرار گرفته‌اند، تازه‌ترین چرخش در نحوه مدیریت مناقشه با ایران از سوی آقای ترامپ پس از جلسه‌ای در روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه او رخ داد.
به گفته این مقام‌ها که برای گفت‌وگو درباره مسائل عملیاتی خواستند نامشان فاش نشود، رایزنی‌های محرمانه بر کاهش ذخایر موشک‌های رهگیر پاتریوت و دیگر سامانه‌های پدافند هوایی پنتاگون متمرکز بوده است. یک مقام ارشد آمریکایی گفت جمعه گذشته، هنگامی که یک موشک بالستیک از پدافند هوایی آمریکا ــ که در حال مقابله با موجی از موشک‌ها و پهپادهای ایرانی بود ــ عبور کرد، سه سرباز آمریکایی در اردن کشته شدند.
به گفته این مقام‌ها، ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، در محافل خصوصی هشدار داده است که ازسرگیری عملیات رزمی گسترده علیه ایران امکان‌پذیر است، اما ذخایر موشک‌های رهگیر در دسترس فرماندهی مرکزی ارتش آمریکا را ــ که مسئول عملیات در خاورمیانه است ــ به‌طرز خطرناکی کاهش خواهد داد. سخنگوی ژنرال کین از اظهارنظر درباره توصیه‌هایی که او به رئیس‌جمهوری ارائه می‌کند خودداری کرد.
استیون چونگ، مدیر ارتباطات کاخ سفید، گفت رئیس‌جمهوری «همواره به‌طور ثابت گفته است که راه‌حل دیپلماتیک را ترجیح می‌دهد، اما اگر ایران به فعالیت‌های تروریستی در تنگه هرمز یا علیه متحدان ادامه دهد، همچنان همه گزینه‌ها را روی میز نگه می‌دارد.» او افزود پس از تحمل تحریم‌های فلج‌کننده و حملات مکرر، «عاقلانه است که ایران برای دستیابی به یک توافق مذاکره‌شده تلاش کند؛ در غیر این صورت، آن‌ها می‌دانند چه اتفاقی خواهد افتاد.»
آقای ترامپ درگیر این بوده است که در جنگ نزدیک به پنج‌ماهه خود علیه ایران چگونه پیش برود و به‌طور مشخص چگونه تنگه هرمز را دوباره باز کند؛ آن هم در شرایطی که با ازسرگیری درگیری‌ها در دو هفته گذشته، قیمت بنزین بار دیگر در حال افزایش است. دیپلماسی شکست خورده و به نظر نمی‌رسد تازه‌ترین دور حملات گسترده آمریکا توانسته باشد ایران را از لحاظ نظامی بازدارد.
به گفته آن دو نفری که در جریان گفت‌وگوها قرار گرفته‌اند، در حلقه نزدیکان آقای ترامپ، افراد بسیار کمی ــ و شاید هیچ‌کس ــ معتقد بودند طرح تشدید درگیری عاقلانه است. یک مقام ارشد آمریکایی دیگر که او نیز به شرط ناشناس ماندن صحبت کرد، درباره اینکه ازسرگیری عملیات رزمی گسترده بتواند ایران را به میز مذاکره بازگرداند، ابراز تردید کرد.
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 413K · <a href="https://t.me/VahidOnline/77500" target="_blank">📅 03:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=PEPkoD2etqTGCDke9nFEt8w1VuDm09ea4P857bv4eUBcbbD_RVCVWpAJT4ct6oW3tI1cq5orsX2mmGwNQfdlv9rK6qwMIbAl0R6Ie4y1ebFXfR20pq_brkQjUz1bQ0-asP1LGO-Nu4cqjHbxzpE5_fbZ2Isu7kym2Cph4Q7IxvuFitzVgRuRhHwWs5NvU13ArKHRA9UYzCmuRlmQU7GIgji6LXheGCycZK8fi2EM2PVOKuSoLW7T-lunBtsjt7LeI5VfBN6HCUiF77chOFP3_VrXR6NHvknrQlUUfYEZcikdwuCfiaaczAAZwYGxr77GDfRt1x49yaczbT9_vhW6rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a2f96f5fb8.mp4?token=PEPkoD2etqTGCDke9nFEt8w1VuDm09ea4P857bv4eUBcbbD_RVCVWpAJT4ct6oW3tI1cq5orsX2mmGwNQfdlv9rK6qwMIbAl0R6Ie4y1ebFXfR20pq_brkQjUz1bQ0-asP1LGO-Nu4cqjHbxzpE5_fbZ2Isu7kym2Cph4Q7IxvuFitzVgRuRhHwWs5NvU13ArKHRA9UYzCmuRlmQU7GIgji6LXheGCycZK8fi2EM2PVOKuSoLW7T-lunBtsjt7LeI5VfBN6HCUiF77chOFP3_VrXR6NHvknrQlUUfYEZcikdwuCfiaaczAAZwYGxr77GDfRt1x49yaczbT9_vhW6rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین: 00:32
محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است. تا ۲۵ ژوئیه، سنتکام مسیر ۱۲ کشتی تجاری را که قصد شکستن محاصره داشتند تغییر داده، ۲ کشتی را که از دستورات تبعیت نکردند از کار انداخته و برای اطمینان از تبعیت کامل، وارد ۲ کشتی شده است.
صبح امروز، نیروهای آمریکایی عملیات ورود و بازرسی برای راستی‌آزمایی را در نفتکش M/T Charminar با پرچم کومور، در دریای عرب، به پایان رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام روز ۲۴ ژوئیه، نفتکش M/T Lavine با پرچم موزامبیک را در دریای عمان از کار انداختند؛ پس از آنکه خدمه آن چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به‌سوی ایران در حرکت نیست.
نیروهای آمریکایی
🇺🇸
همچنان کاملاً هوشیار، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77499" target="_blank">📅 01:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1KSJkEmIBbOa4uHr5LZv09kywHc_jlp_kVYb0lUgp5lFFWFZZHhlrbTsadT9uDM7p_SB93vKgOwZRZRlKyeQfvfphdYVeGOKSHCKEvWZicEJmDPbauehS8H60qWzroCBD55MwznZcW5IxsFbwnH-aYFNhuE3-J6njMay-rAzGbw6bB4JWkUxeZw26KQiRahm81Xa29NKQWlbxmPxuQenYB-n7UalsnvqmoC_e5XmSK90jGkDNGBIke3lgm12MmNeY7LNQ0qTeq2wXogFLgbwhnbwnL66LE2mMbYxf7G7dTOR4D2LQZH5sf2poOvREaVPKlMrGiSlI64PMDmRVXotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه هشدار داد که اگر دولتش به چیزی که در مذاکرات با ایران می‌خواهد نرسد، قطعا حملات گسترده به این کشور را از سرمی‌گیرد.
خبرنگار شبکه فرانسوی ال‌سی‌آی در شبکه ایکس نوشت که در گفت‌وگوی تلفنی با ترامپ از او سوال کرده که آیا در حال بررسی ازسرگیری یک جنگ گسترده علیه ایران است یا نه.
رئیس‌جمهور ایالات متحده در پاسخ گفته است: «اگر به صد درصد آنچه می‌خواهیم نرسیم، قطعاً.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/77498" target="_blank">📅 23:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_EItgUpbTW6OfNhe4ExV-hHvj7U9jBcjnVntkf99gx1Mu-26bEkVj2d8hjjzS4SZVhGfU7pNP3emgHbV2PXtDQD2pMj3eyraxogolRaWl_R1HQc7Ggv_bLkPcNxMm12G9ZgJ_Sr6ZKGySa3AmW7hXn6rPlzL13iUYy4tN4yw415B_-nr7eI6whUxhtCU2wlBQ-lydb5LdOKIUnPfoJtqDi1kwisbJuM5bLWChmiEc2MJt6dHl9sI3sX4464kS3HK6PNeXSBdBqI0yAOC9iwtLyTgoTr9pRW3Zvcyay86FDRiNBGCxv1PkaHnCyDEHpCjaYMWA1aYH2iseOPRGr8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.  زلنسکی روز شنبه، سوم مرداد، در پیامی در…</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77497" target="_blank">📅 22:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw7zfw-xc9MsseC2pJykEd-mNC0fYjxcqy4CCeYmsZthkmruvDP0oOEf5pPc6bjWCfOvOw5vIzg3QnF2R6HcsCW1vKLr6q5Tg0ecCjVdc8loedAFdi3KQk9WmOVtjegF6_5Y_dozn7FwrB1EWvNkx1hu4OnRNijU3_4CbGF8aomeFMewiCVQSouGHqOTkVDlbCq9sIKUsUgZfR7X3AnOMyGleAm6uIYYTo-QORtcIKIT8ngy5KadPn4t7cN2geH6jdCwKtDLpCoeXMHTKv1Qdes8NWNa6AyutloNY_px42_MBDVAYSfCbilhDki5ZpvKcSVBhRcjw2Ro0RPOV8Z_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی پری، خواننده آمریکایی، از استفاده کاخ سفید از آهنگ «Firework» (آتش‌بازی) در ویدیویی از حمله آمریکا به اهدافی در ایران انتقاد کرد و گفت این استفاده بدون اطلاع و رضایت او انجام شده است. او افزود که از این اقدام عمیقا شوکه و خشمگین شده است.
کاخ سفید روز پنج‌شنبه ویدیویی در حساب رسمی خود در تیک‌تاک منتشر کرد که در آن بخش «boom, boom, boom» آهنگ «Firework» با تصاویری از حملات آمریکا به اهدافی در جنوب ایران هم‌زمان شده است. کاخ سفید در توضیح این ویدیو نوشت: «به ایران هشدار داده شده است.»
کیتی پری روز شنبه در شبکه ایکس نوشت: «از اینکه آهنگ "Firework" به‌عنوان موسیقی پس‌زمینه ویدیوی حملات نظامی در حساب کاربری تیک‌تاک کاخ سفید استفاده شده، عمیقا شوکه و خشمگین هستم. من این استفاده را تایید نکردم، از من اجازه‌ای خواسته نشد و به هیچ وجه آن را تایید یا حمایت نمی‌کنم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77496" target="_blank">📅 22:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrzdZZg5gP67T9ccIJRI1PsF-5Wr2ijlqLwKjJli51bzadt_ZVAHkPqwkvlr2HJvE-uqV2lBAPFQL0I9aAxVuU4zRkrbLrCGTodc-5tspMzvL6RsslNSRqyt1gxh-qWx-kFRRprjOSNLnmRNeWOcRvMPaVaP-voA78TDmfvLyamvcPoFLpL4Po-KYTY1aZXP2-WBLDqagN6vQNfZZIwt15d0AwPBXw-zGVJ6TOl2M1ioD91nPRjUy5LERDvMx4U7uOfoFmkIP6LGC7liFB-SY2QhOPQQlwUMtuRO5tqtR4CtF8Q5dmNfoh_XRZXmRY4b3qvH-F8fuhajh4RxZd1v8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ دستور داد ارتش روز جمعه در ایران حمله‌ای انجام ندهد
ترجمه ماشین:
دو منبع مطلع از این تصمیم گفتند دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه به ارتش این کشور دستور داد حملات جدیدی در ایران انجام ندهد؛ دستوری که به رشته‌ای نزدیک به دو هفته از حملات روزانه پایان داد.
چرا مهم است:
دستور رئیس‌جمهوری پس از آن صادر شد که او طی ۱۳ روز گذشته، هر روز حملات را تأیید کرده بود. هنوز مشخص نیست که دستور روز جمعه ترامپ تصمیمی یک‌باره بوده یا این وقفه ادامه خواهد یافت.
▪️
تصمیم ترامپ هم نشان‌دهنده تمایل او به فراهم‌کردن فضای بیشتر برای دیپلماسی است و هم حاکی از این ارزیابی که سطح کنونی حملات آمریکا ــ مگر با بازگشت به عملیات رزمی گسترده ــ به مرز اثربخشی خود رسیده است.
▪️
اگر ترامپ دستور ازسرگیری حملات را صادر کند، ارتش آمریکا می‌تواند در مدت نسبتاً کوتاهی برای انجام آن‌ها آماده شود.
▪️
به گفته منابع، ارتش آمریکا همچنان در حال تهیه طرح‌هایی برای بازگشت احتمالی به عملیات رزمی گسترده است، اما ترامپ هنوز دستوری برای حرکت در این مسیر صادر نکرده است.
▪️
کاخ سفید به درخواست اظهارنظر پاسخ نداد.
آنچه خبر را رقم زد: ترامپ طی دو هفته گذشته، هر بعدازظهر طرح‌های حمله ارائه‌شده از سوی ارتش را تأیید کرده و این حملات ظرف چند ساعت اجرا شده‌اند.
▪️
روز جمعه نیز طرح مشابهی در اختیار ترامپ قرار گرفت، اما او با آن موافقت نکرد. در عوض، به گفته منابع، به ارتش دستور داد حمله‌ای انجام ندهد.
▪️
اندکی پس از صدور این دستور در روز جمعه، ترامپ به خبرنگاران در کاخ سفید گفت که می‌تواند حملات را ادامه دهد یا حتی آن‌ها را تشدید کند؛ از جمله با «نابود کردن هرچه آن‌ها دارند».
▪️
اما او روشن کرد که به نظرش «راهبرد هوشمندانه‌تر» این است که با ایران «به توافق برسد».
▪️
ترامپ گفت: «همین حالا با [ایرانی‌ها] در حال گفت‌وگو هستیم. فکر می‌کنم با گذشت هر روز، جدی‌تر و جدی‌تر می‌شوند. ما کاملاً مسلح و آماده‌ایم، اما در حال گفت‌وگو با آن‌ها هستیم.»
▪️
ترامپ بعدتر در روز جمعه، در سخنانش در شام انجمن خبرنگاران کاخ سفید، گفت تصور نمی‌کند ایران در حال حاضر آماده توافق باشد، «اما من آماده‌ام گوش کنم».
وضعیت کنونی:
دستور ترامپ برای توقف حملات، چند ساعت پس از آن صادر شد که یک هیئت عمانی روز جمعه برای گفت‌وگو درباره ترتیبات جدیدی به‌منظور بازگشایی تنگه هرمز وارد تهران شد.
▪️
دو منبع منطقه‌ای مطلع از مذاکرات گفتند در گفت‌وگوها پیشرفت حاصل شده و ممکن است توافقی میان عمان و ایران در تعطیلات آخر هفته به دست آید.
▪️
پس از آن، رئیس‌جمهوری ترامپ باید تصمیم بگیرد که آیا توافق پیشنهادی را می‌پذیرد یا نه.
axios
:باراک راوید
تصمیم ترامپ هم نشان‌دهنده تمایل او به دادن فرصت بیشتر به دیپلماسی است و هم حاکی از این درک که — مگر با بازگشت به عملیات رزمی گسترده — سطح کنونی حملات آمریکا به نهایت اثربخشی خود رسیده است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/77495" target="_blank">📅 20:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=OXWJHKeYjscnHzElllyOeOk7tH54XsfvgtYL_pqRrIJTWkn5CFM6uBEGhD4JPsvySWkBM9BtiLM0xPHpMUirPOOFo7wjKS1qggDv6uWRV-Vwa1iMSCiGFs3NDssStqovlQd-ivRkNssAzt3Ve4ukz6FmBXulK6Y9OvtgcQGtF8z1lw_-Qt_NbKjzY8IfaOR5MnraTDG4Mn9HODw-Zn2ktGF1o68KKc2ZEsBJP_c_uFOpuOuu0GMqRasCaVJwogar34JmUE_C1HB_ADP1s8yDV4Y1a9GYTEjkYB1Mhfo2eBAw-m5Z0Y4vG6Coe5LBzWJ-28tJFHkAnZ2tLywubyJJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/136e1a65b9.mp4?token=OXWJHKeYjscnHzElllyOeOk7tH54XsfvgtYL_pqRrIJTWkn5CFM6uBEGhD4JPsvySWkBM9BtiLM0xPHpMUirPOOFo7wjKS1qggDv6uWRV-Vwa1iMSCiGFs3NDssStqovlQd-ivRkNssAzt3Ve4ukz6FmBXulK6Y9OvtgcQGtF8z1lw_-Qt_NbKjzY8IfaOR5MnraTDG4Mn9HODw-Zn2ktGF1o68KKc2ZEsBJP_c_uFOpuOuu0GMqRasCaVJwogar34JmUE_C1HB_ADP1s8yDV4Y1a9GYTEjkYB1Mhfo2eBAw-m5Z0Y4vG6Coe5LBzWJ-28tJFHkAnZ2tLywubyJJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: تغییر در قیمت یا سهمیه بنزین قطعی است
سخنگوی دولت مسعود پزشکیان اعلام کرد که تغییر در قیمت یا سهمیه بنزین قطعی است و دولت برای مدیریت مصرف این سوخت ناچار به اتخاذ راهکارهای جدید خواهد بود.
فاطمه مهاجرانی گفت دولت همچنان برای بنزین یارانه پرداخت می‌کند، اما با توجه به ضرورت ایجاد تعادل در مصرف، تصمیم‌گیری درباره نحوه عرضه این سوخت اجتناب‌ناپذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77494" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uURZZofmsBUC1T9yuPbA8lYVn6mxsQGP4EdtG67AWdpkl-Mbifzce-4cimk8jkuoefqHo_UBPg8iautA8YsTq-d6o6DjRrWneYtquSKkhOGW7jQL5LWX_7HL8JWrcJebHaF3INuSbYEyS7KDI_6mE6SpouJMm8cf2DucgfRr1asc4Grn1dRfGDlJy46PnvCoO3OWBglfaKGPwYE7wDePJPr4RD3t4ZOuxFv3_zZh9S8-CIiI8SJD0x0G6XztATgIfzp9vBP1jKfn4OmBX801GwDq8DnARVSUYg4E2h8LaD2gh-xcs6gyiwU679AwmD2nzigjNFEkr-V-xAKPMiqOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت خبری وای‌نت گزارش داد مقام‌های اسرائیلی برآورد کرده بودند حمله گسترده آمریکا به ایران، که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود در حال بررسی آن است، شب جمعه تا بامداد شنبه آغاز شود، اما با پایان روز جمعه به این نتیجه رسیدند که ترامپ فعلا حمله را متوقف کرده و فرصت دیگری به تهران داده است.
بر اساس این گزارش، در پشت صحنه، قطر و عمان فشار قابل‌توجهی بر جمهوری اسلامی وارد کردند تا مواضع خود را نرم‌تر کند و از وقوع آنچه یک عملیات گسترده و تقریبا قطعی آمریکا به نظر می‌رسید، جلوگیری شود.
این گزارش افزود مقام‌های اسرائیلی همچنان معتقدند تفاهم میان تهران و واشینگتن عملا از بین رفته و احتمال دستیابی به توافقی دائمی که حکومت ایران را وادار به پذیرش خواسته‌های آمریکا کند، نزدیک به صفر است.
بر اساس این گزارش، از نگاه اسرائیل، فرصت تازه‌ای که ترامپ در اختیار تهران قرار داده، تنها به جمهوری اسلامی امکان می‌دهد برای مدت کوتاهی زمان بخرد و تغییری در ارزیابی کلی اسرائیل ایجاد نمی‌کند.
@
VahidOOnLine
🔄
باراک راوید:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشدند، بلکه برای حمله‌ای دقیقاً هم‌اندازه حملاتی آماده شدند که طی دو هفته گذشته هر شب انجام می‌شد.
BarakRavid
رسانه‌های جمهوری اسلامی درباره این توییت نوشتند اکسیوس خبر «رسانه‌های عبری» رو رد کرد ولی باراک راوید خودش هم اسرائیلیه و علاوه بر اکسیوس خبرنگار واشنگتن شبکه ۱۲ اسرائیله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77493" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drgJsY5egZusU9gvqtL4prfedK1hNVgFJcZOVw-No9UGSjuZOdJMoltL-J3D_LW0osdo7VPkXy8560HcbjxehPrjat7jitpw1xGwH0m_lPnt5kD3c7SDG5VdtX3oCb0fDyDhuirlQNsuTN61T2GFNClOpF2X0NMg9Lb5xk5ehvv68opc1XUuNPuDvPvEYOgGmA4_aDaNgH1G20hg7zHVGFWq1e4mWs8KOGznphnJc2rCtmuW0GE2y3Oj65oXcHSNZ3WtkQHZ7oSehJbQZLUoCP4T7BfmVywtwUo5t5enNdeYwdoXbaQgK5r_W419FgCPlhK_2A3YNmNVcwpoCBaimQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولودیمیر زلنسکی، رییس‌جمهور اوکراین، اعلام کرد نیروهای کشورش یک ناو جنگی روسیه و همچنین کشتی‌هایی را که به گفته او برای جابه‌جایی محموله‌های نظامی مرتبط با ایران به کار می‌رفتند، در دریای خزر مورد هدف قرار داده‌اند.
زلنسکی روز شنبه، سوم مرداد، در پیامی در شبکه ایکس نوشت که اوکراین در حملات دوربرد شب گذشته در دریای خزر به نتایجی «بسیار خوب» رسیده است. به گفته او، در میان اهداف این عملیات، کشتی‌هایی نیز بوده‌اند که «با مشارکت ایران» برای انتقال محموله‌های نظامی استفاده می‌شدند. رییس‌جمهور اوکراین اطلاعات دقیق‌تری درباره هویت ناو جنگی یا کشتی‌های هدف قرارگرفته منتشر نکرد.
سرویس امنیتی اوکراین (اس‌بی‌یو) نیز همان روز گزارش داد پهپادهای اوکراینی سکوی نفتی «فیلانوفسکی»، متعلق به شرکت روسی لوک‌اویل واقع در دریای خزر، را هدف گرفته‌اند. بر اساس اعلام این نهاد، دو کشتی باری با نام‌های «پورت اولیا ۲» و «بگی» نیز در همین عملیات مورد اصابت قرار گرفتند؛ کشتی‌هایی که به گفته سرویس امنیتی اوکراین در انتقال محموله‌های نظامی میان روسیه و ایران نقش داشته‌اند.
تا کنون نه مسکو و نه تهران واکنشی به این ادعاها نشان نداده‌اند و گزارش‌های اوکراین نیز به صورت مستقل تایید نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77492" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=A0ocqTKCo_3HxmRYR_KqqglqfJgA9StN7CoJLEygYYSsnzWtig2qyyelIPlfp539Sir5AEA9grGVbcWwtWrfrXnLfkR3hM4m4qqt8dMiCkdy1DX5u6qaAZx6GXXY8vIu4hLFcrjLdbfYzoWwXNhoL9-ghp7QRKZEcGqQe9dUPwjsCeWVDKgEG4IdgkfhuD9MNsG6aSRn6Pw7gtlrAYVL8C24l0yVeNdv411YPS4ic0el6D9aYBB8VO9DtCR8C0yddYvQKp5aLSfLCAsYJBU9UObsWW_c0YRI94tsv87XS4MUHpZBASOJc13x6G57qT3r6kBWCSBpB_OkjqC9vqKzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0ae743c97.mp4?token=A0ocqTKCo_3HxmRYR_KqqglqfJgA9StN7CoJLEygYYSsnzWtig2qyyelIPlfp539Sir5AEA9grGVbcWwtWrfrXnLfkR3hM4m4qqt8dMiCkdy1DX5u6qaAZx6GXXY8vIu4hLFcrjLdbfYzoWwXNhoL9-ghp7QRKZEcGqQe9dUPwjsCeWVDKgEG4IdgkfhuD9MNsG6aSRn6Pw7gtlrAYVL8C24l0yVeNdv411YPS4ic0el6D9aYBB8VO9DtCR8C0yddYvQKp5aLSfLCAsYJBU9UObsWW_c0YRI94tsv87XS4MUHpZBASOJc13x6G57qT3r6kBWCSBpB_OkjqC9vqKzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ در مراسم شام انجمن خبرنگاران کاخ سفید، بخش‌هایی مربوط به ایران، ترجمه ماشین:
... آن‌ها پرسیدند: «می‌مانی؟»
گفتم: «بله، می‌مانم. یعنی، فکر کنم بمانم.»
اصلاً چه کار دیگری دارم که بکنم؟ ایران را دارم؛ این را دارم، آن را دارم. همهٔ این‌ها هم فوق‌العاده خوب پیش می‌رود. اخبار جعلی را باور نکنید.
پیش‌تر داشتیم صحبت می‌کردیم. گفتم: «ما ایران را به‌شدت هدف قرار داده‌ایم. نیروی دریایی‌شان از بین رفته؛ نیروی هوایی‌شان هم از بین رفته است. ۲۵۰ جنگنده دیگر وجود ندارند. ۱۵۹ قایق؛ قایق‌های خوبی بودند.
در واقع گفتم: چرا آن‌ها را برای خودمان نگه نداشتیم؟ می‌توانستیم از آن‌ها استفاده کنیم. اما هر ۱۵۹ قایق در ته دریا هستند.
آن‌ها هیچ راداری ندارند. برخلاف آنچه می‌بینید، پهپادهای بسیار کمی برایشان باقی مانده است. هر از گاهی چیزهایی را به نمایش می‌گذارند، اما چیز زیادی برایشان باقی نمانده است.
ضمناً همین حالا با ما در حال گفت‌وگو هستند. آن‌ها خیلی دوست دارند توافقی انجام دهند. فکر نمی‌کنم هنوز آماده‌اش باشند. فکر نمی‌کنم هنوز وقتش رسیده باشد، اما حاضرم گوش کنم.
ولی آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. نمی‌خواهیم واشینگتن دی‌سی، هیچ‌یک از شهرهایمان، اسرائیل یا، صادقانه بگویم، خاورمیانه با یک سلاح هسته‌ای نابود شود؛ چون من قدرت سلاح‌های هسته‌ای را می‌دانم. آن را می‌بینم؛ اجازه دارم آن را ببینم. نخواهیم گذاشت چنین اتفاقی بیفتد.
بنابراین، همهٔ این ماجرا دربارهٔ این است که نخواهیم گذاشت آن‌ها سلاح هسته‌ای داشته باشند.»
[تشویق حضار]
«و اگر آن را داشتند، از آن استفاده می‌کردند. اگر داشتند، استفاده می‌کردند.»
---
ما دستاوردهای بسیار فراوانی داریم که رسانه‌ها هیچ‌وقت درباره‌شان حرف نمی‌زنند.
برای مثال، در دولت من، رژیمی قدرتمند که زمانی هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شده است. رهبران سابقش برکنار شده‌اند و اکنون دیکتاتوری همجنس‌گرا آن را اداره می‌کند که با اختلافات داخلی روبه‌روست.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 471K · <a href="https://t.me/VahidOnline/77491" target="_blank">📅 06:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77490">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=RQWro2tbtXuLFJ-Y-83lLzK_Os08A6tsXKoPvwdSHE3Ux7sj3ZwDZ33rTWfPYz2fRYCq3-XG0eJ_shq7IN2vryGY5hXLLK3FD8C3ZYxjd-COkbuia748GwmMOmgqokzr6Pl7qymb6hJE8_LnoAMiNy8VLQXZ_ETjhJSSEETKzQNi7KB1uafHlHgTfU9uDUPMFHx38LcPQd7tZw4MEVJ6fyhPA4eBZnk6he0mvkG8jT7gkZ9rMCwnKuPmIxWFCy1jcu1frNWvRqlmKSrIdS7SRxy6A8S9Uz3h0V_VK3XhuzfQKkRG0khiTfJ0N1kSCGwMhRhPe0DGGEk52aaUwM8SRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7cf983c2ea.mp4?token=RQWro2tbtXuLFJ-Y-83lLzK_Os08A6tsXKoPvwdSHE3Ux7sj3ZwDZ33rTWfPYz2fRYCq3-XG0eJ_shq7IN2vryGY5hXLLK3FD8C3ZYxjd-COkbuia748GwmMOmgqokzr6Pl7qymb6hJE8_LnoAMiNy8VLQXZ_ETjhJSSEETKzQNi7KB1uafHlHgTfU9uDUPMFHx38LcPQd7tZw4MEVJ6fyhPA4eBZnk6he0mvkG8jT7gkZ9rMCwnKuPmIxWFCy1jcu1frNWvRqlmKSrIdS7SRxy6A8S9Uz3h0V_VK3XhuzfQKkRG0khiTfJ0N1kSCGwMhRhPe0DGGEk52aaUwM8SRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم شی‌هی، سناتور آمریکایی [و افسر سابق یگان ویژه نیروی دریایی]، با انتقاد شدید از اقدامات جمهوری اسلامی، حکومت ایران را «گروهی افراطی و تروریست» خواند که ۴۷ سال است کشور را تصرف کرده و ایدئولوژی نفرت‌انگیز خود را گسترش می‌دهند.
او گفت: این رژیمی که با آن می‌جنگیم، اهمیتی به سیاست‌های حزبی یا اینکه به چه کسی رای داده‌اید نمی‌دهد. آنها می‌خواهند همه ما را بکشند. ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
این سناتور آمریکایی در ادامه تصریح کرد که حملات موشکی پراکنده یا تحرکات قایق‌ها در تنگه هرمز نشانه قدرت نظامی نیست، بلکه «دست‌وپازدن‌های یک امپراتوری در حال سقوط» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/77490" target="_blank">📅 05:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77489">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJD5GKQYX8t88wUL9mmK2r21NkNKaJhXRj-0tYE5jPrwksG5fz6E0BU1Bu06rbJ_GOHV_PVCzFaQ6HC-mtngSDLNC-D7IioG5qKNaAKLTgnhJx2z0tlfzLO1_Gg0xiY1cDWsxdmoal2bgh_1X2fpvvC3gQu0wgMJyfNB3INGxQNXBI-6ujpqoXtd_SzNBUR4qOmwoOoloRL9NS9GhZbW6rC8DRSu21V8fHtksWFgaVCeYdJQ_UwWkOKbgUc2T41YMK_OntmNet6aEfTTcztA-n1W-Yz9HqMO4SDbiEB-n-1HqQCsJAlBqrSvs_J-Nw1xsx3Ti_N90DFbxje3DlpcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت فرانسه در تهران با انتشار پیامی در حساب ایکس ادعای روزنامه انگلیسی‌زبان «تهران‌تایمز» مبنی بر برگزاری جلسه محرمانه دیپلمات‌های اروپایی و آسیایی در اقامتگاه سفیر فرانسه را به‌شدت تکذیب کرد و آن را کنایه‌آمیز پاسخ داد.
تهران‌تایمز پیش‌تر مدعی شده بود که در ۲۰ ژوئیه، نشستی با حضور سفرای چند کشور اروپایی، ژاپن، کره جنوبی و نیوزیلند در اقامتگاه سفیر فرانسه برگزار شده که در آن موضوع خروج دیپلمات‌های بریتانیایی و هماهنگی برای فشار سیاسی بر ایران مطرح شده است؛ اما سفارت فرانسه با رد کامل این ادعا خطاب به «خبرنگاران تهران‌تایمز» نوشت:
"به خبرنگاران محترم روزنامه تهران تایمز، دفعه بعد، لطفاً اطلاعات خود را با دوستان‌تان در سرویس‌های اطلاعاتی ایران که حدود ده دوربین برای نظارت بر سفارت فرانسه دارند، بررسی کنید. متاسفانه، هیچ مراسمی در سفارت ما در تاریخ ۲۰ جولای برگزار نشد !"
FranceenIran
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77489" target="_blank">📅 03:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77488">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N2fWppX599joeOft6X-4yHDm_zwukXbYM8uA-L9q31QqYiVowArJTLaEhVeHDvNVD9ZU3IWABIhWRj-TbeyC_Sq-kId0ER3vTBxtJcgCOtvUhtOaZ5LQrkx6PrK-kUjMy4JwWEXIdmjVC24jZq0XbcJZH7FhwuXERjnRXizaBn3Yll3bMbj22K2tQaPPN2uTCd23Uw_4_NEIR00_i8_AxK5ezELro9jEiBaYk0jUbIKYw2Xwd68caWOYWh_PeWkBWWHLPX2sZYjDwEPGtf5JHgCyWvPH2wrHsutrRGluBttLqe3biPB7oT2qOr-kvuQKgRSQIcng5yPF53Z_PBB-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریم خان، دادستان ارشد دیوان کیفری بین‌المللی، در پی تحقیقات دربارهٔ اتهام «سوءرفتار جنسی» از سمت خود تعلیق شد.
نهاد ناظر بر دیوان کیفری بین‌المللی شامگاه دوشنبه ۱۸ خرداد ضمن اعلام این خبر افزود تصمیم به تعلیق کریم خان پس از آن اتخاذ شد که روند رسیدگی انضباطی به اتهام «سوءرفتار جنسی» در پروندهٔ او به مرحلهٔ نتیجه‌گیری رسید.
کریم خان، وکیل برجسته بریتانیایی، بارها این اتهام‌ها را که نخستین‌بار در سال ۲۰۲۴ مطرح شد، رد کرده است.
نهاد ناظر بر دیوان کیفری بین‌المللی می‌گوید کمیتهٔ اجرایی این نهاد رأی داده است پرونده خان به نشست ویژه کشورهای عضو ارجاع شود تا آن‌ها دربارهٔ آینده حرفه‌ای او تصمیم‌گیری کنند.
کمیتهٔ متشکل از نمایندگان ۲۱ کشور عضو دیوان با اکثریت لازم به این نتیجه رسیده که خان در ارتباط با اتهام‌های سوءرفتار جنسی مرتکب «تخلف جدی» شده است.
این اتهام‌ها از سوی زنی مطرح شده که در مقر دیوان در شهر لاهه برای خان کار می‌کرد.
طرح این ادعاها در سال ۲۰۲۴ باعث آشفتگی و بحران در دورهٔ مدیریت او بر بخش دادستانی دیوان شد.
تصمیم ارجاع پرونده به ۱۲۵ کشور عضو دیوان اقدامی بی‌سابقه در تاریخ این نهاد قضایی بین‌المللی محسوب می‌شود و می‌تواند در نهایت به رأی‌گیری دربارهٔ برکناری دادستان از سمتش منجر شود.
نهاد حاکم بر دیوان در بیانیه‌ای تأکید کرد که تعلیق کریم خان «به معنای تعیین نتیجهٔ نهایی پرونده نیست».
خان پیش‌تر نیز به‌طور موقت از مدیریت بخشی از دیوان که مسئول تحقیق و پیگرد افراد متهم به جنایات بین‌المللی است، کنار رفته بود.
در این بیانیه آمده است که کمیتهٔ اجرایی تصمیم خود را بر اساس گزارش یک نهاد نظارتی سازمان ملل، نظر هیئتی از کارشناسان قضایی و همچنین لوایح کتبی ارائه‌شده از سوی خان و فرد شاکی اتخاذ کرده است.
این رأی تازه‌ترین تحول در روندی است که نزدیک به دو سال دیوان کیفری بین‌المللی را درگیر کرده است.
@
VahidHeadline
کریم خان ۵۶ ساله که به دنبال بازداشت بنیامین نتانیاهو، نخست وزیر اسرائيل بود، به سوءرفتار جنسی با یک دستیار زن متهم شده است.
پیشتر آسوشیتدپرس در مجموعه‌ای از گزارش‌ها به اتهامات جنسی علیه کریم خان پرداخته بود، اتهاماتی که خان آن‌ها را رد کرده است.
طبق اسنادی که آسوشیتدپرس دیده است، خان با دستیارش وارد رابطه جنسی شد و سپس تلاش کرد مانع پیگیری ادعاهای حقوقی او شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77488" target="_blank">📅 02:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qtdr4cgalUQqx-MHLGlFp5SnwDmNU0s_P6AaVo_UjW_beYpCh4lD90IvMANBZpu7KDrIaE9-zAGSuWGeJNDDuKf-MSuwn69zX5Q9x7-Z2y57KwcSvscwWPYkm2zdBsjZWXfkKoEuK_T56KBvR7BlZIxrJH5Qz-TzH0lRqTjmVodopqSYLBaD-F6vvAbVNva9puLF5YvGiwKJ8Oqgg3jYx5PQd2aMLbUHFlmetBNZzFzGR9cN9A4-NILL0wLEuVVuqhUHcLxH2-2LHGqJ5xjGGPQdyL6JDDRZGSAuk3hK1KD9r7VdPxKa49lShsub33FDjQKgoGC20Dhr9wG-MqkebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مشترک نیروهای ائتلاف، جمعه‌شب، با انتشار بیانیه‌ای اعلام کرد که در پاسخ به اقدامات «بزدلانه و شتاب‌زده» شبه‌نظامیان حوثی در هدف قرار دادن کشتی‌های تجاری در دریای سرخ، عملیات نظامی متناسبی را علیه اهداف نظامی مشروع این گروه در استان الحدیده اجرا کرده است.
ترکی المالکی، سخنگوی رسمی ائتلاف، با تاکید بر اینکه عملیات پاسخ نظامی طبق قوانین بین‌المللی و با تحقق کامل اهداف عملیاتی به پایان رسیده، تصریح کرد: «بندر الحدیده هدف قرار نگرفته و تمامی بنادر یمن از جمله الحدیده، راس‌عیسی و الصلیف برای کشتیرانی، ورود کمک‌های غذایی و سوخت باز هستند.»
او همچنین افزود عربستان سعودی همواره در کنار ملت و دولت یمن باقی خواهد ماند و هشدار داد که در صورت تداوم اقدامات خصمانه حوثی‌ها، فرماندهی ائتلاف برای حفاظت از کشتی‌ها و منافع ملی «بدون هیچ‌گونه اغماضی» مجددا دست به اقدام خواهد زد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77487" target="_blank">📅 01:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vtky4SgC04kYUul3q_c-Uv0cbkY3UcrCHRGL3VFQBzHww1h4tAgfRpEVtIXHi0NMr_-iKv9i8O4SdpSbumaEdpsBO0AcKTA2ZYz7q7atlNAoADCiDeTPHm3DEHGk4W8QFRqlZDOzHhWQc3G1lwQP0sItGhE-mL4Z_j5_kwXQsiG87KGGRy86v7Ea7F5GV2ikB2oYPM7Zcd84CFNt6864vVSAGc27LuE97db4XCb0bLqJj4zQmjqg2NOd4iCJIbiAr-WHpTLWmzFGEMZMMxJAjBBvBEzOEWN6uY2JfzhE58zXmoLXjui7e7ibSZ3I5Amu0FH8kFX-uPaKKj9dQpjWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
اربیل، عراق (خبرگزاری آسوشیتدپرس) - ارتش آمریکا روز جمعه اعلام کرد که به یک کشتی تجاری دیگر که سعی در نقض محاصره بنادر ایران داشت، شلیک کرده است....
...
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی ایالات متحده، به خبرگزاری آسوشیتدپرس گفت که نیروهای آمریکایی کشتی M/T Lavine را در خلیج عمان پس از آنکه کشتی حداقل چهار بار تلاش کرد از محاصره عبور کند، از کار انداختند.
هاوکینز تأکید کرد که به خدمه کشتی هشدار داده شده بود و آنها از دستورات پیروی نکردند.
سپس ارتش به موتورخانه آن شلیک کرد.
این دومین کشتی تجاری است که از زمان اعمال مجدد محاصره توسط ارتش از کار افتاده است.
فرماندهی مرکزی ایالات متحده اعلام کرد که 12 کشتی را نیز تغییر مسیر داده است.
....
apnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77486" target="_blank">📅 01:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین
متن زیرنویس ویدیوی بالا
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه دوم مردادماه در کاخ سفید به خبرنگاران گفت به‌نظر او جمهوری اسلامی ایران در جریان مذاکرات با واشنگتن «هر روز جدی‌تر» می‌شود، هرچند تاکید کرد نتیجه این گفتگوها هنوز قطعی نیست.
او با اشاره به اینکه مسیر مذاکره را ترجیح می‌دهد افزود: «دو راه وجود دارد؛ یکی را عاقلانه‌تر می‌دانم، اما راه دیگر احتمالا ساده‌تر است.»
رئیس‌جمهوری آمریکا با اشاره به حضور مقام‌هایی چون جی‌دی ونس و مارکو روبیو در روند مذاکرات، گفت موضوع اصلی «پیچیده نیست» و تأکید کرد که ایران «نباید به سلاح هسته‌ای دست پیدا کند.»
ترامپ همچنین مدعی شد در صورت شکست مذاکرات، آمریکا می‌تواند اقدامات خود را «به سطح بسیار بالاتری» برساند و افزود تهران در شرایطی قرار دارد که «عملاً مجبور به توافق» است.
او در عین حال گفت عجله‌ای برای رسیدن به نتیجه ندارد و تأکید کرد که باید این روند «به‌درستی» پیش برود.
@
VahidOOnLine
گفت که به سخنان شی جین‌پینگ، رئیس‌جمهوری چین، و ولادیمیر پوتین، رئیس‌جمهوری روسیه، مبنی بر ارائه نکردن کمک و فروش سلاح به ایران اعتماد دارد.
این اظهارات در حالی مطرح شد که پیش‌تر پیت هگست، وزیر جنگ آمریکا، در نشست پرسش‌وپاسخ سنا گفته بود چین و روسیه در سطوح مختلف در حال «تسهیل» اقدامات جمهوری اسلامی هستند. با این حال، ترامپ به خبرنگاران اعلام کرد که رهبران هر دو کشور به او قول داده‌اند در این موضوع دخالتی نداشته باشند و افزود: «فکر می‌کنم به آن‌ها اعتماد دارم. آن‌ها نمی‌خواهند باعث ناامیدی من شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77485" target="_blank">📅 01:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qLTzBig98QPy-gzn18mleRQaXv7VU2RBz8uElT4cDjLjQVspxyMLnPjkxtiYbe1C0W_o57UXVz3xwNGhmUG6_Z4DOI1fOMMQ6npeY6C-0MjbjS99i0quiQMJ6aMeULS6pi1vH_mHBjGwVkbPPMPJkcadd2N3yXvxr1BT5XKfwKrGvCnxz1fsgdHz4IsNULwxC9FqBDWQ_Nel4BBpnlPRTSWqFPQLUdvcUryQjt2anVxK4w6nx-0qCgqYAAx5p8uh9zVkpB0Yv7KPdzdAoOCUrvhDrOvG5xmEohGQDaBkO_jk58uyCgo5PZNUYuZI-b99WzJqvyC46nr5RrqaWa_Zig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون روز جمعه دوم مرداد در ۶۶ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/77484" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WDgr9bau8a-lr9yDQKY7tuGu-ajqYle_n_-DZ8w-Z6tBTRePVza-Pu142zIVfrA027ULbmnY6TM5rEJ6F6Gt_m1-SgDAcmt5O771aKxOSKoMQTAhJJr36nUxDn1wpniC6_dcx-O4lC0_Q2d0MfPZe-pUKN1jWfeNchugl_rGxxfMi0-0WrYXPFooeq3MJAsA-Ff38qWyyjKchPOOCo8Npoa2UUBTdzn3p7lG3TJzGGCscDbE6Es7f1G2RnmzU8ES4jXGyX_Ih0M21QWmSpswwqEC2rGZ9RqURCF0ATpEvMgk0Gx7goTNzOwzTbJtUfxFST8m3x9zbOA7dHBOWWA7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BwZFlzlaRVKKT-Qx-PcHK-PbTZG2Khp3PZ5pkdyl21Fw7gjBPo3Rx85UzQymqrPpehpMtCjrA96yiyjrazfUczi3X3XYQaoIKwTWwXYgfLGQYMUUMFtkY9i8aQeQCR0c1AMaw3v1HIy-0dIIwFUOCZZwm_0g7j9A774bcBj0SnqWeYiKRM2m8xVzwAZ0Y5wtF7sQj1vAivgx7VcKiSSJODGfSd8aGlmpsbGEuEK3eQ-rfPQpg1xCqcyFbu1G3JV-kreBN8mNEbP-C4nkU6NDQtrwwJLZUCwooQpRmDxYII1u-_eJwyIDcx97j-qpo-A93o9ETtHGxXx3PwY3DK9Mng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده روز جمعه دوم مرداد، از اعمال تحریم‌های جدید علیه ۹ شرکت و ۴ فرد مرتبط با بابک زنجانی به اتهام دور زدن تحریم‌ها خبر داد.
بر اساس بیانیه دفتر کنترل دارایی‌های خارجی (OFAC)، این تحریم‌ها فعالیت‌های وابسته به هولدینگ «دات وان» (Dot One) زنجانی در ایران و چند شرکت پشتیبان صرافی‌های ارز دیجیتال او در ترکیه و امارات را هدف قرار داده است. خزانه‌داری آمریکا اعلام کرد که زنجانی با بهره‌گیری از سبد سرمایه‌گذاری متنوع شامل خدمات مالی، تجارت دارایی‌های دیجیتال، طلا و پروژه‌های زیرساختی، اقدام به پول‌شویی و انتقال مخفیانه وجوه برای ایران کرده است.
@
VahidOOnLine
تبلیغاتی که در کانال‌های تلگرام نمایش داده میشن به خود تلگرام سفارش داده میشن و صاحبان کانال‌ها ازش بی‌خبر هستند.
دیروز ده‌ها بار
تصاویری
رو دریافت کرده بودم که نشون می‌دادند مجرمان تازه‌ای حتی از آوتار خودم برای نمایش تبلیغ‌شون در اینجا سوءاستفاده کردند. ولی من امکان جلوگیری از نمایش اون رو هم ندارم.
تبلیغات مجرمانه رو میشه با کلیک روی اون سه‌نقطه عمودی که زیر علامت ضربدر در گوشه کادر تبلیغ دیده میشه به خود تلگرام ریپورت کرد.
فقط کانالی که تا سطح پنجاه Boost شده باشه می‌تونه نمایش تبلیغات رو متوقف کنه. چیزی
نزدیک به غیرممکن
.
بوست‌های این کانال در
سطح صفر
هستند. حتی نمی‌تونم رنگ لینک‌های اینجا رو عوض کنم چه برسه به استفاده از ایموجی‌های اختصاصی.
باید هزاران نفر با اکانت پرمیوم کانال رو Boost کنند که برسه به سطح یک و بعد هزاران نفر بیشتر از افراد قبلی دوباره کانال رو بوست کنند و....
این رتبه‌بندی ربطی به تعداد دنبال‌کننده و میزان بازدیدکننده و آمارهای اینجوری نداره و فقط باید هر روز از بقیه التماس کنی که کانالت رو بوست کنند.
یعنی حتی اگر به سطح یک هم برسم باز برمی‌گردم پایین چون باید هر روز بخواهی دوباره بوست کنند.
با روحیه من سازگار نیست.
خیلی زور بزنم، برای درخواست ریپورت سوءاستفاده تبلیغاتی از عکسم می‌نویسم: ریپورت هم میشه کرد.
از این رو محکوم به سرنوشت مشخصی در این زمینه هستم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 447K · <a href="https://t.me/VahidOnline/77482" target="_blank">📅 21:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77481">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y97-BaQwFzGysw63Md38112SldQ6r3ku18ntwa_0i5uSUfXc-pOUs040SYguOBnafngmRb4Rnnrf68Z8qaBbZmoeUvWGjnGBmCAnE668BYlpasA4TKtxi6NhjuYs9Yqzli4pvYw3pocsBv5KOoJvIvvPqMIcit9xREcDaz6r_z2X7ei5xQr300L_Iq_iDjBOoYmKH5EXHR0ucTVrjjyf1j6Z9oadm_jE5xJ4rusgFtgjRmWiMdQI0p8J9AX04Y3bRg2AJPV9608rHKrFtTmheBhIUXPm_2sHl_LmM-ntmj6XTqmkHoVeRwJCissnpkjGdTXAkQphRqVEjcIC0QfVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رئیس‌جمهور شی، در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت — و این اظهارات شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، حرف او را باور می‌کنم و علاوه بر این، من نیز لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
همچنین، رئیس‌جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین جریان دارد (روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز برقرار است)، به من گفت که به ایران سلاح نخواهد فروخت. او می‌داند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را پرداخت می‌کنند و اینکه آن سلاح‌ها چگونه توزیع می‌شوند، هیچ اطلاعی ندارم.
بنابراین، دو کشور بزرگی که مردم اغلب در ارتباط با ایران از آن‌ها نام می‌برند، به نظر من، در این موضوع مشارکت نمی‌کنند. اگر چنین می‌کردند، برایشان بسیار بد می‌شد — و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77481" target="_blank">📅 19:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY-4vvgrgAkbmpH2nei6K04csTJkl2JYnUCYJM2ouyK1iAdlGGncAlQvX7JZN0epLLAj6Y1vDUHdO2TLutqUlmZVRUrPQscZYlPOyCRwZWWWcVGEIPAPNFF4sDiVZGEFTtmfXj3auJs7hvrKconG5UtuC2dXSfwX--mr_fVzrELZm-OlTzc80qcb2sm0tZMxbhToCvZPf_q4a2G3zgOH5JT51901RMEWhDJl3DYvJRyj2wTbfUitbf9vg_ns8apEuEsx52WKt7FJNIbM2mNvl_qwNM-MVKNKMGb-9jkPBmQs5S9GKqo1-CZOsTPtYm8nnnAhJuMzSnuaZRLsiNOgfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای اطلاع‌رسانی دولت روز جمعه دوم مرداد، با صدور بیانیه‌ای از اقدام سازمان صداوسیما در سانسور بخشی از سخنرانی مسعود پزشکیان در روز ملی صنعت و معدن، درباره اجازه رهبر پیشین جمهوری اسلامی پیرامون مذاکرات، به‌شدت انتقاد کرد.
در این بیانیه با اشاره به سوابق مشابه، از جمله پخش نیمه‌کاره مصاحبه رئیس مجلس شورای اسلامی، سانسور سخنان رئیس قوه قضائیه و پخش نشدن مصاحبه‌های وزیر امور خارجه در طول جنگ، رفتارهای صداوسیما «گزینشی و مبتنی بر سلایق سیاسی یک جریان خاص» توصیف شده است.
شورای اطلاع‌رسانی دولت تاکید کرد این اقدامات وحدت‌شکنانه دقیقا پس از پیام رهبر جمهوری اسلامی مبنی بر لزوم «وحدت کلمه» صورت گرفته و نه تنها شایستگی این سازمان را به‌عنوان «رسانه ملی» زیر سوال می‌برد، بلکه تهدیدی برای امنیت ملی و انسجام اجتماعی محسوب می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77480" target="_blank">📅 17:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pHJ35F6oUkq6US_e2dE_n9IcCVvaiHr3Djkzavcvt6KgRYkRWHI6SbA_cHRML0J3Q-9RzteyDxJJ7OtZzkqKKfoQiwEoxYgSgpRXuRVoB7rlCbe36RoitapN6-w9zi377fZRZE_GGPWqg0rFImHMEE_PLLksauMyuf-poM_N1ce2BdsN3lneJRCWSNFtst2It80VI0SNaZz0JG2Cvvo4oHnAZUbZ76gMoneUkZQj6TW68gKaAqv8yxi5aC1GPOf9JlYLwGLHFkdWtK5p3FZzBx6bc_Gwqea7zuo0PyHUJEXFuqLZqyoefev273opyR-uC01hc1avDTTxfgVeetSffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین (شاهان) علیزاده آذر، زندانی سیاسی، با اتهامات سنگینی مانند «توهین به رهبری»، «تبلیغ علیه نظام» و «سب‌النبی» به دلیل «توهین به آدم و حوا» روبه‌رو شده است. او دی سال گذشته نیز بازداشت و به «تبلیغ علیه نظام» متهم شده بود.
این شهروند ۳۸ ساله و مهندس نقشه‌بردار، با قرار وثیقه آزاد شده بود اما بار دیگر در ۱۳ تیرماه مقابل منزل خود در اسلامشهر به دست نیروهای امنیتی بازداشت و به زندان تهران بزرگ منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77479" target="_blank">📅 17:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77478">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZTh4ZtRKJ-2N-Myj47ReTeeQE_vqR-sklU18eKixVi9bmxTC7W0-qe-Xui5xnZbdbLAAiyWWSrlxAyyp50MDtrAJxLRcg6FVZmq2woZut0TBS9JcN44jNj2jA4ja454U6nZ4WNMj1zbldJ7BGOEbcFYE4Gws6FhYXwOOgaRjXxBIz4J9Q8m5njXGN0r66yyaR4OU9DgIYYsAwWx9brVtogzXg6XSpHr2sf_C9JFtAJQVzaIr4m2ehoabn0hFiFOMzxrMXkwfAp0dC1C9ttF9tgcQl-Bwr687kQOwUcSFmXhlL8gRFXaGvCMmlViftWci8Gd8G3GlQ4AjppE5J1O5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی وال‌استریت جورنال روز جمعه دوم مرداد به نقل از «منابع آگاه» نوشت که دونالد ترامپ، رئیس‌جمهور ایالات متحده، در روزهای اخیر نسبت به این‌که مذاکرات با ایران بتواند به صلحی پایدار منجر شود، بدبین‌تر شده است.
یک مقام ارشد دولت آمریکا به این روزنامه گفته که «ترامپ معتقد است تنها چیزی که ایران می‌فهمد، فشار نظامی است» و افزود او در برابر تهران در «حال و هوای انتقام» قرار دارد.
این مقام همچنین گفت رئیس‌جمهور گزینه‌های مطلوب چندانی جز ادامه حملات نمی‌بیند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77478" target="_blank">📅 17:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77477">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbI-SOQtQjbKtCDQ5K5FUPvyqz_iNkpf69BzT5oeYE3LcSHNhPmsTtUx2zss62u37g0qOEJSMXTmQ-5vRuI3tDC9pz2jyssOxz7eqHW9hlF-I7jUGdOWE1Taf3vONJWjyUhbmXLKQVAhNFd8EELQSeLQPP1Wkaz3bdaOn-rBNIjVff7P0ZNzKcSPxzKxe91akMlqjv9c2ynwkPRZ0vjLuiYZ2LmLI9nxpHCs5EXl57OLRpmEblVaRdGtJfaKS1UbQXpuCkI81RLLWuP6jXIZf_OpqQ6_2VlS_31QoHwA_eD-5IdXJ_zghSCcjrCUhvBBqPc5GOF_DZ0PAzzdcDAtUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا اعلام کرد نیروهای مسلح آن برای حفاظت از کشور در برابر هر حمله‌ای آماده‌اند.
این موضع پس از آن بیان شد که سپاه پاسداران انقلاب اسلامی هشدار داد نباید به بمب‌افکن‌های آمریکایی اجازه داده شود از پایگاه‌های بریتانیایی استفاده کنند.
سپاه در بیانیه‌ای در روز پنجشنبه اعلام کرد آمریکا از پایگاه فرفورد در جنوب‌غربی انگلیس برای انجام مأموریت‌های بمباران علیه ایران استفاده کرده و افزود هر پایگاهی که برای چنین حملاتی به کار گرفته شود، هدفی مشروع خواهد بود.
اندی برنهام، نخست‌وزیر جدید بریتانیا، هفته گذشته در جریان این خبر قرار گرفت که لندن بار دیگر به توافقی با آمریکا برای استفاده از پایگاه‌های بریتانیا در چارچوب آنچه «دفاع جمعی از منطقه» خوانده می‌شود، رسیده است.
یک سخنگوی دولت بریتانیا گفت: «نیروهای مسلح ما آماده‌اند از بریتانیا در برابر هرگونه حمله‌ای، چه در داخل خاک کشور و چه خارج، محافظت کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77477" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isr867rpiGGe_HUmn5wqc5Cw51In6KwE3A8011eirJK7hAkw0e7HEaL4Czs_CdY2GfSOUrE06gdrFcgG4LrzwmRu4ggBmvugwP6Rfa_i0yvn-j4P6jdtwSS-nWNhzaRiZKRgz5bm2ZlMjWXiJPreesw3BovuYsrAqYsytGohwGm3VMmyE1jrgfJ3yYMCtS09PAHenlSTFEQn0a-pzys5fg6qLc8fXWe-U8aAo3dMx_R5nlDQ7PSlNl1nshumivnKWMq-KOgWF-e-p_nwnF_Mb_7XqB4zfjlrWJPsU1Jxixs0ndEPN9U4GLWD-qUYJNSP6oWtJRwlAKCPVp0uG6evFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران روز جمعه ۲مرداد۱۴۰۵ با انتشار بیانیه‌ای مدعی شد در جریان عملیات موسوم به «نصر ۲»، ساختمان باقی‌مانده مرکز داده‌های شرکت آمازون در بحرین را هدف قرار داده و منهدم کرده است.
سپاه در این بیانیه ادعا کرد مرکز داده آمازون نقش اصلی در تکمیل اطلاعات ارتش آمریکا را بر عهده داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77476" target="_blank">📅 17:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KXFXpok2ju5uR7bS6aYgbqu9LwJ7ErTjoaIES8LgIBmz0OMfVdEp8VbDlMrNgZJIjt8kvMMlUHlVp9fEv_YVeJERW8pjVwC4wz5Y5_V8wB8Gd3hz9fAfByMETrrqhgU66HbifrWwKTFVnH9Qx-Hk7WGqP2DVFCPf3k6mlAATNgG5Wk13x8LGhUkeUlbpFpkU4ljzWIfdvM51FYneR3Zfwpa09QPDBlESpkkOXY7-vWsqMJH0a3a9BdF-uN5TUBVurwtxm2jLOdpi1Rv9_eObDA5hgdLd-ZEuuoI8PuRW8FeoFvh5qeFkn-NdDX5TBC3845s_ioWC0qLjrKYDKlYwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ciidpV-4fDlCvjPH7iQLqIM7UNMrJWuzTZMX4o-UwedjtJjhtHhBqCIY3_C74nilbqeryXyHtb_efMPbQwQfP-TnSyhJhRla_Nl1gTN5X8BewkIOMm-DdjhkWK3gg4fn-mZiD9G-lA3tXgwbTH7FJu6oXYaUfzqQ1-_IrPUxd1PwX87jl9k7gC6oRepNDyg_OZGvz0IBHlJUZx42u8LeHIPPY8iIOI-UEMR_4megAgoux38dWNPKBnMYMxqVYnTYyK6PbCsHpOO2bqxahpD3j3_9LnZUE5LJVuvQSHF7TjQw3MxkFL53jSaIOAMXS-Y3vQexNM9KE9XDxH_D7wjDWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه نیویورک‌تایمز به نقل از چند مقام ایرانی و عراقی گزارش داد که جمهوری اسلامی ایران پیشنهاد آتش‌بس از سوی دونالد ترامپ، رئیس‌جمهور آمریکا را رد کرده است.
بر اساس این گزارش، پیشنهاد یادشده در جریان سفر علی الزیدی، نخست‌وزیر عراق، به تهران به مقام‌های ایرانی داده شده بود.
آقای زیدی در جریان سفرش به ایران از جمله با مسعود پزشکیان، رئیس‌جمهور و محمدباقر قالیباف، رئیس مجلس شورای اسلامی دیدار کرده بود.
جزئیات این پیشنهاد آتش‌بس مشخص نیست اما مقامات ایرانی به نیویورک‌تایمز گفته‌اند که این تنها پیشنهادِ روی میز است و آن‌ها علاقه‌ای به توافق موقتی که مسئله کنترل تنگهٔ هرمز را حل‌نشده باقی بگذارد، ندارند.
@
VahidHeadline
دفتر نخست‌وزیر عراق گزارش روزنامه نیویورک‌تایمز مبنی بر انتقال پیشنهاد آتش‌بس آمریکا به ایران از سوی علی الزیدی، نخست‌وزیر این کشور، را تکذیب کرد.
دفتر رسانه‌ای نخست‌وزیر عراق روز جمعه دوم مرداد در بیانیه‌ای اعلام کرد ادعای مطرح‌شده در گزارش نیویورک‌تایمز «کاملاً بی‌اساس است و هیچ ارتباطی با واقعیت ندارد».
دفتر نخست‌وزیر عراق در بیانیهٔ خود مشخصاً گزارش مربوط به انتقال این پیشنهاد از سوی آقای الزیدی را رد کرده و درباره وجود یا عدم وجود پیشنهاد آتش‌بس آمریکا به ایران توضیح بیشتری نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77474" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=c_Jm80xOHDFmyh_wgeeIBWgbBGAmdt9AS4py5jmizbLPHBLNdWDMrOHR_1Czk5hzkQRTJFksqlQ-zGAVT1U_KYfdNua7rIxEgtbHtCnmcxgOTOHg0qg92N5S1jBsaT2wH-4MMu1rfGbny7bfdJcZO3gBEJspAK2WqfhJgGIxzlwE2y_hqWN32bZJQaEkkTdbvJHR-TDH-XMVmIIQYrKu-wbFizqX9PvcpmTfQ1D93kG5JHP5a0opZnfJkfaho0M3deE_qxxh2Ax3xhKCfa6AlF3HTVS7XDvOVOojT4RdqdyzY6exqfLErlsd3NkJrcn4D5gItcp0qqi-1XVIeTWgqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0055dbc0e3.mp4?token=c_Jm80xOHDFmyh_wgeeIBWgbBGAmdt9AS4py5jmizbLPHBLNdWDMrOHR_1Czk5hzkQRTJFksqlQ-zGAVT1U_KYfdNua7rIxEgtbHtCnmcxgOTOHg0qg92N5S1jBsaT2wH-4MMu1rfGbny7bfdJcZO3gBEJspAK2WqfhJgGIxzlwE2y_hqWN32bZJQaEkkTdbvJHR-TDH-XMVmIIQYrKu-wbFizqX9PvcpmTfQ1D93kG5JHP5a0opZnfJkfaho0M3deE_qxxh2Ax3xhKCfa6AlF3HTVS7XDvOVOojT4RdqdyzY6exqfLErlsd3NkJrcn4D5gItcp0qqi-1XVIeTWgqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون سیاسی و امنیتی استاندار گیلان از حمله موشکی آمریکا به مقر نیروی دریایی سپاه پاسداران در زیباکنار، در صبح جمعه دوم مرداد خبر داد.
باقری گفت: «حدود ساعت ۷ و ۳۰ دقیقه صبح جمعه، بخشی از تجهیزات مستقر در این مجموعه در حمله موشکی آسیب دید.»
معاون سیاسی و امنیتی استاندار گیلان همچنین افزود بر اساس بررسی‌های اولیه، تاکنون «هیچ‌گونه گزارشی از تلفات انسانی» دریافت نشده است.
@
VahidOOnLine
مدیرکل مدیریت بحران آذربایجان‌غربی اعلام کرد حوالی ساعت ۹ صبح جمعه ۲ مردادماه، یک نقطه در شهرستان پیرانشهر هدف حمله هوایی آمریکا قرار گرفت.
پیشتر اخباری از حملات هوایی و موشکی آمریکا به اهواز، قشم، بندرعباس، تهران، امیدیه، اندیمشک، خرم‌آباد، خنداب در استان مرکزی، نایین در استان اصفهان، تفت و شیرکوه در استان یزد، فیروزآباد در استان فارس، کنارک و زیباکنار منتشر شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77473" target="_blank">📅 17:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77471">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivGctZHATi1gjNNNZR6BKsr_wCZHXURApLYsNM29lyzNSOMPDSCJd1d1F0J55zqmruz59AibKwEzTCQPqy7apCphjz64E8DQHNaA0JF-n7y8ZenZeHNINNYBKiYIuFN5yYLAUKB2GpinEc8KXYrfz-A05wNJlL8QlXQSZ_Bkhq5j3HSD6NtUGBY0-kdI-MMRFiPODpJQ7fRysvHz9qS46jTHsEzdb20yFM5jylhKAAYXHL9E3DEAkjzswhR8AExsje8nM8B1kFVmy3hM7yCc-hqabfKaEpHY9a5jAb68YO3LhlpqUlQpUV89Gqdvq2jjbpAn_MjAgyhSc3ogroYHtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHm533aklJtO4NDua1jOVYPlZKxKHO7jQdw-XtFaiNcl27YKAt0eWM1DJXu2HBfM4xQUI_JgdaccGWbxd8WONvpTVyx92Qei9-1_AG-sD5B4X9BwqXiIetXiDUSF9dxWwx-9R1POc3u2ihW2oe-ftsn0hnvbyxB1owiEEh_P-sJ0LMbNVw5a-0HzpgqChXpC_6PZ5pi6j_xF5-jq7_VIgKL-D3NaMfOpIhkMBz2-Cfv7u2T7eS-kXLPWLAl8z42qDV-0QTU0iFV_zJoqzvcdqSl4erwZ8W_Gr6mllj3I1Jub1gSlW69AK9OGT0lyfKB6CQ20PFneKul3x_yCztB-jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عفو بین‌الملل روز جمعه دوم مرداد از مقام‌های جمهوری اسلامی خواست که فوراً هرگونه برنامه برای اجرای حکم اعدام بنیامین نقدی، ورزشکار، را متوقف کنند.
بنیامین نقدی ۱۳ دی‌ ۱۴۰۴ در شیراز در ارتباط با اعتراضات سراسری بازداشت و به‌مدت ۵۳ روز به‌طور قهری ناپدید شد.
رسانه‌های دولتی ایران یک روز پس از بازداشت و پیش از برگزاری دادگاه، «اعترافات» اجباری او را پخش کردند.
این ورزشکار بعداً در ۲۲ اردیبهشت امسال به اتهام «افساد فی‌الارض» به اعدام محکوم شد، با این ادعا که از کپسول آتش‌نشانی علیه نیروهای امنیتی استفاده کرده است.
عفو بین‌الملل می‌گوید که حکم اعدام برای بنیامین نقدی پس از «محاکمه‌ای به‌شدت ناعادلانه» صادر شده است.
این نهاد حقوق بشری با استناد به الگوهای پیشین مقام‌های جمهوری اسلامی ایرانی در گرفتن اعترافات اجباری «تحت شکنجه و سایر بدرفتاری‌ها»، ابراز نگرانی کرده که «اعترافات» بنیامین نقدی تحت اجبار گرفته شده باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77471" target="_blank">📅 17:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KMwhDeJf2WJHHSDbKx3vIVNI6Et8lcsPLs6yetjCruNbu9wouQTfa4Ks8kVRPPLNT6jqs8Li6vTfAlqP-julqINifbjX_xP2aUj_-rAwty9MkmMLjuzYSH5XCZAztLKOtCj1UYTTcOPw5KmNZD-5xEEOyobXVOapEjhonQdYfKPQ-w7MvxGFUq7kVGCa2xDSCpWQaq1Hw0a8Yd_kyakkba_Ciqkzdga6J-akANQEkuBDFHss_CS71PJnDmt2c-PwAovEFgdjndvRHQ4J_rMYTkyQLGQgBf7IFEeNREj5QWtrM98SZIctCVyKi0IvJ0WOateM6SZ1vZvkV5sRrz8xCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته بود:
از این پس  خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
واکنش عراقچی، ترجمه ماشین:
مصادره دارایی‌های یک کشور دیگر برای پرداخت مطالبات نامرتبطِ آینده، بدعتی آتش‌افروزانه است.
کسانی که از چنین منابعی استقبال می‌کنند یا از آن سود می‌برند، باید به یاد داشته باشند: وقتی دولت‌ها مصادره را به امری عادی تبدیل کنند، دیگر دارایی هیچ‌کس در امان نخواهد بود. هرج‌ومرجِ متعاقب آن نه زیبا خواهد بود و نه مسالمت‌آمیز.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/77470" target="_blank">📅 06:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lkk6Z1w-QXX28PkEEjsjw0se_iiHZV448YWsPiqn6KWHEG8Np6Sl_dVkd63ICu-E30NN-w_qOZXYNFJIEn3shH91yXi8WzzXTpV3DiUGvMf6m6O20wLuEp5Xc-IgJEoa6r_AWUH9KBuILbyHi7gJvSgZ_0tq3RQAdjOw273QGD8ptU5guSGd7JnO5neRbreKZvtS9PwDQqF6e0nKOsgfZvIIl24hSs6ULlDK95iTMcNMYa8VcDYJcMB9kmkBC5KoVPT0AFSncO6cQG7ou4PcqBUgSqcsqolsfUSzGk2kJXtCyhQ53xQQ5TQNkWA17wJiTxnQSfcVLD3he7cJhpRqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E07-YSr-w-5uNB-emvfEqISJ_HHlnAuKGY-HzRc-_UEXxoAuuSto88ht4SBlLSd65Kc8aXHe1GwNovcvb72EJ5bNScYmVT8epFIAo6hRTTk0nNnE39OTeZHl-QALOnUgymM6dGellFAeArP-Cp3PYbOLElCrfmJ50XVYdSw0w1dyzAR1Ieg4mxiqcXtnpCJpGoLAyfRfvdkWNbn7mMeo27nGWFgm6QtVW6OKizHeDJztWz5DhPgB6nquvfVXHh1zbOELBGBA5df23rNL54Q_DFGAnO5Xe12ceHcOBVn7mn4ruFH92SWylSZTMazNh34Zh7dibxk6EvoYnw0M_tbvVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d0pwI26eWHz9sB_5PtaBtVn7deFdL8oCv6c-0-T0kmzRAk3stJIoQl4d2N8RanrMXbhqqnpUbAKV4YO7pugb3ceCQ-wmEL1IPusgB8eNX1eKPSaRce7vjKn6X7rIUEjtMA9uliSvzTxuF7F09BNvGKNu7F3YPLtIYLc-813r8cgpeNicpkMigT5HBZTXm23_a2h4XNvBZsiMYPP0xR6A7lEmPxxUd5daWEjGkX3kKnTcEMpRP6uKUL64Jb3baMnoEAjvItD5WVsCqmohvyKSBg_k7nCNOVbEJxYHb1EJxXS2qpDnEBN6VZ5P11ktpLm1UMrsJfSbUyyOP3fEd3-nbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CADR-VqYwmZciM6WiTbY3mDdlUz8TJa5DYSZmH26OEtiIWovJXeg-AKKDZHT5SEssdiuMFzK-gyIYefEYo0ZQtUgzLAc4SEjl7DuRG_KtvfIa0kcnNtzAs8zmnm_baCdpvxzstKqAAVTBdHwlqLcBkCEcVAyteOHBZzgTTrx-f95bskCIYvjJUEGYZnxWFGbrgYZEOz7fqRJvEJen3M5yzUpzdEipRdKWy3JCzy_XUww7sVYUeZOG6xOTCMWHV8-ZGmCGDsiQWMqH9q4O6fYS0CDgtePx_zjcfvmciMrUUrfrR4AI3Eb5GtZvSos4VN1C2C0vJjjGYwRXXivAizdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qnDpCkFNjLE7QtOFEvqD-nsfuVLldDvKPkSVtItzTc7A8_-UlHbLGH0XNj15z4UyFLUd0trF1WDZaVyHjVqIZnBjqnaiGQZWv1oyqo-B_jbpWR5fSPEdQO9SvIjiLUaPAELZ75mO5jMImVvMs7QuD-n2EgABerSlnv9IUyfw9LS1fDKqPYEjmAE56rFual7ViHuoWoaXkmZPmzErUesy4Tly6Xygin9ptkKNfQRCBs_R0eDiq2WbnmuL8q4YftpwgxROYaFSZw8RgvjT6Uksh2KlXsQxt36_C6nKrzEcccLjPaI0nxRGDcowCECLL4se20l8BS_J0wANKz6mQGYx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QzDgEP01YzV4Vu9hwfyshZWp5IOVBM_zMaCU04YyGVsTiG-lHUFJuXoXvl4W8-HIWUaP9k-nqKpecITZSGBe3yV36bnawGkyfT7nBPLmkKILAg7YzrlMnjl0XC4BaytEuGvZxTQbgSUBhUZfgSgFVthmZld3B-Uqcoc_ruPFSYalKbIPIzZRj_nCoCGx1XNMHPPVMWc8dJUUEFsRoXyljPv1OdsqzW9oMLVUDXCQmcqnF4GeUsXYjh4RKWk6QbwqTs-tCuu3jf_yqMFtvfVwwQw5Pgi5yMpubEmnkGbRcwMbFuK96ybViE0bD9u68zbJPNE4kQ3Hms4FumhnAt8ldw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=pEfBng5YzuIwRymvtQpTvvf3PtvWJ7F9nj8nsFWGnqm8fMGKLXDuqflL6foZrwd39gzpOAmzhoYiYjbSQJNeEAMQpRr0Bs0_pg7CV8XLpHDhqRLHmcX5FYDQf6KS-xsfR9X0Wg12HYTBWZnWb66sE_HJZ6hv9sGSwm9UOrOAytrhrXlJ7w7-F79JpTEL53DvrGeQcTW8dIw6wp0ohgeR6IOM9N6dWDQBvclqERerhZ4ZNFaCfFpAAj5GGQe1_8EwD7bFUbRQohjtj-ndiDKahnNMq2HgjGN-gI8jtySCNVOcMUV0xgAMFkpxjqW_HRQ9CwrRf09OkcryLXHVlVkMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a1c04c15b.mp4?token=pEfBng5YzuIwRymvtQpTvvf3PtvWJ7F9nj8nsFWGnqm8fMGKLXDuqflL6foZrwd39gzpOAmzhoYiYjbSQJNeEAMQpRr0Bs0_pg7CV8XLpHDhqRLHmcX5FYDQf6KS-xsfR9X0Wg12HYTBWZnWb66sE_HJZ6hv9sGSwm9UOrOAytrhrXlJ7w7-F79JpTEL53DvrGeQcTW8dIw6wp0ohgeR6IOM9N6dWDQBvclqERerhZ4ZNFaCfFpAAj5GGQe1_8EwD7bFUbRQohjtj-ndiDKahnNMq2HgjGN-gI8jtySCNVOcMUV0xgAMFkpxjqW_HRQ9CwrRf09OkcryLXHVlVkMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: پرتاب موشک از بیدگنه، خمین، نجف‌آباد، شاهین‌شهر و...
تصاویر بالا و پیام‌های دریافتی از استان تهران:
همین الان از ملارد موشک زدن
همین الان ساعت ۵:۵۲ از بیدگنه موشک زدن
سلام وحید جان همین الان موشک از رو پرند رد شد
سلام همین الان 5:51 از ملارد موشک شلیک شد
از بيدگنه موشك فرستادن الان ساعت ٥:٥٠
شلیک موشک از بیدگنه ملارد ساعت 5:50 بامداد
۵:۵۰ دقیقه از بیدگنه موشک زدن رفت بالا
سلام وحید جان از [....] بیدگنه الان موشک هوا کردند بعد جنگ ۴۰ روزه این دومیش بود
سلام وحید ما فردیسیم همین الان از سمت بیدگنه فک کنم موشک پرتاب کردن و صدای شدیدی اومد و لرزید ساعت ۵.۵۱
5.52 از کرج موشک فرستادن ردش هم تو اسمون افتاد
اشتباه نکنم از بیدگنه
وحید جان سلام.  رد موشک از سمت اندیشه  شهریار خیلی صدای مهیبی داشت همین الان ساعت  ۵.۵۲
آقا وحید سلام ساعت 05:50  از بیدگنه ملارد موشک رفت
سلام. روز خوش از بیدگنه موشک فرستادن
جمعه دوم مرداد ساعت ۵:۵۳ شلیک موشک از [...] بیدگنه واقع در ملارد به سمت جنوب غربی
🔄
وحید جان همین الان دومی هم فرستادن ساعت ۶:۰۰
سلام وحید جان همین الان موشک از رو پرند رد شد
شلیک دومین موشک پیاپی از ملارد
از ملار یکی دیگه شلیک شد  6:00
دوباره موشک زدن از ملارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77460" target="_blank">📅 05:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=Q-YHED_tEqokgdbUIMHMeBz9aATqRLKK5z7_QG-Rg7cOiCsZv9N6IUVqr6V74N4mPhFDa0q0rU6Tnd6V42MxVwpqTY7nP16iHc8XfsTmMbE5piIDQsrkIvW5IgceDZeZxqgo3q1Qi5JNSned7I0z2Z_9QbAkCi5fHcAa3pMr-CxDxWNHvO8uEiW8shnBrijjIZrdYe89m3YlsZOM10UhAmXkk19zC7F1Fg1_dw5aInThaS-_R8T-G6jdF1leONbj6UVqwe1jhNTgKWIb9pEC5ZBTqPwfF0pYlqKnE_s_lOohwroAJw_-nLN3JgcD_FqLAU610N7ZUCCEIK87DOIVmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08e419bbe8.mp4?token=Q-YHED_tEqokgdbUIMHMeBz9aATqRLKK5z7_QG-Rg7cOiCsZv9N6IUVqr6V74N4mPhFDa0q0rU6Tnd6V42MxVwpqTY7nP16iHc8XfsTmMbE5piIDQsrkIvW5IgceDZeZxqgo3q1Qi5JNSned7I0z2Z_9QbAkCi5fHcAa3pMr-CxDxWNHvO8uEiW8shnBrijjIZrdYe89m3YlsZOM10UhAmXkk19zC7F1Fg1_dw5aInThaS-_R8T-G6jdF1leONbj6UVqwe1jhNTgKWIb9pEC5ZBTqPwfF0pYlqKnE_s_lOohwroAJw_-nLN3JgcD_FqLAU610N7ZUCCEIK87DOIVmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۹ شب ۲۳ ژوئیه به وقت شرق آمریکا [۴:۳۰ صبح به وقت تهران]، سیزدهمین شب پیاپی حملات علیه ایران را با موفقیت به پایان رساندند.
سنتکام مراکز فرماندهی نظامی ایران، تأسیسات نگهداری پهپادها، شبکه‌های ارتباطی، سایت‌های نظارت ساحلی و توانمندی‌های دریایی را هدف قرار داد تا تهدید ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری در حال عبور از تنگه هرمز را بیش از پیش کاهش دهد.
این آبراه بین‌المللی، با وجود حملات اخیر سپاه پاسداران انقلاب اسلامی ایران، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با پشتیبانی نظامی ایالات متحده همچنان آزادانه در این تنگه تردد می‌کنند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه در حال فعالیت هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77459" target="_blank">📅 04:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان همین الان صدای انفجار خرمشهر
درود خرمشهر صدای انفجار ۴:۴۰
خرمشهرو زدن
سلام وحید خرمشهرو همین الان یه موشک زد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77458" target="_blank">📅 04:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
سلام الان یزد صدای انفجار اومد
سلام یزد رو الان زدن
یزد یه صدا انفجار اومد ساعت ۴/۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77457" target="_blank">📅 04:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چند پیام دریافتی از فیروزآباد در استان فارس:
سلام فیروزابادو هم ساعت ۳:۴۵ زدن
صدا اومد فیروز آباد فارس خونمون لرزید
نزدیکی فیروزآباد فارس چیزی شبیه انفجار رخ داد و موجش بد جور گرفت مارو
الان صدای انفجار فیروزاباد
ساعت ۴ صبح
انفجار مهیب
سلام  فیروزآباد در خونه داشت از جا کنده میشد
دوسه نفر  میگن پل احمدآباد بوده که راه ارتباطی هستش به سمت جنوب
آپدیت ۴۰ دقیقه بعد: صدا و سیما
شنیده شدن صدای انفجار در فیروزآباد فارس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77456" target="_blank">📅 04:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان ساعت 3:43 صدا پدافند شرق تهران اومد ولی کم بود
ساعت ۳:۴۵ صدای پدافند شرق تهران فعال شد. از حکیمیه صداش میاد
پدافند شرق تهران فعال شد
سلام صدای انفجار در پردیس تهران [لابد انفجار شلیک‌های همون پدافندهای ضدهوایی است.]
الان هم پدافند زد
پدافند پردیس فعال شده.
شرق تهران صدای پدافند
[+ پیام‌های دیگری که با تفکیک اسم محلات مختلف شرق و شمال شرق تهران دارند فرستاده میشن و دیگه نقل نمی‌کنم چون همین محتواست که هی داره تکرار میشه.]
آپدیت:
بعد از چند دقیقه تموم شد.
🔄
ساعت ۴:۱۰
دوباره صدای پدافند شنیده شده در شمال شرق تهران
🔄
ساعت ۴:۲۲
پیام‌های دیگری درباره شنیدن صدای پدافند در شمال شرق تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77455" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDodg53PoqwBb0PhPn9OqBBp8nqtQgFwFELp6tdP-p5JJaxEKphdYvvSnPDrv1FFY9xcg9MCCCnUGOvCCbzuSABDOLLwUMOvY8Bow3mS3_EP8KmQOQeQtXDcl31BzdvJHYNwEhVNbVVHZBMRn4L8tHAk40N7136xLbAStIx_B2H3fBzUIxOW5nDEW-1L33swRRGcODt07ZmfuOT8-whnVhUXCe8pQMEGcu1MTk3muOvKlhAx0eJQB1KZYeGdUFXY4HcjaD5PsYkqDUPHekiN81eqFQTDpFqg7hF3qca2D8h2eRXN8oZTrH6mhxnjw6nIq04YpoM3Il-zoLS_QDelwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: تفت در استان یزد
پیام‌هایی دریافتی و تایید نشده درباره مناطق مرکزی کشور:
ساعت ۳.۰۵ دقیقه شهرستان خنداب صدای انفجار خیلی بلند اومد
سلام خنداب و زدن 3:05
نزدیک خنداب صداهای وحشتناکی میاد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی گفت: یک نقطه در خارج از شهر خنداب دقایقی پیش هدف ۲ پرتابه دشمن قرار گرفت.
———
سلام وحیدجان همین الان پایگاه نیروهوایی انارک نایین را زدن
آپدیت چند ساعت بعد: منابع حکومتی
معاون استانداری اصفهان: ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
———
تفت از یزد هستم
از سمت بام تفت - شیرکوه رو بد زدن
خیلی صداش بلند بود
ساعت ۳.۳۰ دقیقه تفت صدای انفجار امد.
دکل تفتکوه رو منفجر کرد
سلام ۳:۳۰ تفت استان یزد صدای انفجار مهیبی اومد که از خواب بیدار شدیم. از کوه های اطراف نور و گرد و غبار شدید بیرون آمده.
داخل شهر نبود
سلام وحید جان .ساعت ۳.۳۰ تفت یزد صدای انفجار شدید اومد و خونه ها لرزید.
صدا از تفتکوه محل منطقه گردشگری در حال ساخت بام تفت بود که از اول جنگ کلیه نگهبانان و پرسنل را سپاه تخلیه کرده و هیچکس اجازه رفت و آمد ندارد
خبرگزاری‌های محلی میگن موشک بوده و جنگنده اصلا صداش شنیده نشده
آپدیت: صدا و سیما
صدای انفجار در خارج محدوده شهر تفت در استان یزد
———
بروجرد انگار زدن صدای انفجار اومد. دو انفجار پیاپی
بروجرد زدنننن
صداش وحشتناک بود
بروجرد صدای انفجار شدیدی اومد
دو تا پشت هم
آپدیت:
در بروجرد فقط صدای عبور جنگنده شنیدم
اما صدای انفجاری نشنیدم
از باقی همشهریان هم پرسیدم نشنیده بودن.
صدای جنگنده شبیه  جنگ ۴۰ روزه بود که بعدش خبر بمباران خرم آباد اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77454" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjFUMhOLqejkWUt54ZWeqUnYL09bJd_TQayrGjEH7W-ivFf2gKHKACNXNpv-XLtHTkhVCjuJPWeyfETdr6upx3h58oAD-bcTewGW8wSdm3ZklcfTQ7RJ3deVHO4H-yQQissaVtkMzCQDwjnxmRtI8Zz6JpqRSvjiMbos0TG--WjA0ZJaHwTfAW-AuBOun3Udv7IZzElqH67aDpQvbNdd7buBRS2Ql8JMcWXyVCARk1oqlrQhwuzyVqOzf8HtN6jFeIXSTF7gKkZxkysU3G8ntwV6wIQjvkHKWUsixbss2V3sDXE-MOpmxgwG3SRu0Aja5F-gW3E3MAIA4mZjmJAtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، معاون امنیتی و انتظامی استاندار خوزستان اعلام کرد که ساعت ۲:۵۰ بامداد جمعه، نقاطی در اطراف شهرهای اندیمشک و امیدیه هدف حمله موشکی آمریکا قرار گرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77453" target="_blank">📅 03:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیام‌های دریافتی:
خرم‌آباد ساعت 3:19 دقیقه صدای انفجار شدید.
خرم آباد الان انفجار شدید
همین الان صدای انفجار خرم اباد ۳:۲۰
سلام خرم آباد همین الان ساعت 3:19 دو انفجار شدید
سلام خرم اباد وحشتناک پنجره لرزید
خرم آباد زدن یه حالت لرزش هم داشت
خرم اباد وحشتناک شیشه هامون لرزید
سلام همین الان از خرم اباد موشک پرتاپ شد
آپدیت: منابع حکومتی
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان گفت: یک نقطه از شهر خرم‌آباد دقایقی پیش هدف پرتابه دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77452" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9wMmGXXvFijGWrdtpgw7poSOgHGUVFP2MVXTL7PsZpd7YrbbebtL5y48MzJlLwwbtbKR3rKQenGWyxQ_aM4fdNQLfY8zk6hCT57wQ1jsJEb0hXWk-W6XqRpEvZR6grvOhb9QdzlPU2PUaHZAIsVOkMvHqs2lELPDF9Eqed8aBmdsHZiqEplZuMyMnuQlKjsGDnDB8bBSOLlLznOVKfTJORSrN0RGLAO7g_DkxRP4hgCNCUxrtoi25IYnUD-ZKjGEUyqJ1UPt1ZFbWZQ6rx1dqRT25lGH8W98kU1eC3Ac3IiUvV-YgEhr5gRQQEt8-6QDNrwmEdLLX6fc3ZTTlAbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77449" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B4UuSJPL390DClB_yi7edZZLXgYwEwXMvMBI3f9FMiw6SByhJ-uzkwBsPAT351sVNfucV3jlRiaqK1p6uJmVm-5Wwc0roQe-8IOUP8z-MBiqE-Sejy0lafcFAymokvT08AJcNZVL07WPRnpqn9Hr8NN72iy8tzaXJAU0ANc3kwMZgMQGk5qvOcflGsLiqTTJsKjxkIsvSuQpKHpa8ChDEcXI7fVfaLLlZIIenNoE1Z32BgMZuJTrqPyYuEnMQznlRkDGO7msT8u5rvb4DvKz_wMlcivPhjm2xVVSugaGF7slkEAc2REH7-DK8z5nbJ5CDpjAjHFbmcAaZI9kj-RXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: سیزدهمین شب حمله را آغاز کردیم
ترجمه ماشین:
نیروهای آمریکایی امروز ساعت ۶:۴۵ عصر به وقت شرق آمریکا [۲:۱۵ به وقت تهران]، دور دیگری از حملات شبانه به اهداف نظامی ایران را آغاز کردند.
این سیزدهمین شب متوالی حملات است که با هدف پاسخگو کردن ایران و کاهش تهدیدهای سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77448" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=hidlKxNWHtd5k-wZaqNyLHTH2i7X3U8gQZSHkgg5TLDa39E-nQJNAXN3Y2ViY1ZeK7y6TRWy87-tenTRZ41TYix3cS0X9tNAgclah6nKfn5XVd92tXg45Zkw-ntftX2qG_Zj4Ru6Ba2qDncU4nXKzV4smqlinm7EQgLWYkpM-Nptq0t1YRglAZEsWEtpCsL7DU2reP79dwhXR65v08cPEbzkxQp6U_mpb_v5uXP745lodNa0mhez6pKQR8aHl7bswtNd33lDyyb1tz85rKUSUXIYWKUR4Ok1lonA_XZ35bAfotasUsmZCV-NKXMVPD2dLxoir1GEhM04hIFp-Dv62A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1bff03107.mp4?token=hidlKxNWHtd5k-wZaqNyLHTH2i7X3U8gQZSHkgg5TLDa39E-nQJNAXN3Y2ViY1ZeK7y6TRWy87-tenTRZ41TYix3cS0X9tNAgclah6nKfn5XVd92tXg45Zkw-ntftX2qG_Zj4Ru6Ba2qDncU4nXKzV4smqlinm7EQgLWYkpM-Nptq0t1YRglAZEsWEtpCsL7DU2reP79dwhXR65v08cPEbzkxQp6U_mpb_v5uXP745lodNa0mhez6pKQR8aHl7bswtNd33lDyyb1tz85rKUSUXIYWKUR4Ok1lonA_XZ35bAfotasUsmZCV-NKXMVPD2dLxoir1GEhM04hIFp-Dv62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
داداش
بندر
زد
همین الان
بندرعباس
سلام بندرعباس همین الان صدای چندتا انفجار پشت هم اومد
ساعت ۲:۴۱ دقیقه صدای انفجار بندرعباس
سلام بندرعباس انفجار های شدید پیایی غرب منطقه ۴
بندرعباس 2 انفجار
سلام وحید بندرعباسو زدن 2:41
بندرعباس ٠٢:٤١ يه صداي انفجار خيلي بلند كه مركز شهر  قشنگ حس شد
سلام بندرعباس همین الان چندتا زدن خیلی بدد برق قطع شد صدای انفجار بد بود
🔄
بندرعباس صدای انفجار بلند ۲:۴۱
2.42 چند انفجار بندرعباس پشت سر هم سنگین
3تا دیگه
٠٢:٤٢ سه تا ديگه پشت سرهم
صدا و موج زيادي داره
سلام وحید بندرعباس انفجار وحشتناک
دوباره داره میزنه خیلی بد میزنه
بندرعباس ۲:۴۲ صدای انفجار دی در پی
دوتا دیگه پشت سرهم زدن
۵ تا انفجار شدید  بندرعباس مجدد منطقه ۴ ۲:۴۳
سلام یه صداهایی میاد بندرعباس فکر کنم صدای انفجاره اما دوره
وحید بندرعباس ۲:۴۲ صدای انفجار بدجور میزنه
ساعت ۲:۴۱ در خونه دوبار لرزید
غرب جزیره قشم
بندرعباس همین الان هفت تا هشت انفجار خیلی قوی داشت
آقا وحید بندر خیلی شدید بود بیش از ۵ تا بیشتر.</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77447" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=ndNntxJW1XqMUjCEowQddVwwkVIn5vT8XmmwAAwGPVQLbPcDR_aH28GRd15uxjpPVOPyzo-nfHFlvKNvq3VbpJEzIou3H8k8Yd1DcV2bgFnWrPsapIqRrWMQfUEiXaHjZm56eYQ84iABmNmhVfdX9x11bASsHFPp4yHIQsRJmUIqhUupLWidy9I2zwKd8kXQ73lL_dQzAflA5B1NKGAqxQcrey0gOYfHDynEYytnJoR3TegrBjasTS9K4casoOBOmvzQRObAeFR4FDQBC2FtGYgNYkSQsfejQ3SHm26uoycA8qYLzgSANc6Tp5I_WsTzZclAn_cI-z2JnxV9cq_KEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab7e6ef3aa.mp4?token=ndNntxJW1XqMUjCEowQddVwwkVIn5vT8XmmwAAwGPVQLbPcDR_aH28GRd15uxjpPVOPyzo-nfHFlvKNvq3VbpJEzIou3H8k8Yd1DcV2bgFnWrPsapIqRrWMQfUEiXaHjZm56eYQ84iABmNmhVfdX9x11bASsHFPp4yHIQsRJmUIqhUupLWidy9I2zwKd8kXQ73lL_dQzAflA5B1NKGAqxQcrey0gOYfHDynEYytnJoR3TegrBjasTS9K4casoOBOmvzQRObAeFR4FDQBC2FtGYgNYkSQsfejQ3SHm26uoycA8qYLzgSANc6Tp5I_WsTzZclAn_cI-z2JnxV9cq_KEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌‌های دریافتی:
اهوازو زدن
شدید زدن
سلام وحید صدای برخورد اهواز
اول ۳ تا خیلی دور بود
الان هم ۳ تا نزدیک بود
اقا وحید همین الان اهوازو بد زدن
اهواز انفجار ولی دور بود
اهواز ساعت ۲:۲۰ صدای انفجار اومد
اهواز صدای برخورد اومد 2:21
وحید رگباری زدن اهواز
ساعت ۲.۲۰
ساعت ۲:۲۵ یک انفجار شدید اهواز
سلام وحید ساعت ۲:۲۰ اهواز رو زدن
داداش اهواز صدا انفجار قطع نمیشه تقریبا ۲  دقیقس پشت هم داره بمبارون میکنه یجایی رو
اهواز ساعت ۲:۲۱ خیلی زدن بیشتر از ده تا
۰۲:۱۹ اهواز زدن
آقا وحید اهوازو شدید بمبارون کردن هنوزم ادامه داره
ساعت ۲:۲۵ یک انفجار شدید اهواز
انگار یه چیزی خورد زمین و ترکید
انفجارش طنین داشت
چیزی مثل رگبار
انفجار در اهواز 2:25
سلام ۲:۲۱اهوازو زدن از گلستان اهواز پیام میدم دور بود خیلی ولی کاملا صدا و لرزشش اومد
سلام وحید جان، اهواز رو زدن
خیلی شدید بود ساعت ۲:۲۲
سلام اهواز شیشه ها کامل لرزید مثل یه باد شدید بود
🔄
ساعت 02:24 مجددا شروع شد.
مجدد ۲:۲۴ انفجار شدید
یکی دیگه دوباره زد
انفجارش موج داره
ساعت ۲:۲۴ یه انفجار دیگه شدید بود
۲:۲۴ دوباره اهواز زدن
وحید دوباره صدای چندین انفجار
اهواز هنوز داره میزنه
اهواز رو پشت سرهم دارن میزنن
درود وحیدجان، ۴ ۵ تا انفجار عجیب در اهواز رخ داد، انفجارهاش با همیشه فرق دارن، با اینکه دورن و صدای کمی دارن ولی زمین و شیشه‌ها رو میلرزونن به یه صورت دلهره‌آوری
سلام اهواز ساعت ۲:۲۴ دیقه فرهنگ شهریم صداش اومد هرچند کم بود صداش ولی مشخص بود بمبه
انفجار ها توی اهواز همچنان ادامه داره
خیلی شدتش بیشتر از روزای قبله
کل خونه و پنجره ها دارن میلرزن
اهواز زاغه مهمات انفجارات پی در پی
اصلا تمومی نداره
۲:۳۲
۲:۳۳
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77446" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FAJ7EJEnqR0YY0-Er_X_kUANgYLrFThnXzsu1H4Z0PUaNCS6BkacAsz0zxaot1uQwzboQFSUIgeGG9zMAw0_oT_LNbWVx-PO9H8F5lzsUL7ilbcwt5fu2ShrLns_lVqq2w8f869illOSzA51PltGoIwzTzlbe99kPnx_jWUtTHldYAjMoz3l4pytgFNNl0ujdCyRpHxG-mXg8ko4ODHUzSQdTS3YFrhH4srldDQqS1hac74ItYIV4FdIld5CWTNvadIue2Zi3bhcoQRbrf9l8GC5LC-cgV8uFvXIh4ncV5djgFsX1IKIuXoIhalXYZDD9B6KWzvLzgRbWdJDyiCtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: خسارات حمله به کشتی‌ها از پول‌های بلوکه شده ایران پرداخت خواهد شد
ترجمه ماشین:
لطفاً این بیانیه را تا اطلاع ثانوی به‌منزله اعلام این موضوع تلقی کنید که
از این لحظه به بعد، هزینه هرگونه خسارت واردشده به کشتی‌ها، محموله‌ها یا هر چیز مرتبط با آنها، از محل پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
این خسارت‌ها ممکن است بسیار قابل‌توجه باشند، اما با وجود این، این کار منصفانه و عادلانه است.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77445" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tWrEmRzwvBXkg0CA-vFX47l5s5PEei6kgvrejIMDf0spjUjhxgjvS57BuRRo73Vj9pOCboNYoQMBcVykwWwvMQAh--upFGu8OpumsssL7IwDvxwgpGIHtm4ezNG6_kLpbtpEhIMHmxS5OLFJs32KBv3F08h8RXNG-uCAQowrvEstMuP9R4b_-iuzubH2BtWcOKrNgNvIi0dAlkfRUsns4mjQI9SZ1StiOg6ukqepYTOWhIVgUSzocrn-DCNfCSkHEpM_JK2h6f1cLpDo7gAkCoTTK32xXlDC6XlCrIiFNYI0NfD6lW72CZz7x00VzFbj3rnh6z584newsYWr9zNQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم: اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم
گزارش خبرنگار تسنیم:
🔹
ساعت ۲۳:۵۰ دو فروند موشک در جریان حمله دشمن آمریکایی به محدوده روستای مسن در جزیره قشم اصابت کرد.
براساس اطلاعات اولیه، این حمله در محدوده روستای مسن رخ داده و دستگاه‌های مسئول در حال بررسی ابعاد حادثه و ارزیابی خسارات احتمالی هستند.
من یک پیام داشتم ولی اون رو هم ساعت ۲۳:۳۳ دریافت کرده بودم:
سلام وحید جان
ساعت 23.30 صدای دو انفجار شدید  ذوالفقار قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77444" target="_blank">📅 01:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77443" target="_blank">📅 00:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=ldA3KChSR1M_d-eDnJgPWIu-m4tUvr28glxfv8a7rkds7Oc6WhlK_W9csMOJrbDMSM4GMerezJoZugWnyv8YJJa31A2oA70ldpLS_H2ptuAG7PB91HdxBkUT4Eb74O8AfqbbNgvFvK2h4EmGFNZkTVVkTNvIqwWqMzwsto0qJBGgJKB0IGThCLD1Y4a9t-B8oe4gvUIbFKz4JMUIQpeT50J-_ihNcrNDhntMAxF7XnuEzmWYrqRAt403agjEpMaaAOqKHIjeBUrI12a8Qpf9nrN5bKgurdRr7MdZEkFfHz8a5rGgtDr6ZkDyf33UakKET-ZYPZ1ev2X_FpB-LAiaX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=ldA3KChSR1M_d-eDnJgPWIu-m4tUvr28glxfv8a7rkds7Oc6WhlK_W9csMOJrbDMSM4GMerezJoZugWnyv8YJJa31A2oA70ldpLS_H2ptuAG7PB91HdxBkUT4Eb74O8AfqbbNgvFvK2h4EmGFNZkTVVkTNvIqwWqMzwsto0qJBGgJKB0IGThCLD1Y4a9t-B8oe4gvUIbFKz4JMUIQpeT50J-_ihNcrNDhntMAxF7XnuEzmWYrqRAt403agjEpMaaAOqKHIjeBUrI12a8Qpf9nrN5bKgurdRr7MdZEkFfHz8a5rGgtDr6ZkDyf33UakKET-ZYPZ1ev2X_FpB-LAiaX4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش‌هایی مربوط به ایران، ترجمه ماشین:
ما در برابر جمهوری اسلامی ایران بسیار خوب عمل می‌کنیم. عملکردمان فوق‌العاده خوب است. آن‌ها دوست دارند کاری بکنند، اما من می‌گویم هنوز آماده نیستند. به مقدار بیشتری از همین رفتار نیاز دارند. هنوز آماده نیستند. نیت‌های شومی دارند.
نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند. اگر همهٔ این کارهایی را که درباره‌شان صحبت می‌کنم، از جمله کارهای مربوط به مراکز دادهٔ شما، انجام دهیم، مگر این موضوع مهم نیست؟ وقتی شروع کنند جوامع را یکی پس از دیگری نابود کنند، نمی‌توانیم اجازه بدهیم حتی به داشتن سلاح هسته‌ای فکر کنند. دقیقاً همین اتفاق در حال رخ دادن است. در دوران من هرگز سلاح هسته‌ای نخواهند داشت.
ضمناً، این کار باید به‌دست دیگران انجام می‌شد. تقریباً سه سال است که می‌گویند ۴۷ سال گذشته، اما این کار باید ۵۰ سال پیش به‌دست رؤسای جمهور دیگر آمریکا یا کشورهای دیگر انجام می‌شد. لازم نبود ما این کار را انجام بدهیم، اما ظاهراً اگر ما انجامش ندهیم، هیچ‌کس دیگری هم آن را انجام نخواهد داد. من انجامش می‌دهم و هیچ‌کس دیگری توانایی انجام آن را ندارد.
ما در دورهٔ نخست ریاست‌جمهوری من بزرگ‌ترین ارتش جهان را ساختیم. کمی بیشتر از آنچه فکر می‌کردم از آن استفاده می‌کنیم، اما اشکالی ندارد.
ونزوئلا را داشتیم. کریس در آنجا کار فوق‌العاده‌ای انجام می‌دهد. هزینهٔ آن جنگ را چندین و چند بار جبران کرده‌ایم. میلیون‌ها و میلیون‌ها بشکه نفت برمی‌داریم و آن نفت به هیوستون و لوئیزیانا می‌رود. خودتان می‌دانید؛ آن کشتی‌ها را می‌بینید که صف کشیده‌اند.
باز هم می‌گویم، هزینهٔ آن را بارها و بارها جبران کرده‌ایم و رابطهٔ بسیار خوبی با ونزوئلا داریم. مردم ونزوئلا اکنون خوشحال‌اند و نمی‌توانند آنچه رخ داده را باور کنند. بزرگ‌ترین شرکت‌ها و بزرگ‌ترین شرکت‌های نفتی جهان وارد آنجا می‌شوند و به شکلی تجارت می‌کنند که هیچ‌کس تصورش را نمی‌کرد.
ما هم سهمی برمی‌داریم؛ باید هم برداریم. آن‌ها هم سهمی می‌برند. بسیار جالب است که اکنون پول بیشتری درمی‌آورند. کریس ارقامی را به من نشان می‌داد. ونزوئلا اکنون بیشتر از هر زمان دیگری پول درمی‌آورد. ما هم پول زیادی درمی‌آوریم و فکر می‌کنم حقمان است.
بنابراین واقعاً اتفاقی بود که [نامفهوم]. یک جنگ یک‌روزه بود؛ یک روز طول کشید. مردم می‌گفتند: «قرار است آنجا برای همیشه گرفتار شویم.»
اما می‌دانید، ما ۲۰ سال در ویتنام بودیم و در آن جنگ هزاران و صدها هزار نفر را از دست دادیم؛ دست‌کم هزاران و هزاران نفر. سال‌ها در افغانستان بودیم. در تمام این جنگ‌هایی که درباره‌شان شنیده‌اید، سال‌های سال حضور داشتیم. این‌ها همان جنگ‌هایی بودند که من آن‌ها را جنگ‌های بی‌پایان می‌نامیدم.
اما این بار چهار ماه است که درگیر هستیم. دیروز روز بسیار غم‌انگیزی داشتم. به دوور رفتم. چهار میهن‌پرست بزرگ آمریکایی کشته شدند. این یعنی ۱۸ کشته در دو جنگ. حتی یک نفر هم بیش از حد است، اما شمارشان ۱۸ نفر است.
در حالی که در ویتنام ۲۰۰ هزار نفر را از دست دادیم. هزاران و هزاران نفر را از دست دادیم. در افغانستان و در هر جنگی هزاران نفر را از دست دادیم. در جنگ کره نیز هزاران نفر کشته شدند. همهٔ این جنگ‌ها سال‌ها طول کشیدند.
ما می‌خواهیم این را تمام کنیم و می‌خواهیم درست انجامش بدهیم. اما باید کاری را که برایش آمده‌ایم انجام دهیم. نمی‌توانیم اجازه بدهیم این افراد بسیار خشونت‌طلب به چیزی که می‌خواهند، یعنی سلاح‌های هسته‌ای، دست پیدا کنند.
[...]
بنابراین فقط می‌خواهم در پایان بگویم که حضور در اینجا افتخار بزرگی است. اکنون می‌روم تا دربارهٔ موضوعات گوناگون صحبت کنم. یکی از آن‌ها جنگ ایران است که باز هم می‌گویم در آن بسیار خوب عمل می‌کنیم؛ بسیار بسیار خوب. می‌گویم بهتر از چیزی که هر کسی انتظار داشت قابل انجام باشد.
نیروی دریایی و نیروی هوایی‌شان را از کار انداخته‌ایم. تمام رادارهایشان و بخش عمدهٔ توانایی‌شان را در زمینهٔ تولید از بین برده‌ایم. توان پهپادی‌شان ۸۴ درصد و توان موشکی‌شان ۹۱ درصد کاهش یافته است.
بعد روزنامه‌ای نوشت: «آن‌ها اکنون در موقعیت قوی‌تری نسبت به چهار ماه پیش قرار دارند.»
نه، این حقیقت ندارد. درست نیست. باورم نمی‌شود حتی اجازه دارند چنین چیزی بگویند. نیویورک‌تایمز نوشت: «آن‌ها اکنون در موقعیت قوی‌تری قرار دارند.»
آن‌ها ارتشی ندارند. نیروی دریایی ندارند. کارشان تمام است. ۱۵۹ کشتی داشتند که همهٔ آن‌ها در کف دریا هستند. ۲۱۲ هواپیما داشتند که همه از بین رفته‌اند. رادار ندارند. پدافند هوایی ندارند. هیچ‌چیز ندارند؛ جز اینکه خشن و باهوش‌اند و هنوز مقداری توانایی دارند.
اما چهار ماه پیش، باور کنید، بسیار بسیار قوی‌تر بودند. متوجهید؟ می‌خواهم خبر واقعی را به شما بدهم.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/77442" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
افراد نفوذی در دولت آمریکا سرشان را زیر برف کرده‌اند.
آن‌ها واقعیت‌های میدانی را نادیده می‌گیرند و به نظر می‌رسد فقط روی سال ۲۰۲۸ تمرکز کرده‌اند.
تجاوزگری بی‌فکرانه‌ای که از آن حمایت می‌کنند، تنها باعث خواهد شد رئیس‌جمهور آمریکا برای توافقی که در تلاش برای دستیابی به آن است، بهای سنگین‌تری بپردازد.
Compromised individuals in the U.S. administration are burying their heads in the sand.
They ignore the realities on the ground and seem focused only on 2028.
The mindless aggression they advocate will only ensure that POTUS pays heavier price for deal he's trying to achieve.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77441" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fonpghwvGUEQGK4gYNFp4cgiwsZk4qi2NXmcsJt_O9QVfKEKyWNltIFxVrFj7wY8ts0CaYTYglgVCwpoRA54PrGDbirjeO3ShtLM2-SJPB1w8bxooxTECURp0gmVFirE1navQAEmulNImIoRE8MG-7DE-ZjW6gO3MXnfYgnrXVOq74iAfTj9czYZbzPW0BaXBIGdh34d08c5I5gThJbL8EOax_nLMJQzUw0UnRz9K6NZaqyyRrSK2DzJhgvUVUXrzr4fF6iOABri6bKrbIc-rmqg-OkZFTYkpHVzVrkaUKIZGE0OljMYwrm7MtU1IR6R-Cf9OG23FfoJChQIkRF4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
هم‌زمان با پیام‌های دریافتی درباره پرتاب موشک از اهواز
آپدیت:
ارتش کویت پنج‌شنبه شب اعلام کرد که نیروهای نظامی ایران بار دیگر خاک این کشور در حاشیه خلیج فارس را هدف گرفته‌اند.
رسانه‌های حکومتی در ایران نوشته‌اند که هدف این حملات تازه پایگاه علی السالم کویت بوده است.
در همین زمینه ارتش کویت در شبکه‌های اجتماعی از جمله شبکه ایکس خبر داد که موشک‌ها و پهپادهای ایران توسط ضدهوایی‌های این کشور رهگیری شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77440" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=oUgdPonVJVfo7voCX42BomXsylebUUSoOsmIR_pVgeyG7sstQT7cGEiqz-VFxXZB8FAlISaUfer7H8ruGJIWYaWnOGyPYfqMU6RPvSAsozT7ROS6tGYGSOylMk5pTZPTPZzs0ZzXfmC_88wAAgYTOQDn5Jj2Qq4Y8PUVwKHBnGP-BjvHv8_JaTeb3TejVNOWK387UmKhwdMbX1mW5FBpAWnVLLaoVAbHBtAWcamcEa_0tyvOhp5okl6oG-bPJNoLs1bqkxoQ8c90ova_aIP9v9XAaVk8qckCaN8GN_ZNFdUOhEz-WHAdMTN5KWs4ChYwHNeluRpT2cp8a39mfhm8cGO621JauGba3jwfOf2gAPlZqKEECl3gwB3_MsjpjyJYhAiYVIpJ9xLqQtUmp32RoR3myw3LTLuvWpbk1fYpe383bU2tmfR6YYhAHaQL5cAaT8YFGxqyxdsQ9vxoAw7St0PVP0UguQJYav6woV00wR6k1ywiPFTQFZjadR_Z1VBxLVEwcTnWgXoyv4b7NwtcoXHOBZxt7Ez2LY8TroTTfiN8f-__XqK6KPxOtDZcPVQuenw_W8iQ6IcgV4ZeIMR1UfDAUGoCyjTfpFMi-Tb9BXjf-B0-El05Q5iahKl7QrHq-00myvi6VzYvTgpkHeFiTlTQvgX753tpXpnAzeJCxx4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=oUgdPonVJVfo7voCX42BomXsylebUUSoOsmIR_pVgeyG7sstQT7cGEiqz-VFxXZB8FAlISaUfer7H8ruGJIWYaWnOGyPYfqMU6RPvSAsozT7ROS6tGYGSOylMk5pTZPTPZzs0ZzXfmC_88wAAgYTOQDn5Jj2Qq4Y8PUVwKHBnGP-BjvHv8_JaTeb3TejVNOWK387UmKhwdMbX1mW5FBpAWnVLLaoVAbHBtAWcamcEa_0tyvOhp5okl6oG-bPJNoLs1bqkxoQ8c90ova_aIP9v9XAaVk8qckCaN8GN_ZNFdUOhEz-WHAdMTN5KWs4ChYwHNeluRpT2cp8a39mfhm8cGO621JauGba3jwfOf2gAPlZqKEECl3gwB3_MsjpjyJYhAiYVIpJ9xLqQtUmp32RoR3myw3LTLuvWpbk1fYpe383bU2tmfR6YYhAHaQL5cAaT8YFGxqyxdsQ9vxoAw7St0PVP0UguQJYav6woV00wR6k1ywiPFTQFZjadR_Z1VBxLVEwcTnWgXoyv4b7NwtcoXHOBZxt7Ez2LY8TroTTfiN8f-__XqK6KPxOtDZcPVQuenw_W8iQ6IcgV4ZeIMR1UfDAUGoCyjTfpFMi-Tb9BXjf-B0-El05Q5iahKl7QrHq-00myvi6VzYvTgpkHeFiTlTQvgX753tpXpnAzeJCxx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجریان فاکس‌نیوز، متن زیرنویس، ترجمه ماشین:
مجری:
بیایید نگاهی بیندازیم به نیروگاه‌ها و مکان‌هایی که ممکن است بتوانیم هدف قرار بدهیم. لوکاس، وقتی به این‌ها به‌عنوان اهداف احتمالی نگاه می‌کنی، فکر می‌کنی اول از همه کجا را ممکن است بزنیم؟
لوکاس:
خب، نمی‌دانم نخستین هدف باشد یا نه، اما نیروگاه دماوند ۴۰ درصد برق تهران را تأمین می‌کند. نیروگاه هسته‌ای بوشهر هم احتمالاً هدف قرار نخواهد گرفت. روس‌ها آن را ساخته‌اند و هنوز هم اورانیوم با غنای پایین در اختیار ایران می‌گذارند.
مجری:
چون، لوکاس، باید بگوییم که منفجر کردن یک نیروگاه هسته‌ای خطرهایی دارد.
لوکاس:
بدون تردید. میدان گازی پارس جنوبی هم روی بزرگ‌ترین میدان گاز طبیعی جهان قرار دارد. نیروهای اسرائیلی در ۱۸ مارس، در آغاز جنگ، آن را هدف قرار دادند و ایران هم با حمله به بخش قطری همین میدان گاز طبیعی پاسخ داد.
مجری:
اگر بخواهیم در همان تنگه‌ای که آن‌ها در آن به کشتی‌ها حمله می‌کنند پیام بفرستیم، آیا آنجا جایی نیست که باید سراغش برویم؟
لوکاس:
چرا؛ فقط سؤال این است که پاسخ ایران چه خواهد بود. دیده‌ایم که ایران تلافی می‌کند. تأسیسات گاز طبیعی قطر و میدان‌های نفتی امارات، نگرانی اصلی همین است.
مجری:
یعنی اگر ما یک نیروگاه را بزنیم، آن‌ها هم پاسخی مشابه خواهند داد؟
لوکاس:
بی‌تردید. تمام این مدت ماجرا همین مقابله‌به‌مثل بوده است. نکته قابل توجه درباره اسرائیلی‌ها این است که آن‌ها پاسخ‌هایی نامتناسب می‌دهند. احتمالاً یکی از دلایلی که اسرائیل دوباره وارد جنگ نشده همین است. ایران از اوایل ژوئن به اسرائیل حمله نکرده است.
مجری:
ارزیابی تو از شیوه‌ای که اکنون عمل می‌کنیم چیست؟ فکر می‌کنی پاسخ ما نامتناسب است یا می‌توانست نامتناسب‌تر باشد؟
لوکاس:
پاسخ ما نامتناسب نیست. نکته قابل توجه این است که نیروهای آمریکا، پس از آنکه یک پایگاه آمریکایی در اردن هدف قرار گرفت، به پادگان‌های ایران حمله کردند؛ همان حمله‌ای که سه سرباز ارتش آمریکا را کشت.
مجری:
پس این همان نیروگاهی است که ممکن است هدف قرار بدهیم. این مهم‌ترین مورد است. برویم آن طرف نقشه؛ اینجا «کوه کلنگ» یا Pickaxe Mountain است.
لوکاس:
ارزیابی اطلاعاتی آمریکا این است که ایران احتمالاً چند روز پیش از عملیات «چکش نیمه‌شب» در یک سال قبل، بخشی از اورانیوم غنی‌شده خود را از فردو به کوه کلنگ منتقل کرده است.
این محل بسیار عمیق‌تر از دیگر تأسیسات هسته‌ای است. همچنین اینجا کوه‌های زاگرس است و با سنگ دولومیت بسیار سخت روبه‌رو هستیم؛ بنابراین حمله هوایی به آن بسیار دشوار خواهد بود. این یکی از دلایلی است که شاید از نیروی زمینی استفاده شود.
در واقع، چنین مأموریتی برای نیروهای مأموریت ویژه ارتش آمریکا است؛ نیروهایی مانند دلتا، تیم ششم سیل و اسکادران ۲۴ تاکتیک‌های ویژه نیروی هوایی.
ریسک ماجرا این است که هیچ‌کس دقیقاً نمی‌داند داخل آنجا چه وضعی دارد. هیچ نقشه فنی‌ای از داخل کوه کلنگ وجود ندارد.
مجری:
درست است. همین را می‌گوییم.
لوکاس:
آژانس بین‌المللی انرژی اتمی هرگز به این محل دسترسی نداشته است. بنابراین با اطمینان نمی‌دانیم آیا سانتریفیوژها و اورانیوم با غنای بالا به کوه کلنگ منتقل شده‌اند یا نه؛ اما این محل زیر نظر است.
شنیدیم که رئیس‌جمهوری ترامپ گفت به‌زودی کوه کلنگ را هدف قرار خواهد داد. بمب‌افکن‌های B-1 را دیده‌ایم که از بریتانیا پرواز کرده‌اند و البته بمب‌افکن‌های B-2 از پایگاه هوایی وایتمن در میسوری برای همان پرواز دور دنیا که در عملیات «چکش نیمه‌شب» دیدیم، برخاستند.
مجری:
و نطنز هم هدف قرار گرفته، درست است؟
لوکاس:
نطنز هدف قرار گرفته است. فردو و اصفهان هم هدف قرار گرفتند. این‌ها سه محلی بودند که در عملیات «چکش نیمه‌شب» در یک سال قبل هدف قرار گرفتند. با این حال، کوه کلنگ تا این لحظه دست‌نخورده مانده است.
[جملاتی که در ویدیو هست ولی برای جا شدن متن در پست، اینجا نقل نکردم.]
مجری:
و حالا تا جایی که می‌دانم، این نیروگاه برق [دماوند] دو میلیون نفر را تأمین می‌کند.
لوکاس:
بله.
مجری:
و خارج از تهران قرار دارد.
لوکاس:
اگر رئیس‌جمهوری بخواهد پاسخی بدهد که تا حدی نامتناسب تلقی شود، نیروگاه دماوند را هدف قرار می‌دهد. باز هم می‌گویم، این نیروگاه ۴۰ درصد برق تهران، یعنی برق پایتخت، را تأمین می‌کند.
تنها سؤال این است که آیا می‌خواهید برق میلیون‌ها ایرانی را قطع کنید که با آرمان آمریکا همدلی دارند؟
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/77439" target="_blank">📅 21:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77438">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0fwlRFVcGtPYq04qfa3U6dDK7FMSkxVTkM-fiZlrs_-9hPtISamozmysXj2YifEVgrzkhC6k5-doUWKPexozyQ5etwk5fh_qToEzLEfFydvuAbn2gp6wNFtezycZYBRNBoZFGmZ9V6uQO94cx4ZfR6YYzpQewYuYdZz1MJnB_c35B0hj4wBju5bG8vcyuCQSMaiH3HFTwTkIRp-ar0JoYmgqE_FZfynKdsx6_8mWOcsnwqZIeREzN0hpMbzolmB2EHUFfcWAcYQH1eoyLhFUjFPajqYjeAawRkVANMn9H66yw0EsFcq-ndpQ5xEu8Mb6w0VxvGGG0V8teEqU1qESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش کویت عصر پنج‌شنبه اول مرداد اعلام کرد که یکی از گذرگاه‌های مرزی این کشور با عراق برای دومین بار در یک روز، هدف حمله پهپادی قرار گرفته است.
ستاد کل ارتش کویت با انتشار بیانیه‌ای در شبکه اجتماعی ایکس (توییتر) اعلام کرد: «گذرگاه مرزی العبدلی عصر امروز بار دیگر هدف حملات پهپادی دشمن قرار گرفت که خسارات مادی بر جای گذاشت، اما هیچ تلفات جانی نداشت.»
ساعاتی قبل کویت اعلام کرده بود که آتش‌سوزی ناشی از حمله صبح پنجشنبه، مهار شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77438" target="_blank">📅 21:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ng_hf7AM8c18ro_p10FmgsgxHizybNQac1Tf94r0AHwmDbVm0r3Xk4LxRDIeXImyAVpVOFyw_iplTHFbD2rQlLzFUr1Z8bn5r-nAlzg5FMLAMRP10otcdAYozQg8LE1Kkn50i1XDx59-nCDPud-5puDE-UedN3tlYDx0PXZAK7tCf9LUgtgYXw9nBdPWj1kT_Yc381XQcW1NOYU5VvtI2TNBkBBTlpxasdXo-Y8QZI7Lz_cTUGRiHX7w9tnw9-dz2ylf77NYOBjv6nS-zQIyWyZDTKLJAQzaY3AmgnZ-RnjIrFghBBfitrQK0WEYVxS_ixQG7Ag6yf1eiAj9d2vYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درباره
این پیام‌های دریافتی
:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد ساعت ۱۸:۵۰ عصر پنجشنبه در پی حمله ارتش آمریکا، یک فروند موشک به نقطه‌ای در ساحل شهر سوزا در جزیره قشم اصابت کرد.
تسنیم نوشت که بررسی ابعاد حادثه و میزان خسارات احتمالی از سوی دستگاه‌های مسئول در حال انجام است.
خبرگزاری صداوسیما نیز از شنیده شدن صدای انفجار در قشم خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77437" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMuZ4MKCYiOPXPiFdpMde5frOhECPUOILxdwv8BTJYwmP1rBXYqCDTdpFJfsdG8Ifrm32U_OTbT0U4kbcK_0c92hwT-sFz2ocwLR-7dDFuGBrlpoSMh9Y2NNVPtSnyacZbzzznYIV6VqsqYE50PbDP8XSph1xYVtpRttkXWXpqh-mKKyFS8QuKRJd-EMvcmi7npqM1-q4c-oqNe-m4XYwRX9-PRIG9lP2WcKwTOA_IBLVaeLDx52wDa3Rp634HngF6mHJ3o5j9kf8Dp6kQ--qNe8_KNXHjIcw73rawBWTNU-M3VR-jpZs5AzK4xh8Cdlth3cIPVBZSuHqSpq4aFk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز پنج‌شنبه ادعا کرد که پایگاهی را در خاک بریتانیا که بمب‌افکن‌های ب ۱ آمریکا از آن بلند می‌شوند برای حمله «هدف مشروع» می‌داند.
وب‌سایت اکسیوس پیشتر به‌ نقل از مقام‌های دولت آمریکا نوشته بود که ارتش این کشور در دور جدید حملات به ایران، روز سه‌شنبه برای نخستین بار از یک بمب‌افکن دوربرد «ب ۱» برای حمله به اهداف متعلق به سپاه پاسداران انقلاب اسلامی استفاده کرده است.
اکسیوس نوشته بود که بمب‌افکن به‌کارگرفته‌شده در این حمله از یک پایگاه هوایی در بریتانیا به پرواز درآمده بود. اشاره این سایت خبری به پایگاه فِرفورد در جنوب غربی انگلیس است که در حال حاضر ۱۸ فروند از بمب‌افکن‌های ب ۱ آمریکا در آن نگهداری می‌شود.
حال سپاه پاسداران در پیامی این طور نوشته است:‌ «هر پایگاهی که برای حمله به خاک ایران از آن استفاده شود برای ما هدف مشروع است.»
سپاه در پیام خود ادعا کرده است که در پی ازسرگیری حملات، آمریکا ابتدا با موشک‌های کروز از روی ناوهای خود در اقیانوس هند به ایران حمله می‌کرده، اما در پی خالی شدن انبار موشک این ناوها، به استفاده از بمب‌افکن‌های خود در بریتانیا روی آورده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77436" target="_blank">📅 19:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j6Fd8GQoMlVbGQ5HghenaL_JrSkDfxD5U3cwOvUxr2tIhxSXVUjv_jnGpvP9ZQgb18AW05DHr-_DyPM36174ys9HvQHhFYdrQrBtazFTIUK1acIlPNjpBF91qtHuBo3Qw_47apT0Cg0ukZRVV2znGfzFCOKPAAPxbVan3q7elcA45SQxPsgCZ_YjUEv7ZI6_3b5RaAeiR1dNM-Dy-k5j8KPHz-VKsXFjjrRRinUSSDXdBYXiVvU_Cmvy1_wPoIFsMbbKaJif5tA6k_QVMamxq0s7QYCsZB7H30W77qOAoqh2f1uEFx-2kox2H3CFLz7TvCrG6-B26hikQRkOdDHv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: ترامپ می‌گوید به تصمیم‌گیری درباره «حمله‌ای عظیم» علیه ایران «نزدیک» شده است
ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنجشنبه به آکسیوس گفت که به‌طور جدی در حال بررسی ازسرگیری عملیات رزمی گسترده در ایران است؛ از جمله حملاتی که از عملیات «خشم حماسی» بزرگ‌تر خواهد بود.
چرا مهم است: ترامپ در مصاحبه‌ای کوتاه اذعان کرد که چنین تصمیمی پیامدهایی خواهد داشت و تأکید کرد که هنوز تصمیم نهایی را نگرفته است.
ترامپ برای تصمیم‌گیری خود مهلتی تعیین نکرد. دو مقام دیگر آمریکایی نیز تأیید کردند که هنوز هیچ تصمیمی گرفته نشده و هیچ دستور تازه‌ای به ارتش داده نشده است.
تشدید تنش‌های کنونی تاکنون باعث شده قیمت نفت از بشکه‌ای ۱۰۰ دلار فراتر برود. بازگشت به جنگی تمام‌عیار در آمریکا به‌شدت نامحبوب است.
آنچه او می‌گوید: رئیس‌جمهوری آمریکا گفت: «من در حال بررسی یک حمله عظیم هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام شده است. به تصمیم‌گیری نزدیک شده‌ام. ما کاملاً برای آن آماده‌ایم.»
ترامپ گفت اسرائیل «اگر از آن‌ها بخواهم، ظرف دو دقیقه وارد عمل می‌شود»، اما افزود که برای آغاز عملیات تازه علیه ایران «به هیچ‌کس نیاز نداریم».
او همچنین گفت پیوستن اسرائیل به این حملات «پیامدهایی» خواهد داشت و تلویحاً به احتمال تلافی ایران علیه اسرائیل اشاره کرد.
تصویر کلی: ترامپ گفت ایرانی‌ها «می‌خواهند مذاکره کنند»، اما در حال حاضر آماده توافق نیستند.
او گفت: «هنوز به اندازه کافی درد نکشیده‌اند.»
دو منبع منطقه‌ای مطلع از تلاش‌های میانجی‌گرانه گفتند رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده را نپذیرفته است.
یکی از آن‌ها گفت: «داریم تلاش می‌کنیم، اما ایرانی‌ها همکاری نمی‌کنند.»
محور خبر: آمریکا طی ۱۲ روز گذشته حملات خود را تشدید کرده است تا حملات ایران به کشتی‌های تجاری در تنگه هرمز را متوقف کند.
ایران تاکنون هیچ نشانه‌ای از تمایل به تغییر مسیر نشان نداده و خود نیز حملاتش در منطقه را تشدید کرده است.
شورشیان حوثی مورد حمایت ایران در یمن حمله به کشتی‌های سعودی در دریای سرخ را آغاز کرده‌اند؛ اقدامی که تنش‌ها را در یکی دیگر از مسیرهای حیاتی انتقال نفت تشدید کرده و بازار جهانی انرژی را بیش از پیش بی‌ثبات کرده است.
ترامپ در حساب خود در تروث سوشال نوشت که اگر حوثی‌ها بار دیگر به کشتی‌ها در دریای سرخ شلیک کنند، «ایالات متحده ایران را مسئول خواهد دانست».
او گفت حوثی‌ها نیروی نیابتی ایران هستند و بنابراین «مجازات نظامی سنگینی علیه ایران و البته خود حوثی‌ها اعمال خواهد شد».
آنچه باید زیر نظر داشت: ترامپ جداگانه گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قصد دارد هفته آینده در مراسم وداع با سناتور فقید لیندزی گراهام در واشینگتن شرکت کند.
ترامپ گفت: «روابط با بی‌بی بسیار خوب است. اگر او اینجا باشد، با او دیدار می‌کنم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77435" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید قشم صدای انفجار
الان دریابانی سوزا رو زد وحشتناک
جزیره قشم ۱۸:۴۰
ساعت 18:40 دقیقه قشم صدای انفجار شنیدیم
وحید جان قشم صدای دو انفجار از راه دور اومد ..
🔄
صدا و سیما:
شنیده شدن صدای انفجار در سوزای قشم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77434" target="_blank">📅 18:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpY0aJ5aqVCwZOZaRjZPekArHV-DyhMMC6EG3bshhmRsWOj3SGUl7TgimbtQtRiIIgEzpS0qxDLxcuyW_O9C3CNBUM04Afqwkjo0WwUceyZFdRXinZOf4mqfF6C2sIdeZtH01tpFPrZ0r0Nb0R_IWOLqmaxesV-70hxN_CR5ePzML1DTKcAXhFuBqElCkrkvmeA0mMHXAQ2bPgXgiFZH8ksLNB9lRQRRPq0Rx2Cd3kKPNI0vDsu10NNo85bY0G1k4HUpp-LA6By-peGn7qcgW1iH0rmL7Em-005bHgAVopwYaCG81WGTKeUf9_mBIDG4KtFnXnlH1Bz12SrEoMp6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف، ترجمه ماشین:
می‌خواستند ایران را تنبیه کنند.
در عوض، خودشان را با قیمت سه‌رقمی نفت تنبیه کردند.
استراتژی ۱۰ از ۱۰
👏
👏
👏
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77433" target="_blank">📅 18:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwDT1hGBd-6VFedM-c5wQe5tnc3GEzR9XNb9oJFdwwhnT0UP7VqRNUDqkhJJYyMheELHq0-GIIwaV4r4CJ6YDJ31rA-p54j5i3fc9G1cWjdAOWrpBgP2uXwqoUz9Q0dJS22HQkOJ_uOzrxJhvgvZMzxtYHnxFFYzEVBYbYVyCJ4BteI8vynFTGgH_BZsfXYJo_UFPwAwFxSARrWUkStBxHXNvRGPgY8tKh8tvSj29Tx6z158NZlEKLw3oYi9OIZKD3k-HmEJjpAD5VWyo7R9luNlyDwQOSanPdM-TBG7WFMqnv1rAqYZ8W-QprQ0M9IyN2nVnqOWKfnnI5SDt5PS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ روز پنجشنبه اول مرداد، در پیامی در شبکه اجتماعی تروث سوشال با یادآوری حملات نظامی ایالات متحده علیه حوثی‌ها که سال گذشته انجام شد، نوشت: «حوثی‌ها از آن زمان و در جریان درگیری با ایران، رفتار مسئولانه‌ای داشتند، اما متاسفانه با تیراندازی شب گذشته به دو کشتی عربستان سعودی، بار دیگر دست به حملات زده‌اند.»
ترامپ هشدار داد که اگر این اقدامات تکرار شود، آمریکا جمهوری اسلامی ایران را به عنوان حامی حوثی‌ها مسئول خواهد دانست. او تاکید کرد که در این صورت، مجازات نظامی بزرگی بر ایران و همچنین خودِ حوثی‌ها تحمیل خواهد شد؛ گروهی که به گفته او، تا پیش از این حرفه‌ای و هوشمندانه عمل کرده بودند اما اقدام اخیرشان مایه «تاسف» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77432" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-_OlNKObbrdAaIfkD6BfxfwWj99PlcD9JS2FGPuKcdvQi410_szEzj38422G8XZiHIpTDByzzb-Rgj7CDAeI47OUm8au3vJFBkYusQOWb8defHnYxgoTDBPlP1jpSsDGAba-Qox-zge-5QuXt4MLowkwt98uLLI66rZYiEfxhhaX0k8CoU6wS7yQPBMBMA5gloZlHkKCJoJv_qzmuov9fAeLrpFkBSHMLyw8AzTGTd2q0nyfRH_MBaASYExJ28UdWMMKADFzDMn9ZjOIA0AP4KnRSL2I6QCbPRmTmfTtjb1ekgfqg8AToIfl9tw7pRI9CHJsRvTtbwuhM5IovVv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد امیرحسن اکبری‌منفرد، زندانی سیاسی ۲۷ ساله محبوس در زندان اوین، با حکم شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، از بابت اتهام «بغی» از طریق عضویت در سازمان مجاهدین خلق ایران به اعدام محکوم شده است. بر اساس این گزارش، حکم دو روز پیش به او ابلاغ شده است.
هرانا همچنین گزارش داد امیرحسن اکبری‌منفرد زمستان ۱۴۰۳ همراه با پدر، برادر و خواهرش در کرج بازداشت شده بود و سه عضو دیگر خانواده بعدا با تودیع وثیقه آزاد شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77431" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X3IktdRMO9wHf3_IeMpVhRFrMcqhzOtRTKhFGl1DeNCgNFtjz39PJQ12t883jTKwWMwbfIepKCf3OBFddyRkQkbQX-Ew62gIdHZBPB37g9vLYXcA4xun5XaljvZih2WScHINgaLcgyvsYThXsWAOn1-O2aOa6iTrByeedvd4FTvrM8-HMHIRSYSKp6i4keWAcF3Ke_DQvuTnl3AuBLanuQixxDs2a4hHFPzNiRHy9RXwcsEMJZUaco5n33jdpWmEkoUXWrIPj26uubHsS8iABKAOwdnPCHd5BjUA6PRiVRax-hvrXnST5TQATb8abwB3vhsQ2RgDUUSsaluXRPNIew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mk4pI1VwemPoqw1S0NXnzPyX9ih-368vKbDh7AUJGg4uyiiS-M_Ejj57yJjWnCPqrkp1WGXCnRQUcQY7EJkeKXwgxj2_Y3WlHhO48rkuf5hT5s4CKFgT5Z0dqRqU-zhWnaZSalUlgz1x5byx9wgh9-ZBqKS37-Ejw_afnsV5utt84cU1NPYochaAMMZtYwwEPYl3BQuVhlwoBeYS_RVdZW6HHRFufbDMxJlW_PZqvPW8DWGVDoqXXiCGtJOKIQ6x-CaHe4LEgu01LklKn3UU5zsQaguY9LpWesLvu-KlQ0VKGmqEPOgufwbouy3DqRRccY5vtKVoN0t50a32QHe4hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اول مرداد ماه، در پیامی در شبکه اجتماعی ایکس اعلام کرد توافق هسته‌ای غیرنظامی میان وزارت انرژی آمریکا و عربستان سعودی تصویب خواهد شد، اما این توافق مشروط به پیوستن ریاض به توافق‌های ابراهیم است.
ترامپ در این پیام با اشاره ناگهانی به «غیرنظامی» بودن برنامه هسته‌ای ایران نوشت: «توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال انجام است، تنها به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی و دیگر کشورها دارند، مربوط می‌شود. اما این توافق کاملا مشروط به پیوستن عربستان سعودی به توافق‌های ابراهیم است.»
رئیس جمهوری آمریکا کرد در این توافق «هیچ غنی‌سازی مواد [هسته‌ای] وجود نخواهد داشت» و آمریکا با تاسیسات هسته‌ای غیرنظامی و بدون غنی‌سازی مخالف نیست
@
VahidOOnLine
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل پنج‌شنبه اعلام کرد پیوستن عربستان سعودی به توافق‌های ابراهیم، تحولی تاریخی در مسیر صلح در خاورمیانه خواهد بود.
دفتر نخست‌وزیر اسرائیل افزود اقدام نظامی مشترک آمریکا و اسرائیل علیه جمهوری اسلامی و تضعیف محور «تروریستی» تهران، زمینه را برای گسترش دایره صلح فراهم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/77429" target="_blank">📅 17:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joifKXPKPu1rig7pm1wumcSiqQqYRO0CnDUqhUxjNIAlitzFBBgBMP2oLTj8wzv10skT7zgBdGyKr8muhphzcXFZKR86lDAgs_AxgDDLrOlKTL-NeDI00IVf6IHVfgWSoGpzVYpNiWb9E7p1XPV2Z2mT3CrUXYgAMkU1x3xrVCIjIlZOTj-uk2K3utj4nWQeyRwVf7v8FqcgYBO6Gi1CHljkE9wRmqSRQxtybEVlx63a_r_r2uKzulr2C78IGBcxDTc3drRG-RglCAZF5PW-xINQVpTilNkS9IoyAc7O3lsUG6l8ila0lS8szV36mPXQtLoG_Sbv7KMSi8H1ZFSNSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایلنا در گزارشی از ادامهٔ بحران کم‌آبی در زاهدان و برخی مناطق استان سیستان و بلوچستان خبر داده و نوشته است که شماری از شهروندان در برخی محله‌های این شهر با قطع آب تا سه یا چهار روز متوالی روبه‌رو هستند.
بر اساس این گزارش که روز پنج‌شنبه یکم مرداد منتشر شد، بسیاری از خانواده‌ها برای تأمین آب ناچار به خرید آب از تانکرهای خصوصی هستند و برای هر بار پر کردن مخزن خانه بین یک تا یک‌ونیم میلیون تومان پرداخت می‌کنند.
ایلنا همچنین به نقل از شهروندان گزارش داده است که برخی خانواده‌ها به دلیل ناتوانی در پرداخت هزینهٔ خرید آب از تانکرهای خصوصی، ناچارند چند روز را تنها با چند دبه آب سپری کنند.
محمدرضا کوچک‌زایی، عضو شورای اسلامی شهر زاهدان، نیز در گفت‌وگو با ایلنا با تأیید بحران کم‌آبی گفته است این شهر با کمبود حدود هزار لیتر آب در ثانیه، معادل نزدیک به یک‌سوم نیاز آبی خود، روبه‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/77428" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zsh_MOpO0gl_LdyzbpqtJ8Wc6HcWsMxASBepafhPeZFcT--rbCG1wcjXWJED4RTWDpiOxIeb02vOLkOeWsTqegm7x5H6tlNZykZwvWXBN74Nngv5sJroho_P46YfKrvk5QKHwGO21X3PGTUSQ0dY4AqUt602xqBxH_5Ddy12hXvSJrsYzXSwl8St-sP2N45fAtQ_V743hrEH33xs3aJIiXUUQ76e8q90WtFxpaJKRQH524rYiLbI4pY_abkiOBOImEaO8FYNKlmLtK2l1ZfTEmltJavmUd6o89pIaCQ7H84MOuU9cyQlweaCDQUI4DM8Zib3Q9wUIHo21GNLS7Ysmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما و خبرگزاری تسنیم، روز پنجشنبه یکم مرداد ماه از شنیده شدن صدای چند انفجار در شهرستان کنارک در استان سیستان و بلوچستان خبر داده‌اند.
خبرنگار صدا و سیما در گزارش زنده اعلام کرد، صدای پرواز جنگنده‌ها نیز در این منطقه شنیده شده است. به گفته این منبع خبری،َ انفجارهای روز پنجشنبه، اولین حملات آمریکا در طی ۲۴ ساعت گذشته به این شهرستان بوده است.
@
VahidOOnLine
من هم حدود ساعت ۱۰ صبح پیام‌ها و عکس‌های مختلفی درباره کنارک دریافت کرده بودم + کلی پیام از چند شهر دیگر درباره پرتاب موشک
پیام‌های زیادی هم از دزفول و اندیمشک داشتم که در اون مورد پیش‌تر اعلام شده بود قراره  مهماتی کنترل‌شده منفجر بشن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77427" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2nQzZfJukkqpd3ik09V87VAbJSyzy1B7VA-ZoNuRMJCL3cH98WhcYjvu1-ZXbW889yreR5avcNB8MkrLjppYjNoIRbZPjAVsvki3dNz7le7KGyq72FyUFFVRU5UEPkV9nwPGtKOyREZxIGSoHx0u51RPos5x98sJFKT--syda5QvVhGlAja-6a-70xud5pp-WSW1_hlaarL_8rSMnpDuHM6PH_Ca3zMz5C8dvVLp8NoA6_pDXX-ekKxJuOmBnhkpxRH4uWpAH5ga_Kzw2uUIKOS_IhhGKuIMGAxR-zPtt4Ysjnl4ylWx1w8xH4Y6gwM9KfHNqQzuMqSezBRICLtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماری
از داوطلبان آزمون کارشناسی ارشد در شهرستان‌های بستک و بندر خمیر استان هرمزگان به‌دلیل تخریب پل‌ها و بسته شدن مسیرهای ارتباطی پس از حملات آمریکا، از حضور در جلسه آزمون بازمانده‌اند. به گفته آن‌ها، با وجود اطلاع مسئولان از وضعیت منطقه، هیچ راهکار جایگزینی برای برگزاری آزمون یا انتقال داوطلبان ارائه نشد.
کانال تلگرامی «
دانشجویان متحد
» خبر داده است که شامگاه ۲۶ تیرماه ۱۴۰۵ و هم‌‌زمان‌‌‌ با برگزاری آزمون کارشناسی ارشد، پل‌های محور بستک–بندر خمیر–بندرعباس در حملات پهپادی سنتکام هدف قرار گرفت و مسیر ارتباطی این دو شهرستان با بندرعباس به‌طور کامل مسدود شد.
در حالی که حوزه امتحانی داوطلبان این مناطق در بندرعباس تعیین شده بود، بسته شدن جاده‌ها باعث شد هیچ‌یک از آن‌ها نتوانند خود را به محل برگزاری آزمون برسانند.
به گفته این داوطلبان، آن‌ها تا آخرین ساعات پیش از آزمون بارها با اداره راهداری و دیگر نهادهای مسئول تماس گرفتند، اما هیچ راه‌حلی برای انتقال یا تغییر حوزه امتحانی در نظر گرفته نشد.
این دانشجویان می‌گویند ماه‌ها برای شرکت در آزمون آماده شده بودند، اما در نهایت به‌دلیل شرایط جنگی و نبود تدبیر مسئولان، فرصت حضور در کنکور را از دست دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/77426" target="_blank">📅 17:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQDW8TvB_zFcwGrQFqEiHtuYBkbcL9mjya-Mi5fMZX1nDGaB7APpICH_0p9jCG9R6qKSCEjL90TXPq8SC4TgXhdZMPyDND4Y_gVp_lEt_7trFLh5nSKU3M2CjGJKEGm4jnjvKRAWrkskoW3Oy5wZDe_5Sg61iiNqhPQxkMYJLf1Ra_JKkUr2VazEESOns5auImEV6Of_f4nOMkyL2fOU5xERwVLXcXrYUFQsaL9fPb-f8VYM67cXc353nL2_jSQx-yXsVwFr1wNJR7dSLzxHR34b7ISn57uPLbZrYC4MK17CSZf-oMR8DZTWfJC-w0SU2UUv_KMa6KHQn1cPGxnmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا، در حاشیهٔ نشست آسه‌آن در مانیل، با تکرار اظهارات پیشین خود مبنی بر «آماده نبودن ایران برای توافق» گفت: «آن‌ها هزینهٔ این موضوع را خواهند پرداخت.»
مارکو روبیو روز پنج‌شنبه یکم مرداد گفت «هزینهٔ ایران هر شب بیشتر می‌شود تا زمانی که به خود بیایند» و افزود: «با وجود جسارت ایران، آن‌ها به‌شدت در عذاب‌اند و این رنج همچنان ادامه خواهد یافت.»
وزیر خارجه آمریکا در عین حال ابراز امیدواری کرد که حکومت ایران «احتمالاً به‌زودی» آمادهٔ توافق شود، اما تأکید کرد در حال حاضر به‌وضوح آمادهٔ توافق نیستند، «حداقل نه توافقی که حاضر باشند با آن کنار بیایند».
روبیو در پاسخ به سؤالی دربارهٔ اظهارات اخیر دونالد ترامپ دربارهٔ پرداخت هزینه از سوی ایران در ازای کشته شدن سربازان آمریکایی و حمله به کشتی‌ها در تنگهٔ هرمز نیز گفت سیاست ترامپ «سر در برابر چشم است و ایران هزینهٔ سنگینی خواهد پرداخت.»
وزیر خارجهٔ آمریکا همچنین با ابراز امیدواری نسبت به توقف حملات حوثی‌های یمن گفت: «امیدوارم آن‌ها تنش‌زدایی کنند، ایران آن‌ها را فریب داده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/77425" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc7VCEl7Nd0xpO_Ey_tgaOmPd_vYtagES_G6kpC9uvrc98gdEf8Vj2xjVUWD8alBH_Dr4AdBGujQ4XFYlCOYht6Pk71Mk9nz43DPqa6IL3BS-kCKlU-v57Z9JPvkHkxmLhzI1C8Eao0vQO97pvTMpzDlrTCI5HNDTH0Uc3fz2swXl7o7u7Fbr3NM3Z66M3jCEkPNAgum8gRCiAI75v73KQT_cCNb7zq0r0w5rWlG-G0toFiKr9m8bXAhZPAJN2RuH94Pay4zuFDEFXqyx7KVcsZixmsU1JtSyvuZntY98hpfT0HvTqkBt8fCNgx7nyoo6Ik4J61vNpM6fi9wjOre_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی برای دو نفر از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ احکام سنگینی صادر کرد؛ مهنام نواب‌صفوی به اعدام محکوم و حکم ۱۰ سال زندان علی صانعی نیز در دادگاه تجدیدنظر تایید شده است.
مهنام نواب‌صفوی، محبوس در زندان دستگرد اصفهان، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد با اتهام «محاربه» به اعدام محکوم شده است.
در پرونده او اتهام‌هایی از جمله «محاربه از طریق مشارکت در تخریب اموال عمومی»، «تبلیغ علیه نظام»، «اجتماع و تبانی علیه امنیت کشور» و «تشویق مردم به کشتار یکدیگر» مطرح شده است.
هم‌زمان، حکم ۱۰ سال حبس علی صانعی، دانشجوی ۲۲ ساله رشته کامپیوتر، در دادگاه تجدیدنظر تایید شد.
صانعی اسفندماه ۱۴۰۴ در ملارد بازداشت و به زندان تهران بزرگ منتقل شد. شعبه ۲۸ دادگاه انقلاب تهران به ریاست قاضی عموزاد او را با اتهام‌هایی از جمله «توهین به رهبری»، «اجتماع و تبانی علیه امنیت کشور»، «تبلیغ علیه نظام» و «همکاری با اسرائیل» به ۱۰ سال حبس محکوم کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77424" target="_blank">📅 17:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EAhiVHOTkTHXRWBKW0IDeqYH6skDHI16lVs7JVgfM_Ixgc5ue7E_uIC8Z9XBO0Q2QHaJKoarndEyiYdhYJQyKV_8GH8ZZuef36rwMVqn4raXY48LK7jReEixufIFCqf9iEqeFYLxTSpmhlk3jEWXSJfk0A-pM7z7l6z-MBdcc7lC7qmIn9m0rXmuohn_BXyN9y2SxiuToCup_dL0Y1M4wZ141czf11K7FvhphzRPaYFdXn0-oi-vthhkZToa6VG-BVkEcCmY2x2Pb0gqfVS9HAbQL-Lt3pyuDCpjJ8rh4dEneJFr0SyHICZaRdYJwPJ3OXbErNU7CDay0VzhReJxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس: آمریکا هم‌زمان با تشدید حملات به ایران، بمب‌افکن B-1 را به‌کار گرفت
ترجمه ماشین:
مقام‌های آمریکایی گفتند ارتش ایالات متحده روز سه‌شنبه برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران از یک بمب‌افکن دوربرد B-1 استفاده کرد.
چرا مهم است: این نخستین بار از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش بود که آمریکا مأموریتی با بمب‌افکن B-1 انجام داد.
استفاده از بمب‌افکن‌های B-1 که می‌توانند ۲۴ بمب ۲٬۰۰۰ پوندی یا ده‌ها موشک کروز حمل کنند، نشان‌دهنده تشدید و گسترش قابل‌توجه کارزار نظامی آمریکا بود.
‏B-1 می‌تواند در ارتفاع پایین با سرعتی بیشتر از سرعت صوت پرواز کند و در میان همه انواع بمب‌افکن‌ها، بیشترین محموله بمب را حمل کند.
هم‌زمان با ادامه افزایش حضور نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان در حال بررسی بازگشت به عملیات رزمی گسترده علیه ایران است. مقام‌های آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
اصل خبر: بمب‌افکن B-1 مأموریت خود را از یک پایگاه هوایی در بریتانیا آغاز کرد و در وب‌سایت‌های آنلاین رهگیری هواپیما مشاهده شد.
فرماندهی مرکزی ایالات متحده (سنتکام) در بیانیه روز سه‌شنبه خود درباره حملات آن روز، به مأموریت B-1 اشاره نکرد.
در این بیانیه آمده بود: «دارایی‌های سنتکام مراکز عملیات نظامی ایران، توانمندی‌های دریایی، آشیانه‌های هواپیما، تأسیسات نگهداری پهپاد و زیرساخت‌های لجستیکی نظامی را هدف قرار دادند تا توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز بیش از پیش تضعیف شود.»
مشخص نیست B-1 چه هدفی را مورد حمله قرار داده و آیا این مأموریت عظیم از دیگر حملات چند روز گذشته مؤثرتر بوده است یا نه.
آمریکا در جریان عملیات «خشم حماسی» چندین مأموریت با B-1 انجام داد و پایگاه‌های موشکی، مراکز فرماندهی، تأسیسات نگهداری سلاح و سامانه‌های پدافند هوایی را هدف قرار داد.
وضعیت کنونی: با وجود گسترش حملات آمریکا، به نظر نمی‌رسد حکومت ایران موضع خود درباره تنگه هرمز را تغییر داده باشد. ایران همچنان به حملات علیه پایگاه‌های آمریکا در منطقه ادامه می‌دهد.
برخی مقام‌های دفاعی آمریکا می‌گویند توانایی نظامی ایران در اطراف تنگه هرمز «تقریباً از بین رفته است»، اما برخی دیگر می‌گویند ایران همچنان قادر به حمله به کشتی‌ها در این منطقه است.
رئیس‌جمهور ترامپ روز چهارشنبه تهدید کرد که اگر ایران به حملات بیشتر علیه کشتی‌ها در تنگه هرمز دست بزند، پل‌ها و نیروگاه‌ها، از جمله تأسیساتی در تهران، را بمباران خواهد کرد. ایران نیز در پاسخ، زیرساخت‌های کشورهای حاشیه خلیج فارس متحد آمریکا را تهدید کرد.
نمای گسترده‌تر: همچنین روز چهارشنبه، شورشیان حوثی برای نخستین بار از زمان اعلام محاصره بنادر عربستان سعودی، به کشتی‌های سعودی حمله کردند.
یک مقام دفاعی آمریکا گفت حملات حوثی‌ها، پس از چند ماه که تقریباً به‌طور کامل از جنگ دور مانده بودند، ممکن است با تحریک ایران انجام شده باشد.
این مقام گفت ایران می‌خواهد با استفاده از حوثی‌ها، علاوه بر خلیج فارس جبهه جدیدی در دریای سرخ ایجاد کند و بر یکی دیگر از مسیرهای حیاتی بین‌المللی حمل‌ونقل نفت فشار وارد کند.
روز چهارشنبه چندین کشتی تجاری در حال عبور از دریای سرخ دیده شدند که از بیم حملات حوثی‌ها، مسیر خود را تغییر دادند تا از تنگه باب‌المندب عبور نکنند.
آنچه باید زیر نظر داشت: مقام‌های آمریکایی گفتند میانجی‌های قطری همچنان با مقام‌های آمریکایی، ایرانی و عمانی گفت‌وگو می‌کنند تا به توافق جدیدی برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند؛ این موضوع را منابع مطلع اعلام کردند.
یک منبع منطقه‌ای گفت رهبری ایران تازه‌ترین پیشنهاد ارائه‌شده از سوی میانجی‌ها را نپذیرفته است.
مشخص نیست ترامپ چه مدت به تلاش‌های دیپلماتیک فرصت خواهد داد. ترامپ چهارشنبه‌شب در سخنرانی‌ای در جورجیا گفت: «آن‌ها به‌شدت زیر ضربه هستند و می‌خواهند توافق کنند.»
«اما من می‌گویم آن‌ها آماده توافق نیستند، چون هر بار توافق می‌کنند می‌خواهند آن را عوض کنند و همه‌چیز را تغییر دهند. آن‌ها آماده نیستند. خیلی زود آماده خواهند شد.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77423" target="_blank">📅 07:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/de3OanLqISixObug-lOzVqg7i3cDaL81qh3jCoWB-MAWvgLVXZegyLzBY-X23JxuBumEWwFzz3dKzMzc9uXC4vPlL1fMWtZ6C1wv1m34WdzGv0yuuUWNwi3fDeRtG-8z4TTPs-pXW7Cgwxo3ZdEQJoCnvsluKBbzCJdUt_dGCXFL3daIjqJekdDxWpaPyHuRkBk62qOR8M_J6o-lLDuc20ZdJddlyGUAVBdu6y7lV2PiAV_vnA9n_DdCUH5tTNEP1dlAJGx6k3qvoBkiPDAEQdxdJvvNVukfoyxoBJHOc4vJURZHUDDDlYIpg5hjczNY7hZmh4Od340ODAPBv-YPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان (واس) تایید کرد که کشتی «انسیلیا» متعلق به یکی از شرکت‌های سعودی در دریای سرخ هدف قرار گرفته است.
به گزارش واس، در پی این حمله، آتش‌سوزی در بخش جلویی کشتی رخ داد، اما همه اعضای خدمه سالم هستند.
یک منبع در سازمان حمل‌ونقل عربستان نیز اعلام کرد نهادهای مسئول اقدامات لازم را برای تامین امنیت کشتی «انسیلیا» انجام داده‌اند.
پیش از این، حوثی‌های مورد حمایت جمهوری اسلامی اعلام کرده بودند که دو نفتکش عربستان سعودی را هدف قرار داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/77422" target="_blank">📅 07:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/111a8149da.mp4?token=Oo-7OaYuOgsfgNDqd9K6kaRjqJNoBiyqX41-Z3Z5HvTRCjp33IT9OhveTq5AlwjHv0pw0mSQWbW36zxPYzHdCueADGMPuBTsqxdS6DfVMESS75JybZE3WI3O7LP-9-dvLh2hZKnB4a3AYyGATIEJNf9Mtr8u567fJZ0CmSKrc8QYp4o5B-h2cpLJl3BZNbdKhVXeEi2Bi4_IUE7iQqDmE5dHTlWBxD8DUYSwlG8vlvVKcKkhiWw-HVs0kLwyzPFbKbQcblQVZ6VbX0XJ1pXsXOfRKuT8zASaQLdakzTwC_3n5lACAXCgt6bSWY8R2ZDSr_-YqF7ua75Ajb7thrcQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/111a8149da.mp4?token=Oo-7OaYuOgsfgNDqd9K6kaRjqJNoBiyqX41-Z3Z5HvTRCjp33IT9OhveTq5AlwjHv0pw0mSQWbW36zxPYzHdCueADGMPuBTsqxdS6DfVMESS75JybZE3WI3O7LP-9-dvLh2hZKnB4a3AYyGATIEJNf9Mtr8u567fJZ0CmSKrc8QYp4o5B-h2cpLJl3BZNbdKhVXeEi2Bi4_IUE7iQqDmE5dHTlWBxD8DUYSwlG8vlvVKcKkhiWw-HVs0kLwyzPFbKbQcblQVZ6VbX0XJ1pXsXOfRKuT8zASaQLdakzTwC_3n5lACAXCgt6bSWY8R2ZDSr_-YqF7ua75Ajb7thrcQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا [۶ صبح به وقت تهران] در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
نیروهای آمریکایی اهداف نظامی ایران، از جمله توانمندی‌های دریایی، تأسیسات نگهداری موشک و پهپاد، مراکز نظارت ساحلی و تجهیزات پدافند هوایی را هدف قرار دادند. این حملات توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری را بیش از پیش تضعیف می‌کند.
در ماه جاری، نیروهای آمریکایی ده‌ها مرکز نظامی ایران در خشکی را هدف قرار داده‌اند و هم‌زمان محاصره دریایی علیه ایران را از سر گرفته‌اند. تا امروز، سنتکام برای جلوگیری از ورود کشتی‌ها به بنادر ایران یا خروج آن‌ها از این بنادر، مسیر ۹ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته است.
بیش از ۵۰ هزار نیروی نظامی آمریکا در سراسر خاورمیانه در حال فعالیت هستند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77421" target="_blank">📅 06:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UB4gpBKf8V6-iOzHjc80O5IOIpIzVLvqQCVFk6zCmkiV6D0cGTf1HCURXJ-_7xw582eNoKms6WXq_4gvLyNMl5t-VfDL3LEvIf5ghYbf3aTPbkdtw9siZp8BnJS4dTFcS5fJTn91-sUc0sLLQtToN6uNC-GMxroXxfc1QGF4c72f4NkVU8S65Q5zG6XEQ2I_YiS1p3TQBesMsveokuAgbfEuj5okhuegWXpUtli9-6hIFQpa0WxRHsCfUzLFhN7AUHP3fW3IQh2wjVcqvI7sdQ7aoz8j1mMw8icXSDIzZ7VYZe4_-Roh7AIjHsbXxYMTCvp3GJKuZ-1PE4TsHJhyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه پیام دریافتی از ساعت ۵:۱۳:
دوتا انفجار سنگین پایگاه دریایی ارتش جاسک
جاسک ۲ بار زد
جاسک چند دقیقه پیش دوبار زدن . سلام
🔄
دوباره زدن
صدایی شبیه به جنگنده هم میاد
یک صدای وحشتناک انفجار جاسک 5:30
همین ۱ دیقه پیش دوباره جاسک زدن، نمیدونم دقیقا کجا ولی صدای خیلی شدیدی داشت
باز انفجار مهیب در بندرجاسک ۵:۳۱
جنگنده بالای سر شهر در حال چرخیدنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77420" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AccWJm3gc4pUQvCTfIJujp9pb9pN-sPiZbn_g2Gu2Z2RCtWyVXOih7qfOsZrnRXKPXqSEgvCitWs5-Nfj7_KYgeHxia-b4PCU1FSA16WeP4JcxuKdGRZk1HviSMocQePHca1-gAo5JsjBSCUHN4ANFQMdhb66atCUDV_VFoZTN6O17zNoVm-QD9g_kNq42kE8ohUJrxUbVGo0y8fmq6amrQVTnjMHaycll1EdwMRACML91T4GxjKlepPsOXcactQukDEEpkEcMc1QM0UYibUv-RNC7AtGctHBcOg8C_msJyGkmPO-cRjjJ91pc60L_VsRXD-3zIaPJPASuK2jAJAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hgu-5LZpSm9Am0SkH_maeQYz3Bqr6FX9sTtvQ-xTWBEuqczDh_K7yHzmiMwoyi8v8WlSyLrza1J3oUPl_mHPAx9-h4P0pXmoQ3MXdd72VbvtLJVOZGDC_YbhZgKRqfLecEzK6PaR1AN7Uoj8aTtAat8zkDw3Q_k7Hfw8Bu-fx3h7x9nsGSz-2_ElBgs3tnpTPJgb1qtIjjI4SzpQGUhZs2yHBMYjqvQu-_aNt34QdSD1xJnE8etO-jdT5Kw8ePHjP0Y-S2DYf84NbHCO6WHF1wVTqxG0UaVcURgCysTVwfy8_tPpwxiMeOhUYkQHiUKAIXBjjz7tXsuqSXRhGWGhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rxeyi8BAdO5Y7Pe08BbQodrqGAPo5PryMjFTUDWO907LijRegQ18b-3NOJM1MRhsNx6ppQVmelrsLHdtE7UNIu1U2DpcvuuF0znfl_jhMh93rPf3DJ_jW7fAM3oCLb8XBWG4QAIJFmNZQD8UvpcNI47fpjmrnG40-csiRrVVyVKOvplrXPfln6jz6my7cTPhTlknne8uDtOi8ggYxJVLGZmLU7NmugaK29XIo7Yt3VDvnIVqtslPL9zAU2XhcKmibShdUZdAsfGja5QPvTAC771sOP_D6wKhxOGtT0LQBOaeo6ZppWRwPLZz3OGUB-rqdZ5d7a6Wm17ETyjMitE_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sooo9lls2UNF4_UtbzqHPjFu0rdsjs0U__2ljq6f36wJDfJXJOKEBJEAq4y_9wgsXmkB2xNjF8cOpr6v0eZNUV0oW6kgkU7rAhjH5rAzi_syG87Z_QEqKo1y7-ikklVY-mVBWcaLpC0rIT-C824oCyMcFvScSMjt2zN9YcuuQkOR9Afni9tqX-pjbXsbN867DssgJtXIKZHkMQXQpIAqYSHDkqC38HTNZqXKAL2AvyjPd5XsfVHbj4mRbsJzYteJMNE-WNPM5D9koog9Hze-gbx4ac-FCkCw9otjYyiyXtb3UpLwucPnk3mZscvH5fBBDDk-qdT0dPBB6wpBbqE85Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر پخش شده با شرح: انفجارهای حمله به  اسلام‌آباد غرب در استان کرمانشاه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77416" target="_blank">📅 04:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ZpA09e9WXULGh3Xq9k3miQGZig_zog9rykctbDQ2siZ0OcsD30NvyORGFnzl-A1580KmCucoGaGMpdz84WU42hSuaEFkj3j3zSfVTC1eNljTkyOCMtqT8_UPS0ekZLLasjTVQ4WzytpkACna3h72_ubCbg0T9tGN__Tj4uNLaUC6Jr3I33YihYyi1oM2IBxaSyQLpamzZltdlClYFK9zkvNHepy9uuRoFeA4xqJBITrYudxSR4RO4RpJwmJTT7qGCngSwNcHpmtq4K5gD7_TLmk509Mn_M79mVNqSujwCyecYmJsqV7_77Rr04zGdBywd5VITsqnL_XG5g162iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش تسنیم، معاون استاندار خوزستان اعلام کرد یک نقطه در اطراف شهر اندیمشک هدف حمله موشکی قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77415" target="_blank">📅 04:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=FM7fLLuL7xC0qI2SnlzyzWBb2wooE_4dWod82XAcHkjTJe3DqaNLPN04xSdVmjNz3t48H-oNIhTV_Eh4tV_DP4QUGn9QvZb6k7O4I2xmAzmWZwIcpu3Seo5GnrjWqvNHch35KPCzXQTnnMitWmNByFpnoIpzIPV8I38__JbkDCVyhbZRa4Cpb0xvZwNiqhewIM4osxRArlp0tcgCceoEDcngWOtIXDwYg7TiWRte0ePTQl8j8M_Z3Av_GdMrm2KbXhCMQl7zFC7e-IE34zUpBUd_Om7HzO43vqxPGT4orQpoVosfm2L5EaPFICILgYA55FXltB-AOMSkbomPkF2wFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9aaff68657.mp4?token=FM7fLLuL7xC0qI2SnlzyzWBb2wooE_4dWod82XAcHkjTJe3DqaNLPN04xSdVmjNz3t48H-oNIhTV_Eh4tV_DP4QUGn9QvZb6k7O4I2xmAzmWZwIcpu3Seo5GnrjWqvNHch35KPCzXQTnnMitWmNByFpnoIpzIPV8I38__JbkDCVyhbZRa4Cpb0xvZwNiqhewIM4osxRArlp0tcgCceoEDcngWOtIXDwYg7TiWRte0ePTQl8j8M_Z3Av_GdMrm2KbXhCMQl7zFC7e-IE34zUpBUd_Om7HzO43vqxPGT4orQpoVosfm2L5EaPFICILgYA55FXltB-AOMSkbomPkF2wFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
وحید بوشهر زدن بدددد
بوشهر انفجار خیلی شدید
😐
دستم میلرزه بزرگترین انفجار
سلام وحید همین الان انفجار خیلی شدیدی بوشهر از قبلیا خیلی بدتر بود
وحید بوشهر زد ساعت ۳:۵۹
بوشهر چند انفجار وحشتناک همزمان ساعت ۰۴:۰۰
بوشهر زدن ساعت ۳:۵۹
سلام وحید الان بوشهر رو زدن و خونه لرزید یه صدا خیلی زیاد هم اومد
انفجار سنگین شهر بوشهر ۴:۰۰
سلام وحید جان
ساعت 3:59 بوشهر رو زدن صداش متوسط بود
بوشهر صداش خیلیی بلند بود
همین الان وحشتناک بوشهر زد
همین الان بوشهر زدن ۴:۵۸
وحید جان بوشهر پایگاه هوایی باز زد الان
درود، همین الان
3:59
بوشهر رو زدن صدای مهیبی داشت
وحید جان بوشهر
همین الان زدن دقیق ۳ و ۵۹
یک انفجار نسبتاً شدید ساعت ۳:۵۹
۰۳:۵۹ بوشهر صدای انفجار خیلی شدید و خیلی نزدیک اومد
سلام بوشهر رو الان زد
همین الان یک دقیقه پیش انفجار وحشتناک بوشهر خونه لرزید
از بوشهر همین الان یه صدای خیلی بلند انفجار دقیقا نمی‌دونم چی بود اما خیلی بلند بود همه از خواب پریدیم
ساعت ۴ صبح انفجار مهیب در بوشهر
چندین انفجار بوشهر
یکیش خیلی بلند بود و لرزش داشت
داش بوشهر بغل خونمون انگار بمب اتم زدن
بوشهر صدای وحشتناک انفجار، گمانم پایگاه هوایی بود... ساعت ۴ صبح
همین الان خیلی شدید
از خواب بیدار شدیم
بوشهر
صدای انفجار خیلی شدید از پایگاه هوایی بوشهر
سلام همین الان بوشهررر صدای بدی اومد که همه بیدار شدن
تک انفجار ساعت ۴ ولی جوندار زدن
آپدیت:
پیام‌های ساعت ۴:۴۱:
صدای پدافند بوشهر
وحید بوشهر انفجار
ضدهوایی هم کار می‌کنه
بوشهر پایگاه هوایی صدای پدافند
بوشهر ۴و ۴۰ پدافند پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77414" target="_blank">📅 03:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">استان کرمانشاه
فقط سه پیام دریافتی در ده دقیقه:
انفجار کرمانشاه ۳:۳۶
اسلام آباد کرمانشاه رو زدن
سلام ۵دقیقه پیش اسلام آبادغرب در کرمانشاه را زد ۲تاانفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77413" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDVKk0jYl98i0dl81y114FlTNFoeXXiIiwsKaugUVfPrQWj3A82fcRav3rKKVrX16iGreU-gn0Vl-SJL7TBpPljzWAD-N1ob97naBzHZzGJAIGTFn14a2mnuJRaewsPG41_QsuMAe9LJAcNODiFdLKNt8v6eF7Xv39KzNE4v54Op7gC0D-f99RkCzxX-HkyFkgMR8ku13MHTeJOy9SFLtnhaOFPgFw3nANsbEWaeWsMVXwuZKSHElQ0SFn7oO5_h7CSLRvvfbKW05LzsAr0u505V1EWYnY5I9hLzxEGk08Hfp6OyFwHWwPAnxZH0A5bKc8gdr5B0E8lKed0jkVAApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران صبح پنجشنبه در اطلاعیه‌ای گفت که سه کشتی قصد عبور از تنگه هرمز را داشتند که یکی از آنها آتش گرفت. سپاه دلیل آتش گرفتن این کشتی را برخورد با مین عنوان کرده است.
سپاه در این بیانیه تاکید کرده که کنترل تنگه هرمز را در اختیار دارد و هیچ کشتی از این تنگه عبور نمی‌کند. در عین حال ارتش آمریکا می‌گوید تنگه هرمز باز است و هفته‌های اخیر ۹۰۰ کشتی از آن عبور کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77412" target="_blank">📅 03:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=Y1yHYmr3C2ZklxRvMsJU5My7DPIgZFQl_GFLWLpuOzvE6QjOXiukQL6Lvp6NwW15C_mHmwgsNtlsryM15Ls780RPqYd7vDUT2nsOfwUiyFYVWfrkmg4rrEfF7OlQ0W4HKLmf0yWowFOFebQI_4x_kRVzggFYCSqNHO9GZywzXNuqcIxd-uT39wVN6U2JzFIhLjU24zfjbnfkqsf_osjAwKoosGI8e0hkm9RAaa27G9evY4OT-LagYIkge9xOuvRz1YCwWAlTwv-tZJ7V3hUhh2D5oHpg60G_6taEG0vvXs17ET--zpAhG4pp3MOAEbceqL81rXLHTjvra1X0NSoDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/733c9968e4.mp4?token=Y1yHYmr3C2ZklxRvMsJU5My7DPIgZFQl_GFLWLpuOzvE6QjOXiukQL6Lvp6NwW15C_mHmwgsNtlsryM15Ls780RPqYd7vDUT2nsOfwUiyFYVWfrkmg4rrEfF7OlQ0W4HKLmf0yWowFOFebQI_4x_kRVzggFYCSqNHO9GZywzXNuqcIxd-uT39wVN6U2JzFIhLjU24zfjbnfkqsf_osjAwKoosGI8e0hkm9RAaa27G9evY4OT-LagYIkge9xOuvRz1YCwWAlTwv-tZJ7V3hUhh2D5oHpg60G_6taEG0vvXs17ET--zpAhG4pp3MOAEbceqL81rXLHTjvra1X0NSoDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای منابع حکومتی: حمله موشکی به اطراف پایانه مسافربری در مرز شلمچه
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: دقایقی پیش اطراف پایانه مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.
به گفته وی، تردد زائرین بدون مشکل در حال انجام است.
منابع حکومتی: کشته شدن دو نفر
معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: تاکنون ۲ نفردر حمله دشمن آمریکایی به مرز شلمچه به شهادت رسیدند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77411" target="_blank">📅 03:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LOMrVKGYvwsfRPcJ5b7paChvz9Ti_1_lzSeNzYvWcayoc3SugQFIsNVT0nz-UxbQmnV0mkXu5AwY7mKzO4n0Ktyw6obXbLeZu5_15p2xcHQuoq9CCSWjdTX0XnVhb79TiaWpNk9z-WuWT4h5n1htpOeEY2iS9reKIuJadho3JIZ6V0ftRR-p-yPsr2hfL97YCU8wMr9lOgCiWyXo9ucEP5uvFPyvaP-_9uEY8ORn9HgXzkC7WTBg7ATuZegbJytPCUlIZHeS5d9rPrhlt0u9garxxZx6vScAuh_G83iY5nx-AhyKr74zi0611OGjYXBWqZfmlwXJOER1Z32XQx9QJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا گفت تفاهم‌نامه با جمهوری اسلامی بر پایه پایبندی به تعهدات بود، اما تهران آن را نقض کرد و در نتیجه این توافق دیگر معتبر نیست.
او افزود تفاهم‌نامه شامل بازگشایی تنگه هرمز و تضمین آزادی کشتیرانی بود و جمهوری اسلامی باید حدود یک هفته و نیم پیش بیانیه‌ای در این باره منتشر می‌کرد، اما در همان روز به یک کشتی حمله شد.
وزیر خارجه آمریکا همچنین گفت واشینگتن همچنان از دیپلماسی و راه‌حل مذاکره حمایت می‌کند، اما به نظر می‌رسد جمهوری اسلامی در حال حاضر در این زمینه جدی نیست.
روبیو افزود، چین نیز با اقدام‌های جمهوری اسلامی در تنگه هرمز و اعمال عوارض بر عبور کشتی‌ها مخالف است.
به گفته مارکو روبیو وزیر خارجه آمریکا، جمهوری اسلامی با مشکلات اقتصادی جدی روبه‌رو است و شهروندان ایران با تورم بالا و افزایش شدید قیمت مواد غذایی مواجه هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77410" target="_blank">📅 03:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سخنرانی ترامپ در ایالت جورجیا، بخش‌هایی مرتبط با ایران، ترجمه ماشین:
...
اما میلیون‌ها و میلیون‌ها بشکه نفت در راه است و ونزوئلا هم اکنون بهتر از هر زمان دیگری عمل می‌کند. شرکت‌های بزرگ نفتی وارد می‌شوند و قرارداد می‌بندند. کریس رایت روی آن کار می‌کند، داگ برگم هم روی آن کار می‌کند، اسکات هم با آن‌ها کار می‌کند و واقعاً فوق‌العاده بوده است. آنجا ذخایر عظیم نفت دارد.
در واقع، اگر آمریکا و ونزوئلا را با هم حساب کنید، حدود ۶۲ درصد بازار نفت جهان را در اختیار داریم. بنابراین ما به تنگه‌ها نیازی نداریم؛ به هیچ‌چیز نیاز نداریم. به تنگه هرمز نیازی نداریم، اما وارد عمل می‌شویم، چون مجبوریم؛ چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
در قبال جمهوری اسلامی ایران نیز در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز، هرگز نتوانند همان کاری را که با بسیاری کرده‌اند با ما انجام دهند. می‌دانید، آن‌ها بیش از ۵۲ هزار معترض را کشته‌اند. افرادی که اعتراض می‌کردند کشته شده‌اند؛ ۵۲ هزار نفر در چهار ماه گذشته. هیچ‌کس نمی‌خواهد درباره‌اش حرف بزند. رسانه‌های جعلی آن عقب هرگز به آن اشاره نمی‌کنند.
[ + جملاتی مربوط به مراسم سربازان کشته‌شده آمریکایی که در ویدیو هست ولی در پست جا نمیشه.]
---
بازار سهام رکورد زده است؛ آن هم در حالی که این درگیری کوچک در جریان است. من آن را یک «درگیری کوچک» می‌نامم. این درگیری کوچک ما با جمهوری اسلامی ایران است.
دلیل اینکه آن را این‌طور می‌نامم این است که، بگذارید بگویم، آن‌ها چنان سخت هدف قرار می‌گیرند و می‌خواهند توافق کنند. اما من می‌گویم هنوز برای توافق آماده نیستند، چون هر بار توافقی می‌کنند، می‌خواهند آن را تغییر دهند و چیزهای دیگر.
هنوز آماده نیستند. خیلی زود آماده خواهند شد. با وجود اینکه این وضعیت همچنان ادامه دارد، بازار سهام رکورد زده است.
---
نفت نیز پایین خواهد آمد؛ قیمتش سقوط خواهد کرد.
سه هفته پیش فکر می‌کردند توافق کرده‌ایم. گفتم: «فکر نمی‌کنم با این‌ها توافقی داشته باشیم. آن‌ها هر توافقی را که می‌بندند، نقض می‌کنند.»
اما مردم و نابغه‌های وال‌استریت فکر دیگری می‌کردند. قیمت نفت خیلی پایین آمد، بعد کمی بالا رفت، اما دوباره پایین خواهد آمد؛ شاید حتی پایین‌تر از زمانی که شروع کردیم. فقط کمی به من فرصت بدهید.
من همیشه می‌گویم: «کمی به من فرصت بدهید.» به کشاورزان هم گفتم: «کمی به من فرصت بدهید و ببینید اوضاع کشاورزان و مزارع چطور پیش می‌رود. این کشور با قدرت در حال پیشروی است.»
---
فقط در ۱۸ ماه، این کشور را به شکلی متحول کرده‌ایم که هیچ‌کس پیش‌تر ندیده است. فکرش را بکنید: مرز ما امن است، اشتغال افزایش یافته، تورم به‌شدت پایین آمده و کارخانه‌ها در حال افتتاح هستند.
سرمایه‌گذاری به کشورمان سرازیر می‌شود. گفتم: ۱۹٫۲ تریلیون دلار. ارتش ما با فاصله‌ای بسیار زیاد از همیشه قدرتمندتر است. می‌بینید؟ ونزوئلا، ایران.
آمریکا بازگشته است. از همیشه قدرتمندتر است و به شما می‌گویم که فقط در یک جهت حرکت می‌کند: رو به بالا.
تا زمانی که همین طرز فکر و همین نظام کنونی را حفظ کنیم، رو به بالا می‌رویم. اگر راه دیگری را بروید، هیچ‌چیز موفق نمی‌شود.
یک بار گفتم: «در کمونیسم، همه‌چیز به گُه تبدیل می‌شود.»
بسیار خب؟ حقیقت دارد. چیز وحشتناکی است.
The White House
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77409" target="_blank">📅 03:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGNzkiJHzaODOVgpOSk2GoIIxvBSx_kHWvowZjvtxdNxHhYGBVziTdEA4RK9Lwa9GKBmCRFYxf_nCflxX9RXckkKY2qldsBszPLrYJMmF28cG47erTttZ7i4BzlKKbHWQSJqaTuf4Gpx3cVQa1yW9Pvmi7fmUm-1dwnsuAuA5ZNIn37LEsWUcrOaZlatbkGsljowmfKt2i9fJSsvGPQoDhfIziJcIVOBacLCqIw2ylvOaT41RkXUG-KnhFP0l9H7YV0I3NokLdlAY0T31ZbGq6gTc_OGcdnsPs1DN3A_Us6BXxjt2iD2QJj18mxPivKD_8ZhPcNCt1ruH5lBZPNZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ستاد کل ارتش کویت، بامداد پنجشنبه اول مردادماه، با صدور بیانیه‌ای اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» هستند.
در این بیانیه، این حملات تاکید شده است که صداهای انفجار احتمالی، ناشی از رهگیری و انهدام این اهداف توسط سامانه‌های دفاعی کویت در پی حملات «تجاوزکارانه ایران» است.
ارتش کویت همچنین از شهروندان خواست ضمن حفظ آرامش، دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای مسئول را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77408" target="_blank">📅 02:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QP6mNCsHl2DBt1qAh3lxIdbF8kMGLaRp4PJvKCzmz6Cby1rAijjpT0zPaLkAO0tkpBAhuH7SzdlaweovfSTW-yuc4sSEr4490mHP1UioIGwT4TWlGegzRQkq9ZvIPQC88-VZmYrqdjFqibezcxO_IL6O2XZmWXYA82NOaa4ifJjbTtOI1Gwwal-cIQpJfGpBvK3By_F2JjLY2EKXmqBwExcpkRWbtMCenvPcwrXBwY9B2Vf8U4emfA6A_ORpB1SIBg_nFG_XZBekCEfGJOECv82352nuD7VSLsMasYIPDNX2JzPQOFkHZp0SSLEVgKfO0n9xu4CA9oZHOW-kER_x1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۵:۳۰ بعدازظهر به وقت شرق آمریکا [ساعت ۱:۰۰ بامداد پنج‌شنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات علیه اهداف نظامی ایران را آغاز کردند. این عملیات ادامه خواهد یافت تا توانایی ایران برای تهدید دریانوردان غیرنظامی و کشتی‌های تجاری در حال تردد در آب‌های منطقه بیش از پیش تضعیف شود.
CENTCOM
نکته قابل توجه این که همه گزارش‌های امشب درباره صدای انفجارها مربوط به پیش از ساعت یک بامداد بودند!
حالا یا ساعت رو درست ننوشتند یا اون حملات کار آمریکا نبوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77407" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9imTKwRCJ1waPhR7TN83YWy_lXax3BzXmngS-PVfUXHHBM3oIdUm8Yp24uyhe_8wv0b0GvD8C87yvG2mHNaQfxloppRiwTJbZLW_Cw1Ua1GKwKUUJ_MaW2nhTbSmYLbwI1VrjCILY8NoQ0wPqu_Cj3lq2zdX6wU28KiBte6GyqcFQTe8kvdkvItljN1tJ1rLKQ4Q44DYivjTy95JyMNh-A06EFXfaY6ENbM8-0g0NntTyG54gHMuX54mXINy2crzRB1mZZH5TJvSOhwmPDaxujbE9lb28vrDV3yznbPjf7JEtFSscUGW8I31ZqA_6xrO1qKncdXYwlNr_QeFwAZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت گزارش در تصویر: ۲۳:۳۰ چهارشنبه به وقت ایران
یعنی قبل از گزارش‌ها درباره شنیده شدن صدای انفجارهای خوزستان و هرمزگان در بامداد پنج‌شنبه
ترجمه ماشین:
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در ۷۰ مایل دریایی جنوب‌غربی الشقیق، عربستان سعودی، دریافت کرده است.
ناخدای یک نفتکش گزارش داده است که یک پرتابه ناشناس به کشتی برخورد کرده و باعث آتش‌سوزی در عرشه شده است؛ خدمه در حال حاضر مشغول مهار آتش هستند.
هیچ تلفاتی یا پیامد زیست‌محیطی گزارش نشده است.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77406" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
سلام بوشهر دو صدای انفجار ساعت 12 و 49
صدای دو انفجار بوشهر 0.49
بوشهر و زد همین الان
سلام وحید بوشهر همین الان دوتا پشت سر هم بد زدن
وحید بوشهر زد دوبار ۰۰:۴۹
خود بوشهر زدن ساعت۱۲:۴۹ دوتا پشت هم
دوتا انفجار خیلی شدیدبوشهر
پایگاه هوایی الان
همین الان بوشهر ساعت ۱۲.۴۹ سمت بهمنی رو زدند.
وحید بوشهر پایگاه هوایی زد
سلام،۱۲:۴۹ دقیقه دوبار بوشهر رو زدن
بوشهر ساعت ۱۲:۴۹
سه صدای انفجار
۰۰:۴۹ صدای دو انفجار شهر بوشهر
بوشهر دو سه انفجار بود خیلی صدا داشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/77405" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تسنیم:
شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
دوباره، تسنیم:
بر اساس گزارش منابع محلی، ۵۰ دقیقه بامداد صدای انفجار در سیریک شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77404" target="_blank">📅 00:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در اهواز صدایی شنیده شده.
آپدیت: چند پیام هم از رامشیر، ماهشهر و سربندر داشتم.
پیام‌های دریافتی درباره اهواز:
وححححيييد
زدن
بعد از روزها..
اهواز ساعت ١٢:٠٩
اهوازو زدن
اهواز انفجار ۱۲:۹
وحید جان اهواز ۰۰:۰۸ صدای انفجار شدید
آقا اهواز زد دو بار
اهواز انفجار ۱۲:۹
سلام ساعت ۰۰:۰۹ اهواز صدای انفجار اومد
سلام وحید اهواز همین الان صدا برخورد اومد
۰۰:۰۸ دقیقا
سلام وحید اهواز یه صدایی اومد ۱۲:۰۹
اهواز ۱۲:۱۰ صدای انفجار
وحید همین الان ۱ ۱۰دقیقه بامداد انفجار شدید اهواز
وحید داداش ۲ تا انفجار ۰۰:۹ اهواز
اهواز به نظر میاد ساعت 00.10 یه انفجار مهیب بود. فقط لرزش رو حس کردیم.
سلام وحید جان اهوازو زدن
00:08  اهواز انفجار
وحید اهواز ساعت ۱۲:۰۹ دقیقه ۲ بار صدا انفجار اومد
سلام اهواز صدای یک انفجار شنیدیم
اهواز دو تا صدا اومد
وحید الان اهواز ۲بار پشت سرهم صدا اومد
تو اهواز دوبار صدای انفجار اومد
🔄
منابع حکومتی:
ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: یک نقطه در اطراف شهر اهواز توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت.
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77403" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rnsGQmrfBZQf-K2vr5EAc5irwzJMoKshOzKcAxpdY1SuRsjBHuR03g46W8_NIAeF_hVjK3qiArt5CeBmubfcfFBLb33Ed8OiZUzlqCg8xMxThYYCcESac9heCsm5LphqYIDh4pkFu1DeRkWMr_msGvspVT82kzH33MVte3MHufxLIQHlOayvS-BjZtRXkoOLbEQ6Pt4_dPJx234B09OCHR6I3Oe1iqG-eVdg1GCWp4-fbUeBYYRHIFHljvKiLpWsCy8oAgoTWGNzQVHWS6NDehsH4WZHXUIQt50sAVCq9QVBJ6vh1eeLdJCdwpjzNwKm-RB5UR9LMY4hoYPryLUwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: امروز نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران مدعی شد که ورود و خروج از تنگه هرمز را کنترل می‌کند؛ ادعایی که نشان می‌دهد دریانوردان بین‌المللی فقط می‌توانند از مسیرهای مورد نظر سپاه استفاده کنند. این ادعا نادرست است.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این آبراه بین‌المللی، صرف‌نظر از تهدیدها و حملات سپاه، همچنان برای عبور و مرور باز است. کشتی‌های تجاری با حمایت نظامی آمریکا همچنان از این تنگه عبور می‌کنند. از اوایل ماه مه، نیروهای آمریکایی به عبور بیش از ۹۰۰ کشتی از تنگه کمک کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77402" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
دکترین دفاعی ما روشن است: چشم در برابر چشم.
هرگونه تجاوز علیه ایران، از جمله علیه زیرساخت‌های ما، با پاسخی قدرتمند و قاطع روبه‌رو خواهد شد.
کسانی که به هر شکلی در چنین تجاوزی مشارکت داشته باشند، آن‌ها نیز اهداف مشروع تلقی خواهند شد.
Our defense doctrine is clear: eye for an eye.
Any aggression against Iran, including our infrastructure, will compel a powerful and decisive response.
Those who contribute to such aggression, whatever the kind of support, will also be considered as legitimate targets.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77401" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اکسیوس:‌ رئیس جدید موساد با رئیس سیا درباره ایران دیدار کرد
ترجمه ماشین:
به گفته دو منبع مطلع، رومن گوفمن، رئیس جدید سازمان جاسوسی موساد اسرائیل، دو هفته پیش برای گفت‌وگو درباره جنگ در ایران و برنامه هسته‌ای ایران به واشنگتن سفر کرد.
چرا مهم است: گوفمن یکی از نزدیک‌ترین مشاوران بنیامین نتانیاهو، نخست‌وزیر اسرائیل، است. این نخستین سفر او به واشنگتن از زمان تصدی این مقام در ماه ژوئن بود.
خبر اصلی: سفر رئیس موساد درست پیش از تشدید تنش‌ها در تنگه هرمز و ازسرگیری درگیری‌ها انجام شد.
یک منبع اسرائیلی گفت یکی از اهداف سفر گوفمن، هماهنگی با کاخ سفید درباره مذاکرات با ایران برای دستیابی به یک توافق هسته‌ای بود.
پشت پرده: منابع گفتند گوفمن با جان رتکلیف، رئیس سیا، و همچنین مقام‌های کاخ سفید دیدار کرد.
در حلقه نزدیکان ترامپ، رتکلیف یکی از صداهای تردیدآمیزتر درباره یادداشت تفاهم با ایران بود.
او پیش از امضای این یادداشت تفاهم هشدار داده بود که ایران این توافق، از جمله مفاد مربوط به تنگه، را متفاوت از آمریکا تفسیر خواهد کرد.
سیا و موساد از اظهارنظر خودداری کردند.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/77400" target="_blank">📅 21:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پست قالیباف:
معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت. اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است. بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/77399" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=ddVFZD3POCh0L-sAAFiiENczfjixV3QT66lZB0qN0Z-w202oajz7LV73YMBto0iix57Mkgw-dMi5CQNd49kXfVHrp2ouwyo3URMKqSd8hgAgUaeAhBG23P1CHqFyZEILxRZMlJrIr7c_m6InwTWUsNiXeSqk0FA6F_OuQiAmadaJGN7BvMXt6zfS_tHAe8vLraibLvcE1LQsSAxOioYqjmR9j1fgi0470lxE9hJaVDx7srlaFzUivWRV7ZBJ56_n4Hnq-vNOHTl80iVpsq7WEEOVSZnf2crjZktqkwNl5ySDs0pz_QjpkNNa5wIIkxmkScQ6o-nZ0-Y_Dd8P79MyXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fdcc2765ea.mp4?token=ddVFZD3POCh0L-sAAFiiENczfjixV3QT66lZB0qN0Z-w202oajz7LV73YMBto0iix57Mkgw-dMi5CQNd49kXfVHrp2ouwyo3URMKqSd8hgAgUaeAhBG23P1CHqFyZEILxRZMlJrIr7c_m6InwTWUsNiXeSqk0FA6F_OuQiAmadaJGN7BvMXt6zfS_tHAe8vLraibLvcE1LQsSAxOioYqjmR9j1fgi0470lxE9hJaVDx7srlaFzUivWRV7ZBJ56_n4Hnq-vNOHTl80iVpsq7WEEOVSZnf2crjZktqkwNl5ySDs0pz_QjpkNNa5wIIkxmkScQ6o-nZ0-Y_Dd8P79MyXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ کاخ سفید را به مقصد پایگاه نیروی هوایی «دوور» ترک کرد تا در مراسم رسمی مربوط به سربازان آمریکایی کشته‌شده شرکت کند.
تشخیص و ترجمه ماشین:
ترامپ:
برای ادای احترام به قهرمانان‌مان می‌رویم؛ و آنها واقعاً قهرمانان بزرگی هستند. واقعاً. آنها گفتند، و همه‌شان با قاطعیت گفتند: «نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد.» آنها سلاح هسته‌ای نخواهند داشت.
بنابراین می‌خواهیم به آنها ادای احترام کنیم. این برای من یکی از سخت‌ترین کارهایی است که یک رئیس‌جمهور باید انجام بدهد، اما باید انجام شود. فکر می‌کنم، همان‌طور که برای ادای احترام به این سربازان می‌رویم...
خبرنگار:
آیا درباره تحقیقات، اطلاعات تازه‌ای دارید که مشخص کند [چگونه آن‌ها در اردن کشته شده‌اند]؟
ترامپ:
نه، دارند روی آن کار می‌کنند. نتایج منتشر خواهد شد. می‌دانید چیست؟ ایران...
خبرنگار: [گفته می‌شود ایران پادگان‌ها را هدف قرار داده].
ترامپ: نمی‌دانم. خب، آنها بهای سنگینی خواهند پرداخت. دارند... در حال نابود شدن هستند.
خبرنگار:
قطعاً در میان خانواده‌های این سربازان، کسانی هستند که با این جنگ مخالف‌اند. به آنها چه می‌گویید؟
ترامپ:
خب، آمریکایی‌ها مخالف جنگ نیستند. یک نظرسنجی... یک نظرسنجی همین حالا منتشر شده. آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند. این موضوع در آن نظرسنجی کاملاً روشن بود.
هیچ‌کس نمی‌خواهد ایران سلاح هسته‌ای داشته باشد. شما می‌خواهید ایران سلاح هسته‌ای داشته باشد؟ فکر می‌کنید خوب است؟ بفرمایید.
خبرنگار:
[نامفهوم]؛ به آن چه پاسخی می‌دهید؟
ترامپ:
تنها چیزی که خواهم گفت این است: «دوستتان داریم. فرزندتان را دوست داریم.» و آنها برای خانواده‌هایشان همین هستند؛ آنها فرزندان‌شان هستند. هیچ بازی‌ای در کار نیست، هیچ‌چیز. او فرزندشان است. و تنها کاری که می‌توانید بکنید این است که هرچه در دل دارید نثارشان کنید.
متشکرم. بسیار متشکرم.
خبرنگار:
پس مذاکره با آنها در بحبوحه جنگ چه فایده‌ای دارد؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77398" target="_blank">📅 18:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gnlsp_9DLxYGj43xcVm2Go27HFMoTPS3-r-rvWrbbygDiVR8CD8hhDtda6Y4lf33CvfXIUKGz27Z01CBk7O0Qztgy4HXXZoTlfVD5Y2jd7u_R74NrNhwAWMv-mObmCvdKBynzwUBOqDhKVuIQfoaDGl_OppGmoK8o6DyFg_-YGzR3g7mfSbYC8ws5pIoGRrZovjTxKXJZlMlZ7tULKqi_tJ-f_d96GQhZtEcZh8KJi3ZKvrlDIRACvGJ3m6av5eCJzWPKTK6AsaKc4gg3R978kwzIGgaoDT9qoFALlTNoqtjW7y1Ks85J6c5ZSCvXKbovLg8A7z6XMi5H6828F1A-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز چهارشنبه ۳۱ تیر، گزارش داد جزیره لارک در تنگه هرمز ساعت ۱۴:۴۸ هدف حمله موشکی آمریکا قرار گرفته و به گفته ساکنان منطقه، صدای انفجار شدیدی در حوالی این جزیره شنیده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77397" target="_blank">📅 17:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bj15D4M7tLgkvfLedU1zw_LBHLHte-fOaX_ueTelOC5Ij98Q9vYONv9wGL55QY2YAhfuxYp2yocO2U3C_-R3IBuSAzUu7xuTKQrEBbaU5GGZ9iIShtQQKAs1s27Vf4hA4raU3MMt09tdFosdSprwee3ltsqG0Z9VG1TFg4LiJs4ohn71mBbriV6A4m-qnvmmJmi7FB7OCO6n6AE-2cfVITShwr4-2P6CQZnR8FxllYkfUPw5DVV6FUIciel5_5Q4myYsQKF3yXXjuXchjxUwzZHAzZy8ntFK0XlqkSbrFSwMGw4zZLhHb4a00T-NRGn1AZIWGyczKuI2DEUUbDXupw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
از این لحظه به بعد،
هر بار که جمهوری اسلامی ایران به یک کشتی در تنگه هرمز شلیک کند
ــ چه با موشک، راکت، پهپاد یا هر وسیله یا سلاح دیگری ــ
ایالات متحده
یک پل یا نیروگاه برق
را بمباران و نابود خواهد کرد؛
از جمله پل‌ها یا نیروگاه‌هایی که در نزدیکی یا داخل پایتخت، شهر تهران، قرار دارند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
From this point forward, any time the Islamic Republic of Iran shoots at a ship in the Strait of Hormuz, whether it be by Missile, Rocket, Drone, or any other device or weapon, the United States will bomb and destroy ONE BRIDGE OR POWER PLANT, including those located next to, or in, the Capital City of Tehran. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
پل و نیروگاه برق رو با حروف بزرگ تایپ کرده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/77396" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
