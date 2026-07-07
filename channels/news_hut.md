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
<img src="https://cdn4.telesco.pe/file/gJQfLE1ObTYugu6coPDEtmI4T1wK2lBUZ2fCCR0nfpWzrVIID7RAWMTxZaIVfAUzFXGTjeAi_PVDYTfST4MzvAuA5Y4eA061t7PcWUOAacqYLx1WB-bdpgfN53anaD6stYg-JGLk0wI43ly0Tm7CVlxLHCwo2BHjyjJ3Yaoa4HFM2OZUn2MZnJFvZ2-w4BDUgVlGDWoDxI5UjV3AhUhQMMtv4EjetPDAfPfgGFNNX60yn9Rq9LbNouwRBg_3_1dNJCWAuGJoU7mfDPaUC644Er_YPdxbFkWOcWLNi2RHXwqcyvyVmEgI7RUoKZA-ZgdmB_gPIM8dwGqHaOIPffyCUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 197K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-67418">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FufM9s0BnbhzEk_jQm9Q0Yl9GCV6tV1GCMCTG-VTMkGOfUR5RV8Ej4dF_9TfN9OYUuwvZJ3TxNH6hUZ8WQvriA-ma8hgvJtk25sYC1r9nepws5BkrvjKBKImA7pE7-6Sg-Xo7cUXCfjsskgAj5XFxceJ_X-cgvLJLseEbc0NsMuMfKtMBecyPWtzWae8tsjOavMAoWcnNYaddiII0BSH_hTi1SYb2KEJs_Zyb2Yzi3UrSud-NLwFmviw7bkFyxjj8sNTzWQFgK64r4jwC-m4WQHNNPyPRjqznIgHNg03Vw6K5ah9-mJiTPiHzAkwZCc5JWO7oF0UU_8khlOZ8FkNmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری رویترز به نقل از چهار منبع آگاه گزارش داد نفتکش حامل گاز طبیعی مایع «الرکیات» متعلق به قطر، هنگام عبور از بخش عمانی تنگه هرمز هدف قرار گرفت و آسیب جدی دید.
🔴
به گفته این منابع، این حادثه پس از گزارش‌هایی درباره شلیک موشک از سوی سپاه پاسداران به کشتی‌های تجاری در حال عبور از این آبراه رخ داده است.
🔴
بر اساس این گزارش، پس از اصابت به سمت چپ کشتی، موتورخانه آن دچار آتش‌سوزی شد و دود غلیظ امکان ارزیابی بیشتر خسارت را از خدمه گرفت، اما همه اعضای خدمه سالم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/news_hut/67418" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la-EsNavPi8ioUicveS8bGTT8T1lU6Nt4ggs0j0yiQkyfXQxAsQ2KImlW1iTMmJ-BnFeTccdvqwRmOQdA3jDL5gURBh64aVwhOAw3zs7XAk3XQP8zKfv1rE6b0_xwGsY11-4kUp-oSzWpoYIL_hz9kFMyNro2kl_GvYqpWmPHH1nlxvNEbjPRWlH563nHsQLUbAsYNGwm-yKvBwWJShIsKqcC6XOjkIpX6clhRYFbElvzUi5JZWXPxtAZu1aF0hGhEy5YDMZvw7ug7-dz9nG-4z6LPgC6SK6maz4QpxlDg5yCxom3MmTlK4cMuuM4ZXcBMmff11Xuk4m8S2I_Wi_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c0b1a540.mp4?token=f-LHuAXtuItTRBOF1J36KFVybI0sS6BG_XFRXJI8sQOLA8QNP2mKHlzjg6y--JwkD5g9p8e1u6ViHFia7xQ9z_L1Rm-GY4TB-P7dAK0ZrnSlOGSWe9cjzNdovsde4TTDsKGKlGVGI4p2wiNoSm2ha7_mbDitSKi4ZoEaCuPRMAm2oZXTXnDKsBJ9kBWAMGiFMURY8aY0xigfVtfbbN6t3ogGfeVIh7dsXMfqTN7djetuXUOVV6ovXxPtN0IDiMFNtSDVV8G2fvXEsUNTPinMOp-0BT1JYkyBR_l61v-k8uUOU-M-TxSSdND0Nbg-veYOUH3bAv1v1kMYPZ17Wk7DMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رویترز:
تصاویر ماهواره‌ای نشان می‌دهند که هزاران ایرانی برای مراسم تشییع پیکر علی خامنه‌ای، در پایتخت گرد هم آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/news_hut/67415" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f2d062cc.mp4?token=v_ndpivhsS0hVLt3YBn0H8aQ0sZLrNebi4gbchlpEyMdKBKetgt-dt3q-KX28wfR2ffNDBjOQ7B-gipL_Sq-zM1OTAVuHJ9u0sAhIo02s9J7OzdpZFQYqs0c2Gx-n6L056QG6VOVH2hyHVlLwiCRwC3_6g1uBj-7ge3xXpGHMrlw6RQZU31OMysaQ8txef3Fo50rZcLuGMrpnqBbEASQjTmwJB9UDA4DuGoyXxAOv9pagmFMnpFmDjAnat789YD1yuh41QARo2lks06zRfxZHA361MfdzDA9KrZGDWUm6v9ZSSMp36yLATUgHQtEt45xtwL_734i400TJywHuMknqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جکسون هینکل فعال‌رسانه‌ای آمریکایی رو بردن میدان انقلاب و خودش داره شعار«مرگ‌بر‌آمریکا» میده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67414" target="_blank">📅 12:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/440a1d9ab7.mp4?token=UWcRJN8H0x0swhDwITLP-VWgZmcGBaD-Z6rcT17yq_kNU6Xl4iPPGbV9z-wwvlSrdtrEP0EKI70dRk5Q08Oz38BkTIikde4DauaOJhGKJC9s2E7SQXq6zQb7x_3L8y1EJHSoJiFjhVpyQruAzueKbbypNjmpgQDArBdbIxBLnWzIoh1-1DpkDLhFhaGvRWV_YkJYS1w-Rng04tC8T4rRTd5AKkaSZ_LS9k-t3W_14w1dMXpzHeKNestjQz-2J3HjVLONGC2wyXT-1K1f4uXBWP79CsXnq4oBIQZxTf1ek1ZuEdLzURAFkQBDEdLwmOr95mUCzhcol-deMZxNgrv6pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در حال دادن شعار «مرگ‌برآمریکا» (12بهمن 1404)
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67413" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIA5PEyeosPnqgWlH5qmCrtBek7hBza7JBiTAu4_GyrZwrBXTUaSKOfmJUiBeeHXBW6Mca9trsyQL4uSSHUEsI8bxSU2oEgIT6MVf1ceBJwmiXrds0844OfRqLH9ee67hGmUtsq9vIhJWPWEYHkYOls4ZAHD_u2iAptwaQFuQKSDlqtriyE3CskKEq92-ot68rQfbJnacXD7RUmrlCNntpNr92Wq4zeWrFXTT4VXa7cN6ah0byNsiTzW7WQR_0iYI6QfMVcDMlINUF6BocIm3x8oqhRtYhBoVHht6r1dwmI-gCV1G-Xpa6SgeMl-h21kt9O9jB7EdzCv6X-tiZPKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آکسیوس:
دو مقام آمریکایی به «اکسیوس» گفتند که ارتش ایران دوشنبه‌شب دست‌کم دو موشک به سمت کشتی‌های تجاری در حال عبور از تنگه هرمز شلیک کرده است و دو کشتی مورد اصابت قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67412" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
احتمالاً نباید این را فاش کنم، اما ما دو تا از بهترین نیروهایمان را برای محافظت از قاآنی در مراسم خاکسپاری فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67411" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64666ae825.mp4?token=InoN07M2isUWRtnChPAxmn_FaS2se88-MnBwMqg2x9gSDgxksSuSymrt4SQMkNK4plajGqwkhg3wzS7ku4yNBwO-uqwNgY9Ms4i0yuQ1Rw1nhMDk1Yfn6oKB_Jh7vT6xqQVvzaLShVLCPaqaG2XmAkW3ULZ5bk0vU2w83bTUgjmaDpYhyN5QGU83QiZnUi1PORmFNzE0P11JKoJUtrSC5fHMC8d85fXfczures1k-hRvtrq6ZDjfBAoJUYxDl-bTajCI0Ow_pNiwP4upztD6Jmi9wtpABWT3Rc5Fjg73zMZy61zLlFsR2lMjjqhodB78xEyVuhqlQyT8nvYhZgWUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته میشه این شعارها علیه عباس عراقچی توسط تندرو ها داده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67410" target="_blank">📅 10:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbee8c865f.mp4?token=J1uE3oupNr9E0v4jfY_casFy3B9zoCrjxbV6gSFOmNuCtT8c4kgvlbAWTMrTpTbr4amGYz8H0ih12U4gyEGyQ8gQpv5vhv7CC9pwoiS7688E77IrTgZsWF8MjE0n-PH4rQtftEF7YEOp9bdD-C4dmi6P7C2O0cdv6hn2OHg7HeiFMv5zQsEFg0RmiSgLneEXcMbUbQAz5r2UbI2oliTrwXtsvOyhG4_JBUaOJ0WnRu5mf8SPXJku-4bDUi_iWn3IMEzy3jl_LmP8_rkdZwWXgDcCsHt55bjtEwLzGW5NyUO3oyMlrgwc0A3tQ1fgU6aBYE5kinrDttyJ21aio6-yTiMJaINge3LIK7J5R97eOPcXrxscUc1HlVWYYDFPYDlOqNGxiu_ndic6X4h1b3ycEtN0cie_1XqL-4Ssp4KxUZlX1iDRAlQiTCyvFJ3i9-0R0kzkKG4nj4iAo9xXhLV6YUUbUm8zXesRa2Z384b6swuprWlM8dmdaQ8sqd_mh1O70gS0epLqhSdoSxlroZqFLAVmhA6fyg7B3XvSM0NGUf4EcbyIEu1h-pfKUU1fm7GgpsTZUwhpZZayulbl_ZkuB3kl3O72L0yz76lHkGlittYJNH4pUazo_2RdHXO4rR1mGru19XEVn5CPWN8FY2MS6ifaB8WbnIm3DlpVzkbqE1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش‌چشم، کارشناس مسائل فوق استراتژیک:
باید هزینه بالایی برای خون خواهی امام شهید ایجاد کنیم. کانال ۱۴ اسرائیل می‌گوید رهبرشان را شهید کردیم و هزینه‌اش فقط ۴۰ روز جنگ بود و دوباره می‌توانیم این کار را کنیم. این بار آقا مجتبی توانستند جایگزین پدر شوند، اگر باز رهبر ما را شهید کنند چه کار کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67409" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7142559e9b.mp4?token=qF05nh8tcTnLZwYpjmWt_twS5nYNN5d8Is59v0wffqp7vA9OkadxxSo-5-_dFBhSdX3QFEVo-EV4oVjSivyYB2Hl7Sa03m7sniiQq9rItnZuw51NezcOieTQz2z3vB_O16p2_GqevFL4O1KmbMYJ24IfJrXWWT9Gwz86OsdxCJjaOYUJvHqc6KdBcY5D4Tjocce2fRgRDNz8NNto1HEVhugehwJ1fM3AUU9DtEmkISGUrwgGr8gnGeC2_j0JZBSIHXJxmqFRzp3XdCc4_fBy29jWe0t7rLVxHo52GrTfNLOovtVobPDZIu61jBMDyNH68k0NhTd0QEnbkpL3aH31Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش جالب یک مازندرانی به حضور سعید جلیلی در مراسم تشییع علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67408" target="_blank">📅 09:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcgPScQ9Kw0-gIVNE0tm2LQs_1-3T2ZSsW5JvC3lBLcvPUTnyI8EY-8LJ1Mbtqaq7UuW-yl74brixxvknrqxvdUPSa3-VnsdsBmiiDMDiDZliSOaVPubSkt1ixBfOQnqqcm1GwlaA3BeIveiVZM0uiDoo8DP9hqT75sRoy8ruMLxw6WxDbhazdZTCcNT4WxndWpHwgT2omrsdWaBpu2jqdwDGwydKyNdgEOZuZjeDF14NHQvzALVgpPSMppdKfTwVMiWFeR_7bxP4RBQsLGq5aEq6-WfX5ORbY8YM3G3LDMzWeF9wEDp8pkCqsZc1E4kETav_AXGAB-8mpQZWULBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
مرکز عملیات تجاری دریایی بریتانیا:
یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
بنا بر اعلام UKMTO، این حمله باعث آتش‌سوزی در سمت چپ کشتی (port side) شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67407" target="_blank">📅 09:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67406" target="_blank">📅 03:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67404">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cBtE8Oq7qdCNA_z8-N74SdgSUpYRZaWHJ9U89xZhuS2Qn-J8KLKKiF6sXB387TtRi9no_g-rLioy5yHRlgEWd3jeQPEDL0jgYW5CqF4sgP82OFkTPVRhM826m-KAZmbIRW2ZKoI2Tc-rcsy5CAkGehLi8aMiiRN5vSAg3dmKxwlHLzmcifLHoLIzslUVGMSmwBqV7QFJ-onD_tFvfUtyTl8b9N5ZVp6vaYuVX8dy9h-paasujLfrclUyzCpahmz2EwlHti9zntRha2ATLMACUcm414eiP_iyvwpd4lwNprss1Bwsc7Afh-EOE1kdxYz1_6-dh87x8fllmc75hkcfFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67404" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67403">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmeGBYTX-1t_vob9flAPg1dBIEIxR5Wncg1UU5XfqBgXKr6CE9Y4NpCX88a0aKpIdf_52PO45-w1uPTkw5VxuilUXpwyDy72Tjg_1ZuOYbqE-XRv6M9iwjBekDa3U3exwdCfYyqsjz21yPcV6DkQJQmohrkF51N0_xmhzGyV_KyEBWc7jPX7YxUoOVDw7uQznYlZtyWBUWOWddt16JulzHVVdWLL62B7NU60LVFjNeZnhkrp4tu86KjeX7PccXP-R7fNlOw7AzqaxpO3oKQ6mrlhzKSrBW6MTwQM6SIDU7aZoLdyd40fVbrJ2RXOE8h98Ros2uHiMUtdP8-6OouSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026
| حذف کریستیانو رونالدو و یاران با شکست مقابل اسپانیا در دقایق پایانی
💔
🇵🇹
پرتغال 0-1 اسپانیا
🇪🇸
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67403" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67402">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9EPOMo_EwGK5TWXy-w27uzWFe30iPPNfNcZmXyKj7oWeXNgMaTfH1i2faLYmketlENwqqYYsPzpFfQOrutPzZhxTnWwRnU8zNeDWyZl1Vk7mTbeivjxelxmytsZFjAxZhzLNwXQX0VK9PZ3VX_4F35GuJdCDHcc5ePoJDBeUreNNqM5BWLgPpxiMNMANnZMNy02pxlAic90AgYlMo946Sol-qHfOWcbo98VlDkiv-hMBg9IlRzd7ZG4CO43BhcK4bWIatHeDUq_4FET2l94bDF9aBvZ1c8QqrEtlnNKMX9lQFEMsGrGs-j-txxdIQ5R4QOLOD3LrXdTHWA1f9fH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ادعای کانال 14 اسرائیل:مجتبی خامنه‌ای در مراسم پدرش حاضر بوده.
🔴
حضور مجتبی در مراسم تشییع تأیید شد
🔴
مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
🔴
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از دانش‌آموزانِ حاضر در جمعیت، تلاش کرد از ردیابی بیومتریک بگریزد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67402" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67401">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781360aa4f.mp4?token=gv7vtphSTaY52hmHj5eFLxwd5MwEwdaBvoiq38fxkdmzB4LG5URQpHGo4x5qJH-butoo_MTM30QwyaFNryf55-2H7Ifi6XPxtc5-_WyPtTFIuajXIrNpc1YCxQthYiugBTmNxtrbw7xdeXfjgACJAiZH5BF3lH2Ef5oWIr6qPySaZhS40T-z8jOLBcQMK9qN_TAXSz8cFCp8xtYwBDSUpZCvH8nTJahvAfXnR8jSVaDju3Z6YW1tIxOG-KCZLiD6gdlbrD8xLE1o9ixaWKlxomRUUWFk9Ovm1siHGXdVY8VF80AxqlbEGwQsLeB4huSBplORKDqN_UGBD5YMco8Tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارها برعلیه پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67401" target="_blank">📅 00:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67400">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتلوبیون اسپرت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT0SrnmGJJrvFyDQk04ksgojZ-BWkm1irBlfzd3gzz5vbtOPkpxo8i6ZeZ0dHaQSpxJILhTl4KpEtMdY-ftcpL6c1YtAOslnx_7UEvWKhYokxiXitCmkpPeVRxFSCJ0M8MB3XCRNZBx2KRInKtgDxgifVRBtN193l6abmgSACLxIODzUuaSNqTr9iCrkh7EgHETQzfEe9Ap2-EKTK1j-sfRw3rngsB_syO2JUd-gopaXjMqaVXELLYOnv31xjgT7DVynTNcTjDiaH9gF5-W-GpfvoCaiW85tAdso59mtFP71ELXze7nWFnw21QSN6sJJmPtNnvj2T7TIS-WHMhfQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
اسپانیا یا پرتغال؟ انتخاب با توئه؛ تا از رقیب عقب نیافتادی از تیمت حمایت کن و پلی‌استیشن ببر!
🏆
👇
👇
👇
👇
🔗
همین حالا حمایتت رو از رونالدو یا یامال در لینک زیر اعلام کن و با بازی کردن پلی استیشن برنده شو!
👉
Https://tcup26.com
👉
Https://tcup26.com
📢
این پیام رو برای دوستات بفرست و به این چالش بزرگ دعوتشون کن!
🤩
@telewebionsport</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67400" target="_blank">📅 00:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67399">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e727650.mp4?token=crH_ZBmmMjbHk6ZeCPhCAVAj0P3giHM01Y2jQnF6xWYi8CDvBhFBYBDgR-bOuEUTsg0u2Al9JEkweu58QD-mUsN2xjOB6gHoneZfrMzySJcUYgT-UWWx8YWNsceNBdk-MfHpMum003qDqaxhso9vahPkISSmdEzz99bk736ect0cCpPsSW-uCZjLNlrfOESbkbrVL7KHhz9eG-NJGOup7my2J0ppm9SMI94ry2oe8pYZaUqAkmF1VWvJbUbJXNJPq1EpZ7adXY17ID4mdNneA68JdFGnep0IM_GVJTF9P2JGbAS2mv2cY_FhSK-IR6-elSmy7zHKF4eqbCUi_EvXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
عجیب‌ترین چیزی که امروز میتونید ببینید:
نیسانی که با یک چرخ جلو بدون مشکل داره حرکت می‌کنه و سگی که داره راننده رو قانع می‌کنه تا دست از رفتار‌های کصخلانه خودش برداره
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67399" target="_blank">📅 23:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67398">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad6611348.mp4?token=Jdgotm308lj4ID9_cegzyhOhu0DVrefvROUXOI9edm2mZeN4QRcsTp6CiZKoM5Nt6uVL-hRw6Eu55yfXYgCziBQMWhhcTq8oDHkD30ELYEhpb2UEW5NdfiJqviZq921Hx6zGsfrdbF-4j4wtSzZDLw5wv-staOz3tNR5hKhfDQTsP67Euq-u2Xh94GFp7DbzSBs-vhIRPksAecCzscq8qk_jYyL1X2WXwKw-XsrRnJmmoElYgidR2bClIllCI5uAjAdfphmI7p3DqZX1iVK2m2DuVKNeGhEGh5zjRlTxhStwrKO_0UH5bZgrjUV7q9AXtro0X_RS8_xk2qdcpKIGJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فحاشی وحید خزایی به خامنه ای
رادان کلاهتو بزار بالاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67398" target="_blank">📅 22:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSY-X2EF8UTgN2_qkAK5hkqTY1VT82FDalU-AxPj5CKPQ95ZqDw85BKrx_brpZgfr7s0moL3kzDKI-ZNYcXloSdit3RvOnin_epxTEhWeJUiTPf2rjXk0OTqcTRNunEAQts2ubQHGiz3DKYPG1qQPMzVaJhECCX4NwKCAX17hY4Mh1Dh7bygAnBJjeR-hQ_u09wBz0UdIZW3HLCrQkoZm3-feJxMRodpePw6pBbV2zwzTy5EN7SQ9yc36JWZMhx_e0bOlt0HkJk8PFKIixa7fvoG6y8smoCCVmhyp0qzCk4ANEntk01TgOqK-6IbLeorO8uBChJEIENZSC-fQSz8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkvG6CuaqMHkUuzoApGzAhyZe0ehRo-rJRT4lu59bjh-7IOG5aK2LzRlo0GZp0dWLwFtzEjNR7Oh4DHZ5v2ga8gJeY3GmusHjdbut81O6UfJGUlXOfR6Rb4gkAcHLcMxK06mzh3RjQYbDkrDWZfE_5z5ZQtx9VmZ4TcCRVBwYi9I8lp-BY1CZNO2mVlvtGYETtlh6hsoxebZ5X64D8p0cF74HIR0qSx71qImMQUlvndPbyLl9fkP7ixn2K2LLBKBT7NvShX-UXw1SGUVHtV5eGjy4XKSWqiKNiW_W2pAzJ-l-j-2vXtiGrkmnNP5xtj1fOopbD3Rbhs4lvZ-9LawUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/886967cfe3.mp4?token=HKYqC08KFpd6BiaF__GgTOZ8KbQR-6QVOB-7d11QJZjZVTowNYHFP9TP5jDsiobF_z-3_cT0RgFnlYB64dOaGqrTU2JzcDx1sAE9-iPcJuyBuEDjO653HMstyvji3Yv6VUjeCKVeb-Xphs4n44V4oNeogq6uojSe0QjR1kmsP0RaiJBRh1fKtLgWeGlRXonHdC1HyKpKur-81JgucINBxAIsXZSh5dPUAKmaYn83bpmFj-1TsoEyuFNXGkmiEjg4x8n6cIAyYKMtLw2zkulTUqFoWP_5vCx03KWHFgxAluTJYmtiNK21pBEjravXDTzp4ia9v_sk5bJlxvoGzRHmcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیلم اول تصویر کوچکی از جمعیت یک میلیون و هفتصدهزار حجاج است که امسال برای حج به مکه رفته بودند
مقایسه کنید با:
🔴
فیلم دوم جمعیتی که روز شنبه ۱۳ تیرماه، با وجود واردات عوامل جیره‌خور نظام از ده‌ها کشور در مصلی جمع کرده‌اند
آن هم در تهران با جمعیت ۱۵ میلیون نفری!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67395" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1d208e49.mp4?token=cp1KQvesViQCLMXLLWAcoxleH0MWuYBIhp_3_gmWSUi5r_drGhdcWBjV0Q-qE-xNXwqNqJzC_DJKPhCW3BwAhtXBCFaTB1pygSjJWzOltnM8VnF-jcVERT6YZ1SIcJvv5kbcOOWDZceBlwQW98bocFL2o22hPmD9MmbkhJByS9lS0kIESOa8jqktmOWXjPx-pMMwQ4W4ZiiHVQxHJ3Ey4-K1mOlOPvqJbTXeNJopdOX3zyNBGxIlRlypHCgaVS40wumSJS2L-ykUJG5EGAyZSaG0OjpVnpAu1SMBXtXo2vvEblpL6vPBPMzJpixA324usA-3NFMCzRervjsSR0rcxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره مقامات تهران:
ما بسیار خوب پیش می‌رویم.
می‌شنوم آنها میگویند که«بسیار خوب پیش می‌روند.» آن‌ها اصلاً خوب پیش نمی‌روند.
آن‌ها آن‌قدر شدیداً می‌خواهند که یک توافق انجام دهند. آن‌ها باید توافق درست را انجام دهند.
آن‌ها با بسیاری از چیزهایی که بسیاری از افراد گفتند با آن‌ها توافق نخواهند کرد، توافق کرده‌اند.
ما به یک روش یا روش دیگر پیروز می‌شویم: روش مهربانانه یا روش غیرمهربانانه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67394" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=O09A54PsbRn9cJBEoTVgAeQOz5Q8sEPqJ9e--PTCXGfBE5-RYuer-weWsxN_OYKLKnkGIr2SPALo9zhg85i2n099p5_Gq1akapBuZjRhQNSKjVPSTCNUFSMbEdEzlWErexu9GIIkKt36soTK-U9j0Bup4kwq8JpGuOaTTnDfCs9yCppEspGW7L4fnBh_ngBVCZk8Q60fOS-Ei_oJ3MYnD_O6mI_ASzDLqiWQnX3U3PonwCOeUACKGzgucsrAHcOwInIKUNpRS87rQTEyNfLmmrRyMNdKL_adrtB9yBierCBgH_RiUZOGlalukZWUQzRwGmasLk085l20kO9Oh6DOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e3a38b86.mp4?token=O09A54PsbRn9cJBEoTVgAeQOz5Q8sEPqJ9e--PTCXGfBE5-RYuer-weWsxN_OYKLKnkGIr2SPALo9zhg85i2n099p5_Gq1akapBuZjRhQNSKjVPSTCNUFSMbEdEzlWErexu9GIIkKt36soTK-U9j0Bup4kwq8JpGuOaTTnDfCs9yCppEspGW7L4fnBh_ngBVCZk8Q60fOS-Ei_oJ3MYnD_O6mI_ASzDLqiWQnX3U3PonwCOeUACKGzgucsrAHcOwInIKUNpRS87rQTEyNfLmmrRyMNdKL_adrtB9yBierCBgH_RiUZOGlalukZWUQzRwGmasLk085l20kO9Oh6DOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح عقل عرزشی رو ببین
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67393" target="_blank">📅 20:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67390">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-bMcSBMCmy81PLmAaYXxTsLndV4XzIfJKGyQOBhpsMPl1j5yu_U6BRDceFZaEa4lhfRvY32Z_RspzY1ZmYOVEDmoct8mDSBEQqf6VTdTWGFX5VBZWOkYfabIfeUjJJqkm8fPgbtj-XeEA_dQafqjrzXmXmdTfk70p8Wg9JCRiceYz5B4pUNGVHDj12-Q4AeWb4XT8D6JM5IF154pFxKn5BVGctNxRe6gw0Va5QyWFE_LzAkfSv_in-_P-VHa2GpQ4Bh6F2UnbcCDUf2MqLyXtUl5KDq4iLRwFICv5qw13ccEj9irVe5cO2wPjiRCTryiAW7OdX2V9JMsVpYMQwJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZHw3fQrgpIrIOfoVvCWmVX21zKPNYx_4EEMRbB7as_k8MGRqwosB8niFK054xHCKBDKaVYgAXKtqhyRkeHalDGTn474StyU1_FxghPBrgH_Z3-HLLFGU42TPI6suCsVQ6CSQae0lIrcgEztzHFrFbD_zKyt9h8TH5HYtbsYSJ5g0ouMg_rFQ0MnIEcvuy5RoaMxpXB06U5QHxdMiS6uCIcjYsQfoKTI3EiZcKcEBPDiJfkesPXQ7LKZ3afrDkk9AUiZanSrNmsba-Yz4E3fwjk758XMoqNNEb-76gUJZXk-n5di5kW8YfHPyZAn-HgZPokUeIbYHayOQRn-xj80Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=doNcP5Pv2HjvBtCXeos6OtDdjrsMexf6BEXQhl2Req8jcekmJMAsuo0F9tSWQW_rvOdOR6Cc7Kd_psCg6UbPphl_4FOl2MxlzPht3lJnckZ-dxU6o1TKET2wFR43Lh0hx9SYg9J1HZF_b6I_D7VkaCgfqErAADmgTSShgbTwRgspWpfA7lQ-lVJkyy24nPO37HYZrqtWCh7aRxxt6YToXREa-pjgFZ5A9a8NEkTElgo3KbT6jkl8gok4YzjE-BB9RLFpXA9Aki53_4wU2kTfZsdLo7pNfs6xpIPnwgAK8kIgzl2zvQdn5l1PFgikbwCr2IwKgiVyzprXzpDm6rIbhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bea0c04d9.mp4?token=doNcP5Pv2HjvBtCXeos6OtDdjrsMexf6BEXQhl2Req8jcekmJMAsuo0F9tSWQW_rvOdOR6Cc7Kd_psCg6UbPphl_4FOl2MxlzPht3lJnckZ-dxU6o1TKET2wFR43Lh0hx9SYg9J1HZF_b6I_D7VkaCgfqErAADmgTSShgbTwRgspWpfA7lQ-lVJkyy24nPO37HYZrqtWCh7aRxxt6YToXREa-pjgFZ5A9a8NEkTElgo3KbT6jkl8gok4YzjE-BB9RLFpXA9Aki53_4wU2kTfZsdLo7pNfs6xpIPnwgAK8kIgzl2zvQdn5l1PFgikbwCr2IwKgiVyzprXzpDm6rIbhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
پهپادهای اوکراینی اوایل امروز به پالایشگاه نفت اومسک، بزرگترین پالایشگاه روسیه، حمله کردند.
این پالایشگاه در فاصله ۲۷۰۰ کیلومتری از خاک اوکراین واقع شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67390" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=WIK_ZHl8BpNXue9tc5pJbfuraHL72Bvo6aAv8ua7JdZAFrF22IY7nuuMcXH8TGhh4Xh0WFtLQCxWLxXhxFU578khXciDcqgtB5_DORJsPFtmXyLifx5DYbNy0hX50upa1vvMR-e8330yJ8uHoWXkgenD5MUR1VHtnYL0eltEmyCTG3uWQOvWDwTscIH247ARoT8ph-Y58SqPXmv6XfgW7nW3kI8_5J95WYvbvnsmcoudwaS_kpJmtTti0KjElclUaQmCHONd6plgF_Ip4Ea9fwsjGU021IEPKxtleg7ZT8gZZkI7L3DXvjYvJbvAEjlt7LwPJcayn-6rEzi3pmQZ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee21b0d93c.mp4?token=WIK_ZHl8BpNXue9tc5pJbfuraHL72Bvo6aAv8ua7JdZAFrF22IY7nuuMcXH8TGhh4Xh0WFtLQCxWLxXhxFU578khXciDcqgtB5_DORJsPFtmXyLifx5DYbNy0hX50upa1vvMR-e8330yJ8uHoWXkgenD5MUR1VHtnYL0eltEmyCTG3uWQOvWDwTscIH247ARoT8ph-Y58SqPXmv6XfgW7nW3kI8_5J95WYvbvnsmcoudwaS_kpJmtTti0KjElclUaQmCHONd6plgF_Ip4Ea9fwsjGU021IEPKxtleg7ZT8gZZkI7L3DXvjYvJbvAEjlt7LwPJcayn-6rEzi3pmQZ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد جنگ پهپادی:
چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند. شگفت‌انگیز است. شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد. و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67389" target="_blank">📅 18:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=PGzmQ6209DNs5KpYKw1DBKOiva6TMR43pib7pvDVcYVL6wo1toc-pfWJQslI91ncTxV4E6DqYlj2HKelBxuDjfLxME_rV5DdyIO_PAE3Voc4F2NaeGduW6Pl0IR568wBGKqPjFAwRDlLxDg05LWkS2IQEx3YaWRVRE0Pjt3a5iHI1iMbAXpvmAU7tjboyKNzsj0tGe4IHK1W2FiLdsIhHQqvgpIahtAKSpY2uvT7lc0i1RM79KEaUPnoMtCrGIRGHIbCBI2-Syxlgihgfa7sHFK0LuJYHZ80DqtA4JuMQazejrVgWN2TJjxdfvSPBHXE-cJQgbeZBCE-uNfNGZr7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a06527a7.mp4?token=PGzmQ6209DNs5KpYKw1DBKOiva6TMR43pib7pvDVcYVL6wo1toc-pfWJQslI91ncTxV4E6DqYlj2HKelBxuDjfLxME_rV5DdyIO_PAE3Voc4F2NaeGduW6Pl0IR568wBGKqPjFAwRDlLxDg05LWkS2IQEx3YaWRVRE0Pjt3a5iHI1iMbAXpvmAU7tjboyKNzsj0tGe4IHK1W2FiLdsIhHQqvgpIahtAKSpY2uvT7lc0i1RM79KEaUPnoMtCrGIRGHIbCBI2-Syxlgihgfa7sHFK0LuJYHZ80DqtA4JuMQazejrVgWN2TJjxdfvSPBHXE-cJQgbeZBCE-uNfNGZr7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره کارت قرمز بالوگان:
من درخواست بازبینی کردم چون فکر نمی‌کردم این یک خطا باشد.
این یک نفر نبود که به صورت کسی مشت بزند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67388" target="_blank">📅 18:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=lHUtfLcNqWZOYlFIZI6YJMs6hnZgPPPnrPeo-NprBUB4McmrTuENLkc2JyecnV4rp9BvD35s-0qYLtIpS6Fj3ehR1kFpcILjSbYMlPftevp-sPQWeYSRMFUR8w6P2eDS7P2G1pzKpfoypDGjz8qxCRYgqlVtWwtB-fWkF-uGj4Df9C0aZkdODbvM2OZmVQGkXRoVGAzk4-IJSvtewBQjZSCWjR5q6P3CbeveXo1XpIAlwDzt1kDT9i1OlHyhx7DpiK96MEb8iqyqWZTM70vRuQOQi9TjqL-kIFg7abKP5diIiSPyB0Eg9WWnLW-XmzuBtoRAaKgw3GfEr58pj9QU8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1e1775aa.mp4?token=lHUtfLcNqWZOYlFIZI6YJMs6hnZgPPPnrPeo-NprBUB4McmrTuENLkc2JyecnV4rp9BvD35s-0qYLtIpS6Fj3ehR1kFpcILjSbYMlPftevp-sPQWeYSRMFUR8w6P2eDS7P2G1pzKpfoypDGjz8qxCRYgqlVtWwtB-fWkF-uGj4Df9C0aZkdODbvM2OZmVQGkXRoVGAzk4-IJSvtewBQjZSCWjR5q6P3CbeveXo1XpIAlwDzt1kDT9i1OlHyhx7DpiK96MEb8iqyqWZTM70vRuQOQi9TjqL-kIFg7abKP5diIiSPyB0Eg9WWnLW-XmzuBtoRAaKgw3GfEr58pj9QU8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره بالوگان بازیکن تیم فوتبال آمریکا:
بالوگان بهترین بازیکن ماست. او کارت قرمز گرفت. من نمی‌دانستم این چه معنایی دارد، اما بعد شنیدم که به این معنی است که شما نمی‌توانید در بازی بعدی بازی کنید. این بسیار ناعادلانه است. چگونه او را برای بازی‌ای که هنوز بازی نشده است جریمه می‌کنید؟ من درخواست بازبینی توسط فیفا را دادم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67387" target="_blank">📅 18:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=f9wE3Y7J_qlVWQD6bkocV8lp8ygq6tRGu6UxE7Z63i4qADvOG9Gkna_Lx6DlMRk9mmbJK3bF6C8wSsaqzmMssO0dMf4toPI2_Le2q-MGPXti2YBTpKGrjCZvXW_U8QrzFquFYAjjLypf1EBrDMuU0qJx8TvpNT4hmlubbo2d9aOyYpSnP5864vmQJh3nsBLNdRabR4tcaAOJbaWeJvPgzzHpUbpkTvOaevDXbCjobTFOkvuphFI88vRiPsEiqeNQ4EWzSKbs-4XE0Yo1US0fhJ9VF25xbYbSedT4rpP7jRU-4E0sr2ibfmoayJ_e99bLvDnpJEIn9IT42TGepJI3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af665dba5e.mp4?token=f9wE3Y7J_qlVWQD6bkocV8lp8ygq6tRGu6UxE7Z63i4qADvOG9Gkna_Lx6DlMRk9mmbJK3bF6C8wSsaqzmMssO0dMf4toPI2_Le2q-MGPXti2YBTpKGrjCZvXW_U8QrzFquFYAjjLypf1EBrDMuU0qJx8TvpNT4hmlubbo2d9aOyYpSnP5864vmQJh3nsBLNdRabR4tcaAOJbaWeJvPgzzHpUbpkTvOaevDXbCjobTFOkvuphFI88vRiPsEiqeNQ4EWzSKbs-4XE0Yo1US0fhJ9VF25xbYbSedT4rpP7jRU-4E0sr2ibfmoayJ_e99bLvDnpJEIn9IT42TGepJI3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
یا قرار است توافق کنیم، یا قرار است کار را تمام کنیم، باشه؟ و تمام کردن کار سخت نخواهد بود. ترجیح می‌دهم توافق کنم چون نمی‌خواهم به ۹۱ میلیون نفر آسیب بزنم. می‌توانیم پل‌هایشان را در یک ساعت خراب کنیم. می‌توانیم تأمین انرژی آن‌ها را قطع کنیم، تمام آن کارخانه‌های بزرگ که ساخته‌اند، بزرگ، زیبا و مدرن. آن‌ها اکنون هیچ پولی ندارند. ما به آن‌ها پولی نداده‌ایم. می‌توانیم کارخانه‌های تولید برق آن‌ها را، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر کارخانه‌ای از بین خواهد رفت و آن‌ها این را می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67386" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f387513a36.mp4?token=tUC-9PMelA2KMSdicpiqQtiPWuFSe0Q_vIynjiOkM_AsnhHyNVsFJjDyiGDN3ZD92gzdV2Q1h_sgdCHLaCwNnR9nFtgNLYavI_OEYYohBkzRabKjrlg2DePi-BlApkYCUEQw2ICiNX5jGw8NSNRA3OQFqqlZBvRW4Soj9jzZCFqlJ7t4ugTYW3RtnC8S-_9aLjD1_Y7v8La9MXXZbgSiZ8ZTuwgcdznV_0JX_0Zuh-KQvDpKnGjBqdV7CdbQiY7TC51AfjI8FKdkH9xYCKsPXWv7ZMUrlEd1JyWC2WKJhUPq8drhSsNOyCwQqAUFwnjXGSsZCrtF1cC-yp3kG-UtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f387513a36.mp4?token=tUC-9PMelA2KMSdicpiqQtiPWuFSe0Q_vIynjiOkM_AsnhHyNVsFJjDyiGDN3ZD92gzdV2Q1h_sgdCHLaCwNnR9nFtgNLYavI_OEYYohBkzRabKjrlg2DePi-BlApkYCUEQw2ICiNX5jGw8NSNRA3OQFqqlZBvRW4Soj9jzZCFqlJ7t4ugTYW3RtnC8S-_9aLjD1_Y7v8La9MXXZbgSiZ8ZTuwgcdznV_0JX_0Zuh-KQvDpKnGjBqdV7CdbQiY7TC51AfjI8FKdkH9xYCKsPXWv7ZMUrlEd1JyWC2WKJhUPq8drhSsNOyCwQqAUFwnjXGSsZCrtF1cC-yp3kG-UtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
تنگه هرمزِ معروف؛ هیچ‌کس تا حالا اسمش را نشنیده بود، اما عجب ماشین پول‌سازی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67385" target="_blank">📅 18:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67384">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=fbCJ0kEqVpnQ3k7Hv5kUo1r_H3khBOEyF7R7xJ8wwkj3Inc053c-3BeKm3VujCXLLCF76-LpTJCyJGDZwoADloPZ-jMRl22e_FRx8Wo4jEouGCbe6xCGmA0uGq310-oPyj-ZGZ4kgeojIazklWORQx9Chg1XapWZvcMXj8xuhlX0iQKb0InaccfBdFH9tImU0czQoZqITPXv7hCURScSWi-FqGE2WLkGB0mQtmTfMCraPZy488jaJCMd_G-Km3kSl8407lHn5gKufCfd5Cv_EZiprEmWkBH3STGds5ULgEs5eyYG_IBR_2etC3HyNuyYrGDIVeeKGp_ikkH6KtyrvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b6983cd6.mp4?token=fbCJ0kEqVpnQ3k7Hv5kUo1r_H3khBOEyF7R7xJ8wwkj3Inc053c-3BeKm3VujCXLLCF76-LpTJCyJGDZwoADloPZ-jMRl22e_FRx8Wo4jEouGCbe6xCGmA0uGq310-oPyj-ZGZ4kgeojIazklWORQx9Chg1XapWZvcMXj8xuhlX0iQKb0InaccfBdFH9tImU0czQoZqITPXv7hCURScSWi-FqGE2WLkGB0mQtmTfMCraPZy488jaJCMd_G-Km3kSl8407lHn5gKufCfd5Cv_EZiprEmWkBH3STGds5ULgEs5eyYG_IBR_2etC3HyNuyYrGDIVeeKGp_ikkH6KtyrvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
به یک دلیل وارد شدم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
من به دنبال تغییر رژیم نیستم، اگرچه این تغییر رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67384" target="_blank">📅 18:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67383">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=SevPJujYCZRZSQIEXS5EKb3XItXunoHHp5Y5JVnBwKBF_IJTPB_aQG11mho1o4RtKCS6Dz_lQ5SxWJjNfwYGVaKDfTT0l_xK6aIrhwCjU3pVlwZRS0U8k5wxWTNb76Cr2WDOLb-M_lm9Hkwkp71aVKSals4PgSjzV9eh4gAWeGYuVvqfvoQS3enD1lNFZ17wfRRTTQBFEk6PbC96GowljxJogPnCRnmnTAu54noJJ7iuNXa3o_DrDMJPiR8UR8rFv5D74Nh4k69E5eo890iD182c-ZPvYSMWqw3WEsm3tRCH1fDViOdtDu5sjrDMIv56QW6pdwY-Un5iX_A7taTvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d6c7e39a.mp4?token=SevPJujYCZRZSQIEXS5EKb3XItXunoHHp5Y5JVnBwKBF_IJTPB_aQG11mho1o4RtKCS6Dz_lQ5SxWJjNfwYGVaKDfTT0l_xK6aIrhwCjU3pVlwZRS0U8k5wxWTNb76Cr2WDOLb-M_lm9Hkwkp71aVKSals4PgSjzV9eh4gAWeGYuVvqfvoQS3enD1lNFZ17wfRRTTQBFEk6PbC96GowljxJogPnCRnmnTAu54noJJ7iuNXa3o_DrDMJPiR8UR8rFv5D74Nh4k69E5eo890iD182c-ZPvYSMWqw3WEsm3tRCH1fDViOdtDu5sjrDMIv56QW6pdwY-Un5iX_A7taTvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
مقایسه اجرای سحر امامی، مجری تلویزیون جمهوری اسلامی، بعد از مرگ علی خامنه‌ای (10 تیر 1405)
و اجرای ری چون‌هی، مجری تلویزیون کره شمالی، بعد از مرگ کیم جونگ ایل (28 آذر1390)
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67383" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67382">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237168e66.mp4?token=glcPmHuR05DECDh5ytdPZdj1OSC8iKwKNqMicfP1gBkSRusMhTgwpgidzo5PFsJ5i-rBRgi_sDXI_znorrUvG13sMomEnf7Zmu6fvnIDOq4ss6jOLXG1mq7-vfmHsT6MJddFEhdDto2o-35oEG6oQPHWhHWf_amZFqmpg3rsVyZjRpVWgV8fJ-ZXSecBbPGP0Yd9UQSH8RWX_QoNp4KWGZVqhH9IoNSfFDtcSRabGFInAydFXJlfGZCLhXCN76uIchges8JWVyij07X3pdzEqan-VHvK6Racd9l9ML71GR4q28L79CvOhclR_oyKIswE7OjoQxfL78tCQYanCapM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237168e66.mp4?token=glcPmHuR05DECDh5ytdPZdj1OSC8iKwKNqMicfP1gBkSRusMhTgwpgidzo5PFsJ5i-rBRgi_sDXI_znorrUvG13sMomEnf7Zmu6fvnIDOq4ss6jOLXG1mq7-vfmHsT6MJddFEhdDto2o-35oEG6oQPHWhHWf_amZFqmpg3rsVyZjRpVWgV8fJ-ZXSecBbPGP0Yd9UQSH8RWX_QoNp4KWGZVqhH9IoNSfFDtcSRabGFInAydFXJlfGZCLhXCN76uIchges8JWVyij07X3pdzEqan-VHvK6Racd9l9ML71GR4q28L79CvOhclR_oyKIswE7OjoQxfL78tCQYanCapM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
مارکو روبیو: سوسیال دموکراسی همان کمونیسم با ظاهری آراسته است.
مارکو روبیو، وزیر خارجه آمریکا، با انتقاد از سوسیالیسم و کمونیسم گفت تنها کسانی که کمونیسم را از نزدیک تجربه کرده‌اند، درک می‌کنند که سوسیال دموکراسی در واقع همان کمونیسم با ظاهری آراسته است و پشت این ظاهر، همان ایدئولوژی خطرناک و ویرانگر کمونیسم قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67382" target="_blank">📅 17:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=SIk9ZVrefL1TzbszhqmbNllrhkoldttape1NJG5cGaLNzoAm8BMeDoKJNqi4gVufWdHyzRIiNfHFSSpIPWkRBVcn2CbrnVQRi8Bd3La0mvK0iAc_T8XM_zGdQvZ0szsq0K16ZPuKBdkThEz2JbNtVR-9BvtDjN0RAb0jZ2Gur3EbUKLfVhzkGag5LAD5ZfQm5RL1Ytdgfnz1qcBIDBiB_Kzcn5WJDhY1HtRaaAtwIf3YSJNwDblZ_cl6Oxq4J_q9kPfgiN3eIeXh_VQ93lAvf0KmUJrQCRKZ1vxIcyeD43pHXVybcO8A9TJPPCVktotAwIMUR6FYds_LxVTTzKpskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54408a1a4b.mp4?token=SIk9ZVrefL1TzbszhqmbNllrhkoldttape1NJG5cGaLNzoAm8BMeDoKJNqi4gVufWdHyzRIiNfHFSSpIPWkRBVcn2CbrnVQRi8Bd3La0mvK0iAc_T8XM_zGdQvZ0szsq0K16ZPuKBdkThEz2JbNtVR-9BvtDjN0RAb0jZ2Gur3EbUKLfVhzkGag5LAD5ZfQm5RL1Ytdgfnz1qcBIDBiB_Kzcn5WJDhY1HtRaaAtwIf3YSJNwDblZ_cl6Oxq4J_q9kPfgiN3eIeXh_VQ93lAvf0KmUJrQCRKZ1vxIcyeD43pHXVybcO8A9TJPPCVktotAwIMUR6FYds_LxVTTzKpskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در برنامه ای در صداوسیما حدود بیست دقیقه کارشناس برنامه اسامی سران و مقامات جمهوری اسلامی که توسط آمریکا و اسرائیل ترور شدن رو خوند
بعدش مجری به کارشناس گیر داد که الان بیست دقیقه وقت برنامه رو گرفتی که اینها رو لیست کنید و در ادامه میگه به جای اینکه به مسولان و مردم دلگرمی بدی داری دلشون رو خالی می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67381" target="_blank">📅 16:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=qsmaavs76elzC6IyH3BNsfyWVNZyLlWxsBLFcAT9Z796RHsrl1HKHQS04vig41k3Eg6_PfnXQ_A3eEkB3wbU4uTG4Rk1uOc2WXILkHIelW8echSqyThNhiuJkdvy0kOxUeqFX1HLX4tQRIkJu3UAU_ypXQPBj_-ZxVMvuC3WmkPoGLZhJ8WS5ePCzJXYSsu3MqzrKdMcFtu6Mkg3JDQT1GhegCwHy5JN570dPinY6Fpx0O5mH294A2uFXkNDp7TBrXxu_0MguWU45H7OSet1y1JvJix9uHAx0Ar7d7ZOGo5rDJYLpBFFeWz8QCixqORKlBsfB3APvbOn2qdLsijaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84629e4c7d.mp4?token=qsmaavs76elzC6IyH3BNsfyWVNZyLlWxsBLFcAT9Z796RHsrl1HKHQS04vig41k3Eg6_PfnXQ_A3eEkB3wbU4uTG4Rk1uOc2WXILkHIelW8echSqyThNhiuJkdvy0kOxUeqFX1HLX4tQRIkJu3UAU_ypXQPBj_-ZxVMvuC3WmkPoGLZhJ8WS5ePCzJXYSsu3MqzrKdMcFtu6Mkg3JDQT1GhegCwHy5JN570dPinY6Fpx0O5mH294A2uFXkNDp7TBrXxu_0MguWU45H7OSet1y1JvJix9uHAx0Ar7d7ZOGo5rDJYLpBFFeWz8QCixqORKlBsfB3APvbOn2qdLsijaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو در گفتگو با فاکس نیوز:
ایران کشوری با حدود ۹۰ میلیون نفر جمعیت است و حدود ۸۰ درصد مردم آن از این رژیم متنفرند. اقلیتی که شعار «مرگ بر ترامپ» و البته «مرگ بر من» سر می‌دهند نماینده مردم ایران نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67380" target="_blank">📅 16:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67379">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=gNbtHqztIeRsGETisdQoNLyc45Cd0OshjmCepZ-bSXdO75u1FWqSbb5Ya078QRB6ii3hjOtTeykaSULoevtRe3n9GbsUhJ8lcLLz5q6n4N5KluwIVkQMmEuB3QfB4ulnBMP_poc27F8S8AA8rcv11ebhREol1OqGEgcT7Kfhp9cRHhxdlvyKEyjOdDSfCka-HWGTcPV3u1yrfQyUmawZupcnTZIcqGFMsLUoDgfKgTIt1BkgxAVeJ5tq8jcZym9gt_lSIt5MxpBg746_33_JD7EsEcfQa3rlawnIydAqePjXGkLV1KRQzKfuOwCkX39eyEWtsxMBk_rCb8V_n0mFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336146a8b7.mp4?token=gNbtHqztIeRsGETisdQoNLyc45Cd0OshjmCepZ-bSXdO75u1FWqSbb5Ya078QRB6ii3hjOtTeykaSULoevtRe3n9GbsUhJ8lcLLz5q6n4N5KluwIVkQMmEuB3QfB4ulnBMP_poc27F8S8AA8rcv11ebhREol1OqGEgcT7Kfhp9cRHhxdlvyKEyjOdDSfCka-HWGTcPV3u1yrfQyUmawZupcnTZIcqGFMsLUoDgfKgTIt1BkgxAVeJ5tq8jcZym9gt_lSIt5MxpBg746_33_JD7EsEcfQa3rlawnIydAqePjXGkLV1KRQzKfuOwCkX39eyEWtsxMBk_rCb8V_n0mFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری:چرا آن دولت هنوز در ایران پابرجاست؟
🔴
نتانیاهو: زیرا چند صد هزار مزدور دارد که در روشنایی روز می‌کشند و قتل‌عام می‌کنند و در شب مردم خودشان را می‌کشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67379" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlhTZwcJBSW4kzWr0yCqmSZ-vvj4tS--sFgeAtQOfhMRUNcVORdxcnv19pqary5Xr3ORATtdwntaVrP6spjL5b-OqFYi-lOAqGbGs7XBGmem211EjVCc7tPgc5YN2IPV2plQjlUX5vGYfB5VrN1UW5aUJquATSH7IR3jkJf0qrqCdKcOIN_6V-H3SizqSPaua-9DtFnxekluHYogUfKiETz0n4R67nfUewyR0rX6_qZTtuVuxjIWeKgPXGkyxtkUTwB75q7vSuRjri4SHYE-Db820mZS1pDEctsxdFV-1maopXfvCwInoc5o8Ty_5sFLVZu5Nkpk_CIu2phAOVvCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واسه کشتن نتانیاهو وترامپ 100 قطعه زمین 2000 متری جایزه گذاشتن،آیدی رو هم زدن اون پایین و گفتن انجام دادید پیام بدید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67378" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz_Wulh_7SAqI1HukXrFWhl72T7cW7fbhFhPeahJbVeGbbI6NN9_hafwxtvykVBpx87R9cgtbbK-9o0HagAyfrIa2VWxj1-k6xDO9Z6I5akeAhCUPdeB2cDaTsM-p6ZMlrlBVLCoaAViHvBrAwYoQCiJAMb9bxbJHwP5nioDspIPQM5L6nDsAvrwIWzezWP-2TXQnmIjrgvenzj6ZpkZhxqRXZHPhFQk5tZ-AD3CCRZqpYIM7BTlfS_0Wc35UkfLDcBGahG6vdOMYiWs1djdm0FLL3t9j7MQrYzGl3X2dATQN5yo-hYHu0_I4rSlQ1lDGm9K74Z7LeYqrC32BjkBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67377" target="_blank">📅 14:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouoZ3lEQEgpSgSAmE3eV_Vjiv0NnX4A_oVxWVPdny1itJvalQMclJVE8CNNlPp6CGmBIGSo64bqF69iOEkYm0uK0N4i4y4apR-mNPGnTqrmGNgTd5YlHLpHl45IenOLrGYl7ax8JjD-W39s_wkA77Pt-sYoiS-0JaCHXOribVpYh1vOZRKBoi5q31sjMvzs2K41txl3B-GWfZY4SmelWBp11oh42Rn1QSqHuKEJpKe-niuHAkEtAfJJxNYHO_f9z-ItF87sik5G_BdRiiGOW4cmNOMn6XuN9OF2BdAFOShpI5P9AVLefwkpAl-_BVl-VFXN4hOpb9jZIRbTH_uQw3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏شبکه ۱۴ اسرائیل :
سپاه قدس واحد جدیدی به نام « یگان مختار» تشکیل داده است که با کارتل های مواد مخدر مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67376" target="_blank">📅 14:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-REPrvEIGrN7HmlbAHkBlXlrfBiG6FQ9RD7xnudU6BMOwDeoF3ur-rJ3gLEsiqmHpH9F7AsKHN2cKQPF6bpcGn4GGNoD1NqaF-mBWbt0DG0-WOEGLq33RqDl269oxu-QJG-Tm5lKQVKsiLRoGrZ194E6ABrcVYINBYtjzkfbEvf5HyRHed5PChHwn1_bW9HlhQtU9V8MOeciZ_z9wjkRx7KoUx0snyo9Wbh-jn_W-q7jFk5kmt2aSgOXIUSUx6fGm5Uc8V8AbP24LnDa_VXvND3LjZ8MkvlIKxqziea_jIriUhCaMszc7tDBTXy8i6QXTiseFNFgTQ-bgkyD0LHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک بنر در مراسم:
دونالد، نابودت می‌کنیم! از توجه شما به این موضوع سپاسگزاریم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67375" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsJrvdtBwgBfNCyyxUcjWn08nMIvDxndtrjR92yfST_ySLa8bxiwkVqx0La4UZYpFwW7SuoZ9XO7wfYXHLSTB1-nI1ZPTA-YbTgrzK7lnlDbVxJ-p4FSKQbYHR2wRNEAbX0sGTiQ8OtfvEQZMuebayXsuEAk9mUMmZgnePrRT6K-fm737fU8K5dip14XCJtCEJNhrRjhR7M0YV816nYGoDniRmda8bjG80Iml2GPvGCVTLGKQ-o2WVqz4jhJvtVL93qMd-e-8_nhA98s_3JesDJkjHWASY7Y2AVYVkTVQkAFvSrvsc7ggorqpXSQ2MO2Gqsc0L0I3wON43h372YydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ادعای
نجاح محمد علی کارشناس عراقی مسائل خاورمیانه و از حامیان نظام جمهوری اسلامی:
در مراسم تشییع امام سید خامنه‌ای رضوان‌الله‌علیه در تهران، فرزند ایشان، بقیةُالسَّیف، آیت‌الله سید مجتبی نیز حضور داشت. او پنهان نشده بود، بلکه در جایگاهی قرار گرفته بود که کمتر به چشم می‌آمد.
هماهنگی بسیار خوبی با نیروهای ویژهٔ امنیتی و فرماندهان ارشد سپاه پاسداران انجام شده بود…
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67374" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67373">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW0KhrrrjIxIfCuGJpAbpjrkXC3_8uXRdmn3CDgc0RbpmpY_7ca9MHr0p4eaK1Yt-V7DoFd1no3qQThOP1zebJeqN2HWV414DzBEzRq3RxFKcs_C_kuDCbpTVoAoCwEdONI4ozpYQgQf8X3BgU9CYD_UFCOrNMafXsZ81pivalyQlECcTrjIp3IoMcVOtv8ujLXWcbDWEqh9Nmp-jKedlQu6diB9gqRs6sUThUiuy1dAE7dny8ZFfqo6IDDrl6SAwMPki-hjVYb22fFMSHzJNAgn3g0kzX0i0qLdRCyy9Ua-Rz7bYjLcnCw3mc97AoFZ9qYg4lIBYAf71wb4mJyZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
«آیت‌الله خامنه‌ای که مراسم خاکسپاری‌اش هم‌اکنون در حال برگزاری است، توسط اسرائیل حذف شد. هر رهبر ایرانی دیگری که برای پیشبرد طرح‌های نابودی اسرائیل تلاش کند و اسرائیل را تهدید کند نیز حذف خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67373" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=M9VPDEAuQvVLYJsBOHy4z-lCtujw5IM-NWRS4Hf3MDXDl0EYqPe1C0ffWmnFlLYnB_YQfoLW0Y-fFvEe2_e6syJeaymLF5B-jujR8KnH5spt1UiFGzTdEMzHMR9w2KyenXECQmE1NtR8Rn6iLWggBuo_3k9dpeeh44bi7LoFGBO26dAfu2I0czGzq1Lyg5qOKzMD3Zk9A9aJ_lAEKe0qcagGkhx-pJr3w6jwpUwlRrMSXH9iizdR8Pb6F4kR8Vwe0poVb__hUZpvzrcWMmGf0NNZlbwRlgZsI9isoJ2sOGfTzf7BlwGNeZUSsqJo6mI018Y4YkVE5EMki4pNAVSgxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aca7392a.mp4?token=M9VPDEAuQvVLYJsBOHy4z-lCtujw5IM-NWRS4Hf3MDXDl0EYqPe1C0ffWmnFlLYnB_YQfoLW0Y-fFvEe2_e6syJeaymLF5B-jujR8KnH5spt1UiFGzTdEMzHMR9w2KyenXECQmE1NtR8Rn6iLWggBuo_3k9dpeeh44bi7LoFGBO26dAfu2I0czGzq1Lyg5qOKzMD3Zk9A9aJ_lAEKe0qcagGkhx-pJr3w6jwpUwlRrMSXH9iizdR8Pb6F4kR8Vwe0poVb__hUZpvzrcWMmGf0NNZlbwRlgZsI9isoJ2sOGfTzf7BlwGNeZUSsqJo6mI018Y4YkVE5EMki4pNAVSgxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حضور احمد جنتی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67372" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=mKXHjvRvayxUalWJ21V1ugqemjZzjSKRsdubyL97hpwVx-ay1835sxz4BqPE7hdEDBzTR4VUhraGvXe4Mdx0phvgNbKctXzuUSxKO8iNewV5jJYFla--dBDaaErcQF-L8U4utIwECoISVTE6t7w9F4lbzVmXGet-p6imOHkyplMXrZZMjSP5Kn3vjUj3oYPzMAj28lVFadJFOSOAXCeeByQIdRJkxvWeZRtfKqc7OLKI0CzgLOdOiBjHVFXgEa_SCsjNLuLBYNiSk98NOtpZ_kr97LkjchL0K4a3bnFxB8muujje3BJeuX2D8Q2Owbf9Br28fD7v5Y0c9skvitCH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad63d7f30.mp4?token=mKXHjvRvayxUalWJ21V1ugqemjZzjSKRsdubyL97hpwVx-ay1835sxz4BqPE7hdEDBzTR4VUhraGvXe4Mdx0phvgNbKctXzuUSxKO8iNewV5jJYFla--dBDaaErcQF-L8U4utIwECoISVTE6t7w9F4lbzVmXGet-p6imOHkyplMXrZZMjSP5Kn3vjUj3oYPzMAj28lVFadJFOSOAXCeeByQIdRJkxvWeZRtfKqc7OLKI0CzgLOdOiBjHVFXgEa_SCsjNLuLBYNiSk98NOtpZ_kr97LkjchL0K4a3bnFxB8muujje3BJeuX2D8Q2Owbf9Br28fD7v5Y0c9skvitCH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی عجیب منتشر شده از وحید خزایی شاخ اینستاگرام با سردار رادان که میگه کار دارم با وطن فروشای لاشی،ترامپ گفته گوه خوردم
من سلطان دختربازی ایرانم ،حتی سردارچندبارمچ منو روی کار بادخترخالم گرفت ! اماخداشاهده آنقدرمهربونه،هیچ کاری باهام نداشت و ولم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67371" target="_blank">📅 12:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=AlKjvZ9Uwl5i-VGqjOT-8X1SChtI7ZsGISkxCK7U6O_tb6xI9Pi7BKniB_6U-Jpap04DM9AJx-v6RjHbMO_Fcb90paHWev9t4Pqv0NPL9WUMTecOKi566k-92O9KdbUVpbEny4DuzENf8zcz_tCAo3ueiy1vomO72ahw4Ir_Sa4g9MmpZm9_GcyqA__KBxzKD5_ZbxthRUYit0CfAUDcb3lVtjQWrB1S7EIvehQk2Go8ltvCG_c3z8gXBhQhr8HvMkWyN0MqFUT7SGbota2EXY_pcJzA1L13BZWclqh7oykjZ8YG6_gJlYQvU2srCf-aN4yevXQXrLYuGPtLwhxYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=AlKjvZ9Uwl5i-VGqjOT-8X1SChtI7ZsGISkxCK7U6O_tb6xI9Pi7BKniB_6U-Jpap04DM9AJx-v6RjHbMO_Fcb90paHWev9t4Pqv0NPL9WUMTecOKi566k-92O9KdbUVpbEny4DuzENf8zcz_tCAo3ueiy1vomO72ahw4Ir_Sa4g9MmpZm9_GcyqA__KBxzKD5_ZbxthRUYit0CfAUDcb3lVtjQWrB1S7EIvehQk2Go8ltvCG_c3z8gXBhQhr8HvMkWyN0MqFUT7SGbota2EXY_pcJzA1L13BZWclqh7oykjZ8YG6_gJlYQvU2srCf-aN4yevXQXrLYuGPtLwhxYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=J4ZYzKkzsUGm09596ZcBEyBw6lz-L6Y_9sJdUMsjIDe8eC7KTXh-XLW9Gup87zMB6smpRKGjACkusN1PYnfOHuB_tkPFQxi5ClcsRsn_23KIWSug7abVOu1t_IRFdicts3u-x8dpAV_G0l1TULiEyZ6Ll16EqSfQrf30PjspNzDx9kRFIGNxBVWNjaNoYoMfX5M9tn4sS6-I8g9_pxT9viem5SLTKKGnN27HJ6dn5x624_PMF_XzNS7aHhjnZkM8RnpAyPibJ3_Cf-d9SRPZviMPrIM-jXcEEIYOLk3pb7roM0pXqdkeGyee13oF-X37Wxe-h6GthvvoUdKIHllTmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=J4ZYzKkzsUGm09596ZcBEyBw6lz-L6Y_9sJdUMsjIDe8eC7KTXh-XLW9Gup87zMB6smpRKGjACkusN1PYnfOHuB_tkPFQxi5ClcsRsn_23KIWSug7abVOu1t_IRFdicts3u-x8dpAV_G0l1TULiEyZ6Ll16EqSfQrf30PjspNzDx9kRFIGNxBVWNjaNoYoMfX5M9tn4sS6-I8g9_pxT9viem5SLTKKGnN27HJ6dn5x624_PMF_XzNS7aHhjnZkM8RnpAyPibJ3_Cf-d9SRPZviMPrIM-jXcEEIYOLk3pb7roM0pXqdkeGyee13oF-X37Wxe-h6GthvvoUdKIHllTmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4QYWxXQUpYRgvYTHyf6eWrtVbIjAhjR14GHDPdpVAnUFgu5NIFZl_ntcPWtBuMBlytgrrWICQl8roy6aDKKZE-11-Fu84BqSb7H4Kd2vRKlXCpfVR7DTqJy5o3ECV8wU1vda_Ohc4OWd9_V3W6tWnbziueFUPpdEbkXCVDFz3T6S4B7JkmlKmsD4ikzuHg1mboxMCZMXDSj1gkX_wZENAYF78SsjiS0Ew97gxVvdXViw7Ot3Fzazzt0_karKATPZkvbea9QrzJOmT8n_t7G4aD2O0dlEyaWK1ME8aoGMfa6niGsjCYSbapUvxZi204_M2BIU30SaLxQL2TjiS329A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=h9Af2fcbvjOY1NaONpHqMICBJfcqCzzF3RycFzuQJMA7skuyh8OQgLg7TjV7ZU6tfiOiOyQyhagC2vmUHtZmOZApDBmtt5nxihdUtWtt0h7rkNyuvAuLWSTp5CkBUh-qvOIX1XzqbWGLVOEOZZQyvakne5ezXjhGMZc_3G0a0vJo5nm1KsQFX2w4yyqQaUO52-D4Rl9hw1RYTDO4Xc18b7kofE3TST3grr2OzXqcvcjl8l5a3OTecKsNo84ZiWTsraik2_Kw7s9IpgJhjTbSIh6KoJCALUhnP1YFkHbaNWYkvwkZUxJ0WGTIjx0A0_IPRyG_TVBCrpqS5d4896luEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=h9Af2fcbvjOY1NaONpHqMICBJfcqCzzF3RycFzuQJMA7skuyh8OQgLg7TjV7ZU6tfiOiOyQyhagC2vmUHtZmOZApDBmtt5nxihdUtWtt0h7rkNyuvAuLWSTp5CkBUh-qvOIX1XzqbWGLVOEOZZQyvakne5ezXjhGMZc_3G0a0vJo5nm1KsQFX2w4yyqQaUO52-D4Rl9hw1RYTDO4Xc18b7kofE3TST3grr2OzXqcvcjl8l5a3OTecKsNo84ZiWTsraik2_Kw7s9IpgJhjTbSIh6KoJCALUhnP1YFkHbaNWYkvwkZUxJ0WGTIjx0A0_IPRyG_TVBCrpqS5d4896luEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=gYGCxbq_EBQGhn8lpcZHjrNBSNuq7Ix9J_KRdpZCcaHuMuklKf8ItduyqyvFINnvoknAQBhSKn_22t4y_PR6pZU1VAtxtHogVo1jVy9ZEdCWcwidPHkUBmjNNDtS8vXu2xA8U-StHTxz_NPDWJZzXqfMxFFqp3v1vSH573GSb0-ZBRHwXEJaOG9cBcgSRNR4HtDaACROrCbzteTlNzPlmQ-G-ES5ciWimeTWpEAlJV301jY55c6l4ny1vcs2FyA_2ViQH5BcK9kJK-zl-eCasH8fxLgNXjkdHgCWpIFhifwdmET2KggSdgdlQ1PZUJjuBItn_RUfDqdfexiw6GzHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=gYGCxbq_EBQGhn8lpcZHjrNBSNuq7Ix9J_KRdpZCcaHuMuklKf8ItduyqyvFINnvoknAQBhSKn_22t4y_PR6pZU1VAtxtHogVo1jVy9ZEdCWcwidPHkUBmjNNDtS8vXu2xA8U-StHTxz_NPDWJZzXqfMxFFqp3v1vSH573GSb0-ZBRHwXEJaOG9cBcgSRNR4HtDaACROrCbzteTlNzPlmQ-G-ES5ciWimeTWpEAlJV301jY55c6l4ny1vcs2FyA_2ViQH5BcK9kJK-zl-eCasH8fxLgNXjkdHgCWpIFhifwdmET2KggSdgdlQ1PZUJjuBItn_RUfDqdfexiw6GzHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsWHEGVZ7ggrgYcG9KWuByt_-f3gfac6IZUchOp-vANgCvfKKnrWfbE7kBFErXZjMeVWHcgnZ1cbL5rJDuvXglBMYe6jDubt1_Op2VN2GHa_4e_MT4uYM3tLFRkg89gBSO2Fq1PQgYBBoLwpmFGjAeBLIXPd54rhrnhjIJdpa1xzKX5bI1LjtlIVCZG8hfYdehx1-LGh1MRwk-DDLEk7eTusaV_lc6kGvgvhpMGUs-63-8bjCQZhVNmYMswY704R9dmcw3KTmC8emovNuWEmVgAezXIQz5YhzV128hjukfPHyaKJlgDaWNUqTb056p4rnGj7unSZ88UK5u6lN-xmoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vgCicWtV4nyTd0Hfq66RI07ZeG7vy84Mr1IfIc98Hnx-UAI8_5k28Psz_Ee_ilAmsDGv76wUhGzPiMMeoXzbEihLMAGJIEiFOFuhX3A_1GzNQ9v1AuEDQRHNQIyT4cvrpuLulEu5M-R1WGjDE0cQaxofwvwjIdqTGNFDPq267yrMuhv_nI-U36Qdo23V7E2TGBbDz0ZDf5k0TsyeE1gfoMrKt_ryxAuZ66qP4hrkbOPuCnrQFWcrKFTCB1OB28PL37f17GFDk88eBP9HnRbQPjJg5MZ2aXakt9xn_wKkQvBPj72eGSg_r9SQJcgW4J0gjRv8hLcEQe6-4nrW_ig1IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=V3Iu917Avng8s8_wxnmmstSHmMJ7Pn6nbNM_ReTiZdNhceKbsvsXyqtw2GTeKkyoHQwpHdc-L4EMOnBixXuequUZnqntn29zqXQCcaamQo-7hYSh_sgH4Uj33sqCXYWmCgJQwy8to1nME5kvOBd16SB9lZk8MpPA5TtauRFVbFYy0LNOFWwuFAlZL7yTVQq-ThHQY9IUTfaOuwQ3SNm8Crd8Kgk0mTQ9nPkMUDVVk8B9HJjWK5sD8Gtri4LHnfsukEdcKkwVZcwW-UOS0W_YewOmj2fn5UhuB8c4vFZxUPk1IPhrHomvk5J4Xt4byvj-Nmia5Pf1rjKQ63RyGRZ17A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=V3Iu917Avng8s8_wxnmmstSHmMJ7Pn6nbNM_ReTiZdNhceKbsvsXyqtw2GTeKkyoHQwpHdc-L4EMOnBixXuequUZnqntn29zqXQCcaamQo-7hYSh_sgH4Uj33sqCXYWmCgJQwy8to1nME5kvOBd16SB9lZk8MpPA5TtauRFVbFYy0LNOFWwuFAlZL7yTVQq-ThHQY9IUTfaOuwQ3SNm8Crd8Kgk0mTQ9nPkMUDVVk8B9HJjWK5sD8Gtri4LHnfsukEdcKkwVZcwW-UOS0W_YewOmj2fn5UhuB8c4vFZxUPk1IPhrHomvk5J4Xt4byvj-Nmia5Pf1rjKQ63RyGRZ17A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b139DR2KRlVBWNYU-PJFi-o1AsZn2b4S4Xa-CkU3hVf8_-5ilBQMULnVZQvhAptSXGkEXiVEb7dJThDsLGrdQEd73IKpsDEaOZkztwgpJ0XXh04-aCJ3tZSsICtQi24YLHRv7FWAJ3evDwIMv5ujMNGfWAeks4Lx67aYEJOf3cHgd_1FMRaon6qKlyx_1WYs2-hM0guTV4rPT3bv1XvM8Q68DWR2v95aGMGVEWKueW-O2F7Md4u8GMUUnBV7Cbgic-bMxoiUZom0jCeJE7skyZFj5l7AHOo420slK2arvywZOnGSQrfUNefJP328JTBqsC-8iJhrNSEHOtlJGzj9Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=bCc-chIB6T_zMnVkrpj2ZTSJyuc862M8SlgPP_B0JPuRX-u29ZMvAL5oKR6ZoRW_IU9Et5Gkxafe1LfjZsnZdeQUfxzSxN3fL9HOMc7B2atDoImc0PdGfz6nTTmHiwB4bplIC4fLuE3zPutgDkActMpKNCpht5yh50epjhTlQ_3k_PjWJaOrSpwWzI4ByV0ngzSoGCe9y9Ab_EuzIW-2tnX9oEAhKKJdB9jNfLu037iJclHD6CI7yF9euk8auXbBNlng2trbvOvhVnC0BeH5w84js1qNtoVQ70GaJKVzEWFcCGi92ehndmM7Blj3mdFcTQqW1w8hPi7wxLEMj6cIRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=bCc-chIB6T_zMnVkrpj2ZTSJyuc862M8SlgPP_B0JPuRX-u29ZMvAL5oKR6ZoRW_IU9Et5Gkxafe1LfjZsnZdeQUfxzSxN3fL9HOMc7B2atDoImc0PdGfz6nTTmHiwB4bplIC4fLuE3zPutgDkActMpKNCpht5yh50epjhTlQ_3k_PjWJaOrSpwWzI4ByV0ngzSoGCe9y9Ab_EuzIW-2tnX9oEAhKKJdB9jNfLu037iJclHD6CI7yF9euk8auXbBNlng2trbvOvhVnC0BeH5w84js1qNtoVQ70GaJKVzEWFcCGi92ehndmM7Blj3mdFcTQqW1w8hPi7wxLEMj6cIRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=KwaqHli0epd5p2s4eq3VbibIVruMy5WMyUkNADTKiFokrsxIqfFWrEbdoGgWWLaqU-gVuQFk8VYqijKqlxmNif9ySoQxT_vDW3F_LTcKP95ELLXR-0PoDmkbh4tXM8a0qiy97A8suNZDQza7QUiuH9qbaVoHyNMG9Ym619-9LlhIWhHpV6dXD1S-N_CDce0G-dgtr5H3kWzZZUqld34rgebxR0LlObU87IviJg2aU54sL82RnC9iBT9ImCs72TTHZqV2wqnkawjtthXOWs4WHv-kp1qabPpzqxnodcyrmxbhKYkUS6xqmGxZWIBwtzhpEAjNPtjUh0wBmzRCm57e_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=KwaqHli0epd5p2s4eq3VbibIVruMy5WMyUkNADTKiFokrsxIqfFWrEbdoGgWWLaqU-gVuQFk8VYqijKqlxmNif9ySoQxT_vDW3F_LTcKP95ELLXR-0PoDmkbh4tXM8a0qiy97A8suNZDQza7QUiuH9qbaVoHyNMG9Ym619-9LlhIWhHpV6dXD1S-N_CDce0G-dgtr5H3kWzZZUqld34rgebxR0LlObU87IviJg2aU54sL82RnC9iBT9ImCs72TTHZqV2wqnkawjtthXOWs4WHv-kp1qabPpzqxnodcyrmxbhKYkUS6xqmGxZWIBwtzhpEAjNPtjUh0wBmzRCm57e_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDMFfJFSs822cW0aC_A2yQXYCUomYF1m3OAw1GIAP4UkdBwsbzilc9K0X0jKDcFru1sFoaRRnZUuz6nMxQhZZjF8cYJCPb1_4u4ofqvJnIXwowdPWni4X2GoLKQOucPywkZiFC23U70LDt8FbbXsnqlc8nw2NbY2thagdySOn2ia4QUlfOMvGgMC4nLQeUPeo4XsKkYwsmHrQr8nVn1NNByIllP_cazHGxZZs1Iz2WahAUmZur0Ggzil-74Juh9Zs7F4fR8jE_x-aR3_X3yvbvJxV63OJLf4trX1LOda4d_l_o6cLPhjff0qu5LTVcjrYE64G32NvwgBs7t_jGDkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=OKMEQXCbsmXKtKOzfhhsAUOlpSROPj4zyiqlECHec77vhQxJjkYJJogh_aM2xTw9QGBzeGEQu0M8v8HuF4yftqN5yPBGdjm4XIsWPSNqXH0TEHWo3kO3ZMhAgKb2r6kXOc5l97Mloq42iMR2PHJsCv1Sy10YplC9mPda2hTSnIc3I9B6zS8biBpIHAwOPphfX7exD5FNKKp15HQoOgsjwkOK6-8ViKMmKWZ5Mgl0LrJtw5IrEYZbCjG1yg0VftruDaBhBw5l8Is2ctgh5fddc9ywb6r1z9Dc5WhXmp5bCzGRM2mj6b3XPhPt763GwYgTeoPrr8uMGnqIF75MkgNO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=OKMEQXCbsmXKtKOzfhhsAUOlpSROPj4zyiqlECHec77vhQxJjkYJJogh_aM2xTw9QGBzeGEQu0M8v8HuF4yftqN5yPBGdjm4XIsWPSNqXH0TEHWo3kO3ZMhAgKb2r6kXOc5l97Mloq42iMR2PHJsCv1Sy10YplC9mPda2hTSnIc3I9B6zS8biBpIHAwOPphfX7exD5FNKKp15HQoOgsjwkOK6-8ViKMmKWZ5Mgl0LrJtw5IrEYZbCjG1yg0VftruDaBhBw5l8Is2ctgh5fddc9ywb6r1z9Dc5WhXmp5bCzGRM2mj6b3XPhPt763GwYgTeoPrr8uMGnqIF75MkgNO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf5rnXQMHpGdREkZP44jsD-CuHNuJkDUBGSD24nY81sb9a_mZfCToDvELe1PHx22Kv_Fw3A8z686oSgy3knctppSAAmJxYAFZ01ESGtpvCr5vRNKX6r62XFKKu3va9xlWjB6md6haPQSqQvTJkGuF6nlERkJRyillg_q1vHVUDOqv8Q6q6uXozJnvsBnHtev0ZsOoOBPs8SIhHoVGf1HOKZXGsii6HHn6ZAcbgntW15qEHnfFu5ZfdrUCEIrHlQ6DHVt1M8jMFvHOVwDLPNjyaGDXr63ZL5PxBjfsbOWkV4lmr0v2m8KvOlUzHMScvdI9l-dK0w_GK16cqsAV60Urw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=HuZ6VS4-iMo7ZKO__t5DMiozEvtGla4cV1S19R5ABIg4uo_apjLTTkENeTHsYXCkpifEVq5Sw_BEMtuOuWJ-5iBTfY05KQRUR7vKq_kHCmFRUrbgX_pr8_AtTDMGxD2yKRClJlEXKMS8F45e-P7vnMyhiV39-tC5SfJCNvnKU52XwctfGywWglnutEW5Pxf3uYMyNpp4FrzITR0H6omb8jAhQP11RdbH4c1q2nexkACRQJfXmM3PSB9UYWkVR556zYTEopxjrmgQARE6tKGtMySC4JzEEkyshujWmNZmZFRTHM94DBokFGM_Y73-bT-q7u598LGqy15ESgrEClSr4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=HuZ6VS4-iMo7ZKO__t5DMiozEvtGla4cV1S19R5ABIg4uo_apjLTTkENeTHsYXCkpifEVq5Sw_BEMtuOuWJ-5iBTfY05KQRUR7vKq_kHCmFRUrbgX_pr8_AtTDMGxD2yKRClJlEXKMS8F45e-P7vnMyhiV39-tC5SfJCNvnKU52XwctfGywWglnutEW5Pxf3uYMyNpp4FrzITR0H6omb8jAhQP11RdbH4c1q2nexkACRQJfXmM3PSB9UYWkVR556zYTEopxjrmgQARE6tKGtMySC4JzEEkyshujWmNZmZFRTHM94DBokFGM_Y73-bT-q7u598LGqy15ESgrEClSr4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8KP2k_0y_wmNgvdWhTuTMOMYeaQBOD6lb2L0DwKSmrbw0WF9K1qbn1oPX5yrfuQFoviNEyjqTsQL_GzN4d7r74rGmUYNzBonwOGfndsXfVQgNOS30QVqUsW3VnnSdL-kzJYnkRNyU6lB0BUP2NMt8dtRyNaDE9Eh1JP-rvXAD1ab1viGsvGshs0JZK4-_WkgRKQXabfkKZst-jFnss6Z0pbyBRf2b5m32DV6FjFOk4Zj0h5bYmV5qVZPpGaWA3hm6c6ib6DMoiEXzWHcuOUhhCNgb6VV55j_NHAZCNyQxsDHYEWjqAgIEv3WCoTrFcUfJ05C6fPDzELXPVujUXvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Y_bw1yWT7IXaLovm9LgU7B0ap-T7UZwua1zor4dNCAZibbR5oA7Mxu_gfvjeExJ4D85UjrCATW-0kSpnqeOredubeYPk6w-Rso9fbDIzEfj7HnN92_HIX7aXyjri1ohbYUrl-BSFE4FUpfTzNJYsIKniVfWeQwDM06V7m_j-duSfeElIqrbOgjo5niIZs7eDXgzf2xM9Gh9VkDzdYGGSSv5X3yuwAxFbok0MgZnxZFtDS-SF213lmvgO1DHfiZtRrWGWEwQxkGFHlL30hRBpCVJPhaRnBZgDTlnDOX3-ue3XayVOaF86xzt8Q9RsXa4zNxWLJRDgooaVNnrvYW-8Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Y_bw1yWT7IXaLovm9LgU7B0ap-T7UZwua1zor4dNCAZibbR5oA7Mxu_gfvjeExJ4D85UjrCATW-0kSpnqeOredubeYPk6w-Rso9fbDIzEfj7HnN92_HIX7aXyjri1ohbYUrl-BSFE4FUpfTzNJYsIKniVfWeQwDM06V7m_j-duSfeElIqrbOgjo5niIZs7eDXgzf2xM9Gh9VkDzdYGGSSv5X3yuwAxFbok0MgZnxZFtDS-SF213lmvgO1DHfiZtRrWGWEwQxkGFHlL30hRBpCVJPhaRnBZgDTlnDOX3-ue3XayVOaF86xzt8Q9RsXa4zNxWLJRDgooaVNnrvYW-8Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=lp1REvbA94Orj74flqfeHEBRCuRLXXtqG7s52mc4BLjd4mMJAFyV5D2EPBJxl2-UpMlZQxNbxeu37fl3QTYzIM7VlUjxmtnmaowAhS65YRAZ1LoCx93e9UNSqtY0pKCeonhKaI8FoOX3tot3QJVBPhXHt6prvYHhYsm0lK3peMOQY6m7X84T_39k79fk7mppYlmcmHD0oie3WL57Qr8LI3Iy_m09l9A5erI2eiBUEZv9HjHuNuDGdMHxaQjiBLeTLzziI3GhZPlLDig-GgtuKcPce4KYFtJfCdkuCZQxxBGKRqcNKteR0fNx4oqPSHKPSZYZARqoZ9LQioeFKzETag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=lp1REvbA94Orj74flqfeHEBRCuRLXXtqG7s52mc4BLjd4mMJAFyV5D2EPBJxl2-UpMlZQxNbxeu37fl3QTYzIM7VlUjxmtnmaowAhS65YRAZ1LoCx93e9UNSqtY0pKCeonhKaI8FoOX3tot3QJVBPhXHt6prvYHhYsm0lK3peMOQY6m7X84T_39k79fk7mppYlmcmHD0oie3WL57Qr8LI3Iy_m09l9A5erI2eiBUEZv9HjHuNuDGdMHxaQjiBLeTLzziI3GhZPlLDig-GgtuKcPce4KYFtJfCdkuCZQxxBGKRqcNKteR0fNx4oqPSHKPSZYZARqoZ9LQioeFKzETag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPUssm7Cv2OZqW6RWqHw5uooH29LCzqp_1QPuSvzHJpKQhYYG3V5BbyVBb0v3VJR41G631-Y-jjButwYJEZPCFEOIEuAvhP49n4ThvQEHPPjfweqYgjDWVaH0mN9po0l0hl3Mc95ozbswc6UyWA4wC-dTJOROjd3DvHL5TdhckXVprh8iC8jJ8oZKpquACfTuDJJBR7tqJRxAeg00AUOAQ9v1WEvm5_Yu8-j54vwwqQCZHTLT9Tu6etSjR1PZQYD9KsiUhKA6hSouPr7gug0bCNRUJRceVA-Dvkg_6TO1k6E_5TbaeYcTCmtFiCERPwITrs5iVRiNAbMwlII-wh3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQ9NvQlnA30l048lFtQIF0s7NErMHJsH4J8OyWdW-ox97bmVYPrIL4qPrsPoe1UaJvG4t8g0mtlOff6yYpgpPgRSi1CTUzV1C0GtL9x_obuQhUJrmeR7UhmpojRJdYBa8KWmMMKbpNc3Bcny1H0iUNXpBDZwgMe4Z29ot45xH5v-CiCBMiFTST-Y7SwkA9oKJ11w7XuieHV502jeZFfs_BzMEk-M3VJr9xwjOpX7tqr49r8V3QcVn7T1HAMnA1hrd-iVYLlC43hcWw6wELcT7MCE68JtNDmxse-PmaQ52nJnIPGw0QpyQaJL7qbbQcVjjW6I27hntY23k8BeQ_WLBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=Yt0kKDmQaPvQsJldKJJgMA2D00kPQ-GSB2XTqsniL3-SvBjZOXEGDJ3mG47QqpDYZN4ogGObuHOunbetL9uy3WIBy15Fz8aO-s3Fv5SKLSnB1wkTDN0iZxKq9PKGO7IR4WN4iwKRXTK3Nvxe4-AvgoKRKPJOQeq-XB83GkRUyh9LJPDp0C2H6wnD7rZZdFskxYX0ZEKarB8I3Do2ZrqCtCVndhknjwpz2YSeeWGmtOjZjYVbg7T1V7Wevc65MqAXcsS93EbzeOU9d9wJhKqIfn2EgRS7sYSDTDaSJ7nsG712jrdqhVEvVe6jTR9aOs7J-3NeTlj-RBH-CnI5RXmuEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=Yt0kKDmQaPvQsJldKJJgMA2D00kPQ-GSB2XTqsniL3-SvBjZOXEGDJ3mG47QqpDYZN4ogGObuHOunbetL9uy3WIBy15Fz8aO-s3Fv5SKLSnB1wkTDN0iZxKq9PKGO7IR4WN4iwKRXTK3Nvxe4-AvgoKRKPJOQeq-XB83GkRUyh9LJPDp0C2H6wnD7rZZdFskxYX0ZEKarB8I3Do2ZrqCtCVndhknjwpz2YSeeWGmtOjZjYVbg7T1V7Wevc65MqAXcsS93EbzeOU9d9wJhKqIfn2EgRS7sYSDTDaSJ7nsG712jrdqhVEvVe6jTR9aOs7J-3NeTlj-RBH-CnI5RXmuEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=pElb8W574BZ4csWn69kfNl5Lgaos-_egBbXf6Dd-ZjV7Zc4_mAHFQqE4LjUMGzogHDGRoA3jV1wvIZhdfNiP4_klVB11WG4UAEpC6GmvxxanDqjXCMnKQpJxMmVJZBHRK2Y8CI9Vuvcbm6ucyf1OQPcZPPDj_XR1ClvJlwmmLNPuJLmX_r2BulnQ4AW05Fc61xBpEUfw-1-wYHrvwWwumN4IlNxZ-qI6WwDPJAxsBe09ViQExyoHxLknJDWgb_ZgSYc92kmXv4TsPob3Cxyh3G91PBlPk6GVbdLe8ETyEDLVhXbX26U8nnZsaw6HxfoPxmptMfsVnF1w8SzUb20OJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=pElb8W574BZ4csWn69kfNl5Lgaos-_egBbXf6Dd-ZjV7Zc4_mAHFQqE4LjUMGzogHDGRoA3jV1wvIZhdfNiP4_klVB11WG4UAEpC6GmvxxanDqjXCMnKQpJxMmVJZBHRK2Y8CI9Vuvcbm6ucyf1OQPcZPPDj_XR1ClvJlwmmLNPuJLmX_r2BulnQ4AW05Fc61xBpEUfw-1-wYHrvwWwumN4IlNxZ-qI6WwDPJAxsBe09ViQExyoHxLknJDWgb_ZgSYc92kmXv4TsPob3Cxyh3G91PBlPk6GVbdLe8ETyEDLVhXbX26U8nnZsaw6HxfoPxmptMfsVnF1w8SzUb20OJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=jUoAu-CB6nBAdW3YY4eM5-CsS8fpdP5gZJetuaqZQuF53hmpnEndt_6wh3gIDi0TmAbz8ek5E2KrrCa6Up-YUuEdkaHN6wwey0Ran1i8GebtWweURF3oLg_kExCxWfNNwLKFr-0M3SS0w9uubO0GjjTGc7gZCA4AevQB1ne6HxOIfXzV-Q7y4R-i99sRSQFGyTJ5mglgcDB2JYhoErF-HVoUgQ4Hqcj9siY6JnLY04rVohR_btgNuEG_Pn55Xd56j8_Ko5KkZty0H6Lmmc429zVHwcQzZiKTDCGA4dDwRzyZVlVmrbe3460fPKTkyRnTefHepx_e37bwlTGrotmpFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=jUoAu-CB6nBAdW3YY4eM5-CsS8fpdP5gZJetuaqZQuF53hmpnEndt_6wh3gIDi0TmAbz8ek5E2KrrCa6Up-YUuEdkaHN6wwey0Ran1i8GebtWweURF3oLg_kExCxWfNNwLKFr-0M3SS0w9uubO0GjjTGc7gZCA4AevQB1ne6HxOIfXzV-Q7y4R-i99sRSQFGyTJ5mglgcDB2JYhoErF-HVoUgQ4Hqcj9siY6JnLY04rVohR_btgNuEG_Pn55Xd56j8_Ko5KkZty0H6Lmmc429zVHwcQzZiKTDCGA4dDwRzyZVlVmrbe3460fPKTkyRnTefHepx_e37bwlTGrotmpFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=iV2s2pidQ8jGgBierHraWBmiP09awaelhwWvOgneeI9pbnFuimnLAoApvvhWrYYA5cZWLivcZYCwrRAXGT4Lp7hV_WzIQZ3fK2A4EEhIMHLEVFx0Voc3KneidrVfbx-hY-rNtc-mfFiWUMqK1-0-ILQ4qIpahvLCKTSKQLP0NOH_Z7jPaJw9GtK9tswTCClKJvYSMV98_4Yy-lwZmpaRPmPz4h4bRvPWWubyxbYn-HInRV3C4mrLKH0b5TNPXTnrJKv9mvaidBPkEUZWSmVny0_jSZ4uCdwuux7BJEP_XBFSmIgZw98g1werB6UwpBw_Bi0uNYicy2xc7kJWQ1ZCag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=iV2s2pidQ8jGgBierHraWBmiP09awaelhwWvOgneeI9pbnFuimnLAoApvvhWrYYA5cZWLivcZYCwrRAXGT4Lp7hV_WzIQZ3fK2A4EEhIMHLEVFx0Voc3KneidrVfbx-hY-rNtc-mfFiWUMqK1-0-ILQ4qIpahvLCKTSKQLP0NOH_Z7jPaJw9GtK9tswTCClKJvYSMV98_4Yy-lwZmpaRPmPz4h4bRvPWWubyxbYn-HInRV3C4mrLKH0b5TNPXTnrJKv9mvaidBPkEUZWSmVny0_jSZ4uCdwuux7BJEP_XBFSmIgZw98g1werB6UwpBw_Bi0uNYicy2xc7kJWQ1ZCag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=qtNy1izFIQfCwX7ybx_za5JYzizyIXwmY5U1dNh3K_Uoos_B6ICQJbnYySP81C009paR5pQuNj1c9xCEupHkLIXBFtLZlHDfKcW_NVXsrETiu2Yr6zvLT0i1i6VYyisXwNCNzwv9HJeKq0Cgup1A3MMhXMmWxqV-2Bc6drsBt1XWJSvpWhGwmDwPly_zG34ekrSzDNJ7FXAobzfV1IC8SZgVFHL5tgRdMqBywE1bYCGzcEqO5r0W5ADfvfkiVtsRMYwUjmfZASu550CKOaxAZ8SIhskJiekg5PdlbfMorARrDLVe1C36-emx3f3q7vdDGus4sZU3e6QGXF1iW9Rrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=qtNy1izFIQfCwX7ybx_za5JYzizyIXwmY5U1dNh3K_Uoos_B6ICQJbnYySP81C009paR5pQuNj1c9xCEupHkLIXBFtLZlHDfKcW_NVXsrETiu2Yr6zvLT0i1i6VYyisXwNCNzwv9HJeKq0Cgup1A3MMhXMmWxqV-2Bc6drsBt1XWJSvpWhGwmDwPly_zG34ekrSzDNJ7FXAobzfV1IC8SZgVFHL5tgRdMqBywE1bYCGzcEqO5r0W5ADfvfkiVtsRMYwUjmfZASu550CKOaxAZ8SIhskJiekg5PdlbfMorARrDLVe1C36-emx3f3q7vdDGus4sZU3e6QGXF1iW9Rrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF8jqlGPqba6_EP_jCyrIeWrTn9IlqDfTvLnMDFtlHkypizShtAeKpzC2zUrcg3qj3-EWQE5laKX87RbKZjqlMNRBa-vloZtPU9sNy4zd4clHc9PjbpRFQo7VUZ6WLU8SCl8eO3uIRqifVjcmRDnmJfP8opmoEdJUt1v7ooN8hXUOdmE10cDZXQZTUpKXf1br9ruLaEInXrPwRc1xXgEute3hMYXzN-otwUn34K9nqSCmgcw09oXulOimqrCK1AwhAfI1LAtttwS7MfYvC_vV_NjoxSA0WJd5p8pcXYeOoLej9xcou5R62RI43a-NDbS7nmwqi2bDG9Z3AjS6ZP2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=hjqQffuTWOD_N9CRP_nb0VuNju-Mv2ihNXgabn-Z2MNfKFF4KQ04n4XSajT5IDxijt1lX9qsAAay9Y-wdPuIBzAmEHuF_1OKXso4JxVUnWLybvi9ThT9ZVakNuGIPb9n7zZHkIWvfoJRlzqUYH5LUG-E17CnKXc0lIf7fcpCAa8pohBjbhXlWy1XV1sSvbtOE3afkcDdZKrCnWEgS9-9oyA4qJYWtwZQtOggBEAe_1IHTYwl_Ajvsi2vPcYfz-c7bAJrw8bV-u04DAAfAlKUUtaIvw_8SqUIXM12NbCl78hH5e6EE-84Wn7zBwRFNvZtS4xhzfXTSfR-jN6kFFQ-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=hjqQffuTWOD_N9CRP_nb0VuNju-Mv2ihNXgabn-Z2MNfKFF4KQ04n4XSajT5IDxijt1lX9qsAAay9Y-wdPuIBzAmEHuF_1OKXso4JxVUnWLybvi9ThT9ZVakNuGIPb9n7zZHkIWvfoJRlzqUYH5LUG-E17CnKXc0lIf7fcpCAa8pohBjbhXlWy1XV1sSvbtOE3afkcDdZKrCnWEgS9-9oyA4qJYWtwZQtOggBEAe_1IHTYwl_Ajvsi2vPcYfz-c7bAJrw8bV-u04DAAfAlKUUtaIvw_8SqUIXM12NbCl78hH5e6EE-84Wn7zBwRFNvZtS4xhzfXTSfR-jN6kFFQ-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioJv-8HM5Zh_5YfQxIujggKCF4wHkdjGSiyEJUu8ZEn93FGMn4eV7r96Dzor_KU1iScTh8aiWuVGfD17hXL68LsFFn6KJbzqHBbHcsBkfWtVVwQR9gFBbnbCiG4hj74eHBFofte7gYhRoemvC09yBbsyDLF0ouGD9rPHcnsPTD8WCqViGmCGHHbJa1FbzgwmYPXXjw8F5YMMmofjaK1YzZ8ZoUPOqSlB0u6UQM37Y_06-N2GiDFCHYMjsYNU9d52xupNqExQxLIcVVJ2T8WpFH_HIWhSXLD7kPyz6g2WgvWePEkFi6sxKtKWbeJrAlxv0jllZTt_Z-0LFUDmvbdz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=dCJ8rAbDq1tKc8As2A3Lrp8zyDK6asL9YD-NfF49POisaYi30etCvAFeQBqWAGlVyPJAJ9PLKFfC4GJ39vEuEV4TNOzZKSNJCUvFdZydkEhlObve2m5em5M_SWE-OSqyPiA7_RXZZKeZjetQNHBIHXLw2D0dN_gOymXZYlweZW8mIbim_v6707VZhZW12EHT5NVmbaTiT-v9hmaQqQfpEpSTyYgi-A66wbRRCysO-4DOE5eF5M5nFMlx-LAezJ2BHeIZFejXKEqfQmWAQeL8tCVaDnbHrxjbDVUpszl2SctPRBKVN0KRwcohep104UjEecgEPTKOTiVbVckSM0rsTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=dCJ8rAbDq1tKc8As2A3Lrp8zyDK6asL9YD-NfF49POisaYi30etCvAFeQBqWAGlVyPJAJ9PLKFfC4GJ39vEuEV4TNOzZKSNJCUvFdZydkEhlObve2m5em5M_SWE-OSqyPiA7_RXZZKeZjetQNHBIHXLw2D0dN_gOymXZYlweZW8mIbim_v6707VZhZW12EHT5NVmbaTiT-v9hmaQqQfpEpSTyYgi-A66wbRRCysO-4DOE5eF5M5nFMlx-LAezJ2BHeIZFejXKEqfQmWAQeL8tCVaDnbHrxjbDVUpszl2SctPRBKVN0KRwcohep104UjEecgEPTKOTiVbVckSM0rsTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np9cODfn3hJt_XrfZck20wNnBtCH7yml-2P_ev9wHeJ53PGdAHLUoa5XFPDpBXvCFFPwhBJJ5xLy_mF7OSfQt2l17FOKFRXnPet-K3bhvFwvc_PxCggIFFqaEDAx9GnikATStbc0ins6IYnMeEuAB-Bk68SKnoW-n9QtwoXO6FnmMXs9vKE7ZyPYnSJftECnTZQKlmjbEFDX4SBgKA4_MxZAPTM3uDeUlT5BQQPGwjS3-Wiw4q5yVGp1abZJeOYdIjuMnowRUZV0R2b6j7J-IZAividCecT_-Ih-_q91SMkeSbfrijyaWRTY3Ek-Ad-07Ourdae2EPjWWGzQfpDr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErX9k-GSWenI_4ENIEK_bAbXe0-vdGXOlUGxXUuHqudAMbISquCGod-Xcx_SA9CHfIUco5oHfMRhiBVE_3RYsKmc1PHcI5oNgqZDV2iGYre2vedGNVfsYQ0nS__-sl_ig3fvHHVaC6PCGBKB6s0-xkClGky2jt1rt-VzvKc-DCfeIfe5aYvwA107Ch_DI4XHnSB9lKsuxo41FvftUUineU2gJYsu7l8LabIADxM9sLlsd9qpyPl8-b_THOS9tp4xUBlco7AoT3L5o2T5qDPOgm9eyu9hmtx3oddRiSvRlrlMKrq3b3xhUxosqf48cuZz2S2oXynxdPLqwT0MI2baqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHN4krsgSl91fLkzoZEsezQv6I8TfZbiCnHKuF0q_hTFt4gmkIJR6SMSLc077RCfHpfiKj7EZHMVlcsB5bZVTvu_yjaGgwOHvuPTH0D9PBU2tA0D1i8dFOLKze8_gTgOEN2Ru69yU-M1sYlPD0UDQEWi3MQMjDxNlJ3vX5iaSF5xZWSgdd595y-FhTSnEhwJtyk5Zqr33U8gFW33FBmtLGkf14sOJw0SdLIk4wiY7kMWAozKrtXRH5VlKQWeJcryRbNOARibrAogVz3ges0RO0pL0QX3oBHemEkOw59ldA7JNKHw9hBDHropRma9g76GxYMN991hOImI-vx4cUXyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlWA817j3ZXfixiadlOOpdJhG72kvQypw0X04f56DkUFDk4Sb1IC-BmfptF3l339JRlOKdd3q14XOl1JkkZ6o74vFUcRODWSDt1Gv3oJcUP7oncjhH0VTi65JV6th8QvdsO-mIpa8L2E0OhNbvgSOUwZwxriW_5HG8i3RM7S1fAs3npthPiWaZ7r2wz6_ExrqhJwWXCKDeRk9g555UENlWsJXDDmoW9A1aLVLyRxDXJPj4f1w9Rbznp16ne0yhL2vMYj-2Dhdnp5Y7msbN8H7ylA-bdpABsT7GIgsdQzrTlfgdAjnLKQRA8kDkAUp8FKqgv4aGN24BrQ0JFoxCqZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=jVChYuvMssyIzHgL6ENFRjXJtLu4-wWChGkNvJxPZTrTMw0lFXo3-TnV68P62t1cXSe4arrqkHejMvNBoEhyCxc5I2FzQV9tZkUEsA8H-fx2NA9Lp-AXdmEfprpivD6eZWqZLpqPHmPFbnEoGLwyjvtKTWOmcEwcmiKfSr4AXvl3GMSRFMvpUbYl99KK-SzARP3BC40i3ZDHVuUlFLRWXNOxQI1fE7npLkUzlSXMzxlgjX5MmHjBigu6o7wcbahOsVcAHNhggefS0aguCNii0XqlQU0ZRCFQINxPB-KUKcnqXraE1RLifoqM1wQGRj5BWYxzWm85sUXKAiNdwMi2Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=jVChYuvMssyIzHgL6ENFRjXJtLu4-wWChGkNvJxPZTrTMw0lFXo3-TnV68P62t1cXSe4arrqkHejMvNBoEhyCxc5I2FzQV9tZkUEsA8H-fx2NA9Lp-AXdmEfprpivD6eZWqZLpqPHmPFbnEoGLwyjvtKTWOmcEwcmiKfSr4AXvl3GMSRFMvpUbYl99KK-SzARP3BC40i3ZDHVuUlFLRWXNOxQI1fE7npLkUzlSXMzxlgjX5MmHjBigu6o7wcbahOsVcAHNhggefS0aguCNii0XqlQU0ZRCFQINxPB-KUKcnqXraE1RLifoqM1wQGRj5BWYxzWm85sUXKAiNdwMi2Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=XRiL0zv9cAqtvoZcsIGYWX894nr946dOKgWsNukl5j6eZ_oH4p8ou5JgPnDxWdFLcuUIN1l2Qwugu3xM2kg-UIiOviuqZ36A9NOLkuLi-LUMbiO8EpYrLXTgorLDcwB-yB9q4A7kjMiFLESl4NWVktyJGlbdJb2u8aT7Xa4WKFRLMw4w2Di7yCUiRNCUDkByh22uiRVxAA9fB5C7ENY9SpnoqrxNEwDA8ObbHncaR2nR52t4-OdQl_J8NtgNbd_D9IafdUGOGfMclK0OplkR4sjcHd-rPfAkU8nEv1F7oOsNjZGc-sf4s1eKd54LwcrMVPe8VqH8LqVs6MNZ1CwNQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=XRiL0zv9cAqtvoZcsIGYWX894nr946dOKgWsNukl5j6eZ_oH4p8ou5JgPnDxWdFLcuUIN1l2Qwugu3xM2kg-UIiOviuqZ36A9NOLkuLi-LUMbiO8EpYrLXTgorLDcwB-yB9q4A7kjMiFLESl4NWVktyJGlbdJb2u8aT7Xa4WKFRLMw4w2Di7yCUiRNCUDkByh22uiRVxAA9fB5C7ENY9SpnoqrxNEwDA8ObbHncaR2nR52t4-OdQl_J8NtgNbd_D9IafdUGOGfMclK0OplkR4sjcHd-rPfAkU8nEv1F7oOsNjZGc-sf4s1eKd54LwcrMVPe8VqH8LqVs6MNZ1CwNQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_nQEMvD08z3c05b3yCkYJEIN2ciQkfQhGMVBplaHt14IzGFOz-wj_HEnP9W7-tCoy8uvsVmN8q8cotmQT97ksjWFWAvSj0R3kqI28vyrJL3N9PoVX5VY9rIr-aOuKAFi030Wjn3pHn6f1MF8_mZ0FkqVfxr_WeMos1sisxmLoiQks0Z6-2PCSgWkMDiFn15WYTlkH69cF6dwkPXMCFNiUFtyXuq1AG6hlmJzOZDVTKk36Xn-1Qz_EIUnTgd8rnAkDrvzp7DGRfwTb5GZZ0riq9QXja7QgzUtsyA4iWkwAXQptz4ZVq2fFT4q8JJdKVIhzoxHHXsbTcxLLD5B2ySzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnYFv-BN1YCZf1XazdV9QsP0pMJezJJT7PMz865FjVzpGWslPaz-in0BnzIiNz4ES8id7ebc1Gb6nkVTcU92L4voxXoJtfQEjl_ZI5ITOg9WIZxtg5U_NVE834TXKf8-z4aE8yDm0gA5RlvQUU46LCeRFoyYgdWRsLCb_AXv3sbfAlDc-tJkZ_de0X8DMicuwZlIYDEZK15xgHsvCUrEo2lk0QCe6tOmV_EGN_VNi0w8ifeEqcf_0GbqT7s2zuckqcOZj7CPwnA0N_1qTA6A9qvFAbWoWpyL_HmjrbIPnLSxNQBYe_M95nSBeA72IUUECe8hz4M9jRn35N7ccCgy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=caYG4zUevaluQ5SYv-IJEO99EH1L0bmeA8Pwcpp-hBbCcfgaY7vL6TEwqjFagXnZbi_3SBZcbxnwJAikv0alu-9MHGiLjai8KjYKBo0snTWHbs1Cvur04Ny9zX9M2HyeAzhinNxPxelnLXwr8tD7tORvuxAMk9u1xpLUg0sW7PWqPggdLhrG2j4khr817j5XjR0di9H9IWAiCmDuRrZzvHKc1PhEnkNphXQB-kyPWfnSa5FJ6FyhtiBFtXIw6sToD5sywao0c8OWIJFj6jF_PBpNOBB-XmREup5CmDI2sXYyIoUIcEsapf0iqNGIQ1w4MQI7aCT9dDCE8Otn-cLihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=caYG4zUevaluQ5SYv-IJEO99EH1L0bmeA8Pwcpp-hBbCcfgaY7vL6TEwqjFagXnZbi_3SBZcbxnwJAikv0alu-9MHGiLjai8KjYKBo0snTWHbs1Cvur04Ny9zX9M2HyeAzhinNxPxelnLXwr8tD7tORvuxAMk9u1xpLUg0sW7PWqPggdLhrG2j4khr817j5XjR0di9H9IWAiCmDuRrZzvHKc1PhEnkNphXQB-kyPWfnSa5FJ6FyhtiBFtXIw6sToD5sywao0c8OWIJFj6jF_PBpNOBB-XmREup5CmDI2sXYyIoUIcEsapf0iqNGIQ1w4MQI7aCT9dDCE8Otn-cLihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=pHigmhQPEGtRWhUKx5ZJH8DUdgJkEU4dPs0-EgzlJbt8a8gNtgl_GimQeDd29ZOY8MC1p1A0pWZZlFHbqdVQ9IjcXsBnSeTjJRQ41wjkzEsuK_R0PtZlRXcgrcmVyU2TXj3LH3thHQhm0rLSFz1lP7rdnH8HQCYF7uNcgPpEjW71vDnbngQxGpZk0W8HMrGKrmh5WgHSOj2DfUX_qXdB_dusGsNYxYKLHUg8YpqgIFDdJPE_3hIBlvFB0xOv0675B0G0_MgEoJ559Bxx5F4YOcLEMkHd8Lhguk2l2_TEkVrlHSKzAjfRGxLVLlN77ojQ8E1xjaZZpUhg2by7WtwSXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=pHigmhQPEGtRWhUKx5ZJH8DUdgJkEU4dPs0-EgzlJbt8a8gNtgl_GimQeDd29ZOY8MC1p1A0pWZZlFHbqdVQ9IjcXsBnSeTjJRQ41wjkzEsuK_R0PtZlRXcgrcmVyU2TXj3LH3thHQhm0rLSFz1lP7rdnH8HQCYF7uNcgPpEjW71vDnbngQxGpZk0W8HMrGKrmh5WgHSOj2DfUX_qXdB_dusGsNYxYKLHUg8YpqgIFDdJPE_3hIBlvFB0xOv0675B0G0_MgEoJ559Bxx5F4YOcLEMkHd8Lhguk2l2_TEkVrlHSKzAjfRGxLVLlN77ojQ8E1xjaZZpUhg2by7WtwSXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=KLjKPGYlL_PfSVQu98CmEvwhnD3lgBeaFkkAXCrIF0fBRKlUvsnIVMeOOqTLBB7XCYf6NIIBAQPtsCMLFyTepBNaWz6ZJt1EpKmvb0PLE9Io4XWzH4f1hGjHGsgpM582HIUkN8a3c6dLTIbTXtA0Vi8m2VCymPoZd7XkwM3AvbOwcP_2F-EZzUVmYgfQXyG3gjHW5tCLCOy7SMFuGyXfLFmPa0KtoJ_TZTp1Nx6ooD6_bTEJoe7opNW0DPy6qpWG_TO0RqjdbxRuRrg6d74x5r3WsXLaJH5ruA0cqgXobzQPw7yXQsM_QpaqfSE0N0GTH0A9x8nkKPIniScVeaApLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=KLjKPGYlL_PfSVQu98CmEvwhnD3lgBeaFkkAXCrIF0fBRKlUvsnIVMeOOqTLBB7XCYf6NIIBAQPtsCMLFyTepBNaWz6ZJt1EpKmvb0PLE9Io4XWzH4f1hGjHGsgpM582HIUkN8a3c6dLTIbTXtA0Vi8m2VCymPoZd7XkwM3AvbOwcP_2F-EZzUVmYgfQXyG3gjHW5tCLCOy7SMFuGyXfLFmPa0KtoJ_TZTp1Nx6ooD6_bTEJoe7opNW0DPy6qpWG_TO0RqjdbxRuRrg6d74x5r3WsXLaJH5ruA0cqgXobzQPw7yXQsM_QpaqfSE0N0GTH0A9x8nkKPIniScVeaApLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=BmoxDZokt_hQHAY50NDg-JJx0NaBd5rZSj-biY7n0N9Axf2vz3_U1jrkGVqTTCX2_fky8c6ZwNANXZ8KzT7aeR1M8w2nTeyWZyodFEbfWuz6yjIV4Zj8JLjKnQO33TMz43AoHAvesWWQsPKfH8-XJ8QoibGq7tCx4UY3znySel2fT-tHh1u1oSfP_eC6G4XfDPaU90vWPoG-oM9tQJyqmBvBcNocd0EVVWY5kOt9wXsBLjc687ASgl9PndzUSxauCCGjvQTAzeHgUoQkfnQTtI8rO0sw-GYcuGAuxwqPLwSxGXxAW-fySAXBjdAcCDJNcmZr8ME_aWgYH1eE-tg_xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=BmoxDZokt_hQHAY50NDg-JJx0NaBd5rZSj-biY7n0N9Axf2vz3_U1jrkGVqTTCX2_fky8c6ZwNANXZ8KzT7aeR1M8w2nTeyWZyodFEbfWuz6yjIV4Zj8JLjKnQO33TMz43AoHAvesWWQsPKfH8-XJ8QoibGq7tCx4UY3znySel2fT-tHh1u1oSfP_eC6G4XfDPaU90vWPoG-oM9tQJyqmBvBcNocd0EVVWY5kOt9wXsBLjc687ASgl9PndzUSxauCCGjvQTAzeHgUoQkfnQTtI8rO0sw-GYcuGAuxwqPLwSxGXxAW-fySAXBjdAcCDJNcmZr8ME_aWgYH1eE-tg_xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=Fu6ypyNVmzsiwhUaRHS613BaOmErH_SS2A8wYyxJ2FC1ELecLapKUOatdy4rS9LuVeXkQyhSY66j7tpBtAghTz5lBkv15sm-_ezKnb4RC1fW-pBnl6gXJM0y59hhw-Rw2R2WS7dIUwzaUBTpn9LYtZliqRsjPIyHx4yyI9DamtKQAJdL8VDumyZJISIE7Le48pJ-twBwFXDD92jTe8RIx2Z6Oso1VzX9UDibNpq9NWPHKCH7lSbO9-3nxUrdyZdPTYRX8hMixsXZSYOMKOUVBr_x4NpkX8yG2M5kho8nOnYEGcgH4KiNFEhX3B7XMJNPMGcod7syM6h5VpqFWXrcjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=Fu6ypyNVmzsiwhUaRHS613BaOmErH_SS2A8wYyxJ2FC1ELecLapKUOatdy4rS9LuVeXkQyhSY66j7tpBtAghTz5lBkv15sm-_ezKnb4RC1fW-pBnl6gXJM0y59hhw-Rw2R2WS7dIUwzaUBTpn9LYtZliqRsjPIyHx4yyI9DamtKQAJdL8VDumyZJISIE7Le48pJ-twBwFXDD92jTe8RIx2Z6Oso1VzX9UDibNpq9NWPHKCH7lSbO9-3nxUrdyZdPTYRX8hMixsXZSYOMKOUVBr_x4NpkX8yG2M5kho8nOnYEGcgH4KiNFEhX3B7XMJNPMGcod7syM6h5VpqFWXrcjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=UfkAELRgohFBhzgzN0aUUAhs15IT6V8y03jRWCZl3hsyXaaXEQ1kcSBEaEWEs0uPYAAkeOZ2y33R4ZGICugRGErWqB8vmtneQ6KE5vRobjstm8Zxs5E_WCcquiVA4LBf69e2Ud04h5PolYRp-tIdi6k96t_iNoMP4Bb0iyQDDC8dbK9-IYGPXtZG7WZoaPcrqZpbGooM3qTVGY6O2evLp0CLOXmA5Wm71Q30-5nRbgDKH45C1P8mfEMzxSXluWy9tKtzzZnc6aJAWGZcUvaUujV09YUJmDxcNzphVz-KsWLVvh3GciTwSXbIGsnurj378dekKHSoe7HYh6jjMu0KaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=UfkAELRgohFBhzgzN0aUUAhs15IT6V8y03jRWCZl3hsyXaaXEQ1kcSBEaEWEs0uPYAAkeOZ2y33R4ZGICugRGErWqB8vmtneQ6KE5vRobjstm8Zxs5E_WCcquiVA4LBf69e2Ud04h5PolYRp-tIdi6k96t_iNoMP4Bb0iyQDDC8dbK9-IYGPXtZG7WZoaPcrqZpbGooM3qTVGY6O2evLp0CLOXmA5Wm71Q30-5nRbgDKH45C1P8mfEMzxSXluWy9tKtzzZnc6aJAWGZcUvaUujV09YUJmDxcNzphVz-KsWLVvh3GciTwSXbIGsnurj378dekKHSoe7HYh6jjMu0KaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mog0b-4w8s1sUFdL18PQrLpp-LfNuhAfCbV4U759MXFSsh0uvKFSb9jrxrmkGJeEYTcVVcWkBp0l1rXstwnmzG_jM2IWf2YDQmVb9PlnbER8H-l7JeZ0dvojW6qnLU_SxaPd5kG0w4lalLuqWe3kdix1tqDRU4kcItWghhiPD_P7J1_cadFE1NA2jnhngOcNHv0e9da8R8H0yVhWgAGXSrWenyQP_pXnfttmHCuNdLTPldMxZNzuuNAbJze3AImS9GSpepfYJhjBjjWGkq0Griln46p1WLh_roFa1Ymf232xL6BBX77w-2CVpxQ71NOUQEQd6BhZLJ-L1I4_lR3-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ml7Sjr4L4gGn6HH4UK7PGPydqhP_zGxKdfE-RWtU65DF45YyGRNPfTNrE9XJ1DtwKjxYOT-86sQmNhJ5zoosZ_tux8vMFpOGSDrxIUiTKgzuNgjJx6BTS8PVJMq6hJL2ejvZyIn3TJYZoPW22OUVcEucxumReWYSgW8IsVnizJ_l8oNkrFCxs1lYakyJAx68o3A3vTy2Sx1SQZ_nkNMjwrvYNzIPLyO_oa7TYTSItgXRz4zvsEb26VkvIAH-eyvcFpn_i1oYxw5gl1oSRMk3-oR9oUuIxKs7W9SOdHSi0Uy-ldMJNTlO87MLb0PC4jyJF9qEZgzpSQsiDlCaQtfwgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmiJjDpJP9KHSBPgbSPTQZdHcivHVsP-hX5jCBNTpp1dgqJXLmvCzvQ9KwDbGWrZ3VbHZz3bFD_oay25N2FD8K97mgbCYRVdGTprWoLKrEe8cVmEq3ApowXvY2eBbUE18pn-L2eHS6D1TURo5kso0qrsYfhxcyFZB_IExeszFTw7zaAVrKzV0yYMGGn1reOmz-Mr6jb6S8pDMXXn7HiNBeOdGLmXQDFaihh55l1x4beqUbfDUzTdiJUbLQUpeKZWWy_6bZnyZEVqTlxeLfN9WjeouxBxyOmUv8XGUSZfr_JMXaKdOl0frEGHdNOoD_0LgfB7POAwp3t6Ft5d3ZbLoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=FRQ9WJbH4l-nQssAZjWrp3jgISeNmfcF-TDBeR6nqrNhZ2KNetNFZY_hCFt3Ch-iwoYGFlhF2bPwRd0AT7HOFB5mij6Kg2L2QzfUtZb4sVtXRtZUqzNA4qYLaVLWz7B8S4_fc198RRM_XgALqivjLXKpODurROCw6Uq9nul7n263AybAsc9Z0sK_7ICQTGaecLg_iNx6S2020ItkcGruQr5EUYoL9g8qe_xg1r_5MTmMWXmTSHM7DbAnoHIfSn0B-FlF35y_ObUDKxc9lv0Wz_d0t-FpMX_tanwJ6NRyQnxO6MiA7HMThiRWb4DdP7WWP2MxvGT5pjSZeDY5B7w0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=FRQ9WJbH4l-nQssAZjWrp3jgISeNmfcF-TDBeR6nqrNhZ2KNetNFZY_hCFt3Ch-iwoYGFlhF2bPwRd0AT7HOFB5mij6Kg2L2QzfUtZb4sVtXRtZUqzNA4qYLaVLWz7B8S4_fc198RRM_XgALqivjLXKpODurROCw6Uq9nul7n263AybAsc9Z0sK_7ICQTGaecLg_iNx6S2020ItkcGruQr5EUYoL9g8qe_xg1r_5MTmMWXmTSHM7DbAnoHIfSn0B-FlF35y_ObUDKxc9lv0Wz_d0t-FpMX_tanwJ6NRyQnxO6MiA7HMThiRWb4DdP7WWP2MxvGT5pjSZeDY5B7w0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFAHdGWsfA9XMjeJA8lceXm1L0tCM9VIRsaR5pscrneoP2k1htjRzzf37xWGsvC2_U6uiQT07ETclHn6fZgoaHC_r1mQ1l3EFDrLMjLJdV1sAvDskjbJqqyL_Ti7hDMI-xfsKLG0gLiNDmZogSPJDEx9D5z8nDsk_ugA9pP9a3yXo3dA3gx04kTwQXGiqwaGwnEkA3LenTisIa95ZRTtLowhXT66duaYYxbM9tQvM3oRMsSdLxJVLgwLN5NJ_YL-Xuy6ShZzrj_TGrJVjI-XZzoiVS8mB8sIACiFaXgGz5Emw12dBglRGJxHwZEXLw2VLEB1e7WIiLzD3NI9IY9PyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=tKu5Lda1eqsWcFs387BnJK9HN4rgal0aBC9galtySuVWmAuzdwNjqTHkAnk-qY3juQVm_-_eiAInMxydyxsNfkZx7YHZ9nlIjEmOiyC1tJwsTqiQK26mXvDJLwDImFP8m4uwiZufEjXAQKIKo4VLtM9FY-JhUhPWHC7KoszO-yaMj9evxILT59QRrX6KjyYgcFh-MPK8lgaCU2S36fy-TLCOGFZLv3VB4O7yXdu1reHtnfSdLvUE5vvWOpuh6fpyVfLjkh9bEzdNfWmEl8fq55_drF8v9JB0yKoOkXKHedP9eGYMNIhTl5bNZ1Jxbfu9M2HwJKSAKiGGJpe_E_0o_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=tKu5Lda1eqsWcFs387BnJK9HN4rgal0aBC9galtySuVWmAuzdwNjqTHkAnk-qY3juQVm_-_eiAInMxydyxsNfkZx7YHZ9nlIjEmOiyC1tJwsTqiQK26mXvDJLwDImFP8m4uwiZufEjXAQKIKo4VLtM9FY-JhUhPWHC7KoszO-yaMj9evxILT59QRrX6KjyYgcFh-MPK8lgaCU2S36fy-TLCOGFZLv3VB4O7yXdu1reHtnfSdLvUE5vvWOpuh6fpyVfLjkh9bEzdNfWmEl8fq55_drF8v9JB0yKoOkXKHedP9eGYMNIhTl5bNZ1Jxbfu9M2HwJKSAKiGGJpe_E_0o_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IKinqUZBqPPdrhPXhxiGqQRip_7ZSNsJSlN6Ms_h1Pa7gWhOrPpGzf2_HKrVFZNnBN40-pf0dEc2KaVZb2ViS67nbjn9OrA2XVzjLkEzHO-r5BhsCdrBMFfmm6Z7ze6FuJn1zKfFFix6bEXE1U16ZJAztbVJEZ2zPe3cL2HPyaNDFwQGIznZAOA89-tEmOEhWlObePO06oxTNC9HxKqq7qFocn2XpXqFh-RupGAisukFo5oBE3e36Zfi7ZwWQ50sghEgwSlhviH9bRCMZGYVeaUrXZE5UrAICKcabbQT8T7zt8iVQPsw_JjZrZWPUrNvFkY9XRm8FlVwPnCW7Gib8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=iH1_nkdnifbJvzZXLT8alUATWiTccfkOAVidC1FBH5V16knNJRMwdYIJ_U6oz_v2wOOgB9RZVoaYeUeTkvyChMJw1AMkrPMUCtEkLbRV-wDfD1d1wWcYFG0PJOZfJpmiprgOt0oK8GSCNOpaODQbGsjfNH2sdftTZN43Vy9GbaTXNp34-K3gMmyczwv3_0eqLDkmkUHBv-gbpQDPd27T86nhAcHLaZercShj41-bnRYAyHL98_1XKYlT6zwzH8GTTFY5l8CO0RV7y1rIPiI1lPJSW0MsiXzNl63GDz99hUQD9fdu9FVsMx0fL0cVyaptKGc9bl_1P8zc2ZqmTUG9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=iH1_nkdnifbJvzZXLT8alUATWiTccfkOAVidC1FBH5V16knNJRMwdYIJ_U6oz_v2wOOgB9RZVoaYeUeTkvyChMJw1AMkrPMUCtEkLbRV-wDfD1d1wWcYFG0PJOZfJpmiprgOt0oK8GSCNOpaODQbGsjfNH2sdftTZN43Vy9GbaTXNp34-K3gMmyczwv3_0eqLDkmkUHBv-gbpQDPd27T86nhAcHLaZercShj41-bnRYAyHL98_1XKYlT6zwzH8GTTFY5l8CO0RV7y1rIPiI1lPJSW0MsiXzNl63GDz99hUQD9fdu9FVsMx0fL0cVyaptKGc9bl_1P8zc2ZqmTUG9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJmNi8K0oGmlWwu40LL98WsHrTZhuB6KUTwZ2U3e9LitWa0AH-RiPHGh5xk2Vn0rupTp9Q7KKQ_AKZDeakwBL1SaUdt17J5PPwl1xwqlFPoNoU9lYNQ1u3YVcx06AkvEwcKdZrlRF9WTZHwc5t3PxfEWQea-Seb6uOQNGMpFR5sxlUlIiij0A8FBCr3HTD-AD1EZSSnkf4jgpgxIIdR3H4F3XXMGg6cUOqv1RMcSq2CGqlidvLxvtXs0Zj6HCDRa2HUsM_ktV9fYamfdUmI1KLg5j9-k-iu0nRSD-ozCYVs64gqvWoHnZecN0NckrnevVPOCvTUjM8fK6bbiZ7NOdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=nv9xRqS2k9TP14wWa4r9Hs_ACLkXqKISOjIIQW9iBtTzrr8zLN46QutsmhxNKMGVzcqwfSPJZUUbH8YwbUjbni6a6QQ-01_mnP1J_wxhqc4PoGfzWjPAZFioKZMTiA4op2bwtrMF9zNudu-3OXzHIesANWtqzj5WVbVin-2fPJay6c1AuvtKhZsMI65UcTVZomqhai_f78rV9dgp7sfUJaHM-893w-pmNOv4WJfmy39dneA6Bed0PqaQuDqHpfcIfqButfrM4XsZJPESWO7ouPqZV_6bQNOlpTdDPPH7k6Wxippap5_gLEaUkXhQPZHXoowL0lqqaJ16Gq5GxHavGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=nv9xRqS2k9TP14wWa4r9Hs_ACLkXqKISOjIIQW9iBtTzrr8zLN46QutsmhxNKMGVzcqwfSPJZUUbH8YwbUjbni6a6QQ-01_mnP1J_wxhqc4PoGfzWjPAZFioKZMTiA4op2bwtrMF9zNudu-3OXzHIesANWtqzj5WVbVin-2fPJay6c1AuvtKhZsMI65UcTVZomqhai_f78rV9dgp7sfUJaHM-893w-pmNOv4WJfmy39dneA6Bed0PqaQuDqHpfcIfqButfrM4XsZJPESWO7ouPqZV_6bQNOlpTdDPPH7k6Wxippap5_gLEaUkXhQPZHXoowL0lqqaJ16Gq5GxHavGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=o8U5bVwRRtJDRNCrbWE-MYEWFY_YhksetrMLn9Lx-5q4fK5MrvRyMDA25FZlgS382Vohm31KxRM0LwR6ukrgo4F6NJLegpi9NsfIJ6PthzCg2o1K5nh68Sq0gRz78qE_OZd6KbN0Hu5uN156q03CV5vtSoIoHSh0cwTNX2xjX0lMCk0aVd4zsgfoVjPxyORN3dC9AiG-BBbrcLIl79D4PNBmmk8jD_KQlzIwo_VTnt5LEcaXwmFmbVrosx6wqsXgdrRWyUJHYyJ6MgVwsiF0urjkKy5o2YiKMzRvh2xChv1R32k_1SPr5L3rOHeOIHo38AfKlvRy7IXjBlPxjlK-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=o8U5bVwRRtJDRNCrbWE-MYEWFY_YhksetrMLn9Lx-5q4fK5MrvRyMDA25FZlgS382Vohm31KxRM0LwR6ukrgo4F6NJLegpi9NsfIJ6PthzCg2o1K5nh68Sq0gRz78qE_OZd6KbN0Hu5uN156q03CV5vtSoIoHSh0cwTNX2xjX0lMCk0aVd4zsgfoVjPxyORN3dC9AiG-BBbrcLIl79D4PNBmmk8jD_KQlzIwo_VTnt5LEcaXwmFmbVrosx6wqsXgdrRWyUJHYyJ6MgVwsiF0urjkKy5o2YiKMzRvh2xChv1R32k_1SPr5L3rOHeOIHo38AfKlvRy7IXjBlPxjlK-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Br-SDrkzgAT2RHcraubULY1pdF1acy96EXSTiIRb3GWXVspRAsr5eQu02SzYwTVQjcb8NxsYCf5GE6XtyKb5M3DwFyFzvBoCHlCLbhuDN1rmfr-j2Ji1Yc7mLiu1VehINb-JgP2y2vIYh77Zq7XVqFZ9624IEWmY1dMFHLs_z4I9K_RFfpf8DwVGKqH0Ri0pfKkxZANF8fOUQfgqJnWg1m8fvShNobn961Y4B0wCcux8YAEf_7dCfaTVhMgnDct93iUKOa6548ONvc2-ZAXrSvX9Z5WazZEf4lHyBOQGvgRq-ozsy_b74dWwK-ukphbTqZ_B3ykNu6zbGY61OAqVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGzb8uy9r6_ZZ5rc82qoYpE21_9tYZmCgEKa0bv0OkBupsAD0YF_aEr0VwOGd9GZdK_LZCG5fVPVFnYl3lJNV1yc1qaTRpO6LDegPou96U7BBqlnnfZDEjm454GM1jjtuC3Ot8N1SNNnrEWivOaUsQTO5qjmfNaB3DbQanmV6ZFz6cUlGlPD2WyZC5UxoGfPCwg3_DR0xrNK2VJ86tCJDDjqfLAfTpn7zdRr9gmF4kDda6BNWMI7vboMuYImORnL_OvrJBKlzoZT1oa9k9HImLMDQyO15_mO1jgsXYwc9tv1TkWFJd-C3ybNoLm66W51t5PRh82Ji8NAO16XdVi_wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
