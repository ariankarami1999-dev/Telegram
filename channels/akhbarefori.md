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
<img src="https://cdn4.telesco.pe/file/hM5rYHFbH5Hy4hoUtW3tGtxrkQXvpGcloEQyEORrzs8SMzWNtlFBmw0ZKDMLTtANMuU5zcDl1LL-oim7L-ubYZUZOUQiv4SphL5SnHtm7OKX4mPrrJGBzL7Sy8rvDnFAfb3mxEXu-F5UEKzYt-aXPjudGCm5-6c4e7hZaPjQ9ct5MdFmDdYmsJD2YI29SD_kYmolJYBHRy6UTmozBh1nmcSARWxX1y9MM7YdMZ9vRohAj1Fkqrekj4MK5QXsZX2ZuIwm8zl0iTFzQK222ntOSbuIpLSM-Q9sHUyYPuLcq4zZf-nncacEorAjhe3RsT8220VuA6UlITMaTy0z1ApRWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 04:31:48</div>
<hr>

<div class="tg-post" id="msg-692801">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=ZS2tpFoSaEu9KVxNjMYhaxHILtyX-NqiIYt3w_cM96sQZV9l6WlMGtkNP-_gBnVP0uFNGHpxGB7LRsI_PL-CGZtUB18LrWIileX33woanmpEbC7l0V6NIwKlwDhQqN5E0dXk7UCWmWW0nt6gqJfAOuazIAABSyak1Cjp1QFOkgeTBZrK26Coy6-hcUkQdMDpu0N3qv2MEwe5cJsHGnJkXd8wz6S8DN6l5-gvCS7IriX_pbJ3vSOVUG-r5iYCdM-oTZ0v-m_2FL1_f-BVpOsl4dhvf8vwZdtCqQ7DP1zOlsGfsDd7Wpm-qovZm9WZ8CU9d02v-ZLtIJ7s8Q_j0sInLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=ZS2tpFoSaEu9KVxNjMYhaxHILtyX-NqiIYt3w_cM96sQZV9l6WlMGtkNP-_gBnVP0uFNGHpxGB7LRsI_PL-CGZtUB18LrWIileX33woanmpEbC7l0V6NIwKlwDhQqN5E0dXk7UCWmWW0nt6gqJfAOuazIAABSyak1Cjp1QFOkgeTBZrK26Coy6-hcUkQdMDpu0N3qv2MEwe5cJsHGnJkXd8wz6S8DN6l5-gvCS7IriX_pbJ3vSOVUG-r5iYCdM-oTZ0v-m_2FL1_f-BVpOsl4dhvf8vwZdtCqQ7DP1zOlsGfsDd7Wpm-qovZm9WZ8CU9d02v-ZLtIJ7s8Q_j0sInLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز: آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
🔹
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/akhbarefori/692801" target="_blank">📅 04:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692800">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e602d4c4bf.mp4?token=QbyeQtMz5fk8AAoNnUEYZ9WeCz8KfzdnR9RWU1HIYTMtwnXYaEWMLx9KIsrI4a5ux9MHwLGLAsNFBVsShzXl_x94T_qMz0PX65gQLd7K05n-rMq5OWfiFAmx8ObCxXxUah9RPRMtifbTul-JG5vKPdBbKY5MyPGyCePDY2z0KJs8MZ0jfVdsf5Ifb_q2J5NvjjnqA68XXHijErXRBgx33sklm8PaxbiFqIikv1VvGi90I-XAepdJc5lgNfN2ooT1-ydqKChGzCJeHlFju-bnCYDcmNGMa8dSa-5T_RBkjJxyTUtFNJIhRHQM0U3Y5TL02tCCkQEllRr9GMOpfdgkHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e602d4c4bf.mp4?token=QbyeQtMz5fk8AAoNnUEYZ9WeCz8KfzdnR9RWU1HIYTMtwnXYaEWMLx9KIsrI4a5ux9MHwLGLAsNFBVsShzXl_x94T_qMz0PX65gQLd7K05n-rMq5OWfiFAmx8ObCxXxUah9RPRMtifbTul-JG5vKPdBbKY5MyPGyCePDY2z0KJs8MZ0jfVdsf5Ifb_q2J5NvjjnqA68XXHijErXRBgx33sklm8PaxbiFqIikv1VvGi90I-XAepdJc5lgNfN2ooT1-ydqKChGzCJeHlFju-bnCYDcmNGMa8dSa-5T_RBkjJxyTUtFNJIhRHQM0U3Y5TL02tCCkQEllRr9GMOpfdgkHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری فاکس‌نیوز:آقای رئیس‌جمهور، منظورم همان حادثه ژانویه است. شما جراح قلب هستید. نیروهای امنیتی ایران چند ایرانی را کشتند؟
پزشکیان:
🔹
ببینید چندان هم دشوار نیست. می‌توانید افرادی را به آنجا بفرستید تا حقیقت را مشخص و احراز کنند. آنچه فلان و بهمان نشریه در خارج از کشور گزارش می‌کند، با روایت دقیق و مستند از وقایع مطابقت ندارد. وقتی می‌گویند ۱۰ هزار نفر یا ۱۷ هزار نفر، چرا دست‌کم دو شماره ملی ارائه نمی‌کنند؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 375 · <a href="https://t.me/akhbarefori/692800" target="_blank">📅 04:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692799">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb1368f28.mp4?token=eYkdD9iNJpa-SEmYO6H_853A1iq6Qj0Uzc1HQF9ukPXq9vP-DJjy60JQugSMZPDtHJvKw5pPylc5Ulsps3UBI0SirxfMfzsn9IpaDNHBBJ2UFM9ulSso2OfjDgKsy5UgkLRaNm1UFRgfiRjzfTNIjU_8BGu_D0zriCKpZSv3t_tiqYq1URzYhQQD5uvTmQ0STrdaPb_k2mX0Eu6gOglHbXoKIvZUft03QhD4XbXc1bVTlwYG2OHk3fTH0Rr2R4YU6snvvkFhQoQFaA-86QtzKz8XVZYIQ0qCzc_z8CGVbmCPLL1IFMUvA8oOB-qkNfczLNKd30221VwwfwsOOrjfrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb1368f28.mp4?token=eYkdD9iNJpa-SEmYO6H_853A1iq6Qj0Uzc1HQF9ukPXq9vP-DJjy60JQugSMZPDtHJvKw5pPylc5Ulsps3UBI0SirxfMfzsn9IpaDNHBBJ2UFM9ulSso2OfjDgKsy5UgkLRaNm1UFRgfiRjzfTNIjU_8BGu_D0zriCKpZSv3t_tiqYq1URzYhQQD5uvTmQ0STrdaPb_k2mX0Eu6gOglHbXoKIvZUft03QhD4XbXc1bVTlwYG2OHk3fTH0Rr2R4YU6snvvkFhQoQFaA-86QtzKz8XVZYIQ0qCzc_z8CGVbmCPLL1IFMUvA8oOB-qkNfczLNKd30221VwwfwsOOrjfrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان به فاکس نیوز: رهبر ایران در سلامت کامل است و من یک جلسه ۷ ساعته با ایشان داشتم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 481 · <a href="https://t.me/akhbarefori/692799" target="_blank">📅 04:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692798">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
فرودگاه بین‌المللی نجف در عراق، تمامی پروازهای رفت و برگشت به ایران را، از روز پنجشنبه، ۲۴ سپتامبر، تا اطلاع بعدی، لغو کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/akhbarefori/692798" target="_blank">📅 04:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692797">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bca2a5e28.mp4?token=Fg2-45rCSo2xxkgdJXA-UIME4ILjq0iBEt_xsAZTG7-ssrD6nhoo3aXQUYYHmjD5TmdEAJeF5Pr2peDEMxo2CBZtenEBaQe6J5U9MVW7JHttagVMgJDn6C-BqHFiSzxz_2FnGAsABkJxRimqw72xocDnpcm07vUU3-_mUZmjhA6UWCwxHXYdFUl45o1TnRCZL-HGiqBsdgsIsX8PFxCQNf6wdZD1gKkDRubZAYOdgtUjK8cyeh-ZUdkYCIlNEBFIKB7bYOX844euwH-4jLtAU-jbzU0TChbODOGK8L8PVi__kM2vZ_wPp4pC-pMq48kqSmavFTHqkY1pzIjBCBdCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bca2a5e28.mp4?token=Fg2-45rCSo2xxkgdJXA-UIME4ILjq0iBEt_xsAZTG7-ssrD6nhoo3aXQUYYHmjD5TmdEAJeF5Pr2peDEMxo2CBZtenEBaQe6J5U9MVW7JHttagVMgJDn6C-BqHFiSzxz_2FnGAsABkJxRimqw72xocDnpcm07vUU3-_mUZmjhA6UWCwxHXYdFUl45o1TnRCZL-HGiqBsdgsIsX8PFxCQNf6wdZD1gKkDRubZAYOdgtUjK8cyeh-ZUdkYCIlNEBFIKB7bYOX844euwH-4jLtAU-jbzU0TChbODOGK8L8PVi__kM2vZ_wPp4pC-pMq48kqSmavFTHqkY1pzIjBCBdCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساکت و مبهوت ماندن سفیر دائمی اسرائیل در سازمان ملل حین عبور پزشکیان از جلوی او
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/akhbarefori/692797" target="_blank">📅 04:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692796">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRXlMSwyxCizX3lS9pgW8GcGqbGyWHsxEdxdD1IERvPZl5n-BXlTg1ZFTYtkTNuJzmwNIfvGT5gqUHgCS64VSJC0PZZIgeb151WTGXKl79Ar3H1hdyIX6OXuRdsJK_T3QMZkQ5YqUT_F-jK4dc9jyLS35amHXKwxQXsbgT6p_Au5X_MSMOo2cABQ70120XSUMSitI2x3Qfx13GQzgUESavY5UuRIYjXRZS3w6rhvC9MkqRWzeIk7s6ENq8feg85LrvQLEFxcniJGYhulXCvIBvNqshE_mlUsezzRLcfvlFKv3JoVWjJo0UdrFruTmydnzUKmxSxLhIsQYwLEnJEitQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پکیج جذاب استایل مردانه؛ کت چرم Artim + نیم‌بوت Rad
🔥
✔️
کت چرم مصنوعی با طراحی مدرن
✔️
فری‌سایز، مناسب سایزهای L و XL
✔️
نیم‌بوت مشکی با طراحی خاص
✔️
کفی پرسی و دوردوزی‌شده
✔️
سایز نیم‌بوت: ۴۱ تا ۴۴
🔴
قیمت 2,580,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/63697/180124/</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/692796" target="_blank">📅 00:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692795">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔹
از خبرهای جذاب امروز جانمانید
🔹
🔹
هیات ایرانی نمی‌تواند از نیویورک به تهران برگردد؟
👇
khabarfoori.com/fa/tiny/news-3247541
🔹
نقشه پروازهای ایران تغییر کرد | کدام کشورها پروازهای ایران را بستند؟ | احتمال اقدام متقابل تهران
👇
khabarfoori.com/fa/tiny/news-3247657
🔹
هشدار: قیمت سکه به این عدد می‌رسد | نظر شما چیست؟
👇
khabarfoori.com/fa/tiny/news-3247593
🔹
تولید سریع، مزیت تازه برای رقابت در بازار جهانی
👇
khabarfoori.com/fa/tiny/news-3247497
🔹
همسر دوم بهاره رهنما ناگهان سکوتش را شکست
👇
khabarfoori.com/fa/tiny/news-3247553
🔹
صفحه اخبار منتخب خبرفوری را اینجا دنبال کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/692795" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692794">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ولیعهد کویت: ایران از تنگۀ هرمز به‌عنوان برگ برنده در جنگ استفاده می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/692794" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692793">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876e946901.mp4?token=a2pksIn04Y8OzLr4Htuq2VO2RudWD1q-5laX8ibdl7WIG7SaFSS9gOdj78OgR9cBcEOj5kd-pX3iP6BMC9OJiwng4jJjxddDlAL-Oo13Y1Idwz2ohNlNsnIjLQ8i7Y9bus6HSe3t7DGDB9Ln-fS301bWRXaAaqGbjkWtmkeCnfyQAMYtOS_-TEQrUFcvQ-1NuZvsAkkhZ2g4YOP-zR_HghyoGirYyghGcmDlWQFLwxLFhdIAhle2Y-hNY0QmSVDuzQjKhRj-XnpXo8_mMe6MjyFsWOLCvpf121pn1a-n8Xaz7nKmJNvGfWzoE9XtJBhF-JIhh1KW8TyfT90ROGIQHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876e946901.mp4?token=a2pksIn04Y8OzLr4Htuq2VO2RudWD1q-5laX8ibdl7WIG7SaFSS9gOdj78OgR9cBcEOj5kd-pX3iP6BMC9OJiwng4jJjxddDlAL-Oo13Y1Idwz2ohNlNsnIjLQ8i7Y9bus6HSe3t7DGDB9Ln-fS301bWRXaAaqGbjkWtmkeCnfyQAMYtOS_-TEQrUFcvQ-1NuZvsAkkhZ2g4YOP-zR_HghyoGirYyghGcmDlWQFLwxLFhdIAhle2Y-hNY0QmSVDuzQjKhRj-XnpXo8_mMe6MjyFsWOLCvpf121pn1a-n8Xaz7nKmJNvGfWzoE9XtJBhF-JIhh1KW8TyfT90ROGIQHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون، مجری و تحلیلگر آمریکایی: قطری‌ها به ترامپ یک هواپیما دادند. و این کار چه سودی برایشان داشت؟ هیچ سودی نداشت
🔹
ایالات متحده از قطر دفاع نکرد؛ بلکه سامانه‌های دفاعی «تاد»(THAAD) را از منطقه خلیج فارس به اسرائیل منتقل کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/692793" target="_blank">📅 00:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692792">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LawMoiIXkFpb74kJfOQgFN0FZJksXXRdagzF2IWw9rjh5MdcBe-p9Nu-VDcTfD21hmSk_sz6BzRm52U1JE_lVx4b4WeDBtyk_9kG5Kbfcr0wVYTLL5AmdEUD9IbL8sOb3-ec4ESS8ebFmECi5jn7KYCqnN_x5Vpp9yrjDukH0Xp-u9rvrbeILTYC0AU2f1NAz9iJ1cHgnX-Mn20ykAwce4zfKfArpJm992W_PxUig1M7WLSmJWiYsvw_1jRWymP08x0ZoD7tv9UKWFtdeMwQ67pLwsIdKO5LlmROwIuRTAsYmSS0E07Ek_nq0MxYp-1aCux0l1jCiPlmsLyq2KtFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اسرائیلی: تبریک! ما یک دیکتاتور پست و مضحک روی صحنه‌ سازمان ملل داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/692792" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692791">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: تحرکات فشرده‌ای برای دستیابی به سازوکاری جهت توقف هرچه سریع‌تر درگیری‌ها و بازگشایی تنگه هرمز در جریان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/692791" target="_blank">📅 00:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692790">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام کاخ سفید: ترامپ همچنان برای گفتگو با ایران آماده است اما نیازی مبرم به مذاکره ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/692790" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692789">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رویترز: عربستان جریان انتقال نفت خام از طریق خط لوله شرق-غرب را افزایش داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/692789" target="_blank">📅 00:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692788">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e20b2386.mp4?token=A5xtmEhy5iuE_1uf3y3XJ5KHvArWA3AJ0bEYk8qAjpr8GvAb7FHvo7ejBKY7T0DcS24Kb-Z44iCiCZ08cBPk56MLL3wZiaKZOuEOO5FJl5dguxlfOAh657wr1fD0PlAfEIkllRMNesqqUO_nydLBA9Hwqiv6IhWVFEV1wW_sgL9anEn8el_X_Z1RCj_xChdtttET8anZQkfVnUEwOvub1kvNzwf8Ki3-vDdbAk-ka_MtngAp_-eE3NJnbVkivRUxpvduX6sEKvaN4q3un0709ojRZgV31pt4sCghwmglvZ7Pjjg5Lz5oD6cxXYzZvKxlohVmxKbdkl-PYjtdYvOq3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e20b2386.mp4?token=A5xtmEhy5iuE_1uf3y3XJ5KHvArWA3AJ0bEYk8qAjpr8GvAb7FHvo7ejBKY7T0DcS24Kb-Z44iCiCZ08cBPk56MLL3wZiaKZOuEOO5FJl5dguxlfOAh657wr1fD0PlAfEIkllRMNesqqUO_nydLBA9Hwqiv6IhWVFEV1wW_sgL9anEn8el_X_Z1RCj_xChdtttET8anZQkfVnUEwOvub1kvNzwf8Ki3-vDdbAk-ka_MtngAp_-eE3NJnbVkivRUxpvduX6sEKvaN4q3un0709ojRZgV31pt4sCghwmglvZ7Pjjg5Lz5oD6cxXYzZvKxlohVmxKbdkl-PYjtdYvOq3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاوت اساسی رمزارز با پول ملی در چیست؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/692788" target="_blank">📅 00:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692787">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkC44mRkt71n2jFvuMjHa7o93LlERBOi2gtO-2XYUvTjrLx7HTfxqp2WmhHxAmAvFCwXHbsgOQp6UbiuQaGxJ6A3b41aTlD7XrhpXYgmOdn9LPsumyq8oj0bfnffBPpdwP5cri4mFzPkhdfnoTge_doSykBw4dkVSvmqT80CTDu3Hom-0wsFmTui8ZUkrZrdQ3aLT8Sjmp00aG002n46MeixljFSTsAdUHfujbITAfkhHp24yoEskPJBd7xr5JG8rLk9qsYWOeJwtd2PkWSDcNzSkN-qcAYlKEqERR2r6Nooj94MHj2PSTnVsH1pYftzSUgIzN859LfkOkocFrxLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در آمریکا، قانون خنده‌دار است
🔹
اگر علیه رئیس‌جمهور آمریکا شعار دهید (مجاز است)
🔹
اگر علیه هر مقام اسرائیلی شعار دهید (دستگیر می‌شوید)
🔹
اگر پرچم آمریکا را بسوزانید (آزادی بیان)
🔹
اگر پرچم اسرائیل را بسوزانید (قانون مجازات می‌کند)
🔹
در نهایت شما می‌توانید هر مسیحی آمریکایی را توهین کنید، اما اگر یک یهودی اسرائیلی را توهین کنید، مشمول قانون ضدسامی‌گری در آمریکا خواهید شد. این شوخی نیست، بلکه یک واقعیت است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/692787" target="_blank">📅 00:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692786">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ab0c03cb.mp4?token=Bu0PWd5PjckplKHqi6ESRKU-Qjw7Z9IQhDSb92dysto8ZcMiutglnGrXbsOzpxeRZN76ITlQx_bRBg77_43TqC4FdrPgOB0E09O-DJgp7uZ6UZr0irAdyhBgoaBGQ6f2BwNQkq_HYKZ0RqzOBsyWZ4b1gWGZJZqntHnwfVGX0fWpUqWQROu683a1qTML8nCtT7BJp77baACu7xwgNtijU38a-pdwcm3ARhYOSo3pJ3dTDPej2c246yLoADXrN7nWXMVsX2ltpCJM8FfYfJZrEV7FPI_mmjJyM7K7IJ2qnOg_P0CkcUhQg90oeLnhUW3aaQ37OjoO2m6AwPmVO4lksw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ab0c03cb.mp4?token=Bu0PWd5PjckplKHqi6ESRKU-Qjw7Z9IQhDSb92dysto8ZcMiutglnGrXbsOzpxeRZN76ITlQx_bRBg77_43TqC4FdrPgOB0E09O-DJgp7uZ6UZr0irAdyhBgoaBGQ6f2BwNQkq_HYKZ0RqzOBsyWZ4b1gWGZJZqntHnwfVGX0fWpUqWQROu683a1qTML8nCtT7BJp77baACu7xwgNtijU38a-pdwcm3ARhYOSo3pJ3dTDPej2c246yLoADXrN7nWXMVsX2ltpCJM8FfYfJZrEV7FPI_mmjJyM7K7IJ2qnOg_P0CkcUhQg90oeLnhUW3aaQ37OjoO2m6AwPmVO4lksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشین لگویی تمسخر سخنرانی نتانیاهو در مجمع سازمان ملل توسط رسانه‌های جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/692786" target="_blank">📅 00:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692785">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IshCtEdFNe8qlx9FRRxleXT_h4JTwFfxx7ucHN1xOKT5-PrRvld86cmrzQpVm1d2ZR27RBRX52o_2boorilA4VRx4neHyJnXrBQfSnNbu0fR6GcqIEYaWC6AuGMNnNl4s623pjyioQAyCkuwGNtTEqZIVdC6HteJFd6Nd0KbP50a3SxTwHVff0KSuj-dFfAOaSg3hjYRWZH8YMHMGIjJp5HEVAnj1QnE3LLUg3PBwdBvVrOrFIhReEmqArxX4mJlfYaOaxyjJtaJnHQPCAuIGGY0vAimJH5lx1iyJU3m-g6Ff1p8IHoT4UBufQ_yggIEy6LiP8TlM4UlNmzUFOMI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/692785" target="_blank">📅 00:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOjU9kaH23ZHAn5Kbuad25R80HIMS6kPd6TKWgV6hGjqJV84R4FSPT-ThgfZq8Vu8OhcDdZtPOkD9G-EJwRDQI8rjv4OzeLOc7KSA8bs4DnA5xL0FBsaz7uCPbP1Od-pyM3TaYr_NpnydDRb7r7GWr3NjhS_Iw3y9CqWtBnji3a5lW66SvWvDwpC1jSzRLvMy6MH6BiuFpRfVZzlbOhxxfKAeyNp2wl1Qi28ABSy4DGMz5sC7tuggx8rdAHh020wYUSPRkiZ0EcEq944mgOlCNHeyCWcFE68QYiSXK_It6-xxMLndIt_gnJi9ONV2Ow4x4TCXUVGzSEPJv9nVZGACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: فاحشه خودپسند و کثیف جنایتکار جنگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/692784" target="_blank">📅 00:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692783">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
معاون امور زنان رئیس جمهور: پیگیر وصل شدن کالابرگ و یارانهٔ زنانی که به تنهایی مسئولیت فرزندان را برعهده دارند، هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/692783" target="_blank">📅 23:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
نتانیاهو علیه شهردار نیویورک: از زمانی که به عنوان شهردار این شهر انتخاب شدید، بسیاری از یهودیان دیگر در نیویورک احساس امنیت نمی‌کنند
🔹
همسرتان پستی را لایک کرد که عملیات ۷ اکتبر را می‌ستود. او پست دیگری را لایک کرد که می‌گفت تل‌آویو نباید وجود داشته باشد.…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/692782" target="_blank">📅 23:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed-6l0Px291_hTQjipC-ejNFN8J0PIdz5NG8enHlgJy9E5bHxmO_jVF5HyGepAJF1eLZ9xysvaFXUb4pDgiZWV-YMHD0DehObKkxuEgNR1_pZgIRDJZ--At9vJHcHROwxsKkPLuNvXXAuMgYxuyv9yE5i5BhjZ8MrP1ACM5IYiIwTGIl11odlaRDjlA5TSRVcMzWS8GyjVReLIY6nMC3yaocSoSakM06Wf9Jc2YvuHFJZBB71Z-oH4fcNj66cIJ6Hk2czuvX_yZ7XRtKHrufK3bulQ0KLtTfj-OM6ACND0T4opgZvRVQxP5hDnw7ND9Pxe-OrPaAlo76ybjUWvCWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوزان ساراندون، برنده جایزه اسکار، در جریان اعتراضات ضداسرائیلی در نیویورک بازداشت شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/692781" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io4ya4tlCLFcQVUOz5fz6s3uOfyZT4GPTua0UJm4eGPGlcKbtNnypE1dOjDrqozMTteotjvXwWn4bwIVa7MobBa8DTz0N7GNAlBuAumAGtALPCu8oKeHm78oM8NwDJ8QpXAm99lNrkwiJ04vvrJF1i4axBy1d5TD7Gx8V90_tShfBAwFs7ZVInRcU0iqKyIrhJGhTBqX49OGFaRMmyMORkTnsZSmKQSPqOBPtHB1UHI7Cq4SJl-o7JeiSdH__QCtnT39G_bFVsV0OtE3HhPi1-6peHMpFLGC2z608ZIAuq7bFUBkPgMmcIsP2aKjLkXtlB3oLe0uubHAHdIQa7poQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ایکس گلوبال به روبیو: «تنها دلیلی که ما در حال جنگ با ایران هستیم، این است که اسرائیل ما را مجبور به این کار کرده است»
🔹
شگفت‌انگیز. وقت آن رسیده که روابط با اسرائیل را قطع کنیم و با آن‌ها به عنوان تروریست‌های تشنه‌خون و انگلی برخورد کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/692780" target="_blank">📅 23:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7616c58484.mp4?token=iwyf7X4iOR96TY9_r208eoB83YgPEtvwC-oa5rNWPaS4sg8YDLpPCFOee-yF26sypAkPU_6GoHKxmHXXLfduQM7cAwjS9ROVtSpJLwcz73-Zraw1cmTnEOi1Gm6rq1pXqZ5-RvnSTWzPrgVK-Tob8dFw7swcq6h31pmXJC8OZA6nocsmMT2gIJy1pq_bL5VEzPeZDNhA4kFr5AiofKVivWzYXncp5HBLem01roymBdbyzlsrFKo1EtQjxmJaLkcReMkisT__o25UfW4NhgvCiu3fQYCNC7BksKzCCiSp_ykIkBtB51cAdO7E6Z3ogtyliTFN4H0T0XR5K-EyEuDl6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7616c58484.mp4?token=iwyf7X4iOR96TY9_r208eoB83YgPEtvwC-oa5rNWPaS4sg8YDLpPCFOee-yF26sypAkPU_6GoHKxmHXXLfduQM7cAwjS9ROVtSpJLwcz73-Zraw1cmTnEOi1Gm6rq1pXqZ5-RvnSTWzPrgVK-Tob8dFw7swcq6h31pmXJC8OZA6nocsmMT2gIJy1pq_bL5VEzPeZDNhA4kFr5AiofKVivWzYXncp5HBLem01roymBdbyzlsrFKo1EtQjxmJaLkcReMkisT__o25UfW4NhgvCiu3fQYCNC7BksKzCCiSp_ykIkBtB51cAdO7E6Z3ogtyliTFN4H0T0XR5K-EyEuDl6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غذاهای عجیب چین که آنها را خشک می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/692779" target="_blank">📅 23:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=OXo6rEY1k3p0irEf0sUvYy8fTiYkSBLucGTNydtACf3KYGtzBvGHXaZpFKZaI49OeXc0EhaPobRRd1OSmNebUk9qWYdde1JFi-BYH6UgynIqYU3EHYJaSKHk8nZrx9PHcdpPZZSX1rciEodS76LUXbvE0d4-MVgpGI3Bf7MLJzZ9NFWZnBf1bC9hSn5FmIEnZyVz3h0h3GL4WHN-sh_tSUHv7bOaZ5BpU_fW1-FBs9MSorBwgPueqZOtoAEcDadE3Z2hHh1vqAnKsbd2jmX7J86fL1jcxbxROv-wuuKzOdOAcmuBgyDzF3yzdtZwRAMjWuMEoGYbiWj2UpOI4StfzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=OXo6rEY1k3p0irEf0sUvYy8fTiYkSBLucGTNydtACf3KYGtzBvGHXaZpFKZaI49OeXc0EhaPobRRd1OSmNebUk9qWYdde1JFi-BYH6UgynIqYU3EHYJaSKHk8nZrx9PHcdpPZZSX1rciEodS76LUXbvE0d4-MVgpGI3Bf7MLJzZ9NFWZnBf1bC9hSn5FmIEnZyVz3h0h3GL4WHN-sh_tSUHv7bOaZ5BpU_fW1-FBs9MSorBwgPueqZOtoAEcDadE3Z2hHh1vqAnKsbd2jmX7J86fL1jcxbxROv-wuuKzOdOAcmuBgyDzF3yzdtZwRAMjWuMEoGYbiWj2UpOI4StfzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
جارو شارژی خودرو با مکش ۴۵۰۰Pa
🔥
این جارو رو می‌خوای؟ قسطی هم می‌تونی بخری!
سبک، کم‌حجم و شارژی با ۲۰–۲۵ دقیقه کارکرد!
⚡️
اندازه جعبه : 16*16*6 سانتی متر
مکش نیرو:۴۰۰۰ - ۴۵۰۰Pa
ویژگی های خاص:قابلیت استفاده به صورت خشک در خانه و ظرفیت باتری ۲۰۰۰ میلی آمپری
🔥
قیمت ویژه امروز: 1,389,000 تومان
🏠
پرداخت درب منزل
✅
امکان پرداخت قسطی با ترب پی
🛒
خرید
👇
memarket24.ir/product/brief/26903/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/692778" target="_blank">📅 23:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8efda3679.mp4?token=sMscHIDmOk__sEiEbu6uw8Sd97mOYyXst9vMaHEEcadj5aHwFsLw8Z2wz49-agUoTBTrIiM9ipTKWtUzQIkMbXytQhIaSV-yXSjPf9TCallcKTGxfGMGW01CzaUewU8iadBFsRcdr3cj-PXM5CW1jQQg-VmGxS_1QBxOgx2LdQBXtG3gdZM9_QHnStr0DOtxj5bMomPglPQQ_Hly0Pwob9_73us2tovMno-ldtB9-ItLB9wATsmAPdr8BPDgtknRXwN_BZE3h0EsldI4reMo7YSJp6upW6e96h0Sq1LUTc3MvxbUNUHWWBxpwuaQFuG7QOqqmzb6PAW6cEsxjpnvSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8efda3679.mp4?token=sMscHIDmOk__sEiEbu6uw8Sd97mOYyXst9vMaHEEcadj5aHwFsLw8Z2wz49-agUoTBTrIiM9ipTKWtUzQIkMbXytQhIaSV-yXSjPf9TCallcKTGxfGMGW01CzaUewU8iadBFsRcdr3cj-PXM5CW1jQQg-VmGxS_1QBxOgx2LdQBXtG3gdZM9_QHnStr0DOtxj5bMomPglPQQ_Hly0Pwob9_73us2tovMno-ldtB9-ItLB9wATsmAPdr8BPDgtknRXwN_BZE3h0EsldI4reMo7YSJp6upW6e96h0Sq1LUTc3MvxbUNUHWWBxpwuaQFuG7QOqqmzb6PAW6cEsxjpnvSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی متفاوت از اطراف برج ایفل که شبیه یک جمعه‌بازار شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/692777" target="_blank">📅 23:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692765">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAQkR2z80212kK1RwmRw6Uw6M-50-_5JJ0UwobPueKU5P76Qx1P0O-hwU7aPfitZJLsFeJxZO5LgbcpCGbDyan3BdpEzCvRwHUQYzba9uo0yF6miWWk43P-ZYqbsl7p5YWj6Wa-IYbH3wzIvb3GdwhLuK2eVkELWZzZC_EPc2ARUjboPBGb_-XYMvjH6nD2uBY0z_tIuxVU4XQbO5G4dd1S6phkvYy7vkPttZzrUn2BQ0D8x1_MVd_WCheSL2U9BZRG58uTHa_J75HUoFSA2Gk1PRgBjoHlAuMzkV25rw2Q27iV8HzA5I5UQnVxt-wVhLrl10_B1YDCkf0WKid254Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKolCrodTXJMxQWvwyLqieMxVbVLliXfofSzy6jedp6D7dcXVVUnMeeInF9qGHAhtyAWoLBjGbYWGBNqaE6AClkLVu7bYq81MHbG4y47KuImcaj3U8NPNvTdsdxYEcL4MSTCTXilSfFMGwYPCmm_zrxDbGLOH6gOW_5hBMeP2lpzT7oFRXfSAXz-L6i7SYl0AKM9sJWm9je-supxw72cSMFv5cKz2sSC5VNkPTN4QATrhwWb1zta0tmB7lkojGb9oGrOyES5la_iJL0Sc8CULDaJFk5XHn9kyUARjIW2veoV3SEOJVsOx2QKTLU7SUipnsV7l0Db_r9a9KkMhG3qow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DamIdtjili89x683N_3do_F6RK3iD7X6PrXpajKk0ijosP1Jha18EVWXHVZSW21lH26jNno9n-YIgUBThLMLi0wLJmScaa5nNRgchfMKyUjbmj8jRPundEsvnlbtoHa19oDUb11aJHeSxolhTBdCWqH-ve8XS5Mv9wAnwvQU2adQ_yicNw5VcIZCxFPXeU1beZrxTqhI7I0UsqLQOPFSn6cTIKT8Gy83ReifN1DbXTAbqxyH9Uu4Rc0_IkIsKcXw52Zgcu9c8SmkZDB94zbwRDhFiocYgmcworPoNxgVc5Awj5fwxcAA71ru9M7_5Oewi_vjwEmdnGS9y9B4E0b5tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6RutdsdV4W2m_lGzi9pAZM13cw4fUACAOceDSdWGt5oBCorzHa0n7IW32VN59zSwh5ow3Sz64iEurTjvgTsn7JVwY-4WS2J_cI12vrHKzkjJy3eTuhKOpH_cdXLx_p2BEj-gJMjnk-6SJYlCW_RRl-FUVzhmbKsM32Z3cB1pDKyKL-muXKwIVEcbHyjkgwu5Db6B5K0d4muCp9ecVJ6PMtzM3LwyxStlXthECTGgKzLE9DEh9by-vtL9W0tRShFR7txYEXQKAwO2FSVfb05IpM3EP_g0pgsbISEi1MOg4H6wK189xw1lucpc--ftWnW4aJZ0FbGZESHlJ8m-uzSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sv4mWdMMA4KZWI6Rq2LnqtnHxGeJLwLY-40sbaDaQpwBRii1rFzMPiK1t8LxrK4xvYwFbjGzjEZWombSqDAiz5q-0sq6HWhZGFJN1hrXhwEpnOoc3yZf3rIkEEcda5u_RRecE5EhK2UpQ38ek2pkH8qsbwMjvuINub7WQ8Eup9CiIlG4cvi533rgznuo0m8xq3CmM-Gl7v4KkpdP3h1w5dP9opuhcZzatsRyS0TEw8zA5jsS7aJxapgRVC_LShNRwoF5dNH34IyabPemZgVOMymgobpUQbqBVn6OUQX84V9ipPo5Sa8mGnvW0nRTik3oR__qOECKmsNnnOKzEMwx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VY4lZsGAfh07Dx3XyRy_c0eDj5VFAkyZgp7QhGfHY1OIzm0YbLuuV8ZXDNyxgFIXmJkywqjUxcfIRCsUU0V80yvMOJlDk_To_2pPnKUSTdbBOb7V2iwbnsSMWYAF7F9zGR3JkBYH9ftFsF91JL03-li5o4giRlrMvl-GBCE5JA0cOT3KWIy9kPQaeWuEY8R6M9QLvgYyxz-tDkiMxLxtCri_yM55gMfMrnaDX79l0HpMKC9qs_Iqujix0hNd9En0uS-6quTmIqFAmyar8rg_ytHG64YdwJM8-a5HiTnljgQiRR7RVcG2e6eeo6dpJppHeW5VPInyC08tB6BrO1I_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUlkeVUfDiKaePmFuv7WC1YcAiVOJ-3m6aznPWhwUbjhxD0CVU21KQnkCSxWl9tyf-quYC6nTt_ADF0n2Njjb_quy79UdmClbapOg6LNOP9UaHZNNsOnYgyA2-89h3LBmkHsd6quNzMhHH9HjGB21HnJZKxuUfNi0ZuEgyNpda4dyqBw6NhXKUyFvA91Fkwr7oXe9Hwy2PXUKuMC9AY3my0t81Q_aLsIm96t6ZX97Bd7gEIOjoGS7014lSl5iVm6x-rHRTkPgN7PZwg52SaTbMmnUj3YC5L23Y54pEB_8eJUrnYwmMtM6X63QLFm0TSzOiOybtG79FeOFshYryAP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTfB0IcLX6XfjACUT5jtsGipoOD6gdTYycRdAxyrb7UF0y8iyrqj01MzdO7p2gWqN7c9CvyYBq9-DcRgHBb5farMSSZbjI0c_9l3FD3QopXA-pEfXbumP7bOSKQD0IWFIxQ-og5xV9VuEPHMATU64xkXh5BXztUEixa7RpZZhcOnTpRWWQFiZ2BJDIZ5i6N8LBLdn77D6-a-ur0l5H-WhEzjlyg3fUGWywCh-vxtO1LFrKXL8Ds8PBZOVfqPvrTIgE2NsEhvJy5wLBuFK1PgzS1xX99St--PzRa2WsKXWdYj87G-j2244ngpOGXbOdZ46qknFvN3PiojbCcLtqJiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4lBfJqRlgPKLLwhIYrCo_yaNPnNSIJjX0GDK7oy8PZa5tWc9l5xSCqS9051urOslSNLNTf8R4CS4I_3a3LlzIdyFu9N9X0Y1exB6n1Qe2HAGNegya6sI6khacJkSzKgy0X0oI7w-1eJZE8qKDL6hlCTXW6immPaob_wQ797ep1Z839pSR05SEbNmklZEtO0v76pwkhfY4oFp78SM5fN8I7zm5Qwl7pkFR5qfTYE0uWIpneXHK2S4sa0z2YlZdme1QKWkX8QYALXtbXBrQnPqW3GfuRA5rpuLzfX9WWi9q0JtkfgQbuPaR_8JOii6bdeTaNLJOmIIVoFBJIeTNvBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQWmJIBNvAbL5jvRPQoEHvT359cbjd9zK9DB0WUfAbCYc0ntC5wZpyjlcig-bfEFxVRIRZ4TOw-jxk1dB_3-Svtcy4mpB0qChAnQwL1H9IAmt0hapCc_HkjcB8XnNiZfM5FCVZuruR2R5ImpcmQc52WoPM2e9pE60898V9a5cPQ-rqcSBx0DuN5OmUMe_36kG00MkD14vwrd02TY-TwmjK5ip7F_T6KhXpUoEaVRjrX9ugwbxMm7v3fxRalkTzTkdqh4hEdee6Ik3h9IL3lpF9XGmEivvzBD5_X6O_kQW37HbIuqdLBkKxcbVpzmA28_mMigl6pYOgoJjx-oiC6Fgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و چالش‌های  تأمین داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/692765" target="_blank">📅 23:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692764">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
در این کلیپ توضیح داده شده که چطور کوچک‌ترین انتخاب‌های ما می‌تواند در عزت نفس و سطح استانداردهایمان تأثیرگذار باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/692764" target="_blank">📅 23:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692762">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
بلومبرگ: فرانسه برای حفاظت از پالایشگاه نفت عربستان سعودی، کمک‌های نظامی و نیرو اعزام می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/692762" target="_blank">📅 23:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692761">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه چهارم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692761" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ چهارم: تفسیر دعای فرج
🔹
دعای فرج به‌ عنوان یک سلاح و ابزار حفاظتیِ طراحی‌شده توسط خود امام زمان (عج) برای این دوران بحرانی معرفی شده است.
🔹
دعای فرج  ترکیبی از «اظهار وضعیت وخیم (شکواییه)» و «ثنای الهی (اعتماد به قدرت خدا)» است.
🔹
ما انسان‌ها در ظرف «زمان» و «مکان» گرفتاریم، اما حضرت صاحب‌الزمان (عج) از قیدوبند زمان خارج است و به علم لدنی دسترسی دارند.
🔹
محاسبه نفس، گوش ندادن به «صوت دجال» و مراقبت از نیت‌ها و کارهای روزانه، لازمه‌ی عبور از فتنه‌های آخرالزمان است.
🔹
راه نجات از رنج‌های دنیوی، دست کشیدن از تلاش‌های بیهوده در عالم ظاهر و اتصال قلبی به امام زمان برای صدورِ «فرمانِ گشایش» در عالم امر است.
🔹
امری که خدا برای زندگی ما صادر می‌کند، توسط حضرت ولی‌عصر (عج) اجرا می‌شود.
🔹
رضایتِ قلبی، قوی‌ترین حمد و شکر است که راه را برای گشایش باز می‌کند.
🔹
در تمامِ لحظات به حضرت صاحب‌الزمان (عج) تکیه کنید و بگویید: «خدایا راضی‌ام به آن چیزی که در عالم امر برایم رقم زده‌اید».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/692761" target="_blank">📅 23:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692760">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABMvX0sQivCtEaq84cjRiYe-tbNrXmivb-bcOGkWZY8JkcQylieLSQJuaKZU8Qfqo-hOp4YNElJzpe9gPa6jf20fCF50fkeLGLFJ34Fo8e1flZYYKz-JO2zyLwHTuPiz_YPS84zGa8ftk7ESJ8YV3Wsu8zMMU-SiDUgP0LKN0SSwZVkZgYodDWQ3jHcfDUZlABBKZZmty3EwkUu2lpyY-79Q9tkKt0U_YK0e2FGsWwgUJcVj9FZwOpr3QC1zXDKReHeUauYy9dRfJAnjmvJ-7-x9nVNrsqiPLbOHqHJp9tzWI9nTPcqskTqnXgdyZWyBbAWshBUkUvpJdvck7ntWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: مشارکت اروپا در تجاوز به ایران بی‌پاسخ نمی‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/692760" target="_blank">📅 23:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692759">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtiijgaO-XK_3a9_MXOj1omz9njLlW9c7tYBELMml7UsSgSmAuTHJehtfpBVXP4JSaaU4gipkB68XlCL6gcr2VinHaX1R9-PiTyl3P2d7MBGepSYiRn1SJYFGCN7j0jw9aLkk3JwAjK5sBF3Cc3IekhInkxHkDf1kIP8xrwDc7wkRM5qU4Fsy7jBzpVKW9KA5bCt-r5BaCXo5rDEiZ1DHur-Dx4anBq-zIOOqh2HJt1bix7Xwlf7j2wH1nO2RnqZFBO0XxBFy7CetrUzoSo6z3awNmfgviOZMA2LfCldOqY1ZtFFFfNNd7E3VDeho8x9q_Ur5Ndnawh5PT-apsFbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☎️
«با ثبت اطلاعات مرکز آموزشی خود در سامانه ۱۱۸، کسب‌وکار شما همیشه در دسترس خانواده‌هاست.»
🗓️
از اول تا سی‌ام مهرماه ۱۴۰۵، فرصت معرفی مدارس، آموزشگاه‌ها، مراکز آموزشی و کودکستان‌ها در سامانه ۱۱۸ را از دست ندهید.
@tci_iran</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/692759" target="_blank">📅 23:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692758">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe0cd02cb.mp4?token=AtdReLnDW5NSJHrp3MTcswODkE0qyq2urMCGvDTNs0kuRO55cGNeFry30cvLqFhIwRfGdg9BSHOqu0K3wyId3IVXM6CMOkJBVKoUcqzZIU_fCohsU8ZN7RDk55ZEhzmpN8kukd8Tfk0IIq6r9DaM6D5BtW9oHPnAANU5ipk5sZE3TYFaFGYREIGI3H3YnN1XKz7TlbUvVNoMqRvhdOrNGjVFMeafaa_cH0hjFZEZYr8bOFhreVYtk7HbQxJgK-7l9y7Gyj_dqPKghA3QcldrFdBSz7Go57-aZ3P1Og7dmLRquic1mIil4CD8V27m5T13QRLhcsJAw9mSxz5OaxWrZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe0cd02cb.mp4?token=AtdReLnDW5NSJHrp3MTcswODkE0qyq2urMCGvDTNs0kuRO55cGNeFry30cvLqFhIwRfGdg9BSHOqu0K3wyId3IVXM6CMOkJBVKoUcqzZIU_fCohsU8ZN7RDk55ZEhzmpN8kukd8Tfk0IIq6r9DaM6D5BtW9oHPnAANU5ipk5sZE3TYFaFGYREIGI3H3YnN1XKz7TlbUvVNoMqRvhdOrNGjVFMeafaa_cH0hjFZEZYr8bOFhreVYtk7HbQxJgK-7l9y7Gyj_dqPKghA3QcldrFdBSz7Go57-aZ3P1Og7dmLRquic1mIil4CD8V27m5T13QRLhcsJAw9mSxz5OaxWrZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رپ سخنرانی پزشکیان هم ساخته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/692758" target="_blank">📅 22:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692757">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q63wTA2sOF7Fk8A6hRFxQMRqNGeY8u4b9JQA1exfSRPTKXz_gl1kwUtgCJxKRppgm1dH34Xwkvj6_PvIPj9gAm_6glVRvN4RXhL8FgfnOTkmyXFah6x2JvfvFSMf55P8tJnur8c5NlbHpfV0Q9k62UIq5MoFJH2tJh6SuAbPPqIVJupc0dAKqXp7wd4UU-OhbhsgEI1nyQMw8i-44SFnwdsi9xk79Jiee42Wi1wU53DaHV75bBIr0KfyyBvGE6BVXD9oKdqQ1ui6xXmHAQf4jGHgqikwQd91d-f7vUes4PuDwZktMf_53TNPROLDax9CXruz-DnqdYmiQ7D766t1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکهٔ فاکس نیوز، که محبوب‌ترین شبکه‌ تلویزیونی نزد ترامپ است، در جریان سخنرانی نتانیاهو، دوربین خود را روی میز ایران و تصویر حاج قاسم سلیمانی متمرکز کرد و این تصاویر را به‌طور زنده پخش کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/692757" target="_blank">📅 22:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692756">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نخست‌وزیر رژیم صهیونیستی تلویحا از برنامه‌ریزی برای آشوب و اغتشاش در ایران خبر داد
نتانیاهو:
🔹
می‌خواهم یک خبر خوش به شما بدهم؛ اتفاقی باورنکردنی در ایران رخ خواهد داد. روزی که چندان هم دور نیست، حکومت ایران سقوط خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/692756" target="_blank">📅 22:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692755">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e2919c55.mp4?token=Xe9V61cr1eN4NA7Rg0o57oZRYIK6aQXGILsBTB3UKARwjZVBq8NDRlk0lemMVr7tGkGiYPW3tCAUV97OA9J44YNg0gNb6iaKehtuH9-pAE8orfsW57Yd5uCxwV7vGMWwr70bj5B5ZXSVznDsfjRSpZ8t-AB13Yg0As_xHc1Al9j4NgAheoRksAYaaZpOZdqBgZ4-lZnTmSFiKAoHRcLhIPfbvFOBwAwC9ivaKPiJDi7bpXbgPZjJWvC9FKjBY2LhSVwE2l3K2nX5QMOn0cMkn7oYlK2-ZjQJRkawKyXrS2rfGNo3WcAkygUMuwIpQwAny69zPmWaDMcHFIpboXBZvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e2919c55.mp4?token=Xe9V61cr1eN4NA7Rg0o57oZRYIK6aQXGILsBTB3UKARwjZVBq8NDRlk0lemMVr7tGkGiYPW3tCAUV97OA9J44YNg0gNb6iaKehtuH9-pAE8orfsW57Yd5uCxwV7vGMWwr70bj5B5ZXSVznDsfjRSpZ8t-AB13Yg0As_xHc1Al9j4NgAheoRksAYaaZpOZdqBgZ4-lZnTmSFiKAoHRcLhIPfbvFOBwAwC9ivaKPiJDi7bpXbgPZjJWvC9FKjBY2LhSVwE2l3K2nX5QMOn0cMkn7oYlK2-ZjQJRkawKyXrS2rfGNo3WcAkygUMuwIpQwAny69zPmWaDMcHFIpboXBZvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رئیس‌جمهور چین به توهین ترامپ به بایدن
🔹
در این ویدئو، شی جین‌پینگ، رئیس‌جمهور چین، با خنده به پرتره‌ای که دونالد ترامپ از جو بایدن (با کنایه به امضاهای خودکار) نصب کرده بود، نگاه می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/692755" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692754">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCh8yzx_NuepOKgUF58jrfYCO5IZDnMCvE2AvXTKoc3EJvwKkqxIwrXzI6605_mPmqMPKkQtRlxLLrWFV8Q7M_v6NgpBRQpJJQ-1Irc7ILZFW-idwHznoPnrcFkje3eGj6JSpz6VQAPhQ96AaZCMDg2bjwOpctttUdnusVsAhHrnyVwEtzwaHBFr5bviYcGY3Qf7-fVt51QK2iokYBYBpEM1Etd3j22K3B5ASCzYKuRvTMipJoyHpDGbUNU-Po8PoyJM8it020ifNrOaC0xEXIfJdZObXEuXo6gRlgYMi4a9ZHQ40LhR-_Xxdl8d4jEQFp0vMeev-H0d-N8Jf4R7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال سیاسی آمریکایی: هرچه بیشتر با منفورترین کشور روی زمین متحد بمانیم، اعتبار جهانی آمریکا بیشتر به باد می‌رود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/692754" target="_blank">📅 22:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692752">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01569f344d.mp4?token=OW3tqAs__ts9xR6b2-ZgVyG_N5zfrvFBNKlpjPwJjVJHnEbDiW_mEgTbFVfL8x8QD-0EZuuWLNU7qAmLftt71A7Um4oNjQfBAF6Tyay08fGzTIFjplt8Kgsu8qtHCpggHF4wIoLkl8Xr8_ciF09t0i8PwO6zEO8xEUkgA5r0kDyjgxnYyoI1brQjc8VzWgxN1sP61H8Ydd3QAcqRnvrXLf4ta56JSNJvTfiSiW2w93g5U5zPtxOcK9II0PIP6OaotR20_j4MihUS9GP9-VIK0MGcUWM3FIqYRS8aIsz6e9_tQLBME_jqMcP0lYdXMBQq0YHe3KO8KUjtlI0_pp5fVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01569f344d.mp4?token=OW3tqAs__ts9xR6b2-ZgVyG_N5zfrvFBNKlpjPwJjVJHnEbDiW_mEgTbFVfL8x8QD-0EZuuWLNU7qAmLftt71A7Um4oNjQfBAF6Tyay08fGzTIFjplt8Kgsu8qtHCpggHF4wIoLkl8Xr8_ciF09t0i8PwO6zEO8xEUkgA5r0kDyjgxnYyoI1brQjc8VzWgxN1sP61H8Ydd3QAcqRnvrXLf4ta56JSNJvTfiSiW2w93g5U5zPtxOcK9II0PIP6OaotR20_j4MihUS9GP9-VIK0MGcUWM3FIqYRS8aIsz6e9_tQLBME_jqMcP0lYdXMBQq0YHe3KO8KUjtlI0_pp5fVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از پیوند قلبی دکتر پزشکیان و رهبر انقلاب
🔹
سید ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات با انتشار ویدیویی در فضای مجازی، روایتی کمتر شنیده شده از باور عمیق دکتر پزشکیان به رهبر انقلاب را بازگو کرد.
🔹
دکتر هاشمی گفت میان این دو، نه دیواری است و نه فاصله‌ای، آنچه وجود دارد، پیوندی نزدیک، باوری قلبی و رابطه‌ای عمیق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/692752" target="_blank">📅 22:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692751">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن از انجام دو عملیات تلافی‌جویانه در پاسخ به حملات مستمر ائتلاف سعودی خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/692751" target="_blank">📅 22:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692750">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=P5e7W9R8gkBR4FFOHjKMqK1TMz-gZG0w7T8zbHeoPo8iH0R9kPp9pBL3fTeEGQDx2VT-4bNOAzMi7sq9YLSPgBDVdMP-6vuzO8TB5MalMXaYTBWLt6XlvZw4XjVYqnmDaU1TMtOWlsbaqFaMVxC6ordx39xtA3DvajIa-EH-50MFE3ly4F4qtTufp3TZsqQdiAKanz4nNkEUygtmPGsUidwbg4284FXt9oiZisBHfhH8e3JgHMZAjsYSlQuBOwaUzXX5eDkVDlUfL2mhjAnYZIKFg_5iKz6m5qrrCaOqJPY-BWMOhXidTapf0M0FNzanOS-dUVqXXWnxE8prvTbAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb8237eab5.mp4?token=P5e7W9R8gkBR4FFOHjKMqK1TMz-gZG0w7T8zbHeoPo8iH0R9kPp9pBL3fTeEGQDx2VT-4bNOAzMi7sq9YLSPgBDVdMP-6vuzO8TB5MalMXaYTBWLt6XlvZw4XjVYqnmDaU1TMtOWlsbaqFaMVxC6ordx39xtA3DvajIa-EH-50MFE3ly4F4qtTufp3TZsqQdiAKanz4nNkEUygtmPGsUidwbg4284FXt9oiZisBHfhH8e3JgHMZAjsYSlQuBOwaUzXX5eDkVDlUfL2mhjAnYZIKFg_5iKz6m5qrrCaOqJPY-BWMOhXidTapf0M0FNzanOS-dUVqXXWnxE8prvTbAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه فاکس‌نیوز تیزر مصاحبه رئیس‌جمهور ایران را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/692750" target="_blank">📅 22:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692749">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBOpnEpkukB-tjtCOc5KSkj4SRRmY27bKr1bBazMJbyzcUH1BdJFW3Xa0k9TqGaFdJ3IE_hXfEjMzYDuA7lxQuSBGb0TcrJsr5aPmAQWo8IMhLge8YXbnA8qiOt142JT1z40stDcQfUz8rs9Kwq2wwZMdIO55z2dASrwClOChMdyP2dv0-iLYGFsQYLUK5sGoy5UyscsWmVGZCEAQyfyLmFRZZmNVI7zPtu4Okt75EqVJVp80YlfZjA5NRHHjyn41fd1i7xUtrEAydCcvjPTtxbroiiaBeYCLhiUF8345QU7YfH_-FhBvf7wxWWZQF4XYME8YXkZL92fU0uE8T8rPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون: در جریان سخنرانی بنیامین نتانیاهو در مجمع عمومی سازمان ملل، سالن... عملاً خالی می‌شود...
🔹
این پیام نسبتاً روشنی است که اگر اسرائیل می‌خواهد روند افول جایگاهش در سراسر جهان را معکوس کند، باید رفتار خود را در عرصه جهانی تغییر دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/692749" target="_blank">📅 22:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692748">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMfE2ox-eYOG1Jv96AdWfVd2NOlJXP2FLNEeplgHD9I2eKy9dBmiSf1p69BGbZm13cf4ILZXTFBZeeK_0mebvp2FRQ6537iEJkfHb5kxDuha0mX3WNwj5tZdXxHSvCTxBG5CWeCDqkOMSR03F8uwRRYaDjHlE61p4cFBFI0dCP997M8_9SYDOeqg1u70PykCFzbGBHKcUnqV1ZhR07kI7wQdeS2k9vWl60FVJ4v-gaHkXlDwFX7vPTah0ZKBJs7ND_lKfcnJotgn2VjRukgyh5zaXHnjQrxHsLSc8Fpry3DCdEABMOqbR8HEUjK-efUfarPWPXDEqvNtcaErYZ_rRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۷ هیئت زمانی که نتانیاهو سخنرانی‌اش را آغاز کرد، سالن را ترک کردند
کشورهای عربی — ۱۸ کشور
سوریه
فلسطین
اردن
لبنان
عراق
عربستان سعودی
قطر
کویت
عمان
یمن
مصر
سودان
تونس
الجزایر
لیبی
موریتانی
سومالی
کومور
آسیا — ۱۴ کشور
ترکیه
ایران
پاکستان
افغانستان
بنگلادش
اندونزی
مالزی
برونئی
مالدیو
میانمار
کره شمالی
ترکمنستان
ازبکستان
قرقیزستان
آفریقا — ۲۰ کشور
آفریقای جنوبی
سنگال
جیبوتی
آنگولا
جمهوری کنگو
جمهوری دموکراتیک کنگو
لیبریا
اریتره
چاد
جمهوری آفریقای مرکزی
ماداگاسکار
نیجر
بوتسوانا
اوگاندا
لسوتو
اسواتینی
گینه استوایی
موزامبیک
نامیبیا
کنیا
آمریکای لاتین و کارائیب — ۱۷ کشور
سورینام
پاناما
ونزوئلا
آنتیگوا و باربودا
بلیز
باربادوس
کلمبیا
دومینیکا
نیکاراگوئه
پرو
سنت لوسیا
باهاما
بولیوی
کوبا
گویان
برزیل
شیلی
اروپا — ۶ کشور
مقدونیه شمالی
سان‌مارینو
اسلوونی
بوسنی و هرزگوین
اسپانیا
ایرلند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/692748" target="_blank">📅 22:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692747">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
وزارت خارجه عراق: آمریکا پایگاه «ویکتوریا» در فرودگاه بغداد را به عراق تحویل داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/692747" target="_blank">📅 22:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692746">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نتانیاهو: رئیس‌جمهور ترامپ بزرگترین شریک ما باقی می‌ماند زیرا او با نهایت شجاعت در برابر خطر قریب‌الوقوعی که متوجه ما و جهان بود، ایستاد
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/692746" target="_blank">📅 22:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692745">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtpSdZNL2mPR6-cGanna3twOeEfhozrrM16FayiuVQNVGbLkyE93iK7E6wkkfXkSsKDBlELnTOekiPYI8Qseob8g7aQ_5HVDP4U6ANh5zx2bshx2-55rKmwDnr3jC8ORC2050of64NsU3dkCOoRI3DoieRfcIbCx2cBKQ-THsbl40EGjtjN7mcBk3fulCuhkhzOLacsS1oTUMclVoQaNswEpbFUYfqANiVZpDMlW1A0BJpJc4r_LczLGB57WEUXDn6pXhSmrbB7Je8iOGEcr1l3lmaHXLGBB9JIsziPIpRSKLujGG9vfi-GaccueF1p0D5m4awUgLSI0doszRFD28w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از سخنرانی نتانیاهو برای صندلی‌های‌ خالی‌ سازمان ملل
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692745" target="_blank">📅 22:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692744">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
نتانیاهو یک دستگاه آنتن استارلینک با خودش به سخنرانی آورد و به دبیر سالن داد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/692744" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692743">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111bb640ed.mp4?token=WKSWYI2bQt9Zt0ZaEF1q15-rG4SvNY6eegXAI7Cfl1ArgPNABwspckTD-VDcEWgHz_jYszPBWyho937WKUouJJFAs_oAjwTcMNg1G7aknVPBHvvd1npk0_X4l2eCkd1p-v8Lb8MI2x-14--hHkrtR7-gUatmuB_v1ly6j9mylbGXysmy1_M2ydMb1Vuqj4yVacVDK5NM4F3Q5vFzCFectS45mnBrBt99gYuYUxB1gF6R35UHmgp6dszsDCgbI3wtz3pOFlBiA7yIbyCLuEME7s9ZfjU2Aa--5HGit4IrILR4n2yOgqoUG10vykGPwJ46oR1UjrshZuvd813KuxfInQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111bb640ed.mp4?token=WKSWYI2bQt9Zt0ZaEF1q15-rG4SvNY6eegXAI7Cfl1ArgPNABwspckTD-VDcEWgHz_jYszPBWyho937WKUouJJFAs_oAjwTcMNg1G7aknVPBHvvd1npk0_X4l2eCkd1p-v8Lb8MI2x-14--hHkrtR7-gUatmuB_v1ly6j9mylbGXysmy1_M2ydMb1Vuqj4yVacVDK5NM4F3Q5vFzCFectS45mnBrBt99gYuYUxB1gF6R35UHmgp6dszsDCgbI3wtz3pOFlBiA7yIbyCLuEME7s9ZfjU2Aa--5HGit4IrILR4n2yOgqoUG10vykGPwJ46oR1UjrshZuvd813KuxfInQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس نتانیاهو از موشک‌های بالستیک ایران: خانم‌ها و آقایان، شما اینجا در تالار مجمع عمومی سازمان ملل نشسته‌اید
🔹
آیا می‌دانید اگر تنها یک موشک بالستیک یک‌تنی به این مکان اصابت کند، چه اتفاقی می‌افتد؟
🔹
آن موشک کل این مجموعه را نابود خواهد کرد. در واقع، دو موشک از این نوع، سازمان ملل را به کلی از بین می‌برد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/692743" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692742">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5d82671d.mp4?token=NwoYk1_wqRtjs3HZIhOKFX4f7ynB-v8TM4WCJ9iA3EJcOnKddPDUqyxPDjosPykjlmF3IwgGwCaGpewg9tqMgng7HctRWthlDjE2QXTn7yDxTFdK9fyMT_8FlsMcJ9woywjcbBsFS4q0eK2_izycUYQHXNPEiiSSgiggL9mWN_9Hz437xozmVFJmI53APvf8MhUoz_ut56sHBoquB6kRncpZomLkqNWHY-w2GvE8jRlm472pzyN6ToU_dokJC5o4SuKePjg-xgBy7lIqIp4FoN9OcZtun3yI0S1dv7_xWKNY-YsraLZewMbjshu98WTzK_inwPbbLUuwi3XkckmzBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5d82671d.mp4?token=NwoYk1_wqRtjs3HZIhOKFX4f7ynB-v8TM4WCJ9iA3EJcOnKddPDUqyxPDjosPykjlmF3IwgGwCaGpewg9tqMgng7HctRWthlDjE2QXTn7yDxTFdK9fyMT_8FlsMcJ9woywjcbBsFS4q0eK2_izycUYQHXNPEiiSSgiggL9mWN_9Hz437xozmVFJmI53APvf8MhUoz_ut56sHBoquB6kRncpZomLkqNWHY-w2GvE8jRlm472pzyN6ToU_dokJC5o4SuKePjg-xgBy7lIqIp4FoN9OcZtun3yI0S1dv7_xWKNY-YsraLZewMbjshu98WTzK_inwPbbLUuwi3XkckmzBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف نتانیاهو به جنایت در کشورمان با همکاری آمریکا!
🔹
خلبانان آمریکایی و اسرائیلی مأموریت‌های مشترکی را انجام دادند و دو کشور برای بازگرداندن گروگان‌ها نیز همکاری کردند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/692742" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692741">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: نتانیاهو برای دیدار با ترامپ در نیویورک تلاش کرد اما موفق نشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/692741" target="_blank">📅 22:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692740">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
اکنون رأی‌گیری سنای آمریکا در مورد قطعنامه اختیارات جنگی ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/692740" target="_blank">📅 22:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692739">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d7b5c9e7.mp4?token=qc8ViEx7ihXnatnvMtablgMc5p7cTGHUp79PL8p8md2i9w3twoe9d5WWSNMrOqxuQsM3BmcOUJcoml9NRUn9YiYl6qGqUd9NSl7BFt1my7FXqHK9cIngrmr8eZBtss5qpKYaonl_nhQujXksDbrwBpnX0bN4cEjKyLet0MqFrMmrjZi7JaygCI_FwdYgigFvIncj7MJ6N0VnhuS_Fu1bgPzTfV_C2RTVPjfSYJbgYbuM059V_7Rrw2DO-GAYPRb3Ps5_RAlvG_5BTDEZPwo2kg0qqIfhefZs5-tVlmdj-AkwW09txO4yVbKVWBGF7_My4_iw4_-b9L6TE0OOeJr4BYRKIRwgWFoOywkNZDtc_h0go_fuewIgi8665iK47-5Pp39XC7nyBgpLXxQwvn8UXmSZHSP4n0TbzRGJvAVNY0i-DkGniz2L3ytV-f1k-OulJ6_xbDyRCDZRu5X9Tu34I5MlqjleRYNM5mwTOI2Gp7XVooJHP_t7cQ_QpWDfURr9jR7nfYqpnKeHsdfkbHlKdTv4UKsUx0yVhwHJXYI0U47LbyBuWqG2zsYvpKDJyhCvirFOXOfuhVrsHL-n_9oq-kNvVX-UCRTlJTTEaqMZ9VvlHp_gdFy0g6MvQxB-Fl-NvpRNIR7KtIxJ3RXJFpbSSLo75NVHjvlBjrP08MTeooE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d7b5c9e7.mp4?token=qc8ViEx7ihXnatnvMtablgMc5p7cTGHUp79PL8p8md2i9w3twoe9d5WWSNMrOqxuQsM3BmcOUJcoml9NRUn9YiYl6qGqUd9NSl7BFt1my7FXqHK9cIngrmr8eZBtss5qpKYaonl_nhQujXksDbrwBpnX0bN4cEjKyLet0MqFrMmrjZi7JaygCI_FwdYgigFvIncj7MJ6N0VnhuS_Fu1bgPzTfV_C2RTVPjfSYJbgYbuM059V_7Rrw2DO-GAYPRb3Ps5_RAlvG_5BTDEZPwo2kg0qqIfhefZs5-tVlmdj-AkwW09txO4yVbKVWBGF7_My4_iw4_-b9L6TE0OOeJr4BYRKIRwgWFoOywkNZDtc_h0go_fuewIgi8665iK47-5Pp39XC7nyBgpLXxQwvn8UXmSZHSP4n0TbzRGJvAVNY0i-DkGniz2L3ytV-f1k-OulJ6_xbDyRCDZRu5X9Tu34I5MlqjleRYNM5mwTOI2Gp7XVooJHP_t7cQ_QpWDfURr9jR7nfYqpnKeHsdfkbHlKdTv4UKsUx0yVhwHJXYI0U47LbyBuWqG2zsYvpKDJyhCvirFOXOfuhVrsHL-n_9oq-kNvVX-UCRTlJTTEaqMZ9VvlHp_gdFy0g6MvQxB-Fl-NvpRNIR7KtIxJ3RXJFpbSSLo75NVHjvlBjrP08MTeooE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف نتانیاهو درباره ۷ اکتبر: در آن روز ۱۲۰۰ اسرائیلی کشته شدند
🔹
اگر این رقم را بر اساس جمعیت مقایسه کنیم، معادل کشته شدن ۴۰ هزار آمریکایی در کمتر از ۲۴ ساعت است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/692739" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692738">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نتانیاهو: ما قانونمدارترین در دنیا هستیم! / شهرک‌نشین‌های ما مورد حمله قرار می‌گیرند درحالی که قانونمند هستند!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/692738" target="_blank">📅 22:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692737">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نتانیاهو علیه شهردار نیویورک: از زمانی که به عنوان شهردار این شهر انتخاب شدید، بسیاری از یهودیان دیگر در نیویورک احساس امنیت نمی‌کنند
🔹
همسرتان پستی را لایک کرد که عملیات ۷ اکتبر را می‌ستود. او پست دیگری را لایک کرد که می‌گفت تل‌آویو نباید وجود داشته باشد. شما از محکوم کردن آنها خودداری می‌کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/692737" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692736">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نتانیاهو: اردوغان دیکتاتور است/ آخرین کشوری که دروغ‌های یهودی‌ستیزانه منتشر می‌کند، ترکیه است. او می‌خواهد بر سوریه مسلط شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/692736" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692735">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd22202d3.mp4?token=JCMm2gFPGPSvs8XrOlpLVsF5s2BMm0txOTqq9VI5MiGXVprc4idEPUXn3_fPHVcsI2b9tNu9-vnHE3O3r-pzgt4SYHlUqKQZQ0U4JPe8oTnFpU2aekPqFkXgDegPbcp_Oo1crhGbUzYhd-BVbSVfdxxqIX6Zf_0uQbHpHWeuPBoLiVT8jEgD_FrPMk3PoU2rBxlV21mAudm8xhEDq_XLxLzo0DmLJPq9DgXc0MH29C89ODtsZtf4JiK6ppwf-FRwZNX5Dw2zck0j6gUeajfd_VuyBJlK6OPl9OdU9sSTCjD0GRsJ_jVMIyh_GGdQ3BmawNo4Vf9W7KM2CzA5FK24MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd22202d3.mp4?token=JCMm2gFPGPSvs8XrOlpLVsF5s2BMm0txOTqq9VI5MiGXVprc4idEPUXn3_fPHVcsI2b9tNu9-vnHE3O3r-pzgt4SYHlUqKQZQ0U4JPe8oTnFpU2aekPqFkXgDegPbcp_Oo1crhGbUzYhd-BVbSVfdxxqIX6Zf_0uQbHpHWeuPBoLiVT8jEgD_FrPMk3PoU2rBxlV21mAudm8xhEDq_XLxLzo0DmLJPq9DgXc0MH29C89ODtsZtf4JiK6ppwf-FRwZNX5Dw2zck0j6gUeajfd_VuyBJlK6OPl9OdU9sSTCjD0GRsJ_jVMIyh_GGdQ3BmawNo4Vf9W7KM2CzA5FK24MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاتل بیست هزار کودک غزه: متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/692735" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=YSgkWl1lHn5E4hT6dbWEybqiBFoYlvxT5oTjQSRjqZdXyOauX7y2r9XdYv-jsp6uSdqdrTMXjWeUaAf_wrDA9MD34AQl9F3CI3yPmPVcpabLjoAOPGwc_1qDgg5xvNTPSYiGZ4Un2xAfbPOQjpgidYz5AB2N_Zobk2TETAe-CKcaD1hNtOg3NzHpIsnQLSUInwEk5HyEV3kYcNH8wzl_wQjH6OJSBDQ9MrdMFgfaOgxXzVomtixaRoWRBThPCQwmdH0Dm7Tr32olcHTKzir8OQw1Q383qbukR9rVyX7vYIqCWj0vRk9ouxU9PKvQl8SzUDHyzwp6zQCk_evz8ZovBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=YSgkWl1lHn5E4hT6dbWEybqiBFoYlvxT5oTjQSRjqZdXyOauX7y2r9XdYv-jsp6uSdqdrTMXjWeUaAf_wrDA9MD34AQl9F3CI3yPmPVcpabLjoAOPGwc_1qDgg5xvNTPSYiGZ4Un2xAfbPOQjpgidYz5AB2N_Zobk2TETAe-CKcaD1hNtOg3NzHpIsnQLSUInwEk5HyEV3kYcNH8wzl_wQjH6OJSBDQ9MrdMFgfaOgxXzVomtixaRoWRBThPCQwmdH0Dm7Tr32olcHTKzir8OQw1Q383qbukR9rVyX7vYIqCWj0vRk9ouxU9PKvQl8SzUDHyzwp6zQCk_evz8ZovBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مضحک نتانیاهو‌ جنایتکار: اخلاقی‌ترین ارتش جهان، ارتش اسرائیل است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/692734" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حمله عجیب قاتل غزه به یکی از شرکای مخفی خود: قطر "مبالغ هنگفتی" را برای تأمین مالی نفرت از اسرائیل هزینه کرده است: "هدف آن‌ها کاملاً مشخص بود - شستشوی مغز جوانان."
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/692733" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhRtz-3R8_GmtB7sazWgJXZ1LZ8qat0gUyNUZ11xCexX3wAXfj9Vlbfrq8aNWXB9ar1DexDO5vVRfDSSe0jaVHz1_ABGUDbjQ9lQFPgyAJ_kFOjl8typlz1sihn44u0GC9KdozNl8QQ90ECQv-LcTGcN5SjXrUoUVJMPyRTnVQ81wvZ-OPyhe9hsk4vOVlPdd13toFIpt9_KM_G9Ad_4yOb4psaYJgDrTLeh31GqRD06XcFgZW93xKMu6jumEJ9AC2CJbHZT8QN1HTh9eCwFtEWjFVm656TF2EOyJl_7JeUeZ_p91Y0rIwbSLZxsCA8inKiqyOyEoIk_BBom2egi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو یک پیجر با خودش برای سخنرانی به سازمان ملل آورد!
🔹
وسیله‌ای که منجر به شهادت و نابینایی تعداد زیادی از کودکان و زنان لبنانی شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/692732" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
گروسی: با طرفین برای بازگرداندن دسترسی به تاسیسات هسته‌ای ایران همکاری می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/692731" target="_blank">📅 22:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c840c0f046.mp4?token=qT8N7uygAh5o_a9HU3QNz7YeFQkbNJkJ09lDC3fBnFMIiMpyOWuLNFTZrX3APfBSSSkym0EL4EAEafgRKBfrDTEoztYiEN40Wi_Vs2TLx5nZ_eNy7-zCC1KI-CeTOV_7nLRWxnndoz_cAZJ5YdF4IEDDHA8NWe5DnEzozyZd-YhGHJcgNxEs5txNVXAUzYYCStFyyISJyz0ulz40kgpI2MY39IrxGBH5KXGw1nfcYrvtHsqWmJ9GNGy5LVG3ULbwzk5-NR1HFvsix4ShSl2EpV5srb8clTyNt83Ln81Z3S7MNnaDg9DM1i8eSMKIDXBHhmQqi1jx7KHbTsc78KrfjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c840c0f046.mp4?token=qT8N7uygAh5o_a9HU3QNz7YeFQkbNJkJ09lDC3fBnFMIiMpyOWuLNFTZrX3APfBSSSkym0EL4EAEafgRKBfrDTEoztYiEN40Wi_Vs2TLx5nZ_eNy7-zCC1KI-CeTOV_7nLRWxnndoz_cAZJ5YdF4IEDDHA8NWe5DnEzozyZd-YhGHJcgNxEs5txNVXAUzYYCStFyyISJyz0ulz40kgpI2MY39IrxGBH5KXGw1nfcYrvtHsqWmJ9GNGy5LVG3ULbwzk5-NR1HFvsix4ShSl2EpV5srb8clTyNt83Ln81Z3S7MNnaDg9DM1i8eSMKIDXBHhmQqi1jx7KHbTsc78KrfjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: اسرائیل و آمریکا برای نجات تمدن، با یکدیگر اقدام کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/692730" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46547643ab.mp4?token=l1OK3yN3V0XVczq_CgWQNSNKN4keNe5G7mU41PrRnTouHg1a7X0VYaJL3dt8kIokmSCOIcr8kEVCzbwqfuW1cSYQxyXgrdHFua8smpj0_bVOPrMhyruWucraNgEOMqdE2sH3A8tudNlmHY5DxJAuJ-l6ib2f78KzxHlP7Fiv9frpyuS66TsS2aafMjOeT199aev-r0TvOPOgsJk6AfLx5ozV0f02_3HXAU_-n3XEkWKY7btvn01Sc_ye7UVOGHuoOkbPBV2csN2GI0qpd5XBA80iwonrzbX4IKneuORD1X67CLTeJwAS1sCWuk1en7zZ_BUCYi48PaHRRjfEToNUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46547643ab.mp4?token=l1OK3yN3V0XVczq_CgWQNSNKN4keNe5G7mU41PrRnTouHg1a7X0VYaJL3dt8kIokmSCOIcr8kEVCzbwqfuW1cSYQxyXgrdHFua8smpj0_bVOPrMhyruWucraNgEOMqdE2sH3A8tudNlmHY5DxJAuJ-l6ib2f78KzxHlP7Fiv9frpyuS66TsS2aafMjOeT199aev-r0TvOPOgsJk6AfLx5ozV0f02_3HXAU_-n3XEkWKY7btvn01Sc_ye7UVOGHuoOkbPBV2csN2GI0qpd5XBA80iwonrzbX4IKneuORD1X67CLTeJwAS1sCWuk1en7zZ_BUCYi48PaHRRjfEToNUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو یک پیجر با خودش برای سخنرانی به سازمان ملل آورد!
🔹
وسیله‌ای که منجر به شهادت و نابینایی تعداد زیادی از کودکان و زنان لبنانی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/692729" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-CAkrOx1afuMWmpF1iMbLZUm8Em2oJ3Uf0-bM5x_9wW43z_lIhjtYgGGWAhiWHJNbAXLEYyz5EM90dI470Q1Ve6vRP2ZsEJAvm89pRIvAYcg9yUcrQfmGlxCAFKBCKc8WtPyreZOf9k1oTGYWXmRNytY6VHYe1LL3Au7akxVF9VdBAiX8QTE4-PgJfzZW481ghpkXx0iDRefxzRJiCuoFdWoj_APvSIn2cC0GAHZw0OXf1YsiZ8zY2KCqM17fcN2WVzYXowm-vr9zqjIjO1jLcdRnCIDLdqXFCMB0tdXoUnxXdsWmqQKA09FBY9Ikx2L4SNbZxdak6o6IrMAucMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرار گرفتن تصویر شهید سلیمانی روی میز هیئت ایران همزمان با سخنرانی نتانیاهو
🔹
رسانه‌های عبری تصویری از محل استقرار هیئت جمهوری اسلامی ایران در نشست مجمع عمومی سازمان ملل منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/692728" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
نتانیاهو خطاب به انگلیس و فرانسه: جنایات امروز ما برایتان خاطره است
انتقاد شدید نتانیاهو از انگلستان و فرانسه:
🔹
انگلیس و فرانسه، اسرائیل را به استعمار متهم می‌کنند. خودشان این واژه را ابداع کردند، مستعمرات آن‌ها کل جهان را در بر می‌گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/692727" target="_blank">📅 21:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
نتانیاهو: آقای الشرع، یهودیان از زمان موسی در بلندی‌های جولان حضور داشته‌اند؛ می‌توانید در کتاب مقدس بخوانید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692726" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a4488558.mp4?token=HqdPv0nzXZz7demqNGBOP6fGvRLfsuX_LVkr968qdFXRrz9AMqLYsy7o-nt_T7oc7zC2q3XYUH0XORFtxoSCqggp-DQD9rmP1E-Inva6OQkoq0V9BraDJlH4ELfwjV5dj0eEMSmbp2-WMS2m-WtDgWPVQlP_4HPKMGnN7ET0hNq8FpFnriqf-0_k37FQfzlMDWtG9Ji1w1eN3_fI2tcE-_fMfaX4GAeIwbS0mIKLhnECCa7eCFdDistCJ6JtUXPSuD8DwU0od7IoYNaEQcNnXekzV9tV_jnHt8Ct8aOyZm175rOn14xEm5B0WxfYTGD6LKc1cjKbqujRDplLldrxqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a4488558.mp4?token=HqdPv0nzXZz7demqNGBOP6fGvRLfsuX_LVkr968qdFXRrz9AMqLYsy7o-nt_T7oc7zC2q3XYUH0XORFtxoSCqggp-DQD9rmP1E-Inva6OQkoq0V9BraDJlH4ELfwjV5dj0eEMSmbp2-WMS2m-WtDgWPVQlP_4HPKMGnN7ET0hNq8FpFnriqf-0_k37FQfzlMDWtG9Ji1w1eN3_fI2tcE-_fMfaX4GAeIwbS0mIKLhnECCa7eCFdDistCJ6JtUXPSuD8DwU0od7IoYNaEQcNnXekzV9tV_jnHt8Ct8aOyZm175rOn14xEm5B0WxfYTGD6LKc1cjKbqujRDplLldrxqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای دیگری از هو شدن نتانیاهو و ترک گسترده سالن مجمع عمومی سازمان ملل همزمان با آغاز سخنرانی وی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/692725" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692724">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نتانیاهو: وقتی اسرائیل از خود دفاع می‌کند،[شما بخوانید بمباران مدرسه و بیمارستان و غیرنظامیان] اسرائیل از بسیاری از کشورها نیز دفاع می‌کند، و نمایندگان آن‌ها اکنون سالن را ترک کرده‌اند. این یک ریاکاری وحشیانه است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/692724" target="_blank">📅 21:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxSW73MYAQ3vxy6U0De1m-9g3r1MH2Frv6_rEOnkYvp_h949EIlrL28nU5WTyHfSvbSxx1FkXibsUzDqCNNNz9ieju7m1paYrqC7KkHuAE6nMfgDW4UlixiDTljsNk2tfEkDZ1wGNTtBIiFpGs0v2RusXUBeqZ5aMvI4cDETGZrfDFt1jnr8ErUixseMHqX5vnvhiWkCBp8tZunxIb04QHo2AqWv7Lu8zf1X1rcTu32dKHc0EfrH_uRDBqIrbiFN9p-U-cmgfNQWSYgEC1BeKaPBVJ1JrNKxkONNFAptWBcMIOXxNT1T16oVhzuGmcr6olajNYDe4xmlN2fUGnmWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علی‌رغم ترک صندلی‌های سازمان ملل توسط سران کشورهای جهان به صورت گسترده، نماینده شیخک‌نشین امارات در سالن باقی‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/692723" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a549f532.mp4?token=UID2yH3fWNcJL4MXgVqmwJZ99AGbFtYgMlW5OSpJCYNoJkiPsaI9-kKz9yd8POzOmVqbCvU4rWIZNmCnjqDhSilYuERs3TBtI2XAiyCgtMWcbXr-pGUx1M6k2aia7eFpmrtpLalDMnpn0e7waostjc4ARnt64phdGuNELKwlIIsSwr_KkE8i4NTynXu8Y7PedW_DVdSaBfHyg0R-FlPemJ-8_6JNvw3eHicYdpVoG8BT3Scvz6i0c4STKenJA2CSgJeUxsUvKZKYFoHnEi0h8Pox_EyUo5q3JWfC_bv9uc-j8gWbl9SYYPjZ0B6c0t_alTHqlinOt9rA5f-PIQF6_QNcsmbQRgTuWqTaKVJCpEZndPNKEcacnUGQHZazJtaQ6fa67aFBaFaZnB9k_CtGYO_-58BUAQ-cbsb_Z19mgVX07jlV_Xwb1zfCYSDiQDMBCCYPtwJfjMn1UZtkti0ZcD_SxshkONDygFOQ3BiDyNI_Fs2oEBZ2l1y-0qWk8ImHh4RrDjWJ7fLKVCHXqb4rFYYNqrN7v0o70nLhRV2pFnaLhGnnCur6bxGa4AQz5l9JhmpkufO5bpOrzjytIkDNsk1REQKX35ECRdRNddfQ9ZaBZvsgwXzIRCGyCtm0jkVjae6fiufLhRe69clnCihN-v8M6cUbqRdLmOFQ8j-0dhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a549f532.mp4?token=UID2yH3fWNcJL4MXgVqmwJZ99AGbFtYgMlW5OSpJCYNoJkiPsaI9-kKz9yd8POzOmVqbCvU4rWIZNmCnjqDhSilYuERs3TBtI2XAiyCgtMWcbXr-pGUx1M6k2aia7eFpmrtpLalDMnpn0e7waostjc4ARnt64phdGuNELKwlIIsSwr_KkE8i4NTynXu8Y7PedW_DVdSaBfHyg0R-FlPemJ-8_6JNvw3eHicYdpVoG8BT3Scvz6i0c4STKenJA2CSgJeUxsUvKZKYFoHnEi0h8Pox_EyUo5q3JWfC_bv9uc-j8gWbl9SYYPjZ0B6c0t_alTHqlinOt9rA5f-PIQF6_QNcsmbQRgTuWqTaKVJCpEZndPNKEcacnUGQHZazJtaQ6fa67aFBaFaZnB9k_CtGYO_-58BUAQ-cbsb_Z19mgVX07jlV_Xwb1zfCYSDiQDMBCCYPtwJfjMn1UZtkti0ZcD_SxshkONDygFOQ3BiDyNI_Fs2oEBZ2l1y-0qWk8ImHh4RrDjWJ7fLKVCHXqb4rFYYNqrN7v0o70nLhRV2pFnaLhGnnCur6bxGa4AQz5l9JhmpkufO5bpOrzjytIkDNsk1REQKX35ECRdRNddfQ9ZaBZvsgwXzIRCGyCtm0jkVjae6fiufLhRe69clnCihN-v8M6cUbqRdLmOFQ8j-0dhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه در شش ماه فعالیت آزمایشی «مدار» گذشت...
🔹
تلویزیون اینترنتی خبرفوری با عنوان «مدار» شش ماه فعالیت آزمایشی را پشت سر گذاشت
🔹
این ویدیو، مروری است بر آنچه در این شش ماه در «مدار» گذشت... @AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/692722" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc6a1b3d5.mp4?token=Nuxkh-BsQdk_lMNq_N3h18C4NiBZSxoHwG8P-MGJA54olCv09cov5cT4xK_t5wTre_p5upknIGsu6Gyontmpt7eVf2KcSNiwPKVTZNe4pxczBNd1ixwE2M1linwFI63JcMvH69zA1dy7PZSoSQK5EtsauQgADdtwtP8L0HUmKM46xKtFsqTICuRccx5Iy0ec5_zSoN4MKS1cRPUQOQavCZ0VqgdIl-bIyrc21pin8BtxhZDSB11aB_jYP4X1pqyNApj9FRcGBsJRHwGQd9wXvGl9jh9cqTeRWPX85REbb-c885Gk9mNfw9R2ALNbkE_4l-6I623U_KWGNHIyAU-l4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc6a1b3d5.mp4?token=Nuxkh-BsQdk_lMNq_N3h18C4NiBZSxoHwG8P-MGJA54olCv09cov5cT4xK_t5wTre_p5upknIGsu6Gyontmpt7eVf2KcSNiwPKVTZNe4pxczBNd1ixwE2M1linwFI63JcMvH69zA1dy7PZSoSQK5EtsauQgADdtwtP8L0HUmKM46xKtFsqTICuRccx5Iy0ec5_zSoN4MKS1cRPUQOQavCZ0VqgdIl-bIyrc21pin8BtxhZDSB11aB_jYP4X1pqyNApj9FRcGBsJRHwGQd9wXvGl9jh9cqTeRWPX85REbb-c885Gk9mNfw9R2ALNbkE_4l-6I623U_KWGNHIyAU-l4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی
نتانیاهو: تخریب تاسیسات هسته‌ای ایران بسیار سخت بود، اما برای من یکی از آسان‌ترین تصمیم‌هایی بود که گرفتم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/692721" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4a943a26.mp4?token=IN-JymfR83rJ0rQS3NWpc8lL80GF3E0O_LBzQZZhG4zFvLy3lNC7FNECq7x53w91igWSk_mNof0cID6M9-Q0VZgEe7HbP3kmOKEFHvh87gQLPN8qbxm3y4lUiyl4Zd40TEsqpo8kDb1NdkUbBfKck2Hp7GNVmVL7sdhjcgZN6uOsq9mDbr6cvGqf-sXUuMBGSPMWL37uQPIg5KquOnmOscsVNxTask9_WY-3O5dkR99I_fo3Veum3K1dRbbWM-fBT9kaznXz9uqSeeCuHmkoizEh25CKxV2dcn46F_GO9aZvXRGLn1En7pMyrKB1sJYrvRGLa1LbQfPxoSaaydYVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4a943a26.mp4?token=IN-JymfR83rJ0rQS3NWpc8lL80GF3E0O_LBzQZZhG4zFvLy3lNC7FNECq7x53w91igWSk_mNof0cID6M9-Q0VZgEe7HbP3kmOKEFHvh87gQLPN8qbxm3y4lUiyl4Zd40TEsqpo8kDb1NdkUbBfKck2Hp7GNVmVL7sdhjcgZN6uOsq9mDbr6cvGqf-sXUuMBGSPMWL37uQPIg5KquOnmOscsVNxTask9_WY-3O5dkR99I_fo3Veum3K1dRbbWM-fBT9kaznXz9uqSeeCuHmkoizEh25CKxV2dcn46F_GO9aZvXRGLn1En7pMyrKB1sJYrvRGLa1LbQfPxoSaaydYVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب نتانیاهو جنایتکار: سران کشورهایی که ما را علنی محکوم میکنند در خفا از ما تشکر میکنند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/692720" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
توهین نتانیاهو به سران کشورها: اگر بزدل‌های دیگری در سالن باقی مانده‌اند، همین حالا خارج شوند
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/692719" target="_blank">📅 21:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692718">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0d7b0ceb.mp4?token=vWCRsGVINZhcHsbIM4pED4bV8BjvQRSYXYDTMqKGDuqT97vC1CfePmfY-zku4hHDZp7GXFtq6_X7cxmvHgkzwARp1Mc20yvfLTXOFRavcniKIXbrhIZMWlQKL9Ck4TpgRbE-5Z2NEYOruK6qSHaxtvFRBarcZxf_IOYBL58sXKOkC9l2czcINoMvqt54FZkkgI3JTbYtF5pzcbeAz1qIqEj8SXGXBh3f8FgorDOUERNbSdg5HnB1r-GecXOQmV0XDFDKR04fheshyq-sua4AWQPJ4D71oC5qrunIRGsy8gUS4vAn8Ik_FqgpaALnlSY7Ek3hWESnr-JrWDbP5SLr2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0d7b0ceb.mp4?token=vWCRsGVINZhcHsbIM4pED4bV8BjvQRSYXYDTMqKGDuqT97vC1CfePmfY-zku4hHDZp7GXFtq6_X7cxmvHgkzwARp1Mc20yvfLTXOFRavcniKIXbrhIZMWlQKL9Ck4TpgRbE-5Z2NEYOruK6qSHaxtvFRBarcZxf_IOYBL58sXKOkC9l2czcINoMvqt54FZkkgI3JTbYtF5pzcbeAz1qIqEj8SXGXBh3f8FgorDOUERNbSdg5HnB1r-GecXOQmV0XDFDKR04fheshyq-sua4AWQPJ4D71oC5qrunIRGsy8gUS4vAn8Ik_FqgpaALnlSY7Ek3hWESnr-JrWDbP5SLr2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو منزوی‌تر از همیشه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/692718" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692717">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ترک گسترده صحن مجمع عمومی سازمان ملل متحد توسط نمایندگان کشور های مختلف همزمان با آغاز سخنرانی بنیامین نتانیاهو
🔹
شدت شعارهای اعتراضی به حدی است که مدیر جلسه حاضران را به آرامش دعوت کرد.
🔹
نتانیاهو در واکنشی عصبی، غایبان را «بزدل» خواند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/692717" target="_blank">📅 21:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692716">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8p1DMjSfxQB2q5TVggl4aP08TRMa0NEYE0W7l3kCV_uBiS4gYJOgr5g2C4gY_dsJotAKwxoUNFSFEGUMiU8cRZi2KdfnZL0gusfyjVjDmvsq6Sard7jWe8MFW4vE5wsMZyit2C_GynIGqZ89BTA-XJzaMiSopfipH5Yn_Fjbd-UVbJ8zGoV9y7zq93Dsw22KibCGpKaKDcxaYkThRDiRb-N9GltNHIM2POWw8O4Yaw2Zjbr-mc89Umv9WGvizPcr-lbCFns4dFkZts0IEtgVul_bUGi1L_xYzkCnBUVlYZ9zQWPqTEzv_PYjGdNjxVYZ4IL6IFLPstfEBtgiGJM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکنون رأی‌گیری سنای آمریکا در مورد قطعنامه اختیارات جنگی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/692716" target="_blank">📅 21:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBiUBegYHgxAo9XegYn0aqYWULsmVjWp3zafS0gWgtMMhPKd-NzA9O4zMtkBWrZ-bTv_gnxhEh3JcQEB4v184gXwrnNHDdZ7waUx-gDJ-tvFUgRiwW55eV0I52neanN3BeSPdwEF7KVdmlKoA3GrmBI9DHBOfJ-xucKo7f-i68qHaxM9JITMRtJ87UstSZqVvjYN-f5-DVeI2bTSX1UrEb6pUQaj4pCwYmtDFQFBPY_U9ncS5pq4hMZMP4xle2m399T2bH1CchdTt8p7d78h0A3I8aXo4HdrHkZKQ7vQslfVyoMy3FRiBV6wvraqUWWAKn6BE6HPWDS8wjA34Gnbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از مصاحبه فاکس‌نیوز با پزشکیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/692715" target="_blank">📅 21:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آخرین وضعیت پروزارهای بین‌المللی ایران
🔹
پرواز به کشورهای چین، ترکیه، روسیه، عراق(نجف)، ارمنستان، پاکستان، بلاروس، افغانستان و … برقرار است.
🔹
پرواز به مقاصد امارات متحده عربی، گرجستان، آذربایجان و عمان لغو شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/692714" target="_blank">📅 21:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22daba2ce1.mp4?token=ZQUk6ZtfXog4mQmVQQgcifvB4uKu1TJvekaJXS_dM6yX-wRrJJzyPt9Yar7SvQq29A9dm9tHDp_THBFFK1lJtCubcByPcIXFNn0UqdB_jpzqcNpFL8Thn9DkzI4Fw2pCQ4d8Q6QbGjgUCyjD0VoKS1j8ZgpARSVjkUsBCOFw3OOjRaY2qWH2kAEiyTqOpOHBnhU_aNL1sOe5QREfWo9mIO9wj-Gjq9c80XM18rHSY2Xu6GliwAGS-taqKu6IERe-aHMLPSNdhMXpp5YAg3jxZhHPBX0xsXQITwnwYVycAZn4CIh3GcU1X310T9nS-_6vizmkJTSDjNtCFJfEKftQYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22daba2ce1.mp4?token=ZQUk6ZtfXog4mQmVQQgcifvB4uKu1TJvekaJXS_dM6yX-wRrJJzyPt9Yar7SvQq29A9dm9tHDp_THBFFK1lJtCubcByPcIXFNn0UqdB_jpzqcNpFL8Thn9DkzI4Fw2pCQ4d8Q6QbGjgUCyjD0VoKS1j8ZgpARSVjkUsBCOFw3OOjRaY2qWH2kAEiyTqOpOHBnhU_aNL1sOe5QREfWo9mIO9wj-Gjq9c80XM18rHSY2Xu6GliwAGS-taqKu6IERe-aHMLPSNdhMXpp5YAg3jxZhHPBX0xsXQITwnwYVycAZn4CIh3GcU1X310T9nS-_6vizmkJTSDjNtCFJfEKftQYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آوازی که اشک شتر را درآورد
🔹
۲۰۰۳، صحرای گبی: شتر مادری بعد از زایمان سخت، نوزادش را پس زد. کوچ‌نشین‌ها آواز باستانی «هووس» را خواندند؛ شتر اشک ریخت و بچه‌اش را پذیرفت. این صحنه مستند «داستان شتر گریان» را نامزد اسکار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/692713" target="_blank">📅 21:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c756cbbf.mp4?token=TcBtz7bTSpPHLIG5cNrr8mbYXNDkAUbglKdlDSTWqlZt-P8oXGNtv7-8dKSskQ3w7CLi1-dusoIBox0CAf4gXPOv74XMawebPqWwt259Irnq6fbHTgdfiCHN9SFpuSeVA9gtyMMnhS0pB1LuM_WBhILueYk2qJbfxmN5XH4RcFVHi7QwGKj6UdkKDSNdoLjyUGMoUeryrqOaNfoqye_UQKAoAfDaq5umHbkwMeFIAF21-Y4L8g4z_G4mtMXlgBITFc59E2jLmKIYbyPceu1wiaKa1ukCazSf6nJMafy5Hlsg1198wLJU-g4rkh46psLXPEGBkMa88lDqaQ_BPfQCJwqhruoxvNUizA-v94_7ZMnlJjuQpWDyluag-V0W7RjxlUJkB8mTJ0OoiOmdZ9ivF-5KGos3J_sASHAjMQRXOBKyI879ET1HMidEg7EP4CUEv7v1iI7kYBnHFeMhXdSypB773BWkARKK2InNLl8B-fFb-bwyMEY1qmb_mebzb0nf-W5ILxzxPx04NMuA91QRNQnOHCy4aCBtR_uJqtNHHDU7SKzIeXIZG8CA7MG8s4YiJv4BtQUbHxVsXqoGcp6LFYzYM58qQrGyZPzhmfABZz_xaZoYpmxPCJz7PLZdp8I7hpmBd_UzRZZWRYGo7JGSEro8dKuFb76kzMkXArgfiS0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c756cbbf.mp4?token=TcBtz7bTSpPHLIG5cNrr8mbYXNDkAUbglKdlDSTWqlZt-P8oXGNtv7-8dKSskQ3w7CLi1-dusoIBox0CAf4gXPOv74XMawebPqWwt259Irnq6fbHTgdfiCHN9SFpuSeVA9gtyMMnhS0pB1LuM_WBhILueYk2qJbfxmN5XH4RcFVHi7QwGKj6UdkKDSNdoLjyUGMoUeryrqOaNfoqye_UQKAoAfDaq5umHbkwMeFIAF21-Y4L8g4z_G4mtMXlgBITFc59E2jLmKIYbyPceu1wiaKa1ukCazSf6nJMafy5Hlsg1198wLJU-g4rkh46psLXPEGBkMa88lDqaQ_BPfQCJwqhruoxvNUizA-v94_7ZMnlJjuQpWDyluag-V0W7RjxlUJkB8mTJ0OoiOmdZ9ivF-5KGos3J_sASHAjMQRXOBKyI879ET1HMidEg7EP4CUEv7v1iI7kYBnHFeMhXdSypB773BWkARKK2InNLl8B-fFb-bwyMEY1qmb_mebzb0nf-W5ILxzxPx04NMuA91QRNQnOHCy4aCBtR_uJqtNHHDU7SKzIeXIZG8CA7MG8s4YiJv4BtQUbHxVsXqoGcp6LFYzYM58qQrGyZPzhmfABZz_xaZoYpmxPCJz7PLZdp8I7hpmBd_UzRZZWRYGo7JGSEro8dKuFb76kzMkXArgfiS0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع خیابانی آری، تضییع حق‌الناس و مزاحمت هرگز!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/692712" target="_blank">📅 21:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
دلیل زودتر تمام شدن بسته‌های اینترنتی اپراتورها اعلام شد
معاون وزیر ارتباطات:
🔹
چون دارندگان محتوا اطلاعات IPهای داخلی را در سامانه تعرفه ترجیحی ثبت را به‌روزرسانی نمی‌کنند، ترافیک محتوای داخلی کاربران با تعرفه بین‌الملل حساب می‌شود و بسته‌ها زودتر تمام می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/692711" target="_blank">📅 21:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXfcr0xqWrkRs9ZfklsP5Xx-63wN6wchb6JxYQOLo4TN3VJqGjZQeIfJPaKOh1V06rsL03qPvYF_wpOlKuDs3fFo2uO58mFh9eEspRrtfv9t8lNdmSKCGhUgOyHMA5YACK9WemXqYEXhwsx3S-ft0KHXeY_hYk_4ZZ9tkLZr0r4UpvfnGjVvurRa95oldSw9Yc1jW8kZ9e4hLjX6fTOaSKEbQUGRVQpaQHfWkkDIOORHCqQijvxP_YfVkWvVvjMncX1vSy2DYx6PoKHVBCmqQTX0wBvtRwL8IJejjq2CPL1JVurCd4hrDHOOa-0dOJqTfa_jq6Owf-ozPU6ia-WDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درس‌هایی برای آمریکا
🔹
ملّت عزیز ایران و جبهه‌ی مقاومت، درسهای فراموش‌نشدنی برای دشمن امریکایی دارد؛ رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطه جنوب در این روزها نمونه‌هایی از آن را نشان داده است.۲۶/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/692710" target="_blank">📅 21:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سازمان اطلاعات سپاه: ابتکارهای نیروهای مسلح جمهوری اسلامی ایران، معادله میدان را تغییر داده است
🔹
مقاومت مردم ایران و استفاده هوشمندانه از جغرافیا، ارتش آمریکا را به بن‌بست کشانده؛ به‌طوری که سنتکام تخلیه شده، نیروها به اردن و مکان‌های پنهان منتقل شده‌اند و مردم آمریکا هزینهٔ سنگینی برای حضور بی‌فایده در اطراف ایران می‌پردازند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/692709" target="_blank">📅 21:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fcb10f9b.mp4?token=t3o5qSPvBudlclCgSgnEXszmylEHIlxzzYABuDM4MvlP8xkGF_tzG364fS1_z7Ks-ig3AJffROXxDngUFYer97d_xnP5muq3A-pzrx4zoMuhYeTnSCLAxlUXG7u2LEcLRs_5OLJ9JYNZSUFSL_2N_j9eVIQn3Wz0zIyTTLql1GahPbeWSWhkHhzCSDz0Mb2zTQwGLwSljVHO1Tsz3es-vNRUP0OqOzODe7K_J9GAC5B754zpcHOtC4pZ5TqUDcmFn3yjjcYIquH3r-uv9zR3HG6O65g0TSG-fJ2P-F1QQbfM5vflznf2kmGPCqlO9B6MF19n6OtEyk4GHuhh6swPyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fcb10f9b.mp4?token=t3o5qSPvBudlclCgSgnEXszmylEHIlxzzYABuDM4MvlP8xkGF_tzG364fS1_z7Ks-ig3AJffROXxDngUFYer97d_xnP5muq3A-pzrx4zoMuhYeTnSCLAxlUXG7u2LEcLRs_5OLJ9JYNZSUFSL_2N_j9eVIQn3Wz0zIyTTLql1GahPbeWSWhkHhzCSDz0Mb2zTQwGLwSljVHO1Tsz3es-vNRUP0OqOzODe7K_J9GAC5B754zpcHOtC4pZ5TqUDcmFn3yjjcYIquH3r-uv9zR3HG6O65g0TSG-fJ2P-F1QQbfM5vflznf2kmGPCqlO9B6MF19n6OtEyk4GHuhh6swPyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابانی: باید چه کار کرد که کادرفنی تغییر کند؟ کی می‌خواهید بروید؟ آقای قلعه‌نویی نمی‌توانید تیم را جمع کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/692707" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رویترز: مذاکره‌کنندگان آمریکایی و ایرانی در نیویورک در حال بررسی مسیر مرحله‌ای برای پایان دادن به جنگ هستند
🔹
مسیر مرحله‌ای برای پایان دادن به جنگ شامل بازگشایی تنگه هرمز توسط تهران و لغو تحریم‌های واشنگتن علیه ایران است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/692706" target="_blank">📅 20:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d5d8a708.mp4?token=CuJKxDsjLofJ1Im2668UIavUeHpfHIarTP2LT94OpgP_scKyKphC9mzB5PYabjV2vfEF0vUw_GazzcbMbAQdRrfT2bldqURIn7NhBfxJr0ViDrfkJNWqPXQx-N4mv0it85qCvOX3zP_wGn3p2aPkk4ifnVInT44sY11W3Xb7hYTY_PSGtpM0aqrYXITdpRtiZM3O8eQpIXaObjewFhGi_vcrzyAiePBhdfAISoB_kFvxcOs1kEHvczMLMan4mOgeYNOg_fRymiWvG9ONfFBHxmO7Jm3rElebY_TDWPRdxjHkEBWxvWV6_gt03UavgZEgzzcbPx8hgFm4qxaXCMnlow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d5d8a708.mp4?token=CuJKxDsjLofJ1Im2668UIavUeHpfHIarTP2LT94OpgP_scKyKphC9mzB5PYabjV2vfEF0vUw_GazzcbMbAQdRrfT2bldqURIn7NhBfxJr0ViDrfkJNWqPXQx-N4mv0it85qCvOX3zP_wGn3p2aPkk4ifnVInT44sY11W3Xb7hYTY_PSGtpM0aqrYXITdpRtiZM3O8eQpIXaObjewFhGi_vcrzyAiePBhdfAISoB_kFvxcOs1kEHvczMLMan4mOgeYNOg_fRymiWvG9ONfFBHxmO7Jm3rElebY_TDWPRdxjHkEBWxvWV6_gt03UavgZEgzzcbPx8hgFm4qxaXCMnlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۷۰۰ همت تسهیلات بانکی چه شد؟/ آمارهای بانک مرکزی با واقعیت همخوانی ندارد/ تسهیلات به دست تولیدکننده واقعی نرسیده است
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/692705" target="_blank">📅 20:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692699">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtQZ5vi7FeYMgr-F599hvIWb-sAsJya-yG-1uqUEDA1vcm09yz8yBP_lVRBSIyfwQ1oUEFxGEBFrNcASF6uUMTanG2DLnga3xIuRPKnC3Sc-pgzucpb95iHfq5OMCHPP3Ilsg1NfHJa8kVAWcpCrxVDI8yVP1NxcTAbHaPs6EWC2KwGH9p559dQqQGV38W8gm0_1PhK5bctry_aXBqKnv_fNYU3wukW1fHneh9HAjHhe_9ckqT8B1lIPsER0aI9nPwd85PoNPqICvNFkDE2xL1Yz2ugg93k5G33gQdPTkXfSfJV8sQSu6MO2bgbJ2gs_qgys0Wm9u41luVaG1zHlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHpbzt83kPgEjHc_hK6p916sIuMtyQq7FulSeZCLohkNP_bsyI5a0mGeZRW-UzZYo0L2XA_IBMXIpGrYAVEl25KIZmWu-kwHNYbCH14MQ98MYc2JoKNBtTVVpCvM-9MCG_sMT7H8G4kZwLaYKqxy13nftRWCe6Cw3w4tRSAhetQkhzxITqmLbsx-NI_VjF_lVoyEAS6FXdEhI3v22jJzRyCqgN8AoKIowO1RiUg4TgQs9GctoekxlxeirmxO1m-e3jz0ZngQEWZGXW_P78KL7DE37MLKIEBVbqS6FrxnNwTLHCbbfjKCn6FwJlYbFxi-F-sicPofLOxiphVJbRO1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DadFrvKgEqdglHY3tgR2-t3n9eZwxUXZfzRlN_wFNIUfQCLVg78GQd5mPYcYkIMpU_Bb-fYCc3Z-7hEEPTEq0xDLTqXAeIwqz_uW_m3196Y44pUNfvl0hC-be4G_SNpIgzKW1OJZFzyD6D_UwM4D44FvN7dhokZLJq5kjy9Qkz9-wd8Kca7D4dsmRmKV1pkdM-9IF3NtQNxKIziDLqQsc9urSxs0S3uy4x04K-_fd1cPHmqddoC4RSM_9joQw_ZZROs0rMHKmxxpGGHPb7cwOKZOn-LgDzzkx0T0cB7z6-OeZPOW67O5XUnjno44fQy7tMTjkKQfMVvys45Hlehfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-F_3GfzpF5ZfgWO-EOPMiF-Qd5TTk0F9tU1FRvDbWcGweuuv7sGurNCes6Pc26DyETKHcMZi9iM-LNuQEdeuAkRL4q0CgU3lhGLGzUYfniaPVgQUIWpJyKXLN4pStrjoVCFnSbqcaRbMusiFBLydfoYvXEP9_xB1hYqPoRaKcqj_01stGKhcAf7V4igKcVoA9BeOLAerr-KZXSaXCVrv66-pxVEibLg18wKj1v7u88qf1QHHB4y6YxhVwZIYwLlDys41AeSOJ326KLokZwI5utoAsIRKs15yKcNqY4sUWKTfyvAt0LrOJBZ5Aa_8iHNliTyXGJWoDsSyS9kE7pCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OA4EARadv348AUDSvzJtdUL7d9Ir6RmL8A1N8AzGyw5zw2WyXDv-sN_bt1J3_hHHowvbXOG-4PdT7T3YPtNdilP8Fb816oIdECBtlSsFjGNqGR93B9SXMk9N6NJEubinltpOm9YsXKkQCATggCq1N1kV96r1sjjd83XM3dRL8RS5px_vq0W6bdfR1STWPu_qGqMjqJ7jRiAXc1GtISJw6GojU34G6BqvXM_m3rNYUMPPSCUKnFQfXdRd0ShV-ZFsb5NFiP0rbFx-Zc9DQVw7gs0UztucpV5o7tUoTr4LLPygrOxcPnbQjO8VwHieXaVspPcqzq7W0Tg_zuOK7gGqyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آیا همه آجیل‌ها خواص یکسانی دارند؟ ۵ تفاوت مهم بین محبوب‌ترین آجیل‌ها را بدانید
🥜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/692699" target="_blank">📅 20:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692698">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
شی جین‌پینگ خواستار بازگشت فوری ایران و آمریکا به تفاهم‌نامه «اسلام‌آباد» شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/692698" target="_blank">📅 20:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beLVuh9O7biYBn-9CAU-GzRZRgGXzR_FCJYQ4IGORr1BnkABxuYZ7tUs9PFwp_dLRKJu0KnWSueKB8lEU5_JEQ87SApUZ8Vn612xv083JPmLJKdTrP5VVl1AMZvN0l5QMHULNuo3YbUFUMoIOdaRwp0OtguCGxOkhusqT3p9745g6yX6W7cfFq5B34NM04P45ndQdD7EJWEntVhYBQG_pXibUgJu0fdHUhVvnBYyz1qFc5Xe8zNHzYtZsUoKrT2aHW2rGjTFeHVkurupRQJg8USEyeqKho4YjzJkcZ8wOqVLT_ylwyyFoK3lgVjRvWHUWdvMZJc1JG7WXteBo8Mj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕯
طاق نور
یک نور کوچک برای ساختن یک حالِ آرام‌تر؛
ترکیبی از معماری الهام‌گرفته از فضای ایرانی و نور گرم، مناسب برای دکور خانه، محل کار یا هدیه‌ای متفاوت.
✨
💸
قیمت اصلی:
۲,۳۳۳,۰۰۰ تومان
🔥
قیمت ویژه: ۲,۲۹۹,۰۰۰ تومان
⏳
موجودی محدود
📩
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/692697" target="_blank">📅 20:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fde349ad3.mp4?token=SKD-uGBXvS9CCnUGKpJ31U2by1Ao0Sks3LJsrJmm2Hi4fqE89MS1E3wjzIgHpSit63eIyl1joQAx-PME1EorIWkIZBKEK02xVJaWiFrnVe4URwCC1_MVff7-KtD9uXNmyW9chPSxG8fpCWZtBtZgZ8Yu-QlV40KurCPV9khEM6KImSCuVRva-WAThQhG0S07a6PGQClSI-Lc70-M2GR0ypVbPRFcq31PgQl-LmfoRm60Tsg7IebMgIyomqNIA8hEMFagjfQEfqAMJW1HwEYdiGJcpm8ZPjUZjSNGZrSIMOEOD15LXSvVrLMeJPUusaw46p6y11ootmb2UpmqXcEQOxbsRnW8iGorFWsd3VN44f3Se5cHNCG3ZLmOK3V31HtdjTM0VYGFcvT_GUh9x3OdvmWWLuF9QNlao0_oJi_wN5zwVpIg8UYhuQB3YQof_l-cZfNbH8oKtM_QWmrRD0JPhBfecvmG_qzNd4fuCAKY0TqLoe0ciZODsnuRny3u1sEIOEc78ggdcR6bGuTg-9DIuzQmSbukXPndsZVbJdoV2TePa70a4HwgqYdcdfAOOyAuYZjfFILDKBNOibjkiCIOnwrUvyJMJvMvjxq2AUlABClxAi3fJINHEFKx1fi7DC_0PpCmQ4_jepG0emV5ZHYrDlRfR5BsZhXkimfJ5g69YoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fde349ad3.mp4?token=SKD-uGBXvS9CCnUGKpJ31U2by1Ao0Sks3LJsrJmm2Hi4fqE89MS1E3wjzIgHpSit63eIyl1joQAx-PME1EorIWkIZBKEK02xVJaWiFrnVe4URwCC1_MVff7-KtD9uXNmyW9chPSxG8fpCWZtBtZgZ8Yu-QlV40KurCPV9khEM6KImSCuVRva-WAThQhG0S07a6PGQClSI-Lc70-M2GR0ypVbPRFcq31PgQl-LmfoRm60Tsg7IebMgIyomqNIA8hEMFagjfQEfqAMJW1HwEYdiGJcpm8ZPjUZjSNGZrSIMOEOD15LXSvVrLMeJPUusaw46p6y11ootmb2UpmqXcEQOxbsRnW8iGorFWsd3VN44f3Se5cHNCG3ZLmOK3V31HtdjTM0VYGFcvT_GUh9x3OdvmWWLuF9QNlao0_oJi_wN5zwVpIg8UYhuQB3YQof_l-cZfNbH8oKtM_QWmrRD0JPhBfecvmG_qzNd4fuCAKY0TqLoe0ciZODsnuRny3u1sEIOEc78ggdcR6bGuTg-9DIuzQmSbukXPndsZVbJdoV2TePa70a4HwgqYdcdfAOOyAuYZjfFILDKBNOibjkiCIOnwrUvyJMJvMvjxq2AUlABClxAi3fJINHEFKx1fi7DC_0PpCmQ4_jepG0emV5ZHYrDlRfR5BsZhXkimfJ5g69YoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رامبد جوان از نگاه جنسیت‌زده بخش تبلیغات صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/692696" target="_blank">📅 20:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df64165d71.mp4?token=sBbMErFCfXdINyJAs5zGCNK4jj-5R7QHyvnJbigienGM2QyAkXJIsTTdv6snwTRPcznsvYMDi5y0dwZwg3Jpc96sEQFcbt0EjWwmhT21Fnm3K56qIdBbjwLce_UdB4m6e49K1cqkFXuKMyKMgf-9SPeUfzxDCtuMb_1cMhTKjl3kDuyI1xD_JTPFNcb_JZdFWqUyOHbHogUDUlRyLwIpixHGuZbhWPo_46fS15fjPc49u5-IOMAUNlD8pjT_0N5QXILIluxgNVGBo1xPlnmdOMZRYi0MHeXJMWBda7-STGN3D4XiBkaDKYJBu-BsthPjtZjjL3ijtxb_T4veAX3tLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df64165d71.mp4?token=sBbMErFCfXdINyJAs5zGCNK4jj-5R7QHyvnJbigienGM2QyAkXJIsTTdv6snwTRPcznsvYMDi5y0dwZwg3Jpc96sEQFcbt0EjWwmhT21Fnm3K56qIdBbjwLce_UdB4m6e49K1cqkFXuKMyKMgf-9SPeUfzxDCtuMb_1cMhTKjl3kDuyI1xD_JTPFNcb_JZdFWqUyOHbHogUDUlRyLwIpixHGuZbhWPo_46fS15fjPc49u5-IOMAUNlD8pjT_0N5QXILIluxgNVGBo1xPlnmdOMZRYi0MHeXJMWBda7-STGN3D4XiBkaDKYJBu-BsthPjtZjjL3ijtxb_T4veAX3tLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوکه شدن دانش‌آموزان از دیدن قالیباف در مدارس تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/692695" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
پزشکیان ساعت ۱۸ به وقت آمریکا (۱:۳۰ بامداد به وقت ایران) با «برت بایر»، مجری شبکه فاکس نیوز، مصاحبه می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/692694" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522ce71498.mp4?token=slNCNIur2k0uZRsT879GAV1dLierW2UPUcyfl8QAb_MnHS0Rt1zbSQzW8uNEuQ0cmRizy2lIlAraxHsNiVcC0xW7G3rnZNVS66on7Nh-f74yuAcSzzasNBdFZy83W3GpVgMFk8hG-B1TLTtZF4KQYVpWaXQhRvzL18T-PYHUHJNnHPP3P4B_Lw4dBLiBjQWssabEQ5zIR0GmFAhsaqaH8ulgfoTjfaDEgKvYoSadDHrxQJmbVXtoB7Bwr3YThh1hNldXhglUDrYoxBvVszNNXHhqdH3QqXvk9UJPDrcaAP2knladtC7KnaolQnDgwbKqO4ORWm0sFm0saW-u_iHDEqRH6ifGmuBOTfMszn0Wwbuu_I5sry7_rXbd75LsiBVebeeRR6BpMzIr0u7zTOnXq1C0KwdG3uWiVhoHissqig1ZL0rt1K-AYEyH-Vo5VhGmRPuj1xgmE2os2x6VOdEAz9AQd7eWUcnv4D5iBGwMhU_NUMtlct7JSY7ny9aQhzuaT__nbRYB7rKm8DViT6_hPDOt_zoXqabSSzri6MAcKl75cU_SszqCsfkAHHbUHWBn7xC_cNbGXoDyXRU7zgJne8o1G5mri22hoX_vyb4OGBy86XEcGepI5Vsm7JCFplOwXnPrKdmEUyF4ZWx_WtTMQNt_cPo9PFYjmrJ4G1P3YGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522ce71498.mp4?token=slNCNIur2k0uZRsT879GAV1dLierW2UPUcyfl8QAb_MnHS0Rt1zbSQzW8uNEuQ0cmRizy2lIlAraxHsNiVcC0xW7G3rnZNVS66on7Nh-f74yuAcSzzasNBdFZy83W3GpVgMFk8hG-B1TLTtZF4KQYVpWaXQhRvzL18T-PYHUHJNnHPP3P4B_Lw4dBLiBjQWssabEQ5zIR0GmFAhsaqaH8ulgfoTjfaDEgKvYoSadDHrxQJmbVXtoB7Bwr3YThh1hNldXhglUDrYoxBvVszNNXHhqdH3QqXvk9UJPDrcaAP2knladtC7KnaolQnDgwbKqO4ORWm0sFm0saW-u_iHDEqRH6ifGmuBOTfMszn0Wwbuu_I5sry7_rXbd75LsiBVebeeRR6BpMzIr0u7zTOnXq1C0KwdG3uWiVhoHissqig1ZL0rt1K-AYEyH-Vo5VhGmRPuj1xgmE2os2x6VOdEAz9AQd7eWUcnv4D5iBGwMhU_NUMtlct7JSY7ny9aQhzuaT__nbRYB7rKm8DViT6_hPDOt_zoXqabSSzri6MAcKl75cU_SszqCsfkAHHbUHWBn7xC_cNbGXoDyXRU7zgJne8o1G5mri22hoX_vyb4OGBy86XEcGepI5Vsm7JCFplOwXnPrKdmEUyF4ZWx_WtTMQNt_cPo9PFYjmrJ4G1P3YGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسدود شدن مسیرهای منتهی به سازمان ملل در اعتراض به ورود نتانیاهو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/692693" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxK2Xi0TVjJPO3sEYMNwNSGHNjQrbhBPN-0QXPMd9XrHt0a5pTGCkgW9He6g5eIm34B8bPT4q55J8cmrYcgHRwW9hc9tzJbhpsF4yPhM0RV6eetQv5EhTaUcvHbsta-pd1mwA-Z2YPVg5Gzj5fsZ8nH2x4jSFc41d2RlKX0NHZEUgETIUIZbAhbDRfrVMCgVz1m28zBe6FLZ0_FwJfsvj1lNeswVYTs5mN1kKJEH53IN-ze7HOBtrtbK-w6Bc-0R4-AhCgR4CpvYJWU8_Q_tJmvHll48cKjuq_gIpSyozrML2c6DlQ9c4Y8W5fF3ESCrCagpdmmslJRuTTLdJA_eZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف یقهٔ بسنت را رها نمی‌کند: رکورد زدن بازده اوراق قرضه مبارک! ایران آمریکا را به وضعیت دهه ۱۹۷۰ برمی‌گرداند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/692692" target="_blank">📅 20:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">18-1 Ane Manaee (1404-02-03)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/692691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هجدهم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
ولایت حق از آنِ خدا، و ولایت باطل شبیه‌سازی ظاهری از ولایت حق است [04:39]
🔹
رسیدن به بهشتِ قُرب الهی  یا برهوت گمراهی؟! تفاوت بنیادین میان "ولایت حق" و "ولایت طاغوت" [13:37]
🔹
ولایت طاغوت یعنی بی ولایتی..یعنی بی پناهی..یعنی تکیه کردن بر خانه سست عنکبوت! [19:30]
🔹
سوره محمد با تبیین مفهوم جهاد و قتال، و مردن برای مانایی و جاودانگی، "الهیات مبارزه" است، نه کتاب مذاکره![22:46]
🔹
معیار حق‌طلبی نه الفاظ زیباست نه تظاهرات دینی، بلکه ایستادگی در نقطه بلاست و پذیرش هزینه‌ها [30:30]
🔹
رابطه انسان با خدا رابطه‌ فقیر است با غنی، همه‌ی هستی، تجلی نیاز دائم عبد است و رحمانیت دائم معبود [35:09]
🔹
رحمت خاص رحیمیه، مشروط به شایستگی و لیاقت است و هدف اصلی آفرینش و خلقت [41:05]
🔹
رحمت رحیمیه، خاص متقین است و بلیط ورود به این ساحت، ایمان و عمل صالح [46:07]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/692691" target="_blank">📅 20:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxT9ZynQ3Y4tPJ9Jcb8n3-WBnrCP8-jT26rr1rh9RTFO6d6Ab-vd8LYu4UlP1gTKftX1GltPFGUCsSk2TZqLpk78fVrQL98NReLVM7Xv812So9C9QQTTUw6XiUmBQyNMeFl6TdTidOxqcotrEodxqBVpsYn3H9ztUtw6_wqeVtpO98H9A2l8P1alP_weN9bb8rBx7Spp3k8IkFMeTo1cADL4dy21RNng6nVXNTArtSdRY7JpKdN9RJ0riI7ypdDGFz_EYRQf2gcer17QXH3Z1tz2FrifjnYKxwqaxgchEDnvt2hOTtZITp9OCrOpIKCHrsVUHysIBqqMvSzoPoEBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: مذاکره‌کنندگان آمریکایی و ایرانی در نیویورک در حال بررسی مسیر مرحله‌ای برای پایان دادن به جنگ هستند
🔹
مسیر مرحله‌ای برای پایان دادن به جنگ شامل بازگشایی تنگه هرمز توسط تهران و لغو تحریم‌های واشنگتن علیه ایران است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/692690" target="_blank">📅 20:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رویترز: مذاکره‌کنندگان آمریکایی و ایرانی در نیویورک در حال بررسی مسیر مرحله‌ای برای پایان دادن به جنگ هستند
🔹
مسیر مرحله‌ای برای پایان دادن به جنگ شامل بازگشایی تنگه هرمز توسط تهران و لغو تحریم‌های واشنگتن علیه ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/692689" target="_blank">📅 20:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxXqsBaIGjLYdd4r5oJje9mUSdjO39gyZ9uJs9_UgikH8CCGBz2TIH3ZTG9ksBZPQiPTLsSo6wTgLaM1yXy1FfPAUC_AYFJ3wDA-OpNB-yP8PDhshGepopXJSagUy7CJNxEU5S6d5UMa99ljVSAeKXnKacUQO-3wPsUScVDWfpNEwiuIMx2F1jLlLLt6mUHBUSHHbttgaR6tmXJeDUz_ztL2tcPQkK1wYI2XNidr66nXtR5pu3-4XePimDCnQJr1JPJhNrj3URT76pODfIIH0FGdFFE8tLWtjhpo46ToCnWjWCl8yHgFbdssRiFKnO04n3ReJoJaKmf5tqMVS2j29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت پروزارهای بین‌المللی ایران
🔹
پرواز به کشورهای چین، ترکیه، روسیه، عراق(نجف)، ارمنستان، پاکستان، بلاروس، افغانستان و … برقرار است.
🔹
پرواز به مقاصد امارات متحده عربی، گرجستان، آذربایجان و عمان لغو شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/692688" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e8b1ed5d.mp4?token=VVdVqFE67JeDOcv9BMv_d7lcBE-opTWnkXTuOpJvVXUfOPCKhJjl4eWPbJfYKnRRQWJTCeizHkvdZSlB78xDuNbqSiNUp6RvPs0Jcsftevsaz6opeUuLzbCXxcwXJYXLgX9l-HMcgXaaRJNRlwsCOKwPPonjnjS9zroSnVdD0IKWNZYFOMItR8M8SDzGcHft9k-P43th6PGGafMs0eQFurpQIqxwhDCVQBjQfGDFN8JNTkUQfJf8nOnuc3OvUm0KfrwDnT5eynv3hMZjL34vK-lkZ-EmKa4fFTFunANNXV-k-krZdz0k-5GvAjDFmghMveFd49bpbZN5vBLsEdsMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e8b1ed5d.mp4?token=VVdVqFE67JeDOcv9BMv_d7lcBE-opTWnkXTuOpJvVXUfOPCKhJjl4eWPbJfYKnRRQWJTCeizHkvdZSlB78xDuNbqSiNUp6RvPs0Jcsftevsaz6opeUuLzbCXxcwXJYXLgX9l-HMcgXaaRJNRlwsCOKwPPonjnjS9zroSnVdD0IKWNZYFOMItR8M8SDzGcHft9k-P43th6PGGafMs0eQFurpQIqxwhDCVQBjQfGDFN8JNTkUQfJf8nOnuc3OvUm0KfrwDnT5eynv3hMZjL34vK-lkZ-EmKa4fFTFunANNXV-k-krZdz0k-5GvAjDFmghMveFd49bpbZN5vBLsEdsMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌بودن اتفاقی نیست، تمرین است
🔹
جانفدا یعنی هر روز قوی‌تر شدن؛ در امداد، در تاکتیک، در کار با اسلحه.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/692687" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692684">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKfzHcREvKDqMxk-rsITjL2Uoq6MK8IzDANVZyjpdbA9jrc8EQCWHd6-LsVXYQ5zIejUYG9SLWNfUEFfd1jKl8_h07KxvKN5uC4EoQ-xpfvAsBkyIBRqokiu0xF0B7klcGqIBvCjVObFIuk4E8s65Ue4BCqt-3a-oGyY90NCVKzn1nn6qXUVXIO3YRM0p7dDw2kyR1kNvtpuGEqH5ug-1kcKBbI6KWLpz-c3PKlLpgRaXdW3c0bHIZcV-7nRxXrcLVh2mLjPeBhdNxM4xRsUGefPGvwDtceuCccghgp0HgAXki1eYF-kBZbPmUFRk1iDth3z_QJCKXjbssGb3lmsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDw_aAMuY0-jXaN7W_XVNToCj4-5MhBgNTuiFOsmKLuFgJqisQ8RC6GY8kepu1bz-PRDESKLB3A8l0EDPSBujkFJa3mvF-yYFWIAIb9igy2wNe8ohaGrQszjtgl0qIJQs4oDig6VbkOswR6lNv0MfEZQaYmNHwen-_A5cZyX6FrLdMvolfHOiEWvOVOXWLPQQrhOC8KUoThAJ33auHCdfHwUozkRB-xknylsI6rgsn3TL69EHmCjKOFssMdNyM1qF-VE3YqTpfJwP-BOobV2snsh2AYkKqli9p5hhrb5UlOi3NOHNBF5H7BVx3PnAeolBPgultA-ZNET5eWd_1whCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk_jKHgcLR-CVfaNPfzAeaCSMlfHDMt0uZbBsCGmXA1GThyKW9WqN_EywiObbtvOh8RAiZuTdOcAJpOSaGcM1ehoas7TqJc6lmo7gjw91yvub4tUEPK-3U1fRmdDjUHP0WRmi2I0VTI0653Vwko3tsfAwsYjp5j_Ue55NCxTr7bJLw0QXe9RAeGtm2MVmogzrjPBM-tEoVtT7nKwI_K8f_p59nB9N4Gl5tApJT-GzbVVHIPMcYmZxUrD91rxlM9ErZ5nRUKLplMqz-qdw3qZe0U2fbZc8oKao6Fgd-jWmL7zI-oUJfFeV9blXInvc0ugkov6luVsI3PLvwglt-F80A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عبارات توی آزمایش چه چیزهایی رو نشون میدن؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/692684" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692683">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kau7NlbACz5SP9DBEuh6cO4GV-GcfErHsUQ8EhU0lgNFdsZzrYU5fIaX7JRKBdr1Z7WujnUh8-TpdAWCk9wbWHdR53wb4vTlbi3TLNP_EjunxWsB2aD2gW6k1ACp4EVtsh4erIVt8rp3KI1qo-_vLD68KwpunREP8wFUMnsY817PLTIaYKQpxtiY1xSdOsOpivfqBihchuqy0wexIjyArreGTV0Ti15at-oHlOfsEHf2GF8l4xkwhnThSuzapyWDW6DNDvfcQnzy0-KC8VKA7yftSXyKEc9lS9m0qhPazoNLK3hsh1OAmAYHX7Koi1lNhClVQ9kBrcWe1jTa4O4gRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آشیانه‌های ناامن
🔹
محسن رضایی در واکنش به طرح آمریکا برای تحریم هواپیماهای ایرانی، به کشورهای منطقه درباره همراهی با این طرح هشدار داد و خواستار پرهیز آنها از «ماجراجویی آمریکا» شد. او تأکید کرد در صورت جلوگیری از پرواز هواپیماهای ایرانی، فرودگاه‌های این کشورها نیز نمی‌توانند پرواز داشته باشند. رضایی با اشاره به روابط ایران با کشورهای منطقه گفت: «شما دوست ما هستید، اما نباید به صف آمریکا بروید» و از آنها خواست برای جلوگیری از گسترش جنگ، در این مسیر قرار نگیرند.
🔹
هشتصدوشصت‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/692683" target="_blank">📅 19:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692682">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psGM8uJjk7DimqRcgOM2BRPH8q38mJQ2Gj8bu_SFo9uWpmkLTrHKNfE1qO64ugfjNRuOHFxVuE6XFXcV7HaLBeXP0AmuxaQ0748OcgTzJ-oP7ckrKn32ULBbU7TKrs_tsIgVM-7PdlETc21C1s_3-nChQ4gmEHiFYb2kHwCFn185LaHJPsKAP-USoF1YUkUVWMMfX86BOeKcUCPHaknGc4QkcffXpUmcdDzWKtMsjdWXl0zvWxvkeV1XB-oQsBkK62P6WH3_K2SCJmzKO5Me7iVkj-M9qZQdEwuE7hSnWgbiKsfCK2B1aMmM1sUg4UwLN7_QhSurV9_-xVQaLw3FWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جلد جدیدترین نسخه مجله اکونومیست: وقتی امریکا فرار میکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/692682" target="_blank">📅 19:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کارزار سازمان‌یافته علیه هیئت ایران در نیویورک/از تعقیب تا درگیری!
🔹
بنا به مشاهدات خبرنگار روزنامه حریت ترکیه در نیویورک حدود ۲۰ خبرنگار و مجری از اینترنشنال، صدای آمریکا، ایندیپندنت فارسی و رادیو فردا با تجمع مقابل هتل محل اقامت هیات نمایندگی ایران، اعضای هیات را تعقیب و با سوال‌ها و رفتارهای تحریک‌آمیز در پی ایجاد درگیری بوده‌اند.
🔹
از جمله سمیرا قرائی که برای یافتن اتاق اعضای هیات وارد هتل شد و بیرونش کردند، فرزاد فرحزاد که پس از اشتباه گرفتن یک رهگذر با مجید تخت‌روانچی کارش به درگیری و ورود پلیس کشید و مهتاب وحیدی‌راد که یکی از کارکنان محلی نمایندگی ایران را تعقیب کرد و پس از مراجعه وی به پلیس متوقف شد.
🔹
این اقدامات با محوریت بخش رسانه‌ای سفارت اسرائیل در واشنگتن هماهنگ شده و هزینه سفر و اقامت افراد را تأمین کرده و به هر خبرنگار روزانه ۳۴۴ دلار و برای هر کلیپ ۲۸۰ تا ۴۰۰ دلار پرداخت می‌شود، همچنین گفته شده طراحی پروژه و انتخاب خبرنگاران با مشورت مسیح علی‌نژاد، پوریا زراعتی و بهنام طالبلو انجام شده و جلسه هماهنگی آن ۲۷ شهریور در هتل جفرسون واشنگتن برگزار شده است.
🔹
در این گزارش به خودداری بی‌بی‌سی فارسی از حضور در این جلسه و اظهارات رزیتا لطفی درباره اینترنشنال اشاره شده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/692681" target="_blank">📅 19:37 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
