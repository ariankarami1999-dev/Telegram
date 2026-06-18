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
<img src="https://cdn4.telesco.pe/file/hIuGvJSyWv7e0pfT0duJG5ZKbWz1UJ47rSzSkhdTTafNlcq2NCdhPlaoyoqxJiAXGfzuKj1hBWkBhNkPAshTSIJ-OJG8Gb_zWzKs3RGUXoOaeZGpugzuAECazilHsIaZN0GKqFWD2pSKdib8O_p9_7aNnJ_iaQg_YvoeOnqGjd91c4ixQEzSzZ5SO4n9YOlUolfJmODdHo-Xn1eJ-lCO5l-FfI9SCp4QCLdvSMKM4DQJCQoVY49wPhYm8cXRqqdj4THEGDCMOUATxBeu3EwZpE3zj5OsVUI5s6la5TwL_iATw302ssiPoY-wUwYjfxmnzp0deFimXp43qg3IQVsXfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=MK8nQH1OIYmj_2DOSI4QGOEqTN-2izHtnEPY92uDptApHNV03XKQhdSdxsHdzPOrGWMzOtpapbYM_2osqa6GQFlqBcbGJbB7db9COQfHIkq1OBG429ZWfAl6utwZ3U1lyhgjBrM5j7qIGL2tf3yAGREr-DoaZqIvy2r4xwAkHkDFsUX5rYbvzLKk8yGr09FsMwYfzb-XiaDtLZZKy5Nb0wtoJSGK1e1GHyFaecNf1V7VTozeV4B05prVGsXmK-oHQ5Tqzv5qo7o5OYSZMpL2it2ThvYay5JoKm1JPbvtFgUogv-YU0DVfceKXcgvtti3i_JTeyB9b6O_hVGQy7kvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=MK8nQH1OIYmj_2DOSI4QGOEqTN-2izHtnEPY92uDptApHNV03XKQhdSdxsHdzPOrGWMzOtpapbYM_2osqa6GQFlqBcbGJbB7db9COQfHIkq1OBG429ZWfAl6utwZ3U1lyhgjBrM5j7qIGL2tf3yAGREr-DoaZqIvy2r4xwAkHkDFsUX5rYbvzLKk8yGr09FsMwYfzb-XiaDtLZZKy5Nb0wtoJSGK1e1GHyFaecNf1V7VTozeV4B05prVGsXmK-oHQ5Tqzv5qo7o5OYSZMpL2it2ThvYay5JoKm1JPbvtFgUogv-YU0DVfceKXcgvtti3i_JTeyB9b6O_hVGQy7kvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw872ibYpjMJoSRZEuRV5LmU_jErSt1HQn0mGTvFhYwF78SHm7x-rVvyrl3doHMNn2mXmEIVr_Escqys5s0LVeg3Mo-cVgfz50UcT4TSP5JUN-Z5I_h-xb4nAMrc2D2dVJjrd2zNnnZZnBONPLjJHVZjEhFNWF2mxLTEV69KXkzLIQ4dO5FyIl9teE_mVIaD-F-4tnoQqNCtefRYY2N3tgVHOJC1MFh6Kc_MRJTXZH2F2RyQREuFC9tVtCgf3WdesSzBHcMik6taKSTEpeYocmhpNM9OdaziP6e75MMNGDGREE-UWgtlwPHxKL7ov6wsARSehdKeLT8B2vgmXJzWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLgi1N-_1djW0HHzwd3kZ3WU4mIBG5kPplN35-CH9DTx6l_o1mJZpKa-MQyTj2h6jFnYr4PRk3vK-pxGJK1GPR8NTd7yFE0JpqtQGK5rqIDP65uNZUf2CAeJD38ogV6EXGglfwJESnr0_rsYLH5mBhH0Ym9d4Nd3b7JwlpNmK9nVRHTwxjaPC5E2AhNfBbaAnxFvM5fJ0_DfFMCnxUY1xPIuhXjdmRM0Id35DR0MeqtHJAWgrYNQ0KjrGfFo24jNvKpKQ_kKqrY_rbTQOLSOyIlrRaRtrKxqeDGmYNDe-kH6NDov-XaRhGIyFQ3O1PPMuIjoiZwteS7y-6oNt7R3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZUv8dTG9ngk2piIBTJbnZQ7taen2jP-TTHzhSdAvtLWUYhMbf0OKMhplwudhckKNs-45VRqCjr5WkP-GHHIBguCGZP6gPqjGk4xkAe_nh4evq3MrN7KhQmQmInuC_L1S6UtB1aBPR8wEUIfbIladax6bE2t9i9UPYxQeBvEKVpOvQW8N-wIod7YYKnJRS-7uosZiircEemgfmon9eIdNABcfVXjnS0iU4snoy_XyyybBhW1stvW2HZRlxVCJvAWfQoSpvLRAXhsFKQEqzg5phQvyq-f4F6Z_7foNUJAKx4vFhQsGuzVJDlEM5LVBd-IXlq-ntavyuB17XauwtUmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=Oox6I3GNtMkCy4biwbIjycAJFAmF-z5NwHs1aiDwAHw_L9Wp3qRU3DIhc4K3fA47ZEoRwfIgpkcPlEwOFzd50Qc6O453atqm9xvXIejaFaKLk_4qZh_xSDqLlc3wMJB7Wev_zV5ArTinj1rZp5yph2Q8gV0016eVps40QFOgc8ZZOTu9-WwvaqN-Q_70orMwyukJoCfSpbBP5NaLJCqSDdKpWAtz_2U_vBupkM2fHD3m6NLnCUdU5ARfGJybJxFsNscJHVeCX_h5V-z0ytjVlcnJTiwqXBjodI7rBnAafW7hFZnixCsL0HL4Lmcj2Hg2AdlSEJ8fYUKjG70ue8cq5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=Oox6I3GNtMkCy4biwbIjycAJFAmF-z5NwHs1aiDwAHw_L9Wp3qRU3DIhc4K3fA47ZEoRwfIgpkcPlEwOFzd50Qc6O453atqm9xvXIejaFaKLk_4qZh_xSDqLlc3wMJB7Wev_zV5ArTinj1rZp5yph2Q8gV0016eVps40QFOgc8ZZOTu9-WwvaqN-Q_70orMwyukJoCfSpbBP5NaLJCqSDdKpWAtz_2U_vBupkM2fHD3m6NLnCUdU5ARfGJybJxFsNscJHVeCX_h5V-z0ytjVlcnJTiwqXBjodI7rBnAafW7hFZnixCsL0HL4Lmcj2Hg2AdlSEJ8fYUKjG70ue8cq5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=smoRAa-ik6AL-anpBw0K-K7kGq4fh86ieKEPYPjbSL6B3vJtSU_jvzt04FWWf7tOhyBV1B-dYUvR6aRhQUNHUsDIpuDx_o4QT52f563nEWRETLRGouscImHAKldGGY_vrg7U-gmLVcUwUVCp8XqrQwX7Pxo076iuSDqhv2M-clJlWDRwLEkA57ZHmYY2o9TmsQISFvtk3gjk_yNjm34XgGFUsdDj-LwHDXx196_yr9S6Xm3O7Z9VIeLRBQcIfHRPIJfoiPdUI3bJzDQl6QQQd_H1iHP65u_LcysjINWb4ntpXFRZIehNwCQUlpOcJ5mOValx9rsjvgqSOE_0FHziMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=smoRAa-ik6AL-anpBw0K-K7kGq4fh86ieKEPYPjbSL6B3vJtSU_jvzt04FWWf7tOhyBV1B-dYUvR6aRhQUNHUsDIpuDx_o4QT52f563nEWRETLRGouscImHAKldGGY_vrg7U-gmLVcUwUVCp8XqrQwX7Pxo076iuSDqhv2M-clJlWDRwLEkA57ZHmYY2o9TmsQISFvtk3gjk_yNjm34XgGFUsdDj-LwHDXx196_yr9S6Xm3O7Z9VIeLRBQcIfHRPIJfoiPdUI3bJzDQl6QQQd_H1iHP65u_LcysjINWb4ntpXFRZIehNwCQUlpOcJ5mOValx9rsjvgqSOE_0FHziMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgGBba6OaRmlo_ftAL7LnLEzvBvwfningnMk2gWSkq5Ne0TDOQEHHqjTn7VSNt-G3Dml9WbYESg6Ga3-kNf_aaYkFXxLvkLlk2Cvfu_-RkvXZ1qBh9WPbPDG41aLaue2SVvwqxc2ySf7hzwVuMUhIw-ORQj5grfdCRAiv-gcjF6oyl4MkNNZ_hwCuuV32sFMEg_zsSPBUKpnjtYkrKhPmB483rBcDmPQznwpkQV55QbTZm66vJHkJ-TDAwTSPcGRvkE2nt5Kn4Vae3d8AXqcqFzTQ7W1ekgR6nUkkt3p8NbMDKSZyT74r9hWXElHyVeMhjxq8CIa42NQJom0k-Lzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=r30Vxe7y8o7N3VrRVu7LAP_wTc4fJZQQi4ZOrrh4l1yccF8rjCcfMnicARTfVX4M5EI21R0UC_U2E2QwliwgKoKs2ErUqxBNG6odgxEDUbo00mmboOsmdKOTRHKNYHx4kbz2gxiqh-tftpgC6kJS0XavJl3WmQYR6w-nCRFbLP2M4VEqMaIfC9qNU1Pe4BfAHQxZHq8ZsEvyVEnheKWWkJ33fcgOLt_jKAgk6kWfY_hhTOe9ygtIlD3em4crcqJDVB5PD6qxECJUmAW9yXkG3smX9lgqeK9_rh_uSoJO2CID2z8yf7PmZHE5nvfI-pEY9VgyOO1BKvlKxv9oPDY45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=r30Vxe7y8o7N3VrRVu7LAP_wTc4fJZQQi4ZOrrh4l1yccF8rjCcfMnicARTfVX4M5EI21R0UC_U2E2QwliwgKoKs2ErUqxBNG6odgxEDUbo00mmboOsmdKOTRHKNYHx4kbz2gxiqh-tftpgC6kJS0XavJl3WmQYR6w-nCRFbLP2M4VEqMaIfC9qNU1Pe4BfAHQxZHq8ZsEvyVEnheKWWkJ33fcgOLt_jKAgk6kWfY_hhTOe9ygtIlD3em4crcqJDVB5PD6qxECJUmAW9yXkG3smX9lgqeK9_rh_uSoJO2CID2z8yf7PmZHE5nvfI-pEY9VgyOO1BKvlKxv9oPDY45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=joR1uzloC7Lo0h7pYOySDEhNelCQfvoPTyFF3xWiXh6RQmPBq_gypfegU354kC0krhiKvesrEWeLDONV6nCdvO5mjd2d0iMdMm7ua99B_QXk_NcOTyjNU8nqXTUEtpEI3o7USKitJ9nk0wLQx0u2typdIh6JvL05ia5w6zuPrrD0bWi7SBTxrNOdUi4aJUOmHT_7DW6epmwOht4yZ-tezuAoeHTvgHCPNxarpz7ksemS0nUSqYhRvgmGilcyGxkOaWfd27qKjpLq-L4G2e39g0B0aHICZGk9IpE6-lNAtZysmyZkpNfI7VxzkfMTBWOcbF-KqT3rQOQKKj01eqYptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=joR1uzloC7Lo0h7pYOySDEhNelCQfvoPTyFF3xWiXh6RQmPBq_gypfegU354kC0krhiKvesrEWeLDONV6nCdvO5mjd2d0iMdMm7ua99B_QXk_NcOTyjNU8nqXTUEtpEI3o7USKitJ9nk0wLQx0u2typdIh6JvL05ia5w6zuPrrD0bWi7SBTxrNOdUi4aJUOmHT_7DW6epmwOht4yZ-tezuAoeHTvgHCPNxarpz7ksemS0nUSqYhRvgmGilcyGxkOaWfd27qKjpLq-L4G2e39g0B0aHICZGk9IpE6-lNAtZysmyZkpNfI7VxzkfMTBWOcbF-KqT3rQOQKKj01eqYptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=fVQ80bg3nn6ms4bj_gkHCv65704WVDpuIE4OK1QYB-TwqfyRB2YnHmz8YAqSEQdK7hv99TNu-twZN2fQvXOO2BfLiu5pz1W9wlpC4tWEzW0NIzKuezShKsS7FrSCh291W13SGMDjl-Mk_ohPmwTU_ef1SKfIPjV-3AN4NcqTlbPAJaDGYrhJOOZOJhMG4cyYSVuKBM0JU7dcdirqqruoLpZS4HMpuaomLT6kze0DIhMkwZKifv8KLHW3xzEpiKtKZ7HPaSjSPk4-4XYKnYu9j3nrJG4iBr4sCZ7vWfntNXsV7x-XsOcvHolUc8nGrtchyAw5KIasfsP89cAuqrjsuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=fVQ80bg3nn6ms4bj_gkHCv65704WVDpuIE4OK1QYB-TwqfyRB2YnHmz8YAqSEQdK7hv99TNu-twZN2fQvXOO2BfLiu5pz1W9wlpC4tWEzW0NIzKuezShKsS7FrSCh291W13SGMDjl-Mk_ohPmwTU_ef1SKfIPjV-3AN4NcqTlbPAJaDGYrhJOOZOJhMG4cyYSVuKBM0JU7dcdirqqruoLpZS4HMpuaomLT6kze0DIhMkwZKifv8KLHW3xzEpiKtKZ7HPaSjSPk4-4XYKnYu9j3nrJG4iBr4sCZ7vWfntNXsV7x-XsOcvHolUc8nGrtchyAw5KIasfsP89cAuqrjsuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=lEfrVQXeGv-RNJ6qcQUqE53NWscNb1RECFu_B-3zEZi1Lh1ET6xjRKuanIEZENapz_QhnxhAbJVkVP_Ek3vAf-fgFzIlfUQP2SzaElIDCmp29Wexr8OUA5WLLXZDmxNF0dqnTxJhorq4K0_dXJF-SYwGmRljVzlIFWLWJMGwGHDhIsKOrL82HsmKoyUMpxxTAr-pATqUQ2A_zY9mz8szb6IBeIYn8s-bgj8yfZeRQfhk6hcF-Lz0mUxplGtw1HInDiH6owSq9s9OiG-pVxi78sb_VK6IHU4CLc_BN8z4kmE-pkX6U4e-IC2KHkquNULXRKIlaNJVa4dFeGhj0iWWvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=lEfrVQXeGv-RNJ6qcQUqE53NWscNb1RECFu_B-3zEZi1Lh1ET6xjRKuanIEZENapz_QhnxhAbJVkVP_Ek3vAf-fgFzIlfUQP2SzaElIDCmp29Wexr8OUA5WLLXZDmxNF0dqnTxJhorq4K0_dXJF-SYwGmRljVzlIFWLWJMGwGHDhIsKOrL82HsmKoyUMpxxTAr-pATqUQ2A_zY9mz8szb6IBeIYn8s-bgj8yfZeRQfhk6hcF-Lz0mUxplGtw1HInDiH6owSq9s9OiG-pVxi78sb_VK6IHU4CLc_BN8z4kmE-pkX6U4e-IC2KHkquNULXRKIlaNJVa4dFeGhj0iWWvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=oXk7vLVA8TNaCORddxHZ-CHxkkiVDjjRapBRLlewqr_YWTjLwuJsU52wG4Pp69BadSqiXeVuHJUU7g8C04e9dcTMIDX6QgMLaSMtz2PD55fRP6R6Y8chOeqgnQCrShg2V9bRoZL3wWb5KOUVtmrWyqVRDRcqPJjDyC2E8sBruB3KwNBj_BAXjTzAC0bcD58zqq0RoVLC_f50eo-itwSbd1bMqw-hn9p32THm4kVTFfwXYkoWnzgNpoTxwB5mSt8Kw_HNPM9fABKBJKDGwa5-e9TPYAMDbsBHqDkDIVbwEqaIYEaHcy1uQogEwl67OJrK__2QlSoU4AA1YYTK_U1JNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=oXk7vLVA8TNaCORddxHZ-CHxkkiVDjjRapBRLlewqr_YWTjLwuJsU52wG4Pp69BadSqiXeVuHJUU7g8C04e9dcTMIDX6QgMLaSMtz2PD55fRP6R6Y8chOeqgnQCrShg2V9bRoZL3wWb5KOUVtmrWyqVRDRcqPJjDyC2E8sBruB3KwNBj_BAXjTzAC0bcD58zqq0RoVLC_f50eo-itwSbd1bMqw-hn9p32THm4kVTFfwXYkoWnzgNpoTxwB5mSt8Kw_HNPM9fABKBJKDGwa5-e9TPYAMDbsBHqDkDIVbwEqaIYEaHcy1uQogEwl67OJrK__2QlSoU4AA1YYTK_U1JNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XclirMHnNPE9R583h4viXvbz7HW7Q38VvbEQbTGyYbC_BjT5jiXKfs3I6fmdKWZ6wBki7BB6T5CgISULXMk2kdzOqxCEGigC8IlFT_goZxGtVGVgvmHxnuTz2Hju-50FYu8OyZn1ZGjlTAXdSQXzp2ti0nxHspzgOMUApW5b1ParLuCdlFWOWxR1ht9MYsVwxrXsR8hgJ9SKu0tMZacPaoiAXUpLwRv9JNiF99fAL1Gsy9IsUCDGflvRJWm8w8JZjTGO_ric1M_zrTpmYLiQ0CMKSiF2WKKOrAc267yDNbtd0725NZffoDyPqqNF73SNErm8de8k0Sv0FUQ0ksFxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQfNUPLXqF4oV7Bvp-w6z0zeq4wq3hvi7L-6v8jxDDV71jujNi1sXzqLrSMFR1jpfjQ0STbBEcRaEMa73Ds8vaHg3SJgJCfYZkhcOd79lxnlzIroqHTXihidpV8CiCgKhW6WR2GnDqzfkX93Oda-bdgIzH4DZfIDVECdFVTnkKNY_dky9kosnDuxFSI9pKqgpTVYal2oySZBJungAZHhn1sGfDYzMG1BodmJveyqXobrkx7fJYSt466NmQxs0nHVu6yw44vJbORwHskBnSZWRfckghJzXoC-lzMhUO-mpbMtPlcoHHe06MTcVm_bxPxBietwIICYoqh3RQ-0iOuc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjbCnIU9n9ZFYxSLASrCAmV0HyP7Y1DlD3kKEWbiSg5x0oFzsndcvEKUW-aMfdct5-Md_OiH976nNSLTJoU7E5sazhpwGpQYmcWSdAPEsJImSoG5T-44uXZzo79qBACDZe3g_HhZD2TJ7KALv1kHLywiRqZEm0X2_-2GI-f3Hec6t2689rT7qPoohiYw8FLhnJMEsyBJjhB-g7OWCjeq0ZxPUjcbrClDNkVGGgmiexldofdF85m3_SucTXQK8IXh8DgMFG12JtM4E8jQccHpOdoh5yLseawyGtO_ZitjHA79aDQ40JbL13jDJsFrk_dxyoizAy6oB13u1n_xGvlQ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8QaVCiSgjqKt3lQNkGke4WP7wKPCum7YPspOz_5vRPvpstcqyTq_zrrVmbxOErTruSgZugM8HuQhLki4SjNCYSBPuGpkz22zKMNwOW0LfL41rri8ng7f-Z2a4R06K4hi8NxND4cKdJHlf_h8sm6F9nWNi8LTZbcniF0vKJQfdV86BMvRYkhXPDy3NKt2tAeqzWm-aAunsCxfOMggPCJHsoRY1xazl-sJhe77BpialtfVTafOugdThvsM0Ba22G19xkZbitMPpW2g4wMhzNnKKr3ds4Pd7_Fb8u9BNnAxFSWf3wOCHzv5CuTxWy9s_vqDIuYmEL05QiCr0FffOm_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=nHIaK4wej7Vu5wspzeGM5Viun2Nacq3O7HsRiv4bXjMDvTDSghkE_j2BSLaOYWRf7qcrKGVNAZm0OqsgPq502Ia3RWAMlghQiDSIBnphANYZkaJ19uqVUnt5zpMEDqh153BJQD5MK1ZtDD3DmlsojvqFmgAv-ZZ8yWGgg4HulV2XnAeJB-wPgqolahrlVnsDLnAMySHnDEdn00r-KaMqk4w-wKYR3kwU3CmI0X_NkRn6RAvudh0hC-bYQPcvlOUVGlL8fIJGL0nIrhA3BTBcZOZTF5ogJ0OnJToANUH5THn05gBw2fhUToqbzq7CNIb3Zov6Ic9KRkFs-nyo8l3dQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=nHIaK4wej7Vu5wspzeGM5Viun2Nacq3O7HsRiv4bXjMDvTDSghkE_j2BSLaOYWRf7qcrKGVNAZm0OqsgPq502Ia3RWAMlghQiDSIBnphANYZkaJ19uqVUnt5zpMEDqh153BJQD5MK1ZtDD3DmlsojvqFmgAv-ZZ8yWGgg4HulV2XnAeJB-wPgqolahrlVnsDLnAMySHnDEdn00r-KaMqk4w-wKYR3kwU3CmI0X_NkRn6RAvudh0hC-bYQPcvlOUVGlL8fIJGL0nIrhA3BTBcZOZTF5ogJ0OnJToANUH5THn05gBw2fhUToqbzq7CNIb3Zov6Ic9KRkFs-nyo8l3dQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r0yFpXdHUEN-PFI8WC0-o3kibSmjTAjugpFZTY-mgkF61uBSj1MH9LRjzFl3L_3-dlSbrumV7A1aspc-iStpMjz-p0BjUi3jQAAYuznFe0TwGJHbhhtkohMAZ6yd0bGhdkCVGBQvXae1BwOBIuuTBFDmT8pT3xVpiMW8u8_VKJ4iM0ZuLPRABBpuWyQfw8S8daxZ7iYocGp4d7cJOFZS_Fe2A3vFnqgoC-rLR9RZKqZ6VCx23eCX8Tsd3roHrGD7bTvTDFi57J9DEUO31WEskkzLSIlF2aOwHk8V5z_SsyLneVgv6QI9E4EXPrx3LhJ8WXiyCrXGxxINuuaPQ19WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qMT9zzcCutRbQ6rO7KjoShWi0j5uONoM76s1s-IR2Grq41urFIFcgfIpFPYVSrj6ueTXTNorPpkBosJLjXJmYHlisNGcy1xIe0MMuA0HeFAGU-Gfs6K5rP49IBkPehOxaI_q6uKFLLZQuzwqHHhHC2jPU3qUcvIWUwVYZUqWXWPyK-c9WTqzAGDU8n_f7mbXg4pGbP76LEs7ZAeLXd3d-HQ2kbYiip2CXJFdzax9qw9C-aqcrwnFm77ogE8BqOQasZx9jitEDaKkqGvoG8H-BGFit6enxblmIpbZbS225SEKEaJvDj0i7xHw0o5wDVOMQxycUccmoVhm6bmXQj-XPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=VryyjCSujXnoxkOIvFpUgOfe155ZaG0y9rF3xHRYTfBGCFpe-xi5TcxqBOPtEgTIJwNuhe3vg7MfV7h3j-OJAUs4er-nadh8bbDZ05GbykhsqPz_Q8GTQUV7WN3tq1bKgc-JbqhhffcVLNeYd3wRmfPFOZQMyxVBxUtwuM-Zh0N2N4x8V7KUpnCkZPXy_C8ib3TRxoq7GqFF-8L1v5vvenAXE0D6rO6ZkbWu3C6VXW6u_sb_fl85_Em-GhHF3zKKbrnuDTgCTwR-zoKY3B4s6PGtStpPFEzuA5JlbtQ_UbAF5gTJXEMQ9IGoyi7FVvon6rkoxbMxeIllt6Xaz-FUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=VryyjCSujXnoxkOIvFpUgOfe155ZaG0y9rF3xHRYTfBGCFpe-xi5TcxqBOPtEgTIJwNuhe3vg7MfV7h3j-OJAUs4er-nadh8bbDZ05GbykhsqPz_Q8GTQUV7WN3tq1bKgc-JbqhhffcVLNeYd3wRmfPFOZQMyxVBxUtwuM-Zh0N2N4x8V7KUpnCkZPXy_C8ib3TRxoq7GqFF-8L1v5vvenAXE0D6rO6ZkbWu3C6VXW6u_sb_fl85_Em-GhHF3zKKbrnuDTgCTwR-zoKY3B4s6PGtStpPFEzuA5JlbtQ_UbAF5gTJXEMQ9IGoyi7FVvon6rkoxbMxeIllt6Xaz-FUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=SxTdCOcIk5mtPWcOiNOhwADiARJXjWGiP1N8KzEhy9C0oxIzWPP77v1jCk0PIXmWP1bZgn6rFPx27Za29P_wVmf28CJH6pjR_M7njUTeDa8xkp0vsd3MBlOmPCI_-p59gwEH4ZTn_Zp4vHwvCziJEUSulmB8DJRZQAsJrXvVAQNNIGimaL-zAezEVbjNHO9nHCCovGdPW37xMkcUndP5t8oHbUAEEN4HuZplTrMFw8ZmiLW7b9gtfutx6q3xjOSXouyhZ4wk_vCXn2ioMy4qU98C7dBfXkxLZ3v2F6_Sy-9cTXrRsfCWYdzYV4paWnkJ2R-O16wrfMRRsKBqbBdnXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=SxTdCOcIk5mtPWcOiNOhwADiARJXjWGiP1N8KzEhy9C0oxIzWPP77v1jCk0PIXmWP1bZgn6rFPx27Za29P_wVmf28CJH6pjR_M7njUTeDa8xkp0vsd3MBlOmPCI_-p59gwEH4ZTn_Zp4vHwvCziJEUSulmB8DJRZQAsJrXvVAQNNIGimaL-zAezEVbjNHO9nHCCovGdPW37xMkcUndP5t8oHbUAEEN4HuZplTrMFw8ZmiLW7b9gtfutx6q3xjOSXouyhZ4wk_vCXn2ioMy4qU98C7dBfXkxLZ3v2F6_Sy-9cTXrRsfCWYdzYV4paWnkJ2R-O16wrfMRRsKBqbBdnXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=WnMWSLshpEH2-BapnvetjTBD-kR8W7q-EDI0M3Z2mZDfjQo0Kgu8QkLceZgJb06NDA1Clhzdbupjj2pE4-L6W7JwcoV56A_ROnalV3uGg57br1kw3G39kENfJBu8RIjPXE7iclB6wKKxAZnmcZxNBPqdtQRQ6rBk4it63a9lspb9WzYFAZDKWnmxPT2N3pE7cehSMfVAUxSTW5XvCkJ2DeUnkee34QPI0e8MDbfyHuwd6qm69crIN1dZHCaNYAC6fUnXvw69w9KYm5ZoL_R-bKuMeVLDIKICHNs1ic9ZyaqXF17U5eE6N4p4KxtvOpPU78l9VyzKv9jlR1VYkW_aow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=WnMWSLshpEH2-BapnvetjTBD-kR8W7q-EDI0M3Z2mZDfjQo0Kgu8QkLceZgJb06NDA1Clhzdbupjj2pE4-L6W7JwcoV56A_ROnalV3uGg57br1kw3G39kENfJBu8RIjPXE7iclB6wKKxAZnmcZxNBPqdtQRQ6rBk4it63a9lspb9WzYFAZDKWnmxPT2N3pE7cehSMfVAUxSTW5XvCkJ2DeUnkee34QPI0e8MDbfyHuwd6qm69crIN1dZHCaNYAC6fUnXvw69w9KYm5ZoL_R-bKuMeVLDIKICHNs1ic9ZyaqXF17U5eE6N4p4KxtvOpPU78l9VyzKv9jlR1VYkW_aow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=EpvaCiEXMga6ST4abIQJ_q7WOt2xftEilgM99KeFgohpP25c4vuKwFLoayW2WDgst9a-bP-SG-vPpwEP0JR6WJvARaR1sbyc620XJMCtiIh9FecBpjSG8gF-EZhf5dzxw5nUVBYCjqlmEG1FbFxORS1MWeJiW0qD-h_nZjH9gVcEAla0h-NOqBBiP3EF3IEnc_hEb4bBhAq-2KjBT0e182Q517PY17fAxOIBJJW6p8ZulSlHnq7JrHgQy4pZDHtW9IymOM853IAQZNjzKKWrtrrREzefeq_7vKiLjSoTu0wF2zEFcSlmJ39JMxkZivPOJh3QhaKFZMi5w0ezoIvuVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=EpvaCiEXMga6ST4abIQJ_q7WOt2xftEilgM99KeFgohpP25c4vuKwFLoayW2WDgst9a-bP-SG-vPpwEP0JR6WJvARaR1sbyc620XJMCtiIh9FecBpjSG8gF-EZhf5dzxw5nUVBYCjqlmEG1FbFxORS1MWeJiW0qD-h_nZjH9gVcEAla0h-NOqBBiP3EF3IEnc_hEb4bBhAq-2KjBT0e182Q517PY17fAxOIBJJW6p8ZulSlHnq7JrHgQy4pZDHtW9IymOM853IAQZNjzKKWrtrrREzefeq_7vKiLjSoTu0wF2zEFcSlmJ39JMxkZivPOJh3QhaKFZMi5w0ezoIvuVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=RshAaI4BMryv8AQs1-6M3TBTcNa_W4Gc5WFfcUsRy3qNYncf8W9H_hxopEkqnL9dXzohrVNx44aJ_DLkjjkGoMOAnECpxhoyZQ4iyA8GHIMDH8Rd1ZUkfBxceUIK9XsZAOugYZPUvR0BYjQXv_k4S5FpaxsKHUcjVtIE6fJtTQ5iP3tD1lFpNIZTjx1juvDRtCQMPXCXZizpeyfb2-hfcwrANLTW9WoxHPvm9V5u2wD1O2x4UKZtAX3h3D45JCIenoniUlTIJ82A9mn5XSR8wtMhVItMG-JsX82DmJPLEMd7T5wLjtVOfeRlRpgCXr4m5XzZFrryv_EBRG3vAZy1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=RshAaI4BMryv8AQs1-6M3TBTcNa_W4Gc5WFfcUsRy3qNYncf8W9H_hxopEkqnL9dXzohrVNx44aJ_DLkjjkGoMOAnECpxhoyZQ4iyA8GHIMDH8Rd1ZUkfBxceUIK9XsZAOugYZPUvR0BYjQXv_k4S5FpaxsKHUcjVtIE6fJtTQ5iP3tD1lFpNIZTjx1juvDRtCQMPXCXZizpeyfb2-hfcwrANLTW9WoxHPvm9V5u2wD1O2x4UKZtAX3h3D45JCIenoniUlTIJ82A9mn5XSR8wtMhVItMG-JsX82DmJPLEMd7T5wLjtVOfeRlRpgCXr4m5XzZFrryv_EBRG3vAZy1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=axNQ4FqxcGEuRKOB8m3JeNp1zGvORPMVcv70b7QUTQ4ijg5qnYb6xFGD_oT5LH-AAMEqW9RVXRnzLTU9icGnJKYVXcQItERZ3pTjFrhl5pBg4UX2sCNxUqOlb0_uR4VxkvNAzU3mpYgzS0pxTEHLltKMh77t8jmnib_UR0hqstjb6ZvhBkysp800R_S5SIeYZOggkJAA8OOMdk-0iiVNEz6why71s1FvooqJEEyGFvkvamgmoHk7pBTzIOdWxi5KPOqEJh7P9_MLtAnGZEhT1vpVWdpzVrtbU8bQ1EXxHHGXR2-_S-Atcz6N-7c_EVlJnEggTeEKGxUtiyIUtxohJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=axNQ4FqxcGEuRKOB8m3JeNp1zGvORPMVcv70b7QUTQ4ijg5qnYb6xFGD_oT5LH-AAMEqW9RVXRnzLTU9icGnJKYVXcQItERZ3pTjFrhl5pBg4UX2sCNxUqOlb0_uR4VxkvNAzU3mpYgzS0pxTEHLltKMh77t8jmnib_UR0hqstjb6ZvhBkysp800R_S5SIeYZOggkJAA8OOMdk-0iiVNEz6why71s1FvooqJEEyGFvkvamgmoHk7pBTzIOdWxi5KPOqEJh7P9_MLtAnGZEhT1vpVWdpzVrtbU8bQ1EXxHHGXR2-_S-Atcz6N-7c_EVlJnEggTeEKGxUtiyIUtxohJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0UhY4FjdKvZlVF6Sh-inuefri5dvi5_hGgFGH04teDmzJOvVN5XtdL9AAVOO1cgu-pPAwTIG8tbaUheat16BVBEHXyaer2JtUnhWV4cFqECmrh5TH6c4WMkvBE-FoKk6SaFMWELP1iu-ESNlOTccez5vRijPNwGECbhMPcbRoqEtV86imqqfIuw6rbEoVRkW0v9BnCsY5tjD1G03URTj22hgbVBwmf9IhmEfp5cCPh_D9AHyCzdmwO7guGLRTupcEQxJZ4FuvGWwe4fMzGY25EoidhBnL20IdC7x8XTRPaYfwCVAC3be1RAzYVzCqGyfizLJsQzoDCJP64N1iLwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=GDKp-XkRRJoXpmKiLOnujoHvAl4hPxdUBRpvB26gG66GhJoqPWU5-mbVlYpj2XJUbIAqYmalauhlbmjyqyPRuhztP6E-cmsaJryqnPH_khcJqPSPIKVVduueBJLsmmZ2Neagbd05Q_v5CeDEdcWzC7-IPCYzl58EZvAceaVECFPHboqtrYOMq-57B6phnf2-G83bsHXBUXpaSrEez4D4tK4g7YBGACMbjYEFQPuPRrXfDP5QnV1ZSQeBEyjHrEQ1ONZa0hz1lwdfqAZcNOEAbDa9pPc3WHDUsvCDLhpeeXKrInooYAV_DNBhmiI-3NwzbdA8W02mdKL6bWr3-GmzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=GDKp-XkRRJoXpmKiLOnujoHvAl4hPxdUBRpvB26gG66GhJoqPWU5-mbVlYpj2XJUbIAqYmalauhlbmjyqyPRuhztP6E-cmsaJryqnPH_khcJqPSPIKVVduueBJLsmmZ2Neagbd05Q_v5CeDEdcWzC7-IPCYzl58EZvAceaVECFPHboqtrYOMq-57B6phnf2-G83bsHXBUXpaSrEez4D4tK4g7YBGACMbjYEFQPuPRrXfDP5QnV1ZSQeBEyjHrEQ1ONZa0hz1lwdfqAZcNOEAbDa9pPc3WHDUsvCDLhpeeXKrInooYAV_DNBhmiI-3NwzbdA8W02mdKL6bWr3-GmzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkpEHFhS8tUeKasqd1LXL-FOdbDmH1wiGoKzGPVuWgHvEymV-k9DxEbOYlIUuPb03ghkVUJyDHxv4OXGzgxPgNJzzvwpYNgs5cyMsJ-2AEx4Ve-UXyfGbTJoGDsj07s9LDEzPAU4n2fdJWirQOFxXk3-2MnOUkBz1uI5I8-BrnuYsWg4XbvLUsPPhIRL5gVfx4A_gY-nguzhlqa9QJwA1AkqosYfJAGauJCK3k_iiYgUvYzzELK_xNm3v41b0DRO57GsDSDra7GbbVi4b3Y2m4DQJgKudJ2XO4HEUYP7aBYU0tKflG4NRx9gjHWqteH9b993gRwDkpVi9QQOol43YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=L_aKWg4ppGelskHK-ZMo2_0D5TDyX-vaOV-CcNG7VBbhYbHRH0oQVDoOau8n1CX_1AVU_uA8J3_rQVQEi0m7WJsbatRVgTWI_JWNIkDBASpqW35uH63UmKA2FI-mNjxarPJ7EcEHLP83VO672_MeJp9Yh6GNlAdNgn63ghjnAwHgHGm-6_YQXfnfmeNs0tF39_0g7dIaRgZwJXoRKN-wniEaEyBMq_XzGdO20H2SUHo1hs_NDLQqLIppYQsloZal9jT7xwoVNSFNkDWUGpTXSA9Yrqwy6gx1_e-Y69FxVvMJn6HUy-ZkHoTAR34oLSxmiDBOHgmyzqUV7orhtWdPDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=L_aKWg4ppGelskHK-ZMo2_0D5TDyX-vaOV-CcNG7VBbhYbHRH0oQVDoOau8n1CX_1AVU_uA8J3_rQVQEi0m7WJsbatRVgTWI_JWNIkDBASpqW35uH63UmKA2FI-mNjxarPJ7EcEHLP83VO672_MeJp9Yh6GNlAdNgn63ghjnAwHgHGm-6_YQXfnfmeNs0tF39_0g7dIaRgZwJXoRKN-wniEaEyBMq_XzGdO20H2SUHo1hs_NDLQqLIppYQsloZal9jT7xwoVNSFNkDWUGpTXSA9Yrqwy6gx1_e-Y69FxVvMJn6HUy-ZkHoTAR34oLSxmiDBOHgmyzqUV7orhtWdPDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=QTMTSfycvoeidzDzxUdLTGR2Yj2v3XCXB8-5XVf3Ku3T-4vCU9owcQGwYYwchiGi73ZfsjcR5mXGdfN4ST2PeOdSzCf1Qm1Yc2T3vG-G0VObj_k_NnONTc9bxZ8quzf8bfbDWYUeYZ5Zw7V31CpPPonQTWgfQYj93Zt9wh8xW1iNUm8JmU-Kcfx3xIDGqjhzbJd5LC0CBQCuD4in9aArP0A4XpWmygf73CcCuVLGi42xE7eIiScGFD4eZIK7XEVLntt5l38dczQqZ3CF2EIIjpXKbIh6feCyiCMhvOt_SzAHTxEvivyVYjwaT1wt28Gib12EtyBmiEVQxfg1a9GA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=QTMTSfycvoeidzDzxUdLTGR2Yj2v3XCXB8-5XVf3Ku3T-4vCU9owcQGwYYwchiGi73ZfsjcR5mXGdfN4ST2PeOdSzCf1Qm1Yc2T3vG-G0VObj_k_NnONTc9bxZ8quzf8bfbDWYUeYZ5Zw7V31CpPPonQTWgfQYj93Zt9wh8xW1iNUm8JmU-Kcfx3xIDGqjhzbJd5LC0CBQCuD4in9aArP0A4XpWmygf73CcCuVLGi42xE7eIiScGFD4eZIK7XEVLntt5l38dczQqZ3CF2EIIjpXKbIh6feCyiCMhvOt_SzAHTxEvivyVYjwaT1wt28Gib12EtyBmiEVQxfg1a9GA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=Hr37j7mBNZzsK2l56Q9M7hJizKBAcbVb11PFrgX3q_0GiKNLeZCjV64F8mh2DUvuIPohK-2_qN2if6Rj4O3xS6iUlcoIwf76TiTjtEGdqoRWBvCEzWlT2wLyg8fG6K67YW3XwpjxK9WgQC8vKjZ-Ow_EeHutYnB-D9fo80QSUIFvP5UWZQYD2SCeo7HVdvMA1fZP_rt6-RRLEXXaMspuzavB5BTZ54a7_3NEOWVPouC8Kye9oStzw28Em0tPmJbuyCDJLEISguujLC0UEz4EgQhTbMpwiHjb5nn0b5ucaCEQOolML3m9eLbbicTYWJLmgn9mUNtK3AP4WndGjLENMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=Hr37j7mBNZzsK2l56Q9M7hJizKBAcbVb11PFrgX3q_0GiKNLeZCjV64F8mh2DUvuIPohK-2_qN2if6Rj4O3xS6iUlcoIwf76TiTjtEGdqoRWBvCEzWlT2wLyg8fG6K67YW3XwpjxK9WgQC8vKjZ-Ow_EeHutYnB-D9fo80QSUIFvP5UWZQYD2SCeo7HVdvMA1fZP_rt6-RRLEXXaMspuzavB5BTZ54a7_3NEOWVPouC8Kye9oStzw28Em0tPmJbuyCDJLEISguujLC0UEz4EgQhTbMpwiHjb5nn0b5ucaCEQOolML3m9eLbbicTYWJLmgn9mUNtK3AP4WndGjLENMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=CgBV9skGEvNqdgTjqBtMzcjTza_s5BlEgbMfBA2gfNM5J6_anGJM_cZVX2OzgrZULZkLXUlyvRA0Cf8e9SNeqZpxXFK6BAH2KPKrQketbCPpqaZVWKA4Oily-LhxgJPxwSucnv_YBCM925l5HiguB-DReAeLE4IxIa9YvlibGvzYQMY6iZV8NV438UPGdaKGgEbUaxYK3KAoSR-Fl_hQueTMClaGxX5yDio8HG2pY-Hi-k_ETOZgylVXj56-suGy9zuAN-1D5eCOALZVrrhF6fUgKqOyweAr5MjzQQ05HW6uKaejUSV68RuCDRrwdkQsZMkF8JSQ5p8Tvy7cSvqSPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=CgBV9skGEvNqdgTjqBtMzcjTza_s5BlEgbMfBA2gfNM5J6_anGJM_cZVX2OzgrZULZkLXUlyvRA0Cf8e9SNeqZpxXFK6BAH2KPKrQketbCPpqaZVWKA4Oily-LhxgJPxwSucnv_YBCM925l5HiguB-DReAeLE4IxIa9YvlibGvzYQMY6iZV8NV438UPGdaKGgEbUaxYK3KAoSR-Fl_hQueTMClaGxX5yDio8HG2pY-Hi-k_ETOZgylVXj56-suGy9zuAN-1D5eCOALZVrrhF6fUgKqOyweAr5MjzQQ05HW6uKaejUSV68RuCDRrwdkQsZMkF8JSQ5p8Tvy7cSvqSPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2ONNq2hDzGlgb6Ud4dSjiwddobvkn5GxEOTyWf0UFip-mS61bzCXSqqCOMgVIvJa2Goqv1zCznSCBdX86nx1V2uc-Dc2MitHws_6io-u9R9coEMxnKLZt3RKDHo02Br7OCFN3idQfzvJ6JdNP95mOl3K4N378KDBHZfmT21ssN4TlsgvOOPFAPHoikAYSrjXbrUwqI2Vnkj7S13RROacoNe82v1BbV4Eq3z50j5ZaBD-qakzTldY5qRTQp47LRfZkcUXfcK47wdWGzgQdoILJ71quBFeuWdIIG_fqzABHyvy3jdHsdF62wR3mNHqukygheA-mhUUjxFO3bpCjWzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729c69207c.mp4?token=UCg9UN8MoMLizITv4XCzqM3waDN0P1vv3A5PUIxBkfJYwq_fBFkwq1ahwfxHe6108SxfH3lJn85hBtna4xzXRoNaQxkx_RLccs43uildfe4Yvc7zgpWppjckEvmP4lysuz3738ZFM7RbrojSfjuqQVV3ep-mvm6u4TuXyrb2t6-MDj0T9E1pZoHg7xVMQ-gurhofjqfcslFYokGIpa1ZE6HJwtsRVBKsIr4IL1Re9tBLnJoZg91MwUpjj_QyLq3uu72bgO_ClpCF-zslBcv2qkTIqQa1v_CiZacWTeEC6ScqAn_vb8zdKLzuuOnL4mKYoAvQMlf6K-qL9j2oeRY1eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729c69207c.mp4?token=UCg9UN8MoMLizITv4XCzqM3waDN0P1vv3A5PUIxBkfJYwq_fBFkwq1ahwfxHe6108SxfH3lJn85hBtna4xzXRoNaQxkx_RLccs43uildfe4Yvc7zgpWppjckEvmP4lysuz3738ZFM7RbrojSfjuqQVV3ep-mvm6u4TuXyrb2t6-MDj0T9E1pZoHg7xVMQ-gurhofjqfcslFYokGIpa1ZE6HJwtsRVBKsIr4IL1Re9tBLnJoZg91MwUpjj_QyLq3uu72bgO_ClpCF-zslBcv2qkTIqQa1v_CiZacWTeEC6ScqAn_vb8zdKLzuuOnL4mKYoAvQMlf6K-qL9j2oeRY1eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر آنها به توافق‌نامه پایبند نباشند، یا برخی موارد حتی در توافق‌نامه ذکر نشده باشد - این یک یادداشت تفاهم است، اما ما بدون نوشتن آن، از برخی موارد درک داریم - و، اگر آنها به آن پایبند نباشند، احتمالاً به بمباران آنها تا زمانی که به آن پایبند باشند، برمی‌گردیم.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کارهایی می‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=qGZfNqiwZgKlg20fFkrRpRrxtNxFuOr0vr2Pw3s0lx5G2OiBTjc-zfsMoFb2N8lg8Of4tlC3AFqpRnxAEPNbzugoOEYzJn_5UBdkM6agFvW6kuv6AAC97moiJhMWvOX9v1KmrysX99sy89VEGf8ie5fV-Eor54yNXPifXpFMvt7bqQ7W5g3NJSbuL0tV8qffLkHdN7A4F1IMIF3f1u2DGndMsVkPMkIBlbQNaBFxGcGHiVLEXMO8p_IBX4Eip81GzokWXwuqy7LmKdSzgFm37s4QI09Lt9mMfJS6v_1ASO36_uWCz7WXAUn4uVuSXBntw9qpEjloRUL1RTXUrlKfCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=qGZfNqiwZgKlg20fFkrRpRrxtNxFuOr0vr2Pw3s0lx5G2OiBTjc-zfsMoFb2N8lg8Of4tlC3AFqpRnxAEPNbzugoOEYzJn_5UBdkM6agFvW6kuv6AAC97moiJhMWvOX9v1KmrysX99sy89VEGf8ie5fV-Eor54yNXPifXpFMvt7bqQ7W5g3NJSbuL0tV8qffLkHdN7A4F1IMIF3f1u2DGndMsVkPMkIBlbQNaBFxGcGHiVLEXMO8p_IBX4Eip81GzokWXwuqy7LmKdSzgFm37s4QI09Lt9mMfJS6v_1ASO36_uWCz7WXAUn4uVuSXBntw9qpEjloRUL1RTXUrlKfCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=ALmZiLBAjMyAbgDgJPfgXHT6nHe6puJpZYIXiI-DA58maZDuPgoq31KE0sTiYq6MaDz8X47U_4kgE-HjoqsN5rPHmRDbc9Iojfi8atKrMiuafRqQ9zxvhSIOsdMUABvZgn5npXrt-3A0YAHb6UozuZ_jS4f-WPcqFwkUQzH25ZxXJS_FP__lNKWKt1yphn2h2allTj4t1P1vs5ugTLjxbzXW7daST1C95zYy9T4egIdyr660Nr0XJg7TCQSYxhrx94GuVifFvi38O_gcdkoeBQd_W4G6q5nH7BE1ffOVJPVBuXKHAjKkRbMAoURQoBnvhULAMES4vV5y-g9N8UageQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=ALmZiLBAjMyAbgDgJPfgXHT6nHe6puJpZYIXiI-DA58maZDuPgoq31KE0sTiYq6MaDz8X47U_4kgE-HjoqsN5rPHmRDbc9Iojfi8atKrMiuafRqQ9zxvhSIOsdMUABvZgn5npXrt-3A0YAHb6UozuZ_jS4f-WPcqFwkUQzH25ZxXJS_FP__lNKWKt1yphn2h2allTj4t1P1vs5ugTLjxbzXW7daST1C95zYy9T4egIdyr660Nr0XJg7TCQSYxhrx94GuVifFvi38O_gcdkoeBQd_W4G6q5nH7BE1ffOVJPVBuXKHAjKkRbMAoURQoBnvhULAMES4vV5y-g9N8UageQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=ZCbG4RA3SYv3FxBbsxSXhdS5ZYSinQMjsfVckRI-NpAgs1ddqlEeIT0o1lqh_LOieKk18eo5GsNnMGEfuBnnN4pRxSG_zThuVIgV4nd7fjmIfEvfrvKSOPdcK_-N1tPT8KyIeR9reptrNMONpNNJRG_hA6Z6be5Ju65vkn0AjRZZ8-p45HPjMBqijczjcYfifdiLveVRpu08G0aizeMDUBOdr9d4hIsdQRlv9wWUm2H-H3C7h7o0bHrbhMFi0le2gVTynKYPUTdTzS5tFoWs6zEXctsKNLVhgVGdMbNFoXmpdEyN7RBZVEZ80ckigKA0of8H0vYwBX2b1NEgYLeFnDjwpZtyuSADia4UvQSiizAAi9UV8X083RaFexxUYaygFkx0-9B8F0pkI_M91q0zRD5ADcgUpmMxHXsuk-8ihYfd2pWEqvxgXwFoAIwYJtkuVFSI0pBuFEFTwa0JohzExTGmGpDtbJXM9beMptogcTA4obZ8TkfHSA_t6pSiutkUzDLJxEqbyrK0ZCq3nI5E76eAhknNdBMF_vBCM2M-JKN9HEtaZrUr02X0IUbqoWmUY36NiWSrKAyHDAKk9SisObWGZKjU9ZRsC4SuPX5JcHD7Dg4p751_lu-sllYfuoDSqKhofQs4SSVtN3HpcuZjoxgbo5Rpk1IQSIxMW4SzdXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=ZCbG4RA3SYv3FxBbsxSXhdS5ZYSinQMjsfVckRI-NpAgs1ddqlEeIT0o1lqh_LOieKk18eo5GsNnMGEfuBnnN4pRxSG_zThuVIgV4nd7fjmIfEvfrvKSOPdcK_-N1tPT8KyIeR9reptrNMONpNNJRG_hA6Z6be5Ju65vkn0AjRZZ8-p45HPjMBqijczjcYfifdiLveVRpu08G0aizeMDUBOdr9d4hIsdQRlv9wWUm2H-H3C7h7o0bHrbhMFi0le2gVTynKYPUTdTzS5tFoWs6zEXctsKNLVhgVGdMbNFoXmpdEyN7RBZVEZ80ckigKA0of8H0vYwBX2b1NEgYLeFnDjwpZtyuSADia4UvQSiizAAi9UV8X083RaFexxUYaygFkx0-9B8F0pkI_M91q0zRD5ADcgUpmMxHXsuk-8ihYfd2pWEqvxgXwFoAIwYJtkuVFSI0pBuFEFTwa0JohzExTGmGpDtbJXM9beMptogcTA4obZ8TkfHSA_t6pSiutkUzDLJxEqbyrK0ZCq3nI5E76eAhknNdBMF_vBCM2M-JKN9HEtaZrUr02X0IUbqoWmUY36NiWSrKAyHDAKk9SisObWGZKjU9ZRsC4SuPX5JcHD7Dg4p751_lu-sllYfuoDSqKhofQs4SSVtN3HpcuZjoxgbo5Rpk1IQSIxMW4SzdXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6EyJ_OWIMUjeAM9LAltTyiLyKQ_aZAgDyOyGtW_LzgOHaTxcyfkAVDScqrL8kZwuIZTonINQVOu-mPOg3eNBfDZT4ItLuOuoJ99jzuJd0yuZ0T4rTEMD1kDAD92L8dDaKcQmoSUdcU0Fe8EJzSL9Ofi0kobdknNnL28kbDUt5_saZ8I25T9KqAJ2H5SDBPZpxfiRPh4LIXbSHr6l1zNk0pJqFp43__P4k_MqfJxkORE_LOizN6rht8rHOWn7EPwz6V4IcgcIlzpXHV0EJIyDjsJhNkRLV8gC3RMQI2SQ_AuFf8wzXksFi0eCwJLibp25fXlVYADsiv0zSLDyKNnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEtaLSoGEHthO7vKerRKPhEctJRtb2czFu9rg9pw0vC3sT_ke1tSrLPI-JoRqWgvmr6Ak1O8qOUEhZAr5dza3kVVkMOE9sTIffzqz_Bd0olggioqZK_M7H2YHJ2qjRqrlwyIAvblC1iC9212zyrmnzjWc-dROs1D-L86oSL7MVeV3dIDX1-gjfYtAkkEFzklSRBilf8DxFemVtbkMfGEc8-AcSCgVdhFdJBuZhDdCFxi0-NBXoBR36T7UU6ywNtxdAUzpxuLcxGV-ouIXJQ9Ts8EhGGn4fQ1sY8SoQTdX6v_Ujhs5PNuHtS1j1sI0yXC6iBB7uiMXXY8x1s8_bVhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=uT17yOyAM0rjtPpPXeM-QBGDg9nuTNmtknXj5Puymp_lefLH_wZuoPUJFyE5PzxIMU6WIUOG95xRy-bQApwz3zXheMhVKaHS4QxDKrwgJXnzGGXUF3Nk3gjhNz0YOYzDnooK_AXfhvT4Ic4IIBsCBRgl8YA3Df4n5eFqLpvzS6xhj7Jgi9702XFhHM_zvdJ-Tm73Yg5BUn5abJm8UFmdEePnxvo57D7FYOwy5TCHmdVgCmeJ4e6ExAjBuIXkCbmNeeKbo6UP3UoLHLdArt5sPpbAsec4G9QBVGEukmeiw32nYcA1WJ877g7mQy2vFDa3OMmtQTmlGEkAfMpqN0Mtx16yGRFpIeyMRF3Q057aC-2Yar6AdOaEn3tPwdjTLnlEkIP8eX2i_mx3ZZj-qsIjFB2jHu3HxYuL771U53n4NwlS-OpiAcYOm1D4O8Et4BhaeqZ8gFa8RYbQl5a5XBtUA-qg40_O-Vc0GwPXd0Xp2u_Z3LCxWXkYkYKsOwyXKbnwgW1lMryweh7WMTsVVt9YO5iaIvuht3rTQXouugPLZj-Fp1wUOxrpJ8JUpfqqyGsoPsREGSqmJhLDn2MtwPiqm0Pb1dm8DZPO2J3LGToMvB5kv-zzkQJ6DwcoAnX-CValJ5Uc9ZO3PWQN8CYzdcdFbZCQqtoYQ0kLIDRDZ6HKE90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=uT17yOyAM0rjtPpPXeM-QBGDg9nuTNmtknXj5Puymp_lefLH_wZuoPUJFyE5PzxIMU6WIUOG95xRy-bQApwz3zXheMhVKaHS4QxDKrwgJXnzGGXUF3Nk3gjhNz0YOYzDnooK_AXfhvT4Ic4IIBsCBRgl8YA3Df4n5eFqLpvzS6xhj7Jgi9702XFhHM_zvdJ-Tm73Yg5BUn5abJm8UFmdEePnxvo57D7FYOwy5TCHmdVgCmeJ4e6ExAjBuIXkCbmNeeKbo6UP3UoLHLdArt5sPpbAsec4G9QBVGEukmeiw32nYcA1WJ877g7mQy2vFDa3OMmtQTmlGEkAfMpqN0Mtx16yGRFpIeyMRF3Q057aC-2Yar6AdOaEn3tPwdjTLnlEkIP8eX2i_mx3ZZj-qsIjFB2jHu3HxYuL771U53n4NwlS-OpiAcYOm1D4O8Et4BhaeqZ8gFa8RYbQl5a5XBtUA-qg40_O-Vc0GwPXd0Xp2u_Z3LCxWXkYkYKsOwyXKbnwgW1lMryweh7WMTsVVt9YO5iaIvuht3rTQXouugPLZj-Fp1wUOxrpJ8JUpfqqyGsoPsREGSqmJhLDn2MtwPiqm0Pb1dm8DZPO2J3LGToMvB5kv-zzkQJ6DwcoAnX-CValJ5Uc9ZO3PWQN8CYzdcdFbZCQqtoYQ0kLIDRDZ6HKE90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=eXF22iBnmK9wfEwHHOw-FqcsIhBfzuyIQhdCEAI0XYhbwgPOIv8A0VP4lTYJXhPRgBmfxusV6xqw4G_8fMZdKcPJk4EmBHlMbwXejrSX5_Eedv2dXXIJSJL7N2rFdyndLgsc-JkyPriNF4uV0b5f1bMicHnsjo44O-EMXeF5in6Wz-Ge4Lx6yPqjNPm8dKFa3alIPk0VKfLMUrkJpXOVYMSaq4UmCyK0eb0zSyElJTB8V6_Kc-HS7FtYGgs3PaeuVQFAzlYR9A0O7-GDKo8RQIk-wCTw4ciYS-NaZiVm-JiThEanjV3aqLievKcFtWF5q1-S4PWchpwci2lAXU18OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=eXF22iBnmK9wfEwHHOw-FqcsIhBfzuyIQhdCEAI0XYhbwgPOIv8A0VP4lTYJXhPRgBmfxusV6xqw4G_8fMZdKcPJk4EmBHlMbwXejrSX5_Eedv2dXXIJSJL7N2rFdyndLgsc-JkyPriNF4uV0b5f1bMicHnsjo44O-EMXeF5in6Wz-Ge4Lx6yPqjNPm8dKFa3alIPk0VKfLMUrkJpXOVYMSaq4UmCyK0eb0zSyElJTB8V6_Kc-HS7FtYGgs3PaeuVQFAzlYR9A0O7-GDKo8RQIk-wCTw4ciYS-NaZiVm-JiThEanjV3aqLievKcFtWF5q1-S4PWchpwci2lAXU18OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=nDZtKvffNCm0TTPqBsOEV17QEfmQqba_Bg4C8CRwEXXAKtpBLKII5mbeYq5h_krp9Zp_mK9kmq-XraVdC_33d4tCLXX3KrEvdHJxfJp1JqD1y0zxeOZ2nGQUE4z-Dmt7MGzu3_4muDuVCI3Zx1F-fdL3YUfU2lff93cBZAu4firQlQ4vAC2ijdYyeyQVPKdM1pIVFYVguyJX0e9Zvvq7TqxshPJ3w3vyqtEZN1h-2f-cvm2RR5mmFYC0IhTxFct2VPbnKiuMbH7cYUbBv67-hAzbTRfwHYbiaoTwaEoRqPGoF6R-cVVuIqxpu9eP67x8aG8dm5FCVIQU350qTdbdmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=nDZtKvffNCm0TTPqBsOEV17QEfmQqba_Bg4C8CRwEXXAKtpBLKII5mbeYq5h_krp9Zp_mK9kmq-XraVdC_33d4tCLXX3KrEvdHJxfJp1JqD1y0zxeOZ2nGQUE4z-Dmt7MGzu3_4muDuVCI3Zx1F-fdL3YUfU2lff93cBZAu4firQlQ4vAC2ijdYyeyQVPKdM1pIVFYVguyJX0e9Zvvq7TqxshPJ3w3vyqtEZN1h-2f-cvm2RR5mmFYC0IhTxFct2VPbnKiuMbH7cYUbBv67-hAzbTRfwHYbiaoTwaEoRqPGoF6R-cVVuIqxpu9eP67x8aG8dm5FCVIQU350qTdbdmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET2vXACx0MHMsOI1Q6JIw3bLGlh1uI1fcRhtY77xsPnL-xhwnUjUcO6LFzl4uIWhoF990z3_2EVuets1UxdxWezfOesDPqbltLOMA6zp0cNfg25T7mU-NpOWh9UA-5t9aa16iGt7KcpZwkkrjy5q7669Ag4qAJIdQJaHA28IfMXWwpM6F535bz5Ijhp248jK_JZquk3FMYmvGTJ7741p_ltMtADuihz5e23XRCYl8MXwWKnm_CHBcXXbeVAnIW5xr4LtPxoFwN53mjo6R0U2fimkONzZhPyqkrbF8hPRwb8p_4YbxJ9oKktiEf5yz_y7bySAlvX6sZczOu1lbIXrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOrYBTL5CLu2LHCahLGxHDCUe2tAzf26A1-QYmTy781kelLKCm-wadeMZQSImrcILe0NudF9x5fNe9qOdliGaKFmS98Ms4vjzayeV9z67F0KRtXGrdNMts8WzHTSTsNKLqS2klPY4zCISbvi3QV6nc33-M-nhi_0WWi2MKRd5jWmtGs0zbjT459yrco8D_ntvVtYVCcqNllqN89C8BUTp1zgp1C9u3qg5OKmDvoj9FQXPf_dmMGIswbY1I2PYb7l-mfPEQO04T8-Esclb84H18aaGN6vneicOouiciv_1glJMD49sMlfvZXzKw90iCahfZh7WRJLiEGHOx0Wusntrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djqu5bGe_E1lWGNYanrMNbtJUu5Vm50IEwWUcoRurkdrabSZGCnR1M4fSymj1r439x72Y4eiePeifKU6zGUfOEroVs9USsEh8mb1x9TpDaOR1Vby2WOLutoJN9B3SUEuCMvce3cbvkKEjFhFQO_oUPI5Pmo3KaugTSMBJMXuWnYJZ8sFS_OmOu-H9tlh6bQIVWbZ0DKlSgHnLGCgOG9gbi3GKWed1Sl4lKkMum8fxIcaRWkve-aONb2cMZ_zwtgTpVT_XPzVN9hoDTnKWNLemSt2txu_2SSoppYtlR7Jp5Yzo_7bpShZLMizmxNJ7oUqB7G-fGk827qRzGjCpFLOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=hbKkymAl8ytGLLA-2Kz5fx-7Tqj6ddv9TRTPnyxjFIlpsJEhxXmoNJ_KiJRoPzKwtspT21aihMpKzlXgZrlulOMJOsuv2khenDj6klJQPj9GUN9ZsJprNixEplcnrghnR8ePFqvyTS7eAlp8RFK3xwR8cR38_JjJnJGxligwppBjEG_uQdSBCvLprNB-XzlOL4YscAy8EJcE1XtJlXYnosegkYrAWOOzK3b4F8W51fmRElBH-3IfWVWY-SG8slh_dXlAXPRvuMf6lrX8TnmaoWbxIKJw_YFWhjI4REaIqRLZ68a09TX7t-DkzjwAErlY7Wx7ksFNO721Tlp5rXRknA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=hbKkymAl8ytGLLA-2Kz5fx-7Tqj6ddv9TRTPnyxjFIlpsJEhxXmoNJ_KiJRoPzKwtspT21aihMpKzlXgZrlulOMJOsuv2khenDj6klJQPj9GUN9ZsJprNixEplcnrghnR8ePFqvyTS7eAlp8RFK3xwR8cR38_JjJnJGxligwppBjEG_uQdSBCvLprNB-XzlOL4YscAy8EJcE1XtJlXYnosegkYrAWOOzK3b4F8W51fmRElBH-3IfWVWY-SG8slh_dXlAXPRvuMf6lrX8TnmaoWbxIKJw_YFWhjI4REaIqRLZ68a09TX7t-DkzjwAErlY7Wx7ksFNO721Tlp5rXRknA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=N-AmzgLwNLxv3Y2TSBOu1pl4JUB6k6VEs175zUNRIEaiSE_3eEyUC_1QRtAjxosRR6fWjez8kWTViz-6HM5HLMlbTUyzq9NDchia9T5aCpKjjmvmi2_uqcKV0IIM0puO0nhRIFb1W3UCiOsSlL4ukHHp4owNlc7YnN73tWLPEr092-b2oEZBnwCXsa-O0GSYMfZBhS9TOqyiVUw_hgcZ_6ieJKWqMnXpKX71646J0uVHNRSMr0uj-Q_uH7f_qHpzsm0hdCw29bRdxTVOgPlYoQhhUPL68qBh5wQF4PUgvhUS2ncCEuW5ohP2jXCaaLsQ78lkKQ0kQvGHX8E6HXhABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=N-AmzgLwNLxv3Y2TSBOu1pl4JUB6k6VEs175zUNRIEaiSE_3eEyUC_1QRtAjxosRR6fWjez8kWTViz-6HM5HLMlbTUyzq9NDchia9T5aCpKjjmvmi2_uqcKV0IIM0puO0nhRIFb1W3UCiOsSlL4ukHHp4owNlc7YnN73tWLPEr092-b2oEZBnwCXsa-O0GSYMfZBhS9TOqyiVUw_hgcZ_6ieJKWqMnXpKX71646J0uVHNRSMr0uj-Q_uH7f_qHpzsm0hdCw29bRdxTVOgPlYoQhhUPL68qBh5wQF4PUgvhUS2ncCEuW5ohP2jXCaaLsQ78lkKQ0kQvGHX8E6HXhABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=XrTncqqGPLkkKIci7szPEq2eVp0k8UFWpI_S6SkWC0ZcaW3IEGjCD2UZpEZFyZ5_XAzaIR2blNUrZOvU9W8XQv7El9qIxkT43sN3_OADNkuru5ulvEUEaT5whoNx42kKPsSkUzv7u4mVXcYMpZuJPtU5Tb2XVdniOzH6u9YExea4tktDyRXwxCitJLLQ-qTd4xPyOynxC0zDojbMGSfPKYRtDkdnBgN8luEK2ytFa2p9XiHMW-5EQ_2rpzmVY1c3wnu89gcNm6SgMgHDGpCAKsiXqs46Vx2RYEv_AeER9E3JjV6Fakc-UKWrIQ1wHujs8QPgkbxycKEY9p9n91PYq4WASIO3R7AGkkM-gmlMBGI1BENXpaiWlvApd3_6_yG3pGVW2ZY47k8P-oeGKboL84QAYmJ9VzdiNI_fGuJi-dr1NhUOaAR8CVk4yjO0SDxARA_fpEEH34JTzmnQbVn2CH3O_Kp2uHhwVk7j_KdvexwxgKSYIoObJyek8QaglkuqG2sGNYD6uGrWjE-Qt4aLHZneshOBhqM94DsTH9bD75NvixgRDpQQeBQblucVWHtEYIFAV43uh9XHt3FllYJ8ZBdpxweeV-_0X6ffSO30KIgebu4fkYaUV9WKF1ql-18J9R9_6ShnzMunEl3AVprPiKue5cE-4n7PMC5imIYBeXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=XrTncqqGPLkkKIci7szPEq2eVp0k8UFWpI_S6SkWC0ZcaW3IEGjCD2UZpEZFyZ5_XAzaIR2blNUrZOvU9W8XQv7El9qIxkT43sN3_OADNkuru5ulvEUEaT5whoNx42kKPsSkUzv7u4mVXcYMpZuJPtU5Tb2XVdniOzH6u9YExea4tktDyRXwxCitJLLQ-qTd4xPyOynxC0zDojbMGSfPKYRtDkdnBgN8luEK2ytFa2p9XiHMW-5EQ_2rpzmVY1c3wnu89gcNm6SgMgHDGpCAKsiXqs46Vx2RYEv_AeER9E3JjV6Fakc-UKWrIQ1wHujs8QPgkbxycKEY9p9n91PYq4WASIO3R7AGkkM-gmlMBGI1BENXpaiWlvApd3_6_yG3pGVW2ZY47k8P-oeGKboL84QAYmJ9VzdiNI_fGuJi-dr1NhUOaAR8CVk4yjO0SDxARA_fpEEH34JTzmnQbVn2CH3O_Kp2uHhwVk7j_KdvexwxgKSYIoObJyek8QaglkuqG2sGNYD6uGrWjE-Qt4aLHZneshOBhqM94DsTH9bD75NvixgRDpQQeBQblucVWHtEYIFAV43uh9XHt3FllYJ8ZBdpxweeV-_0X6ffSO30KIgebu4fkYaUV9WKF1ql-18J9R9_6ShnzMunEl3AVprPiKue5cE-4n7PMC5imIYBeXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG2RKZwvXMqmYmtvwXsEcC43tc49zJp6N8o8CGGTLAx-gqZ_0PSuvhO93nodqvosOXljuCfIj4gXMcR0p5Z9S8CTcC_wgmYosvYVj-lqcK_Fi1JlteDbzJ3_rzv9I4pZh_lxYqXEMxKY977nwJMw3-OPX0QS6WXu1oXc8FNm_4IZ1nARg-UJlZs-yU1yDFWwi5TJKQAUi5RkDSdD5fYiqvqPV95LqRwzS-7l42AmXajI7Dq-CckggjZioffOdF1TSAqNpNopd85q3BLgDKZIIy8OMCRBQu2Lu2WHLY0STqxupDclKisxpKG5_UrkebFJP6HEYs1AuTTuU1BD-1rg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=kBAYWcIs-29COsxqEFwiM5Qb8PCSi3tR6s2Q0F1dm2zT6D1Ootrl2D7xng7vRcsc4O-F0BwGWqePv0t_-z_Dkh29VrkSlh2-G6MYIYhY4eNhOY4mEyOBEmNN5Ec11KP7pi_9ThCYykqw5p7apG46wL7LDuPgWMauAGALUqluTgt_qLq434qxHMfPaGJWTsNOPwJvuc3_l0Ww6izdLZhtjtjInBmgZsdpxlHiYWx7sZ53YJCuvIJWW2pHLQXYwYtuycZ4vdc1FmXDRy5L3x1Ffx1SCMmLWEQZag38E1SUbuOpBrpvWekxjQKctwndrwrYQb6attddNfme8ExuUS0PUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=kBAYWcIs-29COsxqEFwiM5Qb8PCSi3tR6s2Q0F1dm2zT6D1Ootrl2D7xng7vRcsc4O-F0BwGWqePv0t_-z_Dkh29VrkSlh2-G6MYIYhY4eNhOY4mEyOBEmNN5Ec11KP7pi_9ThCYykqw5p7apG46wL7LDuPgWMauAGALUqluTgt_qLq434qxHMfPaGJWTsNOPwJvuc3_l0Ww6izdLZhtjtjInBmgZsdpxlHiYWx7sZ53YJCuvIJWW2pHLQXYwYtuycZ4vdc1FmXDRy5L3x1Ffx1SCMmLWEQZag38E1SUbuOpBrpvWekxjQKctwndrwrYQb6attddNfme8ExuUS0PUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=iS0jSs5v0dkFsftwo6RvGFsUPaD3XYVz2TVCbf2ITzHhHiZMLn-a04xbNWIYzoCY286Sg1RWcUNZh8GK_D0G65TgrNZxjvNKplAIkQ4eShWCnPpmEQ7D6ZDk7EHS_DUpYpV8S7yHEdnp-fXQDVOhll5tmcAKPEoZYLjWniU3gzabvmeLPnQ9aOPMc2uVUDWQGi6sw-O5P_GCiEc2JmdyZhRhuyIGtocexjUPaJ6J57JpOqE_DZlWOygjKDSC7gq_4jVSy0OlDJnlvLRBJ2vDMF1V8id4OXBqE8jca_uN9Lo4Y5aEqeF3x9vgQCaxblTqB_h71oNSDzaRoBX58me7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=iS0jSs5v0dkFsftwo6RvGFsUPaD3XYVz2TVCbf2ITzHhHiZMLn-a04xbNWIYzoCY286Sg1RWcUNZh8GK_D0G65TgrNZxjvNKplAIkQ4eShWCnPpmEQ7D6ZDk7EHS_DUpYpV8S7yHEdnp-fXQDVOhll5tmcAKPEoZYLjWniU3gzabvmeLPnQ9aOPMc2uVUDWQGi6sw-O5P_GCiEc2JmdyZhRhuyIGtocexjUPaJ6J57JpOqE_DZlWOygjKDSC7gq_4jVSy0OlDJnlvLRBJ2vDMF1V8id4OXBqE8jca_uN9Lo4Y5aEqeF3x9vgQCaxblTqB_h71oNSDzaRoBX58me7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=NWDz_xg_rvnpm-L7Kti1DyyvQFi1wlvJ3uakQYycjixS4abThBkef_MD0UBGvTWRr5X7qMOvXLdadg2as7GCf-OFa88WrsSffoXiPASunnsigQmOyAqi-TI4Z-0bvqY0ASwdh4RzaU60ZtRg6-fkIqoUr42Igvfl6YSZNvsdZxTBu1d-t6Q1_PcDd2LoS4cdED5gsT9GJPDfevaHOKeVBFcTZrM8d_wYvrMfkY26qYgNBR52L2oSe_ibfgvqlCp--bvEKIIGyGKlu2mI1REGRMUTtPhcViR3jBmxlEMKIozHCxqWZjSRbV8OY2pBE1Wogg2pcdwRq-elXKstJk-Zmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=NWDz_xg_rvnpm-L7Kti1DyyvQFi1wlvJ3uakQYycjixS4abThBkef_MD0UBGvTWRr5X7qMOvXLdadg2as7GCf-OFa88WrsSffoXiPASunnsigQmOyAqi-TI4Z-0bvqY0ASwdh4RzaU60ZtRg6-fkIqoUr42Igvfl6YSZNvsdZxTBu1d-t6Q1_PcDd2LoS4cdED5gsT9GJPDfevaHOKeVBFcTZrM8d_wYvrMfkY26qYgNBR52L2oSe_ibfgvqlCp--bvEKIIGyGKlu2mI1REGRMUTtPhcViR3jBmxlEMKIozHCxqWZjSRbV8OY2pBE1Wogg2pcdwRq-elXKstJk-Zmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=tRAsOG4Gfnb2E4kifC6srlsGh8CxTMN0yPmDssXTlD0woK7wXolIiW4u5WDWXsawpT4ltprDBDA0suxGCQL3RfLH46pjPappNuguvc6qF253PZ0NxDLT-mIP4wsWnY_8KWMNY1lxMp3nE1Iazg4w36qGtdfZOpVmdnb9IeivumLrT1SIHNORJ9IqPDf19aNo-N9GlML-26luAnjUPdcMyLnNkVq5ymyCQGoTozdkxDCrAh1W0gU6lrli8cc0UD0iXt6dogaRp0cbtlS-g2PnOJu74sXbXseL74fcCmC9ga_WJI8ThZ84qCyPvlvza4CDw73w_IQBEc5tlDLcZcap9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=tRAsOG4Gfnb2E4kifC6srlsGh8CxTMN0yPmDssXTlD0woK7wXolIiW4u5WDWXsawpT4ltprDBDA0suxGCQL3RfLH46pjPappNuguvc6qF253PZ0NxDLT-mIP4wsWnY_8KWMNY1lxMp3nE1Iazg4w36qGtdfZOpVmdnb9IeivumLrT1SIHNORJ9IqPDf19aNo-N9GlML-26luAnjUPdcMyLnNkVq5ymyCQGoTozdkxDCrAh1W0gU6lrli8cc0UD0iXt6dogaRp0cbtlS-g2PnOJu74sXbXseL74fcCmC9ga_WJI8ThZ84qCyPvlvza4CDw73w_IQBEc5tlDLcZcap9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=E9tkzF4Czt7MAcTzPIskeBgcJpo5wpMQFLAu8hjHitpVfGJJS2kIzj7QvXabBL4TLFSUB2dVPKP3DXIcs0EYktsrEiubC1YHFJ3Ip_qPkq5thV7u0h162R-rzYUyl_Hk5m4BvHagnNDksqmtOR_YZtIMkLAV3Rs3QLt7q-TcLrlsu7JAa7XkLEvuvFfBPBZFE9aN_sBwbXw281vyy-aIT9fDIohSbm5a6yJXAcNBABIZNzWjM3O7YhzbThJvk6agX6aLk6QI3pHCVqCXK1ByG8CHukEBzp9ZnJchZN4zWb9uGD1-XEeznPHnstnl4JwGS9l3KAEnnQxG8_hiqI1xbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=E9tkzF4Czt7MAcTzPIskeBgcJpo5wpMQFLAu8hjHitpVfGJJS2kIzj7QvXabBL4TLFSUB2dVPKP3DXIcs0EYktsrEiubC1YHFJ3Ip_qPkq5thV7u0h162R-rzYUyl_Hk5m4BvHagnNDksqmtOR_YZtIMkLAV3Rs3QLt7q-TcLrlsu7JAa7XkLEvuvFfBPBZFE9aN_sBwbXw281vyy-aIT9fDIohSbm5a6yJXAcNBABIZNzWjM3O7YhzbThJvk6agX6aLk6QI3pHCVqCXK1ByG8CHukEBzp9ZnJchZN4zWb9uGD1-XEeznPHnstnl4JwGS9l3KAEnnQxG8_hiqI1xbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=FB8pU9-9FvW-m4koJtFEq1v7wvMBuf2E6tVEQ1M2PQJTEbw1r1bQcVfPsqELDyZ9O7SwrO2vh2fx9aHoW31tQ0ky76xiDrvizfZFDk8EG9kuvSjS_DYxYeEyO_lb3IrnfQE_IJ6K_jnj6IrrxnqLf5sT3-ij837uzkkRZTz_1YvMTfq11kZUEomhdUzAh_k2ywH74XguobWOP-oCvmXmXnoDds5ugthfwMZk5REWOZqs93meked6onPpy-dN2Q7KkuVDPPAWBCuA69aw7vD7xF3z3rYuokiTpxIX3VvCd9grNoi8ls-k9XO0mVdG5FTO-QmcfqgWQ8dAY_sNw_WhfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=FB8pU9-9FvW-m4koJtFEq1v7wvMBuf2E6tVEQ1M2PQJTEbw1r1bQcVfPsqELDyZ9O7SwrO2vh2fx9aHoW31tQ0ky76xiDrvizfZFDk8EG9kuvSjS_DYxYeEyO_lb3IrnfQE_IJ6K_jnj6IrrxnqLf5sT3-ij837uzkkRZTz_1YvMTfq11kZUEomhdUzAh_k2ywH74XguobWOP-oCvmXmXnoDds5ugthfwMZk5REWOZqs93meked6onPpy-dN2Q7KkuVDPPAWBCuA69aw7vD7xF3z3rYuokiTpxIX3VvCd9grNoi8ls-k9XO0mVdG5FTO-QmcfqgWQ8dAY_sNw_WhfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=FPq0SLp2XQdR0OSqI-aLCfw11ZX7CBIFZ5_7dlbcLnfrrzTumminBS8ybd8VVTPXRJbCn4_gMixjs00vlmDJHsE1xyW9Pv5xAhlXknx_LIvpQo959kvZ6YE7aDYkmNH_JsyGqmgYI3x0GXGzkQgSP_1obYhcIo3S03HNm-3h9Zc9A0TMIK-p2xvxZQq7d4sBcWZBCjUANUGkFIyc2B06X1AI-FSVUduLR5jn93GSuplAcD7IQEI_v8s-JUgaTHnsS1GVCxH2kNL75KzSahFRRWr58dVW7YhOiXRpPLFWW7NFtI7pLpexn348Trt8sZozD2Iw-DeRE-_ImkjPa5P82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=FPq0SLp2XQdR0OSqI-aLCfw11ZX7CBIFZ5_7dlbcLnfrrzTumminBS8ybd8VVTPXRJbCn4_gMixjs00vlmDJHsE1xyW9Pv5xAhlXknx_LIvpQo959kvZ6YE7aDYkmNH_JsyGqmgYI3x0GXGzkQgSP_1obYhcIo3S03HNm-3h9Zc9A0TMIK-p2xvxZQq7d4sBcWZBCjUANUGkFIyc2B06X1AI-FSVUduLR5jn93GSuplAcD7IQEI_v8s-JUgaTHnsS1GVCxH2kNL75KzSahFRRWr58dVW7YhOiXRpPLFWW7NFtI7pLpexn348Trt8sZozD2Iw-DeRE-_ImkjPa5P82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=uMg2IbFnaQnzNpKuyejW-dqtxhM4bHUXPCfzYHxrPgfsMzbKR1m3EhFMelgLc2vSOV4kVWv-2G1XgQb80wDofcornq6IjhvbGF0idg1Cs1ustcVA6iIej6jUOmZFAyzT-muHJUgDClP61pzgSrLlpUJ8sYHQV3sez0w413AnnEh2aHxxF_BN30JxUSzFUb2oXGyAus6PdRwxaBorIG5U67P-CyKMHpaeTqxXTgDJm-JWqBkVRPeLobHph15WSF1wcP-gBJ1eQcTjhWzSteddavpKxs2enpDUyS3KUR6zxuzPRQJLK9rt6zD7k0ngDO1oYhHdbJNLnVMDuwQ9pt5QQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=uMg2IbFnaQnzNpKuyejW-dqtxhM4bHUXPCfzYHxrPgfsMzbKR1m3EhFMelgLc2vSOV4kVWv-2G1XgQb80wDofcornq6IjhvbGF0idg1Cs1ustcVA6iIej6jUOmZFAyzT-muHJUgDClP61pzgSrLlpUJ8sYHQV3sez0w413AnnEh2aHxxF_BN30JxUSzFUb2oXGyAus6PdRwxaBorIG5U67P-CyKMHpaeTqxXTgDJm-JWqBkVRPeLobHph15WSF1wcP-gBJ1eQcTjhWzSteddavpKxs2enpDUyS3KUR6zxuzPRQJLK9rt6zD7k0ngDO1oYhHdbJNLnVMDuwQ9pt5QQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=Eul2cQCAcbhM8Ma3s_H8Rw8LOs1gZPKv0vKBoQT8zN1HRg86ZPBOxci8L99uEIZicYqItZ-PWBWflifYPl0X9lJ58r4WlZdgru-PysPtPDo1nybRJ5C3Jstw8_V2W8FWUn0e1Wnu2qfGOiteLBeHSzQxH0Kw4vS4xvH86MXtOYVo3KhhI4TFrIJFUNTfZLD4sCWEE2cXvn6RhYXRhaf0kb8_NBwoL1K0zT7dgUkbQZ2qfKDEiPlozpC61xQNXaFeY6yWytbhARJW_tquBOsTkqWIKcpw7T4qehwnZq6uxowRU1BRHVyoVTOYIDY3dX4mw5d_MH5IpG9gLThZbg439g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=Eul2cQCAcbhM8Ma3s_H8Rw8LOs1gZPKv0vKBoQT8zN1HRg86ZPBOxci8L99uEIZicYqItZ-PWBWflifYPl0X9lJ58r4WlZdgru-PysPtPDo1nybRJ5C3Jstw8_V2W8FWUn0e1Wnu2qfGOiteLBeHSzQxH0Kw4vS4xvH86MXtOYVo3KhhI4TFrIJFUNTfZLD4sCWEE2cXvn6RhYXRhaf0kb8_NBwoL1K0zT7dgUkbQZ2qfKDEiPlozpC61xQNXaFeY6yWytbhARJW_tquBOsTkqWIKcpw7T4qehwnZq6uxowRU1BRHVyoVTOYIDY3dX4mw5d_MH5IpG9gLThZbg439g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=LP4tQZo07p9vee0TJ9ITbCkcxc-_IkvB_GGSVGFA6O_15qOYEJhhMDGMZ2wqO3j3If0iBky2segTomVC54G6YdoE97z2kySd2iDjyUHmVjMCMy4gaDx5xnsGYxmjvBuKaanLHf1vswahUkQTNOhfksi8lfP3NJiHW6si_adgQf9rdDWJFNwcW2OyzkNF1CCtdTVl7UBvpNWQYHHLmhr3jNlstcu8G4BSMEZebYyI3txe-58-9FdwmqcIKNFQCGCdd0XS_hNqxz4e41jer9qLsWUUzVwUQvqG-Pp20aVtTfWbW-AviIsDfmmotWlguPUnAmkZSCBjyxB6Cs-4e7_U3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=LP4tQZo07p9vee0TJ9ITbCkcxc-_IkvB_GGSVGFA6O_15qOYEJhhMDGMZ2wqO3j3If0iBky2segTomVC54G6YdoE97z2kySd2iDjyUHmVjMCMy4gaDx5xnsGYxmjvBuKaanLHf1vswahUkQTNOhfksi8lfP3NJiHW6si_adgQf9rdDWJFNwcW2OyzkNF1CCtdTVl7UBvpNWQYHHLmhr3jNlstcu8G4BSMEZebYyI3txe-58-9FdwmqcIKNFQCGCdd0XS_hNqxz4e41jer9qLsWUUzVwUQvqG-Pp20aVtTfWbW-AviIsDfmmotWlguPUnAmkZSCBjyxB6Cs-4e7_U3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=hFYNx9vhizaJ2mB1Q2I8Rt2Sfp9AJEsc7GiHHxnW_WPMMYu1jjB0OZSI57j47oPBwReiUbq5H-JoVcGSYBJuuSzdlDfQmXNVuOuACqMWNmzWh9Xa2LtgUekaMA0zrQy8Dsea-3UnM0XvDHqE7_V2I2ZBQjovOBUuB4FYQcFZJ9593JfO4sr2_LdlZWCmSaVUWfashD5gzNQ7fQPDjQG84SI-3LhOLTcJi9aqwLBNYW6Y7U8G0ZWkInXjG2W6RWSVIK86xwp3Dg_cFTOR_djS2r9m6EWo_KhEcxZWaqNsrOjiD8S-FS3DQDNl8_GONQHt6vpDaMELBrgkkxpYgzSrHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=hFYNx9vhizaJ2mB1Q2I8Rt2Sfp9AJEsc7GiHHxnW_WPMMYu1jjB0OZSI57j47oPBwReiUbq5H-JoVcGSYBJuuSzdlDfQmXNVuOuACqMWNmzWh9Xa2LtgUekaMA0zrQy8Dsea-3UnM0XvDHqE7_V2I2ZBQjovOBUuB4FYQcFZJ9593JfO4sr2_LdlZWCmSaVUWfashD5gzNQ7fQPDjQG84SI-3LhOLTcJi9aqwLBNYW6Y7U8G0ZWkInXjG2W6RWSVIK86xwp3Dg_cFTOR_djS2r9m6EWo_KhEcxZWaqNsrOjiD8S-FS3DQDNl8_GONQHt6vpDaMELBrgkkxpYgzSrHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=urvmIvFqe2nbN79fok14EuOGbkxZv33jhyPgRy11yNedWM3rHc5dG1A3MGfhcEiZEmUscQuX4kGm0rPCS2v8ANHYPgjfcu-AbYLzUkDbuoHNcrM-3Tgu7Wy_tlTkrHfR_-N7KzOMvTdX_-Ik7P0zQEtSOCLWJuxlPH0gUoH098osj7ml1gauOsmYc8zbuWoBD-Z6NzI_bACwbAYpSsNEI0SMhbV_miak1o4r3sSFH4D_JDA59NFGOIzPbczYugj1lvlaLHpqnX17KegFiZJTTEhjROjkYVg7JCrJdjeMPkGNGU0q_8Qcdr5e651gvpCLd4AnwDrvQNfM-QR83DPgxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=urvmIvFqe2nbN79fok14EuOGbkxZv33jhyPgRy11yNedWM3rHc5dG1A3MGfhcEiZEmUscQuX4kGm0rPCS2v8ANHYPgjfcu-AbYLzUkDbuoHNcrM-3Tgu7Wy_tlTkrHfR_-N7KzOMvTdX_-Ik7P0zQEtSOCLWJuxlPH0gUoH098osj7ml1gauOsmYc8zbuWoBD-Z6NzI_bACwbAYpSsNEI0SMhbV_miak1o4r3sSFH4D_JDA59NFGOIzPbczYugj1lvlaLHpqnX17KegFiZJTTEhjROjkYVg7JCrJdjeMPkGNGU0q_8Qcdr5e651gvpCLd4AnwDrvQNfM-QR83DPgxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E93bIA4gPze5233cMmwwjIIrIo7L0w7Rcjl2NnCPi5_PwG3ELBVvTYQKkO19uBTwYDIdl7G7opzsP8C5HKGhheIcQoI2ceZtCJy5mJI_VSC_SBTYdQSufLk4eynIqV8g6-BTXRMnQUPL4o5FTPp-qn-TY9kcK8GeKDGhMzgMGYDY4_DRLaU2K06rX612uu6ggqoF1nR75SHwBWTh9CgzDVsNTP5ZNAScbCnairjRx7_bKzaUFdxqoAQ4ZAPbKI57zKhd93m_17FAdf4VAdrU_p18a1pSF1fDVhzwlBXea1HNYPKF-d1yRmWTCSId9wEiqtsUs0K-JTPg052EX1tXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKtouxfALsr2ehPePXNKIIn1mHqLFYCoM_rEcRIDWQyNW5t6YOkR9QpKUr7raOlBC-VbeyGzYOXwvHDEhAS5ccWm53tILCgnJSg1q5MZ2oaVy54TITb9J9MUfmq8gq_2Qdus-uYiWwBFUwkFXpyWZGVWXZG-MBV63_j-Gky-7ZUNxvkCZK28N2VQ1T4Hy1XvLkXzjUsJDxktMq8uWOOUhxzMwlPrScxuA69RZegsvue9AG9CfQGxegv-wEB2C4N7iE-u5IJKnDLMDTp9KHNegT_yV3516EXKe9P0CakEzMcD0NzjW1p2DzP51FS-m392etN7zTl1NlBPbCp0s6w4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_Kd2Np0v9ZsggnQFB_e92DD3cFEzVHKz59-EXpkt0tfxWJV-fQ842DTRABxNrWr7hCRk8IxP5iwoioeZAnbdA9IL4KDEaatVaoU2jRnRwe6Kwns_8OUcr2bgoGZdO6_MI2nMbCRCeWs8mDWgwmGbAyWZkrVdNokIpNwFg87RUvDzCkxh2DWXG7OAEfPnY5ZYfzzhxGv-eb6RZoMBTE348Kj1_SS6LZb6uV_xslSONw6xZar-fTb58DJiZIuIHHI1FrdiOEZ8BpVTyRLHNBvJ7Oce1uRB8QPJxLPuEQs5LiCB_YZPHe_FZk9rNSkeB0Li9k1vo9WAy1KD06bONJ4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrCFl-HJuEc5mWFeFqSOsvGL-SZx18SfoJruj-hYznQaHQzEq1DC-MBTys1ZNM7oHwOEn_dLfCLhI3f2l_pPYuvcMY80OD2MfvCARpEGi8PBFbkuqVsCWLHtgAGtxeX36keF10q7ZbCNIFjbkfGqV50RAkoGlCYjgzY6YFjMiiSBcpzDhueiQ_ZnmJj5OgdAxHj5bUDBg_eKYIcetDovginijOmQmbTX4kP2mwYcPL6yDsi5S8AOt0J0kamkEMFfzZgsgMN0UzHFMh9s_FS-7Ybsd1Y1Hg41JxLyzlR0yUmgkYPW30MKg2hwqjUN6_n0zJp6lsgsF4XCC7elnZDxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=TEYGyuwdNlwO71WODADJy7ihtl5mzhsOafJvQmF76dnrOc4Zfq3bxD6SSrY0zEzePx7RSLDPHvMvkXY3UDzLns0xULwvV12Ki2l3KNcy9pJhvee3YMwg0LGo9-Wc5zzTdUntFDLHY5gnBpEb_3U3DIZWp3vJ_HRHAPDkzpozzuB6HIyFlt_7gfDtwtDtySDdOAfcdXr_WbD-OVPi5Z9DOYZsmRjptnU6UwOtJ7Io8xJvCpxC1EdTFWqirau2ot_6wjjcGxzSXdsPII0a_5h_9V2obIYvKpMMiqngBf1mR0ZhaNYT0omTaxFxKFx9j0daxxuEj3LWixPs2-EEn_x10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=TEYGyuwdNlwO71WODADJy7ihtl5mzhsOafJvQmF76dnrOc4Zfq3bxD6SSrY0zEzePx7RSLDPHvMvkXY3UDzLns0xULwvV12Ki2l3KNcy9pJhvee3YMwg0LGo9-Wc5zzTdUntFDLHY5gnBpEb_3U3DIZWp3vJ_HRHAPDkzpozzuB6HIyFlt_7gfDtwtDtySDdOAfcdXr_WbD-OVPi5Z9DOYZsmRjptnU6UwOtJ7Io8xJvCpxC1EdTFWqirau2ot_6wjjcGxzSXdsPII0a_5h_9V2obIYvKpMMiqngBf1mR0ZhaNYT0omTaxFxKFx9j0daxxuEj3LWixPs2-EEn_x10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=W8VySKh1lh1FQtJkArZXksNkXuNb5BKC8xK3GOQo45pO5-YLaEOek-N-XEtzMqYDJAXnDVh_SSfajldNnpBp2TIuex9OkRBhQaW44MJJjnFtNlLRqkTMSwHXrqpKmOuj6H2KU5yU9WCbTMoHgCyg9nUAVXfxkRsQDR3DgbKGTQe0yyUhjJId-Zq-sPdr6Jb6LOLxaNf7jHYqv9Qb1G1OZhNdbvgxqbBQvxCqbwDLiqQyI-o2N_G5orNhMroSKY6z5xB8tYbK3ERL9yA47PLVEvk3s2ClfrK697wAVcrzIqa6ecgrBeEOiFPUnU9n9LyomzA6B6lHjki8wrtmobri2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=W8VySKh1lh1FQtJkArZXksNkXuNb5BKC8xK3GOQo45pO5-YLaEOek-N-XEtzMqYDJAXnDVh_SSfajldNnpBp2TIuex9OkRBhQaW44MJJjnFtNlLRqkTMSwHXrqpKmOuj6H2KU5yU9WCbTMoHgCyg9nUAVXfxkRsQDR3DgbKGTQe0yyUhjJId-Zq-sPdr6Jb6LOLxaNf7jHYqv9Qb1G1OZhNdbvgxqbBQvxCqbwDLiqQyI-o2N_G5orNhMroSKY6z5xB8tYbK3ERL9yA47PLVEvk3s2ClfrK697wAVcrzIqa6ecgrBeEOiFPUnU9n9LyomzA6B6lHjki8wrtmobri2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=grTmg2rGLWRE4muE2r1daam_Pg1TsBhRLbJR9-NGwDPfHg_aXrkzC1KuFp4emvhD6pyajW8k6CWcwc2ORWrbJTbeijGH65wzEHE1J0sMML5cmyLL-cFbUhkGPCDj9OU_v1YNEnbmpRAXoUWnfB9JdVDg-x0nl-TObJQD7nPFJ8FaZRRlJj5xwv3WbBOEePP7aHxFDwziZDA9FnthKuUo8bAnfwk-fQknBVyLAaRxZVmXDSGuxQ-7FSPyR-q40N0OfdrucdV-8ua_V0dLHEx0yegPDP23RJrFJCe9P4bds1AiWQi5O6ulYwHjn9kfzxVhFsId5-QhbEijRi_mOOjoMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=grTmg2rGLWRE4muE2r1daam_Pg1TsBhRLbJR9-NGwDPfHg_aXrkzC1KuFp4emvhD6pyajW8k6CWcwc2ORWrbJTbeijGH65wzEHE1J0sMML5cmyLL-cFbUhkGPCDj9OU_v1YNEnbmpRAXoUWnfB9JdVDg-x0nl-TObJQD7nPFJ8FaZRRlJj5xwv3WbBOEePP7aHxFDwziZDA9FnthKuUo8bAnfwk-fQknBVyLAaRxZVmXDSGuxQ-7FSPyR-q40N0OfdrucdV-8ua_V0dLHEx0yegPDP23RJrFJCe9P4bds1AiWQi5O6ulYwHjn9kfzxVhFsId5-QhbEijRi_mOOjoMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLCjFW-jEFyH3FHMW1HGOilLFFcvWKAMP7F9QcSXF89vNfxcMIVyhuHmdsngdpSsUDP2-6hdx6EDS4Gyh4Hqd8BQqugM3ZjdzPj6f25T-WceREM0Hywes8YxOGhLBOZ66knZbKrq2JbPw7gPJiH1G9Y4gP7vx5SLRkboZXw5yyyb6lSOXD-s2tbEIg8sB5nQZMC_GAna7ED9zXMAcMFDBhbdkCh4XsuD-PBBy58A_l1sJxR-7oxfUH6xy-GAPrOAbF19IpKhm55BoexwZ7Ndl5I-5I7QiUsW3XIJoGltJK6k-xQ2XCTOzoHPehdny9vYiUOFD1RehkA7kbIDatBmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=SGmk2G6c8mwL3xtjEumuluICwRLiM1C_VuLjniik2fdq1plmqtbXtgoXWjgvuT1D4mKs_2CvEqVxn69CRfqYNqr61M73zMuTBxQyjL9fCbtcQR32pHpIrvBAMqCZqPRokf5qYgb9_3lOfQhmLq-u6_sBI0yW7arJFqNOxiHw79wxHIfuleWfQ9M06n5MxKUcBajBav_1Udqm5Cq14waZvbhOCm8geY5rC3ClUnTffXIJpP-AdwAiK_NkZCe58hnUNtOwbfLJRTS_fnxQ3tRVeq9R_1pVJ14BcBOEfXrxotbJMdjlerbmuNBT-zWWI-ZlWun43yyn52JKDJK8LqPxmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=SGmk2G6c8mwL3xtjEumuluICwRLiM1C_VuLjniik2fdq1plmqtbXtgoXWjgvuT1D4mKs_2CvEqVxn69CRfqYNqr61M73zMuTBxQyjL9fCbtcQR32pHpIrvBAMqCZqPRokf5qYgb9_3lOfQhmLq-u6_sBI0yW7arJFqNOxiHw79wxHIfuleWfQ9M06n5MxKUcBajBav_1Udqm5Cq14waZvbhOCm8geY5rC3ClUnTffXIJpP-AdwAiK_NkZCe58hnUNtOwbfLJRTS_fnxQ3tRVeq9R_1pVJ14BcBOEfXrxotbJMdjlerbmuNBT-zWWI-ZlWun43yyn52JKDJK8LqPxmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66335">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555366529c.mp4?token=izN9oSFGrLELdFJI2_V7JppaexsWMpVX2F2QNNoLe7XigzKjZD0hkvJEnggBA2OhStbvll3xRAzoYEB1JS0JpJzZecS7O8AHNyFHKwIuuZlL9IhT1NAJU4Z7tEdSq8HCDs2pQw4r9jq0_Jccb4y0M1J_46IFgWeflAf7qOl2bEKgALy6WFqA8FI4-W7bvjEXyl8002FfZ3LO-L0sUDQicYfNjNGVeVLVsC7CdA-GT1fzNg9-_X8mp7Q_T7bZa4Ew-RygAGoo_ctxWmLvZmZO6Z9v_ejGF_9FQrmrK6NswCyWVUNabU0WGpPAXUWO31ZtOersZptkyEXEODDY5XFQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555366529c.mp4?token=izN9oSFGrLELdFJI2_V7JppaexsWMpVX2F2QNNoLe7XigzKjZD0hkvJEnggBA2OhStbvll3xRAzoYEB1JS0JpJzZecS7O8AHNyFHKwIuuZlL9IhT1NAJU4Z7tEdSq8HCDs2pQw4r9jq0_Jccb4y0M1J_46IFgWeflAf7qOl2bEKgALy6WFqA8FI4-W7bvjEXyl8002FfZ3LO-L0sUDQicYfNjNGVeVLVsC7CdA-GT1fzNg9-_X8mp7Q_T7bZa4Ew-RygAGoo_ctxWmLvZmZO6Z9v_ejGF_9FQrmrK6NswCyWVUNabU0WGpPAXUWO31ZtOersZptkyEXEODDY5XFQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقتی نماینده میخواد ثابت کنه زندگی ساده ای داره و اونجور که همه فکر میکنن نیست
😂
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66335" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/an6kYLBm4XLRDbOMgk2lboXuIZcL7Ik48ClJKrI5oDdUqtYDSt5MewrkdCT3bcUPI672_Oxc33H2bpsXVy6wmdSrwIQ6MADeYuREqcoSiv_Fw9qiHHscq1p8rT-Psl1lN9YXtadksok0t_CchcbCCDlNKNuBLf5iMixoXGuCM9Qjvay7lUGMu_vzV3LMw58bQyKX6uvTd4To4PT1ahvfN5iZc7LnYIjFcQask7_m0B-JISbXgggmdtDu_Qc3KVWiD-uy9riVPiXEM-wPKuwHJFuSXl1ZuyEFR8uuVitQ3LED8aHWOliGY7uTQU1MgSQSV0ku6Y9TevyB9ov73tdHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=dejfV6veDUOyqfpus-ldxcfcdZ5n9idi43a33ULuHx9EboQGW9067__8hn4WUaMN-JLqAbPS2Sdmxydllw9B5lGb5gIlqt2BYHij8w6TiPGzawV2q-WBO76KLhfoutkGAZCZquTOf3LAE58b1vAyf5LMt9Uc5LH9zMyrP4q_aLoyPFPchmN8U-uW7MWUY4R0PQ1aicMImAMBHAIZMJXP13utmExIaTDc3LR-qmbEIYARAeDiRd_UqCwNc3-np5T1GPBbq-1zUhMSTajAWDADKxYksSghDImkqWLcnOoEvuWe49RDF2u5nJfwvKaiYSG1SxUqvpOBabNrznpgJbE4gYbqu5UYX9-M1jUIWysTznyVlcoyPdSITkOTsKu-hPiVYSN_zRckz6USNP_OqMF_Gt_6YQ3-F8EbUAFbJpR_pDxo0Y8f-IoWrhAg0IAr98Sm8BwyowuoGyWboBF7_QGEkmOP2irTdrQsgH8mBGF5W0nHDAXDLyvYCnh4fzNcwESb0iQe4rJZetehSyK4PpBojk6JeBEtXjDL_zBsJoOk4iFeYcrZqGW5pgkHf3tSDdHNYvAcN8Mdo-coMY2PiZW_iwduTcArJofD9fHtkN5JX0B-E1_endulOnIZtLzZJYPfQNtYc13BIIFMp8yrN7NrZXsi_awfOMsXGMBBd7UeePU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=dejfV6veDUOyqfpus-ldxcfcdZ5n9idi43a33ULuHx9EboQGW9067__8hn4WUaMN-JLqAbPS2Sdmxydllw9B5lGb5gIlqt2BYHij8w6TiPGzawV2q-WBO76KLhfoutkGAZCZquTOf3LAE58b1vAyf5LMt9Uc5LH9zMyrP4q_aLoyPFPchmN8U-uW7MWUY4R0PQ1aicMImAMBHAIZMJXP13utmExIaTDc3LR-qmbEIYARAeDiRd_UqCwNc3-np5T1GPBbq-1zUhMSTajAWDADKxYksSghDImkqWLcnOoEvuWe49RDF2u5nJfwvKaiYSG1SxUqvpOBabNrznpgJbE4gYbqu5UYX9-M1jUIWysTznyVlcoyPdSITkOTsKu-hPiVYSN_zRckz6USNP_OqMF_Gt_6YQ3-F8EbUAFbJpR_pDxo0Y8f-IoWrhAg0IAr98Sm8BwyowuoGyWboBF7_QGEkmOP2irTdrQsgH8mBGF5W0nHDAXDLyvYCnh4fzNcwESb0iQe4rJZetehSyK4PpBojk6JeBEtXjDL_zBsJoOk4iFeYcrZqGW5pgkHf3tSDdHNYvAcN8Mdo-coMY2PiZW_iwduTcArJofD9fHtkN5JX0B-E1_endulOnIZtLzZJYPfQNtYc13BIIFMp8yrN7NrZXsi_awfOMsXGMBBd7UeePU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=CGZWV4ihaRZJ5iaSRGOCuR01Txbi_BIMaAXDB-CfVDw6aVAj8gUIzWhuM6k9Rtab_mP09TXXw04oBWjhtx9I6rwtNipe4BXO1AAqwfSQHES038fLaNO6n4CKUwcqwdG8nLNbMPjDnUPN8q-xLbPRhBtOyTp80bzqcpQk9JlVDdLzUm6s0TB0CZSOO8LipHO9FL1Aa_aYxadcas12meMwJiJBOjtdUPRn79Zz-2qFmnL0iBlIZlhbshF2p2EqI8VqPujAXXOZeSly6ZXncNiu1xIFjxmrYza2dsAPNFEgNKtB3_sfVL5B8WhhE7pWKy1rOJkf5ypWBbnP3eDm7rgmsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=CGZWV4ihaRZJ5iaSRGOCuR01Txbi_BIMaAXDB-CfVDw6aVAj8gUIzWhuM6k9Rtab_mP09TXXw04oBWjhtx9I6rwtNipe4BXO1AAqwfSQHES038fLaNO6n4CKUwcqwdG8nLNbMPjDnUPN8q-xLbPRhBtOyTp80bzqcpQk9JlVDdLzUm6s0TB0CZSOO8LipHO9FL1Aa_aYxadcas12meMwJiJBOjtdUPRn79Zz-2qFmnL0iBlIZlhbshF2p2EqI8VqPujAXXOZeSly6ZXncNiu1xIFjxmrYza2dsAPNFEgNKtB3_sfVL5B8WhhE7pWKy1rOJkf5ypWBbnP3eDm7rgmsoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=baXxdeuj11sB7AmvQmKlayIIKAGrsju174ZAh8tJ7eyk-aoUW13rH7tiBvpRmBoYKTqaEZbxJFgFt7ujRtqQ3ykt5tMRVDkavx_4qPy5NPiW_JeWgT-D9B7m1U6rD4g3q3ffiGs9t65joPLAbVMP_IKnHNQRssw5LM8v3SK_GYD0sHUBkPKv70qgxQU27TEn4UpYXPgpuXNjX88AE2V4t30mpSkMjkZFkSaAGlIw4qMKW4P_SarbsMNw6ESmpeA_Cd6reqvG95FzKFiexFTmDOBXZdKstGprukzrYyOahd1izHLmVInCpu7QYV1x7zfwT51bkz42devRuhu-tfd96XGCjzlQM887W1NSZ2WvKs6JIlOnDuMLeZYYIsf54aXgA0MdVhLfY2nFZxRE8hxKtalJF3CMxCTfgjz-x7HJ5TPHLj_KbH2u85sFX2CEvZk-ihYZK1dGAAn6yuAehMKOwpRcPAW1BdNUfIVKTisdPBoLm7CqTW9n1J_K5eWMeoHsy-YWGTNG36RkwcF-31oxzYKXsllpy3Nfxm_iC6vZLT0JZtdXzxssTPApvwVc9f8uzUZygWaVINxaA6OFSVAbimHR8rcCfccKq2NlBvGikfZN668Cy8cRcWrbzUqRCMGTGmwgP51atrOzfNb-T6WNyQ3Tmi9RdmLlHVzEdxo_2qY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=baXxdeuj11sB7AmvQmKlayIIKAGrsju174ZAh8tJ7eyk-aoUW13rH7tiBvpRmBoYKTqaEZbxJFgFt7ujRtqQ3ykt5tMRVDkavx_4qPy5NPiW_JeWgT-D9B7m1U6rD4g3q3ffiGs9t65joPLAbVMP_IKnHNQRssw5LM8v3SK_GYD0sHUBkPKv70qgxQU27TEn4UpYXPgpuXNjX88AE2V4t30mpSkMjkZFkSaAGlIw4qMKW4P_SarbsMNw6ESmpeA_Cd6reqvG95FzKFiexFTmDOBXZdKstGprukzrYyOahd1izHLmVInCpu7QYV1x7zfwT51bkz42devRuhu-tfd96XGCjzlQM887W1NSZ2WvKs6JIlOnDuMLeZYYIsf54aXgA0MdVhLfY2nFZxRE8hxKtalJF3CMxCTfgjz-x7HJ5TPHLj_KbH2u85sFX2CEvZk-ihYZK1dGAAn6yuAehMKOwpRcPAW1BdNUfIVKTisdPBoLm7CqTW9n1J_K5eWMeoHsy-YWGTNG36RkwcF-31oxzYKXsllpy3Nfxm_iC6vZLT0JZtdXzxssTPApvwVc9f8uzUZygWaVINxaA6OFSVAbimHR8rcCfccKq2NlBvGikfZN668Cy8cRcWrbzUqRCMGTGmwgP51atrOzfNb-T6WNyQ3Tmi9RdmLlHVzEdxo_2qY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=MkfvQiW7YD5U6Yrepoi-pJuy1JueyAY8s38MUYlBUqtRL0zCByq7HcCV138MrvCVYUwvZi0IMCJVhKGfy3810XZdhrpCnH4HAK93mVj-hO92thfQeXs3D5mV0bQElMqGAK3ikKUKTD8m6_qMpLfQnMCRsZdejGK2Ujiz0QXxiEllacmK2Eba0kxttzMC0RerH6Y79Z97Lgy0NpUX-WlDYAgZAKm_O2nj_4-afYHWt3tFFGd71QggBQ_ml5G4isrTPeiLjD7t5hBYCtp10OUyk1NZJkAhYmJLIJMI1HcLg3DZZN_Rihz3ZvoWPNB5vdwKrvvIOsfcaLYbrTaZTnURIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=MkfvQiW7YD5U6Yrepoi-pJuy1JueyAY8s38MUYlBUqtRL0zCByq7HcCV138MrvCVYUwvZi0IMCJVhKGfy3810XZdhrpCnH4HAK93mVj-hO92thfQeXs3D5mV0bQElMqGAK3ikKUKTD8m6_qMpLfQnMCRsZdejGK2Ujiz0QXxiEllacmK2Eba0kxttzMC0RerH6Y79Z97Lgy0NpUX-WlDYAgZAKm_O2nj_4-afYHWt3tFFGd71QggBQ_ml5G4isrTPeiLjD7t5hBYCtp10OUyk1NZJkAhYmJLIJMI1HcLg3DZZN_Rihz3ZvoWPNB5vdwKrvvIOsfcaLYbrTaZTnURIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=uE9HEMAoYuyaF0pIou6yqPoUpGP3lqgDaVcYm9RGKY3R_Nl--SrETAglQ7hfb_xHCKS1T9ov9Q8ro038LFQD35pFFA9rO2Vk5AywOn1mYZTS2UsLLjQYzRs8ItA6GjoEUt6r29N1E1un3J4roHXkkt3R8bHPnzD5s8pGSF529JW3cNcSmbXiRv6rAttpyMiwbZB2fOo4pCc3iOekQuFaI6P0cIU8bRcmPaBoYSAioNSALdJ1f8ngaAIUVFdma5CCkE7snM57gKaNOO1nrYWP8n0Gu5NGyDYXn2WF_VvtqGjzaJgp4B1AxU3GnVmmrYKFEcKnc9aXYu648fFlVoFDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=uE9HEMAoYuyaF0pIou6yqPoUpGP3lqgDaVcYm9RGKY3R_Nl--SrETAglQ7hfb_xHCKS1T9ov9Q8ro038LFQD35pFFA9rO2Vk5AywOn1mYZTS2UsLLjQYzRs8ItA6GjoEUt6r29N1E1un3J4roHXkkt3R8bHPnzD5s8pGSF529JW3cNcSmbXiRv6rAttpyMiwbZB2fOo4pCc3iOekQuFaI6P0cIU8bRcmPaBoYSAioNSALdJ1f8ngaAIUVFdma5CCkE7snM57gKaNOO1nrYWP8n0Gu5NGyDYXn2WF_VvtqGjzaJgp4B1AxU3GnVmmrYKFEcKnc9aXYu648fFlVoFDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=aiQgRTMRO1aMXv5B3vjYuEf0toS8eSNFuH3h95nMWqgRX791jmrsF-GzAdkxc4UtJWOuN36SZILCQS2BtiLz2rDsCIOVExCuFeiBdumFPMQJwz9q1ayx84QRFLZCabQmwXs8hH0MMnVzmvOU1UCDadd9UAL8UmG1y4iIcB4fqEA-urKv_OhZtl-B0DqfFKqXKUBpbfwFs8kuVO9U1_J1QGWrXdMPFRAfUMQ_tUXHo4QaCxXVMwvpc3ofNs3rn7yBciMeIr3z4OXz6ZhHur8ze-UG1DIMOK4imY6CEuzHFV97Eoy-1EpvIvb51sKvzDNy3sKl9tjmiXTt0JHtaDaI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=aiQgRTMRO1aMXv5B3vjYuEf0toS8eSNFuH3h95nMWqgRX791jmrsF-GzAdkxc4UtJWOuN36SZILCQS2BtiLz2rDsCIOVExCuFeiBdumFPMQJwz9q1ayx84QRFLZCabQmwXs8hH0MMnVzmvOU1UCDadd9UAL8UmG1y4iIcB4fqEA-urKv_OhZtl-B0DqfFKqXKUBpbfwFs8kuVO9U1_J1QGWrXdMPFRAfUMQ_tUXHo4QaCxXVMwvpc3ofNs3rn7yBciMeIr3z4OXz6ZhHur8ze-UG1DIMOK4imY6CEuzHFV97Eoy-1EpvIvb51sKvzDNy3sKl9tjmiXTt0JHtaDaI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=JyR6alt5Ym1_AFtvkGu0qLiPBEQpocXX7h22jCWpT2BaK0CTL_hx-lVTH-0pVWqDu7LWX-A1E8aoXwppWTUpl8-oXJ8-5Ux7JAfqXU6L00q-v3ZBKclN33rQGu-5rDXJFj0ahPEyi_6nU7r1Kgx4j57TspqZ3YOo4_2tA_EaJ1mn-1VTJfdClZJCsLnvH0LhDQTh3dL1VJpsmEZQqb5BMBSAJPcbW6hlFGvN-__omUuUl80cmRUd6DdjperyXvJweXtva0zdXwnvVSA5_u_wwZj9yg7Hsl3VJhF4sTxnW6Ke84p8_Mnigy_EFonikvjwJ2l0b0qAilfsitwZifLvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=JyR6alt5Ym1_AFtvkGu0qLiPBEQpocXX7h22jCWpT2BaK0CTL_hx-lVTH-0pVWqDu7LWX-A1E8aoXwppWTUpl8-oXJ8-5Ux7JAfqXU6L00q-v3ZBKclN33rQGu-5rDXJFj0ahPEyi_6nU7r1Kgx4j57TspqZ3YOo4_2tA_EaJ1mn-1VTJfdClZJCsLnvH0LhDQTh3dL1VJpsmEZQqb5BMBSAJPcbW6hlFGvN-__omUuUl80cmRUd6DdjperyXvJweXtva0zdXwnvVSA5_u_wwZj9yg7Hsl3VJhF4sTxnW6Ke84p8_Mnigy_EFonikvjwJ2l0b0qAilfsitwZifLvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
#فورییی
؛قرارگاه مرکزی خاتم الانبیاء:
اگر ارتش رژیم صهیونیستی حملات خود را در جنوب لبنان متوقف نکند، باید منتظر پاسخ سختی از سوی ما باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66321" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66320">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=JK12iYRNCpkpI5kwuzZ9TU8VxBM5QVDQWKfJVtMHxZLhYL2-zpm52I8omN_P7TDYGe5a80MuHIXbZSlzJcPk7grdAxtZqFNeNKTGrva1F1swYtX4hA4gQXPVM4GoH_HZxnLd6wls_4UvpnbNwRfr9Kjl6yal_ZqfDL4YowhhkDYfRQ-2yCuzY2LuvGxw6sgY_ctJ7FGU2pju9NO898KfZbdmv8MS28IgGYG_tpUAQVn8Bl1l50Amx4J7u_4lxB9UPqgfNKFwOvfza_ECfQ4FGmUTfI2bJMhZGLfIo5h0hIvTcyixjrZtQdM9Mmaa2uwBWYBx1OwXKgeqNAcW_wJGsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=JK12iYRNCpkpI5kwuzZ9TU8VxBM5QVDQWKfJVtMHxZLhYL2-zpm52I8omN_P7TDYGe5a80MuHIXbZSlzJcPk7grdAxtZqFNeNKTGrva1F1swYtX4hA4gQXPVM4GoH_HZxnLd6wls_4UvpnbNwRfr9Kjl6yal_ZqfDL4YowhhkDYfRQ-2yCuzY2LuvGxw6sgY_ctJ7FGU2pju9NO898KfZbdmv8MS28IgGYG_tpUAQVn8Bl1l50Amx4J7u_4lxB9UPqgfNKFwOvfza_ECfQ4FGmUTfI2bJMhZGLfIo5h0hIvTcyixjrZtQdM9Mmaa2uwBWYBx1OwXKgeqNAcW_wJGsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنوز سواله برام؛چرا خارج شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66320" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXINfOcO_C_XrecTK3H23tWfSklNeCWBOfHEIw2S9yRY3YF2S3mI5XHT1bRzSISFgrNIE-ntksmYUc9u2LUVCJ8zVAbcOprwffvrpfLZ7NIglVFUsJg2KrjtAyTnyAqufzPi0RXyTRyIAIKJ84c5CVqnckY98lRh-pw2g9QLrJtKXldhFqa7k1edG1108kiP5o8YEa37JnwSeWOBn4ggGWv8sl6h2AWMFiC8V1MBYnICt2WaRL_B-r4K7ygknQz4vvRM-iBeMORLqrtMEq_NLtQjRUbht1LR-fyvIRP_N1v_PR3BrC_0ZX-mnbjB71kMqayCnPTETfby1jvPoBaRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=HUZrU1qZoUD_euyr01k4xMRe64Fj3ZZhCF3vTgVmUNUvWSzRG0TlvIK6cEegH4dca_UKGrsMrpyXP2TWev4f9lgRYV8qnNamFfip9uglAiPpx0gfyzZwbHVobH2TB10U-faLhTou73WIQ2F9AZU_QErmu8rhYPg-hSt9m_Kx7WehsGtQ1PYDNqFa6vHAn5qcHYewIHuicXXvUkgNzmO0zjxkYycbRi_6iE1Qzs1XyvboY5mRF_fucsMd5xgYVBwcJL27TwlSGwm1trDF_pa44oB19pp2PK4hINDO2nfxtsmexlRZbVybxopBzW4vhK2yBLdUtMnVwRCIzSjd8-Xlvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=HUZrU1qZoUD_euyr01k4xMRe64Fj3ZZhCF3vTgVmUNUvWSzRG0TlvIK6cEegH4dca_UKGrsMrpyXP2TWev4f9lgRYV8qnNamFfip9uglAiPpx0gfyzZwbHVobH2TB10U-faLhTou73WIQ2F9AZU_QErmu8rhYPg-hSt9m_Kx7WehsGtQ1PYDNqFa6vHAn5qcHYewIHuicXXvUkgNzmO0zjxkYycbRi_6iE1Qzs1XyvboY5mRF_fucsMd5xgYVBwcJL27TwlSGwm1trDF_pa44oB19pp2PK4hINDO2nfxtsmexlRZbVybxopBzW4vhK2yBLdUtMnVwRCIzSjd8-Xlvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpxmTOKcE_SPMi0bWQsskCDZQ0sL2cgyPCP-JGPMYozbJT3fZRRuwjQKXPtgoCyszhibcKl19mGV_9G4elw556Dp_c8oiuuz7LGqdV0NmLDRt2ARZADCeWxIki7A8AeVOHyYZZLp388EqGxa6kkqcyf6LwDwxRjjIFpvOadB7aO4pLEJA8Q7UAPyZJLAY5cSi7AiSYHQFESliszj8W9UshmH6CQDnDantTC65Ygbe77OHz3gDWx1Ok8is43_KiywZwvEs7nWCn4-9sONIMTPZxzOzd1r1smv_UvyWuqnu2OWWjhbgw4LADVEiFZMBO6UCQrJLjflDOvkPuHupG7KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDxwyB3HP1NpUVlJUaJFnjvcYJeR14n2bCjmyfYfUCwcoh0eTQVhklK173AIhH_J996iNNVAgwoHo14YCfKtZ5X71HncFiBnTBbcsy9osFw9QV5LkJ3NqaIa_X1pb3tlSLC-fOsWf3n-hfHLAG5gmzalb2VCwCte8XdMFeoe1Q8s-xQHKSaMZkKBR_1NgD3Mei1BKWfDZ9TcQL80_D9jd8mt0Ye7_BHLPWUnMy3NNKNy9RwJt5Qe6rdlwzt39cZgY8Dlctg7h8I0UKRAZXy6DCRVB-4ixuSiTU3eVIXqOnnKJxX1kE_ZPncTzPvZ2lwblNGp-SwRe4IRMYiEnzWX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
