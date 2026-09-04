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
<img src="https://cdn4.telesco.pe/file/eAMM251mj5LMAALZBfm-wmOw5is_4zCHZ1PNoWF-c-vVXgcL7FJK2TqZsp3wldmUyXvwNe9fHe667qRniCRH0Ns69WmXEz68RSt0tlg85qSFf0InW7UAs_HNIBHijI4QUZND3Ge12EGgrnzoPyRKoqyuFmQlfb4xNXwsBnO6CPi_BaWB8IIgAJ_S9amNxPRajwh746A5l1ytvsgf0CQ55t_wq5XoMAzFP1MOPWOQYjOeaKVr8H6yyImwF-60byhiYU2M2sRUECAZp0LjoaUZFYVdQNwosPnnbDja3u1yOtN3BQYxaxQfF5HAwYIJTD-RvsaXUayztZfjB5i3wn8Qig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 610K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY7IlKPtSdQNmr_J9trOT__ZqZvFa54XR453mFz7HEE2FWOExq7uQOsW3OTYU9dEOP34o6OM-1ZCAYsoaOZu7Ew2KqFBqwgA4eYpSCHTA9-WyG40bLPPhY-tYXdNIzbb8-xGdx6h1hvCFRCxf3vU13HNS8QLQfhnnPwg6ceH0rWl4V70IjtsN0UJQ9X8w1jz7A0mnQpVgD2L_qx6o3jw0jlTxOb4k1tD1XFnJjz5EuRBRcM51h5WWC3xs0apMEBPdpWIScrJRzBqAPXA-ELA51L9taamX1VuBlb4r-pEbW9uzm4xgMAMDsR4dmGexpHL4yakKjaNlbLWXkxoN7KDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D01OmTvvurkuwYCpvZQPbOb_Te7yJ1ytlda0HOa6PJUqzoQqdQQypl9ITAD8J8X_TFi9s6KAmrFtT5kvQZquf132ZJWXTnpckm9HM_UhegQMfmmGx_roIvnn3ZD3akX9EhIZ2Mlj_TcdHnLJ8QlbHxVWVxesXBrYYNys1uylAR1EmFe9ettmwoVFwAvccmL9YkFB1MVgm2nnQbzvybwuUnQJV89KJa1uoNmm_idv_iAb_sCAIWS0AZuELejs0lOsIAd7OMuZVMSeUlP7wRJY81HR8pI2a4ymFzLZLrOviV_ZNYC1KBnbcRXWXOnEJZs4VxKLnGtLNwb9K0CqzAZT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlgsVPOew2D8smBbRzNvSFqLo-gmYL6U8Q4C0rMGLJ36YHVLjSaCVBsatkTPRsBy1OvuRqzmcJiDsRsvTjnSC56xLtM9_vCZXiKQyiu_e9IvAR15LAMzerTK9MvsVcYMbN43_WaZjZZEa6NQYTk_PR1aN1ZJepcOe2zelVy1Y_QTPMehpv_ICOV0nTOldjJcjQLZW34LPudWbQNq3c9sId1CcsGDO9easfhsZLgBmylCHYz5qGJRcrviGAeis3TbCDM6HK9R9_KufvDj9hBUDhkBm88ULDr3Dh_BMnuxXQJ_KMkLiF9LmNxRDLyeirWya-TlWpDJai9i_kE3uEl0lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2OY8s2DwI6iyJsKFMbUe26xN5nQKUm-ZCyhjqY0jQlHO-NjJzcxYlyyaP_rP3c031tFCIY4dRWq3O8p3WPTrEwWeH2vUxOFvKWjGyHAY063bRGrwIjGSamAApJ--_zccqQ74aGSNV81IB5sre_B7CFaVji5bdoGT30oOYJjVlXAmpJSYZWcTDxaYVqRWIPTZu-DSCICkeiISTFxpZthf-dJVlS_GXIzQO-X6PsyN-KHkzcuxsE3QhxDQFy-iLB8anyYAyGcu1b_foO54c49B2NP11ZxwVQOGdrqI5rYpNnvO8bS-xDA4OJyHboPKQ1I23awlNue_I9fqWgvjGuQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29052">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=Y4A6UeEOXoIyEyWBkcqLI_GrmQnX6rpm2-AjjLFOMrk2KW7LwkmPS6_i7kFR8RJ0hSpd2FRfOwkG_96vlaPI68D8o4lBQQmf9ihlYAyUeM0iT-KUxk9at60OBslDSx_21Af0iBfinBnrHhIls--GGQqarF3aTbjzSbRVFGN-qFz1UJcLGLBqmxAMo-e5LYNkmfUhEXCNg0oZnQNe7HHqYS0fPYss5fBOolearWoADYMfEgl2yi-cSKnMAMzH1qCbFBMsQGtPl0PN3rBliYR1aREYDTHYJ6knXpm0ulFxDE8z3wOt36Nry969Tq52Wc3M_NGIbnIBWzlT6Lojs_rfrKraWgyOb6hT8HneA4BoQFIw7y_p5qFhaSA58X1K6qV3tm7HJ8V11Suw97Qd4zcS24R4Wdu-fsdnITb2jmiyzHTMaItGEkfJORksiG2h0DFSJ0kZrhz0avGEKbHJRgJ3oPsjA7JqydvpnYjlDdaCUSPjMoMpdrdJLaq7NDtqns81QRyrqMurieQFr3sY8nugIDGux04trLHk87jDd5c6RZ8Gm2kVXsUZqfOMNLJV9cutZpToLDGQiov3uqTjikgVwJLpqy_-uTwGXClVN7LTJYGzKYLZu2ltpymKmKMURnLgSHGxWjUjbs5JpQ95hPEWYmWHfI1P7RAldMDAJcpGtCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#فکت
؛
رودی‌ژستد،کوین‌یامگا و یاسر آسانی سه بازیکن‌خارجی‌تاریخ‌باشگاه‌هستن که در شهرآورد های پایتخت موفق به گلزنی شده‌اند. جالبه هر سه تاشون با گلزنی مانع باخت تیمشون شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/29052" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29051">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=XxvkLKM3UQPYDnPJjFHtUzC-7n_biSIO5-I2jk51Oe0lrX0POCBB_XzMzfGBbRrvTsseLWSp-8PB6KYurBTlAZ66ckDCNChsbNnay6mvXHz3GOYy0APr2UeGoTp2APTRAHT3ew-teOYf46vxIljG1HuTx_anGvQdJtRJgy6WuwHEXher3FQ66dgd_RZse6-_xNnbfB0yfK-62kt3S6sGWhArSZ6jEFD8bWc9qg-wEUh-iZBMWF29eFiBqGydXM1duVl__0qgGOWIoZq8h7HiK1TSWn6OqcmyWYuvm7r1A3N6HHgVijTrgcXAu7czXyVNfl41puvHe80qLcwGmNaVyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/29051" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29050">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4yGZSslhzedIsa-94Jf3CHIvtXnaG8EZMTRkAj2tp2j_CS5bwpXSe8_I5vA9NE8Jb7ELPnsTtj1l3HwpOpOFRCvqpWrJUxk6h-GveOWMOKItlgkunKJFFdGIU_QiXSAAQJK9vwyxjpaXedwKRLjFgIRVyXdEhnZCY8DaLYkTOCbR1GLxrs6rs9vDmfBdLLOUNAzRw8nfh2wVwyLwUqGC_4ivhl5dAJsLyKKonlvf_3vn0VCx2ZXJN7NNHiKjgrkoJsvB1wST5NSDMl3P5itbFMl4EKZ4hJX4pMo3hHYV84BK6APVSL_EfWB2gKZHhJlyeIlR0PdlhuejI5Bh1R--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
پاری سن ژرمن
🆚
موناکو
🇫🇷
⏰
ساعت ۲۲:۳۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/29050" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29049">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDfjRQ5rSZ58Nq4qLb9oytctivx37WM9Vpn3QIOaUZ2QcXpiDh9ZBqJwpxXgZz43MTht-SgoFkoTHMFBJVjuS-Q0nCSrjJ1SiqcbqM7usESJ3LuVnyNq5TO5dVwtv4jbArAjlcTyS10p8cbtWSjNV5ME8Gc9SIp72UBg-y3acxdXQ1NW6kTHdH4_0Zp3Djky0hJbHNOZ4s5tX_oh1k00bkUsr5X6eEF_oeIYVEEcI8pmv5alk1s7mnoao2rIGFWgePq-RtQlcQdwARI00D7DcUmjmfiXkQmb5MUlvCGkhPHKE6NIrtlq2TSTb27q6qYsacykrSDJnZozQhh2VU8lZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/29049" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29048">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SldhEvyIPDVjBPERRH-XJyvo8_EKt7XeNVF8HqIIsNJgae0VnH3nSRxncpzDPcNnBjVS4iI4p1xlhYLwjVLXOsn3tUkvIPzKrUvcpLpqL16fnI9RCB06XGwy6rpkdrkNWm91nMgmtFvnjOHkA2rQr4KdYaeRMMch8v9gzFTIXqwXd7ghonO3QbKQsIOlP3Jn97uh8AA9S5IpzdBVZ_e1pOw6Z2rIZZjSXnZtzCEbmbWzId7ih_AdRQ78XnC9JvduH4kvik549LtUuc_0YBXs9FWXcnVCEQlCFfhczNJspk246XFtMBjTvVp-crYHnX7QKLxZy3s8jQWL5eEI4DHOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یه‌موضوع پیش‌پاافتاده‌ست ولی چون زیاد پرسیدین لازمه یه باردیگه‌بگیم؛ استقلال در سال 1399 و 1400 دوبار درضربات‌پنالتی پرسپولیس رو درجام‌حذفی شکست داد اما طبق قانون فیفا ضربات پنالتی صرفاً به‌معنای‌تعیین تیم صعودکننده به مرحله بعدیه و نتیجه در آن…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/29048" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29047">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9KOxamd6ISM6tGWs_lbCZ-lu74MQZULsLjehbQd054l5DAQO_Vp1XmzZPFFqfKOum6z3M2XaS02lXGQj4zq7u9fS5YBhiixbUtvzZAz277j2DBXoaAnr-3jqnIPeK8xlpHX2bdQh9cFQTk0299p_9hHo2OSXN7W0iS1g347IYNu2SJkxIG320hdNahMHOg3p26pnShSkS6BLU-opoFmg9xynkoqcjxtp4F9ZYgqKTFmr7kLXlGONO1CFgLuri4mGWlju_eR7j_2MY00VbpLb_NwJWdLqlO0uK-enbPoATNdzlcDorOdlwaa4vZkH9SX7wr4HrRBhzto-mwTFhVQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29047" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNjeS2Dk0uuMutyUYK9HL-9e6ieaqCywlM7dnNDoF4zhMmeKLD2qIECx9v4AGjkmMPK62BdW9cQRYleD3XDST76cdZwdITK1MMpFCQk-R-6ZYQvn8NBcsUDVgm_a-HcbOiD_wUMZMG_QauP0NRNOszVzzQqi4uqoNENFmqbe4OuUTWsYax4X7ZwXjf9lqMfWaZWMWmtTp67SAf4R0p0Yw7U9NLctXGD0tkMh_3KvPbuWuFoK3HgPOwa7e-lE2BMv1gudcgURCGquano7mFsAv0TBdS8oSpRq1jsL9VY8j7wmM2uA_bFAQ4mFypjk68-ftsGrjzN3Ggy1q1qsfQQ_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=dsGd_zaPxQtqnJ8taSdnojhKtE3XQZbkdgVkH0gMaYulVEWNo836C-TNp1YxDMryGIP-_8tlQ9tedMm-3ip3B5iJ2yLB-afpUQKHMmHfNMi31ytakLM8og4A2kO2o8cvSH-9YuZj-BzIVPhbRcFW5wt3-tPM70hcALaJ4u7zbISDKoxKgzAmHdX_8eyw4d5WJODgBVXfwQYwt6kE1fIUIcKfVu3IissK82Ie1NECA_YsSC3A_Sq5KiZjQSGIY7WEjd0yCnaO2uVh-H7XIYqNsZjX_Qc2V5Y7R1F7K3yTN9qkOCqEXXDor8h0wgfnIQZiC7RNEgfjdSefuxdLv48xLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=dsGd_zaPxQtqnJ8taSdnojhKtE3XQZbkdgVkH0gMaYulVEWNo836C-TNp1YxDMryGIP-_8tlQ9tedMm-3ip3B5iJ2yLB-afpUQKHMmHfNMi31ytakLM8og4A2kO2o8cvSH-9YuZj-BzIVPhbRcFW5wt3-tPM70hcALaJ4u7zbISDKoxKgzAmHdX_8eyw4d5WJODgBVXfwQYwt6kE1fIUIcKfVu3IissK82Ie1NECA_YsSC3A_Sq5KiZjQSGIY7WEjd0yCnaO2uVh-H7XIYqNsZjX_Qc2V5Y7R1F7K3yTN9qkOCqEXXDor8h0wgfnIQZiC7RNEgfjdSefuxdLv48xLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/29045" target="_blank">📅 18:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=f09kFnU9jkA5boRtilekglHDxSnY0krgBFvI7fOKpq7pfr_NTpjYGjQ6Dzeeaxm2VTJgtVcbv0LbEG3zwMncRblKgykZEOte9UvO-tdJNesTmHUwGQtnFnpjrTi9ibITSxCM2_Lpq-lCkyINATX1pbMSbneJHXaVI2rq8By969Bb4Lt-9kSSd85qzjeTwCnkeFtlqM4Dqw9D-WQuEj6ySiCu-2V6j5WEKyAchey4m5CRhJkiUIbOEDMV3BI3VFbAKhd8ji5yMDcpKU4oFPqhVwdLSHGrBj3TgL3190gncx2he13XrOaZliFtAoyAAl6cwB8WEPdyxhhf_q-DXrFyjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=f09kFnU9jkA5boRtilekglHDxSnY0krgBFvI7fOKpq7pfr_NTpjYGjQ6Dzeeaxm2VTJgtVcbv0LbEG3zwMncRblKgykZEOte9UvO-tdJNesTmHUwGQtnFnpjrTi9ibITSxCM2_Lpq-lCkyINATX1pbMSbneJHXaVI2rq8By969Bb4Lt-9kSSd85qzjeTwCnkeFtlqM4Dqw9D-WQuEj6ySiCu-2V6j5WEKyAchey4m5CRhJkiUIbOEDMV3BI3VFbAKhd8ji5yMDcpKU4oFPqhVwdLSHGrBj3TgL3190gncx2he13XrOaZliFtAoyAAl6cwB8WEPdyxhhf_q-DXrFyjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/29044" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBfNwwWchQVLp9ccFmTh5sj-n4FNMUryzoRTEb0WMn6rm-Kmjg8auEhJdFn6-_Z_rOCpGpk3WT89-UY9511y-SAN1M7wA2faGyKa9wC6nxLfW733jAOFo_xT10opoYRqaJI9VLVsXQLjfsO9w4w54j0awC3uMD8vMamZc4B5byw44qm8DyQm4B9516_S5lpfB_UaI7MMkAEf42gpQdDP1bE9hZDSSTJWpCVpv9B_-R5UKUqfRQFOkAoEhszj_3DZN9TAWy_0ms1CD55ZkLQwphlrBOoSG90XKwkjK5KzwgcBAmIONsY6ImFxWdVzHuqqPQB4Y9Rk2LTOLQXRP_dHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep8dSMgq7bvHi4fUu_8KOfajXjY70OYKxOojRC5ObcriY4wGAbUf3jYaO-mWiDGTxd3Om_iphAc1k1vIsGcQQZwLcbzBS1iZYOy_nAZP8i48oi93fx3MPSYXL65vhb3txdRXV0_Js7NeRUnZrvV9oZxjCH0ktjcZGJErqRHSRDYsvrya2RSUhmvZDQuumkWiMY30FV0niwgE04Vd9CXrbluRtWP5-4s9JFtx-dIgZv1Gu4poOKhPym0vVqOmWcSv0I1pK32Hm2llnenQWcONKX36GW4RQdWaUWkUG3EFFRiKYN0xXpU7X2wJqOxy39o8njP6nf3FUiKJqGX7IEaz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29040">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyARmuUmnRPduzk82QjwF5ZuepkbW_veqmdwgJLUyqxLbt9Y0thpkqoWJd3bwN3BF_NY_NCgNE2j9FbFgeXfQcZma-MlpUS3tDhT__ExqP9IRnDMYR_tVNO4bhhrT8nsE6-7Hgkm_BHhyWG10BFdkU7pBkvXIvBmDoRsBAmRCsJoaqTwVHnRg2rNbiwitYy1HZqFj5bXfz-O2gwfJpgZ0sbQTZfXS6nxmfIfz-ZbaZEw-fuhgOdHMqevqhp90rFL9NYTAe-UkpbmjCkbATv4YgE50MryS6pGjQZloXOBfbjafMXR2cNNe_Cy8JTrsA-k59Q-yQxMY1rhxvO0IGe1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته ششم رقابت های لیگ برتر؛ بازیایه‌هفته‌بخاطربازی‌های تیم امید به تعویق میفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/29040" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29039">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نکات‌طلایی‌درباره‌قطعات‌مهم‌خودرو؛
این پست رو یجایی سیو کنید، رعایت کنید که هزینه الکی رو دستتون نشینه و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29039" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29038">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyQi5g2en-5YeMIbJupz-d8r2bqeYEenNHRQqHxowg36bzIeSqylqONBrRci9p1x5iO6XFL_U2cY4YNI1gaDYTPiLRxd117lW3qlmkbDmrbXr4jxy3hyosHN770_f7iKc_61AD7G1J5igQs3yS9vw9lf5enTDtINw8Inbw3ZKKXSTV5Odm_aOyT7ee4YHGk8p5EJwUIGeaj5m3tgU6jkd4FrApdO8PX4qqzxjDjAPtBeyF7UNCN11hgTOo-q_RTcaW2xIQYUd_c36s5obJpkiFv1mpJLt7cQ1GZO4-nKCUAk2EXYenRlhr_HxtB3nO4w7B-BMejLpzakfrKOJe6d6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس قرارداد زینب عباس‌ پور مدافع میانی جوان تیم بانوان خود را تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29038" target="_blank">📅 15:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29036">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_lA-Zn5sqV7IYcfwB4TdaN3Ozx7AuJ1ArcG2UkRwGHjoN4t_ZgR0nVyGp8Se8hQAEBW2AuZ2nfWqiEeL7u8uBG3WCjMVOEg2tq1oNip85BymObDsKKCKyCQCIMTVqBfsUR9--CT9MTI7OntHu8pFHf1z6egfn16DAotCq4HNL21H0HOJ9zk1AiAVuGCn2XiztCktIakkmufCiSwkXAIQ_hM-9vyaE2BMZNbXj1G8-ewhAouzIu23vQbq0CuC-Yr3c12fhq9igyXcnubcT9Fk_sNOB-VHhrSca26miLwDxIHJYEhbWpkMuk2Kz3v3htQIDpZ-EaHycCtuIZA3WJ3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7lFCTDZGn1AlS5287jxg69w5vaM2gySPSuwQ9-JIp3-JVpy41GQ8xhX7r6HzM3oWFiGxJfh3lududPyckgotr4A5lnMxLabrjzA40azcp16mLCw8B4yoxqf3dD5mZZD0ul2uY1hR3cIb32XvRrMMG9jkrWVpaVfVvIixnF9VJ-Uo6btSXeyUEdj0UnKZ7ssM84X7TmtrPANXdZS_MUNT8eQqkXr62ALUq4k17wtvh3enH2R8cRhHNwaaJzhFUaqCTOvG91t2Z6gFPBqrlvQFciVEtp6JVkgIhFqzZmthsgwTp2iv3C43MBKrpMh6Nt2waOlVDPSMYV77ccMqBHO3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29036" target="_blank">📅 14:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29035">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لبخونی‌صحنه‌جنجالی شهرآورد 107 پایتخت؛
کاپیتان تیم پرسپولیس غیر مستقیم به سامان فلاح میگه من کاری میکنم به تیم ملی دعوت نشی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29035" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29033">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCjbZIiJq4XKSdJtN9nYP_V8DxKQw0DYSyCQ_wdEZDB-BocfCnkjPuZbbcWFNolOH_FNJv0jnRCCmQAIPpeM2i3olmOrSi9KdzWrnKgZqYkvdDkIE-FXgC-qtYQmre_43ik7WmbCGP84mn1NXEcKa0apq36zAkZmKKVqrTWabWk7GrSE-MIZWg41t9m0wLDCViuNuHguuWPJiLohSFMgNw4UwWr03oMzAjgZ_GuKhdQmVMaMbjJSN2_8ZOxUk4fG5lDrq2b7r1hzmjFSIs3MT31_W387JqLSTFF14noXtpUY6CMKS3_4VhJNN8OZz6BULvxDmFZB536DDtjWblGMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_2ZACWubCK1ABG6YSO6C3kIJ6Z7UBHl9K_1zYk_fwJD0a3cAP3RE6INdyTAwHtWhEbk2tHRWQdQlSBdv25XNAqbi5Wv6cfc9hqRpGYxLlkWC5XUOmAzxWbuzez9_jSu5AN4lsJ-6o1CiognjLEg1k24x0mXjaPAS8tLTfkTSa7FysncPcpahpS6SFJAuJWLZ-TWU0ISVLWt-GAX-oPY5HmPSdOzptMu6SE-fdVFtTVmHfAhoKTVoL9Z9VoWTDYWYuic8S3OY4lcL9B4k0i2WB4qVc6yPqrWfly-u_CBJ776cQZNc7xw7aDq2oDP8OinQ07aiGu5p_7_40A_q2xkzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29033" target="_blank">📅 13:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29032">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUw2drwT1RHECqMbQ2Or5zKiCcU9uaDetsYTkIgNF6CCPmF3dwIUEIbD5p4uZYa2ILZZlk3_rgyOofn_-G6hOv7gVEgYrLd1ljq4mxy9ahrQzuFqK040T2zs5wmrDhS3IxipjNRGE_TYxPJ58CqxuG5f33cZXlAfMAgzEykfuhxSjejEHCl5zUA0TkF5OESEwymaSovcLobaG1Pasbp7YjGp3vv0bGlMSc_dDxEp_OF6krgpYIwvegc2VX-prCD8TKPa8mOLXOij7DioAuCqWr3p9Au_jRihb9-ntKnS_NDNSz5fABZknRN0MEimFaaSkhUXH67FnvN_Pi-jwJZyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
دیگو سیمئونه سرمربی‌‌اتلتیکو مادرید:
3 بار درآستانه گرفتن کاپ‌قهرمانی چمپیونزلیگ پیش رفتم اما هربار کریس رونالدو اونارو از من گرفت. قطعا اگه رونالدو نمیبود من الان سه قهرمانی UCL داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29032" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29031">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29031" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29030">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVvqGIyPNYXVfiOnU04ujdH0sSkNnxrwc4TAko8YL49vGLDLbn30ns8T6uLjts76CULWZ95fASCjBAZLZ_JsNIHVt6mflPh8dGCBHNQxAV2vyVX0THXcmHPIL-ggR6EDVycyB7clDTxvWzKAqnhQROxz5aFCYeJm8ZttHOum6B0O1DAzHNtPPPS0NGUA7HRqTwqsJhtY9BWF73S54mq5su5V0KiUS5q5Rh2aI1TdBJpxDRtyoUD4yJXleAOvafN1bHAp_xJ0Q6F802Vp_HaUcQVl23SNeh6wJORYkvWLRUbD97RBuwV2wPKikgxITPpsHC67VuvMaFFSnIR8bPkZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته ششم لالیگا اسپانیا
🇪🇸
رئال بتیس
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/29030" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29029">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmoHw41y142BNqCAhoVPPjvYldqtuXYlN9sg9tKsrpfM6xNV1JsKOdvHc9kpYNFkTWtT-q4dSz6JDTnTQBhKu_w3Rp-BO9mHbYQr_bGdKz78yDY_dM02vPlnKWh89wL1IByVnYktDMdcrJqIyKfRR_1RYKTqtKtvlcz_CIB1O0-lVZEyPM-BVyKI7AJ45Y65z7akAiochmbYvlMRmA20jAa2AGTewhweyrkJHq5knd_Rh33nIzubytc-9TtXXP4197mpk0Ve6cgFe7PRU5wrsK_gxqJKrVUa7fSlppSRaU-pY7jGdLLHG0q5JD1yrwwtOMA2UwWV1DENGGrTKDzMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
نشریه ESPN: احتمال اینکه لیونل مسی و لوئیز سوارز درپایان‌فصل‌جاری رقابت‌های‌لیگ MLS ازدنیای‌ فوتبال‌ خداحافظی کنند بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29029" target="_blank">📅 13:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29027">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4wF2lm610y1IqhHx7EGxOPSp-JQXXTP-kjhV9itZa0YT3ku2eHnRJRNZAd31d-rU-S66-IzCY404EHbZ70KBOReHvMfqOKyfvYSBO1fwe88CI_KBXWOHPHcq6r7yM-YdqTm5-YanwqpjbwOVUvSUCWvS9Wzn3ZQFaG_TAVp5tfPsajn20dhtBdwsIOGN7Npa-9PPnsHNqG8yOgb763b5WBm94vFXhVA13zlnBnvHR92ZnJfS2t5sZRhGIpD0KY4qG6wtLxdmQBEsMHbErukaE0G5Kq3g7W7iu1Bq469vxmRgXx39NDeD_1HYbuLcMUoOEvSO7WTdde5i29AnA6V8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYG8SaSODOFWKM3pXOfgxoi6UF7xFoOxhT6boMbfaApzMAZZmY5BqTeybsXHLyQa6-ve4KeXdqwLgFgq_TlRaHt0bEocE6PvK660EHKTKdk4_pdd1OWg-qpMQsqn1oEgL5aXt2PuW0TL1t7n1BiYmM-KmUVuz3HIBSCW6LHVXsqvNZVWGQh2OGYc0rwy8en1Yp2QYLem93ZE1WT51MsigQZ_7iT9ysZc6HhrnqcyHrj5rQV_qYz_Z5eKiwkNfE1KmBvhZ939ZscUm3gjQU-cdpiy_CCnMKwCCQB53NYNJowbI64wD4ykFNA4RlRcEQO-gDRwa9gKh1EZtAS1bfAkDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29027" target="_blank">📅 13:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJAEah9fswP1bysHox6BWzVIHf2F1rzTUQAO42IwJWNASNrngo2RsLAhWvHWyZHfMLB8o8E9aVOr6SAJ5w1fq2QaqzYv8RuUPXPwBh_RI6oyUI6xCipAVTbFvQVTT-N9UDFyqX7XgG237ERPtkE_PNs8iWiZGEQWvGd5QCKWeIraS-og0j4oKyo_ivbS52q69keCkecMeycI7zKogXDdeSfoE0IYq7FWv-6kxjnXEMMiAYpBsYBdwlMRESrxmA-QMHGqA6m5nFAwaAwpI_WxC5piK_embVRNcF2T0t7uNIt1_UwUG_EOd9LKqG5a3ETqDXJ8nrTqHYQyb8IsSs3fow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvSbFG-j0j5oDPLb_7qfQApLHbkH2QWDMvOQlvH1oAW4Kvt0aRmfhxit2Z7637vzcY8bL92SYrBy3yx-z1ruC-SnYyLRcWX1D6DWn_lRJ5KIxIYu4n1HtUiMn2RDttjFNI7GytHZDE05p-kjoAFJATnnqGVHAtwbBx8gZvVJMuOczxsCcWutxqmH1IW8mjNV7QJYuWWFD1q3naLUPJ0cmY1xqgoHSUFnOua3akB0RB5--eWMfq88NgrMdeT50PiEZqOhepTJ7hBijbGBtlOkNeZASNENFjz9YGY2GlGLH44CePjvO7Wt8IpNZ1C12zO9ImyNUf3LDEBs-QlejF7TOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIQfkx1ahLY1C9x0AgRbgi9pHY2GG5_6ywVGf05lqt6Z5c5PE0IYT3Q4PZ508gfj8ClG90HqjBdP3cIkjIRF_F2UCZCfzNaBjnYGt0B7P2wG_pP0uQMNH7DkR9CPJO-xuMAppDflRh5gzQ16K1mj7UyueXknWHJWutndyBpAFyzHemZG7jagkhDQxOLbVlnYEU2XQngUcrgCLZBOk-zMz3SiDpDAfbuTciDlO7jRu5odLUtjLuoIC6cGbAeW7--sv0OsgF05OmgLLzA4kCLC_ryriHoJhJUCPGIqsGmLk57p7mcvtNzmJzg-JZXGKCD3rtkUvAuuk0r7xtgAcqhrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0wctuF_4BLobvE3nYgFyYui8RTSB3SHGbI-XzrvkGcDpXKy2rsj0OaYTkZyLSPMLhH-n22DX3LBGYRfcW6kh0dLT2Kil39CGd-LK-b0NLUJT6x4_YB_YD4B-WGLbsZYI9qNEbbiUkrbKKvh3TmEFFqEgN37gaXb4YhK2RLKOfI_UioeeIHhCwNYdXaW_kEKsgYf3T6htSlwBYdp-WfV31FknUNfbthF-cwM_ebons4sXBJyQ33zfc9Kty0paf_MNrsLBQLiHgfm8zXonfZtIzs52JE49GtkfEmZb0tf9YkmcPDx1gKu1JKFLQCI7blmJqwAe5khRWVcnaY77cQNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc_NnBwKd1xSUrbA2-e3r4IZDyu4mhZgIi755l_MyihcbUO8xFsEBSdWixnqmIJkhMsXlg6EBg3mqFMTxuD-L2KFrrQGq9YcLKKPxQbQ4N8hJZXs3-Qj1jhy7B_DvNAkAQfOcsSSeVqphHvWm1yG87Wnjcc7hNOYY67ROZsaag86WBWdVLK217_KzB6vcsRgVu_zLiM6PqnA0L_Mbq9H1bcCmzBCHoN36uw0VOVDCmBI-6OcWrUcj61-gjAhVnFZO_yNlRfgssiQZfQeE4g5_zmErUTZ8o5tM6Cz6iD8gcEx7NLxYFhDQ058SHQkGPqOubsxliH5F20HIACKlEYOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFGtQMBGSea0mPE520BNUsr0f1D-DJiKesQbH7oeSgsKiOlhUr4RcOpPqEfKqi1-Qcf-ra88PTBUDJK718J8H0OMt3EJcOn-2x_SkmEojFushOLJPKytdbTKaKK2TzlpL8Qs_uzGgt9Kg4z2YvVRLXgO3UqyfUF-GjbTjx-4vj3x68Q1VYyjG6EJAmyyhGtg3YFYD3N8etmcI4utFR3Ao6t2ExTsQEiVbIfhKSdsRB-NWFNal_zCwdPxL66YMrKhp2ZD8g_f-XXM90oaVfHcqewXT6ChOlMyKIw3HqQIUxppXrJRq1qht750Flt4BdrhvNv8D3yZtJgdoAWGQKQTMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29018">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCsbln9JZljuriC1fvGJ5e9leZeAfE23abaJq5imW1wAr5Iu3R8PwQkF-ng3PtM_g90XwXOMbzvkSQ4QK-1ViaYsIA_qKeB29LCp8_6Yz6RSbgja016Y7pI7ybAXY6ZnXXFD8vrDeQCSXtAgtArfXroaJkI9TIStkmAadckPCPnuB7nhKrLk39puEMfOvpLohAP7yzoxv2AL1STf-a6v6Z12GFo6A3fO5xf0YeQWZY8u8QxeH_jj9hnkuWLPi-fouglHUG_BIgnxelwheuFo4_ckzVkrylKhtD3iYlkKT6BGU0UAY8B8KWgv4e3BEfXQeCsnfqytwii2DHIJWRVKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیزری‌جدید‌وجنجالی‌ازسریال«مردسه‌هزار‌چهره» باکارگردانی مهران مدیری. مدیری درنقس عراقچی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29018" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29017">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piuOvl4xx9sgrVxhHxaXV3c0be0QzMmvEpa9QJsV8_q5RF4klPpwsv7Hz4te6JD_E514lLsR-9g4jQCTDR-FFavYN-BDWImenunefA5AJHfCEqDmy9oeHKvaH9n6m3wt0NGLSbn0CJ970ol1RteTvMtPc87Lt3KV6-ZJeghLdiJn8pzxI0XcBlCaSamHI43bizMa_Mz-BF-tluQhZbw3Y3uUBMLPU_c930GZ659RnQgSXpINSXOLbGbXSUaJ-h4KycUAnalrWvjV1SxUySf0ZolOeJEiZfeMBW7Lw5nf6XcjIEwKi3Tkz-gqHl_q9ce0Hnj4o5KAyHq_5K3UtKauxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
گابریل مارتینلی و همسرش بعدِعقد قرارداد رسمی با باشگاه الهلال عربستان؛ مارتینلی در الهلال سالانه 22 میلیون یورو دستمزد دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29017" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29016">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAANBJwmjl3ZLiOD5CnTUKZfuI5aCr0GpvOXhMRDEuFxKtS_NKKy-xFbU5rJ6I6XDcaA1qUPJelp_gyCsrfSA0Zoi408w480OTTbcHUiWkDWMaSSoBuq2HQ6-uOyVlR3abJSGEcLriFnsqejbjBf_XIHtS0B7JhnOG-WUitX8EG7hKVsiZMF8b11IJk3si8-Ptc-JKt1YBGSTFd1WsGca9FdoJ9_2weYsAavSxqTduXv0HSoo3ldfvJwtYgGqVofnK6nKhvqY-UECC-L3ZEa1q6odJsZ2YvimpDess6NrMm76t3wx6PstifKtIcWz_ls9YbYGLdF-EF34gENgTA93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار: من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29016" target="_blank">📅 09:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29015">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcr0H41fgbmnzrygGmSePnIk4k08JlsLpIWdnZnvQp5OwEfvluRmaWq-YiDWy8N3B4YON4y7QjUhWefZpR8pPiRr8zwPpCmLMMbWJ3KqxHp2Br1ckZH38aMuqQiF3VIw-wLXy20Ze4oYiTGgfzjrymGdpJC4K45YDVnXbMPkkNLxksifTUfvFczvgZxnxhZJ3tnQPz2Jehv2SmCGeJL9Nq1TWdoxpM7c3e6JKkT8H-eeom6gpV5RsiugVGd3mFop6zUwkOmkTFSJ638esQG5WO595ao4EJ6NM1kQP-awZA83JOvs7--Snav0w2_cuU-7E4WiNTNw5qrQTLkvWcEsLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی دو تیم رئال مادرید
🆚
بارسلونا برای الکلاسیکو حساس دو تیم در روز سوم آبان ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29015" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJhOMsRxXe5ZaKtZPFNrRzSwPfINFupFzaU1N9WjC2L4RAnqlE-Nkqe4U0Ln4NMdpXmYaUX6JOyStnnP7gTUKkMxFeREBroPsUoLmIv8nuSQdg8vRHSF-fnIVrSdQxXNpZnQh5V9-pqxsLkKG7LO9HVrV2PcMOxn5oS9otxRvpOLsbIqrliuaDPjkXzEIo5VcUYMBo2EjkzqMzhdldv3rZPw8hm35EKjHUpCfnH3ls_8eks2Snw66TtEaQMMbnqU4nGhy8N77jBQxVHcNBIW2e2-ASIzdntG-XslVZfnCVZ6UtTSjwktiMtQBTR4EeyTB09uMQ8hpHVcTF23mtyShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvnBcB3uQ-C-0cyKORJe0e8IcPPfDV65XHhDTquFrn_r29281t5tJFQ7bbHAWdIv3hQaEnI8jMHcI8z1Df1or3sFhxEXVfn1me9Q6fBihHraaIWsibF9t80ZsAsBOugZJejNgIqzlO70HSwAmwGCa9mMQeCLELp402irvCRPuVEwTAVxsoxbv8pVJs68ZRw1u2V5Dd-9FwoR2azE-CrxtVuGlhPrvMoTSKGJORbgN5q8xggpUAv_Q0podZBKg1QQMmXBcy1-FvRiRkWCtojLWVzb1TKvZIK6PCxdQjKGMQ8QI3O6Tedw2dbIFPOMth0S6Yi4-SsqssVsvSpRjge3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=SqPwDgXYyw7jdAUN2lpmx_sbUkGyCL-TwEkYVEJxZVgVYXbJkzM08WGdoi-xhBaQKvEF5OGdv7vHdwNNzZzLgWBzn9IxxdMXRHFy-79FPIafrbCOlJfsl7rZg-uuFgOBbcb-J-9VwM4xkM3nLOy4FaBIDEAOaBma8ZFWBMztnj1s3w2DtsNYAZ9BfsI79OTEjTAxaIXT4M1uo5oTWE1v17y-_BeOwBRMgKVQB-8vZOcAM74wQ_br8YpjiqYSRXA7M1cLWz5FwDVNpbA8eJIPhvl9ByhYfK3HUCA8TtBSrio73irs1CxF9Ebk840bIJ_SjG13uIOzuNQzylwzSZpiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=SqPwDgXYyw7jdAUN2lpmx_sbUkGyCL-TwEkYVEJxZVgVYXbJkzM08WGdoi-xhBaQKvEF5OGdv7vHdwNNzZzLgWBzn9IxxdMXRHFy-79FPIafrbCOlJfsl7rZg-uuFgOBbcb-J-9VwM4xkM3nLOy4FaBIDEAOaBma8ZFWBMztnj1s3w2DtsNYAZ9BfsI79OTEjTAxaIXT4M1uo5oTWE1v17y-_BeOwBRMgKVQB-8vZOcAM74wQ_br8YpjiqYSRXA7M1cLWz5FwDVNpbA8eJIPhvl9ByhYfK3HUCA8TtBSrio73irs1CxF9Ebk840bIJ_SjG13uIOzuNQzylwzSZpiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
ویدیویی جالب از آنالیز کامل و دقیق دو گل استقلال و پرسپولیس در شهرآورد 107 پایتخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbTnY1Fao9E8d_Cyx_jSUT4e-4BuMmcuGFnKjMdZIVZ0a7fWo_ttqdXlP5Ca7-zH9fKI5ovOzLBHFFm2vq3v7yPMGC4aHPHvIdbmRF_2XffAmuX7wOsI9L1Y9UUqLtE74kj7NTnQvOplNmpXzOF4q47mPehZG9YiC3pEeln1SXMcHgM7TPI0XdyY3ZJGPjMyp_NJnhLmRm39iYFmdXbVQkNHqHlbE03I-jiQpx26f-y4KFLEne3VCgedd18aKwiM9yJ7FeKFktS9qFRFdSh_M2uY-q-fUdbgwbN4UN4RJVnOywSreVRceemTXPctMUvl7QsF062Ql4sS2QyvdUw8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-9EEIrtN6-2cgPliT66HD1_mmnieFcz47w2749Lw0vrw5y6IREmfqEIe3nslPSU1bn-gJExKqGOn7zt5BgNqnWS-5Hb0uvi3fP1BgidwVOQATcGzbrygriKc2nPbj6DAp20UR7flZnh98W0cl1ggy-EK7cb5qy0nawC1Lffx-whTHuVF43Os2zzFQweT-FgseSc1Bmyc9yl1OVFk-nBx8tJ43mMTWMsYtNhEtnOQN9oStkkXoB_BtgXGpGsngsnDN-YMwu3lsxHAAVimoaNVuEDpVzWjN9h9_CilYpArZTmx7iMue-pKTj3jrPbfaEj3CXHdGTWT6Gme0I9c6t5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUVnAAWpyCjsFeesKAg3BM2eGMHxFoDE3YAOu0kkE_EOLVMQrzIKd4BHEQYp2YJcKNpMj91ODy-b_drazwD9kUfLAq1DHx5QSTN90AfGK9Bg0_qqsZ57AyFCtGwuLMBgdUrnqdvb7MFVbQM1a3kzQyIUFkqT7r03M7BQg-3Wzj02FoyD64McK20yCqob-5o9Ql39Cz4HNP6JAwNCJwzSSrduEN0QblNL4i0StzZord0LzZsK1fl_Oo9UNkBnRloKgKXHwb-O1xmPA9gRlxyZ0mjrVW_qpstyJ0C927TMp0tLnUdVt6BbnY0TlvzVAiY2edTqKqILq5VQ3wG9bbZlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nREOkOjw-ip1oZSzHAM2Ia4t6sac7YF-mMjVsdebYN4tF1ivCQkBICsMo9WZE9fyD0ecPCmSz57lVfGg8VfYE-NkYItTTpsEPJtBG7qmX5oUIecTmV1EXqtXbZMepklZNfACdssSyIYG83k8z4tVkp7qdzunsvGQlJtm0KoLA0--oNJxftnt2pjDVcHXr_WzAD82xwIa2Qv6Lh4Q-7egUyfmuZyt6g3J4fGl52P5NCMgq55cm1opxoHFLpbTuYwUDNkM8aPy3VBhjHEYTGUEP6AqIBLmmYb8BhQIvwldCNLWhw8mdemtHfHzJCB43wZiM7W-X3evuDdrECf7LNVW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMLQuTwr1HyG_z0pufQR1Z_0-L8dcgYvxbl3QzCXXXYV62QCzYLkkw723LvY017X4RjHydQJ7mazLsJ1dDr4o2vx8mK1FwA6Cd-41obqwDcGXJoXi19nv9j1LaibA3kMHQRqUObYmZtJOyIhEKMxI3znj4N9gJz8cjKa6iuS2NZpThsVivffEH0Yc6rHfZQfTkL6hYvWPOJdPhlKCUTfnSBFD6S_FSMU1klFWuIOmbLMFX-H1jewobDvl-pWQ1bdGKBrFERsm9oNBUH19L5H55lWPLuMhMKMTd7-hA_dGonAtuqS3Lu-bs21urmV3kLgvlZ9-DA-oVtsn0POJ9IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnKtnBNEHb_3WySJOwThB7xQFYQKqNfBIFgTSh9eO1jw432_oX8FqsH8Z4ccDLrYIKgWnayJNei-NWMc5MbnzCFSbYF2BTfNjHh0FTfnl3VgkauJvQBnEmkqvCcV_GV2tSn30CV7fXauWRurbsFUV8f9-7bmK-bp9UR1oaHJ3aLeu6Ir8Y5z43AzaB7-Py-E2HNakv5nqV00Q88hZnMZJJonAzZ43vIt_2zWSd8v8Nt2EQj8u5EByJucc_XYz4OK1jY_vlLSmf7zfbUEk9ejPhYE38jEx9aw6lMryuSw_EjWfanqFTXzdxxbno-ybVFosCzd22pMuJ90E4te7EyHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3bWhEzLAuvpP7g04acibsZT57cf8uxHltQR_MrCIKq9cITW_AlUuLtJHr60R2X2WRa3gh0kBYXsS1reUBzzOgzVOMi5mVOhfaEtq1pV8Wyab4cL0BmzZ4rDuXq218CKcmd6PB3WCJpRAkgUx6BlZKqvdPTUYUV34vNzaIJX1xoDw8bwVvIrMA0PUDTeIUaUdV_HSDkxQn7u3EKIoNm56cZrH1pAUn3iFh127oxyMkURNLkZt4OayTAKzfI6p8EhfZbtD0uWa_lFhwpt_GL10YpO-X31GdMHiHQqYzWjkysZTRKSZ_F5IP9MZaqzD9UB5k4EPNQ5VaDubSUhiZlZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CuZU8yC68izCaNYj_m_SjsCUPL9GDJzI_L7TPZ0SVxgjbuKo1nmi_fqelV-gyu7gIMQGWLW5C9ET8Bne2XcZ2-IniiYcur-aGH2MaVe7vpBGYyGBq5756v2ux4BbZK2wsSQq1OKFcSCvJBg4BNMsSuyGbFOAt32v82RDzRNmizu6oV54DocoIAckBiLVvCKegre5Axcj-PcOdUUfIslXS_8gZ_UK4p7i07707rMllEHOEEyLdWC-JHcQEraWLFCbLcnMwyaINZoJ4avYasf_ynqrSffcWM0vyf1kyflCY5z4mOGWtSwqUNCauHrPCBCXUg2iCz7Cia-8VFdUDe2_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiF0Bffai17lMlQtKF6vpiVICgftVUevdcQXMk9iOgKTwzd7ObPzJLP81I-YZ4nVcrefCP_sSZWuG3nwaRqx42g5BLlequYDCvMeSJl6Dr8fVqwrKsWjuPWgY6MNmTIwouvkVrdMbHtVbfKeJOE5kcfTHzCZD9XTMKNpSPzqXQDZOYdUm-6pSti1Yf8puW84KKWrgV_MIBD9_oRtyq5LSz5_U3yZyUg6sIdPwKxeVui2b-5vvo86tGNGBUsJkrhCQSeCZdJAGZChialLrMLpL-lt81xBzlAMrIZbJkiUpcbSd0kTXcdUEYb00BQ3juH6He8ftcIoFzlQfOXRS0uzUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvobpQbq59pSiKwxGFBiHeoGUuU0ZCvaUZQZ_tzcSp4nKc-_pstwXibPRjaUJm4fSSNVsnD1QLLldNctd_bC1ncEl1uSOKK8EKzx7o6k9nS9e52RqASk29fW53I6KSGuu0Txqd6GoclFLr1SB8KDIKiJ7zDfJLkGPCbYnyTh1SUTUH0mUw9CcT6onxgiJTcg6TaX3y2vzcMCCxRyX-2fPpDl5Az1GMqoo-1wbq5KEwlj53AfOaaWeRGXm8J06Q2sRgIhlHq7ESMg4U8fZEjwWwJf71OChubPi3SHGtxrjz87064EC-H-bni9J9KrFX3UXfVP0HQt-F-beaFZUA6Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcMCu3uHB70y2L0tvn91bmvvy5-nODopTxgf-37Mz9lzngpPwlSW8zgFNpNASXFu1VsR0Yi8VxyJbNS7I82mKmDdbNfj0wtHDwKO0rJa9rp3bqgvwuVbY3bLpZz6Zq5O00S2weDL-WSTr1QfFHR1lsipcvkEEdjIsBuggSMjJkAKKPZLoOqISc1Hkh_WGtQPhNxLU8jqOHkSoizcpNFSbmjSaR8oF1_o8WB6BJ8We9Y4YNsspLmyto603Gfys75QW9vBdTJeNHz9_k3lZ5x7fDn_EXdtkZbO8w11XI6rcqfm8vp4OUQQMn79nwVPFN38j7M1OFxZhnphu1BkcyVm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuWzobXOKKFwDXl-xpVEw0I3nEL67iC7YIDZzsXYPgmVxl9iXbYsZEyqlFKrVs77wAQYUf3iBOnn4RJ1yuv7T_GNCuMpSAIIMfPldBsyY3cG0wZmtsc00MGUIIkMM3a8CVG5MYQhBSEbV-yl5fOwcDg3x9UXdYN-cFR_TOt3no-d0BTG2AjlFDukwBEyiAiA6KBrSW3oji_gRg4U0myO4449DpvkyZnc6HTJXjt7IqiLEblgKVCvNTO53ehTbn5PpeeTF-md4WteWgYZg1ivl8CAjIPRSRq77P05efKZkNWd2nepuCcaAd83nlacAAXAbBn_0q_l6N8ng0Gs7F7cVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coRPWDN4vhZNb9QnFthutl4B2ImW1pLSWxnP8ek589rZkyfJnR_FESFS0XpCzIqGwUEUfRO_vdF-e6mox6Fb4Yf1nTpR4I3V8Mm7jD6VtGLN4je2c-CTNeCbSih6ksSQLa-saVe0X20udDGNtbznmWUYvKLBKWQnbeqs--20TfvRZMwwaCePn424Hn5o3oMkSStlM3E659HNA4rMongxECT4NNUO3QpO4v6oHT7yrbWLrP8e3kOtQvP7PQH3gE0BpyBfEC0USIqOcQjia3uW8LRCbXTbd3TL5fP_S-LvOMRM-wIRaG--VaY87jnNc_dK0Zx2bSKzWmBRcNkcgue2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Tbi8TSfuiGj6ktYj9Lr-LW_8jVhLrAdFptYzzWmaaoEVkKpkTa7x5PoXFWd1VscjXHaY5KRmM4jpSVwcGZULkCrc6w15_Gg9BwlxaJEjGpepXTsz_yGwCoUv6ruB5YzkbxJVUNrzEctttR6P-lFOq-AvEN2R3sgjU7c3uDLaAY2n5ZEimNvOsqI8DPCDr_9ZMR29xFLmVPOooY7yWGbkBkTKu_MMAyS7F5bUzX3fOjSRFg_MbnjqBFlVuDZipqtLRLmnm8-qfb54Qu6hDQQ1JpQjufq7tR2bay-eBjg1KNy_wO0Fz3qMvjt-PCqLApnAG4005jiubrOdPwrWjtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=Z5HgxQe4tI1SpRtPl6XUFF9f7zuXizoHOzpRpZ8v1S_5Mvn8B_dl_5dy8rwqLiepiWG9w237ZbE0pkoDxix3jJ-oBbJmZw4_ujfjHRU_cGmppQjFdqL8UvtCAmko8HgV-2_IuTnu1c98jkpJ9-hmJt3AJ6-vq7_4TskvS9aCzboDA7cGGAsjEYC3V7PgmXkc3uM-buR0k_j1tWO7PnV_mecoMg75yn8D6aDpXEuf0uflKqBIqq6DBgHimdAOpg121R1naw1ZIKjYNU80sulVSFW51XZi5EDvUKLXzztXb2PRebvDtDu7NBnCOzhvnyXltPAYM3zfDZ-wpc63g9vHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=Z5HgxQe4tI1SpRtPl6XUFF9f7zuXizoHOzpRpZ8v1S_5Mvn8B_dl_5dy8rwqLiepiWG9w237ZbE0pkoDxix3jJ-oBbJmZw4_ujfjHRU_cGmppQjFdqL8UvtCAmko8HgV-2_IuTnu1c98jkpJ9-hmJt3AJ6-vq7_4TskvS9aCzboDA7cGGAsjEYC3V7PgmXkc3uM-buR0k_j1tWO7PnV_mecoMg75yn8D6aDpXEuf0uflKqBIqq6DBgHimdAOpg121R1naw1ZIKjYNU80sulVSFW51XZi5EDvUKLXzztXb2PRebvDtDu7NBnCOzhvnyXltPAYM3zfDZ-wpc63g9vHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFv1iVaNWuOqBfBjzEzZmZEqVC0gXZbo1sDxw1XfMKw1HZlUBapOYck7BVCozKXZifNLpPEhp5OYXLRsA5HRaoLV42ve44ZxY2k_FDWN-G-JnwfXdT6l1sm6_YoMYvmgdYhlRDi-81RdmNros_L0xRZZOla69HmnuUwmYXOhvIgZQX6yXiH3P4SdaeGePIUz1ya3y5iXYO6Lpa9mmuDv1NPXKAltTcRxoUcVIZTbNJJtt_pDYSwE5MiAC7LtukHTfI9IIQHR4W_UNtgJvrA2icTgF2D5CaWyS42QcKb_OkGgPKnE3bb75yHhxtMT5bWPCTSn5OiKDLCSOra-6nbxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDC3iVn0FGk1JCl0M2oJoDUSvgqRaGzkhH0YybmwTKkBNtSrnzaiefQiZ0MjGSMuQ9K88gBYoSNlYkv9kZImotg7VaVcxN_7HMBIzt5Ovs83zTFaRMp8IfUIkK_Zn08wvMztiTJma4xKhd1bNg6E6OIgPZBFMen4vTTHcBfjUUL91Fx9r-d84gZct3-Vo-kA63imG0FxzY_wnm3xlz3B4q9zrgnL7nt--OSsGMdo8Gi_rECppMuwqkYhqV9-fQuwSufNZLVXPMuzZGaQml0W9O8ulQxsg1gRq5P8ObEyPnio6ysbph6uJHbYWL4bFQ7kFjUllXh2neyS4D_Fis1d6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixE5B0KAEkFHOPWxz7eo7LknFj79lvsRiiam5zmq6fJYDZzkcxAqmaunItKjl7FBHp_WB9w2238sxkDIV987r3Z0xaZAqgk2bSLOa8ZWW8bsEGaidigrYst8hn1puZ5LwsyFJBhRgPbdHYwVvQBF9RhKpY6tT0Xbd1sNxWLRJpnP9TUDYZYT1Q5tPtliWJ4cphDHKN-YvEP1WZzBKo0w0kim_rCRw9bZuSzlVAYqZmwuUqBfzyKNM0U8VAk-A3xpJI4FWFpmPeyitUz3T9gmEfBAzm_PIvnJavtg4wfH56ua-fDmCQlgVd5A6cZyf61fS8meYREoJtz5k-qbZR90pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfba1QgNrWAI0R2wWvYJyOndQrfmUPetV5Pq5yGmtaE5O-g3Ow-BmBZOfKD6-_0RN2Og1vyz0Mc_jx_fyLeF_S9FoQfWhNlLOP1mjf8nuKBxX90GF-xFnZ4He489VAMpG0P66yPGftAg0r6IRCrg_hnKOWf9IoWKrL1tk0Hrr-1pXOtdQ-UDxxkBmiopWgW-UKq6Ea8a9SjIEBBuqfCes5JVsuWoe7Me5FIlztReB7gCWSxNHGW0ZzmmAkmgsVzs4vW72n6z7GRImUX4mu1a_xU2yhEaHgu0PwoI4CvlqujeP-td2HZOxQTGjMedGxuNEyy-gNzGh_ZTStIAUxu_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=cqMdcEz5D_n8JTvzYtY-Pzp44WfpuKga2ohppT3X9xjtFwRxvaKANFe4l0C_AM8ds-OYhGLXJ1ECIi2_AtAVrMxIfrUbIznbeHBcFAUU4TUwPTslF8vNjMXVIvuRUAIOvTW7O5bdCTDdoQBtYXt2hXbRvq7Kd5wm_ILFjXy0Z2yUFgRdJN4SJmtfeFEz0bVl9tWgnohF1nofBBCXnN-x_Ed0-4YD57DAq3iw5FB4g_EqpVS_mXQtMivXDf1Kel4c0ZI2Yuo4QkhG1GKIMJVoutkZJbt6LvU8x8xuuo1jr-yNE7dTkGkv1ZHPH40MIC-Lxq2z2XMit5bETAztT0rt6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=cqMdcEz5D_n8JTvzYtY-Pzp44WfpuKga2ohppT3X9xjtFwRxvaKANFe4l0C_AM8ds-OYhGLXJ1ECIi2_AtAVrMxIfrUbIznbeHBcFAUU4TUwPTslF8vNjMXVIvuRUAIOvTW7O5bdCTDdoQBtYXt2hXbRvq7Kd5wm_ILFjXy0Z2yUFgRdJN4SJmtfeFEz0bVl9tWgnohF1nofBBCXnN-x_Ed0-4YD57DAq3iw5FB4g_EqpVS_mXQtMivXDf1Kel4c0ZI2Yuo4QkhG1GKIMJVoutkZJbt6LvU8x8xuuo1jr-yNE7dTkGkv1ZHPH40MIC-Lxq2z2XMit5bETAztT0rt6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماره 17 منچسترسیتی که سال‌ها بر تن کوین دیبروینه فوق ستاره بلژیکی سیتیزن‌ها بود به انزو فرناندز فوق ستاره آرژانتینی جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGKMoDVjoRBwZOPcKikXaR2EexJlphSKD3MqkcJZKvNN9dmFwRR32i4_E9a_5UKtACq90zyoe2GUY_C0fHZJs0tHHPgjCsyUU8DDexqUZDw3ikE02amKLPHHe3s0_4gzA1JTE38SwlcEvzGmYBlCBFoeKzSSrRIc8FJJqE46XjKoVaDXw2ORI4Oi9QtqiXTCJyWjbk2U77K9PgIPxzYUBhCVgwpiOUgE3kwdQzogZz2TJdl1MPV0i5sFo6xwOHEJwHBX4e86VsXguVDqYDRd33LKyB_ufzdxY3u5tRBJi_hopjO0lGOLS6uYEjxc_Vq2jis69AHQNNdfR7iyoAIRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=XSGt6EoHI8G6HsDcRo1AyF0E5-UXzsYMMI9DlHHjFwwUIFcR63Qn3xbRte94aJ_szV6juAbAd71tMFgzPDUzbWK4j4RP9JQ38Ywdclx1wXR9jCsmO3DP3GUWutYf5zcbVF8vMqv5NrpDOK5Zb0TV1w-G5TqNksRsBJsjbU3-wiaXK7SMaNwwURyM7W0Yvyim-S6wwMFaURD13pOXnTzaBWw7l-aapCujowzBf5i4nbSU-4J8ONTpKD6GcxHRGGf_Z3AZdyWPLPdCvzHt9G1-H4kyuPGcGxfQUptAuXac-qpRpZKKtlgJmJZzSUov68Jb9YJiy4vhvf-wWDuxjA8tvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=XSGt6EoHI8G6HsDcRo1AyF0E5-UXzsYMMI9DlHHjFwwUIFcR63Qn3xbRte94aJ_szV6juAbAd71tMFgzPDUzbWK4j4RP9JQ38Ywdclx1wXR9jCsmO3DP3GUWutYf5zcbVF8vMqv5NrpDOK5Zb0TV1w-G5TqNksRsBJsjbU3-wiaXK7SMaNwwURyM7W0Yvyim-S6wwMFaURD13pOXnTzaBWw7l-aapCujowzBf5i4nbSU-4J8ONTpKD6GcxHRGGf_Z3AZdyWPLPdCvzHt9G1-H4kyuPGcGxfQUptAuXac-qpRpZKKtlgJmJZzSUov68Jb9YJiy4vhvf-wWDuxjA8tvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcMz3owb6a19-mSkB_mL-MVbEm-sl0O2Hem99_aS0u4dDUJ4HrcB6RMkRuJgcIJmqEhYfWyObx-ZWgS0EZrZpOKu3NBMOqn6_HRkmoKIiMtWuyJgpkerAIZJ7e1HAsTgrhA53SLMXrqaOd0nnL-5SvF9wVlhQ-wP80npMQZNPr-mgB8ohuuiZ7IxBYr0XkQEsoSsY96xjSDYqxXEvkZMeA075CS7sGrT0CVtSOl2217fAbe4zJ_OWx8AFe8gWDeFgkuiut23STpYuRZN9HSxAvY7jVL2EsbhAofLzoB7CJy1pPN9Snr3sALQ5PzNm3DO3fQZ7ltXl8RzegUZ6zs_wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28985" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTovn2jEsTxRMKXU2EGkBiEIB1ljwDgL80AqXlKpLY5K0XzhnsTxGCDmHk-D1Y11cMxyA2ft0FHYNvviKpJx54MtBlHPJhDAfu5O2g-qPrig3pGhRpc6rq4JQ4ccH2ZyTDkMPqbsrJqdmk6HZPdMnvj5z7K5TUsMITgxpsmThlB2x6pbCZu68qHxtmpv3rcg_sXfRb2KOCKqsZf01QtzHVil11QnZXnoGXjUA6EVTTMz1uQhFz6v87TOQvn4nR6q7s9T7geVEtVAZ5nrzQGPRjpgN4DKMB4gvi51OpHEbGs7Zyuh_DrL61sWl_11iExFVUL5EuctnCo06hH53KB0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28984" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmVJhnwNJs4x6MKMUB_NvR-B1GXyLZPYdT90sWWIURQ-oCIBrseUKImCJMB-yU7TE_B2pIHZNYlxM0ijcYUj8lDfHKLSq21SRACFovpnuubRi2X5bvhcpS4rLaU3YKmobm7P9MD00CZPLOi6_VQwYj1h_ary3CzRDmZn7VvzcZQgVe9VE6bcy5LPaVgrK05KxXCzuuf9A0OrRQIZY1FKesMz7z1-q8OY6Xrd7ud3U3tlp6-tAJKKPgaoFMKDHhzWFs0VlJMkJNLZQ1D6DHIv_wE0DKiSOc8vr_4OEzZjAts51l6hHO6Mm6eLCVp7TY2xAdiAHNGIZ7GoCeNii_KnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C46U_630M1lTTLwe3xX2a-MJSij6xxC5N7c_RtgZD_O_bpBfUXCGSDxsdym1kPeRJUQsRN_0Rr7emLP9FCeW8X6x6kHh-pJT4dT5tmt-yFIlcPz94phb6EVV8sBhFP28sLSRNCu4vC2JGvqTJhMgwwtRIlivW2oDuBKgbG9KUB05ofJlukqlaclGXM1i0U419Vi59yndKmt4a8v09KuHuRdSc1Qjbb9TCPVw_vxNQlAwHfVvPOHes5fg4q2UKJ-NHk-eCvB2-FuU_WbGMZkY1ERwm_ZZkVAKzS_4ssNe-S2oDeHYQHh4ZINEC-yfzFDHCPjG2DNUunBiWfnY4JtgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWgILwXnUpS28bTNSZmbGUS9fA_4l3PPr-4uHSWelxG2boEC3yJQmRG1l0URZcY6qF730WiDO2XHVgtimOz_Zj9M7MZDVaSDM-2G8UuIS8v4a77q2mtLMLH2r7yU05o2yNekUtnq1aA2FZ1N6EflUs4ihzzPlQy3AKFYlImmsx4NxpgOeJeItaFrvdKH8nkaTuD81X-SZ-dsy8wsOdnH7DuDSev_1bVVszJ63c7RJMk2L7Uka1UG1kKbIrQI3UWCg4XSzSS-N1JKT_RMHpkTS-6TkXgwD83yWq3epVUIjcky2flDnuqaAXKKsc1qmFX0PqnQsro5G0stpWyxT9v4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noaGb2gV47pJ6p7YL4V_bce0A2G1pSiVm8nGc-f74phGjyfIzcntbJEsjK23DCvI32LidyDNlKdERLzllO0jR9UsNuJWrdXltIgQW_z7uiVJec9Fx4OlqVokmIsGIh3yw5Op3MRyyjuYp5LHqzMyV42qXGN8XomzWTlihDlFTGq1xiMZIQVKY3hl85h4kGTHM9EzOblKNg_ls-Bj2ar5tFObJKrYc5oIeX4lF7fISTdg7THl2v5aRFtZJ1xh6XuWCCJ-DDB9fMbwCFg2J_999dfLSOqLxFBf5twGZyfSuxo6LrC0shfFyq5sUnoUftCpS2ZsryVEozo_OdIXbYd11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=Psi92kRLQNObuwaGaXuZa4MnwaYuF8m7tuMdtIDyMrEqkvb5PQx8H4ylSolD3LOl2wlLj3mELhI3P8RF9oIuWKYyHCNGYYXkNj-qbO19TrCL8jbvwo115uMdvQsB2nCY-0JHXsSXGNNe62j7KAsqTRg26XF-UMu4-vXsGvvTM2vSDSgDG_w6SK1YV1IyUXuFp1H-kucvoe4rcid8DpX9KeofYs_uZAdL69aIcUxwOZIP2lPmsvIB7tm2TQxsZ6njHb1t2A9beQb7c-FDEC-Nl-8XpinJzM8ydTqbqTbyd1u6NQgMhWYtNUE9E9G44AHK4FC7xreVzdegsPJqZFeMnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=Psi92kRLQNObuwaGaXuZa4MnwaYuF8m7tuMdtIDyMrEqkvb5PQx8H4ylSolD3LOl2wlLj3mELhI3P8RF9oIuWKYyHCNGYYXkNj-qbO19TrCL8jbvwo115uMdvQsB2nCY-0JHXsSXGNNe62j7KAsqTRg26XF-UMu4-vXsGvvTM2vSDSgDG_w6SK1YV1IyUXuFp1H-kucvoe4rcid8DpX9KeofYs_uZAdL69aIcUxwOZIP2lPmsvIB7tm2TQxsZ6njHb1t2A9beQb7c-FDEC-Nl-8XpinJzM8ydTqbqTbyd1u6NQgMhWYtNUE9E9G44AHK4FC7xreVzdegsPJqZFeMnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های علی‌آقادایی درباره تقابل روز گذشته دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=WtkXdPBckuFbXJMsQRbILqnZosNghk2hBNYm_jmN8RWmAtJnglEBZaTtzsVTEgmiEB-uqShbO0su4eBy9c2-e3EFcjc5V4aXmWvJlxh1EXc2X4faVJVHKauLWrst6YSTCRrwB3sj9YSDn1QEOrdfdyLqcXJYAQGIpDFE4jQldRuOJhMEJowouWZcu20aNuW8GeKrDt4gA9AUYuagWt0yjOJl9-AG3QMsCO8u-kwDUtBjJ6ilP_w9b59eTGOYUJYX7V9iSMLdKR5sVwqU6l3M_H_CHaq88psSCpIrqs3FvMeDIW_Yk6kPvGYVCRGzWz4RIZ3zr8ym_7XCVoS32QAm_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=WtkXdPBckuFbXJMsQRbILqnZosNghk2hBNYm_jmN8RWmAtJnglEBZaTtzsVTEgmiEB-uqShbO0su4eBy9c2-e3EFcjc5V4aXmWvJlxh1EXc2X4faVJVHKauLWrst6YSTCRrwB3sj9YSDn1QEOrdfdyLqcXJYAQGIpDFE4jQldRuOJhMEJowouWZcu20aNuW8GeKrDt4gA9AUYuagWt0yjOJl9-AG3QMsCO8u-kwDUtBjJ6ilP_w9b59eTGOYUJYX7V9iSMLdKR5sVwqU6l3M_H_CHaq88psSCpIrqs3FvMeDIW_Yk6kPvGYVCRGzWz4RIZ3zr8ym_7XCVoS32QAm_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسین ابرقویی مدافع نیمکت نشین پرسپولیس دربازی روزگذشته بااستقلال خطاب به محمد عمری: مدافع چپ تیم استقلال خسته شده دریبلش بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fplTHEVAIzlQTQYGT1bg50d0RJ1K7Z8_bwxQz54-ivekQKLx3b3wncLyyMp4A2fQbduSG_LziRuAYggPg4r2pO3lweV6uCskdxIrhSKGkXhpidKUaXeKhvoRLTYGe3i5_ltANabTrIfbOb21x4MhPQabRj07Buani9DgCO-TUZ_iegEsxp_6HIGhDbpJIYm6y6hrqJP37V3i6EXBwcNWwIxyoe-PC4QZrVT9DU5lvk6c8sq9t3gwc5M0fm-g392e8Lv13-bCAbHUx7-b169az06C8Ak_wkocgHLMhVuP67c0KYI5uZpltAXlIrvcbMGonjC-xhM3RSMDou2joLbycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=keQa3yFKSFctQKFdK4-7hYOxTyUZLzaAnjsuBqSp1gWmwvZzC8PGe-J41oJwuyPK97eMrkmrALEchXaf9HNcMsCRdqV_GEc7bKxBQJqSvM0ICC8Nu3M0Vl5axBqdlY6AZRxo-y0bqgpwNOYRVVt8CAyFEkpPGr6GxFNdZWp0In3pXjbjvl_bfXSojLgQhRnSHd8rmn2CKrBSUU0eJhfyIN3K-NvKLjPnlZLz-Nl2KIPKGyWzh2rdOZXMty1aOoUb3QxznDxObu1DJ0hrW7NAFO0_n1EB6krhs_627gsr4A24F0pTAssESu_VEM4vi2rmL11JFGooQ4G0AChfclXG6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=keQa3yFKSFctQKFdK4-7hYOxTyUZLzaAnjsuBqSp1gWmwvZzC8PGe-J41oJwuyPK97eMrkmrALEchXaf9HNcMsCRdqV_GEc7bKxBQJqSvM0ICC8Nu3M0Vl5axBqdlY6AZRxo-y0bqgpwNOYRVVt8CAyFEkpPGr6GxFNdZWp0In3pXjbjvl_bfXSojLgQhRnSHd8rmn2CKrBSUU0eJhfyIN3K-NvKLjPnlZLz-Nl2KIPKGyWzh2rdOZXMty1aOoUb3QxznDxObu1DJ0hrW7NAFO0_n1EB6krhs_627gsr4A24F0pTAssESu_VEM4vi2rmL11JFGooQ4G0AChfclXG6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMiFsZQyfvL1OZ5qO4JnENSns-zdoK8pgmN6pW6b5-5t6FRbNv--lBJuB6jdkAaVolSDTFUWAimpcoYjyp_3musWMgBGt55jT8AvOv4wlnGwKKSgn0M8XjzNZ2_tpj3O2FglBatsfr-Uq7XDuscrp8u4us-7JS9mQ_BoIXgjZ4aV6vbX1Vgu_lSDcYvxkQ7yrYFvMQ-8Wcf5s6sNRyCPHWsAB_twCh35A18BHZZETU-RJcUSZ3pmZLMCjPxTIGVNVqNlLnrgFRXZCA_97-FUMVEK2tRre0RQFvzdRk6HwDsU-49o0_FahFjLMiZNEo3Ka3qLdNBv-2BvFfhsE7Zydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsB5rDqvM6mPXBv79oA3PJV_BZ10xQ9hkJDFwoHDr9CC7MQgJXhWVvn1ZRIE-lg3gtNej6V4gA6eevtnDijX88vMQ-DHxX9Y1g4BpH_RBtSec2JfuMFkfLcO1CB4jbVvwmIU9TdEESq5CuJqFxF2UK49l9lJPJgDfm0RywesfvFSiBwJNyl7esl0qKfI1x0ZjKqYm7I_tynFeLeTSYVc0rmprVLgDQziNzypCOgdjHCHIqkaOfgpo1moVjBlm8Wj58Si-tHI48zU5on-hbQH84e5nlpVffrURuePs9z5l1gdTobdblrkjAR_HE4jHA-Z4QEB3Q5M7OKA2GQE5zuNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaeaNSdu07hQp5luLzDsvj7nuUo24ul9IPNd2Xha2VfySiYkTtV5tr4hQ95zjZ39fz0Bg-Fs9k04b1e1qz0EVpquq9gtzU2V3fWS_gzVxyFR74rS0NAQYaR8DKadJE31K1m0sppbUJ1dYyvuQPQkiv2xxmBsQFLErmWgVFk_8X8BTnPMApAdpKvnafuN9HTjYuGrJQx_MqrPBQTnce_VUvCVo82wJLOF-H7R6-VXLS-cB-R9EJviT6WWmf6j_Vv913CVP0a1TrLhmxCMltPbiYXeAArFLa20jizz2MAVQ-ai4a4iR85iYd6tYVz6odPjUCl3wWKXfMBW6wLYQBvHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bys0cIhIe_7kvqxHXELckSqn4Qv1Y8VblVh_XJX6zqeqMJCA5HfYrtY6raxwnLLFAXeoHzINhqETjqUjKIepXzEQ5W4VWagtAzEgVIVQDyCi_XwTomFDsvjwyA10an_LOi3DN4CNn6O8AmgVYmocT-YXZ0UXERurKO3-tvg49XrVryV1IT1UP_19AbVm6ze4qEr6UAYIoGgM2gRHBO3qXu3JsE6BKk1Nm9u8bbqcOzYVyqt8JvFTh0lO0hNBy24rW9RRhK_R72InRLR401ZDw4Anww9zARaTjhVqR6aF6qTFZtr2ozdr4YTwEwX5QtYMnC1yRGCXcTPvyaRIeVaIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=Lqz_9sjV5USwVUVvO0fBZvZIbtIgLD9bVXlTZ8-xXYVYS1TfvgWJjvjnYJjONM83PyRXReh4vE5MOij8kAa1XEBecLa_pMm_OEYXUVf-GrVqj36T6WqPwJCQmc9-6RSImFNCvXb3qKrW8jSsYtw0I3hDenPJ9UsGA1C1WDo4EioEItpY8vkv2b7Y_hCUYcjswUeluDbfKi6VxU-fGki2mXYRBhR68QEuFdWFwGbDaiumqzak_6mrkvXq_-wU8h_E38zxlvNuWKNjTsq7F6m7H0anQmluIykJeKljoeMY3xvIm7fCgIv3JjPlL7rO4qUbxInAgq0CS9rovf00BopgKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=Lqz_9sjV5USwVUVvO0fBZvZIbtIgLD9bVXlTZ8-xXYVYS1TfvgWJjvjnYJjONM83PyRXReh4vE5MOij8kAa1XEBecLa_pMm_OEYXUVf-GrVqj36T6WqPwJCQmc9-6RSImFNCvXb3qKrW8jSsYtw0I3hDenPJ9UsGA1C1WDo4EioEItpY8vkv2b7Y_hCUYcjswUeluDbfKi6VxU-fGki2mXYRBhR68QEuFdWFwGbDaiumqzak_6mrkvXq_-wU8h_E38zxlvNuWKNjTsq7F6m7H0anQmluIykJeKljoeMY3xvIm7fCgIv3JjPlL7rO4qUbxInAgq0CS9rovf00BopgKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=JDKD4dm2O91UUGaKPnesW9UIITAjOPVlLsmJBcAYLNWA1osrKHqaPAC_91wayNXDRiOI-56G0eD3RSfb9affswhCR93AVCJmHj3l7nNyXAQfBJMfAWQiA1Y9fQT-A-GHd01oVk4VAKxFcaQl-so_YgrNpxHaatzTdSyhEiWvXjV4ht0_vqbt_JivoRjDu5gCRG-dzBRxkY1zLXn9wnnaHEFK2TK8F3GInpScvkKWnTuTMZv-YT8vUGOkCF-fm5FW_sL-zwlLk9MgjMbdqJqj8KU9rSmDx5Fto5Pza1HgSDY7n97B-_c7Pwrf9sZigOG8Jl7dhOOR-tCNn48eGu2o-C-LeQ_PH173T_W7NRBjKU5jon5pz_ea182bYQrbGnqPIJYavkakVH0WwnVScmG7C8s3gDKPtwQlWpP2GPTGaniAZqTJXHdmonPavlYwvNe7v0mRFl-TIH0ha6x9fJRCYDUMeJ0ftH0HEEOw0V0zjO8zhZqT6hc-hSBVbrGJ118yk1PpWGPTU926a327tXw_Z7iqrVtST9fT3qFUUePYMwK9e6SCa0-b9gVgLw-mgQTAGDPd4uHEPPrY9ah6f07iq4uFzevwGu-C1SZ2oktcAwRxlA6e8PJ_6ncj1lsruL5Ryrj0knDP39XQtcjDyUjtzfdMVwSsyWHgOED88O3kdaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=JDKD4dm2O91UUGaKPnesW9UIITAjOPVlLsmJBcAYLNWA1osrKHqaPAC_91wayNXDRiOI-56G0eD3RSfb9affswhCR93AVCJmHj3l7nNyXAQfBJMfAWQiA1Y9fQT-A-GHd01oVk4VAKxFcaQl-so_YgrNpxHaatzTdSyhEiWvXjV4ht0_vqbt_JivoRjDu5gCRG-dzBRxkY1zLXn9wnnaHEFK2TK8F3GInpScvkKWnTuTMZv-YT8vUGOkCF-fm5FW_sL-zwlLk9MgjMbdqJqj8KU9rSmDx5Fto5Pza1HgSDY7n97B-_c7Pwrf9sZigOG8Jl7dhOOR-tCNn48eGu2o-C-LeQ_PH173T_W7NRBjKU5jon5pz_ea182bYQrbGnqPIJYavkakVH0WwnVScmG7C8s3gDKPtwQlWpP2GPTGaniAZqTJXHdmonPavlYwvNe7v0mRFl-TIH0ha6x9fJRCYDUMeJ0ftH0HEEOw0V0zjO8zhZqT6hc-hSBVbrGJ118yk1PpWGPTU926a327tXw_Z7iqrVtST9fT3qFUUePYMwK9e6SCa0-b9gVgLw-mgQTAGDPd4uHEPPrY9ah6f07iq4uFzevwGu-C1SZ2oktcAwRxlA6e8PJ_6ncj1lsruL5Ryrj0knDP39XQtcjDyUjtzfdMVwSsyWHgOED88O3kdaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvihPiSxskm_r1OlBRp3qYynYqxUFhryGbbnYJu4jnDvY-af9S9PSybeZPHG6-2E2DtJyvVl_xFNXQxqYu7CmC7fk6u_4a2cJmflSyr_MlfpoS72X328OuJ75_C45SufhOtZAwkV24iMuklJnhBKH60YgO8t6bLOOvOsNyyEDh7hf7MaA_fSYX8cldp498wCrtn02jUR92wwW2lGHd2oRZUjhZj4TgTMN80f66OtufOyD0rRVNlr6qsxVGFdD3jtB9XcQ6aApChEghUj8n9kSGChR7-TuGYDc3jQs6_PRv5T4UKXQ4jeVlZNkk5TjLE2d_yGl-0Ju5YCduxMyKImYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8TXJf3ZFMgc9jhbqyTyMME5tYAEJ-gMUf3wqEQThL1Vwl5n-y59qtM3UwrgXPcD-t-IVibun2sfYcrT9tnZNyPcUSy3ub4-wVptBxZlD2L-s-1cl6zSlreTqmje5vh1PYNvDNLN8HYK3QOTJi8BrjdLlnAxkbccH__BgA0ejpfWEpgGpFNS9gg-b0n5po8Psj9ceWUD2SOxlupvJ_L6RfyCDByt-Sgxw5cLN8emgeZCTESB088fqULT5CwmuhwKhDJ-XCPWmNZbaG_pi5ZzIVNahTKG-t0hE892WB6g92dAAQ4o6U4RKWZZEuH8o-CrVMqZGqJ5dA-3C5wbptTEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=hJu5jAPjNLy5RXlLx0nf9-DaRq9HYOiQSeEs0t2oJtIWvSZvWkPJJJy0eldZ-U8A1jlbzNBMiabIUjC07GKnkKzHo2ekdLEE9r-TVxPpFe0TLCQi0xM1hsrXvjLF0KX7n0kj6lfS1fLYI4pacIZ6qJwBl9oEneDXPwPgOECsZryPFQnKr5TyqG9U_xoNUjyiqxgCep-i6PqWG2IVbXTOFKi6Lq7xxbyGLFZRu9NK9hT7-lwts5vCTXAp_X4F4_4HSoWNptmdFgiGzYhFUCbEN9qELJUMhdR2VdZ0kV2fGYUNABcQ8TBOsXPq-dSi0eiiWBEZHFw1wAVsmykZsV6MD7TH2jHezM2Bg0Oo4El7tVuqntua3BsmyJSKS2sAIGrdhnutjHDqRNiZ8Yr95kT0ip7G9tbc9a0E3pu8YyMpFB1ynyX_Y-jXMvNZCXI8eYpwZNqYGHBLXRXFtpC1EYfxl3k8rIaCozpAH2Om02VbF_EF1acDTdDqhLhCL6MdiORMgiitew-UrKfIgPe7sO3X3ECY2HGCnKl4oxECl-gZIoHgu69UPvJCb-ti0cfPgsi1tzCBntcdXAoWd_1ltExGy3s212QjFwWLCMlaxJGdEBwg-V0U3O3ROGfza8uqwVANQ9p-vD5ng4nYmLFmWe-4lFBHGPv6_aP3P57d_DKTkTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=hJu5jAPjNLy5RXlLx0nf9-DaRq9HYOiQSeEs0t2oJtIWvSZvWkPJJJy0eldZ-U8A1jlbzNBMiabIUjC07GKnkKzHo2ekdLEE9r-TVxPpFe0TLCQi0xM1hsrXvjLF0KX7n0kj6lfS1fLYI4pacIZ6qJwBl9oEneDXPwPgOECsZryPFQnKr5TyqG9U_xoNUjyiqxgCep-i6PqWG2IVbXTOFKi6Lq7xxbyGLFZRu9NK9hT7-lwts5vCTXAp_X4F4_4HSoWNptmdFgiGzYhFUCbEN9qELJUMhdR2VdZ0kV2fGYUNABcQ8TBOsXPq-dSi0eiiWBEZHFw1wAVsmykZsV6MD7TH2jHezM2Bg0Oo4El7tVuqntua3BsmyJSKS2sAIGrdhnutjHDqRNiZ8Yr95kT0ip7G9tbc9a0E3pu8YyMpFB1ynyX_Y-jXMvNZCXI8eYpwZNqYGHBLXRXFtpC1EYfxl3k8rIaCozpAH2Om02VbF_EF1acDTdDqhLhCL6MdiORMgiitew-UrKfIgPe7sO3X3ECY2HGCnKl4oxECl-gZIoHgu69UPvJCb-ti0cfPgsi1tzCBntcdXAoWd_1ltExGy3s212QjFwWLCMlaxJGdEBwg-V0U3O3ROGfza8uqwVANQ9p-vD5ng4nYmLFmWe-4lFBHGPv6_aP3P57d_DKTkTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQHnNc_3cDoT-tIa5yPPHv8hUfrO_6Ew_0zieMPIFZu_w4nYMV162Nqw6ynQHaCrq_DhK65gG7gNR42LW3xBaapZLXYeoQvd05GDOitd83NrQjDvHc6jMF9NHtl61JV1lC5NruOb7zUjqkl49g2URAasdFXpU-v9kHK5e_IN3eA1DicTsqARt8fnY2M_sZJ0EGtAxA5HKxsghKfIh4hAL_F9Iv7qgoLBmKRMZlRay3-PJl_7D0d2pMdbJCL3oMy6ZClZIfGgM1OdnqzQAl5oFkDLhTuXL_yPXjgGLxVKTnti3ygbRYTKPV0FcI6VR2hmo1svNp2K0JIkLMh0iyAnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbvrz1-P2BRm12C5VoB9XItKnLNHLCPJC4qzNV4bK3OUHMJ2Pi7uaFZVsIBe0eBe8GCMh68vvSQ2jN9QEb8XFSuu-KXMBzLZCFdxVyjw4eU_LIc6hsQuPmXjPXOI1q4I8Hz9d_87KDSMYQ8GpH7aGFQwWtWCh28FTsAKV0InOWGnuUbyUfhiFwhwsRL0dtyx8wgj29HvCN9aRtb9PcTARB-UJy2uItUepCGAK9viSO2U21qzbujj2mTbeT3oKMUDCTJtKqP63OJ_RuCEJ6fZE9MVq8vmTTtEfjEGt1B8Tg9gx0146a1AW0TsnojdSfa1K-h7tOwduskryLMtab-20g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uByG2HbSbNHEEK55kTzgwbgTZW8iOa8e1hMhldVgUfC3qJnbbZDivuG7r9gQgLU9BNTU7wls2Xmq6MK_oqj9ggbA84hbrA0TJ1MusPH5XI4Bgc_xESvG5ggDii-6WLNPSr3c_1rkCd_Y-kA1mzQhxRuWw1LMJPj7_2UZ1KsAVeLKNdm5WB1rB5ozWrThUSp-PaRa5q2-10Gt1KrGwNjVBbsXpGK0aNxJZKucdwHB5do3z_iWeggdU1ITOniaUeuVDtgJLTuGFf8GH3tT6E3vvNi1RrKGpK8BXJQ513zVJuFVMeFaw1TLcE8I_rX4XTejv_bYr6gpbgIjUZFDCOzf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqoSQe1RpaeSmewKymGhEqoArWggHuQXagxRvybhnfpiFGjX5p8vSkoK6pdB3EdZBOthv0idSSJaNh-jf32xWIUa4-ktaFV3I4CObC2m4JU6q2Jd_ol_p_4KKWnj9uZN6XeS0GoohLLT2AACiPW5jd7B0NzRaNIMxZyP2xUxiIeJaWOu0q-Qf7Kb__dXy3PZZwPGttJbobBjLeR7Vb6iq-RayJUaQ-VIpoI3I3tuYEM1jgwr_BFNik3J008sAQgxbDbxxJyRvaUhAM9yWwR35fMN90kOXlXD5bbzOWzjbyiY1grOEujVYoLei40Las5oDtev1pTt4lAecE0hTSnqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VO7hghxkNFJcK5egroauRZIkebyC0Brp53X0vLlRPLA7aFjJI27Y2rRY111IFiCVc9SEMzwK_JAWIAIjAV4a9Qs5_36Qw2YhuttFrds5QTUuboZsDUsxDWD9mHAJI4DQqv1k_3XF7yOk3B2npBZDPtEYu1PssvM-cx8LjWe4vJY5vJV16w63g-xM48HNs0EA22BmsT7skMwZcFz9xfNMolkgJ8ZiVejFLtwCWoBIjLPhrjTQh7E3dcDbQWGJeLIcOG0u36SM2QaPbuPniEKY9eUGpZTc7dqz4sAutPep0g1LZZ8837gozZQpvPUqdvXI284uWYu0c0lx3DyXWcYnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD0wc7rUlEw-exCxu4cU-7xmUlPqc0VyDfHAB4j6N8YzGIr3jy3OPOhC5E9-Mcze0Y_rxLd4Kq_odvn3fkl4ehfBl-9g8mJIYm_fVGfdTYcrJL0dhEF0aq7TkZIqp2k-Hrqp6IimKVAsY0hw9_tXHkduvan_wcO5LaoL9ojni8IaIkHN6PcV1Ea6vQ3MCc0cfleh2WEewP7IzvT50I_Ih_1VYEDx0M5XpwhrGuLj-6gQKFVjfgVI8wCnzRKMFjcNTXGQ5yPbc0RoreU6Yd-T0lTe9UTjw8xOm8OcnI0QeH07Fkdft1LsWSbPi7OMACBGD3v7pOtFVSU_jli26r6qtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbAytpj1BSxK9UP7LccC-Y6BscreegBYZCm45P-7hqkSqKRPYjpqI5LDL37sA-UrB5QPApPdVGZOr0qaet9_qhrhXzgDeGm6qMD4DjBjiBrzM6QFY84onzGV71HlyAsvBd8w2x1Pn9NsSrxazoAJuSORbH_afa9X4CAgtj2EkGCvMHYAqFQ-etqfMr2Z-gRgfeEDepkD5uOotp9HVKjf4Y5GNClxIPZgMhE7EozOUX0hgzoUhS1mFj8mh0bL5ExKSG_c88IJGDEboFif17JKapuGe0DyqQzITv0OkZ_wi8w2t-Kf7dDYNOwitgsB4XeVb2aAbneYPERgQct1xgqR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdoY3ObTdYn9pY85j16bJMxxI90EKDfTtjtwhc_DUXzKKmgaI6euFh2dRMJ01-OysC_sWNr-7iXpxuyvxwfOiKhNHAp5weTdoPzlkaY51f4p_Wj6ioIJimhv446j9uFssn2jdT8lBR0NNOz_Gt65HYWAQ-_BSyJOj6l7I0QDgfCIIyFleQlZ7QDf1zVkA_15OiIuJp2eSQ4mJUxfgdQA515M6J2l7eJGb45X4RdeS5OkDzXG0XgGxDGCv__8zjkdvFl1KsaKv0mZP90nIFdB13122sj4FOdVRlZne39M9AvAkLWfuzKRxCte67PWo7CMjqwO2ikHa_wEZmRmDZddyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdL5Ddg4JagX1x7aj1G0Rrlw70rUnUJobA2AuOy837mgco203Gq2jwmhUb2FAVzK0CKqpp5Cmnigj6Ml-Y8-s5yn05v3ednuQuX9AFoW2_hjBPwV4rsS5rHn53DDfX5IskfCd27VGL1rol153mp6DHd9dy1koI_CkV4WheXhawQfPKA7Ge2q7uoqNHHqPFiK74QQDmPHjwKZO--oFU67htwoZXjc8wyexmskmt0--vES_-lTE1GGzD8LJVDHPczC5QbHcGidghAvMr8YLOxcFrOpVz1IbhNG7Fyqrz2m0pkq8nAdpUGCFb8n3dkVgtpeee-Q-FezKjNZJjddsb4q3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI9vSrNw6AFsNtnXdJemHD9W1mGQVjDcavDoLwir-XPUFCYJ3GH1bdaVJINt_OOvphCbstAYIKZZm0nPMYiEZUb7LabGb0NN_ckmUNGr06iTMm5dpy98cdBNdUgt3EIBIsm1EzdI1pt79eckzM3fP83liWX9lQ6zIQiRILIYY4dbL-m6EZ6AdIWBRYzgBmDU4cltgL69rLzB1I0qD8KDzaU6tHxxKwV0L1TPpGjaCJO5h_0fl-D5BrQQrBkP_9rzQAGw1us1ehneWXRZKcjIIAEfJt2lz-LK04Q62vQ2OgMfcKlBVrZqOsQ__uK8KJKlcRK5ai2WEadrjbUOl6nJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTh3v1nZjRV-pJgPyFZMe3us_buE7nOHy3pYc458YJo48W1Sdfvd0KIHhrPpj_h_u9NZvgfEOkfN3RsH82z-rW2PXgxbVcYmzmL-O-8f95dMWdIex0RZ5neThteKbot9QxIzlbBYX77Xqib7KEI4C-kad7S8UndLzdi2QbyolDk3EWDRH7cLZcgD5Osj3FF1__tYl0Ys5wXtxzWF3X4oscVGlD9oTAU79zHu66VriH_8VrBXn7OUXWMIKr5oUwKvwmKe3qCf8sKZsDqzPn4yfYJYuPJKFTT3PZrKhCayzAOpq0fCd0HB872l_gw8dq-itkzmClYMivH7_MJH65UZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=OHQ76ebOxeMk8zuLYt1dUCQZORCb5vutbl__kshvWSEjPq8QHmxLSCRVIOiVIyKChmMy8wUmWn6CVPcljlekY44kCWfbTs_ex4zp144c_LYjMeRovnpFXI3rEIV-3B75KS1sQ_ViKubJChB891I3fbSqHalvKeqSa26wh257Kcwb10h8csgcFErTNOKKa4CwbiS5umO2z6ZsQU2e2-_W81o78IIfY3cBqeUobJ6ZM4y9Ma3nJvNWng3VIrWDmXDCAqliT4sUUabjwOwXAUoEP1d6zg67BSMI4IqUgWNh0fZ0a4cXX_ghbFPi4po9KGVk_qFNiZ39pwKPqCKYqkGujQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=OHQ76ebOxeMk8zuLYt1dUCQZORCb5vutbl__kshvWSEjPq8QHmxLSCRVIOiVIyKChmMy8wUmWn6CVPcljlekY44kCWfbTs_ex4zp144c_LYjMeRovnpFXI3rEIV-3B75KS1sQ_ViKubJChB891I3fbSqHalvKeqSa26wh257Kcwb10h8csgcFErTNOKKa4CwbiS5umO2z6ZsQU2e2-_W81o78IIfY3cBqeUobJ6ZM4y9Ma3nJvNWng3VIrWDmXDCAqliT4sUUabjwOwXAUoEP1d6zg67BSMI4IqUgWNh0fZ0a4cXX_ghbFPi4po9KGVk_qFNiZ39pwKPqCKYqkGujQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری جنجالی از بازی امروز پرسپولیس و استقلال در گیرس عجیب بازیکنان دو تیم که منجر که خونریزی گردن عارف آقاسی مدافع آبی‌ها شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buG00jZKMKKpaMqIkeNwrj6KqH52G3YnNtKkfA9O0FR6x-jNK3nkKCpjvs-paOMl88R4Y4byGr0uE33EgwvKmqVsHvs-xPH5WnTcH9dylGvYtvkWqjdFhSX5r5x5u8fnpwDqRPq0dcorSzP6HXG-lPMWlZltLaPqAfPwZI3h0B_BXztuPTJj7SSmNyq7EfQDgl-o__uyuaYT8WTN1IJWcOJNluwGWmq0wbpsiUEqDnTAD7wbnZTU0GrsIZtm4QymmWey4MV4w1KxfG0VGq-36KERScSQKeP3d9v0tUc-CPSIrgb1Q07WnKCNXB7krSzahmngLzb2CVTuWL5vJyl7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=pB4InVg-xQ1gbCD-KJdeUf2VErK1TrdOuyO6CHY_I2q2hueOQ0T8bB0tCaXG4-aV_-tAGEIswVeGn3Tz2q6sdZ7_62Yb0rnca52vvC4eTI1TF53NxjqhFBLUoJ9i8ThDlms-kwEaxDXwoE6BIolX7Vj8mhr2_eMOpMSROslMsqD0REFKmmet30klS2RWPeGXsR07vN3F0Hy8O9pNlOiCEDk8ior8nNyDFTclELZ9VAqfBbVVvsWVmyG_ZxjogC5PEFaGw7Cls0yLoaNZE-VSo0xGGrwUmJnE7UPuA87QdLHeAH90jy86hIQEblcZvwcck3r8kUJYl6MyTlkBnfIa3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=pB4InVg-xQ1gbCD-KJdeUf2VErK1TrdOuyO6CHY_I2q2hueOQ0T8bB0tCaXG4-aV_-tAGEIswVeGn3Tz2q6sdZ7_62Yb0rnca52vvC4eTI1TF53NxjqhFBLUoJ9i8ThDlms-kwEaxDXwoE6BIolX7Vj8mhr2_eMOpMSROslMsqD0REFKmmet30klS2RWPeGXsR07vN3F0Hy8O9pNlOiCEDk8ior8nNyDFTclELZ9VAqfBbVVvsWVmyG_ZxjogC5PEFaGw7Cls0yLoaNZE-VSo0xGGrwUmJnE7UPuA87QdLHeAH90jy86hIQEblcZvwcck3r8kUJYl6MyTlkBnfIa3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDQZEmN_yfyyXYsE6-uL1pQHJa5tSkRBRfTKlGitlzXK-ZjlqITt9cX4snFienCRV3Rvi2rq_Q08vh74wTHxrZM3tluUSpuWYAk9SSQva3Y-u0cYxZsVQygYDubbvkAXKXlIEcbpzCw1rcGBANMLd6yY-45jtWVE84JZDyrLA6phuIFbCq51im4E8z6GqaIDlKn7DN4iyyoDX8zMaAfDnT4z6h8t_9xSqkAKijvHjWJtK88jEMltg5IRcQogTJOXNIyUT4Znu_8jdgaw6nLroW-E6rqjkR8LUy5VYxlYrHjfSwuBS3O7tB9mxSy3gNMeAfKeHzB2YgZ_5C5yHhBcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhpHx1ue_cyPwYDZ2qlggL__-F57e9iF1ZC5UaL9ZHp_9pQU4x2eDNQoTskgW_Q7Ghs7jJYRRs6j_Vfl7bCjOt5rblyC8MAq2baiUgLDMmIoLfDnCCjfNTpOsZNLOvibHSWQFuX9sZylvMAkHwmI3sptZHz-jVts94SEoqf25bd1tYixm9wEhH-mnTRNcUloA8N4XVzpULV4Paui1oW_AgZmxHs6i0uZjIx_JggHluFdqed8AuW6i4jyT3f3em0CAaNhXdLH6iJYrXOXNZ2fI-iKLoaJjyeyOd6xLrfkAErcC8j-2vuV37iCbnj_TT00BrGLLJ54Z7yRm5FcPjb_6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIxjUA9evoySug9jP6_Cpv4PKPwVBRZJ1FWDxgVvfEvE9dSnQ7pDEjb_XknxnoLjhgiCVs4pUjzYAgy9RWnHfzfcFMhw92F7OX968TrAaKazRxVKSVqfZIm_p9GMHe4N7ytdnTs3tBHpyOH63RJnRsbcu8C0i5rR_KSuvxd4kHJH0vK2riFfFDsUovxBJMkyCnU0aD2miQAs1etTQZZl0KPKspjXk4o7U9kSEXfhkcgwCif1j1f9bJjPCKkGXJ8txhUstsuQCC86fhWGaygk8zw4T9GWAE3Bzq-RCL876gyKuYEj_cbXKG6095touVTPc9SCy3pcUCcZmaFu4hOYIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX56higOHRN_KCW-oIDsPf4q3vjZZT2AFZXILWUyNMPaugJ9gvv2lzRcwKSrcMSW53w45YEhfHHJCurzjq3dmwdTGmVda56UJhjUXCMAS_xE9Uc1GP4P2RiiI4UrKOUNAyMgdSicNJnrSGbibPAxpQEV3fGz7EfcJDWy_ph5vZHxCK_LaSSmLEoLpfL0l2-SLDgNnE4Ao70aCBdsMi7IeY8qqZRl5_uRjBD2nUk9OjhuykeCcs-kEPP9Vo3DdhsEwA7i_PvuA9Kc8Guurg64QdOh6R3WbI3LxzTysoCHEOTnJcB3YYmntOf8Js7wlOC77EKM8rTB3aEL77vPKG0fGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozOG6CJFd3MRNeQ0jnBm1PJdE8FMZkRe8TuQtZaP8bxDinwlQkEnwu-KzJk0EGYKA3LudbBGM1_6RXhMEyxvZOJa-FRoYzC-IdqDaNY_1AtmdXkQuNa76gqKfEbQIG2hugSXGyq64VerimnjAIaWxPA10DB_fZTSv_FZL0_n05ph_x2EgR-dgGaA1XpcKJ6UjHY3xDMesgSaiqM5RcUDMXoyJZIrC3e8SOSQ7NvqBS8i1LI9Ql4JFhps0RSB7yVpEj3nPv8N4erK9T4rMbgD7ZJtm_W_Mjlh0diF7CuDA7JRCZ8KixO5PB45SzNAchHJhhyDYaBB13DmfkonXpGoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=t_5NApPdTUGxlTHdNVWkw8GJpAV4l3qL3Nu1zUbvTEN5cQOEMJcLMNGti25fqbk6I6cp0fvDUA5X6TPZQsgqUBFph3LwFGjogbUfyX0kMTmiPnKh9RyPxzJxzPiLJxb09teVWfY85OXeAHojO2uPhuJdrIW53w7z0RZmA6ST9co7Pd0XKGTwi_XG4UQMda2rYsaWuWO8PucDbKO1xfp3S7SWggsmmfwRmnAr4u_nC27NPMyusawUHqlwoShoOtuuqvX1xwyqaLlBHBzYRBs6a-i8Ms84Pkuhq9WxWh9ilT1gR7YJ_Q_LklJVpuyS0qJsaPK1h1YBXYwkvUKbI0Sqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=t_5NApPdTUGxlTHdNVWkw8GJpAV4l3qL3Nu1zUbvTEN5cQOEMJcLMNGti25fqbk6I6cp0fvDUA5X6TPZQsgqUBFph3LwFGjogbUfyX0kMTmiPnKh9RyPxzJxzPiLJxb09teVWfY85OXeAHojO2uPhuJdrIW53w7z0RZmA6ST9co7Pd0XKGTwi_XG4UQMda2rYsaWuWO8PucDbKO1xfp3S7SWggsmmfwRmnAr4u_nC27NPMyusawUHqlwoShoOtuuqvX1xwyqaLlBHBzYRBs6a-i8Ms84Pkuhq9WxWh9ilT1gR7YJ_Q_LklJVpuyS0qJsaPK1h1YBXYwkvUKbI0Sqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
