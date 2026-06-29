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
<img src="https://cdn4.telesco.pe/file/I4aHwKbs0rQ6BbiQKC5zczX10670ykBkK0copiM2clwhZTrmfDGnA09aCgXaYlAA9P8G2sZxHRPoPgdHOA75O0XdxO3DRDd2jzsQoQgVGUOwmJERA-Igelhss8akD7FlPsRwswqBUn1Zj8HEniBl5RCV3hRhXfk0CsG5kDQeFdsPWwdpkgfvDnHHW-JUT9owANJxOQNv2ZHi2hC-wvdYzD_mQRubXccffui-45VDM6D6qeucbJLm9Gvsz1UlLnG_xro4hROlkHy--PrutSMfM-jJ71-Nnr4XtHjkprS-6rqBl79OmwoiLr7b-XctKqs-qYiYeD81SG_7tQyWHwLl4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=o0va46qdIpLUVhtLwk-dfVjI7-Dps5LsldJAQANvLdwrUOsmOGC31LpQPm_UpSbdJeO7wrGqsTLIGLI0cDG3J56wSjGULLeMZ2PPEuittMrJt1JrlgqLsDHfUsxReBE1tKeOu_mtB26P8P02l6Fww-2_qpcsOzc3rlDOlRGNygZSkG8fruNayz4GJFMJZVKm0UwFBKWBZSRYW-3pImWdbORepn5u-sD2gOcHDsZRoggXTdLiVS3oyo1P2PqsvIKbXj5MMIQ4EbjOfUSd5J_onlgpGTPVCxt-xKN_zMXf1xmqESg8q8Nir5Dh3uPtmHniUopu6VsU_1AM4qQsuT5g8rvy9hwLjk8ZB99iDJxqgCMPDc3JL_uZiT5jARHL03lOmaJre0c1ExtlDHDyN5pIg98QNl5hjN5f1O0L70aCFXYgPW4wXmCOofWzLhZ9evLuaRc6zQ7PbEkclKHXBQpZ0R6m7VOl0TCu_71ebkhqFSbOeWFbUjyUWKROqTj-sh82SpfwyNv0H8Ca_63kkbRmR3lP25mHN0Kdc1WGiu5pOmUDhxghh3QKfehO-UWv_ppLBf6ruuvPA0_4ru2RSVIX-gKwInl8qLMbLU6KFsQCNL7fYEfLpFppOK0XIh0erGG_P1HBylVKmfsDd0Y7Q7MZzPRLGwOID2x9LO2KkUHAahY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=o0va46qdIpLUVhtLwk-dfVjI7-Dps5LsldJAQANvLdwrUOsmOGC31LpQPm_UpSbdJeO7wrGqsTLIGLI0cDG3J56wSjGULLeMZ2PPEuittMrJt1JrlgqLsDHfUsxReBE1tKeOu_mtB26P8P02l6Fww-2_qpcsOzc3rlDOlRGNygZSkG8fruNayz4GJFMJZVKm0UwFBKWBZSRYW-3pImWdbORepn5u-sD2gOcHDsZRoggXTdLiVS3oyo1P2PqsvIKbXj5MMIQ4EbjOfUSd5J_onlgpGTPVCxt-xKN_zMXf1xmqESg8q8Nir5Dh3uPtmHniUopu6VsU_1AM4qQsuT5g8rvy9hwLjk8ZB99iDJxqgCMPDc3JL_uZiT5jARHL03lOmaJre0c1ExtlDHDyN5pIg98QNl5hjN5f1O0L70aCFXYgPW4wXmCOofWzLhZ9evLuaRc6zQ7PbEkclKHXBQpZ0R6m7VOl0TCu_71ebkhqFSbOeWFbUjyUWKROqTj-sh82SpfwyNv0H8Ca_63kkbRmR3lP25mHN0Kdc1WGiu5pOmUDhxghh3QKfehO-UWv_ppLBf6ruuvPA0_4ru2RSVIX-gKwInl8qLMbLU6KFsQCNL7fYEfLpFppOK0XIh0erGG_P1HBylVKmfsDd0Y7Q7MZzPRLGwOID2x9LO2KkUHAahY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdEhpHlpzfRLUmIiiACtbk4VruEym-8yMhJUI3ws_KrtOOVah5v4yncrkoT24qXAJod9AQUAmz9oT6WdH9esAUF8j2JF50fuBunxsyanTppbajCWi131vuUkREO7GwwADzYU3gGFV2t7JI-IddVi4oaxIxTVAPk4kAxGOJuWYWnczK4_PX6its-vvHYrM8UZyMELaghydCLvkPrS3vL1Ypd9IQuWSws-EPykhhlpi2CxTyDpPmhOdR7OOoGgc8C-ydC-rc0ywcgaGxZbQIMApbxi9JfJS_B1gJhfgTaQW7F8rV6HIYkgabftrtYEAc3AcEUWbUWnkqA_LkXLEIin_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=G406c2S-_dYlMw4kDTU66txGuG2oFeEIxTiJZJ-JULqbAxjiR3jnnjgmxPNmHCzpLOltf2ysRwMLhxx5CGDjUwztFRIYGkHC6KyFwTWNXAJLUFOR1mos1MbDRByAGxq7NiLwKLKaNtH7lhIKy1JlwGmuszC-x9ly8uGzPfZRf0ziau5yMF8iUWkYnvq4soNZdcdyK02r3nWMlkGNPmdo0DKfM5hOGauY_vC2iHTGSrLWGjwY6KbvyB4XQG9xo0JLy1gaV84NjGKLL5XuJRqZHWRXt_kgEkQIKlxd3FwPLF3uqCfMxAK-9jWilpCfAN7XgVKWOHHIGJ-pcmj8S_pZGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=G406c2S-_dYlMw4kDTU66txGuG2oFeEIxTiJZJ-JULqbAxjiR3jnnjgmxPNmHCzpLOltf2ysRwMLhxx5CGDjUwztFRIYGkHC6KyFwTWNXAJLUFOR1mos1MbDRByAGxq7NiLwKLKaNtH7lhIKy1JlwGmuszC-x9ly8uGzPfZRf0ziau5yMF8iUWkYnvq4soNZdcdyK02r3nWMlkGNPmdo0DKfM5hOGauY_vC2iHTGSrLWGjwY6KbvyB4XQG9xo0JLy1gaV84NjGKLL5XuJRqZHWRXt_kgEkQIKlxd3FwPLF3uqCfMxAK-9jWilpCfAN7XgVKWOHHIGJ-pcmj8S_pZGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=a2H8XsKrIa5N9tvRoARqQi0fIp-oCavmu7n5CdHQpWGHOfUpSi6g7JHN4DwsTVE-2PB5m9EKs796bYvUgeZ0FOuPK0NLH12QeWXCP_jHnkHwK4uGRgQufcpsOy0pOuZTp67aRvGHQttjeCds2xqYnnIJmnSfuUZw5zyG2GlxYaAzluPy3Vebq7r6us1fS6INOZQBQLr7K4UcviOj99486jxzG2PCBKA8kyWSNrf7leO3kyKWwGcJNAbg69OWFDjwgJce9J3pl9bvVsxBSeGNfI33-EfQbSTrY2p9Fs7ik7YDgVyugiHSys55ebVK8krkZXFvwuSJXbh4jdUXdeknCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=a2H8XsKrIa5N9tvRoARqQi0fIp-oCavmu7n5CdHQpWGHOfUpSi6g7JHN4DwsTVE-2PB5m9EKs796bYvUgeZ0FOuPK0NLH12QeWXCP_jHnkHwK4uGRgQufcpsOy0pOuZTp67aRvGHQttjeCds2xqYnnIJmnSfuUZw5zyG2GlxYaAzluPy3Vebq7r6us1fS6INOZQBQLr7K4UcviOj99486jxzG2PCBKA8kyWSNrf7leO3kyKWwGcJNAbg69OWFDjwgJce9J3pl9bvVsxBSeGNfI33-EfQbSTrY2p9Fs7ik7YDgVyugiHSys55ebVK8krkZXFvwuSJXbh4jdUXdeknCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=nFstDO0puA0PKfLIsGDB7gSffiPESqA1GmWe8CoMspohaSFEQsBYFLSNPq80YMgBYCvbRyCml_V5Iy5sElxPQPSdcyIlsha1D-PzaEm-1ycr1BmRvacSdT5ToaRULoQfhHlcI9eJHIixZOWg3hzEj0jnLnSxyGlmD_vyqU5X-KGOZkwzbtGypcz7Pzev7cAmj8E43oynVChO1A5fjaGqGaQOjIDxLJjyXQh7QFPsgTKHrfkEzs2M8WnoivI6Efisa_pvnrU-vnM_utogPm1uarqh6ABVGdn8z3iCciTZ_CNfbD1lZMCbHdkw2XY3qfSvZlAcI9UfQBxJqNKFNcrwtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=nFstDO0puA0PKfLIsGDB7gSffiPESqA1GmWe8CoMspohaSFEQsBYFLSNPq80YMgBYCvbRyCml_V5Iy5sElxPQPSdcyIlsha1D-PzaEm-1ycr1BmRvacSdT5ToaRULoQfhHlcI9eJHIixZOWg3hzEj0jnLnSxyGlmD_vyqU5X-KGOZkwzbtGypcz7Pzev7cAmj8E43oynVChO1A5fjaGqGaQOjIDxLJjyXQh7QFPsgTKHrfkEzs2M8WnoivI6Efisa_pvnrU-vnM_utogPm1uarqh6ABVGdn8z3iCciTZ_CNfbD1lZMCbHdkw2XY3qfSvZlAcI9UfQBxJqNKFNcrwtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=tMbgw8EXpigUC-SVqV-UTWKYl4CGG929eOBvXKkGDLH6qeD9mByOehdb-dK-g4f7BtC2Te57XHi0sfN4N6D32D-DTHMO5Qxu7_tat1o_yehqdObgUFkRttEKXcZknV7WyBCH-DNYFFe-Y1vGDs0yKkC0-G-Kd-ywPuCeBrQULD0ewK9DDSM8p6xi7kd6Clf0yuGwgIX9Wqc7G53-5kRWXxoZ5ybnGlq-U6qPEJjt1ia1TVl5BZwy9XH2GQV8B5vXtUHr4Lnz_XGsN-A2gMtqSIMZoJBNjQoT3KVn3nZF6IHAgSHKfieoWkUwTEnk86KRo2iG1MM3xfyup1G2Zgvg1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=tMbgw8EXpigUC-SVqV-UTWKYl4CGG929eOBvXKkGDLH6qeD9mByOehdb-dK-g4f7BtC2Te57XHi0sfN4N6D32D-DTHMO5Qxu7_tat1o_yehqdObgUFkRttEKXcZknV7WyBCH-DNYFFe-Y1vGDs0yKkC0-G-Kd-ywPuCeBrQULD0ewK9DDSM8p6xi7kd6Clf0yuGwgIX9Wqc7G53-5kRWXxoZ5ybnGlq-U6qPEJjt1ia1TVl5BZwy9XH2GQV8B5vXtUHr4Lnz_XGsN-A2gMtqSIMZoJBNjQoT3KVn3nZF6IHAgSHKfieoWkUwTEnk86KRo2iG1MM3xfyup1G2Zgvg1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRmKh7nnoiq_slPtrr3Fdqxci7VwlvKthqGrG1ZbdRd6qs6NtVUYN15HzKPOoKOKlvsDSxn142MSm85U1UNCGIoQhzmyF7VTVp6Dft_h21YiCRtUfTUuWLLt27yTK2tCFt6VwDcfXXV8gfu799HSFdOWE0xmqzuAB_Fy7SDXEkqN41qdy-7CpKeSaU6k8kXJN4tdKiYJeiz0unUk7SsfsjXQMqI6NagWjLXpxpRpTqd2RYyLA8h0jO7vqr72eurz6c8tuscLm72b4E917uWuIkSUNlBBg5t8PB8TWRlOMQifF4vGk87lq3ltsHq57-eanyEBotUxDn3ulgZtlnFwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q1QuHE63OsTASea9aKnkJrAOr19Vdk-1EaIUgiF2znWyfGvLy_Jv5LRSfirXLejJqznD4kn7yEUeZ2evYDdfFVaabshRAaFLbyEfHSKJzkIxYCVKRuqPxSLX4gEdNdLVyZIMFUzvaXYN0YXRxTMoBhbikLIG_oFZ2-8ZTeb1tKwA98TauuW8rrzmvUVNPcX2JS9F4g1ZAJo-9R_aHeW1uD52WJ39aMmbwArLT9Fb9RErFtnRJ3zHgKHe6QHFp-Ku7BozMF63jhPdAIuSRfTz_jnTawqyGtCSGUgCMWfDarGVz8rz_MUrHirI2BbM2E1e_aGMThqF-tJorOuSWFdBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Z8_HBrdrLAvPtTFIdCsN6vFEkIxXqTp8FuSKjb4Cj7mCl1h1IoxFG2QYtXvxhiyflSCkQnkHiWE-6yEX31fmjsVONKGh3Iyxgd-6r-2xlVO8jJdUlkdbfirdk8WqMdeTLMRvWTIcxkjqAmszwyZD2_JUUdKzewvJetLfSlGz0_8OJhcrLOff9_nDdzqqPsMhKYfoqqtDSc0wfO51giqLIQhzUpniCKM2mqq_7j5aFFszpoJ4azbmBx0GYXNwKGi7uradDaHcSmeiRPKYtt-z3SNPBQIOGaR3hMqa9Wgb7q9OtZ6jDnmEwZYAtKYfxBgdnKFY1wy4Qg5zoyG7ELHIkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=Z8_HBrdrLAvPtTFIdCsN6vFEkIxXqTp8FuSKjb4Cj7mCl1h1IoxFG2QYtXvxhiyflSCkQnkHiWE-6yEX31fmjsVONKGh3Iyxgd-6r-2xlVO8jJdUlkdbfirdk8WqMdeTLMRvWTIcxkjqAmszwyZD2_JUUdKzewvJetLfSlGz0_8OJhcrLOff9_nDdzqqPsMhKYfoqqtDSc0wfO51giqLIQhzUpniCKM2mqq_7j5aFFszpoJ4azbmBx0GYXNwKGi7uradDaHcSmeiRPKYtt-z3SNPBQIOGaR3hMqa9Wgb7q9OtZ6jDnmEwZYAtKYfxBgdnKFY1wy4Qg5zoyG7ELHIkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ot432rS62Td3kR6ec_wLozGEAmBdB5rICwc2vneoyJPfgNYl6DvTN8hKzrGTPyOqoRby25hwW0C0BmLGteuMxyCToz6cvia77kY-3hIYT6yO1-1eYZYJIHaI9gsGTqGZ8i9TMKJTxiGpRa6YVGxVAXf3aiLhmK2vJMMRKOlLIY2uVPqvaAxyLCmVOcefczWPP9UOp1cQzTCDwWYjM11sShifTbeIewFx8l2pg_K--wUeEn0F1JtSpdt1s3WgFIpqGHCPqsVzxmp5Tqhp-vCDWlsoPZYHmT2fHufmBUh_73uqG8_R4v5oxOoucuak0MMwJfPHPWSi0wFEJ7fLHJ23Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=ot432rS62Td3kR6ec_wLozGEAmBdB5rICwc2vneoyJPfgNYl6DvTN8hKzrGTPyOqoRby25hwW0C0BmLGteuMxyCToz6cvia77kY-3hIYT6yO1-1eYZYJIHaI9gsGTqGZ8i9TMKJTxiGpRa6YVGxVAXf3aiLhmK2vJMMRKOlLIY2uVPqvaAxyLCmVOcefczWPP9UOp1cQzTCDwWYjM11sShifTbeIewFx8l2pg_K--wUeEn0F1JtSpdt1s3WgFIpqGHCPqsVzxmp5Tqhp-vCDWlsoPZYHmT2fHufmBUh_73uqG8_R4v5oxOoucuak0MMwJfPHPWSi0wFEJ7fLHJ23Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1q71CYhLnSDuybInhRzU9CHxv5rDxKGw4PYGH2mFPKHLV5wsQK4v4VNYgs16WLLncdYVmhkIrDIWPhverll-2TS401dKAZzPMG1JETWd9Cd_ERR2PElraqY_TM4cZNrH8u1zDwyC1hjQ-PRvpqLCYQnuZEHcqfbLS-V3paWA_V4LsOB-noLR47M0T0Scl2lL8pdw0wLl1kf8SnUMvzk5JQ9qB73fdxdEb3i8X_6T4KT0qMTLGJFTLIR5VNVZSXxC7pFn9tZcpvgndkxAUVW8fGN8aRAlnOX5FUZAg04nAfI0xtEjDsPXBth67rUnghaMly9rOTr6BpzXrEoiYv3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=NMgzHPrzWv7xXAJC8BAyASoAvnC0doj6_choqWgHamRYYoVKZs4SWPy7ZGF0AZXdICQaZpsPsYTFsqOQJafFShkVQTKeGMqTYF3gFiEMdY3Mn2RE_771wobDcfBD0ojT2UXCjrTTrjZ7vMUS4P1xoqJuCouJ_fwsGOAX4LPH0N2WyZTW1xdUdmr6EqHqNehvPc2ixyNlA8s58eeD-ZnaHfvBaHGXZdTFQX1Zkd-snamLjgN1ppLziWOT-pO5sx4ImRSJL5wqyGBApqu0SrzoNXSnkcaTh1DrP_L54_v9H_8Re_p6_RKAQlbn8iteUYSJNvWrOzgfw3zjsIWIwpH6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=NMgzHPrzWv7xXAJC8BAyASoAvnC0doj6_choqWgHamRYYoVKZs4SWPy7ZGF0AZXdICQaZpsPsYTFsqOQJafFShkVQTKeGMqTYF3gFiEMdY3Mn2RE_771wobDcfBD0ojT2UXCjrTTrjZ7vMUS4P1xoqJuCouJ_fwsGOAX4LPH0N2WyZTW1xdUdmr6EqHqNehvPc2ixyNlA8s58eeD-ZnaHfvBaHGXZdTFQX1Zkd-snamLjgN1ppLziWOT-pO5sx4ImRSJL5wqyGBApqu0SrzoNXSnkcaTh1DrP_L54_v9H_8Re_p6_RKAQlbn8iteUYSJNvWrOzgfw3zjsIWIwpH6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=DF2nxGBaOeE7EapkCI_WOLOJHa9MzLyyzXk7ktr4nl5H6LqXxLWzyESQOVlQwnr5_pufhS7iHEgD1Clg7SSIYcMWEXAtOvFbkRXbEA3VT4hjsvvGkmh9F_gxEtcNpf_WpMAvc3oozHhQMUEUVGAIMgybUWKdBl06xusQDHIp4KzDQ0XEbpAq8kidG9g7wcOAcc8QL0Wo3GFS_x2zlp1GmSJ-RSyGckES5R_aEUVCs8hz4RGjkQNLvbeRAL5VnhDssy7vECJEvfLTbeXKH3sc8yQDY1y0Q27c7ocOIOsu2hxh7w3HTI7lFtMouuT7E1xif7ov5n3-FYZWdME56uDOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=DF2nxGBaOeE7EapkCI_WOLOJHa9MzLyyzXk7ktr4nl5H6LqXxLWzyESQOVlQwnr5_pufhS7iHEgD1Clg7SSIYcMWEXAtOvFbkRXbEA3VT4hjsvvGkmh9F_gxEtcNpf_WpMAvc3oozHhQMUEUVGAIMgybUWKdBl06xusQDHIp4KzDQ0XEbpAq8kidG9g7wcOAcc8QL0Wo3GFS_x2zlp1GmSJ-RSyGckES5R_aEUVCs8hz4RGjkQNLvbeRAL5VnhDssy7vECJEvfLTbeXKH3sc8yQDY1y0Q27c7ocOIOsu2hxh7w3HTI7lFtMouuT7E1xif7ov5n3-FYZWdME56uDOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1vSYvEDcq0l4ZKUSn0z6sN-oYHQmCv0-V9H7aFVKPdulX9_Pas3013MzLKtywWtjEufUgjWjBzfaGdddh5xziVLc-v3yxEtej6Rikgw6wT6-zfqiGE6Xko0FzUfBEqKcSdcXZvBtLYl45N1mVKb-18w7RE1uCH_A9iGjPnif3Wfhk1LUdkdkR97B3icYxq-8djgmMT7Mmk_vqffFg2YCBrWpPnqe_o1mcFLVIjd2YYHxFTAZEVr8SWnZn5WhWI87IC47et5pzO5y-2_V3ecPWKauncr0fl5HSVgVP9poDCbXf_mvKuTOVuaYUKyGhWiKw4yYbdAJg5C73ka2DCcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvnlZH-QNiC2Ltq_mHe9ekVhgGZ9lDrAMKIgTJmpRs53XL6p-KKtc0B-F1ljXS2z374u5FIgI8Lu71XhzACIX3Z1OqOn326mzpM3NUZ5RbxXNdGVDFx0o7J_cPVHKakX9l6Dy3uKgUKtTYJePR1-C9QxEJ0jAFEXnUckbJUm6KsdGLf01MResvarSBmvw7KddVgJusXcfUZ_9oSYwG-1wTP4fPDl63SXnuV6RpatNe6ndJ5YD2R-qiDeF41-XJEzHJHDRoBRhA3F0Ir9YDwftswOZUi-4BSHxEfJMh-llgeE0-D38eIrCETKTymbiST8rHQHffxaIeQZ9yfkQoqF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9G-ZtQ3Lrncz9vtTI5IPMhWmXqK08eNnO8USvvFS6AscUQjOGZEtM4ia0B-ozEj59kyhLE0cytUt_gJ_PiiKyGWAqb9Fif9Bi_E2qeur0GxC2o95x8xW9-oyzwGyTxStnq7OdgMTYTjED4jAKU0m8GM-GOy98MQuvujnHyF8-mtja6fu9wOq44mnAWQdJzklpz3NQKIDzbutGOK0olsZ-usIzFlhKz02m9eyWZCV-zbBKCrbNhcLv92HRodA-luTbmQwEsoNmHDIh9ndxfFyoSgGJDJj4_sHv6kFfnqRAglMS1_EbaD-OwzTpDdarok1D5ktjL3i3OtkGxG7R1GfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=YSHPKGdHt9PaYOuxS5_PajL-93r3jUbXebT_8zsVR11dKRl6nSyCLP_N7-2Qte4sCWH263luZ-8X1jhy0A1H6fYFV2N-lKgAU8YOd6MbEFbwEqkhk8fz8U1pjp8rg6XhfD3byROnBYWnLIMYv-hptmJPgeFjPXl2ZZPwJokEITYs1qdxYblapAOpqdjVmKmhPyr1lcmt6mE7tAMDBbaA9-zjS6jybr5aVaZEqrUMEcnIvx0feYQbm4Lo7V6COVfVnarSmYtKF8EJNFNp41HUt9mKbovrhc0Ze2ikXNhMTvdnXzzame3BfUBYwTa7yLyA9tnXUA4yJ4As3ltxfuDpIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=YSHPKGdHt9PaYOuxS5_PajL-93r3jUbXebT_8zsVR11dKRl6nSyCLP_N7-2Qte4sCWH263luZ-8X1jhy0A1H6fYFV2N-lKgAU8YOd6MbEFbwEqkhk8fz8U1pjp8rg6XhfD3byROnBYWnLIMYv-hptmJPgeFjPXl2ZZPwJokEITYs1qdxYblapAOpqdjVmKmhPyr1lcmt6mE7tAMDBbaA9-zjS6jybr5aVaZEqrUMEcnIvx0feYQbm4Lo7V6COVfVnarSmYtKF8EJNFNp41HUt9mKbovrhc0Ze2ikXNhMTvdnXzzame3BfUBYwTa7yLyA9tnXUA4yJ4As3ltxfuDpIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txE5BLGY47fqy4AdX46zKMrx8hN7TiTCWmMXUBZwcI5n-Lp9lld0B6sue7D1K3S10gSYwaQj1XpnCQieJDM6k0hmbA7U1X32HnPPwprlx7bdxW44ntKa4HyHn0PseUKSZSSiUIPzLWglTHvwMKe020kLhiKbymTrD6WsBVysiFODAj4zh5U0iwT3WNyzeBUVALPFIyswQVLYlOa7LdZsdtJak25WTlLBDVMPetNomVse1OtVGQLhPQDtFI9yWpjApLzqXP_mUCMciyFOC8QqeCz8-uNaRB9E0PXrxOJdryYecgo_xy_vV37k9pa8LVKKqpoIUs4m6yiVXbfaVxr5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdA217xoaLWDtcnNFlCbFGYMTsB65mE9aZ2Y-kQ5iFkkHbJCkTkJyjcdSVNTQK1AKaqx0_VmkgcGI9cGXk5F7LMdfOa0uaJ8yshmH6_gvFwchvL7_oUi6fI0vn-RobnGhLFGuWLmXCoYT_4Gib7oIl5IXzzibpx4QTPjY93ttEhQnNAWCJAH7EIIJ09x8I2sbfeHgrsLXftBT2vc5tcmc6mnLsOzSEUd4ce0K6oehhD8Wtb6debAOcdChMPgp4g-9hN90TR75iyoooVRgoD82GWZ1GkZ7qxw1GuK7x73pR2TtioKfMAH7PvyPleTkkWX1jRPxLLqZG2vSnNxkbgRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=mSl7-pZNuLVQgDVCFwaZ3nkPicvCYMZHKy3yuitS6-eD6tBn60wy_Hn4vzanu1zPYJ8YkPiXvPbCQ32t-gtdYRdDXVI4sEUhE3HPZYt-1AvKJEPuIeksh1PHKa86OmSerjCBRKejAKfj_zjwu_fR4kTvVfMcnQhdR_HyMcUy3i80Xo_1weGfq-ZsZkv1TlgwMJQmygHqLBGkXPvmbLgsOME7he6CamdhZty-wxO69LYr5pw0M5CBpj9UJpXhrPpG8HsJRk00VDYg1g7t9gLyd6jwK30flkcM93z7EBOTbfDoE7YsWoA5-GBMHsRon91rQSN-KHMvgoPvbt2fxYSjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=NlxcDwdQlOnTsPz7VqSy5kqrI5aNrZijwu26OWwjyBGlDB7Yh-YzHfR2x90TSkIYjJGRN6lSTcH_q4CPwuHGlcSTt6jiq5ygNaeDRZuNZ8--4R6FVm-6Wfw7EtXZa-2ZBSl-snOYdo8nslQ9YiBpR64xAZxCsix22Cd9nx31lXyuDz05Fye6zOKxgBMMrzjw04nIqsuEoKRKA3CUEU1E7sU9AoIxfbD4xFNWg8ecgtxL9raEWsSloUwu9DYKIoV7LmcaZTba7RjZCDlxOaFPBwz8N1a-96do-KacvretjcISFtfKSaSK8ll3Y1vvfNrbeNrM_INb9_RIi6S-jMXT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=NlxcDwdQlOnTsPz7VqSy5kqrI5aNrZijwu26OWwjyBGlDB7Yh-YzHfR2x90TSkIYjJGRN6lSTcH_q4CPwuHGlcSTt6jiq5ygNaeDRZuNZ8--4R6FVm-6Wfw7EtXZa-2ZBSl-snOYdo8nslQ9YiBpR64xAZxCsix22Cd9nx31lXyuDz05Fye6zOKxgBMMrzjw04nIqsuEoKRKA3CUEU1E7sU9AoIxfbD4xFNWg8ecgtxL9raEWsSloUwu9DYKIoV7LmcaZTba7RjZCDlxOaFPBwz8N1a-96do-KacvretjcISFtfKSaSK8ll3Y1vvfNrbeNrM_INb9_RIi6S-jMXT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=YkdBmjXUQ71CcxcDqsSJ6OD2HPP7IKqQDPM0yqbl20kKB3Vl-ezWfRhKjc28mHyfvz0lXiB7noQgyhfv8UtV6YAGe_AwmaFqo5aRDxLpG7AQj8CdJxnsAO1c-vtfXXW6X_D-xH5Xstu1Jf-x7vSwZ8rfBsOiqkZoIs-5EE-CIZt47oZpxQ_xKCUk83HDdk8g4TYF4tPTBTZwbmc-Q_wS2otJoUXvPWbr20zMngVOzVNmXOVd8I2Dbp4OfVF3_y4Jb53H2J6EVJhi3EfTNeosp3zWL941S5uc5h6lDCP7ijb61bJLP0CCZ_RupMvVwXYkBPxXsKsPiKNwA5mTLKKNow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=YkdBmjXUQ71CcxcDqsSJ6OD2HPP7IKqQDPM0yqbl20kKB3Vl-ezWfRhKjc28mHyfvz0lXiB7noQgyhfv8UtV6YAGe_AwmaFqo5aRDxLpG7AQj8CdJxnsAO1c-vtfXXW6X_D-xH5Xstu1Jf-x7vSwZ8rfBsOiqkZoIs-5EE-CIZt47oZpxQ_xKCUk83HDdk8g4TYF4tPTBTZwbmc-Q_wS2otJoUXvPWbr20zMngVOzVNmXOVd8I2Dbp4OfVF3_y4Jb53H2J6EVJhi3EfTNeosp3zWL941S5uc5h6lDCP7ijb61bJLP0CCZ_RupMvVwXYkBPxXsKsPiKNwA5mTLKKNow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=WF4mLTc_7M5gsN2wRX3uJvA6o7TGBPKsiZImu5Ypf2WKvv6JyiVqcqEBYGukjf_EFoJqrlHqyC7YP8ASWRSU2563mt2IZ96_YkkMm4JPCag2pnx2X_yTb-MFWFwjm_xIr7ofoCfybVIiwdmkaRQQP1FO5sNpdGmomXcw014sv5er-6TKkyC5sfeTlppLgkiNWMhL3f-xAjWeZ0QU7c3ckxCa0i_cBrSnsNR-HCuX2WezJMKWeH0gvDuQSwvS3EcjmbjDFYxMXCxaNrgx8X-YYEbRpoJmGqO_721Y0Zsnmuipc0lRsZxIbs4DuioBCcDJDrv6hRtTQ-pkbiIfg2m2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqY1hWjfaUckfNEoKctyqQ7wOnxbo3CMzdmWor4-uPGNeW1owAhlanzMmxK-kLAwqhtNwUj7nHfU0s5-gM2un2QUmzxshbHYE7XO5Cex61csJ19L68oFbO2mA1Wwr0aBuig8lmTYjI-75JahDl2Lcm0SiwjkyCQ2E7a3__MV1RGs4hfrHqFZS597Is43s-MfYfStKfzWzLe9nS7Y2gnpwI4aCYZfxVVyimLexhsCR8xqfyOqn5IYZOodID52SWtuWnSakyaDE5Opt2T7JbRozwY_dmZXzLb9cGH-404vL2aBrjWPlHwtwwV8D-0IMHvQMvoAkTgRiATsJcf8bxFidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=sQEDW5Q2shOijTMKR32L2J7cAIn00nITrwTC3DowUYssXpR66C8Uq7ax_A0xpMOLjXojyBvbWnXfWc7SpXEpqfVOc5Fdl0qL_31iaWzfLfrqbkLLEoBSsgcMh7KoMoI24tQMwZYV8_FW5VTyEza0nggy0k04Cbg9h573lzqG2ewJ8WgXU4a_7FGHniMzc5xe8ebSR_Eg0_i5IoAZAI51LcQQX4DwDQH02ySElZHEzlNfujo_hYxpUg97ZOtBtqT3xnekFt8-9Ii2MRqbhInwqpCVQzW2g_SnzoumPuouWw4eX6nCebidzDkONk63CMVTG5SkE5F1EI-ShR4guJfXNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=sQEDW5Q2shOijTMKR32L2J7cAIn00nITrwTC3DowUYssXpR66C8Uq7ax_A0xpMOLjXojyBvbWnXfWc7SpXEpqfVOc5Fdl0qL_31iaWzfLfrqbkLLEoBSsgcMh7KoMoI24tQMwZYV8_FW5VTyEza0nggy0k04Cbg9h573lzqG2ewJ8WgXU4a_7FGHniMzc5xe8ebSR_Eg0_i5IoAZAI51LcQQX4DwDQH02ySElZHEzlNfujo_hYxpUg97ZOtBtqT3xnekFt8-9Ii2MRqbhInwqpCVQzW2g_SnzoumPuouWw4eX6nCebidzDkONk63CMVTG5SkE5F1EI-ShR4guJfXNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFeG3hsmhazIenvADbsaYxau1cczOm-yNLXlgddShMuZ6u-5E5l_nGtt1KwILc63vxRFp8IOc3fheK2umQb1uVVhTaxoCqzMhQnFqXIPdcFEQcrguHYqAyHGR1dKegEMiN488Yhcm75Bu8m8vMVKYbfhDOI6zajHHpdWyZUfsPq8WWXdcMpv9rt0bar88FZ9nnACA8ZPlKkHksyhzgFfzEOBHEFqjnSeJpK4IHPiucMBltXANUkqkkthtxa5wghJPVsCubF-rJsebMYpq78ZGQpDhoxnu-fGC5fyvOBO4uskle0Sgnt8QP3o1ZUdBP7uow10-5Wz6hlbM2DK7fPE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPLlBT7bcfhTb6ASEykFEON8TbJHP1FIays79LVatqofGIQCBO3uzOeeiQBHzZN1vIyqZvu3EDTPo_tkpQdypnaiZvhAD1B9HJ4Jiiq8YYLCMKwSPEKR2XZzGOJHqHfxGDUr2eIwsMLt-N5Fj2Kzw28gMmhxiWS4LVfj_NbyRUw_ltmW_ReD511c6yo6w-eOhbRmqtaPF6gqGZsYGBO6KyTkB_AT9egLpQ3ANyrTfNr0xFlUjIbNx8o3hYKSbvKS2AMda5jUCBtPqlZnr386VKOiBxaQSA7m61y2aIudLrNxQRZDraZnC1UX-k_gQRK_2PkEQKpSszWch4YXpRS1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-7VJNbcxEttbbxId6ubwKYU626aScOL3HdlpTz_EHUnTvVUmN6QrNDB3e2sfj1IRLdAuqbJ4gqZhDBjZ4AKL7eFExIm9LpUkZ4Us3GfG1UXotvo5oWxqZzGL2sWW8HnA6MOP_iHyxZZfG1gMHseUvdH6TyPPwjtoh-O-CWyz2DbcPlLmfvMHD3p5p7yTC9UNhaO4eLaJT4wT3VQcQvGI80zwkfIDYyblsDJNToHfQYfkEzFAik39th1KtOykY9Qk0-YM3iL8D_ssiQKxWi794EYWQV7cg7gyW-Ig-5uezb1bFg-aiOvm05kuDd0hCu-AkknstdABn0f_Cj6a37BWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=Q3i-cuqzflIgRuUtkcxXF7Tply1C92F5ngT3Ahwansiqog0HS0IvxGTThE5fVcpK0KXzHck7073Jdu3KcuMJLo6zrbx0EXPJnDQk6orjg_opryxS_XSTq6ceHgPrXYGg-jmr_bAqRfVo9qegetOia4CMTFjlmKX8My1gvumhwFbxdfcTkZNUV3SzhlmeJvj_3C9xc4g4GroGGfefbNGNX1eNyTTYBwDcufz2rKoRMGvm5gwos8tu85ki6uPiHc78Mc467heJc7CC7Oadkg-K-df3gFcC73cPRe-IwqZAKOU7jZnhVGQuW92IlWjzwP5GM2kZp2A8rsUhKBQ8w2Kb6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=Q3i-cuqzflIgRuUtkcxXF7Tply1C92F5ngT3Ahwansiqog0HS0IvxGTThE5fVcpK0KXzHck7073Jdu3KcuMJLo6zrbx0EXPJnDQk6orjg_opryxS_XSTq6ceHgPrXYGg-jmr_bAqRfVo9qegetOia4CMTFjlmKX8My1gvumhwFbxdfcTkZNUV3SzhlmeJvj_3C9xc4g4GroGGfefbNGNX1eNyTTYBwDcufz2rKoRMGvm5gwos8tu85ki6uPiHc78Mc467heJc7CC7Oadkg-K-df3gFcC73cPRe-IwqZAKOU7jZnhVGQuW92IlWjzwP5GM2kZp2A8rsUhKBQ8w2Kb6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIQM-uPy12KcyYUgBE3mioISFRhNqun5z3f6disfdg44e3bYVbWojHThe-CY98_dScLumV5cced1GZQVUMDXeYDe_z3i6lZu5l6tVgtMxO0nDv5CZ0dzmbPQy81CeBTvkaWyAb9dFY8lnxrx8CXtQrdRG0ksYi4gG9mSBpLItMqLxgSKup3ruOArsuPQvmJhmfJlrJO9Cb-S5WxiaUAsWjMnd-QyCd-hXq_iCr2Bz6epsViQAK7D_nBDenYssmCGRf5q07LC9aa6q9CPPRKlaFdZAGEPB-jWxXyhwpdgWKDz3FRrbppX8xhpWtqXmblmP19YcASm4JHbz3h1yx92bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=cQya6aNwGAf-3qY3XyJiyrlebNKE3FdHHn1vKZd6elaJxe9megTRMl4u7QkLVPj4yE6kreJcqdREPKvTwZgzvSSYV2LTw3KA283H2ckOR9kc4YYuv5m_AUT-6kLGgGbkW_lq64LTetyQB9wibA1Obg60vqIKLZYJ1vUi0lB2Ixw8EI82pmSwylPioL35NlW4j5im6D4K14pXJKgI--6kCUxRBdWlUR5VzACMApgmVNuMLpL36S6CTv0zGdAgkMOXeW7jDueuURSkwgTlL_R9jKM2kBglPyfAP3qnwMxYf5BKdKweRGI8EL6vhPRCANE-MA7Q7C1bVQ9j54KsjSG1PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=cQya6aNwGAf-3qY3XyJiyrlebNKE3FdHHn1vKZd6elaJxe9megTRMl4u7QkLVPj4yE6kreJcqdREPKvTwZgzvSSYV2LTw3KA283H2ckOR9kc4YYuv5m_AUT-6kLGgGbkW_lq64LTetyQB9wibA1Obg60vqIKLZYJ1vUi0lB2Ixw8EI82pmSwylPioL35NlW4j5im6D4K14pXJKgI--6kCUxRBdWlUR5VzACMApgmVNuMLpL36S6CTv0zGdAgkMOXeW7jDueuURSkwgTlL_R9jKM2kBglPyfAP3qnwMxYf5BKdKweRGI8EL6vhPRCANE-MA7Q7C1bVQ9j54KsjSG1PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=ImNAtptpQN-djP-znLlLcdQl4i7o3BEBfboHxjAL2DJls19HiM06q9iO_DFpgy02BPWEQoM5IMI72d8h-AFTtp52qHKutShr9xCI_1JAtmgxL4Q32EC6bfHr-c6wNfasm3W383LL0mGapVDkmSWRuBo2ex029lhS_kOOzFg2w63c3OpT4Ph8ySYnFp524sb1OAYKihki9L6HI0Q-Mkrrq7m5VkXHI3vTpqmjGrhIW2GLKw2wYYYcSMjRsaMZvviDSTUTlj3ci0Y6YrmsAdfz7QuLGdig0g9Cq6P3FjFjzGXokchN2eyk5O3oBKaT9qQ0QZAx98jxv0tDgBYPzR211A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=ImNAtptpQN-djP-znLlLcdQl4i7o3BEBfboHxjAL2DJls19HiM06q9iO_DFpgy02BPWEQoM5IMI72d8h-AFTtp52qHKutShr9xCI_1JAtmgxL4Q32EC6bfHr-c6wNfasm3W383LL0mGapVDkmSWRuBo2ex029lhS_kOOzFg2w63c3OpT4Ph8ySYnFp524sb1OAYKihki9L6HI0Q-Mkrrq7m5VkXHI3vTpqmjGrhIW2GLKw2wYYYcSMjRsaMZvviDSTUTlj3ci0Y6YrmsAdfz7QuLGdig0g9Cq6P3FjFjzGXokchN2eyk5O3oBKaT9qQ0QZAx98jxv0tDgBYPzR211A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=vjJaoIGrfpuDO98dXrkjBSo4lWfZ42FXd_TzJOPboxUc6_2002pMRMVNizYwzXgNtV9aLtebeyBE9aNo5q2gtFXoOrpTyw3Ov9qREcKF0Ea_7XYof8qKdrHzx5O7ghxlxIUHnQbbnzxPV8KMcvdSyJ2AAkgc4iLrw-y79E9bPAlsSBe1_Sx21f-n3Oy6jTOYVymQvG6xXLeOhgLB2hpuiZwv2GdlpqoHLhYaaOmZvq0TbuXJC56pbl-Wb02BOJGLawpZ1cwMHLtkVmki0BSEUk7zkkKFS-mHaDIRG1RZ4sSSIMPi-aniQEzlGQmg8yopJtJGvU3OTLWuIRki5-0vDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=vjJaoIGrfpuDO98dXrkjBSo4lWfZ42FXd_TzJOPboxUc6_2002pMRMVNizYwzXgNtV9aLtebeyBE9aNo5q2gtFXoOrpTyw3Ov9qREcKF0Ea_7XYof8qKdrHzx5O7ghxlxIUHnQbbnzxPV8KMcvdSyJ2AAkgc4iLrw-y79E9bPAlsSBe1_Sx21f-n3Oy6jTOYVymQvG6xXLeOhgLB2hpuiZwv2GdlpqoHLhYaaOmZvq0TbuXJC56pbl-Wb02BOJGLawpZ1cwMHLtkVmki0BSEUk7zkkKFS-mHaDIRG1RZ4sSSIMPi-aniQEzlGQmg8yopJtJGvU3OTLWuIRki5-0vDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=swF6tAgMigf73FxfIsTC7qW_q7IohVA7zP1EJXt0vzgPG9P4mh0GFyvTogtZATbr6u4Is8JrAg_ISP_VQCkT7CxVRCRZZEbF_fpA5e2qplJQGe0jGfs71murjylB0l5jKvvyfjYoBFXYtMdQwxZwq7aB_0Ud3BqBbzrhF5eHczsTvo5wQqi4uILSIAcMN5Um72avUVUWXiQZddFxyXugn2ROFG21ynzqqpel0ui7DIGLEgUyBU0ChY7EezoSCdZr6tXJxD7AGsVSMJrE1myyX6SwqGJseXGNeT-G_RRjyDHyvygZzBcoqaBbJiL9x3sjDJ8VsJRvwNDDOkOYKYrO4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=swF6tAgMigf73FxfIsTC7qW_q7IohVA7zP1EJXt0vzgPG9P4mh0GFyvTogtZATbr6u4Is8JrAg_ISP_VQCkT7CxVRCRZZEbF_fpA5e2qplJQGe0jGfs71murjylB0l5jKvvyfjYoBFXYtMdQwxZwq7aB_0Ud3BqBbzrhF5eHczsTvo5wQqi4uILSIAcMN5Um72avUVUWXiQZddFxyXugn2ROFG21ynzqqpel0ui7DIGLEgUyBU0ChY7EezoSCdZr6tXJxD7AGsVSMJrE1myyX6SwqGJseXGNeT-G_RRjyDHyvygZzBcoqaBbJiL9x3sjDJ8VsJRvwNDDOkOYKYrO4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjTJBCv4OoYJEgeZ2eEAW8X7EnFNlUWDIKpKIibTw29DXojK1UIV-NVimrvI1p7KKibJwjfVuYLODvPWNzZsiCU4QMKUlKXx9JIUeHXIboqS84awCQyfShO6DNa9ZlLLmNPLKCpx8Xxb39zoSId5mnGcHZqlAYNwYFPN17Gs5ACpUB0qCisHm4dT3h06asAP5XzZdqp2g8Cs2xQPB670_NeF4OLxHMOY0bSBvImrxS5leFQo2XPnD0l1Byd49xF-JNASk9rAkiDmNiWnYYB9t_PQkQwbAHgVZ-5_iwzgTeWRKTJqooWdS2U0PhnapTxAMEOIBcTLFMPMujIFhVuklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB4gMXY4m4_ei8zPx8jodhLMJMvuIukPvHw3OeVCk9aF5ZAkVAdsuhCr-ZemL12ULojWIpcArG6tTe2q2TkVcSL4dbsCO2AV-sw6eOlebZLoNU9NuypFFnzLit-kDNIzhHI0JED8Jh8XJzelbS7gLAnN7A6gM18Kap1cwKMVquB-dR4nXWYS0copoqGVbqgNBvzq4kqqgPnT1v5vKEpdYpBfzxLumbRtur5VjhUaqc9KKH5rWo6dZM-OBNHFfnvUP8IyAIomq95fuoSSqUbD7dbdwH7y7BG8ObtYgoH8x29renKFH7WmO2LtiJYeN5VceQVuINEgzAby0dxpLSBdXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=JEQFPRlvc6RoSJYRVCaGj0K1LnXEotzCqKRif-p3saNl2P9M16tSgGqHR6XcamKkPdTZX-yNE7ZLXJI3RVnSgwgv5MONR9SFeDJDusxwP8tktjdgM_IbSY48vuplIh9HN2AV_70gFzOuA2I5J9_x9QhNI8R6HLhvliFJ8fgalSVSWiG21JBmdoLQyYHP0p7d0k3eg5-4ouzT13nNSRIcFRaEYOotZBImziN8PmLlh16KnP2JNM434Peunesbv4wqVD3DYJTvqT1KIZQaq1trHBZVL87qkdBUByjtL4F9GmlwYf14jVBUe6whaGSX3stlWgvLimZsVkJ4A-RXhwjxxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=JEQFPRlvc6RoSJYRVCaGj0K1LnXEotzCqKRif-p3saNl2P9M16tSgGqHR6XcamKkPdTZX-yNE7ZLXJI3RVnSgwgv5MONR9SFeDJDusxwP8tktjdgM_IbSY48vuplIh9HN2AV_70gFzOuA2I5J9_x9QhNI8R6HLhvliFJ8fgalSVSWiG21JBmdoLQyYHP0p7d0k3eg5-4ouzT13nNSRIcFRaEYOotZBImziN8PmLlh16KnP2JNM434Peunesbv4wqVD3DYJTvqT1KIZQaq1trHBZVL87qkdBUByjtL4F9GmlwYf14jVBUe6whaGSX3stlWgvLimZsVkJ4A-RXhwjxxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=RLxdkMrMNyhYpTcqVBVc51HW950yb8JfCZO03NoLL3_v5Q4yPJV_D6UoRDT08-OtZasSxL3aDkbFN8ULwY1d8-XbjlcWkGb5jKWeAON2l_rW06AbuVspjsw-3MACQIAc4m-IF5LoTW-bSxSQFO3FEwl6h99e3WpKhawj6QvEBLywRgzdFpQQ5MhvXSWBjObfx5QZv-VPHIg8HStqQBaoDLnzXfKXJ9p6MkIK88saCjqI2x90f5133Bg_-nHv5eWgkzYjgFBPUa89Fhsc3NBQo56aGmbDHcq42QK_srwadOB2bO_91GqdL-wlwE9W30EpAlhhgwE4NIMAOWCQWJQuFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=RLxdkMrMNyhYpTcqVBVc51HW950yb8JfCZO03NoLL3_v5Q4yPJV_D6UoRDT08-OtZasSxL3aDkbFN8ULwY1d8-XbjlcWkGb5jKWeAON2l_rW06AbuVspjsw-3MACQIAc4m-IF5LoTW-bSxSQFO3FEwl6h99e3WpKhawj6QvEBLywRgzdFpQQ5MhvXSWBjObfx5QZv-VPHIg8HStqQBaoDLnzXfKXJ9p6MkIK88saCjqI2x90f5133Bg_-nHv5eWgkzYjgFBPUa89Fhsc3NBQo56aGmbDHcq42QK_srwadOB2bO_91GqdL-wlwE9W30EpAlhhgwE4NIMAOWCQWJQuFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksSjTJgTlPoHP3Rg2ZdMSG31fYx_dBpP6S3AdxaQ63546gWQmoh2rG36_iffOKmUdMAW06GRcuXZjtijbtfmnmVi2smqZ-lSgHCp_rYqMvO9QUrpFZR7MC8iSsyZw5LhqGi-ebSNjbwhiSw-rTMwxUKcFvTQQdFbnuRR6phpzlPVGqiznte2hLUoMCSkvqcY4GOizfQFy48mbxtRKGOMABMq1_LY9uWCA-FBVHUqll5_wn3M9lXEfBFR_Uuc86p0GW9E_Kl2IpphRa_j_mRuxrR21Qh4pY7PAprfxYlh0yPAuSINgKtFU35YfVehSkgEtt_lURhw0sE9PaYjmlaAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=XHLFa3aYMAaE4NE9vLD2r0Ar7zscJx66axrRbDym00SXXvLElDAK3nfwjnRgQm_8DHQxXQYH_vTt8QS3AIVV6CtHq4kka66LpiOTHcBCGGc9X8deCR2WqsvomjFarAoMUygxm1lc5GTDRX1w8xceiFEngfgJNtJo3fkSN5xhgcxuVT2s_UUCacAYKLmh39zE9Hw3JcEJdhCR73rITkKiNm6eKscH8ZSZ0KmtUySJE3KRJ9I_JrED_U97nKi2EM-9LvG_c6Zjr519-eNqA5ReD6n1mn7xTmgooSjB4o4_F5b_IVR3ELlfgovEV0qsl-ZowFAcmkiOzQ37jLk9qK-4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=XHLFa3aYMAaE4NE9vLD2r0Ar7zscJx66axrRbDym00SXXvLElDAK3nfwjnRgQm_8DHQxXQYH_vTt8QS3AIVV6CtHq4kka66LpiOTHcBCGGc9X8deCR2WqsvomjFarAoMUygxm1lc5GTDRX1w8xceiFEngfgJNtJo3fkSN5xhgcxuVT2s_UUCacAYKLmh39zE9Hw3JcEJdhCR73rITkKiNm6eKscH8ZSZ0KmtUySJE3KRJ9I_JrED_U97nKi2EM-9LvG_c6Zjr519-eNqA5ReD6n1mn7xTmgooSjB4o4_F5b_IVR3ELlfgovEV0qsl-ZowFAcmkiOzQ37jLk9qK-4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=g7CfOSdTahu3BfOMuPMHYkfGAQjBErVY0iVBksr_BY-ZAXk3GDzS_oLP8WXZS1BmCcDNP3UKQtpU7r6C-Z1gSEmVztRYW9fdJU3YR846dRhbq-LdY7qEs9NeI1cI5qcl2UMtR3rQ6tihzRLir4n8TpOXVVW98ek8fdqZF9WTzDOtd0mq7VJmAZfJJBXkJjz8Xij7vMLOFH-tbPcZOVewTPl2HxRK69ndBUwZm6K6A7Pb5nEXNl-uq8B6RD2s6vQQNRNv0yjPmUz7fqZY8x7FixfwyubnDna7Jvq1iK5AtgfOL0jRKDLlOGr7EZzgzIFsACKiK4XnHzEs-jn-ZO5KvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=g7CfOSdTahu3BfOMuPMHYkfGAQjBErVY0iVBksr_BY-ZAXk3GDzS_oLP8WXZS1BmCcDNP3UKQtpU7r6C-Z1gSEmVztRYW9fdJU3YR846dRhbq-LdY7qEs9NeI1cI5qcl2UMtR3rQ6tihzRLir4n8TpOXVVW98ek8fdqZF9WTzDOtd0mq7VJmAZfJJBXkJjz8Xij7vMLOFH-tbPcZOVewTPl2HxRK69ndBUwZm6K6A7Pb5nEXNl-uq8B6RD2s6vQQNRNv0yjPmUz7fqZY8x7FixfwyubnDna7Jvq1iK5AtgfOL0jRKDLlOGr7EZzgzIFsACKiK4XnHzEs-jn-ZO5KvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=FelJ_OjsEh9DUgOij7RDgfUKpILG72Tx_ZXzfHkvBkQxaMtyxZCC8HdyEkALddvYJnMF3txprg-oazHq0ru-dEKVC62nUwso93qOe1eM9MuCkuf9rw7YdE8Z9U0ayYAZqI1OKKQXkJU5o7avroef40pOQa3kB5yIwicCv8obX4LoIcU12GvBod2Ja3umSbM0BoO734JN6aIYdGl8AhKasbk8GNMu2nvulWxMRI7ZRfKTFS3-4k_91xy4yK-4O8wB99hySajxDzofrKZIPL2DiXfbFZn-IGuu4geiq_rpR0JzWMZdbR12vA8F8jimJJ_VuPfBGaGRIBWk3sayr6weRA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=FelJ_OjsEh9DUgOij7RDgfUKpILG72Tx_ZXzfHkvBkQxaMtyxZCC8HdyEkALddvYJnMF3txprg-oazHq0ru-dEKVC62nUwso93qOe1eM9MuCkuf9rw7YdE8Z9U0ayYAZqI1OKKQXkJU5o7avroef40pOQa3kB5yIwicCv8obX4LoIcU12GvBod2Ja3umSbM0BoO734JN6aIYdGl8AhKasbk8GNMu2nvulWxMRI7ZRfKTFS3-4k_91xy4yK-4O8wB99hySajxDzofrKZIPL2DiXfbFZn-IGuu4geiq_rpR0JzWMZdbR12vA8F8jimJJ_VuPfBGaGRIBWk3sayr6weRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWE5v0sKaIKwerP9K8ZfpAdqZD7apSb1n9x5YumjJ0elZNpP-2Ki__SXA7gmH9031bmsRfcb69Jx7U5FVP8mhZxDl0UnHy4CfaMNrK7m1l9ICbiaXtIdzJA1PSz-ffj5hjisOQKWLXu3Skin0CWxgKjNXSAx8QIL9Tex-bknDYP_7FJDFElB8NQSgUXvTfiW1N9dLvnVW8kQRnoEA7tDWUB8uBS4zLdmTfP5gSvF3PLdd16IjRA4WUnIUvFBrcy29IpbGQiz0Zk_fau1EljactUivfMGgvjXMf3E0rnuIDlNhc_T4_9__4mFMwILz05U86Z_iKT-s5u_H7FEZ4LFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2yPRds9RLII20z_acmvmk8Qv_fdBnnxjSRQN1Q41f565wRpuiXGEQ9a135g2SsXfnwPaJAZVdTby55DgqFsgAbhRw6g0HmWKWgrkcfysu5OMNE_T-6ZXs9gRRe1F1c_t47Y2v_qR1KTqsMxVucmo-ZyO3mDZZo62COGR-4uZG5nEaaZgyZ_GHrKGgqcWrKsobmxe37z7b6uqJXUkGtVJjtRNP7DPNRCa-f7B_bPdX7h-kQGXFWOFT0n8qgvki8K8m1lzn4dEhniZJCVG4w9Pr8PIOERVfQKyo0-cJ5fVBrmYjiSlu3xI8icgLl4Or2VKbveP3ksGnkb8gVOWfgKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgBPq5fgHUPuCKZ-Vy5hN4VEtxnHlbOmB6CAB4XU4KuyTR8z4a4oI9ry4VOtnoL8-1-ZMhJzD4Hnmr4YLLI1BUoU0Y9MwypNEg2GD-9chiYIq9DeIthC-XlryBhdBr3NIVy0s6pDVjKKOvyRAnVqtv5NRGhS3pqgInyUjNiYssfg-WyPenn14eghL1p__x4bveuewqCAnAAwGRocDqntIF4tmQMIyt1wjL9fT_a27r-WfSnSAaXIa3V57EBPHWK4HcgndiQqhmNaCIpPjMgz3OE8osOpyOwU6wMX68O7DXaIa_zg25bPWSPtRZKAwnXsGA8LtLMQ2zxNs0CfC-Ccdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3n0NIpTXQ7_hkAyHnNlqfk2K7yVDCVB1SEteY6YvH4MrF0PxXxexWuVbO-zlp1R_AqmQvcXOM27brVmMkALlOOATGLRM96OkD-Vkej-_HGfWXd6S8prsGV4KEcByj6yesRQDkx_1P87bjrjcGmwExExLIN68xJxBOSfWGYcvasFKbj3Aj2bIm9Qw5Gyv-XFqxjy4lhhdMbKEijBbXwceG-wBdKxtmWhAAlWiUtxZKmjcoM7nISGfO993HjL9LjxvAN6jjdTjX2divhmi_12vN0CnCaBuUaPzbLUzV2vGMTs_PjiAT8qjwt2G6W2V7I_HeIhjO7zLsNADItEV0B-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=eMIHTpj0HHmc3m7ebvQvuTo3909hkEc65jtYsZiPLNjQ146QLYSMpr6YrTM3lUnrLSKE5ksq2pTWjEbtCAk9agJkh8G_bRRzRQk-4ZvN5hiPuNC2QJHVcL75-Ks8t6WxlXRP6jEeYPMAx5-ut-qCOW47FBN7quXgbJVwOq5dxqi7m1z26JreUEo6jwEeV4brEWSwmVAuGcxSohVQC0U0z3GIcikShOwYaqP34mjf_AZA3AtDJg_HRaCne8pleObGKgR8LG5V24rBDaIIpiF0lH1TUes-t-80TcZ1n3sb9c4piv8ve_OMnL_bof24fDCNoB7wE1b36MOLFGcE0MZiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=eMIHTpj0HHmc3m7ebvQvuTo3909hkEc65jtYsZiPLNjQ146QLYSMpr6YrTM3lUnrLSKE5ksq2pTWjEbtCAk9agJkh8G_bRRzRQk-4ZvN5hiPuNC2QJHVcL75-Ks8t6WxlXRP6jEeYPMAx5-ut-qCOW47FBN7quXgbJVwOq5dxqi7m1z26JreUEo6jwEeV4brEWSwmVAuGcxSohVQC0U0z3GIcikShOwYaqP34mjf_AZA3AtDJg_HRaCne8pleObGKgR8LG5V24rBDaIIpiF0lH1TUes-t-80TcZ1n3sb9c4piv8ve_OMnL_bof24fDCNoB7wE1b36MOLFGcE0MZiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK8O3TEp-0Mn-T7pwux_rI7zCJ06XN9ZwVw0UGoRqAnIy4RdYOhCcgtLPhL_m1mVB97xU_bcc-htKNpAQfZS9VUP-3aM_i0dYloCkQFkqaWg6rOnQVVQVs612TGPZdtA-Xw6vfaPVIi1TQUNoTdPDWhpDaBiXgr4XvRrEKf6IwiDf71bsVtzyB70rFrFICLXsOjy5X-WJuat5DUwHSw0klj7pbXJqPZQ4hPUb-Cj02kJRDB3uy_2z8m68odkjAcupX6tToOtZB_3Mcmj9-cfDlox3T4hPVykIP3-SEOZjxu6HTw7KsccboDUVvdr7FcrlJvrc98BTBFC46iG_e-F_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fJPNgIkK3dk3XOEFg-iG-CoLRaFEnS9QOyxXZuv0l_iRz_EddIPPkUiFFR0O90YBGR-5G47HGu18-z1LBmZLh6zKi5qKZ_Co0a3iUut07h4yU-FDk9Xkg4Fo5k8txIKVcf1aTQmC9ZQK6J4BekPwNQIEGgOdYsFJP0pI50njtyvW8E4OR7rg8JtsHyuKe2rthtxLpo3r6dTX5G0Ag9O5kdCY0w74XMKuGWXEOO1s3W0iRdwgmqNqyAGZJ5UEIfR1frYOb-wEUXkwiIZiYbVp1ZJ22AmzNaf2VarGXK-bQVhHzPV3Am9-q6f4-q1R31PS6kseoZbWkn42NbWSgHFl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixz4JdixXYg89D9Y5hoa8K-zPiz2p67zyGwUg3vPLvrMcezyYzeHHhDiWmubakbf_eOye59wZ2qCz6SehcaQ7uFe9xnYtS3XttQIL4ezpM_cwWVjkiDXVP85JPs8LCrf8KdOOO_--DTpJWXXwRlkOsxFrm4KP44Oql16ewVzXvSMEU6ujukCyUwDZrN1phBE9XH504lqugG6vbud9H3r7vjF9SEBiu4-uU0Ikq9m_xBQvxesuWkypijzhYGHUi2rIdbIlGQKDnrrleRtpKlKIIBJhf0Q38VgxMjGv_ZHHe1N3kdsdyH8lpIg07dtZrknYPyRu7Z0e2WxPh8wUO6FrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALTYttz4OVYIzYJM6b3A3DAX2tYhPuI_rfzlKaZunlgMSLOCFqxYT4AR2sA5JczD48iekttzsbI_9tM5p3SOquVDfb5-jXj3RIMsOkwcyj_H0t2o8_7nRdk2vwCwa2ST3CWIy9oLJED7kkz6s1Jg7XFbP-rcy02URwSylnuz1_Zb5yhA7s2sbCQizBZHMfZ0zP8krYCbjTnA-8KT1NBG2oTdQX1qxfHH3miQsnLEsWvrQalRK8MZh9YJx5Z9n33B-iDPrU9B7z3XwjgASolI_dv7r-J0WUXU58pGTxB5uSXGz6uipBHeMNkDit058h4kYjrDid1iHWCRJ619WNxlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD62Pqyrv7iMcfCLFBQkPFsWFbFyw_AupQngKdE9QEYLl48GHbTHJ0vVrLDKXCj6bEEm-1iQylCA5RgNm3ag1TDAsf1gIo4gESicSIm1UyI1aF-uQxjFoiY2VbcNdqsA3k5_sqJokE5lD8fx4e-U6r_WCk2dm7ZdUJ0njb1wb4RNMJ2gZ5zuOjuOJ6-YwEO7oYDezvs8p5ormiBMswQH6FS8Fey50j0U8Iq-dLQ9fnZHSAjRltRi_R_ClEQtsfhtboQz_LIAb2gSyc8J-qI2J_xR8lyhtWumAUut_ZzPhTE7JWlePnZnMaNvLWmdfy2KM7jfzctZaoxLyaMUj41cKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=dFVFs8Zu19uMG7sXjRFaBHIp8NnKYJDJp6Z5xfSmQ0ulU1p8sK2QKdbJCSWCVgBVHGN2szjV4iqeCBVMcbGYIH8ObZgYxkoa5GAHb58d5err3VR2ucv9y5BZqTBZfHB3aNdlafaLTYWC81crHlHhBSGgzNVrFFiAz-M_AGcIgYaq3IuhQV8_c3HReaqornA05KkMfS0khOKVT1TDZSaucEhGJSF39ZaPxMIEB9zwVRAcM_6tEHG5sAGshKQ3OcdhlZeels_uorot47ltxTUgJ0dqe-Jgw0xywE0w8VgTV-GpWEDGwbqE0rUusQwG0CkV8z55cQFbFhpf84TIOr4Y4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=dFVFs8Zu19uMG7sXjRFaBHIp8NnKYJDJp6Z5xfSmQ0ulU1p8sK2QKdbJCSWCVgBVHGN2szjV4iqeCBVMcbGYIH8ObZgYxkoa5GAHb58d5err3VR2ucv9y5BZqTBZfHB3aNdlafaLTYWC81crHlHhBSGgzNVrFFiAz-M_AGcIgYaq3IuhQV8_c3HReaqornA05KkMfS0khOKVT1TDZSaucEhGJSF39ZaPxMIEB9zwVRAcM_6tEHG5sAGshKQ3OcdhlZeels_uorot47ltxTUgJ0dqe-Jgw0xywE0w8VgTV-GpWEDGwbqE0rUusQwG0CkV8z55cQFbFhpf84TIOr4Y4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=mlJOI_sbuEkbxeVceb3oz4dllpC74mA7hPYSbeO3-IqSuABVuJWgEUjvxBHlZOFCrJe_NxAR56wFdeQHqxSivK9NBOTbpnz_y0G-g_iD0KEQbPi-T4yB3wufPJ2jqmh7uHSE3kavLryIg04Besj4ZjbVBHgr-8-rKRLFXLxcGQXI8jFf4TcSdfD50lmrmMyslYTh5IrAj4uPp8Iovp16mOPeljGC5gEesLr1IdzHngCJJ6zLE7l1qneOBchU6eC6CRk9oh1IkJTcT1HH1g4gXAEyExES_AqVaTd6jO9H0ubQVwJ-g0Ctd5aH67oR1_4IKBieMAUBPZAppGPsciIqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=mlJOI_sbuEkbxeVceb3oz4dllpC74mA7hPYSbeO3-IqSuABVuJWgEUjvxBHlZOFCrJe_NxAR56wFdeQHqxSivK9NBOTbpnz_y0G-g_iD0KEQbPi-T4yB3wufPJ2jqmh7uHSE3kavLryIg04Besj4ZjbVBHgr-8-rKRLFXLxcGQXI8jFf4TcSdfD50lmrmMyslYTh5IrAj4uPp8Iovp16mOPeljGC5gEesLr1IdzHngCJJ6zLE7l1qneOBchU6eC6CRk9oh1IkJTcT1HH1g4gXAEyExES_AqVaTd6jO9H0ubQVwJ-g0Ctd5aH67oR1_4IKBieMAUBPZAppGPsciIqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=C4uq-XSZbqeNpQCrYhb4uPa01yvH3vrHEGMwpFWBDzZ2cLYOfv0RrcVJ_pEgYDZ1eYQXOUifRYr1cpbfUptC8DP8Pnm61L9p8nJioAqbzsumKPaTclap65lKXGz6sZga1rn-5yK1i3uV4JVaAMrtBtTHtIhnBrnR-7UHavdvxaAtU9KPA6-ikdu4DtjAaxGMTEdngP5ojDVJbBXf8xPNCCMghiH3RSd0haqjhyFY5yts79YoZn4T9Q5xtNS_rrg0xFdV4opLLmonJiFzv_W34JBRgzcAim3e9_ruI8qB2C4qC_xX8x5xpSx6MVHpbaCY_a5uF-mvQDefquFlcWf4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=C4uq-XSZbqeNpQCrYhb4uPa01yvH3vrHEGMwpFWBDzZ2cLYOfv0RrcVJ_pEgYDZ1eYQXOUifRYr1cpbfUptC8DP8Pnm61L9p8nJioAqbzsumKPaTclap65lKXGz6sZga1rn-5yK1i3uV4JVaAMrtBtTHtIhnBrnR-7UHavdvxaAtU9KPA6-ikdu4DtjAaxGMTEdngP5ojDVJbBXf8xPNCCMghiH3RSd0haqjhyFY5yts79YoZn4T9Q5xtNS_rrg0xFdV4opLLmonJiFzv_W34JBRgzcAim3e9_ruI8qB2C4qC_xX8x5xpSx6MVHpbaCY_a5uF-mvQDefquFlcWf4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=XkZI9G3-A-MHFGM-yx4LuYU2EmpbXKFIfvNZM0vMeZJncPa3p0zKOgOjOja5PZLKgKydvldiwXBI1uIdUgvMJ2-F3JBTd4a9Aou0N1MGxLGQbwfphRllJNUkjzb_2i2PAKyu6bMbQqvBH4VXKG_NvhQmlBrQx2q1SRUEg4s6WyveYUKsPpcg7k16C_yQSPbZ_--8RYpgzfLba32w_1ntA1pMzsyyMQFNkiNpBOh5jHsDRMLptVvVZ0ib9WTVkbeWWCxCaxRztyhEwLsuAJoArhxgKhTQgwuPTXc3KP7eZnihr2L20-fzsQ0Q5qd3Y0QqOUGg49Ap9B80JCoxiU0igoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=XkZI9G3-A-MHFGM-yx4LuYU2EmpbXKFIfvNZM0vMeZJncPa3p0zKOgOjOja5PZLKgKydvldiwXBI1uIdUgvMJ2-F3JBTd4a9Aou0N1MGxLGQbwfphRllJNUkjzb_2i2PAKyu6bMbQqvBH4VXKG_NvhQmlBrQx2q1SRUEg4s6WyveYUKsPpcg7k16C_yQSPbZ_--8RYpgzfLba32w_1ntA1pMzsyyMQFNkiNpBOh5jHsDRMLptVvVZ0ib9WTVkbeWWCxCaxRztyhEwLsuAJoArhxgKhTQgwuPTXc3KP7eZnihr2L20-fzsQ0Q5qd3Y0QqOUGg49Ap9B80JCoxiU0igoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=J1hpR3BnX00f8DVwyUt5sf-NV10C7Sss87QgEqNu-3al21S4xKUeOcSNZMTUc7hK6UDkiyeQLfi7VMZfI9XHt_gFwM7i9-VqrzLzb_V0ec0gkkeET6tCPUJW4mwJgD6nD2ZfzLGndCMvN42zr9LPMPIcyn97KzAireKEUuASwf9Qeqoe-9n3Eool3xepnwwZvmtjT6wuIQFdzC9950Kfchw7pi_3e-ljZKjYdidhd2oSzVtRKIIcFdrlzI1xkt3oQVE2MNzBZaeSQgJWBNpNPFy6E03kZbRjDgyiyR8tN_qDN_PYWhPJ56wnzUYm8SSzuFapwnOnKpqSLYPdt1wXGl0Qw1bzyAKRq_ZO6FZYCnFvO5efNcG8s13VYQYIpG63FeRoxDJNdmntUfMo9adwezJQM8tKG-xlRv1RQGj4ED7mI7zKyuHzx_-Mq6Ku1WVqMAPjNY7QC1wp_wymvd4_2i-HgB_cdlxZ3aOpsuxd5WOW7EsHOuf3Rts2nBGX_aCVEfA1-5ilGJb4Ot5rE5YA8JGOQr4xHNqJFtwvkGI8eivZatT-oFtgI4SVieVS_zOTCS-B8kM-vpt-wMNMF7ZCKgRIrpFHQ29t0XIo-DDM0mhN_oBmqhUCjhVuWiZaFwmTRBHGNgS-GSuQtQ2TmryWwE9cN_C4TgFd3LobdyIrrYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=J1hpR3BnX00f8DVwyUt5sf-NV10C7Sss87QgEqNu-3al21S4xKUeOcSNZMTUc7hK6UDkiyeQLfi7VMZfI9XHt_gFwM7i9-VqrzLzb_V0ec0gkkeET6tCPUJW4mwJgD6nD2ZfzLGndCMvN42zr9LPMPIcyn97KzAireKEUuASwf9Qeqoe-9n3Eool3xepnwwZvmtjT6wuIQFdzC9950Kfchw7pi_3e-ljZKjYdidhd2oSzVtRKIIcFdrlzI1xkt3oQVE2MNzBZaeSQgJWBNpNPFy6E03kZbRjDgyiyR8tN_qDN_PYWhPJ56wnzUYm8SSzuFapwnOnKpqSLYPdt1wXGl0Qw1bzyAKRq_ZO6FZYCnFvO5efNcG8s13VYQYIpG63FeRoxDJNdmntUfMo9adwezJQM8tKG-xlRv1RQGj4ED7mI7zKyuHzx_-Mq6Ku1WVqMAPjNY7QC1wp_wymvd4_2i-HgB_cdlxZ3aOpsuxd5WOW7EsHOuf3Rts2nBGX_aCVEfA1-5ilGJb4Ot5rE5YA8JGOQr4xHNqJFtwvkGI8eivZatT-oFtgI4SVieVS_zOTCS-B8kM-vpt-wMNMF7ZCKgRIrpFHQ29t0XIo-DDM0mhN_oBmqhUCjhVuWiZaFwmTRBHGNgS-GSuQtQ2TmryWwE9cN_C4TgFd3LobdyIrrYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=Sis-a3gaaogKpcTMaX1hL0MeeB--RJ2jTgBUobZghJu7L0iWtdKLym3S5j6btWsb3xVkMsAlAI79nVoVtXTO1IBM24qA1gbsngceIF3zrxTfytJdFhghtjDH1iz4S53BGwP13-Ck_lKO7L8zJe-aQazI-N1fxLYd4ez43QmI6vfd14iRPKpwSdQsQaN_ZFyOJtTFPEZHb9HdxN2dDpQVB_NqhxXopolnR5eu_Q-PjrpN_ch5rxbGvF_26p_pusECOZ-rqdoKNJt1YTAqfEAl6pZVJQIwObtkjCkB0wOvkhG7edKRY99bJdPjd0cMnldLEyw0B5rLUUwydNy2qCsLHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=Sis-a3gaaogKpcTMaX1hL0MeeB--RJ2jTgBUobZghJu7L0iWtdKLym3S5j6btWsb3xVkMsAlAI79nVoVtXTO1IBM24qA1gbsngceIF3zrxTfytJdFhghtjDH1iz4S53BGwP13-Ck_lKO7L8zJe-aQazI-N1fxLYd4ez43QmI6vfd14iRPKpwSdQsQaN_ZFyOJtTFPEZHb9HdxN2dDpQVB_NqhxXopolnR5eu_Q-PjrpN_ch5rxbGvF_26p_pusECOZ-rqdoKNJt1YTAqfEAl6pZVJQIwObtkjCkB0wOvkhG7edKRY99bJdPjd0cMnldLEyw0B5rLUUwydNy2qCsLHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxZ0G57X1-nCuVpD4gImVV-atDnBA5_BZs8mohf_E8hYxVDFmS5GE87nQNOuW6IQA5RCp5mlKLB4m2vyDdxYZvV6qYUE_YoCWY32dgPi90wiOPAFGkxDZwtItfzCmefJ3QfsXN1j3fDTmHTiQ59Qv8zl9chkSsJRE-9nvB3BKjWiOoQ5Ckt0755d74ILXHtnW2YRdA1JIt4J2Hn-ONobNjcuHvgJ62BWIbqJe8MJ52OIC0l74OHaLM1328kzcqA-uYS0-i5ncDrCclFTJN3AxCMQrBkO4joHlOkLYWj6WJnOKUr9fdnY4akQV7_moi0dG8prxRaZ83CM6A2e58o70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vykM5zXDKbk2irsckeseOhvkYGcVftmBNvtN-ZLca-8RLS0AFHNbzjdPs0zgcIA8uUW8otBPPNgDwCRE6DvqnvbHxHnnFO5BOcahqXKXcRAnWpq9kVfFWJbbcYfMkvMVclnEM0YRk1YeSjLZEwa_EaKzSldkafezDm7fI2WWC2ZadWpDVi6DzEZqJEm9QvpxT3YfVQylGaTV9yBQ9Cc6jro0McpiCPPfmpcHSJY0NewOb9gN3Yc5LLXXLSJpiM-tUMe9qhFkNJFDKBda1NjevoIKStfXUBwgElFkue9xMUD2S9Ckz0AwAFxFDatVv7Dqc9KVGT6fjxC1xQ8PKBTLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsbZ3tLfbuRVTgStvn8lAsdzZaw3dFIruZlWAn-EjiKvDuMo0BJJ8o5t5_SmAL0Dwxpsljva5lWrPmgAynxjzLHVhbYjzE2NPLmSNJWLyi1Wcwp5WJQ2WCUj7FE2ghOwCRIPxh0UH4vel952ebXtvq182xiWW29GBy41_z96dvHbDV2r4y9Ptty4rYKpd5Je7Be440T0IJHddYz5YlZOj3UPHh4o94o0upKV3DI467dFMg9qu8uhgdTUrrGpBbdNtnYNfLFYSAFSt9_l3rufqr-Tq3YrAaUtSzr0R83OepjP3sJgUKfoTLq2WXtjdKtr3_q5n4gnh52BlCgN8De9ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7GYbpjy8IZIyvB29oFif0HdAm5GDewrJYUJ83CgMNnrG_6RhD1zfH4AzP_95q3vbnB8Sa61yNRpDNg4OCTKThTnf7sjkKonCO1w2txHcvr_mCXo3gSA3QtKz74cABJCHMlR8SjiGbU4_MvQfL-_-ci3D1f4CL7o32IBTBWceSgcQEF3UbUzKIz5Za0VDjfZLuzrpHXCHPyH-JBFbUQzZr6dMjZXTLaB4RJBniC3AsYhb7NOX1dWuep9yvmPJp4mD8f0aK5UJtQ9CbeYkZSAEESYDaIve5B2MoPcF0ZxxzWIjcXcL6O0w6EKZ-aimnMg6xaGbCCyBme7tKfE348I_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZeL55gI7tP8Fu8_2tn8Oe6BRP7dWzA1-xoavq7a8nVC-jrCwPoJ6o8nrFfreLMFK29Duj9LtKtnwL4Sc8CMHic3_UDsKjKleW3ObD6MGGEqQMVMnAyVpiai8tdlV0kE1pe1QVt6YcHnjWXqRUpX3o3XR9rs1nOh9KNOSrVDOYl25TBflabSRTuN3Djr-Mg0N7jMDSPxlFtlyHIGKsmyliPKqJJENRTFxw6FrT0KcOPDZWieYZIpS6YRVlH0lRfVT_89ElzFQnpiQYW-FfPoGT90n5dWnA9Mg6c-9m9c_Ecakm83TxiLRVBOPgL16pI_4JcnPP9T4zYWYeXyxC-9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=ujB8xyslcmIJSbAT3BQDE4wbB2dSPx1_KdNs_ssfB-NeXyncVlU2s0ktZIioe3OFwUdudd8Xv799SL81Yq0Hn__J4E9ZPI_BZvFO5VGnIwRJOOU9TUOvqunohX116unVukBVrheWPXiux7OaOwQoXBs6NUk-_187L8mD29i7iZjyvKGwCwDSr_vBNtHG0N7o4ovxd-lMyKUlcBKF08PjkMq-apJC1LxmDN18xwbMIntk29mBXt5HqKZj5kHNVvfn_0_XNVgQ4K-jZsAwTMaHkk6E5d-bfBLy9HXHMJgYvBMNNy5oiI8LsIrfgGijDXN5vvpWHCcYDNz38YboiauYKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=ujB8xyslcmIJSbAT3BQDE4wbB2dSPx1_KdNs_ssfB-NeXyncVlU2s0ktZIioe3OFwUdudd8Xv799SL81Yq0Hn__J4E9ZPI_BZvFO5VGnIwRJOOU9TUOvqunohX116unVukBVrheWPXiux7OaOwQoXBs6NUk-_187L8mD29i7iZjyvKGwCwDSr_vBNtHG0N7o4ovxd-lMyKUlcBKF08PjkMq-apJC1LxmDN18xwbMIntk29mBXt5HqKZj5kHNVvfn_0_XNVgQ4K-jZsAwTMaHkk6E5d-bfBLy9HXHMJgYvBMNNy5oiI8LsIrfgGijDXN5vvpWHCcYDNz38YboiauYKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=g6S2sSEPkYkVir45BhFLfp6n0diQhaOsU9Bo_wpCoe98z6RBafToC3Sd0_YNh5sIc3JV-YuusMY8DYH54gsjDsChbkxzvEPmTycOh61gWbD8vLzzQ8CFpD_SKG5jQl1ybhcJ3Sn7hqhjitgSfX4dPKCtKSPR4lwc5vxDWjIz-fmD6KE9HlOrD_Ag6BhcoiWkBKTywi9Amo97U2HUJmlqUUHBEJn3s10muCE8BxlDhmmrq0P6SEdTgRFqIrtIAp7uurwq5TZNv4T_DUoz5g7bvxEojphVMJ5pplyAeoYdDw0vV31pLYnjIJVSLPqNATw7kmgnU3TFwEExPLUe0VCjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=g6S2sSEPkYkVir45BhFLfp6n0diQhaOsU9Bo_wpCoe98z6RBafToC3Sd0_YNh5sIc3JV-YuusMY8DYH54gsjDsChbkxzvEPmTycOh61gWbD8vLzzQ8CFpD_SKG5jQl1ybhcJ3Sn7hqhjitgSfX4dPKCtKSPR4lwc5vxDWjIz-fmD6KE9HlOrD_Ag6BhcoiWkBKTywi9Amo97U2HUJmlqUUHBEJn3s10muCE8BxlDhmmrq0P6SEdTgRFqIrtIAp7uurwq5TZNv4T_DUoz5g7bvxEojphVMJ5pplyAeoYdDw0vV31pLYnjIJVSLPqNATw7kmgnU3TFwEExPLUe0VCjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=QxGFoRDNuVPo2OaWH_mwrr1jf5hW4yx-xBB5Fkren3egRgDetJGg99zj1ttNKY0Af2efa3EMwMEF8JBAwI_ssSsr4W6jhlo4BoUb2WxDNMz4FaVJ4nRRloieahe5WTVe1vW4u9d4eg39NwZobPDKrwyxRSDpM1rR6dLmhUKZihzOs9vyijNxt9y2pJ0txiPV7OxnH_zqdxNb5FN93BhoyI667v5hwp8B39RdoT6r32ClHzwls80dbEQlvoY8231boSC8-LC9XOxXWXolHbj6PFG-W9coSOYRTwsDdqC29QByS_IvSwJO1TL2gpKjh9UdnQQin4En-wIU8yXmBvMvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=QxGFoRDNuVPo2OaWH_mwrr1jf5hW4yx-xBB5Fkren3egRgDetJGg99zj1ttNKY0Af2efa3EMwMEF8JBAwI_ssSsr4W6jhlo4BoUb2WxDNMz4FaVJ4nRRloieahe5WTVe1vW4u9d4eg39NwZobPDKrwyxRSDpM1rR6dLmhUKZihzOs9vyijNxt9y2pJ0txiPV7OxnH_zqdxNb5FN93BhoyI667v5hwp8B39RdoT6r32ClHzwls80dbEQlvoY8231boSC8-LC9XOxXWXolHbj6PFG-W9coSOYRTwsDdqC29QByS_IvSwJO1TL2gpKjh9UdnQQin4En-wIU8yXmBvMvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7RF3I8WmEpaWsh7NS5zUyeNFGV7JgM8PXQVmZVnWQ0OjCGX8bB0krZypgip37V-CGT5ML7Sngq7OQ192WkLAQrChvwE_3rAVn4qJcQOwqlzo5q9e_G20TLTDq_0ZOiQFhtFDcGRpaghL6bkUuaVyCdchf7xypnqIc0nXIurE6jnYZIX1XDAMTJrS8LnYELgzhne7qV5hC9XeDcaZq5vOqdvW6wOIKBtS4xqrWfsbpRsXu5kDWNO1Vvqw4CBVs7qeid_cbi_UZFdmcwcpKtfEGU4Je1-Wfm9sHw7Xl4E95_XOg_q0qxoeiYBdSyQ8crEeSFwYfRY45BMGRJwemcX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=Ob3rlf2Pmbjh3fK3zUVm7qj8wLBcYo95V3cPezKoRgIEl6emDbycjOZALrX7ePlwPzn_VSDa7LpxvmrW9VLJOHCvx7ZOwXK-O3Vebzv8g5Rl7g8h6wlUbeZQ_P6lvxEI0bxG8SPxPzDZj66uEhMPRmMGH7IKyf7GDat3ls9SKmKhOee-iQfJwgLfukVX9VXlkGCAvpglrYPe4rcJNe4RJN_bIoYFool5X2f3MHbkQycGnXK3nAxtmjtqwJaIjXujMJaOiOB5yMvNncKtp1bNsnn0A5ZUyz7pEO-xTvDVfdtGMfZk5CN0tfKxYHM8XLE8-s_1ymAJwpDs4Y_-HjfFiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=Ob3rlf2Pmbjh3fK3zUVm7qj8wLBcYo95V3cPezKoRgIEl6emDbycjOZALrX7ePlwPzn_VSDa7LpxvmrW9VLJOHCvx7ZOwXK-O3Vebzv8g5Rl7g8h6wlUbeZQ_P6lvxEI0bxG8SPxPzDZj66uEhMPRmMGH7IKyf7GDat3ls9SKmKhOee-iQfJwgLfukVX9VXlkGCAvpglrYPe4rcJNe4RJN_bIoYFool5X2f3MHbkQycGnXK3nAxtmjtqwJaIjXujMJaOiOB5yMvNncKtp1bNsnn0A5ZUyz7pEO-xTvDVfdtGMfZk5CN0tfKxYHM8XLE8-s_1ymAJwpDs4Y_-HjfFiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=KxrNoUDu0aTDRE9p3deaHeFFl8P2pb7dnEgYhLwpY36HnlLPNA76_vwd0fqiPibfGvk9lm8V6YyNZsxhTFh8lqg0_gHNWxxIUB9809VdSabus236iVrjvDASZxo4SijxE27r7vvZqzecDKBAfu9aT6MzB1XhYW8ZbxJe5PRdYx_SJ1OVVY_EBigEwrwi1ZceHRVZxHYcipjENuTBYotuaPRBd1eEPuBYgfstxE_AmGEGhLtGtjzMN8lybQsyi6hoMkUaRJ1M_hcbgKWyt0j7ntLCS1LYsIP1ocotTU1Lx39ULTh-3t3zBrJr9UynbppejXJPB_xjeQHDcz2shS5sUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=KxrNoUDu0aTDRE9p3deaHeFFl8P2pb7dnEgYhLwpY36HnlLPNA76_vwd0fqiPibfGvk9lm8V6YyNZsxhTFh8lqg0_gHNWxxIUB9809VdSabus236iVrjvDASZxo4SijxE27r7vvZqzecDKBAfu9aT6MzB1XhYW8ZbxJe5PRdYx_SJ1OVVY_EBigEwrwi1ZceHRVZxHYcipjENuTBYotuaPRBd1eEPuBYgfstxE_AmGEGhLtGtjzMN8lybQsyi6hoMkUaRJ1M_hcbgKWyt0j7ntLCS1LYsIP1ocotTU1Lx39ULTh-3t3zBrJr9UynbppejXJPB_xjeQHDcz2shS5sUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=YJ1-M6eo8SDcYR9d71ThAHuW8VmHLGdeDe8hS6SwRvkH7wnpDjg4uyEeKOvAU_ScRruzrZaIn5FRX81xOxPXbqPE-Au1F10ra5zFwFJ0JpWX0GfWlRd-YN6-IqoSQGWtLmVwSAdOPuMo144DSVmg4wgUBYRGFYmwnn9U5B8cfqukVCIjgn-rNjX_XcWAppPITkH-u_qqbCxymuFI7ljt4DUR3HRTXR4ARvrNiIBfJse3BUrmFNmTK12dHc6kvJq-cwrUCBX82l_EVJXR_io1l2h3N3YWmbvM84LO1u2HhUQSqRYm0DkkmYyxQz_0nBuJl2KFuQvasZ8GOyzKredoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=YJ1-M6eo8SDcYR9d71ThAHuW8VmHLGdeDe8hS6SwRvkH7wnpDjg4uyEeKOvAU_ScRruzrZaIn5FRX81xOxPXbqPE-Au1F10ra5zFwFJ0JpWX0GfWlRd-YN6-IqoSQGWtLmVwSAdOPuMo144DSVmg4wgUBYRGFYmwnn9U5B8cfqukVCIjgn-rNjX_XcWAppPITkH-u_qqbCxymuFI7ljt4DUR3HRTXR4ARvrNiIBfJse3BUrmFNmTK12dHc6kvJq-cwrUCBX82l_EVJXR_io1l2h3N3YWmbvM84LO1u2HhUQSqRYm0DkkmYyxQz_0nBuJl2KFuQvasZ8GOyzKredoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=f2KmKUfPu-RHsA08f3X3PNf5a2GYIeQQEPEwSHRhyjM15rkONMPYlROeeMQg5-sdNqd1K6e072fnMl6i_P5lj_vudzf5WXKicQfjuL-OgTtyO8k28Esfam4qANQw3S5SeXhzVJUoWpY3ddQlZ9pB_sxtzvGztNJ-PAhoY0Xmdf1v-yx33eDnis1CkrCtjH1H4neHfcJalXBim0aYhu6szyGqzQ99jBpLHq3jr1QxMjJ36QuHranKVLr2cQBKKAlLzuEzQ0qV_6wex5hrll9jn2ZGhhUNNHcOqO9XJoOAhGeWyzQbqxzIky7blrwEDDIKpdUUKr5rt7vuHKj4damnkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=f2KmKUfPu-RHsA08f3X3PNf5a2GYIeQQEPEwSHRhyjM15rkONMPYlROeeMQg5-sdNqd1K6e072fnMl6i_P5lj_vudzf5WXKicQfjuL-OgTtyO8k28Esfam4qANQw3S5SeXhzVJUoWpY3ddQlZ9pB_sxtzvGztNJ-PAhoY0Xmdf1v-yx33eDnis1CkrCtjH1H4neHfcJalXBim0aYhu6szyGqzQ99jBpLHq3jr1QxMjJ36QuHranKVLr2cQBKKAlLzuEzQ0qV_6wex5hrll9jn2ZGhhUNNHcOqO9XJoOAhGeWyzQbqxzIky7blrwEDDIKpdUUKr5rt7vuHKj4damnkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=MK5Zfy8Y9jQqHKDhKZI8YaVuuLIsCx3spsa00fGKMj8dFkLWfHTWIYbPH-kIoK683KUjpLc0r7TQMtoKVBcYJS1wxT6cy9CuZQVM5F17gm60k5oPnJjT79h29-2pPEOmybqtfME7vtzj1UMu8PQ_wWbF_v18_3SXGjesRol-Iqv1fFpGU-STlZhA0E1uC-wZ8KSnw2jzg2Im1MtCb4mgxkC1V1c6RpOFQXYpN9gyX3kfeFcwYtTXZlzvhklJCK4467s1xOZsXwPnq_wy3z2vpgtrwqPF2wHP7bKcZqXQCenMo2w2T_p_dhO5-epJrV54XqWNVsjDPsxqERq4EktYIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=MK5Zfy8Y9jQqHKDhKZI8YaVuuLIsCx3spsa00fGKMj8dFkLWfHTWIYbPH-kIoK683KUjpLc0r7TQMtoKVBcYJS1wxT6cy9CuZQVM5F17gm60k5oPnJjT79h29-2pPEOmybqtfME7vtzj1UMu8PQ_wWbF_v18_3SXGjesRol-Iqv1fFpGU-STlZhA0E1uC-wZ8KSnw2jzg2Im1MtCb4mgxkC1V1c6RpOFQXYpN9gyX3kfeFcwYtTXZlzvhklJCK4467s1xOZsXwPnq_wy3z2vpgtrwqPF2wHP7bKcZqXQCenMo2w2T_p_dhO5-epJrV54XqWNVsjDPsxqERq4EktYIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sehl2yjsZz9WG_JoCBDcxzQCz3c2vEW2AGEXA1zzWHoHxRdB8T0TF1O817D3Gtrf237fQE4tkX6o3aGQrfFFoFbP_b6beE1K_Dajb-tQJYuvxcj-9DBeNPezhaduqGKsdy8WA4U1xr_eyZw87dC29T25yZOzYr9l_vseFk5YEIV48JN0r6EtFq1bFIkp0OQwKnQgWQBg4HxLL83QHz8kRAJn6ji-b9xC7KfobbTFmxN1SKttzz1QF5vERHaYsanzS8tJnrwjzTfPZqMr_p1is3OmYZ6RCvHE-q4f5mlnCTk3zi9j10wTsoYD9PicdUf6wRZHFi8pZEt-jKm0mf6vrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkWIAN0dRr4KVesSb_c_zC_bA2F4M-RvHyZjZruGF15WkTTseUMXspH6HCKe-b0m572zaUjlKD9bj9HF8puWjB6TSb07AoUmHbyFN-7kSIKomi8tgUPMjOQ76zPG5IPKELTEZIVGqhC-Hte7WdKJv6JRi-xSpsXna-8UsbC2Dj87lUNOB7CgmoPXvBhPhJUk5bpfi_y7b5Phk5O8QsjgDNuIIv--_Oni1mIXCkSrxI0UhWsK0aroxYVXtfF74p0X9kDPhkxl-fpJ51LgDPqMnYewrp8_mOn04MAGbV5IULq0S-2mPg9wJ-vs9p4tnbmfzF6zCKozViK9jagmjnpbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
