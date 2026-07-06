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
<img src="https://cdn4.telesco.pe/file/uj3oj40kWhW9OP3fKi7TzvQqREeVC10_UiJKzSzUDOH3Rtj1i60XZ6RSpNeNo4ezQQJSOI6r0wfEC4dBC9_rCI95Q_cdCWNH8BC2VWasfGgB-JBzd4VtrxdGDML-J29Dy5S2LV9UFrLVG7HulKEM6ZfABw8IzIvBcvYn6joamEuzPoxzBF97Jf0VzvmwMptw8jy_asIvK-IQuTa2tBH9Y_tJc2kCU6UvTV6axICsJmPfa3HxVQqjeSdd3i7xLnYCF5MVtzlCZqYAYUQUtNHK5Dl6hE3frUmuc_bDZcy0MM1Y3VDBFKG32xEfZqnUZWKs-5HKU0HtHQbNOsRXMwE0eA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 01:22:22</div>
<hr>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔻
‏الإطار التنسيقي يجدد الدعوة إلى المشاركة الجماهيرية الواسعة في تشييع الشهيد  السيد علي الخامنئي (قدس).</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/naya_foriraq/81263" target="_blank">📅 00:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8qcJFhrob-2ZY3kdgWrw5s-Hl6kRySddYSyAoOF7xlsWsy1Sfe_EPVUZKp7mPhnLLguMO-69n_HMCoSbuEeYJQP6tlosEOcHiV3yONd1rxM2NkrvFpOTRov9qF150Dr_mHLCf972CT3hQ-8FDxCwjM4BXB71n2szjP6gr6q_YbD4ysoVf93jaw_gsSBH6jb0e1Nfk4QPj5DHGTrissdwcDvs0K7UgtPmyXl9rhF78fA7Fnw0zITyEBvc5XwuxI3LIG4YueL6BHWiDoHnnLDCn9y9rGURrCU77w5xc0ZSr_hHqWreFEw4PVrXFF9pyE-6pySuqLiaaXyDycNkn8_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROVK5LQS1jA_qK7_LJNaxCg4GjyRwKaeE6G29p2jTakRY7zS8JeUoJmMidUv-kGNLbJe3U3iDi5vH1UXL8M0PNqXN6S09YE7HWiYR4t2-YUlaE96x2oTA22AUMlOJ60Hul_zCrGq_B41gLIbVWV0MV6aWHeEjMQCH8D06FPOcd3ZKk8XJITtuQ2lYIAbNwAkRWvtcmYgB5tSKuAZF71ZXnOqolaxJOx-iO69BoaAighK9l8D2zLXt60ld3xingPMAm5yUtk8kUCIz6UngZQ7mP7VVP5Hj2edihbDT1WvMHne6oHHUNKG9hEp5oKQ_sCWsdpQlSlpza2bybCibTjlJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlqWQxEg6flx3ZHWnyCVGXrtMOONVvhbN_lMh6g0HIoyrnqPtW83rraJrV24RcWTfshf5Fm1EEemstQFa4KdTPHInxXVhJMboGBp27G3hbOYyqHrV70HVFK-RCFt2HjvU88M8A4HaSQw_2ssgf9n7bx53JoyfNBzbJ6S5IHvbl4GQM0h68s6QJMQL0_zqt_yNG2ZI8aqrYW93C6bsxNuw8I3jBBgJ62iGD5kl77-zw7sQ5FWDzOyGeYbjJrRHit5ijnc8RvhGFe2CXKBq-XriphoSsKBQ_s_4CQiNk1h8-Z7BbIzQgq_FqpmPsluF_rnGIOTQWwzd1AshAQU0RZ6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mb1RVeG7N81DNd3i__uUFFntkszuF4BiUFMSC3uj6YExUDbKGbkhqKy3a2TwDhc6GVPHnXQzEzfuCubN73Dt0z-0SH1joHXKNkpmDWzw71skqVRKFPVozs7B3MFQ_8kBHEREiXa7zAigi0SVrtzYZRyPXXq64KVMiBZpvULGpRGLUDUqfA10kdb7BRslPATBAMUH6aUOjkmMZ-CcV21Nwh2u1DMhX1zEpEYHO0JkicJzz8ooDO-O498hKIxLHNuVrDa0X69YEtumZT7qNNWxQhFxTmUs4-ayLXj8nzA-dpEIbLvwLqvFH7vMDo889-O6aE1ZawOFkNc6iBONmpsb7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
تواصل مواكب الحشد الشعبي تقديم خدماتها للمعزّين في العاصمة طهران.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/naya_foriraq/81258" target="_blank">📅 00:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29b0ce560.mp4?token=h_Sqd9jy22mZKBySMWmEFn5EClnlw6WAhQVVxcbdOl-zRqHTK8yTVy1P1m1dVdRvFHOuJ7QQYrN590dhmuhLQch4NEFH1e9791qB10rfc7BSAK3_4aPgXwxqQtvIEIx6FWJlhUoCtPaLbx2t4qvL-WQOEzmyHigiKK0d1iLlpzsBe_8Ok7uaLw4tTJCK4d91YRg4ST2eQgyGHuY2KZ9C7cAjU91xI03ae-6TmPp0ij3uk3JPQHFbAjU-ZNCa85vtn7tn8NAfNA7n7vT2M8cnWepvfnndNuutKaAcHyvLlM-TtMnEQaWvleDiOpqzViZ8LJ4pC2Qj6O-IvYRIVcYi_7ugcPN6m8tJn6wPGEaEFLZt6PnXG7taHmqE60Qk3Lp_t3RGnto6ncYbUg4xY_vQ2trR3zc1-NYG5JE8YULji8Hdka48-VQzdXCPpvwCkfcimHSm3U5x-T38JQwogogXCjVVFcthri085zbNTecuzVqRt3d8K4Q_-UeJN65rJI3sSl03Jjh5eID1tF5azT1bWH4bzgs2Kjvqd2ViRDxypDUAiNLRKZRhoafzhfIGxPRHCmpaPjDAfra4sgCjho7JXb4t4_V7PqRfoKQk1f5VLfQg7EjSZCCOTyvSHPC_Pe_MfZ0CSOMnXXJSK99vj90WShQkO3gFEGtLzdcrG6HBch0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29b0ce560.mp4?token=h_Sqd9jy22mZKBySMWmEFn5EClnlw6WAhQVVxcbdOl-zRqHTK8yTVy1P1m1dVdRvFHOuJ7QQYrN590dhmuhLQch4NEFH1e9791qB10rfc7BSAK3_4aPgXwxqQtvIEIx6FWJlhUoCtPaLbx2t4qvL-WQOEzmyHigiKK0d1iLlpzsBe_8Ok7uaLw4tTJCK4d91YRg4ST2eQgyGHuY2KZ9C7cAjU91xI03ae-6TmPp0ij3uk3JPQHFbAjU-ZNCa85vtn7tn8NAfNA7n7vT2M8cnWepvfnndNuutKaAcHyvLlM-TtMnEQaWvleDiOpqzViZ8LJ4pC2Qj6O-IvYRIVcYi_7ugcPN6m8tJn6wPGEaEFLZt6PnXG7taHmqE60Qk3Lp_t3RGnto6ncYbUg4xY_vQ2trR3zc1-NYG5JE8YULji8Hdka48-VQzdXCPpvwCkfcimHSm3U5x-T38JQwogogXCjVVFcthri085zbNTecuzVqRt3d8K4Q_-UeJN65rJI3sSl03Jjh5eID1tF5azT1bWH4bzgs2Kjvqd2ViRDxypDUAiNLRKZRhoafzhfIGxPRHCmpaPjDAfra4sgCjho7JXb4t4_V7PqRfoKQk1f5VLfQg7EjSZCCOTyvSHPC_Pe_MfZ0CSOMnXXJSK99vj90WShQkO3gFEGtLzdcrG6HBch0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بدأ نصب خيام المواكب الحسينية في كربلاء المقدسة تحضيرا لاستقبال ملايين المعزيين باستشهاد الولي الفقيه الامام الخامنئي(رضوان الله عليه).</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/81257" target="_blank">📅 23:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81256">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ffa92b16.mp4?token=EQFccqEZP8mOjZ7NYqggaGoV9ceS2ueoFb2TYiduVQRUWqRnVXoufE9sPhTlyMcAqAuwXwp_XSaAzbHujrFGnw0FsXb6MKf11VkXAk6gGhxPIVvqxFddIPdploVAODMVCGT3J2qTqzj1GebFzsvn78DiuXYjvZ8Jpt4T3npHcD5EngHMnPh57OitqzdaKaD6xIE-jSGSdyxqQ5J1WYNZgLyoMlA_Yy9TpHbjbijXPazQUGjhRIF0CmA3RdJcx4tvkzhQ_yOgddT-adyR1uV1X2Yvv88qs4mqFPuZ2uYKKwZnxRJOUjksf7iUHKQPcBFFCzNzAFFZ6-xgmPlqhLhfr3A3-DbuZmufyq5ki-g6sgRyqMDZSZGb9bWSUDP5DjsW3wIJUWQCDssbhJga39Pj7gWBdnt4BX6YUnIInIk18nZr2rfBR_-KqQEJW4-4OPOnk8hhh5mQj-4dzB7RmKXVChbO6jn1yKENuVr87clr6mpuzW6OBE1aBbK1uGK3LNDb1gJ_zZ-cXFjINNZN1KhfUFq_OjIXInf6Oo-YPB8MM32Mv1KkOqNt2K1r-J7OTfdbniiPPz0U6dbkyp6F5mE21FtftD7eSUt6g4RT4FPZ9iUSb8IvZBssogPDuFp8kCB76PJTTgXLH0WeeYEe11K4eVpO8LEq8yPfl7yYr3VEEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ffa92b16.mp4?token=EQFccqEZP8mOjZ7NYqggaGoV9ceS2ueoFb2TYiduVQRUWqRnVXoufE9sPhTlyMcAqAuwXwp_XSaAzbHujrFGnw0FsXb6MKf11VkXAk6gGhxPIVvqxFddIPdploVAODMVCGT3J2qTqzj1GebFzsvn78DiuXYjvZ8Jpt4T3npHcD5EngHMnPh57OitqzdaKaD6xIE-jSGSdyxqQ5J1WYNZgLyoMlA_Yy9TpHbjbijXPazQUGjhRIF0CmA3RdJcx4tvkzhQ_yOgddT-adyR1uV1X2Yvv88qs4mqFPuZ2uYKKwZnxRJOUjksf7iUHKQPcBFFCzNzAFFZ6-xgmPlqhLhfr3A3-DbuZmufyq5ki-g6sgRyqMDZSZGb9bWSUDP5DjsW3wIJUWQCDssbhJga39Pj7gWBdnt4BX6YUnIInIk18nZr2rfBR_-KqQEJW4-4OPOnk8hhh5mQj-4dzB7RmKXVChbO6jn1yKENuVr87clr6mpuzW6OBE1aBbK1uGK3LNDb1gJ_zZ-cXFjINNZN1KhfUFq_OjIXInf6Oo-YPB8MM32Mv1KkOqNt2K1r-J7OTfdbniiPPz0U6dbkyp6F5mE21FtftD7eSUt6g4RT4FPZ9iUSb8IvZBssogPDuFp8kCB76PJTTgXLH0WeeYEe11K4eVpO8LEq8yPfl7yYr3VEEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استنفار القوات الأمنية في محافظة النجف الأشرف قبل يوم من وصول جثمان السيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/81256" target="_blank">📅 23:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81255">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
محافظة كربلاء المقدسة تعطل الدوام الرسمي في دوائر المحافظة يوم الاربعاء لافساح المجال لأهالي كربلاء المقدسة من المشاركة في مراسم استقبال وتشييع الشهيد المرشد الأعلى للجمهورية الإسلامية الإيرانية اية الله العظمى السيد علي الخامنئي(قدس)</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/naya_foriraq/81255" target="_blank">📅 23:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81254">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c715d310e2.mp4?token=gtsLQUiagApuoOyluy4YmVtlug45gMmulinctl94-qyYFhDlKj-k8DOHjriDoHePUrEI578NVUafbAZ6tSu_GHodW04nFyMVoi7h_rK-LVxWyfVLHC86AXEt3XHqdnri6w9Zv3fZ43tY3SiN6moT15fJSgvZtfi_F4gq9OILSknImbxoqx7S88DEiOHh8QszoNn3iVyEsvVfrCn4uvyNTLZdh6Cm5xHVW4qP1JTirC9OPw7a1WfH3iMm7ev62ao9WTir9ZbSjVaWy6mFPMn9_x1KJINA5OSdbF18lSHkWcoq621i5qeVxK_hk_FCUt7ExYcpv0MZIao48jKHlDHnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c715d310e2.mp4?token=gtsLQUiagApuoOyluy4YmVtlug45gMmulinctl94-qyYFhDlKj-k8DOHjriDoHePUrEI578NVUafbAZ6tSu_GHodW04nFyMVoi7h_rK-LVxWyfVLHC86AXEt3XHqdnri6w9Zv3fZ43tY3SiN6moT15fJSgvZtfi_F4gq9OILSknImbxoqx7S88DEiOHh8QszoNn3iVyEsvVfrCn4uvyNTLZdh6Cm5xHVW4qP1JTirC9OPw7a1WfH3iMm7ev62ao9WTir9ZbSjVaWy6mFPMn9_x1KJINA5OSdbF18lSHkWcoq621i5qeVxK_hk_FCUt7ExYcpv0MZIao48jKHlDHnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء مراسم التوديع لجثمان الإمام الشهيد في مسجد جمكران</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/naya_foriraq/81254" target="_blank">📅 23:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
محافظة النجف الاشرف تعطل ليوم الأربعاء بمناسبة مراسم تشييع سماحة آية الله العظمى السيد علي الخامنئي(قدس سره).</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/81253" target="_blank">📅 22:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4f292302.mp4?token=W5AJG9z8_UUEcaMnLd9pmmLl3h-1Y5YniMNg56g1KT07tphNlHY56axL-xEYThLykqCy7DNrDTOb5WkBrAnqYDpmRWM3o19W2coBxnCyYYDj2Oo7Xhb07B5-dtnCZb8xt5QKqiYbMTTDgTYUZRnM7u7rSjPkgfxB1zVZv9MHRS8s9MSYnW8PhbjKE6WxLYB0rXJPIHXX3XEe-kXS3aedmfFUJ1VhZPHu8xtUECNM6cMDr1av0c10UzU1ie-FB_CG9ktfENjpQwG7KFHwIBkI1VgI79LaQosSXoE4aPwk21sMAZXgt31cOq_vf_YXKuaFmDQ35tUkoVJPacxRKh2pPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4f292302.mp4?token=W5AJG9z8_UUEcaMnLd9pmmLl3h-1Y5YniMNg56g1KT07tphNlHY56axL-xEYThLykqCy7DNrDTOb5WkBrAnqYDpmRWM3o19W2coBxnCyYYDj2Oo7Xhb07B5-dtnCZb8xt5QKqiYbMTTDgTYUZRnM7u7rSjPkgfxB1zVZv9MHRS8s9MSYnW8PhbjKE6WxLYB0rXJPIHXX3XEe-kXS3aedmfFUJ1VhZPHu8xtUECNM6cMDr1av0c10UzU1ie-FB_CG9ktfENjpQwG7KFHwIBkI1VgI79LaQosSXoE4aPwk21sMAZXgt31cOq_vf_YXKuaFmDQ35tUkoVJPacxRKh2pPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أهالي محافظة قم يتجمهرون بانتظار تشييع النعوش الطاهرة للسيد الشهيد علي الخامنئي وعائلته.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/81252" target="_blank">📅 22:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
محافظة ميسان تخصص أكثر من (120) حافلة لنقل المشاركين إلى محافظتي النجف الأشرف وكربلاء المقدسة ذهاباً وإياباً مجاناً.
▫️
سيكون التجمع يوم غدٍ الثلاثاء في تمام الساعة الثالثة ظهراً أمام مبنى ديوان محافظة ميسان على أن يكون موعد الانطلاق الساعة الخامسة عصراً.
﻿</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/81251" target="_blank">📅 22:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38afce1093.mp4?token=Q2qPDACQBP1A9XuIKKsabC8jNBUYTkOEt_1Wvil2AuU4ZA3JAYZ5w4yeZS1s6c1XYhO-uBf0W9Q7aMcl7A__1nPGLRzHMiUSFmha3YDNQY9x2VIY0PPO47YZYptYqb3FsdEZOM8urGLix-VrQfcxITbH27nOifb9usDSzcWsY1HI-2NMgi6e8ISc3wkWeiclbcixMJMb_wLCOYDxshCo85ciHytydcNoxLpehDKT8MdzUUtmD67FA6FMVudMFFKzTscPFDeE_7sUbExqmNveVzhtqPwC8Y_jGj6vlhtmP8FFIqVpGhNTV28V5gEkD0BX80aWUf94qrHWtIYwY1p1AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38afce1093.mp4?token=Q2qPDACQBP1A9XuIKKsabC8jNBUYTkOEt_1Wvil2AuU4ZA3JAYZ5w4yeZS1s6c1XYhO-uBf0W9Q7aMcl7A__1nPGLRzHMiUSFmha3YDNQY9x2VIY0PPO47YZYptYqb3FsdEZOM8urGLix-VrQfcxITbH27nOifb9usDSzcWsY1HI-2NMgi6e8ISc3wkWeiclbcixMJMb_wLCOYDxshCo85ciHytydcNoxLpehDKT8MdzUUtmD67FA6FMVudMFFKzTscPFDeE_7sUbExqmNveVzhtqPwC8Y_jGj6vlhtmP8FFIqVpGhNTV28V5gEkD0BX80aWUf94qrHWtIYwY1p1AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سائق الشاحنة عراقي الجنسية يفقد حياته على الأراضي السورية نتيجة انفجار شاحنته أثناء نقل النفط</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/81250" target="_blank">📅 22:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_QHYOgxaXjQoYOm3FxuKGB7aW-VNswHO3kIOSUaIRalf44B91QtXwzXqoJJyiVusqxoLFj_kx-OrxV6KxCjIDl8UKTxJ9KWNXABXopXYgnURTT07rYpzTL8-8KOD-R1vZ4Y53VJEyVSapUQUlkU0uf2iD8SDkluxwj0AfOhyhP_ELNcB9stzzIkuFsq-rw5SBNaySvjK6sjhFUekng_LXj5PfYYEbAS30AFGDgDJOey1rmmcWzG7CrDwVbN8OZjuHU8eZhkq1guCc2mHHki0K1kn2bAdSC7KHdxAekWfvXh8NwguJB9U1cE9AyBdx59rMX--Vr1Lkj_0pT4tVEZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الصهاريج العراقية التي تدخل الأراضي السورية في خطر حقيقي وفي حالة شبه يومية انفجار صهريج نفط عراقي على طريق حمص طرطوس.</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/81249" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81248">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f5055980.mp4?token=BctxaBt2d0soup2l0C7Zb3k-wCWqDnauk3Knzy9ENQiZ-fpPLlyGaescH21pBWuktiMEMpCJeXW7NMFdJVrNbPOsKN2CJAzyQP5wqpQb_mIRZdkkQUYY7jUe0qU3dlNqK7gtcIpK4RiSTf2zthpb8U3aPOBamSCKDuA5fnY5HYXE1nlHVWWslEltAyyvUHnVBFqsPc0PKQaRNV9bBOyJBe-8xMwq4gNxV8YUUDvKmbcIRLguraO8wiBTO7lhDPVrDMb8AA2YlHHYBcCAt5YrM1RNm390rgXIVntaMR6ZZr90nMuy98CXC51CpF873FVg8TE7Wv5lknh_d9cgQpljrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f5055980.mp4?token=BctxaBt2d0soup2l0C7Zb3k-wCWqDnauk3Knzy9ENQiZ-fpPLlyGaescH21pBWuktiMEMpCJeXW7NMFdJVrNbPOsKN2CJAzyQP5wqpQb_mIRZdkkQUYY7jUe0qU3dlNqK7gtcIpK4RiSTf2zthpb8U3aPOBamSCKDuA5fnY5HYXE1nlHVWWslEltAyyvUHnVBFqsPc0PKQaRNV9bBOyJBe-8xMwq4gNxV8YUUDvKmbcIRLguraO8wiBTO7lhDPVrDMb8AA2YlHHYBcCAt5YrM1RNm390rgXIVntaMR6ZZr90nMuy98CXC51CpF873FVg8TE7Wv5lknh_d9cgQpljrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الصهاريج العراقية التي تدخل الأراضي السورية في خطر حقيقي وفي حالة شبه يومية انفجار صهريج نفط عراقي على طريق حمص طرطوس.</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/81248" target="_blank">📅 21:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81247">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovd01rUJjkuOwB00GzVsBY_dR5pYhNH10ncUCLvAIkgHZbxk7SGNKWq4QjE8_dfRXf_UH38HXw_EdmHMkXJAolrT04GqUCRN4-uDGJ4gLGb31HnbysI3YsvaktE3unwGBVBxtqhK5vnW3csScvZprhfVLZoiRfmH_PQdrTRvatra0sNP4ServDiuvWVbKEQFSPF6VGhR13VxCbivdZ0YrTKsdDQIvBzX30eX7EJGEg30Qa8KteSkGKgPBB9OEnv1Wg3MSZV6g7Oc-dHtULZe-kKLgpBImZTxKStY984IJCvOI9lSxk4Ipc0Mcpw9fI8RBAy653jXdDqRDGmg1gzCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سمح بالنشر.. الشيخ المجاهد الشجاع أكرم الكعبي دام رعبه يشرف على عملية تحضير صاروخ جمال ١٠ المجنح من عائلة كروز</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81247" target="_blank">📅 20:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ظهور سماحة الامين العام الشيخ المجاهد أكرم الكعبي دام نصره وهو يطلق بيده صاروخ جمال 10 ثأراً للإمام الشهيد  انا نايا عندي كل الخفايا</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81246" target="_blank">📅 20:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e74022703.mp4?token=ueEMZ4KmiJw5wxOxfs8ctnpwDSE9o0q9pdOwbCkSZcVDJDdKWHkmgaUB46g2d7RiGJk9Ftr09VhFFxrBR9KrPcJNCX5ffjtDe1-5D98bTTi3t1Ohlpl-UXFTlcPaaNPd-NMuzUzp6fQ9qTrXIhac2Uyy7htsRYhhzJsgEQprGz1QbzAn2ewnDi2oH7B7Jhg7kxAcL7iIF3nyyKhiwBgifPtjXoqw1sriU7RvXOBU3yaBPMelyL2nu6wWVbPxDFPulZ1yY53-lQ2R9tn0rUO1H5w1JfgCcw-scZRndYYvbg2Uy23ZJmyx_-pgKpOENSGG9eve4Pd0BS3AaiTZM89zGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e74022703.mp4?token=ueEMZ4KmiJw5wxOxfs8ctnpwDSE9o0q9pdOwbCkSZcVDJDdKWHkmgaUB46g2d7RiGJk9Ftr09VhFFxrBR9KrPcJNCX5ffjtDe1-5D98bTTi3t1Ohlpl-UXFTlcPaaNPd-NMuzUzp6fQ9qTrXIhac2Uyy7htsRYhhzJsgEQprGz1QbzAn2ewnDi2oH7B7Jhg7kxAcL7iIF3nyyKhiwBgifPtjXoqw1sriU7RvXOBU3yaBPMelyL2nu6wWVbPxDFPulZ1yY53-lQ2R9tn0rUO1H5w1JfgCcw-scZRndYYvbg2Uy23ZJmyx_-pgKpOENSGG9eve4Pd0BS3AaiTZM89zGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يا لثارات السيد علي الخامنئي  السلام على الفارس العراقي</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81245" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81244" target="_blank">📅 20:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنون - NOON</strong></div>
<div class="tg-text">أوبريت “أهل الإباء”
إلى الروح الخالدة للسيد الولي الشهيد الإمام علي الخامنئي (رضوان الله عليه)، وفاءً لنهج العزة والإباء، وتجديدًا للعهد على مواصلة طريق التضحية والثبات.
#كنا_ومازلنا_مقاومة
#كونوا_احرارا
ً
#
قوموا_لله</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81243" target="_blank">📅 20:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
العتبة العباسية المقدّسة تكمل خطتها لمراسم تشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81242" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3df93ff3.mp4?token=vNwI3np4M8zAsxospLoH0CCfL1nR5497e2TJQvN7NcfmAuKrlM3wLVFDz94pauPwwPX36kIL4fSKP6mBOFNhf_72kfCJiDC33XPsmOCS6FD_XSndi_Q6A8ASSDTxBYCfu9u6aMfVU7ntlcTuYbaf6N2DEl0_j0pYem2FeXVWNdBsrkXt8I2pXBuoK2SRzUrdXXTKIfz7D_Afp01HXPIcGm9uFNl6OURFfoUcV6H1obhH0--N4m_uzVStS5HTglsSU51KRRv1P9YLGc4P6JePlvZNdoGiSLL-jSVe7TYQYvMKICbo0h7cr8tXY5oU0GIzvGivZ7_aMmjHbFH4fZ4GQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3df93ff3.mp4?token=vNwI3np4M8zAsxospLoH0CCfL1nR5497e2TJQvN7NcfmAuKrlM3wLVFDz94pauPwwPX36kIL4fSKP6mBOFNhf_72kfCJiDC33XPsmOCS6FD_XSndi_Q6A8ASSDTxBYCfu9u6aMfVU7ntlcTuYbaf6N2DEl0_j0pYem2FeXVWNdBsrkXt8I2pXBuoK2SRzUrdXXTKIfz7D_Afp01HXPIcGm9uFNl6OURFfoUcV6H1obhH0--N4m_uzVStS5HTglsSU51KRRv1P9YLGc4P6JePlvZNdoGiSLL-jSVe7TYQYvMKICbo0h7cr8tXY5oU0GIzvGivZ7_aMmjHbFH4fZ4GQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المواكب الخدمية لكتائب سيد الشهداء تنتشر في شوارع الجمهورية الإسلامية في إيران لتشارك العزاء قولا وفعلا وعملا كيف لا و هاشم الحاج ابو الاء كان يقود المعركة من الأرض في أيام رمضان مطلقا اطارهم و سياستهم العرجاء ؛</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81241" target="_blank">📅 20:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHCa7UMRG6LOde6RV2gXS5ISAnroPSM7q7O8Z8S9UZiQ6wpFCqJaracg3jcMMFOGQq3eTgQsZo_e9mKsn74F97QH14joKwuGWUVPy4GNrT-sW3kzezjtaFZG0MKag63Og8u1Q6JdgsVc2Jh4cHXcDwRaXXy7ThxS3Kh8Oa_MIES4Fngg1AAYy2bi_yAqR8adBo62od4jhZKOazZkoxLWO8-qTBIqmKcRuxn_m076CWvjuQH2O984g_DBBgxFb0g6zMcAqt4sTU9LpAgi1oyrr-c2qkyZw3umkmgtqLgDeWSgqq1R5HEUg_cFcaPeCdo3NPy-vrI_5HfXidw4s4Js1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا لثارات السيد علي الخامنئي  السلام على الفارس العراقي</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/81240" target="_blank">📅 20:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏الرئاسة الفرنسية: يجب ضبط الحدود اللبنانية السورية لحرمان حزب الله من تدفق أي مواد غير مشروعة</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/81239" target="_blank">📅 20:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/81238" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/81238" target="_blank">📅 20:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">يا
لثارات السيد علي الخامنئي
السلام على الفارس العراقي</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/81237" target="_blank">📅 20:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXSsSrP9PNE8UlyNGWbJ9KF29RjEq7PqsKtTq4qHhJ_6TdKDNpP7_TBozi8-ya_M1EPA-IfSoU--GxOTmVumrUBN3193To06ojPbfZ_YQM4s4IHCYIUDK-NyqseYmQE1rdzN0UKjtExLoRL9jmGPM1epdMObbv7u-iVvBRhcH9Tul6GxLLXrCHe36ce9b-B-y2tU0-awTBsbW-UcU43gtzgyVDNHneotWrExFJbYPvsvQuyx7W1qZQ_bakK1Lr6SaI-HE47DWPfPs1sRGcmxdpRKx-ToJNJNBQGjhMwhu3rXl0GuD7srZWjK2XWEaZUUlDXwjBqPnf9boFLpPayLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
🇷🇺
الجيش الأوكراني يعلن مقتل أربعة من أفراد طاقم طائرة هليكوبتر من طراز Mi-8 بعد تحطم الطائرة أثناء اعتراض طائرات بدون طيار روسية في منطقة بولتافا في 30 يونيو.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81236" target="_blank">📅 19:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📍
النجف الأشرف:
المدينة تستعد لإستقبال سماحة السيد المستطاب ( رض )
#قوموا_لله
🏴
#باید_برخاست</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/81235" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">20260706_211431.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/naya_foriraq/81234" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#بالوثائق_للتأريخ
🇮🇶
🇮🇷
أعضاء مجلس النواب تقدموا بطلب رسمي إلى قائد الثورة الإسلامية السيد مجتبى الخامنئي لإقامة مراسيم تشييع جثمان والده الشهيد السيد علي الخامنئي (رضوان الله عليه) على أرض العراق العظيم؛ وتعاهده على مواصلة السير على نهج الإمام الشهيد والتمسك بالمقاومة.</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/81234" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoDsR2ENY4shWkorg5SsuqY6AyzS6LmV_7DD7uzwQCZScmRy-F-MqMIBL1owDz_WqfSe_QViqYtWknhvWthTEwvaG7AtaUniwgglorTP9FXRe23LFII-HqGJYTRbUSfkRLZLXnCCXF_4r1MGMU532AzwZpxxo3-D-nIooWt3ORBlHf4QCmldfKy0RQmatnojT1JHdNzce83sWulanPrLYVsu99C-vgps7PRlxeK45XC1kSZuY4WV0i6GKI4GAyueQ5uMHTe1jNSzvv3ift9Kq9t01E2bhT7ZWn10AKDpeIQzdUa1wcPOa1_0SeJi1-zm_DzGDCYyc3JbcppqLeCbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسماعيل بقائي: ‏
اليوم، ودّع الإيرانيون في العاصمة الإيرانية قائداً عظيماً، قائداً قلّما شهدنا مثله في عصرنا. وخلال هذا الوداع الفريد، انطلقت الأدعية من الشفاه، وامتدت النظرات إلى الأفق، وكأن التاريخ توقف للحظة ليقلب صفحة أخرى في سجله.
‏لقد رحل شخص مبارك، لكن ما تركه وراءه هو أكثر من مجرد اسم وعصر: إرث من الثقة بالنفس، ورغبة في الكرامة، والاستقلال، والوطنية، ومقاومة عاصفة الأحداث.
‏تحتضن الأرض الأجساد، لكن الأفكار التي تدعو الأمة إلى الثقة بالنفس، وحماية الاستقلال، والمثابرة على طريق المثل العليا لا تتلاشى مع مرور الزمن.
‏إذا غادرت شجرة السرو الحديقة، فإنها تترك وراءها تقليداً بالوقوف شامخة من أجل الشتلات التي تتبعها؛ والبذرة التي تسقط في التربة ستنبت من جديد ببراعم جديدة في ضمير الأحرار، وهذا إرث لن يمحوه غبار السنين.
‏لأن الاستشهاد لا يُنشئ حكومة في العالم.
‏يعرف عشاق أجنحة الدجاج أنهم على حافة الهاوية.
‏على الرغم من أنه ليس من المعتاد حمل شمعة أمام العدو،
‏نحن نبحث عن قائد السيف ذي الدم الحار.
‏صائب</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/81233" target="_blank">📅 19:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏ترامب: مضيق هرمز الشهير، لم يسمع به أحد من قبل، لكنه آلة لجني الأموال الضخمة، سأخبركم بشيء</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/81232" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5df5b7d88.mp4?token=DMGlAzXL7vFtTG_txTnC5OjilhYAtVBU2svCZTIa-4c8UZ4P8bJD98EXPGbgnl5L_q814zX-W0QV7MwK4WMhNPs2Urpv-ikrVwHEFQ9M9sB5ZfVePnysfAp0SMDWbJhhB3kbtDcEUwlEoXsE0Qj8wN1Hx8s2_LeNQ0tzg8Lq5LLZlDmnhgp95OUV61Rd6pdDyt4QTzBVJV-iTkyVTG40KReMY7V4jhMxhUp90cAxw2S8LlCxt1ZQvHruyCW_deS1TXJjYvVy822O-vacRoPOwNvhYMO7ct-S6Aan3uYLZMBNQJh32tNvBxRiSR7WHsFXi9HNG0a9WFCbk3CJ13QlFSL1Lgcz7L_OPjTIMU_yvAOodEvoeDnAPu2jJA6bZAQocqE7f9gWHhWy-nfTrpcD_crRewCdrkHTq7aXqa7pCuRVbO0Y4594cjf_TEjIltXQRNeOcugsbVAMjMAuXVpQyoJdbVP4ZZg7dAOGET_oZsDO5pujcL-JX8xVgEqv0fm9RJObXD9H9tpix9MLbj0-9mLgyN-d16qkUyoZe7xF9OBXcKHx0gGilMx9ymiNPZ1UMGhsGLPkg2rNBwMeWCSZbccOSpsx_940C3mOI-elwMeUeTVVAGcYSFSz475Gzmo_GqtAERV_FvR8prg8bnfSq5jbnQjpX7ewpZYV1FOgCKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5df5b7d88.mp4?token=DMGlAzXL7vFtTG_txTnC5OjilhYAtVBU2svCZTIa-4c8UZ4P8bJD98EXPGbgnl5L_q814zX-W0QV7MwK4WMhNPs2Urpv-ikrVwHEFQ9M9sB5ZfVePnysfAp0SMDWbJhhB3kbtDcEUwlEoXsE0Qj8wN1Hx8s2_LeNQ0tzg8Lq5LLZlDmnhgp95OUV61Rd6pdDyt4QTzBVJV-iTkyVTG40KReMY7V4jhMxhUp90cAxw2S8LlCxt1ZQvHruyCW_deS1TXJjYvVy822O-vacRoPOwNvhYMO7ct-S6Aan3uYLZMBNQJh32tNvBxRiSR7WHsFXi9HNG0a9WFCbk3CJ13QlFSL1Lgcz7L_OPjTIMU_yvAOodEvoeDnAPu2jJA6bZAQocqE7f9gWHhWy-nfTrpcD_crRewCdrkHTq7aXqa7pCuRVbO0Y4594cjf_TEjIltXQRNeOcugsbVAMjMAuXVpQyoJdbVP4ZZg7dAOGET_oZsDO5pujcL-JX8xVgEqv0fm9RJObXD9H9tpix9MLbj0-9mLgyN-d16qkUyoZe7xF9OBXcKHx0gGilMx9ymiNPZ1UMGhsGLPkg2rNBwMeWCSZbccOSpsx_940C3mOI-elwMeUeTVVAGcYSFSz475Gzmo_GqtAERV_FvR8prg8bnfSq5jbnQjpX7ewpZYV1FOgCKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
تطور جديد غير مسبوق تشهده سوريا في ظل حكم نظام الجولاني الإرهابي.. انتشار مرض الإيدز في بنوك الدم السورية بعد تبرع عدد من المواطنين النازحين إلى دمشق من إدلب ودير الزور وغيرها.</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/81231" target="_blank">📅 19:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
محافظة سمنان الإيرانية تعطل الدوام الرسمي يومي الثلاثاء والأربعاء تزامناً مع مراسم توديع واستقبال الشهيد القائد الثوري.
▫️
تعطيل محافظة مازندران يوم الثلاثاء</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/naya_foriraq/81230" target="_blank">📅 19:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8928abb69f.mp4?token=PbI3u1n4bPOIj_S0y9Y8kQtu266Lp6Hg3zZ8ZWHQZAAKmfaDUgsK0EV_TSmsp29HKiKz1A60Mm4A7EaKRT58RcWleDLr9ingrgW4lH10WDfPtkMSuSWBlpv1Rr4ZEvsMnhMjn8cf9L8f6bAt2fNv17M_WaM3Xs6ZiHeXXjN2nafnULUSLqBT2k-xszTdsKTACKE9RKlZgrUEAb5zVGYIne1szTbSSypkmCwXoh9nwC91mcuJh-oNca_ROIZNkTGrqV6IKc2nIFYcsf72__y7rBdb0dq2lg9q6CrK5vGCMI4ICAriBpjIWIomM4PGyrW44rXkrGoqaSUd_xEVNcdPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8928abb69f.mp4?token=PbI3u1n4bPOIj_S0y9Y8kQtu266Lp6Hg3zZ8ZWHQZAAKmfaDUgsK0EV_TSmsp29HKiKz1A60Mm4A7EaKRT58RcWleDLr9ingrgW4lH10WDfPtkMSuSWBlpv1Rr4ZEvsMnhMjn8cf9L8f6bAt2fNv17M_WaM3Xs6ZiHeXXjN2nafnULUSLqBT2k-xszTdsKTACKE9RKlZgrUEAb5zVGYIne1szTbSSypkmCwXoh9nwC91mcuJh-oNca_ROIZNkTGrqV6IKc2nIFYcsf72__y7rBdb0dq2lg9q6CrK5vGCMI4ICAriBpjIWIomM4PGyrW44rXkrGoqaSUd_xEVNcdPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ناقلات جند صهيونية تتوغل في منطقة حوض اليرموك بريف درعا جنوب سوريا بعد سيطرتها على معظم مناطق ريف درعا.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81229" target="_blank">📅 18:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b83f2717.mp4?token=ixcd8jSoKB3rbfkKJ-frzOaHqFd82lH2wCuKH8zh3mQxeE2MT2hlLGb5h37MBt7kK0KzTWh8I6v2RLflza7PJl-XgOcRR8beKX_wUY4rNY77_TmrRbcp4PHtHeLu0ZQM0Rv66nKUb3HwZu4RN8bfUl2bvDqM7bFyqGztXpYneBlTsMlPPH_mXfTSSO74ikn1ENnZQDLJwMck_htZW2TD4uqxxzE7bB8n-Wc7tWDnamLJ-v3Zxr18vhzs0lU7bD3Q_zGg_iK694hrEYduRpxSi1Zbr4Y_IHzOwB2Gk_NpYy8Tdtd0r2HKNIqmQ4mnObm3QJwWJF7Qg2I_i3-4cAr0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b83f2717.mp4?token=ixcd8jSoKB3rbfkKJ-frzOaHqFd82lH2wCuKH8zh3mQxeE2MT2hlLGb5h37MBt7kK0KzTWh8I6v2RLflza7PJl-XgOcRR8beKX_wUY4rNY77_TmrRbcp4PHtHeLu0ZQM0Rv66nKUb3HwZu4RN8bfUl2bvDqM7bFyqGztXpYneBlTsMlPPH_mXfTSSO74ikn1ENnZQDLJwMck_htZW2TD4uqxxzE7bB8n-Wc7tWDnamLJ-v3Zxr18vhzs0lU7bD3Q_zGg_iK694hrEYduRpxSi1Zbr4Y_IHzOwB2Gk_NpYy8Tdtd0r2HKNIqmQ4mnObm3QJwWJF7Qg2I_i3-4cAr0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشادة كلامية داخل البرلمان العراقي ونائب يطالب رئيس البرلمان بالاعتذار بعد وصفه البرلمان بـ"الروضة".</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81228" target="_blank">📅 18:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة:  - سيشارك أكثر من (3000) إعلامي عراقي وعربي وأجنبي في تغطية مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره).  - ستتولى (2500) كاميرا و(23) مركز بث مباشر تغطية مراسم تشييع السيد الشهيد آية الله العظمى…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81227" target="_blank">📅 17:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81226">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: سيشارك (751) موكباً في مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره) في النجف الأشرف وكربلاء المقدسة، والعدد مرشح للزيادة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81226" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81225">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e74d73728.mp4?token=ofY9WKWbvvrUuzB6tZ3y4zhdv9zARIq6ar4MBuZdkMxADr0851PnyhPiwO2U2JRy7ww32rZBasYL21js78H-s-qQfoyV9fMyijrp-DJiR6NualbSuF6q3yM3OnqsvzM9pS1X1gdDait-6NP8xGXredR9GAegtIcTgsDdPGiZJCyrmgbfrh1JwESvYLG9CtwGhNcbe33i_BanZQtk80Bjh-bS9MncO33tLtv4o4NILVguH-Et4RV773frvjwuCr-YFCb4Hpn_W51vLA2n3VaVeWrV0gNXGz3fwpPyshPKE6gXL0hOhPa66Zf-E4xyjUPFw7dJUJM1KS2QW1vf_0Mghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e74d73728.mp4?token=ofY9WKWbvvrUuzB6tZ3y4zhdv9zARIq6ar4MBuZdkMxADr0851PnyhPiwO2U2JRy7ww32rZBasYL21js78H-s-qQfoyV9fMyijrp-DJiR6NualbSuF6q3yM3OnqsvzM9pS1X1gdDait-6NP8xGXredR9GAegtIcTgsDdPGiZJCyrmgbfrh1JwESvYLG9CtwGhNcbe33i_BanZQtk80Bjh-bS9MncO33tLtv4o4NILVguH-Et4RV773frvjwuCr-YFCb4Hpn_W51vLA2n3VaVeWrV0gNXGz3fwpPyshPKE6gXL0hOhPa66Zf-E4xyjUPFw7dJUJM1KS2QW1vf_0Mghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: تحدثت مع إنفانتينو، رئيس الفيفا، بشأن البطاقة الحمراء، من غير العدل أن يقوم الاتحاد الدولي لكرة القدم باستبعاد أحد أفضل لاعبي الولايات المتحدة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81225" target="_blank">📅 17:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81224">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامب بعد هزيمته: أفضل الوصول إلى اتفاق لأنني لا أريد الإضرار بـ91 مليون إنسان  مو جنت تهدد بـ"محو ايران وحضارتها"
😄</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81224" target="_blank">📅 17:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81223">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: يمتد خط سير مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره) في كربلاء المقدسة لمسافة (5.8) كيلومتر.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81223" target="_blank">📅 17:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81222">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: يبلغ طول خط سير تشييع السيد الشهيد الخامنئي في النجف الأشرف 6 كيلومترات</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81222" target="_blank">📅 17:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81221">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: اكثر من 600 اعلامي عربي واجنبي سيشارك تغطية مراسم التشييع</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81221" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: الدرونات ممنوعة وسيتم التشويش عليها</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81220" target="_blank">📅 17:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81219">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: الدرونات ممنوعة وسيتم التشويش عليها</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81219" target="_blank">📅 17:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81218">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامب: أنا لست مهتمًا بتغيير النظام في ايران</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81218" target="_blank">📅 17:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامب: أنا لست مهتمًا بتغيير النظام في ايران</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81217" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81216">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64db71377.mp4?token=F7U7taMNzpNQ7p26fnhOqVfBhOzWvxm_pJhUPG_oQsYA80S_pDOTO29qJ32IQjSy3xliZk75XTHwITUnv_dvodrEgLOHeSfr1NvvZcdULsHsgPo6KJ0pW1hlR7aVxV6YCZm6MCbO68YZhI_P2vJG1UyKE8Xs3t_IFBi6CjCRnm0aTVJV-joAEYGf0I8KIjlIZOCFAxbSpBUmY6Rq1tpigJfHqm1m_o2OZIjEwunux78dNZ8EFo5DY1SWQHYVMUih2BAV9EKCWz5QiuMk8b7u4TZoozk7FrtekDwXyViV51xnmKrQ0ZqFfaZ59VkOIZrvEPDu_-_eq7caID-9IJ79Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64db71377.mp4?token=F7U7taMNzpNQ7p26fnhOqVfBhOzWvxm_pJhUPG_oQsYA80S_pDOTO29qJ32IQjSy3xliZk75XTHwITUnv_dvodrEgLOHeSfr1NvvZcdULsHsgPo6KJ0pW1hlR7aVxV6YCZm6MCbO68YZhI_P2vJG1UyKE8Xs3t_IFBi6CjCRnm0aTVJV-joAEYGf0I8KIjlIZOCFAxbSpBUmY6Rq1tpigJfHqm1m_o2OZIjEwunux78dNZ8EFo5DY1SWQHYVMUih2BAV9EKCWz5QiuMk8b7u4TZoozk7FrtekDwXyViV51xnmKrQ0ZqFfaZ59VkOIZrvEPDu_-_eq7caID-9IJ79Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب:
الرئيس بوتين يريد إنهاء الحرب الآن، نقترب من النهاية أكثر مما يدرك الناس</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81216" target="_blank">📅 17:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81215">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
إضعاف إيران يفتح الباب أمام اتفاقيات سلام جديدة على غرار اتفاقيات أبراهام.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81215" target="_blank">📅 17:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#ترفيهي
🌟
‏ترامب يقول الامريكيين "اخرجوا واشتروا اجهزة ديل" بسبب تبرع شركة ديل بمبالغ لحسابه الخاص.
ابو جنة فرع واشنطن</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81214" target="_blank">📅 17:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81213">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f395cb56.mp4?token=IWd3juHynuIdk6GPTGTT-aTuMmq4XFa9d0R50xwkpz4AiRfVDjPHzafQbhTC2bR4OhVCTl8OMwsCjnfflBCprvrnY6WfAMZxovTsOLuqakb8pX6HL7ZuHt0wduoS2VUIQJQO3zcz6RN-vx-SiyXdWu_Erj2grVtlseL3DmzPKDJ2qtYfHCXU2tfsBpWvrdLtdeorkS8Cipvqlby1m1Cw69GiTMLD5aZgoftESkz9iSpwKkrpHPsH7ZYaxacZPWmScpFIWnQLTeP2d2Q-e-zVlnr0STD3LTkRFrZtQSsmui3zC4KCpOqwsquifO7KSE8mH2n0JsFdLcWHRTmlijdYNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f395cb56.mp4?token=IWd3juHynuIdk6GPTGTT-aTuMmq4XFa9d0R50xwkpz4AiRfVDjPHzafQbhTC2bR4OhVCTl8OMwsCjnfflBCprvrnY6WfAMZxovTsOLuqakb8pX6HL7ZuHt0wduoS2VUIQJQO3zcz6RN-vx-SiyXdWu_Erj2grVtlseL3DmzPKDJ2qtYfHCXU2tfsBpWvrdLtdeorkS8Cipvqlby1m1Cw69GiTMLD5aZgoftESkz9iSpwKkrpHPsH7ZYaxacZPWmScpFIWnQLTeP2d2Q-e-zVlnr0STD3LTkRFrZtQSsmui3zC4KCpOqwsquifO7KSE8mH2n0JsFdLcWHRTmlijdYNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تقوم بقتل شاب عبر بث مباشر بحجة "الغيرة على العرض" ويلاحظ في نهاية الفيديو سبهم للذات الالهية بعد تنفيذهم عملية القتل.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81213" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZzKTE3_aTZz4KT9kis9sRwAbH4KIqz37G2dd4ya4vSWeJCRiRG0i7P0dlKZytcUqJnfxHOxHkMTxJAgvLKj3OTjwVIzw-sExYzX2SeiNPNvBlPwZeERkb-h27eHQv3ZOHvgGNaw1ilfrNpFLb1cRdutPk2zauf2LX2x3eh-m8X86ye1ANzbye1JzUrmQZYengfNqZOWKat59cndILauV4xqWaPlOET0SkeS000ZgZk1oI4f3RsBzhXkfy-eX7ot5_9-QFVLIUUdQJQgVrZyjGm_QrDuAKdwUFFXescVfdg6zj0Lj9ua1SF9wS03DSZqsO_1Z0vEN1hepia7BEAn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البيت الابيض يقر ان الغاء البطاقة الحمراء من اللاعب الامريكي جاءت بسبب ضغوط من ترامب على الفيفا !
لا يابة السياسة مالها علاقة بالرياضة</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81212" target="_blank">📅 16:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81211">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">محافظة ديالى توجه بتعطيل الدوام الرسمي ليومي الأربعاء والخميس المقبلين للمشاركة في تشييع جثمان قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81211" target="_blank">📅 16:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سماع دوي انفجارات في أمستردام</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81210" target="_blank">📅 16:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfqs1UCGZ6VvVhuGUx7ga8TfzxXUQy5dlgzE8rGZKI3rwH6j4lPoOFzZbUsfnp-VNOyWn7b9md6dykuMoRmhGqg_a54mgp-vghGKy-YUJgNd3NEv0RjOxzvMIPYadeCdwug1k1llAaTNO2rB_QTQ9rmrNIIIbnXvtASgcy0mj8Fsg2OvEqXzoORDo7XK6e-NFgkIDpju1guLYcdlKiKdKolJwvTcsdClHZDmza2bbu8C3JeDtcJbjrLB3Ki7Dy9TjxUmefgvTCnt5skMBZ90mnh5yEHuptRkMC1fCpKJ42xoXUFOjNufuPi-nPC17RSNIg0nDW86Rri7w7Y5Vp9YAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرضت مجموعة الضربات الحاملة البريطانية مرارًا وتكرارًا لتحليقات طائرة الدورية على البحر الروسية Tu-142M3 أثناء عملياتها في بحر النرويج كجزء من عملية FIRECREST
✈️
.
تم إطلاق طائرتي مقاتلتين من طراز F-35B من حاملة الطائرات R09 Prince of Wales لاعتراض الطائرة الروسية ومرافقتها حتى مغادرتها للمنطقة . ووفقًا لوزارة الدفاع البريطانية، كانت الطائرة تحلق على مسافة قريبة جدًا من الحاملة، وألقت عددًا من العوامات الصوتية في المنطقة ولم تستجب للإشارات الأمنية الدولية
📡
⚠️
.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81208" target="_blank">📅 15:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اجتماع أمني وخدمي رفيع المستوى في النجف الاشرف لوضع اللمسات الأخيرة على ترتيبات تشييع جثمان الشهيد الخامنئي
بتوجيه من السيد نائب قائد العمليات المشتركة الفريق أول الركن الدكتور قيس المحمداوي عقد في محافظة النجف الأشرف اجتماع مشترك ضم رئيس خلية الإعلام الأمني الفريق الدكتور سعد معن وقائد شرطة محافظة النجف الأشرف ومدير عام الإعلام في هيئة الحشد الشعبي ومدير قسم شؤون عشائر النجف ومدير قسم الشعائر والزيارات المليونية في ديوان محافظة النجف لبحث آخر الاستعدادات والترتيبات الخاصة بمراسم تشييع السيد المرشد الأعلى السابق في الجمهورية الإسلامية الإيرانية اية الله العظمى الشهيد علي الحسيني الخامنئي ( قدس الله نفسه)
وناقش المجتمعون الجوانب الأمنية والإعلامية والتنظيمية وآليات التنسيق بين الجهات المعنية بما يضمن انسيابية مراسم التشييع وإظهارها بصورة تليق بمكانة الحدث وبما يعكس الصورة الحضارية للعراق وأهله
وأكد المجتمعون ضرورة الالتزام بالتوجيهات الصادرة والتي شددت على أن تكون جميع المظاهر والسلوكيات معبرة عن القيم الإنسانية والوطنية وأن يتم التعبير عن مشاعر الحزن والوفاء بأساليب حضارية وسلمية تليق بالعراق وفقيد الأمة الإسلامية
كما جرى التأكيد على منع حمل السلاح بمختلف أنواعه خلال مراسم التشييع وعدم استغلال المناسبة لأي أغراض والابتعاد عن الشعارات أو المظاهر التي قد تخرج المناسبة عن أهدافها الإنسانية والدينية مع الالتزام الكامل بالقوانين والتعليمات النافذة.
وشدد الاجتماع على أهمية تكامل الأدوار بين الأجهزة الأمنية والدوائر الخدمية والإعلامية والعشائرية بما يسهم في توفير الأجواء المناسبة لإنجاح مراسم التشييع والحفاظ على الأمن والنظام العام وإظهار الصورة المشرقة للعراق في إدارة المناسبات الكبرى بروح المسؤولية والانضباط.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81207" target="_blank">📅 15:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx2Kg5CxJuaOZzEG9l2znVg2-s9C_o09KjTZ4I9k_NCk5dz5jit15OYDb7jLC3tk5TbVvc6qpd_db72yvd4A_kSkLnuHWFWDxJ_8UXekS24zKxsXOsa0DZtpctIuHUPR_yMzyrbr70CsSDnp4e1IHWxwXi_7feRZ-_ck9Fth4CArTvPiLIM1mQVSAbg8LN3zs762CJ4Imlrp69YzNL6xTy6AL3vvDR6E-Vwn925Arlybag2T9Zr8xBNAVPD5_etXknp360AUjQ5XrDeYn_SR4I9PN4MUpCeRa68RTQb7R3numOORMYm2fvDoq_3pzTTRlu9emv1k1UTHzsXYKJJc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزارة الداخلية العراقية:
وكالة الاستخبارات والتحقيقات الاتحادية في محافظة صلاح الدين تطيح بأحد المتهمين بشبكة الفساد التابعة للمتهم (عدنان الجميلي) كما تضبط أكثر من ثلاثة ملايين دولار امريكي وأكثر من سبعمائة وخمسون مليون دينار عراقي، كما ضبطت مجموعة من الأسلحة الخفيفة والعجلات الحديثة وعقود حكومية داخل داره</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81206" target="_blank">📅 15:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🌟
‏
الرئيس اللبناني:
بقاء الاحتلال الإسرائيلي يقوّض شرعية الدولة اللبنانية، على الإدارة الأميركية الضغط من أجل تحقيق الانسحاب الإسرائيلي.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81205" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇷🇺
مصادر روسية:
اغلب الهجمات التي تعرضت لها روسيا مؤخرا بتخطيط وتنفيذ وتسليح مباشر من بريطانيا بالتعاون مع النظام في كييف</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81204" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAPVQaxsGgy13hYCQP3YCySw3vKaxXiXOtq7fNPjfZCEPVuR0V-OyDQx3tUBrt7UO4Hq7ju0_onHVIRrtpnQYKiWwLbBU6yq_ynp_SC17cT2w5rrn7BFheZyXbvefN5j-BHvPVCFM9qF86D5BQP8K2Fy93N8m-cjcS5P2DIjji8ORMiNPRs-nYDpyw-1hRLj0dyrM5kk68RWd_4_xAQQoBST8884CJrgB4p71M8-NRh3wk5gbVPt7lYq6dkqllJ7cKvtCkPsmEO3m0fkgZsfEvnnEsd0ClrL9gH94_qWzm-PqrpNHP9yzZWxqPrrgGsrs_09opM3C40SzS1cjAlhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-0VErx4wCoVKN0e7igxh5zfGRcDNDD40YdnrroBd95gcj6YA3NJdFGEvIkP3etj5vSV3z8SuAuzHaKQkIdrD0VC-6xJ5shfQuIUXfxo1_Og0P-vmtCUPp43CO4rBkzBy4Ne_3gOOOL043giGDqIMXFMlminSTKiry_OhcbHtj01vDi1lffwua7fH56pkSl9fcizYrTkZohCqF7dTw3t5xFJWMJWpYz2Au2FeZ1cYRUPO6Ni6i3M3yCOF2bi3eLxeq8EyofigUC-KpUCdxVLlHXdmSTKD3QggxAbLD1sm9HoLtNwlOsgS8WeHw-EDaYAOxlHxs7-6nupZTyzztrabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9ntxhEFmjr67x4LFzVl06vA4FzXzpxlOHokPj87EZ-r3Oymv3xpnBrqtOSS_ToC3zCfF93aOeoiE7ReoCEjV_l3L7TYbfc310PwVi5bJ77aOBHWQiv2OJHj3Me6Qi2Ixeasrod6eVfBpPN949lgiN1LdS0VkArO_uRoIzsPu3XK5KOVqUwXL0ctQkc47tCh8ImvE4N3mUIDmBftz2QklCFafGAgPdcyP0FMzx4WqoT10xGHHSC2-LKmLNFJ49kd6o507OpELZ5vUJApU82mMmhiKSzXCi2MvpaWhTVMPYIxqwdUD2wjAhxDJxq641GujkIH0WkkPe4YHRuu6MY3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYxMykL03j4UmJehnAzNLlrn2kYZx1E_oXidBVmvOVIpdIrK96UOBuwVyOfnXZUpIdJl9K6S9wZYsb0_8EuIjVft6n0dZ3UhV2aIfmNpf5iAcoTVjvS8IS6qUiGOfd0IWPkv8CInatSCcG4xImIOGrFrnGol7140EUDLIFIfh04hr75giCgyN2z6MDVnVZaqEJzMivCDfC3LSwvypH_rp6DIiLqgsQdUkRmyp7EpPMq9PYVBawsIobQt6ckdjmQ0iur1MhfKVG94VFCKKS3O53dJFYDOzklFYfE_2HqgpCSxBZuMWZ6xR9x1Zp_JTlxScKNcn2noo_SG3P1PXbQ_0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جثمان قائد الثورة الشهيد يواصل طوافه في شوارع العاصمة طهران وسط الحشود المليونية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81200" target="_blank">📅 15:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني: سيشارك الرئيس الإيراني بزشکیان، ورئيس البرلمان قالیباف، وأحد أبناء قائد الثورة الشهيد في مراسم تشييع جثمان الإمام الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81199" target="_blank">📅 15:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d673daa6.mp4?token=Lyhy9ZfD5GqWUFymsKz4FbUFsQMi-54KIOjy5ipOhW2JiREbK7O_nIbjO6Mz4-aKn4mUL6aMHEzwh-0DuRWh3aliXo4D6BAF1dCYkv6LeqLT-1huf1A_R8ga7op2BKUaJNrLrD1LEVCvfHW5iZt0GWwj3s-tB0fH73EIlDFrNbgp5NEno9m9ABLMgwsgqbLEaC0Ux2IFCt1QBKqbcTEZdiD8HuIKe_iqA3wU-TbUNq_0Qr3X1VZ6FzlNNj3CZUVvRndKWupDJXsSYiazt1I9ld8XpudkLF8vXO5xoQpPUKDqYMw0qXbKWVOcuJKKtszVjj_EXuyRFfD8WmcT5fdMqZK7fWk1V-3Vd66KQgUqygmGuRydoPwXbyF0eacJc-azD-MqfBzKGVEI7LyFqfuqet0aV7-9BvQlYIej1aHas9oEF3m3RxoeXxyIBwUKX4GIyN9kqfop8h-1NPYoabf7eP40kvvvjdHmAKjdahaI--0ZodddIDEHdvJJ88X5FZ5FVYLVpR0jcPQQv-x9kwaeoRuAMQWos0JSBLS3HGd9yLE9LNsZgFg59vFwLcHBKsCB-bS3dWoTdRSExOnrgvH-YpTCjxALk9gd09Bu7fmThVxl3LnURkSuWYIZp-NOqYyVgeC7RaNo-oS-MAM8G35wV3hhKmXEqsgUOHNProBowfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d673daa6.mp4?token=Lyhy9ZfD5GqWUFymsKz4FbUFsQMi-54KIOjy5ipOhW2JiREbK7O_nIbjO6Mz4-aKn4mUL6aMHEzwh-0DuRWh3aliXo4D6BAF1dCYkv6LeqLT-1huf1A_R8ga7op2BKUaJNrLrD1LEVCvfHW5iZt0GWwj3s-tB0fH73EIlDFrNbgp5NEno9m9ABLMgwsgqbLEaC0Ux2IFCt1QBKqbcTEZdiD8HuIKe_iqA3wU-TbUNq_0Qr3X1VZ6FzlNNj3CZUVvRndKWupDJXsSYiazt1I9ld8XpudkLF8vXO5xoQpPUKDqYMw0qXbKWVOcuJKKtszVjj_EXuyRFfD8WmcT5fdMqZK7fWk1V-3Vd66KQgUqygmGuRydoPwXbyF0eacJc-azD-MqfBzKGVEI7LyFqfuqet0aV7-9BvQlYIej1aHas9oEF3m3RxoeXxyIBwUKX4GIyN9kqfop8h-1NPYoabf7eP40kvvvjdHmAKjdahaI--0ZodddIDEHdvJJ88X5FZ5FVYLVpR0jcPQQv-x9kwaeoRuAMQWos0JSBLS3HGd9yLE9LNsZgFg59vFwLcHBKsCB-bS3dWoTdRSExOnrgvH-YpTCjxALk9gd09Bu7fmThVxl3LnURkSuWYIZp-NOqYyVgeC7RaNo-oS-MAM8G35wV3hhKmXEqsgUOHNProBowfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والقلوب تستحضر ما تركه من أثر
#قوموا_لله
🏴
#باید_برخاست</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81198" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q76X7IH6D3nzsW9hoQYv6AUWEJq65bBLuHHppIr-JHtufHcimB6B-nNIyRIAnpIZsEsGLf0sd3xS_iN3PsfA2nm4HDDyxK6MKKYH_oyKea6zeQOAZFNOD_59ssgAMq0K7-sBEoW1D3TTN0Ydsoce6y8sX9OiPHhl_p2QNxhnJx26hJHRLhyEH9SxipixMMucJwwn6E7HLw1_TWWkHczQ7ECy1PXsjqJ41KtUJS5ueQVZtDKpnfaajaJxed_JOqEw6GMSbouKhZ2TQzNDvb8jMWD_shMC5Et6GYp44dn91Mmhy_DcWZ4R1MpkKaT59CPkC0mfjtmXG6DCQ8LfywLVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المديرية العامة لتربية محافظة النجف الاشرف توجه ادارات المدارس في المحافظة كافة للمشاركة في تشييع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81197" target="_blank">📅 14:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇧🇬
عشرات المؤسسات الحكومية في بلغاريا تتلقى بلاغات عن تهديدات بوجود قنابل</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81196" target="_blank">📅 14:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الاتحاد الاوروبي يهاجم ترامب:
القرارات بشأن ‏القواعد الرياضية والشؤون الرياضية هي ملك ‏للهيئات الرياضية وليس السياسيون!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81195" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URx41Uy2erCMeQNt0cMlnXWx4rvjbM5pOSCX875yb3vBC_IOg7vDktkQn9nSaQYVVFeA7UFlUxAfn8tgJ4Il45QkJfs3R9ls-KzomEjljR0pOPvvu4Rbqhzy1L-8oL2JqPNS_L2GrDz-X1IfQ0rq4zu5-l_hrEKEBXBiA5olKG5JggMCYHE_cFe94s1i57HG70ZHiapyoOW9-6GkHSqokW33kraI5FWpwoPM6_9eun0cZePUi0IIbHjwKH2A68y56L_vFgIp-zWSP_xQ6LkhNcj994Muo4V7qPavOros_d1SDORTo9AMe-OSnYebOfO_QLaAk05mnor88NFUhSFJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMaTVEZLbtvf0iKMMwwW0Z5M6luw1wBdD-9TMk0L-LrNc_441HkX1t5PZJEWonC95EFu8uHyfX2SGXbWwENmv1fpD046ZwcQ7o8vJBL8PPPfCui95kJu1h8h6Azuu3jNu9Pqnz5dsv17JYcZV-DQnFOFjDMPSQPL33hjIwndMgY1VjymTcC5qiSPRLvA0V9myx-Q-q7IWgJPaJVDsxxDMS6dzwp2uVOoChXkCY2_5vcb3lAQ7nckYhcUuWsiS2pR6P8U4kF9rAetJsNZSRaulDWs6gGE2k4u4hjOVuv6zMOy1t-6l_0QYw6g1JPhXvGMoxZ0KvoPUBWI1I6Leeiuig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقجي يشارك في مراسم التشييع</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81193" target="_blank">📅 13:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fabc1873.mp4?token=pems3IduSGv4Zj46F-5iXBk5QF8P45uQ7tl5Zh8rbWR9JnLarUmWkrkv3QQTFG4lWBUi9ew-aQ2LAdx3g_Wmrg0hYwT4N0jHkh6sydXETH0384x__GrElw6hdpiYTvUqCS848CDlv40jx1EQKYz0G1b18xc5UT0qAtqWZoGmgmeTGV1PtwC-oxulUk42rAoQHl5wh9VVemVbTwadA--U90jpwzQPQOsTaOQ9VJcQ0xqrspY9r7Ox3j8zwl2WF2dFc-f6fHtxZ4WmM_dVaOtAhWNvcUThmLl0rsQOTeQnVCePvOpaAvp8i0VfUsgyPCLDH4Fpv1sam2RjDkPALhlR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fabc1873.mp4?token=pems3IduSGv4Zj46F-5iXBk5QF8P45uQ7tl5Zh8rbWR9JnLarUmWkrkv3QQTFG4lWBUi9ew-aQ2LAdx3g_Wmrg0hYwT4N0jHkh6sydXETH0384x__GrElw6hdpiYTvUqCS848CDlv40jx1EQKYz0G1b18xc5UT0qAtqWZoGmgmeTGV1PtwC-oxulUk42rAoQHl5wh9VVemVbTwadA--U90jpwzQPQOsTaOQ9VJcQ0xqrspY9r7Ox3j8zwl2WF2dFc-f6fHtxZ4WmM_dVaOtAhWNvcUThmLl0rsQOTeQnVCePvOpaAvp8i0VfUsgyPCLDH4Fpv1sam2RjDkPALhlR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
المشيعون في طهران يرفعون صور مجموعة من مجرمي جزيرة أبستين ويتوعدونهم بالثأر القريب.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81192" target="_blank">📅 13:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81188">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_eNRDm6RWUCuOV9wY5zXb8gsr4xV9x8dDv1jkAZGB0it-AKy0ZQjn91kKBW_Dx4dSZB8VhTNl2DWGqNe6plgUqurcmOsCBi3yF-Yi27InyKbbcD3pRVQsKFiT4beFlYeJJ5BXJG7mdZqs-U_QNgxjBQ-SFgcI7IHeINq7_O1opBnupGZv7vQTMSmimjFFnZxR4R7YhXeHHFwo8d2LPGtYh6erK0CAdqZGcKIE7hMwMHm2NvRmCxcHHTpcExz5Oszv2Ak8hVDauCFtE9O5pRSNYtIwEnM0863yePzLWSjItdrHw2VKDSQWvA7aWVHkV_6dHse8N1qqx9mzndHLfbYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0zxqT-WsurUs_xiboXTAWmquvxNVMxoAMbH4S6LRfC7wH47Ca2kA1up4Tvgy86tw1c0gBQtKlk5GuJSD8TpY4QeHGaxfOS4hiwyZxS9HxS6V3YFJcgWtOg_OX9PBkx5z9K1wya5zw7rOng3gV1gmxxoDPygzjI90o5MRc75eM2IZjS50M4Awi81jCA1gvptP61RbTjILU9QNhnKeFfq6YjJAkP96TdbB0DphRMofJFJ2AmjHMDlf6GZlV8YPsr6feN5UERThqWXF5DQDMiTiKi6lA4zMjeG8jOqb75ky9G81m7XRo7BI_0S4S33ofb1cZ2b2gSyKkU7jAtMn8p7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsabYHxEiFj6NqFYq9JA6qg0cInsZJT1iNC9g5bjCTKenPHtJpnztbivSE6KpKwBzrAe8I_aX-MwVkiAbiR5f1HPqj8ewQx3x7MABNk1Brnc3tYoVI3nV74G7SMBbr9yRciT5y4qWE8Vu5oy4LCbM-R6FpYj7JwtwAiudug6fHVSyXxg_wNmj9RLsrDrFjnhhel89k9ZV3P4GInC9nLrDE62RH6HKvAltKTgw5RqK9NGvBjed57ssvCajpzHaqASmDc9wAbsV8pVdhLUF8GAedxNCsKA1t0dCN0jM8ll9Xa4qdhHaKTpU208cZWaxx5efX6oLJzrNFo6nKZBwIi6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXrg9gj5CkVZg3e5VBi-B4xi8XHJKXyBw9kkW8Jd5JH8E5RmFwgbc93dTuLQm08v58ZUJmo8VR3zMIVQTAomDR-Lv7j6dJJM7ptZ7nAPs4X987oH_0Smqk8NfdNeV78ltNQFqfxVkQ8_unjbC24OsNUxefGiFOuf62yu_72VwRAkhMy_FvzlGt5Zh6eU9X6oS9LOnfDlLiII4rsyDKQ8svDGkJORVjyA5sczkR51IcizrhvKWYV6h95-QIuqE6pUXl07d--VtNqQ4QruG1YHG2Oqcm_eipwV7FLuy9eBUFY5bjnLjHtxhDL5GafgcPCLR6LVtab_UAQdKcyQ2IdB7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇹🇷
مشيعون من تركيا يشاركون في مراسيم تشييع إمام الأمة الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81188" target="_blank">📅 13:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81187">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
🇹🇷
مشيعون من تركيا يشاركون في مراسيم تشييع إمام الأمة الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81187" target="_blank">📅 12:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81186">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZjYO92ximu3mHEXV9y8Sc69pF1UTC3eLfFdPmnuaJlKp8BMV5jqDQ_tL7XYRqJ-k6Cf1LBJptEmevUTn6tSg0s3uS7oGRg7Ufs-DQLrxX2NST9sQgtB-X_NIkYprCiQDv8ZNj8wpoLKrw1t4JzyGpDE1v--wSXFXDfqZm1ZWfa1rovneqAJqdfiz7kQ6zI92CuP8OTgj6wc07xL-chhCCQHdk7pb96_volsibReAkW8Pqhlc8nQeTiQk-w-TTE_Eo97BLqQ6LpVvveAdAYOmR8GHCkQfcRQDp06vPStVOmK8FIrQCSDKBkYQkx37x9_kxqvOCqz23K8UafNjWq3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
غارات صهيونية على النبطية الفوقا بجنوب لبنان؛ ارتقاء 3 شهداء كحصيلة أولية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81186" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81185">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني:
سيشارك الرئيس الإيراني بزشکیان، ورئيس البرلمان قالیباف، وأحد أبناء قائد الثورة الشهيد في مراسم تشييع جثمان الإمام الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81185" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81184">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoR2BY4K7UqzxAmtRgW-pSGJkg2RnJlaMRTqka5xP_JsaMc4a92lExwvEX58gKv5wXxjsqroiXWHgB0jnKMNIEgIz1_6wq425Bgp3eaGsX8UBdOwlQNOIY1TQL4zO45i26lBJkY3NHA74k4AmsEo893fLoVVTZTCvi9Lim9hvpR7GWUNI_eqtU5_RU0kyOhnHuzypGrDzx8KyWZcF7Covf4j7gNpPomA8QYGMeSw33JtmIcQzNuMyFKGoarV0Hs76YMTmw6lh-adsF1s7JC-bSpSwjOzaaQI6VgWN8WIpP2LquWBFzZT78yFpvsEjm-w-gXXP61691rYGBWy8MQQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
المشيعون في طهران يرفعون صور مجموعة من مجرمي جزيرة أبستين ويتوعدونهم بالثأر القريب.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81184" target="_blank">📅 12:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81180">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4kfEsSap2da1_7qDS-CckKWuvUcF4J7IZy_zcFmtM8txhiZ0OFxpuZsO7MdmnpOwG1BSMVw0A7twd6GBuStiTklyAOsx95LMpH0DtOxMv2Svb_PT8iicZSwJfjGs00uYo5qDxaB3bMvTqW3aN3McQTzmico0hMX3EoJC5jih3Dx9JAC9ddjhl364gV-EfLJ8MhpD9TEE8-AjMy64v3agnx1CwYClmjk1MIotrnwnnE7DZHOiw0tGoNAcPQcyPyFkli5uhcUedBeYznYOHbpWPMbu74guiBhbs7gyGcVNp6iG3Xk1zQlOR4Bc9cQyXyGnyDXL9g3p1eaa5O44dXpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4jTLrToZyE76wCTtK5sG4CEepI7jH8PG7VdblqUfEyeZuoAYi9Puxo_ZmcrE3_QcXp1afFi8AISvpbMZ2Oawo96oirpE_7l5DxznOxg212QcghTPykFz9wtmyt7evz7dJtbMZA3Bra6lRgDr8t3cRFxJtyf_lRQzcP-ooEItn7dD98jtbMXbi9krUHfEx9lgUZohWw_0C9PBL1aKaLPB4d9_if742VFBF1pLwbQrLnHxd-JdOQPUqRgIf2FKrlDW-q3lCOGnyCsc9QOpPSpQhbSCe6APRED4rSaBl_tCA3OeUZskaj1_merYl18mtcfqZQ_tDixCWryX2Ji9R7sSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYzGzrjJPu-SwFYdpiY4NjEPcUvJ3xImMGwaSMDGhsdS-lU4HmWWKT9sVPDqPuLT5XEsNep8H5tT5PwrpJtWjc3pKkn2qNDSV7fdEl0lXJyq2AqOD7J_7K23D3vAai8i69R4xjOpsS7YWBDVrCPguW6jJGW1y-BWfcDDTXyFQfnnqn1C-7KxlW06MrHMzZvC4XEwMKLkx5tzBlRKYvWqsCABS0h5mWoAIGGIrZwVoBYtY_APZacliFRUFSP3C0n9Omf9P8gA4jI4CRqQ07x1wjhihR7uyjedElHc0ZJC5rnIlcFDYFAYaWTuTxu_ooDsqbKQ-7doGlfegDFjd2adSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nki4wORUUj2wBvGsLcVu2Mby4yeXrvf0J4ImBjpLKHecbu2BiSIukGkhkR7crWnEXI_45J5VnoNMkqCnhIW7pr31bnPRun7_B3g7oF_haTygUADbJTBdNJQu5PHlwTfuvQs6eg1wcD8S1Z8lRwWXWKlR1wBfU_yuBOyP6zU_tO92oagF3vDj8GAQY8fu9wLH0Xs4PH0TDBuAfEFaGbiti3U-yjpjSyA5JHKw54XGgLrjvmBVojhiIkTDwa4URsxEQ2JlfHYM3TLVNRrXRGACh7hEGyl6Pu9lZVw5DWyuc_WFEDtuL5RX3tQsxMEE7zKq8M0T9T8CtsNv1EnVSxDbog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بلند شو عملدار.. علم رو بلند کن بازم پرچم این حرم رو بلند کن.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81180" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81179">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19d2d9f50.mp4?token=D9leXEsnKm3_4bSzEZ8hMMCmLac_bbXwULVkmzA9v1FVhjJwtR-qYtcKqHfElRmpDcTwPeQ5HNkE_rP7yHFyQN8dPjlJS9DmGL77aCOfQr1A9l-j8AwHpFUgduhcLuchHfYshRKQxpqRwHg7eKCVmK5SZsYQ21jen1RStzRGETX1eG8Qa9PGXd1RA0surjvUYTenuQtETAb1p36BfchkrHDsqsqLaIUvGR_HR_m3zslyVwpDWWwX4CESMrrRqOsB76g1ZUKeo0W1pRu2qVYdUqD5D6CO5nJVDVLy3X9wLcl7OEfH4hgg8I2-TDQzm7pustkfk0N89wz_I4_5rpRKPX_UBCz2UakreAvfroKifCdFZnywiLXLd_pARFZALzUCRnkDFHBC5zHmRB12-3GuE5TcaT0MFFPW1soV0dJdvwixeQtPm82amSXA9n58YDSGyrc6-nr6luf0oOmDVN8K6rBeWHR_iHlTfulhWmlmYt2QTD1wp8euOJYpAnvUG19VeWbUZ4ic6BpHD26MnsC6_tIv4kBTGdspLzpU8vRlsp8S_xn4uIidwVjicsbta545uM-g414GynUZaqTbv_QxbVLFp0MiJRqEorv1DQ2VcFNdhTTSwXhNZ1UVlDhQ964xbmycbaihTxSqZEAzM3INZC6yjEbXkEgYE_aqlskgzRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19d2d9f50.mp4?token=D9leXEsnKm3_4bSzEZ8hMMCmLac_bbXwULVkmzA9v1FVhjJwtR-qYtcKqHfElRmpDcTwPeQ5HNkE_rP7yHFyQN8dPjlJS9DmGL77aCOfQr1A9l-j8AwHpFUgduhcLuchHfYshRKQxpqRwHg7eKCVmK5SZsYQ21jen1RStzRGETX1eG8Qa9PGXd1RA0surjvUYTenuQtETAb1p36BfchkrHDsqsqLaIUvGR_HR_m3zslyVwpDWWwX4CESMrrRqOsB76g1ZUKeo0W1pRu2qVYdUqD5D6CO5nJVDVLy3X9wLcl7OEfH4hgg8I2-TDQzm7pustkfk0N89wz_I4_5rpRKPX_UBCz2UakreAvfroKifCdFZnywiLXLd_pARFZALzUCRnkDFHBC5zHmRB12-3GuE5TcaT0MFFPW1soV0dJdvwixeQtPm82amSXA9n58YDSGyrc6-nr6luf0oOmDVN8K6rBeWHR_iHlTfulhWmlmYt2QTD1wp8euOJYpAnvUG19VeWbUZ4ic6BpHD26MnsC6_tIv4kBTGdspLzpU8vRlsp8S_xn4uIidwVjicsbta545uM-g414GynUZaqTbv_QxbVLFp0MiJRqEorv1DQ2VcFNdhTTSwXhNZ1UVlDhQ964xbmycbaihTxSqZEAzM3INZC6yjEbXkEgYE_aqlskgzRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بلند شو عملدار..
علم رو بلند کن بازم پرچم این حرم رو بلند کن.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81179" target="_blank">📅 12:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81178">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ba224243.mp4?token=f8I86HXaRVRulLsu-Ca3tICah-6l3FgFnhD4iWIgx9v5zjY3hVbbUPDZk6DLyO1Y9S6ZlY1-6fIjzJEsbRQTrCV7tcg7ydP9jPg0sVnjm68uBFkwUhFVoxEGYv8O8Ezkv-CQGi5KrAORWxOJ8L_9LjI00K_Ce9wfIeF-Sn59eftEMZImRbM5riTOCLU8I0myCctjJ0io_bcyBpr97CyfvgLhGWKzB-D2S7Gyt5-LQrGzgib6tRsY4tBVlS19vABDshQWAlInXr3uzuGWYWL6C1jpBXrsvdBtqYEQccWmnDUb9EI2e2R8az-GLQJlFKNNe8tzmtIlWK2i49QDXhlaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ba224243.mp4?token=f8I86HXaRVRulLsu-Ca3tICah-6l3FgFnhD4iWIgx9v5zjY3hVbbUPDZk6DLyO1Y9S6ZlY1-6fIjzJEsbRQTrCV7tcg7ydP9jPg0sVnjm68uBFkwUhFVoxEGYv8O8Ezkv-CQGi5KrAORWxOJ8L_9LjI00K_Ce9wfIeF-Sn59eftEMZImRbM5riTOCLU8I0myCctjJ0io_bcyBpr97CyfvgLhGWKzB-D2S7Gyt5-LQrGzgib6tRsY4tBVlS19vABDshQWAlInXr3uzuGWYWL6C1jpBXrsvdBtqYEQccWmnDUb9EI2e2R8az-GLQJlFKNNe8tzmtIlWK2i49QDXhlaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعب عشق قائده وإمامه..
سيدة إيرانية كبيرة بالسن تسير زحفاً لتشارك في تشييع الإمام الشهيد.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81178" target="_blank">📅 12:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81177">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3013d59c.mp4?token=V29E072lBZ4CWe2RxEIg1AQGoQYoO9Q8WDTNaKyA6zqavRmFRJWddkvY2zxmf1rgC2UPRryXbpTDc454DCxC5MQyr1422ZOSKVMJj8o3UIKi5cofQCwSoXu-IxdvGfO8co5qkSOiw2F9Ud7MA4pRjFqmzpvQBUBg2OVW4aWDF2hK_cL2o-VFmH62UOkUpdJYrffPTz-elMdNZt4p0Vg9mSunIpvhlQrMts2p837gbCW3lLInfTyytpEEPfJFtYneDXx5_mSJ3Pqc-UlV5BcIUshrEIFmhJKVAF3bk-wveRFsti5FsDcHOiHtiW96qmLdkLJoPcB3Co0mvAs3nbR9gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3013d59c.mp4?token=V29E072lBZ4CWe2RxEIg1AQGoQYoO9Q8WDTNaKyA6zqavRmFRJWddkvY2zxmf1rgC2UPRryXbpTDc454DCxC5MQyr1422ZOSKVMJj8o3UIKi5cofQCwSoXu-IxdvGfO8co5qkSOiw2F9Ud7MA4pRjFqmzpvQBUBg2OVW4aWDF2hK_cL2o-VFmH62UOkUpdJYrffPTz-elMdNZt4p0Vg9mSunIpvhlQrMts2p837gbCW3lLInfTyytpEEPfJFtYneDXx5_mSJ3Pqc-UlV5BcIUshrEIFmhJKVAF3bk-wveRFsti5FsDcHOiHtiW96qmLdkLJoPcB3Co0mvAs3nbR9gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية تظهر كثافة الحشود المشاركة في تشييع قائد الثورة الإسلامية الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/naya_foriraq/81177" target="_blank">📅 12:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff45c8712.mp4?token=mlamghjfbDDMz5nAJqTk-0oBdl9AN9V8WuNSN3j7ugt3kPWBW8ZxHD4P8uwi_lo5Q2MqPuIdV-YGAYzDuiz0iplNXc2nPTF5sskPojFPYgULNAzS0aW9EgCb_QLKm5y24k9vOaca4p9TS73m-pu4A14F-l9qxANUrKiTpgACZZ2DJIWfY3EjryoMQWiyubP05uDxmow5EmbS_NFbbpncfDAGBBIt-pklVGK6r8dgNuWpT6vrgMJTXJx3SYuQaCjfbICuAXSTMNgyMxODWZ9d28LM48jQt_qPwZPA6KwLasuiiXEBv1Egmr-JijbfN3ga1ZrxIQ6UuyKTxNOU8HLqlUJi8Uh7eqNOeApCl44XsZgKEoDZ5f10ySnMF8BTkjUz7qyewKqBGTrsFoPbr0mHuYQfM87dQZ7baNzkXBqHfd1vEEm56nMLW5o5vbI9IaVxieE8o5nRnSsPbRhJts92vGYTXl1W7Car-OSNSgh7RMem6CtwL6u5k2FK4DEmRYkCGUMXXmKMpPJu17YrxgoE9zh3iA77HYqgqw_MGPGc2h9GVlzuo13eS2ZO25GeS0XgyjK7ifVnWIoeF02qlSO1hcmQvG9Ty5HkzzG7h2pyIDr6wN__SSij-EvJUG4hQ7y8L5OpxB1keVMsy95IaMFvQe4XAunhe4aA5m4Mqa_hBRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff45c8712.mp4?token=mlamghjfbDDMz5nAJqTk-0oBdl9AN9V8WuNSN3j7ugt3kPWBW8ZxHD4P8uwi_lo5Q2MqPuIdV-YGAYzDuiz0iplNXc2nPTF5sskPojFPYgULNAzS0aW9EgCb_QLKm5y24k9vOaca4p9TS73m-pu4A14F-l9qxANUrKiTpgACZZ2DJIWfY3EjryoMQWiyubP05uDxmow5EmbS_NFbbpncfDAGBBIt-pklVGK6r8dgNuWpT6vrgMJTXJx3SYuQaCjfbICuAXSTMNgyMxODWZ9d28LM48jQt_qPwZPA6KwLasuiiXEBv1Egmr-JijbfN3ga1ZrxIQ6UuyKTxNOU8HLqlUJi8Uh7eqNOeApCl44XsZgKEoDZ5f10ySnMF8BTkjUz7qyewKqBGTrsFoPbr0mHuYQfM87dQZ7baNzkXBqHfd1vEEm56nMLW5o5vbI9IaVxieE8o5nRnSsPbRhJts92vGYTXl1W7Car-OSNSgh7RMem6CtwL6u5k2FK4DEmRYkCGUMXXmKMpPJu17YrxgoE9zh3iA77HYqgqw_MGPGc2h9GVlzuo13eS2ZO25GeS0XgyjK7ifVnWIoeF02qlSO1hcmQvG9Ty5HkzzG7h2pyIDr6wN__SSij-EvJUG4hQ7y8L5OpxB1keVMsy95IaMFvQe4XAunhe4aA5m4Mqa_hBRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد يومين قمر الشيعة سيكون بيننا.. ويجب أن نوفيه حقه بغضاً بقتلته الصهاينة
#قوموا_لله
#باید_برخاست</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81176" target="_blank">📅 11:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e69322afe.mp4?token=AynCBbNVkDhmCbhJ52LL1DEeYWlTM0y5EEeJ0DApaeBNP8SEUPUI_4yX2w9SwrLGgqy4AYm_0v357W8vhVxIxTP15C_s47ef2EOdUca-ScPB4ylA5QILTMVTpBGpOnON-ZSxf_B4Ldnul21g1R5dB-Yi3b8zbyjYluckIdF4fcTV9uoZN2vX8tb2mrj_yVpeULs_HJil6t6Ol3HuC3NfNPg5PgaUtwizoWTd4aP8OJYfYiI70A2ua_lCoHqu8pLP2cagwva_-w9JFJ5gYPWKLa-tIFwCPqD5qTGIRRNdo_i1aoYZKCURY_YESqvyMAnjhKn4lO_KSRMtwPyTZAPazCrBoq1QiN5M3NPuAP6sB7YuPTRI_pTOB1cNpK_qec8AwT2OWd-q1botcgiWYBeJdedFP84WfMS_IgDQGzPxk8w3Mum6N1zZ5pFkXwFtnXaMjx8WwMTQ2RXiYmI82072WrehDsNhED1W-tEEe_6wYXgW_Wns_5h4D_xY8hMdz4K_-almkxFgLKeHTfVOzgqoaLJhuf2-4y0aE03bAe5XqYTYPZ_hOVSybtBpOx-GAavWJBkJx-iubmd3azRjbn9zBwiNTGTa_GtrdW9imnXz7a0-0-i4BDht5BycfAe5rTj9D9WX9Avvd5Awcigg0qbczheDZ9PpEat1JyYcnvZRQbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e69322afe.mp4?token=AynCBbNVkDhmCbhJ52LL1DEeYWlTM0y5EEeJ0DApaeBNP8SEUPUI_4yX2w9SwrLGgqy4AYm_0v357W8vhVxIxTP15C_s47ef2EOdUca-ScPB4ylA5QILTMVTpBGpOnON-ZSxf_B4Ldnul21g1R5dB-Yi3b8zbyjYluckIdF4fcTV9uoZN2vX8tb2mrj_yVpeULs_HJil6t6Ol3HuC3NfNPg5PgaUtwizoWTd4aP8OJYfYiI70A2ua_lCoHqu8pLP2cagwva_-w9JFJ5gYPWKLa-tIFwCPqD5qTGIRRNdo_i1aoYZKCURY_YESqvyMAnjhKn4lO_KSRMtwPyTZAPazCrBoq1QiN5M3NPuAP6sB7YuPTRI_pTOB1cNpK_qec8AwT2OWd-q1botcgiWYBeJdedFP84WfMS_IgDQGzPxk8w3Mum6N1zZ5pFkXwFtnXaMjx8WwMTQ2RXiYmI82072WrehDsNhED1W-tEEe_6wYXgW_Wns_5h4D_xY8hMdz4K_-almkxFgLKeHTfVOzgqoaLJhuf2-4y0aE03bAe5XqYTYPZ_hOVSybtBpOx-GAavWJBkJx-iubmd3azRjbn9zBwiNTGTa_GtrdW9imnXz7a0-0-i4BDht5BycfAe5rTj9D9WX9Avvd5Awcigg0qbczheDZ9PpEat1JyYcnvZRQbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية تظهر كثافة الحشود المشاركة في تشييع قائد الثورة الإسلامية الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81175" target="_blank">📅 11:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b422331f5.mp4?token=GvvpDZXZtNYGHWWos1lsA_Gpl1Fkjd69VCZAflx9ZJ7lnPWQQ4kA6SxDXZZiOE7yzFalcAvUt-H-HwgCwLBCzk4ARvCHJCvUOdVpRHO6h6S5LU6UmrtZs_Pk5rIhogy6wK4ZgcM4r1E0AugMYRp-0l7CnfIXfCpQzEMfBpWu8MHsyMZQGCD-SUievpPThRRexIvmazmgVABZ1cJrKkuW6gro-twcitvHtMQEtamjTH42td7sGEEh7uZ7WOTjZNPNXKPGFH_LkOcyOJx0yoh6e4DlH85vNI39eC7U5LbYfKCQ16CtMOyqYofRK7aoO8pe8Y3m8b1-HqqXyES8P_xhjkU2RxmITxDB48VxBi_n6JwgR_WJC0hSlk0jGZttGufXB15QlzyAxm1-u9ArU449FW-DyhVe9ZGREpP5a6iBkyIktbvp2CPrPIdwKlNOQbp-6eYFsW0UFy0ALePWGwXGozTWoDrpQiQqasYUm0pt1Vk-Ewn2P-_5PVyucvtcLHs_t6H2exKBX8UJcYnr1Xa5vX0531mM5EQGKwq-H3Q_MCKcgmuoRtBaIv9-6kOnnXfuq4iULvEpwmS6PKECxR9gRC03rggRqdhliIYP6TSQIe8yOm5aRz_Vqmn4UVOFkMezc6mQk3Oxa8pdkirPRphBsz2emZFTjwMyJ9Hgvw0xODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b422331f5.mp4?token=GvvpDZXZtNYGHWWos1lsA_Gpl1Fkjd69VCZAflx9ZJ7lnPWQQ4kA6SxDXZZiOE7yzFalcAvUt-H-HwgCwLBCzk4ARvCHJCvUOdVpRHO6h6S5LU6UmrtZs_Pk5rIhogy6wK4ZgcM4r1E0AugMYRp-0l7CnfIXfCpQzEMfBpWu8MHsyMZQGCD-SUievpPThRRexIvmazmgVABZ1cJrKkuW6gro-twcitvHtMQEtamjTH42td7sGEEh7uZ7WOTjZNPNXKPGFH_LkOcyOJx0yoh6e4DlH85vNI39eC7U5LbYfKCQ16CtMOyqYofRK7aoO8pe8Y3m8b1-HqqXyES8P_xhjkU2RxmITxDB48VxBi_n6JwgR_WJC0hSlk0jGZttGufXB15QlzyAxm1-u9ArU449FW-DyhVe9ZGREpP5a6iBkyIktbvp2CPrPIdwKlNOQbp-6eYFsW0UFy0ALePWGwXGozTWoDrpQiQqasYUm0pt1Vk-Ewn2P-_5PVyucvtcLHs_t6H2exKBX8UJcYnr1Xa5vX0531mM5EQGKwq-H3Q_MCKcgmuoRtBaIv9-6kOnnXfuq4iULvEpwmS6PKECxR9gRC03rggRqdhliIYP6TSQIe8yOm5aRz_Vqmn4UVOFkMezc6mQk3Oxa8pdkirPRphBsz2emZFTjwMyJ9Hgvw0xODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعجز العبارات عن وصف هذا المشهد المهيب، حيث يجري تشييع قائد الأمة وإمهاما الشهيد آية الله العظمى السيد علي الخامنئي (رضوان الله عليه) في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81173" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81172">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
الدفاع المدني الإيراني:
لم يتم تسجيل أي حادثة حتى الآن في مراسم تشييع جثمان القائد الشهيد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81172" target="_blank">📅 11:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81171">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAOcgfuYVjmNMgad3E7ldzXZoiHgtp_8icaFA49_hHx6iV_v5YZmZaI96UW0j0b2j-DR5n1yLPjAnbUrXvaftLITCdZ-r3w2TPpTRa9lFFBL7be-zmr8nl-LoM-FrQpSK1GGcpl3sxRHnuUzcUgw-yTUvodyOJtcMVC6ERnGdk0PRWgXBRXaBCRrj1R-wNxJFE-2R6NBpJPrDqz2qtDCSrYOrthhLTBpt_yU1SfLU9075UKbfYxEdXe2F-HwocuU3atpaeM46i1uO61OnocRlsprrC5_uMKUIwjtnpaRc3QyKbAKuuwyaz0FjKBNUgilsMwzouVC2ZE4ygJ_BRJ1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
السيد مقتدى الصدر:
أهلاً وسهلاً بالوافدين الكرام إلى تشييع وتوديع الولي الشهيد شهيد الجهاد والإباء تغمده الله بواسع رحمته.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81171" target="_blank">📅 11:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42524754b1.mp4?token=sd0yVqtduXwcB_9fgdmHxKAw1RmtS7nwdnQTtBIyoNea2awh3KMat605jfo0mNOHdDVRBYNMsBJENCuFphgDAb6JzySQyTu2lgGyyaUeQBuKImTdYBtzevNywWTc-n6jwfl21Gk8OonqWEdBmumdtEhkzb_lGe5J5jyaIycjFy1It6Gda6KuPTU75bx5_4NdIdLKYsqP65XPL3-rDOYq2XkApj0qQOCKZl0uvIF2zlPvc-gTB1hyog9WMtcumU9LPFpecTz0Z-27c2rWt8oXh4mR8q7xBxaL1vNGGGgiug7XL4NpIoRRVdzdD-xygBtL71afhJ6Wuex7apYUcc24og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42524754b1.mp4?token=sd0yVqtduXwcB_9fgdmHxKAw1RmtS7nwdnQTtBIyoNea2awh3KMat605jfo0mNOHdDVRBYNMsBJENCuFphgDAb6JzySQyTu2lgGyyaUeQBuKImTdYBtzevNywWTc-n6jwfl21Gk8OonqWEdBmumdtEhkzb_lGe5J5jyaIycjFy1It6Gda6KuPTU75bx5_4NdIdLKYsqP65XPL3-rDOYq2XkApj0qQOCKZl0uvIF2zlPvc-gTB1hyog9WMtcumU9LPFpecTz0Z-27c2rWt8oXh4mR8q7xBxaL1vNGGGgiug7XL4NpIoRRVdzdD-xygBtL71afhJ6Wuex7apYUcc24og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
شعبٌ لايَترك ثأره.. سيدة إيرانية تعلن عن جائزة 20 مليون دولار لمن يقتل المجرم ترامب.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81170" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-FpBmTKdCoNcsK_CabLtfLss9wVmLS5mdDV0rjwHA10ACc73pYevh9AHjMwyYYxUfGrkj3akoIzZc6DWrty6lCrkxOZeEOIdS4JqAQb6vr-REavGWe_M9NJaLt-5lSz97mMoK3t8oKJkm7tM-oQaD-wDPWaxWn3AC57Qxwo7ZIlcT5yJL48ux-jFTrNPxdpsYHZrRuBJzy0EeUU0c1cggaSdWfbc4FpIFtbuXTkGzSwNXVZANM5tfXS-woX8ZeF2tr3xLlPbv4jKzHgtTegytlN2eY68ytgnUmpb-S68vD7wutBWzeZ0WhmkgPsICcyagUme7dpoxlNb1hOcxCDsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شعبٌ لايَترك ثأره..
سيدة إيرانية تعلن عن جائزة 20 مليون دولار لمن يقتل المجرم ترامب.</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/81169" target="_blank">📅 10:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGU96lS8TGBgGiCvFkKCAirtKniaPhUqJkGMlqP0pDxHlGh7IH8cjtlQPvxvC1YSZ790vPnmrlFltJyeU9nWyd2zcvAe9Q8O4l2-5N3ThqAEN26gjketYJu7au497nzvsesSFjpGzD9TJIKmmP4QzVsfDSMhBlh_OYrJwkZ-OyEFQei18flSNPElpQZFtzOF_DFnKrf6xl4TSU_xNF8tXdH_1z-uO3bNb-RcnWAs48Q4czwUCRAwl2nyND3G_9u77owZeIdtNxRjoxOgF8ey1LGEwCfdPuxvQslqQtgEMeG9GThnUodmJ2PukkdqEMvSsPFgsPsAJTXvg2ZezFflmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
جينه نواسيها اليوم السادة.. أبناء العراق العظيم يشاركون في تشييع إمام الأمة الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/81168" target="_blank">📅 10:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
إحراق أعلام أمريكا وبريطانيا والكيان الصهيوني من قبل المشيعين الغاضبين بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/81167" target="_blank">📅 10:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
🌟
مهاجمة صورة ترامب في العاصمة طهران من قبل المشيعين خلال تشييع القائد الشهيد.</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/81166" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d247494ec.mp4?token=TByIqNSldn65nHiV0xMCodG5-W2bJUxzg_MF4LhWOXTlbcyauQ8NnHG-WtD1CSzU8X9kjJ_rLVBnLa2M2DT3JRQ1zUYcRGOlukDoNpdlCLTG9DGLrw2sUhLfUNgAuiP_pGGq8Za5zV6SZVAJthXGVQ8qsQ74zNG8l4toxeocdi9PsbjmG5dYG9D-esjsSGBEKurVA_1pZ1TJvrKlE5mVh9M0HdvXnTTFKopriYTDBYKbeT88yOSTB_zRH3EtKemgymSKgn9ifa3nvAWbYzoI2XX5-pqzW0zu2aTe8NTengUUPM8trCz4Wbff-EKFlnsgxTQXijKiqXZmuviYX6plYgCDtYPEFd-Y-bkI5_pkVuKyx_59W0--as34BUhKf_z5cTFuL5O0mAGm-FBqq_zWLygje1Rx6yh6_1QoTR_kXHLw2Xx2lEOtV8HnCKInmxBUJlQ-KOFPzD5591_4EhRbqAX8D--kIxqZTOB8utLtJgEeCJiTEA0Mx6EvXu9_wHvm25gGqSCDVuVpxF62lff2QFyDFF7HuTZaL8S2QMwY7jzgu5k5Zh-iQk5Myl93dy2NpPdTCkPcF29GS_6mg7RRc19SBs7m8uYdN1j_BEI5Bj3RwyICRV9fZT5RYcLbLGzNNFazON7rzJHpFjqZdcoTowwFa8jeJv9Irh5mB8Vdqas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d247494ec.mp4?token=TByIqNSldn65nHiV0xMCodG5-W2bJUxzg_MF4LhWOXTlbcyauQ8NnHG-WtD1CSzU8X9kjJ_rLVBnLa2M2DT3JRQ1zUYcRGOlukDoNpdlCLTG9DGLrw2sUhLfUNgAuiP_pGGq8Za5zV6SZVAJthXGVQ8qsQ74zNG8l4toxeocdi9PsbjmG5dYG9D-esjsSGBEKurVA_1pZ1TJvrKlE5mVh9M0HdvXnTTFKopriYTDBYKbeT88yOSTB_zRH3EtKemgymSKgn9ifa3nvAWbYzoI2XX5-pqzW0zu2aTe8NTengUUPM8trCz4Wbff-EKFlnsgxTQXijKiqXZmuviYX6plYgCDtYPEFd-Y-bkI5_pkVuKyx_59W0--as34BUhKf_z5cTFuL5O0mAGm-FBqq_zWLygje1Rx6yh6_1QoTR_kXHLw2Xx2lEOtV8HnCKInmxBUJlQ-KOFPzD5591_4EhRbqAX8D--kIxqZTOB8utLtJgEeCJiTEA0Mx6EvXu9_wHvm25gGqSCDVuVpxF62lff2QFyDFF7HuTZaL8S2QMwY7jzgu5k5Zh-iQk5Myl93dy2NpPdTCkPcF29GS_6mg7RRc19SBs7m8uYdN1j_BEI5Bj3RwyICRV9fZT5RYcLbLGzNNFazON7rzJHpFjqZdcoTowwFa8jeJv9Irh5mB8Vdqas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اليمنيين يشاركون في مراسيم تشييع إمام الأمة بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/81165" target="_blank">📅 10:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180cd7b6ea.mp4?token=RX_lOIgErLfoUvMZdbM_WmeWLL9vnJ0kQbQoK1ibCF37Vs8bk33yesTDxOxU8kFL2Frswt-rVCzjwnf4w8FIikXpLHxqc41j8Uvf8Rw5wZPEHSvX9KnvEBfN2evd9QXe77FlOZ4fXoo_uE8FhdR8-qkiSyMPZP_GGOvMYjpEBu2XCgMIzGq_kO-Yrwf-nwPH47dMG6au_2ebIrKwnbT3ASoRuiUzWHFigbBTzb6dlrBkLDwNicDPg5Fezr8CDk40M76nOqZ59jn3tDZ4VziOMln_iLqJMLMPz-atiYTwzAfP1sE4P-GAwj632NErp6z3x1T2NLz3pSOc9mDiUfT_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180cd7b6ea.mp4?token=RX_lOIgErLfoUvMZdbM_WmeWLL9vnJ0kQbQoK1ibCF37Vs8bk33yesTDxOxU8kFL2Frswt-rVCzjwnf4w8FIikXpLHxqc41j8Uvf8Rw5wZPEHSvX9KnvEBfN2evd9QXe77FlOZ4fXoo_uE8FhdR8-qkiSyMPZP_GGOvMYjpEBu2XCgMIzGq_kO-Yrwf-nwPH47dMG6au_2ebIrKwnbT3ASoRuiUzWHFigbBTzb6dlrBkLDwNicDPg5Fezr8CDk40M76nOqZ59jn3tDZ4VziOMln_iLqJMLMPz-atiYTwzAfP1sE4P-GAwj632NErp6z3x1T2NLz3pSOc9mDiUfT_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
إزالة صورة المجرم ترامب.. غضب عارم في شوارع العاصمة الإيرانية طهران أثناء تشييع القائد الشهيد، مطالبين بالثأر والإنتقام من ترامب والمشاركين بجريمة إستشهاد الإمام الخامنئي.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/81164" target="_blank">📅 10:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0db34ce8d.mp4?token=S8FSfuPuWb_LbEQgHcWzew1R_agS6XhTYeYY42F4Mcz0ZP9zb9ADPxpf6UNaxvmXd0UgHyKJuzZQ_6oR8WH15nkIuCIw5en2tXkgnfGT6TuIZqn_HQGPHr1QNjTrSwwegE1HxVFBjvgCc6S9sQTp9s8tc2LM-_4ku0f6JufM_NbMGeBP5V5rOnmbSMiVuS7koDnAU2hlTyKnM8Q2MrTQ3s8lvQrvZjGlJbiN4zwIjSYnul2HjX2O_7MrILULT65hJxxaeu7yF4CD0bfU-3MkvzSc7YvaJLjxWxkETaDMhom8zTdu8HS_lGw-I9U6Kco4ol5HlWLee2G6VgT2dvkS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0db34ce8d.mp4?token=S8FSfuPuWb_LbEQgHcWzew1R_agS6XhTYeYY42F4Mcz0ZP9zb9ADPxpf6UNaxvmXd0UgHyKJuzZQ_6oR8WH15nkIuCIw5en2tXkgnfGT6TuIZqn_HQGPHr1QNjTrSwwegE1HxVFBjvgCc6S9sQTp9s8tc2LM-_4ku0f6JufM_NbMGeBP5V5rOnmbSMiVuS7koDnAU2hlTyKnM8Q2MrTQ3s8lvQrvZjGlJbiN4zwIjSYnul2HjX2O_7MrILULT65hJxxaeu7yF4CD0bfU-3MkvzSc7YvaJLjxWxkETaDMhom8zTdu8HS_lGw-I9U6Kco4ol5HlWLee2G6VgT2dvkS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
مهاجمة صورة ترامب في العاصمة طهران من قبل المشيعين خلال تشييع القائد الشهيد.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81163" target="_blank">📅 10:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b95403b3.mp4?token=Bd9G0REZsK8gHZjGvlfVISA-Bc_Ofh7vkRn6GA_rr4DqdnGMUVF0AodeNKWHGtFyW-6rWM8gHwO13eu6nc9Hp2lu--NhxMszRtWLqSbpxTMrULvYNZa-BE4HDGQ1diQ_T31EjGwNHek4d2ma3SGTfpoEkbCQijt2_S5sFWlp5tsaQRsfb0-TOkafkmfTccJ9Ded5l_cvvt-733-BkZ1VsJtMmuGLFCkr-t9Oi3_Mki64bPZ7uiHlzBDjig0eecsB-_VdGzXaNGXtMmucMuOEA1SKq3O-8GH9vUeq3iZdGz_FDLZ-J54d9cf57xYisPRUejPOf0s17G-MmojlnzBhXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b95403b3.mp4?token=Bd9G0REZsK8gHZjGvlfVISA-Bc_Ofh7vkRn6GA_rr4DqdnGMUVF0AodeNKWHGtFyW-6rWM8gHwO13eu6nc9Hp2lu--NhxMszRtWLqSbpxTMrULvYNZa-BE4HDGQ1diQ_T31EjGwNHek4d2ma3SGTfpoEkbCQijt2_S5sFWlp5tsaQRsfb0-TOkafkmfTccJ9Ded5l_cvvt-733-BkZ1VsJtMmuGLFCkr-t9Oi3_Mki64bPZ7uiHlzBDjig0eecsB-_VdGzXaNGXtMmucMuOEA1SKq3O-8GH9vUeq3iZdGz_FDLZ-J54d9cf57xYisPRUejPOf0s17G-MmojlnzBhXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
يالثارات الحسين.. بحر من المشيعين في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/naya_foriraq/81162" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abd840738.mp4?token=MgZd6l1KRpFCNWMXcPNKeJmAnD802UQ6CHeXRqPBlJG8MQJdnOKwDKcemQu9qOoJ2fRJOp1yRG-XDrFP93-XCESKmH9jkE_vg9rCcntwgGpJSylpKMP6Rr6QtRas3YXjAaGo_ConCj5MpzVKtdDZmqrepTisHIhhI0S2AJQrv-Tv5zYKv_y7tLif4Q8rB8UiyJOtkyJJeHp0GvbxRSjaVTn5EXlCFxNsZK4AowzGHk49Fa15Y3J_tXAlbsdQsUDxwdDDkM4m_J3ldq04RwCjyODvjvHXH6sLy4wxV1WUhArCIdUnIEVK3rOqUI4bZNPcSO-GXFxLGOt3UtjPdbF3r3zsMqHj_t-DM1skxMHahtTzPE_OdaF_5i8-IgxvO6jJfs5pGv-EiDbOWEXVhvwo9CwTH54KxA9aM4ui1KsUr-PMjrVMCZ-CaDdPXHi2fHVKjZazweJRvCtCXD3f8Q9uQdJE7G3RSWUMjcy40DUHnPOI4i7UPoo2qsbpCz0nOcwdgu5_FRBeEFA92jMcDoUwVxP7G1kC6bpLcq-qsrLns_nmcdf958w2WF8Fi_4plAl4NrvoGQTXx0tgvAp8PQ1h3LohiLW1iADJDxnVOPl1SizZIT5w41HP6Zpm47OG7rEwM-xvAc2qQLe8pqlCLKL-k02nsw0t6RzZiH8HvxlkKx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abd840738.mp4?token=MgZd6l1KRpFCNWMXcPNKeJmAnD802UQ6CHeXRqPBlJG8MQJdnOKwDKcemQu9qOoJ2fRJOp1yRG-XDrFP93-XCESKmH9jkE_vg9rCcntwgGpJSylpKMP6Rr6QtRas3YXjAaGo_ConCj5MpzVKtdDZmqrepTisHIhhI0S2AJQrv-Tv5zYKv_y7tLif4Q8rB8UiyJOtkyJJeHp0GvbxRSjaVTn5EXlCFxNsZK4AowzGHk49Fa15Y3J_tXAlbsdQsUDxwdDDkM4m_J3ldq04RwCjyODvjvHXH6sLy4wxV1WUhArCIdUnIEVK3rOqUI4bZNPcSO-GXFxLGOt3UtjPdbF3r3zsMqHj_t-DM1skxMHahtTzPE_OdaF_5i8-IgxvO6jJfs5pGv-EiDbOWEXVhvwo9CwTH54KxA9aM4ui1KsUr-PMjrVMCZ-CaDdPXHi2fHVKjZazweJRvCtCXD3f8Q9uQdJE7G3RSWUMjcy40DUHnPOI4i7UPoo2qsbpCz0nOcwdgu5_FRBeEFA92jMcDoUwVxP7G1kC6bpLcq-qsrLns_nmcdf958w2WF8Fi_4plAl4NrvoGQTXx0tgvAp8PQ1h3LohiLW1iADJDxnVOPl1SizZIT5w41HP6Zpm47OG7rEwM-xvAc2qQLe8pqlCLKL-k02nsw0t6RzZiH8HvxlkKx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لافتة كبيرة تحمل عبارة "سنقتل ترامب" باللغتين الفارسية والإنجليزية خلال تشييع القائد الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81161" target="_blank">📅 09:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81160">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd3ecf504.mp4?token=mC0mfV6Biu0Q8HOuQsqwgZTD28-1qAwCxig2NhMLd-lOSf7iZ2Cy3wRkq3O5pJe9NIh84y5Le8Zcz6Ykb3so_jxuMdOLvk11vOJjOLioRTsv_795s6NNSb5GjGH7r44TeH3PVb8So1WTeIgjYfvzZhhz4hmmiEfB8tzcvdxHis8rSGrNFaiflRBMwdd56qXJdD352fNQXzRegcSm5T1DfWmY7D5UUfk7Hp55pw1afpyLrdZBG28N4iWwKgP--wPHix7iHslG8ooH-aTkHOJJKeo5JEgobMXw1XIX2j-t0C_Od9OLWfsYonIfWcJ8SWA3RCiZQg1xFnPgsjXoYALKdlZE9_OERfPVlPWxjJIBtUZpHa5uOczFAIgWVIIsFwFHZnLqd5iTy8NHWV0e91OHw9L7EyF_YlzIwkDqibYsLsHVVXTQEbVmCLdZ1KgXdDgptBn_MnN3gbjuALtMkm_PJ7VU1Pz2gBWLivJCRFWcRHx04lEay8OM-y3wtCN9pqGN7u6o9n-r_9qp70X-iaFVDZYbHWNIB3V1M7_V971WG1u6Z6pOA5_lUYAt3iil_oAivpLE-aj77Cnmhg398BPrADvJwSEdPMaqZLA-VLjhaWZLMdg9KzqI4BvWc3QVzj8UcmI8UBboln-p75f_4vg4xkJYHoBxBua2ZIORnubrfzU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd3ecf504.mp4?token=mC0mfV6Biu0Q8HOuQsqwgZTD28-1qAwCxig2NhMLd-lOSf7iZ2Cy3wRkq3O5pJe9NIh84y5Le8Zcz6Ykb3so_jxuMdOLvk11vOJjOLioRTsv_795s6NNSb5GjGH7r44TeH3PVb8So1WTeIgjYfvzZhhz4hmmiEfB8tzcvdxHis8rSGrNFaiflRBMwdd56qXJdD352fNQXzRegcSm5T1DfWmY7D5UUfk7Hp55pw1afpyLrdZBG28N4iWwKgP--wPHix7iHslG8ooH-aTkHOJJKeo5JEgobMXw1XIX2j-t0C_Od9OLWfsYonIfWcJ8SWA3RCiZQg1xFnPgsjXoYALKdlZE9_OERfPVlPWxjJIBtUZpHa5uOczFAIgWVIIsFwFHZnLqd5iTy8NHWV0e91OHw9L7EyF_YlzIwkDqibYsLsHVVXTQEbVmCLdZ1KgXdDgptBn_MnN3gbjuALtMkm_PJ7VU1Pz2gBWLivJCRFWcRHx04lEay8OM-y3wtCN9pqGN7u6o9n-r_9qp70X-iaFVDZYbHWNIB3V1M7_V971WG1u6Z6pOA5_lUYAt3iil_oAivpLE-aj77Cnmhg398BPrADvJwSEdPMaqZLA-VLjhaWZLMdg9KzqI4BvWc3QVzj8UcmI8UBboln-p75f_4vg4xkJYHoBxBua2ZIORnubrfzU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
جموع المشيعين يحيطون بالمركبة التي تحمل الجثامين الطاهرة المتجهة نحو ساحة الحرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81160" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c809f5d37b.mp4?token=vBB8Ab2TTZVucwtqj6neNw0GSYRUyDfKisZ1zalV3e71SBir0KjWFPU7sKXd8lc2lC66fPjjhjRQ-WwlR1ffrk6pPGns5mcJ6aDpEi8qJmysbyqRuOdKkP6snnllAoETtgH6jbS8H6N-YfnYpqDLelvdMX9FK2cw5WHCFvkAEf0H_dIrZcWMMMh-rac7sb_BqVda-XOhSgLMZ2OjD-DPIYOzN9k0l8-wR40DSfLoUYxbymNo_7J8fWFTGJtzZCVMn_cqVNXCN8jglZC2sCIa5snGU6730IfiywtObLyHKm0vlrtrV2ZSbRRo49Pq9GBuOTY1whbFHgOkRJgLdLd3GrotlvUHNciQzk8QrmC3hGcCyXNZqTuQLblcwH19ZBS41nS7yZvwBYAyjobqlgFL_X9xGpfqoK4HY4N9KdM5iVpUvGblrYZuUwzpGbEbBSOkXVgiHeP3wldYlodCHkkS-J9OFszjsu31p-w8CtyUJShIFRmzG-r2ybaczysHu7FP9o2-u5QiuVOzpm_ke23A5ibf98xIgRhkQWtsIFBuWajDTwmzlRhRDWB0KDRb6Bdy--liSk0mKcn55iCr1SosFXC16grwmmh5jwrK-qWXSDjFZuY_6LvTcFYO0bPhO3rgL17kDrGu0RhW1jtZtTEeSkpMpn7-RfpqrvlHAmUGsWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c809f5d37b.mp4?token=vBB8Ab2TTZVucwtqj6neNw0GSYRUyDfKisZ1zalV3e71SBir0KjWFPU7sKXd8lc2lC66fPjjhjRQ-WwlR1ffrk6pPGns5mcJ6aDpEi8qJmysbyqRuOdKkP6snnllAoETtgH6jbS8H6N-YfnYpqDLelvdMX9FK2cw5WHCFvkAEf0H_dIrZcWMMMh-rac7sb_BqVda-XOhSgLMZ2OjD-DPIYOzN9k0l8-wR40DSfLoUYxbymNo_7J8fWFTGJtzZCVMn_cqVNXCN8jglZC2sCIa5snGU6730IfiywtObLyHKm0vlrtrV2ZSbRRo49Pq9GBuOTY1whbFHgOkRJgLdLd3GrotlvUHNciQzk8QrmC3hGcCyXNZqTuQLblcwH19ZBS41nS7yZvwBYAyjobqlgFL_X9xGpfqoK4HY4N9KdM5iVpUvGblrYZuUwzpGbEbBSOkXVgiHeP3wldYlodCHkkS-J9OFszjsu31p-w8CtyUJShIFRmzG-r2ybaczysHu7FP9o2-u5QiuVOzpm_ke23A5ibf98xIgRhkQWtsIFBuWajDTwmzlRhRDWB0KDRb6Bdy--liSk0mKcn55iCr1SosFXC16grwmmh5jwrK-qWXSDjFZuY_6LvTcFYO0bPhO3rgL17kDrGu0RhW1jtZtTEeSkpMpn7-RfpqrvlHAmUGsWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الحشود المليونية التي خرجت للمشاركة في تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81159" target="_blank">📅 09:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02d27f89c.mp4?token=YWbR0WsW_iK7-O8VOCi9l89B90EMnla8Srnb2qqkSBosot-wSLJVtooRQdVp6w8sA7Uwreh-A9ya4TsKJfe4Z4zL4TJbxVWwY16OXpBDZ2htixk4JoUORvoUyLKYdFfNlG2aQiez9qK-3Yel2A2ZRFFdrjIJAPMtUleG_jquuKfb20Op9Xd3pCVAJopMvNL5_UCHAP3tMlUjVYsoPWVaPLcGvWDqBmiQw6s-R4v7lr_15QWRABlC6eWypL5qbiwBOGr8RDNfN4JV18uBjGrJyy2E3ZYFANNeubHombT1QyZhDmmCkbdS9RJU59gr0ajqgAdyWD_zLdZm7ppf5z4_0nFSifqgAvv_SLSgL7lPC0kXOWw94OSsOHaFAiUuClFKzRtMviHixMDMHCz6PDRHNgL7dDV4RNO-luKPxUPf1LO8sCk4-9DHGYnD_Fvk8S_zj6CpjybAPLmR7R3Z1LuAju6ga4F8kgYJxbG-1R9KsUD0cmdRYagnf3zSajqiDqncRr1ty_J9f5UhmmoB76cmin0VKYTKSHA3nPpeCiq69XF0c-RQhe1fMshAockNhIUxMp6f3GZXHbtq4lRhEzd9uJ2bTfAeOixK4TJhR9uT8h4ps0fIW6rN8iMvZdHCYTob_YonqVKrZEzBO9JqdRLHAYvknKR_R6ES9q7wt1XHTck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02d27f89c.mp4?token=YWbR0WsW_iK7-O8VOCi9l89B90EMnla8Srnb2qqkSBosot-wSLJVtooRQdVp6w8sA7Uwreh-A9ya4TsKJfe4Z4zL4TJbxVWwY16OXpBDZ2htixk4JoUORvoUyLKYdFfNlG2aQiez9qK-3Yel2A2ZRFFdrjIJAPMtUleG_jquuKfb20Op9Xd3pCVAJopMvNL5_UCHAP3tMlUjVYsoPWVaPLcGvWDqBmiQw6s-R4v7lr_15QWRABlC6eWypL5qbiwBOGr8RDNfN4JV18uBjGrJyy2E3ZYFANNeubHombT1QyZhDmmCkbdS9RJU59gr0ajqgAdyWD_zLdZm7ppf5z4_0nFSifqgAvv_SLSgL7lPC0kXOWw94OSsOHaFAiUuClFKzRtMviHixMDMHCz6PDRHNgL7dDV4RNO-luKPxUPf1LO8sCk4-9DHGYnD_Fvk8S_zj6CpjybAPLmR7R3Z1LuAju6ga4F8kgYJxbG-1R9KsUD0cmdRYagnf3zSajqiDqncRr1ty_J9f5UhmmoB76cmin0VKYTKSHA3nPpeCiq69XF0c-RQhe1fMshAockNhIUxMp6f3GZXHbtq4lRhEzd9uJ2bTfAeOixK4TJhR9uT8h4ps0fIW6rN8iMvZdHCYTob_YonqVKrZEzBO9JqdRLHAYvknKR_R6ES9q7wt1XHTck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الحشود المليونية التي خرجت للمشاركة في تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81158" target="_blank">📅 09:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed80a1b5c.mp4?token=lMql4WFLov_rB2XuGNjp_C5Igd6guw-IGA-A-rQQ7c6cnqghQYcXetCGpB6K3uGPrj_m1zHKz1UVPLelJDApCKO0kgrm6G3jI4OPv9HHzV8-eqBjQEsC4hvVL0wzdbnTQc5YZf7ydUE4vAh0uxO6vF1niwwWLhGzIgVFw6z1PV9s-iytiN536FEXTiYbA58B3sB8ydho_WNob1YGRfUlaWEVPM1Rqx_7Pqo9KZlsCiMEyJmt3JcFo6DV1hZwu7Pw-ojf8adBUtTgHwBFG1_91pT6yns6Nc00G2KVBIw_PPY64g6f5EMnIIyrq5sxSIdDooGHUydEySQo1BUt9AcOtrtg-TO1th1ljggw4oU554RUsa9e1EB8tS2oO3VkNcX3nnixLRL1G1ON7BfgpKCzcIPiFVK4w6Z3mBMmiAk3k3Rt-R68XOTnZftmL5uol9xoIVlGOjExIHoeTU-Zw_X64RtbB3KBLRc9OtjJQ8s4hpJDFAuLz8EJZmHllmfuLHpoRERYbXzsVb0kyyzBBziOAE2QHBWjR4uTWchvl8VySaUsaVitdQb2Z4L4UdUNgniHA8P4XbQSeoZ1-nCvMqJEGwocwtae8PzrHR6lyb0qKyqwiKxAc0WwWx-S10ZeaLIjYdsKp2imxGDgBYTyeRGYr7yHrevwFyMrRBpBar2LYcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed80a1b5c.mp4?token=lMql4WFLov_rB2XuGNjp_C5Igd6guw-IGA-A-rQQ7c6cnqghQYcXetCGpB6K3uGPrj_m1zHKz1UVPLelJDApCKO0kgrm6G3jI4OPv9HHzV8-eqBjQEsC4hvVL0wzdbnTQc5YZf7ydUE4vAh0uxO6vF1niwwWLhGzIgVFw6z1PV9s-iytiN536FEXTiYbA58B3sB8ydho_WNob1YGRfUlaWEVPM1Rqx_7Pqo9KZlsCiMEyJmt3JcFo6DV1hZwu7Pw-ojf8adBUtTgHwBFG1_91pT6yns6Nc00G2KVBIw_PPY64g6f5EMnIIyrq5sxSIdDooGHUydEySQo1BUt9AcOtrtg-TO1th1ljggw4oU554RUsa9e1EB8tS2oO3VkNcX3nnixLRL1G1ON7BfgpKCzcIPiFVK4w6Z3mBMmiAk3k3Rt-R68XOTnZftmL5uol9xoIVlGOjExIHoeTU-Zw_X64RtbB3KBLRc9OtjJQ8s4hpJDFAuLz8EJZmHllmfuLHpoRERYbXzsVb0kyyzBBziOAE2QHBWjR4uTWchvl8VySaUsaVitdQb2Z4L4UdUNgniHA8P4XbQSeoZ1-nCvMqJEGwocwtae8PzrHR6lyb0qKyqwiKxAc0WwWx-S10ZeaLIjYdsKp2imxGDgBYTyeRGYr7yHrevwFyMrRBpBar2LYcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
وسط أجواء حزينة.. تسير العجلة التي تحمل الجثامين الطاهرة، نحو ساحة الثورة بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81155" target="_blank">📅 08:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13427680a.mp4?token=dKLqnaKyFU-0EwRU0EHZwJq5i0Y173QkRh9p86q3qVZjWaV_LPfilGNFCXk1eM3qU5a4wYvJJwnL4vILbxEAMGCbFiEP32gnuE2KPETAUvwKtmuaRFTn2TQOyT2QGfG9P6LS2StpEXAzMyyBqSMYrcLvan0Cg3eXDJo6dsMqUb8P5u2Kv6BC_Tc65EIYOCwd8NYVx4qknZ7MkTHYMWkQlCPMUch2rNaLiOvDWAoqNmel1E7QY9ZgJQriEkXmoV9RVMegkphzOHo-JXfPhO3CgP84f06UM96HyaGQaSJxEp9t0tk3YBaMK5dD6GigxzhUqJ05_s2BtqHS0zflSaIGbjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13427680a.mp4?token=dKLqnaKyFU-0EwRU0EHZwJq5i0Y173QkRh9p86q3qVZjWaV_LPfilGNFCXk1eM3qU5a4wYvJJwnL4vILbxEAMGCbFiEP32gnuE2KPETAUvwKtmuaRFTn2TQOyT2QGfG9P6LS2StpEXAzMyyBqSMYrcLvan0Cg3eXDJo6dsMqUb8P5u2Kv6BC_Tc65EIYOCwd8NYVx4qknZ7MkTHYMWkQlCPMUch2rNaLiOvDWAoqNmel1E7QY9ZgJQriEkXmoV9RVMegkphzOHo-JXfPhO3CgP84f06UM96HyaGQaSJxEp9t0tk3YBaMK5dD6GigxzhUqJ05_s2BtqHS0zflSaIGbjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81154" target="_blank">📅 08:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5DlHfysNWA3AD2rxANS0jCIvEljU5oGauNkzUWFXt3OI_ONmZZUNP_kES5LN8EsMGxMR1miTgQ9VtOUajMNlIugVpfK4psRz3h0sZ9p0NV5n9DeerQ2oQDqqLG5NFYc79YDsrAgCrTJa8ZEya3CVJr2UrvVEztBeHwDBnRxfUeO74irzPc7J4HmXStfYJns7iV12HFyxoO2xfUdOcSjFHSoEqFLzPwLN-qgjQaL31-bHUKUMFEUG07eePRJWCNp61N36ES4gUo5FfIdC23S6iMOK45g1e7H5BKsqSjIOBMF_0bBp6i4SnAc_jKLAHth6yL5JLt6LDX4ze8Uln4r3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81153" target="_blank">📅 08:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6616f0efeb.mp4?token=eo9Yyi2g_Wry2TqHLpFUlIECHR6mc7mTPwGGNa5tZQw0mAGPi-LS3p_X9qPK_zsva0Qrsrb7Bn05vo_r9NnBpvRx0tvoKG0QphG3vL3HsjD9H5YxOIssX6gaK6dEEgHIQ_nuxzdxNpmCWKmsS7BHysuK4PsNfvl9oLCKPofFnZPJmnPZkHAH15seETFXuf6Vcmh_7XtNEjaqaREwT127_Fyk-uuxzerYnb_hlCRgqj8v6NOL-i83DnKh2PO2gAOTec6TmLXNn194o0QC3V33A3Zgilb9p4jJrrUjQzBs7qQbQWkb7PxX5JTBlWll0jgZ3HClvyc08FBJ4XuiC9uzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6616f0efeb.mp4?token=eo9Yyi2g_Wry2TqHLpFUlIECHR6mc7mTPwGGNa5tZQw0mAGPi-LS3p_X9qPK_zsva0Qrsrb7Bn05vo_r9NnBpvRx0tvoKG0QphG3vL3HsjD9H5YxOIssX6gaK6dEEgHIQ_nuxzdxNpmCWKmsS7BHysuK4PsNfvl9oLCKPofFnZPJmnPZkHAH15seETFXuf6Vcmh_7XtNEjaqaREwT127_Fyk-uuxzerYnb_hlCRgqj8v6NOL-i83DnKh2PO2gAOTec6TmLXNn194o0QC3V33A3Zgilb9p4jJrrUjQzBs7qQbQWkb7PxX5JTBlWll0jgZ3HClvyc08FBJ4XuiC9uzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81152" target="_blank">📅 08:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7081ef9.mp4?token=RZgpselYws-y54LaBEjU9rjI63yifGHQTX1xQaWDawh0fUQBzuHr7UJ93E0g2svMnFJsXfZUDp11MPL0c6hZE4176QdhcC36TiZZEiNXuRclGjqntuOa2ELzNUEmAkOOH7AMqswZ29zbcfPuNU1XEln-vIUNeczv8CnWJVRnPUP0JcOGnajrqfe4s29HWUiEl2sw8-jQTTAP-iNK2r7HJDbVE0zFVqb67Yw9857shiBUnzoeegyJErQtNGhKIWWFm7ISonvE-6wNsb0XBYa6MbB-c2e2WrZXM4TIgXBlivfC2DOlfeDbYeozhZjxsqGqFqyg-Qm3G8RcMToIf8DNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7081ef9.mp4?token=RZgpselYws-y54LaBEjU9rjI63yifGHQTX1xQaWDawh0fUQBzuHr7UJ93E0g2svMnFJsXfZUDp11MPL0c6hZE4176QdhcC36TiZZEiNXuRclGjqntuOa2ELzNUEmAkOOH7AMqswZ29zbcfPuNU1XEln-vIUNeczv8CnWJVRnPUP0JcOGnajrqfe4s29HWUiEl2sw8-jQTTAP-iNK2r7HJDbVE0zFVqb67Yw9857shiBUnzoeegyJErQtNGhKIWWFm7ISonvE-6wNsb0XBYa6MbB-c2e2WrZXM4TIgXBlivfC2DOlfeDbYeozhZjxsqGqFqyg-Qm3G8RcMToIf8DNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همه آمده‌اند، با پرچم سرخ انتقام.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81151" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22423dd0b.mp4?token=SB_i_2NlVH9pEzkw6vze40FjggJPGc9o1rRsjQyao3e9KV1aouf3RLay8GZLOY80OfGUAvKlr3_wo3Co0B4ndxalPC2dONQtsn2rFKJWfcR0Q_QBRNnQEEzTVRrksFVDZWmK1ki_LFoJiPJjMrspFR97gRjEqBfTtWExD6QWJvrTGowcOo24fdHuQMz5lddYvjdCTLRN9V6YYXifGWnGsNV-T9NhA8EMYWbMIDy7CBELv6rPCmurMTVRMhKvaY6U_iSmLqbVcI16qH5-jXjv26aLH11_YqgwJMuXbln6Li-L1rll8l-ue0Se1JNnty6fklwJRgRieydgsauKn-exEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22423dd0b.mp4?token=SB_i_2NlVH9pEzkw6vze40FjggJPGc9o1rRsjQyao3e9KV1aouf3RLay8GZLOY80OfGUAvKlr3_wo3Co0B4ndxalPC2dONQtsn2rFKJWfcR0Q_QBRNnQEEzTVRrksFVDZWmK1ki_LFoJiPJjMrspFR97gRjEqBfTtWExD6QWJvrTGowcOo24fdHuQMz5lddYvjdCTLRN9V6YYXifGWnGsNV-T9NhA8EMYWbMIDy7CBELv6rPCmurMTVRMhKvaY6U_iSmLqbVcI16qH5-jXjv26aLH11_YqgwJMuXbln6Li-L1rll8l-ue0Se1JNnty6fklwJRgRieydgsauKn-exEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحشود المليونية تنتظر وصول الجثمان الطاهر للشهيد القائد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81150" target="_blank">📅 06:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRdZxVkEC7aYj66tRlple5zquRX0nwTetdRAJhhqplbJgN5Fy7WdQxy-ZUu0adpSN2U3imvcGIjFyAVAtqRngt45rj_iiG19IwcSQUrC9TyAVayZkAKs4XWxg2znAz3IAi3v4dapy5Xfxj_oNuMp1fTW7os2GtGdFSGdxMCdDCehFMXZo0frIYFHro-vJOmMAkGp05InTp9V9kWTNfXQLX8C9mVhLlYurodvE5sQsnqu4Q9wlPVH15DHzRUDpQboXnDS0BKURbSEj8JCmMXo01XhWuNZb4etZncLrbIU6rWlCSP8HycEbCZ8K5bKCUMVRp2ElreJn1Wpp-7b_FqP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
سنقتل ترامب..
الشعب الإيراني ثأراً للإمام الشهيد، يتعهد بالقصاص والإنتقام من المجرم ترامب.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81149" target="_blank">📅 06:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkVA9mgS59PyLYumAQp15cZ0rtzE4bU0isnA6vaNlwNCmlB-yAgbkDszHKWbs11h8vsKdXAVUMhcfjIaFmafEWALzAAKLA--VHHkRmkhYdY85-NS3lxHSglirUsGi0d7xK5tuEJgJqmVIN1nEdUgts890BalxWdU1IWmnD-KTNWXHdqItr80Ou8ADUABS4A7O2B8YC_7koN_mai2Itl-_d-2GMB0y6xMWOxynRMSdCpR7aJh5yIb6AHeEEViPDAtP6EAlyOApVWzT3hPjmv-_N2xG9h-2ktdJvtt2OKvh4FOBmdt7Rhu4vz5vAibf6kytGNQnLJaiQIAKlDmzJH7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحشود المليونية تنتظر وصول الجثمان الطاهر للشهيد القائد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81148" target="_blank">📅 06:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d52e5f01.mp4?token=AR2jTdNe8K7MLI7Yu-IFxjLTk-as98eLccpXqGQWVmkzodJ9JRBYteaT74dMyqGuZGM_WlQDpuKDr1GJeE1Dq3jnr-Mqj08t91zehpotJaJrAGRl3bJwMN3Unrih9iwKpxUeLxXCiige_0CjrnQ1Fm1IbZg4qHRM_ZwOElzIy73rhjk5gTW7AJmQUsEJFpuG1YuPlQhMheop8fe06enDkEZRnNAQkUMy_aS9Z4qvZWrDlhDHsGFzxhyEtTvah3VWISo6gFWs1KE4PS7T3RPH_8d3jysDTa7eVOmEJOxM1d1qMjXRO22TeXLvDKEUoRmncSRzbv0sAZ18XoOfqJORUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d52e5f01.mp4?token=AR2jTdNe8K7MLI7Yu-IFxjLTk-as98eLccpXqGQWVmkzodJ9JRBYteaT74dMyqGuZGM_WlQDpuKDr1GJeE1Dq3jnr-Mqj08t91zehpotJaJrAGRl3bJwMN3Unrih9iwKpxUeLxXCiige_0CjrnQ1Fm1IbZg4qHRM_ZwOElzIy73rhjk5gTW7AJmQUsEJFpuG1YuPlQhMheop8fe06enDkEZRnNAQkUMy_aS9Z4qvZWrDlhDHsGFzxhyEtTvah3VWISo6gFWs1KE4PS7T3RPH_8d3jysDTa7eVOmEJOxM1d1qMjXRO22TeXLvDKEUoRmncSRzbv0sAZ18XoOfqJORUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أبناء العراق يشاركون في مراسيم تشييع قائد الثورة الإسلامية الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81146" target="_blank">📅 06:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1119c62728.mp4?token=qYNte4iDPxZb53Zv_xEN5BDJgEiUqW_j_P2NwCA5Fw1S1DB2lDv92qsMT0xLkbT5rREc3UfC13gymxpl8-6FT6wfsr8HDwiUwWpREMrrcsr-Tywyr0TyLL4-L8KOEg8Flfmtz9aSjsHddNDb5vtnLFmwgedSOpDZtBmPdpJ1IJZpDcd5qy3fvighzmbwhUr_Yf-qM2X8oMtT7kCKQB8FdmdmaL-Ek-VGbWNLv-9Hrbcadb4Px_8FDbLDeXxEDaVkUuc-KYFo3aZESSi3AU2WWjOz23SrJjJrtPDpmDiYJwam39NZsh1t6bxMIplTaF7B0Gcb4a998h5K5ijBpFSIBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1119c62728.mp4?token=qYNte4iDPxZb53Zv_xEN5BDJgEiUqW_j_P2NwCA5Fw1S1DB2lDv92qsMT0xLkbT5rREc3UfC13gymxpl8-6FT6wfsr8HDwiUwWpREMrrcsr-Tywyr0TyLL4-L8KOEg8Flfmtz9aSjsHddNDb5vtnLFmwgedSOpDZtBmPdpJ1IJZpDcd5qy3fvighzmbwhUr_Yf-qM2X8oMtT7kCKQB8FdmdmaL-Ek-VGbWNLv-9Hrbcadb4Px_8FDbLDeXxEDaVkUuc-KYFo3aZESSi3AU2WWjOz23SrJjJrtPDpmDiYJwam39NZsh1t6bxMIplTaF7B0Gcb4a998h5K5ijBpFSIBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بدء مراسم تشييع جثمان الإمام الشهيد بشكل رسمي في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81145" target="_blank">📅 06:18 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
