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
<img src="https://cdn4.telesco.pe/file/qHrhrOlJW0Ab8yBq6dj5CaDMG2WCOrGwMTsCnStIBblnmtpFKlb4tVx5X_UREvm12D95-Qm2Zhr6H_m8XqUi94mW8ffk3ux6fBYWFgISoqq8P01jvOA2zfGfXdTAedF05Yqz6H8vG9fHwlynwFQStGRNGEOwLgyP23uJguvMsCMFjWwqPpXcuGPx4dpaYuFgYcpukv6KBTddlkcFgjnic-GMoes9Q-RQK0FwmYlOUruous5t88J_qQ7r6t5GGunADraZm3m0rFtI31fdTDRAwPB2ABtA7LACC_OPcc-S_fRDESWeQJcMDjZ6jRoI7q_8hQ3ALopkwCMfN6cwqP0u8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 220K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 00:48:02</div>
<hr>

<div class="tg-post" id="msg-66703">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=ZSeJPAWYejX_mmcXmu0FceC-6awamHCwUUJMaHOe8oFEroPcRjjvKA79hPA0xkqCII2SjETEw2dNhFZvBan3wXnNwIMFaYSgKg8wD7F0goM79Rmsa_L3SDF47YprZnTg_rQDUWfLbvwFssaMXHZ-CE6ZMyXWmVxFgPlEG09nPO-BOWUxnkPq5B1kdt_HD2oxsHmvlJujuiHXbwb9Qq-MYw5YmG74_brOBMcRcARHUyHt4T28y_HIfA67AVKv7a5bmw8z_lQLFkgdSzyqDbKMIPwV0kZ4uKi6IHzjBZGEEVewJtoMlDs740avcenyTqx_30QS4vow3qejlZn1ETn6qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e034e891cb.mp4?token=ZSeJPAWYejX_mmcXmu0FceC-6awamHCwUUJMaHOe8oFEroPcRjjvKA79hPA0xkqCII2SjETEw2dNhFZvBan3wXnNwIMFaYSgKg8wD7F0goM79Rmsa_L3SDF47YprZnTg_rQDUWfLbvwFssaMXHZ-CE6ZMyXWmVxFgPlEG09nPO-BOWUxnkPq5B1kdt_HD2oxsHmvlJujuiHXbwb9Qq-MYw5YmG74_brOBMcRcARHUyHt4T28y_HIfA67AVKv7a5bmw8z_lQLFkgdSzyqDbKMIPwV0kZ4uKi6IHzjBZGEEVewJtoMlDs740avcenyTqx_30QS4vow3qejlZn1ETn6qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏قالیباف:
به خواست خدا، حاکمیت ملی لبنان بر کل قلمرو خود در این مذاکرات به یک راه‌حل نهایی خواهد رسید و تا زمانی که این اتفاق نیفتد، ما آنها را رها نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/news_hut/66703" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=SI2zcZjK0KDOQZq8tqz6Y3ke2_XIBC4BiZW9bFEtHMuNv4OPIzCTaObWgim4D8lt-GrcL14UjKHC4J0wjCfL01cwcPiXlHCpQspYiA6wVJ9VHtaHPanULvmIcWteVvAN38kUvY4l-9zvsFV7TpWN_u386kRxKTPqRIp6H5kA-Cvov4hgT21Hqlum9CdAH7W_7gnzT4UnOcOAeo0M_BvUH81BLnWmfA-NQkOHvesFBqwoJAuQ9sY7rHQPGaaFEa6Vvbg1AGVBZn3h9Ll-eIMTTDASgoppSZZYUwEv5fxIgKRecPfEiPs2wxklDxbpoezJ7Ez_sC_HNpVx-cIOGS_4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf0726b2f.mp4?token=SI2zcZjK0KDOQZq8tqz6Y3ke2_XIBC4BiZW9bFEtHMuNv4OPIzCTaObWgim4D8lt-GrcL14UjKHC4J0wjCfL01cwcPiXlHCpQspYiA6wVJ9VHtaHPanULvmIcWteVvAN38kUvY4l-9zvsFV7TpWN_u386kRxKTPqRIp6H5kA-Cvov4hgT21Hqlum9CdAH7W_7gnzT4UnOcOAeo0M_BvUH81BLnWmfA-NQkOHvesFBqwoJAuQ9sY7rHQPGaaFEa6Vvbg1AGVBZn3h9Ll-eIMTTDASgoppSZZYUwEv5fxIgKRecPfEiPs2wxklDxbpoezJ7Ez_sC_HNpVx-cIOGS_4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور تانکهای مرکاوا اسرائیل در حومه نبطیه
@News_Hut</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/news_hut/66702" target="_blank">📅 23:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66701">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146941c66e.mp4?token=tvVJPVTsBHivtFdFeYAEvPeGFVNckRuN7bWz1gpZbajKI670afA2nO30tKhuJ3q6vO2PXUAeMMwFkNLvTPCJwQcPsr6WbMqldYXa8BiE77XYMvO-JUu2q36g3Q--3hYD67L_-9Xv6Oh5YN6KODdkGxysYtUAbQr1t2NvNoqmbt_qF2vUvcSyDzlLR56OZ6dgH-URyXdW7tvetWAXtYiiuJZhpCRBFTCYD6BcLwOq0bDBT7wgxV8QYJcY1jbYg2_BBiQj2uRepCrS2aLan00TFhOK3lgYuvYdOd4eHt4LdQ8dfS1QGy2dJkVnm5lRIyQqoje5i6YYe3pE-ICLHf7TFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146941c66e.mp4?token=tvVJPVTsBHivtFdFeYAEvPeGFVNckRuN7bWz1gpZbajKI670afA2nO30tKhuJ3q6vO2PXUAeMMwFkNLvTPCJwQcPsr6WbMqldYXa8BiE77XYMvO-JUu2q36g3Q--3hYD67L_-9Xv6Oh5YN6KODdkGxysYtUAbQr1t2NvNoqmbt_qF2vUvcSyDzlLR56OZ6dgH-URyXdW7tvetWAXtYiiuJZhpCRBFTCYD6BcLwOq0bDBT7wgxV8QYJcY1jbYg2_BBiQj2uRepCrS2aLan00TFhOK3lgYuvYdOd4eHt4LdQ8dfS1QGy2dJkVnm5lRIyQqoje5i6YYe3pE-ICLHf7TFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعتراف
کارشناس صداوسیما: نتانیاهو خسته نشده،این یعنی مرد»
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/66701" target="_blank">📅 23:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66700">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06705953.mp4?token=t1dZevpQy4-3kFOX5XSMSZbJp0d0uWnZ3NibUKVydYlkUoa4VSP21AgO8Ny7s85_ZXTSnVCRq-R61PL48MibhSGJkwty-FzH9kZCNHYEVhJRBfpDMO7kbg5sNIDxnYPh-DOA29tcBFu2LcAbGCRrQTpmC51huTLx1RQhmlH7mQLgj5PF2YgR54eXLqH3v_wV4gn1RJLVNVV6ZwByrP3rZaJnoBtzuKB59LihxNhOPMDZbUmYBKf9FV9qHAW4k_Z6s1eOhbtiQ0Viebw2eQA5q-HLrCwHG33xafvbFdr7JjNY-HIz6jkHnfnjRMnZ2cG1l51et1JwQ8TyP6r0laq6lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06705953.mp4?token=t1dZevpQy4-3kFOX5XSMSZbJp0d0uWnZ3NibUKVydYlkUoa4VSP21AgO8Ny7s85_ZXTSnVCRq-R61PL48MibhSGJkwty-FzH9kZCNHYEVhJRBfpDMO7kbg5sNIDxnYPh-DOA29tcBFu2LcAbGCRrQTpmC51huTLx1RQhmlH7mQLgj5PF2YgR54eXLqH3v_wV4gn1RJLVNVV6ZwByrP3rZaJnoBtzuKB59LihxNhOPMDZbUmYBKf9FV9qHAW4k_Z6s1eOhbtiQ0Viebw2eQA5q-HLrCwHG33xafvbFdr7JjNY-HIz6jkHnfnjRMnZ2cG1l51et1JwQ8TyP6r0laq6lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏اوکراین یک کارخانه تولید تجهیزات الکترونیکی نظامی و واحدهای تأمین انرژی سامانه های موشکی و راداری روسیه را در شهر ورونژ در جنوب غربی روسیه با موشک های بالیستیک هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66700" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Uyo9jSJgr9j9cm-5aCWRy1gZD2-W9qcPDLhO8kt8EOs9v06UHjM9Xvt-oRg0GRFjqhNsYQpdpGCPWe2urj4Hi5M0acHaw_3cdxvpYSaxCsztpHTKwWV_6R056FpEXhCM9188guQoYslJdgXFySWEYnHtpu5ET8kzkSmH8bxcV2MNxYzt1K3CEum2M-hYIN36hnWPmQ5ugyj7i54suEfExTcddKLrjQpdYK1KLKEwhw5iQJYfiU3X41Nbe5VC0LJrFDoreXxgSbKHQxGFzuKPJib7uGbat-3jRM6oP4VXLZ59dJHdWA1O-QMhFFpPOAzxbR3LNzlSbx8JaCqSLcQi5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee51609a91.mp4?token=Uyo9jSJgr9j9cm-5aCWRy1gZD2-W9qcPDLhO8kt8EOs9v06UHjM9Xvt-oRg0GRFjqhNsYQpdpGCPWe2urj4Hi5M0acHaw_3cdxvpYSaxCsztpHTKwWV_6R056FpEXhCM9188guQoYslJdgXFySWEYnHtpu5ET8kzkSmH8bxcV2MNxYzt1K3CEum2M-hYIN36hnWPmQ5ugyj7i54suEfExTcddKLrjQpdYK1KLKEwhw5iQJYfiU3X41Nbe5VC0LJrFDoreXxgSbKHQxGFzuKPJib7uGbat-3jRM6oP4VXLZ59dJHdWA1O-QMhFFpPOAzxbR3LNzlSbx8JaCqSLcQi5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صداوسیما:
نه تنها از کشتی ها در این شصت روز عوارض نمیگیریم بلکه قراره آمریکایی ها بعد شصت روز بیان و عوارض بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66699" target="_blank">📅 22:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ2pzI2L0dSN8noSw4PxmgeUWvKIsnbwheIGerPaxH-jWyCMxblzRQn4JQj5I8EqxKUL3I8NEBF5_7DB41_EZddEI_uvkoTfe6L-poPcLJ1NHMyXxhLZV1SZxarybDH2IsVdmOi3vQvJzY_MJ8Dj20EpqjMpP8qF25FfmcPspbxGsMm76tFEEgm46Zid5Iqw0M514hb6EkjFvldbJbgM3OzJYAaxcS1ajx8fgBpGETb0DU15J1Q_F4HTIe7Hj9PrFrvSYtdl65os4nJh-M7DOgveIYircOOrMZORzixlmVS3OKmCAiLvCfMOfOUACTdHJe4uO4YLKchuCIB3ykxyBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
وزارت امور خارجه آمریکا تایید کرد مارکو روبیو از ۲۳تا۲۵ژوئن به امارات، کویت و بحرین سفر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66698" target="_blank">📅 21:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9z7qKWIcEkUBmMXMKJx3UK2aCFnvu9hvPL6I3lTVbw_KRwA_-t1BfoR6KF6PWllDJkwlXWy7WIxbwQ733e6QawxKAmvM1qMsIuvqk4ns68TimXaamLoOI6wwgBRa07R4k89cQeISs4-YM7yhoMDzrb9XUP09nN5RJhEmNJ-M_ZCjbHlDkZP5RjrBtPrJGF3UEip51ISbLDze2dB8cH58eyUgS1AYCceVJRC8NI58yoJ2gUMcUW1yFGAcSeAckHp6jGFyKyXmzLxV_KgBwlThLeKF5fZuNVqlbQ8JqseCOCxvfcC07bQrL-LqXz5UxewUtoEvEv1hU142AILI52SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA6jrcoWfgfd8qtqEp8Xyv1bE21ouQg_m5nBzGjCDTdcx-SFMvqdiDvJ4uy7erpF3So5-zjOIKa08uM_BDEIvCndNDY7Vwy8Va72-x-cUENfJTU9XlJ7RzRKH3i7Oxsl3rGzyAKsfGUU_p3z5FtAQDU2KwDAoTPkiMyN8GTmvIc5JeMuW6_R7k_HnS2-E76XIPArBkNHbKiS8JmaVkUWZGEmiJoJdbdWJEpuZCS0tCjX0NC0mFlC3qmLslfqdXBriPQfwsx3THG65EVDbHLZGxNqpuuZwl4n5ViQBp5XAJqkE7rE_P4k_wJ5a7Z7ujCKVGWJqwIPegyKp8O8yIV8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR1eyaN3aN6ortsUIyV6zrmNQebPn95xsQFpIzbW1H0sHRdIrPSGXl3BarTzsEGG7MbCCxc8LkQt9ERXIpRkcRqTcyNX7XJDITPmOaQlaTf_YlYOsqYDMmnESGo5c05g5FfG5ZHQO9aFBK6oCaxKcPv-5P_w2Iq1L8TSj6segIxzzNLO4AKVsehHfhi63zPaDfamyFqJCpMmSQqgxlKCbUzGDaLJIegxB7n3owEelrL-_3h6jne96jQl2kPRrG4P2mlqIoTdww7OceYM-NdnUyTsT7SwlLTW1NFK5MfKLeG6UWX18fOcXFYoUdYSrDBKJVpODzahr6wiGSRTzVLaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTYBJZaaKWwHHlRR1ggS9ygCVUWi98mSlYbLJK_8zaAT2vaLN-E7mYJhT54tprgZ-vlIGQikCD8wRvKp7CO3wQilMj7pDT5E9ULAZxpCW_foACcqOWpD-zET3FwdHP4R-HRDaO5mX1f1vgGXR0jaykVD2lJiOwEIVZn7YRVgGZ-v_PbUlwL1O2Szl1FEIRXBKiqGqT2FfTM1DPMdAj1iXfQPEM47wI5DuPZoRZ2Y-e6DV2oUs2eaZ-OTL3TVAXM6BV5XcDpwQNSjz7m0vvAteoRGNo-q7ORj8oBCE9rw7tNNF03o3qBcK0XHj-rOOMcZrJ53Tx9Pb1G4a8X83PvWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLIcb079eswKtesbqB2R1k_Xz1qk1yxZIzItS0WV-1HUy2yKLPiPE6RVDWUPjKfQV9j66UTKjUWo4aSiEJXv1-45daLlYiJYBwLqasysZUVAo5XEOcGLIKXfMl004KVRRfKG58GGwKtslMJbsNX-6W7vBr0TKGThJ8PgHCvkpPx7czLjGrn0sxfYjIXYy8LyDdbSZhcD94yJyKcGrathnIbFMXHlkrsbzqbRPiS9tZPu_U8FAR5D3QihMnauGeAHGWl3_AjPMUKlE9EHRvqEWHffXj9-3uekI7F4qFaRuT4XExXxknLxB2-GVEm-1FamQJLkRijBB4Uf5D51kG0F3wnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLIcb079eswKtesbqB2R1k_Xz1qk1yxZIzItS0WV-1HUy2yKLPiPE6RVDWUPjKfQV9j66UTKjUWo4aSiEJXv1-45daLlYiJYBwLqasysZUVAo5XEOcGLIKXfMl004KVRRfKG58GGwKtslMJbsNX-6W7vBr0TKGThJ8PgHCvkpPx7czLjGrn0sxfYjIXYy8LyDdbSZhcD94yJyKcGrathnIbFMXHlkrsbzqbRPiS9tZPu_U8FAR5D3QihMnauGeAHGWl3_AjPMUKlE9EHRvqEWHffXj9-3uekI7F4qFaRuT4XExXxknLxB2-GVEm-1FamQJLkRijBB4Uf5D51kG0F3wnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=lIwb6I9SaEDnykDgqa4njzngfgnsIyn1ooCuo9E7iUD_ZEotouJN0wv5TcYdR9izQbhf3QEpDsYrS67x3mcPmA0Etz-d890EifyTy3aHL4HvepD7XVsKjJtXiXCay4gckpBz30Wk9EUknXFspw2So1mEI4KQRYYtHSFdL2xkdPygLin6QtIehegO3--V47d8D8Cx6r_mHRuvVHEiht4tqUONRbjcnRmyE0igtYsazDtufIUBXej1q3IMopb5Ol2yHvzSNDQKzGSHkizla17vwWcAMbFgb1xG2Jf8vrdf_XA-66-4bN3G-ql7P4sK8m6A1qZnxyVzNIdJdZn9AkBhyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=lIwb6I9SaEDnykDgqa4njzngfgnsIyn1ooCuo9E7iUD_ZEotouJN0wv5TcYdR9izQbhf3QEpDsYrS67x3mcPmA0Etz-d890EifyTy3aHL4HvepD7XVsKjJtXiXCay4gckpBz30Wk9EUknXFspw2So1mEI4KQRYYtHSFdL2xkdPygLin6QtIehegO3--V47d8D8Cx6r_mHRuvVHEiht4tqUONRbjcnRmyE0igtYsazDtufIUBXej1q3IMopb5Ol2yHvzSNDQKzGSHkizla17vwWcAMbFgb1xG2Jf8vrdf_XA-66-4bN3G-ql7P4sK8m6A1qZnxyVzNIdJdZn9AkBhyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=UD8g0fFrwBB1Qq0Di9cj4eqh2O4kzmi0ntlRIG8IiTee0vAOIEXHf88RWAp0DJEmrYDEYIpH3SjX0p7pVHD9HzdU_B2Rmsaz_WhkxaOrGtKo9CGIF1po911hsp9F13wrY2K9ABDs2ateuAh3WkJ26RJMtAS1eR2NtB-MkWdEDGB2frmXASao63SMVjcslwxsifpe9v2GlJfsWK69tMNxRNEOUj7tNWWekcuYaPSxjYacOkCWXb7Lg-ZdJ0MN9HvKtc_X9ybjJ4XFa7KuUuJsaogBOQAHL6F-3FZHMMqG4rMALvddQ03OsS6KPn9jAmFLnUc1iyd8ZGELX5KWslNEtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=UD8g0fFrwBB1Qq0Di9cj4eqh2O4kzmi0ntlRIG8IiTee0vAOIEXHf88RWAp0DJEmrYDEYIpH3SjX0p7pVHD9HzdU_B2Rmsaz_WhkxaOrGtKo9CGIF1po911hsp9F13wrY2K9ABDs2ateuAh3WkJ26RJMtAS1eR2NtB-MkWdEDGB2frmXASao63SMVjcslwxsifpe9v2GlJfsWK69tMNxRNEOUj7tNWWekcuYaPSxjYacOkCWXb7Lg-ZdJ0MN9HvKtc_X9ybjJ4XFa7KuUuJsaogBOQAHL6F-3FZHMMqG4rMALvddQ03OsS6KPn9jAmFLnUc1iyd8ZGELX5KWslNEtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=E6yvgStXYyOAQ6b6LEL8XAm3T_M51wL8_s3dT4GpvOy5rk7wL8OEkD-Xbjlehg_7B9qGKJv7mq8-JwzPyH6PR9rcX7FQ0_cG0wB0AGms6JVFFsgxd1e_4pRFaSCjCrHBjuS2Gj4oMOBRKupPBUU5MnJfP-6Qzts1yAjitllLGPcWvOsv1kfxIiTk915PMoS1FwdJk7Y6Cu4rCWH6Mo9F31_pmnOAILXFEvSU2krxwe3IWetzlAjd9O_2ivd1w0hbVQwOO_OQFwqFTnX4xbq3GcodFnwdZpi0xK50P9fK9U80fJOGR0bQ3K85NBHIA9ptzlFd6Kstavgxx1o5XV5u6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=E6yvgStXYyOAQ6b6LEL8XAm3T_M51wL8_s3dT4GpvOy5rk7wL8OEkD-Xbjlehg_7B9qGKJv7mq8-JwzPyH6PR9rcX7FQ0_cG0wB0AGms6JVFFsgxd1e_4pRFaSCjCrHBjuS2Gj4oMOBRKupPBUU5MnJfP-6Qzts1yAjitllLGPcWvOsv1kfxIiTk915PMoS1FwdJk7Y6Cu4rCWH6Mo9F31_pmnOAILXFEvSU2krxwe3IWetzlAjd9O_2ivd1w0hbVQwOO_OQFwqFTnX4xbq3GcodFnwdZpi0xK50P9fK9U80fJOGR0bQ3K85NBHIA9ptzlFd6Kstavgxx1o5XV5u6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPphgGDYYPwxvynwc1mAP-uWgqsbsDQi4dTdBhvHZiPZWuyke622u5XnUVXzCDZYmZSEJW_czeIsEPNR_Lpsmkw1l0c5P_rvwMuRxmHzh-3MYRJF3hVxGXdtofP3aJ9CMFu4cBB9kG1KE_dWVl-qOOo3zAEqU1Oai6HvAJ1mh9Cvar70baXCkHvxPKuLSZydwWdPVGCUhYOiZEVZJsecEbFv92adahyEi3SHkqvWYr4hIzG_fhTU6BQarN8aoAAzYynoDElGZe2bc_AGyxjbDUwSe84x_m7O3Nm0PULlSI7Qrom08Xj0Ncn7hV_py-iu4Ia1A6N9StvuFMuVFDiGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SgssrHGb5RYz-UDGMJLywv87tvAFsXClqBujbq4O7uXNU8v9uUyoIObQxCGdTtjA9giFRhmlYOGZJaoJkx2ilJNRz8U7GbvWGuSmeJoqfk_jqF9UJukVjwh-zcuIeUgAYW1dgVuYwGLQ3VCxxRTzb3ebLz_2I6i5nM0M96y3jdSwftlu0_EwTtSB6dxSJnmNEkLmGTAEHsem25U-qHpsTkAN9-o23rCzjJ37FzLa6CFo37IDJWGiQSXqjxy_rjGdGHJlDu4XoZ03xHiy7YICBN0cNB1xydkHdXymXQdqYWVBm6iwR4JejKAqgw18ybHyXw1yLZ1Skyz_ggBP-M1mQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SgssrHGb5RYz-UDGMJLywv87tvAFsXClqBujbq4O7uXNU8v9uUyoIObQxCGdTtjA9giFRhmlYOGZJaoJkx2ilJNRz8U7GbvWGuSmeJoqfk_jqF9UJukVjwh-zcuIeUgAYW1dgVuYwGLQ3VCxxRTzb3ebLz_2I6i5nM0M96y3jdSwftlu0_EwTtSB6dxSJnmNEkLmGTAEHsem25U-qHpsTkAN9-o23rCzjJ37FzLa6CFo37IDJWGiQSXqjxy_rjGdGHJlDu4XoZ03xHiy7YICBN0cNB1xydkHdXymXQdqYWVBm6iwR4JejKAqgw18ybHyXw1yLZ1Skyz_ggBP-M1mQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=mjJZyWWtAreVtP6netfGvZtPA7Yp8iTR-xUc73kFP0hAz39Mpa30RZpgQR6bDPK9E36oYsozsnSN4E2e2VA36ydFHc9_LVbyMfFn7pkJXbz62uZCEiyZaORL-68zqAGUOzG_qFs7K9KqYlQTwEFoNmzCWjr5ntI-QBtMzq5KQ0fpcV1PgqwwSxdnEFqxNwQQVty45V065z6d_L-Fv9tNtNIsPc1zwE7VcPbQRmenHi2F58BwreTT1Ytb7zd-YPe6hADFCrPABAztAIbc9u6jg0EgsFvXwXaYVvPF0FBcC1DBhfvFZYmmaSj7rT3U0JP_-w9BJ2U3jHJcRLfs7S2UYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=mjJZyWWtAreVtP6netfGvZtPA7Yp8iTR-xUc73kFP0hAz39Mpa30RZpgQR6bDPK9E36oYsozsnSN4E2e2VA36ydFHc9_LVbyMfFn7pkJXbz62uZCEiyZaORL-68zqAGUOzG_qFs7K9KqYlQTwEFoNmzCWjr5ntI-QBtMzq5KQ0fpcV1PgqwwSxdnEFqxNwQQVty45V065z6d_L-Fv9tNtNIsPc1zwE7VcPbQRmenHi2F58BwreTT1Ytb7zd-YPe6hADFCrPABAztAIbc9u6jg0EgsFvXwXaYVvPF0FBcC1DBhfvFZYmmaSj7rT3U0JP_-w9BJ2U3jHJcRLfs7S2UYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=vc2Z4H_N7uRViLHuHXDPIvnp0ndF9Pa09bipebRW8qmmdtSDvjWaQHhTED3h-5TOyQWH7H7v1QjKiOHxYm8dZbfYcpd7CXzKvKLCy_U9rEBzH_doPR7gUEwUq3sIcDW40vZPsi-Gv2pVm49LcE3EMuxwHp8maRNic6TGNLbpI1t1YRdhr7u8NCD6ja8TiE_rbFOqXdF2sbfbGxKp_6HR4suzxzdu7DfrBDgnrAeYjdcopmEFYgjJsR-BKmMNu9kmm1lOiAdvEZ5ALCa2LLaUGFDjMWVheY6RxunOC58NOF31Y0Ibs23t6FE3ih5qGOe9JfqIn7xT_bSNFzgxJoBcdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=vc2Z4H_N7uRViLHuHXDPIvnp0ndF9Pa09bipebRW8qmmdtSDvjWaQHhTED3h-5TOyQWH7H7v1QjKiOHxYm8dZbfYcpd7CXzKvKLCy_U9rEBzH_doPR7gUEwUq3sIcDW40vZPsi-Gv2pVm49LcE3EMuxwHp8maRNic6TGNLbpI1t1YRdhr7u8NCD6ja8TiE_rbFOqXdF2sbfbGxKp_6HR4suzxzdu7DfrBDgnrAeYjdcopmEFYgjJsR-BKmMNu9kmm1lOiAdvEZ5ALCa2LLaUGFDjMWVheY6RxunOC58NOF31Y0Ibs23t6FE3ih5qGOe9JfqIn7xT_bSNFzgxJoBcdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=BE1YWs3fPocWJjO-jQ_c8W97TT-zFqBz4HP3Zfxexr8EZXpR13kWmh-blU1uoKqW_fBO80oeq_P7snRNqT6t6luhlJpeuokIKS0BDYsBK7OzLOzpWWl2CPfhtt5skf2UDv-FiA-rBrp5JR6M7BulUCCwVjk15kUSitfotDvCiOeJ_8NOiRM7yLniQURCpgxmg61GThGR_laueJU0mUA2OF6iNXO8gDEgJS05of8ZZictbxkM96oxz4G7c0fZsg4DqlH3e_QXwEqBskI4tXH6Sj13xoO7Ep8VpY-k1QmNyNj5FlAytkm-l_OvPXu6fV7Y40vFRYDrHxTqnV-vQpwHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=BE1YWs3fPocWJjO-jQ_c8W97TT-zFqBz4HP3Zfxexr8EZXpR13kWmh-blU1uoKqW_fBO80oeq_P7snRNqT6t6luhlJpeuokIKS0BDYsBK7OzLOzpWWl2CPfhtt5skf2UDv-FiA-rBrp5JR6M7BulUCCwVjk15kUSitfotDvCiOeJ_8NOiRM7yLniQURCpgxmg61GThGR_laueJU0mUA2OF6iNXO8gDEgJS05of8ZZictbxkM96oxz4G7c0fZsg4DqlH3e_QXwEqBskI4tXH6Sj13xoO7Ep8VpY-k1QmNyNj5FlAytkm-l_OvPXu6fV7Y40vFRYDrHxTqnV-vQpwHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=MF41eBNo3ap0kHk8gLoM5XZ-5AHjKtpU_gLKqWzyhOS3gIFiW7k4SoSHvkhh8dRv3vfoXaK7dA_NBYbPqQQ6yBGBiZXR2VZYpB5juAwohFejjHlm4lr1I-ncZkfqh9lfZtSz-JX2Jt7i8wG8_Jyrkozjgnd6RxxySVxUeUclPCAcQ1-U5wsoA2ZfLfWFkGVX6wMMmnlbtQB09I4s9rRRgJmkoQ34fytQvD1Vi9N3zeXu04F-dS-LlIcF5l_3JIGRUlM7vjTSZB1PT5uBB_zqk9-RcouGwaA1JEQ3wkTMZkuMdl1KBAelrs7IQlXXMi2QCQOTX8z4F5x0wcAhZK9uBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=MF41eBNo3ap0kHk8gLoM5XZ-5AHjKtpU_gLKqWzyhOS3gIFiW7k4SoSHvkhh8dRv3vfoXaK7dA_NBYbPqQQ6yBGBiZXR2VZYpB5juAwohFejjHlm4lr1I-ncZkfqh9lfZtSz-JX2Jt7i8wG8_Jyrkozjgnd6RxxySVxUeUclPCAcQ1-U5wsoA2ZfLfWFkGVX6wMMmnlbtQB09I4s9rRRgJmkoQ34fytQvD1Vi9N3zeXu04F-dS-LlIcF5l_3JIGRUlM7vjTSZB1PT5uBB_zqk9-RcouGwaA1JEQ3wkTMZkuMdl1KBAelrs7IQlXXMi2QCQOTX8z4F5x0wcAhZK9uBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymq14t1KU6rftUVtB5W0Yb8TRhs1j8dFBCrSzRIwN5oztsqEE8hzYuue87CnabzoUN2Y6mv2Ty8zij6IBXOp-1oj-pFKgpnNoWVawVz_P_ehwjYVEOB3g6nHM-ssREww4-JBadio5okNJnHlU2hpOWRQYW8cCKxV8v9j9kKaiDT26wDuzwmq2vm4x_549peNlQoSfcWTakMXQGGFhhDrxDBwDwtnHCL9Bdgpfwp0OKdoFN9cK_ccmbTxopL-QqXbcGg7R2HLFsoDtAfjpiEjZNKC--ZonpUvtu4dYjJr_hyKcOs6xn1grsJovSw3FNd9GrzdYCNLvnEyPCtXCORBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=ku81SZw-melvDezxOHUi4US9INNV9NZf3U4Qby9y4vXBZuRw0FCeNhUhbKg_FKg19NEVYTWw-jObMIoOk4VT1rognCY8qDuw3NOoeTpVzhI8OtzobGCqfVB_TxQxiMfSwVd5xyGdBl4FTWJSbglt_M7lFRBsbP_pNu--RogNJeQWhFSdJa2ovOVXxmG_9mspJqQ3fuEt-zAktjrfLsG7cPkqf_BlMkkbJGxIhvh_xRip_S1eraKRw7wIsXemw8pbwRC6umog2BKE2cn67nGvPZuyr5u1fXLWesGtnud-vFJ7-yXs6MAd2joXicgcUqnD6vU8Yw6EkJF--nArXpXsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=ku81SZw-melvDezxOHUi4US9INNV9NZf3U4Qby9y4vXBZuRw0FCeNhUhbKg_FKg19NEVYTWw-jObMIoOk4VT1rognCY8qDuw3NOoeTpVzhI8OtzobGCqfVB_TxQxiMfSwVd5xyGdBl4FTWJSbglt_M7lFRBsbP_pNu--RogNJeQWhFSdJa2ovOVXxmG_9mspJqQ3fuEt-zAktjrfLsG7cPkqf_BlMkkbJGxIhvh_xRip_S1eraKRw7wIsXemw8pbwRC6umog2BKE2cn67nGvPZuyr5u1fXLWesGtnud-vFJ7-yXs6MAd2joXicgcUqnD6vU8Yw6EkJF--nArXpXsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=aX0Ceosh_2tmRyHescvIevyy8iCfJx5TzNMOnGAznrwsfv8NL958Vd1X2YHBPsmwRMKbFCUxX-nzJ3c5DxeN6ME4dccbA8F6dKmhYn5uRBVphE4u15w8rKbPGy44PIgMJ4mtbXabw850COuLBeVmyaQirMB6Iy6Lxa-C0GKk-o-L-JcnUL8X0C3QHNYSN4Tz4ry-S3Xbc6Mm8D7mJ6gHe30mueq3nClO1TPugcwxsqIEojbCOn6IGy2nL2Z_EbCFkibE1_oBKkmklQ8eWN10QgVXXQWfj77Kh6m_nZ0JfyhXDkVY_2M-V6t9uKcXC0zriB099GwFDXRlRWSln413Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=aX0Ceosh_2tmRyHescvIevyy8iCfJx5TzNMOnGAznrwsfv8NL958Vd1X2YHBPsmwRMKbFCUxX-nzJ3c5DxeN6ME4dccbA8F6dKmhYn5uRBVphE4u15w8rKbPGy44PIgMJ4mtbXabw850COuLBeVmyaQirMB6Iy6Lxa-C0GKk-o-L-JcnUL8X0C3QHNYSN4Tz4ry-S3Xbc6Mm8D7mJ6gHe30mueq3nClO1TPugcwxsqIEojbCOn6IGy2nL2Z_EbCFkibE1_oBKkmklQ8eWN10QgVXXQWfj77Kh6m_nZ0JfyhXDkVY_2M-V6t9uKcXC0zriB099GwFDXRlRWSln413Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=IzmoOOudoNEXNNbIH52Aj1-3sWNFNf5GwKwnC5-w0z0i8eJ8IJDevcrB_IWnDZjuCnah5LT1zAgKD4cNiDelwmj30K5DXGN9621gkeV3bJc2kdOQyLzujfFHd1yT0X_tOpX_lPt_WMk0S99uD7mpX1DYiRHItu0b6mLofC7-tCQFNr59e9Qv5oVixQiZ5eX5AIpOZxEdWqjCE4coRmRHRu6JG1jlHOQdRTkW9w8FePYm8d2naXKUf5PGg4cUGqGSjTCkEKrrf4bJPWxFlYTynUBKF6ct_wX5DBry-90zV39TKFw97HvT3IkpcrOEQp5WzwvwmeyIWAG3z2SZiEdlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=IzmoOOudoNEXNNbIH52Aj1-3sWNFNf5GwKwnC5-w0z0i8eJ8IJDevcrB_IWnDZjuCnah5LT1zAgKD4cNiDelwmj30K5DXGN9621gkeV3bJc2kdOQyLzujfFHd1yT0X_tOpX_lPt_WMk0S99uD7mpX1DYiRHItu0b6mLofC7-tCQFNr59e9Qv5oVixQiZ5eX5AIpOZxEdWqjCE4coRmRHRu6JG1jlHOQdRTkW9w8FePYm8d2naXKUf5PGg4cUGqGSjTCkEKrrf4bJPWxFlYTynUBKF6ct_wX5DBry-90zV39TKFw97HvT3IkpcrOEQp5WzwvwmeyIWAG3z2SZiEdlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhbhHWj5yN8jPF7WFUlMcD7yPRQLfFi0mwF64TCW4fZ-Bz5k9Cf4yKNTY6oWehs3lRXDbr-AlMDITbhXEGcx86jBpvzrVHxHq1kZ5R8F2bLruuaCOYEPE6Z9phh4JKslVO7YLHs7Jt3Y3W_7epX3-sW1_l3t9gbV67pIooEInmCx3EikEKUOmctoiKhLiHUzHUQEP3D6POg4wr3JcZgtFGSU_-KHtluKmKZzoDI0c2bQ9zi-uBDrN0R8MPHUl8RcOonyP0J2FpuFjIrAFzqEPElhIxz0MYwRzGU0kXGIrypDa_HfXQ2XnmX1XEpXajagos38sNClE-_u4b0hmv1cLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=olnPqIaxwaSh5pfCPf9n0zK6zi51z3Afd5jeT0KPZtVURQm0G0XA9BB-OVIuM3jcBQHkOs52OlbOpKzrWgVKWDGGT4LVblHsVzXKhw4Yjc4OwpzQcviqA8SVxnZI26U9Ehn2i2OJ9wbyfU1XmOjZkn6N51YtwVjdfEIx0BS-hAXo9HSGDRR88cvfGEdpdImrmYCNoPWv7-dXWH6FM3cJJXdTax4vVJVMngd01izwT__ygs9kHntkjKCTSYzO7_AncuqCmGVOg_vmvRMNugCannwOLqZhABvenIy1zMwANwv57UWl9cuTLRjMwcGejAKPUaap5fq7IIr_jSrS_rzl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=olnPqIaxwaSh5pfCPf9n0zK6zi51z3Afd5jeT0KPZtVURQm0G0XA9BB-OVIuM3jcBQHkOs52OlbOpKzrWgVKWDGGT4LVblHsVzXKhw4Yjc4OwpzQcviqA8SVxnZI26U9Ehn2i2OJ9wbyfU1XmOjZkn6N51YtwVjdfEIx0BS-hAXo9HSGDRR88cvfGEdpdImrmYCNoPWv7-dXWH6FM3cJJXdTax4vVJVMngd01izwT__ygs9kHntkjKCTSYzO7_AncuqCmGVOg_vmvRMNugCannwOLqZhABvenIy1zMwANwv57UWl9cuTLRjMwcGejAKPUaap5fq7IIr_jSrS_rzl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPC-7uoTPDXnCscI14CT0cPovv8yJJ53vnadATwoXW2PCLVkNKsklHsrqvpZktEi8QfLl8qZqbCTx0sFQKb47WmP_yJXcFYZDfHVuGa-kzcxsvB8tCHZslV7x6UWhm30KVRLgz1uDGN6IfxH9XQ6Z31-6IXaxOYnpQGeAIVPnSxzwI3F1ZcFJYmcRIzXbQPWAbLemLsOiyvhpY5aYl9GlJGCq3cWDiYWbX9_jzYOqpA3T7TtS9cYvTxu_HysD9RSQ6crXGFMnh45VqSZMN0TCHmGHxmamYPXIrhVqAjTHMxZ2hiSBs7GkE232_XnIi3UGEUuVv5Ioskd_zDncOItGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUxf_R0HWOqQFTjsvmwFNOWpJKQpOY0r9A-4yg7qQIwUE-Dgr3zWSKHvH6WoUtFMkucteLI4IukL2M1XUifR1nY3dasApbDFmtDqor3IikV2EYnD4GwfMeiCy8hYdW1qgX8srPYS5Wf8pGSwWkUfw5ASJy7BskXo9e4Y-cxqNQpsmalfYl_svOyE44WEhn8xyUs-0vARTn2JAXMGl8Yu5XXUkYDkrtP0i5zIvknNjH8fSFwcGkjDkjlq4ShizH0ADx1LdDVJwQID5IeXwVdXyOqfOk1dcBJFcBzSItXuyH6WpiNp1CkpfFpBgxce25bCz3Uiq27ugpQbPqtqUbAiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/os9YVJT-Lh9LD7g_Q_vS6Zb1CsvEiiL7SCi06qruMuXsvvHMFZpK43H7BJBBjpuTbAPWsZflJoVurUuyYmka0fhPszLmS2lnBoUPkwJz72nfpPB13xNYvuLYsdwfwtH8Xn57dFdy6bFNf38PNbxH3hTujy2WQWn1Em3ryYnSD-h8Bd4yYMwkLq6oaQnnvwNPuygbO8f3lPeEOjf4tkAZfaGPL0yvEVBnnlGV2N_89aSh56pjoAdxXUelGm5JzpajA4LiLuUKHsUQg-AIEdP7GGTsKWhonF80GR85J0wT4rzFcIqRgtAMHMHJXmKLk1udBzp0hHCDo7WFeFd1WYzZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ltc0vqIEPU1mpslUNo3xB1ENQ2vCQbQ9YhV2ArNHrHjDhXaCwmsiP_VfeG2IxHk1corSFezT8zplhsCe1wJE0j5T258eQihlCaZ9Ohiox4ulNG4gui3kV9XQe7FMvLzX_hWDlBl-jIcVe8kMd7v2Z_aEFFHWWcYJmMDIP1VibYEF5c06m-oCnxrfI1BiAJmZOm3il0pO-0iszImeBVvkd_K5tiAfl1MuNb6fDsfyf_ydTxEesa4J5ZBW_hbmsxiFbzSm-Xx7d8VcahveGZUSTa4obcOBjKGo4qXNoMLbMJR-3kCwhL9gaXK3uSXgga6IVyFlmv4KEqAUWZOAPOZDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dErKmu17BiCvQp4mF7StGWl4aVUFiZKZ6BjRz-KhJKCJq0IE1YTajtla516jUNdvb6C0vHOIQTrAyDFseZoivKRFOowrnoxkuzrGrn37NIG5zJmC9pLkZ97AGcLFS0-yJdSCCFgbhU2Vowv26EgBdyTqyypLb5ReqCr5CvfwbftDZQ9BIT8YwSUeb8AQwObyK2eqcmFX7i0P4dSOc6ZUW_MTsgh5uoL7EAgFOGv46jfCbmYlXQcwlSlyBISPXlNPK5TvlCDqS-X9_G2f-1ulY6N8_EL-8SvTpMxdCypgK1thTopcNnNk5dY3-B5Z-Dxr6OnsfGZJxPZj_8rfsu50GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=AwHW-_54iEDG-uj5LfEHQt9PSq2A3x33Twu08QUICSZjzKOaWHrnwePj-OgrwfbznYhtz4AieCIs0Bq7P5sdN_E4SiSmaHeMcphejbiiJWZI0DogidMcBhYynippaMxlnUEwk51g935-bK9RsyziTriyXTw7NYl2_Yhq-sYAyTmWOiYZ9kh7iLlL-JJ_fFSX52W7Y0XqoVOkMqLw5R14l8eKNbcwC4Ft67zYNB9jAJBtLkFUiw2OLd7h7Wgot9TZJSoMBwj0zNwgrCdL5CYzie5-pUeCvxPTDffshGfli9sQA7RTloc1ULBEM_ZR0GpedF_jJaAFBhc8jXXmrlvtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=AwHW-_54iEDG-uj5LfEHQt9PSq2A3x33Twu08QUICSZjzKOaWHrnwePj-OgrwfbznYhtz4AieCIs0Bq7P5sdN_E4SiSmaHeMcphejbiiJWZI0DogidMcBhYynippaMxlnUEwk51g935-bK9RsyziTriyXTw7NYl2_Yhq-sYAyTmWOiYZ9kh7iLlL-JJ_fFSX52W7Y0XqoVOkMqLw5R14l8eKNbcwC4Ft67zYNB9jAJBtLkFUiw2OLd7h7Wgot9TZJSoMBwj0zNwgrCdL5CYzie5-pUeCvxPTDffshGfli9sQA7RTloc1ULBEM_ZR0GpedF_jJaAFBhc8jXXmrlvtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2H2ZS9KVpxCloZVtheFNNihiN5egyhTXq9quGiROCCA0ZXPRz4Q0PKTarcRFxY4ZgwQj0e7uySYM82PyXPO-amzu4N-RnKP3XDLZy5BFrECcYJqXxkXp5K8U5zwCci1vf71GsY9n3lyimmSVBDGQel24wMM9K_AQMo-OePZir9Vh1JtE1i-WKdi77mHPlR7xqpEiNVFjmQDMIfnTrASFBTNOWqTqVs9KzHabCQ2p5Oxm1LZOwrTT7GPYnHyu3yr5Cndc1BxqISIGJ0Tr06mjWfMkyvSislDS8Nrjk0py-5uep6rdWioWuKsCXG1TAUkfxTYx2lTS4tuCABJio5OZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRvUBW1vMxa_k29FD_f53co6-XG7nGvD5yilVumTO6Q3HAQSvxdFOS0Ilgs58mxfvJ5J-8y19NIfYVJuKe2lT7oI154jllyDLUG8inFeC998aMDf5Klr0rt8O_MvMxaF-1Ty5PzvjXf-6k4hIuO62j2wDNJ0P8a-tVXHyM6UWLwoQmjTk9J2X1ZkGDiWmBeyG06qsLhN4f4f9jYDiGt9hsFcolv0Vdj9u4MiKzCyUPjYmZfJ8BFIK_ET7d_u03wlEtyGqoAPDx_1BnSYwk0pmZJwBwNbpZoDyQfNSEvWm31xIs3U93ch5yrU7AFigf46UhuSS9c0kFbEP1ZigaudYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=hsyszvy9G1uhFmpb7sVfhELqElxSmiOBbce9WR1B-AeYlxjPcmNTzYe8aifwwdyhlZGtWo6zdzGa-BQQHtGRnAuvSatsOsKp9As1FjLe6eifZJj8weBdS40fz4dM-rRsmoszWiMraDBeb15FFjBHe6QDxWS8YK3TuwJa2sabe7R8IdJNo8uPF4C9hWl8E5PhY3DNvWRcz7gN2pwC23zekuNrOiZqHwplRSnfu59jUofSkmuQssjwgCVZ_qv0cpnR2J8D6CGl3KWKY-i7u51wCf6pfhK20K1tg_8LB-yxB5GSz8Z3npNrsTC75AC5Wle1ZqbbL7kh69PKjogJoQ10_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=hsyszvy9G1uhFmpb7sVfhELqElxSmiOBbce9WR1B-AeYlxjPcmNTzYe8aifwwdyhlZGtWo6zdzGa-BQQHtGRnAuvSatsOsKp9As1FjLe6eifZJj8weBdS40fz4dM-rRsmoszWiMraDBeb15FFjBHe6QDxWS8YK3TuwJa2sabe7R8IdJNo8uPF4C9hWl8E5PhY3DNvWRcz7gN2pwC23zekuNrOiZqHwplRSnfu59jUofSkmuQssjwgCVZ_qv0cpnR2J8D6CGl3KWKY-i7u51wCf6pfhK20K1tg_8LB-yxB5GSz8Z3npNrsTC75AC5Wle1ZqbbL7kh69PKjogJoQ10_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=O8Dvhw-DPo35r4AnwAb0TzIvLCb6oLcEJNe5XnK3yu4RfUY6nKbPwuCZAFcJf3jp24mXndEumFQQmTx8UjRD2F_21TfE-22e7M-SEAlhMnds4ElNy6_L6oDXkVCDb6AqEXuMLg5G6sfKg1EiZNaP-BuDKKTH6dRSrpqwjN89YQ6iQRmcNYlEEkGLdWfrl3EOS6czqScPLcE7wQbKO3cwrJ5Se844S3Qpb7K4P8lm0TgkXIPjTwmDp84dLUTLJ4GEM-IC-u1OK6AFja-xCsbYWmQq-rRasOm-zdAMHOK6K05EEA6v-aie8fPIm3gDfdUJn5BV8UobeY8kDR6bi037MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=O8Dvhw-DPo35r4AnwAb0TzIvLCb6oLcEJNe5XnK3yu4RfUY6nKbPwuCZAFcJf3jp24mXndEumFQQmTx8UjRD2F_21TfE-22e7M-SEAlhMnds4ElNy6_L6oDXkVCDb6AqEXuMLg5G6sfKg1EiZNaP-BuDKKTH6dRSrpqwjN89YQ6iQRmcNYlEEkGLdWfrl3EOS6czqScPLcE7wQbKO3cwrJ5Se844S3Qpb7K4P8lm0TgkXIPjTwmDp84dLUTLJ4GEM-IC-u1OK6AFja-xCsbYWmQq-rRasOm-zdAMHOK6K05EEA6v-aie8fPIm3gDfdUJn5BV8UobeY8kDR6bi037MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO8UK_tzcJex0nNU7QqnLI-Cs8FVmqP8A4MSSthb1L2D90NmQBe6CI0fKVQSEc9MWDcFuhV4khFdwxihxHkR6bD7W5Di2mjOcShQYD4vrzhot_jiii1f0uEx-H6dDXZtU8xdFV-a8wOPEx8hQJ7A7KAFqyAXKgGCQNcG_idmosVm4-RjDxuD01Gx7GUJu8SigMqkCWSA_ciuwNaz9c1Pqxjk0BxkBHxufDlpGeBWq5m2c_y5JtUdYwLY2bpw4QaftkfI9t9nLE-NZuFM-DFZAeixHhZ20CnndipVapCPukgB6lwXyrxJL7KokUar6RR3Y8Fsx4PVxl5v-kx33CrUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzndSuVkLjCMgfn_ZkM_S114Qj1U3Zfx_npDV7OFPFeQSXR6xT4ye1PBBorQ65etyN3p6uUyFeUOPELiari4ubPpSTWZUBxrmv17T1oFLCtMGLCW_L6toF9x-rBvcJsG446pSgp_zoBmh_4Kqd2llKV9RX2Um9QRbMzJpmcssk5ZROvP4dO8-4UEnOnlEApXJoVvF60L5gfv9_5hVbkCqjxmeXQja7ydxQZZnnCzyxeNbl_vJntCyRhYIrvxR2YerFs7u2l6eX0Mkau7eqhKEADMt9KBb9pHGiSJKM7Ghc5YQccm6sxifA7ngozv1BMQwgTYaDmqVWa0c-uqKKxY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUTaBa6ZU5o20FlqgBTNWUnLSiS6TQAj_dfETWNK0b_EkOUQZpZ0YRSlVJHtKMsBHzNMYwvq3IptClaPRmKi8CVylr5sUi_TWTZGSomaKEwPnmDMooikBshzJ4o21mq6Hr1Ev6KRL2MVSmOcjVpN2ZEqIPuaFjRF88-OwV1_3rYhdWoUTJB2HCNUwbtDBiQlW6T0jUuvmuuuy1ySclFKvpIJMqF_U3DdnRlnQZBea5uLFrBNl_zsjxlNKoXTIboqk7bYxM7HIxOw2NWXhZHCxX-V37cKXGnRlwiLOZEDQGvcBRegnvX9lDT6J-7UkUbZg_ODLWESuzMzF5I1KdHEJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRo6Km8wGfkeor6BiANHjKJWq7p2l_ttj6lcJPH4CoQSWS-PYXsYVaWHJjipEgxvBi3PtXG45h9jKxRjvKodtGDkXbFDgFNrAxBfx41Xwn39qB0LXCzNCPAORmM7sbQhXGA1RN5jPBm-CpXkoCeJ38Da0rPnBaMTsfcEbYDlMosVUqWayMr4nu0K4Fgp4214YCfRdTZ6vxam0F4DWBTdRsggU3K4V8QY00SUaGBAb7i2e-nJjnvk7bhr4rurSQUl3nLasnYW1IDB1Vzv9zA0gp6uWL-NZ5SX-cxD546fYcX_zYH3UOenT5Hty5GjLrBwSO3f3XdWRhCbGBNnuR5i_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cunvtHdM0nX4w1Nk_aZgPRh15H63qYcTIlCHSKdr6CsLmQAwlbpT1T5RA2cLz6mXPR3nBKwWq5lUjVbHNRM7n5Ti9asD9dIe6B2X_xfFTPQIaLar6uyLb3SQvTYShzGNf2wPQokZ7Wk0QlvDZ6hWJ456rK0vrI5TtSddDPY1qQmxtuep4gHiurLGB7y2ZjC0wMuf8mButMBr99vEgIJdQW2moNriCZGnGARUQ6frUhTxBLsTLdpOZ001ERBhihOI9D-vc_3DgaA-mxbT1HLSZEWI_71q-1hnCjbOJ_wD9fi74O8f7TGSavwgevKT2d6e_eOPyk0W2vfad897xWlHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXebkdq8EdR8eQilGRR9AjfF3LEVNJLyCF2vzynOT6kOBus2lPNJHfPuAzIaM71gqVCK5_wt30kb0vh9u1xbbTGEyLV5X-mtwbuMkv3-KIV-MOUh-o2GPHbE14YWClEPo8Fyb6Ela0aVQtRbcKTgtlEuB_TN3j6xbkUnKc9ezjU4wy2PYYLhQIiTHaIz7PUTz7-WN9ZFzfQRdYjn_jNlEb8uPOaT4OSkJNs23grUuMxJmItDQU1XogQOVMYSLOl7KukkO-0YItL9so7zJQF0Pz0LrIrkxxG0BP2g9m3FOUI0WWHcxTuW3hGyx1golQ2MPQv4dkmaRIacGqwU9COoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SV_fcGyJjH8TbqTvMbBrioYPud7ssLbGM0dAmXElpgHkVwFJZyUCZtU2whl9ixc1A_wl0pXndSQVPoIvJs5xkg0fv0xnJ18HdzxD45Z7XeRbnsl0ovr0R9qDr95KZIQeQtkEjSmkLN0VfTt-4jwIJenhQzEFI-oF6osrRwZzq_uIQc_pxhCechQPy399acbOrncmjZgorMRvf3JYtIVSbM-ET8Hu-j5NJuK_wisxEl7qXEnfQUsK6TqIxhz0_ioAGn0Ps5b-R87kW5Bzqaa13771KzmnmCaM4BXa-7_BwLYRuvTK3r09R-LoMjdt2K0o-W_NQdR9xSeJwA3A7otC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGyAVuT2ndz5YU4mCXU4Wnk8Vi8BbzUegw2mrJpPjqfnGPupJROOhrJw06DV42SFiqIv6NQ3m2avGZZOgloaIPpNB01MmavvSMXadRYS8IShlIwFzqZ9PsSupBE0WU9w6qDFVVJkqchxoI7Vg-nTWs-2P-rtNzvB0QKHk_mK5UPlUO1IM98rktsIBDLSGz9buagJImHo9UdkT80H4yhvVn5xkKMxCOI9tFkhLpQfroIGf6hzptYSqpxE56aqpx47xzJFF8Ta5T7BH2PfMTJvetqRRy6VgGIFVOvEbfTldg9Y-jzktq9J7xEJegD3OpbhtSytQ58YQ6MY5PbUEDj4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skW8sflue3KRLufQ0Ha-507TO-wg7ttvSTjEe_tR7m9S7-vEFCUFvZU8uwvo3feyEvNSl1tVzeyyZBr35x-fbo9mfzcl1_zIsLygSMaGYpNMZf9aTg1RTWdfDN0qLJIvZaf_glW4ckQ2sIKluKL1Hi-Cwm0xXg_aLfqBnkWZDtxdhUEF08Ugpg7LsXdYQ7V7qoaDP2b7EZBbO-TqpfTDLHRUsIysMns8wdvZZGwxkTy5ZfOvmMHbzxfsgIEG1Wp-y5e4oaocrtqimu-2M4PCTo3IZRSYc-KxV4qTbn0OANily-MKlNa2OjWq8Xz92YEbvMIdNbh8yENPh00c5QkqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzf4T1YmLo7x7RtKPGVdPvV1DKEqR8rKGbgz76QwMvy88TvOAnWxJeDA5XvzcTfWxO5-iBy2nvU66wZhAPysEbH6XP3jeXF24o9ajqVIZxYOmBgRrc3o9QGWuzGi-BN8gPL96j8kxYtIoR0Fq0Sxl0kKR_zva_ImNxGi8Wb40vyrsubydPq6UdNel5U0oTclCVg5GA7LBGUc06uUNb4f0ZUOg-2QjLGoNf9O2eaU92fizoQOcGHXW-yFKa_w2ixLyfg3vUNwHmJ4PVkAB5mj1-fCfh4vE-oG5lAxJljdiNLZB-shpLGi_QyqMMG2dXBTsDSP0nfKAk0MqgbmCuEx8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP6E5XorvMJguSNjK7est82h354KySpzyyXimRcdx7Lpj-Hyx9apProtdeSHxkeq8TCIGYlWViyzSPwgdbX_RyC7raw4R15lYZz0jd9R3O0j-z6yfJtCVyr270ATH2hVMqa7AlK_9Qfdlb58DnjQ7BCjCwQN1FzF57QWx-tF2zoIsoZZmWum-SjvaC1t62L41D70eL21VHO7zase9dop5DdhF7HP0pSWCHY3zAZg1rg2xw-CsfoePPsN44X48mwB_wLBJy6tMOTt-BV9oHcAgrrxUQdLgovCw1VR_-9_ys8S76gvw-93fKGC9oUJA8-l_0FbPIItWZOr6BMSGqvwpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCrOTyBriwWiGC1ks0oDMRynbSZYzVweWe-B67iHNjxXx1j7UCCum6T0LrvZLdJhm7RG_d3l8QObG4EWMNMHBjMtBP8eTqK5OYDWFFpYmgcciIj-0ydXxJFCgaV0mGmE9WWGUjfrSIYtvSpsIELb7WvLcGKtmA0PLn1W0CJCGGrRwEI_x_Wgmcyz7iRm7XzT-yK93YT-LUWW9oF4c0Tzr3gPXeqAXIZ537rrZB_LO7VlhMKlK0mVPmItk211ysOyzK5O1QkThnhQ8n3oUG-C79vgu_XUUZa8PuFSsleGHYMJCbzRmMCgRl4pV8waGaXWsOEHr9IiIBhfN8APaoALRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=o6lKsD8nFCeX04fwDX6jWqRkAnsfgIyn8ZGDqqCkHKxpiu-9JyclMboYmLJw8WzXwGQZVP7eXGOMJf3tQ4V1Kgg0i6I6IWvLb_wR7cEb3c2At6Rq6yhEeXToQlaFefLbla0MzJLGr7LasPUhuPIlco0KNozV8IS275WfekAoiTZXBIln5piyDvmg_RymYgSVKQKK-2nVh7F9K55KDC5kZ4QN1FdWz3_hmEIbJOjJqq5ToB7YeODP4IQXwqHLOzlvMGJWB78W1pUcPFAWtGYDIcv9ls0YlrZldVSiktYerq4BHp8pT3I4NaEI02PV9KUrFkQrj_JBG41C8pWGgsydUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=o6lKsD8nFCeX04fwDX6jWqRkAnsfgIyn8ZGDqqCkHKxpiu-9JyclMboYmLJw8WzXwGQZVP7eXGOMJf3tQ4V1Kgg0i6I6IWvLb_wR7cEb3c2At6Rq6yhEeXToQlaFefLbla0MzJLGr7LasPUhuPIlco0KNozV8IS275WfekAoiTZXBIln5piyDvmg_RymYgSVKQKK-2nVh7F9K55KDC5kZ4QN1FdWz3_hmEIbJOjJqq5ToB7YeODP4IQXwqHLOzlvMGJWB78W1pUcPFAWtGYDIcv9ls0YlrZldVSiktYerq4BHp8pT3I4NaEI02PV9KUrFkQrj_JBG41C8pWGgsydUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=j9oup_i5GKpcZE2DQnFBTtzd3I9-8-M-rC-1Xqv2UNdCd_tQ6LDIo-lFvKkIldIF6Kxgb8T_Da5VJO6uSgU7n2_z58I6JT00rZYxAF2D3I8APxMDW77WyVOwAn3I8AaF7iCqih1zU8DlQLSOEepBtR9cKEmENaM-frqbe92cKaBnZ9zwVLY_iie5YuEJMuFSVLy_0RELBQCTUkz1RyHJy9tnDcp9WM9gIH9FrCBXTnSfv0uUKLpn7aC7RZX6QM4nWI9I--5JjqKO1Lq54PVxDUaGv_Ga3W7rxN_zs3T8IN_VHwV8V51WU5x4OE169rTEIYIw1axNmaV8UGmKmKuCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=j9oup_i5GKpcZE2DQnFBTtzd3I9-8-M-rC-1Xqv2UNdCd_tQ6LDIo-lFvKkIldIF6Kxgb8T_Da5VJO6uSgU7n2_z58I6JT00rZYxAF2D3I8APxMDW77WyVOwAn3I8AaF7iCqih1zU8DlQLSOEepBtR9cKEmENaM-frqbe92cKaBnZ9zwVLY_iie5YuEJMuFSVLy_0RELBQCTUkz1RyHJy9tnDcp9WM9gIH9FrCBXTnSfv0uUKLpn7aC7RZX6QM4nWI9I--5JjqKO1Lq54PVxDUaGv_Ga3W7rxN_zs3T8IN_VHwV8V51WU5x4OE169rTEIYIw1axNmaV8UGmKmKuCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhUr3pOuCI8Za9QEyUlyaZaMrBOAN4ej2AMdsUVL0_K_Ahm2V8dGHu-WW_1Mz0LkO15SJpPRg6KZPjMiEMXcPMCLqlMcYJXZD7cr8BmIIPc2jlEIaWi4faN_uJ54pVqYDrDND-xsJV9CImSuMo85QGZD37Wm405lQ1td7PIElhGyqWJcyzI-WUe_31XDY_kE6YQsQ7-pSQ6t6LlNq-0WuqtcO-QEISJMTIG5F6TvqEnx94I_4lyxOvaNLaBlmNtWJW0u-39dfS4NinOsSz6d5wTC8F1Il1RvNnpMy-zaGtiCqbZAbczg5yLfHREGlyrBS21U4ItIFGe3bhAfKdY9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqbnjj94fBPrGH9a7nA7Dx755JsMmfCcTa3T_aRkVV48Q8PgZzCyfPhVAw1cxbXpwa8rcSFu9OgveenwW8CfyklccdRG90kXtHzIAz9O-JbzKSNHwochwm4X38dTQ5PNccgyh9EOKlRp9FXM7vh06zBGpT3sjQYz6tBWWjR1nvzvwh224CaNlzUmuw8LuyEnoqFEAAejjqFuN-zxo-b-yK9PC-oDikYT30Bab9Ii4P0Qees6-RGBM2uLO_5PO14OO8rZ4Ep-qvZmadnd2dgbXqczLy7aCH_vA3ATIkOm_dv_7M2kvViUxEzbbwyCCpLNN6aHOHFfCV9mDI7ZkavroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=Tqt7bm0BqG_q7-z1bC9A0JoGzCGz4trgQu8T1iZmQkyxxDCjf_j3m8VT6SponUg9ptzSgsd6AwDsGB1ql2_9SN3VtFljWxHEIVq1cIvRWqzzmj_3Yx2U22QljhsXckP5suwXuA9SFDfdd5GqnkG7SejTzvXYrMrmZpewd37PwN6aFQ3BhzWvhOynq2hMrTEbIkb1GoS3XTyzgK9_elBcG0ou7r4Hb3x0QSR3RvOphvBYDcpi7aJHud2Z57YvHPYKcHmgv_R7bwAOt2xpooA8do7-xRjEh4GB3sc0KCDptu2FOqIhAAhjP850c_A7mS0pjlaJB4_hbJALWEzIlD6u-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=Tqt7bm0BqG_q7-z1bC9A0JoGzCGz4trgQu8T1iZmQkyxxDCjf_j3m8VT6SponUg9ptzSgsd6AwDsGB1ql2_9SN3VtFljWxHEIVq1cIvRWqzzmj_3Yx2U22QljhsXckP5suwXuA9SFDfdd5GqnkG7SejTzvXYrMrmZpewd37PwN6aFQ3BhzWvhOynq2hMrTEbIkb1GoS3XTyzgK9_elBcG0ou7r4Hb3x0QSR3RvOphvBYDcpi7aJHud2Z57YvHPYKcHmgv_R7bwAOt2xpooA8do7-xRjEh4GB3sc0KCDptu2FOqIhAAhjP850c_A7mS0pjlaJB4_hbJALWEzIlD6u-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=lUYACJkf1QwpB9WuATJ43DCFy5gSHBPDagYXIxOt7eWTV8MtDfdUwXDuiuOcad-S2ou6nlk1m9zoKFp8VGNj1S4QmngfPEekQSGQ-MI2861Ah2cAcU5O4Saxkl80gm8rK-lTeo3nD59pkz6Zp2MQdJM4yKZjWLx60FP2RZvp90LxdZqJZLTHrHY76NVXd8Hl8eI25vY_vDlKOnIFgQS9xqp7S-8Sa8yAFowIbplx55KjrShpf7k5RgdCtHlv9U03Q3y642VCZFjr0n2E0yozZhoFFIqpebss1bKsZLbIJaCCugnbZtxb9MbK1BQs7aORi9tLG-OxFjMh7xes6-g95ppEiEaAGLMIDT3R5EPIpa-bFcxxmZ408SZsYCdBhVzJg7iD8hoTZMDcA9fdit3plBYs9FHmzOcO8TcECjXYNdnEgQhzrMNIhSRYIzxwImoCg_t41e_pa5jUo_bmBbtWepZvVa9q4dwpqYyD3OaGLSQuhKP92-2a-nfFBY6uKCB-_EdEnyKjPy67FiOYN0dXQyD-D_xBtCg6Br-DJbkCLdlz6J-dFyTnldCHEEDrfNDmIj8rkMJY7TSD-kGnblFTw3fdt0R278tWJFi53AUCOMxAJCASk0KxLsCen4fzD_r5HwoJUV27zdOkbP9-MsjoVQFD-_QC6e3kQhabc8OogA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=lUYACJkf1QwpB9WuATJ43DCFy5gSHBPDagYXIxOt7eWTV8MtDfdUwXDuiuOcad-S2ou6nlk1m9zoKFp8VGNj1S4QmngfPEekQSGQ-MI2861Ah2cAcU5O4Saxkl80gm8rK-lTeo3nD59pkz6Zp2MQdJM4yKZjWLx60FP2RZvp90LxdZqJZLTHrHY76NVXd8Hl8eI25vY_vDlKOnIFgQS9xqp7S-8Sa8yAFowIbplx55KjrShpf7k5RgdCtHlv9U03Q3y642VCZFjr0n2E0yozZhoFFIqpebss1bKsZLbIJaCCugnbZtxb9MbK1BQs7aORi9tLG-OxFjMh7xes6-g95ppEiEaAGLMIDT3R5EPIpa-bFcxxmZ408SZsYCdBhVzJg7iD8hoTZMDcA9fdit3plBYs9FHmzOcO8TcECjXYNdnEgQhzrMNIhSRYIzxwImoCg_t41e_pa5jUo_bmBbtWepZvVa9q4dwpqYyD3OaGLSQuhKP92-2a-nfFBY6uKCB-_EdEnyKjPy67FiOYN0dXQyD-D_xBtCg6Br-DJbkCLdlz6J-dFyTnldCHEEDrfNDmIj8rkMJY7TSD-kGnblFTw3fdt0R278tWJFi53AUCOMxAJCASk0KxLsCen4fzD_r5HwoJUV27zdOkbP9-MsjoVQFD-_QC6e3kQhabc8OogA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDt6lmPEUUA759WjTpcDtk8z-g_ye0mfXe4X1xaFFVXgLpzf3CE8JTlEFK3nknfyjOD87rFom8LcqY0Kuo-ymGQGKLGH3jDZfSYFJMpVfQePdqqHV_NF4fCRI88W_KPavMYigWi5x4CN3omKMMuVXEsBuCa7ZY8gKTtIGBP9T0va8U-X8a8sho9oTrAYOEzb3NIqlzYqMS_-AWVBiFRlF5lvbu-OyL2p4s7D-1d8rTgH22heOMJqqBHy24HSrdvyOXxNzwUySLKvmUGTWRuRwLRGgMTa3idAxt_URczpiwHqz_awRlAiQzpjg9UQK6QhJGIKV5nzXeSsapEyqiuPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=FyAs7e4ECt1LAcDxA5KAq1Drd6RYOsw70jg1sgPiPbw204TUuOn1v2RBq0JagMdr1sEWYFPdNxC2ow9pmeEQczvWxThBCtEwrE5IuoH9VMbkQFTPUj0AEtbC4XR8aqr5OknE2H-_5my-09n4yNJRGndi5a6EsgoLCmnuaYk9QsMPFgpQs5RigEtJwg9wkYkQVvoXsCfdffOFekdsG1eNWVPITAgKH7zYDmuovTeSlwAeFh_KlaX_M1CG-6WREAL3GOAkwBk8-fNHxXpdcIOkaY9rRNx9TJuBkYu5ryda_x6LNGVsfCzWFuXyWjL6Asr1gYLCmYEn9UaBucR0ez-s9oTbpuTs1WzZptz_MQWbqhZuxvnougZhu8tkJIP3wARZ1OfMJqh2aj1hdYpa7G7Rs1umb5UzDFrMSzK7uk3WqlJnaqooaT6iqAy5Jxh6Ssc6aXoScLq3UZdgvMw0LgTzHO_J65odqomlzcYc74wB8YR3_H0rcIg5XzJTH-BuRD-iF0tXQ_tRmS9LevFPoW2j0i4GkpthLsG5SZ78cpCPb8abv9QuUNv9UwT24Osf-O23J96yYz4ekoDH99tM0J9CuYCE7JbotUSq8Na8AYaMFSRCd1ysrDfxfuRbqJgD80IHIZQRRNPN3RJ1RWQVf0BhmZLm4qar9HFMi7BRCy2MNcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=FyAs7e4ECt1LAcDxA5KAq1Drd6RYOsw70jg1sgPiPbw204TUuOn1v2RBq0JagMdr1sEWYFPdNxC2ow9pmeEQczvWxThBCtEwrE5IuoH9VMbkQFTPUj0AEtbC4XR8aqr5OknE2H-_5my-09n4yNJRGndi5a6EsgoLCmnuaYk9QsMPFgpQs5RigEtJwg9wkYkQVvoXsCfdffOFekdsG1eNWVPITAgKH7zYDmuovTeSlwAeFh_KlaX_M1CG-6WREAL3GOAkwBk8-fNHxXpdcIOkaY9rRNx9TJuBkYu5ryda_x6LNGVsfCzWFuXyWjL6Asr1gYLCmYEn9UaBucR0ez-s9oTbpuTs1WzZptz_MQWbqhZuxvnougZhu8tkJIP3wARZ1OfMJqh2aj1hdYpa7G7Rs1umb5UzDFrMSzK7uk3WqlJnaqooaT6iqAy5Jxh6Ssc6aXoScLq3UZdgvMw0LgTzHO_J65odqomlzcYc74wB8YR3_H0rcIg5XzJTH-BuRD-iF0tXQ_tRmS9LevFPoW2j0i4GkpthLsG5SZ78cpCPb8abv9QuUNv9UwT24Osf-O23J96yYz4ekoDH99tM0J9CuYCE7JbotUSq8Na8AYaMFSRCd1ysrDfxfuRbqJgD80IHIZQRRNPN3RJ1RWQVf0BhmZLm4qar9HFMi7BRCy2MNcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=Pjyv4X36O9EkX2zXPaZLc7aSNa6X5tN2FSRh36C4bMP3rssvQI7P1m6b9B13wT5lgOUqYBqivPWiJ0B4lUNCUKro-nj2rw0KsHhEdUUan0aw_BmGgozGPHef1fE7y3zqwgf4ZR0Dg8DcQJ6jDREZReRCI72LIdrKyzlWvpuvkm8PwBLZ97lHdQ26W63AJX9oaOkhCUnn70LDcYGuBD4x4h8OMxDcOwFhBuL-aLNx_qZB6ewWNnTRmPhGutwUT7Ve7P9QiJVJCXfYsuzA3MrUAit_TVpkuu979CrPieYEzI31mlrSpf0mLyZYiEUSn0JwKdGd-WLc6FiNWgRW4XTcsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=Pjyv4X36O9EkX2zXPaZLc7aSNa6X5tN2FSRh36C4bMP3rssvQI7P1m6b9B13wT5lgOUqYBqivPWiJ0B4lUNCUKro-nj2rw0KsHhEdUUan0aw_BmGgozGPHef1fE7y3zqwgf4ZR0Dg8DcQJ6jDREZReRCI72LIdrKyzlWvpuvkm8PwBLZ97lHdQ26W63AJX9oaOkhCUnn70LDcYGuBD4x4h8OMxDcOwFhBuL-aLNx_qZB6ewWNnTRmPhGutwUT7Ve7P9QiJVJCXfYsuzA3MrUAit_TVpkuu979CrPieYEzI31mlrSpf0mLyZYiEUSn0JwKdGd-WLc6FiNWgRW4XTcsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=su4VQPI7-5EvcHuSuochxAaaMLu5gLiVy3HAhhLD-lu9syLucKWGOzO8qk6SVZXpfLINWRVluV1xbBp8lO5jpqI8RiTRjrOywBKQRYeXwLSmypfIE6FB-Px2BsWZy9t28AMbwcDEqeHGKUu_VSW3pAS2SGHsdIyed8ehpxSQp1yGIkEMTUTR23MmzwEF_TVah4BUltltrxJy-fWqCG_XxtxcV9rBAq4Jg3d4VaJJb9wYNdL_zd8VMsDPYGfuEXVoKUfSf2DXQ2SzUHoSFfBMDXLccF6hPokDgLgChjlYVmjnwcnQzZWWCqoAHkOgHOB8hZUcqYxyCJJfUz36KvNOTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=su4VQPI7-5EvcHuSuochxAaaMLu5gLiVy3HAhhLD-lu9syLucKWGOzO8qk6SVZXpfLINWRVluV1xbBp8lO5jpqI8RiTRjrOywBKQRYeXwLSmypfIE6FB-Px2BsWZy9t28AMbwcDEqeHGKUu_VSW3pAS2SGHsdIyed8ehpxSQp1yGIkEMTUTR23MmzwEF_TVah4BUltltrxJy-fWqCG_XxtxcV9rBAq4Jg3d4VaJJb9wYNdL_zd8VMsDPYGfuEXVoKUfSf2DXQ2SzUHoSFfBMDXLccF6hPokDgLgChjlYVmjnwcnQzZWWCqoAHkOgHOB8hZUcqYxyCJJfUz36KvNOTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=Mm3MwrMxYDzO2huv1iFpLgd56DB7jHhGYFwKbVerMKos3m0I_t0z77kvy9XUspoAgq_aliYOqkWgoJobQGUci4FWFBcle0-lcrdWWwNGuAa36WGPR50ynRN39TK8Zc2rQqT5XXl-sNXcCdqORWbW84YxhM_6s_XwgJvfck4QnoPsI7UB13__ytuj29ytHiUNDAiqQsYnTJP10VlDY0laoLaUss9NhLw8rm1xj5O9izgumQ-rQaBKgj-eXzYM8ZcwGXavTpBV9RHMVW4gp61uuJaBMQj6pUNe7LlB7dE1-P8GSbrHySl2JSfQWl8ap_UQ25iCOwBBtN8kGGLDd5FgVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=Mm3MwrMxYDzO2huv1iFpLgd56DB7jHhGYFwKbVerMKos3m0I_t0z77kvy9XUspoAgq_aliYOqkWgoJobQGUci4FWFBcle0-lcrdWWwNGuAa36WGPR50ynRN39TK8Zc2rQqT5XXl-sNXcCdqORWbW84YxhM_6s_XwgJvfck4QnoPsI7UB13__ytuj29ytHiUNDAiqQsYnTJP10VlDY0laoLaUss9NhLw8rm1xj5O9izgumQ-rQaBKgj-eXzYM8ZcwGXavTpBV9RHMVW4gp61uuJaBMQj6pUNe7LlB7dE1-P8GSbrHySl2JSfQWl8ap_UQ25iCOwBBtN8kGGLDd5FgVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3Ka-W9HxT25kQ0YwFImbeUbr0yQH5njkFP6JuV6Hzr47KtQcBQYyJeg-P-8CyQ0albzLh-eRtv9d89bV7TIVaIu1M60RawAvzx6e3yv65E9B0dKKATshePB2gVUmyclqeSyKDJ17k1AgwRgWX5z_dQUr43ja34rwN79NUDMlZWo64kG5hd6I88Ausx_EOVq8xFJ_y6WAuX05_7tBRWUM3om8xE8eolYJTDS5s_SxCEwIrYXv7FBx5gTCtQJfMPtoM4BAa9i6nARLTfRtPr7VGr7UOeasBQgtr-GUbZjdMKhN4tje6i4_z83MMY-EUKaG0Yl7mc-kVJqa0orRFdTlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWjX3ROqQpL926Id1RFvy9iwO22lrwf8y9nhxysMeYjWHj2dMii1k0TuPmi-R_zp5M1izucYS8RhEoV_33indi973y5LryHLMIiqMLWwYEIPvoFyTLandi8SLmhwf81qrqyQ7iNEELz9u3tVOE0ESdW0opPxbqXjyIWS50dRWD0MaNg1KT9zfcUZsMAvEJVAeyhIFsaylFwp8uFteyt3stC-fyNdkZDive0xwtytHr6JzvbdwutqBnkeFm1JEQF6gJOrhIg2e4izhTu0ica9O3biDjRAVOQoKBLvn0ol5K0LuNBvhpWG6qHTbyj6IAo5iqdj5WQO_m-vq53Iqq6kHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=v0KqkG4TMclOzTnGEcNrbSXSdVk1jTgPqRx8OWp6zkg571UFKMIQDMdL89q0BuTsPeHNz19ENSHoA6x_fTtwD3E-JmwKUNC1kjNyblK_7t6qeicctFb1zIPMs7HRj8wYIqrsZ2LUHXvuBvSm1wSlwb45suQkIP2RqTsrDmsAmLHLl4DM6r5OunxIaJJ7ZnozijaY2dorL_4_B_53LAVHwT6Y22bnIDnp2weLMeT_UTErJp6B3wC0sgO6BoH5L7ndEBk_dFdaNIAgY9ibJEmVBSXCUEopGzh0eylHYiF5DTvlrUj4kWylIe5PYaRmVzC9vEXh6ysosolk6ilJ37nuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=v0KqkG4TMclOzTnGEcNrbSXSdVk1jTgPqRx8OWp6zkg571UFKMIQDMdL89q0BuTsPeHNz19ENSHoA6x_fTtwD3E-JmwKUNC1kjNyblK_7t6qeicctFb1zIPMs7HRj8wYIqrsZ2LUHXvuBvSm1wSlwb45suQkIP2RqTsrDmsAmLHLl4DM6r5OunxIaJJ7ZnozijaY2dorL_4_B_53LAVHwT6Y22bnIDnp2weLMeT_UTErJp6B3wC0sgO6BoH5L7ndEBk_dFdaNIAgY9ibJEmVBSXCUEopGzh0eylHYiF5DTvlrUj4kWylIe5PYaRmVzC9vEXh6ysosolk6ilJ37nuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=b6dKRMkOqMs9EKsxYBqcPcPTlRwZTUzpVuJ8TTbZBoIXUaNSbT_mZ4zl2yZtop2J6m-5YpkIj-NHvLtKOaALv3REXC9NXgGBOzP6OKF4-5BPOenXPuWVQ5doWeT7l-2n-qC6H2LTsV7xeEfYkvLa-RD9upyRH1BzhYqow3eIboOBkBp8I7RWlHsYsDm2uzHTQuHeQerb90JIuGYxKxoe_ByHW6jGFcMaZn_CtwHxSG7rolZAQJFLYX7kEVldYZLImY2djHK3URNd49EQIfahaCJLChOqRTWvA_vgjS1Hm6F5MDSaGgu4GZh9iJmXlz0gqxfH8fHtozqCb-z9Od1MIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=b6dKRMkOqMs9EKsxYBqcPcPTlRwZTUzpVuJ8TTbZBoIXUaNSbT_mZ4zl2yZtop2J6m-5YpkIj-NHvLtKOaALv3REXC9NXgGBOzP6OKF4-5BPOenXPuWVQ5doWeT7l-2n-qC6H2LTsV7xeEfYkvLa-RD9upyRH1BzhYqow3eIboOBkBp8I7RWlHsYsDm2uzHTQuHeQerb90JIuGYxKxoe_ByHW6jGFcMaZn_CtwHxSG7rolZAQJFLYX7kEVldYZLImY2djHK3URNd49EQIfahaCJLChOqRTWvA_vgjS1Hm6F5MDSaGgu4GZh9iJmXlz0gqxfH8fHtozqCb-z9Od1MIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTqtz-U3PdDQWJwyQMpaayV-CYgdrNrrUSAIYVdFZAcHPSoyeG6A-A_fSOzn6-ihraJA03qfvu8OvhVwGxcXknnCdufG4NzzFMPUh5UEHWJ3Kad1qpT4v9mu0LhCCqNgkDtVDMC9dwzqZpfY2xu1NlvQZXOCbxakxNFCwSRG6X3l5BOvAUr0EyGYpKg6mHEaD5OxhwZyEo19Uqy-I3xl-yl4NdRfk8dssF1tGONVWja7Cuj0H8IQwVOmZrk82fghlS968qRFR0uGF0tff2f3eF6oohzhHklx49xF7rJlpAoMotkt31xtxXXLvp5lZeVv5JW25X5pFpK33H0yIZpCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=uYpR0rIcjpmSF84IWthfUxLnYqtjwrqtIZ9FVnwmm85AYnqI89Rvi5wUad7dCCX6JP_FrYLENwTDHoHu23VDne4WgY1Uo6I5E4qkO-KndcBB16c0lE-yCDA3iRnkqpFTLVaSiNi_uAHVx6yrZKJcCZrGfe6ETcfv_ElqD6geKMKpA3KvLgapUwzaxy85JdlTNpBIG-wKDCnxCNrnBVFaYY1KyvxYYCi_lfdEdSfsuUIyWAgVp8hhXENFdm4YCadYY8BgrF_g7_LEKNUviSlco0FnlRaUr72MnF5qPDmRmUl_bz97CJsW79QKZ5CtuOZ7R6Px5YY5LXdcknjgd0v7Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=uYpR0rIcjpmSF84IWthfUxLnYqtjwrqtIZ9FVnwmm85AYnqI89Rvi5wUad7dCCX6JP_FrYLENwTDHoHu23VDne4WgY1Uo6I5E4qkO-KndcBB16c0lE-yCDA3iRnkqpFTLVaSiNi_uAHVx6yrZKJcCZrGfe6ETcfv_ElqD6geKMKpA3KvLgapUwzaxy85JdlTNpBIG-wKDCnxCNrnBVFaYY1KyvxYYCi_lfdEdSfsuUIyWAgVp8hhXENFdm4YCadYY8BgrF_g7_LEKNUviSlco0FnlRaUr72MnF5qPDmRmUl_bz97CJsW79QKZ5CtuOZ7R6Px5YY5LXdcknjgd0v7Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=mXAfOUtunv4p1f38ldeNupBS1letrkVhksp0vMtmljq2gWkzfesfbYLKjJwgpvMM3Ks49seswMLgsGw-1ZeRCoGQebmZoribnsVF7AAMCGMrUPvncXL-NQliS4tqeI0IEvC3Ntkt0ut95r_SHL_0-jYJf-OgSw1BqIzt_-oPHG6Ct9beTAjKVLlhNvlYxmeIvLXljczrqKZcdt2RB0F_E3BUONwgw7dlr__dxWMpHNbLnwJqbRoDDgzEPwHcS7MVEvXd7cjuQw5FKch2AhzsLuoQRVfroFYK_fZHuOCGENTj-sQSBtN3aZ6GyT6lkuYWsaOcBJuNNx90KSwW5nHkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=mXAfOUtunv4p1f38ldeNupBS1letrkVhksp0vMtmljq2gWkzfesfbYLKjJwgpvMM3Ks49seswMLgsGw-1ZeRCoGQebmZoribnsVF7AAMCGMrUPvncXL-NQliS4tqeI0IEvC3Ntkt0ut95r_SHL_0-jYJf-OgSw1BqIzt_-oPHG6Ct9beTAjKVLlhNvlYxmeIvLXljczrqKZcdt2RB0F_E3BUONwgw7dlr__dxWMpHNbLnwJqbRoDDgzEPwHcS7MVEvXd7cjuQw5FKch2AhzsLuoQRVfroFYK_fZHuOCGENTj-sQSBtN3aZ6GyT6lkuYWsaOcBJuNNx90KSwW5nHkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=Pr6ffrQK7phMbHvdIDkHTb8gfljCWHynQonOL8KxRyow8rs_uT2N3qlULzReOthGZYK-ty4uBx2b2FsFJ3TgdUL3arpVRZ4gnQ16tOKTqvSBS-ELG8ihq1flSJy-E7wrra8kF5iOXlx0PMO8DSBWxlzTtCuJRRae5zegCufVfI-00-Y830oWR5Zg6TcXRmpczkmiEpg08To7URQ-6yL_WadVoe5yZ-ZZmnx8GzD_DTmkRCwx6IW_DLkDNbydcUOB5mdV7qGu4m3xx1Q4JMQuTmJ_ke_kpMxGJl5hvuqnmjpmHqaTQDr8im_oBrmXLqtPAXy4gd9Yrs5FxuE2Dn4GVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=Pr6ffrQK7phMbHvdIDkHTb8gfljCWHynQonOL8KxRyow8rs_uT2N3qlULzReOthGZYK-ty4uBx2b2FsFJ3TgdUL3arpVRZ4gnQ16tOKTqvSBS-ELG8ihq1flSJy-E7wrra8kF5iOXlx0PMO8DSBWxlzTtCuJRRae5zegCufVfI-00-Y830oWR5Zg6TcXRmpczkmiEpg08To7URQ-6yL_WadVoe5yZ-ZZmnx8GzD_DTmkRCwx6IW_DLkDNbydcUOB5mdV7qGu4m3xx1Q4JMQuTmJ_ke_kpMxGJl5hvuqnmjpmHqaTQDr8im_oBrmXLqtPAXy4gd9Yrs5FxuE2Dn4GVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
