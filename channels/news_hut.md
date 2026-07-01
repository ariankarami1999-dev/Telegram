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
<img src="https://cdn4.telesco.pe/file/dZgscLsOJWDZJWaENpraM0Vmeti-gSV910qZ7AmchnSSzfgu5t1fm_WcOp3yVF_zQea3eJPGaBK8R2DKsUmTSgIDeJPYpYVEuuNTj_7bcUg5IPEm-j_uEWLBQIV9zNWSygz-zyE07ICylBZK_R6TY-s97Bz3gn4BFOo6kMM1udyxh3e23EYJJoE2Xf1T8L5xUu-C-gE-iIpYJUJWe4KKDjp_GhKDA0sZvSV_ULbQFGUI42J5CcOqWPN-m79qldGh451HsOZD4ELIgHcycADi3_PYervWGfulEAKfj0FTWjCwHtI5XFIO3uJivAPewBXS9xP-VVDdTYGaJArHWm99YQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 215K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 15:22:34</div>
<hr>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvIfb01H-0LAeb_oAfAGusg3T2cDUjVu7qqVuFf-MpA7WckJvU-s1Vd3YlKaQ_aW32010Yms-X7jTHOzDho6YyxY5Ip5ef8dnAHFZqv_moJfhT-nACbUXUsiTd827hxsEy0p_HhRCdcwwzxKGeaXQwy2kmQmqetAiJI1eHIbSvpQGilwabO61_JHrgDlUydR2XAVMefe8woeVKMmIKAEgLVhUuhAdW3DygAbj8WQC00aZL0yBstSPqW7I-YtUvCLmvMvHubKqv2q3BQVQrc7GDOrGWhgbPM1bHm5cJj4z1CoSAs-kQT6ZZ2BnWsAmVl8jIZ2RZmapzbWtUK30fttDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBneLo0u2_UOGTmOUffr4Gs8sG6hESRiaDftGYLGCQZJDtelqNeZLjxXIW8zbdPGplANGtRQ0XFfJ9lmUvjtOtABR3Dwv6o81neOduWi7HgyrwlvuzIeW50Xhlc4zTobavks5SHJDcIsKKrvHrgmuUHzs_FY7Y9TkvnCG3nuPrkEaIJ6CZsLpiLHfg3p1TapK_3TzlBcwiBKkK7WjJWLjTG1g298dfGNG9SmQR_GVy1DRLM7iouWJUKtdzMWlWXdcSRv3WfDqz41AqOzHeF4rLOaO2EQaIqBicGbPGGH3rDfi_KigpGc0NyujrYsKH4ceSTciD3mHN2d3i8PLpHZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiKHhF0ELrnyr79vcU6I56haCbVVgKkE4ylh1S2Sf_2FzHd44SQSA6e7E-xXl3BpgRLwxAGdr-zqcFqA_6M5Mx4nGabI_-zUypaD6Mz9b7BTCRxxSjnAVl6AlPQ_llghjDLKaSkJdbAzYKtpQqPZt6U2pZC5Fx1JVo_bu_2jkoLDy4CuzjMV3GM1fR95O0ThEgDcoIMMrvNGlV8VYTMOLWpuEnYPA8prnNiQ8Q16oCwgkNTvSIGl9LwPZCNrcU9HsMQQxc3_W8JVuZPysh1O9dSUrDHh9fW4lsh5VhducsV05KNBg_xVwEWus9Si5WdD9Y0pggWJ-TYYUuo5JXfvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=KTTmAQeYectZQw8D7CfKAsKkeLrqO68mn-q7gK3lkJESfa1hi9KghkiRI65N-xVOJ7bGL5LtK20xVvOFKikzDdzH59LR-8ZVRxlMZ_dlxqMx8O9oMrlUfjB88MdnGsKyyRxyOnOpiQFRLP9Ua_IU53pw64oG8kuS7j4gmcwdsAsZdDPjgCiySTWyInIqtC_-sjWDh8GdyiQP3EZBcBDQ7TO0zM8WZ4XTyhEjzWmiEUbMdKBLl66K7nNJyLTeHXRM96R_PPTVVeLI6DYyqF5QfPKXgJeSq2K9nvNNvkbBtV-8tJOjSIKjMS0jRAULYTakULGu8bgKQ-4RgOwj2W_XRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=KTTmAQeYectZQw8D7CfKAsKkeLrqO68mn-q7gK3lkJESfa1hi9KghkiRI65N-xVOJ7bGL5LtK20xVvOFKikzDdzH59LR-8ZVRxlMZ_dlxqMx8O9oMrlUfjB88MdnGsKyyRxyOnOpiQFRLP9Ua_IU53pw64oG8kuS7j4gmcwdsAsZdDPjgCiySTWyInIqtC_-sjWDh8GdyiQP3EZBcBDQ7TO0zM8WZ4XTyhEjzWmiEUbMdKBLl66K7nNJyLTeHXRM96R_PPTVVeLI6DYyqF5QfPKXgJeSq2K9nvNNvkbBtV-8tJOjSIKjMS0jRAULYTakULGu8bgKQ-4RgOwj2W_XRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lV7ONs_qKNoluYCc1YrJ3fN-7NvMxgM2cBTER6_shzy4WKvqFR60BOwAdvlTGSbHvxkm_5szMZ2dbEqXrPeeiviYWddrH3EfLPybmhRjQBe7NUF7MBcYI85IN-Y8vFrCO0vP-qXy-zybU4Iau-Db8dTkfqRgDYJADepp8f7_L6062wZPAkQB83S4ouGNF_ipAkTxpsBi1fF4JK8AxE0YVygEWWzzAVz4JvQikkgFwT3YVTICMePYIVLlL6PMkcszhPVhlZ5ROhaIknmHhUAXC8S0odnIoWU16kHH0ZOxTf39YehlevlXmz8LC2xQDZBWkh1rz9YTpJ3Xq4Ef46fW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe6NBDFT2yhxoGK7f83jXn8gI3ckx1I9MsZNrl6MKVVKkQBv4x8zOAtOYbAIQ-YApJgJMmBTz5EXWutPO2wtyx68t3Rrifgeh3apVQc7mu0OKuLl1_4j13D0EDClaXbiPazxRHIhLAej0ldivN9Qdy8KMIwsaSbgYeKYyUlOukAHs1yUAfJjcl1gtmcNseBppNNz3-8yFjxDcFZlCW4uh6ML8BKBXlDSasQeJrwo1UvJfPYbqvzjRjSnnbUW1gNizMifDJ0VxLl2YqAIHou5XLj4p6JHk7qY790etdwsAL53zAMdF1tEAEZNfRcmcIooKAkf1lK4FiUyyGWu60WY1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=AuyyZ6F8vL4fwJzqG5-a_VDEY1NOtGiiEa5gbOAlBUeSfJdEVjMwVLPy84UoTLD4qN97kwmLpHf_tgNPI9g7gJhvcZ2g9GUgInGeg_REiIDpvDPmEAN_TY5yJwjLh9OsarkitP_6Js5wJ6fW0--HwDcd8LtPeJ33GdswLeReNM9JPygcVPC3_TWBA42VbrU_50MJhox9rfiCLhvhJgXjVcRDXEs0jYVVTR1LyxVzcCRQrL7CucVZKqkcf0w87VZvJUpgO1G13csVxGt4jGup0ICvt3dCslFKtYSox9_XOkq4s6sxG6Ep47jcbU-HRyQ_AW9sDukqOMPM2TOtPg_aLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=AuyyZ6F8vL4fwJzqG5-a_VDEY1NOtGiiEa5gbOAlBUeSfJdEVjMwVLPy84UoTLD4qN97kwmLpHf_tgNPI9g7gJhvcZ2g9GUgInGeg_REiIDpvDPmEAN_TY5yJwjLh9OsarkitP_6Js5wJ6fW0--HwDcd8LtPeJ33GdswLeReNM9JPygcVPC3_TWBA42VbrU_50MJhox9rfiCLhvhJgXjVcRDXEs0jYVVTR1LyxVzcCRQrL7CucVZKqkcf0w87VZvJUpgO1G13csVxGt4jGup0ICvt3dCslFKtYSox9_XOkq4s6sxG6Ep47jcbU-HRyQ_AW9sDukqOMPM2TOtPg_aLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=HrR_Th6BESep1Hn07yHjFKiQgqboRkjVs0-5mso5Yg15ilqk9ko5XNCkXJN5sVrUctmI3QayUXdK-Ylq5KaZIsSrYs87XbmjPLxETkxWvc9f-DLs06DyGseLWxti56cIa7ZxlXlzR4SsMinHMiXqB7YtsonXlqDZ0DXFotGEHgLMX8xDECezdGEIIDeRWLM2h0b_UVLNe0L9iYjdn6BQP-AKrF-fO2zYp03_Z_O_RvvagRO1T2KzOFhlO1DgYix5w8uieF77c2eG_sy6Av4yHzoU79X1f1Jkp84F4AsOpGA0SC1uKz0dnnmgZ0cHuFTr67MWcxoJw3f7PbrIdciV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=HrR_Th6BESep1Hn07yHjFKiQgqboRkjVs0-5mso5Yg15ilqk9ko5XNCkXJN5sVrUctmI3QayUXdK-Ylq5KaZIsSrYs87XbmjPLxETkxWvc9f-DLs06DyGseLWxti56cIa7ZxlXlzR4SsMinHMiXqB7YtsonXlqDZ0DXFotGEHgLMX8xDECezdGEIIDeRWLM2h0b_UVLNe0L9iYjdn6BQP-AKrF-fO2zYp03_Z_O_RvvagRO1T2KzOFhlO1DgYix5w8uieF77c2eG_sy6Av4yHzoU79X1f1Jkp84F4AsOpGA0SC1uKz0dnnmgZ0cHuFTr67MWcxoJw3f7PbrIdciV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=XPPz-XaFocdDCWZCoKI53mfbjs1UUm2pyzv4WLUdz8pceDsy6ibceWBkcRd_0yvo0LqbkzOCkBFQx5kKLRZKoDT8KnDCsA1N2nWWRSqIzEY93B-n2n7ENSMSKqYqTfSluD2NlhEwFvKRUxlo44ZtdpoZ-VHMfjzC_H-p4GlA1Bxku17a6gfJi5L50Dw0Gn_YDiIi_uK_0gOi2peXWu0mAUcf8WJCUWOnSgpyW8xbDeFeniYn4ufDDi7freiTuATU1rmQSENDnXQx2HlckNwEIZL4J2BGi4ZIsK7O8qWkNLIa2uUZgSxs8ErsS5Ff0jwES8UHpboC0zI_47N1NUBw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=XPPz-XaFocdDCWZCoKI53mfbjs1UUm2pyzv4WLUdz8pceDsy6ibceWBkcRd_0yvo0LqbkzOCkBFQx5kKLRZKoDT8KnDCsA1N2nWWRSqIzEY93B-n2n7ENSMSKqYqTfSluD2NlhEwFvKRUxlo44ZtdpoZ-VHMfjzC_H-p4GlA1Bxku17a6gfJi5L50Dw0Gn_YDiIi_uK_0gOi2peXWu0mAUcf8WJCUWOnSgpyW8xbDeFeniYn4ufDDi7freiTuATU1rmQSENDnXQx2HlckNwEIZL4J2BGi4ZIsK7O8qWkNLIa2uUZgSxs8ErsS5Ff0jwES8UHpboC0zI_47N1NUBw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Y9cuVlUYZ8k2gseV0n-cjZbHl4dLBFE_2B4ns5TWMkKfiigtMJN8Rvikw5nK906QiK2x5kcbhpRI_mLqlqK9iK3oBKRPMr4qfWquijG396DhskQ75aljSMU2IrPacrU5DuypR21WcwbCXPrxQRPd51TKV0EdesPO31m4UC9e-2n6xjkDeTwZepXajlDTK1vYCY4UP_nZscnslNL0xa6eOWPrGJnzN2kv8aj7tX1CdDRJhsLHYOQ-Q4KNe_8KtfOQ5FxdxNGwU8Cd89e-x1xYIkDBKpurI2erLSESjgMeLNZi5Ye6ytixZMeqIXtLNxbBBIu43ZgzC-g86NDd7krU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Y9cuVlUYZ8k2gseV0n-cjZbHl4dLBFE_2B4ns5TWMkKfiigtMJN8Rvikw5nK906QiK2x5kcbhpRI_mLqlqK9iK3oBKRPMr4qfWquijG396DhskQ75aljSMU2IrPacrU5DuypR21WcwbCXPrxQRPd51TKV0EdesPO31m4UC9e-2n6xjkDeTwZepXajlDTK1vYCY4UP_nZscnslNL0xa6eOWPrGJnzN2kv8aj7tX1CdDRJhsLHYOQ-Q4KNe_8KtfOQ5FxdxNGwU8Cd89e-x1xYIkDBKpurI2erLSESjgMeLNZi5Ye6ytixZMeqIXtLNxbBBIu43ZgzC-g86NDd7krU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=S5FKpF2e0wZrCyoh2hk-nFidlGcWn9FDIUX4ARxifPP0pZdGY3EWWVl7hM4kXKCDoSfkeJpQoJiG7O1p-EZxn_mJp3xYLBJP_KOvSSzzZcXJFYVA4cW68GotIPdSZvxUl33pJuyu2DH5d3hNuUxAB31VEOsCqs7xwEe7DRdsqcqdN_pWX4DBY3-R-0uHuendPCOmnjuxTJUF7mCPUFiIkfNp1oOBru8_uG16dBrmZAVkucnmn0KhxCjtUNFqdcc9FSSkODnPoMKOjz497kJ_-MnzbnASY-qIje6Egsr_MfKwkWnrXTojvpvwf9DUiEq58n7nOARx_q8le4Wwc_IHNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=S5FKpF2e0wZrCyoh2hk-nFidlGcWn9FDIUX4ARxifPP0pZdGY3EWWVl7hM4kXKCDoSfkeJpQoJiG7O1p-EZxn_mJp3xYLBJP_KOvSSzzZcXJFYVA4cW68GotIPdSZvxUl33pJuyu2DH5d3hNuUxAB31VEOsCqs7xwEe7DRdsqcqdN_pWX4DBY3-R-0uHuendPCOmnjuxTJUF7mCPUFiIkfNp1oOBru8_uG16dBrmZAVkucnmn0KhxCjtUNFqdcc9FSSkODnPoMKOjz497kJ_-MnzbnASY-qIje6Egsr_MfKwkWnrXTojvpvwf9DUiEq58n7nOARx_q8le4Wwc_IHNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK2aQlTYUkQ_jzp1RkSUQasDL6u4pDMvuvxakwE7cyqDwKYPAbIgR013NB1epKLAUC2IsaENi2wI8cfdKVojUTNn1c-4Jyif2_lrPVLS5ZDHS-naEDVPenNHTCondPFbR-Ej9EckYh0gZHMdBpZBnJctCP-PtmMtrmq3pT_IpngrhKF78nZbAuith9xt2uUm90s3xJZsQPG_g7hZNblqH1BnRGULl_-zciYr8fM9AJZdp0NnH3Q26Fodg8s68lB1vjcyEJXdOdXWYn3ASuRPulDQv4tpvKLRRNW1QPC100btOzkxS74oB9FZNQGvbveFZ5GI7Z2FyULTqJfO_-g3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOte9Oa4iMxQ79MGqGintt9rPnh6Q47wsLREXK_wXwT-LFHIhj9AOzDZiVIltphpRoFYY6Gnt1vwf9kBMetUKy2FYnu1thQOBuGQ6qSKMMX6jotRT5m8sXpCJxFE0_3vHC1of3agoTPrB56xkMp2UJxSq45vH0LayGmL7HQGSRbELIhO4dr3nKBdcoSr02kxj1Y0kwbKzBmxvQVIgDtrpjR9FH5Uvqw9LWkqC-5M6bh1odavmOYcyFGAMnJRVYxIfVJHasmG2Aqv07eHQxHFRhPCcs_8xJ3nHZlHSdM0e2XpyD-G3WolbAS9hVmW60YMn-1NqkPkUOr3lXZ2Ibz1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIEHIdySgO72RJzFnrbD_UUe8aXo1UoTMTJ6Vnwnz_BZRdwQfWUWSpgg_1QL9stERD0MdRPPeYAx2JDg0kd4hRqKiGqhDB73ceZZDwPjZXHLIKW7Jo0ZERfwZfwMOWfVXe_9zcN-0TUCKWw_PZD5m5lVszS8AJZHiaQ3aVfM05OjATLIXYgu3OFVUpgkukdrJ2G3naC-wMFf-qKhPfUnR8LuQ0nwiTrU69TOBtwq_t5wfSh51E4QsF88cYxAU875n5kHVfIBWV7i2qdWdnFXVZzKp4LyRIuqa3zOZrHVytai18Vw8f8Jcbgc_JooIeBlgNB_LWIf7HiYvi58Oof8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=NOqShHzu74iMPGBJ79thZcfbE1vB2X_ej3iYGMljksMV_IpZOHd4qht7A0-dnUbjFzOric9uWrcWRasd_FxFoGOYrfuPmOby4tv6uBIOXZlJq63azGBKfGMG4vb7DCr4IX9Cz827rnv4dbODlkRXAJ5IMPewfI3qg2lWy1BkyPkMx9nmREn__twy5TFR3Mgo40GCdJGVuTTQTw8Z7NXB-EknzbL4y5DMJyH8EwbsZSojvDlvWiF8nMrbbtJHCyyzgjL1nosWU1xnmkU1ROW8R_P9iTXtcYx-bOgWclyYai4AGXQ-86d9BhoiFYSrpjGrtnEgta-GAZueCgKjfnQ4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=NOqShHzu74iMPGBJ79thZcfbE1vB2X_ej3iYGMljksMV_IpZOHd4qht7A0-dnUbjFzOric9uWrcWRasd_FxFoGOYrfuPmOby4tv6uBIOXZlJq63azGBKfGMG4vb7DCr4IX9Cz827rnv4dbODlkRXAJ5IMPewfI3qg2lWy1BkyPkMx9nmREn__twy5TFR3Mgo40GCdJGVuTTQTw8Z7NXB-EknzbL4y5DMJyH8EwbsZSojvDlvWiF8nMrbbtJHCyyzgjL1nosWU1xnmkU1ROW8R_P9iTXtcYx-bOgWclyYai4AGXQ-86d9BhoiFYSrpjGrtnEgta-GAZueCgKjfnQ4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLPeW2ziJY8lR4naMS2QP14B8XHhya1B8hvm63qIDES12IZlR7OL_O_d9egn-QoHiINYaGf0kaFXc4uMCw8w_kMx-5732RX0WKheZYhD1-tyXbfiCoFqB2JbQjlQoVZi7JTBXgb4oypF4d3CZ2KD30-NKtIFACypdsNZenvBmHwlIhGGncTrpncqY_kVT7t3JB8zCQHvHFsqUISc-4kETXpSe66rPhXKA5nJBesKqOwaSpY_LMU6agSHNrwfuhqxWzqn9azin3hLIqF_1liAPFk3hOOhsSJMNoqHAAnZH4PUJXkvmhhNuDnbZ_sQWDrV2EOj5d5y4YuX-WnMnhcJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=DLRFM1FHaro_di4LzcA65twXCeNbca5Px53QaJua5K6zWhS9rsMFRJ4sg6o6E_D-wMP2a3TL-skVUyciM-D1UIJH7nIHM1cL5eEXLVDUQztfshJLrhRJUFQWp5afPRBqPBJXI4MQeuc5lD5mAASK8keSWM-BMD8qkXqTpuqVMrtGP_8IjLwR-K-lC8GSjAtylyKguQEtMf8QyuWQ7-bdG64znrSOyanLZREulwzrScXP2AzYuFtlWgUsUeBwiPcb_UdCerwlQBY0vivhNXNkCxmmdRsSyk3wf4rJ_WhyK_FXLsMgIzFpuNLmmzyYr6GH_y9hUWa42BwIOXHZAJrOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=DLRFM1FHaro_di4LzcA65twXCeNbca5Px53QaJua5K6zWhS9rsMFRJ4sg6o6E_D-wMP2a3TL-skVUyciM-D1UIJH7nIHM1cL5eEXLVDUQztfshJLrhRJUFQWp5afPRBqPBJXI4MQeuc5lD5mAASK8keSWM-BMD8qkXqTpuqVMrtGP_8IjLwR-K-lC8GSjAtylyKguQEtMf8QyuWQ7-bdG64znrSOyanLZREulwzrScXP2AzYuFtlWgUsUeBwiPcb_UdCerwlQBY0vivhNXNkCxmmdRsSyk3wf4rJ_WhyK_FXLsMgIzFpuNLmmzyYr6GH_y9hUWa42BwIOXHZAJrOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=pCrQtz0z6bWFIViSiYCSRnasJoLw1bQYNiRjqujliyT6OUuVYi3Fatec6c6NW1pu9fvKiZHgxMT0ZAmW6Y11vE1HyjA4hR3hDOySIc8hfD_VABIR7x-CKZC_kwPzxovkQ6oIHYxXEGcnRTBfQEPSZrp6U74DBbCY_L0vm2DlU6Xm1Q3MMQK9oEyyy3kz2cG7wtwTnxAdqHeVKzKG4f-p4hA2S9SEsGSPOSoNHO1dblpBjc4X1DmRV0q0J0-S3pqzuBDGp-A597TiU5THn_lPNtgM5DfBqqYds_MN-SYCP5P3cQ8L2vrnetkCRrSiBM8LNYjhs40RhZP8jKhss2TA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=pCrQtz0z6bWFIViSiYCSRnasJoLw1bQYNiRjqujliyT6OUuVYi3Fatec6c6NW1pu9fvKiZHgxMT0ZAmW6Y11vE1HyjA4hR3hDOySIc8hfD_VABIR7x-CKZC_kwPzxovkQ6oIHYxXEGcnRTBfQEPSZrp6U74DBbCY_L0vm2DlU6Xm1Q3MMQK9oEyyy3kz2cG7wtwTnxAdqHeVKzKG4f-p4hA2S9SEsGSPOSoNHO1dblpBjc4X1DmRV0q0J0-S3pqzuBDGp-A597TiU5THn_lPNtgM5DfBqqYds_MN-SYCP5P3cQ8L2vrnetkCRrSiBM8LNYjhs40RhZP8jKhss2TA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=TOLrQ2YekB22RjdW-S9xtnFDgL68vefPgcuXaSWVJ_Wy5JfCOU3g9iJQpya-pDb4sapcuoneTy2Di2aL_eYyE_DnxT38R_lHTQjOUF0Pi7yDPI7Swp4S_J4n2bUewjRCZ3VIVAUXgdKnLPT1TI46t_K7spv7Va8YhT8xnJUtI5jIoGMSxs2kwwnTkDS2gBJ0iVKMLigbHNq_Pb0pFTc7MRSrwvvAgfwrpm5v4169vcZAXdtICr8MZxeQ3jLFimTpSNZua8jHCctlhLvDbfYRSRMlR7Chn1F5MPikGcw75BtS-MYY9O97X4UVQGbkYNPr_42IGJJLUnmssYSmIz3efA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=TOLrQ2YekB22RjdW-S9xtnFDgL68vefPgcuXaSWVJ_Wy5JfCOU3g9iJQpya-pDb4sapcuoneTy2Di2aL_eYyE_DnxT38R_lHTQjOUF0Pi7yDPI7Swp4S_J4n2bUewjRCZ3VIVAUXgdKnLPT1TI46t_K7spv7Va8YhT8xnJUtI5jIoGMSxs2kwwnTkDS2gBJ0iVKMLigbHNq_Pb0pFTc7MRSrwvvAgfwrpm5v4169vcZAXdtICr8MZxeQ3jLFimTpSNZua8jHCctlhLvDbfYRSRMlR7Chn1F5MPikGcw75BtS-MYY9O97X4UVQGbkYNPr_42IGJJLUnmssYSmIz3efA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=AtUaBaG9bAb34E0btgC7kMVnHSPmkA8TOEFsohImo5NAam8h2cOPEBD-OZwoKvei4EpdUoInI3wHnulshTjroEXI8WgJRXMsIegYipbevjPJpGK1rOltcrE0L_348dzNgx7PTEPByHfbnQ3H4V1yA4kf4AeOqukmP3eHK6DVaFaFL0W6SeCcs8C2qPOGhL1LfeuYGY27JlSnKp-sC9LC8yuS0m85LrOEWPbSCedeOtBytlQqhAmQsPCmuJgAYqgjXj6gANcXtehJCm4fIe14p9YyVSiSYFWA2dhlOwyN_gU7xh5CSC2-7PpnLKadTZFBbTttMEYW7eCOMYQUmkLkHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=AtUaBaG9bAb34E0btgC7kMVnHSPmkA8TOEFsohImo5NAam8h2cOPEBD-OZwoKvei4EpdUoInI3wHnulshTjroEXI8WgJRXMsIegYipbevjPJpGK1rOltcrE0L_348dzNgx7PTEPByHfbnQ3H4V1yA4kf4AeOqukmP3eHK6DVaFaFL0W6SeCcs8C2qPOGhL1LfeuYGY27JlSnKp-sC9LC8yuS0m85LrOEWPbSCedeOtBytlQqhAmQsPCmuJgAYqgjXj6gANcXtehJCm4fIe14p9YyVSiSYFWA2dhlOwyN_gU7xh5CSC2-7PpnLKadTZFBbTttMEYW7eCOMYQUmkLkHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=aHkZAkafZdE9eWIWgyZsxbkv9T937CHHkECtZyEtXc5wLBXNuT9GOdyEoYCNq4nOPDqpsjOIVEql03iyZUPyxb4-AuX-g7h-L31QheopxIGlZv1VenaksH8FNS_5nk1TXc0uGX8hmcBzh843ufDVdTEzYWIbafOKkzC44J7OfF2Yim09L6-xo7JGsYrReE72qO1YE2QazSloWHe070HjNUubGfnVxHo8u6W799DMVpZU_j6yN7pWSjUgG_g0A_uQa4WSitLYc6uxC_Z7G7WJxyRyMUO9DAN-pE48j_IuIn1yumrLFRAgdGc9D2H4nngrL6oyQtRKHa_42e1L1vhiNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=aHkZAkafZdE9eWIWgyZsxbkv9T937CHHkECtZyEtXc5wLBXNuT9GOdyEoYCNq4nOPDqpsjOIVEql03iyZUPyxb4-AuX-g7h-L31QheopxIGlZv1VenaksH8FNS_5nk1TXc0uGX8hmcBzh843ufDVdTEzYWIbafOKkzC44J7OfF2Yim09L6-xo7JGsYrReE72qO1YE2QazSloWHe070HjNUubGfnVxHo8u6W799DMVpZU_j6yN7pWSjUgG_g0A_uQa4WSitLYc6uxC_Z7G7WJxyRyMUO9DAN-pE48j_IuIn1yumrLFRAgdGc9D2H4nngrL6oyQtRKHa_42e1L1vhiNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyPcs-JG5YKOS06KI7Lxgtoxeyu7W__-HFRsbPGnZc_mMYwLx6C3IglejRrMre9fsAW1mHk_IGXJb7X3kMxv_U7ZZ3FRVExIuTnk9HNvsuLoqN091QiILKaSvdnMhhibEh3hHAK6YJL9O7IaionmGeCq4VKkRBtjUaKDAShSKqPN3q0Ddtqiv_nQ7D2kKITZYYvfKV43eL0amOYa5XoqyynoYCsklUDgxZ5NcUshvV7tbXEVAvrCP8T9B4jbqqsCw2kxCb-7XMqD0fiP32LbQfpk1ne48RlocFyYN57aCg4C4ZnCd1FZPzAYMOS9-g-O5YsNuL1rOeXhvN_W0h6xIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYy8fP99gypJzkFjr-fCDwjxUNevhMTR34OzR5eXtvMncsHxn5tqUPOmzqWkRUTntWCpSGwXCewdFvQH9Q-9hXHVr-X46PW_oMMxqqJhdJwOFNZmyny1yPFeVvWisx4VHBj1U3Zl5sYneVx28svb6_fR7KXZJT31cPDEsj5s7yp6yfGqeF_S7qSmK523oCyp62id91iuAr7ioh8uCqcYtoFxs7XJT8vR3lxPbi1wKKbGo8TuHB0bL2uwTgLRhXtM4_bTGPvMQx_aT4JE9qfeY7euMAu5VH2FlqqzkZJFVxyxB74DMf-9oiv9Gh0eI2cA418DyNoA4-8gjnCJtMNOwBv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYy8fP99gypJzkFjr-fCDwjxUNevhMTR34OzR5eXtvMncsHxn5tqUPOmzqWkRUTntWCpSGwXCewdFvQH9Q-9hXHVr-X46PW_oMMxqqJhdJwOFNZmyny1yPFeVvWisx4VHBj1U3Zl5sYneVx28svb6_fR7KXZJT31cPDEsj5s7yp6yfGqeF_S7qSmK523oCyp62id91iuAr7ioh8uCqcYtoFxs7XJT8vR3lxPbi1wKKbGo8TuHB0bL2uwTgLRhXtM4_bTGPvMQx_aT4JE9qfeY7euMAu5VH2FlqqzkZJFVxyxB74DMf-9oiv9Gh0eI2cA418DyNoA4-8gjnCJtMNOwBv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=caWslOTo4v1cvC1xmp79yfMZc5ONF_Ba4DNlmSfKBJm1DZxUU2rTWd-LgtD-B4FdxXBNznTS8z8VxOj-PO6YImJuE9gQ8B1kDzH8R4w0_JB8KGO03SThUDSFwcTKlzKyesss9NErw6CkR-Byeu7GT_Ynjut4oRODGfiirUTmuzpGdAnNUi0WEns94tNhD7iU1d01s9KVsYNj_cfAiOl-wgXXwiu1Fn0hLsCVWvGh49qdOBC0yYjIAKodrciiu2GWGJcH6WRpRWs6S3rWrfdxlcnyiPQoDuehA9xK_MJGLAKxMPuyExdgWSsIse-SWCFtYYmFyKpt_LXd0BF1yfwzow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=caWslOTo4v1cvC1xmp79yfMZc5ONF_Ba4DNlmSfKBJm1DZxUU2rTWd-LgtD-B4FdxXBNznTS8z8VxOj-PO6YImJuE9gQ8B1kDzH8R4w0_JB8KGO03SThUDSFwcTKlzKyesss9NErw6CkR-Byeu7GT_Ynjut4oRODGfiirUTmuzpGdAnNUi0WEns94tNhD7iU1d01s9KVsYNj_cfAiOl-wgXXwiu1Fn0hLsCVWvGh49qdOBC0yYjIAKodrciiu2GWGJcH6WRpRWs6S3rWrfdxlcnyiPQoDuehA9xK_MJGLAKxMPuyExdgWSsIse-SWCFtYYmFyKpt_LXd0BF1yfwzow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=bOrIMTAG8ah98L2mz89ALQMupycleMgecv-qYLTumvPWlRBtYonWnmy8-c970snroq13nvkghsoLd_rZ6fzNsUT32jcH632PoT2c6rkPK22xadtW10UC90_1LmwJm1g4Zk0Xn83UfkVY4WX1RUNreHKeWXHCu6dmkhTeNPbIXH5P4c6IcchktOKOmE3aNULEuRWYr5EZkDh0eDEXgPHmV8Ce_Mdxhoyb8W0iybmvDXh4tIQLyBGurxHen80f8pQArV4i3nixnmiHGzsm9CvYqrXrltGDlV4l04yS_tQKafgwvKd5QWe3phCo5YPRXP39hAx0LCpm6jbMRDvutb_Myy-gI45Q9PsEvoMybYGDcp4o2XfoKBIjK1tC8OU_gF-KijZF8uB6_8ITRs8qgO__f186s5XhEXa1Cr17UlkksNu8tWZjL1FTtvXGu0vv51rVm-DLMOOpqn_brjktBNs-87MZkmZNoI4DEpeS4LKly6_YSb6CBZkkxHusctIpl9eNevysyEAy6QP7qabC2cGbvix47goMG9g5bWgrV7TtCKwishnQj3G3p1n5C-YXj6mBPl6iHqd6zaTIxAGkJXKG8lJIjy7Ycima57ZlW_hehfliAtUD6wbpj3XL5kHRlxWVcYSgfCIlQBCajS1pg5GblP3jn2SD3GwB15d1ps05Sls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=bOrIMTAG8ah98L2mz89ALQMupycleMgecv-qYLTumvPWlRBtYonWnmy8-c970snroq13nvkghsoLd_rZ6fzNsUT32jcH632PoT2c6rkPK22xadtW10UC90_1LmwJm1g4Zk0Xn83UfkVY4WX1RUNreHKeWXHCu6dmkhTeNPbIXH5P4c6IcchktOKOmE3aNULEuRWYr5EZkDh0eDEXgPHmV8Ce_Mdxhoyb8W0iybmvDXh4tIQLyBGurxHen80f8pQArV4i3nixnmiHGzsm9CvYqrXrltGDlV4l04yS_tQKafgwvKd5QWe3phCo5YPRXP39hAx0LCpm6jbMRDvutb_Myy-gI45Q9PsEvoMybYGDcp4o2XfoKBIjK1tC8OU_gF-KijZF8uB6_8ITRs8qgO__f186s5XhEXa1Cr17UlkksNu8tWZjL1FTtvXGu0vv51rVm-DLMOOpqn_brjktBNs-87MZkmZNoI4DEpeS4LKly6_YSb6CBZkkxHusctIpl9eNevysyEAy6QP7qabC2cGbvix47goMG9g5bWgrV7TtCKwishnQj3G3p1n5C-YXj6mBPl6iHqd6zaTIxAGkJXKG8lJIjy7Ycima57ZlW_hehfliAtUD6wbpj3XL5kHRlxWVcYSgfCIlQBCajS1pg5GblP3jn2SD3GwB15d1ps05Sls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=P9ASF7yhAZSs1XjQa1c3R7pQ2UR9Ivu-6PPE6tVaO9mZIsGr8e8W7hzSHRQUgR9kKOe8pLNaqmsGn-eoxG2o4ht1-_2o-bSE6ez568aIRraGFeGeYd8jahrBdoh4hCe2YcYNF6GaWXUtJm7K-IIC_bIjDipLisEOOrZEVGwV4Xj65JG2q8ujBvNSQyR9-9FNTknih275gx8I5Wtn0P5bIdMRxyGZwqfGEzfAb4f_5bq0Obp-Me3QIXyMKG9sAeT3Lrz-EZLk2RaKWIXP0D26Cz0REV_fjycOOaIGzjB99tny8n97xWgZBNIZwEVuurceqUBinDZAWEmzBnrCIb9s_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=P9ASF7yhAZSs1XjQa1c3R7pQ2UR9Ivu-6PPE6tVaO9mZIsGr8e8W7hzSHRQUgR9kKOe8pLNaqmsGn-eoxG2o4ht1-_2o-bSE6ez568aIRraGFeGeYd8jahrBdoh4hCe2YcYNF6GaWXUtJm7K-IIC_bIjDipLisEOOrZEVGwV4Xj65JG2q8ujBvNSQyR9-9FNTknih275gx8I5Wtn0P5bIdMRxyGZwqfGEzfAb4f_5bq0Obp-Me3QIXyMKG9sAeT3Lrz-EZLk2RaKWIXP0D26Cz0REV_fjycOOaIGzjB99tny8n97xWgZBNIZwEVuurceqUBinDZAWEmzBnrCIb9s_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=dA4TWtEdBxHwaS-M5NZxq9aDgcKHxhUxPvTHkVbNCDuJQhaQbPr8ZzbkbBtIVno7b8OE56jrvUjHGrnYulZqt4IIVNMK0V39ypUcnl0Sq7SwIRS8PIw-KDNkow-foyL82qG37tbS5E4pFEL5Bdoyys74CA92yGNqBm0Snm6TSy8-lZMALquyhSZAOps_RwhC6mlB5eBzSm2wZSyFt9ZzNnjFNU0MT0Ou5jMmmtdDa9KYBiILbxI9XTzx2Ua-QmDpaKzFc5jvt7ZXVhw9eimtT2kDIlO5UII0QqbDbco7I5GI9mDUfi822vjKNs157jOR8VpnPHLlifv-2n-5TP3-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=dA4TWtEdBxHwaS-M5NZxq9aDgcKHxhUxPvTHkVbNCDuJQhaQbPr8ZzbkbBtIVno7b8OE56jrvUjHGrnYulZqt4IIVNMK0V39ypUcnl0Sq7SwIRS8PIw-KDNkow-foyL82qG37tbS5E4pFEL5Bdoyys74CA92yGNqBm0Snm6TSy8-lZMALquyhSZAOps_RwhC6mlB5eBzSm2wZSyFt9ZzNnjFNU0MT0Ou5jMmmtdDa9KYBiILbxI9XTzx2Ua-QmDpaKzFc5jvt7ZXVhw9eimtT2kDIlO5UII0QqbDbco7I5GI9mDUfi822vjKNs157jOR8VpnPHLlifv-2n-5TP3-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=umF3B384v5YAKuDpcf7SkTjs6vcpI_rL6Tx-NC4uy6BzBGEIhFIN_gT0UY7ILsrcLJtZEFA5t8tUv1UN-JogwdQHbbA6S11TlJJo7wzpwTMQrzv1tu93EwwRbVnaIcCt4YkS8B4W4CALBOZbVmkRlUbine4l2gFvQQviVqJqroRQS9wzJ5oOtw3xBLB_EePP4WoW8cdxtcnjfnY-vczfRykM-Ew-RSgbWd-zIUJEy9HQ4XeZx-XPmD3X4l9ChfVwdc5M4QF9y3-EakRXKta-mfMX4eybX0bGVzIzKgjKnXw99UfBBEUp7xSFkDD68WqceAVd9gDKtTV7Nnk824dWPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=umF3B384v5YAKuDpcf7SkTjs6vcpI_rL6Tx-NC4uy6BzBGEIhFIN_gT0UY7ILsrcLJtZEFA5t8tUv1UN-JogwdQHbbA6S11TlJJo7wzpwTMQrzv1tu93EwwRbVnaIcCt4YkS8B4W4CALBOZbVmkRlUbine4l2gFvQQviVqJqroRQS9wzJ5oOtw3xBLB_EePP4WoW8cdxtcnjfnY-vczfRykM-Ew-RSgbWd-zIUJEy9HQ4XeZx-XPmD3X4l9ChfVwdc5M4QF9y3-EakRXKta-mfMX4eybX0bGVzIzKgjKnXw99UfBBEUp7xSFkDD68WqceAVd9gDKtTV7Nnk824dWPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnXd6SZCLxmd2Lu9MiE9xsemqGa4e8le1NiRMwEiDPZE6Dag0h4d4atqCGjijqSVEfedudeCa6LsHv1-A3xyzfBA-_1EkhnLdpUa1enDGmrL2ENenDBgp5N5Kxz3JOi5fBKf5r4OBzm9wjbdNn2oENZnG7pWsyqdo4GNuEPb0vKH1YUD8WZKRplsrquuaSX-MDjtmqOQ49RupSTUkbUihr3P3lasiFxpd7T4ot-0j1COekBn6s9xeyX1DbnTmCUfburATrwF_0UK0AkqRyeubrvHexRASF6uRwbS8nQWDbLuWXiTHB7athbXj4sXo2o3xARJR6ZkeA1d3JzquhxlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHwB7H2fy0LlOMGxSJeNnC3X8zDQv2pItZhmvM1uTtD3-oov72vLfidbXphKhNexr4Epgg9FSfJuJ2wCX2g5SqhBJtHyM6JxgyctUVHZYp9LeUm3VnDlutFa01Ho0MrRYF177A5o-xiJ6ctqnnok83VwLK8Q6sujqDTDFJutrTmJ2qXvP5DofqWKHPrHM9uAwd8VSBg7pBXrBuiAhl6ppj-jgWvVWSOJuMchSVekAjTZyDOuI1bBlUqpHnaNAmoPyHaXqiK8LVMRy6wc1or8crZ3ZhEs6BXGb0pnGfTd_m5dA0hAScRxX0_5MAbG1TisCvaioNjv25A61-q5hzCa1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxqllUa5UuIUYq_jrN1pwEmYGGWWCj0_sUye3LR45D69I7hcynlsrHZUjsjfFdRUFQ3zYcYqDCLkBdZCcu8fcpZGKbcnMMD19ARLGPHfoeeJxcyX-vpq7p9n1FHbdhRagSjVfh8jdkgVKn6Eh9_luSa8mT7yCkBzMIg8T7sAGMEeArPKtThU_gYdh7qDPJa6NuX9y6QVcF3XjwMf_-vilMaBUgC5VAL9P9WonhtagzcHtykBFTpfJyV3RqUF5gBzgp9vISLtrU5OlujelOG6_sAwWBTx78__ZkHqKGlzCxsKIReVe2ibcqeLurIb82-kGy1KSYherWbBlxt8RL9LYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SK6ex7YHdj0A2wfePfKyahTUmpsW9XO6yNxhFzwePKRwRld4k7hB7jk8PMXEHndT9s0mcj0BU8eq3yZJF4yyH276At7XKPNl04UlKYtSVdJI9jK5H7Xfhyn_J9xZnoHPYKCJXBPPY2fjrDPmClMmWsEQL7dLEPgdR9OcLD-tV3CXATnVIJK3lQZMwgtsh__vY01EO2K6N2Mm9w9AbgjwV1Eug4FaazCdYmTYXVF1TscOAcC-k_beF39WtPy4MjRdxGW1scSyNt7dsz3JlHqRCDpRg962jbprRsQex7zOLRu0Zfs7WjIcefXd65kC5e54cSF2GA3EbN4DmNb9nZeehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5MOqyCWzvUMUz7gAEKcY5Qh2qRbCuGbnyF_uxjTGftZcwvFTsxQunZx7QEHKgwilASPDwB1953M2bPnmzpkISFHXzf9El5q4RWF9k9483h4OS0hV460XNswdiu-DMhVRprkd6mm9xis8zFZApwHQMrNv_6cV2wqbxjX8lKTJHmBi1-4fhzaGH3a1FHBt0rasdhm_8u7YSe7h5dpLLKK8SduLIwg05zy_T1pdZH0stpmU3YHPZkK8ajN01PV5zVWu-94ahhM3ogQHGkPWPzWFMSl1O2iX7YnK31pfZ9nc5j46UxwuY9W2vtw4He2r1hXlOzCnaEgJXdyvWP81wLc1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=ELdwF-ITOTaC33G3cgcwPY8iQPowO8LTdlsHWSdTvrgYUXJM3zpYhOfN5OTdwV6grjEU3fzLjrT1utL7dGaalSdxhJhn6G7nfH9LGK9giC5Qd6fh4hcUUF_WJZqHHWpJzCp6nxfguxf2rApA1byQuDf7qUFUXaV6ajCJYoSBkawKMDCB3jJANciIw1xwsMEHUNB-B6igGiscfcQWV_O1tdMqWa1sj0ZF0gPkwJ-Xv_0Zvjs1s17g_ImCPxL08_3MTKOlLCj1dT4OkD48o2L69L_Kl3ETiYOlUN3c5jfN7XuvCPFoYyddGrLtEy8RpiqGWafwpXMizuyoZN7fPoUlCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=ELdwF-ITOTaC33G3cgcwPY8iQPowO8LTdlsHWSdTvrgYUXJM3zpYhOfN5OTdwV6grjEU3fzLjrT1utL7dGaalSdxhJhn6G7nfH9LGK9giC5Qd6fh4hcUUF_WJZqHHWpJzCp6nxfguxf2rApA1byQuDf7qUFUXaV6ajCJYoSBkawKMDCB3jJANciIw1xwsMEHUNB-B6igGiscfcQWV_O1tdMqWa1sj0ZF0gPkwJ-Xv_0Zvjs1s17g_ImCPxL08_3MTKOlLCj1dT4OkD48o2L69L_Kl3ETiYOlUN3c5jfN7XuvCPFoYyddGrLtEy8RpiqGWafwpXMizuyoZN7fPoUlCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OcxQZTbTjHuTYQla-qkFaWA0tm2SVuNeELlqxhpJDKhssROXr2zxdkJGSP-Wsb4ynBr09Evl0-_2iY4cpmOLlNSLVkLcTPbDYFrpTZeHb82kUWlHDasyfFPE-V90y--19TWQVMjcmZHEotKfD5eD6eyGs2n7tdLE7N6FafpYTiNh3SW4KlZfQO1Bi8cj_BeA0AjoktRo9ROIcH8cmXl4rJ_7sGOrmuVYPdGbiB8dnW6H94urBnmT0d3QNXdXP32PZFiiCK-A49fBeIMfQFZIORbX17ix9iLxQAs0OrPWa8mMECyXFH3Uzn4P9BI7qkyqBpEApgco6fW-5WtfoF9JeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=OcxQZTbTjHuTYQla-qkFaWA0tm2SVuNeELlqxhpJDKhssROXr2zxdkJGSP-Wsb4ynBr09Evl0-_2iY4cpmOLlNSLVkLcTPbDYFrpTZeHb82kUWlHDasyfFPE-V90y--19TWQVMjcmZHEotKfD5eD6eyGs2n7tdLE7N6FafpYTiNh3SW4KlZfQO1Bi8cj_BeA0AjoktRo9ROIcH8cmXl4rJ_7sGOrmuVYPdGbiB8dnW6H94urBnmT0d3QNXdXP32PZFiiCK-A49fBeIMfQFZIORbX17ix9iLxQAs0OrPWa8mMECyXFH3Uzn4P9BI7qkyqBpEApgco6fW-5WtfoF9JeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJRyewRvaKblRZhnopiwZvAhgZEcnuqAjA9vzB_x5NCFUYam5tNvsYSEwpvu6QP_5bIgItqIXjh471DfMS_g0g__qZHwVN7yyhjbEnRhaaB4Km6pez1Ir0ds4ry0uWyM2Tj_Nc2_eYI0ChwqRQqTKkHjpkQ9d4Qi7GZOiZIKFc0kIYaMfeBm0vDTfETY_IimbJlY_c6wOqvM9ljdfCjz6TH2ujIg_SUUJVWjYUTyf-tGrA3hngGecaHkJRNONuhxgTeD-qmDKE3g_zUXmPU2IAdUCzNWSWjkBkW-Xz9X7EzOIyxPTn5SmJsYY8EPAtyvLZiayJHaam5UM8pjfD6A5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK_nUGyCVHAk3yypBvbRAVq9kjUsjCW0fYe2jfuzlGYPfEzCUUXcUjsb7KcZR_3xU-STb5N9P-RyCnOCw8DFCqQQOJV-OT-MDVhD3YCbR7w4nYHaHnyk6pPK34P-c0dWr92hpoenTDacTU4j299bRg9IOi-DzGY0izEC-cEfUt-pDQ8yoyYDu8ykoGYJMiNZPN7_P5QE0f8_1EOqWqlqju_H_scIH-FvlBVXJ1TmfymrVzyf9hjywvThU2Ky0kIW_nnBO2feYoLfFI5hAUp3eLlqMtzf05zVl-K6TTkGVWrEvJ_Q5fvozO7X6aaTMmvJmOhq4O4AjSvva9rdrwn86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=stJ2xrRr8xCDxgC4bbom_v-xNa3-OcpdF4K9Fc2uPEp8uBZEGePySc-olGaq7qygXD1JlsImuVaDx5D0lwfTAnhp_owTCgafqTqy3OTQpg9q8hEAP4bqzUCMkvtDtZxcnpdnNF_rlilDcnS8V-tUwv7zBohpgN3EbEyDNDoIyxZNFPRvz829pSQ-qypTfDtMI5kcAdMS95YsUG4AMyVAPXxT1GaUdEZ8Vb-eJ4ONHV5UpKuPnFosGo5zVnpv56-BtKDODi74WzHVEpie6MS0X7s6HB4EgsY6jHw_pwcc9EQ36qW-Ceib_aK8xbWOav4VKVMxjDCCasSMf4gpho_zqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=stJ2xrRr8xCDxgC4bbom_v-xNa3-OcpdF4K9Fc2uPEp8uBZEGePySc-olGaq7qygXD1JlsImuVaDx5D0lwfTAnhp_owTCgafqTqy3OTQpg9q8hEAP4bqzUCMkvtDtZxcnpdnNF_rlilDcnS8V-tUwv7zBohpgN3EbEyDNDoIyxZNFPRvz829pSQ-qypTfDtMI5kcAdMS95YsUG4AMyVAPXxT1GaUdEZ8Vb-eJ4ONHV5UpKuPnFosGo5zVnpv56-BtKDODi74WzHVEpie6MS0X7s6HB4EgsY6jHw_pwcc9EQ36qW-Ceib_aK8xbWOav4VKVMxjDCCasSMf4gpho_zqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=gK9HU6TShjp6msonY5ETrf4sgXfSB2kzYZX65m_mX-XlNKkJIdwLeNeGbhzqp_VLSRhe0b6D_n9QpLw9-QH-fom1grYnebZWLRsRmbSwtws71JAX3J19Rjb1HBtAKlJjxKoPIFwJG_S-FytoQZsP0kTVBTDZl948VUvKahN8rXX0_UvLvayVgToTcs9eWHRSvAPNAtl3MLOSqLTwEL0SXoEGm39WchhmHJBddQEvXyvij0t8fRo5C7aORcJIPw3prMHxU_KIJl-R_0Bz4XnXAUi6C80J1UUkxYQxKbdz-fyLrgvVc7gcdWnC1tOrKGoQgM6hezwk7LmeO48ITGzHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=gK9HU6TShjp6msonY5ETrf4sgXfSB2kzYZX65m_mX-XlNKkJIdwLeNeGbhzqp_VLSRhe0b6D_n9QpLw9-QH-fom1grYnebZWLRsRmbSwtws71JAX3J19Rjb1HBtAKlJjxKoPIFwJG_S-FytoQZsP0kTVBTDZl948VUvKahN8rXX0_UvLvayVgToTcs9eWHRSvAPNAtl3MLOSqLTwEL0SXoEGm39WchhmHJBddQEvXyvij0t8fRo5C7aORcJIPw3prMHxU_KIJl-R_0Bz4XnXAUi6C80J1UUkxYQxKbdz-fyLrgvVc7gcdWnC1tOrKGoQgM6hezwk7LmeO48ITGzHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=Ok-zz4a1QizC5hQgUoZbP7rojclk-xN7HVQzYHqvJ7AbHq7Mykjq8MMXo4_mC2V9bVn9sofzppm1Blfo-30AZse2GRwjPAvd8ZsTssEACL_bU-ww7Do0Hzz-EBSTpv4Ju_XiOkEoQGJE2GFwtIbg4cSFM6ZK_04bdACGrLhdNQEl2jEy8ElJxS3YZG8_OddeDWVcGspIXO_SpX-sXpzShjZBt6jflE3OtXRHn_KwMtt11k-vmtr70SKvYzM-eSZ0Vl07IbFPP7FPpK6QW_9KkI81KU3zMg8B5y3chhXMVSS5KJmnJi0Iyj1Q_uJlXxuBcRkJzCdwZXgCiDg7ZQSqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=Ok-zz4a1QizC5hQgUoZbP7rojclk-xN7HVQzYHqvJ7AbHq7Mykjq8MMXo4_mC2V9bVn9sofzppm1Blfo-30AZse2GRwjPAvd8ZsTssEACL_bU-ww7Do0Hzz-EBSTpv4Ju_XiOkEoQGJE2GFwtIbg4cSFM6ZK_04bdACGrLhdNQEl2jEy8ElJxS3YZG8_OddeDWVcGspIXO_SpX-sXpzShjZBt6jflE3OtXRHn_KwMtt11k-vmtr70SKvYzM-eSZ0Vl07IbFPP7FPpK6QW_9KkI81KU3zMg8B5y3chhXMVSS5KJmnJi0Iyj1Q_uJlXxuBcRkJzCdwZXgCiDg7ZQSqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=Suvx4f3mjbMtA6fzMr72dGzQ2hNd5f64oEp7mWr5D1v94_Fz-2vpxlPIrPZ9mJRUr9ZKvBHWvNWNWdw54_IJGQY863RynnOsFiyI6425gEnad9ckW44sxKR1Cn01bCkibDYL0sA64FKwdfDie7tKSRSRFv5qZerla-Pdpzx3rI19b6pYSfNXDW0eFTuvHLdFmZ9cha9nQ-ar2Ded2DxOq83WeaQWbwgWKRm3WIu7ilr1iRKKwYomxqOE6Bqz14mu2ZJPYuvCKu_VbJSStpttncBXyQqOzBhVKFS3F1wcGmY1naP9goc4YR8BoEfmQ8rJKKuHOXGDG3UxBRLj-7ecZLuB_R81vsal-_WUW-wM0KKzdyp95ilk242yUYYn5lrTYoXuLS48GleCZYhIY1LQPEuKDDstWuk6Kb1rfw2Pi-FJ4UOMXHbj-UTKzV_r4JsQizjbYbwtucVVwQ-tPBlHWCJTFtdBOsKPWsW4kX495zLRiEGAKkAJX8J6QqcuX-XsrbTBCIW0JvDdN6SSbWS_iv64jncJ7Do-g9u6FiEdfKVx5brye-yFFGe_2o842Dap7g9ILKBHiLbw2Gu5d2hahKwXTDmsLpVi2linHVXsEN6AvoE0-p44DeDDXJUpFQuU5Pd5oankGPrl6nhAB20fDyWFmnEY1l9uw4DkBzAcAAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=Suvx4f3mjbMtA6fzMr72dGzQ2hNd5f64oEp7mWr5D1v94_Fz-2vpxlPIrPZ9mJRUr9ZKvBHWvNWNWdw54_IJGQY863RynnOsFiyI6425gEnad9ckW44sxKR1Cn01bCkibDYL0sA64FKwdfDie7tKSRSRFv5qZerla-Pdpzx3rI19b6pYSfNXDW0eFTuvHLdFmZ9cha9nQ-ar2Ded2DxOq83WeaQWbwgWKRm3WIu7ilr1iRKKwYomxqOE6Bqz14mu2ZJPYuvCKu_VbJSStpttncBXyQqOzBhVKFS3F1wcGmY1naP9goc4YR8BoEfmQ8rJKKuHOXGDG3UxBRLj-7ecZLuB_R81vsal-_WUW-wM0KKzdyp95ilk242yUYYn5lrTYoXuLS48GleCZYhIY1LQPEuKDDstWuk6Kb1rfw2Pi-FJ4UOMXHbj-UTKzV_r4JsQizjbYbwtucVVwQ-tPBlHWCJTFtdBOsKPWsW4kX495zLRiEGAKkAJX8J6QqcuX-XsrbTBCIW0JvDdN6SSbWS_iv64jncJ7Do-g9u6FiEdfKVx5brye-yFFGe_2o842Dap7g9ILKBHiLbw2Gu5d2hahKwXTDmsLpVi2linHVXsEN6AvoE0-p44DeDDXJUpFQuU5Pd5oankGPrl6nhAB20fDyWFmnEY1l9uw4DkBzAcAAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=uEdoLXQR-SdbwuIrEHE6_g6YFA2wqdoCMaJ8OrFXoAX4Qqc2zLK08Ljzg9muiENRK2zpwWKt2wZ-JEYX2REgouc_xAttXuyAjVwx_2akjW7RSH5tIWUZSke1pAHCbobWTYyzbuXomlH2DvHmmOcruC5lR07VBLyiApsigkpbV92crw0aYYiPNbY8U_4FIAJgk9Ee5jMZutLk_uacLE_ePMJXfSiuCaQtTyl5YccLRqVMAwSWUiW7XUewIQHfO_4my8syBdt3zItwDU9xgQvERovGsLKsKbadb92wpI8qH94ipeWMsSXcXlO0EJB7WRksWj0BFNIXCrwEfSSE1i7ZlDJ2IqEziXOxFOoPZxEfIuoBlKmLB9gQ_OilCCtB9sCnxWFHYgZ4FWHYRjOx53FbbMkAnrcwKYHMt6bJQK6q0ud0NgNjR3Kf6rx3o55IIdQ35jpfcu-p1-sV-iocAcCINJbmHd3Ptge_Wb_ghiB6fu3Nz047h_w6hnpzXPnphrMXdOHNTHzjUf4ll6F7ElF7Z5U1N6rOEQCx4a9Z9R4gV9fQyTzlQDeVaMKO57Y2locsFWwhIVRYB6AIzdziBiFHWwtG-aEgLeoQzIaQIMiG_4b0LmZ37Rrhg8aAFG1KFXAMbIPevq8KK4xT3lYkbIPvukKbugx0p7bsDMbRcy5-DG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=uEdoLXQR-SdbwuIrEHE6_g6YFA2wqdoCMaJ8OrFXoAX4Qqc2zLK08Ljzg9muiENRK2zpwWKt2wZ-JEYX2REgouc_xAttXuyAjVwx_2akjW7RSH5tIWUZSke1pAHCbobWTYyzbuXomlH2DvHmmOcruC5lR07VBLyiApsigkpbV92crw0aYYiPNbY8U_4FIAJgk9Ee5jMZutLk_uacLE_ePMJXfSiuCaQtTyl5YccLRqVMAwSWUiW7XUewIQHfO_4my8syBdt3zItwDU9xgQvERovGsLKsKbadb92wpI8qH94ipeWMsSXcXlO0EJB7WRksWj0BFNIXCrwEfSSE1i7ZlDJ2IqEziXOxFOoPZxEfIuoBlKmLB9gQ_OilCCtB9sCnxWFHYgZ4FWHYRjOx53FbbMkAnrcwKYHMt6bJQK6q0ud0NgNjR3Kf6rx3o55IIdQ35jpfcu-p1-sV-iocAcCINJbmHd3Ptge_Wb_ghiB6fu3Nz047h_w6hnpzXPnphrMXdOHNTHzjUf4ll6F7ElF7Z5U1N6rOEQCx4a9Z9R4gV9fQyTzlQDeVaMKO57Y2locsFWwhIVRYB6AIzdziBiFHWwtG-aEgLeoQzIaQIMiG_4b0LmZ37Rrhg8aAFG1KFXAMbIPevq8KK4xT3lYkbIPvukKbugx0p7bsDMbRcy5-DG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=j0PINYuA-UmBSoqP69JY-DKQMBQKUC1JbBKLhFSYVBWahmxExEOYcS-1VQ8RPAPBIeUIhVkRHakHF6zJP0r8xhZdmxzldLVzk5aIhljcFJ4JtzR_AePvqHEnhIhAJz4KWGTHz_ycnEht6Z6RP_cUdDYH4m3GwjX3D8hYIdVFD3zq_edsgZBTJlgawe39qK4GMBj9cCHggezwJKEpl8grPY1430V4U0Pfy-5W1Djpz5S07UDAIXgW8LQ4zxvArZmlM5mWtbmpCKRZTHm6q7z5Pm_ArATav5to14JBPxr-pdxFF6D67mpyeJyat2yKsnTgPbPRLQUBo6E-rGoVeRzwaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=j0PINYuA-UmBSoqP69JY-DKQMBQKUC1JbBKLhFSYVBWahmxExEOYcS-1VQ8RPAPBIeUIhVkRHakHF6zJP0r8xhZdmxzldLVzk5aIhljcFJ4JtzR_AePvqHEnhIhAJz4KWGTHz_ycnEht6Z6RP_cUdDYH4m3GwjX3D8hYIdVFD3zq_edsgZBTJlgawe39qK4GMBj9cCHggezwJKEpl8grPY1430V4U0Pfy-5W1Djpz5S07UDAIXgW8LQ4zxvArZmlM5mWtbmpCKRZTHm6q7z5Pm_ArATav5to14JBPxr-pdxFF6D67mpyeJyat2yKsnTgPbPRLQUBo6E-rGoVeRzwaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0UZeGYMYtdOhxEWXgP8xK57XKnwwtMzEPXufV_Xpr-hLSf0z_cUVkH5KuVrGsmzKPXzhifaP098X6Q9BNa7gZRIS81kHIwrjOK9NCJfWCdnE798t3diQclvUqHCJhHAFRpFGjIJNY6wajZAKstB2doIZ-wTNB7_-eZGjeF6Ko8_c8MUSgF5XKou_X1QV1CNL_DmiYzayVhgYrZrC2R10xT6SDNS6yV_mt8UXIhfWT72zWPLYLCTmBrpJhpX2Fx3zglD6R7tdEnzUq_EMPIEaP-w_O6Ujf2qJ9INKQcOZT9M00BnLjjHHmguk0Pa36IuVs-jDEFS7rlxTMQ6mkKbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-iXYKTookm-YheXcKqPGwlN55xzr0UPIoDkdTiLfHhqgkGI-vMEZxcnLbxdmlC_o82vKCCfZipt-syfRaj-7IwzAWQtC3N9ezhNapjyhvcIvS92JbPHxzltEgv2mRIqNOdpS3bMQefyHCO1zqFB8v1BDhRaTqon7PFTfzsWdBf0bgGG9hV4sOUBM7I1Lmp5POO4XUtGKkoAuGOWTUkDUUMs3-YXDPoqm624NNk-SoHTd75jcNdh2dPqxDCdrIXhSFXnKwsSNOQz17mYohl6bPhS9F3yONSA8WmaGH6V9e1Otaadfn9Mgf0jOUXaer77AdOoGtVbUhdx-tIhVXqfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=oeiptnIp9oQ6r3o_Xsf7XE0Q0VUYyASedE5Qt3_4kkmiRTYO4JXUj44t6p5Nca3NHi0tNmsDbXUld4ndpfCpxyUzCEO3cAwn9NJdqDnXIWMfzmXZZNZb8rYl3WlPK9W29oRJoUTPAlqktVCDMQaksumIBN9hKh9DsTkb38sm_-nsh9dm25FFt6zlVMGSs_HAzehoWcshDO9T2h5I38D8-ItzwIdqHVf9FZT-4FyLefWVvDP2S-odxrC4LDcyx2RHlRvuLCVH7F_-9WkemMwo8dFEkRqwv9g_7t-a59cEwG1pgF70wmA_pLK53Dx8j5sCXN4W4d-oNQwXkD6_3xvCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=oeiptnIp9oQ6r3o_Xsf7XE0Q0VUYyASedE5Qt3_4kkmiRTYO4JXUj44t6p5Nca3NHi0tNmsDbXUld4ndpfCpxyUzCEO3cAwn9NJdqDnXIWMfzmXZZNZb8rYl3WlPK9W29oRJoUTPAlqktVCDMQaksumIBN9hKh9DsTkb38sm_-nsh9dm25FFt6zlVMGSs_HAzehoWcshDO9T2h5I38D8-ItzwIdqHVf9FZT-4FyLefWVvDP2S-odxrC4LDcyx2RHlRvuLCVH7F_-9WkemMwo8dFEkRqwv9g_7t-a59cEwG1pgF70wmA_pLK53Dx8j5sCXN4W4d-oNQwXkD6_3xvCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhRjcK-h5xxokAovoTSlYwgWMk65ahGSSE8_rpSwrKseWQuquxLmHp9uI6-sST2zjEukth3ZQZ7smYVDdfQ_EmVz3fXAtV_V0cq41YUbx0ebu0A2rxh3M6sRa-vYwh77mEgLk4Xhg_SG3WyflcsrINueznY8crPr9Q28vZcNcJX1db38AktkVSGlXrvzyhw0cjq7I0jn5xi551XHLLAGdLlW1VzANshxC4eW0FleUxRWtQGuBj2j_qFlSHAbzXcJemkeNdSXYZwqFTaXtEOmNIyr8wQIbcl_1O2LGF2cQOi2VOEa5iE7IvcWOaFPKrNf1vdY3ufXmRu3PbPvegjPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK8_8dmkT-yIl_gWdqUXOIf7vnZXOzZI8A1hQ_S0yS9cFa9Kr3FNMP5quyjSNShG1kxG4gXQlTsAqeq8aDmdtiHB6rIdEaT04QwUkesiR51kCcdfmNxtllNEtet9bVw9T6e79udZ9p74ReLIryzJ6Qb_nCHbirVqzRippRrzME3yw33YIo96mvjN-IoBH6Mqm7VTSRmm88jVcrAYFlGJAjDzKWn14w-YyEM3QLXY8sArx0Gym-cEBGzyJoGexnR-v1b3oWGmETWcyTWTps8ulAeFoFsfh1XL3C5SQ1qAgwzLIAjOfyHlYU_4yMWUtcZ-ULR700KNhOYNqZGrFJDj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGmz0bnWPeIXTcbEyue2Iw-GnqdEVEfWZgpJM7lfvWPlgul5ChazP7sUdL2-MTaQZ7uXHRKcgJy29I9cFwtKA3QjRIS4_afYfm87ga_huexN7mnEZvDROaY0yv6UpdswON04Yzu_b19SkHfSlk71bKhGkocJAbGM8cKzLaFLbQGBtP7u_kVAxIyERPLJmEEwu-OQ3ruVrTlEYLJGUQLSoXpAQu_dQZSfHUtDqxc9ZqcctRwcWE0lu3-Mqse3Igz5tLfPrsszcKIvOaD_Ni9hzZQN4R3PBP9qxsjHXH3OUrOtHxBv0vbNNd8ROnhQ0bUJOekLLJDEan5JDmmw4z1zlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJ8IfAv5-x7xDFSjWjk235OXdGOHENVJcwV_QyUhbWsk-GHYvEuEQqB607OKYZbmKHej5L6gE7AO0m4TBoqNXhLBjApH3CowzIFE_k77lzTNgmz21n6vh0oNz3PqBM5L7yhjtq5E09zfXclwjXN9X2nGtiQvpgjLSuh4nuHiGAdCv9AAdjJlsgZpGRG2iTQYyGOBevuscX6MHeQGwpZoFRnqouD_ajF71eOMqkABX67yNTqvEb1rnPPP9bli0J1Z9q9s1Z1Rhm0YMruFJ3v2i77gHB2eq0MKElstVgd3bHf80bDvZ5kKVyq2GVkQki8S7lH4OuS5ZZGRmGHnTAUbDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gnUsqZQiryJmbJQfnjq0D8YIVe0dVnRhA4DR_gUMp-XX-ByyoWQ8dx7aVMbiXoRX7HZlk9JHb7PVRRqVVgxmcJopX7W55pvjlmhsP9iV5NW2ef3DJSfM8JSCV3P4pZpEW3OV2DGJneC-awiO1RqSJpJ8BFU4XnMJQGq1TFR-e8ftbSx375vNXuaweShfuxF3BIpL8Y9f6rGsEw-D5hxT6cSe7zldsfaVOtmI4sWR2Sq7DVXOemyVy_iLLB3JDuSfxjmJfh4T-tjXuiKnohQ9KwJoShzQMSLVh96GrjrLAkgK_JWXVVvQmwxYe8aljfoh7L3T434RQ3tuD_EAsAW5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyVWB1MPI30Q_wmKp7f8iF1txiRwoYHRMCCkh6sB0l_GUoKO6Ey0pW-SdeBh9m5Df8acK7XCiWMcJtIwt7V7CPLQIg_k6atsd8Xon2tqU8absxAtR02wTXW22VHRSPKSLZhEBdoaWWsEz_VOO-dKCwAxZMLYsxB8zxxfQOHpaM3rseAjwBSo2jZ6ZYQ10D7NmNtNlNiy_DMeB_yA-I7MOSR_WxPe0D2JBC_N_qWzAdH4Nn_zB6KxwW8KHApTMcJ7NZYfDEy4EgBH6ddBm9fE0aQVJvGGKX7qPs20Vj0c35peB_XF_PHX7lnYIrp9Xtkh21T0Vrf_4PRwRaWyg-e28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfRJFhhPVz2vw2oiZynVpRrI1yLI_5gJASaioWalwYDK2Eg9W_GDg9Iou-44URU1eLb9tf9JY2QW59WJ2e4m3bNs8pjtCpI5z_YaPINiGPlfpGuJK2B2hY8brFw42qzBlUoOj1K3hG1tUiUc-N2TWxx9gTgHLEIVhq3w8QqUsrMfJl3XsX-hXdjoLt76ng7-wyj5n7PMjCveveVzxocq2kc6KQHpTdx8AV19lNadNJBeUZjOz4fOYWTu_mJtHHhsOrSxk4xEnwPCexWnIZMws8r4JoYbgp0sJHNUqilOsy73Y5FCzb5zLTJvhfMhdYFZVdj6N4LBhOGHVRLdWmLYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIoNQqz6DN2t2n3_jNwHir1zATJppW83Heza5ye6c7qLN0xCjjXyw2UCc-DA6IhNgFiYFXojlwZkQsv5IA8YO3CVw9MGhvx7DIf-wUtfxGPD4d2mDQjNKjOhP99-G1VZvs92HCfXduSsEbCxFg-3jv8QdwosgVcp8hnHxfsilAHjrPAf8ZQWEg3xaK7XIrtNldHNmKvBmvZtie2RAFsSKx-WTjT9cUvkfkKSE-ZD7gg86ivtaRodNlzeYa1CPGj8i6R5DcyVthYuo0-3w0x_wMybKfnqFtQyJpH0m9ucrHmeuYV4ce_V5VvlZBhbEEC2Ya_MS8ZZy_LgHwqbS_cx7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cw6Iy9_TF4BG9n6KWd4zwM6SkA10rvj63-zery4n_K2Q6uCI0_VIRi_uF_yOuGe3jMQyC8opIZBBfne_1fCCX_n9CgMYh8Dl5Tidv6YoiELfxfJLFAch0oD03tCm02frDbnjCDMmLRRantI4Bf71DVD5-ZmfIS48f-HTkKc9-5Y5PBNFxqZWDdmlyg899G47CLEmhZW2KpfELUpZGXy-u8jKYMHZ_5Qoe6YOfE_33xcl59mjnmkvISc8IhJzwSMOBPQrP50WrEQkiVdh4asjUkNZq8v6I1hAdCYm9NiCm4yxvpn5qHMs4SLBWIgJAWqGcMsKpTtD_tyS-tCL7RG-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDb5CZ_H0jULMqmxJ9U0Cm4sJg66rEB3BWexx6Yqi4WjhJBZV2ayDoGfSUEO6c2D5wcOuo44zcK5PywpuOps7d6X2muY1lQJFoSXAxmmZNiuEQrHIIehw8lFinnqN_D9eBRn74xrMyC-idWGOchiyKvK4PBay_J9M7z4SzkjWMh03wHq9ayYNYyKf96Y4HF_34GbhU7dppN8HwbaJAUhNFbsPnGhprKdL8K0JLhomPhnrEi6er0hb310Gf4BiRZ5UpPCbhep0OJQf9Fb0YUGyo3jzIqQFmjajFX3XGMGf75XvL71pZeDXsvE2fdTLkvEp5fHeJiWc0RI3VyleQTYmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8WEaigoogM3nz0WoJezyWwMGPipzWTCCD5VayWG7GJcNdDCPdenLqJSELGN7Q_hZj6fmk36NnUN-YjKxjT2Gb-AiQuTH_dIHkI7LMzuQ8VQl9n5dP6wKl9Qx9CGmJyQsBOsLhzjdXFfgQEcDQopAjBaGuQXR7raIWAgzu-50VsI9OTrI-jwZtMGWyV5NMV1u9l_gS1Xq-InAyyVzkrcNfgYzL63oMaU8XzjjZjg-JHpNjs447xQflYf-WOTmyNBmtq35pF7OgTWEIpXWYBduAu1mHj_DeBHXlnHusUV-KUfAjeuZY3oiIvEOhD8a9zVyO2_l4Mpl6Cr3fmJ4ftH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=qFPKXFzATOxvDpqZZoHupeA1EJyq_AnPBArG1YFUK4UZ04UDQtF5uB3zMY2hvqllAEEbDSao9ppjtl6VkMUmzTX55Xu_HkWWttnI2oOTEJw8ss1_JoeVIv5egKUGfklWMQu5l9Q5W09H5AS8aO7X7p-GjG3aByA69uojdvkTqr1PKyrMT-FTTVVafIFinJjC_TDzXuYARDbORjaEXmx2iNZRvK6m-0DYb9HQh7bU2Cl5miCCsOiqN2TLTNgZECyQyFTVsW-xTjdtSxgjUgi4P8PkFrMP3lX1mS-rdAsW9Tk3l2Mdg7xHfot6lO27dmzBkQg_rf-Fb7YQGEC2V18SMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=qFPKXFzATOxvDpqZZoHupeA1EJyq_AnPBArG1YFUK4UZ04UDQtF5uB3zMY2hvqllAEEbDSao9ppjtl6VkMUmzTX55Xu_HkWWttnI2oOTEJw8ss1_JoeVIv5egKUGfklWMQu5l9Q5W09H5AS8aO7X7p-GjG3aByA69uojdvkTqr1PKyrMT-FTTVVafIFinJjC_TDzXuYARDbORjaEXmx2iNZRvK6m-0DYb9HQh7bU2Cl5miCCsOiqN2TLTNgZECyQyFTVsW-xTjdtSxgjUgi4P8PkFrMP3lX1mS-rdAsW9Tk3l2Mdg7xHfot6lO27dmzBkQg_rf-Fb7YQGEC2V18SMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=k7ahOPPCCt3dL7fonu3T2ceRfhUYScAaUZduc9ofpGCX0Mha7lPsgVSjjkHflyqcGSE7EuXF3NBjm4CW0Ts4LR0GOJpfydTctdWLUxE-06_OFD5V1Hg75ZF61uL7dBoCJdImTATqUpBqiJO7g8S869To16Cz2p3at4nph7oQ7C5xtv7bwlWhI7HiZv25vUcGb6ZDCgZLnIxmmLsAGCx8sH-5WJ3q-3opkxrDzXoou9hl8gAnUf_jD0tYTlBO6s6JBPD1762Nhjn18Zp6OJJCegBDQwDiwQhxh8HGT1t2ltuhgQV8LZAp8VKyehY3V6nAJL55Z4MUTdWjFM-SEhIZuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=k7ahOPPCCt3dL7fonu3T2ceRfhUYScAaUZduc9ofpGCX0Mha7lPsgVSjjkHflyqcGSE7EuXF3NBjm4CW0Ts4LR0GOJpfydTctdWLUxE-06_OFD5V1Hg75ZF61uL7dBoCJdImTATqUpBqiJO7g8S869To16Cz2p3at4nph7oQ7C5xtv7bwlWhI7HiZv25vUcGb6ZDCgZLnIxmmLsAGCx8sH-5WJ3q-3opkxrDzXoou9hl8gAnUf_jD0tYTlBO6s6JBPD1762Nhjn18Zp6OJJCegBDQwDiwQhxh8HGT1t2ltuhgQV8LZAp8VKyehY3V6nAJL55Z4MUTdWjFM-SEhIZuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=JffOtuAdwNahaywfIiwIPaIAoaACxx9KDcvgSy8sIGZXPDLJ_dPE5sbEOmc7q35bPJK-4i7U6ma7r-0_QTiNyl0q1kYc7U_5U6BuqQQIkCQ_b4RVLczb64bBGeJQL7jQxUTSYkSQNAvx1CApwffERbJuYVx7CYYoZpWD1CCCho0-wBWpw8roWJjRjFSEz7pRhWzcU0MR8VOHj8uTTB95WOqCgEIuvQyPE1Bj5uSIVTyV-pXGZLhza-c7Jlv3yM9A0SIF1ixffONmO32d_b5l_A-eVKWVMbIQR33WmMdVH-1XMfXAlzue5DffbYiKsbj6CMmS2H2-mcmR1LagWCHjAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=JffOtuAdwNahaywfIiwIPaIAoaACxx9KDcvgSy8sIGZXPDLJ_dPE5sbEOmc7q35bPJK-4i7U6ma7r-0_QTiNyl0q1kYc7U_5U6BuqQQIkCQ_b4RVLczb64bBGeJQL7jQxUTSYkSQNAvx1CApwffERbJuYVx7CYYoZpWD1CCCho0-wBWpw8roWJjRjFSEz7pRhWzcU0MR8VOHj8uTTB95WOqCgEIuvQyPE1Bj5uSIVTyV-pXGZLhza-c7Jlv3yM9A0SIF1ixffONmO32d_b5l_A-eVKWVMbIQR33WmMdVH-1XMfXAlzue5DffbYiKsbj6CMmS2H2-mcmR1LagWCHjAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=Af402NURCgG1BSrRly2a53-l4OAVzkgWhh93R7lahJA_SomZj70mqjNCWmbd2LUsx2KOTDZNosYAeFRulQoWWoXwgZdIolIijIicLcSlIHGehQg0nP5Y565T81o9I9ZtIInp-sM5_5k87ImaKmkG6nMEmn-7dsqZGs4tq-_ZV3MQHYYWXSp1qt-y3VkDC8Ju_Vzwb8BIxyfEr5rX0YWd1eDc2V0yEBC1YsT_rnN6-cIQoNWNNBwaD2vSOQOwUlPTyKDdFM6Da8V0XPJGuUZICUy0Q15jk2YydUx_9mx_RiarpRS4nn_L5jYH7t7QJaP8uLMOrNb2CC8jhoPLB8vJag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=Af402NURCgG1BSrRly2a53-l4OAVzkgWhh93R7lahJA_SomZj70mqjNCWmbd2LUsx2KOTDZNosYAeFRulQoWWoXwgZdIolIijIicLcSlIHGehQg0nP5Y565T81o9I9ZtIInp-sM5_5k87ImaKmkG6nMEmn-7dsqZGs4tq-_ZV3MQHYYWXSp1qt-y3VkDC8Ju_Vzwb8BIxyfEr5rX0YWd1eDc2V0yEBC1YsT_rnN6-cIQoNWNNBwaD2vSOQOwUlPTyKDdFM6Da8V0XPJGuUZICUy0Q15jk2YydUx_9mx_RiarpRS4nn_L5jYH7t7QJaP8uLMOrNb2CC8jhoPLB8vJag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U-bdgPcZXgt3xDVduxrXAf7UKgJAmoCHEFgc61I4YukDgX2SaSKNJSTkb3Rs10EQbuAtQdjrDrXJr8AxvrD213RCEniSDbB5wcGv0zsMJQ1tSm56tRJzfSVrpa7-dIuFihBAkfB3fJ6AXv9equ_MY7z-YGJL6Ak5SivDCIwXvJcT83xsNCPFR2hwCXuVv6O1EucNzuZeALoFgonKGmEnGGYoWCu5M4Fz7g1IW4mL3kjgaH_T9ug-rWhR1cZaTDj7oQOa3QimMDSenBQRMhvbP5Y-vznt7wbMVlu3OpNdWZnB3-AGw10j8IppQFRU51rx6YvxVxw9m3vB5WkgWoIxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUlwTNLaOJqVqUtLrxyz4ieABnkvMYRORZhRp7t_Kzq5XAi6im6yfkfRPENonIM1hDou1c5ZPERSO6iOuywtyOjz4ZfXC-7P1APV4B8JKhAof0Rw2_R0tyhBHsrB38bgyfpkMjzeZwmnOgWp16wnWNLHsg3guUJwL3qSVyxym3dotk95VNdgc2AZKGIVy1KZfHvR9OpnkHNzwNI0xQ5FLoNAzm4fR7IYCVtDfyYEhxjAqoh1DRiZvAeHomS7l7Jy-RjPicCtGS0_MKOioJEWO-jeKikjDwcryGkH4-WxFZlMeb6XcHZ4UZKGzot2QKm2bN8g36ODd59HRp-9b3B87A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3CUpDxllCc4i_VAPcJHM1Pfgpd0NzlBVnwx056IRBxysBDarRNxUSqM1inWdt_Z1jINnvGksodo4-fJr3VxWuDBMZvQgGChJinVumWSSuQusfFBAr2ns2PiHjfAdARtq_Czvsv3WwWzEsfcg9H1OX2_B6nvALLTfdIpqZ9ADLG1pAmtYI1PzgrpfcVnZV7Gp1FMIDKDO5Dama7HRYM6CdAZSCJIQjR0-7ldm-djHx_9xeCylqD5YwpdLjW8kEMtOQ-z0t2XdMf8zgT7k-B31YYZLKk4_ifqwe7LKxEycVECp1ZnSM8_6qhxRcn6gMgcqUQo7zNF5Fuy0bUIeP0sLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=BaWNG5w3Brs7VCRHwHtzur2AsndK24RngCj2ySBXkLVebCsBXWZwdY3ZacwlQKAPMPtqOtg7nAZlPsvgjqdqsy0UvzTUjzgrgcfxEaBY54-1SnTBX6-sG-lYyRfTWrpTduJMqrYICR2YRKz7azrceDTyLnGr2Gns8nqWpLeD0qGBViU7su3BE6oY6ZhKqPUhDxSXDAqHhO13I5rb1SecZL2ZotDYbfeFnDYXMCsX8zZSWwBTlnj6opDKviWUpQ8wnROUUFeE7EeWWvSf57YPOJB6Xv34OK24mB7kzcd0AmqG_OCGe2AijxH2LX-EoVYqVL3VfYJfrbLI_XswEcOhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=BaWNG5w3Brs7VCRHwHtzur2AsndK24RngCj2ySBXkLVebCsBXWZwdY3ZacwlQKAPMPtqOtg7nAZlPsvgjqdqsy0UvzTUjzgrgcfxEaBY54-1SnTBX6-sG-lYyRfTWrpTduJMqrYICR2YRKz7azrceDTyLnGr2Gns8nqWpLeD0qGBViU7su3BE6oY6ZhKqPUhDxSXDAqHhO13I5rb1SecZL2ZotDYbfeFnDYXMCsX8zZSWwBTlnj6opDKviWUpQ8wnROUUFeE7EeWWvSf57YPOJB6Xv34OK24mB7kzcd0AmqG_OCGe2AijxH2LX-EoVYqVL3VfYJfrbLI_XswEcOhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPAuy12D3ygTN3cfgvnICJjj6tKGHZA299hLihyCvgM5reWN4SKGxQW0vK-sIJX3zrfyCWptJMroGwg6U8D-d6Www13HFzaMeyotiMH8cWJqjccyQTgY_GS8qgxoTioaGP7YahezVw9nJxq9XfGop-Zr23o2Sy3RUdpMR0TzIqEsRisdacBXrybdRs7wBLQNJVeMM_hmfMO03zqlRO76qn3N2OxhqlkXvVyzkPR3Jlq7xdT0gQA249FEyT0-VSzUrXMJe4Tqd2bPVBbbfD9P7rz0XFd1GcnoNzxa47Emg0JkaQ-fvw7vlIBNYzEsmmqE59I_RAdVz9e9jnT_lI0L6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=GFoJD6Pm0HRxP6VmJrWHPk6j6Wh4a1Zwc3-z33uDYk7TTUopAAgcgUuRhctAM_65fWrovEnaTBHmgWsLN2-WqSuqmybhdV9ct21yQCzngukTQRjn9_buDLzOL_jNMFMbA-BTUySPXfAKhU6xhXSxMq1xRc-GFunAG1RXDQTitqoLWpGVm3VgjpHCpbAj0izbdh6V4z6LpBLox362H3QoeN_hXnkSv_l8P3ar4uH5g5bQgPFILPyjBzDuSgtuEgMFYNZGCTFGCLRt9jNp1bKNvn1zAeD--8PTbt_8a6Yqr2B8FFs1FgcFSm_QhgluluhiBVNJ9be6FOhh85B2qXx4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=GFoJD6Pm0HRxP6VmJrWHPk6j6Wh4a1Zwc3-z33uDYk7TTUopAAgcgUuRhctAM_65fWrovEnaTBHmgWsLN2-WqSuqmybhdV9ct21yQCzngukTQRjn9_buDLzOL_jNMFMbA-BTUySPXfAKhU6xhXSxMq1xRc-GFunAG1RXDQTitqoLWpGVm3VgjpHCpbAj0izbdh6V4z6LpBLox362H3QoeN_hXnkSv_l8P3ar4uH5g5bQgPFILPyjBzDuSgtuEgMFYNZGCTFGCLRt9jNp1bKNvn1zAeD--8PTbt_8a6Yqr2B8FFs1FgcFSm_QhgluluhiBVNJ9be6FOhh85B2qXx4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=YYC0Bz1oTXFo_c0EsSM8wtKoGEoCLN5xa-XRnWMsXdfeVQp10apVz-9ZcC0F521jwV6XXHR92GQ4ZSSPqxQY8OHUVWS_HUEYZ9czD4s7hiAo9RTQ6Ki9ClXYoUBrdLJqYvL-rwyce5QCEovnAP5KOfjdh--hB46kdPtjxO-HOo_lff_xJVhOIm9QjUF957X56EY8Y6Rx44TE5nlUnBnGQU-uAEqr8PpQ1Rs7FBAl1m2-HMUSmcqiHa82dckM_Lx3b2IRDR3MY-zLQkFtWz0rl7V-rLY0RdXNfkYfenBUlNTTxmcZXg8ibRyAJfRp8WDjavqsuqJ_REWHo4Jze1wyQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=YYC0Bz1oTXFo_c0EsSM8wtKoGEoCLN5xa-XRnWMsXdfeVQp10apVz-9ZcC0F521jwV6XXHR92GQ4ZSSPqxQY8OHUVWS_HUEYZ9czD4s7hiAo9RTQ6Ki9ClXYoUBrdLJqYvL-rwyce5QCEovnAP5KOfjdh--hB46kdPtjxO-HOo_lff_xJVhOIm9QjUF957X56EY8Y6Rx44TE5nlUnBnGQU-uAEqr8PpQ1Rs7FBAl1m2-HMUSmcqiHa82dckM_Lx3b2IRDR3MY-zLQkFtWz0rl7V-rLY0RdXNfkYfenBUlNTTxmcZXg8ibRyAJfRp8WDjavqsuqJ_REWHo4Jze1wyQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=bkfOB_lq4TvKA6Z1LS0qzg9evbx2Q-zcRR-9c2GnoGurzjudr_ylFF8sdGHVNjHHjc-S-Q7v9mm1COFJf7MuAas60lq2MGjqdiT98hpJ3heZV-wWtmYq-aK6RHtQ_7C7jWhCtTGkHTP1pTycG8BArzQviwsL5f076bnmzL5TkIpPxUFX5gXz34pc-N9VlvFHL8nApjnmwZ8q53MezQVSE2TZODmTMHx0qNZlYYYMsS6CW1XnSGjnT2kpmEq0eTRbYMcp8i0NVqWDSOymr22xb-6krg6vTUyFMjIZH_ZT1EFTBI0EfvUkCDi7Ti9rsRgpM8Em9eru_bcKEfW5Ulqvlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=bkfOB_lq4TvKA6Z1LS0qzg9evbx2Q-zcRR-9c2GnoGurzjudr_ylFF8sdGHVNjHHjc-S-Q7v9mm1COFJf7MuAas60lq2MGjqdiT98hpJ3heZV-wWtmYq-aK6RHtQ_7C7jWhCtTGkHTP1pTycG8BArzQviwsL5f076bnmzL5TkIpPxUFX5gXz34pc-N9VlvFHL8nApjnmwZ8q53MezQVSE2TZODmTMHx0qNZlYYYMsS6CW1XnSGjnT2kpmEq0eTRbYMcp8i0NVqWDSOymr22xb-6krg6vTUyFMjIZH_ZT1EFTBI0EfvUkCDi7Ti9rsRgpM8Em9eru_bcKEfW5Ulqvlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGh4rFincGIppMyF52bJIZ_GIuDiVcPBI4av5Q0PBaXiM5Z4i1A81hmd9BGXZeSkI7oY0TNwtUa-hu_aY9uv_wYyqOubdGGBdIIm1lbR-v-a9Acp9b1h6IayAUdAD5AL6OOAqzZJhSAJvditzKz9o1e7Q6w5ei5fjzSciOsJEpTIMfcZ6gL8NO62lMu1IBmXyGi3xV3pO3PfORhP4yWpNz-tE5HDfFZFK2-cBVZqZ8fEo8exJp_8303OUgkEQX0edp_8GIS2aPYGEH6Hkpmp5oH-Fh2wrJ1c9um_OS_WzF_5Jd-DhMnT8piPCqATy7CrLyOSnBkpECizVTVHLn7jcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=mr3xlguo4tSPQn0orEgyKiCnGV4CJZsl7XkuIZoYD1o85qH294jpOMgWOxwdvZjQtkjaNqndn7IUVLYpL5n5drw4IsK_-a1su882bJwQ68LEEAVA4IQ33j39x_xljbQHEXDUnq0kZzKsrq9CN3-BO63bxeefH2dQdMaHq5MmSYZsZOT3biXJYh1tHXIx0E_mCmKQge5GrBRDyHilZK6Q1VZaK4P3Ed2DAHDS9Qhk5clWQ-Rcqhcdo2W0qHK9v0PMKx4ooNvG7qjkIvrF9cmADZMJMn527WwgdV3NZuq2Zaj3F5UGgF37ft0nnnTra838F4O16sVBJdDSUpCbHWJoiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=mr3xlguo4tSPQn0orEgyKiCnGV4CJZsl7XkuIZoYD1o85qH294jpOMgWOxwdvZjQtkjaNqndn7IUVLYpL5n5drw4IsK_-a1su882bJwQ68LEEAVA4IQ33j39x_xljbQHEXDUnq0kZzKsrq9CN3-BO63bxeefH2dQdMaHq5MmSYZsZOT3biXJYh1tHXIx0E_mCmKQge5GrBRDyHilZK6Q1VZaK4P3Ed2DAHDS9Qhk5clWQ-Rcqhcdo2W0qHK9v0PMKx4ooNvG7qjkIvrF9cmADZMJMn527WwgdV3NZuq2Zaj3F5UGgF37ft0nnnTra838F4O16sVBJdDSUpCbHWJoiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNST42PGtN5VgmCyY53OhzvfZzkLRFNitwr77YCuC8YfZ3oiu6w2_fnGAmGjWUqx_76_dfB-GLEeEcmjwC6Wzs9_fQKCB8_XCCza5EUsqQKETUhPIrkn-pnJCSfsdsIs0fn-9hscgB3TQhX3nq5P2BNbu1fBpedwCNEzHbuRbM2noHctaXjBnYh6tpUeDCiiM4prqflX5_A2R7wQW8zRjIaw-f4T6u6NaQIuS8u1JkjWLsOR9YoW5lCaNEhoVd5ZuQiISI5G2RWAYfdxCD8BU21ylLFmBgGwYXge93knrf90ccfaUce_NFfKUEjwViFy8wBkXa57zxLpUQFsKXasVWD6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=txMd1NkyrThd2qmUK0X9rd8sZt-wK01qaMw-dj2HGJzjZzo2NUJcrOKsd3kRQrE5_II4lO1CDHNDuNfaevIAi4lY75l4p2dDp_PCfD5JG4dcRtpM2xnjCdCSW-JwUY37XN3gmuuXuPTl_P4g6KnwzNBryM8kfRbjaU5gip10jh-w9eGCaaK3vQp1c-wmmtKEDEzVb3XxtW0mB_q8gMnPU_4XWFLavJocBh-IhyiCEjLhS-ltLawAT8hGrixYUPW_ksheO83FBK1b0e45qY72SK7Atc9VzFBRj1QeOqC-EVhCAsLQB8f-kbpV4uqcDZ5RpN_Aul9wmrm2IG2_ZDiNST42PGtN5VgmCyY53OhzvfZzkLRFNitwr77YCuC8YfZ3oiu6w2_fnGAmGjWUqx_76_dfB-GLEeEcmjwC6Wzs9_fQKCB8_XCCza5EUsqQKETUhPIrkn-pnJCSfsdsIs0fn-9hscgB3TQhX3nq5P2BNbu1fBpedwCNEzHbuRbM2noHctaXjBnYh6tpUeDCiiM4prqflX5_A2R7wQW8zRjIaw-f4T6u6NaQIuS8u1JkjWLsOR9YoW5lCaNEhoVd5ZuQiISI5G2RWAYfdxCD8BU21ylLFmBgGwYXge93knrf90ccfaUce_NFfKUEjwViFy8wBkXa57zxLpUQFsKXasVWD6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6U2z8JRysek3S_Hqs7c64IBE6tvS_JMtyGwgRwJDeNBCC2t6Z-w22-QCXI1XmZRngjFDVKxMptGy-zwrSct2qdpEHkHlY8tpMK9dI6-AtQT9r3U708EAC5EveO932LsjqcgKRC7Io3sCcI8XTpZRWDY57eXMj3cYje81cXJKRcXR8WDe7LF6p45al4wjUv1mSdJ2Fp35CBVWhkAK-MFhyou_b-WHyiDJ2ZidCq5h146N1mFrZktKalusrnDjSuM0K-tSrLGwbgKOREqFx3WDQFL47IzAyTxHOFrg03vuOgPW4et_Xy3CM5hrsZqWzff1vZFaIwW-r-uBUKMAgbkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Kadn0Y00E_caPQ8b0anCpmWCirLI4a8Hcwnx3fVcZsiU-kSTg9clkw7E9lPLzuTcJIoLcqlF1TNcDZKOIdq8741ryXQkFi2RPy_BH4KGBOWYp9VCJ3r00LYDfrJity6IBIursqMlhY4fyUTXDG8dOlr9ro30l43nRsB1SSGDRji6iBRhlMTtNIpD3XXnytv6MuA-EcPAWKhZ1XN8giw4lrA5EpcCejWbYL0kgtHCDSEtlVjbT5vLtRItuG6VEIHKVKPXtPxRuhC5TwSI023WNHXUstoPfGxEgPd5Uw4G5C9WDLCeGVRxTgwpcaIMaGI0kieCndnk4HNevAEXq_GtkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Kadn0Y00E_caPQ8b0anCpmWCirLI4a8Hcwnx3fVcZsiU-kSTg9clkw7E9lPLzuTcJIoLcqlF1TNcDZKOIdq8741ryXQkFi2RPy_BH4KGBOWYp9VCJ3r00LYDfrJity6IBIursqMlhY4fyUTXDG8dOlr9ro30l43nRsB1SSGDRji6iBRhlMTtNIpD3XXnytv6MuA-EcPAWKhZ1XN8giw4lrA5EpcCejWbYL0kgtHCDSEtlVjbT5vLtRItuG6VEIHKVKPXtPxRuhC5TwSI023WNHXUstoPfGxEgPd5Uw4G5C9WDLCeGVRxTgwpcaIMaGI0kieCndnk4HNevAEXq_GtkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-wZzEQZ_bb8N46JI7GUAM-M87dDwNnXf9GVmNsJodhRH3vdHbfCfBL32YzniLhj95CTUjxf_yDr9rAHOY-hdih_iIPDZv38sLzLRjOPGP1nIyZVqqhXnApKNaf_zDxJ3TYQcYo91DpBnlZCsPcyPdkkRqtD5zme36Tw2yOWnBltEL-_OEvILRUpLOt7FbI4bk61QwBckH54zaZqol_ChqPDYvvmoLo6gZK5tZ1DuZSPNIlD5lvjZvQFY21QcB1NvyWHyXM22nVrSPE6BoEvPGbojbIJ1V8HyvPG6SPCGbmQdgeEqNdqEC_ELSRu9gZ0mygQ8_jy2qcKs18Ig6yF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=lCIlQtnAj9HCLhgrc-cHi7wccJrj_UTvRd3t7zQglk6mM2gbwCa57zbJkaj13F6BY4d2teGOjRvvbDGOtYO3An5lqziFQlBgdzf2-GwaAFUgPi1wvXKzbbHmsJ3zD9mGObysafi5fvukXar3pebwVhHehBAy_TyOJbQbVA85SZmKvD796SDwAlMv703cSIfxSQbHFr7ucFmLZaao9FuW7M8q9ja4e-rjNAsJnVxGLOZtrRJ-lVFwqQtaebnqlnJme2yLUnRDUyxQNTYnSsfLwLeN7CUfdVrnRWeySvUzh0wxQ6YIgN4RsVc7NnUnurme4v95LK97E4NXyKacC4pivDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=lCIlQtnAj9HCLhgrc-cHi7wccJrj_UTvRd3t7zQglk6mM2gbwCa57zbJkaj13F6BY4d2teGOjRvvbDGOtYO3An5lqziFQlBgdzf2-GwaAFUgPi1wvXKzbbHmsJ3zD9mGObysafi5fvukXar3pebwVhHehBAy_TyOJbQbVA85SZmKvD796SDwAlMv703cSIfxSQbHFr7ucFmLZaao9FuW7M8q9ja4e-rjNAsJnVxGLOZtrRJ-lVFwqQtaebnqlnJme2yLUnRDUyxQNTYnSsfLwLeN7CUfdVrnRWeySvUzh0wxQ6YIgN4RsVc7NnUnurme4v95LK97E4NXyKacC4pivDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=YQs2eemBhOSgvvjpjjgNsyN6sDUGtVxgMXuY6c_fG1U1JNnttsGT7jUJoee-AMOABNEYC2QeL1QD0LEzG1VbqCX2NAHzlNZy7hugNhFZFBPqWf2Gd9v2B9VG96Fr9BZCEdu1uVGFn3qynasiBp1sNYSD1En7FgmRDSLxonT7V4hkbA3qlkHP2omiv34WHd-WRGUmF67N-V9D_f_SkgFgZ_DqbQZQsuXEx6EqKfhMrIFBtbqv-bE7jdHOgAnKj1N1hOJBZ0JgUbBbkcRY21HqlBX9smk_9H4Xofg2k60bfxbKMTW1Ubw-DqiyhJoTz2LW-fAe2ibEinTVVGp8qXR3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=YQs2eemBhOSgvvjpjjgNsyN6sDUGtVxgMXuY6c_fG1U1JNnttsGT7jUJoee-AMOABNEYC2QeL1QD0LEzG1VbqCX2NAHzlNZy7hugNhFZFBPqWf2Gd9v2B9VG96Fr9BZCEdu1uVGFn3qynasiBp1sNYSD1En7FgmRDSLxonT7V4hkbA3qlkHP2omiv34WHd-WRGUmF67N-V9D_f_SkgFgZ_DqbQZQsuXEx6EqKfhMrIFBtbqv-bE7jdHOgAnKj1N1hOJBZ0JgUbBbkcRY21HqlBX9smk_9H4Xofg2k60bfxbKMTW1Ubw-DqiyhJoTz2LW-fAe2ibEinTVVGp8qXR3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=QAU_Pf1_N9fRCHPv0Zzurbpea9ZE6cMb5k-wTxpU_iDqlBD6GIAEUM5KCAWPHLs-H3jTwWM5gmfnHRiIBhZUnWaHZHZ6Esz-BL7atICCsb9pwwHRaV8T16LTbTw6TKxW_7RSFqaEywr5kdNiR3seYnzw_cUX7BnRJFfbmt-ndcNCINXEEdCqB8ohYailfC32-K7y--nvHHj5BZSGHoXtCdhLqhzwTkIvPAVmhD_9oRytgFF6SZEY7sWxyO4KeuyS8rFlXOm58kSOL7kO14jJJ1rcl2uc-0ex2OF4o84ScEaYWfSx52449depUbr_72F1msY4HiCgLbyrZgfAkfYjHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=QAU_Pf1_N9fRCHPv0Zzurbpea9ZE6cMb5k-wTxpU_iDqlBD6GIAEUM5KCAWPHLs-H3jTwWM5gmfnHRiIBhZUnWaHZHZ6Esz-BL7atICCsb9pwwHRaV8T16LTbTw6TKxW_7RSFqaEywr5kdNiR3seYnzw_cUX7BnRJFfbmt-ndcNCINXEEdCqB8ohYailfC32-K7y--nvHHj5BZSGHoXtCdhLqhzwTkIvPAVmhD_9oRytgFF6SZEY7sWxyO4KeuyS8rFlXOm58kSOL7kO14jJJ1rcl2uc-0ex2OF4o84ScEaYWfSx52449depUbr_72F1msY4HiCgLbyrZgfAkfYjHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=pPVQEQmxRTqQW_eyMgM2DluRM_PgVsexTw6B0tE8H3NRRFp12UbvG-NnLi3rySkK3O1ba9UwOSmXAcwqM_i9PqWBxiMeYXIDqRVuGXWMtWJrzUIGaicQ6Qctu9T3vh6u7ML1RpKy99AJOx-pDFRMFySZQJUSYqQEyXL4_6Q6SmIDSGG6NghsxlY7MTyvk_PlOQqblfB0wb-Eh3Ca1i9wkipkULxY7tpTXnmMD2RRiFkG9-YISUQh4xBCfefRAqSBC9OQ5LDDxD5AESiOWzFqow6pixrgDxTGLDlvbWU30ZQT7-Yc5QPVEHNQLGsCYZ3XPIkEmtf1kcCZRL9cYElrXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=pPVQEQmxRTqQW_eyMgM2DluRM_PgVsexTw6B0tE8H3NRRFp12UbvG-NnLi3rySkK3O1ba9UwOSmXAcwqM_i9PqWBxiMeYXIDqRVuGXWMtWJrzUIGaicQ6Qctu9T3vh6u7ML1RpKy99AJOx-pDFRMFySZQJUSYqQEyXL4_6Q6SmIDSGG6NghsxlY7MTyvk_PlOQqblfB0wb-Eh3Ca1i9wkipkULxY7tpTXnmMD2RRiFkG9-YISUQh4xBCfefRAqSBC9OQ5LDDxD5AESiOWzFqow6pixrgDxTGLDlvbWU30ZQT7-Yc5QPVEHNQLGsCYZ3XPIkEmtf1kcCZRL9cYElrXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=PzidScRCDifISFbtqBt9-TS8vV4BhzT4b5lbgPpG_Bd5s4AiVLCV8HT-M8Yg05ue7MkA_s7Ihzzf5FavwWewbFsl99Fe1W-RPIcuwgeSne1o0bZF8323gmMv893MhZ9rQpxU6WGV-58VhKMVx-ek0Irh3I9TTAMZSz6P5grz7GuLADjuwsrqN28NJL5yoNmr5s5_8BTl7H2BYhUFlpWt38R1Ch2mUSBa8OMBsFw_OAIULAjqrlZoRRvDDQS3gvwFg0u33J1Gu2LFMcZfZfrP4YGb4EGznm0P6rzWLySwI9F9ZtDsW3DSoRzJ2UdqwiLat7Mu87B10ud4s_F8rQ4yxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=PzidScRCDifISFbtqBt9-TS8vV4BhzT4b5lbgPpG_Bd5s4AiVLCV8HT-M8Yg05ue7MkA_s7Ihzzf5FavwWewbFsl99Fe1W-RPIcuwgeSne1o0bZF8323gmMv893MhZ9rQpxU6WGV-58VhKMVx-ek0Irh3I9TTAMZSz6P5grz7GuLADjuwsrqN28NJL5yoNmr5s5_8BTl7H2BYhUFlpWt38R1Ch2mUSBa8OMBsFw_OAIULAjqrlZoRRvDDQS3gvwFg0u33J1Gu2LFMcZfZfrP4YGb4EGznm0P6rzWLySwI9F9ZtDsW3DSoRzJ2UdqwiLat7Mu87B10ud4s_F8rQ4yxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=ceplP-YEqLwI4ctW2_WR9F9z2bmb3Um4rZgawtLD20NtlDcGy_Dbbqtinq6GKYy-ViK9u4Qce4cYBUyPvmQwO5lVWyRCwlHjqE5EkaWRVTmSrV793nBxwWaDg8xoMUhiIXibPTVaql3uXPgsXwEWY8BpwZ6COdvzyNdBk1yGZ__jCIF9d73EPFSKPEeP8gSbf6h_Pcpq4jcJqsnDF5a93o2guR4umvDdUyVG5H2oTHYtA7Et-zuQNdJjuCTJR7M6Cr41OmZgxnwuQyurR0dE2H3_6j-eaHLNFB27pTKpoCOA74paxJz0D9E6VkH5PA_IGv4A2jH0ih_ISR4F7GMbog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=ceplP-YEqLwI4ctW2_WR9F9z2bmb3Um4rZgawtLD20NtlDcGy_Dbbqtinq6GKYy-ViK9u4Qce4cYBUyPvmQwO5lVWyRCwlHjqE5EkaWRVTmSrV793nBxwWaDg8xoMUhiIXibPTVaql3uXPgsXwEWY8BpwZ6COdvzyNdBk1yGZ__jCIF9d73EPFSKPEeP8gSbf6h_Pcpq4jcJqsnDF5a93o2guR4umvDdUyVG5H2oTHYtA7Et-zuQNdJjuCTJR7M6Cr41OmZgxnwuQyurR0dE2H3_6j-eaHLNFB27pTKpoCOA74paxJz0D9E6VkH5PA_IGv4A2jH0ih_ISR4F7GMbog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=TSYmHAROb0ZXGQOXvf5sD34N09dKkBuc3qB_piK3ubCulnV6sxrcmbXTazt5hBQuKhZEGULqyZw2HhOIJTRruVdjq39tkKMy5m8XWxyL8-dvxRr3ID6vNTsefSuXANI3jEklUbv8L7sMPLD_fozgr0xcs3PMKo_tz4ds7qf960nUFylPPGuG85a3oJLUxYavd3Joxc0O6N6qref-P56HcDu4d7SPr8TBR1xOUSs2mYX-6lqY7sE4h_dhGBysx5YaqEvdbzBUx4HU9ouqwok0MAk6AaBtG4Qt7JWY_dOuheMZw9fIPQE01glRWCIBFscPTwRWvailv1ZhGVacJlUajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=TSYmHAROb0ZXGQOXvf5sD34N09dKkBuc3qB_piK3ubCulnV6sxrcmbXTazt5hBQuKhZEGULqyZw2HhOIJTRruVdjq39tkKMy5m8XWxyL8-dvxRr3ID6vNTsefSuXANI3jEklUbv8L7sMPLD_fozgr0xcs3PMKo_tz4ds7qf960nUFylPPGuG85a3oJLUxYavd3Joxc0O6N6qref-P56HcDu4d7SPr8TBR1xOUSs2mYX-6lqY7sE4h_dhGBysx5YaqEvdbzBUx4HU9ouqwok0MAk6AaBtG4Qt7JWY_dOuheMZw9fIPQE01glRWCIBFscPTwRWvailv1ZhGVacJlUajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNBw4JKWh86Svr7j8pGH-v9uvsZuGTZNjYmXzTqX80d60kUGh3P4ukGhTfbur-tp_IcjKhpkVo5TGWMpp62mdQ5Sq9ELwDFeXrpyOAXUrzZWm7WRAmsv7Qd0uGkrjvmeTruanwdLSY61Ad7PQgguqA1A84z5jz4bmw8fFymIVXzpOBxoqUsKkIPNC5ISZoJfCP_MQovDqIjVg6vaAVF96OovbwMM6b9PnBEOLJfspZLB72Y7PpVb9Di21pg7-161HNr5UIEfpjMXeHXju8pR6CAVmfsqsBkH-QCQU0aIwyEnTQ9wwFp2t7-h-2BZ92TP8yHgkaoMOMxiBf7sFsN1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIein42hI3Qkc7arh9cpfOZ3z7wabXXMUuT_IM3ZFAqwVNHVp80V_m8O3v7-MP-Ipzlz6MXvXE20PnHkliXU3cKMoDVln8iBkxUakXK616tjK3u2zBOS_nNk2KNZFhQW1TjIlL7FUzdjPUhfpqTXTdaCiv1uMvTEwQRdglBBXgUGY6695FIBMxXZBIQTdc1GD0zzupeZm9XyBX04klBWMJiaDuqCYXjVEZfjURVc8ZWzYVSWEWzzKsZY-g-amTPek7dk8IeffqyvvmH5LlKCoEO8tHje9pJGIeRwzyWS0Tf5fSR5QSpmmnw84pTphn6hXAxmeYiCBMjNWiarKw-Ddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr1insrn01nB7Tjn6pbSaZD_BVYubSLb7MQuOls3JEEwEd8RL0Mk5USutmKOASJsSxr0WP_M27fT1YrTM35yJ0hRsDWgA2of8LfW5S7sxdqkDXYhpoNB8ERVqPRsRSHuqwvhuUZCDlOKeR_AdjIXXri3koHQmyP3lv3gIkXZCrSx7XanUOAYkXDnzi3s2cDurbEAQ81YaHpdMIVQB5FQEDj1rpATRh-Hb8mtMClCzHE__56Sqklbtqbw02g8Gwu2GWclumXsb5MjQkF3ifG4VkUHdXVR9RselkWfNI-myi14GDhfoXTCecWdBszSuBIz-DzmcJFy4Vp4HawGfkl0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=CGsvMESuQCg_yDdemtMUmg1fH5j91sJhnEgZ-2E1PngYoarl0N-agX8klDdjJEMn4oi3JSDKxEf2yYIrT0NAMz1k0VnlXytmxDqT1FWzVMwow43rZdcP57cT1_GgfYmORsuBdF9LyFW4Sl_aL76t_YIOLbgmMBHSiKwTFzsVf3rdg4UtyvFSQ7r6HFv-fUJxafSJ9el6LsBX66uebyr_hEDcseBfFuDOeu6kxwTz3_rA8_DojcwjscA0HFYWxF-12mGq8_ZCYZzXXoD7cCQKWVfHLLErArweaAtbuQ2LSvSkVYNBLse4voBkiAAnYMSEqrjbbzqkJqQbuKbZH1ele0K0cCUazKLYyrXZ3AXuz965btW4S39fLhS2T54BRuO1wvY8p-Oy8Ba_5hCirEZEpuBEyjTKMf082UhuTGXa3didUx3SyGvWSPPe7MbqHXP4SZ1518cL6levxZqjEyxYQ0DFAy8xS1O3djOwVEmJOSEgZ417MPV6mtf5XBCYTH43zJHpa70835FNY2lyTHLq-3AppuO1dzeQIaEsWH5IwiXVl3swxXVDJXQqarTvdyjCiHXEPbmfLWEmQl_Ne97piUDZgreBMlfQo-O6I4r-vDiDrC-vMobUxAnNGvVyZyTUbVMZoTKFObveMSxYcVgPR77QXlt_aguCK8DwYQAgjnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=CGsvMESuQCg_yDdemtMUmg1fH5j91sJhnEgZ-2E1PngYoarl0N-agX8klDdjJEMn4oi3JSDKxEf2yYIrT0NAMz1k0VnlXytmxDqT1FWzVMwow43rZdcP57cT1_GgfYmORsuBdF9LyFW4Sl_aL76t_YIOLbgmMBHSiKwTFzsVf3rdg4UtyvFSQ7r6HFv-fUJxafSJ9el6LsBX66uebyr_hEDcseBfFuDOeu6kxwTz3_rA8_DojcwjscA0HFYWxF-12mGq8_ZCYZzXXoD7cCQKWVfHLLErArweaAtbuQ2LSvSkVYNBLse4voBkiAAnYMSEqrjbbzqkJqQbuKbZH1ele0K0cCUazKLYyrXZ3AXuz965btW4S39fLhS2T54BRuO1wvY8p-Oy8Ba_5hCirEZEpuBEyjTKMf082UhuTGXa3didUx3SyGvWSPPe7MbqHXP4SZ1518cL6levxZqjEyxYQ0DFAy8xS1O3djOwVEmJOSEgZ417MPV6mtf5XBCYTH43zJHpa70835FNY2lyTHLq-3AppuO1dzeQIaEsWH5IwiXVl3swxXVDJXQqarTvdyjCiHXEPbmfLWEmQl_Ne97piUDZgreBMlfQo-O6I4r-vDiDrC-vMobUxAnNGvVyZyTUbVMZoTKFObveMSxYcVgPR77QXlt_aguCK8DwYQAgjnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcYZ5dfqRWZAZhb0b_XrEgRb0-4ca31L7RM9f8dEKmhj7IbLWQEOywr7FY8xo08-urtkHXndu4HfmulnMlaDLTgttgarvSOZKPcp_4xM7US_ZSyl3gisbJp-JIPTgVf5OfhlAECYDt5pdqnvOD1iMKSNCShQtfG2j9e9QhxEqtE4SjTEdgNtOXr37btv7kKXFbUxZJ87QhHX97CzSNaaXIHdgqfubEYgfPLHLxYVkf_1vqtCosN_ddpt-SVAkwEoE_m0XZk6Xommjqbs8NWy-hp3l_oZWFTNdFEJbvt6uCz_XaZdSflOLrx8_TegbU-ofjwra84qw4KGID_aS6qB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=vhP5SrBl4qdn2ExhTCOp9WAkYLqBlYIK8Kuul_ULeFUla7HiYPV-ynFllHLVT07TSdTJE2rDSPWBFEW4FZ5dVpqFvxExSN3hzf7PYzclQL9_rGI0AFlAXFZlmm6q8Rfthg3P1ti8i4sl0W6I4Br23TboGINqgtENdEWjqt1HGkjvk15ZZyA_u_VC_rk_0ejopH8-wSEMW_5hJQ_83HcplRayHZIbqfwpsWqv5L8ZqD1lE1QEmZb9t6ruFDmwyovPhxMvmK6xKMcJM2Dj78ukoRfEec6xjtdkfOJ3-SMxJjsjQ0gcmen4QYBusneeYTxbRw4m1FoWMPh94o3SUNjwYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=vhP5SrBl4qdn2ExhTCOp9WAkYLqBlYIK8Kuul_ULeFUla7HiYPV-ynFllHLVT07TSdTJE2rDSPWBFEW4FZ5dVpqFvxExSN3hzf7PYzclQL9_rGI0AFlAXFZlmm6q8Rfthg3P1ti8i4sl0W6I4Br23TboGINqgtENdEWjqt1HGkjvk15ZZyA_u_VC_rk_0ejopH8-wSEMW_5hJQ_83HcplRayHZIbqfwpsWqv5L8ZqD1lE1QEmZb9t6ruFDmwyovPhxMvmK6xKMcJM2Dj78ukoRfEec6xjtdkfOJ3-SMxJjsjQ0gcmen4QYBusneeYTxbRw4m1FoWMPh94o3SUNjwYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Iz61Du_T_7rwpmCa-LwXK0ntGhlC8S_kyJp78-NYSSP9CaztVGGS_JWOA8AmYWRsb6Zbllf9EKC6KZs5648GGOedXGrHNTfrPVzHbUW7Q2FA-KekBs1B9ZqrlAV6-m8UxhCJDEMhcQTJX3UcdhboBSxtgXla7GmAegmD4_kGbXXAu57CCZ2_8Vrbmg24B6RCVsFA_u9SUADZT-eAKDU4AQM31Ruw5ZzF3-GcOGl-KPe1OH0iMrEZqSWsIHR-CP7_L73b7DexX-m6LKO8d43itN5kgeFvn-j9h6n2bDhrmlBWgL8yMJ_mzAx1TbTadnxWljnFm-4z8rUveyboNOMz7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Iz61Du_T_7rwpmCa-LwXK0ntGhlC8S_kyJp78-NYSSP9CaztVGGS_JWOA8AmYWRsb6Zbllf9EKC6KZs5648GGOedXGrHNTfrPVzHbUW7Q2FA-KekBs1B9ZqrlAV6-m8UxhCJDEMhcQTJX3UcdhboBSxtgXla7GmAegmD4_kGbXXAu57CCZ2_8Vrbmg24B6RCVsFA_u9SUADZT-eAKDU4AQM31Ruw5ZzF3-GcOGl-KPe1OH0iMrEZqSWsIHR-CP7_L73b7DexX-m6LKO8d43itN5kgeFvn-j9h6n2bDhrmlBWgL8yMJ_mzAx1TbTadnxWljnFm-4z8rUveyboNOMz7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=V6qzBAdt6ecJw8zkbDZWMF5DFKtDHFtv3uRAAjzLW7MKpNNIPIJkGyEkAclhMimdvwPhAQIOlQ39WFy_0aeuQESD5gH2QUV5yx5N_B1SAZtpvmptUR07tQGxSuIM3jDsGTLYDd6YATxVZFiya9zA4zxc81LrUz4D86MUzn_aqMiAPXkJW_PJJrHWoWz-KGt-45R0i3BQxZjVF_m3wb_P7DFUnBmz4iKaMmLC0TuIhYQKyrcyxvyLGtHXZWCj23G1NFxPe2lJ4t3tCOG1wRJ-mCbXYedL7zEuzqHRrLGNtwzyINgaSOlGR6dW_fDYC7l9PYyyYVHIawndRFk5QUJ1HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=V6qzBAdt6ecJw8zkbDZWMF5DFKtDHFtv3uRAAjzLW7MKpNNIPIJkGyEkAclhMimdvwPhAQIOlQ39WFy_0aeuQESD5gH2QUV5yx5N_B1SAZtpvmptUR07tQGxSuIM3jDsGTLYDd6YATxVZFiya9zA4zxc81LrUz4D86MUzn_aqMiAPXkJW_PJJrHWoWz-KGt-45R0i3BQxZjVF_m3wb_P7DFUnBmz4iKaMmLC0TuIhYQKyrcyxvyLGtHXZWCj23G1NFxPe2lJ4t3tCOG1wRJ-mCbXYedL7zEuzqHRrLGNtwzyINgaSOlGR6dW_fDYC7l9PYyyYVHIawndRFk5QUJ1HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
