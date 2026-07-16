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
<img src="https://cdn1.telesco.pe/file/n8b8TT_YOR-ZDbYMWzPzvLY2JsRMy-M97cP4GTpdbqM1nYeBj9ZTn_53qFpJUqyk7i1jaQXHHGcMWo39Wp_9nEvBWbX3GHPk9lLkxqcqvZY8Jysd_wVjYc0TG6skDpIJrTBVSjjnUseGTOoJ1j8_i_D_2Ydh4AZQ5j63DsZTXQmC_07SJKZK0F8HXz60wexbcLmetHbCuVchyHhcT6dat23MgNVePe6FVXF74tJqVUPTxNQCTmiMGSD7hBpix86HqhsW-habmxAqUYbPN7eA7-GKpeTV2Ldqhu-HRPZrrJoImpDeINZfy9aPioeQ-rM3iJ0dYJCcoLF9da6EJrbVrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.38M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 19:40:15</div>
<hr>

<div class="tg-post" id="msg-77153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9KuofcqRbNEgfTbYy8Y-jAoofG8yMSs0H9dXTZSSnSH4jsE6NAtDRtcbgQ2Oywc0uI5fnaCmhwvEmz2EbxxB-AdpyzAlhEmIWPYqsikGkk1doYoVcIXxD5f2nbsGSGhuv3dKJ_K8GBqbAbXQuSf_D0wvDQ107xD_dpARdn8vSNW3TIT8S0vTwbE7zhCEdAm2zOOj21tJqd6t1ndqVGeze5EQZ91fOa8WeS4lVXcj57hIAS-sqHftYxAtetjLprIES4PH5dQXVuqbN5Ds9xJ0R75kaVT_S8QNIHU7epjUyXiFyCcQa2HojeaNZ1mI2mrxzxRtaZqxDyI875pMYUW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس:
🔹
استانداری هرمزگان: در ساعت ۱۸:۱۰ نقطاتی در حوالی قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.
بندرعباس:
استانداری هرمزگان: در ساعت ۱۸:۲۰ و ۱۸:۴۰ نقاطی در حوالی بندر عباس مورد اصابت موشک‌های دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/VahidOnline/77153" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77149">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RRXBnJ0O1oLMqfS99VSClIqC3d5N0nsXkyE6c60_eF4GpCmtDWy0Wnbw6ktdeIOGqfjjqI8UyqP7WE8MfISBCAcSrA5mqyajHKDCg4tnnqCo9_5CPPodCYWR4uV1W0vcTpmJpKnqmBiRcQSLU0EcNopzPlVkh-uw-kmmGUqXwTr2q7jI-wEd_TUR14vVV9G2Z22hUB6FHhy9Zqb2oRwkyYCOeiB9nEgvtl0g4XqfJ3Jvc9LX1E84h5yhSuU2hEW5yX9-0DHYNpsNyKZMHzv7jZclHi6qtSFzHfrZmU7Ph6ffi-jO6dVmGfTFEXNWQk7mrfbamh_YsLwVH5WVnZVUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QG-tr3XYSUcuuSum9sodNJieXvkNweINGJTA2OsrdPDxyijf7qbH_5IDbynLwg95WiCCxUX6Vyg3xFZVYorAP1BUhCG1yr2Mppw5WRUaL78cf8xpTtBOrrx9BSTWI_3nM-0mZwK5G7FoTSyp5vOVSbQg4lKNMsdXxxkMUFOviafkPgfqAkGwiQ6_-NfZosMI4_VZ1KaK8BfWK-DrRQ4M3KG_n8HKPUDT8k-WDIdGUFbNXMP58j1RgWRx4zjZDyOq6djodvEbpf7v5tqJaSPdsB2VT8jyUWIpNuKEg7Tm1_0M0PfyM229_j1FkDEP46RFJEt4mABgIUILXNi3ArmkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/evG2xpkqioLHTGG5tnglZLfFJ5leeGQOvvy1ZX-2A6X0kwtdXaChDDKhqibQpSyyVHnOy5DLcK99xaQCno9eCGzKkabEmlSEXHC2EsvHYfJW3tZaH6U8rLcF5qmPV-2dGGP7knI9rqVr_oyJpP_7DPlb26HPkEL3jKdZzwM5qo8Xzz0rRDL2wJoxWq-faI4XwruUf55qNwIx_f7olmrDFVKVddiUnub--Dy3OLZEyPFuLMLrE52zc5FWN6q1s0cMx1hfYIVsSyesEimI8-sckO40vpyVD18_2DvNAuIHuTblgubDMDbmBsbsxvmV_h78Yue-er--IKwjIQbCOObFAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=R63Rw3s8UB1ox2FfljpZFJTwGMrW4Zr6ShY3Wb-y14cfiFGNPJqptpvbuu1jKaYlxa-wt-cW_fIHnFSxeS34bbG3zN84dEIkvTKwJKTcktLbbi4_cByTsr35ZXGOlgCUFDXvl-KujIR3eJJOvq-71mpK8AvrtaJWPyxGwJPyvwMbgsGGUD3q_uByoZvg87KS1Bh1oxWbZSd09nENhmIo7YyXznBaqGrl1TXfp_xhl44snmBGIHSzq73x22DvuOrEysrPTLqnN6SBMx1hQyivoLhrd9ga_lK9u-0diMbhcLbJYnODUQ3lNo9spfVxy0DqTMwq3fe-CG6F-P83cC0AxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/96d56893a8.mp4?token=R63Rw3s8UB1ox2FfljpZFJTwGMrW4Zr6ShY3Wb-y14cfiFGNPJqptpvbuu1jKaYlxa-wt-cW_fIHnFSxeS34bbG3zN84dEIkvTKwJKTcktLbbi4_cByTsr35ZXGOlgCUFDXvl-KujIR3eJJOvq-71mpK8AvrtaJWPyxGwJPyvwMbgsGGUD3q_uByoZvg87KS1Bh1oxWbZSd09nENhmIo7YyXznBaqGrl1TXfp_xhl44snmBGIHSzq73x22DvuOrEysrPTLqnN6SBMx1hQyivoLhrd9ga_lK9u-0diMbhcLbJYnODUQ3lNo9spfVxy0DqTMwq3fe-CG6F-P83cC0AxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرستنده تصاویر: پلیس گفت اتوبوس خراب شد پیاده شد تعمیر کنه خلاص بود از ایستگاه پله سوم تا پله اول رو رفت.
آتش‌نشانی: یک اتوبوس متوقف‌شده مقابل پارک ساعی با ۵موتورسیکلت و ۲خودروی سواری برخوردکرد.
اتوبوسرانی: بدون مسافر بود و پس از عملیات امدادی و رفع نقص فنی درحال جابه‌جایی بود.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/VahidOnline/77149" target="_blank">📅 19:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77148">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=LW_7YHIzcFqJvY-ykP1ug2DYI1fKoDVdI9A5rV5oOugQtgFVfHxA38-zC5mOWWSWTYVD_kV3-jspFhUyaiv6_bqxyoivGy4I8-_ZEB9ZnTp3EludqLKAtOGYz4nd8sEJQNRsLfM-XaEma4N_-3CYAyV0HD5KespqXSJ2_0dp5diqro88puMkxwR3_GAKH7HGrthrLt30xAL4bGBZi8ZPpNVwWoIZgHCdyV4i_bIlUOEuOL601QQ-aKaouECXOl1GPUS9XeymqneEjarO1R682Iatmync1vTfHGUV51vaf9qr7i62HoNOc5u-5pB-CCnMXQ3px07HmgQJyHTgpPS0Uz4EeG9BB8XZeno9JukgFdezkdyHO82QNqTET1M6qZwGSrZv2ey2J9cxjqkop1jv5-gpHwa9WCPYLmFRSJg8-V0zkf_nBaG9Flrqtj-uk3ibZ6nxeFI596IgdgXKhPLJZHdvTFBKItQ9OWvD_ZQgRcuDLc0871end491cYTeDiCnk95IengSvhFMTwlJfVSxCpHr_d0KeFA9CMicQC7pdQpK3eE_hFqH6-ox4flQqDz_D0r2Laxde6hTTAYE9cncpns1ma102RfnQXbe688xTr5eJzOLoCvn8M1QvjgSmQjuRmgzTZ_NmmryLnYZOHe3jpQfhQ_lGbdpBggEIy_o3UU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e1540b68c.mp4?token=LW_7YHIzcFqJvY-ykP1ug2DYI1fKoDVdI9A5rV5oOugQtgFVfHxA38-zC5mOWWSWTYVD_kV3-jspFhUyaiv6_bqxyoivGy4I8-_ZEB9ZnTp3EludqLKAtOGYz4nd8sEJQNRsLfM-XaEma4N_-3CYAyV0HD5KespqXSJ2_0dp5diqro88puMkxwR3_GAKH7HGrthrLt30xAL4bGBZi8ZPpNVwWoIZgHCdyV4i_bIlUOEuOL601QQ-aKaouECXOl1GPUS9XeymqneEjarO1R682Iatmync1vTfHGUV51vaf9qr7i62HoNOc5u-5pB-CCnMXQ3px07HmgQJyHTgpPS0Uz4EeG9BB8XZeno9JukgFdezkdyHO82QNqTET1M6qZwGSrZv2ey2J9cxjqkop1jv5-gpHwa9WCPYLmFRSJg8-V0zkf_nBaG9Flrqtj-uk3ibZ6nxeFI596IgdgXKhPLJZHdvTFBKItQ9OWvD_ZQgRcuDLc0871end491cYTeDiCnk95IengSvhFMTwlJfVSxCpHr_d0KeFA9CMicQC7pdQpK3eE_hFqH6-ox4flQqDz_D0r2Laxde6hTTAYE9cncpns1ma102RfnQXbe688xTr5eJzOLoCvn8M1QvjgSmQjuRmgzTZ_NmmryLnYZOHe3jpQfhQ_lGbdpBggEIy_o3UU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
خون در ۲ ثانیه اول)
صدای ویدیو: "اتوبوس ترمز برید، هرچی موتوری بود رو زیر گرفت رفت. خیابون ولی‌عصر"
به خودروهای پلیس هم برخورد کرد.
Vahid
تهران، پنج‌شنبه ۲۵ تیر
via @
iliaen
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/77148" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77147">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=jAGf98qSn-yw0RPtRCnxPpHroqkH20dqqRjNBXsWyoqygiqmXDRU99lbcRQ1LzqDCnlq5ChXaJDfPiwDysg9Ihp2w_ocejOlogXRJyOwhmSPWeDdDj9E8SxMBQYeeEfQS8QtMTniaCOQWFBMpXSrP8K8M54xKEgi75vd3g8qqWikzDt4lgjBLPtlp46vdK0HL1cKIf8NdS1T5z40E1XM64gERxxNwnOnYH9JJ6I3U7RgcJ4gSErv5sjD8SF5f0mEeyylsSQvsJSD038T1AfXmZAXhWpoFkVNkqzq8ajYqKy6EwK0_S_PRwEa2j8q0-7D8i1PSQzxe7zV3jB7kMJdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71f1bffd36.mp4?token=jAGf98qSn-yw0RPtRCnxPpHroqkH20dqqRjNBXsWyoqygiqmXDRU99lbcRQ1LzqDCnlq5ChXaJDfPiwDysg9Ihp2w_ocejOlogXRJyOwhmSPWeDdDj9E8SxMBQYeeEfQS8QtMTniaCOQWFBMpXSrP8K8M54xKEgi75vd3g8qqWikzDt4lgjBLPtlp46vdK0HL1cKIf8NdS1T5z40E1XM64gERxxNwnOnYH9JJ6I3U7RgcJ4gSErv5sjD8SF5f0mEeyylsSQvsJSD038T1AfXmZAXhWpoFkVNkqzq8ajYqKy6EwK0_S_PRwEa2j8q0-7D8i1PSQzxe7zV3jB7kMJdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/77147" target="_blank">📅 18:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77146">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZH9kab-8OOudL843QQodBBrykpsQujcgSRLMXsC-sdkaJhOhMNLbQ2QZRdHkwwnAa49NC6SSFo66O4cmVdARuSanEHymCxPjC8rVRq_KdeFcjHjpW_6xYjQWCMNx4RITC-ztG5Mrnui3oRMS93l5MBaX-WiNZ97kfa_PVDlWSX4ajSfF3DE3K1ic8LZGZvaVfEJdzdBCiaDd_VxC3zhPWSaYJBRrIEifZ9Dtc9IKrZdU4p9bmGyWTOW_wzNuzUPZOoRyhQofNenBsUTFRWgMiUFmrLq3dWmsn7TQTr3hDKnZ9mioAnpkont7AvHKYJV5cSaakXEsk8iEhiQFRrZrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام استانداری سمنان:‌ در حملات بامداد پنج‌شنبه فرودگاه سمنان نیز هدف حمله هوایی قرار گرفته است.
محمود قدرتی، مدیرکل امنیتی و انتظامی استانداری سمنان، ادعا کرده که در این حمله یک سوله جانبی در محوطه فرودگاه هدف اصابت موشک قرار گرفت و بخشی از شیشه‌های ساختمان اصلی ترمینال نیز آسیب دید.
به گفته او، این حمله در ساعات اولیه بامداد رخ داد و تلفات جانی نداشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/77146" target="_blank">📅 18:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77145">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vToNloZ3_74tjYethKfqoT_BrFPqNdRBaC7NbRtDb43brKo0ZeKZWMwOdyYo6Nir0s4aU_8TykTGQ-TEh2ScmYjjRXNsvB4vNGo-1yXPcxS7Df8qf2KMpjQXxgQfL6wcs8u2d2nUnR8he1j0l3i4o00GFKfreezJhxE34bz-1FqORGd9vFqsq9jM9jjErVkoE9D0_GIDW_Gg2djSgZt43d2ZYnUUiE24ZyGRT2zmxkvvnP5XLOsrqtU33iidyHGoD--bxKsW49-Qde9KWSlCCC9lPp6kCxyBgYicoGsQ9Ac1lNnfTknVLymZwDFxx2sf3H6uonjLN2j4CzkhQ_NgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امنیتی به خبرگزاری فرانسه گفت که روز پنج‌شنبه ۲۵ تیرماه پهپادی به یک کشتی «حامل خودروهای آمریکایی» در نزدیکی یک ترمینال نفتی برخورد کرد. گزارش شده این کشتی از امارات متحده عربی آمده بود.
همزمان چهار منبع نفتی و امنیتی عراق به خبرگزاری رویترز گفتند که روز پنج‌شنبه بارگیری نفت خام در تمام پایانه‌های عراق پس از برخورد یک پهپاد با یک نفتکش در پایانه بصره متوقف شد.
در واکنش به این گزارش‌، سخنگوی وزارت نفت عراق با اعلام این‌که بارگیری نفت خام در پایانه‌های جنوبی عراق همچنان ادامه دارد گفت که در حال بررسی گزارش‌های مربوط به سقوط یک «شیء» نامشخص بر روی یک نفتکش هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77145" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77144">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJNAlO123lg9e9VVIrAD0U0V_Un-eCgbObdad-zIQ2JnyvgC87l6WTfhxnt3ROpBSCluSTQ2aGLUSt1AVqDsaRix83e5uNkLYSkCUy8x28beyyiPrZPKMJ0hYylWfFXBT9ctyv1VFD7PGdQjuWeB-zxHQGtGLvBb7ledkEM2comHsPWYcq9nc5bESfznsUXPjZDfl61TeZbJqAUghg1lk_cadK0a7cd-kt_nM4ndHUKqa3nOEu6NCrS3X8RyOuvXPnsnJammhUTdl1MU57FA9z93CG7l-MIeeoxPtZd_USxPK62uHax8UdjalxhEZSbS9HS9go8Dhix284u9RQK5sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی، وزیر خارجه لبنان، می‌گوید تصمیم برای پایان‌دادن به نقش نظامی حزب‌الله در این کشور یک تصمیم حاکمیتی و مستقل لبنان بوده و پیش از توافق اصولی اخیر با اسرائیل اتخاذ شده است.
آقای رجی روز پنجنشبه ۲۵ تیر گفت که این تصمیم زمینه را برای توافقی فراهم کرد که ماه گذشته با میانجی‌گری آمریکا میان لبنان و اسرائیل حاصل شد.
او با تأکید بر این‌که لبنان «تصمیم خود را گرفته است»، گفت دیگر بازگشتی به «دوگانگی حاکمیت» وجود نخواهد داشت و جایی برای سلاح خارج از چارچوب مشروعیت دولت یا تصمیم‌گیری خارج از نهادهای رسمی کشور نیست.
رجی همچنین گفت استقرار ارتش لبنان در سراسر خاک این کشور، موضوعی جدایی‌ناپذیر از خروج کامل نیروهای اسرائیلی از همهٔ مناطق اشغالی لبنان است.
حزب‌الله که تحت حمایت جمهوری اسلامی ایران است، از سوی آمریکا یک سازمان تروریستی شناخته شده اما اتحادیه اروپا تنها شاخهٔ نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/77144" target="_blank">📅 16:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77143">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWiTQ1DPxl2M7R5FSbrIdzWBlWDkHt8XU2I7V7gBSOasHNnj_pISWX3VC1v-1iCL_aONJ-OiXQdUpku2p4nKH6Gb_AEfSc6_2BqhvMcGW06c5YN8R6CN7Ju4lPapxhA2kW3o_5fbgLnbj8N6-YC8hdVbxabEJDh7RLKcP9_aIjlx66LAcKoEHXh0lGF1skywT5knbhm5spsKExPDur-QzUCQIFN7ehTdgAbUk7eOZB3b8wJIg7qaYWma5QkYLClosLHFY5BmTzCmq_t4LxNaMh-T3xiO__ORC8RmjZRdTl0qZcteM0HQOrQyF9wDxSTvqWVZuF-X3gAU8L9rg-6B0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت جورنال به‌نقل از چند مقام آمریکایی گزارش داد که دونالد ترامپ پس از چند جلسهٔ توجیهی با دستیاران ارشد خود، به گسترش عملیات نظامی ایالات متحده در ایران متمایل شده است.
به‌گفتۀ این مقام‌ها که نام‌شان اعلام نشده، گزینه‌های مطرح‌شده شامل افزایش حملات هوایی، اعزام نیروهای زمینی برای تصرف جزایر ایرانی در نزدیکی تنگه هرمز و بمباران یک تأسیسات هسته‌ای مستحکم و مخفی است.
به‌نوشتۀ این روزنامه، دونالد ترامپ عصر سه‌شنبه به وقت آمریکا میزبان جلسه‌ای در اتاق وضعیت کاخ سفید بود تا در مورد تصرف احتمالی جزیرهٔ خارگ و سایر مناطق در امتداد تنگهٔ هرمز با استفاده از نیروهای آمریکایی و همچنین بمباران احتمالی یک مجتمع تونل در کوه کلنگ گزلا که به پیکاکس یا کوه کلنگ معروف است، بحث کند.
کوه کلنگ گزلا محل یک تأسیسات هسته‌ای عمیق و مخفی ایران نزدیک نطنز است که تاکنون هدف حملات آمریکا قرار نگرفته است. وال‌استریت جورنال می‌گوید گسترش حملات هوایی علیه اهداف بیشتر در ایران، از جمله نیروگاه‌ها، نیز همچنان محتمل است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/77143" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77142">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=WHrEAwTTQoexbVOe9_Em4yiqS2XNJVaMSuJldmpeodEUUPfyEOh8LfVkvEnT-Sd2-Th54XkhqM_QB6-JTmsewegNVvQxHckXKZH4UGAONdZh5rWKfKU-gCKceWf56u0sjEhVNjBefdY5l1Lw0wYCi04082FIfnErvA2Djhz3TwWoXV55PzmJVB3g0d4LgulHyHLVqPISHTVS-CxgMpKVCT2dVFKJ7bWl-cpAvk92b2Wuqj35roeHxObxznjKfFOhbL5ODCAO-WOFIy7kH12d5dOd_lmzIJKJTXaB5f9bQRAHzUBXizeL6RdfYzCUZbKYgMAXHqLaXZtmhCJBQo89TA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81194af4f8.mp4?token=WHrEAwTTQoexbVOe9_Em4yiqS2XNJVaMSuJldmpeodEUUPfyEOh8LfVkvEnT-Sd2-Th54XkhqM_QB6-JTmsewegNVvQxHckXKZH4UGAONdZh5rWKfKU-gCKceWf56u0sjEhVNjBefdY5l1Lw0wYCi04082FIfnErvA2Djhz3TwWoXV55PzmJVB3g0d4LgulHyHLVqPISHTVS-CxgMpKVCT2dVFKJ7bWl-cpAvk92b2Wuqj35roeHxObxznjKfFOhbL5ODCAO-WOFIy7kH12d5dOd_lmzIJKJTXaB5f9bQRAHzUBXizeL6RdfYzCUZbKYgMAXHqLaXZtmhCJBQo89TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در پاسخ به پرسشی درباره تهدیدهای مطرح‌شده از سوی ایران علیه جانش، گفت که به این موضوع «اصلا فکر نمی‌کند».
او در گفتگو با فاکس بیزینس تاکید کرد: «اگر به این مسائل فکر کنم، دیگر نمی‌توانم مؤثر باشم.»
ترامپ افزود این کار را دیگران انجام می دهند و به نظرم در این زمینه عملکرد خوبی دارند و تاکید کرد خودش به این موضوع اصلا فکر نمی‌کند.
@
VahidOOnLine
او همچنین تاکید کرد که می‌تواند سپاه پاسداران را به همان شیوه‌ای از بین ببرد که در دوره نخست ریاست‌جمهوری خود داعش را در عراق و سوریه شکست داد.
ترامپ گفت: «ما در وضعیت خوبی خواهیم بود. آن‌ها تضعیف شده‌اند. تسلیحاتشان ۹۱ درصد کاهش یافته است. توان پهپادی آن‌ها به‌شدت کاهش یافته است. هنوز مقداری دارند، اما زیاد نیست. ظرفیت تولیدشان کاهش یافته است. پرتابگرهای راکتی و پرتابگرهای موشکی آن‌ها به‌شدت کاهش یافته‌اند. موشک‌هایشان هم به‌شدت کاهش یافته‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77142" target="_blank">📅 09:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77141">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیم ساعت از
سه ساعت
گفت‌وگوی جی‌دی ونس با جو روگن، بخش مرتبط با ایران
جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با جو روگن از آنچه «جنگ‌طلبان» در آمریکا و دیگر کشورها خواند، انتقاد کرد و گفت این افراد با صرف هزینه‌های گسترده تلاش می‌کنند مذاکرات دولت دونالد ترامپ با جمهوری اسلامی را به شکست بکشانند و افکار عمومی آمریکا را تغییر دهند.
ونس با دفاع از رویکرد دولت ترامپ، تاکید کرد دیپلماسی برای حل بحران حمله‌ها به کشتی‌رانی در تنگه هرمز ضروری است و گفت در کنار اقدامات نظامی، گفت‌وگو تنها راه رسیدگی به این بحران است.
@
VahidOOnLine
بخش پرواکنش‌تر:
... من دو چیز را از میان سطرها می‌خوانم. فکر می‌کنم بعضی از آن‌ها می‌خواهند حکومت ایران به‌طور کامل تغییر کند؛ روحانیان سرنگون شوند و فردی بسیار دوستانه‌تر جایگزینشان شود.
ببین، تجربهٔ ما از انجام چنین کاری چیست؟ خوب نبوده. خوب نبوده. خوب نبوده.
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، تصمیم با خودشان است؛ اما ما ۱۵۰ هزار نیروی زمینی نمی‌فرستیم تا تغییر یک حکومت را رقم بزنیم، مگر اینکه مردم داخل کشور خودشان خواهان چنین نتیجه‌ای باشند.
در هر صورت قرار نیست نیرو بفرستیم؛ اما پیشنهاد اعزام نیرو یعنی عملاً می‌گویی ارتش آمریکا باید کار مردم ایران را برایشان انجام دهد. ما دیگر در این کار نیستیم. واقعاً نیستیم.
نتیجهٔ دومی که فکر می‌کنم بعضی‌ها خواهانش هستند ــ چه خودشان آگاه باشند چه نه ــ چیزی است که من «نتیجهٔ لیبی» می‌نامم.
اگر به نتیجهٔ نهایی سیاست ما در لیبی پس از کشته‌شدن قذافی به دست دولت اوباما نگاه کنی ــ باز هم تصمیمی بسیار احمقانه ــ چه اتفاقی افتاد؟ لیبی عملاً به کشوری شکست‌خورده تبدیل شد. بحران پناه‌جویان به وجود آمد. مردم به اروپا سرازیر شدند، به بخش‌های دیگر آسیا و آفریقا رفتند. خشونت و تروریسم زیادی از دل آن بیرون آمد.
فکر می‌کنم افرادی هستند که می‌خواهند همین نتیجه در ایران رخ دهد. اما باز می‌پرسم: چه چیزی به سود ماست؟ چطور به سود ایالات متحده است که ۹۴ میلیون انسان درمانده به اروپا و ایالات متحده سرازیر شوند و زیرساخت‌های تروریستی که وقتی تروریست‌ها را در سراسر جهان پراکنده می‌کنی، می‌تواند شکل بگیرد؟
ما قبلاً این آزمایش را انجام داده‌ایم. سیاست کنونی ما و هدفی که دنبال می‌کنیم این است که تنگه را باز نگه داریم و جریان آزاد نفت و گاز را تضمین کنیم. بدیهی است که می‌خواهیم مانع داشتن برنامهٔ تسلیحات هسته‌ای توسط ایران شویم و از ابزارهای دیپلماسی و قدرت نظامی برای رسیدن به آن استفاده کنیم.
بیشتر متن زیرنویس ویدیوی بالا (تا سقف تعداد کاراکتر مجاز):
telegra.ph/Vance-07-16-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77141" target="_blank">📅 06:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77140">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/858e125a28.mp4?token=kt1YBLIeldKBoQVUd6hpL9FS6PX5IanwaWHEFuuxdCAcDRI2fvHuo8p2EiRjdNuj_PFZvgAG8Lh7_owz53jmIqX_D6Y0BzOn7NkhS2tAlSvwQFDSBfZCjIumED_d7FE2d7-An4vDK_Tf4YqEnVzp3_tWRZBE8B2Ase8lbKLDvMQxZ_Su12ko60A4cb3fb-EbY_6j1-5qOrmxaPOY8gExzMfarGP57Jgn1sziSX2XUiGWE7FYjFnQJVdgSGnhli8lKs8bYf1VUVCJcd22jV8LATzLTB1nFbUKAbzN0YeClshQeWLOMVwbPVQDrXEoo45-cNAjm2pK5pG3gOOjwUYJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/858e125a28.mp4?token=kt1YBLIeldKBoQVUd6hpL9FS6PX5IanwaWHEFuuxdCAcDRI2fvHuo8p2EiRjdNuj_PFZvgAG8Lh7_owz53jmIqX_D6Y0BzOn7NkhS2tAlSvwQFDSBfZCjIumED_d7FE2d7-An4vDK_Tf4YqEnVzp3_tWRZBE8B2Ase8lbKLDvMQxZ_Su12ko60A4cb3fb-EbY_6j1-5qOrmxaPOY8gExzMfarGP57Jgn1sziSX2XUiGWE7FYjFnQJVdgSGnhli8lKs8bYf1VUVCJcd22jV8LATzLTB1nFbUKAbzN0YeClshQeWLOMVwbPVQDrXEoo45-cNAjm2pK5pG3gOOjwUYJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام،‌ ترجمه ماشین:
تازه‌ترین موج حملات آمریکا علیه ایران پایان یافت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) موج حملات شامگاهی علیه ایران را ساعت ۹ شب به وقت شرق آمریکا [۴:۳۰ تهران] در ۱۵ ژوئیه پایان داد.
نیروهای آمریکایی مراکز فرماندهی، مواضع پدافند هوایی، توانمندی‌های موشکی و پهپادی و تأسیسات نظارت ساحلی ایران را مورد حمله قرار دادند تا توانایی ایران برای تهدید دریانوردان بی‌گناهِ خدمه کشتی‌های تجاری عبوری از تنگه هرمز را بیش از پیش تضعیف کنند. سنتکام برای حمله به مواضعی در چندین نقطه، از جمله بندرعباس، از مهمات هدایت‌شونده دقیق استفاده کرد.
پیش‌تر در صبح امروز، نیروهای آمریکایی طی یک موج حملات ۹۰دقیقه‌ای، مواضع دفاع ساحلی و موشک‌های کروز در جزیره تنب بزرگ را هدف قرار دادند.
ارتش ایالات متحده به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۱۵
🔸
رادار پیش‌هشدار سامانهء C-RAM در پایگاه علی السالم کویت و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا آماج حملات ترکیبی قرار گرفت‌
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم غیور و بپاخاسته ایران!
🔹
در پی تجاوزات شب گذشته دشمن به نقاطی از سواحل و شهرهای جنوبی کشور، فرزندان دلاور و قهرمان شما در نیروی دریایی و هوافضای سپاه، در موج هشتم عملیات نصر ۲ بارمز مبارک یا زینب کبری (س)، در یک عملیات ترکیبی با استفاده از توان موشکی و پهپادی خود، رادار پیش‌هشدار سامانهء C-RAM را در پایگاه علی السالم و نیز محل تجمع سربازان جنایت پیشه ارتش تروریستی آمریکا را آماج حملات خود قرار داده و درهم کوبیدند.
🔹
بار دیگر به مردم شریف کویت یادآوری می‌کنیم که این جنایات توسط آمریکا با استفاده از خاک شما علیه ایران مسلمان انجام می‌شود.
🔹
از شما برادران و خواهران مسلمان انتظار داریم کشورتان را از وجود متجاوزان پاک کنید و با عمل به وظیفه اسلامی، شرف و عزت تاریخی خود را حفظ نمایید.
سپاه درباره
صدای پاکدشت
: پدافند بود. هیچ اصابتی نبود
🔸
اطلاعیه سپاه حضرت سیدالشهدا علیه السلام استان تهران درباره صدای شنیده‌شده در پاکدشت؛
روابط عمومی سپاه حضرت سیدالشهدا علیه‌السلام استان تهران:
🔹
دقایقی پیش صدای انفجاری در محدوده شهرستان پاکدشت شنیده شد که بررسی‌های میدانی و نظامی نشان می‌دهد این صدا ناشی از عملکرد سامانه‌های پدافند هوایی در منطقه پارچین بوده است.
🔹
ضمن تکذیب قاطع ادعاهای برخی رسانه‌های معاند و جریان‌های سلطنت‌طلب در خصوص وقوع هرگونه اصابت، هیچ‌گونه حادثه یا اصابتی در منطقه صورت نپذیرفته و فعالیت‌های مذکور در راستای آمادگی و عملکرد پدافند هوایی بوده است.
🔹
از مردم عزیز ضمن حفظ آرامش، اخبار مربوط به این رویداد را تنها از طریق رسانه‌های رسمی دنبال کرده و از توجه به شایعات هدفمندِ رسانه‌های بیگانه که با هدف ایجاد التهاب و ناامنی روانی منتشر می‌شوند، خودداری کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77140" target="_blank">📅 04:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77139">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیام‌های دریافتی از تهران
احتمالا همگی درباره صدای پدافند:
صدای پدافند میاد ساعت ۳:۵۱ یوسف اباد تهران
تهران انفجار 3:50
پدافند تهرن داره کا میکنه ۳و۵۱
تهران یوسف اباد صدای پدافند
نارمک صدای پدافند ۳:۵۱
سلام وحید جان مرکز تهران صدای پدافند میاد الان شروع شد
.
تهران صدای پدافند
همین الان صدای پدافند شرق تهران
سلام خرم اباد صدای یدونه انفجار اومد
تهران مرکز شهر صدای پدافند
۳:۵۰
البته زیاد نبود، چندتا بود
وحید ساعت ۳:۵۱تهران نارمک صدای پدافند
داداش تهران سید خندان صدا پدافند ساعت ۳:۵۰
پدافند تهران میدون شهدا داره کار میکنه
صدای پدافند ساعت 3:51 مرکز تهران
تهران سهروردی صدای انفجار از دور تقریبا
صدایی شبیه پدافند از دور شنیده میشه، اختیاریه، ۳:۵۱
تهران عباس آباد پدافند ساعت ۳:۵۰
پاسداران تهران صدای پدافند
سلام همین الان پدافند سمت میدان امام حسین فعال شد
۳:۵۱ دقیقه
من ميرداماد تهران هستم
الان دارن ميزنن
٢ تا صداي بلند و بعدش ٥-٦ تا  كوچكتر
سلام.تهران پیروزی صدای پدافند ۳:۵۲
وحید سمت سهروردی صدا پدافند شنیدیم 3:52
سلام سمت سیدخندان همین الان صدای انفجار شنیده شد
سلام ! ساعت ۳:۵۱ دقیقه سمنان صدای جنگنده میاد
الان ساعت ۳:۵۱ صدای سه تا انفجار اومد تهران
سمت غرب صدا شنیدم
وحیدجان سلام الان ۳:۵۲ تهران محله نیروهوایی صدای پدافند
مرکز تهران. یه صدای انفجار اومد (دور بود) بعدش صدای پدافند ۳:۵۱
سلام وحید جان شرق تهران سمت فدک ۳:۵۲ صدای پدافند به گوش رسید نمیدونم کجاست
سهروردی سه تا صدای بلند متوالی اومد ولی منشأ رو نمیدونم و دور بود انگار
سلام وحید جان غرب تهران سمت فرودگاه صدا پدافند و جنگنده میاد
فعال شدن پدافند در تهران محله دبستان ساعت ۳:۵۰ بامداد
سلام ۳:۵۲ دقیقه سمت گیشا هم صدای پدافند میاد
من میدان سپاهم
صدای انفجار یا پدافند! من تشخیص نمیدم از دوره
ساعت ۳:۵۰
سلام‌وحید جان سمت امیر آباد شمالی صدا پدافند داره میاد
سلام وحید جان تهران شریعتی سمت میرداماد صدای پدافند اومد نزدیک نبود خیلی
سلام وحید جان ساعت ۳:۵۱ دقیقه میدان شهدا چهار پنج بار صدای پدافند اومد
صدا پدافند بود فکر کنم
تهران محدوده خیابون امام خمینی
ساعت ۳:۵۰
وحید سلام توانیریم، صدای پدافند ونک دو دقیقه پیش
سلام تهران الان ساعت 3:53 هم صدای پدافند میاد هم روی اسمون نورش معلومه
سلام وحیدجان سمت شرق پدافند زدن اما قبلش یه صدای بلندی اومد اما نمیدونم زدن یا نه چیزی دیده نمیشه
3:50صدای پدافند شرق تهران
سلام ، غرب تهران (پونک) صدای انفجارها پشت هم و خفیف از دور میاد
سلام وحید جان
شرق تهران الان انگاار صدای انفجار اومد . مطمئن نیستم چون خواب بودیم ولی شبیه صداهای اسفند ماه بود
ساعت ۳.۵۱ صدای پدافند تهران خ شریعتی
کوتاه بود
سلام وحید جان الان ساعت ۳.۵۴ صبح ۲۵ تیرماه صدای پدافند گیشا
تهران شوش پدافند ٣:٥٣
غرب تهران 3:51 چندتا انفجار پشت سرهم شنیدیم
الان باز شروع شد ساعت 3:56
همین الان ساعت ۳ و ۵۵ دقیقه دوباره صدا اومد سمت هفت تیر
۳:۵۶ دوباره صدای پدافتد یا شلیک سمت نارمک
۳.۵۶ امیراباد شمالی دومین بار پدافند
از اختیاریه، ۳:۵۶؛ چند تا صدا شنیده شد با صدای قبلی فرق داره که پدافند بود [پدافندها انواع متفاوتی هستند با صداهای متفاوت]
وحید ۳:۵۶ شرق تهران صدای پدافند - تو ۱۰ دقیقه گذشته دومین باره
تهران شمس آباد  نزدیک کلانتری مجیدیه همینطور صدای پدافند میاد
سلام مجیدیه شمالی صدای پشت سرهم پدافند میاد  حدود ۴ صبح
سلام وحید جان. مرکز تهران صدای پدافند مکرر اومد.
وحید جان ، ساعت ۳:۵۱ دقیقه بامداد اتوبان حقانی صدای پدافند بسیار کوتاه
داداش همین الان  ۳:۵۵ حدود ۱۰ بار صدا امد  ولی زیاد نزدیک نبود یوسف اباد
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77139" target="_blank">📅 03:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77138">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پیام‌های دریافتی:
خرم آباد صدای انفجار
سلام ساعت 3:48 صدای انفجار در خرم آباد
وحیدخان از بروجرد انگار موشک زدن صدای غرش سریع و شدید تو آسمون اومد
خرم آباد ۳.۴۷ صدای انفجار یهویی و نسبتا شدید
خررم آباد به شدت صدای انفجار اومد
کل ساختمونمون لرزید
سلام وحیدجان ۳:۴۷ خرم اباد صدا اومد
سلام وحید جان خرم اباد لرستان ساعت ۳ و ۴۷ دقیقه انفجار
🔄
دوباره زد خرم اباد رو ۳:۵۷
سلام وحید جان همین الان صدای افنجار اومد دوباره خرم اباد
سلام وحید جان بروجرد الان ی صدای مهیب امد. من هدفون داشتم درست متوجه نشدم بعدشم صدا موشک یا جنگنده امد
آقا وحید بروجرد صدای خیلی قوی صدای واقعا عجیب و قوی،واقعا نمی‌دونم انفجار بود یا دوباره شلیک بالستیک،صداش از رعد و برق بدتر بود
خرم آباد دوباره صداي انفجار
دومین انفجار در خرم آباد ساعت 3:57
بروجردو ۳:۵۵ زدن
انفجار خیلییی قوی
سلام وحید جان از بروجرد صدای شدید و یهویی اومد (ساعت ۳:۵۰ صبح)
طبق تجربه، صدای شلیک موشک بود
داداش الشتر لرستان دوبار صدا اومد معمولا از اینجا موشک پرتاب میکنن یبار 3 و 47 دقیقه یبارم حدودا 3و  56 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77138" target="_blank">📅 03:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77137">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تو ارومیه صدای انفجار اومد از سمت کوه های اطراف شهر
همین الان یه صدای انفجار با لرزش خارج از شهر اومد (ارومیه) بعدش با صدای بلند مثل صدای موشک یا جنگنده تو هوا
ارومیه صدای انفجار اومد دقایقی پیش با صدای جنگنده [احتمالا صدای موشکه]
خارج از شهر ارومیه نزدیک مرز صدای جنگنده میاد همین الان
سلام وحیدجان، دوباره از تبریز موشک زدن
سلام وحید. الان ۳:۴۶ از تبریز موشک زدن
۳:۴۶ دقیقه همین الان یه موشک از طرفای اسکو آذربایجان شرقی بلند شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77137" target="_blank">📅 03:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77136">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">استان تهران، صدای پدافند:
سلام وحید جان الان ساعت ۰۳:۲۷ صدا انفجار اومد سمت پاکدشت
اقا وحید همین الان پدافند پاکدشت کار کرد بدجور
صدای انفجار پاکدشت ۳:۲۵
۳:۳۰ سمت پاکدشت داره صدا میاد
سلام صدای انفجار و پدافند حدود دو سه دقیقه پیش داخل پاکدشت
پارچین و پاکدشت انفجار سنگین
خیلی صدا شدید بود
فکرکنم پارچینو زد
۳/۳۰ چندین انفجار در پارچین
سلام وحید
ساعت۳:۲۰ پاکدشت صدا پدافند اومد شدید
دوباره الان ساعت ۳:۳۰ داخل پاکدشت صدا انفجار میاد
دارن میزنن پارچین رووووو
صدای پدافند میاد
۸ بار صدا اومد
سلام وحید جان پدافند پارچین فعال شد همین الان و صداش پاکدشت شنیده شد
سلام دوتا ویکی الان3.31دقیقه.صداتا قرچک ورامین امد
البته اول چهارپنجتا انفجار شنیدم که احتمالا انفجار گلوله.های ضدهوایی بود
شریف اباد پشت پارچین صدا شدید پدافند میاد ۳:۱۸
ما صبح امتحان نهایی ریاضی داریم یه دوازدهمی همینجوری از استرس دارم میمیرم
و یه صدای انفجار اومد همین الان پاکدشت چند بار 3:30
صدای پدافند میاد آقا وحید شدید
🔄
همین الان پدافند رگباری سمت پاکدشت ۳:۴۳
همچنان ۳:۴۲ ضد هوایی شدیدا فعاله
ساعت ۳ و۴۳ دوباره فعالیت شدید پدافند توی پاکدشت
🔄
دوباره صدای پدافندا شدید تر شد
از سمت پارچینه
۳:۴۵ شدیدتر
دیگه همینجوری هست
هر موقع تموم شد میگم
😂
صدای جنگنده ساعت ۳ و ۴۶ دقیقه
بازم انفجار شدید خرم آباد ۳.۵۷
سلام وحید  دوباره خرم آباد زدن ساعت ۳:۵۷
خرم آباد بازم صدای انفجار اومد ساعت 3:56
انفجار مجدد خرم آباد خیلی شدید بود
تهران صدای انفجار سمت آزادی الان
وحید جان 3.48صدای شدید خرم آباد دو مرتبه به فاصله 10دقیقه کل ساختمون لرزید
لرستان. الشتر(سلسله)
صدا و لرزش شدید اومد نمیدونم اونا زدن یا ما موشک شلیک کردیم
3.50
دوباره 3.56 همون لرزش و صدا..
لرستان الشتر وحشتناک دارن میزنن
خرم اباد
سلام وحید جان ساعت حوالی 3:55 از بر‌وجرد موشک زدن صداش خیلی بلند بود
آپدیت: منابع حکومتی
فرماندار پاکدشت: صدای دقایقی پیش در شهرستان پاکدشت به علت فعالیت سامانۀ پدافند هوایی بوده است.
روابط‌عمومی سپاه سیدالشهدا(ع) دربارۀ صداهای شنیده شده در پاکدشت: این صداها صرفاً ناشی از عملکرد پدافند هوایی بوده و هیچ اتفاق یا اصابتی رخ نداده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77136" target="_blank">📅 03:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77135">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌‌های دریافتی تایید نشده:
۳:۱۵ سمت «شهرک صنعتی سمنان» یک تک صدای انفجار بزرگ اومد.
سمنان، دو موج خیلی شدید انفجار اومد
جوری که خونه لرزید
ولی منشاش نا مشخصه
همزمان با پخش اذان از مساجد هم بود وحید جان
سلام وحید جان 3:18 هست ساعت و صدای بلندی در شهر سمنان اومد
آپدیت: منابع حکومتی
مردم در بخش‌هایی از سمنان صدای انفجار شنیدند.
استان مرکزی:
خنداب دوتا انفجار
آقا وحید 3تا انفجار سنگین خنداب
آپدیت: منابع حکومتی
معاون استاندار مرکزی: یک منطقه خارج از محدوده شهر خنداب ۲ بار مورد حمله پرتابه‌های دشمن قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77135" target="_blank">📅 03:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77134">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLgo8YhOETKjRyM4fcK-d3p9aWlKK6WSNnmmP22ceIUsOODvay1MgKR9KxsUMzn_td7hj6zmQR8xb9eCtOPgtvi6vbqymu98ciSHrDETMKcx0CG-X5y5HNZXnK7vsygT4JshsO9XeZcYvoUenbMX6FsoWDhlEVqpZuamQFgPR9635cVC8gbQu0CpKCuwBC57AwAIQ0SOwIN0Dt7PmfXnH9JdqshlG_YG1aBvBoIy46ZX1jricGKP4qCLdpXfCP7BAZ58MsZ9Ycrgvxk8bqPttMUtxBlgVOJDC4vGRnIClzDT0E0BEc14CvHAsnce_a_IOlHxChFGfovfaEq17b_XCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران یک شهروند بازداشت‌شده آمریکایی را آزاد کرد
پست ترامپ، ترجمه ماشین:‌
ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴، در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود، به‌ناحق بازداشت شده بود، اجازه داده است کشور را ترک کند.
او اکنون به سلامت از ایران خارج شده و حالش خوب است.
ایالات متحده آمریکا از این حسن‌نیت ایران قدردانی می‌کند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
گویا اسمش "دنا کراری" است:
twitter
آپدیت:
جرد گسنر، وکیل حقوق بشری مستقر در واشنگتن، در بیانیه‌ای
گفت
«من خوشحالم و با هیجان اعلام می‌کنم که موکلم، شهروند آمریکایی دنا کراری، که از دسامبر ۲۰۲۴ به دلیل اتهامات بی‌اساس در ایران گرفتار شده بود، اکنون آزاد است.»
او افزود: «این اتفاق بدون تلاش‌های فوق‌العاده و پیگیرانه رئیس‌جمهوری [آمریکا،‌] دونالد ترامپ ممکن نبود. دنا اکنون در امنیت است و در حال بازگشت به ایالات متحده آمریکا است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77134" target="_blank">📅 02:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77133">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس الان ساعت ۱.۲۶ دو تا صدای انفجار
سلام
بندرعباس ۱:۲۷ پایگاه هوایی ۲ تا انفجار شدید
درود وحید جان
همین الان شرق بندرعباس پایگاه هوایی صدای دو تا انفجار اومد
سه تا انفجار بندرعباس
احتمالا یکیش پایگاه هوایی
سلام وحیدجان چند انفجار سنگین در مسن لرزش شدید برقم قطع شد نیم ساعت قبل
جزیره قشم
یکی دیگه الان خورد 1.29
🔄
فعالیت پدافند بندرعباس ساعت ۱.۵۱
لرزش پنجره و صدای پدافند شرق بندرعباس شنیده میشه
فعال شدن پدافند بندرعباس همین الان
درگیری پدافند هوایی تو بندرعباس نزدیک پایگاه هوایی
فعال شدن پدافند بندرعباس همین الان
پدافند توی محله [...] بندرعباس جاساز شده
بین خونه های مردم ، محله [...]
وحید جان اینو کامل بفرست عزیزم
🔄
صدای بسیار بسیار شدید بندرعباس
دیوار صوتی شکست
یه صدای وحشتناکی از آسمون اومد
۱و ۵۸ بندرعباس
همین الان مجددا ارزش و صدای وحشتناک، ۱و ۵۹
نمیدونم انفجار بود یا پدافند ۱:۵۸
صداش شدید بودسمت پایگاه هوایی
وحید جان صدای عجیب تو آسمون شرق شهر بندرعباس عین غرش ولی منبع نا معلوم
وحید سلام بندرعباس ۱:۵۷ ی صدای خیلس بلند طولانی اومد انگار ی چیزی بخورد کنه و تخریب بشه
🔄
انفجار شدید ۲:۲۱
شرق بندرعباس ۰۲:۲۰ زدن شدید
بندرعباس انفجار سنگین
بازم پایگاه هوایی بندرعباسو زدن
شدت انفجار خیلی بالا بود ساعت ۲.۲۰
الان ساعت ۲:۲۱ گلشهر جنوبی بندرعباس صدای انفجار بسیار شدید،مثل غرش
سلام بندرعباس ۲:۲۰ سمت فرودگاه صدای بسیار مهیب
سلام ۲:۲۰ انفجار مهیب بندرعباس
صدای انفجار شدید اومد بندر وحید ۲:۲۱
🔄
۳ ۴ تا انفجار دیگه ۲ و ۲۶
وحید ۲ انفجار سنگین همین الان پایگاه هوایی بندرعباس
سلام ۲:۲۶ انفجار مهیب بندرعباس
بندرعباس پشت سر هم داره صدای انفجار میاد الانم 2 تا 2:27
۲:۲۷ دوباره انفجار
این دفعه دورتر یا ضعیف‌تر
بندرعباس دو صدای دیگه ۲:۲۷ بازم فرودگاه یا پایگاه هوایی
صدای قبلی شدید تر بود
سه تا انفجار پایگاه هوایی بندرعباس
ساعت ۲.۲۷
سلام وحید جان 2:27 بندرعباس صدای دو انفجار
الان بندر دوباره دوتا صدا ۲:۲۶ ، اولی زد دومی انگار پدافند بود
2.26 بندرعباس
دو انفجار شدید به فاصله ۴ثانیه در منطقه گلشهر شنیده شد.
منابع حکومتی:
استانداری هرمزگان: در ساعت ۲:۲۰ نقطه‌ای در حوالی بندرعباس مورد اصابت حملات دشمن آمریکایی قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77133" target="_blank">📅 01:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77132">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S8pRM0HMzTPL9qZ_Gae_v1KiEpXX4Ote-liIkf6IFCC_qs5OUYQX45H7bRTlXd4KzuUmwqsOW7inxwc7Ug4AO2jljIdnRsMavSc4u9nn75ezCCuk1IPzzpz0UqW8yMow92DvOEEUgpO1pRvld8-D1i-TpCsyA-po4-ffteFd65nEaMztXZf51le33qnVD7Eot2M8IA0YtLUnOA19EYxxpxnobYc8vNOiUx544ZODPLVpNr0CeLSABryyodzUx_NpJOPpLBoknPrfHRFW6jZ0mOgt9kxyfodBTt_lrZjlTyi5GRbywgJ8zxbXOFyPl-Peh8MHoZtrPh69Nc6EHJsvgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه ۲۴ تیر در سخنرانی خود در «دانشکده جنگ ارتش ایالات متحده» در کارلایل پنسیلوانیا، گفت ایران «به‌زودی شکست خواهد خورد.»
او با اشاره به حملات اخیر آمریکا علیه ایران گفت با وجود آنچه «عملیات نظامی» خواند، بازار نفت دچار جهش شدید نشده و برخلاف پیش‌بینی‌ها، قیمت‌ها افزایش چشمگیری نداشته است.
ترامپ افزود بسیاری انتظار داشتند قیمت نفت تا ۳۵۰ دلار در هر بشکه افزایش یابد، اما این رقم در حال حاضر حدود ۷۹ دلار است و حتی چند روز پیش به ۶۸ دلار نیز رسیده بود.
رئیس‌جمهوری آمریکا همچنین گفت اقداماتی که به گفته او در واکنش به «عدم پایبندی ایران» انجام شده، محدود بوده و در صورت آرام شدن شرایط، قیمت نفت ممکن است به حدود ۵۵ دلار یا حتی کمتر کاهش یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77132" target="_blank">📅 00:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77131">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b248f4653d.mp4?token=EtcIdkqtqDyp3gv7MbzIJgpUsp4sGlRWc6OCUG_RzJyz3Oo_6X7W-NOUMfDIYmFdjO7bOYhmju_Dh7wJnSAkn-6TV6TOEw4qwz34IMY_ejGdv8jJnoaN-099Y21anvSRycSg2GS3mxpq5e4aNr-6Y-MaR3ms-EkZx4ONn9iz8UaSwl4bkFkbf5f3L-u85uPANjNra7fM36vLkKtt5Xu3WaXZeku3b_DHHFnoY918jkOjnAWzvJC2tUvqxXM38Wp3s6hE76lCU65y7Osb-qIFRbX81RwQiVJeHpkzqy-bU2AD5mA_cCREBSzF-byhnrViZPKeND5_MSfDH3wd_nyxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b248f4653d.mp4?token=EtcIdkqtqDyp3gv7MbzIJgpUsp4sGlRWc6OCUG_RzJyz3Oo_6X7W-NOUMfDIYmFdjO7bOYhmju_Dh7wJnSAkn-6TV6TOEw4qwz34IMY_ejGdv8jJnoaN-099Y21anvSRycSg2GS3mxpq5e4aNr-6Y-MaR3ms-EkZx4ONn9iz8UaSwl4bkFkbf5f3L-u85uPANjNra7fM36vLkKtt5Xu3WaXZeku3b_DHHFnoY918jkOjnAWzvJC2tUvqxXM38Wp3s6hE76lCU65y7Osb-qIFRbX81RwQiVJeHpkzqy-bU2AD5mA_cCREBSzF-byhnrViZPKeND5_MSfDH3wd_nyxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکایی یک شناور متخلف را در خلیج [فارس] از کار انداختند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۵ ژوئیه، در اجرای تدابیر محاصره دریایی علیه ایران، یک نفتکش بدون محموله را که تلاش داشت به‌سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) مشاهده کردند که نفتکش «بلما» (M/T Belma) با پرچم کوراسائو، در آب‌های بین‌المللی به‌سوی جزیره خارک در حرکت است. این شناور تجاری هنگام تلاش برای نقض محاصره آمریکا، چندین هشدار را نادیده گرفت. یک هواپیمای آمریکایی با شلیک موشک‌های هلفایر به دودکش کشتی، آن را از کار انداخت. این کشتی دیگر به‌سوی ایران در حرکت نیست.
نیروهای آمریکایی در ساعت ۴ بعدازظهر به وقت شرق آمریکا در ۱۴ ژوئیه، محاصره دریایی شناورهای در حال تردد به بنادر و مناطق ساحلی ایران یا از مبدأ آن‌ها را از سر گرفتند. در نخستین ۲۴ ساعت اجرای محاصره، سنتکام مسیر دو شناور تجاریِ مطیع را تغییر داد و یک شناور متخلف را از کار انداخت.
نیروهای آمریکایی همچنان هوشیار و آماده‌اند تا از رعایت کامل محاصره اطمینان حاصل کنند.
CENTCOM
سنتکام به جای «خلیج فارس» چیز دیگری نوشته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77131" target="_blank">📅 00:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c3872dd08.mp4?token=CCNfFAmol8Jhia8yMLDyQP0mnbfb3kHGIijdsVtr2E88M6-qVQrIp_gNZy7p_RzuvWkIoNACXuYY6XPuAIAF5UJJE_uo2dIPtW-QNw6f8IOP7gBj_gudpewKQJKYcqpsNNBWlGAQKxVrXbtvVjmECjqJRRwSHg1UwAtoNG3bIwTyivahZdrQ9_eFc2peKJFRsZRotw9RFGkXD0mdHJ1NTZTqJ_JuX-AbYzAjhtonzxqvb9UqXolwCnmmnacyKZAhzKtonZ73HVa8XqZ8HFTyeuQAke7hgveJ-9UcOfEnv4kQ4pe6awqV43uFZbI4E_tbkeI11YScgV2RSggSe_zp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c3872dd08.mp4?token=CCNfFAmol8Jhia8yMLDyQP0mnbfb3kHGIijdsVtr2E88M6-qVQrIp_gNZy7p_RzuvWkIoNACXuYY6XPuAIAF5UJJE_uo2dIPtW-QNw6f8IOP7gBj_gudpewKQJKYcqpsNNBWlGAQKxVrXbtvVjmECjqJRRwSHg1UwAtoNG3bIwTyivahZdrQ9_eFc2peKJFRsZRotw9RFGkXD0mdHJ1NTZTqJ_JuX-AbYzAjhtonzxqvb9UqXolwCnmmnacyKZAhzKtonZ73HVa8XqZ8HFTyeuQAke7hgveJ-9UcOfEnv4kQ4pe6awqV43uFZbI4E_tbkeI11YScgV2RSggSe_zp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی با شرح: 'پاسگاه احمد ریزه
#چابهار
، شهرک بهار ، جاده‌ی رمین و چابهار' در سیستان و بلوچستان
پیش‌تر هم‌زمان با آغاز حملات آمریکا پیام‌هایی از شنیده شدن صدای چند انفجار در این منطقه دریافت کرده بودم.
چهارشنبه ۲۴ تیر ساعت ۲۲:۳۸
#Iran
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77129" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWJ2V6eZoalMkt8qg1MzvW_SkmogxdOtQXwTYG_GpcjlSc2YXYUaDokUH42jOVud-TR6GHGpr6ipLF4ESQOXkjPEpefF99QpFBpDlRjvrcEEBtpDE9m8y8h1ba2sMLGYMek0S9A6AgEoS-0pfPXC_hffNTaiXD6q4DaOKVRWQUiAtyAtkLNye-S5cc3JxVwRscQ5gMrux8SSbq_pEP8axb5jzK-NGeN9FnJgJRdP8FMauYxoRgv6cEycHDIsq9BwOr8l2hlTLltuNhLp1z5NeLGKaefZrTXOD8qokKAppHMNaXS1bFB4ZZGToOW107PGQhrgx9ahjbjnm7IvI9NNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های داخلی ایران از شنیده شدن صدای انفجارهایی در اهواز و چابهار خبر داده‌اند، اما تاکنون جزئیاتی درباره علت این انفجارها یا اهداف احتمالی حملات منتشر نشده است.
رسانه‌های ایران به نقل از استانداری هرمزگان از انفجار در شهر بندرعباس خبر داده‌اند. برخی از گزارش‌ها نیز حاکی از اصابت به شهر راسک در نزدیکی چابهار است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77128" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ۲۲:۵۷ دوباره انفجار
یکی دیگه وحید 10:57 بازم سمت گلستان
دوباره اهواز رو زد ۲۲:۵۷
بازم سمت گلستان
۲۲:۵۷ گلستان اهواز بازم انفجار کل خونه لرزید
تو خونه میلرزیم خونها میلرزن
همین الانم دوباره زدن ۲۲:۵۷
اهواز ۲۲:۵۷ پشت سر هم ۳ تا سمت گلستان و کوی مجاهد خیلییییی نزدیک
انفجار شدید ۲۲:۵۸ اهواز
اهواز دوباره زد شد پنج تا
همین الان دوباره فکر کنم واسه 7-8 امین بار بود واقعا از همشون خیییلیی شدیدتر بود
اهواز ۲۲:۵۷ این هشتمین صدای انفجاری بود که شنیدم
۲ انفجار خیلی شدید همین الان
اهواز ساعت ۲۲:۵۷
دارن مداوم‌ اهواز  رو میزنن
سلام اهواز و سه چهار بار زدن آخرینش 10/58دقیقهصدای بلند که شیشه هالرزید
اهواز ۲۲:۵۸ یه انفجار دیگه.ما بهارستانیم صدا خیلی بلند بود
از ساعت ۱۰:۳۰ اهواز رو داره میزنه
🔄
الان باز گلستان زدن
بازم صدا انفجار ۱۱:۰۹ گلستان اهوا زشنیده شد
۲۳:۰۹ بازم انفجار گلستان اهواز
همین الان دوباره اهواز ۲ انفجار پشت هم ساعت ۲۳:۰۸
وحییییید ۲۳:۰۸ ۲تا پشت هم داره بقایی رو میزنه اونجا پادگانه
23:09 دقیقه خیلی بد زد
سلام ، اهواز سمت گلستان دوباره  ۲۳:۰۹ زدن
۲۳:۰۹ دوباره انفجار شدید اهواز
اهواز رو زدن دوباره
اهواز ساعت ۲۳:۰۹…سمت کیانپارس صدا شدید احساس شد.
وحید اهواز پشت پادگان بقایی و پادگان ملاشیه رو داره میزنه ۲۳:۰۷
ساعت ۲۳:۰۹ اهواز سمت گلستان صدای انفجار این چهارمین صدای انفجاره که میشنوم
اهواز همین الان دوباره انفجار داشت
نقاط مختلفی بوده و من دیگه نمیتونم تشخیص بدم دقیق که کدوم پایگاه بود، اما انفجار ها زیاده
تا ۲۳:۱۰ بالغ بر شش صدای انفجار شنیده شد. در اهواز هستیم. که جمله از صداهای روز گذشته بلندتر بودن.
اهواز ساعت 11:10 محدوده بهارستان* رو زدن
شش هفت بار دیگه هم از اهواز صدای موج انفجار رو حس کردیم. با سوت شروع مسابقه انفجار ها هم شروع شد
🔄
ساعت ۲۳:۱۶ موج بعدی پیام‌های مشابه درباره انفجاری دیگر رو دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77127" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i3MAXb4vGJ2upoMuSx2tR5QoF11n57uTtqe99WsCpv8Hpphsu7jte2_tmSxOVw24GJ4mnpiWX4rkVI5eoWhBvhYlp3qXEwOENyppGRwHOCI-KsTCMIEmhOK26plp6A8X4HxXWgLsfsCgwBgJe-B0o-9OMT3JvD_r8YWe31XtVBgXT3g-6W97eXyQVrjCDzUkKbQcacV_KtDQJ4P9Cf63hfHZyIJrLW1n6OC0UGHb6kiLLJo1syz1CAQDplFDzjau3AF2gY8VHkXNr7fDJV2OGeZ_QV9iRqt_oHK1QDzzolARpdlVkgKGY0o4vRmE9twbCoL7iILW_dR42iFseUpmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، ترجمه ماشین:
ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ به وقت تهران]، نیروهای ایالات متحده عملیات دومین موج حملات امروز علیه ایران را آغاز کردند. این حملات توانمندی‌های نظامی ایران را هدف قرار می‌دهند که برای تهدید کشتی‌های در حال عبور آزادانه از تنگه هرمز به کار می‌روند؛ آبراهی بین‌المللی که برای تجارت جهانی حیاتی است. ارتش ایالات متحده به دستور فرمانده کل قوا، ایران را پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77126" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/416beb8ba4.mp4?token=A4J4Wv2o-N-yvZ3BbrXo07AOuuzBGclkX7qOU0kJR-eh3g-JcbaTzD-OaiPjmu3rhB7j0UY36adhzR8fgvYJxpoAJozhH8IDeX_HTx-BNzLNOh0XmmHqMgu_XsppqscnQF9Gk78-E4rWRUrD6abWgwSuhickC16yj3LBes3MiPJhVfwBjXEVz4INWVS8A8J29rnoBr-YKdC4DmUo-ReR-E7Tfnkq85mMm876-DZkdqYYAgYeMoGtJmqzH1iHPnGkIKxlKluUF-pCFDfJUEQgoxj-TWt7DTWO4MJ8wku9zwELTxozuXQOYdZzUYN0BXCz2Fn_XT8rRXi-Rn3C-CUYXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/416beb8ba4.mp4?token=A4J4Wv2o-N-yvZ3BbrXo07AOuuzBGclkX7qOU0kJR-eh3g-JcbaTzD-OaiPjmu3rhB7j0UY36adhzR8fgvYJxpoAJozhH8IDeX_HTx-BNzLNOh0XmmHqMgu_XsppqscnQF9Gk78-E4rWRUrD6abWgwSuhickC16yj3LBes3MiPJhVfwBjXEVz4INWVS8A8J29rnoBr-YKdC4DmUo-ReR-E7Tfnkq85mMm876-DZkdqYYAgYeMoGtJmqzH1iHPnGkIKxlKluUF-pCFDfJUEQgoxj-TWt7DTWO4MJ8wku9zwELTxozuXQOYdZzUYN0BXCz2Fn_XT8rRXi-Rn3C-CUYXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: ویدیوی منتشر شده در منابع محلی
پیام‌های دریافتی:
اهواز ۲۲:۴۸، جنوب اهواز کامل لرزید
وحید جان الان زدن ۲۲ ۴۸ اهواز لشکر
۲۲:۴۸  خیلی شدید تر از قبلی ها صدا انفجار اومد
انفجاری وحشتناک ساعت ۲۲:۴۸ اهواز
وحید اهواز کوی مجاهدیم ۲۲:۴۸ دوتا خیلییییی نزدیک زد
دوباره 22.48 اهواز، این سنگین تر بود.
همین الان سمت گلستان اهواز انفجار
اهواز باز شروع شد این بار صدا از سمت لشکر ۹۲ میاد
انفجار اهواز ۲۲.۴۸
صدای وحشتناک انفجار اهواز
ساعت ۲۲:۴۹
خونه کامل لرزید
دوباره اهواز رو زدن ساعت ۱۱ و ۵۰
اهواز 22.50  دوباره
اهواز بازم زد ۲۲:۵۰
دوباره زدننن خیلییی نزدیک بود 22:48
صداش خیلی زیاد بود
براى دفعه چندم اهواز ساعت ١٠:٤٨ انفجار بسيار شديد، انگار تمومى نداره
سلام شب بخیر
همین الان  اهواز ساعت ۲۲:۴۹  صدا  اینقدر زیاد بود انگاری سنگر شکن بود سمت گلستان
ساعت ۲۲:۵۰
بکی دیگه هم زد همین الان  قشنک خونه ها میلرزه
ولی صدای هیچ جنگنده نمیاد
یکم پیش اهواز رو زدن فکر میکنم ۹۲ زرهی باشه
همین الان سمت گلستان اهواز انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77125" target="_blank">📅 22:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjsIrVZ_qZRybFYI2SdXtPnvaIA0BoVQ38ycBZjf33kjMk2fjTDlMpb8eMx9ikd766Vgj5rlN26fTiZmGeRhS4B35gWfpfcgGq-iAz7DkDEBbzcEaeV2A-uiLRLGJCMLYIGOpjNsww1f6Tx_PSWZK26GUN-5gxZcFszCs3d35Q2Ti4vDdjPKe8wyQ_mVoW8xFETC65Aj0gRA40f7LHdmVmDDdKizF9G0YBSpSBxN_kAucKn47hoHmjVtDKONvkDjLkow6AzZuIcVtfPe9EkC8fw5EWcACF9aUHElvX7NWKJzso1nnyENW5F64JcNB8FBAjHVrpIfS2w--t9fy6JvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه در پاسخ به پرسش خبرنگاران درباره این‌که آیا پیش از آغاز حملات آمریکا به پل‌های ایران، مهلتی برای تهران تعیین شده است، گفت که علاقه‌ای به تعیین ضرب‌الاجل ندارد.
ترامپ گفت: «من دوست ندارم مهلت تعیین کنم، اما آنها تقریباً می‌دانند؛ آنها از ماجرا خبر دارند... بهتر است رفتارشان را اصلاح کنند.»
این در حالی است که رئیس‌جمهور آمریکا ساعاتی پیش حکومت ایران را تهدید کرده بود که اگر تا هفتۀ آینده با واشینگتن به توافق نرسد، نیروگاه‌های این کشور هدف قرار خواهد گرفت.
او به برنامۀ «گزارش ویژه» شبکۀ خبری فاکس‌نیوز گفت اگر تهران توافق را نپذیرد، هفتۀ آینده حملات را به نیروگاه‌ها و پل‌های ایران گسترش خواهد داد: «هفتۀ آینده وضعشان واقعاً بد خواهد شد؛ چون نوبت نیروگاه‌ها می‌رسد؛ نوبت به پل‌ها می‌رسد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77124" target="_blank">📅 22:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">در لابلای ده‌ها پیام از اهواز این چند پیام رو هم درباره چابهار فرستاده بودند:
همین الان صدای دو انفجار شدید در چابهار ۲۲:۳۸
چابهار ۳ دفعه صدای انفجار شدید اومد
درود
چابهار صدای انفجاری مهیب اومدددد الان
سلام
۲۲:۳۸ دقیقه ۲ بار چابهار زد
هنوزم صدای جنگنده میاد.
همین الان چابهار زدن
چابهار رو الان زد سه انفجار ساعت ۲۲:۳۵
آپدیت:
سلام ، چابهار رو سه بار زدن ، خیلی بد بود ، احتمالا یه پاسگاه مربوط به دریابانی به سمت جاده رمین
ده دقیقه پیش دوتا انفجار چابهار
سلام وحید پاسگاه کنار خونه‌ی مارو زد
چابهار
پاسگاه احمد ریزه
جاده‌ی ساحلی رمین
سلام چابهارم زد
📡
@VahidOnline
آپدیت
:</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77123" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#اهواز
پیام‌های دریافتی:
انفجار اهواز ۲۲.۳۱
سلام اقا وحيد
10:30 اهواز دو انفجار بسيار شدييددددد
اهواز دو انفجار خیلی شدید ساعت ۲۲:۳۱
سلام وحید جان
۲۲:۳۱ اهواز صدای سه تا انفجار اومد
سلام، اهواز ساعت ۲۲:۳۰ صدای چنتا انفجار پیاپی اومد
اهواز ۲۲:۳۱ صداش مهیب بود
ساعت ۲۲:۳۵
صدای انفجار مهیب اهواز
اهواز شروع شد با شروع بازي
یک صدای انفجار خیلی ترسناک با لرزش زیاد اومد تو اهواز ۲۲:۳۰
دقیقا دیشب هم همین موقع بازی زدن
ساعت ۱۰:۳۱ صدای سه انفجار از  اهواز
ااهواز همین الان زدن
اهواز دوباره ساعت 22:31 دو انفجار پشت سر هم
وحید جان سلام
اهواز ساعت ۲۲:۳۰ همزمان سوت شروع بازی فوتبال ۲ تا انفجار
سنگر شکن بود احتمالا
زمین لرزید
سلام وحید جان،
اهواز ساعت ۲۲:۳۰ صدای انفجار اومد
شیشه ها لرزیدن
اهواز صدا انفجار اومد موجش زیاد بود
سلام وحید اهواز رو زد ساعت ۲۲:۳۰
ساعت ۲۲:۳۱ دوباره با شروع بازی اهواز انفجار
اهواز وحشتناک بود
۲ انفجار سنگیننن
ساختمون بد لرزید
🔄
الانم زده ساعت ۲۲:۳۵
دوباره انفجار اهواز ۲۲.۳۵
دوباره زد
دوباره خیلی شدید تر ساعت 22:35
دور بود خیلی اما اینقد سنگین بود خونه لرزید چندبار
صدای دو انفجار همین الان ساعت ۲۲:۳۵
۲۲:۳۵ اهواز بازم زدن بار دومع
۲۲:۳۵ یکی دیگه اهواز زدن
اهواز یه انفجار دیگه ۲۲:۳۵
همین الان یکی دیگه زد. سنگین بود ۲۲:۳۵
پشمام دوباره
زمین میلرزه، اهواز ۲۲:۳۵
دوباره ۲۲:۳۵ انفجار اهواز
سلام وحید جان
همین الان دوباره ۲۲:۳۵
ساعت ۲۲.۳۴ انفجار دوم
اهواز
این یکی شدیدتر بود
دوباره زدن، نمیدونم نزدیک تر بود یا انفجار قوی تر بود، سمت جنوب اهواز ساعت ۲۲:۳۶
۱۰:۳۴ دوباره یه موشک دیگه زدن غیر از اون دوتا این یکی از اون دوتا هم بدتر بود خیلییی بد بود
🔄
بازم زد ۲۲:۳۷
این دفعه سه تا بود انگار
۲۲:۳۷ الان هم
10:37 اهوازو زدن
بازم انفجار پیاپی اهواز ۲۲.۳۷
بازم زد ۲۲:۳۷
این دفعه سه تا بود انگار
آقا وحید بد گیر داده
۴ تا دیگه
۲۲:۳۷ باز هم اهواز دو تا صدا پشت سر هم
اهواز دوباره زد الان دو بار ساعت 22.37
اهواز ۲۲:۳۷ بازک زدن صداش بلند بود
سلام دوباره دارن میزنن ساعت 22:36
۳تا دیگه پشت سر هم ۲۲.۳۷ اهواز
خیلی محکم داره میزنه
یا خدا ۳ ۴ تای دیگه زد
یکی از یکی ترسناک‌تر
اهواز ۲۲:۳۸
با سوت شروع بازی ، انفجارهای پیاپی.
اهواز روی لرزه‌ست وحید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77122" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JEdIsyZuvr97HodyyYhojT7aqjOUD-2_zrBtlNModdMdzInA56GCPmlDjXrxgxCHAD-katSVUDYNc930R1iPh1mD9y69GlEBek1wG6u_hi7km0aVnsEXwEDS_1sfnRhsbnHf0DF60mPmwaY7MWh8W0arvgXVWUhdGAQE4k2M5rAI6_Fsv7VdTQqb7TlE1Ry7AlP8PgBNrBgBpx_e-tNPTVooJamgUNsTLwi8wVHNpgEkKy4q4NqLSBAGzSw4NIXWVx6djHl0MepXLqQWtv1qVGFuRnlq2MaT6ivQvpw6OtrC064w4AgOVsO0UCufxZ-KwAGpAwwyyPkOEXAwBdhK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام عارف خوشکار، از بازداشت‌شدگان اعتراضات سراسری ۱۴۰۱، سحرگاه امروز چهارشنبه ۲۴ تیرماه، در زندان قزلحصار کرج اجرا شد.
masoudkazemi81
یک منبع مطلع نزدیک به خانواده این زندانی سیاسی به هرانا گفت: خانواده عارف خوشکار حدود ساعت هشت صبح امروز از اجرای حکم اعدام وی مطلع شدند.
همچنین به خانواده اعلام شده است که برای رویت و تحویل پیکر، صبح پنج‌شنبه ۲۴ تیرماه حدود ساعت ۹ صبح به بهشت زهرا مراجعه کنند.
این منبع مطلع در ادامه افزود: عارف خوشکار روز شنبه ۲۰ تیرماه به سوئیت ۳۵ زندان قزلحصار منتقل شده بود و خانواده‌اش روز یکشنبه ۲۱ تیرماه آخرین ملاقات را با او انجام دادند.
خانواده او با درخواست اعطای مهلت یک‌ماهه و برگزاری جلسه‌ای برای جلب رضایت خانواده مقتول، در تلاش برای توقف اجرای حکم بودند، اما این تلاش‌ها به نتیجه نرسید.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77121" target="_blank">📅 21:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه محمدباقر قالیباف، رئیس مجلس شورای اسلامی
،
به نقل از منابع حکومتی:
🔹
این روزها که دوباره آتش جنگ شعله ورتر شده سوالاتی در بین مردم و گروه‌های مختلف پرسیده می‌شود و هرکس به فراخور نگاه خود به آن پاسخ می‌دهد. آیا ما به دنبال جنگ هستیم؟ آیا جنگ و سایه جنگ پایان می‌یابد؟ آیا با مذاکره می‌توانیم به اهداف خود برسیم؟ وقتی با آمریکای بدعهد طرفیم اساسا مذاکره چه فایده‌ای دارد؟ و در نهایت موضوع مهم این است که چگونه حق خود را بگیریم و پیروز این جنگ باشیم؟
🔹
اگر با نگاه منافع ملی، امنیت ملی و به‌دور از نگاه جناحی به این موضوع بنگریم می‌توانیم به پاسخ‌های صریح، روشن و دقیق دست پیدا کنیم. اول باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است.
🔹
دوم، همان‌طور که قبلا نیز بارها گفته‌ام، آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست. پس نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم.سوم، مقاومت یکپارچه ملت ایران و نیروهای مسلح ما، این نقشه شوم دشمن در جنگ  40روزه را باطل و آن‌ها را مجبور به درخواست آتش‌بس و انجام مذاکره کرد ولی حتماً راهبرد غلط آن‌ها را عوض نکرده است. آمریکا همیشه خوی استکباری دارد و هیچ‌گاه ایران قوی را نمی‌پذیرد.
🔹
با این فرض‌ها باید پاسخ سوالات بالا را داد.ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم.
🔹
تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد، در غیر این‌صورت اگر قرار باشد جمهوری اسلامی ایران از این متن انتفاع نبرد ما نیز براساس سیاست چشم دربرابر چشم که قبلا گفته ام، دلیلی برای پایبندی به چنین تفاهمی نداریم و همانطور که این روزها شاهد هستیم، نیروهای مسلح ما مثل همیشه برای مقابله با تهاجم دشمن آزادی عمل کامل دارند.
🔹
ما بر خلاف جنگ 12 روزه، به درستی در جنگ 40 روزه تنگه هرمز را بستیم چرا که باعث ناامنی و به خطر افتادن امنیت ملی ما شده بود. امروز هم امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود.
🔹
حالا برای تحقق این موضع ما چه فرایندی را طی کردیم؟ با شروع جنگ تحمیلی سوم در اسفند ماه، نیروهای مسلح ما کنترل خود را بر تنگه اعمال کردند. در طول مذاکرات نیز ایستادگی و ترتیبات ایرانی تنگه هرمز را در بند 5 تفاهم‌نامه تثبیت کردیم و آن را اهرمی برای اجرای 4 بند دیگر ستانده‌های خود، از تفاهم‌نامه قرار دادیم. حالا هم که به مرحله اجرای تفاهم‌نامه رسیدیم، آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود. دشمن برای جبران شکست خود فشار وارد می کند ولی ایران با اتکا بر قدرت خود اجازه تحمیل اراده دشمن را نخواهد داد.
🔹
ما باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم؛ جنگ و مذاکره دو  روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ،  بخشی از راهبرد مقاومت و صیانت از منافع ملی است. این هماهنگی و استفاده همه‌جانبه از ابزارهای دیپلماسی و دفاعی، برای حفظ ایران عزیز نه تنها یک وظیفه بلکه یک ضرورت اجتناب‌ناپذیر است. جداسازی و انتخاب یکی از این دو روش  به‌عنوان تنها راه حل، خطای راهبردی است. ما در جنگی پیچیده با بزرگ‌ترین قدرت مادی جهان مواجه هستیم و در این جنگ افتخارات بزرگی کسب کردیم؛ پس باید فکر و عمل ما همان‌قدر بزرگ، پیچیده و مقاوم باشد.
🔹
این مثال را می‌توان در مورد  لبنان، رفع تحریم‌ها، آینده پایگاه‌های آمریکا در منطقه و انتقام وخونخواهی امام شهید انقلاب و سایر شهدای این دو جنگ تحمیلی هم تسری داد.
🔹
راه پیروزی و احقاق حقوق ملت در این جنگ و شرایط حساس، پیروی از رهنمودهای رهبری و حرکت  براساس یک  نقشه‌راه دقیق بر مبنای مقاومت، عقلانیت و استفاده هوشمند از همه ظرفیت‌های دفاعی و دیپلماسی در جهت تحمیل اراده خود بر دشمن و کم اثر کردن تبعات اقتصادی جنگ به مردم، است.
🔹
مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قوا است و همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند، برای جنگ یا دیپلماسی یا هردو تلاش کنیم.
🔹
بر همین اساس از همه ملت ایران با هر نگاه و سلیقه‌ای می‌خواهم در تبعیت از اوامر رهبر معظم انقلاب وحدت را حفظ کنند، در میدان باشند و این حضور و وحدت را به رخ دشمنان بکشند. همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید.
🔹
همچنین به اخباری که توسط عده‌ای منتشر می شود تا شما را از مسیر طی شده پشیمان و نسبت به آینده ناامید یا نسبت به خادمین ملت بی‌اعتماد کند، نباید توجه کرد. دشمن به ناامیدی، ترس، اختلاف و بی‌اعتمادی‌های متقابل طمع کرده است. حتماً حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند.  مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت خود را به فضل الهی خواهید دید.
🔹
اینکه ما امروز از موضع قدرت در تنگه هرمز سخن می‌گوییم، نتیجه‌ همان قدرت میدانی است که مردم برای ما ایجاد کرده اند، و برای ما مسجل است که انتقام خون آقای شهیدمان را نیز به ثمر خواهیم نشاند و دشمن باید بداند که هیچ کوتاهی در تحقق مطالبات خود نخواهیم داشت.
🔹
بنده به سهم خودم در دوران جنگ تحمیلی سوم، هم در میدان دفاعی و هم در مقابل طراحی دشمن  در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام.
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های رهبری معظم انقلاب است. عمرم را صرف مبارزه با دشمن کرده‌ام و هراسی نیز از جنگ با دشمن یا تهمت و تهدید و تخریب نداشته و آرزو دارم در این راه به رفقا و رهبر شهیدم بپیوندم.
🔹
در انتها به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما، در مهم‌ترین سال‌های جوانی من و خانواده‌ام پای سفره‌های مهمان‌نوازی شما در مناطق عملیاتی جنوب نمک گیر شده‌ایم، گرمای عشق و محبت شما به هموطنان خود و به ایران را هرگز فراموش نمی‌کنم.
🔹
بدانید که ما سرمان برود، پای قولمان هستیم، شاهرگمان را برای دفاع از این مملکت گرو گذاشته ایم. به فضل و منت خدا بدانید که پیروزی ایران عزیز نزدیک است و مقاومت تاریخی شما ماندگار خواهد شد.
🔹
مردم عزیز ایران! ایمان داشته باشید که این بغض‌های فروخورده شما و این وحدت بی‌نظیر تک تک ملت ایران در کف میدان، پیروزی ما را تضمین خواهد کرد. ما نه تنها از تهدیدها و جنگ با دشمن نمی‌هراسیم، بلکه تحت ارشادات رهبر معظم انقلاب، پاسخ قطعی این جنایت‌ها را به دشمن جنایتکار خواهیم داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77120" target="_blank">📅 21:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبرگزاری فارس با انتشار تصاویر بالا مدعی شد:
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77117" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EChD1Z0tQVntwOwYCx95M8ZNulnfPjl5nmfOmf798ly83wxNv71eaXACK-cN3APpScV2-Ms0St1-iKv9YB3sNNu7AFpEvLci5BYhRwSpLfotfFYmA9C61uVjNTNyFIzWxAGyFWqXfxmJldENHlW_dQq1rlqpwQp91G3UyTydg4fF8HeUSU6P9AhephByi4KG4HNzFdkT9p09jAsyATfB6pXnBKPPi7RXGJG-9gi9fVXvhI-ynPkxPc79WepbYpDPfvexC5DH8sUpJUgI99qVIHPoYYvPm5hDpHdrAa9iAr-SE4K2G8FBe7-_u5hXdR9CU0wTB3SGTMsCrskDwbuPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام، ترجمه ماشین:
🚫
ادعا: رسانه‌های دولتی ایران مدعی شده‌اند که نیروهای آمریکایی در ۱۴ ژوئیه یک تأسیسات غیرنظامی ذخیره‌سازی گندم در هویزه را هدف قرار داده‌اند. این ادعا نادرست است.
✅
واقعیت: نیروهای آمریکایی در ۱۴ ژوئیه اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. هم‌زمان، ایران غیرنظامیان بی‌گناهِ در حال عبور از تنگه و همچنین غیرنظامیان در کشورهای همسایه خلیج فارس را هدف قرار داده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77116" target="_blank">📅 19:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77114">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NPqAS1Np-4kZc_szTIlcFBMsEWvTdNEneVOrnJ_iwRLDZ9kDTmqH1EbY4a3w_FC4GaIjzevcRlijSPPOfDeIGv_9i4j81QyR40fYORckyG4WNAR9wONc5YhHUG06d7rYQJJBklreUp5OcNKsymsFFsVTiK9HBpxREcXnBRCRtBZc8mk-lHqBuamfkRxsnnXQ7yymnnpGo1IvyZet1n-MbQuomUsNb1J5a-tiUHLCowgzUll7RnBGRg1msq7SxJTN4e3sL-jLzGRVfMxqlkvcE35vnLbO2cusZC5CVm3N3_sXl52jz3AJrnPPDTz0K9UoWEhjIVzdSJOsPSap7thYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=GnF5HpRzzJRJKjuIDRKEI2YB1XtODgx5y8p01l775RP5PMSIOdAYXnuqArPsaiN6t0Y70c0we2sB8XagYm_s88rO1Hl1_HX-VndGz2LWNJlJG5guqGQ9hh4-NGzyOJpI_kQLidubhPRUYfe1RTfUcaaXaO6KVEQgItEJZCJiKuUd8W4lj5EC6fzE1u1yPTe-QqfgRmN-UgYTlodu9VgrHZReQzJ5dI2sAMih7munZLhKMg9pLJ6QK-c-gKG__Pb8iPLn0RKyLmotXbM4Ml3EeuSxm6OkBrdRmXLlnajlfoEc8BDqdRBemqQ0UaaMGP7ebfA16SwP3KwQDhf914u5mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32acbd8d90.mp4?token=GnF5HpRzzJRJKjuIDRKEI2YB1XtODgx5y8p01l775RP5PMSIOdAYXnuqArPsaiN6t0Y70c0we2sB8XagYm_s88rO1Hl1_HX-VndGz2LWNJlJG5guqGQ9hh4-NGzyOJpI_kQLidubhPRUYfe1RTfUcaaXaO6KVEQgItEJZCJiKuUd8W4lj5EC6fzE1u1yPTe-QqfgRmN-UgYTlodu9VgrHZReQzJ5dI2sAMih7munZLhKMg9pLJ6QK-c-gKG__Pb8iPLn0RKyLmotXbM4Ml3EeuSxm6OkBrdRmXLlnajlfoEc8BDqdRBemqQ0UaaMGP7ebfA16SwP3KwQDhf914u5mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو پدر سام حسنی از محل واقعه منتشر کرده.
کودکی که در میان جعبه‌های گیلاس کشته شد.
پنج‌شنبه ۱۸ تیر:
نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
@
VahidOnline
در جریان این تیراندازی، گلوله به کودکی که در قسمت بار خودرو حضور داشت اصابت کرد. او بر اثر شدت جراحات جان خود را از دست داد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77114" target="_blank">📅 18:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۱۷:۳۸
[جزیره] هنگام، الان صدای ۲ تا انفجار بزرگ اومد سمت وسط جزیره
جزیره هنگام رو همین چند دقیقه پیش دوبار زدن
📡
@VahidOnline
🔄
ساعت ۱۸:۳۹ خبرگزاری مهر
:</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77113" target="_blank">📅 18:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77111">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FzcgmkzL3W2pTPePrUJW6J7NhaPwozrODUAN7keVlo6wC7I5GsFQwIUON_n-ZSsFeD53jRJDylykYZit_dDV0WN3wAQu5VIiKNO9yX_xUpvTZvBC52Qj5mhyqOolkc9wfWa6ZiA-L5jln5K1VUac5phgQWDsBhE0zFbdnqamuy0cmUytr7ma9p78J3x9v9Ppy47VeEabwObLumShJb4JqaHFFG24IOm2-_ye2CS6PmLJtnbUnWC02LCVROGdpRp1J6aSIr9TvPMod9ytgAeM1c8qySVYRpzcPcz74fRb-m3erUBWE_7B0DC1yYASzoqS4_fU-MGLBgfrAT6hxz33-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I9WM07wyLac7QcWBrPcNtmXJRMuN7-1KZcPlArJFLe5ItIQm6GW0PkwKa5fJkJV2xgHQYaM76_SmCvIpkTU8-ncUtTZH2iD5fsDUlFEIlm9JvtSUb_jh62q2WLT8FCeM3q1BP2F8qmhrHHuPxX3fz1SV5vZiw15U1E9gqrx3V5uHcrPCKX60MWTDyKzTZIstkXU3WC4392vUhvw0T4Fd36j9s9bEF0Du0ufRktWvB4eFA5qEOCtCTVU7lH3JyViqOjyRHmVPMYm7nODf4A_aWUjNRGmjI0Qfdi7ikrYWgdh06BwXvn4ywjBk3GlOy5o4StH7UOnFDm-tV_zfYrsbnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در بیانیه فرماندهی مرکزی ایالات متحده (سنتکام) آمده است: از زمان ازسرگیری محاصره دریایی بنادر ایران، ۱۷ ساعت پیش، نیروهای ایالات متحده مسیر حرکت دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند.
@
VahidHeadline
صدا و سیما چهارشنبه ۲۴ تیرماه گزارش داد که در ۲۴ ساعت گذشته دست‌کم دو کشتی که به گفته این رسانه قصد داشتند بدون هماهنگی با ایران و به‌صورت غیرقانونی از تنگه هرمز عبور کنند، پس از بی‌توجهی به هشدارهای اولیه، با شلیک اخطار نیروی دریایی سپاه پاسداران متوقف شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77111" target="_blank">📅 17:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHA9mmdlw9YUgTUQgY4nx0P48qpfk60Wd2Todjx3naLpgZEk6b1BkS25se_4_utbR3JwqPdJwQ07Won4Mu0gPtqbzvIWFtf2uDVs8QUWF8MnQkgzZYkhIWAe9Ied87ZNIqxI93n7CbAet7qCT22RFok4cFq9uwYiX6Bok9GACp5g5nSZOv3JhUAoaB2Ryzk0Cobdeng1s4JBX5hz8MmO-ebKv_eqeQe4QRJcwxN8nPUCqIJ4UIyvDqPHn1_po6vSBdRd3mDeGUGqHCTxo8RVVcju-CVtG6uyXKnnRDMFFszhwowJqB98jp6TBuYP8YFP_VesDc7K0r_1nCikUewB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده کریگ فورمن، شهروند بریتانیایی زندانی در ایران، روز چهارشنبه ۲۴ تیر اعلام کردند که او در زندان اوین به دلیل انجام مصاحبه با رسانه‌های خارجی، به دو سال حبس اضافی محکوم شده است.
کریگ فورمن و همسرش، لیندزی فورمن، در جریان سفر زمینی با موتورسیکلت از اروپا به استرالیا، در ایران بازداشت شدند. این زوج اسفندماه سال گذشته از سوی دادگاه انقلاب به اتهام جاسوسی هر کدام به ۱۰ سال زندان محکوم شدند؛ اتهامی که همواره آن را رد کرده‌اند. مقام‌های جمهوری اسلامی نیز تاکنون هیچ مدرکی برای اثبات این اتهام به‌صورت عمومی منتشر نکرده‌اند.
پیش‌تر وب‌سایت حقوق بشری هرانا گزارش داده بود که  این زوج ۵۳ ساله در اعتراض به رد درخواست تبرئه و جلوگیری از آزادی و بازگشت به بریتانیا، اعتصاب غذا کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77110" target="_blank">📅 16:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77109">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Clo5eGwme9Gf8lkl-Vcg0NCzz7BCtXOqsTDfngUvFr6KkSGcrgnrcHpnaXjNBeuid78hoINzDbJCcU2Sikk6j35t-0BGvjwag8gAxZ_LKytEgjvoUzCTl0Kb6bWQzVDsGUXYZpY676lxIhwZKUlaNp9XnkHFGoMi-PAOlwvFEd62gxQXuh1bQPq0HHMLgRwtT3osaBH8V0rL1XaVGeoD4kfYemvw1okT9nfVlZFMSqePsvR51YpviyH9x7R3bHbKpz5VvVw870lObz1wgU06WJWxBOu0t-ZFc3ETxgYyKxWYNrHMR98EoTbKdeo5fRHNRtkLzoyRGq2i4g1hBgTNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت دولت:
اطلاعیه ستاد عالی آزمون‌ها در خصوص برگزاری امتحانات نهایی در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
ستاد عالی آزمون‌های وزارت آموزش و پرورش در اطلاعیه‌ای اعلام کرد:
🔹
بر اساس تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش و با توجه به شرایط خاص کشور در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته‌های تحصیلی پایه دوازدهم در روز پنجشنبه؛ مورخ ۱۴۰۵/۰۴/۲۵ و پایه یازدهم در روز شنبه ۱۴۰۵/۰۴/۲۷ لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
🔹
بدیهی است امتحانات نهایی سایر استان‌ها و امتحانات بعدی استان‌های مذکور، بر اساس برنامه ابلاغی در موعد مقرر برگزار خواهد شد.
dolaat.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77109" target="_blank">📅 15:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=YfhHidOVa8l2a5wX-6xi-7qDxT5ZpNsnvkVA90DGT7IrkPZgUpD_QgmwxjPD5V8p4YO1ryBLlrogAkjJNodVkzufsRnjMcJ96HqfufmCjKU_ejEvdrzHadtXLmbKZPszBZJjXMqIDoZKc7RsBB4GSy5HEkJkGQgKFC9ycZmRXvAdeNyjUXIOM92_qWvLskE-zvABKmPGcYAUHzv23SGmDO_4k8l0aau5b8XLO61vbXMwpL-hsTclsdd15fhazCZZsrAsh_T5zdhF17sDIjTK2d8NnEyIS8p-Ipc0rb0dl-3apcEJg3iMc0PduoQ_rYAFsAdG6wbWuMJR7Q-V1w8aDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b87d0cf0d8.mp4?token=YfhHidOVa8l2a5wX-6xi-7qDxT5ZpNsnvkVA90DGT7IrkPZgUpD_QgmwxjPD5V8p4YO1ryBLlrogAkjJNodVkzufsRnjMcJ96HqfufmCjKU_ejEvdrzHadtXLmbKZPszBZJjXMqIDoZKc7RsBB4GSy5HEkJkGQgKFC9ycZmRXvAdeNyjUXIOM92_qWvLskE-zvABKmPGcYAUHzv23SGmDO_4k8l0aau5b8XLO61vbXMwpL-hsTclsdd15fhazCZZsrAsh_T5zdhF17sDIjTK2d8NnEyIS8p-Ipc0rb0dl-3apcEJg3iMc0PduoQ_rYAFsAdG6wbWuMJR7Q-V1w8aDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از دکل مخابراتی بندرعباس پس از حملات نیمه‌شب سه‌شنبه و بامداد چهارشنبه آمریکا در صبح چهارشنبه ۲۴ تیرماه در شبکه‌های اجتماعی و رسانه‌های داخلی ایران منتشر شده است.
بر اساس این تصاویر، بخشی از تاسیسات مخابراتی در این منطقه آسیب دیده، اما هنوز جزئیات رسمی درباره میزان خسارات، اختلالات احتمالی ارتباطی یا هدف دقیق این حمله اعلام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77108" target="_blank">📅 15:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77107">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9180947e9.mp4?token=mZXO9JYtleHaPFJq8iE4nC8llad3AG2jHCS9cRyHk_rjEN-fRZc8V8Lf6RRCSVywLQtDhWtJBnvca7p6YKnajcOA8ny2vTU7UP3UiQ8NhzAzdXAEuxhvYckAIGChbXCDGXoVVa7WDbeP7MKuW4xVnE6dI7sf21RlKXIs9jjnw2EhpWpslnYDBkpa8dLJcS0J2r4XOorD05HEG8IOMzyttPqaq5aaPQBxPWgZClnutHsLMjpK3_L1xfPezosHXKxZy2uJSdPLa3HOy0d4xHw0t81PvppZZNWLt3hmRntA0wyYcAnRLbWyI90nLN9NYkTItCKZr0YLFkcyoScPfWqdig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9180947e9.mp4?token=mZXO9JYtleHaPFJq8iE4nC8llad3AG2jHCS9cRyHk_rjEN-fRZc8V8Lf6RRCSVywLQtDhWtJBnvca7p6YKnajcOA8ny2vTU7UP3UiQ8NhzAzdXAEuxhvYckAIGChbXCDGXoVVa7WDbeP7MKuW4xVnE6dI7sf21RlKXIs9jjnw2EhpWpslnYDBkpa8dLJcS0J2r4XOorD05HEG8IOMzyttPqaq5aaPQBxPWgZClnutHsLMjpK3_L1xfPezosHXKxZy2uJSdPLa3HOy0d4xHw0t81PvppZZNWLt3hmRntA0wyYcAnRLbWyI90nLN9NYkTItCKZr0YLFkcyoScPfWqdig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام دور تازه‌ای از حملات صبحگاهی علیه ایران انجام داد
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دوری از حملات صبحگاهی علیه ایران را ساعت ۷:۳۰ صبح به وقت شرق آمریکا در ۱۵ ژوئیه به پایان رساند.
سنتکام در جریان این موج ۹۰ دقیقه‌ای، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد. این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77107" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77106">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwGof2wsb3YPMmoiA6C22c4DZrSr65nWDG6_0L6zdKRqdI-8rOP-CjVmzwWmqGTSWcvXUhyVTlb7TGRV7yKQaOtlWasTPWB_m0FgZF__zOJKqEGNlqcvQDKvSPuXLG8mlBayy0tqZRY_gw77FDl7bYZab2i-4f36c3CuZhBvDK619zNjIjylywunpFMDWtG8XAtDpwRxsDUT5JzNBzE4I8pfAOmvXwjDCd7HGss8DbcNO1Fv3TDRdrxYjsNTMyFHz7M6W6-AEw1OO2MgVjzrqAlkhRPAmdsYa8A6uM4Gv5xo3tEstpxwTGBvUv1hCluOvhr5d8svZAR7iIkjyWnGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپیده ابطحی، مستندساز، تدوین‌گر سینما و از اعضای خانه سینما، صبح امروز، چهارشنبه ۲۴ تیرماه ۱۴۰۵، با یورش ماموران امنیتی به منزلش بازداشت شد.
خواهر او با انتشار مطلبی در صفحه اینستاگرام خود از بازداشت این مستندساز خبر داد و نوشت که مأموران امنیتی علاوه بر بازداشت سپیده ابطحی، تعدادی از وسایل الکترونیکی شخصی او را نیز با خود برده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77106" target="_blank">📅 15:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77105">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZQXllU1vJ_1DgaJ2_vyB_cpYGRYyUzPfuRSSWkI0oZ1xjMuXya8dZourb2uOjsYW1ZBLMUXg4zzkx6k-pKtsc8uGjqmsSEBSLwPDTaBHbt5bDIoH6zffRNLyEihqYxbcsBQa02CjwYIaIHw16I_AtX-6yh317BoX8vI-PrSvsPu883HmxXCBRMBWm7v3NByszIM7wHOEHl4Odl5f-h-qio3colnrWzphnoY58pS364-zNtlAZNdjd2x4FjXjqkaRY1k4eaw7Gct48IzuEyTckQcZZbBfKUNr3m9WN8TMxSY4FMe79ll7PkA2D3kj6Zhyja2dYWuwfZuFjSh68XIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای هر دلار آمریکا در بازار آزاد ایران با افزایش سه هزار تومانی نسبت به روز گذشته، از ۱۸۷ هزار تومان فراتر رفت.
براساس اعلام سایت‌ها و کانال‌های اطلاع‌رسانی طلا و ارز، قیمت هر پوند بریتانیا به بیش از ۲۵۰ هزار تومان و هر درهم امارات به بالای ۵۰ هزار تومان رسیده است.
برهمین اساس بهای هر سکه بهار آزادی طرح جدید با افزایش چهار میلیون تومانی، بیش از ۱۸۴ میلیون تومان قیمت‌گذاری شده است.
این رشد هم‌زمان با تشدید تازه جنگ و بازگشت محاصره دریایی آمریکا بر بنادر جمهوری اسلامی رخ داده که نگرانی از افت بیشتر صادرات نفت و درآمد ارزی کشور را تشدید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77105" target="_blank">📅 15:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u94IKvrxC0eqJdLhvJXhrw9MpluOxiJIYgzIz_vq6_vSIW4d9YB36VBsHcG0r4kwputDn2zwCSuAKzUEBjipmV-l1AGmKNs7-oHb41R6u621igRYv3h60wqxSFkhJYGHNzjd30x0K-3VPerNg48nqPAJe3wcsPJHHgfD7sczBEX67UOZUebriyEk6nqVA8zi0kn-Gn6CMqa6MvVQZdE-74l8VHZGXNPv_sW1bU0d1fp8FRxGg9LzlaaoKozC8GxsaBcJ63yrX1l8KTjSNFJrCqNDOxmYiqB9d-xWq4M5WnbGsAwbrYQHt6xxgHLFsjh4CIyglV02-bngzVmbUU_n2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک زن ۳۱ ساله به نام پروین الله‌دینی بامداد ۱۶ تیرماه در محله هشت‌بنگله شهرستان مسجدسلیمان به ضرب گلوله کشته شد.
متهم که از آشنایان او بوده، پس از ورود اجباری به منزل، مقابل چشمان دختر ۱۲ ساله مقتول به او شلیک کرده است.
عامل این قتل مردی به نام جهانگیر معرفی شده که پیش‌تر بارها از پروین الله‌دینی درخواست ازدواج کرده بود. گزارش‌ها حاکی است که او پس از شکستن درِ خانه، با یک قبضه هفت‌تیر وارد منزل شد و زن جوان را هدف گلوله قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77104" target="_blank">📅 15:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB9-B8CAnJC6O4JH6ZGv3LftU0zdTTtQs9l1jVy83YPiTaMoPj29stbwUx7JFk4zOyWh9szqq68p_fpJvrlwLGWGNWS5lFEWfQ9hmNLu0uH_4TKN6AwSE2nNV-h66gSangTiIIzhc5D_qiEHAUw7iObRj8GJRC5kCwzd4PQ_qTvdAvDB6rh3D-BE0ouATxDYPYNOMDcQFr-YrOzeU2SvI_geTP-Mr3av3brBGtW_OxhqNuphYOhZc1HBNJtSuDmKrob0INrytroxWcod6GNXSmovMGfOZIl3fkrQl7hxkbg1kNfh2wu17SCZn-8o_WS7gL4dC64yrPrJrjqreO2aqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های هند به نقل از خانوادۀ خدمۀ هندی گمشده در جریان حمله به یک کشتی قبرسی در تنگه هرمز، گزارش دادند که جسد او پیدا شده است.
این تبعۀ هند با نام هرامب کارمارکار، مهندس دریایی شاغل در کشتی کانتینری «جی‌اف‌اس گلکسی» بود که سه روز پیش هدف حملۀ سپاه پاسداران قرار گرفت. در جریان این حمله ۱۱ نفر هندی دچار حادثه شدند که ۱۰ نفر آنها نجات پیدا کردند.
سپاه پاسداران انقلاب اسلامی در بیانیه‌ای با تأیید حمله به این کشتی گفته بود به دلیل «حرکت در مسیر غیرمجاز و نادیده گرفتن هشدارهای مکرر»، با موشک به آن حمله کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77103" target="_blank">📅 15:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsM_uHiPUO0FBVfeuErbXe20vqp4HJsAErj0zUPXBggXVb5UKBB8yP2C2EcK-_7C5BYfY6c3-4x4TgBlkU1TfqI2TxrUz9jW8A4RTr1Hu_pLW8WlqxkOloOtmVTV1njhMF5W-uBikZxLTgX94TMc7sxLlSxJUDngygaTJLeKeI3dvjWvH77G0t-30QnIvICQjSCkU3xakUF935Q0levlHYFa-2RwjU-cot20qH4ER6Gpy8mnU4AB2rGJC4Pw753SKYfFwcShSktsZhZM1KFbvMDjfCeIlmq-lDStCw0GIWe80aDdnlqNjkvEhix6h06nQ55ul4LIjnd9a_9Ew4bXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی صبح چهارشنبه ۲۴ تیرماه اعلام کرد هفت نیروی پایور و سرباز وظیفه ارتش در پی حملات آمریکا به پادگان نیروی زمینی بمپور ایرانشهر در استان سیستان و بلوچستان کشته شده‌اند.
در اطلاعیه ارتش آمده است که ارتش آمریکا «با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش جمهوری اسلامی ایران در بمپور را هدف قرار داد.»
نیروی زمینی ارتش جمهوری اسلامی تهدید کرده است که پاسخ این حملات را در زمان لازم خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77102" target="_blank">📅 15:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139d0c2397.mp4?token=tTOhf3GsKUiMr-SQfUPY0OwUK7f2AM_0rznwb9Pjqik4AHakGzI3sfYc7Y1XTF5uK1Sn61DJ4a0cT_uFIGHbX-QLql3KnP31zOqnjEABoVAnXiF_6CGn923fYKPVbtH-iDK_9OLptTN26HGBt9sza5qAiQrT3fhlCZLk0cznfk45XTFIj1WJjnpwXUn7OtbhVGcI2YoF70dcdwHzQUMuyzPxGvDMGSmrDd7AIuvFZLf3dBPGOtkSo8WBwqCF1TKPwlW9PxL4Le3hpboyw4q4o-FTv-h8W2cmfzBLOcmOWXkzJ2l01lUNuPI3SmR8NGtIbNhd_4zqUvIRyqL6fn_NRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139d0c2397.mp4?token=tTOhf3GsKUiMr-SQfUPY0OwUK7f2AM_0rznwb9Pjqik4AHakGzI3sfYc7Y1XTF5uK1Sn61DJ4a0cT_uFIGHbX-QLql3KnP31zOqnjEABoVAnXiF_6CGn923fYKPVbtH-iDK_9OLptTN26HGBt9sza5qAiQrT3fhlCZLk0cznfk45XTFIj1WJjnpwXUn7OtbhVGcI2YoF70dcdwHzQUMuyzPxGvDMGSmrDd7AIuvFZLf3dBPGOtkSo8WBwqCF1TKPwlW9PxL4Le3hpboyw4q4o-FTv-h8W2cmfzBLOcmOWXkzJ2l01lUNuPI3SmR8NGtIbNhd_4zqUvIRyqL6fn_NRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
صدای انفجار در شیراز مربوط به عملیات معدنی کارخانه سیمان بود
🔹
صدای انفجارهایی امروز در برخی نقاط شهر شیراز شنیده شد.
🔹
براساس اخبار رسیده به خبرنگار مهر، این صداها ناشی از عملیات انفجار کنترل‌شده معدنی در محدوده معدن کارخانه سیمان شیراز بوده است.
🔹
بر اساس پیگیری ها این انفجارها در راستای فعالیت‌های معدنی و برداشت سنگ در محدوده معدن کارخانه سیمان شیراز انجام شده و با هماهنگی‌های لازم و رعایت الزامات ایمنی صورت گرفته است.
🔹
شنیده شدن صدای انفجار موجب نگرانی برخی شهروندان شیرازی شده بود که بررسی‌های انجام‌شده خبرنگار مهر نشان می‌دهد این صدا ارتباطی با حادثه یا رخداد امنیتی نداشته و مربوط به عملیات برنامه‌ریزی شده معدنی است.
پیام‌هایی که من دریافت کرده بودم:
انفجار وحشتناک شیراز ساعت ۱۳:۱۷ دقیقه
وحید یک صدای عظیمی اومد الان شیراز
شیراز
همین الان ساعت ۱۳:۱۸ صدای سهمگینی اومد
من سمت زرگری هستم
درود وحیدجان
۱۳:۱۸ شیراز سمت ما یک صدای شدید امد، فکر کنم زدن، چون چندتا از دوستامم از جاهای دیگه شنیدن صدا رو
انفجار اطراف دلیران تنگستان شیراز ساعت ۱۳:۱۷
سلام شیراز  ساعت یک و نوزده دقیقه صدای توافق اومد، جاش رو نمیدونم ولی صدای مهیبی داشت
وحید جان کارخونه سیمان شیراز رو ساعت ۱۳:۱۹ دقیقه زدن
ساعت ١٣:١٠ صدای انفجار سمت محله فرهنگیان شیراز اومد. برق هم که نداشتیم از قبلش
سلام وحید جان شیراز یه صدای  دور امد که شبیه برخورد موشک بود ۱۳:۲۰
سلام شیراز یه صدای انفجاری اومد
طرفای صنایع صدای انفجار مهیب
صدای انفجار در شیراز مربوط به عملیات معدنی کارخانه سیمان بود
من که این قسمت شهر زندگی میکنم هر از چند وقت، محدوده معدنی کارخونه سیمان انفجارهایی دارد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77101" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77100">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNqNa0dyWsUDR5yLc_Cf_19iZEDoRjsAdAZv67v2MNCJS3ac88ACobyoBqone9yNtvY81m9mcVEtd5sz4A4CAl3EaCCTyXWd0gGCzFtnvSNWenfmwWe1Qp0WIKxzW3SkNPSOUiC3PgdxP7FGQ5319BxQkZ78_wEP0mPHyV1FRKL5bKRS204-MH3VDZVupY0DPqNfaq1d3a3bunN9D27nv4GhuAcFuSt5uz7bjqzBOJkX7b9i3xpUv51C-hPDvb0E2IcIJrbGhuj5CwPM6YU3Rh9e_EuXFYdXD6hUcI6WWsTp9O3nGAmxpY7uhWsXliksGJylU0BvP4bh6H1EUDj0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ارتش ایالات متحده، سنتکام، بعدازظهر چهارشنبه اعلام کرد که نیروهایش از ساعت شش صبح به وقت شرق آمریکا (۱:۳۰ بعدازظهر به وقت ایران)، موج دیگری از حملات علیه ایران را آغاز کرده‌اند.
در بیانیهٔ سنتکام آمده که این حملات با هدف تضعیف بیشتر قابلیت‌های نظامی ایران در حمله به کشتیرانی تجاری در تنگه هرمز انجام می‌شود.
دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه،‌ ۲۴ تیرماه، به برنامۀ «گزارش ویژه» شبکۀ خبری فاکس‌نیوز گفت دور جاری حملات به ایران «تا زمانی که من بگویم، ادامه خواهد داشت».
او تاکید کرد: اگر تهران توافق را نپذیرد، هفتۀ آینده حملات را به نیروگاه‌ها و پل‌های ایران گسترش خواهد داد.
او گفت: «هفتۀ آینده وضعشان واقعاً بد خواهد شد؛ چون نوبت نیروگاه‌ها می‌رسد؛ نوبت به پل‌ها می‌رسد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77100" target="_blank">📅 15:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLqeHBXcjolQ52aSKX-TKCL0sOieUzYaRFhO9w3klNUvkz3JdssN92hDuEHsGytxwdGjRjeFw14PHnoZXghjFoJJPcaAdmp7ETe3Whc93yWteq4FR_mjl8YteZyuvi-NzCJ3dMTYc3Gzt5HecDkUssy90cA2tv3g5vCuk9sUE0D-6DiP_4BHb0u4fkb-YmbaH-fs-7xv5nsequm5aIO1dcYNq1Vhlm5Ups6J7uicvs8cKhmoMkjYln-PLTpWGzsLqITaGa5AJ5sCriCCJ5lnWGVAPRESpioaOQwlx1HDF2wU-x-cpndlojUXA57R_4vWSTg-6u-LhxZbGc5Mm-osYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77099" target="_blank">📅 15:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77098">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M90FjG9-8MmEP9J2kXEeXD_wnFXqM-8aiva_vgAiVlQYeXTF1R3Q8-zfn2MTzTtAr-E1dd-Hr67toM0MW0T9i3lqbgn1CS7nW3jJYzURNgbxM6sh_FqUl8XPiM27Qx4_BtgEMMtBXJX5Ka6Vucrmx8yI6nbTOUeOZHDUTqPNI76VQxMAWyOiwiqGRk8EBjnIFG8nCTjmNdLFi3Jjl3cHZvh2AnkY76i8QrvwnQs2qoyxk1kza-Fmk7Jod19kx4q0UK503sVzWOwp7Ysrvl1-fdytdgtLqBdhCZYBH7Gunj3Sjd0TOgnZBRaWU4KDJAgiwcSql_0z6OZXn5xtdt6S0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M90FjG9-8MmEP9J2kXEeXD_wnFXqM-8aiva_vgAiVlQYeXTF1R3Q8-zfn2MTzTtAr-E1dd-Hr67toM0MW0T9i3lqbgn1CS7nW3jJYzURNgbxM6sh_FqUl8XPiM27Qx4_BtgEMMtBXJX5Ka6Vucrmx8yI6nbTOUeOZHDUTqPNI76VQxMAWyOiwiqGRk8EBjnIFG8nCTjmNdLFi3Jjl3cHZvh2AnkY76i8QrvwnQs2qoyxk1kza-Fmk7Jod19kx4q0UK503sVzWOwp7Ysrvl1-fdytdgtLqBdhCZYBH7Gunj3Sjd0TOgnZBRaWU4KDJAgiwcSql_0z6OZXn5xtdt6S0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#چابهار
، چهارشنبه ۲۴ تیر، ساعت ۵:۳۰'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77098" target="_blank">📅 08:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67211d7671.mp4?token=tRsWpfEbP2JpGj51AUNxhrlrVxRC_ghEXb1gGobRX-A-77xOD8rmUItFTYPuadOtEhsfi6_Ayy-diedWSn2N8qweYCqHwAdr7RHoh5z8xgCwbmnsy-i8zzCBy9ZYHiXUvmGUpd19sbwAKwOFE3RuwokZNhZNN0lKhACG7oz3FNVqqr_agEXHioiXfq_fsT6aLbf4M8kL8C_0QHk4vjf0LgNVskKRImeohxgswCyzlC6Eog0yScRAfMUooRgSumWXoOuVajnXZ9afoQf5s6NGRzMeIUH9tSN-WSxyhyTTUeGc66LrlNVux9IPp5DvVF9smh9wo8-2qU-LMwGESOJ0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67211d7671.mp4?token=tRsWpfEbP2JpGj51AUNxhrlrVxRC_ghEXb1gGobRX-A-77xOD8rmUItFTYPuadOtEhsfi6_Ayy-diedWSn2N8qweYCqHwAdr7RHoh5z8xgCwbmnsy-i8zzCBy9ZYHiXUvmGUpd19sbwAKwOFE3RuwokZNhZNN0lKhACG7oz3FNVqqr_agEXHioiXfq_fsT6aLbf4M8kL8C_0QHk4vjf0LgNVskKRImeohxgswCyzlC6Eog0yScRAfMUooRgSumWXoOuVajnXZ9afoQf5s6NGRzMeIUH9tSN-WSxyhyTTUeGc66LrlNVux9IPp5DvVF9smh9wo8-2qU-LMwGESOJ0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰ شب به وقت شرق آمریکا در ۱۴ ژوئیه، دور دیگری از حملات علیه ایران را به پایان رساند و ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار داد.
جنگنده‌ها، پهپادها و شناورهای نیروی دریایی آمریکا در جریان این موج حملات هفت‌ساعته، مهمات هدایت‌شونده دقیق را علیه سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی و سامانه‌های دفاع ساحلی به‌کار گرفتند تا توانایی ایران برای تهدید کشتی‌رانی تجاری و خدمه غیرنظامی را بیش از پیش تضعیف کنند.
این حملات در همان روزی انجام شد که نیروهای آمریکایی محاصره دریایی علیه شناورهای در حال تردد به مقصد یا از مبدأ بنادر و مناطق ساحلی ایران را از سر گرفتند. این محاصره امروز از ساعت ۴ بعدازظهر به وقت شرق آمریکا به اجرا درآمد.
نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که فرمانده کل قوا دستور دهد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/77097" target="_blank">📅 06:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZzXkNhwf79rdmGV-KD8XE1zvuL3GK75xTzCkMrf8BF60lH_sHzn0NUpGeZuMHOc2BM4OZ9vosGaxFteD7JloYIQBYgJqA-NBmODkVMgcT1QcOjxZRjc1l7Od9qsCmbpA7Y_jWZDlx-qHyRZLW1Up6aO4fu6JmMFEcTSRhKUg1WUSBrKXoOnwRXw5JYv353BpVLKIxxl_fgkoMJf5XLoDuHbx7PRuG-hIflx-aMjfiejHY7pJTcucsIq6AFXRyctv4xjee1SJDrXdN6x745UzrDTTaA0y-E5jLX0bMXnKYap5xYhguJht2S5yBEylmnLMFgkmOAZ68LWeNEsXNG17Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYohBY3S2l8entr6dTg-bUSc7TJfuIYCGDaH_-L0hvXICVyuCP8YBAw12glniboN0hOsYLD4a-Q3ZzLhxjMtkWmUJw9vkimy6v56nzPOAuzJLhGRlo-3KJ2YGnRlrf9-arcDVqf3WNEirakC4cRp0gqqldz7edKPnGh6RyrJJJJgm9Kktw4H6IE_FBtN-8y6gcYnGcFQGY72WXO4KdlLD7aC4BDqXlwSV0qYXtvgGJ8NtkzjM2tTF8VFL9eLrnGngi5Sk1GuTu33qTrBK6Tb1k6YpekJf9cEQ2ZpuqCCFdRjLYA2Y1eYRKi3sQ0Ur9vIOllEH4s2IasfjRlnhkuLJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=aF5qaVS3pmUUKd7lHZvKVfgO9NXO0s1wsvR0NKhQvoQ1HULDAGZads5he0pl6J7Hulq1ZBKnk-v5v8650Rgigmi-bWpQXID9g225cp8PeNXWhb519fne4dssu_CYV0fgNSd-31ERUu6tdzOk4RxwVPD1JA9BotQFGoM8fI-cd1oAspvluGTEt9a7BsMlUE7xM8IUP4Jk8qT_K_XJL72zKm1WKWIs6T3eLVMtA2glx0buLARvvS-PEZvMoMJtv5G8sFZN-qe6n-_XFXRs9mK2IuG-R12CIJuieU_vAtaJeDmf_lBpoO4-9WVbvo79Tm_OARNJ6mqtyUEAqqVYgPlMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=aF5qaVS3pmUUKd7lHZvKVfgO9NXO0s1wsvR0NKhQvoQ1HULDAGZads5he0pl6J7Hulq1ZBKnk-v5v8650Rgigmi-bWpQXID9g225cp8PeNXWhb519fne4dssu_CYV0fgNSd-31ERUu6tdzOk4RxwVPD1JA9BotQFGoM8fI-cd1oAspvluGTEt9a7BsMlUE7xM8IUP4Jk8qT_K_XJL72zKm1WKWIs6T3eLVMtA2glx0buLARvvS-PEZvMoMJtv5G8sFZN-qe6n-_XFXRs9mK2IuG-R12CIJuieU_vAtaJeDmf_lBpoO4-9WVbvo79Tm_OARNJ6mqtyUEAqqVYgPlMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح:  انفجار حمله به چابهار حدود ساعت ۵:۳۰
چهارشنبه ۲۴ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77092" target="_blank">📅 06:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YI9iA-kGZSAFYvvz8a14lI0c_wa5hp6nHxU2nTmpDc3vbk_DCIF9LVzvOXyxH5vrG4Z_F2CWEyRnBz6ut0I5CYlEqzPojOtUGEP1DTns5Wn8I6Ju-HTwkavhpq8A0E4Dx_9mqjTXj2QrWHKC_2BDrpLjqsZb7e-ydSNMgLLCew26xXXbwhHHX6ALc4jBr1JAQmmjETDG5Ct6w_maBRdnHVeCnfioJmF4PTSPqdLsqhiqjm9UDIXeRh32soEaLBpwjYrpkp3ZSQyc2dZk3ThGyzKsDsxnBTCbwq2oLuuJA2txTaz0wWMS22r1pFH9iw-bR7sml9n10I1To71y8k1P2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از سیستان و بلوچستان:
چابهار پایگاه مستقل امام علی همین الان دوتا زد
سلام کنارک الان دو تا زد
سلام همین الان صدای چهار انفجار در کنارک
۵:۳۰ دقیقه چابهار سمت دریا کوچیک فکر کنم زدن. صدای جنگنده ها میومد.
ساعت ۵:۲۰ صبح جنگنده وارد حریم چابهار شد پایگاه امام علی و کنارک زد
کنارک دوباره یکی زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77091" target="_blank">📅 05:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام‌های دریافتی دوباره هم‌زمان از سربندر و ماهشهر:
همین الان بندر امام خمینی‌ رو زدن سه بار
یا خدا سه تا انفجار وحشتناک سربندر
بعدی
وحید جان سلام ماهشهر صدای چندین انفجار متوالی
سلام ماهشهر الان زد نسبت به قبلیا موجش بیشتر بود
همین الان صدای شدید ماهشهر، نمیدونم کجا رو زدن
سلام اقا وحید سربندرو همین‌الان‌چهار بار زدن
ماهشهر الان ۴تا زدن
۵تا شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77090" target="_blank">📅 05:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REX8Kj31UpofN3Ug3auvkXDHXpB6hGR7Y8wztX-Cw-wK903xC8XGN-DY1sVWVm8VSZIf02B-anknAOYNTcaT0VK_XIEKYM44DOzXE7TqZYgEJx5ekVdqmkAakP0aBl2f3tXG-AYprvJq9hVOUa_bZdpB1Z2XoRl-rrWXLReT1HV9QJ9D9rsC7c6vQezl3ax2swKwIpQoCSWTfHJt30NoY-bHNjYOd1i59W8L6YD__KTefRvOkTTtT1drVe7HEwccNYYnJkIZS4y-XWxG0xzmpcCkHJkkTghQApdouhHWbAkm3GCBpUHD6faSjTmCaF2tPYM4QssZ8qJHeAY-MdOZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از پیام‌های مربوط به شهر بوشهر، پیام‌هایی از شهر جم در استان بوشهر داشتم درباره شنیده شدن صدای انفجار:
۴/۲۵ همین الان ۳موشک به فرودگاه جم برخورد کرد قبلن از اونجا موشک میفرستادن
جم بوشهر
فرودگاه جم
الان صدای چند انفجار در شهرستان جم استان بوشهر شنیده شد.
دیشب هم همین موقع صدای چند انفجار شنیده شد.
همین الان فرودگاه جم رو زدن
درود وحید همین الان جم سمت پایگاه چمران نه سمت فرودگاه توحید دوتا صدای خیلی آروم اومد بعد دود سفیدی بلند شد و نورانی، معلومه موشک خواستن بفرستن نرفته
جای همیشگی نبود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77089" target="_blank">📅 04:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر صدای انفجار همین الان
انفجار ساعت ۴:۳۸ خورموج بوشهر
سایت موشکی را زدن
بوشهر ششم شکاری هوایی [رو] زدن
ساعت ۴:۴۰
سلام وحید جان شبتون بخیر ساعت 4:41 بهمنی رو دو بار تا الان زدن و همینجوری دارن میزنن پشت سر هم پایگاه هوایی
انفجار خیلی وحشتناک بوشهر ساعت ۰۴:۴۱
وحید بوشهر ۴:۴۱ پایگاه هوایی یا دو طفلان مسلم
😂
بوشهر الان زدن ۴:۴۱
درود وقت بخیر
بوشهر همین الان یک صدای انفجار بشدت بلند اومد
سلام ساعت 4:40 صدا بزرگ انفجار از بوشهر اومد
۴:۴۰ بوشهر یه انفجار بزرگ
وحید ۲.۳ انفجار سنگین در بوشهر ۴:۴۰
وحید بوشهر ناحیه‌ی بهمنی صدای شدید انفجار
😭
😭
😭
😭
😭
😭
بوشهر زدن الان ۴:۴۰
شهر بوشهر ۰۴۴۰ زدن
سلام وحید الان بوشهر رو خیلی بد زدن مراقب خودتون باشید خیلی میزنن مراقب باشید ساعت ۴.۴۰ بوشهر بیسیم
وحید ما سنگی بوشهر هستیم صدا خیلی شدید بود درحدی که انگار صدمتر کلا فاصله داشت
بوشهر دو تا صدای بلند اطراف تنگک اومد
آقا وحید پایگاه هوایی بوشهر و زدن 4:40 صدای انفجار خیلی بلند بود
داداش بوشهر شش دقیقه پیش یچیز سنگین زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77088" target="_blank">📅 04:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=ARuA5PU5jFniL66e6yqkIrwA5rW1CY7TNh5psRR2y3tiaaBJz3u6Vw5BTLFkSUaLTkSCWRVeC-Jac4pfKs9Cf8OSof6e7Z9NIu_cl0gTMOs__srz8_D2UwRSJKCL76o_gtQtSdRtDOW9FHIXK2gVZiAXVRhm7Y__HgYxtltVN8EYeaLxMUw2L-_SEibS96UHEkTAMixmirYf2WCP-n8F8ipsRlykQlw9_czW0_9zxncQR5OBByfTx4cFX7llr7otFspfuSQUHTjhJiIJRzoM7a9VQsrVF90BuaoLIdgM0kZzzhd-Fnx4sdyITGUPSNL59B7yqOom5jZtxfgVzwBlaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=ARuA5PU5jFniL66e6yqkIrwA5rW1CY7TNh5psRR2y3tiaaBJz3u6Vw5BTLFkSUaLTkSCWRVeC-Jac4pfKs9Cf8OSof6e7Z9NIu_cl0gTMOs__srz8_D2UwRSJKCL76o_gtQtSdRtDOW9FHIXK2gVZiAXVRhm7Y__HgYxtltVN8EYeaLxMUw2L-_SEibS96UHEkTAMixmirYf2WCP-n8F8ipsRlykQlw9_czW0_9zxncQR5OBByfTx4cFX7llr7otFspfuSQUHTjhJiIJRzoM7a9VQsrVF90BuaoLIdgM0kZzzhd-Fnx4sdyITGUPSNL59B7yqOom5jZtxfgVzwBlaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
تصاویری که بنا بر گزارش‌ها پیش‌تر در جریان حملات پهپادی و موشکی ایران به کویت ضبط شده‌اند، لحظه اصابت یک پهپاد شاهد-۱۳۶ را نشان می‌دهند. آمریکا همچنان با ایران به تبادل حملات ادامه می‌دهد و اکنون اهدافی در بحرین و کویت زیر سنگین‌ترین آتش ایران قرار گرفته‌اند.
sentdefender
,
MenchOsint
ستاد کل ارتش کویت، بامداد چهارشنبه، با انتشار بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» است.
این ستاد با تاکید بر اینکه صدای انفجارهای احتمالی ناشی از رهگیری این پرتابه‌ها توسط سامانه‌های دفاع جوی است، از مردم خواست تا دستورالعمل‌های امنیتی صادره از سوی مراجع مربوطه را رعایت کنند.
@
VahidOOnLine
وزارت کشور بحرین، با انتشار هشداری فوری در حساب رسمی خود در اکس، اعلام کرد آژیر خطر به صدا درآمده است و از شهروندان و ساکنان خواست آرامش خود را حفظ کنند و به نزدیک‌ترین مکان امن بروند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77087" target="_blank">📅 04:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری جمهوی اسلامی ساعت ۲:۵۶
حمله به یک واحد تولید آب معدنی در موسیان
🔹
دقایقی قبل، یک واحد تولید آب معدنی در اطراف روستایی در بخش موسیان (استان ایلام) هدف سه پرتابه دشمن قرار گرفت.
🔹
مراد یگانه فرماندار دهلران بامداد چهارشنبه به خبرنگار ایرنا گفت که این حمله هیچ تلفاتی نداشته است.
🔹
وی اظهار کرد که در این تجاوز به تجهیزات کارخانه خساراتی وارد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77086" target="_blank">📅 03:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77085">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=Xo3Si2IVKmqHNkbKMCXecr8m0eSNayY8SmcWM9aWnLq7uc4udrj6brBIUyceIfkuwM8FLyVi1ORGHmFJgNCntBD74ky3v_Fk-d0alIE1kvefuoDYAevFentC4rx0-y-y_UWrBFUwprA3Xf1x0d8splP9lKrLmH76jx21Xco-n0DN5xyA5a1Khdz63g7FvryiItN6GGsNodYb3IZB-t2ZU6jYf2wQEs5lFNSDsh1_RXgnJvdJm7Fb2ZE9edE8c5hZ2UDOLRN9ZLOPd981sELoUUbEl4VNDKohYyvlyWseABpsLedtJgA0bFUqglCmXis_OvFH9qAO0BUNwdaBgefGMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=Xo3Si2IVKmqHNkbKMCXecr8m0eSNayY8SmcWM9aWnLq7uc4udrj6brBIUyceIfkuwM8FLyVi1ORGHmFJgNCntBD74ky3v_Fk-d0alIE1kvefuoDYAevFentC4rx0-y-y_UWrBFUwprA3Xf1x0d8splP9lKrLmH76jx21Xco-n0DN5xyA5a1Khdz63g7FvryiItN6GGsNodYb3IZB-t2ZU6jYf2wQEs5lFNSDsh1_RXgnJvdJm7Fb2ZE9edE8c5hZ2UDOLRN9ZLOPd981sELoUUbEl4VNDKohYyvlyWseABpsLedtJgA0bFUqglCmXis_OvFH9qAO0BUNwdaBgefGMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
منابع محلی از افزایش آمار مجروحان حمله به تیپ ۳۸۸ ارتش در
#بمپور
خبر دادند؛ دست‌کم ۵۰ مجروح، دست‌کم دو فوتی در بیمارستان و گزارش‌هایی از تلفات گسترده در داخل پادگان
بر اساس تازه‌ترین اطلاعات دریافتی،
تاکنون دست‌کم ۵۰ مجروح به مراکز درمانی، به‌ویژه بیمارستان خاتم‌الانبیا ایرانشهر، منتقل شده‌اند و حال هفت نفر از آنان وخیم گزارش شده است.
به گفته منابع حال‌ وش: «از میان مجروحان منتقل‌شده به بیمارستان، تاکنون دست‌کم دو نفر بر اثر شدت جراحات جان خود را از دست داده‌اند و وضعیت هفت نفر دیگر نیز بحرانی است. روند انتقال مجروحان همچنان ادامه دارد.»
منابع افزوده‌اند: «همزمان گزارش‌های متعددی از داخل تیپ ۳۸۸ حاکی از آن است که
شمار کشته‌شدگان در محل حمله بسیار بیشتر از آمار منتقل‌شدگان به بیمارستان است و ده‌ها نفر در داخل پادگان جان خود را از دست داده‌اند.
با این حال، به دلیل محدودیت‌های امنیتی و جلوگیری از دسترسی به محل، امکان راستی‌آزمایی مستقل این آمار تاکنون فراهم نشده است.»
به گفته منابع محلی، بخش‌هایی از آسایشگاه سربازان و سایر تأسیسات داخل پادگان در زمان وقوع حملات هدف قرار گرفته و همین موضوع موجب افزایش شمار تلفات و مجروحان شده است. همچنین تدابیر امنیتی در اطراف تیپ همچنان ادامه دارد و از نزدیک شدن شهروندان و خانواده‌های نظامیان به محل جلوگیری می‌شود.
حال‌ وش
پیش‌تر
از وقوع چندین موج حمله، شنیده شدن دست‌کم ۱۱ انفجار، ورود آمبولانس‌ها به داخل تیپ، خاموش شدن کامل چراغ‌های پادگان و انتقال مجروحان به بیمارستان خاتم‌الانبیا ایرانشهر خبر داده بود.
تا لحظه تنظیم این گزارش، هیچ‌یک از مقام‌های جمهوری اسلامی درباره آمار کشته‌ها، مجروحان، میزان خسارات و جزئیات این حمله اطلاع‌رسانی رسمی نکرده‌اند. اطلاعات منتشرشده در این گزارش بر پایه اظهارات منابع محلی و شاهدان عینی است و حال‌ وش همچنان در حال پیگیری و راستی‌آزمایی ابعاد این رویداد است.
haalvsh
همزمان با انتقال شمار زیادی از مجروحان حمله به تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش در شهرستان بمپور به بیمارستان خاتم‌الانبیا ایرانشهر،
مرکز انتقال خون ایرانشهر با انتشار اطلاعیه‌ای از شهروندان واجد شرایط خواست برای اهدای خون به این مرکز مراجعه کنند.
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77085" target="_blank">📅 03:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77084">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mgwS7WXiS0JKIsJ0Yh4pfi6nkOUWCpxJiWeEv0W_2jXZ8-18fJphOuBaN8KMLnALTIHH0C8WVzNHOtLUyTAXaRssLeFCmRGMHZxyoE47JsJ9DLsq7tPwoXP2nLiiaMkupp9cXN27BCe1dTcgjOfdvKk_paSlHwDz04wR5jV56f_PLUf6vMcTIoQ1GnwKFNy0u2j7V2KO5mOHkj66FKq5VOz4crFcnCTKMLr1MMdKQVWsm3EDTqDa9jGPbvMPBD5fHCtTL0xb_MzpQtIV7_xacK8CabwoLM-54NaMk5k-lr9s1pLAqzx5sNls2HgaAkvwPvDnUgDKHCKcHva32gCfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام، با انتشار بیانیه‌ای اعلام کرد جمهوری اسلامی طی هفت روز گذشته با حمله‌های عمدی به غیرنظامیان در سراسر منطقه، هفت کشتی تجاری را هدف قرار داده است. به گفته او، در نتیجه این حمله‌ها نزدیک به ۱۲ نفر از خدمه غیرنظامی کشته، مفقود یا زخمی شده‌اند.
@
VahidOOnLine
تصویر انگلیسی رو سنتکام منتشر کرده متن فارسی رو بالاش اضافه کردم. ترجمه ماشین:
بیانیه فرمانده ستاد فرماندهی مرکزی ایالات متحده
«ایران طی هفت روز گذشته با حمله به هفت کشتی تجاری، عمداً غیرنظامیان را در سراسر منطقه هدف قرار داده است؛ حملاتی که در نتیجه آن نزدیک به دوازده تن از اعضای غیرنظامی خدمه کشته، مفقود یا زخمی شده‌اند.
نیروهای ایرانی همچنین ده‌ها موشک و پهپاد به‌سوی کشورهای همسایه در حاشیه خلیج فارس پرتاب کرده‌اند. نیروهای ایالات متحده، ایران را به‌دلیل این تجاوز بی‌دلیل که همچنان جان افراد بی‌گناه را به خطر می‌اندازد، پاسخگو می‌کنند.»
دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77084" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=XIHm0ydQNm7x3078akVVuDlxl9M1moVy0LRhBLG7lFd9A13bRI4712jKrUoYy7cTMCxTvdHGYv-gwommpJLnz5nb0gdYOlt9FdxnVySyG5x5JW8aOwfuq-tn5iN6CnmOAaCyJoNEcADn60JOezgY7lkvvW0uuWA8H3PHhDaP4v3NwllkoeDkCxMQCk-wTsGgBuG6u-D94SB1TTpe3c4I18UsgWY0JsTxLBn2OTCZxc6bdhfzCBAM1HOKqstvsCfqToRjIBg6Dg8QNj4_wFZyeeAxJLanvRLX4dzCIxowQYNh0_pQdet_HH2sKEVwX0DYnioMMZEXWW2ylO_89iubtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=XIHm0ydQNm7x3078akVVuDlxl9M1moVy0LRhBLG7lFd9A13bRI4712jKrUoYy7cTMCxTvdHGYv-gwommpJLnz5nb0gdYOlt9FdxnVySyG5x5JW8aOwfuq-tn5iN6CnmOAaCyJoNEcADn60JOezgY7lkvvW0uuWA8H3PHhDaP4v3NwllkoeDkCxMQCk-wTsGgBuG6u-D94SB1TTpe3c4I18UsgWY0JsTxLBn2OTCZxc6bdhfzCBAM1HOKqstvsCfqToRjIBg6Dg8QNj4_wFZyeeAxJLanvRLX4dzCIxowQYNh0_pQdet_HH2sKEVwX0DYnioMMZEXWW2ylO_89iubtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Vahid
پیام‌‌های دریافتی:
وحید جان همین الان تبریز موشک زدن باز
سلام وحید از تبریز موشک فرستادن ۲:۱۰
سلام آقا وحید ساعت ۲:۱۲ دیقه از تبریز تا الان که ساعت ۲:۱۴ هستش دوتا صدای موشک اومد
سلام وحید جان همین الان ساعت ۲:۱۴ صدای های انفجار میاد از ارومیه
مشخص نیست پرتابه موشکه یا چی
پرتاب موشک از حوالی تبریز به جای نامشخص، صدای غرش خیلی شدید و بی سابقه
سلام وحید دو سه دقیقه پیش از سایت موشکی [...] دو موشک  پرتاب کردن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77083" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=M-m63Kql5Qw3ilMLGFaa332ZXTDlTRDVfc7GKfNsff_Vcd4UkUJYh8l3xyZzRJoRiusEPXeRVMUG6d2esKcTAsBMJXGPdWIwCWnxJdW54lQjHhEwogfPzLioWMEVVwkU8IICkIcVT5C7OxUqmhxKFp2z7XGg--qVSTT6Vip5BBgELwfDTO9AwQdOanGYwrVq8Lx8rYHDHlAx-RepbarU5gKRLssVAfV552Z9gkNIivHs1Roaz37bHI_r_y4tlFkJfGhx0giOayN4srQwdGiHMQLSdaJX5ZkLPaakS8iXkNOIQGcI-TuWPExkVbNrj95othIqVVi_qXMaqrnTysNKxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=M-m63Kql5Qw3ilMLGFaa332ZXTDlTRDVfc7GKfNsff_Vcd4UkUJYh8l3xyZzRJoRiusEPXeRVMUG6d2esKcTAsBMJXGPdWIwCWnxJdW54lQjHhEwogfPzLioWMEVVwkU8IICkIcVT5C7OxUqmhxKFp2z7XGg--qVSTT6Vip5BBgELwfDTO9AwQdOanGYwrVq8Lx8rYHDHlAx-RepbarU5gKRLssVAfV552Z9gkNIivHs1Roaz37bHI_r_y4tlFkJfGhx0giOayN4srQwdGiHMQLSdaJX5ZkLPaakS8iXkNOIQGcI-TuWPExkVbNrj95othIqVVi_qXMaqrnTysNKxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه، در گفتگو با «فاکس‌نیوز» در پاسخ به مجری که از او پرسید حمله‌ها تا چه زمانی ادامه خواهد داشت، گفت: «تا زمانی که من بگویم کافی است.»
او گفت آنها (حکومت ایران) هنوز تا حدودی توانایی جنگیدن دارد اما چیز زیادی برای آنها باقی نمانده است.
ترامپ در پاسخ به مجری که از او پرسید، اکنون وضعیت را چگونه توصیف می‌کند، آیا جنگ از سرگرفته شده، گفت: می‌توانید هر نامی روی آن بگذارید اما ما ضربه بسیار سختی به آنها زده‌ایم. ترامپ بار دیگر بر اهمیت باز ماندن تنگه هرمز تاکید کرد.
ترامپ در پاسخ به مجری که از او پرسید آیا جنگ از این فراتر می‌رود و اهداف مرتبط با انرژی ایران نیز در فهرست قرار دارند گفت: انرژی را برای بعد نگه‌داشته‌ام.
ترامپ افزود: امشب و فرداشب و پس‌فردا‌شب، ضربات سنگینی به آنها می‌زنیم و هفته آینده برای آنها خیلی بد خواهد شد. هفته آینده نوبت نیروگاه‌ها و پل‌ها است.
رئیس‌جمهوری آمریکا گفت: هفته آینده همه پل‌ها و نیروگاه‌های آنها را از بین می‌بریم مگر اینکه پای میز مذاکره بیایند.
رئیس‌جمهوری آمریکا پیش‌تر نیز این تهدید را مطرح کرده بود اما پس از آن اعلام شد که مذاکرات از سرگرفته می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77082" target="_blank">📅 01:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77080">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=tVdMLDni7if4cKteHFsUk5NsxUsdtO-ZAjzyrtfVxVuzWs_Ern9DRuAs2c2epsW6fJ55ZJo7KUcNfdntmKoEFRpn8ROmOqHxX5m-zbWYTtt5w1H_lANVvD_mpYT-S7GRudsUlEfQiFtYLpm83s_k6-jdhCyxeDg7YND7saGqSPIraUqGLXnvM5phubX00oEi1g5DJbaCG5WxP1GsHY5NgUwoPTcm1caCedshNiSdVsx6ELyTPvF6dp11O1AUKCmiYGeDxMz8Gua55_uADkStXyjaqDe485VvmTV8D0uqsf8YCu6vXe5-tVKzSyX4uUwPOLi6OCks0BmZO7PvPmm90w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=tVdMLDni7if4cKteHFsUk5NsxUsdtO-ZAjzyrtfVxVuzWs_Ern9DRuAs2c2epsW6fJ55ZJo7KUcNfdntmKoEFRpn8ROmOqHxX5m-zbWYTtt5w1H_lANVvD_mpYT-S7GRudsUlEfQiFtYLpm83s_k6-jdhCyxeDg7YND7saGqSPIraUqGLXnvM5phubX00oEi1g5DJbaCG5WxP1GsHY5NgUwoPTcm1caCedshNiSdVsx6ELyTPvF6dp11O1AUKCmiYGeDxMz8Gua55_uADkStXyjaqDe485VvmTV8D0uqsf8YCu6vXe5-tVKzSyX4uUwPOLi6OCks0BmZO7PvPmm90w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
ویدئوهای جدید از حملات و انفجارهای شدید در محدوده تیپ ۳۸۸ ارتش در شهرستان بمپور
بامداد امروز چهارشنبه ۲۴ تیرماه ۱۴۰۵، ویدئوهای جدیدی از حملات و وقوع چندین انفجار شدید در محدوده تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش، واقع در نزدیکی روستاهای ریکپوت و کلاهدوز از توابع شهرستان بمپور ، به دست حال‌ وش رسیده است.
به گفته منابع حال‌ وش: «در این ویدئوها، صدای انفجارهای پی‌درپی و نور ناشی از اصابت‌ها در محدوده این مرکز نظامی مشاهده و شنیده می‌شود. شدت انفجارها به اندازه‌ای بوده که صدای آنها در روستاها و مناطق اطراف نیز شنیده شده است.»
منابع افزوده‌اند: «حملات در چند نوبت انجام شده و ویدئوهای تازه، بخش‌هایی از لحظات اصابت و انفجار در محدوده تیپ ۳۸۸ ارتش را نشان می‌دهد.»
حال‌ وش پیش‌تر گزارش داده بود که حوالی ساعت ۰۰:۰۵ بامداد، دست‌کم هشت انفجار شدید در محدوده روستاهای ریکپوت و کلاهدوز شنیده شده و منابع محلی از هدف قرار گرفتن تیپ ۳۸۸ پیاده مکانیزه شهید حیدر شهرکی خبر داده بودند.
تا لحظه تنظیم این گزارش، اطلاعات دقیقی درباره میزان خسارات و تلفات احتمالی منتشر نشده و مقام‌های جمهوری اسلامی نیز درباره جزئیات این حملات اطلاع‌رسانی رسمی نکرده‌اند.
haalvsh
لوکیشن دریافتی تایید نشده:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77080" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">در میان رگبار پیام‌های اهواز سه پیام متفاوت درباره جاده تهران-قم حوالی فرودگاه داشتم که نمی‌دونم چقدر درست هستند. هرچه صبر کردم پیام دیگری نیومد ولی اون اطرف کلی نقطه نظامی در بیابون هست که لابد کسی بهشون نزدیک نیست:
پیام ساعت ۲۳:۲۰
هم اکنون انفجار فرودگاه امام خمینی
صدای انفجار دور بود ولی لرزشش احساس شد
در پی مکالمه اضافه کرد: من اطراف فرودگاه هستم. چون اینجا بیابونه و نزدیک ترین لوکیشن بهمون همون فرودگاه هست اون  رو گفتم
پیام ساعت ۲۳:۲۳
سلام وحید جان جاده قدیم قم نزدیک اتوبان غدیر هستم صدای انفجار و لرزش اومد
زدیم ماشین رو بغل
پیام ساعت ۲۳:۲۶
سلام حسن اباد فشافویه نزدیک فرودگاه امام میشه صدای انفجار شنیدیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77079" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RykkYZQolFoPfAnf5MyONhBYAu8EpeXI0-v0DdaQD50pBxshWkn41CcsTLBBWCNxdMxSgrchhCpRbGjy0wd7l_95EGhN_eIlWxy_kqatcX9syybP9ERlXSAFa2v1Y7pCxPQb6IczT-sSyzvY-25V4xePZ1GQ0L3wJpdZx5c0vGHRhMHBk2ZSmShhH6m6EH-s4GcRSuh4CVU79T-j1-3FS8Fw2AlUCsD6ux0kE6Khl1ZJxLw8m5xsTrmYmGe5lTc1Jp3AdsJSJboQ6go2ghIXxIpwU5X8VsMqEH8p25cgROOAuPznUtsY1gdFxPzOcwIZXyxiAfR95xhAAza58DyIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، [
در پستی تازه
] اعلام کرد نیروهای آمریکایی از ساعت ۴ بعدازظهر به وقت شرق آمریکا [یعنی دقایقی پیش]، محاصره دریایی کشتی‌های در حال تردد به بنادر و مناطق ساحلی ایران را از سر گرفته‌اند.
سنتکام در پیامی در شبکه اجتماعی ایکس، این اقدام را پاسخی به آنچه «حملات اخیر و غیرموجه ایران به کشتی‌های تجاری و خدمه غیرنظامی» خواند، توصیف کرد و افزود آمریکا جمهوری اسلامی را مسئول این حملات می‌داند.
بر اساس این بیانیه، در حال حاضر بیش از ۲۰ ناو جنگی نیروی دریایی آمریکا و صدها هواپیمای نظامی در سراسر خاورمیانه مستقر هستند و نیروهای آمریکایی «هوشیار، آماده و دارای توان رزمی» باقی خواهند ماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77078" target="_blank">📅 23:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۳:۱۸ یه انفجار دیگه
ساعت 11.19 اهوازو زدن
۲۳:۱۹ ، اهواز صدای انفجار اومد
وحید جان سلام
دوباره اهواز روزدندساعت ۲۳:۱۸
ساعت ۲۳:۱۹ اهواز صدای انفجار
سلام وحید جان 11:19 اهواز، زدن
اهواز الان زد سه راه باهنر موجش اومد ۲۳:۱۹
همین الان ۲۳:۱۹ اهواز دوتا پشت سرهم
ما کمپلوییم! خیلی نزدیک بود فکر کنم لشگر ۹۲ زرهی بود!
سلام اهواز صدای انفجار نمیدونم کجا ساعت 11:19
اهواز  الان  ۲۳:۱۹
سلام ما باهنر اهواز هستیم با اینکه کولر روشنه و فوتبال میبینیم ولی صدای دو انفجار حدود ساعت ۱۱.۲۰ شنیده شد
و کلی پیام مشابه دیگر که بعضی‌هاشون فقط نوشتند: همین الان یا دوباره
که چون ساعت و دقیقه نمی‌نویسند نمی‌دونم کدوم باره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77077" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در بهبهان
بهبهان رو چند دقیقه پیش زدن خوابگاهمون کامل لرزید
سلام
چند دقیقه پیش شیشه های خونه وحشتناک لرزید
نمیدونم انگار تو شهر رو زدن
بهبهان زندگی میکنم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77076" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SVjNLoy6DmRuDn9HJ9HbrlGtAPqyHzxcQ0lvy2hq9vhfD2NIyP2YUygUvCexHQafBu7l7IRnUuPYV5F1QpqgHe9IdjJscx5pVvr06C3qr3zKrO0P8qe9aMrIhuC9tEivfhOwwvVjJxKx69uOo2uls9H-xQai0sO97K9OHDuQhsLd9SlmJFYdpn_VUlyEUQFj0quShRD9E2_M_fmYj9KHtbFVSD1rgr0WVTlZt829t6-oMZh9FP1U-TX60_I6fujGqMJRiMQi9V6m03cqRNxpR4u4BAIVRmkZvVfHLV32SoytDi-LlAOVEeMmsRKmmxHUBSmCCFFC_0LDr-Hgf4jw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ تهران]، نیروهای فرماندهی مرکزی ایالات متحده دور دیگری از حملات علیه ایران را آغاز کردند تا به تضعیف توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شود، ادامه دهند.
این حملات در حالی انجام می‌شود که نیروهای آمریکایی خود را برای ازسرگیری محاصره دریایی بنادر و مناطق ساحلی ایران آماده می‌کنند. این محاصره از ساعت ۴ بعدازظهر به وقت شرق آمریکا [۰۰:۳۰ بامداد چهارشنبه] به اجرا درمی‌آید.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77075" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
بندرعباس ۲۲:۴۴ صدای چند انفجار
بندرعباس ساعت 10:45 چهارتا صدای انفجار اومد
چند انفجار ممتد ساعت ۲۲:۴۵ بندرعباس موجش زیاد بود
ساعت ۱۰.۴۶ صدای انفجار خیلی بددد تو بندرعباس
درود وحید جان بندرعباس سمت باهنر چهارتا انفجار شدید بود
🔄
سلام بندرعباس انفجارهای پشت سر هم سمت منطقه۴  ۲۳:۰۸
بندرعباس ساعت 11:08 دوتا صدای انفجار دیگه اومد
ساعت ۲۳:۰۸ بندرعباس ۳ انفجار
باز بندر رو زدن 23:08
دو سه تا انفجار مهیب ، لرزوند ساختمان رو
۲۳:۰۸ صدای دو انفجار شرق بندرعباس
سلام آقا وحید بندرعباس دوتا صدا پشت سر هم اومد ساعت 23:08 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77074" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۲:۳۰ صدای ۲ انفجار
سلام اهواز رو الان زدددد
سلام وحید جان اهواز ساعت ۱۰:۳۰ صدای ۳ انفجار مهیب
همین الان اهواز صدای دوتا انفجار اومد
اهوازو زدن
درود وحید جان همین الان  صدای دوتا انفجار اهواز شنیدم. ساعت 22:31
اهواز ساعت ۲۲:۳۰
۳ تا انفجار
سلام وحید الان اهواز [رو] زد ۳ تاشو من شنیدم۲۲:۳۲
سلام اهواز [رو] همین دو دقیقه پیش دوبار زدن
سلام وحید جان اهواز همین الان دوتا صدا انفجار اومد. زمین لرزید.
ساعت ۲۲:۳۱ دوتا انفجار اهواز
سلام اهواز [رو] زدن خونه لرزید
سلام وحید اهوازو زدن ساعت ۱۰ نیم دو تا
سلام اهواز دو انفجار شنیده شد
وحید جون 2 انفجار اهواز 22:31
انفجار مهیب همین الان در اهواز صداا از سمت غرب اهواز بود. اونقدر شدید بود که زمین لرزید
سلام الان اهواز سه تا انفجار شنیدیم
سلام آقا وحید اهواز الان زدن صدای 2 انفجار نزدیک خونمون صدا مهیب بود
سلام وقت بخیر اهواز سمت کیانشهر صدا اومد ۲تا صدای زیاد
ب[ذ]ار فوتبال نگاه کنیم جون مادرت ۱ ساعت
🔄
۱۰:۳۵ دوتا انفجار دیگه اهواز
سلام اهواز [رو] زدن خونه لرزید
یکی دیگه زدن
۱۰:۳۵ دوتا انفجار دیگه اهواز
اهواز رو الان دوباره زد
هنوز اهوازو دارن میزنن ۲۲:۳۵
همين الان ١٠:٣٥ مجددا دو بار صداى مهيب توى اهواز
ساعت ۲۲:۳۴
۲ تا دیگه انفجار شدید اهواز
اهواز  . از ساعت ۱۰:۳۰ تا الان ۴ تا صدای انفجار
ما کوی نیرو هستیم اهواز
صدای دو انفجار اومد
حدود دو دقه پیش
وحید اهواز رو دوباره زد ساعت ۲۲:۳۵
سلام ساعت ۲۲:۳۴ سه انفجار در اهواز
همین الان اهواز برای بار چهارم انفجار مهیییب
با اینکه کولر روشنه ولی صداش خیلی بلند میاد
اهواز ساعت 20:37 چند انفجار پشت هم
۳ یا ۴ انفجار ، صدا از سمت ارتش 92 زرهی بود
صدا سمت  زرگان  کوروش کوی عابدی کم تر و بیشتر سمت کمپولو هست احتمالا لشکر باشه
سلام وحید جان.
تا ۲۲:۴۵ صدای ۵ انفجار شنیده شد که یکی از باقی بسیار صدای بلندتری داشت برای مایی که در نزدیکی پایگاه گلف و الحدید هستیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77073" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQSvNuP-zXBQoK1mKPmnPkRV859opmOkXKDG3-zbsuIayxpO-Mkj_1bml5a2_POY7tZd0wTUNzjQhdAlPM9zQ4IB0CqJRfWAVMQnJ9bEyhLqQODIGNiPpD6yIDlk0byuqxsrNX2W9I8sOsX-p1xwL21kgfWwfZAE9mM3vu1TQGAeac1LxU0UUlP4KOFnDFiuArBIXsXVUzjUrQYspcg3TdZ7FoVvz2iOwYxXBONgFdPqRDfGr6OJyKQTd3Fl9mgDD8DWtyKK1MmhuDDvLOieEVSsWseQbY7bosixm8vjhWvOfczF404xnvgqHoNXo4axUCS32N03brpevfFUqpxocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس به نقل از مقام‌های آمریکایی و اسرائیلی گزارش داد که رئیس‌جمهور آمریکا روز پنج‌شنبه در یک تماس تلفنی، به نخست‌وزیر اسرائیل گفت که این کشور باید خروج تدریجی نیروهایش از سوریه را آغاز کند و او را ترغیب کرد که اقدام مشابهی را در لبنان نیز انجام دهد.
بر اساس گزارش روز سه‌شنبه ۲۳ تیرماه این وبسایت، یک مقام آمریکایی گفت دونالد ترامپ به بنیامین نتانیاهو تأکید کرده که حضور نظامی اسرائیل در خاک سوریه تنش‌زا است و می‌تواند به تشدید درگیری‌ها منجر شود.
به گفته این مقام، ترامپ به نتانیاهو گفت: «آن‌ها شما را آن‌جا نمی‌خواهند. باید نیروهایتان را خارج کنید» و افزود که همین موضوع درباره لبنان نیز صادق است.
در مقابل، دفتر نخست‌وزیر اسرائیل اعلام کرد: «نخست‌وزیر بر ضرورت ایجاد مناطق حائل امنیتی در امتداد مرزهای اسرائیل تأکید کرده است».
این تماس، یک روز پس از دیدار رئیس‌جمهور آمریکا با همتای سوری خود، احمد الشرع، در حاشیه نشست ناتو در ترکیه انجام شد.
به نوشته اکسیوس، سه ماه مانده به انتخابات پارلمانی اسرائیل که برای بقای سیاسی نتانیاهو حیاتی است، بعید به نظر می‌رسد او گام‌های مهمی برای عقب‌نشینی نیروهای اسرائیلی از مناطق تحت کنترل در سوریه بردارد یا فراتر از آنچه پیش‌تر در لبنان پذیرفته، با خروج بیشتر موافقت کند.
ارتش اسرائیل در حال حاضر بخش‌های وسیعی از جنوب لبنان و جنوب سوریه را در اختیار دارد.
اعضای ارشد دولت اسرائیل خواهان کنترل نامحدود بر این مناطق هستند و برخی حتی از ایجاد شهرک‌های یهودی در آن‌جا حمایت می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77072" target="_blank">📅 21:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSZ6Cn7CCKQks9BCUiB8I70KsJmiKqvEdXMxQOu1_F4AEmvRsNmIYDVV2NfFiQuh4UzsoE-ciAbvchWNeaIOTtrFRGRFWO0scoGWWzH_2_XY8ZWwKfnxKLySciXPBwd_VORzuqt-ICHsJHlI0g5pfVpaiEwJNBfPX8hGar0-JNmkAesdOMNUAmcb385p0oEZuA1Pw3UmTLwv9eNKkCTmQd_aji2I9Lv-WmfgYKpqWrfu62oHCyjv-_MqG2dZkQdrXEgsVmuOpMhIcpWq7rZbdi3zb706_0OC75xQ3pfKkrlLAxaHXOJN9XopirIEo-9OPhkR70kGMzdnhdhvPNoWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه عربستان سعودی روز سه‌شنبه ۲۳ تیرماه با «محکومیت و انزجار شدید» از حملات ایران به چند کشور عربی، تهران را «مسئول عواقب ادامه این حملات ظالمانه» خواند.
در بیانیه این وزارتخانه، از هدف قرار گرفتن تعدادی از پاسگاه‌های مرزی کویت، یک سکوی حفاری دریایی متعلق به شرکت نفت کویت و حملات به سرکنسولگری کویت در شهر بصره عراق خبر داده و با اشاره به حمله ایران به اردن، بحرین، قطر و دو نفتکش اماراتی هنگام عبور از تنگهٔ هرمز، از «تداوم تهدید امنیت و ثبات منطقه توسط ایران» انتقاد شده است.
وزارت خارجه عربستان در این بیانیه «مخالفت کامل» خود را با آنچه «نقض حاکمیت کشورهای برادر توسط ایران، ادامه رفتار بی‌ثبات‌کننده آن در امنیت منطقه، و نقض اصول قوانین بین‌المللی، منشور ملل متحد، منشور سازمان همکاری اسلامی و اصول حسن همجواری» خوانده، اعلام کرده است.
عربستان ضمن درخواست برای توقف حملات ایران، بر همبستگی کامل ریاض با کشورهای هدف قرار گرفته، تاکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77071" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZbZWLPfprf-m8WLcWNl9wnnVBSEVfhXBmgJGVBa6AXm7_HC5C0mQ14iK4D9pwXaCJc-aezDLPZ0xcAecmvALqlHvezyINWJNL3HzQLz-BSMG283AitViTnTg_vmrYSxld9A-K4ZAUsNQ1mMyeIHuJVHr3XhCzyQF73h5yGc1I0pcJt5GOXuf9z1rAxPTIggrCJ-Ywyc1nB0VJwqUGNG4JxtOpH9lQZShU1gLCg4-16wj4RXvxuxP4a7mZkQL2qYK5oi69gPC6v_0aaBpxF_7RWuac5UcF9zL_wxq4Hi_77NogNaRgWqGpttt6IEASbYMOu8BMDe9zG9eYIv_iEoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا عصر سه‌شنبه ۲۳ تیرماه و ساعاتی قبل از آغاز رسمی بازگشت محاصرهٔ دریایی بر بنادر و کشتیرانی ایران گفت هیچ‌کس نباید برای عبور از تنگهٔ هرمز عوارض یا هزینه‌ای دریافت کند.
دونالد ترامپ در یک نشست خبری همراه علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت که پس از اعلام قبلی‌اش مبنی بر دریافت ۲۰ درصد عوارض بر کشتی‌های عبوری از تنگهٔ هرمز، کشورهای مختلفی با او تماس گرفتند و گفتند به‌جای دریافت عوارض برای عبور از تنگه، مایل‌اند در آمریکا سرمایه‌گذاری کنند.
او با اشاره به کشورهای حاشیه خلیج فارس گفت این کشورها قرار است در آمریکا سرمایه‌گذاری کنند و فکر می‌کند این موضوع راه‌حل بهتری در مقایسه با دریافت عوارض است.
رئیس‌جمهور آمریکا با تمجید از علی الزیدی گفت اگر عراق به حفاظت نیاز داشته باشد، ما در کنار آن خواهیم بود.
او گفت ما در بخش نفت با عراق همکاری قوی خواهیم داشت و به زودی آن را اعلام خواهیم کرد. نیروهای آمریکایی عراق را ترک می‌کنند و شرکت‌های آمریکایی وارد می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77070" target="_blank">📅 20:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=V-8EyNPzOaFV2O151U5bBWVOz0oEcMzRu4UvpLgoU4EQ162yE3WyYGx93jmp0GN0PRnBg76-V_kh1UdaIsj5qJmp7P4R3YJvDGpib1YQmEKDWgsDanIzXzsn_AaoSKZTFeIGns51prpcAwK4frBUX3w3QmbOME6mCfrCTbQpp-JQa6KNHW5_sU5lRixd5O6OQiKOmdud6QCzbTBThO8PKCZdkwzHn41Xd4FByS-tL0GNowNL7kcciOsC9jhfwMfspyYXEtovp-7P2NDVe3mXdsMGwrkcPgNpMU3p2TCdEFA3VTho8NCPCXSN5-cOjBxFnoo8KBa_2UW74CUd61y42w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=V-8EyNPzOaFV2O151U5bBWVOz0oEcMzRu4UvpLgoU4EQ162yE3WyYGx93jmp0GN0PRnBg76-V_kh1UdaIsj5qJmp7P4R3YJvDGpib1YQmEKDWgsDanIzXzsn_AaoSKZTFeIGns51prpcAwK4frBUX3w3QmbOME6mCfrCTbQpp-JQa6KNHW5_sU5lRixd5O6OQiKOmdud6QCzbTBThO8PKCZdkwzHn41Xd4FByS-tL0GNowNL7kcciOsC9jhfwMfspyYXEtovp-7P2NDVe3mXdsMGwrkcPgNpMU3p2TCdEFA3VTho8NCPCXSN5-cOjBxFnoo8KBa_2UW74CUd61y42w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه ۲۳ تیر، در نشست خبری مشترک با نخست‌وزیر عراق در کاخ سفید، اعلام کرد که خاورمیانه در حال تجربه وحدتی بی‌سابقه است و دیگر خبری از ترس و وحشت ناشی از «قلدری» ایران در منطقه نیست.
ترامپ با بیان اینکه ایران پیش‌تر با رویکردی سلطه‌جویانه، کشورهای منطقه از جمله عراق را تحت فشار قرار می‌داد، تاکید کرد که اکنون توان نظامی این کشور درهم‌کوبیده شده و آن فضای رعب و وحشت از میان رفته است. او در بخشی از سخنان خود به سرکوب معترضان در ایران اشاره کرد و یادآوری کرد که آن‌ها ۵۲ هزار نفر از معترضان را به قتل رسانده‌اند.
رئیس‌جمهوری آمریکا در پایان ضمن اشاره به نزدیکی کشورهای منطقه به یکدیگر، نخست‌وزیر عراق را به عنوان یکی از رهبران بزرگ آینده در خاورمیانه توصیف کرد و افزود که این اتحاد منطقه‌ای، در سایه پایان یافتن دوران سلطه‌گری ایران، اکنون به واقعیتی دست‌یافتنی تبدیل شده است.
@
VahidOOnLine
دونالد ترامپ در نشست خبری با علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت: «نخست‌وزیر عراق در انتخاباتی پیروز شد که بسیاری تصور می‌کردند فرد دیگری برنده آن خواهد شد. من هم در این موضوع نقش داشتم و برایم مهم بود کسی روی کار بیاید که بتواند این مسئولیت را به‌خوبی انجام دهد. اکنون یک قهرمان جدید و فوق‌العاده داریم و حضور او در کنار ما مایه افتخار است.»
ترامپ افزود: «شرکت‌های نفتی آمریکا با حجمی بی‌سابقه وارد عراق می‌شوند، با این کشور شراکت می‌کنند و همکاری گسترده‌ای خواهند داشت. روابط ما اکنون به سطحی رسیده که دیگر نیازی به حضور نظامی آمریکا در عراق نیست. ما برای کمک به عراق حضور داریم و اگر لازم باشد از آن حمایت خواهیم کرد، اما فکر نمی‌کنیم چنین نیازی پیش بیاید.»
او درباره جمهوری اسلامی گفت: «ایران رقیب اصلی عراق بود و بار سنگینی بر دوش این کشور گذاشته بود، زیرا قلدر خاورمیانه محسوب می‌شد. اما اکنون ایران تا حد زیادی تضعیف شده و توان نظامی آن تنها بخش کوچکی از چیزی است که چهار ماه پیش بود. این وضعیت به عراق آزادی عمل بیشتری داده و یکی از دلایل ورود گسترده شرکت‌های نفتی آمریکا به عراق نیز همین موضوع است.»
@
VahidOOnLine
ترامپ با یادآوری دوران فعالیت خود به عنوان یک چهره غیرنظامی، گفت: «من همیشه می‌گفتم به عراق نروید و به آن حمله نکنید».
او با انتقاد از این مداخله نظامی و با اشاره غیر مستقیم به ایران، افزود: «صادقانه بگویم، آن‌ها به کشور اشتباهی حمله کردند و آسیب بسیاری به بار آوردند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77069" target="_blank">📅 20:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ESVqBCai9MhpZCaIc6TQtV4Hx_gYGsuMqskh8fW4K9RmlRFGBtIi5KnLLcIPslT6kF7bp7GrqMRYZPLQETiFvIlszNk2S44JB5A70sOi5L9vR-CfF_pUDr6qt3wq7YcuDg_DJRW9oUv4CY9x8hvkbJlPPuQXoFaW0L56uLnfXUzxgMO7tD5_008yDA1ZVUrSRIRQdPlCXfoWfnRk2r4CvYnOXWm9mnicd-ZhrjIXzcsAX4_v15BmEisfFZxylHjVBSEYokMUN6IeFCmzSB8V0G29TzTIoV0krQ05SpWaqGUS6lL2nMXxUr4duxz8wpyZ4a2r6YRb8PmHmNaggi0wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار خطر در کویت، همین الان
رسانه‌های ایران عصر سه‌شنبه بدون بیان جزئیات بیشتر از شنیده شدن صدای انفجار در اندیمشک و جزیره قشم خبر دادند.
صداوسیمای جمهوری اسلامی به نقل از استانداری هرمزگان گفته که ساعت ۱۹ به وقت محلی، «نقطه‌ای» در جزیره قشم هدف حمله آمریکا قرار گرفت. صدا و سیما همچنین از شنیده شدن صدای انفجار در اندیمشک خبر داد.
هم‌زمان، ستاد کل ارتش کویت با صدور پیام هشداری از رهگیری «اهداف هوایی متخاصم» در این کشور خبر داد.
در بیانیهٔ ارتش کویت با درخواست از شهروندان برای رعایت دستورالعمل‌های امنیتی گفته شده که صداهای انفجار احتمالی ناشی از فعالیت پدافند هوایی در رهگیری حملات متخاصم است.
خبرگزاری فرانسه هم از شنیده شدن صدای انفجارهایی در کویت خبر داده است.
@
VahidHeadline
سپاه پاسداران در بیانیه‌ای حملات شامگاه سه‌شنبه به «مواضع دشمن» در خاک بحرین و کویت را تایید کرد و گفت عملیات «نصر۲»، پاسخ به حملات عصر سه‌شنبه آمریکا به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی بوده است.
در این بیانیه آمده است، در صورت تکرار حملات، مقابله به مثل جمهوری اسلامی ادامه خواهد داشت و این «تجاوزها» نتیجه‌ای جز تاخیر در بازگشایی تنگه هرمز ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77068" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsXPYZPTdXR5qLSgcKzKsHvQPa3tBO-CsM3xnJuCjSHcWxrOxtehYI9BcsbfjePaTk_IdpZIVKtyPMH3RvFxK0m3eKlXNkhLxBgmegNGzGj8VSlM9O9yzlKjpqoNIu4bVn69HqRFjQ_xvNzRjziwUwq-EmltHkpk33-_jyQy3WjZ0ziEVNLsFnLLIRs6yWdwhGBXD323KH6ZvFFtWdTG6iEPeCrcNaAL_rBp2dwlqsLii981_kwfNm9AkGLauM5wwwRFZXs0cND66XnW03BAnad9bDATP_2ssnE-MZ3hkBSM25N6-goutRfH-Wc15ihIKB4m6vtYEv8ays8DeiK6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌ها و محموله‌های مرتبط با ایران، باز است
ترجمه ماشین:
نفت به لطف قدرت شگفت‌انگیز ارتش ایالات متحده، بیش از هر زمان دیگری در جریان است. درود ویژه به وزیر جنگ، پیت هگست، رئیس ستاد مشترک نیروهای مسلح، دن کین، و فرمانده ستاد فرماندهی مرکزی ایالات متحده، دریاسالار برد کوپر. به لطف آن‌ها و همه اعضای قدرتمندترین ارتش جهان ــ با اختلاف بسیار زیاد ــ تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌های ایران، باز است؛ و این به‌دلیل رهبری دروغگو، خشونت‌طلب و بدخواه ایران است که این کشور را به مسیر نابودی کامل می‌کشاند.
بنابراین، ما یک محاصره کامل خواهیم داشت، اما فقط علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هر چیزی مرتبط با محموله‌های ایرانی حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده با رهبران خاورمیانه،
تصمیم گرفته‌ام «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌های تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حاشیه خلیج فارس در ایالات متحده انجام خواهند داد.
این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.
همان‌طور که همه می‌دانند، ما بیشترین میزان سرمایه‌گذاری دلاری در ایالات متحده از سوی هر کشوری در تاریخ را داریم، اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهند کرد و شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطوحی تاریخی خواهیم بود؛ امری که میلیون‌ها شغل پردرآمد دیگر برای آمریکایی‌ها ایجاد خواهد کرد!
آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای بی‌سابقه. دوران کشته شدن صدها هزار نفر، از جمله ۵۲ هزار معترض، به دست ایران به پایان رسیده است و مهم‌تر از همه، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77067" target="_blank">📅 18:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77066">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4730c53847.mp4?token=TRvyFCiAdIy1VuUAqad59XQxQCqEWcxthPXtDL2ASv540xTyarbuiXNEAiG25Jzqkhp0XEmQyFoXAMXe2I7X8hG9Lsou6G-kIC39kyPJ7yrEIRWGDHNy-dOIyuBs5_MNAPSQxRQ5ghlErgcHibEjeHsYYYmamSOHtK08rCbBr1CpBsSivTbszuwX3LilBtoEyAFORIoy3lS3BLNdf4uzC8FwYpzBVaUW46wl5iFFeHt0LtBgnvBNYUqnT_iRXCi9F9QHT6ymTwveM_Ep_gWL5Pn3bDTF9AwP6LbMeVsP1DJAtSJLXpvFWJBZqVeElgChBae0zxWX8l9ReYGD9rSenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4730c53847.mp4?token=TRvyFCiAdIy1VuUAqad59XQxQCqEWcxthPXtDL2ASv540xTyarbuiXNEAiG25Jzqkhp0XEmQyFoXAMXe2I7X8hG9Lsou6G-kIC39kyPJ7yrEIRWGDHNy-dOIyuBs5_MNAPSQxRQ5ghlErgcHibEjeHsYYYmamSOHtK08rCbBr1CpBsSivTbszuwX3LilBtoEyAFORIoy3lS3BLNdf4uzC8FwYpzBVaUW46wl5iFFeHt0LtBgnvBNYUqnT_iRXCi9F9QHT6ymTwveM_Ep_gWL5Pn3bDTF9AwP6LbMeVsP1DJAtSJLXpvFWJBZqVeElgChBae0zxWX8l9ReYGD9rSenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۲۳ تیرماه هشدار داد که اگر تهران حملهٔ جدیدی به کشورش انجام دهد، اسرائیل با تمام قدرت به ایران ضربه خواهد زد.
@
VahidOOnLine
ویدیویی که دفتر نتانیاهو منتشر کرده، ترجمه ماشین:
ما برای هر سناریویی آماده‌ایم. فقط یک چیز می‌توانم به شما بگویم... نه، این را به رهبران ایران می‌گویم:
اگر به ما حمله کنید، روی آرامش حساب نکنید. تصور نکنید آنچه در گذشته رخ داد، دوباره به همان شکل تکرار خواهد شد؛ زیرا این بار، تکرار گذشته نخواهد بود.
حمله قبلی به‌اندازه کافی قدرتمند بود؛ حمله بعدی بسیار قدرتمندتر خواهد بود.
دورانی که کسی به ما ضربه بزند و ما با ضربه‌ای چند برابر پاسخ ندهیم، به پایان رسیده است. این کار را در برابر محور شرارتِ ایران انجام دادیم و در برابر هر کسی که به ما ضربه بزند نیز به همین مسیر ادامه خواهیم داد.
روش ما همین است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77066" target="_blank">📅 17:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJe2u46OYkw3MlZhU8JGI31Il35lStEJws1_ywSEwvLsAkmC8Mi6VC70IjJld6TgpisaLeQhkRX0pc3IOIsFwVovuRZEtqfQIRWGrKJk5NGuTcpDDUOnTRnggxWDScW2nC3h498MD2jMCIgOFdZVis85nZY3UfYBMOYMZQkIaDZ39Y9AFztJ118MQoRBEuc5YQkALTdNHLuOj5ThS7ABlHQJ5c5aXKwm23l8bQmkm9f_8KTWnbAfk-M0QobZ_3g6-KHIh0m2A3_VyiJXECjecRBVzEZNs2TqLPuwPfe7sKqydlOFI_bU56Ae7xFaVtSwQuLQY5Ri_AvCTJQaYadN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع ارشد در تهران گزارش داد که اگر دونالد ترامپ تهدید خود برای حمله به تأسیسات زیرزمینی موسوم به «کوه کلنگ» را عملی کند، جمهوری اسلامی «پاسخی ویرانگر» خواهد داد. این تهدید در حالی مطرح شده که کوه کلنگ طی سال‌های اخیر به یکی از مهم‌ترین و امن‌ترین مراکز هسته‌ای ایران تبدیل شده است.
دونالد ترامپ، رییس‌ جمهوری آمریکا، روز گذشته در گفت‌وگویی رسانه‌ای اعلام کرد که واشینگتن یک مجموعه زیرزمینی عمیق در ایران را به‌دقت زیر نظر دارد. او مدعی شد هرچند در حال حاضر نشانه‌ای از فعالیت آشکار در این مجموعه دیده نمی‌شود، اما آمریکا ممکن است به‌زودی «ضربه‌ای سخت» به دهانه ورودی این مجتمع وارد کند.
کوه کلنگ گزلا که در رسانه‌های غربی با نام Pickaxe Mountain شناخته می‌شود، در استان اصفهان و در فاصله حدود یک‌ونیم کیلومتری از تاسیسات غنی‌سازی نطنز قرار دارد. به گفته کارشناسان، این مجموعه به دلیل عمق زیاد و استقرار در دل سنگ‌های سخت گرانیتی، یکی از مقاوم‌ترین تاسیسات زیرزمینی ایران به شمار می‌رود.
برآوردهای فنی نشان می‌دهد سالن‌های زیرزمینی این مجتمع در عمقی بین ۸۰ تا ۱۰۰ متر و در برخی نقاط تا حدود ۶۰۰ متر حفر شده‌اند؛ ویژگی‌ای که آن را حتی از سایت غنی‌سازی فردو نیز عمیق‌تر می‌کند. به همین دلیل، برخی تحلیلگران غربی از این مجموعه به‌عنوان «دژ هسته‌ای» ایران یاد می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77065" target="_blank">📅 16:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mk7rrafp_JlirktWIdlHYPki8bKsQpvtnLPMcb24NFI_Zk2yhZ_DCJPfqF7YChNGjHdKLUTHaYkdW1GuDWUdyTbGNo3dx8xh-iTZqjfLelXgTRCyD4ylzagKH-IoPrwTALA0JWjTAnOd4OGSUFtaG4Qviw_pLzxUPgYS9t2O2SqLtGE0bQMLqMNVwrA0kJJ1F2klxBXY9nlZXioISO-3PUUYdrH0pYLMTlqwtncmEXgC_CbGBn2l_HCbDDcc675AmIjMhAdWfYiag1wv-W7IVYG1rg4LulH_GJ3Bbc6nfyQ_qEgRFUboRhVoZ81s50mxGGptk0NwiYvqOXYyr0F8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TyeUEdi48JC6hEpEnCONWLpxapvlDUMbmALxZWkUYlIPRx9O2wO3tJgCkeZmvzoaY5FjsvLw7g8smmITZRJkz9KrCM87OXNuFyGy4SPpipDot5PGQdHSygNrHAVP8dGkjVk3ccoBLNcVIyq4ZUQs2mTJ3PibSfuEcq7-F-724LZ4YFUq5-sUb-h7c0bptzBhHH6YVyAtTrku_h8zhCDzbd_rqnUEfcGXIMMlckBJqOraSg5FKkah595dzdlUj-e5yXK6oROyFcRuDlsmIXm8hwSxIKpwLihp4D2-56t8QcvwynEB4uBrk-LnMdOxcUNe8ZaAJr4u7ScjakpZdfJIwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت نفت در بازارهای جهانی روز سه‌شنبه ۲۳ تیرماه و همزمان با تشدید درگیری‌ها میان جمهوری اسلامی ایران و ایالات متحده آمریکا در تنگه هرمز از ۸۵ دلار گذشت.
@
VahidOOnLine
قیمت ارزهای خارجی در ایران در روز سه‌شنبه ۲۳ تیرماه افزایش قابل توجهی پیدا کرد و نرخ برابری دلار آمریکا به ۱۸۴ هزار تومان رسید.
قیمت سایر ارزهای خارجی هم افزایش یافتند و قیمت یورو به حدود ۲۱۰ هزار تومان رسید.
در کنار ارزهای خارجی، قیمت سکه طلا هم به ۱۸۰ میلیون تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77063" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TcIWHdEg4s8sa9K7ktZp-mJq5WAzhWchlh1IfvMZqwFWl_77RHlqHttvuE_HZw08p-MJPBmQ445LSYezAdd6WygdU4iJgoAxoZmTtjXarh_npMsm_fiJR_850lR4GRBeWzdJJ0FEC0O_uJ1PXU9-DF6GyTgqWWFwwV5VYiW4u_AjoKk-NSQv3IztG-pffnigjLcg4vYQn2K46lxZ8dz_j2t4ImSn-tZ-nYHO3KGBJQJDyZd73HVFeTjATevA5R4ZhAJb4cu9r1UhjzqkxJLRq5pn7Ue86Nu26_oxCf5KW3CgbUEezr6n5C7VdJgDDS1Hx2v_iCzFw9-sjTsnCgj1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BjTpOjxv3N3cyqsm0x4eGn1C8AD-od1_NvJUPPYo5iCpdvbQthc-LNrwTXSOjzjXhb0vuWOHi2dfRYnlWsLWk3O8xdMemcKm6M8CZUh8-VmO_IRsxtOGd3ir67wtVlMq-2i0cYMOlmcvsCtFCY-0haW16zkxPy4GT8-OpFecEnjNCtywWalLjEyMEBvgWxIgY92bMmHzAlAL06ANTDHgtdGgwSPg9DWlIGjoKh31jL2Aii-_p8sEVZplfMA3RvsngCFAQg3mes4MmUgYrnIBlHr2Z17yQVxrPTJY0VtkfkKr0CrGKo4Wi6flccHhcMLkievP7w-nft7HCesav7CSbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز در گزارشی اختصاصی که روز ۲۲ تیر ۱۴۰۵ منتشر کرد، از تلاش چندساله سرویس اطلاعاتی اسراییل برای جذب محمود احمدی‌نژاد، رییس‌جمهور پیشین ایران، به‌عنوان یک عامل اطلاعاتی خبر داد؛ طرحی که هدف نهایی آن، به گفته این روزنامه، نصب او در…</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77061" target="_blank">📅 16:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfvnmo6cYoPSRldhepLf5PxGATvtKa2vsBpMiaHl7Qsd9h74nI3TF3iZxkdCOg8orfPF_1oxF3_P0oJUWNoIE2i9h9C06cCkux5-9gqLUmx6nhIdj441NWkqktzz7unGLL3iwajS-8urNi2EyNaFb8YHEEowWC1KFiQPCXKSNzzjGbV2nMqDPztD8aqhT5KKg8ef-k7rWPimvZM72nQnqsAhuSmsSZm9KD6SYH-3CW3C9TQbQ1_HplQrBKkLRbgO6bokX_txlGsfIn-S_7st8I_ZbQmG1sFmj2dwDGzjBqreQczcz4f-EEGyovZYkDl-L2i994sZxS2qLIe31NPORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی صبح سه‌شنبه ۲۳ تیر از اعدام دو نفر به اتهام «بغی و قیام مسلحانه علیه نظام جمهوری اسلامی»، خبر داد و و آن‌ها را که آن‌ها را از اعضای گروه داعش معرفی کرد.
قوه قضاییه نام این دو را محی‌الدین عبداللهی و حسین پالانی اعلام کرده و می‌گوید آن‌ها اعضای یک «هستهٔ وابسته به داعش» بوده‌اند که در ارتفاعات بمو در نوار مرزی ایران و عراق و پس از یک درگیری که به کشته شدن سه عضو سپاه نیز انجامید، بازداشت و محاکمه شدند.
جزئیاتی از روند این محاکمه منتشر نشده و شرایط برگزاری دادگاه و دسترسی آن‌ها به وکیل و دادرسی عادلانه نیز مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77060" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=b6t8LwjEIN-L_7T5hPNM41l1dz2_oScruIrXF8EHIuFreKRwaOg9ClaPMVrKU4OE1GBEVIF74v2YhIkPe78eFnlgAhMJgQXNG7_THXL18x2sKIoE6Z2GwRXrs0RxzcJF2VJALMdVlbpGPlESj0u5Eyj2xhSU40JBYih5udRAlesJ5ciytzKxX9BSHdMYllCyKlWA-i3ukPW3HjQ8zDk9jlwbX0tfls0Gv-rNBL7JElNKjqnqt2X1TpDOI1DW-WkD0t5DCSzsL5BY2WRjAK0Qj5CcUnDtCTw0r5dmT_LHw7YKiB44P5pkWgKBJCei3XE3FeA4SmCNAY0omJ0HvElcPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=b6t8LwjEIN-L_7T5hPNM41l1dz2_oScruIrXF8EHIuFreKRwaOg9ClaPMVrKU4OE1GBEVIF74v2YhIkPe78eFnlgAhMJgQXNG7_THXL18x2sKIoE6Z2GwRXrs0RxzcJF2VJALMdVlbpGPlESj0u5Eyj2xhSU40JBYih5udRAlesJ5ciytzKxX9BSHdMYllCyKlWA-i3ukPW3HjQ8zDk9jlwbX0tfls0Gv-rNBL7JElNKjqnqt2X1TpDOI1DW-WkD0t5DCSzsL5BY2WRjAK0Qj5CcUnDtCTw0r5dmT_LHw7YKiB44P5pkWgKBJCei3XE3FeA4SmCNAY0omJ0HvElcPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتشر شده در منابع حکومتی:
'حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77059" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MxEsS7tqp0jknQlVcV4S11OlllGwv6NgBLBkc6GyGiNhSOYO31KoG60zDsHyb4qqG_wUwBgRxmBTDsAKbdb3i8NwPBkag81nIDb2cjoTcD1GTO0xQ7bJFUU2aJSa0qRBC3wmTa7QkUQpz2jqXe0oD6afAl2LKxDRCrOE8jMZv7aqV4KMcAl75FnH2aVGNpmpXknCA7tJ72FVwRuDUSl_PFhuzsE7vl3zMZTkQcS4vAuoVQ9ks1OUdGS3SESVBr6JlpzbkGvfvJFwb7JDbLuQkRoTUe_-U7vHBvJSverQBCiKlBk_pJba9xFx8mafjV2rFMsbToQ80W4DopdNA4LXoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'مرکز آماد و پشتیبانی دریابانی نیروی انتظامی بوشهر محله بهمنی، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77058" target="_blank">📅 15:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KQBakGc6dKYxZSsMJOESfJvtQcR69OCtgOeS0EY7dxUSJ8fNelcJiPrAwFTbLp_NkRzm15ProASYKgVqvWExIvlfa5uBheiguOdRYj203WJKwV0rkHZwqCmyGPP9FUU79_AEhh6dl59zSiYHGsy2xIyorbkG7wNBLy_El3eXaZzg4f0TjkqjqBENoYR2cYo3eF42RWDdpGEcQM3zXApsuxhrsmGGei7bDPT5hvVlwxD9Pi6Wgow6DXJ-OhhLnIeYt-lmzpzuIYv35Zq-w3EMkV23ZY05TGg7VC9mpwPfsC4YjqngMptUNeXDMY75kyf_eV4ZpaeuiCLdZ__wJ-T4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=Wx8OwTWwr7fwAk-0YOLjOTAJniHegyuff05FLGk5NYU5ocwbfRVA3gMgAF4Ix6gKh4S1BoskmKNB9cmjDsJKMFrzDJQPYBD2tfh96lKWEOKE_IyghsE_g4HXg0fxFt2-MzaWudCkB6qsODzR0elWE59r5nskNOdCxJ6evA0cdjGjLuauRI9FfePDPJ5h3K__LpKcSkIIXx06wT44cBqsY-U-UQfMe_7Q7VySiQ6ONal4fj_iM1JJYs4KonWWDTRnnK53SkATPNt3aueUiNCgYILKG57indJEivRDWIO5e5xVs-wIh-ISe8ZuGNFeBNAzMWwrwxJv4FSkYuyQnZGVzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=Wx8OwTWwr7fwAk-0YOLjOTAJniHegyuff05FLGk5NYU5ocwbfRVA3gMgAF4Ix6gKh4S1BoskmKNB9cmjDsJKMFrzDJQPYBD2tfh96lKWEOKE_IyghsE_g4HXg0fxFt2-MzaWudCkB6qsODzR0elWE59r5nskNOdCxJ6evA0cdjGjLuauRI9FfePDPJ5h3K__LpKcSkIIXx06wT44cBqsY-U-UQfMe_7Q7VySiQ6ONal4fj_iM1JJYs4KonWWDTRnnK53SkATPNt3aueUiNCgYILKG57indJEivRDWIO5e5xVs-wIh-ISe8ZuGNFeBNAzMWwrwxJv4FSkYuyQnZGVzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا برگزارش شهروندان از حدود ساعت ۱۲:۴۵ بار دیگر به نقاطی در
#بوشهر
حمله شده و بیش از ۱۰ انفجار رخ داده.
تصاویر دریافتی، سه‌شنبه ۲۳ تیر
#Iran
Vahid
از بوشهر پیام میدم
ساعت ۱۲ و ۴۴ دقیقه صدای انفجار امد اما کم بود
سلام وحید جان
ساعت 12:45 دوباره بوشهر رو زدن
بوشهر ساعت ۱۲:۴۵ ظهر منطقه بهمنی صدای انفجار خیلی نزدیک بود. خونه لرزید
همین الان ساعت ۱۲.۴۲ بوشهر منطقه بهمنی رو زدند(احتمالا پایگاه هوایی ارتش یا پایگاه دریایی سپاه ریشهر) زدند. صدای دو بمب شنیده شد.
سلام بوشهر ۱۲:۴۷ شدیددد صدای انفجار میاد.
درود وحید جان ،بوشهر الان دوتا محکم زدن
الان بوشهر و زد ۱۲:۴۴
به نسبت اخیر صداش نزدیک بود پس میشه حدس زد فرودگاه بوده دوباره زد ۱۲:۴۷
الان زد باز ۶/۷ تا انفجار بزرگگگ کارخانه جاته چون خیلی نزدیکه ۱۲:۵۴
۱۲:۴۷ بوشهر حدود ۴، ۵ صدای انفجار اومد. نسبتا شدید بود.
۱۲:۵۳ دوباره دارن میزنن.  حدود ۷، ۸ تایی زدن الان.
سلام   بازم بوشهر داره صدا میاد از ۱۲و ۵۲ دقیقه چندین صدای انفجار اومده
ساعت ۱۲:۵۳ دقیقه حداقل ۱۰ تا موشک به بوشهر زدن
از ۱۲:۴۰ دقیقه نزدیک به هفت هشت بار دارن میزنن بوشهر رو. خونه می‌لرزه!
وحید جان بوشهر رو ده دقیقه یک ربعه دارن همینجوری رگباری میزنن…
خیلی میزدن انفجارا همش دنباله دار بود مشخص نیست چنتا بود
حدود ۱۰-۲۰ ثانیه یه کوب صدا انفجار قطع نمیشد
وحید جان  رگباری باز بوشهر منطقه ریشهر رو زدن وحشتناک بود
ساعت ۱۲۵۸ دقیقه اسکله والفجر بوشهر را با ۸،بمب زدن، انفجار شدید
سلام ساعت ۱ ظهر صدای انفجار مداوم بوشهر
از ساعت 12:30 تا 13:15
بیش از 15 بار صدای انفجار مهیب توی بوشهر شنیده شده و موج خیلی زیادی داشته
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77054" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌های دریافتی:
باز بوشهر رو زد
سلام دوباره بوشهر رو زدن
دوبار بوشهر زدن ۶و ۷دقیقه
حدود ۶:۰۷ باز بوشهر رو زدن.
بازم زدن ولی صداش به مراتب ضعیف تر بود.
🔄
سلام وحید الان ساعت ۶.۱۳ دقیقه باز کنارک زد خیلی بد زد
چابهار ۶:۱۴ زدن
بازم چابهار همین الان ۴ تا شدید زد گفتن تموم شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77053" target="_blank">📅 06:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=keuWV3uPiKm4h3HMIEH2EY87Hd07v23yR2IpTADlnWH61aQBND_MDl6slqxhoD1e2d81jvkHbVciI899j-79_BnRA29dc81YyhjjEx68r5NzFZkTXVfce22D4oBS3aciUi6PJQ67_FXU0qyB6_pWMDTa69v02yLHTEzw_Ol7S9UCOYwno6z5KS9yOyPrdIb-DmtrefSU1cb7qp1YBOf5jl6Z-AcgMzEqsUZFxFDDOeo7ZPiJWvIwtMvM_RT6eFEp1tl8HB3bZadR3ijCF2rTJwM0pjCbAUCZ5s3eZ6AAWd6WmqaSfI5SY9MQyAlWE7XRYMDzt4cX2X8P9iSwAtClzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=keuWV3uPiKm4h3HMIEH2EY87Hd07v23yR2IpTADlnWH61aQBND_MDl6slqxhoD1e2d81jvkHbVciI899j-79_BnRA29dc81YyhjjEx68r5NzFZkTXVfce22D4oBS3aciUi6PJQ67_FXU0qyB6_pWMDTa69v02yLHTEzw_Ol7S9UCOYwno6z5KS9yOyPrdIb-DmtrefSU1cb7qp1YBOf5jl6Z-AcgMzEqsUZFxFDDOeo7ZPiJWvIwtMvM_RT6eFEp1tl8HB3bZadR3ijCF2rTJwM0pjCbAUCZ5s3eZ6AAWd6WmqaSfI5SY9MQyAlWE7XRYMDzt4cX2X8P9iSwAtClzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا نوشت: نیروهای ایالات متحده حملات جدید علیه اهداف نظامی ایران را به پایان رساندند
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) تازه‌ترین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب به وقت شرق آمریکا در ۱۳ ژوئیه به پایان رساند.
در جریان این مأموریت پنج‌ساعته، نیروهای ایالات متحده با موفقیت اهداف نظامی در نقاط مختلف ایران،
از جمله بوشهر، چابهار، جاسک، کنارک،  ابوموسی و بندرعباس
را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری را بیش از پیش تضعیف کنند. نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران را هدف قرار دادند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/77052" target="_blank">📅 06:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=RmL1grl1mzYfcMt9HbVUV2NbADNmdfnuMcDsztaNZFtbrPFOU-gnSxhmUwUU15sn35i6VR5Iks5x7ij6576v9GusfFXbs6gXvihTjDgj__GBr7vNxgfI4t3W6lRZ-aszr1gc4TFb5K4KkFtlB9DfazCDIYLr3jA12d5zCUdT1-OppdnNAIjpy7GJAnWrKF-IDK7h5NWZKihQFvGWMYcqXP9QExgVs5chCtUs2nsl3AEiU1UxzExRklAhJUOp_ATr0H_7A3iDpZDZYCiVugNQvZOLtTgWlJwE1SvqhNGaRUgnotsqlsLUYQif3_FcHycD1kCtfzv3W96Zb3VEgUKpAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=RmL1grl1mzYfcMt9HbVUV2NbADNmdfnuMcDsztaNZFtbrPFOU-gnSxhmUwUU15sn35i6VR5Iks5x7ij6576v9GusfFXbs6gXvihTjDgj__GBr7vNxgfI4t3W6lRZ-aszr1gc4TFb5K4KkFtlB9DfazCDIYLr3jA12d5zCUdT1-OppdnNAIjpy7GJAnWrKF-IDK7h5NWZKihQFvGWMYcqXP9QExgVs5chCtUs2nsl3AEiU1UxzExRklAhJUOp_ATr0H_7A3iDpZDZYCiVugNQvZOLtTgWlJwE1SvqhNGaRUgnotsqlsLUYQif3_FcHycD1kCtfzv3W96Zb3VEgUKpAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش: حملات به مقر سپاه پاسداران در سراوان
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/77051" target="_blank">📅 05:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
همین الان ساعت ۵:۳۹ صدای انفجار اومد چابهار و خونه لرزید
الان چابهار رو رو زد خیلی سنگین بود هنوز نمی دونم کجا بوده
سلام ساعت ۵.۳۹ دقیقه دو انفجار شدید چابهار
همین الان دوتا دیگه هم زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77050" target="_blank">📅 05:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام‌های دریافتی:
الان بوشهر [رو] زدن
دو بار
باز بوشهر رو زد
پایگاه هوایی بوشهر [رو] زدن سنگین الان ۵.۱۲
باز بوشهر رو زد
وحید سلام  بوشهر [رو] باز زدن 5,11
سلام بوشهررر رو زدننن
ولی الان باید بریم امتحان بدیم توی این شرایط
😐
😐
🔄
ساعت ۵:۳۷ موج دیگری از پیام‌ها رو دریافت کردم که از شنیده شدن صدای حدود ۱۰ انفجار پیاپی در بوشهر خبر دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/77049" target="_blank">📅 05:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtIMibzha64YjgatKBzmURfCCUlY2TEczJS4DKiOQRjMG0AOl8t7MTGDGiqyYITLb3io4_ZV8ZbOGEy6qLy4oaAp58UJajrjnKT1z6LIo2bnORyO8o1P_1ZVdEyZT3O1GcKjRX9YjifZqA9v_ZiJThg7Pd0wxW5viUwzKjaYtQRynJkvGJ12wSlnOrzgXaF_NIJh9mVlOpXY6ZU5H--qZMQx3mHRvBnOPCidVnBEG_vYeD5-QxYEBg8OsBHQF_61tFdSMC5WAHkOvL9jH8r1AYtqezwAHAZf-rxOAXhUUmZGwKd4ceyLFNb8Rbp1T5S9BuL0ke6zZvekMBdzgKCtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCwCZj_vgUG1FHzdDDx5I6XOgsLVJkfkhragt1rW8DNd3Cp0nbODLdcXhzjo2HBHm7xwJdlbWxiTXQ5iwrUXSJtnG-ibh4eSEHpqpUNlCWV4Hdx43KQ9S0nfbwjD7hKdCqeUS5aEDLqOb8GNBszLwQagWy4MiEI4rg6QjLxjTTqi5yH97S9ZeHYk7i0LvdRgl9ImwTmap4b4FephZpBTpZkgk0kcT7XcRimEsGR4ns1Zpk0UjI4g8vjDrPZAf-qm6lwq17DBNYxIsbj_0Qs_y-ZbQHTYqRxUi0LN_cpTvkdlGvcrG7I16tyc5_BHDAb1jPnr8_rgDmck63tgXfeoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnAa5fsdEUeXfdLgvq3x6KcZDkm-V9qJ82f1cHdvTORcyWpL5WsCTho1nYeMH-3R1D42DhUZJfh55__A35om4GXF_P_jCBjqrai27WrgFMCgtnt216HMKBf5FISA_EQ_c6BvoEZUEITB-jkdmAlBQ1M54CIFptWGrlWaq1z6fihn89cGAp7IS6hREIQp8RBmT6_0id8y28RmTlH3VRAsrhO3phnHHUyzZvnA8FpUDKw4dUrDR2TnW4RBgnEDMPH2b7m5sjl8IhYQDY5oOqYzjMSVJpHq489wHc8E9S5E0fgIiyXGycMk_hLQPnOqI7pxtsK9jA-Y2fGeCCa5zwlJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8E1g85biwvgjO-MIX3UDpnbfRgOrXhZmsw8Qg_zRuK5V9-Cddo0nPhWdQEIgQFQ-2AWIeUU5C39wkbaME7io-L5E1zvC26XsiJhPfSXhhqFgl7DwzAUVhYNqeEoi-_DCqCZK3-WHGQzqwtRNK-e5oQFzm8bs6oMwF7B9NwPL6S6KHnhNlGsjikP5W5Y-bq5UBALEiNSMJ4w4VZQ69hU7p02t1dqCNFHpYh31psi4eYqw5rWAlqghloD7o7d6hA9VvGl2M4kgK0wT4ZS_RnSFrdKwxZfVkZwZcqUtDCWK3kTJLSRwe1PPjA6PpXQtPUZU0NhhW2m9k4eKpK8AmfzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9GUluoEJCal03F39ahE1LDTBhrfjPFTYskeTrnQ0gn5loTVBzuz6Bbn3-HhNg7dz75Txxmmw9zZtFfBWfkfJXuv5_ZDqPqk1End4Vto5zpL_VXekifkpGB00l77ZLic5e5ybTM20KpCBYGTGGZmweegokT5LeADkIq4_CqPb2rcNyeCqU_kgbfgj_jMIViwovRB7Mpd3tB0aquTDmUZkA_nozJPKAm2qq5NISPHg2yLUaO-7yL35AFG_aUZR0dy63vywUans6WqNHy4FLBYcsHLYPfWGKl-KHKnvn9qjlDzj177dZLThKCLSbECr44Tji0X5kZAp561W_apQ0q6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pf6bMMBnzsp6EzZfW6gXqVAoz07lTWWT05cgaK22046eE_U0bkFDealQt0nP1xRqLRz7jLlArRME0qXH70chIMwz4cucI-UUlw-fc5_B4OCX2CO5ipJzG1KYC6McnP_VdCO1bg2_BvjurqS6xljpVZz77C_ZSR9DSMTSZPQXe6-JVaFc9cXSYVQaZFEThBLKujXHYoOxG-N4Pe6xypdYaqZTdhl9qFLJF6ERgO5MZegA4ypVA1kZIlcKfOA9FJOLpECM4o42mBQSd6wNb3O0ydpXFZRI2yvM40xktfdbYuB76Q9ij2YLY_sytZXi3kdK59qSfItbTOwdt8FkTHwORw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجلس [شورای اسلامی] پس از ماه‌ها تعطیلی، شب ۲۲ تیر اولین جلسه علنی خود را برگزار کرد.
به گزارش خبرگزاری خانه ملت (خبرگزاری مجلس [شورای اسلامی])، بیش از ۲۵۰ نماینده مجلس با حضور در ساختمان بهارستان جلسه خود را به ریاست حمیدرضا حاجی بابایی، نایب‌ رئیس مجلس، آغاز کردند.
نمایندگان مجلس با شعار دادن خواستار «انتقام از قاتلان» علی خامنه‌ای، رهبر پیشین جمهوری اسلامی ایران، و فرماندهان و شخصیت‌های سیاسی کشته‌شده در جنگ شدند.
در این جلسه مقرر شد که در مواقع اضطرار و شرایط خاص ایران، جلسات مجلس می‌تواند «در فضای مجازی یا خارج از بهارستان» تشکیل شود.
از نکات جالب توجه در جلسه امروز مجلس، نصب عکس مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی و همچنین غیبت محمدباقر قالیباف، رئیس مجلس در صحن علنی مجلس بود.
تشکیل جلسه علنی مجلس پس از ماه‌ها تعطیلی، آن هم در ساعات غیراداری واکنش‌های زیادی را در پی داشت و توجه رسانه‌ها را به خود جلب کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77043" target="_blank">📅 04:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIolldxMD5L8SkCRXu0Jlfr1HgFGdXo-wGGAGxkNTRXvkDZl_esGYyz-p8gkDdJGDeNM_06PRGoMUGpbHrh_4no8B-AaNXaKkOTsxwTWrC7LPqFSpNdBpIcmRH7c3BE089bmL6UITaSXOUe0P0I3s1bJ9FRimj67Fzd14X5cMRdfyv7g1Kyv7CNtk9NyDvOhRI_CAiIxKFJmNIQQXgPNPZHZCpDP6OB1k_6ij1ahhL1dmE1RbSjm2VbfNKK3OTRsiIJcPE8cnDMXqnTGWu6ZBg_YsMehHCreQOtZvPPl5MGu7adkRRgCmRlYjwlN42DKU4Ub8kDGQwQ8QsniZQ5E4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان گفت: در ساعت ۲:۱۰ بامداد سه‌شنبه، نقاطی از شهرستان امیدیه مورد اصابت پرتابه‌ها قرار گرفت.
به گزارش مهر، ولی‌الله حیاتی گفت: بر اساس ارزیابی‌های اولیه از وضعیت مناطق هدف قرار گرفته، تاکنون چهار نفر در این حادثه دچار مجروحیت شده‌اند که اقدامات امدادی در حال انجام است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77042" target="_blank">📅 04:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77041">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4M1hpAxl_7Uqdw3u83nCQpzRsFOWsAnG69w2DtIwFzl82xAXqCY1V5h70CdSsXQsJ5onaBTWFzTuLi_eHA9CPLRGDB-3F5Kbk1vo2RKVQXyc-ENcw0QWZ8ER22NM1S9UwL1RRi2f0-rvzHomUrfCPxKlVVlU2kDWt31nEjayA8MM5XbBI0ADfDoXSUsLFVAeKCKUgsoxeSfXQ3mwm9t-QbkGj2xBQWAZCmc66ZS_PePAJ-_56Xb2_ZEwjMuF9osZroCnqiVWR5RV6IbXDK-d68p3z5kbUTiLAGa6TEl9QvzFTR-AkekoDNWUwwXLpci8qFUdeF3XCFerBgPtJ-C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی اعلام کرد که جمهوری اسلامی ایران به دو نفتکش در نزدیکی سواحل عمان حمله کرده است. به گزارش آسوشیتدپرس، در این حمله یک نفر کشته و هشت نفر دیگر زخمی شده‌اند.
@
VahidHeadline
" اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی"، ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت قهرمان و مومن ایران عزیز؛فرزندان شما در نیروی دریایی سپاه بر عهد خود در حفظ حقوق ملت ایران در تنگه هرمز تمام قد ایستاده‌اند.
ساعاتی پیش ارتش کودککش آمریکا که از شکست های مکرر عبرت نگرفته است، با تحریک شناورها تلاش کرد تعدادی از آنها را از مسیر غیر قانونی عبور دهد. دو فروند سوپر نفت کش متخلف که فریب آمریکا را خوردند و با خاموش کردن سامانه های ناوبری و بی توجهی به اخطارهای مکرر مرکز کنترل امنیت تنگه هرمز کشتی رانی در این مسیر را به مخاطره افکنده و عبور از مسیر مین‌گذاری شده را ترجیح دادند، مورد اصابت واقع شده و از کار افتادند.
نیروی دریایی سپاه به همگان اعلام می کند همکاری با دشمن متجاوز که از هزاران کیلومتر دورتر آمده تا حقوق مردم منطقه را تضییع کند و عبور از مسیر مین‌گذاری شده جز پشیمانی، خسارت و تاخیر در بازگشایی تنگه هرمز و ایجاد بحران انرژی در جهان نتیجه ای ندارد.
و ما النصر اِلا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77041" target="_blank">📅 04:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d09iL4SCK7uu6qDKc8kwmvT6Qa7BPXsIWU9DOMdxiaETB0rvFLu6pgthjkWWsgaJV_R52NNC8OPnfAX-RdBk6hP6wm_OzJblAl5LU4126hxfGPTDYKqSJ7ZJuepvqT6SOGDQVrZkbmC3_5IaMoUrPQBkR8XRNsPa-QBa4wtpFhQpFYGv6An57OtbA2bicFepgtET4b2i7aGbfbkSTEzdqlMy5Z36WfPNbquE7rOYiXtAqhpf4ORtkHbKORI9Y72VCK5VKT93NsxYlya-ka0XYTn6xikl-enFUOsV4PfTc0HKyj3VBbYnHtkuiUpGGZt4Fm7IY5gjCBZWXaFPMEDBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MgZZrh2nb_cgoW-75Xgm03MRGKclVaP7lh3kZkHTydM3tAlE2Nm3EghuhKJZhzJFJKcDZdKsNPAOhLXBdkbBN-mSB86t68fYCLUKC38JlkQ5kZmzGdpEUfuB2Km69WXXVrXDAzXRYX0vDs7uSONu1E8IFZLEbn1lHSjp6pzULIsmaxKPGM2sOjXsjQkgd6tbG8n8vgUXahO4Dk533WWG8mRO4fQ9d_ELbuy4PxN_SYOdbrggjXiDgO5FelCMJxgTJ3Dhk08A9IOw0vLvliCu5yO8qrLBS3ADyfSi5kP9RjvG9pQy-8Lt2oX4aKVzsujC7du6uRSl4bJwvfUFG2OUdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: کرمانشاه ۲ تا موشک شلیک کردن ساعت ۴
آپدیت: ممکنه تصاویر مربوط به پرتاب از تبریز باشند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77039" target="_blank">📅 04:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تبریز
از سمت شمال شهر  دوتا پرتابه با نور شدید قرمز به سمت جنوب غربی دیده شد
سلام وحید جان، تبریز صدای جنگتده میاد [احتمالا صدای شلیک موشکه]
سلام اقا وخید همین الان صدای دوتا انفجار کرمانشاه
سلام
صدای دو انفجار در کرمانشاه
ساعت ۴ و دو دقیقه
ساعت ۴:۲ نردیکی هرسین تو استان کرمانشاه صدای ۲ انفجار سنگین اومد
سلام ساعت ۴:۰۳ کرمانشاه دوبار صدا اومد احتمالا شلیک موشک.
سلام وحید کرمانشاه شهرستان هرسین دوتا صدای وحشتناک مهیب
سلام کرمانشاه ساعت ۴:۰۲ دقیقه صدای انفجار از سمت تنگه کنشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77038" target="_blank">📅 04:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=aWvk3m0e2dEFwEdchA532V6CNaajLlPMQG8UiyPzoHAvie3DJ01I31ayTTYiGU9rUgukDbeH8ACHnp-4YZwDdqVZyfKzAy_Mhy76vUouhjc9l9GgCPLnoeEHp3hpINTriU2Y9Dc60x9t6E8cOMIWcSIylyFL0-bLIIQX3yL9V5vBYVIvLnLV3sZeuWS4YX9gaUOc4xjZZTfFW4sDQLy16nufvIbolDn7dc8UD9bMG7_8LdVkeWOEGEsdgftMBQ7z_z1q652PeTQd9MzB2L9ni-MXu5uo01fumzEByVR_boPSU3i4dT3wxm2cSN782LEGC40yzcOu9-wD_nIW5Ikfhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=aWvk3m0e2dEFwEdchA532V6CNaajLlPMQG8UiyPzoHAvie3DJ01I31ayTTYiGU9rUgukDbeH8ACHnp-4YZwDdqVZyfKzAy_Mhy76vUouhjc9l9GgCPLnoeEHp3hpINTriU2Y9Dc60x9t6E8cOMIWcSIylyFL0-bLIIQX3yL9V5vBYVIvLnLV3sZeuWS4YX9gaUOc4xjZZTfFW4sDQLy16nufvIbolDn7dc8UD9bMG7_8LdVkeWOEGEsdgftMBQ7z_z1q652PeTQd9MzB2L9ni-MXu5uo01fumzEByVR_boPSU3i4dT3wxm2cSN782LEGC40yzcOu9-wD_nIW5Ikfhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده با شرح: سراوان سه‌شنبه ۲۳ تیر
پیام دریافتی: اینجاست
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77037" target="_blank">📅 03:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wqrfh0_b2hKsf6jwTskMg12kWSjZt_kRApLFRUhKkYk3I3u2zCGRohQHHN6-NIQx_9iZhHVnJ2PLytwPuc2l5FIcldEX8WQZeGwv3_DgwVikjpRTvAHK1qtgH6s71XRAuaqUWOwXQiQcLVLR7yKjLdNjIWZLo_Q4kngSuaLVBVERYe1TnB4e32RGyYeZoeFgV1xdFF0aH0E18yX460jJqKYKBm3thyqrxpG1A57WAVjOIoIPgUcG7cRAB_8_MaNAE_P-B-WAtvjyiJSizUGbM80biCGe6c-DB8Z-4lDsilvVqnnb_spMYKLqEBi6cSk3tbXCywDctVaKOyaXajQu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۳:۳۰ بوشهر دوتا انفجار خیلی شدید صدا توی بهمنی اومد
بوشهر 3:28 مجدد صدای انفجار
بهمنی زدن 2 بار سنگین بود ساعت 3 نیم دوباره زدن
وحید جان دوباره صدای انفجار اومد بوشهر ۳:۲۹
سلام همین الان بوشهر رو دو تا پشت سر هم زدن فکرکنم انبار مهمات یا همچین چیزی بود
دوتا انفجار مهیب پشت سر هم شهر بوشهر ساعت ۰۳:۲۹
سلام دوباره زدن با صدای انفجار بدتر
بوشهر تا الان ۴بار زدن
چهار تا صدای ترکیدن دیگه ۳:۲۹
پایگاه هوایی بوشهر ۳.۲۸ سه انفجار
سلام وحید بوشهر همین الان سه تا انفجار خیلی شدید پشت سر هم
بوشهر رو زدن ۳:۲۸ نزدیک به اسکله جلالی گمونم، پایگاه هوایی
سه تا تا حالا
الان بوشهر صدای بلند انفجار ۳:۳۰
3 تا انفجار سنگین
بوشهر ساعت ۰۳:۲۹ صدای انفجارهای خیلی شدید و نزدیک میاد
بوشهر ۳:۲۸ ۳:۳۰ هردو انفجار بلند خونه ها داره میلرزه سمت بهمنی
بوشهر صدای ۳ انفجار همین الان بهمنی
بوشهر همین الان ۳:۲۸ تا ۳:۳۰ ۵تا انفجار شدید ! خونه میلرزه
سه تا دیگه زدن
تو پایگاه هوایی
سلام دوباره زدن با صدای انفجار بدتر
بوشهر همین الان باز زدن
دو سه دقیقه پیش هم زده بودن
بازم زدن سه تای دیگه
بوشهر رو دارن میزنن
انبار مهمات اینا نیست فرودگاه دارن میزنن
و پایگاه هوایی ششم شکاری
و موشک های تام هاواک هستش ک صداش بلنده
یعنی جنگنده نیست مثل سری های قبل
بوشهر خیلی بد دارن میزنن تو این چند وقته اینجوری نبوده باز خونه هامون لرزید چهارتا پشت سرهم زدن
بوشهر - اولین انفجار پایگاه هوایی بود ۳:۱۳
انفجار های بعدی شامل دو انفجار در همون حوالی
دو انفجار مهیب دیگر در اطراف شهر بوشهر بود. احتمالا چغادک. حوالی ۳:۳۰ تا ۳:۳۲.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77036" target="_blank">📅 03:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی:
سربندر همین الان دوتا پشت سر هم
یکی دیگه
همین الان بندر امام خمینی‌ رو زدن سه بار
ماهشهر ساعت ۳:۲۳ صدای ۲ تا انفجار پشت هم
[احتمالا همون انفجارهای پیام‌های بالایی]
سلام ماهشهر تا الان سه بار صدا اومد
وحید جان ماهشهر ۳ تا پتروشیمی سر کارم لرزیدیم
سه انفجار پیاپی در ماهشهر داشتیم
😔
بچه ها صبح امتحان نهایی دارن
😭
سلام ماهشهر زدن 3:24 دقیقه
شیشه اتاقم لرزید
همین الان ساعت ۳:۳۰دقیقه
بندر امام خمینی سایت موشکی رو زدن چهار بار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77035" target="_blank">📅 03:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر 3:06 صدای انفجار
سلام ساعت ۳:۰۵ بوشهر صدای انفجار
ناحیه بهمنی
سلام وحید جان ساعت ۳:۰۶ بوشهر صدای انفجار اومد
الان بوشهر و زدن ما پایگاه هوایی هستیم خیلی بد بود
ساعت ۰۳:۰۶ دقیقا انفجار مهیب شهر بوشهر
سلام . همین الان بوشهر رو زدن . صدا خیلی مهیب بود
سلام وحید جان ساعت 3:05 دقیقه بوشهر رو زدن پایگاه هوایی بود فکر کنم
بوشهر زد ساعت ۳:۰۵دیق شب
همین الان وحید جان زدن بوشهر رو ، لرزش و صدا خیلی خیلی بیشتر از روزای قبل
ترس و لرز وجودم فرا گرفت برعکس شبای قبل
واقعا ترسناک بود این یکی
سلام
پایگاه هوایی رو زدن الان
صداش وحشتناک بود
تمام بدنم داره میلدزهه
همین الان بوشهر نزدیک فرودگاه صدای انفجار بسیار مهیب
سلام بوشهر بهمنی زدن ساعت 3:06
سید جان ۳:۰۶ بوشهر صدای انفجار (فکر کنم پایگاه نیرو دریایی بود)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77034" target="_blank">📅 03:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=DZpcuT-e0bOJFu6gRroxAc5p61kLqXVtslytVME0GfmqwblWc7exkam_R0i2LbmK4vKgTfZrADhNz__Z6yfJk6NE6AWu7jaKVfw3x0U2HTGyLw3kh0pxfN_g39KTYlx0NAMmC5FgcOep2zC0tvXYWhEA2uRVLlFXzK4sj-8g5eiYRSf1nkE1QpFcxETCZmjYzeSFmW0SUv4NSEw9RbR6xbCOC1yzx9rNLI0QFYh0xr0tKno26qxtKbCfedF-SEnoR7SfokPwTFef9S1ZYyJucsCnf7WQeWTA92eEUbnCztlOpVI8xEk4nyjJnDM0bBS6c4IAKnyWVXg-ZbuBrmWQeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=DZpcuT-e0bOJFu6gRroxAc5p61kLqXVtslytVME0GfmqwblWc7exkam_R0i2LbmK4vKgTfZrADhNz__Z6yfJk6NE6AWu7jaKVfw3x0U2HTGyLw3kh0pxfN_g39KTYlx0NAMmC5FgcOep2zC0tvXYWhEA2uRVLlFXzK4sj-8g5eiYRSf1nkE1QpFcxETCZmjYzeSFmW0SUv4NSEw9RbR6xbCOC1yzx9rNLI0QFYh0xr0tKno26qxtKbCfedF-SEnoR7SfokPwTFef9S1ZYyJucsCnf7WQeWTA92eEUbnCztlOpVI8xEk4nyjJnDM0bBS6c4IAKnyWVXg-ZbuBrmWQeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح:
#سراوان
ساعت ۲:۳۰ دقیقه [سمت] فرودگاه رو زدند.
سه‌شنبه ۲۳ تیر
Vahid
پیام‌های دریافتی دیگر:
پیام ساعت ۲:۳۵: سراوان رو ۴ بار زدند
سلام سراوان سیستان بلوچستان ۵ تا انفجار پشت سرهم
پیام ساعت ۲:۴۱: سلام، سراوان بلوچستان رو زدن، ۳ تا صدای انفجار اومد خونه‌ها بد لرزید، حدود ۲۰ دقیقه پیش.
همین الان سراوان سیستان و بلوچستان رو زدن
سلام ساعت 2:20 سپاه شهرستان سراوان سیستان و بلوچستان رو زدن
4 تا انفجار بود با صدای خیلی وحشتناک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77033" target="_blank">📅 02:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=S8lEoW9YnuDsxYyoit9OUDaD0m51OBdkrvf4UrUVx749S_tZprJ7rhMDlyye_c9jtgGAF7oArqHpa1ejLTmfA3Pf1YwY97A2cBGc-Ietnv9ZH_OwDU4qrz3dz4hRAkFsGhsOOKa9CGycxdUIfdZgWXGkTsKMrgNr8bfgW-O70EzPT2o16T7aShLRqJoU7cdJ98ET2mZnPBBAnIw7fA8nasrsN9WnBzMenNP8MPo0qXNU5O8h_wLevmrx6yJ8JeeNTjtQuZY7xq2PrX9nEC-TiHv7gyOwwbOF6bRDljqVvhIuewHwRD-QlXY8lIhef0nNl4yPkjlcXA1wodAiEjuDCr8Kki-UY9y2xNfApq9Lwc7J-7N9_qmXomaJeoCdDfPkj1RcTzfKKmV1cGiMrjy_CeFBmgc2UUer1yUAaNYQzYOmCMF5tN5OZoH4RxGDrYUbj3k1AS1WB-XraQ3dZVbHv00aO1roJ4oDE5281WRtjnZgYOPXXd13EiRqqmxsF7CxuaqglocnOxcdAyqtZKJwh7R3yJYqHJt8H9zQ72D_5AkIj7I6rPeGGi6jsOJRVSVa2pWuA6XQLYGKV-pD6aIBlMASlGvD_W6XyhgO79mQNkTV2Z8BBiCKZpBHnlCs3lnXStcX5MyLw422ByDpEaBSqwGUYzCob2jei93z-SpM1W8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=S8lEoW9YnuDsxYyoit9OUDaD0m51OBdkrvf4UrUVx749S_tZprJ7rhMDlyye_c9jtgGAF7oArqHpa1ejLTmfA3Pf1YwY97A2cBGc-Ietnv9ZH_OwDU4qrz3dz4hRAkFsGhsOOKa9CGycxdUIfdZgWXGkTsKMrgNr8bfgW-O70EzPT2o16T7aShLRqJoU7cdJ98ET2mZnPBBAnIw7fA8nasrsN9WnBzMenNP8MPo0qXNU5O8h_wLevmrx6yJ8JeeNTjtQuZY7xq2PrX9nEC-TiHv7gyOwwbOF6bRDljqVvhIuewHwRD-QlXY8lIhef0nNl4yPkjlcXA1wodAiEjuDCr8Kki-UY9y2xNfApq9Lwc7J-7N9_qmXomaJeoCdDfPkj1RcTzfKKmV1cGiMrjy_CeFBmgc2UUer1yUAaNYQzYOmCMF5tN5OZoH4RxGDrYUbj3k1AS1WB-XraQ3dZVbHv00aO1roJ4oDE5281WRtjnZgYOPXXd13EiRqqmxsF7CxuaqglocnOxcdAyqtZKJwh7R3yJYqHJt8H9zQ72D_5AkIj7I6rPeGGi6jsOJRVSVa2pWuA6XQLYGKV-pD6aIBlMASlGvD_W6XyhgO79mQNkTV2Z8BBiCKZpBHnlCs3lnXStcX5MyLw422ByDpEaBSqwGUYzCob2jei93z-SpM1W8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان تامی بروس، معاون سفیر ایالات متحده در سازمان ملل در جلسه اضطراری شورای امنیت، ترجمه ماشین:
بار دیگر، این شورا برای برگزاری نشستی اضطراری فراخوانده شده است تا درباره تلاش‌های حکومت ایران برای تهدید همسایگانش در خلیج [فارس] و تضعیف تلاش‌ها برای برقراری صلح در منطقه گفت‌وگو کند.
در ۳ ژوئیه، یک پرواز ایرانی از تهران وارد صنعا، در قلمرو تحت کنترل حوثی‌ها، شد. هدف این پرواز، انتقال نیروهای سپاه پاسداران، از جمله کارشناسان پهپادی و موشکی، برای حمایت از تروریسم حوثی‌ها بود؛ آن هم با پوشش انتقال مقام‌های حوثی به مراسم خاک‌سپاری رهبر جمهوری اسلامی.
این نوع حمایت، حوثی‌ها را قادر می‌سازد مردم یمن را به وحشت بیندازند و آزادی کشتیرانی را در دریای سرخ و آبراه‌های پیرامون آن تهدید کنند. از زمانی که پروازهای ماهان‌ایر به صنعا در سال ۲۰۱۵ متوقف شد، شاهد تلاش ایران برای ارائه چنین حمایت آشکار و گستاخانه‌ای از حوثی‌ها نبوده‌ایم. در واقع، رهبران حوثی آشکارا از این پرواز اخیر به‌عنوان دورزدن موفقیت‌آمیز تلاش‌های بین‌المللی برای منزوی‌کردن این گروه تروریستی تجلیل کردند.
این اقدامات نقض قطعنامه ۲۲۱۶ شورای امنیت به‌شمار می‌رود. ...
افزون بر این، صبح امروز دومین پرواز ایرانی با وجود دستور صریح و علنی دولت جمهوری یمن مبنی بر خودداری از این اقدام، وارد یمن شد. بی‌اعتنایی عامدانه جمهوری اسلامی ایران به حاکمیت یمن و تصمیم‌های جمعی این شورا، به‌سادگی غیرقابل‌قبول است.
به همین ترتیب، بی‌اعتنایی آشکار ایران به قطعنامه ۲۸۱۷ شورای امنیت را نیز دیده‌ایم. ....
هفته گذشته، ایران پهپادها و موشک‌هایی را به سوی سه کشتی تجاری غیرنظامی که در حال عبور از آب‌های سرزمینی عمان بودند، شلیک کرد؛ اقدامی مغایر با حقوق بین‌الملل. این حملات می‌توانستند دریانوردان را زخمی یا کشته و خسارات زیست‌محیطی قابل‌توجهی ایجاد کنند. یکی از کشتی‌ها، یک نفتکش قطری حامل گاز طبیعی مایع، در حال سوختن رها شد و تردد دیگر کشتی‌ها در تنگه را نیز بیشتر به خطر انداخت.
سپس عصر شنبه، ایران یک کشتی کانتینری در مسیر امارات متحده عربی را هدف قرار داد. یک تبعه هند همچنان مفقود است. این حملات از هیچ اصل مشروعی سرچشمه نمی‌گیرند. بلکه همان‌گونه که یکی از مشاوران رهبر جمهوری اسلامی روز یکشنبه گفت، این اقدامات از تمایل ایران برای تصاحب غیرقانونی یک آبراه حیاتی و استفاده از آن به‌عنوان ابزار بازدارندگی راهبردی ناشی می‌شود.
فراتر از عرصه دریایی، ایران در هفته گذشته پهپادها و موشک‌هایی را به سوی بحرین، اردن، کویت، عمان، قطر و امارات متحده عربی پرتاب کرده است. وزارت کشور قطر گزارش داد که سه نفر، از جمله یک کودک، بر اثر سقوط بقایای عملیات رهگیری پس از حملات روز یکشنبه ایران زخمی شدند.
...
در چند هفته‌ای که از امضای این تفاهم‌نامه گذشته، ایران بارها این توافق را نقض کرده است. تا زمانی که ایران به تهدید عبور امنی که این تفاهم‌نامه از آن حفاظت می‌کند ادامه دهد، ایالات متحده آن را به‌طور یک‌جانبه اجرا نخواهد کرد.
به زبان ساده، اگر ایران به سوی کشتی‌ها شلیک کند، ما فوراً با نیروی نظامی پاسخ خواهیم داد. عملیات نظامی ایالات متحده پاسخی به این تهدیدها در چارچوب دفاع از خود و دفاع از دیگران است.
...
ایالات متحده در کنار شرکای خود در خلیج [فارس] ایستاده و همراه دولت جمهوری یمن، در برابر تهدید تروریستی حوثی‌های مورد حمایت ایران خواهد ایستاد. ما همچنان متعهدیم با اعضای شورا همکاری کنیم و از همه ابزارهای موجود، از جمله تحریم‌ها، برای حمایت از راه‌حلی مسالمت‌آمیز برای درگیری یمن و حفاظت از صلح و امنیت بین‌المللی استفاده کنیم.
و در پایان، بار دیگر از شورا می‌خواهیم با صراحت و بدون هیچ ابهامی به ایران اعلام کند که این اقدامات آشکار، مغایر با حقوق بین‌الملل و غیرقابل‌قبول‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77032" target="_blank">📅 02:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77031">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=EqQ227G2jASdMCoAc5XId6dO5eO0AJTvmfNOdGM_6BA7RZCvhvBuob7evKtoDsFeJZFKLIF3fxpfgsM9_LJMAG_iorGC9uWeaQS4CtIF042x4ti7gHztoWVQ3vQhP-4Fp_rGsiy5HDUa9eMZUbTbirih1jDM4eaV84OzmwABG4UwZMENs52Bn7UbgdPoW6UdG8bQd750WvDJVd9WQtVUKjXU0Fv7vB8sdoomTljYjdZyrP8StyoPku_dcXsxoMhdVnDD7ylk3r6Tqi6u9pQrem6aGCp27sdEL6cOYiI4KQ_EKZv-LF0H87vb5n5eY4Dmbi64j_E4GGWCVZKcX3F_Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=EqQ227G2jASdMCoAc5XId6dO5eO0AJTvmfNOdGM_6BA7RZCvhvBuob7evKtoDsFeJZFKLIF3fxpfgsM9_LJMAG_iorGC9uWeaQS4CtIF042x4ti7gHztoWVQ3vQhP-4Fp_rGsiy5HDUa9eMZUbTbirih1jDM4eaV84OzmwABG4UwZMENs52Bn7UbgdPoW6UdG8bQd750WvDJVd9WQtVUKjXU0Fv7vB8sdoomTljYjdZyrP8StyoPku_dcXsxoMhdVnDD7ylk3r6Tqi6u9pQrem6aGCp27sdEL6cOYiI4KQ_EKZv-LF0H87vb5n5eY4Dmbi64j_E4GGWCVZKcX3F_Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#کیش
، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77031" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77030">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از حدود نیم‌ساعت پیش:
سلام وحید جان
امیدیه رو ساعت ۲:۹ دقیقه زدن
سلام همین الان امیدیه خوزستان زدن
شهرستان امیدیه خوزستان
صدای شلیک دوتا موشک شنیدیم
بعد هم دو تا انفجار قوی خیلی نزدیک بود فاصلش
تونل موشکی که در روستای نمره یک امیدیه ازش استفاده میکنن همین الان بمب بارون شد و تخریب شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77030" target="_blank">📅 02:38 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
