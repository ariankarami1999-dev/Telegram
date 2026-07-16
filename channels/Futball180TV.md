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
<img src="https://cdn5.telesco.pe/file/i5kruk9pXJTOKeHAEy3brOdrH8Ko6UcvZYbY0nh2Xe4PZM17ji6NGz-NGR16jvEwAF2qFqK9fxkuYy7gFHjlN23TPdwdXckqFB-kMsl4yIZqlzuo1tn32cApPLsUK4jyCMM96UxQycpHOtmV0CI0EWHIo6ksNrfL7jrqLWgaFvuSTx0O8vqOka9bw4hB58HIKsknftNO3ph-T-rtDPzvoouKgi4gAlEoouX61kmXm-K07uZy6YBXK2CG-gKRdgOjzrMbm9Gp3J3Az1wXvafUkoUouBpJk8yaAv4U-K8N-jVy_lwD7A20K5ppOsjkX1uM-62FzTR3sPDp7i0A9VAp2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 571K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 14:20:03</div>
<hr>

<div class="tg-post" id="msg-100483">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فریادهای رومرو بر سر بلینگهام بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/Futball180TV/100483" target="_blank">📅 14:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100482">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنچه در بازی دیشب اتفاق افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/100482" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100481">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-I5MCyBozQRxvYuknNE-ct5ewx027CXlmiyiNvclzLco43GyAa2LvJZKPeAygOG4Y4OaeaJfmxcwUFoBADEHTVjlIijp5DqWLj5dLr7JzSJMfYk8Cuu6hVQyZiYTXmAJdRSQY-u1c2_YwS5aWB6HZqxWmLSMZaRUPhC-UJT_svUePUf8Jb-QUG1wIqVHXueVfLvsEOZbti8oMEvfBFvqXau9iB4WF3DiP2xMgi3PZ6Fw3i0n6uUwfioqkUkH-kgx7N9zV-F-pLDPt5rwt8wWkUYD7Y5tqq4SURu0TmE_sRhuPPgsbIVDrEhIpiuT7vMKfL6vqhRWdRDRE2mw3OZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محمد مهدی زارع، مدافع میانی ۲۳ ساله احمدگروژنی روسیه، با قراردادی چهار ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/100481" target="_blank">📅 14:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100480">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇦🇷
سوپرگل انزو فرناندز مقابل انگلیس از از نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/100480" target="_blank">📅 13:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100479">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=t_IMJlK5t6ZGQi9n7drXvYdURA4MgcAO4Kif7T4DR2Wi8AIVE7ad_P-vvEVYy3uViFGmIkDwzzJUALoDq0aBSgrMnX2l4Fg0kh-1tt2XhttdwiniaNivlYyJCs3G3xNR_ek0adKGXCuc-1jfxIvAzW22iUJXIv-sS5Ydpg4l5j2St9QvgQizWpmlYoxFlvja7ir9FtJNoWDpFkot4pTE-kAXkiLiLm90ahN7EDO2OMpdwHA8Uj1XfibZLowOLrq1enCaDCXF8kY-40PWcAwH1ejdtsm2_UIASnXczHFXYVKSZeNbs9P0MMKB3YVtTw_w89BU1I4vmpT2_ze_MF-N6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=t_IMJlK5t6ZGQi9n7drXvYdURA4MgcAO4Kif7T4DR2Wi8AIVE7ad_P-vvEVYy3uViFGmIkDwzzJUALoDq0aBSgrMnX2l4Fg0kh-1tt2XhttdwiniaNivlYyJCs3G3xNR_ek0adKGXCuc-1jfxIvAzW22iUJXIv-sS5Ydpg4l5j2St9QvgQizWpmlYoxFlvja7ir9FtJNoWDpFkot4pTE-kAXkiLiLm90ahN7EDO2OMpdwHA8Uj1XfibZLowOLrq1enCaDCXF8kY-40PWcAwH1ejdtsm2_UIASnXczHFXYVKSZeNbs9P0MMKB3YVtTw_w89BU1I4vmpT2_ze_MF-N6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب تیم‌ملی آرژانتین
🔥
👀
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/100479" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100478">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کریستین رومرو: امیدوارم وقتی بازنشسته میشوم مثل گری نویل احمق نباشم و از بازیکنان انتقاد نکنم
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/100478" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100477">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U54Dih8fr03Yj8tRyiczh56x1n9Uw4jfhCch4JjFZrnAR8lBD4FWEMUqyvAkHHcWxJybbGA5ncBXfLkubF6gn9jSuOdmtFvX3j3JVTufQKkduo-GDSFoLILBcuYaCQMpbZPhwBBZRvPC74g2UzF46_MqXjkTsIQj7vcytl5L2jr6nLeR9_lrN8KLdDPC2N_4FJtWsnRu3EavuM7kx7H-798Fd_0KHlQlYf7DdTo0Ke6-ShMXfYpbgNGqNNt6odB25GyZWXVdEVXss3mAVeyJTPEb8Sfn_NcyHhJWY9Cy0QH8q9GL1QO7YsF7vtIPYPrUe7StMDVXSxY9fqHS7hxteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دو سال پیش در چنین روزی کیلیان امباپه به عنوان بازیکن جدید رئال مادرید معرفی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/100477" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100476">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3896b54423.mp4?token=Hcb9kKkZagFJ0mHmFumVztLPuuWp5fvtdm_XZ2MQEixvJ1K50xba6_DksP5meKacNIkQMFuSxUyRE-4OqeR5BBl7bxFCMXuGA6shkvNEe2aCtrN5TtQiHHGROLjBH5_7oPsq3Td0Qz4LGDVhS2Bx3v5gOPx4L7DD0sVtSeCfi1HnJ-EVesnV6CgMi8rshtlo8R2WMpAfOhjon3zdo0XjqctvJz4U72-DTf-s5xX6BWTB4HZSd1s4jr_6-LH0U5nozns1TK5avMySX8RlyeFJPFCsL8S2jtEjuVrZZAhfcSbD0A160Bkyz-Zpew3cRLjV1BZSWBu7xzfmiPifU4rn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3896b54423.mp4?token=Hcb9kKkZagFJ0mHmFumVztLPuuWp5fvtdm_XZ2MQEixvJ1K50xba6_DksP5meKacNIkQMFuSxUyRE-4OqeR5BBl7bxFCMXuGA6shkvNEe2aCtrN5TtQiHHGROLjBH5_7oPsq3Td0Qz4LGDVhS2Bx3v5gOPx4L7DD0sVtSeCfi1HnJ-EVesnV6CgMi8rshtlo8R2WMpAfOhjon3zdo0XjqctvJz4U72-DTf-s5xX6BWTB4HZSd1s4jr_6-LH0U5nozns1TK5avMySX8RlyeFJPFCsL8S2jtEjuVrZZAhfcSbD0A160Bkyz-Zpew3cRLjV1BZSWBu7xzfmiPifU4rn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
توصیف عادل فردوسی‌پور از کامبک آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/100476" target="_blank">📅 13:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100475">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876233c65c.mp4?token=ZK34Dfx2U9QKLolPyJ6107n1WrTxHDJsOQW_pe9aJdssUR0C9StrSncCeZeM_8W64A5RMHFXGreOpl2WG891Q1c-F6pu0sec9o3xWpIpEtS9mx9zdC0I34p_Mr9qD8KmgLrGZFf1pcap5eJBPJVDGJIPip-MHu6EciH0qZmGTcmY4DIzplT0Lj7Aj2j2Bt0FMmhSxeIT_y80i4u1LGWU_dfNu9kyHL8oLPxWG1Z87ojojzHX4pBZHjc0epLD1oYM3CvGoT0q1L-xXTxgRVDOWTLm9kBnkTi0Svt5Q-2xkXx-WRNIM464pW8FP9DWvr-DQPaKLUZfB_uyWUcCC4axsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876233c65c.mp4?token=ZK34Dfx2U9QKLolPyJ6107n1WrTxHDJsOQW_pe9aJdssUR0C9StrSncCeZeM_8W64A5RMHFXGreOpl2WG891Q1c-F6pu0sec9o3xWpIpEtS9mx9zdC0I34p_Mr9qD8KmgLrGZFf1pcap5eJBPJVDGJIPip-MHu6EciH0qZmGTcmY4DIzplT0Lj7Aj2j2Bt0FMmhSxeIT_y80i4u1LGWU_dfNu9kyHL8oLPxWG1Z87ojojzHX4pBZHjc0epLD1oYM3CvGoT0q1L-xXTxgRVDOWTLm9kBnkTi0Svt5Q-2xkXx-WRNIM464pW8FP9DWvr-DQPaKLUZfB_uyWUcCC4axsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
گل‌دوم آرژانتینی‌ها از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/100475" target="_blank">📅 12:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100474">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=XsYICfvdLvb8HE_8peHGArurZsUZzKou-VtJPj0d0TWq1xyPk2lmh95BiOgI3Cfthc-5lqH-C79oWSFIu5nHuG51-n5gReEfYgmb4f_0hyAO8FM-aKvmoyOSaGXvV10rlhPO563hevqTv535KkxiiVE12qkXNbKqVyosecwkBlsIHq0IrxRvuYYD-Vf3RUDo4q-nzRvqffgDs0CCN8vI7zc_g1JRWTkTk7IoQpjV4KLxS7oNKkmMtkNpNORmXZl_pNj65tQlw6rckBr5LAFEyFgNDO-t-yZR2WMyJBLw_J4pzslQikUSp47EkSNmo8y18rgqI2qw0yqKofAjjbrskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=XsYICfvdLvb8HE_8peHGArurZsUZzKou-VtJPj0d0TWq1xyPk2lmh95BiOgI3Cfthc-5lqH-C79oWSFIu5nHuG51-n5gReEfYgmb4f_0hyAO8FM-aKvmoyOSaGXvV10rlhPO563hevqTv535KkxiiVE12qkXNbKqVyosecwkBlsIHq0IrxRvuYYD-Vf3RUDo4q-nzRvqffgDs0CCN8vI7zc_g1JRWTkTk7IoQpjV4KLxS7oNKkmMtkNpNORmXZl_pNj65tQlw6rckBr5LAFEyFgNDO-t-yZR2WMyJBLw_J4pzslQikUSp47EkSNmo8y18rgqI2qw0yqKofAjjbrskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
پست جالب باشگاه اینتر برای لائوتارو
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100474" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100473">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M63EL4ssOxM9XwjFfl3wP4V76LNz9EaQV901tuyVeQWEBW-Vj2UCxsCBXfWVeSkJQWrzs8chFurhRQi9bvykMGRRB54M7HFLGKn2q03xipP7bQOqc1FYaSzuzCppAl2U3MQq2Y820VDGTlTEoTGPH14lsHun_VeXfP_iqUjtE9XuKOnMbxQ5q10TScUSJYi3bIYRlR1uGsPWKzKrT11D0QYIj3mFopPCgH4r1BBu0FAMWikfkN8RQsOwldmZFXY_7_xNvUhWwjqliZh1u8vjqCwtK5c5OO4fRmP59XsC1WaETcI8M_xSNsiOGuMkT3bZSFj0iY3x0QGDp-0_77MENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب نیمه‌نهایی جام‌جهانی؛ خط دفاع کاملا اسپانیایی و حمله آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100473" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4QbAhNQTNzD4BYDpcS9K9BF7hOwVdOoMDsZ7iUJRAg-G7mUjdQRVR96X8DQD-yFAwc_Ntqt2nqWqjIfeDwJa7U8iJmakal8Eb3C5JqXj5O-fZWgTeXQPGlEhFeLm4ghqwoyFUqaySfKZdM_Pzlj9eciJupOLCIUC8qUahUof55tNlrFu1yvcpN22TKb9GklF6jAS7BukPg6wPHD56Cl3bv3m3xiknnSozwvtCqIcKBwaYjvDM7GlF8RoBLxWC6lRc4qg0tV--Qg3b-_Pti3DuAyz7dtckVziKmXOP73CktxzPW0RaLIxEjU0LN7QFB4AFOETyywzQPpeQd0wnUczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYaIKm8E5-Gj4vgEw1bX46IZTA5GoHpd24Vi2f4fjC0X_qxHA4yTKFrVh3VXE0mfcOnnDJTGhZgtf_j8fPSmuUuf9PTm69SWhBEsTNH28Obb1j2i-gcsuvtd61kjx1OE3l6SMg1mBU_WrXxxstRxP5bmxq4ITa_Ctiw8_zfqk1RjP1nwY-5Iz_9E-N4KUTG0orVTw04wrQcywoQ-TD6U32JpDObbv-2beOda4M8Uh0U56Cqd9f8XJ7mFS_cT0gTR6mXxLlxY4wRI7WQ21Xto8NIII8fN1VB-f4G28AUnvESNua0alXV0kIfs1LCZtLfX2bT27VXNcUUKSuxGMK4gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUt3LGRUuEUK_jsg-33v8CRFUTUA68HGFLLFBZOT4q0Qh5pej5iTS6co8p4LzAWjXDv6A8MwwJ1XIHZ9wOLGMN_hB2Y1dbhVKu_8olt_bmUoxla5Gj0ZIXNYCLCMP7bplKgX5ztHHXYd9QdQHATdtphWpUMNgDE23TtNynAk7SfuTSDPydzie7LBuX7LUh6JGcGepO0o0Fn0bGk6jcBGwisdrnS30DiOyAwp2gFzPjCDyQzcfsSSDciErQQd14mP53PwUr1teYqunA30HJcXi6CH8Hui9CnB9hwZbv9gkm8C0sU1lKnu0EJt7Rm2q6a71izwk43DtSUetwXyHETtEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
📊
مقایسه قدی سه‌بازیکن مدافع انگلیس در دقایق پایانی بازی‌دیشب با لائوتارو مارتینز که نشون میده قد دراز همیشه ملاک موفقیت در نبرد هوایی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100470" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DoIZj75agkj7Ap5qJp2Og7DShaYMODqTUsDfHbaYIJnQEqhbjGpaR-4kIwA-lMGOtTKiblvOkNw8opPKp0Y2cZjCL7GSL1I4jfyTn0qW9HfH2FdsLsfF-FPihPHD2l5bDTzAoOA5dtQ6ADNpi-ACT0r3Od3du2Rv5OHS4ClO66xCzBcT8o3fvY1a-9LonDPFnQ2aRDMoLmCOcMvUc1iafFzLr1ugDEEApkEWMcgK-dvVZMlKAmRiGkUmiTIijn0rPR6e0NOs7v_12OIn--xXv4gmjyxFXrdgDzpPaNlPOO3xlz5fLmFWWP8iiAmUMtofbnqfsPYx24VZSRePIvFqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uG4M42J0R5rE1GTnW935sHW1OGlutr27R96V4G0z8v8MYdxWwUDv_POdnqIhaDIGrVsg568fMr1yhipoOkWrpdMrsIxotJg8stfqP4cqcRhMyrak_uDzXEJNxa5zX7XGGTKJvO2SXg5Hbhv6GODMFll4djt5hBWhwbjihC9e7Fya79Hpdsjn8n0c8TZs6xE5t06Qoan3ljtntP0qTaZU_AByn79uMMVQXn1iMKYv__WnM9-2MVU5O6R1VbS8fyhZ1h8fuzHLYOWmJDzuA2Djjcyg37OEEgb3nXzNQA2-TSv3jb4001SxkH9rZxhhIehsBAceLrIvnk13YJ3kpsFBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTUkSiKxfLI58-m3FjL5XdoB-gbPnztuSprG9OxoVoA2w9_PdDa1v_GZqd4uZCv8NBjwBLgcWKwKGDzfJOl_PR1sL85_CRjNcchyz0Mbe6E_5sLbptrHx7kVE-Soa-nOAmMPBM1Sp3ogpLPcF6U3kf0_EM0CgB8q8lB-gC3M08ZWHF0Q5AdRdYSizbn6yedFMCAf35g4cjFMkBrg38j_GMINrGLtAYvaRlz-IwMf-r6w6eu1rFt52oVejH83cLOccaebEwJQQRb5CxS85SmmmL1NMs_I7TDSvGpAsF-1lMqCWbY9skcrGzgBcgINyjXLjrG6H9LCwDRu7vCdhTnlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHXczvbUgH3i35Qy8PN9dpgoHEfFrontLjefBYxKfM2bsRDifpI0rUZRv6WA_3QzqqZkzS7h-pBCKG4c2secwuebmUgxF9Erx9c7W_QH1Cyvzxp5zYuJZArq--X-9is-wDd8TlY-VKRGwUPZpQnXeE_Yuvy8XS7Ckg3-I748Ye3Gd47SXP5lcmvMr9vdysaR1lO6LGIlpPh5e3L-S83JTwEAPyQEV1wSSMkkPWAvKqQJG95IxM_D09gudTbZ9e9RKSqdsHs5gbiBSCIbZRBplhmN3MDNYMhRdUGECbDKWX15Imo3GAa1EfCkQDpfe9JEtJSvMNXW3IaVL2HKuNBwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLnaHyH3lp2vGALezLt3p-5TtKIGP4mlSNc8k1vI5VyvSdKz8t00J0ByNOuD6WI1PZjMzPJqAp5w-uQXwJsekLQTSm6NkWwHPJcCXy1BCKg9DgsIU8DFD1Gz-lSM-8WH-S4Xylf87I_qt6F7OR0dAEx6pB-CB50grjfjlT-zdc8KOv5YAHTCiAy1B0uxm7siYFpvhXE0gGTa2TB45NPWwckbLXyG-NSyr-nBWA_QnpQC3Z6c6A40N_2IoM2RAGcNkfef58Y5StBerlvhxzmCxsMMWq1cLQ5MY0HmWUfOSG-9QZb_bKYWrQb4qzVhoqdj71G9vu3aqScaHFa9fRlSRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🙂
اگه یه روزی بعد دیدن این عکسا میگفتیم مسی قراره با همین بچهاا فینال جام‌جهانی بازی کنه بهمون میگفتن کسخل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100465" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=ECkfQd84b7Qy4tTTYb2UQH9FKXPg3Pk2zLi71KCuUZxGUOQ3Mi6Obi-R0GGv0QlmVgFNbBzDpxlMSGeVLMJjOdCzhzifVy4DtdQaasIWEBaBzR77aLcjgX43a9pxNtN1J5AqkOppX9-lPbuUjFEbUmeGwZ3WycOGEozUeMMBGYRGaq05zackAYt5aatvmIm8A1MQinE2r15zZkUpZ0X7epLIfPHI8yC-gYFniIDRCdeNl05dzTcC2G3C9pA8goy-nZ-UAUXha4aZ-g59Ix9PhQzu62y3GsYFmjwjY14it2BcOMsGIeElbE0XdrLLEfvQtURtHwXwyCltoQ-VUd-NmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=ECkfQd84b7Qy4tTTYb2UQH9FKXPg3Pk2zLi71KCuUZxGUOQ3Mi6Obi-R0GGv0QlmVgFNbBzDpxlMSGeVLMJjOdCzhzifVy4DtdQaasIWEBaBzR77aLcjgX43a9pxNtN1J5AqkOppX9-lPbuUjFEbUmeGwZ3WycOGEozUeMMBGYRGaq05zackAYt5aatvmIm8A1MQinE2r15zZkUpZ0X7epLIfPHI8yC-gYFniIDRCdeNl05dzTcC2G3C9pA8goy-nZ-UAUXha4aZ-g59Ix9PhQzu62y3GsYFmjwjY14it2BcOMsGIeElbE0XdrLLEfvQtURtHwXwyCltoQ-VUd-NmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه‌های فیروز کریمی به قلعه‌نویی: تا الان سه تا تیم تو جام‌جهانی نباختن که دوتاشون فینالیست شدن و یکیش ایران بود. این برای ما افتخار بزرگیه و باید جشن بگیریم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100464" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=NYTMbZoa6l5sf0P3FGpajUqFSTfOqe-vzbuuumVWY-FaIy5pv_B4HXq3msaTHDgK4JoogBFvOAyfsISevZ5Y4Q3qSlF65-GD-0vVLLcE_CNu3d4fPuAsK2wVWeaPUXq0taE9Pc4V3jsHD6h8kSEcIBlPkNqF8bL4ZbT2T7XTgH0DlGdHftbuhQZ7esPE2qHeafPa_8T2veAujKI8pDVon-vYJz9hnz2RCo2IvysjYxpJrUkUpcQy0Q-ywMtlFe9dwdZDm6OgYsCyjryTrzZynIlHoKH76mBJVVTaYTaeOcFDhJL0pvR7C1ER62iBWgDZu4hdyaVHNZB4TmeAXUo5jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=NYTMbZoa6l5sf0P3FGpajUqFSTfOqe-vzbuuumVWY-FaIy5pv_B4HXq3msaTHDgK4JoogBFvOAyfsISevZ5Y4Q3qSlF65-GD-0vVLLcE_CNu3d4fPuAsK2wVWeaPUXq0taE9Pc4V3jsHD6h8kSEcIBlPkNqF8bL4ZbT2T7XTgH0DlGdHftbuhQZ7esPE2qHeafPa_8T2veAujKI8pDVon-vYJz9hnz2RCo2IvysjYxpJrUkUpcQy0Q-ywMtlFe9dwdZDm6OgYsCyjryTrzZynIlHoKH76mBJVVTaYTaeOcFDhJL0pvR7C1ER62iBWgDZu4hdyaVHNZB4TmeAXUo5jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
😍
بغض و اشک‌های جولیانو سیمئونه‌ وقتی دیشب راجب لیونل‌مسی صحبت می‌کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100463" target="_blank">📅 11:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=nYvlNq8nyNmcxS8DdLAlow2-FrjCA2iVjbbCwTh0rndo4Epuel3_v3pZpxEhDV9NBc9K5HDCR_-DhFJxdBY9GOMOZ9KYoGrOoTWaPWuX8hUzHiX25B9PBSK-2c59LeHhGRcTtLyUdDGeoHloern08Eo1eIOMoEuGYFhHnDwnwyyV3OzjKyUFQgiIyAUnabO31TTOvGyqEmVz148O_QdlbQJCKisMvLYChR4OicibfMVTlvpzLrhDC4y21bdWZPYY6iKMC3rZ4fYNFffKo4yJkF8U2Jd97PJAoPgTVH5jVFOrF2y_L9myzECBADQmWa53JV8sdiDwoRxYQueEzFP3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=nYvlNq8nyNmcxS8DdLAlow2-FrjCA2iVjbbCwTh0rndo4Epuel3_v3pZpxEhDV9NBc9K5HDCR_-DhFJxdBY9GOMOZ9KYoGrOoTWaPWuX8hUzHiX25B9PBSK-2c59LeHhGRcTtLyUdDGeoHloern08Eo1eIOMoEuGYFhHnDwnwyyV3OzjKyUFQgiIyAUnabO31TTOvGyqEmVz148O_QdlbQJCKisMvLYChR4OicibfMVTlvpzLrhDC4y21bdWZPYY6iKMC3rZ4fYNFffKo4yJkF8U2Jd97PJAoPgTVH5jVFOrF2y_L9myzECBADQmWa53JV8sdiDwoRxYQueEzFP3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
لیونل اسکالونی در تمجید از مسی: "اون دیگه چیکار باید می‌کرد تا ثابت کنه بهترین فوتبالیست تاریخه؟ واقعاً دیگه هیچ شک و تردیدی وجود نداره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100462" target="_blank">📅 11:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=PevvDllHXZS6JuJglpCgveEaNltgFN_SAP9Rdk63Rdee4gn5qO9Fkr1qAYtwxrLMbKQfFruuHY5lXAHU2Tflu8aRlpBcZKr4Lr1xskVIveRjArF-9Dvvqb1nFJ1u5bLFA_vMKzhFxgLy7JgREN8J6y8qZ7ITiF5ZqOQXLzIyblgwgz61R41NVaohJE7ZyXsWuEkbBnxwO7HeUQiRqsxLbkwhFOgch8YP8XQOpJKlIoc7WsvpZkERGliU3wh2i_z28FEa_fkmPw572soeePnWinNI8Z0Z8xBU6b2YohKgrFhbLe10oPfYm2HsYXSltzGJbPC22KjtObkOFK4Hsa8YRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=PevvDllHXZS6JuJglpCgveEaNltgFN_SAP9Rdk63Rdee4gn5qO9Fkr1qAYtwxrLMbKQfFruuHY5lXAHU2Tflu8aRlpBcZKr4Lr1xskVIveRjArF-9Dvvqb1nFJ1u5bLFA_vMKzhFxgLy7JgREN8J6y8qZ7ITiF5ZqOQXLzIyblgwgz61R41NVaohJE7ZyXsWuEkbBnxwO7HeUQiRqsxLbkwhFOgch8YP8XQOpJKlIoc7WsvpZkERGliU3wh2i_z28FEa_fkmPw572soeePnWinNI8Z0Z8xBU6b2YohKgrFhbLe10oPfYm2HsYXSltzGJbPC22KjtObkOFK4Hsa8YRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
بطری تقلب پیکفورد که دیشب دست بازیکنای آرژانتین افتاد و حسابی سوژه خنده شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100461" target="_blank">📅 11:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔥
🇦🇷
جو فوق‌العاده رختکن آرژانتین که نشون میده با نهایت اتحاد و شایستگی فینالیست شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100460" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
‼️
⚠️
زد و خورد طرفداران انگلیس و آرژانتین بعد از بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100459" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=Xu0VSQ1vjVoSF8Gn0TRu21c99oOxLj3ShohHTAxSPDd4mGX-FkfTKJA4vnsCHV5w-W9RMopC-Pc13pSyl2Cn9ZCuUnOzGAWJheb3V5g-8nK5P4ik5surmKoCTD6FS4hndFMmfDz6cFp7PYNNQcZJNUQezDmtgpYRmnp1HObthbqnburJcEIIu0ANHlAQ6Nbfft_D3N_TwSZdkeRxsAh_z68xqOPMV1q4I3FYoMl5WEscRBAQurEllxyrY-FLUSeDTgK72BJGpAiuzErnJNvGI2LUuQS0i8Uhx82dxK37jQqQPc8mj7iPWa80Lu3yYq4z14uH6_aR7y0NzofeQtnmLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=Xu0VSQ1vjVoSF8Gn0TRu21c99oOxLj3ShohHTAxSPDd4mGX-FkfTKJA4vnsCHV5w-W9RMopC-Pc13pSyl2Cn9ZCuUnOzGAWJheb3V5g-8nK5P4ik5surmKoCTD6FS4hndFMmfDz6cFp7PYNNQcZJNUQezDmtgpYRmnp1HObthbqnburJcEIIu0ANHlAQ6Nbfft_D3N_TwSZdkeRxsAh_z68xqOPMV1q4I3FYoMl5WEscRBAQurEllxyrY-FLUSeDTgK72BJGpAiuzErnJNvGI2LUuQS0i8Uhx82dxK37jQqQPc8mj7iPWa80Lu3yYq4z14uH6_aR7y0NzofeQtnmLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
۲۰ سال و ۶ جام‌جهانی و افتخارآفرینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100458" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=JU5HpWqSQG3RQkXU30anpv4GTUWn06Wn7ZIm9-1RsWEQAy6yucnoE0K7zrighfAuYngO1xw_qCeA1AoaVOscMRJaRqtYs9n7DIHQY9V37Ko-whaoXeL_FBAU63NepL5Sn6re51vX0Md2q_4AyV7CooGwHwHRO0b7u_NunxJ_A13XsiKGlwLLidVqGaROkhinIUR98woVDIXijfWZsWHL7gy5S9i_ccO9cv2ryQoPq8D834_dfx13HipXrleyaakjnDmXrxjXMCa73dsf-3hyaRFgNsDVQocmZDY60WrMayse4w8XAGzumuQDLPbkILL2cyFQ5Yh4Tn-9GcJxuEI1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=JU5HpWqSQG3RQkXU30anpv4GTUWn06Wn7ZIm9-1RsWEQAy6yucnoE0K7zrighfAuYngO1xw_qCeA1AoaVOscMRJaRqtYs9n7DIHQY9V37Ko-whaoXeL_FBAU63NepL5Sn6re51vX0Md2q_4AyV7CooGwHwHRO0b7u_NunxJ_A13XsiKGlwLLidVqGaROkhinIUR98woVDIXijfWZsWHL7gy5S9i_ccO9cv2ryQoPq8D834_dfx13HipXrleyaakjnDmXrxjXMCa73dsf-3hyaRFgNsDVQocmZDY60WrMayse4w8XAGzumuQDLPbkILL2cyFQ5Yh4Tn-9GcJxuEI1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
پشمام از مردم آرژانتین بعد گل لائوتارو
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100457" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-Rub5fXMu3AirHI99xH2XAa9kKnS63X8G6fCxr2ILuDfxv-tOe5dgWXe-gX0YIkyaFKU0DN2o6OIBWlVUdwy_XZgHJXtWk9mbVJViISrjd5yrdZ9-U6CWjRuSkmM0KhxpjuF0ZlBkNjX-iXjezI9G9PP33E4qB_od5ah3qrf0683djttqtI1Jwoup6mHkrMPv8yK1dDzUztsBRM-Bw3JCPfJMRtryNYqS6TENCIaHPHHdJsWXsXMnu9ZoKEgqygXAfiDb2tc8xxYwMM2bRTPhmNtWeFgZueARVzY5GuezSRo308q13yu5kJvzNfVYkXq8U0hczjQnhmZ-pcKBazEh7y38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-Rub5fXMu3AirHI99xH2XAa9kKnS63X8G6fCxr2ILuDfxv-tOe5dgWXe-gX0YIkyaFKU0DN2o6OIBWlVUdwy_XZgHJXtWk9mbVJViISrjd5yrdZ9-U6CWjRuSkmM0KhxpjuF0ZlBkNjX-iXjezI9G9PP33E4qB_od5ah3qrf0683djttqtI1Jwoup6mHkrMPv8yK1dDzUztsBRM-Bw3JCPfJMRtryNYqS6TENCIaHPHHdJsWXsXMnu9ZoKEgqygXAfiDb2tc8xxYwMM2bRTPhmNtWeFgZueARVzY5GuezSRo308q13yu5kJvzNfVYkXq8U0hczjQnhmZ-pcKBazEh7y38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کون پاره لب خندون مثل اسپید کسخل
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100456" target="_blank">📅 09:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbdUNMG8A44NjycQ1217wv3Fd8bEoSknZdxABs2xBRRvuswtEM7w9mst2Ggfy2b4fldvLLvf1H-Rum-H3OE_EsumYb1ruiA0oaSy2CZ4gXUCOMJDpEAnCcFd9Rh6woXQOav_bjoX3abAQ9xwn8St5mWrd1RnlY-b4AwwhycNbNvULk-xyHKXnYD-zscVFhhLRaSTqZw6p9HP-uSK84NQI6WhVZjr5MsWlwpVNxoNbfMGaezNdfZD2RgxfxeyrZyAvt30EEjMD9UuHfnwiLG53p-JgvPf_dBunXDZSWd58xaedFFimXekVgUUQWBmEQXs3JdqUQz-KkUSSJsWrXrrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جود بِلینگهام: "برای من، بازی کردن در برابر لئو مسی فوق‌العاده است. عملکردی که او در جام جهانی ارائه می‌دهد، شگفت‌انگیز است. برای او در فینال آرزوی موفقیت دارم."
🤝
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100455" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=HJS7szEi1VwXKAFxHiJ_AS2umZ2lS0RbZmI7aXIvKWUeTURppB1SPfZY1WaeTV34E11gtIfBfdUF5DVOpnn6TLf7RB_zBVQvEwZImN2Iv2R-0Gu07Dfee8Kdq6e_iRZVmOljChxb9XQluGpSs0nB1oIb-7PRToeZ77oAdAOlAdg2PfFLX6jgRvYCkY0miKYeSHbuR7zAWPEt26753OJgbJ_mcZ29fgBWWLkwJiDXXh6k_TkIEPNkEOTgegX9VnGE9PiPWe5qBAp8INqPwqzmkXrQzBV2A6E4AywJYi5pqxCIs-1Ayq8nl3T_VcGZkRie_7NMaab1RtfYbOFGJtX9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=HJS7szEi1VwXKAFxHiJ_AS2umZ2lS0RbZmI7aXIvKWUeTURppB1SPfZY1WaeTV34E11gtIfBfdUF5DVOpnn6TLf7RB_zBVQvEwZImN2Iv2R-0Gu07Dfee8Kdq6e_iRZVmOljChxb9XQluGpSs0nB1oIb-7PRToeZ77oAdAOlAdg2PfFLX6jgRvYCkY0miKYeSHbuR7zAWPEt26753OJgbJ_mcZ29fgBWWLkwJiDXXh6k_TkIEPNkEOTgegX9VnGE9PiPWe5qBAp8INqPwqzmkXrQzBV2A6E4AywJYi5pqxCIs-1Ayq8nl3T_VcGZkRie_7NMaab1RtfYbOFGJtX9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی خودمونیم بدل هالند خیلی خوشکله
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100454" target="_blank">📅 09:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpDjc5fcHl9LAoS6DVtaVU1K2uL4KBw0G8mnu2Ihl4PGtxGDDaEPp0gvPrHQxRu3P339OGV9EEqhdSxO3xIwHSN0XJZf8QwwSqoebfs_N0hAVMoFbZCD4D-JQLjG7HME8ZmFuWZKVstBdJieK9Do4evlZ46v6rebwrDLZashSRX4jY_tsORkKzd7nQw-GQ5T3hxb6L-IepDqn6te1A4r-UjeK5pwX2qlbxer_09YP8-R7hnTKGqvdt5meiwh1wNwJh67i7Glu670jODDnFmnCIi_9M7LPN-9YrE2gLdwBqrgOfe8Ji6vCb7x32TInI2Me-ChHwKJsILlJoA-vBvqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
| تعداد دریبل موفق بازیکنان آرژانتین (به جز مسی) + بازیکنان انگلیس در طول کل مسابقه: ۱۰ دریبل موفق
🥂
مسی ۳۹ ساله: ۱۰ دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100453" target="_blank">📅 06:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pea_U9C02Rc3k2ssk5GF7jwkcKV84cHyW9jGZPLeFPzLr0u5iwVinrd5l9pflTR-VEuRwqKo4xL0PMQfCbBC-vBVfpDLYUSgN-FnsNTbXOie7ilpfdU7ZgNsFJsT1ocVtrWz3CNN5stt2l8pIXpWzqOpT5gu8GcXEGSZfcbhqxkqKCWuFL_5_RrQZ_GdZRKLSAPbff7IU4IwYYLmx8HduEg59hEZFV5gwaH-rMmxvx6t3DjB4hcf9UuJI1lTw5-oIkNlo9HQP5tjbmbTTNeEVjBUN7e--sKwcfjy2oyEfoX3tDibiZt4HmSWwKsaOB058tYDvpV8Od4Kfs35e1XG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
لیونل مسی :
🔺
من خیلی از بازیکنان اسپانیا رو می‌شناسم. خیلی از اونا در بارسلونا بازی می‌کنند، تیمی که من عاشق آن هستم و هنوز هم اخبارشو دنبال می‌کنم. این مسابقه بین ما و اونا بسیار نزدیک خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100452" target="_blank">📅 05:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100451">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=Gh1Z28KTCUByzDomyMOmtfY_aSzRX3h7_8xBnTDReFRT1CeouyZ_Va5mr_8srHeoS9gLrD1Mag445O4DGV0ipF1rX0757PgKvoXS2VkBiXQ2_EA9_Q3JLBvYR-l4ZExRMOLNIxaHUxA3e8LoUocFyx4LScbXshKn8Kc6xZO1nPr3tyNW0c3onc8URXtPdg-EfWXtlNE69pmaWE0uiEr8v4KW53uKz6H4hIqkSzq-hUy1yaAmSyUDOSZCb2eMPmx0AQROCnknXYonPfCMOOs1nGhuoZXAcHk7RVt8w_Hz-HYrFC5QdKfsM2t6umAdS9H3rkhB6yhy_g4zp2Y7ntCHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=Gh1Z28KTCUByzDomyMOmtfY_aSzRX3h7_8xBnTDReFRT1CeouyZ_Va5mr_8srHeoS9gLrD1Mag445O4DGV0ipF1rX0757PgKvoXS2VkBiXQ2_EA9_Q3JLBvYR-l4ZExRMOLNIxaHUxA3e8LoUocFyx4LScbXshKn8Kc6xZO1nPr3tyNW0c3onc8URXtPdg-EfWXtlNE69pmaWE0uiEr8v4KW53uKz6H4hIqkSzq-hUy1yaAmSyUDOSZCb2eMPmx0AQROCnknXYonPfCMOOs1nGhuoZXAcHk7RVt8w_Hz-HYrFC5QdKfsM2t6umAdS9H3rkhB6yhy_g4zp2Y7ntCHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی 2026: اسپانیا-آرژانتین.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100451" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100450">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVca1GuB-D1bUfWDFnseCTfRxEVH3T_0R9XhXiWVew2Xt3Z-5prR__2LhFp0ppDjGFTCL6If_QfJREPgvsCdNTbzphTGc0OgDweo9_UYc2_qnM62i7mNkX6yNkOtY4PwgPzyOqTsZPoBLTblQSFgYs-YGvlEQkOup_6r38QT8C0zWA7V0yCcmH5tQPRA3hozYQpupeY21Chx-lXIVu7wzyQCPgbUxslXKFFjUxRWlwE7aK7VywQJ0GL4yuDt5kuP6eVoT_NqdxJn1WX4ommO5h11kqHZGlgji8Xv74b4rayCeAtg3ENWGxLMTrUB6M9lKhnkLMxvXM2jIaoH9D6HlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100450" target="_blank">📅 03:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llCwU2g7TMoUdUmdhy-5HDGzZtuQ4LtoXswgW9bLMiiQTQ_ZzJbb2NVC20KAqL_b_5lD3RBiG0pfVr3UwxPGRwgp2TdKqsZzIsnT7P_XE8C5QyiSKdgskhb3r7s5I5VHRnuBU-uun1ioFL2sFGd49kVt2OKixxRcDHneZUhzAUdGxgNECqS-l6u7aWmrLDUQoW2vjn2uWq5E9y076yw-t_WtnhgLuzFdSZ-lgeXbJgd3sqSSkUKq_vhVWp0pFuULkpoLhWIJm0EgpD6Fzg27qUFCMw5hQVovMyDLIh09300o5QxBsC6dFXh5wIi2nr30WS2KkJBTRap788JkK15-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا ممکن است تیم ملی آرژانتین را پس از برافراشتن بنری با عنوان جزایر مالویناس (فالکلند) متعلق به آرژانتین است جریمه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100448" target="_blank">📅 02:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=gandeb1C6JhM_U9z54mSm9AOMBBbXN6nnVw4FPXQ6UMD5SEV1Vkt872GQrjdrmLOqfQCyQdSH4CfG1Hi8dkx68tlOe4Gb-rcpszstOn5a3-JgPv4qJ5DYo9ZUohfiWYW0pT6jPWGgwB1ekths7oqTOVHXhpMt-MwAOAfQWQxaRYfpobMIwXuEZlQNmPN7wGbC6ZdL7l9CzMnFRoqZ8Qr1DIRs14ETkhEyMqJIrhP0g3yGAAtkg5p3Xcdz9maxQaMYuHvwgdB3p7oC4tgXoyXK91WXrK3rD4yhWs9xXD0FhafK1nO9rsU7XPw3ktVCBHXWhZlcPA5ddWOLNOtj_8WNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=gandeb1C6JhM_U9z54mSm9AOMBBbXN6nnVw4FPXQ6UMD5SEV1Vkt872GQrjdrmLOqfQCyQdSH4CfG1Hi8dkx68tlOe4Gb-rcpszstOn5a3-JgPv4qJ5DYo9ZUohfiWYW0pT6jPWGgwB1ekths7oqTOVHXhpMt-MwAOAfQWQxaRYfpobMIwXuEZlQNmPN7wGbC6ZdL7l9CzMnFRoqZ8Qr1DIRs14ETkhEyMqJIrhP0g3yGAAtkg5p3Xcdz9maxQaMYuHvwgdB3p7oC4tgXoyXK91WXrK3rD4yhWs9xXD0FhafK1nO9rsU7XPw3ktVCBHXWhZlcPA5ddWOLNOtj_8WNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری اکت توخل و اسکالونی بعد از گل دوم آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100447" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100446">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=cknfvziZZBTlRGl_4oAovrLTxureS6cPnj2RVcZhE9_1zSBBZY3otgkm_KS9LJtoV-sm25npLfiLyYtWDHlNrVKpYf89JiShRz2hbNpxCJqcHd9iC3FiutXjLcNBygyhbvOUV6q-xQHTT0r_rhWkdRJRewh6Pss-313FMtDvXk6jbCgeZccJgLvecZb0pFVVdED2KIV8APC_2i6wKBMV7Gtr0ldpnnHaNYXr2-s2Jf-tOkF8eVVJY3-8cqwmeqMVRmrh6JMK9TIn2imb91Jge63vNYckb3qOmhKpI2NMO92j4sCpEle58K7JNuZKIQqNX81k_RrvKxShlX5uuVAA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=cknfvziZZBTlRGl_4oAovrLTxureS6cPnj2RVcZhE9_1zSBBZY3otgkm_KS9LJtoV-sm25npLfiLyYtWDHlNrVKpYf89JiShRz2hbNpxCJqcHd9iC3FiutXjLcNBygyhbvOUV6q-xQHTT0r_rhWkdRJRewh6Pss-313FMtDvXk6jbCgeZccJgLvecZb0pFVVdED2KIV8APC_2i6wKBMV7Gtr0ldpnnHaNYXr2-s2Jf-tOkF8eVVJY3-8cqwmeqMVRmrh6JMK9TIn2imb91Jge63vNYckb3qOmhKpI2NMO92j4sCpEle58K7JNuZKIQqNX81k_RrvKxShlX5uuVAA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل کل مسی و بلینگهام
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100446" target="_blank">📅 02:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100445">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYfg2bQTPd0603UWT1jLMdIliv8GmF2ky58c476nuU34IC9al9ut6X5AoSR6ffDIFVxYx5EgT2FQ2yQzMdro54_qzaWArrcNyk7vOAJcbmBi4SGrYzgvmhoM3GsO2WcGmZLNEIt9WQnPVG0hHCnkCarHw_E7d3cph6Wm283wpEad4Dp2FVrnAUWT_tM80X7mm3SRfIY96cc4mTTzfWwzpFDBc1jA3cxPB65gXBJHpOAgtF_EjNM11Hv9U8Qx8WoPO5ZZrJCH9sLlqOfn_ikLC5vxpQ-dbbCjzDF-syWSjtNVvxH6BsHs_ZmQ_u1JeGQjpDRJkFZLqgXWmv5Wul90QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لائوتارو پس از به ثمر رساندن گل، نام مسی را که روی پیراهن او نوشته شده بود، بوسید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100445" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDtmvp_2gj-AUnn0Gj8AG9Qb6PoQjXz0-D7RJIdH_byb9LBHYBBK82JyXD9oFIBj1F65ysn6sYlCjs4Fl-8fKc94eQ0H6YGPh4YTiu0VrQJk-i_6jSWzQT3A1ttmlLK7l8NQNJlYkXW1KGyKYNHH8dgVl1BKBIEJtaVU1A1M1ZqIvFnvgG691fa0lksKKBrLkf7ml3AVKlqZehOE-HHPP1Wu1vwJbRRlGujujq4yn492956hv3xJ847l8QMRAbLfNHM3TJqMAoEXkyGLAbCnR_afR_2cyBENV_phEwESEcBIv5vDs9rnByFSedw56LOqmo7afDZXrroxhNlViacJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی:
این جام جهانی دیوانه کننده است و رسیدن دوباره به فینال باورنکردنی است. من به آرژانتینی ها در قطر گفتم: خوش بگذرانید، این تیم هرگز ناامید نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100444" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100441">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBW0EMK8o30YPk1LaFp9I46jgnBR9qO1w8t1-pWrBRg1BKUeD-ULRY9GkLh2-kmyAahApCfNoaC07lzacE6tIzpO3YjQFENLsZXF4ycasbCEfU0IqH0DjLtlrllBmBWJ64rTytsb77vNBgNaIxcUQXtZ1MFuliQpTFSq0AlNMj7JsY-O55qRcNIDdxSOOAuoIb5pbVQEJ5WTN1QVmn12m9_lq1s-zFG_GaAOZZbT2ZKlqgJWh1h0h-exQEGLYg2fl8ZmMigLtC0cj_tx621hU95uy5ZP4ZTV7TwlZ3GT4lna9Tee7nf8wbmEpQIH7coG27mX0mPf3649NWSnGi4HNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mo2TBExmq9YWLHkLQvW7jBM5HCjJvf5PoXOUcUD3vlTm5v01MBQzAPMFWrlb2HKOc1uqBFFQOKsd0mv3lMjirZSaewnmoV8vK_3nzn9Bcz4RvIS-IInbyu2bbFY_mH7L1TY4mXo25JRdwzWzamOgKrM2aWph9kZOMSAdqBmPDi_x9AxnG5DBRVVPtfl5RDAxYhwIAOK_doVoPL6xLnHQKFOJHLQ100HvWKkTO0OJmsePw07mq4Rd_K_8W3SWt0CLcAdKJIfpex-MDGyAS_0uKQRiV3-j_bz6CbRQs3p9WGdoSYQ4YcvEOJ_QiBbem5XrmkOCj57VIkeApKPn_M97Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbDyv5f9UHQHGMMbHlf8N-3L2-Kya4XBPGGxL_z39jMsq987Ipzl92g48IEDmdpOlPBiKzswwBh2_F9K5BGEaVeuf5JGJWGVzW7KbE5gkOJ227tNRSpYPJy0qU8jPNEMlUKPeJXJrlzhpyesN1_a9t9HEkvHdlpASWmEdg8SPRJlnkFUXyVTuRZt8BXz9HZE14r3eFKSGPkEhbqCJHnVJz-095rhOS_PCnFfel7hC1CKjAVlcgetlYTee9V8Euc9MKHB-099xQyV1ru_HG2zbaNKvPfe1YLGT5yDWa1CcYwVzrYaS_871UKV-d3sbcftXEYSfZwpezv5bYXZjy8aDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🐐
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100441" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100440">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqstjDIUolHjl3kuzszg_7QxNI6BbwhhE6g-x1suRaLRhaV1AB_ueuGpCFtVmdM9cpiC4wKJ_0RIZoPjlmdeCSdPaaM1oqb-qKl1_1zjY9aGMyjtG7Td9R58tAjZg6BDJ7IHnRPr9BP2vuzE2l22XK15r7g1IF1rWyUATV6UAPo1ccwsu6r53AlPJU0qz9xXQMdBLd2AuWpErvzeQvwfh53SmuxZU8SR3Jz6hRlile-iLpKNhqfwF1a1Nxwj0-fL8xm3wlD4uhGL7gEPfrHdxdBfPxb9F_JQ1Jn24peqtqAjhy7eq2WVfCM5yi3j7AvPW-r5YJo6ojR8vSELbs-o4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100440" target="_blank">📅 02:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100439">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135c24c050.mp4?token=adSu5oopaAthiuM9_3DsfY8AI8arKBZtqFPN5j1f-8p3KxuZmp_ZEAm-4Nee3NUqYrQEVVDH5E4UEOgTXBGVsIvEe97uJ4BxprDk4jsBPGDOomaKp3M4RZoXsXdHEbIt3GjscCPDdd2ortyrP9fC0Cp31cPZ1oaEOihGeZhMHEtXlvwPIFbgjqixjhTEQIR7IrS3FfAWUxz-Hvi2X3frRlCBG94uV32Xj7lombWjftKTR9a7wPOdjOGiLSCog3Hqr98e3OKmY97XwZXfBv9RVyzqKbtUjKXiwGfcNvX7vBwUla0jyVLjRrGCEDe4B4R6domQVTiL0wwAcY3kuHRAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135c24c050.mp4?token=adSu5oopaAthiuM9_3DsfY8AI8arKBZtqFPN5j1f-8p3KxuZmp_ZEAm-4Nee3NUqYrQEVVDH5E4UEOgTXBGVsIvEe97uJ4BxprDk4jsBPGDOomaKp3M4RZoXsXdHEbIt3GjscCPDdd2ortyrP9fC0Cp31cPZ1oaEOihGeZhMHEtXlvwPIFbgjqixjhTEQIR7IrS3FfAWUxz-Hvi2X3frRlCBG94uV32Xj7lombWjftKTR9a7wPOdjOGiLSCog3Hqr98e3OKmY97XwZXfBv9RVyzqKbtUjKXiwGfcNvX7vBwUla0jyVLjRrGCEDe4B4R6domQVTiL0wwAcY3kuHRAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
شادی آرژانتینی‌ها با رهبری لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100439" target="_blank">📅 02:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100438">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubFQzRH5ZAcNpjX03beelrUexG5q7CzVbDgyae9mGH7X47SHIhpnHvYqy2Eyl6T4aC9GMRGB6GrDDKuljCXAUZenzZE97JauKWfNpi77ve2popP77vBAwsThSmkNGFmJ7d0J2XOb85Voshn5ZWadDWqMEdAZtTnqIbk-ouFZjRIvV31RTsxjEZ5n02ytFSzFZIvtcjy3ROjgE4JJkxZ0MmXi-hhECS9b5PB61FI6PPlUDYToCx0ZxUrT2_WgzdEgVOf8l77FfAyCgDb53bu_RnVqg46PxU_CwgUOUWE4y0hkAa4Gk-MYh3HDT1-ogC96hlHcMnEhz823nCXuxNo1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی و کافو تنها بازیکنانی هستند که در سه فینال جام جهانی شرکت کرده اند.
کافو: 1994، 1998 و 2002
مسی: 2014 ، 2022 و 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100438" target="_blank">📅 02:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100437">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=pL_nfPI34CkTujFrFKegEukZk63tWPyohNXfq-VXs9pZGjXaWYFQXG6d-cBRa42KZjcxUAqA6R8GlrstuvCQEd0SGUMweL_8ANxOHil3f2aoDyyCE2VZBVAyY6V-J80RmpreXSJqD8Bh2fNOK-d5MIrI-DIreb1t3rKAmtCCsvzmox51So_7yBiOMgRMlucXeHHQXDMdL-5275KeY1GSapZZVyz3PsJsw0GsmOG31HlSebNNC4ilzeLdqjTtmvoKI9XiDFGJMLWqFwIP5ih6PBgQJhZlJHk-Ns7X40lRVtToWZONYXljyRP3sqK4c_gY2cUdnHA-URVR4-js0zA6XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=pL_nfPI34CkTujFrFKegEukZk63tWPyohNXfq-VXs9pZGjXaWYFQXG6d-cBRa42KZjcxUAqA6R8GlrstuvCQEd0SGUMweL_8ANxOHil3f2aoDyyCE2VZBVAyY6V-J80RmpreXSJqD8Bh2fNOK-d5MIrI-DIreb1t3rKAmtCCsvzmox51So_7yBiOMgRMlucXeHHQXDMdL-5275KeY1GSapZZVyz3PsJsw0GsmOG31HlSebNNC4ilzeLdqjTtmvoKI9XiDFGJMLWqFwIP5ih6PBgQJhZlJHk-Ns7X40lRVtToWZONYXljyRP3sqK4c_gY2cUdnHA-URVR4-js0zA6XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
حرکت زشت و عجیب بلینگهام بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100437" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100436">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎙
اسکالونی:
ما برای پیروزی به فینال می رویم و برای قهرمانی در جام جهانی تلاش خواهیم کرد.
هیچ کلمه ای برای توصیف بازیکنانم پیدا نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100436" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=KKGDN6mzMngirVYk0nVwfWjkVKdUMcI3LWcpTzNNrb9ehtpcYeFXsvlFZRyCtRZRmmhdvFcsGBCkS2m66ZcsEmXWEkt3sxSmcLnyWJOv_TuZovDdVhbwm-Nr59TCavWkyevYlgKMvwlJRoSfGJx96JQYWo41VUrf69JmGth75ddvfUQ3XlweC1k717yn26Lk_HVSvPn6nIKG1s1fIaPJIcEAONjtGy3ioS2luEUOucPrCKbDehh0AGaxCnyiys2imd8ZrwXjYgO7QvLtxvu2KdjlaV9LptxGKuAXzknBS2oXOMkhR1Y-WR4aLehfNwO59HNdqNZfghPX2YxcMC6AIEVuKkaDMb4snUzk8zDuIc1lR_dyGTjjuSv5NtOM0eqCG_LwSoQZ3yoTXvViOk-bde0B-66wFBIj3nh_uhROqWS1Q3U0YzBN2RYA8uC_WP3-Rw3WngGqK-yvhJtBF95aOM5n3n5-7tuH67MgcF90N1_-oRmeX0VhhY9NHCZ7KXZkKJxZ-hFa5m9b3ju0Fq2r9blLpRrIrQwJAmHyc86xlpRNpOdJXSIrFfVv0CxOOVT-3Mngph3qZzbkQOuyoQkFBjVWa6lOWGqIL8Ud7SX5bds4pzwW0-tOJ0SuZvzN2waqbn7_4ViXPgxozr7i8qMGJAeSW0lGcnK6iuKIra37XeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=KKGDN6mzMngirVYk0nVwfWjkVKdUMcI3LWcpTzNNrb9ehtpcYeFXsvlFZRyCtRZRmmhdvFcsGBCkS2m66ZcsEmXWEkt3sxSmcLnyWJOv_TuZovDdVhbwm-Nr59TCavWkyevYlgKMvwlJRoSfGJx96JQYWo41VUrf69JmGth75ddvfUQ3XlweC1k717yn26Lk_HVSvPn6nIKG1s1fIaPJIcEAONjtGy3ioS2luEUOucPrCKbDehh0AGaxCnyiys2imd8ZrwXjYgO7QvLtxvu2KdjlaV9LptxGKuAXzknBS2oXOMkhR1Y-WR4aLehfNwO59HNdqNZfghPX2YxcMC6AIEVuKkaDMb4snUzk8zDuIc1lR_dyGTjjuSv5NtOM0eqCG_LwSoQZ3yoTXvViOk-bde0B-66wFBIj3nh_uhROqWS1Q3U0YzBN2RYA8uC_WP3-Rw3WngGqK-yvhJtBF95aOM5n3n5-7tuH67MgcF90N1_-oRmeX0VhhY9NHCZ7KXZkKJxZ-hFa5m9b3ju0Fq2r9blLpRrIrQwJAmHyc86xlpRNpOdJXSIrFfVv0CxOOVT-3Mngph3qZzbkQOuyoQkFBjVWa6lOWGqIL8Ud7SX5bds4pzwW0-tOJ0SuZvzN2waqbn7_4ViXPgxozr7i8qMGJAeSW0lGcnK6iuKIra37XeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇦🇷
🤯
کسخل شدن گزارشگر آرژانتینی پس از گل لائوتارو مارتینز به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100435" target="_blank">📅 01:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100434">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEPRntvfaBjUTkO53xbjhe7X_FsxnmWakF7iiSUV2tQhbI7MWLiu3rJcf7fpuOZ4log-P21_CPNg3144RzZQizsVFniq1S15gOcYroEw_RhyI1jHcw-Unoqhv26AHzad67PuQdI4qaNLPar3WnaNwOQbd8DXnXhJACKZI8QqmDRfICTbR5sG7CO-3GUzNlk9nhHPPNgPmrYAdRqqBlh4dRrRS9rVKGTkDSRWgB9NTqED9EJaQwsxsSqDj8V2wbdA1hhuV6O4c0AvBwzTCk7mbQU__CP4e7uVs1MeIcqFWcV9uM2CpXtNkuhlDKjU2WpOQosSt45msaF_i_6tsQQdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ‌هالند بعد برد آرژانتین
😂
😂
🔥
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100434" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4tCtIgF3acV78bYt9wGmLL4DZ-5UhWCuck1x8ILUBruIHOHr2XNHIzSkJxKB8jpoSRGsLVmiV9YUgE_-OiVasKUxXTqmU7zqp1eQ208EzTJ3781w0-QrkRp_4LT_3i6QJDvSat-1K5a-kIa1t2C7wFCUd8bZAazf5gxWj4ATkrXiF_D5feMSZBk-RgfYXPMOwGCBPuXWeIg9cC3PAKYPU-1gRe4i_8itRmSPJJyo6W-zZSPnpaAhV2o8IHHS3h412iTMVSABkBoszjMy6aanXiWbqgvpONRyYNn9v52gIIHxBL5yA-FUfQrX63pXMwGQMcMRdba3CXMR8nIjLaMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
خایه‌مالی سنگین گوردون برای بارساییا
:
سال‌هاست که شاهد تأثیرگذاری لئو مسی برای بارسلونا هستم و امروز متوجه شدم که او حتی از آنچه فکر می‌کردم هم بهتر است. از حذف ناامید هستم، اما می‌دانم که حداقل جام جهانی را کسی خواهد برد که دیوانه‌وار بارسلونا را دوست دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100433" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=CluqlbZ10dkIp0sjhch4CFLnN1rdIhGmqG2yLu4cZVaADnLmL7FRzaZiM01HLCVnVvlC4g2a9Ty_NvwJ7Lfx09tEwWPxEYP1Ewr-xPGo-6m3WXbnIimoiQlrgbl_jYksFR42OsTEpjOOOhp_EsOsoNIhP5uYPIRrSTQcENv9npGRa2AoX1lFtifanvwi2-OJzjRZdl7aaSkcGo0yDODrWcpqEH1bRPtUyMWIVVZGWFgSqNT54yQ-DlezLNdhrZNVTHpphoagWpRkOwN-EfJzhnUPvcBIl-is0t7C9IA7oJDhPhHAAMpL00TzzTtALq7wxklnSMMsNeTF-JL8BimRCVME8Ys-RJnvQajjr4P25m60WFFgaavyZOYbozGy-Y1P6zaYq4IcpgDw7Pdye3XuTB32N1b318QI5sD6s917M5gpHwwbhZFoyjHGzDQ761L7mHkR2EKN6Hax9P14Mxa6TCjNLh0-u1-NXD2JIlPAI0KJiNIaZWxRK8NWpSiv8M4nr3KA0TVnMpEwUySTIaAUrOylEX5ZVnfwDPnqWqWLWmOqBQfda-m5BjmqloqzcyBmte8Wv2BQk2zIEItFWsul1Lx7nxpoeBTaj9rZQS1KADRsqe4gl6svqJmz10FeINivlCMFv2wjNAlxC_isRAlRpv8_Tdgor4iaKDC0pv46qbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=CluqlbZ10dkIp0sjhch4CFLnN1rdIhGmqG2yLu4cZVaADnLmL7FRzaZiM01HLCVnVvlC4g2a9Ty_NvwJ7Lfx09tEwWPxEYP1Ewr-xPGo-6m3WXbnIimoiQlrgbl_jYksFR42OsTEpjOOOhp_EsOsoNIhP5uYPIRrSTQcENv9npGRa2AoX1lFtifanvwi2-OJzjRZdl7aaSkcGo0yDODrWcpqEH1bRPtUyMWIVVZGWFgSqNT54yQ-DlezLNdhrZNVTHpphoagWpRkOwN-EfJzhnUPvcBIl-is0t7C9IA7oJDhPhHAAMpL00TzzTtALq7wxklnSMMsNeTF-JL8BimRCVME8Ys-RJnvQajjr4P25m60WFFgaavyZOYbozGy-Y1P6zaYq4IcpgDw7Pdye3XuTB32N1b318QI5sD6s917M5gpHwwbhZFoyjHGzDQ761L7mHkR2EKN6Hax9P14Mxa6TCjNLh0-u1-NXD2JIlPAI0KJiNIaZWxRK8NWpSiv8M4nr3KA0TVnMpEwUySTIaAUrOylEX5ZVnfwDPnqWqWLWmOqBQfda-m5BjmqloqzcyBmte8Wv2BQk2zIEItFWsul1Lx7nxpoeBTaj9rZQS1KADRsqe4gl6svqJmz10FeINivlCMFv2wjNAlxC_isRAlRpv8_Tdgor4iaKDC0pv46qbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جو فوق‌العاده رختکن آرژانتین
🔥
🔥
🔥
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100432" target="_blank">📅 01:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شب خوش رئالی
😐</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100431" target="_blank">📅 01:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6D5lDKmxzBUzZeBHhI7w3n_8Xqi4uLJs_ubYuRrCOt7bB9uV8lyWTB6TJgR5qr9YI_9DwdDLwJb_eRsp1bXvbecTNX-WH5TttE3q7g1qae0aEDbYNZmGWYqOwPdpxR1dgci9q8WZToJu2Y7U5FT2InXF_jCwJmuMQiTlh26m57oMK3EPCD8_QfPaJorH2Md0s4YnXxv9CqazUpBKDrfpYRrM9Qa3j2tnWRLHy1gTAnzDWu1a8WPvJQVVE6wFp_D38FUVw1VedR94JaM5d_MRqdFfRqtzPwPgJquRSenbFQ5RJlvMBoUVgHuKOVbFV2pJ6UFEd9dDgAwlxE_SI4h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
هری کین: مسی یکی از بهترین بازیکنان جهان است. ما سعی کردیم تا حد ممکن جلوی او را بگیریم، اما وقتی توپ به او می‌رسد، حس می‌کنید که انگار دوباره به زندگی برمی‌گردد.
😮‍💨
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100430" target="_blank">📅 01:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbN5kaa-jhSBRMWiC6hfIxpE1doSSsWYPcrOGSWstuzo8XfzJaN2AITzpeTj_LA8a9P1JTWfJaJuPJVL0zFknqvcHVHW5fJ2qBZ18CjzZQOaChoBaOiyWm5uJUXJw5mSxVsoDOSSqMduEXGf_mneIOYqyNYK1xaWV0ym-i2CgQzpqULgF1VIWv2BPNQc1EblvuQAxlar6g0UbSZKBST9LBFQ1slY2SqRpH3zU6AlcvKpQWuJQ-3_cLX0PZl0EqPC3GU-3yDOQcewzvxEdxXkTtP6rgsq_tIHR0BNhb4otxvWkvmC_4ABRVPwFt1v0f_guNq5TVP2mR62Lwfp943A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇦🇷
طبق آمار اپتا، احتمال پیروزی آرژانتین قبل از گل انزو فرناندز، 1.3 درصد بود.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100429" target="_blank">📅 01:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqbFiU0jETubyqx2EhM6b0SkxJsDEews3gyCJ2FzPyccnJL1tD5OskY3udPFgkon-OS2MksNc_W7MRHwg-bpbsqgBRuxv8V0RmU93vPye79Bm5S_huR52kRTM09IirOp1wdx9qpjwPLGlufueFsHAH-6oJkUQgQFwwq3Ju8lneuJElPBBrS3jhLhQVw2FBft00CQvcR7S4Z_lz1n-_WdjSzJJTz_Pblkw3T254mmRlj8fot8hkaAEC5brZKbX4i7vV6wV48BxQCUBRBmIy_jf_5qHFrEmODIEo75jQwgMm0Z_wLCSmf-l3npSHBsRXvhcQOW9kcqu25fQMjVvytpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
🤯
کاربری ۵ سال پیش پیش‌بینی کرده فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا سه بر دو به سود آلبی‌سلسته تمام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100428" target="_blank">📅 01:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100427">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7oVgZvWSwawPe4USKH5IGkfLkuyJJEgFpIskl3NQtiUyFyn6i-4g0CN4EArR3s2r5Wb8kcpAg4aUduwoQKEcm54Z40aphTAiJF2Hp2PdRVDIva-kSVeYVJEMgiz_dVTk0_3O8HUw7egrnsvC3TuxB4qi6KCiDBas1YRiN-nBs-TXCsTTYwVdzszL6zMl0bNKEP22E9XzZ3FpK3Pc0y3aqsqvejbyJgLGxZmQa-z9NYaZeaiwJUioMtxLgAUuCRJoY-FQxZrjWIEnb3_oPht2j3WP8uk8WxTGKzU7ZMgNnAiVOCA7epA8b5MwGmIar3ccEctwkIXAwJbyaIY7eiRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
MOTM
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100427" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvDWsCvi0GeFa81-zvGauvh2CFuH8DqDa3EuTHtgkmAE7ASPD3Kt9OTKOZSbMhVFDcmCUh5_zN7MAt5VNFeBPNq6SsR5iD0Cxcbxmun-PsxHXpLddbEmGa9-HNI4FxDUp9Upfrrr7Ies88bWQJl_x5b6c1-SvueOQbQLUORMafZGKFsnB92X5A_pYY56Cn-YhEjq0dJleiUH_H3AtZ7ypkRcBFHZNIutsBU7fgfMYzvprAH1CsCCbCyJcIaZxySkx8dTt5JXJ8UPjMmkKmXVWJE2_DBpSUvQ28ri477sQLfTF9NpHWnAyzwdDiwa4hkayNM83SLsVhceVYWJAo0lLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری کین:
قلبم خیلی شکسته. تیم بعد از اینکه جلو افتاد، خیلی عقب‌نشینی کرد. نباید اینکارو میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100426" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTomG6MnLF9E8N_wVrfdiM7CpwdVRfjk39iTjmtIueFH8P4xZRu9YVZJ2GpZEvM2GTQj7rHqBRIrZoC0j7F8q73b5YkOBJvSiXLzaWYj0Tah3Cx2mhyUM87e-zwFAuYSlEjV61Oj4JOS0QqHC3_n3-w0kaoRtgCkF1e9a1H30Kn-BCIxxrbbPj_H3NmfDUdgW5PcCQuyowMSFbFoIv4ra5fDdpd7zkxkzKuUXnaFWF-fyapmPiiTZjemIv__-n0qJZADidYx5BXr-99Ht_qFptK8HmAHMmNOP2MxFZ_GzKRz9kwMT_Qzc4JIvedstEXPI-od8USk-MYQT6MKk5M3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: قبل از بازی به صراحت گفتم که لیونل‌مسی یک قاتل بی‌نظیر در زمین است و از او باید بترسیم. او در این سن توانایی خود را به نحو احسن ارائه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100425" target="_blank">📅 01:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKnpb9BpInNWJBR47pH4E_c5SnQzh8tqAOlL43-ZWjmGzahVxkHdPkbN0kWSlawJ2npvx_uvxYXjsUP7mrJCdsFBVv3r1cpIXX7vtfkTznhmv2TuRGaabftlhXQcM55Q_DwfVXgMC6CPe7vV0ump_4ZwihjZv2MMCbu1ZS9VJ6yEr7Qwxg6i0emXRyi9toK01nra2FKSmmcqgY7UshR_ipoxILkGTbZVXVFR10Ps_g24dQxxg1JXEgsHYNSHSUGXZXAXjcC6DExc-mpijr_W6wSEHJ-8Nzj3lFZT1miM-GK59Fsx0CuZ7u8rQP7R6NHTvNQnNs0tGi2jLeHgt_dtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
اسطوره، مسی، تا به امروز، بیشترین تعداد دریبل موفق را در جام جهانی داشته است: 24 دریبل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100424" target="_blank">📅 01:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY2rqQQyKQY6m6YuhBHiS1DajfASQz3iqFyC-324GfkemordZvocZA7IXJnHU6s9x3m2BKveJRDghKnshIQS8-3Iq0o3mmb4_QhkeZMe8lKtnj0YAcbNf8_8cHi0q5fHNretVfJxaZbwHwkLC6iWEIxkkuNb7QrWo269zuFOSR44NaVELBUeukcv5VQOG1c0nfIiZRKHxb2M0DXcfyDqkzr2p9dds1A_-mKKU4JEaGIgm_ka2tX4LO031UUGVTdGKGgCz2oaJu9GQviTIfqeDl4W7WpE2dZPPSAuDgeO2KGEvkvMK0IKc37cWsY6haSdhN_WfM98AKgM5tBevoQ40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: شدیدا ناراحتم. نمیدونم چی بگم. بازی ضعیفی بعد گل اول ارائه دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100423" target="_blank">📅 01:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgKfdl6K7PLl1dqjq5wEsMR5HEbKIM11ebblQ5ntfmU9GnTOZHPE9uJ3TNIPGhjR19luWW0s8Ks3polMT1IB6-hq0BW2Q-Tz7I6ZQfEsyZmq951fH1NsXkRUUmpz6XIcKxwRlqFlIHi4Jrj4Ng3xoq2688LdkyWiqi8QKYgz2XPloAOyhbj-DEKC1SBPwVg6avMR0St-ty6YwOCu69yusZ6GEVC2gHBCUiKcFy7ItRq25v1_0UDZiOPpHnLe6CCuAFVfI5cwrlSOTEnbPAR2NNpDTVD4tJnYPGEMX2pth1jhHQqiwzVqxutN-foWTJ7lh5LEff0MMJ3N8avruMDMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100422" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC6JV48_V9nx3ngVXp6w5v75Jl3IuvUkDm_-Pvk46fBvRuQwyzFfaTc-bxammeb20Zbw0KY3NdwL-9j4bWy-z3_7cW9IjojQ3pdO-So-C4arSqX3cNLfFdc_15OEYyAJJMlkWKUOPuYUn3dBM7OsLxSHGAQqOB8M0iYBHxJcHqRWEjs61imfzonxEI7crsNmpK7lj90gbuK83VY73LoS3-I18ICKyqaQU56OtgHxgTs92XDlo2kGcFB7UesWdF68dTYcmP82MpPpIydHXl9FqYzZeBEErAgKmjXuL38F-NN_6M3Qb7i-LGr7XsONTz3V0OBh_48fGxoQ_e-BSEiw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
⚽️
پست جالب DAZN: ‏بعضی داستان‌ها تغییر نمی‌کنند، فقط قهرمان داستان عوض می‌شود.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100421" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDtW3lOiYAiUTqsIW0CL9gKptn3AsrZCgSb11nfIxc9QRsbdRk2eGSsOJ9XFZIA9qBWzXJm5KaBQrtDC5MHU8JQjv9xnmpJH0ge2961gsefG2q2JMQ996I-ggznLWMR8Vr0i0RT4s7WVkouECpLJEmtJGUWE4Yt2euzrwIxM3h75LdB4RAIwJtt3o4KS6B9TyeXSCTuDA7i-Ag5govPrZ31QlvaMdgZsSRRccwtUnKJ5zd7wdJJa5rFmgpyDMsm9xLi7CeHD3eSqPkrpb6EAtjUilJzCAF8h7uMTzN5CJNLi5ocU50lYh_oeZZv1hr0mEv_BsiDwsJEF0PBcXO-OIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
کلاس‌آموزشی احترام به اسطوره توسط آرژانتینی‌ها؛ کاری که پرتغالی‌های بی‌لیاقت برای CR7 انجام ندادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100420" target="_blank">📅 01:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d365933365.mp4?token=Y4iTRNFo8VSyExqIi328meLhLhRAx53i-BtGCCtAw8lomj8zNQWL4Lh3_Lra7A66GP1vatfT8sRyuKy4hf8OOy8OxLXvFfP6vg2Al1eoTIQMQ1GXYND-bmkCk8z2wuP8ykbIfoLQktoGqt4hbVYhz8FUOJ0nafq10fJ7xf2DJV34AD_-tvKOkgq-vDySvJ6F71LWX6Qd8XMU9wM4T6qWB6A4KWm-_O0UZV8ghu4siFScVKNS3VgCdtLnxOb3IfHmrHaywRgrLv2-_9RbzVi_8L0VeLjQlhNULRNsBecnN1SOfwW_ez6OUTAxrRkxkYjt7jBNsk5y2c1NJukAaryePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d365933365.mp4?token=Y4iTRNFo8VSyExqIi328meLhLhRAx53i-BtGCCtAw8lomj8zNQWL4Lh3_Lra7A66GP1vatfT8sRyuKy4hf8OOy8OxLXvFfP6vg2Al1eoTIQMQ1GXYND-bmkCk8z2wuP8ykbIfoLQktoGqt4hbVYhz8FUOJ0nafq10fJ7xf2DJV34AD_-tvKOkgq-vDySvJ6F71LWX6Qd8XMU9wM4T6qWB6A4KWm-_O0UZV8ghu4siFScVKNS3VgCdtLnxOb3IfHmrHaywRgrLv2-_9RbzVi_8L0VeLjQlhNULRNsBecnN1SOfwW_ez6OUTAxrRkxkYjt7jBNsk5y2c1NJukAaryePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم این چه سمیه
😂
😂
😂
😳
😳
😳</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100419" target="_blank">📅 01:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEdKproqPE4mOSbD-T1lPvAa_g3DvOZQSgdshVgVp7S-BNBetNFHcGMuD8orW7q4Yu3EqIfAux6b-rfsd8TupQUXOdId6WcF7Os4eWj9IvwfndhOvIApOioduc9YrTu3bfKzsT_bPD8LQ5xn5uCskUPCx8Vegx0-sPqXsBxnGp7bJc8HAtU_xDru1dP-p0gl-E7XJnLziFtx8BVSVJVVH6ppYUW5e91WnTonhEGKai0HQ6zkjguBh9Dex7gggoONTYfvuyrwSAtfOYO4IMbLP8mPYJby60ggaEREwFEguSOKVXXcV-ts7WEc0wkBEwlh0RioM3WNK3-VkGU4gSHH-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
لیساندرو مارتینز بعد از بازی
😂
😂
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100418" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100417">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_fhiWTungRLLK2vIr5Ikb1-OSIROb9fZLjStfFSnIeS4qpdEGsWLCur59VfXmiI9q38Bv5pMdE4OzooNp0tYCZAAzbysqfkEAB25Cy94olkQh1blKLp4qwxtmNc2SfWUWPsv3KR2zVVcrffelbKjV8_mCB9Rorvjxr1JqsG-4mBmSvJDW9xUeeyHqqX3Wd_GtKGbCZ6_uLtLfV_n47g04XtWbqDc_MCWwGkwC0euRTzJ-fpE2secqR7iuGYzUlXNRACfHkBWw4kC27wZkUx2NTwpDRgjh1zhBy5xvCHvI1IdNPAAygtNC8FajhZX2Oa9tryMugT63fhZzx85ZiWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو جام جهانی و 2 فینال
کسی بهش نمیپردازه ولی ایشون واقعا مفهوم آندرریتد رو برامون معنا کرده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100417" target="_blank">📅 01:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100416">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh6SzM9Knmw_hjyMwxDJOFaIuz7kjiE3R6PrGbjHpip8xmdio4oeJ3nrT1w9djL6rXAd2Nu2vzlNyXYfrxrqk2sFoytQQiPb8nZEluEESfjiVD1WkeAlLQemBhGUQc9_CGFfvErjlz4ZDCe_p04HEgbrsW2Xg-5WIMx4YmI3wyeNOOZC5JmhEgep7Xg75xd9gk0D4Of_FjoGtTIEvPDzNJWcQbZ4FF14Wc2CqOeC08C5E4imL4HXxhVc4ja3FC3BOoe6q8EBnZiQY5VkDZt7it3L8kSzkrvgniqkd69kNW3OYD1chHFNPwm62qkjwpqRtEFXCPuYtq_WDPO9OidewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
لیونل با کسب 87.1 درصد آرا، در صدر رقابت برای توپ طلایی جام‌جهانی قرار دارد، طبق گزارش پولی مارکت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100416" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100415">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD3HHpI9oZemXt2nC1lc0PFb0c-aNg8yRZGuO1cuBbY2bw0qGWWg0XV1IuVo50szYn8P3B5aQ5uFkAfYu_zG9kedfm2T17QCVcyBPUJcKBdEs_gqJG7etz9nW0HMdk7CZSGPLg8iLfU_qIoobpNj3W4XuWxs7lhx0ROEPeLCKFAuJ53AxH5zL8-1JeT7lq7IbmffZwewth2ljh_-lySjbFBVz1zomDYXplCf3b_TFi0Nvq-2tueJ_T5KNpAcaxYrgnEcRhofty-cq8w3kWWfkj4QVMeRCb-SZYrkdyFRDQ6cN7e4Bq7NtxAaxK9pLh4lxmc0MfvdZq_f-PzG0WukQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک توخل بعد از اینکه انگلیس گل اولو زد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100415" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100414">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnPUd7X7xhy_5B7Plku7oR0pev3PuuMl8WRC3xUEw8V1jawFUPXJJgXaesbKVKLww3QNgxOJzE4hvjVD1vC8rEoS9tso-zlXFUUwqpOURDNyfnkKxR1GNYkd6RHBzhAjuYlsKnZUgiah0QeZtIBAa_l3XIHigFfginWiJKsS2lRIplnzAxHELNzhZaH_zTiZPJAIjJLNM2GbhhnF8s59a5SvmIJc7q8InvHo8dVKnufviKfyf9jyO5k798O-e3V_FahktoGI0-jRtW0NrA1M87TDpGY3Mu5G7_vV_62eboKgXNo5qOkp8nMdW6RD5ql4RpiVy16rejS7tvw9VEjk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
ویلیام سالیبا مدافع تیم‌ملی فرانسه بدلیل مصدومیت از ناحیه کمر ۴ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100414" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100413">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100413" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100412">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hitEl3H-7O3_muRlKjQj4hV23JU6dNhKZFVZFa_5i1NJ9dX2gyWzPAo2z9JLL3F2y335EVw5wWvtJz2iej2eTC2wwzhfsQ2YbSdiA977Ni17EbLRyLniM4sC9YzcKij5r4M4Qys9WuWpy-lNPC7d-606RClhm0BrjXxK2XMrOaZiwuDGaH85bXPa7dHKgBjIrdidbpKyLzzpZr7tEVBDz78_QCoUTgMs56bn6_sBpE5NmDFycQPJ10StZOSVWWxLLYRghj3e37k7qdLSfl-CtY0H49lPZ0wZWr4WZI-TX0cuQkMgixdOBcS987e0F6ZQM7xmAlu4kxVSG9ctH5aIhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100412" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100411">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
از الان بگم دوستان رئالی - بایرنی - منچستری - آرسنالی - پاریسی - بازم رئالی - وغیرررره
بازی فینال هیچ ربطی به شما نداره بهتره نبینین و‌خوابتونو حروم نکنین
مرسی از توجه تون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100411" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100410">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9T-pXaoZ_jLaAx1D3Pebqlf0ypLylG6ZLK7KuPHaG4-BiUihc1tjt8lByKqPJSva4RX8rUyjKtG0Fxtj7SirfY1HuCuzqJeydWNfcd8TmlxcnWj4fPpP8cTN5ZMzsz9rvhxURSPW-zHp-yrgKbjMNBMc2ew01_PR7Qixw0icq6MYjzwMi5cHCyUmyarQ8d0lc2xwupl7gqZ2dyUe1trvhoesg94vAaKdoWdXECADqRyUZJaNnhANphgSxjeUk5HdPbHxTJZPOK1icSx41KXsh3bjyc8CqaGR-uMpRJAu2U59Jmse8DdIKi0lDtP7NYMhhXmpi_h2tsvf1WFg1cZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روباه مکار گریه کن پدرسگگگگگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100410" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100409">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
هری‌کین: من بسیار ناراحت هستم بری بازیکنان. من بسیار ناراحت هستم برای هواداران. من بسیار ناراحت هستم برای کادر فنی.
🇬🇧
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100409" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100407">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKRfVL6SFZJkTjaYJQmMQECST-MC7Wlgd2J3gArLbovWgBR0dv54-ku_8VJsPdndjIhUcGvWT4-6XakvmfdGb-EWDuQxz3YrnChopgA4HgP1UA93UTxBPDYv2EuQzjIMh2jLL3z9P584t2dkiuQnUXGbvo48FR52q0dXDHLhPqJ4pN-G0McZ3z3T5NhZrCvX3cg6X16zoC9sm7rs02xAWh88reDHKs4G4NIqVjZySO6z9Us5sQ6XAaDk5RjiDVs803ChaSlwWKEZebcxlwKm94piRcokFkRUvZfjfmPirSwXdpvZnYVkwBMMS6QbUA0pNN9ENN4eZ1QRQs7h5tTiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4OWfhktumlPhsanO9o2D0vW72Ol3bv4MmPttEkWmSxuCIXH6SQkuFa9Z17Hk6fzA5n3eEvTDErh1dhallaD4mkDhUmFKURyg4uLiXtUbO4vpo2sIAUrF6Apxnvs2IYJFTy7cwSnB2AqVdsBWRxBv7Vb5LZ5X06eqNFs4ygIvEKKYR4MlgEPT81DpQbnoJn5OIfgmAoYyy6xuZAnIpkw9w5ixkeRJSmn5OSqJhObz8FyQ2yNqr0972ZlyjldEpnFQDIcdWuMmbP54cOhP5t9FJKN08ezdyNe6lDAE16NKVMcXVMpLi7WfR2zr0GiDNcVwnGh9Jw798lAqbopEu9Hjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا بقیه هیچی، چطوری دلت اومد یه کاری کنی دوا لیپا ناراحت بشه توخل احمق؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100407" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100406">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9z2mrquQIMZc3Uwsmr9ROf8woUN1fPxjk3GnINWadgKo6EJtTdUFyQ7mi9z53MiGKyRa26PHvRckg6p0JbHHsO_FJrPY0F0OfPylsr4sqdpS9AKgkmfwHOmJEHEuCg4lua8b0_aB8exNzqEG1KkIri_Q1W_Zc2pY3mUexKnBcgXKef-iAsoy3m5E0aktTfV28JlBiHVebtuFkVEeVoIp3V97aId_u36o0LVRaUW8yzWeLf4cbdkSyM-u-h4MfWJjSS36-CHfMMxTtghqmj4MVB4Rv-6nYfK2JG0eWerzJRjl0mTTh5aZfz8r6075ckBwLx9HVXb8rGF01VO5e_8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
🏆
🇪🇸
#
فوووووری
؛ علیرضا فغانی شانس اول قضاوت فینال جام‌جهانی شد. با توجه به اینکه فغانی حداقل یک بازی برای فرانسه و انگلیس در این تورنمنت سوت زده، فیفا قصد داره رقابت حساس فینال رو به این داور بسپاره. جمع‌بندی نهایی تا حداکثر روز شنبه صورت میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100406" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100405">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhUkMqK2qbxnFWGrQM6SGKRh_2hafZoNG8e6E2IZE2wal96ql_PkOTHlzQg0_HfC2i--tCHUJYNYJscgSOtRXUOzyWnY0GVVNcpu5lsml9yoXmT81T6yRNZAvDg2MHFT07OrcWszDp4Y2xqqvO6d8FrL9gjEL6PByUANEiUa4Hni_aDkbSMpfUDbu9HRHNPBVuBvoqOcyE--zgl-6_PnIv-PXYwwwudWB3p6qgOmGAdwPa5qUJXntyq6A5Qz5TkqRcu4M8jwS0hgeRLFX24RZbL-Cn6tgp_I3IKZ7lkhnNycDrLpAhPEceysEjBO8ZlseIHqDa2AUjQwHPiVGN2sYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعویضای توخل بعد از گل اول انگلیس رو باید تدریس کنن تو کلاس‌های مربیگری تحت عنوان «چگونه تیم خود را از هم بپاشیم»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100405" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100404">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇵🇹
➡️
🇫🇷
➡️
🇬🇧
➡️
🖕
چیزی نیست دوستان مهاجرت ۳۰ روزه دوستانمونو بهتون نشون دادم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100404" target="_blank">📅 00:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100403">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSaqBDij9k6wdDRm_z1ItSOaMc0ixguO9GV-ZWMl0B9oHhzev2D3AjroydUMZH5smClKTdIoOEpeSx-jX0mW4ROkgpDLWbWIvvknGBPo6u1WA01Dt26aT2rK9nFtIdQ1i8mnN2G9pjHpMNXyk_qsuXJNrpmLufAqvpKPvLCKpKaNAPYaBmy_mDESYLZ0y7OOC0qR_e-IP5ryKb-TIPjlPyqZvGolAwwxmzD9zbjJBjpUh4gfv_RYGBMhx8OwtiiVAWGm0jMGyYgNikIVAVRbTkzdBirQpwJHno6wuOMM8JW9Gmp_2YryhxVr9gPt9MzT3snHZK8EcdNFui2RkLIxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
|| بیشترین حضور در فینال در تاریخ جام‌جهانی:
🇩🇪
• آلمان — ۸ بار
🇦🇷
• آرژانتین — ۷ بار
🆕
🇧🇷
• برزیل — ۶ بار
🇮🇹
• ایتالیا — ۶ بار
🇫🇷
• فرانسه — ۴ بار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100403" target="_blank">📅 00:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100402">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6480a164be.mp4?token=pClEPsWVHVtjxjgKwrEzlXdRlrvsKjHdPkg9MsQJGIJ2GVhAOnP0HGX7gKwXlgPcT6HCC9jeyS3x1OzI1kh72290x74IZyyl9iRhjRzl7Zx5h0jxYevyWu7_3PJdQ4cenzPQqUagft2TVAT3-Hw-2g2BUhf8aopHwXo6ivoPUjkSu0U3FZjeUaA6PUnijptAlilUTl_ZUlZlXWSpFkkBXoQ2QhyN1qO9izyA04xa162UHA1zINkx9AOZZZpVKInt5Tn2OvaQckCMS8IjL-6pkS32wenN2PuLBn6F431z69O2HRU7ZUsVkULXNUiuTPJcbj-RvyqwSxWH4MgoWcVPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6480a164be.mp4?token=pClEPsWVHVtjxjgKwrEzlXdRlrvsKjHdPkg9MsQJGIJ2GVhAOnP0HGX7gKwXlgPcT6HCC9jeyS3x1OzI1kh72290x74IZyyl9iRhjRzl7Zx5h0jxYevyWu7_3PJdQ4cenzPQqUagft2TVAT3-Hw-2g2BUhf8aopHwXo6ivoPUjkSu0U3FZjeUaA6PUnijptAlilUTl_ZUlZlXWSpFkkBXoQ2QhyN1qO9izyA04xa162UHA1zINkx9AOZZZpVKInt5Tn2OvaQckCMS8IjL-6pkS32wenN2PuLBn6F431z69O2HRU7ZUsVkULXNUiuTPJcbj-RvyqwSxWH4MgoWcVPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
اسطوره لیونل‌مسی بعد صعود به فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100402" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hgb7ZUAR-M44nP8tzeTnQ-6vsTdW6MZDYzqjcMCErnYEJP892Ly9Q2x3VXqWrCSf454scxOCFdyiE1N3lGV7XfPMAJ8s-gGbVwSu_oYweERQUV3HyX_-n-TmgoNCltBsjbi2EVBO8JSbLrnc7UybjtqE88HtAYFrTpzg57uJLQjmDRrV4jzK38i2wQqM8EE65gpO-Nn7kN2p7_oCrHj7IIVYE2_du1nxVbTuh9ESJnKJ55aM3qXovYLcpWSDaLP-nXzylg5kyS0c3CE1eXLztQTR6la6mPTABkQ3DGC920lRS8bk3zccatZkBHqJaevRpsi0zHjmPtcfDsGoizfanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100401" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlLM6tThqMjl3FD4AUjlaokKBYlgtn0geUSOAm9oCP3HGVd98P4rZ9SYlQXQIYhfm-GbnP2lzZ9Lwct5p22YQ9RoHFdrEyeb8wdrIPolFSS7SQfgJm4gl1n8pQ7HtQN7hCHUjsVuwDvJyq59Dyp8YBY22xpRxhdtuWsTjdmOw_oQNAibD0OH_5Bo6XWC4R5gSP0qbyPUZ9-SO3J6IeJysnGRB6CZOHkyd6rPcGWvzQMmT6CF7UzDLv9dn3ZdrwxKkUzRS8zuSwBtGVvezJ20mhUFzuv_CqJsBBp53zUtrfLwvKbWc1CFpT3li0ewhi9YpXCs9fy3WeC0ogeTUBkI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
👋🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100400" target="_blank">📅 00:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPdOlh5ADUYnp5Z7u7TCAki-hiVcngPONR-1qxktCh5reBDGfPL2mvuXl3Cszpo0Sb3QxDL2Zyb4aFmJqJqtql1FptP04gNc54kBxO8E0vkeEJ9b5-d7UTNL3JRSRakRdM-E2rTlSOFgUiHhxR5ACb2-p4r7YJROPNc5dsp8yCTIRTjLq2ljPhrF4l8lMfDa3GUDrW6sDcvo7LneicCJ1PPChA0tXtNs8WSAKXXWdBy-j0ibV7bsk0ok6O5PHbowAmJHUkLyeVD9Zp5ud8OrmbpKIdDn1yJEfRAWdLNAh8s4DjjWcDCxQpl8sNyEPFRaBsM2UEAoNrAXt6ozr2z2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی، اسطوره فوتبال، با ۱۱ پاس گل، رکورددار بیشترین پاس گل در تاریخ جام جهانی شد.
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100399" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسطوره
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100398" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-OZAFtNMUFcATW8hMhCgs0yaN-qpl7cVQN9MD6VA3KESyPc0LjzelXliWH09FHyyad59r4CK1tXQvu018XHEaYm7eBAyB0vwvs44BXA2ku7bzbxZVoCamRYqNAd9_A0Gx5MCteoNkCRgxqoDkv1mjIgWL4R2DMTTXkKCRBDpmGXhrk0sbmy4QYD-QBaBhUfQz5kIBN6006GcDmTcrts1iqKypKbr13kX_7hZh9ilHOsgUCvPPPKMSx5QB8ocyzx1ItzAZrFB34RddOxlRl6J-lln80_Vq4KAIzzEqdsDkGS_Qbf-LjQiYsxglYyX-csrZAfIqPZl0YXPgYnQ985Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
#فوووووری
از ESPN: توپ‌طلا جام‌جهانی فوتبال به یامال یا لیونل‌مسی اهدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100397" target="_blank">📅 00:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOk-9WKgRRLzMSh16DyRLFG2Qw1ZOb4potPNZ87bKEAIrTP3XpJ_kyJh27_oGNgvwCb-omr-TDL0eonwU4AZ5MQ054ukd-4uDxsIFXtPUMT7eL8P1PDbDQc5ipc_xsqBShXgGTfW9HMKJ7zcZ1Gg4GpFjAp04hKctTVucdKgg-QgELdogq_wDcHMcVdnaWbYJc1AfFvWzqGrRnDj01YhtHuXu7IBzXe-UWx1JmmitEbtlBYHjjcF20bI09d3r82dhbMeH_S3txoG9Uz3sj0Ze91xSI5oDbwdBl4znQfhaMYRk3pNgPlaC67LngCtJkuM7Hq4wYX5V-TRKP4JtBlGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
آغوش هری‌کین و لیونل‌مسی بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100396" target="_blank">📅 00:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A53OgC5WMXZKzHIzZfQmNH-FmJcwo3iFYj2rRNpJ7K8hxpaALMN1TVWN7vbdQ4atCya2CTdNNDru03ukC4IBJikEdfdqGHULd-bhaHG0Dk-wVjlG3KF23bfwxmanNZH7wC7AHWDzcJFPH5x4kl0lOErbZc-dKjBH023x0fVpih5bE3GcNioSTaXkP0XdcxAwFfN1UeBXJohzakxg-V623pMPEf_JiXwIeU9fnoh5JJe3o7SqMrVyEgYYygHQ3izwV70yogJqEfhKiaXpUDCUE3uOuJ4jB0h4lMr_twiVmNuaeQLkXgsmjBTzXBX_fsOANbODTthW_H62qjZam_SLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100395" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lCoJzcEyvUQLUkUaZ05qsVNqcQsERKfFJ7FFDf659VhNzCeAhrHmfgkdclJCbFoYeHvRrKZJDq-r2jN5kfJDruqGfiVtmlT559zgqJwMd4BgNaq-NdyCcnZnvt_8EIdFXh83ER1L7Y3kWuqic4me5rhPhNWbx-zEtnQWDRDDqaCv6kkg2gwNryX-FzY4O-PPhf0U3cD9eMA2SaSqrCM-oOW_7O8yN6dAz8ylZSzyfgF5U8k2zl_MgAjiV9myezcYgJVscVkjSMun5KDVTTKLrT1GxZ49M0UAYGgPLuThj2xy9zlGCuHxmhA-Y6L3w9MygfOxZdHxuUvfMNOL0ZowBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه سر عالی فیفا به انگلیس
😍
😍
تیم ملی فیفا ۲ -- تموم دنیا ۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100394" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100393">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXPeqYJZuSlseAWM0341FWg5zxRLn-cdHvPGvkO7-sMHAlzRwIcS1mqky3NeVAMlbiEEiuhxu9TsuH7RhupnbcQ1ulp9I0yVOHaHkbR3UrDOvmNIU_Qosn9QbGWVSBZVvoD2JwjKl4biL9ccNQc2bNZ_6yFs3cFTFjNpCjC8bxUwnUThwEpqDPOr7CpUxpOU9FJx4n-TYJ60JzQnBWyGVcDfy2cnQI5SNKnbJwgzp9mKmG6bOviaObYEQ5IQvAtid9imx1mavI0wN3EdKbd7ocPm50eq5NR1JwKZ9S8yQ-wEdTiPbCXRPeTyaD5rSYb5nk0FihEQnIcABRiapW838Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100393" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
خلیل البلوشی:
- فینال بین آرژانتین و اسپانیا، چه کابوسی برای برخی از افراد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100391" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIiWRWtjon3wpEbJz45GGemyz4q7yYVl0M5PA6Um1RlilcDMYG1l02PNFskn3xPLsXP9Z7ykBQLDSo2P3BoDIgPBmy_rURZxq_dWqModop1KL6kzI9CFlOyz-LafhRjZmfgC9yr51vw_rUjug_c6AtQkR7ru3p4x34VqHZOrBBV2zrBxX9YZBHpKAfev13GvPssxgF2Sx_uBip5qYgWckyK-5J325ZnaEwzCpXRcsF2xMSUcjFVapqSV1eJGSyIXVQ9LxnBy751O5Kx9a7ik0icqrlS1_7C9VJOynQlrcNa0rxWr8uO13R2RyolH81xOoAqpj5D6XWGPQfvBoD7Czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|ادای احترام جهان به اسطوره مسی و آرژانتین؛ نمایش درخشان مقابل تیم انگلیس؛ اسکالونی و تیمش برای دومین بار پیاپی راهی فینال جام‌جهانی شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100390" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">زندگییییییییی به کامممممه اقایووووون</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100389" target="_blank">📅 00:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iFsrXAi8DnRV8MgdmIDeMJplDWXJ9je0CzS7O79wbcREl9Ic-8s-_U97YZyLyyrDyJ5ADkVeM7CaoButTdbVCZ9C0y0hfLRATnPn887NbC4h4g1zTpdovTP_j7v34a3A3ENkFFyisHwkjxtIeKXoTTtmxdBTgNBd_N-MAjrfFVNySr7JYxadv-UcrAcdl6mHf4iQiwak7VBORrAZ3ig_tuCHAvQscsBOBBSttVpUoKKd3p6Y6Bmr56XREd8ZnNaH_TJI3J_bolsYCDUIYd4YpcqJ95CQVo55rARspsQx7EvQHY5sTjdfUmSiZ7pj9r_H212c6cT4HU1SAy37CrVXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی|ادای احترام جهان به اسطوره مسی و آرژانتین؛ نمایش درخشان مقابل تیم انگلیس؛ اسکالونی و تیمش برای دومین بار پیاپی راهی فینال جام‌جهانی شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100388" target="_blank">📅 00:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXBvoAhuPghu2i8sKLtj1qWkEdYQMbI3HRn2DyFGNIhXHooaSleYsO4Kazu4HTHzvW7HDnmtElpuyAjlZz6TvSQygGYCR1_zl-74qcdNWKUQ8dZVH4OW7az0tnCq040pBnMMSXf2kkhGP19RxWs2Tw98xgAhMRHaMZGCSWv5aM0u31zInzc00n8NfvWiomiqyGnIx7cZvfbIJ0nusyFeQGPUGfbs5XFVkFllsZQ0uYLaMINe2sDTv-PqS5PP5uglJufFnctv2wB37LadUxNy8ybjHJQLDoFgZnt5sskVns3L0MxiQPJ7y0zaGCjzEDHjY7sMhH3N28L0KpdgaAoyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت مسی از دقیقه 80:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100387" target="_blank">📅 00:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">توخل حالا میتونه پرویز مظلومی استایل ده دوازده تا دفاع دیگه بیاره داخل</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100385" target="_blank">📅 00:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کسخار انگلیسی جماعت</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100384" target="_blank">📅 00:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حاله وقتشه امیرعلی ۹ ساله از کرج بیاد هشتگ پسرفیفا بزنه
🤡
🤡
🤡</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100383" target="_blank">📅 00:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">میگما ؟
تا الان که ناداوری چیزی نبوده ؟</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100382" target="_blank">📅 00:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🔥
گل‌دوم آرژانتین توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100381" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اسپید کیت انگلیس پوشیده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100380" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مسی: من به اینا نمیبازم.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/100379" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100377">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/591054bccf.mp4?token=azCfbjGphhktPMSQwMHa4bsXwnKRkQrvY40IcjxdRj5hee_Ewc4d0NfROLzNix5sM_nGgZWMp9w-Hg0LcHUYnIdj_fWGHAU1TvrUnQUIz9_wLz4FcAUZ_bdj6gBiJKQZJnGjniyK3F78eMQt0LR3FmBxteTNhSXCbPWRXIfdFqO0-fP7vJrDUBKiEQ0ktBLycUoqGNmS2_4LftHe4sknHgKPOVyxJQ6LX9GxeiStyeVy1Gxp79IYFEZkKzI2bFvQkH2Ow4uBjFXDgFrkX65K2nox7fFPIw0afG2T6lg6ZUsYhXoPg6IpdyKwXOLAlWopOIB0cacvAVwv4TB3RpPjwxN76iD_l2ScR-i9ZBjXLPrZx6mcur1_06MoGM7gUT3cnwhhk5tzUQdgVW6-SpMQsHlRChx2KFmg8kdzzRPJA8BMaNMuCbAC96RnmyK9OWiGzSCk3dZbwVIF9zMxNbj8qfT-T35dEdsPooNT_mV746zhTNKbF5Zt2VqG116dF2wT_sr6CJJoyoEIx2kqaSC2npCjBXqFy69MDaEtHRrQeqTcO1I7-4zHJrUbLfw46A0FbOn9aea-Rlx-DkraK662opd7fPp05oOrTOZ4ajBHagjDJq1RNtX40vgXUQz5pJwJJKzeqGOjKTbrkLL5olsBmp2NojCMeL_LMaybs3W82UE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/591054bccf.mp4?token=azCfbjGphhktPMSQwMHa4bsXwnKRkQrvY40IcjxdRj5hee_Ewc4d0NfROLzNix5sM_nGgZWMp9w-Hg0LcHUYnIdj_fWGHAU1TvrUnQUIz9_wLz4FcAUZ_bdj6gBiJKQZJnGjniyK3F78eMQt0LR3FmBxteTNhSXCbPWRXIfdFqO0-fP7vJrDUBKiEQ0ktBLycUoqGNmS2_4LftHe4sknHgKPOVyxJQ6LX9GxeiStyeVy1Gxp79IYFEZkKzI2bFvQkH2Ow4uBjFXDgFrkX65K2nox7fFPIw0afG2T6lg6ZUsYhXoPg6IpdyKwXOLAlWopOIB0cacvAVwv4TB3RpPjwxN76iD_l2ScR-i9ZBjXLPrZx6mcur1_06MoGM7gUT3cnwhhk5tzUQdgVW6-SpMQsHlRChx2KFmg8kdzzRPJA8BMaNMuCbAC96RnmyK9OWiGzSCk3dZbwVIF9zMxNbj8qfT-T35dEdsPooNT_mV746zhTNKbF5Zt2VqG116dF2wT_sr6CJJoyoEIx2kqaSC2npCjBXqFy69MDaEtHRrQeqTcO1I7-4zHJrUbLfw46A0FbOn9aea-Rlx-DkraK662opd7fPp05oOrTOZ4ajBHagjDJq1RNtX40vgXUQz5pJwJJKzeqGOjKTbrkLL5olsBmp2NojCMeL_LMaybs3W82UE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
گل‌دوم آرژانتین توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100377" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100376">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لایوتارووووووووون</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100376" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100375">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100375" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100374">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">چه فوتبالییییییی</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/100374" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100373">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یاااااااااا خدااااا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100373" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100372">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ایننننن مسییییییییه اییییننننته مسیییییییی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100372" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100371">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یاااا خداااااا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100371" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
