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
<img src="https://cdn1.telesco.pe/file/o4k9lyWIOuJQhGL8vqbDn028_PKdenTVmQWeQzbzo03lv4IvwviQ7o_3FildXNA8pcE22YH3rfxYKbg1wPM2J5tMgNfj25aoJWr0sk2-FkuW6QMpD-ii5vrefj-iNF60XcKuUmIsGhXL4WeQ0saKo7UTQpD9aFkQdmlKYPD4PK8Z6pbSZ1k9--Wh014I_N7PzJZckL_mwPU19eBtQYUgbIPEeFFJdZQT6mhAGT86pCl2S9E3NlfrgrL1-fRfSCQuyaw8WtqD9LXGC1JTr9-LBd5A3Zni_jeDz4EptpdOClh3ZPqmdZWYUnDDXJky46t2YUWD8FvrbiJyhzOLZtpvWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 03:12:48</div>
<hr>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ks47G7a5a-HH12ME9vgMHPeyW7yBa4nTJL4V-S6nnUS9KI6S3vaoyxGsfq45wlICPamitAsZudVXbJo-88_N83T0TQgTMxVACfOTN83M4FK4R5VV0ttB4NVF33OcFbY1qyO4uTOofpqxaaktMqUqavZQ4OaJSLTaEg20SxbaEBHT6EN-O03lBPCSN1fpTt9rXOh0eVp9F9GRHnE3sY0M-kn9Tu625ycE5zgnwJhxmUfHlkMM2OPPTDgoYzi0nErQFVRhvWDt-ciIJt4KFBTgIpqMG8Ec4gGk9tfDWWR-xMHX-4VUgBYJ39Xx7L_PRUerNOJl-GpbxQ925Hki3eVFbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=n1or4xyUSWmpFJuYpDnm9DxtheGiPbDrz8vAXgTJBn2Npd99DmUN-tZ_jl_T7K4qCwOfVOk1sOpxDwuX_qTZDmagIcMU_etjLiJ2xUk_xS6zdVNmzry9CNDILbxda92UG_DG0tD4dGRGHOHr3RI3w6cp6aKqXt-TW8v7d0mJgMWyBBFPD26ZjVcEgZVNSB4VTAITx_c-T1bb0MEmIF8jg2cdHcuG4XlfplnuMR9HrK_AsjK6UQRcsz3A-eV19yBBrN-QpynX23dlJuOoIE7YhA5X4NuPKzKxxa7Bys4EDkMVKOkZyVwMQ-RCZqUHO9URRzhg0wunT_uZ03M-W7G78g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=n1or4xyUSWmpFJuYpDnm9DxtheGiPbDrz8vAXgTJBn2Npd99DmUN-tZ_jl_T7K4qCwOfVOk1sOpxDwuX_qTZDmagIcMU_etjLiJ2xUk_xS6zdVNmzry9CNDILbxda92UG_DG0tD4dGRGHOHr3RI3w6cp6aKqXt-TW8v7d0mJgMWyBBFPD26ZjVcEgZVNSB4VTAITx_c-T1bb0MEmIF8jg2cdHcuG4XlfplnuMR9HrK_AsjK6UQRcsz3A-eV19yBBrN-QpynX23dlJuOoIE7YhA5X4NuPKzKxxa7Bys4EDkMVKOkZyVwMQ-RCZqUHO9URRzhg0wunT_uZ03M-W7G78g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UwEjwDv6FEivTuzhzitX4s5GFJz2HcHWW-S6YmgGP4cyNKcGaI5uSmEoBMRHM8BnHUp7c6qaDqJZ0f8lLMRoCp3bK1DESUsaOBWdNLK_0xgFg29CvbEayuaUYk2NI5lwGbjF1sxAyxHiCkamCMAdrEWAz7LwsqN8bG15aYx-79Sgr-hcc52UQguiXsOaeWcw0wfGGduSRAGoUoia2v7l6y1WmybmFwKWtzy8rJOoucGkpLchOqFlHvgF_ONCm083Dc47FjZRISK1TJMQ1OXVkBwxct13nSEs7qBjYeRL5rfncTZDB4er7zCE9kwLDCVpY2OADSxnBKAC6X74yFDDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jw0wNrzOK_ChYaKp1nRkdyAfpeA90RSbbTL2vRkVlkxO-ZH47KWxmu0PnRrTKteO-nNXDV105XaCRlbsfIo3JNQQ_2z1psZFrDsExq8uiE6nRSzhIcxZdgVFMFOKQr5lDLr-r4e1w0TWR-zmZiGQd_PiPcj_AnaX3yxkatXv5huHajwDVEIV7ggxZz34WS2MngwgaEgqFEF3lorVFaj8hIv48qDRsTf-AI4zfOf0rxuyuDhFeBN8cCmSL2uIvLyQbEz9sU9IyPIqxU0BHQyYK2X1RJcag-8HnaQ43ZD6bytTCszE_6jiq6igEobrMv-J4Oyufls865jY6lDFy5mm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC_n-BMNfI18EU6n9zpaK3inBaDqDH-YdH_s7j2NlEpDOAy7w_5_E1gJyTExogb06slfQ039r9CweSyid-ZZrY0YZ_4CJbf0UJqL-eCyEgsVAAEPc6dHRcGkEc1eFsQw9H6GzS04m7c_IIFTaoAyk7ruAniFo-cfCTD2dO2mTkls_mo0eRw0hw_VoE4OQo8h9mu0aBbwpYPYnVVGU5Qrt7EQ3ZpAGfcvo7jWez3jZDcp0f0usX8PleLp2ifphYY8b4kZjic31mkX3CzKlCaC9o_oD-rxnP-Gwq93iUbNVXWdJN3_l7Jlnm1_87dUEK91PjhxxYRJqR3pcux-QboCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IkgtW7PP9xochi3553zr2rUk8FMtDlsgV5kDaeT0WsAbITBGpjPpu-ECwgewFkdt-_PD09xdXuTM8snI4o0MAaCoWpo78X8z_e1uJHUSwgbs6Ao1j63GRW6JZTcQ8SRuhKY5ZkDikytH5AHoS4mz4D9UBbPDZXBLc4MbSBB8qIpMWQi7lW_naLJItZQOg5Ne11jD0AxJIKTVXPMB0fzFAuR4yzkIJGCUqZhuOOWLPAqyV7ZYLtMTVccDbI8czEs4Z14AckGmC7f348Z6HJklhwiyM48VNMlQxEGbq--OjOGbc6cIBwKgxDYaiMvrVDO24mhcMkWuWUx2xMR3j2iSpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=SJ6Fn9EEIYT4VKK3S4x9us1JnsZcTO8V9NMLaPf7qQrgBVwcRA5EbF8UynQbdbY4taeSFIlRg5CNMfwTUtbN43UD5C9fWPq-FjXpWBTPPgRspGQY_PZO0cBSZiyIn-sh13qlsiaiMGH5TVK3hiK8oXMPqd5ry3NKnFZb3iKikCPNwrW7XK_AbuLwpGHxlOQuzI_6DeCH_TX6vbB3FFEvgQ-BAxeOBfbLlOJTFOdP8ZeQVqsKilyHDY1gbOSy1xZeziSw712Zlp56s3IzKBK4XIgy_LJlF6BVKwu_zAgF7bLSUpi59N0r3DUDLBSNhrBkvn0bnC_FwszybYXrx-Zs0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=SJ6Fn9EEIYT4VKK3S4x9us1JnsZcTO8V9NMLaPf7qQrgBVwcRA5EbF8UynQbdbY4taeSFIlRg5CNMfwTUtbN43UD5C9fWPq-FjXpWBTPPgRspGQY_PZO0cBSZiyIn-sh13qlsiaiMGH5TVK3hiK8oXMPqd5ry3NKnFZb3iKikCPNwrW7XK_AbuLwpGHxlOQuzI_6DeCH_TX6vbB3FFEvgQ-BAxeOBfbLlOJTFOdP8ZeQVqsKilyHDY1gbOSy1xZeziSw712Zlp56s3IzKBK4XIgy_LJlF6BVKwu_zAgF7bLSUpi59N0r3DUDLBSNhrBkvn0bnC_FwszybYXrx-Zs0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=d8uJzw-J4RSe-TP_xuH9TuToNZcT5-vYBlfT-Slb6bg5AX5NN10-LObCNNsVkfKw3zXNNF18IKuNtEOporVpAzoZ98NVWGXTs9OKf_rzKYJFHN8jGySl-yJ19YCSRlZf8B40_ZMHUkvtYAybEodvtYV8wtK3Djt4bvhVbUcms6PYKLQS15hV07rsTveRn7T64jpmMmS22ymkitiR80Jc8MsBX5FVAOAM29PkEUVPmTf4yxCTPwKz38XvCIubn7_eTqgy_phn_hasGD9JEQFEzX2DAxlO6HZN5JFqx3sbpgGC6RrQG5QL1kmw3R4FmCR4tuKAhFAFbQCdKVvqfYF_Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=d8uJzw-J4RSe-TP_xuH9TuToNZcT5-vYBlfT-Slb6bg5AX5NN10-LObCNNsVkfKw3zXNNF18IKuNtEOporVpAzoZ98NVWGXTs9OKf_rzKYJFHN8jGySl-yJ19YCSRlZf8B40_ZMHUkvtYAybEodvtYV8wtK3Djt4bvhVbUcms6PYKLQS15hV07rsTveRn7T64jpmMmS22ymkitiR80Jc8MsBX5FVAOAM29PkEUVPmTf4yxCTPwKz38XvCIubn7_eTqgy_phn_hasGD9JEQFEzX2DAxlO6HZN5JFqx3sbpgGC6RrQG5QL1kmw3R4FmCR4tuKAhFAFbQCdKVvqfYF_Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=pW49nIzmzcv0Qc-z9T66GK2nGUA8pdHQhto4lLQOI5Q4D43Tdn1WByN1iq7E1LzEC3ZtUa8GznvRJWm_NEWGqSxb5ixpQKsW9pf9l7jRq10Klj_cwAHOEyuRRGrz48toTljbaq-00yH4xd631Uup-gjZDsWVXr_QzgWniYBpdcKPyQ_PcAWPmj1EYowJauun6a8AdntVq-bXoISPXYtykCuqcsX8oPlquC5LRZQuH79Af5PdT1VY4LXfE4fAhpH0I1F15SRF-siqXHxdFmRK1YAz5Qzk8RmDO37Vutqa3EMW63ugD2jG-Q9y4PoCiDs5nACd245qSfcbH6-KhFUB2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=pW49nIzmzcv0Qc-z9T66GK2nGUA8pdHQhto4lLQOI5Q4D43Tdn1WByN1iq7E1LzEC3ZtUa8GznvRJWm_NEWGqSxb5ixpQKsW9pf9l7jRq10Klj_cwAHOEyuRRGrz48toTljbaq-00yH4xd631Uup-gjZDsWVXr_QzgWniYBpdcKPyQ_PcAWPmj1EYowJauun6a8AdntVq-bXoISPXYtykCuqcsX8oPlquC5LRZQuH79Af5PdT1VY4LXfE4fAhpH0I1F15SRF-siqXHxdFmRK1YAz5Qzk8RmDO37Vutqa3EMW63ugD2jG-Q9y4PoCiDs5nACd245qSfcbH6-KhFUB2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک برنامه زنده تلویزیونی که از شبکه افق صداوسیما پخش شده است، مجری برنامه با اسلحه واقعی به پرچم امارات متحده عربی شلیک می‌کند.
در این برنامه که موضوع آن درباره آموزش شلیک با اسلحه کلاشنیکف است، فردی که لباس نظامی به تن دارد و صورت خود را با ماسک پوشانده است مراحل آماده‌سازی اسلحه و شلیک گلوله را به مجری آموزش می‌دهد.
مجری برنامه هم در مرحله شلیک تصمیم می‌گیرد به پرچم امارات که در بنر مربوط به دکور استودیو، شلیک کند.
@
VahidHeadline
صدا و سیمای جمهوری اسلامی جمعه چند برنامه پخش کرد که در آنها مجریان در بخش‌های استودیویی با در دست داشتن تفنگ ظاهر شدند و کار با سلاح‌های سبک آموزش داده شد. مجریان در این برنامه‌ها اعلام کردند که در صورت لزوم به جنگ خواهند پیوست.
این برنامه‌ها که دست‌کم در سه بخش پخش شد، در رسانه‌های داخلی بازنشر و در شبکه‌های اجتماعی با واکنش‌هایی همراه شد. برخی کاربران شبکه‌های اجتماعی این بخش‌ها را نشانه‌ای از بسیج در شرایط جنگی توصیف کردند.
جکسون هینکل، مفسر سیاسی آمریکایی، در شبکه اجتماعی ایکس نوشت تلویزیون دولتی ایران نحوه استفاده و شلیک با کلاشینکف را به‌عنوان «آمادگی برای تهاجم زمینی آمریکا» نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 230K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE2fnRhyeR8l5aUyHu6XErNnWQZ-jH5I9XdNREUPElv_9PZOzakUPqMXehYMoxB49PCjuFpZ5cI6vCC43nY0I3UgcuYMv34KiCOj9Eg0b9BBkilJt2G_c0rm-Zd-I9Mg9CU3vDct4m5euNYcyFK_mI5zwWWPhHyBydBXbJDlKJPommEpGpJIiB-lNsFEvBCR3KJybmT-Dc0wFJZHH4zU7PEVvN1CDKSzWAsbSJEWMfRLO0hyFR-dkvf_pzh8xKkE6W3CnAF2TQGKLicfImhuUqh7ddzSmKgRJZzJdnSzna9ppaEDYQ-P9mO802pZ3f-JdC3qmjjtyUfFGdpQL8yRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c9lvg2J0qpRDf06ear7d467K36BTinIDlDrml6ZB6AwKqH413qRuxQtTxm_va2sDiAezEfQY4BDtkIUk05oWGqhEDM7zYxGvn5bffA_McT8TU31AhG2UiFw2ato4jFKeg5_zGRfYD7KNq8-eB6wKz8Wde8X86aVsQa16LNR4BB9fW15hIt_m6QjacE6p004rRDyDRtutHxW2J-P_PtmA0l9hFb_Lt8cEZ2R_dq61QfDF_3okI-5j67yToIH9FJxWPCgWN4Cdbny5Gyv-YUtqNcgXR-4zNcbLu7EDlRk240m5R_J2FjrOmfkW8P6i06dylxMEZhICUUP7_BwHOi6LGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SlVaFzyIN3FFRXHrtAArCv-dQ-fHMS3xZ9TSW55Von2TuufS7Ub6w-zMZF7jmXMq7qfsCyrw3Nw3jJUT8gbqGMbq8_6F1rdZRssx5NMvT5MHATo9SW2qFl-afe7OlvMUYcArtGbpjlkSUOhn4hhr4kV9MNTjWJTo0XVFRWC1u4LZO7VlpRsmUSkuAi2YpHlqDLFouCqNFPh2TiRbpTe7MKniTaXPvOgD8mk4d_77OlNEid6PAep69TfIr--A0Ekd0xCokFcB-zl_Ax7541yECDIcd6ZitkEATsyMUc418JZZHeL07yEwvgCTmS3OSIaD1ZnpbmeH7bWdgAv02ecnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TvsLRKnQnnVHT7NjDMut5e_rd7pWA5S45wtl6C8fWA9PpZTqyToRBwXJvjMGJzOYC8drB7szbDsgpKoH_snCJAMdgEetMHc0jM5Vx4e5Gp6xL7Pw7mbOw1IuPLkYJ9RBPyWqwdicjcmK7mwDd9dAPBJ55ALCACK9914U1KheOFYil09IR0g6DqLmmUsANjZPhI1lJQmAeBgzxx3tgkwvgDnRcXCcWy8jCtamCSm565Nj5xlld0f-w9NBmNrkrK3NDcZnxCle0C1lAkW7BfihcdKp5XfvrJMHJUC6ShWcL8uh5knNxJ_rTEtbJMIY4tfJmJC3BcaevyDqcP2cnUbbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rACi73oqdjvMhrX2uPDgF0FOTkpPhuQVZ0EzI-vt0s8v4EpobgDP7WX2S4dN1l_Szc_OHCjLbG7TgDnAfaa89O8Ls6fmRnYbGfZ_CJxNY3H0n2VYDE_g-boTaeGapByQaXLX65DKEasWBi29rpQhtItMdrpHw6kpiucLPX2B8kCpOuRwGubDH_DeN2Af-w2Ub_icQOOgkh1OKQQwEbINnBNto9pd7OzfEWu6YU2JytTXNeAEumtDesWLP4ceXS9wrVPZ728Ocz244ibffSH7PRRIJTtsBzsn4BIPZK-wmhia5cMkX1eYboTmsHIqvdm-_ofKjdj94XusfToo0BFzsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او تاکید کرد: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت حکومت ایران از نظر نظامی به‌شدت آسیب دیده و بار دیگر تاکید کرد: «آن‌ها دیگر نیروی دریایی ندارند. نیروی هوایی ندارند. همه‌چیز نابود شده است. نیروی هوایی‌شان از بین رفته است.»
او تاکید کرد: «تنگه باز خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت و دنیا ادامه خواهد یافت.»
رییس‌جمهوری آمریکا گفت به درخواست مقام‌هایی از پاکستان، مرحله نهایی عملیات علیه ایران را متوقف کرده است. او گفت: «آن‌ها گفتند: می‌توانید متوقف شوید؟ ما قرار است به توافق برسیم. و واقعاً چارچوب یک توافق را داشتیم؛ بدون برنامه هسته‌ای.»
ترامپ در ادامه تاکید کرد تهران پذیرفته بود مواد باقی‌مانده از برنامه هسته‌ای خود را تحویل دهد، اما بعد از هر توافق عقب‌نشینی کرده است. او گفت: «هر بار توافق می‌کنند، روز بعد انگار می‌گویند چنین گفت‌وگویی نداشته‌ایم. این حدود پنج بار اتفاق افتاده است. مشکلی در آن‌ها وجود دارد. واقعاً دیوانه‌اند. و به همین دلیل نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا در بخش دیگری از مصاحبه، در پاسخ به این پرسش که آیا توان و مقاومت حکومت ایران را دست‌کم گرفته، گفت: «هیچ‌چیز را دست‌کم نگرفتم. ما به‌شدت به آن‌ها ضربه زدیم.»
ترامپ تاکید کرد آمریکا عمداً بخشی از زیرساخت‌های ایران را هدف قرار نداده است و افزود: «پل‌هایشان را باقی گذاشتیم. زیرساخت برق‌شان را باقی گذاشتیم. می‌توانیم همه آن را در دو روز نابود کنیم؛ همه‌چیز.» او گفت به تاسیسات نفتی و برخی زیرساخت‌ها در خارک حمله نشده، زیرا آسیب به آن‌ها می‌توانست موجب از بین رفتن نفت شود.
رییس‌جمهوری آمریکا درباره وضعیت مذاکرات با جمهوری اسلامی گفت افرادی که آمریکا با آن‌ها در حال گفت‌وگو است، به گفته او «منطقی» به نظر می‌رسند، اما توان یا آمادگی لازم برای تصمیم‌گیری ندارند.
ترامپ در پاسخ به این پرسش که آمریکا در حال حاضر با چه کسانی در ایران طرف است، گفت: «با افرادی طرف هستیم که فکر می‌کنم منطقی هستند، اما از توافق می‌ترسند. نمی‌دانند چطور توافق کنند. قبلاً در چنین موقعیتی نبوده‌اند.»
او در پاسخ به این سوال که آیا تا زمان دستیابی به توافق صبر خواهد کرد، تاکید کرد: «من کاری را انجام می‌دهم که درست باشد. باید کار درست را انجام دهم.»
او همچنین گفت مقام‌های ایرانی به او گفته‌اند محل نگهداری مواد هسته‌ای به‌شدت هدف قرار گرفته و «کوه گرانیتی» روی آن فرو ریخته است. ترامپ افزود: «آن‌ها گفتند فقط دو کشور می‌توانند به آن دسترسی پیدا کنند؛ ما و چین. گفتند خودشان توانایی دسترسی ندارند چون کاملاً نابود شده است.»
ترامپ گفت: «نمی‌توان اجازه داد ایران سلاح هسته‌ای داشته باشد. آن‌ها از آن علیه ما استفاده خواهند کرد. اول اسرائیل را نابود می‌کنند، بعد خاورمیانه را، بعد اروپا را.»
او درباره افزایش قیمت سوخت در آمریکا گفت فشار اقتصادی ناشی از بحران کوتاه‌مدت خواهد بود و افزود: «وقتی مردم توضیح کامل را می‌شنوند، همه موافق می‌شوند. این یک درد کوتاه‌مدت خواهد بود.» ترامپ گفت پس از پایان بحران، قیمت انرژی «مثل سنگ سقوط خواهد کرد.»
رییس‌جمهوری آمریکا در پاسخ به نگرانی‌ها درباره افزایش فشار اقتصادی بر خانواده‌های آمریکایی در پی جنگ با ایران و رشد هزینه‌ها، گفت شهروندان باید این فشارها را تحمل کنند زیرا به گفته او هدف، مقابله با تهدیدی بزرگ‌تر است.
ترامپ در واکنش به این موضوع که برخی آمریکایی‌ها افزایش هزینه‌ها و بدبینی اقتصادی را احساس می‌کنند، گفت: «باید تحمل کنند و باور داشته باشند که ما آن‌ها را به نقطه بهتری می‌رسانیم. اما من باید کار درست را انجام دهم.»
ترامپ در ادامه، فشارهای اقتصادی ناشی از بحران را با ضرورت مقابله با جمهوری اسلامی مرتبط دانست و گفت: «به مردم گفتم متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا همچنین گفت کشتی‌های حامل نفت ایران که چین در روزهای اخیر خارج کرده، با اجازه واشینگتن حرکت کرده‌اند. او گفت: «ما اجازه دادیم این اتفاق بیفتد.»
ترامپ در پایان در پاسخ به این پرسش که آیا حکومت ایران در نهایت عقب‌نشینی خواهد کرد گفت: «بله، قطعاً. هیچ شکی ندارم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75494" target="_blank">📅 07:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzeAZeu8U8iHW7G3_EKrjvIvujhHS9elfV7-gutKX1LYu7r1u_0-XINQMa-TZk1WNZmIJ_RA2mIBpEkKnq7NnhxSH42oXkDLjAaHNS34VjT_0ZoJnATYH2UcgllwyoPlVKgkeruaLKGP7Gm8JsZ6EpB-_uoMNjeBmvQZnAx4qc97mrHYS92KgYjsUbRZBnhL6qqB11R-mdbuY4HeGC5SpoJEn1rJM8GzvcvJpYNxol6zVxEI0iLYtlfqPpIQWL2NTDI0ZiOMR39uMmtiXP7QH7EuXypyf9xpWeRXxNFT6hmiQS_EShcdN4dASpxqj5tD5QkKzVdoZDW3is1Yu-HQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در واکنش به بالا رفتن قیمت انرژی در آمریکا، در ایکس نوشت: «در حال حاضر، افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید. درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.»
او نوشت همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است، اما تمام این‌ها قابل اجتناب بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75493" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izOZS6aaaTapmyJEzcdoAOvh7mtwf91EsLRARm2cAJYr04UQjwG0tXZKBPe5WaaANcLwewVoKD9EJzR1cq1RUi6WANQ_jZELPX1_NraIOGq89UTXxglG2Rj2ZxQhJ5sb2RvFJj-U1j0B5GR4veVI-bIApCpAm0o2-yQm54lTOqan5Adt-0x187ZhtxzAA9TuZwx_9JuaPdRM7Y7_4fKIru1ryZxDTduCosGe7dLO9IuP4glY6hZWwaXThpKE-NuaJos9RgOchlN6Pq8AZ9jXyvi9UMm6BIysyjqWndd1fJxYSQKdCxAeq56LnkCTQTUqzrkV2RPygYSFfTlUrIPjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نماینده چین در سازمان ملل و و رئیس دوره‌ای شورای امنیت، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین درباره تنگه هرمز انتقاد کرد و گفت که «محتوا و زمان‌بندی آن مناسب نیست و تصویبش کمکی نخواهد کرد.»
به گزارش رویترز، این پیش‌نویس قطعنامه از ایران می‌خواهد که حملات و مین‌گذاری در تنگه هرمز را متوقف کند. اما دیپلمات‌ها گفتند که اگر این قطعنامه به رای گذاشته شود، احتمالا با وتوی روسیه و چین روبه‌رو خواهد شد.
دو کشور ماه گذشته نیز قطعنامه مشابه مورد حمایت آمریکا را وتو کرده بودند و متن آن را علیه ایران «جانبدارانه» خواندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75492" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PO3T0xnh7IgzdakJ0fPZTLxlv2e5Z5JgDspBeQOHYwuFTYemUAzhUaL6ot3Zdjb7BpWu9ypBcBXf-SdKJNqKyN7V-7ymkLL-dOdz5OINq6rSjb7159h-dTmdeFahDW8CotvRE-bCZtyi0zjHejOqANOuZNPDUE20GbO8FoCcA-I2Oj-WZAV0ePLFgBbYf22Q0I6XwLZdHX8JFDABYiResKN1vIJXi9UFiCRckEkVkEpvoG_lHu-pIF7qURR6L3HvCkC7VME--PrdCAiCkVH8-LM-vmSrmrMsPHqzJDx8dvSd4ezPpTlsDIrb0ibRbL_r0d3gU5QB1r49oB_cJ4TmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند عبدالرحیم موسوی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، گفت که جنازه پدرش که در نخستین روز حملات اسرائیل و آمریکا به دفتر خامنه‌ای کشته شد، نزدیک به ۳۰ روز زیر آوار مانده بود.
موسوی پس از کشته شدن محمد باقری در جنگ ۱۲ روزه، به‌عنوان رییس ستاد کل نیروهای مسلح منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/75491" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m8N1TuUdk-gGAJh2O0PmIkgafevDJQUUqhqDRRv8mx-WYeYZgJENjkbVVAbHrjMDbUBqdKC7Z1_r4mIWuTvJ4pjE41AlVNXEMf1wCV02SKsCGE9uIaWrxfSpqXlqx-I-QGQpC97ZwEfrN320fyXAumSqCzr8uqsjy9y31ZGl0IP-pv1UgvfGDZcA1pEOJg1xrrUl0fmMm8bItcuXTv0FloahbpPsO6nQjxvyZIbpk8a4V-nfX2xLYvCkiklNKvOEGDZCdJqquXTc1aU_iND-Pnv6a2TqjL4lL2dCZYHndBv1xE-pPN-_HgoU3pt5Zu14raiBiBQrnJzHkz4NuWMK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db61779f21.mp4?token=SpKdUyMBw9H9Ck9LqxuXKCZCKOMcO6hlXWzdThUHTDDEHl5z4f5lXxNF33kmlC0YHRBF0-DOCVW5o-PIgIlEg3OcZQ2uAczA2um5_BkquOWS5IJuNA53xhY-3Mr3V-zfwAC5WaPF541LhiCzhG5RDwQdmDBSmCwhH8hJ6bj4n-Jd6Wk8tM-ZaPC4rglNPtNF13WnDpDm-ShBu0IoVK_6rLv47WzeUf04uga2Zgobboz2Yl7qOu6YGtQscPEu9N2yModEjF4ci-PJooym3FDC1Vklp_Zu4487EZj8UN88_Clc-QapmP1VDLDPLsjScDkrz-THptGwix5feqMQnst6Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db61779f21.mp4?token=SpKdUyMBw9H9Ck9LqxuXKCZCKOMcO6hlXWzdThUHTDDEHl5z4f5lXxNF33kmlC0YHRBF0-DOCVW5o-PIgIlEg3OcZQ2uAczA2um5_BkquOWS5IJuNA53xhY-3Mr3V-zfwAC5WaPF541LhiCzhG5RDwQdmDBSmCwhH8hJ6bj4n-Jd6Wk8tM-ZaPC4rglNPtNF13WnDpDm-ShBu0IoVK_6rLv47WzeUf04uga2Zgobboz2Yl7qOu6YGtQscPEu9N2yModEjF4ci-PJooym3FDC1Vklp_Zu4487EZj8UN88_Clc-QapmP1VDLDPLsjScDkrz-THptGwix5feqMQnst6Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتز، وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور، عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده است.
عزالدین حداد، از فرماندهان ارشد گردان‌های عزالدین قسام، شاخه نظامی حماس است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/75488" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZb17GCqkN5-aKSSqf8sy5n1oXqjLFgErzDNN7m2MWiTUSErieGQd7nZnqTyvpROtbPAJXgRfQzh3u3q7liqQVCvOzh5bRLQtKFTX0AFnCwAsLQIIows7WgAfFaDHKb0lGfaDLghlSV7_Rgb5DJarPwXBhyHTdmoqc9gfQtreuB48Boy6gjbGQHxT_PD9Z_pzaAYUApZW_4xADAE0r7xO7b84Od1BVpdtHjxEL9yo94Drxm1phtr50LV6mZjpblne-W5HpPk0bcehxIt7HXV1rGZV7EvxIWzrLS5s2w6DaaaKPzpuA8pq8TP_Eo0rgqawnZGNg_AOh9sfS61QMQT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا سپهوند، عضو کمیسیون انرژی مجلس شورای اسلامی از کمبود روزانه دست‌کم «۲۰ میلیون لیتر بنزین» در ایران خبر داد.
به نوشته خبرگزاری تسنیم، این نماینده گفته که تولید روزانه بنزین در ایران بین « ۱۱۰ تا ۱۱۵ میلیون لیتر» و مصرف روزانه بین «۱۳۰ تا ۱۳۵ میلیون لیتر» است.
سپهوند با بیان اینکه «در کوتاه‌مدت امکان افزایش تولید وجود ندارد»، خواستار جدی‌گرفتن «مدیریت مصرف سوخت» شد.
پیش از این وزیر خزانه‌داری ایالات متحده گفته بود ایران به‌زودی با «کمبود بنزین» مواجه خواهد شد.
اسکات بسنت با انتشار مطلبی کوتاه در شبکۀ ایکس، نوشته بود: «در حالی‌که باقی‌ماندۀ سران سپاه پاسداران، مثل موش‌هایی که در لوله‌های فاضلاب غرق می‌شوند، گیر افتاده‌اند، به لطف محاصرۀ دریایی ایالات متحده، صنایع نفتی آسیب‌دیدۀ ایران، در حال از کار افتادن و توقف تولید است. پمپاژ نفت به زودی متوقف خواهد شد».
او سپس پیامش را به سبک دونالد ترامپ، با جمله‌ای که به‌طور کامل با حروف بزرگ نوشته شده، به پایان برده بود؛ جمله‌ای با این مضمون هشدار آمیز: «مرحلۀ بعد،‌ کمبود بنزین در ایران!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75487" target="_blank">📅 21:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=t2Kr5yEaCbsBke7byLl_emq8nhda3RXwnvCjNsDeoERufR_qDFPJyfX73aaFSLdfiT3lCReMuJBhCezEd-06UH7FluKqH8Uty_xuP0ErPPLEk-pPekGThgCynKlq3TN3Wk3T59jLS3GeI7RxriCWukkaaxqymOtbCPMy6H5ME2NuNSyOLjCyE3U-0enkt578eOVmByu9b3bhaqZAmNEwGdTMcsr45QlbttwfXT9EoPPFUQF36pkehf2Xpb2-qj0gM8h6L5BqT2P7n1DzWYURovYWQSE_FMQu99xDw0yh5m3na0AUH7IBVnfpbSrhuk9gxySfzzUaOtw7AZEW83j4lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=t2Kr5yEaCbsBke7byLl_emq8nhda3RXwnvCjNsDeoERufR_qDFPJyfX73aaFSLdfiT3lCReMuJBhCezEd-06UH7FluKqH8Uty_xuP0ErPPLEk-pPekGThgCynKlq3TN3Wk3T59jLS3GeI7RxriCWukkaaxqymOtbCPMy6H5ME2NuNSyOLjCyE3U-0enkt578eOVmByu9b3bhaqZAmNEwGdTMcsr45QlbttwfXT9EoPPFUQF36pkehf2Xpb2-qj0gM8h6L5BqT2P7n1DzWYURovYWQSE_FMQu99xDw0yh5m3na0AUH7IBVnfpbSrhuk9gxySfzzUaOtw7AZEW83j4lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
نشت نفت به
#خلیج_فارس
پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
#جزیره_مارو
[با کیفیت بیشتر:
۶۰ مگابایت
]
KavehMadani
برشی از سی‌ثانیه سوم ویدیوی بالا درباره وضعیت ساحل بیشتر مورد توجه قرار گرفته:
AzamBahrami
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75486" target="_blank">📅 20:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfFUmIg72KAJg8BqWAkYaEzZp-O1-uj-18kWZ4i7yMs0Yn4A3h4i7P8PipCeHuEkc8Z4m-8goOnhfProE53YRkrhsCGGMUk_9gXeF7bwxwGVajmGJo6iazonpx_Kd7I3hvgvxAL4kgz9c-HB47LcPEwOu03jVSA6W2UenOiJIdCpBHYS3dKw8MtXl78MZSBJFj1G2uUNI4HptoH91wJcNak2f4b2-ro6qXOK9e92_L4DrUePahIX1j-PqQSuTVXSveEqiLdO9Lk2BRtZB5UwZVh-F8D65ZxxaTs_Uirq1_u9U6bflxQgrKoTrXBHtCCW5Ep2Ps0VYd4z3T-uQQhbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان اعلام کرد که یازده شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا در آب‌های آزاد گرفتار شده بودند، به اسلام‌آباد منتقل می‌شوند.
اسحاق دار افزوده که «تمامی این افراد از سنگاپور به بانکوک رسیده‌اند و اکنون سوار پروازی شده‌اند که قرار است اواخر امشب به اسلام‌آباد برسد. سپس بازگشت برادران ایرانی به وطن خود تسهیل خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75485" target="_blank">📅 19:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlpYWq_UY3gAI-NU6GxxASqav6wZ_JYkgR-L-fmKNT6HgGfPJw3JGtBxIcX-YaoIB9HiKee5LpQLtZNe2UASWILQwMCMRL9c5IcPMfP9r4N46G2MKOnmFBeXU2YcDGWxyLUw_O0gUFwIKPsWizqOTlN6GPM75k7rO0p3cR1da1kQPujL0OtMVg-r1HxIpKtU2BAEpRCcvfloCMbFdMb02GMl194Q_AozNsVRb7N4Nnfwu6KD-CgPNm6kV4DvWSWP50GcV9n4S1u5hcR-2qlgAHNmOWfs54pWfxjju3iRilUiAzpLXYqz85IdT8_p4hkOzcFtxTkSGQU2ipKDMi0tCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s4PGWlO7YH5nNTfBlHjxqfFcyEgk28ZMRijXS37Kbp8Ky_QCADX5KYOQ3kb5gzMG5up_mbii3S-Lk2u8U_g9498r7aK7c97Q9WsmOH4YQDhRcHZlv9ygl6phNqGwqrOcNZ6uRNIfBruBshcMvfFki5zVrzGH3G1GvfFAgUelhZAwIs3FyVdYZuTd6VgveE2I_k4NHJRXMeOIr8AyQ6CgnmNaPQeP_msn8aZ9VkzLeAHktK0TdCjcss7vj8_j4NaE8IYkWIgre2PHRYf8N-_fvcI6PSjj8l0eA2OyMU4E9p1GQd187wvwrG1IA8Foz1jkG6awcJD7MFjfRL9KwEJMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k8P8ZmhPF5A9crDNfiENrKnAwsqBB3SJ3ubNtNNFc9BlM3C4YpXj35Xi0891I4gUsvr7u4juIiaA221hYDb530OTh3MwdmqN1VrOwTl3n1vpApTEaWxGiFlhyQuSgJtX7nVZ572lyh9qLUubOQw7s6BBryQM1uPKi78ZAiPlWjhIjKCeKbtiJ66KEA2iRtvSYeLt5MReleY0PBi2E3hCVjInIJ7a-nCSNmaUoiahvnnBzN_iBTsS_aKrLngzp6D-kjb4kyWyw4eAbzGFQJLmesD32kQWwyT87AvwEafLyBwPNNtSNxvWC-tBVUdzymSqeyIRdGeGH2nUNNj0YL8k2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MqYtpJ5p8jri7iGY0EsK1iziEQS74hQwOT1RK3Xl34jNX0kgUZvegs813IPSWpJ_eUu80Nfkq_M97ea91sZa6C7uHn7JgT0wkhVTrkHW4zKZqUq3JpYsa-nrYGjRU6h-827BIJ3gJkUzgiiZFwgiKJEK-JQEaEuHSla4-K6PspPOc9YsFVBLw3mIflY5HnCx8OfV0vzXNJ-yOUrxtMoZhrzgRBYo2V4pMjB5UQI8c3T_Ff9VERNOybTptowsrC8QtSMa0VaboIUfzMVAC-nkmKE1Em9n_LXYW5UkIiGoifkWoY2bi54pZBB9wh5OoaE7yLbDD1cLIE2WB6KmcqLhXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=JS7xAIriCvgFFrhHTZkacifdyO2v8s_eVMlD9rKfrB3WaSuouoRk_HJBnhT8Zm_mAmkRkBupXlZSkNfrrk-LS3GqK2eq0tB8Bo0dP9ayCV72wCLQckJEElGxsdw90bGsApMVILf-rpC3znTm7eHPeRHkzUsWfTSAJxI3J7jRTXdTFT9KWl_J68jIR4txnRrVqjTdM3NfUIOJLhnDfNafscesqboxlB2M0oK6Qss3mku0-LkNGlPrHasN2giUhdYNKVXWU-0EZ9ZhpPyRbWf0k6e4XBhDVNLpBbSpi33_vrcBp1Bo8iVhZJAevUm-cJlcDz9wZlsa6zvgG7himm_r5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=JS7xAIriCvgFFrhHTZkacifdyO2v8s_eVMlD9rKfrB3WaSuouoRk_HJBnhT8Zm_mAmkRkBupXlZSkNfrrk-LS3GqK2eq0tB8Bo0dP9ayCV72wCLQckJEElGxsdw90bGsApMVILf-rpC3znTm7eHPeRHkzUsWfTSAJxI3J7jRTXdTFT9KWl_J68jIR4txnRrVqjTdM3NfUIOJLhnDfNafscesqboxlB2M0oK6Qss3mku0-LkNGlPrHasN2giUhdYNKVXWU-0EZ9ZhpPyRbWf0k6e4XBhDVNLpBbSpi33_vrcBp1Bo8iVhZJAevUm-cJlcDz9wZlsa6zvgG7himm_r5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز جمعه ۲۵ اردیبهشت در مسیر بازگشت از چین در پاسخ به خبرنگاران، درباره آخرین پیشنهاد ایران در مذاکرات هسته‌ای گفت که آن را «از همان جمله اول» رد کرده است.
او با بیان اینکه محتوای ابتدایی این پیشنهاد «غیرقابل قبول» بوده، افزود: «حتی ادامه آن را هم نخواندم.» ترامپ تأکید کرد که صرف تعیین بازه زمانی مانند ۲۰ سال کافی نیست و آنچه اهمیت دارد، ارائه تضمین‌های واقعی و قابل اجرا از سوی ایران است.
رئیس‌جمهوری آمریکا همچنین تصریح کرد که، هرگونه توافق باید شامل انتقال کامل مواد و سوخت هسته‌ای از ایران باشد و افزود که توافقی مبتنی بر «حرف‌های توخالی» قابل پذیرش نخواهد بود.
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره پیشنهاد اخیر جمهوری اسلامی گفت این پیشنهاد را بررسی کرده، اما به گفته او، اگر از جمله نخست یک متن خوشش نیاید، بقیه آن را کنار می‌گذارد.
ترامپ در پاسخ به این پرسش که جمله نخست چه بوده است، آن را «غیرقابل قبول» توصیف کرد و گفت مسئله اصلی از نگاه او این است که ایران نباید «هیچ شکل» از برنامه هسته‌ای داشته باشد.
در ادامه، خبرنگار از ترامپ پرسید آیا دوره ۲۰ ساله برای او کافی نیست. ترامپ پاسخ داد که «۲۰ سال کافی است»، اما به گفته او، سطح تضمین‌هایی که جمهوری اسلامی ارائه می‌دهد اهمیت دارد.
ترامپ گفت که اگر قرار است توافقی ۲۰ ساله مطرح باشد، باید «۲۰ سال واقعی» باشد و نباید به گفته او، توافقی مبهم یا ظاهری باشد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز جمعه ۲۵ اردیبهشت و در زمان بازگشت از چین به آمریکا در هواپیمای ایرفورس وان به خبرنگاران گفت با وجود آنکه نیروهای مسلح ایران در جنگ نابود شده‌اند، ممکن است نیاز به «یک پاکسازی کوچک» وجود داشته باشد.
ترامپ ساعاتی پیش در گفتگویی با فاکس‌نیوز هم گفته بود که نیروهای مسلح جمهوری اسلامی در چهار هفته گذشته، تلاش کرده‌اند تا تعدادی از پرتابگرهای موشکی را از زیر خاک بیرون بکشند و جای بعضی تجهیزات را عوض کنند، با این حال «آمریکا قادر است در دو روز همه این‌ها را نابود کند.»
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره اینکه آیا شی جین‌پینگ، رئیس‌جمهوری چین، تعهدی قاطع برای فشار بر جمهوری اسلامی به منظور بازگشایی تنگه هرمز داده است، گفت از کسی «درخواست لطف» نمی‌کند.
ترامپ گفت: «من درخواست هیچ لطفی نمی‌کنم، چون وقتی درخواست لطف می‌کنید، باید در مقابل لطفی انجام دهید.» او افزود که آمریکا به چنین کمکی نیاز ندارد.
رئیس‌جمهوری آمریکا در ادامه گفت نیروهای مسلح طرف مقابل «اساسا از بین رفته‌اند» و ممکن است به گفته او «کمی کار پاکسازی» لازم باشد. او همچنین به آتش‌بس اشاره کرد و گفت این آتش‌بس به درخواست کشورهای دیگر انجام شد.
ترامپ گفت شخصا چندان موافق آتش‌بس نبوده، اما آن را به عنوان لطفی به پاکستان پذیرفته است. او از مقام‌های پاکستانی، از جمله نخست‌وزیر و فیلدمارشال این کشور، با تعبیر «افرادی فوق‌العاده» یاد کرد.
@
VahidOOnLine
دونالد ترامپ گفت آمریکا ممکن است در مقطعی برای حذف آنچه «گرد و غبار هسته‌ای» نامید وارد ایران شود. ترامپ در مسیر بازگشت به آمریکا و در هواپیمای ریاست‌جمهوری، ایر فورس وان، به خبرنگاران گفت: «در زمان مناسب، یا وارد می‌شویم یا آن را به دست می‌آوریم. فکر می‌کنم احتمالا آن را به دست می‌آوریم، اما اگر به دست نیاوریم، وارد خواهیم شد.»
او افزود: «فکر می‌کنم آنها کاملا شکست خواهند خورد و ما هیچ خطری نخواهیم داشت. ما تجهیزات لازم برای خارج کردن آن را داریم، هیچ‌کس دیگر ندارد؛ شاید چین چنین تجهیزاتی داشته باشد.»
ترامپ پیش‌تر نیز در ماه مارس در کاخ سفید درباره ذخایر اورانیوم غنی‌شده جمهوری اسلامی هشدار مشابهی داده و گفته بود: «یا آن را از آنها پس می‌گیریم یا آن را برمی‌داریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6PR-2ZACdF1bzxRO8KDk1OG3yuRnrc8oYKMFanJ7uFvxLAUjbvS53cjjFsxUIGSa2Tulygalbl0L5Mzzop-FJQc7w_ZL7wt9lUBN08rZtGxs6NCoB_oGz2S550XV-mX6oI-N0yv8vpQc3uNy39SFdmJx_w_qGVkecjGZbyzXGz1KqUfpoE6EfC5kyMDX2NW6X764Un4_SDTrPBsH7QylFg8a00ksgxPGUbSlQJ_1vTmhMuxa4hlH7RX-RvmGT7D_T8-I5mle2yhePEPFUrEWMrorKxnUYwMrE4keUlKONQX0C6LnJnL7uT0PeUO25SuCFK303UwurhNQAol4oIUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGyqawSYccTXUWUNR3TXMNNEbwVVM79bm1LxZDVDTm4c3V-5lbm5h5BhGGgZXgxI2u8qyZpkk34xFijhWeSUOfTHdHu7At5YHGTh2bVKMOp77TR6JNR2bAUv3-GvaV4ML2-JkomqziomgEkd2we2QjjxA5zt2MEKiZc4DukZv4_Y-NG9a1ZIdzPq-Tj7faNyJTysHNlXSx1AFpgwneQvpLX0RNBwlqoBZXk3Kp-IqBwI-Hp8XOvMoHV0Izp7_pyverDbqFBqapLAA2ZgdtatICbr1q7hEWHttX9ngEx9cxRTg8snrNJPCD_I7qb4FeOjpwH1t7GZp44C2UuBuwl7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G5WjpN0Bgy3K-k0P2DTneQKqgftPa8u6CyUUpdewfPHr5WaIihR2qPwrzkGWPHTefFXsOhvhHCpbRaqhozWGjQ6v92GYzuFQSDuDpje36H4TCqZk1uxqSKQ-wLRnREGE74N0wskVwRvsWll3-3K6JzLf4s1vfqr700LnPttJUhe_MVf3kIGALRn0NEj9wNEXQ_Ou0aLhOCMZdA4cF-bygsuHwE7SFktU5WkQb3mTOaTj8r9-qfHW2BuUwskiZkdw6ij4Vi1Rfa1wA3VXwuEyd7QYMtfX8UKs6HmMH2xx9yKVOuMaoNGBXXYt2B4ywYP9Qmp4HLFnSKJIDAUPS3uJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lUzEJNpOM1fH6Utow2FMv-z-06g0OBSPjn2WtUwavuLNljNw2zvujEb3V5SOQICGffsHVMWYFaDfyaWKkUzs6XlkxyeW0vrSddyy-x9p77Ds_-4iHR2TFxoNT6g4jGKxYESXmF07jc_5w3H1vzL0CfHUu0h1ahsfn1UJsE0NjdXq9A0gQ46oA3sczwABRH8TyT3uj11eY-pI4ebZ0aTAf3y7Ax2ZpGZAejpP6TZNjF-LN62luOB1VkZ0Mf-28fSBlq4f56ILKZEMqHR3lvti5Vm7EqTWu0Ko8NHJhNsecp1tht1ksQ5DbpUS-yhnWJuh-uLicOsOUhdm5-o6bgAu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UTPIq4mVScY2_nbjTMd58avmPwl-DkmMZFCXBzrdvkO4QJoRiOuHPSUA_BUyFJ--B81ThQmwIvNR7G8Lh_TWJ6cNzFiqALRtGquaE9ZceQSb3FCvHvku_PinlmpVuFUpVmWcnBaNug-Tf5bjPpy21QWHNtXg_9FDZLiKIXBebiK4VkNsiaBKKyBx2ZT2VA1-EHwqbceIYUP7S5yQa5i5AbWT4_Lnwnq1k56Yfl7MZ5U1VJVqCNBy-dC44lZLfO92CysoHTdXw-TyMLngThsoXasG6o8viIYjrOJHwOaKBB_p0tD1-gsMZXHpgd5AHRAaM3VzkHKCBpbzGNu7enz0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ebg8DD9UJrczW50yDs4n6dQ3e1nttjWEWZFAhIeM3LK81Gdtb86N4ITImXySIUO3KMZNrqwCnOLL65Iz6g35ZbxSzNXF70OcTS5L4OBJggiNw6FqsO1D3fBSdt0oYHPqWwAS2Eb3j-qsF9v49lLUCh7DfUjBSXHeWW3aLLDtwSd-q20WM7Toy19QBLh4Uw2JWQYrpcPR475AdrU9AiR0KackLK47och333w9mZMY5-iuQzrcE8s3wupsPwi73p4NUL4dsQ4aqKSHok6U4tm2qgLbVQ1oejq9SqgBmKuvCubjfg3cBK3yXUvOTUYyN__obhWG8KuAcOx6vYxlL-3_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fTgb1XMPcWXoYaYsrlXsmZ5BQIcrCxymh0n7HqELm-_zBCM7FyCqlM7WtlzsoSuVFMSovq7Q1uK0OIXT9JIhQJ32VxBekTQMHbVz3uMnskED4UQ7fw3EiIYd9Wub4g9r7JXjY1yPqdog-jXzqG3TIh3uNAvBmOpfT3ymEog7a1RPfBFDpa546NzY00xU4_FUuEgUsFnMJYYBV74XL_8-rwwRgdY18AXPKntm_fkzC8f1cfuwhBEjeS8cIiJIc4IPnTS5UcNurEpcmS8XHIaZq1hU0gNyUMllE8ZxkfchGaD7eCTBykohCBPWRH-LKPWCzEu_4Z5Yb98AO0Q8KpeaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H0wUEbhvksW3N1X0_fBM5PZu4gq2Hkv141DRfq1LaMCufyK4IzvF9ZQE8dTPc8M1Mh7NlbBk0IpyVPV7b_rXSGOGlrBQW3SovU1zkK1Lur-zAjXgA0UW7yD4fW2gnoQx_v8MWpcTCzTaOoY7v5jZFvAafTrKakUKxGX4hEgDRdEM52wbZl2DA44gWT5GZVDTFB9Oy4HCLr8TPiGjDXEJNQZaSGzDF0oZfeZCUL-ST_5JSL969nCedU29MNz6NkutNpFTX0BR7r4U0aPCo5D71K-S2Cl_DMaV6mBT-qC5Lucj0TSGfPJNotK7ige2SVSnojk2h14xq1RQ5D-Vkmm9rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در مصاحبه‌ای که با فاکس نیوز انجام داد گفت او درباره ایران با چین صحبت کرده است.
ترامپ افزود فکر نمی‌کند که چین هم خواهان این باشد که جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند.
او گفت جمهوری اسلامی می‌تواند یا «توافق کند و یا «نابود» شود. رئیس جمهوری آمریکا گفت نمی‌خواهد چنین کاری کند اما آمریکا قوی‌ترین ارتش جهان را دارد.
ترامپ گفت ما در جمهوری اسلامی با «رده سوم» رهبرانش طرف هستیم. او گفت رده اول و دوم رهبری نابود شدند و فکر می‌کند رده سوم از رده اول و دوم «که دیگر با ما نیستند» «منطقی‌تر» و از لحاظی «باهوش‌تر» هستند.
او این تغییر را به‌نوعی با یک «تغییر رژیم» مقایسه کرد.
ترامپ با اشاره به اینکه جمهوری اسلامی «پنج روز» زمان صرف کرد تا به پیشنهاد آمریکا که «یک ساعت» هم زمان نمی‌برد پاسخ دهد، افزود جمهوری اسلامی در داخل خود «آشوب فراوان» دارد و «چیزی به جز آشوب» ندارند.
ترامپ در مورد حمایت چین از جمهوری اسلامی گفت که رئيس جمهوری چین، شی جین‌پینگ قویا گفت که به جمهوری اسلامی سلاح نخواهد داد.
...
او افزود «امیدوارم» جمهوری اسلامی این مصاحبه را ببیند چرا که آمریکا می‌تواند به سرعت همه تسلیحاتی که آن‌ها در طول آتش‌بس ممکن است به آن‌ها دست یافته باشند به سرعت نابود ‌کند. ترامپ گفت «ما دقیقا می‌دانیم چه کاری می‌کنند...و هر کاری که در چهار هفته گذشته انجام داده‌اند ما آن‌ها را در یک روز از بین می‌بریم.»
رئیس جمهوری آمریکا گفت جنگ را می‌توانست «چند هفته بیشتر» ادامه دهد و ماجرا تمام می‌شد اما به درخواست چند کشور آن را متوقف کرد. ترامپ گفت جمهوری اسلامی دو گزینه دارد: «یا توافق کند و یا نابود شود.»
ترامپ همچنین درباره خارج کردن اورانیوم غنی‌شده از ایران گفت این کار را بیشتر برای «روابط عمومی» انجام خواهد داد و او احساس بهتری خواهد داشت که آن مواد از ایران خارج شود.
رئیس جمهوری آمریکا افزود «به‌دست آوردنش پروژه بزرگی است، واقعاً پروژه بزرگی است.»
او گفت: «اوایل به انجام این کار فکر می‌کردیم، اما زمان می‌برد؛ حدود یک هفته و نیم طول می‌کشید، و این مدت زیادی است که در قلمرو دشمن باشید.»
دونالد ترامپ توضیح داد که «باید این حجم عظیم گرانیت را جابه‌جا کنید. می‌دانید، آنجا گرانیت است. گرانیت سخت‌ترین سنگ است. واقعاً شگفت‌انگیز است، چون بمب‌هایی که استفاده کردیم فوق‌العاده قدرتمند بودند. و یادتان نرود که علاوه بر آن، با موشک‌های تاماهاوک هم آنجا را زدیم.»
او گفت فکر نمی‌کند خارج کردن آن مواد از ایران «لازم باشد، مگر از نظر روابط عمومی. به نظرم برای رسانه‌های جعلی مهم است که ما آن را به‌دست بیاوریم. من همان کسی بودم که گفتم آن را به‌دست خواهیم آورد، و به‌دستش هم می‌آوریم. حواسمان به آن هست.»
ترامپ اشاره کرد که با «نیروی فضایی» آمریکا که ابتکار او بود همه تحرکات در اطراف سایت‌های هسته‌ای در ایران زیر نظر آمریکا است.
او گفت «من ترجیح می‌دهم آن را به‌دست بیاوریم، اما مراقبش هستیم. دقیقاً می‌دانیم آنجا چه اتفاقی می‌افتد. چند روز پیش مردی تلاش کرد وارد آن گذرگاه شود. دیدیم دری کاملاً متلاشی شده بود. و ما از همه‌چیز خبر داریم. اگر هرگز حرکتی انجام دهند، و این را هم به آن‌ها گفته‌ام، اگر نیرویی بفرستند و ببینم کسی تلاش می‌کند، تنها کاری که می‌کنیم این است که با چند بمب دیگر آنجا را می‌زنیم و کار تمام می‌شود. آن‌ها چنین کاری نخواهند کرد.»
ترامپ گفت: «به آن‌ها گفتم ما در آن محل، در آن سه سایت، ۲۴ ساعته ۹ دوربین داریم. دقیقاً می‌دانیم چه می‌گذرد. هیچ‌کس حتی به آن نزدیک هم نشده است. در ابتدا بررسی کردند و گفتند هیچ راهی وجود ندارد که کسی بتواند به آن غبار هسته‌ای برسد. اما با این حال، من ترجیح می‌دهم آن را داشته باشیم. ترجیح می‌دهم به‌دستش بیاوریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTW2ygwJnPndnyqUAiKwieFIB5kNvH_ealReKxd62vOyYMBPBNUyGbbSHbfhPCs9QmXDaXSdluHtRXVHgGabj-HKu2k0ETfMJyQR97oyTpE9hDHpSI3IPAoo-efdAJ3B6JTWkckYDbsuxloTWY-YCL7PmHsITeQvm2PeOXQkPPXWLrlTRqDAYSZV7H8W7-CLJceMIv3rUAYbM6aiQTYoRCtu6OxxiOdWTi1YFx3YiMBFjG2O_opEX0TfBgBR98hWwhUC5q3mKgXJX1oneFX6yTqhgTqPm7Z9Ouk09d6G7F9SPg928l7C5wEPTnt5Ck3rloTnlym7WoGB7hzO6fRHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8EIzLd6FT8kyToDaWJ7tm6L2W4pCN9tjJ7t3wiPHuM1jTrAzYDpGKNJr7k4IUiVXCe6BOcvOVu7kOqRIjNdnShrY3SvGt3FvGjr-jozg-uJMzKv8ub9MF3UM-gk-TON93Qj3Z5AI4uqRoPVKypxeH7ZbZrOcmpiG5yY1E6bOr9qxwJ2_k1CWj6s78MxmMB1D7Ai9VERz1qmlLAxDPFxiBMVhLmwGWGOYS9mbW1jOx2moHJHRywbhcOKa1sOHQ6jyxV_UI2fyg0spQ902ZJM_gX77zP3WzxXgZYQQp_LCXit4FxKw0JwqXvAoBHE9Cw-NBsWKVH355PjowpNcfyB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T715SREU4Q7VxQVlURJN56Rw9kqnwsiZcEwGPOjyDj_PDIejhLQjIG_UIWXjDNFbYGR9bTexqgcQ2aB45YWreEkd-G_NLqhnuSbbO_7PMPKZJAgNKTjqQ79DCH5hSqkNYwuWMtv498VtxnkmQz6EZq-ZgbWLaJyJXdy6B6144KRi4bwPKBQY5wrdwn0pMYrTjzdCt0dBziW4Ka6haOvvgyKkYbXSTE2IpUauohu22hNn1m-4X5FElY-LscwbYDWmDa7tcaqPAGdnIT2BUxG8oiyOmmpLpw7SrY_QQkDPdrrahuvW4bKzmTWMvRyimPVpvZgxuEgSHK9q5RwlVnhbBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، اعلام کرد که صنایع موشکی، پهپادی و دریایی ایران «۹۰ درصد تضعیف شده‌اند.»
او در یک جلسه استماع در سنای آمریکا گفت: «تهدید ایران به‌طور قابل‌توجهی تضعیف شده و این کشور دیگر مانند گذشته، در هیچ حوزه‌ای، قادر به تهدید شرکای منطقه‌ای یا ایالات متحده نیست. آنها به‌شدت تضعیف شده‌اند.»
کوپر اشاره کرد که نیروهای نیابتی مسلح ایران در ۳۰ ماه پیش از جنگ اخیر، بیش از ۳۵۰ حمله علیه نیروها و دیپلمات‌های آمریکایی انجام داده بودند؛ به‌طور میانگین هر سه روز یک حمله، که در نتیجه آن چهار سرباز آمریکایی کشته شدند.
برد کوپر با دفاع از جنگ اخیر  تأکید کرد: «امروز حماس، حزب‌الله و حوثی‌ها همگی از تأمین تسلیحات و حمایت ایران قطع شده‌اند. این نتیجه از پیش تضمین‌شده نبود.»
او همچنین گفت نیروهای آمریکایی دیگر برای سرنگون کردن پهپادهای ایرانی از مهمات پیشرفته و گران‌قیمت استفاده نمی‌کنند.
ذخایر سامانه‌های دفاعی پرهزینه برای مقابله با پهپادهای ایرانی در طول جنگ خبرساز شده بود، اما فرمانده سنتکام اعلام کرد ارتش آمریکا اکنون از مهمات ارزان‌تر استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyPKgwCPVuTM5F26jmOFjFEs6eDLqLRX409RMPxBX3z94MSWJFKdLyOcPWwSXbKZcMkdSuSNTOokp5WipHPicaaAq8tuvG4pcm75059-5DfaAU0zFi9s_QeDcDdiazEuSkkUorCS046NWoCoFSQHCDtmUpb_y3Rs9IVnhnkYIIy71mhJQ1ui-1CSo4RaV-OAzm1MY4P9CknWM0gg_aT9K7X4kHb_h5F_9MI75zGiwHNsrr9i0UggtwtOA8W9BTNSW2q0IoLCwgZCv7FnMNn-dR1TX_foYymQUBif18pm1hZLh4t6rYQI02wOEVnsuNhq0x8WwTZemwE3dyU_nP2peQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOw-V3lFnB2v54k_fPhoCTjAzOnIM5v5vwK7f4G7ecloNc3LVMk5p25aJb-HuFmHLnGejDhj0DSsvMlZM9BbM9BpVSKiDAijhPVQSRDcJnBIfKQ5mKpKyIT1l2Cy1cV1WWi2OLSKc3rawIM3LWW7RKaRoEtcbTTFGbtVkIOu5iY0dOjunccel34l5sEWCCCOkHqZPiBMNQoap-ANnE6Hc4DfayEhoASxkCyjoUjHxOT7u_gNwtb1DaSaPxHCdzLptPhVFzLEL5erpytwl7WieS39Yjp4e9u17AODEyom5hG8o2GhzsAcPujHIWe9-jUn3hWSjppGg7PhZEMcFyMiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_OxrEvhjBCHXtngeL2W5TJh8X4QQBW8F6Hw3Al0r1d2LjhNqgmSfytOF6XLklQIpNBSXRzUc-8GyBXzdqRYfSJBU6uTaeBnNq2gVrFN8kDMoc6a6Cu4MZ4KW-n5cPYAmD95sL6HOU2cJGeQDCBudPtMtRMEGYLn64RCfCJXN69OgtX6rmtEeR1wQzt5tCwyHpep0IRcHz1Uyx81m8LvMeEJdAl-wp1m6V76m3PQIS7rpGMa5wevUEwpQC9e7Wqrh5umdHrAhLfkidBQNEIhqmlSCAqQiei1vXxEmjpTa6IoY-frTKbAQJMipoD1JU2lTTJPtYsEnJ4XlAuk0Mvx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbdM0t1wj3WuObqJAgrCPyEyH1kTFYmwO_kQLzbuuJ7p7-VVfjWi99xGq8sczbVXXEDRlH6nQq6WiqJbAF2fAhGTp9LPM93VaSSAnlTN9GjX6OuX8yF_ipBrR33H97TfxdHa4VH3fzOKk9qOZb3491yuiv6jA3NTxcZ8CuNpIHFC3jxAt_K5UH9livBHmeARZagfqjj7JvLt8K7lW8GFyiPm1oPlouWiztKwQhmnHZfA5p42PPSEboX27lEbGpZ-7iULrDhOEYefH_vfaRo60sZhJopNo-l2XCqjJN0GEK6uLO8v5pJe1toity6QjUepu1mxPRdgqoiHu5ugGpfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWLcTDZ0_VJM9KhSvGhZuMho6Ayz-foIvSY_VtXFyc_gUvMG94DYZsT0ssZC1EqWpcECxzqUdYdtQcT-knmKaEOYDOoxaDatX-r5zv3Dx8PFz7jRrMO5fwUFfCs9wf7a6P7Q-1lAxt6uCXMqH8NtO1tBIaCi8KoFeo46dYcIL6qZKoedDZDdayiF0B1RVBqEGK7jcViUI18crp2DPCB09XbscuiSgZdiAslcVJeFGzoIihvniCjS_caaE02TnG22E5peQzDOhUDHJbWR20MbsCszEwRBbY0GnpSwqbzAbtVnP1zy9oX2MbR7QlO31ayWoAcEq-KJsKmZs3mCGc1MMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران می‌گویند وزیر خارجه جمهوری اسلامی در نشست بریکس در دهلی‌نو، امارات متحده عربی را به «دخالت مستقیم» در عملیات نظامی علیه کشورش متهم کرد.
این تنش یک روز پس از آن رخ داد که امارات ادعای بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مبنی بر سفر به این کشور حاشیه خلیج فارس در جریان جنگ ایران را رد کرد.
خبرگزاری مهر به نقل از عراقچی نوشت: «من به خاطر حفظ وحدت، در سخنرانی‌ام در بریکس نامی از امارات نبردم. اما حقیقت این است که امارات مستقیماً در تجاوز علیه کشور من دخیل بود. وقتی حملات آغاز شد، آن‌ها حتی آن را محکوم هم نکردند.»
رسانه‌های ایرانی مشخص نکردند که نماینده امارات چه اظهاراتی در این نشست مطرح کرده بود.
بر اساس این گزارش‌ها، عراقچی همچنین گفت که «نه پایگاه‌های آمریکا و نه اتحاد با اسرائیل برای امارات امنیت به همراه نیاورده و این کشور باید در سیاست خود نسبت به ایران تجدیدنظر کند».
عراقچی پیش‌ از این نیز گفته بود: «کسانی که با اسرائیل برای ایجاد تفرقه همکاری می‌کنند، پاسخگو خواهند شد.»
رسانه‌های ایرانی همچنین درباره اینکه آیا شرکت‌کنندگان نشست وزیران خارجه بریکس در هند خواهند توانست بیانیه نهایی مشترکی صادر کنند یا نه، ابراز تردید کرده‌اند؛ زیرا اختلافات میان ایران و امارات ادامه دارد.
در همین رابطه از کاظم غریب‌آبادی، معاون وزیر خارجه ایران، نقل شده که به دلیل حضور امارات در این نشست، «مشکلات و رایزنی‌هایی» وجود داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Cx_L8tDGQw_en8LWg07z_zhG_7LasoULi7sVUU1WnhRp8YqAoeMrqgRaSJ4mHrMgrS6aBde9jonlFBsWT75I3VqQZik-Wu_lsf59T1dAvSbYYh3oXmaO-b8r8r-5Hr7BmdtgUeOuw6665DpGFu5oTxqCWdqqWhkS5HaLn5SUU1cdyZZ60mx_YLWBRjGxdBolOkYTUf8iAGlwgYaHty4ieZ_NNSfIGuKOwQN2r-a7Hs_-b2cgVYGP9Plu59MR0xeeXKp6Vr9P6pNE0QZPRcuL14Rd23laiZ6_uIkHI3oUQAgFovjOujOfpKzUh3nrhE3E_hy_XMszSduoAPsTzo5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-nb9UVw3IoYSPOwpyalvkt2WQQsmFMs981KAds-9xKZPV-pSNAQwWWdzzcfpHHb5yGRHmG2olJ3_NFgROLn2P-R7TNmY9fUN1it0aT-Z5PWmYLJFue42-1U4N9paAIzBcW9prihFEfzjAYBcF5xBqEZWTLdgX-eEeOu8QcwbNJBoEJWFFPUn6ydjUL7k93-SkIi3NgRkGDIlhlirJa29BpGTGS-a6eKLFg23kGCiGUjFIJmiEXObyoyq-jCaeaPWNiFXorNtHzGQwxVn2zYcLCrthPjqbkXlydhJQQvNC-9T09Imvra0HqO6Rhz2vWfTdPU-lGKmO4nGZ10i9HpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا روز پنجشنبه ۲۴ اردیبهشت اعلام کرد پس از وقوع حادثه‌ای دریایی در شمال شرقی امارات متحده عربی، «افراد غیرمجاز» کنترل یک کشتی در لنگرگاه را به دست گرفته‌اند و این کشتی اکنون به سوی آب‌های سرزمینی ایران در حرکت است.
این نهاد گفت گزارشی دربارهٔ حادثه دریایی در ۳۸ مایل دریایی (حدود ۷۰ کیلومتری) شمال شرقی بندر فجیره امارات متحده عربی دریافت کرده و پس از آن، کشتی به تصرف درآمده و مسیر آن به سوی آب‌های سرزمینی ایران تغییر داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/75461" target="_blank">📅 18:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5Pla-MTI5lIUCKr1bNEBmukobHKrAxYFBGih_n1rE6z_D9CFrYTpT1x6bBtOoTIb92akiJeJS_uIPL5mEx47duwRQUJlN7R0zzcH6MeGtjfDFyvTuIK3HW-D1JDhYKl-EqVOBL13Y6WMLVDiMJMX3CHI_URaEuHa4Oqx6mnMfBTmjg6QnFcVu6pB1d_7b7Bm1Rx4HP_ZdxqwIIIg0aNNY7Z16HtwmAX_yFciPyDNVBbV_bRzxje6cazLjdikRi8uh58atL-Iu82yGQb6doSQSwrRBGtwZutD2dgKzzWfpS7imE5ZMNbOSuu6pVtag2cUffqZWzdmaSRG8ZVQl1yEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید اعلام کرد که دونالد ترامپ و شی جین‌پینگ، در پکن توافق کردند که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
آمریکا این گفت‌وگوی دو ساعته را «خوب» توصیف کرده و می‌گوید که دو رهبر در حال تلاش برای تقویت همکاری‌های اقتصادی هستند.
در بیانیه کاخ سفید، رئیس‌جمهور شی همچنین «علاقه‌مندی خود را» برای خرید بیشتر نفت آمریکا ابراز کرد تا وابستگی چین به تنگه هرمز را کاهش دهد.
همچنین گفته شد که مدیران برخی از بزرگ‌ترین شرکت‌های آمریکایی هم در بخشی از این دیدار حضور داشتند.
آن‌ها همچنین درباره اهمیت پایان دادن به ورود مواد اولیه برای ساخت ماده مخدر فنتانیل به آمریکا هم صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75460" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPoyEYzFn1DtzsN0Uvu-ZCujtAtfUbXSYD-j_sq2vceuQUd7_o7KbwVHD5bdEVoWiMsTItDk4RrX1QSrfqVgzNLJI2jQ6TKNHp5Pk2tyIWCN0WymCK3E7WNxiPtycqG8jnyW5nWY5m09hBcjApHnGoIsY_T6wOYHqb1pwCw44VNCKMrvlG_C88DtAari1-buGxesi60mwU2vXxG-PSfEuNq7xD3nxQgDTi3VKYi9xQTrk-f_LZTkT4lrt4M5bucybYUf8cOpTmmlpkFxe7vGV7rMEJ2GHiSmF8q5fKL-RexKfHwSWBvvV7pd4BJ2HLw3bYe3TToD733BC2qOb2QMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید به نفع چین است که حکومت ایران را برای باز کردن تنگه هرمز تحت فشار بگذارد.
براساس گزارشی که فاکس‌نیوز از اظهارات روبیو در راه سفر به چین پخش کرد، او گفت: «ما این استدلال را با چینی‌ها مطرح کرده‌ایم و امیدوارم قانع‌کننده باشد. آن‌ها اواخر این هفته در سازمان ملل فرصت خواهند داشت دربارهٔ این موضوع اقدامی انجام دهند؛ زمانی که قطعنامه‌ای برای محکوم کردن اقدامات ایران در ارتباط با تنگه‌ها مطرح می‌شود.»
روبیو گفت حکومت ایران در حال ایجاد ظرفیتی بوده که بتواند با «انبوهی از موشک‌ها و پهپادها» سامانه‌های دفاعی کشورهای منطقه را از کار بیندازد و هرگونه حملهٔ احتمالی به برنامه هسته‌ای خود را با تهدید به وارد کردن خسارت گسترده به کشورهای خلیج فارس پاسخ دهد.
مارکو روبیو همچنین با اشاره به بحران تنگه هرمز، گفت این وضعیت بیش از هر کشور دیگری به زیان چین است و پکن باید ایران را برای عقب‌نشینی از اقداماتش تحت فشار بگذارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75459" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/miYoAYdjs-QiG1vLvGYOloLwomp1qhNraQWDz3sNHVBEhw_h4tOKg7BgG0DfgDQBP-eLeVO1N7628C2KO3cbORUICdQ9fGxVY-pYTukVREei7eyHxWI7azTuSzmQHXGuyYhfpH6h8HVyKBn5z0Jbm18PTH8SUpG6c998-PDbF1U5UwhqFH7_RAajImoZ7BDLRuNLsb9t-A1WAqQpttXeLtuzNyew2y6LbwY1SkxeDMe6mX-fPCuJtu0NqqHCHLGwwevj2EQJmR-U-7e5wuHYE7-l3K-GUOvOH7RQ9AZcs-_hxwCB4rKhdaubenc5gkIseQM8HPYMebL-ssNJ--ltCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hy1GwHxTe3s5Fy_ROiczqS6Z4W9tTbqE8kTUU0m02HeTDqoq7k7AjhMP0rPo5l-9q2JP1djGlHVs_nUB62tKPMhhWzjSfwB1incIoCjfOH3OCbncKMHQ6GaJFCfhnvww0iHwaUKMv6h5JlmkujppnkGDjSOcYooZHqxb4AQW2rr7q7orfholcqW6CLF0eeMEB_5XxSRoZGeKILiTCXrbqsI5udPKP_dvsYRureanujDCkxAiRlKb25vbt58F1vt66Nh7hX2Hc0MIaVbpKmLQFXamj6HvskxHC2nnbdnRtvAW7wVU7RiB8TUwKdXTou38RSyvnSgh7NmQCVDrpWmHxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد بین‌المللی پایش اینترنت، نوشت که پس از بیش از ۱۸۰۰ ساعت قطعی اینترنت در ایران، نظامی طبقاتی توسط جمهوری اسلامی برای دسترسی ایجاد شده است.
😋
💩
همزمان مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر مسعود پزشکیان، ادعا کرده است که اگر همه‌پرسی برگزار شود، مردم در شرایط جنگی، امنیت را به سهولت دسترسی به اینترنت ترجیح خواهند داد.
@
VahidHeadline
روزنامه اعتماد گزارش داد که نخستین نشست «ستاد ویژه ساماندهی و راهبری فضای مجازی» هفته آینده به ریاست محمدرضا عارف برگزار خواهد شد.
هدف اصلی این ستاد، فراهم کردن زمینه‌های لازم برای رفع محدودیت‌های فضای مجازی است تا حداکثر تا میانه خردادماه، امکان اتصال مجدد شهروندان به اینترنت بین‌المللی فراهم شود.
عارف در این مسیر قصد دارد از ظرفیت نخبگان و اساتید برجسته ارتباطات نظیر هادی خانیکی و علی ربیعی [
🤨
] استفاده کرده و میان نهادهای حاکمیتی برای بازگشت سرویس‌دهی هم‌افزایی ایجاد کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75457" target="_blank">📅 18:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75456">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka4qVaPVnvVXceXTtGCLejFAOCvbTIYvtuoiOF9HADFzcxYbIdzDgS6fVqEerUK67W_xZ5XZGSdetPLXy5Co-DioqBR_90PHscmk3W4GOzcfCJsJR8jUjePM5NmBF2IOZfXczeXyqc2o8rDxsQEmO7GweXXFhRa0PD8mSq8-3kE2w5tp_pPsveNqF70sWty_AMw8leqvLB44eY76301lHsOfiJoPksnfcdPasf2W-Wa6c0zN9NBSZD51C1ulGwUomB6l4_eo9JZcCjrBUjr-wQqkZOjKFj1lAV8IoDWT9OON0B6OPVM4i1HiwpP5i9S0YvFSalkkiuEoxAu_CtBS_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی شفاخواه، فعال حوزه آموزش و حمایت از کودکان کار و ساکنان مناطق محروم، توسط نیروهای وزارت اطلاعات جمهوری اسلامی بازداشت شد.
این فعال حوزه کودکان عصر سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، ماموران وزارت اطلاعات بازداشت و به مکان نامعلومی منتقل شد. همچنین تمامی وسایل الکترونیکی و ارتباطی او و همسرش نیز توقیف شده است.
@
VahidHeadline
هنوز از دلایل بازداشت، اتهامات انتسابی و محل دقیق نگهداری شفاخواه هیچ اطلاع دقیقی در دسترس نیست و پیگیری‌های خانواده او برای کسب اطلاع از وضعیت سلامت او بی‌نتیجه مانده است.
مهدی شفاخواه طی سال‌های اخیر به صورت داوطلبانه در مناطق محروم و حاشیه‌نشین فعالیت داشته و از طریق آموزش ورزش و مهارت‌های اجتماعی به کودکان کار و نوجوانان آسیب‌پذیر، در راستای کاهش آسیب‌های اجتماعی از جمله اعتیاد و بزهکاری تلاش می‌کرد.
او برادر رضا شفاخواه، وکیل دادگستری و فعال حقوق کودکان و زندانیان سیاسی، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75456" target="_blank">📅 18:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=vqGmCUXxohYJk9ETaoo0-y7NuV8wvF8OA17mv9wLp-nfFVVtW-qO_XQh7dKrhQ4PhxhjRmyypEENP_83O--5EyKCpMPQCszRAUnT856mZ8pPysmtD9MiEJYPjm0rNVdilO3r4w10An8blTWB2XHn9GOdiHBGL4oka3rdvkixXkQtsBt6A-2SQcZHFIiNcScfR3btJsF9nNM9kAj2X-0ecWAbMbr2tjNl6m8nDB7XlncsPyseQqJoxWeKXK0umkQJkBiFJ_duHziTjg4WWdsE5VvBxs2i1GvfegDBYHnUyx8zEMmTJFd6YIserx9u1vIpdALITdjNfS8fTaGwZq8JUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=vqGmCUXxohYJk9ETaoo0-y7NuV8wvF8OA17mv9wLp-nfFVVtW-qO_XQh7dKrhQ4PhxhjRmyypEENP_83O--5EyKCpMPQCszRAUnT856mZ8pPysmtD9MiEJYPjm0rNVdilO3r4w10An8blTWB2XHn9GOdiHBGL4oka3rdvkixXkQtsBt6A-2SQcZHFIiNcScfR3btJsF9nNM9kAj2X-0ecWAbMbr2tjNl6m8nDB7XlncsPyseQqJoxWeKXK0umkQJkBiFJ_duHziTjg4WWdsE5VvBxs2i1GvfegDBYHnUyx8zEMmTJFd6YIserx9u1vIpdALITdjNfS8fTaGwZq8JUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر پرچم حزب‌الله را در ویدیوی مربوط به بدرقه فوتبالیست‌ها سانسور کرد.
FattahiFarzad
دیده شدن پرچم حزب‌الله تو اینستاگرام مساوی با پاک شدن ویدئوست و ممکنه حتی اکانتشون هم بن بشه.
Sam1Kia
اعضای تیم فوتبال چهارشنبه‌شب ۲۳ اردیبهشت‌ماه در میدان انقلاب تهران برای حضور در جام جهانی ۲۰۲۶ بدرقه شدند؛ رقابت‌هایی که خرداد و تیر ۱۴۰۵ به میزبانی مشترک آمریکا، مکزیک و کانادا برگزار خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75455" target="_blank">📅 07:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LexdyrBRppK9I2VPeDSWdDTXvmZ99U3vpqYj02-zXrmzygL5lm9YWZogHLaD6twowBFVpZQATwFsCNYFCZHQJJdgoccOMNQKnetykZh6oZWBArtsGhz7AbY79Pn3w0oiRkCX7tHlx9lCJfSbsbofgCbN4tFPVFcHAaYMuwm5MCHai_QoUwcrbthj-TzCvjtdpjAx4Dnu2-SoE_N75-inQRDhZIVKdhspoxg_R7kkGhc2XQjb6uxf8WNrIxb0BmacqPeEuykzelhq6-KGHWpkiEksunuEEHU_Vd0m9YWD1Gn43FtvSSWJda8JufpBQWcoWHEgSj3W-sVxG57yI7G73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B90i4LhMWkV8cIF_o2ehlheJS-lij5T7OWLj15wU_--jrVmmapZM8ryxqyDnckn_JjWOCyC3dqFYOWqkBhidlt2F0R6EpPzX2JhvFL1qIkAcV7bI46ayJR5ozWyhAlLwweZVserJ6vIdNT4Z0nBX1nFLxSZhnv_BhgPYTUBxK2vJO8VCRQPru1lW_ic3RCa5LN-z5Pb70PZVuUfPJf2RNaR4Rn_BsCAdkANticK6qUt5nKxQOZE0bDWTMfT6V--daTMc6hw1j0l_RIrXkf4uxxP1elMPWxhZ0WJDLWOwy8PHaYIiH0YCdqpqfhgqTVhHFJcCnHQfsQ8iDTkDwu12aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KWWB_-GltQCclt2htFPhBwtPmE9unscaUxTAHpTPWVW0UmjfLLc7ZujBWC0X41C4ettba0CvzV2u21WeuWA_76pJTwhJ9gYDfY60PGhKkzCQeBRwpNftxaOklA6857aksMAAwf033y7mWfmGgzzO2au4F_AaR-05StWfDh-lD4qnNlHSH0jzUO04KPkOrEdmxdRHMQZbLYj5MKXyLrSoJUXEJNP2O5H0bSYFPbbznhRrpKB_ZiUthZVCx2E4jhGTiiIppbV_qW-kbsjTtrvjyK03WqgYuvIt9gHx0XwLCk2W2d7E81L1emwNCxB6wN2ez9l8AADHRpsmObrJAIulOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUh67MDH2U2_hytgvsvBKhORtr199Ti726C7TTFS5K109PoCGrsMMy4UbgtjTWvdzxzsdtNfAOUXSm1f3xKEHkwdKkjpgVmaKcRuFkKGmRaKII0yjWk0VGQqO1Et0WCNebH3LwBJe01XbR7nOl9mDNMiuP_v5rmpJcbsUxAt8blxMnX7Rt8pgtjj7e43x1PYmKp_LJkGwJ78A6IIQ9oUM6igsWBOC1uDAyXfIPPdMLdewwsmTcSMF3RquYpUcRfCeCVvkzjog9lb9TiMy2fEXToTOCWY89I9rD_w1085kBDU9H4Ltqd4EA9v3tXp1Wxv47ARBkJvZmEnOql4lBox3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل روز چهارشنبه اعلام کرد که بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با ایران، به‌طور «محرمانه» به امارات متحده عربی سفر کرده بود.
در این بیانیه آمده که نتانیاهو با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
دفتر نخست‌وزیر اسرائیل گفت: «این سفر به یک پیشرفت تاریخی در روابط میان اسرائیل و امارات متحده عربی منجر شد.»
پیش‌تر مقام‌های ارشد آمریکایی تأیید کردند که اسرائیل در جریان جنگ با ایران، یک سامانه پدافندی «گنبد آهنین» به همراه نیروهایی برای بهره‌برداری از آن به امارات اعزام کرده است.
همچنین به گفته مقام‌های عرب و یک منبع آگاه که با روزنامه وال‌استریت جورنال گفت‌وگو کردند، دیوید بارنئا، رئیس موساد، دست‌کم دو بار در طول جنگ با ایران به امارات سفر کرد تا دربارهٔ هماهنگی‌های مربوط به این درگیری رایزنی کند.
@
VahidHeadline
آپدیت:
امارات تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_f3FZo-CzlWDx4PO9pB4XruPNigMwtRCS5aad39qCtzfTSBzSOkLM8W24tSIp17eGyj-xDeXVabB4YRFXmD4pjFTTB1aS1_Pn9lPgDTlqGo7N3pU9AsL8fKzqbtJEPub2mWFKFBzdRf75HdUEzX4D3qJu4r4FE3aTw-2Tvagq3tl14pUfvnUfDLSnuo3AvmF-QoTEq1GUX8ktzbBPQElo3chyMN4Z7Qqb0RXZGtuVJChNPhDL-zcbIo6RSqzBC1pUjAEGbwSUkRFvV_vLXlN8ou7alHQ0O2YdhwfimylwJ7-E2c-T4yCQPaUsuKivirjgZobbqfHgPty8yCCEsH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده روز چهارشنبه ۲۳ اردیبهشت با تاکید بر ادامه محاصره دریایی بنادر ایران اعلام کرد که از زمان آغاز این عملیات، به ۱۵ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده شده است.
سنتکام در پیامی در شبکه ایکس نوشت که نیروهای آمریکایی طی چهار هفته گذشته ۶۷ کشتی تجاری را وادار به تغییر مسیر کرده و چهار شناور را نیز برای اجرای محاصره «از کار انداخته‌اند».
این فرماندهی همچنین اعلام کرد اوایل هفته جاری، دو کشتی تجاری دیگر پس از تماس رادیویی و شلیک تیر هشدار از سوی نیروهای آمریکایی مسیر خود را تغییر داده و از ادامه حرکت به سمت بنادر ایران منصرف شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75449" target="_blank">📅 19:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=MN80RYPFNzYCMV_HFyQRSCKqs96IMU_SNjxp74FfAmAR9qr_p2t1KA13Une2t0j7UH_8OS60d5oZQg501U67xB4EtxJMc3MqLN1i-7HdDNvV_Py1hB_glFcz81E7aLLkll8US5AY5DywEP6Y1_kcT54iqDUzMsYF9xdS7fPikhlaQ30pG6C2EFV2xHSLizBOizFMxfzJVpQajj-sri5GXG-g-HpQJZVqx7E3KDq3U0zHS8fIMN8zUdKrP0QLjJzNzp2jvt_8kaZJNDrQgVxQ8C7Dw3w6imzO5kNaRo-TdIneLeT6ihqsklBbHhVmcNaZGJx2oPUylptW7BLDaI3jIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=MN80RYPFNzYCMV_HFyQRSCKqs96IMU_SNjxp74FfAmAR9qr_p2t1KA13Une2t0j7UH_8OS60d5oZQg501U67xB4EtxJMc3MqLN1i-7HdDNvV_Py1hB_glFcz81E7aLLkll8US5AY5DywEP6Y1_kcT54iqDUzMsYF9xdS7fPikhlaQ30pG6C2EFV2xHSLizBOizFMxfzJVpQajj-sri5GXG-g-HpQJZVqx7E3KDq3U0zHS8fIMN8zUdKrP0QLjJzNzp2jvt_8kaZJNDrQgVxQ8C7Dw3w6imzO5kNaRo-TdIneLeT6ihqsklBbHhVmcNaZGJx2oPUylptW7BLDaI3jIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ‌های ملی‌پوشان فوتبال در صداوسیما درباره میزان تحصیلات دانشگاهی‌شان جنجالی شد.
در این گفتگو، یکی از ملی‌پوشان در پاسخ به سوال مجری که پرسیده بود «در کدام دانشگاه درس می‌خوانی؟» گفت: «نمی‌دانم، الان حضور ذهن ندارم».
در دوره قبلی جام جهانی نیز انتشار ویدیویی از دروازه‌بان تیم ملی فوتبال ایران که گفته بود «من دکترا دارم»، بحث‌برانگیز شده بود؛ دکترایی که بعدها مشخص شد به‌صورت غیرحضوری در رشته تربیت بدنی دانشگاه پیام نور اخذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75448" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlG5V-4xAW74yGelho5y1WtNeJvc0oiXUwoe2zkg5nX0xJyZPBSFn1PZzWq5M6zgT06AyDXRZYc8RO8iAf8HkXEogFf--fUTm5cGxOxCJrFpOdrd1xfri3xqTqdNvEp9xYn4DzcN55jO6Nc7B7tMcCLkSuCNa29zpDxla_o7RZvYES7o2U5DzfC2HZyRjKbCzOUZ1e_nlgxG43iZvx0vCj1VSGozsEq5gk3ocJs0yV6x2SZRF7zy2MfU_0nZboO48Etaoxx4GAC4gc-8WQSEvq_ywIhplfBpHzADhxse7dxmwCcs3ieBmw2Cu6iSG8obd_JieDznX-a7pJBoaSjKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از دو مقام غربی و دو مقام ایرانی گزارش داد عربستان سعودی در جریان جنگ خاورمیانه، در پاسخ به حملاتی که در خاک این کشور انجام شده بود، چندین حمله اعلام‌نشده در ایران انجام داده است.
به گفته دو مقام غربی، این حملات توسط نیروی هوایی عربستان سعودی و در اواخر ماه مارس انجام شده‌اند. یکی از این مقامات گفت این حملات «اقداماتی تلافی‌جویانه در پاسخ به حملاتی بود که عربستان سعودی هدف آن قرار گرفته بود»
رویترز با اشاره به گزارش‌های پیشین درباره حملات امارات متحده عربی به ایران نوشت اقدامات عربستان سعودی و امارات متحده نشان می‌دهد کشورهای عربی خلیج فارس که هدف حملات جمهوری اسلامی قرار گرفته‌اند، به‌تدریج وارد فاز پاسخ‌گویی مستقیم شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75447" target="_blank">📅 18:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7xbRgkvTi7UfglSAgnp51dJcqR8MVriPCijAnYUmrUA6zWqMMakxqk_vQDXK7HOnkeKjURQYs_nnM6ma680IPrm5kqrS3_eu2DJzT1PEaIW3CLDfKBqd74DR4IiZq06e-IaZrw8tQBLkMrB2YGoP4AVxe3tG4ChHAI_AifPLD2OzPGQulT-3d8A5mJ2yH8roMSV3UeQERg-Zgc9pM9Ft6p2dMueYqOcPJGrf71lRg-YGLvUxgoD1Zj5HIhH2tYJT3kiJVF0DDZDNQ0Dw_iCEufCBO4h_7lNUfrgW5K7G2x8mawDge1-7fNSMg2XiwOH1K1uopACzQQddDKoeLOxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کمیسیون مستقل اسرائیلی جزئیات تکان‌دهنده‌ای از خشونت جنسی «سیستماتیک و گسترده» توسط حماس و سایر گروه‌های مسلح فلسطینی در جریان حملات ۷ اکتبر ۲۰۲۳ و علیه گروگان‌ها منتشر کرده است.
گزارش ۳۰۰ صفحه‌ای این کمیسیون نتیجه‌گیری می‌کند که تجاوز و شکنجه جنسی «با هدف به حداکثر رساندن درد و رنج» انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75446" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cFKfzIoj-8liY6ZlmatSN4aJCXR7OmmnUHzgyTW3QqOkjN-iRBGtgxjm7homiGXCsbcyNrtTyEMBQ2Oz26v5dcLsUDW10aAvkXD4vovfrOn2cWVAzzpSo-Zf0ArECl5GrZNn16-CB0o86tTtWQ3waDVzsNPaocW1YJFp9lHGwLjtRd2m19c9F_ht1mhipMq1EHiQ2xAkx7beq7A3pLsDU2FsH5B1WWeDH79M_iLD-xVjOB2WJpNVML1o8YFMn_Tf-ZIFbhQ7Jk2kKnFe05LRVfmZ0q_OR6fW1DYR_TIdGOLsS7eTTOTf_HsiX5mBsYVlkNMqgm5MA5WP7rkON1U5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، محمدرضا عارف، معاون اول خود، را به ریاست «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» منصوب کرد.
در حکم آقای پزشکیان بر «حکمرانی یکپارچه» در فضای مجازی، پایان دادن به «چندصدایی» و جلوگیری از «موازی‌کاری» میان نهادهای مسئول تأکید شده است.
این انتصاب در حالی انجام می‌شود که امروز هفتاد و پنجمین روز اختلال و محدودیت گسترده اینترنت در ایران است.
حکومت ایران از ۹ اسفند (۲۸ فوریه) و همزمان با حملات اسرائیل و آمریکا، دسترسی به اینترنت بین‌الملل را قطع کرد و تماس‌ تلفنی با خارج از ایران هم با اختلال جدی رو‌به‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75445" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E3WbgfiE3LWdF12o1Z8XRTogPTAnd_Lzrj8cViH7KiHVvi8xjGImSlZnTleG8UicmFOh1efe_gpKOkh8TxCbM0FlrL0KKLFknETDwznscrsHDhwGP5V9Ir12pBWn6d27403oMw7E7sKAOwUxor988kcsmoK5Nt0vU1YCggxj0yCkhFYLTg9IzgV_KO7CIgLv-fdo-67BKgVcNuTDtzdt48omY3awhfqaKcu_6AtI5UFaVGlAlKg3jbERT0TVhge5lH8eFFe75zgZiKHTBy3GjTV643jmXGqhDX-BNmtP9ozZHonwD9MpmlLUynievljIHHsm_QUQ4w-e7fFjVXkrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با اشاره به زمین‌لرزه به بزرگی ۷.۱ در قرن نوزدهم در گسل شرق تهران گفت: «وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی دارد. وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل را تخلیه می‌کند، ولی این لرزه‌ها می‌توانند نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر باشند که مقدمه رویداد بزرگتری است.
به عبارت دیگر، لرزه‌های خرد و متوسط، هرچند تا حدی تنش را کاهش می‌دهند، اما نمی‌توانند به طور قطع احتمال وقوع یک زلزله بزرگ را منتفی کنند. در برخی موارد، چنین توالی‌هایی می‌توانند پیش‌لرزه (foreshock) باشند.»
@
VahidOOnLine
امروز پیام‌هایی از پس‌لرزه یا پیش‌لرزه ساعت ۱۲:۳۳ دریافت کرده بودم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75444" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSkFwxLhteeyKGcxie8Mitl5uG0ouo7MVakf1B2-R3DOYBFRSV5csi78LgiayTsEECPbu4lLB2Mvr4t0jn6FQ3sTiLK7N9ySWspMaKEwzI8kKlXRMF3XQf4uoqRTd81GxbDsRBkMCWgcrTpn3ptYfc6E50KCWeRNGkNqpq_luvI_vjEPMR0RV5KNcSloX9nB7Nbs7PmacjllCwqSQv1JsTvUm8t4eeA4MZXKZNzDg6CZKYvGoVYkH4ngt37ASNi96wbkuacWfePbXEE-AonmywSXt6MBpSSsBI-4UGWQ5SH51chTjWH_Un7bGKcEw_k3Vm_OCfmQT6mAAl7RHFqVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان شیرخانی، شهروند ۳۵ ساله اهل شهرستان ملکان در استان آذربایجان شرقی، بامداد روز سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، با شلیک مستقیم نیروهای بسیج در ایست بازرسی شهرستان بناب جان خود را از دست داد.
بر اساس گزارش رسیده به ایران‌وایر، نیروهای مستقر در ایست بازرسی بسیج شهرستان بناب، خودروی این شهروند را به بهانه «عدم توجه به دستور ایست» هدف تیراندازی مستقیم قرار داده‌اند.
یک منبع مطلع در این‌باره به ایران‌وایر گفت که نیروهای بسیج بدون رعایت قانون به‌کارگیری سلاح و بدون شلیک تیر هوایی، مستقیما به سمت اتاق خودرو تیراندازی کرده‌اند. به گفته این منبع، چهار گلوله به احسان شیرخانی اصابت کرده و او در دم جان باخته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75443" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P7VigGtudfEfosOsKk5R0EwI2rRxpgMNzZ3OQAvIri-xTknzA2GeOaNanH57Ex0h0nkWpIFMWsgM8jkMi5WN6ZsR1zpS86kXkW36KeZIPQlwH1tU12TAW4nFQyz86jRwwsgx7gIy508VQ1YsnqN-Hz9X3hi8wRKDd7fmehHCK1JEXAaR5m8j95ZsYklDSedpsjgB35pH2yl7qMqiNKyeE8OGciLfHQJOGfDsnQOvaoUsBt_MrCDwPHhWcM4hGrDcQyug7VS88IY29RNkthlXxgbq271bSp8rmZYQ3Y3WlxCti41ZLohExbeEgvtsKBNbiOiE22OqEcs1OBv-rPzDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tlQ1i3tk4psYKfmZ7XZaoIZuVutr48cl2Y6bESpwMyZ8f8xXmURVCfmyjcceBe6i6aMzD8ya70hJhAh4o8bqK9iGOWe8zSdzvkDkz4bFl6BPaYligtgYO--Soc3tvlEeordwJZR51ISaINiU06CRHQs-26X5cBz8IR3G1Fqz8QzqeoecsaJ_mkwoY6LBaRjp43vQtcSxaXiZiF6LijiGi9cXhngSbeav65NiGyJBBJKDY_eW_-5DhI2f5aGPjPihg2RgqDtNnfdrccX-XxovKeDzROKDbCyYhM8hT1LQeAbBDtNvRUzp2orMy06a7RUlyL586FDLsVppbGvpYqshdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KBgXN2Y_QraMNXjQnBv12bUnxfn2sHVn6DGtO4RfvlRBvWDImaMSQlj3FwVjZ7iIC9L-FQvbKVT2teQQ_tfgAwzO2xRN-YO2ARlvv--YCI--Y0xFHNXT8-C9-nMZEAOfO_SF_ATTquut7VI7P6EnBkV4hp8Xsw_7ZuAzNIbeYHO2bNlcKWatZxTMv9mj1nEZywNfjJuJkuNZdxrmiz69-TqVqlPqtkogj6T0ghZ56YMnQzcbhbWzd0QEmryJSXNqYCStCEcvX0IdP8hQGV6qmexlsiJAmXJYaXaecf9AlzUKbyXFaoRNdI4IlcRh6jMHH5_cp1NZOHb71WWWs9sneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ojUn_6PgGSK99Qe2vT2uG-fxc9q5-TVbL337QmZEXl_rO5QVJlt6Q_TIaU8ajSsMiHUDQ-F1qNSnsHENDa0Q8W99Mk9zqPsa6G3ka2rvCJA2TQLovN0blkmSXovjk7wGVoXrJx2ZTAaPU63nhlYCcE8Lv627mjMM7rgy2iRp1Jgz74CtPd8bDYcyaL1rvp7Qlo9uHO7vv2oejLW9Y5bz8f-hgDC5ITtc97sH-z_4TVw07wVjpX-clSAJ9xFpsxND58-MVvcQvKjwk7UcMtZPNs0gjZ7GLJIj4IQihskKKG0ILWLWCie6NNJ9kp9ohVrsHFzCQSHZG2C3FlDhDgEg2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9t21Cx781KoltaZ6FAhrUpRbfLfPnSkCwT9IsYjdWU6QpSZfCW4b-qaD0xZX7lLfxaGaLcR27012UsA7nuYOlja36QNlGrxO4lQYLKmKoeg-3wX-5g1Nc8X36H7yIEjli_CF4q-A4czyz1sMtQ9M7TBA7WFfv6F9xOehAePfbJqgvfOePx53DiK1_KFtTvaUpt_fUn3_dlDsHhgTVhtrOWHzZeeEd0P24BRNHt9VpBEx27x5ZbwaEcaCJebfl-eUNq3blLH8wSydX2ZxlpLiXqSXR6N7yFIwWrIgUBbzxXY3HpuzmMt-PDl5C_YIgoAd04U3OwgPPIe1mBWTQ9GSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxFc1fKTcVczT3E0nq8Asow6uOZgY9sOxjt8R-NRKnwFS6pKAngSb5_4kfhAmTSeVlCkHM-SuEFWbahB9cRP4vtqsdNyN5nTw2FBLZUGeNHD8LR1baXbzPMFhQ5lgsaHGoKfqvs6HpvFyhmSmzrMZyBeczv0b-N-IuIVrt1t14NBwsdG16T3PNsemksjTykwj8RzSS9ABEPNNJU6Oi4vkv63ckaF2ciMF2ri2wtiTaUCUqx-OwRwaxBR6O5LHc2PWIxkCCYJK8jcQC5tZwXuYF9qmrT_BD6AJ5YAR1xjOqXd_LM5GZVshb7Ay-wRQ_qgzpWYBw4p6iZIDFOXV6griA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SljJAONGT00CYZYP4Pt9XsMGhza_6MzeMiTKTXbFFElS2PMCEzslHH0X4k7TzGlPF_ysS_exyVBsh_6-QX--txB-m6m1pw5dqSfvXQYOUg3UDKYkGj_8mWvUBj1wZLJXbTDEytc4_gREfNQtQscBmLx7JtuP7KLZ6EdmJ8QHs5CLIsEfNKRJ2iAv7wFfTFH1WCWEkHZ4PFWoCH7505Wq-vpKD9jzDk-nZowyEWvOiYHtBsiknyfYPuZOjufLovBnPSR2VKKIwxQq5nWcvK8HNRLVahehlnfDakt21VimQCGbqEHWYaBVxQJXWuoQK1FWIE8uC1GnDc6GnJ2Kbl2LbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=DEQ85UL8XghEn9fOqFPa3AiyTN0jvL68qh3YUdFUUXNx4-iUrG6fc-eow2SbTZwI-ZbcprQjIe0-z6zKm8Z46UBKwAOF34wC41Mr4bblp6D9tze3Df2N8XuL006aMuUSDkhlyx7AETT0MOs-c5VuqmvtoNlBkNxJ912lVb4JLCO2lb1s_Rdi-Ukj7YhF62N0zrEknEBmKIVkKiu4zxBXb2Dty9jqboW7SQnaKOAempse-atWCjE9T6QlsNawoIzEsxrm5ofj3f5lBNgHbnQCNlmTVyXkfaI_lvyV1LmSy_DYuuE0jq-l4xNagaWym16mVI7Tpr2_KDPJsCXB8Sf7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=DEQ85UL8XghEn9fOqFPa3AiyTN0jvL68qh3YUdFUUXNx4-iUrG6fc-eow2SbTZwI-ZbcprQjIe0-z6zKm8Z46UBKwAOF34wC41Mr4bblp6D9tze3Df2N8XuL006aMuUSDkhlyx7AETT0MOs-c5VuqmvtoNlBkNxJ912lVb4JLCO2lb1s_Rdi-Ukj7YhF62N0zrEknEBmKIVkKiu4zxBXb2Dty9jqboW7SQnaKOAempse-atWCjE9T6QlsNawoIzEsxrm5ofj3f5lBNgHbnQCNlmTVyXkfaI_lvyV1LmSy_DYuuE0jq-l4xNagaWym16mVI7Tpr2_KDPJsCXB8Sf7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJIoPVoufqbcaB2hoK-LpUqIM7pVPFigG_dZlAl9aspHOGWf5vm0WYOQg0BRACsm7Wf1nBZu4PAY6NhDm3sIFlCEf_TJodhx6-s02_VnAmtFsy1QKRIctztD63VLYdCvrkLGAtzrw_xg2onApUMfkMLGWhu8SBxINmb8LzUR4t7hE_vc3cpIHZSvKfzW7j3SP4rMccYMJpU40MzOXt8KMTRgUvlBGJ5nXq73OisKtcLF8YPNmq3Ax0Qtsszs7xGnMSHapO_DGcbvW9VH0B0iwcPUGLO5ksfeZg8deq3_htT4_mix8XBSAnVhewV7QtayArV6K4jwKn7Z1YGoB9dfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-oBnZ9MDbPf-3CcF94TqJO2aUagRs6LtqT-T5AFoVs-Et5aqTsegphRXPbzYTR68JBOqfbP9jKVhlZ56piW_8irZ6eoCG1PdC-XG2V788MgU1R_7GHuHjElQK-QTz_wOJUuUOGpPkymwRSer2l2CXJrlW2K9YhOrCb7wU-KJZHDJH2_gslXJslxwLJf0qGH1JLsjyNsJIzMYGcxlQsOfaqlUo22DAB3wsh--KXXHgfjE-lgNs6cG4Key5bMHXZaPpyj7h1fURMqJ1UR-AZQnKBRGcDq7IilJlivbQZympZH8G7BPg6gVn8_SvzuuFOUcTSYWZN5LmXal3ODA_icJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mbU-sy-Npq5YSlPl9Rjjcz4AFJjwpzoojDoZokHEMrsyA98qfjvQy7wPAEus07zU4RmQZI3tvT3kVIdaFWEDMA2PKGj_Ce5IHnqmUELwFoTzwqBL0SoRaXw10hORvzc29zDNlcmaCpm2qCbQIAMYjjbiRy2tB2h_oaXyqlbP1iwLfcVilBZus792zayN4WnfaBID1ynFT3HPwxOyOi6h1SUrX6ZfBu-uyYYJttAVPHhL2juS6kk1QObquoTchcW02xRptGGid3HFqJ8o3j2uKqc1EfZgPfTbAgJMjry1F-SfPaUVGkO_04liCNjXSkblJ1ydKGyO3J_5lAuFKeSubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=sWewAwGWIMOzIm1DhjEosdHeaeyddQp0-5ZgoGzmnHtZVYxaYhKN_GuwItj1oTbHPe9mtk8kaPxs_qk--gVb7A-j-QXvMa7q_9_Z5_ff6PEooVD-El9s_Tbuo3Vj49JVOVcTnNGFjxU7Pcj2Bp5PtRLrA5NbgDYw1yxKC2uaJ2_lig3nwpmbcaz72V9f6MiVMxjHqqG_D2hK8T57G-yhe-CTpRDq_bIua04PIvOfgLD7cA2mYwY76eIvMH_GwhhI_dt-QcqNprS4YYkaD1YfmRWLAYVsbZqdZr2gdzZQk3qpc1kIAzKEp4wTXBkLH90UCYgAmQiFkSvV1XpqnN67QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=sWewAwGWIMOzIm1DhjEosdHeaeyddQp0-5ZgoGzmnHtZVYxaYhKN_GuwItj1oTbHPe9mtk8kaPxs_qk--gVb7A-j-QXvMa7q_9_Z5_ff6PEooVD-El9s_Tbuo3Vj49JVOVcTnNGFjxU7Pcj2Bp5PtRLrA5NbgDYw1yxKC2uaJ2_lig3nwpmbcaz72V9f6MiVMxjHqqG_D2hK8T57G-yhe-CTpRDq_bIua04PIvOfgLD7cA2mYwY76eIvMH_GwhhI_dt-QcqNprS4YYkaD1YfmRWLAYVsbZqdZr2gdzZQk3qpc1kIAzKEp4wTXBkLH90UCYgAmQiFkSvV1XpqnN67QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZNY_cJS_QW2rd1fMlxORqEMk6SLu2pmufZrOY_KfVcupS99SY6r6OhJUT4D11YCV41ELM5qutXtN4Oez8R9UNmtRpHklBEa08LNtdgfEjsGnJZfOgc-BqKLlu7B-KPXDNbX2w_IlMrZ4r3sX8904VeyWnRBtkqvMp6iBb04aFQfMfByDMh-Q5wC0tBP7Nq42X21XDgdY1KIFedPY-nv_fWzxk0EIzoTuoJAtVts0M3PExhkBeVKCO2gK99oFrB0xOwzXoZAMKjFtHAIqTvVRyye1qjvzKoNs3_oE-sJ3erl4K5FIxBQ3c2yd3cl0Z_xIRUmg-cGRIYmNqS5QLGpk8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSQaGJmw9igEi6nh2eX1OJxQQS3v2ewqjaLG0_RaIPniOxNA9ZnyQk987uMsf1R7R0cfhHQVixu5OjabOs4FDkLRTN1f_rif2W7a3QWBmfsPYgd4YlUAYyGKuif8JcyKJMPCwWbhYmsJ9vEZ_akvN6YfhbJMRFyxwH5rz1KWHEi-R99ZrJTYs0SVtvqxY7lH2DSvdzSpH4pyHDb6Hn4jGNS50HsOGRgflPAFlsPmAWuLApeUcSFy41ok9Krlofea_REClMvPlj8GUnZz9IP-WsT_C2r68SRR1EIQXHG2Ndh41h63NsOBMfflmN7H20cQMXjNnwAF02XVOfo-3wts9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOk8Zkf5BpAXCamE2qXjRnfVVRv7Bj-VhhxM5OP41DbcrjTpVblsGq_L_UUS9SO5W-FRDp6Jdl_w1984lNGqry2OuQCR3IIhidOJ3IUk9GcWSnZQ03fOAMIcFyNAf6tVYRAfjfoQmCGTfEtUOYWPLn_pQ1TsyM2EClyRKIghsy2OvBlYtEOAmbO7daK5C0tLqpWbro8_SfFGUu01oVJsFevsIKS1e4OhhC6p09HwoA4nywX1mfkhcm0pHHZUNQ4bDjXkt_ccDAYbZDATXBnw_Q93QQaR0GpJwUOFOFwIUEZvvjiJGVnL_J5GwdF-u7wjUlmSA4iuqq2Lwedun4z4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHSegrB9AtcJoLLhOarX-7FlQKqL4pC_Rag797exHPPHkdYoYojoxiG-Ai-uytckFaxPWTofTVrpyrwUw_kPeuQH4hW6qlSuLGDAO9B_Fme0jtXKgAhWudMGM9VRsTRNxzxWCM-mWEd1P1N5M4eoGDEe2h5A-vBeLcO16pw-ENeDreDQJeOadSg5FjY88IiPEy2ypkI_hLO6ipfU6fUetQmNxCWvZ4ADd-WYkZAAlzfjrVdn5_DIwaDDHe7GL5m778dNwB995spxFUfDkS8TKp2IwnySgB5W4--GjJ7nZahn9NVJVABmeUH5HDlJdU7B3iiqcdzd88Qi_g0-SXcukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM26y7M-AMs2PZnSw9lpd0VqCdepzfo-iNkh_x4jTPjh2LG2oWGFk4KcossmMDybauvWpjj6rOEy2gFBzRAeHAWFSIIjJaHzBh0p_3eyocyle586NKFV07iOGjkHAlbb7nKvdyVWfpl9U_cGBnj0iL7StvSPJysBKa52PBQwxaz0wC-B0uvMED080PPMLVXGMtzH9mKpiwGlZB6P3qQ3fLITsXQFQ_4LPTKEQ3TiEtc7zi2irOYme0jrv6soAjVddq6xErVu0uvFOpDMwJZDgT6ZpKprPQmQoTokppwRrZJM0VwEpATnuOlukNb2MRnKXUkQ8t3XBYML7vh4XTy1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/paD3NpYkQkhL-hybDSYp3qEGCzouH80ZpvJBc83I9VCioVTMZM1j1pomf5XFyydJtaTG_DDncpjNUKkuwTazs26Vl29UN80aT9-KCdYL5xu-QShdTC5em5mFIy3Y6k6-bhiI4kLe2KMYKn-bBgu4fVGgj1YnSxyj_0rokj5nFNqDZAhjTJuQXosGtMd_oZJRLW0w88GpRRrAfRRjRQ0EGpCUa-VEhijkSenwdjEYJozEqZ9rt2owB5lGTcgF77uuhDPkfXzo2tWzXMp7WTAsL4X2sZ2xOWgqILzwL4Ah4l1Gn1p1-IwcPXJ4zMHvLD-X3A5ErgzEVSVgngk7ljVFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GnxLiqjKd4kvEzcZgGi545qpyDMw65ok9ZApylgL7OPSdyfoMmVAI6WglPBwQ20DklzQAlsqlA-h-HgkhYChWNBwcjx3vQmbW9twT9S31g_1LCSQ5TZ-6CpVCFFwfHFMir7Rajh4z3OnHW9e7HVltIB61yLwHnc7ghcIuJQ9VelybAHUAkoEmlffzVcq87s0lCrjVW1WDRUaPmUIZy8FXgdUrO3mzRmlL_btFIHPMnZLEQFg8ttz7T5uYM8Sjl8n4tZWS1POacor4-G-0yt3KtlCzyG62Cc0ifZ2STYRWMEzdiVnC-AAxP6pPN6aC4fwuIvNENya9mmYUoyThqdidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RIfddBxCHDe9rdzoFlUwoeJg7WySn9cusroKuUH5fgHaeZEgv2nqt0XhWyB3PfU3_0TbMPlavF1NAFzvArgPKOwDoKgbrcqf0XPTN036xQ2MMwHa8PVhQlAYwqRmNFp6W2HK4T6q1Z3i8lCxLrsTDH_oNeAQ_IJDS9hyr_vEZzmJDcFUSlJyTD5_Cp09pEKoRkGwm2DPq9Y_U92XjtN6wtmOZemI_vVu4Y4WZHkIqFKi1xQAacamhlsssc46Rf0OSN7UADW9IeRiDe5KZghxepH3-W4VMZlDDEvzUfZe_KUuiwEd6VR5tckcjnC2fs6w1poW7fblznvvXqCYM7SQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GRVcePJIEnaYr93p2aiPpQ1GwBw_NLP9m25Pge0YK4J-lORf1JLyjv3mh8RNuABXrnXAblQUviRE53c5MrpPNjWp9Jl-egOtjZZFGAn0ovPYYqiWS8C4T1JVzM26R2JoqXdQie6lfMu6NE5LDQ2c5IrmUEEkdFhBsfhcU1efNzVU2ix0HtxIncITIgHuxWqJQbdWBf_5suH4Ba2NcL5Jp305Pn3ibXSdVoKjN4STfJJ-BeVXmOVH5tSBNj1oQN_iyV_7WRXyrLZYV6cbrnu61yC-oDPiC-4ebYDfYo-pdwtJYnhG_p2ter_m6XvTvgRrPSh2HfjYz64ENIGLQRh0PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IGaQnGQ-mx6bVsmKGr7qdnEnsf_xKKZqjQUbgcazaGy4uwYHNk-rvOcg4jqRh8q98PeIpC520U-FAzRnn1zcn7f-VF1qj5gjFEFfnJGKEL3C21LFR2dRFWtyk5Rij7FZjd5AHrzagXOav7Ats2ext9LGg3PGw0yNEX6ds2Kpgdr-GDzJVdcHTig2jBbbfLOJjMIc_0zCh7bIl7Jprh_j1MXFsuH9SPua3tMv54kZ0jqOfZ2lfRLZWLMGmnNzpf1axnshvgyNKiGTpQSkE4EE40b5lippslnzGp9XIaFRzPCU5H_EcG2fE7g61p1pLOrSXkR7zYs3ykW5nhuFg0Ylpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jSoWJpQE5SOMa9RACf6PyfUMVOm1ms0eb43AT4OzgHojTtYVjReEoopmu3CAw7JeFdEJ7gkAPRvOYlZ3MZPMXG-CEqN0lSbEGOsyE4_-ljPaBm41B8hMlXegR6eGZdqeScdAhTYmCOTMGarJiSPg4zabxCVCFnBto5Q8Mv5tF53-jGCk8FiluY0vNPnj8yEDMG5-C0pBgCmDFtVP6j-hXIYyjOlUALhmBU3kBiOEymX-QP3w0LA3Gk2GFSJQBgKRqo47DRHuqNkrr0aKNSlUA0OWT4aEnxu17u7LDmUs8-zp1Iii6HCmdYJX3sarQGEtUAAU79SDjCmdQWSJihWGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FsSeqQhwoOAIQXvsJXFEgFM4vG0wLJT9-2XFl402r_iiLS7hVdayzqHtGSlrBz1xsGd1Bwc7hOfculIAUBJcvN3d-Z2FAihqTgG6lNVeMu7Q1izI4ztJIIm-WZPCmlOEXksxS8iOJdalqURD4H00tpTZkAHUfcblFlWQ18Itv_7KreZhQytLI48JFYKK7PnIbmx5zD19DpinEKV9-_XWak-U6KQrjPn409MEcnWfd9bk5fpUwhslTZ9jKjw4IIGVYGS6JjVgoeFyHmm2DhL3T02WR4lLouzzURqnMQp6Z57ps18Mo2joOKTvcTLBsIlH27GaBIwpktswaGNdJm1vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ozTyjgFaztVXcybBIEDWLZcFhoMUPZnGrxHiWj5W5FKQwrsYzkb9ll5LFW-y1Vpa1ReS6iIP4unRjTjFQ-RP8VQJPpICA4g_e4uIbCHFyD4tddWCEknDTfy-jrbF0Z8h-iGDv5fj1mlLxgBMVta2C3dI2WF_FGAHsDHCjcpjvg-uNAPrNsOEeZTVtQDBe24XfjOvlKjnTjyrsuDeauq_W4reGy5iNpk7JXIeC0lyGCkcb7c81AjhhiuaI2IWp7rsZy-0FGrsD20CF491xND3PL09dzhM-_QMronwKSumeje9-dQbmppU2huSQ_CV9BjDkH7OL3dAApRdI46CLEgImg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=HhBvWMxAtNjjRqfBHJ2i8mtsOWERORJhwuSJ4_w4byu-DlhFEKEgcKqwdzYVatc8ssYzLSUdTH7RX972cOOQA7NH8WMQC0eS-74ojGUwD70CYR_A9tUYmpyop1zd8w36cZTzhq3319w_3mKjh80cGdY6SmxhsLr04gTGqZpF8N6OtDyHlejMIMZznzZwMLQG1uY1Ahdb8d3gExhpg8IJt1coCfKeKJMTg-tcG0RQbqr9lgTyAxaz9b-5zIPKQFnUQPrhqOvI4X6JJzJAG-hkr88lyTM1CUyVRnZxMfDa-bcTGdKhyNJe_g0HzHCmtKjIxpDtKoxBcaWUSdn5moaiQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a88e38f89c.mp4?token=HhBvWMxAtNjjRqfBHJ2i8mtsOWERORJhwuSJ4_w4byu-DlhFEKEgcKqwdzYVatc8ssYzLSUdTH7RX972cOOQA7NH8WMQC0eS-74ojGUwD70CYR_A9tUYmpyop1zd8w36cZTzhq3319w_3mKjh80cGdY6SmxhsLr04gTGqZpF8N6OtDyHlejMIMZznzZwMLQG1uY1Ahdb8d3gExhpg8IJt1coCfKeKJMTg-tcG0RQbqr9lgTyAxaz9b-5zIPKQFnUQPrhqOvI4X6JJzJAG-hkr88lyTM1CUyVRnZxMfDa-bcTGdKhyNJe_g0HzHCmtKjIxpDtKoxBcaWUSdn5moaiQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت گفت پاسخ تهران به طرح پیشنهادی صلح آمریکا احمقانه بوده است و او از ادامه جنگ و فشار بر ایران خسته نمی‌شود.
ترامپ در یک برنامه عمومی در کاخ سفید و در پاسخ به پرسش‌های خبرنگاران درباره طولانی شدن مسدودیت تنگه هرمز گفت: «احمق‌ها نمی‌خواستند قبول کنند. فکر می‌کردند من خسته می‌شوم یا حوصله‌ام سر می‌رود یا تحت فشار قرار می‌گیرم اما هیچ فشاری وجود ندارد.  ما به یک پیروزی کامل خواهیم رسید.»
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز دوشنبه ۲۱ اردیبهشت، در پاسخ به پرسش خبرنگاران درباره آنچه او تغییر رژیم در ایران خوانده بود گفت: «در ایران میانه‌رو و دیوانه‌ها را دارید. دیوانه‌ها می‌خواهند تا آخر بجنگند.»
رئیس جمهوری آمریکا گفت جنگ خیلی کوتاهی در پیش خواهد بود. ترامپ تاکید کرد که میانه‌روها در جمهوری اسلامی از دیوانه‌ها می‌ترسند.
دونالد ترامپ از پایان هفته سوم جنگ می‌گوید با توجه به کشته شدن دو صف اول رهبران جمهوری اسلامی، تغییر رژیم در ایران پیشاپیش روی داده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد که در حال بررسی دوباره «پروژه آزادی» در تنگه هرمز است، اما هنوز تصمیم نهایی درباره اجرای آن نگرفته است. او گفت هدایت کشتی‌ها توسط آمریکا در تنگه هرمز تنها بخش کوچکی از یک عملیات نظامی بزرگ‌تر خواهد بود.
ترامپ همچنین درباره مذاکرات با جمهوری اسلامی گفت: «حکومت تسلیم خواهد شد.»
او روز یکشنبه نیز اعلام کرده بود از پاسخ تهران به پیشنهاد آمریکا رضایت ندارد و آن را «کاملا غیرقابل قبول» توصیف کرده بود. همزمان صداوسیمای جمهوری اسلامی اعلام کرد پیشنهاد آمریکا رد شده، زیرا به گفته این رسانه، به معنی «تسلیم کامل رژیم ایران» بوده است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، به فاکس‌نیوز گفت واشینگتن در حال بررسی ازسرگیری عملیاتی برای بازگشایی تنگه هرمز است.
او افزود واشینگتن فشار بر جمهوری اسلامی را تا زمان دستیابی به توافق ادامه خواهد داد.
ترامپ همچنین گفت هنوز تصمیم نهایی درباره ازسرگیری «پروژه آزادی» را نگرفته است.
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در گفتگو با سی‌بی‌اس نیوز درباره پاسخ اخیر تهران به پیشنهاد صلح آمریکا گفت جمهوری اسلامی در برنامه هسته‌ای خود امتیازاتی داده، اما این امتیازها «کافی نبوده» و پیشنهاد تهران همچنان «بسیار ضعیف و غیرقابل قبول» است.
@
VahidOOnLine
دونالد ترامپ در واکنش به اظهارات بنیامین نتانیاهو که گفته بود «هیچ‌کس پیش‌بینی کامل و دقیقی» درباره تنگه هرمز نداشت، گفت: «من داشتم. من می‌دانستم آن‌ها تنگه هرمز را بسته‌اند. این تنها سلاحی است که دارند.»
ترامپ افزود آمریکا می‌توانست در چارچوب «پروژه آزادی» این گذرگاه را باز کند و گفت این عملیات می‌تواند از سر گرفته شود و در آن صورت «بسیار شدیدتر» خواهد بود.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده یک روز پس از مخالفت با پاسخ پیشنهادی جمهوری اسلامی به طرح آمریکا برای پایان جنگ، به فاکس نیوز گفت که ایران فنآوری لازم برای بیرون کشیدن ذخایر اورانیوم غنی‌شده مدفون زیر خاک را ندارد.
ترامپ در این گفتگو تاکید کرد که اورانیوم غنی شده ایران آنچنان در اعماق خاک تاسیسات هسته‌ای دفن شده که آمریکا باید آن را خارج کند.
براساس آخرین گزارش‌های آژانس بین‌المللی انرژی اتمی، ایران دست‌کم ۴۶۰ کیلوگرم اورانیوم با غنای ۶۰ درصد دارد که گمان می‌رود در تاسیسات هسته‌ای اصفهان مدفون شده‌اند. این تاسیسات در جنگ ۱۲ روزه و جنگ اخیر اسرائیل و آمریکا بارها بمباران شدند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری ایالات متحده در اظهاراتی گفت: «مردم در [ایران] می‌خواهند به خیابان‌ها بروند. آن‌ها هیچ سلاحی ندارند، هیچ تفنگی ندارند.»
او ادامه داد: «فکر می‌کردیم کردها قرار است سلاح بدهند، اما آن‌ها ما را ناامید کردند. کردها فقط می‌گیرند، می‌گیرند، می‌گیرند. در کنگره هم درباره آن‌ها شهرت خوبی دارند و می‌گویند خیلی سخت می‌جنگند، اما نه، وقتی می‌جنگند که پول بگیرند.»
ترامپ گفت: «من از کردها خیلی ناامید شدم، اما ما برخی سلاح‌ها را با مهمات فرستادیم که قرار بود تحویل داده شود، اما آن‌ها آن را نگه داشتند. من گفتم آن‌ها آن را نگه می‌دارند، اما چه می‌دانم؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75408" target="_blank">📅 20:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/knwQf-_vJysOd7ZJ4bGzd58YaGBaqUDRzMveeEMU5cmAyDGFKihaaoDlvo-LXCChNlwDdBlutc-dAcD_G43MBLkAJAi7E3MCKayJR5MfDdaKX5CPSpcwrC98AG3OBnYQsrsXmp4aiTcQatLShWnvVxzMtLvqGrZS_kDv2R2fSelMWzu02F1Khri_kmWOYf61m9pGbHTBqiXiJiBqQAg2lPfh-HKOzFFAU4YZ0VIglt-bnawfbxUFhnAXJbb_PDZAhsONMfC4DL4dcRz9b3Uhe3moKBduAcEHW1o8soH8mPrU2Yx2O08rRrMDoyrGIvFQghV-8HxqLOpx73Zeo4D4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BDUzdA0tEbmYJP1KYzXOzG9DQrHVH541GwRRFwfKDNyRv0T6CvnLpV9QRKVOwzwDIppc_bxmtjc2-ys-A_RWxOD1uNSVC9ndZpOJvrR3iMM_Wl1pbwWx3vzChUbqal-tH8CZv83jZC61nCrsVwT8aFSPX-mQG7bkUPtfl9joaXtj_8eIkQnR9pp_JwePu2MVoeWoZxGcJiwCNJJ1JVIIDlQssnZ1munEZf80MOWZ8ySKaLJkNG5Q8q0KUUtz_yN73dCUVBLADTyGZtZ9rNh_B6VV8oUY4uIKQWPJ8pIBRafOnazFMDnm6tUrFwZ_OU-3DV2WJCPHaLItUEOpcLGTNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">AmirKh1982
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/75406" target="_blank">📅 18:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قطع اینترنت نه تنها ربطی به تأمین امنیت زیرساخت‌ها ندارد، که «اقدام علیه امنیت ملی» است.
در ۷۲ روز گذشته میلیون‌ها گوشی، کامپیوتر و سرور ایرانی از صدها پچ امنیتی حیاتی محروم ماندند و در معرض انواع نفوذ و هک قرار گرفته‌اند.
در این
#رشتو
بخشی از این آپدیتها را مرور می‌کنم: @
hamedbd_channel
hamedbd
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75405" target="_blank">📅 18:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_QYYpbCVtHPe8XzjrgV3gKInZYJ641e_eqU2nysEgz25JXdedxdO6qkKjvoodvaHqqv76wp9UVYHw8RDRJbhBqklNsoDwCHn9fj8rFxaf1sHHwZjj77q9e7HKNnu7GoosjDK5nv6meTd27oBZDLncykDojhBY58R_u5gKArQG1fFom9k9VhrGnv_knTQ316M2mxtdu9iEQf969X0p6bXV8w56B6aslo_g5G24VcOjHFuNMx164ypP3T5fIGw8nJ0sq6Y-GhktgR0Eoxs1iTd6kR-nBLpRjPxz85g2EN50c1yJ07RlvUmceS--FXq3iTSPcSc7U4PCnBLW4YkQvBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار روز دوشنبه ۲۱ اردیبهشت‌ماه در بازار آزاد تهران به ۱۸۲ هزار تومان افزایش یافت.
این جهش قیمت کم‌تر از یک روز پس از مخالفت شدید دونالد ترامپ، رئیس جمهوری آمریکا با پاسخ جمهوری اسلامی به طرح پیشنهادی آمریکا برای پایان جنگ روی می‌دهد.
علاوه بر پاسخ منفی ترامپ، بنیامین نتانیاهو هم اعلام کرد که کار اسرائیل با ایران هنوز تمام نشده و ذخایر اورانیوم باید از خاک ایران خارج شود. این اظهار نظرها احتمال برخورد نظامی دوباره را تشدید کرده است.
قیمت هر سکه طلا هم روز دوشنبه در بازار آزاد تهران به ۲۰۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/75404" target="_blank">📅 18:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dJMEAAQiYehPif_aacooVxn9aRS9j2SfbtLnzOPYTzMvkxaJtoGz9icITP1t-KET8Kb_L_HLN8aXKIfsPWXXeDaX2vhZFFAKsF4n4wKaZccpmSfD8fzpCVL0YEy8AHNTajYPrIkzqQvKyc6bzjXrlS7tBoAm5YD0lNIvVpua71q3lTbhjMBpCxeR6NEreS8U9kzdn6VxqYzBBFK2pfkzcqbi8OzF-UqB-HF6W6Ck4_KL48rOy6SuEMjkxvNYAVc0pKyE5Mm7RX3pGgC_9GtzQsTK5kSjtVJbU7nXpSa_6W1nkcwAAZSE19TIbs-20N82i6B1AG2OaEQGCX9WBijXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uByeQ0l-oSeH-9nRZTexDb7ot_u8pNpYdBeXRco-0w3WGlFUFsuobVB_EJNfCIpzRjTOgeok-n6nUb-QURKdaqzU8r5AvqqFxymqotmOj5H06a7KleeFOKeS6rGMgjJPaceX1kZmr7LjjyVE_WZ3Bs8QyOit4yYCSUIBgH_xw27IXzPES50P_FzuGXyI72Emu0sb1XU7oJ62RtMOE6Pj51untDIkZaUfp47BCKCTyv10Kdue9oYxYA4Ax9I2zUNRozjnJyfykQil3GBdUeTQEsNCI7ZIpn3bk8Vnia37vIerwa4W1UTHO7NJ0moCytDO0iFkKm3j5BrXUhV8_P5LvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😋
💩
«محسن محمدی عراقی» معروف به «محسن اراکی»، عضو مجلس خبرگان رهبری، انتخاب «سید مجتبی خامنه‌ای» به عنوان رهبر سوم جمهوری اسلامی را «کاری الهی» توصیف کرد و مدعی شد در روند این انتخاب «دست هدایت امام زمان» را دیده است.
@
VahidHeadline
«ابوالفضل ظهره‌وند»، عضو کمیسیون امنیت ملی مجلس جمهوری اسلامی، مدعی شد حکومت ایران به ظرفیت‌ها و سلاح‌هایی دست پیدا کرده که «بمب اتم» در مقایسه با آن‌ها «ترقه» محسوب می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/75402" target="_blank">📅 18:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bbhYoo-7DdXDtx1aD81zhUCNxIFaAkG90hGtO1pNCNXRhIWgxhRlq38_Sc0gijhfRSaS_MrVGcxgq4Rhwbz7SJBefxe67vRb5v6eynsFA-3z6_d-YnUn6qyrChdueh2AyOKIjGJWKrYkNvdTtRbnyZrQapahuIwnZl6lZ2e_OQSRTLiJc0A-V1CHAbNIJYzTwjoKTM1HdqyHYXhRb1bV-o96_D3Gjno1LMnqdBCP0I-S3AvnJ5oqpGVH4gCtnt-8pJyNosCIhO8VRB0dJ5eibRvyJ-MJMf72W4nhsEzzP3Zfn_qRV0ksQXaYd4BsVnhEUWEpHMzcsZsfPzsV6o0RUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TA49VYydy4K51M9RgIITJ3Kkt18o1IuebrpoUAPyHFtgsbcawMCRSHoLmmKe1PA2zKLfEUOPODKzaxFH2T4LwBE69TEkw12xUiej0us81EKNuFb0wbHouhhQI5e-GSS5A0UC06sdJWu2GAtsIpIWp7YOPGvybzt7rQxvsV41GHcVZFGnVbT45ijfXyAzAs3KrS8wRWQJ9FJyBvEdOV_5I72D9bWX3-80bbV13tpq4PsZBBFiHi5Rzka5y75H05esZIynrkobFRueldbd30Zq0BOrFcq9aCpX-pC8ndnRGPvt1LoBa82srGk56u6gfpW2ndgVwV9gn3Zg8EUEy2pClA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر بریتانیا تاکید کرد که از جنگ ایران حمایت نمی‌کند و افزود که شهروندان این کشور نگران افزایش قیمت بنزین و تاثیرات اقتصادی آن هستند.
کی‌یر استارمر تاکید کرد کشورهای دیگر می خواستند بریتانیا را جنگ ایران بکشانند اما او هرگز این کار را نخواهد کرد.
@
VahidOOnLine
دولت بریتانیا روز دوشنبه، ۲۱ اردیبهشت، ۱۲ فرد حقیقی و حقوقی مرتبط با حکومت ایران را تحریم کرد.
به گزارش خبرگزاری رویترز، این افراد به «مشارکت در اعمال خصمانه» علیه بریتانیا و چند کشور دیگر متهم شده‌اند.
در بیانیه رسمی دولت بریتانیا، از جمله این اعمال خصمانه به «طراحی حمله و ارائه خدمات مالی به گروه‌هایی که در پی بی‌ثبات کردن بریتانیا و دیگر کشورها هستند» اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75400" target="_blank">📅 18:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POcKXM11GWa8b7KD5OzyNDfVv4I0MHxCLa898Uy4WXyje9w_kYdUDxSBDg5SreJu9DfgIYEx-g1W6C4YGkeqmpPuhjGEuRcDuXLVTOhohEl7j5M0B2Mga6BS1rHes9ek-_v-HUVRew0HrI6dM_WWeXSWNclWOaahMZFtT6hawnUfsSdPJDRL4vm75FDcZFBS8qvjXw5Knf-jpDX6E4zExjCwkXluCoKW2MBv4pZeQUNZX3mv2weShqX4maB09a4Mvc7wSVvnRgQaE3D-9jiGEXxszXdOnrf9gsPgV0_lLpbzSq0hi583FmldV9uKIzMDrmLcmlTlLwZHby0OdhJMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی جعفری، فرمانده قرارگاه «بقیه‌الله» سپاه پاسداران، گفت: «تا زمانی که جنگ در همه جبهه‌ها پایان نیابد، تحریم‌ها برداشته نشود، پول‌های بلوکه‌شده آزاد نشود، خسارت‌های ناشی از جنگ جبران نشود و حق حاکمیت جمهوری اسلامی بر تنگه هرمز به رسمیت شناخته نشود، هیچ مذاکره دیگری در کار نیست.»
او افزود که با این سطح از بی‌اعتمادی به آمریکا، طبیعی است تیم مذاکره‌کننده با هدایت کلیت نظام، شروطی را مشخص کند که همه حقوق مسلم جمهوری اسلامی را تامین کند و این شروط «حداقل انتظارات» ما است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/VahidOnline/75399" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SVkH_8jiSFkpLj9AoX-Wk4MYdFrXikzDQBEL7JLOFALd_TwT4L6ib2e4zAog-EudWD66pNR8tKHwpyduGRLPlGJPT9bd07WpWYQkolGbEwFEd7R7PKuotSinHYtQK2Auy9nT_mAwEldjX-48HKmDYAsARZmFkuzc9d0eTxbWwJFAogAXpuBEVw_UkfkwUPTLo_pimOw69qP0SQ5rzDjH8tILYAG-feyYw8MGC_zlRqORjVsnaSWpNcmcTJf4OAAznjPrxDRzMrqf6ziFU2Wj2lDMSMKFrYSCu_Y5eGojknLz38BgXtMe__WT9ge_EdqiZsB7Lb3Akn6w4SeBmDLU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RA7U-YFwRi_AibD3ThJBZo5PPU8H4qFLKhq3voFwpgDaDjgcnAMlnBuYuBXeNllWwmQ5ZrUQd8H9AOlL2emYwBQPCLMh_Y3fMAgInm9RAxl0mYuh--9hOBWT5eoEt0cso1mY4G2bFFaInWYOzOUY2rVjyUXpH1Ia5lFZhMvf66vr3GeEkXu9mPDF4eXAT8HQ-sETHPdyXi1RFG-dPyZcdQA5rOIaz2aS64sVBMj6qh5Bj4AQYse2f5qbAN5KJ4AcrZq7VIffGKLXFAneYKUO4S0SnS98JHzWxsq7MBxKQNUyG6yZ_dNltzn48u3cSPC_zJVs0Fm8_GzgLVpbKasG9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=vAHy-k-jCZVvn1Ux5ge0dWyAlydflYOIhPoDTK3GazUjcdi6EkStRsntz4agmpUe0LGxQ57n58Qgl5UiBTPLCryrSlZLNxQrzGUDH8DL6IdKCqTXSJiIYFvFJneDNwhxJwkjrI1_QvSdWRcMm5AiBqlO86XsM_RH9ej9dfztVC4ZwYY4c9dEdvqeu7ldQIjA9POPMgwEIOGil78gpwbJjIjkWW0ZzYPuUJ8uvokfio9xwR-GX3tnhC4IT1gC9uryC1zIrne9uvk9sUvbjQvl6j8HuffoGs97yeNXepcjDtVKYBSJg0t4T3_gtOXiXOC4UJxX0SZofbSb0fkc6N0Ong" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8603029cf.mp4?token=vAHy-k-jCZVvn1Ux5ge0dWyAlydflYOIhPoDTK3GazUjcdi6EkStRsntz4agmpUe0LGxQ57n58Qgl5UiBTPLCryrSlZLNxQrzGUDH8DL6IdKCqTXSJiIYFvFJneDNwhxJwkjrI1_QvSdWRcMm5AiBqlO86XsM_RH9ej9dfztVC4ZwYY4c9dEdvqeu7ldQIjA9POPMgwEIOGil78gpwbJjIjkWW0ZzYPuUJ8uvokfio9xwR-GX3tnhC4IT1gC9uryC1zIrne9uvk9sUvbjQvl6j8HuffoGs97yeNXepcjDtVKYBSJg0t4T3_gtOXiXOC4UJxX0SZofbSb0fkc6N0Ong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نشست خبری روز دوشنبه ۲۱اردیبهشت۱۴۰۵ گفت در شرایط کنونی اولویت تهران «پایان جنگ» است و نه تصمیم‌گیری درباره آینده برنامه هسته‌ای یا ذخایر اورانیوم ایران.
او در بخشی از صحبت‌هایش بدون نام بردن از دولت یا فرد خاصی نیز گفت: «هنوز با کسانی که علیه ما تجاوز مرتکب شدند تسویه حساب نکرده‌ایم.»
بقایی در واکنش به اظهارات «ولادیمیر پوتین» درباره آمادگی روسیه برای انتقال ذخایر اورانیوم ایران گفت: «در مرحله کنونی تمرکز ما بر پایان جنگ است. این که بعدا در مورد موضوع هسته‌ای، مواد غنی شده ایران و مباحث مرتبط با غنی‌سازی چه تصمیمی گرفته شود و چه گزینه‌هایی را مد نظر قرار دهیم، موضوعاتی هستند که وقتی زمانش برسد حتما در موردش صحبت خواهیم کرد.»
او همچنین درباره روابط تهران و پکن گفت جمهوری اسلامی با چین «ارتباط مستمر» دارد و گفت: «چینی‌ها به خوبی از مواضع ما آگاه هستند.» بقایی مدعی شد چین نیز مانند جمهوری اسلامی، اقدامات آمریکا را بخشی از روند «تشدید یک‌جانبه‌گرایی» می‌داند.
سخنگوی وزارت خارجه جمهوری اسلامی در بخش دیگری از سخنانش، آمریکا را «بزرگترین تهدید کننده صلح و امنیت بین‌المللی» توصیف کرد و گفت: «جمهوری اسلامی ایران ثابت کرده قدرت مسوولیت‌پذیری در منطقه است. ما قلدر نیستیم، بلکه قلدر ستیز هستیم.»
اسماعیل بقایی با اشاره به حملات آمریکا و اسراییل علیه جمهوری اسلامی گفت: «حمله به یک کشور، از بین بردن زیرساخت‌های آن، ترور رهبر و شهروندان یک کشور، مصداق عمل مسئولانه نیست؟»
او همچنین در واکنش به انتقادهای «دونالد ترامپ» از طرح پیشنهادی جمهوری اسلامی، از مواضع تهران دفاع کرد و گفت: «ما امتیازی نخواستیم. تنها چیزی که مطالبه کردیم حقوق مشروع ایران است.»
بقایی در واکنش به صحبت‌های رییس جمهوری آمریکا گفت: «قضاوت را به مردم واگذار می‌کنم که آیا مطالبه ایران برای خاتمه جنگ در منطقه، توقف راهزنی دریایی علیه کشتی‌های ایران، آزاد شدن دارایی‌های متعلق به مردم ایران که سال‌هاست به ناحق محبوس شده، زیاده‌خواهانه است؟»
او همچنین گفت: «هر آنچه که ما در طرح پیشنهاد کردیم معقول و سخاوتمندانه بود و برای خیر منطقه و جهان است.»
سخنگوی وزارت خارجه همچنین مدعی شد که این وزارتخانه، از هر تصمیمی که از سوی نهادهای نظامی مانند سپاه پاسداران برای «تنگه هرمز» گرفته شود اطاعت می‌کند.
@
VahidHeadline
گزارش ایسنا:
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/VahidOnline/75396" target="_blank">📅 18:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrubNsYe35T3BnJ4HxVMc8uGNqtZBeShcAyDmINy_zbbC33IY4GVox7GIuTYGQH-5-nXQ69FWgTGU_XMALjHe4Yts6AcFHZNTXK-yxTq3qyJYXJBpHgP0yf2JQsc5Je9Z28CZo_gS1rZpiSDRwuDCUN9QmYukIem7jIXDnirJpGiNIPkPJ-XOGAAqmU3cu-f2P8-tc1uGbY0A0A4RMtAfuncoBT_DIpMrLIpxHHEpvaLiu1NQsi5OvpLN815dy8h0WjfVd97IC1Toh-rOXz99Kv1vqovMgDHN-Fz0N8VVkQHuKZ2q_utQAoJ8lew53mULnTlQLZOelAQRRedBzxXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار تصاویر ماهواره‌ای که نشان‌دهنده نشت احتمالی نفت در محدوده‌ای در نزدیکی جزیره خارگ است، سازمان حفاظت محیط زیست ایران می‌گوید: «منشا آلودگی مشاهده‌ شده در اطراف جزیره خارگ ناشی از تخلیه آب توازن آلوده یک نفتکش آسیب‌دیده بوده است.»
این نهاد گفت: «هیچ‌گونه نشت نفت از خطوط لوله، تاسیسات پایانه‌های نفتی و یا سکوهای متعلق به شرکت نفت فلات قاره ایران در جزیره خارگ مشاهده یا گزارش نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/VahidOnline/75395" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XIknh6Po-2G0VIcU1YD7grBCmams7SVYYBCVninScqaDJuP3i6hWOgQAZvBesPbqqF0N3ZzJzcLQpUg3WRSezm7w1gz2SzuWT9FB2oYfmVkpA3CvqQazE1rPqoYSmH0RQizfcqYQOklHQGzkgWuyO9YEXVgjb6xSGPwsfAhQHEXqYW24I1HR7EbHXh6E0f6-CtsJya-wi4TGFOtagtSyqQeoUImHWTYIQDkS6eMY-bQdG3fSNB-7iS3NaH3OE1XBHFEAyFG0an4ckNialxV-QPfHxzA2-E4uwkKfq2N4yGOh_zuewhrEpe8pMmVtdif4lF2NJTVse_0_THH3afdJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گزارش سی‌ان‌ان از اینترنت طبقاتی؛ «فکر کن با بدبختی وارد اینترنت می‌شوی و می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است»
♦️
سی‌ان‌ان در گزارشی میدانی با اشاره قطع اینترنت و رواج اینترنت طبقاتی در ایران می‌نویسد، قطع اینترنت در ایران اکنون بیش از دو ماه ادامه داشته و طولانی‌ترین اختلال ثبت‌شده تاکنون به‌شمار می‌رود.
برای میلیون‌ها نفری که زندگی و درآمدشان به اینترنت وابسته است، این وضعیت ویرانگر بوده است. فراز، ساکن ۳۸ ساله تهران، به سی‌ان‌ان گفت: «تصور کنید با بیکاری و تورم دیوانه‌کننده دست‌وپنجه نرم می‌کنید و به ترتیبی موفق می‌شوید ۵۰۰ هزار تا یک میلیون تومان جور کنید، فقط برای خرید چند گیگابایت وی‌پی‌ان تا بتوانید وارد اکس یا پلتفرم‌های دیگر شوید، خبرها را ببینید و صدایی داشته باشید.»
او افزود: «بعد وسط همه این استرس و خشم، وقتی بالاخره موفق می‌شوی اکس یا تلگرام را باز کنی، می‌بینی کسانی که دسترسی بدون محدودیت دارند طوری رفتار می‌کنند که انگار همه‌چیز عادی است؛ واقعا مثل مشت به سینه آدم می‌ماند.»
متوسط حقوق ماهانه در ایران بین ۲۰ تا ۳۵ میلیون تومان برآورد می‌شود. سی‌ان‌ان می‌نویسد، اینترنت پرو، شکاف عظیم میان فقیر و غنی را عمیق‌تر کرده است.
وب‌سایت «خبرآنلاین» نوشت این طرح «جامعه ایران را به دو طبقه متمایز تقسیم کرده است: نخبگان دیجیتال که از اینترنت سریع و بدون فیلتر برای تجارت، آموزش و ارتباطات بهره‌مندند، و رعایای دیجیتال که در محدودیت شدید، سرعت پایین و هزینه‌های سنگین بازار سیاه وی‌پی‌ان گرفتار شده‌اند.»
قیمت وی‌پی‌ان‌های بازار سیاه به‌شدت افزایش یافته و بر اساس اعلام سازمان «فعالان حقوق بشر در ایران» مستقر در خارج از کشور، قطع اینترنت طی دو ماه گذشته حدود ۱.۸ میلیارد دلار به ایرانیان خسارت زده است؛ رقمی که با برآورد اتاق بازرگانی ایران نیز همخوانی دارد.
روزنامه اطلاعات نوشت: «قطع اینترنت ــ که خود منبع درآمد شمار بسیار زیادی از کسب‌وکارهای مجازی بود ــ وضعیت بحرانی و پیچیده‌ای ایجاد کرده است.»گزارش‌های داخل ایران نشان می‌دهد «اینترنت پرو» از طریق «فهرست سفید» در سطح اپراتورهای مخابراتی و بر پایه «سیم‌کارت‌های سفید» عمل می‌کند؛ یعنی برخی سیم‌کارت‌ها، حساب‌های موبایل یا نهادها از سیستم فیلترینگ کشور مستثنا می‌شوند.
برخلاف وی‌پی‌ان که با رمزگذاری ترافیک اینترنت سانسور را دور می‌زند، «اینترنت پرو» ظاهرا کاربران تاییدشده را از مسیرهایی با محدودیت کمتر عبور می‌دهد. گفته می‌شود دارندگان سیم‌کارت سفید همچنان به اینترنت جهانی کامل دسترسی دارند.
بر اساس گزارش‌ها، هزینه اینترنت پرو برای بسته سالانه ۵۰ گیگابایتی حدود دو میلیون تومان است، علاوه بر هزینه فعال‌سازی ۲.۸ میلیون تومانی و حدود ۴۰ هزار تومان برای هر گیگابایت اضافی. در مقابل، اینترنت عادی ــ که اکنون به‌شدت محدود شده ــ هر گیگابایت حدود ۸ هزار تومان هزینه دارد و همین باعث شده بسیاری ناچار به استفاده از وی‌پی‌ان شوند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75394" target="_blank">📅 18:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MddkAsLiMAlnNOQnN3KIz2JfwL646mEiXlz7azXsJy406ri1b1PWIw2ETaidw9b7Tii1mnitEdpr5lp8J5kAw-W5CrzUH6wmE4avC1FOv7P5ikTjhniaOhHNPsZMOLLBvdLvQjSZrJ1bpTvZy6TESqSnDfQ-sFTJTijHjxKqmvCOvEY7F5EyZnbw-no1-zdz2FMZiOvDoSanZguVO1ifhetMf8R07ss0QA5fnqLTZxQW9ks2xFA-BmZzWhS0ITH83t8AbueAul-1oSwz-lJSu9WSLqkeEGTUFXLixRuUUxGAh92SrKEVzmF_50b82204_oq8ty4-uFk42VJyuO63Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی، صبح دوشنبه، ۲۱ اردیبهشت از اجرای حکم اعدام عرفان شکورزاده، زندانی سیاسی، با اتهام «همکاری با سرویس‌های اطلاعاتی آمریکا و اسرائیل» خبر داد.
شکورزاده بهمن‌ماه ۱۴۰۳ از سوی اطلاعات سپاه با اتهام «جاسوسی و همکاری با کشورهای متخاصم» بازداشت و به اعدام محکوم شد و حکم صادر شده علیه او به‌تازگی در دیوان عالی کشور تایید شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75393" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rq59BiAXX57r_XqU34xClhcOVLBUDPIMVmfV5jLftKwFU1ij9qKcsp6Kg1qVNY7g4DNK1jCQctheYozSx5P3617H5zJ8s4q0VovLPz9FRCgM9JG3kkq3Y_KbQKbeKU24KcvjJWHhfG8nQLY-KK4N81Ioj3g_WttnG2Z76VVhAUNQM7Uis4krUmF0Kp7sChdghEwBE43JxL0ofAzehiAUFByvPYXFT4Ju3CT-krTFRBZW4OteZ3yGcpv1HfJVoRhpk_B3uWVPgFbiFIg4_JfAFs_JHwYRI-NX89aLkjFEsCu_ijXoafJ31si8H7PCUQ-r7rQDuPnZaBRbl1vpZzfGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IHrjQ6j23nu1B5KiThqPDiL4owXDrsBfGKF9sHdYuSIm1MrviIUrpiWVsTrUwLOZj0iZsQ3zdzrQQ5lwHhTgXR39FrSXDlYHC8HRZVt-3LRzSO3YUh4SlyU_E85holCTOI9W_dYxxXxk1xJdEAbr93J4Gt7U_z8-RdZ7Aw_C13WJcrwIumO1tmpR8D4NSjFj0O3Jrq3x2gcYvdy_F9Mxm-Y8beez4SboDMsIsJaqLRz8A-Z8v-8USWmL1ns1AUefRLXBo0TZjJBjggNdqmA9Lbawrq6UFDLcXVmyO4cCkyFYjA_Z-vj6EH12Oyz2ddZ8KBp-9kPXZxA2nVsWaXKaAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس
: پرزیدنت ترامپ روز یکشنبه در یک تماس تلفنی کوتاه به آکسیوس گفت که پاسخ ایران به تازه‌ترین پیش‌نویس توافق برای پایان دادن به جنگ را رد خواهد کرد.
ترامپ اندکی پس از این تماس، در پستی در تروث سوشال، پاسخ ایران را «کاملاً غیرقابل قبول!» خواند.
ترامپ به آکسیوس گفت روز یکشنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، صحبت کرده و در میان مسائل دیگر، درباره پاسخ ایران نیز گفت‌وگو داشته است.
او درباره نتانیاهو گفت: «تماس بسیار خوبی بود. رابطه خوبی داریم.» اما افزود که مذاکرات ایران «مسئله من است، نه مسئله دیگران.»
ترامپ در این مصاحبه کوتاه روشن نکرد که آیا قصد دارد مذاکرات را ادامه دهد یا احتمالاً گزینه اقدام نظامی را در پیش بگیرد.
سناتور لیندسی گراهام، جمهوری‌خواه از کارولینای جنوبی، در ایکس نوشت که ترامپ اکنون باید اقدام نظامی را در نظر بگیرد؛ موضعی که گراهام در سراسر آتش‌بس یک‌ماهه بارها تکرار کرده است.
او نوشت: «با توجه به حملات مداوم آن‌ها به کشتیرانی بین‌المللی، حملات پیوسته به متحدان ما در خاورمیانه، و اکنون پاسخ کاملاً غیرقابل قبول به پیشنهاد دیپلماتیک آمریکا، به نظر من زمان آن رسیده که تغییر مسیر را در نظر بگیریم.»
گراهام نوشت: «پروژه آزادی پلاس همین حالا خیلی خوب به نظر می‌رسد»؛ اشاره‌ای به عملیات دریایی برای هدایت کشتی‌ها از تنگه هرمز که ترامپ پس از کمتر از ۴۸ ساعت به‌طور ناگهانی آن را متوقف کرد.
@VahidOOnLine
خبرگزاری تسنیم، رسانه وابسته به سپاه پاسداران، روز یکشنبه، ۲۰ اردیبهشت‌ماه، به نقل از «یک منبع مطلع» در واکنش به پیام ترامپ مبنی بر «کاملا غیرقابل قبول» بودن پاسخ تهران به پیشنهاد واشنگتن، نوشت: «همین الان واکنش به اصطلاح رئیس‌جمهور آمریکا را به پاسخ ایران دیدیم. هیچ اهمیتی ندارد؛ کسی در ایران برای خوشایند ترامپ طرح نمی‌نویسد. تیم مذاکره‌کننده فقط برای حق ملت ایران باید طرح بنویسد و وقتی ترامپ از آن راضی نباشد، قاعدتا بهتر است». تسنیم نوشت: «ترامپ کلا واقعیت را دوست ندارد؛ به همین دلیل مدام از ایران شکست می‌خورد».
@VahidOOnLine
خبرگزاری صداوسیما گزارش داد طرح تهران که ترامپ آن را «غیرقابل قبول» خواند، بر ضرورت پرداخت خسارت‌های جنگ توسط آمریکا و حاکمیت جمهوری اسلامی بر تنگه هرمز تاکید دارد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75391" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QAfkwzicqcwTqJIPub3vnSilVPDGLwWRhBt1sFhigIgVtYRFf-hm6GGx6kFLEGdfBEeXn1hSYRaODHfAh5Trk2o5NMttELEZnhbFi1ziWTaHzF9Wu8g0mqgTdYTbrYnlMr7PZQJNLNjZIXVz_8tvhLSq4X6C_pwNE0gUqAjxd4aECt1mPAFUffNmyRu9FKGto2hZVydAMHmvNLgmTJQEc1D2UhztEgYriAYSfNCoct6ktdxD2zMXSQyHOVJ-RxcYO7SMW9Yr5BIcTqF4pctyyezT_QaKxWOd2hfZwxoTXczxDuoeBjoKNG7wJhZqNYFpJBRpuwrsNmp_5neZ4C8dHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ پاسخ جمهوری اسلامی را رد کرد
پست ترامپ، ترجمه ماشین:
همین حالا پاسخ به‌اصطلاح «نمایندگان» ایران را خواندم. از آن خوشم نیامد — کاملاً غیرقابل‌قبول است! از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75390" target="_blank">📅 23:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eeB4GhGz_uUG1UHCHwL80FFI5_8TP0XrR2ERwowykdT18pTXBcR5UqeJ0eSFLTx-T4PnRxxG6HV8m2a8lhNwn-FecvhXR6YcxLiD2-PhJ86rNpO4p4wEJskrKAxQR77QiF3tGF7a4WIwBRe0g9EsRwwDt-CEfSQyzzay1Vspa-cZU11RUdCqvRIk-q2RVd-63TiHVxtswbqb9t6JUxkEODmouUqtUBdCEDFITP94xMX0tqNbJCVclfTL2C5PxqEbOWm_B6zXlK-zawSI61yNjabQjg_fWNpQgAhFk41GaiQLN2G9Ike4n16HzOXf6nKDTHZ4YqfPRHOEQBESqymHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال، شامگاه یکشنبه ۲۰ اردیبهشت ماه، به نقل از منابعی آگاه، جزئیاتی از پاسخ ایران به پیشنهاد صلح آمریکا را منتشر کرد.
به گزارش این روزنامه، پاسخ ایران که از طریق پاکستان به‌عنوان میانجی به واشنگتن منتقل شده، همچنان اختلاف‌های مهمی میان دو طرف باقی گذاشته است.
به گفته منابع وال‌استریت ژورنال، تهران حاضر نشده از پیش درباره سرنوشت برنامه هسته‌ای خود و ذخایر اورانیوم با غنای بالا تعهد بدهد.
ایران پیشنهاد کرده مسائل هسته‌ای طی ۳۰ روز آینده مورد مذاکره قرار گیرد.
مقامام‌های ایران همچنین برای رقیق‌سازی بخشی از اورانیوم غنی‌شده و انتقال بخش دیگری از آن به یک کشور ثالث اعلام آمادگی کرده‌اند.
وال‌استریت ژورنال گزارش داد تهران با برچیدن تاسیسات هسته‌ای خود مخالفت کرده، اما در عین حال آمادگی‌اش را برای تعلیق غنی‌سازی اورانیوم اعلام کرده است؛ تعلیقی که به گفته این روزنامه، مدت آن کوتاه‌تر از توقف ۲۰ ساله پیشنهادی آمریکا خواهد بود.
بر اساس این گزارش، ایران در پاسخی چندصفحه‌ای به تازه‌ترین پیشنهاد آمریکا برای پایان دادن به جنگ، خواستار پایان درگیری‌ها و لغو محاصره کشتی‌ها و بنادر ایرانی شده و پیشنهاد داده است تنگه هرمز به‌تدریج به روی رفت‌وآمد تجاری باز شود.
وال‌استریت ژورنال نوشت ایران در مقابل، خواستار تضمین‌هایی شده است که اگر مذاکرات شکست بخورد یا آمریکا در آینده از توافق خارج شود، اورانیوم منتقل‌شده دوباره به ایران بازگردانده شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75389" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q76RBGc8OtZbOniSNVe21KXAMlETpynm3J4OzHDWOOX6yy0ICCYiiHpSOsmt7y1bxGa1086_CPs2ru58EGwjcjrpMdIP6R7GfqBr5R3IZcZUu8LV3RdRIhPVfZXUAoA58Rr6IX_tnE__eguKeR8f1z2Fe2YC-SfcN-R9FrMF2PNIRDsCpe__97fal3C-Pj54QpphEfS1AqsNQguLlQMpYJ3kGY83UEFAdv2MbvJdT1RsJkZ6EcAyYWhbHMSr2dSbJyjAznB_3gDVBuNZFaILLhnaVxikNueSICs1S2KqHd-n_GS7NfdWUHrW3MxUUHpfd-lbXVoYjQ2A9a4BcqlZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران شامگاه یک‌شنبه با اشاره به شنیده شدن فعالیت پدافند هوایی در اندیمشک و شمال دزفول از سرنگونی «پرنده متخاصم دشمن» در اندیمشک خبر دادند.
شهروندان نیز یک‌شنبه ساعت حدود ۱۰ شب از شنیده‌شدن صدای پدافند در این شهر خبر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75388" target="_blank">📅 23:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#دزفول
#اندیمشک
پیام‌های دریافتی از شنیده شدن صدای پدافند:
پیام ساعت ۲۲: دزفول حدود 20 دقیقه صدای پدافند میومد
دزفول وحشتناک صدای پدافند اومد.جدود ساعت نه ونیم
سلام پایگاه چهارم شکاری دزفول از ساعت ۲۱:۳۰ تقریبا یه ریز پدافند فعاله
پدافند پایگاه وحدتی دزفول فعال شده از ساعت ۲۱.۵۰ تا الان ۲۲.۱۷
فعالیت  شدید پدافند در اندیمشک ساعت 22.15
اندیمشک
ساعت 22:19 امشب پدافند فعال شد در حد 30 ثانیه.
یه صدایی میاد انگار پهپاده
سلام، اندیمشک ۲۲:۲۲ دقیقه چند دقیقه ست پدافند ها فعال شدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75387" target="_blank">📅 22:32 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KmrcnFae3M9u5JLRz8q12eiPSZAYLXGtpqcm2yN0FbSqZ0gfFynkbp3NSrYB0GOgE2h2MOZ3J1H1gqK7kfeDJZL4i07cRM7PJeS9z2haVsMI474TT3hbWYiRH1B0ZokNMNvseCpQVimC2J0pI_llsEF9bPssmtIfSYIGfgvb8yc4okn3u5JJzGnfqj_WM7DJ-Hfopwj-QySCuRWxQqPZ1iotTrvFUGZjiSUjuOH3z5qqERbTqFb76Z8Kwjll0rT0nfycitO2yDP_2h8las24D52uvrsQGXn-AxRBi32xMyY-B5WWNUOHCBGQiAGLqkJzxFpaTplHNfwMrgN362OBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آن‌ها دیگر نخواهند خندید
پست تازه ترامپ پس از آن که جمهوری اسلامی گفت پاسخش را از طریق پاکستان ارسال کرده. ترجمه ماشین:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است؛ «تعویق، تعویق، تعویق!» و سرانجام وقتی باراک حسین اوباما رئیس‌جمهور شد، به گنج رسید. او نه‌تنها با آن‌ها خوب بود، بلکه عالی بود؛ عملاً به طرف آن‌ها رفت، اسرائیل و همه متحدان دیگر را کنار گذاشت و به ایران یک فرصت تازه، بزرگ و بسیار قدرتمند برای ادامه حیات داد.
صدها میلیارد دلار، و ۱.۷ میلیارد دلار پول نقد سبز، که با هواپیما به تهران منتقل شد، مثل هدیه‌ای روی سینی نقره به آن‌ها داده شد. همه بانک‌ها در واشنگتن دی‌سی، ویرجینیا و مریلند خالی شدند. آن‌قدر پول بود که وقتی رسید، اراذل ایرانی نمی‌دانستند با آن چه کار کنند. آن‌ها هرگز چنین پولی ندیده بودند و دیگر هم هرگز نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما پایین آورده شد و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آن‌ها بالاخره بزرگ‌ترین ساده‌لوحِ همه تاریخ را در قالب یک رئیس‌جمهور ضعیف و احمق آمریکایی پیدا کردند. او به‌عنوان «رهبر» ما یک فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
ایرانی‌ها ۴۷ سال ما را سر دوانده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای خود کشته‌اند، اعتراضات را نابود کرده‌اند، و اخیراً ۴۲ هزار معترض بی‌گناه و غیرمسلح را از بین برده‌اند و به کشور ما که اکنون دوباره بزرگ شده است، خندیده‌اند. دیگر نخواهند خندید!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75386" target="_blank">📅 21:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUOI-nRO22wCl5V0ACmySbeNsBwSZ74WG8xAYogdN_cGyirtU61BLUCmFUCeXthdhHX5knZ138HXCCanExXDg6sGBrZllFfaZjEcM7zW_xhf4NpBW-LI4qT1j7GELRq68WrBXYvcemm8mP0Y9InvCrYF9wIh99Kcz2Li0NZ_jqRukVXyB6LubqkJ9eptXzggHCZ8dFG9PRNfymW1BeFhGKiIFpUnNANlc78oc4hrPQ1goqvPz_97ndFIIhcmW8Z0NwE3w1C35_z0Rt5AMupkYDKhvB5r8OYfTFX84WbrEaQNtqY_JeJeaNDe7fUMggzK5cdUKLrFqJkqSIMvfQ41Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در بخشی از یک مصاحبه که قرار است ساعاتی دیگر مشروح آن پخش شود، گفت که ذخایر اورانیوم غنی‌شده ایران باید از بین برود تا بتوان گفت جنگ آمریکا و اسرائیل با ایران به پایان رسیده است.
او در بخشی از گفت‌وگو با برنامه «۶۰ دقیقه» شبکه سی‌بی‌اس گفت: «این [جنگ] هنوز تمام نشده است، چون مواد هسته‌ای، اورانیوم غنی‌شده، باید از ایران خارج شود. تاسیسات غنی‌سازی هم که وجود دارد باید برچیده شوند.»
او همچنین گفت: «ایران هنوز از نیروهای نیابتی حمایت و موشک‌ بالستیک تولید می‌کند. بخش عمده‌ای از اینها نابود شده‌اند اما کارهایی باقی است.»
آقای نتانیاهو در پاسخ به این پرسش که این اورانیوم چگونه باید خارج شود، گفت: «وارد می‌شوید و آن را خارج می‌کنید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75385" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75384">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVx0zE0jx-KWSOrvejzEUhGX_wxITcIuHbSTMAL74xnEfxBbrsuyM-mogzgAIvdNkCaBCay185yITsMycYEzIndgqrk27TPSWz9o0a51HhEls-0vs5WXSBNNJmfzGkf9-mVHyKMTVrkDSxitvIgcLhvuiDYdzC7VChRkS0Nnsd82Li-eYeSuLzakD9UBWUpe-6kAEwBD7oClG-A5izSn-oChQECFVYtOapk1JPQMV0BntSbuxi_TnFioa6SMgyUdWLta2BudnJxlPS0etM7WX6ZV_qhEInNbG1-bnWa8PoErFW3dsjyLLWoi023Z5o3Xr0zFIcUXHkgRLQwU4-sT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Afkham_minus
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75384" target="_blank">📅 19:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75383">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAB7EVIrcLu5XWlWKW6lCzwFIJWVvQbJsW7kfBrns2vVlMeFS9_iS4OxRqru7rZGyduv6A-iGohEV7jOF4BhUaT1duO3Qg7PkXDNY1cTmWvyy4IxWeeTmFMeL7rzF3jxL5CTF2nblP3FGQHvnzKLDB4rnN0aTNYLSBYSj9VZcLC5VNcY2yAJHP0Y43GXqeEwBx1MkhvTFM9qrjwWMaBGwBb-jQbeF4H06Hh8dj1lh_y5T65hfzb_lPdQvN4MIVDV6qQ8SCCtBrrQxdEXRflTTwceDpekr-n-kx1sDoAcNMsYFHdcQDUVvPl79HurMiyhsXxEFqhzp5ZarujJ0u5FoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رحیم نادعلی، معاون فرهنگی سپاه «محمد رسول‌الله» تهران گفت: «در جشن بزرگ پیوند آسمانی زوج‌های جان‌فدا، خودروهای جیپ جنگی برای جابه‌جایی عروس و دامادها در نظر گرفته شده که با گل‌آرایی، پرچم جمهوری اسلامی و تصاویر رهبری تزئین شده و زوج‌ها در این خودروها در مراسم حضور خواهند یافت.»
او افزود زوج‌های شرکت‌کننده قرار است با «ماشین‌های عروسی به شکل جیپ نظامی» و «خودروهای نظامی گل‌کاری‌شده» در سطح شهر حضور پیدا کنند تا «فضای شهر را به یک شکل هنری و نظامی» درآورند.
به گفته او، هدف این است که نشان داده شود این «زوج‌های جانفدا» جان خود را «زیر پرچم جمهوری اسلامی تقدیم این نظام خواهند کرد» و «از هیچ چیز نمی‌ترسند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75383" target="_blank">📅 19:39 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q8I_1tuXP-ACyZNW4v68xG7rGdWswZiVBxa4jrPTPSdjPvpRhu1AzmRisBSJBkzDMx4B995iMoXseDmr9qi5Jp6Y0JMTzgWL2cWuzJe4Av6APjYvGq57n_oy2B7VbuCdAFnobYsBYfT5oxfNOQsOh7_aNegjLqqyH0mpgr_YPJCiI6NHM9tfJlfmKdGvoWdUea6p0q_PaXz1FfEna7AoLHlEcAI7EKyfkNqlINnjVEyEfipDgsnMCo7ZXVfKEQXAzuXGBHuyAKqqexBJTX3tRVP448WQz5fFkLmlBFjKZbJ7Gj4cl9-b4b_f900K9ZiVq2O9rAoUQ_Dtr4DT4f78lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eBWLwrjO0d_5sLtT2K5f6RCghnb2arTDFmFoV0XaCNJNriLctfac78aX4UGiI-wV4bPm-ovqAthYupfecE8OI9sS-stikJHDMHEvK0Y2g0H9XckDm5YTeBr5xPDwSq-DNWQ7zZouX7tK2biRR4vBd4Zghd2ta9BFL1aFqq7sXh1nFwXSx50d7BvclHMHMnuwYJ5QrEcRagTzrNxX03hoMhvpAYH9pJrBhH1tn52yvt28OcT_K0D1E0862TnpZcrLb6h-a8PCcoUBVM9ji0UZw3mIHY6F3fITQmAotpOCKz2wIyhWDYR2KJQtT3OAuSAchBLvAbtyOJkgPxhgxyeegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l963J_y1Jbr0Ua_EJv0ldwHR_6PiFTujBesPgt3ltiCL94vFyePVGJh4VWp_IqOcHku6TP7IWMg6f1oQtKpf9pWJNeped9mYc-CPYEoqxtKthUJlB25DqTYpHYoK3nqAsDjx11MI5j0GbnZ7fwMbF1vwus4mCyxMijaIDXMPl1h6NE_UhDTcwV_hxcARkAaYjWKjC05u6NrD6Idf5EaSlQlOlo2TqlzLKVhSSd1yxhTmD3DLVAKwGFYOmnZ_eUxrg7b2luWl7FXHHailO8U6HQ8juMOKMmuanEdoQbywUAa0_QiNGkwGlFSrdD6jJWUw7m0PuunPlGVwIu7aT2qvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WVGeS2FE-HLyOUQdSvVB0BeaFhg7_pGmuPWNCjcroMd7_pOlZmGIm3T4PCIDBbAY9Q7RUfUWdhTqNM9qAW88Ur_41RLSrOEyFUTTXZv-Kn6JeDZSH-JnqP-ULprxxC_62gBep3UEE1WC1aNF2-kF60baZOrFqcMAWOnWdnd7Yb_UajOBdh2SSnv4VXgzMg5Epo9WEOn9YJeJclqwyjd-ZeWrDD8TnnM8EQv95Ir1xbh634Px78k_o27Y0f8i833DMjxwp3whlHu_Hsc-Mtafzga2ikx1tGDJ56rTkKANftB8XmMcpOmRL63a8drkxeoMijFvbqJUrmSIkft4ix6wkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uq_JB5wytNidZ2QPMIrbDNBySEIVdH3LHjinGI_vmco5b06u3ZgLyOjZ8iwUQfAPKQNobh6NNXYV6nQYqjxTehreavJNU2lWtVogLu7gc5TBJDzijSgfacvtWnxCxpyyqMFwou9xpZ0PRlXa3FxTEh_iJyww5nbGDE6yjGg1lEgWZTj99DjgnUrAS9mesI6UR8FDnPyMnwMf7BR7IUqTo62bsjmfruRJb0QZRfqbNj5IqqZRIyqhahRrKcIAUnSfjlbTl0To81wsNO3Y51wXT19K9-FwHkaCU0FBvLrB9BfBajIdx1row7XkiyQ36Bh4Q8U7zKuNuslUVjOBJHKIjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا می‌گوید عملیات نظامی در ایران تمام نشده و ارتش ایالات متحده می‌تواند اهداف دیگری را نیز هدف قرار دهد.
دونالد ترامپ در گفت‌وگویی با شریل اتکیسون، مجری آمریکایی، که هفته گذشته ضبط و روز یکشنبه ۲۰ اردیبهشت پخش شده است، در پاسخ به این سوال که آیا عملیات رزمی در ایران تمام شده است، گفت: «نه، من چنین چیزی نگفتم. من گفتم آن‌ها شکست خورده‌اند، اما این به آن معنا نیست که کارشان تمام شده است. ما می‌توانیم به مدت دو هفته بیشتر هم وارد عمل شویم و تک‌تک اهداف را هدف قرار دهیم.»
او با اشاره به این که در حملات آمریکا و اسرائیل طی جنگ اخیر «احتمالا ۷۰ درصد» اهداف مورد اصابت قرار گرفتند، افزود: «ما اهداف دیگری هم داریم که احتمالاً می‌توانیم به آن‌ها حمله کنیم. اما حتی اگر این کار را نکنیم، سال‌ها طول می‌کشد تا آن‌ها دوباره بازسازی شوند.»
به نظر می‌رسد اظهارات آقای ترامپ پیش از ارسال پاسخ ایران به آخرین پیشنهاد آمریکا برای این توافق انجام شده است. هرچند که او پیشنهادات قبلی ایران را رد کرده بود.
رئیس‌جمهور آمریکا در مصاحبه با شریل اتکیسون همچنین دربارهٔ اورانیوم غنی‌شده ایران که در عمق زمین و در تأسیسات هدف قرار گرفته در جنگ ۱۲ روزه سال گذشته مدفون شده‌اند، گفت: «ما در مقطعی آن را به دست خواهیم آورد… ما آنجا را تحت نظارت داریم.»
ترامپ اضافه کرد: «من چیزی به نام نیروی فضایی ایجاد کردم و آن‌ها آنجا را زیر نظر دارند… اگر کسی به آن محل نزدیک شود، ما مطلع خواهیم شد و آن‌ها را نابود خواهیم کرد.»
او بارها اشاره کرده است که توافق با ایران باید شامل تحویل ذخایر اورانیوم غنی‌شده ایران به آمریکا باشد. تهران چنین درخواستی را رد کرده است.
@
VahidHeadline
رئیس‌جمهور آمریکا گفت: «ما نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد، چون آنها دیوانه‌اند. نمی‌توانیم اجازه دسترسی هسته‌ای به آنها بدهیم. اوباما این کار را کرد. اگر من توافق هسته‌ای ایران را لغو نکرده بودم، الان سلاح هسته‌ای را داشتند و الان علیه اسرائیل و خاورمیانه و شاید حتی فراتر از آن استفاده می‌کردند. می‌دانید، آنها در واقع موشک‌هایی دارند که دیدید می‌توانند به اروپا برسند.»
از آقای ترامپ سوال شد آیا این درست که عملیات رزمی علیه ایران تمام شده است.
رئیس‌جمهور آمریکا پاسخ داد:«من این را نگفتم. من گفتم آنها شکست خورده‌اند اما این به این معنا نیست که کارشان تمام شده است. ما می‌توانیم دو هفته دیگر هم وارد عمل شویم و هر هدفی را بزنیم. ما اهداف مشخصی داریم که احتمالاً ۷۰ درصد آن‌ها را زده‌ایم اما اهداف دیگری هم هستند که می‌توانیم بزنیم.»
آقای ترامپ گفت حتی اگر هم این کار را نکنیم، بازسازی سال‌های زیادی برای ایران طول می‌کشد.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با سی‌بی‌اس نیوز درباره اورانیوم غنی‌شده در ایران و جنگ علیه جمهوری اسلامی گفت دونالد ترامپ به او گفته می‌خواهد وارد آنجا شود و به نظر او این اقدام از نظر عملی امکان‌پذیر است. او افزود اگر توافقی حاصل شود و بتوان وارد شد و این برنامه را برچید، این بهترین راه خواهد بود.
نتانیاهو از پاسخ به این پرسش که در صورت عدم توافق چه رخ خواهد داد خودداری کرد و گفت برای این موضوع جدول زمانی تعیین نمی‌کند، اما این ماموریت را بسیار مهم دانست.
IranIntl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75378" target="_blank">📅 19:20 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-yIxmaHouboneABfQEKdu8rJSvLLuZSLNWY__CqXQ0cfWWm3xnnpnCgrNFJpPg8XRT-GS_bot_rHmZ8jYBFpoJXLDt_muqACmCoSbaf4B7dibhJ5dzXEce3wu_SrPIIbBZUW94RySaankyq3SZG_fCchOJFiapm78JmGKxs2NTqeclApqDX7eKAk1d30K04a_ysbWJfSJqrc8M2j9TfqvN1O0mu4tEjcBYaIQvxVEXpNAcfavEfgJ1NiXVBsfIc8W_l4SwaGo5K2KASh2-GfoN5JfWwjGskfgUH2GKnLPEGgsSma7N-t9To-zD6tjqTFQLeg4BQ6o6UCxlw7-fukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایرنا، روز یکشنبه ۲۰ اردیبهشت ۱۴۰۵گزارش داد پاسخ تهران به آخرین طرح پیشنهادی ایالات متحده برای رسیدن به توافق بر سر پایان جنگ، برای پاکستان به عنوان میانجی مذاکرات ارسال شده است.
ایرنا بدون اشاره به جزئیات بیشتر نوشت: «بر اساس طرح پیشنهادی، در این مرحله مذاکرات متمرکز بر موضوع خاتمه جنگ در منطقه خواهد بود.»
وب‌سایت اکسیوس و خبرگزاری رویترز، چهارشنبه هفته گذشته گزارش دادند که واشنگتن و تهران به یک «یادداشت تفاهم یک‌صفحه‌ای» برای پایان دادن به جنگ نزدیک شده‌اند.
رویترز نوشته بود در این تفاهم‌نامه حتی به تعلیق فعالیت هسته‌ای ایران یا بازگشایی تنگه هرمز که از سوی سپاه پاسداران بسته شده، اشاره‌ای نشده است.
در مقابل، روزنامه وال‌استریت ژورنال گزارش داده بود که در طرح پیشنهادی آمریکا، تهران باید ثابت کند که به‌دنبال سلاح اتمی نیست، تاسیسات فردو، نطنز و اصفهان را برچیند، فعالیت زیرزمینی هسته‌ای را متوقف کند و همچنین بپذیرد غنی‌سازی را تا ۲۰ سال متوقف کند.
رییس‌جمهور و وزیر خارجه آمریکا روز جمعه گفته بودند جمهوری اسلامی تا پایان همان روز قرار است به پیشنهاد ایالات متحده پاسخ دهد.
@
VahidHeadline
ولی جمهوری اسلامی به جای جمعه، روز بسته شدن بازارها، صبر کرد یکشنبه پاسخ داد که ساعت ۸ شبش به وقت شرق آمریکا بازارهای مالی هفته کاری رو آغاز می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75377" target="_blank">📅 17:51 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLpge-x3h60NZ26YjfLFki_3ZEyRBDrh1Bh4LOc0DzkmUmGsuvr-lRf7IWihbxjFZkhWBp3rsGsbjbr-nf_cb0NCQK0EYc-YKB3K-cGIJZZSRk1DQGTvFYOmva5aoUdfCHjAP_qReO-wc-rF87As_VTBFABHxJ0Kp2_3AdHgu6S9LM3Lk0kw30-xRdr__w1zroXJAZvJE6c-oaO-XbcCqNJ_AIuesV-AnqAKwy_qVwRGayMSTUdjfkv2Es0mpo4xPN51Hc4i1nzThmuIRJvsxcvRz0NE0XDbCVBE8xoccXvOMN0DhH8aYBaQje072cXlWlheJWUQjjVylctEFAXDqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی روز یکشنبه ۲۰ اردیبهشت اعلام کرد که سامانه‌های پدافند هوایی این کشور با موفقیت دو پهپاد پرتاب شده از «ایران» را منهدم کردند.
این وزارتخانه تاکید کرده است که از زمان ««شروع حملات آشکار ایران، پدافند هوایی امارات متحده عربی در مجموع ۵۵۱ موشک بالستیک، ۲۹ موشک کروز و ۲۲۶۵ پهپاد را منهدم کرده است.»
وزارت دفاع امارات همچنین گزارش داده است که از زمان شروع حملات آشکار ایران، تعداد کل جانباختگان نظامی به ۳ نفر رسیده و تلفات غیرنظامی هم ۱۰ نفر از ملیت‌های پاکستانی، نپالی، بنگلادشی، فلسطینی، هندی و مصری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75376" target="_blank">📅 17:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGx9N8NIjsTXqLEvDjDyBorKRh0MxJC67CQc2gLxzdIGqoDcY7jjoBp2FUagUTGy-pEFcbVqmw6_HNBg36gjlL_R2z55BKAnnQfq5YtB_C4VY5YZfidvWzVmd8OkJcEh28GkJypvbBkEk-FIZiNLchftFGGeyL5t5ZQMH3OGGzn_f3FjxL8Wpm4u2Ryn6fkIih-6rAwZ6bvZTUtjXdKhuhq9ky62xX3TpgF-_lHBR-Rm0JllTefQPA-cRk9vfe6ZlraeXU3jQVQ3rQBF2L0cKWh4cZqtfTBQifOf_CkGyvXu8ZUAQTlUKgaE3pZqWO9sZqAg12tqtH6-qMuqiLn1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی گفته‌اند علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، با مجتبی خامنه‌ای دیدار کرده و گزارشی از آمادگی نیروهای مسلح، از جمله ارتش، سپاه، نیروی انتظامی، نهادهای امنیتی، مرزبانی، وزارت دفاع و بسیج ارائه داده است.
بر اساس این گزارش‌ها، عبداللهی گفته نیروهای مسلح از نظر روحیه رزمی، آمادگی دفاعی و هجومی، طرح‌های راهبردی و تجهیزات لازم برای مقابله با «دشمنان» در سطح بالایی از آمادگی قرار دارند.
این رسانه‌ها همچنین نوشتند مجتبی خامنه‌ای در این دیدار تدابیر تازه‌ای برای ادامه اقدامات و مقابله با دشمنان ابلاغ کرده است. با وجود انتشار متن این خبر، رسانه‌های جمهوری اسلامی تصویری از این دیدار منتشر نکردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/75375" target="_blank">📅 17:46 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vkwc9fR0ZTYurHlRv-uJad9n2bXgMJi7yEV_5fbdNgXYCXk-0Y88Lb34dbvpvCidX2EqhWwYI1m6EHXZYC0QugpCvadsGxCMnG-OrOJD8VhfAmH_2-Q9jhZkZpIIE-kAhIF3FXO12b0dQWoB4x1AzTP-V0MtVrpDyTtqQMBV371gyZJcWvxgIuY964E3ZxB_xWnVQH8usSBm0uaSsB9obRSuQ8A_r0qjb6SiJYexK-TUK2fgmDGSJDOE2X8AAYPjl-r9mP0VMIFZxKh0isfhIpHBlqrPvPv3F4BLguUE2LvOXvhRMlaQPz79-At64nxVpF1Uy9Un-tLwncxBxLuD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران درباره کشتی باری هدف ‌قرارگرفته شده در نزدیکی سواحل قطر، به نقل از منبعی که نامش را فاش نکرد، گزارش داد این کشتی با پرچم آمریکا تردد می‌کرده و متعلق به ایالات متحده بوده است.
سازمان «عملیات تجارت دریایی بریتانیا» (UKMTO) صبح یکشنبه گزارش داد که یک پرتابه به سمت یک کشتی باری  در ۲۳ مایل دریایی (۳۷ کیلومتری) شمال شرقی دوحه شلیک شده است.
بنا بر این گزارش یک آتش‌سوزی کوچک در این کشتی رخ داده که خاموش شده است و تلفات جانی نیز نداشته است.
این خبر در حالی اعلام شده است که مارکو روبیو، وزیر امور خارجه آمریکا روز شنبه با محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر امور خارجه قطر، در میامی دیدار و گفتگو کرد و شراکت دو کشور را برای بازدارندگی در برابر تهدیدات و تقویت ثبات در خاورمیانه حائز اهمیت خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75374" target="_blank">📅 17:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV9ixkwMYaQTZzIKhWCEtwU79zeuvOTNu1GL74XhDsUMfZfzH193jiA1zTCAL8HR5atPqSqoYZorvNtqo4IcBHwT57nv2PPBDgfRCx15Rz0uG8VNh6y2oH_27YchgykUJpyLligQoi6OjwFpfRc3r4brnhiCfFHDKSmjKtezBw0UpyjnW0ZF23to5dJ5DaV97rSeq9dblEQgrwiBwaae4bW7nu2KMjG786_09-1_KMwk5nZp6ZVRG1yt1PfQU4S297zgXUWsTJVIkP6geux-b_PSuAuEabW5hq-frzYtDW6TbXlDYixTmm5xHXI_93i4L6GlDjuc6eYlzqVwy63hog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
خبرگزاری فارس می‌گوید «یک نفتکش حمل‌کننده گاز طبیعی مایع متعلق به قطر به نام الخریطیات» با «اجازه ایران» از تنگه هرمز عبور کرده است.
بنابر این گزارش، این نفتکش «روز گذشته در دهانهٔ تنگهٔ هرمز دیده شده بود و پس از آن سامانه موقعیت‌یاب خودکار خود را خاموش کرد.»
به گفته فارس، «این نفتکش که مقصدش پاکستان است، نخستین نفتکش غیرمرتبط با ایران است که از نیروی دریایی سپاه اجازه عبور از تنگه هرمز دریافت کرده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/VahidOnline/75373" target="_blank">📅 17:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvauVjSJtAOoaO_OfMe_jsE8pC99gJHQc2aF3EckQjMC4yhBFahPaxHLco5njpt0xuzzvuaO7dFC9qV2HjL2Y4QmDamSVfKhrUeXrBrr8gQMc1VvlbfauQ1JB5WvLQ2WsolGiQENVF7mmwkTYdztg-EzHFb607jfsYt6fX60A6WKda_effZz6xHV7yOk158AaloLZ29QbMl6y8raduiFa-3dM2khOeewI9kJiyx0EHC18TceLK6EFAbrXCDl2bNj2cxCyXDDP2MijjJla9Dakipufbt0_vAS9SuiCjTjCib4DR2LuqOB12HfTO3gwfHOlYlRzasFREZFd5k0D0mvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخل ایران روز یک‌شنبه به نقل از مدیرعامل شرکت پایانه‌های نفتی ایران هر گونه آلودگی نفتی ناشی از تأسیسات جزیره خارک را تکذیب کردند.
او گفت: «به محض انتشار این اخبار، گروه‌های متخصص اچ‌اس‌ئی و اداره شیمیایی و آزمایشگاه، همه منطقه را پایش کردند اما حتی کوچک‌ترین موردی یافت نشد.»
خبرگزاری رویترز گزارش داده بود که تصاویر ماهواره‌ای ثبت‌شده در روزهای ۱۶ تا ۱۸ اردیبهشت، لکه‌ای بزرگ را در آب‌های اطراف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، نشان می‌دهد که به گفته کارشناسان با «نشت نفت» سازگار است.
بر اساس این گزارش، لکه‌ای خاکستری و سفیدرنگ در غرب جزیره خارک دیده شده که به گفته یک پژوهشگر «رصدخانه منازعه و محیط زیست»، مساحتی حدود ۴۵ کیلومتر مربع را پوشش می‌دهد.
به گفته عباس اسدروز، «طبق اعلام مرکز بین‌المللی «میمک» به نمایندگی از سازمان بین‌المللی دریانوردی هیچ‌گونه نشتی در زیرساخت‌ها، مخازن ذخیره‌سازی، سیستم‌های اندازه‌گیری، اسکله‌ها، خطوط لوله این منطقه و کشتی‌های در حال بارگیری وجود ندارد.»
اسدروز توضیح نداده است که لکه موجود در تصاویر نشان‌دهنده چه چیزی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75372" target="_blank">📅 17:43 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOLimn407VPudi7FYM7v3KSE_dlac3pNqQNBIWFSYviOX0YkqkyQV5JG64yClHknKg2oi8HddLN8OLt4oC8SY0372Do1w3SUBibr0KclkJPF4GvpyarOI5oOciaCXfs-wTDFKLP8jDsfyz7OoaNz22XAo4HT_SSPMdHqV7pfVunhwtYW_h5wh8pKcgKAD6sirEwozAMoi-ysWxOCY3LVL57xfXPCB1rYdOWkkhK0Rf1xUeIsW-PdDaSmCApaeRswPPheC8qVhb6SU97y8YbgvkdKv1BixAKiQf6rwnQ897Sg7t92rJyaAWrmDGCsVhfu6i1OMV_OPOBxB4eJCYdKQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «وال‌استریت ژورنال»، اسرائیل در اقدامی بی‌سابقه یک پایگاه نظامی مخفی در بیابان‌های عراق ایجاد کرده است تا از این طریق عملیات هوایی گسترده خود علیه ایران را پشتیبانی کند.
این پایگاه که پیش از آغاز درگیری‌ها و با آگاهی ایالات متحده احداث شده، میزبان نیروهای ویژه اسرائیل و یگان‌های امداد و نجات برای خلبانانی بود که ممکن بود در جریان حملات سرنگون شوند.
طبق گفته مقام‌های آگاه، استقرار این مرکز لجستیک در فاصله ۱۶۰۰ کیلومتری از اسرائیل، نقش کلیدی در مدیریت هزاران حمله هوایی تل‌آویو علیه اهداف نظامی رژیم جمهوری اسلامی در خاک ایران طی هفته‌های اخیر ایفا کرده است.
این گزارش فاش می‌کند که مخفیگاه مذکور در اوایل ماه مارس و پس از گزارش یک چوپان محلی درباره تحرکات مشکوک هلیکوپترها، تا آستانه لو رفتن پیش رفت. در پی این گزارش، ارتش عراق نیروهایی را برای بازرسی به منطقه اعزام کرد، اما نیروهای اسرائیلی با اجرای حملات هوایی سنگین علیه سربازان عراقی، مانع از دسترسی آن‌ها به این سایت سری شدند که در نتیجه آن یک سرباز عراقی کشته و دو نفر مجروح شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75371" target="_blank">📅 01:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eVRHcHqVl-VM_u-DND8NITIb1CPdMuzRmsUcIe41vfRRV-PflygQ29_ruG9M5lQ0QVGnHuUqMXmOOczIY8N6CBzaaivEi8de2xvmQXzawe590oo7VCW-xsU5VWTl6jRBKN30y_x27QapuH-Xlu8qhWKztSV4I8TOitGYZUDTYSFiG8dSVkN-gIzb9i4Am3Iv9MTc_7LdXlq4fds1pCvlHM0S8OmfmiePAj4m_krhc-DLZGpdX7jyibLLAk2vC7KW0JCD_7QyKAot05t1PoX3kn1-oavTmt6mokl4CJrDOumPgFBQdRvgF_COY3OD0keqlhnk7NUhYer7qGyRX4ZQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EHJGRedP_cqJDHBOnYWJeg_K1CPAwtzokYFCSNoffuHMoJDo1vRwMwMfu7FzEWTi6CXtChC_luMWFgXrfN6j_FW2541z01Qm8rVF5RULBlvHiErg8amS-IKsR_aEeHbnPUmnfmYscwWb8ohEUqfkgrAniSHTHnFJa2LFJq8UGHBNOAd1HPB2_5L0gv8qD2IoUC3M32KNUZtYO3CFhu7iK3Sv4PNutw5OMqt5q2eW5hYq5C_hu0W3F9tO7bzpCe6iO7yAtsN3YPQRbul9pnvdRDhnWMQ1SiSFYVZJkOkis84QJUNgVLNTFGE4nhfoCJAMdgzQPtsmfJS6XPUPpdAHSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر ساختگی دیگری که ترامپ در صفحه‌اش منتشر کرده
:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75369" target="_blank">📅 01:15 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TxGfoiW5JuOiVFIQa49iIhzAca6vvdazMt-vU9qJCuNsXpA2NR_aALPFNOHZZ5w7QIgVpjU6YihbKT0ha0mjpy3h0cl-2WaH7gs8JqsLDmMe9czLcJNcUlUc1vFcVOiDHtithIf1uEeokZW-jbzdu6fUMIPGeytMPXYzenZoU48A9Hm5HwAFPpFD6DyykI7iltWw07HtjEbpMvyBd6Xib11Cn9H-a9sc5QpMJcnfOPPUEyVKYgAvRlKRsTTcxU_UlqH4mK4rVaaBGoNP-CWy7qWIhtf6-Wt-bUpf7qmB-cRhVOfvWBy--jg3DQbYfgbGBO3KP6gt9ftInrnmqTLKjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75368" target="_blank">📅 23:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7nMKbjkbhFnmLoxuEtT8vr8imI9sPUx6v3Oom1eVtND_9Sb7CgPh2B1mKw5J1TWjOQ29DBcu7y9GMLEQghUayusQc0HXp-UVmcN4FubW0PflYHfog8UuPkM2jyMDuyvpT7HZqm2OR3JC1Rw1plKqLjUDmtoT_93Xl5bJknyNq0XDyxYY7okfNHmNgngfKe0VtR9MLVIY1DoJcfeVPyWNabxnCR5R5eF2sCM4TIqKqM0QVROmzAk7FAVJJ9wantPmYSpgj2bOMl7XlYHSjKdcQrvI77tX_1IYql2p6ip1974HwP26i0jC-necPttLAb80H3ou1yHs2DHk5ZTx_XjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، با اشاره به کابل‌های فیبر نوری عبوری از تنگه هرمز و تهدید به اختلال در اقتصاد دیجیتال جهان در صورت آسیب به این کابل‌ها، خواهان اخذ هزینه از شرکت‌های خارجی و الزام غول‌های فناوری نظیر متا، آمازون و مایکروسافت به فعالیت تحت قوانین جمهوری اسلامی شد.
تسنیم نوشت: «کابل‌های تار نوری زیردریایی عبوری از تنگه هرمز روزانه حامل بیش از ۱۰ تریلیون دلار آمریکا تراکنش مالی (شامل پیام‌های سوئیفت، معاملات بورس و تبادلات ارزی) هستند.»
رسانه وابسته به سپاه در ادامه خواستار «اخذ هزینه مجوز اولیه و تمدید سالانه از شرکت‌های خارجی، الزام غول‌های فناوری (متا، آمازون، مایکروسافت) به فعالیت تحت قوانین جمهوری اسلامی و انحصار تعمیر و نگهداری کابل‌ها از سوی شرکت‌های ایرانی شد.»
فارس، دیگر وابسته به سپاه، نیز در گزارشی نوشت که ده‌ها کابل فیبر نوری زیردریایی که آسیا، اروپا و خاورمیانه را به هم متصل می‌کنند، از گذرگاه تنگه هرمز عبور می‌کنند و تهدید کرد که «هرگونه آسیب به این کابل‌ها می‌تواند اختلالات گسترده‌ای در اینترنت و اقتصاد دیجیتال کشورهای مختلف ایجاد کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75367" target="_blank">📅 23:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAwbBcoXqbXrVggvD4sOVM1qsgq3PD4_fjQ6CdhQW1vWSKbTx580TbBf_aWDBMYh8tBlMRQPsh9zOqRBPl-jw5_HG44BVKaqmUzhbH4C0DkQZ_6As46J40owxFPyu7lPgMAPfMfRDPxLhOkwsFo_8CgfaYF0mkHjm1-Ky2ivZm0vt2hpVZ7O-zpQ1LmRqheDa1iO1_DcDa27gg7NjacBHb5Kkni6SYFwpCzEFkkBz915W70oPTTJu7KWyh4BoT9c-Y9FMXd7D4dijo3fAd_D6rptUcPQsHeP_jOU1Our65VDqy8ft4MKJ62mcmuH6DaNovEDgQW0vijALVEG3ujWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، روز شنبه ۱۹ اردیبهشت، ساعتی بعد از برپایی رژهٔ «روز پیروزی» در مسکو، گفت که معتقد است جنگ اوکراین در حال اتمام است.
او بدون اشاره به جزئیات بیشتر دربارهٔ این جنگ به خبرنگاران گفت: «فکر می‌کنم این موضوع در حال پایان یافتن است.»
روزنامه فایننشال تایمز روز پنجشنبه گزارش داده بود که رهبران اتحادیه اروپا در حال آماده‌سازی برای مذاکرات احتمالی هستند. وقتی از پوتین پرسیده شد آیا حاضر است با اروپایی‌ها وارد گفت‌وگو شود، او گفت که گزینه ترجیحی‌اش گرهارد شرودر، صدراعظم پیشین آلمان، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75366" target="_blank">📅 23:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=ZbdwXytGyMZT_8OXO_stIh4zGLuY0U1_gcbGvdEuWtoB5o3GYF29g6h8WPG8r80sY3LlQ7LFruOUx-hhqxjLjDabzOUbfwBP02RrHVAG6t1bT8H8LrfUUwSjE8LFivCfiURl_-HUxeIEdNqLGAbwacKTrF0w7uaEgBPf9QlPmvMlOWNPok-CroSDqObSdpFvlLVnpa2Bm5fL5NAGYBDeL2lTJ_fnj-QqgVErrLEM9PFXwEuvZ48q2sB4VVZpD3f0gYZ36uv3uc4YhLGrwP_42GKj9mhAY0tzOwh0QxwC545OANq6gZ_MBoxLuXAke2c89_7NH97V9_Lgoo2HCdKEmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6d6c074f6.mp4?token=ZbdwXytGyMZT_8OXO_stIh4zGLuY0U1_gcbGvdEuWtoB5o3GYF29g6h8WPG8r80sY3LlQ7LFruOUx-hhqxjLjDabzOUbfwBP02RrHVAG6t1bT8H8LrfUUwSjE8LFivCfiURl_-HUxeIEdNqLGAbwacKTrF0w7uaEgBPf9QlPmvMlOWNPok-CroSDqObSdpFvlLVnpa2Bm5fL5NAGYBDeL2lTJ_fnj-QqgVErrLEM9PFXwEuvZ48q2sB4VVZpD3f0gYZ36uv3uc4YhLGrwP_42GKj9mhAY0tzOwh0QxwC545OANq6gZ_MBoxLuXAke2c89_7NH97V9_Lgoo2HCdKEmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از تجمعات شبانه طرفداران جمهوری اسلامی منتشر شده که در آن فرد خواننده می‌گوید زنان «کم حجابی» که در تجمع طرفداری از حکومت شرکت می‌کنند «نور چشم» آن‌ها هستند و ظاهر افراد ملاک نیست.
نظام جمهوری اسلامی پیش از این زنان بدون حجاب اجباری را بازداشت کرده و طی لایحه‌ای به نام «حجاب و عفاف» قصد ابلاغ جریمه‌های و محرومیت‌های سنگین علیه آنان را داشت.
با این حال، در هفته‌های گذشته حکومت سعی کرده با انتشار ویدیوها و مصاحبه‌هایی از تعدادی زن بی‌حجاب در تجمعات حکومتی، پایگاه اجتماعی خود را گسترده نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75365" target="_blank">📅 21:01 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g71Tz1Yr6C39NqorKxxE16hKR7_5b0PTLWwQ9RCc04dAc57cUQU2JLCd56JN5N_dkjfv5zQ64YbH2HwqHI-aFp95yRACPPeMOtRgjjb5HcdFnCqAFhL8Z9NT5Np5SF2bChaDBZFBPcG5jSLkZujW4uoyJI7JALIasy_3vXRBmuQksxEA9U-xL7LmpBm0obNYelezozTuX-xxXNksAs7GSrfA1QKNUGXYt6QPm8jbU6YQWp1SmhB7VRVV4nN21p7mYiY6l9cIyWCGXl0-ZFgQRBtywaLRbgXZlMuSkLjcCh1A_Uo2JDU33XhsWHjwldTJH4_w9W18ZDXhCbg6Sn0Cyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های لبنانی روز شنبه اعلام کردند که در حملات هوایی اسرائیل به جنوب لبنان، هشت نفر کشته شده‌اند. همچنین بزرگراهی در جنوب بیروت هدف حمله هوایی قرار گرفت.
این حملات تازه با وجود آتش‌بس سه‌هفته‌ای میان اسرائیل و حزب‌الله، گروه مورد حمایت [جمهوری اسلامی در] ایران، انجام شد؛ آتش‌بسی که تأثیر چندانی در توقف تبادل روزانه آتش، عمدتاً در جنوب لبنان، نداشته است.
حزب‌الله روز شنبه اعلام کرد که در واکنش به ادامه حملات، نیروهای اسرائیلی در شمال این کشور را با پهپاد هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/75364" target="_blank">📅 20:30 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOcnIH7ON0_XNJCaPZz7a_R8m762aWZGqqbY4XTRTIT6bUHAjmIZ1WT_OPtJjBTCBRKPRaD--5JM2WxQ5ZvBK8AsBOf3GwHKovbx99z6Q9vGuFYWQ02eiv3NSWMNXPyjThmKB6hW8PEVJ5xOQtG9kvLXE5_M3cdSxMU1ILZfFItbHo_SAsWLl68Xa5qbGfnTZe0z0iTRNvYUD218bQeBxGVKLhPj4cAit3nou2Ni6uFdIIqkwMdVcqXKJXe0F0yVfgDSj5Aog4TSsB-pIWZEk44eu-YM6aArQsNmDYUAwMuNddTgHgCqiaa-ThPFHN-hyZjB9Vpcgvti1WB-jCVSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا، سنتکام، روز ۱۹ اردیبهشت ۱۴۰۵ اعلام کرد محاصره دریایی آمریکا علیه جمهوری اسلامی همچنان به‌طور کامل اجرا می‌شود و نیروهای این فرماندهی تاکنون ۵۸ کشتی تجاری را تغییر مسیر داده و چهار شناور را از کار انداخته‌اند تا از ورود یا خروج آن‌ها به بنادر ایران جلوگیری شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75363" target="_blank">📅 19:40 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75358">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMxXMRVoCVu4jr24pgYK2G00eq4XMfvUTDeG99n2cQ0Fa1feacN2eKM32pIKNi-KtWmauhL5U2h_9z7iSZU_5YIusQTDcll8zokTzouYCY6QOurA2P85inPw_fQNK7NvJM6G83FHbr9mcs21i6NZ5dZU3ts4WxrJiwTju65644KmU4IDipLJPhhmq4B2zmduodpVoauRlHbHvgI-O3YsfZm6tmqsJY85lN9SPowFjYWbFgJZjizTnmHeKexGLo9V1IUcDvxvhjhOqbeTSuI_5TCzhCVaXeTLlbkIYifS3q49L6vsvrCRyZbfWkMj7ImPke8zsJ6nag8wsTsgjySOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JL5ibXLXyC3bUiC-7svNuGVlPrgR-4ppJecJZvkxJI5ksTovQqXKZp8eSjiLjUdfp3x81CJockQOpJPL81g9Pzb7UejQLnw5CPEl938LyTlmommntaaymfHrcWhpQYPkCtxIeg8HKW0hUUhTDTjHwjOpA2pE-Zp2_u9g1U-NmsfUxjVMytGWhmeoUJPqY1sf77b0F_jP0RlI295cWKegpVuRVuvP1HPZazZpoydXi990QilTbGPz2tI6iAl3gbEE8kRV2mOknOlmy6zpxxo7OI0yuXXpiZ-sOn2XpchJAcXEfIiKhlTjHxAkLMAC-C0rKj7M5gPxiMFvt4znW1HAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EwCpdLaZffPspObONVVrcoqk_873nmXjO2y9k82Qs3DIg_3JafZ4XJ1PJ_CfdQBp1dFFnQAQaw5fEyc0tlCcaI_BGZWK8y40lqEtUXO50XZPFq_Y7qivgYFnBtfkZ09UTv4iLnImFzvk4EmQRYidVHW1-dbtrfOHub-46XrYwHRQI41OwMF5ad7mZLvEDXcm7rFmgixrqxAX-DvwQBakrwntycP2pcMnn7r1lcGrvqMSheQWtPVeBiPNuF40ZzaATHfNAXt29ngZift9e3qgAKR5K35G9jzcQ1i-kWVzLdcWf_KMOWwh-iggHvlG7G-yPCQh5tfLI8NQXK2pzpEW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eRYlJWHRSZYM-D-97VMbhfywgLi3xQkRA14zNKmtCtwd5szPztSF3jK9OqgKniY8Oqt24L3iuEB6PIFbZXpoljUMeaSjteIpVF0AOuo_mUS3S9h1ociMN4mOvNih0Lx72tJdpbWzMrnBMARRAiW7DN3qYIeRlqKymXs4SyKYltR12sU4SvArClU2_K7xLFdjGBYGPVG35iZckDnnmItPwOSuCoozcBkHAyI2FWIXdT00DKcvDiM_UTrT5FVGHid_IzeJ9oVi-KMxitbf3D7sY8E3esS6_ajzDcv7H-5YNYi898qIaT6-aQl12FT_0QNPKcbWmNvE2sru2sy4RosAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U2UH5NmBwzXLvtiV77bjU3jemwFW46Ck0XYufFpjoLv7ZYNGMsoY8fmK1frAP9razPV6Qh5AWBm9Cb7aCdHgF0GRHPIFMDOlUorypzsijIoeQgOrhfkoC1xR1ZhLia7Bcn-PjXa-43rUaFchWHrgGS_y5d68yLGKsqmDOfshwcV8sqKYw52xs2k3vvLU7OZh_HLwv_ASY9Xpj0wss3cbfSlbRsThbucD_Qr6cRYKKBz3YVtDcwJ7KC7Zy_RCBvY_dJkLN-Pf9R3pXt50udtwkMqELOLjFfAg8ZtAUBWfcjc19Rc9Lub0R0AfuaJOqsuLOfjPXRjiqVrxMwPQPpeRPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذشت
‌ عبدالله امیدوار، یکی از دو برادر امیدوار که اولین نزدیک به ۷۰ سال پیش با موتورسیکلت دور جهان را گشتند، در سانتياگو، پايتخت شيلی درگذشت.
عبدالله،  برادر کوچکتر پس از پایان سفرشان به شيلی رفت و در آنجا ازدواج کرد و شرکت فیلم‌سازی در شيلی تاسيس کرد.
عبدالله۲۱ ساله و عیسی ۲۳ ساله،  در سال ۱۹۵۴</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75358" target="_blank">📅 18:51 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW2L-ipOOdww8MPmRwFyP8Idz7qR5TCZJt6pzCd10_G7wiGIm7tsIwnRKij1aud3HhW0am2dAfb2QZbWKCHZCqt-A7iIH8m6XjSat0fOMttabRm_ZNd0eilCyT5OphNXFh3x_XiTYvR8eHuYsNfUeJcmqEyg4DgnwbbO2ctOSLTyetMMKOvhsAVeIAHlbxm6tqU3hMGspxFk4n_PmLwXzbCi0YXajT0sq8AaQBoRdeyXdgWf34fhAtVexpCa0RcBLQVNtwbR5U8ccg3SY-lkcpizod_fZJJoHxLkxtTdHoeL9b_Z-kxuSBafpbx26mfLMIUR28vH2qRWPujiyxcEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع بریتانیا روز شنبه اعلام کرد که پیش از هرگونه مأموریت بین‌المللی برای کمک به حفاظت از کشتیرانی در تنگه هرمز، یک ناوشکن به خاورمیانه اعزام خواهد کرد.
سخنگوی این وزارتخانه به خبرگزاری فرانسه گفت: «استقرار پیشاپیش ناوشکن «اچ‌ام‌اس دراگون» بخشی از برنامه‌ریزی محتاطانه‌ای است که تضمین می‌کند بریتانیا به‌عنوان بخشی از یک ائتلاف چندملیتی به رهبری مشترک بریتانیا و فرانسه، در زمان مناسب آماده تأمین امنیت تنگه باشد.»
لندن و پاریس چند هفته پیش اعلام کردند که طرح‌های نظامی برای تأمین امنیت تنگه هرمز در حال شکل‌گیری است و در بازگرداندن جریان تجارت از طریق این گذرگاه حیاتی موفق خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75357" target="_blank">📅 18:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/axj9lc6vsx76U9kRmdUYfAPrV4Xz4eiZlL41J4vlXwtk-2JbcxZ8dTaCCCAkAn5LoB8r-JRh6hNS3P229Aqz0w84Dvf_LdlZKn9lJKkzdQL1_2RleVToTr6ijUE1OqGVo7nqJaMKlIgCWntJCg4VXSko0JzmdrcIjUd2qQRKjVFkGRlzqFQ_Kd3gm7LxgLsDEnMlEuPzYdG-wyiHhk7E3xr0gEhCvxJvaJDDmPPNXXRnDS-wZNB_RkMKsbxLPSfpqJjEn9JWSuAcDbn_4uk8e7aWQlct03Z3Si2trS1VnU4omXImBO8lM-w3Q0-pNaTVXynwOYsgxEuJAONUll5ptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LfkqBwNSMNZqYgH4Sm87Tqp0dJnoG9OUpNRmH6fpyYelEeq-qiraLVTKULCc_0CmTqvw0hXVt6GPpO3_h1m14hMDI_-G6sqaoEdm9fBGLumzzxS6Rkz7lvwAyaOudpJWRj-qtPSqNL1ErSILhyuzhxcxUOr4E8n7BkdjNoThG6RHQ5DnvNwCq1xo7anra7WsoVaM03Rub6bCBN1KCLaRe5I5h9TA5Bck8TiqZ8MaxcTK91uZRpo-rdFb9l5l_QzcZQdgTnjEOuPd2t0aZ7OVUOIMhPluunyGOsUysfbkIa6CiZ5PuHcfiF2OsXXpe2AbbSEhylkq85CoAw-HhwD58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UUFgjQL2P610Hwaft0dPeMteEK6Haa10aqq5e2nMmlGLgafGInjlYrlhTSp23xbYkmWTJUTRCqyYr94-aVhwx_1ZwQ836GqJXstgpqsCta62pRlG1Lkp31qmf7DfnPFbzmksueVv3Kak1oV2VnOip6BIJ-Q-aV2GeIw6o47dczxeFP0NDu72dii1S9HBEpRdNdLh37KHQ408V76H_winWGTF4YKRHVfrDICXYbQVxJXv9XJ9U-CsCeaHqrMejyYYkD82vbdFYcC3fiCKu4hKIrc5lXni939zsmhcBqP5r0N9jZ6AOjHp16aUVchHKrsOMGTeMaoYtx9aCOZsOnAMSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت کشور بحرین روز شنبه ۱۹ اردیبهشت اعلام کرد که ۴۱ نفر را که به گفته این وزارتخانه با سپاه پاسداران ایران مرتبط بوده‌اند، دستگیر کرده است.
خبرگزاری دولتی بحرین به نقل از این وزارتخانه گزارش داد که مقامات امنیتی گروهی مرتبط با سپاه پاسداران ایران را شناسایی کرده است و افزود که تحقیقات برای شناسایی و برخورد با هر فردی که در این تشکیلات فعالیت داشته ادامه دارد.
@
VahidHeadline
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس شورای اسلامی، روز شنبه ۱۹ اردیبهشت، با انتشار پیامی در شبکه اجتماعی ایکس کشورهای منطقه از جمله بحرین را تهدید کرد که در صورت همراهی با قطعنامه پیشنهادی آمریکا در شورای امنیت سازمان ملل، با «پیامدهای جدی» مواجه خواهد شد.
عزیزی بحرین را «کشور ذره‌بینی» خواند و نوشت: «به دولت‌هایی همچون کشور ذره‌بینی بحرین که در حال همراهی با قطعنامه آمریکایی هستند، درباره پیامدهای جدی این اقدام هشدار می‌دهیم. درهای تنگه هرمز را برای همیشه به روی خود نبندید!»
قطعنامه مذکور که با حمایت آمریکا و کشورهای حوزه خلیج فارس به شورای امنیت سازمان ملل ارائه شده، از ایران می‌خواهد که ضمن توقف حملات علیه شناورهایی که قصد عبور از تنگه هرمز را دارند، محل دقیق مین‌های کارگذاری شده را اعلام کند و از دریافت هرگونه عوارض عبور از شناورهای عبوری خودداری کند.
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای حمایت کامل ریاض را از اقداماتی اعلام کرد که پادشاهی بحرین برای مقابله با آنچه «اقدام‌های صادرشده از سوی ایران» خوانده، اتخاذ کرده است.
در این بیانیه آمده است این اقدام‌ها به گفته مقام‌های سعودی، امنیت ملی بحرین را تحت تاثیر قرار می‌دهد و با هدف بی‌ثبات کردن امنیت و ثبات این کشور انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/75354" target="_blank">📅 18:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JANyIDf2DuWtHvFt30mRapMmOrtc0qjp-UkFJ-ePiAWhEVNAG4qpXBfH7wGRLzFjuS4Ykmx21_PZyEGGrLdAvU32tGcnzcCEh_1-uBf5b_dABbCkkZbhztTKiNekozY8DedJvSRMKU-U2J5jtBlyNrIXobH3is1pEZW0lGYCo7q35w3zm5vxw-QiGbA5oQQeQnG9Rn6wxSACz8g_A9WqzY9H5Fb0cp3uhj_5Pu1xCd973tTtflNSVCnmoZYg7OP99ObgYT60y1algn_koPbA0I7d2ax7aJuP0Opsvl8Uj9elbor-okUPEIcfoGAqOvfeI8kkVDY-apkSRGK7S1JRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با شرایط پرتنش منطقه، رویداد «در امارات بسازید» در ابوظبی برگزار شد و شرکت‌های تجاری نزدیک به ۴۶ میلیارد دلار در امارات سرمایه‌گذاری کردند.
بر اساس اعلام اوپک، این رقم بیش از مجموع درآمد نفتی جمهوری اسلامی، ۴۵.۳ میلیارد دلار، در سال ۲۰۲۵ میلادی است.
النهار گزارش کرد این سرمایه‌گذاری شامل صنایع دفاعی و تکنولوژیک، دارویی، شیمیایی و انرژی است. این رویداد چهارروزه حتی در شرایط جنگی تعطیل نشد و توانست جایگاه امارات را به عنوان یک قطب صنعتی در منطقه تقویت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/75353" target="_blank">📅 18:30 · 19 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
