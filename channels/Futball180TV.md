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
<p>@Futball180TV • 👥 570K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-100509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو چندسال پیش گفت: ما تو الکلاسیکو مسی رو خیلی عصبانی نمی‌کردیم چون در این صورت عملکردش خیلی بهتر میشد و دیگه نمیتونستیم جلوشو بگیریم! درسی که جود بلینگام یاد نگرفت و باعث درخشش مسی شد!
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/100509" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2241a88830.mp4?token=NZQXG2ZHOal4_d3CkUfrSzUVIAbiqxjVhjNebSKd0VDy9pmLWisvaLrCkd3nmZKpA2Dcnp2GX-2hxKP5Iey1VueuotBjGirfeLeh1xLUJ3y18RLDfm5UlurHIXgJchdneecsABCbhtJdslpUhOQ7EgxZN9OupIeySgtocsGV3uVlpzUqE-0r4sWqrXvNDzx-RDWckPiwHQJyXc4vkLudX69Fr_AYhZAEHE6nPOw4drFRIsYCEQ_KekBpI4M3TS0gux0v2aXvGsgwSVyYpJQ3ktDV7_umfqyDPFDKg14Pyk_cnPwry7gVX5rS7Husk_a_KuW89bIiDIn1vOJF20u5mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2241a88830.mp4?token=NZQXG2ZHOal4_d3CkUfrSzUVIAbiqxjVhjNebSKd0VDy9pmLWisvaLrCkd3nmZKpA2Dcnp2GX-2hxKP5Iey1VueuotBjGirfeLeh1xLUJ3y18RLDfm5UlurHIXgJchdneecsABCbhtJdslpUhOQ7EgxZN9OupIeySgtocsGV3uVlpzUqE-0r4sWqrXvNDzx-RDWckPiwHQJyXc4vkLudX69Fr_AYhZAEHE6nPOw4drFRIsYCEQ_KekBpI4M3TS0gux0v2aXvGsgwSVyYpJQ3ktDV7_umfqyDPFDKg14Pyk_cnPwry7gVX5rS7Husk_a_KuW89bIiDIn1vOJF20u5mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش عادل فردوسی‌پور در تلفظ نام وریا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/100508" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپید:
دستم به دامنت یامال، تو رو به هرچی قبول داری قسمت میدم آرژانتین رو ببر و نذار مسی دوباره قهرمان جام جهانی بشه! اگه اون دوباره قهرمان بشه ما هوادارای رونالدو دیگه اصن چی داریم که بگیم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/100507" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I66BdoEzW2YZ8RXjTCZ1O8LIhTJ9cPlqcvIN49gv8ldUBDhWA4ZMe71jvzEBj3GJuBnZ-6W1dsrjFofNFvOsTgBW4a6vzCAfkkU0N5TKjbpbDjWeUJCq5lEw7zRhgyBsIr9qrqEFDwfWMNrasPat4AhpRm_ZO077Sfw-NuBgnc0FVxeJ17QzwxjNcD-m-VPMQzS6XNUkZVWbvj0fEtMc59_JSJBXId1bE_sRLaBpkNsk6i8V0qB5iQ2__XXQ_AnbQWxF5A5OtaVO9Dl5TkauTgA84GtXZGC968V4yfXAKhkI6Mi5-0GVfihxxjQNr-sZkwppIr0BPgQcjPbC_hhjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رامون آلواز:
رئال مادرید واسه فروش کاماوینگا مبلغ 80 میلیون یورو تعیین کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/100506" target="_blank">📅 17:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
تصور کنید توی اوج هیجان و استرس فینال جام جهانی بین آرژانتین و اسپانیا؛ نتیجه بازی 2-2 مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه، همون لحظه بیژن مرتضوی وسط زمین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/100505" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه مخ‌زدن در استادیوم‌های جام‌جهانی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/100504" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100502">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
قیاسی: رگ گردن میذارم که هالند لره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/100502" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100500">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlPUFoZLOGzXhPfEgL911uGYR2kTNrz72fM2LrXh1HjUuwYawbya9Zy3cwu3TqU4yQyw1hrrD_Vb6fIYhy0NgQSo92nw5G3tOImIVKzgTL1q8d9YibYKZ7iyd1VVrkN-FEquz9KHcLBhhFCLFwWajM2vIRCRMEfFB3H8Z3rfYZ_yVHwlxbvf2ypDWD-E2jqr9FBTW6auJcQKGGqLPep1mpQoUq35Qv6bMJuHP4IDkiAb-zqJCnYRb3pIm3TStVE5NBng40ATBrMtTL4Qh8fWIngqcroZdAY0P3F9N7jg974sCkcoPU1IcdutWk4MQPuD50L_kk683B-3lr8DvpfIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLgHvIcjW3v5cxBrPfeOEQbc1MubyAHwBEH0h3-eEbdBkbBiLjMnZK9uh3aLTB4EneklySr7DQRXll9lo9m30Fjb2Dkqo_3nVwu-oZ-ArAlzZKWHJzZ8qAmwlCty9UmE3Gpi5wkUow-Pbm8uOqE4Sq_pYBd4Q3Yjvo-Cli_68CjOQ166rgz6Dm4gpyR8nXta_iZz94upXci4A4pewMxg30_lX3N11P4fzpVOKWkolZjNz4kzipL3pdcU5y8QjMiSvaLOf-A2oqEFgr9Fm2Bb2Ane2ws9WkSbX6kYdxQZzkMzRB6kebP0zpEuxAAgvzZTEZZtr7WeIbLtGoshrwAz-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مینی تقابلی که قراره روی سکوها بین داداش یامال و پسر انزو فرناندز داشته باشیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100500" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100499">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvD1o_L6-OC_3pt6tiNxH32dSMxcW83AjIz9HFTn1qeu1bxq6B3qDxy_4pa2WQ2-GlaYtrWhCMF47Xn_7ZklF4OAIXIt8rCA1Xb7DcGlIoHobzrGTpP546ufW9Q2TUoKz9hMogq23I4UxwrXX7PNBBkzd9dWqf-XZDr43e1lLbmre45fAD3JEfkxA-Gx5wsHUDjXKgQvM12ZsZ8B9sKnaTKhQYnGgSrbCeMaamuW43an8l3yfTtGUDynDidX0Y5-s0ELsVnIAYEe1bC5asW7tbciavaq1-OeZBrOIqVQk5XB37UEgSCQcBaPRaGGGCfu-RxQOR2jfQQk7yXN8mZzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
الکسیس مک آلیستر بازیکنی است که بیشترین بازی را در تاریخ جام جهانی بدون باخت انجام داده است
11 برد، 2 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100499" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100498">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxErwStoKTi15Z9NPKM96b8ln3BuOsTtnyIQiK1MEuMGVPcpaLT4lAE0gM0AewfVhdda7-wUCpesGI_z_T1havWwoUbiSXh4ZJD_5a3fCmvD_VOycP5HPyxhRsgHTJlQbHF_nWt8yzw71HcgJIe9yZpb5x54X2b-f4uh8EQLuU_NCTtodVjBihjfB6cbcShOUsaP-_WlxKMJfPuyHTSXYmarozgh7I98vOl6qcTLxf_WdBu88cemokmdmEXsPR9pMZn-fWVMZJPTv0ssAJ8R3y_JF22T0DWJeGs8aPMaDYTJgIaE96KfwIMpsgykJvc3fDhT5b0fSAgtUr0hpeNE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: سوبوسلای مجارستانی با لیورپول برای تمدید قرارداد تا ۲۰۳۱ به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/100498" target="_blank">📅 16:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100497">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جام که نشد ایشالا جام‌جهانی بعدی بانو
🎈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/100497" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100496">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
علی‌آقا دایی که میگه بخاطر مسی آرژانتینی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100496" target="_blank">📅 16:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100495">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N92zQns_P9Ro-c8n1xGcyRTq7k6Eb6uxJ7jb9vdhnSaT8RrlgCAiFS36u0K3y1fkysM-evd5pj3MOGamQBZsP76g0AHdv3KP9laorkQ-HZZLLad-97O05RLl3dlZ0RseN72nEMHi0iCOxG9HE2TQte93FYYR2fSkllK96CYyaXXoQ2K3fBgd31ayntmwZs31fAEB3ojQA5g3tfUquFnW0M1YW3UJ1-ks8gFNUBvUTPUlS6H9GGVc8VHkjP5A6QvYE_uxI7Unpt167u5rqje3p8ylPDK6xwRlWa7-rVOU_qJSbdPY0RFLVNgsAn2ot_iJVVAc1PHzaNBYB4EPG4hTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دی پائول کنار مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100495" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسلط کامل فیروز کریمی روی زبان انگلیسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100494" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
آخر عاقبت گنده‌گوزی یه بچه‌سال برا اسطوره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/100493" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای عمو ها اووعو اووعوو رو بخونید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100492" target="_blank">📅 15:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd1G_fIKc3AuegYTEV5r8-mWnNaXj7LF459qAWhs4Gf28UVTpjwMM3FjFNeN51CjTv_INvYJ1dDy2qmi1D8C_QCrxZziPdBSJarxhLwMdMzAJMom42rxKWRnzDM63RUauuZhpq5ENc7oonyKNsURU0tv_z49fp11sPqEC-KWZx0xsa02xnp7uYAthHJ9C4FXYB2OoKL_UbCPkEpA0uReqZbqAgiw8rveDRN65WS3z60B0mTPRFzCA_Rm8GEuzKh3a1MDrisu_zrWtx5sgHn4Kb2eXG3cNM7bS_XiGVMegNSzFbMQe_GxiIkEsdIaxUtbngvTUL_kXL-xW1SSSPW0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
🇦🇷
آرژانتین در مراحل حذفی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/100491" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZdyhRScUn2A513_RPvtabk8iZmhrNZJJwOjrfu5r4qhJ3eZhZh7bP9tNYQF5sDBstCiDcN_1aN4Ho3CddsOi1vo_3ZNCuE1c55YWzlb1XRLbLHJMPxZ7e2amdLkNwgTpI5TUqxrPAiRWIis2P9q4AZv_q7N4XTkFArZstx6h8yodhnyj6pjbnkAoFy0NzhOOtbaKXviuFS10E5hRWUenwwaZi3iupICNavDcxaDx7mSxiVIRZXcKuIMqHevRcqk0mOZbKW8YyUw7nYlOxVuRBw13OxtamgbxxVRRc0CohqihkB867IUnm6yRm0lCVGkFxOxaHgqa8R_MeJOo_ldZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏆
با صعود به فینال جام‌جهانی، آرژانتین با عبور از اسپانیا صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100490" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYN5nsVCu8LBNJCHW5FzG-8cXpIVWAJEHtX20C7uGm3XsAqTodJiCkdzDqS3clvo7OQKqfMPGSblskCZ5xNyKgbygPlClEztDlNG39dndHLNPzDmaOO3X5f_mtRBAAB8ImyrNlgnXpBagU2ayVXhqKLs0VDleTH7hPl0qZFcFLmzHv435MS-xNbWaAf5RziRk8VUhZZLfWXeca9V3Yhw_BCXHRUOVSQRnjwtPYmfvHM-p9ya8JLtLKSlnYRrw21L6MhOMw0Pflh3e9Pta-P1UV31T3lzK4F_6_liDlVtdMUOZnykYaSg9A-PnPLQ8xPSiwU5eZ0OkQpIl6D-QQBPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏆
مالکیت توپ دو تیم آرژانتین و انگلیس بعد گلی که گوردون زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100489" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100488" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100487">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100487" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100486">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لیونل‌مسی به فینال جام‌جهانی بازگشته‌است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/100486" target="_blank">📅 15:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100485">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مردم لندن درحال تماشای حذف انگلیس از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100485" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100484">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
جمعیت پشم‌ریزون در بوئنوس آیرس آرژانتین هنگام صعود این کشور به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100484" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100483">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100483" target="_blank">📅 14:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100482">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100482" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-I5MCyBozQRxvYuknNE-ct5ewx027CXlmiyiNvclzLco43GyAa2LvJZKPeAygOG4Y4OaeaJfmxcwUFoBADEHTVjlIijp5DqWLj5dLr7JzSJMfYk8Cuu6hVQyZiYTXmAJdRSQY-u1c2_YwS5aWB6HZqxWmLSMZaRUPhC-UJT_svUePUf8Jb-QUG1wIqVHXueVfLvsEOZbti8oMEvfBFvqXau9iB4WF3DiP2xMgi3PZ6Fw3i0n6uUwfioqkUkH-kgx7N9zV-F-pLDPt5rwt8wWkUYD7Y5tqq4SURu0TmE_sRhuPPgsbIVDrEhIpiuT7vMKfL6vqhRWdRDRE2mw3OZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محمد مهدی زارع، مدافع میانی ۲۳ ساله احمدگروژنی روسیه، با قراردادی چهار ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100481" target="_blank">📅 14:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100480">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇦🇷
سوپرگل انزو فرناندز مقابل انگلیس از از نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100480" target="_blank">📅 13:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100479">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100479" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100478">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کریستین رومرو: امیدوارم وقتی بازنشسته میشوم مثل گری نویل احمق نباشم و از بازیکنان انتقاد نکنم
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100478" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100477">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U54Dih8fr03Yj8tRyiczh56x1n9Uw4jfhCch4JjFZrnAR8lBD4FWEMUqyvAkHHcWxJybbGA5ncBXfLkubF6gn9jSuOdmtFvX3j3JVTufQKkduo-GDSFoLILBcuYaCQMpbZPhwBBZRvPC74g2UzF46_MqXjkTsIQj7vcytl5L2jr6nLeR9_lrN8KLdDPC2N_4FJtWsnRu3EavuM7kx7H-798Fd_0KHlQlYf7DdTo0Ke6-ShMXfYpbgNGqNNt6odB25GyZWXVdEVXss3mAVeyJTPEb8Sfn_NcyHhJWY9Cy0QH8q9GL1QO7YsF7vtIPYPrUe7StMDVXSxY9fqHS7hxteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دو سال پیش در چنین روزی کیلیان امباپه به عنوان بازیکن جدید رئال مادرید معرفی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100477" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100476">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100476" target="_blank">📅 13:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100475">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100475" target="_blank">📅 12:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100474">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100474" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100473">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M63EL4ssOxM9XwjFfl3wP4V76LNz9EaQV901tuyVeQWEBW-Vj2UCxsCBXfWVeSkJQWrzs8chFurhRQi9bvykMGRRB54M7HFLGKn2q03xipP7bQOqc1FYaSzuzCppAl2U3MQq2Y820VDGTlTEoTGPH14lsHun_VeXfP_iqUjtE9XuKOnMbxQ5q10TScUSJYi3bIYRlR1uGsPWKzKrT11D0QYIj3mFopPCgH4r1BBu0FAMWikfkN8RQsOwldmZFXY_7_xNvUhWwjqliZh1u8vjqCwtK5c5OO4fRmP59XsC1WaETcI8M_xSNsiOGuMkT3bZSFj0iY3x0QGDp-0_77MENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب نیمه‌نهایی جام‌جهانی؛ خط دفاع کاملا اسپانیایی و حمله آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100473" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100470">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100470" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100465">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100465" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100464">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100464" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100463">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100463" target="_blank">📅 11:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100462">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100462" target="_blank">📅 11:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100461">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100461" target="_blank">📅 11:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔥
🇦🇷
جو فوق‌العاده رختکن آرژانتین که نشون میده با نهایت اتحاد و شایستگی فینالیست شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100460" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‼️
⚠️
زد و خورد طرفداران انگلیس و آرژانتین بعد از بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100459" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100458">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100458" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100457">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100457" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100456">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100456" target="_blank">📅 09:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbdUNMG8A44NjycQ1217wv3Fd8bEoSknZdxABs2xBRRvuswtEM7w9mst2Ggfy2b4fldvLLvf1H-Rum-H3OE_EsumYb1ruiA0oaSy2CZ4gXUCOMJDpEAnCcFd9Rh6woXQOav_bjoX3abAQ9xwn8St5mWrd1RnlY-b4AwwhycNbNvULk-xyHKXnYD-zscVFhhLRaSTqZw6p9HP-uSK84NQI6WhVZjr5MsWlwpVNxoNbfMGaezNdfZD2RgxfxeyrZyAvt30EEjMD9UuHfnwiLG53p-JgvPf_dBunXDZSWd58xaedFFimXekVgUUQWBmEQXs3JdqUQz-KkUSSJsWrXrrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جود بِلینگهام: "برای من، بازی کردن در برابر لئو مسی فوق‌العاده است. عملکردی که او در جام جهانی ارائه می‌دهد، شگفت‌انگیز است. برای او در فینال آرزوی موفقیت دارم."
🤝
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100455" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100454">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100454" target="_blank">📅 09:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpDjc5fcHl9LAoS6DVtaVU1K2uL4KBw0G8mnu2Ihl4PGtxGDDaEPp0gvPrHQxRu3P339OGV9EEqhdSxO3xIwHSN0XJZf8QwwSqoebfs_N0hAVMoFbZCD4D-JQLjG7HME8ZmFuWZKVstBdJieK9Do4evlZ46v6rebwrDLZashSRX4jY_tsORkKzd7nQw-GQ5T3hxb6L-IepDqn6te1A4r-UjeK5pwX2qlbxer_09YP8-R7hnTKGqvdt5meiwh1wNwJh67i7Glu670jODDnFmnCIi_9M7LPN-9YrE2gLdwBqrgOfe8Ji6vCb7x32TInI2Me-ChHwKJsILlJoA-vBvqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
| تعداد دریبل موفق بازیکنان آرژانتین (به جز مسی) + بازیکنان انگلیس در طول کل مسابقه: ۱۰ دریبل موفق
🥂
مسی ۳۹ ساله: ۱۰ دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100453" target="_blank">📅 06:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pea_U9C02Rc3k2ssk5GF7jwkcKV84cHyW9jGZPLeFPzLr0u5iwVinrd5l9pflTR-VEuRwqKo4xL0PMQfCbBC-vBVfpDLYUSgN-FnsNTbXOie7ilpfdU7ZgNsFJsT1ocVtrWz3CNN5stt2l8pIXpWzqOpT5gu8GcXEGSZfcbhqxkqKCWuFL_5_RrQZ_GdZRKLSAPbff7IU4IwYYLmx8HduEg59hEZFV5gwaH-rMmxvx6t3DjB4hcf9UuJI1lTw5-oIkNlo9HQP5tjbmbTTNeEVjBUN7e--sKwcfjy2oyEfoX3tDibiZt4HmSWwKsaOB058tYDvpV8Od4Kfs35e1XG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
لیونل مسی :
🔺
من خیلی از بازیکنان اسپانیا رو می‌شناسم. خیلی از اونا در بارسلونا بازی می‌کنند، تیمی که من عاشق آن هستم و هنوز هم اخبارشو دنبال می‌کنم. این مسابقه بین ما و اونا بسیار نزدیک خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100452" target="_blank">📅 05:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100451">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/100451" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVca1GuB-D1bUfWDFnseCTfRxEVH3T_0R9XhXiWVew2Xt3Z-5prR__2LhFp0ppDjGFTCL6If_QfJREPgvsCdNTbzphTGc0OgDweo9_UYc2_qnM62i7mNkX6yNkOtY4PwgPzyOqTsZPoBLTblQSFgYs-YGvlEQkOup_6r38QT8C0zWA7V0yCcmH5tQPRA3hozYQpupeY21Chx-lXIVu7wzyQCPgbUxslXKFFjUxRWlwE7aK7VywQJ0GL4yuDt5kuP6eVoT_NqdxJn1WX4ommO5h11kqHZGlgji8Xv74b4rayCeAtg3ENWGxLMTrUB6M9lKhnkLMxvXM2jIaoH9D6HlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/100450" target="_blank">📅 03:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100448">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llCwU2g7TMoUdUmdhy-5HDGzZtuQ4LtoXswgW9bLMiiQTQ_ZzJbb2NVC20KAqL_b_5lD3RBiG0pfVr3UwxPGRwgp2TdKqsZzIsnT7P_XE8C5QyiSKdgskhb3r7s5I5VHRnuBU-uun1ioFL2sFGd49kVt2OKixxRcDHneZUhzAUdGxgNECqS-l6u7aWmrLDUQoW2vjn2uWq5E9y076yw-t_WtnhgLuzFdSZ-lgeXbJgd3sqSSkUKq_vhVWp0pFuULkpoLhWIJm0EgpD6Fzg27qUFCMw5hQVovMyDLIh09300o5QxBsC6dFXh5wIi2nr30WS2KkJBTRap788JkK15-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا ممکن است تیم ملی آرژانتین را پس از برافراشتن بنری با عنوان جزایر مالویناس (فالکلند) متعلق به آرژانتین است جریمه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100448" target="_blank">📅 02:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100447">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100447" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100446">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/100446" target="_blank">📅 02:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100445">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBnO6j12EfQJC-PU0I5XIKqC05Eb9hku896t8b8icrDbIRZ13nOwjv1_mq2_nfzsG7kvnhjxPf3W4LClHXu_V8qa_oDzrvKofdyNMoTLQyJw_kyhChuqxbEM9mrPIvC1Ett11sqjwqJF64ZR_zxRS4iYXFdfsTDlMsZ-xfLo83uKmMG_ZWY6fueF3Hdb4oeYAVp3o82W4CBKqOtj-sGWoz-XFfbogQrYOT5IZKvylosWLuw1RWYoFt1T3oGqlKFv9mGKWzD_WcnzEPIGeoH4i3bNCbfxuGLH3ZXv4Jf0OpVnehSEo4cH-uz55l9gn3c1dWnwIzCCLjyB0TNGkK8q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لائوتارو پس از به ثمر رساندن گل، نام مسی را که روی پیراهن او نوشته شده بود، بوسید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/100445" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDtmvp_2gj-AUnn0Gj8AG9Qb6PoQjXz0-D7RJIdH_byb9LBHYBBK82JyXD9oFIBj1F65ysn6sYlCjs4Fl-8fKc94eQ0H6YGPh4YTiu0VrQJk-i_6jSWzQT3A1ttmlLK7l8NQNJlYkXW1KGyKYNHH8dgVl1BKBIEJtaVU1A1M1ZqIvFnvgG691fa0lksKKBrLkf7ml3AVKlqZehOE-HHPP1Wu1vwJbRRlGujujq4yn492956hv3xJ847l8QMRAbLfNHM3TJqMAoEXkyGLAbCnR_afR_2cyBENV_phEwESEcBIv5vDs9rnByFSedw56LOqmo7afDZXrroxhNlViacJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی:
این جام جهانی دیوانه کننده است و رسیدن دوباره به فینال باورنکردنی است. من به آرژانتینی ها در قطر گفتم: خوش بگذرانید، این تیم هرگز ناامید نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/100444" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100441">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJA2HBSImJZhdyLVaIKo3_FwZvCHDoXV2xfosLdQH-g4jqQ9pa1TrEzTv_AsJR66cL9u35rBr0Bcb3c7GLSqkSxHURdm0fg7KGI0qcyeqkmH6h5K4IkOWymI7e7JNge8bLbJsDVjSqvD5EqFmm_hfLv54owy3OIiyEQuao9luucgRFuSufPAMSjJeG4Kn3FITNpDahhGdc4qkUQNuO8vpUhIXg0h4LupWquUuD3yKugoqRE3g8iJ37_D5SH6eptBkxdT0Itj1kWU_nlkAaFdPz7Rtr1AgUCMPuVW3grgNHJdujsraB6lI_yI84mVAPiSUjxDqiyugt0b39pH5sBnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZZ3HOtO9YPPN7v_07HIsN2u35IYmEFtSORWzMbmDNA17N8sExgjYH8O_xh04h0ythHxgEzjtqlBK3Tp3v3OeiyUx9ttkGqLwHpP2tTDnVHyZhGOmn1_fUkmZxsrCloZybNSizao9WOyyRcYMJvzlFomeRvLcg_MKjAH1lY2gBK_KbeMIH-_pit6K_oUuk4QaQLyJ3dRnLeVosw9rS6LklVYXuoMSLJUHchGF1HKRL8S5O2vv1Gde2UmaNatTsPnNzkQx0UoYiT_oMRZFPcRtWQkW7xhRXWRiJCq1wumLnzc799J9Qih9_gNJ_uq-TrDqGI24eyw36kIDjuPspEJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5dJfMnB7lfSk1zTpU5sqv1xVB-y6sVjXGMVKyjeAIGiLixcUvyiO_ENHX3OuVJ-dH-vOuDJn-eMgDuSn05y9hHroxk_1hzLNTVTw9ziRNN5FfnmPmp3q9_FzUlOKV2wY4QAUqc9tjZ3F5Tr62mZz-HqiIAL_raN_9OdAjPMdvB_6Ha2gRGFeoyvA-czWJZAoQGQq8OYUKTj4pVf6q0YFS7HQ5IqMhwNIpeRJXklo-u1Mc-Xei5BeHB9Z6NFjDH47jlQlB58EeeZIrRLkR_NKMXQhCYnPNuMB5jJgOjwg2dG6v3ufuljlMX6_YE7d-W9os7F7Y-Mfd3AyRp-wYnPnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🐐
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100441" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100440">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqstjDIUolHjl3kuzszg_7QxNI6BbwhhE6g-x1suRaLRhaV1AB_ueuGpCFtVmdM9cpiC4wKJ_0RIZoPjlmdeCSdPaaM1oqb-qKl1_1zjY9aGMyjtG7Td9R58tAjZg6BDJ7IHnRPr9BP2vuzE2l22XK15r7g1IF1rWyUATV6UAPo1ccwsu6r53AlPJU0qz9xXQMdBLd2AuWpErvzeQvwfh53SmuxZU8SR3Jz6hRlile-iLpKNhqfwF1a1Nxwj0-fL8xm3wlD4uhGL7gEPfrHdxdBfPxb9F_JQ1Jn24peqtqAjhy7eq2WVfCM5yi3j7AvPW-r5YJo6ojR8vSELbs-o4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100440" target="_blank">📅 02:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100439">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135c24c050.mp4?token=e57foO161qspQKgLJ8RzfpFbUDo3ZcIWRolnkRjwlC6AG7f6fco_pFhVDzH5S9t61gZeDHrbCgMm17btYmCfqvZ6WceYOg-3h0Styfi4T2Co-NgnLpdOCn-Pb0rhKUH8P7M2GUEAFltZWWnpdfu3yuLT967puDxNd1gTNL2JgXy65i0sYc1EmndCQIyy9bM8a4VRTm2TTuy-6xYrglwE4HX5BEb-qbf_3_uH9WPSeFcj-gqwZ-Xc_Zdk5Mp3vmxMmjqUJivZ4hD74rseHyLyReXYTuPCfNZ02giPvnrz8XluqbGUX4eKN0nlr6_2yOOwR-jBKdCBEuOcwHGpx3anJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135c24c050.mp4?token=e57foO161qspQKgLJ8RzfpFbUDo3ZcIWRolnkRjwlC6AG7f6fco_pFhVDzH5S9t61gZeDHrbCgMm17btYmCfqvZ6WceYOg-3h0Styfi4T2Co-NgnLpdOCn-Pb0rhKUH8P7M2GUEAFltZWWnpdfu3yuLT967puDxNd1gTNL2JgXy65i0sYc1EmndCQIyy9bM8a4VRTm2TTuy-6xYrglwE4HX5BEb-qbf_3_uH9WPSeFcj-gqwZ-Xc_Zdk5Mp3vmxMmjqUJivZ4hD74rseHyLyReXYTuPCfNZ02giPvnrz8XluqbGUX4eKN0nlr6_2yOOwR-jBKdCBEuOcwHGpx3anJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
شادی آرژانتینی‌ها با رهبری لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100439" target="_blank">📅 02:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100438">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_3IKrNCk2N9oYBL0nco8ii0TgnMM2knfFlxL5RMg-N9PwWUM4Mq_kuhpUKA0AbtOIhme0f2WfxaM6wj4_72YJFIdByREGo985UndZZnUg-bU_IpLWaV8zVcpxP5hOt5-wtiDHMH4mj8KwVFNEfpImdkPfGFMxm9eh8RXlUiWpCQG8paOVzSmmKieGVh-sYSB-NQvjJytXjkQrGAiJo59sn8Vr6XnNCNT9tlMBDMOzSaPfRikLBO5JPk7ywLJ_G2FmixwNBk1rSiqkhf2Ecf8HbXMlfSj0RU_78Tm9DBT8_71MDPQMm2TXW2EBL_L8ZmdBsyGZSkN9z7zcb9orBjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی و کافو تنها بازیکنانی هستند که در سه فینال جام جهانی شرکت کرده اند.
کافو: 1994، 1998 و 2002
مسی: 2014 ، 2022 و 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100438" target="_blank">📅 02:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100437">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100437" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100436">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎙
اسکالونی:
ما برای پیروزی به فینال می رویم و برای قهرمانی در جام جهانی تلاش خواهیم کرد.
هیچ کلمه ای برای توصیف بازیکنانم پیدا نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100436" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100435">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/100435" target="_blank">📅 01:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100434">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEPRntvfaBjUTkO53xbjhe7X_FsxnmWakF7iiSUV2tQhbI7MWLiu3rJcf7fpuOZ4log-P21_CPNg3144RzZQizsVFniq1S15gOcYroEw_RhyI1jHcw-Unoqhv26AHzad67PuQdI4qaNLPar3WnaNwOQbd8DXnXhJACKZI8QqmDRfICTbR5sG7CO-3GUzNlk9nhHPPNgPmrYAdRqqBlh4dRrRS9rVKGTkDSRWgB9NTqED9EJaQwsxsSqDj8V2wbdA1hhuV6O4c0AvBwzTCk7mbQU__CP4e7uVs1MeIcqFWcV9uM2CpXtNkuhlDKjU2WpOQosSt45msaF_i_6tsQQdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ‌هالند بعد برد آرژانتین
😂
😂
🔥
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100434" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100433">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4tCtIgF3acV78bYt9wGmLL4DZ-5UhWCuck1x8ILUBruIHOHr2XNHIzSkJxKB8jpoSRGsLVmiV9YUgE_-OiVasKUxXTqmU7zqp1eQ208EzTJ3781w0-QrkRp_4LT_3i6QJDvSat-1K5a-kIa1t2C7wFCUd8bZAazf5gxWj4ATkrXiF_D5feMSZBk-RgfYXPMOwGCBPuXWeIg9cC3PAKYPU-1gRe4i_8itRmSPJJyo6W-zZSPnpaAhV2o8IHHS3h412iTMVSABkBoszjMy6aanXiWbqgvpONRyYNn9v52gIIHxBL5yA-FUfQrX63pXMwGQMcMRdba3CXMR8nIjLaMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
خایه‌مالی سنگین گوردون برای بارساییا
:
سال‌هاست که شاهد تأثیرگذاری لئو مسی برای بارسلونا هستم و امروز متوجه شدم که او حتی از آنچه فکر می‌کردم هم بهتر است. از حذف ناامید هستم، اما می‌دانم که حداقل جام جهانی را کسی خواهد برد که دیوانه‌وار بارسلونا را دوست دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100433" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100432">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=JxdG1YfdNh3WqjcAS5fT0MqNC8X42_9nfd1r9Zg7lEy4hmfIB9AqabYlJAptXAX8ldJNPy2jzsEwnU0hFWqtBOAZO0NaBUYuodIXlJ6AwTghRf_86AGrNJ6D9bAuru1KS2ojv1KSMJuVbuQvvRX5_8BxUDZQj-BXyn-fnSeXFYVxvmiAjPLP4ezASTBgXyqu7xzBuBYrcM2GIBOLe3RuAtJ-Wf80UqNgRmJEQpjixx5q0q4IrO_aZ-Vo3LuvwjgCrNo9d1tKnawgtb31ZGOobZjT5VcRQ1N8NleMOyEUclALm8QIX7kh3pXYQ_nVe5DjPk8vVuz3sLYoXQoRnWvfk63YTv5S68YrSeTzSKKQsmlWL7JuHOJ45sTDAlHbKtelEfh9rGc9JXUWDc5EquwC9AOFZj9lhxZVL2bOEtGelO5I-gjLyOUuUvQklXo274VDj0yPJoQlQscfYvAC-VZRzB2YAxlLNod2N1Yvv90vQ0Tz4wYlVkDW3I3gOC6FRFFYkBexg9S7PFIQTVQUsSrNvw_UcHnwmVl8Fnnnhu0w5nQ2-pzXYC_DUDEP3CkzKZCpMgk5VJx-YZOuzlnKGL263ez_lqHwXl0Kme9m_QHScoWOtR_qsIvau0-WiasQM1htNhEOmpDWZXWNgAcls_mwOFgUD3GT1bEhOuDMoakZUn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=JxdG1YfdNh3WqjcAS5fT0MqNC8X42_9nfd1r9Zg7lEy4hmfIB9AqabYlJAptXAX8ldJNPy2jzsEwnU0hFWqtBOAZO0NaBUYuodIXlJ6AwTghRf_86AGrNJ6D9bAuru1KS2ojv1KSMJuVbuQvvRX5_8BxUDZQj-BXyn-fnSeXFYVxvmiAjPLP4ezASTBgXyqu7xzBuBYrcM2GIBOLe3RuAtJ-Wf80UqNgRmJEQpjixx5q0q4IrO_aZ-Vo3LuvwjgCrNo9d1tKnawgtb31ZGOobZjT5VcRQ1N8NleMOyEUclALm8QIX7kh3pXYQ_nVe5DjPk8vVuz3sLYoXQoRnWvfk63YTv5S68YrSeTzSKKQsmlWL7JuHOJ45sTDAlHbKtelEfh9rGc9JXUWDc5EquwC9AOFZj9lhxZVL2bOEtGelO5I-gjLyOUuUvQklXo274VDj0yPJoQlQscfYvAC-VZRzB2YAxlLNod2N1Yvv90vQ0Tz4wYlVkDW3I3gOC6FRFFYkBexg9S7PFIQTVQUsSrNvw_UcHnwmVl8Fnnnhu0w5nQ2-pzXYC_DUDEP3CkzKZCpMgk5VJx-YZOuzlnKGL263ez_lqHwXl0Kme9m_QHScoWOtR_qsIvau0-WiasQM1htNhEOmpDWZXWNgAcls_mwOFgUD3GT1bEhOuDMoakZUn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جو فوق‌العاده رختکن آرژانتین
🔥
🔥
🔥
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100432" target="_blank">📅 01:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100430">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMmHiGusV0h85B3IeEVxw49ynDsjLsdAWuD4Xqn3G4Z3c6YSTVyPW4Dvx11OI7uM6dllfU1EjQQiDFiRY2yBlAhVWGXpK5UbKO3xcL-Tz0cWWIhsOAUckkTEOj1x6Z-_prObkoC-lHvmzFo8Y1QjrO-EpQyGQmKk3IhJeUu6WyLUQfKYDKgboNtNP-Y1PwDhlj3LaSUXoQjCsHsras940Fv1kAMdZPjCFypitu_ZQygQ-01d6QcWVrdM9yd82DNSUr7sIP0TTUSyWntCbFTkxVhqWPFyYhXzRXEKC1BQ8cmWhuBJaC5p18w_JgfyUYl4Wis6kTBQGcxfZj42kWnSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
هری کین: مسی یکی از بهترین بازیکنان جهان است. ما سعی کردیم تا حد ممکن جلوی او را بگیریم، اما وقتی توپ به او می‌رسد، حس می‌کنید که انگار دوباره به زندگی برمی‌گردد.
😮‍💨
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100430" target="_blank">📅 01:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100429">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbN5kaa-jhSBRMWiC6hfIxpE1doSSsWYPcrOGSWstuzo8XfzJaN2AITzpeTj_LA8a9P1JTWfJaJuPJVL0zFknqvcHVHW5fJ2qBZ18CjzZQOaChoBaOiyWm5uJUXJw5mSxVsoDOSSqMduEXGf_mneIOYqyNYK1xaWV0ym-i2CgQzpqULgF1VIWv2BPNQc1EblvuQAxlar6g0UbSZKBST9LBFQ1slY2SqRpH3zU6AlcvKpQWuJQ-3_cLX0PZl0EqPC3GU-3yDOQcewzvxEdxXkTtP6rgsq_tIHR0BNhb4otxvWkvmC_4ABRVPwFt1v0f_guNq5TVP2mR62Lwfp943A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇦🇷
طبق آمار اپتا، احتمال پیروزی آرژانتین قبل از گل انزو فرناندز، 1.3 درصد بود.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100429" target="_blank">📅 01:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100428">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tigZaz52km2kr-8NGyomv0ZfIogIxSN4g-wGQ-YRRGc6oQ9spavGQ5F9Bf1e2kkQq68Epk2LvXZzZq-gweTGrozjhEmKN7rzJED-YQLi9Yfhg0PDhgam9VWnIRhxdYZvTmzsoEHSFiNXc6xHq_Y1tMf-bscSdU6iwiwZ8TJkct3Z94wVNMqKTqP-FJoYxKk-zFDQLxQmFfq4Rh_p-R-hxxVc_7SVDajm8AVzn5uoOKz4a9OEofgZrQHu8qDNtYaNJLi7kaAufsIMuQ9x_7nZ3jAbygWPuuZdwjpP9khvzzIzAmo4jACM7rxBUEy_Hqp_Ew1Ht4qPUmF5guo5bscVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
🤯
کاربری ۵ سال پیش پیش‌بینی کرده فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا سه بر دو به سود آلبی‌سلسته تمام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100428" target="_blank">📅 01:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100427">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkxJQ6YkCqKRoYcqfZ-gyTMo8s9WOZ9hXEMWIyrxaDDYPRCRR7aBpS7SKw7xEwpwrCZlrSB_3qWK90o8ZsXxOTNkPBTETiYvFtyYT5fSUwh8JLKda_nycu56DTsa2Ql-SO1LyNFYKRXdpVM6-anf6ZHHrNYgy3o-zBC9m07uWbZOsHuWkX3VVHDophdzKKk9vzXgpnxZHRaW9sOHUKEa0hxdGml_UsNaMid4IM__aiAOBLi-QU4-dqav_7UflyL0jOGAC3bMar3gBI4KcbjZJaDeVVcMapZniCPkHpDrzqiAzhJovaeGUM3Yrt0ZPxBfKNT44zH5OClwI-x2ybNLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
MOTM
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/100427" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KORqh1r5wjUcGdA2lig8GHfz-fUbWoCB2gLswnxA-c2GUZxYgA6CFv_7nbYQhYZ4vgeqhnoV9fEhCGklyHlrg9IJNJN-u0r2cHuqPUQONa8edUi5nrEw2CITI2oqevafJJcHjYQg4u_L4neHkO_soz05uqE13uqFmu4faa6kRz2UbqXYV2HqlebE2ahwS6ejyK-2ENjuPu7IqkkNupca_r851xgJb_IKZ84uGDLfaiuJ817coZ741SmUb3umh8351dOQuZk_oDjUQBnqUD6Mi1ujLI4r5lgu20vTcrcBewFoaAgXu8qDA4-jRqHNN4-P6m7AWsjLPG4Q7v1ICSLZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری کین:
قلبم خیلی شکسته. تیم بعد از اینکه جلو افتاد، خیلی عقب‌نشینی کرد. نباید اینکارو میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100426" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OITLkoAjsWNWaauDCq4chYRet50z3__k2iveHBAVXY7f54wQhQG66KbwXMsAK7IpPyw6iDtNFyrfcc3eYksMWEZg5-2KQRzFD8k-5THZkqx8V6xzuQ7p3q5iij0YrKB9KPjkNpFCZKV6PvhLgDkGZpQva1-ynTXelazfoNa6KfmswikrJPUN2VzMY2Am50X20cXMlO51UuLkbhtWBJArZKaVjkbwlR5gTuetq8pn8e2-im3s1MfCmllZIw-xT8RykcmCbRiAPrAE43RRKtxsxCodzSO7vYuJjVR9fLYve4_wA5zQTqzGcER2tV84e1LJe5mHpWn19342GLc8X4tEXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: قبل از بازی به صراحت گفتم که لیونل‌مسی یک قاتل بی‌نظیر در زمین است و از او باید بترسیم. او در این سن توانایی خود را به نحو احسن ارائه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100425" target="_blank">📅 01:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxRBPoKV_gob0Eme1sWswPZMnUHNUzf-X5o0Zb8Ny0o7CIpO4NBIB2W-jl7B6iybRG5OB1apJJYbK5GDpxHtes-1SPnmwjg_7BFqL63IsP4V49m8XA6HtQmGSPfzRtnfNm3bkJ04ORnYdfC0G_EFvIKhI6graHFj8swwIyhPgFXwUj56smkYtH6sGBd4gKhKtAppZDC3CzZkjQ8Rw9R-kocyPA_f5E5A8udFkC9n51_zd3d7Gzzn21KiUzUReqoeoeBF9FszZ2JEAkc6EoA2KzBo4gie5s6nYtlWpzGf9s_g9p0Z6R54x1ZKeRJ7IG0Z9Ud5QbvFIwonaM-Dg3s9Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
اسطوره، مسی، تا به امروز، بیشترین تعداد دریبل موفق را در جام جهانی داشته است: 24 دریبل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100424" target="_blank">📅 01:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzaOOq7xXt4Fq4tH3mvO12Ajl3c3VFNHvZYa9WnJ_b0tO_uaGT-Ya6JHMutpzT7qMGNAch9qoAVK25t_AGO2bdwMfJXssHChgpGtLeIdxE5hMV-gnhgB-EtsxtRyh4ExUpKgm0MgoHg0kOvTTYoctOX-aBTKlUcfU8O2-vzt5zLzvYwRBNXy1oG2bLt2LOjcBXzEmeDA5StCzrl0j_KIuf6W_9Q_U36qGnMPe-jHFI5dKDzQQnLQX7364b0iT6K1Zxx0_MG6mkCEhyTXQ1afOShI4g_4vpGtu9iVLb_O4579NTtQdfYP65UL3X3v-9A99VsMBZLkbIq-dCj79nx2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: شدیدا ناراحتم. نمیدونم چی بگم. بازی ضعیفی بعد گل اول ارائه دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100423" target="_blank">📅 01:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhTPlOh35Yts1yktNq0D1fSNN-8O8bzccYLEDGOMUBm---mQWtBWxqOX1b-f5mcwhGsLljCpuXVx0BEzBMWkS9HoRXQ4sP1kz5sAYUlm3fsO70FkIto74YX3N7Pv5XRTHNDPWi7joxkQx6GvJbwu-U_kDGC9LR59hygI23zcLOHG7FT1uPQqeUcPDdmjY-M_0Jen6PvXKUMOVZDkvWZXMLqTn05eIouPbxN-zZ5QR3etmFHFarwDmWBO9qsH4-wCEnch5KyRhTpdUbz6iBEPO4oAZRzT-EvdmRRN8SRvWvLv6cIxU9A6eRxAEs1A1155PHa4JL-gb7v8pm9MzaQEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100422" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfEvCYGH8igeid4qGh4IyHRsGSjKrMR4fs3Vt0mPOfoLNuMBuG-Djxz93_c2JqwYxNhFhs54Pf_zuNYbiHCJ7BT3l7iXVUIVJH8alryt2xvP62x7qDg9Xrew9M3Ybn11sbcWsTjbvrVhCSYdqyjnlDOdhLs6dOwIw0-sMe7A1r1YzdvMVXMYtBiGTHMoiESTKnWeauNmXHa96iscPmMgiqhHQaTU1mhl3fR4MFoqWti1cFnB6Av38THnqrqdNYrnAlkDSIDbTfc15Ib2rIneQDDwexEf7xxOQDJQlDrG4PDlZoXoYFmGAaAg3FqqgV7mQPVKcRjmeoi1tv5T8GJm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
⚽️
پست جالب DAZN: ‏بعضی داستان‌ها تغییر نمی‌کنند، فقط قهرمان داستان عوض می‌شود.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100421" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtsPl1FuDgUhYRZqWL5bsXhLEcKG9KpW8mySphp7zVMTpaCMdMoUJfqgLc7r4n7FWBWVswVFQB65FumeXhY9WWAAV1A2mpbYSGvzXNafDtyXEh6O2w091D4lQ_Pxh8-qpiJ6CF3ujFDAgEqBVAUGf-Xy4cUELpmyWyoHTO2AzzynL57wo1Re11TaHG_kA_SlwSqEGpPZ1oVssRCuyFi8U0q9ys7bMXafuJYvQZaUojlCES6l0tU38PEb0S8392TkKhSxI_jDykGnIgvFIqSvC8C_SDPi0hKmquP6bE3yJm-Roj_iIIRjeSrFA7iPIGxBk-Osmvl0r9pHMawcHm95Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
کلاس‌آموزشی احترام به اسطوره توسط آرژانتینی‌ها؛ کاری که پرتغالی‌های بی‌لیاقت برای CR7 انجام ندادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100420" target="_blank">📅 01:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d365933365.mp4?token=AfWFioQV-LaYpTbFhtv0B6_8QPAJRin-MYVaiLbV91uHwMbaMM2sVk09waZpc-crFJWBQej9pzRfPtU5IR6LQkZsavxFL_s98XBL8WsyWO5amf6slOltbZy5jaDKywslK3RtBkEL0OrpwUk3vJzJIkNfZGVQjng9eEpnxzvwxoG4ueysamBqTl27ZORU09Q5xJ94QB_B2MCHyNM3wLpa_mwBu7dG3fAlUynpXmg4zUV71ypjKZbzpcQsBf__EKoQ9wJW-8SbqMwmcYmqs-H3PenSqQ5I1jAu2sgrnFsJQaS2izJcoWUa8g89RMTDuTp7uY_iwCAoY6uViO9yzJth_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d365933365.mp4?token=AfWFioQV-LaYpTbFhtv0B6_8QPAJRin-MYVaiLbV91uHwMbaMM2sVk09waZpc-crFJWBQej9pzRfPtU5IR6LQkZsavxFL_s98XBL8WsyWO5amf6slOltbZy5jaDKywslK3RtBkEL0OrpwUk3vJzJIkNfZGVQjng9eEpnxzvwxoG4ueysamBqTl27ZORU09Q5xJ94QB_B2MCHyNM3wLpa_mwBu7dG3fAlUynpXmg4zUV71ypjKZbzpcQsBf__EKoQ9wJW-8SbqMwmcYmqs-H3PenSqQ5I1jAu2sgrnFsJQaS2izJcoWUa8g89RMTDuTp7uY_iwCAoY6uViO9yzJth_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم این چه سمیه
😂
😂
😂
😳
😳
😳</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100419" target="_blank">📅 01:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNvmq-PuzyImstubfSYps8YjtApsi8CO2mLmaOJIpYfEvzo0R8PHTDufdufzEZctpH53ahe68MpiHhbjI3LYKuq5btqn9p9VwNQYIHuuR18E16F9k-f0MIQdR9JWF9Un25W7FpOnUAauWfzFyCmwyyGRH8g0falL9bP6A5kbWuqBw9DTB6ZsV-FpvkKAhaocER5cvOr-ORBrnTTrbLLLOQW4ITIGyRPCXBaK0WnyNdd7H0ixMWYMxY6gTd1nh6Kqy3HwRLqmY2yaSsZdN5oiC6QQBeWheVmMi8bjaPUstciNdcWN_JK0Xh3lq62-1KbkvYrqTjmjxXm87mt9U4D69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
لیساندرو مارتینز بعد از بازی
😂
😂
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100418" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ_7spmtO_m8TNc0iMzE9UGuzjphpbUFEuyhbD6qCtOJtfLHjCbDYFEmJGQztG838zjF8mzgpLZ1K_d6_O74SiNCYBeNjxyTE8wCwj5GEY5vv7r0kSQi6cgazg-athvV7LHJGeEFGY1nlR2qLm804tDvcuIPGwsWhABurZJQxaeuKSRKTBHnFirtacGjrMOCpGQN-Jh0JHzJRT0yMvsA6dVj6-Ae3ZMiINDClu7AQWIKnr1KOd_NUzCjnEfo4cTB7EWW9f-TMfWlhjGNrHVVRn2rWk5te-ZMp1xgP_QgxlM6bgfsRSJHrZaubZNcV6PJ0EXJCd1Prnm1Bq3G0PugMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو جام جهانی و 2 فینال
کسی بهش نمیپردازه ولی ایشون واقعا مفهوم آندرریتد رو برامون معنا کرده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100417" target="_blank">📅 01:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqSfqGm-goAqRxdYR37GiZGYunVS8QJRtl-uFxCVYJrd6vvRaDfiiuMWK1kQk3TFU1itEH1sAGytppawDUNNd7336FtBvnUkJwTG-krNqHzgv0qAu6LXEmarWN35XvaVbvW5C9WYkQi_WWYMyQXU1Ja76y0il4NQoSN_8aDo34Blt2Sy8-MWCBHcdiUjX1j3dUrvCweAD2hQsvbCFiGvFtCpMOHaR-Y2KiQL9LAABQ9s-4a4IZm6jtLDWXvCtcqQd-0y8pXyGs0u6Kxk45MzbHGQmUHPF9JCFkqr3D8XVBu61zioCxKVdazMeWNKS6i6L9xvdUHJZUu60kiqA5gHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
لیونل با کسب 87.1 درصد آرا، در صدر رقابت برای توپ طلایی جام‌جهانی قرار دارد، طبق گزارش پولی مارکت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100416" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALSuTQ48jn1j9JiNgdo32KILj3hRFkhtbP-sU2FCehQTBpe0AWDeBr7mJpTMQWh5c83v_xM8oVEg8wGVeeFbUZH86QcuxJCW1O_d4_T4SutFw_knkHCq79t2-rGXrcZeFZF0RJ7ndJWgKvTC_9KGkBquVsARVvF4a3-cF7WDrrNqXngBrv4KuG19kbw3DsbvQferUabDQWVzZxVgBNeCHBHmhV4Ae6BfOICRlGIr3F5Pb9JSAmxjZFA-qX-5kzaelSBH7HD6QrnR4CPsxYGYwLEy2cmw2ayjf7m_IT8vWCmGVO1v6uqeazEpn1aL5oXcCJT2zJY311e5JMR0R4C4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک توخل بعد از اینکه انگلیس گل اولو زد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100415" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnPUd7X7xhy_5B7Plku7oR0pev3PuuMl8WRC3xUEw8V1jawFUPXJJgXaesbKVKLww3QNgxOJzE4hvjVD1vC8rEoS9tso-zlXFUUwqpOURDNyfnkKxR1GNYkd6RHBzhAjuYlsKnZUgiah0QeZtIBAa_l3XIHigFfginWiJKsS2lRIplnzAxHELNzhZaH_zTiZPJAIjJLNM2GbhhnF8s59a5SvmIJc7q8InvHo8dVKnufviKfyf9jyO5k798O-e3V_FahktoGI0-jRtW0NrA1M87TDpGY3Mu5G7_vV_62eboKgXNo5qOkp8nMdW6RD5ql4RpiVy16rejS7tvw9VEjk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
ویلیام سالیبا مدافع تیم‌ملی فرانسه بدلیل مصدومیت از ناحیه کمر ۴ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/100414" target="_blank">📅 00:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100413" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DDJ948n9OwAthXi6NjoeirURRJT1WA53BiNFcUtUKinV2P3alTjcRZQA5fr5K9g7mLqcHYP-cSXjX0nPFX8BYi9dGdrQaD0ZaSN5Z6b4nbo3-iiHB8FGqnQPIJnpV_EGNdTdY5MjJ_Q_wOOU1m_cYzzaLd6BNcK8tujvS25QRG9H__zL112hopC2DEvfezuDGabYHW3eJqdQImHH0FiYzU5qhHMrKjecAA4rgWDwmWTCNRp-Dwt5rSx320hda3Xwt0B7e8A3YUNIwFYxgzJRVJn6F9TQB_e1mdW8BgZ2AO9c-VU2bbJMzbkFZsx8ELBYPIouiouY_wLOwv-O-9euVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100412" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
از الان بگم دوستان رئالی - بایرنی - منچستری - آرسنالی - پاریسی - بازم رئالی - وغیرررره
بازی فینال هیچ ربطی به شما نداره بهتره نبینین و‌خوابتونو حروم نکنین
مرسی از توجه تون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100411" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9T-pXaoZ_jLaAx1D3Pebqlf0ypLylG6ZLK7KuPHaG4-BiUihc1tjt8lByKqPJSva4RX8rUyjKtG0Fxtj7SirfY1HuCuzqJeydWNfcd8TmlxcnWj4fPpP8cTN5ZMzsz9rvhxURSPW-zHp-yrgKbjMNBMc2ew01_PR7Qixw0icq6MYjzwMi5cHCyUmyarQ8d0lc2xwupl7gqZ2dyUe1trvhoesg94vAaKdoWdXECADqRyUZJaNnhANphgSxjeUk5HdPbHxTJZPOK1icSx41KXsh3bjyc8CqaGR-uMpRJAu2U59Jmse8DdIKi0lDtP7NYMhhXmpi_h2tsvf1WFg1cZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روباه مکار گریه کن پدرسگگگگگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100410" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
هری‌کین: من بسیار ناراحت هستم بری بازیکنان. من بسیار ناراحت هستم برای هواداران. من بسیار ناراحت هستم برای کادر فنی.
🇬🇧
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100409" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPLZXhPZdGWtULzmk9ESjYT5I4M99hRXygtjkxn_GIV9uwVh7lrizuB1z22lOdDfcF8VrZaF6RiQ39Nq4yqQHmjM7_n_2gSx5vzNKroG1NWR1TA11g2PYYfcbe7eNWNDBTKLrRhLirqp6wjVaedP_Lic1gyFIhgOb-AT5_bKKSC4InzWBmBxve8WnmxZ7iu-mIKPzTDlxPNftEpSt_kATos-DnEH_7Zn0_mYNm1XB4Dnryypcsfun8axpC8OYv4OYT06JGqlzP_d_c4H2iY2oOEoPFgISpLT9OFjhZ066L2qOwm2_F8h2WGzbdXuzbhhQ9wNTPkRisYBMCjNwFfx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4OWfhktumlPhsanO9o2D0vW72Ol3bv4MmPttEkWmSxuCIXH6SQkuFa9Z17Hk6fzA5n3eEvTDErh1dhallaD4mkDhUmFKURyg4uLiXtUbO4vpo2sIAUrF6Apxnvs2IYJFTy7cwSnB2AqVdsBWRxBv7Vb5LZ5X06eqNFs4ygIvEKKYR4MlgEPT81DpQbnoJn5OIfgmAoYyy6xuZAnIpkw9w5ixkeRJSmn5OSqJhObz8FyQ2yNqr0972ZlyjldEpnFQDIcdWuMmbP54cOhP5t9FJKN08ezdyNe6lDAE16NKVMcXVMpLi7WfR2zr0GiDNcVwnGh9Jw798lAqbopEu9Hjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا بقیه هیچی، چطوری دلت اومد یه کاری کنی دوا لیپا ناراحت بشه توخل احمق؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100407" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100406">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100406" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUyluUtgS_In4zfm3XwXKgMwJKXL2CTnbChORGtxrvZYQrHfd4ei52C4ztlHIIm9bCWCT-MZqLam0CS0JrE6mRfAh4WW7znwtRyEtdNFSivyLFEI1ZcVWPYS58POVJc6IB3z8unf7NBBTr_7Kn5SjW9TdMrkGxr290F9OL6J-mJAUWd0J52-DZxRyq4W5_UGFqwTmIG0-87LgPvrVqn8yB8tjPy3poNZAP1wPGVL_g3E_goIFhCtpR2a3Deu58yHujUmPlD1d3oeUPZYRu4qUcpW5ZSN_1IY1Xy17AoA9YSHANXvMAWElq0OsDc3y1-5yKiVyMHBzBqWE3kePv3qDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعویضای توخل بعد از گل اول انگلیس رو باید تدریس کنن تو کلاس‌های مربیگری تحت عنوان «چگونه تیم خود را از هم بپاشیم»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100405" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100404">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100404" target="_blank">📅 00:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100403">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100403" target="_blank">📅 00:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100402">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100402" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100401">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/100401" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTO8RvUj1RRkcDUppaClFTWQ8G2WasVSIHHSAKAKNvKp6KmIspICXvLPNQcu-5Kph2nhVnpCxDRtkS5IY_DtE52I3hemSrMP3XHDoTgAg8HNZnIBfbvOIaGAphCwNJoShT1pLSMzF4_mvT3d4ktOxbg1PUx11eQyqkDM3MyuCv1gmMoGQtRINvRIErbJ5zMuRBciezTB0-azBAsegkSaZ51ZKcTvwFAWvMOqS4Nkvhi6HM8vLAMTTj4oFw1ZdAzsm-b_Hux7aGP8NEjOp0PJoaFSUXCQBHNdnQHbvd0RoxEol60xiXR57xt3jn_WB7BqBlg1CzuExRRzfFFFnM15tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100400" target="_blank">📅 00:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs958GnhsARA9f8SlZLiklzRtcXU2ar8N2VbPrwsRwS5dcS3huyUA_Tl6yefNoz7b0zdWhxhELLFMsAkSgFLHBGAqmO8GDvntRVLpM4H_Ev8ztx_U2C6n7YvvHZryO1H3vywIqSmo9mFSIdy77JRWzGzfxFfnxfWV5XrfPM3rxD_-zYFt946h1LBwH84n3LinqGS_hDZuQUOW27_ZJmbZ5Od5pQF7IEtu3VhNIvfb0RKq-tLqC8tnmOPFWJEPvJfZ9nG8IUmIyq1d5SgCcmlotFpDOFLHY4H5wgz-y8l9URPsed4sbdbtb28O3hfKXPVHC58z8TOWhKEqms6Wlh1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی، اسطوره فوتبال، با ۱۱ پاس گل، رکورددار بیشترین پاس گل در تاریخ جام جهانی شد.
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100399" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100398">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100398" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100397">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOVLaLymIRrKLb4EaZVOnZLw1tp0fy2WyakcQfkIfL7xFPhUUl_r-JB60-dLK4em6-omSmXcGYldQq6JEi_5E_2Rm8CsoTbqFTiAXaRAl804-9j8XhTfNI4KpPspfMvFADCUNZ5I0FBPZROfnHuJi-40rJVZ42L3yBorltnxWrXQBgPB8ucpVwVWUooNUD1OJJUPUqFwP-vde7M9Nmo2msuRLX9hZVKTJixbagPUL0tXzI8sEOHKFn8v3GrHfxojotu0M8-fCiMRwRgYuMauqpFHGBUKsu6ZrR5BJhdNTDTfDHnQ63_nfcviPqdWCkvJu7esWc2O1sdFdDi7rEbAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
#فوووووری
از ESPN: توپ‌طلا جام‌جهانی فوتبال به یامال یا لیونل‌مسی اهدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100397" target="_blank">📅 00:40 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
