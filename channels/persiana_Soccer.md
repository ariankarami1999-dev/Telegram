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
<img src="https://cdn4.telesco.pe/file/iWqKpB7m6HaYvoUmd9Z4IhqLKmsoNTnvELS6hLArbZiaRZfT737DKmiBh2FaLlpXisDPkLBfSJQ_9iZLOgx1vF-bAOnD-UEDKU8lVe3jUugp3laC6qg3yepVJSG9iW-9M2d6wZLdGC6cLb4l7AymtOxMpQI4eYfGvV1UidbJm4JF0Fg-_E-FYr8Iqsl2CYx7_pgN49xRbgEKxBcVTTU9XnQe0HZE1uIplHQjKwW6-62Ou_SfRg6rwI-NdBW-V21AUzOYpEAHxWEJF6ccU6DpQKTG_7Zz3ylRVy_Q78QWMQHLMpcPju85ZqnZ2kkpGo3JLRHCA0KUk8iycD5GQKlfSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 176K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 02:45:20</div>
<hr>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViwDVVTofW-QyFaCQspQZe94UO8ZJhHbRINBLaFJxa-ppURfzzulmCi9QnyAT9G-20Y1Eo2eyTrCGrLlhL04qR6n4ogUxkrJip4KzQumUc0DSkzkhPoq_GWuPbF4aDUwi9E6SauL5Of-nqzjG9Us7u6F-d0nJ3xorfDF6h8DZDoOews08Mzjt2DKCvDxOhZqaysRcWr6B-Bk6c0_1844bwzTD9PHrB7Oky05tVvdu7r8zJC40mV_soPNvyLFgT2mIqz4sFk3Jr0qXG1HSZtv0hiAEm8PpZzjLQx573wQs1X_oempw0z-_F4EOSKRPbKD79FdtFhevdI4vq-hyoWgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmtSga1dH4MiOfYH42qP6bOwJDSyDmMa86OR6Zy_j2BotHKYMRiY-E4I29pIK02Q7tdPWcXR_m1NIo_VU6aGglpdpAWLCC0FVaglJX3gjZS_E6H9Zrin1N5g8i5S5pxOs0hjhNMRnmwF_nJLgMxrsCMh_qzxxY1M3cNqB7aiwsJwyayN1jt2vhKr288g7kxYvWWi_rE5xLnKvoQQiz8xorhPlhlrgRwyRDqCKy5M4VAGrGJUIc0FzkUc-S91DJSSkmysURlqKRgz3Dxb2mn1LPKS1a3Pti_swOadRawXrEeFOx2DAObFQYNFG3JT1dq1BG7R6Ua6DxNJGKtaam32Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzbPSeJk5AoTjO-jejYBh7-DEcbUVFX1ivFarE6sj9BkUvax31j0yuyF9guS0A24pQtyOYVE7cnE9DGCO29pCGW8VoyvtvMxRNa14zMBdrP_mJtgfBnNLYNDrz-Xjf3me_PoPVrlBNqPE0Nzw85cB6vCCjUIQdGsoTCdQHsvgSY2kGMmtKt5OkBn3RnPlegMcTAPkbKWodVwcRUg8I0s7-9swadZ3_ZJJLO-Oom-hNP-CFAqbb7gASaqe597L66U-9BcQCuAGUAYXf3PV8Wb_MzZ5EyY0IuKK5Mw5vnyzftXM7bj7wEB7kOhnpuKfV85sAcUeI37aSX9xWX7CTA3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6HEM-ixABX2xogG7uZC5VDgQXBpnSeHmgZ63N0DubowIqSfdebXYJa-VRSzMqpXG4BKWywVTkZBMQwREqywS7OPBFcZgVAEiDCUEh1cdIANPQZdS-_CG-kKDRAysJ-NAB-2KIe43oZW1e0k1LzzJEIHXetpLplei2gyidOd6zmmUEi-CJn0Lk2-itCCDD-vbjAxxg-q-r8R0QCHc9LzPmKvazU26cqJrNj8mTgREgztVA8XXIzMAXvTep_EyygXIT7PBqrJiPxpZVdOVlX9mgcmEfVX4bQPY7DEHlbH3RNDGLEjuzYsh3I888DL-Limoty-Uof6DUkaodYThAWzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0TjJvuq7U9fUDOCYOO4TmZtbXQe8QOKFfJpTXClRYqDdWwX9xwKNwYeDlAu0sv-gSstHfffqFxMX6scKBqLGIB05TC13uQtu1pO5SlBoPm-OwT0RnK2QOFkZ85b51aMPum3aONH6wn86I2FvI95-FfaK-KnKMt0pYG9QCRXhKPZUb4xJ5Vk7caSU4UBALHyHUbzIADjeWbQivsT12prfOj8VNnzHvsykggopLftbKwrJf0V0uXGindtEtaBFnfVk6yg5cZjVs5ZoV9FSpUOgRZ1C4UOLbbXkBsoSJfNDNT4zo_cfiR8_VT-LkRdl0R627Nqn9sN6ERJCSv9ZDPGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW5ZlVoU-oZc6ZZzt6s6FVFCR1qi6l_zRV4RX81Xm9t7ByZ-J8dbQMqlHyjAincTkodxWa-baZQB7KSsPs-XbUK8fwoApPrXlMNSMyvNGjBdONF-Ew9eOzHEYbM00T8jwMVdfC46j94zULsXcgl1PjZrp_nnCE7uqde7LRyGkwitSmZznoOmK-_0YhElh1xx6Xs50TvRHHnAgbWzkgBRwpvdtg1PfDSiCWIelzzS-oAfEMOmjbgPgQBNajpFABvYTwf7-zBczr1UTFKb5K7G0WR16kKlHrTs6Da6_5B4_JcQRLcE4S6JSYlFoB7MqJQxTCxWlfCpA_Q08N1oDbKm7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGfmJgX2ZKyFHTABL0BTAj1aeQ2S3SqgrGnJ3Iw7T1wOZ4BN7K7SQdaWrebYgKZ_fKj6Xvsi80CqBisAspnqSaPo-sin0RU1j80YvVvpZuFeNAzhOD-ezr-4KkiRJGB7i6524ox-OdEcvLgyvxL2aWpSS5-tBN21Bra3A_ey3xrMZQQfvYDZPEQTG4VQicIfvN7-LPRSC9YpnPmj4sUbeHmrnqn8k875QV8iAFRUSKw7RpITlgyID6He1I8ZfOQeun94fc5ShWe4rcBp7l0b9Ruxq33tWf6XyzQETClDODmUIvy51XuR3m3KdHUuaM9zzHp3fJsXJyVLisn2XLu7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsGxHBOv0EcIqPsxz-ikA_bNGdL-O3ZWfrNLlfve5I1uMDzJqBt4qskzuR2xgkNBH1kSfKew6gBgegyGr8paINYZ5J5pripq9GfXAt4Udn7UGqhIXhOOLSNIPLEJ6RlZPWiwEVPXgZztXnV3x6uButSck6_dDMYMMFgR2UizE0VN6Xdnz6Kvn7ivpUdEOIawG2qyzaOC5OzdWAk3zk46iBEeyDNLDqxxnOi7RtmPrONBNtr3bn01fh38DE0aKGguBaZOi1iqkHJ6Qtm6nW6HXTY3LvFZLLdQI5YOu4h6amMDtv8UHSX8dPICNtRWGO_9SzhSlnK--YO9MKquroG7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILd3YLSDm71dN_rWvCpOgXOViohS0V6D9uaB10cdt7SCe5GCaF6oID4fKEoq_Kgacey7H1ERxbutEDcIfrY8XaP1rShxggujHvqsDk_XMzaU2CrzFEBNuRlVkf5nohssT4brHll5sgAU7Jo2gmAgCfemgvOOyKxEUA9UiVLWk2BwLYDp-j44G9cuxFtYcOdecGGtB4qJbUTmLIPWDnYjI5xBuEq8oT_NKp4REf8L4hOcetpsfnP-o5J8rQPAsq_95FUnyulST-Au-kD9Y_w9KkBD92a4myOhz5RoMkI-P_6tAXCcCq8ohW8SfdseBsnCYrFhjAqUUtK3_-hLBRRXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM9jXUAB0jYc80_6R7VOZZMlSkGa1KSZXIXJSnDd5iNADzHWWnApP0v3sEUZuWgQmpc7B5aMtzM7WlcHMCFtsJw4rWFtA9qHWtf9eYTgcZ8khna0GEw8MLAUy3dmBBWGPJvOoTlJRMZAF-C45y_C_gDN9s5pOpbKto4KVv-AIr3V4D7yE_Xk6zF9Nylu8PJV7twKYJq9WjZSZe6K3CzavscwRcCy5D3m-4287nB0gZo5qo_Gt2HHAthlyJFJOZ2VI4vU4xUnMBtl0EJEKN06pP4wGVCI2l_KegpN-_f3p6S5Gy8RlYd-UCMPQtSrXLO0pFvReNnPORxvrLe4xmTH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCkZVDVRozApnxw76FtMANxMg0f8MOYPDF1vEyRwEYU-vPuy2lj2v3cPCA9jwIt-hiL-Bdr-z9XJZP0oCIRFP2xsXVgCx_I92ImdF_Wbl6LSP2hCAu0Xy8rA8BxsDbrCJCCX3VFJUyfPWu_fx9FBufctoCvnv5KdS90_hPkwzBPocVzInSboF25eqjUwEH3Hw8qNb2xWSNswsfQPmz5xHzMiu8XQ7DwG-cO1zK40iMroCmvx00rR_u4ioq8T-bmE7NmUQ4-QD0ATtS9BghKv6xbjp9LCb6jdHsQZBjdPkjnc311iV_TViWV79I5iAG2uzgpxe-5TaLpqmusHhBxHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJIbKkPASs9oiNRJintKZA8xAvnoCZPCq3ri25JvbXl0RJVIT_BeIXEstv7ikiyywYAL6Y9M8H6OVsuOqCeNcJcruLMmjM4Ihqa3c7LGtgpnxg1P40z4QAKOPBe9vV9iMm4lkBjcBqaitBrEOnF_rG2lYfwhgsm8ghEM842VlhifFeUCxxwoi_t1hHkR0mBh95DnwcFq0rVEOVqfYn1y5ivxOcmvAquD5YgVU6x5rBLd6PAR41qKgl-SQ9UggCmxUC1FBefElZK-AhjS2ivXtu-37sozwfiamdqVT1BbnYBA-83w1K1_2CXuVcLPkPFmUIHxb1aamA-XF3FEq2M0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-YEMn2UxOV9iLOlfFcQvJnXbYLVALq0Pv9eWoALvBhvSgHWtCOhF83TKjpLW9ZA9WQcn77GCvsT7XoFwDTSQZ8hhnVJvdXEZFEyyeO028v21DppLWqVT_Qn0dk83kh5_uERDUMPWmdTThykFd_HgLkPqn8mfkVxjPNh4ZaJx-dWRuNS0AbLyK9uQin8NnIlSfXsEy23C92i0Ew2gJKpIO8qRezs5LimskM2QX9qb5t3oRG0m1jbPUms83PpmKJdqSslk9aRtVuHxGsE-zaOm1WfqlF8e5_mL2OPS9VOP9lgnSjwHvEO5q1XGhTEEpkq33ZxPk1DeIZkGaR4-t9WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT1C5NRituRP1PkES2LugngbA58IhsAQYy0coNLkyLFgLoQ8GPvk29XMeKKDiyu41Ab_dB2NUZ9Zk3hzJwowEUznNH0JH6Q5aiEpag6RXrY4jNiylV5VrXN7WGAalwfUbUIA-sKYckJERbK_JQ4_DKCxrjdX3b7iGfz3s0cVNRKXFCT5bXAwn4a7-sqjEzCfI2nSokPwEVKqnH1pi7HLqaTahXOI0gtduzoBHfrq-aBqexEXNESE0dMMq2CXYhuIbQ5YYt-HBPDssWLEoNc_LbhoJXKJ3umzjSLE8cPeKX4dDjjECGJ-_B8m_SMC2HZH-ZyzBBhPIN0kaNy2O4Xrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg70vCUiqqDzJQQ1yxT9zpMovM9smRml_pcOz1EsUvcT45XLktlzURHRl-EpikuFYCIQjMak7ovsCZScdWkCQgtcoilHEJAkWPVWu9rj6QINeM_7Wrsb_B9vamqsYStrkmWb6jsz_QCBSsLvE7jhetNB4s-Ml3gUmAVYPGNGGqMd8W2EDcMhuFIbFNVRcb3jSung1M55uFCIhZ07YOhhiTyH_cx3sttDTnUb7eOkMFHGWPBFYoi7jBYwMG5Iv1FHgOlRKDm4kGtXwz2Hln-doSRuZORnYWiyp7BKS2Wg38HDlU7URxAyxjnJMWJEf9sq2npQZtl-XwAGplycp7nFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuD4C286E2w1VrJ3myv2n-5Dxw_fNBw3DXEgogaMaXS-7GU1iMjcDKJX1VWGOsiTGPsk02162Lzng1K4dfFMJVrG1hqzaBUL9VOqtAzA2yyyJ1IMRSKl95Ps2tY9hzytX2-QG1Gj8OdP06qSybLybwkW0qJjDW1OqDTR83_hXx1AUXrezO8ajVC0V0b1yU9uJzZthnpJ1Ko7lD1CbhPzBuOQpCja5ylZVYUYySeyXrLXXjsGjmiSQpg2F4KtNZ5WobyT3G56_imt5UGIw-a39zlC6FyOr5Bm4rCc_H2VicR9JtbBjzmDUNJAmKLTkndMJhEfJXS8EXMSPDFOjobeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22672">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxn1dzp3ZuXl9wBefXL4XTn6sr2QjmOI23G1lyGRdIHGedT-CiPaitblhSKmV_lW5uVXWDRS6Q-wMlaoIv_mO0_DKokCCgI2piezxVaTG4PX54zhUHcXSZGO8l1los1ZLTxSTHVoF540jRSnAJuKv1i7UmmrTEz3rE4MwPne0X6BrnKiIeAS6WQv6jXCeLVtimFyyZuJV5ZuXlWf7IuOERUwTFvp6pTZStTKqWeFFxvYdPRer_Uc3ckx01cMC-nKr932eXLhW2iSfBXY475z8M6ymgwSeGK7hyA9jr6rLOpZTnM-r78_7KFUk-aS7gAZ2Si5ajXfCUjcU3Uipfx5Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22672" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSaayPErbbxIX_SEGg_BuZmmokKpa7RiNhohHluQzjgsbquQ3dYwM1hllSQTBfNkQcSggPI4Sx8IB6vRstvKBZrF_TcCd-iYhM-t_vzbwXfpbtKh_D7zIjsZVcLYwy2LTaGlzlNmf67LNqqVkLqwYbBdpI4zG-pM5El6wozCNTJH4ztdbZu-K4bbEPtw01zf41Qxuy_UhVIfFawfPfHSTUK750E_bxys3E7eIGh-ZHntwwzDkNWWYi4mvlInpFDGAcAbZ-43niRx1x45YkV1rIBNoFrEOMSp5GGYF4hTXD1cT9gBGaBSAKnbXV5-Kvtb9DhuWnJVzSRi9F_XRPRT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oat-ZeSdjXWOIVhiiOUFQ-_oO79UU4QWqKdzG2fVk36AoFlcIcMwrhLB46Gqq8tS5vO3FWFR0pNjnLCxWc7UMurYcjoX4D9j_NziHZ9mHhzWOaGMF0ccSVc3bXuu4IuCsB86WDyQwYtd_YjreZAVxtNo4K9vtxEM12YO_J6asQvICtOsrD-rCcbchrDNilI0TZ8w3qFpgGCrpazkAFNZ7gp5asLmDQvzdmBNcSOsUQacMBpLTdKL6H65H-FqUeH-zGrZjh5bKLfSgLmc8lCrJ8HLnb3ydm2pnSQ4kltsSo3m0qlH0vB9VjMUH62VrpMRIjrLOzY9m4eATqKPiBn6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXQmvB8rRGTa70FiWUhARawdIOYdfQdD2TFBkeDtQrnCqGFClDxw7Nxw3aP-D1045efENBYVcj2nDHNWM-cOqQLX6Yu7bjulIHo637TGdQ0JDF7-Tk5OFkxLjEYFhThO0a9i5zIQyXXZK08yAjBEuG7iGJ0r_dLblep0WwezxDooA-YnGQ878L3GFPQhEBWjd0hklxrnE-QDJdoJN_GxmTfgrls7IZQyYmmXIDY2Dn4AweIqjzukIeZZZagn1j7li9ktovPVIuDBCr-GMgeHRoVsQJDh4wbW4WzUwTFCx-lhK6XkfywfgI31_6bI2OrUpx-fVT0I5FxS2AqFSF5Wqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbM46susScVz9xwfdHfStpPR1pP9MMbUWc7ExfqP1doE5auc6JsLtZxAH6PbO9Mg_SvR_jzL5R5n9jhSvYVYJjrAMGvc_rs3kAMd4bYLBJ7fGgknnQUiypf1WcZA8Ycuzx3O5KLQtfiSmD1Y5ccdmVO4F913vaJWlWk6XH3yEIDgEKXaqqhcG2JSq4XBwuPxWXEBizdpDF8A_RENuPb0XQ8HgmCjzLKWGBYGmnrcLstAQPsPRxyA3TxObaqct7Eyh346NROMP66zHrBeKH41rxJKo9_bU0_fBt1NTXFVMAeOJGmRCIBAmpSm7W-ceaLItWReOOyNqRhRvsHcOLz5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avG1S1TCyKQ1qwhwtMntvd8riVbZPOGh3D7gOXdN69hICvYevv0ShmGTHS8r3RgcHW64fl2IZmW9eiTVX9yrMpSOOPLmozBa6U6kAIvI6zuJSm8w6i6F6BRwNetacUOcULejX8s9_Xd3Mobb0MPaUusastScIMohEKCJ-BhXxAXGg9U4ms7l0KrdmRKH9irU1sV2A3ziprQWsmX0y_lW2lRTXonIwbwjuDXe9msmKbv5LMDgtvQMzCbGRUfrV-9yMUHzWNqlhxKqRCNNWKHLgehGVML_iXXe4k8FjzEG7AcTDjiH25arnFzaHTaQGuRQkqSkkljjXbC44GU7X-etMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smI72iBjZQMeiC22lJMgNtsJ4CLizjOuH5VFoU_DUJZERYlUFDJHHr5yC0fOhZkFOnaVJSTUp_jfTuBK8ts3PFgs3dfxt6xDcvCKAhgT9_juGZ5pBopomsl5YbwTcVk71ADMjHFHgvAwntww3XfxtE7GlJW1nQhG7M1ps2BFaFi8IixBqxHU3BIsWc4uXk-VXaip8-CTCxA0QIyR8r0Spaj1-htVeEgGI9WJsfTRtpkNZ92xgVouRBiBwr11k7Ef9OApqNJdCo9YrgD76Ush11HEkyEwiY_wlzFUYgZvjmOVngL88G2azsbZpwt19k714-RsDfGmAxRQ0VOohafI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzd1ZgESS86X9P6xtO9lUHWZyGSjhWM4Nz9esB1bAZ3lXLotrvJOhAQbBJVTaT9A2FGa2E2zebwhdscY6kFMLvvkA9HvXPglpI4fHBXJOoTOy_YtS-XU2UTVS8W_2wJwT7jk-25eNtEq0xLAt_MsgubuMMEgqIIAGgtrPU0gqa88WDIPViNKnjQsAFBUhPcyBWc5ioEs4P8k-hd0NNpEcoaFWzWzxWUNgtk2qS9V2B474inpADyis-V_x6DwBKxoph-m1dbi89BH61v3NwNGPfLTz4-hAUjLVzR6gClkLU0x-Iis8zdukgxMmDqf-SeY_wn7yYb_K9tpPVmvlvrRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ-HBQH4QB2Ts9dMQplU7E3JEORB0ROxMfXMgpRch0TZ1QVRF98v9ur6kbwyJROc5CVajyPsiDA7vg-k7fDwRXg0cOe23oinkUawGXGFOSfklASc8tGRTwkatxKBFPAHSGXakvk2VDl5Ra-gtJ5Xlne3cjkpt2mYm60sZAwwhTzC7WIZ-u-eWkbrdAmykgq4uU2cgmzmJhVnzLLUhns70nZbByGOYvsydHnitDeVA2X31PmZV30umI-rvRD5ivgrUZu26CDo-9eN0D_fMEvj3p83NdPc3QKujgMrhRreE-alYWyhw_g3pbZyyou5P_d2wUI-aWW9y2nPKxRz9PTANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTphCkxQyMhPT84QgUYYoxDo2lxbHhUD34pKK-5aFfTCJj6cH66X4JQNxQzcJVAiqGebq4fjnxDS53W0Fy4_cHwztVgoMnqfkZdqzWnSrirDHUVeP4CacbXfRzKFAvhaux6roVZh5PnEEx7nbMqYPhIMJikptPV80wzNb3udZVLHZB7syRkLdXfrTyN7PdH2bjG7SFDz4roeA9zzup5LMWxxT0U7zaiYqy-Ivy1jsFq4TvrNgyUGulcZpnOr-WcKlQMKdKFCenLUNMOiJyBOKGUcdvCnva1STDlXeWmFmpBPBtxvl1SIvciWYj90irUSryIOzwttN4g6xwIr9856LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7xrkZMdes8VFTj4apF1g7ffescdl4vaCn7NuVmcSBJwygUvMV26Z1ixjkfST9EtfgDNpO1BRxAXI6HJa-gDiYvvEWtZqcQpbIYJUBGixj1jWRd1vs3onVwEKWYFp-K8spQ9WtpsL9dYQUyRPRhDYUKF10fGu2TdZRYqiboqi5W0iUE4PGimw6ARZv9kUkk3Ho21t-rIEYp2Mxm9zkXpKkHI00Bg40EdUZO65SbYX9f4RBEHeozsadwTUW4w-m2FPjAOTumGm46PaUmVmoxikfwbbnIx8SX1ukoznZftoRdicSmi6XEdXD5CTgqnR8qro-2khf1Q4-kMHqKCLkFVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOuAq6Y-Lpy7wK_YHSVRac41JxU_im2vGOEHWjzsME5HWJ_pq1Re19L1WJjlus7qTk82EJq_vnAC5sJJ6hbbaknnWur0IXZgiSM-SMm4eB7hgiPoFwbDQA1enngdlAHcYclE8ylFm6aiM1ILGwyIFdL7ctabEDAT41l-bxW4pKSSQ7p66DKnMYU1BFAza4CqUkfv07zH2zLAdm9y5Ea0F_G5mKLT_BeOdQp2iTwfBY3QUFnv7Xocsif3sstgr8sHGao9v2XWl9nDexeE-fhy8JwcHgB4BsNNvCfrwe3COMsMmOSVJoD8O0g5p0P_jB3JgKsSQ7hEIF__lUgZSZS1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=jq7ZUfCQsCwveoMH8cB0bKwN4kTi-RHhYNnAET5b5kVeMmH2H_pjggBGHvwVSq-hD1XKMw7Gev6emwdwy1MhTCa7c-1y52CNaBUBp4WND1ToDIvQlyF2TIVBBMHwPsy9id4xr1b1RpCJZ3LUfa1lwG30MgacB7hap1juiL8DBSZl7MjqfLs3cZt4z_NZpHUTyUqdWZZTh3pMsCGOhXmx_Z9AaRlHY5PWTDAGVfSmzBtOyqQcfRmxaHYV2ChOKnQyZ8eTMVdb6MfuPvLqsBcqdYsBUDTiUQqYr1crp7NN8fxFAj4zrTYdSQRTi9v3RVdLpKJNckjfcTgbx-4i1k5qLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=jq7ZUfCQsCwveoMH8cB0bKwN4kTi-RHhYNnAET5b5kVeMmH2H_pjggBGHvwVSq-hD1XKMw7Gev6emwdwy1MhTCa7c-1y52CNaBUBp4WND1ToDIvQlyF2TIVBBMHwPsy9id4xr1b1RpCJZ3LUfa1lwG30MgacB7hap1juiL8DBSZl7MjqfLs3cZt4z_NZpHUTyUqdWZZTh3pMsCGOhXmx_Z9AaRlHY5PWTDAGVfSmzBtOyqQcfRmxaHYV2ChOKnQyZ8eTMVdb6MfuPvLqsBcqdYsBUDTiUQqYr1crp7NN8fxFAj4zrTYdSQRTi9v3RVdLpKJNckjfcTgbx-4i1k5qLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HT4CZRds39HcNXOIhSEAaisvXm22BcnyRNXn8ulbKp87-TDwlv5NwNQkCm0-UCKkZNcc4KvX8vD9Jz8GVhvlaWrMuJizlITu5mlYfdF_RaD9WRe4HtEmZdb6ciTCie5TI82ph_uEQxnEGNnOag5BZItZbVFgK6RzyM-8SNR6PlQ5LXjIqPMV3njmaA7vMsVwX-2DZfkehQb-1lfykX29dE503_gwIehhkzzkIfwCFCHR_1uNwDyxrzQkMP0WCYgrkMOsPho46CuLiRZzDl8i_qu1Fbucqzp-0vET6PAzxD3AEWldIg5laEwa-H65YXDEC9v7UQpKbkUdq9fRv3Tw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1v5OZnQS4kd0T9q9bFj56j61LWjSCpZ1dEl69NzYtMc2Czc83yt8D0Qt7k2-PuRSpR92JivXwWTmWRrdUUVz4WlnsIKhJ49jn6jl0fZn-3Zvzysm_S_xQLXwLI9cPk0BD_vs4spNxHm3c7YfD5FMD6hKpSFedOtg9uTKIU3aBBZze9Yb8qsoCfoBKYTIpH-8FnZX_o9CYadaqRJjW_IC1vkXeaUJOUWlcxlSt59F4NmtoM622DeMO4m3Ut-I9UPAn9eGxKUMGzL_SpXbCORzzG7coABeaIlmbZWkwVqsA0O4qGHjkmJW3sD1OZsfxa1AfwDonwPcCwV1WpjHFwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=oS_fsG2tYPq5V4dw28t-wqNne3hTRe_30iPWGNBsMlrB1uwzm3FPK3ojWp4DhkQ1HULotGAwqZzdUIJYTT9pak1H75BhzuzpCFIcqe0RNHGwxaxsxtir0R-MftfR-pmIZaifsvZMdim7UsE4fmkjoGgMVCTyghSUf-u4h0oUd_yyl9rX_j0lBz7bLL6hkrnM_GR2L-a2XYRS7jN2P0_PlMB4tL20pQAMKZi504sAnRuQ7idy0VDGHGDKX5a6G38AlzCtxPD_IFOgk5Xn_m1a4ZLcdkIvWOoDyG47hnFupGZkHuXGxrFR-UKSfuddPmAplBt2RKYCULF3f0nKysjZ4lXgDg81J01mSnyFUO6bEab2uW9NhVHlHn-C_o2YSadpOkxGBID5PzqKweMGAKhsjfZxl4P7ZI1a7GtjAe0iUTXtJAlHD_gvKiyIW_rWCfkuIfcgC2PSHB_vU6XuklJlhsm93EBSjwx4WEuybizb5vnAX0MhqsaIAFRpOmoKTYtFsGwi3ogr-xvv6O0JHM_hlR-lPGp_bWbrfvVvi3luy7B8NTf-7pR8GhEpqjEQimd3cay1JPxDrEVUr794d5Ekq6w7qA6m9dXZLzaQvMS5cinOjKtOD0L2TIHgFliCNxCs7rVL5qeZEeCJAjtzi9jG8drPSj40NRSCmau-DQQI330" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=oS_fsG2tYPq5V4dw28t-wqNne3hTRe_30iPWGNBsMlrB1uwzm3FPK3ojWp4DhkQ1HULotGAwqZzdUIJYTT9pak1H75BhzuzpCFIcqe0RNHGwxaxsxtir0R-MftfR-pmIZaifsvZMdim7UsE4fmkjoGgMVCTyghSUf-u4h0oUd_yyl9rX_j0lBz7bLL6hkrnM_GR2L-a2XYRS7jN2P0_PlMB4tL20pQAMKZi504sAnRuQ7idy0VDGHGDKX5a6G38AlzCtxPD_IFOgk5Xn_m1a4ZLcdkIvWOoDyG47hnFupGZkHuXGxrFR-UKSfuddPmAplBt2RKYCULF3f0nKysjZ4lXgDg81J01mSnyFUO6bEab2uW9NhVHlHn-C_o2YSadpOkxGBID5PzqKweMGAKhsjfZxl4P7ZI1a7GtjAe0iUTXtJAlHD_gvKiyIW_rWCfkuIfcgC2PSHB_vU6XuklJlhsm93EBSjwx4WEuybizb5vnAX0MhqsaIAFRpOmoKTYtFsGwi3ogr-xvv6O0JHM_hlR-lPGp_bWbrfvVvi3luy7B8NTf-7pR8GhEpqjEQimd3cay1JPxDrEVUr794d5Ekq6w7qA6m9dXZLzaQvMS5cinOjKtOD0L2TIHgFliCNxCs7rVL5qeZEeCJAjtzi9jG8drPSj40NRSCmau-DQQI330" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq_fRMdu25rW_DnO_kMF9a_nFTxHv6HqXnybki7gl07gfmbRHGnnb8Zytv9WPvfolWtquQByOg_i8amAez4Fs3y2Wfnc3AY_y9xOr-LoFEMDXDC0oaJC9dzpTrTUo51MGDXwEDEojTqCFVDRDcs3FX1RIbTiil0zesfxT6YAHGP7nTFOz3iWu872o3Vgl6HBzJpZ9EQgKpt4pqGk7sWLlPn-RdLxounOjU-IMnEFI-TNrSplgUF1SQenXqOLXY3SIeCsoPIbcdJiTLnoiTmD50fWkI0FfJBYD22sQGZvtwB-izmHkIUQLZpjUu2rqIGzGyqVb_wvA2mXi2yy7dfzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=h0rfxb0r_VbpOdUebbRrwZlT4JvLf6weAif6ofzkHzPWCjudQZc1Zg9ojzgmfRoRLv8foJBPr-rprN1C24bnAUKiQk47UqvFyJbBji7mamrdcQcQM9rU3Ck8AW7ia2zdXg9Ocoo_3Hi74B_A9J62fsr2znU8Qkhptn0mvqI6Td6ljT0ki1bVB0mgAdrNjCcvAPhFSA-9S2jDCOEVuOQvbISAoAutYsnDppaZFRKXM46p9PK1867_yIVtn6rYIDr28fWHUATZsclGfhiHjQ5wI45-_2muv99FjsAiR6Ybleo7CqMBsn0SbQM8K9sDeLD7_E6sXdId6RJvtmsmFKyY7g-P3coZFJ20UOT7N1O06xKi3gcIfJp8OBnKRzl3NELf2ZwFcpI8WGe9zh8_zeFXKUpIIwSwcSlUJEmG9Qk09qj8uKpEyuhyE7hfiFEi9EOxEgiwndIk-tqE0H7aea8FSbCgOYgQ1oKnqk3FiGydSm-QKlz0jveZUXbTo0G7_7uFu84JutRi_icVyWl2P0amdx5JZ6pIDCizt1tWnxGW0wuBQ4t5G1yMtzH6yT36t7aCKkKPottdeI87Pl0CWuFCMjnB4YC-vF1ZCrT2QRl8i3nqcHW_i1odWU37R3F9YDuTJLvvx_k6LpfTdRVSgaEzagZ2NZuM7wCkh9QwhM_vNlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=aTyesFYz3k60hBI0PR-36W9okcCiFiNI9_9tAa12eU_aQHv4TZX98aVk4gP7WhgvZyWZIxvt-4p8QBN6x8huVDmNBcUmdgQq7mUlCvhJ-UrAIzh7ODmsOMFCEwK_JkvZF_YfDJpd5ctW1xsypX-dMn7JGNF1ZUUCezZs4WwZ4Oanz7ybaTP72UbG3mH5fco4bXalTavHeek63C_cQyqzkEHUQJrFWjpMUbla5uLCA7ntFCVM4iw_K-FvvOdRwS2OG6NzuPdttwvNFbqKQksl_eb2uWaRq-vUvZoYpv4dXVWdvDn-Oby5fyqQV0vpMUexGO8nB01u5YQhqq6E7RyQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs1EnwjQRiPUhlGOBA_7KFfxDRJz_j5PZvwJzY39qgXhV83swW2DdtdL4tZlfntwFOt1uPGC2vqRCmVaBQEatPrzIzs0Lx2Oarx8rzcXbdtKzvr40u9rEdIwb0WYelelvRPkI8YrGm8u2i9j5RLWP7TbrfarWr1idji2QoQPAeJNdcqCCDEUGvT2UWcJj0faizQ8k_gmzz-56OWEr6t5DwtgA16jppvs48hbkIe4qkdfsmMK7Z45MGXUVFQSaRXbyUPqArd-2fNaMXRD-E2-jB7N8_loYH7aIwAP6LFDmPiJwRQS4An4IR7-0qjZ81IV-TFIMhLrJshbjwiHepp4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22651" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAn8vhCyXwnFuIuXaU3zcI2XlqBQQ4F01-koPHWciDC4WqjwzMFl_Kuu45DDMy7jsfppB2qS5ETJxZ4aAMsVeinb-cAHOrqXoQ2LVkOuCeZQOXni5SMtEDNHHxyNrW1EPAJlu-ypdLQO7fY0jRo8AGmnmTZ1QC5EO6PjiKcnefsc56KxQdlyFgtWwA4rgpgtB0Y9VIBMdeLtaQ0maGZjvRwsLfv6GycEdCXBFKepDg2-JqS_Wxt5Xtko-k7GtBu-3xYpab1QCmGeGKDKhlKwFs-0o7xzYWn6B3R5iSom0BeVH0avekZlogatBZf9MaY_8fP8-_0b45N-T6rKbYNq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaOHNvDT-Y-0KJhjWsgphlRduDHKEYxFqfEuz8dW4OmRGknGovcTmreZ6qwTwo9k3MJheS1TFNpUOGRTftYG1_IzCFvB9VKgjWBZgEaTOx0U2_fqZFHlNutEox7oeVudCcz-UC_Ay_c4J2fYROLZFKQvU5qSO7RnX6pliPrwWy4o63SIwqMW1F7J5_x3JN9OJxqe4n9LavKPZs8fBZC5Urv9Z3tD7VpU0CJhn9wDIKUJcYzLQyWoDFSGW5io3_wPdIZgIvnftXVRyZvidu0KIOqgPSCGnf3dBhyYRqJmwk2hhONp2CniW3Q9LirreKYzb2LzKSO903EB8PgP4_ADoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=aZcj0E829EIQ4QtQZ5EIt3XdrGrYj4vtpUtfgb67Bh30BNXigXhlYicQQjRprHsUi39XYnbyAKK30IhEUBD_TzRsPtrhJBUtmIMWfQ0ENZPUBJclq-AD81TawxCVrV2vIiB5Ou3h_DGSHW0g0K5DrugP01rTBgkleZX__zwWDWo5y_v15P49gwFaR-0OproDQJ_GtMTPw9ciqJ2oUyI3SdlGBzAxk9CAKDmMcgHpyUHCKsmByXSln1AFj5FDQ9ZKXo2Y6H8P8tZgnlq1mmrRU4ORCzK5DYWfQrW4J14x53WweRPE7IIp4tWGyMxdmuVPVP5REcLyo57QshE_5pW-Sy0aUb5AOeNjeOPgfXTBK4fgR1NKJQBbi0aXd9JE0SjOLbXZzuTHo4DTVhymM6H-1pKirY7UQiAY6ncjLQn6JiiuDFVOUYIw_jWjMqzKlpJhp0lFaSB3oTumecRDaffjHbrmIVC2uvBgoRF7iqo2-mv7yzvOJT-fwVKDYue1LKTioKJBNALQSTZ8nS-JJtgi1RqQGqoMof_BG9VTI_z7hwIEc2o1Hq45u23vTwhgrDS-8Dq5qKg-oC1E5qlmLwbYVifsZxNhLBuovAWlqA3noMkm0j2vrLhxFT8g1pcu2PHMZSgtbc27oSNSNCpgsQTl2jWx9brPiNKwgDk1w3QwB1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv-W_xr7beGP3DKGWcH55l3k67riB7kuCPH7E9sLF62pUWoXAJqSy_4n4gXTSsZt8xuonirddlVQWBsvmHOmc_8logkfnC-cihuNWoyHOj0hfg-3zAeoDdqZNYF4t-x9jD5h4xBvEUKK6mlVnDwtGo1SXr5DkYbTN6X7NXo3xL_WWv0VACIL9P7aclJ0XxVYIzhNIAj7HOBdLyef2XJpLD5KpkczbHq7r3ymKyy25j1N-ZMZ0-Ime20Ma9YROAR0trcNumuQdcGrGYr3TJFbpQQNefP0GWj1dqqaWC25Q545bOvGvp7vb3w2xQ0Di77iEWmwVRVIZ5pk57v9HgRhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeCUMZ0y-JHa2kqRNdmLV9v_jdBU_FhZSO0HkjIEHhtHtNrXjSXNSlh0ee2DQlbIqlKY9JSbeVMvPWXLxRUWVPVnZ5YpQerqppKy0g_EJUTNiWDeqGTnpJIjcLb_NvOjF1K4lY2KA__ZQZrA3uCj-Z_fcGyvo0cXgqnPT_L7YTvbnpx_o66SigA4l_t4Walyl3rZszaPCUumaUdJrZxwOblYSwwDdAlnIyTq5kBLhpGyXW9Kj9jFmUURfqgb7Uc33METsTUmddaT2zisRdGJ_Blh6GpdORMmnGroxh4fezihT3p5cJJ0ovK7TBhut1ncw414L9XClOyy7u7xEkGwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwKKvlaSjGTPLPwiKIC5nH2y3Rla5UpPiTWoMK2s_8MRU-wdlgzuOB_-KOrHaY5bfm4Tqtg_aqUXaSwGIKjB9l38nbIPXbG5YUyDfaAkdu11Hhx8ydNSbAssh-KKzKRzZ94StK1OSGFa--6ZHbYmovXoOYbhgXqLqNOmxpqMkleU3OXdxXVxWnbRQVCAeqNciPUuIgEA9UOeTO-jFgUqjuo4tFScYRjdm0fIKxV16urA_KHmHsgNe3hcD7_pCQph3xPDt6cuwRnsKJBi5CmSx-GgKV6fZoYNSQgC8z3I1nJ_cCAM092Zf-oQU-FnTJoGe9wrEXsbrEewqvR4SEsMnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLeuwjl8tDKYuoRtUgQNB_Gv-qJLhmMXUGOBNh437hgFR77sEE2PF-rK5ef5xqFFphskWEMBMlO_4tauRONeiAHACJNPl-T4sC7D4PgR9QKpwK9FwjjHvhem2x2swjg3ExppYDfv5PSK_aK4Fn7BKyALvlfcJ8NOc6aBFF5FOlqnQBaz_dVDbD6PhfpjGf-detUozH6zn8rT4PZwO2pobx-9E7gTm5SrrMhIs-xYQ21VBP68do3o36dSsHmkosrQTnMm5eHWi4EjPeQz26GNU6a8J72rtpwnI2IIDzZ8BI0ITpmhf7JvSuRN5ejOLoNCER4nk40PkaIWiS0bqJqEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBbqyuMKs6a8os9I5tgxS5qCdZ-pjCsKAdjgpLRWt085Kz7STsghfKYW4JTc2L25XDip7omJd7Gsx8n0P_Bca_RmZeKhb5-avRVWM3gxTik1qgwlBXX03UNwrWzkboDF0CGDlaFoJz0iHUwwyRy0NC_yRhdftJ0Sg7RRKlrBonnIfQ8BqvpDR0-ggbIzEpeq7cgLYVv994fYVNhFvKBOPJApnYiKMeVJY5tPgpp35JZhYGuBCfg9UAimCKM8TgDa_l4ad0PN27iKJJXcemYn6dOv4LIsjT496k-E8qpFIxMVl5WP7rwpTpbvUcDq1hfCn8OeLXhMfnHbOc4nWjA_pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=RDzsWmchpWd4sj9UqlRxTpw8CyKLgn1likbCkhvY2Ia4F_DsC0Fk03AhTui_1wTUzz9-9Eq-uWMCzWguLQz1bTcYenN0F4FJ7BJ1kAoJH5faDETV8_oL0s4nWDpK1Nvay00whEODGzYQK8D1SIRCp67a7huk59gcBsahhZavmZv3U7Yw8ognACJdQUb7DTOHTOwM9MmZKc67117HfX0L-s4_04Fp8HpUHN4kOAAJFZamKgV906Mr99rjxqPTJSPlOeF9PPnRwU0dMoA0jyI5pTbWjIeQmv1HEqW06UWV92ak4DuiCjkg_IHHspHtPlWsVkmmg7BwUyEfO3ZDfxjnYp2xszZjeDlQq4CPmiU7Z7o1Ow9Xo532zAMaq8N8SzM9YH5r7m8xQa8ocvwIcWdPmHeGdxOeE8qFvMlZdixWY8dOwuvQwW4F8YOPn__O1Dvob_gZrg0WoCbJfClyHtbzUJGicuDB7lFEWxFl0t2qs5AvMwNCrZjG9QzYki0TpzXKT3jcmCNA_yqF0oQfYIC9n2eHAveAw_eJX6IifVT3LWq8c_XjrgbwneL3EfGjZ5Kiv-OyESDSpljLzGiQf5bFQ8oLG6ClerM-vNDVGWGdo-MrJjV3TNtINClMLtf4542R8VzLS_Emex5xy4HacZnn3f96Sve42sg8jqy_On0n_4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=RDzsWmchpWd4sj9UqlRxTpw8CyKLgn1likbCkhvY2Ia4F_DsC0Fk03AhTui_1wTUzz9-9Eq-uWMCzWguLQz1bTcYenN0F4FJ7BJ1kAoJH5faDETV8_oL0s4nWDpK1Nvay00whEODGzYQK8D1SIRCp67a7huk59gcBsahhZavmZv3U7Yw8ognACJdQUb7DTOHTOwM9MmZKc67117HfX0L-s4_04Fp8HpUHN4kOAAJFZamKgV906Mr99rjxqPTJSPlOeF9PPnRwU0dMoA0jyI5pTbWjIeQmv1HEqW06UWV92ak4DuiCjkg_IHHspHtPlWsVkmmg7BwUyEfO3ZDfxjnYp2xszZjeDlQq4CPmiU7Z7o1Ow9Xo532zAMaq8N8SzM9YH5r7m8xQa8ocvwIcWdPmHeGdxOeE8qFvMlZdixWY8dOwuvQwW4F8YOPn__O1Dvob_gZrg0WoCbJfClyHtbzUJGicuDB7lFEWxFl0t2qs5AvMwNCrZjG9QzYki0TpzXKT3jcmCNA_yqF0oQfYIC9n2eHAveAw_eJX6IifVT3LWq8c_XjrgbwneL3EfGjZ5Kiv-OyESDSpljLzGiQf5bFQ8oLG6ClerM-vNDVGWGdo-MrJjV3TNtINClMLtf4542R8VzLS_Emex5xy4HacZnn3f96Sve42sg8jqy_On0n_4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAmoNp1sZi8lzTshQ1MFZKxmn4RhBmNFAvLJ7jTiovcv2OWe0prn3Hl_WSgJ0UoxLQC0iUklChS23BQ5C5tS2CD1T9GIRSagXu1pUEvMOl5VnFOAWCuhIbTf5-7A0rTBMiFp6Y2Vqlj5RdY6UvRFwRrg2Ak-X3JsM5L-P5swfkDXQ8gzVBLxERgOrlBDawCzcMbEqxjJPH4w1zwMr5OGTazkkbSggIa8sJpT4pQj1VHVe4PF8CVdMa2qX2QFz1fiDJlD-M1nJR_askrKS5hwcHBs3i5QP6RFyG17_pPuec9aNosJAw0zUiz7WqfpQjF865LVcHHq3LQgD4weuqKUuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=tXW5w2r84FE6AXeY6_eDuKCchI0Utdx8xg7_aLIfXXtGK_HMoj7vsRPap7bzAiGrbOItffOfsH7Tm77YTkzds-2IAf4gPlbe3Zi-lmwPXQJLOX9VjZi4WrOMDOPUkv8Zt007GiOeY8NOGcOfqqWh7dnniI6knbAkuT4FgewX91zbYRXKPrJsK42Sfrftxcd3UrGNNtaVb2Q2CFOgCz8DoSKYw6PQ2tP4CDxPvpD5CmDd4VdLxvoU5jSKxPU1xTi0ZW9wf5-Jvr1F3IJWaJE9GXDAF7AUqrs0e6UtL5mNp2yaV_gmy5Cy9xLYTJukD5vVgyNsAj4fYObWGMZ8GjmBNKe0UA4-X8kzEuM3rdAdtiqpaPnNEFCTpnCwV_75agZQqOEoPnBlSw25LQYNVV0wsE0uMTHSL_pJOHYQwl_dEvYFZcwy_29vOtpp1MXh4n3yB1QfqGow0TvoXrfSj_Ubj9C4GCqjBDq8Abr5BWViC45xiLPxQakc7i2p9ilLbpsSYt6IF7f3pYdEU76bfjHHGRU3LD-ps_MRhgfOOsbQ_OhEQJSgTLrKLrL3oOZhDJm-WBYQVyrEPZCbABQOf8-xJT1Z6pguyFvit_ucNjCTytFHVbSGtwMM3bME3EGPxYjRkWK-YRrY6V6SF53FBfj-6IOfYJrlPUM--TcP6YlycxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=tXW5w2r84FE6AXeY6_eDuKCchI0Utdx8xg7_aLIfXXtGK_HMoj7vsRPap7bzAiGrbOItffOfsH7Tm77YTkzds-2IAf4gPlbe3Zi-lmwPXQJLOX9VjZi4WrOMDOPUkv8Zt007GiOeY8NOGcOfqqWh7dnniI6knbAkuT4FgewX91zbYRXKPrJsK42Sfrftxcd3UrGNNtaVb2Q2CFOgCz8DoSKYw6PQ2tP4CDxPvpD5CmDd4VdLxvoU5jSKxPU1xTi0ZW9wf5-Jvr1F3IJWaJE9GXDAF7AUqrs0e6UtL5mNp2yaV_gmy5Cy9xLYTJukD5vVgyNsAj4fYObWGMZ8GjmBNKe0UA4-X8kzEuM3rdAdtiqpaPnNEFCTpnCwV_75agZQqOEoPnBlSw25LQYNVV0wsE0uMTHSL_pJOHYQwl_dEvYFZcwy_29vOtpp1MXh4n3yB1QfqGow0TvoXrfSj_Ubj9C4GCqjBDq8Abr5BWViC45xiLPxQakc7i2p9ilLbpsSYt6IF7f3pYdEU76bfjHHGRU3LD-ps_MRhgfOOsbQ_OhEQJSgTLrKLrL3oOZhDJm-WBYQVyrEPZCbABQOf8-xJT1Z6pguyFvit_ucNjCTytFHVbSGtwMM3bME3EGPxYjRkWK-YRrY6V6SF53FBfj-6IOfYJrlPUM--TcP6YlycxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEkNwRZvFgZt6W2k6S1nsEjeDuA5P6p8h6D3U8K2kNA0CokbBhHRLyLHZFWLtc6cBHhCdYxyOVYtN88D-Nn1Y-07g9VCGawSsiCxMVvPW4SZKcxqf4nba7Va7dJXkkO4ghw7EQpnFzHliRzS0tywr94YbjfkBZ_BVtQ1aENdC0KdLNksB_xZbGM09GHuMEl4OyB4u8txtrErSYmNVXpKvKFUBwcP_gwbnMYk7mMyg1eNmOWUC8NFn8Hem40eNoNljaDqFhko2qn9W_5sg4vcfAS974bMWsIaNaMLX4LoRJJUYibCmEkX9hxi0aOJu_rHi72oTGqHq-GUKYNHxL9fsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR6wCtNZ_cib1DqTeyYyiP8QXbJikTQm7P5YZjUA38Ss1IFr_lAozNwMZCFy15vjlM1zY5gyw1mmV6lCntd0mZZekNM_iN9aJuw7sOOYLMqZeeo_2O1tG8TPLzhmoBAdag1T2ZgvC9wpwA6UEBLQkFQlWpZ_s2wVx-0CHNCGh2x_ZZvrIOy9M0U01wbhsmSq8nkLns708RQydSVCEoTVzBXEMtxznAw0kDx8Qyj6QFVJKFdiEM0B0rPBFTEcH7y7lItW23KquZPYkxa4s6Wv88WKY7Ddi9oi-y_ZqpuxN5KA6vh7X5jxvYej-Dz2q6PTT-41qf3ifLrhcsJ310c3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=ru5bBmEsHtoTZ95WG53SzvuDK0yCFdlzzfULaWjjMqpukWG-lRUwpkyqguGRCFIOqygENBIdAvZORzVl-y4jphD5Dm5tNHLG12phukKOlAwmqQBacAQ06ynXzelo2Tp7tAKn5wcg9SxqxV0kVb4QVAadETXsSvvxbiNNImxvm7-QKNSOM739kOxACel6odcIIMPXHNGa9ujzfoE97d_HUocrGyhYPO-MIrq-uBeNhUvl8w_EfMV6V4DP5ZISmgX6I0LRIzuUN9DrDzkP9RrkAQVqe9zFlfUSEF1-VMTcqygW7BcROEBtjavKRBVHEQQrcm9ZXp2egwR8wgJtHblhYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=ru5bBmEsHtoTZ95WG53SzvuDK0yCFdlzzfULaWjjMqpukWG-lRUwpkyqguGRCFIOqygENBIdAvZORzVl-y4jphD5Dm5tNHLG12phukKOlAwmqQBacAQ06ynXzelo2Tp7tAKn5wcg9SxqxV0kVb4QVAadETXsSvvxbiNNImxvm7-QKNSOM739kOxACel6odcIIMPXHNGa9ujzfoE97d_HUocrGyhYPO-MIrq-uBeNhUvl8w_EfMV6V4DP5ZISmgX6I0LRIzuUN9DrDzkP9RrkAQVqe9zFlfUSEF1-VMTcqygW7BcROEBtjavKRBVHEQQrcm9ZXp2egwR8wgJtHblhYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3--H3RGMEnJrwVVRQA3l7ttGwDwGOJKWzkz2odNG0raFLhH8ugmZ38F2tjRQCbpk7YuS5n1u1BNt8xd7y2wE3D3VHDJGEKS2Q0_jpVqYKx3y7wcwmBMCX7GzRkZGBlqgibq1a_9Hofrlfv_CufS8yqY7qj9oRWQ-689t9HGQNVw7OD0ZzJ1xKij49cBMyWQ7KUhaOIsL0Dke8wxwL41fLPVWpcTyx-eYYuCCJG0My39rDeTP9E7VBucK45SIIdFsrt8A5osaK9YLjKZPVzEy97QOVz4WWMX-t4Z_oEMeEb8ucBJl8Pk6Yg88aBBbW_gwXmHEqsLyr3YbRtf675GOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvuBKlZWTIjQKWGHdAQNH5iesiiDzqUoKlkf43lSic6570HxdILTnXPyKJrahLPk4Mf2AbfVVLXJHuuhLfu7e5zCyOTkG2D5BbsRH3_-sNiMhFi9z7hYiNaLJfI47NyzQIjCQ2RRHdXjqZ9poqQk_RWTs6GRH6DsPf1KJ8KeCPl5tkhy7ApVsRLqFeyfMvsfT6MJhikcy9ZuImJpXzk4CSaiYUGK2wdiemIJatvPttltut_cmrQWxqpWzjPAHkX9nti2NmeaLOUe5n6uKLI04jVZZunZ1vYAbEoZtOm7QuWC4Fce0cLqVPrrykoSuHHM4SxXOqw4YgQTnfdH46pDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=KMalStg3lx8Nh3B7wmA6VZ6UKMQ0umjKBeGoWU4ZjBiUiFz793L4yNyajftiIa0xP4RGeboaDA_idJN8h8nRqknSGf24u_eyVkm3gFt40NDtDKD1xWbYk3D_Ar-Rvukd-vg6Zzidgr2aFOEThgMW2ZQGu4IoaN0k0HhS-BdPikDJH8CYmNDWUf4_d9gx2H-NSDhfPClzPBMCgtxFZHVuQbXzgbpE-CFY7antVBF77eDQD3RO2hWAhzhSRWkL3XiY3mS3K3tesMPeVxofKkQReQIrdrSJt9dCJNRsbS45MjXrJ7sI9iPHdlmVnjQ54oF3WLqCBt5X2oiptSBzn4sgCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=KMalStg3lx8Nh3B7wmA6VZ6UKMQ0umjKBeGoWU4ZjBiUiFz793L4yNyajftiIa0xP4RGeboaDA_idJN8h8nRqknSGf24u_eyVkm3gFt40NDtDKD1xWbYk3D_Ar-Rvukd-vg6Zzidgr2aFOEThgMW2ZQGu4IoaN0k0HhS-BdPikDJH8CYmNDWUf4_d9gx2H-NSDhfPClzPBMCgtxFZHVuQbXzgbpE-CFY7antVBF77eDQD3RO2hWAhzhSRWkL3XiY3mS3K3tesMPeVxofKkQReQIrdrSJt9dCJNRsbS45MjXrJ7sI9iPHdlmVnjQ54oF3WLqCBt5X2oiptSBzn4sgCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT4g9GsTI2dg05-w1-MvclxLLCVkFdoT_V_HqNvqlI5DQmgnl891EOWt4WPR6FTsw_8hMRRRxKhdm2TjvCq6qXG55DG0MT2kfE2EUmh0qf7MVLaKGSS4hBMlgUTwWBQtkSV9BsdjDYwP78v3gvvfnTr-y6b9tO8c6Mez52JYM7AmNf3im04-1EEhrD47Pwg4DZ_IEyYvZUydWGn9LW0VkSGz9lXrJfuqVRaprxzZUKxQuEPzgZ_IWFKYPSDahsL69estlo0LN-nZ6mq_fSQ0ZZjU7LsZONTfIkvStKqp9Z8bEhVzwu1k03bMs0d-gzD7KDdx2tzt2YFF1Y-HSc24xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQA2hLsAKlSlu1OCb9Y2DblO0cEczua2grZoCHMc5xKMh-JN9tpsS6M9_paF9vUrzW_l0vihWCZKwWMRkipUPVJsV_uy1fdbO2gOWiUBKEvPvY-_OmWeQkALcbRtUiLtejVDdPK6tVlrCRRcUB-llCzqYYJn3NqxhSbtGQlBNZRIGwf6d-ncGlAzVkkLsMyX8HTpfTXbpfocXMBMc2pKoUfQzQQXDm-eS2USIA-OZ5pqajNwmVD2p9uUpnxoz05OPphd1DaH7JiHNpRSmfYX26MgNNmehwGL1_GEx6gh073-NKxqwIUAlTP6TazfMTSKqJqu1G5Bnz3N8KiB9T4_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=n9vGqhayUGQnzXKEfBiDs2lbZvqF7mhEXDecXXbCKQ-xVMMn_glqHzg2gywDdNjT_XwzprkmFlQpv2606ZIFAqRAj3B2suZDkP22Sh0BaYfD3su5tKBKmOEgytL0IoqPMtAARXwD7VjG7Q-gHqTdnukjxVvox_1Ht_j74TFod1FtFXoht8SFz_rr7vWS996jv1sAWil0XwXogoZoW8KzkX1ry5DjM-CS8bzayJUqsUZ70yhIcORmoPjIZ5jHewdH5prOS14gdijA4-f6QF67iDBsY80o78IBacHujdDCpE0n-zpdALAcEC7qZ7C31nCMUuE67I20XQV-QHE6NI5Jlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=n9vGqhayUGQnzXKEfBiDs2lbZvqF7mhEXDecXXbCKQ-xVMMn_glqHzg2gywDdNjT_XwzprkmFlQpv2606ZIFAqRAj3B2suZDkP22Sh0BaYfD3su5tKBKmOEgytL0IoqPMtAARXwD7VjG7Q-gHqTdnukjxVvox_1Ht_j74TFod1FtFXoht8SFz_rr7vWS996jv1sAWil0XwXogoZoW8KzkX1ry5DjM-CS8bzayJUqsUZ70yhIcORmoPjIZ5jHewdH5prOS14gdijA4-f6QF67iDBsY80o78IBacHujdDCpE0n-zpdALAcEC7qZ7C31nCMUuE67I20XQV-QHE6NI5Jlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=FXlpdKqzcQifpfGAJmqz7Of-Loeovl0C81VzKu9w60Fhq8OFIJw79TiVspNiUhZj7q2rEbZJg99gLj0j4cJ9TYam0XLpktIzyi4OIYRwGDbKMJrK1ypxvMRRKUifd42WdcIbHSFqkpk5hKMQP7zRGExbtHegGZroDcIu8Xme87OgeSAAHjI8dOR5RgM537QcfXXWLsPbYVaNda23oQRJKIf8Jvd0SsCPk3AnP0E41Q-ODVmBrHfi2DEwHSY0YWJ6uTx1MdfR4heCEo__5610vNSaxDKHAXcmriZMPPCjGqlrAckk7mEkTUGExjofCK8iMRWhwfmdFdfpmfhdmL08Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=FXlpdKqzcQifpfGAJmqz7Of-Loeovl0C81VzKu9w60Fhq8OFIJw79TiVspNiUhZj7q2rEbZJg99gLj0j4cJ9TYam0XLpktIzyi4OIYRwGDbKMJrK1ypxvMRRKUifd42WdcIbHSFqkpk5hKMQP7zRGExbtHegGZroDcIu8Xme87OgeSAAHjI8dOR5RgM537QcfXXWLsPbYVaNda23oQRJKIf8Jvd0SsCPk3AnP0E41Q-ODVmBrHfi2DEwHSY0YWJ6uTx1MdfR4heCEo__5610vNSaxDKHAXcmriZMPPCjGqlrAckk7mEkTUGExjofCK8iMRWhwfmdFdfpmfhdmL08Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjOcITg7Xu9mrgUocUb0u59Cq04w9CJSuIxidG76dciETmDhZr7Pa3LvlvuNhwO9QQ7cccxIESzxb_3YTOHayQlAygoLzF2L_t9T5Mr1EeY21vreLZHQRVGsNngqzhPrh_ovG5oqlvPEGJjdZjS1zZFSdgyY4Jfbq9AYHsAAqZ-ct1-2meFJK7qQ3F3Vu05L15HZjhgkb1Jdx1aWuKHeOPFoRThvc2ZEJXIl7XgB1s_MWbCXIyCgbWEI-iciHu3ZKB6MxoJsx8MrzAkANgm0gGyDgTUvSiIO_Yl7fYd_nrmIK7pM6f0VPW5oXzB73jk-QB9idQknOV0GHP7Am03r7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbLBUVQyKTs7y8sEpdDq7aX22Z8W0GAG-R7QcuA2c3I02fTe4Zj8hYYNfspvZ5VRJ1Z6_xvjvywG1sYPakzFn9CRyFWen7ZUIG0WMTv3Tl28ZsxyMu7DCLxSspUAgcbpcl0HaAAehVQyZr95G4txxCJhRQoBhCxF1z1VcCaFX_S_fsYFbv_KLZ0SZTVzYBCsASUDmJvKffH0OzQgFevNgmwCWlbJC6K3Wv3vOpWA74_xCMkUYdH1WPlJDgY8JCLE1PUo0tQlbrCO-Ehx2wwRvftUYIYLtVYpxq9bNoPuTaKj8aHxAM74G2WCRtIewcJOlmUggaErJ8QP81FQ4aoTKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=U_xLLmlmpzrsR0m2F-Bct_BI5NU6jAsKYCW0wMSeVOfFFQ_2SXj9g_OvUpGbo2yTTm4vCnYBPc37OEa5cYMf5vD2Qp48xig8Yv0C6-CyZQu06kUpwUm6oY0zIqCz9RJHS4KVI6CwXm16UXZHXUmg4sULCZ2DpdfbyHQenp9w7yUSy4bo4em2yI_WRBg3Ju8P80udYHTOLIS0HrVvtJITGliOviHHdwXNQY3M-Q0CcVfnq9LAo_ciFdehASo5PFMS0fDsuukWBjhIbUWlnzMU6cS-HUmjyyPB5ZpQPTKs8SxUYrfZ6yu_omXQrinT4kOjVLemoZv4o_Y6jLS8qHhEgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=U_xLLmlmpzrsR0m2F-Bct_BI5NU6jAsKYCW0wMSeVOfFFQ_2SXj9g_OvUpGbo2yTTm4vCnYBPc37OEa5cYMf5vD2Qp48xig8Yv0C6-CyZQu06kUpwUm6oY0zIqCz9RJHS4KVI6CwXm16UXZHXUmg4sULCZ2DpdfbyHQenp9w7yUSy4bo4em2yI_WRBg3Ju8P80udYHTOLIS0HrVvtJITGliOviHHdwXNQY3M-Q0CcVfnq9LAo_ciFdehASo5PFMS0fDsuukWBjhIbUWlnzMU6cS-HUmjyyPB5ZpQPTKs8SxUYrfZ6yu_omXQrinT4kOjVLemoZv4o_Y6jLS8qHhEgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=AuxBA-wNZMUGcQGce1R1gcKPwAezm1CM1DRQbvIPezwwPZtIUtHoeigHGiPz51de6WUMpTTB7HtUBg7y_k91rqBSX4J8RrWW_hehqmGlMfkpwgRrS2T9bHWfaSGAJFQsYdjisdQw3wOIsYFbySfqDXs_Epi-Ozgt5NcMvZTXxIsCopr_-XArxonIZY2dvBi2YAvFOTC2E4WCX8yJUxvIqmsn949eNCEfg-bJb34wMRPZl2yzvKaBDV6FHVo4-pejy0sfMdcFPavivVZq6acIT76aEso5jlhvwokvwCSHK6OsjVyYesIpIIchsmwe8aG_2p_9bonGI_VyXHXC6GK5PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=AuxBA-wNZMUGcQGce1R1gcKPwAezm1CM1DRQbvIPezwwPZtIUtHoeigHGiPz51de6WUMpTTB7HtUBg7y_k91rqBSX4J8RrWW_hehqmGlMfkpwgRrS2T9bHWfaSGAJFQsYdjisdQw3wOIsYFbySfqDXs_Epi-Ozgt5NcMvZTXxIsCopr_-XArxonIZY2dvBi2YAvFOTC2E4WCX8yJUxvIqmsn949eNCEfg-bJb34wMRPZl2yzvKaBDV6FHVo4-pejy0sfMdcFPavivVZq6acIT76aEso5jlhvwokvwCSHK6OsjVyYesIpIIchsmwe8aG_2p_9bonGI_VyXHXC6GK5PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsX2o8RVi8dRLJCXWoJkife0OAU4RhHS7kuNNBe1ZGlkhdNao7kXeEFz4wETmPUbwQ-6WuOTtPo7WcimEmTCEKPGIn1KIJorFA7ragvh-vJeVlf77v5p5E-3zL9O-js3-slYZEuMn0_YfWA-VKRn8jSNRH8vYNekG0XHmm1s-tcBZbk_Z3H6YqMgTYF84IMj5avaMzG0CKhaZhUAllWIGidCmQZmom6mlRkl0H2iFGSD0VB27qnn7BCeuY2670KYTrxv-ws39zaZ8u2WGKFWUYKe-xyRJK5jCJ16YcZl880UbYoqNo-3TGg_gwP506G7_gMAquil9cMmDm_jTgxD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2zLsDBlZnJIGg3g0mbSMPVps95434bnSaClTvTe35oQvZ4tTe7ahFI6HCaH1lah8NBTxeb3IduzMtiuM8fRpqzSZ67CC2MzUYd_mC0wamPYbswoaLCX2ZL-yabSxjwOpHIzf9pNvb7iXMOq0ezoAFhV9C8yImA_ihGfjq0FQXqkyy0ZdvLZUaUNnxFZBkMPl27PLrO34wP324aaF4phroy_M-jhlah2Vgg0U-EqbzGrAETtQEg9yLwp8Daygfi9LeLZz_tw1jZlIbZq_N3MQpwOEmVt6Uiwqg_Rmv8spZ8MJUy9EhPP1An5LZlnpbpa4Z2wuw2GHKMj-ixgr-Qj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9DfuRHFjbavY6VSCIEXRTDKAbcFpCVY3XgNqAUrgXN1Y9IwzYr5ZJFGXfbnJYEm9UMValxg2AQ-lQ4ZD6tM_hwGcbxxic-D8RLWaiJ6hEKZ9UVZnvITWWFslDaUeRwpKL_TZ4NtzFSJnc97uMAQ_vTn2Ppp6RKY60EDv8JPWinRfxa3sGpX6oUMeLL8jEkecF3DUxdFJCkHLEOGKm-Fj9khfWvNWozjs6v3KdrEdkZMU6pSHvXdbr1v2KitklY9dbu0FrIG8vDBSLe-HBC5h2ec3I51bqeSqYjwedGDeE4jBuQ_5AxoK8GA9epytiLpjm30pwTmKBJ56JKns65bgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c27C5_rZrjYtGdTTJoCM2p_CewCkD8AOsEyB_rJDKDq1QRDT-xAEde5pV-3lvnZxzCtd5VptaUafHbzXuBg-kwEVNM6bySu45rfivbrI9TL6LX__FMhy-nPoJEciT0i_tDA3HCyMUwZod_dm1PkPE3IgzchwWA8oVoCR2sEKwcV9qM-XnAxdP4ZalL-HLJOjhvb4U3djVkt4mryTNEdQ9o9CwNOnqbqOUFp224ai5orpnjLaOcoRC_-0-FPPww4IGLhYcwu8LiLE1qaKGlK5uO2o2KbT2RqM8chirf8AXqBElDswM8Wf2p12PO9npM_wVbjfiifdWfx3_oDZhIPLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diJYPIgqVfsFM_k9kmAFlEpUttyZ1Z3UfYRJHO0ErPvq0xXkyfFMJfZ2MVbEdotdjPGPvRVs9r1Wh2KPAznwNbIRYrYaejU31J8auS8Uynafh6WCQy7E4gl41qQASqZdkmGEVLPBwBNv_S3C5EcER8P19_c36p4P4YCh7T1ByYXEq8VMle9HTWzTIlt-PmUtITFZldgeBssBUd6VTqd7Cn9JZtQL0R7zGUx6hSElHKCGqAXpWr-Tyd4gRO2eZWLRpsbpoRZHtqJrGXqTcdytqw4lssKjf1xx-H2M2t-NiJsoBbF2aT0Imst7j6HSvwtNUH5jTg9BHXb3yKeIh8CvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=uyQ2NGzwxnM4MV8C6ziLyhTAP1pjx-Epp-pavA7A4baETlMpX2XLTHg9edyG1ruJ0Oww0co4Se052OtHyJRtc89Igix0WA3pIvIFlaJyTUb4PaUDPPrheBruMLuWq2mgWGL58lVNoWBpq0MTNrx-p5ANQz-IPojOoGUGZjkBM49pCInFLLAFZ6x7G6Ss0eZIxNfGjpX7au3VQY3DoRyvsnp3A4hiVE_huH8AAFnl8-PqC2kRP2wtHCFoECSL_tACv8f_jBcMy1Eu2zCZ5OlX3qGCwBSdwj_qD92cPt5CrX4kwKlOqjY9q7sxYgnKCw9IqFF0GYOg5Osp0OObaLnfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=uyQ2NGzwxnM4MV8C6ziLyhTAP1pjx-Epp-pavA7A4baETlMpX2XLTHg9edyG1ruJ0Oww0co4Se052OtHyJRtc89Igix0WA3pIvIFlaJyTUb4PaUDPPrheBruMLuWq2mgWGL58lVNoWBpq0MTNrx-p5ANQz-IPojOoGUGZjkBM49pCInFLLAFZ6x7G6Ss0eZIxNfGjpX7au3VQY3DoRyvsnp3A4hiVE_huH8AAFnl8-PqC2kRP2wtHCFoECSL_tACv8f_jBcMy1Eu2zCZ5OlX3qGCwBSdwj_qD92cPt5CrX4kwKlOqjY9q7sxYgnKCw9IqFF0GYOg5Osp0OObaLnfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwFz23PsDBuU2b2DVXc2iau0cIKnsAmxvXkwZD41J_JlduU4FdKkJhrMRVcUMYJ2Gt84U4DaB3CG_RNdA_vJukx63DtmLxj2O1nJ8gn2QxANbpbB37wbg6QSujwu43Mo9eCrpUfpZcA-_d-oaKsCuV_OuEzPHtQPQ6ekwyWCwnh0mF89OHDLXmi8cIFfOO4ACuoKJYnFJNhdvCjWV-5p7bUAgf_yoJSH5YaqkMWN2GOr7vfv5XocjIH4nb3b6hVhP6XdYqRNbAIPJeAuXPlTs9xlRvksC13FRflrBuG7tSBkhvvd2ljxDTYIltwAu4ruZB_3RnV3qbBZkYAI7_y-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=K9FW6iSyoxCI9K1tF42ta57IdZsIeH0dCnX9nPcE-1TSbNYM5mMu3O-zKFlsFN-ATPhDLQo4GY25_zCB5FhhY7NhwmFofbAhSZB8VhZZVyXLIMYb-QZFY8pzKYL1Mqi520XVnnVtigqlTPsXm21Mrta3q-EX6NgOMk-VcWYDv0Z-AWhm8Kn0ZYK_4Wk0FAgKf9v-lz5uSCg8fLlOznfE3N0Pj0RCh4uhAMS2aT8nkhhYoLPSBWkxTg0hnrJDEyoYYHOV-ZaawPWs30WZPLtcEfFAxqqhgHbAE0Ii1iXc_1_KlFSqc8OgX5x0D-lKQnRyWmIDJrF6s-mhplzpABQqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=K9FW6iSyoxCI9K1tF42ta57IdZsIeH0dCnX9nPcE-1TSbNYM5mMu3O-zKFlsFN-ATPhDLQo4GY25_zCB5FhhY7NhwmFofbAhSZB8VhZZVyXLIMYb-QZFY8pzKYL1Mqi520XVnnVtigqlTPsXm21Mrta3q-EX6NgOMk-VcWYDv0Z-AWhm8Kn0ZYK_4Wk0FAgKf9v-lz5uSCg8fLlOznfE3N0Pj0RCh4uhAMS2aT8nkhhYoLPSBWkxTg0hnrJDEyoYYHOV-ZaawPWs30WZPLtcEfFAxqqhgHbAE0Ii1iXc_1_KlFSqc8OgX5x0D-lKQnRyWmIDJrF6s-mhplzpABQqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcP-I4Xz4i-8PBOkx7pZIvk_xiAzCqyv_MEuNGwFbfVMQ0DWxNy6yrYZo2XbT1oL5p6Wol9G2BeNXsDXi7H3Yk6aK34OUx_w8z486d9T4SYX4GsnqHWxtnHCqV_yb5AqLzhL0mjl0U4HCeOws-ij5W27yxJ4FnOTKS46gmoepy1sgWHTWy6XJ1hY_DXdr3QeacnFQ6_etSIvpixmBgTIuut_SdnlhEQ5WmaDPySIFl-iquUNRN3mldtW27NSdF9iVIoKbnHa8fen4FgUteDrrxsHL06hsKDn-qH-ijMkGxP2M8Ex0vVqJXgCNkAO-HcMnlzjZ0-o9Ol6oBoeoJNw3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=Qp389irELv9jqsGBzx4a5ySMev8lb-Eb9xheWYYs__mpJzTTXpWBXxGQPXEHGubwCj11HTMQ1QMR7GsYEcHdGDgP0Y9tIggZ-UkCCVnbMEtKKX556EKfE3ay65kejI-R2UitOSJW3w-C6XOrxf5ag2LiTQtsz9OnwOG07gl9GOY2yzBJigRQD5-eHHL3dgGaan_qOCnSjPYAATMVmzcw9YS6puOyw8-IMEPTBA7_Z8HqzK26JJqqHwoF7vJhx0JyhPjTjVT35YVW4WTrQmkUfkUoSWgpP1LC48Qcj6qs1lmXkhpHCjjvMJLUvBw6MLxUB1ZzMJDzqjioHhcXe-NPbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=Qp389irELv9jqsGBzx4a5ySMev8lb-Eb9xheWYYs__mpJzTTXpWBXxGQPXEHGubwCj11HTMQ1QMR7GsYEcHdGDgP0Y9tIggZ-UkCCVnbMEtKKX556EKfE3ay65kejI-R2UitOSJW3w-C6XOrxf5ag2LiTQtsz9OnwOG07gl9GOY2yzBJigRQD5-eHHL3dgGaan_qOCnSjPYAATMVmzcw9YS6puOyw8-IMEPTBA7_Z8HqzK26JJqqHwoF7vJhx0JyhPjTjVT35YVW4WTrQmkUfkUoSWgpP1LC48Qcj6qs1lmXkhpHCjjvMJLUvBw6MLxUB1ZzMJDzqjioHhcXe-NPbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAoYnc0UvUEs2Na36TbzxifZ-7NKiqxJU-8SMy0ZcSF8VDHXm95PLucadNIaWZ_9fz67FG43R8FXqAVd9X7YmDWOPPs7xH2_fiH_U0Z4yEp9dku-7GTjQXDWkQTMR9J3643vW9d-zxc9iGaoOegYmYfpygniu0sfir6D3MH3fVzZMNtp-HH-oRS2RQbov0Yy5x40uAuiAXlwmpkIftP3hiEW8PSQVan7Lwzyq-sRerJIwC7SznOZR_WfTBlvVz5EdS8brZes-Ynya4AUCqWp-JgDCBjNLIDFZ5PvfymaLynTMOMD5OCK5tjr2lC4S0NO7RKtHK44b-3oFLoNbPYlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el6RfOR64ZbTG3B7au06CFVbbpCuSKVK_39IoG83BkZ5dagvGfN2q6Uoq1YDDJ-gkphnvgw0SOlkgFjrqnKKRw9u61Fjo8IOIblMNyfPFifnCUkq05mMWEAmWxVNOnmwAClxyiZT5_TgUQkBeOaIcb_x2rLQ4_6-TpvaFuGlBWaNiZrT-66YzhvgAfo3tF0FbdJ5xY2CqhwfLBWfkON0Tambb9CWpnn0eqnDBT0EjC611UpfAGbQqvmJUB2MBT_gTSmL0ZPIhOOlEjcj6LIvr3jEwbANHiFy2r6GKnveo9Xo-qO1_fbooiwE9mPVpDavGtttjmsfwSqQ8iiQ8NAD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw91nPAYQxy-f46ZfWM_kutv34btPRgm3CvRUfbPWsMOv6oDUW5vZR9ftWO4GvaPgMvx_ttSzJynKFqo9PyWSKwBDRCtrEA9v88ywA7PTelkuVoSC78QdC_OmS5v6gCEzGPIMz_pHXdHvQPlWHBlpWhlnyPjZaC13E0vFTij--7KP0s-ad1f98rL-koQYCeFrL1Zm4OZ_Ol4fuK5UPCz6XnQmz1EhZ5UNrtl3vU2pJFbSxr9bITcic2Ub5-2x6IU2z_cXYlHV4t82dppVyhv_1d5ze63iZlpjK6qdLO01kqWSLpV8wssuKmrUO28uU8wpo95AN0QT-_5OG8p8YNKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22606" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_qcilu6IiDJfu6NYkWhGdCqlrfa8rBX6Dt5OjOF6UVziDYC6rvZ2rgN0LAh2qNHn8ohPuPFYDKxwzkqp4Ye-jiVgTH9CKnJATRcTrSpmykN3BUdKhV4GRVoqq_TrlM8Ticp8R0UTNRWUwTGdU1__WZ0QBRkcclXPYRzRtZz4749gu3qVMRYiS83Lvdb7Ku1NV_5MO4xUaFjXiTd-RTBBga2Iej6aGNeRARHfTl8BFySa-i0vFLgKWPehxfl__Zza36vegMmZjlLabrxQ0blxQLrHD1EMn-Cxs6e8b9kIVgTOxnyXLMmNjcZB_aaq6SU_L60Oi4WxFJY-cg8I3YPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارکینیوش کاپیتانPSG با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22605" target="_blank">📅 15:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2yBOCn4xdoHM2LPSxAHXsZENn7znB6jnx3pQ7LwY9yLZb2bzpmNdI1GAEQetaL62EIM7gt7Hmy0e3Tu0Y1M-hy8hqReQTlN66N-TjhK4el8uv09_dic3BaJ-n1ShbqZZhUdf_k15vZEfS4b--cWmn18zNu1AOnQgOKCZiMxQ3xKU-5-PU8YNjdS70o-sQcNhKbn-HdkSnmx-aABG1ZpL03-BC_nBEMTpDW_jiBlXvVSYK6vOygT_Rgc_UFLqgwouPKL_Bgccg0sxUz2OAKsVUVbwfLVVucNlpu7SBeMT_BkBhugENjFVFnCN7F7CAo_ZzsutZwV1qIwsaWjPUaiLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آنسو فاتی ستاره22ساله‌موناکو تاقبل‌از شروع هشتم؛ با 5 گل در صدر بهترین گلزنان لوشامپیونه قرار داره. فاتی در پایان فصل به بارسا برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22604" target="_blank">📅 15:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlJ8DPGkcqCpTvUaF6JOME4v5hfH_najZO2EGBG1dgeQqGC8OFqLgoQt6aKIaDfGN4cCP3iwjYoo82sdeRGanVuOp29jMKqO_-eXzLQUyGaZ6IGwl3xpQWoZJTeVpFzyFmTnNdEN54IlndLWqI-l6SaL1jUpaB_9J5k4wwG_y42ItHGYNx7jjKoIxNwkLDQMjnIyUjbvfbrrLHA-o88yIhvp9muoiPAjHkhH0SFJ72pFea4walxqbjkAYxL0bJNen1yLLok1mAS_bwfKYX_KaofsSgNno6i3OxRdf9tzVGJrTDxRxR9YuEyf6PquivGl0sNKSJuEgavl8B6l1MPAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22603" target="_blank">📅 14:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvxEPDErQXf9ot4S-t7KdTcvEnlb1lLuI0mPQdJh5uF_jHXGRzwvXkOKabNkfqXZxcTH-SgGc4t0Yc95XqrpRPhEI8jhQB7dXHasQHQvx-ujKkypiF_sBz3HsCmr816qFMlStYy5eQmVta5vdFMzNtlnVXKc4b1E6EDRqiD9CchfKJwlfXyKBxQz2EdSi03mhOt2AJiVBpSKAwuhPrywM0o0vuwY5ZQY3v4zMIaVKisObE1RIB7UqaY988ptsc801rG72W3CPpUAEImzZ84hCDoN2IlrHYJNVayqC5HCVdjjEsv_Bx5qnShznlL1omlADjfxu_-Nc57J_9Wu48JgUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هرکی‌بهتون گفت که چرا اینقدر به فوتبال علاقه داری؟ چیش به تومیرسه این ویدیو رو براش بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22602" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKi-IZv_Dw7K8qMOYHNgsfmNYi2yU9tMOBohwCHpgIGpcFMkZSqJitNngjKH5semctVqUx0rNWU118355XMPistOmKqxGSQRODuwrq78yw3EMkVp4Q-xhMe5VSecWJfeWATe1I4LyUEjLwawHs850NQWSxDdypH-MOKz2Nad0wBtss4cgxgKtlgAkekezUn0BhmfXR7DbsTsiYoSWMzQSdTFzrjx9A6cTMIXsFWdqh1NsT1UW46BDPDmsHM8RhBriU74Z1I40ANLzi1LEp94zqDfOeVViS73g_9kGCBXrRj9S5N4uijAm7n0Kp7yEm0LvH-nRfnZGcmZ7LW7DmAUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
کوارتسخلیا
: بازیکنان‌تیم‌آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بد ترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خیلی خوبی بهشون دادیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22601" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=n1Koc3WzeAYJtaoXGytW2Se0GmfqFMlX5m_wK7LYlHhp_s26CXWxOWrpFMeGhwYIUyN20YxnkgSNmlS5coNrvSpMG1cjFu_O9I4jJtBGsrNp07FEwPercAB5HH1SrjUcOkPzKW9fzFPpzx4J9HHxqzhClcnwyXYfDoP6kw9T7wONdwR6bMuYXh_H46thbcyFNlTcp5DB3TtIHoV4DoachwBCTFOR_DUg6DOaqL6BUddVpiaq9tWuidgaamCywpCDe-ZRGuMZFjaRSdbCvxfx4ieUHyFXRGuA-xRDMHxedzeDNlQQmauDtHa_GTJ3GwX6WZa5G2z5md3e7_wcVw-eGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=n1Koc3WzeAYJtaoXGytW2Se0GmfqFMlX5m_wK7LYlHhp_s26CXWxOWrpFMeGhwYIUyN20YxnkgSNmlS5coNrvSpMG1cjFu_O9I4jJtBGsrNp07FEwPercAB5HH1SrjUcOkPzKW9fzFPpzx4J9HHxqzhClcnwyXYfDoP6kw9T7wONdwR6bMuYXh_H46thbcyFNlTcp5DB3TtIHoV4DoachwBCTFOR_DUg6DOaqL6BUddVpiaq9tWuidgaamCywpCDe-ZRGuMZFjaRSdbCvxfx4ieUHyFXRGuA-xRDMHxedzeDNlQQmauDtHa_GTJ3GwX6WZa5G2z5md3e7_wcVw-eGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
اکسپوزیتو زید جدیدکیلیان‌امباپه ستاره تیم رئال درحال قر دادن در کنسرت روز گذشته بدبانی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22600" target="_blank">📅 13:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ab989954.mp4?token=dedXDETubxCaZ63lVaORwDlEPsNdmaicB1m0fHllQIJgx7eAD8wkdYozJHPX56m2UAtN1Emz_LyEgFVKkormX4sdnk1r2vweCjoWPv_kb43GQC7BmiU7rkQdY--5UTsZlboRaId5hd8U8Tjjo73K9hek_GOXs6fR7K0DSXJTBlNkTTFV-7JGrLlRcXcSIiTiHHgcup_ksNyABC_kEQXKrxvaqxQt6YkfjJHvdJF_oXXQ435y0V0WxPPTtUOQ_hDw-CecnUt7uCixij5MhdWAfjymw5PPLYOQf6s9Nr1qKgHm_swundGs2AtJIWkTdbPLTFCxkUc5-o2-dxlHuo7-1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ab989954.mp4?token=dedXDETubxCaZ63lVaORwDlEPsNdmaicB1m0fHllQIJgx7eAD8wkdYozJHPX56m2UAtN1Emz_LyEgFVKkormX4sdnk1r2vweCjoWPv_kb43GQC7BmiU7rkQdY--5UTsZlboRaId5hd8U8Tjjo73K9hek_GOXs6fR7K0DSXJTBlNkTTFV-7JGrLlRcXcSIiTiHHgcup_ksNyABC_kEQXKrxvaqxQt6YkfjJHvdJF_oXXQ435y0V0WxPPTtUOQ_hDw-CecnUt7uCixij5MhdWAfjymw5PPLYOQf6s9Nr1qKgHm_swundGs2AtJIWkTdbPLTFCxkUc5-o2-dxlHuo7-1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22599" target="_blank">📅 13:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7D3lrgA5KfojK9jDLGJmDP7JQvFLr59eVp2071AN1kjszA6vIVKOAEclJ-xI1e2AZJpr6B-xdqNf_pT-gbx_KFD-Vd_sdTTGlI2T35cN__O1DFPT7iJ16JcpdCKeIJBTDOGgM2_Ukrn95pbB3PKZpyAjmfi3FhpAQ0mbb9P05DwE5-jh7ktdzId9KT2qNewZyEugSyGdc22x1AtbRcOfwbB3vsoNCSPFyLZq12e7OM3VBLlsidPEosWWTb9jbZeQEgngz5ouLs4lAMqJ1NbF58LYfUnJyfvyIttxW9OmDrW1xt7mnIrxKzSlws30FWKMvecs_mfVd7222c_S4svrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22598" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=QtoLtR0Mm0pN83MLtWGd6lu4XgCuA-8JrlYZSkEj5FClSWpcYwiQOoleZ0Ym1wAzS6t9EpCtelFzR3x4biyg1B3KinWf8A-UmoYRhlALx0-mEMta-C-BEuOMJPw-19I4BJ4MelzqK9RZuTkp3redOUmuJT_U-TgbSxjU75N1oWPyy-VqMEekFl78MpCwW-GQQCuaIV89FY2vENIHv-W-eBcOVUVHjFMkxirxXgYEgH9l-O2ASsvNPNt_qNAa46VzcqhHge_ZbOM0OjHyJlcs1wsCaMPAHTAo3NRkyYWzMdP9zm1Oq5uS25X3FiQO3iFfM3083DQ0asGiRxyREn9SMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3a620208.mp4?token=QtoLtR0Mm0pN83MLtWGd6lu4XgCuA-8JrlYZSkEj5FClSWpcYwiQOoleZ0Ym1wAzS6t9EpCtelFzR3x4biyg1B3KinWf8A-UmoYRhlALx0-mEMta-C-BEuOMJPw-19I4BJ4MelzqK9RZuTkp3redOUmuJT_U-TgbSxjU75N1oWPyy-VqMEekFl78MpCwW-GQQCuaIV89FY2vENIHv-W-eBcOVUVHjFMkxirxXgYEgH9l-O2ASsvNPNt_qNAa46VzcqhHge_ZbOM0OjHyJlcs1wsCaMPAHTAo3NRkyYWzMdP9zm1Oq5uS25X3FiQO3iFfM3083DQ0asGiRxyREn9SMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه وقتی‌میبینه که با خوب بازی کردن در جام‌جهانی و قهرمانی‌فرانسه به عثمان دمبله توی گرفتن دومین‌توپ‌طلا قطعی‌اش کمک میکنه
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22597" target="_blank">📅 12:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plf-9mkDccOJ_iqYb0sG2k8QuNfHDRvqtJifZ12mkmoWLH8C8urkloN5ukJr2bUs0AskZY-4uagOo7-o970nj93JOSoVLyVufCy9LHab84Vxc2WvQ4NjZgdZbtZC7U_5strOQB2oMV3dxzpv8f_LPaPlV4aLcXyYorjZYM-pJaSVN8IlftDtfs7iZtH6RBr4k5B7jeX0e0wQ8oe5iGXdparxd8BGL8cBWAhRfL1AvnX72ohA_skP9kg1kuDYDIOW85RvLGHL1KjoufJiBoRx86If7dOZUURLDIReUnKFpoo8nxhZaWfECyyOLcQQDjJoYd5mmRuiRzVcF0ZPtEpbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22596" target="_blank">📅 12:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMAqU42MPx5UgGTUlalbptoRDwG-M5_LWFFUxnhQafoxDPAJw0iLGMS2nQzm7bhfAABZ5FGIYylm0bUiKe9zRH2VLRgGn1j5kbdeQX8thSlBja-RN8k4mgK1hkkd9GfRTRtN_curcLSNkYQZDC00s_xyquS_6cfXKBRu5XydV3csTWUmG4CUDdjR-4WMAJtJ6qwa9rMJ8w7rvsZxz-SnSdybLy_TQJnSdPHTHlsb-6WvtK6JCck_2hLAjxfzeZ_nOSbtgjOHmManmcWaaNbCFa8J5xD9O_d40nW5pI-YKEop8I890hlTfRw4dvep2xVYVmzg0QbtDA9HGZ1hZzuERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22595" target="_blank">📅 11:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=Ryh4RaqF7aAZIXfoNNdJMYp5kKx9bZ93BqTi9S9WiUSLOy6CBenZeVeGiEtU88OdJqDamKKBCtVyrIARn3YSlX_MHb1fkmQnpawHYGsqncCOE2Q9bdRBm9rkw8z6RpTO6eC0YgaMv7R8CEmS0fHZSDsv1y1Mph3YkRooLVss2wk1xoFIiFNeAhHFcXxvtyaTKHKvwTa2Y7FlUeB3UkpoutD8A5SVpdP5tBbmQPC4hSiXKyHho7xvrOBMNVgBg64hQdzvpGCyDaYK3zbMB-2IuUSrApeaKoGRLe-xehqvGx8T-UxG_HIILNF8bDdvPsxhW1fY4HDjtJhZkNefl44BwSGnQbESO3GLidmsAc9jb0rId4V4FvAXcy7f8CKlD7GwVxblySzj1KWzZA9gS4vmpkW7fzlS4jspRYB9BCDsNuh_nn05tpxzjnV69ZiVzc3pEDz1kvrOAnIfpch8feQBc1UBjS4KDnkr2zB0EhP325k7dIUVEifYiLNRLf463jovD1qGOH3YHXakI5ixVh5UOEXkD8xX6tewDUa4-XDsQstJULfgm61Yk6hqIH5uYMZNTAwId0Q8xoIm_ROYDMQ2xCM8iD_d_iWtzslo2zhxeQP8kyMWij4mlfvftRIVIml3M2rGc8DuEkkBN0NQ2DMsssnM7zynVZssGGNpdBF94IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238aa793a.mp4?token=Ryh4RaqF7aAZIXfoNNdJMYp5kKx9bZ93BqTi9S9WiUSLOy6CBenZeVeGiEtU88OdJqDamKKBCtVyrIARn3YSlX_MHb1fkmQnpawHYGsqncCOE2Q9bdRBm9rkw8z6RpTO6eC0YgaMv7R8CEmS0fHZSDsv1y1Mph3YkRooLVss2wk1xoFIiFNeAhHFcXxvtyaTKHKvwTa2Y7FlUeB3UkpoutD8A5SVpdP5tBbmQPC4hSiXKyHho7xvrOBMNVgBg64hQdzvpGCyDaYK3zbMB-2IuUSrApeaKoGRLe-xehqvGx8T-UxG_HIILNF8bDdvPsxhW1fY4HDjtJhZkNefl44BwSGnQbESO3GLidmsAc9jb0rId4V4FvAXcy7f8CKlD7GwVxblySzj1KWzZA9gS4vmpkW7fzlS4jspRYB9BCDsNuh_nn05tpxzjnV69ZiVzc3pEDz1kvrOAnIfpch8feQBc1UBjS4KDnkr2zB0EhP325k7dIUVEifYiLNRLf463jovD1qGOH3YHXakI5ixVh5UOEXkD8xX6tewDUa4-XDsQstJULfgm61Yk6hqIH5uYMZNTAwId0Q8xoIm_ROYDMQ2xCM8iD_d_iWtzslo2zhxeQP8kyMWij4mlfvftRIVIml3M2rGc8DuEkkBN0NQ2DMsssnM7zynVZssGGNpdBF94IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قشنگ ترین توضیح درخصوص بازی تخته و این زندگی؛ واقعا هم همینطوره. عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22594" target="_blank">📅 11:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fogZfnUIPa14d6ZnJQGiCwPuT6P_gNOD_UeV_3HE0d19LBvtDPdxAHLhBLGkQBz22sCPzMCyOzDXPf1QKyD4R0M472QWwjRzsbyc92AP6vXlXe2vIQAen-xbzMYrstiGXCg9Yb4kari7xvASdVxz-Mjd5cuX9eDCC_WVJdq-3Vn8QMRb0woANrzVop5zJPe1GSXo4DbnQzMepefA5KxVXc0jGNGsN0Ec8DsltBEtvqOZx_I3_o2PwsdbhdW8ICAQjQRontnwgc9OQmuHkTf6EJFJadK8wn9YNDKzs27wVAJ8fOyg-cgoWqAyCOUgXDK7L-Q7zbl-xu5QD2gGbJcsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22593" target="_blank">📅 11:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkJ73XpQFcinEPChi32cBtXd3uywTtetqbkxKd3AQTBDDrRBSH0nOKbiS9m5Usg2h2tEuLNgTguVhofTnd75Bf1yMQGwxSKRhKaeyAf8BHj1dbMwsvvQth__zQ13k_c81zwRqJNBbHXuiYOk55mf8eMUkJ02tRM-wxVv-Fet47_VYHRg9xw6-PAaly_TUcHZkX9RcuUoe6cLm6fWkLV-26SDhx0cuZfiRpT02yWEWdZAX_9mw48uIKrBHiM5P_dA0s3eBvAGYpy1Ep4J06wWn0WdrP1vvgQrwh5GcOE-v-bVbMvg8HlHPb0EkjChxgtrwXmEyGp-i1-5CLUxzUcf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های حاضر در مرحله یک چهارم نهایی رقابت های جام حذفی؛ تراکتور تبریز نیز حدف شد!
✅
استقلال، فولاد، شمس آذر قزوین، ملوان انزلی، خیبر، پیکان، سایپا،گلگهر؛قرعه‌کشی‌این مرحله بزودی انجام میشه و بازی‌هااواخر اسفند برگزار خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22592" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3bWQPSvYJYE2VhS3LSo1fgxgZG886UDJDhlrFQrMxSOcFvk7w6GoGTKbYFh4I9OEvn16bJJ6YpOfqBWmKN5NjWIt37z5aeh8p4-uNq7bXhvU8g-pJKs95rhuiRQDUUAPQ30oAsvwXfhk5yu1_OZfvRkFjnsu9mWZKYVrNMZ_v3UCWE024-r9qmN6u99GvrR5-zlBH4yvZ2DgqiaN1qy3LaBTDHleFn14-Sh2iiGx_0L--haou6kpEiu4GnJtnl66zpHN6xG1GGf2_eEFzaIPvMjv-ToI_SGJwLoH6CF3frDbVMumA50N8Kwn0Mg9dyW4eyhjoLnrqB1KExE71egfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد صلاح فوق ستاره سابق لیورپول از طریق نماینده خود به عربستانی‌ها گفته هر باشگاهی به من دستمزد سالانه میده، قرارداد 3 ساله میبنده و تیمش روبرای قهرمانی میبنده من اوکیم که به آن‌ تیم بروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22591" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVXPMrffq24tpQ0mx0mCEn4OWXwCEMhDp-SvFw_9rpAH9heO4i8YVwW5Ytx-ik2N6HGXL5QTKMfRAstnaTj1GHrS21QDtLg3H8DMZbpjus4InKS78sDL3BEkSeJzp7L9wHEV-AB28ItyeWR3HYreFIrpn1IYFA3UdzcMWsmkO7QJcY9AQwOCsSiDMIOO6GUcW-oPhRNenUwsFZ-NM7fjdbXytfqAbGACDKFAooymWJGuIZJFGhrHOIJ72-T-ZjDPm54HwYC3ot2ZcID3zk2RxbJzFW6MQ3B1wVys2OM3dKX4Ej3maFvDVAgGtaxvYHdZAtPx0hW1PH-Jnqxm42y0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|رسانه‌ های معتبر فرانسوی خبر از احتمال مذاکرات‌باشگاه رئال مادرید با ژائو نوس ستاره پرتغالی تیم PSG در روزهای اینده میدهند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22589" target="_blank">📅 10:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GySKxy6MZtEn3JwIte8iEZDTLXDreiCYlbHEQ0YoxS_pY1mz1x83WytrThqrnSBp_BiZbOrOX_9iqBKh-9a-H4y8XHnlzt006J2-1R9neFYetPX--ykYmu8Q3eVQy51YWRqZXK0TkFVuVKu95voYkz5hLx34j9PC-ixdSRZwi-b4tvejNgPETkxcuRodFbQClJbIJ1jSdZrRkxEPyIWv9KNtYPq0kTRMGeiqS9uDGsULfBXti3LxcpS2VMPi6lmFO9YMSC87iKMntqVJ9VPem4vsd5vLvGL4XijJwO1B7S8CbhMkuEkC_AArooRsSQER-MctJNKc_YgHu_ejlMQA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی فرعون مصر با هواداران لیورپول با چشمانی اشک‌ بار؛ محمد صلاح فوق ستاره مصری لیورپول بعد از انجام 442 بازی برای این‌تیم بالاخره از جمع لک لک‌ها جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22588" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=XNuLcXafDvg_POilqX6gOH-Aevh9i6Zr3TllkuWqBfAVhVoScAlJRX0XDafHRnWR-6aEn6EzRQwV04dYM3nsARiq4jZsQAYk6dClXPubUdI68dBl-IoVnksVO_55uEqsBMjO2zzaZtYaNi4nkebLWoyx2DDagiiXKsF8jrcW3F1cLzOwuXWdeaVG9yiyHi4O22gvMKDvO8aQnkufO52Hr5PWww4o5r3gXDBU90XxYUzJtb0KjUiy-CzzFTKHKsGKq4oOTNMAl5Tm4Ujay-CwFzaxg76SqFySl93Jr4Zxzo6hbeI2LJ0O1ogarNNBdCLK7VTg-iuz3YZ9sy9gz5u8gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=XNuLcXafDvg_POilqX6gOH-Aevh9i6Zr3TllkuWqBfAVhVoScAlJRX0XDafHRnWR-6aEn6EzRQwV04dYM3nsARiq4jZsQAYk6dClXPubUdI68dBl-IoVnksVO_55uEqsBMjO2zzaZtYaNi4nkebLWoyx2DDagiiXKsF8jrcW3F1cLzOwuXWdeaVG9yiyHi4O22gvMKDvO8aQnkufO52Hr5PWww4o5r3gXDBU90XxYUzJtb0KjUiy-CzzFTKHKsGKq4oOTNMAl5Tm4Ujay-CwFzaxg76SqFySl93Jr4Zxzo6hbeI2LJ0O1ogarNNBdCLK7VTg-iuz3YZ9sy9gz5u8gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به باسن هینکاپیه‌پرداختن؛بن‌وایت میکروفن‌گرفته دست داره اهنگ میخونه هینکااااپیه
🍑
تو نشونمون بده
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22587" target="_blank">📅 09:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imfJg2EkpretWFwxnd0eShNSa7XCPx3-XZrEKN39zp9UpHbIoCKKDLM8ebmfLdmT4AZLGB89pZDlUQZ964dV_kSj3VfOO3dp9pW3ciRhjrMxWTOZuhMVuYFuDsFvxjjPEkvP7K6KZ-vXhXbISzmHEAiwEiBo0dDj5CBw3zYzq7oSldiC1KX81UH52BTXN1Agv0FNbYNNdRhKLUq_Q0mXRuu6nVokbb6YhL2MEUJLMOk4s0UAm9G929jTuEUd-N8NK-GhLQJxJudJP6s28y2xqI_shzJG8i-hcj2Os8aArbPDX8EucoaAwIBs6hMvv0C9zAv9Q1_N_nzQxAZBj5O-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛ از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال  بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22585" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=PnVI5nCl8N7AOTKG6W6WPjsdt-NfimtPjAwB9VLnjHkkyVtjMEIfH8hLHMXg_lra_qMfM4i3WQCsowO8B_V1cP673r8Q8kZL4_B1ijZ3twzsmB_e7XpaSeA6FzU0l8ncDQWlZg4w1r10ADUIjb914sEnoP9H4w3zIcftDrCcwx1UtQCbO839UASgTlwdM5ACi9RQF2jV15UmwRD9jpim-exa98aR-qLE15JC5ikS53MBQFXszvsOHlwhYOoYbK0Vt9YQb6WtGWIMr5UhU3ILaIrtVGYHL1xJjGKHRkCCdF5k_dX8jaWkFLf4Y8KNkfVbFf-yfK2lhZxc6ney1-Hj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9282b8e98b.mp4?token=PnVI5nCl8N7AOTKG6W6WPjsdt-NfimtPjAwB9VLnjHkkyVtjMEIfH8hLHMXg_lra_qMfM4i3WQCsowO8B_V1cP673r8Q8kZL4_B1ijZ3twzsmB_e7XpaSeA6FzU0l8ncDQWlZg4w1r10ADUIjb914sEnoP9H4w3zIcftDrCcwx1UtQCbO839UASgTlwdM5ACi9RQF2jV15UmwRD9jpim-exa98aR-qLE15JC5ikS53MBQFXszvsOHlwhYOoYbK0Vt9YQb6WtGWIMr5UhU3ILaIrtVGYHL1xJjGKHRkCCdF5k_dX8jaWkFLf4Y8KNkfVbFf-yfK2lhZxc6ney1-Hj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌ کنیم از این ویدیو پارسال؛ میکا ریچاردز به‌مارکینیوش‌میگه‌میتونم مدالتو لمس کنم؟ هانری هم میپره وسط و میگه بخاطر اینه تاحالا بدستش نیاورده؛ مارکینیوش هم میگه منم مثل تو بودم
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22584" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH5DnRWdfgKPRf8n9HL7Jcuu289cGYBjp3YMy6G59ovxmxHvq3cshAYPWjVXYcYT4g_M_pQq6KuZ-c-XcFT-UL5NuyoVAGuNpoQC0lLUvSovVKy1frE1OGNiIsNqVpPAkcpFF2stVuN0ocwCjvzb0t9RORRv6g_Wj9WBWjViZSpG4l68MADJY1zQOoKK8meu4CnM8x_0kWrt08hZqHwKuFX5xNbqHnB9YsiPK3_jChGqTsf_xTqsyExn-Z0pcRyBarLG_nqC87BHr4eL8uH4h5kyi-Z00AOFUGh-JOGD7KCbHqocDPI1Yw2hghH4Prw-C94kFXDy409BQrqHQQ-8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از جدال یاران هالند برابر سوئد تا تقابل ازبک‌ها با میزبان جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22582" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8utmnvIEEx6mfonI6PkdqaI8-7UO1pqzAtynp5PCjm1_9vIW-kOOWWArnNOpvEPJlYs-WU42X0mjNwA1a8WltmZUVU_eXcQHpFWJE3SRgBW8Vyt3pZV1YRzvMjXvOJL7c2PclpOsocqfo2sAv5vTDltrOjDZrfpKAVdyy7QuPPFPpN84-kOxe5urJot1mE9T7KZxpi8tsNxr6RMvyYveYodFKPoRziSlLCMJ90JOl9VRDGCx6RUw1HTqjgylpRSlzcxyxRpfPWgtEz747t1R3ewg2wnY95MpnBcH5tkbE9GApRyWGBbPocsFqKDkN7qjKnce4718VU9nFO-l_ua4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار‌های دیروز؛
از برد قاطع مانشافت برابر فنلاند تا برتری آمریکایی‌ها مقابل سنگال
بازی شاگردای آنجلوتی مقابل پاناما هم تا پایان نیمه‌اول با نتیجه 2-1 به سود سلسائو در جریانه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22581" target="_blank">📅 01:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YL1dN8wIGUwbGfuLA6ErLpwI2Qj4q0COAJ2pZYoZ6hmszrinJ9s--43_CzchifmOIoEcU6laIjQ8eXkw9uomsaMe7G0q-PSCsdH7LOgdl7UMxfklUQ_JxJ1HAj5bH7wCBLe3aLzSsh-0KvbyJRiKRHquV2ou27-tYtFYy80uemRdYjRMR-nvVGH4oc_RqBOBu6_90b2iDQkxsKuhfo_DpFYl5Erh4B1QptJXjMp-67_667-2DhSe1ERwOvFzSDNeoFIK3YOtdHuwsnMiiTf19ZGuD4fuakUDNLGZbTG1THp1an-4hAO4nI73un_z6XokFxyIdyRqJM7f-jBAuJGIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkPlMR6IMgeemhPY2hxuDIfogjazyuVCFtCJ80SfnRpIm4jSHegsb5aj-WPaz25QH49P-BFUpEssaGE_XMEeKYsqPMqY-cLKlFs21sIu3RWUjHZn-Z3UHE0hRWKTe5l7fAbr2HTE7qVGrok6UNYm6vhgZFUmLpYLU3eAGbjaruw4VvLuIWyyZDyvdqwroUCgEIV2h0UjDXk_PrNaVQWSuyeku_RqC6-JtEd8Am5QIDf1GQuWCdKQBngvnRzJEEFwEqYVHemMHqWmGti_PRyU4eNLz82eKDRH-I2_B7-LDkp1f58qVPCTC7u1jjAddRnJMmaPB0sYLKUydSAIJvRBtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
مری‌راک مدل اونلی‌فنز قبل بازی فینال لیگ قهرمانان به سافونوف وعده یک «شب پرشور» به ازای هر سیو رو داد. همسر سافونوف که از این موضوع مطلع شده بود گفت: شوهرم اصلاً نمیدونه که «شب پرشور» چیه. برای اون شور و هیجان یعنی حل کردن پازل، تماشای مسابقه تلویزیونی‌وخوابیدن‌راس‌ساعت ۱۱:۳۰ شب چون صبح باید بره‌سرتمرین؛ بخاطر سبک بازی آرتتا، سافونوف در طول ۱۲۰ دقیقه سیوی نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22579" target="_blank">📅 00:50 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
