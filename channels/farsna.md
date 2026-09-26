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
<img src="https://cdn4.telesco.pe/file/BtMVHioafcblr0vb-bN2CO2-05L0-WY5d1EccOgFgi8JhHuqcPg4kq0Ey6Khu03H0uPkLyQuT4DdFRj-tdWC8t3BNSfxhL-7wG5cl4xJhdiR5EdnHBhX3UD54z_gxxUf1u3rcrCqbUw5nRgpiKe9dPZ_BEx_1bAfzGYt8lab2iny2cHjXJdWR-7PhLrvGKLiaoJjwliEkUIFrcXw5Bf-v1Ix37SzhWbrWgdGjy5YvhUt6CMVETPpk_36efT8RPjrgLUz6ED6rtFr3l4RKVNzbmBu3uTRKTc5DYiHdjw9cLMh1JKw86laChrS2WTHsZ8fitIvwqkUEOtjLxz9X6ja7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.88M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-464484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d750122962.mp4?token=inVzIIrTM0tbHRIoihSm3-EdNCtYGi4h_melNKHVoHdK6gY0aOYgyMPBIxxYG7vO0UESPbZtI6ZlRvfmiWB8bb_BFQUDAUTblEdGUYAvD2L7Q03DNMp-PcS9HANZkhqnYPqG96RX_-bkto7XTw0VweRw-fxH0ts8uoODa1PSnm2tdGoQ5GYe48qPo4utimA5hwySsoAoCopXjSEizmbcgnKYfBPn8LD13rMyb0LEXVvSqV8vZT8RyFV5SHpFFCasATSOKGDsBuYSydOjnWKto8xMuJXWfsgfqmQkvQuhiWBZrxhK4X8oHA_-Eo93Gj1V7jltu2BxAo8frd9e90is4rD790rdeialyPA7nAb_EBrGnrkxiAC-p19FiPoymCpD7MMAlzVpOFsl9DQuKnKlHbeymuz39wpQ91PSjZK3KFTWAJPaOvnMxYjLXfOZJ2LfuFi7ZXeaTcCi3J8_iP-AWwCwltdyseehlFXcnewSTjdOpBdQb__Rcg_-MzcOEM8hrzVNSZT2PR9uxFFUT90M0Rm8Nh_QTzsE4qgjBu9USLyh5zR-xQ8s6o3sXeHeNR-xeQeryNYpEoQa81WDtOlx11s-0DH2suHPtDSYz7CJvVwu9uk1Uq1c5-BUG2EOuw-JrL0djY1RIIiJvSZ7sKETvHwRuCgkkA_iw1cv26Y-EbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d750122962.mp4?token=inVzIIrTM0tbHRIoihSm3-EdNCtYGi4h_melNKHVoHdK6gY0aOYgyMPBIxxYG7vO0UESPbZtI6ZlRvfmiWB8bb_BFQUDAUTblEdGUYAvD2L7Q03DNMp-PcS9HANZkhqnYPqG96RX_-bkto7XTw0VweRw-fxH0ts8uoODa1PSnm2tdGoQ5GYe48qPo4utimA5hwySsoAoCopXjSEizmbcgnKYfBPn8LD13rMyb0LEXVvSqV8vZT8RyFV5SHpFFCasATSOKGDsBuYSydOjnWKto8xMuJXWfsgfqmQkvQuhiWBZrxhK4X8oHA_-Eo93Gj1V7jltu2BxAo8frd9e90is4rD790rdeialyPA7nAb_EBrGnrkxiAC-p19FiPoymCpD7MMAlzVpOFsl9DQuKnKlHbeymuz39wpQ91PSjZK3KFTWAJPaOvnMxYjLXfOZJ2LfuFi7ZXeaTcCi3J8_iP-AWwCwltdyseehlFXcnewSTjdOpBdQb__Rcg_-MzcOEM8hrzVNSZT2PR9uxFFUT90M0Rm8Nh_QTzsE4qgjBu9USLyh5zR-xQ8s6o3sXeHeNR-xeQeryNYpEoQa81WDtOlx11s-0DH2suHPtDSYz7CJvVwu9uk1Uq1c5-BUG2EOuw-JrL0djY1RIIiJvSZ7sKETvHwRuCgkkA_iw1cv26Y-EbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندۀ قرارگاه عملیاتی شهید سجاد سراوان به شهادت رسید
🔹
قرارگاه قدس نیروی زمینی سپاه: سردار سرتیپ پاسدار حسین ظریفی، فرماندۀ قرارگاه عملیاتی شهید سجاد سراوان، در جریان عملیات مقابله با تروریست‌های مزدور دشمن و در خط مقدم نبرد، جان خویش را در راه امنیت مردم…</div>
<div class="tg-footer">👁️ 649 · <a href="https://t.me/farsna/464484" target="_blank">📅 11:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciQCbl-q4YgrVE1Gw68pLkyUuT6hLn48oxutp3mDZ24s-pbu-5-9vM1Y64te_P5BUNJa6PyFbzhJdYEDjo76DJabgK7p9TgG8SZ8QG5BMF-eTgqy0pizuHCo83XvZ7TQi-wjkngODxIOZxZt0NUfMhD3g04MY9FQxw3_td0CE47sZF_0Cz-3c9iPUz0Eh_xpxaJUZpPZuUbaMj_w17bhRvDOEiqx93zIZ8UP2R3hwMTDdwWUTYP1dNaHZ09J4l3-MzpHsc3Gv6x3eGBumDQekcLQiO3ZSbefM1dolGJL9Aa1d7cxj9NGeRJS7VjS7ZcymPhQ7h9NZIAI4C05p4yD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرق آسیا بی‌توجه به تحریم‌های هوایی علیه ایران
🔹
مدیرعامل شهر فرودگاهی امام خمینی(ره) اعلام کرد که  پروازهای به شرق آسیا از جمله چین، ویتنام و مالزی برقرار است.
🔹
مسئولان هوایی می‌گویند که ایرلاین‌های ایرانی در حال مذاکره برای باز کردن مسیرهای جدید هوایی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/farsna/464483" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464479">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723913721e.mp4?token=nD1tWVA9PgfjvfCwyQ7_JSAPqWfc2qh6rZNKmEZxGidd89Ss1b3SpX8NV1rODAFk84c7YNQitntSANoXqYG76w2U3b97sy5fystPuA-RH8tI6jpuLPXDZgIvlN0VkDfNvYCFaEriG6kYRjZ7Ac9_JyPiWUkukruFmRf_XXhJ_audGklMUdEQq20mUKHRXe5MHPHTsaTyR7-5mocejPIQ5SveF1Q-WXkZb_H5F5U6AfKo_zjAl_43VuVsUdE_I-XKuz5e-tEd-elFyZ46al37kFWSBpW59Ho1vW3ZVmXISQvM4CNFqGdWyeIAibLv9yEprLWc9grFz0K9Byy8VC7Fow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723913721e.mp4?token=nD1tWVA9PgfjvfCwyQ7_JSAPqWfc2qh6rZNKmEZxGidd89Ss1b3SpX8NV1rODAFk84c7YNQitntSANoXqYG76w2U3b97sy5fystPuA-RH8tI6jpuLPXDZgIvlN0VkDfNvYCFaEriG6kYRjZ7Ac9_JyPiWUkukruFmRf_XXhJ_audGklMUdEQq20mUKHRXe5MHPHTsaTyR7-5mocejPIQ5SveF1Q-WXkZb_H5F5U6AfKo_zjAl_43VuVsUdE_I-XKuz5e-tEd-elFyZ46al37kFWSBpW59Ho1vW3ZVmXISQvM4CNFqGdWyeIAibLv9yEprLWc9grFz0K9Byy8VC7Fow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های تایلند زیر آب رفت و ده‌ها هزار نفر گرفتار سیلاب شدند
🔹
بارش پیوستهٔ باران از عصر پنجشنبه تا صبح امروز در پایتخت تایلند، موجب آب‌گرفتگی جاده‌ها و تخلیهٔ اجباری برخی ساکنان شد.
🔹
براساس اعلام دولت تایلند، تا امروز بیش از ۸۴ هزار نفر در ۲۱ استان این کشور، به‌ویژه در مناطق مرکزی، تحت‌تأثیر سیل و آبگرفتگی قرار گرفته است.
🔹
تصاویر و فیلم‌های منتشرشده از این حادثه، بزرگراه‌های اصلی بانکوک را زیر آب نشان می‌دهد و رانندگان به‌دلیل بالاآمدن آب ناچار به رهاکردن خودروهای خود شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/farsna/464479" target="_blank">📅 11:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464478">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akrPeH7neXHCccYQU_-girRf9NsoFgKSE28W9O4xmHV8mozeDV95-SjDq8eWVBew6zb3oCSiyXzRVln30nsP1OFEU4sjXqVyDyt_U2Qw6KAuEMk4bwGUbOzcKVoHabxQIWvyW3bO96CpUuRDPKboiNvRIqEragtw2tT_8WqAik4cj8O6t-38Qh-7i1ZfzI-jXDESmmy_MAHgebJmFG9DbmIM3ZlKIzc2jcRclCESsNAzSaHP8kylWIa7ZDEt4XtozOrdFBginlmoB5RBPhS2XheK0d_cGMcp4-Z2a1vDzaIWrxc8xeFqYXcJG5TyuxdBJ1iD-j9jJQtw9AWMRhWl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیدان رئال را شوکه کرد
⚽️
«وضعیت امباپه خوب نیست؛ باید به مادرید برگردد»، این اظهارات تلخ سرمربی فرانسه بعد از مصدومیت ستارۀ رئال است.
⚽️
دیدار فرانسه و ترکیه دیشب برگزار شد. امباپه گل پیروزی تیمش را به ثمر رساند اما بعد از گلزنی مصدوم شد.
⚽️
فدراسیون فوتبال فرانسه اعلام کرده امباپه از ناحیۀ تاندون زانو مصدوم شده و بازی‌های فیفادی را از دست می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/farsna/464478" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464471">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSDUxNx3uc-ioKQh0hJD-4Xrcf9CGHmvys22wUWZsI6X5QC2NO6UNqjSna9FLN_XJIeghcMKbOVbBsZ3fVHsTFZndAd9F7WP0Cbi52595Yd68Nr7QO7gyoi5K7HyPzo0o9Qxhx1NYFy-aHS3K-cpUH9RFKkVDE7TbqMj77oFG_D3x5v-udSLLTtUBmV4SiEQIrDcW4oL30_wqeB0e_1zT83SOAFP3kb3X6pmgMZX3TAlpfQIvU2CUzolSgsvPaocEexPsRMLzhLPX84WsG_yoFlZrBLm8E11qszuc1eabCJkutjMbAi72Vhdo4T5mvR2ozxHSZU5XYZu70jAls0rSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvfACsnrxyzc2uc9I3cD6u0Om9bV-aHLV4Sg2aT9b2Rg9oHrvJ6fv3cBnj4zvlPYiDFyXHPqkzEGaB-tEz9GV6YzUlbQF27EINo6evbYQDPLYvU664Brjt8rL69BhkENMtVJtjDJZcaqvepIYzFEjOC2VbuGu9eNhRyFD74nK593KqZfXFdfeRnlIOS3bwZOi_-Bf2EfLj8f08ZBT-nLMjTZgNAlzeDt-7BJ3tsX_CfBhnP8VN-OSck39zuH6CBbsQQ4QwVQj2FVlc-HSsKPKVOcgMhWNE73lGgYMH2OPa16M-pgkuWJHAVtcsY_zXvogCLZ6wZHSU9aX-YyzUuXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_uJOsBTIIsh5ELUekILodiwc9PvUmt-6hAAbyKouNNTtFF0UuRk3SGMV_KizyCA2G1k-e7izYZ9BUjfCh4wz0dFgv6vXe0lqKmECtVbCWk15rs1-Uz7iDgaPCX6kdReRQxdwee93VCtsfF0uQYXsfwJl4IMBH-kfYJ6EWLy-TIwnc-oPoq22p6fbdX9I-47jkvACEUDrL2U9og10iML6ztlbUL9LAM0ROk3gWCEX-QGQOfc1HKUNw149sdLciAw7fIhZrcWQDyXpV6xU2m7aT6t4fGDsmDU7p9heuXfcFLuEScTcTUusJ_Y2EprIPYFBFe8TYsSJLe37Z6oq3EqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfw511SJl_9vAg5sHjxEeFiRI9jgWh7dzVAUs7fM7LAlDjQ30v6Y9COeKqPKFz1z64ld4C88Tz-pG00b-CMqGFYJ95JRW2zRgmTkrJisZTPrdaN6vqFXoEMCyNBaY_OCsIhU1CVkRLQC1WRWgXADOjRfhTv_KSTy-RzZDVvry18o3LGemTcvUKgDoHLdd5q0auerlMDSQuXq8wNpuwTXDTF3m308PMOj9KM1UNn0F99K37jkuGEU0XEJmtIGy0vVZkD-kY43B7Bhu_EEnU52IiRRTF6J2tN8qSATgf5XPby48xEo2aNY2gNBrpCKNCkEQ6M0UKuxhuJSw6dg9hU1fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4CwSyfIBdFe5jdLkyz7b23DWGwd2BeM0oAet3eheFcavolAT7EFO_d_4t6RqqzLWDTLLXpuxskwXOBxJM9AhhJP5ruD1iItC7X8O5C-9JghJyqRhoGw64vUyi9iFOyZJuViULFvldv4LDGw0IE_gtAoDfdS81dpm8E3AQvXyI8-_yI4DdzZRuxCiG1s61-KGIsQlGHU9yR6EsNx8-C45MaMEFDcazqSeITtDUujo9E-z5MsBbcOFQeyDvZMgHtO_8HxtQ3iI64GifaMBhQvk2TuSmgjG6ZYerZuPt2S89EfTTTDqHsLehRZPjtB-zUYKRcFi0V-uwOdjRF-VBHf6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtLP6d7Xe04nGjb09CASCFu8BwMW9D6sToeTHpiKmZazxdu2dPqylfwdexjrm3IoN0qVMUEcv2mAFVYaEyCsZfdrhxIOVI83_zXk2FHpAvXQSUIvK1Dze55Vx43t324TGLzJ2NDJ-_w5GYp637Vf-kFz5SKbGEOwKagpoz_Uar8NXzQQvo3xo9LpypMMl-rozpMr3r4sMrHrMqUE0jfO_31bkxO_75G5sRp66daqjipEm4XtGYbtl_uEt_YpdxMJozYwkvTqurnAe3vvC4UHuNw5Yz_vBbqKhIaDXDIIUGNZAwLDG_W9KV049YGyQoezaME9lSS2Xb2KfbFGmsz1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6ncRX2hieGZxFj4ConSUsQWrnQ2G3xlw3M0r0QYhhaGhL1qRavaP2z2-NW8nougbsoxmeuUL-rV2Lg7-WtR0EoatG0e2ByRTpSK6t6alLElQJXFq03lNUR1BzJyF4R_j4yMghTRVrl04hhg8nNgtzO4wLw9xg-0kndASAFp6WWHDGtZv-De75VIqic7vPJTsk4K53k9ngLX4zO5EpImeWzkeTL5rAxJ9U2X_dM38xKtAdx07SbkMggJJIhJyaxvrHgIpls_Avnv_rTjiwkRiDozHC2OZ5f7Yk3T07LX_rgaKvJ7MZ43EWwOkzruM_2RAOEhfepOSimpC6XpCImrCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
از بمب سنگرشکن GBU_27 تا شاهد و رعد
🔸
در باغ‌موزهٔ دفاع مقدس زنجان، آثاری از جنگ‌های ۸ سال دفاع مقدس تا دفاع مقدس ۱۲ روزه و دفاع مقدس ۴۰ روزه، از جمله بمب GBU-27 سنگرشکن و تجهیزات شاهد و رعد، به نمایش گذاشته شده است.
عکس:
عرفان تقی بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/464471" target="_blank">📅 11:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464470">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKamd9FdqjwqgYVF4RNHN5noiNzaTIfVsbY-fQ0CEd_QdT3pxjbrSUfq3TYp4KgIeNe2u_I_d9lnENNL3E9cKU1PaJnMd1nICmNfyrIKHwFoJC4m4mRaDSbf5LO0aFcdboSL2Vv3rEdPY-LgQuloba75RbEXAol-C86d0Ot9_yP03lRbA_4j0CbVM843m0FQZ-BYS-UyPXRvec5Jc8qLrHcvqEaKwrp4RdR2fNaF233wg_cnHHWtSRkeWpC7I4aq0SPiXDWhsJ2R2XAB3tmb8Pqsrr8ASxLp5EbHAXrN4BkCtC2ufe2cV3UN6eVv3yvjQa_S1_ObOsvw7gaX_HvTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانواها گران‌فروش‌تر شدند
🔹
با وجود هشدارهای مسئولان به پایبندی نانوایان به رعایت قیمت،‌ بنابر اعلام سازمان حمایت، شهریور ماه، آن‌ها بیشترین تخلف را بین اصناف داشتند که گران‌فروشی در صدر این تخلفات قرار داشت.
🔹
۲ ماه پیش بود که دولت قیمت انواع نان را در پی اعتراضات نانوایان ۷۰ درصد گران کرد؛ با این‌شرط که قیمت را رعایت و کیفیت نان را بهتر کنند.
🔹
حال شهروندان از گرانی و بی کیفیتی نان می‌گویند، یک شهروند تهرانی می‌گوید که قیمت نان سنگک دولتی در یک نانوایی ۱۷۵۰۰ تومان در دیگری ۲۰ هزار تومان است، آنها مالیات را هم از مردم می‌گیرند.
🔹
یک مشتری دیگر می‌گوید که تعداد  دولتی پزها نسبت به آزادپزها بسیار کم است و مردم را عملا به سمت خرید نان گران‌تر سوق می‌دهند، اصلا در آزادپزها هم قاعده و اصول ندارد،‌ سنگک تا ۵۰ هزار تومان می‌فروشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/464470" target="_blank">📅 11:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464469">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=Wj7pfTtOWuCWgGQmT7WzvX6tzqBHeFGBOrVead3s1wgXIYyDivvFwH8Vb_MiFViaoJXmN2vtXe_Q_qtqAZUnwq8c3dQ14KNw226V2ep05b2mWu4bi4cDnUhgIGUBLOSdwr-iaNsgDL2LcLGYlcR8KQfMvLRFOE8jVBHAsPjPBh7ygOaqJ4bBquZoKo3GANXuf1yV2no_HG7a9XP4I8GneENp2-j_N2zy7vHEj1hQPTcSIBmAWklbRbzQKzA1Ht5wUzyoc4zTqwggaEn3eGOtViLS50f-PvkqSVDovSWX3OAXk-1o5Op6lAOMsWfO5H0Yx8zy1yEokfZZtOgxvrBdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e28283e6b.mp4?token=Wj7pfTtOWuCWgGQmT7WzvX6tzqBHeFGBOrVead3s1wgXIYyDivvFwH8Vb_MiFViaoJXmN2vtXe_Q_qtqAZUnwq8c3dQ14KNw226V2ep05b2mWu4bi4cDnUhgIGUBLOSdwr-iaNsgDL2LcLGYlcR8KQfMvLRFOE8jVBHAsPjPBh7ygOaqJ4bBquZoKo3GANXuf1yV2no_HG7a9XP4I8GneENp2-j_N2zy7vHEj1hQPTcSIBmAWklbRbzQKzA1Ht5wUzyoc4zTqwggaEn3eGOtViLS50f-PvkqSVDovSWX3OAXk-1o5Op6lAOMsWfO5H0Yx8zy1yEokfZZtOgxvrBdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تکمیلی: ۹ فوتی و ۵ مصدوم در برخورد اتوبوس و تریلی حمل میلگرد در محور بیرجند
🔹
هلال‌احمر خراسان جنوبی: شمار کشته‌شدگان و مصدومان حادثۀ آتش‌سوزی ناشی از برخورد اتوبوس با تریلی، به ۹ فوتی و ۵ مصدوم افزایش یافت.
🔸
این اتوبوس از مشهد به مقصد زابل، و تریلی حامل…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/464469" target="_blank">📅 10:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464468">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=CZdVB_o4s2G_YnSZSP8r4yo256aQPw2pI50Kcuja-UEV0FtxI3X50cTxM8CoT5PZtzDSqmyI3sMFvnCUN4parUGUmicGEcRR7ROeObc7t1UnhQ4zzBSAErVtoN0A6hgDgoGrQFwOwWNRBQO_nSMDmKT1Whpj86TubLQvLA8GV1zUD1cd87-CcIK4Vw_8mLtiLWiE--sSf-XUHR8e4lCxTjWwar6IufjeP2yAYYZ7Nqzbpiz7TrQUfTtn-1ENUAcyYFb8PdZW1ZbJXZyw3pLKRUqBOZ3IJRa11pXcz6gQOQxBtQUdFw5LOoXVxxgGrry3i_YI_xDwEQj5GjC-eKsKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18fa6d3c9f.mp4?token=CZdVB_o4s2G_YnSZSP8r4yo256aQPw2pI50Kcuja-UEV0FtxI3X50cTxM8CoT5PZtzDSqmyI3sMFvnCUN4parUGUmicGEcRR7ROeObc7t1UnhQ4zzBSAErVtoN0A6hgDgoGrQFwOwWNRBQO_nSMDmKT1Whpj86TubLQvLA8GV1zUD1cd87-CcIK4Vw_8mLtiLWiE--sSf-XUHR8e4lCxTjWwar6IufjeP2yAYYZ7Nqzbpiz7TrQUfTtn-1ENUAcyYFb8PdZW1ZbJXZyw3pLKRUqBOZ3IJRa11pXcz6gQOQxBtQUdFw5LOoXVxxgGrry3i_YI_xDwEQj5GjC-eKsKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ پزشکیان: در دیدار با رهبر انقلاب ۷ ساعت روی زمین نشسته بودیم و گفت‌گو می‌کردیم
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ خبری سی‌بی‌اس: در دیدار ۷ ساعته که خدمت رهبر معظم انقلاب بودم، ایشان هیچ جراحتی نداشت.
🔹
ما روی زمین نشسته بودیم و گفت‌گو می‌کردیم، ما چون عادت…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/464468" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL-5RQPaF9ivvPDYx0PQmiADEORG_I_JyJFPii1cXjR3weWJ74AosoSJwjVqavcBTQjRTUqtTCy-sY176yBIv6WD7hnFod5mRCh1hgpIpCvsTZoSszUfOrfmF8MZ9rVI7IlZFYs4RtWYIjjxQW7kX7YDM2uIY98ih2RBe5QBMWm3jsHQTME7NIpQ3kbWcOkLF3jMEhGGyiAytQ6adIFIfwC-yPAIwcewkAoxVUtT54UgsXRCIVSZxyND3tyfuOh1EOEM1JHn69akgOHX6KI_BQ-AFKzt3TNfzWuM16LTxrDaZsytBiirV08BsBJsFBsW32Ckpr5aGn0a6AScwr3ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیرو دریایی سپاه: اگر تنگۀ هرمز در اختیار آمریکاست، بسم‌الله!
🔹
معاون سیاسی نیروی دریایی سپاه: ترامپ در فضاسازی رسانه‌ای خود مدعی شده که تنگۀ هرمز در اختیار آمریکاست؛ اگر چنین است، بسم‌الله. یکی از ناوهای خود را به فاصلۀ ۱۰۰ کیلومتری نزدیک کنید.
🔹
آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/464467" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnABBPVzlvRvCOWmoiSLfcEZakqUYb_rg1xD-sExVHYCus0xrpXi_corGIEjQLbkLa8R_19LsPJ495HSssZhgpplVeXSI6e7s6xIfqtljltM6JULyva3EFyI9a9exdFD8jyNiADjYvHeWhtzrLHdyxxdm6zj_sx_s9DLH-giqsjWZmDWlyao4GpKmAswrI38MLjdWkpole6RVcoyrtjtC59QkWfhbclD7O5g-OuEzoNMgOYRhjiIQu8-hTP1uj6QBfgkwliIGj6qFR_t6M05TrWc-sgLnpU41sn9T0dJdmzuCHRTA8szAfw2dnk316WZS4pHLzeVv-KFZdsOmKqEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش بغداد برای حفظ مسیر پروازی ایران شروع شد
🔹
دولت عراق برای از سرگیری پروازهای ایران، با آمریکا وارد مذاکره شد تا فرودگاه‌های این کشور از تحریم‌ها کنار گذاشته شوند.
🔹
بر اساس بیانیهٔ دفتر رسانه‌ای نخست‌وزیر عراق، هدف از این گفت‌وگو «فراهم شدن امکان از سرگیری پروازها به دلایل انسانی، شامل درمان، تحصیل، زیارت‌های دینی و منافع غیرنظامیان» عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/464466" target="_blank">📅 10:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464465">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTOb9zir82UBV2SfNYiuNKF3QXCy8D10aJ2XZfwdsYddncWGr0W1CWmX0OZO_3yXZheSbEtvDgQ98ux8Sk5IaIxpffwjfiX2coREoGXOhZO44VVhYdVC36P7HKd3lOu7kxiFa650i9BFw7UL8FXYxXppO-iVXXPLJV7iY9UfH-m1o4YCZdF9paUpCJr_NeisTuz62T49MCCl0tRdUhKAtfiYwcTdd02AeAlRCGAv9_Uyi_enLFuxkyu7ToXdrVI4OcuEv1-UhTVTiWgLV22a6oDH3tHxDda9_GayvuLDy1g4CcQyYzZ4LdftMdAqTmjcqB_4vQcVUjT7ntvi0Yx-7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: سرباز جوان ایرانی جان‌فدای ناموس و وطن شد
🔹
پیام رئیس ستادکل نیروهای مسلح به‌مناسبت روز سرباز: سربازان عزیز با شجاعتی کم‌نظیر در میدان نبرد جنگ تحمیلی دوم و سوم حاضر شدند و با تقدیم جان خود، از جان و مال و ناموس ملت، آرمان‌های بلند انقلاب اسلامی و میهن عزیز دفاع کردند.
🔹
حضور مؤثر و مقتدرانه جوانان سرباز، موجب ارتقاء چشمگیر توان دفاعی، امنیتی و انتظامی کشور و افزایش عمق بازدارندگی ملی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/464465" target="_blank">📅 10:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3c43e28a.mp4?token=USUc9nwR6rubl1E7_v_XdBb7-2AfcpxpkjvzuvUrlJONjrM4F473xvBsg-qZV2d2IaFX7FPhEx-v4dJwn5BzaTSLfB4gU1Wallm7EaoneL7YlbDtO4U0Vt_KF9I6KcyJpMMcjysbbEzbNQ_igqlZb-55LCFXrj8-UIV2z5AmPRD210rNw5wpJedsJy0nlLvuPrggJTIHQcwBwEzpsX8zBmqSB7kOEi3tAtTxANKCzo-XeiD7bVJT2Jh2dStlAuVBYrpItFMEOeyXH4kYo1P_Juc-azLTFsFOIalmUrlcbWjeAD1cB-Kh5mujxw2CTlqWWN7uy7NxTftk06v2-rttJIqmvcQ4vJWJYrNHrDJ1vpD2ENPNJgNEJksRiXOl1CoqfXS-oljdT7OtU6etPDCJz0HGKEhQzICypsMgLwEEXh5nyZmLybk0hjitxAiUgZoj35Plllu5lLNwvybpHFoZYs1kGTkt52-8nZ34YhklZKC2gRmM48EZPC_AjVuBqpuPJ4ZFKKlE9bZ8wcwDE-3xXcQ22wRICe9mktAmOdsbB6fDMfThCBw7gnv0-_UaPWj0dFEMsNUy5h4_48gu3qdG_It9pStKRWlHHrylAtBsXW_UquQwBHziRbveL_Uz54vIExRmb8yM1BUybbHG1zTZEgHH4T4Eu1SRUaJorWZd7tE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3c43e28a.mp4?token=USUc9nwR6rubl1E7_v_XdBb7-2AfcpxpkjvzuvUrlJONjrM4F473xvBsg-qZV2d2IaFX7FPhEx-v4dJwn5BzaTSLfB4gU1Wallm7EaoneL7YlbDtO4U0Vt_KF9I6KcyJpMMcjysbbEzbNQ_igqlZb-55LCFXrj8-UIV2z5AmPRD210rNw5wpJedsJy0nlLvuPrggJTIHQcwBwEzpsX8zBmqSB7kOEi3tAtTxANKCzo-XeiD7bVJT2Jh2dStlAuVBYrpItFMEOeyXH4kYo1P_Juc-azLTFsFOIalmUrlcbWjeAD1cB-Kh5mujxw2CTlqWWN7uy7NxTftk06v2-rttJIqmvcQ4vJWJYrNHrDJ1vpD2ENPNJgNEJksRiXOl1CoqfXS-oljdT7OtU6etPDCJz0HGKEhQzICypsMgLwEEXh5nyZmLybk0hjitxAiUgZoj35Plllu5lLNwvybpHFoZYs1kGTkt52-8nZ34YhklZKC2gRmM48EZPC_AjVuBqpuPJ4ZFKKlE9bZ8wcwDE-3xXcQ22wRICe9mktAmOdsbB6fDMfThCBw7gnv0-_UaPWj0dFEMsNUy5h4_48gu3qdG_It9pStKRWlHHrylAtBsXW_UquQwBHziRbveL_Uz54vIExRmb8yM1BUybbHG1zTZEgHH4T4Eu1SRUaJorWZd7tE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌بازی مردها از روزهای سربازی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/464464" target="_blank">📅 10:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پزشکیان: آمادۀ گفت‌وگو هستیم، اما قلدری را نمی‌پذیریم
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ خبری سی‌بی‌اس: ما هیچ‌گاه به‌دنبال سلاح هسته‌ای نبودیم. آنها رهبری را شهید کردند که براساس فتوای ایشان، ساخت سلاح هسته‌ای حرام است.
🔹
از نظر اعتقادی و نه از نظر قانونی، بدین…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/464463" target="_blank">📅 10:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMf9i4Z3b3bPh7emeZcCclBskXMYXFE_PYfa98donRQHvHJKxSOJ8FVUPtwz_c8jCdCiPcU7tmqoj8o0PaQDV-wusE7AfFfuWuWrG3UB1IjitL8PbwEyf6hMO-nISKCJJry35s8K5HWht4p9XK_q3MrDJHLSPSMTKCuiQf9huzNt1Zuv12Ro-U3U0N6blEdpIYZbK7ezUXrPzZdxSG_3C0Uz5HhPWvBbWwNvbFg6snQ3wSMFvStPYWe6BXulf8sTyaEBTrbvniTyN02JIXXoQvmktX0Hju-xXMCh5WoWsOL1HiakBrMwCQLuDjKzFyWDmYk-KI2x-khTonXJCy6TAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعیت افت صادرات نفت ایران به چین
🔹
بررسی روند صادرات نفت ایران به چین نشان می‌دهد حجم محموله‌های نفتی ایران در آب‌های نزدیک به چین کاهش قابل‌توجهی داشته و موجودی نفت ایران روی آب در این منطقه به حدود ۲۰ میلیون بشکه رسیده است.
🔹
بر همین اساس، میزان واردات نفت ایران از سوی چین که در مقاطعی بین یک تا ۱.۵ میلیون بشکه در روز برآورد می‌شد، اکنون در برخی محاسبات به کمتر از ۱۰۰ هزار بشکه در روز رسیده است.
🔹
کاهشی که می‌تواند بیش از آن‌که ناشی از افت تقاضای چین باشد، به کاهش عرضه و تغییر الگوی فروش نفت ایران مربوط باشد.
🔹
باتوجه به تغییر مسیرهای انتقال، شیوه عرضه و آرایش فروش نفت ایران پس از جنگ، به‌دلیل مشخص نبودن کامل این «آرایش جنگی»، امکان استخراج رقم دقیق صادرات وجود ندارد.
🔹
درآمدهای نفتی دولت هم نشان می‌دهد بیش از ۱۰۰ درصد منابع پیش‌بینی‌شده در بودجهٔ ۱۴۰۵ در نیمهٔ اول سال محقق شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/464462" target="_blank">📅 10:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVtszxlFhdtAWC5ZOsr6fdyjp0E0EDKxiFmFmjMEIF1i-F9nLkoQd_VyyyQ89pHVDNtczt7637Al3bi6uDahH2PX3_2bTjQ9ai0W_APUc4txQlzOI7Mgcgw--1Tj3Z4ZESai_xBv7VvvED20JQbZ8XyUETbM7S4h5eARh-_GPtVcV7n3WoFsd7gV7PFpKu7ojYG1uWPX-7tIC2jWJW6XPvqy4GKMFr9xVDf6MQtaoJzneJR6yCsh2toFhVvDOrrx8BiSNWr19BoujyJBkKQwA5x9V7OmE3CeIp2Ky2rzsfJojVvFPIUPo9vYGrpcCitcLhtWhPClInGUWvmsi0b_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔶
شستا پیشرو در سرمایه‌گذاری و خلق ارزش در اقتصاد ایران
در میان ۲۷ هلدینگ بورسی کشور به لحاظ شاخص بازدهی از ابتدای امسال تاکنون، عملکرد شستا و هلدینگهای زیرمجموعه افتخارآفرین است.
@tappico1381</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/464461" target="_blank">📅 10:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2fMNeK1qwHubgLhfjLmK44UxQ3tckMccxrD4j-j6YjM3dRjH1rDO-XHfRmTGVOmPB0rJm7O3iwfGBzOF6FmU_oUKY9hfR2iHCci5icV5WeyW9s0gB1mksQpSiI3Ml42zmXhDWf5i3LeKx-_-VaaGqxa6v8cQPNG14MlUBmAzgIqADG9sLSY8Ud9HmTwNl2Sux9xaNonrmd5CFNdYlV-7o5L4on5ymdUX9RlDs29aOhmSr6XUvxteBqtrnQtx0i8iTl7p-y8ZQzWmwjvKL3X3fhj8NFxvUmso1DijFjbDxHnBLpg8ZHVGXsKdlq30vh5dXE4JNbt09qJsaFABpGNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/464460" target="_blank">📅 10:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464459">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/464459" target="_blank">📅 10:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464458">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK7V6d2KmhwqWSwWbG0_nb078NV0wf3CUCdgzV0yUKA6zzQy4BEY3ryS75YbDb3OvwEHEUty5Zn6ojtD-CKornC-avxjGOe2jon2Hrlw90FFpUpDTmNN35AzC0MVztgwRnLMBg_4CXzPUr7Su7y1OKiqDykn2UWP0GzdCpSgo6cxP3tEuFV6QoGtjs18jouXsVS32XRQ0UvAJDknfBnj3fKAoaf44BERTFtsuc10QpSMzL6AMw3iM2dItTzilzKuISo-WmjfZn0e1HEscpVeIcMLkfVIZDCLm-Wf2YfmL8H7jjASYOm7TRZaPkRpn_RuFgxZtnbu9RDTd6TQkOY2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: آمادۀ گفت‌وگو هستیم، اما قلدری را نمی‌پذیریم
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ خبری سی‌بی‌اس: ما هیچ‌گاه به‌دنبال سلاح هسته‌ای نبودیم. آنها رهبری را شهید کردند که براساس فتوای ایشان، ساخت سلاح هسته‌ای حرام است.
🔹
از نظر اعتقادی و نه از نظر قانونی، بدین معنا که حتی اگر در ایران کسانی باشند که انگیزۀ ساخت سلاح هسته‌ای داشته باشند، از نظر اعتقادی حق ندارند به آن طرف حرکت کنند.
🔹
آمریکا این چنین رهبری را ترور کرد، ما در حال گفت‌وگو بودیم، تفاهم کرده بودیم؛ چرا حمله کردند؟ قصد آمریکا این نیست که مشکل حل شود بلکه می‌خواهد حکومت ما را ساقط کند. رهبر اسرائیل در سخنرانی خود می‌گوید قصدش ساقط کردن حکومت است، نه گفت‌وگو.
🔹
ما با تمام وجود گفت‌وگو می‌کنیم، اما قلدری و زوری را نمی‌پذیریم و نمی‌پذیریم که ما را به تسلیم وادار کنند. گفت‌وگو می‌کنیم، اما چرا در حین گفت‌وگو به ما حمله می‌کنند؟
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/464458" target="_blank">📅 09:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464457">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSVaZt7T5jJaqzdrp3ta6MosUZjEsSjddzdA6Q5alYvcMuWbGLBMcfn0f1Uu-Sh82JwKXd-bsp4rTjfGRY2wQmaaivmQO87XzODc9552Dtffs-VQx_TRtstK96bu-M1xs7GVeXFBhZTs2GTbl0whQi7ouUXjm4Ur5JIjuPM6BMw5U4_BYCQWg2BXtzyy7OJ6krEw4D5nJiCA54L5MYdVbbcVxbZOnXRbN4C5q7TymvkzrmT3eTlIj8ezmfnMsSOK7cmqeh-tPK6-we3amQ1-4mptsPB66b7tUElk3swWk6S5y-vPXMkbe9DYPFxS4bO8XP7IkbGdACxOGlZrJEx1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط محاصرۀ‌ دریایی شکست
🔹
«خط محاصرۀ دریایی آمریکا شکسته و عقب‌تر از حالت اولیه رفته». این جمله اکانت Open Source INTelligence با نام مولو مانیتور است.
🔹
طبق اعلام مولومانیتور از ۲۶ روز پیش تاکنون، تصاویر هیچ یک از ناوهای هواپیمابر یو اس اس جورج اچ دبلیو بوش، یو اس اس جورج واشنگتن، یو اس اس باکسر و ناوشکن‌های کلاس آرلی برک، در تصاویر ماهواره‌ای سنتینل-۲ واقع در خط محاصره دریایی ایران یافت نمی‌شود.
🔹
براساس این اطلاعات، آمریکا تصمیم گرفته تا خارج شدن از تیررس موشک‌های ضد کشتی ایران عقب‌نشینی کند و بدین ترتیب خط محاصرۀ دریایی را که تا یک ماه پیش در خروجی خلیج عمان قرار داشت تغییر دهد.
🔸
حدود ۲۶ روز پیش اوایل ماه سپتامبر، نیروی دریایی ایران برای اولین بار موشک قاسم بصیر را آزمایش کرد که تمام دریای عرب در برد آن قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/464457" target="_blank">📅 09:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اکسپو ۲۰۲۶ گرگان؛ فرصت توسعه یا نمایش بزرگ اقتصادی؟
🔹
برگزاری رویداد اکسپو ۲۰۲۶ آسیای میانه در گرگان می‌تواند فرصتی برای تقویت ارتباطات اقتصادی گلستان با کشورهای آسیای میانه باشد؛ اما تحقق این ظرفیت نیازمند زیرساخت، برنامهٔ راهبردی و تعریف دقیق اهداف اقتصادی است.
🔹
کارشناسان معتقدند صرف گردهم‌آوردن تجار و معرفی محصولات صادراتی آن هم با هزینه‌های گزاف کافی نیست و باید مشخص شود تفاهم‌های تجاری پس‌از نمایشگاه در چه بستری به قرارداد و سرمایه‌گذاری تبدیل می‌شود. همچنین موضوعاتی مانند حمل‌ونقل، گمرک، استانداردها و زنجیرهٔ تأمین باید از پیش تعیین‌تکلیف شوند.
🔹
از سوی دیگر، گلستان و استان‌های شمالی باید از رویکرد صرفاً صادراتی عبور و به‌سمت ایجاد صنایع تبدیلی و چندملیتی، تشکیل زنجیره‌های ارزش منطقه‌ای و نقش‌آفرینی در امنیت غذایی کشورهای آسیای میانه حرکت کنند؛ در غیر این صورت، خطر آن وجود دارد که دستاوردهای اکسپو به چند تفاهم‌نامه و نمایش محصولات محدود شود.
🔹
اکنون پرسش اصلی این است که «آیا اکسپو ۲۰۲۶ می‌تواند به بستری برای سرمایه‌گذاری، تولید مشترک و توسعه پایدار اقتصادی گلستان تبدیل شود یا صرفاً به رویدادی پرزرق‌وبرق برای میزبانی از تجار خارجی بدل خواهد شد؟»
🔸
این رویداد قرار است ۲۴ تا ۲۷ آذر در نمایشگاه‌های بین‌المللی گرگان برگزار شود.
🔗
مشروح این گزارش را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/464456" target="_blank">📅 09:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZY4bmjTXw9DxO6JaDFcRVgfrRR64CZVyg0uOXXxKVBa80P1qFwsfosx6ucJLcOy3R780uezhmjw4a-VIQb0AJYugS93uf5HDGdxCGhpZIW53sRy65rrTbyyaEbo0HqolCozo71gihHzJi-NE2aDXatJXp2JxOg5re57AoeOckFnIRDGzHEYu24knkjhaWrpLvQkKatOAaG9N_gZ6Adsyu3eH98YyfUR8C-lTlbJARMwJ1d8HgbN8ECi1donP_VHAiC0F52CHuOVPArnZLveoLElu_2MeZ2tC0OnWRoFsUXQD2jSQTw-F09uwFkI1d-6Xj9lEcjKUUTLXu7rUGHRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اثر واژگونی یک دستگاه اتوبوس در مسیر همدان به ساوه، ۱۱ نفر فوت کردند و ۲۴ نفر مصدوم شدند.
🔹
پلیس‌راه استان مرکزی علت واژگونی را «خواب‌آلودگی راننده» اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/464455" target="_blank">📅 09:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boSHPOL19UAltQJU9QAQODoqUuQMKBzQZLTzNOr5XycI5yKW3h-GRH1KQLGBWpkM8b4ADVz8bT1eX7H9hDVQVzyd32-Qb47vt0hIG-xzhB_cJuJ7vGuRiYzWIZx-eAabr8s45mwcDpp8WwYQchbyhyKXMQh4XjPxAEYAv9dRCSyTD6EXKZoGliaEfN1AStfpJkoyiOsl-wnloiDRgLqCkBg0VpnbJ2u-B-0_N_FQCKoXy04JMCiADM-3FHtKqS8KACvavtNwMShu1qUdrijDJ2vR2xQViT3-xLfpZ7ioP84bSTh7ApYrCEJlXf4SVpYwAINZZhpOZPbTxz98RuiOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختران کبدی ایران فینالیست شدند
🔹
تیم کبدی زنان در مرحلهٔ نیمه‌نهایی مقابل چین تایپه با نتیجهٔ ۲۳ بر ۱۹ پیروز شد و راهی فینال شد. @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/464454" target="_blank">📅 09:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6660dc271d.mp4?token=tHsb3FC7AcZq7c7bvrb7DngIdXVomh7yGOggmzk_CqFNKTlI3gApT0_vxGVF_9TyFSj4auT0wEwHYSi0q1Y3Ys8arNld6o1UHWexZcWXI7zfUIFERYI26AJKR1Xh_ClBc4VJeoCtmsEeSD4XN3PaKA_iMOl4XASNGKqp6V6lcMSQ2vPrVCUl2FdDp2kTjf8E_HUcsrLtDWOS1C1fLaKXMpTpIOhg4eduS2SVjtxKF7oZD0kZ54rbOOpS-De7wCpihd61AO_e0OPsnVpPc-gkVeUAGnQpS6vomv7Hu3jY1mfCU8THzWSz30Hzls3sbN8Bug0T2ULR9G3f_GrBKS_uWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6660dc271d.mp4?token=tHsb3FC7AcZq7c7bvrb7DngIdXVomh7yGOggmzk_CqFNKTlI3gApT0_vxGVF_9TyFSj4auT0wEwHYSi0q1Y3Ys8arNld6o1UHWexZcWXI7zfUIFERYI26AJKR1Xh_ClBc4VJeoCtmsEeSD4XN3PaKA_iMOl4XASNGKqp6V6lcMSQ2vPrVCUl2FdDp2kTjf8E_HUcsrLtDWOS1C1fLaKXMpTpIOhg4eduS2SVjtxKF7oZD0kZ54rbOOpS-De7wCpihd61AO_e0OPsnVpPc-gkVeUAGnQpS6vomv7Hu3jY1mfCU8THzWSz30Hzls3sbN8Bug0T2ULR9G3f_GrBKS_uWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آدم‌هایی که خوب می‌خوابند ممکن است آلزایمر نگیرند!
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/464453" target="_blank">📅 08:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئیس‌جمهور به نیویورک سفر کرد
🔹
پزشکیان صبح امروز برای حضور در هشتادویکمین مجمع عمومی سازمان ملل متحد، تهران را به مقصد نیویورک ترک کرد.
🔹
براساس برنامۀ اعلام‌شده، سفر پزشکیان به نیویورک تا شنبه ادامه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/464452" target="_blank">📅 08:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464451">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مذاکره با آمریکا و الفبای سیاست برای آنهایی که خائن نیستند
📝
شش گزاره که برای فهمیدن‌شان نه دکترای علوم سیاسی لازم است، نه تجربه دیپلماسی!
🔹
گاهی یک مسئله آن‌قدر ساده است که توضیح‌دادنش دشوار می‌شود؛ چون آدم نمی‌داند از کدام بدیهیات باید شروع کند؛ اما ظاهراً باید شروع کرد.
🔸
یک؛ اگر کسی با شما مذاکره کرد و وسط مذاکره به شما حمله کرد، یعنی «مذاکره» به‌تنهایی مانع حمله نمی‌شود.
🔹
ساده بود؟ یک بار دیگر: مذاکره کردید؛ گفتید آماده توافق هستید. حتی گفتید حاضرید در موضوع هسته‌ای عقب‌نشینی کنید و از ۴۰۰ کیلو اورانیوم صرف‌نظر کنید.
🔹
بعد به شما حمله شد. نتیجه خیلی پیچیده نیست؛ صرف مذاکره جلوی حمله را نگرفت.
برای فهم این جمله نیازی به نظریه روابط بین‌الملل نیست.
🔹
دو؛ اگر طرف مقابل با فشار از شما امتیاز بگیرد، ممکن است دوباره فشار بیاورد.
🔹
مثلاً طرف مقابل فشار می‌آورد. شما می‌گویید برای اینکه دعوا نشود، امتیاز می‌دهیم. او می‌بیند فشار جواب داد.
🔹
حالا سؤال کلاس اول سیاست؛ دفعه بعد احتمالاً چه می‌کند؟ می‌گوید چه انسان‌های خوبی؛ دیگر فشار نمی‌آورم. یا دوباره فشار می‌آورد تا دوباره امتیاز بگیرد؟ سؤال سختی نیست.
🔸
سه؛ اگر کسی از شما می‌ترسد، باید کاری کنید بیشتر از حمله بترسد؛ نه اینکه بفهمد شما بیشتر از او از جنگ می‌ترسید.
🔹
خیلی ساده: اگر دشمن بفهمد با ترساندن شما امتیاز می‌گیرد، انگیزه‌اش برای ترساندن شما کمتر نمی‌شود، بیشتر می‌شود.
🔹
چهار؛
صلح خوب است. رفاه هم خوب است. سلامتی هم خوب است. هوای پاک هم خیلی خوب است.
اما سیاست با گفتن چیزهای خوب اداره نمی‌شود.
🔹
وقتی می‌گویید «تفاهم»، باید بگویید سر چه چیزی؟ ما چه می‌دهیم؟ او چه می‌دهد؟ چه تضمینی می‌دهد؟ اگر زیر توافق زد چه می‌شود؟ اگر دوباره حمله کرد چه؟
و مهم‌تر، آخر این امتیازدادن کجاست؟
🔹
اگر جواب این سؤال‌ها را ندارید، هنوز «راه‌حل» ارائه نکرده‌اید.
فقط چند کلمه زیبا گفته‌اید.
🔸
پنج؛ به کسی که درباره نتیجه مذاکره سؤال می‌کند نمی‌شود گفت جنگ‌طلب و بعد مسئله را حل‌شده فرض کرد.
🔹
فرض کنید کسی می‌پرسد «خیلی خوب؛ مذاکره کنیم. اگر دوباره زدند چه؟» پاسخ این نیست: «شما جنگ‌طلبید.»
🔹
می‌پرسد، چه تضمینی داریم؟ پاسخ: شما مخالف صلحید. می‌پرسد: چه چیزی بدهیم که دیگر چیزی نخواهند؟ پاسخ: مردم جنگ نمی‌خواهند. بله؛ مردم جنگ نمی‌خواهند. حالا جواب سؤال چیست؟
🔹
شش؛ اختلاف انداختن داخل کشور، دشمن را ضعیف نمی‌کند.
🔹
کشور «الف» می‌خواهد به کشور «ب» فشار بیاورد. کشور «ب» متحد است. برای کشور «الف» کار سخت‌تر است. حالا کشور «ب» دچار اختلاف می‌شود.
🔹
یک گروه به گروه دیگر می‌گوید شما کشور را به جنگ می‌برید. آن گروه جواب می‌دهد شما دارید کشور را تسلیم می‌کنید. جامعه دوپاره می‌شود. حالا کشور «الف» قوی‌تر شده یا ضعیف‌تر؟ باز هم سؤال سختی نیست.
📝
حالا همه درس‌ها را کنار هم بگذاریم:
فشار آورد، امتیاز خواست، مذاکره شد، باز هم حمله کرد.
🔹
حالا نسخه پیشنهادی چیست؟ مذاکره بیشتر. اگر دوباره فشار آورد؟ تفاهم بیشتر. اگر دوباره تهدید کرد؟ نگذاریم جنگ شود. اگر پرسیدیم چگونه؟ صلح خوب است.
🔹
اگر پرسیدیم چه تضمینی دارید؟ سکوت. اگر پرسیدیم نقطه پایان امتیازها کجاست؟ سکوت.
🔹
اگر پرسیدیم چرا طرف مقابل باید از ابزاری که برایش نتیجه داده دست بردارد؟ باز هم سکوت.
🔸
اینجاست که بحث دیگر بر سر «صلح‌طلبی» و «جنگ‌طلبی» نیست. بحث بر سر یک سؤال بسیار ابتدایی است:
آیا واقعاً سازوکار فشار را نمی‌بینید؟
🔸
عنوان این نوشته عامدانه قید دارد: «آنهایی که خائن نیستند». چون اگر فرض را بر حسن نیت بگذاریم و فرض کنیم کسی عامدانه در مسیر منافع دشمن حرکت نمی‌کند، آن‌وقت یک پرسش دیگر باقی می‌ماند:
⚠️
کسی که دوبار نتیجه یک مسیر را دیده، اما برای بار سوم همان مسیر را با همان استدلال پیشنهاد می‌کند، دقیقاً چه چیزی را هنوز متوجه نشده است؟
🔗
شرح کامل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/464451" target="_blank">📅 07:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464450">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
شاخص کیفیت هوای امروز پایتخت روی عدد ۱۱۲ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/464450" target="_blank">📅 07:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464449">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
محیطی‌زاده: قبل از بازی کفش‌هایم را بررسی، و مجوز را صادر کرده بودند
🔹
ملی‌پوش هفتگانۀ ایران، فاطمه محیطی‌زاده پس از حذف از رقابت‌های بازی‌های آسیایی ناگویا به دلیل نوع کفش‌هایش، نسبت به این تصمیم اعتراض کرد و گفت پیش از آغاز مسابقه، داوران کفش‌های او را…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464449" target="_blank">📅 07:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
تفنگ سه‌وضعیت بدون فینال
نجمه خدمتی با ۵۸۷ امتیاز در رده دهم قرار گرفت. شرمینه چهل‌امیرانی با ۵۸۳ امتیاز هجدهم و فاطمه امینی نیز با ۵۷۹ امتیاز سی‌ام شدند و به فینال نرسیدند.
@Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464448" target="_blank">📅 07:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نفتکش‌های ایرانی دزدیده شده شناسایی شدند
🔹
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔹
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔹
بر این مبنا نفتکش مجستیک ایکس…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464447" target="_blank">📅 07:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stADwwZNpvBsP5Hu8tiE-1sKmlkJ_n-zxR8_Kf6YE5ZNMUwzNesypkB6BlFFI1dfTu1OjvfOJkU0sz5_OH3lqDvG4SR_5pWCHaIJxM2UUdjI9qgClJ3uvn2vFmCCkTOdVgde-zd9gbH7OfL5sKtS-T_9LfCrxs_F37Gb13DdT8PaOhPQ5h5vWgbwR_BjQIHa9GdS38SrT944bHrv7THoeoolaruSfT-W29XA_T4fUEP9nMpG8-WiTOP40-N_P-4nXvbRfAKNScJUkMXDz5DZrmxZpNKW5zMknTg85RvLWpN6CXHOz-MgWo80QmRHIkeT7W1-Wsc3ji9knKFGcCvDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنهایی ریاض؛ عربستان به کمک فرانسه چشم دوخت
🔹
در شرایطی که عربستان با تشدید حملات و تهدید علیه زیرساخت‌های حیاتی و انرژی خود روبه‌روست، ریاض برای تقویت دفاع از این تأسیسات به شرکای اروپایی روی آورده و فرانسه با اعزام نیرو، رادار و سامانه‌های دفاعی برای حفاظت از مرکز انرژی «ینبع» وارد عمل می‌شود.
🔹
رئیس‌جمهور فرانسه در این‌باره گفته نیروهای فرانسوی قرار نیست در جنگ میان عربستان و یمن مشارکت کنند؛ و هدف، فقط حفاظت از یک تأسیسات انرژی مهم است که امکان انتقال «چند میلیون بشکه» نفت از عربستان به بازارهای جهانی را فراهم می‌کند.
🔗
اما هدف فرانسه از این تصمیم چیست،‌ و قرار است چه تجهیزاتی به عربستان ارسال کند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464446" target="_blank">📅 06:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2TiIrs618-QMCpShfC3gZw2qXM6aziFvSOUJT7ek1Yu9cjuSXXPN-tW07qh9ZxYBlZJ5R3ZmhfPkP_RIhTiAbfoNt3vjYeSatZXqcUHq1o5iYbKZFW0iYUASjBbsKkxULmMUW84pGlw5YeZXWFwX0S-RHAp14brs1EILSJ_yt7LHTDkZ10V-d2ATONEaLLqIc5bZ3nZKtVR6n_RSDVOpDjYBb65-MeXCoVZ2PYxJ-vVmyNiYr89hG1I73I7iZxDXRX1d_AiRq2SVB8LOuUc1kVNWulBgqrXWiHv3DVVzkSjIq72YES7GG7IrIbqRBCBAFuIv5XhAfoQX_i59StmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیک‌تاک دادگاهی شد
🔹
برای نخستین‌بار در آمریکا، یک دادگاه در آلاباما موارد مربوط به آسیب تیک‌تاک به سلامت روان نوجوانان را بررسی می‌کند.
🔹
آلاباما می‌گوید طراحی و الگوریتم تیک‌تاک کاربران جوان را به استفادۀ مداوم سوق داده و آنها را در معرض محتوای آسیب‌زا قرار می‌دهد.
🔹
تیک‌تاک این اتهامات را رد کرده و بر اقدامات خود برای محافظت از کاربران کم‌سن‌وسال تأکید دارد.
🔹
نتیجۀ این پرونده می‌تواند بر ده‌ها شکایت مشابه علیه تیک‌تاک در آمریکا اثر بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464445" target="_blank">📅 06:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9vCtos10AH3OZBm1v8WhA5zj0dwoBh6i4085CSEKUu-4yMVX_TdmjQklQqqul1lLUrzc1_mxQ7oOsH9cHl2NqbB9WCwxx2gSRUAFh_yUhOFTRAK0Bq91t9MBmIOjTRuOeHnIXknryNJ9rDTXAXqDSw-a8yaSAzE51-UJpV3crFEO_tqE9kZ8GhD8bsun-0ylgVr-xMQrJJ198LK8i6jxU2jaTXZxVYrk3LxOUhvSatgJsnD37k0HECnNL8tW8OjZTA2dbTUa6lp4ketQ37g8uZFmwv1s3I0RiDkMNFpClvc45z91lc6BrmNJ8WJdG8ejCRZ1Hkf5YuRc_w5LxzY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به فضا می‌رود
🔹
گوگل قصد دارد نخستین ماهوارۀ آزمایشی پروژۀ «سان‌چر» را به مدار زمین بفرستد تا عملکرد تراشه‌های هوش مصنوعی خود را در شرایط واقعی فضا آزمایش کند.
🔹
این آزمایش مقاومت تراشه‌ها در برابر تشعشعات، تغییرات شدید دما و مشکلات خنک‌سازی در خلأ فضا را بررسی می‌کند.
🔹
هدف بلندمدت گوگل ساخت زیرساخت‌های پردازش هوش مصنوعی در مدار زمین است؛ جایی که پنل‌های خورشیدی می‌توانند انرژی مورد نیاز این سامانه‌ها را تأمین کنند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464444" target="_blank">📅 05:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0578016e29.mp4?token=Bj_lZ4otikPOQLR6yI86t1jSwPgvT-6TYDenRSl0VdSufL4Sn7OT5hQB_7DI1lMkmY5shE32m05uidDRTEeMTh7ESbKLeUDagJl5ZbiybkAK7vtvwsJL6eIH8I3JsyUbppxBaDnSJMC0apvjtqTHVjwXK9CHdktOmaBkeJwwjObwh_Nlezfre6rRA7M8_GcBjCaksRHHHmsmXRK7Ckk4P53Dk2gh1p35sgJQSTGdQhhYgAFovwusVnnhltg0ALDA8twNmC_pr3aHnDrU7KTWUk72ATTGJXVlV9XiXWhYr7I87FbaJBrDA4w5pRDpYTXbwzR_gMG5Py2L-IPlk6oR6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0578016e29.mp4?token=Bj_lZ4otikPOQLR6yI86t1jSwPgvT-6TYDenRSl0VdSufL4Sn7OT5hQB_7DI1lMkmY5shE32m05uidDRTEeMTh7ESbKLeUDagJl5ZbiybkAK7vtvwsJL6eIH8I3JsyUbppxBaDnSJMC0apvjtqTHVjwXK9CHdktOmaBkeJwwjObwh_Nlezfre6rRA7M8_GcBjCaksRHHHmsmXRK7Ckk4P53Dk2gh1p35sgJQSTGdQhhYgAFovwusVnnhltg0ALDA8twNmC_pr3aHnDrU7KTWUk72ATTGJXVlV9XiXWhYr7I87FbaJBrDA4w5pRDpYTXbwzR_gMG5Py2L-IPlk6oR6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قویدل و کارگرپور فینالیست شدند
🔹
پیمان قویدل و تانیا کارگرپور، نمایندگان ایران در کایاک دونفره میکس ۵۰۰ متر بازی‌های آسیایی ۲۰۲۶، با قرار گرفتن در جایگاه نخست  مرحله نیمه‌نهایی، جواز حضور در فینال این ماده را کسب کردند.
@Sportfars</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/464443" target="_blank">📅 05:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">منابع عربی از شنیده‌شدن صدای چندین انفجار در منطقۀ جیزان عربستان سعودی خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/464442" target="_blank">📅 04:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464440">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN3PPoRSCYn0MYXmUODfeHTMP7-W8FWUrBrwLQ-cj98jtcXLN_vp2RY7aT_mgPN8J7JzCa1ZMfxHWBxvm1SOA4q89C5adm7oWBDL4nMu64palbsEWXMxqbeZamirvvr1zv5Jxy--Op4EzHUf4B4_mt80Xkg8MiVGrMLP1LhebklVUvysF4vw5N9b2emASiMkOwuYi4GwfLoTBwcN20ETWRikWC6WcB3vDKWDeqXG947PCuWx2MlT_D0pLSE8bYTQYgAr8ZVOf9GyqI2A3bKvb2vi47lVKuHar0O6702eOuw-UXVdlV7msZkOMzsdFOea_5zXAxk0RRrhSdhbPLov5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RW0l29iojYkJYt556X19zIKVAxDeRiDXs85lur93a4uzweDEvFrRsUAC22c6M2LlWQTbTxWEK-pj2t-aDJN4Qce2mhnDsqzKxrqvATWv7PlJinrqNomzDCPmft102-VenDMGLUGA0nflMc41eAzji8EZnxLTrUEMA4U5J2MBsGNZc4a8_puIpdX3xrksrOFp4uk0oMRnuAVRUvV0ddW1uwoa9FwljaxdmudWd24mAOmg1tp-Y7e47BCy7Gj53kUYwGu9qRLaxe_ibbT4gUeXc-veNWn6YoCRM3Ckdtg44heI9PolZk5GsDgLuOjRCN3jgJvmITOdNoGUZykOCfn1Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تغییر عجیب جلد مجلۀ آمریکایی در طول ۴۷۰ روز
🔹
تنها ۴۷۰ روز زمان لازم بود تا طرح جلد مجلۀ اکونومیست از «پایان جمهوری اسلامی ایران» به «پایان حضور آمریکا در غرب آسیا» برسد.
🔹
در این مدت جنگ ۱۲ روزه و جنگ رمضان به ایران تحمیل شد و سنگین‌ترین فشار اقتصادی تاریخ به نقل از وزیر خزانه‌داری آمریکا در دستور کار آمریکا علیه ایران بوده است.
🔹
حالا اما مجلۀ اکونومیست که در زمان جنگ ۱۲ روزه طرح پرچم ایران پشت موشک را کشید و نوشت که «عاقبت چه خواهد شد؟»، طرحی از یک سرباز آمریکایی شکست خورده روی جلد برده و تیتر زده است که «وقتی آمریکا کناره‌گیری کند، چه می‌شود؟»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464440" target="_blank">📅 04:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464439">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4db251178.mp4?token=shfFjLvFPmLfVSMa-bpomarCrda8-Iq0RbkPUGOUcO1AkeGQdWIQj2aeHlOt5fHkGclTVaMEQLE-E1eYhciBs3rz89q96mhLaoLQesWt8TYbtW2gJEBDzchkjYfzXAX-EehvMwt1GOa-AMnpwZx4UzQvgFONtWAtl5khHza3kLhq9Q93neDLN5gNiR4CW2EoWARHTkU-jWtf-iGZBYHfIQ9Q3oBpsbvTS8XkTX03_0bWR9VBuin8P-v6ms5euEHciMePt-SVE1osynlb5l6AjDQ34Pdht9r_YGgY3rNWO7gwNL-4NEnvkVTiNccbvjV0_am_zgus-zaPKZ0jnUrLPxYi66blIygkkdbHUqPq0scVhDhahNvfNEAHJ48dK_-gQgy23uRewuUOw1gBnbt_vPbYx5nXfyl4h8LrAXEXYYd0BLkiHeIUYSeK3rGWm6drWSff3wJ6tCBRBEE2hHkXh3YQDRT8AUev1NAg4dN0JcQAYnTKeUNaVbZL2y8NqSBFNreZ2TaJqAVV98DBjdKc2rgt-8qxKPZDM0JnAv3bs_nKQuCfJXxZjQR3C2VNuIxpVdJAthnYv6vbRHQ_H9GnqsDygSX4kB_LjCl_KSZloVR9jomUgWoLvREO8Z4k22zBbnv1rIiTy7FTnN-K6nPmLwvw7apoQtQC8Fn2pbSFC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4db251178.mp4?token=shfFjLvFPmLfVSMa-bpomarCrda8-Iq0RbkPUGOUcO1AkeGQdWIQj2aeHlOt5fHkGclTVaMEQLE-E1eYhciBs3rz89q96mhLaoLQesWt8TYbtW2gJEBDzchkjYfzXAX-EehvMwt1GOa-AMnpwZx4UzQvgFONtWAtl5khHza3kLhq9Q93neDLN5gNiR4CW2EoWARHTkU-jWtf-iGZBYHfIQ9Q3oBpsbvTS8XkTX03_0bWR9VBuin8P-v6ms5euEHciMePt-SVE1osynlb5l6AjDQ34Pdht9r_YGgY3rNWO7gwNL-4NEnvkVTiNccbvjV0_am_zgus-zaPKZ0jnUrLPxYi66blIygkkdbHUqPq0scVhDhahNvfNEAHJ48dK_-gQgy23uRewuUOw1gBnbt_vPbYx5nXfyl4h8LrAXEXYYd0BLkiHeIUYSeK3rGWm6drWSff3wJ6tCBRBEE2hHkXh3YQDRT8AUev1NAg4dN0JcQAYnTKeUNaVbZL2y8NqSBFNreZ2TaJqAVV98DBjdKc2rgt-8qxKPZDM0JnAv3bs_nKQuCfJXxZjQR3C2VNuIxpVdJAthnYv6vbRHQ_H9GnqsDygSX4kB_LjCl_KSZloVR9jomUgWoLvREO8Z4k22zBbnv1rIiTy7FTnN-K6nPmLwvw7apoQtQC8Fn2pbSFC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در گرفتاری چندبار یاد امام زمان(عج) افتادی
🎙
آیت‌الله مصباح
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464439" target="_blank">📅 04:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464438">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNhp4Sa1HpgXRE8iAkfXIC18qtba9PYVeCuE0l0of1FUgLoYbcN84Uo4cfErajDo-vWRSR20jM-vVOiPtbKwtLBFrpz_jM9fKPNgm-kAqiWDR6mJ1AorUoJF_SKQ9xzBAAd4gI2jFUE2F_y0gyyYNc0tDgCGJtOtYeZ_bB9JXZeJWKWhnMp0SZEwwt4HBtVreL-lqYeO3ue9ZE3ISFn_6-IAJ1qlIplOvxpfKxAsC2-u2UgGsoxCBH1kFLArajH98TW0rwCYBh5sIMM3I7KCNWacBIuRG9cQNMdY9PSMkAhVNY1MGC6bTAjw5DmzIRZc3xWecMPtWwbL0JGT7IRRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتائب سیدالشهدا: عراق نباید بخشی از محاصره علیه ایران باشد
🔹
دبیرکل گردان‌های سیدالشهدا در عراق، با انتقاد از محاصرۀ ظالمانۀ ایران گفت شایسته نیست عراق بخشی از این محاصره باشد.
🔹
الولایی گفت کشوری شعار لبیک یا حسین را به‌عنوان رویکرد و موضع خود برگزیده، باید موضع و صدای خود را در تحولات منطقه بیان کند.
🔹
وی از نمایندگان پارلمان عراق خواست دولت را ملزم کنند در برابر «دیکته‌های آمریکا» تسلیم نشود و با الگو گرفتن از روسیه و چین، با محاصرۀ ایران مخالفت کند.
🔸
طی روزهای قبل، دولت عراق تحت فشارهای آمریکا پرواز هواپیماهای ایرانی به فرودگاه‌های این کشور از جمله بغداد، سلیمانیه، اربیل و نجف را به حالت تعلیق درآورد.
🔸
پیش از این دبیرکل
جنبش نجبای عراق
نیز گفته بود، درصورتی که پروازها ایرانی به عراق ازسرگرفته نشود مردم عراق برای اعتصاب در فرودگاه‌ها حاضر خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/464438" target="_blank">📅 03:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464437">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/464437" target="_blank">📅 03:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464436">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آتش‌سوزی اتوبوس در محور بیرجند-آرین‌شهر ۳ کشته برجای گذاشت
🔹
پلیس‌راه خراسان جنوبی: در پی برخورد یک دستگاه اتوبوس با تریلی در محور آرین‌شهر به بیرجند در محدودۀ پسوچ، اتوبوس دچار آتش‌سوزی شد که تا این لحظه سه نفر جان خود را از دست داده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/464436" target="_blank">📅 03:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464435">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2zUezQzYu7sNBzV-ASxSafi6CctrtgYFItG8XRh4jh0tfG9BWTg56DKp2eakl-9bYEbyKeVIWyu0yFV3pi8XylJ3nvLGN5iCpBddtgDt2Yt-ByaA-2Xbzgc449Dz5le-Zg9Y0FpsEyqOVwaKfg4Zb7VvEtbv1VBxJ5R6nx7zHRpio6VaMQh2uVQKRQ2URJbtLylRfssoGZ3FCXYr44CkzRHhJildGZQIWv4JRrZQWvU_7quMoip__cHSQzq2Zg8YbmjtZpOVbneRAgX2hsGCYNiKuEY_szIPoFMuh7t4rZtQoDUB5SKQMURqy7XDgbLg4uJ0wl6GAyrB9AJLjuQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست اضطراری فرماندهان نظامی ترکیه، پاکستان و عربستان
🔹
عربستان سعودی، ترکیه و پاکستان در نشستی با حضور فرماندهان نظامی خود، دربارۀ حمایت از ریاض بر اساس توافق دفاعی مشترک میان سه کشور گفت‌وگو خواهند کرد.
🔹
بر اساس بیانیۀ وزارت خارجۀ عربستان سعودی، این کشورها…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/464435" target="_blank">📅 02:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464434">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB96kUIckwWf4UXz66MVnAOOcw79iJgNgYFUDcKL6dUNYRmy7qtPgjuKmKfwVSxtbBFyK9oTOMIriE1Nl7VwsuHoeX96ZymM2lOhiWZdRQETIpS3cDJkA8rKxkISx2nXPJLjKhviJc666U8X_f4wuum56y3gYvKzlUpF7_13q2xkCdOwH1HvUzjoAYEP6x16W38mXHMMb0b0uOoMoJ7vjB8MWQMjYVTgUE3V5rn2dLJ88FFAgG-zmFXdaqOvk8X1CrbrNZ4kTgDckK7InM1VvxCj4ZewqjQ4ZuQLzHTV1wKVqQ7H7qDj9APkuWTCg0qaAJnBNTXm4UhPDimxzVnHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوکار: از غنی‌سازی ۶۰ درصدی کوتاه نمی‌آییم
🔹
رئیس کمیسیون امور داخلی کشور و شوراهای مجلس: سطح غنی‌سازی حق مسلم ملت ایران و جزو حقوق بنیادین کشور است و هیچ‌کس نمی‌تواند این حق را نادیده بگیرد.
🔹
آنچه امام شهید نیز بر آن تأکید داشتند، این بود که ما به دنبال سلاح هسته‌ای نیستیم، اما باید از برکات و مزایای دانش هسته‌ای برخوردار شویم تا ملت ایران بتواند از ظرفیت‌های این دانش استفاده کند.
🔹
غنی‌سازی هسته‌ای در سطوح و حوزه‌های مختلف، از صنعت و پزشکی گرفته تا کشاورزی و تولید سوخت، کاربرد دارد و در برخی حوزه‌ها نیز می‌تواند در تأمین نیازهای راهبردی کشور مورد استفاده قرار گیرد. بسیاری از کشورهای دنیا نیز از ظرفیت غنی‌سازی و فناوری هسته‌ای استفاده می‌کنند.
🔹
اینکه گفته شود نیازی به غنی‌سازی ۶۰ درصد نداریم، دقیقاً همان چیزی است که دشمنان می‌خواهند و ما باید در راستای احقاق حقوق ملت ایران، از این حقوق دفاع کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464434" target="_blank">📅 02:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بحرین: پیامدهای بسته‌بودن تنگۀ هرمز از منطقه فراتر می‌رود
🔹
وزیر خارجۀ بحرین: پیامدهای هدف قرار دادن کشتی‌ها در تنگۀ هرمز و اعمال محدودیت بر تردد، از منطقه فراتر می‌رود و بر قیمت‌های انرژی، مواد غذایی و زنجیره‌های تأمین تأثیر می‌گذارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464433" target="_blank">📅 02:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آتش‌سوزی اتوبوس در محور بیرجند-آرین‌شهر ۳ کشته برجای گذاشت
🔹
پلیس‌راه خراسان جنوبی: در پی برخورد یک دستگاه اتوبوس با تریلی در محور آرین‌شهر به بیرجند در محدودۀ پسوچ، اتوبوس دچار آتش‌سوزی شد که تا این لحظه سه نفر جان خود را از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464432" target="_blank">📅 01:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">منابع عربی از شنیده‌شدن صدای چندین انفجار در منطقۀ جیزان عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464431" target="_blank">📅 01:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHAvhovWGZPLldg3_DJaknz71-XbzYSGW-3Jdi1ZMPY78Pj7dlFRc0SWofyHBjhtomMZZ2qBUDf7bmhKxhf9M6Gxm3MjYBzHKwMhE7yXOMdKoGmqlZVmkambh47jqZdmQ--TuP8XiNlP88sRoEzj1JCc81mgHZFrVj92MoRdiKJUA4LYFMCpcfkKC3k7pAAICvHXtfCaYB8ndeZDFrl6dxoh_qqJ9-ZoBSx-EEIcEo7byTLEVTz9htwc6SM9dvGmJHUfYgdrk2EU6IhvPqQDuAxN9zdYi_dxdpl4cBcSdm7398WwyEhLKN9dOuyD15kar1R_CSDZzB-mXSkjmNUSbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن پالیسی: قمار عربستان روی ترامپیسم شکست خورده است
🔹
نشریۀ فارین پالیسی در گزارشی با اشاره به تشدید حملات و محدودیت‌ها علیه مسیرهای صادرات نفت عربستان سعودی در خلیج‌فارس و دریای سرخ، نوشت: ریاض با یکی از دشوارترین مقاطع امنیتی و اقتصادی خود مواجه شده، ‌ علی‌رغم هزینه‌های هنگفت، آمریکا نتوانسته این کشور را در برابر خطرات امنیتی محافظت کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/464430" target="_blank">📅 01:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c1cbe1b.mp4?token=GLm25Ta61i_yptQVx4dK1FM8AIm7-TmmSz-ByZWfJtTbWwfGkUVb36MXn35FRgVsubuJPyY15ZBG8xX4zNmq81hM_dZhfaShfT7PGBX4BBIygMUrdyWNL4wi4XgGnPy_0rcJ7dR-wb-QpMblEsDMfO3lkLMhIp8qhg1XorNjoQxNy_1fRe298xmFbIXlRjzmcBsxYaX3eZSgS6y6w4-WegGu2_zVjd0rzkpL3s1QylsxCmRnjYunr2YqqqcfJViR8FjZehjUNJ9dbxCT02aFceWZqoj63XtBdlfieSSauS7gCyGmVpMf2Dt1vpenPQeIb-WUaMYhUZ67wgCSRISoQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c1cbe1b.mp4?token=GLm25Ta61i_yptQVx4dK1FM8AIm7-TmmSz-ByZWfJtTbWwfGkUVb36MXn35FRgVsubuJPyY15ZBG8xX4zNmq81hM_dZhfaShfT7PGBX4BBIygMUrdyWNL4wi4XgGnPy_0rcJ7dR-wb-QpMblEsDMfO3lkLMhIp8qhg1XorNjoQxNy_1fRe298xmFbIXlRjzmcBsxYaX3eZSgS6y6w4-WegGu2_zVjd0rzkpL3s1QylsxCmRnjYunr2YqqqcfJViR8FjZehjUNJ9dbxCT02aFceWZqoj63XtBdlfieSSauS7gCyGmVpMf2Dt1vpenPQeIb-WUaMYhUZ67wgCSRISoQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محیطی‌زاده دیسکالیفه شد
🔹
فاطمه محیطی‌زاده نمایندهٔ کشورمان در مادهٔ هفتگانهٔ دوومیدانی مسابقات آسیایی ناگویا در بخش پرتاب نیزه، به‌دلیل استاندارد‌نبودن کفش‌هایش دیسکالیفه شد و از جدول مسابقات کنار رفت. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/464429" target="_blank">📅 01:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
🔹
المیادین از حملۀ هوایی رژیم اسرائیل به شهرک القنطره در جنوب لبنان خبر داد.
🔹
همچنین منابع خبری اعلام کردند توپخانۀ ارتش اسرائیل، دره زبقین در شهرستان صور را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464428" target="_blank">📅 01:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464427">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvHAhR-6iHuawt5SDCTmdwCZmP5wOhrMDuJJ_hqTrcG_-ztlGiuLyQ5_jJIevJIjgnGS8zaWEinqXnP4brU-dZtZkiGXNm6tVUcUpkBYHFcf_nzkHLdyZ5mAiC9mQXPXzvf44eSV39Jx0xpznZNu92-LK5Lpx6pxUxya0LMEtHhOnPU9sNNxtqcq-Bsi2p67UANcKaDu8NpscVz2oipuw-5aANi10mp39bYGdIuko0FZnEEIjywi680LqyEttgVAq0rzQRVddWFO2LL5s1OkBQt1KL9QxvAFx4TdEsAYVXSmPzo9k_f37z1Uc4RxuOrMCZs9nX3yhZbWuxpKrr2OoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام سردار سیدمجید موسوی به ملی‌پوشان تکواندو در آستانۀ اعزام به بازی‌های آسیایی ناگویا
🔹
امروز، هر فرصت برافراشته شدن پرچم مقدس جمهوری اسلامی ایران، آوردگاه و میدانی برای نمایش عظمت و ارزش‌های ملت متمدن و مقتدر ایران است.
🔹
ضمن دعای خیر و آرزوی موفقیت روزافزون، چشم به راه شما با مدال‌های رنگین هستیم. پیروز باشید.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/464427" target="_blank">📅 00:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌ عراقچی: نمی‌شود کشوری را بمباران و محاصرۀ دریایی کرد، اما انتظار داشت کشتیرانی آن منطقه به وضعیت عادی بازگردد
🔹
ایران همچنان به کشتیرانی ایمن و امن متعهد است. با این حال، امنیت دریایی از طریق اقدامات نظامی بیشتر، تهدید، محاصره یا اعمال فشار اقتصادی قابل…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/464426" target="_blank">📅 00:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌ عراقچی: ادعای نزدیک‌بودن دستیابی ایران به سلاح هسته‌ای دروغ بزرگ است
🔹
اتهامات جدید مطرح‌شده دربارۀ برنامه هسته‌ای صلح‌آمیز ایران، ماهیتی سیاسی دارد و نمی‌تواند جایگزین ارزیابی‌های فنی و حقوقی شود. این ادعا که ایران در آستانۀ دستیابی به سلاح هسته‌ای قرار…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464425" target="_blank">📅 00:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عراقچی: ترامپ و نتانیاهو از تریبون سازمان ملل تلاش کردند جایگاه قربانی و متجاوز را عوض کنند؛ آمریکا و اسرائیل نمی‌توانند اقدامات خود را تطهیر کنند
🔹
وزیر امور خارجه کشورمان در جمع خبرنگاران در نیویورک: در جریان تجاوز آمریکا و رژیم اسرائیل علیه ایران، بیش از…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464424" target="_blank">📅 00:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عراقچی: ترامپ و نتانیاهو از تریبون سازمان ملل تلاش کردند جایگاه قربانی و متجاوز را عوض کنند
؛
آمریکا و اسرائیل نمی‌توانند اقدامات خود را تطهیر کنند
🔹
وزیر امور خارجه کشورمان در جمع خبرنگاران در نیویورک: در جریان تجاوز آمریکا و رژیم اسرائیل علیه ایران، بیش از پنج هزار نفر شهید شدند که صدها تن از آنان را زنان و کودکان تشکیل می‌دهند. ترور رهبر معظم جمهوری اسلامی ایران و شماری از مقامات ارشد سیاسی و نظامی کشور، جنایتی فاحش و نقض آشکار حقوق بین‌الملل بود.
🔹
مناطق مسکونی، مدارس، بیمارستان‌ها، تأسیسات انرژی، اماکن ورزشی و فرهنگی، زیرساخت‌های حمل‌ونقل و دیگر اهداف غیرنظامی مورد حمله قرار گرفته‌اند. کشتار بیش از ۱۶۸ دانش‌آموز و معلم در میناب، حمله با بمب‌های خوشه‌ای به ورزشگاه لامرد، بمباران منازل مسکونی با بمب‌های دو هزار پوندی و حملۀ موشکی به یک مراسم عروسی در سیریک، تنها نمونه‌هایی از این حملات است که مستند شده‌اند.
🔹
با این‌حال، رئیس‌جمهور آمریکا به‌همراه نخست‌وزیر رژیم اسرائیل، از تریبون مجمع عمومی تلاش کردند واقعیت‌ها را تحریف کرده و جایگاه قربانی و متجاوز را معکوس جلوه دهند. ایالات متحده و رژیم اسرائیل نمی‌توانند اقدامات خود علیه مردم ایران را تطهیر کنند.
🔹
آمریکا حالا محرومیت اقتصادی را به ابزاری برای مجازات جمعی و اعمال فشار سیاسی تبدیل کرده است. این کشور عامدانه خسارات شدید و قابل پیش‌بینی به مردم ایران وارد می‌کند و به‌طور مستقیم حقوق بنیادین آنان، از جمله حق حیات، سلامت، دسترسی به دارو و غذا را نقض می‌کند. این دیپلماسی نیست؛ اجبار و تروریسم اقتصادی است. این اقدامات، نقض آشکار و مستقیم اقدامات موقت الزام‌آوری است که دیوان بین‌المللی دادگستری در سوم اکتبر ۲۰۱۸ صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/464423" target="_blank">📅 00:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c__o_4Z5H3CGUa40b55n2JA6i1P454Ie9gvVKjFCYsDftJ7fiIiB4xuLdrG10Jq0cU2kWXTl5d741kWiv1g3ymm_EatyjuBFaWoUgppjjtDWydSmvc7Bj9F0xe-b31DLXNQNW3IWbhikk6LS2aXfNFnOOhrZvs_AwoJ17aV9N3CubOYVl3RvedibdA3t_6r1W6gLHtXuJmeaTiZYjrTLUn9wAwSrVJyIM8ftRrjMjExsc7pLfMwdKUv2PLGDGRh75tjPrac4y2wVzWAbgie2gLtK6zAgUWhP8Tr7WGejQkLLsomlnIUQz4rYMjXRD6u3SKRQl7kbCski5tSkPeKHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما می‌کاریم تا دیگران بخورند
🔹
روزی انوشیروان ساسانی برای شکار به صحرا رفته بود و گردش می‌کرد که مرد پیری را درحال کاشتن درخت گردو دید.
🔹
انوشیروان به او گفت: «ای پیرمرد، تو پیر و سالخورده‌ای؛ چطور امید داری که زنده بمانی و میوهٔ این درختی را که می‌کاری بخوری؟» پیرمرد پاسخ داد: «دیگران کاشتند و ما خوردیم، ما نیز می‌کاریم تا دیگران بخورند.»
🔹
انوشیروان از این سخن بسیار خوشش آمد و گفت: «زِه!» (آفرین).
🔹
از آنجا که عادت انوشیروان این بود که هرگاه کلمهٔ «زه» را بر زبان می‌آورد، هزار درهم پاداش می‌داد، بلافاصله هزار درهم به پیرمرد دادند.
🔹
پیرمرد گفت: «ای پادشاه، آیا هیچ‌کس را دیده‌ای که درختی بکارد و میوه و ثمره‌اش به این زودی به او برسد که به من رسید؟» انوشیروان باز هم خوشش آمد و گفت: «زه!» و هزار درهم دیگر به او دادند.
🔹
پیرمرد ادامه داد: «از برکتِ توجه و نظر پادشاه، این درخت در یک زمان ۲ بار میوه داد!» انوشیروان دوباره شگفت‌زده شد و گفت: «زه!» و دستور داد دو هزار درهم دیگر نیز به پیرمرد بدهند.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464422" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMc1CUvVUCTBX12_56gqW0gc3fExUUjRxb61Ve2V6us1lxoRwGgNfSxsMwk6O3CURoJ-_woI5xTx6xSk3-rKq4onUO5gxDiR_H1ocWzUrK9c0SY2JfCEbuX8TOleLfjrHSUXmcVIO8wkx2wtwaTz0HFgDgrUjzk1buHlDQkX75NpNPqZVcS7cPuUZ_iszlNInduyeYIgov-A_AClyIzRkLZSa6TLW0fKUoeHJxtG-6LBHlq3Fyw6MBe-K21VlMogvAHxTO8aoDmo5alusWlGcnrFOOt-oAK5Ad6uufRDnPGVHS5Bjb-ATRXgv2TtJD6u-IjHz0-if-SJhdlNiybqtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توضیحات عراقچی دربارۀ طرح هفت‌روزۀ بازگشایی تنگۀ هرمز درصورت پذیرش شروط ایران
🔹
مهلت هفت‌روزه از زمانی آغاز می‌شود که ایالات متحده این برنامه را بپذیرد. اگر این اتفاق فردا رخ دهد، اجرای برنامه از همان زمان آغاز خواهد شد.
🔹
در صورت انجام اقدامات لازم، معتقدیم می‌توانیم این روند را ظرف چهار یا پنج روز تکمیل کنیم؛ به‌گونه‌ای که در روز ششم تنگۀ هرمز باز شود و در روز هفتم، ایالات متحده برای توافق نهایی وارد شود.
🔹
اقداماتی که ایالات متحده باید انجام دهد، پیش‌تر به این کشور ابلاغ شده و در چارچوب یادداشت تفاهم قرار دارد.
🔹
اگر جدیت لازم از سوی طرف آمریکایی وجود داشته باشد، این اتفاق خواهد افتاد و تنگه هرمز دوباره باز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464421" target="_blank">📅 00:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464419">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک منبع ارشد امنیتی ایرانی به المیادین: خبرسازی رسانه‌های غربی در رابطه با مذاکرات کذب است
🔹
ایران شروط هفت‌گانهٔ خود را به طرف آمریکایی ابلاغ کرده و توپ در زمین آمریکاست.
🔹
دلیل بسته‌ماندن تنگهٔ هرمز اجرانکردن تعهدات از سوی آمریکایی هاست و همان‌طور که پیش از این مشخص شده، تنگهٔ هرمز با توییت، خبرسازی رسانه‌های نزدیک به کاخ سفید و فشار هرگز باز نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/464419" target="_blank">📅 00:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464418">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgxg_FNQXGKs5qH7Zq27J9y7yLKejGEf8rN9FzbN3qoX9trfJ4ybp0Y3pryIGWKKnRBM1spgaovsNtGWJSUKrsz--7QL8knSVlFMrerGWI9voMAGkTuuR05VstoB3h-KpidGx-jHhXJ-XJJnPbOOUvEY_rZwDwfvLmE5-GEzcx777lrh4QfBWkW42zXntD55ce9P6lY108UTNRLOsGJY188Nf8Cp-V8rMV4Ckt9g3c3q23kyswc7_EUWHVDdMLVb3Viks3iQZtno819lHptwWG8mRD7O3thCP4s1ywwAhqem-04l9aNNTe6ilLr1JqihluOEWWLQrnCwf0kGrRjamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با دبیرکل سازمان مل: پس از تجربه‌های گذشته اعتمادی به آمریکا نداریم
🔹
ایران میز مذاکره را ترک نکرده و  خواهان صلح و امنیت در منطقه است اما اجازه نخواهد داد فشارهای خارجی این کشور را به تسلیم وادار کند. @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/464418" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvVpc6-P6l5aoNOn4aeJv2RMvyN-XNWJGU_5Ok69qRZ3s-xcP5ezCaKWQwaAvp35zUMkae5qqzPrSAjnY6nGzCOyQi331RCB2D_fmUs8M7E9qkbzIPFaw1haYhsHFSc_V8dgQ6wRpQE0ImtPaRij5yvV79jhnmP3-xOEC3uLH8cF2yA4blZb7nPCBdCOl6os87zjkpLshSBaNLehuV2tnlK_yixIMR4oT3Geramdj_lOj4LobRqFcjIkDcvXlIgrcR-KLq1eXr_1J_BK8xfqrMLWtVoJsbKxhQ4fqQ7IhNsZ9R51YBmgPwtQrqkAI7jGrfLxJC-D09iOwJp240UaKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال در اپلیکیشن دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/464417" target="_blank">📅 00:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2587ee3592.mp4?token=TCwzDEpi8BiGm4sJnpqBq7UdDyQbn8ZucBuip_iw6xkVK-eHeq7XQoF5LcWQe27jNiCnQhisk5WRiD3r52w86UKUflDbmhaJymDFMT1LRakQq-aYr2B38l9_joyUTj2Da8BZ0rbv9Il1_YJfUso8HrSbClvShnoB-U3OOgYhOBQ64pIoTBxOrHMA4T14gtG8AKjgMQO2yqPyd3NLA1iDdX_W6BOtRgNdhNjDWb-Q3V5zy6vjhm-b8azhy7OvZBf5gF-II5CFej2E8KHw90hVtxLOQaF6gkO6yVlWMixURDfsO_ViJVHS4Gt0KoBqgg6cSoTWvpjl4z2rCLpMrpDiE34LDomY0Xu715mTnX2kn1gsHbUqDemlXtkSabgYammsGXls_KtrafoHEFWzvjQDunu_rCo739qrLbBYDzo1UGjvjVzdgCVtcBXj3AEeDBiC03fkgUKyXDAfKXpj6bNsFo7svnvNVurdldKYU6HGKRUt_qdcpf3GSKy7v39gSD4WiS0StaZtPPqtWM_GLsos-M0iCl1KnUQNabSPjfC6Vtl5wpbsjOfPVYQ_4HSZeChGN0dAzr2K45kuiofPxDksaMyW8-4pzgtHdzz8LmxUYzJ9vKuGOqLSD927xY5GW0mbbY5fC08AFlJP6K7biBQujTQp6GNVi2Norro0xOsh8mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2587ee3592.mp4?token=TCwzDEpi8BiGm4sJnpqBq7UdDyQbn8ZucBuip_iw6xkVK-eHeq7XQoF5LcWQe27jNiCnQhisk5WRiD3r52w86UKUflDbmhaJymDFMT1LRakQq-aYr2B38l9_joyUTj2Da8BZ0rbv9Il1_YJfUso8HrSbClvShnoB-U3OOgYhOBQ64pIoTBxOrHMA4T14gtG8AKjgMQO2yqPyd3NLA1iDdX_W6BOtRgNdhNjDWb-Q3V5zy6vjhm-b8azhy7OvZBf5gF-II5CFej2E8KHw90hVtxLOQaF6gkO6yVlWMixURDfsO_ViJVHS4Gt0KoBqgg6cSoTWvpjl4z2rCLpMrpDiE34LDomY0Xu715mTnX2kn1gsHbUqDemlXtkSabgYammsGXls_KtrafoHEFWzvjQDunu_rCo739qrLbBYDzo1UGjvjVzdgCVtcBXj3AEeDBiC03fkgUKyXDAfKXpj6bNsFo7svnvNVurdldKYU6HGKRUt_qdcpf3GSKy7v39gSD4WiS0StaZtPPqtWM_GLsos-M0iCl1KnUQNabSPjfC6Vtl5wpbsjOfPVYQ_4HSZeChGN0dAzr2K45kuiofPxDksaMyW8-4pzgtHdzz8LmxUYzJ9vKuGOqLSD927xY5GW0mbbY5fC08AFlJP6K7biBQujTQp6GNVi2Norro0xOsh8mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان‌فدایان کرمانی پای لانچر نشستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464416" target="_blank">📅 23:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLak4h6-oh0ShOUtEZ2HoeCSiHM8E9Wdbf5X5An5WmWqcGCfRE2OXP4aazyxGu6mcvPpzbhz1Ll1hLY62w1Rtt-3FueC89xMGnm9Gbmv_VVfhyQl8Ywy-8yflJev6CdDOs3fCaZQpEwMBIMy_oaFXWWgSCU5BWfJeLvcNiaJvMKVg9P5YHA6ST75LikZU3YiZtijQe6IIHPA7Uy7IRlTW9YZXiDEDtg-IpP_OCKIUDTIQBPpQxLmUiUvXG7TWaXV2M7KB4WhsALhBkywkuTXfAAP2RKuD2QFSf4bSS5U_iSFsWQGaUbTwoXbssfZ4ZMP1lQKTaTlBvALCaR-WUe6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون یک نفر دیگر را به فهرست تلفات جنگ با ایران اضافه کرد
🔹
پنتاگون یک مورد دیگر را به آمار رسمی تلفات نظامیان آمریکا در جنگ با ایران اضافه کرد.
🔹
با ثبت این مورد آمار رسمی تلفاتی که ایالات متحده در جنگ با ایران پذیرفته به ۱۹ نفر رسیده است اما بسیاری…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464415" target="_blank">📅 23:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA8Ca36vtpkVnf9Pf7poMJvVjheUTdCV7FK_ZdGb1-bcH3SSX3qhDqkMIkhpeJICCmpWr7H64uV6alaUWlBdvGEW4WCNvS8-vGzhFM2nVjWNGJujxqVLf4-uwrhpI-h68o5HnfeMWjvyNbJPklnQzk1_smcuWPySQ67VUHbV9_DOlWEF28968ts3D78tXeMYheXdYs2fpCYVBSL_b1zZgSrcPWNNTVLs-EgtZuPxLNoFgH5yw17-HwbIc6Luha-moEdqE1TEPpeHSUv3-YZWG6uHk9tsIwcna_d2JyMqwdWNqW7KY2rM4_nIHmllEupu0bZp56GRXLvdcQ8yaRT7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: تا تحقق ۷ شرط ایران، دست از تنبیه آمریکا برنمی‌داریم
🔹
موشک‌های ما قادر به نابودی پدافندهای چندلایه آمریکا هستند.
🔹
آمریکا با وجود بزرگترین نیروی دریایی جهان نتوانست حتی برای چند ساعت تنگه هرمز را باز نگه دارد.
🔹
آمریکا ادعا می‌کند تنگه هرمز باز است تا از گرانی نفت جلوگیری کند، اما کنترل آن در دست نیروهای دریایی سپاه است.
🔹
پیش از جنگ، روزانه تا بیش از ۱۰۰ شناور از تنگه عبور می‌کردند؛ اکنون تنها نفت شرکای تجاری ایران با اجازه تهران عبور می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464414" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464413">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c44200972.mp4?token=v3BtXNssMTJTxPE7-TT81NFWK3Z2jWetqRyl7vLNHu8LNrkGo6UQGPpvoguvYR-7Adfj-7t0q4tWk1uveut7HpQgGpM6jBHGxX8GYJ1W-p7KrawnzwVAaRXYzT_E03XAYhdOtgx55QvK-zSVTh6-3ZMGWh1CeMjsYRiUetVyjXnZwvU4osAPFg3aUISDFgjRdTZyITwBd9itoh6Pshg0SgfYzUqkNXFXl7ls6PvkdWt3DAuRV8XDk1mbnB7DNneNFP8gJ2w-qaA4qXTyDbA6ajNWWbAi3SSKDl1btgQ2ka8mve-CZG0UGr69sP2zmcgwN0LU7qg5e95HZSeeYVvRZ7d1x6aEJ8OsATB9Ow-9d94w11Mc0AVKoWt1diXn5bf5kQ2DKLtua5PzpUHZOElkscSJZXHWWz56B6juumSBy3qXR-xMpPxj8WF6ePT9GyzabcXL3jABB8O7ubxDNi61518ao0kE8dKHT66d-nxljuNY4kinDfiFNH9K0r8_DCqwFks_3A8HeWQS49zjWlDcnrdwXjOJKvPLJYQg6mxhPB-jBUBMk2pIzDPMNfcv_xwLLKy86Zo_XC1QH6CD67t3z2tk0wiq1Uz9C85OLU9cg0Bcf7reeHt5cEU4nlwi0BM-8jvb1_EYba9LGpH0dd4jcMr3VjeWLOJ3hV-RCe1DgJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c44200972.mp4?token=v3BtXNssMTJTxPE7-TT81NFWK3Z2jWetqRyl7vLNHu8LNrkGo6UQGPpvoguvYR-7Adfj-7t0q4tWk1uveut7HpQgGpM6jBHGxX8GYJ1W-p7KrawnzwVAaRXYzT_E03XAYhdOtgx55QvK-zSVTh6-3ZMGWh1CeMjsYRiUetVyjXnZwvU4osAPFg3aUISDFgjRdTZyITwBd9itoh6Pshg0SgfYzUqkNXFXl7ls6PvkdWt3DAuRV8XDk1mbnB7DNneNFP8gJ2w-qaA4qXTyDbA6ajNWWbAi3SSKDl1btgQ2ka8mve-CZG0UGr69sP2zmcgwN0LU7qg5e95HZSeeYVvRZ7d1x6aEJ8OsATB9Ow-9d94w11Mc0AVKoWt1diXn5bf5kQ2DKLtua5PzpUHZOElkscSJZXHWWz56B6juumSBy3qXR-xMpPxj8WF6ePT9GyzabcXL3jABB8O7ubxDNi61518ao0kE8dKHT66d-nxljuNY4kinDfiFNH9K0r8_DCqwFks_3A8HeWQS49zjWlDcnrdwXjOJKvPLJYQg6mxhPB-jBUBMk2pIzDPMNfcv_xwLLKy86Zo_XC1QH6CD67t3z2tk0wiq1Uz9C85OLU9cg0Bcf7reeHt5cEU4nlwi0BM-8jvb1_EYba9LGpH0dd4jcMr3VjeWLOJ3hV-RCe1DgJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز خیابان‌های تهران مملو از موتورسوارن عاشق ایران بود
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464413" target="_blank">📅 23:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464412">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnxpbz83AVnD0NVou8urjXKv672CJwb_AFp_q4kerHP43MCfh0wWI_sFibN5Y3rSDXmhocHSI5HvyihQ_vHqxja7FssZjkZzMtBA6efJdAjaH5Fz5e_5Gw5hxXEO4cPKPAzQyte-CehaN_VZP9QpTWpwxqBJ6qD1JRf3pZyf0bVGc_efGKVVEEOVsF-do0koeP3-Q5MtFWXYnUbAzYmI-gV7A1nptMU5DPueNxzBikwUlrNJzu3ssarL1-AUjKOKxdvt79a1PixuVTTFjR4KOKtuaxQvhB5F5YpfuEPJbIBKKydYke2YNm8GbliAfTCPDjMyV9c67vW-jadKTK5Mww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464412" target="_blank">📅 23:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464411">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71242c0f2.mp4?token=jPdl8J48pVEpQ2h_YYKpCAcbz1-NrbJ2fOe8KYN44fwrcd05E8nBRMH6DagXKx8IxD0vDenmb5b295sY1JlheKQ9pQmiBQbdczZ5N0sI6Qp2H9_S_AdKBUWrU2pGD8Lm-fyyfF-5rKrzC2j23i7onQMrBtOpbKL5yBMqwAdQD2fwGnxh6_3-1YRzpd5wf56c22LLPnI2FxGH9nttiPDjV2nQ9AqxXpkyicWegZuem9p2ofZaNUxIu5mva4x_VUfc0Qyd1B5rBh8bLdZuIb6nmbOdCnnuhg1RosgVJ2HWiJo62zQ1RofDxR-PcTCi-5u1IC8qEyfDTqiNA9M4M2Z9SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71242c0f2.mp4?token=jPdl8J48pVEpQ2h_YYKpCAcbz1-NrbJ2fOe8KYN44fwrcd05E8nBRMH6DagXKx8IxD0vDenmb5b295sY1JlheKQ9pQmiBQbdczZ5N0sI6Qp2H9_S_AdKBUWrU2pGD8Lm-fyyfF-5rKrzC2j23i7onQMrBtOpbKL5yBMqwAdQD2fwGnxh6_3-1YRzpd5wf56c22LLPnI2FxGH9nttiPDjV2nQ9AqxXpkyicWegZuem9p2ofZaNUxIu5mva4x_VUfc0Qyd1B5rBh8bLdZuIb6nmbOdCnnuhg1RosgVJ2HWiJo62zQ1RofDxR-PcTCi-5u1IC8qEyfDTqiNA9M4M2Z9SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشایر بلوچ جان‌فدای ایران شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464411" target="_blank">📅 23:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464410">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ETDCcv1ejwPEQYNspdhVst5x18CeVoLWympuwJYIXQZIkSLh5GoIac-zhkWMLql9on4ym0REqn_hAOzFjbvsGUZn7ZqSqMdSVFYtmibEDgmXrjqZHNac3paEbqrTOE7kUHk5xRa6ff9NP6KQgt7W7YpymTeKOZ0K4_0q806ACjNl7uBfZZvXcghF40x-vg5erGnoyW5WixGBb99tNb6q2jQ5xHzqx8yKyxJeFsr34T48jZiOZ1GkKkEIeYYYBFxEYyNoqTp1MJd2adkgPWG5CGJtJUjhSw3ydZJDCdiAZCmGHNQvBDwObGoKYslOd_qlxrVecILzhDC5IbQ7uhwRvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ETDCcv1ejwPEQYNspdhVst5x18CeVoLWympuwJYIXQZIkSLh5GoIac-zhkWMLql9on4ym0REqn_hAOzFjbvsGUZn7ZqSqMdSVFYtmibEDgmXrjqZHNac3paEbqrTOE7kUHk5xRa6ff9NP6KQgt7W7YpymTeKOZ0K4_0q806ACjNl7uBfZZvXcghF40x-vg5erGnoyW5WixGBb99tNb6q2jQ5xHzqx8yKyxJeFsr34T48jZiOZ1GkKkEIeYYYBFxEYyNoqTp1MJd2adkgPWG5CGJtJUjhSw3ydZJDCdiAZCmGHNQvBDwObGoKYslOd_qlxrVecILzhDC5IbQ7uhwRvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار و گفت‌وگوی عراقچی با وزرای خارجۀ عربستان و هند  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464410" target="_blank">📅 23:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464409">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETesEDxIim0-cYSRWVqqhX-7cwKTt5WKP56K70FNhNp1DrWOithlv4zH8YNP8eHLAmxsj3n2HxWKiteZqeeM0zeKNMDFYpfDXQ03bAdR_Pmw5cNirK7LO9O6lokpM3VVn_6R0GpkGwBspZhQ__JlVxU4PeBw4--tULyZDhsk_CeIBXrOMxUsMtAiXvl6fbxB3CQS3Qws2klqBfSo1iQxShrXwDdeYVhHE3Hz6Irho7Mvt76hRvK-32mxTCKLh9D12zevWEldhQ91hyilAu8NTCDF2VaAscWS-iIalF8Ox3ftrIwBr2jog3zxRRR7IsPY-GiYWQA_-sd3qgyHlqr4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رحیم‌پور ازغدی: مواضع سرلشکر رضایی برخلاف برخی انقلابیون سابق، همچنان جوان، مجاهد و خلاق است
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464409" target="_blank">📅 23:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464408">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b1cc01015.mp4?token=CVL0KPSiN9CXU7aXCYYEbFc0lzo040eetamBCSVWNoIZG5O3y9eRkpMk8H4SJv6nlUs_cBoEtrWLcHW2PDSmJge21Y1gVL54Apo2xtvmJUwg4jjl3gh9kVkfpE-Nu0Bva337sLgaOot0PE-HGHW7d1p48KYx5FbrwYZ-aK4fl3SzhpJaaUzIqanROt1jsTCoWtU6FVYxu5zPaVKIRrUjwGKNKPK_f49BdZu4lws5Fv4r6vvZoyLc2CebTSb8U4NMuNrlvQg6Ux8uYTbDUUtV1gfsEg9jHMDkEr5abx_6oFom0inh4NEXgltG6cswBR7g6ZDkTzIYDAfNIYlRWwC0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b1cc01015.mp4?token=CVL0KPSiN9CXU7aXCYYEbFc0lzo040eetamBCSVWNoIZG5O3y9eRkpMk8H4SJv6nlUs_cBoEtrWLcHW2PDSmJge21Y1gVL54Apo2xtvmJUwg4jjl3gh9kVkfpE-Nu0Bva337sLgaOot0PE-HGHW7d1p48KYx5FbrwYZ-aK4fl3SzhpJaaUzIqanROt1jsTCoWtU6FVYxu5zPaVKIRrUjwGKNKPK_f49BdZu4lws5Fv4r6vvZoyLc2CebTSb8U4NMuNrlvQg6Ux8uYTbDUUtV1gfsEg9jHMDkEr5abx_6oFom0inh4NEXgltG6cswBR7g6ZDkTzIYDAfNIYlRWwC0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از اجتماع ۱۰ هزار نفری جان‌فدایان لامرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464408" target="_blank">📅 23:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464407">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXVWAa-1Y8ve6J1EkwD4Mbx9q15tcZo6IXKvDdithvXe8jzGOSf7jmtwhtUQVDWLHDM19CP-OnGgWBjZ732Iaxe4GZJrgdDnFpo2mDqIcbZutY0zaeLUr6IpeiUWb49l5q-Kx2sDCGi3iuhN9PlEFSZCsytUdY84ihjITjnNL6SRiKd-uZDSruTtB1doaQNIB-bCuMfylP1BjbaENjKiBASQv9eFEgA0JsYnLootZinobmnzImLHjqek0Y1lWQT3UdQa6NcDsbc3KYGtEmSz3Jr-rUU8IMYJdMj-f1x3wYIACCBFOCP6V1BykJFIZNCLdEFcY04IUYGhce7gSjJ2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ میلیون نخ سیگار قاچاق در یاسوج توقیف شد
🔹
مدیر تعزیرات کهگیلویه‌وبویراحمد: محموله‌ای شامل ۸ میلیون نخ سیگار و ۲۵۰۰ لیتر تنباکوی قاچاق در یاسوج توقیف شد.
🔹
متهم این پرونده در مجموع به پرداخت ۱۰۹ میلیارد تومان محکوم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464407" target="_blank">📅 22:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464406">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdLaznsAiVPQDxBQgDijPgN3OTOc5JufDRynePkpYFHYswXyKUKEa8o2kOCH86bfMQH5U-UFrdJre1vrS32GUtsdF7ePi2clZCucvpKq8xLY7LsfU98fpIJ2QAHZyLEg68ZWm9BkEHKoKLHDvInXtdbyRZDQqXlreX4g-ceDqcXV59QTV5Fe082xf1kpH4GlpQjhRcH5a-1ubFQKnM4H7pENEQ0a1IbEBm6yl2PR6RLLb77_2WCaD5GcdMg5ZPQj3YF6zma7xBWVY8oCXYoqDU43V59gc_QiQTN2i1Pm8bETSpf-N2UCQhMyX897C5N48M89vs6TvozT8vtpL9Z6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: بر اهمیت بازگشت به تفاهم‌نامۀ اسلام‌آباد تاکید می‌کنیم
🔹
من از حمایت متفکرانه و مسئولانه رئیس‌جمهور چین برای بازگشت به تفاهم‌نامۀ اسلام آباد و حل اختلافات از طریق گفت‌وگو و دیپلماسی قدردانی می کنم.
🔹
ایران نیز با این رویکرد موافق است و بر اهمیت بازگشت به آن تفاهم، پایبندی به تعهدات توافق‌شده قبلی و ایجاد شرایط لازم برای پیشبرد مذاکرات جدی، اساسی و نتیجه‌محور تأکید می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/464406" target="_blank">📅 22:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464405">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxWpBDVLtKEJRcJ4UCqeBL0veDJPN4SgJ1RjqI2m_s5YOVUKc9xAQYSIA5B4zxa5N7dZV9911odAOwbBAvpx2nvAs5ke6SNkOuPjwDoh5aStRXpvBaYkCYc6_Oxr-_iTitsRw7kdaPybJlcJKijxjUJLTpW3Ur_yIpljdJbzD9XEkFEflMACeAbEbrX6QXYT9siuAKcObdAO60fZPTwIqbwiRtiDnWP-2ReRfkzUmIKifgAsBFv3SpC8yN-cTLkIyeEDjg5WNFO9b3WsfiefgKeSdioTwzR1lyC3d5DIl-KtwZ2VTGFeGN5itK-B3YwCB3VjIfI8qfr-xJ9cRzR8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: از صنعا تا نجف، جبهۀ مقاومت واحد است
🔹
دشمن در تلاش است وحدت ساحات مقاومت را ازبین ببرد.
🔹
ساحاتی که با خون پیوند خورده‌اند، با توطئه از هم نمی‌گسلند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464405" target="_blank">📅 22:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464404">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">توقیف ۴ تانکر عراقی حامل بنزین قاچاق در مرز باشماق
🔹
مدیرکل گمرک باشماق کردستان: ۴ دستگاه کامیون تانکر با پلاک کشور عراق که حامل مقادیر زیادی بنزین قاچاق بودند، توقیف شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464404" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464403">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
هر سال اسفندماه بحث
افزایش حقوق کارگران
با هزار و یک وعده و ترفند مطرح می‌شود، اما در نهایت افزایش حقوق بدون تناسب با وضعیت اقتصادی و معیشتی مردم تصویب می‌شود. دو سال است نزدیک عید اعلام می‌شود که برای
نیمۀ دوم سال
در شهریور
افزایش حقوق متناسب با تورم
در نظر گرفته خواهد شد، اما تاکنون چنین اتفاقی نیفتاده است. فقط یک سؤال داریم: با این وضعیت گرانی، هزینه مسکن و مخارج زندگی، آیا حقوق کارگری حتی برای تأمین حداقل نیازهای یک انسان کافی است؟
🔹
ما عده‌ای از
کارگران پیمانکاری شهرداری کرج
هستیم که با حقوق حدود ۲۵ میلیون تومان، از پایین‌ترین سطح دستمزد برخورداریم؛ با این حال همین
حقوق نیز به‌موقع پرداخت نمی‌شود
.
🔸
تو را به خدا صدای ما
کشاورزان
را به مسئولان برسانید. با هزار سختی
گندم
تولید و تحویل داده‌ایم، اما
هنوز پولمان را دریافت نکرده‌ایم.
بدهکار و گرفتار شده‌ایم و نمی‌دانیم باید هزینه‌های زندگی و کشت بعدی را چگونه تأمین کنیم. با ادامه این وضعیت در منطقه ما دیگر کسی انگیزه‌ای برای کشت گندم ندارد.
🔹
۶ ماه از موعد تحویل خودروی ما در کرمان موتور گذشته
و حتی تکمیل وجه نیز انجام داده‌ایم اما هنوز خودرو تحویل نشده است. اکنون به ما می‌گویند پولتان را پس بگیرید، در حالی که قیمت خودرو در این مدت چند برابر شده است.
🔸
در اسفند ۱۴۰۴، بر اثر بارندگی و سیلاب‌های فصلی، کناره‌های
پل روستای دم‌آب در شهرستان باغملک خوزستان تخریب شد
و تردد خودروها با مشکل و خطر جدی مواجه است. با وجود گذشت چند ماه راهداری شهرستان باغملک هنوز اقدامی برای رفع این مشکل انجام نداده است. با توجه به احتمال بارش‌های شدید پاییزی، از مسئولان
راهداری استان خوزستان
درخواست داریم هرچه سریع‌تر برای ترمیم پل اقدام کنند و در صورت وجود قصور، موضوع را بررسی و با عوامل ترک وظیفه برخورد کنند.
🔹
لطفاً این پیام را به
مسئولان سازمان حج و زیارت
، نمایندگی بعثه رهبری و شورای عالی حج برسانید. انتظار داریم خواسته حدود ۵۶ هزار نفر از ثبت‌نام‌کنندگان سال گذشته که دو مورد است، عملی شود: اعزام به حج ۱۴۰۶ و عدم افزایش هزینه نسبت به حج ۱۴۰۵. ما جامانده نیستیم، قرارداد ما را به دلایل مختلف تغییر دادند و امکان عزیمت فراهم نشد.
🔸
کالابرگ ماه گذشته برای برخی اعضای خانواده ما واریز نشد
و متأسفانه کالابرگ این ماه نیز برای آن‌ها واریز نشده است. با توجه به شرایط مالی خانواده، این موضوع برای ما مشکل‌ساز شده است.
🔹
مدت‌ها برای
رسمی کردن سند خانه قولنامه‌ای
خود پیگیری و دوندگی کرده‌ایم، اما می‌گویند باید صاحب اصلی ملک را که خانه را از او خریدیم پیدا کنیم. بعد از گذشت ۳۰ سال، چگونه باید صاحب اصلی را پیدا کنیم؟
🔸
خواهشمندیم درباره
وضعیت مترو و مونوریل قم،
گزارش شفاف و جامعی تهیه و منتشر شود. مسئولان تاکنون چندین بار زمان افتتاح مترو قم را اعلام کرده‌اند اما هر بار این زمان به دلایل مختلف محقق نشده است. درباره سرنوشت مونوریل قم نیز بارها وعده تصمیم‌گیری نهایی داده شده اما هنوز تکلیف آن مشخص نیست. لطفاً مسئولان مرتبط با حمل‌ونقل عمومی، آخرین وضعیت، برنامه زمان‌بندی و تصمیم نهایی درباره مترو و مونوریل قم را به‌صورت شفاف به مردم اعلام کنند.
🔹
در
چهارراه نظام‌آباد تهران
هر شب از ابتدای شب تا نیمه‌های شب،
وانت‌های میوه‌فروشی
در دو طرف خیابان و
وسط معبر بساط می‌کنند
. این وضعیت باعث ایجاد ترافیک، سر و صدا و مزاحمت برای ساکنان و رانندگان شده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/464403" target="_blank">📅 22:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464402">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6fc40131.mp4?token=Bjh65bP7ZdeI9d-znVxa9rp01vMssx6kXrGvpLMtK10g-lw-BhXhoE5P837AtAGk9AD0zoReyFaQ05Jm_07jkwOgESfWeWByriMHK8JIpEb1mO8SAgKWhUKpE5_WjZKLL0YyNhJUtW6hw_ndSdPOvYj4YbFQs4GEUhHEGMNGNWhkxmjsS8Dk5OjswxzFv0gsC_1Fx-8COCqL_Z6qfdIP5BMRHsijeIHJ4ZjK6raz-DsOFfvPQy9NQfwgwNQsFFu_KzfVX-7tkLdUvVqaNPdjOYVz4HsXMNLXMxWZ58cmBIMzbDDOWazWwpNnRVPQM_c04sZZDeKAgwsdtlKIK7UFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6fc40131.mp4?token=Bjh65bP7ZdeI9d-znVxa9rp01vMssx6kXrGvpLMtK10g-lw-BhXhoE5P837AtAGk9AD0zoReyFaQ05Jm_07jkwOgESfWeWByriMHK8JIpEb1mO8SAgKWhUKpE5_WjZKLL0YyNhJUtW6hw_ndSdPOvYj4YbFQs4GEUhHEGMNGNWhkxmjsS8Dk5OjswxzFv0gsC_1Fx-8COCqL_Z6qfdIP5BMRHsijeIHJ4ZjK6raz-DsOFfvPQy9NQfwgwNQsFFu_KzfVX-7tkLdUvVqaNPdjOYVz4HsXMNLXMxWZ58cmBIMzbDDOWazWwpNnRVPQM_c04sZZDeKAgwsdtlKIK7UFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: مجلس تعطیل نیست
🔹
نیکزاد: فعالیت مجلس برای انجام وظایف ادامه دارد و نمایندگان تنها ۲ دیوار آن‌طرف‌تر از صحن، وظایف قانونی خود را دنبال می‌کنند.
🔹
در هر جلسۀ وبیناری مجلس حضوروغیاب انجام می‌شود و  اگر نماینده‌ای به سامانه متصل نشود، غایب محسوب می‌شود و باید نام او نیز قرائت شود؛ این موضوع مانند گذشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/464402" target="_blank">📅 22:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قبح شکنی سنگین در صحنه تئاتر؛ آغوش نامحرم در مقابل چشم صدها نفر!
🔹
در صحنه‌های تئاتر، مسئله دیگر یک دیالوگ، رفتار یا حتی یک نمایش خاص نیست. مسئله، تغییر تدریجی مرزهایی است که باید میان آزادی هنری، جذابیت گیشه و ملاحظات فرهنگی در صحنهٔ عمومی ایران فاصله بگذارند.…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/464401" target="_blank">📅 22:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YItB2af4pMPIzFaLYcBdLso7FeC9CV9VhxK6ctYnstmD6_seYuVEN-dHaLo69lYa7b8THFzBf5NBsvBhE0NwalLj0eqOXKSvT2LGBX4_utvlsXYxKRMk9lUONfw7ymwTpAIbP7TkKg7dRmmydiHNmM7okz_5PY1Ud1FfOBtFZSB0bVn6m6spNw9H6vJihHLMkWYogRSoDfdjmsqnBoktdFXNiRZoE-aGaCko2TBFV9hzE4r1FjMhg2kcx7Z6M7vQl90AB9RRxRIMHw5kctgNNoI0zOutsiSGNu6pvsCQUb_d3kqLiQnUe8owZFBQ9hCZAwD2AJoLqcJ_73QAF1uX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیرکل جنبش نجبای عراق: درصورتی که پروازها ایرانی به عراق ازسرگرفته نشود مردم عراق برای اعتصاب در فرودگاه‌ها حاضر خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/464400" target="_blank">📅 22:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
ادعای آکسیوس و الجزیره دربارهٔ مذاکرات ایران و آمریکا کذب است
🔹
یک منبع آگاه: خبرسازی رسانه‌های غربی از جمله آکسیوس دربارهٔ دور دیگری از مذاکرات، کذب است و بیشتر در راستای مدیریت بازار و قیمت نفت طراحی شده است.
🔹
ادعای اعزام کارشناسان فنی از ایران به نیویورک برای پیوستن به مذاکرات که توسط مدیر دفتر الجزیره در تهران هم منتشر شده، فاقد صحت است.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/464399" target="_blank">📅 21:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKufBUQJaau42qkxQBcj1pore3c3kMnQSPwR1LItmOSMMtP7x-wJG0FS4B0GBF02P89PRL5TziY8BiXD3U3vow3ZoqEiguv6xQqDWcSlIVhx1jeruWPbwGJsLsYSCz_erkQJ5cJo-_ECJsNTawjz4tofaWP2SA7mVAtiFXxcdoEHHPe5-T5razWMXW11KLDUZGHtUh8qoJk7fGgbCX4wU32Nj_jbF2PI_ShnPyrsTLT2NM8kQPCtizhYm8wkUskAa-nsG8mMke7he7WaiiBVvBn6-ibUpcijaDoAQnjbgAVRE1KpYHtXL72a81eFjilagx5pGxwgXdyXa3TjiZJKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اظهارات هزینه‌ساز معاون وزیر گردشگری دربارۀ تامین دارو
🔹
محسنی بندپی، معاون وزیر گردشگردی در اظهارنظری گفته:«رئیس‌جمهور در سفر به هند، با هواپیمای اختصاصی خود ۱۰ تن مواد اولیه برای داروسازی کشور آورده است».
🔹
نکتۀ اول اینجاست که موضوع تامین دارو، اساسا ارتباطی با وزارت گردشگری ندارد و صحت این موضوع هم طبیعتاً باید ازسوی دستگاه‌های مسئول در حوزه سلامت تایید شود.
🔹
اما سؤال مهم‌تر درباره چرایی طرح چنین موضوعی از سوی یک مقام مسئول است؛ آن هم در شرایطی که تأمین دارو و مواد اولیه دارویی از موضوعات حساس محسوب می‌شود.
🔹
حتی با فرض صحت این اظهارات، بیان جزئیات چنین اقدامی در شرایط تحریم، می‌تواند اطلاعاتی در اختیار طرف‌های متخاصم قرار دهد که از آن برای شناسایی مسیرهای تأمین و تلاش برای مسدود کردن این مسیرها استفاده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/464398" target="_blank">📅 21:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hpcn5rnc9xIkvuH8gXw6zHFxSKUewujUy05HNZf_EFTL92d_XObCetBbeDEbOZEZCH6p2CM0zPs5ZeMO2FL4VDJSBXuGXWTSFNZQyDgCVSArBKpmOVrjlr3MohpNuDk_eZiDyF5nPkj1kkMLkEeqSeUyB8_13fZdHhzBmBjRxJUpDkHKvV-qfc0CNgVHiOUa5S7xx4QXGEtNskV4Zq11nvN7WPxI5fkAa0hbCDhaNEVOuycgQb_zvRKB_8X8ui46BCK-4xzoHmxsS1iZRG3PHNJdngIb3NpTFhRh-MmoyRzBnJPTKaaITVpRsll6d9SWci3WakE_sRSig9NCpmo4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر ارتباطات: اینترنت به وضعیت عادی برگشت
🔹
رئیس شرکت ارتباطات زیرساخت: اختلال در مسیر ارتباطی بین‌المللی که باعث افت کیفیت اینترنت در ایران شده بود برطرف شد و وضعیت اینترنت به حالت عادی برگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464397" target="_blank">📅 21:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464395">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdmwGf5HZPNgwg3WWJGQO15BZwLpitiLenmRJ2DQGAZNMEW2QoSmJak4b-mHkOX0ppGPhHFe0OTvZo0Mw-_hK5CsU0iCxD78-8yWXAzUb20EOUsfPCwhthwbPnMEugc3RbeKI7V39_5vlC-N6D3AVBkpGm0Q_DRoiZwrRm5PHDKs2BCX_i9kc_AynGSc4SXhXOaWcn-5GKSkccwbGgiZVecgAQhg95MqGL11nE4yZYa2VNo0RjPD-nLck3fUbzxkbzmxppXyvmsQvUK0qS5HPVyvFKxUmLzt2aSxBKw77GO9HaYsPmHgrVGGnyJF3hIYaG0E9gU3RS7rKtX1sZ1MFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی آمریکا: عربستان ساخت سلاح اتمی را منتفی ندانسته
🔹
روزنامه واشنگتن‌پست گفته به اسناد محرمانه‌ای از کنگرۀ آمریکا دست یافته که  نشان می‌دهد که عربستان سعودی احتمال دستیابی به سلاح‌های هسته‌ای را منتفی ندانسته است.
🔹
این ارزیابی نگرانی‌هایی را در میان قانون‌گذاران آمریکایی دربارۀ توافق ترامپ برای حمایت از برنامه هسته‌ای عربستان ایجاد کرده است.
🔹
این توافق می‌تواند به ریاض اجازه غنی‌سازی اورانیوم در داخل خاک خود را بدهد.
🔹
این توافق در ابتدا سطح غنی‌سازی را به کم‌تر از ۵ درصد محدود می‌کند، اما توافقی در آینده می‌تواند اجازه غنی‌سازی تا سطح ۲۰ درصد را بدهد.
🔹
سطحی که اورانیوم غنی‌شده در آن می‌تواند با فرآوری بیشتر، به مواد مورد استفاده در ساخت سلاح هسته‌ای تبدیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/464395" target="_blank">📅 21:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcsc2uU6bp8vgDuZa42BCH4i3OmM-NBhJTR34Y2ppBFc0_CfbooZENd4-duqqtLgtONQoSK8zP-91BDB0CrjRwO8brzRNq-5A2DJcG-rHduSLwcHZEl0a-xWas--4sL-ND0FN99nWY0L2cjWxBtPl52Kgxn7bsZOF3ZgTPF2s1KdzZSDB2bGDuBVt9cLki8I0YXF24OgCrrJjBEYo-9aMMKCZrK1Q-1vbCFUWgWqzY0tYm9rhotpIPFCeUSoItXE8NumcjNidMrQLeCRK03HoNVueynarIRjiheelGTSnx5u8dwDfQhylny1JOsunQElbZv9QsEe1VcYb1FJg1FAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464394" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464392">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌ اگر سازش نکنیم، چگونه از شرایط سخت فعلی عبور کنیم؟
🔹
پس‌از انتشار گزارش قبلی، یک سؤال در میان برخی کامنت‌های مخاطبان با این مضمون تکرار شد: بسیار خوب؛ اگر راه برون‌رفت، عقب‌نشینی و مذاکرهٔ مجدد با دشمنی که بارها عهد شکسته نیست، پس راه‌حل چیست؟
🔹
سؤال مهمی…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/464392" target="_blank">📅 20:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464391">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDtT-wxpANfEw1p-DB_IfDLiAty6Jv4t5J3hTo188RH0WAyt8NpDO8UJwG1O8IEqUMJ_7KxurUtEXZImi9UaQiy5nsY0i3vIcVxS19FFkNa5KxOiuWFBLgylOzwcltBokw1SU2UAPp9-HOQfoyf-Li1WNhen2b6R_-vzWqvh6ve4-uCyrXUz9UzX3PlMZEik7_gUc9AKl7q0hZHRQVmN1W-aIDSe64WjDRFxHpXf8qApP3C_bpBHtYLRebfGGf25sKOu15DaBHHhYFbFxvAdtkLKDxautjuOEYzB1okqFMMnbZzz5Qw8_Jj4M6pe_NRxOdS2vCC2d5TGfev_7qd8Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه‌کسی پشت دستور تعلیق پروازهای ایران به عراق است؟
🔹
پس‌‌از تصمیم آمریکا مبنی‌بر محاصرۀ هوایی ایران، عراق ابتدا تعلیق پروازهای ایرانی را تکذیب کرد اما یک روز بعد پروازهای ایران به فرودگاه بغداد متوقف شد و سپس نوبت به فرودگاه‌های نجف، اربیل  سلیمانیه رسید.
🔹
طبق اخبار واصله، نخست‌وزیر عراق که اکنون در آمریکا به سر می‌برد، هیچ دستور کتبی و معینی برای بستن فرودگاه‌ها به روی پروازهای ایران صادر نکرده.
🔹
وزارت راه عراق که تحت کنترل جریان بدر و هادی عامری است نیز اعلام کرده اساساً چنین دستوری نداده‌ است.
🔹
بررسی‌های بیشتر نشان می‌دهد که ظاهراً بحرالعلوم، معاون وزیر خارجه عراق، نقش ویژه‌ای در چنین تصمیمی علیه ایران داشته است.
🔹
این تصمیم که تاکنون نهاد بالادستی مشخصی در عراق مسئولیت آن را برعهده نگرفته، تاکنون با مخالفت بسیاری از جریانات و اعضای پارلمان عراق روبه‌رو شده است.
🔹
رئیس مجلس استان نجف گفته لغو پروازهای ایرانی می‌تواند «رنج بزرگی» برای شهروندان عراقی ایجاد کند و شرکت‌های مسافرتی عراقی هشدار داده‌اند که لغو پروازها ایران زیان‌های چشمگیری برای آنها به‌همراه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/464391" target="_blank">📅 20:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464389">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ae_c64Cx4KrMcS6ySH6GAflkKFoacF7sNY9HLVaFQE5-YznsUY1umFPDXVvSvzJ2WoS3d1M_M-Q3z6Bp7WjDJt7b0FvTVuJ0h6yHe5op4VkCwhNa9jKjFlEsVzSs-nPGrGlerRaPv0Tkq1urqMw5JoviUsr65LwtnZqHYLJqsoVUIdaqLnXllgZtQ6-pj0CJmyGCdlAc8XAWLuhYsPVibYyAwnMpjAhZZ-sq714a7XqF0wuQAxgDndPNxHzX1UX1FTtu71RfOc1ATRSw1NzOdULE0AjqTzLHliXXpKmTUs9jn5ANL_k5IpcILDg9ckA5MKyMBJDdiWr74aweh9zf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqnBsz3DW_uNaqbY9AHHj0UtLbalpueTdT0U3MksTefnbLTelalYWR2FwOHuID7kkhSoz6ek1zyVYOkSQaRdRwQDCtDUmo142bWA1TRdul4oBbAbllHyzXp50qkungESWniURNlCQEtFwvpJWb3J7PFgCb35JWf7xGwxLUG_19zDoFIeHSb2uxTJbmrzcGv6c1xZs6LnnXIYQzJcDsJaPpDEcvfSCWFA7NJ7RofxTtQyIc68H_PNdBss7Fv0DxcHDrx9W0CeUxmCeQAKGdCiKj4fPr4nd-qZV3T_ONZDyJIc2VqVoBCCcUB1trjvYWlB8nrYrBNntHacM75oBYSEdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار و گفت‌وگوی عراقچی با وزرای خارجۀ عربستان و هند
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464389" target="_blank">📅 20:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464388">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38636147d.mp4?token=GpObzZud3hRe3rPeLidJ7_rlBvdnPeVFLN35Y0yFHVf1gSEZBOt-b0pfPS7FOzEAt7u5inO1eKALXE4IXLY3qwUEHKK9fL3EPMo5rsBRIgvTBJq3L8scWvKm9dozLj9ka4lSO7GU9UshWneF9zMLH4Ukre3p1OKZDoz2bFc_rtEioP8Ewdu10jCafDZkxtEwe2mqk2Uqcb1x_JAdi7HIaVxk10k8zF6TYXPn2sJqmZN-O8j5Jj4Wl7GxjNIfiWzpn6wbNSKadfWOr6cgQXcxRBhWYcUO8SHYPISEYMG15qs3nRr5lYKx3_MaJGQTq1BG0Ss94mc0Ol1xPFp4LsjBDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38636147d.mp4?token=GpObzZud3hRe3rPeLidJ7_rlBvdnPeVFLN35Y0yFHVf1gSEZBOt-b0pfPS7FOzEAt7u5inO1eKALXE4IXLY3qwUEHKK9fL3EPMo5rsBRIgvTBJq3L8scWvKm9dozLj9ka4lSO7GU9UshWneF9zMLH4Ukre3p1OKZDoz2bFc_rtEioP8Ewdu10jCafDZkxtEwe2mqk2Uqcb1x_JAdi7HIaVxk10k8zF6TYXPn2sJqmZN-O8j5Jj4Wl7GxjNIfiWzpn6wbNSKadfWOr6cgQXcxRBhWYcUO8SHYPISEYMG15qs3nRr5lYKx3_MaJGQTq1BG0Ss94mc0Ol1xPFp4LsjBDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: من انگیزه‌‌ای برای شرکت در مراسم روز ملی عربستان نداشتم اما از سوی مقامات ذی‌صلاح سیاست خارجی به من ابلاغ شد که در مراسم شرکت کنم
🔹
من در آن‌جا حملات آمریکا از خاک عربستان به ایران را محکوم کردم.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/464388" target="_blank">📅 20:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464387">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2d64b6ba.mp4?token=kJxNbhExlHn8ZrChrlcInQ0XDP9mkWkAf2pRhdo8XrYMq0bdp6DXRBjaNA3s5FOk_21wXUeErJautd4J2ZUw2D7e6dH4XXjw9VFOpO9itClVkccMquRw4_hmJvmA_9tsRWXasVd6Qwfpw_GYYSbWEH-8uML-j_n6KF6iScFirpjks5LNKngzz6MBFVmgaGC7IBU284sFoOYQgHBYJqr8tgxHx_tjyuG6y1Jw6xy9sYa1kGRzuH3gSqVBmudo1wZpS7ahkMEz79hw939wQIuYkvfICfT-F69PxueRmuIQ81flGPg6mUDkLU28KhiJJW31UQWBE6T5COVTz6op2dZjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2d64b6ba.mp4?token=kJxNbhExlHn8ZrChrlcInQ0XDP9mkWkAf2pRhdo8XrYMq0bdp6DXRBjaNA3s5FOk_21wXUeErJautd4J2ZUw2D7e6dH4XXjw9VFOpO9itClVkccMquRw4_hmJvmA_9tsRWXasVd6Qwfpw_GYYSbWEH-8uML-j_n6KF6iScFirpjks5LNKngzz6MBFVmgaGC7IBU284sFoOYQgHBYJqr8tgxHx_tjyuG6y1Jw6xy9sYa1kGRzuH3gSqVBmudo1wZpS7ahkMEz79hw939wQIuYkvfICfT-F69PxueRmuIQ81flGPg6mUDkLU28KhiJJW31UQWBE6T5COVTz6op2dZjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جعفر بازهم حماسه آفرید
🔹
جعفر قائم‌پناه باز هم خبرساز شد؛ این بار نه با یک جمله، بلکه با یک تصویر.
🔹
معاون اجرایی رئیس‌جمهور در مراسم روز ملی عربستان در تهران، کنار مقام‌های سعودی ایستاد و دست‌دردست نماینده سعودی، در آئین بریدن کیک شرکت کرد.
🔹
مسئله طبیعتا…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/464387" target="_blank">📅 20:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464386">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvJHV_3d7P-JxG1e_yvNsvrP1JtmnEyh1E-_dcd-I_vJ47NOoHFxD_axMBtu9eJKq6CI1jEHg9o_KfKXF-G31lHBK_-_Q5c-vELBdl33jbKCAmdIyfg4Fcrf7pDc-HatVOp9gCDX4LaYb_15M7GPeHuPs62TmcHPhy3ycRaIKElAgylMc7Tam3S4zefrmldHX9LgsxsLt_SVrgA9AIOp-zwNOIyojQeGtt4joUaMjtoci_5RsYoO4xP6ZjzQb8J5pG-wFCc1rPjIlPRovGiLgDSpRM84HBgihzjgmPKhY4caSUKCT4ikAqYox8T1xpPpKW45Lnl-uCi500yIF7Ahug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حبیب آبی‌ها به بازی تراکتور می‌رسد
⚽️
روند بهبود حبیب فرعباسی، دروازه‌بان استقلال که در بازی با السد قطر دچار آسیب‌دیدگی شد، به خوبی پیش رفته و او احتمالا از اواخر هفته به تمرینات آبی‌پوشان ملحق خواهد شد تا مهیای نبرد حساس در تبریز شود.
🔹
استقلال در هفتۀ هشتم لیگ برتر، ۱۶ مهرماه در تبریز میهمان تراکتور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/464386" target="_blank">📅 19:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464385">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b2adba85f.mp4?token=mCAVhrayXSit7h7s3QXMIE1VLhYbOBlIYT5W8HxX4bLZ_ohL8uOgEb8eshecD4YMSwebYXRfsbGhdl1endU8oaXc7s9R9O_JRtaV9B8IIzU9NjyBvMJJ0eCfM18fCIvyaQp82KPDNDfXOMsWJFRMJDpyZPAI1HtQTZp3LkkAbC6p6z8kpeF-D4EA3ODT2semHsc49pzWc8f2KVd7WdPtpNrw4oIKCO9lpH6ApOiUbxFj05qfesYHRJwY42gDqfV9D9Bd2Q1ppiOO1tSM_nkTo4U7t4kOT4L3BcQa76vodiASAVgrEsFnoo1UGklitkIeqDInRSYRAdVo-bOZCNXUIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b2adba85f.mp4?token=mCAVhrayXSit7h7s3QXMIE1VLhYbOBlIYT5W8HxX4bLZ_ohL8uOgEb8eshecD4YMSwebYXRfsbGhdl1endU8oaXc7s9R9O_JRtaV9B8IIzU9NjyBvMJJ0eCfM18fCIvyaQp82KPDNDfXOMsWJFRMJDpyZPAI1HtQTZp3LkkAbC6p6z8kpeF-D4EA3ODT2semHsc49pzWc8f2KVd7WdPtpNrw4oIKCO9lpH6ApOiUbxFj05qfesYHRJwY42gDqfV9D9Bd2Q1ppiOO1tSM_nkTo4U7t4kOT4L3BcQa76vodiASAVgrEsFnoo1UGklitkIeqDInRSYRAdVo-bOZCNXUIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناگفته‌هایی از سناریوی شکست‌خوردۀ دشمن در غرب کشور
🔹
امشب ساعت ۲۳ در برنامۀ «قرارگاه جنگ» شبکۀ افق، مستند «مریوان» آنتن می‌رود.
🔹
این مستند روایتی از برنامه‌ریزی تروریست‌ها در غرب کشور برای ایجاد ناامنی هم‌زمان با جنگ و اقتدار امنیتی ایران در مواجهه با این سناریو را نشان خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464385" target="_blank">📅 19:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464384">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff530db003.mp4?token=Ezv7m7zJKKbllF_UG53pyXRX_jT_HmNs4iI-Vssby2ohTd9MG57CdnLXNz-q8pJSWMZQ00F2XhYzSugksWjP9wZy8ZHz0aD1FsCgz-oOosrPoA8fimuCInPrui0XAUHTedU4nMv3I4xBHlCK98mpNNT6OElJDbEL8j8xolpqtsdTEWKZKanDAl9ZpIssQe-G2FmgPoXayLi8PAGw_MfRVv3LDTPokleEhKfLFk1eRF_whqjnv5xn_roym_lPNaMiPnPCpqLV-vvNMKIxnckpCy2NQNhCmN8zLlWmr8TrzSr163UbAg_4Z0Tm4cKqGP_GyLQuJBuPdxXYgR4mvquxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff530db003.mp4?token=Ezv7m7zJKKbllF_UG53pyXRX_jT_HmNs4iI-Vssby2ohTd9MG57CdnLXNz-q8pJSWMZQ00F2XhYzSugksWjP9wZy8ZHz0aD1FsCgz-oOosrPoA8fimuCInPrui0XAUHTedU4nMv3I4xBHlCK98mpNNT6OElJDbEL8j8xolpqtsdTEWKZKanDAl9ZpIssQe-G2FmgPoXayLi8PAGw_MfRVv3LDTPokleEhKfLFk1eRF_whqjnv5xn_roym_lPNaMiPnPCpqLV-vvNMKIxnckpCy2NQNhCmN8zLlWmr8TrzSr163UbAg_4Z0Tm4cKqGP_GyLQuJBuPdxXYgR4mvquxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جعفر بازهم حماسه آفرید
🔹
جعفر قائم‌پناه باز هم خبرساز شد؛ این بار نه با یک جمله، بلکه با یک تصویر.
🔹
معاون اجرایی رئیس‌جمهور در مراسم روز ملی عربستان در تهران، کنار مقام‌های سعودی ایستاد و دست‌دردست نماینده سعودی، در آئین بریدن کیک شرکت کرد.
🔹
مسئله طبیعتا صرف حضور در سفارت عربستان نیست؛ ایران با عربستان رابطۀ دیپلماتیک دارد و سیاست همسایگی اقتضا می‌کند مقام‌های ۲ کشور در مراسم رسمی یکدیگر حاضر شوند.
🔹
مسئله، تفاوت میان «حضور دیپلماتیک» و تولید «یک قاب صمیمانه» در شرایط حال‌حاضر است.
🔹
در ماه‌های گذشته آمریکا حتی محاصره دریایی ایران را برقرار کرده و گزارش‌های زیادی هم از «همکاری نظامی واشنگتن و ریاض» علیه گروه‌های همسو با ایران در منطقه منتشر شده است.
🔹
در چنین فضایی، طبیعی است که رفتار نمادین یک مقام ارشد ایرانی بیش از شرایط عادی زیر ذره‌بین قرار گیرد.
🔹
اما شاید مسئله مهم‌تر، تکرار الگویی باشد که پیش‌تر نیز درباره برخی اظهارات قائم‌پناه دیده شده.
🔹
ابتدا حرف یا رفتاری از او خبرساز می‌شود، موج انتقاد شکل می‌گیرد و بعد نوبت توضیح می‌رسد که «منظور این نبود».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/464384" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464379">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZxdRNXZFCNB1OzecdZwd6U6jtdnb8hUlccrdyVEkQe_D2E3-Rg7uuPLf6rl1IkfceqLbV7DpW2e971K2Fe-M5fvjv28_8vucCtSjVSqYbRv5R1bNmmMXYF0wMwncEajFL-VkBDssdItuvmbBQUYUXpIS_OnPd8_CQ4UnENuxlp2fzGYk95YW7SIXWyMMvEriWULTXwAP8XkWEa-U1Syy2e4iMiTckzT16TaXsNejJp9HG-xTYh14kEEnVuB88608dbbkVetRCVtZ497LnIw5tltObyxtH1N9SWc7wVAzsAfwY_sTbPSvN0kvfjJewrDQNOVPpnPBgy6iG0bjMaMxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqPUCr5uLeRU2i2-5xJ06XVkGlUObRlykEfY_9XsDCkmqStVuV8a6wi1dsI8Hwab7agQMybmHxFr6W712VpRPJq4z6N4Dczqb2A6bbvuLbuXrVDSnEYVD2bXR9v_AXqTiN1b3_ZvgHUvj9kjsVUOrkSTxO2c8p96RLHvWN-Fu2X789Fakgsdw4kDHg6sToMVNV0Z9kxaI30O6_1MpIy0tX4doX65kQZwCKMG25mt3Ps6CToYYSMcM4c3JXvvPefzcrRywmEoqAIW7eSndsYWBAPRuSGH_EImKcLdG_YqJJiHT9s4STctCTnAsgU9tqtPFtKPipS-HyxOq0uwHAq1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3FBbGsuhFUPcaL00S08UOoOz-bBWc89S2Fk9oKxtVIw3vibOXDABpN0-rvLzT6d0s31zlYUf8lnF4jPtzi_BNOT10k0HN8-OLP-zmxm76nTefOClVW_Mt1fnqliMWKjZwViWIrl0EdMmvvdPzpNjmQ14vubJ5COZM3phmeMchTt_7L9sdXRRygYLO-NEZU83JUb0Sj9axhsxgPf5TYXIYae1wSRxHKf8rY1hTneHjWc5V-r4oFPfo4KKs20aA6HLAMj3SXRrPKvJq5k4VPL4H9QY5B-6TyjQ7InmacBjHVcaq7rtpiAbe1Ehxdi7dfY5z5B3PO0pZw_30oKtMLACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTZkwm6coOra7UyxsoX9J6y6hVYMloKJoCmk6_VM1bHTd6hkwUbkfPgigBNsfiZuZq_Wi3nGU4LbK1C9WfVwE7hiXn3HXjQfgeDHVEwXb5Zwo9ui3ywzvWtYmh9pZH7ZjamPvFYK2wVkjmnz-GpWUpe5p4_D2UYBKnlqxETy_Wl7x8eJZHmt2Q_gfJAG_DVrTb0wJUeKKd10w9aNCici38c6Pgdt-RLGCxdwJJTY7oDd4T9H2sQEiTdJiRiPHpmMV7K5mgJCKK4cgEiTXUyDqSXmMICQHxICqWlEAJiiF3Kpy8B0v7_bcDRr2HRAXaaM-UR-9tBRamfus7WIBk3k0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfUIFh10TbSJvXuw8R-7B483IQY_72m7rc0dr1EvOKUd6ZxrZwq1-qDx-vrxHOuST7NJPPM68MwqZYK9nbHmibpk0jYZ_SZm_kdFYzKIEpnvTTWLFH6f0kfinAM3h9OS-92m_ynQsGh51h8NIbM1S2Fdb9Lr9HhQMEKUKmQV4JUiMqgiPuBdZPfdDzFfmKAcYjXbFw94aUenIgxAbKoe-StjN6VBOqljt2jTypoZMhv1OL830Lapnyfd9rveyGPHgZtNsyAtYb2lVnDzCiulOTN7VUQksCltq5RAkzsqALdEAJ55013HCRQzDTRfFeyTag8MdGj1ypE7nYccGHnq7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گذرگاهی به مشهد آقای شهید ایران
🔹
چهارمین شب ویژه‌برنامۀ روایت‌گری در رواق کشوردوست.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/464379" target="_blank">📅 19:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464378">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
گزارش سی‌ان‌ان از رکوردشکنی تازه ترامپ؛ این‌بار در تنفر مردم
🔹
«هری انتن»، تحلیلگر ارشد داده‌ شبکه سی‌ان‌ان، با بررسی نتایج نظرسنجی‌های انتخاباتی آمریکا گفت میزان نفرت آمریکایی‌ها از دونالد ترامپ در آستانه انتخابات میان‌دوره‌ای به سطحی بی‌سابقه رسیده است.
🔹
وی گفت: «ما درباره این موضوع صحبت کرده‌ایم که دونالد ترامپ با عدم محبوبیت تاریخی‌ای وارد انتخابات میان‌دوره‌ای می‌شود، اما وقتی داده‌ها را بررسی می‌کنیم، مطمئن نیستم که این توصیف به اندازه کافی گویا باشد. وقتی نظرسنجی‌های مربوط به میزان محبوبیت او را بر اساس شدت احساسات مردم تفکیک می‌کنیم، ترامپ بالاترین درصد «کاملاً مخالف» را در تاریخ انتخابات‌های میان‌دوره‌ای دارد. ۵۰ درصد آمریکایی‌ها اکنون می‌گویند که به‌شدت با عملکرد دونالد ترامپ مخالفند؛ این به آن معنا نیست که صرفاً او را دوست ندارند، بلکه یعنی در آستانه انتخابات میان‌دوره‌ای، میزان نفرت از رئیس‌جمهور ایالات متحده به بالاترین سطح خود رسیده است.»
🔹
انتن در ادامه گفت: «رکورددار قبلی خود ترامپ در انتخابات میان‌دوره‌ای ۲۰۱۸ بود، اما در آن زمان درصد نارضایتی شدید از او فقط ۴۵ درصد بود. پیش از آن، جورج دبلیو بوش در انتخابات میان‌دوره‌ای ۲۰۰۶ با ۴۱ درصد در صدر قرار داشت. جای تعجب نیست که جمهوری‌خواهان، حداقل برخی از آن‌ها، دارند از او فاصله می‌گیرند.»
🔹
تحلیل‌گر سی‌ان‌ان در مورد رأی‌دهندگان مستقل نیز گفت: «۵۶ درصد از رأی‌دهندگان مستقل‌ به‌شدت با ترامپ مخالفند، در حالی که فقط ۹ درصد به‌شدت موافق او هستند. در میان این گروه که در این کشور تعیین‌کننده نتیجه انتخابات است، شاهد نفرت از رئیس‌جمهور آمریکا هستیم. این همان چیزی است که رأی‌دهندگان می‌گویند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/464378" target="_blank">📅 19:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVDX7pPGJCwLL998OOPV4TKnWyEUCd_eDSw4qRvxlT6UA87Ve6r8hbCdTucAdDfjOEsS0KHeQKvEiCCgn2giMMAiCgTrVjSO1562x1VqxNl6yxsnZRkJmgknP5d6ango15FcD-Hv117BtjaA8uNDD7EeBIfnXH3VQEsOK07WjNPMpyrl34qtxJivUZxIC-IEEBNcZPjKqTZhahwd_ZRgI3VG2kiZf4h8X7pxA2nYlHjfFIwGCA2ygalgKBl-dScBhoXT6t17rA-Litq_znpuRo4-ohCzD_Q-QIYqImMzvjwkKabD30RCLgfmpmtkUQU2NI7pz9nhaZpXTXZ-vkTfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMpfCF8xiIlT11E5ZIdc4maW3TpypIkKNCMD4Gs9iFFEVdWMSoBvoof_Oh0tzM87jhnNqPoAeOEJqUdPScftjtrFFVTJHYsx82hNZa0axyjZERIt-MNoyxHBQoPCwvaTU5hgCKoE8asLtED4--ooCQCcCZZpW2iov4Kwjpjq_z0shdbC-_yvpc2mvhMxG3odMZ4ePPtg4pjQO7Xh_w5ceCq8QfG449z5UvWI-BmWnBL51QZOJ2FZ7-Kpvud4H-bXKtGkh3TeRqOK6cie7i9v0h7Ic95h1ywQxmpHiHTJCgI-8KepL2ZDgJuoeuWHIxv6h27SLrrk5QgkU4vV9Gzcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgIyiq_VtdUSvBRK8Ev61E2qVPMs23mwyD6UbpxNf-z_zfYZlITOPUyWYNfk7elPkzz_2Vw3hbFRj6dp_cOcpDSzeochlQ2b7GQwUudvqpoktFVjquxc2xAfUg9E4uI4gKV_DuGbvfCxEkWbq-g8LY7ak2JkDRuTL1H95f4r49Zu-silM-1UCVLx-t2RzFZvd5zGyBMW1kv2PzaoVRWT9DINxwLGsiUPu88EUEMjdccrHPs99Am5mrvPare9pSdFqnmxjaEEdN2JvdTr1icbPN9RCVYMEiapywyjhfVe9WfqqL_Xvmgak10SNx7pOR4lpYAHyhVvQPD2z2GGxRzEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqOmdplyjXGOt0Vjuo15_Giwh0fw4ZDEX1RAN7UX36eKLMly3sOVgJViSO-PgTvE8fp_HlJHGM0-H1_kgzlN-XiiZJ-lH2eUdTVYXqs4_Y7_SREqvB_EoQyTZOyURYhOCsaY1os7nt4YM9hOJ_GOcF_Jx0cqu7He6Pr8nOFYUUo2jH7PVGMl3wng3Du8oeed1NRQhsJQBMW0kG0UL1gPb1pagXXo8BHmgw4kAlp95fQdBaa7qkqAaHuJbbymcniS5Whr0SbqHKD6Cp71Of3B39zMDoNd2qyn9GfZ21a9Cz58GwgxFJ0b9hRWhEBn1UURIZ9QhRXpKTc6VBTFFsdJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-plunk_KrqaJFufQSJhmJNGMRLQAyX6oviHOwPQcR7nBMI9TiY7oTFKzF6QTw_a4gNu97dP6TJir7eTHcFdNCuR2_S1QONNWItWAC6a0dfruXa4bfHkyD3dDddgjNp7rCiiEScOnADuBWPuvB4XKi4IoJhVolt4OxKu7M2w9z9OFAFag3zNQjU1q5BsKctKuyB_pYlPV4C58yeshojNJiCEsvgf192xlW98FOSnZ6sPB_lSwlGlCPptCYZbGtGTchad-QEBk_dQM8yzBFjxDZoVvB5e1s8-5klRp97P7aJfzwMQ99WrBlPvGr7QVKbtu88z3GCCof8mtpdtKm_qjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltUPP8kDcmV4rMtBi2k9Q_O777Ks1GRETC_j0yUN4PqB6vG3jmoyT8PrxF9k5nkPs_riNXM7vl5AYHhitJebdjcgHc8SRet69F6IBlz-7QAcdvNxl5ZJgmdKXD1lPy8GYZYu1FqphaxizwRHPdRusySfTJLhlCfZ0lkX3wr7RnCX1y5MM-jbO4MeEgl4925o4AHqOTJIzzmwnRIWKDvRO38md0IRprNxpwq4HE7gEdDGDhYfFyiHwf6Q4eG5N0FRpBwv25yEe1tl1cRgAmJtOQtBgX3ZoOketgv1hQNK38vn0FNbZgivpUNzpiILgqJIiEZQol_0gm0VsJgv0mHV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M29qZuJECIirG2gC4tmsAXWQJUkk_WKMc0yaCLeBbgRJhylrkD6bTimw1bz8L8tBbGEgSX5omR9nIi-4QFEgjQxjhnMOwdNqdGnIc7f7kparY5PFVB7fR7YojhQ3VCQwKASHJI5zLP05Qywe8JMhRzfw9B1SLaEPRtwLipNWoI9-DPZeduI8x9YJiDk9uN8Ax7_Bkj_BxfQfY51tp2KJCB-41UgJ9zinchh9lQk40fFwQfFXVuifu0F4Z5IekYHgj7r5KbULpnlpjwhZuZy03JaZYx8grDHUcDz6mfrNcM41Un17j_fDrwY3jGVAWSQ0v40fGfbfQg5xXtggfbPOiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سی‌و‌یکمین آزمون المپیاد علمی دانشجویی کشور
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/464371" target="_blank">📅 18:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBWgGJzccdIo1wBTZ5fdtO_ontjD6VC4KrJ3tZtL0BL8DzWLBq76Iv8GCgbRJWmA2oaQacHM9Qv4P6gGLVUqAJ1cCsk--bYTqf2swrUVK5td2Q66NJ9U4T-wlB9jiccm8ZBvK1m5NtviL8jiR7rLjdU-s_61AHfO5PFEvD4sUWN-KUyzGwL550dLqozzSBR33vfSo1Zz-pFqQWRxpkwh19tiofXQCFt3EhpH9yS87gSPx6bJMHoHn2ImXB1slDLvoJLeiS0sH0m2xFxfgsCx5QAUnTAod1svp1FenEg3RlEb8Oo1FOqfGUarH-ADc4roAFyy72YunPf_AAzFDsXK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۳ پهپاد و ده‌ها نیروی مزدوران سعودی را منهدم کردیم
🔹
مقام نظامی یمنی:‌ نیروهای دشمن سعودی که قصد انجام حمله در منطقه الوازعیه را داشتند را دفع کردیم.
🔹
در این عملیات ۳ پهپاد دشمن منهدم شد و ده‌ها کشته و زخمی در میان نیروهای دشمن سعودی به‌جا ماند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464370" target="_blank">📅 18:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464369">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmCUJFI0LwD6yZdHWuJciQHWfiLD0hpAO0_TopdgIviFG-6pwPF6CRlawpURG_SohFTNA8gtWsSAQ9SOGfGP3eu6qIXaemABaUBtY5ddMRDodGzqTAI5YbrnZhYATK4PGGndjbPuQTOZwRWnLtCKITgTf2Oyaf3YmlxPRMWB03xRDN8iKMyhAMUbV3RrVMcKeZMhI7EIlj45IJ7Q3ZdjWKTkEFRDKPWxE-hOxR2rl7bBqHi3ERvivNSfSKsc7PBCrv2fnE6635o3cwEEvbPJRtiKaRdlmst1CPcutBC4WpT2xO5gNtmRSWeMrKDzxkvb30lrnmS4Ec2jtw-NdsgqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضوی: پزشکیان در مصاحبه با رسانه‌های خارجی باید دقت بیشتری می‌کرد
🔹
معاون اجرایی دولت سیزدهم: رئیس‌جمهور در مصاحبه با رسانه‌های خارجی آن‌گونه که باید نتوانست مواضع ایران را منتقل کند و باید دقت بیشتری می کرد.
🔹
در گفت‌وگو با رسانه‌های خارجی باید مراقب بود که چارچوب و ادبیات سؤال‌کننده، روایت طرف مقابل را به‌جای واقعیت ننشاند.
🔹
نماینده جمهوری اسلامی ایران باید در عرصه دیپلماسی و رسانه‌ای، روایت خود را با صراحت و اقتدار بیان کند.
🔹
پیام ایران روشن است؛ ملت ایران اهل تهدید کردن نیست، اما در برابر تعرض به حقوق و منافع خود نیز منفعل نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/464369" target="_blank">📅 18:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464368">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIZTTSTm0U-jNQWRn5O8P5yBc7eNFp0DDYIjJD26sk9fxoIK97wreXkDo9ZuvWN4_AdHKAXQ1AeE5-UGBrswW_rtr1XaLMr3nAjMlTosKQ77yvDTL4tio_G33DOo7QyRvj29bolkWpBnYEM68IlLMZzZL75Y2sNgZgozfMXz2Tp7T2wKsGRnpaGQA45tDgr-Nez7bhI59qSat00R0rxiyReIGJpKfc1mxZzS2mW4H3FRXdkYDUHX6IuC_7wA6Y-CTLD8lcwvBvijx2P4pV1SHjgkgp9AOuCr7n1pimlL9BimF9IbDRBks7d4gNSSBmkjkpCR7HWJHpb4HkpRtykY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نجات: به هر تهدیدی در هر نقطه‌ای از کشور پاسخ لحظه‌ای خواهیم داد
🔹
جانشین فرمانده قرارگاه ثارالله: رزمایش ۴۰ هزار نفری موتورسوارن که امروز در تهران برکزار شد در راستای آمادگی برای تهدیدات بود.
🔹
پیام ما بسیار روشن است؛ آمادگی ما مانع حرکت دشمن است؛ هرگونه تلاش برای مقابله با ثبات کشور با سرعت و دقت پاسخ داده خواهد شد.
🔹
ما با تمرکز بر نیروهای چابک و موتورسوار، در واقع با مدل‌های جدید جنگ‌های نامتقارن و تهدیدات ناگهانی مقابله می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464368" target="_blank">📅 17:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDemuZhkE5P-elv9M9Nvp1B9g-iE9L1cqaFC15i1rbhVnbGt1-vV3ynRy6OHS4w4hYLYJIiw1z1WoiPhPT4wmF5yTZHUKnxQ1QX9pnmHSGRJOYaWTnlujBfWQR9iuOKFzTd8v4dXvK5ancBiol1-sOyftOdzp9Ewpdwsstsdogm89V_0cJQupjkSRTMn9MsKNIc4pwae2G-Awxab-i2yZ9HWWxfNygqjGXtjDYpcNMQU-Y6DUki50Qqu5uCdfxFKbtJ_KeehJ3rybosY7nwFdCX50J3lB0d-nHipoBMY9rbvlvDs4EVn6MA8TF8M5XREgheqg30PhoCJ9t0u8JlPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lsdaKQ7oSr3iaQhFTDsaiNxgVaMkn2-tDvnbG2nQIJZKl6mq1cyzBLVg5skHqlDrThWiCXxzz5Fw4NrLnPEz4bUWb5jjwSmCQXMpQQwbPjvLEEkTsOu2aUxmF4kpVYjduyxVDzfUzUyLcSXiIFIxFjCCNG0Ga3ozxiXjiEJDuYpb7OFYgol_TdwVeetcBn0ob36E-fblQdHGtmM4amEv2zAzj4lLdUq45cpvNPVv7PqLbYHZ1w3m6cQEW-x3msbXg_2dLPCoc56OvdzuI9qTtzSwUhKtvHoc_TiUgtGwdhBXnBf2_Q-9h6SIyZGmJvytGLSFg4ITlhrYDGsBtZPgsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سخنرانی عراقچی در نشست ورزای خارجه مجمع عمومی سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464366" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۹.pdf</div>
  <div class="tg-doc-extra">2.3 MB</div>
</div>
<a href="https://t.me/farsna/464365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۸.pdf</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/464365" target="_blank">📅 17:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-ojnYoGBUOGvZ5rVUJZngy7v4LooTUIpx1LWH1ZNhqLyhrbjZOAlYFx0_Krmc8Nn8O82F42961q-zyNFc7zB_P0C1gaq80ZJZPfXKLPwHHNZbrTa2QOGhwK98SeUjEvYGZUHMFDUKX8Rn16Rpnf3oWelmN3ld426uvsDhiptSo-2jGIcarI_sPFvooPbtnzHomD6AfxCFN3gZAYffyjIbRyGLVFRqYRvJitzKljQlO82LQGGvGph9uluYt9ZoyISqEeNEAKNYQDAhnQyiIY3wPhUuaXcOvSfujusp7KYLtmf2DDYW_UlUDv7yzJGR-Fq8jqCeLXuy9byZxjSKyU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبح شکنی سنگین در صحنه تئاتر؛ آغوش نامحرم در مقابل چشم صدها نفر!
🔹
در صحنه‌های تئاتر، مسئله دیگر یک دیالوگ، رفتار یا حتی یک نمایش خاص نیست. مسئله، تغییر تدریجی مرزهایی است که باید میان آزادی هنری، جذابیت گیشه و ملاحظات فرهنگی در صحنهٔ عمومی ایران فاصله بگذارند. این مرزها حالا بیش از همیشه در حال در نوردیده شدن هستند؛ گویی هیچ نظارتی روی صحنه‌های تئاتر وجود ندارد.
🔹
چند ثانیه تصویر کافی است تا یک اجرای تئاتری از سالن بیرون بیاید و به موضوعی عمومی تبدیل شود. دوربین موبایل، صحنه‌ای حساسیت‌برانگیز را از دل نمایش جدا می‌کند، در شبکه‌های اجتماعی می‌چرخاند و همان چند ثانیه را به نمایندهٔ کل یک اثر تبدیل می‌کند.
🔹
به هر حال، در این وضعیت، دیگر بحث از کیفیت هنری یک نمایش عبور می‌کند. مسئله این است که چه چیزهایی در یک اجرای عمومی مجاز به نمایش‌اند و سازوکار نظارت چگونه می‌تواند آنچه را که واقعاً روی صحنه اتفاق می‌افتد، مدیریت کند
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/464363" target="_blank">📅 17:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464362">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ff7897c9.mp4?token=Nc99T6jFpP4hiBD1MyJ4oM1LIeutGoc6jcq9Qb1XzZiv7RPummDSlF4PK5B-mxCosyEK2sa6jPNWmmfkNBiRiJA962Pe4GwjHgIpOQAhfOVPbK5u0qnviYPtcKdp_Iz6EVXetgLofBBzNuqmdyfCjJXId-DfaOab29sNWK78W1pSgoHPwWAXL4jjfWCc17-N_Fhkk290aux-OQwrP0HR7k6TYVlxzwWWo-1Xjj0iAb1IQYRm3lPabVcVOAnNBie8okGaX7bt5r2f6tV408MJ55kIbJ3JUq762EZcPS6B0pIh91d3HJW4TXqpI1AGZMX16odfS6_lXSpphBKagM37KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ff7897c9.mp4?token=Nc99T6jFpP4hiBD1MyJ4oM1LIeutGoc6jcq9Qb1XzZiv7RPummDSlF4PK5B-mxCosyEK2sa6jPNWmmfkNBiRiJA962Pe4GwjHgIpOQAhfOVPbK5u0qnviYPtcKdp_Iz6EVXetgLofBBzNuqmdyfCjJXId-DfaOab29sNWK78W1pSgoHPwWAXL4jjfWCc17-N_Fhkk290aux-OQwrP0HR7k6TYVlxzwWWo-1Xjj0iAb1IQYRm3lPabVcVOAnNBie8okGaX7bt5r2f6tV408MJ55kIbJ3JUq762EZcPS6B0pIh91d3HJW4TXqpI1AGZMX16odfS6_lXSpphBKagM37KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی پویش جان
‌
فدا: مردم ایران شدیدا پیگیر آموزش نظامی هستند
🔹
در سپاه تهران بزرگ به‌دلیل مراجعهٔ بیش‌از حد مردم برای حضور ایست‌های بازرسی و ایفای نقش در دفاع از کشور با مشکل مواجه شدیم.
🔹
برای ثبت‌نام ۱۰۰۰ گردان مقاومت ملی مردمی ۱۰ ساعت زمان پیش‌بینی کرده بودیم که کمتراز ۱۰۰ دقیقه ظرفیت تکمیل شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/464362" target="_blank">📅 16:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464361">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTIv1Y-W-5plpVMv2x-mNMeW0ePGClsivSJ75HwAiX2dKtsZTB8GAMaXzBdxmt8WaAuYvy4iFjxaV-MiJD2hGO94GuvNU11_teiMAxg5AnX1Nq-cvuf0bK8nDXJMUvi35_yf-q9INGPGcxRrBNge0RVPeENYhKpYp-tqMdwTEky-VGizLmhOgeDypdYZJPKe9Y4JjY2xnSJcdIMPsWsRfmKZ6gxqWzDkVyZlAR0qIElJUFgGkEG_YutWusrU4p15bQGiFFPxtf10VMm9oU25EL2znkpUsvlw2WL5E6t3MsX1cRxHZP1Sde4yqDvRigfJCDesrPEFsll55XBjzzGT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران: کلمبیا در جایگاهی نیست که دربارهٔ تروریسم و موادمخدر دیگران را موعظه کند
🔹
دولت کلمبیا به‌تازگی با طرح ادعاهایی دربارهٔ ارتباط ایران با موضوعات تروریستی، از قطع روابط دیپلماتیک با کشورمان خبر داد و آن را اقدامی برای مقابله با «تهدیدات تروریستی» خواند.
🔸
وزارت خارجهٔ کشورمان با رد این ادعا اعلام کرد: دولت کلمبیا که طبق اسناد، تحت نفوذ شدید کارتل‌های موادمخدر است و از بخش‌های اصلی شبکهٔ نارکوتروریسم (تروریسم موادمخدر) در قارهٔ آمریکا به‌شمار می‌رود، در جایگاهی نیست که در این زمینه‌ها به دیگران موعظه کند.
🔸
وزارت خارجه همچنین به توقیف ۵۵ کیلوگرم کوکائین خالص کلمبیایی در تهران در اواخر شهریور اشاره کرد و گفت این محموله از سوی شبکه‌ای وابسته به افراد ذی‌نفوذ در کلمبیا قاچاق شده است.
🔸
ایران همچنین ادعاهای کلمبیا را متأثر از نفوذ آمریکا و رژیم صهیونیستی دانست و اعلام کرد در قبال این رویکرد، تدابیر لازم را به‌کار خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/464361" target="_blank">📅 16:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464360">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOrr7DPV38rXtOJVsbZQXB2DjiaDPYAbf8Rl5WSNUe0SrWiVdyizkCe8s45ZMh9PmH3qT5Cw3dv5gq3M_FfUMSFBb-FR3_-Wo-BxfjCkFUdqjTDj0O8eIMgEVlt5YOfY5w4IUhx7nDI2VfTnQNF-stve64p_p1G7seh7lCvbwpMvU7xve45VKJTPT-rSofhxOFfFUuepi2bnnUSJYZ2aqN5-0mvq_mLshj1C_Mp2jnZWw1K1kSpBZ6fdrtW15VWwwb4RAfq-ydeMUZTMOWkgjMPi9A_cVOOUceFOXhUlXWSgqmhD_mIQ1cZlPiTSxsSV8qe_o9V7HQlwmSfQMEuVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زارعی فینالیست دوی ۴۰۰ متر شد
🔹
زهرا زارعی در مرحلهٔ مقدماتی دوی ۴۰۰ متر بازی‌های آسیایی ناگویا در گروه سوم با ثبت زمان ۵۲:۰۰ ثانیه به مقام نخست رسید و راهی فینال شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464360" target="_blank">📅 16:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
آغاز تحویل تدریجی پایگاه البعشیقه ترکیه به دولت عراق
🔹
«سعد معن» رئیس اداره رسانه امنیتی عراق از ورود توافق بغداد و آنکارا برای تحویل اردوگاه «بعشیقه ـ زلیکان» به مرحله اجرا خبر داد و گفت این اردوگاه به‌صورت تدریجی و براساس جدول زمانی مورد توافق، به دولت فدرال عراق تحویل داده می‌شود.
🔹
به گفته او، دو طرف از مرحله مذاکرات عبور کرده و وارد مرحله اجرای توافق شده‌اند و روند تحویل اردوگاه با هماهنگی میان دو طرف و با هدف حفظ منافع امنیتی و حاکمیت عراق در حال انجام است.
🔹
وی تأکید کرد تحویل اردوگاه زلیکان مستقیماً به دولت فدرال انجام می‌شود و این مسئله حضور دولت عراق و حاکمیت آن بر اراضی کشور را تقویت می‌کند
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464359" target="_blank">📅 16:42 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
