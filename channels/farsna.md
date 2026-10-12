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
<img src="https://cdn4.telesco.pe/file/V1uvVkVjPhzIzVe_4cH2W2mzqx5_hUb8lnvVrUvX-cIEqPF05G6uOOsrlghlDZ4wSMPcayG3CmF26fvxeS1gZ7NYWLksjDolORfQ137kvYMU1Lz4NXJ2KDAPM6iBWWrfZSYlT1Xz0S5iMvZAf0q0yd8itJ0p35yNYNzLX7M0lgX-OXLIMz8F4Kq4zlVjOoqMw_TdtqZJGBUNylTA9Q9ru63nScS8cxVE1T4srZ-a08-vBkQ0xg5uaFMSwrAseE1boaIDgY0S6dW4RZ6Uhnw7FQWeET2jPIEdtl_8ZOnhfBtDt7tvp4N5Tfwn9gatKzkE9b8E02xhYjg7zX9YQMLxzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-468006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXXU0WlIrpvau8G5m4pGpHLnOFS8UHGB93vJZRs3TY64wOFTMSutZzoF5sfyiB_iomysh3rugXQjRWVLmbGtRkPqKLGvwLVtKv1mo4jfith7KNijlu_RYC2IkKKI4FSvF6wvm-I1i00kPR4Le5gcUWdT52iuTZ170y4zGPbQT7PU-W2I-IcENWNBwa3whhB5Yh5WN16JfQmp3OOngk9eRjDDaolre4ZIOVVq2n9rhrpxoog0L9Sw20IquwH_FVa4-RSnIfnj49tAfSva21IkhGBcg7ZLGxpk0x0Z3KykWr1BuBV_WbC_kclcRLU1x7XczjZtd0ITzfuPrxCsMNEZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv4i_EbpSmkbmbVmP6NMm9Ss34ph25suj1ZHq3gVafoMHTU3upurBVFL6TEMBTsGjqVOzn4dPLHRq9OD1d81rduMT4f87cTZOJuvoareooxGKE2-NXSRn-IRwhiz2MAdcpzqPDYJ5VIx2bJEoq-vNyG2nsnuq9DG7ZZVRyq-a--d0Dtl3oDwsC0NnqwIgZR1IosJbgQnGqGc4qlKJJ7GzQgB0kfI07U10w22HBIHT4BSCyYtGg0m4Qn-w6Dy_C0dz1R1yGiPbIEInYHmjVDZG4Yr9c2FaM9_3HpYf8Ks_GLL00euoCBMGgllLYBMRpngNbXxZNBJS_T5SNflZCfW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLzWUL1AhSzSrM4X6msPS91rGNkkkbQ-AqlsZoZI4QzUDEI1mnyMSz7zBuBTl5POta2v3ZHg5-7pdmj3ofCEIw197zm7XIoSDxwjFCXT9I7di1B3yILz0rI1Hw1Qc2ONehoZDPA4h6zn6nb3nJ3yKMYmHPT9lTx0-npsSt3C-BQBpn9go7y7pd3eqozF7vQ4JlnUYIWfAOSRaBiW9lnOC9iyKL6PsOXWIh17YNFANeYB7KB-6NWuTaT_oA84QtJQt8ExUpMzlkFnbWaf98V61mTa__SaW-rFCLMfNmGtELmtEr6ZBMRSVpU5b69hN5-dgb0j03G2ndbDWw3PMIAVWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
اخبار امیدآفرین ۲۴ ساعت گذشته را یک‌جا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/468006" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30f2ca925e.mp4?token=YOQSfGNIPZvO_ElIcILnU94nIE3IjtJmJh__8CBQ4BpDK57zI3om9jwtRwvJwXeGYf8AQPiof09AsLuDvKWgwdCLc6JiSEBG7ndB3q8bHm8ztmXh9dll93WAGQMplbYL1oJn1L97Kj0xuuPxtmBwcqKiLCSpCs77e3J12SiwKTCNQA-s4a9AZXxDioOHT6HGFqnLZHWTG-xlJQxTmcqGrFc3rtrVYOZZJtgDLeICIDrJZmYNxACsW5o3myCUibpko5n7pvQK4C2AdH57Uxumx1d2E8_VaryFHPr-689mQRcG_ss_kls8S_evAelgaDXIehO-ej86c8mcb4Vbi7y8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30f2ca925e.mp4?token=YOQSfGNIPZvO_ElIcILnU94nIE3IjtJmJh__8CBQ4BpDK57zI3om9jwtRwvJwXeGYf8AQPiof09AsLuDvKWgwdCLc6JiSEBG7ndB3q8bHm8ztmXh9dll93WAGQMplbYL1oJn1L97Kj0xuuPxtmBwcqKiLCSpCs77e3J12SiwKTCNQA-s4a9AZXxDioOHT6HGFqnLZHWTG-xlJQxTmcqGrFc3rtrVYOZZJtgDLeICIDrJZmYNxACsW5o3myCUibpko5n7pvQK4C2AdH57Uxumx1d2E8_VaryFHPr-689mQRcG_ss_kls8S_evAelgaDXIehO-ej86c8mcb4Vbi7y8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردمِ برنو به دست کهگیلویه‌وبویراحمد، اقتدار ایران را به نمایش گذاشتند
@Farsna</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/farsna/468005" target="_blank">📅 20:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قیمت واقعی نفت در بازار چقدر است؟
🔹
جدیدترین قیمت بازار نفت خام فیزیکی دریای شمال نشان می‌دهد که قیمت پایه نفت فیزیکی برنت تاریخ‌دار «Dated BFO» به ۱۳۱ دلار در هر بشکه و قیمت گریدهای این سبد نفتی به بالای ۱۵۰ دلار رسیده است.
🔹
چند روز پیش  مدیرعامل دومین غول نفتی آمریکا، شورون، مایک ورث، گفته بود که قیمت نفت فیزیکی تحویلی به بازارهای آسیا یعنی همان نفتی که نقدی معامله می‌شود به ۱۵۰ دلار در هر بشکه نزدیک شده است.
🔸
ساعتی پیش نیروی دریایی سپاه فیلم سومین ابرنفتکش منفجر شده در تنگهٔ هنوز را منتشر و اعلام کرد تخلف و با آمریکا همکاری کنید هدف گرفته می‌شوید.
🔹
حالا آخرین قیمت‌ها نشان می‌دهد که برنت نقدی و نفت فورتیز، یکی از بزرگ‌ترین اجزای سبد نفتی برنت بالای ۱۵۱ دلار، نفت اوسبرگ و اکوفیسک هم به بالای ۱۵۳ دلار در هر بشکه و نفت ترول هم به مرز ۱۵۴ دلار در هر بشکه رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/farsna/468004" target="_blank">📅 20:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/043c9d1a30.mp4?token=oyfy3DsGP9tFa7rxRf_2y-VtrrLOhOVvpae-E0N75Mdg60px67hms56QpxZ5HaOxTU7Eye7HGuSepjh33V8i8cpdJ2Ypqaa-N0-uClaEG-XzSCcdKAzYhAMBXocgStA1SRjNpggpnGtXSS8ivKtWz46V6Vcq315sDADgm0VVbT107vhwJ27ZH9dkUYiSt-CrryQ3khjluI86awXYDwOh-yEKZlLhCEHpjAg0GHnvd26WsSm0yXSIaPltL7FZJw1vNEI-kQBLEXGMVLt69FEDDygk0lvcGlBnE_Xi4VVDRX4X1F7LqZvsTMk-k5IyaDOW8zqGOKHea12g4-mX3gvA4Q9iMHkOZQX_0NWPPXi4PO8gwTCoZQp4pFlK7aW1t9l6v3UjuLTJRjG22Fa4AlCRIgClpGdg3-X4EgEeNnsGRTz7zHCDJua8tsaqR_ey8LUjiau-AIgl4QON8iUW0AuRdKJwkZk-GXKb1qpJdoCOx7P-MKoYo2ZklBcz9TXdTgkUS0LSVJoA__xeRDUXm8MkZ25WYIwG21eDMOFRz7404jl5O-ZZzaEidTwdQHyH6Pjv7Qr2d2YqbF7ZRqiE9ioTvLOX2QSbCDLJbzYSFi18l8xtqzp4dwEYvWOEnvkOmWw2A1MoomIaXvvnrW1aSiI_BM9R6tRq6dm2XUqeHQhXG-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/043c9d1a30.mp4?token=oyfy3DsGP9tFa7rxRf_2y-VtrrLOhOVvpae-E0N75Mdg60px67hms56QpxZ5HaOxTU7Eye7HGuSepjh33V8i8cpdJ2Ypqaa-N0-uClaEG-XzSCcdKAzYhAMBXocgStA1SRjNpggpnGtXSS8ivKtWz46V6Vcq315sDADgm0VVbT107vhwJ27ZH9dkUYiSt-CrryQ3khjluI86awXYDwOh-yEKZlLhCEHpjAg0GHnvd26WsSm0yXSIaPltL7FZJw1vNEI-kQBLEXGMVLt69FEDDygk0lvcGlBnE_Xi4VVDRX4X1F7LqZvsTMk-k5IyaDOW8zqGOKHea12g4-mX3gvA4Q9iMHkOZQX_0NWPPXi4PO8gwTCoZQp4pFlK7aW1t9l6v3UjuLTJRjG22Fa4AlCRIgClpGdg3-X4EgEeNnsGRTz7zHCDJua8tsaqR_ey8LUjiau-AIgl4QON8iUW0AuRdKJwkZk-GXKb1qpJdoCOx7P-MKoYo2ZklBcz9TXdTgkUS0LSVJoA__xeRDUXm8MkZ25WYIwG21eDMOFRz7404jl5O-ZZzaEidTwdQHyH6Pjv7Qr2d2YqbF7ZRqiE9ioTvLOX2QSbCDLJbzYSFi18l8xtqzp4dwEYvWOEnvkOmWw2A1MoomIaXvvnrW1aSiI_BM9R6tRq6dm2XUqeHQhXG-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگهٔ هرمز؛ خط قرمز ملت و رهبری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/468003" target="_blank">📅 19:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c5bb9592.mp4?token=rZxPVQ8AKtS_boEp8SkiqRHDq7JA1cYuLT8fWTrj4Ji60WG2EDHUk2zk4xJaU0J0YeNCdaHrcGMiwwLbMtIolD0P1sQAT19saGDFhTlCt4Xg_qng8_kPS-TYz0PhMKuUc-JNDRyJfLin3UFrUoSKtNwNkMjBU_KsGss8iwx5p35k8vdTUVyb4FlnNwx1NHOnH2uuW5PbMrvh45_CIsFMAgHVpruV_szpn4LWqCrA5lBuNMFEXaV-d22EcrQn855xBjFg-WWxvhdPe78zi7pWsCvShrEctduBAhxICJJ-aqoAsjxhVgZdzpdEr4goFYHHpe3OkzXwk-X2w-_NQbN_ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c5bb9592.mp4?token=rZxPVQ8AKtS_boEp8SkiqRHDq7JA1cYuLT8fWTrj4Ji60WG2EDHUk2zk4xJaU0J0YeNCdaHrcGMiwwLbMtIolD0P1sQAT19saGDFhTlCt4Xg_qng8_kPS-TYz0PhMKuUc-JNDRyJfLin3UFrUoSKtNwNkMjBU_KsGss8iwx5p35k8vdTUVyb4FlnNwx1NHOnH2uuW5PbMrvh45_CIsFMAgHVpruV_szpn4LWqCrA5lBuNMFEXaV-d22EcrQn855xBjFg-WWxvhdPe78zi7pWsCvShrEctduBAhxICJJ-aqoAsjxhVgZdzpdEr4goFYHHpe3OkzXwk-X2w-_NQbN_ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف مجری اینترنشنال به دشمنی آمریکا با تمدن ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/468002" target="_blank">📅 19:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aa588aba.mp4?token=sPyaDbdjarUMUnt-Tc-AZuI8y6VJ-cg3V5sMF3Y4zw1Qz5nyCm3gB4XHVEg-kfTljHwUMJLZEyJ7I5XVBMExrNxxh7m_31ZLziEtuvhbwb5LzEn7dtTLiLcC0yHFHmpK8avLM_b33g948oUmsq3Ug7ack3XalZO7V3nDYw2taux93epE8KxddN2CtNszds60IBZqjpXmxB4JPy7_2zY88tXQLZmm_4ibVQcYkTvM0HP1ikXAOfc08VoWthcBuLTffEoWgUcWqK6ulCQZkWaO_0i0DlGOeHzLN4za6CwJRgefhcqNVS4SMMBZoQE_iNSi-iOanc0YWKvI_mufXC5B9RjMxP6Hl085rKMm_DD5h5ETHHsFHN6jdzgv1rfvIsrqm3ylo00_7Cmm_i4oSTKtJoL4KBgafslvjQ8gHwx2Vubxd5GzvACCrfDhlalWTNHLviB2jCNAyrWm3mMXIjmX7UWjIPZZizA4qwl5l4Q_gZTyWM3rvq-CMzzmhO2TQJjSY3WSVdSP5KRgizIrVZDA64MbW7A9zhXWMgkzGPMEsfnJm-Kg9oa_1EnVk00B-q8dqLCOnCzyBJ3OHmQXc-ZJPJfaH5_qEY5QYHw5VFqgJrKdyJQwHns-Wck5gzvMuA4VsAIuNmGpFepcF-5jLpMAJs_V1Y08SbIADftDZVlKmSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aa588aba.mp4?token=sPyaDbdjarUMUnt-Tc-AZuI8y6VJ-cg3V5sMF3Y4zw1Qz5nyCm3gB4XHVEg-kfTljHwUMJLZEyJ7I5XVBMExrNxxh7m_31ZLziEtuvhbwb5LzEn7dtTLiLcC0yHFHmpK8avLM_b33g948oUmsq3Ug7ack3XalZO7V3nDYw2taux93epE8KxddN2CtNszds60IBZqjpXmxB4JPy7_2zY88tXQLZmm_4ibVQcYkTvM0HP1ikXAOfc08VoWthcBuLTffEoWgUcWqK6ulCQZkWaO_0i0DlGOeHzLN4za6CwJRgefhcqNVS4SMMBZoQE_iNSi-iOanc0YWKvI_mufXC5B9RjMxP6Hl085rKMm_DD5h5ETHHsFHN6jdzgv1rfvIsrqm3ylo00_7Cmm_i4oSTKtJoL4KBgafslvjQ8gHwx2Vubxd5GzvACCrfDhlalWTNHLviB2jCNAyrWm3mMXIjmX7UWjIPZZizA4qwl5l4Q_gZTyWM3rvq-CMzzmhO2TQJjSY3WSVdSP5KRgizIrVZDA64MbW7A9zhXWMgkzGPMEsfnJm-Kg9oa_1EnVk00B-q8dqLCOnCzyBJ3OHmQXc-ZJPJfaH5_qEY5QYHw5VFqgJrKdyJQwHns-Wck5gzvMuA4VsAIuNmGpFepcF-5jLpMAJs_V1Y08SbIADftDZVlKmSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای هدیهٔ یک دیوان حافظ از سوی رهبر شهید انقلاب به مترجم بوسنیایی خود در جریان سفر به سارایوو
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/468001" target="_blank">📅 19:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467993">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YS5e8hZzgYHXwT13jLW8bNXo7qJXHifTBj4Lm2QVclfW7Gzk9BrD7LRSNb0ykz_2KgWFwVrxG3OQDs9mC41xL_5ZBs9r_siEsoXulRxGlquqDjqbzU-OPerGWEBmVtGmCHKCvl2e3aH_shGxi_JzmVcRufRM2sMwhULVMHRMVqiddeOWGjBhuy0LTmZOXfgQQCc1vXf-W1QqvYapfH0VFLAwpv9Gn30-u1yW6lEshWg-fVgHCLuj6qvAvo3SYKQy4iZN75jkRphNG0ioCsjVEWMeCGPR8GW7pNdN52HvEulqUFTvehYIbuz9y0EImG0diEQYHEw0_dqNIG6r-2Pc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MDClYgAWlH1KvCixHN5LFLc1vxaeY9vzf61RqCePwNGGdv8Hc46pJqh2Tt_S3CVzvJWjgRNLKt_nJExFqZk7jcfSKaROqLSnhG3ehpgGYqNzW9IHwYL8e7VDyYnWht-iFWHLN-zmFr2e_QHvBaZcHJXameOCmGRk4w4NNJGDg-un8gp2hqoaKwduP7H9W79hJKkurpz58AGKzXcpzTt3CmyP64ecHumrZCFMIFIADSkX1yl6ovwIv_z0r_O6zmeEfDTq0i3_naL4213IeRL4ReWq9SEauemExew2_9sAScBNfB0KZY2dy7oBvaHZdfG-9em4Z5T681DJPnqTTzeYNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaETyfuUJ9gNfGSKJUCpVAslErtbZHI5VkVJ8Lmy71-BJe4bpKnHl8sr44XL26jC5042qXI62B7lkXp7pdwLaggq2nFqrfdjdeyhkotGhRSKhBvYlH4ccjFmXVA3aBo0FMt-Uz8WRRprfZ0Rho9ooo0ag1uynE1YZjfzmZNCcb5p1mPJJ9yoP4636-HyMZzaEYF-8sNAbqawGqWHQ6bFlgim1cEP_sN06_D3Os-tt9TFEkca0ACjewQMyHee8flPm4giKVPzJLmDzmF4PRzZvt0X_1llAFBmC0Jfm0HXwUbTloewLOpccjpsTZ06MeZptRc_ITOr1lQg3bRpc92Lcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTQdmbGpV_QqjnT9IYOzk4pjasuqvfyB4HuNtIeCTj2gZ1t1N-v0Obsemi8HcVpXjaCrED4zFdOllxQBE-y9x0B2BFC8LZ78OVIfd9DJ8dTLmwvvpIK3I8ybwBOL0NnsxWzNafk0hQePU5ByScPdOdGLI6LkMlPlnIgJN3366l6OG78xgR9tyWqfyBPubH77o_yRFL20lJ5mpZKXnO2FZHRwmEV4_yPgjyVHfGMIrFUGCAoFZZ6mNlerJfiWd-mRxYfujnEyxbx3buaZK2p8X9vzMz92QpxCGJ2SFpkSRZCZEWNfn42MXWySZ_0qiGmnxYphwclgxibDxjatVlFtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iatnE9SbMZAAW7rIVYlEGAsHBhM4VA735oAQimla8TYzzUFy3MV0eqjJykTaI8Gi70_tjwV_XveucTM5fbeIRGtgrCWmYnkYl1FeUngKmSRwrqJ2AzbvnVE1V8nKm7lRNeoEF64EH4ifIJfR2O2gWeUmo0732XiaLWSWM06pDEzJpYzZg7qst05csgiU-eG0xaUpNoVmqxTAUjtVloDjEL_3LrgU350Ad5FPSyhxub-b4Oj6qf_dCzz7GFQ5KkH-myNkrzW1swej71PXI5w_Ep8wnKn7fJ0Q1f75kRQJ8ZY5hDirz3GdeNqyS44NkIc55c_ipjPB2RvOrgipppmRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYVQDXbeTzHmTjfI87ya-I5j3KOayQtHH8_Apg0aYTtKDH2IwvevEBJpS16g_QUYOTgQV3l_kZIRAj-8T02ghosjbZi-OrfeAB-ISGtIehfmWRVpicS8sj8bVtb9q1knIJ_FC6qahzjwBiXGEAqOjjlrC2QJdani7VYxJ3vOdS5MyQnMLVI--dsHgcUHHK4r1_GO_F8g8AfReXDnDgctkXKyGRxumIDxVQKC3tSX8Pav3TFalQ-MMldy7h6Nx9rOy6zCfA9VsPZgRNP_XYYGPSgurJ5Iq3Gps1XMhUODqdlN3nZrBOEKz07CQfv0eE5yO23uLhmBjckyo79Dul6rHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_ao1WwKFKQDWmYm2-Q9kGJHH27p8vU182p1eYGRt5c98uKaAI6AovL95vo0XdgAjDGe0zjSTlDcELd5hOyECGUQGDmQyH88gTkcROujKFVywwBG8oobIGsJjdyz-xb3idLqzEKw1TQ5cKRXwsDR3jeINm5Btnlt4xZW7_4uX2eIoQ3Zaaf3uim4eA0haMIkwT6jQTQMpN6pgmX1kbjEc2la4kD2RLmgEhOH_qZbyUGVrKE0SATbkWag4Jm6FyzyafsJzTy4qYpAKzpn_uDvH2CjJuSqwJF16iLJsqnLG0EWkoIHp5sHB-Oylyj-Njk14F267LplTuNvAG6b9Ki9fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
از ترکیه تا میناب؛ کاروانی که‌ به‌عشقِ شهدای میناب رکاب زد  @Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/467993" target="_blank">📅 19:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467992">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c955e2c28c.mp4?token=fpEm5eEcDz-Th4Vw0ozLaC6h38M4EC_GYidp3cOIIdzNg1PKOH5WOObx2ESTF6goKdcwKQ8Ao9qGQlJ1EXYg94iGXy75nZCtdOU4kaE-WQQ58zd9PdcDQwK0oSUzuwfyjSxQEkJnZVcCd4tsMoMZdsw2y5nc_D3EMnTu60Hy4dSQYXxJTG4YXMNrvnpihymQ7VVSicF5T2ZBcy3XLTXk8McpWHMgP72YaKOPFQbvkkHGp2FhlhfCqME-1lo0Mu-d1bQmfzqkyZqi0eQShMyYGoLEbNlcPBpDb6vzVvgKqhAIClMwsh7WOlI6Ff3-o-Ho5pZ5C96C2BVjWqdcAF6pkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c955e2c28c.mp4?token=fpEm5eEcDz-Th4Vw0ozLaC6h38M4EC_GYidp3cOIIdzNg1PKOH5WOObx2ESTF6goKdcwKQ8Ao9qGQlJ1EXYg94iGXy75nZCtdOU4kaE-WQQ58zd9PdcDQwK0oSUzuwfyjSxQEkJnZVcCd4tsMoMZdsw2y5nc_D3EMnTu60Hy4dSQYXxJTG4YXMNrvnpihymQ7VVSicF5T2ZBcy3XLTXk8McpWHMgP72YaKOPFQbvkkHGp2FhlhfCqME-1lo0Mu-d1bQmfzqkyZqi0eQShMyYGoLEbNlcPBpDb6vzVvgKqhAIClMwsh7WOlI6Ff3-o-Ho5pZ5C96C2BVjWqdcAF6pkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/467992" target="_blank">📅 19:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467991">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0CoCes2-Ow-WKbphAOaZ30eZVcOa3rmEtpfDzB7HpGRQflv3a8gLsZmQLQaNVHTK97EP-Ir2mhqd8sZi3zgDWmuuekGdeoo3r-9_-mt--M9OvgQsOgp1L3nTc_aNiBjXrGSCsi1vKmFPP2FU0tmLUkUoP474upllC13ER_qVYvJzKbpKsz9DGrCB5FUXVH5HFTNG0sGaMS2Np7CxD9RanMgBzG-JwHYxYYWxm7TgEYT7e__AWpQVr47GWVrndBhdysUp6uTT6QlGiN2V8gvHK4vN51kJAHeIpLUrFI9qCzcDVMussWlTIR-Dp7py381L0hQPHs_GesgljtX21DecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت ۱۰۷ دلاری شد
🔹
سابقه نشان داده که هرگاه نفت به ۱۱۰ دلار نزدیک می‌شود، ترامپ از «پیشرفت مذاکرات با ایران» می‌گوید.
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/467991" target="_blank">📅 18:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467990">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd3FeUMsKSUGFfieGfCFFgr-vyiuXrp6KaWIl-RVi8tLM-fuEBU5slzuEtjbHrkftBeCk-WGTj8MyYmns1N23P2-3PQPRVMS4DE9bIGALbQ6DvKcO4zmAGiXrjsNM2LJTFbBD1RBFzM9jx6atYaijUeTwCrT0A_gdHT5ADPA7GtON9FN2nPRMXtNt2Or83JVRJB8F7eoICxV-JVcwohaU1Ag2SegKdNx-tydMLDjgL2YDWPnvxpHzXKAYXiGL7XOb0pbJqb-kjBHnIR6RIlHrRt3Wy2u4-TGyK30o7fLqEsp98qkmzX_4ptv4p4Z09oAhvZCbJqzXTSEc9Kph84iNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبانی مسابقات آسیایی در عربستان زیر سایهٔ ناامنی
🔹
رویترز: حملات به فرودگاه بین‌المللی ریاض و توقف فعالیت این مرکز هوایی عربستان، در شرایطی نگرانی‌ها دربارهٔ وضعیت امنیتی این کشور را افزایش داده که قرار است ششمین دورهٔ بازی‌های آسیایی داخل سالن و هنرهای رزمی آذرماه در پایتخت عربستان برگزار شود.
🔹
ادامهٔ محدودیت‌های پروازی می‌تواند برای کاروان‌های ورزشی کشورهای شرکت‌کننده، از جمله برنامه‌ریزی سفر ورزشکاران، مربیان و کادرهای اجرایی، اهمیت پیدا کند.
🔹
در صورت تداوم شرایط امنیتی و اختلال در حمل‌ونقل هوایی، تصمیم‌های بعدی مقام‌های عربستان و شورای المپیک آسیا درباره نحوه برگزاری رویداد، بیش از پیش مورد توجه قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/467990" target="_blank">📅 18:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467989">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7559f0540.mp4?token=TjAwk5A8VHdOekuL14CS6mHaP0cPPfLHAzOWuabDKM2QRbLdx9ynJ_cJTdJNTjwocHhfw8iVrnmv3r256RU8auEtOjR1lWNsH-fAfGMIm2zURFFKPUxe3mSM435lYddLt5X4aB4I5NuOEqyDNBtX4pLlhLHWhj6H7gajssw3R-6GqiRgkhMDZ2SfJkYAiLbsX3aajPiXytazanQGL8Yx6QfYVDXfc2tGf4tUPce_T6w6j0wxBXWidMmPXuWItqeqdzDBRrDZ4TG8-LiGdDG9yZX83MkWg4Jg8qW96f316nfjA14_Bk4TlAaXMST6IpyzT-Mqkl_7BfWhAtnQ9iXG3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7559f0540.mp4?token=TjAwk5A8VHdOekuL14CS6mHaP0cPPfLHAzOWuabDKM2QRbLdx9ynJ_cJTdJNTjwocHhfw8iVrnmv3r256RU8auEtOjR1lWNsH-fAfGMIm2zURFFKPUxe3mSM435lYddLt5X4aB4I5NuOEqyDNBtX4pLlhLHWhj6H7gajssw3R-6GqiRgkhMDZ2SfJkYAiLbsX3aajPiXytazanQGL8Yx6QfYVDXfc2tGf4tUPce_T6w6j0wxBXWidMmPXuWItqeqdzDBRrDZ4TG8-LiGdDG9yZX83MkWg4Jg8qW96f316nfjA14_Bk4TlAaXMST6IpyzT-Mqkl_7BfWhAtnQ9iXG3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان رئیس‌جمهور را غافلگیر کردند
@Farsna</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/467989" target="_blank">📅 18:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467988">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFvcNpK3pr4ceOcLMSW1iIbVpLVgBDt_MZ8e61BaCJZf02DUWGdO6IPKDdxZH9SFyBrJ1oDLS3Da0AIvBaFYXmvOW5z1FoJMFia40NRrs8qHqRotHP4mD7LqIXDjszxK3jlmvgFd5CL_CCyjtwXTfTvU93nVqT-_97SQarzvyar6WmWXyXtsNbXJqx8yivRPZ-VJv5FHm1C1b2oadH2meBMD9oz53qvO1O-shmAwPma7ZpYckRQm5zZNPUzXcNtFCELlj5TgHjZ_4hPn8C4RS19aYgPNbsHf-AYM_iPeyS-0bAFiYWuSdQh0pjtAtFyOPetDePjaM3DRvyILDgkqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج لغو پروازها به ریاض تا سال آینده کشیده شد
🔹
شرکت هواپیمایی طيران الخليج (Gulf Air) بحرین عصر امروز دوشنبه اعلام کرد که پروازهای خود از ریاض و به ریاض را در بازه زمانی ۱۲ تا ۱۷ اکتبر لغو می‌کند.
🔹
این شرکت پیش‌تر نیز در تاریخ ۹ اکتبر پروازهای خود به ریاض را به‌طور موقت تعلیق کرده بود و اکنون این تعلیق را تمدید کرده است.
🔹
طيران الإمارات شرکت هواپیمایی بزرگ و پرچم‌دار امارات متحده عربی که مرکز اصلی آن در دبی قرار دارد، لحظاتی پیش اعلام کرد که پروازهای خود به ریاض را تا دوشنبه آینده تعلیق می‌کند.
🔹
دلتا ایرلاینز آمریکایی نیز هم اکنون اعلام کرد پروازهای برنامه‌ریزی‌شده خود از آتلانتا به ریاض را تا مارس ۲۰۲۷ به تعویق انداخت.
🔹
درپی حملات اخیر به فرودگاه بین‌المللی «ملک خالد» در ریاض، سازمان کل هواپیمایی کشوری عربستان سعودی امروز دوشنبه در بیانیه‌ای اعلام کرد که تعلیق عملیات فرودگاهی در این فرودگاه تمدید شده است.
🔹
ده‌ها شرکت هواپیمایی بین‌المللی نیز پروازهای خود به ریاض را متوقف یا لغو کرده‌اند؛ موجی از لغوها که برخی از آن‌ها تنها چند روز ادامه دارد و برخی دیگر تا ماه‌ها و حتی تا سال آینده کشیده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/467988" target="_blank">📅 18:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKJoPLxgmTaFTjCokZNVPAfUWE8Ju5rJySixpSThbli5yIO9QjKXsBFZuZj6r9RGmmgDMTjMuzKZzKn0Aw6bYV5yAGqMQlVYjrMAThc_r-Mj3i4uUZGCYd01Gkp4df43JCUiVmnQn_uOQzzHhjnDEsatj5RISdfoxXUvAo_ZGl7sxTftZn_CTJcq2Gng6y2j2u8QYVKqcltn1KhhEK_08Rdid0KszO7yCRT6m2ISU-djxKK6WKxIqwPUKPOXfQvb7UbaZHfnlZyM9ZXH_pR2iQpQ-IyG2kPLauLLRzYw1_e2Va444h3bJnDNnLW79h7qLeZrOQfigTR8dex1Ead2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر نتوانیم مشکل مردم را حل کنیم، نمی‌توانیم جواب شهدا را بدهیم
🔹
کسانی که برای عزت و سربلندی کشور جان خود را در طبق اخلاص گذاشتند و فدای مردم شدند، برای این هدف از خود گذشتند که ما راهشان را ادامه دهیم، نه اینکه به دنبال پست و مقام و نام و نشان باشیم.
🔹
امروز با پیچ خطرناکی مواجهیم. جنگ ما فقط این نیست که با تفنگ بزنند یا موشک شلیک کنند و ما مسئله را حل کنیم؛ این جنگ را هم داریم، اما بدتر از آن، وضعیت اقتصادی‌ای است که برای ما ایجاد کرده‌اند.
🔹
ما موظفیم مشکلات مردم را حل کنیم. اگر نتوانیم این مشکلات را حل کنیم، مقصریم و نمی‌توانیم پاسخ خدا و شهدا را بدهیم.
🔹
اگر توانستیم در جنگ پیروز شویم، به خاطر بسیج بود؛ بسیجی‌ای که مغازه‌اش را بست، درسش را رها کرد، مزرعه و خانه‌اش را گذاشت و رایگان به جبهه آمد و برای دفاع از این مملکت ایستاد و تا آخر هم ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/467987" target="_blank">📅 18:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۶.pdf</div>
  <div class="tg-doc-extra">2.4 MB</div>
</div>
<a href="https://t.me/farsna/467986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۴.pdf</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/467986" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رئیس سازمان بسیج: برای رویارویی با حوادث نوپدید نبردهای ترکیبی، باید شبکه هوشمند و سریع جامعه‌پزشکی را در مساجد و محلات مستقر کنیم
🔹
هر مسجد، یک پایگاه پیش‌دستانه امداد و سلامت که نه‌تنها در زمان بحران، که در ایام عادی نیز مسئول پایش سلامت جامعه و ارتقای سواد بهداشتی مردم است.
🔹
ما در این بخش مسجد را نه‌تنها پایگاه اصل انقلاب، که سنگر سلامت و کانون مدیریت بحران‌های اجتماعی می‌دانیم.
🔹
این حرکت رجعتی‌ است به هویت اصیل ایرانی اسلامی؛ بازگشت به من جمعی که در آن رنج یک فرد دغدغهٔ سایر افراد است.
🔹
در این گفتمان، مسجد صرفاً محل عبادت نیست، بلکه قرارگاه مدیریت امنیت و سلامت است.
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/467985" target="_blank">📅 18:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467984">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzbCHAD_BreV0Cf4lV1rDOplm9hKMfoJO5t6klh-A8D58yDftx3LdSJ42v8q2Ot9Y6LQj1Ubtj80qu2aUKf7j8Tf2NUsxc_OiWus3aHK-uhbhTskjelVLN-jM1P415HBk8fQYvIDd78KLNSxwdZO2DHZ-1G2_HddIHYKZQ-CEvZpBa1R0OuB0qznarykguW7uFT-u0bEj8FEjox3SmEYR8ELU3l65sZ-9k24IMRPHj3bt56emloyB4_-AHHZokPSKspljUt8y_PhDlRVFe9Fpd9VB60wge6fUngmuOmDtGjtr_x2fs8Zy5ilCWCWz1CjoXYXe9basY1XPYbvrdAMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمان جدید ارزی برای بانک‌ها صادر شد
🔹
براساس بخشنامهٔ ادارهٔ کل عملیات ارزی، دستورالعمل اعطای تسهیلات ارزی ۶۰ میلیون دلاری از محل منابع بانک‌ها برای واردات کالاهای اساسی ابلاغ شد.
🔹
این اقدام پیرو مصوبهٔ بانک مرکزی و با هدف حفظ امنیت غذایی و تداوم زنجیرهٔ تأمین تا پایان سال جاری اجرایی می‌شود.
🔹
مطابق این ابلاغیه، تخصیص این تسهیلات مستقیماً از محل منابع داخلی بانک‌های عامل صورت می‌گیرد.
🔹
همچنین شعب بانک‌ها مکلف شده‌اند پیش از صدور گواهی تخصیص ارز، مراتب وجود منابع را از ادارهٔ کل خارجه و دایره پشتیبانی ارزی استعلام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/467984" target="_blank">📅 17:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467983">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqm-8h8ZPqY_yVvi5CfbLMH84f0ZlK8HSfEEDvrGBTRsHwYOIOmHHzoGaRltrvr7Zn0t9QPb1LAVdeWSrdXaAu5yike8FIXpHjjrkrazRj9E0m0ahjrkKEVNDlsOP80tlu_ltdxBMMNkcCF1VMTVazPc0FL_gtNVnEk8-dhDMOXEYUPdFcv9VLu0-oefcl_JBjJfAmuOEjIOYRQfpW5NXLN_S7RjSVDGLRjd5bh3ViCwLBnUSo2Ke0eKBJbCr6pqWEH7AG6SD2Tr32NjVoChu304aJ_RoW9Df3OlpZCRXTw8V6hZturhC9bw9F-Xsyv2F7lyHL940iLMsyz1FCMLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  وزیر پیشنهادی دفاع: تقویت پدافند هوایی را با جدیت دنبال می‌کنیم
🔹
مهرداد اخلاقی در نشست ویژه مجلس: اولویت‌هایم برای اداره وزارت دفاع در برنامه پیشنهادی ۱۶ مورد است که یکی از آنها باز معماری و بازآفرینی وزارت دفاع آینده است.
🔹
باید تلاش کنیم که از داشته‌ها…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/467983" target="_blank">📅 17:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467982">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d9550576d.mp4?token=bM7iFJi_29984LIwVC1uyfnoJgXZgKWuwYVjabiDDKpdwgGk1vsX9awM_tmYBpWSTOQwd9k5PwBxiuwWPwgGm9UjUOUEz2j12IGo-p9t3h4_dnjQRy0i1OOTymYqGwnj2L_ywOWuh_FXqyMoG5y9CEgObBYAq7MxSU5l-Tq7mCQi5GvcGqOouBRo3NQfVHafPKWjJIli9NsxbFe6IyVga2FmdGQdoZx-BRMFLmXE0hL56fYJx0j6NMJyrHl7WtOJUritZ8Uf-QkKhTSa2zf8b-cO4MFbMh1X57FNobReGMt7x1Vy_ClhfH-JKPALWD9TvSuD0nxV8XFH41TUjwyvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d9550576d.mp4?token=bM7iFJi_29984LIwVC1uyfnoJgXZgKWuwYVjabiDDKpdwgGk1vsX9awM_tmYBpWSTOQwd9k5PwBxiuwWPwgGm9UjUOUEz2j12IGo-p9t3h4_dnjQRy0i1OOTymYqGwnj2L_ywOWuh_FXqyMoG5y9CEgObBYAq7MxSU5l-Tq7mCQi5GvcGqOouBRo3NQfVHafPKWjJIli9NsxbFe6IyVga2FmdGQdoZx-BRMFLmXE0hL56fYJx0j6NMJyrHl7WtOJUritZ8Uf-QkKhTSa2zf8b-cO4MFbMh1X57FNobReGMt7x1Vy_ClhfH-JKPALWD9TvSuD0nxV8XFH41TUjwyvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینستاگرام حامی رضا پهلوی شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/467982" target="_blank">📅 17:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467981">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTNXE3huYfxnSPcElVbcHCNd_2mbCsD1i5i4sn47bbndXw52fJ80G4Rw0zLLU4qASaDi_eGuBIAG17kxDwfSDdIDW20RKVIt4bcTvhfQtcDlQKG-cg-TM-r2G2lmbBUfwOOoe4CklKCqfQk8khTdarhjMwlWQDzFsg8NTcmuOyJGrE1jprgti7uD6Zg5ATfTZNtAkpOcF5GoxozJ8880clq_CbS_-HEpelBCkCceT9BI0lny6sAuPKuLtVsz1IDkyTyL08yFAy7SNg5MF_Q8WqZjLOKseXOCRC_U9I4GmO2rKtDDeA9jfjajMKsjy0v2rQVeStRTV35ocC1Yk3cgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/467981" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467980">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfwkdiSVwqgjlnaXNPRMETobwdt4QMFEUHisTI-bbUea5T6YVYWdRaHurlHS3QFC4dIeUD8y1JXnY7yuq4QOScHMzK1qquoBrTdSt9U2BsQT1zoEM6ADoNjllqwzN_19qzfE54IFlSPNyGO2NjPkh1RPNMUKhcL7gLqDpl1bq6Mpl_w6sGPAs0zog8HCU0WxTv2aMHEZa4renOHipMHULKT2fJKyFgm0VMpoiGVBUYXsaHw47dcY0EuPHClS-2GdFsJwVIBDkz3ilEVVGhicSFq8fvtg2W2UBoehPoQif8xal6kbsThJ_Z_TyGAY_5uddua096U1wAfAg4uCCZMjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت هرمز علیه دشمن کوک شد
🔹
زمان در محاصره، کالایی کمیاب است. زیرا دشمن تاب‌آوری شما را هدف گرفته نه صرفاً خاک یا ناوگان.
🔹
هر روز تأخیر، فرسایش را عمیق‌تر می‌کند. بنابراین بازیگر محاصره‌شده نباید زمان را مدیریت کند؛ باید آن را به سلاح تبدیل کند.
🔹
درس تاریخ این است که در موازنه‌های نامتقارن، پیروزی پیش از میدان، در ذهن حریف شکل می‌گیرد.
🔸
حالا باید دشمن به این درک برسد که هیچ سناریویی، نه فشار حداکثری، نه عملیات محدود، به پیروزی نمی‌انجامد. این، مسئله مقدمه صلح پایدار است.
🔹
حالا تغییر الگوی تنش در تنگه هرمز را باید در همین چارچوب خواند. ضربه به پیشران کشتی، برخورد جدی با کشتی‌های اماراتی، مجازات کشتی‌هایی که AIS خاموش می‌کنند، فقط تاکتیک نیستند؛ پیام‌اند.
🔹
تنگهٔ هرمز حالا نقش یک ساعت را دارد. هر اقدام باید هزینهٔ عبور را از سود پیروزی بیشتر و ارادهٔ حریف را در محاسبهٔ شکست غرق کند.
🔹
خطر اصلی اما پالس مذاکره در لحظه‌ای است که  ادراک عدم پیروزی در دشمن هنوز تثبیت نشده.
🔹
سیگنال گفت‌وگو در این شرایط سنگ مفت و گنجشک مفت نیست و می‌تواند پیام قدرت را مخدوش و زمان را به نفع حریف بازگرداند.
🔹
در محاصره، آزمون و خطا تجمل است. ایران باید زمان را فشرده کند، نه آنکه با تردید آن را بفروشد. صلح، وقتی می‌آید که حریف به عدم امکان پیروزی باور کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/467980" target="_blank">📅 17:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467973">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb5NORyF6Kocoe7LN3RJsCmanfZ3tfE-1BdSx0K6u19zpiIaZz-meu_0cVxdF53ogQXsX5Izd4OEUzQScZ2ETIPPhcr9_nje-rD0qrJfLN3LJWTabT-OiS0Fqf3FDPCDfYp6QiY-Iz4_sZmAoprdLSEsftG2jpPKZ9FyQmA38mKywuR1iSW7jX1ipupCkUSZ8lUzbEJXHlFc192o0mUTwhiLq2cxt8XWsgqW_1g3EBbxqF5wCHD0gWfPIeh6oHKpinYI1QcWC8PX6aZbSfiBm7aPqk0LBnkRpbQtn6ci10xwf9ZzgBqhBHxuQ9mpoxyIsYktKJ-1cyH-9O8h8yQiqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoZBoZjnrwuhKl1nmgDWD9hbq4Bd_CoedkglUsstv_DvUnaP6fxH4lott8BQRZzqQCjFaB53cvnKvucYVvc7cr2TrG9_rWDRoh3iekNA-hmvXW2GRTortCUYJE9FkZShDp7YkgJ703jFiH9vZ2v20--fxVdNRwbeAKo8t-xhIDw4L4fZOPmOK9z10q9joV3YMZGf3cwlmFRpF_5RDsryxx7Fkq8V2d69pwR5WGacqqmT5lNJKYMUh9hqOEO7ij76h_uH-HZv19Oa8Leu804kNLesakx44ECYfi9VaPi_tMM9KLj3CjsORmabAwvzZzoOwqmb-q6ZVUxxd97itWYYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5L09LnwCzutoRAK9iow0i0EY77N_J6JDyag5BWW2OA0r7tNYBwifVk98x8GYxpXicQ-9JzCdrJ_BrZVNQ5SvyVn4Hz3Tmtwj9_4cIVslzZNwCKzX_EWn7Txt_ChNGny_VFerabBBgnfmJBT2O6yN1rfTuLOSDukM9rZdm_lWL-BeSPiJTr38LwC5MpSwFUP9mq6_IMS7uuSI0pKHd3OMK6Wa9O6MVsIVACsBDaArbKHDlI-C-QQ4GrnltaQiIvvTRK5Tn2R1w8oW6wBV4cEDDCPwZKlR3eeV0QXGBKWKQ91uajehrbrUlmRDemHuAZKPnKBS_swAkgne9mESfR1Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjDCilnvUshb1LSSu8DybdTVmS0PT-Jk0uI9WWmHFw7zecY4Bt8r9B8ugUQ3tktAFRP7IwhHggRtT0w8zsCZw798dukRJ0maENQjEZrRElW3zyke2Ere-Cg3PYYmgie1qPdUwMR4_irYVEKmkZ17qhYNiI8Ay6NOgdUjlNwmN8G7rYKUZIgtWPnp0Lk47XqHwVmZIAIo2jh4ca_zAdug-nMnHHqypOIkftacpkLW9IHWhhX0ygeUm7jaWoz52Cyy1uG4qAQk-DnR7y8xo0SF44IMrswsOhTzfJHnNci5zS6Vaq2WN76N2AVenmRXzIJQar_SfInmXXD2G5f2jK_pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTI1eB9lRX1Uv1hFltXXf8byg_Q9wsmZc2NeP1VSvROj2fii89gBMAxg0EXBB8_BpFvM5R9qVgahHikWolwaaFTVDMPHrBWoKjQ0wbDZWMU0jH7w_PENEkV1x6N9xxjtdYk1pfXU8JHb5MD0nykw_JgcNcjmMjVpGxrI2npu-ztq6Ef77k3G8fOC_h0rOcbY6avhzOCoafWzw2PijiDko-v_mKnldTHrAN32fFyOBdhBw6fu4_6ef1YQh6XBGOeWuR30RgKQPmAuJP_HAMGpN-ASxZ2vzfl5ar8_Ts4DWQbaMTwDvUouM_TDAJZNQAQv2wj2xxk8goVhKf6wdFVlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyjHLbxcUPE3s_jjgT_v-16SyEnQv_Dik7FgX0sgm9DBwxxTpsWpGgX_77xHmslxXelekJP0VIEoXbDF6_OOJoSJow1ajlCFToxaMlCOMtdfmmenMzIWmkdnVXD3-v7t3H2NEbF9W_C0wGvxs_QBsu7WcLEnsnueX9Io5jZKX69a3_zayE5L1v_73Zb7NCxtsMitdn-tauuL2GZLn3D6kSsvusyiGdL5GGIEKTCoJAiBajKcDOl2Czkv2DLPJjU3R3IlOxb30EDMlT1-ALiMM5YJmqRA-VybRJ7NEyyAqO4qiKxl3DITkwl_FSo-IR1ZiSBWFO8oabl5wd1bD8C61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otVVRxYKfgT_OMYwQECAp4p-xSBiWIMwejOBHnf_QRkTsWsTKGquubAkiYKJ7LT9UCl5-4W6P4ogjx33qz0koj_SkYPUkKDzZiE6hTAYOAIyQ3Arf6kLjjcLIeCVracZyrPvoDBb05xx1FS02CWxQxMH8oYOVVy6XM_GpwnPXPy2ht768Wv4DbxVd5w0HR9YkhZq9YMPRrOnRtgg5BPcoDwIsA8edN3AGCRlUMP4HA_5IRP86lDq19q4ZhjtzobbrwvtKedLe3536hsam8l1MbtwaGLEIknFAX49zvMwgR5kbugg6hQoONdOfvdf2chkzMfp-_axKXr2g373RO0j-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جان‌فدایان باشت کهگیلویه‌وبویراحمد گرد هم آمدند
@Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/467973" target="_blank">📅 17:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467972">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/221c7424d4.mp4?token=U5ycJYiEREqsANznlkzETOHrGorHrCSiQvet4pbH2cum5kMxdQuxNQ1j71tobNUZwZA10tWdiCFidjBqmcrEA-74VlgGwjHwXsaMM7l43qXTMQpOby2XV_KDw_J1nUKXyTOLjIID_29pX9IpwOpPjWT1q2e7UZjo-NXtACkCGo9kp8cl-SDrXE2DZzvpdI5iOJcnwkE__5dYZKAti3qPc5wO2zQ8i1V6GhBzZeypQTByfadD9EXMu-ZN1-BQowTGcj7CCxCLa-N-vAbN-xzNBo4Tp8tgEmsh_r1jhpOYoj6ioZovfrSYmuxXsJDn6drcCFN5YANB-LgtwjjTOVZfBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/221c7424d4.mp4?token=U5ycJYiEREqsANznlkzETOHrGorHrCSiQvet4pbH2cum5kMxdQuxNQ1j71tobNUZwZA10tWdiCFidjBqmcrEA-74VlgGwjHwXsaMM7l43qXTMQpOby2XV_KDw_J1nUKXyTOLjIID_29pX9IpwOpPjWT1q2e7UZjo-NXtACkCGo9kp8cl-SDrXE2DZzvpdI5iOJcnwkE__5dYZKAti3qPc5wO2zQ8i1V6GhBzZeypQTByfadD9EXMu-ZN1-BQowTGcj7CCxCLa-N-vAbN-xzNBo4Tp8tgEmsh_r1jhpOYoj6ioZovfrSYmuxXsJDn6drcCFN5YANB-LgtwjjTOVZfBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه: سومین نفتکش سوپر تانکر طی دو روز گذشته در تنگۀ هرمز مورد اصابت قرار گرفت
🔹
روابط عمومی نیروی دریایی سپاه: صبح امروز سومین نفتکش متخلف از نوع سوپر تانکر در تنگه هرمز مورد اصابت قرار گرفت و دچار آتش سوزی شد.
🔹
این نفتکش با خاموش نمودن سیستم…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/467972" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLm1DWP_tLtLKkWvKZXyDMrQA0DOdTUvRo8NEm1M4-HLiq5D2nNI8646CuYF1obdjLZVykNRxpp56PmsP-Vnf-bS-atA9J-1PDpxfXmLYIzl8Yc9xjxLs1U3tbfOQ3JE_Y9i-IjLAB5gRW_ORlyxvvAPeUMUUJsFDhS2qFMYd6qpJu5unWI8FheAvmzbk_9c74Jm6KTQnY1SM--pL8RcxHfpKsZQlIh1YGofod4bHhLiViOgcKMt64kODV0kDeWCR096tKH0QsZ1xd7pK0BWR8sjpfDBX-Y9lN3fI1LNavgf_l-yK_Erc4lW4tzhXIhAlWRhkC6egZws1OaHCMBV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سومین نفتکش متخلف امروز به مین دریایی برخورد کرد و دچار آتش‌سوزی شدید شد
🔹
نیروی دریایی سپاه: یک نفتکش شاتل حامل ۷۵۰ هزار بشکه نفت خام، بعدازظهر امروز با بی‌توجهی به هشدارها و اخطارهای نیروی دریایی سپاه، تلاش کرد از مسیر غیرمجاز عبور کند و درپی برخورد با…</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/467970" target="_blank">📅 17:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467969">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712d3833ba.mp4?token=ogUZspZ5IEyl9bkDGUosIYg--oZOdPLdtaxyks1BbXCNhUaCHyqFtTPiQl1smm4V1T6H98zmoSdcslwmrEABh9caUm8pp3GnxkweKU97HqYIXmZ8z-JV4rc21T8oJYIJrmF-VtHLBT1TKx-d0qfQg1S3yTW8xShPfS7FsOcaW807tOh5Y4SMjDPkPc00XC85fVU3ce-3MKQJFukP2yDjn8U-_6-fbOSAYNN27cBvECM9jXSRBE62LWJmNhZc5EkvC3HeqZUzvNAcj6yg3jZwUipYkXB7tvUwH07f0oNIvzN6TfwjJIw3kRkgl35E94g3WsyNz2XayHr8li2Uco2C7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712d3833ba.mp4?token=ogUZspZ5IEyl9bkDGUosIYg--oZOdPLdtaxyks1BbXCNhUaCHyqFtTPiQl1smm4V1T6H98zmoSdcslwmrEABh9caUm8pp3GnxkweKU97HqYIXmZ8z-JV4rc21T8oJYIJrmF-VtHLBT1TKx-d0qfQg1S3yTW8xShPfS7FsOcaW807tOh5Y4SMjDPkPc00XC85fVU3ce-3MKQJFukP2yDjn8U-_6-fbOSAYNN27cBvECM9jXSRBE62LWJmNhZc5EkvC3HeqZUzvNAcj6yg3jZwUipYkXB7tvUwH07f0oNIvzN6TfwjJIw3kRkgl35E94g3WsyNz2XayHr8li2Uco2C7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دادگاه رسیدگی به جنایات منافقین: دولت‌های اروپایی میزبان منافقین مکلف به استرداد متهمان به ایران هستند
🔹
بر پایه رویۀ قضایی بین‌المللی، کسانی که متهم به جرایم تروریستی و اقدامات خشونت‌بار هستند مشمول پناهندگی سیاسی نیستند.
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/467969" target="_blank">📅 17:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467962">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnpicYsjLgknsmEHOKnT3z_fEElqLeSfqwWRrobNgFgNNik_c6psURsKxnXgyJ0xhoiUWyn9FC8010Ur9E7N4Ae1x36GSDLVmaJhiOuE8-vr0tnqsMWKG-rxcdgEXE_-gIq3eCF_PR8gGYI6T2h27gEXagkkMYByppmRxXNzgWqe84pvJqZWeOUpZ4AZ1B2il9VpYe-tQUprb189q0dgfaZxq030CbK9HrLLPfuimq_UCIj4VsavOFtzQspFdPKW4Z_09kL9B2M-btPSoLKxu_Vnsf96L-0zGKRQsDN69UPvfoBPaGQoyTAt2kaITdWaK419YmikCx3vqUBmC4kIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCeSfaXIsxOUU_N7wQGRGpIkYJchGzaZRNC_k98j9RXJJkC-5msPYbi0MrA5vS-77IHyskDcpNI09w2BK1kQLBHCO_5s0UXiE-bwoftF7wJIfkPgNzLZttsHWn4e6MTFd3jz2CGkbgxx4EvII4TYUaQypFlgu0dPpS0lkWYWvIyH8iU8dknuGWhh89s-Lc0rKg3nLRiAZZnC0QqCl9QjGmNCQ6sYQSyfj9EWNzpCv9Jcgwsnhi4xRt5xAIbkAFoqp05Z4tKicuDkH9sSEulmP61V2SsFVh5pzBsOBZVLgVDSg3hI6xuf2KjEgFoFh6E_iY-5guyQD0AXN5h0h0lLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFoXqIEkT5Eo9uvaeSxIUjoknY7zBEIcZsVCbgjMfHRp5phaazWuZJWMO1KAFVmQ8Ae6StO2TzVDynKnvRwr8uwhKcNhTwh2e1MHYEi0GDHgLfNBYKyfZ5IzEx4Xr78zxVQ2bplXGgZ_KlkfXd8dSzohPhvQYvcgCx_iq7Mj60VzsEmn9T6Lysn5OIOIcqp_TEWY0d5rsJoepoddgyGba1AbqGANkzcEXCfXmX1IyxvxJhJsLocUtKaOTZ44RMBP7lvkEQj198KYGxNV5n4YTZC_Xy1ze6U_pPpj9O3qDy_JNkhfFnjAcVmjNx9of1jsHtiVhM1n8FQbXZsEErRuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mb6xV9L1dizQk0Devs7zfswIjSmOT2IPn1TbABFQdIe1YLN4bRfGuUjZXFCPhJF5EOaDDCv2TxujmVhoCWEHhya0-5TjG_8xmNHC2a-Avo_YfxGhPt4xMb3uZ62PEjK7zQDjfnGKlSsJ8e3JiPWy3Th-q4pOTy0WRwoeOlJCavgUfRanxFPPVZZ21yg2VGAgIpfmZvng3YvSAkq1ImKIFzUb0yDJoxJrcu1p3SB6twaYLRQduQuK0TXjw4qPYle78iIlkfwDmFefaRfaUDDfKnVa-LMsEX8zmAqLuN2dH1DpNLiCMbztYecafgBRCZUWWGCc9uQFuLCBD3uf7WnBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTGodcKHxFou8sR_l645F-dAr3LBSMe9EsdCLshQxtCjd4JtjNMPdPhsFwQ6c0yjhriOLCQbKv9UxjND0x6YHtwN5CevZtItkV7MhsSJ8eUvbqpUor37fsHVgQP-6GP-5H7XHzRAoAZS8W0YfJonpliAnZ0-T-kw5o9Ag3mFCEv2AAgN1l0bVeuLbhMdc7axpizPNfvcwKyWBsN8MobFuYgxYxMUEcGA2ATS5nCDjafpEub6P-5xz4wkW7SIgZvaBtXgA5OXkQfb8xF_6CK7TU6gYr4yUlg7_LojUdXzEHxcwoH7W9D1LwbfOZwLxai3LjTuwiAwPWmeoKjiWi7mcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8oTU8RbueeVxCjccpTRgIiEuRdtgSRDgUj6sHW5lba4HoO-hUwKJNXc7tI43N2LfrHNPy7a7HxA_4aWFeGd3T_SLDZsVwp3KiNE1bjYvM5G_CzyOn4GM4KjQLjfiwAvAgdE1YmIEgNgCgYZJTuSOaFgB1fDxFVP4gtr-DIxrjV-by3RXDvI4SMy6F5ZOdbpT8aUVmv3lrMWyxu3HmP0ZLfdHds4uDvH_YQ9Am7XdtGzFtHJRKTMgNzluuCrebjFiov6XdjedK8esHMlvutKXHRYVPsQJTquoNTkLqyHdWoK7PeJ18_xn-KvE6-2p5dv7S5PCOVNeRm9jtAZlB5K-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMzxLMy79McyvBec6AJ92iH0-y4VHqNyj7RZEiOwUHqJ74_2OiMPkPXVhdvB3IGO6_PWNYz_WeetFZyNFthYR-4RIjen9Ht-D2q-jcCDHBk85rUMAUvnansVfPuObB8OLuaGAReZ1b72bEuIW9rUr5jztmWhADFk0dyE2ol9nzGubj4UaA-E8vad-OPKvjKQpf2M_T60C9dRgXdjaFVH8NkwWoxqr2e4a4pEEeUxrBf8DE77rHWtWajuh0pn6wGF-IO0FCZriGArpwRZXKCGZle2qjlySvy1Q4OGTiu92kCp2zWraf91z3qP7fDav7qfOkWccf4Uw2-l-whwq1GYMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کرج، شهر اقوام و فرهنگ‌ها
🔸
۲۰ مهر به‌عنوان روز کرج، شهری با پیشینه‌ای تاریخی و فرهنگی غنی نامیده شده است.
عکاس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/467962" target="_blank">📅 16:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467961">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbARstdho1OYz_Q5QHWY1SEY1dlW8CCu1TAcazOcF0fnBIjv-TBC0XOuVRFxc0hlI-kq0dWevr3ph0t9ykwtM4rh3RNhte5VN8Dnx32FwDfp1dVWXRHlPoUUqUA1PX8VAjZ86z3G-WkeadO0Jot7AYW8O_Hc1CS9cQafsY-4e29Y0o9cWJvMeSpopCmVsEdwDa2QR4PKaxmQoLhEyWE218_Orxxa2g3ezyNx2Lp96-ZMpk53lRcVTUTyC-MK__vhZ8WMntaSH0riyACRTyq5BmKt-ShbPGVUAXoc0bMinKHiGFT5PuztomdXTb-r4m9MILNIHxdPYIyl8ikVun1WYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: دلار باز هم ارزان‌تر می‌شود
🔹
رئیس بانک مرکزی: روند رشد نرخ دلار با اقدامات متعدد بانک مرکزی کاهشی شده و این «روند کاهشی» ادامه خواهد داشت.
🔹
دشمن در تلاش است با «شوک رسانه‌ای و اخبار جعلی و دروغ»، این روند را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/467961" target="_blank">📅 16:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467960">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZn4K57hiStGmY_WE9v8eYHtupDvBfgGUn9taEDbv386l3oh9EKAvonq0U9xWeQJawbx5VQHmfTOCOv3lg33p04Oj2H8frBlNh_K6sJ2xWSDDMhWUYWfKKkVNVicsItwZvYFpy9Rhh_uSm2oCsfdBK-mxWJsJw_dn3ltnMACXM3pWN82g92Zo2fTLzidi9GBZcfO_JM0_bizQeNKouKGkkpy_Yrkbz_ADC7NPrIB_mJYuhdrctnmQF9ax3NFg3yH23WprR6CP0Q3Ei00psDHtq4EXFbRIlKzuUOJw_FCCjbFpl0HzslCAQE5_ecaxQfZ12ef1w_Wjf_gi6W0867MNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشهٔ محاصرهٔ دریایی برای فلج‌سازی شریان تجارت کشور خنثی شد
🔹
رئیس سازمان توسعهٔ تجارت ایران: هدف نقشهٔ محاصرهٔ دریایی این بود که ۷۵ درصد وزن تجارت خارجی ما در حوزهٔ واردات و صادرات که از طریق خلیج فارس و دریای عمان جابه‌جا می‌شد از بین برود، اما اتفاق دیگری رقم خورد.
🔹
از لحاظ وزنی ما فقط حدود ۳۴ درصد از تجارت خود را از دست دادیم. یعنی در واقع بیش از ۴۰ درصد از آنچه که قرار بود تحت محاصره قرار گیرد نجات پیدا کرد.
🔹
پیش از آغاز تنش‌ها، بخش اصلی بار صادرات و واردات کشور از مسیرهای دریایی جنوب جابه‌جا می‌شد. با ایجاد محاصرهٔ دریایی، مسیرهای ریلی و جاده‌ای به‌سرعت به خط شدند تا بار مبادلات را به دوش بکشند.
🔹
از طریق کریدورهای جایگزین جاده‌ای و ریلی صادرات و واردات کشور انجام شده است بطوری که در واردات کالاهای اساسی هیچ مشکلی نداریم و صادرات کالاهایی که صرفه‌ اقتصادی دارد هم ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/467960" target="_blank">📅 16:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467959">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7aab48d0.mp4?token=pMqajnRFJeiCFegeF5m0VupYUoVSSfLE9vzSC6WnvRtUv68HYuWjVw5-4YR87EKSb1bkXXvAa6ubuenu_SKvdmaHn3EoJL8rDy0-FkLsSl_dh-NEXvNBOG6vhKIZgcsrdcI-J_l7Jn6WpppAbNiMKKiwWJJUb5ohIP5LGFLGjVNW19A8y6sLJciwhYUmv3QQE_mUhSHWhB6X6r3wRhf0eOBJ12oik6659QgQQOeeYbsILhN0Uqd5E-kzXZdA0ErSZ3L7P7fPMzq5wIOfuqTzEQc8Xu99edN8ezW0sxvplyKZnfhleaiut24eckDcpX_kKTPm3zoWzOQZxKRKJv_Xaxw6M5zw1qSVdX0mTKdA8wsvtissHmVmBTUdm5slJZSa96qxbEdz_0t0cKHTDgxRjT6p5eGMHnLJ_nM36JmzInCPvz7B9v70ji15Ra0iiNE3qEqdRgI-Tg0YJ59q5OEk7QekqxRKLf7GdN8jkh_C7nE2wcNgFitqKu5Dc0CDNULe-CTXj5J4S0j8PssbGiQaNWaG295EOAMQpFdFrP0fNgXQEjew1j7PHDAkVPIbBkM55AfpLPmCvxO3SlFPBlrn22o6h9z-bk2xAa2beVxk1-C2m6SrM8D4xvNaHg3aanIgUzimP7cJM7WdJWzmD4KXQ7q5vnGd9iXMyFtAjLUbI4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7aab48d0.mp4?token=pMqajnRFJeiCFegeF5m0VupYUoVSSfLE9vzSC6WnvRtUv68HYuWjVw5-4YR87EKSb1bkXXvAa6ubuenu_SKvdmaHn3EoJL8rDy0-FkLsSl_dh-NEXvNBOG6vhKIZgcsrdcI-J_l7Jn6WpppAbNiMKKiwWJJUb5ohIP5LGFLGjVNW19A8y6sLJciwhYUmv3QQE_mUhSHWhB6X6r3wRhf0eOBJ12oik6659QgQQOeeYbsILhN0Uqd5E-kzXZdA0ErSZ3L7P7fPMzq5wIOfuqTzEQc8Xu99edN8ezW0sxvplyKZnfhleaiut24eckDcpX_kKTPm3zoWzOQZxKRKJv_Xaxw6M5zw1qSVdX0mTKdA8wsvtissHmVmBTUdm5slJZSa96qxbEdz_0t0cKHTDgxRjT6p5eGMHnLJ_nM36JmzInCPvz7B9v70ji15Ra0iiNE3qEqdRgI-Tg0YJ59q5OEk7QekqxRKLf7GdN8jkh_C7nE2wcNgFitqKu5Dc0CDNULe-CTXj5J4S0j8PssbGiQaNWaG295EOAMQpFdFrP0fNgXQEjew1j7PHDAkVPIbBkM55AfpLPmCvxO3SlFPBlrn22o6h9z-bk2xAa2beVxk1-C2m6SrM8D4xvNaHg3aanIgUzimP7cJM7WdJWzmD4KXQ7q5vnGd9iXMyFtAjLUbI4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  سخنگوی نیروهای مسلح یمن: مزدوارن سعودی را وادار به فرار کردیم
🔹
یحیی سریع: نیروهای مسلح ما، یک عملیات پهپادی موشکی علیه تجمع‌های مزدوران سعودی در مناطق رأس العاره و السقیا انجام دادند که ده‌ها کشته و زخمی برجا گذاشت.
🔹
همچنین عملیات موشکی علیه یگان‌های…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/467959" target="_blank">📅 16:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWVgf_9W4uD-4e6_DNmepl8pupOFKfAfU3p4BPYXsvP_2uEvSwZYKUkclRh-3-LgUBtxapdMw7cviwzTv5nMwkWpcN9eYHQ81ssR8qCARYKN9EjDAIFxHQ-GBwTpvVBYHF1gKwYWbL_fY2DpQgylnIPmfAEIf5UK9c4VYUUAV0OZHDmxxBxvYw60dvU7vDQUkVILcS4qOT-jIM2pBlFlBvKqdRRJheff35CqtO2Yo9VLeUap3IqA3UvhqXWXc3nNEZ3ZYf9p2kRGEtds-Q53O6aVriJyhLiUcSrnXrDmcED88NHHML1jSK4jMD3SL0txipTyPX3qUvTek0CRuJRp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Idsc1s9lyR4-8ju60KLoYsRujjNL8Pvmr94_Ti9VCbiQpPmdzFj6ikNHMYeZUraEv0bhzDqXL6i3B8E0QxkFpzWBxdzCrV6Xhvs_QPZBJtJ12FNccIiHUfeo60kR0StL3v8yTl5qJ5C9swpfqY7X4LGrKR3IUNz5W3h4nQlocAA4fvx8rIc3RRBxzVXKDFqZ0yJTqj2_cfQj4cL5KJQJ-BKDAmbv2DY2NNIV_nfp0Phx17mWM8nmPh43_ueXzNkSGRsu48Txz56xqdsG3KPaF-H1UfV-_zllp9hBRp0ElmNmBAaAxaCFxYidokGB8h8znXSN_GaDhzx2d56kJWYAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTpi8jzjloTv_Podh5gDuVUD2zBY-8uu7oVSFuHcjLwq2mBYVAm8TStB5vzVJURcEL8S-HYKw0eR6jk5fWVzr340mO8DqkhqwF-7XRvH1C4y1fkJpcY6JdcDMVsrLEzbER_B3ELDYRClhkiLAdj2GVcbKlfwiA0_AnPNKYk2Wui_R08fc0vJ_c8SsLxYm2z__WOYPpX9azEeFdn_DBy9u__0T3giGz86YuNZbU85NZj5IuQ7Fpwx6bB0u9hnny0WXBlh5FERwlfyWYraePoRPy1hwPheRUu5ZXFMga_dSHZtLxFy2zYipnt3Q45OsbvnyX9aTSEL4N09qmuCJUC6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ylu-9qGh-dazltoUeU8xsjHh5BU5FHYq09nXt5EYrbwAcJDMvT-S2A6f50Pe0o2tWtk0ML4f0EJktffvyl_PN9etGJZjdu8Vci-IFdM0vQd1Cg_wBajgipopxXNnypZbX9rCY0DPUnzdjAlWC-SmKjX4PYdZ6XzwRiEs-h7IJoJ-V3D7cEpN30UiPfMLh5e8Nk3VxbKAsnAu2fm6MFe-tf4Ow5GJ_l_muFyPyh1ZOWTv8HsPRu1cHBUlHjnJ4kAsC56HICphgBlNrbvvcrNqqszIaZiOFlANkS0EZ2mMJmQqNfIDt1-M4TBZrNR5l3mqGXmhvIufNYvnbAn94Ona9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضور رهبر شهید انقلاب در حافظیه شیراز در سال ۱۳۸۷
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/467955" target="_blank">📅 16:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB_hX_XwOhUshHzjYdEii5JQcTchx5BQ_gLrrNH-W7ZFCLuKof2kexLG6RAauXkVvME21oJaYoBnMrW8otcwYVOlqlcQMPQrjB-7PyaNTeLnkI9k3ybhU1GdianlSyu69BxOwjaLPy1mCJiL55EDypK3PAb2dJYobuHSjLaNcV4eZYo7pN24qndvlfcChfAv0CMvZHrPdRyYeLiqtYDQS3AxzhJAt4Qpimz-s86Fk4v5BqJAZpXA0hHl2YuxBuAfnWzceJ8S75by82pvy3vJGs4v7HlSN6TWMNFsxt-de2YV40D3uEXQRuKJIU06XwFUFuopoS_jlV2jyMgnVBAstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفر در وضعیت بسیار وخیم است.</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/467954" target="_blank">📅 16:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467953">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دسترسی ۵ پلتفرم رمزارزی به خدمات بانکی قطع شد
🔹
از ساعت ۱۶ امروز دسترسی ۵ پلتفرم صرافی رمزارزی به خدمات بانکی و برداشت غیرحضوری محدود می‌شود و کاربران این پلتفرم‌ها امکان واریز و برداشت وجه را نخواهند داشت.
🔹
طبق اطلاعات رسیده به خبرنگار فارس، تصمیم برای این اقدام در کمیته‌ای در مرکز ملی فضای مجازی اتخاذ شده و بانک مرکزی با ارسال نامه‌ای به بانک‌ها، اجرای آن را ابلاغ کرده است.
🔹
پیش از این خبر ایجاد اختلال چند صرافی رمزارزی در بازار ارز و تصمیم بانک مرکزی برای مسدود کردن یک‌طرفه حساب‌های بانکی این صرافی‌ها منتشر شده بود.
🔹
با این حال صرافی رمزارزی نوبیتکس گفته است که این محدودیت به دلیل پافشاری این صرافی‌ها بر حفظ حریم خصوصی کاربران و خودداری از ارائه اطلاعات آن‌ها اعمال می‌شود.
🔹
این محدودیت سه روزه خواهد بود با این حال احتمال تمدید آن نیز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/467953" target="_blank">📅 16:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU2g7rz9pm2cs-lBnxXPwYzbepIYpv-p4GMm8Klp4vHIJvKwXFnIEy8laq97fz0hx2eL0pHRHDlgRKSznGpPIJoDSWiE7yG-uV4MkJrPktICGrKcfb0VbqFsBSUXs_9-awzPWBAys9VHCEHqLz4r7mGVYNOtOtR7mq0vwYbXuuDaNVid5RHLUK9njPuA4fX5b_mgmGezwZNIof89g-6L77yI3OjZG3nD4CAQwBDl3BWJKBjnZzvgV1SXXK94kB8H4h6HnkP0pe2n5jlmRvB8WQXmFIaZE2AlsIkfUFbDJa_HtWojOT53v8sGURy4xF4wMRqrWldfTnMYdwZ3-1H59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌وال‌استریت‌ژورنال: تلاش حکومت سعودی برای تبدیل‌شدن به قطب هوش مصنوعی اکنون با خطرات جدیدی روبه‌روست؛ چراکه دیتاسنترها جزو اهداف [یمن] هستند. @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/467952" target="_blank">📅 16:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9198aee7.mp4?token=L381Jgqxbrxu_tQhdYC7QU0dYu8JmJHbm0YWQlzHhTE19KM8ZRyz4wXhpZ-Xg32-9CZ5LJkvFBwUpYwhHCkVKmOmPaS5TBYmlaYWgIqEzaa3aJsmIjawv3HQe5qKNq8Qkq36a_MlWKAUN6Sx5fjz5XR06Z0Ri3li5XbkT28wFDto7uAQetiDxRsRB9uvdnFbULIUKc81nAGPUdR_MR0W3nLh4jIeMTDKnMAZgPtrESPXWpfVf4ui4zPQmOQLp9N3D4C2wWg_ncQf_yKsNTJ2SxeajmqtXAPjwR68TP38dsO3PDo9VPrMxJkmBfOqxl3h_W8Z8gadoa__FuppoNYmHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9198aee7.mp4?token=L381Jgqxbrxu_tQhdYC7QU0dYu8JmJHbm0YWQlzHhTE19KM8ZRyz4wXhpZ-Xg32-9CZ5LJkvFBwUpYwhHCkVKmOmPaS5TBYmlaYWgIqEzaa3aJsmIjawv3HQe5qKNq8Qkq36a_MlWKAUN6Sx5fjz5XR06Z0Ri3li5XbkT28wFDto7uAQetiDxRsRB9uvdnFbULIUKc81nAGPUdR_MR0W3nLh4jIeMTDKnMAZgPtrESPXWpfVf4ui4zPQmOQLp9N3D4C2wWg_ncQf_yKsNTJ2SxeajmqtXAPjwR68TP38dsO3PDo9VPrMxJkmBfOqxl3h_W8Z8gadoa__FuppoNYmHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انفجار در شمال فلسطین اشغالی با دست‌کم ۱۰ مجروح
🔹
کانال ۱۲ رژیم صهیونیستی از انفجاری در مرز با لبنان خبر دادند که بر اثر آن دست‌کم ۱۰ صهیونیست مجروح شده‌اند و برخی از آن‌ها در وضعیت وخیم قرار دارند.
🔹
برخی منابع صهیونیستی ادعا کرده‌اند که این حادثه بر اثر…</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/467951" target="_blank">📅 16:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467949">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
انفجار در شمال فلسطین اشغالی با دست‌کم ۱۰ مجروح
🔹
کانال ۱۲ رژیم صهیونیستی از انفجاری در مرز با لبنان خبر دادند که بر اثر آن دست‌کم ۱۰ صهیونیست مجروح شده‌اند و برخی از آن‌ها در وضعیت وخیم قرار دارند.
🔹
برخی منابع صهیونیستی ادعا کرده‌اند که این حادثه بر اثر انفجار «مهمات باقی‌مانده از جنگ» اتفاق افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/467949" target="_blank">📅 15:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467948">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939fb64b57.mp4?token=cQGqj6Dt_n3xCuXhqCIdQKAvHU6AruHqzH8JwGkPrp_PtKU3mX_1o5TFLwpU2HyTwcH6heDCPJXPG4QnjiF_FWb8SH7x___Q4xFWF6w7jUbF4W7L_cazVnYCHjRdglBFrIBN3hECvBHy5MBR1jLss3EF7QcQocGii-qZcfnxeZ-MwnTjEGrrFyr1nICcEQIjDL483ExwlmJFOWp3u5cm2tUY7_lRTEqyMBcUdySp5Wv069fKij4vGp5MwqXK5hohVOiFjk-8G_8GrppzXybRV7e43z6TSbZUUp8_09TvdbWtFE_TaNNxJj5Ouvqhp9naNlA53m8YKp3o58VQjuuZXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939fb64b57.mp4?token=cQGqj6Dt_n3xCuXhqCIdQKAvHU6AruHqzH8JwGkPrp_PtKU3mX_1o5TFLwpU2HyTwcH6heDCPJXPG4QnjiF_FWb8SH7x___Q4xFWF6w7jUbF4W7L_cazVnYCHjRdglBFrIBN3hECvBHy5MBR1jLss3EF7QcQocGii-qZcfnxeZ-MwnTjEGrrFyr1nICcEQIjDL483ExwlmJFOWp3u5cm2tUY7_lRTEqyMBcUdySp5Wv069fKij4vGp5MwqXK5hohVOiFjk-8G_8GrppzXybRV7e43z6TSbZUUp8_09TvdbWtFE_TaNNxJj5Ouvqhp9naNlA53m8YKp3o58VQjuuZXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: شهید ایزدی ارتباط عمیقی با گروه‌های فلسطینی داشت و مثل فرزند خودش با آن‌ها رفتار می‌کرد
🔹
حاج رمضان هر سال با گروه‌های فلسطینی جلسهٔ افطاری برگزار می‌کرد و با تمام گروه‌های فلسطینی ارتباط داشت. @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/467948" target="_blank">📅 15:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467947">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وال‌استریت‌ژورنال: این روزها بن‌سلمان میان کاخ‌های به‌شدت محافظت‌شده‌ای که مجهز به پناهگاه هستند در رفت‌وآمد است و توسط یک تیم امنیتی گلچین‌شده محافظت می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/467947" target="_blank">📅 15:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467946">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd2cb0f3d.mp4?token=VKQmMr3p5J3DD5bJQNckI9Fy4lWkDhOHIwuFj7lNaNbgFAcaxk9N-0yontWeJ8SWVa-c7EJhhS23nTK54i-hrhDEq3wQFFqISlwJHuJqzk819DUwsFg3zFuVCWwlOkzEnrZpFfC6JbMAyA6FSSvgNb3v7-DL3j23LfAgietPAD-mJPJNRUharNM1eKsrwxcxN6qv6q72cvozB8JxU2bC9w2M_fi301ZDjyoOZVcQuBdMqgclD8Y4lUQvRbXcHr76ezprjLVrPzktE57Aopxxb2qmJSU-_Ys9xoloAR63YnWY7VyrQs4rIAmhMMTZYUkle4qxMn4CW-e1nSABTgiRjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd2cb0f3d.mp4?token=VKQmMr3p5J3DD5bJQNckI9Fy4lWkDhOHIwuFj7lNaNbgFAcaxk9N-0yontWeJ8SWVa-c7EJhhS23nTK54i-hrhDEq3wQFFqISlwJHuJqzk819DUwsFg3zFuVCWwlOkzEnrZpFfC6JbMAyA6FSSvgNb3v7-DL3j23LfAgietPAD-mJPJNRUharNM1eKsrwxcxN6qv6q72cvozB8JxU2bC9w2M_fi301ZDjyoOZVcQuBdMqgclD8Y4lUQvRbXcHr76ezprjLVrPzktE57Aopxxb2qmJSU-_Ys9xoloAR63YnWY7VyrQs4rIAmhMMTZYUkle4qxMn4CW-e1nSABTgiRjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر پیشین ایران در بیروت: پیجر من قبل‌از انفجار به‌صورت فینگلیش نوشت «یک پیام فوری دارید»
🔹
اولین‌بار بود که با چنین پیامی مواجه می‌شدم؛ روی صفحهٔ پیجر نوشته بود که «برای مشاهدهٔ پیام دکمه را فشار دهید» و به‌محض فشاردادن دکمه، پیجر منفجر شد. @Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/467946" target="_blank">📅 15:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467945">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5RavMaL-_SBx0DiPBbsMYlLs6bzVwjSAj3pCSXEJ5ezULARlLQE4xrAwvWGWKQURbgSzefWrdOi0TxRhKNk6Ukq_Sy30O7AcHFKND_T3XyUWTnFdEb7bgF66F1RLQTLIIp95PgJ7HrE5W44fL6K7GrB6-6EdUPcCufPuAkd84GzfS1g0WKGQrwl3gXCzVU3_TuEoJjOkh8TOKhj9RZsx260tv8OpzKCem7AXls8fPgHepIemff9JXEV_kh0ahBySmhONp9zf9cqMlzkpiDsBuKXy67kGgQ2YbAK-Weqvpgh2KmDSuGIKEk95XR7PWQMcTjoBdsi7CCrXk1jKRaXuVh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5RavMaL-_SBx0DiPBbsMYlLs6bzVwjSAj3pCSXEJ5ezULARlLQE4xrAwvWGWKQURbgSzefWrdOi0TxRhKNk6Ukq_Sy30O7AcHFKND_T3XyUWTnFdEb7bgF66F1RLQTLIIp95PgJ7HrE5W44fL6K7GrB6-6EdUPcCufPuAkd84GzfS1g0WKGQrwl3gXCzVU3_TuEoJjOkh8TOKhj9RZsx260tv8OpzKCem7AXls8fPgHepIemff9JXEV_kh0ahBySmhONp9zf9cqMlzkpiDsBuKXy67kGgQ2YbAK-Weqvpgh2KmDSuGIKEk95XR7PWQMcTjoBdsi7CCrXk1jKRaXuVh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: قرار بود پیجرها بررسی شود و برای همین عملیات را زودتر اجرا کردند
🔹
نتانیاهو پس‌از حادثهٔ پیجرها گفته بود «کاری کرده‌ایم نیروهای حزب‌الله از جامعه طرد شوند» اما حالا جانبازهای پیجر در لبنان احترام خیلی بالایی دارند.
🔹
حزب‌الله به‌دلیل مشاهدهٔ بعضی…</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/467945" target="_blank">📅 15:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467944">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434a367fce.mp4?token=LjodfcLGhrA5HKhVLtX2KAFGxXqpJc9gzwVjTGcJbKYYY7755GJWBYx9NAbM7ZacDu2focoYureSYzd-Rip_utnv1o7ZMQtH7g-8N-yQ6DRvTg6aH4J5xZe0-nV_543l3iT_Lj7NltzrzlsgOUhfIP-XEoKJ1qEwLE-xTHPJq8c1OznDtFfo_bfk-JDksH2662wzCMKv7zoIXWRaxtt2bRBhNk9u79cVmPZaLVuZkGT7k-uYBQe_3comjCEBVT5m_FU_EM29uC4WROxkn_pUgW3HT6BHHzcyGr3KvrovK1BAFSP0An8Rg4o1mXYdVFP3uvXJkmaSD5Plf-YY0Lf2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434a367fce.mp4?token=LjodfcLGhrA5HKhVLtX2KAFGxXqpJc9gzwVjTGcJbKYYY7755GJWBYx9NAbM7ZacDu2focoYureSYzd-Rip_utnv1o7ZMQtH7g-8N-yQ6DRvTg6aH4J5xZe0-nV_543l3iT_Lj7NltzrzlsgOUhfIP-XEoKJ1qEwLE-xTHPJq8c1OznDtFfo_bfk-JDksH2662wzCMKv7zoIXWRaxtt2bRBhNk9u79cVmPZaLVuZkGT7k-uYBQe_3comjCEBVT5m_FU_EM29uC4WROxkn_pUgW3HT6BHHzcyGr3KvrovK1BAFSP0An8Rg4o1mXYdVFP3uvXJkmaSD5Plf-YY0Lf2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا ایران به مغز دیجیتال آمریکا در منطقه حمله کرد؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/467944" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAkGrty_K1GKyl8xwJcGJ_Hjc2Klg-YRfQ_KhQ8gZuRnoRmRjUcyLeU5N_2AeDJ8tov-tl2kjt6hBE_95nbRGhkYbBoCzAaA8HCG_MbJpvq0Sziuqewh2ENCsF4Q45_rWphHwHgz94zapwY9El04QZZnCSLVGm1W_mng6GWZlWsTOxGph93wwETaZNXg0oOSOLDutkYs8S9tmAL82snLGIM7fvRU96zEy92HKtEEFk95_GslOBat3fTlx5v-fM0TZjdop26KDu09fqWhS49HlIaaq2XGZFO_5zgtBywN-yLMJ9vGxq7JDmGHbdsBIsB86ZhXpBKZ0r_SAy9Ft5SpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجاهد: هدف آمریکا از مذاکره هسته‌ای؛ «مشروعیت‌بخشی به جنگ» است
🔹
معاون دفتر رئیس‌جمهور شهید: مذاکرۀ هسته‌ای برای آمریکا ابزاری برای مشروعیت‌بخشی به اقدام جنگی و نگه‌داشتن سایه جنگ بر سر ایران است. در این منطق، ایران از پیش متهم است و آمریکا خود را مدعی‌العموم و قاضی‌ای می‌داند که رأی خود را دست‌کم بیست‌وپنج سال پیش صادر کرده است.
🔹
غربی‌ها در بیست‌وپنج سال گذشته، هیچ‌گاه نپذیرفتند که فعالیت‌های هسته‌ای ایران صلح‌آمیز است. آمریکا میز مذاکره را ترک کرد تا به دنیا بگوید محل نزاع با ایران مسئله هسته‌ای است؛ سپس با همان بهانه تکراری، حمله نظامی کرد.
🔹
مذاکره هسته‌ای بدون اجرای تعهدات پایان جنگ، چیزی جز بازتولید چرخه فشار، تهدید و جنگ نخواهد بود. این مذاکره نه‌تنها به خاتمه جنگ نمی‌انجامد، بلکه می‌تواند به مشروعیت‌بخشی به جنگ مجدد و تداوم سایه تهدید بر سر ایران منجر شود.
🔹
راه پایان جنگ، ایستادگی و تحمیل هزینه و فشار به آمریکا برای اجرای تعهداتش است.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/467943" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467942">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4ce1f7eb.mp4?token=DjNa6BTD6a6ejGvp2ml0GTBTTl-lLNzmyrNYQ2VIp1uOHMzPWdh4hrK6MbffbvcEgYGX-IgTVJ1vnz0RfxoRX453Bpa_hzh8UgDGfZf1CbYFPdmJJo8SiR8U8d_zllkJPo5i0-laAJ0EYmt_kaotCj_A1GC9v1Z0xdFMtn6gPQqVu35NOL7Y5x_OnxUTLI3T1g9YEVf0ltCydjBNxGZv-sLWEHl406AkWsHd2vgplmcOvcofneOh9EHO7B9sYGQPaqPPUYQIx6BYTUiGm_W198azHxr_GiTgi3hpSpYB1_9Xh03jy777jGxGwe_HVXT39mLDsw42Neq2m99Rxg0HnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4ce1f7eb.mp4?token=DjNa6BTD6a6ejGvp2ml0GTBTTl-lLNzmyrNYQ2VIp1uOHMzPWdh4hrK6MbffbvcEgYGX-IgTVJ1vnz0RfxoRX453Bpa_hzh8UgDGfZf1CbYFPdmJJo8SiR8U8d_zllkJPo5i0-laAJ0EYmt_kaotCj_A1GC9v1Z0xdFMtn6gPQqVu35NOL7Y5x_OnxUTLI3T1g9YEVf0ltCydjBNxGZv-sLWEHl406AkWsHd2vgplmcOvcofneOh9EHO7B9sYGQPaqPPUYQIx6BYTUiGm_W198azHxr_GiTgi3hpSpYB1_9Xh03jy777jGxGwe_HVXT39mLDsw42Neq2m99Rxg0HnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جانشین فرمانده نیروی دریایی ارتش: متناسب با نقاط ضعف آمریکا تسلیحات جدید ساخته‌ایم
🔹
دریادار بمانی: در برابر تاکتیک‌های جدید دشمن، ایران نیز تاکتیک‌های جدیدی به کار می‌گیرد.
🔹
پس از ضربات ایران، دشمن عقب‌نشینی گسترده‌ای از مرزهای دریایی ایران داشته و اکنون در مقایسه با جنگ تحمیلی سوم، در بیشترین فاصله از مرزهای ایران قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/467942" target="_blank">📅 15:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467940">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0930038d1c.mp4?token=O2H1dRKW5DZ9kqIlx4Um2jq-prSc_uSdLVd_PVlltpqnAGaeD_kqb8EN8wUdngoHBvZMDb7XzfQMTpvnvpiRfbmh9LPiOY83oDqX2Atdyh_8EWVZDgvsB8rGAdr_awIo0qB6K2wZ-Np7o02o9wOUlTSkFM8uUDaK2QN2kY8e0OoonGkwqLiQ4CWYmfNcn15cgsoubQs_BOa6OB0exeiM5tqJfgv-yNLIV0qhYW-yNSfiQywRSNKbvRXSjnvax7Oq_ukwuT_eBS97MdoWS5o2fMdQxWzpqeD3VacL9q3dXplFJHwGgNeZColnZpQ5BY9-TOBiSc66jr1ae5dR3ccf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0930038d1c.mp4?token=O2H1dRKW5DZ9kqIlx4Um2jq-prSc_uSdLVd_PVlltpqnAGaeD_kqb8EN8wUdngoHBvZMDb7XzfQMTpvnvpiRfbmh9LPiOY83oDqX2Atdyh_8EWVZDgvsB8rGAdr_awIo0qB6K2wZ-Np7o02o9wOUlTSkFM8uUDaK2QN2kY8e0OoonGkwqLiQ4CWYmfNcn15cgsoubQs_BOa6OB0exeiM5tqJfgv-yNLIV0qhYW-yNSfiQywRSNKbvRXSjnvax7Oq_ukwuT_eBS97MdoWS5o2fMdQxWzpqeD3VacL9q3dXplFJHwGgNeZColnZpQ5BY9-TOBiSc66jr1ae5dR3ccf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: پس‌از ۷ اکتبر مشخص شد اسرائیل موبایل‌ها را ردیابی می‌کند؛ برای همین حزب‌الله به‌سمت استفاده از پیجر رفت
🔹
بعضی پیجرها از قبل وارد شده بود اما حدود ۵ هزار پیجر جدید هم وارد شد که در مسیر واردات، مقدار کمی مواد منفجره وارد باتری پیجرها شد.
🔹
واردات…</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/467940" target="_blank">📅 15:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68241bb1fa.mp4?token=uTknrRcwKZPNu3x-tG7J4Y4qxSn3RyN_qOj3dKPmitvapG0W79E3cWFAi89lk6KvfjJr3xbB1hOoHkK0_j2QM9PGTkMJApTuZETG-AuGWBEuc9qzhCONKT20S2H6zXqU-D6youUBp1XNzj_WVHQ66dZaRhe17NZCLUVwNsDm8hOaW6RwehAnkS4zHzMLrimoL3EUZMi1G5hjdP1VrbIK37L4lnxv-O9t3kQwt5s9knZRMMX1kjTvqtYmzw9ztbtnzxmDh9auVSoZN1YovBSV3ns4fasOXGaoD_q1xi2udMq32XrMkIrg1Z4AYcgNolfFQF_Y6vZnlxBVULrC2F2J3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68241bb1fa.mp4?token=uTknrRcwKZPNu3x-tG7J4Y4qxSn3RyN_qOj3dKPmitvapG0W79E3cWFAi89lk6KvfjJr3xbB1hOoHkK0_j2QM9PGTkMJApTuZETG-AuGWBEuc9qzhCONKT20S2H6zXqU-D6youUBp1XNzj_WVHQ66dZaRhe17NZCLUVwNsDm8hOaW6RwehAnkS4zHzMLrimoL3EUZMi1G5hjdP1VrbIK37L4lnxv-O9t3kQwt5s9knZRMMX1kjTvqtYmzw9ztbtnzxmDh9auVSoZN1YovBSV3ns4fasOXGaoD_q1xi2udMq32XrMkIrg1Z4AYcgNolfFQF_Y6vZnlxBVULrC2F2J3TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: شهید نصرالله پس‌از شهادت شهید هنیه و شهید شکر تصمیم به پاسخ گرفت
🔹
سفیر پیشین ایران در بیروت: همزمان با پاسخ حزب‌الله به شهادت شهید شکر و شهید هنیه علیه من شایعاتی مطرح کردند که «سفیر ایران به اسرائیل فرار کرده». @Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/467939" target="_blank">📅 14:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467938">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2ab366dbb.mp4?token=dufVRJIeeUVYXoFHAJPYdcIA5MYWIePZRK3daRLAZQOYzbrKQusDyJY24BA4Z0jkgWLEMhH_Ogjz02y9hzvgYHpyR9pnx9RK1UigTUu9wJtMWq1YO_OaipPJAsSpD-w1DuqphXIlu47Sodj8osUZgPuMUE-NpZs7deex0pPAjkuKzD0pO81yr8hbwLGajn36i9y4zYLW2HoXQIxmBeUssly96lldfy7qTN3r52FuulZHA7YOn39p35xXWV9r2EC_u80QRqpBernrqIMNbJkQTkpdVfXuxp0S-srX-zmWYJupTs7C_-iTHN2ThiynUQAd9jIvxyYT3t1loeEvu-URZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2ab366dbb.mp4?token=dufVRJIeeUVYXoFHAJPYdcIA5MYWIePZRK3daRLAZQOYzbrKQusDyJY24BA4Z0jkgWLEMhH_Ogjz02y9hzvgYHpyR9pnx9RK1UigTUu9wJtMWq1YO_OaipPJAsSpD-w1DuqphXIlu47Sodj8osUZgPuMUE-NpZs7deex0pPAjkuKzD0pO81yr8hbwLGajn36i9y4zYLW2HoXQIxmBeUssly96lldfy7qTN3r52FuulZHA7YOn39p35xXWV9r2EC_u80QRqpBernrqIMNbJkQTkpdVfXuxp0S-srX-zmWYJupTs7C_-iTHN2ThiynUQAd9jIvxyYT3t1loeEvu-URZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  وزیر پیشنهادی دفاع: تقویت پدافند هوایی را با جدیت دنبال می‌کنیم
🔹
مهرداد اخلاقی در نشست ویژه مجلس: اولویت‌هایم برای اداره وزارت دفاع در برنامه پیشنهادی ۱۶ مورد است که یکی از آنها باز معماری و بازآفرینی وزارت دفاع آینده است.
🔹
باید تلاش کنیم که از داشته‌ها…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/467938" target="_blank">📅 14:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467937">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28da4e7be1.mp4?token=q1ArhblwEUK2-saPTZANv6iQc1I0xLDeNN8Z47mwL7zFig5g2nInCJa5V1zAphbImZoK5VLfDn2lZ5K1YWf8XaZR49UFlUEkV5Fvi3XqxvvI_XuY4UuN1BRT9EAHuve_hjF7X7uqv-gE_s3q0EOV22gRl6Rt8gLvagunfu39UUyYjjY2Y3OcsbpCRxcrBwjROaPBagQojB0yH83ycIXVLeCQBQIDGtoOobUusChBGTEfe4-tULWdUitHaRy0Qd8Uw8adM3x6NjJNwM9w2COMihqolds-L5syuWriMrf1kcwuxJXxlo5O3X3lCknJ8AK0MqWjGtE273N40B7Amjxl8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28da4e7be1.mp4?token=q1ArhblwEUK2-saPTZANv6iQc1I0xLDeNN8Z47mwL7zFig5g2nInCJa5V1zAphbImZoK5VLfDn2lZ5K1YWf8XaZR49UFlUEkV5Fvi3XqxvvI_XuY4UuN1BRT9EAHuve_hjF7X7uqv-gE_s3q0EOV22gRl6Rt8gLvagunfu39UUyYjjY2Y3OcsbpCRxcrBwjROaPBagQojB0yH83ycIXVLeCQBQIDGtoOobUusChBGTEfe4-tULWdUitHaRy0Qd8Uw8adM3x6NjJNwM9w2COMihqolds-L5syuWriMrf1kcwuxJXxlo5O3X3lCknJ8AK0MqWjGtE273N40B7Amjxl8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر پیشین ایران در بیروت: حادثهٔ منجر به شهادت شهید رئیسی و شهید امیرعبداللهیان مشکوک بود
🔹
اسرائیل از فروردین ۱۴۰۳ شروع به گسترش جنگ کرد و به‌سراغ مهره‌های کلیدی رفت که شهادت شهید امیرعبداللهیان و شهید رئیسی هم همان زمان اتفاق افتاد.
🔹
شهید نصرالله دربارهٔ…</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/467937" target="_blank">📅 14:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467936">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نامۀ معرفی وزیر پیشنهادی دفاع اعلام وصول شد
🔹
نیکزاد: نامۀ رئیس‌جمهور برای معرفی مهرداد اخلاقی به‌عنوان وزیر پیشنهادی دفاع اعلام وصول شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/467936" target="_blank">📅 14:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467935">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سردار شکارچی خطاب به مسئولان آمریکایی: شکست را نمی‌توان با تبلیغات و جنگ روانی پنهان کرد
🔹
سخنگوی ارشد نیروهای مسلح: آمریکا برای رهایی از باتلاق خودساخته در غرب آسیا  که هر روز بیشتر در آن فرو می‌رود، به قاچاق سوخت متوسل شده، اما پرسش اساسی این است: آیا راهزنی…</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/467935" target="_blank">📅 14:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467934">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e597313e96.mp4?token=L5Ga_rujR25IlLBcGbo8MyzdToFL9YzXQ4bhvq7n8hMD26cCKje797SDHf3ITr2wbFNoJG_7sCt7n2JGllNiYXiPQfhTbdhYK572yBNx0l6DW3lITm0WunYghEVyv0fLx_LBlhicNKBtpfQFbg6OawosNyXTCl7r9Ufp_69nziOyHFs8nQ3vCW8bNEFrPwUju5JsO7CJ4ZmnUJzkXiR-Yv1rWDC-pZaXRphBFgvD2WX6p4Oyf7Afi-QI6giLYvHDpSbrGlEyuLNWRV_tjK5gkJbmn2e5hVVdM0PbHPhO__PpHfOWX-kfVdLowSdscyyutVkPyGHGGjhbnfHoxcPgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e597313e96.mp4?token=L5Ga_rujR25IlLBcGbo8MyzdToFL9YzXQ4bhvq7n8hMD26cCKje797SDHf3ITr2wbFNoJG_7sCt7n2JGllNiYXiPQfhTbdhYK572yBNx0l6DW3lITm0WunYghEVyv0fLx_LBlhicNKBtpfQFbg6OawosNyXTCl7r9Ufp_69nziOyHFs8nQ3vCW8bNEFrPwUju5JsO7CJ4ZmnUJzkXiR-Yv1rWDC-pZaXRphBFgvD2WX6p4Oyf7Afi-QI6giLYvHDpSbrGlEyuLNWRV_tjK5gkJbmn2e5hVVdM0PbHPhO__PpHfOWX-kfVdLowSdscyyutVkPyGHGGjhbnfHoxcPgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: شهید نصرالله هیچ درخواستی برای دخالت ایران در جنگ نداشت.  @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/467934" target="_blank">📅 14:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467933">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سردار شکارچی خطاب به مسئولان آمریکایی: شکست را نمی‌توان با تبلیغات و جنگ روانی پنهان کرد
🔹
سخنگوی ارشد نیروهای مسلح: آمریکا برای رهایی از باتلاق خودساخته در غرب آسیا  که هر روز بیشتر در آن فرو می‌رود، به قاچاق سوخت متوسل شده، اما پرسش اساسی این است: آیا راهزنی دریایی، دزدی و قاچاق سوخت می‌تواند مانع شکست قطعی آمریکا شود؟ هرگز!
🔹
جنگ تبلیغاتی و دروغ‌های پی‌درپی مقامات آمریکا درباره تسلط بر تنگه هرمز واقعیت‌های میدان را تغییر نخواهد داد.
🔹
نه عملیات روانی و نه ادعاهای رسانه‌ای قادر نخواهند بود واشنگتن را از پیامدهای راهبردهای شکست‌خورده‌اش برهانند.
🔹
شکست را نمی‌توان با تبلیغات و جنگ روانی پنهان کرد و واقعیت‌های میدان را نمی‌توان با هیاهو تغییر داد.
🔹
توهین‌های اخیر مقامات متوهم و نابخرد آمریکا در مورد تمدن، تاریخ و ملت ایران، نه تنها بازتابی از استیصال آن ها است، بلکه تنها بر عزم راسخ مردم قهرمان ایران می‌افزاید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/467933" target="_blank">📅 14:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467932">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ff8d97839.mp4?token=bFM_0GuSX3cnNKC8_nDH8p5bwt3k9RHy6J8vi2Ic0rP0zBzAxDKHbfmIUZiZyr-nuOSP5rXe3AEyWXTdSHOu_Pw0AiCVW73ulz94d_jDFdATnUYScYUTnHJbzI2oGO5mORA0uKIVuwrXD7B_y9jWdtiW0EaaK4UCzJEEoJQCUpChzGeI-19ahmN9iFOgLW9bREsFHzzvPkRH8F5irj-3UOKZblcywUuBJIa6O-zllx9rE1PsTwpemz2_VCuRnoyMmhNs-fKaLio6_xYTs4rkjMNCpyWsbhfLJ1JPIgXPu-cqQKkRHmiJy076MsbLkYBd6R2OINoKkXGwSnMgSm2tVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ff8d97839.mp4?token=bFM_0GuSX3cnNKC8_nDH8p5bwt3k9RHy6J8vi2Ic0rP0zBzAxDKHbfmIUZiZyr-nuOSP5rXe3AEyWXTdSHOu_Pw0AiCVW73ulz94d_jDFdATnUYScYUTnHJbzI2oGO5mORA0uKIVuwrXD7B_y9jWdtiW0EaaK4UCzJEEoJQCUpChzGeI-19ahmN9iFOgLW9bREsFHzzvPkRH8F5irj-3UOKZblcywUuBJIa6O-zllx9rE1PsTwpemz2_VCuRnoyMmhNs-fKaLio6_xYTs4rkjMNCpyWsbhfLJ1JPIgXPu-cqQKkRHmiJy076MsbLkYBd6R2OINoKkXGwSnMgSm2tVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: تصمیم شهید نصرالله از ابتدا این بود که حزب‌الله یک جبههٔ پشتیبانی باز کند؛ نه جبههٔ جنگ
🔹
سیاست شهید نصرالله این بود که از مظلوم‌نمایی اسرائیل جلوگیری کند و در بالابردن تلفات احتیاط داشت؛ درحالی‌که نتانیاهو به‌شدت تقلا می‌کرد تا جنگ گسترده ایجاد شود…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/467932" target="_blank">📅 14:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467931">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJjUTR7ZPLULlgZWYDusnsFQod5KOS08AfuQcV-t3IAWc3ZGAD4jETd8L3J_BsodAyOWaqV3wdvH6O74N1hgTZLfuNKV0JXAfRt8hDTK9-YyBLvO3HpUsbJflV4IaBFbORurSvWELKS8bWDOz3l-nh7JHVO0weoy9skSluJef967eQOAegVcii61_gKUIP5AnQn-BBHtlpsR569qp7sVAV3QoeHkuqiZBKcB5XE3QFZbnrBtLwT3ij5naLBcGk2oOKO4JuHRvhKF4jpW4SGFBOWAHQp1utXHzzIiL8-XViU43SCkxFPbpou4rCpVaeT1YG1QNrNnlTG2_ozzTT3gYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع خطاب به آمریکا: با آتش بازی نکنید، دست نیروهای مسلح پر است
🔹
سردار ابن‌الرضا: کسانی که امروز با ادبیات کینه توزانه و سرشار از عقده درباره ایران و هویت تمدنی ملت ما سخن می‌گویند، یا تاریخ را نمی‌شناسند یا با فهم غلط و ناقص از مفاهیم راهبردی عملا با آتش بازی می کنند.
🔹
ایران نه هویت خود را از کسی وام گرفته است، نه برای حفظ آن به اجازه کسی نیاز دارد و نه تهدید و تحقیر را جایگزین حق ملتش برای تعیین سرنوشت خود خواهد کرد.
🔹
اگر تصور می‌کنند می‌توانند با تهاجم تمدنی، ملت ایران را به عقب‌نشینی وادار کنند، تاریخ ایران و اراده این ملت را به‌درستی نشناخته‌اند.البته همه اینها ناشی از استیصال و شکست آنهاست.
🔹
ما نه با تحقیر و نه با تحریک دیگران به دنبال اثبات تمدن خود هستیم و نه اجازه می‌دهیم دیگران با ادبیات برتری جویانه با ما حرف یزنند. موضع ما روشن است: احترام متقابل، استقلال ملت‌ها و پرهیز از تهدید و تحمیل اراده و برخورد قاطع با متجاوز.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/467931" target="_blank">📅 14:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f27fc550.mp4?token=pkIr9NwIrH34ZwjtCzqiTMj8QJWiVKfExYP6xf8nBLKy_d982I9NU4ddh2VyQpNENYWizvyGh_IPrbsovMt3TCWgL3GsH7LuV5--4TnPU6z7gj6y4Fq4SQhqqZcwREZW9Aifeoa4XcHWqFNLN204rMLEbdk_nJ0nPDsRpeyB_Pj-doXISTC01PxsL1WGQhP48AecgTrGcB2em_k9HlZB9rM0ILbLZ6Z9ElLiFvEiPpIffcZR6NRbw_s-9MQX-hJnFUxa95SacU1_bobW1n-N7OL71a9Fw1KcZNZ1OmFN98DWi0cr3wZexJZsHRjMbmgYPp4DQrikoGVlx_VnlXeUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f27fc550.mp4?token=pkIr9NwIrH34ZwjtCzqiTMj8QJWiVKfExYP6xf8nBLKy_d982I9NU4ddh2VyQpNENYWizvyGh_IPrbsovMt3TCWgL3GsH7LuV5--4TnPU6z7gj6y4Fq4SQhqqZcwREZW9Aifeoa4XcHWqFNLN204rMLEbdk_nJ0nPDsRpeyB_Pj-doXISTC01PxsL1WGQhP48AecgTrGcB2em_k9HlZB9rM0ILbLZ6Z9ElLiFvEiPpIffcZR6NRbw_s-9MQX-hJnFUxa95SacU1_bobW1n-N7OL71a9Fw1KcZNZ1OmFN98DWi0cr3wZexJZsHRjMbmgYPp4DQrikoGVlx_VnlXeUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: نگاه شهید نصرالله به نابودی اسرائیل، «نابودی تدریجی» بود
🔹
شهید نصرالله به من گفت که «ما بر اسرائیل با امتیاز پیروز می‌شویم؛ نه ضربهٔ فنی. ما نمی‌خواهیم اسرائیل را با لشکرکشی نابود کنیم؛ مقاومت و ایستادگی ما اسرائیل را نابود خواهد کرد». @Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/467930" target="_blank">📅 14:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25bf9ab12b.mp4?token=pLSfnTH_6yFiZqnENi5ghgJuWe28jimwhQuG8ihawTt5S3ev8IxEX6NdwfXQ3hH9XDnltpmcGegGZ9f-fvZuby5mnc4WadTv-OKYXc0fE1dynMdd65lq17YGHb7RKxizPN2-IJgubROE7JH3IiayrD6ejWTwozQu4my0GglAv9Yr-3QlMGlzUT_1KHVCJXxuYQiR2CK1DY26zobWgIaCmaRSoXvY_320Gl3_Kf8dp-QTxUKecavStnU_ODIg3TT3FNTnYYaLrbF_tuiw5nwI6tyieHnHGvEvj4japSriLywjPd8hzvYjyRuV0bSSsHnyNAlbLptTRpSe7fqbS-xYpBWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25bf9ab12b.mp4?token=pLSfnTH_6yFiZqnENi5ghgJuWe28jimwhQuG8ihawTt5S3ev8IxEX6NdwfXQ3hH9XDnltpmcGegGZ9f-fvZuby5mnc4WadTv-OKYXc0fE1dynMdd65lq17YGHb7RKxizPN2-IJgubROE7JH3IiayrD6ejWTwozQu4my0GglAv9Yr-3QlMGlzUT_1KHVCJXxuYQiR2CK1DY26zobWgIaCmaRSoXvY_320Gl3_Kf8dp-QTxUKecavStnU_ODIg3TT3FNTnYYaLrbF_tuiw5nwI6tyieHnHGvEvj4japSriLywjPd8hzvYjyRuV0bSSsHnyNAlbLptTRpSe7fqbS-xYpBWALTxB8BG8MIR_ZPgly_aiGUH1GhS5mIZgHzqwbyDqNGHXZecsRaIXdI0z31pppEUVZ5ZSN_1h4JRgzeqZwqGUZOPUgbzBUD6Gt_Ud5yHdodlX6IAjLclWSmiXD2fwr0Dtq_vb2UxkIuii3v30vn54zqYgZSVInnxNv0yfB9pi8jgjjL_cOK5BAAf5R3AYlO4wkq8kqYlK9neIiSGdUz_bL5o7yex0lqbGfaQcDOyNQI-c4rw1U9Z0EBklOkxELMaog7eWhf_N7WAe1HcgJQKbwQ9xAFXCx4hy-I-dgPTiBSH2GDWn3CAWtpIk7hW328wst5I3amBU8i71JzlfQ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار رتبه‌برتری‌های کنکور سراسری با رئیس‌جمهور
🔹
پزشکیان: برای عزت ایران، باید متحد شویم و در برابر دشمنان، سر خم نکنیم.
🔹
رتبه‌برتر کنکور: ما در خاک ایران رشد کردیم و بزرگ شدیم؛ بی‌معرفتی است که ایران را ترک کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/467929" target="_blank">📅 14:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa97a5647.mp4?token=CU-r8SrsfuS8lXI2zOcjYeIQ-Bo4ANytqC-XdlZZsxcgMDDnLvzg4PfClmrcGVSr6QwkKD6exM7vPD_8FKuDGTb6Gd1Sjnpy2w8FFZLMifDtOofIl5zs7f3lrbeEPEr8kjhuMBOKs3pqVogwF_jDwSZdkELdl7CBrc2qiAm9zcWdbootpiPCY6413lkUdwpdNu9gikyu-dca4qJSXQGdmsp2P-O-vCsnbybDtTzdk3r25HLF_GK17wkO_0Jt4atdlYHsK7QFdlGzNTiEagxJJWqJSBp5MisAd0Wglzjy0zw4PA4-OftJSilTU9CuPVBSMTP0bhVoxDD1MSegGWyO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa97a5647.mp4?token=CU-r8SrsfuS8lXI2zOcjYeIQ-Bo4ANytqC-XdlZZsxcgMDDnLvzg4PfClmrcGVSr6QwkKD6exM7vPD_8FKuDGTb6Gd1Sjnpy2w8FFZLMifDtOofIl5zs7f3lrbeEPEr8kjhuMBOKs3pqVogwF_jDwSZdkELdl7CBrc2qiAm9zcWdbootpiPCY6413lkUdwpdNu9gikyu-dca4qJSXQGdmsp2P-O-vCsnbybDtTzdk3r25HLF_GK17wkO_0Jt4atdlYHsK7QFdlGzNTiEagxJJWqJSBp5MisAd0Wglzjy0zw4PA4-OftJSilTU9CuPVBSMTP0bhVoxDD1MSegGWyO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امانی: شهید نصرالله به‌دلیل نگاه منطقی‌اش هیچ دلخوری‌ای دربارهٔ بی‌اطلاعی از عملیات طوفان‌الاقصی نداشت
🔹
شهید زاهدی کمی از بی‌خبری دربارهٔ زمان انجام عملیات نگران و دلخور بود اما شهید ایزدی حس می‌کرد فرزندانش این پیروزی را به‌دست آورده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/467928" target="_blank">📅 14:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9b003b67.mp4?token=YTfNaCmv8F1t0UswsbTPuq6Lwe2iN9mlyr1sqoP-zbi3-J-l2nsuvpkDLbFVJAqSadlA1jqQvzqO9nsk3cb5fAFAHVzGtZjdMSRk8__lTjE-EDgL5ATyKoujBkJSf1nI7l2eCN9j2nVj4WUkwgeDUhpibJK9foBCSZmlK9eYxQKBQT0GUQEYBT8kBqKWzhFxLauVWOsmoT-QaptQ26gUupN8GjtoODiX_3kAMxnEcm1OPrm8doexBCWOggZdGFk2WksN-aQJXcZ_cEuphccCmJ7QnXR4AT39mRDBOewpcG5NsDN0aLyz_iLggn9fuABXIOdexQsMQRfkAMHXVJwzag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9b003b67.mp4?token=YTfNaCmv8F1t0UswsbTPuq6Lwe2iN9mlyr1sqoP-zbi3-J-l2nsuvpkDLbFVJAqSadlA1jqQvzqO9nsk3cb5fAFAHVzGtZjdMSRk8__lTjE-EDgL5ATyKoujBkJSf1nI7l2eCN9j2nVj4WUkwgeDUhpibJK9foBCSZmlK9eYxQKBQT0GUQEYBT8kBqKWzhFxLauVWOsmoT-QaptQ26gUupN8GjtoODiX_3kAMxnEcm1OPrm8doexBCWOggZdGFk2WksN-aQJXcZ_cEuphccCmJ7QnXR4AT39mRDBOewpcG5NsDN0aLyz_iLggn9fuABXIOdexQsMQRfkAMHXVJwzag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر پیشین ایران در بیروت: روز آغاز طوفان‌الاقصی با شهید نصرالله صحبت کردم
🔹
امانی: صبح ۷ اکتبر با شهید نصرالله تماس گرفتم و دربارهٔ برخی ابعاد اتفاقات صحبت کردیم. ۳ روز پس‌از طوفان‌الاقصی در جلسه‌ای با شهید زاهدی، سران حزب‌الله و شهید نصرالله دربارهٔ این…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/467927" target="_blank">📅 14:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467926">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b174703275.mp4?token=Mufdac98-wkxmwTe5w6I0CO254yYAjsy_7UkB-DRJJNTo_Zl1Dq9t8eoebLSEf3ijb_QW1AtGBpTKmKVD8fmpeks_1Ld3FcuAsNYKk_2RO53EKT3GQfvlbUKoermkfJ08xif1MTHSk8zDW0KHghei1jk8G8LD2gsDf5ga4faIiJ07OIyjkKHlNxcOsQhEeJS5ppqMWZWqRA4pa_EXLmzdf0OkN60CKGB1eff6ejPu-ndwrV-7iwYrUF1_ZHY_y5ICAjXLJmEMD8qez4BUex_mNxd-zJXBtBs9tALUUu7IY3FPS-htTqKineFQbXQOuA4ncw409SRAmgEL2x5eH7BFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b174703275.mp4?token=Mufdac98-wkxmwTe5w6I0CO254yYAjsy_7UkB-DRJJNTo_Zl1Dq9t8eoebLSEf3ijb_QW1AtGBpTKmKVD8fmpeks_1Ld3FcuAsNYKk_2RO53EKT3GQfvlbUKoermkfJ08xif1MTHSk8zDW0KHghei1jk8G8LD2gsDf5ga4faIiJ07OIyjkKHlNxcOsQhEeJS5ppqMWZWqRA4pa_EXLmzdf0OkN60CKGB1eff6ejPu-ndwrV-7iwYrUF1_ZHY_y5ICAjXLJmEMD8qez4BUex_mNxd-zJXBtBs9tALUUu7IY3FPS-htTqKineFQbXQOuA4ncw409SRAmgEL2x5eH7BFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
ماجرای جنگ را از زبان سفیر سابق ایران در بیروت ببینید  هم‌اکنون در پخش زندۀ سایت و تلگرام فارس @Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/467926" target="_blank">📅 14:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467925">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ypgbep3SIXnJLrl_EDr84wuuLodW1Rc1rkPw0tcWhOfRyYxaw-6obMhwETpCBwiEXN0YEG1NTtK_-VIrB2LH6Cwb5okV36Q-6ySab5b2jCJ9gjVGjsDTvYJYgrsXAuIO0yeZi-9saMVjnUStBC_WQY4cUR9s8k-xTQm4pNL7QuYcUESktTLM7rO-NLz6zrAm7uiQ2_zrDJ2iOgGNu4IgYnsr7UwvBlIRzQXz_21EqMNe-D9JxOFGhuKJnRrQr90WD9JRGGXYhySr2f_Jp-Uky0yAZE8o7A2ytsczy-5ZoYRPdvlnyo5MY_Pnt4rn0OWie5nNcnYYjXf-iTVDoCP1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت‌ژورنال: این روزها بن‌سلمان میان کاخ‌های به‌شدت محافظت‌شده‌ای که مجهز به پناهگاه هستند در رفت‌وآمد است و توسط یک تیم امنیتی گلچین‌شده محافظت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/467925" target="_blank">📅 14:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467923">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRabPF9vxZxvOxAGjqzpyZtAdcXd3keqTnLjq6TM3cJf-kqg1OJ4q4t4Lze7dkPPwd3o-LbJ7ZNUdq7z-0_sGd4vvYXqxPCWYRRRjO3OAion120NRw2CMJw_gTS6geiqgX_VwAwRbmMPJpAI9FM6oqyMZpTw40QDohyW2pgUyBKLNGZ9JHYkdSZyg1_1UsxoRPXK5Wmp6kRrfs01TTEF7_E4A9YPGnjiFfFTOULs901yv5AxE6V99q5fzimdlO4r9d9qDs6FIzMoAbSmL2dElMQnLhp5A1XIrbvTs9uPnCHnit1GKwqIOBm7jk3ABm6M6TkjJhZ1DNaeNu4sYMVKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوبل اقتصاد امسال ۲ برنده داشت
🔹
جایزهٔ علوم اقتصادی نوبل به رابرت هال و مایل وودفورد برای «بنیان‌های خرداقتصادی سیاست تثبیت اقتصاد کلان» اهدا شد.
🔹
این ۲ اقتصاددان نشان دادند که چگونه می‌توان با بازسازی مدل‌های اقتصادی، سیاست‌های تثبیت اقتصادی را احیا و تقویت کرد. به‌جای آنکه مدل‌ها را براساس روابط آماری میان متغیرهای اقتصاد کلان، مانند تورم، تولید و مصرف، بنا کرد؛ آن‌ها این مدل‌ها را بر پایه بنیان‌های خرداقتصادی طراحی کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/467923" target="_blank">📅 13:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDmZjwaP2Bvwn31j-g6xJ0AUoAI2YgpQ4eUiK17PeL0NKVJoeXmk9BMijjVals4iLJoYiG-cqQ5I0td2qsfM-yUN5lXR7NIAt4JwXhD6oYtEDLG8ogSsAs5Nzg5ZS4wLtuj3eynlCHr-3vEBRzmCJiNeynThgfxxCznzj0sCXc8iqU8t4Xthn22xYaw3DMbElrWuSu3BU-gQxMkadUXdc5kXuYj8lQlosXA4gwrxxMKgybcSUd6Rpfbm1JRkmZkkkX2IZg3W_XuIe8U2pdQjc3pJPDaak8njBHl-9OSeIJ8R3TVgq-VETdfBO6uOecFMrns4cx85t4_D7L8dgqPcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
ماجرای جنگ را از زبان سفیر سابق ایران در بیروت ببینید
هم‌اکنون در
پخش زندۀ سایت
و
تلگرام فارس
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/467920" target="_blank">📅 13:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4cbe380f.mp4?token=BfdzAJoAahC69pEQcIaoz0k41YIQZJxt4MAP6nQCP70QUEpxC7vpwnxqoy4PLKXDy7Pj5hKPQULTqIv_4GtzCWUj0pi_maoyAujXYpaRRqqnSEqVfotPVxmnOFmV1Fj1WoEdG4jc000onGJySxM2V1grqdnyhjqxpbhXj9beYTCds3E5ZCmAlI8dLfTq_1bharPebOzn4xiQ7tZkUOTAZbYTc_A-b3PNaPeL3hYdUZCUn0Ekex1U_r1jqT_fpUOU4-uMPy73kLNGgZKbM_potRKON6TFjDPwkb05B-awysqleiCrWQ84LRPhysTpGLuyJio-G_PyaEYhPujqJvo-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4cbe380f.mp4?token=BfdzAJoAahC69pEQcIaoz0k41YIQZJxt4MAP6nQCP70QUEpxC7vpwnxqoy4PLKXDy7Pj5hKPQULTqIv_4GtzCWUj0pi_maoyAujXYpaRRqqnSEqVfotPVxmnOFmV1Fj1WoEdG4jc000onGJySxM2V1grqdnyhjqxpbhXj9beYTCds3E5ZCmAlI8dLfTq_1bharPebOzn4xiQ7tZkUOTAZbYTc_A-b3PNaPeL3hYdUZCUn0Ekex1U_r1jqT_fpUOU4-uMPy73kLNGgZKbM_potRKON6TFjDPwkb05B-awysqleiCrWQ84LRPhysTpGLuyJio-G_PyaEYhPujqJvo-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات پهپادی به مواضع تروریست‌های تجزیه‌طلب در کردستان عراق
🔹
منابع عربی از انفجار و حملهٔ پهپادی به مواضع تروریست‌های تجزیه‌طلب در منطقه «کوی‌سنجق» واقع در استان اربیل عراق در خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467916" target="_blank">📅 12:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiabfjwfZREb_dn5wId_DYmxPhhU0cYCAKl14Fq_sUTE2v2BR3wv3gNgXFBW1-6s_V1jOACxAk0q-NFL-Tgy9bvFtYn7adVFc4oiJFyYneEdN2oHfHiG3mmI0pc1FBDiG_pnGTNTxhViwITkBdaYKnTi_DK-tKmtyRFDeRtBxzxK4FhGcDa0mki6IIis52coztytKN8b9UyYUjyU4ATAldhZlVDLagzIhR_aVpuiSqcLY0b8tjS6oQ45AhFj2AwdU_AlhqEkWKSyedjgtrw2q3gASdvkO-eHFTI1JyZp3prQh843LRE5WNakeMn3qeAMjfEP4l9xOYpWANQ7YNSKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردشکنی تازهٔ بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۱ هزار واحدی به ۸ میلیون و ۳۳۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/467915" target="_blank">📅 12:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467913">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42c15d12.mp4?token=hQMYwO_eZgHN2qs-x7qSzKL8GKo5X9jG65oyym3n53ttGknc768VmAX-xaaqx6YyPCmISJ-sfcRqVNEKwELLlIJnfNLTrf2Z3uuphwzUe3cLO9QIqJl5I6NL9HQEpsHWC-kDXfvnDnQfrRBOdyVKkp02IhrU5JrqJd-pKFT1G3a4_W6_np17MojhjDa5YpRZcGtIEVSqw1GuJzmmHgU92uczKyxDQ2s8EzVWWGUJuXShcLpYj1yrVKMe1KrVocKyP0jdCG3zXgJIBh-x42Qxq5cwGRkpWIP2usHNAkV1wRRTlPUXU1FNRnjdyAya2lW74Sx4IaB4ZCfhXsWpv79VuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42c15d12.mp4?token=hQMYwO_eZgHN2qs-x7qSzKL8GKo5X9jG65oyym3n53ttGknc768VmAX-xaaqx6YyPCmISJ-sfcRqVNEKwELLlIJnfNLTrf2Z3uuphwzUe3cLO9QIqJl5I6NL9HQEpsHWC-kDXfvnDnQfrRBOdyVKkp02IhrU5JrqJd-pKFT1G3a4_W6_np17MojhjDa5YpRZcGtIEVSqw1GuJzmmHgU92uczKyxDQ2s8EzVWWGUJuXShcLpYj1yrVKMe1KrVocKyP0jdCG3zXgJIBh-x42Qxq5cwGRkpWIP2usHNAkV1wRRTlPUXU1FNRnjdyAya2lW74Sx4IaB4ZCfhXsWpv79VuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدیمی‌ترین بازار سرپوشیدهٔ پاریس در آتش سوخت
🔹
قدیمی‌ترین بازار سرپوشیدهٔ مواد غذایی پاریس که قدمتی بیش از ۴۰۰ سال داشت، در آتش‌سوزی بامداد امروز به‌طور کامل تخریب شد.
🔸
بازار سرپوشیدهٔ «مارشه کوورت دزانفان روژ» در محلهٔ «لو ماره» پاریس از سال ۱۶۱۵ فعالیت داشت و نامش از لباس‌های قرمزرنگی گرفته شده بود که یتیمان در بیمارستانی در نزدیکی آن تا سال ۱۷۷۲ بر تن می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/467913" target="_blank">📅 12:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467912">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb615441f6.mp4?token=LUu6OWug57rGMArblpFnTotqEDJeaQ5HG8K43Lp2pmHe61-uel19EYMgEsAn-m0QDxV1YIoeTWjdow0VvuKiY6IwFIjtXUBLanjlnoYxwT6U9UgG7OBtWDPGRmjT9NwnwotbDP-XrMWVzuamkyi_TnwWwxlPyqCWn1K-7KU6uzv20Sc__pdyWBhzkltjeO-1_A4hoWyaFPZt_2g7tr3-dBOXrOQ9qAIxajgL6Kqj3HKsvNraeMbTAcyYxUTYCXl_BZza-WUkriFvSMOIAq3JZm3AXFWnADt3QUS_fJ7vTR8MYgHAdcUwCHhcl36l_xDjkBbL9_QqObveAlpHwLccBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb615441f6.mp4?token=LUu6OWug57rGMArblpFnTotqEDJeaQ5HG8K43Lp2pmHe61-uel19EYMgEsAn-m0QDxV1YIoeTWjdow0VvuKiY6IwFIjtXUBLanjlnoYxwT6U9UgG7OBtWDPGRmjT9NwnwotbDP-XrMWVzuamkyi_TnwWwxlPyqCWn1K-7KU6uzv20Sc__pdyWBhzkltjeO-1_A4hoWyaFPZt_2g7tr3-dBOXrOQ9qAIxajgL6Kqj3HKsvNraeMbTAcyYxUTYCXl_BZza-WUkriFvSMOIAq3JZm3AXFWnADt3QUS_fJ7vTR8MYgHAdcUwCHhcl36l_xDjkBbL9_QqObveAlpHwLccBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ فرانسه سفیر ایران را احضار کرد
🔹
وزارت خارجۀ فرانسه اعلام کرد سفیر ایران را دربارۀ آنچه «کارزار انتشار اطلاعات گمراه‌کننده» دربارۀ اعتراضات دانش‌آموزان خوانده، احضار کرده است.
🔸
در جریان اعتراضات دانش‌آموزی فرانسه که در اعتراض به کمبود معلم، کلاس‌های شلوغ…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/467912" target="_blank">📅 12:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467911">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عنصر عملیاتی جیش‌الظلم به دار مجازات آویخته شد
🔹
عمر درستاران فرزند عبدالقادر، از عناصر گروهک تروریستی جیش‌الظلم به دار مجازات آویخته شد. درستاران یکی از عناصر مسلح گروهک تروریستی جیش‌الظلم بود که کار پشتیبانی از تیم‌های عملیاتی گروهک را انجام می‌داد.
🔹
حملهٔ تروریستی به مقر انتظامی شهرستان راسک، حمله به مقر سپاه شهرستان راسک، حمله به پایگاه پارود، حملات تروریستی به مقرهای نظامی در فروردین سال ۱۴۰۳ در شهرستان چابهار از طریق پشتیبانی عمر درستاران انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/467911" target="_blank">📅 12:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467910">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71d2aa1b6.mp4?token=buU6heSO9qvVLS5v1lmWv2tVBBCxfrkA_TmSbHnbdGkdh03QovA8TwXUwHQyTTVErfLmLEwEOZj2e0A7UFbXYHrOqorp6bv9JJCcJdT7uVOX-fuA8aiNq1D-34eVx1HIkcmBmb0vs-dbpfW124s1MWVVly5RIY7YHGp6yfj3ZRNdwYuyXZyESh7gtawzUfwirf5zrAyaZTQ8st3CjdpB75OIr_ShYUwq12mtSkY82JrehyeAlI6VIViffJRw_WrgypC4h7Azvr3TjPxjayuvGDJqUBSa3obf-NcMTcl9n6TuwsCV43zzfshklZRnFAchWnWUJMeldVdRouZXykqGYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71d2aa1b6.mp4?token=buU6heSO9qvVLS5v1lmWv2tVBBCxfrkA_TmSbHnbdGkdh03QovA8TwXUwHQyTTVErfLmLEwEOZj2e0A7UFbXYHrOqorp6bv9JJCcJdT7uVOX-fuA8aiNq1D-34eVx1HIkcmBmb0vs-dbpfW124s1MWVVly5RIY7YHGp6yfj3ZRNdwYuyXZyESh7gtawzUfwirf5zrAyaZTQ8st3CjdpB75OIr_ShYUwq12mtSkY82JrehyeAlI6VIViffJRw_WrgypC4h7Azvr3TjPxjayuvGDJqUBSa3obf-NcMTcl9n6TuwsCV43zzfshklZRnFAchWnWUJMeldVdRouZXykqGYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ انهدام یک تیم تروریستی در سیستان‌وبلوچستان
🔹
سخنگوی فراجا: در پی فعالیت های جنایتکارانه و تروریستی مزدوران وطن‌فروش در چند روز گذشته در نقاط مختلف سیستان‌وبلوچستان که از جملهٔ آن شهادت ناجوانمردانه و مظلومانهٔ شهید افتخاری و جراحت ۲ نفر دیگر از همکاران…</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/467910" target="_blank">📅 12:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467909">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLQiLlWKXW3JFFiaZfybkMx5ojrY_FmBmfLv5FL6-RqtNH6tzp7dll6SeXbwUQv4Anzr1RLUgO0O7DM0O11Uhsp3AtLf5iPiGaho5EvOfYZOu1p7WgE7FabmeoHZBKt9CBUrTOev86t0Em_BFpnM0KdFKlROw0QxyX-cQpSi44yuDQcJHm7n7qDQhS7ONYYiym_AKw6GKau5lGjsmfPx4RS8U0Q-ox628DuR4VTNZPytmXje3TL_y_-P3zagL6JFB7lP-BwXiMX-KnGUb19o4V2IP3EJvXIljQDcvwIC-eKzO8nimUm0tcrrqNoivXA7cvz2d4NyunfTTsrfL5Yb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماس متعدد پزشکیان و علی‌اف؛ منطق ارتباط با متحد اسرائیل چیست؟
🔹
بررسی تماس‌ها و دیدارهای رئیس‌جمهور ایران با رئیس‌جمهور آذربایجان در بازه زمانی جنگ ۱۲ روزه تاکنون، نشان می‌دهد که این ارتباط، متعدد و همراه با رویکرد دوستی بوده است. هم‌زمان، منابع خارجی از جمله موسسه مطالعات امنیت ملی اسرائیل، از همراهی نظامی و اطلاعاتی باکو با تل‌آویو در جنگ علیه تهران گزارش می‌دهند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/467909" target="_blank">📅 12:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467908">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-nPCRHmop618XPVfTKgvraKMAzguX0P_9a6nMLX7KmQ_0ZrMZwz_ljpD20MsErFcuWiEVFEqW6x4Jgh9HUmCsN-pqG8EbqcZl0iMkbd4dN7QQ0rLVBVuZ2mvIb4jid2L9TBeGepxmpGcTt198oaPVR0JxyDAReNa8Q_qLzXSEjKH5ij54N7MNlnXDLBfYi_cXlgjR-ZniBeVXPoXzvky-CnetKgEKqtSz9yNCESg4NZqDBxtbZZzp97pFSpCYjrLYr6JyO2XD1xhMrs7lhbROlLXRW2GgbZSxuALM72wz-y_RMTS5t8Yqv3ht7AHXy4ZhFM2rHbelwN847AOTs_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موسسه آدم و حوا هیچ‌گونه فعالیتی در زمینه چند همسری، ازدواج موقت و کاربر زیر سن قانونی ندارد
اطلاعیه موسسه آدم و حوا:
🔹
متأسفانه افراد سودجو با ایجاد کانال‌های جعلی در تلگرام و سایر بسترها، استفاده غیرمجاز از نام و نشان تجاری آدم و حوا و حتی بازنشر محتوای رسمی مجموعه، خود را به‌عنوان نمایندگان این پلتفرم معرفی می‌کنند.
🔹
برخی از این افراد با وعده معرفی همسر یا ارائه خدمات صیغه‌یابی، از مخاطبان درخواست وجه کرده و پس از دریافت پول، ارتباط خود را با آنان قطع می‌کنند.
🔹
پلتفرم آدم و حوا صرفاً در زمینه تسهیل ازدواج دائم و تک‌همسری فعالیت می‌کند و هیچ‌گونه خدمت یا فعالیتی در حوزه صیغه‌یابی و ازدواج موقت ندارد.
🔹
فعالیت آدم و حوا بر مبنای تسهیل ازدواج آگاهانه، مسئولانه و پایدار شکل گرفته است و تمام کاربران این سامانه دارای سن قانونی هستند. فرم‌های زیر ۱۸ سال در پلتفرم آدم و حوا ساخته شده توسط والدین و متعلق به آن‌هاست و هیچ فرد زیر سن قانونی اجازه ساختن فرم یا گفت‌وگو با سایر کاربران را ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/467908" target="_blank">📅 12:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467907">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nfd1A2gR5ePSRd4nZYnHSmAw1m_DhK5weDFKAXffYkFUBX3D3KwoloFitYpjLzR7BPeCYYO4vwdrWOUrVZtlLt6H9lk-siG6xGLkuzcwVMJ3ET2bVm9V_DaUct8B85kQ8rLHLwC--uXASCCqw0UObe_r1aPaY6H9FqnVbVEO4sETqVEOzk3LRfFM7WeteTkJU3T3nx5emUElN4fafE42FG_qJ4NCQfF-JDucm6ibQ68zA9KTAw-L-zGS5uu2iDzsyR7aCli1ODqThkJ86tv-v0azkgU6aHSjtw4h0raXPj3EAyrZFQkXaVY6XUVJLc7SLfNMeVuxA5lNlmv1E9ogfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر پروژه بزرگ، از یک انتخاب درست آغاز می‌شود.
آقای استیل، واردکننده و تأمین‌کننده ورق و کویل استنلس استیل، گریدهای مختلف مورد استفاده در صنایع را از برندهای معتبر بین‌المللی تأمین می‌کند و با رصد مستمر بازار، اطلاعات دقیق برای انتخاب محصول را ارائه می‌دهد.
ــــــــــــــــــــــــــــ
راه‌های ارتباطی
☎️
021-37216
☎️
021-22121204
📱
0912-9686424
وب‌سایت
🌐
AghayeSteel.com
ایمیل
✉️
info@AghayeSteel.com</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/467907" target="_blank">📅 12:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467906">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/467906" target="_blank">📅 11:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467905">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61253719e0.mp4?token=e7gAwNO4IEjN3ilfEIldipoX61GJfEVA8N655Bw3yb6n1QPflHnLk0rCPVW0wlAnoe27-KRARz9heBf5oSwO8LzUdC0eWr3qrVRe5BFpDWllSwlfkUVIiLWN442-U-UjRh6j5wPl5dlR715uUmEEZtGHRbz_4jE_0QBbKSDaGyQo0w4Lwyw2JaqdncTlCLykWtob7Fuw9XNuANoQ8ggmEGQX9UHS4gnaBPACaV6kr2nGAGJgd7G3BhABy8qULA8Fn76ebQn1uUW4NzWd3yU9EsnTQ97gFGZpLVl5wP1qFLoFnrh0ZFJoRJ80HFpIstLPJM9ej22_0ip9EKFmFurOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61253719e0.mp4?token=e7gAwNO4IEjN3ilfEIldipoX61GJfEVA8N655Bw3yb6n1QPflHnLk0rCPVW0wlAnoe27-KRARz9heBf5oSwO8LzUdC0eWr3qrVRe5BFpDWllSwlfkUVIiLWN442-U-UjRh6j5wPl5dlR715uUmEEZtGHRbz_4jE_0QBbKSDaGyQo0w4Lwyw2JaqdncTlCLykWtob7Fuw9XNuANoQ8ggmEGQX9UHS4gnaBPACaV6kr2nGAGJgd7G3BhABy8qULA8Fn76ebQn1uUW4NzWd3yU9EsnTQ97gFGZpLVl5wP1qFLoFnrh0ZFJoRJ80HFpIstLPJM9ej22_0ip9EKFmFurOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: فکر می‌کنم وقت آن رسیده که اوکراین یک رئیس‌جمهور جدید داشته باشد
🔹
پیشنهاد می‌کنم که آن‌ها یک رهبر جدید روی کار بیاورند که بتواند توافق کند. زلنسکی می‌توانست توافق‌های زیادی انجام دهد، اما به دلایلی هرگز این کار را نمی‌کند. @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/467905" target="_blank">📅 11:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d65baf23a.mp4?token=g7LrXMMeqdWY_UAa0sTxhuAB1pEEIyRsWOuncBC8VUZ9QIUJE2s6HPeIXWTajS1GVvDiVnN8fMRnelUJ940QWo3_4TzmIv5DWT2TqoOLB6PBCKd6EmAWhp-Zmq6gOrPyqxZgKg_kwRyhWywlqUyFQcc-_OHGtHyg-ZyWZevfL9eA_x2PCs6Q3EsvsFhV5gYlrVGNWXRtDecIpG4l66h7t2hmZlzXrAHY_3Hl0TeQ7pO6RANrMaGvCImGarU3w1qzcLQ3uNL6Rng_5_B37XpJhnFgXKNVfBBoC8WnbZ06gRaslnGRIJQt7fZWKNgJhCPwGn9-S7ygSJZ7rbSl64byEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d65baf23a.mp4?token=g7LrXMMeqdWY_UAa0sTxhuAB1pEEIyRsWOuncBC8VUZ9QIUJE2s6HPeIXWTajS1GVvDiVnN8fMRnelUJ940QWo3_4TzmIv5DWT2TqoOLB6PBCKd6EmAWhp-Zmq6gOrPyqxZgKg_kwRyhWywlqUyFQcc-_OHGtHyg-ZyWZevfL9eA_x2PCs6Q3EsvsFhV5gYlrVGNWXRtDecIpG4l66h7t2hmZlzXrAHY_3Hl0TeQ7pO6RANrMaGvCImGarU3w1qzcLQ3uNL6Rng_5_B37XpJhnFgXKNVfBBoC8WnbZ06gRaslnGRIJQt7fZWKNgJhCPwGn9-S7ygSJZ7rbSl64byEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی دربارهٔ حواشی ایجادشده پس‌از حضورش در یک نمایش صحنه‌ای: حاضرجوابی‌های من برای دشمن است؛ نه هم‌میهنانم.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467904" target="_blank">📅 11:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2a06561df.mp4?token=vwWjRVnvYPCBZl9ZXKc0cK7t8qkSOh8BzzaCREcHjZ5PGFv3KkeRVOtxEX69TiI8FWDfPG4YhIy2v5fukDAuAjCf5m4GG1oZS6i8oLt6-5hnqKTQgXBI0uLLpzo_Hda6tw4jL0sWqDlwo-t4CUFNIptAwQTKaB1xEZYkemgn776NzIs-PwYSOwUwyhZUTjC-uyQHtTzerUC8FocyteOZ04APBMRWnM1ZjW0pf4dVOjpSP03OUJifj5dEJkT36-eDSnDwRt3pVE1FlfLriKlDxgL_vcOGYmLHx9jTjywSVytx9vlgNg-9ja2C20YztWt3pSUCKAXtwrV1Iu-72Hx-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2a06561df.mp4?token=vwWjRVnvYPCBZl9ZXKc0cK7t8qkSOh8BzzaCREcHjZ5PGFv3KkeRVOtxEX69TiI8FWDfPG4YhIy2v5fukDAuAjCf5m4GG1oZS6i8oLt6-5hnqKTQgXBI0uLLpzo_Hda6tw4jL0sWqDlwo-t4CUFNIptAwQTKaB1xEZYkemgn776NzIs-PwYSOwUwyhZUTjC-uyQHtTzerUC8FocyteOZ04APBMRWnM1ZjW0pf4dVOjpSP03OUJifj5dEJkT36-eDSnDwRt3pVE1FlfLriKlDxgL_vcOGYmLHx9jTjywSVytx9vlgNg-9ja2C20YztWt3pSUCKAXtwrV1Iu-72Hx-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنجال واگذاری اراضی چابهار به افغانستان؛ اصل ماجرا چیست؟
🔹
اظهارات اخیر محسن زنگنه، نمایندهٔ مجلس و رئیس کمیسیون ویژه اصل ۴۴، دربارهٔ واگذاری اراضی چابهار به افغانستان، با واژه‌ای همراه شد که موجی از نگرانی و انتقاد را در فضای عمومی ایران برانگیخت.
🔹
او در…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/467903" target="_blank">📅 11:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9937a69255.mp4?token=msDiUlHK71t9qt3ueUDzTQFhMZ_-sPGmfKL0DioVBtHD3Sx_c0nmfD64NKmT0dL4ytj3MuNLady4yY_kkCfXNjmaIBcyOX9JOqIgS5_zhEZxDvr8tPsOu0rh1TmPkNXaeu9vc19GUuooFArOC6SWpJANhlvJrREuMXTT6s-PkTB1SqvYitI1jkOHYvjsScLRZbXG2j_6sOa1Hnn5ztdh1h-HIBFaM0_ALQ8diQ6U0MlpPNHpMpbTgi8BKgxol_70tgIf7UivZfJmTDMxx0Z76jZEfoIFYzENrB7KTXm0i2NcfQmtKLAgrTGz52n_SU8CWT68VlpBQau3Eg68G6H0QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9937a69255.mp4?token=msDiUlHK71t9qt3ueUDzTQFhMZ_-sPGmfKL0DioVBtHD3Sx_c0nmfD64NKmT0dL4ytj3MuNLady4yY_kkCfXNjmaIBcyOX9JOqIgS5_zhEZxDvr8tPsOu0rh1TmPkNXaeu9vc19GUuooFArOC6SWpJANhlvJrREuMXTT6s-PkTB1SqvYitI1jkOHYvjsScLRZbXG2j_6sOa1Hnn5ztdh1h-HIBFaM0_ALQ8diQ6U0MlpPNHpMpbTgi8BKgxol_70tgIf7UivZfJmTDMxx0Z76jZEfoIFYzENrB7KTXm0i2NcfQmtKLAgrTGz52n_SU8CWT68VlpBQau3Eg68G6H0QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/467902" target="_blank">📅 11:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467901">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d7a1e181e.mp4?token=q4L5aHW16flVLI3W1RRxohY19M3plalcvap2ZEHWaW4x7ZarRWqdibVfF0EH1Cq86y-5WN78DLpDZWq1BS-iHNb-pBexiX2MZvepvR_GG5vNK19Dg5tvYGzMFbwlyFqelYOyp3KNsk_6RvcolOwc4u55b5Uv5AKXLloUPVsXfX1HtlQBOjzSSDDB4Nr-VkDne2kCQxlTAKAuzeZz0nsLOmAFUw87h3RLfg7vNSANlksXM474SwlhtjM_VChq8UQVtk423Vt1GYwfAJqLfzJAbglbVXcBZxnGGEmJAeTQTBs_4_lc57Vq1A9asgZ3IDq2DXvDALAsIGTxHC_BmO8AAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d7a1e181e.mp4?token=q4L5aHW16flVLI3W1RRxohY19M3plalcvap2ZEHWaW4x7ZarRWqdibVfF0EH1Cq86y-5WN78DLpDZWq1BS-iHNb-pBexiX2MZvepvR_GG5vNK19Dg5tvYGzMFbwlyFqelYOyp3KNsk_6RvcolOwc4u55b5Uv5AKXLloUPVsXfX1HtlQBOjzSSDDB4Nr-VkDne2kCQxlTAKAuzeZz0nsLOmAFUw87h3RLfg7vNSANlksXM474SwlhtjM_VChq8UQVtk423Vt1GYwfAJqLfzJAbglbVXcBZxnGGEmJAeTQTBs_4_lc57Vq1A9asgZ3IDq2DXvDALAsIGTxHC_BmO8AAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: یک پیام برای روبیو دارم
🔹
سرلشکر رضایی: من پیامی برای وزیر خارجهٔ آمریکا دارم: «مردم بسیار بزرگ‌تر از شما بارها در طول هزاران سال آرزوی آمدن به ایران و اشغال این کشور را در سر پرورانده‌اند.
🔹
قدرت‌های گوناگونی رویای ورود به ایران،…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/467901" target="_blank">📅 11:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467900">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیکر شهید نصرت افتخاری در گلزار شهدای زاهدان تدفین شد
🔸
درپی اقدام تروریستی در جادهٔ چشمهٔ زیارت زاهدان، دکتر نصرت افتخاری، معاون فرهنگی اجتماعی فرماندهی انتظامی سیستان‌وبلوچستان، به‌شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/467900" target="_blank">📅 11:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBELRfLDi3ZPEGXSkv6fgp8irN2RSMDKVApeQTHExIfDu3u62AidaLb-L_O2TwJTeW1tqJ2Fwedys7UmKz3gJhFGOIEaxPmQSiKrl4FRNKCqOe1ZJMTwvGlEHSIwgcoLaH2t0ei_rzQ5y4EHHy5ILZsr8Q17FUbprisqsS3dfuzOw8edbAnwCQmAmvtO-WDWvNc7ZXwlGctFrTvv-HuTUyifsLT8wukWKTbzaoJNID5JFl5vs-Dp4UF1KcmXqlMMAQ8PCiosFJxVGpAtLMPdajNAqHZRdL8m-amhBYE5Fe_UJ_Yze545iGYvS02sF6Lwv3Ne-2ToNrd8BqLoFRmtag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tKmFhjWAEP_7QlvMhhSOJiMEN8LLzHcCQum8kVaYvnAqGoTkzf5_ixvZjCVC1e_d7QWc6qBpH2GyQtCXn6xxCIGwEmIfdndV0JvjJ-UfgZHdcWhbZPnrUO4TMkFQHndJFEW2gGPxk9yITwSilaGAWhotpRJMXJfuv9dIm-V1RFa2rVazfmcbMMUie_xhJnjKBlrcAMSQb3s5Ni2VHaFBF98eSuslgBeYrxv_j4H6KNDp0Z_xx0mqWyb2xbrhgBTJyT2oO7yok2ifNWU6H4R05eLTr2gnVd7CdEVfyNzfDEEq81Ys22FArdEKkW-9zRJFS1YP2Kvxu48fO91Dv0tXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWcDAv9axa6Pkpu-RjlWFGljDf9Ehx5BmaTBzxHX7ejfOJk9n8qlAOBL-E0P5-Eo4qqiZHqxXKxfirC52gYSsKVxzenVFrk6SAxIjx62LwhtJ5Z5nRN2wgtKcWLk-9TlAZBHxo7jpycdndhzeEZVx6BVqdt_hhLvGeQVYzF2bL7iKdnSZhLK4pknnTL7FGQsKzj_nhXVHfb7GmC74G78J4BEPoX_SY4M0tsejce9HiREujAze-ZGBkbGBd1MxDvK0zHUe-e5jvpjhCLuy8KLccZvaB6N53AHWoOWc7VLfZERGltIfx37rkXR3_PyXe-RlGod8bFTvdf59TSG0edASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0NoDTAsWBjNKfJsQmARhyqrla1_tIw_Hiv8TwIht52oZU5T8BhLd17CS98OkR1uWMPJ1O7hstpeAxEQNj9FyvjbeeZPuS-rRswTIir0e2ggXo0EhlqMLmlztt-pjJqZultCS-udEp6ZirUil9GFP85K_L-6Ug5iqXg-jhXo47WLyU4XgdczY72NwVL9mtSunctdie3DkuHC-aUCIDtEpF8MH-fOo2hpIZWWaxx51EMu38zYTFw2UsLcso0VVfbxj6hD-VgXZGVnRkVonb_zDKDm-CjIVoZTETZ5yBJWyODBkwNm_aCxDF9CVhJv_ZZRP8HOSzI3pVrFbDDmIkDs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXLGB5_liOTTYinlUhrx49QGq9aYaJnUIRCg_IBl2CjnL_-gFjz8PYy5JlSyLSl6SfnN6pBamtQFHLUzdFGlqt7HkrEpbws9eCuLvRfOzNhUBihUUnLDn_HWX6TSoR5XBsKZuUSfbnsPPr746C_WQdzgOtoJ-4i-aUn5NFmc2XCaEHEpUbCL9pvkVb6S155uDxLxW5HxdXMSKNVoUnEPuyIirYD_SWsU6QPmrwQTdd0kcoEqIvHzc7PqYgoxYxtGLR60449PnjfNV3JyrHLcZLdyRuG8c1Hz_pX0FBlKOy9SK8rZIIGGViPZBkx1fk3LycCBe4icVNOueQMvg2Isjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت چای قرمز در روستای علوه خوزستان
عکس:
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/467895" target="_blank">📅 10:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5c327b1f.mp4?token=ndWpnMdUmpXflDttTEJdr3NNRNbbzA_MPP2e_KVXiXnSocmZH19YfKVAHQrFW76LIVAuE4tK-YDfdaBvlfNxk59XWjyar6GIe4F2u4nTeoOkVPnTDYE_Ouj4PGXHP3csEeY9KjU_YtO37WYxLtyw7PxwyIHiSqRVMgUYCWQ2r0l8E7rq4-jdDnZDRgQy7-xP3Q9v79RlkOqBGStwZ0sfaAuLvwRqP-ALSvMBB_cExg5zvG-u_SUChfVgLt1UI9SXrHwvyb5KsiLqRQY2nzUgRuFE5dLRuqmUnR8ZrkEXWpqm-EhM4EXh3Mz1HlFixqsAlRBJaxZh9_AyL_KaI9fKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5c327b1f.mp4?token=ndWpnMdUmpXflDttTEJdr3NNRNbbzA_MPP2e_KVXiXnSocmZH19YfKVAHQrFW76LIVAuE4tK-YDfdaBvlfNxk59XWjyar6GIe4F2u4nTeoOkVPnTDYE_Ouj4PGXHP3csEeY9KjU_YtO37WYxLtyw7PxwyIHiSqRVMgUYCWQ2r0l8E7rq4-jdDnZDRgQy7-xP3Q9v79RlkOqBGStwZ0sfaAuLvwRqP-ALSvMBB_cExg5zvG-u_SUChfVgLt1UI9SXrHwvyb5KsiLqRQY2nzUgRuFE5dLRuqmUnR8ZrkEXWpqm-EhM4EXh3Mz1HlFixqsAlRBJaxZh9_AyL_KaI9fKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لشکرکشی جان‌فدایان در خیابان‌های یاسوج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/467894" target="_blank">📅 10:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-VjShlXU3of_5NJacfJwTKF51-pTcp0_g8DV2jv3LW59cQWzsYwlNuLPBMyFB4M1JraM-s-0u7YXKjt48b4brDZb1jx59uLwsIzW9f0Qt_Qe6B3LMillaaRKhCZ3AEI1OjdotRV9kBJLlXcadxH-VioJV3X8YkBT5GLHQqv6N2mvs4Wbnngx2CZhciHsqSljAXFmhcAeYl045ruyG32aB_mPNadfurKHLat0p63dqMCUhq5dekG-ql_D3LupBuM6ENRSXCFz44p3PxuO3ThIltV8YCsJdgGHy9Y-84ExD18WBS7I61OYCBsCyqBOyAAudTfE4_5MhDUaETKm53I8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی‌ترین شوخی سینمای ایران
🔹
رده‌بندی سنی در سینمای ایران بیشتر به یک هشدار تزئینی روی پوسترها شباهت دارد؛ قاعده‌ای که گاهی دیر اجرا می‌شود، گاهی نادیده گرفته می‌شود و گاهی زیر پای تبلیغات و بی‌توجهی خانواده‌ها له می‌شود. رده‌بندی سنی ۱۵+ یعنی افراد بالاتر از این رده سنی می‌توانند فیلم را تماشا کنند و تماشای آن برای افراد پایین‌تر از این سن توصیه نمی‌شود.
🔹
اما رده‌بندی سنی در سینمای ایران صرفاً یک عدد است که آن هم پس‌از مدتی، با تذکر، فقط روی پوستر فیلم جا خوش می‌کند و به توصیه و تربیت ریشخند می‌زند.
🔹
برای مثال، فیلم «والده» که پایه و اساسش شوخی‌های جنسی است، همین رده سنی را گرفته؛ اما ویدئویی که دیروز برای تبلیغ این اثر در یک سینما در قم منتشر شد، همهٔ این تذکرات و الزامات قانونی را شست و با خود برد.
🔹
این اتفاق پیش‌تر هم دربارهٔ فیلم «پیرپسر» حاشیه‌ساز شده بود؛ اثری که رده‌بندی سنی بالای ۱۸ سال گرفت. قاعده‌ای که عملاً مخاطب اصلی فیلم را از آن دور می‌کند و در نهایت، به توصیه‌ای بی‌اثر شبیه می‌شود؛ مثل هشدار «سیگار نکشید» روی پاکت سیگار!
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/467893" target="_blank">📅 10:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
پزشکیان: زمینی که در آن زندگی می‌کنیم یک سفینهٔ خیلی بزرگ است
🔹
الان در تهران آب زیر پایمان را بیرون می‌کشیم و آب مناطق دیگر را هم به تهران می‌کشیم. آب زیر پایمان تمام خواهد شد و مناطق دیگر به خشکسالی خواهند رسید.
🔹
میکروب‌ها وقتی در محیط کشت رشد می‌کنند…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/467892" target="_blank">📅 10:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVSj9K_awASMXUPcdUJupqG3xqxAwNnWYZnyHEnLhlil6ybbmNZ-G6-zLhSlJu8U9uyJ0MYaft40rVaceKdNhKpeMPbw5KguEoKCnlQgQRudvKhJmwqbHLPj7BqR1HQ8393Z3WzxXWqOVUuJotJDWYSTtOSMaVhX8_QNUHjRBCBafyGQLLfHUls9XBxLN1E9Ade-0JHHV1MZ4jy2233b7W2GGNZ2ky-umZVo39Fl33bE5CM9weSeEIvcSaZ63RkMkF0595tX4OgiELlsrMM63gKwRnKYhTvbl__WoRzK6QkyL6C2VTq7IFsBdPSnjBVtYJH6mcOCyhQaImUcjnKBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری
🚨
✅
رفیق‌دوست از مدیرعاملی پتروشیمی فن‌آوران استعفا داد/
خوان‌زاده سرپرست شد
🔸
با استعفای حسین رفیق‌دوست از مدیرعاملی شرکت پتروشیمی فن‌آوران از شرکت‌های تابعه
#تاپیکو
، علی خوان‌زاده به‌عنوان سرپرست این شرکت منصوب شد.
🔸
به گزارش مدیریت برند، روابط عمومی و مسئولیت اجتماعی تاپیکو، در پی استعفای حسین رفیقدوست مدیرعامل فن‌آوران و پذیرش مدیرعامل تاپیکو، در نشست هیئت‌مدیره شرکت پتروشیمی فن‌آوران، علی خوان‌زاده به‌عنوان سرپرست شرکت تعیین شد.
@tappico1381</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/467891" target="_blank">📅 10:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467881">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهنگی مترو</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fW0EsN7magTUuzrJgj_iJOPPi4SCgzZLtyawt3NDA2J_Pa_42KXvW8x1Zir0BjSKDoofshuyCreT2f-zGAiXa3MD-INm3qdbGnWqE6RuamLS4rYqM_a-o6G9Ywh-ki69gfwHUOcoYx4GK8QCUGQyLU1AS9Vn9GmgVC5ddHFu0VdWBbIYNUV9oLH9vmnHOoy6P1eeSA6V3NsLRxmthMvu4S4-7fC2V7XAIlS8742Iiyokg6_8Uutmsb_eAM1SQ-cm-y320o3NJ3hl7jKtmqD7RnayHZQ63_4FhCAkrnu1Dk4P6Vay2u0U7xLMM8nzBGc8CByFlGo8qJkdQFZJmecBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0LRwsEUasf-cqqLTu4XUp_aU_DIq9q3lCM7QyGRatY9ik5eBMteD7tWiGhAqEj83ct7OF735C_McMsADlP6hNd0UbIRdoEHR0Qq8oYJ52r0hWfN-35QAn_dKp8RJwM3iY112VQDvFQXBLivcmRNC2CqNKmiQ3MJRzrtcl8ZjqcbFNLqwwNwqgVBYrzUxg6mpQZyl7phJrimWaxQkyUNNv3s1QsJHCQ9o8bbVsZxCioVkhyKBXKnwMJ3YOm4w-U5XuQHi8axOMaXQiGtQfx5LIO8iwbF-Hta8XQB7rmZULx7svuA4BO8xw5aK3igXVkZldHokHTss4WRc-byGOvv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LGYJuAFuna4frsT4kf7BswPY1qHzQbV5bjHY88cou6Qiccp55sWfbJOdRXwfofd-FC94xJDRLHdY0s7DgY96AXoDF1iT5xQQNINMb21cg5IFeQJzqRqRqUt-jk_OI2l54Mnypsw4tqaUBzA3yKikh4tmpVR7-8ui4YzoU2d9Ra0L9kCMPuh5XkOXUN5Jq11FDrFGiqhcUY4DGCYuHyKm_maIaXZPGGQpmFG3BM-PzGEcZTIzfhoXm5qvpXM71wD1fUi6R_Pou_OjkAua3X1y2pVVaAcp1vlBOXQVYW_LfiQtxa2XLdls6KQl7vo_d4dXg8xVCaslMfavn8i_arj0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_J0-21j4iS_R-ooGhWZorT9WNhwNgJFubvq7rNVI8jLXUknVLli0jaTxtWPNq0mMeCQewiHeF-o6bbp9CXNkunqfdzNinAI2dfFlaZff5cOsXY_N-FvNVVxxR5yrD-hoHmgTLxfM_ayuPuSp3wzH-65X14BybGD2F-HhMGbdhD9rqik9EPOkXlLAadq4SovhxIJtVBVI1xWWW4kEqkgbWjxIRaqZD2okIgxpT_nBGUY2FBNNYjl8CWyxxWlReUC0xn-TUYbwOk4odywFzhWozgbv1b63k1De4QgBgqkeN8MB9Y1HbGK-KFxFlkEqc58raeala_qeAmtSGgxejDBaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_SoJLw_eM9G7_1iIDO7xk2pWydZWct-v-VQRXJrEX4oLq-lLDtj6hw-ngi3_-m6fDBzxvrZrQrO5DkvTwNDXKzvkBuChG41XyUWN4dHZZb1qhMytOcGnQau_i4nX0SPqfcyA5Dj6EziqG26-WiVkrUUTRxLTshM6OToEWFgPxxd8TdKDYmblulD3XJj2VhVZ394Wrv-4fL0v8cq6lMesqFVeHO6OixfjeILvDw1bJHS6pg-XEuTZ5ZTsrNIwV-quiwZYwAZHljCid52EMfI1jWdaLkP140ejpA8N0ne0W4UXLVjpDhA0LFTDImsL6ffYydtP7C_2-MKuzgo2rQF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJKe5gVl8Vo4wVG8kLy_rPyNaKfOGSUiGbqQYi0O5XtXlXnOfxO6PCzhJpr2PWXxxKbyUj4nMT_AGLUjq_aNK6cMstbanOl3ROqUAez60I0Kqpywo1YgWuCNv8rhC4oHeQ2LYJ_SUypMMCEe0qhDDtWCJxr1BnZ4f8urAHXag25Vrd3EiJ51pKhtefOje1k_r_5YxkbTS0A3kUuNuTES1YHzd3hCHs6Ke_JxzLVMiGEiTk1B3R0HTLgmVVlshGLtkru6xN8nJVqnXZ0KTZr_e8WG83UR6xDz_6fdDUkqNs4fmKEWBEQUz2gZLrsVDxkxF4V_v5Dk53okdAgsGZmZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-jt4gPCZVlt3-YmHjNIlUQnX3eiLbY-W3OVUdZVEtUanTqRkmk-8Fm8-wkO8fwLkeDb49dy1AgRVUZQMgNNgN6NaNC67o6G1HPqm4uwR7CLoLdLo8G03eR5oraY5QkS1hqDPZ0boye6W84WtFYdUd3h1ij_Q3gjVu9mM8a8SY_RH9KSzf2wM8oNhY78hCWNKfRVDliaGFCiCAbhliElw9LWwmzQYSXUwVdLCe-XM3BVDg4YWytslggx3XeQVKhdaK9tv0GQ3VQR6Kof5VIZTT93yNOHF2kNXnFQgcIGNJ4iHY5jv36Gs58XD8XNjbIzegYS0C0psyXfbgnYAasBnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZ194D8y4m2C23opRzEv1sVJmPiFmzxh1utIMxf9B7DlWhA8_h6grutnviCgzpG3qM4LjZzpDZLT2SkioIGRqWOwDq-di8aB-HUjqI7EPofq5IROqx1kekT-03aUYacRk0e3PTn7zI0fLH5ryJw9FxSjwy5k_DwZ4C_Uyx5MRMZs6zTEq2YB_3G2FW9ZvJtsX8UBPWIMiFy2fCANX9--TwCgf8RhS4GmJvSMAhDXRZcCHhLitHT3BizPU96_VhH850BkLoAevl_PVvpEeqEaMdx2Y2QFF2UFvRcqCuZMUL3G6V7bHINHsI-aiyBF2jQiF4cEah8ZCpDDG8yq6xpDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RzASHBuYoON-qKeMw0tePsvpdLtwWAC22G4YV5TbuuJMKs-R0nCK6ZnE4pMNp26tKOh4-2tcrWsB9_bosJmP_159WNxhaeaxmmua76tKHcJp77ie1UZSRzmQdvjgbkqAF2JR-HLvw6S27wF2UFQ0cBa34Z-3UumiO3sl8tGF7MfPe8Y7FrQQNQvSgq_nFzKMFdY5FoZX-Ymo9mI1c1AQLWV1zbWlkMR-99QJbB0vQavfCQWjvJlTHCSuTb3yg1y7eVY99VUKEgmhDedLqQ8QJH3-aC6g3VF4iqgL2v7zP3-NALdnZy3bdRQ2ufO44Nx87JCk8L2GQtYUMuelJnxX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptWkeSLE4fmXSybpL5aW9Ij6xc9jiWGhYw5-8xfP5tRMz9RVj9D48eQihIUy6GJYMNImyX-aqesLWJuatrJH1vBw55-PR7_OPTlwk6yebhoF8NAgVaSgtuSYFvIgQRc_3dE59eSI7kmNxf3LzX6DPI0onAluJfTrJgvNva1f2fSmWganpaqhlG_uAmN0l0bADRA8-BpNqrJtNRQpeL-9GGCGX7niUL7JEPqAg5jOhlKCw4lMoC3yv4Y9ity_KMEzS4D_n6JUudGPfgQC5-oCp2Rvv7AbkOuxh_THVkIObj9lLSmHn72pogsNOfUtpUQ0P7liglCkrCIAxYT-BMm7lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی ظرفیت‌های گردشگری پایتخت به مسافران به مناسبت هفته فرهنگی تهران
توزیع نقشه‌های تهرانگردی با مترو
🔸️
با مشارکت
ستاد گردشگری شهرداری تهران
و در راستای معرفی ظرفیت‌های گردشگری پایتخت و تسهیل دسترسی شهروندان به جاذبه‌های گردشگری تهران، ۱۰
هزار نسخه از نقشه‌های «تهرانگردی با مترو»
در میان مسافران ایستگاه‌های تئاترشهر، امام خمینی (ره)، تجریش، صادقیه، میدان آزادی، هفت‌تیر، میدان کتاب، امام حسین علیه‌السلام، میدان ولیعصر (عج) و انقلاب توزیع شد.
@metro_farhangi
|
ایتا
|
بله
|
اینستاگرام
|
زیلینک
|</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/467881" target="_blank">📅 10:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467880">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/467880" target="_blank">📅 10:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467879">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77cd82f292.mp4?token=CVVqBQw3f1yHTkvqSxaAyPwlLA25rZ-d2eppzqhpHylSiJAruzmvwvwlZE_eRxOw1EqcbYRbisofBlZlrrIRrFznRKm1WCuD26VB5nfLZenr0vlvToDzoUrYTfs3PwP1qZISaFUS6Wi8i6gRHXDOcPFqe337MxuRilTsVNawIgYfZHvsYaOP7CBK92I05EFyURm4KxisK9LPUOhBBG8qJkh4bVaIGElYojabMoGqLbIASqqe8XhU2pHoEFHkO-x0P_A7zob6klvRx-69148J7aAMkfBrDIcCoQVGxiLYm8ddJhP3JyGhWG7zakdG2v8FpAbJq8PNoCyvchIl6OhCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77cd82f292.mp4?token=CVVqBQw3f1yHTkvqSxaAyPwlLA25rZ-d2eppzqhpHylSiJAruzmvwvwlZE_eRxOw1EqcbYRbisofBlZlrrIRrFznRKm1WCuD26VB5nfLZenr0vlvToDzoUrYTfs3PwP1qZISaFUS6Wi8i6gRHXDOcPFqe337MxuRilTsVNawIgYfZHvsYaOP7CBK92I05EFyURm4KxisK9LPUOhBBG8qJkh4bVaIGElYojabMoGqLbIASqqe8XhU2pHoEFHkO-x0P_A7zob6klvRx-69148J7aAMkfBrDIcCoQVGxiLYm8ddJhP3JyGhWG7zakdG2v8FpAbJq8PNoCyvchIl6OhCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: همه می‌دانند که نمی‌شود بنزین را ۱۵۰۰ تومان فروخت
🔹
حمل‌ونقل بنزین ۵ هزار تومان هزینه دارد اما ما آن را ۱۵۰۰ تومان می‌فروشیم.
🔹
در پزشکی، بیمار را آرام آرام به شرایطش عادت می‌دهیم؛ نمی‌شود با یک نسخه مسئله را حل کرد. هیچ بیماری‌ای در یک لحظه حل…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467879" target="_blank">📅 09:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467878">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c620be4b9.mp4?token=B1O8PkyhBc0wzGnSKn5y-xUSPT6ZcqnbzIcLvj07Z21oFwAs69m5f9gfk-TbIh_HkLXNpvQa6NhIZkIxHe5fbaU79dWLK3HBX28kn0M1uPFVHfpPR1w4fJKes2g4zJKOtSp-doHM1G4T8v1P-n9g1EIpEcYwvSEx76DEFTUJIvulWX13G_2No98qiaksgrJPnf3nufpYNJO8WD5migZW_Dqv6bdb_bxtTpoqEPwBeTDuuIvmYmG3MAX54fohHXMMe1FnLLI4zaw61IGiUDvjbMKvqNqVoZKmGecvVDFEOVqtHiJXzAzfk87pAGHxoJMgIUSKqBkHuYUKej350fbdSAliYM7IfXtTUZN9KmZmXbRiny74K-4xWvXrMZ20QBXD_Zjsi13x-yYGuZfk5gMtzw-LXw_dckMuXzxNNztdUqM1ERvD8tdj1z6_b5RT845Ke80s9XFdghFfuPmDMT6DWndA_UZULIJKDZ4sX41WzuFjvM4td1ZlWkk5iMfYuPVb8c4b2BJX3sl_hdkPJnzqyrRcj-DHd2YChbSKOmKaeFrAeehlod0hziUuLeZM04wdxMMWs4btLM7dncU3TEQ2tDY00x28AjWOWrCO8sNX2H9yrF-Pn-5sQFdmSbcnyJZb4J3mo03IoMebvGhJsGLfDoc3Kf72lIYp-hhgP56suuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c620be4b9.mp4?token=B1O8PkyhBc0wzGnSKn5y-xUSPT6ZcqnbzIcLvj07Z21oFwAs69m5f9gfk-TbIh_HkLXNpvQa6NhIZkIxHe5fbaU79dWLK3HBX28kn0M1uPFVHfpPR1w4fJKes2g4zJKOtSp-doHM1G4T8v1P-n9g1EIpEcYwvSEx76DEFTUJIvulWX13G_2No98qiaksgrJPnf3nufpYNJO8WD5migZW_Dqv6bdb_bxtTpoqEPwBeTDuuIvmYmG3MAX54fohHXMMe1FnLLI4zaw61IGiUDvjbMKvqNqVoZKmGecvVDFEOVqtHiJXzAzfk87pAGHxoJMgIUSKqBkHuYUKej350fbdSAliYM7IfXtTUZN9KmZmXbRiny74K-4xWvXrMZ20QBXD_Zjsi13x-yYGuZfk5gMtzw-LXw_dckMuXzxNNztdUqM1ERvD8tdj1z6_b5RT845Ke80s9XFdghFfuPmDMT6DWndA_UZULIJKDZ4sX41WzuFjvM4td1ZlWkk5iMfYuPVb8c4b2BJX3sl_hdkPJnzqyrRcj-DHd2YChbSKOmKaeFrAeehlod0hziUuLeZM04wdxMMWs4btLM7dncU3TEQ2tDY00x28AjWOWrCO8sNX2H9yrF-Pn-5sQFdmSbcnyJZb4J3mo03IoMebvGhJsGLfDoc3Kf72lIYp-hhgP56suuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر ما را شهید بکنند، از ما بهترهایی هستند که بیایند، پای این مملکت بایستند و برای عزت این مردم از جان مایه بگذارند
🔹
در زمان جنگ اختیارات را به استانداری‌ها دادیم؛ باور من این است که همهٔ مدیران می‌توانند رئیس‌جمهور یا وزیر بشوند. @Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/467878" target="_blank">📅 09:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467877">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7342a99a82.mp4?token=q-36xMrMrfjzkzykPbKQsXYu4cR5ja67Si_pcLasDYCWF4AxjFICsrc4Z4C3Fb6rIuAjzfX39IigrmqOHgoek0g9ctBnnORZ0D3Up13wye_EHeKkCPuW7kba7IwssJOWiqPsHmLRSzcdVgkPTAlSFjNS_VbLPzAD5uNv8Gmjor854ysWVAn0ucRLFRaLRSID_NfVgwScaWkEEfc9aokBtfV-mRXc4LP23jmhYGvu-1Ge_WHCLGsbjExc5y5gWquFw8dkhbxNGHu-UquoDYdamB8LP4Is5iXsJvwtJ3iDFDvEXUWkNZ4Nc9YlgKPJ2AkQ7M8sdNBfqpRb4Du4_5yFoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7342a99a82.mp4?token=q-36xMrMrfjzkzykPbKQsXYu4cR5ja67Si_pcLasDYCWF4AxjFICsrc4Z4C3Fb6rIuAjzfX39IigrmqOHgoek0g9ctBnnORZ0D3Up13wye_EHeKkCPuW7kba7IwssJOWiqPsHmLRSzcdVgkPTAlSFjNS_VbLPzAD5uNv8Gmjor854ysWVAn0ucRLFRaLRSID_NfVgwScaWkEEfc9aokBtfV-mRXc4LP23jmhYGvu-1Ge_WHCLGsbjExc5y5gWquFw8dkhbxNGHu-UquoDYdamB8LP4Is5iXsJvwtJ3iDFDvEXUWkNZ4Nc9YlgKPJ2AkQ7M8sdNBfqpRb4Du4_5yFoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان در مراسم آغاز سال تحصیلی دانشگاه‌ها در دانشگاه شهید بهشتی تهران حاضر شد  @Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/467877" target="_blank">📅 09:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467875">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qILKGjkUzKEB27NfHjaxSvfeNSSYSRbAtUMKtC8u933ea1RnZuEISwAnHnYmezpKNuTblVZ72jTTObJDL8-NPHzRdTv_m_R0YukFht0ZY41cKuRsB6OZfSGyQM_2ejE_IFB4IzX50tndBGRM0B6Kvevts9dzyn-HKEmK0bN-KfcN0OVoJBPgiKOX42AeOrgAsTerqUzr9X1e2Z91sUyfhwtgwNloZd5GgEVPGjyFeWvtSpWJ5I1EUhjBOMGFOvOgrmEsgFegpbmyGiPIZ4hhVyoKyMmdos87MqdHu5d5m_udcG9tqUEYBh2lKDr2e79S6ASH4JMDg1_C3z4mn2wNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله قربانی امام‌جمعهٔ پیشین رشت درگذشت
🔹
آیت‌الله زین‌العابدین قربانی، امام‌جمعهٔ سابق رشت و نمایندهٔ سابق استان گیلان در مجلس خبرگان رهبری بامداد امروز پس‌از سال‌ها فعالیت در عرصه‌های دینی، فرهنگی، علمی و سیاسی در ۹۳ سالگی دار فانی را وداع گفت.
عکس: روح‌الله خانزاده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/467875" target="_blank">📅 09:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467874">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فرمانداری شهرستان دزفول در استان خوزستان: از ساعت ۹ تا ۱۱ امروز انفجارهای کنترل‌شده ناشی از امحای مهمات توسط نیروهای مسلح در برخی از نقاط شهرستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/467874" target="_blank">📅 09:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467873">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ce22dea0d.mp4?token=BVB6HLEjb6-Cg3rOKkSFqXvWrX2huyHSbXsZeCjSumR9CGWldp7MIM0Ew8v4qULl1OBt0ZHKc8CX8KSbt3FQqa6ftK3Qx_9v2afvJqApwZVCvx-m-cfALcINXPTMPZlpo2o8ig8nRxvY0x9V52kA9CnlVhPN5CCTeHwhxAK4HnurtAf2GWgxnLq9HP7krhtjP6RfaGIaslU-Wy_sdpIFv9jDQf5EAht40F3jzZnLNIFIgecstGawYeJh-gwRHyM4uy6W1HB3F8aGbt-9YK4WXPSx5YkMhMF2ElzEGrq3GMviwbmASlRVkp4VgWApIv7s3u_X24CxIWrXlNg5V51eOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ce22dea0d.mp4?token=BVB6HLEjb6-Cg3rOKkSFqXvWrX2huyHSbXsZeCjSumR9CGWldp7MIM0Ew8v4qULl1OBt0ZHKc8CX8KSbt3FQqa6ftK3Qx_9v2afvJqApwZVCvx-m-cfALcINXPTMPZlpo2o8ig8nRxvY0x9V52kA9CnlVhPN5CCTeHwhxAK4HnurtAf2GWgxnLq9HP7krhtjP6RfaGIaslU-Wy_sdpIFv9jDQf5EAht40F3jzZnLNIFIgecstGawYeJh-gwRHyM4uy6W1HB3F8aGbt-9YK4WXPSx5YkMhMF2ElzEGrq3GMviwbmASlRVkp4VgWApIv7s3u_X24CxIWrXlNg5V51eOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: یکی از عوامل تاثیرگذار بر کیفیت شبکه، تحریم‌ بخش قابل‌توجهی از اینترنت توسط کسانی است که شعار دسترسی آزاد به اینترنت را می‌دهند.
🔹
استفاده از فیلترشکن‌ها نیز ماتریکس ترافیکی کشور را به‌هم ریخته است. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467873" target="_blank">📅 09:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467869">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKdRQos7apeSMpyzqCKoWqeyuQ7GrXGDS3QF1C0hVOROpBKfmU10Wd6sHtZ9WcK5llkrNkRAWtWryE38p44zgH6fast2Om0nWmgvSfv1cyxUxw4qGrUC44N-WAVl6IIW-zPQsvXoingvsgu7wl6X7APSFNUsTAsI7KRuAky0ath86ZBT-8KkFa1MJI4VO3rg8x54nzuWQqlhL3cCmXGRwj50wwzleMWtS3iA793wmoOhy_QVqtpFaCOfRWvUVB3LwQeqUMytuuMH6Q56SatEWV0Jf-jPgV0z9c17DNEAfj8JdffuL7Vltfg4rTxBV0i2kVzyKosecg1johg2CQ0ypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaUuvKYohJpb8XNZbUkkpkI1HdCX4yQs4nrEjht3qAwcC5mX2IgmdY2qz6PBuQo8e4Q9lOJQyTtNKuRO_-lGivstS7UY8i9ylXPCrPe9Ilt7l5YbywlW6h7m_MoSg1urayEqfVRNaXtJfNQGhL1L5MZdPTKzfxeF3x2PPVT9Rv4NXUwCR-ubuI7wYqXASq5Rf6Gxmib0zZMfG6e-f-0oGRG_-uOnT7mnG2G7STCsPSjMdidd29LowDKk6-Bj8WI0BnwQ-gUPsePAihSUY-x62iAz5nt8xCuuOaIX5zvzp9-wLFQGZrlrC7RdTuUY171o1v146HeEoHEyhxE7kvuVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UutHEghbxAnW5gk9GBvsDdJgl5KAHXpWtazDq78M1smAzGBSyOhy0DkQ9XG8BT7ZE3vdCrpFTa4HjQW0Q8yMbSI-C0gNRd9reVCvO7oMUpNJ7zjOgnUaG7VyfMFqmtQRa5Qy9K-TDMPeu2X5mosQyvslq9iSeMAi1wBEeSXpdmffGKGTxhDHplYqRf-iThr1aRlsyovD-tx0iAR299rZ50UMqxIPzzjK7kHAUl1NOTvjosAZ2YeQh27kUWuW7Z4o3TKkl0B1gIpbs8un2FxNi4cyGFbxw6NezlsxDkJjyaQb2GOV-Xf-LvNM7jzaBM1yhinuDr3TqhfnDoIAL_oUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcO4DZ-juH2t-Y1BJdtG5hgthGH_mnSziPTxJ6Oew-3IMUOAZq3xFOX58yOPk36BEqVH4wy2JTYIwM0_-_ZpLH6lzn0fi-MD4DxVYZp6U5G1yWaEOVZAjXnjNi6WMLV_ojxs_hsgsI8FRBgRIUQAKMSz1hGMoRxC-1HgV_EemtE9pncNAebVuxtq83qAmKW36vEk0d4s8OXzSCuLylqeTz0x_rxRCITc9erMANfnjXOCaphdcuDbOhRv-uxhF5i-sGnSbBRgsLFAj7LJ912IojfEBt00E8QsreIn7dvlUDzPRb_irdWBy5nXkI0ZNRGoeVQecFeGgVHzoS1qjAf76g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان در مراسم آغاز سال تحصیلی دانشگاه‌ها در دانشگاه شهید بهشتی تهران حاضر شد
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467869" target="_blank">📅 08:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467868">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87eaff606a.mp4?token=T-Sifglv1jrJRiDNoERP-9Bd_lc9ea3p55esQMSdBpoBTOazjhmw-UuUbdLRaR6kDYq3AIeHZgLNcUadVE5TFkMZxP8YWBe8uWSrX0-ahWnyyYvogb3zKNtGOYZCeZ9nxElwF029OL7Pw4ejj5SSVrg7rqZCVjs0MXETnCDTzJClZ-IkkfubGMP-bXFYWLqT6Gc-pdh-MGmxztfMzyG_ytz9F3MD22Nz6Cw_JdPj7zicuIhSfQuHG4o4ROZCszDP-11B17EYzemKNcUuLTHHyQRqUlDDKw0Rmx2oZoKfzK2SnLUUK3X9-omIX6N-LV3zUYq9aiPjy85l_dLbfMpOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87eaff606a.mp4?token=T-Sifglv1jrJRiDNoERP-9Bd_lc9ea3p55esQMSdBpoBTOazjhmw-UuUbdLRaR6kDYq3AIeHZgLNcUadVE5TFkMZxP8YWBe8uWSrX0-ahWnyyYvogb3zKNtGOYZCeZ9nxElwF029OL7Pw4ejj5SSVrg7rqZCVjs0MXETnCDTzJClZ-IkkfubGMP-bXFYWLqT6Gc-pdh-MGmxztfMzyG_ytz9F3MD22Nz6Cw_JdPj7zicuIhSfQuHG4o4ROZCszDP-11B17EYzemKNcUuLTHHyQRqUlDDKw0Rmx2oZoKfzK2SnLUUK3X9-omIX6N-LV3zUYq9aiPjy85l_dLbfMpOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: بعد از این سلاح‌ها را در میدان جنگ رونمایی می‌کنیم  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467868" target="_blank">📅 08:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164ece171a.mp4?token=rbUi9v2RxVmOcV_27pDbV5pB4oUq5VIw9PfubbOwEudI-rOe9cCT9lGZSEGqBb79b3moKF7c1SuyBz-Bu6Ws_a8OWG1ssKxCY8S5696nqbdc95JJ_maSVcae2lnlbvibod6ckho1nc8DI3GmX7NWFfU8Vmp_CKfv-5j3BrFWBvLoJjqqkyhZyp-GN4t7xssM4rad62MeshAw1b-vKMXHZg4GyrKAnjHikfl83IqZAQvdZHvOmu_cfj0f-dmGXSQraKtDjiR8iIE2QPu8eBN_G2biGGybOsKpmea_kFsj3IqNGRKQl5IPAxGTGoaipQksRStGRoLfZv3n4txdHrWgfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164ece171a.mp4?token=rbUi9v2RxVmOcV_27pDbV5pB4oUq5VIw9PfubbOwEudI-rOe9cCT9lGZSEGqBb79b3moKF7c1SuyBz-Bu6Ws_a8OWG1ssKxCY8S5696nqbdc95JJ_maSVcae2lnlbvibod6ckho1nc8DI3GmX7NWFfU8Vmp_CKfv-5j3BrFWBvLoJjqqkyhZyp-GN4t7xssM4rad62MeshAw1b-vKMXHZg4GyrKAnjHikfl83IqZAQvdZHvOmu_cfj0f-dmGXSQraKtDjiR8iIE2QPu8eBN_G2biGGybOsKpmea_kFsj3IqNGRKQl5IPAxGTGoaipQksRStGRoLfZv3n4txdHrWgfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشنهاد «وام بلاعوض ازدواج» در بودجهٔ امسال مطرح می‌شود
🔹
مدیرکل دفتر برنامه‌ریزی و مشارکت‌های اجتماعی جوانان وزارت ورزش‌وجوانان از پیشنهاد تبدیل وام ازدواج به کمک بلاعوض و بررسی امکان بخشودگی وام در صورت فرزندآوری خبر داد و گفت: تلاش می‌کنیم این پیشنهاد را امسال در قالب طرحی عملیاتی برای لایحهٔ بودجه ارائه کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/467866" target="_blank">📅 08:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مهلت انتخاب‌رشته کنکور تا ۲۰ مهر تمدید شد
🔹
سازمان سنجش: مهلت ویرایش و انتخاب رشته برای آزمون سراسری، دانشجو‌معلم و پذیرش صرفاً بر اساس سوابق تحصیلی، تا پایان روز دوشنبه ۲۰ مهر تمدید شد.
🔹
این مهلت به هیچ وجه تمدید نخواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/467865" target="_blank">📅 07:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌧
تغییر الگوی بارش‌ها از امروز
🔹
بررسی آخرین پیش‌بینی‌های هواشناسی نشان می‌دهد از امروز کانون بارش‌ها به‌تدریج از سواحل شمالی کشور به دامنه‌های زاگرس منتقل می‌شود و در ارتفاعات این رشته‌کوه احتمال رگبار، رعدوبرق و صاعقه وجود دارد.
🔹
در جنوب شرق کشور نیز شرایط جوی ناپایدار خواهد بود و جنوب سیستان‌وبلوچستان، شرق هرمزگان و مناطق جنوبی و جنوب‌غربی کرمان در معرض بارش قرار می‌گیرند؛ بارش‌هایی که در مناطق مستعد می‌تواند موجب افزایش ناگهانی سطح آب رودخانه‌ها و سیلاب شود.
🔸
از فردا
نیز آذربایجان‌غربی، آذربایجان‌شرقی، کردستان و زنجان در کانون بارش‌های شدیدتر قرار می‌گیرند و احتمال وقوع سیلاب در برخی مناطق این استان‌ها وجود دارد.
🔸
همزمان در قزوین، کرمانشاه، همدان، مرکزی، لرستان، غرب اصفهان، شمال فارس، کهگیلویه‌وبویراحمد و چهارمحال‌وبختیاری نیز بارش پیش‌بینی شده است، هرچند شدت آن در این مناطق کمتر خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467864" target="_blank">📅 07:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfPI5FouSQs2lEKD1otz3R2o5DhukZTPGA5ROV59zfAAE0nqpSaL-opQCf5k_tmLQ4AK-QNFqWwtSP2DZPxf8Rm1n35YHiUwljvRaxqfW_xUCbvqg2sBQJP_-CXhQ_s4_PoT01DLHMbN0kU_rJcAjSngeXjBMf6ETeow7rQ6rIOGRpd9k7b61OdyBRXNxqyqLrTjGkxHYYjrLf4rIiec0rDiamaktT0XxrTjwWCdZq0lUgPe35qcxlPPsA8vOqMB4vuYcdXZsGlMhXnwaOvxFO8LW1HMz_5kga-o45hc010fc2PrTLBjpJ6mGdSRUoH7mLWiomoFb_kuAKu_JVl8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور به باکو رفت
🔹
اسکندر مومنی به دعوت رسمی همتای آذربایجانی، برای دیدار با مقامات این کشور عازم باکو شد.
🔹
دیدار و گفت‌وگو با ولایت عیوض‌اف وزیر کشور و برخی دیگر از مقامات جمهوری آذربایجان از برنامه‌های سفر مومنی به این کشور است.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/467863" target="_blank">📅 07:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
مجری برنامهٔ ثریا: استاد فرصت‌سوزی‌های اقتصادی از دوگانهٔ تهدید و فرصت می‌گوید!
🔹
محسن مقصودی: آقای ظریف! با دستمال آلوده به میکروب برجام هرکجای بدن‌تان را پاک کنید مریض می‌شوید! دستمال برجام شما پر از میکروب‌های فرانچسکوها بود!
🔹
اتفاقا در کشورهایی که نمایندهٔ قدس سفیر بوده، وضعیت صادرات بهتری داشتیم.
🔹
رایزن‌های بازرگانی ایران در دوران شما درکل دنیا به شش نفر کاهش پیدا کرد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467862" target="_blank">📅 07:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly6pf5o3RKH7loWAiISBULNFfXXiWj-f_uw9iKQtxDcq8isXCNl7SKuB-jCJYErWAIIONl-Od9yprzi8cnGlv38rwLlcdIm8c0-NqiZGmYt17zfaWIpY6SfQKNV86nvIsut3G3g5EoP5A51psjJNPJJks14ZcpWntor-KnogRETv9EQ5oM9Mi265M2-m_LKr49jAMa2WXmEcOYtLYCh61tZI0v2_B4SIAGyjB4UQ8SqdsOaSfbLbfLPZNNqVw455CaPbsw0nfoTR-TjUGoRODEbPxU45mxYyCBzR8TVHlaTw1uBKlZQyxIVxkgEx3R0t0B4Ub423etFXFGCerAl21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوق نزنید، زندگی کنید!
🔹
در هیاهوی ترافیک‌های سنگین که گویی قرار نیست پایانی داشته باشند، بسیاری از ما ناخودآگاه به خشم و پرخاشگری روی می‌آوریم.
🔹
این زمان‌های پرفشار، نه یک فاجعه، بلکه فرصتی برای تمرینِ خویشتن‌نوازی است.
🔹
می‌دانید چرا این‌قدر به هم می‌ریزیم و خشم ما به پرخاشگری تبدیل می‌شود؟ چون دربارهٔ مسائلی فکر و نظر می‌دهیم که اصلاً در کنترل ما نیستند.
🔹
ترافیک تهران در کنترل من نیست. راننده‌هایی هستند که ممکن است درست رانندگی نکنند. آن‌ها هم در کنترل من نیستند.
🔹
اما حداقل چیزی که در کنترل من است، رفتار خودم است. من می‌توانم بوق بزنم، سرم را از ماشین بیرون بیاورم، فحاشی کنم یا خودم را بی‌قرار نشان بدهم؛ اما این رفتارها چه کمکی می‌کنند؟
🖼
چطور می‌توان خشم در ترافیک را کنترل کرد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467861" target="_blank">📅 07:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بن‌بست عربستان در جنگ با یمن
🔹
یک مجلهٔ انگلیسی از تشدید بحران امنیتی عربستان در پی حملات موشکی ارتش یمن به فرودگاه ریاض و ناکامی ضدحملهٔ نیروهای متحد این کشور در یمن نوشت؛ وضعیتی که علاوه بر تردیدها دربارهٔ توان نظامی عربستان، جاه‌طلبی‌های اقتصادی بن‌سلمان را نیز تهدید می‌کند.
آسمان بی‌دفاع عربستان
🔸
اکونومیست می‌نویسد دلایل ناکامی سامانه‌های پدافند هوایی عربستان در رهگیری موشک‌هایی که به فرودگاه ریاض اصابت کردند، همچنان مشخص نیست. این در حالی است که عربستان به سامانه‌های پیشرفتهٔ آمریکایی «تاد» و «پاتریوت» مجهز است. عربستان نیز از کاهش ذخایر موشک‌های رهگیر خود نگران است.
ضدحمله به بن‌بست رسیده است
🔹
توقف پیشروی سعودی‌ها در ۴۰ کیلومتری جنوب بندر المخا نشان می‌دهد که بار دیگر رکود به میدان نبرد بازگشته است. همزمان نیروهای ارتش یمن نیز در تلاش‌‌اند شهر تعز، سومین شهر بزرگ یمن و یکی از مهم‌ترین پایگاه‌های وابستگان به عربستان را محاصره کنند.
زیان اقتصادی عربستان از ادامه جنگ
🔸
برگزارکنندگان کنفرانس «ابتکار سرمایه‌گذاری آینده» یکی از مهم‌ترین رویدادهای بین‌المللی مورد استفادهٔ بن‌سلمان برای جذب سرمایه‌گذاران بزرگ، تنها چند ساعت پیش از حملهٔ روز شنبه اعلام کردند که برای برگزاری این رویداد در ۲۶ اکتبر آمادگی دارند. اما حملات اخیر پرسش‌هایی دربارهٔ امکان سفر شرکت‌کنندگان به ریاض و تمایل آن‌ها به حضور در این نشست ایجاد کرده است.
مذاکره؛ گزینه‌ای پرهزینه برای ریاض
🔹
اکونومیست مذاکره با صنعاء را گزینهٔ جایگزین می‌داند اما پیش‌بینی کرده که دولت یمن در ازای توقف حملات، بهای سیاسی و اقتصادی سنگینی مطالبه کند.
🔹
این مجلهٔ انگلیسی در ادامه نوشته، یمنی‌ها در مقایسه با عربستان توان بیشتری برای تحمل یک جنگ طولانی دارند. در مقابل، عربستان با تهدیدهای مستقیمی علیه سرمایه‌گذاری‌ها، فرودگاه‌ها و بخش انرژی خود روبه‌روست؛ تهدیدهایی که همچنین برنامه‌های این کشور برای تبدیل شدن به قطب منطقه‌ای گردشگری و کسب‌وکار را به خطر می‌اندازند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/467860" target="_blank">📅 06:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zphxs-_npM5VG5SOloxTUviYN4d4MjhR5wPHD8pGs070zmmrxBH8CIjhM_WoYnjjN0yfnsVRQoQe53VgMPEGbzf7RK8CfEJHlNf4n0lzBhpBEFwjBeLFoRFvnoY3NzBY7PBtG75ZT7RNep_IwRZF5SlMXTeFXL3xXzybTqpRlS_2eoO2v6oycZVtZRBgkjm-JXTFB_qZ4s333kHiMpBRuaiq0FP72oGzVmOwfLg1AIddig-3NsiaPVT2w_ct2NL_tH1TBDyNNJBdmRyCWiGmhbkWeaLsIro2rXLwGLhp8_WeZBl2YZrt8TnWI54c3TlnyXYqX9KldgivH4XECZWyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی در مسیر تغییر چاپلوسی
🔹
اپن‌ای‌آی می‌گوید مدل جی‌پی‌تی‌-۵ در مقایسه با جی‌پی‌تی‌-۴او، رفتارهای چاپلوسانه را بیش از دوسوم کاهش داده است؛ رفتاری که باعث می‌شد چت‌بات حتی باورهای نادرست کاربران را تأیید کند.
🔹
این تغییرات پس از افزایش نگرانی‌ها دربارهٔ گفت‌وگوهای طولانی با هوش مصنوعی و احتمال تقویت باورهای آسیب‌زا و وابستگی ناسالم به چت‌بات‌ها دنبال می‌شود.
🔹
البته که نتایج بررسی‌ها نشان می‌دهد این شرکت هنوز با چالش تضمین ایمنی در گفت‌وگوهای واقعی و طولانی روبه‌روست، و این اقدام به‌معنای حذف کامل خطر نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/467859" target="_blank">📅 04:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL0dpF7SPrlNQw1dfTD1AMinNsv8kkXfk1FVzs1rrOwNg_m_UU208C2xKJvHGlx0pb4H2p958LwjfaGJlneRCzWRjHcGRBQ86MXxsXhT3gUZJRZqDMLoWUR642CVrr2Y-jTktPE0mDBWWeH4xAEgHWeonsaxLt90SPBfNlbQynTJLFD2zGbwXw__GMBK_DSihx-TJmyZ24X4NQRhSXTAwS5SrIsZA2L11lyLiZUGNNIB3DgkQbVsPy4iVqvOSKEZKxeI8MY6MbTKmr_nozUlPPuull50u8j3oCCAfKkbS4pZGby95srUh4zQ419D23G4Mg-VGo6C-rfTtc3ZK4mebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عوارض خطرناک قرص‌های لاغری را بدانید
🔸
در دنیای امروز که با سبک زندگی صنعتی و کم‌تحرکی روبه‌رو هستیم، بسیاری از افراد برای جبران اضافه‌وزن به‌دنبال راه‌های میان‌بر هستند و استفاده از قرص‌های لاغری را ساده‌ترین گزینه می‌دانند. اما متخصصان این مسیر را بسیار پرخطر توصیف می‌کنند.
🔹
یک متخصص فیزیولوژی عصب و عضله دراین‌باره توضیح داد: بسیاری از این قرص‌ها با هدف جلوگیری از جذب چربی‌ها در سیستم گوارش طراحی شده‌اند. این داروها با وادار کردن بدن به دفع چربی‌ها، علاوه بر دفع چربی، ویتامین‌های محلول در چربی را نیز از بدن خارج می‌کنند.
🔹
طبق گفتۀ این متخصص، مصرف طولانی‌مدت این داروها منجر به کمبود شدید ویتامین‌های ضروری می‌شود که پیامدهای ناگواری برای سلامت انسان دارد. از جملهٔ این عوارض می‌توان به ریزش مو، زرد شدن رنگ پوست، از دست رفتن شادابی چهره، شل‌شدن پوست و حتی بروز دردهای مزمن در مفاصل مانند زانو و کمر اشاره کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467858" target="_blank">📅 03:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
منابع عربی از شنیده‌شدن صدای انفجار در شهر ابهای عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467857" target="_blank">📅 03:15 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
