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
<img src="https://cdn4.telesco.pe/file/C6txvn9JkJnSBQm7zw2oyDdriv7RnqhI4NJJF7OctIE5w0hLwzjNSnM4-vGp-g2_cn-K5YX2cG-pSb_3H6g6BUx0jjtAM904zGX_V9b2zljUqEnkvbriRP8lPd3-oHja_iGeS_FUX51j1UYSbTLUjV5_lIvIs08DfcAej4btwslyj6QiJv8JYnIZmc-WPAN2quJ78aFwo2dLFof2cM9aLE8A0EPIxnPNAJGHzLAqk9cM5NIJgqO3GJM340h86q1f4jc_L0vzJ9-6Z5WRj3krroZ8wBYOaeB5k7qYZPmfaVva224aGUNbkbNcIFF26ZMVQ5S59wG7NouV33HGZGzxAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-447569">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3592dd4f.mp4?token=JTG6WrpjK41ejzbvfI5kc4VH-wmdFkFEEgOJhNMNphaBnhxjPkoR-Z2Wn7fyGybxQ2s9SaG_NPR0EOA9YYpQE3Gr62CGeZoCGMoUM1a9ahgYSd9V7AwwzmECdOETyGsuJHXz1-RcLgsontHz0dIoynTR7X20b9esRMqJQ0Nt0aL1aX3kwbH1UaMG08g7lmmvYRNG0yEZKMSAfBatmpAAI1rwGD_dznGOLLjOiz-H5IPWOa_T1wS_6G7Up0GXeLmkGVEH41DequBgX_Z8Mf2NAQQOp8fcATgwUdIV_DuYoY7ws-1mGB9ieNLlXMRNGckJamB_hdDsl79ztwyHM27AuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3592dd4f.mp4?token=JTG6WrpjK41ejzbvfI5kc4VH-wmdFkFEEgOJhNMNphaBnhxjPkoR-Z2Wn7fyGybxQ2s9SaG_NPR0EOA9YYpQE3Gr62CGeZoCGMoUM1a9ahgYSd9V7AwwzmECdOETyGsuJHXz1-RcLgsontHz0dIoynTR7X20b9esRMqJQ0Nt0aL1aX3kwbH1UaMG08g7lmmvYRNG0yEZKMSAfBatmpAAI1rwGD_dznGOLLjOiz-H5IPWOa_T1wS_6G7Up0GXeLmkGVEH41DequBgX_Z8Mf2NAQQOp8fcATgwUdIV_DuYoY7ws-1mGB9ieNLlXMRNGckJamB_hdDsl79ztwyHM27AuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای عاشقان رهبر شهید انقلاب در مراسم تشییع پیکر مطهر امام مجاهد شهید و شهدای خانواده ایشان در تهران
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/447569" target="_blank">📅 15:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447568">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72987d517.mp4?token=pbgHNXGmkvbcU9SoQey-CpV2K_QejH515PH9zpPPDIjTTqoe2P9fouQsP3hoj6j5k4KAJV3MEXh24u82Pn6zX86WMKjtBNaYR6ofA4gQ3pV_6f2fkC71utZanC1DMir0Gt3RuFvNVdabKSb6ESvVNver8bTI84ht8Ui9IGXvOkiBmX9i31wgEBa0bid_XlLMcq2G_8DMDW3Px-qOwKyyiei67K1s6VVR-earttk4okNNSEvqvzy_8t_EjRucG8-uJWZgJ2WpxZmt3SS-cK9kN0vxHFqc8hEvhSLneMrwBHQ3KeyVonXyRJF8gE1zTbKBCDYXBZsUIOhbpiFj_9kvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72987d517.mp4?token=pbgHNXGmkvbcU9SoQey-CpV2K_QejH515PH9zpPPDIjTTqoe2P9fouQsP3hoj6j5k4KAJV3MEXh24u82Pn6zX86WMKjtBNaYR6ofA4gQ3pV_6f2fkC71utZanC1DMir0Gt3RuFvNVdabKSb6ESvVNver8bTI84ht8Ui9IGXvOkiBmX9i31wgEBa0bid_XlLMcq2G_8DMDW3Px-qOwKyyiei67K1s6VVR-earttk4okNNSEvqvzy_8t_EjRucG8-uJWZgJ2WpxZmt3SS-cK9kN0vxHFqc8hEvhSLneMrwBHQ3KeyVonXyRJF8gE1zTbKBCDYXBZsUIOhbpiFj_9kvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از تشییع پیکر مطهر رهبر شهید انقلاب در میان مردم عزادار تهران
@Farsna</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/farsna/447568" target="_blank">📅 15:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447567">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b5032ec3.mp4?token=mojt3pBznKgJXIqZAD7WZRPvXKsgxwL74jOL6LwwsaqRGpTe81-efGDnvcehfJ_ubIAqYr_gNj8RoZL0xZbkelEOnieIsPbg-eO0Vhu9iQbGTOSckbvQ429kyLwVsR8487Qhfw3x77JtffFjzqUlLHCkAcAE6Mq-IEGTOzOcdl22MWxy43qUoLbtla5Hw8RoH3DE5WoiAeAuFIAUurgNNbZVQV2cmj6wNqXgmFI0DEmmt_4ajCxJVFq14KFzwOFkUB9sPMP6omZJcOUtuvH0mWhlTFMC0uc40ArWgmQ9cVSaEBVll_E6aIwGKkPNpPs4_QzAU4qhPKiWX8_MnOvHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b5032ec3.mp4?token=mojt3pBznKgJXIqZAD7WZRPvXKsgxwL74jOL6LwwsaqRGpTe81-efGDnvcehfJ_ubIAqYr_gNj8RoZL0xZbkelEOnieIsPbg-eO0Vhu9iQbGTOSckbvQ429kyLwVsR8487Qhfw3x77JtffFjzqUlLHCkAcAE6Mq-IEGTOzOcdl22MWxy43qUoLbtla5Hw8RoH3DE5WoiAeAuFIAUurgNNbZVQV2cmj6wNqXgmFI0DEmmt_4ajCxJVFq14KFzwOFkUB9sPMP6omZJcOUtuvH0mWhlTFMC0uc40ArWgmQ9cVSaEBVll_E6aIwGKkPNpPs4_QzAU4qhPKiWX8_MnOvHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سوال از حاضران در تشییع امروز: شغل‌تان چیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/farsna/447567" target="_blank">📅 15:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb_fIa5RhQ8eRMN_navnzjXBvw-bxy31zohRdKceVyJzxTZHeRR-aPETZVKDcizKApYf3bNnGWVhO0uKqLAxv2kHT-vL-U44IUk2K5iwnlRw9hQc1MBOByYUu73i_lMuSXBOJGX5s79sZtHOKCCEqtaadAzceuoUZRdQAkTW27KTlo-1EUenvuMG37AVYEgJKB0KpO8nQJVttPIODWjmOY-FGM4VoXiFjhrt_sXBNfbZti2vEgNpIphf4j02tJYonDFBGqN-9K41yGjRjL8SmBYCiuPWfO7Mo_3QjJ5yB3IoTh2tRj6OzZIxt6VSnHoTTCGdBQV8FzAjGHe2p7d-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور عراقچی در تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/farsna/447566" target="_blank">📅 15:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447565">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eff642341.mp4?token=ppDHVtoatzA0jhCQ9I9BVrPOpcoboBgIyPZwiNJAa3axb1ysvdXnRTF3Z3ZIzF0GbjmS-N05FcbkpHYQX6fYAaNsZllarqI3mjYVNslrfi3uDI6WmUYZHDu1YK2j_9kIKw1L2Fsjo7IagtrHaXG5uh7IwPuieGxErZbl_eREnW-7snx6d1VqAJtyCbDTy4blt5zej6GYlAZuVXWbF5gM1UfNwpHHyrw9BgiDD4ColnA9l78l0L34_SvTOedGnYOqxJrl1_njwWw5Lqrxtaj6oflxhtJiQqPxVjm7cDIcwUdX1YlBBbItxYnuxRup86O0HDr7OEdOgsKfiFmw7jBWCAE2Lwm2ycWXD61PxX4RYVf76AH56EqjGEEW4B8dFMRlTeQVpftF1hG0xX4DCUuPCI2uJ17spJa0wPkp2fDdoiClTba4aPxHz3d0tq3J46s3k1lNphqFZ4nE7lsymIJmSKEc-BClPedlwLhTASDsHgvM0JCSL2qqGi-Ib4_8sAJNKBTm0F9hG64kiHbdjH25FXTgbjzoSxiWz-Y-NdUlhvgo8cIPHHL61nV5neKKAUJWj9q_owdTORPnittMZ2dqaxrNdvTNoCKz_vo7g_1qO5avKV6FY-5gF09htMlmUiWx6zSREhU7OSeKkSuZIctYHgmT1qbgMyqnL6vi6GCBlWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eff642341.mp4?token=ppDHVtoatzA0jhCQ9I9BVrPOpcoboBgIyPZwiNJAa3axb1ysvdXnRTF3Z3ZIzF0GbjmS-N05FcbkpHYQX6fYAaNsZllarqI3mjYVNslrfi3uDI6WmUYZHDu1YK2j_9kIKw1L2Fsjo7IagtrHaXG5uh7IwPuieGxErZbl_eREnW-7snx6d1VqAJtyCbDTy4blt5zej6GYlAZuVXWbF5gM1UfNwpHHyrw9BgiDD4ColnA9l78l0L34_SvTOedGnYOqxJrl1_njwWw5Lqrxtaj6oflxhtJiQqPxVjm7cDIcwUdX1YlBBbItxYnuxRup86O0HDr7OEdOgsKfiFmw7jBWCAE2Lwm2ycWXD61PxX4RYVf76AH56EqjGEEW4B8dFMRlTeQVpftF1hG0xX4DCUuPCI2uJ17spJa0wPkp2fDdoiClTba4aPxHz3d0tq3J46s3k1lNphqFZ4nE7lsymIJmSKEc-BClPedlwLhTASDsHgvM0JCSL2qqGi-Ib4_8sAJNKBTm0F9hG64kiHbdjH25FXTgbjzoSxiWz-Y-NdUlhvgo8cIPHHL61nV5neKKAUJWj9q_owdTORPnittMZ2dqaxrNdvTNoCKz_vo7g_1qO5avKV6FY-5gF09htMlmUiWx6zSREhU7OSeKkSuZIctYHgmT1qbgMyqnL6vi6GCBlWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجف برخاست!
🔹
اهالی نجف برای آیین بدرقهٔ آقای شهید «جهان اسلام» آماده می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/447565" target="_blank">📅 15:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447564">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86330faad.mp4?token=Hhp6M_FVZHpGs-AyIMTeRW6C39irI6KjlQtpQjQ880RVSt7xhqUml26tm1q4nlzTKJqy7PMhZc54V7jfKFd05KbpgRHVgt4y_9jd_c4wqEazdIG9fKDKoiYvNbD7rumzNGi0APKP-pvCZcCxZmzqDyL04VmvTnmwQMhNC2FARLB5OECNdX1cTry1WTXqGz5ym0xI4lum882D9yWrv_9wfc44eWiIs8MLUgMS2THYNW05n2tQDH-No4DuS8Ppg0w6FWKl-kNpdaU6dmWDBHtxXhAVFKUYJQGZ-CvgTiXHosmbu-0H60pkGaqASt6rd88XyqhsChKzXyau6PLnHLeOKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86330faad.mp4?token=Hhp6M_FVZHpGs-AyIMTeRW6C39irI6KjlQtpQjQ880RVSt7xhqUml26tm1q4nlzTKJqy7PMhZc54V7jfKFd05KbpgRHVgt4y_9jd_c4wqEazdIG9fKDKoiYvNbD7rumzNGi0APKP-pvCZcCxZmzqDyL04VmvTnmwQMhNC2FARLB5OECNdX1cTry1WTXqGz5ym0xI4lum882D9yWrv_9wfc44eWiIs8MLUgMS2THYNW05n2tQDH-No4DuS8Ppg0w6FWKl-kNpdaU6dmWDBHtxXhAVFKUYJQGZ-CvgTiXHosmbu-0H60pkGaqASt6rd88XyqhsChKzXyau6PLnHLeOKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم بافت کرمان برای رهبر شهید انقلاب
@Fsana
-
Link</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/447564" target="_blank">📅 15:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447559">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPjRcfyHwi3rHWMHOhu935kIX9VUtpxUXvMqCnwF8CisI8HuofBp685JmQSSWvar_3X5dKaYDrmALXyj4DXUxbyD0l2Bl72GrPimt4Ko-UvcXANqW_zS0Kj5RQYiBq1i1rj-FCXwbh-1pnDswvKaT04Cie4zw5ie4lREyn3FpNYdjjpqOEvYWEOaFpDRHBCfM1uMvJily-mPT1BDqg8RmR2iu_bmVXm1HT2w3VntAqkLRBwtkQLcUh_Vcumqt1hpotErq5HanccACi5oWEKjxkKCvk9z4BxZFZloh_1oO-WqumNyeEbz6pXFEERdNbakCTwylkHw8NpAUaIfxKLSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axj43F6rN-Uaovv0hxl5Q68Kv-gximpAwqnH151jZk7_SK74DEZqpP-SfIRKBwIX9wFRsvIMEy_1KdMjc6IdaFqL3PdyUYmEHDPtNJcxLEwNqPq5RMesTJsb9mN6dYQWWs8KbnU4cjtO1a8v1hKcSZ3MFzG7oXzOcswsx05EhT1-7E-GomdSBnO1hDL58nSFowxevdhuqgAdYXDj0ozbj1UwpbbHop0tCzSVRKCnEQ8gZgnLFYVQw-9hYf-Hg3lmA-ND3kxZyf1qpWv-LJk_UeS7jZJAL0oy7FS_LE09atsju5pj6ZtjEROpULsnjtRN50nFjlcakk1ZCHIXDXbe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8JCESbCn_i0SCnNFGh7jyzAfmlnU1nofOv1POjixg1-HLyPvnwLulMYaXmcPYM4ERixtU8yV-gkn8I7Yw7D1LzurUkS8fqiT8HUuGdLQ9C-EE42UYhs5YCQ8Ddbzn6_wK4iatY67DoLwwqCmtnoImhlcYWmM0BUYqYWs3aJ1XAGqlPc-CDvKAMTeWt0GZnzqQMK8MLOyD7trWevgV-8TzQLhJafHq-VyVR7ic9jg6iaGhYAr6AbhA2u9cuAfQL7LOubFzlYOYgfpgF9yJJvfoau04PKIsUhpaAY6YGyk4prN3xWVofKxl5GFaHtEVgMNg6RxjfB6aZpp4PTPsDS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFUMPJrH43C2PZfaDluBLsDINs-6a0TFf4tTZeox9Tx9eCQcuLGQU6nRZ8p2ti_QdoYZBVhBRfMh9vQN3WGnlPy3kkkq0lkxJnoZ-fW2rc1RAfm7cE8eRhgPGCFb9McxIiFhMT8x2heIguv6rXMthRDAOmiOIA_QiA7kvwvTPjcVH6_HxjBNDtGDb2UEZwohqszB00B992aieqRi1q554ycEcTtY7lToQICA2O8dwSWicVYiQf5eyseUn9gaBdElBejZQe4PDbf6-TXWYDmYP4Idw06931w_bOhvTe8Cv9cJmdCfWG_qroe3Eb52Cok0OwtA8QJhpuBK7II2plQWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPxV6NP4TXYl6tgtOMn1b_ESXLHlhh_eYql7bHNGZNiSIg80G7Jjye3s-pNXIYdinVtXKkoMF6sNNn-VJqceYk0ypkj6dnugwCDvUuK0wVr5bKV7vLhZbzc6ShauhSrtiCxIi5KSb2ZBUIh1Xhn2TpVK0W0SzsFYXfH16RzInBFEkXtGZDe-57MJJ0eVVivWmSpZmsZ96XP1GhdNJ0rDyBd3ZhJ3IPWmi05kAGN9e7XaeIbJj-wTgACyHa1BXU2DGp-OpXaIWZJH5qwiPgphZoTS6tffzeIcCYKgbs7gMZ0FwefrVf2TKWwfd_lAOYmqGkJ204ZJpqiSk4r9CXbaAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیکر رهبر شهید در میان سیل انسان‌هایی که برای وداع آمده بودند
عکس: محمدمهدی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/447559" target="_blank">📅 15:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447558">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be8b66395.mp4?token=vaqDLJefvmfzj8FpFOy7fLS3dMLxTpg2i2hhmjlXSTo_6wGCLRDc9_LMiu1GXsG2v_Mi0WC3q2W_5LqpYEFPJ7QQWLE-05-KVrpDn1YJOyRG2CgRJt9kUlU5OLzBTupEA3AGU_loCVdQh0Usy30FJzvCJnkWXlLpR1wFNuk4NF3dM6wtw3InWNCI3lk9P2rDwcZGNTP-rYi-WW1vwdT0kaK0U-gzHTw56BJ_GlLnwBDTLIEuwq_wxa0GDq2VqRc-ubXl8FE4YsRKx9lrSFHLeNyPDoArIaYQJ0wMEGVWxVErxNOWVUoFZWi4dRshZY7PfbjuglwPlZJZnRjWbx860A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be8b66395.mp4?token=vaqDLJefvmfzj8FpFOy7fLS3dMLxTpg2i2hhmjlXSTo_6wGCLRDc9_LMiu1GXsG2v_Mi0WC3q2W_5LqpYEFPJ7QQWLE-05-KVrpDn1YJOyRG2CgRJt9kUlU5OLzBTupEA3AGU_loCVdQh0Usy30FJzvCJnkWXlLpR1wFNuk4NF3dM6wtw3InWNCI3lk9P2rDwcZGNTP-rYi-WW1vwdT0kaK0U-gzHTw56BJ_GlLnwBDTLIEuwq_wxa0GDq2VqRc-ubXl8FE4YsRKx9lrSFHLeNyPDoArIaYQJ0wMEGVWxVErxNOWVUoFZWi4dRshZY7PfbjuglwPlZJZnRjWbx860A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از رهبر شهیدم معذرت می‌خوام که به خاطر قضاوت دیگران از او دفاع نکردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/447558" target="_blank">📅 15:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447556">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Usbl27O78G3TX4evmz3QE_oHXC0PbMVarRYO8og5r53b8JNjwAKEuWZZISoeo7vJEh1D02jsN3Bnyfpnf0g9NgVePo5W3WcJEEJK8QZ53fYTTAKKcwRerQnfzivIoXyxJ9HEyj7l1A79R5o9lecO316WwAX3SD_OrbJkGkjWDXqhWDdt28tSCkeKhyQZx1MNcXqJNgYmoT9Gx-VSJ5QKmlw8xeH-sazZrhzGsEHZZSZzLUY5musgXYn3_ZUPt5ikCRBrtuxHSiB8_eXHbIGMP4vgxIdlUQyYbKO4ScayWMSe1WDAqbbpCEYQ5mcBhQ7FfOzNQrdzxb4D3cILoz4i9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVDEFzVwBAHCc7eqhclwd870ES4Dy8UsdxWUg4u8LuxpxBdRDqc1xkzpeK7JaDvKRM6rAJIiqphbOJVdNZbt5Uovpy5Vd3DrbBFjr73cVE0n9_29QghI0UEhcEc076CO_1xzcj3uvvYi_6MZgXtnTSh0w3Go-RSi96xC1eXnzU0Ge-AJ7afq2pCh2YB__r7KeH0EsQ-dJiEV6HhNAJjT5Z04vXw1ijbx7y948Pzc_eTO_S8jcgJcUIST2OpK2q1bjo385zhHMF8Y4bknAqSZDQgcQLjVUKM2RcThEmG9QhsbXmZWNRIyMeEk5_G6A1xvJkW2Dt_vVN8Xk-zXk9DUGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور دبیر شورای‌عالی امنیت ملی و وزیر ورزش در تشییع پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/447556" target="_blank">📅 15:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9930dc6d55.mp4?token=FQEWzcJkYR1v-N1GhZb-pcUUytqARUlsk8LOVV5IGSy46vcVbvvZl9ay7AfLR4287M7UrrbMjReBU5pOZ5HXMpRzWsz2OuJRluwpotM79Q0H8SpWD519HHUOssDgHZzFAXTi3rBzgpbA-nBaSNASEFEhstaaBRnniBC6glh9mqXKHzz7PvpVQGAHdYLrwhh9PHtenmX1l_R9A_Tv5UfN6fTuFLOuIT6NaDTRlEOgiFYXUA1hdf5NyYN3c4JGDFUP6wgULAhT4rqdcEYZasq2Di2p4TvkTxm_rsMlJu7vJYb90eibeOTBDVzFdYlcVAzXnohpcKceOctbu5TnjGWEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9930dc6d55.mp4?token=FQEWzcJkYR1v-N1GhZb-pcUUytqARUlsk8LOVV5IGSy46vcVbvvZl9ay7AfLR4287M7UrrbMjReBU5pOZ5HXMpRzWsz2OuJRluwpotM79Q0H8SpWD519HHUOssDgHZzFAXTi3rBzgpbA-nBaSNASEFEhstaaBRnniBC6glh9mqXKHzz7PvpVQGAHdYLrwhh9PHtenmX1l_R9A_Tv5UfN6fTuFLOuIT6NaDTRlEOgiFYXUA1hdf5NyYN3c4JGDFUP6wgULAhT4rqdcEYZasq2Di2p4TvkTxm_rsMlJu7vJYb90eibeOTBDVzFdYlcVAzXnohpcKceOctbu5TnjGWEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیژن عبدالکریمی: باید به این مردم و فرهنگ عظیم افتخار کرد و بدا به‌حال روشن‌فکرانی که از این مردم جدا هستند!
@Farsna</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/447555" target="_blank">📅 15:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447554">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wdb7B__alOP5nsY0IbW5uxHxReUe5mMoG7iZMzco-8RtbId1_0RnHBsVbHMBPajGtbTggUn8lmgMo6Xu6vFU-hkBjg0KX2FKo4rBGwYQrV1ueEHEUMf2-sr3BwZ3wNOH8-0hp_FomeP3EQKXfHkJ_UAovC-ySjY6s06jhCQy0vb-oRFZGG-cBL2Ca2ws3771uQAAV_7WqX5z3sfl5tJOzkPbgvZqukdhXewgHnXFUCithNe0B7DfXshMZclKfxy3qu3GFbwI4EGJi8gfCStH2yqZMBxHG1LxIbzGYSsLFuy70JK_z4KEtlFqbGD0jDaT-yP9jFxZg2EFBjhGr3lhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس اورژانس تهران: تا این لحظه هیچ موردی از فوت عزاداران گزارش نشده است
🔹
تا کنون ۲ مورد مصدومیت حاد ثبت شده که یکی از این موارد مربوط به بیماری با سابقهٔ زمینه‌ای قلبی بود و مورد دوم هم یک مادر باردار بود که عملیات انتقال او با بالگرد امدادی در حال انجام است.
🔹
تا کنون به ۷ هزار نفر از شرکت‌کنندگان مراسم تشییع خدمت‌رسانی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/447554" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447553">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f42a6017e.mp4?token=kzwSS3Zz-O3kD1kwb685s4boy-So9aydQQyMSKPobnYoDdlN1JlQgBqzkWok03g_PZen-UxhMINSBN9FGo7QCvI1sm-igCyucAYjInX9rBY5fcJ5B0fyhR4FgV7v02rg9CzFjofHpubtf-a4NF1EGLgwHkxKeXdMf1PKNbW4T2Tt4wxRF3K_hfPmYdm3fyRzygLJF6WhNaSY9VN0sC1m8qRL78IpVLxNiNkQxjOKV82BzFJXujDbsZd66e1IDX-Fd1kfrh3e3_Z2nKAqaiUH-EgQhwZ0SjojCufBbdCTRPL8BEJsy4ULDmwH_wMq8djmkLbp-yD7RfKt3iVGWYFFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f42a6017e.mp4?token=kzwSS3Zz-O3kD1kwb685s4boy-So9aydQQyMSKPobnYoDdlN1JlQgBqzkWok03g_PZen-UxhMINSBN9FGo7QCvI1sm-igCyucAYjInX9rBY5fcJ5B0fyhR4FgV7v02rg9CzFjofHpubtf-a4NF1EGLgwHkxKeXdMf1PKNbW4T2Tt4wxRF3K_hfPmYdm3fyRzygLJF6WhNaSY9VN0sC1m8qRL78IpVLxNiNkQxjOKV82BzFJXujDbsZd66e1IDX-Fd1kfrh3e3_Z2nKAqaiUH-EgQhwZ0SjojCufBbdCTRPL8BEJsy4ULDmwH_wMq8djmkLbp-yD7RfKt3iVGWYFFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «فرمانده کل قوا، لبیک سید مجتبی» در تشییع رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/447553" target="_blank">📅 15:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447552">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLE9XIfYQe4Hy57mTm2caf-1V1FYQag-jq5oqNTQj2rM8U0r5okwy4ZNc5Lf4VPxJFzhWFn4G_pRJcRpSwP0TmOAfHNd0SwYsplnKH-9BjfeYvTqGEqkDp00TTR5yz88x7OMmwZY8lTiE2hgjAveqNqM7xLGaa7Q-ZbJuKWRSogdGbH8FSxGqbiQ04qwdqQb7akluzoaAJFkWWJp2oQ0AkOa10Rh2Yba09Oz2vDgFivrEHMBQjgzqGvyd5EP3ArbKD6cd-vpymO6hYXtCke3rsgsPnGT24IE1Pw14kZbGf0DA8tZjymNBjgYQTAKrtcq5f9YoB1-Rj-V_H9dZciotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه شماره ۲ آستان قدس رضوی ویژهٔ مراسم تشییع و تدفین رهبر شهید انقلاب
🔹
آستان قدس رضوی با اولویت قطعی تداوم جریان زیارت و خدمت‌رسانی شایسته و ایمن به زائران عزیز، تمهیدات لازم را برای برگزاری شایسته مراسم تشییع و تدفین رهبر شهید انقلاب اسلامی و دیگر شهدای…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/447552" target="_blank">📅 15:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447551">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0e772f65.mp4?token=GBwwzc9Gf0tzUPkikmAVV7AyQbz_IyUJJfNBkAJgAaMM3T5genT04XB1aUDAno47W_UY96p4XVetUx7OP7NDdzSBSRa5uv6UdWLHzMWbXsqL0U0QqmqfUXdjm3qyYbOA4Icew7EcOX9IFYAFaVSLxWKh16TxWsg4jfuIbkbRowXWFpvtp1E5DnHXdZ9pL9oKA5r3KOkxZVCUSgvqq3LzUmS47UPEALo4Vq8B-cm6Ynryn-jDfZrlvvBDLmOz3-zms_FTVD4rzmETX2wgLjCcqwCZH2wnO0nF2ODgCJ4zhC1KxVAmDHVVVqOpRy78CMPqkLajqmRoFMWrJdezgnmLTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0e772f65.mp4?token=GBwwzc9Gf0tzUPkikmAVV7AyQbz_IyUJJfNBkAJgAaMM3T5genT04XB1aUDAno47W_UY96p4XVetUx7OP7NDdzSBSRa5uv6UdWLHzMWbXsqL0U0QqmqfUXdjm3qyYbOA4Icew7EcOX9IFYAFaVSLxWKh16TxWsg4jfuIbkbRowXWFpvtp1E5DnHXdZ9pL9oKA5r3KOkxZVCUSgvqq3LzUmS47UPEALo4Vq8B-cm6Ynryn-jDfZrlvvBDLmOz3-zms_FTVD4rzmETX2wgLjCcqwCZH2wnO0nF2ODgCJ4zhC1KxVAmDHVVVqOpRy78CMPqkLajqmRoFMWrJdezgnmLTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامزد ریاست جمهوری فرانسه: تمام دستاورد حملۀ غیرقانونی به ایران، تقویت نظام بود که اکنون از پرستیژ و اعتباری کاملاً بی‌سابقه در جهان برخوردار شده است چرا که ایران موفق شد نتانیاهو و ترامپ را به‌طور هم‌زمان شکست دهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/447551" target="_blank">📅 14:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447550">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmtooxl7mCS9SDP8dAyOJTiH5jlWOVD58yNOggiMob4J_PgXVGHJeCOIz69Xppzb1EJN2PVIos0tM-YkuqXi4tkliEVE3ioedHCDbPqXY_Vf6aqnEsBjq0AnDClEJM49XsYYmZM52ndd3rqdAc888C8i8M_MnSfegFmGQWU3YB8DYzNfc3D5RPXSeOj7M_YMtH8etW56oskmxoOQbXP-45C7Alv9rX52SLqgR_Ft9w1b7KxHboij52Kop8D4cN_VYPw9YGuOGap7W7T7iwFMrV8QdGIEuO0k9-TdtGVqQgCwJQLEVm8zFFQiTXyiI2WT_Lcc9GUqY6bj3YcpUx8K5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
۲ میلیون سفر با مترو در کمتر از ۲ ساعت
🔹
همزمان با آغاز مراسم تشییع رهبر شهید انقلاب، در کمتر از ۲ ساعت، یک میلیون و ۹۷۲ هزار و ۳۲۸ سفر با متروی تهران انجام شد.
🔸
به‌دلیل ازدحام جمعیت، ایستگاه‌های میدان انقلاب اسلامی، تئاتر شهر، دروازه دولت، فردوسی، امام…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/447550" target="_blank">📅 14:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447549">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45b42b1ec.mp4?token=L3uW3hb9PJhWbmPSpCeSIY-3w99gNVDbxrEsx41eGIAVeIZ9aLnolz7jqcYrV-EPb9LtrbnzKwSjVjtT5hRYpDtn2OvFSSu3xnYxFeYb5I0Y0AU0gXpGXIZ-GipcntteOEUy0EtCnuwZOpRvOXJU-JJs1-rELenwfJPObAr-wkEHqRJzzGUXwv6vhN5NRg4KoD5xOj29PEy0YQCzzvo6CJJ9c0cTWk2aYCG_7-FWOSFfP5klzZ3YkGkjVPU2-n3Aza7LszO7laDQjTWE6dbnccS5Am8mzPFup5Fn-gw4jmyFRdaeMb8bP3fb2fcN1fsQqX7IlFp4FyX05StxiyJNrzWygHumIIjd5_FbvaLbRcIHyFCQ2L-M9b5NBoWAolowqmXe8RENX8eJZHvEICvRH62XBcUBne7Wp_9zolgntasrgfLTSFwKbqsIqAdlPtaOa-vKmHPN_cx80cpRL6Wvqe5xhzjMRXjC_-MRqJNAEadMFam3N8vQ03aReqExEikE2VY086fYSsjpNNINgfyb8-C7TQEeXSX94IIPGxdeAM0ai94R216GycezO3_HUKbM7clo42BwmeML_6QpSQ_av7vXGB9Icatkk5mxil5TmDN_QRzeNvQBwFom_vh8FzsQH0zgMxAUk34L28HCgAJG2hMuCqv9fW74bYC16qHmRvY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45b42b1ec.mp4?token=L3uW3hb9PJhWbmPSpCeSIY-3w99gNVDbxrEsx41eGIAVeIZ9aLnolz7jqcYrV-EPb9LtrbnzKwSjVjtT5hRYpDtn2OvFSSu3xnYxFeYb5I0Y0AU0gXpGXIZ-GipcntteOEUy0EtCnuwZOpRvOXJU-JJs1-rELenwfJPObAr-wkEHqRJzzGUXwv6vhN5NRg4KoD5xOj29PEy0YQCzzvo6CJJ9c0cTWk2aYCG_7-FWOSFfP5klzZ3YkGkjVPU2-n3Aza7LszO7laDQjTWE6dbnccS5Am8mzPFup5Fn-gw4jmyFRdaeMb8bP3fb2fcN1fsQqX7IlFp4FyX05StxiyJNrzWygHumIIjd5_FbvaLbRcIHyFCQ2L-M9b5NBoWAolowqmXe8RENX8eJZHvEICvRH62XBcUBne7Wp_9zolgntasrgfLTSFwKbqsIqAdlPtaOa-vKmHPN_cx80cpRL6Wvqe5xhzjMRXjC_-MRqJNAEadMFam3N8vQ03aReqExEikE2VY086fYSsjpNNINgfyb8-C7TQEeXSX94IIPGxdeAM0ai94R216GycezO3_HUKbM7clo42BwmeML_6QpSQ_av7vXGB9Icatkk5mxil5TmDN_QRzeNvQBwFom_vh8FzsQH0zgMxAUk34L28HCgAJG2hMuCqv9fW74bYC16qHmRvY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقامات کشوری در تشییع قائد شهید امت
حضور یافتند
@Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/447549" target="_blank">📅 14:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447548">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e39c84c9.mp4?token=IUAL8Wcsspc4xg7WQg_1nffDGkcd1edGD0sUN8HJGVdzQyvIoc_UgnZt0i-eRWLADfAKO5nwcXiFyP9u-LlS2DCEo2MabWh1NvZhLBzKIY4lYcAi94aLPiaa2RGdLmZRz6Ne7z2jDbVl3nG7uCOJvUXUcvV-Py3hg8SrD5R0OoGmI6mnaS8ObT1mcFwRDF9QVNnrjYBftBXZIL-BMm-Tq4z26S9wlGbDCcQVHMUks2xy37lxJO8JvDdgjILkB05Ff9u4mpaFZoMxzfyABKrOEqDIGMuMMWX9jtaKJis9Qqwr6cBDx7k43vX2a39Rbb2I8CArjw_AiETcA3azxSKPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e39c84c9.mp4?token=IUAL8Wcsspc4xg7WQg_1nffDGkcd1edGD0sUN8HJGVdzQyvIoc_UgnZt0i-eRWLADfAKO5nwcXiFyP9u-LlS2DCEo2MabWh1NvZhLBzKIY4lYcAi94aLPiaa2RGdLmZRz6Ne7z2jDbVl3nG7uCOJvUXUcvV-Py3hg8SrD5R0OoGmI6mnaS8ObT1mcFwRDF9QVNnrjYBftBXZIL-BMm-Tq4z26S9wlGbDCcQVHMUks2xy37lxJO8JvDdgjILkB05Ff9u4mpaFZoMxzfyABKrOEqDIGMuMMWX9jtaKJis9Qqwr6cBDx7k43vX2a39Rbb2I8CArjw_AiETcA3azxSKPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی کشور: به امام شهید قول می‌دهیم راهش را ادامه دهیم
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/447548" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447547">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادارات هرمزگان سه‌شنبه تعطیل شد
🔹
استانداری هرمزگان: تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/447547" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447546">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12c6b29e1.mp4?token=ojNj-jZN-dKmRE-zyELmQ_AjliYPexs8yzHTQj-ZPssv5EpyB0NXmLO1XDy1PYdgLQF6RqEKwUn3YgzmFlh_SFgUgRAksaQSfR3BsjE2wI0FAcCvd-dmDEJM7o-vX8cGCJ5oz6JcE4b29EXd8NPP9xVw9P5JlKYAuxEVCnvvF32hcSyDjcWJknjoHPR5cxsL9zd6Ald40gmaq0GIVUDEq88RLdfiBp_-Npz0RfQZgVlVgFA7Leb4NffhqCxLLDuwXCvf5ZzgADA0M9DNLclwIZiGO6pWTJvw0A1uPMDwd_VWo8lcZhXjkU73DBHQDGFQDRD5zTdXkQOMwZXAQL-ccQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12c6b29e1.mp4?token=ojNj-jZN-dKmRE-zyELmQ_AjliYPexs8yzHTQj-ZPssv5EpyB0NXmLO1XDy1PYdgLQF6RqEKwUn3YgzmFlh_SFgUgRAksaQSfR3BsjE2wI0FAcCvd-dmDEJM7o-vX8cGCJ5oz6JcE4b29EXd8NPP9xVw9P5JlKYAuxEVCnvvF32hcSyDjcWJknjoHPR5cxsL9zd6Ald40gmaq0GIVUDEq88RLdfiBp_-Npz0RfQZgVlVgFA7Leb4NffhqCxLLDuwXCvf5ZzgADA0M9DNLclwIZiGO6pWTJvw0A1uPMDwd_VWo8lcZhXjkU73DBHQDGFQDRD5zTdXkQOMwZXAQL-ccQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آملی‌لاریجانی:
حضور مردم دفاع از راهبرد عظیم امام شهید برای ایستادگی در برابر استکبار است
.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/447546" target="_blank">📅 14:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447545">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d01a8dc9.mp4?token=IcJ5TIHzFOJpbQ-6SRqPXdJjiaY4Kd5W8tPomPs7qJfF3_HNBdEZSxI7VH8e3eIJOzkbh8qJbSBSc0Ts_sfiUrWQaLvbtDQ7mBO4zlDP8QBStZHFyJRV70QVA1We9W4fnahfjggLsvJ8tZLUcu6p0XzaLJTewgvKnmqyfykSnS-Swrbwnh2gLaE3_QnJSnkV1iOL8p_rOTjqdIYWAQPhKM20RigrnanzED0DN2j4lE8e5rtmA9Fp6EEKdTMq6FQy27-vxcMYcYYbg2rOzj5LxPt0bKpGhzdnyiheS_OEcVaISrNf58oef7FMIjPoA-oQ_wdDXQM7iMCH_LAxQUxceA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d01a8dc9.mp4?token=IcJ5TIHzFOJpbQ-6SRqPXdJjiaY4Kd5W8tPomPs7qJfF3_HNBdEZSxI7VH8e3eIJOzkbh8qJbSBSc0Ts_sfiUrWQaLvbtDQ7mBO4zlDP8QBStZHFyJRV70QVA1We9W4fnahfjggLsvJ8tZLUcu6p0XzaLJTewgvKnmqyfykSnS-Swrbwnh2gLaE3_QnJSnkV1iOL8p_rOTjqdIYWAQPhKM20RigrnanzED0DN2j4lE8e5rtmA9Fp6EEKdTMq6FQy27-vxcMYcYYbg2rOzj5LxPt0bKpGhzdnyiheS_OEcVaISrNf58oef7FMIjPoA-oQ_wdDXQM7iMCH_LAxQUxceA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک قول مردانه به پدر شهید ملت ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/447545" target="_blank">📅 14:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447544">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c94066dc0.mp4?token=dleJXtJnTrqW4RVaDyxEkPSLCRJh5bYfu-VMi2Ku0eYmv3_6q0guBe8vInUlUJw8NESuKtLocZNnxdXOgX-XxYugrS_zKU7MKMCpUaRZr5Pcw92R-1OaIy1R3rIxKwiBi6V7eP0SxPl-xNQZvHyv3ot4oF6C37Yn6_7mzlPBbp-VZ3nQL2VrZAlmq_5CTdpubLZ8NlOD_n9KZvjEzZUvqYR1FEv5KQCWRe4h94DIThCZxEO5MbvQAAv_1BrYCune4z4X1YxF4tdgWiM6eCIuCskcaroIowROR6kBYD74lTdf-mQfZ-kLyxFqYuGT9ObZDkkaJ-pSoYAZ4v-fPD8RGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c94066dc0.mp4?token=dleJXtJnTrqW4RVaDyxEkPSLCRJh5bYfu-VMi2Ku0eYmv3_6q0guBe8vInUlUJw8NESuKtLocZNnxdXOgX-XxYugrS_zKU7MKMCpUaRZr5Pcw92R-1OaIy1R3rIxKwiBi6V7eP0SxPl-xNQZvHyv3ot4oF6C37Yn6_7mzlPBbp-VZ3nQL2VrZAlmq_5CTdpubLZ8NlOD_n9KZvjEzZUvqYR1FEv5KQCWRe4h94DIThCZxEO5MbvQAAv_1BrYCune4z4X1YxF4tdgWiM6eCIuCskcaroIowROR6kBYD74lTdf-mQfZ-kLyxFqYuGT9ObZDkkaJ-pSoYAZ4v-fPD8RGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مردم انتقام می‌خواهند تا هیچ مجرمی به خود اجازه ندهد جنایات دیگری انجام دهد
.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/447544" target="_blank">📅 14:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447542">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da4fa8c0b.mp4?token=p430_wyZfevB8-VazVsvRJA6DjiLo4bQblPdeAxhTzR4mpd6egI0ANXTc-ouY9b4gjv4KiVfZqPqLGAs00vpDiwRmVbBb_niWkJgYPChMLRpxl_7wnCrehlFxKghdJddnKyh2CvZznD3NTLn3m0LXkhYhMzw9plDmgTYcrTb8uLi7WluaP2veV4uO2tbSdOJDJXwC7vOII3DMqM4B3wJbw1srODYuvK-OL0C7gOSMSm19g7mWu3zlfrza-jUf2_AarifrFVak-8DcffDkqlpCxYYOeWG4AEJQ85qCICazODxzOCDAG9Lb10NN_pPTAc2FUkm2kmVPKF2iW8eNZ0bW2P6FtJcIgInqXhpT4Nb9go7nUcIPl-RA2kiaqW1dTiRIwKKpwmhOCH_EZCo84KWXtFsQdfpfZRXVHv5utnkdKzVxRYSJhLOWo83Q_8g5j7AukERt79uH7a9gzFzpELdYDwUe1YwwWmc1eyPvjue4SfBtMIgYBUeCDP1LSvlgRoOWbrM81gwfJfMZtQQT2gg9xAh1xEq8hLemha5kQbb3HY-40nAOphqs7qQY5b3fXwxSiBM8RAPnpXt4VgclYY2iQIaWTqjC8c5skh5nRHFI2OJJB7Z3isZJhcPscaPohFwsXeTlsv6ub3L-8EBJQ9SonUKx4Fm6IzVV7HtTqsmJPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da4fa8c0b.mp4?token=p430_wyZfevB8-VazVsvRJA6DjiLo4bQblPdeAxhTzR4mpd6egI0ANXTc-ouY9b4gjv4KiVfZqPqLGAs00vpDiwRmVbBb_niWkJgYPChMLRpxl_7wnCrehlFxKghdJddnKyh2CvZznD3NTLn3m0LXkhYhMzw9plDmgTYcrTb8uLi7WluaP2veV4uO2tbSdOJDJXwC7vOII3DMqM4B3wJbw1srODYuvK-OL0C7gOSMSm19g7mWu3zlfrza-jUf2_AarifrFVak-8DcffDkqlpCxYYOeWG4AEJQ85qCICazODxzOCDAG9Lb10NN_pPTAc2FUkm2kmVPKF2iW8eNZ0bW2P6FtJcIgInqXhpT4Nb9go7nUcIPl-RA2kiaqW1dTiRIwKKpwmhOCH_EZCo84KWXtFsQdfpfZRXVHv5utnkdKzVxRYSJhLOWo83Q_8g5j7AukERt79uH7a9gzFzpELdYDwUe1YwwWmc1eyPvjue4SfBtMIgYBUeCDP1LSvlgRoOWbrM81gwfJfMZtQQT2gg9xAh1xEq8hLemha5kQbb3HY-40nAOphqs7qQY5b3fXwxSiBM8RAPnpXt4VgclYY2iQIaWTqjC8c5skh5nRHFI2OJJB7Z3isZJhcPscaPohFwsXeTlsv6ub3L-8EBJQ9SonUKx4Fm6IzVV7HtTqsmJPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بأمان‌الله یا شهیدالله
🔹
پیکر قائد شهید امت در آغوش مردم بدرقه می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/447542" target="_blank">📅 14:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447541">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c229deb0.mp4?token=CUue0ZXYvoLkO1GqkB1eZBnvvKxZgB2n6Wz83TG8HsrV1SFPhkrvpkTGb6QNoKKwlEDpztOgwqWvJ5oe2eWQraRA3GXllaxAAVRQct9G8z1S_Sn7Zxb4fmfeCmXzxnQUZwfHwVomoArmVmfz6_-cwwP9JfHf5Eoto3W76M5QXEEYZF5o2wGgOCYyr2g0W5zP3Lqc5DVZZuNE8lCN3qX70GqtU17xcBfAGuRLZnlShyf2nKQH3TT0Iks8pY8q-p45LnrY10XBeKaHbottR4oodu2ypYDmYakNXsW3E9DAwYumJMjvJerUemoxuzL-mYAPh2qUvukChj9YgLshZSkl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c229deb0.mp4?token=CUue0ZXYvoLkO1GqkB1eZBnvvKxZgB2n6Wz83TG8HsrV1SFPhkrvpkTGb6QNoKKwlEDpztOgwqWvJ5oe2eWQraRA3GXllaxAAVRQct9G8z1S_Sn7Zxb4fmfeCmXzxnQUZwfHwVomoArmVmfz6_-cwwP9JfHf5Eoto3W76M5QXEEYZF5o2wGgOCYyr2g0W5zP3Lqc5DVZZuNE8lCN3qX70GqtU17xcBfAGuRLZnlShyf2nKQH3TT0Iks8pY8q-p45LnrY10XBeKaHbottR4oodu2ypYDmYakNXsW3E9DAwYumJMjvJerUemoxuzL-mYAPh2qUvukChj9YgLshZSkl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تشییع تا ساعت ۱۷ ادامه خواهد داشت
🔸
تشییع را از میدان آزادی تا بزرگراه شهید لشکری ادامه می‌دهیم.
🔸
پیکر شهدا را باید تا قبل از اذان مغرب به قم ببریم. @Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/447541" target="_blank">📅 14:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447540">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FipU54wAfJhdOkXwWDbzezQ9t5i6R4GjFbuCdEaFho6q8tiWw7P3Nr39NwR9tObdvHG0X3e22vhr0dYKhD1Ys4cYaa0mxuadmtPS2u7TBbI3beU2Go7kaQavOFo0VMl1kf5ZRzfpnPe5GxSd7lPMi2H8neHQyU-2X5w_z6uO4ykzWu8x-yfnLW85oYJcI2LkeM88saVzCpfHTMbJHRAu5YpHMsd12WkGJw-gD5ArtLyaWRYW02uCE7w1DyjBpc1Gi95Eskv76RR0jitdfs0srYvKYfWWsCptR8ej9z2oT_oHvufuO1WWd5HE256K0SNQ2LhKUQDVqJ9M770aD2FA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور وحید شمسایی در تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/447540" target="_blank">📅 14:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447539">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba09cea50.mp4?token=bvSBrB2A-Dc3Vt3GKwMQXaskQkQdSHfzjQb8wLX6fZvjA8J5f48Sf3lYhPsZzkgj7Sq15P47ae3SEdMmPoobgliS8cx1VRn1SWO5TK3QugEp4nZ9leuoHckMuY7VDAhqwm67paj2mELLxE2-5xDxgo6EWZnV4Y7KmH2lOoN-iL1Jqo5a-2GskaGJnmNT14WpGbZj_JKVyZM2euQ7G3Q-xVlu4govt0WO5SzYr7yCpNBU8cP4YHt0ZslQRcsbQzY2_i2UbE-7uiPL0O092nV4aobgkXIDaH60SxAlZQJEeiVIo4aDxWupFMb3XjHGkMh35mlk2OKwX1lNovTEQM-SZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba09cea50.mp4?token=bvSBrB2A-Dc3Vt3GKwMQXaskQkQdSHfzjQb8wLX6fZvjA8J5f48Sf3lYhPsZzkgj7Sq15P47ae3SEdMmPoobgliS8cx1VRn1SWO5TK3QugEp4nZ9leuoHckMuY7VDAhqwm67paj2mELLxE2-5xDxgo6EWZnV4Y7KmH2lOoN-iL1Jqo5a-2GskaGJnmNT14WpGbZj_JKVyZM2euQ7G3Q-xVlu4govt0WO5SzYr7yCpNBU8cP4YHt0ZslQRcsbQzY2_i2UbE-7uiPL0O092nV4aobgkXIDaH60SxAlZQJEeiVIo4aDxWupFMb3XjHGkMh35mlk2OKwX1lNovTEQM-SZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم همچنان درحال حرکت به‌سمت مراسم تشییع رهبر شهید هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/447539" target="_blank">📅 14:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447538">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fe6b200b.mp4?token=bZO6ZSpGY2SqvX-f69aqkDrkS-EYrx3e6X9obGnFl97UQThe2QmChgn1IQ4TDHDmmI9d3iMzXlvO4NzdC9jQU8A81d6qmsnmSiY3yypxjhmT1-WBnZwZCrcC5ELFx6X7PXy_jLlpCQ-tbfjQ7KHysNxcyyB-2EYQ2wKR1FMWeGuGvVOuIdXR7kBtGLEBUemaJHKhXMIVxzvennJJfGl_U0GR8Y5Ta4pwreHgAKCz-axwF_kNVFmI73oy4jyvavwVDY2IZfhWQBU0BIw8JNgbqA5bnzDFhX6MPK4uUFPW_2sL8Oz2YRUm94Dnw2fEX-oGmnQFwivEJPM2MvIqDIeJKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fe6b200b.mp4?token=bZO6ZSpGY2SqvX-f69aqkDrkS-EYrx3e6X9obGnFl97UQThe2QmChgn1IQ4TDHDmmI9d3iMzXlvO4NzdC9jQU8A81d6qmsnmSiY3yypxjhmT1-WBnZwZCrcC5ELFx6X7PXy_jLlpCQ-tbfjQ7KHysNxcyyB-2EYQ2wKR1FMWeGuGvVOuIdXR7kBtGLEBUemaJHKhXMIVxzvennJJfGl_U0GR8Y5Ta4pwreHgAKCz-axwF_kNVFmI73oy4jyvavwVDY2IZfhWQBU0BIw8JNgbqA5bnzDFhX6MPK4uUFPW_2sL8Oz2YRUm94Dnw2fEX-oGmnQFwivEJPM2MvIqDIeJKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از لرستان برای وداع با آقا آمده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/447538" target="_blank">📅 14:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447537">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I88hbPVaYimuxA4nF0AJ3fCF3mA5Ehkt40vPjiISDQEVuf_k7f3Y8vTnW0lZ0UVmNoKHniLenjiG_pM5k-EndbhOLyx1pXY9HJqEKI8T4k7g3V6w4ril8UyVZtU7tjbhlqDxpksjfEq9fo73afo0EYzIE7TzKE7Krg_pKxseZqEBSTsn379BG2QwNGztAkWuOel0TCD7mMUNkpxLqt6nasvtcTbWZAlRiOnojXGbK4m2a_PIoBysbgGN0cPk06TVMy4wnVmocJ3hRlcTKzYK3RvVphc3wTazisgR1jPq4XNZ8QGKOEUhVdnBosIHw4OlxAyL5AOBROcQAPhnXUqmew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله نوری همدانی: عاملان قتل رهبری بدانند قصاص آنان قطعی است
🔹
شاید امروز برای بسیاری از افراد هنوز به‌درستی روشن نباشد که چه شخصیت ممتاز و بزرگی را از دست داده‌ایم.
🔹
در این چند روز، همهٔ دنیا از عظمت حضور مردم متحیر شد و ان‌شاء‌الله در روزهای آینده نیز این حضور گسترده‌تر خواهد شد.
🔹
دشمنان بدانند که این حضور حماسی، تنها بخشی از ارادتمندان ایشان را نشان می‌دهد و این مرد الهی در سراسر جهان علاقه‌مندان و دلبستگان فراوانی دارد.
🔹
این ملت هیچ وقت ظلم‌پذیر نخواهد شد. یعنی فرهنگ دینی ما اجازه نمی‌دهد با ظالم و استکبار همراه باشیم. عاملان این جنایت بدانند که قصاص آنان قطعی است.
🔹
مسئولان قدر این مردم را بدانند و با حفظ وحدت و همبستگی، برای حل مشکلات کشور تلاش کنند و از رکن رکین ولایت فقیه حراست و صیانت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/447537" target="_blank">📅 14:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDZVOjFwD2dc0Jz25evoJqzx3eqlaApELBpnfAStHDa0hWMys83z6jj3rqOsXGPflAa3KibqsPzAGHoWIhBhsAelUgyx130LUtF1n1T7ZQNiqNzmQ4zsd2CUVYrP7ETju5C9_bJqwJKB7Y87YFkbxGkvETgHBjXS4dfHsj7xNPCoj61XxShk8I5UEM32jS40oOO8gFN2bkoWJLUvIjJEbU3pc79E6y3WkiUVT7JIPPyElHMTSG3Sg-jBczjD8HN_VkHCJfvbc6Wd-SjVY-LJL5dDbIK9MyuzDF73QuecStEaCV5BUo9SZs5KwLhvn_RzPbPEPYCFjDQQsGZXy4GlZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEX3kBXe45DauowMJ9xXyk05KgwXXlFCCReTLA9NfvekkL4SyutFOlEiL9dnQBfG0t_LuSzLYSinAkpaqdH4AQSvzh06tStV1u1XMaC-Y3WlaqjHkD_MCrpBoJUwIXWpPsstxj9uSGwn8QhoenD39g7AsA_ZI8uc5h_mchOUch1hQ1ZEoqVu_5GtDcNTJ5b1Dj56mSCnmQ5nM17cWgYs0_J9gff3_na1R7hciQUJfKniq71A1BUsd_tadQu-WazycA3X74BkazKRIF3P89uUOqjBRAk7krKwuBtQvB8IPE1nImrMMSeO2IM986QXWd3X9j33FVquFEbdrgi5FGqEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZ4aKhO-_p3NU3WQIdtbRxL0gUCClw4mQnwFICqsfPC2Vj4t5oN0Efp5vj2wS8AkDgCyqBRBGDjgEaN3IvG1aqNv2lBhBOI1Blv5XhJoGIoFrmDrTEMVhWTykIjuS8clEXCufXsgnF0UGk2qi8AxRXBiJ2_9RXv6V3P7VAb54jgpnoACBVlhwatkIYD8c9Z-KSTJ-dazFARXsr8gNsInOdD0NqCySUGtrXJfP6SmXHZiKV8ulGbdVYN0HudDnluyYLMp6Xusf1o5lEsXPXIH1HMNvPDV-6CzPfvg7_hc6MT5ajljsLIBnOI-gipZZ709X1a-jrlg4Nft88Mv2K0f0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1pt3UjVx6ytude8wOvh32oGz5yrIMELHeTy5WoCl6m_QnZHNw6Z5ZNW7IL8V4Jv99lzPFDOivKTKyxF7PmtFGjO4juISDIhoTmvORWQrk2jDVTDXfQ2HJz8pH_auWPY7r4w-p1QK0yGwZDFt-1ymqt-hX5pzUxpPpAU8dfxwc9rG5erIRarBFjalbK7ShHtYXed8RgnWo6NzORb7tmVz8ebrPBOVS4avnPs5KQYaBJx6cD80A3bGVjAltf6mVC6fHIJncXcpoVdcLeBZZEb1jLpzfjOD93XsS7UZ9twoqKBoQmeGOkjFcPDELTe-9pQxano-KJ9uYVAs2GU8hKpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cAXPvsZk7ToJY7tyaWIHuc3WLpHl-SOGOFzgMaFZGJrJ6eT3zSvGUmo8u4a_wbQiEuFLEmXl-ASXgeB3iTjPU9E7M6zNQh1ZwFJXiF6dL5XPum5-8ELkShvb0VWoW5FMVm5e2HYW8sXSu1VDQR4jWOs3c58C8Tj4wuwlOOtwAs00EEx_ZWhK47cuq9OTvj_cTRNcSRah2ghWpgppNyHozzP7-YXC0mZjBdvuEc78jDIJR67J8sekbDbPdTDBiSUhgvK_YtyNny1oDm7bNzJfXEeYrmkz5xc95DtShoVvSKoQsvRC7KqUh0SVEgfE6a9M4Rd4eDO1C-kbRvLlqUi-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o4TP0-PRPqiXwjQIs-9uoIu7MeDYFNA5UnHvEUVv1GrJjvUq0rwyibDUHoPBYvhFeGMptXAAlnJ2fbx2mKX9mv7cXkf_3kUKTmai_Cg-V9-yWV50Kk0POsc7TXmlSK-OZCv645Vvpkj0DfLXXHShl2zAQ8sKBKzmJ6xMDWGfv-TwTfnGuU7R_UEdP553pY3qaxVTLlYsb339HLvG8Hs5A1B0nBjiBxxeToFXl9l1X8um_eEPdGTGAv1PrbaXY2yRF8bZy-b7vR4rvkjo67x06lVBYEe3WZl0dakGXVUmYhMrkR9tGWm6vJMLZzGsA05BgRhvreIcTsUWYAfUIIrNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-JEVn60pMHPQjaqbt0tAdgYuTjSPcvhTzuldHQpA7AhS21-yCwDqQBa5NUJqBCwcuJ3of_-XwbVqo076HlxaJYH4q-VzO3eshWWgPLPxwAemuqV7WQ4nM-pBSi0G6MwQDf0py1oKhJ1mT9byu88_lStqXJr5TbqEajTdjhHawmHeIlgElTsLlkGNMMkp0OgXNMuETatd6-hEStBIYhgOfwe4B_sFOBv44wttHrr22OVyeaf7FCH61ClLXoehvIh05xJkvhBesy36TVkNyFNtUtIzG7RlwPJf1f-CkWf4xZgTTAeJyQIl62EJg4HKN9OJt1AOOZqhGQL8SRKdcusKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCF8r7PZgvzKBlUYxh6o_peImxsmGLmgVtvGrqo_6e0LA5DCJQ47QWh7tfE2hgLVSSLD-X3IT-N3mWmt6k8Uf5bDg_RlktaOj2VxkKeRXe3GXUj0k4Zn86J9upyKAWlYqLxRGbErYySESHAZe6QhwoQGp2O7OycdH5kl69Q56zDU7mhQd8TKmBv7DEr4nqLRsXp-VTIJ6bhmesJZ0FviwsuehMY-Xb_H6QLOpqjBuIQQFoxJZEJnHBxZTLCNuWUC5Y80RtUqZs8-tryQBk-3W-XEZllDmBIH-dub-Vb2-WdNlH6qIAi9BUseu_nNuOAyEPHaegCX4T3Simy5Wtk9DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر رهبر شهید انقلاب در حلقهٔ قلوب عزادار مردم
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/447529" target="_blank">📅 13:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40467efade.mp4?token=Rmy4C3nDWtM95LPLIUaG4Rc2ISrC7wR1Qh0LW9tpMZBiRNBvsqztapUI-qWcu6S9U2lZEieQfaAKpD0X6kTfmArbH-TrUh5lYLGVAzSs1Wibsw_7HkXuewtzww_YwrCcCyEeNlBTaPLaH5Arswh2dqqxtquPgjNnlX4wTelisyGIaskphwa-bBLg7Xg3Wk1ma3pAur3N9u49GDZi2bzaIDsx6SSHQhVfKUZ_MBSkI0kBcNh9kuz506nSrZm7NieNKUTMlJyzzAVqF9t5KbsFZ1W9Wp1ZBGRZSuA1ZWL0YhaMlRVRnirw_gLbetDV7PbVUFcKA2OK5zJ8TJfzyPGjcAvC_WRistQt_lx44zOU43ldKlHu9iuh7tBix4viqIZEorlR6A04Qf2SHS6ri0AatG0h-mqUYu01esOkgxmk0PRHuwKLB4rRKg3shRwtnBoHuCzo_hbQufrVZUbKSM64XCqkZRRgDan9sI-saGkoQv_8TSpERxuf_aArDTYpnN0XJ86ypvvvDYId0ig-sihAGaF1FVQ7r9I5714I2xn2ZvrzsTyDu6LWQQJkkjaIcJuSj1RVdngfz9NirUcUvVFI4V5trYhBe-myRgjTNICtmmLBlvf5-5AqiP6Oebtenh6T6RrUZUfLCYLOTW6iQPdAaXZ0erXb7z1IP9_RIp2eKa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40467efade.mp4?token=Rmy4C3nDWtM95LPLIUaG4Rc2ISrC7wR1Qh0LW9tpMZBiRNBvsqztapUI-qWcu6S9U2lZEieQfaAKpD0X6kTfmArbH-TrUh5lYLGVAzSs1Wibsw_7HkXuewtzww_YwrCcCyEeNlBTaPLaH5Arswh2dqqxtquPgjNnlX4wTelisyGIaskphwa-bBLg7Xg3Wk1ma3pAur3N9u49GDZi2bzaIDsx6SSHQhVfKUZ_MBSkI0kBcNh9kuz506nSrZm7NieNKUTMlJyzzAVqF9t5KbsFZ1W9Wp1ZBGRZSuA1ZWL0YhaMlRVRnirw_gLbetDV7PbVUFcKA2OK5zJ8TJfzyPGjcAvC_WRistQt_lx44zOU43ldKlHu9iuh7tBix4viqIZEorlR6A04Qf2SHS6ri0AatG0h-mqUYu01esOkgxmk0PRHuwKLB4rRKg3shRwtnBoHuCzo_hbQufrVZUbKSM64XCqkZRRgDan9sI-saGkoQv_8TSpERxuf_aArDTYpnN0XJ86ypvvvDYId0ig-sihAGaF1FVQ7r9I5714I2xn2ZvrzsTyDu6LWQQJkkjaIcJuSj1RVdngfz9NirUcUvVFI4V5trYhBe-myRgjTNICtmmLBlvf5-5AqiP6Oebtenh6T6RrUZUfLCYLOTW6iQPdAaXZ0erXb7z1IP9_RIp2eKa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تلاشمان این بود خودروی حامل پیکر شهدا را در خیابان انقلاب در مسیر تشییع قرار دهیم اما به‌دلیل ازدحام زیاد نتوانستیم خودرو را برسانیم و به‌همین‌دلیل از مردمی که در شرق تهران آماده بودند عذرخواهی کردیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/447528" target="_blank">📅 13:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08e7fee0e.mp4?token=YDJFZoHMZuC3ZX8G9EycrKETlcRxs600UYcULmLmDgWzVM_pXhPnXmqW-Tl2v8_CW__Ar9TD1CnriXY-8DkWO5DrsRgD2wciINCFpjESs3O9GCFJ0saJeQMsvBg-2hjqJaSDSv94hEV0loKCWb99OQIvOZII4Lx7tp_W12AhJMTJIU2ajz9sqcjT5wBJbx_D5xrhDtcpd_we7aTrA0_a5Mua-naTW3VcHC7zfJvH8YRqycXPU7zPRAxUmYksw_RIKap3NxIBZT4RQRIJ4q8bHsgFy2TF4ztFNNkv7n8GY4ku2LvUwHWAALava1wdxFAcTnRw74mrhGyjjqRAj38S2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08e7fee0e.mp4?token=YDJFZoHMZuC3ZX8G9EycrKETlcRxs600UYcULmLmDgWzVM_pXhPnXmqW-Tl2v8_CW__Ar9TD1CnriXY-8DkWO5DrsRgD2wciINCFpjESs3O9GCFJ0saJeQMsvBg-2hjqJaSDSv94hEV0loKCWb99OQIvOZII4Lx7tp_W12AhJMTJIU2ajz9sqcjT5wBJbx_D5xrhDtcpd_we7aTrA0_a5Mua-naTW3VcHC7zfJvH8YRqycXPU7zPRAxUmYksw_RIKap3NxIBZT4RQRIJ4q8bHsgFy2TF4ztFNNkv7n8GY4ku2LvUwHWAALava1wdxFAcTnRw74mrhGyjjqRAj38S2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری دیدنی از تابوت شهدا در کنار میدان آزادی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/447527" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQirUXhqGDc9QyJmYipyck44gB1pe0HHvJ6sqkMIdKsU5ZtaRKm1ARmMSXJ5RU2yOEzswIcmElLSXKzAzdzNeMmxTspavWR4-tyeyqpRUqY5Ox2wlMV8dTTpQwSFy6Kf5cXB1TWAoW8Yuv1jjPVQY4comd7ZyuvDFBbYJiwnedpCBCbmVu5gxcZdxN1WhaSgDQQ-2pGCqbwDOc1ToVfbI8oJSjp8gZyPcaoEii2KsZ-tbparUlQeSP0EUTdWcn80tkJXkd2exNj3UMU-UCxUCkP1DN9RKXAO-B4ykCnfJxRJOEm1EoLqb9duVtufHvw2WoF009FkXhg8pKUFrkzSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTJluGgl0puxWJs9syGjr0dKoPCGW9lcjWGuA-k-aiZU-XVCLlRHC0mqEI-V2LqSyb6eOUWvRA7w7jYL6k5UQvboItSB58vMIVuA6PnCmlYM5L1bj2OcPNx7SPIBj8T7pMvkklCzy_jkI5J1JTO3Ml6NvZ04X7159P_Tq4lQ8yrvSsASj-FXiNgVa83Bdu5aft-DKkfmKCdHPcCIcaUL8e4No6DSSyoPM4YqTziM0Pp8OLI1X6ZdpKf3Dyh2iloqPfcuJxYwsoM55u_P1n75eq7u4gn0g75NXcahkoJS5ujkmy5kHhd5ju2iWgpWZWrQjkIE8IgkXuv0FTQGTd0EcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dsy5oXnsP3ICCPRyFokRpCRWpVNoTd5p8DjPH8JF7cyYHh2VEUavDRpZlEacXBUet8CLhlMQCWihwVHnaYIWUYUgOf6eNknnIuUg65VChZbdXiFAfX06ZDGPgtwQe-2IMT6mrCo4x-d2MaTWuOJcVIEuH0qPgNWZ-xEfk0NFUl9KYR1ri_Wwr4EXtJ_VOGRljnN55CslNCSnuLyIQnFr6jF0PArYXR5gvoFh4-e36xgxX63jyh5fmA1EbU1h9vQgcUClmEANwlE8wzrCvETrPj3uC66ilNntq_uUV2-1VXrRtMANt-LQy5KjGfnnAW6HkLq_Ml86-sI6zXsW95MKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3KTmz_E50JZpjbPIUg66HB_RzNx3BNUJh-HF-eSX1zMJJSHzpII5epm4ASI6FK_2une5u_5DZFwSzfn-z8rLuEPay-a_VrZwBAU1ZRrcq3LnazKq8hRopF4s0kMQbRmopH_P8dT58uTmV6qMTke1DoIhY_qfX62PT34gcYQ10fxnb8HmFlTWCkvX2OaUQMIvFwsjjtkTDmR59YDesD_6fsvYceZRuRIcoogXHNOKVYef8U3YYQ2-jwbrIwn_TAwcqQVfGXoEMupeton2A8iPJTdlU33o5dr0B0_wvJJF9Dm15SrZVKC-I8CQrn6blKIcB4BEDyNCvLLrQHk9UKb7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cw4nKq4r3wAzzuMNdptdqk6dsGSIQYrakeEFrpcPm-1zIbiF74IBhkg4w41HdF0gdkxXT3AdOx0Elo7U1_TGDVLE7JMbjlUVkFeWOrN1mk0ipegsGzkN_1f0wfiapbhY1KyLDCRRa_OeC5-kjPG2RRsU6QDd1xocAJcXTnac-IWWerJq-WXysCKb3XEyYjr895htCOt1jQomC8uSE7yiUKFEwjXVKCWDg8SRpeLdZ7BhC6XbDF8UUNDkIkFySG1yCeZc_eazq2XnZIUGbOPChuYrUGLk8G1hMTzjkpbeNOPjOvmyjYvcO95ohq3x59NyZUrzFui-4F_bBroB6vMy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6ccHzKt1nZAWQ9XYhBJorc33bfCji4wq12jQrIT0mJTj_9uA1e4li9eztwS2rpTBzblyflXGxxdvhIMA6OhymKMbsUdGyt56BM7F0rrrOU2wzFycjF4uSKqgMiGchgwsOnOg1n4QhJUk6Wr11O1biyHBqvRu6xVQ37S0towTobv0dGrVaDJpXA64zeg2Tkh6cJT7uY9YUMxzyTdGpueEzE3SyTzqwiRpqkV735e_5pJ0styzNfbx5-lWf71ztBLu7-mgCvTVtJOCLy0G-r7s4wQ72kgVQAmj0tY70bKuiEbva69GO3KHBWUr124pTFLi8uyHLoXQvfKOnPbLFDEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1M81TzuipM5eEU787xP9hhSw6m0a5lQJ5RjdkSA9yeNfA8F2-6P0hO6HycYSf9Bh39pB8QY2ca8He2T_spi9VU6gHmcpTgmSlLdVHCpUH_ZOpjVj5XGdqMS7rrLlSjBDUFAjHb7Gsr6T1J_RC7oES7dHIBNdu305DE4Y_s3W1c62Z3O1YqhOOv-ezbGs2IewjN8x1P1K_6wwma1gckf0B3pyStEr5omjwrwSezAO8heGUpL9ZpQcTKB2DkGe3elo4OKkxVEyzwaD5lGEOBBN4a_AzA2ut-cvTjjCxI5d6q7Q3w6T59c2d5My5oi_EEN3Cg3jOhspBUXacciA-0Xnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تئاتر شهر مملو از جمعیت بدرقه‌کنندگان قائد شهید
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/447520" target="_blank">📅 13:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1839d04a.mp4?token=J9-XYFYSTqmUUl0Kt3Wy9PSr6bwL_rox_BOhkz64MddXsW_f15x778RHLm7sdzMkFYrdbDBM2tcYHI1K42oXb4b46DVFzdSUmVWMSsMiiYkGeyZ2vyoBQjO5EHU8VmPr0G1JLnx2E86BTH2R6gbZjIPOt06Szmt8eA5z9JpiUHJUVCARA_GErRndWPJW9DVIoJDk5iC98d6cmjTx1OcdaKYghqKCRQkNbu6V7YhrWZbjeoqI_7GmgxhfC4fmsrVVIyv2wN5h5PgVEjWlw0czyvyJjadHnrtRqc3v2d51q6tHTxKjtpkDgujYrNs6AufR0dME9ORPZ0cHm2vC3CYleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1839d04a.mp4?token=J9-XYFYSTqmUUl0Kt3Wy9PSr6bwL_rox_BOhkz64MddXsW_f15x778RHLm7sdzMkFYrdbDBM2tcYHI1K42oXb4b46DVFzdSUmVWMSsMiiYkGeyZ2vyoBQjO5EHU8VmPr0G1JLnx2E86BTH2R6gbZjIPOt06Szmt8eA5z9JpiUHJUVCARA_GErRndWPJW9DVIoJDk5iC98d6cmjTx1OcdaKYghqKCRQkNbu6V7YhrWZbjeoqI_7GmgxhfC4fmsrVVIyv2wN5h5PgVEjWlw0czyvyJjadHnrtRqc3v2d51q6tHTxKjtpkDgujYrNs6AufR0dME9ORPZ0cHm2vC3CYleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تلاشمان این بود خودروی حامل پیکر شهدا را در خیابان انقلاب در مسیر تشییع قرار دهیم اما به‌دلیل ازدحام زیاد نتوانستیم خودرو را برسانیم و به‌همین‌دلیل از مردمی که در شرق تهران آماده بودند عذرخواهی کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/447519" target="_blank">📅 13:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447512">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyq_9CSN7RPL8m9Eh1h6RlULSFcCaT-e0kUlUFS1pnqlCFoNKF6zAWwYRUGWv6uUHgzRQqHfSUQIVF-kJIeMb9VGsnoRGduY8RseZViOgf0Xjwy2Kb2sPz-i83C1XYQvILQrq3XSi_IgKGCMCFZFGt2qtj4Q_NfjNiMKf9-MQQYhBS0xZNvnrl1MOqPZv1x9E6sbDBhmuiTtSNv4ydPqa8fqZ_hptZg5hd-2ZcC4pA1576h0tQ1k_E0QEpaazTudQhvqig77jOsEsdab2P0OHSwL8mm9GypdqLEpHV18yeGE0vfvFm8ocWdEhaSM0fw9nHpB3Sfx7AnxPTsKwazpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAUcnKne13fTyb5NdybXTLKxChkK5ZpPs0Tt6SGHnUNjBkCSi3wgh3Ff3iZ_FcHE6Sfpj8LYXi04Lgu33dkqTSIj2VrkEDT7jSmhf5bWmL5OH6sZhcgLiR2ZZ1OXA1wc6s6gNdWgd8FnaA1LZOpdeJL59HWFoXashW9afpLSWoZLhpqEsqo4m0yJzllaP-wUercUdxQCWVDpYMqti6TQu4gsqKEO4bVZL9y9UAOvuRcERYeQCf_zBrZf_oOxK7MlM96qBMs-3OtQASSf5v5Ba8r5OBNWWwVE3nOO7wgMFSTX_d6j8dQ8--HT88dj3-ncdbLoKlbeDlbN5dAsKfubWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugD7XiZFrLoiBcin_oVzA7A7_sQtw5APKZeqojX45FDl77Mq10Fxik3Jzc9U5Q2gPp1o0_AVjUiUkyJ6FKz-Ps14849503OnyzWPuPzZICT6vFMEyu6c1wFGkvcRbFMvrWCWoZTjPm2f1Esi7bM4r1Ot98GJeVN4IVHimmxzyFvSRidFJ8ub8OfkR4iC89B1sFquahY0JGoNIirtFul6jY3ABDoAkB6uyXJTjzqBYsgtiu0EoGKfn4Q0PFDCukhXlWM_a2PkOEvqwB2H9AZFHUE7B4j6XvJeEsFXzuzilC9H_A3Yo89iI5eTd-DyNvBUvHMXyaTE8ESd-4hZ3Hfa8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrHrjJhXulOIfu9r3MYEZ5wH1CvGUiJp4Cvi_kgJ4fOkEyIjTV9FhzshN8YJbDeLNrilUiJb6uSZEQzCsglHJqcG1rHT59JhOtKUlOyYn3rR0tgM60svb8_VUqczyWQndxtpicmbbrIDKYDc9h_Xq1LMkHl3X9j2_AW1XfSEpTfOhqVu2Su1PdBCPjDctTNYdduRirYZ4IFDs2z7tzxtXrSADR_oXoWVgFrJInvFNDYD9pAncTqILHrcOagdIS-TPAw3biVWFAgHFNtArlmLR_fcZ-iavJ3S9yGTWsI9snpo2OKCb30G_vhd8JXB73YQvueyz4L_L4a7-UEOhJC0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhB6_7ql4KsD9TxQDJyh02aQmBy7sWHWYCWvvYlnkHlbA7jABgUC3NnEpDfP-yADCeeIigA78qoid7Nb4dxAg20DtW7ACoy-rZUNkQuXguZKxSM5nvpn0qM9mzRG4YDgWQeJM1Npkq8eOgcYLXXOSHej9s8N8lVXKtyn6w21vrh1PFrqBdC3WQrtpkyJoGooRIVngX50XJm2EtOy1MnOq6vetHBtVsuu4s0R7SCqeC4oKV_RGWXigQQeR6fqCaYHxb8e8ZgbkxwPBCVA5R8n9tzghOdUBA9eyYWEIZ9FFxkzrmvx0IrquMtBrzgxyEk6aGc0bTOnyqCjpAYL1dmaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZlScUBSiLOmOXjMruAU9jUHb6OdM2enAnYVuMrL4WdypQr_8ojANJOHi6CB9LOUiRbkjgDPToynzSz62dbEbYelyg9gCfBbNFVJ3g7W4Xvncn1ZvlT2PSqBEitsx3drcQKGgpGaZJJI4ISnVJbXzQuBnvoqIl1Nmvr3dPA7jboGyPFP8CDC7DlbHT9AfDeAac7_lBGViWRTOsf8s3AxDVTR5Q2rKPNULDEYxP_0OABvGSVJYj9ls0HbMJFKs4wy9N6D41Dq4mMVCLPY75D3YZCHhJrLfHT6Jkq7jQ3XsPx5bXtQPalY6e7aHvgYnWHs0pJT0pQ1XgLek9AlrlEGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRlrhQ6j4pWMU19bGqf82Fs6ZqpMepOvWMuTJhFPdfGEAWXyUe3JaowO0qNTHveCTs7qZuJD0OycV4u3cDdo7_xFcQBH9Lf3o6ihMCj7HmjBf8_TEJLMrBE7BbSrSXvf6yzLQSt65Zrl0Ewg0ceDqBLPc2nLD2U3DHbnCk3-tPpkOuh2ZPyusi_n-i_bIJgcpDozqCOJBxbA4LiQthqPq-kKU7Ruw9MSNEcn35CEb8wPLhKqm3UooeSZwuSex-voajPXznzV2NLW8oHkI-xHj6iCLoso5_IpAPL2bLHkSM_5BWgC_FdZ24FSsGvU--4yGle2wZFI7VHKgEGe4ZyxqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از تشییع تاریخی رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/447512" target="_blank">📅 13:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447511">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX3-wzHumoxovMD1HeljgGuKlxInWbi56er5H7rQvm47gKtmFu2oIZhSdnogO02xG5py8Or9i8blW6Mgj13pVtG3KuTdK4-53d6__9v-wq_-hNY75UuCgZXhKljKNEBrp2VDLiT8NX-yxvknau3TiC3IeABRGOjbv7hUOZu_JayUZaJpbTU4SZ0gMYBeO1vsRvs_2nroy46tkCYO5k7QjhRwdyTIs5EgvlYPKxQJWptweyNsSdCkRCFaNgokgmUljAyaUrI-te1Ftl_3MuTtIQYpkAT-gnv9-K8DXMY4NiW0g26c8Cj3dW9j36KewBeRDjzyHDRuqHunCz22cJ-cag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور جلیلی در تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/447511" target="_blank">📅 13:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FULN-UXxTjyEtTR_W7xs8aHOH3OU1VGovopXw_b_7soxfaYcJUmUuqkpmukYhB8yfWtc5eY3c6QztMfg3cKoBrp630mxsZcdiDbPy8spKztj_ohvKdRZcYci2GalXN6iboNfpa1PR3SHH14dBe3dUY_4AcX8TGJWjxQfCFFrs_wAxqbhJXtPfbqLIktPdII6HKf34TOC3ESPx7maOmjlqBWAcJ-Hr70rXYkCb-TRpePfjenE0giiC8G18svQH_igxl5us21dftcsOtL-vcIfh8jH8LgeRmoB72md8sAz_XwFZ1lJlAtkx44bVU-lh2Nuqys-gtT_iKG2kgcWiOSwxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3KKOam_TSGeu-Wn_E65It0HuhZ12XYoLfInH82UMyRG1-crR1LaS-yo2k4ayRZ__5QEBHr5pejQSRYVG16y2FAhhM-4n2UG5Hpp8Mu20MiR6abWZE21meqnaWe33Rak-quN_qlqzYxGJglmrj4oxLfnG2R5EcmKlYNohynldKfUsmvjFy2H0LZoOyO4JuIM_unOnhGhpCGzzgD9ADJ1250wxgdJciSUIeoC83lI6BGvYiS4TQxwA1pwHA9mQFQGZIpbiWLGFZ_eWnKHUjOe03CCtApALFVF6P-tpC1P0FgDrMO58uFLSXMkoRBzbhcfO3oK_vKRj1GgP8SWcShW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssxyCRga8Cf_ii86i43dMBrvxDRtjklijoxpJ1qFm5quHoZglXi6TqSPn1DPM7rzFEBoiMNiFDMJvczky4vmcn4keDTsHy-yTiyC97x34jCvhcXPBFXPpTTdzOgKb--akfnsEPd4jcGILPlLRaDuCDfY3lI-dzVnbVI5Ge3W-PHOjn_5bVBT8GrKmigTYbyQAaxFjlqVHA_KaWKWkAikRwSNuk1aQJ7MlE0BnDiyLyntCd-deDoHXvORipDMODaFEmP1-ml42yYMgdHVXPfRG47AYKd_nSC158Yg6Hw6cTTvHTHXsspcgs-byo2GIpExohHKmqXWmXi87yqJ4xB6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUXacZBfNHkgHmgE2kURUAZfQNPwkuBu7vWU-iMjntBAvlBzl4tRYATSVD5IbWRrYFvg3xec7-yarIb2e_hDgGXQ6CFeaz9SejgrThyq4mQWaVFLUtSSsjkOKrsrE28rgo1KhLwc-EEwlco5Jo5_LFYqNUU-qJaoAjUIhQo9_QTRvlnezzkzXO5x6N6zO_Xo-1Hm6txYJgIwbhrFcC281UYItcHGHHvGPQ6hz_RZkz8DHU_r0TyW0M7dwxJ6Axi4jpZD_hxaeZxTQ4506-GzkQkfh2dYZ8xwD6FYvjk4JsTyMJgGcDvWLerSokasLm7s1lXxBUWrnqpsdnSlpsB79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Quq-_B6p2X78rCA4jTjTdMNkW3M8LBafEVc99-acZrpyA789VtgqzqYS0uVc9QUFKoYz3Bpa4BIsD9aYUl-DEEpRAFf657y4Qth09uGM0zTbzv7X_ZCOsc6kZkIMPvBczDf0B6evQy_UN7eeGMm_MHNgp1ItZsTTkWzf17a6ytWC8fskcSAzXFh2NzOZTRvLZ5-_sKczc9d9zhJJWh0F-w7oTzmY2z2Ixqg_JgbRN20QLlJu7DSE0u_Lj0WMhQcgT-MsC-xPeV8gBDZDNbYqYt5avBeh1fYdXP51ZbI9RFE_BF6A1iSf7q9uyvKLOYCJGqw-scGaycuQN8QK1H3JoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8aNCGaaXF1cfpFpL7g9LSUN19aHYyOr9QpXPA0SAjh_TBWuPhBIWb9myTZS-0ZkwESTgrKjit-yiTqqwTPyeuuW-bUSvPnPzO1x6zZWXK92wXKrPgDYroqS5VExCLuYlePQ0louUjOU--ekWlyC4H4L4TcdZ7neFr6d_KcXPhHyt-0ykVU6hk1et3SkJwPRjC9reoGj5nBgSUWunC4PYPbm47ca4lbzJQGzG2JQhDeNbhLs0x-XyGbRN0YcEKwtfhtrg68YQsQZMW-FKlmAfo2nZalAW_p7g_wBTRDUwlRB-TkwPTPqI9sC0UaDtpblKjNhTjhrRsxgBWYpoKHk3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz5gCULyxUNJrJfRa4QMt0YavtHNAl47xZCZUPuIkkwavR2dE3zIVbaZwPEaqfZs1itUMAIWvi6iZIK2az2m7DASstorGSkX4lSZXVIDpphHz4sfYfy_NKnxxYElxBUiSujBr62Al8TasE8aG6eCWbn_FnV6DeJHf-HfzEA8nzu3O3hHVRqGdVkB74B0gkywy12EBde7iCQU386XVsV-xFY-rw4tBd0zeh0nVOpKQtF8zJ1g021X3hz8b35q0Kw5xa9UMWc5G4bbHZ23I_BzsspNsLZ1MPfuyNIGpFil6tWpnmq8UYnUX1edLmKO25IhhvVBJVocEfUUmpu7LrES0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIcgHVf4z8aokxHCFpqD6QxxD5-p-GVMeSE9QLBItHPNCe9QWoZnMgN7gUe77h6b6seMCK4X3x3y6IeYVMXMrBxuJld-F8hZgI9UTVXGijJtvd_XAOo6QIuX8prhCm93Xjgc-aisZfPWIn1AzsMmhDwP5tcapk_uwFKNm-pIgVx4L8n1iW3fRR4MO0DkKtqJT9RDde5gHJZqN3X6kZCBB3Qq3EGvOOodX6z33kDqV15Cg9rFnqGWfwS1aocRFMHlLQqLr9gdvZNWzc5X7Eo6qeIjRpyWLb8Gipw3jmOAOizU0kZe3_IOaoV-5bOfRsZW205YfbpAGK6rUhQ5kPoHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu3T1Je0YBpxAmCi8zYCJS-Lwu9jWcO0QjlIC1fg0vHbOwCCPv2LXusPDZ6Fveoczu8eW_UZQFQ98iunWU_oyt7cDlSIzDqj2W1J0s2H8_cPfp4EbHmQ9DhlM2YENpqmfZiosHaXoM--bRIcTPB86ojBD-Kyf5Vw7NML3BNXtdG_Y3IIz760OD-DP-qWUzFvUBqE15q8-5Oyyyv6-Z3oN_FcDNa-Im6ccLBwMHeBrbkicW0sjM9qTTzMUnoAiFZUKUiS2woa1pelylqwj_YyGIQ2_w36EJwl_CzciRf9Kt6PZsIcwvszufeKJVtsGfo1PaAF4JGgry8BcqKjNaphTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0p8LPMxwz6p4jZuj3Mg4QFTtBjMKkMlaK74RndtX3B3GMJqnTEjsJNEm1rc4jz0bWmwR0NaOMQiG6UfRXHyYfo_u3pVpcS8DBjt0MyrjlCt8Vz_XJ_6ag0Hb_bD0C7_2eeyHDws4V_zDpieUdaLLi-ceI7Qe-Zt8WHTWTZotSmJrydhF_FdCawVUghaQZVyOdQK0tpOgjxDq7P-fJHdbWMYfixXfNCfjSJPzRCMd-MQQZDMHibm3KvQuG7UQx3SBF1Js2jrG3YLIY6aWbjdD6wUJGVRI42rRlPziY7WdaRtUSr0Fbd7_2xh9ApbdtalS5-cOO3-wmrhEPEwx4LstQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
به یاد رهبر شهیدم...
🌹
زائرشهر چهل‌سرا
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/447501" target="_blank">📅 13:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr9s3Qclxu7krIoZLbyMgBVUPyXseMI2ik3sk_3qTAbmNNJ1pKj6rLyplyoXWkCVinMGTeKJYrLbje5mis4G5rhyZoliSoem5DRyKK3QckXOQ_5byEV97dSExCGGmG_rDxzsN_rlA8XW2Oy7qefA5m_lm7xMRhimyfIkBFoPCGEO8zQo9qst6phQz66WUjNj2Sc__IgM2VtXZY3jLFEv5C0cmcY3p9l1_Xm0uZrPfq9yMSSHk6RloRjm7NZ9-b_0XHCBgASfOnR0HTvloSu5ZmKkk0hlt92VKyVPokHcLvvWTJbG-D3can8rr_AepDwNpzrI_myw64kkdDhT4dJl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید مدیرعامل از موکب‌های خدمت‌رسانی؛ نوراللهی:
#بیمه_البرز
تمام‌قد، پشتیبان زائران است.
مدیرعامل
#بیمه_البرز
در جریان بازدید از موکب‌های این شرکت در پایتخت، بر ضرورت ارائه خدمات در کوتاه‌ترین زمان ممکن تاکید کرد. در همین راستا و با دستور وی، علاوه بر استقرار شبانه‌روزی تیم‌های تخصصی ارزیابی و پرداخت خسارت خودرو در تمامی محورهای مواصلاتی منتهی به تهران، اعضای ستاد ویژه برگزاری این مراسم نیز جهت ساماندهی فرآیند خدمت‌رسانی منصوب شدند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5056</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/447500" target="_blank">📅 13:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/447499" target="_blank">📅 13:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmvtW_TbLSqLWHIJGiWnmdvhvwuPE1RWtxwXBLMPWLAM5lX3hwGw86lYvc2WJE_BBeMMTp36wPAdCtd2PqKG5QIuYliSztjBWOWp-PRX5eB6oDyMIGSBVr4Bm6YCb4ZwKuSKNmzzYFKv3bcunsnp32DnGUvs8_x6t6MqS634sS25o9gudpLajwCSuMIyNy47F5sfOxGcyNKes9uiAlWNWMr1ep0vLOKn1bwfSHShBPWCVHsZE_gXt1Ha36QCeGLcNshnikSqiYvdGd_53QI12mAbPGSYSacH-T5RXwz8VqVf_GF1C4fABxDTcJi6Qax06JrSYgu8ZU3UhXo3O_j5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور سردار قاآنی در مراسم تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/447498" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e946efca53.mp4?token=Vo9Z6UGJ-WbnqusvHlVx-IFXjSTxFn9S1xKWSsCXiO1cS9QotymjzkMSPWcLMUTnWpjzmgPBeTYyO44A0UVRO6q2rrTiQrDRI3004S5ArU4YsszKsi7BoxHlBo5jzMkm-YPujLzTbCOJI06bj6pbPWme7fn4xgaBk89hRcT_fXKPFGx_UllOCaU-nm6-ipTfNoF-RIAxSE19YOUBl_J1oWKsDT6amopn1JIWjPD5pVMfM9IiNyUSL5qTpE5Nyqb_bJnsxhphSY6pK0PNit7pRBlWcSxv6YcanJtS_0HyfBmBwUTGQuDqIEqu-SATtD3m8SljF-5m3qjf_U38Yf5Jng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e946efca53.mp4?token=Vo9Z6UGJ-WbnqusvHlVx-IFXjSTxFn9S1xKWSsCXiO1cS9QotymjzkMSPWcLMUTnWpjzmgPBeTYyO44A0UVRO6q2rrTiQrDRI3004S5ArU4YsszKsi7BoxHlBo5jzMkm-YPujLzTbCOJI06bj6pbPWme7fn4xgaBk89hRcT_fXKPFGx_UllOCaU-nm6-ipTfNoF-RIAxSE19YOUBl_J1oWKsDT6amopn1JIWjPD5pVMfM9IiNyUSL5qTpE5Nyqb_bJnsxhphSY6pK0PNit7pRBlWcSxv6YcanJtS_0HyfBmBwUTGQuDqIEqu-SATtD3m8SljF-5m3qjf_U38Yf5Jng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش سی‌ان‌ان درباره پرچم‌های قرمز مراسم تشییع رهبر شهید
🔹
شبکه سی‌ان‌ان در پوشش مراسم تشییع رهبر شهید ایران گزارش داد که سوگواران در طول مراسم، پرچمی سرخ را به اهتزاز درآورده‌اند که نماد شهادت، مقاومت و انتقام محسوب می‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/447497" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70242a5725.mp4?token=Xe6IMJOJ3VtlQpoud2tW3zcUUd1IYZLAjqiOktkpzKhkIBxWDo2QcbKYOUbIltWVOXd1pka7eeu8MOxtz_Ku-YZgkVD9v3pk2WPF1dhkUCSqQQp5cnn9hMHPimO2NPgsyqoiPxeZGGbEAY0Rq-8tFPxUkm73zgQruR_z619aw09ma6MwXi3guIl_gCe31CUCYce6U7wLqY3WMNU2mnSJYvAp3u3OV4lLlO7kI-drYT9DM8XR2pij6DoibUIJqvheNx54TWTZ-IJtvethDq7MR80uNUqpaqMHRmKcfZ0Px798TzwjRP5ZNnN7iEbl0M0nnYWxMqeoQIjmHJgLtUq20g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70242a5725.mp4?token=Xe6IMJOJ3VtlQpoud2tW3zcUUd1IYZLAjqiOktkpzKhkIBxWDo2QcbKYOUbIltWVOXd1pka7eeu8MOxtz_Ku-YZgkVD9v3pk2WPF1dhkUCSqQQp5cnn9hMHPimO2NPgsyqoiPxeZGGbEAY0Rq-8tFPxUkm73zgQruR_z619aw09ma6MwXi3guIl_gCe31CUCYce6U7wLqY3WMNU2mnSJYvAp3u3OV4lLlO7kI-drYT9DM8XR2pij6DoibUIJqvheNx54TWTZ-IJtvethDq7MR80uNUqpaqMHRmKcfZ0Px798TzwjRP5ZNnN7iEbl0M0nnYWxMqeoQIjmHJgLtUq20g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی هوایی از میدان آزادی تهران و جمعیت بی‌پایان مردم عزادار در مراسم تشییع پیکر مطهر رهبر شهید انقلاب.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/447496" target="_blank">📅 13:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1288f6e2bf.mp4?token=fAqYEFfA52wT-WCfCEVbg75x2kjSRLBFIytj0h9Uiw4iH2x8o8QWXfQnswCa_46y2UFI98p9WyWUqgOGncr9hbcB7bGLRclNevfRG_j84NkcVvth0bV9STAogpU10g_EuxmA0is4z9yy6CvYcIe1AvqOUf3ZsfBLBY98LHkrULqOqKkV0GeOqZZNTqkFLQ3A_CGwD3g_wjAdW7_YyuPZV6zD7Oy3Wzz47irS9NmFnSluUc_bmLeMBxn-9e3KkLLTJ8ScrN0aRIRt8qBXOmIU-5WsHkNjD3IWpSuipvrrDUH4mZzkizlEzCptIJWDvsz-zdhQYVuZMA-X5KcG0qKplA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1288f6e2bf.mp4?token=fAqYEFfA52wT-WCfCEVbg75x2kjSRLBFIytj0h9Uiw4iH2x8o8QWXfQnswCa_46y2UFI98p9WyWUqgOGncr9hbcB7bGLRclNevfRG_j84NkcVvth0bV9STAogpU10g_EuxmA0is4z9yy6CvYcIe1AvqOUf3ZsfBLBY98LHkrULqOqKkV0GeOqZZNTqkFLQ3A_CGwD3g_wjAdW7_YyuPZV6zD7Oy3Wzz47irS9NmFnSluUc_bmLeMBxn-9e3KkLLTJ8ScrN0aRIRt8qBXOmIU-5WsHkNjD3IWpSuipvrrDUH4mZzkizlEzCptIJWDvsz-zdhQYVuZMA-X5KcG0qKplA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حامل پیکر امام شهید با سرعت بسیار پایین درحال دورزدن اطراف میدان آزادی برای تبرک همه زائران امام شهید است
🔹
سیل مردمی به سمت اتوبان لشکری برای ادامه تشییع در ساعات آینده درحال هدایت هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/447495" target="_blank">📅 13:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8d1aad6d.mp4?token=t0jkwkz-_ek53SmiZT_hAwffMdcTFb9asQE3meVY-fKWPMDUJhx-Au55tOWf3gJTal0amjgqxz4a4adfwGbc_oRQfi2L9jVdzVEDqELDxfAr7yy0CGbr-IVVXNcECaZlGKoom9rBK-DXIcZrYu42pC-cecuL4-0tvUqilMONqgeQfIdaMuiKsjqVworyOKCvdFPFbHVhAC9JMvq00F59wHpWu9Saq1o7bh9fiGoDoScXdGZfRgQFT6Gn9gPJGo-F1sN18g7RKGAXPD_cia3UbCVpEnRPPtQUIy-krEfn9JhSdhRQbZNiMICKiPSJmMANVraf4j8pD5ocBoYf9KS2wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8d1aad6d.mp4?token=t0jkwkz-_ek53SmiZT_hAwffMdcTFb9asQE3meVY-fKWPMDUJhx-Au55tOWf3gJTal0amjgqxz4a4adfwGbc_oRQfi2L9jVdzVEDqELDxfAr7yy0CGbr-IVVXNcECaZlGKoom9rBK-DXIcZrYu42pC-cecuL4-0tvUqilMONqgeQfIdaMuiKsjqVworyOKCvdFPFbHVhAC9JMvq00F59wHpWu9Saq1o7bh9fiGoDoScXdGZfRgQFT6Gn9gPJGo-F1sN18g7RKGAXPD_cia3UbCVpEnRPPtQUIy-krEfn9JhSdhRQbZNiMICKiPSJmMANVraf4j8pD5ocBoYf9KS2wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدر زهرای ۱۴ ماهه در مراسم تشییع همسر و فرزندش به‌همراه امام مجاهد و شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447494" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLDoBFJFf-NXNrCHvvrszD1ZnnArhzWpTqlFIakPaH9NGYBjWq5ZPfgy-kDY7lOZ8_DOCJCmHNPKA8mvpTYJz_4i3yMNa1CfYydxC6cXy8q2noQILhbaoJSEDVqlQu9-JQXSyWu7v_j3OfwROEGwtkZIyEoCPLXltQLBuf58BsN1o2NYE4cQg-PSCy6cXCZMR-SHxVIvbrnmh238SKpbbKaTDlRovXzIKPJ1brIuxnvrFKhK82NHvomN-ad00jznrPBTDIhDy_wmRs-TIDZ_PMst7xdbJkbWc-mLSM1sOyc0S2BhSf6ObL6IHOXDwEkkbsL8SpWgCizXd9qPPrCl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ok8j6a3kuw4cwWPikA8Q5IhcRQx4_Dkc89lxX9wUhk8kq_BVkAHOgAXPxbLfzPZCTJ7ziCMHXZMUxfq1gAyj6q3Q7hQxVLS0wcBCmlJ_hjdlr_q0pMLkP0HJqjd2XsCpMBcDc4aGbG2OH9hSso8tF_nqVtXcf1LOf8Keyot1UhHvIOZ-2NsYDX1ARE2ZYtTXyTqseeIlOCLbOxtdclKD1kTIuAvw4OG7_WH7p6-bdj9daxuNYLYP3b2XEUYajftxP7O8f7Wim0lqeAYxHF7FrPmpOa9ZnDuGEg_gvg8QlFILlFs0zd8BI1frmLtLax6VCbxa_lojgNnub1-DAzBcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPm26ANKX6FPFomEjTqxr9p4NCPAcOn_M2Qc3B_7QMVYqV1fGifHmP-Ix18lkFJ_NmA5bXe9D836DvaQjRbt4bHlodbPJ5uGMbHNgEiyzv5TaOlOhjYZbt5rrVFluORaI5LHsEpDKjj1LXWmA8KLZOKLXkBHsFlWfJN53otTIJCi1WBKrvVGdGeXFycFK7fsgWuzEG7JWAGJHikjEPmmI3JpUP9qWjVW4ZLobgS0_hbTKwDbXZ9dh0P_eeHQKMnWOKYDYCrtVBo8emId8v9Gw1D9MVNOMByCI4wM4kHWaA5FrQ0jIKEbV7R6vyAJZPTcEHSe8oIQMKaEBDpPyvSfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brV4CWPTH3zd2RYqRQEsOLVnDEVumFmCUGrqIySpvbCsyUTJkDMQ2QqqTXTiVfZNhy8GBqy6MZ4FXgsJpY2UDn7g979ACVP1lZkTXy9ldFZtCfxBcI3_8634xWlTCz6HAodbgu1pGyP1Th-Sd69E58bb-seXT0hwdXH32uVVBPst-QHjveE67AL7tLesi6FAMYEHykjCT-0czBJD9GwJGI-8ann2l6SDOYDpfSNbfA0mckJ92VPkq0t7Wi7KrTtpyx8QWWChjSICCXOHvmevSK2EfMGJYSWmJ2sRA_lc6wYSFR-X6QorhlQCnDXE3PjlRm5IeKTCGdOO2-LorTMVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BASJHSA0IHhJXzWpNuRzpXhs2hQA8U5Vk7fH1IQv9aIeNpOedzFFKZD2GIDnqIOfkFUC4nk13x_wZsHJPW9StAUEHOTUWXJ3hMlruMdNgXRFe5CEbnesf4YiaI5RfPpWKuWXYOSTFMpvO-DPdluFYStiKt0jDqVGpb2x9PvFgPPiSs89UaxmdWuca-tMju1lmomPYE9Ygo8ia7d6XL_BJ6Jhhr3y8Tqfc2e6_HelHpBF5QCQn0TYiGwj9aT5UrJ0l8GkqZC89jZUxnPg7WTrb7uBp2IrDQmSK2a_y6_77srwdPNV49-2o5KjfGZebwZFwR6c_xU--0HsUFb7vCT_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxj_sHrhyhDMMYJm9RB6mmjrbJPh8VyIgv1GiZJ_HQHKV5JJcwk1Nb5BNhY-66tBnXMhzctgq0IVyynZ1mj8xnMApCam7Yt6dKv3rTnsHUJcA3U2KFX81GptivhOIbD2t-sqUl0wTAUj7tm0orddpbtMkHGEv4P2-2W4peyTqxXLi-pi3q1imbEQ3TfIsnDYFD9s6uswmjqaQbO3b2nDAXorkCHYP107kOfmrXiK8sfVrYWsyPHQaDHTEZuswZ-fU6oL1R-rOZgUWqSpkfu8ZuKsi7extNIL-AufA0_LRQVga4h5RsyQCTQ8iaKZczmTpdF0l9SrAujLIv_SGiZbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPboR5jhChwBgwWOZGT86dqXDsrh24a0GEyOpEQiFrgJqgZZ4pjmQyPOzCemmnKF_5qbQKprJR2HQVig_m8S7crNpEnyaorvC4keaPCYtalSp3jDLbkW52lHYLPOzDbtyLEqIX_8vdEocAxezBjT6EB9y-78K2fVi25vlbcYlQFVlBHIV8q3P3rFt9PGGWCA4BWhQFRIksn_xlZLyuePXSZVWAa-QnTMrDv0HAgZrvouQrME4hGWlBatKMSYgU_CX5woXsw0t2afdRThvxdMbr1-5GhBKiu5xykz_rBZKZqp_MgO-jh8-z82JIs8XKUCaH6IGkCXt1epgJE-Yp5R6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9Cz60QWL_CCbH1mALn0bq2hU1MH-d-p3jLdyRERxO5Wz7HeDRsw4oylbQGwDtvaGgLBTtniJewAqmN4b-QCkIJ7poxzg5rtRX17r3ancyVfzMygp8FBdMLDSlrqX-aJAMFgVu429Z7WIBrpgF-4JNZcTuOzZhQFJEoGiOZvIbbL0X4Nj8gfF64ybo5kNuxZ_NTWJhqY4S0ltUCduJstbRGNitg0VBBXGvd9mmK2sMWVY8D6PH5gQI2BOUpdjuMfpgKMHU4oeKdLhAz9dvXzsZrFM12q-h_HdTqxy5Sjrb8Fcl9QnkHlP0SsbRr8RGJMYyR9orHGlpHsnh2m5R53Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8qCO9RbZbU3T5QBF6TlywzwkniA6rjjqNq6hCTQC60uBMMVRM-gHFD8inr23BP5YrdDiQiWF7I4GGnhbYhM5ZbOLM4UkaIZOnS27FMXaFFasoefrfMXEBpLDFD-pO8W1EdIROtS9NeeCHp7S8aVC13Wd1mmt8jzCeXJcvq9hpHgGPx2Y7Ig2UFDlsnyTnwgmMlAbohW263ynaTFLjlQxfS6rlBpt-rRS1hG6FVHXmtbN13GZpU8bJQqYT5zk8YHgy1ZJeexzGkz9zawPdZe09URSXv5KqR4Ew8_7WqXL6VQ4kzPUS3s5d0WOzd7DJhjVuOh30_p30QQZBQ8C21mNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هوایی از حضور جمعیت عظیم مردم در تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/447485" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447483">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdewM6sec0VTmDv6HqFhZCjRr3ugmQZM77GoosLeA23q29oM58837wZJM7KktPL-gNrCrrbGVsZELEsJrXF6bPeK0B2M_JbS9d6koRuS-43hO6zDKYk862xaLMDTZVYbHHe3R9pAmEV97fekeKEdXArgU7JIiHYAQjDze652joobGXYmO3nsUpRA4XQLoK3UoaXVCGh_5MscH1AkaTkTFjawct5DTdrvILy0ELEZ7CSsB_QQRxlyHC1NUEt0oia_jUfYhsObauT-XPyr0ln5dddFf3v2GZJAkx6rLAyUvTo_4w4NxeWMqVvykDhLLAx6phEk1tpjArrQ7sH6nD8Omg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUAb37t1Wlhu2Q-IqtOtkjCH-F62U4wwkWEppb84KgDVEOzoSDDPsM3ax2ITmouPWfLYSVl2uhdsyf9y3zyiypjGxT9jwunPZB29eOpM2_iA3cDM5Odslyawcmgdko1X-EyiteWfBq-UHZrScLaT7md1Kz7jJ7a1cBzeEIGdSOoIcv5SZuZze25OOI3YG6DNYLhrjAK4xMtq4xprX9HLToEfFnereUkLtLELTd_Mp2GbcDJMgseUPu0paVJDgUJhLcNMcZQJwI2n0J-j-dHfGSsY6Be2VrnkvIYle5Mk9sBG7r7U9pkfafIHqrtjWM7lBbGVh_3kDFXzkib0EOqslw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس‌ بانک مرکزی و وزیر صمت در تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/447483" target="_blank">📅 12:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447482">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a7e697ec.mp4?token=F38XpuHe2XdGfc4bX6G8CFjOp5O3N-joMcRmescyjq_e-jrUjpcAI1nQ_aYkvK2F1_ml_SpYYrgEOCDSe_f25lr5dwuzWQ8YtO9KppuHqXSBaQupluS51ZEcUiWMNfo-qTXbX4bww9s7PTyY1UfBYqM5Cd9Eb-6LAdOLCLalKWT07eV0sabCqHsrBRkiz00itKqB8ojv961dIdh4LxAIFD_mGqAP2SQZ-OOfwhSkYxfgRNHlHD8LaRLhN2hcjfPHtya9IUHW5DSxJWE2CSS2cWqTL2FfEgdYh5gdI9gSNXSMZ6fpOZIQRLBXFOC4zbl-1mFcloehm1sIe7cq5NFf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a7e697ec.mp4?token=F38XpuHe2XdGfc4bX6G8CFjOp5O3N-joMcRmescyjq_e-jrUjpcAI1nQ_aYkvK2F1_ml_SpYYrgEOCDSe_f25lr5dwuzWQ8YtO9KppuHqXSBaQupluS51ZEcUiWMNfo-qTXbX4bww9s7PTyY1UfBYqM5Cd9Eb-6LAdOLCLalKWT07eV0sabCqHsrBRkiz00itKqB8ojv961dIdh4LxAIFD_mGqAP2SQZ-OOfwhSkYxfgRNHlHD8LaRLhN2hcjfPHtya9IUHW5DSxJWE2CSS2cWqTL2FfEgdYh5gdI9gSNXSMZ6fpOZIQRLBXFOC4zbl-1mFcloehm1sIe7cq5NFf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید به میدان آزادی رسید
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447482" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447481">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c24c445a.mp4?token=u2Mon7VkrQBZ1JXxTOIgYfVPt7oiOxrbT8yEjnw-TfPosb0lph_0D5pXJyKfPtira7EGB4FiJ3mZoEwjh8PfAjexjOs8ZFnjoXIOaGgyj84hhQIQWGc3M9VJPQArySYl0wJuy9cTU23d6RMBQMkUEGJExVNT2q2QDCM0IUv7yUBpYNLo2m6qlGtzPHXGr9oQEm8s4exHJGErLBlfBJuQdI5sXQK-4zK8ZPaWO0CfKqVB9OyRJtOjtqvakKK-OvNqzCj9QgZ96l7tUxaR_b1nWsaHb2CLvHj3JMUp-PCE4NDM5_TZcm_wgTb9dGDcSQTc5B1X5X_z9FuEjVQ1O_BmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c24c445a.mp4?token=u2Mon7VkrQBZ1JXxTOIgYfVPt7oiOxrbT8yEjnw-TfPosb0lph_0D5pXJyKfPtira7EGB4FiJ3mZoEwjh8PfAjexjOs8ZFnjoXIOaGgyj84hhQIQWGc3M9VJPQArySYl0wJuy9cTU23d6RMBQMkUEGJExVNT2q2QDCM0IUv7yUBpYNLo2m6qlGtzPHXGr9oQEm8s4exHJGErLBlfBJuQdI5sXQK-4zK8ZPaWO0CfKqVB9OyRJtOjtqvakKK-OvNqzCj9QgZ96l7tUxaR_b1nWsaHb2CLvHj3JMUp-PCE4NDM5_TZcm_wgTb9dGDcSQTc5B1X5X_z9FuEjVQ1O_BmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در مراسم تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447481" target="_blank">📅 12:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447480">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791da2e3a1.mp4?token=W9iKgix-HjfdjjCuO18dk1SC5Bd1sBJkshP3O9oL53_1yMzP38u78QI_CRZuCy3ZxLgdv6UE7LETBxBV12zEgFGUORFuALGEFO0zP-Vnbdn23qshoqmhsazkX5amHj6md30OPET0csHE2T1DzSNs_nVJgTXMYcGrUsyfGyBsQ1bXyfq4EZ3PEBpoxFfCCpA7CEEbFe4B_XVhNzKcHHu9xKr-s1GsweNz2p_9lS-36KH9LJ9v8gE-qUeaUeU98hw8hjRz5YgUpDjjNkEFq94Ul8PAalQOj7nGeJL3JqORtSL1L19DTwwl80Y0wS0PZG4hYQPYnoElUA_ed-VaynMhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791da2e3a1.mp4?token=W9iKgix-HjfdjjCuO18dk1SC5Bd1sBJkshP3O9oL53_1yMzP38u78QI_CRZuCy3ZxLgdv6UE7LETBxBV12zEgFGUORFuALGEFO0zP-Vnbdn23qshoqmhsazkX5amHj6md30OPET0csHE2T1DzSNs_nVJgTXMYcGrUsyfGyBsQ1bXyfq4EZ3PEBpoxFfCCpA7CEEbFe4B_XVhNzKcHHu9xKr-s1GsweNz2p_9lS-36KH9LJ9v8gE-qUeaUeU98hw8hjRz5YgUpDjjNkEFq94Ul8PAalQOj7nGeJL3JqORtSL1L19DTwwl80Y0wS0PZG4hYQPYnoElUA_ed-VaynMhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقۀ پیکر مطهر «آقای شهید ایران» توسط جمعیت گسترده مردم عزادار در خیابان آزادی تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447480" target="_blank">📅 12:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447479">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ce7f8401.mp4?token=nv9NU9Tp1wAWGTYKtY6RGfVr2mosoGN2f-iCVDAA9G29pK2CAMeaYWHAirpNtHlMg9Wpiob_6ZLxztA9LAtJ-9e34iWUo0fAeLIginI-s4DUniHS23WIzuJp049BHY0o5umltqHqppqNNq4_WJw_Hh7_qfrR80ePRA0KjSP1Bv9fT5bgzRdqo-gCaAFw9BrFWSOKHkycD5I3vfPFzO33XEkzJb6bOqBRo0RM6iYsdG1z6csvKpYjDJk77CTxTgnaMH-2UX-eJN1an5gEhBylqvQrVEyxZKVrQ2o-mjokj1feC6BJG3Y8ab1IzXEXbQ6g0_1vr9uAVTeefJ1aRrIjOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ce7f8401.mp4?token=nv9NU9Tp1wAWGTYKtY6RGfVr2mosoGN2f-iCVDAA9G29pK2CAMeaYWHAirpNtHlMg9Wpiob_6ZLxztA9LAtJ-9e34iWUo0fAeLIginI-s4DUniHS23WIzuJp049BHY0o5umltqHqppqNNq4_WJw_Hh7_qfrR80ePRA0KjSP1Bv9fT5bgzRdqo-gCaAFw9BrFWSOKHkycD5I3vfPFzO33XEkzJb6bOqBRo0RM6iYsdG1z6csvKpYjDJk77CTxTgnaMH-2UX-eJN1an5gEhBylqvQrVEyxZKVrQ2o-mjokj1feC6BJG3Y8ab1IzXEXbQ6g0_1vr9uAVTeefJ1aRrIjOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من خود به چشم خویشتن دیدم که جانم می‌رود
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447479" target="_blank">📅 12:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447478">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b745ac698.mp4?token=qcsWRAjljA0PozzgCNo-68CdGDW8Q3Qh4m1swENSV6W-P-wVSmnsFSkS-paFZ8P67dWWhLl7CTlZNHgb7b1kmrxMW_2kRepF9-k8UP0A7t-8EDi1yoNuOR1G3CNvGd3zgzs-2StExiYh_iq3JX_elMk8vhTMPTff_7OsM1UrpZgLeQrVsh8SpOCKi2ZCmjShovx5_i9tLsazh__vbIEuhU8dVhhg3boQhFAJPuom_LsT91C5vk3GJYyoX4yPQAzs_J-HKzZ3ZRQ6khV5B4bFWGTt7txdh0jGxCUU8B677PJUGrSHYRYAz663CwxV0V5ASZjUfRnESjB_38sXGrjMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b745ac698.mp4?token=qcsWRAjljA0PozzgCNo-68CdGDW8Q3Qh4m1swENSV6W-P-wVSmnsFSkS-paFZ8P67dWWhLl7CTlZNHgb7b1kmrxMW_2kRepF9-k8UP0A7t-8EDi1yoNuOR1G3CNvGd3zgzs-2StExiYh_iq3JX_elMk8vhTMPTff_7OsM1UrpZgLeQrVsh8SpOCKi2ZCmjShovx5_i9tLsazh__vbIEuhU8dVhhg3boQhFAJPuom_LsT91C5vk3GJYyoX4yPQAzs_J-HKzZ3ZRQ6khV5B4bFWGTt7txdh0jGxCUU8B677PJUGrSHYRYAz663CwxV0V5ASZjUfRnESjB_38sXGrjMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز عزای شیروم
🔹
عزاداری محلی جمعی از بانوان در متروی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/447478" target="_blank">📅 11:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447477">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJfqxfNzLUjGDklos7oNAMVxwQrJrf3MQuWxqm-nXuFeAPfKjkACnljmU2lrCFHj_DcR2mTDcS_EmTgYuClFEzKW3OmElqeQj0noMGIIswxlSKF8O7g884UUh1EEKJj6HjGN-EIIUNAmCT-iZMtVSynHHDMvcvPKIcQq9gha6fXRdPyiMVVfihj90m56mrt1bMvwWiXKy7FN8JrRqK_APnVid-Q19wyIb0C6cnwqAP6xjd9NhwTxUF8TC68MGfXIv12knm0WNF0fm6SsspZoWQY6UAhnTL2Maz0Y2OY8VTli6AzW49ha9hBW2CL7xAC2kIcaMVHlsN3e6GWf_Tg_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رهبر شهید در آغوش خیل عظیم مردم
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/447477" target="_blank">📅 11:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447476">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a0e53ca5.mp4?token=hUX3XjFElqesuIzg7sy87ZFsozf6LiEH9itoFcIkzmyE-dwpR0A6CO14KnlgRNHCbBDqMePan7NbWxzZ2t6s3-Hbu-mXgo4VpC5nau1mIee7tLAoR7j1f-8pkdVgy0bFNcsignchH2T5gAfVwbdcbf-AG0cMrVDF3JSw7lH8E4-7d4rR8qHKMW18h4Q6pAWcorU0I7OckRjk0XnriG09JjioVlz9-IbJwNjSqxvQnc8JnN1woQxCDXV44tRgBOMEY_sJK1s_3KynqbqhTQJB3EycIWeaqB9yatOvoBMIxm0b4frUkbJqg54c7cY7PhN1JzkLDwhvrKDCMWxShFEUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a0e53ca5.mp4?token=hUX3XjFElqesuIzg7sy87ZFsozf6LiEH9itoFcIkzmyE-dwpR0A6CO14KnlgRNHCbBDqMePan7NbWxzZ2t6s3-Hbu-mXgo4VpC5nau1mIee7tLAoR7j1f-8pkdVgy0bFNcsignchH2T5gAfVwbdcbf-AG0cMrVDF3JSw7lH8E4-7d4rR8qHKMW18h4Q6pAWcorU0I7OckRjk0XnriG09JjioVlz9-IbJwNjSqxvQnc8JnN1woQxCDXV44tRgBOMEY_sJK1s_3KynqbqhTQJB3EycIWeaqB9yatOvoBMIxm0b4frUkbJqg54c7cY7PhN1JzkLDwhvrKDCMWxShFEUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور آقاپور و محمدی، ستاره‌های تیم ملی فوتسال در موکب فدراسیون فوتبال
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/447476" target="_blank">📅 11:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447474">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2JX6HXEH5JlWHVzqzGiOjtibfyMOr4COQiQGw0QalN-OL7CpZODblGeF8h_HhenOiIJc3dDU_LYcssjx-U97LTEMebXJGngxVn-H_OcotovxUUFMHuXuZjFFKc9wgDc1gdm5ZxxTbfEZVtpOqsi69A5hp1X1rDEKvcUbfnGtWqHhi4reZJtGo1T6DQAhLqZI0jnTk5yQyZxxZRmMqViTsLZNKejiQrwbwZNyRKgcbCR1jk3hA8WYyoKW2X_dz8lWQ1r_JXvHkFhns4z4Ck0eOLaYskpuZ3Tx4rlgB-8XnQKhGzrqag2qAVf-4hKBt9uX_mR5lxtg4F-B1HP8evgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-636pT-kgQZWnmmtr5h1G6Z9-3b2U5GqSLai_HIbb9m97exN8ynfnLGxI8QPv05xtOf639MpdNMr6MfsK-WCZb83XXu-I0fLCg12jCIOAKKF116h-RwGVH4fbl-HbuERUbQTOQB8JVFYZlcf8XolmsMXcMb9qCxvu-LwmNkSgDDCsjZgZlC9Ewi06rB093swpNSEnqaEGXrlbJkEXYUrBKNGJxhG-Z4xiSXSL9enrWQOvJ796hyOSlQkhnx4mWzO87ymaxhgh-jcRG9j3s3fuZVv-ksbgCY5XYsmSUzIUj23FV19gvopjcMSP_aMaaMSz3W35_xOnLEZHmGUQD7qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر حضور پرشور مردم در میدان آزادی برای بدرقۀ امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/447474" target="_blank">📅 11:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447473">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1fb342e27.mp4?token=Z7Zc3bEzEMFGnc51Kz5PiJLTH-2acA70XYKkFElf1BLzX6Dj8yny4jGs-M9D2t409jsQiMZ_0yH3kToCo6sDbkh0pVglKf4_vn9pi79brmOHjC3-Oho_tS9KaiguHNBHCn1Cd1ljUHXxfy46KmKLNqIrC0NXYGcd2YyihU5AeFMNe0sh3q4K3ZPROX6m36DwShRRWUHXB2aReoTQMORIKqU1PuBTeTeQ7dXwCLEae58muf_VcvYy4M3WowCwB060PtqqqE5VxmHcXvKdOseUjLv3n12MhzzR4JFJhwzEeKBec43NjKavhbJtIKbk8F34dDrY6f9VNJBNcj_xuzcGzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1fb342e27.mp4?token=Z7Zc3bEzEMFGnc51Kz5PiJLTH-2acA70XYKkFElf1BLzX6Dj8yny4jGs-M9D2t409jsQiMZ_0yH3kToCo6sDbkh0pVglKf4_vn9pi79brmOHjC3-Oho_tS9KaiguHNBHCn1Cd1ljUHXxfy46KmKLNqIrC0NXYGcd2YyihU5AeFMNe0sh3q4K3ZPROX6m36DwShRRWUHXB2aReoTQMORIKqU1PuBTeTeQ7dXwCLEae58muf_VcvYy4M3WowCwB060PtqqqE5VxmHcXvKdOseUjLv3n12MhzzR4JFJhwzEeKBec43NjKavhbJtIKbk8F34dDrY6f9VNJBNcj_xuzcGzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت عربی خبرنگار فارس از تشییع رهبر شهید در تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/447473" target="_blank">📅 11:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447470">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBH61qe7N9ZQuokcad4EN6uCkeZ28IHy__A_vmfdMlG4FOGYLtuWO2m10-z0Qqv74bWGnOT6VkbeC7XpuKfPmfhPkwY6eHYeRiMc3WBGzXFA9K0tj0tQJ3syLpbyW2C_8AeTtHSBksdVAYyPt8-cesUtskbzxlmlAnhawpRlcXhzbO9KWCmR2eEA3TcEbCGQvGHrjBc6ztjWcEJ3yatQYijplsOj0IG7UG8oW320p9HuQpz9NbCbBSWkv8Zdl-jy8o_c_SL8IoC_WlZ3uJyBQ5DBlezfTVcm_4HnjhTcjK8q3W33-ioYbSCrMeWRWnrMJtpLCo4SoSV_hc0G0J9gvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPnMxMcXd0BuvciBEzJJj67yy-MO4T0ORWD6ASwfFZar03dtBsqQgf7VnK7OjGGFqurQaCe86obhXx9Fir-LxrV_3Y6UUUQOwg3zA4qHY7qB2VyVvwpcL0Q317bXiaZAgZfYFswXLG50oZCNgatDY5cEboo9SXQkGcTIaLFZYw1rnpMK8P3qASRhSq-yWN5YDVxUNu9UEYgJop_GqXgoPmDvqSnbeT8WUu9XC8sOiHvDNlkmmMnVLpRrsPOniQ8Pb1epsKeY3U-c3RGm2N6bf6MNepUlYQPXSOOl1r3KQYFy5-bPDgmyF5aYD3uOC-FTTXZssh90mCX-OhjHXYJYbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5cf82a8c.mp4?token=p89H9EpkTRt9GIgwjRMt6jcIFS-p7xtdecTC2WpOeO6oOlEQE4RPClI7jpynraQabv8eOgui6yZfTV809JxWj4-H95ebDLUDBU9EY-i6-3r1cPey74LXR_GHJ1hi5wV4w73aDY-E2jA_-K5V58sBNGQajXwsg2BvwVvYv9hY7w9HhPov5fVVW8oe3RhZaUil_Lhvf_p5EEvr5h4N7sl0f-b3NtQ7brrIpQbu_1LL2JY3p4DrfZgpk-8LPWEEEDIBEvEEN5gPiz_eIdMYjW7b6VNREb8-6fHiDkO5jbtU9gbz7wfo8WGQFqGWwtIqCKRPY504O7ck1Xv9x0BNExZEOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5cf82a8c.mp4?token=p89H9EpkTRt9GIgwjRMt6jcIFS-p7xtdecTC2WpOeO6oOlEQE4RPClI7jpynraQabv8eOgui6yZfTV809JxWj4-H95ebDLUDBU9EY-i6-3r1cPey74LXR_GHJ1hi5wV4w73aDY-E2jA_-K5V58sBNGQajXwsg2BvwVvYv9hY7w9HhPov5fVVW8oe3RhZaUil_Lhvf_p5EEvr5h4N7sl0f-b3NtQ7brrIpQbu_1LL2JY3p4DrfZgpk-8LPWEEEDIBEvEEN5gPiz_eIdMYjW7b6VNREb8-6fHiDkO5jbtU9gbz7wfo8WGQFqGWwtIqCKRPY504O7ck1Xv9x0BNExZEOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
حضور وزرای نفت، ارتباطات و راه در مراسم تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447470" target="_blank">📅 11:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447467">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=d7ygj6B04hijt7t5wiOMvfW1X5KK_g4PpOHfiw_UDFkFMX7ew3McTtR7wTQQW4kAEt2PL9YAB7t1YGlUHO5Y6hP9JDnCvhspGNNwIW2Aw7ewS8iOPjklXbugxjOrfDbZGyOwEXA6dzSiHx6VzhCsvOaX8lzB2mnGzejaCZy9sjHRofcO46m0J0rHXupzK1SEBxQEEZMFCuegWAhATN7HaFOPXArHQcB4qBxHYzt1ywV2caHvfShCXpj0V_biD3vI8T1HzZow7h1licmQWnS54yXzG5GEVbL2tz-Zju34-wxaZz9aNXg046y4TIjSGwl9-_yo6U1EXxlbk2BHP-RtBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=d7ygj6B04hijt7t5wiOMvfW1X5KK_g4PpOHfiw_UDFkFMX7ew3McTtR7wTQQW4kAEt2PL9YAB7t1YGlUHO5Y6hP9JDnCvhspGNNwIW2Aw7ewS8iOPjklXbugxjOrfDbZGyOwEXA6dzSiHx6VzhCsvOaX8lzB2mnGzejaCZy9sjHRofcO46m0J0rHXupzK1SEBxQEEZMFCuegWAhATN7HaFOPXArHQcB4qBxHYzt1ywV2caHvfShCXpj0V_biD3vI8T1HzZow7h1licmQWnS54yXzG5GEVbL2tz-Zju34-wxaZz9aNXg046y4TIjSGwl9-_yo6U1EXxlbk2BHP-RtBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامۀ نماز بر پیکر شهید زهرا محمدی‌گلپایگانی نوۀ ۱۴ ماهۀ رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/447467" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447466">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV0uug3FSGH_Yy3kZqKKu0qnfQe8iJjLemHixPHP-NUbeV3eKMCZ5ExNXzxJh20shIYjmdElDhYHA80y5h4ywOBi1S5n4PuwVd5XLCS3BGWq_ap1JqLn4_HA-8wib9nPRs6fEZaKoTfbOlMpQAG27J10TfGZ8b9zEcLIoO6bPKvK4nhaNoudGeb1cQOLxQ3mQzht-JYo5inUN3b-7-utWdoBfQ0FIofe0tbVZtLZVzbJgd_kvS5BTtQ3qDauA6FrCjT6Sa3x1uNSKtxh0ntG3kD8bkSfenrN1d8YANIgcWo-RmHrboVdvI-4n4OiQUzepU78WYSCK5SM1thlIBY_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور مخبر در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447466" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447465">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f531ef0c9d.mp4?token=eQFc-TXF1DS8pnps86G1455WMIIynUv_O2K2mpmm5JbOgd-9S0y3Hf71qYKPt4Fx2OpPn6l0B3DkFTuP4-EQ7cvKp8uCws4TVLyD-n4ArVD64LIkMYkzM5xDzuW3uhuqLCNuaANusAs8SDUNfWZfa_amx2wrxKs5g7Y-gK-NQH-7rjnjJDR3Mcazu0uD7kT7SSa2I36zETrkI7EBpczMXcsF1a_UiMb7HACaJwb0fbyXLelfPsJxRyCU8dHCdtUpjO3MJoeK0kN4zVfYBA4kNRM7ukd1trBu0HJkt8EiL2OgVr7pHvxVKJ3JHfhWBH7UZ1u_9SG4FIlQ0ReG2ZJPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f531ef0c9d.mp4?token=eQFc-TXF1DS8pnps86G1455WMIIynUv_O2K2mpmm5JbOgd-9S0y3Hf71qYKPt4Fx2OpPn6l0B3DkFTuP4-EQ7cvKp8uCws4TVLyD-n4ArVD64LIkMYkzM5xDzuW3uhuqLCNuaANusAs8SDUNfWZfa_amx2wrxKs5g7Y-gK-NQH-7rjnjJDR3Mcazu0uD7kT7SSa2I36zETrkI7EBpczMXcsF1a_UiMb7HACaJwb0fbyXLelfPsJxRyCU8dHCdtUpjO3MJoeK0kN4zVfYBA4kNRM7ukd1trBu0HJkt8EiL2OgVr7pHvxVKJ3JHfhWBH7UZ1u_9SG4FIlQ0ReG2ZJPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت انبوه عاشقان رهبر شهید در میدان انقلاب تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447465" target="_blank">📅 11:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c51590d4.mp4?token=fVZQ-Wlc5BDSkRMW7WE2o3kKxYFIvz5phkk0V_EQS-UkLcIjmvUCvlARF1916aBOJeGUv-JZUtyZ-JQtEnWSmUAH_pxqouvqmQ77-TQlsC-C6Bnxq7emwpCRqttuLjjztouqQLr84DKE59CSK7rEO_zXIHjZSnVT-2RCQt10jVGJrvb7UxoLm2ig9o2HLKzwWISU8FTrvySLK0b3WITCDcGPXeQFbA2B_VV6Zu-xgKrI3BC5W_Yfbz4uoSf9uBnUH4ASvxSHzY6LrImEi0qQgTNgExFtr2NQFRfEAhUpw7YZf2CLXzo4TlGBz_ddwHkoAxeQCaLtoR5Fs5kMMm46xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c51590d4.mp4?token=fVZQ-Wlc5BDSkRMW7WE2o3kKxYFIvz5phkk0V_EQS-UkLcIjmvUCvlARF1916aBOJeGUv-JZUtyZ-JQtEnWSmUAH_pxqouvqmQ77-TQlsC-C6Bnxq7emwpCRqttuLjjztouqQLr84DKE59CSK7rEO_zXIHjZSnVT-2RCQt10jVGJrvb7UxoLm2ig9o2HLKzwWISU8FTrvySLK0b3WITCDcGPXeQFbA2B_VV6Zu-xgKrI3BC5W_Yfbz4uoSf9uBnUH4ASvxSHzY6LrImEi0qQgTNgExFtr2NQFRfEAhUpw7YZf2CLXzo4TlGBz_ddwHkoAxeQCaLtoR5Fs5kMMm46xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور آیت‌الله جنتی در مراسم تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447464" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8044130594.mp4?token=YmRceDteYs44BYH44FC9ouFs3rwZ4jKBZhRu0IZnol41E6wV4gqLKnlNysN4vlutz_Fhmeejl230dDT_C7Qztd-q-n-CF4Y9nuITtUeNLcvNqeD2E2eeTg17RhcNbskVd8449S8tiq9M0tUHzg4OLGz6Af4ImrUBefaOQtGgTyIgoo7WcP0hUwWmdD52jRrOW9RuGdw2oEoTCOgNRSjVaS-kNdEkqyuccNLSVsm3_0rfH8LzNO-bU4Exa3vFyq5wkTu3IcbxHHN7guREliJDNqng3oY_i8YBwF4dpgxXMXdaLcGMrSx3tCRiWzB5SnR0rEl8J9sfKdL7a1WYU7yaTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8044130594.mp4?token=YmRceDteYs44BYH44FC9ouFs3rwZ4jKBZhRu0IZnol41E6wV4gqLKnlNysN4vlutz_Fhmeejl230dDT_C7Qztd-q-n-CF4Y9nuITtUeNLcvNqeD2E2eeTg17RhcNbskVd8449S8tiq9M0tUHzg4OLGz6Af4ImrUBefaOQtGgTyIgoo7WcP0hUwWmdD52jRrOW9RuGdw2oEoTCOgNRSjVaS-kNdEkqyuccNLSVsm3_0rfH8LzNO-bU4Exa3vFyq5wkTu3IcbxHHN7guREliJDNqng3oY_i8YBwF4dpgxXMXdaLcGMrSx3tCRiWzB5SnR0rEl8J9sfKdL7a1WYU7yaTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد لبیک و انتقام‌جویی مردم در وداع تاریخی با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/447463" target="_blank">📅 11:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8P1w_5UZ9_HsYDu4I1nSe9lUu4R8UUWkdsdr8Rgf5AkqEGT2L9ceij0NLmYBla8XKdusnR5SskDveESNCcwn47V2r_ARUqP9Y5fJXuGQNzx1SeVcmtEg7Pqqm5jgaRi3KTOznUJpDqjUtP6LJWee32uZB4XKHALiIoLYkpMot6z3TOiSyIxIrGVF3Odj6t4GzMXtYMrT6G40NfkLVxI6xZ-CqYWnR0ER6-x3dxvdkvYwev_VXuKru8rnBR7z9R2D5-j7Gm88B-VTAba8kRRMdUeF6PEcLPxa-SeqHNYq7EYGNq9KjUh_YFMj7XpD82owEo-9UmiIuCIg2_6viH1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور رئیس سازمان انرژی اتمی در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447462" target="_blank">📅 11:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEhz7mo5igjcLTNHce5JdpWhIC70i4f_v12-dZszrbAK5RKQaBo1qnGUH2Ezs7kb4HEQxnWAO4veH7GIuTWRBzfRW9SnD8cpO1r_GAF_YYLiui1Q0hHturFuDzEIlOMqYqwR-rPQmKFqYmjn9oDWz3wFaMu2lF5TfG_uDnFPuxGkE1XlF40DNISmP4S8MEFwNyda88UBpGY45riC3JRSgSmrtPKVLGashHxFceMTO2eE32zEXZn61m6EO5DRPSTLWVKkkvGReF0YKfECTcNenawxEjXLrfHa9WfhD6Ay_tFOogX9-T4Zgjslk-ocGhu9rcGepnOtThWT528RLw6u8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شکوه حضور مردم از نگاه دوربین
🔸
اینجا خیابان آزادی تهران است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/447461" target="_blank">📅 11:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4ccb9859.mp4?token=Ur7LZXYXcqjZJp63sgJCQMaThO6N4TBZb8KFna0i-VfIU13NNqfQ9KNMdT5xXnerFCG1qQYVrawNJ_jHi6p_42KeGJabETVJHC72H0k3bxQM6zsUf9H_kh-E91mBYC55OxyjpFy7jxtgQqPWnkhJ5rdbI4OcoapbpaX88D-5jLmr42DtBm-fK7j9VCafM-2qLTIsQ7orZIwMJddahNdfy0V4ZgXE9ltbBKX-zDc6Goa8S75-ON2vuyIqoIMk3boTSt-oNYGK40s5s-vNXqkhU7Oop6AuqybewbTocRHmg_XiauhgirHSFGWAxHoTeAO1x4Co2r_gLjuZesf-IE1Ouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4ccb9859.mp4?token=Ur7LZXYXcqjZJp63sgJCQMaThO6N4TBZb8KFna0i-VfIU13NNqfQ9KNMdT5xXnerFCG1qQYVrawNJ_jHi6p_42KeGJabETVJHC72H0k3bxQM6zsUf9H_kh-E91mBYC55OxyjpFy7jxtgQqPWnkhJ5rdbI4OcoapbpaX88D-5jLmr42DtBm-fK7j9VCafM-2qLTIsQ7orZIwMJddahNdfy0V4ZgXE9ltbBKX-zDc6Goa8S75-ON2vuyIqoIMk3boTSt-oNYGK40s5s-vNXqkhU7Oop6AuqybewbTocRHmg_XiauhgirHSFGWAxHoTeAO1x4Co2r_gLjuZesf-IE1Ouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلباران پیکر مطهر امام مجاهد شهید در خیابان آزادی تهران
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447460" target="_blank">📅 11:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srSL2FPEkV0DUpya8LxeGGRo_yTzFeDmjGG62I7dyLsFbdE-rUTs0qFBtd8VH9vbqluCdtMqola4xhF-w04f_G9H26yTl4wZXLGb_RQ7clY0z3ANvSnFROdG4IXmhY1ybGDRzUD0yhjhwE_0aOR7Nh4yC1h4NylSxvvCCU6OzyOuacUTUdwR3NJ64u5-IIo6NLSkmtwpwg5kxV3Fbx-yAVZfPvopPO8iDxhclvoyXFJjx4LVPvTnk7_FFSoOyloLpJR0D0nAEEn26oHvbNgO22xUxHyUxhepdA45GFJRf68RUUFJAOYzQRwyD_4_NhI33QQ1LEeEBPQFDBFgvnLQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تدبیر جالب ستاد برگزاری برای جلوگیری از بروز حادثه در مجاورت کامیون حامل پیکر
🔹
انتظامات با استفاده از طناب و زنجیره انسانی، مانع ورود مردم به جلوی کامیون می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447459" target="_blank">📅 11:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e634dea5c8.mp4?token=nwMvFtbt4ZV5VcR3XCoQRdvaCLyyjBzNu_Q6MIH--3N9qLHJssDXnKHzceKv17aFGU4JrMfCzvat_PmNZC8TNy30D2kyoNnImYBG8CJCfGUyA1Nf6sOLzxvggkYMn_lUMMJYNeu-TR6YxsXVOFwupOTut0cIbRwx4ZjOkR7TPXkERKap4P12raBofsA6Xa-sKN-yGidwb9zSjRPwISM4IoGlUzjWzzneFFVoNUio7wlcf6WlgLwYlJAWza7_rpssMC-kH9x-MUclueNKSP6devyxMQVfa9Q4s91GF-TkSGbEAJwQfo7bgfnvhKOjQC_WE68EoHenAyJplz2BjZyWzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e634dea5c8.mp4?token=nwMvFtbt4ZV5VcR3XCoQRdvaCLyyjBzNu_Q6MIH--3N9qLHJssDXnKHzceKv17aFGU4JrMfCzvat_PmNZC8TNy30D2kyoNnImYBG8CJCfGUyA1Nf6sOLzxvggkYMn_lUMMJYNeu-TR6YxsXVOFwupOTut0cIbRwx4ZjOkR7TPXkERKap4P12raBofsA6Xa-sKN-yGidwb9zSjRPwISM4IoGlUzjWzzneFFVoNUio7wlcf6WlgLwYlJAWza7_rpssMC-kH9x-MUclueNKSP6devyxMQVfa9Q4s91GF-TkSGbEAJwQfo7bgfnvhKOjQC_WE68EoHenAyJplz2BjZyWzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید آوینی اگر امروز بین ما بود...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447458" target="_blank">📅 11:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u089UYvAZX_XOLEnq0Eg9rIpwXKrtIDDe6tfUb_D-_JV6ZvqRFj_fZbh39fnqTSeq8NBGTKT3ySYLAxlXp46H8LKMsjJ_4KXjLjJrEnUcXDKv7vkPdljf8w0NGex_lKDp6dLozsfMSPK5d--60mo3kiDUsdl8EAc-NZhfThLOfALtK3G17fPrhuR8vUJgfr0ZIyOrrHhWZ5CQ9rf71RBUycUiUR8KPb1RII80OMhNKoQ3MFC0EpP1AJqsQhctny3adXYe3wxxC-s2nvcLkf4qceM0HtrsK4F2unZRfPnQ65GtedDVxvXE8Nu9rPL1hbmXLrdMSZ00oKw85ibx8qSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: رهبری شهید به همگان آموخت که بزرگ‌ترین سرمایه ایران، مردم و وحدت آنان است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447457" target="_blank">📅 10:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=mIfJSkE5wc45de2LVCWVSWsndGm7vjF2ThAm35LwAJV8JwkssGSEafAKVcH7M6FQ2A4x-gKpN5WSOGKw98w7f1lUmrTlnszD3lucy4pztx-NipySU3qxbR2LnXMoJvUdRczmyeULr4dDiEeiDxexaTx5Ybg0w2Ojlcbayb4lVqPyqRShDh8HnWjKl03qhlpcma4A8uZGXCsjq6ZgFRVh7TDMkmV1W0XOavMq-rEAAOU9oACVg1Jf1D10JVbsqGM9OStlBZVH9_kvI2AYHnyeSOPNkxifdVCffGk2FbJTIeRKyvg8ia_-HmrhY0PjL62YmCwKi1Auw7BGsZXQcLgg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=mIfJSkE5wc45de2LVCWVSWsndGm7vjF2ThAm35LwAJV8JwkssGSEafAKVcH7M6FQ2A4x-gKpN5WSOGKw98w7f1lUmrTlnszD3lucy4pztx-NipySU3qxbR2LnXMoJvUdRczmyeULr4dDiEeiDxexaTx5Ybg0w2Ojlcbayb4lVqPyqRShDh8HnWjKl03qhlpcma4A8uZGXCsjq6ZgFRVh7TDMkmV1W0XOavMq-rEAAOU9oACVg1Jf1D10JVbsqGM9OStlBZVH9_kvI2AYHnyeSOPNkxifdVCffGk2FbJTIeRKyvg8ia_-HmrhY0PjL62YmCwKi1Auw7BGsZXQcLgg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ میلیون سفر با مترو در کمتر از ۲ ساعت
🔹
همزمان با آغاز مراسم تشییع رهبر شهید انقلاب، در کمتر از ۲ ساعت، یک میلیون و ۹۷۲ هزار و ۳۲۸ سفر با متروی تهران انجام شد.
🔸
به‌دلیل ازدحام جمعیت، ایستگاه‌های میدان انقلاب اسلامی، تئاتر شهر، دروازه دولت، فردوسی، امام حسین(ع)، توحید و شادمان موقتاً تعطیل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447456" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447454">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRO2f_0qLCbZ7NBdDbEa6Ib5Z17ROFd9yd2SDMU5aoUnzVeJJRvjq5Mv6HJOIYTCJBGi7KMlhbUU-ndKmdVVMzFXH28MreojNigj_iI8WMH-RYMJsSufA_z3sG00fzcAFdqtQApBl8TEq_drK8UgT8mYYdNwz0PypPbGmbMj8Vvr7rJjRXynBIdNXHpT1uhyncKF7W4sSQZtvoimmzp0uKAIpfePaihidWgXC4oxRhzsT3BLEU0y9lHDf_3TZj8_-yMbdzSH5zu723ogiMmrAakFRxDRqOhZnQJmlFEeVZ7Hk1jABnqEgeAXd_-eR094UM635jHNFjE67e7WlJ4Agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMwXczyXnMka_dK-P2p9Qih_F8hKdTK1e43f20pk3ja2uf6vWZFGTJVsRMoDzYTAd8QHoXhjBSTPONC_EVTEzQrdKNHF6NWg4UFuVoFExO-w3N1U_Jbr-i8ZeQmfGVL9m-b-8JH6vx9XpSGGzzzSs4H_nE3eR14B9QjiNOXaAhmxNB02nFC6k9ROFkv-SD3Pp1QslPZA5RU8xflW1bzvgWQQ-9naT5ni5VSNU0naKNnXijcya69ocp9xl30F07BSweoaglv11L1UqcWYwDenvOgrvOXAIUwiTnMSlVSGFvsrlygbAzpXON3s9KGJbJJftsq1s3Rt7AV58haTvocdxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جمعیت پرشور مردم در بدرقهٔ رهبر مجاهد ایران در خیابان آزادی
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/447454" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447453">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEDeSSPI-6mGEoOVPX9PCZmZOPwdrGPaa4fDnyE3LuEh3VSewFdQUT7OZtTK-eJD0I6lXPOf1D_MEpNk28ES9t72JnMRlnwzvB6h1XrkGml5tRKYAEVcNVKo5Wk9LuoQL4PCMl_cJruzPqdrChtw1eUwiAm9QDWrhLo-mW2zdpa7_qh5H7sdIIlhwmYE0dhyLhQISfksoxRvE1Svc71Y5rynGYZkQAoiDzjvvbCJtB6zp61UAx4UAr066IfyJM8p4hc7k3uzLgm6KF4KOBxLE3BoZS8PU9pViCkZPv-9LQlYXBMus1nYBtnTma1FDjqt-VYKOXmCn2LaLzB_l12qnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور جهانگیری در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447453" target="_blank">📅 10:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447452">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRavWUQqj8jKhVeTSeyvM4aMO6rftVX4IO4qiyczXMQDFuzPxOqXGshpln5oSfd5Zg2f1KD7coxn4Qq-JL-F30LkAmm8JEFIM8k0sWGYqqid1tznqXqTYfEChV1QdAvi-cR_W53KzUFTODCSRXsP3g8G7Hmw-JV3atANG7mo8rIdzv8f8XMk1BixTyly5S5BTVXMGqYEBjHMxC6RTpOO7WjyNfgWep3_QUJJyF6a4yjtUh0LdY1on0LxOe45WVULByrmfBg6uaRLVioHRrA5ySUqQl1lSQVyBgRY2XSqSRg-ovq4k8p34dXXXBMpsLHBi-nZoBOEVgy9hjJO0Wbxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برپایی ۲۰ مرکز خدمت‌رسانی همراه اول در مسیر بدرقه رهبر شهید انقلاب
🔹
همراه اول همزمان با آیین بدرقه رهبر شهید انقلاب، با ۲۰ مرکز سیار در مسیر مراسم، آماده ارائه خدمات ارتباطی و رفاهی به عزاداران است.
🔹
این مراکز با هدف تسهیل دسترسی شهروندان به خدمات ارتباطی، در نقاط مختلف مسیر مراسم شامل مسیرهای شمالی و جنوبی میدان آزادی، تقاطع آذربایجان، خیابان شادمان، خیابان خوش، میدان توحید، میدان انقلاب، چهارراه ولیعصر، خیابان حافظ، میدان فردوسی، پیچ شمیران و میدان امام حسین(ع) مستقر شده‌اند.
🔹
این ۲۰ مرکز با پشتیبانی ۱۰ مرکز دیگر، خدماتی نظیر اطلاع‌رسانی، مدیریت سیم‌کارت، راه‌اندازی سرویس‌ها، شارژ، پاسخگویی و رفع مشکلات ارتباطی مشترکان را ارائه می‌دهند.
http://mci.ir/-NJ1Z7C
@mcinews</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/447452" target="_blank">📅 10:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447451">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx9EWW0xrz5oZ3ZoQDRsE4LlBvHrIWalLcmEoz6-NYXB49VhwU9elVdw5Hs0D2RUr-JCus5-lUoE4dQqkiT4Udog9biOrWLGZBkXsXrn_VHVS1VO-T-XoeXEC3pEL4jTlk8OR4Em4zKJgvMneNxteSHndfhXdWSFYlQr0C8fCXcVACm7rkzbg3nnUQyaI1lRertkP0u4A-hbUr3tvNaTBmSRAtNv_1aLnPDMfpECoyKooWlyOl2qD-VmpW6Uwg95CNWYILjGC7E-R-ZyuYvDjiaSMUxdI8YjQRBj3N62VU82x4B0P0ZyboZQ3GjLmZTUw8G4WJ-y8NA-jCx2u2CPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/447451" target="_blank">📅 10:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447450">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/447450" target="_blank">📅 10:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447449">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544f106e.mp4?token=hExuS86_oftydPT9FfW_7hY36WaLY7Vp57Yo-i983oUGFq8bo4E5psj8rm8AjCVNbjAiHLITH73DtugecqzM7f5bclzjNZ0mfJml5K9_tb7srAblxczbxGwn3nIAhUIexF-5wWuAV0rMj2kBOtqdcxPUpGDqNMvP_3bq6v21cNQmmOIJp9_Vjm3JWraLgV_ZYYtgsOuNMtgsjhxfTejB5lGfX8rnCKqZ1ieMy1MPLfHiHNu5GBPDsBuJ5xNfIcjaPWFqVs3LGR_cvGEf66WZvwd22Nc6MdrcUzWjqg_i01HrbiKuyXmh48q5x9_yl-9gq4oiP0zUVK4HF8ZasgYRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544f106e.mp4?token=hExuS86_oftydPT9FfW_7hY36WaLY7Vp57Yo-i983oUGFq8bo4E5psj8rm8AjCVNbjAiHLITH73DtugecqzM7f5bclzjNZ0mfJml5K9_tb7srAblxczbxGwn3nIAhUIexF-5wWuAV0rMj2kBOtqdcxPUpGDqNMvP_3bq6v21cNQmmOIJp9_Vjm3JWraLgV_ZYYtgsOuNMtgsjhxfTejB5lGfX8rnCKqZ1ieMy1MPLfHiHNu5GBPDsBuJ5xNfIcjaPWFqVs3LGR_cvGEf66WZvwd22Nc6MdrcUzWjqg_i01HrbiKuyXmh48q5x9_yl-9gq4oiP0zUVK4HF8ZasgYRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در میدان آزادی، منتظر آخرین دیدار با آقای شهید ایران
@Farspolitics</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/447449" target="_blank">📅 10:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447448">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW-TdWJB4fulpI0DX6W79TMqQFCyznjUWXmRcREY6e_88KKm9OtFBUW0tKPD6bKR2IBGrOZl11cCL-AUCzoGw6ST94bYLe8ZiX4AifU6L6Gx4GWWpEJoWzuHkbsOOUK2dvF-Nh5wVJSP2ucbS_qbQANNANTmBfvDpaiZ9qoAHjKjefrB8mR6uKIXnGLADRmV2Oi7nPU4jlU09wUAIqLzcBzW8_GAhwPgYHouRxDDAWWzmameqIEAiM6dsxZrn7WmQdjmAzq4eFUWgmPEPUzjaOSvlQdePyCsQRKnvgXMI9eyz_jpFWujm1o9V44XxSnc8DXzUNK4klXewEmG_gQGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تشییع امروز آغاز حرکت یک امت داغدار است
🔹
دست‌نوشتهٔ مردم در بدرقهٔ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/447448" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447447">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCCpbGf__RjhbLrRYYgKIiLLkNCo0nIT4SZLMG-5dE7tnuE_U5IPiY5YPIjA1w6HKkLE6XlQ299OxdmmBH59p7avdKUDEZJZE9-7nKXr-X9zGOiBJ1W4xyh5iDrxBrCZ7S7zZ6eYgYFc8eZeiZBAuP9ZrE2jOEtDDoHAH9VXrEdajxw1dim14N6k2c7uHk8YAca8r6ldn4djuKb-iVgbv20Y0dwaT_AXH8xQzHeCaM1TFFqaIQW1Wh-AEGlho3bWxhJh6-aP_yfRKjB64coFp612XE7YzAbZ5cpMb9ok8V9lDrC3qhukZEgkNI9Sq5wGMbRtHh0clzr1Xnq-y2MUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور احمدی‌نژاد در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/447447" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447446">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caMSeZPIe7tl4-WY3KSZ8Knia1742a-Ffnt8F6vhU5ZCTIKKYoP_h3wSIt1Hdnc-1PteNTJKJ6_ek6gE7gWIUZH2cNUAfrvDayS1vYC8deppRnHWtK37nv7GC802BLILG9CZQlzLlkA87pDzyoPkdL-LX_OyAnayNIAeOq7KquvHFiCGpWg4dQQO8u33p0Q3LzEmx-61oPlqlmyMLvaYe7PzX-2Yc_zRLawv9-7_2UXbmuDW5hz2CjQODFdDFCAQqrI_CdkUDuBXECBBFe_1GB-jSgJq3ZkmnTE1gAxNaJGNAEwi6VbWQ4gQzHeQCyESJwRDldakVhjNJZxuIPHr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف ‏خودروی حامل پیکر مطهر رهبر شهید انقلاب در میدان آزادی
🔹
سخنگوی ستاد تشییع رهبر شهید انقلاب: ‏خودروی حامل پیکر مطهر رهبر شهید انقلاب، به‌دلیل ابراز محبت و ارادت گستردهٔ دلدادگان و عاشقان امام‌ مجاهد شهیدمان در میدان آزادی متوقف شده است.
🔹
مردم عزیز عزادار میتوانند از مسیرهای اعلام‌شده خود را به کاروان شهدا در میدان آزادی برسانند.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/447446" target="_blank">📅 10:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a768e4b8.mp4?token=hM5sG6bMN2LGOXa5z10md49jbB19NQexusSXMcjA1vhUEUwNH_4Bn4382RlsqVeiwyVLLTXnBOCCUqsHq2UdXQZ_Wpem5fAAKAL6iGF-zipuGTBvlJ_KiaTKf3Zo7Roo781908FSR0aeX8yy__lYzrhxmrn8qQU9ZSm0Tt4lMvg6Rr2CLAEsrt_hNCct41IwUy9VoInMEjIb93I4vBBgU7clZhhy-Tv3q9gVAVjREcdP-NTGZ3F58svMP-B_9e1WbrOr823-briC4iYU3xq5G4ThfHdr6_QqbD5fwvSVkyPCf4pFEVQLIoOjqtjWJ9AfRgJdTohjsJdpmUEeZgd-44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a768e4b8.mp4?token=hM5sG6bMN2LGOXa5z10md49jbB19NQexusSXMcjA1vhUEUwNH_4Bn4382RlsqVeiwyVLLTXnBOCCUqsHq2UdXQZ_Wpem5fAAKAL6iGF-zipuGTBvlJ_KiaTKf3Zo7Roo781908FSR0aeX8yy__lYzrhxmrn8qQU9ZSm0Tt4lMvg6Rr2CLAEsrt_hNCct41IwUy9VoInMEjIb93I4vBBgU7clZhhy-Tv3q9gVAVjREcdP-NTGZ3F58svMP-B_9e1WbrOr823-briC4iYU3xq5G4ThfHdr6_QqbD5fwvSVkyPCf4pFEVQLIoOjqtjWJ9AfRgJdTohjsJdpmUEeZgd-44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسهٔ حضور زائران در بدرقهٔ قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/447444" target="_blank">📅 10:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0171cd7cfa.mp4?token=F7RidnSeMGL__-uwrxqLCDL0e4hJQbC9e3l-i5IWEum3Y-Cevsp2tvOLdTBpKe4bP7hnCNumFXhRXKkq5g6t-xgk2HqfLg8QXnEyMZ-YICyy-6MGnhzVs1aRGK3OyUhayOylsTJiLZTkAs9wHiQvn696LFnRHZzxKQ6CoZ9NBwGeeIGPdrDxs_jcIWTUs_NvvAjiMNyNV37g8MKSw7SWiiyIGC0Jl0rM9uw-HTF64GRJrTgkp-yWnYiwCE0aI9rRtS2txDapdszt2yEluLop_ow13cppsADSUZtGXqwuxiYtIHNlhro6TCzduk0XavHzo_ZwWR27w5Rhjmq4o_djpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0171cd7cfa.mp4?token=F7RidnSeMGL__-uwrxqLCDL0e4hJQbC9e3l-i5IWEum3Y-Cevsp2tvOLdTBpKe4bP7hnCNumFXhRXKkq5g6t-xgk2HqfLg8QXnEyMZ-YICyy-6MGnhzVs1aRGK3OyUhayOylsTJiLZTkAs9wHiQvn696LFnRHZzxKQ6CoZ9NBwGeeIGPdrDxs_jcIWTUs_NvvAjiMNyNV37g8MKSw7SWiiyIGC0Jl0rM9uw-HTF64GRJrTgkp-yWnYiwCE0aI9rRtS2txDapdszt2yEluLop_ow13cppsADSUZtGXqwuxiYtIHNlhro6TCzduk0XavHzo_ZwWR27w5Rhjmq4o_djpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت از میدان امام حسین در حال حرکت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/447443" target="_blank">📅 10:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O52iqktQtAOHMLOoW2jJVHHAOa2pnOJYs5-_vxhqEG2liGiZN8jM9ESdNbjRdum-mSo6f6aRKz30_-JTsN2QQE42zI6jvpxGSdiA_JkqJ6CX8uVHpWS0bDoaGkD0bktwlSKM-gh7Gh8_wqBnR95T6Mm0G5GIad98ELvU5cu87AqHOL2CVEbLAwLzWWAUs4eRjmd61qNt-pYAeyRqQoFSvNje_SeYSye4k3nvG2bSA2dI7Yvla-pL37rVfBXnVjtOPW9G-zEQUv9I0BhrOzORfvCDlwlam7RCqSWIK4gWC7k5EJmp9Qn8SV0feBvzsbTpnKnHCFFQeqfL2NXRmWd-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aebaj0fE20YW-62dd8B_-nzWE6ITqTjRQXg-dYQDoCtMoN-EAbbJJ55L0JFKjoWmMomKjXLEDD_nQw9qJuT26YddKr50xUsLS0yJxvvEeVdr5VCqQIXpA-WKlYKqrLL6vRJHKha2ndoxFxSXpkPyO1SMFXzoIvIWdZGYR06VghfAA8Ukxe83x9v_k4bXDecY2MxjgaSXp6zxko9p5A2ih551vO2OiXbVNrHzQk3-EtCl-7nEuTecAvFPpg0jXZVThCXa40XlAJ724Kv16FPqCFAJN9ovnkcvr5Ix0USAgjA5lqUJYxD6J6lOoExenvvI3GDnnRxFUO9jrjcgRYr2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTOd7svqIHlWsBRoalPT_VTJOn6MiKiIhsRY5umNX1t1ED_rIDhSr9vudKdX8A4ISKO2ufosbp1AJWA8LubLSpXYcG6yprsZKZVCei828NhROpG-7l8HcgaXEos-QFGQzHYd8MZubQJdBoeJ-XLjNO1ExoJnZojQz3LtJA0NCJbbeeaxt9y_fBwroLrHGvgTnhBAGmw3sKfzQPv2rEB2dqDDAmWn0q7xyjJXzRmwzhfzNIwJHe8OQQSBct-O0aDT2bjbwhCa1HqXCVC2FRdmXGDPzXY-CFLyXNiUiElzdqgds_moQNhD2H54Xk6ksjTIm2fs7Va98hvxnA5V4Kwk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SP4mxxKjkx_swky5D6njLyFAc4X65-atQJ-yg2NL7b8iMCgPVzvHK1_URv8L_LB3fvZD4rgEcLrorrMyRCkP1pnRQrRMgpiqS68g5CmeUxKnuTG-fI0l2qWDBVWqQYzP9Z0rMHXobNT7FCRcLOGM6XI5JtB0DX6WzrszHpPFcU248Pe7Ia8fW-1-WaOD-QctgytSfnnYvI4GO_sn-vCFJMrPajAEm-fB5j0grYemf2nq-t_Vfj28DwtKfCFS8esmZIF7VwkdqNjQ4nMfGcqYQv3aMmgLpgtV9TE9nghhyb-7PifYygL0jIkChSTQnHaeCTgNHaZkzo94RnKGRE8B2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlqx8ysGlxNHrZsePBQOPLkETdsHXU4mvoeCYperrtKgR6JUYUUASvhU_aPRRAO1Si5WyxU4w6lxkMQGRDKtsXg4MjbihelM-ktuUQ6f0yNSWt8hWQdM5QUrEyGW10M2SYdrDKnU8y0le8rqu4JOmA53azJn38rttXyqXsmtBM4072S1UtG-NxPmVuFkkWjnmcoISYcot0musrpuEX8C6ykZGCU93oZFCsdvVBpkdFc28jr-p24fMVs8CFMlFPF0IruwAT_m8ZVQpCjnIuv6Kf6b2CbgJ7R1bk2BF15IpC_ZBsl4_au8JAWnhO7SHfgFoTJhv9Qs4SnW_97LuDuPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JmaZmSelW7z4zuwkfBvRLmkLxzpwaJeHDQbloQ75nuVUKYoaXYMjoDUquZUF4Mk2edEwpKoBcwQviElzijn49cGwaFaASZHwMNFKraJ48zDbeRIG2iy3aEHueQff62NtorCmreRn5B8zy2gCrQYP-Zzcz1FfuMi7u3YluhlffjhC9DsxkOhvi2iw162irBbhkOo7nvD6hkSLTDUXXgGAMMAgfPuK_2lHQqDYc7wCnAv2mBBltDraDXwM-FXmcOdpHRVH7GKrfeyIGv0EjfJmsRUkRauyzhKo3UXW-HmRD01ocCdDws-6nBMwnIPRg1aITWRe5EshhO3iarWyqxvXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mabCx6ADLdBYmIELySonCRbXZA9m5dFH9NbnBi7vGlKR6sEZBkgC08vnivBeoCB2igNV6Tn2pOgrsrm-fZetoWc4ruG8cD-cV4IvW2tBEiotEAffLXJ-UrZzvW82BopKevLtr8XLYdDMEVJ4sRP28iRzzBJxhnFZiKq9Nv8ezKY_im9k2fvpfBry03KQP7Nn_PT9fyhjne5s4RcECwNR8ZxBVwx7jQ-XFBxPbtUKo6PJT3VpCyj8oj5KUhGE_N8ikvAnODTyvPCPN4q9y6k43_txE2VR7SgK44w_mDR0J-OWOSF7SL_4QfXaYuNO3xMt2j8bHvsp_T8GkpKoWkN0vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هم‌اکنون؛ تصاویر هوایی از حضور جمعیت عظیم مردم تهران در تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447436" target="_blank">📅 10:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8004c00f8.mp4?token=lRjVAHMuBfO0t8fXj44ZHbGWLj7C4VllBMY8AGHGloa5rrL2ReGkXtoQR4tDdoAu7D3b4cUtL7I_IO2KiIvBf2DGZweIDPspHWDk-N6igKdhHXf4FABcg4pT0XRxJLZb8HfHvX9O660uvNMqmW9wiRAxg9iH14VMe6WqOWwZ_1h-sjD3Hzjr_0VIT4Ds3JalUvUKUXp4N0KRH3S2JIprlkG6waHhaNfbdKienHgmBstXw12fNVr26hrrzWSwQkqz3IyJ8jPjbju_HFcni2PSjRhAqN1bC_Xngq64Ss-1V1dttIHAkjFxLWjvD6vOcwnRmZVBfP8BRAeWPVDc7Z3cig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8004c00f8.mp4?token=lRjVAHMuBfO0t8fXj44ZHbGWLj7C4VllBMY8AGHGloa5rrL2ReGkXtoQR4tDdoAu7D3b4cUtL7I_IO2KiIvBf2DGZweIDPspHWDk-N6igKdhHXf4FABcg4pT0XRxJLZb8HfHvX9O660uvNMqmW9wiRAxg9iH14VMe6WqOWwZ_1h-sjD3Hzjr_0VIT4Ds3JalUvUKUXp4N0KRH3S2JIprlkG6waHhaNfbdKienHgmBstXw12fNVr26hrrzWSwQkqz3IyJ8jPjbju_HFcni2PSjRhAqN1bC_Xngq64Ss-1V1dttIHAkjFxLWjvD6vOcwnRmZVBfP8BRAeWPVDc7Z3cig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش جمعیت در تقاطع بزرگراه یادگار امام و خیابان آزادی
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/447435" target="_blank">📅 10:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447434">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9910a7d906.mp4?token=NtgbMRYnQ7FyphQ4CYRIH_e7pGWgiFc4fk6PYBEDroOeYDiysj9pLvqZGiJEtWcXP_07TfmyDdmYrCHe7Lr9j-XwbQseC1xJD999vXNlH6CwHxjlKbfuKdmMm3pcVXzMwLRnlzx2LXYNhprSttWCCpPxaVT0iilNwNF3UuXGEgF1jP_U8Bjf0reXVtId4WgPAYtiTJfhkdxJJp9l1DB08j5qG7oSoNrpA5JH5EIp9gYFgwZceWaiw0JpNzJK_4m10qgQtKiP_mjCVdZDUIaMhTYBOhHu265OwqQAk8qUoaCWi1ftpokmtD_RfnL2rYgciZRUXw6AFPJePQBWyCPi_Ylqy_ArE_1LxXcAi6SRM9AfvUA4yWrYNLd428vgb6Tmt2NYdN_yPiTzeRMl3fafI2sTx38uT2heNL_WIs7stTTJUaZP97Qplu18IlBuj42hjyGLXnUnWpaKzY9NkaIwtZGhAtSejoehZOLfsltjnR68xqbBkD_zEZ8CHveYF24RMGahWAGAztqb6WKUeH6moUsWXnzxCc2y4nAQ1g76MmvV4x6uVBT6LKVVUqnxofAls_fwz8_HIhI6Qtf-PUo9olNRwnwshEFfPrDIflEAFHeC4AUWfrFbildpwm378owZI6CxeA992HgxKYJ61BtxaPn2J65Q4N6rZCkPEEONJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9910a7d906.mp4?token=NtgbMRYnQ7FyphQ4CYRIH_e7pGWgiFc4fk6PYBEDroOeYDiysj9pLvqZGiJEtWcXP_07TfmyDdmYrCHe7Lr9j-XwbQseC1xJD999vXNlH6CwHxjlKbfuKdmMm3pcVXzMwLRnlzx2LXYNhprSttWCCpPxaVT0iilNwNF3UuXGEgF1jP_U8Bjf0reXVtId4WgPAYtiTJfhkdxJJp9l1DB08j5qG7oSoNrpA5JH5EIp9gYFgwZceWaiw0JpNzJK_4m10qgQtKiP_mjCVdZDUIaMhTYBOhHu265OwqQAk8qUoaCWi1ftpokmtD_RfnL2rYgciZRUXw6AFPJePQBWyCPi_Ylqy_ArE_1LxXcAi6SRM9AfvUA4yWrYNLd428vgb6Tmt2NYdN_yPiTzeRMl3fafI2sTx38uT2heNL_WIs7stTTJUaZP97Qplu18IlBuj42hjyGLXnUnWpaKzY9NkaIwtZGhAtSejoehZOLfsltjnR68xqbBkD_zEZ8CHveYF24RMGahWAGAztqb6WKUeH6moUsWXnzxCc2y4nAQ1g76MmvV4x6uVBT6LKVVUqnxofAls_fwz8_HIhI6Qtf-PUo9olNRwnwshEFfPrDIflEAFHeC4AUWfrFbildpwm378owZI6CxeA992HgxKYJ61BtxaPn2J65Q4N6rZCkPEEONJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر شهید؛ مهم‌ترین مطالبهٔ مردم در روز وداع
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/447434" target="_blank">📅 10:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447433">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
پل کالج تابه‌حال چنین جمعیتی ندیده بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/447433" target="_blank">📅 10:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=lGIU65J3qQM7E4ENCrT5XA_zMUQ89vXGect_l4EvaQHfCGDBWwjXacU7CqXJN9BirNfnnhSTegJVDo40CGsauNNZLPnhVcjp8jhgKGsTYxipSchLmxucAi-p9e5UOVisYoN7Ps98O10pJ4AOOE_maHwz-RKGpKdmVpa7_LnGx6Z9g-dfb8UVyCx3OvNDlR5AuRAT4AigB0IWhDqGwKucYXZxJP_lVItjt5PoW6ixMPvWlz2xIRm46sTzXfdRe6jKVhdQqNJdpXu4UHMmwMsd5cLSd5DxBaIakPGGYWQWDFgRA7el_8qOX-yflFP6u5gha4ZaKwlnQqJRpMl5ib90NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=lGIU65J3qQM7E4ENCrT5XA_zMUQ89vXGect_l4EvaQHfCGDBWwjXacU7CqXJN9BirNfnnhSTegJVDo40CGsauNNZLPnhVcjp8jhgKGsTYxipSchLmxucAi-p9e5UOVisYoN7Ps98O10pJ4AOOE_maHwz-RKGpKdmVpa7_LnGx6Z9g-dfb8UVyCx3OvNDlR5AuRAT4AigB0IWhDqGwKucYXZxJP_lVItjt5PoW6ixMPvWlz2xIRm46sTzXfdRe6jKVhdQqNJdpXu4UHMmwMsd5cLSd5DxBaIakPGGYWQWDFgRA7el_8qOX-yflFP6u5gha4ZaKwlnQqJRpMl5ib90NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در تشییع آقای شهید ایران به شیطان بزرگ سنگ زدند و عکسش را پاره کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447431" target="_blank">📅 10:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447430">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGmJ9NMocxU87oVTG5d-B-ffwpzvAubt2DXPIO3a-QPYzipBPrdSpHDGXDTPrsATEIFUBTEJhIL7NkKEmWF0l9g05iwaOwreOszW1WlnMXA0OsDEoVPAiHO-rWniJ8ZdSz8gnRuwC2X7yXgLaAw-Ml2TgOAlBbug2YNSUh6SDh66fCBINVthI5NnScJPnAGeeSBfSOgeJZE7bBTBS57c8bWUNhe4yyWUR6u0PH5J1ndptlslG2E-kZz8-7DsxsQJc4A8UoGfFFZ696yVITy66LREv78w8jCgHE4byVGb42ncTgPtKagNX7T22uhPW8Ve72sk9RYCAzcKHJZG1z69_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور رئیس قوه‌قضائیه در تشییع پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447430" target="_blank">📅 09:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447423">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgXN_1oxTxoGqIFhrW0m9CaC2IwiHPTmIB4WEldJGE_RScIGsEm6jaWjekqggMYRIDS-cx0KeoC22GxKJBy7hBG0DbPiZX9KU_Je7V-dFXpZGR6KfmlC12TYQE-g_Ao5RXEv6FYHcxSU_LdNLVwfwkaTfwtLsVRXmHgcaj34m__0xzKWcZwEw9hGHK5HBKfsFSldMUi771EJW8VWnGdH_ieW1wXj1A7N6axloCH16f_w81ZC5iwknvTUq_S5s3SnJI-CerUCTVtiUsg6H5VEfhlGaJY_jsrY6ivywme1OTqcr3zbpw5AjxExuw5Yaz-kyDvsB5uADkfxAaHIVUGHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzcLn8B3_Jf9ismmDBo5A3h5Dz7ErTs-HDAaEWHNCYy6ndz5VeyCDPn5Y7cbdECAEyABs8Sqw2doUWAsaJQdpqJ5n9ikelVkoAQitMAIofRiaIrE2kDsgYEMzKueoqtddUUva8L75jefWFllLOEeD_SOqJMcSDHrPGzae-Aak7phPDM6WCij9D6u6uHfT5sMqhOs_aFrjMm-uSbssewxDPWNc0ZCbIGiCAAZa4mm0ETS6KwysnXNycR4NDRpe5KRQVJrLTzAqqKKlgm409G9yabrWU2mk-MqYlPC2Y-Ju_kOlVWoOFa63VP25-ayTloT6Du_kwhj3g2TvAFASbaxNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbpRBlwzA8ov7UV6wx1zs02TB_4U64k69iRCrUFHlWt4XwByamK16_k7M5_OTC63URFKw5WUYiDDQv8Jg8J1iQdHj-EOX1wZkpTlkekjkWi4tvi1bifmrz8elerHiVnuuw66SKOA38Cvqju6sTmv7FDAmfRcJi4bpZASPbEaCttpcfVzmd1iufdeSlYnwjUR_4EEIav1jPR2vQdUU58Ry8MPrC9dBMJ4j-v1zZEqWu0yBJA4uilFRUBdd6pZZk9mf5MNHgTikn1BoblIueM_qOVAl9tRCbmvzierhlpFRfDsPEYZ-qd_Uc0E30d9A1NHWVE-sJrRUl4qjP2_Qfi4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1a_geiZ4Gm2ubQ6uQGjmRhfyVhr3ZJpnKY54Lq67lb6BLjX3OKmqBx6clrRK3jIwYAgVN30a9Geo4r0DB-snaNHJcJaGI4pCTmUg6HEd8qJ0ILoTDtYU7JvOEiOmGPpa0P0OBd0JGHAOQVXf-sDTmhaSS61r-cokR8ZX0B1aXet3tw0qnsf0I7sIEg_zi4UBCmGnOlnfFjZXjalEnlcNycjWzTVAoNGbR1BjbmDyPZFU106MCJUpO76FZ7bo4wFwHkxGKjzo3c-Yad-G_lXuoxtNZoBUc6eE-aXpVoqcVGStt1Vx5Y-F6fTROxFj-07HztXmRBOVej_wxydJ0tTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iM4C1HAA0FoFnjv-ewAhh_RR3JHPCJmIqa9-JC4Arw93YARLJ2tiM9mB5eVnhV3rYoQrmrY5wNJvZTmDaeAfyoEogD7PiNsOudZSFZH-Iikoo57cSA81qo1ZLImvo3FlhXEdahCthH0wfboYw3UiyQQChOp-Dd9iOmRZHPUfSEGhTf4H8PFDPXib-vR9n5_z43T6whwNqqzixqQ6wKqjbsTNC_TPwvB0TDcs4tW1qfj-bgFAv1RytaADlqx2temOkYqKvVDyeMQydpthQ7QOaf_-kIB7j4d6vsTSM3RkS3MZJEf0T8Bq564t5FnTVN5aOP_JTSdhSBFIeUh1xssPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gknY75nG8u0F4jc30GDKFF26BYy_Owz0tE3gm0tMGkPl3ULrtQgfGrwl44hJP1pqJlglJb9wJyES-zcRucPvBOAi3cE1LEdAGDjOqOmcxbqsn99_Cu1z8RqAfZ6KC2-jqOb7CPd_fgkwhgdOtECLoaBZI16B_5Dt2cCuDOyk4bPrCeyemPJT1n5CJDoNFUSBBKYapqGkTNhD7c7a5GK9L5kda7jpX7bioNTYALj4lANVU0mSdWU5P7IAXLBYibTl14gR22O3wbyVfVw2MzPXjhQn2BrFYLiLAghUv1z8OoV9uTVYfUwEbhKI2Y5KI9BeLLWvOgblMt0SFht5tIk0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXaGE0vQ4J4iB0eOE5uKYiwjwlQLGbAwG0YmjZePJ9OUpjRb11nI3SdUN3vRPCH1kqWPa98zogFzu5-w-UneRseZq_tFR2MlvNq9gRKOEr66y5ee0eeN9AyD2fVAGjysh1DlsP4OCcVu2eEdOd-2hulWkm-MYhI8zC_LSjsvpibTurKEAIeZbDSGuO07RKq9UReN2BE6in7Wn47Z6Nb8vRdCXUbqiEDWbeZ0IcY7hmtiOzOjs-COSI-Y9Phc2OU_bwk9kihk5JqBH-B7lHJ3iGqWduD3k1AsBATTrcnwApTbzC3ijMpFqcteYHB5wOPWn6f-lYsQMLCS2eakBdS-Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میدان فردوسی سرریز از جمعیت شد
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447423" target="_blank">📅 09:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a28b7dd526.mp4?token=Zwb_qslcJPKt1F_YsL7IuTnPLLpj2pJGxiXjJ1PyBPGOA3faiQt-zCGY3rG7zN6IFs3uCRX9FIp5pCfbkF7Mz-3KujeF6QYTfR8MZ8VvK_DVNzxtd-Va2TS28xPQZRwPa3Lz787120Urc1Ezzi2rQt0LWZ-KFkKFWtZl_tSze8ZbnKACOmS9AZL6rDNoe0Y7Wo35B1KX7NQjjURpL6BiHJokbatAI51q4iKDdLL4nEvC8PoZslIQnOzwuY7V2zlEpm4NKfEUJhXkt7zBsvdoeifSKAxFws3knCr5qy0QsunueRdKPKOVqLC1FRkH08RYdHS3kj9djDtPU0UiQmtJ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a28b7dd526.mp4?token=Zwb_qslcJPKt1F_YsL7IuTnPLLpj2pJGxiXjJ1PyBPGOA3faiQt-zCGY3rG7zN6IFs3uCRX9FIp5pCfbkF7Mz-3KujeF6QYTfR8MZ8VvK_DVNzxtd-Va2TS28xPQZRwPa3Lz787120Urc1Ezzi2rQt0LWZ-KFkKFWtZl_tSze8ZbnKACOmS9AZL6rDNoe0Y7Wo35B1KX7NQjjURpL6BiHJokbatAI51q4iKDdLL4nEvC8PoZslIQnOzwuY7V2zlEpm4NKfEUJhXkt7zBsvdoeifSKAxFws3knCr5qy0QsunueRdKPKOVqLC1FRkH08RYdHS3kj9djDtPU0UiQmtJ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از بدرقهٔ تاریخی قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447415" target="_blank">📅 09:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d24e9588.mp4?token=WrZsXnRQVyxweyuRr4w6eHfUK7sZw1GHhYBCnt4AOLOmbmYdBMHJ0TLsyR2MgaGVvJP_yJVhsM1Lql8SSw6-4syrwW4KPua_tsQw7F37S_4-VtKREA4uXoCmiWt3H66ZcRq8BcOxEcxYACwh0__HEcmBPLz5lF4JBLX6gwGW3StDqWiPtzKAXvk55uHYm-9dwvZUwKhzM0R__snN3_6z45Z1IyOs1LV9PEfuyF2uEOEN_GUAlddWEQ1qtost1dYgWMV6E5UFozrAqw_9reZHRkaEXHRIibPnEJ7FvWy_galETWjE9f-R41g0mj2caP3F8tgrjOnZJDO8nqE4EBWSpTe-C-UdOHt8jshxZhv7dgKS19rqAdASOXU6MinvbntF8_fc-HbpGWelo_x-iTsNUIGMhkC9KLN8tGapNBw4oQwJvP8pkwc_rOBBJ9c6GRRxfXVBUQ756Ib0DuNioBXKPO__lT0uNX8ZNBQv1tcU4HSBreSxveAy5ElupjyBXyT1rMueFLK64ZNGa9kNZXet87jNjW1lCf9n5nMYX5Zs-MBM20qE1G6KWdMZ8OQxZo-WZtTPoSZOzvV6m2HRJiv62GnqSPMkvvnnggt2xA0_8B90NHBJi4UIbtc1pf57FdyPKAh-rnXv2q105qj9nzXWA0s2_5a-XiASXroSkORfM0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d24e9588.mp4?token=WrZsXnRQVyxweyuRr4w6eHfUK7sZw1GHhYBCnt4AOLOmbmYdBMHJ0TLsyR2MgaGVvJP_yJVhsM1Lql8SSw6-4syrwW4KPua_tsQw7F37S_4-VtKREA4uXoCmiWt3H66ZcRq8BcOxEcxYACwh0__HEcmBPLz5lF4JBLX6gwGW3StDqWiPtzKAXvk55uHYm-9dwvZUwKhzM0R__snN3_6z45Z1IyOs1LV9PEfuyF2uEOEN_GUAlddWEQ1qtost1dYgWMV6E5UFozrAqw_9reZHRkaEXHRIibPnEJ7FvWy_galETWjE9f-R41g0mj2caP3F8tgrjOnZJDO8nqE4EBWSpTe-C-UdOHt8jshxZhv7dgKS19rqAdASOXU6MinvbntF8_fc-HbpGWelo_x-iTsNUIGMhkC9KLN8tGapNBw4oQwJvP8pkwc_rOBBJ9c6GRRxfXVBUQ756Ib0DuNioBXKPO__lT0uNX8ZNBQv1tcU4HSBreSxveAy5ElupjyBXyT1rMueFLK64ZNGa9kNZXet87jNjW1lCf9n5nMYX5Zs-MBM20qE1G6KWdMZ8OQxZo-WZtTPoSZOzvV6m2HRJiv62GnqSPMkvvnnggt2xA0_8B90NHBJi4UIbtc1pf57FdyPKAh-rnXv2q105qj9nzXWA0s2_5a-XiASXroSkORfM0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش ملت ایران در سوگ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447414" target="_blank">📅 09:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447412">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f62d2a87c.mp4?token=W6zbEGPfXFKw6s4DpnBH_g1YtaPbBRpgdGoaiiwFYxvtU5r0EVaiWPdZowAiFLxcPe4JIiNYkU1h3N5_3AjOxNtptISKcb9V7FMwVTYNctYxZeaRFvFQZweSh70aDw5bSgfH0WzwazXqmJMwOrAgHbiScTph4ykJYXlLSdybC_BwJWncRydYaZAMsb4yfxMm6ynFOJeBi8Pt5DFRJM86eRPL4lCq0_1dtBVUekhZi3JAhcSZJJxZ2QcBF3eundPzMs4JjY2wKn5qYhM8_ePfXkFvj9-VlJTe6LSFizH70CmAmyaGPemcfisYVE5PXS-x2Tu9hODOtRthg8iPtKl21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f62d2a87c.mp4?token=W6zbEGPfXFKw6s4DpnBH_g1YtaPbBRpgdGoaiiwFYxvtU5r0EVaiWPdZowAiFLxcPe4JIiNYkU1h3N5_3AjOxNtptISKcb9V7FMwVTYNctYxZeaRFvFQZweSh70aDw5bSgfH0WzwazXqmJMwOrAgHbiScTph4ykJYXlLSdybC_BwJWncRydYaZAMsb4yfxMm6ynFOJeBi8Pt5DFRJM86eRPL4lCq0_1dtBVUekhZi3JAhcSZJJxZ2QcBF3eundPzMs4JjY2wKn5qYhM8_ePfXkFvj9-VlJTe6LSFizH70CmAmyaGPemcfisYVE5PXS-x2Tu9hODOtRthg8iPtKl21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم در تشییع پیکر مطهر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447412" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=IUuTA-SSlhXKaCVCjg3DWrcHsxOLSqOIJBDczfwkcQKqllQWXXi1-B4bVO1gsTc0dzJ1fVl4ZADXcafoIFaKVnSR1lElXcUSfY3qjKFSolS101JFit6elzBASygCmBd3PCvceZnkuHHMMeI3DZ1wQrZe_EqepKuk-tqdgsTPUz6xNN4oJqXF-IjOJiGjkZzXyc2k5TXiJBDYADPPYQcpRBnmZ9nVQANKKgtP234CIJoHpNUnOwExVC31gP5iOo734VR5J5_6685EzngrfFHNtfuefzKnOcj0ICu52acXEibbJofnytcNR3yRGU_Fnk4Uy-s-qGrrms7yoY06zMWVXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=IUuTA-SSlhXKaCVCjg3DWrcHsxOLSqOIJBDczfwkcQKqllQWXXi1-B4bVO1gsTc0dzJ1fVl4ZADXcafoIFaKVnSR1lElXcUSfY3qjKFSolS101JFit6elzBASygCmBd3PCvceZnkuHHMMeI3DZ1wQrZe_EqepKuk-tqdgsTPUz6xNN4oJqXF-IjOJiGjkZzXyc2k5TXiJBDYADPPYQcpRBnmZ9nVQANKKgtP234CIJoHpNUnOwExVC31gP5iOo734VR5J5_6685EzngrfFHNtfuefzKnOcj0ICu52acXEibbJofnytcNR3yRGU_Fnk4Uy-s-qGrrms7yoY06zMWVXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبوه جمعیت اطراف خودروی پیکر رهبر شهید انقلاب را فرا گرفته
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447411" target="_blank">📅 09:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMILBi9KZYR0IqYMfYr2KUNdJVrKwRNHd3jXOCNdhhv05g3mbswvNxEH2R9zkwsBtn3OCIVJGZlXongXe2rVexBa1c1NWVZRxU_mjDe0YdBouWxP3aEbbejR4zMmStNhRJR06KfkAvUdcNEy2_MsQHcZ245ICRtWVugTHR8oeujppNgcSpcxRU7dnHXE-XNjzwkvllC3_UR42JRb9-c_PaQWXx54KMO6kHNsOhGzoJud4jeAyPoPAzFBnoRurD4nP0ZQHZUytIdbhrPc2envdqDpskWJDoPdukH1b44vippI-CMVT7_Het6ECcU2N3IQDl4aw_okvQVZWQAkLE1HAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOEpH50tw58E_n4nqsfd8iPlthMeoOFsCAwQ98785djczPa5rByzxRk8c3e0iOEYXmlMCzJ3xzEoTazqmi7xrxhmoQxZ9x1GKv5pLurwLel7byp_vnRq5sZsiWqwc1Nfx4UGwcPpYIP-dBxyt1Dz2Qhg6vt93_zoS_QqrNY0DauTaYHTuyiwnQ2Eg501WMtA_pCzR8xsNHCPW29SgIfESMNkuHbtz6oHaVs02xgVTa-otap3EZ7l7VXzhHWdIDiRWS5t29tDkeNXKt4WmQwgO9woYIISdPE5aTzKTDejtjhIIlQoiAJAwUoOPeVK4C8YfEYCHQTEJRdrZlbAC5NQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brLJBiwvjLL8hVWoB4jXEMJyjcXQ2rFcEkK003ZUkQt2uLgxDy58yOeSQU0oLIduqYAQYIEud_Wfqws--PeFr6q0SP0ld0bYwbTlVHy_MlJ-k-rKH1-FOuoGpeQj-14IvIea0MgLabSNRaUthZDQOC4qq1u4kDFI5XysX0tqI96IS3K9iUju0DYXWQ3j9tRsPSRJq3H9vuzKaTknsGLIwXK-EIyRab-zL5f8HqlB8Odv8viEqWrcYURUnGe6zRyY6y0rTNULAS3yo58Skm1cLDQ-eg9F41ivdRAB-bexo23ba959dfKLG0_JxHO7pbVqTttWvSCSmdP-8YfL_5nY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VCQhFxU53wxhQsSJRZKTUUEIgFhWeYMnxPsqE_vi2sZoMZxB_fXWgGdyGMuaU4TCDkjU6d51KQb5PF3oeTXJhpi2zEPZPhyib9H3C3MCv-6EIlQxff2w8vTOlOuICVS7LrKQRzhSZjyLYKMj91QGZUf092p6SUv3-9K92XPX2-mX2vqQA5VQ2-RSrOICXVoB53KFlHe2KpFCY7_i5ucC9yl5TxDbkEHzo2efzfZ13C7xOdsKrD1rojO03rBN1h6ZilB6gJGvNW7MsZ4lVFWGCC6rIc1fnmcP7dBvbQjB5FO2bcaZJ51x75xFvE7a8kZ5u7Z5C5DZkDvt-wuNcZXQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDMwl9oVVTfCNCoCi1Gme1ll2TVV2RdAuaD05ccOyUGAFotbD5jiho6QP9QIFplM8o-gaRdWGQewrMuhf1abiSBY_NgBd1vf-hZQYRKROFN2R_pUWKpncTm-IzQ6gwMI2_upJ-f3_0ztWixRy9a1k3IS3UV9ZweCQJmgsRRCUkzLBuoK6fAjRO3KXB5GyYuITnBoT7UxMNrJwjQIoLU63FAgE7red8clgEccoNVC1JlfW1-v_tScmol4AUFGpRqoLhQj8h0z-i9AZGEooejTQH4oYbz16_hWrZfiUjMZGFeuPUV5vBa27aKsKsHYuPnDTjdbotFghavrExN19Prsvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
موج عظیم زائران در خیابان انقلاب اسلامی
عکس: محمدمهدی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447406" target="_blank">📅 09:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7qr498qUzNf0dURqvcZzsy0wUa1EOQX8z5WnbCFg7CBPAtwaJi1cPXrmJzTHwiHZRBMrCf5O6T-K9_HEBMyRG_2MQ5hz-lRJ6jbK2obuvqMmUcdILT5_XZO-CKPYTtOCpnNCLigk_7UiLahnD6LEqJoLnyuyqVgtgHLOs3lJoH0hgRIub36Asp_5pQ_udP5BHn0WbcilOMJWBlHxk7HtUkRD0I9FRbGFU1CsOfXOSktcJlQB4ELY07FHhy9XlOnWv3Gp-ws5lxpBRHclPnFeIB8QljoNW-R2xBdB9BgsW2AP5ePuI73gBNtPRDUWUR1vnaGmb4A6u7Lgl77RLfXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بنر انتقام‌خواهی مردم در مسیر تشییع رهبر انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447405" target="_blank">📅 09:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447404">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=g-JWbzx2UFsK5cExRfJZODOiSU1TBwybq81sksJLVv0zipcKSdNOXeuOGed7ef0WMo7ictlEpZlMvr8BGteajOLNSumA4u4gdp6Bfac4pCwauAxhgcdZYNegv_NBy5Q0uAv8zdJQg7DhMZoqL4fAYcfHluPZ84ImsrJjFlN36E8oXd8ya49hS-_nkIW_fNyKHxKB_ejqUUtxWN2DnTkc9MpGnm1RWc79yP5DgWXAse5KkQsl19DbPqADai5mBw7b4KUcaJCh6bvmSWVFSj0PBcUrt1iY7Sm7XE8tOK9FNkQ0t3hUeQNJoKwvQIeG9W9PMxVN91NfgynImkvzz1nUeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=g-JWbzx2UFsK5cExRfJZODOiSU1TBwybq81sksJLVv0zipcKSdNOXeuOGed7ef0WMo7ictlEpZlMvr8BGteajOLNSumA4u4gdp6Bfac4pCwauAxhgcdZYNegv_NBy5Q0uAv8zdJQg7DhMZoqL4fAYcfHluPZ84ImsrJjFlN36E8oXd8ya49hS-_nkIW_fNyKHxKB_ejqUUtxWN2DnTkc9MpGnm1RWc79yP5DgWXAse5KkQsl19DbPqADai5mBw7b4KUcaJCh6bvmSWVFSj0PBcUrt1iY7Sm7XE8tOK9FNkQ0t3hUeQNJoKwvQIeG9W9PMxVN91NfgynImkvzz1nUeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار لبیک یا حسین مردم عزادار در کنار خودروی حامل پیکر مطهر رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447404" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447403">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5226f64d40.mp4?token=hrlspckIjYMmQi1hJbBu0nTQGp-kZOjlSc7p6BvLW-Km0xmSNYMggYugEaexPg4zC2Qk3yWD5esVMqSvNhrceQEXRaV9BqTvcoED2R1DxlBPsPvowr1WJ0iikwZrE4cDI-yOvDrRy66vYaZOoa5jab-Rj1J3vj8nkJGzS02bilXtPjpssv98lr9vQBgt6tgJzIQ5Uh2i4IY9HmG4Dx-mXFAqelVETWudSIukfkv-Zvw8jCwN6E_byKsr6aEvcJwSc7KOM1V2V2nNVLlJYAFEqVjuEFSSUImRPxg6KpdGK0alrXeDStBNtreOCkizSF-Xs8iiuoznhBHU7XTpUiUejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5226f64d40.mp4?token=hrlspckIjYMmQi1hJbBu0nTQGp-kZOjlSc7p6BvLW-Km0xmSNYMggYugEaexPg4zC2Qk3yWD5esVMqSvNhrceQEXRaV9BqTvcoED2R1DxlBPsPvowr1WJ0iikwZrE4cDI-yOvDrRy66vYaZOoa5jab-Rj1J3vj8nkJGzS02bilXtPjpssv98lr9vQBgt6tgJzIQ5Uh2i4IY9HmG4Dx-mXFAqelVETWudSIukfkv-Zvw8jCwN6E_byKsr6aEvcJwSc7KOM1V2V2nNVLlJYAFEqVjuEFSSUImRPxg6KpdGK0alrXeDStBNtreOCkizSF-Xs8iiuoznhBHU7XTpUiUejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه حضور زائران در بدرقهٔ رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447403" target="_blank">📅 09:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447402">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e9bd3f29.mp4?token=nGU-4RJVz_cVZsKgcWAk43ldxu6LXV7h-8vikQQaKdrfnDXbTqy_xUz5yX2zQW3it5SAIdRAfMpMCXYxKiwBWGGFxtHfs-bMFUxRBXqeLNf1nCP955cE3Q1mhVcviK4IHja56gqytOVXJFo9O3_BVY0faJo52R6FS2ZEzjT2GxlhbGKjZMiGwik0vvxOXBH8NpHKvX0Mq32ew1ziMW43x5t4-pNd6TK3D2sTSMBl2gHeAgw-XJuGtwZIPf9oR2EqTlVTrcZTpd4elp59oMsYFC2dAVe4hkP5YGHkDuqAblM95wyQ1HIs_jak3DZpFPeDdoa9s7pfBsfWsIyArUTP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e9bd3f29.mp4?token=nGU-4RJVz_cVZsKgcWAk43ldxu6LXV7h-8vikQQaKdrfnDXbTqy_xUz5yX2zQW3it5SAIdRAfMpMCXYxKiwBWGGFxtHfs-bMFUxRBXqeLNf1nCP955cE3Q1mhVcviK4IHja56gqytOVXJFo9O3_BVY0faJo52R6FS2ZEzjT2GxlhbGKjZMiGwik0vvxOXBH8NpHKvX0Mq32ew1ziMW43x5t4-pNd6TK3D2sTSMBl2gHeAgw-XJuGtwZIPf9oR2EqTlVTrcZTpd4elp59oMsYFC2dAVe4hkP5YGHkDuqAblM95wyQ1HIs_jak3DZpFPeDdoa9s7pfBsfWsIyArUTP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: خودروی حامل پیکر شهدا دارد حرکت می‌کند
🔹
پیکرهای شهدا را بعد از میدان انقلاب به‌سمت میدان آزادی می‌آوریم.
🔹
مردم با آرامش خودشان را به‌سمت میدان آزادی نزدیک کنند. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447402" target="_blank">📅 09:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447401">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9a627324.mp4?token=QWqbYQNxztyzcOQrHww7SaGRTc5fvQURyF4hCxC5rO7dGj1pmROTMSRal09JQq1dRfzTaOuR88Q4H49IYPEDuroR_p8oXoz31RxpHPkcjQxh9G0qgDE10gVv7TAxwF7ykXGOqu5Z8NL0idAMr7MF_arOVetQXdiSB9WdgUUHDD-tJG4Wo9KfUN3FUICsYGnYhuXbdsIzej1ueeddhUWo_bQhLOXjMTLspSmgMiC_-qPkEE-Sa9wbS06mZpEX2v2WvabTjaE6gzDAoeeENiGv6SsdHINrv1NJ_K9YAVbuyl4mZCyDzB1969_wC4dXfocN5Qxq5LxV6M2-vk4LUJx8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9a627324.mp4?token=QWqbYQNxztyzcOQrHww7SaGRTc5fvQURyF4hCxC5rO7dGj1pmROTMSRal09JQq1dRfzTaOuR88Q4H49IYPEDuroR_p8oXoz31RxpHPkcjQxh9G0qgDE10gVv7TAxwF7ykXGOqu5Z8NL0idAMr7MF_arOVetQXdiSB9WdgUUHDD-tJG4Wo9KfUN3FUICsYGnYhuXbdsIzej1ueeddhUWo_bQhLOXjMTLspSmgMiC_-qPkEE-Sa9wbS06mZpEX2v2WvabTjaE6gzDAoeeENiGv6SsdHINrv1NJ_K9YAVbuyl4mZCyDzB1969_wC4dXfocN5Qxq5LxV6M2-vk4LUJx8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل عظیم عاشقان در محدودهٔ پل روشندلان
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447401" target="_blank">📅 08:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447400">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d52JGhHhUqNmHaGEqV6w0jR-K3nz309wKN353U8vzwkwZ6kjhUMdAMzvVKMqNP-eZDCbahZDONs4qbuG5VIXpT2iaoMMB1Vq-F12fjcPXjCVmAPinR51rDuH2ipi-XlQ_fBG2YrxjZ-wFivANcg16MqDdQspk4PhrFY5y8AsaH0K3etUL1OpHilnuZU1gY-vb5OMybTmIg_NfKbpz0Ch0BIqZQwd7CKP9uLnYHy0PmqPVDpemK1QmOCMwdT33GQOqdmKGi4fxiNHA_UHNZMonSVjKEFoMM_FAOc52ACiw0ei6uTfGbpDy9W6qGp2wR9ppDOcrH5PnZ9Wk0WQxdCUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
شعار لبیک یا حسین مردم عزادار در کنار خودروی حامل پیکر مطهر رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/447400" target="_blank">📅 08:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c66ee92f3.mp4?token=Wm_RWE-HecdxMwmw3TndVCVMLRYt8uyplagmt-Q81K0teyRaLbhXmf-af4rdUNC5vJDoxVU_K4NoNy6R7IKtWgujFmaqTIRtc3nsYJuIHv059zWpQGUdlZePaq5Bgq0LUtL5-e0LaNLOmn_SSB4h3JooQLAh4LKcdes9xnQKFfN2YU2gau8KKUnwyCmquK4uCaswGO_BZfBXeNiFXuFBdIXs4P031aygGblKDGZQMrIIlGOJEJX3q5DjjgHn7-Lpi3K1jQ_-YY3_kB3qGVQKW7JXjOIBWkeXzHIGJrVziCR2ziok9oqz3D2hK4nQWuvncWSvPkg_fjDEK-hy5wi-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c66ee92f3.mp4?token=Wm_RWE-HecdxMwmw3TndVCVMLRYt8uyplagmt-Q81K0teyRaLbhXmf-af4rdUNC5vJDoxVU_K4NoNy6R7IKtWgujFmaqTIRtc3nsYJuIHv059zWpQGUdlZePaq5Bgq0LUtL5-e0LaNLOmn_SSB4h3JooQLAh4LKcdes9xnQKFfN2YU2gau8KKUnwyCmquK4uCaswGO_BZfBXeNiFXuFBdIXs4P031aygGblKDGZQMrIIlGOJEJX3q5DjjgHn7-Lpi3K1jQ_-YY3_kB3qGVQKW7JXjOIBWkeXzHIGJrVziCR2ziok9oqz3D2hK4nQWuvncWSvPkg_fjDEK-hy5wi-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود خودروی حامل پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان به مسیر تشییع تهران در میان خیل جمعیت مردم عزادار.   @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/447399" target="_blank">📅 08:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUyN62aLNLZBCBAaDRkF9g5vdIH3kGWKtsZg0dBKhHrbCxgTkqn8gnAtp6ekY5HEneH8S3_9Q8zMt0osg-7FjE6vvyPzTdoqvZJjjJlwG6qMkiJngrv93XzkD8Vp3MCJhBxw-87kra-3jYJHFPSdjyriObIM82EYz_RBe4u15Vsli_LWjAp52-aGYlcY6HEWU7dcajXBg5h2Wj4LuZ3OHWaFSwTtdTl5rGoG1FkxU9tc3_fPJXFTKo36qj3sSUIbBnFHmcBXWhZwi1rGcD0ac8c8S4nyAOqjTy82RFzoK0Hj1hPjwJeunWyM5bKbBsn8efePqt7-ox0NjTg1lt2i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دریای خروشان عشق و وفاداری در وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447398" target="_blank">📅 08:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7t0h5ZN8H3VGOW07rd2u6JxoBSmQJS2juv-AGp4NkS3j08uI9Xq109ML-8kVYKyVDnZmVkwp9DP_o0P9127539lqK1kHBiMIMJ5SN3Qm8MipoyToA9mxpUUk32mEOJ1_QEVNVpygZXu0HDDVmR5az_dia5pQnsN1vpleK1w3DeywU6yz8Rrpla9DIO6MQDZ47G2yG58HloQLyeo_XdxeumJpOKjEpYvPEXTGCezllbHogzzEezzpBaeLelUqLW_K36e5uxzUmlAok-RAV-lv6QxUbXYVHmSVTaKfb8N2R8oKmfLdEylGcO8wXgEtSUdVxGPglYmXMee7y-KlkstTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سازمان خدمات شهری: با راه‌اندازی سامانه‌های مه‌پاش در مسیر، دمای هوای مسیر تشییع بین ۵ تا ۱۰ درجه کاهش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/447397" target="_blank">📅 08:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aee71456c.mp4?token=PLCw5rgu6kr8-K6VWpNyLiLxttnSn1SqbMHzQqbBJXhQE4tAyxa7onbRncLhroIjAFGex8vNhYDKR-SjcqCpJcpJOovuyTQDCzR43FDXVmx_C7XxNlFrebyLn-bGjJlCstY716PZlsRLU6Exihi3XVv8LFZGXUZcYQvTmOuJKoi-0MvwUvDOrNSmPzL96Pkr_hqnTo77o4ezg9MliIdFXpVJapltjBeMgyZeD0NkOQyhkCG6LnA2NCvtDZ8DdnKm9UqOvrIWKRAJEehXNTsZfhcZ_g_mWrKngofMr51kGQtKQnWyzIyyuEyeV6jgJd8brnIUFmTFrnLSU2ncrverQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aee71456c.mp4?token=PLCw5rgu6kr8-K6VWpNyLiLxttnSn1SqbMHzQqbBJXhQE4tAyxa7onbRncLhroIjAFGex8vNhYDKR-SjcqCpJcpJOovuyTQDCzR43FDXVmx_C7XxNlFrebyLn-bGjJlCstY716PZlsRLU6Exihi3XVv8LFZGXUZcYQvTmOuJKoi-0MvwUvDOrNSmPzL96Pkr_hqnTo77o4ezg9MliIdFXpVJapltjBeMgyZeD0NkOQyhkCG6LnA2NCvtDZ8DdnKm9UqOvrIWKRAJEehXNTsZfhcZ_g_mWrKngofMr51kGQtKQnWyzIyyuEyeV6jgJd8brnIUFmTFrnLSU2ncrverQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود خودروی حامل پیکر رهبر شهید انقلاب به مسیر تشییع  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447396" target="_blank">📅 08:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAxM7c8bn4Cf17oA2IThRWdZyaFeyIXyFx_m8WrPsjPVTtRGfr770MC7CtXxvozBDCSM3WJzFHGleESmTIjzjxbmDvLlS4UPH44D_lSvieyetnaDxw0fcmFHxQiHqvrlcAMSOtau5oMcfWLozay1JJXupaoglzz3Rcizw8JW4uz6BiqrllK3y8Cyjyrg1W9GbL49EA-CJrlLI538QD0PtKOLXxaMy6j6ACkwNe5bH1nJAYjrl5j6W2LGg8o90xSms1rc-LhWczqsQ8i1BWpo4sclRnZ7Tqs2kO-ljxCPF6aRMj_jhK0EWZj1RRsROKu6Kv4nUOgKmG4KJHRuAhehrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ورود خودروی حامل پیکر رهبر شهید انقلاب به مسیر تشییع  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447395" target="_blank">📅 08:23 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
