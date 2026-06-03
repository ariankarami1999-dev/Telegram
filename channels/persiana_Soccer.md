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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-_mjC_aP1qcHNGN1Q9n--DWU8NWP7GWBTuqtM7vghy7DG9eUd7gaZwdihnY9BIGWYlDYvfcfVkuPIrMrrSSvm1npLOH_SSftQQsuMFVTlWH1gwgxNOxub08F4pj-xNRcO9LDvtq5GjKWo7CgUf4PkSNwuW15VLwDT-khRWQopuIztqCRtEDZh3E2mTalYwy-IRrpVC-oOWgIS4h12sJ0zDBBbCY5qamAAwQ-Va4H80wP78dc7yc0MU-bBvt8jdnj6h0QQ1cNxDju-S5sdoxULDgZE7-htY0SlBxa4GSamTKfRMebZBm12Dl2SrG3ghw_Lo0-LyXc8Cu0yN0deBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViwDVVTofW-QyFaCQspQZe94UO8ZJhHbRINBLaFJxa-ppURfzzulmCi9QnyAT9G-20Y1Eo2eyTrCGrLlhL04qR6n4ogUxkrJip4KzQumUc0DSkzkhPoq_GWuPbF4aDUwi9E6SauL5Of-nqzjG9Us7u6F-d0nJ3xorfDF6h8DZDoOews08Mzjt2DKCvDxOhZqaysRcWr6B-Bk6c0_1844bwzTD9PHrB7Oky05tVvdu7r8zJC40mV_soPNvyLFgT2mIqz4sFk3Jr0qXG1HSZtv0hiAEm8PpZzjLQx573wQs1X_oempw0z-_F4EOSKRPbKD79FdtFhevdI4vq-hyoWgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmtSga1dH4MiOfYH42qP6bOwJDSyDmMa86OR6Zy_j2BotHKYMRiY-E4I29pIK02Q7tdPWcXR_m1NIo_VU6aGglpdpAWLCC0FVaglJX3gjZS_E6H9Zrin1N5g8i5S5pxOs0hjhNMRnmwF_nJLgMxrsCMh_qzxxY1M3cNqB7aiwsJwyayN1jt2vhKr288g7kxYvWWi_rE5xLnKvoQQiz8xorhPlhlrgRwyRDqCKy5M4VAGrGJUIc0FzkUc-S91DJSSkmysURlqKRgz3Dxb2mn1LPKS1a3Pti_swOadRawXrEeFOx2DAObFQYNFG3JT1dq1BG7R6Ua6DxNJGKtaam32Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzbPSeJk5AoTjO-jejYBh7-DEcbUVFX1ivFarE6sj9BkUvax31j0yuyF9guS0A24pQtyOYVE7cnE9DGCO29pCGW8VoyvtvMxRNa14zMBdrP_mJtgfBnNLYNDrz-Xjf3me_PoPVrlBNqPE0Nzw85cB6vCCjUIQdGsoTCdQHsvgSY2kGMmtKt5OkBn3RnPlegMcTAPkbKWodVwcRUg8I0s7-9swadZ3_ZJJLO-Oom-hNP-CFAqbb7gASaqe597L66U-9BcQCuAGUAYXf3PV8Wb_MzZ5EyY0IuKK5Mw5vnyzftXM7bj7wEB7kOhnpuKfV85sAcUeI37aSX9xWX7CTA3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6HEM-ixABX2xogG7uZC5VDgQXBpnSeHmgZ63N0DubowIqSfdebXYJa-VRSzMqpXG4BKWywVTkZBMQwREqywS7OPBFcZgVAEiDCUEh1cdIANPQZdS-_CG-kKDRAysJ-NAB-2KIe43oZW1e0k1LzzJEIHXetpLplei2gyidOd6zmmUEi-CJn0Lk2-itCCDD-vbjAxxg-q-r8R0QCHc9LzPmKvazU26cqJrNj8mTgREgztVA8XXIzMAXvTep_EyygXIT7PBqrJiPxpZVdOVlX9mgcmEfVX4bQPY7DEHlbH3RNDGLEjuzYsh3I888DL-Limoty-Uof6DUkaodYThAWzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0TjJvuq7U9fUDOCYOO4TmZtbXQe8QOKFfJpTXClRYqDdWwX9xwKNwYeDlAu0sv-gSstHfffqFxMX6scKBqLGIB05TC13uQtu1pO5SlBoPm-OwT0RnK2QOFkZ85b51aMPum3aONH6wn86I2FvI95-FfaK-KnKMt0pYG9QCRXhKPZUb4xJ5Vk7caSU4UBALHyHUbzIADjeWbQivsT12prfOj8VNnzHvsykggopLftbKwrJf0V0uXGindtEtaBFnfVk6yg5cZjVs5ZoV9FSpUOgRZ1C4UOLbbXkBsoSJfNDNT4zo_cfiR8_VT-LkRdl0R627Nqn9sN6ERJCSv9ZDPGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW5ZlVoU-oZc6ZZzt6s6FVFCR1qi6l_zRV4RX81Xm9t7ByZ-J8dbQMqlHyjAincTkodxWa-baZQB7KSsPs-XbUK8fwoApPrXlMNSMyvNGjBdONF-Ew9eOzHEYbM00T8jwMVdfC46j94zULsXcgl1PjZrp_nnCE7uqde7LRyGkwitSmZznoOmK-_0YhElh1xx6Xs50TvRHHnAgbWzkgBRwpvdtg1PfDSiCWIelzzS-oAfEMOmjbgPgQBNajpFABvYTwf7-zBczr1UTFKb5K7G0WR16kKlHrTs6Da6_5B4_JcQRLcE4S6JSYlFoB7MqJQxTCxWlfCpA_Q08N1oDbKm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGfmJgX2ZKyFHTABL0BTAj1aeQ2S3SqgrGnJ3Iw7T1wOZ4BN7K7SQdaWrebYgKZ_fKj6Xvsi80CqBisAspnqSaPo-sin0RU1j80YvVvpZuFeNAzhOD-ezr-4KkiRJGB7i6524ox-OdEcvLgyvxL2aWpSS5-tBN21Bra3A_ey3xrMZQQfvYDZPEQTG4VQicIfvN7-LPRSC9YpnPmj4sUbeHmrnqn8k875QV8iAFRUSKw7RpITlgyID6He1I8ZfOQeun94fc5ShWe4rcBp7l0b9Ruxq33tWf6XyzQETClDODmUIvy51XuR3m3KdHUuaM9zzHp3fJsXJyVLisn2XLu7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsGxHBOv0EcIqPsxz-ikA_bNGdL-O3ZWfrNLlfve5I1uMDzJqBt4qskzuR2xgkNBH1kSfKew6gBgegyGr8paINYZ5J5pripq9GfXAt4Udn7UGqhIXhOOLSNIPLEJ6RlZPWiwEVPXgZztXnV3x6uButSck6_dDMYMMFgR2UizE0VN6Xdnz6Kvn7ivpUdEOIawG2qyzaOC5OzdWAk3zk46iBEeyDNLDqxxnOi7RtmPrONBNtr3bn01fh38DE0aKGguBaZOi1iqkHJ6Qtm6nW6HXTY3LvFZLLdQI5YOu4h6amMDtv8UHSX8dPICNtRWGO_9SzhSlnK--YO9MKquroG7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILd3YLSDm71dN_rWvCpOgXOViohS0V6D9uaB10cdt7SCe5GCaF6oID4fKEoq_Kgacey7H1ERxbutEDcIfrY8XaP1rShxggujHvqsDk_XMzaU2CrzFEBNuRlVkf5nohssT4brHll5sgAU7Jo2gmAgCfemgvOOyKxEUA9UiVLWk2BwLYDp-j44G9cuxFtYcOdecGGtB4qJbUTmLIPWDnYjI5xBuEq8oT_NKp4REf8L4hOcetpsfnP-o5J8rQPAsq_95FUnyulST-Au-kD9Y_w9KkBD92a4myOhz5RoMkI-P_6tAXCcCq8ohW8SfdseBsnCYrFhjAqUUtK3_-hLBRRXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=SF_SRwN7UboFJK6jm93MIOcLhoDcl37D_nEjHqvUKNedaUPS00zJbOB5sKUVgqKgnUODepi7MztG4we-cvzHZXOljtkgHNoVEletqYebDmratdwwxbHqibzhSX2ucmGcfDbQvPfVFf6YSuZeQTi-3W5Ki3vfCMZ5K5sxOxCVCAqacKPNK0I-qDRjEq3KEhRxUy7NXd8XR_HkPyp0P8pmeRyru-Ww6HBCP_nikSgUOjTCRrh6ahlbphMClP1OtSv4zEH1IByZVLR3yflRFy6mCOjFAx_ENrdiTs-0eS6ZrynK_tgjVTUDD14NO93AO2i-QyMqqwIqMcQBSk3PyVD3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=SF_SRwN7UboFJK6jm93MIOcLhoDcl37D_nEjHqvUKNedaUPS00zJbOB5sKUVgqKgnUODepi7MztG4we-cvzHZXOljtkgHNoVEletqYebDmratdwwxbHqibzhSX2ucmGcfDbQvPfVFf6YSuZeQTi-3W5Ki3vfCMZ5K5sxOxCVCAqacKPNK0I-qDRjEq3KEhRxUy7NXd8XR_HkPyp0P8pmeRyru-Ww6HBCP_nikSgUOjTCRrh6ahlbphMClP1OtSv4zEH1IByZVLR3yflRFy6mCOjFAx_ENrdiTs-0eS6ZrynK_tgjVTUDD14NO93AO2i-QyMqqwIqMcQBSk3PyVD3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM9jXUAB0jYc80_6R7VOZZMlSkGa1KSZXIXJSnDd5iNADzHWWnApP0v3sEUZuWgQmpc7B5aMtzM7WlcHMCFtsJw4rWFtA9qHWtf9eYTgcZ8khna0GEw8MLAUy3dmBBWGPJvOoTlJRMZAF-C45y_C_gDN9s5pOpbKto4KVv-AIr3V4D7yE_Xk6zF9Nylu8PJV7twKYJq9WjZSZe6K3CzavscwRcCy5D3m-4287nB0gZo5qo_Gt2HHAthlyJFJOZ2VI4vU4xUnMBtl0EJEKN06pP4wGVCI2l_KegpN-_f3p6S5Gy8RlYd-UCMPQtSrXLO0pFvReNnPORxvrLe4xmTH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=KJrQxAHs7Hm3dkJBSmVCFB-BwMJOgU7HV_vnpJ2dQ27Hb278r3bx--0Ae4gNHroPiShl7RaLdWnV3anQKj7XUlN_2lBV9XKWBFYCq6y7YwrTcEt7M_lWUxwO0cdRebhTqga_LSRV8AxfrpiEGbSWHKCWLlryXxxCslMiU_04hZVUHCmDRIA00-d4mS92J8LNUsVjWDj3OPZP6kB1PEC1OPYZkDhjeJr5Pvxe8HhC5tpRif_SIkdb0-K4Oey7vqTYpCiH-k3KvPWHoRu-DxuMUjuZl-fj-bc7-8pkcaMqgV3pAk7Y_QbVY2EnhIeGVkpOi-ePlZjd_dUp6ObXELpsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=KJrQxAHs7Hm3dkJBSmVCFB-BwMJOgU7HV_vnpJ2dQ27Hb278r3bx--0Ae4gNHroPiShl7RaLdWnV3anQKj7XUlN_2lBV9XKWBFYCq6y7YwrTcEt7M_lWUxwO0cdRebhTqga_LSRV8AxfrpiEGbSWHKCWLlryXxxCslMiU_04hZVUHCmDRIA00-d4mS92J8LNUsVjWDj3OPZP6kB1PEC1OPYZkDhjeJr5Pvxe8HhC5tpRif_SIkdb0-K4Oey7vqTYpCiH-k3KvPWHoRu-DxuMUjuZl-fj-bc7-8pkcaMqgV3pAk7Y_QbVY2EnhIeGVkpOi-ePlZjd_dUp6ObXELpsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCkZVDVRozApnxw76FtMANxMg0f8MOYPDF1vEyRwEYU-vPuy2lj2v3cPCA9jwIt-hiL-Bdr-z9XJZP0oCIRFP2xsXVgCx_I92ImdF_Wbl6LSP2hCAu0Xy8rA8BxsDbrCJCCX3VFJUyfPWu_fx9FBufctoCvnv5KdS90_hPkwzBPocVzInSboF25eqjUwEH3Hw8qNb2xWSNswsfQPmz5xHzMiu8XQ7DwG-cO1zK40iMroCmvx00rR_u4ioq8T-bmE7NmUQ4-QD0ATtS9BghKv6xbjp9LCb6jdHsQZBjdPkjnc311iV_TViWV79I5iAG2uzgpxe-5TaLpqmusHhBxHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJIbKkPASs9oiNRJintKZA8xAvnoCZPCq3ri25JvbXl0RJVIT_BeIXEstv7ikiyywYAL6Y9M8H6OVsuOqCeNcJcruLMmjM4Ihqa3c7LGtgpnxg1P40z4QAKOPBe9vV9iMm4lkBjcBqaitBrEOnF_rG2lYfwhgsm8ghEM842VlhifFeUCxxwoi_t1hHkR0mBh95DnwcFq0rVEOVqfYn1y5ivxOcmvAquD5YgVU6x5rBLd6PAR41qKgl-SQ9UggCmxUC1FBefElZK-AhjS2ivXtu-37sozwfiamdqVT1BbnYBA-83w1K1_2CXuVcLPkPFmUIHxb1aamA-XF3FEq2M0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-YEMn2UxOV9iLOlfFcQvJnXbYLVALq0Pv9eWoALvBhvSgHWtCOhF83TKjpLW9ZA9WQcn77GCvsT7XoFwDTSQZ8hhnVJvdXEZFEyyeO028v21DppLWqVT_Qn0dk83kh5_uERDUMPWmdTThykFd_HgLkPqn8mfkVxjPNh4ZaJx-dWRuNS0AbLyK9uQin8NnIlSfXsEy23C92i0Ew2gJKpIO8qRezs5LimskM2QX9qb5t3oRG0m1jbPUms83PpmKJdqSslk9aRtVuHxGsE-zaOm1WfqlF8e5_mL2OPS9VOP9lgnSjwHvEO5q1XGhTEEpkq33ZxPk1DeIZkGaR4-t9WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT1C5NRituRP1PkES2LugngbA58IhsAQYy0coNLkyLFgLoQ8GPvk29XMeKKDiyu41Ab_dB2NUZ9Zk3hzJwowEUznNH0JH6Q5aiEpag6RXrY4jNiylV5VrXN7WGAalwfUbUIA-sKYckJERbK_JQ4_DKCxrjdX3b7iGfz3s0cVNRKXFCT5bXAwn4a7-sqjEzCfI2nSokPwEVKqnH1pi7HLqaTahXOI0gtduzoBHfrq-aBqexEXNESE0dMMq2CXYhuIbQ5YYt-HBPDssWLEoNc_LbhoJXKJ3umzjSLE8cPeKX4dDjjECGJ-_B8m_SMC2HZH-ZyzBBhPIN0kaNy2O4Xrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=SQ0ud1HREJssr4tY7QX2ZTklkzPjQq5j-XSGoPUxLcWRMph7Qz3HRGyE-cUARig-zKjfUnkahtSg-HsDAWRQBM7g_wHT-eF_tYgKPbgY-0s0DXaJ50POaYNOInck3SOLVSu4MDMRH2pmbFvxvwoZEdTRoTcYZUtEwcKDJdPsxvo7ueV2UjDNlgV0TN2o2PxCUpIyJMJwrchrEFMIH8GIyXWv6OKeA14yDo_KBa5gCkXkVYXNqiakaxL70-GO25bTXPvycplu44wYr8dwHZLC_c-cQ11rBFtuAs6VMQfKenQ22aT7C4YTjvfEx9F__ALa17gSv3egbRzTOVJgcSd7Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=SQ0ud1HREJssr4tY7QX2ZTklkzPjQq5j-XSGoPUxLcWRMph7Qz3HRGyE-cUARig-zKjfUnkahtSg-HsDAWRQBM7g_wHT-eF_tYgKPbgY-0s0DXaJ50POaYNOInck3SOLVSu4MDMRH2pmbFvxvwoZEdTRoTcYZUtEwcKDJdPsxvo7ueV2UjDNlgV0TN2o2PxCUpIyJMJwrchrEFMIH8GIyXWv6OKeA14yDo_KBa5gCkXkVYXNqiakaxL70-GO25bTXPvycplu44wYr8dwHZLC_c-cQ11rBFtuAs6VMQfKenQ22aT7C4YTjvfEx9F__ALa17gSv3egbRzTOVJgcSd7Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg70vCUiqqDzJQQ1yxT9zpMovM9smRml_pcOz1EsUvcT45XLktlzURHRl-EpikuFYCIQjMak7ovsCZScdWkCQgtcoilHEJAkWPVWu9rj6QINeM_7Wrsb_B9vamqsYStrkmWb6jsz_QCBSsLvE7jhetNB4s-Ml3gUmAVYPGNGGqMd8W2EDcMhuFIbFNVRcb3jSung1M55uFCIhZ07YOhhiTyH_cx3sttDTnUb7eOkMFHGWPBFYoi7jBYwMG5Iv1FHgOlRKDm4kGtXwz2Hln-doSRuZORnYWiyp7BKS2Wg38HDlU7URxAyxjnJMWJEf9sq2npQZtl-XwAGplycp7nFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBgok5Jb0oOFaA2A20s6p_dmYRdHbR1-ozDcdyEJPWthFuJoXzbMWpTcaRANVVn0Q-684fJ2DHBA76cqSAdKF2W2Vo2aPT63sopvFPzT-6cJ7g2XNUrXhOPE-CsXQsFzTwozKvBO5u_2jgu2IgVmIH1Z7Np4HV3pr9KVHL7KdaGq5v_1EjoMeZFWHhdGFRmcYahugqGhb5Q_q3pY35jBeRr_m6Ll2i2p-RiDuMJh-d_O1uyfRMfaTVc7VcPzNCOZffvf0Vv33p_Y6OJ6zh95qwAu0_caa92yr9YfKnwZctQ6oQ5SJ6mnjgf0ljwc49AGwRsikbAKwhU9Sbmp280bcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22672">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvdNvXKEFQOHH3ywSbZLQ8rC47uKnGuurD3imvdi0sTstSX4TE6eI6vDfogiRxqnKOKLafCmSu2oAtnRbd0N8QDV7bxJc4eV15x4QAuNLwGgWvbPoR8Zet2dfGQj29gzyxay2VgyFAuS4MXQsBvEUUPgRXemi676oR2XRYgrbF-8MUmeq3CCh1184lIEZt6uban-z1qHjVm_m40l6Fv1lKUb8znKf5bNk2cz7aIphTkgEVd7uqeCNDVb3YD81_V9uRuQcpOMbDvGO9RPBZTrgFkWokAXUXoCONQFrlMsRMvuKA7MNoI9yZfx2LLjCYvWojCNgiJ-qT6DN_K5BbllQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22672" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuGgDNnwy0StxNjRcTRib9tERRIm_4l_9Z6QQBEjCqGMd8KrjxiviatvQTPp55-xgtuD6G-nDr_40RgpjwQIAYcf-XrzxRqxgW06ASAb8F1bmCZBlTBR0wZ4JKz68NKxLb5izREIXUbStDac4wwBKjHUf-qWmT50SyRdJ5AycOp_ja3jtbJGgXRlbuTTnugzCV8FATRG2v9ffJLFVAQAs8LXWS7wz_dyaYUcwWCNjduOa92qwhA6_d_Y5NUNadpNt_I7pfsMTVfLyhAJGTDuYRKifLIiLcw13OcVzNGb_IUs8jM552cj8iB581MXApFNXXrh7dPzNJ46IInp_bholQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0_V4BKh58KqUmqJPVUPbVj94d7U1GEmEJ5IleIvB3M83qmzKH8YL-hHRMthkZfnm6NlFs2puRWmNppieUJiCxxbB-YFr7gaHvw9Pgifh0EuPnCFMBgU62i42Vzjh0-Ybtkb0uScZawh03sML5ar8FkfWYdaPYz2a0gZXRF4nsHNXeyaRtCZ6N2gDClEj2aI2ai9e92bpZm7QIgfY_aTyf29tF_Gijo0VxL4-mJCqU_SJ9oSHvBEbi8XaMIXomQgSXn8zb5amcN5U4lAE13aDwmG23M_Y6elUhXZxnK-ryg9hcccwEPMEPPWUzWE8mWvNDb_TWuM5mSpzWVFxcOFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdiHLegJF0aDHhW5T2hiNdhwfzQMKINvCBRpKuif5BzugkkTtUptqUA25wrBUxmtpWiJAvjiNO96EEkdl3jHaHr1K4vn54Fg-Yya31W2inkYEXPTbhq86KhQXZ2tiFXIxtRfM_nEnB1tpn5MEAKTXqTMx77-ExmLyjRwiWyJl9Tn6jv7k0grpK-cXdTrbp6jaG0TWnLjCipt2pZvObvaVK2jpQtZtJzJ-MtqEi3GmKiDSSiEvYk2LCmky-_0RP1wVTluLtdoK2vu7Y4-7OsHUbPQLuHs_FcLq7lhILo1iK6fFowN_o5m95y4H8MdV4EMhxhmhKjGRf4EHeUS6bUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A19AXaBJ0NmQp7V4dlU3oiAkl9BbMWfIZgo1-PrvdvKyKA8U1oOH9cvB0Z5Wxn2pH17yUcnWwWbmqlEmpo1PFziDko6GJGaaVN696HHlamiG91Pp8H8pEF-Ial-hz614_frWA6a8aBNL4x6MZ_VCY_L48hzwyywjVkRwYsG946d50Nan9uWm6cBjD8Cpu3uqFLCRWr7T_CFu81F6H7cPJxJO3u5OxOm34cwrSvYR0SQTrWLKE2ZXeOnBJglf05wdPQyiTfwlI_jAYAcGniXlvCjpIWA1Jp6elJJ4R5oUFkSiYALPbLxPCBcoYsn10zi05j0i5PdZorpEIE4n7VtFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWw8_oNTXO5uHaY8kW6LsQx1l82C9DT9Zc0VEruJjfG9eDurj0Ec8rywzgTC_BndJUpYh4zeHPVb5QXR81qpuppCEBJPMRfwhzjQeVfXfPR1z1W_KIWgfTuntPV2_2DMo9SWTbEM296sJdYtLwYJ-ZkBEk2GZQvk0bCV22ZBvJYduoBuAGuvcGZEAQQ94m_LXzd1UpPwjNAsVIdU7Jvjq-XiZjsVySN4Uk0hh5lPqg2S6mply7xrZjTvgYbSs1liONk6m1JAtx-UlDKqpWD-plwNxsDNZj_zX2wtp2lc6mMrKKeEe1qfB4GnHsqm6FUPnNgQ9G6W7rMnNQi2Gv1zRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifFjPc3PkFn8Us9FEI7jYx8J2xEk6cB7irb2CIBEFJk5Sr20bc-w1iut5Qps-vjP7C85D57Xblp8stzj-Wnf3Q3OPGHrhs3o_5m-PBHr5oEDePlHAcJ3-UrEl5-Hk3Q03Zjm2YAe1RZvJqCPiNyBe26Gqhb1Vy7JK_0f9GRKZvVc2RT4qhMYZOx6ft-JI04C5iO8UUWko7fuPSypfhZ4RBHrThusZiVnaGH-jsI_m3XkxTW5EQGjbHEbwy79FCpGmmVHX3ppGCm33UUtx_fwdp3QhOXLWc38qiDgJ7KM0leHPR17-eCId6XiX7XRMBj4Kj8X5dlCrAJvqYyZFSIVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4_4KSgRVaAak2zFOFHwk-T-el6DIKkt79MeEz5FGYegvlL8MjnwaejClQgj6E4t77OxvwTzcGqgyJJ4dJHDaG5ROc2bZlUNlhqdzFMLwF_AS95E9EqefAS-cN7xvwTVH3gopq4EOUqS_YWarFE0whQAkCPzNPRM-1Lxk7o5yq4TQNJMlwJ8EIdNDba-5jiNoGwoNBLSN3QjKqdKIOf2_Ox1PA9cDYTid-XoR_e5erQ9xOjhR5FZqhfIp5SNtKNOeovUfFRHFBAyN5vEJBqwii-qux9yYXxdq2Ky4cqPQ_lL5in0Q3paSmgy81KIqlPHf3s9QqtSSU4v1RoLnrfUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTXAfEtv9Kksdig14EgNZKCYy8EX6C-Pqeg705TtHBan-y-3gTxCXE-c2FX7HOytUM-b7NwZXxPUlRS4PMgON7-qYOZUpoQubRCFESthBqAnvzbJApbkqD24aFCoHqv-qlUkL_a_gF6w3OJweMFsJcnL6kpG1aeqtFzOtJogIBbRkCoLGuNYZYVqOhCh5v9TPq95sC5LNNWZaG8BzEihZD17oYS__dZF2vQMSU0hjeclZYzXT4z2MFN6iBgFtp5wIUQckIml1aGkyAwEzYeCeyU3rHC1ghQersdWVIilF2WAL_kr7ZRNnWE_zr6Kxw6NAEXcJib5I5lajVk9-YxQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkh2e7QAmjgUASq_i3Jw-MzQmwF9Dr87qGdxx7gKlyahPpUOPWnGOqz3glYz78phMmkzt_z9Lk3c24M8ZqodmozlYiyYqvpXrfLS2Kx90QlQD8jCTg2z3uvqNSkJj4AIk_6mhNtI4uPCzqQyqXS4UTjVVq_MYXc46M1nyz03-sbMTF7zxRjCtslCTcVCmoBrqyAlmRyTm2Og2ErjPgaBTWexkMH2eJWn2piash-jQwdPQlU94Hm-K3MgEwSzeW07Ci4mN6MR2xdp2i47PYSPNfabtKDrwMwJsSC6ilXYGxhnSV-SaN4nXdfSCNRB4VOvlmFUBMecJrVUzs99sDXMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHRwMIuO-RTa_NA9X2enUWdgvZBrnuDr5TvRdERPhlPwqqwAhC-dcJofLerC58euGGKrDHjxfDSPFNoylai349MPNmK48mT1gYeL2FTbOrk51tlM0XxetgjGR119T9qCyBiJDSWFsYXhLnMaFN29H-ub_bMvFRmUxr8HqcVZxkL0X4jIqhlUgbDaTf-VVdXy-LMdaBNik188WQwPMVy5v75Vbe_pggah-69cLmK1iBW1yFMMqYPoCJVfDIb2qkhgJ49Q-U2CEv6ZMhlhDG1snwJbK6hzm7P6PTtsW5ZgBCXpFCciSp5QZboC2ioJoxXvW_f_Ncg3p5YdwGj0JyWosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7ctT3kD3y1UYEeQMiFz4atZUHocT3z6jvboTruLpzIPuAcp9nnWazEn63JXUvO4zLVwxfBAkqfPICwzGx6LUR1qukaIm2XQJvQ83a_k-Azcy2Jhnw4dE2zkZuULX5CIFGSPGv9bRhN8QtgqI1zfbAirgADd4Qbzy59Qg7AYX3y71jcn6ZcODwLpIIEGZuOqJvZE-7Eu7HF6u3hikijoXBHK3tOH7_OlcxOk2KMtrkQq_ZxI-NzYY1bHetDBH328XPlirmYZ_C7E_CE7h1MJdtlh14Gom2euS-bUB2Ya_fQsPVaA-k-tYr_PwnZJv_9EfRsE7_kdHxYW60MGzzi6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=RM5ux8xOwEeUdDVGrBjAzscWZ44DZhbDW6z7FCKaEwuKi5blOVJEQDgcBvVovuDqyayhDBNYpx0OHl8sOxKJP6k13ZiBZP18KT6yrNxGsFyz1KGOOPY7HnqL74RZitORSqjyYa62VTRF6T1H7pFEohDK1OmbOzsxPHOTWIceKmQou3Y21k0wx1WFrFsE9OnqwfzDMV5kAkKeniFpgfGRZw2Y1aJNLcT5OXsoNFLLR_OzmZlVXNAFZe8AvTP51lQoT1MFkG-jV6rTVPrIO3i2X45VzkoSuo9HztzyG94kUcD9Vkm6tt0pxJyZ01otWPDXvu0RlmToR2FKngH7yyl-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=RM5ux8xOwEeUdDVGrBjAzscWZ44DZhbDW6z7FCKaEwuKi5blOVJEQDgcBvVovuDqyayhDBNYpx0OHl8sOxKJP6k13ZiBZP18KT6yrNxGsFyz1KGOOPY7HnqL74RZitORSqjyYa62VTRF6T1H7pFEohDK1OmbOzsxPHOTWIceKmQou3Y21k0wx1WFrFsE9OnqwfzDMV5kAkKeniFpgfGRZw2Y1aJNLcT5OXsoNFLLR_OzmZlVXNAFZe8AvTP51lQoT1MFkG-jV6rTVPrIO3i2X45VzkoSuo9HztzyG94kUcD9Vkm6tt0pxJyZ01otWPDXvu0RlmToR2FKngH7yyl-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arq-hx9DIcrLnVCu4REkjA3knNdlUoYEAjiKmlQnMpJaQbxA85Xm59d7W8rR1Y-0umKPJYZ7hPu9-6Otv4MTbNNqbycMvSEENbKmXgEoTGe7vihxNIcpZ5x3WV13DCHj184hDP7qliuOkpbueJkYrZtXudu4EcCucGc-cAhGVYvqbiONeuRZrN1XfEicBQMBk09ha3Y1wyyf0_tyApzO_9EwcvnlrseXUfvusAqqkFh1_AhT3xGu0CdVOm1m5dN2gmfXHSyhSEiCIc4w4FPPOe9ulvFN6j8NzhyDJ1a43W5Rz7zgHi6ar6Rw-SnVu84P3lrLM2tONedPUJn-fa258A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxYhIQBA9227FrUgo8QugHXyq3lllJpreEPy_O7mcjxhFn6kWDnPaDOcLC6839r9Bsh8hzRdQ7VL8CCOQevvbu8UBYNkZj-_4hhwOre5M4p5Xwkdp5w_rwpXWxS0uev0YYVe_M2Kx3ZV07dIs3or5iY5fz9J8WUbiVbcfu_6fUElPi1hrMwnuPU2fXbJYpDel6gF76w5PXCnb3NeoCQYZFjEGpPy3amOJizT78xHB_nMaEXb8nGStr2ozV8t0-BI8SuaSrfiQh2c7KOb4jX3TUqrpe4cNEb5Buh7LYIwjFFHytA7ow_NgxZnAVAgvL4MJvO1sR3Ed1DUnp4SCeSeeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=NM_a23v-oj-TNznAMwYLZKUP0Jegb9xAJfJ5vdqNobfp2v7aNM8J-083f5MJrEeZEk04yC7JZS_X1HJAW5nuXCFh397NTgOWfc3C4hQnKyMAGmsS9EFM94Ms0lit4okRvh_q6crnBBLrRYEbvCtC4x6yH9cCkqFQQMTvfbrLmD8qhEB1hItwWKxQZdzGRBqGAbKH-MnYZpTzvfIXKMcKVS4Z9s3UxbWDhHEi02c7x8cU7kKMJ5ze49Kx8DEtBKvxVqA85g523LAzzVZ27r1V40pXFK_F1CMLnLFnyJMIQjc2KGZatw97IGSGZnEKdXNyeJNnTY1gMx0tGoeWxIrx35VFib23CLiE-eikx5-CZTqjt78jppz6mWhi9l0sYCygDn5cC7jE_jIAH9Cd51G3EFTxnVaQ0n_WYZnElJdDgCuElYm6Qxkp_v0i448DkVZd4FqcFdd4thbD34Y4g-F1TfGb8_g55vN2fP0Ypgxh0Q_QE8c2nlLpYogEIP3ktf-Po-lQrLfTBFLnwXG_ms4ccyXk092vs5bZTtJ8oFXW_7qOrGdn4noHGN_SLM6_y868DNuwtnxSRufbEvh0z6Fregs7PjLItEqerRLuekMBnJKSytg6bGnRwfHBHtAJUdUbMxFoZ38-9wFA-gfOVInoAug9tZSDCPJV6EGXQm4P8l4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=NM_a23v-oj-TNznAMwYLZKUP0Jegb9xAJfJ5vdqNobfp2v7aNM8J-083f5MJrEeZEk04yC7JZS_X1HJAW5nuXCFh397NTgOWfc3C4hQnKyMAGmsS9EFM94Ms0lit4okRvh_q6crnBBLrRYEbvCtC4x6yH9cCkqFQQMTvfbrLmD8qhEB1hItwWKxQZdzGRBqGAbKH-MnYZpTzvfIXKMcKVS4Z9s3UxbWDhHEi02c7x8cU7kKMJ5ze49Kx8DEtBKvxVqA85g523LAzzVZ27r1V40pXFK_F1CMLnLFnyJMIQjc2KGZatw97IGSGZnEKdXNyeJNnTY1gMx0tGoeWxIrx35VFib23CLiE-eikx5-CZTqjt78jppz6mWhi9l0sYCygDn5cC7jE_jIAH9Cd51G3EFTxnVaQ0n_WYZnElJdDgCuElYm6Qxkp_v0i448DkVZd4FqcFdd4thbD34Y4g-F1TfGb8_g55vN2fP0Ypgxh0Q_QE8c2nlLpYogEIP3ktf-Po-lQrLfTBFLnwXG_ms4ccyXk092vs5bZTtJ8oFXW_7qOrGdn4noHGN_SLM6_y868DNuwtnxSRufbEvh0z6Fregs7PjLItEqerRLuekMBnJKSytg6bGnRwfHBHtAJUdUbMxFoZ38-9wFA-gfOVInoAug9tZSDCPJV6EGXQm4P8l4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTCSzpZdx1HXfGPGqIWDMj42PwX1g-HoG_KQiejsMs7xRvMsihTTGUr--Kl0CApaoKktj-s8eMRtvriaE9KAr90IF4pmv2HWOmNG0jmU50ZmaLYSgkte_h4hCQc2OqtqgKF_TJlO86pRhDoZL8f6NDOgHkK1M-CIhXw8oUy6CBwStNAfYh3J25qqhhdzoBGRLKHEOauEgO8Ky08rGg8XsBVg37b5u3zfMdiRwVunL3fJ8jfGN-xF5NwsRCmvPkbleCDfrMCBtJKAN2DdKa0f6JeqijRxMOKsr_RggIwbndtY87Kszrqtj1J4HwfAJHXly-E3L1DXwTaN6JxFVlnB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=I3BB7D_Rlci6T4MfNrETJlbSIX43N1kkhgK0OHXSlFzTGqOQMpn8y44-qa6ERzO8C9aROBQOveS6A0-CIeQewJ1HDIzqdoUIvYZz-6jldfKxZK8U-i2rtEjMMah_Sd3L1EhV6nli_N1Y-MAbJQo735Ax7B1IHCBuxCZuAhhh_rFT1fogmy_qTxrJAjDI5QpwzYPnswDwi--18F-iZNeQ_MbNPqI48aMwTKUvPVBZPGLMCymwpD7WPgEBgk1Wf_lmmhPJjln7H_g5CPuzQBMgASe08IKwL42oY81dY8zYvDKxroUJuRYJQBYqBpjnGRmDY27l5MKBIAxu5nPO_oJnl7N5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=I3BB7D_Rlci6T4MfNrETJlbSIX43N1kkhgK0OHXSlFzTGqOQMpn8y44-qa6ERzO8C9aROBQOveS6A0-CIeQewJ1HDIzqdoUIvYZz-6jldfKxZK8U-i2rtEjMMah_Sd3L1EhV6nli_N1Y-MAbJQo735Ax7B1IHCBuxCZuAhhh_rFT1fogmy_qTxrJAjDI5QpwzYPnswDwi--18F-iZNeQ_MbNPqI48aMwTKUvPVBZPGLMCymwpD7WPgEBgk1Wf_lmmhPJjln7H_g5CPuzQBMgASe08IKwL42oY81dY8zYvDKxroUJuRYJQBYqBpjnGRmDY27l5MKBIAxu5nPO_oJnl7N5or-ZSNyIUFeFKqktZgsQhxOFkNe64mqrLykoJWxTkEZDfyLNNRZEQoZ04eTtqcrinYnaXktNAZGC4esB5HrTEvHFtwN8b0uoyKc7isdBGBaOF49U6r3ODXzlQJytwPf--Hnfk6EeRvRiFQiqd36vuKDuRNufy___pT8eYrwyNoxQR5RIHiMbs0wHsUu88vhsmygLh5bTTTnKbfkjviV1i2zUOom2Ww73OmG5DoUc-gk5tLUTYa8asihUf27NUBRv5_qdke-cQUjPhEB36hhnDAHFFLerfHW8HBZQlxEQcHOtmTiAL9nIb1XMdu7vzniQDZ9eEWWTBxycwig2QKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=daVJ79f-t0DgsfERBQLHWEX91u1ISCq5aLFp3ryGkW4hBs6GTmJVaWsDtzTlNpJzbpaEd8uhI1HwQZ-y_xOSkPaeie_ceWbMeyNhM6MR5riwIIdnXsphzQel7dRSwHK-UusDFN9-Aa8O1vvPWQbU_6A2GMC-tWMI2rKmSnorR3ZeMg6u0il4mQjUd3GaeGTBUJSNp13eAVv9GY-lLY4PJ8obuHF8C5XeTMpi8CGHDxywM49iu8awnwjXj4e-QyBqcOBwy4gYKwMXzJpzeghm2iEndCb_UxerP_2rZ6f7xc7Kd-w7ULURKR__zO9FO-I0ySHXf2eOY58WZdR560gs4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=daVJ79f-t0DgsfERBQLHWEX91u1ISCq5aLFp3ryGkW4hBs6GTmJVaWsDtzTlNpJzbpaEd8uhI1HwQZ-y_xOSkPaeie_ceWbMeyNhM6MR5riwIIdnXsphzQel7dRSwHK-UusDFN9-Aa8O1vvPWQbU_6A2GMC-tWMI2rKmSnorR3ZeMg6u0il4mQjUd3GaeGTBUJSNp13eAVv9GY-lLY4PJ8obuHF8C5XeTMpi8CGHDxywM49iu8awnwjXj4e-QyBqcOBwy4gYKwMXzJpzeghm2iEndCb_UxerP_2rZ6f7xc7Kd-w7ULURKR__zO9FO-I0ySHXf2eOY58WZdR560gs4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rek4dtiLeTI3F4-k8KZTLPAqLengXb3REsIcSMCTHy9tzZrelluYAgUY5nCgimQSL7znkSQvn0o8nUFICMupHEPSiQhQKo96Q5l5EadNlKifUUVt8cqw8oHicWem7sssEA_JpPx075jTRMskEpuVbETbFRiyejJZfopkEOZjZjfafYgDfRGZc1t3dOo3FpMYQQZWuFgLsm4Wn_gtWqU7GiKrdqE_w_J1RWUPcFVGCVlkg5oIOFEbE9tyeHQ_Z9qMjeDXOzr7KoffT-a9JRKDVTths1n1fu7WvI01HUQvp9FE-RS_Udlt8OLWwDRZ6q_4poFZowbmq6zl7nyw7EcILQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22651" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIvfWeQPrgNbipe9WZnZXTpe-CoR3EGgCB97vbx9BrIM6TfWqNiVXyPYc5TPIdyupWD_VfV3syOqOBU7QVznS8hgffbwHfRaIqbSaII5fpY8NwMR1oFjw5qLUJCjTEjhhcpOXo1spHHMZsP4Lo2GnzeBhMY2efg38vO-BLElwbzVF0AoYm5IlxyQuEzbWkddcLTpiNhc13se_2D71Qfr6q4ng9MeRVmJZnFs-Pb8xsK8KWSdDfN6RSdfZDFN71ifq_tQOtg84rIGYV6OAukZuK8kuRV7qaNP2W-jhCdLx9f1IGcFjRjtIIwWvCza7pyg6RW3VpGQZOe1ZcmHhSYyuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVGQVhy_-rjyPu5AxUbhgBKQOhE4s1BtkHRLxG-3s4ROG03WLE80lJl6TU2_406kru9I0mek1X_tMfRlIShQJz2-r8-eVHdXpGI7kJ07pfaAFZtJTxqWDhNqb_rUuIn9UkylE_Uk0OCnaXtgdEaMAVwNXeyQzUt3LGAgpMAIl1rMtS065RNjFHmQFjwJSxROL2ovAbo9qZLcpyxXHGoy2sOV0CfVMaJgRapjPtQRL0q7o0nnnW5iLnFQlzDLGUOQwbikRpH_bQqsYWO5xT--5pzbW1IVTN-Xe_jxRTzyk4EqlFKsTJuD7mI8olBTLSZjLorLqR5OjGGb0SEL9xr0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-S4cXVR4v6DdQn-qU1AfDe1xTsbw-zMkRVthJdL2hpdfm83JVpEXR1qqMaNM-dMkTAq59aFbSiaoI-KA9wuWNR-Po0GZceK4qriKTi-fXp4hlxDoDn0IZhKpr5TISNaErFx9ZqbapMgdseZnbDLBMhe2VBscpVn-OJvIaO2SK3Kj-B8fBhdnMphwUU8syJT-fUP0xcWqw7sxiIcB36fjeAzjEO2D81G1uXX3djMIdX86KdvQ5xnLQJoxU-Xn1StY8_rKn26vIkcSgfR1MEhIG1hWCb2o5drYZDgeCRV2HG6xcQCM_L1lXAfmF0fCa_rgUtgQYNPtq4h5B2h1LZNrg-20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-S4cXVR4v6DdQn-qU1AfDe1xTsbw-zMkRVthJdL2hpdfm83JVpEXR1qqMaNM-dMkTAq59aFbSiaoI-KA9wuWNR-Po0GZceK4qriKTi-fXp4hlxDoDn0IZhKpr5TISNaErFx9ZqbapMgdseZnbDLBMhe2VBscpVn-OJvIaO2SK3Kj-B8fBhdnMphwUU8syJT-fUP0xcWqw7sxiIcB36fjeAzjEO2D81G1uXX3djMIdX86KdvQ5xnLQJoxU-Xn1StY8_rKn26vIkcSgfR1MEhIG1hWCb2o5drYZDgeCRV2HG6xcQCM_L1lXAfmF0fCa_rgUtgQYNPtq4h5B2h1LZNrg-20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHgLBvxOJHA36R3Ilypq2r2r7FgAq0orDJ6WfUTw6dxWDntRCtc07wFmJKigrbOzVRu9RMgNJ_HuwcpTgTPCzHTRpTO2gKRCLDP9C7YIhgGUuS2uoKNBZsnBndh6Tpm6jjBnK2f-kB1XfKDFNR_k87CDAWV8fZ3Ru6sq37jBE2UE7Sw7GVlcmV0CEc6Zs00kwX1JJsNd2ne5KHZCDs409vA8FkMWNd8-EgzsJmmTgacJW8koOx7lpWDTpaqc5sFmx8spKZojmb2jZ00YweD6y1c_JTypivMOpsorDI-uuV4IwJONbjMkpBe31IiqTSMPIjY7GxgQ50aQCT0s9XNExw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oENe-lD_9hdSchANHf6mWYUFUKrTHAHzQy59OKaIr_cBN8IsjhlL7CmJRkGLUecxdzXV2xZOQllTPTieNzodEvd4KA4b_A1oy_ApdVDQ5KSmdqGdZhuI8iixrVKF2iRrcsWdYzbbWpNlRHdNNWNLOhDlmraKudh1Ln8-cjKyzbNIhICf0BOnqd7f_7ew7jyjFUNZPiqFCoBwNHCexf-t92lIuPENuCaT_ofBuZHC61Ne5caQUzgPnVjnrC-ZwqX-HSZ3Hou0Eee44giy8txArj_fFRbSnN2245vYyhKDrtwnJffRxCrafjGxDi03YexBD7ct1iZlmZwd5FRQoH2tPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tz23q0JcieegZPRZ5INY-vNIVXzJVZdZdFADLcxeuDf8Wj6TC942Fjf0IUQcNtW5rhmLLi39AcI2_lSf944PvvAjDUxoFEOgaoj0McoZx4z_YmUi4U9j0dwu8jTvkVugzZXtRnPuFD4SYHENJvJRK8JOr2KjxCAW-tYpf2yS6XCcL4FX9rS58MxoGZZxK-oyWGJFQyHiA8qy9VxQu-zduDFgHleBTLbesBBBqC7F-r90JEU2w39ETqh2Qyeu9JmgGedVoxOmB7qW0f5oPwtsmnuwDimMfo70fH_A8AUj1LoNyydgLEOnPNKJ_h6APCLrWX9XNoQXPblLrqxshDnboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGHAfTiEpDRDvLqTIU9680JjmkBQOWE8UlO_vNmxeKeq7WV8garxqNbpuq0n5yMA1ArL6aq6KxxY6iEksSn_obES_Lbhuprc2YkUMrAsNBIUCBlbalPF30toIxHCc34rD9c9Huqxrr-98Db0Hutpe7TkRAJV_jzABkos36K2144mAijoaDhWR5gzlxDSybBDN-fBcire9ivQmdzizFZFAfmGz3oHdvqC84cGvu_g853Skm-xd_-L-AZeBAXCV449wryNwOhXuYF8qqQl9h2yJ6Wqb3076SQ7CdauwZyxDfSagwlhwEda4KAA2rjOvCS4ZMMzh9eIVjB3fDnebwOKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC1CIMzshwSFrykc7t05aM2bI2RDEAw8H5iVLXEX-u2CZrnfz1NRZq_By35MU0Wui3l561ED3hMh_gPCdEUObTXN6w1NEUJymKPuRBRCdFiaSpGfqlv-gvBn2wdwL7Fkoh4jekXLpdAYZxEF5KWeA8WIWZ7x-cV_Z76wo_lYGeIqMktqAyiS5bQNjD5sWhH014aMF1NPxvgbO6njGpXUWeoXN70Bh4rNmI07ZohHvfYhN0DGxPRi0rXv9CNe68v9Vk7uZKuPbwr8mpn86wwQUEQyLdFHYnPRFoO1x8aNVjrEsKBI9uvzDa7ENRtROPX918Dh2ofykh68cAlEPPSKkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=ThMdgsJ1ceVi0myhNTAmgJ_lyeInxUqvnlZ1PB8V0z8bFe8G4_l0xhY72qEnVFubZ4Y-2bUujMCyuyOO4MM-NzbCGZAYNq0GoRpymxPTIzxALwT6osggP86bdZ2jXwB7wht3hlp1PKQuwTRfyuoZWiVKC0mm1pUG96gxoDdUeJ9pgdbJnGUIDmZvDfBMvNs_tzEPZ5zWHTtoXGFBYDSntONHTnblwj-gSFf3QCHXVoe36IZU5znJddg_shW_m7tMKFpDONa8GUHiXaijMO2lzqQ7h-D3dW9guGqjAuTkOKRW8hv38SW3qL-bYSXevRZwPyLrXIlmmzp0mczOgBUwnwvIF2ZK1QAalIJTTM7A3fNMUrR9k_DcizFmh8zEUWPaQw76Cm7adwI3VH9AjaPvr55jceJfd8ck8hqJjmthE5rOrGUec-ZNezGeQnCjLKOzF3gocUbxq8HrQxJcb8AlSH0B7T1yu80D9MqqHamD6k8Z8lh2vf6IFEAksk--uhX9Th-1fyTCQ6xE7DfAxIMNN4PQJ7F6awoU9B88LUr4BE3ZROsnWKipdBzJQQHSHCgui3DUEvufpuXEbM9L62jJNIFPl3opKr5Qo8AZC2F_6lbbM_Q2Fq2gXwLE3U9REhTcxncdCxz9sQyqi82sFCuvbzJREHq4fHVJuTDX-hfqYPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=ThMdgsJ1ceVi0myhNTAmgJ_lyeInxUqvnlZ1PB8V0z8bFe8G4_l0xhY72qEnVFubZ4Y-2bUujMCyuyOO4MM-NzbCGZAYNq0GoRpymxPTIzxALwT6osggP86bdZ2jXwB7wht3hlp1PKQuwTRfyuoZWiVKC0mm1pUG96gxoDdUeJ9pgdbJnGUIDmZvDfBMvNs_tzEPZ5zWHTtoXGFBYDSntONHTnblwj-gSFf3QCHXVoe36IZU5znJddg_shW_m7tMKFpDONa8GUHiXaijMO2lzqQ7h-D3dW9guGqjAuTkOKRW8hv38SW3qL-bYSXevRZwPyLrXIlmmzp0mczOgBUwnwvIF2ZK1QAalIJTTM7A3fNMUrR9k_DcizFmh8zEUWPaQw76Cm7adwI3VH9AjaPvr55jceJfd8ck8hqJjmthE5rOrGUec-ZNezGeQnCjLKOzF3gocUbxq8HrQxJcb8AlSH0B7T1yu80D9MqqHamD6k8Z8lh2vf6IFEAksk--uhX9Th-1fyTCQ6xE7DfAxIMNN4PQJ7F6awoU9B88LUr4BE3ZROsnWKipdBzJQQHSHCgui3DUEvufpuXEbM9L62jJNIFPl3opKr5Qo8AZC2F_6lbbM_Q2Fq2gXwLE3U9REhTcxncdCxz9sQyqi82sFCuvbzJREHq4fHVJuTDX-hfqYPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KexRCInqJdSvbC3-JHiE2gdbXoC3wwrUIxcYBfKMTqiIJoN5DMg52ZcF2YasHNJFTifyUWGk7nYnCz-NF4Oj_yRE1i_vTkK6WL3RAef3HldboI3ejIqYXkqxdBIhYxFYFwklcRVC3O3OdmD0R-ZH3GNlU7ZhxFC5qEsRgBHGKcMD5pNDHqDvJxwWYWbuXEubhZQXex1d2Y_bJUOjKkjqzfwUHuSmRzbwZYhYFcdPa-t9xz3ELlKHjdYLWEk5aA2eFt8sLGSrQgVKgrDmdcff0-gTrjhVLR38R6C4tFdSjNEXTar9n9FBvTJ1XBVClM7JPidEOeExqJGnVCXQobfoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=q_T8NtdLz_fhT2xQ-AQDcSp8W7ibz4nJk4JV3H__gdwP5Ul-Riutesxd1ZixMTdwzxrtpYtu4m4MwnRxxD5nO8FW7GmaJKUbE7n5bNp0cWB1gI0JDOjrYqwGVTfTBnj56zGpZ3Hj3bPgRh89JOkblUdPDEuXKtfk1RAfcv34Dld7I016MQN-RdLqBiHUXC-mqk1YIzS_NgdqgvAGaWoh8jGvSaFX4qHJqJdvrbqzZRUltHuUOYQR8zxzR6Z1dh_Vl3DK3IwVnx-T5E0zVQawnmjtXBznCCiua33FhwgrHfNSFDH93lQRoUNcRolcEXk65JFKE7arnEnkQ3cj6lzDPyQmxMowEx5Z8-cF3f01NKNhdWf2qiFndsxO7cAVnl2ZfY3Sw_meA-4eQNZqg7j3yNXlT8Urxp1Jx3A3QuCh3izHW8TtsFHJmo-rcv3TOT4_dITVbGFo4whn3uerz9lr6E6XbjhsYVvTqyA-bE_8tp7NY_kTL-ULeY445gCgz79y9OnfEO_R3rss2s5AbhUrV1s5epUGnYW_I6NDtCGB4iq0JIlxVvCmLDGntCsznTGYP4S-lI2282S_3e4Xaj1QV2wkhTzTYpNoNBi9b-l8QDndVo0z-g705B8eAAjm8tt9a4z3Bj1fIx23g2-FTNLjkX1MtsvFJAquGOLpAqeXI-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=q_T8NtdLz_fhT2xQ-AQDcSp8W7ibz4nJk4JV3H__gdwP5Ul-Riutesxd1ZixMTdwzxrtpYtu4m4MwnRxxD5nO8FW7GmaJKUbE7n5bNp0cWB1gI0JDOjrYqwGVTfTBnj56zGpZ3Hj3bPgRh89JOkblUdPDEuXKtfk1RAfcv34Dld7I016MQN-RdLqBiHUXC-mqk1YIzS_NgdqgvAGaWoh8jGvSaFX4qHJqJdvrbqzZRUltHuUOYQR8zxzR6Z1dh_Vl3DK3IwVnx-T5E0zVQawnmjtXBznCCiua33FhwgrHfNSFDH93lQRoUNcRolcEXk65JFKE7arnEnkQ3cj6lzDPyQmxMowEx5Z8-cF3f01NKNhdWf2qiFndsxO7cAVnl2ZfY3Sw_meA-4eQNZqg7j3yNXlT8Urxp1Jx3A3QuCh3izHW8TtsFHJmo-rcv3TOT4_dITVbGFo4whn3uerz9lr6E6XbjhsYVvTqyA-bE_8tp7NY_kTL-ULeY445gCgz79y9OnfEO_R3rss2s5AbhUrV1s5epUGnYW_I6NDtCGB4iq0JIlxVvCmLDGntCsznTGYP4S-lI2282S_3e4Xaj1QV2wkhTzTYpNoNBi9b-l8QDndVo0z-g705B8eAAjm8tt9a4z3Bj1fIx23g2-FTNLjkX1MtsvFJAquGOLpAqeXI-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYdR809fk3z96w1m9pi9oAljKH4tEdWoLsG-eUGnrxoWCZKBeFYZzCiv5nTf4SKW-rKSB6hAXVZMHDynCvWWPqKrC16oCw77BvtvquWpQwgDLds-WoqGdWQ7Ru8u8onZ50r8xexNUBKTTDmQYBr-m55qu0Q9Epqz0WPEuYyezveOIQ1xPrdF5N_UO0s_EFG-BDABBWglmCe_7nuQPCsfles8jT027kV_XhNLgWhvKStRbHC6_abXQWZD4Ult-yA_H7V4ENp0LklBJ-qUXsryVC7N5R6WP6FiB-D1YUIcqphcTqnp9eBYnJ0JWYCjLG3KdEfQKmXsVDfOudP45Yq4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRzJLtAiQoFUje8Ll279l8slva1LCmb6gu0hNqCPudIxtC-XtPhnjagUpULZju0duj9lH3QXl3FiMTi124K87Dko10DZ5TU4mEXB-RG37sEO1HPDVZT00DvrI9LqJO64CS87D8Dhrzfy0r-eRLBmNkI3jsl83joDRToWgAbHXiX51Gnju33ZWc58Z0JyhzCr0HGr16l6HRqoOq1tZuTYjyCIOi_Qd9pS_ieKN4qFRgSN0pz1qMVc1yc6-LUu0rxhP9WcWHx1N9W9JWFvY9yxL8Uz_VYlw08q6bOfM4gAqOHK9o52ujfLoIzDPqrHBZwt2ifztWVQmou3FzlO9YyyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=Zccoim4v8muNQHg1XrDDQAjSnnI8glPToX6z6yjlWw8FEIKG772BOUOrQmz2LLa_p6e2tZSEfnPM-RVo7pZW3PscYxcDO-oYxUQ7y-rtwXXcZZQFmqQf7PsuerMsLNQKt62RMkrSLMX0swQduPFeFct8XbNiGeSiJiGVuqabA7StRb3EtBYil9c26qW0b94utKLGUuGf-WXRCJnyfSlCumwvS1_Q9LxtRKWytDYe9SmvIZOywpWiZycbk1U0vsJlf-h18eKGAxvlnzHMG8nTzGZl34jYFN-hfE5nvNgr5ZhBYdGss-zY8t9LT8hH3JbyDHxhBDKxo_WQRhWEkTBuAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=Zccoim4v8muNQHg1XrDDQAjSnnI8glPToX6z6yjlWw8FEIKG772BOUOrQmz2LLa_p6e2tZSEfnPM-RVo7pZW3PscYxcDO-oYxUQ7y-rtwXXcZZQFmqQf7PsuerMsLNQKt62RMkrSLMX0swQduPFeFct8XbNiGeSiJiGVuqabA7StRb3EtBYil9c26qW0b94utKLGUuGf-WXRCJnyfSlCumwvS1_Q9LxtRKWytDYe9SmvIZOywpWiZycbk1U0vsJlf-h18eKGAxvlnzHMG8nTzGZl34jYFN-hfE5nvNgr5ZhBYdGss-zY8t9LT8hH3JbyDHxhBDKxo_WQRhWEkTBuAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9aKjdUSzuDmYUvW-J2Cuk8dk_OjA1oSzQtztQ1gmP2LG-v7wPRFBPzeEmC4AWb1okO8ReT_g3KcTDuyccfqO6af3-ZhRzi4QNd2-kWEI36yAxge9VVIZmwBcq2E3DJl3Vwc-WYeJzV8BzZzbedcy4mIzOcyQwBam0CuzUVAOju4Ca8yirSBs5XJL8hESnem6n70l6SSkdpxGAbAxUcwmY69Fw3x3GdxJwhMVBFdMAGLSm2Ozhz6eKSgI511geCxIZYOO6Nrn6oVn-gdpUATX7K7OMUstxJcSI7rYX_OJX9eaSUMnQKji8GVEtLtRjrnaeBbhY9HxitIEvULs9lYJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW8b4gxQaumugDGXUv6uTbadg3yNFCjQ4ynwdOPQXUCiIUJimV_eAFmjJlr1HUIY6rx7Y2ogaTzrVKe5-MuOGhkh1AWYWvwSXes6kG_tYYnRdiOuy1PnZGbWp-CAogW5stARjvKthDdLc51fjWFHLPaTivR9J8-PvPcoAHe-wvcc98aLrNT8oUlSeB_RFkFRzcILM4baKthLydOW0ZDmjV2hn4UtHhBfbDYaBQXJ_Q-vTO4phi57dteVCJpkvjYrpg9V-EaHGMv4IgNt_jczTSP-B4B4_hAI0zxlkmHx7amThd-cIc6G_-YFkFo0ygNrWGUICAAtYcaFoyBjDMglIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BnfDJE-mgKCUPRpEhyeQE4iMt-7h2bCKk5S8ak34ECbEXHvLpq5AwE-pWO8kZ21qAE2j-jbLW2HfKSyRBOMCSV4sRrqf8gy0-DJSrwicsIvFCXYIgZpfpn81AZtRciQFZm7CsGP98kJUrLxl3IUx9LH35APQZtCmAWMZSuTnsfavJpBY7HZvbJhcHv8wzlvb9KEfW1bu7WxwHsqVkCq3lyAXmGwkNi9fsUF7ws32kxVMPZqd5Fc4HgtxR7MynopQfBKwshUAKBVng6Yg3bbx18L-Y0eDsIVGeiXBtvllesWcaEuIXwaYLPJzXRuXbbpDozsAX_PDxrFeiAyZrHANdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=BnfDJE-mgKCUPRpEhyeQE4iMt-7h2bCKk5S8ak34ECbEXHvLpq5AwE-pWO8kZ21qAE2j-jbLW2HfKSyRBOMCSV4sRrqf8gy0-DJSrwicsIvFCXYIgZpfpn81AZtRciQFZm7CsGP98kJUrLxl3IUx9LH35APQZtCmAWMZSuTnsfavJpBY7HZvbJhcHv8wzlvb9KEfW1bu7WxwHsqVkCq3lyAXmGwkNi9fsUF7ws32kxVMPZqd5Fc4HgtxR7MynopQfBKwshUAKBVng6Yg3bbx18L-Y0eDsIVGeiXBtvllesWcaEuIXwaYLPJzXRuXbbpDozsAX_PDxrFeiAyZrHANdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_qouEd29THtsjuaksYs99tKBFve6ZnP9hkUxJGAYOXknWhB41_zWNCQw2RpAa1VQzRqe5CTL4aQSFnnhAqQfQ4isYHR5QbZkcjEznxMcJQUV0-wMjMmr4Atg4sLBgOq2Ck04jmVfjSonIczRGs-jiaT0Sg8m_cpeMmqCEjHM7MWA33pMzz0QWI1oNBSveHaJA6U_N0CJ-rbUsk_Gcb6HPOAo2jt6uB0LF-VQD4l73Hq2KAi5CmXjW1Bn4I2ls2ednDzed4-Fb6EmsKZrRUnhP_xh5lRLJx5eFpd9A2qpKg4RKvUhP3XoxGtIY2tMVK3tP0HApjKcxtpVusfonD3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzNYRfAk6jdyrYowVGWhFXv3bdRv_qbfc9urUb89PTMKXVXaUBKOsvuMhCfKr8pq8LLk56R1S8ySUdNPX5O7FOUk6x0bBcvQBAZw1dqtnA1xkS7yl5yWwT3BT6LAuXuaemV0eICVnsZMt_RBykkngczHGypbbiqU3MZ0plu3JjdSkBH_gy-wiMJjU5UXv-flqXqZ8gZtaR7wDRhyo66hZ-34MqDJmIYFQBNiroNz8dDuieZYXJZMhGNrkh3DdwNAIoSKgO-mhKug3-PpaMN0YuffT0_WcD_NRzU5CA7mRx4ewzKdjwJG1ObBgwli4SKjtzIAcrBgQym2ur-R8h98Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=q6cpqfBcVBr0JLRNzbrW1aIDuwDtgdHetzlIG-7LL_Offn1VglXDfh-g8haCVTNO6_3Ic5Lr7SFpplFTQew3_Y-FOc1fWoKLFyezPOObYzvPlYhTBHQmwV7wSLTvLqrxx_OJEJCShHlZWC9nfMJ3Aq4voT_vfoga9ushnIOs8beec_5CTcMxIPzb88JcpfmGtGPu7NSOatVOANV7aumgSP6zNRC4_thJsAYK0tlOHNaUFwdJHUtVmZdtycHIushIkIOMmKjj8KBCZmeYkBkTszkBdovYaSSZPbk9J_vrD9vDKcDvbjEcdMeI31JIfPDpphIQR4eVwygyNLn-uVgpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=q6cpqfBcVBr0JLRNzbrW1aIDuwDtgdHetzlIG-7LL_Offn1VglXDfh-g8haCVTNO6_3Ic5Lr7SFpplFTQew3_Y-FOc1fWoKLFyezPOObYzvPlYhTBHQmwV7wSLTvLqrxx_OJEJCShHlZWC9nfMJ3Aq4voT_vfoga9ushnIOs8beec_5CTcMxIPzb88JcpfmGtGPu7NSOatVOANV7aumgSP6zNRC4_thJsAYK0tlOHNaUFwdJHUtVmZdtycHIushIkIOMmKjj8KBCZmeYkBkTszkBdovYaSSZPbk9J_vrD9vDKcDvbjEcdMeI31JIfPDpphIQR4eVwygyNLn-uVgpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=KbVzLZW5Z9sljoVVoCQBB70lv0HO4x50YoANw5_sMypAYwDIOBgOWycj3Jzxbl17qokOanNznSNsq3G9WHj4fMV7SkuXZXZRoyCCgk3HhIZ26hw27Sh3YnOeAmpnFTAMXsH_tVsMcA7DVmno1by2zpywlpBfKAwAHHXXtbHxoFaHB50slD33IUj8wppfhU6xGyqvwlXoWu-lJSum2BVp9WGV8xNU4dEEfIKe3UVXFtPLrKlRHLzA85U1_QBovw2psIuVHqlQoAqlDUoQ6T1Er__0HktJqm3fCRXLdHLI3RaVMOHr8N-sfKan9P_xmvfLvdYkhWpXLWlMcdDqff9r8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=KbVzLZW5Z9sljoVVoCQBB70lv0HO4x50YoANw5_sMypAYwDIOBgOWycj3Jzxbl17qokOanNznSNsq3G9WHj4fMV7SkuXZXZRoyCCgk3HhIZ26hw27Sh3YnOeAmpnFTAMXsH_tVsMcA7DVmno1by2zpywlpBfKAwAHHXXtbHxoFaHB50slD33IUj8wppfhU6xGyqvwlXoWu-lJSum2BVp9WGV8xNU4dEEfIKe3UVXFtPLrKlRHLzA85U1_QBovw2psIuVHqlQoAqlDUoQ6T1Er__0HktJqm3fCRXLdHLI3RaVMOHr8N-sfKan9P_xmvfLvdYkhWpXLWlMcdDqff9r8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNz2KLw7_EoKUYNfeqEPl0FrNAH1kvEz8TRlQQIXlTNrJw7cxPHuMe-GVDWevmdQ07O5eceF4zVldHWt2Nylo5EeqhpxquA-IvkOjFSUSH2nMduFUsU-lv1JvOZbeCKxqpYDs0t4hQnM-6rVTlfRzXBt4TG1hvZTuotvUy3SDw07osBq6PmKTPJ6Cr55dh86J7y5fdL6HCs1gcZKIxNHLq-tCdSfH7Ot-DFIaouGwJwm5AX8CRCrwKArIeAuw3-5DMIsmitUchJLptaOR0dy_6xYC-m30mWKfGrQ47QBDXWaXdkOnxehIjyHo5apM6_VRImLZtMtrLMGWysXpDBAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXg5N7LRK5KPej6dxi-e6TFePlVeqost9gRESCChvvUrJ3peu5-nDXUUwEGuby72ToqbPtng_Y7AKw9a2BL9eBiZjvQ2zeHrhSxxXY50sszu2GAGgYNr5H-9PRocLaxlqpCu-6aD70qV8gyH8H7pug3VPcSEc3itcN3qbngwf5mxp276N-Vxfmu8agkKnvLmaAsqeSq2a5yUDLXFV7At2LIx0pqaVVXvV8wjMW2EaFTgGq3qakyO_amqH2aSVQwGLCJA3OfpJ31DTnNPaJN_DIGGzsXf-VQVG0Sppz_YaKtSAx7pWIURtHj9TtY53SesyF-rZlTXGGOyKngFEeOafA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=FXTb0vXT5RWV1lIJ-C_bgIUdUbVEZRoYxPOq4SLccXxsRmIVvVYsWoG_ny9SeakWs6JJ9_gObL1wxJMIR4MAn9e-P-uohJpAzoWt4VOPIUUk8IC4_V68Rejou3HskyxwE-4sLnyg_c7OLO9UfjLAR5KlBb07KooARbdKC75k9kmGgjaYtxpqPtYH7ToA_R3ZLe-VtXbA8CWTeWZn-YaT4-M-6uqmb-gjl1y643_js_c5QY6-Ng-vwSV-1Vi1cjF4TVpgZB3g-Fdoj-FkJrFudwNg6YKo2hUmIe2lf_IIFXOkcn9SuFTRT3DvRGbqA87RSmrXDX7awlhqysW2x2amSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=FXTb0vXT5RWV1lIJ-C_bgIUdUbVEZRoYxPOq4SLccXxsRmIVvVYsWoG_ny9SeakWs6JJ9_gObL1wxJMIR4MAn9e-P-uohJpAzoWt4VOPIUUk8IC4_V68Rejou3HskyxwE-4sLnyg_c7OLO9UfjLAR5KlBb07KooARbdKC75k9kmGgjaYtxpqPtYH7ToA_R3ZLe-VtXbA8CWTeWZn-YaT4-M-6uqmb-gjl1y643_js_c5QY6-Ng-vwSV-1Vi1cjF4TVpgZB3g-Fdoj-FkJrFudwNg6YKo2hUmIe2lf_IIFXOkcn9SuFTRT3DvRGbqA87RSmrXDX7awlhqysW2x2amSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=QYbD2gJozoGqmU47e_mrWjVQ32wxorEMRzjdgmE-pzHPlPjkBjMOynkUt6vu_Lpb6yF1k7V6b4NM6DfNNs9GA5lAkgaHSlYJSPE5WCTkLCun4yqjqBfxamfWRb87JfGvl_gikdTemzUG6EJIeDmBwuuhnD9x0WD6aYN5IM88SAIxo4WJJpTxbGCZVsBX5GHJ2wgqblv6gEwH53H1mqZm_3t8LyQ3OMojgD3jCD-2SvGZ6RoemgxYm5yW2QflVemfYBBi4Ut9TXYi5VnLabt-YD1yTS_Ns8Oi6AxOEVH8x5XAv1vloXHUq0szDMjkCiaI85rCeW5ubfyUEBFbZDNhCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=QYbD2gJozoGqmU47e_mrWjVQ32wxorEMRzjdgmE-pzHPlPjkBjMOynkUt6vu_Lpb6yF1k7V6b4NM6DfNNs9GA5lAkgaHSlYJSPE5WCTkLCun4yqjqBfxamfWRb87JfGvl_gikdTemzUG6EJIeDmBwuuhnD9x0WD6aYN5IM88SAIxo4WJJpTxbGCZVsBX5GHJ2wgqblv6gEwH53H1mqZm_3t8LyQ3OMojgD3jCD-2SvGZ6RoemgxYm5yW2QflVemfYBBi4Ut9TXYi5VnLabt-YD1yTS_Ns8Oi6AxOEVH8x5XAv1vloXHUq0szDMjkCiaI85rCeW5ubfyUEBFbZDNhCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3xaHI6SVk_UAP3GpYSInyfcf0CrDEEq9wAEZzBERwjtWgy2LEG0zDUTqHrsYNArUvkSwSdGMcMf0Cuw64rRSO3EWVPezdCV1nKzIW1Yocic4cAXy7Fq3Zdev007HccArJj8-ODDRCeQuJDXVNF5TOioZEkVFZKBOlo91BlZBH4NBP-BFbuYjkfunINP4_EnZb5GCJfJOM0dqQpwDOwUe15MA2s2u0ygXWtQ9OnoS_GTTZKQv_qwBfen1sYoozVgADowcynDKuVJTt3kh7Garc7Fm9po9I-blvxs0rih4aN19652glGeuJ9J3BqGUxzElDZbo7ARho8MuFW6hsgf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWqy8pHgFyBp8jVnQv0xhOmxVoocsE80kfgfn0_EyDH4Y08-_Ub4l2rY_lxod-2noc98PThVfjaZFgowVB-tOPKH2aNbYu76uwpcJBbfQKqpL0pQhapW5hkTQ66_BVCSudzDM-BeDbTmJybKuKyFwHBtz2QcRAC6k3RRmbwTfE9DIjxCU92jCRv5XHlrtd0GMSDAkP0Zae3UN_79l_S9Zx-S23fzWIQ09DFVl_0GU8dlDnEiNMwB_2XKd9DxJrtZjK3AvvQda2vzDKEyzVMytzvJ29hbv5yRPNuoGA9G_-fwauudH6nanCkqpPecJFBsqZcPq1oDOA-Uo6omAz4eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSkgpN-QW6xciS8atof4JbO3gNgP071lDedndVqnsaPtFLCcG12v_TLKj-0LowI7RSYxHo50OxRJzn3isF752GL7EdNX6Do02tP8wLOO58d5557Dp2-n7lzitCqSCeZTaznZG1uF1fXrQZIddnDFwBTxM-pbdOVWJSOxDmDH_3nChTEqzYgRIuYUct24UYHN0LMr3A-LrYE_Aq-FEmpfh-HUkNW_cZct6VYTtsoVpyzzwDuj0SAofRs7SoKCd3SWmP7QarKkCSU5K_Xs4k6eVZNWxDl2ydb8nW50fpX2RtyxkHyysqhmxX9clOuFkSNeZsgTF9na_rlVaoSg6qEHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsMN0AGHsxUEKQBVfC5vcs17D-3uUx2Fsv_qT6dzOG1U6iMLmRt3Q7QFAuck1IDP7Jp8LgNTaEp7J_ttkPnSl9MbvpRwYccqjvA6WkdqFtmjVpXSqiI12Ytcnp72G1CSKSbbJTxiAhdGlaKA_K752hDMPrGubd3Xcb7Qd5gynfJKkVfjiQ9dsCvDC5cd_b1o3lWyzcrK0aYz0dfGIBdMf9JZn_eztXR5NwFRZksAhRRuUlEdD0lDAsrd4WqZ5Mo8n7eHJzR3I7D_Qz8Smo3vTXLlS7Z08CMmkYKyvcgBepasZXNiiseMU3YztO9DkfCro6TFM71Ny8FI2bCpZD2FcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrucICQM4odfTV8bY000j4T1gtbZvRPmhZg8L11qYnf-EakNa563u5dPgs2cvSej9C28oPT71ZkZ2Y16m9oHYU9JHnXjrcom8Jh2HHFAUUyke3_jyP3GgBO4XDsIg34dC_as-fTChmM8sv10DS9tSGzTCHMgDcsE3_VCN3UgWA40TAQm9GXZr0OTYRF_hN0I3ksZXFmEP6BReDC_aNsMF4-s-E8bR8Ey3rmD1-zTbJ4dtzBUXVgftdpcv3cLO-MTqIDJBQTu66hKTJHEt3InJRPBHxiDDxdsvvQUZ5jTSjWKz7Om5HO_cVFViZ9TvFlPV4Ri2cJX2TJEXqgbKekPCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=JSwtleNjoAR4ybXqhMFqAGYpqJprCPMCqs4uvMIM8C9n3fYOHDdkdTMJSJHdIZ2jQNB36xBshqsqsBAOliqcfwRn0JuWLdsc5RGK1KpBXJH-uou6oqSZ4SsNGyyLecEqEbwqNJp1zT9ATI44cM2HdQAl_EMfge1MfiM2zfd3V-PZOKZNV4_eO2MFY-gow8IjFUSFSTPrHeqXkp_lpQ6HkX5Qsl63kJZX8riFVOC2XqCCnbAsgPIcfeRarfp81bJSbhSeCyw4m7kmAxdZTNUujKbtCZDFpA0EwdON3VloVgrgcr7o8vj6rhXD9BLNOclQbUdjTGH-JE4h-rY9VNeeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=JSwtleNjoAR4ybXqhMFqAGYpqJprCPMCqs4uvMIM8C9n3fYOHDdkdTMJSJHdIZ2jQNB36xBshqsqsBAOliqcfwRn0JuWLdsc5RGK1KpBXJH-uou6oqSZ4SsNGyyLecEqEbwqNJp1zT9ATI44cM2HdQAl_EMfge1MfiM2zfd3V-PZOKZNV4_eO2MFY-gow8IjFUSFSTPrHeqXkp_lpQ6HkX5Qsl63kJZX8riFVOC2XqCCnbAsgPIcfeRarfp81bJSbhSeCyw4m7kmAxdZTNUujKbtCZDFpA0EwdON3VloVgrgcr7o8vj6rhXD9BLNOclQbUdjTGH-JE4h-rY9VNeeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCF_idN5HTcGBLf13RMThSNYjglXHYyEKuXsGyKopK88-sXe59UI6WPhnrbS6Ll_vFTrRzWsJ42H5WuhyPBwcmcYQZA9AJqiMdfbSBOWTnUXcl-Sjz3lcxRMxutNBbR0MPc0YuM1iTnTPhZ99K55OiIP61P_xTQK3s7NhptiYLItoHxXVb5RGCjRCAa7DbVQcrSXLk8GWTa4f2uUPuBzO9L2157WNkgqAR8F4v_Zo-GJ9ePMQiZ1fNaoHW45WO9ApMi_XIAEOIj4llI0UKJUnL8G_M3O-lsgd1i35fe0vP-SuB11gt49pWQZW1uw_AvxIucNXwkOVL2QWkLv8FgXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=ITKnhfxAeyCq1y7h2_ah3kXJkOzDxqyHKDYjsfdZ5Qm-P2TMfBcQcCTpGMXrWeHROACgoQtRx7X26bwn1Vt5MyMyfufdaj5MOpTFCBFtcgG8gl1Yol-l7q4idmVP898ovuRju27hJexuEKXUy6gzuXJ2soXHkGnEPREakz31R8AR_zT_oXCBCGhsQ_3umWpW9z7m4MbjYz72dmAeQ3Qf3xkS2-Nn6NRpYLa2MyhNnnHVFHUN0wr6YQe3WW_i-d3i_xck83wMHY5zEgel4EroWYnkRR-FTJKuboCYC3G_n7PG-U1JF2UZ97f5glTEwzG-HUkW9ONSwaMlRdaFmwVtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=ITKnhfxAeyCq1y7h2_ah3kXJkOzDxqyHKDYjsfdZ5Qm-P2TMfBcQcCTpGMXrWeHROACgoQtRx7X26bwn1Vt5MyMyfufdaj5MOpTFCBFtcgG8gl1Yol-l7q4idmVP898ovuRju27hJexuEKXUy6gzuXJ2soXHkGnEPREakz31R8AR_zT_oXCBCGhsQ_3umWpW9z7m4MbjYz72dmAeQ3Qf3xkS2-Nn6NRpYLa2MyhNnnHVFHUN0wr6YQe3WW_i-d3i_xck83wMHY5zEgel4EroWYnkRR-FTJKuboCYC3G_n7PG-U1JF2UZ97f5glTEwzG-HUkW9ONSwaMlRdaFmwVtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5bmmy6FxuiizbyZ-a1ySshz-dlb3W9Ep5xbRXI6JNC9m65kMTH-PV0LSg0wlRK2QgoR2ulv1-RWdizr8u3qy_v0KrDDOVydL_evriwxm_-Yl8lijl9fsFpGNrNKPeusc386r8jsqOfQAYHPxen8tRpXuYUyIUJS5nJ-kTgj0WXxZfviEdS4l2RkqLvG3GT-6D48cigt_VrQ8uemv_y2ct0O2rc6gim4O-4kbylqBDLfrytJ4gcM25zakpKAoW217vFJjlM8ISClzN-DIR8B-rRRqe1GliqgcHyJk6ZoV2leHOPZff3R-qJyIsARFXnEHI4wNDr7SvP-_7fPJ54Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=Q_yWs-225iF_OqPYDtaJ7dT7eaECFWD2nMDG1Q1azPT0CZ47sqTst3-q2l2ZvOepnejwHxACS00MHBqkSWb45pMtnrDCgQ9vRLK1Vn9bPzkGH4NUyQnBCGQ2tWw3Be7n1uAszBCsiGzuYnOJTA1Rdpe_kZfcBuAD0jwA0gLEzbCtq0xgDRNzLcu1fbVjNgqAP6Rc5I2xGBsX86nW6EJTQif8QcQVhQAB6me27_eVG16SUtUdz297bagcYaVAjfE4tAr-72nb7-4M5IqvFaQ_nzklJ-ZMKRoCgt_XiYUD-Q5sfn1Tt43iIdgtbj0yow9DIuuEHeBTFvOjn3ho_klQZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=Q_yWs-225iF_OqPYDtaJ7dT7eaECFWD2nMDG1Q1azPT0CZ47sqTst3-q2l2ZvOepnejwHxACS00MHBqkSWb45pMtnrDCgQ9vRLK1Vn9bPzkGH4NUyQnBCGQ2tWw3Be7n1uAszBCsiGzuYnOJTA1Rdpe_kZfcBuAD0jwA0gLEzbCtq0xgDRNzLcu1fbVjNgqAP6Rc5I2xGBsX86nW6EJTQif8QcQVhQAB6me27_eVG16SUtUdz297bagcYaVAjfE4tAr-72nb7-4M5IqvFaQ_nzklJ-ZMKRoCgt_XiYUD-Q5sfn1Tt43iIdgtbj0yow9DIuuEHeBTFvOjn3ho_klQZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYhjDJyF7OGDbooSunU-K5I-2TyYuFUT7Zh79ZTxbSdchhLZDvYtWBOmFSfIk5HIOvgtaJCH2zaejlUSJjEHuDnla5-ho9l3u_H9oso_zQDBZX738znjN8xVE1dkZYgJUBoXEe0D7JyGhSm5voOL8l9wSW2v30edZjzg7e2exbgA6pRXHW1hPw91Hp42eEBqyJ4JJRfjgwhc3BlgAV-DmkpPy-LX6udapoK1AoQXSnEb5k4POWcyfK7QjwJqq9yE7bFE31hk2Wlrt9-0RkyBRKwC8b_ueR8o4SHwFpfL3krI4aHXHrdfkYOHyCVenblIdYPMUB0AUPuwKWjhseM-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWHpZIACQCPHPgewh_N8dm6RCqINLrX2entFWfWdAmvI87uPlVQewz2367WlsWxp85eED2m90byvEGDIgm8wd_oo5HGpmY8EGK1wbKBxdRkWbGJdoqjU53Bfc5OJgDd4xg06CleLWw_LmnAulu6SQR7znNrcMhhRFZQbj2qN_2Hk527H4rx5l4o0n09O2d9komqJnST80lwtIqVcyiaXyrqqH7NhENsyKiSD8eTc7ZOIVQM1Fn9M-_5SutBCASQapCwiKdHmaxeLQLVtsbIoKWXOBuzUX2x4k3DSLZNoj8lCiZWIdJ-HzEMFik_8raUVEPAm8Xp-ohVGjI7Sr06hIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsWVmHSo6V7w7opMc16QvC3NrTO-Z0dab2zoxi7YL5n55uz5X8BLhL5d6Y91SOoImgF-8gnYEKEYcRjxnX_koJCV5Mn7g_f_JtD9EKeaQRQF8oTB0-jYQ_qxuesp7IIMtW2nwu1Zay-iWoOyXpl0Xw4uEVieD_N6sgsL-7B8Ak0mR2vJqmsqtmwgbTcf5IN7gCILhLMFSLesSXpv7ALiZZ0jnBiBhpE8O7X_FWj1XvpWK1sf1Lhg-uqo_l633E1kHDpxy8J9imRUY0DQyazjDVVH1h1A2Hg8bbGaA1FJ7zrPmKgld3cPMje5W88p8VVHzGnUO8NS-XCn-BEvmhLK1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5o5u3bu7xgCqS_rShRu2j0UkdKgg2mbwk0RHVnompXM6rfAqsURZTrR9uspPvS6h7uZnHUR0i64Gtrp1RoSXtTxddsPUxfii0PtS3kEmXmYNgb1i2N_ruxKBzMTya-55uXUIBI5vDPMlX8SiVgWE-m6wtxJT1I_wgWue_f2BIi3sm8NCn_fAIk9eqUhMxElRWKHrU1OkaNsY5ojOs7l3H7JXred9oZnCQ_fiPB8FS5Wxg7ITY0OxZbmCDy55rqpJ2ZtavVyxNu9OLPcD0bz9NlCjSPna7rAdOcBXeLTu82G2iEf2Wv3gzk3h7Ad1VO3dg-tLBVJhNvbaE_OvkPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGvbsD81FTfnzkwOh60KPX57Bb8732SOlYQDmpPQ-eFPhoTUAGZiUGdhB-mPvSg2P-S78vwqZN_bkIeQoFpgrqJGNapUzEfP5-oD-DL_VixroMRykVWNHJpP9FrIa4eqkCqWBcxM36tuKKgjVZ7AwkYJkYekXkpvnqjcCQ_38Gub0pay-2G6VgacCCItNs-xZCVnvQpbaBRB1J8p_3342uQYvqH_nAuKNZba2YLPcUHsUx7oZJON0_vzoiXXn-_oHNpBn7oUSvIhAPhaxdCTFnTpWyMLfmk8S-sM6tgMHkOcSVYV5bvsHvVZSPp7ovuOAp7OLpT5qmw7CAS360HfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV4lv1AsBcT4PER4TinTTylvr-208Bs2JGfC_z12QIwWR6gYahdGJ9HjRSjilQBb5Tm_oVwDnmkWUSUG3SW0Hz0z_XUpOXbxRSUDMaFzuKlD3nk6UO9ev95zv55aSTgYVyYvYdRh2EiHKE6bCJjNeuXG4AusRohDsH-mlIII7LCcOqI8FE2_6tZw3eSW1EODdlG8AKutt7Fw_JkXBSMCUyPk2_xtYHtI3nzJOTb-8VGBaMPXI-21poka2MY2m0F70vA1KAZj5FV6ogSC2v81_hBAIV6aRXuN7xB83cFJ6lzNNDtTXDAmiSEh7drbrkP62SnlVmubiq6YV5_k7sgqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl8J38dugEVO5TcCvBdnpK_21TXV4Urv01BZzXfcvcFLvF6S1CAoZVVAOOmpeG6iM2EFyAP33n4iFCrEAZgM8F0IBeu2sLnogJy8prErAb6eFiLzaB_ZB4BnvPoV0Nh0xnreeYXqyRKTBgABA5G8EKl1IGwiiIgZ_ctXBGzhJrb9h8S50CGPO6PBPl7BqEW8hnLXtoPopDElAPMCd26Rk6Gn0JEPVKKChvzm5otqX2WpSQ4Yxw-9fKJYkiAO1vQOObBkRYotZ2-6Q9873PxnMrqCiB2dAezXI34vnVdIlq-JqhwONwpmTZh0sRiv31A2AAYoFNPfGY6PPis7AWPUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unBUFiEqpQLHpJ1yS9bdkeO4Quk47dYvKS0n4GXMDPub62mtwrgGqi7JMKQmFonccZaSI8BEHIwW4-ILRWmLR9Xxv64kKBEPfDMnn2DCYKq7jRMFnGfQq6CFa77wUtuMS5lBCtVecVMAjI5RKyxmBGfPgRTfTCxIas009Obg6MxIGrnaxBDW-PC5RiObPnvsj65AoX9iZvVmoO1dZbjnE3dCyvmAk8K7Nre9AcOVjpWiJrsAXFNtfXMhT2a1KKWivhZuyq06Ejeehng9HQxGnv-0kVyRRwgByLWaXeNMF6e9aX-X_yO1FQBB2BO72z8WVRrbvImnhUqzzaebGamWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=sS4Xtah7k8NHWZx_aESGDdg9doGRhZptj7dco-CsY5zOypOg7Ao6SCBTQDMMIUbhthsdjJdEqOYT851dmImd_hIVAJ7DmOdyWV5ozhmuJxQHgXzhDtVHORPiqg0cXf4xRjxlTI2_7RAHIk4gFOkL4U1z-umj0JO8Vr4EMXD2qhAubX12Ie0owW2yKyH0zUeCgv9ymAQPTPpoRqmRO61S_E032UTpSBzYVg6tbxJO4d8k77w1MJSHHCVwKiYFJYceN__AKBNSKJOb_3KBKxMjKDIE9YF0yaLRL_B2WgElgAf61x_uNLLpi1uNsjAGZ_hRd9hbwnWLnfoJkq0qtSegFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=sS4Xtah7k8NHWZx_aESGDdg9doGRhZptj7dco-CsY5zOypOg7Ao6SCBTQDMMIUbhthsdjJdEqOYT851dmImd_hIVAJ7DmOdyWV5ozhmuJxQHgXzhDtVHORPiqg0cXf4xRjxlTI2_7RAHIk4gFOkL4U1z-umj0JO8Vr4EMXD2qhAubX12Ie0owW2yKyH0zUeCgv9ymAQPTPpoRqmRO61S_E032UTpSBzYVg6tbxJO4d8k77w1MJSHHCVwKiYFJYceN__AKBNSKJOb_3KBKxMjKDIE9YF0yaLRL_B2WgElgAf61x_uNLLpi1uNsjAGZ_hRd9hbwnWLnfoJkq0qtSegFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=ibYL66Qsxim9AbMl07Cved1jbDv7HBf-awDSPqvUoRpB_iWRxKTlIGKHhGTcrQqshjWtbxUe_ekgv9Mq-285PK0XGTs278A_NUZLSADi8vjrT9dqUENosruveOhIRNTEAevgqWiltOBTdQsxGZZQfFW7O-ntd4998gzZkcln1D7b01AfhlaAMYYMHXeuTDnRh16gNMl_9Sc-IdIxt0SeQUeTUQFf4BloZRxs3Zgy1XHubbVc_9q_z8GabkCqRCa9eSNos9lYE-GkBNesAkMpyrWMdbw3fSuNyMDzaI7JzUNW07o2eKF7leIw0JcHsUzzo3-PoWMop0D8a9uDFCKlaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=ibYL66Qsxim9AbMl07Cved1jbDv7HBf-awDSPqvUoRpB_iWRxKTlIGKHhGTcrQqshjWtbxUe_ekgv9Mq-285PK0XGTs278A_NUZLSADi8vjrT9dqUENosruveOhIRNTEAevgqWiltOBTdQsxGZZQfFW7O-ntd4998gzZkcln1D7b01AfhlaAMYYMHXeuTDnRh16gNMl_9Sc-IdIxt0SeQUeTUQFf4BloZRxs3Zgy1XHubbVc_9q_z8GabkCqRCa9eSNos9lYE-GkBNesAkMpyrWMdbw3fSuNyMDzaI7JzUNW07o2eKF7leIw0JcHsUzzo3-PoWMop0D8a9uDFCKlaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz9StI-6yJeBj_tk2XGIa9pqp6IeAUmvphf5vCN0YrhxcMJjr9zRDf4KjRPcUYoGw33_Y95iZ3RqQqSuMt3lWUIFKG9cud7YHA00jN0g94KHTQSA7yDzGvsW1-2YErbFd9dvItvHKjf9t3u--9UCXo7xGzqvpn7e7zY0hhrbN4kNwr2vFb-k6r4JmgZt9fKegHJt_CmBql6F1u-RI5ScXoXOddXNXT2rUUsmuGYhh3Jz9cyBtE2Q8hv5QQPTEjCAMUWBF_-Cp5W6P8vlZZZf-PCKv_Ms5cD21AbfvT32qe0ePLy9kqbErpwZ6o9ita84Z0OZujydykCEE3ZhkM7Qpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=kjRozBatOub-ky0wUd1d96BIEqHMUIcTIttPbC9LfLYW59c0YxQrpeuEQ_33u7MUMMUXyY4ENIcPmiuZaCw87OxGtx8nlKVezkUzKQpvsCFrSKn3R1lVO5eP4Loe2EQioTELAgfndJhOadadfxepggp8Xa_Tn1yds-5ER_IJyM-rsdrTdzc-6mdpn2-9r1A9JFufC4VKk0xqTb2f0yYZivFpj_KJoKU_tgJNMv8IxiI3iuPTp-zVF_kBuEeQiuybN-G3o8BPyECsadFvJ8JfHPYXRmiDavOAHwDxQAjXMcxbYYUYmoIqDIEWIfCDf0P82ebdypSNV0vV2N47EkuU_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=kjRozBatOub-ky0wUd1d96BIEqHMUIcTIttPbC9LfLYW59c0YxQrpeuEQ_33u7MUMMUXyY4ENIcPmiuZaCw87OxGtx8nlKVezkUzKQpvsCFrSKn3R1lVO5eP4Loe2EQioTELAgfndJhOadadfxepggp8Xa_Tn1yds-5ER_IJyM-rsdrTdzc-6mdpn2-9r1A9JFufC4VKk0xqTb2f0yYZivFpj_KJoKU_tgJNMv8IxiI3iuPTp-zVF_kBuEeQiuybN-G3o8BPyECsadFvJ8JfHPYXRmiDavOAHwDxQAjXMcxbYYUYmoIqDIEWIfCDf0P82ebdypSNV0vV2N47EkuU_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njrfKySHWau6ENrMWcTHHjV-6VNv3A76APSIuPlx_cv7zqmPhljQFvkN3mPSJGZzIwAW7_fidepMMk3j7jL0vDf1FFYU-Mzo5fGgTsx4TKEuNpb-_g2YpvTOtyw7SrhJ5e1R8WMYTMIDMXLtGuZLztDIcA1gmWey34rJ3XW30BM9DWvRcXWBK6cFWAt9Nd7pfgNMpQa-3GSA5Rs_tFYWm2ZhmU4C7q0Y_0bef8IzKIR8DCSc_m6O0YzmmzzEMDKPVLNYdc8V1cUXBk-tG2Y3zlu3z-AEbsThxfUq6TMPjucYSW6oaRStIlLPNH1s0nv2qwOs7zAH8deb14cn7R8v3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM7Dx1n6EPq9-rkJMtn7VzErAZSqTDDAmu_2kFdDMizMG-IvreEVIMl8wC5tE3xxdW-gDY1g0NHssAxmKCzCpjlhXU5T7Cf9m29pjyvSU9ViahKMFkuL2jVkGNh_507e1R57uoYQLW0lRodaseMb9syN64XyY_HE-CaXHo7iV3o44-cvcB17YYLioP590d6q0J4WzUEXgEA_TxBAOH_Bq0gXb-dA403bvB5qxzQB49yHKleQsmNr7ePdPl7ZC1PSU5knpZhzyR34_96jlJleXSD7pqUWlwW9GWz6i_QL0Rewh7TtiVwFHnSrODsVHqiFiOa8U3KgEyCsyPnryU2cUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=SYS2vG1VEk7_VP5y5QvWVjRWtlmyEKXbK0RYVqxnaZzVSMqvxXMtMid7R27BtDG7vL2wPkaCKoyqv3RKvJ9GDkS5l2UEv6U_MYSbt1rQog4BgQZEGIgJFkapimi580RGTTZh4bZWnqSZBAgVUcVBJh3lBJV4Bpncc2BlsaX-CDLymr8CvRLneaYEo82IR91_4pKZBZSfviPoQO_oPsRVYszYbelVVHnHK8nJ2tVbfDVPBrctkG6zgt5pagHILFiGEXzLPBCMRKSufVOxQ7fwNYXmoENetvPQ3R1p_foBd1sRu7wEfNoZu1EoeSFWGzaN65ccEIzNioG_x6uUAEqAzmSxYpNjm_H6gbx9EWmcjENFGzGl7C35rONaRE3VXPhGY5CldNEyq8-uZoPiDa9i38EGlmMoKpHmVw-do3R3VfMmpqjs3hPK8djB37yRnO6YGJ7nXDFGUul3BQC96fVYFgtQLPT7DXeL00YSwGsP6bMZUsNNXLXNatXqegK9eAie4B7cR1MdP_j6DB2O0XpbirK9tbZSXGNIj4PeQyIwFrJfxJrpT8mCja2XFOCPamgn2fr-eVTcldnB83H8bvvani19vFg8DIaVKFFVxwtQQe7KPxZFgOyYY5FEOHRtjBJLUND-WS_6XsxEUoNHyNwLiVuvYABAhbSOH0UiMvUOPfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=SYS2vG1VEk7_VP5y5QvWVjRWtlmyEKXbK0RYVqxnaZzVSMqvxXMtMid7R27BtDG7vL2wPkaCKoyqv3RKvJ9GDkS5l2UEv6U_MYSbt1rQog4BgQZEGIgJFkapimi580RGTTZh4bZWnqSZBAgVUcVBJh3lBJV4Bpncc2BlsaX-CDLymr8CvRLneaYEo82IR91_4pKZBZSfviPoQO_oPsRVYszYbelVVHnHK8nJ2tVbfDVPBrctkG6zgt5pagHILFiGEXzLPBCMRKSufVOxQ7fwNYXmoENetvPQ3R1p_foBd1sRu7wEfNoZu1EoeSFWGzaN65ccEIzNioG_x6uUAEqAzmSxYpNjm_H6gbx9EWmcjENFGzGl7C35rONaRE3VXPhGY5CldNEyq8-uZoPiDa9i38EGlmMoKpHmVw-do3R3VfMmpqjs3hPK8djB37yRnO6YGJ7nXDFGUul3BQC96fVYFgtQLPT7DXeL00YSwGsP6bMZUsNNXLXNatXqegK9eAie4B7cR1MdP_j6DB2O0XpbirK9tbZSXGNIj4PeQyIwFrJfxJrpT8mCja2XFOCPamgn2fr-eVTcldnB83H8bvvani19vFg8DIaVKFFVxwtQQe7KPxZFgOyYY5FEOHRtjBJLUND-WS_6XsxEUoNHyNwLiVuvYABAhbSOH0UiMvUOPfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cl_PAjj9DhbdhuksZ4OeNZB0LXTEu_0k6-2i8iUZZjKkXzAjCqSsCJwwiwChyItEMhLbSf67H5drecT0sCQyRyCavFli2V08D_Qqpo6o13VZOJjKZNA3K1hVklRmibguwpLITY8jCuGQL2oE-Mb3GEIIejx01GKijAtwhrAyc0R7Bafr_IUyOv7kmmazlR7_Tvb-tJ4cCc9Aq4bgbhbMnaHiZMnJqME-64EVLuJHkooFCowKgq0yhn92-I3SR4_d2dQJDDGfOyNIfGMevWrOf8HK5Xzh6oKb0JyQnlujb-xRS6Alg27CWnUHsbs68pIFG8UP_whrEU2H3iaYFrfNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDqEmHw5DFeq7Mp1AoD1NLKLb1hEtzkmChtbi1gtguqntJYYZk6zDgZp95OBBFLq99I66eIxPPOU3lyjJ-0T_DrTNs1zBL6Su9FPwIyi8fUHeOirwR7cMcuFkTnDNXkBpK9fG9x6grcfbqMUj0zDRwNC02K2ot34wfFUen6zQlqdGR556aFqpwtyc61q2c9aqc4AtG2DBZ1h5lG3znDpnO_Fu6a6yT2q_JKVCErdKkCpcpWBtMdjxk1c36jy1XV33tZnBC4yM4cnr4DH1RNcMeHpRIQjfv5X_KV7I4nVTnrWv0yrW4gxN9jes8bTIZa40rMVp7g9S-2XX6bvwdpQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkFyutO_1sEDJD9B2maPuEEquQXT1ic8_hg4pRXu9sXXLUBtL3j1082ED83ChytYRENebEtmty30KfRpSn4NMmDGMxV7OnmPRKvv3wZbECg-Uhlsz1_6V8xFDwKqvr2wueO5M2kIf7tYwLOe_5zjW9MTZLGYZn12IAn2yJotiEv6ns6gd6z2r_NWNjEDgTAj66EQL_5rMp2Kg4Wuz-mTRs1tWqbu6E3690I5G3JY9uSaJBLuoepceFTX9ZdI9kN80-qLnLCnGyLnwNohSltzkdef9z1dAyKRIu0uo6YBLqFBDauYb6PfcRk7gukNjUsZRnNP0dv-bA-249lDq1LFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdf1FJTUe2qQRPSxucFwaVB9ih_KF4LmBWGzr9zgyiWLRhCbvSqcjyYcYGq0ogNs56OIUhOFQdT38wc6vTqAOIQrgJxchhs9N6_36gETiPLUKvU_B-W5y4qWBWxR96nAcvMKxhWE14mgFYJoYyg54AcRXwzZNvjxZuE1NEb1oqaplNratb8msWRYLWUzfY97yc7jVPCBtgXG15lbS0eFkaBN5J1Wq2IzfSpb5hcb8aFVdJGUNpGY5DLAmIVHhY26Wr97ghre6EBR-mVJKTnCUp7xmIxvX_cZeYhp4V6P3WgEUkotXo67ekMRF4KmS8eJmxnV59zlX3nejyBYYRMpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLA2wv1g9T_XVoUM_14N2HK35-Y8sKVmZ1nZL1dQ-QGLQfTw9JVd0Gs0EZRWbpr0iBZ03tQBnlbf7V04S036ZCeMjb_AtbcqnnZmqKBwmZ34Goop1mNqCIw6EykWeBxT4ml_cF-n1O6cJli9QLQ05KAx3-ltHaqMvx0I9j7kvAqmPEqHSrD-QMyMYOzVjCdEf2jRFDop_fS7mbRGbqzCmElbYGtXlo-0riN37UfbGv_mpnAk4yJZHAj26QAkomKCRVCzsnW4l6GGSDHZoI6yP8jEuR76poHbJvtdKsU0YXYj1lGcIEGUVaC8syuh_r05rmG9pyIT2qtbFKEErQbHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=k18qSCmNR5b2qjZdPI4yGfYPO1Tvm8jNmAYAdOMYggQwamE-iyFiC8tJ5Kd25Saq9hAobHXL2dgDkhrJY_Z4B8B5OzEBhIX7PlhzF4R-9CJ4cqT5sXQ3bISGtX1m7gvogQ5w4G2YBnzriJ-PQ9Vf5QTFGOMFD5HGOnNa1vr26aIIiGfpozAQbWVvV5NfK88kcmWQvE90dyvBipHjqcdKnrWOrHqupgpfj5XO0oYROd5NPlDheKjZA5sb04iXFuc3M1YH0R0766gfgxOgoY08ufSbudAg9synfqgdxMa3dAjwBbWDjWKg_bY6n-Jz3P9rUOFUeRc589t_pIZNVdgM9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=k18qSCmNR5b2qjZdPI4yGfYPO1Tvm8jNmAYAdOMYggQwamE-iyFiC8tJ5Kd25Saq9hAobHXL2dgDkhrJY_Z4B8B5OzEBhIX7PlhzF4R-9CJ4cqT5sXQ3bISGtX1m7gvogQ5w4G2YBnzriJ-PQ9Vf5QTFGOMFD5HGOnNa1vr26aIIiGfpozAQbWVvV5NfK88kcmWQvE90dyvBipHjqcdKnrWOrHqupgpfj5XO0oYROd5NPlDheKjZA5sb04iXFuc3M1YH0R0766gfgxOgoY08ufSbudAg9synfqgdxMa3dAjwBbWDjWKg_bY6n-Jz3P9rUOFUeRc589t_pIZNVdgM9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMwVmgyCWt5KJmDoZVavdxjWw63WjQJFzGRNNZeLl1ME9ILAqTRDF9Aekq5-OzB9pN379Uprv7L4lqhI0vNoHOmfBof5C3xS1tUkAdoj_hHKRWBKdoQKuZtpz9KphyPPptDolb-WQ_ZVJiQj7gizkd-UxFjOFj3yOadh8SdfQLk91D3qvmoRWOquLao44g5eNtojJ-XLCwwiRzFohq6Lp8scAPdP2-GSPdKQj21jASUMLaflHPaJt1AwC2UfHxOrdtxnhvU41VizsjSgXgghhZ3nhz9BvW3DWdS_J_QM19x9DhJZxMyDIytxL1pe2omJMoZ98ENVtlkeEfPpkY7MsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=B71cGRKZG3ormolC4KtBuyzg93Ea4jI9LvMp0NpWhnAOwB9ZQVvUrIlQZwo0rjbTM7XlEJusMOTY9mIETWZJausNboFquEooQvpbF9BgGcjh_BBxEtzCUQyLX-BAocrRsF42HMW0W9uQZhhHz-AckGkDTjG7ZVCd14tMmm75Jp-ySyGnrjHSnuStfv8JVfoUQLJLft7QktVObJPaU-dNLiYfZyN_R5gUVGyRjW91qoLMi82ZD0sn8Jggvj07RFezg_wZbFG8S69W8kacZNGDQj9na3rN0T1QPvsMDDhM-8MNlkFpgw5QtlOsDrRO6U5NAmV0KjpXhg_P-uNQmBm--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=B71cGRKZG3ormolC4KtBuyzg93Ea4jI9LvMp0NpWhnAOwB9ZQVvUrIlQZwo0rjbTM7XlEJusMOTY9mIETWZJausNboFquEooQvpbF9BgGcjh_BBxEtzCUQyLX-BAocrRsF42HMW0W9uQZhhHz-AckGkDTjG7ZVCd14tMmm75Jp-ySyGnrjHSnuStfv8JVfoUQLJLft7QktVObJPaU-dNLiYfZyN_R5gUVGyRjW91qoLMi82ZD0sn8Jggvj07RFezg_wZbFG8S69W8kacZNGDQj9na3rN0T1QPvsMDDhM-8MNlkFpgw5QtlOsDrRO6U5NAmV0KjpXhg_P-uNQmBm--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB4bz5xtBnFuXEIfBuKgTVammTe_Zh2wc6TaJNFEB5Em-DfItVqT6hYIivxc24iDu8exl3U_wX4Nx-BLs0SR-R6MtHLjCX-5bD1YbqEFUWD4_z9wnZSuhDse6VU038ml3NypJ5fh_fm9TyFPe6HQ7Vu9FIlPM5GTyRjQilI_PIo4t3aegTDrWOBfw782QXnvMzR7jObnUnyVHUje5B2DXPd5mZS28R7Zdab0i3t0ggBg_N1hdrTJ95269KkrXns0W6UGEQGOAQ6WFzCWmHkeXQmFYgznkzR01v75yDkQLVWzb49hJj1awp6aPJTwPOGr60-d_oI9AozaXIGTmSyGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
