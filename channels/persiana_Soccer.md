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
<img src="https://cdn4.telesco.pe/file/Ly8Q7R0nBATnUgJMD9geHOL1M9zUhe_qMeBnYkiaSsVII3qDMYOvYP_7oVSjW53PQBbSb04gwsuV9FMH1gqlfmGYnKEeW3RcKzcovLWZWgI-sGvMdC1VwSK51ZXzOtB7qMoLuI6JDXZZPqeiUm5HrvsQ_b2Ks2mBV1hqYgytzP0EnpaZnUY0eNGGtwgQhv5wtrc5OLQRxa7zgglBe-mPabT-SOtcUJdVphkSa9h_dO8Dv8RCdHWxu8p7Ik6MJtPobfq2YhbHWHU8-5paqDDwIN093Dt_JH7MqBwwystIYPUXZx6_8SYg6Uatvkl0AUuA6kkjhJe6wKss2QC8RvWlKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 176K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO9-4nf5icscnuPbA6HlhRQ4YDSPzG632jb9HuzUhFpXu9HIcRinVAlfChxg_6bnQz_Vr4gm3dfN9O5WWQ_eRbrqJBoOMUelc213oLxFPFT_uONyZPQeZcWG5WRNU-f7Yq_wghFLMVvq7U_ziGjXU5d2PvyLlbUUatuKX6Oa7kpLKtjwTll0OpK35KbF-fWVqTuDnUGU-vCjWH9NA-fxlNTD5gWFPrJAi5gpegPVvM5JYPSOFxu-Ci_FsfZaK0amvIhzAcQm2KePWbjvgy8B42hn3G6OEhXz6CO9AcS6p7plZXbVUOsJVKq8GFoqaVCXMW75n6hDia2TUj6ESdIBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAt-u6Hkka5jF8sOWjKusL_kjLalC1FLzPPj6IsjkmDlK7ifp1Oq4ZRpVonERrMDU_ECMULI2NbJRgTZRliyP2zh2sYHDg0AqWAMhr1Tpdotq8QmxCtgDOuXaUiHxeImVh0w3MSaBaJA_xPeOK_ZgdcxzigiHPKYTxFVcXkSSweDipnXVyiMWwARPeJo3sHHWUQufmML6dj4ES0G2hg3xmCyw-S6H8Q8f0cP1hjI8PnRMGGOTVldg9p3ix4S7iEBqjnnLlCTwMj9Mxzinuyx0ARM-EzByNAaob0uyVhGwExGoZFWmVQXVaEpBOxJmAncJAkbzTdfEFJAFdTWZfwEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuMPfBZ-nk2DaRYm0dB-DXCbQWRB06R6Px_oPk4ardGlfFmIV5iPfRXYp9DLb_uUk2sxB_Guo0QfQR-I8mVgC1DcAILxx5n_46r7X_qqVOWXWsHyRXJyG7hTujfbxzWVG2bFN2aH7eVZeTUJ4NSrkFKbLWEDDcwPJHYCKVHn_mRtTLrlum6RCIYX7N-f7QQJVRkvJC9GxAr-PRACK_kAcX9tINP9gf9mWdlTfWkN3H1kSjeMfAUPptaBbWt-98SHDgLx5x-QpTmCacxzEZ3pWz77fuvC0dEY0whga_tu_EHPyYBNS3ANwV8vTPjQwtQGqdxyUp4fOVCGIZ1fgAjgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYaBUpKjjnPr1CUwh9B1w-C2gPQqCa47bSSP56BND5oPd7yVfjnFX5yuXLp0yXNl4DXV9be4ZzH4wvj8yVxQUY2G2UIUe8oywE_Bc9evZZc-WBEYO6wxDSj-zHkCNWcqm-zceTskbm8AyE6T3lfxdSQ7vjA8J1skQD2Dx5bxQLdgDUQaybj_O2yQKtEKgIWqkxlQVVaZ3gjezuzJ7jcfLZGnIRUwD-CGFmDMnP8P18t7rd2A7MIz2_yx88LwprWMInaDyNSM-xWx_tsWcCrVanBZeYDOIQJ0xHT0gL1GAxNfczhM10QOrtvVtdy9klefwl7guyOYzCWx3zkrSiIFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSu3KJcxRHAtAF73HUuUYrhOgwOypPEjNK2oQoavO2XglyJypoIb2d1mNbriimmbbCsSncCBzgJZ4y_LV80Ybpdm5L-9H3UVQdIIueWr56JHz06XpSCQDWgQoDz_6e_ntPPQQveMasyUk5YtClG_wOzKrKMLwD26YIKJV4666edwFBBfUxaOERay89n_NvpJJExGHNJpO10tYg7WGbyziRQQKxm8BXKzphEWRGS8j5DpQu0JCUnvq2zNnZjqeRWXJXS4IfIr5iD7FRvCwbIhziTRk3fpewsfTcvyY3cA9z0mSdX634AOeBtef7ONOdbgLhBKbtkTSbqb6zpUeCCTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=tEBl-E4ZJ61HpNZwumgR8dheV_DvxcHn095FAH0dv7kPQVpxw1mk3IXjojyBtn7hPSFcgTz3HYlNipZW61efMawSM3sFC9JiTPIwLyZLqyLmMMFf4uRE0HC_8DUT8dpXZeuogOak__GR_ERmcBQhUNBL4k9gnTQXBIEJfIHSL9o_ka7QLAjXD3Kkuikqh9M98Oreu1Wa8-ekZ9h5F2bj-YUV0bsOOIaTJNWxpH9iIEefADg1ijSbbz5EWkaNpJtvtXtIhKK5h6oqjuxnDEOdm1mOqT3MhQH4AyDBg-fbcyWscRNkianDR2BWg92clHXsatMwl75d6I7eeUAc52yGYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=tEBl-E4ZJ61HpNZwumgR8dheV_DvxcHn095FAH0dv7kPQVpxw1mk3IXjojyBtn7hPSFcgTz3HYlNipZW61efMawSM3sFC9JiTPIwLyZLqyLmMMFf4uRE0HC_8DUT8dpXZeuogOak__GR_ERmcBQhUNBL4k9gnTQXBIEJfIHSL9o_ka7QLAjXD3Kkuikqh9M98Oreu1Wa8-ekZ9h5F2bj-YUV0bsOOIaTJNWxpH9iIEefADg1ijSbbz5EWkaNpJtvtXtIhKK5h6oqjuxnDEOdm1mOqT3MhQH4AyDBg-fbcyWscRNkianDR2BWg92clHXsatMwl75d6I7eeUAc52yGYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXgTjAeTpQjyeWIi1HdnbInM46tXTebLiz1OdSB6x1wgYd6cItzD0-i0CzkF0bNwuj1MGO2TXl79v85vB2vc37d5DSDURi4V6smKFwgUhGTkbHsAAJwPOv6wrC_j50UN3xt0fY3A6i3GutzkiuhCB7776tYqBexWUR0OoZ5xLsNgqKUSI-qNvvQZqoZBtDf7uUpyiXidPsG3UT7UhgTAAN-dipY-3ms-qDN8OEa4A_SOf3OX39_4QDPqsJtK0QA1AuNIC-PDnHMLPB0Ou4qwaMoEsd2j1ZMjnjWwjuo8I15S4nPXYoNDpUzACbU8s--5gre0oD0qIeIedXJyVWxqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWllpba6CZmYLhCKBmECvgQmutNxWh0TbWGbhjGAb9PM0jfAATT6v3dAUZDbOZP1P_9EbPpf9ipZjh_7a0z7RHhCtrqqU2xm7GEFvB2hVsZTdPp5ofCWKu3cKeuUixYVUdbz1arDpGKzQV3sx1Op_R9yGSnv9s79ifsANKIIfYA6dVxbGi6X1b3rKlLf0UjphffdGy0s8FLUdEPelBwhLViXb-8m5aXdGToWi7VytvBYiNrcyC_ReecgQPBS-Bs26SsNY_zVQSgzCgMy_AfT5KuAmdxZhk1E5h3wUQXk1wyU8IufHVJcyW_rotGlRfx_9OWxA2fA-Q_fixH1lyg16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8Eg-VnK6zXDOTRKaPv4By0BFApAs_5dLzn3rh68zGa8YrMFccpJ0ttIDWAl58jLNBK6li7YsCCN0_thpyG1-HqLAa_TBIzY40QbJkAZtXh7hoosoeskV6NnS1cI-YQYH9qEQF9QGlbeRygGnphJmw44c1Un4hI4Mg2y7QwIE2_v0H0bETLv0XxOdi3KZba0eL4w3C4OyVhyWgdNfUHpCGqohJ0prQokO5hec4kSke-lqVnshTDtxhB8bWMTswRoEAElD9k7Slu1jszfDzHDdi01Rbn-GeqkB3b9sfUBZHNiZm6mWdTuvrsJ1CEwNiHJpnJn0dnHRlnl68fuO7M2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agYM0pcE_hs8pG--CK4wbBEifipBTVFutv7gUY9jgUQv77nyUBlE8i9fGgTf23hw0FErXoCJjAbRbky_PUdTyGwrvsOqqHVK3V9Jt1lvQjbMbuMuI8GZVR1q7ljgt0MRIrlHHbwujjlJSpSaQphx6Fbl4GrRpdlJMBT5lk_EG_yb9TwVucfD19uoLfBApvtNfkA5gA6J1H9C6VN9h0ZFg3vTAAVx-k9H1uxUEqAg3dDX5DQz89sszNZqGQoNf5-c3SWc0BaWbZ4O7hkYN0JOjhwOQ1wRERifiGHEdK8PL4GV95gAi-KGflsSwmxPfQaCqIM2iLL7SluxvlD__Q5SFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=bUuKbCkydOiZb4FWt9J9hIJZ41rBnlg2klDgMuSVs66SsWziecaBbDNYomcA5lLFE25pm7Nk8zAh2FaQz-E5c77CyNI7IHQuFOameqY9sheQQqLwrpS5MNEGNq9SHaVGKIVYpc6wuu2GonDuof8oHFA5sPs82WxlIK0D2f_9hQur-HJ3jcEkD9g4Xvh7TdaxWns02NJQa8Fotr78UvczK4_YUJ7Fp72bAev3AkdQcI0P222MGSPp1vRorXkdEZebDVN94er33uZC0PxyqRzM6hg4AvLSbpUphpDW-4eZ0erQfIC9-QWn9EAM3FKleMju_NSUS4pxWQVzuGrSXVb3VkES7pT3VW86KXHeIY0DtCln7IL4kcWm5fLiT3RP8HNHDlmekI0ErNbPxzVsnJVbYAaZOlmsLXxLwqiTNlKlIzyhuEi2zMWrQSpTHpIb8FIT8kF5YujEFXsUTAy7bU2yWxRTjqznemCJv8-LFRuOMElnApommNd-hVCszQozy8pndt__fYu_GMwq3T2XsQESb5bfwVv27kYiVdL6YGgrRDZbR-66S7hD93Y0TEbImVWAxFvvj9fSkL8JlwrjClmC6qt4oqRbB1S60rcpKzxXAXFE4q_uv2c69bVdwRaU8srmy_ol4j0HXVeXPshf7QhyFiU8ltI4ceGSU0UJErK1TbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=bUuKbCkydOiZb4FWt9J9hIJZ41rBnlg2klDgMuSVs66SsWziecaBbDNYomcA5lLFE25pm7Nk8zAh2FaQz-E5c77CyNI7IHQuFOameqY9sheQQqLwrpS5MNEGNq9SHaVGKIVYpc6wuu2GonDuof8oHFA5sPs82WxlIK0D2f_9hQur-HJ3jcEkD9g4Xvh7TdaxWns02NJQa8Fotr78UvczK4_YUJ7Fp72bAev3AkdQcI0P222MGSPp1vRorXkdEZebDVN94er33uZC0PxyqRzM6hg4AvLSbpUphpDW-4eZ0erQfIC9-QWn9EAM3FKleMju_NSUS4pxWQVzuGrSXVb3VkES7pT3VW86KXHeIY0DtCln7IL4kcWm5fLiT3RP8HNHDlmekI0ErNbPxzVsnJVbYAaZOlmsLXxLwqiTNlKlIzyhuEi2zMWrQSpTHpIb8FIT8kF5YujEFXsUTAy7bU2yWxRTjqznemCJv8-LFRuOMElnApommNd-hVCszQozy8pndt__fYu_GMwq3T2XsQESb5bfwVv27kYiVdL6YGgrRDZbR-66S7hD93Y0TEbImVWAxFvvj9fSkL8JlwrjClmC6qt4oqRbB1S60rcpKzxXAXFE4q_uv2c69bVdwRaU8srmy_ol4j0HXVeXPshf7QhyFiU8ltI4ceGSU0UJErK1TbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22699" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNwtS7lnuEuh-DjoMGeQVg4xhV6RSAWo8MJujpp1gJzzZyU2gfLzIv8Fvjt6zB-UTzZllUVZRvvFNIdVHZr2RQUkxhdcROyeK-BBlWstFXgHYDNHjeCuyZuID9yHLLG5UD04L4PHoYEiDKYJ4F8ci5wPbq00C6v-kwdk49EL9GLu7HBEBK2xJ6wM2BV5uGMXzEdLiyqZhLKD1LPmpAgSqk4Cbm_hLcc-buNB_44sTfpVySyfcjzCNIRJyAqIsupqdH7GubmGdmiMzsK3xswAxugdr7Zav6PwmJ-E2F15FulrMEUMXGZU_TSPTzi2LRXgNzgX9TTDjJ_xXxilRbJ6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-_mjC_aP1qcHNGN1Q9n--DWU8NWP7GWBTuqtM7vghy7DG9eUd7gaZwdihnY9BIGWYlDYvfcfVkuPIrMrrSSvm1npLOH_SSftQQsuMFVTlWH1gwgxNOxub08F4pj-xNRcO9LDvtq5GjKWo7CgUf4PkSNwuW15VLwDT-khRWQopuIztqCRtEDZh3E2mTalYwy-IRrpVC-oOWgIS4h12sJ0zDBBbCY5qamAAwQ-Va4H80wP78dc7yc0MU-bBvt8jdnj6h0QQ1cNxDju-S5sdoxULDgZE7-htY0SlBxa4GSamTKfRMebZBm12Dl2SrG3ghw_Lo0-LyXc8Cu0yN0deBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViwDVVTofW-QyFaCQspQZe94UO8ZJhHbRINBLaFJxa-ppURfzzulmCi9QnyAT9G-20Y1Eo2eyTrCGrLlhL04qR6n4ogUxkrJip4KzQumUc0DSkzkhPoq_GWuPbF4aDUwi9E6SauL5Of-nqzjG9Us7u6F-d0nJ3xorfDF6h8DZDoOews08Mzjt2DKCvDxOhZqaysRcWr6B-Bk6c0_1844bwzTD9PHrB7Oky05tVvdu7r8zJC40mV_soPNvyLFgT2mIqz4sFk3Jr0qXG1HSZtv0hiAEm8PpZzjLQx573wQs1X_oempw0z-_F4EOSKRPbKD79FdtFhevdI4vq-hyoWgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmtSga1dH4MiOfYH42qP6bOwJDSyDmMa86OR6Zy_j2BotHKYMRiY-E4I29pIK02Q7tdPWcXR_m1NIo_VU6aGglpdpAWLCC0FVaglJX3gjZS_E6H9Zrin1N5g8i5S5pxOs0hjhNMRnmwF_nJLgMxrsCMh_qzxxY1M3cNqB7aiwsJwyayN1jt2vhKr288g7kxYvWWi_rE5xLnKvoQQiz8xorhPlhlrgRwyRDqCKy5M4VAGrGJUIc0FzkUc-S91DJSSkmysURlqKRgz3Dxb2mn1LPKS1a3Pti_swOadRawXrEeFOx2DAObFQYNFG3JT1dq1BG7R6Ua6DxNJGKtaam32Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzbPSeJk5AoTjO-jejYBh7-DEcbUVFX1ivFarE6sj9BkUvax31j0yuyF9guS0A24pQtyOYVE7cnE9DGCO29pCGW8VoyvtvMxRNa14zMBdrP_mJtgfBnNLYNDrz-Xjf3me_PoPVrlBNqPE0Nzw85cB6vCCjUIQdGsoTCdQHsvgSY2kGMmtKt5OkBn3RnPlegMcTAPkbKWodVwcRUg8I0s7-9swadZ3_ZJJLO-Oom-hNP-CFAqbb7gASaqe597L66U-9BcQCuAGUAYXf3PV8Wb_MzZ5EyY0IuKK5Mw5vnyzftXM7bj7wEB7kOhnpuKfV85sAcUeI37aSX9xWX7CTA3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6HEM-ixABX2xogG7uZC5VDgQXBpnSeHmgZ63N0DubowIqSfdebXYJa-VRSzMqpXG4BKWywVTkZBMQwREqywS7OPBFcZgVAEiDCUEh1cdIANPQZdS-_CG-kKDRAysJ-NAB-2KIe43oZW1e0k1LzzJEIHXetpLplei2gyidOd6zmmUEi-CJn0Lk2-itCCDD-vbjAxxg-q-r8R0QCHc9LzPmKvazU26cqJrNj8mTgREgztVA8XXIzMAXvTep_EyygXIT7PBqrJiPxpZVdOVlX9mgcmEfVX4bQPY7DEHlbH3RNDGLEjuzYsh3I888DL-Limoty-Uof6DUkaodYThAWzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0TjJvuq7U9fUDOCYOO4TmZtbXQe8QOKFfJpTXClRYqDdWwX9xwKNwYeDlAu0sv-gSstHfffqFxMX6scKBqLGIB05TC13uQtu1pO5SlBoPm-OwT0RnK2QOFkZ85b51aMPum3aONH6wn86I2FvI95-FfaK-KnKMt0pYG9QCRXhKPZUb4xJ5Vk7caSU4UBALHyHUbzIADjeWbQivsT12prfOj8VNnzHvsykggopLftbKwrJf0V0uXGindtEtaBFnfVk6yg5cZjVs5ZoV9FSpUOgRZ1C4UOLbbXkBsoSJfNDNT4zo_cfiR8_VT-LkRdl0R627Nqn9sN6ERJCSv9ZDPGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=TiZ-v0iMw8rh8HUKeCkRlvEFWRQgLBdhO1Nbijm_KCF53cbNYKFNiRVK0ZK9UiaUiS78V7nf8wHxBWcPp0Os0-eBtEZ1CS4xCcTNisRq-sqIWMFJEYgCMxRcCP-lEmUPi_z45xbDn4kwBPVF9bfdXE5NIYquf50Ey2mCWjDq4SEJMUKIJofUViQeuV3hr-SzBKUZVY_lbz7-uVa5BENt6s9PqljQ6wkj50K7ffjgDtKiYTucC39dRZ0CjBHWGzwUfH5Zd-MZajix7wFoOjHFMPl0rU1onSo7_AIW8w0o6Y91F_2IVDAFecFW6ISbcMadplr7lfs3VSDl_1PDKw1ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=TiZ-v0iMw8rh8HUKeCkRlvEFWRQgLBdhO1Nbijm_KCF53cbNYKFNiRVK0ZK9UiaUiS78V7nf8wHxBWcPp0Os0-eBtEZ1CS4xCcTNisRq-sqIWMFJEYgCMxRcCP-lEmUPi_z45xbDn4kwBPVF9bfdXE5NIYquf50Ey2mCWjDq4SEJMUKIJofUViQeuV3hr-SzBKUZVY_lbz7-uVa5BENt6s9PqljQ6wkj50K7ffjgDtKiYTucC39dRZ0CjBHWGzwUfH5Zd-MZajix7wFoOjHFMPl0rU1onSo7_AIW8w0o6Y91F_2IVDAFecFW6ISbcMadplr7lfs3VSDl_1PDKw1ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW5ZlVoU-oZc6ZZzt6s6FVFCR1qi6l_zRV4RX81Xm9t7ByZ-J8dbQMqlHyjAincTkodxWa-baZQB7KSsPs-XbUK8fwoApPrXlMNSMyvNGjBdONF-Ew9eOzHEYbM00T8jwMVdfC46j94zULsXcgl1PjZrp_nnCE7uqde7LRyGkwitSmZznoOmK-_0YhElh1xx6Xs50TvRHHnAgbWzkgBRwpvdtg1PfDSiCWIelzzS-oAfEMOmjbgPgQBNajpFABvYTwf7-zBczr1UTFKb5K7G0WR16kKlHrTs6Da6_5B4_JcQRLcE4S6JSYlFoB7MqJQxTCxWlfCpA_Q08N1oDbKm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGfmJgX2ZKyFHTABL0BTAj1aeQ2S3SqgrGnJ3Iw7T1wOZ4BN7K7SQdaWrebYgKZ_fKj6Xvsi80CqBisAspnqSaPo-sin0RU1j80YvVvpZuFeNAzhOD-ezr-4KkiRJGB7i6524ox-OdEcvLgyvxL2aWpSS5-tBN21Bra3A_ey3xrMZQQfvYDZPEQTG4VQicIfvN7-LPRSC9YpnPmj4sUbeHmrnqn8k875QV8iAFRUSKw7RpITlgyID6He1I8ZfOQeun94fc5ShWe4rcBp7l0b9Ruxq33tWf6XyzQETClDODmUIvy51XuR3m3KdHUuaM9zzHp3fJsXJyVLisn2XLu7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsGxHBOv0EcIqPsxz-ikA_bNGdL-O3ZWfrNLlfve5I1uMDzJqBt4qskzuR2xgkNBH1kSfKew6gBgegyGr8paINYZ5J5pripq9GfXAt4Udn7UGqhIXhOOLSNIPLEJ6RlZPWiwEVPXgZztXnV3x6uButSck6_dDMYMMFgR2UizE0VN6Xdnz6Kvn7ivpUdEOIawG2qyzaOC5OzdWAk3zk46iBEeyDNLDqxxnOi7RtmPrONBNtr3bn01fh38DE0aKGguBaZOi1iqkHJ6Qtm6nW6HXTY3LvFZLLdQI5YOu4h6amMDtv8UHSX8dPICNtRWGO_9SzhSlnK--YO9MKquroG7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=cNTXpjeIVPkiY7AczmGDWegwfNYBcb-5XPVyZlX3EwcN0L_DQkK3C-3nM1xzh6Sn3Vbeh_6fscyz-Yds1sZ1QYua-I2cA6xfm2T3rjB9yFfT4E-fxCzU8406RzKKy1ySBDDsqsh4cptBJsahndXlmYCXTrqEUlpM9pmx7m1Ag3h84tijeUVbrpu33JeAZB38Wc-hK-bGcwWiy1BzljEAjVknUlYXB23hYjcXmL9uSXvKpbUj9Fao-KB9ewe3ml7tiLUBaeK6Hpz03HwyOQvznZbe6r6_gIY1iva0PRHihpP0kS0n6v2TbBvyM1TfjnKLBBIbx3cJSUOIE1ErMFM41g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=cNTXpjeIVPkiY7AczmGDWegwfNYBcb-5XPVyZlX3EwcN0L_DQkK3C-3nM1xzh6Sn3Vbeh_6fscyz-Yds1sZ1QYua-I2cA6xfm2T3rjB9yFfT4E-fxCzU8406RzKKy1ySBDDsqsh4cptBJsahndXlmYCXTrqEUlpM9pmx7m1Ag3h84tijeUVbrpu33JeAZB38Wc-hK-bGcwWiy1BzljEAjVknUlYXB23hYjcXmL9uSXvKpbUj9Fao-KB9ewe3ml7tiLUBaeK6Hpz03HwyOQvznZbe6r6_gIY1iva0PRHihpP0kS0n6v2TbBvyM1TfjnKLBBIbx3cJSUOIE1ErMFM41g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFKmv66Mnxr4DS2tImgBLmpsTofbURiEGz2mf1CpjqqbAnMZW54z0cLJ46fx-TM7V6m1Wrwv88IAp1_JJ6gnro1LATJ9SpGqhBjPCZ6Za5qG3bbU1FNWwT1dvkWkkjFE4uJ94n_sLYx0voWY8smhybsVm8GLH2YgL-dCXzLRVnNW0ncC-o7SKCqeRhFgNQKZeLlqm2cmrAb9krqAmUI4aU3GoKr19O3EAw3baaNt44-91R9ZdyH4GWun2Y1yPrAFpSQ_fIkoWTemvH0YPrff8mD2UAExbkcx3aF7KfYXAiOLibdP0G1SOjVG30lW6RKb355dlz5Cly-qtv8FxKZpgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=FYLj6lMx8sVxDA48Gcx5-4S7ZhlpiKOi_zAM73bqm0WzTm6Rqqrlw1VnurZALLZKZrLmz83eITHP1RIy8Fb2fyXUgKYHVJoh2NabAieMfSTuEFQbI7BYmu_Ult_p4_a96xdM4ijUo2i_7pPbO7ZHrc7OAXjG1qBaehIanhPWTAME4yH09ZGNalV92PSpyJ_G74yURojMT5HDA64mU1WQtyAxh3znpdzqIIn1_374G_Lwnv578hGBA-LF5boG-dR_hAYozToEnHHylEkMbcZaV0Eor6pkRKW8LxSa4ukddaIse_A_6ZjCjNTrY27M7rliOtj7d7WYZfo806b_lgh-Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=FYLj6lMx8sVxDA48Gcx5-4S7ZhlpiKOi_zAM73bqm0WzTm6Rqqrlw1VnurZALLZKZrLmz83eITHP1RIy8Fb2fyXUgKYHVJoh2NabAieMfSTuEFQbI7BYmu_Ult_p4_a96xdM4ijUo2i_7pPbO7ZHrc7OAXjG1qBaehIanhPWTAME4yH09ZGNalV92PSpyJ_G74yURojMT5HDA64mU1WQtyAxh3znpdzqIIn1_374G_Lwnv578hGBA-LF5boG-dR_hAYozToEnHHylEkMbcZaV0Eor6pkRKW8LxSa4ukddaIse_A_6ZjCjNTrY27M7rliOtj7d7WYZfo806b_lgh-Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7bLglBvVw6P3MrNsuU5lnVttuBVfaGD7i3hRSrP7_LUabCMMzZCqgpIOLqTr5KD9BjUpr06D0CbrV_EVfm1seugC96jOnxOcc9MekEbvFUt9U2sNSQ7RfoRi0xBm7v_LLM9qGw1yYxxTFWYRdRKujtVJFZhhvj3FdWERUrgZtyz2RCwUxexbGW9eKvFa65gTea68zTT1-tCb60eQMXL-mEtHfXyuR0cuobHHe3NGfYq-BL04PfFUBFjIMxDR09fmkhzROU29_V31EUSI-104XxmWMReg7sdsRuUMzxq3_xc6RMOZxeTUGYGkNYnKC-p5wBGFPKTDCJMbHeI5h0r2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=JLvxIk9qjlko4VeCsZVs8pQCfi5_ZMM9h6ilIRnKfY7M1Gp4kcRrffRPw1Pe1WxQh76O4rNOfKNIDzODBjDXCR2IWkkYMFvHWC2wni9i4RbYARgWV3cDNYBpxvTrO_84kiOHlbCx6YFzzPxp_Kfb6H9Fi3GRrYpbQeR8kL606UjxpO1-95wbQ-KlJtz7ni_fnOaDxFZNKelSlMU8jlrUwyvWSnHIHvPAZc-QDkjSJMUZSXYAgKN9YeS8p02SuBsfejtb-tTrT0RL29_aSdY0h8XQCkNnPwRWBN5EQ6mK7GzjWHO-4TWQacJt2qjsnlVTaPTHhItxFHKP9R_HXQ1naA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=JLvxIk9qjlko4VeCsZVs8pQCfi5_ZMM9h6ilIRnKfY7M1Gp4kcRrffRPw1Pe1WxQh76O4rNOfKNIDzODBjDXCR2IWkkYMFvHWC2wni9i4RbYARgWV3cDNYBpxvTrO_84kiOHlbCx6YFzzPxp_Kfb6H9Fi3GRrYpbQeR8kL606UjxpO1-95wbQ-KlJtz7ni_fnOaDxFZNKelSlMU8jlrUwyvWSnHIHvPAZc-QDkjSJMUZSXYAgKN9YeS8p02SuBsfejtb-tTrT0RL29_aSdY0h8XQCkNnPwRWBN5EQ6mK7GzjWHO-4TWQacJt2qjsnlVTaPTHhItxFHKP9R_HXQ1naA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOFrC6ESvaDhiWJBAinAR4tL7WVgJ0sylZsHeDK6chA6uVHhNRc256qLAIcvLKLkPnQS_Zcq3fX4ZWGX7mFmKdCwzQNF8GVC4gGXfOJljBjMWe8N5k3RLVmDUAMFFg8vNcQH5gIaIwKMnlPVP3-AiONNr79rpGu5do5NDyIiyHuyrkVmeEsXxGAeqKIIp67UhbyMSfMq5yZEV64jM6CHgbWIf0h113rsVYS_ThoYjtTjMU8Ilhv28qNZOtxR2cJWwD8OkFYKt5ufZV8E-lU1xF0hqwaJFVLmrj_xNEygH9OrLFVXQ3rU1CWGv9crcHfpCxq9wHeKOeLmy4z4jsIO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEmZA5E1ymHXYdVlGGyTkUfztpOSY_ply3qxXAkgddF8AbkRYd_zceh9xcQXxomRD0ugu_0HvkqQc9DTi75hvRMaqUXnNnamj1EOWbDfUMyGvHYTJtiw0FDVdtIdkJLek5i4MmIpiTNtdoRc0p6cZO8vkLO5fobHqSTltW3yEoJ6_E5txNGF8DbTiSloEHKsUm58pqQHKrdo0VzeTpFUymHuOG-4yJXunt1jF1SYrAFfXLgD0UIRl869FIs2DUjdzHQbiqIiDM71ePjftN24uM7__p2GyKoF74Q8hTZ4wxADSQVVHivsf8qIu3_7qoZFi5uzTVWfwszKdVJb9tBqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGC0SpSFQVOtsTD3unkf9ieuI25truksV_kfr0UYSkKqn_tQT-dNMhDsWgCZBXqtnbNqUNBUvQCaRxlrgs7bEP8ULjq9sRYvifGTlEIH12QItILh_U8UGJo5FCgN_S-7t-NSIUhSiJeLqBisq3ziOACP6i7Juj6jgRor1pZzAX73ctcP3-cdGe90DqLdHel2uUr92bWjFKAsJ6NzZKR_0aGR6N3ijQ3u8sAoeosMmf1_CCg2vHo4YfgExQs5K2lNxrh_VJXvGoiRzHBbsKlQ-AjhfysLQI11zKJdfUTOSHuQj9YwJAsKYu5k6mH0kWw0AgUKuEZPMHE0rvTGkCEThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHB6HLm9nLui3l8_3EoqQ9RCmClejogdSE-G0JK8u0S6T1VFB1oOk41q6GR4suobR3CsEHDt3qcLnPfsGB_wgeg2-lkikXaUBlKgFxAFojDU-uyZxawX33ytruthQ8joGTjHWE_XnRPxcjP5njylyLrHj83NDEN3MG1aWFZiPku3UqLPqT88q65XQaZg_wXf1jcxecTl6FgXBhL3jYUVlWmG6a2vDXA0boVTBY97d6Htn38XRTaqUDFUvh6HLXsYoxlN5KP0scff2nt88uMeBwpRU3oSqnTsgqqJVWGiNFjjPqB-qujxk6XIybkGSQUN-BNRE0JsqFP-h41_yO8Qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=oB-VwUB9XkrHzEmtzvkhKFvPJigWC1WNDsV5krvn1TgeXT_r1lDuksy39_ay9xOPVAyIl_imGuT0kaercqbcI7QfjLnL4oE1o6_MpJ0Xicspv87itYb_feJLw-KZtR9ZnuLu313x6Y_VC8w-XCYEMUGHQTaIEi1fW4-tKT6TH7Te_wh3sm6I2VXO3-55tj8KacW1grnF0rPFnDLg0XJOlFRJ15rJ9OkuYitegmj4MNdqaBuLcmRE-ZcltgZlRP4ozRbkoOVV0jO6VWllY5iHcjwjRiS67Jh67vgwbC87TJ2OrE7ySFjn7LnGVueQ8ExPjycSLlS88fKduR5yrf3lzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=oB-VwUB9XkrHzEmtzvkhKFvPJigWC1WNDsV5krvn1TgeXT_r1lDuksy39_ay9xOPVAyIl_imGuT0kaercqbcI7QfjLnL4oE1o6_MpJ0Xicspv87itYb_feJLw-KZtR9ZnuLu313x6Y_VC8w-XCYEMUGHQTaIEi1fW4-tKT6TH7Te_wh3sm6I2VXO3-55tj8KacW1grnF0rPFnDLg0XJOlFRJ15rJ9OkuYitegmj4MNdqaBuLcmRE-ZcltgZlRP4ozRbkoOVV0jO6VWllY5iHcjwjRiS67Jh67vgwbC87TJ2OrE7ySFjn7LnGVueQ8ExPjycSLlS88fKduR5yrf3lzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liStxeNXOTqdxGavaE1P_oQuucw6_Ossy583XQGJA3sfSk4ncBOf3INcdlQucdhvB7hm52cBc0tw6nEsiI_gGFlUwLRnG6sln7NuGUtQFI_o6unIEbgxRiyOrAXM_kwWUewrsssR3JkDuOTdTkUEJfKaSjxFDUrZ6OnjtaI1FogP2RwKE2yFlcXyKnGWobrHgpCPwYcZMYAK2WBY-rnCwrH-vNMVIhbrP6T4_47V4k8j8YPHu2DONVK4MTxi5_i-tt4JDbdKLniiZrQ4uZLaFjvUE4WBto-kT2p10r34hzKItGNbcGWsglkxzt_3K3OpFNUaUEDq-uxX13ZxBF9vYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktpWw-bpm8FLKYmk5xDFXK6qqfKLZVi4kiB6yFlusRljsln2oXNi4P_UlV37HgmRYGWeh72P9GlZ0r0-OjGSszYL-gsubFNxpyqyZcNUZuPy_svlwTLDjOHhEUiUMWjO21pYDnfAFEjeQbVJ7Ik1PHwOstQ-rSX7D1j7WaR2UUErkJ-lyOZaRoLqgJlvDlaSJBBs5cHp80gbBwfTp6qZh55ygPMAO2yEqd9jC3aI1HY_YdKtRDoR5XAzeF4BgiMVWrVM51IVcSeen-CVjzxbPpMgEHtjEtlonNd3Fns7iyJyCpHoBmHiaHhYM9zC3NaQwsvZVNU399LnwLosBUjaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqeC5wrZ9IGYXrCgtvhsfhjHq1pavCU5YI1GKZ8TJ7pgcWX3D-imnf_Rnf-rLaYgC3Z-G56bZ9ZTzMKWV8EI4eP6omJxauu6K8rfKZW3bR0CYESYEIZdTRzbOe8j1g1Qv0QvD1mKb07YYM-dTHmUiVqWYUWUn9LIVmh0GMtHWcp3PTg7IDjBkwCx_E4c-28KF_2PkEVChzAqmwaWMTCAGthEa4nXSU7BwpXMQm1PG18PH6z9FqcKYWXqhPsrnNZ2BUwpqs2NBULYEF43e3c70KwXGAy7IeboOUXhASjEcDfzrSoBPgNIkk7WQ_MfPqiG4exDjAYdfaarQTtK7AqL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQzloDyEpRkPdUlciFPRBKLmdoZhjZUQbjTwAHuJMsbRCwsnLxCEXPgm2WZ1JhymDalwlEfM1tmVKbFZrCtsPU5wgckAeLOVTlzc4MZNFYoCCMWmqjsYxlfEoU53hlAE03oP1i6WoN8R4_IHYl2vIR-TKCK_Zi6rb-7AFL4kLDASNsAy5AGQSnjLkLS32dwE_TDMxcSrUWZxdGfUryoWPn_kYKMEfM3El32pgeC93RuGi0bX2yMA2YthDF1xArYEPv_b9KROmARKJSiEsUlSsckU56bSVJtIwKYG-QkSWlPq6FmHugAaKUDOBg6sHZ29YEPd8byr_dDxXmpXMbhAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1sul9tixyqFC0pnlFgXE-iqyzQfGAi1XtdXMrFYJW1cPb4ELAtKk7n5AGvXeVwauasXv7W0RDiiGbP9Jx8apX5e35bdV9ph34k9GFCDThnqknFFUk0P6WGGzlxD7r9ptYV9DfzGS3s6wIQ9w8LPAsIwT17BMo94DQ5qC-4y7Fk6GCavI5HxnjJ8xLYhvpItztKk0K6WdiW-O4HIgH9TYxBzkK3cZJQr1hJf-1tLWLUfuoP1moVwHuhR1BlUUgdggIshQs79ZXGXqCiQi_WdavcpLMklytjM_zt0GMQV6GGcHgpHq9YMxefsJkyCtlH3yarxxLYwzS9S-lSzuUhNAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eon90cCDtPj2PZe6OkNDK0e4xRd-HNEfDvHgS-PmQ3iFETJZBJvZxJ515LcZcxQKznnp8yiZOrBPJIHJZUuZaB9KVKOKCt78lGjNtUrX1OkBAx4bVyG0sTkwmtfU-sqniIfQ87PG8khXA-L3p_HL1daNkRdTCupxg2i7ezHfv5xI7hinZJjB5xbLEnSJUhF6a3S9BwfxWliWOo7F0cFQbfA5A1XXu3hf8h1RkjVJIz3hybWyQGE6i5wLwY8pd1Gg9UjrEM9LCOBAdiexC-jr9js4vJS5GMPl1C5sCY7tAFV8iVw_7dP78kKMD9OWWqosSFP-k01_tRyftyt5lOlsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9uzz4FezbCVJlDuWGkqz7JhxKkERyAckx2i2TIwJDqa--7ncMwQYpyRS8KmPvMDTdmRWq7JiBfaqQy4Jc1vmbB4IBTRxRHoyZVs7OpyvxKQSB8cBuycm6GBdPlmsRi00j5SdYLxE6Pq9_oKlE84ouqxhhb2BWKoZ1uMBvA90e5OF0qEgn8hJOJINjfwunrRTRUdaiaVQgUbNeoU3MTPiUq-W3gwenc8P4V6c5RvgQkLyIWcynXe4MwLhwBgpCMqHA0qNmF8asV-6aXICZT1pwEBcmo9n6YrEvpI0CU1B1KQplUYXFbBJALuKDRrwrW7nCsrbKooCCH72P6tTnb6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzzfWE7Cb3oCwzXrMPr_M1s9Sv9aAjXoBZAn0MmpBc9f0YXt1CfXlV-zrwE-5XGG3c7jK-4lqoYUzPNxEDuB0LANng-ibYol97xlb8XJpjTZHzDXgNV_D6RfF9q2crPfO-ucW5pp8PXIAhXuanG_h5sN70BWOio3tUaDE-QP4eIpTA7X7--evF5GPrHholbWCVAJ1b1za0QLcAqoAbAMh5njVGeRnckSVnhaFi8xNd3g1gGrxjEu-3EA3an4kJC23Wsb6QHjK0Ye60GhNbjtq4yS1_OFMyUiPVg-Fss7zdy_sNsWt41g9dyerS1R5HvJiJ6vQqDZnRzOp-vFvLeUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKnb-cnRS7xy6-FjWU89OFJXCP0xRuQ6THuaMDe2TpMkx49TJacWR5YFRdvW9M-9nTRIObMbuiYUovd5ArD_YvB0cKGs2OYhWCmOln72JNxjUCyme56VODMv1xxOYCHUra77sgNnP89-dxtiTzGxqBNOLUovjR3hY69-ok4fOcAB9XdgXz-af-L2ezW9npiet9FILT3Yq9lujM-4gBy6pXsVt_tc4_--wPqy1xz5ZtlMYUFv3iM35FHEDeqpwMxoojEtxI-8OjBlAaEzSYSXWlzQsL5jFj1hho7Sx0UuxuOWl54-KcxEB9822fZXfWWotN-JghS4LXVIGRrD3y4U1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3MxIlbDnd6mUMoKE5wEg0vQW-P4bSjy1uDvyYCAtEZTzSywbB20jGfs100Yc5a__0fCLasPktOkqPyGKweM48Cddvs9mg8Sj9iHjWlbVN8_ySn7Fe9aEDXnmRpWQtm13TCrP8FFbUybJHF4NiFhaI5ylRcicqOkenEJR7LZHgmZK3Z5dLGHkhe1bAe4-DB5NoDNHcCEhl4kRqeCq_ry9DhNsIE0azp15g1uYjhZkWoOHKZzeVL5riWclreHKG2v5dmr2NlWHDVL8fANVV3zrZMR6BD4_gFsQ5Idijsi_vULyMRzbe1ddi2KE4pAopNtnZ_b6zRDYQy1orw--7itgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgYNQU3yayMD67_FoaluLpr7qglg_m8V4Q7rwVmIzPcg2SHtr12n4qWoJjDzCSfepuJI5R6cNTMxlmzlapLhUr7XCLZ3UuCR0wpwfcQh6xyrN2n0TCICzDl9YvQFUwOyCsy1P2Tk4W74nT_r5mosEkLvrmKyoFii4pgpahj-OQuJC92D1yfBlFzoAgTh9YzSiuMS6jrBCXnjm3JJM4e8qZ-JAcRgvqkDtSvU9VLpFNjffRhlC3jlvs0r0Ztr9DONvM2Vra6GBIQFtpnFHjq-wxDeLQZ6EyW2bWWDFvvanx5-PFFzEuI3CfRP2UDh_oMhl8G7vAd8H7gVxhxM-vtdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRmtbgyVpb_vcrgRf4Cujh1XmKAd74Ijv5H5yssQLpRSsGYIq3R4yJcEHy411rNOCXtAKLH8bhBe2aRfcplekpVedgdfelG7htIM7cAJvrEpZDmezimOg70VJL9A5mNDD_GHXwwfdRbaXoJ7zN9m_PoTKUms2K95P6gdxgd4PR4vkRroVgicdFGwPj4TrBbwc_4YV2F1H3l3zLEomWmXK01MCJXhomxFraPJkSNpPUCa8tnd8D2yPk9Yq3uGubzvk7f198kdePmlWcR8ZWSmT2wH1n0vEZc3Lrnyc8zOr9U_yQYe6dail2K4B5HjXZqOXoK9sQWXkCvzgqJgQUIzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_HWqJzOP4DJjBdh13mC0jOTiIRPdZ1TGskk5dMHjf1hb2x6OJm501YoBsOAbmY5VIBFmxyRhxR0deX3z8u-AASQX4IL3P-jdrvkNCXTpOpX6LJuFAaMwD8YJDjPIJx78WuOo0wVP8sTII1V-QhwYtTAHQbFZKvf_6wFZqnVxA1yoByrzQspvkiEKyWouKvYfpUg5TIIaJt22FcIrLNrW3MydW_yejDtZKewZYZRLtcAxkAxuEqxYBGi5xiZGzZHBCSlBJK0Tq6z9xJn2E059GPLvjSy59eTEBuhAupdMcPByL9y-k7rw5k7nOEu2AQm6IWNcTiDrLkGzqT0reMiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=IEo_ouqlAt7GAllb2cBNouzQLhHxI32Zw57fsYQEFYxaHcXkVKikXYB0D-CplMTNEeQ8J678VZs8G1xuCMOPsmLGPxlRRMAHxzrMelgWihEl3fMkjhdSszODQBTMMK5M3mWvEzr7_SRUeLrYssoQaFzo_reMg4nfPEXbjbQGTA_VTs7HfXRPJSx5fKwi2152me1ie-_Mm42AusBJVLP1tDqbqraREOYdk_Tn1MFSHRyf6JT1YW1IiyWsOzT-KD2l7_fFamHgpl5vRZ_igRl1sykRZxa5Nl55b2KJOgjRpDhWy-418unoHDRswcic8zIP5Yp8qPaA7aE6drIm7odF6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=IEo_ouqlAt7GAllb2cBNouzQLhHxI32Zw57fsYQEFYxaHcXkVKikXYB0D-CplMTNEeQ8J678VZs8G1xuCMOPsmLGPxlRRMAHxzrMelgWihEl3fMkjhdSszODQBTMMK5M3mWvEzr7_SRUeLrYssoQaFzo_reMg4nfPEXbjbQGTA_VTs7HfXRPJSx5fKwi2152me1ie-_Mm42AusBJVLP1tDqbqraREOYdk_Tn1MFSHRyf6JT1YW1IiyWsOzT-KD2l7_fFamHgpl5vRZ_igRl1sykRZxa5Nl55b2KJOgjRpDhWy-418unoHDRswcic8zIP5Yp8qPaA7aE6drIm7odF6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBl8vNak2ZMf0L858kkT3xNwn6-MQd8d9T59P2n1NwTPDJ32jYjVSNCVUTO6Rw-G1ieF8JZzuED5XUDSnUYSQFeWk1tHbIKLzgm-gVRi8kcxiOhLzLV7on3hGpinbbXFjAtnNjuZ9GIVyO_nAkQcZ9qJevf5bAPuUKo3CHrf5t8JLoA3iDE0ExufiNc2IE8K_x_efdqgVlmuxTVVqWd3jO4FOIqbgqKrZffYq8GhCBIVE-Q-aFIcwPhZeWCljYh6Jt7O0QlMPHj9dkZDED5Z-HSDzeE_Bo5bfS96MoKSSsb6xwGYD6yBUc5cQCb-np2Fo4W6ah0bXkpmteWa7xHF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBd0acUCxgg6bvyVMqAtuAbrj86ZCNwTUOVYEd-VAy7rchFKcIT_AzRH8S86nz_hUnuoX-rkAFPfk_iSqqQBfL2zbA3kkLyouX4PeCVAvi5NMwPD1DrvU6okVfUw8qS-CwPCe6cdFOjrUbz6oM3d6wfwZbfoeKLWriQO_DvTDF5o6ik6pnXt4qYx3XEpuvxID4kuYUMhpyA6rq9Q_FFhW_scrE3RbxEmK2e0Bnz_SzC7fP58--ssoeoMm7LgXpACqLAReZ6QZTigd01q9rzVOmO3ragIRzgO31w5yLOisOg4bJtVUSJO7Qn9CevB8NWb2F87goy7zOZRMI0IN82hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=RSB-m-gMoKYmrIN7qp7wXkMPp5uGiLVrGXqjS1A2zSatphiFqj8UHWix5zzFymf6Wv_YoeCsXmbjS-mvpjEvZ8u3r4k67IARtzlezWhuuHw_Zm1zhEIYWUnyV4RC0UarZxc7igYz_mJOE0Y3__J1dClUm--CEJ_cX343I3fp-NbUmUqQH8qewk_qMHqrSysR-_pZKOWu4aTJs6VsmhpaKbHDOyx60UJsWSW6qBQYY4rsS13Jx2L6VDPEa4pMMQ_9JjMiwTdBoCiET-fbEHF8whWTdiBqW6HLfWUrkpUPWkNubC1K43dqdgQC0iRn0NISzhZp2qR0LQHffNyswoY9O53S8Eg0a9CoHooJ-83u02lNSmiR1Hmodf_7bj3oNa-upALAoVmkXN714Zn0DQPB3u9JgGcasISn9AbmPiRvK6aPp_Am3qXYrFdInUMRqIqzhsVPNh69RvH-Z9uO1VJvdyUbrMkzKA890cUd2X9Fh28dMA0Ub45A-9r2rEKlqn58HybU1Za7Z4zc3tmEIKcAacq5hUTY3FSUZ9unGLMsMWVk4wZM_Zxs_29o_AXnnh5RB545YoXbQmcm7-WpS2DlVV2po84GhbTcAc1YfYi49IQl7Lome1RiFWkX-EmEPuTLHvqgo6tmbzrwe0SNnNPDiKTIc3pubJs0NDu2zfDYSAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=RSB-m-gMoKYmrIN7qp7wXkMPp5uGiLVrGXqjS1A2zSatphiFqj8UHWix5zzFymf6Wv_YoeCsXmbjS-mvpjEvZ8u3r4k67IARtzlezWhuuHw_Zm1zhEIYWUnyV4RC0UarZxc7igYz_mJOE0Y3__J1dClUm--CEJ_cX343I3fp-NbUmUqQH8qewk_qMHqrSysR-_pZKOWu4aTJs6VsmhpaKbHDOyx60UJsWSW6qBQYY4rsS13Jx2L6VDPEa4pMMQ_9JjMiwTdBoCiET-fbEHF8whWTdiBqW6HLfWUrkpUPWkNubC1K43dqdgQC0iRn0NISzhZp2qR0LQHffNyswoY9O53S8Eg0a9CoHooJ-83u02lNSmiR1Hmodf_7bj3oNa-upALAoVmkXN714Zn0DQPB3u9JgGcasISn9AbmPiRvK6aPp_Am3qXYrFdInUMRqIqzhsVPNh69RvH-Z9uO1VJvdyUbrMkzKA890cUd2X9Fh28dMA0Ub45A-9r2rEKlqn58HybU1Za7Z4zc3tmEIKcAacq5hUTY3FSUZ9unGLMsMWVk4wZM_Zxs_29o_AXnnh5RB545YoXbQmcm7-WpS2DlVV2po84GhbTcAc1YfYi49IQl7Lome1RiFWkX-EmEPuTLHvqgo6tmbzrwe0SNnNPDiKTIc3pubJs0NDu2zfDYSAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhCTiwd5-L6uaxjpEvub0YH-UTW-4-m2eQoZ69m9WV8XId5TaJueGeQTQLUNza6WSUMZQxUAOoAymF3Nj_agbvtRo5DiNyEztpsEx4K70UohHEvOTbuAONYZyFuaX8WKiY_AeuMkEAFa5pGAXJ1ozXt3a_WhJHV7Wlr6QLXLk1Mx4mCT05zRmyi1hfWnToLXaQw76OH-QXS1QR9DzgmS28wf3l4GPZkGY1OTzEdv9YjZEeXuu3WBKkpkY3Ir5vn2Etp45wA4DPGg-PSz-6hnJIgeUqXd_ePeKdqXW3uHkNOHBrl-lqgTJHGDihWCyuoei-pI9IV2iMpvzJP_ffvHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=Y_m2Clq0hYBkQooTjEbDrrI9Fp7Fbb5a0PvarmvGV_MIMeUsNLJ8evdLwJ-n5XJnbwSAye2xFev_zWLVgRy9D9UB3sM8ctfqxDNDoOUmEDbrkunJdTD4RaRe7wjxTSo5ybcFMRJaCRD0_45VWcaL8qZQ_ywnUyKMZjYgaBUNIL86Sk3VPUgwEsCmg4uAEfnxmiwPpzKz4JCoUy2IdYLs7b8owiC_HCs8FL4lnag04lBOxhuq_--c6U4B8oJufh8VWelZid5_zP6tzHHPoBDU2Zs3zdYD4unxVabVSKOkJ8z5z_c_scPjxDto3P3VwrcBP_KgnzlxnvHMZoBw9WP2WScv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=Y_m2Clq0hYBkQooTjEbDrrI9Fp7Fbb5a0PvarmvGV_MIMeUsNLJ8evdLwJ-n5XJnbwSAye2xFev_zWLVgRy9D9UB3sM8ctfqxDNDoOUmEDbrkunJdTD4RaRe7wjxTSo5ybcFMRJaCRD0_45VWcaL8qZQ_ywnUyKMZjYgaBUNIL86Sk3VPUgwEsCmg4uAEfnxmiwPpzKz4JCoUy2IdYLs7b8owiC_HCs8FL4lnag04lBOxhuq_--c6U4B8oJufh8VWelZid5_zP6tzHHPoBDU2Zs3zdYD4unxVabVSKOkJ8z5z_c_scPjxDto3P3VwrcBP_KgnzlxnvHMZoBw9WP2WScv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=i3PTPDX18pWlCIetih79mWI3mxF-i-fiid1omPc_GRKLx1rAu5vTVvsijFGOnuIpApnTX_PkxnNF8CQqzdJS7xTPiRBYFPDfNICDZE9ycTbXSLM1cRz9Ave3SBTzUr4dhYAz11p6TtWkrZxaWvErAmsjesl1q2GNvHON4pntLu_b05HzVKH-YoHc2S8jFM8H9xlwe5iBqZpo-eei_aTE5jIFO1fuyTO26YVWWquPXSNDY08LuSFSs2Nyr6B2Xn7QPFAlk3p-ULS4stkwdjtF8ZBoRujo9tTQVsfR3r_LbN6y1_T6tSEccIZzrA-UOnUJ1YCBi_DDQz47SUbrv-lHPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=i3PTPDX18pWlCIetih79mWI3mxF-i-fiid1omPc_GRKLx1rAu5vTVvsijFGOnuIpApnTX_PkxnNF8CQqzdJS7xTPiRBYFPDfNICDZE9ycTbXSLM1cRz9Ave3SBTzUr4dhYAz11p6TtWkrZxaWvErAmsjesl1q2GNvHON4pntLu_b05HzVKH-YoHc2S8jFM8H9xlwe5iBqZpo-eei_aTE5jIFO1fuyTO26YVWWquPXSNDY08LuSFSs2Nyr6B2Xn7QPFAlk3p-ULS4stkwdjtF8ZBoRujo9tTQVsfR3r_LbN6y1_T6tSEccIZzrA-UOnUJ1YCBi_DDQz47SUbrv-lHPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5heKsEWT4sSumIIN7E2agQMCKkhEH2oD9RV-K2i6kZH3F9L4KVUJeKwwQySK9mi4gxbMGxKyx_FtloVJdzNuMPm-ywh2C1-eWqXRXSSz7uo-VtrPt7g7LhOoku4mQ8xY8EXgFu1PLU11XZiP45dHYrztRFLalSFGAxBQNbcn-FzGfdsc1y88pDz9UxnqRMQj63Oq906FJat0UVfTP4pOTtVZfE7Wx8wKgtrQcuN5lLa4Kx-JYLJVjOTUTV-Qqll6ce9cp669r9zr_V9CXTGR9zyByvbk_3WpaDZe0btuiHaVOgRAE1V1aApeqD5JggvktSXLVui3N29Kij0ymTHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCqemNAliIxxPTVmwW55cz3MPt0thD3DH5egnZoBgd52GEwDtv2Wg7c1vclkhHaUtGV43BL04XlT0dGp_0v_c27cqxw1ETrFSg76HHwujTzrhjHWVJJYC5X7YzHMWqrC-9_NBiyLv6VnMf9O4v1v5suxm6m8AKh1eshj9jjXTirmDXNT9FZWMU99k7vQq4nYki7xINFedhzyehVxzsH7vywxx_0rRMNRBBM-dHbvdgFtWHFAIW7fe3kCtsAYCF9e9qggBeQC6UmG1FkA3FViKzCtRG7-YlwKGpezwe9MlHRBU88NpOs-oovIB_8ZjOGC6qRtoaNnBS2j3NFlSU_YVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBCnVFa4llTk6cJRkCT_WIs7AdgTJbXgJbN5NpdA_B2L90l3r_2jWov5Z0Y-uEnjusqu82tTk8igVanvALuciiSBFYRqepMf5GZ0jDJ3S_o_xfjxoSDhRun3Y85z9cIaC7vPLNtIX10aJruF9Wpu5b9sc0rBqDrcv4Gs2tqtcl-Moo6voB7LuEGRqQUHCtSSjry5KqZEKUU5R8rtjKvQ2beRq8yC1HUPv8fXvfPGiXknVN0drXxF_ozwd2lg86CpT2_XXalYnQnRbl0wunA1Po1rYhfMBTtA89V9cxvm7F4ep5kHfZuNcM6Ezp6TdQMckwfwum7udL4l9nKBP2GKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sw3dWiVeS31imX5pffw4PqIVNAqhpWe5-jFBnCc1dxG-0YXFLkELmrPGiJAOzpJQfbHKI3AQ286cK0iPmz24PDp53gJvYrF4WMTX_NuBUL6oOsRiSvJZJZL_XW8z-pWubj68CItVV4rA0qpyydK4KkcLzjnxA0hFKxsrdMJqjqEF9n9rvuVfMD9umXD18GrZNXBm8oSibTfc-y-qWs8rZZMWZOvaWcAStcwsH5Pxjz5d0k-EYmZAnWPDRdNGquMiBimpqg1erpm3hOHt7jLCnnkKj5q7Bal8crG_IQgX9o7lRO7kL4TQ5vsZCZ_YFsoLvtF9E1i1Rzx6m6HfT7kjJTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sw3dWiVeS31imX5pffw4PqIVNAqhpWe5-jFBnCc1dxG-0YXFLkELmrPGiJAOzpJQfbHKI3AQ286cK0iPmz24PDp53gJvYrF4WMTX_NuBUL6oOsRiSvJZJZL_XW8z-pWubj68CItVV4rA0qpyydK4KkcLzjnxA0hFKxsrdMJqjqEF9n9rvuVfMD9umXD18GrZNXBm8oSibTfc-y-qWs8rZZMWZOvaWcAStcwsH5Pxjz5d0k-EYmZAnWPDRdNGquMiBimpqg1erpm3hOHt7jLCnnkKj5q7Bal8crG_IQgX9o7lRO7kL4TQ5vsZCZ_YFsoLvtF9E1i1Rzx6m6HfT7kjJTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nalW68F2tsx3XZicXF2anBvN-a1D4IHF5UjtQBFmwGN8T0XN4Hnq3k-JCYSXfqU1LcxY2LEMQiFuhXDs5Q2CP3YiWllOCH621fMPryNIKZH9LyQm2Iq-zsXGfRQBHLUNZ-J_agpFhnPUT--GFpDKzkYwMiXUoeGJES_9afezGjAQmF5fVSaur2IQ5Fvt2OWxByZ65Sv6h7pPmsYMyxDu0syAz9gN7A47yPkM6M5tVsOzPjxREY9wmkUhKJKFZYgUUy8cIIrn-3shV48Rf2oRDyLHQzOajr3mNVRuMOzXZiK7wsAqEBJLL9jSLW_ySzG1fV2ruLi4Cr4uVo2HuhYVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBBGHgnk0pa5eSaDqGUHesBQ0t3uQnh3r3e7zzIYRHdavIbuk4w81vdztUSe98L_ITeSJNmFTj440zrU5UAtVkPmPP4BqWa0yIitrLFkbM1_XjN1tCXXbvw5Ma1zuHNRh0X14h5GNtuQivQCfYpAtxagsQlwhDpYLmQ8jwr-eheCGhbqEgPWrCCmLmjAVGVvXaCQuspLCh1gosndclycC1XfqL91S5j80gZF0xbS5qazp9OKh4ULLo93xM9NjD4lwSMjT0qtDT8853PC4cvrlX3RFBIwBhoSUfJ3mt1zFdbjiSZJFfP-tPcBAexD7Hn2jChZPqfjJ8g-pAif07sDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz2XXppavHsi-3LK4bJ5eSxDfF5CrGh0DT614Fsso7rB8E9YUpgM2_Q6uE-g2tyBumFBfqF517EcYua5lUWaNosDRtfDQ3hyuAxkt2TgqedkkUk5E1R_n-QG6o3J_Puqr_aL2dBrciE5adl56cbtrNNtEOsOIOMOIfoO-6ZtQJuSDe_ifTWDjWj1LtT1Xi7iXn1H206rOVHj35DaFeU2M7hgbAv4Gv--cheTVUtKJRoGhYWNZIRRBRbrndUeq_KQGFjI_JDhGmnu_TQLuAvQXR9F0wr7p-SacFg-oUNKkG460QwzE2bhVC_4rw0WC5sJbS-AFquYLNw6A9W9Fz0x_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ds-CisfJqi3qsdh4wZNCcmbzI_zO7BpVsOGboyKJSBEfN_HO1wcR__FHaxoY4d2KRdsJqNjMf08ncJE-j75dCUPPF_4e5S5Wfdq6FBZR3PhwTZxY6DMT9-0DhwPn2O8DH8CXOpqzylpOPqYLkoOjpxd85ahc1NQTnstdecdIVrRpXYtPj-xrLitVrtPY4k9mwXY_B_2iPBhhPWpAyFtCHYvhjuHBs26g50Xgn2YYzLDdaeQwCQs9InpKUfsHn4gBccH-ZKknZ_m6QGAHEgawTpi84GJ9Z48c1wZ3tgJsUDHv8o5f7gn50qcwHq_F4_3P6yliEp4sjf60SfoGmAHaHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRUAGl1YhqCIRcC3xtS5kBLPxbUx3ZfMKmF66FNIcdj6u57fVik3cYcW44zR__yLZlZ2ElSPx_cbqJLgJ0vDRvQCae0wYRsvBqMhGc4DYOqS0b75yEDoZubWoUpyy3AnXLLyz1YiEbMK-KgC41mCESFdcMLLVyXzhQDoF4kLGCeov3wb-UH5eQ_S-ZxDmPdRedhRawXAXHYyx0jfr4VZ_AKm9ppon5mlKr__i2RZTkjiTGUwhd_8ctEJy7dq2hSKlUcWtPnqYXVmImscIn7vz8k0rE44rkX-9OEEBZ2qg8m-nTWl99fj3sv9cC3-MuN3JB6UDP-oZSM-jf4XfS6IIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=ezR0RmstncPnMMvaEurW1rHdZxEnQY9dlZrN7Pdzc0Zup2ml_QbiPOSIPGJiJraiU4-9Rr-X4xFoiA4q7tif0IlEWdGCaLPuy1ywuWoMrVkzs1Al0TwIK42gF82IKJu0GEAVMxd0q6o4zy_9A57Bzmb93AWPlrf1d3NaauhBKKYHaKzkvm8awTxmyjY8cikGIwst7xG3vApxU47vXbGjGnYwOnuxHjDZ1kXTt5KtvBwgcskzVCWONTb-A0-lxytaHUwbh9vVVmg7BUD21uKA0G3XNIO4axHE-a8eLGvd4NDb5LLrlCzbWgd5uKGCbnLRL4INhA4tswQV5e7XzlzAeQ5pTeFbJTOrADtrTLkcihJlcFfqWxQny8sPdSfgSzRcQv323r-9HJq7anPhMUibh0O07Tcf0p-YK1Cjxz0oFR3SQBRAscNmkZlOxC9xKWKihQ7r0LKf67VchkNBztm-5pFQycxCQ-iies6J0wkD6GfJr7tQlkdN5u0GqFvYGbDuKRh3GCc9mAbZIoxlhRDrzqqvPwALateBTQ1AaTcOMez0O-55oz91O01jrtUvQ7B4wIJ5oLqyFx8BRRE6rh-QzqmDNz0clcY68KXYaxm70E5VGz8GpeWegclBlLCDK7R0GubRwrvEN0M01BtiaEbnYfsa18XZlgcLnLWOwP3xWzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=ezR0RmstncPnMMvaEurW1rHdZxEnQY9dlZrN7Pdzc0Zup2ml_QbiPOSIPGJiJraiU4-9Rr-X4xFoiA4q7tif0IlEWdGCaLPuy1ywuWoMrVkzs1Al0TwIK42gF82IKJu0GEAVMxd0q6o4zy_9A57Bzmb93AWPlrf1d3NaauhBKKYHaKzkvm8awTxmyjY8cikGIwst7xG3vApxU47vXbGjGnYwOnuxHjDZ1kXTt5KtvBwgcskzVCWONTb-A0-lxytaHUwbh9vVVmg7BUD21uKA0G3XNIO4axHE-a8eLGvd4NDb5LLrlCzbWgd5uKGCbnLRL4INhA4tswQV5e7XzlzAeQ5pTeFbJTOrADtrTLkcihJlcFfqWxQny8sPdSfgSzRcQv323r-9HJq7anPhMUibh0O07Tcf0p-YK1Cjxz0oFR3SQBRAscNmkZlOxC9xKWKihQ7r0LKf67VchkNBztm-5pFQycxCQ-iies6J0wkD6GfJr7tQlkdN5u0GqFvYGbDuKRh3GCc9mAbZIoxlhRDrzqqvPwALateBTQ1AaTcOMez0O-55oz91O01jrtUvQ7B4wIJ5oLqyFx8BRRE6rh-QzqmDNz0clcY68KXYaxm70E5VGz8GpeWegclBlLCDK7R0GubRwrvEN0M01BtiaEbnYfsa18XZlgcLnLWOwP3xWzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQxDW0Qq76w3difRanrqhI2xzleOwIPMM33NovQJAnhqTgfRz46xuiFUdRX5sxZhil6gAfBnophf7usBleVWvUWrOPomVLwiF8zcrSLric_PvdadKG1_HnalB4JDd2rEoRYq91jdzbEf4Ne9sl9wCWKCFZa8vCbWUBZQjkIAj3VLSEblaKK3oAcbzAVcJoU7y_50c5b3fZly5_JF4msqt51oAlxEQksXKkubWSLwx3_cg3xRFn0PRvYaRxVJKlV9gQeQlhD7ZOT9MIg8tD1VFhUy2W2QtNWOIOSkJ6g_RJlyF6AomvI9qcCnrgg0VzM6Gv1rrfYzEA6vyx7RL1XIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=ljgLNk1h9uAAcNyfexJ41Ej6TB95T3PB3ZL6Chg-YQ-U7pisF05_q7zaoqOIkJZ8CIsr2VLAf4H5N3IkgBcf7EjWGOc6DvTM5-_iVO6JBJHuP_KxCQ2dEc6QaHyte0wkhFC9ckmcPl8rurGYAGRFlmKO9KKq9068wJDhrdtBtLjVJET_Ixa--7wo9z--HhkAOQQEkRBlU9SUkGDeTSh8gOlIdXl0fojZLtxZK-VX1ylLMZcr5CdHHB7rU5P4Gm74tSkp3FbNkBB4KS45k-R6tTC40DI1VklMPkxG70qeXqYyYrBDVuz42i5_TIkZ2DCpwQW6GJS09nlJ1wJc9rtkpxps8NcjdNK7RV5jakQTNQhOiv7_ZjzE4hlhcM1_vko-UmvI7jAR9cFZrAaHZDraV-omY2rIyfb2sd22vy-Nmslj-xBBAE9VG9h0DkFJCWjX4xRw87O1kRszH9n7JwX8JSfn2Z9InMOK0krArZFinnSjTH-carKpM4_qG45QD8ZM0baowWgPFmAHalMZ_8wbZacS8TX4uiDpwP39XCmpC9E46oUHP_zuugIxDX6MFxLCYGwCy3gJzUX2gFzaGjb63ov3wvFrFXmKL_5n_yFGBVq0e-1J-aJJrKn3W-w5V4ejj5GqQCv0jaai433PI9wmO7qj5UUYrUQ9i1_0nsSLRH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=ljgLNk1h9uAAcNyfexJ41Ej6TB95T3PB3ZL6Chg-YQ-U7pisF05_q7zaoqOIkJZ8CIsr2VLAf4H5N3IkgBcf7EjWGOc6DvTM5-_iVO6JBJHuP_KxCQ2dEc6QaHyte0wkhFC9ckmcPl8rurGYAGRFlmKO9KKq9068wJDhrdtBtLjVJET_Ixa--7wo9z--HhkAOQQEkRBlU9SUkGDeTSh8gOlIdXl0fojZLtxZK-VX1ylLMZcr5CdHHB7rU5P4Gm74tSkp3FbNkBB4KS45k-R6tTC40DI1VklMPkxG70qeXqYyYrBDVuz42i5_TIkZ2DCpwQW6GJS09nlJ1wJc9rtkpxps8NcjdNK7RV5jakQTNQhOiv7_ZjzE4hlhcM1_vko-UmvI7jAR9cFZrAaHZDraV-omY2rIyfb2sd22vy-Nmslj-xBBAE9VG9h0DkFJCWjX4xRw87O1kRszH9n7JwX8JSfn2Z9InMOK0krArZFinnSjTH-carKpM4_qG45QD8ZM0baowWgPFmAHalMZ_8wbZacS8TX4uiDpwP39XCmpC9E46oUHP_zuugIxDX6MFxLCYGwCy3gJzUX2gFzaGjb63ov3wvFrFXmKL_5n_yFGBVq0e-1J-aJJrKn3W-w5V4ejj5GqQCv0jaai433PI9wmO7qj5UUYrUQ9i1_0nsSLRH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7GQCsmWqFT9wGwOdqwIvIW5cYUPwZx1H7-svYdG_fY_JPdwbKULl-6pTHG8EsN-Z1IDFlqhOYd7sKu3pDmLgRHuxUCGK6ttHn52LY4NvMZo9O33qkuLq_aInO9XlznbRdo1KYp8UqrO5EZo01vde3O9NJqDPYQ2kAJYV-pQZgP9QuuHgeBZlykeXANv8owDhVn6zsEOcRFjajW7xK_e9WyNFYkMMjWOw7kA7Yuv0AszrDtD8Z0WD75EMw4I1ALXsUwswWBATb1_iRS0EoK-xzSkzAdFJEUfrtwN5-mz8782NAcAxdtuENdOG2ofc1v5NCYIkSM-YWd9CiGaN4m1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2KbH9i8Lbv9Fc5RU5O_jqg3PADDlMD3_JxzDU7P93ronVbR4svV7GJKmBRHIh6az01Kx7BRxX2tDjRNPBYBG-kBVXmBgyOeGWicPRV6AfRqdl20NdKxiy1wEBNHEldNwLJPzHdfl_G-rlBzHZ_RsonOzS6zo12TjXcvuu6WrZn4pDlqVI2gqevZ6OeHYRen9Fj14f7GMY79nGSJp4ohftzE95wlJKMseTKdppbh4tfqacHiCt8urV39Red4MV1P_3I1rkWpwdTRkYZljS4EHdYoNUclipgKhV6A8JgZJMa1z0rMHMWXVnx3PYyciLq-YHVEHZMbkCogadyuQtu5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=bLH6Uv_NnI0ev5LfKo0XQ9o6UaLD24TWmVI_lDjD6z0Ql4H3-A1IFUbVgEvCCwxFumJPhsJsGmMHX2MLU9zhYTKrHFeIq6hYPUUF0jc0WzAdyfha68L4XD9DrEql_yxOWYLRIn293JnVRi90cyExol0OhsO6CoJ5A4JnQfVG2l99moPnimlOiET4YK6ZGe7sSTeSdeO6tJY3d6CldZBCIF2ylxYVxO6YYvh9F8rQIj9l5HKbfDhFMSwQwuzqgY99sgtcNej1hBmrpkjVtwhGwSWzUjRRIIVS62wuLNTkHHfbQ7cfLzpSxA_UjPk99ABu6aNz8wmQ5uJPBiIrqcVAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=bLH6Uv_NnI0ev5LfKo0XQ9o6UaLD24TWmVI_lDjD6z0Ql4H3-A1IFUbVgEvCCwxFumJPhsJsGmMHX2MLU9zhYTKrHFeIq6hYPUUF0jc0WzAdyfha68L4XD9DrEql_yxOWYLRIn293JnVRi90cyExol0OhsO6CoJ5A4JnQfVG2l99moPnimlOiET4YK6ZGe7sSTeSdeO6tJY3d6CldZBCIF2ylxYVxO6YYvh9F8rQIj9l5HKbfDhFMSwQwuzqgY99sgtcNej1hBmrpkjVtwhGwSWzUjRRIIVS62wuLNTkHHfbQ7cfLzpSxA_UjPk99ABu6aNz8wmQ5uJPBiIrqcVAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeSPnxy-YK-RJKIk9_-iATRFrISSBKnryxEQPVe3MqDIugPdWSq2k8ixRohoHLLbyu3TzaM3Xjcc6XdJJWGeMAh5ywehTOtTlM9jigKwgmIWEoBUvq33WSqaF7_caTA4tlTKhyR1Xztcxyd2HTz6Ek7g9ZOjf054Y6RAVdN03rupxt4AtsIkECbZBhCr-vKhFq9-O30J2eRO12i5qOIUP0SA0xUxi3JlMbGYHI0ZwBa9Y_qwoq1bNejpLoS_LkJRonz_8voVs4mxsyU6GWsNx4qeTj6VUh11z0MMkN9KYv5_G3JptMEoYZPc-qL3cMcnOPW8r7aKJ49V0z4iwyYVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgRcK1iVfRqYdNiYR4pNqlH4zJzv58HPQ10aXBrZRT2AcqbcGfZZaJ3G9lA3snkRWVs33_-ac-QCPRXzCiur5by9BhERF7qgPQ64bRq3p1Sv_ndbY4EYklvFZWdEYFPseMRre_sEdwfMXUJUIVLqO89kN_8Ahim_Y6gosj-zmx3IV-LT9v8OAB9cANMnFgbW1s8ZaNz317ANm3_n_INY65ylARU_0eMXFEmnAJ4b78GGtvHIjOs_1oVZSEaaroyGkN8AEvu-v1WDdGnKD5zdyWH7OWTrZRguhvyqeuf2vXASXPN6tF3k0UwLKwQ6b1B959zwpgpYb9VplFIkPvVh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=Y8dnsw_ZDw5vdrCyNyUlwDJShT6hB6v0byNe4CmAjz_FEzzUqL0K1ggQSC5OkZOmA0xkc28CKKJyjdfGOGO27UAq81UHjAvNa3Ti_t6rukslezCKsdiEgb-wXdKf0RvpG1gBDF2TdjL3TnX8AG-1K_zsabW2XVgWo1UT0VLN0J53zHTup4ggOFhNdSGxI62Adnm8ftqBQp5RlSPb3jgq1fk1uJx_fE21c1XcvZrBpEUQCw2AuD-_ldrhXGfHJHAHkhevj2QwKrlVKaK7LGPc8NRnRVqAKlYoOijmWJBX-kdz-PbX6rQgZUgZZ8XmOw1Ae9d6xkUfN31MHjy9DvnaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=Y8dnsw_ZDw5vdrCyNyUlwDJShT6hB6v0byNe4CmAjz_FEzzUqL0K1ggQSC5OkZOmA0xkc28CKKJyjdfGOGO27UAq81UHjAvNa3Ti_t6rukslezCKsdiEgb-wXdKf0RvpG1gBDF2TdjL3TnX8AG-1K_zsabW2XVgWo1UT0VLN0J53zHTup4ggOFhNdSGxI62Adnm8ftqBQp5RlSPb3jgq1fk1uJx_fE21c1XcvZrBpEUQCw2AuD-_ldrhXGfHJHAHkhevj2QwKrlVKaK7LGPc8NRnRVqAKlYoOijmWJBX-kdz-PbX6rQgZUgZZ8XmOw1Ae9d6xkUfN31MHjy9DvnaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hD_A4MfCIuOLw2pjyfCt0zH0lZMpSK3XsTyZiX5_DB-lOs2ILl6cZ8DgEcC1aJ5-m595j_ggtC446I8cuNUBa1KqQIFml-XMKIDmajlUIqcl84ElODrup7VYFSBcUhPYTnBMgtBdGxhjk3tBC_li0sKnTNn3PvUAsWBbyqKbLNNx7_CNrPh4wU38VGzrkUes3UvPyxKmoyVui3QtHfuBdhwpHu1MvbRJBNds6f66-ucmvnRUztI-m_39rKUYoPx5ePXttI6FYyzzL-G-0GH0SsHuXuknKCfrV5C6yaT-RM_kve6L7yapKFW1IpEcVJdEklclIvdINaURZkUoAJhPPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN_kW-JIxStXCUWwgb9i-q9mbresqgSKOxo6xKmYB5Nta8QYCG9xHdr2JvZYaJQLfGeE9EFWX1PsS6QDzUzdNkdpPaYxta1J4KgP7Kj1ABYzcwgG3RoiQKYxetvnh5RaruoCvcSMDgmnkKcb2xeR3xSExXL-irKnPX1klBHDJ6VDeGzQcwQeSCOoQFRVqvI3C0imvpe7y3OJOS5Kv6hPE-AQExLoVLIKNhAz_N-j0pLKfnStQxsSZSeojlX4GX_4phkoYkQp_05V3F9ZDjqVjqr6QdlWdDc5vnQBm5pbfBe2NbaWHCWa7M9lEOUsSthTIgYkaZb2WW7OEnrdI-__Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=kUXHr8bg19ALivxs-R-UbYta10fPpKGpO1OlxmDuFTQ16o_WnBn_LOHWLMo91hvdthnXUDDnXmw9ZjZNqUsJZUwg-4wA-jTKHdAbvNuOP3K32jGoxskvlOwBaw9FRtKQeQgcGvLIbBbYhbjaZqbeofASAzdD3irvxlM_OlSZOWKKD-B_TlKhDixxFpkrXgqmyJDXmv8IimYC6iZqM_sGnDsdNHfpQtDZqA7Wl27P4DMAiu8DsfmQJztX6hfIHaTmlHoIGr0EPe4Em4ZUtaD4KNE_hkxcPx9flNwAZUcP60Bp8IiuZiYY35d6dwzCdod_PeIy9lh22mxFXo3t76tyhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=kUXHr8bg19ALivxs-R-UbYta10fPpKGpO1OlxmDuFTQ16o_WnBn_LOHWLMo91hvdthnXUDDnXmw9ZjZNqUsJZUwg-4wA-jTKHdAbvNuOP3K32jGoxskvlOwBaw9FRtKQeQgcGvLIbBbYhbjaZqbeofASAzdD3irvxlM_OlSZOWKKD-B_TlKhDixxFpkrXgqmyJDXmv8IimYC6iZqM_sGnDsdNHfpQtDZqA7Wl27P4DMAiu8DsfmQJztX6hfIHaTmlHoIGr0EPe4Em4ZUtaD4KNE_hkxcPx9flNwAZUcP60Bp8IiuZiYY35d6dwzCdod_PeIy9lh22mxFXo3t76tyhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=PKONCUChuEd9SX3w-rBgG_FaJSUTtPTUbCzyBp2lyA0NbOjcKNIFixqqXLRuZCzKr6aDVXMZhsG03aHZnKDUkfitwR1origkYbnbVaZFvTiApkuW3lq2E-cPyhp7xKNG2N-k-uZuxxZApImTIX0cPq5FSJm5lFU0BL38Dtw1wjIHcTSii77gpHB2oSH7JDbZsSMWiiQEVcGfu6VCVmXCczsUrEY-Gvh3sgqIetv_aYQZpbGRfUnfqycjx45caV68iwtsnj0H4qsu3yuUgAQAaVO01QTB4Vhu4WI7oc42TWE1WZHudTpZcYZanMMQi7iOi5Yc5UA90F1y8HPbawD0EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=PKONCUChuEd9SX3w-rBgG_FaJSUTtPTUbCzyBp2lyA0NbOjcKNIFixqqXLRuZCzKr6aDVXMZhsG03aHZnKDUkfitwR1origkYbnbVaZFvTiApkuW3lq2E-cPyhp7xKNG2N-k-uZuxxZApImTIX0cPq5FSJm5lFU0BL38Dtw1wjIHcTSii77gpHB2oSH7JDbZsSMWiiQEVcGfu6VCVmXCczsUrEY-Gvh3sgqIetv_aYQZpbGRfUnfqycjx45caV68iwtsnj0H4qsu3yuUgAQAaVO01QTB4Vhu4WI7oc42TWE1WZHudTpZcYZanMMQi7iOi5Yc5UA90F1y8HPbawD0EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVs-C5bH4OYZHxV2USDUwsVs3ijb1uC1EqiayVnqEs1YxKLCYfGV0Uw_4Iq1JMygXs_ggm22oF51NXmhRl1Vtkunp5OFzIl6hEhlLwhsYXGto65GtJhNLtAky-OePii4kBCu6DxLLO8j8Z0Z0_MF8VliNrC9WgCqU-5IqAUO8d4QJyI76qoBczMRXigYGgLh5D7CSEhXAHEE6NNOOJKJ8zWuUBn91wFIwexUzeK0yVRnN6LlhCIFc_H5oTgvambPkrop4ZtmO66YLGXlI57FQCwqjWW7JUbZ7BqklXvZ_Yfv5SLm3OEKSKCNfpRFdAgcRTaHAXLMoCz1o3UxLXThTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFOm8pelc03sItkbyB78Bbj1FsuU9q30KG6WQ5yEl81V-fGQwv7HoD4dIqJv0UCcx_NZSJTT5dZ2lvQFCgGY2gxJd-MlbrzlxjOFeX3vx7i-uCgJ4wzzLuRnO-khnhWRThjFRH3R1Ds54cO3NBpWk8hP-8-ACNEBNi_pKjyU67dDE1-feNzYfxQezGZPMvTbEvYG9CI6GasiyGzzSOsc5g-W0lvpZg71RNrpgH6YLitaI9bcrORsdvCh543JIQGLm3jVDw-PKMfBZiPmQGzsI2ANYPGwYqyfHEYscR62EJrqBBmgdNrobCF-7G04tCAuGr4uzAwmUNsEuIIQUZEa9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=aAK-wmdPJ_FFXyctESECJ9D4kUN8sq4DZlrX-1BfQ4QJbWRBacEyR2H4aIpD1rDiNiq2Ua0HoRt_B2niiv3ExBoai_CuJjwCTViSFJ6TOHeYI_EOpaprogzaj3FgQyPuuXaK6ooiqr9DALoVE3vgf5dgXtOfPnt21eTiT_QJTTb1sMVga5TV6WKNwxqvDLP69ligfHdMQBR5eSsEQeHKUHmjVQYsBNjAjuWU6gNpTkwcnKLrQITzYHZyQP42h5grMMcFPpSO8SOvagsa-ZUoAOQXz-uv8NkssYtyTK1uB0mkHkbAZ3kPImq6rx_6VS2ODGORaoWv991QVEAGilncKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=aAK-wmdPJ_FFXyctESECJ9D4kUN8sq4DZlrX-1BfQ4QJbWRBacEyR2H4aIpD1rDiNiq2Ua0HoRt_B2niiv3ExBoai_CuJjwCTViSFJ6TOHeYI_EOpaprogzaj3FgQyPuuXaK6ooiqr9DALoVE3vgf5dgXtOfPnt21eTiT_QJTTb1sMVga5TV6WKNwxqvDLP69ligfHdMQBR5eSsEQeHKUHmjVQYsBNjAjuWU6gNpTkwcnKLrQITzYHZyQP42h5grMMcFPpSO8SOvagsa-ZUoAOQXz-uv8NkssYtyTK1uB0mkHkbAZ3kPImq6rx_6VS2ODGORaoWv991QVEAGilncKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=JkjSDEi5HCjmb7FSrPllDTb4Mt1zxEYdGOWNt1PYVIMHXtoMYnzzCt89HuwKvQ--kugqs6CfgtqsbttiSuMHT_XcT_-Pdk9olCiwPLwT7J972I2ySWixBKNkWmowi2bV5i3AFZ8JOSZ35e1LivgQUb5O7S3bs2MpPdUKpNqX0oOJ4blT47Imt8KdVmO5HdW5Mijn0p74SGGDZYSE3in1HAe_pGU_DEn_kTGZVHkKwooTk11-K7jkMtchhn0PGO05a2N4-JKm3o_KaghFW4m4E9soWI8UQNN_iLlDhsFf0833lJjX7brl7TbwiUigswKDD9QLX_Ch_j5iTlyWbx3FbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=JkjSDEi5HCjmb7FSrPllDTb4Mt1zxEYdGOWNt1PYVIMHXtoMYnzzCt89HuwKvQ--kugqs6CfgtqsbttiSuMHT_XcT_-Pdk9olCiwPLwT7J972I2ySWixBKNkWmowi2bV5i3AFZ8JOSZ35e1LivgQUb5O7S3bs2MpPdUKpNqX0oOJ4blT47Imt8KdVmO5HdW5Mijn0p74SGGDZYSE3in1HAe_pGU_DEn_kTGZVHkKwooTk11-K7jkMtchhn0PGO05a2N4-JKm3o_KaghFW4m4E9soWI8UQNN_iLlDhsFf0833lJjX7brl7TbwiUigswKDD9QLX_Ch_j5iTlyWbx3FbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR0yqy4zyoxPYf5cdDxHOKcsjdlIdZaMyvoZovpQDV5PFdoCisbOsAraCUYqZDL5mQAYXIjXJ1gZlklk0TesBeheuXueGOOnN4M9IbX6_pN6CpgQiVuCdxz1DslDCco2D0cDP-dlml6exutT0bFub6Wkx7OrxSKX3qLj5eSzNpwFLWDlnqwJO1oCG3TZXy0LfrmlBEAHojulpsoEzUeLtQsZbuUPrn6i93G2NocSVCi3rokhO2mvjB1NIEvfdjjfFJJSmc6vfc0hXHDQzOooMNKNYV_w6MgNXQbMhSL3SvQG6bKxP0kd2bFDB__MuY-Q_7T3I67A2UwjiYLqz5ioag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNJoV-1BXS69pO5A_uL3b0G31GFH_3M9IMdoiRBT9KoDGEX0HV1P5dx-bLqsGlaOWBLZjTeFUFfOARNvHoex_3TwQI-9aa24bgFVbLMlVgK2mTJ0o1fOX6Brq3DnfA_M4dzjLCAkc-uLEDkBc3SrsTzwDICQj4g0OjFDdPbubTR44lqFbAxpoV79QggL3OTZnIqr_HGD6Lkus8HmPvgQl8EH4qH0x_RFC4X1vSBdy7WjPFdCatcW1QmEIF4uVMwSTJdoBlOQokSw4B31pszZoehY3GVPBxEmBtOjhMvKxPfiD_heTuCZYMRIPFustcov14zDkC7M-Ozfr-1gK8E3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux0fy6Cpfns9qmK7kRD1w3JJhi4iD3gOWvj6MsnNL-Iyba0pqQ4Q11wwOTdn9SdOzZZVEmSI2AMNEdVVm7jvzrQdTX8kDoMU2_R0lOt9m_jmnHMXav6lL_yWiXIWlpaKbibopW3hLm45i88zRyWooLwhqKVytRQhXSIGcigzYuUmW_U6xDkiM8tpahTSuj0BS3tHjSnxKaV8IeKzIkKoQ-_Xj1lseTi95aKg7L3xRUSSWrcVeT0wrKgfQkAFC1eSK_mPVLI1eycbkpnZYkZFKyWqfCH6n-MBT-Tw6LWy1oC19OA1uQ6SxhWz0qwcBTg_o25miHb83Upbgnf7ecEDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2XXOulF7ej6vLxFln5QHxcKz48T3sVNgaRLpc6qjZKFvW4r8ncD2kBdAxMfsqgXP3iHcvL6u4wUxf9R5HGGBGn2GaPOsUBHDEtR_kqvNti-UdpsiD2GR24jKxn9IRzKmcXgYlTLOrnjsv4lI3H6A67ChpGKunhPfuog6Q-2_zCRjrRZwQbfUN8fJUhwKx3q4J1ZFCw6aVoXdGs68bgMKJRPd26vZnnOue2wiufhU8XO3gbQeHmQdR_PVnBKJHY83VWYz22CEo_Jps8kPqO0zClDc-JEc8uZJwJpmo_y55r3xNPMwfAgGLDpDbWTYydpCQpD-S_iJSRoevAIJ-A3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgbdWKNLfbyVpX4tVpz21Jy2rDpgqD9P36Fp1OAkHsE_u9lWAy7psHHQVp87QjvaDmvT_XmQQbjNLKgMB6LtGlAy3vLCmPpvGYOB9YbTItkXVAzCuHjrW7aClERXnqvkoXQDZYlQwTERGp2hSOyV0aSuSdShhqE9nX0wZoDiVr4hLnMCnW4htXJfqPfDfuh8yPgCYVJxh1F_ySWs3FHgiE7H6mjMc6rH0CTdXfa9eR7VoJbbaHcYcE5A2sOI6bhw0kMFsFbMfHje518vuJPtkHe7K6iG0pZeQH8V2CebyGrvo8_vzzfVfJdqoRuYUQyf3P5aJKQq9KQVtUeccRajcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=o6q2NuZmOffzNHdjHTt5aablX9OL8d0uupK2n8tAOB9ld-hdTAV-7sd-vOTL-NQd135WMkteyl2LF-NJf08Ve62aJgE_4H0jOQqu_B3zlVQnV-OeIefzp7m6N0VlOsxlLk9UL6F9Ig6bqmvtRnhNQAwgbtvPkhDJgOpj7HQ0koqNE2t_VVAckoNGBax7SFKeQTXfSaFmg139hgGbMTYhzS-_fDaG0FZ2MTwnqP2CSD3kyMMkhTn11gNNmDYT5bGqR02qQDhKYzWT-gsT9ex7o-P7Ea78MWbm9oZQanEcyCSXK0dNNCXzZkK8lxeROiFEY3RBAUk5vvEbTbz3Lhq9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=o6q2NuZmOffzNHdjHTt5aablX9OL8d0uupK2n8tAOB9ld-hdTAV-7sd-vOTL-NQd135WMkteyl2LF-NJf08Ve62aJgE_4H0jOQqu_B3zlVQnV-OeIefzp7m6N0VlOsxlLk9UL6F9Ig6bqmvtRnhNQAwgbtvPkhDJgOpj7HQ0koqNE2t_VVAckoNGBax7SFKeQTXfSaFmg139hgGbMTYhzS-_fDaG0FZ2MTwnqP2CSD3kyMMkhTn11gNNmDYT5bGqR02qQDhKYzWT-gsT9ex7o-P7Ea78MWbm9oZQanEcyCSXK0dNNCXzZkK8lxeROiFEY3RBAUk5vvEbTbz3Lhq9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/topcaV3Nik2GCuFhSSIfqWG5-EvqSlI7SLsLfqhQ73lnZxckAsik7mz2F720a2mxgXnhrwYR-Jzp4YlppDKYGO70yBduxbOHjRq1WGgdFnJrblb7YsehLHLI36xoKj-1tK1jM5CnmLF7oweoPFKP6jD0NpOwpC5ZT3FzlHV2KfAcAyT7WCGUIqICVOM_z1rj8GNrc6z-4Q0Hpmaf1IY0YMuqKLGR-5h7C3msh9EmjLWmHT_9yLey-7myYhAGKC0KthwdAbR5qFNf6CUksOi7xqrHRWxKSYLenFlVisT7AOf2YZ9isNWvQWVpRMGhjfXOzRu1GEvx9tkLNu4og45l7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=Q3mJ7fzCQT81F1l-11F5KUahoIwVY03GnB1y8W2JRaqgr6SjAEabAP6NEDb-gJmXXHSwO_VZIYZ2H55YLepoGOLyrLiLssay-iQM20xB0LNSvgVF_6w74Qp7RnQBXjg58VyPyZdK2gLjJTdXigrBqL8mAx3rbUVEC9aaoNV6Xa59HIviqIUdwAsxNV-JPTSpKGgoYGYZrWS6w1t23nIfS82buhfF4APUDiIw1WhbnQjNyfvNZRgzOBBj8r1ECA6JX2C_ReotjCuJyyySbl7q3vPYgDuxDFsDzOKS3ks_EKzH87IL-nq3z2vQmz9wwgrxMA2V7Wh0FCElrkyJpJlVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=Q3mJ7fzCQT81F1l-11F5KUahoIwVY03GnB1y8W2JRaqgr6SjAEabAP6NEDb-gJmXXHSwO_VZIYZ2H55YLepoGOLyrLiLssay-iQM20xB0LNSvgVF_6w74Qp7RnQBXjg58VyPyZdK2gLjJTdXigrBqL8mAx3rbUVEC9aaoNV6Xa59HIviqIUdwAsxNV-JPTSpKGgoYGYZrWS6w1t23nIfS82buhfF4APUDiIw1WhbnQjNyfvNZRgzOBBj8r1ECA6JX2C_ReotjCuJyyySbl7q3vPYgDuxDFsDzOKS3ks_EKzH87IL-nq3z2vQmz9wwgrxMA2V7Wh0FCElrkyJpJlVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ6sCvfOda-TCi3hXPtYww8BDUDokFppl_EuvdZ8g6zgtFhBkpoWva_Ltf8l95gqou948qDQxbVdcs94LfFnw_4Z8kGTfx4EYFP2C18Stb1VcCNeTUkJqrOKU3Qbreqi0CSkC9HXrg6mvHROgNknDBD1o5cyH87Z_xNlHxfikoHxkdfqWOM9Epi9moBaLPakWcRLtpjUJdhfn6etlhcznzVYRnqZCiZS_tscHqdxrMJMtNt2vCRJMzOuXNo9_Y8Ft09koGn3Mi4JUlY1z9rrWbcA4h7f5Bo8xyCAIYKbHPI-cZ3OnRFf67iz1mWEZH2QY5u3Mks2PYeyHfTRlO3vTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=tZrOUsmDGNmjJcRk_huwnh0LWHLhW0K2YUULSHd69H3fLPmeAtN-cxdQVHWw_s2x3epiQF8FexfkyIa1-dJbCybS-RReM0h6D1UfpYQZJa3tHyg1B6WtwAo_RFfi7lk3yDMwM8mgMq3H2caXTxi6UIO9WbHN7LBtdjnJGcuESFmnaK6qlIl2fxvVe9zjzugMsuJ7H1kp4SsMwPMhVdncGxcwiAJUgbaHgLYycE8GHdmqQ38wdWjVNnmp0Tn58F_yWdfZ71KBmCdnbVqOTJNZB4om5NH1Y2nZofB44yTy8evZb7SQTtbxiUANSjj4i5as0Y1RtRT4ahXipTioL-h-fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=tZrOUsmDGNmjJcRk_huwnh0LWHLhW0K2YUULSHd69H3fLPmeAtN-cxdQVHWw_s2x3epiQF8FexfkyIa1-dJbCybS-RReM0h6D1UfpYQZJa3tHyg1B6WtwAo_RFfi7lk3yDMwM8mgMq3H2caXTxi6UIO9WbHN7LBtdjnJGcuESFmnaK6qlIl2fxvVe9zjzugMsuJ7H1kp4SsMwPMhVdncGxcwiAJUgbaHgLYycE8GHdmqQ38wdWjVNnmp0Tn58F_yWdfZ71KBmCdnbVqOTJNZB4om5NH1Y2nZofB44yTy8evZb7SQTtbxiUANSjj4i5as0Y1RtRT4ahXipTioL-h-fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqLWMKsqLseVt-bJDzZ66kj4rNt3ReJZNlxbpw9eDFWwTOBvJKTcfoVK_bvBL4XBIKgzVaq1xnx2L7VQo7vIARFKo5MLUBwCWDjOGSRsUiIlNZJE92G3mB-8DikV5zZsWG5Yx4fSY60x593b5C-DhRCprJiAdUC792jB_Z_XLzHV4o2jv_kc5Ik53MtEvPt54TWvfEEoPWy3heG4xblT7OrcimIJAxn5FzNZlyC9ktfOVt0zHo7i_4BNC2Zvw66EBniilsufwYSU_rcrMm3vgvUbFAZxAN0yLxaT5aGC8u33Q86xggWp-ZWeAYywzeDffgHNtGSdb207_EoJ4RVlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igSWx5YG6Hf6EIxB9U2MIPbEkgta1FYWkPODh5fLSQ_-bkrzw_D4qGtvesJgCFIsjnQU8UFyX7Jeo7sO8BF-0oDQQgC9eQaQ1mJg2YcsdV-AvdPRB1KCaZIcyPQMyHo8d1aRzK8HDuTQjnCfljxoaUNulGp4poQ2jJzeWEl7ZLq-HopcqMAjejJOx9IbDpclGOqHy17J_-1z1fQuuJjzsANjzJ8u1umvFykcEc2XIrELIh5EihZjE4Gk3cec8hlt9IizNf5BNXoMqanVAjlBD_sPu3VYP4ByPCTbYShNzwNtWsFcQ5am2OpGNtxDTPaBp4GBv7oaDqz9v-LotZzPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdYkjTMfLJr5f1M_70vMEdsznmmUPnqhX8QUwg2gxMJMu_R7DDQwuiNi72YVnTZhbXAmTKPk0gRPp7gdOHXGKVdk7Kw_HRPEiGA_i3tIBeQpOKlSYmL3tF90T3qki-7auSa-QwgldAP51QOO-3OcbFiPzjlU8LFz9INgfZo7bb8W4fxvmr6LkLlxXg4Brjq43_ivYMtyd7Ke6queJUNb9Oc5RPRokIPP84IRBGYvr19ccspwKmKJKLmtzgi46FxsAoJwIIG3qEXpRFAEHeumMlmrJQcqXFnvx3vV6wo8OMR2J1fD9vCqOmCT9LdlveGOG2ar67eJ8FpoXuqp_fuCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg-RsGle88aEXUgeo1gYIRWZA401-XfH82rGHwcb_g2ideJWeM0itCLwo1-1vWEWqxpt4yB6FicH8A8o1cSgIcWFNqYTjbsQt3Vk9rdSVr_sTH7ZijmeCwnq3JDBhe3J8pcE_ZQT4YTfXnsnu-QJnL9AQFGFYhjofBTr7wKX6pzP66qq5vL9pIeWa1Zd_v2DN9CrV8yDvMlwTMeW4kvua8ZPsHhW0cmZ5PBpobNYrhbbUIzDuiNPYhUgIjCzWAcKPFR67qEWSl5u6Mdha5CPico_9yzASE4NAQKYvQyJNET6kVMN43VDEN5i0g6cDfZjL1hCDiFTN45bhwpv_7t37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuonzKNY1PBuxTGSJ9-mCHUEBbAZXzW0r9Dk60kruGnsh7RlUiVjvbvVLLmzQSQNr7a3t-w5-l8thFbrws3LxBwXhhMqB2artKOm2JnuzHnltlLopCzv0JqO1LI9m9CU4PYAQtc1nBk5znrE_f4SQ3E5I4LaOWUr1g2dGMiDgNi0eHPfCUCwAZCFdh2CZwEpjA9lOuK4W-GLKDTK7ZHMXI2OUQz5HD2CSwJDH-VlzDnmg817wljvnUO4JgrqQzg0-0EwqjT_4d97A5GQt1unjRvrFO7OGaeFw1CeFPCHAisnz2SdKwT72aqo8czbGZ3K6mGp_Rf918oQZ0BMPQm2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYveGNazm55nAIKhf69i9tpZ12CGqd4ZSJwVDN6w8cFm84yvtSnI4z_0ll5RTdYokO1-MsZzusoYfYTiAJlv5Ts54nPAU9yQVbsMHmK2_Bmv0kbpV8rj-kHtWIctwvGodiCtTqWHc_LqGyW74QND_WN5HAv9i4RuBqIatRtEH0Ukbu-ibuaCGmIoMy1CteJ-6FEh2zFCrwOp1OS9vakrDWw0anaMPzbtkG0kTX3gO51O_O4vt1VcWRVl53LIv50_3YG065MT6AGrZGubuaSBZLc5_u7Cc9aZIfbMIvkNNMytItAtUdslcXARAlUN8SK5a6BgP35nhV5z3zI3-MNBEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRMNFYBeWNoTmmFLjFkag-QLfrO783CZ20w8eHJKV5TXZJT6HY7eyflxJvzU3xeijKpKq8gmKKkOnQ-tIDfeX4sz0it2DbExYRZQevmFALH4P0IyhNOykjNr7h22HG0CCJBnyt78os7H0WTtEm43o4tMAt3KA7l85erjC6IrYHhB320uTb5dnUrFvk0xEMLIspd_aXBXC5ZKeQvfiUrkej6M0StoOQ9E7wINf0CkA4si4Lhpgf4ALD2XWFtW1RHcBhVDj2U6ijIwrS2-6-texGb5YaMyyHrjhT3gLWyuzkUZKubBLbeUTZuEll-iFTBHhLPET6YQPoqahrtuuKl42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PW3youbJP-TrGhinmsnKPE6wrRRtsXItUe6nohFTz1lMRtMZPbxgK_tvCA6EEesA344DZUUpthDdWSsSD7nwlkX1fJL1rqx0S9CQsLJnql5jgG63aH54YScNCEpvzkGx4geAPOpjktHJrfC67LoEK0lP5TbNnVrXNOZ6-je5lTO3yLsRnQ1NDRag1jhNvT9rQsKEhFfvshA83mqp1jR4j8Z_fmDglsrUMTBxzjdlgep4hNv8Aq_V7TzEr-SKNpf3qyNYAv997uwkw-rt2aM0HgqV4txCIUMSAVQx0MRBw1mKPTCRiJyICZF3S_KjKeD0cH0y8YvY4jPZcTo9xLvjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=JlbKNlc0nNFgkw6nN5MCd08O5y0XVsBxNG4GgxWiVCVjIdFyK1TG0t6mm4YkrfhaHwOsyhsky3N8g1jqO4C6ZgZXBl31nDdL0vvy2RraiQRSgu_JPW-wPmUVwdNvbxpv6WgCG_Q_xyrcW9NgkkapTzjM2bCFiVT0iFOUoeg_3RiSEcNSsi9tf1csunjdpiM4hX2b2dg1jLN9Nfkpa7v-APrBd0hi7DUWycerVMbgZdXqUTmyVUeEb71IuPR4skH2doWeNrT9IR1UbWrHvJkN_SH3qotFpgpPrLFdg1BMbpGJ5Ux2lN9AEmsz68klED17in3-PzrFlqoLSWAQLYzgHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=JlbKNlc0nNFgkw6nN5MCd08O5y0XVsBxNG4GgxWiVCVjIdFyK1TG0t6mm4YkrfhaHwOsyhsky3N8g1jqO4C6ZgZXBl31nDdL0vvy2RraiQRSgu_JPW-wPmUVwdNvbxpv6WgCG_Q_xyrcW9NgkkapTzjM2bCFiVT0iFOUoeg_3RiSEcNSsi9tf1csunjdpiM4hX2b2dg1jLN9Nfkpa7v-APrBd0hi7DUWycerVMbgZdXqUTmyVUeEb71IuPR4skH2doWeNrT9IR1UbWrHvJkN_SH3qotFpgpPrLFdg1BMbpGJ5Ux2lN9AEmsz68klED17in3-PzrFlqoLSWAQLYzgHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=MjSZtHb_IyViDamb-4JLybZYNic-9pJ-SZf2DVFBcvIGH9pKB3BuevKzTMxbPQHWHMgYOJBo95EzEwlCjVlBRD5FiZDVpVuGkAYfEufaUAnLV-gtOdIINyGFdL1_sEPcJ6CljW_xVOhblGinu6lbySCdGwRXwulO5_CRR_58WzWLahBbT99uQzOjKzoqAe9MfYgOCas_4Di7kEp7gnrepVPd2BTr4nVQm9t4FcBQDs09gk8h8u3k4H6tZFOG65Y6eZjUZw8BVktKsB1SX9aVA32eg7-qoTqK5vJch1XwzJz0HvOP-rsxMnkUyMrKkdSgSuCMUcVLte188wyYdt0Lyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=MjSZtHb_IyViDamb-4JLybZYNic-9pJ-SZf2DVFBcvIGH9pKB3BuevKzTMxbPQHWHMgYOJBo95EzEwlCjVlBRD5FiZDVpVuGkAYfEufaUAnLV-gtOdIINyGFdL1_sEPcJ6CljW_xVOhblGinu6lbySCdGwRXwulO5_CRR_58WzWLahBbT99uQzOjKzoqAe9MfYgOCas_4Di7kEp7gnrepVPd2BTr4nVQm9t4FcBQDs09gk8h8u3k4H6tZFOG65Y6eZjUZw8BVktKsB1SX9aVA32eg7-qoTqK5vJch1XwzJz0HvOP-rsxMnkUyMrKkdSgSuCMUcVLte188wyYdt0Lyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCFGbl_9G6C9O8-LEV8kp_g0yzf3AJCWwMeG3R0XdJTEiyWbph4swhmoLz5bioYKDK6xy3iwmv9KuwCuiyJOTRvt334C1dmu1mPl4l7iPiLJ89nu8GaP9mwKAJEy8092x575bH8Koog8ejswtI3NxJM73q8aJPy2lcEXQOnsz-vWpEJGqqTPvgx8kBEWeGTgM801JDvoaGZ5Ta9XoR1ps62r0EnnE2zwfsm5269k3zIzGUF4oh5r0JmDd_BkelhaUHkyMSAOxNj3NZfZ3SNFx7TVBz89WgInXu9rGL6h7rMSNOiq2AGvsqMFKodFzfuVhhtACCCam7aSsf2bRY7UNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=ezQH3WqQbXAF1b--gE0rFVNq2_YwcpOMe7UBtJysB6Gg_lBzL8pgxz7l8bZ5us8Epf5X-tF_cXJyGEftf39uA0Saut966cP3eNLDIRkM3jaQxaZRzf5Sp2AISIvDLUH5ZVPnlnycUJsXWxaNP9Fr_H3m-KIRxWmr2Ilb9F0hI8Kyq_IwJpizUxBt3nQS8wPmcGD1lhO66X3sXkUwdSY8cGEx4MnAF_xycJegAD5wYeEWAo_8iPWDwaudn2R4ODHJLw6iG7H_HHHU_7vcLwCRTJ0FE8u3lXa-eW3Ir4m9VOsaw7nYi58lMzqx6GPe8Vy56UvRBVImGvc8Sa5bO38nSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=ezQH3WqQbXAF1b--gE0rFVNq2_YwcpOMe7UBtJysB6Gg_lBzL8pgxz7l8bZ5us8Epf5X-tF_cXJyGEftf39uA0Saut966cP3eNLDIRkM3jaQxaZRzf5Sp2AISIvDLUH5ZVPnlnycUJsXWxaNP9Fr_H3m-KIRxWmr2Ilb9F0hI8Kyq_IwJpizUxBt3nQS8wPmcGD1lhO66X3sXkUwdSY8cGEx4MnAF_xycJegAD5wYeEWAo_8iPWDwaudn2R4ODHJLw6iG7H_HHHU_7vcLwCRTJ0FE8u3lXa-eW3Ir4m9VOsaw7nYi58lMzqx6GPe8Vy56UvRBVImGvc8Sa5bO38nSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS4wHEknQQNcHqm1ciXDp4httScCeqTrMmkXe3-vsDwkcdcEZgwCII8dZgtUGKJAXQEGwqbvFCXig-3U3pbQZ0ymnwYuWBsQNZWdlUoJI2Eiw6HaJYL2agrSrMlRMz2WlejBzreWB0lKGFeXlMHuvcMKAI6gAhA72H1xz2b-HBIvOHg_E_1um9xqUtHOGa8bZm2Gvps3RhX_4kxcbLARzMdjvffN5kD--0lrOkxjXSvB0Xcu5A9KLnQbWv1yD-Sp-52EJjDpsnrCJZWLnVXgN77BQOGzfTA_d8KA7VH8yiHB8owBhhImLNq8UfFD4xjwwJwizGiX1GR7xoOh7xkz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
