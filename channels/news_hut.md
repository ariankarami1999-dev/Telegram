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
<img src="https://cdn4.telesco.pe/file/LienQdsnIEOBD34zlNN7AF5XR2I0bVQIfoTgnLx1Ve3Hl127ma6K9Xs9vCJNZEutkQuwzignQpdpMuqemmvud4IJdNmkyecKJ70fgV3vH3PZ008UOU5gGszotkFN--ZAZaR4twhvZTaXtkoZlddr8O3jmE5CKhWPOR79hUU_E6gWyHvExpSv7V3DuY6JzW0cldtS0HU4jcPaRciZ-Zkzll92Fl8-2Wf-lAn8NhFEh9x0mSXuBZnL3iT3KnT-NdC8tFUyl7GG7wk-Iu-iEoo_lgUOw5TlZBx7WHs48tvncXfrE5SfV7Sauo5jJGQXbgMvx5dEQhIhZRoAfum8zRkfNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 109K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 11:03:22</div>
<hr>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=l4dTAJfhQybP3i2Zyv7jdH2LCqton29PTGaOd9z2_xDSGI6DDOE9--LOcfF2ULasqZnNspe58fSbH4LtbYPuftABpLCakjB7Jp3ZAYxpCwtbdbLg208YJWx7Ms6xBTwFXpUN4UaxI5a-b7HL2Dm-rGObbXJMUTxX4pX02Umxh86MT-k9iY2XvdXYn8A8j4BDSKCWdEBgsYqrPRVTRrxCII8rifNwcl2hbG-_NBChGry-D7cvydQKWQSUXjI6zZAU_1HWz-IgZYrYAu5czyWhq3oz4nreI5U0qTBG_KoMsZLJvPyb2F34GPDp-BC3tu1pt9J0p3hC5AHkMAlFZQ5pTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=l4dTAJfhQybP3i2Zyv7jdH2LCqton29PTGaOd9z2_xDSGI6DDOE9--LOcfF2ULasqZnNspe58fSbH4LtbYPuftABpLCakjB7Jp3ZAYxpCwtbdbLg208YJWx7Ms6xBTwFXpUN4UaxI5a-b7HL2Dm-rGObbXJMUTxX4pX02Umxh86MT-k9iY2XvdXYn8A8j4BDSKCWdEBgsYqrPRVTRrxCII8rifNwcl2hbG-_NBChGry-D7cvydQKWQSUXjI6zZAU_1HWz-IgZYrYAu5czyWhq3oz4nreI5U0qTBG_KoMsZLJvPyb2F34GPDp-BC3tu1pt9J0p3hC5AHkMAlFZQ5pTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=M8BQDzaxOr6A4KapiV79BKl6CqBANJCn5hJws7kqIO94HQMN6bjrU-oyeQTSRRKWO32Xy0oR_rZC5ks1I5UGUJUl4-upMYEEO4dSKAyHPvJLyBtUCDal0ZOd2q41FEw7-P_X2wA1Tslf9OmRcE6pf25VlpBy2K4wUsfUaVmvtn7N0JUKNhQdrvkgZqFBN1MYb-9r6JCS6tpIVxKYWYYprem4vTvz-yAjyoD5hL-Tszhxf9lNY2_lZ1YD2jLotxmeX5oePG4vxs_Te9pUPwatkUOZOTlrYkPzq-Svx0o0odcUQToWCoyWGUfaR3ecLAKuCfwefXIy5okDJZjcrRMPGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=M8BQDzaxOr6A4KapiV79BKl6CqBANJCn5hJws7kqIO94HQMN6bjrU-oyeQTSRRKWO32Xy0oR_rZC5ks1I5UGUJUl4-upMYEEO4dSKAyHPvJLyBtUCDal0ZOd2q41FEw7-P_X2wA1Tslf9OmRcE6pf25VlpBy2K4wUsfUaVmvtn7N0JUKNhQdrvkgZqFBN1MYb-9r6JCS6tpIVxKYWYYprem4vTvz-yAjyoD5hL-Tszhxf9lNY2_lZ1YD2jLotxmeX5oePG4vxs_Te9pUPwatkUOZOTlrYkPzq-Svx0o0odcUQToWCoyWGUfaR3ecLAKuCfwefXIy5okDJZjcrRMPGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBgwnoR2pVSwXuwG1_7sRDK0F3EjMGNy-smuYjNvu5pyiK4TQ_RjXxJ5i15aGH-Fjj08xwuKL0n7RrJXbzdO-7ln30ipCoenaxfNiJmAIe9dlpVtyspXkJFUwZJFSXu8FUjzjCY1KlAUYHIU8XDMw4VUN_VPre80X9YyTV0-No3_A4YZ-84FTUCXlQWVGH1mh_U7f7GF_cuCVTJPROmf6o-dAlt4A-HCdCOp1OAeS792YjIbI_X-ycgE_MG5OGkQHmk7InOA79vF_9eJddLQkQk4AJ-ogdIYocEzLpXS5x2Azy5zv2yk-o79VRqBTwpMFbMMTAnsSMIQd2_beEhrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI4KODdw0np8bFpp2qTPkQ5BfRlSYaKDX_oYXwjOb8MHpVT0BkGxoj07X6kFxw5jgfeyQuK_OqsgS8L4IeNUFupIP_aP03LvtM7OGWvUVz81k4Bw53QjUgb4-hG8FywT_fW-PV0hDDGAouiWgtkst9-RLDqTyTUeeAoeOWjFnQFqew4nScoLEkFdv2VGhXiwi8FQAX_5OpJAdzeTA7oiWFLMP-cOFkOqRTxRRhQO4ceiT6VJZt6pXKjJ5MOQFW01_AoAZ1_Wdox72pV_4vM4HF9XxelgzuY_FGOuY8VH1VmuybtlNzWx_6IVpV5rvLCCxxaFIjJzU_Xm9AphgPueEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=XWVjf2dPapHfvDJya118UZqFKHDCzZBcUJZZ6nmJlXaDCSr01wktYjcfdSb2NDP64vwyYqPPK0SGh7NXWP2lwnPrbx5V6QDRkvS_V-dWDmirBpdRF09DvncB6mZt8CtVjpFJ56BkvvSoTIxiF-AxF63-WWNDhb7k1CC41-5yo_6DKlSuFO4PK46bhA5Sh3qWflNWceTj44GPns5xpEC1GYguHlmRXF00gNj2P0q3ayssNexRt5nB7hJWHPBZ3yfnms0cgbd2qIIVQ4g66b5gcXBgCoWrCDRVP-WYbXu6s3NgbI3nAh55_OqJ8iOJeJ5dXonhyFouTej3zbhysK2xHFKsoJXsOMb7ntw-L_DR7yjH9cyEpnmif24zKYLAmStIQ-8UB3zqHG5JNV-DJaP1u1TTKvm3QwKlaljKFqSYOy9W4XytgW47i_fNMPwq2hmTgxvuNeD8RovLxX0bIs2UjrSizwa-NFAHfZWnfLcTBdu3KcDd8nae9ILOi9FtYOwX13uQzIR55aezqYRqjGsVbobNPDlNQlMj32gv0EhRKvvYWCJbfQPZqWJcJF5a_mlfM0b_ldYgosfjVKjTlesL6Gbmcjse6mWvR-wYFUoAc5R6LA4EXthPMkeR5IP4YiyY750OvzWXZflYV-yUrKBP5204vnCbFeGkbG2i-_ItDlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=XWVjf2dPapHfvDJya118UZqFKHDCzZBcUJZZ6nmJlXaDCSr01wktYjcfdSb2NDP64vwyYqPPK0SGh7NXWP2lwnPrbx5V6QDRkvS_V-dWDmirBpdRF09DvncB6mZt8CtVjpFJ56BkvvSoTIxiF-AxF63-WWNDhb7k1CC41-5yo_6DKlSuFO4PK46bhA5Sh3qWflNWceTj44GPns5xpEC1GYguHlmRXF00gNj2P0q3ayssNexRt5nB7hJWHPBZ3yfnms0cgbd2qIIVQ4g66b5gcXBgCoWrCDRVP-WYbXu6s3NgbI3nAh55_OqJ8iOJeJ5dXonhyFouTej3zbhysK2xHFKsoJXsOMb7ntw-L_DR7yjH9cyEpnmif24zKYLAmStIQ-8UB3zqHG5JNV-DJaP1u1TTKvm3QwKlaljKFqSYOy9W4XytgW47i_fNMPwq2hmTgxvuNeD8RovLxX0bIs2UjrSizwa-NFAHfZWnfLcTBdu3KcDd8nae9ILOi9FtYOwX13uQzIR55aezqYRqjGsVbobNPDlNQlMj32gv0EhRKvvYWCJbfQPZqWJcJF5a_mlfM0b_ldYgosfjVKjTlesL6Gbmcjse6mWvR-wYFUoAc5R6LA4EXthPMkeR5IP4YiyY750OvzWXZflYV-yUrKBP5204vnCbFeGkbG2i-_ItDlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEo_jk_YzPIwW9VJA36CCG1whM4HDklxY2UnceDmV7xyZhNgjE3tkdVsPmsPDOz7eDy4jSVJpdcwqzebWc3ejz12E7WDWE_6wKpyNs88QJDWB8p4bUQUC6OuwdYYL2CzwTCuTowq3NC3JnJAKAm8FpI0kFQtewR54fLFAubqG-kMsx2usJHWAYVE5L7C6ECU5VLwbARZZnWODwL-7rQR958M4PP7qVppxgftrl99ZWAvEUwFLxLZqmOJKsseHQY7vJf64zQZofKPD1AJGdEw0wzU92m31a-MSXDr2n4ztBMgMbSAgXUa45wtfkh4pCg0erhsYE7j1ZKrn9tvWmGQhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_pB17JBreSLNDp78-YcPC5S-ZMrgnTJXx1a0bJ0MmLpSqobCMqgVppuqrrh05SX5Vw9jYndYjvskVCQTNLHP4JqXK0BgAqAFJrNoXN9ITXUECv9uaaFEiNs_X9wpUso9pER_-9EXFqo-cuAWMor_1TS-R87m61ToCHSUjiExGFwLDdrh1t6j5LGdyo1wW8ijTi2VrXMVAIAenT5ZJ-6L143qgL8NU-hNkZqTV6D6EX5CDFUMpDUfPP6ieBEicyi4CytfZtpNmxonUaNEDFCAVxgHejDohI2iArdU2fW_YChGui8swoSZK6OkqieUaNMSvBAuUkJn3BNeyFIDza-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=W6BQSa3kqjithhwRsJsxdWnbWGcXELts1LjAnlE-iAE5iWgg94Mr4yTB6L4OXp49wLLGOKa3ev700et3HFwkf3d4MPBpFHLVa-FGBU6TkkRM-2SHaIAov29uRDOtua5O7Ng4HpjzXouNFiD1sTdkgO_MqRm_3LGXA020UdeH8qHG1HKdOspESB-c9FFyeaw_rOBgA_AEs6jgIPBN1n26dc85QFpAhbXm22fPNjf6FbxvBz165GYET2VBdmZHqetWWwUB89xlQqmwPW4SoCvLRC5_URUGROSUl56bxupoKNg4suj6qgECYGI_rTf6vYM8o_nM3v3m1QGt9SQe5wVkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=W6BQSa3kqjithhwRsJsxdWnbWGcXELts1LjAnlE-iAE5iWgg94Mr4yTB6L4OXp49wLLGOKa3ev700et3HFwkf3d4MPBpFHLVa-FGBU6TkkRM-2SHaIAov29uRDOtua5O7Ng4HpjzXouNFiD1sTdkgO_MqRm_3LGXA020UdeH8qHG1HKdOspESB-c9FFyeaw_rOBgA_AEs6jgIPBN1n26dc85QFpAhbXm22fPNjf6FbxvBz165GYET2VBdmZHqetWWwUB89xlQqmwPW4SoCvLRC5_URUGROSUl56bxupoKNg4suj6qgECYGI_rTf6vYM8o_nM3v3m1QGt9SQe5wVkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=TXpnDMUGlslTBMSXberwThFq30XwvwRO3VVYVn4AHVBkoCbkP7jopMpVAtWja0RrmgNfIA5FFl4a4bJQkaG6n-Gzh_6IWiCjPcETMW7uCb2_paLgsmAZXgmdbuGkhoxF9RK0YqhLxz5mzM8quJv_25kMrq5kyzULmxgnnx-3H_N6-vscaMez1pTEfZkSmXOyFfun9zYP8MV4xTr6XDOA3-wyOK3CX2qcPuPoCL2r_AjBs4Do7w5DLrEhcBvIkJDM5ClzIz_ugVpnD4LmbAegYJVYEN9hXxC4NfzdUk5FGk8GaXaRZfJ5diDcSO1-ON_LejbjuZ1NJvt59gSmT-5bnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=TXpnDMUGlslTBMSXberwThFq30XwvwRO3VVYVn4AHVBkoCbkP7jopMpVAtWja0RrmgNfIA5FFl4a4bJQkaG6n-Gzh_6IWiCjPcETMW7uCb2_paLgsmAZXgmdbuGkhoxF9RK0YqhLxz5mzM8quJv_25kMrq5kyzULmxgnnx-3H_N6-vscaMez1pTEfZkSmXOyFfun9zYP8MV4xTr6XDOA3-wyOK3CX2qcPuPoCL2r_AjBs4Do7w5DLrEhcBvIkJDM5ClzIz_ugVpnD4LmbAegYJVYEN9hXxC4NfzdUk5FGk8GaXaRZfJ5diDcSO1-ON_LejbjuZ1NJvt59gSmT-5bnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=Lmum7MK4gVHw0k9n5MVrFnJBLXoEIkGanWEe1u0QE1PRSdZG0xisAswLs-B1VpGLepD3Hbh9lV3pxYMglMtyOq6A8jtvA6Vg8urvd5caxltL8X2LjkIN8OVjQCAvjVYV8_7qtRdoIv3-OoyhLG0oGt59wLkG6nVUYAThjQxtJvK2wJ6-u0NJeKwelhCWAaZMmy8H0E0zdvxklhBFmQeWyL5_Zu0cl241AM3wVRTyAggQO_VtIVmCT_ei33OaQzeidiBcD3FyM9JcbdfUP-U9fewYfLA0k8wADUxSJRomo3JgJyO83B9J6RyjoYJbXfBAV2DIonJ_lVuH2FxhEMD-FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qKYqgh1QM4KBwE4qlApLz3M4OKw2C2t_Qjju19fs-0q9RnP4tLn6H4ijm27QgVrj7hde1-n0rpctI8Y1rcrNJajY-RJBwrTks1ld-Mm86eX-mkToKkW6E421KcbFQWQDOCVgeOCNDjOZR7lwKkJGw-MVL1XzuEcwcmHhJe0yBx9kzSLdyg4gmzO6EEpMp9UAypnyuV_s1PMbXMsLL1S35bFxdseeEFf-oHHBraxQswyIMUesC9AYDHw0M42fR9SgvzqV1-cAkR4f03X3Wlyih-n5GNgNLruB_NERS4FyFOLSZeacYqvYnKUxjH4syFFM0TFTJTAvPO9USTAX7_yTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ehp-GWeYkLyLx81OyQMaKX1JxwcnZNZULO94GIIoPVb2OhWIvmQASvHmtIuND8d6BCw-h8MV7o3IeI5Yp4ZQz-ZHjgwpE80nt6947iZ0CUO7r1qDhHf4qLzw4Vw_-EoE9bU77VUd9twUkN79kKBqdx6mx4nZDnR9l0_3kiGVHHkM-4Az5x7Fh0QVZn2UUm2ZY0clWy_wQOVOzkCiYlWneuUSIIMvQnOZ1GnJKJy30_CzJkewmipH7FWJeNKddxW6aP8KlbiIDceC0lSvbE5KxvbTz0_P_tpV_8JnwhN-hP9f-yYonNHjg9oYm8N0S5PNHSfY0lXm5emuwTvd17wQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qu2XJKhCzdj-F9eu6LF-9FknqtYx5hw1ilL3hB5_6AQP2zqp1M6B-tS4fcWlOYnqGzSkZsHvKYUdMFTyZrYhvTWNzgFmTqYXRV5hpNJ_mhrvoGvBuZnn73xhu4lhyZWtYc6aEJugBMtEEzXpus-wCAPX4vLvgQBpkjA150AaGs4eoQuYuK7WcUe50YRfuoLbETj583AmO-8u-uRCwLb17SWkdilMPmVE6Oz1sf9S5K5PxBRdASSwj2XDID2uE1R3H5DAC4S6EWCx19aYrYgMbnF9J1fPjMOa6-wryN-bNFlxO8S9s_Tvb7_GI-e5W7oKKVMEeUUvhydXE0hw4sEXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-O0QuWigpruDFjh3UUzD-qk3DP-g3UFQl30MB5TxcBvfVo1cwuX_v7mzGLYxEjHm_S36zRfgRVnHlUhaxxhnFxsMpSyW8yS1e_6R74aAshLaWh8CVIB3mezowWo9NmCm1wVsvdiaUD5cIihW1SA8w-NMHDmwMcR51OJVdkb44fJbjnN_h7tvj3xnFSiSdploHAi4Dim-z_KT9jzTvHAUhGlK6n_s26tJal5OoMiI5hHBUfQmkX4_TI9p_c9xPLU3OLd8KUdWDmvfWAiWHe1KspSLxuDKEiQs09JJ8h1jLQdYoRDM4PxDjgpGRTjFhaFQiQgWyWgO_p6yPY-Vn2fjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=eYgvVlI6tzsDl-u6tIJMiOqQTZ2RsyCCs6mtYUnX2DfHCzz_N_P1S9FsEBMIAUVsjMkrXOAmDqFUzpI40q1OBPffvPwfKe_OW5PyIaPdznGcaWC_JaW9I73obiyJVfRFLaxZ9jVaoBb1VXpqKtWOlIdjEZVthq3wp5cYMoGWWmYiwTma4aFaN1c4nphpWbn9KTH9dahg4H-8kFmNRfk74j6p7UHLWNGLuSsSI9UtTId484XPzRgbarA7H1Wc4LYpGu1UWtZZZbIeFKmopJNjD3AiGLL1IHqbUWMg4FRX4ERPnUvYY1WvX0Tl4939vB6jgGwQpeBkWNPmXjbYBuZYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOQYGUII_C8KrED11cqdF92WAhDC3304dl8vZcFJz565oDSfE7FLf149WCJCI_ppJfYGEUGqZ0yN55638UQ3RavFm3mPTA-Q7fllyhJydQ7H5T8QdGG3uoKoAYw4dpUitW_-vNHz681b2LrAGxFksgdhj07xk6GvSqzmGfjQGhoLRI6mjLfGaTPV3b4woXNTMRD5qF1OF05SDOdac8o-wrtbX-WYxsF_I39OaZ71V_XX9S7cyyeAQgvZIIYMe8uqYeNuJGXmcxIXCTkshy1RprHVvFD5J0m8Sjtw6IYQPLitjzAyB4OXbu8KnKEN9UCy2ok8H2O5fFlczYMzTxXTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYiGxKxeuH8giuR2sBPwQl_-ODryehO_bVq1HnFFrf5zA3vZsee1B2pV_WtLzOHH6DZOgFSrFQDqGLJonMoqDYEvlkxRskVo5lmErHDAjK8ZgsRXJe3eBIoYD_coLJ584ah5Bj0ZcJM95hg3cQvA9w4FWlkXmXsWb3JfP19Q56Sm-zyAUb4xLDZGtZA1Rwd6_4SUNaLLCM8cB81hQqvzh9nbcs4B0jdPfjx1TH0_kkBj9zNrsX42ixGJcxn8SF29bX4oHwr_PdI5Yj4ivJmJLY2QJw6wxReyd5Kf2os9xHMRYpHmbK8Y8lkqgUoBncBURLLKCmYtd2LuAdo1CFQRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=QnjeGk4JTy6kYDXd1kQ6jW2VXtQ5ZiPf3-d4JA-ILSVv-HHzsLmj4oZybtCKrMbtVG4zHpiSVVsq-Mz7DFzqi7fPElEORabgJCTVJBpcuCjrnyGpMoNwRkKaTIgxLgmZFkjNgotQhgbVTPNWgqUjR20dACjLiFqwbruChsRbLgKMTbeMNp_gZaB22-s61nk3P__JNWDRGYgtWUKbMyqJ3JA2sSpggjcdClz-9VDAhBL7Gy-YkNMjFJY9_f0Adz-AvhguJwO9_zOQetDSGrJu7YlxAEPa5bbW_l514ZLhsjSL_wQaubPgKQszZHqoANNcjfAFbg3XtHeDK582dVaNbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSWR8pwup2w9baJFdEILpUSt6j0G9gYMhCIoRIq6nxAYTNwQQuwtuWgV5A9zoi4EibyMMV5tC0NoM_HoO1T3BTCE0-E2mrYrtXHh1cKShWUbAKIVI5JRumpmrH_jvFFHawLyouDIl_8QUt0_99rJxbTiJx4E89yG_zq2NKO0RQgs15RDyhIV6ncZLQyyebrVOGyW7jIoQkHT8EZZ7K2iV8XN2RKAYkF087G0jUlS3nA7c4t25_Yk0FZte8eVU-lXfXsOqBVdgZCGMcb0wcKC1R0u1_KsVrrkUbaF8BnIjj1Ck59GUGUulmKd60d9bcNzW3Pmn-lgykuciKKFE7csjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=rJ8ws2h0OoqP9hw5a8cfmVA2H8E7aVLVfGm-ByV7h7QgfWXXGGz2-dPb935EKIU64SQ-EUyWi_QkYFWmS_ek63KR-5SB3vdPvRrfDwOWXt4wNf1d8w3jF0FVb8aYV44V7T0uGp1VUIJr6MrLvYWZ9TSbJREDfdAGpZd-ByYKn4vVfMrI4oo7_j_ommMe5NFEpU6ln2oaD2-7ce5W-R11-t0dq1X-ymv9wYMmGb1LDE_hrSgowbFTuJee4bE7T9XD_sVZmv8Ihv2oc5lvIBw8uHB3yeRKkLU3g20VNhy42TiEJfw4wdyQsq4XGTE5pDCApooJCgqrToEv9L2WEGmMH3Qns49LrHnQcXDhfOo8B8qWBmQqZHZ0rO8lS4xaEzmu1wKjTX1nqZCYZ12Vp-UXxskvFJ12uNBwwxQjOclYcEakbAgG-zcnokgu07Ej0c9ubVoOasSwrpuvkom3uU8dqZRE3dfTvccVnHtfY3DP0ujps5IoFTLzP5EORfOuU4t6yxWFNdkfPdmeejEHx6Cf3vjj-csIAPlqUh2YJBp2ITmgW2Vz1eyVvHOv3csIi9vovuIgCf3lOyU2aycZ4FvwUg343lZgCyjDanHlZ7JenqM8nV_PpnQlwIV-F4r2ATMEtX9JQdYX5_JvisiDVHYwxFKwLpInwoIRAkRmRkP0_oo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=usW4mDcrWQvbNLvtbFC4O7HJPK8f_8Zez61nj9SOu86gBSqxaXIuAqzNVYDMQrN6QNu6A_osDqjP2Yz8_f-S0llKC-asV0KZJiF3PPRDFGUVMiH3E7W97xL1V_2vszV8vutiSDiB5ykT6aIhCNst0K2M10yzv73YwlTNVjZDbyGAENhw6bop6PMdtEqJjf9Utw3m0Uu5hd7L8ReZupTW6N8_ljL3Uz43X1UR5JtY2quADL8hVR1MgLa4v2tsFCYpOkio03PZCyz9dMTm4JNRmNKrK1pyVeSWz722KoCcxffDsp8-ixDWgXSdQAYmnWbJIxOw4t5oEJ3APGRA9wq1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=qPahvCUSqjpooTMom5B-FdEFqW-2gevF5hGwt5i9auiM_447iQd562pDuIMq53LIS4oYCCL42IHbwg1zLxkn4PxBp95vPP0_xkdNmrX9pQToAQ9hqNAWZO96WnCdLktANXuqkO8QD6pUua7dWrnUbhLMxddogJ8FkFhWN9kt24alAw_tZQRTW2KvgdvLfX3g4hlvG99Mss0o1sEEipbHsCAO-Ot3KJczq0MbtpNBcyajlth1eE26MwQ39za6aDzvWXZPGsFY0RqM6Gi4xFdOVVyO73oFnneP0LfBPCRuR0_zqBPMr0qns9CJPB6Ccr4FlA_uQaKo1sgE3ELTzZ3IZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=tDdP_Ekrkqw_9ucqT2oYNN_TjH_XExS5v-Pj_FPvj9ghYm76aBUddVk40SvnWLZ0WnlUMyyWgfPhU7l7Z9DxmdoUjGXT6lVi1WbOC6TK1A8IT0a543GAunce2CW-74aPD8mZfkW8f7H7U3sSeBo6p-pu7rPo1322eVq5bwwLFkKNAh16ln32m4jOz-GxPmYvqTzz1yQXDjNG_qMzMgvePFkyOldu4D4NVZXW5ulciySVTIcShpaEo5fMqVgZNLmKwoSEWmkEaXInuL3A27PfIOxWGKJpu1H7GP5hvIX3dIUrtAInDEYd_Y1tl_7XrzRumfbWNUAJTuVvGyxLrG1T1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=iUGpLS3Znua01q6C3F759PaNJi2j22scl3AXPURS9GuMp5AAAovk1dKtJpbdR-Qi805jg8s_Aoi3OO-vvvekd3JyL_rMDV28KcVuaVjydNM6CAfBCopA4SnzOaG8H-XPZ_D7iSUCIIYeipzl0PLg6fOkcDduX9BqO1frLXBBD40qyyQVrdKSIwzOI_NYP6mUzamS8bGGVs70Nvc13Wv0_2uLzEMkELPLMVbFIXa84ZjZ4WDT_Ph8lszAb4QaLacAKpFgo3I8XgOWjRIRyBu-OUbS7gqI8W3ISxy7v7xZdfAlpJAc6u7Sg_M2hmOXL4HD7JvZBzAadpcl9tborzb4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiHwUTmtx9wTHrTXfmwoVM-NkAhi2hS1c-b74w_bwjzi1NuGBmeaFtcykvJlD29UHCQmQJ3h4bK09lb0Q1eB5DDbZDL6IN9kn4qZ7-vSxuQSwc75yYcdUxDjNASpZDWsdkgaOtVJkVqiztu9NbEyjo59uqfjsdjAj1hKO2_NsuchrU3Y_m-XfvpQxGp7NQuppAZnpO-VeySygRMEIwfrPq_M8URCEo3NU85zY2Sk8BHKkOrJHBDoCZM63EBOuFxTmgl-xgfOWG2zx0DdSqE3G-DEwu55q_opJHmKsmD06mCAVMYnVQK8EtdvX69CoO55B33IGtntr-TIRQDtpFcr4kgMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=O_-rAhY26j4zX4JpW2icL67x8tZ9rKtKB0NpI-Dltpqpc0cpD-VNAds2yBkYgP4PZmSy59CM2hYmUIOSc_5jeJDY5aV4SLLFQ2OfLQzOdWgflJhyryaYeLPMavc7ZGy1MJazIxlzGzM3StXuH_hRg-XZpLFkG4j6WLZ5kkG99iDtENYqIwj1yDtU2RgNzNz83eJ859JMAIhuu8Uu2Nm7KTV6u9yY4S8MNWRMYm_Hsr56zLFtya4mE2ngcNzgWndWqRrpZpo7osO9Sq5wh6bueQrKa6bnoB2osyJ65PyMNAaqO3jkJlWmr7RjjiKYeAd5aKrnmY9yReNjPQsx0qmWZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh77uiDscwS5cFtxaX2vW6VHB4BwhI3-BY_7Pcnv4MHZO8HO3YKOp8hj-RQblogz3TjPXUe4GO9LG36H2W_n1x_LUqULZmBwVkiJVuYEHDM6FCFw82xtjt5CSiRbZKHuLFxxcTLoznjdrMHRtgtaFtLPgPdp0R9_Tr9qkuPQJg2HWAih2EIhrnmA-RurdL6tVxz3M2R1LVGfNNDjujKanHIhKo5u5bcSTCpYowa5Om8K6DrgF24d9ZrW8c9_wbRMT_r8VRldq66MSzXj3aA8iZWMDaqkSZF5sqpXLRQz6m7fLJGWhjPy08QILLmJTzLBOJdIn4Ntktimx87AwltJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=nhn5xTtLIk7S8wQqVakpL0gX1Aggg_STFJUuij1h8toRkTvHep_AB_kGZd6Z_9cI2UtAi-m2kfFxTmjuicyPZhbgtdO7qeYi0QUOicJ_LPFe959c6IR9oMV1_sf1gnf3jsyCNBz9J3kBUMrRkdlV3dNn5szbtXAadRqEiildySJNTeNKWTYNcH9eozoREmpZg2vhtBjqP-rHs1rPVQGHnThmfyKWlqIVfAyFcWM_8sF9cRdGdUEFfPnk5hqA4hF3M2gzpAsIpNznIgwq1xRavgFGHQnuLlfwiGnGOkqzuY2iUdDZoX8AX1oKOs5vM47jbJltqQP6NX-AA-9tHjB_vogp9fHqruN92u6IGJsy-0ZSW1Ctb2LX1jhuIhiQFnqlNPjn2TRGvC_Q0gAxKyPo3jEYcCMxqt5zjtQ2BKg8tjvl0Rcs5vzrgNuVQ1d2OA6hR6Pd4SNLLqUSODhzAfKsEE9ulSWisrqGudvFYIUdMSpvdfv4CLXdrv_pSfs-C_P0aHrumXF_JuKdZrRk1RPr_Dmp7nkfNYLUX1nKbvbME0cbn7xr9eaBNKJntsuVjcEXP1OpJusbZj2q7bKHFTIr58bVEqqERhR8-PkqarbywjPB3fQVUIRJtuiaAVfIpsItjLAqXfnB_mKlWBTXQpwRHz6qOTWvvPrhyy8ViiLMMKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=HAQbzVITYPQPs90yV0PbL9NHxxZebMpzQxzZIwikWKa-lzKwvO_EpJnatr9K8_ptDgyp3oXLNGukxj72RlqvbsgjxLingXQOFAqDc-18JxdlXqHgvqhJvyf7eaEqIh9w-BWh5xzMawv1E6Wep4qrZZWlQZOsqNERuOtJN3InJuMBu6HOXYezkUAHVKkErcR_GnfGsg6MSBHxZtC-ZsZFHqoR0skZhinGWzyrDV687CzTxwXWR9Pr_rQ2cf1rgHi3wfIhyOHXyikpb98qEBuLGcfL28jkRn31NF3nWidALH5LtWt3cPdohhkZE8W5A3JxJFrMbZcxvy15KPPEJTVj_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=hLjvFzZZomqj2mGxGRckwqjyDO7bqxJdLJldP6fs2IXyGDhYVtfl5Vz0qlt1izm9QSIbOJo-OKHslNXvw5kc6QB2-DRvgT-jmAFXST4zpod8KxQLAMPWbNYZfFcQqmwVwVfmmssa1CJqgxvdmNbb8kSGnii8R1ZDrZ9cwi0A5pn8yIEcjYlQJ3HT4k7lQXxri8RrHBDstpIaG0PT3b0BcbMsfO3I3wNvY7inRFfUAXSC5GVrXpzC1QHi-xd6987SZbznuHSj1mh16cc0l_JIpA5GZ51f-xXB9UELfRIilf1-ptz2JxvPebEUVWY6FMs4MWM-dCpCHtg0qh0J8bKIIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=hLjvFzZZomqj2mGxGRckwqjyDO7bqxJdLJldP6fs2IXyGDhYVtfl5Vz0qlt1izm9QSIbOJo-OKHslNXvw5kc6QB2-DRvgT-jmAFXST4zpod8KxQLAMPWbNYZfFcQqmwVwVfmmssa1CJqgxvdmNbb8kSGnii8R1ZDrZ9cwi0A5pn8yIEcjYlQJ3HT4k7lQXxri8RrHBDstpIaG0PT3b0BcbMsfO3I3wNvY7inRFfUAXSC5GVrXpzC1QHi-xd6987SZbznuHSj1mh16cc0l_JIpA5GZ51f-xXB9UELfRIilf1-ptz2JxvPebEUVWY6FMs4MWM-dCpCHtg0qh0J8bKIIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=AXUUeMxVX8FCeWpMGk6tMYaLwo-GrAfRf-U9et-w7Ozm1jBX-EUNvjCOtUCTwbu89YeMqIieW8CujlJ-yBfRbgbrc6rSq0oO5U6QuqYxw1WN396IgOlX7fDgQARFGv44GOb_1PkLFAOUaX8XZ_8vpd8jA7PizprmEF8BY2VL-5JJ-5sGggL-sPRcqzDzfQbrlxaPEB8TgWnVaPnQqS1TCjb3qk3duK_1BV5vjkvcyjDs7Jx0HxG0gt7CHIRDmxM2zEPmf93VZ2UkLG9IVrNHZk998krN2R_YJ-uOz8SwO-r078GDicZytugC8gsFCD1ChkCijp9bri3CYkiYsyy6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsXG0WlGe3znJbIqCF_brXEoPVyBT2lzLNyxUd8gsnPJZ-cICprOAoYb7OJLvlyRKQQwQWDoIS90bf2z3vyUdKFI9_12q8FbYpFL4SV5Sha-N_Nd2yIzio5Y0WTE-wxmdfe9Qod5bGTG5iHotjVEV67DhPTx6x5euwub1XvY8RPGaXqGkbC0gjR0Ug1dHqzjYicNc1JCo20aF3_73H72cBJt_E2d8SxiKbaEyWmiaqnUZY4N9e2qZf09GOU-MIsgZRvlJUttZLAuXX1ut0xGL6e3_EXAggbPlCphKEjor4KwFN_AFmag-Vk1S5JnvhBpoBfd8WOe1bXS3vVoROriXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrDuqbNKLXhqc_lrNr75EoRL8zoozDnj40LIESNF1I3yOIGihs8UG_GOWHcmna531c8Dc7HZdc8xScUrJ15MthMrIRntZiVaOVhzV1RSdv-JC3k9aWKE1w5X6Bz33IDy5eCjITCxS7WlsjGhqRmoHNcBfnBhOw42Oe_ME8ltCc01MkNu7239lW1_MCWfpPdUF4buJyqlPM3amg5aqGK3diov9bpgnTJargefKsJv0Z4w5qoYNIOikCWIixFlhT4ROakV4cUbE-BbDy6TjJ2Fl3WOwK3vW95TujRHMDMZnzNl2UAIfOdTKVxxei8_suOrUOLn6mXF4PqOevaKOiWp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=e_a2TXjA5kputxgMo6ZOy7UcC4Q4xP86MGYwvXDggqKvyzN80ps0knTWG6EVW9AZKPK4bZP8gZgCU-aVNRpssg_0vp1lkeKpZ0t8TY-nvuDDIdf0YwP07l538-1taw9ixd8KEJ0uwZ1bjdyVJizM-CaGiP2Jk-R2mzW4hmHs3OmVUQ7MsdnuUt0NSx0kINI_cV2wpN95oq7NDR9QtbwF1uK9zkFdyTYhX_gijG8F5fU-cMxKh4cbGOjbA1cO7G4kB5f8yz0rigSdi8SeyVw_2X9xEaD1PlKTJPq4976EaUP97FRfawTNfFFde0cJg0JlVHaT_zw-p5JgOh6hdSS6Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=B3HDcmGZSr0Smlxx3GNAvwkhbNDNy05QeFuehhUiikNqRRjbkZXWhhXiCkoRPzOABCbVTxaOFcJ75zH9Ae0JIZgMZEkJAvMonDhMjEeyJRxGbSQSA8qs4P2GTOq6aSDnC_wx8tq-_S2gBpgOfeN8UtfaXP5tnWqLDck7nrW8q3ua4OCRVp4SGG4UYyk6SjVh7ao9qL7t2_cE5Yy6mRtbsA44SwO-w13-_CjCn3rB7dpzxbg5wBOWmE3f8C5oFopg5aDkoTZE5cB0DnzkzQTHzjQD9la4BtRX7y742rlYnVCXHQgJrKXaAMKkhbQ_SgUxshkxfvLAyXX_Lkt0mwFnAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=B3HDcmGZSr0Smlxx3GNAvwkhbNDNy05QeFuehhUiikNqRRjbkZXWhhXiCkoRPzOABCbVTxaOFcJ75zH9Ae0JIZgMZEkJAvMonDhMjEeyJRxGbSQSA8qs4P2GTOq6aSDnC_wx8tq-_S2gBpgOfeN8UtfaXP5tnWqLDck7nrW8q3ua4OCRVp4SGG4UYyk6SjVh7ao9qL7t2_cE5Yy6mRtbsA44SwO-w13-_CjCn3rB7dpzxbg5wBOWmE3f8C5oFopg5aDkoTZE5cB0DnzkzQTHzjQD9la4BtRX7y742rlYnVCXHQgJrKXaAMKkhbQ_SgUxshkxfvLAyXX_Lkt0mwFnAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=vdtuiYLxJxU9mdei4rYPHQ7DentLXaISUBUVrpePm5ZCDx_BczOS_kWWjrsDsDULQsnjb1tOH0hRUKm1j6PXDaogIGMw8UDJFFpHrmmARYRjsdNv7VrVcux2y3npOg6ow-VzdoaLsIfHoGu8TR1c69pDPJgTg_QoiWLFt69uF_QhQy67t8q-kjr9_h6FOcCyi3FBGIA6s6sE2esJQOqoa4FYPogOV8K4Jb_MY6EaV6VFchuOyPwEuPrd69rSvMwj-7DGvx3stnmDFwdcxuUFeCQj10g0hK6LRmtMdxhUcmSx7LH6bPIu6_ynP1O9Radt_7l3IYoOQYFDbewHnN2WOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=vdtuiYLxJxU9mdei4rYPHQ7DentLXaISUBUVrpePm5ZCDx_BczOS_kWWjrsDsDULQsnjb1tOH0hRUKm1j6PXDaogIGMw8UDJFFpHrmmARYRjsdNv7VrVcux2y3npOg6ow-VzdoaLsIfHoGu8TR1c69pDPJgTg_QoiWLFt69uF_QhQy67t8q-kjr9_h6FOcCyi3FBGIA6s6sE2esJQOqoa4FYPogOV8K4Jb_MY6EaV6VFchuOyPwEuPrd69rSvMwj-7DGvx3stnmDFwdcxuUFeCQj10g0hK6LRmtMdxhUcmSx7LH6bPIu6_ynP1O9Radt_7l3IYoOQYFDbewHnN2WOzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=VmE0URG4JALTxUTQGIv9NG75poImVd4Epun0NXkl0XK_Sgy4Qmps2P3n--O5rVnMJc8J-smGXf2QLvCl7_pULY4kN3dZLu25FWO8LPRJ2SS22nc5lLr6yPlg1-dIcKZ6FYGaMbvSsstoTbRAgbxgvoWnCNF21iHNmFyfXkvjluhDYJozb2vxSV7UvhYCwCkTAZSwZCuEx5BKMWGlPkD_kZBSp7vo2NI8G5RpvtpwgOp4SeeckYCYAzetqKV4cF1pRMC6_VmTFPeQHe0-KO8ZaGjGZ1v1unpgeKPdGvJgGGAOeTnSMLoHnSPdQZekQU-DA6r9yauQm_OHhYMKXVDNrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=VmE0URG4JALTxUTQGIv9NG75poImVd4Epun0NXkl0XK_Sgy4Qmps2P3n--O5rVnMJc8J-smGXf2QLvCl7_pULY4kN3dZLu25FWO8LPRJ2SS22nc5lLr6yPlg1-dIcKZ6FYGaMbvSsstoTbRAgbxgvoWnCNF21iHNmFyfXkvjluhDYJozb2vxSV7UvhYCwCkTAZSwZCuEx5BKMWGlPkD_kZBSp7vo2NI8G5RpvtpwgOp4SeeckYCYAzetqKV4cF1pRMC6_VmTFPeQHe0-KO8ZaGjGZ1v1unpgeKPdGvJgGGAOeTnSMLoHnSPdQZekQU-DA6r9yauQm_OHhYMKXVDNrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=YTK6AsInW2fof34eNRGdgJRqamRmo0im49K_nkr4QMAhiXvyhWpHicRJEVAwiR2afXWM8LGbukgJu4oxFhPyS12iM4B884UiK6HCp9U9Q-3MoqZX-CWhpy0pmaqrt_JtQkrWi_Qi1wKhI7mRlm9vQI_1xSj9EYz_jCDsLEi8HlpDZ4CbyXEKxhU41o2X-kYYOffxtQrCo_XHORDub0nAI1CiFcB3JY59TF5qFaxH7ukX05szikD0bIhht_QKXTJogtlz_cz1BrktUAFcKwAUq_btXbpNZJeyWrXDbb9EVDsHEOWafcwhJT1O51hW6WNGPcj9HbItkoGdoKJlKoakfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=YTK6AsInW2fof34eNRGdgJRqamRmo0im49K_nkr4QMAhiXvyhWpHicRJEVAwiR2afXWM8LGbukgJu4oxFhPyS12iM4B884UiK6HCp9U9Q-3MoqZX-CWhpy0pmaqrt_JtQkrWi_Qi1wKhI7mRlm9vQI_1xSj9EYz_jCDsLEi8HlpDZ4CbyXEKxhU41o2X-kYYOffxtQrCo_XHORDub0nAI1CiFcB3JY59TF5qFaxH7ukX05szikD0bIhht_QKXTJogtlz_cz1BrktUAFcKwAUq_btXbpNZJeyWrXDbb9EVDsHEOWafcwhJT1O51hW6WNGPcj9HbItkoGdoKJlKoakfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNrlz3pGSgfwWGzLhE_nDYYOufjUZx_2IXUd4SsQK8c08X2Rv0vW0g84jErX347uoNMb9PGJ7Wx5qSk5cmXmR91Hcy22-5WSP91PZXUB1RCn1n8W3HKRy-4icNNup3fqTVj3DZ3fKCuW1MOx7yzwOfAE7ou-VVJfp79EhmaTz-H5RDc_A89pJYt50_tFgFRZTj-y3ZBapPb0qdL0vQrUGhlcEWhyhzv-7QqSR_qdgiATLE6DSn4JE0xKg3TuWJlUi0fgDL1fDuJ_joIBWby179EtMsicdnIUrdeSkLOIROnm0L2nop2pnqPXGYpbp47FkTbHh6VpbtYAIgAGsOWbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=h8dUF0P3fVAG4-t6IMqT4DxfnTVmwk7ftBg8TbK70aVELU_7am94NDIraUu3oVUPa_bAUQHPNTywJo9lZi5UBmWLDDd8ZSPMHv8gNZvPiZgSspzwENXsUo4atgLRar57ZfNaC85GTu1LaNB9Rce1MgxAZzU3iEk0T6NC2geJG5xiNTvCI3DhL8C5M80UUcx5jVwxZt3pOFyHU3u-8gllh04C5TMI7I0rElDwbixdoepvB1wRjMHs33oLJZxiD5QFS72-GanGhgRZcVmPWS-c5SeOFFNpQG4fnK4xBcIUpMtgmlTRNOk7feWm4fJquG79AzCpApBoakWbz0pQYWVlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=h8dUF0P3fVAG4-t6IMqT4DxfnTVmwk7ftBg8TbK70aVELU_7am94NDIraUu3oVUPa_bAUQHPNTywJo9lZi5UBmWLDDd8ZSPMHv8gNZvPiZgSspzwENXsUo4atgLRar57ZfNaC85GTu1LaNB9Rce1MgxAZzU3iEk0T6NC2geJG5xiNTvCI3DhL8C5M80UUcx5jVwxZt3pOFyHU3u-8gllh04C5TMI7I0rElDwbixdoepvB1wRjMHs33oLJZxiD5QFS72-GanGhgRZcVmPWS-c5SeOFFNpQG4fnK4xBcIUpMtgmlTRNOk7feWm4fJquG79AzCpApBoakWbz0pQYWVlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCfyo0YGJhFdaa1DMC2pFhfLgWJF7NAKJhHphBnpNJtadx2eoxQXONETq2--wqfCI5Kt_j6XWO6y9IXsgZsy-S6zs3PlVCRdOjwJcDMrp5p1NK2Tt-N7jW3sxQef3O1VjWRs5nZEoUxGDAdZW0uqK_L3_wX_z2UJc2rB9yu1YnKON0DsbhwL4hdklxlnYyMr0NtI05OH91FN-E1m4Qv2hJegbkIFdwyfncA3sB5l03Acjh1yUphd0wgtxtGmkGd02iBns6g05pxSmwhEH9SxeM3Qycye-Ssy_hQdG4Iu3gxVnwekbfTCQwyOwcoocVO-ltqYpDX9cbWHf09xwWOipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=ucw091CtvBzNgBv0srL2zKpcTHNvoHyPlWEGX2YRFSvRQQse6Q-G0s9tQn8qjp14yo6a8-BKb2Re7Z4kW69LR3Fx3F50G9GPYC3VuWWcZMpQBChygvBtw76NmePhDSDRHg_IYFi6dTtIGw_GTtUs8JPRVlrP7jtLFESOKgtWbEyXdasEYshbGMBn0-ojfQk8RxZuh1-dBTINUAl84Dd_YP7mWfGhVz2PRBbUu3fgZHvEsjLOWV1z4FCi2njaT_R5D5ZndNbDM-l2ccQhsMg6sUGyQKTlOoXmaJN6ZadvFAnAvevV_wN58AzVzyBkZ4el2SmEFug5Yne2bYuIiiXfGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=ucw091CtvBzNgBv0srL2zKpcTHNvoHyPlWEGX2YRFSvRQQse6Q-G0s9tQn8qjp14yo6a8-BKb2Re7Z4kW69LR3Fx3F50G9GPYC3VuWWcZMpQBChygvBtw76NmePhDSDRHg_IYFi6dTtIGw_GTtUs8JPRVlrP7jtLFESOKgtWbEyXdasEYshbGMBn0-ojfQk8RxZuh1-dBTINUAl84Dd_YP7mWfGhVz2PRBbUu3fgZHvEsjLOWV1z4FCi2njaT_R5D5ZndNbDM-l2ccQhsMg6sUGyQKTlOoXmaJN6ZadvFAnAvevV_wN58AzVzyBkZ4el2SmEFug5Yne2bYuIiiXfGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=r3261cemRE7GLqKii9Wfqk6xSsaLfTlBM1-rPEYn-nAtdWrmugLxXCiAO43r9SgC1671tYQXHgjKv1vONJMxBup910IievFsRxciykypFU_18tBUFWnE5AiyhVYJ0Bj_yKwg3KIh9X-ZlW3Yu7re_bf5-qcihaHrZwUhQqZwvtsvZPkDf_zjXDBbdyGtTfZ7Gfrmvc4x5NiK4lcevHHYvxq8J4qFqSBiFOGEDJElvGJwnp-K89BAYCzFfivDP_0SGuo09j5vUHgT2VauQ_2QbmGJXTjV447a_b7tYcRGnteSe9TMBKcJBy9VVnKWwRD-JKqjQ4WjUS-6nC8ISO-Vsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=r3261cemRE7GLqKii9Wfqk6xSsaLfTlBM1-rPEYn-nAtdWrmugLxXCiAO43r9SgC1671tYQXHgjKv1vONJMxBup910IievFsRxciykypFU_18tBUFWnE5AiyhVYJ0Bj_yKwg3KIh9X-ZlW3Yu7re_bf5-qcihaHrZwUhQqZwvtsvZPkDf_zjXDBbdyGtTfZ7Gfrmvc4x5NiK4lcevHHYvxq8J4qFqSBiFOGEDJElvGJwnp-K89BAYCzFfivDP_0SGuo09j5vUHgT2VauQ_2QbmGJXTjV447a_b7tYcRGnteSe9TMBKcJBy9VVnKWwRD-JKqjQ4WjUS-6nC8ISO-Vsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=pjVkUHqcAd5nQYWOAYeAH95Hi-KEehxdRFvDmEbO0g5DgO-Os68lwXMNDRQUSKqCFzPP4EKAtzdW4_hybTgdMt6ID0NkHApk9cLmkry4bvSzQIc7A7o64I9jWAYnhEC9nqxYCbhGg5HWwD7_GrjZy4TDmoKDlKZZ3AoUPwXLckIYNc-z-v-MREUraYuEidav8RsmJsi_8IpyPJlEls-fnROr8Vdgv3OTSM_WBzj3pXhBoPm45ftHYcDfmGQ9j-yv7dW744zLPmds0YdUY10kg4fhl4fy34fBrvTQ6QwFGzN2t8crCB8X1DqJiG8Ap7R8j6M5b2mS_-ID9Lp-Oeipzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=pjVkUHqcAd5nQYWOAYeAH95Hi-KEehxdRFvDmEbO0g5DgO-Os68lwXMNDRQUSKqCFzPP4EKAtzdW4_hybTgdMt6ID0NkHApk9cLmkry4bvSzQIc7A7o64I9jWAYnhEC9nqxYCbhGg5HWwD7_GrjZy4TDmoKDlKZZ3AoUPwXLckIYNc-z-v-MREUraYuEidav8RsmJsi_8IpyPJlEls-fnROr8Vdgv3OTSM_WBzj3pXhBoPm45ftHYcDfmGQ9j-yv7dW744zLPmds0YdUY10kg4fhl4fy34fBrvTQ6QwFGzN2t8crCB8X1DqJiG8Ap7R8j6M5b2mS_-ID9Lp-Oeipzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=EZ6cPCnMZ83ArH3LearYS80AyT3g29HEf_VhvJhdjnJxNPYAGdW7TZtkZhuR_yoXH6F3OOrWRj4Bzb6kPAhgiVcHdpEEKNZ9_GCnagxrxLAhzu39IwQ66KHWHQZiW2anHLaoJrQxnxu1-syycpNmbaDCELtN96rRP5ti0pBKMXeCVAgXLtYu-Dn7H30VQabeyleiNgOJhMpJ9dtxOeYf5S19X6cGk4dHgACyjeqbr3OUgYuHzjQE5dTMRtxWCbq21yIxDi58sRpQ0UVgVYdn8y4lpr7ZUxazPZtTDpqB2ApbM3k77xuS5FPqsn06Oft6cUCT_qjT0APf4sxlQAqJRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=EZ6cPCnMZ83ArH3LearYS80AyT3g29HEf_VhvJhdjnJxNPYAGdW7TZtkZhuR_yoXH6F3OOrWRj4Bzb6kPAhgiVcHdpEEKNZ9_GCnagxrxLAhzu39IwQ66KHWHQZiW2anHLaoJrQxnxu1-syycpNmbaDCELtN96rRP5ti0pBKMXeCVAgXLtYu-Dn7H30VQabeyleiNgOJhMpJ9dtxOeYf5S19X6cGk4dHgACyjeqbr3OUgYuHzjQE5dTMRtxWCbq21yIxDi58sRpQ0UVgVYdn8y4lpr7ZUxazPZtTDpqB2ApbM3k77xuS5FPqsn06Oft6cUCT_qjT0APf4sxlQAqJRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=UnyikxiUhafTyGC0SQZoiPeyZq6qtCqhnQ2Nio-_s53LBkJUoLUGnvOko-YDgPqJbyfLcUXR0VNbm5cP15yofR_lKJOk7YPYSRg7SUok97bvE5iF1dp75SA3pwUCuSyYrdjsXA5hnyirZCKGv6wr07A-LgyFAtkDDdSaIyaWbiBFtpwNmK5PTAZ2_SEndR01g9gn0le2I_HYZXPdlg1wepxUAllp18fguE6RXVddrUkeiDIUnc_Jj7xx2E10Wyf5PvksenqY68DmTETEcaGmEUIV6uE6UxK6BXREgimpnJcCSfiDkiwVI--1xc5Ftb9jcmdVyJNso-ArR4oP0A2SYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=UnyikxiUhafTyGC0SQZoiPeyZq6qtCqhnQ2Nio-_s53LBkJUoLUGnvOko-YDgPqJbyfLcUXR0VNbm5cP15yofR_lKJOk7YPYSRg7SUok97bvE5iF1dp75SA3pwUCuSyYrdjsXA5hnyirZCKGv6wr07A-LgyFAtkDDdSaIyaWbiBFtpwNmK5PTAZ2_SEndR01g9gn0le2I_HYZXPdlg1wepxUAllp18fguE6RXVddrUkeiDIUnc_Jj7xx2E10Wyf5PvksenqY68DmTETEcaGmEUIV6uE6UxK6BXREgimpnJcCSfiDkiwVI--1xc5Ftb9jcmdVyJNso-ArR4oP0A2SYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=jfrMjVtpjLobq-TFBmRmikwr-isF8Z8d1AuPl-uLpoE1XCXf5iy_07dSx5HsGWcVoOPMvQ9lhBoL9J3a1noe08Y89ytuvgp7Gnh_5ljJE_iQoWN7Td4hjGwxGJEUAGuCW5jhnfE0-BkUpwcGxSuHonircLvBzPW7mk6riapgA6yULxkud5E00xM8IgFZS-vKsFlXEASIDioyj2SPtIrvb8eS39NW0g1ItDqVdGkIFO-WLa_pMMMx1dKDBgnFiMwLULbIruOWXWFX-49xAQqEo5gEaJZ3WR1ZIrCOQO2Hxe9oU4B7wmxcbApgq1bNj8uxcNDpk-Dex9b1McS9QOjlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=jfrMjVtpjLobq-TFBmRmikwr-isF8Z8d1AuPl-uLpoE1XCXf5iy_07dSx5HsGWcVoOPMvQ9lhBoL9J3a1noe08Y89ytuvgp7Gnh_5ljJE_iQoWN7Td4hjGwxGJEUAGuCW5jhnfE0-BkUpwcGxSuHonircLvBzPW7mk6riapgA6yULxkud5E00xM8IgFZS-vKsFlXEASIDioyj2SPtIrvb8eS39NW0g1ItDqVdGkIFO-WLa_pMMMx1dKDBgnFiMwLULbIruOWXWFX-49xAQqEo5gEaJZ3WR1ZIrCOQO2Hxe9oU4B7wmxcbApgq1bNj8uxcNDpk-Dex9b1McS9QOjlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrckWZpqUmE7gUZcC2_sEuNiZfzQgOltIOzW_1Z59vRCsaQDyunQYv6Rf0qd7AXMx6PhWO1hWi6cUuWDw4FyvnnGjNBK9_SyziP75o9RH9Q7-Lgz_zcx3DuDCv_WaqYESvzy6OCDMgePnH4Y6-PDMceTFyruB_IDT3lJokumzeJ8CTpWN9BLs2_YKMRcAjELFFz03SIierdZB5Y3C5iR0oDuDt_v79PF1Bhg7gXNgVQmUI2XLGnWgGz2MpKq4V9upGF4SjYkXA9bYqX8iKfqcGdaB2Vko5QTeD0Y9fa2OOIdyjfs7hxCDx2qKhNzF-35MnlXYPSc6i4dkTMblD8sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2JafPkk-eMdCykoJZ-PgwEAIcC4Hn2QRwj7OxNFjvEdnmTiyAW817gAyD9cwAtUX2jeL17dl8GDi9JUaOLkQNMc3u2271s3yXsZpS2KOL5njKcrmmzj2sLVQvv2GYVQk_LC5HlXprmYEj4lUmzvjknb-BAHDarVsTgEStQyPvmXLbGmZspQEmEMWeFbxsoQlG0RsOLejjeJSidtNxh-KQeOLKJl-Vkwg-p4F7FItrhmqT7aEuvGE_0cKZNNcs_negtews4wCwvQxOkKNxTJ7gXlddF2I9vR5pTNLfKqHEIsc2BzTWDYPFfdPVD2BmfaOPuB9_VDIJy_Rv4PuxrWIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=v5AfZTu-uc12r3ugxH-0HjjU2asU8bOkqDKtlNw_aZJCo4ZRoYPH4D2OcchC3J2K0-13SJwAy1DJJ09Gj1llyRERJ4EWCgvW7FJFWR8zFKRST5TcxrktNl8Mq0NRU4XieJmd5aCyos5D4lJ-gFU9jW8DT5pxI7aM_70ogN457ycO7Ne5-V0-dviQnqSRBdveQTAd5-G6FiYNeKn1pXewE8WXMnOK9hy_SPBQ9sKm_PYyZba4SYfkyaeKmmcoScJ0oFFO83n6E4WxkYM8zecxHFkIKSZTVqA9JAPbq9Vt6U-BQKmQXztHwxG1EAyF6Xm0Apvf45RI2AykiObZ6RrS1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=v5AfZTu-uc12r3ugxH-0HjjU2asU8bOkqDKtlNw_aZJCo4ZRoYPH4D2OcchC3J2K0-13SJwAy1DJJ09Gj1llyRERJ4EWCgvW7FJFWR8zFKRST5TcxrktNl8Mq0NRU4XieJmd5aCyos5D4lJ-gFU9jW8DT5pxI7aM_70ogN457ycO7Ne5-V0-dviQnqSRBdveQTAd5-G6FiYNeKn1pXewE8WXMnOK9hy_SPBQ9sKm_PYyZba4SYfkyaeKmmcoScJ0oFFO83n6E4WxkYM8zecxHFkIKSZTVqA9JAPbq9Vt6U-BQKmQXztHwxG1EAyF6Xm0Apvf45RI2AykiObZ6RrS1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Rhvg0nI6r6gCXu6ykMrN93nEiYYZkjJQkp6U4sqbBetlMnq_PYdUlcg6CdyxXJGZCEYJWh-ae5ZvSkDH7vHX_i5UVZz7yfdluIzkK5p1ona5dIeU2bgAqo1Lwp2MvI4WiNVZokoqjfLAWZXQaye8MSR6YIsPQ4Yx2JWvUYbFK70Dfosb5PBjSoQg_3pCm2RygJum8YAs_JFVR7vgRceySZpCWe0r0HJNTp-ae_uDlZFHc3DlF3yidZt81gpngUjTI65XMV7pmVW_GBa0wgHQKBgRFS0_iLbnR-UoOuOegBVBSYmCqHECzaqAkGp-iYPK5hDUSeqsC3iTVQG8S3aQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Rhvg0nI6r6gCXu6ykMrN93nEiYYZkjJQkp6U4sqbBetlMnq_PYdUlcg6CdyxXJGZCEYJWh-ae5ZvSkDH7vHX_i5UVZz7yfdluIzkK5p1ona5dIeU2bgAqo1Lwp2MvI4WiNVZokoqjfLAWZXQaye8MSR6YIsPQ4Yx2JWvUYbFK70Dfosb5PBjSoQg_3pCm2RygJum8YAs_JFVR7vgRceySZpCWe0r0HJNTp-ae_uDlZFHc3DlF3yidZt81gpngUjTI65XMV7pmVW_GBa0wgHQKBgRFS0_iLbnR-UoOuOegBVBSYmCqHECzaqAkGp-iYPK5hDUSeqsC3iTVQG8S3aQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=VlQhJNBvDn2CONt_3d0F3w5xtbe2wh_L0iftHRpT7kyL636UvhyyqIcQ3Q0TeVQsVZxu2E1sEX7QuwgARQWjifswmp6543s5FAbUaQedjMUPjfg5ISgyNRab1xJQYiWg9qY2sNel9P8mtPHgQUngGaPwnrwNpfvTW0L0Xic5XgpIIvVVkLEdkBRk_9uTG6a3X5rTUqV-lD98fjtchFNYqWgV4nrWxMiR-Kx9hwAR2rrWXccXZ1YAVr5mMbjYeVFNzu5UBkui4HoR9V6tDVC1KT-_FDpeb2UDiyQcsaHJDChO7Ph_RW17Pruae8OJrDG9fBr5jfiv_Qgtmj9uzHaiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=VlQhJNBvDn2CONt_3d0F3w5xtbe2wh_L0iftHRpT7kyL636UvhyyqIcQ3Q0TeVQsVZxu2E1sEX7QuwgARQWjifswmp6543s5FAbUaQedjMUPjfg5ISgyNRab1xJQYiWg9qY2sNel9P8mtPHgQUngGaPwnrwNpfvTW0L0Xic5XgpIIvVVkLEdkBRk_9uTG6a3X5rTUqV-lD98fjtchFNYqWgV4nrWxMiR-Kx9hwAR2rrWXccXZ1YAVr5mMbjYeVFNzu5UBkui4HoR9V6tDVC1KT-_FDpeb2UDiyQcsaHJDChO7Ph_RW17Pruae8OJrDG9fBr5jfiv_Qgtmj9uzHaiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=gI4xNNC31T7yOeFDwsnMMJBhoF4oC-DKC_14fI3YLcBuoxP_wSOOsHX-FjSARXAQYSwIDzy-L2VmmxB5_lMGKqabrns-BP0EMuodwd0IWeKpnUcNSc5mJlBkgt-cAUq4Q5KQr5Qt6M1jW0Y-ZVy4z_hVTaf2sRDS1AcxAZOwSpoOyKs4gcmsh9n_xTkWxbR3dEB-APJLdZYJpL9RD35Pb-iqTUPvzLOtT4tXCK0OA5rjSnrhGBvGzixjjxh8zB9dCV-8B-ewcsWPSss2DdTMRtQgd4LXXtoW0LEIrJB4szlzK-9426wB5qhJohAVE6AdQMAQnAOlLq9rk-NhR-mVlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=gI4xNNC31T7yOeFDwsnMMJBhoF4oC-DKC_14fI3YLcBuoxP_wSOOsHX-FjSARXAQYSwIDzy-L2VmmxB5_lMGKqabrns-BP0EMuodwd0IWeKpnUcNSc5mJlBkgt-cAUq4Q5KQr5Qt6M1jW0Y-ZVy4z_hVTaf2sRDS1AcxAZOwSpoOyKs4gcmsh9n_xTkWxbR3dEB-APJLdZYJpL9RD35Pb-iqTUPvzLOtT4tXCK0OA5rjSnrhGBvGzixjjxh8zB9dCV-8B-ewcsWPSss2DdTMRtQgd4LXXtoW0LEIrJB4szlzK-9426wB5qhJohAVE6AdQMAQnAOlLq9rk-NhR-mVlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=aycPmdpzyVAJhO9ViXhVlGXM_Q_VWNwOZH-tJNNDMsLH_UmfSHQURsSe4l3MDX1bZRMjGbNuTni8bsIG0EPaH1XU75e8Lo23IqoQ7cTJ7FOWZFKGDwsW44sYGwuWG61AW4Ka_6gOcrS9tiou6Azw_zjRnOpkzfMNS-oKp2KJhvX2-IaJ3tn65DUqjpDsabZnE2KQSGHmMfXsPQCsNY24lJa0oeEgkPkyM1JDrkeDIcQl7PD3m6y7nQLtWiEL6E2f1z2_eC527tcZ5iJc9rH3gnb-81HMSfNyZJKebJCD0tyh18slp82RNWN_E1MFUxrAoeGijr5Ta2PY3i51JJHVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=aycPmdpzyVAJhO9ViXhVlGXM_Q_VWNwOZH-tJNNDMsLH_UmfSHQURsSe4l3MDX1bZRMjGbNuTni8bsIG0EPaH1XU75e8Lo23IqoQ7cTJ7FOWZFKGDwsW44sYGwuWG61AW4Ka_6gOcrS9tiou6Azw_zjRnOpkzfMNS-oKp2KJhvX2-IaJ3tn65DUqjpDsabZnE2KQSGHmMfXsPQCsNY24lJa0oeEgkPkyM1JDrkeDIcQl7PD3m6y7nQLtWiEL6E2f1z2_eC527tcZ5iJc9rH3gnb-81HMSfNyZJKebJCD0tyh18slp82RNWN_E1MFUxrAoeGijr5Ta2PY3i51JJHVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=nv0D3XAiqnWi6P7a3Pc8V0hAItaWYFnMs1XoExPN1N5zCtFWjvFnhxzH1PQ--R77_j6lyOOkj6lV2qPgoig99c0BNaU3DX8CZYl2Z5RI-9XmQN_BOZ6hhw_W79hvGID0EX8N3lvQf8Lu-LTjBii-FyX3l9uiVk7rfNh3ep6ouTbthPICY4ZI9RBVQ5Q2IdR6lxdmKNIrb17zZzFAwG6Uz0oyLO4HXqVB_s-HwIgkAK8Hg7vrUYfuh939VkV3OItiPCXcvLWdSefa5OkkrtIeOe88gWAt6bLdtwv8j4dVCiKMJUysebY-1Tqb1esjbAZkx8EIyI2bH2mUCe7VeZKHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=nv0D3XAiqnWi6P7a3Pc8V0hAItaWYFnMs1XoExPN1N5zCtFWjvFnhxzH1PQ--R77_j6lyOOkj6lV2qPgoig99c0BNaU3DX8CZYl2Z5RI-9XmQN_BOZ6hhw_W79hvGID0EX8N3lvQf8Lu-LTjBii-FyX3l9uiVk7rfNh3ep6ouTbthPICY4ZI9RBVQ5Q2IdR6lxdmKNIrb17zZzFAwG6Uz0oyLO4HXqVB_s-HwIgkAK8Hg7vrUYfuh939VkV3OItiPCXcvLWdSefa5OkkrtIeOe88gWAt6bLdtwv8j4dVCiKMJUysebY-1Tqb1esjbAZkx8EIyI2bH2mUCe7VeZKHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=meUk2e2IOvJUWxDV_Dm3WDeogua_Kg2-5Y_VkmjEPr2jTOKp6tH-_-PyLgQsicNNqvTtNxaHDAk0bqQ6kVIm3HsSwwv4jAo5vP4If-2fltU1QlnaZNk4YwA25j4ct905C0qgMipjydYCNO89u-Neomyjseu_KEi7a3KxkFXyAvn5x5wA3G0cvNJgjQDLtpkkUpJiyoGTcBXwPgMrHAYxIlazvmA__uClFZdhstDv4OpA3oR1zUF0lo9Cl-FJHU5oBj2q5jLs9k6ffw4Dh3xUctw6OuGzqBgC84ZpcfjGonnuTQP1S8Iqbxr4JLRvcDK7opYl1eOQ0gLsGmHNHFmImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=meUk2e2IOvJUWxDV_Dm3WDeogua_Kg2-5Y_VkmjEPr2jTOKp6tH-_-PyLgQsicNNqvTtNxaHDAk0bqQ6kVIm3HsSwwv4jAo5vP4If-2fltU1QlnaZNk4YwA25j4ct905C0qgMipjydYCNO89u-Neomyjseu_KEi7a3KxkFXyAvn5x5wA3G0cvNJgjQDLtpkkUpJiyoGTcBXwPgMrHAYxIlazvmA__uClFZdhstDv4OpA3oR1zUF0lo9Cl-FJHU5oBj2q5jLs9k6ffw4Dh3xUctw6OuGzqBgC84ZpcfjGonnuTQP1S8Iqbxr4JLRvcDK7opYl1eOQ0gLsGmHNHFmImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=RY6w9JNU1WpMRy4KZAPg2Mbq8Cd0eKWncfmN9gy0ri9AihVWN1uz8OlPuycL3ziIb9UHXjBEAbbsqrkCvFi8V9ya9A0tJVEMzy-jCwacKMVJKRFwZbE1fVlYzkEq1_5pXZ4q6upvuaCL76Rgw6DEdE1SkfF5E4UKaSWhbzQrNUmKnfj3hrY8tayq60MlaF1OXQC3XjJnwFmj3_hq8nfAlV8VTeg4HIkqFGs2XCUW54cWnHMs04Fvu2P184Ui6CoJLjtqhB7WGtxsC2HXRoKZNlcsHn3DlzEtuv29_B4y4fe5Q61wxENUx2w1yjALHnn04LyHIv3wKRhgYb9iUP4yuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=RY6w9JNU1WpMRy4KZAPg2Mbq8Cd0eKWncfmN9gy0ri9AihVWN1uz8OlPuycL3ziIb9UHXjBEAbbsqrkCvFi8V9ya9A0tJVEMzy-jCwacKMVJKRFwZbE1fVlYzkEq1_5pXZ4q6upvuaCL76Rgw6DEdE1SkfF5E4UKaSWhbzQrNUmKnfj3hrY8tayq60MlaF1OXQC3XjJnwFmj3_hq8nfAlV8VTeg4HIkqFGs2XCUW54cWnHMs04Fvu2P184Ui6CoJLjtqhB7WGtxsC2HXRoKZNlcsHn3DlzEtuv29_B4y4fe5Q61wxENUx2w1yjALHnn04LyHIv3wKRhgYb9iUP4yuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=NPX-zGq3Sx-e6kpKRcOHtOWAWVF0ESxh3uhsxMR9xqdK9D61Wprgnlr_q3dmG4O_Wvgu_VOISz0ankup_-GunWueeNAa1f06JBFaKMW6tnkzqQFul_wxRlH-GQ0u-Tq9v2vZ8howuErhlU0jnGoQC2wo22_aN49pK2GtLqJrsNrYn8yBHADb8V5yP5ueNR_iHClrYwdkFNS41ohRTkweBXyYRQljpKz5eQx5WB--iQmRO3366IZ-3PnvYaCbAGeZnLRKtPEn0zxCEgHJifexk-c4X8LDjq02vEfgIVqTj4E5gugGmJGYxaTEPadPEyfb0kCyqPbXzxL0Xs86Nl1Hqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=NPX-zGq3Sx-e6kpKRcOHtOWAWVF0ESxh3uhsxMR9xqdK9D61Wprgnlr_q3dmG4O_Wvgu_VOISz0ankup_-GunWueeNAa1f06JBFaKMW6tnkzqQFul_wxRlH-GQ0u-Tq9v2vZ8howuErhlU0jnGoQC2wo22_aN49pK2GtLqJrsNrYn8yBHADb8V5yP5ueNR_iHClrYwdkFNS41ohRTkweBXyYRQljpKz5eQx5WB--iQmRO3366IZ-3PnvYaCbAGeZnLRKtPEn0zxCEgHJifexk-c4X8LDjq02vEfgIVqTj4E5gugGmJGYxaTEPadPEyfb0kCyqPbXzxL0Xs86Nl1Hqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=k9liFLzXhJyVCXiIVPFsX2zTK3Bzpn5zOgZjLXmHhglIfErzEJmZ6yQmBybY1Rhs9FpktJZnOTyDSaDW7yPq_CfG2AKouqCodphASCiEZPUTzTKCWHfFhRFFUVZeBUF7eZgGRVnMoCu3zocedE5HdbfKqicr6imDbjwKAd9AfANhqw9qVTiwZLv14AQrXXzKgPhMFwVN_Y9tKzyZwJFwYmD3VhC64D-hrIU0-4_b-e79Kjk2sU5xjuLtJV4SGrJmxrOB_AEg4ectrjKcTWm15Cs_p1hFmdYnaj6OkFAcqR_ukzlhnVZFnBAiWS93gC3hIYDwss82uSw9lRrRMuzKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=k9liFLzXhJyVCXiIVPFsX2zTK3Bzpn5zOgZjLXmHhglIfErzEJmZ6yQmBybY1Rhs9FpktJZnOTyDSaDW7yPq_CfG2AKouqCodphASCiEZPUTzTKCWHfFhRFFUVZeBUF7eZgGRVnMoCu3zocedE5HdbfKqicr6imDbjwKAd9AfANhqw9qVTiwZLv14AQrXXzKgPhMFwVN_Y9tKzyZwJFwYmD3VhC64D-hrIU0-4_b-e79Kjk2sU5xjuLtJV4SGrJmxrOB_AEg4ectrjKcTWm15Cs_p1hFmdYnaj6OkFAcqR_ukzlhnVZFnBAiWS93gC3hIYDwss82uSw9lRrRMuzKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeYVAR4iyyCxkqA94XsTo0rRhj0p0Z9SBe2rFWlBzorPbcVfqnbXMDC1rHFBVdEBmColT7mbnzYWNHRI2q08yla_jTP9VkyoPZ6X-2f1MoCl8MCta0ECFmFbf1dWqCq_gA3HBUlITKzKsxM00BYaujp9Wuaiu54h-GbsZr3zGM7lJffjO9Ge14CycER7gAXW440bLtg96vxpJCHn6V89UqsiIhzlYeg3k3VoraOHzTNKR3cbsZB6DLyk6Uc6wIH0C2YBIguE3FoPf1vcFf1Yo5IGAWQnl_5iK7TVhIa4vuyI1DaZBbIasH1LOFovJ6KiZ2z8K21eRYra_Tt1sK8y9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSKdjXqsrn83ZBG7tlP5H5KW1snn8crIMLeoLGcd2uwltuHA7SfXYcBjDTVv3lRPQzTZ6y3dJgV5WgFGvIvTCQ6icoLYtjM4PAeKUyJq3kgloF3nVCvfrB0Hub4s3w0Aa7ujbbwtn486EUy_mbQcBCiYR4chQiwF3ylJuudZ6Nh6TbQzbUY0s64VsereBvWuXZLKKKMNE6Axt8ueVl3jOyY-mZbqhL2LrTY6M7nrOC_g88rRqFPcoYs7vlNgUWdnXhug9MLxG8urlUFUwpkhYWQkbCowM-4fTHQspMzTDz4evy8tNXH_C2GNBWGSmwtOdjW46WSo82dxOg3V6OBARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=M80c2AS2a48vENMPH2YPeQApX6SCijdyDn4MqQ_29Ht2s0asQetnnIfD0Ac4gtXBq4dA_dRXo9A35ehldFTxKja8nZHSrHHtPIoJOmw5_GhMwhOoT4Kh5lmEyhVvo2KLo74jOhmgQ9p7c2l0B788ZnAdCkWXwzvxgjUZa4mCo5erWGL60QtVdWtlvJzrH5sva477umnBUrimN8p75xvANkGBeNhJiggJYBK6VGj3gklkaF8DpVuEj8ytojbDt50ZMK027phVdesv993bXuz4lYaB-Jyu0Ehb2NnRJgDaS9fy2PDIhT3l3J6riJKjo4CnGO68HjGKHIzHaddaLZlItA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=M80c2AS2a48vENMPH2YPeQApX6SCijdyDn4MqQ_29Ht2s0asQetnnIfD0Ac4gtXBq4dA_dRXo9A35ehldFTxKja8nZHSrHHtPIoJOmw5_GhMwhOoT4Kh5lmEyhVvo2KLo74jOhmgQ9p7c2l0B788ZnAdCkWXwzvxgjUZa4mCo5erWGL60QtVdWtlvJzrH5sva477umnBUrimN8p75xvANkGBeNhJiggJYBK6VGj3gklkaF8DpVuEj8ytojbDt50ZMK027phVdesv993bXuz4lYaB-Jyu0Ehb2NnRJgDaS9fy2PDIhT3l3J6riJKjo4CnGO68HjGKHIzHaddaLZlItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=VTbeuTpS895-xHR6Ut7EGvKILtka262YEKvWvi4wk1MlfhmL1wNvIfgO8ZSzN0Xdyll0TTXoRvAF130xVnjaz4Am5M5kjB1WO5OglaraU1TUgREeoHL7_nTQyHpGMknLhHR1aAqQO5iwgwOaH1O9ugvJE7UJfd0lM9ehkeR5j-myeWIjm7FEmz03Ild1kYEI-toh2AH-opaVN51EZFLWNu8EyWlFJio78jpEhg8qv-9HnFaWwfHVx07-rgbwMSW_4eJohkPfDR68PetzFGFcQ-GUjySf3KVKhdWOddMTd3T_IXcip17YJHvSg2tJ49c0qnkCQ4z19VY4HLPrAhNqKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=VTbeuTpS895-xHR6Ut7EGvKILtka262YEKvWvi4wk1MlfhmL1wNvIfgO8ZSzN0Xdyll0TTXoRvAF130xVnjaz4Am5M5kjB1WO5OglaraU1TUgREeoHL7_nTQyHpGMknLhHR1aAqQO5iwgwOaH1O9ugvJE7UJfd0lM9ehkeR5j-myeWIjm7FEmz03Ild1kYEI-toh2AH-opaVN51EZFLWNu8EyWlFJio78jpEhg8qv-9HnFaWwfHVx07-rgbwMSW_4eJohkPfDR68PetzFGFcQ-GUjySf3KVKhdWOddMTd3T_IXcip17YJHvSg2tJ49c0qnkCQ4z19VY4HLPrAhNqKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=vMToNEe2ORLKxCKCq29-A7puUzXefVSFD0dWqLNtAU-YIZ_J7A1P_ItGxrFnlN61tuE9RI7Dz_x4fdJxup-cW1ZovR-HvYdQQe2c2mdRHQouTUzzRQr-soFyLxVSShHwRLxWrfMAO6bgEYgCU0Lpyj133R3weBqxoOyrHQfhDwN5B8DUU-w-UsGr1j6E7Uy44pIvtuS_HjVI46RP9vG5ncpdCYF13xOnZR29Wf8V8yOV_AIdULBzCma5tFB5EW3Wnjg1FmpWZaHMdR1XNodA8QzUjiSHI7OQFt52aEkt2frEU5knbrxL5_UnQrBinEOVifyFypvRRYikjBZZp0d5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=vMToNEe2ORLKxCKCq29-A7puUzXefVSFD0dWqLNtAU-YIZ_J7A1P_ItGxrFnlN61tuE9RI7Dz_x4fdJxup-cW1ZovR-HvYdQQe2c2mdRHQouTUzzRQr-soFyLxVSShHwRLxWrfMAO6bgEYgCU0Lpyj133R3weBqxoOyrHQfhDwN5B8DUU-w-UsGr1j6E7Uy44pIvtuS_HjVI46RP9vG5ncpdCYF13xOnZR29Wf8V8yOV_AIdULBzCma5tFB5EW3Wnjg1FmpWZaHMdR1XNodA8QzUjiSHI7OQFt52aEkt2frEU5knbrxL5_UnQrBinEOVifyFypvRRYikjBZZp0d5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=LlOBnymeIARqhMcsNZPl9M2i4FNV6cSI2IVE6KMV0UjitXpV67BPUkaKQcJqu2Sm4RUNFWGTyDT_-aBtNex9m1AC4xLCyj1jmf6XB3AZNM8UpzIPLgM6YsusL_mee_gYD5MkknSemiCm_1beIksViiI4XvarN7VXqYQHJiXLxMdkdk_PMyew51AMUo9Khg3fBTx_3GpNEVaUoav8EKldImMRO8ZRErrON6-ZuR_Y_oEwJscwFHKVWu1i1jmr3HfAj4ycUzVi9HJlwSlq3LQ1c-EfM1CMaz48uTR-mPg26w22KK-_vAoge_O_ZzYPqqkqr4IIRcrvckXSQAgIanov-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=LlOBnymeIARqhMcsNZPl9M2i4FNV6cSI2IVE6KMV0UjitXpV67BPUkaKQcJqu2Sm4RUNFWGTyDT_-aBtNex9m1AC4xLCyj1jmf6XB3AZNM8UpzIPLgM6YsusL_mee_gYD5MkknSemiCm_1beIksViiI4XvarN7VXqYQHJiXLxMdkdk_PMyew51AMUo9Khg3fBTx_3GpNEVaUoav8EKldImMRO8ZRErrON6-ZuR_Y_oEwJscwFHKVWu1i1jmr3HfAj4ycUzVi9HJlwSlq3LQ1c-EfM1CMaz48uTR-mPg26w22KK-_vAoge_O_ZzYPqqkqr4IIRcrvckXSQAgIanov-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=LMG245Vf4T82Byu2CY025F4tXFKjHmh8HrWibwGFt95ZRaCPjuoy-VUFPr8bloX1MTY2ByR5MNtz8lWd2AmwdX9NaOlmkSuKiU87Zs1ah9iLD7XmhN4vebkNfKSkstW1Mv_WYJOnbjFflZmkX1CLCRvRVY5nQEbk-81B1aXL7ShkitKrbxiGnA244qb75weSh7TY3RKmGM6IO_hvkil4MKcW-x_qvcDLP3XfLgJekQtUmWxl2X-qCfTbly-M1CW0A3EJYvbV2ekVq3glaSt-dmRTYFKe7g3TLjceV4LFr7d-bbwhJPSaROjvCpo1eXPEoN3YuFTpBOhfzcgAYCa3mqpa4ebO-SWqu4k7_VP-ev0-N3jY-KiW-cQOXavx2SvAo-DEYfzGDcpc01YnaJh-q-g0W55iEiWZ0jp2pqL3h9JbgTsgm4o84v0tNsnfniq6Z8PEfLQ9FuPWe5CJ2rX3DGc6CB7Twm3vjs7VsE8_3SulgTssiMZDpveY4Tw3I2VV6_F1RvbCz1eFgg1Ji03Sh8iVbDywr4o4C51GM-qXRvdyxSivW_rsBFWpSt8SanFIwr4wQ2YzzRw304aGJH3cG7vR-a9TCWAjeotjQ0IjHBYbwUXjCwpUy1mRpbl6Ri2huwwAl4-W0rcHVlSqgChyeHoR83_96rqlhoDc2_9Os3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=LMG245Vf4T82Byu2CY025F4tXFKjHmh8HrWibwGFt95ZRaCPjuoy-VUFPr8bloX1MTY2ByR5MNtz8lWd2AmwdX9NaOlmkSuKiU87Zs1ah9iLD7XmhN4vebkNfKSkstW1Mv_WYJOnbjFflZmkX1CLCRvRVY5nQEbk-81B1aXL7ShkitKrbxiGnA244qb75weSh7TY3RKmGM6IO_hvkil4MKcW-x_qvcDLP3XfLgJekQtUmWxl2X-qCfTbly-M1CW0A3EJYvbV2ekVq3glaSt-dmRTYFKe7g3TLjceV4LFr7d-bbwhJPSaROjvCpo1eXPEoN3YuFTpBOhfzcgAYCa3mqpa4ebO-SWqu4k7_VP-ev0-N3jY-KiW-cQOXavx2SvAo-DEYfzGDcpc01YnaJh-q-g0W55iEiWZ0jp2pqL3h9JbgTsgm4o84v0tNsnfniq6Z8PEfLQ9FuPWe5CJ2rX3DGc6CB7Twm3vjs7VsE8_3SulgTssiMZDpveY4Tw3I2VV6_F1RvbCz1eFgg1Ji03Sh8iVbDywr4o4C51GM-qXRvdyxSivW_rsBFWpSt8SanFIwr4wQ2YzzRw304aGJH3cG7vR-a9TCWAjeotjQ0IjHBYbwUXjCwpUy1mRpbl6Ri2huwwAl4-W0rcHVlSqgChyeHoR83_96rqlhoDc2_9Os3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=Bnmf9RA8Zepu9uSLnldCy6UdlOATvaEpnJyUzphhgX0CcSEH0m8dlDvebfKiwcYrRmxqRnRAYYv6yHFZq_GLBwkcr-GYDxSKxK16-Ihl3eVSmdIRleEdm6bXJP6dv3Dy0Fd71faSHasn1hzZpP9OYky9hOy-PUu3TeWEj8YAqkNDyLXF0YMamnIvCy12IHEU3iak7VL26Q_ziRo5VQMVfTGG9mpbbQsuqo538gYpq8fsiFiFncwDXBdpMjMDElvcmiA-iLr_yz75V93tJwcvCYknVAjGxwAiM-9Wft3eWk13zmYdSFbK790eheBI2OVJT1uuUlJsVSzU1sRxNmMhe4qkSGWGxCbae7_V91-4ddhd7Weu0-p11oR8pjYnLQJBZiwip74twp35w9SLSeugkCI4C2oX1rTLie4Z5Cwr0Y_vtudyPdIr2xcLxCIgpMmtW0JwzqH-BJke52QtcijeQlckeSeTsj9JYMPrAPiE2d3Ct00YMXxlEyTEvUpqzQJQz3F1nyJ9IWFm4mpsSf0BYcZjWJVSbDQqZRuqd05AkZFNH5rijRMRgxIo1JG0Ps-UkHElPCswdyZwQFzSpao4JBlHQgdwQghqqik18HDt94FoUhJrV7MQcGJ_LT26bLvw0UizUUgf5BqVKk_8px6nK0KltE_jUcVSbFsgkciU0vE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=Bnmf9RA8Zepu9uSLnldCy6UdlOATvaEpnJyUzphhgX0CcSEH0m8dlDvebfKiwcYrRmxqRnRAYYv6yHFZq_GLBwkcr-GYDxSKxK16-Ihl3eVSmdIRleEdm6bXJP6dv3Dy0Fd71faSHasn1hzZpP9OYky9hOy-PUu3TeWEj8YAqkNDyLXF0YMamnIvCy12IHEU3iak7VL26Q_ziRo5VQMVfTGG9mpbbQsuqo538gYpq8fsiFiFncwDXBdpMjMDElvcmiA-iLr_yz75V93tJwcvCYknVAjGxwAiM-9Wft3eWk13zmYdSFbK790eheBI2OVJT1uuUlJsVSzU1sRxNmMhe4qkSGWGxCbae7_V91-4ddhd7Weu0-p11oR8pjYnLQJBZiwip74twp35w9SLSeugkCI4C2oX1rTLie4Z5Cwr0Y_vtudyPdIr2xcLxCIgpMmtW0JwzqH-BJke52QtcijeQlckeSeTsj9JYMPrAPiE2d3Ct00YMXxlEyTEvUpqzQJQz3F1nyJ9IWFm4mpsSf0BYcZjWJVSbDQqZRuqd05AkZFNH5rijRMRgxIo1JG0Ps-UkHElPCswdyZwQFzSpao4JBlHQgdwQghqqik18HDt94FoUhJrV7MQcGJ_LT26bLvw0UizUUgf5BqVKk_8px6nK0KltE_jUcVSbFsgkciU0vE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=oKaziAuWi7t7_YB-1D9Sg2HGYUXu6Rh5tRmTBRrNntcDGzYQzYS-4NgWWNrP5I8lhK8YszWGF_EKt4jsi7Ga3Eo5KyKtwdg0j0ErqfMyMbiEkzKqriL23xRTW1gWLdvtDWCzPtrqcTLxbEfTfufUU6ZedvtaQjqilyIrDge8dY5uHtmBjIvNowwvvZCv2I45wxERSauKMbjFw6ONZxXXohzHZE-NIA5ocKL0OxNv-0wm57iDU1iusUGlUIzra2s2NztS4L36hBvcRNjXp2OuJJClq-FWAt4nmcCV8N3sXC1XBwJBDP5SjtfOSUFh3p6SeaMxyHVJu5uqTRkqESLmaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=oKaziAuWi7t7_YB-1D9Sg2HGYUXu6Rh5tRmTBRrNntcDGzYQzYS-4NgWWNrP5I8lhK8YszWGF_EKt4jsi7Ga3Eo5KyKtwdg0j0ErqfMyMbiEkzKqriL23xRTW1gWLdvtDWCzPtrqcTLxbEfTfufUU6ZedvtaQjqilyIrDge8dY5uHtmBjIvNowwvvZCv2I45wxERSauKMbjFw6ONZxXXohzHZE-NIA5ocKL0OxNv-0wm57iDU1iusUGlUIzra2s2NztS4L36hBvcRNjXp2OuJJClq-FWAt4nmcCV8N3sXC1XBwJBDP5SjtfOSUFh3p6SeaMxyHVJu5uqTRkqESLmaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=PV434h0HA76cSANm5WmgzN1IqrJSPdltfz9PQO4zYnwVXL6YyGdVvv2tn8L3HoMMCd6EQ4yDQK9yy1277NvYJTlkWNABNjVbmki7caluxF1jf6z63mzT2v4jZBUE4ftSWpuOd_vm5KqFXvXgvRun3y2sR2viWaun5IXqmbJsj9Qq7RemcUQnZUgeKiWCjQ9xinNkSFw2FEOvniaEQYNfFCFYl1wqBhqMxsg524N7PtfUuhKXW4x3JePmpz7MXQw55rLdhw95xh7aa7tz-mF9YLaKRRAHJodz2WMPLx5-Q0cb6QuP5XygZ4krn3twmHxkbhz6pkfRjZf7IhFVAC2Q2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=PV434h0HA76cSANm5WmgzN1IqrJSPdltfz9PQO4zYnwVXL6YyGdVvv2tn8L3HoMMCd6EQ4yDQK9yy1277NvYJTlkWNABNjVbmki7caluxF1jf6z63mzT2v4jZBUE4ftSWpuOd_vm5KqFXvXgvRun3y2sR2viWaun5IXqmbJsj9Qq7RemcUQnZUgeKiWCjQ9xinNkSFw2FEOvniaEQYNfFCFYl1wqBhqMxsg524N7PtfUuhKXW4x3JePmpz7MXQw55rLdhw95xh7aa7tz-mF9YLaKRRAHJodz2WMPLx5-Q0cb6QuP5XygZ4krn3twmHxkbhz6pkfRjZf7IhFVAC2Q2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=fcn8A3MBFdlEFksXSkgylh4Xu2-ln_ZDOdGlhUXD4G3S5vDk8kCvkijBPq08v65tib-qMdMLPpzUwV4GhU2ZWGzsDdaiD8lsuPADr858Tap-8vxNbZDK9IrwbVUapWqu2DCx40fhSqB0puV8kZLYtmeGfL33ukgxFodKFXQ_Kq7A4je7qysvdepdmKZm8CMgHrj9l7Zn9qDMsZrI4Ua9Zmh6PeXJvhd5wOJOWGnsqy0MrAWcZVIerqz7JcRfffpxKmPj3sPwqnKRrDYLkoCdX5muGwWd_i5SkqAOqJr5sHIbuHrOKCXsE8lSrKgG63R0_S8kmk8qe8sC9YGMmq1W5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=fcn8A3MBFdlEFksXSkgylh4Xu2-ln_ZDOdGlhUXD4G3S5vDk8kCvkijBPq08v65tib-qMdMLPpzUwV4GhU2ZWGzsDdaiD8lsuPADr858Tap-8vxNbZDK9IrwbVUapWqu2DCx40fhSqB0puV8kZLYtmeGfL33ukgxFodKFXQ_Kq7A4je7qysvdepdmKZm8CMgHrj9l7Zn9qDMsZrI4Ua9Zmh6PeXJvhd5wOJOWGnsqy0MrAWcZVIerqz7JcRfffpxKmPj3sPwqnKRrDYLkoCdX5muGwWd_i5SkqAOqJr5sHIbuHrOKCXsE8lSrKgG63R0_S8kmk8qe8sC9YGMmq1W5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=Dw2VaVyTdVV8_SFkieCqpk7AEZLS7IBZwLVAceWYz8WcffIs90utpZY_HUEg2GTtl7fqvVejF1wANksbZvh0qT7fO0DdMpK3nY6XxxAEyGabbjrMWE0_fdomnlUAfVVDknnJTOuiJRamB8nWBX0qHzpyNAC9FJZVRUkEIDnjx1LNFR9XOGpduybIJ6plhBzACNThaTkkOqYiE8uVn3Lva_ubeseb5ThrCszOyJCZ7dDhFiCRTWAXSi1C0pgWuYmxQN37_DayhK8zXL9CrxSjsCbzKxNbrJKodj42wQ9q31l3e6EPuSkjfzlMQxLbsUCvKw5anZc5rr8G10cZ8Zvx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=Dw2VaVyTdVV8_SFkieCqpk7AEZLS7IBZwLVAceWYz8WcffIs90utpZY_HUEg2GTtl7fqvVejF1wANksbZvh0qT7fO0DdMpK3nY6XxxAEyGabbjrMWE0_fdomnlUAfVVDknnJTOuiJRamB8nWBX0qHzpyNAC9FJZVRUkEIDnjx1LNFR9XOGpduybIJ6plhBzACNThaTkkOqYiE8uVn3Lva_ubeseb5ThrCszOyJCZ7dDhFiCRTWAXSi1C0pgWuYmxQN37_DayhK8zXL9CrxSjsCbzKxNbrJKodj42wQ9q31l3e6EPuSkjfzlMQxLbsUCvKw5anZc5rr8G10cZ8Zvx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=RnXUG5iXtpI2yUGvHVpcWOtzjRpqIH3KoqIciwtbc7wtKbU8qYyX_G0NaaPRuqTgDDdd1cf3OD66XmOehXQY0-cvU7xBjtLAM8VpRw3yAp2wfc0QOFUqJmZErF-wIR3CA-qwMtph6t2wynalKCzwYDBbspvS7XSCL_om-AmVOYLepVpiTlDJWE__ukYO9JRob_3UK0oI7_D-LxbJtdPU3afy9XDyb6XMcRjZUK2Wp7wWeFCRBFq7z5WIeQTfQGEqpknc1U3Pvpnp7e4LTpDvvXjtOcnvUn1KeEXlMbKZknfXOPMQOSwyD9sh8bVDRmtbwM8xJutQgE8gHd9bMfyEnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=RnXUG5iXtpI2yUGvHVpcWOtzjRpqIH3KoqIciwtbc7wtKbU8qYyX_G0NaaPRuqTgDDdd1cf3OD66XmOehXQY0-cvU7xBjtLAM8VpRw3yAp2wfc0QOFUqJmZErF-wIR3CA-qwMtph6t2wynalKCzwYDBbspvS7XSCL_om-AmVOYLepVpiTlDJWE__ukYO9JRob_3UK0oI7_D-LxbJtdPU3afy9XDyb6XMcRjZUK2Wp7wWeFCRBFq7z5WIeQTfQGEqpknc1U3Pvpnp7e4LTpDvvXjtOcnvUn1KeEXlMbKZknfXOPMQOSwyD9sh8bVDRmtbwM8xJutQgE8gHd9bMfyEnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=mFlTj0rxDqMHHa7Qdle1-CDjwmATe4K9NWKHkz2q-mnrOuFBHPUat2JlVS6rP0-PUMbhqqO4_H9MuQ8t-BOZ8Cl3cPm55QQywMB-TotzVAe51sql-taCKsUv_BpqGiUrjlVrXfFQM2_HTyirwx0QSoF8MT_fWiKNFHjKAJWmJvIK1N_ifSREGYHZnUzJxDI9SDuJoG183BuvIg0joHSMz-Fys6tBiYFqzseiOLvefpHT8L5hJL7HYqNoQxvoPSVqosrEOK7h42AbbzOBH38Q_-AUU6JBa0lbvGx7trRtSKPZvdodqsZbM0A8H9IKgXWJ1ZWZkAz63t_sB3hSrEjQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=mFlTj0rxDqMHHa7Qdle1-CDjwmATe4K9NWKHkz2q-mnrOuFBHPUat2JlVS6rP0-PUMbhqqO4_H9MuQ8t-BOZ8Cl3cPm55QQywMB-TotzVAe51sql-taCKsUv_BpqGiUrjlVrXfFQM2_HTyirwx0QSoF8MT_fWiKNFHjKAJWmJvIK1N_ifSREGYHZnUzJxDI9SDuJoG183BuvIg0joHSMz-Fys6tBiYFqzseiOLvefpHT8L5hJL7HYqNoQxvoPSVqosrEOK7h42AbbzOBH38Q_-AUU6JBa0lbvGx7trRtSKPZvdodqsZbM0A8H9IKgXWJ1ZWZkAz63t_sB3hSrEjQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKg-AlhqrHaJHTZe_hC5gQKjEON0WV4i_offfT2_bhdItAskmX3JlZnb5TTETotU4Tv74093nIAYj9LKyEZpvuv4JbUp4BzphAbMx4rS3yUUdqNGkKPZU5s1ILteIvd6E_DHby-_TcRaMRooSZpCE7RVF_37aC1xS6x98SfhAjuSr_Bki27nB-nR4p6tXFYlP3m9ksP8iHwvJMLLMVSrh8LO2C_EGVTQlJOHkRtwgzHUxQ7ZDcZoSW9on5aFwAC9DuW5QFXw_gqgraw8o_IgWthBOfllvLqTw_IbSe0ZfiBDimR0EevQjZji8EY--xvyMnpuKSfcIOXSAtch_q1fBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz4hAmligoa24mgSFgGBZtAV6ndQ_Nv7Pr3hnO1s7GFW2WXxKziGPXDtNVnSYf7KM-U_83-NI-gwqnAAy1Dp9dsTRtey7UfUZR4tQ2hrG0lwdpiEtcCwWrxn64Klf1UpixEdAHd303PzjRT6RKc_5qcSx9OtYLcrmxEfw48pzZhdzy_ApN0KhCWJLahfrtHQ0IZCYuAHxhvGNrW8uKW2kVu3Phb0p-Af7eyPMVBAROUKuyhMFN_AJk40fKcI-XIy6DIAzg2im-rUD_0bOH8aSPnnQpB_gRjpDOHsyNARiZuUHOlz2q2e81Ai6hagS-h-4ArD-5YkZy_VHS9Bed81fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX0Va1e0U5186iE9oDI4MFKbTMx7a4lL14rtZF_Emd0vdqLJyb8EsoEzLZyKNuqi8yQVTBC97jcD4bsdggfkMpi21ZH1W8Lv-gF6YRAGTnCsKizztvEa3S1C9I_0TABKPAYnU4JTZoSpXYrPox9l1AqbvifU31RG7sRDQD1uzyuqAJUWdn5UcBiDgjcvMYS-JLLV9Thn7BF5mi1GAah6CKmLe-wNI4V7LrW9upBq46pGKvfIEvrJ4P1t8ouBXlZuL1O_yW82i0O5uyiQBw_sXUqOLUskMYTqcVqAY8VcPGRv8AjdP67OaH91f1ogm33MPwnxYnDj02nwpu3mkeK76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWSDvrlnSjmDwK0qK0dosPrysPzA6QPpqYJJCmyI4XgJc4i0z0WwVwePNRM2zpG83dH0prEueX8C5Zo4s4seo4wm1q6BlQjf-HNfRMtoQGxpl5WxFby1Ka1UwjGq04GhAAfWblgNnjvvj_akYSEYHMTcJco_8npIyF32f1iWigecszMpJyo3y4WiN3SgI0InPpjg5ceymxKUkXQmnf5WSviWMCIhMxfs61x_Rmo1PiV_GeH89jfsQgrFpezUPzgzIWlg5qaeZRLIyeH2QcS54gykJUCNYvj-M04dMNzRZuwzPRry5vbIlbZhR17cyNyKHH6vQ0ueAO0IZFGg12r7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=SB4fmyKBi391GEHtaZQi5o-rs-1g-f0DylY_OaWZooPzm1oOBHc4rwRp0pcpjWa7-bzuTssvekVxGASwGLfTyH1Oqw3jDXMhJH0QVkuQyQDo8GCNPDf4ngOopaZ2JpFupYIJPQIQwiAsB6HMcw2eg26xbPeD8kwnFHqgWrHY8t1-1RAIC_43rwffVUbGHrIha7fGFx1jbhnJV6hTDqEl1u1f2lCeX8WLNKuTExtvkDOp-B7TyWef4xLtlZnU9qwEM9wHaF-LUG7KrTc9gw2hfOAvhgCJrcMjfLOABTUA_1NoOXTSyTmnJs6M8zS5fl2Mohz82SsV6V8-16g00MSAoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=SB4fmyKBi391GEHtaZQi5o-rs-1g-f0DylY_OaWZooPzm1oOBHc4rwRp0pcpjWa7-bzuTssvekVxGASwGLfTyH1Oqw3jDXMhJH0QVkuQyQDo8GCNPDf4ngOopaZ2JpFupYIJPQIQwiAsB6HMcw2eg26xbPeD8kwnFHqgWrHY8t1-1RAIC_43rwffVUbGHrIha7fGFx1jbhnJV6hTDqEl1u1f2lCeX8WLNKuTExtvkDOp-B7TyWef4xLtlZnU9qwEM9wHaF-LUG7KrTc9gw2hfOAvhgCJrcMjfLOABTUA_1NoOXTSyTmnJs6M8zS5fl2Mohz82SsV6V8-16g00MSAoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=tH0sspplmPJf38rFnnh8gp46T1rS6RsZEQ6Pzg1l_SySLwt_pnsJP77tPJX13yDx-nlPKYAVykYqu_VkDQ_zTOvadU-EVKz_FJ9zHMoGc44X5STFqToc8ovPoToPD6ztWnB92Vxgdz-rjXbBQ8U1_8K25ERoG5R4xJyAzSUGNk0PrY7CmHuwaZSeI8P5E8aQtRZUQ1HEO8L0K5CzeKjG18s36wgt_wsJ7QZc5Dt-Ctj1f-K3jE7R2MfjZt4uBXvERnHT3Oj91nnmhWQprpVLrV1y5micHOKi2xkAWh-AFtxEG31W7f-MKXOp80aWCd2ujEmhe7ha1yyp-UxiXVpy9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=tH0sspplmPJf38rFnnh8gp46T1rS6RsZEQ6Pzg1l_SySLwt_pnsJP77tPJX13yDx-nlPKYAVykYqu_VkDQ_zTOvadU-EVKz_FJ9zHMoGc44X5STFqToc8ovPoToPD6ztWnB92Vxgdz-rjXbBQ8U1_8K25ERoG5R4xJyAzSUGNk0PrY7CmHuwaZSeI8P5E8aQtRZUQ1HEO8L0K5CzeKjG18s36wgt_wsJ7QZc5Dt-Ctj1f-K3jE7R2MfjZt4uBXvERnHT3Oj91nnmhWQprpVLrV1y5micHOKi2xkAWh-AFtxEG31W7f-MKXOp80aWCd2ujEmhe7ha1yyp-UxiXVpy9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=mn1vnzEJeF7vJHSNpD-Ku3xES8-QpX_HmDOxrdjZ1jem706yMMqclWv1Hs1CCxTS_MzhAbJBi_CANPYNDasKKLOQO2vK5ucGF2RWdLb0zAdwmRcVSANUyck-j03esvXRhMrZewsHY17HGN6VrWV4cPhvC9j62VI2_WCeOcPAqCgxug0LV2hlfyyz4X_vynwb2gJbWg5Due3Ku9G26cf1hxQ69mgd8YoJMJeKDgdM-YE-wGyABsKpx1F24GMF_xmTl503mkQa8OOUK29jp8cruXi_KqUggYWfLoA20NibpVo8L0iwF5utCSd_gf1Miv49cVDwPwAEYF5uUbU8kO8Rew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=mn1vnzEJeF7vJHSNpD-Ku3xES8-QpX_HmDOxrdjZ1jem706yMMqclWv1Hs1CCxTS_MzhAbJBi_CANPYNDasKKLOQO2vK5ucGF2RWdLb0zAdwmRcVSANUyck-j03esvXRhMrZewsHY17HGN6VrWV4cPhvC9j62VI2_WCeOcPAqCgxug0LV2hlfyyz4X_vynwb2gJbWg5Due3Ku9G26cf1hxQ69mgd8YoJMJeKDgdM-YE-wGyABsKpx1F24GMF_xmTl503mkQa8OOUK29jp8cruXi_KqUggYWfLoA20NibpVo8L0iwF5utCSd_gf1Miv49cVDwPwAEYF5uUbU8kO8Rew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g34UJMfYZD5y-mERK8bwq3tTbA9JF_4BOMfhwXli5DawWAgZjSGUtbduKpZA8n3wDUb1ib4-HMWjojX3rv33O6c7P-76ghkTkwyZPNC2mHelNCqk4Pe6H1j_qXWx6krm4ofS3bk1aTWkZU8lPad6QFcGQ7VNs393CimswljIsWmVOnienPXZMlA-mkI7fFflzm2J2DdlJqY3jYdFEjmmzQJu1oPbFynKf5FGo_-WDgYYXrGzzepo2_FzcHFri--eQUQ29-3rtvh8ex0SNXMDDaIG5Y7Ov-09TbRsKa2v-ESaSFBEBkaWZ9oMYfM8Waa-oACEpiNG11aaQV0rgVM_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=pBtMpCDsWKvgxSg7jATHrI-Icfo8fzL6DXriWtPvJT7ZTCLXj6FabV6Kcuh3V6uz-3b0L34OB-i8Ji-fQqqNCJukL4DJbQ4ah9pN_dx0ZkI_71PxQvQ13w6IBkqz2rPrzj4BClZXXhN3mNdhpJaNCJ-JVTTrwfl-85YbsYwBsdcXZKmUVrlHClUuf4lIgdLQIl_4VbR30rBYcnJUrLnRE4B-XMWbX9167rPIjmMW-vaDKAPh5ZS-qmOBlPcHU1nlYmP1fhljq-ShUo6wVCnI3nwEcVGVxQ0N3u-ipLuqTbIz1lRgSS01V1JY6B9seOf61Bxd_g7__fQLit3D9FOAoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=pBtMpCDsWKvgxSg7jATHrI-Icfo8fzL6DXriWtPvJT7ZTCLXj6FabV6Kcuh3V6uz-3b0L34OB-i8Ji-fQqqNCJukL4DJbQ4ah9pN_dx0ZkI_71PxQvQ13w6IBkqz2rPrzj4BClZXXhN3mNdhpJaNCJ-JVTTrwfl-85YbsYwBsdcXZKmUVrlHClUuf4lIgdLQIl_4VbR30rBYcnJUrLnRE4B-XMWbX9167rPIjmMW-vaDKAPh5ZS-qmOBlPcHU1nlYmP1fhljq-ShUo6wVCnI3nwEcVGVxQ0N3u-ipLuqTbIz1lRgSS01V1JY6B9seOf61Bxd_g7__fQLit3D9FOAoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
