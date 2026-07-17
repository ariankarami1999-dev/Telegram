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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 09:43:41</div>
<hr>

<div class="tg-post" id="msg-672016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfv7sQSJgi24bFbSzaaJahTBOHef1mDBD_Hk0o78Dj7BLFontpUohlBL_iMBCnsHj7Tb4DFoTYYGL552qfPUXnmtrJ0qYGg4yJzHvtcYth88McsUzFAxmY4nXhsdugiXMYJRk8ouqyNRt7FmzH3EycoASpiKIXgd4etRuCRqNhWx-md1z7T88B9xa265pNZwZZbDkbOclbJRTCzTAZM_JVa1wSv5Pj5WUeb2WPoamsuOEa6WVGlKHCpUSvsnWinBV_pFCcbFLcZA8kNu0W-z52v6ItsDFNgfDWrTNfCICpNWgc5yP5SOD8us8ZvWN_WKqXoYu_Mxl9i4zsWLNslgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط قیمت طلا به زیر ۴۰۰۰ دلار
🔹
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/672016" target="_blank">📅 09:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672010">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6lFLE4ThOL2uolHdoVCVbaCL0E3cwdIWTPhCkOsQ5W_aBRhVIqGvGF3erLDa1YNJJ6UJwQ3_yFRwtqyu-Nip5Tkc-WFoT9A5DyyHx9i75CJlGRcjvinohOnFBM_fd6TML4k7LkoCm68fLZ7_q8oGSDETYNUtSSXWd6wrgIE8yELKlPlZTLPIAXhdcpfhzPypQIjWp5sTbsR5UHrxkDUCC2RaS__bRRGLGLK7fbk3ZidEKDdVsCiZpXladBOy_ApevYcCcnFURyeA_P0VBCbzzBIJh-m4E9gxL68YIzFW_BWN7jto90SWp8PtF6FAvwqBv6O3LWPAFJhf8b4ujmr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHYxEShxjQUeumfPSh3TVSi2pMZPnLql2oAliCvLrYPCfas4qs38abf1KZL1-LVhulohfqISVmAQHLNd5EyJrtXV12htdQnOiUUajMVcK0s3_-hWvc3cpn1YTsGoH1TQs-JPhrPljPPzomRb936aTZh5gZa7SsNOuSi8WrU3YOSstOK5-XILuzl2KruoEIebSxzTyCIIwWOlRc_KweR_Z4JaY2O1mRFE4wR3TPbbga3mFpTACD3z4eW9Zh-WAcpzzt70E6Rab9-sDPGgsuT9F8JDs4U4AfCvG_Og-4L6HhK5PMYJF7D-tbn3bIcE_Ve3t2F4lCuXrpa7__4GSvrMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPIofuAMUqU2pFYZHHovNZv6kjlrXZ-3Px6jc6FXCWpl1gEuBZo6JqPrBK98z6vF_39tlKXLcEtEjxHiduXT46vUCNxyseqc_HXUwo1l2Zww2O42Y0O7GFjlNrMdDLW9kNB36QAEl03nQWhlJ2ibKPcagIM1HaiSgzMYOYwETTmLs6d2ota3VjXog2O4vClJ2bAXqpN3fAUqSZlk-1150ItIMesmf4iBIDJ2vJSFIQ_7eQNNlb6hLmAVyxB-wevMiO7HsAVbx4ZeFeIce1P94mA771-lO4sebkxeB0iG0i2xH7lbIdF4VfMSuVxGti5vUd3f2F7BI_4jTUYB1-l3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOoAGLF2F-tloruCVl_QH37Vpf0bvmmvjdVQp_NuQZn2ZG0jRw5vG1WU99ONL3tgmHNC8ute8DytHeKNDqukhpJyewH3uqC_vK2WrNulLd97FLsmShlAPSyStjWyXOFmXyJfzfdN9NaF4ck5fbpR0KdVUYqRTU0kU-0pQFdgahD9qzrh1uZEJZ9SIhc9s3kXLmirLPzBI2AQICeLelmCgxQqy4BfEQcvc0vFQBXz79X6BNyapUL7UCJ-5eBQqFjpPaC1urvb6zhIlUvbH66foxZ1OQdShHaaRm1Z3WZ_PqmoWEdqRkifQKGsf8kwi8Im6mFj7xvw8prDvgPDje6gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcfEwaH_eurUs33M67jt9yMZEKxOc7RLrs0gWk21qWs-f53I5XRjDLGGnKs1NJPpsJHVsuhmReauY4c89TTcA2FzZyDcdQPaXa8GJaUQFjW_xMb7zdxK8qx-kJIo_S4t_3R9D4zzUcVqEJYNm99TL0pfkcmvvS7pAZFneHWhNedsX90G4jn_K-rQxzwloLQHUjAEBpjECfgleZOHY3xSjMLG56nC3nKLyvhKJrHeh94aF2kh63vbIUU5yapYY26jfIa4zPgTMaO0gohoOoQCf8ovJsTxoY1zePN4eKyhRPG-OKNAVGm9etYKHxi1LxJllPQIbTvVWvQ3EXEIkIThhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/husns5CDeT0exdyrpbmFECj7YysYmev2p5jr8pc0onv_lm4pWkCZ9Zdb-A4OJygnMeGbkPRoQgpyh3KyTybmLVQecisJYZfCrHVk8nqPzLRXBIfBgp6rfpFVhwsSKYPwWfkYRM-SdOKRTMadqqAmm8qbk7V5NfQzmJJTPXWJDvQp8DIztXSlNQCtqAuopH_yN05iVxZVocaXU0P_JltiW6URT0js7ctYMuDbBPSiYcmbGRzJRn7ujf3S84-_fDY2hy19LLR5uEtXeDpb6C3fCuRkUqRfMh5JG3erUMMhDJqMIpSGkY_JJ_f93Fqxuu1qBhYlfzVNabzCcnMHS5RK4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۰۰ ایده خوشمزه آشپزی که شما را از تکرار غذاهای همیشگی نجات می‌دهد
🍽
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/672010" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672009">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
پایگاه دشمن در کویت در پاسخ به جنایت ارتش آمریکا، در به شهادت رساندن مردم غیرنظامی به آتش کشیده شد  سپاه پاسداران:
🔹
شیطان بزرگ، شب گذشته باز هم به جنایت جنگی روی آورد و با حمله به مراکز غیرنظامی، خدمتگزاران مردم در مخابرات و راه‌آهن و خودروهای عبوری، تعدادی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/672009" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672008">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی به وال استریت ژورنال: حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند
/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/672008" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672007">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حملات موشکی ایران به پایگاه آمریکا در اردن
🔹
منابع عربی از شلیک موشک‌های ایرانی به سمت پایگاه موفق السلطی در شرق اردن که از اصلی‌ترین پایگاه‌های آمریکا در منطقه است، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/672007" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672006">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
رویترز: قیمت نفت خام بار دیگر افزایش یافت و قیمت نفت خام برنت به ۸۵ دلار به ازای هر بشکه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/672006" target="_blank">📅 08:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت موفق موشک‌های سپاه به امارات
🔹
در تصاویر ماهواره‌ای منتشر شده از پایگاه الظفره در ابوظبی امارات انهدام چهار سوله نیروهای تروریست آمریکایی به‌ خوبی قابل مشاهده است.
🔹
این خسارات در نتیجه عملیات موفق‌ موشکی روز گذشته سپاه پاسداران انقلاب اسلامی رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/672005" target="_blank">📅 08:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ستون دود برخاسته از مقر تروریست‌های تجزیه‌طلب در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/672004" target="_blank">📅 08:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672003">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سنتکام مدعی تغییر مسیر سه کشتی در راه ایران شد
ادعای سنتکام:
🔹
مسیر سه کشتی تجاری را که قصد حرکت به سوی ایران را داشتند، تغییر دادیم. یکی از کشتی‌ها که از دستورات نیروهای آمریکایی تبعیت نکرد «از کار انداخته شد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/672003" target="_blank">📅 08:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672002">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
دوحه از شهروندان خواست در منازل و اماکن امن بمانند
🔹
وزارت کشور قطر با صدور هشدار امنیتی اعلام کرد سطح تهدید در کشور بالا است و از همه شهروندان و ساکنان خواست تا اطلاع بعدی در منازل و اماکن امن باقی بمانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/672002" target="_blank">📅 08:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر  روابط عمومی سپاه پاسداران: بسم الله قاصم الجبارین و قاتلوهم حتی لاتکون فتنه مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/672001" target="_blank">📅 08:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671999">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019c4e8a4.mp4?token=BOscTVyBGbhmM7SdUz-J7zruBpUPlK5LJlRyMCiVIBEdlSur-YnaeVYBLd_1JgGk-T7xdnTMDROmSYX8Qd6pJcAZ3Y4nmIyyXhi1V9Ok-iJl5tB_eDDn8a5WiaXkJtEnX36obXXNW4iIX-fuRasy6eUOhKBYwjH4n0yx7IueL9VXt2XtpUDfwQ4Ch7kUXJtvZSOZlItZu9SI7OtlU0R9zCuRbySFt_uj-MovPWoNTlFZQmfa5ZLsTD_g8GrLfU1u_E5tpHtBASqjA6SXcILWJWtAsFwwhyTMU-y6gFvIALVZyVDj3W8SCtgz9wOnjhwT7XIUMGAc_BMmlZWAzn0ijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019c4e8a4.mp4?token=BOscTVyBGbhmM7SdUz-J7zruBpUPlK5LJlRyMCiVIBEdlSur-YnaeVYBLd_1JgGk-T7xdnTMDROmSYX8Qd6pJcAZ3Y4nmIyyXhi1V9Ok-iJl5tB_eDDn8a5WiaXkJtEnX36obXXNW4iIX-fuRasy6eUOhKBYwjH4n0yx7IueL9VXt2XtpUDfwQ4Ch7kUXJtvZSOZlItZu9SI7OtlU0R9zCuRbySFt_uj-MovPWoNTlFZQmfa5ZLsTD_g8GrLfU1u_E5tpHtBASqjA6SXcILWJWtAsFwwhyTMU-y6gFvIALVZyVDj3W8SCtgz9wOnjhwT7XIUMGAc_BMmlZWAzn0ijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به مقر عناصر تجزیه‌طلب در شمال عراق
🔹
در پی این حملات، ستون‌های دود از این مقرها در سلیمانیه عراق، به هوا برخاسته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671999" target="_blank">📅 08:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671998">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رگبار باران برای شمال غرب کشور و استان‌های ساحلی خزر، امروز
🔹
رسانه‌های عبری: کنست با رأی نهایی به انحلال خود، راه را برای برگزاری انتخابات زودهنگام در اسرائیل هموار کرد
🔹
وزرای خارجه چین و پاکستان، روز پنجشنبه دیدار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671998" target="_blank">📅 08:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ddnDOKCy3PopRQ9SCqcqiG0vXf6Pnq1NWQ8NF6fEft_PMXoGUUPInxIie17DqwY-slJo9oBKdpEm1Sb89FSnYpjQb6Uhl4aLnJ3QrCizJNN0HK0-90adaWM-UDYt3wMwZRs69oj1plh-JGB2fLVaaGxvNJMHzc6uWbDx9UrxHZxK7gMYJM8PUxb-hfYwSmpPjt-9JWU-yacvecnGA3p7GOz7Iv3FjHfimRt-UFCp7KY01T52-r3KAyTnkyHSdpc4NZ9ShCySiQHgpWCekhHAvxEtgaLqzKb8kN2OvJCF-WFNBcd_qa4t4QotqhpjwBTxyWHWwBgor79IwHp-E6t7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JcFeRt566F_2dVFn9kMGAKyL0z0uH_WnVDWqYKadOwnI62lYGoWBEOVZT0elhJ9RL6aFlqG97NGQCFkBHAAInBR1p7p_5rIJa_cxYMHvcHa0AXUIfHn2z6I93eiOsdZGby-6EAbK9beCHB8lwmBVWWvjxZHlzQpM7iEQvaHnKK7xYyJ9Zka-vycC_5JILdGRPfaobsXjag0eiF6LNoYWKcqKsFlgCK2yMWQ9WoqTip8y6XU-_SbOn1Zu8sy-6pOLiyV7VDbnShijTj0E8spgQF2Ec4K4piAPKAQ4elhMyOqIhurkZZTD2dGgPzVmVZm1iR-n2XuZDhI30kn3fsovCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
داور فینال و رده‌بندی جام جهانی ۲۰۲۶ مشخص شد
🔹
با اعلام فیفا؛ اسلاوکو وینچیچ از کشور اسلوونی دیدار فینال جام جهانی ۲۰۲۶ که یکشنبه ۲۸ تیر ساعت ۲۲:۳۰ در استادیوم مت‌لایف نیوجرسی بین اسپانیا و آرژانتین برگزار می‌شود را قضاوت خواهد کرد.
🔹
ژسوس والنزوئلا از کشور ونزوئلا دیدار رده‌بندی جام جهانی ۲۰۲۶ که بامداد یکشنبه ۲۸ تیر ساعت ۰۰:۳۰ در استادیوم هارد راک میامی بین فرانسه و انگلیس برگزار می‌شود را قضاوت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/671996" target="_blank">📅 08:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671995">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
روابط عمومی سپاه پاسداران:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات نصر ۲، با رمز مبارک یا اباعبدالحسین (ع) و تقدیم به سربازان مظلوم شهید بمپور ایرانشهر، با حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه تنف سوریه، علاوه بر انهدام یک سامانه راداری، چند فروند بالگرد خاص عملیات ویژه، در قصاص خون سربازان شهید شب قبل در ایرانشهر، تعداد زیادی از نیروهای جنایتکار آمریکایی را به درک واصل کردند.
🔹
کنترل کامل تنگه هرمز کماکان در اختیار رزمندگان شجاع ماست و تا زمانی که شرارت‌های آمریکا ادامه داشته باشد، یک قطره نفت و گاز از این منطقه صادر نخواهد شد.
و ماالنصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/671995" target="_blank">📅 07:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsN1btqSXzNzAZJJ0u0Vpqanqsylyv_FXiYmb_TPnx9-HNnjlldwFDuuJIpXk7zathuSlw_bROzR20gqjT0E_PABDHb4o8YBFQOANUIBzvBGcqa4IKYDhjwtCU4H_3Sm5x3hsq9swBbFld3UjPbDM_uH4GyHuoNgRgXRmN1z1qPTK8DSp9c2OKuQX2-biei6zFyB9t51txIJBN9KHgy6KZEUBpeVoWhaNagZEDGZWrc-k_Rg89XYjfckVtqiEVeJu8UttJsalDcqtBD7TPnc1WuWeX4Ukhh8cwWDt8HrsPaKiiF6gWLrM1SOdozWao75lWLZBQ0FcS7VjLwiqdFVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۶ تیر ماه
۲ صفر ۱۴۴۸
۱۷ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671994" target="_blank">📅 07:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671993">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
منابع عراقی از شنیده شدن صدای چندین انفجار در اربیل خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/671993" target="_blank">📅 07:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671992">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔹
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔹
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
🔹
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671992" target="_blank">📅 06:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671991">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
صدای سه انفجار در چابهار شنیده شد
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671991" target="_blank">📅 06:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وقوع انفجار دوباره در بحرین و قطر
🔹
منابع محلی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکا در بحرین و قطر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/671990" target="_blank">📅 06:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwjM_UkNgB8bntpHKLcnsYdABqFdGHztTspHVigHSW69-zxyuwhn7DRz7gr1pU54CKLHKwc32IU24UV9ybz_Rh_sAmJOT7_B2jJehwySmQhGDyN2JjCmyuT5z9_2JRZaUnKEPReEGUdCVEuG8_LF_nuP-zQk2geH0kVAOb2tNIjf9UwTWg-d-RiOCwZ2Jt7Dq_cZRulfSN5-nh3_xz-jMyHspyiv48iH9awuWumrvEWWUoKIHMkV7qrRbpTglmkYLOjwN21qwtaBt_3RJaIJHOGrGU9wZXOxLK5rtNLZ6ejJwb8HPM3V8Q01Djd5fIWAgmbU_gu2Xmk4OAQZVRNqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی: پالایشگاه‌های نفت و پایگاه‌های نظامی آمریکا در بحرین مورد حملۀ مستقیم پهپادی قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/671989" target="_blank">📅 06:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وقوع انفجار دوباره در بحرین و قطر
🔹
منابع محلی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکا در بحرین و قطر خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/671988" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671987">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحلۀ دوازدهم عملیات صاعقۀ ارتش؛ حملات پهپادی به مراکز پشتیبانی ارتش جنایتکار آمریکا در کویت
روابط عمومی ارتش:
🔹
در پاسخ به جنایت‌های دشمن مستکبر و انتقام خون پاک شهیدان این مرزوبوم، ساعاتی قبل و در مرحلۀ دوازدهم عملیات صاعقه، پهپادهای انهدامی آرش ارتش جمهوری اسلامی ایران، محل استقرار نیروها و مراکز پشتیبانی لجستیکی ارتش تروریستی و کودک‌کش آمریکا در کویت را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/671987" target="_blank">📅 06:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
دشمن آمریکایی برج مراقبت دریایی چابهار را برای سومین‌بار در یک هفته گذشته مورد حمله موشکی خود قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671986" target="_blank">📅 05:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: تازه‌ترین موج گسترده حملات خود علیه ایران را به پایان رساندیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/671985" target="_blank">📅 05:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: "روسیه، چین، ایران، کره شمالی و همچنین گروه‌های غیردولتی، توانایی آسیب رساندن به زیرساخت‌های انتخاباتی ایالات متحده را دارند."
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/671984" target="_blank">📅 05:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
‏ خوک زرد: باید مجوز فعالیت شبکه‌های تلویزیونی که سخنرانی‌های من را پخش نمی‌کنند، باطل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/671983" target="_blank">📅 05:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671982">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای خوک هار: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/671982" target="_blank">📅 04:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671981">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
خوک هار: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/671981" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671980">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حزب‌الله: این حزب در انتشار فهرست متهمان همکاری با اسرائیل هیچ دخالتی ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/671980" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671979">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZO_4N4-OXAJZViwdk2EJF4IDt9B_pjPMd1QCvw5BJopJaAludwz84OpelVWvbw2UBkQV41YfW3wDZmMxPiL5eo86dMIL1ZSc3Gw4EaqexFZ3pDvoNZUILYlM09hZ0kat2d_4Lak1LySx-Kqm8QGmENjGinudFqqtzYx1_KoiArOufW-qirNMhnIUas8PPSkTpPiWhJg5N_qV5OFLv8byyOhFdphN54ptUyNXM2auzIm4lKD-dgvUDAwXf4fNei4Idxxrd7jJkV-T0x5OAmhjYikM5Nv9nD_IPsCGYGNIWeSxUuw8ah4YDiTD9fmqdRz31kS8vg4FlIp8J_b9MbibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر مسیرها از دوحه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/671979" target="_blank">📅 04:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671978">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شیرجه موشک‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/671978" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671977">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توقف پروازها در فرودگاه قطر
🔹
وزارت کشور قطر: در خانه‌ها و مکان‌های امن بمانید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671977" target="_blank">📅 04:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671976">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
خوک زرد: ما در حال حاضر برترین کشور در سراسر جهان هستیم
🔹
ما اکنون در ایالات متحده بیش از هر زمان دیگری سرمایه‌گذاری داریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/671976" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671975">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/671975" target="_blank">📅 04:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671974">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجار در پایگاه آمریکایی العدید قطر گزارش دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/671974" target="_blank">📅 04:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671973">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/671973" target="_blank">📅 04:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671972">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq8fzTHh9nE41X5gO_cR1Qh8RQ7nuq3j5hSsLLNhM-w0hmwoXkO8qAoT3S2aDhoHHYRvgne_SNS-Wa_USxPXQBvdQemX7eY-pe95sZapkNY9YewHMZDmFs3-jg37j9lAZvYh2T-0-XDE5SbaRiw157R8SFWnI_rnWAhjPf9iA5aHt-XfbeJ0H-VK2l5kAnzmdCXHDCeKzfc0dLTdE_1SEhdzHW-qjbFtr2zcXiP0L_CAhwU0h4-Zn-hvZhXu_lylsBx_anADQaE6i2nmQlANN_6CznInPpJndoonLy3VzVnEBgB7yYPrGuAQ2lrB4YU6OxaWeRvKcLV-6gIMzpTEgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آتش‌سوزی در یک نقطه از کویت در نزدیکی مرز عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/671972" target="_blank">📅 04:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671971">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
شمار شهدای حمله به پل‌های بندرخمیر به ۳ نفر رسید؛ ۹ نفر مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/671971" target="_blank">📅 04:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671970">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجار در پایگاه آمریکایی العدید قطر گزارش دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671970" target="_blank">📅 04:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671969">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
حادثه در پل بحرین-عربستان
رسانه‌های عربی:
🔹
صدای آژیر آمبولانس‌ها و ماشین‌های آتش‌نشانی که به‌سوی پل متصل‌کنندۀ بحرین و عربستان سعودی در حرکت هستند، به گوش می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/671969" target="_blank">📅 03:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671968">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مروری ساده بر آنچه گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/671968" target="_blank">📅 03:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671967">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Lh2JsJRCo7uID8a8T7BJHcaJNsVfFx0b2MEQYxZi_yBpShUJwBcuORd785yfBdpRTBbh6UcjrMLdbRDxNKRFm2FvllOZcEqTGTUwoYiMLPCdBe3slryfQHuskg9Flcxy8LoieVRu4WGurRSEPGVDyJKslljia8wB2cMjorCqgyyCDqePOzkMBaoQOrE8cd_FhaUmTxUJA_tnKtPK4SZf1fNs3hZmJgwNKckqZMZw_0DonWSR8q-W5Iqgu4vmU-mhWJYlHn39tw96kF1iVMwOjN9x_Vwmu7AvK1szpsq0UjWdWSEJG7UsvC253rly_bM9lteT7il17T8RVM7yVd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اعرافی: تفاهم‌نامه تمام شد؛ مذاکرات را ادامه ندهید
🔹
اکنون که رئیس جمهور آمریکا با صراحت و وقاحت تمام، پایان‌ تفاهم‌نامه را اعلام کرده و جنگ را آغاز نموده است، وجهی برای پایبندی به تفاهم‌نامه و ادامه مذاکرات باقی نمی‌ماند.
🔹
رئیس جمهور و سایر اعضای شعام و فرماندهان و مسئولین دیپلماسی کشور باید تفاهم‌نامه با اطاعت تام از رهبر معظم انقلاب به همان مسیری که ایشان تشخیص داده‌اند، بازگردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/671967" target="_blank">📅 03:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671966">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد در مصاحبه با فاکس نیوز: اگر ایران به بازدارندگی اتمی برسد، مجبوریم آنها را با احترام آقا (سِر) خطاب کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/671966" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671965">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/671965" target="_blank">📅 03:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671964">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حملات موشکی ایران به پایگاه آمریکا در اردن
🔹
منابع عربی از شلیک موشک‌های ایرانی به سمت پایگاه موفق السلطی در شرق اردن که از اصلی‌ترین پایگاه‌های آمریکا در منطقه است، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671964" target="_blank">📅 03:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VmWyhlE68M0dKEGX1B6MukcgmjHXOndN8hhpp7WmfJhmvPf7pt5BhUsUvVmXyTTCpj_8WlmDXawVXeycEyERwO2QKkAFXk9iMRkj_GosLGaaIYmN6xmWZFO5XWxyAARB5pUjX5qr8fCGCVzNTHxoYsZ1A1XILzcTVCYqWei4ToqjlU09RI5X_RHPIgcCOTsZaB0RRVRuR7IefoDiGSNMAFC90nKzgW-7fSFfQuSOzEHbO4QnLyAAeSfnkfixPRJY8rvQot0F9Ftd7HvgE0EIiYIqze-mJ5vilHxqhy7JmVOeNZtRtsKVJ8tGZkGowW_zD5xFMTI2qWo6-Wm6ESD_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jkj_w7Ux8qTVMruNjrbpDc8Q3HtY9ViiSrj6sFLDjhD7B9XtYCuJ2ZKskQxprD4MS8DKq4LDkpDQV48LDO_lFSRg2Vq2Rk42en_NmI41sXMiWpOXxOCTkyDfj9LDGoPNViHypo6VFqotEDMMLhVCEmBaPLZ6gBPNOwAfyMKE6rRHxcaV3m9e814azrerl-xt6K8KBlzsU7tdsTuIpxFQP2nvhoXF50ndYO0SAeAnMbjjZ-oiUJF-nBDxixAsDOAgSdjX2vpPQXq_VpwEFsHaqAQKusWvNAcH-JWVE_wzQrUpMEezYubbtKPP0miuXswqqWGxgz0vtvCFUVH0Tu2FyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
داور فینال و رده‌بندی جام جهانی ۲۰۲۶
🔹
با اعلام فیفا؛ اسلاوکو وینچیچ از کشور اسلوونی دیدار فینال جام جهانی ۲۰۲۶ که یکشنبه ۲۸ تیر ساعت ۲۲:۳۰ در استادیوم مت‌لایف نیوجرسی بین اسپانیا و آرژانتین برگزار می‌شود را قضاوت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/671962" target="_blank">📅 03:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج جدید حمله موشکی از ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/671961" target="_blank">📅 03:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ادعایی از فعالیت پدافند در بحرین
🔹
فیلمی که برخی از کاربران منتشر کرده‌اند فعال شدن پدافند هوایی بحرین را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/671960" target="_blank">📅 03:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
کویت: در حال مقابله با حملات پهپادی و موشکی هستیم
🔹
ارتش کویت اعلام کرده پدافند هوایی این کشور در حال تلاش برای مقابله با حملات موشکی و پهپادی از سوی ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/671959" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای انفجار در اردن، بحرین و کویت خبر می دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/671958" target="_blank">📅 03:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671957">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از یک مقام آمریکایی: حملات هوایی آمریکا روز پنجشنبه چندین پل در ایران را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/671957" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671956">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در بحرین
🔹
منابع خبری از فعال شدن آژیرهای هشدار در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/671956" target="_blank">📅 02:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671955">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به دو پل در بندر خمیر
🔹
به گفته شاهدان عینی دو  پل حوالی روستای کهورستان و رودخانه شور شهرستان بندرخمیر مورد اصابت قرار گرفته است.
🔹
راننده یک خودرو شخصی، روی یکی از پل‌ها شهید شده است/ صداوسیما  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671955" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671954">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa01daef0f.mp4?token=H5GZbtf-b06QVy-sRu2lONCWIX3EZB6Ui9DiPy1sHTvTIbpFnTkuQVY4EQKoJ6VaEm_1AdqUNBldg4DcEUiz-Ax9LwQPdrHvq1MiOsL15Qd5CLRloLk7bfukC-P44ciASIu6zESbFik0xvU5Ns76jboOuH2yRVFmjcFe7dN4SEsly6M-ddudTnflYbSob0us4YHHuROHb1UQ4Ss4HaAKGrZCJRUXP75k3hbI1iTMz7Mzsym6TQHlpqwNA0ndvAXyHsA-N8e0R8orQHOhwY1xtYV88RE_5SWUF3c-UGwKf_yyWUaDcg04Yv6aE7Debr7_AubD4DWbM_nTIizfZ826eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/671954" target="_blank">📅 02:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671953">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از یک مقام آمریکایی: حملات هوایی آمریکا روز پنجشنبه چندین پل در ایران را هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/671953" target="_blank">📅 02:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671952">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
منابع عربی از وقوع چندین انفجار در پایگاه‌های نظامی آمریکایی در کویت گزارش دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/671952" target="_blank">📅 02:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671951">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی: اگر جریان نفت و گاز از طریق تنگه هرمز ظرف چند هفته بهبود نیابد، باید نگران آن باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/671951" target="_blank">📅 02:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671950">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
دروغ سازی جدید آکسیوس و اسرائیل در مورد طرح ایران برای ترور ترامپ در ترکیه
رسانه آمریکایی - صهیونیستی آکسیوس مدعی شد:
🔹
در جریان سفر دونالد ترامپ به ترکیه، اسرائیل اطلاعاتی را در اختیار ایالات متحده قرار داد که بر اساس آن، یک مقام ارشد ایرانی به یکی از همکارانش گفته بود ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/671950" target="_blank">📅 02:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671949">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b2cff3a5c.mp4?token=U3ibehVTzsh0VvEwT3UJ3Y3PmkrH2DySVTK_WfgLwzsccj1XO8Yq0c6kduZOIdQXMfKX628V_M3pv9L0N3VJpFJAWfYRIZK-JpVY9qYM82qN-LEt8ou-EnUv0ui5-BYb4L9zkA_azmeJWKHogBOvo1uJgdwCL-yofa2tGAbB5Ho3wv-2uzcY-_jvxWZnhfg45lD__ZgBURS5t9zy2xK8qBKmMog6JQO-t2XE8CODyackInVnrLms-cUAVshhKLoXG4OdA-uexnEyKqc5scQ_AySSEYpYkgFxuOFg60d8nRNFPIpMNDOahBAiqIIX_VLtOnxSINVpAq__Zw_slLq64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی دیگر از آتش‌سوزی گسترده در زیرساخت‌های شلیک موشک در خاک کویت
🔹
برخی منابع می‌گویند جاده‌ای که تروریست‌های آمریکایی از آن برای انتقال سامانه‌های موشکی خود به نزدیک مرز عراق و از آنجا شلیک به داخل کشورمان استفاده می‌کردند، به شدت مورد حمله ایران قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/671949" target="_blank">📅 02:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671948">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e155b8e5e.mp4?token=iVYVqZeQDmi3AnwlKX2AJ9Xt0-qNlmAlhogyRtg-Ce-4V-k2kii0GRy6vF-BG63jkMXYZzurXreO5QBy59YGnbTqMWn5zia32FkRtKWNYIBdSIOKQ2ISK4VbDdmk7suZ-rLl8vCKV1zEskI-yH2-I4Emsf01Ge41o52Nm95_RbuOwcoi4HDoOttOWnb3GQX6hHhZHfirM4w9EkSxuFFgUAJVs19rwVLLEgzMTUdk7cvj_Ivzv_EsyESpLSbrHq_hFkFddiCD5URWRcU5Lc4gUEEqox0_eXhUygBSlPrTG3ts-02WOj1MXgMKp9aodsTOyuqe3M2K4NzRdY-wkRLYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله یازدهم عملیات صاعقه ارتش؛ مراکز و پایگاه آمریکا در بحرین آماج حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در پاسخ به اقدام خصمانه دشمن در هدف قرار دادن زیرساخت‌های شهری و مردم بی‌گناه، ساعاتی قبل، ارتش جمهوری اسلامی ایران در مرحله یازدهم عملیات صاعقه، محل استقرار بالگردها و هواپیماهای شناسایی P8 ارتش تروریستی آمریکا در پایگاه الصخیر بحرین را هدف حملات پهپادهای انهدامی آرش قرار داد.
🔹
امنیت و استقلال این میهن خدایی خط قرمز ماست و متناسب با شرارت‌های دشمن خبیث، سریع و قاطع پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/671948" target="_blank">📅 02:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671947">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
فرماندار بوشهر:
حمله آمریکا به بوشهر یک مجروح بر
جا گذاشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/671947" target="_blank">📅 02:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671946">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd9be4b95.mp4?token=DaD0w-iQDW9zlSt_CZoRcxhUtsR-2z_9Pxg2iXsOErlsSqzG6HOVDVRWTagyJQKz4UhVyJhTgJXBEukSA8SC98TB_DbefAIzPvCBXYsRc9QlZwvGS8848GHW3n0J7QPXoAO1zNj9KPh-NslHODsuG8cDfpRkkDN5OLd6N7mfAcuERd1oUCWn2P8Q1urXN_ynDhT577fmx1Ugy4p0nRoj5eo47-zHkaoCbI6FIsyoxJondPBzcAz_s6qmotur-bvhFKih2R9du9J9iX3qjSQfp3KV8me6DvYTtLQOm1g3zZPqQMhn8KfTaBHT0ZtJCbEGT03L7J8tbPBAo0f2aS0Efw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور خودروهای اتش نشان و امدادی در مناطق نظامی پایگاه امریکا در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/671946" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671945">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2p0Sm3KBKMaGKUfVBuat-o3GPgGkKWQWD4c0zMueAZ82rQXI3Fu-ndoz8prqsAD_i1nNPE8D6e7RVf93MmnNhPANPQjL-g5P4UbtDfdxKoqoTuli6JpZXjx5U2L-gtKliMlIyuJBKz434WaZt7AWH63tQmOYSNGGCCTzLwS2OHhFIl3XtbSLZmHAH1WzDCp1LudSj8OHYiH-o18wuRnPjMyApc9UZ83Qm8yacrrLf762e2wwrjj7NkfctjZjgdQFx3Ls6ihOzXTtMvTqytV2x93y0xiTASRhdi7_9FyyigK4Waw6FjaczdTcUgcJJjDuq2xRJ7mf8B7PyMJgu5EeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش سوزی گسترده و دود غلیظ در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/671945" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671944">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
یک نقطه در شهرستان دشتی بوشهر مورد حمله دشمن قرار گرفت
معاون سیاسی و امنیتی استاندار بوشهر
:
🔹
بامداد امروز یک نقطه در شهرستان دشتی مورد اصابت حملات دشمن قرار گرفت./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/671944" target="_blank">📅 02:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671943">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/671943" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671942">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7df7ba20.mp4?token=WHnEw-aHqNgcnA0vfXIUVDeO7TT7h8qcNutD2LFfXkR_6-WyOCvsxnQUcdP_rvKjDQR8P3EONeu5gdFxcK847hxD90hI-7xEoi3kBDnJwlP-G746RYlNNeCSg6jQYzpKf9fUNQhnxKwTsQNT7Nj6TSg7UK_dZUHWjc6z6RKJw_4yYS6saS95rScl1sL5jhb7Bpxvn5VHGQ5Igpn55KaaenZKHX509jEqZ7iiohLBOJazg69y9iIm_DFjQL21R5Tq7mh8s55ekv0LWyoflTvOMYQ1zWIC5Y21jR2wq8eNuwNlf_uLv2F5uaOgRWrX6gDuKZQaeO4RR7I2d9a2sEfNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/671942" target="_blank">📅 02:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671941">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f84b37246.mp4?token=h5PbRZQAE2avKupeVQOYpS2E87IMOsgGV8lrLrSruWyg1zKSP-cOQ_WlHdZS5bmNJN6QzfS_fiQ8fETuadad3tbaYdunDRCbQydhlUcpKxM7ODYpmINjTDwsTh0vHy-j6baJDtDoyOfUlJfy_fdJ1GICGuUYOzqrzChMuzUZ9myouElB3pYka2bMBr6-kTe6exSEI49qQaQ6x1uVJ7DPzynSbSIvYUOx_-a99QelGCN_6SCCYdphmqFxUA_nJwqUYxmnRxx7F2LMtFGZF5GsjBWksooLT8O7UuImnAbqzmqmT-PoyU1QTHl2oNjaVaBy1NDqUPvALKVnFY8jjZrhcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رادارهای آمریکایی در کویت، دوباره مورد حمله قرار گرفت./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/671941" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671940">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f67eb572.mp4?token=XT_xjMDLVWBdKqhhB7v3gYHYU7d-VuD4u6_TY8BH2R0x8INigKZZrCIZ3ISCeImfgBIyQWvC6Hf2usm_ePKOYVJglZo86NCq_XoW9i3J9NtL1LC6jEIYI6aBZrCM0fTSrlDsd9tn551dXg_hjyFsIhSYx_ixKwEk5i2acWYJW0OxxUPDSgNMCQk5w8XXc_RN1V573--io1J6C_FfShq0xo-JjxGKWglLNetLZm5L0cEBT37scRzeFP1VGJTylUdHZVL_uCvDhaXAHEugX3rHnpumu9j5pcW-ciagqCYHHuJRu_UBo4W7aMudaQBCYc719GUns0i1LbAo1GfZDUK2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فعال رسانه‌ای آمریکایی به تهدیدات ایلان ماسک: من در بزرگ‌ترین مراسم تشییع تاریخ شرکت کردم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/671940" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671939">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=Qgy1fXpAZIQ0B_w04JAsIz6v1vbpPRbdTdE7IKMeC7Qm9fSHvp7lMUDmrf3nQZa2NnNDbHUT9itLVUayRcTbtDZYgmRgBY3g6JaNwLBMt32HBdu5_3XJ2TNf-VxqsyuqZEeJsQHiAcHNdK5qfCOaq4EViJNklNt-6lRoVqqqf4oYATAD4yeW9Ls84pRhm6nz89wVNP_HgoqTVi8PO_g8l9UIQyjMJytNvrnIgyFG8C5ox6WH2TK38m-5tHufIhYclOp8b8T4bCTSywg9Wx_MM0Tu8OwZJVI8uWXTf1zy_nNFwAuNkfnLk5RYe_HlXErvQqDNFgyqBuT-4Hh45sC0imnb3auf_oDC5Rtb1I6cgoa89-N2SHszIRYh4lv7mrJktwcRgOY7PrgrbRHGw8m8hrWpmajRTvib598oKCETSH7f8m2fIjs4tPL9BSb7TQzpQDlw1rhXw3egI5IQVYsgCJuF7DGYwSPKRaCzcnaSWeocz_4SzQ22Hd4B4TkrrkbwRtqUy6GOWMf7ZjxT9_oOkgm_BXW4EJ-rnN7CJ6bAQnDBnPi4bjUIbvumqkgwe1a1Bl_qAcXyUiEcwYVbvZMDw2dds2LlVjrEj5O-rvT6OcGe8udg0UNrdhN93nprj8xhZmDr28YCuywOMVLasW4epMHBzkaZdq-G2DWTHqVxav4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530b6d1ce4.mp4?token=Qgy1fXpAZIQ0B_w04JAsIz6v1vbpPRbdTdE7IKMeC7Qm9fSHvp7lMUDmrf3nQZa2NnNDbHUT9itLVUayRcTbtDZYgmRgBY3g6JaNwLBMt32HBdu5_3XJ2TNf-VxqsyuqZEeJsQHiAcHNdK5qfCOaq4EViJNklNt-6lRoVqqqf4oYATAD4yeW9Ls84pRhm6nz89wVNP_HgoqTVi8PO_g8l9UIQyjMJytNvrnIgyFG8C5ox6WH2TK38m-5tHufIhYclOp8b8T4bCTSywg9Wx_MM0Tu8OwZJVI8uWXTf1zy_nNFwAuNkfnLk5RYe_HlXErvQqDNFgyqBuT-4Hh45sC0imnb3auf_oDC5Rtb1I6cgoa89-N2SHszIRYh4lv7mrJktwcRgOY7PrgrbRHGw8m8hrWpmajRTvib598oKCETSH7f8m2fIjs4tPL9BSb7TQzpQDlw1rhXw3egI5IQVYsgCJuF7DGYwSPKRaCzcnaSWeocz_4SzQ22Hd4B4TkrrkbwRtqUy6GOWMf7ZjxT9_oOkgm_BXW4EJ-rnN7CJ6bAQnDBnPi4bjUIbvumqkgwe1a1Bl_qAcXyUiEcwYVbvZMDw2dds2LlVjrEj5O-rvT6OcGe8udg0UNrdhN93nprj8xhZmDr28YCuywOMVLasW4epMHBzkaZdq-G2DWTHqVxav4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت شبکۀ برق شهرهای مورد حمله از زبان روابط‌عمومی وزارت نیرو
🔹
مردم با مدیریت مصرف برق، به برق‌رسانی پایدار به جنوب کشور کمک کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/671939" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671938">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای پی‌درپی در بندرلنگه
🔹
بامداد جمعه، صدای چندین انفجار در نقاطی از بندرلنگه شنیده شد که موجب نگرانی شهروندان این شهرستان شد.
🔹
تاکنون جزئیات رسمی درباره علت وقوع آن، محل دقیق حادثه و احتمال خسارات یا تلفات احتمالی منتشر نشده است./ مهر…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/671938" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671937">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قطع برق نقاطی از کیش ناشی از مشکل پست برق است  استانداری هرمزگان:
🔹
در جزیرۀ کیش یک پست برق با مشکل مواجه شده است و باعث قطع برق یک منطقه کوچک شده که به‌زودی وصل می‌شود.
🔹
حمله‌ای به جزیرۀ کیش صورت نگرفته و برق دیگر مناطق کیش پایدار و مشکلی در این زمینه وجود…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/671937" target="_blank">📅 01:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
معاون استاندار: بوشهر مجدد مورد حمله دشمن قرار گرفت  استانداری بوشهر:
🔹
دقایقی پیش برای دومین بار متوالی در چند ساعت گذشته، شهر بوشهر مورد هجوم دشمن آمریکایی قرار گرفت.
🔹
ابعاد و جزئیات بیشتر این حادثه همچنان در دست بررسی بوده و در صورت نیاز به طور مجدد اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/671936" target="_blank">📅 01:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671935">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اربیل عراق در تاریکی فرو رفت
🔹
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/671935" target="_blank">📅 01:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671934">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وقوع چندین انفجار در کویت
🔹
منابع محلی از شنیده شدن صدای چندین انفجار در کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/671934" target="_blank">📅 01:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671933">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1VeUIk3GBuF1XTELcpZKMV-Qmae7AtjCJhR5uKIngSd0UXkItT3wnlJTnFz_8ecW3Wxg9HcOgWy_jbiu9vah8gStZsSaA_zeVWSqcG10XmV0bIIsjj7rMo-bVqEsK0yIOGBGK5cl-OeCXo7yp8Z9U-dv5UPa7Xe13qulMPn4pvqwVFwWnXt9yXZshsnJFB2mVAf6lDMvPaGBdpzQeY0f9PlYGvmwSUk25yJNgUPY2q0OlX0k8f3mbnWabL5sf1r_2Wrb6dsElXEGazxjVyzY27tAbjrL4PilgAn2eQIhHjApIDYNBsa0lBXhwFAe5xFiMY36C6PFPIrdFYrVs2IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اربیل عراق در تاریکی فرو رفت
🔹
بر اساس گزارش‌های اولیه، برق در بخش عمده‌ای از شهرستان‌ها و نواحی استان اربیل اقلیم کردستان عراق به‌طور کامل قطع شده و هم‌زمان پرواز جنگنده‌های آمریکایی بر فراز این منطقه ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/671933" target="_blank">📅 01:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671932">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای پی‌درپی در بندرلنگه
🔹
بامداد جمعه، صدای چندین انفجار در نقاطی از بندرلنگه شنیده شد که موجب نگرانی شهروندان این شهرستان شد.
🔹
تاکنون جزئیات رسمی درباره علت وقوع آن، محل دقیق حادثه و احتمال خسارات یا تلفات احتمالی منتشر نشده است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/671932" target="_blank">📅 01:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671931">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
گزارش زنده از فرودگاه ایرانشهر پس از حملۀ دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671931" target="_blank">📅 01:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671930">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfbc72467.mp4?token=mIpR_x0fVNr001YTbd1rPkvb2Y9i71dRBQACWhUJaxhabjdFFH0n0WbTRsdkO978uZVusRUUwitnvMXTHkdEyJ7fs31R50LokpNeHb0uPSw-jlHFIzh1PsqugVfdX1Lq5U9fMTOVEMvzeu6dFrNb4ktyC1wxP8y4qeKDnE28eFAbA6GJPIzTCcCDY-2P3LsfXr4mgm56z9K1kqvlkxp99fVFoCqzq1aE1bWYyq4K68g7lP95_PA_IlirDu8pF-d2J4XFL8zBn0OENqWL5E6x0CNMUlIznGzf_HD2e9h214nXVOvI3du-O64CJl8aNtffM765EOw5t0k5LDJlzas8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfbc72467.mp4?token=mIpR_x0fVNr001YTbd1rPkvb2Y9i71dRBQACWhUJaxhabjdFFH0n0WbTRsdkO978uZVusRUUwitnvMXTHkdEyJ7fs31R50LokpNeHb0uPSw-jlHFIzh1PsqugVfdX1Lq5U9fMTOVEMvzeu6dFrNb4ktyC1wxP8y4qeKDnE28eFAbA6GJPIzTCcCDY-2P3LsfXr4mgm56z9K1kqvlkxp99fVFoCqzq1aE1bWYyq4K68g7lP95_PA_IlirDu8pF-d2J4XFL8zBn0OENqWL5E6x0CNMUlIznGzf_HD2e9h214nXVOvI3du-O64CJl8aNtffM765EOw5t0k5LDJlzas8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلی آخر را به دشمن بزنید
شهید حاج قاسم سلیمانی:
🔹
چه غیرتی می‌تواند کنار زن و بچه‌اش بنشیند و بگوید به من چه! اهواز را بمباران می‌کنند که بکنند؟ نه این مرام ما نیست. این دشمن سیلی می‌خواهد؛ امام(ره) فرمودند سیلی آخر را به دشمن بزنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/671930" target="_blank">📅 01:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671929">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فارس: حملۀ هوایی دشمن آمریکایی به بوشهر
🔹
حوالی ساعت ۱ بامداد، بوشهر هدف حملات هوایی دشمن قرار گرفت. @AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/671929" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تکذیب حمله امشب آمریکا به کیش  حسین احمدنژاد، مدیر روابط عمومی و امور بین‌الملل سازمان منطقه آزاد کیش:
🔹
امشب تا این لحظه هیچ‌گونه حمله‌ای از سوی آمریکا به جزیره کیش صورت نگرفته است.
🔹
وضعیت شبکه برق کیش کاملاً پایدار است و تمامی خدمات زیرساختی بدون اختلال…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/671928" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671927">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=egRhFF4FN_W-uJa8wH0zhhf98xha7J-paTTLS62HELP7AWGruIwdlI7KXQ7Tx5hf7TcPx5YlvPCiKtm2-KLkLfyAibsWpn0DpZu_kWzFRXzt8uA94e5YY5dtid6JEd1X583NQsjkp7ofCEO2II1em8e6L8m_xPOnzjdVA2zGMh6OS6mBs_S0C3TcPF58hyIb3TtrtdiitN1fdeVrTeZqNliGVADRuF8TFg_SxJPEOeTlkeHsC_9v0QeyAuxzFhO4eMQsEKWFm1R4Qkb5ySirOXUTYyJ06VXqm00beY_KafzBMoHEu9g1lJrDt-4Sq7JaKKR-InehJ5DrSNKBX-SHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40e8f652c.mp4?token=egRhFF4FN_W-uJa8wH0zhhf98xha7J-paTTLS62HELP7AWGruIwdlI7KXQ7Tx5hf7TcPx5YlvPCiKtm2-KLkLfyAibsWpn0DpZu_kWzFRXzt8uA94e5YY5dtid6JEd1X583NQsjkp7ofCEO2II1em8e6L8m_xPOnzjdVA2zGMh6OS6mBs_S0C3TcPF58hyIb3TtrtdiitN1fdeVrTeZqNliGVADRuF8TFg_SxJPEOeTlkeHsC_9v0QeyAuxzFhO4eMQsEKWFm1R4Qkb5ySirOXUTYyJ06VXqm00beY_KafzBMoHEu9g1lJrDt-4Sq7JaKKR-InehJ5DrSNKBX-SHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زنده از فرودگاه ایرانشهر پس از حملۀ دشمن آمریکایی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/671927" target="_blank">📅 01:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
حملۀ دشمن آمریکایی به یکی از مناطق ویسیان در لرستان
معاون استانداری لرستان:
🔹
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی را مورد حمله قرار داد.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/671926" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxV58mFURiH4ETvVm9AqrzqhLPRjckZIxEzWnv3Ir6lnWJAZw5ayPsWqqFc_1Q546Nlrm_KmIL-nEEy8aS_3qUZ5n8NL4k-HH2Vxhmap7264VfSyJBivSgElNeYnEcjI9Re-R8YVWuat2WBDOLamrGImoAwfMiXRdaP4jXCGtk_9-HsA24Z-Az4PuBICGrCNAEBeHDXlipnPrcncIFh1A9otgb0ZAHWq4v5lFwEnNpEqraKkQKEOUGQYTDRGmFasvu2qiWWEgmsaYhpoe0VNs-9WnuGwauqija2GmbGalu5L2-6Ysoeoct55dfLCKNjm8w0Mwg6I7t5p8KqPIYGY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب_ماندگار از شهیدان حاج قاسم سلیمانی، سیدحسن نصرالله و رهبر شهید انقلاب اسلامی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/671925" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وقوع چند انفجار در بوشهر
🔹
صدای چند انفجار در نقاطی از بوشهر شنیده شد.
🔹
هنوز اظهار نظر رسمی در این زمینه صورت نگرفته است./مهر  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/671924" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
برق مناطقی از کیش قطع شد  استانداری هرمزگان:
🔹
در پی حملات امشب آمریکا در جزیره کیش یک پست برق مشکل پیدا کرد و برق یک منطقه کوچک قطع شد که به زودی وارد مدار خواهد شد. اوضاع اکنون در کیش پایدار بوده و مشکلی وجود ندارد./ تسنیم  #اخبار_هرمزگان در فضای مجازی…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/671923" target="_blank">📅 01:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80f301402.mp4?token=Zp6eKeyVxsMkhk9EIhuinS1Ae2a5N3UJGJ-05bYRvc6-K5i6L4pOO3yZP86QCQ3DGlFXPS2BofCVjfjLoNLbsS9SjKOMn_MVkaFrr2Xh6Ez15iuy3TiU50agHqQ96ps9kBRI2Pv8aisgjD7MIcwRQk8eejO8nD6IYCzUDWpn0GyPvCzyYg4kFrC8kt11mWG5-yZuhB0-tbRAPwj9LRGs7Ka-HE4X_3t5M93Lcm0In_jmDWHgYcPHeoAzsAPImGZJb0NmsudiJ2QrAf6kHS3LUru2gGlqacJFFzYJv9hq1Jl--IhasV5BaszLMLsvOObHGA4KM6iQDbzc-qzvPjP0cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80f301402.mp4?token=Zp6eKeyVxsMkhk9EIhuinS1Ae2a5N3UJGJ-05bYRvc6-K5i6L4pOO3yZP86QCQ3DGlFXPS2BofCVjfjLoNLbsS9SjKOMn_MVkaFrr2Xh6Ez15iuy3TiU50agHqQ96ps9kBRI2Pv8aisgjD7MIcwRQk8eejO8nD6IYCzUDWpn0GyPvCzyYg4kFrC8kt11mWG5-yZuhB0-tbRAPwj9LRGs7Ka-HE4X_3t5M93Lcm0In_jmDWHgYcPHeoAzsAPImGZJb0NmsudiJ2QrAf6kHS3LUru2gGlqacJFFzYJv9hq1Jl--IhasV5BaszLMLsvOObHGA4KM6iQDbzc-qzvPjP0cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا مدعی تصرف یک شناور ایرانی شد   فرماندهی مرکزی ایالات متحده در خاورمیانه ادعا کرد:
🔹
نیروهای ما برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران، سوار یک کشتی شدند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/671922" target="_blank">📅 01:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e6e08f27.mp4?token=WBEhLVeWbXz_VwiTfx3XoFBgOzwsvOAbfn78dEIVsnVnZNvFZ6lV0v5KYE-KkhP9QIM_PLlUwTr7coP26xPqK2_4atyEDayPEty8pRb2e3o-eZtJ9RCZZPNG7zttk_jkYwLJ2dgrhReC3I5nQMTsx4Q2RVsxYW0O9SWhJRaZVoyVF2klBr9X6nzy00mmk4zHwdFxl_ogbQc_2I1KgXjmgEBk-UlZOaOmTMtWN7B_HrEOLLTHtMJYotXZccjc5_2mH57s452hCQyFSVLQQQJ0HGbIAVMgvYJIP7p_v8spGfTvNnDHCjwlaSZuQ__uXtOOO6htQy7-d_P1tKQqbtA8HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e6e08f27.mp4?token=WBEhLVeWbXz_VwiTfx3XoFBgOzwsvOAbfn78dEIVsnVnZNvFZ6lV0v5KYE-KkhP9QIM_PLlUwTr7coP26xPqK2_4atyEDayPEty8pRb2e3o-eZtJ9RCZZPNG7zttk_jkYwLJ2dgrhReC3I5nQMTsx4Q2RVsxYW0O9SWhJRaZVoyVF2klBr9X6nzy00mmk4zHwdFxl_ogbQc_2I1KgXjmgEBk-UlZOaOmTMtWN7B_HrEOLLTHtMJYotXZccjc5_2mH57s452hCQyFSVLQQQJ0HGbIAVMgvYJIP7p_v8spGfTvNnDHCjwlaSZuQ__uXtOOO6htQy7-d_P1tKQqbtA8HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی بزرگی در یکی از پایگاه‌های آمریکایی در خاک کویت، نزدیک مرز عراق را فرا گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/671921" target="_blank">📅 01:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
وقوع چند انفجار در بوشهر
🔹
صدای چند انفجار در نقاطی از بوشهر شنیده شد.
🔹
هنوز اظهار نظر رسمی در این زمینه صورت نگرفته است./مهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/671920" target="_blank">📅 01:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ارتش تروریست آمریکا مدعی تصرف یک شناور ایرانی شد
فرماندهی مرکزی ایالات متحده در خاورمیانه ادعا کرد:
🔹
نیروهای ما برای اطمینان از رعایت کامل محاصره دریایی مداوم علیه ایران، سوار یک کشتی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/671919" target="_blank">📅 01:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
منابع عراقی: یک پهپاد ایرانی، سکوی پرتاب موشک‌های آمریکایی را در اربیل هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/671918" target="_blank">📅 01:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b70A96d3umfztnhXcbMZf2A-ePUujg4fXs13H6BAto-aMihpsKHNhtA9-GM_ijgBjjYxOW7lbk30yNugUanHMvwv6Q9dUnhPfghZoFCvDzKqQtzRIenK7ZKcCh1_k1w5R9iEwmTbyszrfVziXHknMR_8yYbsYN6X5FCYi9-OHuYMc0VVEree33v-w-Bma6Oru-lAlrVwiVFqzZBr9VCDGHTY3SYF6ODGbBliXSkEBBe-zbPh2B2JMK6QObKnavJ4wvPZr7jTB3cF24658zVsS9wgH42F11n5__jVWyLqW-h3dIROunqdaZZj4Llv0gPJGUxeDoEOOXafJtwBybqOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز پس از حمله آمریکا/ چرا این پل مهم است؟ + وضعیت پل‌های هدف قرار گرفته شده در حملات امشب و مختصات آن‌ها
ببینید و بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230905</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/671917" target="_blank">📅 01:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
برق مناطقی از کیش قطع شد
استانداری هرمزگان:
🔹
در پی حملات امشب آمریکا در جزیره کیش یک پست برق مشکل پیدا کرد و برق یک منطقه کوچک قطع شد که به زودی وارد مدار خواهد شد. اوضاع اکنون در کیش پایدار بوده و مشکلی وجود ندارد./ تسنیم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/671916" target="_blank">📅 01:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671914">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_a6mFnHNxpq3eRClzs9_waLtA3Kewg_vrywFD-KbQM2EdEQOEfOrQlEyqU2hkzg18Opv6AswWpNUmPtlG7v8Kkf62Fn46p6RwbJMzZfpuGG5MsbNuEKLs_PpFUQEV9eVYHkbEwpi2O-KvX05TD3uMg2M0w-nEvVnxN_msO3VkMpF7fbIsLa8hiCRcmYtA4SEmpFHTmtvePp0tRG84ySgDRQ-pasijxbkz5RkLUCkXEfLB534SRuSKkOgBBJ_eUUJh_IQU2zj8PqiBDwEkQXCXTE6Z8c1p258kQ0E4J9SHlOyiBUPO2tpsecmBfshRku0JymGmELtwhxiPLKel3iSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/671914" target="_blank">📅 01:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671913">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/671913" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671912">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4GjHCJzNsolHAUN7_DxvH0VuCf7T7U29iTzJzd9fS8oFdvbtS6QxgGo_nkUhPfRNFKMnw6boCQ_j8qYMhuvgPBiGtnaa55Y33t11F2OdxlxT8cWJPMq-hoc5o8OXo0XBC4jNhEkwgGl-LWIdPofJ1LBFu9ZDvBOAqpOldFnQ45TXjm82ZJe0nzctBo3h0da583qAWxhYOX_matAbDV6ZMmxCPByp1u3dUQHi5Z1Q07Md1k-zzDovHvQRaG5d3O4fdK4txzSCj4FAgBBM8enJyuKpfFuO_uqsTFAndASdBUnleJ7xM5r12dS085B2sqQaKqYjUBWGm_zsfW55QtlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین تصاویر منتشر شده توسط منابع محلی از حمله دشمن آمریکایی به محور بندرعباس–لار  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/671912" target="_blank">📅 00:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
حملات آمریکا به زیرساخت‌های جنوب ایران: پُل، راه‌آهن، تاسیسات برق بندرعباس و فرودگاه ایرانشهر هدف قرار داده شد
👇
khabarfoori.com/fa/tiny/news-3230849
🔹
ایران امروز به کدام کشورها حمله کرد؟
👇
khabarfoori.com/fa/tiny/news-3230734
🔹
ایران با این روش جنگی بزرگترین دشمنانش را شکست داد
👇
khabarfoori.com/fa/tiny/news-3230840
🔹
علیرضا فغانی؛ روایت صعود به قله داوری جهان | از قضاوت فینال المپیک تا سوت بزرگ‌ترین بازی فوتبال
👇
khabarfoori.com/fa/tiny/news-3230845
🔹
همه‌چیز درباره قطع بی‌برنامه برق و جدول خاموشی
👇
khabarfoori.com/fa/tiny/news-3230774
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/671911" target="_blank">📅 00:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11af7931.mp4?token=M16C8wbbUt29vThvbGclPiJPUPqbdGhtRWqAISfDWPrlZxqSUQ5zjtZVrVQR2fVRTolI_AEagpj-098B3QVjApkeoNDzu3FY_Sn3MljfID29oLiJeTktIsWMd0uq2rIWTFbMbxYKOpuG1Vpm8mrLhrRfC5kNwKkj3IC6WE3MWAhcLCucFD1gPIsrCNqOjvpzYG62hzmRGu7C_I5AKVvnN8YvVn6IwxyNqZGrZXLuYVxhStmkZrgoTarcusrXmx51tj96LSyUBHVVO47VhTGel4PjHWiYOFdrls8oto0qu5ZmcsWQJYzzpQ66aL65kKJGeR8YscMw_B2cyU1WYy6ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11af7931.mp4?token=M16C8wbbUt29vThvbGclPiJPUPqbdGhtRWqAISfDWPrlZxqSUQ5zjtZVrVQR2fVRTolI_AEagpj-098B3QVjApkeoNDzu3FY_Sn3MljfID29oLiJeTktIsWMd0uq2rIWTFbMbxYKOpuG1Vpm8mrLhrRfC5kNwKkj3IC6WE3MWAhcLCucFD1gPIsrCNqOjvpzYG62hzmRGu7C_I5AKVvnN8YvVn6IwxyNqZGrZXLuYVxhStmkZrgoTarcusrXmx51tj96LSyUBHVVO47VhTGel4PjHWiYOFdrls8oto0qu5ZmcsWQJYzzpQ66aL65kKJGeR8YscMw_B2cyU1WYy6ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی از شنیده شدن صدای انفجارهای بسیار قوی در کویت و شنیده شدن آن از بصره خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/671910" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671909">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند./  باشگاه خبرنگاران جوان   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/671909" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671908">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rth3pAvzy62x2fi5tV5Ff8ytRzA1JSR1IXPXlaZAzdsGU95MlIz46uqLc57czBgGofaCgkHnehd8ShBoeKqczEjAN1oaxLTz9oIrxde25mQ5o1E7tVdotKcutUmiuIC8K13dWInTvwq4RhKLSk7K0qD96yevK2OSyi1RSCV_2jfaprGZq-G2ZLIxmABnFgkup0IG2oSvTpRz8JhwvM9N8-Y-Le11Yvbb2JuKNVjxa2JK31cHL7jW-cxDD0rVnu2gaXHwdtIB8K0kMzC-6ELNgygGXwALdky9qkURpLGOMWPqgxLVL8VYG956FbvAtUN6a3oJoRTI3_Jjz_TFV5D44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام کد اضطراری اف-۳۵ بر فراز امارات
🔹
‏یک جت جنگنده اف-۳۵ متعلق به نیروی هوایی آمریکا چند دقیقه پیش، یک سیگنال اضطراری عمومی (۷۷۰۰) را در حریم هوایی امارات ارسال کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/671908" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
