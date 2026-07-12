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
<img src="https://cdn4.telesco.pe/file/q7btbIWmJNxPbtsN00J1Zi4cY88SLk0JgU9gtsLuXRYDwwFk70wZuIGYEgyrpU9vpA_FCzMyi9qCVlXIHJzuKj8hTg9qZR4FkvR4maYaRdBEZQnbRtA9arG80gXUDj53vasPCUtLUU2ApBzXfnYvH9AyMUKaikeGFwyIFB2lv1QAMmC_23flN-xjvYaExg9ASNsThwCVom0bY8xChVdNU31d9HoMdM3jme67LFfYwphT3CV6iUFqYlSleg9wSCiWJ0o4uAw8WN2Gv7Uz4BBYSPkRwV7tSqRNxeebqHurVgkBwJqNrbatu-Griaygm7jH-CqdCQ6JQ4vPSfphSWhVUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 15:41:54</div>
<hr>

<div class="tg-post" id="msg-670165">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d9aa6be20.mp4?token=ScjY7-uz359ANBTgVTxC6x7dewaditRQPHRIEr0A8Z9pt53um7se1CTpCOUeF7QZ9Qt0kN66dhZxiAf4azigObotI7bHstIHZbnUQRldcjK5TwlGPPeiPQBLBolpzMhkL-UoMRR-H3fpGJyftZtxAdP8EtIQ72g49FmfzBgOZDsXeApr3Js-G_NnHvItC8rlHKPMcvdhQArrLjAWVFQIhcvfOnFPYUsLsfDb5csA2Mg8dLsUv4iEYtDIUZq-tt3Wt3gZbzTAknVZAJwtdnNBzp9dkzmq1_k1Vfu3VQZBntsGlE6teGZNQ2dZE9Lsd7ezFtsWQBlTwSBAsSFSjPtEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d9aa6be20.mp4?token=ScjY7-uz359ANBTgVTxC6x7dewaditRQPHRIEr0A8Z9pt53um7se1CTpCOUeF7QZ9Qt0kN66dhZxiAf4azigObotI7bHstIHZbnUQRldcjK5TwlGPPeiPQBLBolpzMhkL-UoMRR-H3fpGJyftZtxAdP8EtIQ72g49FmfzBgOZDsXeApr3Js-G_NnHvItC8rlHKPMcvdhQArrLjAWVFQIhcvfOnFPYUsLsfDb5csA2Mg8dLsUv4iEYtDIUZq-tt3Wt3gZbzTAknVZAJwtdnNBzp9dkzmq1_k1Vfu3VQZBntsGlE6teGZNQ2dZE9Lsd7ezFtsWQBlTwSBAsSFSjPtEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با اینا بوی بد غذاهارو بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/670165" target="_blank">📅 15:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670164">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455123f5e1.mp4?token=lcfshIK0L3BtFn-LO1hqQGs2z1UPMzGvb4qHXyYb5Dypzp7wd5JNeMrviKNA9O2LQaMpC5pO_aTCExXocOZf0l8D83hzpuxZQPJ-4MecYO8kK3onaT_oyMbv-fOEvYM6-Z0PWFQkAan_Cl5YEx7y3eBb_5bb0x4gkCfzYCwzR6yMBiqfkKmJGzmg4Nly0hV4ScmMLOd4NXb845a7hFrwuoJRcyl2WvS264uTdkUIV6aYgy61-1o82wWUGbOtLPMKR6D1uz4A5crUbC1-DYfffjzu8WcV01Lh4hDh6Y2x1OFzHy04JHFBtxFhCvRF4b33ZiC1amLxwZ7bZ3jDWiKXS0G2x0cLC6kXymZkDsvhkArLRrQy8BgOWfL1kuDM9rmJ3GkG-Rct--5KZI9EnBt4LJ9yuN2HeS86cbhhGYsA7-BlWlq_Dvb6n3lS3xY5g4udI7jfhrXcXCtSvtAFe-3TZaLWAM0Af_axq_ValOpl2Db6ov_eBwzSh88T3VHiLxcVO1ybhMnIzXUEYgo2byS6qD8acjcwdbPeLGKoIAcKnYcQbgyyYrsbjrqOHJpS5Za5rzL9NCrfAqjIOm7HadeGrJ9h_YSNbn53H9vV6UzAkwIj4PFjheqkPeyHpk-RVvYbVBshrXu9xxcHma0hQj-0VGYEr-0B1JadGsKyyOcqOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455123f5e1.mp4?token=lcfshIK0L3BtFn-LO1hqQGs2z1UPMzGvb4qHXyYb5Dypzp7wd5JNeMrviKNA9O2LQaMpC5pO_aTCExXocOZf0l8D83hzpuxZQPJ-4MecYO8kK3onaT_oyMbv-fOEvYM6-Z0PWFQkAan_Cl5YEx7y3eBb_5bb0x4gkCfzYCwzR6yMBiqfkKmJGzmg4Nly0hV4ScmMLOd4NXb845a7hFrwuoJRcyl2WvS264uTdkUIV6aYgy61-1o82wWUGbOtLPMKR6D1uz4A5crUbC1-DYfffjzu8WcV01Lh4hDh6Y2x1OFzHy04JHFBtxFhCvRF4b33ZiC1amLxwZ7bZ3jDWiKXS0G2x0cLC6kXymZkDsvhkArLRrQy8BgOWfL1kuDM9rmJ3GkG-Rct--5KZI9EnBt4LJ9yuN2HeS86cbhhGYsA7-BlWlq_Dvb6n3lS3xY5g4udI7jfhrXcXCtSvtAFe-3TZaLWAM0Af_axq_ValOpl2Db6ov_eBwzSh88T3VHiLxcVO1ybhMnIzXUEYgo2byS6qD8acjcwdbPeLGKoIAcKnYcQbgyyYrsbjrqOHJpS5Za5rzL9NCrfAqjIOm7HadeGrJ9h_YSNbn53H9vV6UzAkwIj4PFjheqkPeyHpk-RVvYbVBshrXu9xxcHma0hQj-0VGYEr-0B1JadGsKyyOcqOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
چهار مدعی ماندند؛ فرانسه، اسپانیا، انگلیس و آرژانتین؛ حالا وقت جنگ برای فینالیست شدن است
▪️
قسمت دوازدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/670164" target="_blank">📅 15:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670163">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjeO2YRzKdXGiVh_uDbuIs8QDmzFwfsmeGIHfmPH1mMBzwtWBEUVcYX6Ro4ZHbiHMNKpHDUu4fJczRDG0gpyPzmSB5K8sUsrn4nC_SsIh-jRRIYk5kfYtuc17qyCe5B1Mm4ROrIhcOqI4I630oCrz9RYJNJp6q5A2WKxkKGjawt9xVJ5nB5lph6byAPmJyV8MfZZMvTEJm-8qQ8SZmkVZHl_Pcd0T3COlO544CtCOFhcbjvviyaVGtvr350pGQdmFk9m9EhZgOxgg5eTD-DxXAzwS5OlTAVFwWw7nrViCuFoe8UBoTX7iu4WmWYVi0IQXfDA_WxqEmNVGTu-FiVT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روغن موتور پراید طلا شد/ ۲ تا ۲.۵ میلیون تومان ناقابل!
🔹
قیمت روغن موتور مناسب پراید در ارزان‌ترین حالت ممکن به حدود ۲ تا ۲.۵ میلیون تومان رسیده است که با  اجرت ۵٠٠ هزار تومانی تعویض روغن بین ۲.۵ تا ۳ میلیون تومان تمام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/670163" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670162">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d45d752bc.mp4?token=B4EkOGgdg3bY2caeLF9lGMh82TXJnzVgUd33-Zt04HFnSZvIdDUw6wzmXHXPwbNvT5eWb5ZYwLYEqbHf3kVySIKlf6BWboxFW_Dh1SrKwr6jKUsyxdSHQ9hLs63Q0TfXp3qK9dplQaLHMycCmAPbTB4RNiex6Xb972356ify3dd7Tz9EVr_b9z1uAT4vHY5dIzLSLtCkfAul_QpMSjbyV1ele3yb916xNBnkoc1qW31CnzwmbGsfDqX41sH4hAo_KiiwE5DHBQo29vN6H7l4DssUXJsL0lFbnaYkke7yyU4ucdSq-2dQifTMmPu976YCakuFZEDqJ8D9EHiX3ox8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d45d752bc.mp4?token=B4EkOGgdg3bY2caeLF9lGMh82TXJnzVgUd33-Zt04HFnSZvIdDUw6wzmXHXPwbNvT5eWb5ZYwLYEqbHf3kVySIKlf6BWboxFW_Dh1SrKwr6jKUsyxdSHQ9hLs63Q0TfXp3qK9dplQaLHMycCmAPbTB4RNiex6Xb972356ify3dd7Tz9EVr_b9z1uAT4vHY5dIzLSLtCkfAul_QpMSjbyV1ele3yb916xNBnkoc1qW31CnzwmbGsfDqX41sH4hAo_KiiwE5DHBQo29vN6H7l4DssUXJsL0lFbnaYkke7yyU4ucdSq-2dQifTMmPu976YCakuFZEDqJ8D9EHiX3ox8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال اردنی: حملات ایران از اردن تا عمان دروغ آمریکایی نابودی توان نظامی ایران را ثابت کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/670162" target="_blank">📅 15:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670161">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue7Z1AaidKoGpmd29RFuTVUKDcvf2EN_x-BtMHdu72IYL4TsKAMzWaQ-VhS6DflOOqvdP9_-bPFgI4BbjjNVAjmaqq77DM4TqeSD1lXc6EOt8NizwhawYWVjEz6AT7Kna82f1h8g1sdGpipF99V3n_LhMtUWHDoBrjhp4yQo67I42W9dVcRBeRDf3jcVfb6HUz18HPZt0Fg57yugS5BfryzhkZKsR3FkPjy8UakwUE5tXQZ26gY3yrxy0DOX1sS1wsDT6JtwYgFpKiTqQ7qaghzRLMcz6KTEebGL-Y4h5oCmv5JZrtPj-NW23qEsy7s8gO1kySxDX9FuxHNnP5v1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: علت مرگ لیندسی گراهام دیدن تصاویر میلیونی مردم ایران‌ و عراق در ادای احترام به ‎رهبر شهید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/670161" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670160">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAwFRL7p4cnlTqgoWQ51SsM7hQsUK269_8o4LHJshYhUd4jScQ-7cz_OVcQYjPnyaFJeHamAHElEH5EK5_zCCN0ibnxr-83rnIGl7NJWmcHZsHi_jpoYEgU_aYJPOyhoDGmytCOnlIMoWkyGNVZ4WTGKpbYFuh_RQhsMLyygf2A9vau66rIFWpqK11v8OGxdOQEEAiiPGdX5hyDfDoWLUD5fos35o4S-9cvkIw0wuBSwEqt3kEbywFYnh4BVoJpQWCa8mJlubbtqLEIlFvqIjyuqV8C2XtbyJ9BO4FB6dQlEaQngyr8jcQ4aONPeL5tHE8Uwt_DANAxkSYxTPudtKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود سنگین پول حقیقی به بورس متوقف شد
🔹
داده‌های جدید جریان نقدینگی بازار سرمایه نشان می‌دهد پس از دو ماه ورود بی‌سابقه پول حقیقی به بورس، روند بازار در تیر ۱۴۰۵ تغییر کرده است.
🔹
در حالی که طی اردیبهشت و خرداد بیش از ۶۱ هزار میلیارد تومان سرمایه حقیقی وارد بازار سهام شده بود، تیرماه با خروج ۶.۹ هزار میلیارد تومان پول حقیقی از بورس همراه شد. هم‌زمان، بخشی از این نقدینگی به سمت صندوق‌های طلا و درآمد ثابت حرکت کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/670160" target="_blank">📅 15:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
«عدم تطابق شعبه انتخابی با محل سکونت» دلیل غیر قانونی بانک‌ها در حذف متقاضیان وام ازدواج از صف
🔹
برخی متقاضیان وام ازدواج می‌گویند پس از ماه‌ها انتظار، شعب بعضی بانک‌ها به دلیل «عدم تطابق شعبه انتخابی با محل سکونت» از پذیرش مدارک خودداری کرده و حتی درخواستشان را حذف می‌کنند؛ اقدامی که در صورت صحت در ضوابط و سامانه بانک مرکزی پیش‌بینی نشده و می‌تواند متقاضی را دوباره به انتهای صف بازگرداند.
🔹
از بانک مرکزی، سازمان بازرسی کل کشور و قوه قضائیه درخواست می‌شود این رویه را بررسی و در صورت احراز تخلف با شعب متخلف برخورد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/670159" target="_blank">📅 15:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6ca0cdc51.mp4?token=PkxHIPu0ozkEZ_b0wzIEjEj8mZHV3yMfKPx-CoSo6OLvXFWjc2ll6qYxfMCEwBbnzVBdLhwQjlLJ2Ch5Tw6ktBixIq4G0WVl08G30uzpGnjL1gLAUCzbMecwbnrNg21yXn8Dh6mhsm8101ctB2O440NmMnXx5Bj2YyvYt9eBl6Vxr6LXjtFWp2Sc7T8g6KOy8lgmRu7xLfzloYAtS2NsXmRDHZ3-uPfq2CqLZzOCh4nuX0Ys7oVokbWA3RwJlgWJ2Vl8OTMbICyfdVQV8o5_7-IJs0PcLIPED70yxppnv6qrGLTzqorOf5E0fn7o-bJH1ewBAkxk-zPg2jtNFtowkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6ca0cdc51.mp4?token=PkxHIPu0ozkEZ_b0wzIEjEj8mZHV3yMfKPx-CoSo6OLvXFWjc2ll6qYxfMCEwBbnzVBdLhwQjlLJ2Ch5Tw6ktBixIq4G0WVl08G30uzpGnjL1gLAUCzbMecwbnrNg21yXn8Dh6mhsm8101ctB2O440NmMnXx5Bj2YyvYt9eBl6Vxr6LXjtFWp2Sc7T8g6KOy8lgmRu7xLfzloYAtS2NsXmRDHZ3-uPfq2CqLZzOCh4nuX0Ys7oVokbWA3RwJlgWJ2Vl8OTMbICyfdVQV8o5_7-IJs0PcLIPED70yxppnv6qrGLTzqorOf5E0fn7o-bJH1ewBAkxk-zPg2jtNFtowkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه طور با یک کاج و قلمه گیاه یه گلدون طبیعی و بسیار زیبا بسازیم؟
🌲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/670158" target="_blank">📅 14:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670157">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
یکصد و پنجاهمین حراج شمش طلا برگزار می‌شود
🔹
یکصد و پنجاهمین حراج شمش طلای مرکز مبادله ایران، سه‌شنبه ۲۳ تیر برگزار می‌شود.
🔹
مهلت ثبت‌نام تا پایان روز دوشنبه ۲۲ تیر است و متقاضیان واجد شرایط باید به ازای هر شمش، ۵ میلیارد تومان وجه‌الضمان واریز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/670157" target="_blank">📅 14:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670156">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObruXKn83LBjNBcfcBGrhCE0TPIo4uQ4_VomZoggJC7vv_97X0Iw3Wj8rbSdcS0hjddkAoRupx-ar7wwF0F8I7wLOnMmS5gG4TyWCPklPFxAuWngRZ2UwS8jdFbyNeJwxr6Y6R93URw4n4xXgQgzfG73kZPA4s3-5td5-TnwsfsyRWC2HxOdvF_8eKDUwqtXa2Xf5dde-ypk9JBIB3E3VsGcs4czlq7t6az7bXVWNoKbvnnNTi3CYK9YNkxeMaRwFMGAy_5J28TrN23TKKlivS0AHY5F7ikotWIYBHSmaCLcYZZzv7UQgGwKQHL6LqBaYV3fOJ0aNqbDNNe5oETnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله ای که می تواند همه چیز را تغییر دهد/ چرا ایران به عمان حمله کرد؟
🔹
عمان که یکی از میانجی های اصلی مذاکرات ایران و آمریکا بوده، همواره تلاش داشته روابط دیپلماتیک تهران و واشنگتن را بهبود بخشد و فضای سیاسی منطقه را بهتر کند. با این حال، حمله ایران به عمان می تواند روابط سیاسی دو طرف را تیره و تار کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3229730</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/670156" target="_blank">📅 14:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670155">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
توصیۀ جنجالی انگلیس به دریانوردان در تنگۀ هرمز
🔹
سازمان تجارت دریایی انگلیس به کشتی‌ها توصیه کرده با وجود اعلام بسته‌بودن تنگۀ هرمز از سوی سپاه پاسداران، از مسیر جنوبی تردد کنند.
🔹
این در حالی است که به‌گفته منابع، دو کشتیِ بی‌توجه به اخطارها هدف قرار گرفته‌اند و یکی از آن‌ها در معرض غرق‌شدن قرار دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/670155" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRRzrZD4ZILMLM0ISM2mLzMuSVh7CXEuN0G4LDu792tb9YOMHUUTdROJ6d73-kCfcACKiGVwMWIe_sv4MHKqBFHdygFkK6oImEs5Vj4Ki1elFQg-dbaI0BXflyEPfGBjeuyUVDVIst4df_zmi5PNjw92g40Ny8JSSzm4yy3J9ZArIfahl_UgQW_Ede9g5125NqhvCqpx3nk1iVsYWvCqkQdSjotkAYyzqd0Bh8eYMDv03p8idi6gaFWnnAnJiyoc7YvVbam2IItpt1sDO_8Yy3tykZ06kIAvXzwQQufxHFIMZ15SOSkSes6pwKFaZ7rGBeT8nPepsMzFz1XMcM-wmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZR6ygwrfgF2y9w68zA6646-NMhhH0JnOCw2ltdQfqEO8klCGiNSus2bzoM5yXsIPfFBponyif1ZSLnic-e7GMrgBD2p_nB00ioXmTQYofv7w3xCOw8IWMfp_OLNkLWdJdhb4Bbhdg_yESrn9XFZcDdaBbw9uEtB72g80_ZOs3g-BTtaLZ2HifWAFoO5YkJ8jsY1b80bETyKoVRoXs2Q5P60okXjXNuaODUVxj3DmvUrBKsAb-542ngagQzwFWAM8Rkl6TyibKcki4NysX99g9mwYgMV1cn-zpfoQiGT1HZh02IuCTRZBowZf3QDeXyGyaeZslxxzH5EXnoodvf_HIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EowIDvrdtFXwfZmpzGoTchaOWoE_6JjbngpevqcQj7lSeC9FN1BMoYrOdmgwfaQ5SbgEiin7UDFBrOaq8y74iq4fVtSqH76iIG2JqnwLPvVrZAfViG8z4C1Pe5SxPwpkc7OoaSE1Kz7Uw4pHj3Sw-hMk9Q6fSvy3fjwa2MFIq1oWcSQyjriMgsLvjyjYRbwGbiBy3u_rL1d-oCREitQmYglnyOmZ1TMHJCbdjAOO0sZslUtMKkuGrYh-C43gihJCP0IOsi5S_TiQ3IVwg9x_nhYyMp9xYPzHOTfGSXViDoL9PVhXFevrFxKWoPDU6IBARjXrIEvH6cOfkrit71S-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJYv-Xv4xUTX8zWaJh--U7fSkR1X4N0uMyFvQBFE6aszXDRScq59ZBLr4EBxx3VEPGhWvxpth6pFETEWISQorbHGP3WP2xLC3UgnBMXPxStVPA5pAhnoVlws8tGMHXJKaMht49D47XBMhukJuraMtc2zQBy2-wcRkCP9fqFPJYPdYw5YxWEIbvxysOVvoTQc669DqPUqUV_hs8tyA4hpQ71eJTfHr2c3b2onA_CbzXWvQP6_8QoEOOkWR3NBUHHPj8tdRxSBcYZfva7d7xQgeNDQCYNMG7uxuR-k4Dy444QQw2Gb_AGL4XaAD0ASlb6aqk4K_-78HzR4f3FSJa85XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جام جهانی؛ فراتر از فوتبال
🔹
برای جامعه مهندسان و معماران، جام جهانی فراتر از یک تورنمنت فوتبال است. یکی از جذاب‌ترین بخش‌های آن، استادیوم‌های میزبان ایالات متحده است؛ از جمله استادیوم سوفی در لس‌آنجلس که با هزینه ساخت بیش از ۵.۵ میلیارد دلار، گران‌ترین استادیوم جهان به شمار می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/670151" target="_blank">📅 14:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670148">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgRDDfriTAvxd1kyPayTgfmlSCZI1nZb_NxpCI5SrTJfZ7VOdIk0jvSXADtwXTj5IpnMHAw8IhtDIYozMTr6p23zvaAAskxBkqWscUknjOcov7C4EMY4mQejFZrwV7b_q6Bfr4M7uc9tx9dMZ5UQ_ceno4ddGqfxk2Ci2d4NILbShKJw6O2SFeqjUNlkCR2VxVzNlNko1H5e9GdlyirnWqITYFbV0CRE6jk-ETFiVU3KQOOnoyeZYJ-gRbrVx78K23MVtfBtoBsO1cqmx5MduBRhfSpbZ-QDqQ7ll4u4sr19htLD2dCsojuP_Ev29NfIuAMQBQOj2vKzhUJmBoiQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش یک کاربر آمریکایی به مرگ لیندسی گراهام: یاد و خاطره بیش از ۱۷۵ دختر ایرانی که در ۲۸ فوریه ۲۰۲۶ توسط آمریکا و اسرائیل کشته شدند، گرامی باد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/670148" target="_blank">📅 14:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/790645a23f.mp4?token=n0NJqWWzuJjshfVEimziD0OwTSW5f1LLws9gejVE5C2lFzmWmQJxI1SHXAXbzNBjMHQFYPwjO6go9AXzaDGtCsXNkL76ui6QVwFK-9LQUdXH3XsZR3NVPH7POTQz0Qq2PeZ4voydBMiZtmRNU2YgKzDdBi3ikwBaNld6WxN-DYJeVeWUTUYs8qKezBHxpGjADCBLQg_UXmNSqA_6Wx54_Ve7styW5vdgK9cof8EbSXGTYzdNTP7QuW2kuQuZCDbf93WuwDcu8TohC3i55PehlPtEWUK7PKjWPQbCMKeGYjgf7HVz8ZkO92miJCP2xTVC6ZDLTBhfIHVpNc9RfGrEUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/790645a23f.mp4?token=n0NJqWWzuJjshfVEimziD0OwTSW5f1LLws9gejVE5C2lFzmWmQJxI1SHXAXbzNBjMHQFYPwjO6go9AXzaDGtCsXNkL76ui6QVwFK-9LQUdXH3XsZR3NVPH7POTQz0Qq2PeZ4voydBMiZtmRNU2YgKzDdBi3ikwBaNld6WxN-DYJeVeWUTUYs8qKezBHxpGjADCBLQg_UXmNSqA_6Wx54_Ve7styW5vdgK9cof8EbSXGTYzdNTP7QuW2kuQuZCDbf93WuwDcu8TohC3i55PehlPtEWUK7PKjWPQbCMKeGYjgf7HVz8ZkO92miJCP2xTVC6ZDLTBhfIHVpNc9RfGrEUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در بنگلادش با ۴۴ کشته و یک میلیون آواره
🔹
سیل و رانش زمین در جنوب شرقی بنگلادش پس از چند روز باران شدید، حداقل ۴۴ کشته و بیش از یک میلیون آواره برجای گذاشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/670147" target="_blank">📅 14:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صمصامی: ۸ بند از ۱۴ بند تفاهم‌نامه، یا نقض شده و یا ناقص اجرا شده است
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
به شهادت رساندن رهبری، نقض حاکمیت کشور و مغایر با اصول حقوق بین‌الملل است.
🔹
با تفاهم و این صحبت‌ها، آن‌ها دست از جنگ برنمی‌دارند و می‌خواهند از کشور ما به نفع خودشان حداکثر استفاده را کنند و ما هم کشوری هستیم که استقلال، آزادی، جمهوری اسلامی را گفتیم و به خاطر آن شهید دادیم و مردم ما با تشییع نشان دادند که در همه حالات پای نظام هستند.
🔹
از ۱۴ بند تفاهم‌نامه‌ای که با آمریکایی‌ها بستیم، ۸ موردش یا نقض شده و یا ناقص اجرا شده و آمریکا با تفاهم به دنبال صلح واقعی نیست و قصد دارد جنگ را مطابق منافع خود پایان دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/670146" target="_blank">📅 14:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670145">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1d248bfb.mp4?token=GxkU46NlXF5AyjTC0Jr5COVWAwxd1tf2xyAKxWclr4kNhjLLOz6jzjfhhbxGBGMMCP4hrgLjPzpUf1GFPqp29PgfkSQoU8bbJ_4__NlDaQ4HAq7hGEXfi4sCTVfk3RAU18j9OR8RR0v-J7RhY1AlAV30JOTU_lo5AzUC4XMNjka0iRu-sYiHs3WbVIj4pWVzoqp2WxBqVxHrhQtsWrZeUOWWAZz56JKYff_Y-JM8mVEPbljshOgsgUTKYnMqAsrcWuqc3UiLb_M86-h1JJZ2YRtptwGh8fqMkZVttb5bqqfrA4WXs03ftR6bqR6Dd-J_CvF2v2TPnu-8S3WkdP__Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1d248bfb.mp4?token=GxkU46NlXF5AyjTC0Jr5COVWAwxd1tf2xyAKxWclr4kNhjLLOz6jzjfhhbxGBGMMCP4hrgLjPzpUf1GFPqp29PgfkSQoU8bbJ_4__NlDaQ4HAq7hGEXfi4sCTVfk3RAU18j9OR8RR0v-J7RhY1AlAV30JOTU_lo5AzUC4XMNjka0iRu-sYiHs3WbVIj4pWVzoqp2WxBqVxHrhQtsWrZeUOWWAZz56JKYff_Y-JM8mVEPbljshOgsgUTKYnMqAsrcWuqc3UiLb_M86-h1JJZ2YRtptwGh8fqMkZVttb5bqqfrA4WXs03ftR6bqR6Dd-J_CvF2v2TPnu-8S3WkdP__Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دیشب تاکنون صدای ۲۵ انفجار ناشی از حملات دشمن متخاصم در استان هرمزگان شنیده شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/670145" target="_blank">📅 14:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670144">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnpxYJRIhrYTWyO7y8jxBez7jNhOVLP5Z98x64VmAbWZm6XfjHBCTOfYnKUl6-kMIl0FNsv4Uvzx5ioeh8yKAyv8pfnoF4SXqxRU0HKJueb4zQhOpj8cRBx2od9kJv5hf9Nbcf0LSp6ZwatuqxEjpkefeLiAtCB6r8ZeJ_R_VGr-p4yTWifh2wK3gSpyVcCe83511n32MLtmDLJS3c25vYDMVnbAt8iQezbGLdzgYyD7KZoKqTAqWSojVSSoIflB5utxm8bmPAtpBc15VvqUJuRYJEHJZynj3_rkFT8ww2nPalWqF6bHsyR0CsfxjP6VH5_CvZ3swiUycqSWAu5vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرنگونی یک موشک کروز توسط هوافضای سپاه
🔹
صبح امروز در جریان تجاوز ارتش تروریستی آمریکا یک موشک کروز توسط سامانهٔ نوین پدافند پیشرفتهٔ هوافضای سپاه در حومهٔ خرم‌آباد سرنگون شد.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/670144" target="_blank">📅 14:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670143">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در سواحل عمان  مرکز امنیت دریایی عمان:
🔹
در پاسخ به درخواست کمک یک کشتی تجاری با پرچم قبرس در پی وقوع یک حادثه‌ی دریایی در نزدیکی سواحل "مسندم" هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/670143" target="_blank">📅 14:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670142">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
وقوع حادثه دریایی در سواحل عمان
مرکز امنیت دریایی عمان:
🔹
در پاسخ به درخواست کمک یک کشتی تجاری با پرچم قبرس در پی وقوع یک حادثه‌ی دریایی در نزدیکی سواحل "مسندم" هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/670142" target="_blank">📅 14:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670141">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
توانیر: حملات دشمن به زیرساخت‌های برق، ظرفیت شبکه را کاهش داد.
🔹
«حمیدرضا دهقان» افسر پدافند نیروی دریایی ارتش، در حمله بامداد امروز دشمن به جاسک به شهادت رسید.
🔹
هند خواستار کاهش فوری تنش‌ها در تنگه هرمز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/670141" target="_blank">📅 14:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ببیند چه‌طور هوش مصنوعی روایت‌های تاریخی را درباره چاه چهل دختران یزد، تحریف می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/670140" target="_blank">📅 14:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670137">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ib9HPyQP4G2uQXHj0g8FR7t_kXy-2nWyd-BQlQIIeNVdmqHHi37Z4fzw4PzqxJkwFxGu-9l9g8rtjSHcr-BLpwj_BipjmKzvtDvuJwuPIG7G6l8MScuuluai0lT7W0sthZ6QwlMKGyZHBc16iz4jGEuf5rvcs20K6wlp5VxEiiMvVIEihJmx0d7mWued-AJFpieQ__hseo853Jsfq_A92fUoSNoU2uU2qG2GEi_zGL0SBEt_qoTyZs0yksFKtifHjQ3kaqwCgFY0nhjW5ounNIln6tfZF3cPV5kJ7agzyoBlLKjnYneqyW3kSXVjqW2nuby2YQZgG5wR4-2sU1dhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کف دست با تمامی اندام‌های بدن مرتبط است و ماساژ کف دست به درمان تمام بیماری‌های اندام‌های مختلف بدن کمک میکند. هر بخش از کف دست با یک اندام بدن مرتبط است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/670137" target="_blank">📅 14:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4yJemsY38kh-QMR7wQalNfJeMDgsg_eSDfcy4RzIgid5A9_ew7xF2gbve-5efG-iQg2bjz5LVZ5H8xW2LmNvvwEJXbEqlo2Z1fLBIdXQu2qXZy1dIyF2OnslvaG2IiAAC6c7d4LCebMWUxizDi273AP72lnbHSQsDHbpVj4_2TdblAN6XYdsarHn1TWnxAOe0vX8Nsk6ntegf4N7AxMQtE8rzOgEAD_LDMYtWhyIqKEYz-p5GBcv5AE1C1om6A13aOjypz6Mw1aoXzvWqS1lfHkR7uqTXRaW-LgvTso9q052BqQxEVQelO10Gwe8rf_pYHag71E0jmbvaTui-19QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع
تشییع رهبر شهید انقلاب
در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان
«بدرقه یار»
ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: ت
ا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/670136" target="_blank">📅 14:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ودوم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای علی فضلعلی که با وجود حضور مداوم در هیئت، به خواندن نماز و احترام به والدین اعتقادی نداشته است، اما با تصادف و تجربه نزدیک به مرگ، تغییرات محسوس ایشان زبان زد می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: علی فضلعلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/670135" target="_blank">📅 14:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670134">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43231dfe7.mp4?token=HQBYlDL-0S_L6DoIiRkvio9fM7m7OFJxr-YjT5ytqjXkNJUJ2esSyz92Sq3NObiWrEtRM5BLxguRyc88Ui_863Aj2prJY7K5p1sh_0rAqH4o7-vocgD4jnrP5KPI65CUeErvM4sBTv1ZEI8CGYp320Lid19i3BAAUod22uM5MJfx3A6r6z4Zp9UaawyXroDyjK4BsiAlfFqAkWV0fowbvOiiJoLO9J3nS4SN-Lkfow2pS73OrtotYJdY5uzROVuuL8AIjcvH_SX9oE0f6JHUCKMznw0WiOl8oDBFvwCo-KyZa3Ng38DNbCPUc1Bk4i2SrxekW3AnZMd9rgM1a6-tcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43231dfe7.mp4?token=HQBYlDL-0S_L6DoIiRkvio9fM7m7OFJxr-YjT5ytqjXkNJUJ2esSyz92Sq3NObiWrEtRM5BLxguRyc88Ui_863Aj2prJY7K5p1sh_0rAqH4o7-vocgD4jnrP5KPI65CUeErvM4sBTv1ZEI8CGYp320Lid19i3BAAUod22uM5MJfx3A6r6z4Zp9UaawyXroDyjK4BsiAlfFqAkWV0fowbvOiiJoLO9J3nS4SN-Lkfow2pS73OrtotYJdY5uzROVuuL8AIjcvH_SX9oE0f6JHUCKMznw0WiOl8oDBFvwCo-KyZa3Ng38DNbCPUc1Bk4i2SrxekW3AnZMd9rgM1a6-tcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حفاظت از روشنایی شهر، مسئولیت مشترک ماست!
🔹
با برق دزدی مقابله می‌کنیم. برق حق همه مردم است
🔹
گاهی یک تصمیم نادرست فقط بر زندگی یک نفر تأثیر نمی‌گذارد....
🔹
قاچاق برق
نه‌تنها منابع ما را به خطر می‌اندازد، بلکه حق همه ما را ضایع می‌کند.
🔹
با همکاری شما، می‌توانیم به حفظ و پایداری روشنایی شهر کمک کنیم.
🔹
اگر موارد مشکوک استخراج رمزارز مشاهده کردید، حتماً گزارش دهید!
📩
سامانه پیامکی 30005121
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/670134" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aG-UDiJgFAMa3VuVh5Ua_lQ_lZ0xvEWEQ10F_7E2Cm1W2KUllBn1GYvwD4I0HtCf0VWYqXb2vF8U6GCSc1zoEpyHlVRmlZ062M2JA21AFKLA9btud72XzGjQ_aBZY6ZgXr_yomDrgPtsVzq5PJY4b53BFiNbX-9Ionzi4UCgNC6_r_7hMg7HG5Ao4B-KZ65TzVZIL5kGg7uSP9i_CfVt4Q268UHWjAEm8Xvizu5zeHqqC_0h6wYj0Ef-ZELXkrtRwA9qIG6gr0t5xLOcwyicWY4rqR5z6M4KH8AalhxGT4_D-IcWQ3_tGydE-cVh_6VmfydZHuqUlfiiJSMCjKZfhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqQLeCZspcu9JjOQ31cavd0OMy66EfwxGPeXVyOA-2K50Et0D-PjUwyns3qJhUD8UUC5FuUqptKQwJin1FH7hy7d17xgYxRNvVvnkctG0MDIMRtvYxN7kc44HOBJuxufImRcIWdbxAp2QhmRilwmOlfWuRFS5WhPHZn-zBC1jPA48ghFDqoa89CM2QDv_xU-3JDxEDMasWEZtZds-JPaMPIXh4h3g5uFqT5gOlLmeZa4Iy7xORgrMRS89wuJ3WAPAzx0I9NEk8EwENfSHe8613MxRaLvqeXpOweGyXlRWumWA73NymPH6vvlD2UYn9PalkSiXL4gPZW-shIwLLiQgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند مدل ایده بستن روسری که شما‌ رو خاص‌تر نشون میده #فوری_استایل @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/670132" target="_blank">📅 13:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03639c19b8.mp4?token=e09EcvxLeAk__UU_O9wAc8apWbCFDvfMxicZsvWsNCYDFVU1gEO6xKd1m3102M_3blBbX7g8qIGrVLyuLfGq3MlMg1ja3QFc94b0Q3R0mKZ5kfz92n1UNUc33hOCkR4aQBl_lOAqESd05XaYfrQF4ZzcLJFXhyszCvWP1pkMuq55_Ahur6UIBt7bFNEj-ab9CpbN2aAJDXrHw1KVCZLqIaMz-l0mNuPmLouajTkVeNaJPfh1doXtL_9ApjzvtkFiot2IaGpelMcsnCaTorAUToW7QdA8MCjvW6LTR76_7qoJasCf64PNLCmiBWOn-ImwflG9QZx7CssPnKF3vHnQ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03639c19b8.mp4?token=e09EcvxLeAk__UU_O9wAc8apWbCFDvfMxicZsvWsNCYDFVU1gEO6xKd1m3102M_3blBbX7g8qIGrVLyuLfGq3MlMg1ja3QFc94b0Q3R0mKZ5kfz92n1UNUc33hOCkR4aQBl_lOAqESd05XaYfrQF4ZzcLJFXhyszCvWP1pkMuq55_Ahur6UIBt7bFNEj-ab9CpbN2aAJDXrHw1KVCZLqIaMz-l0mNuPmLouajTkVeNaJPfh1doXtL_9ApjzvtkFiot2IaGpelMcsnCaTorAUToW7QdA8MCjvW6LTR76_7qoJasCf64PNLCmiBWOn-ImwflG9QZx7CssPnKF3vHnQ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سناتور جمهوریخواه دیگر به سرنوشت گراهام نزدیک است  ان‌بی‌سی نیوز:
🔹
نیروهای امدادی شامگاه شنبه به‌دلیل ایست قلبی به منزل لیندسی گراهام در واشنگتن اعزام شدند.
🔹
همزمان، میچ مک‌کانل، دیگر سناتور جمهوری‌خواه نیز به‌دلیل ایست قلبی در بیمارستان بستری است و…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/670131" target="_blank">📅 13:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670123">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO3hApN97fZmHrttc1GK-Cx-vd_v0rFKeX-K7TedSwkKUY3vMGQWysQcSVOtYVmCPJ7D-hVB1kVT1M2USqKpAqQxqeP3VJ2A2wKcTgqsDKYfHryW2TRynWkwLlkpztcfNLgGGb1fuS2jlA_zW0dB8sOHfg7l8nj7BV7BaC-Q6d9Et4uzTgziSsotump4J1e6F838srlQsPgg5btbhWYh0SN5zqJqjisbQ03SOhOQNzud0v-eEwbn8zCzT1EMWITBki3JF80-YUwpJhlPe9GyMH0cxiw-CkZLl41LK0Y4uxNhCGxm0TvWuY9F3NqZE9W06LZ7zmLracEED9pNJu6PWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fal4CS6MIjygpayp5SFMVHV6h--dcq61BUl7zSRvLPeFOmnFgKqWlNzEc_gTonKnWcHHgRJzF9jyIAf7Eu6n2iN9kjrYnerBU-drKCyry9jyo9Mk-bdsRWCRzI8IRE1ti77eFCPFdya725rofdr8C5LWPhXaohsOhCLUmROLvm2HP3m08lmygJ4yj57l5T10z2QSPA1Ca_Z-WCiUzYTBDfquHH8nOqvxguL1O_5Yk7_LbwayO-sSeHgzpx-GU7Wj17ILm6cDdJmoUOPvvxY5JAhNz8qR0UnGqHyJefXTGgGWT8z5tn13KjzRCO7JbKWJAZ1WLNELMbW0GuH4CITT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nERThtwC871T_i2D25piR_11qhON_OuMoKprKmJfhVYa8LjqoWS4hLY3NAomVVFoOe-6y_zobGY9qnaghwyWf4htV-CtlORQV3MmlJzGXajp8DQ11S8_jUr26j54qiPaCqq7qKnWBDqkEPB9xdTkYaV4O5_rBsAsfthkao-2LJl8saO9tf127g5SGRUwZc9TFW5zSuth0SWVm-IANwyKACgJ-u1dXrgLB5l4f-sEWo2ts_KouM3TFpsoi1XWAEBPjdI_M83p_P-KqSBhO9ZzPuVU4U4LZyXWNGhVo5qxA2DmFqKz59hAr6hPcZnk9EdVtJh5DOrWUbUHmaVelXl1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRPve6CyL32vF8yyeUZAed57-984WClRzQ4CDMDKsEw0PUJ0-h67dYwmdKTIkgd5bW_glgAnuyD744mVynDzGR9vvwnEJKDUL0CHfUssGl3Fl36eVcQTFBly5dR3DDf1a6F3yLflwoaHt9WuAwQdDOG6X8C9BazLm2MlJsQzZi6GTsy10daJYqs1xVRnhIlCS5JY-RopLS8TTlSVP_YPQdGYDy_8OAKTnoJmiS1pZV2F8BSiHTiF2wkFHeZdQ7xudyjfjeJsT2ri2vLPt2bJy7aswZsIcm9IucQnJDcixHNlEmbxcce5eG3QFdAJEq0AgrE4_-FIw2xrGLNeiWAg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCQJ7Ed8XYE_sbfkyW7XrHzUrNMeGumpu2m8kJqo1tpmE8aSgMvlkFXWmzajHSLO_J1zaHNJrhztm0sqYzwDOokhHTBxzcaPt205OMHxQGz6j8Bpfocj-VMjcIOCrp1fdCSAfN2R_QXntyHrCx3tRr7NOGwdJsK1LwhhXKicdWHEWfhJ5ZaYZIdHfed-U0dLIn0bt8k2EGNi4c9ZT9jU5p9eZzRs50ueiIZFhgjH4yQ0H1T9CaVbgO7a1HiXR1KTmThdxBqApWPoLXfW-8JB7U8rUlZAcvjpuT9HV2Ux6D-qlinplaYRepf2DpW1RDFFZHscs7_jzfveYjO3UTbLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5b_2uTJ5Dzy1hozFol0oH3gfOwLSUDWQ1u8ArweyFV5JcHCdB_kx2Dxy62MxJU49sihtfrLftMVp3Q74Ww0Rsl9M187OFdqZhJUp6wA8cASLPN8ixaTJPY3sqhV_U36EkUHQTJDQUaVR2SHM4i7DjXCyJ4k7t62gTyCdwN1K3FJgTRQ20IhORioBRTsOp2wiMMmF7xuKisEnWtXGsRXmXVsTS2yejhyysBdzBA-blFmccwnGumnOMjHFPEDz-6IKUby_ujijGv2KRt3x4GoD2bDZS8dMs2HXiNPegiy9ew7Z5ETjMx0KwSwHKL-eBBMmbmehZSVTslB8GS-XgFM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvC-EDig0CvVrT-D3mANM4Ey86hanX8_EbfddVzSQdoNZyCDKjp-u9wtGjdJ3WxIK3drGeNJO-RidWDi4ICB_KFcMaZj5T-noDJyRKFHliBKlzGVs2HgjGoaF06tqcsKgYk_pf3XMAdMhNyGEVhkfzgBy0xHS_coE24FyYDkYb9uXJFCOdq_lHDyGYRkpW9rZv2_nLOcoYOZrbtAwdPQ6zRlDKjP6N0RCV5_g2RL7b_8zT2i8E3Fj50YrbLELnXzFxr_VuBgglWH12ldlMmJN6A8vMFRP8eIJdLnO2Ulu4iMuGXAabZNqDvoHsM8LDAyXpE80CYWN64kePewnKxSKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3n5kMhDtFKKhq5CwRJk-A86tLKT82vH5iLk2vCPehwH94S9Rq1UVZoxYY3t-P8G_2U_tGYhhGsatdpDD0qn517bn6CQiXYrFFhfOlwBQ2llaK5nTAv66CvqZ8pjMsF-HiltqwSnCG_Cq-g0pg8PWrCWVbKXN_xMTxBE4RjLZHMC_dAXiBNqmI6VUBnnvNETL5wuJeEb3UGV1Ij5XqpieVmtC3wj01pmzyh2WWYHPyiEzT8PxuAeKoQCfk_Ee05fYIIOIR5ZpEZi9buamr79hppRNtmzzYCERtkGSaB6sdJmpPZTD-pCQEgZ5uKtbjI2zaE2LDuCd78QFe4O3_2Wjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پوسترهایی که رسانه‌های فلسطینی برای رهبر مسلمانان جهان منتشر کرده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/670123" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f13015bdb.mp4?token=o8aihgtFu4KmhOJAojBogHdp_NApQse9hpOTMcHHM7uIVAkcye2kJ_zrwoybn2IOmCkRJa8-QP7ZlAMUcDLrj9298igsr0uVvh7HV7lHqV7IGfTXGn52WwIOWVIuStJ0D2qXpF6WAsIEO4lLjSnRuVYq5lq_7xzjoLwwJiKxXXz9MQUQrZe8XMPhT445tqA5Cl-zVvetC-C_uaEfi8FDeeivvI_yD8_NsCFXZfin_HbxR3C_P6udtpYZOCP6pEDlj2AXZLQLciXNpHYOXQBw8AWUJIN6zCO9nikvbgFuI6bqbG0PAeejRgPikuYcBV35z8_Bw4LrnNxSUJTWWVV_7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f13015bdb.mp4?token=o8aihgtFu4KmhOJAojBogHdp_NApQse9hpOTMcHHM7uIVAkcye2kJ_zrwoybn2IOmCkRJa8-QP7ZlAMUcDLrj9298igsr0uVvh7HV7lHqV7IGfTXGn52WwIOWVIuStJ0D2qXpF6WAsIEO4lLjSnRuVYq5lq_7xzjoLwwJiKxXXz9MQUQrZe8XMPhT445tqA5Cl-zVvetC-C_uaEfi8FDeeivvI_yD8_NsCFXZfin_HbxR3C_P6udtpYZOCP6pEDlj2AXZLQLciXNpHYOXQBw8AWUJIN6zCO9nikvbgFuI6bqbG0PAeejRgPikuYcBV35z8_Bw4LrnNxSUJTWWVV_7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام شهید:
"ترامپ" خوراک مار و مور خواهد شد
بدنش خاک خواهد شد
جمهوری اسلامی همچنان خواهد ایستاد</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/670121" target="_blank">📅 13:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
دبیر شورای هماهنگی بانک‌های دولتی: خدمات بانکی به‌تدریج به وضعیت عادی بازمی‌گردد/ برقراری تراکنش‌های کارتی
🔹
خدمات اصلی از جمله تراکنش‌های کارت، خودپردازها و کارتخوان‌ها پایدار شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/670120" target="_blank">📅 13:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVZzkU0pMEfF-HtPFl9C2hgPRexcB7ufHiNZV-ZXeVWyuHS8UgziV3-bXPOYY1sjOs6RK1v22k7h7oKgz1IJl5dHk_DGFBBv9ibCc8tfbItbToF9ATj8TyghkSkhgfty5JHeDa3awSdsrINIlbQKpvFlDg0npqxXxECibHRv-zrBpk9nMpYEQIgn0eJiTKahLqzi5ddzZYWU1fsQ_LKkWbYz7vgB2pum-Dl8D4fAmRRkdfcwkgKmtED09DiOkPf9L9fDjaM3QTNyoiqrxfcNQrhH9kpCBYwkkxkOTxCWknEX1-oP-WHKhLX3eSyCdYzxYtrpbNYaBq0PW3YIniEZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز مین‌گذاری سپاه در تنگه هرمز توسط تکاوران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/670119" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk-zeNbR2h3NSxsrtyI9YP484PM11w5xqaywLjsPKNJ16bwhagGTW1K4IIPt-YAxsUF9fzbfbyqniFRYE4JJWvgWpn7g4mDggZhX3-pEEprmh25s0lKfooiqFWU_lM7sCX26SMITMmtaCqLs49OkcAnXYwox5LLtvvvRAFEipmIpDjyXooh7F5dXZa4ujNQLRR2SrrbXqqXDNBCb9NVDkaRBzpJUl11zcICxahmxPSNO7cn8Jp2ohuxY1nrnpgvLAnMT1RYkqsoWRylgmJWG95V2V_Fdva0PGZMyZEutRwfIcZe5p0KG8Q-ca0Ccq-uIppkxU73s0wy43USEOoMp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۱ تیر ۱۴۰۵؛ ساعت ۱۳:۲۰
🔹
قیمت طلا و سکه امروز در پی تشدید تنش‌ها میان ایران و آمریکا و رشد نرخ دلار، بار دیگر گارد صعودی گرفت؛ به‌طوری‌که طلا از نیمه کانال ۱۷ میلیون تومانی عبور کرد و سکه‌های سنگین نیز با جهش‌های میلیونی همراه شدند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/670118" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDZ4k13Tvd9Hq4PQlqpgzmx8b525b4MAC7g0BmRjkF1tCcFSPyQbaeIxNVfVXq13a91smPaRsVOstPV_gk1daaxrJTGh0qS1zbg7bpnKg0VJNhFooFVD3GjFWzkEUprKcr4aTmwRjYlIbOnwoo6KfQmIX8xsK8RfIeSWQ6tojv-7ppsXyBhnbpG2nGGoiHyJimifMFZ5B1bCNfGYlKZhTbQXiPYXi1_Yw2x0CEyvTWoXAotmstgp9MYmobaxtveo7eZ-dA8AIdo2_FUGZnHHboyBHfloXfSbkrlqFtg8MGt8kaTlUeTUMUTCSdkv1l486c5XaKNcdcGgn95mQnOvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: روسیه کامیون‌های نظامی خود را با نوارهای درشت سیاه‌وسفید رنگ‌آمیزی می‌کند تا سیستم‌های دید مبتنی بر هوش مصنوعی را در پهپادهای اوکراینی گیج کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/670117" target="_blank">📅 13:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670114">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hw_ktQdcDGamglUNchTpKWf--1FBtZATvDYV5MauRvC8pLZNyOa4t1bV4sKw45N9zivHR59hcXyFKEA9Y3OfFpFJljT84zf7A25VVhG8JQtX2E44B7zoLq1K9h04JvfbaqkcS0iIPBF68s8ZcrX4bHrBbN3OFgmAyYNiqKvcz0H8t2Dm5otw6CtzRrVVJIDcC4cpvJCxligRfNpAFsR07SCcuL1aOOZ0I_LmqpvBHeJt3Yd58TZJQQyJlgStNnnjbCQ2UC8FmwdjZW-pqKayojVU4g2FaOdcazWYBUISJM_3c1EO3ml0dUXcAYihzB06pQXIteqBpjco-luZ1bWkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8-giZGMnX6em58u9dT1rXaUbBDr5mPZVovn-Y8mCqCer9fL6gdC73z1Spa5ilgs-YPeBTBgMe6gEmQWnVNbQk1602pkFjO0TEz3o5p0N12ZT-Gqwd8XQi-tbOhQLXSifeXcj_tdmQL0AZTwRBgm9f0qEFSBNCzzJdpUdO11fDnKlm2ltT2RlJdZbPGjoCtNVa0IxK4zLi006dZKKI5GrEbRy0atvndIX7X_DQSTpHsgSZu4ial_2Bqdrz6LDncjJuOdwL4E5qtuFwo1Y2JJQfHWTTZPC018POwMGCIqssY3vTORKJKrjV5PvTE3Ml74rAqAjmaAwE_oZdZ_SMlJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feWmiz18AIp6pP2ffKkvC-fxjtWYGfDMhZJwzH8VqKOHeT6KxBeRFzUKNVZBuLDf_ejIi1yd2-TnlqwZs1WiLYdMiZDXlpmYhscUPXMCWVL-igejdtNyLm669OHCaDDOwnxbMK2thntT6-kXsFarfIJdNxt4cTAmi5eve3nfRyjZqNGB2BfcUniCx55KB_XUSigxXW-cxercmgALU5m0grBrsErek55w1GC3bt2dNkKJB3JaZTeb82ixInB1KT0lxhhto0jHezMM9np5SDHAMFRahzIIpsfUkG15aI-FoUALtL84j2l4QmTfUbzX_LSedNlRWSu8r4KId2KSDKGz7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بیش از ۶۰۰۰ عملیات فنی ایرانسل برای پایداری ارتباطات در تشییع رهبر شهید
👈
جزئیات بیشتر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/670114" target="_blank">📅 13:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670111">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قطر از تمامی مالکان شناورها خواسته‌است که «تا اطلاع ثانوی، به‌طور موقت تردد و فعالیت‌های دریایی را به حال تعلیق درآورند»
🔹
وزارت حمل‌ونقل اعلام کرد که این اقدام به منظور حفظ ایمنی عمومی صورت گرفته‌است و شامل قایق‌های تفریحی، شناورهای ماهیگیری و جت‌اسکی‌ها نیز می‌شود./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/670111" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWyq8WqYkmbm3L7broEgQ6nCpdFhNdsoO5A7zlo2Z5ey3epfgh1JvromrnXi4Ao5hv8-ZyeFWnHETlSOCGwT8Ogm9wzWeeygHCKbnbEzr5bAWJBTi5SIo-Edk65fiH5Y4mgGN1Y78VuRzfJ8o-xQ4MzmC5XllikF7pyKHoSL4O13wcYDSQdJk3q8A1YASMDWaHZZIdM4NM5r3StteW8q5sxTFuMei-dcyWTmiYmp2tma9gFM1UThqixLRyy_c41TN6EcHIMVI20aBFUacDTEIwVOOGlDtqVgM7P7gGHKmn3JIvvc3tpgEMJfF6Gzas3xJc7zafFukpMA4fIy4Qtr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از جرثومه های فساد عالم هم داره به سرنوشت عموی لیندزی برعندازا دچار میشه
میچ مک کانل سناتور ضد ایرانی دیگه هم
به سرنوشت گراهام دچار شده و به بیمارستان منتقل شده و هنوز وضعیتش مشخص نیست
هر کی داره اینا رو به درک واصل میکنه ان شاالله سرعتش رو بیشتر کنه و ترامپ و نتانياهو نجس رو هم زودتر به جهنم بفرسته</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/670110" target="_blank">📅 13:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670109">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
گلایه شدید نماینده مجلس از وزارت نیرو: وزارت نیرو فاقد استراتژی است و عملا هیچ برنامه‌ای برای رفع ناترازی ندارد
امیر توکلی رودی، عضو کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
عدم تخصیص بودجه و مشکلات قیمت گذاری بهانه است و ناترازی ریشه در عدم هماهنگی و نبود برنامه دارد؛ بسیاری از صنایع معدنی حاضر هستند با هزینه شخصی خود برای جبران ناترازی برق وارد میدان شوند.
🔹
فقدان استراتژی در وزارت نیرو به بحث برق محدود نیست؛ در حوزه تامین آب و دیپلماسی آب نیز هیچ تحرکی وجود ندارد؛ در حالی که کشورهای همسایه مانند ترکیه و حتی کشور افغانستان برنامه دقیقی برای مدیریت آب‌های مرزی دارند، ولی ما برنامه‌ای برای جلوگیری از خروج آب یا مدیریت رودخانه‌های حیاتی مثل هریرود و هامون نداریم.
🔹
متاسفانه وزارت نیرو فاقد استراتژی مشخص بوده و به صورت روزمره اداره می‌شود و عملا هیچ برنامه‌ای برای جبران عقب‌ماندگی در حوزه رفع ناترازی و ورود انرژی‌های تجدید پذیر ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/670109" target="_blank">📅 13:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhxvLj0WF30OI7NgqjH7JaQZ7lbSXxLzzrOlMmckFX-MGSelZsu4_-QBu4w2njexHAz4tX6KHLbh7XlBvImlNup2wW7BxpHgd1XwMGto1IlDoC2n8SkshtGyCkbc3V47z4zWwMWcbjyZ0N9sUIzjU_-9ohWxU7rcMfDJ0TGOyIkWOePFupcWkvW2kELG-Jq7oa5eELWMQTBt3EeemNyQav6nIgCBvVd0Th-u7z_87GiyVeR9FuW09vx6LeRkAp7LfheWL_aUfXPxMi0EA1h7cw04pDg434bt4Y81yqsxoWbMVaIBd3kWUVenTFjpXrF__mBdXEKu_XN9ILGA_1xJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست انتقام از جنایتکاران، با حذف سناتور ضدایرانی، به‌ روز شد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/670108" target="_blank">📅 13:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670107">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1b870e4e.mp4?token=v75xOa74Eg9ufjK_bnVDYY0JhIK017u-uIZdMBC0Cxsxcem_p-PeuAgYSxgXq_-WfwXzANqlbD-Vys0Uhus4t3P_t67tV2SI90bRGSdlYJM1dqHg0HgklOZAOMPjglpslXRAgMRPvpuz-xyCRQ_FJPsV-X2NYKB-tHbTMQthXWnGnE2NeUjRJdK6nSKc8E8DNTtiGt5xNia0Kxbz2AxmQNRrbI1ox7SNUK6jaoSPyJgmMpJnNNQsPhob3ERZhExpuEgQ2OV7T0tcCRwPoyL6rWQX_5fVb8Ut8a7kAD7MNOF5QdQ328z5eReqdM8Cu66UdOTJYd2-XAVPScWnyzhm7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1b870e4e.mp4?token=v75xOa74Eg9ufjK_bnVDYY0JhIK017u-uIZdMBC0Cxsxcem_p-PeuAgYSxgXq_-WfwXzANqlbD-Vys0Uhus4t3P_t67tV2SI90bRGSdlYJM1dqHg0HgklOZAOMPjglpslXRAgMRPvpuz-xyCRQ_FJPsV-X2NYKB-tHbTMQthXWnGnE2NeUjRJdK6nSKc8E8DNTtiGt5xNia0Kxbz2AxmQNRrbI1ox7SNUK6jaoSPyJgmMpJnNNQsPhob3ERZhExpuEgQ2OV7T0tcCRwPoyL6rWQX_5fVb8Ut8a7kAD7MNOF5QdQ328z5eReqdM8Cu66UdOTJYd2-XAVPScWnyzhm7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سایه VAR بر گل‌های تاریخی مارادونا
🔹
در بازی ۱۹۸۶ آرژانتین-انگلیس، مارادونا با «دست خدا» و «گل قرن» درخشید؛ با توجه به تکل خشنِ نادیده گرفته‌شده و گلِ ارژانتین، حضور VAR هر دو گل را مردود می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/670107" target="_blank">📅 13:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcr-06ykV4u06ZPjc8dDQE4Ht_RzjdPW34G8mBMfwIykMqZO9M56SVt3vF8qUsCjT9sVJONvLpycgV1L5u81wpTs1GE1hi5cF1iY1jtcESRFUPuLgZwHhEikzZlHsA97rAEPukgAimwuD_jOLO4zLAOVgKOBH_WJ_T4xOWnVGQJvclYbyAYZDJs2702BJp5_uPItQNXboccwEi7f2u-eEVZ8AkF2riDYJCZQLiUkK3AoFBvzpB3gsKHx4D0oq_qbqNhOBQ8sQAKann_o76OKt5-jqGRa60L0xuXl6uDqb-7LDQpo4CuKK7glpevpB2tZdzwelfDEbDyOZovRvT_7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه پخش روزانه خبرفوری
مطالب مورد علاقه خود را از طریق هشتگ‌های زیر دنبال کنید
👇
🏸
ورزشی |
#ورزش_صبحگاهی
| ساعت ۸
🍱
آشپزی |
#آشپزی
| ساعت ۱۰
🧠
روانشناسی |
#سلامت_روان
| ساعت ۱۲
✂️
فوری استایل |
#فوری_استایل
| ساعت ۱۴
💰
آموزش دنیای اقتصادی و سواد مالی
|
#دارایی_هوشمند
| ساعت ۱۶
👑
معرفی شخصیت‌های تاریخی
|
#نامداران_تاریخ
| ساعت ۱۸
📚
معرفی انواع کتاب‌ها
|
#فوری_کتاب
| ساعت ۲۰
🎬
معرفی انواع فیلم
|
#فوری_فیلم
| ساعت ۲۱
🔸
نهج‌البلاغه
|
#نهج‌_البلاغه_بخوانیم
| ساعت ۲۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/670105" target="_blank">📅 13:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjaSGiFNgcfefFNt0Pdp1DoUauBjE3eNmHKzvPNxtFCsHoAmWqbCYfr5H4oqdtXASTgw6O7lMJY2-Z1hROR4BPcB0R-hLpMmqGg09TnE7fdx9zCRuKPuWL6ra5FILLXbMmLriR9doiaS_Xcfqmxd5ieKFiC4xLGqxIc0pAneUhhgRZP_frQ0GUk686SwzDG3aWHCvJZNOGLPAs_5f8fo5-2O9dQv5vTpu7uP-2YiuG_UclsluwQATc11vNZKK-o9ECPA3_7tbGWJoKm5uNosfXkHPtQYiuL3TZ66WbvMl2NjFnDECbpKV4h59wdxrPE3YFqy_vnLTv_TahZLGCSbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف محراب تاریخی در محوطه جهانی پاسارگاد
🔹
رئیس اداره میراث فرهنگی پاسارگاد از کشف یک محراب تاریخی در جریان مرمت و ساماندهی محوطه جهانی پاسارگاد خبر داد.
🔹
به گفته او، عملیات حفاظت اضطراری و مستندسازی این اثر در حال انجام است و نتایج نهایی پس از تکمیل مطالعات تخصصی اعلام خواهد شد.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/670104" target="_blank">📅 13:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBRMFLFmCzDqKsk5fifFNz9yMhegVybGVpqx2OeMwiLpsqRDCCt4AyQrdFFI__8F_3AcA9FmpCQ8HQQssjMBAlu8GqBUVJAEq_aBAyA-hOiuNMVCMMO2Dyft8Ww6-qmfQJAEmoUaRoV-teF3lWBJ3R8D07finDkFjlh1xGJFiTJYwWp2pYGkPiXl10bAmWIkcL3eC8qynS5hsN05zKFxaDnCh_JGJ_FONwi8QgPHVyGZ0fJ8xS4uHGHOrquDdecNXXospSTWscg7aEe_MXCxCr74F7QQAgsOrjiVjsxYWykPpQYfO3ktCkUtV2kx1Kmd1XbC9AmuV7efAwNGfXgFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه شرکت توانیر درباره نحوه اطلاع‌رسانی محدودیت یا خاموشی‌های احتمالی
هم‌وطنان گرامی؛
📢
اطلاع‌رسانی مربوط به خاموشی‌های با برنامه و اضطراری (جاری) صرفاً از طریق درگاه‌های رسمی زیر انجام خواهد شد:
🔹
وب‌سایت رسمی شرکت‌های توزیع نیروی برق
🔹
اپلیکیشن «برق من»
🔹
نوتیفیکیشن و بازوی (Bot) «برق من» در پیام‌رسان «بله»
🔹
کدهای دستوری USSD
🔗
جزییات بیشتر
روابط عمومی شرکت توانیر</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/670103" target="_blank">📅 13:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670102">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: سطح تهدید دریایی در تنگه هرمز همچنان در بالاترین درجه خطر، یعنی «شدید»، طبقه‌بندی شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/670102" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670101">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByQ9oBSA7oDNlL8Ux4upC9cBwUqzSL3wTfSCOhaI0SO2GwLPewv3_8abhtaVTawbxUXAB4RV-VfmzFKOdsdj40einpLSCq15apHsCY5osRr8upjX7YdG69RuupmltL9CAQMmM0ViKCtwO_mqGXvBmAOULZkKd0c-RDXJA9m3tv_bms3ryqomQJRzK79vwraUnVACNUSzC4ues5feKBW7MUASWyTo0vOzA9Zr_hTntUbadjqB3rmn7pLVtrVEy4jQh4Vt9aBKMlNUVI_vWk2CwAOgLLiw0seu1G8EtYbzZoDNpRDl4JjkTOjSZn_uzjoVQOWtxC7U9RgSG0S_dpjqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه شلیک موشک‌های آمریکایی هیمارس از خاک بحرین
🔹
کاربران بحرینی با انتشار این ویدئو نوشته‌اند که دولت بحرین به طور آشکارا خاک خود را برای حمله به ایران در اختیار آمریکا قرار داده و نباید نسبت به حملات ایران معترض باشد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/670101" target="_blank">📅 12:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670100">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: نتانیاهو در حال بررسی امکان سفر به مراسم تشییع جنازه لیندسی گراهام است
🔹
در صورتی که این سفر انجام شود، به احتمال زیاد با ترامپ نیز دیدار خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/670100" target="_blank">📅 12:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670099">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
آتش‌سوزی در کشتی کانتینری در نزدیکی عمان
🔹
سازمان تجارت دریایی انگلستان از وقوع حادثه‌ای در ۹ مایلی شرق عمان خبر داد.
🔹
مقامات نظامی تأیید کرده‌اند که یک کشتی کانتینری در بخش عقبی دچار آسیب‌دیدگی شده که منجر به وقوع آتش‌سوزی در عرشه آن شده است./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/670099" target="_blank">📅 12:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670098">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6ea7e9ce.mp4?token=jo5vvrzNJySn1jYI5q9RqSe972Y2IH2dx9qCR2xBbiysXZs4eVo6wM6H64R7SsABm3lmsb3A_RNXCPhL4S2kj97AaN7qw9NYBlnFFfGrOqF4E4_DfZEwf3hQIRvW7ZbtUd7SaAALGCLyRuEmOgK4qN48A_90DkXogAs6Ju-bnN3i2W2sBgxXin9dndloKtbizkrGX11uTQCkHL5kkK6Iz0bXcA9pSGtj4eXC9qtD7K2hpuDPVXwpJbj7q8sm8uAIoT_rc6UWc_ZMeBZ42fQGwPcX7y5sF6-tekrIGbF9_p8yq3b229AXpXaxrG2R96SuGchR2hatafCPQzNxO2Kvgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6ea7e9ce.mp4?token=jo5vvrzNJySn1jYI5q9RqSe972Y2IH2dx9qCR2xBbiysXZs4eVo6wM6H64R7SsABm3lmsb3A_RNXCPhL4S2kj97AaN7qw9NYBlnFFfGrOqF4E4_DfZEwf3hQIRvW7ZbtUd7SaAALGCLyRuEmOgK4qN48A_90DkXogAs6Ju-bnN3i2W2sBgxXin9dndloKtbizkrGX11uTQCkHL5kkK6Iz0bXcA9pSGtj4eXC9qtD7K2hpuDPVXwpJbj7q8sm8uAIoT_rc6UWc_ZMeBZ42fQGwPcX7y5sF6-tekrIGbF9_p8yq3b229AXpXaxrG2R96SuGchR2hatafCPQzNxO2Kvgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجید، بازیگر قصه‌های مجید: ۴۸ سال دارم و ۵ سال است که بیکارم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/670098" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJFx-o8BCmEK7j93PlMBsHSlxhZuXHgbRLX2GlLE7eu5ZFcOwcOxkt2ycO_ydjNSnrH9_4NKfZTBr51pze2GzEzlE5dbZ7bsjsZD0lYPEsNb9-z8J8xTUiCtH1GyHlvJytE_yDk_z8jK7w2MUi503heP4VVIbypl5-eAFr8zs-r8lLEJQkMDGaFT9ajC1oUmGMLIXBil_4rgdVZqjeBwgXZaD6ufk7ab-5aqSMvMAQs9A_J4SfTMrVA3V2glcCD3P1oeaSOsc3HibHeN4YPqYj9HRVRQmU8YKdhvg9lXjtNppyzOxWwoIAn2_Rfmeej9CCrjYJdzeCUHVL3MeZXc9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز را حفظ می‌کنیم؛ انتقام مسئله اصلی ایران است
🔹
سرلشکر رضایی، مشاور فرمانده کل قوا، با تأکید بر اهمیت تشییع باشکوه رهبر شهید و بازتاب بین‌المللی آن، خاطرنشان کرد که این حماسه مردمی موجب خشم دشمنان شده است.
🔹
وی با اشاره به نقش راهبردی تنگه هرمز در تأمین امنیت و منافع ملی، تأکید کرد که ایران با اتکا به توان دفاعی و ظرفیت‌های ملی، از این گذرگاه به‌عنوان عامل بازدارنده صیانت کرده و آن را حفظ خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/670097" target="_blank">📅 12:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670096">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGE603t4ntRVyYiOC_paJv24F0sPpjK7O6i__oZ_NPRNW97qp882G0NOmp9DZF8sLm9H8cH4xuWGMjq0K3UTIUylJKB5SB3NHJ4cnZXnhWgsO_ybtD9nr4HPp5bqMXf9uIzwqKnoZpL-V8EuYpGA5ZKikoHHbHKzHW0Nf6DzUKRsLqyNQXqgXe4b0t8LAiYThaojgJv1uWg-CelWewV54qKmU-UBpE8dTN-6u6wfRHkzlQMgWTELFNNXaL22H3TEWUamweXtEBOzdgkZzzaBw_2_SYZhCB_eJh6PanMFMv82XtksXQ0T18eBxBCZHKXmqzA2Er-QZqKmavnz7kLkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۲۷ هزار واحدی به ۵ میلیون و ۵۶ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/670096" target="_blank">📅 12:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670090">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtrCUsUIFUfaW9eWJYhX2XA_P9pE_DM2vI_j0zT0k7IBFQ_PlYFhz5JZdLgEDzdwWYh65CaIrZAT55HZYT35uzO2_EnTPHi6wQ3yvholK_5TrPkgfgUAqXHFPBY6QNaZtC-5_iuG2ZcyEa1pl2_4CJgkjQKm5akXx9iNwzFphii8RE9t0K7h2ShoLWZZsPYNr2OwY4IfNGrOqDz7nsxUuk_YrBlXCupaAdn66V2RtUuQmVGIanPcBNukQZPszl9JrnzppVD-6TWkZeSF5d4rMsu-4nXNM8RQhpYscWD5klMG24O1lYsdZk47WHUdXcaX5uGq77Bx9Cd5w0gN8GnIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_8DbyJYcjbpZDBV1N6VCbqGztXdZaH9ecbBip9e4oZA56vwxixMSdQ_1ZfyWJQBexWBF-NJ1eFJ53-RFROUr30Rt1nyKMsvFBi0dyDGjG_4iORA4hHq0farqFBrXIoho2yIqPX46hd_1hpEpAcd8nPyXgU623p-PLsI08xypBdJejnp2mhG7fBK0XhBlt6csBixpUVFttiNbW6BpdeEtHHGGFKXZPzrcjqYnj3lg01Vy3ZMLIc0ajauo7SSTcm8XdUbtbeyVtgCzbBSn0vbqTlukdSA3RW3QM_pFFfsQG1S2R5QOSo93IIivrlhae2V-cUXIRyLbueEUm0EprJfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAuLlFqpr28SRM8IQB7l9PzHER8O7UAkXtfMJJzji9qOhI80bQPzdcDguw_COYsRZoNwbNc97DTdNZGBIj7Qyq1TyWEMQGWUGHT369eh9CcHrz6WztwcL52dSLcdHFEefsd9rS3MY_QGkleyZldfUIFOZUIDF9B2E_1cUGt07Q6Ca9r79qr6Kt6yb1iuwifKPRY4cZwQNtgUy5JS8w50xlwOKB7g3K3a18d-54sSAtHRlASSrT55aDSqQeNkJ1J3iDkhEFzx_2ys6mF576DHC3iBDW9iT7Ww8p89HvclnJtIPPU7LQaAp1Q0GT1lhaa28Rcm_OPQ5RG0ONr61spi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNOBl4LjCORShrXiYFHqDgkf3Hlqb4JyOPWF84o4jxkyA5o_nSIspSLw0r5gHYO8SKI8UQRz2_QUz4HXW4EzLkaqTec9Sy45lxRjakbkFW-Ify7qweKDfQcdlDHurZ_m-tXUKnpZnEgaNUZRHmwuCwWgS3f3kRQ3x0x7lcxFlSETN_vCvBSlwBkGWBDm58Frwj1E70EdO9365It_Lsrf7a6VCcbnemZniNGweKaCA_mbeg6O7paFt__VCsGV1MvE6rexTi8o9Vc0acK42XUiJnGwgY9NZnE9HQX9DY1a46-qx4RqjopgX8fxW4_xZUcb7h-bJ-njbOj3IBtxwYwAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3JeGNVSZZqvtLk8cSmPOkzpgBbtdZGSJ8XvoIS7eha9VvTEIYjquifHrKV-xDxz6spUZh7RBy9uQ5BoWc-d9VbmH5zz8k-cf_vRxaGzhmycwjvK0Jvqui6xFhKV4zpy33BQIYWAijVWq7YJ_QGmYiTnyH1IDdaNpKwNajkOr4bg53oapZgvfyQ5K0Jm1LQFUklIbY4lXhuxWRWXYQco-uPEb1m7pSRLuV6EDPOyybCHpLDS9z31sIvC-_4hPPu93V18L06wuajgruacOI08axwQLE0veElzWWByLc65PnbaQvIe0Rj39PWJjVAkQwUtfrb4dG9i9BQWRE4aII3u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne8Ks8Ymzw0SrM6zrgWFJAH9XCfbQCQO2zSCO-ylRvmh0NPR6ybK4rMYFv6EjYZnP0qdiT96EcJDsQaw7yAHCZUFlju5TRQ_tdhB0gjV2or3rKDiumIOrzJ3IpHytrwMEDaEOu5a576R9VQpJXFZtH3QyqH-XRQhvUXwGTd4U-8Xy-FEH9f9qt-temSIKofMIDBSsv96uw_PXrDI8qLTNvwhE6ojCFsyA2V-sxD7ER-4Cmt8EqF2qt7Vo9pRQNPUS-uy3pq-msZEcxiMZSj8qtCFArH41igP9jiOmbc9hbRFhMjDbSL_iNroh35OgFAxQL_mXhNtuccb_-x3xMSoOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شما تنبل نیستین، فقط نوع خستگی‌تون رو نمی‌شناسین
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/670090" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670089">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c647e449.mp4?token=N188iNxLYIpWP46Bm9upyGvK-b_DC9nUWK0WlOfgfyPOla1s3zQJFkpGcvtbiKVGCZVP8SSJy5Vk9OfqXoqE9cycC4bQV3Xot0IpulFmLcLl3ucofa5TnS7dOrfxqFmfQdA8-LW1mmUXWC_sI6b80vjXQbV7X1UcabyAaSy4jowlcbYcsi3VAyfzMpOdgyYqWsEsVPZNwCRFmEmNzrwieUk4PbSGQIdoL_OS7ektpDYPrfgjrjDC5ZM0V9Vf42uWgYEClIUvzTsmoItxqZaqWZrDWniq5AayJ5wAeMV_rTovZZC0Do0i7hEH8WAzsIgIH0sBySXvR5lA9WP8Obb-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c647e449.mp4?token=N188iNxLYIpWP46Bm9upyGvK-b_DC9nUWK0WlOfgfyPOla1s3zQJFkpGcvtbiKVGCZVP8SSJy5Vk9OfqXoqE9cycC4bQV3Xot0IpulFmLcLl3ucofa5TnS7dOrfxqFmfQdA8-LW1mmUXWC_sI6b80vjXQbV7X1UcabyAaSy4jowlcbYcsi3VAyfzMpOdgyYqWsEsVPZNwCRFmEmNzrwieUk4PbSGQIdoL_OS7ektpDYPrfgjrjDC5ZM0V9Vf42uWgYEClIUvzTsmoItxqZaqWZrDWniq5AayJ5wAeMV_rTovZZC0Do0i7hEH8WAzsIgIH0sBySXvR5lA9WP8Obb-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله سنگین اوکراین به پالایشگاه اسلاویانسک روسیه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/670089" target="_blank">📅 12:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670088">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIlc1qEJfEe3YWrI6N5pLkGkoOOYd8Hpb2CNBnwSFIvMZLURQrn0bd5eqBTdO0myBre3Qo6AxW_tiwB0mwWDA1vNHtPaG-5tLVMtc0pR0naFpTNWvfm9DcaXNXel61Sru2FaUQHEInpHdpU3GiwGvO8pOPHYryIB-p8_CqSffV9hA8DZU_IE3NPs2xhdy3NdsTDEGCYLyuDcEhe-_RG4NaEmBNqoC3z4udIMXeQWilShwJVEvwiatlbWwoXGlly26yh6B9w_uINzv9kQ-eldbXAYDVM-mCTwGUxd9OKxt0EgbIm4WQa42lqLzD9LEMdpbYjSlddR5z-1k8q0qZA75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شلاق‌ بی‌برقی، بر پیکر خسته‌ از جنگ فولاد خوزستان
🔹
در روزهایی که هنوز گرد و غبار جنگ چهل‌ روزه دشمن از شانه‌های صنعت این سرزمین فرو ننشسته، برخی واحدهای بزرگ و حیاتی، مانند فولاد خوزستان، همچنان با زخم‌های باز و عمیق ایستاده‌اند؛ زخم‌هایی که نه از جنس آمار و گزارش، بلکه از جنس دیوارهای ترک‌خورده، خطوط آسیب‌دیده، تجهیزات ازکارافتاده و امیدهایی است که برای بازگشت به مدار، به نفسِ برق نیاز دارند.
🔹
اینجا سخن از تولید نیست؛ سخن از بازسازی است، از احیای آنچه آسیب دیده، از برپا کردن دوباره‌ی چراغ‌هایی که خاموشیِ تحمیلی، خاموش‌ترشان کرده است، اما در کمال تأسف، درست در همین لحظه‌ای که این صنایع باید بیش از هر زمان دیگر مورد حمایت قرار گیرند، زیر فشار محدودیت‌های شدید برق و بی‌برقی قرار گرفته‌اند؛ گویی بر پیکر زخمی، بار دیگر تیغ گذاشته می‌شود.
🔹
ادامه گزارش
👇
https://www.khabarfoori.com/fa/tiny/news-3229687</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/670088" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670087">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRbnXGnN4W49Hf7q_WsfAvlssArA6ELVQmNRxKQyy1y3lAriUV4Df_UmOj_ORKMQoNZcsG8pconwSDFRM4D7trGnrYy533-4caOcRHGZz-NDYzcuOf5TcKAbCM_dhRr96kLnL1oGpqieVp8wqnuy1KIz8eRz359aJrRSgs-uhjtSvP0D6JtdfPJH5TN_nXioQ58fA7oakPHsUTdtRezE_Obbz4kQmEuaDIA06jpLlp3WeWsMGQFc1B4GrRCE5dmgP08MegmRjMzvFvjF92Qptp-nSdvQ9RzzZ4nLqhNUY9mr-9hbIb7dyazLi_e6dBOD0qj-gQ4vGWybWkeXHBJ1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نزاع کرکس با شغال بر سر لاشه
🔹
عکس از فریبرز حیدری
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/670087" target="_blank">📅 12:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670085">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fVX4wTOi1G2CfwESDyg5Iv86VGE85adsJKm-13RpLFTYGbGsGBP04aZKeCHHuRtgWeB1jmUyGjyuhZhif9-KnAYvLgfGzkZxhsAc6SrrkV0u5uG_qJaqo4OlR9J0Y5cxBp6up_GU-mYWwi-QqB3dBLWlMzgH460jYz2gQv51i9Ld96kJUOqRGTuITcsCbPA4Npx_rW9ge9XHJgub_Gw30F9MYHiZZuwOtQT2I7TOvygxi4LQytaro0QJZoc_48URUBD-vEGZS_XbLYomKUqFYhWauK7MLZYnvTLHicHfkYTWD8qJfM4C6No4L1lgkbcS3UTRgc4wUqVwZ4c6mL5E-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOuZoAoE4LtL6rUPKqHspM2DSn5Spg4zV0DUuVLiaA8BVNEi4gl1gTdfNrmob2IAYllIr1OBDdVKaoGY_Gpvh78yrvbyo2_Dlp211P_02B-hXtSDC30EGj56ObV4TRxEftSGMoQNad8mvGfjx7EH9cI5_U7oKghBIi20hiwEHdiQp4hn6DOzhyzWIx_jZxtxMXAOjjgIY_njhs6kD0ytNHUrN_lHjSF1sydLfWk5-X5CXRHg1E5dqdr8gLdZPPD_HsgT_6RQCfImCiCylQrEXfjD3XDDouCIs__skyYZphE2vD9QlO6pO1qVZ7QtBvY9GQdvXnT93HHMfNy9b7-a4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فیفا شروع کرده به فروش چمن‌های جام جهانی ۲۰۲۶ با قیمت ۴۵۰ دلار
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/670085" target="_blank">📅 12:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670084">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پروازهای فرودگاه بوشهر پس از ۱۳۳ روز دوباره برقرار شدند.
🔹
ثبت‌نام حج ۱۴۰۶ آغاز شد.
🔹
۴ روز عزای عمومی در قطر در پی درگذشت امیر سابق این کشور اعلام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/670084" target="_blank">📅 12:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بانکی‌پور: تجمعات شبانه تنها با فرمان رهبر انقلاب می‌تواند متوقف شود
امیرحسین بانکی‌‌پور، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تشییع رهبرشهید از نظر کمیت در تاریخ بی‌نظیر بود و دیدیم چگونه کشوری که ۸ سال با ما در جنگ بود، مردمش عاشقانه در تشییع رهبر شهید شرکت و‌ برای ایشان عزاداری کردند.
🔹
همچنین در تشییع گروه‌های داخلی مختلفی را دیدیدم که مسیر فرهنگی آن‌ها از آن‌چه که رهبری اشاره می‌کردند، متفاوت بود؛ هرچند که رهبر شهید بارها فرمودند آن‌ها هم دختران ما هستند و اگر بدانند دشمن پشت این قضایای بی‌حجابی چه برنامه‌ای ریخته، آن‌ها هم برمی‌گردند.
🔹
تجمعات شبانه در ابتدا به صورت خودجوش و بدون هیچ‌نوع سازماندهی ‌‌و دعوتی از سحر شهادت اقا شروع شد، اما ادامه آن با خواست رهبر انقلاب، بعد از مطرح شدن موضوعات آتش‌بس و مذاکرات صورت گرفت.
🔹
بنابراین تنها با فرمان رهبر تجمعات شبانه می‌تواند متوقف شود و مقام‌های مسئول نمی‌تواند نظری دهند، تا زمانی که رهبر به مردم نگفتند که دیگر ضرورتی ندارد و به خانه‌هایتان برگردید، حضور شبانه لازم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/670083" target="_blank">📅 12:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏆
آرژانتین در مسیر تاریخ‌سازی، سوئیس را به خانه فرستاد و حریف انگلیس در نیمه‌نهایی شد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/670082" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670081">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-text">پیش‌بینی وضعیت طلا، دلار و سهام
🟢
00:34 آخرین وضعیت تورم
🟢
03:03 سناریو اول پیش‌روی اقتصاد (تنش زدایی محدود)
🟢
04:21 سناریو دوم پیش‌روی اقتصاد (تقابل مدیریت شده)
🟢
06:07 سناریو سوم پیش‌روی اقتصاد (تشدید درگیری)
🟢
07:02 پیش‌بینی وضعیت بازار سهام
🟢
08:32 پیش‌بینی وضعیت دلار
🟢
09:52 پیش‌بینی وضعیت طلا
🟢
11:59 بهترین راهکار سرمایه‌گذاری
🔵
سیاوش غفاری؛ مدیر تحلیل اقتصاد کلان
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/670081" target="_blank">📅 12:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvh-jfBR8tXMZa5ooYKzGZU6tcJROg8m1WIUFN6mmUwB6hJrPonRAsuUC9Xbf9Ooq-GbzxRIj34OVOTqMMQbz5aixT9UVYmB0akkgUOCDlGnFXjqNNopPb0aUZB2j0LexIW_GTlrIUDeGzJUOq15QRCrJsZAVcIU5MPZwNjOXrAFakcoqOvuwRWOEcyLTK55s3skuS5oPL57S6CBp9VKeoHP_8Gw5blj-DIxXx60uh5qoZP1S4I8V8mcmzN-3osfjP_7uzFeKIwwVGv16qMzd-jqv-1xOTTP7_moVm-XCNPfbSVxdw0iXvHBJAP6wbuVpTVY_8-Apa8HG57ExO0SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسلیت رضا پهلوی در پی بدرک واصل شدن لیندسی گراهام
🔹
بازمانده خاندان پهلوی با انتشار پیامی از درگذشت سناتور لیندسی گراهام ابراز اندوه کرد و او را حامی مردم ایران در مبارزه با استبداد خواند.
🔹
وی با اشاره به حمایت‌های گراهام از آنچه «انقلاب شیر و خورشید» نامید، اعلام کرد که مواضع این سناتور جمهوری‌خواه سبب محبوبیت وی نزد برخی ایرانیان شده بود.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
#Trash
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/670079" target="_blank">📅 12:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670078">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDzzBzh9kU96sP5W87-_XcDc6RS11yPPVcpT8chvZq5iwUcpUeO-9KLczvGs0ekY8qGMk-6Rqyz7okOjrLXz8lnynNzxYwOuccDaZoDzmkGYaRf0JpgB7BCSVG79HRVwnU2CD0Zw1oQp4c972WvcaTDUUF6dkVnKtx2BVB7_G7HcLsBZk7KDmvfpkGJUOs1eoGpThUjwlOBAMX8wN_8ZjoE4vcOVzqrRipzqSlyEIL1j5RslsDsZvGqHrNzfStRc392FaAi55J2WHVBFqjlJ86AyuPduUgiQ__KClXNR_QUzURsTQAX4beQAwIh45AMcOeoYWX9WZnIO8UHGc3SFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۹۰ درصدی تردد دریایی در تنگه هرمز
🔹
اعلام مسدودیت مجدد تنگه هرمز از سوی ایران، ترافیک تجاری در این مسیر را با سقوط شدید به حدود ۱۰ درصد میانگین عادی رساند؛ به‌طوری‌که در ۲۴ ساعت گذشته تنها ۱۱ فروند شناور تجاری از این آبراه عبور کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/670078" target="_blank">📅 11:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTJwajUtECOTMmxPCO1_DLwkcsTnaNs9sIrLfqc5WvaltfYLqeaViwpoeHDcIeJW1LQ_RpgFkltLPhG2kRhiBHb3sAFn6Dw-cMEHs1X269e6OjLhVqM9ULLEZV8m1NHVJ7UFzApwkRUi9a0vPb0PpDGtIUkFEkOgoz1L2Dra84F4jY6NoeMUzn0Khawx8dq-vvACl6R1rf6ERihej2NgS9mwiZYuxZNu5WtdZnSe60Rq8MTZZYqO9O6GGT8P3jUkahodc6IGOXw2elRZ_5lZzzSGeC1xHCmB1KD4wHpiUxJH_BLzOcXYmbxV8cAC5-bmC_QjeEbRF3j_Hx8f2Es-MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
لیندسی گراهام، سناتوری که سال‌ها از تشدید فشار، حمله نظامی به ایران و حمایت بی‌قیدوشرط از اسرائیل دفاع می‌کرد، مُرد!
‎
#تقاص_خواهید_داد
‎
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/670076" target="_blank">📅 11:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803170b955.mp4?token=Nr8xRMiXa6LT9Ky7dJeVKvYHDhlN0eKW4pVRGshcd8SntV4LI9NlyFsXwvBJl6mGRYY5x4akzLzHBm9a2vGbMaJNPBVsm4OSyKppgEoM4cnPdU8eK3d3ld6XySs38iSOXuTJ-WI6cRi92nYBnJwJgpAuwtEKPkxLt9WLpYA2wYRv4V3KSusz1AvkwkvbJPoAB_cdFEjIojmSqTUtHdlgRDXMo7M9Z7aNqYfi4EwcjDMTevyy99N6XRDSoWv1jEFHXt-HykEAFb-2JUBl8a4-PYWoxLgp0kxMDj1izOkeVxF5QxPaGMW3uF0pWdTqF1a_cqKTSgX-XMaQoukV4vfXCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803170b955.mp4?token=Nr8xRMiXa6LT9Ky7dJeVKvYHDhlN0eKW4pVRGshcd8SntV4LI9NlyFsXwvBJl6mGRYY5x4akzLzHBm9a2vGbMaJNPBVsm4OSyKppgEoM4cnPdU8eK3d3ld6XySs38iSOXuTJ-WI6cRi92nYBnJwJgpAuwtEKPkxLt9WLpYA2wYRv4V3KSusz1AvkwkvbJPoAB_cdFEjIojmSqTUtHdlgRDXMo7M9Z7aNqYfi4EwcjDMTevyy99N6XRDSoWv1jEFHXt-HykEAFb-2JUBl8a4-PYWoxLgp0kxMDj1izOkeVxF5QxPaGMW3uF0pWdTqF1a_cqKTSgX-XMaQoukV4vfXCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش گراهام نسبت به تهدیدات یک هفته قبل از بدرک واصل شدنش: حداقل یک عکس خوب از من استفاده می‌کردید #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/670071" target="_blank">📅 11:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670069">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPhrchTgm2br2S0GLqVLMzK69QdgcMe95dEFA8pFITw-5R5YtdyOA2WQg9qGo73HeoR1Lfovzj3S_KFLwMfvIRNzxwoBJ3vTFkSbgAfJhyU2ArtbOf1_gzyue2G8R_K17xwYlKUMfhJ53Rg1MS5G1cVC4yXicJWTF7cMlM7-AzdiwZyhDNihTQe_-XlZHsh-m-l-_Dj7ODftr0IUIKyx2Z47spRmRPW33P45MHP8YgxPN8y7PcTYQax3IYB3YiwOcUM9MDlpekzbPt7pFl4zb55EtXc0REkD0owSSihkuoiZdMrpSthD-gqVR6ItkZV8nCcmST4detFmZTcFK0tjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش مجری شبکه خبر به خبر مرگ لیندسی گراهام: این خبر آن‌قدر شیرین است که دو بار آن را می‌خوانم #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/670069" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670068">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbf218e97.mp4?token=fGqr9uc0P1Ja-cdc9dPv0OxkxRsRMFenkbgbG0R8kFwbOtLh2BVDD1ZyTmiKlAVx18RoDQfOExHcEvWiVV7aNHH1BhnQA1x7_oOvFZHevGvJiOv8dwaemZMJylWE3vKPM6jU1O0OkK-PK0qvWppchNt1eS8O5V07l-wPnQdl1g236RzXoZBvQeOuEReEEl5BKHlPDN3JvxahbkATZBRKcDhnYTDMaon-q2jXiud9FlZArO_EbnPSLSc7jj7rH12iLuW5osuF4h-5TdgU1pGISfcwibd2yYmBv5nExqTXk9sV_ualVxsBFiaqqqsE3fYEcHyilXWgwizplvJc9UeskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbf218e97.mp4?token=fGqr9uc0P1Ja-cdc9dPv0OxkxRsRMFenkbgbG0R8kFwbOtLh2BVDD1ZyTmiKlAVx18RoDQfOExHcEvWiVV7aNHH1BhnQA1x7_oOvFZHevGvJiOv8dwaemZMJylWE3vKPM6jU1O0OkK-PK0qvWppchNt1eS8O5V07l-wPnQdl1g236RzXoZBvQeOuEReEEl5BKHlPDN3JvxahbkATZBRKcDhnYTDMaon-q2jXiud9FlZArO_EbnPSLSc7jj7rH12iLuW5osuF4h-5TdgU1pGISfcwibd2yYmBv5nExqTXk9sV_ualVxsBFiaqqqsE3fYEcHyilXWgwizplvJc9UeskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مجری شبکه خبر به خبر مرگ لیندسی گراهام: این خبر آن‌قدر شیرین است که دو بار آن را می‌خوانم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
#Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/670068" target="_blank">📅 11:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670067">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8836a59f28.mp4?token=N7tHM9QiTctc8ldjayA6D9XJJoPwkSuxs8VL0iXdLkPYcYM11oi4fsmdSDKncK8wrAnAzbuK26qsCZx7_IiCEJBtBdLF6A5gzMxZ2GU2xT_OEbhyIqTpeg52KOncWXOJ2Bhw9KyELDPrGOAbbo-49mJ--JkhBn7E1OekLu3DkeyYo-L4nGGVAsm4t9yb_IQStK1vulLeTbgGMqBa-SnZZC4VvG5WeDSagnkg0gEBYcOwl2B32gXC9rWDujQ2TEiBuU-rUkl7Rk8YiwE-jzSoHAWnH_Zn0mnjk1X_hwhE224Tdws5bzUJHsunvD1E8yyh5H48PinSplSp3IkFBySKkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8836a59f28.mp4?token=N7tHM9QiTctc8ldjayA6D9XJJoPwkSuxs8VL0iXdLkPYcYM11oi4fsmdSDKncK8wrAnAzbuK26qsCZx7_IiCEJBtBdLF6A5gzMxZ2GU2xT_OEbhyIqTpeg52KOncWXOJ2Bhw9KyELDPrGOAbbo-49mJ--JkhBn7E1OekLu3DkeyYo-L4nGGVAsm4t9yb_IQStK1vulLeTbgGMqBa-SnZZC4VvG5WeDSagnkg0gEBYcOwl2B32gXC9rWDujQ2TEiBuU-rUkl7Rk8YiwE-jzSoHAWnH_Zn0mnjk1X_hwhE224Tdws5bzUJHsunvD1E8yyh5H48PinSplSp3IkFBySKkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از بندرعباس تا بوشهر
از خوزستان تا هرمزگان و چابهار
دل‌هایمان کنار مردم جنوب است
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/670067" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670066">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏆
نه کین، نه هالند/ بلینگام پاروی وایکینگ‌ها را شکست و انگلیس را به نیمه‌نهایی رساند
🏴
2️⃣
🏆
1️⃣
🇳🇴
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/670066" target="_blank">📅 11:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670065">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_MyD3frxZWCEBuUcxdnsA_NN9AbFvKBKcdrojJn-r2JJ8-uHVRRjQ7icurkANvjrY60DTZCf-SAixC3NWC6qfzSD88akygnC_a6l_32HItvuaBvSOcCFSZp9J4opdzzEN43dn4dPaNG4LnnILF6Y6DPnJAkLdO0FzvYAn6Fx7X897QBSBFt4mNkP8Rk8BKjOfFEKietzqz38huwS1wEG9ptBUkUkjzYSKvExxdauyZvMGtImHcFvruLk1RmjEFxY3heztjWfvINGKwPR4QyCwVMbo2R5xNxTXjZ2ltTYi_XWPDeo6zanCI6JnzwtegSzCL3-0dXZbuG8OstNnQ54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش نتانیاهو کودک‌کش به بدرک واصل شدن لیندسی گراهام  نخست‌وزیر رژیم صهیونسیتی:
🔹
در دیدار آخرمان گفته بودم که «ما هیچ دوستی بهتر از لیندسی نداریم». اسرائیل یکی از بزرگترین دوستانش را از دست داده و من یک دوست عزیز را از دست داده‌ام. #خونخواهی #تقاص_خواهید_داد …</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670065" target="_blank">📅 11:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670064">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: عکس رهبر شهید باید روی اسکناس‌ها چاپ شود
اسماعیل سیاوشی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
تا زمانی که رهبر شهید زنده بودند، اجازه ندادند عکس ایشان بر روی اسکناس‌ها چاپ شود، اما الان با توجه به این‌ که شهید شدند و خون‌‌ایشان قیام مردمی ایجاد کرد، لازم است چاپ عکس ایشان بر روی اسکناس صورت بگیرد.
🔹
تصمیم نهایی این اتفاق به دست رهبری، سران‌ سه‌ قوه، شورای عالی انقلاب و سایر ارگان و سازمان‌های مربوطه است.
🔹
همچنین در کتاب‌های درسی، شهادت رهبری و مباحث ارزشمند آن آورده می‌شود، اما در خصوص این که در کتب امسال بیاورند، نمی‌دانیم که به سال تحصیلی جدید می‌رسد یا نه و باید برسی‌هایی صورت گیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/670064" target="_blank">📅 11:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670062">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKZpOI2vyIcvwrdeWXzCGHQNzkvvpeTWN7LuJr0QVEsqM_2dONJhUIRxxdtBQm3Me5G6cNSEoHTP0BkdXU8sP-MF_jUCrJG5I4t4uQADjSX-qBQssQjT39D23pV25-4lqx_JEMCNSEafPcK0zgdZ-tsTGQsyVXAaEiD-v8I6oDJ0VJHXyZJsj-oAKxGh1yqB8UsC_ExPOY3i2oUbfyn5xsX4yXdMs6h2FyRoK-g3CNXwuD9axKVM7MdF5viTD_9CLM-9_LUOpnYiSt6nC4EGW53rbs7Bvi9ljgCLRbCH4klkqcMCCIZe4UHyDyFewoRWbUYPqvfOlfved8QR01yafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وکیل و روزنامه‌نگار کانادایی به مرگ ناگهانی لیندسی گراهام: دنیا از همین لحظه جای بهتری شده است #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/670062" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670061">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKkOBwB9x-swI_xfTBjS2gowkhMWSRClFlmst-Xfi1CJoaDZqHVv66OltsyPIOUro63iSc-Q64fHK2McFTYiLTTem4n4_ygv3fvUb_waZSHFJLLJK6ohOYpASbCPze5judNBgYm6VUUs3boSW6eKbsXrd4F0wDPT0J1kQMiIgBn2x6s8a-q-Ssm3SM1bOlqquTcXzstT_wTt3I4VXke91vwdsHLUe9nO5hheG1AC3LnN0UrBKIlzVfJUUC1Vssdwyit239Snp_JYts8MLviY5Dbb7OdMXxlypYOTSJz4P4q1RFYjuttxPu0ySCANrxGNZubgrc8c1R3iNRECYTPbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد در سوگ گراهام: سناتور لیندسی گراهام، یکی از بزرگترین افرادی و سناتورهایی که در زندگی‌ام می‌شناختم، فوت کرده است! او همیشه در تلاش بود و یک وطن‌پرست واقعی آمریکایی بود. لیندسی بسیار مورد احترام بود و فقدان او بسیار احساس خواهد شد! جزئیات و اطلاعات…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/670061" target="_blank">📅 11:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670060">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
حمله به پایگاه امریکا در عمان  روابط عمومی سپاه:
🔹
مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیما بر آمریکایی در بندر دُقم عمان با یک حمله سنگین و غافلگیرانه در هم کوبیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/670060" target="_blank">📅 11:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670059">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ab7e11a0.mp4?token=MnIgSiwpanX1h8S4lxSvM78BVKJGwyMls9ffHNYAYTino9eo4ljyQTOnGIkb5P8lBaSJqzVpiMwguqtVu_MZ4AI4acbaX6R0DAJrfmSdnqv-VfCnUhY4XRLxU-KF4pVJCDUQcneHvtKtaNwJbSaFF9DJ5zTTYX-ysP9SUp0a_DxGzjer6eaZh_9nUfARMGJdCm8B0KQywF7jWca2MF2j2amCkpQ7kqJzUYXCYAQwAJGC1oiIe7tliSxS8OkT9LCeWMCoq5qNJ77GMAZ2UxbWguF_7UOI3o7ToWVct6W3LACyV-wZF8xgiL8v2EuhT6h0SeKXY-9KWLVDriC6e6heARiKkXBKow8Pj3AUvj_5wn1L7WOkGTwI8ugOoIVjA7R6pXd3J_psqeqrf96g736Des0CJXGTuFcdWYF6370MTiqO2EPGRhMVJUcS_GMEYwMbM74ceYKaUYvQIokpDnWMt84ahf9CXwlsiLqfb-MtaKHNjYa3IifBOfWRJlwxAAnhF0RylonurRYJuJzkCCSpPblsSxcRe1gzFvTq9iJzRH20kctt_sTuFteRgCDlCkZTusv8gtJmhQHUwo2mQ-liw8lBy-nqnQuYXdZwu-UjkbAQgLAqOcrPobdjUsqxCPK8CWp0d0Qwv-SI5G7THSIjZgNZPUWDIG7YfaNS3tAAyXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ab7e11a0.mp4?token=MnIgSiwpanX1h8S4lxSvM78BVKJGwyMls9ffHNYAYTino9eo4ljyQTOnGIkb5P8lBaSJqzVpiMwguqtVu_MZ4AI4acbaX6R0DAJrfmSdnqv-VfCnUhY4XRLxU-KF4pVJCDUQcneHvtKtaNwJbSaFF9DJ5zTTYX-ysP9SUp0a_DxGzjer6eaZh_9nUfARMGJdCm8B0KQywF7jWca2MF2j2amCkpQ7kqJzUYXCYAQwAJGC1oiIe7tliSxS8OkT9LCeWMCoq5qNJ77GMAZ2UxbWguF_7UOI3o7ToWVct6W3LACyV-wZF8xgiL8v2EuhT6h0SeKXY-9KWLVDriC6e6heARiKkXBKow8Pj3AUvj_5wn1L7WOkGTwI8ugOoIVjA7R6pXd3J_psqeqrf96g736Des0CJXGTuFcdWYF6370MTiqO2EPGRhMVJUcS_GMEYwMbM74ceYKaUYvQIokpDnWMt84ahf9CXwlsiLqfb-MtaKHNjYa3IifBOfWRJlwxAAnhF0RylonurRYJuJzkCCSpPblsSxcRe1gzFvTq9iJzRH20kctt_sTuFteRgCDlCkZTusv8gtJmhQHUwo2mQ-liw8lBy-nqnQuYXdZwu-UjkbAQgLAqOcrPobdjUsqxCPK8CWp0d0Qwv-SI5G7THSIjZgNZPUWDIG7YfaNS3tAAyXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهره سلطانی: از مجلس نامه زدند که این زن سلبریتی سگ باز را از جلوی دوربین کنار بکشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/670059" target="_blank">📅 11:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670058">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAYZC8AzHXdrHBXl0eMhg3NEZzxA-iy800Osc08EMkA8lhGvsabYORL7EKqc1ArwO91gnaWyTGjx2687Jopgxrej00AZYOr-JW_XhSzPKRjUp94aNFmLu1RTUW-sFdfGYlWjxi7IusvCZugUQ1z2QUCotOMKoLO01omYQGLOqaAHjlfA5hfoPoPwQZegKhHfNACyIICJHs7iXd7Q73cSBiu-seFrR3FOWO4AFnFR9_wPhCuedT9JNfOC3UVXW4iTdIsIA2srdaRN-hMd3pM3VdVoaY-1vvSZxDTmSLUelrNqTx7xi5S8g9y1bTPz-iAW9AkBl5yIU4UdMzI1-nJmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگاهی به کارنامه و مواضع سناتور کودک‌کش
🔹
لیندسی گراهام، سناتور ۷۱ ساله جمهوری‌خواه که به‌تازگی درگذشت، از سال ۲۰۰۳ در مجلس سنا حضور داشت؛ او از حامیان اصلی حمله نظامی به ایران و مخالف سرسخت جمهوری اسلامی بود که در نشست مونیخ از اقدام نظامی علیه ایران حمایت…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/670058" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670057">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/670057" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=rBhnOX-01fw5CUu4Of9HIg0VHrXrVLrVP09WYloZ52cVv31RX9YcerfYGJ8tkzI8H2c8gJIir36XN-Di61T9BxEK2nv_UWJ4JJm7KDwxK3cU-ViJBdNTHy1KpewJGf-9_OlJI1rBIqXp_pBvXxeuMsWel6llKKc5Dt2QzVR8hfXa7kW9oGqPeJ2DSwTwthQ1bgVA5maNurlnmPgVZoc2ScZkQCD5HmW8XViRm_8dkC2LKx8acTfcEp8IFgCjuZSUIm1vLOIprBLA8pwRb4IOvL2xZQRWqpIwMNfUglRRkAP9dkvhWCw-D6JY6W6kUN_O-WPMMybeeOVapALvYR8hwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1408d2321a.mp4?token=rBhnOX-01fw5CUu4Of9HIg0VHrXrVLrVP09WYloZ52cVv31RX9YcerfYGJ8tkzI8H2c8gJIir36XN-Di61T9BxEK2nv_UWJ4JJm7KDwxK3cU-ViJBdNTHy1KpewJGf-9_OlJI1rBIqXp_pBvXxeuMsWel6llKKc5Dt2QzVR8hfXa7kW9oGqPeJ2DSwTwthQ1bgVA5maNurlnmPgVZoc2ScZkQCD5HmW8XViRm_8dkC2LKx8acTfcEp8IFgCjuZSUIm1vLOIprBLA8pwRb4IOvL2xZQRWqpIwMNfUglRRkAP9dkvhWCw-D6JY6W6kUN_O-WPMMybeeOVapALvYR8hwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات امروز سپاه در پاسخ به تجاوز ارتش تروریستی آمریکا
🔹
در این حملات از موشک‌های بالستیک، سوخت جامد و مایع و نقطه‌زن قدر، عماد، خیبرشکن، فاتح ۱۱۰ و ذوالفقار استفاده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/670055" target="_blank">📅 10:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/670054" target="_blank">📅 10:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670053">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بن‌گویر، وزیر تندروی صهیونیست: اسرائیل یکی از بزرگترین دوستانش را از دست داد #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/670053" target="_blank">📅 10:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670052">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76d40a15b.mp4?token=HgtwBVLV5ZF_Ci5_-kEV4_4UO2TRUa2RbPLm7UpyYnMjta7MjPZ8dRcoYiGqel9RWfRWVXDq_8mn6_M1R4Ql8j6nxGaw8LM-ZA3oWKCJGLWhOhHauEo2fezZLMyjk0Pr7-kwIvaMCfkQ6ZBDZMl_PmrmHngTkVveE0BShTdcuSwlApcedWt7b4hz8UbxGHMEBENZ4DPDaa6LQDHzJZ4soeIItpw_z_Rfo29RkXaeAV2TjJxIgNWxD8G7kIdrf9mGC7-aYu1qXnsS2J-H8GXZOGfcDA20VlDchIn6QN-lHOO_hd8RdTVEtWrXYXcDrEifRGqSBFgpUaVoTv--36QP-q_N1gxmofPp2Uc6zg9n2-leejqntzhd4m6-xuCVhsDAk_sl7QDICIOOrlxW472dqEgMZCd3ROH0q_1ey2KFm-28wFxlqFS4gW2hGYnlcy1NMVXYhe0TFig6QzLKZYY8OqNiw80fOXyYfryyyhVqch7X3fTgrKVfiDc7swCy7K8KabPZmAT_9xZLVpz-BCwzLDizx2TKSWiIqC0vrIMLM43D0i796v3dVkWKCUhCzbzSTYjBolL6V8IGnKr8D_CGuHPgXSE-UOw0IVme729HIYXrVwCGrV8WDW1kto6TsuRaKH4oOT4f8hI9aG-hYRPDhyCGneAjSoElFc5Lv_QU50g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76d40a15b.mp4?token=HgtwBVLV5ZF_Ci5_-kEV4_4UO2TRUa2RbPLm7UpyYnMjta7MjPZ8dRcoYiGqel9RWfRWVXDq_8mn6_M1R4Ql8j6nxGaw8LM-ZA3oWKCJGLWhOhHauEo2fezZLMyjk0Pr7-kwIvaMCfkQ6ZBDZMl_PmrmHngTkVveE0BShTdcuSwlApcedWt7b4hz8UbxGHMEBENZ4DPDaa6LQDHzJZ4soeIItpw_z_Rfo29RkXaeAV2TjJxIgNWxD8G7kIdrf9mGC7-aYu1qXnsS2J-H8GXZOGfcDA20VlDchIn6QN-lHOO_hd8RdTVEtWrXYXcDrEifRGqSBFgpUaVoTv--36QP-q_N1gxmofPp2Uc6zg9n2-leejqntzhd4m6-xuCVhsDAk_sl7QDICIOOrlxW472dqEgMZCd3ROH0q_1ey2KFm-28wFxlqFS4gW2hGYnlcy1NMVXYhe0TFig6QzLKZYY8OqNiw80fOXyYfryyyhVqch7X3fTgrKVfiDc7swCy7K8KabPZmAT_9xZLVpz-BCwzLDizx2TKSWiIqC0vrIMLM43D0i796v3dVkWKCUhCzbzSTYjBolL6V8IGnKr8D_CGuHPgXSE-UOw0IVme729HIYXrVwCGrV8WDW1kto6TsuRaKH4oOT4f8hI9aG-hYRPDhyCGneAjSoElFc5Lv_QU50g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ‌های کوبنده تحلیلگر وطن‌پرست ایرانی به پرسش‌های مغرضانه مجری بی‌بی‌سی در حمایت از آمریکا و اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/670052" target="_blank">📅 10:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670051">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jehESRBCfP6XvvNST_2Wl9tw4bpUEtztvkDXnA3eGrCukRmz3JCG7z0qTOeTkJBrK2-RqzJDUCsnNk65qfMSM6hM_lP7gmOOcpbgVlc2gXwSZ1NSqJINo-OAuN97MILklxcfAYlrNjy0u7grcNqPWCZR9M4Rdmvd-YT44xYCFtJAROEzG_Kg-3xGpjejpMAZ-Pa9Elzj1F0_0SCKl7cdNZQuDXN_wgleLMMMI4LSYuVF49B0Dtn6XTRVPIrWhDFSQCyxYRHASu3F0rNMK0DTwwScgNwR2-kYSYROX9SU6zn1feEXlljQa05CrhYFQyjW_V1eGy5kuXgxmRGKGxxl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای نخستین بار در تاریخ جام جهانی، مرحله نیمه‌نهایی با حضور چهار تیم برتر رنکینگ فیفا برگزار خواهد شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/670051" target="_blank">📅 10:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670050">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj6h8bzc-FTJbwCoiS-MeJUyUTXiuktHBsql3-zwjHmUb8BllZ-Zn43Z7xqyKQoMxxgnJj_aBXZO07mgRxKGXzhBQI4MTNxd_TeWVSB8IFpPPKX8qkvDpXwc89KzmkSuQWdmmDz4qvn-uwoX-FGiB34mQ0KcUoOL2bLXFHsZZe-jIGD5Edekl_HXl4KW3Y79SejceaUrqOBfTOrjqvJrOKRkNUZwrnHnT4fL8zQH7HMGYaJvyMa7SVRtqKbFjKNOUi2d1ZY2bcL4JK_IJKJXBX59sWClTbQ73Tkvn71JuBsEo1FRtPEqY2aHrcmxIP8mO85CDY2R8cqqMr2m0nfOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رفیق شفیق نتانیاهو کودک‌کش آرزوی فروپاشی ایران را داشت؛ این آرزو را به گور برد #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/670050" target="_blank">📅 10:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670048">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHp5eyqCAHGozjy4PT_20_1PVEI5aqgbI55nuaJ5EK7lDER68cLhKsZiLzHFiTh8STdQ7eM26jtXNXTBNwfXFpAS0FRhLdg143K5TSluJL-y5mhrLnBZWp7sFL01ZX7WBZqSajm3WLqwgI0UzlLD3fsT7LNzmmLhBXCPLuMo7GFAwkwgUYgYi5YA9YnrcpQaf3gQxHfnyafIEk8V1PjcnZwBEE_8qrOR0a2Lz0CWD22Je2YY9ziQXZOF4Su9erIVxtNeTLuq8UMGymD7rpLTSzsEnciOclvAXHjx-bQkcoM0MCQ3EqVa9myh2zB51oURrks6K2Ey79txBITI6FKCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اجرای گسترده‌ترین طرح جابجایی با ناوگان حمل و نقل مسافری عمومی در مراسم تشییع رهبر شهید انقلاب
🔹
معاون وزیر و رئیس سازمان راهداری و حمل‌و‌نقل جاده‌ای از جابجایی یک میلیون و ۱۳۰ هزار مسافر از طریق ناوگان جاده‌ای در قالب ۵۳ هزار سفر ناوگان حمل و نقل عمومی مسافری جهت شرکت در مراسم تشییع قائد شهید امت خبر داد.
🔹
به گفته رضا اکبری در بازه‌ ۱۱ تا ۱۹ تیرماه و با مشارکت ۷۹۷۰ دستگاه اتوبوس، بالاترین میزان حضور ناوگان اتوبوسی در یک رویداد ملی طی سالیان اخیر رقم خورد.
🔹
این عدد در مقایسه با اربعین سال گذشته که ۶۹۳۵ دستگاه اتوبوس برای جابجایی زائران مشارکت داشتند، ۱۵٪ رشد داشته است.
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/670048" target="_blank">📅 10:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670047">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
در پاسخ به حمله ارتش امریکا تا کنون غیورمردان مسلح ایران به پنج کشور که پایگاه‌های آمریکا در آن حضور داشت حمله کرده‌اند
🔹
اردن: پایگاه پرنس حسین
🔹
قطر: پایگاه هوای العدید
🔹
کویت: بندر الشیوخ
🔹
بحرین: پایگاه پنجم و الجفیر
🔹
عمان: بندر الدقم (مخازن سوخت ارتش آمریکا)
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/670047" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670046">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
موشک‌های ایرانی از حریم هوایی بحرین به سمت اهداف آمریکایی عبور می‌کنند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/670046" target="_blank">📅 10:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670045">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405bfdb289.mp4?token=nmF_QAZ2bpiifos6oKZ0PEdhKvgzE9BpSiT3P2kE75FcEO5nlNArBG06yc0U8mXlQ_YXB5HB3q6kQbfaIlOMtVznqjhzZiwnh6rrFTJF8PII1eznywVuTDwDJ5yiQxaJDnVszDpIIGv7L3IdeWqikX-z-cQjXQj_eNOAWilj4Lgf7qb6X-ThsrizXL4BNWmyg22bAzVN0gvxXYq0ajt3wCED2Ebbgn28aQc6yzHW9eWSizWZrtMnEbCu0AVmzMocljFwGo_0jWyy8te0nsPQvMupBXE0wj3Nl5grAKDNnuOddFaV2QInjRVn8AvJCgJcwL6DD0mNfFjdpJlLgVqTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405bfdb289.mp4?token=nmF_QAZ2bpiifos6oKZ0PEdhKvgzE9BpSiT3P2kE75FcEO5nlNArBG06yc0U8mXlQ_YXB5HB3q6kQbfaIlOMtVznqjhzZiwnh6rrFTJF8PII1eznywVuTDwDJ5yiQxaJDnVszDpIIGv7L3IdeWqikX-z-cQjXQj_eNOAWilj4Lgf7qb6X-ThsrizXL4BNWmyg22bAzVN0gvxXYq0ajt3wCED2Ebbgn28aQc6yzHW9eWSizWZrtMnEbCu0AVmzMocljFwGo_0jWyy8te0nsPQvMupBXE0wj3Nl5grAKDNnuOddFaV2QInjRVn8AvJCgJcwL6DD0mNfFjdpJlLgVqTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این بندری آدم رو میبره به ده‌شصت
😍
مواد لازم:
🔹
آب ۱.۵ لیوان
🔹
فلفل‌قرمز دودی
🔹
سوسیس یک‌کیلو
🔹
پـیـاز متوسط ۶ عدد
🔹
رب گوجه فرنگی ۳ قاشق غذاخوری
🔹
فلفل سیاه نصف قاشق غذاخوری
🔹
پودر گوجه ۱ قاشق غذاخوری
🔹
زردچوبه ۱ قاشق غذاخوری
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/670045" target="_blank">📅 10:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670043">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixtyhhtwwJ_RwQMy9tOy4xYBBDxlqMv95UeJHW_vJZNZCKGCN0WrE4Bc9atidQ6CBZedAdCZpEb0w0Yg9yZqQCNt1sr-ZOrjTr2LYloXNf98gFSAE7kTVQmruAg3PXw4Hdy5xKp5U5tGh1cy3eIGvrnQQW2ZmYgFoaBOwjhtoIsb-XtT_1YDUyFTmJCxYB6hq8grOM1Gyt7-ZgyxyTwoSddbMowug_agujl8JuUESaEAH4F_k_ysqCMQ1-tS2nl-l8Q-_0qpNhCWEWhqVzjP1BAocIwQEAUJUUoROdJjzdcCxiYW3_Jg6Eb8CrDdPo41WotiiwNSA6KvXirfjShilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuHaypww3SVjWCE3tNUFILVvkfiDOGJXVzKuQvIBiDNUJnq09x15L5j-clnkf2k5L7FaWctwxV9QHTwrNNyENdrFe4fXblToBIuGvIlGl0FYS7S7X4edcHMxK291ULBUerB5mzPDH3GCP9BVsMY7GTidC0oCVwFXQQHMx0BBrrw3UgXP21MesdK2qifaPMcDQ4QRipwLqrjhcZulA6teiXekCgQ13nmI7BWkpo6r6cC4D3FdzDYSXM9fpt-M2epv1GQ9uePAmEaRWyQKIzJ7xR_IRBpgWOiNRRz72dNo-LnZeXoD1suhgXZZqb4J7yHBJgm_39WoN4NECTN8lVAKQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/670043" target="_blank">📅 10:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670039">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzgojqwQTVZBeHBalKyKn1k2WRD2C-boKRUiRe8SF708SHDVOElamcK8HAUKA7LKmtLZIZj1E1Agjo0RefEPaCc6xej4AXgwKcXpthq3motBbYRt-TkoAFksfUGSfZnIVexLGwCxoyRV9MydIqRxXKivf4qrNbOVDyg71Mv1jILqQ-hvyVNwJsMC5FroN-jc6rmup9v-M0VgemXLcByN5fTwmiNuAP7y0rjvlBvMLIARQdBT8uodJXa5WjZDIFoIlCeNBPJAmzkTsSswyZZf9psRD94c__q013-u1zXtHeQqUNS2e_YdeuZ_juvr8X3z6Jyndq8pjGa-770rtROOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/670039" target="_blank">📅 10:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670038">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
حمله پهپادی به عمان
🔹
دولت عمان اعلام کرد که مناطقی در استان مسندم هدف حملات پهپادی قرار گرفته‌اند/ عصرایران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670038" target="_blank">📅 09:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670037">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seoIME35ZUse9sWmuUNlLvCBy0r-OjxeH8PfJ7bafjf33qHhN4fGR5frbn1UoXc_hC40ArTYUXPurU54LNopars0dvY_dBDqQRyE5E41lT5dpS_2ph5ffA95RaeCLqQBD9qsJbm6ILbj3DebpcL76L3wFReqJxL4ATYybio2zCids5gXIUThEA6E9C4SaCpxTD3zZ3zUzPi8NeptWDdq_03fZZkmirUXc3qty_Jf6XxHwduA1PjGKl_IDhx6nWosuOjRTDcaGSgvzXjHTj5AjBYCJEzN13bc_OmZCgyvxefEC9kGTkVBJlL1nDS1MyXsFu5UUEziBK3_Bda4tf3QVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسرت بزرگ برای بودای کوچک
🔹
در فینال ۱۹۹۴، ایتالیا و برزیل در فینال به هم رسیدند. این بازی در وقت معمول با نتیجه مساوی به پایان رسید تا ضیافت پنالتی‌ها، قهرمان جهان را مشخص کند.
🔹
روبرتو باجو، ملقب به بودای کوچک با از دست دادن پنالتی‌اش، ایتالیا را از جام دور…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/670037" target="_blank">📅 09:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670036">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWsYOY5c1mwaJxE9i2PyZGoPTp4z1YBDXpPg1kqgCmjVMrT6HJrdtz0uLZ5iT-TcqlxHz9Zx5vakX0sDBZztRdOdJrP_l6MSrAw6k-056tNMizdcabqtXwODLk-ai_ehOL2U4sNGOF9QLEuG-uQFPxIKBy21qAMZJLF2YRo71-5wqjfZ7oN9Ff9UFpjG02nLQwmB-wLd59sQ3htxdgJejij82IV62iZZGaWGdHlgyPcUqiVrNqlcZ8UPgeMnaoSCRUkvJMSH1fifzy4Eylv-peF0mfXuWghu3dK__fZ9xGDm_VWFedYjMIcEaEL_SpkWtc6RW5twcl0po1ptxGMoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: تنگه هرمز را با قدرت گرفته‌ایم و با قدرت حفظ خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670036" target="_blank">📅 09:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670035">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah23B8FDr1WkDsKgOR90-2M47lxqSgEEJO3HKO7cY5-huw92_aQX0K8iiQEIvbZ8HSWtkLIUvvmo-sR1_kg24zctgck3eb5EYr6lzhNZm4015ymnQwHK-fMxMeeL0iq5317z2ixDeMWAifI686s-pxyYjJJFtfFhzciiLetkvygOyz2ah8M_8uzdwsYWTIDivI0DBjICSEzktARwm5Cf7KwQskYQHlBjjfyPLVVHsTqMcZXfEZJV1nwWiX6c95fQIMVQyblEX5_6c-DlKEQchRMGDNBjyAyNjJQ8k2_-xx9TVSrzEgsGLA-R7K54ak8CZuEIXIR1up0vLSXe8xZ3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی
!
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
#Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/670035" target="_blank">📅 09:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670034">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961db740f8.mp4?token=YCgVc0cfyUNUB3jzcbzEXojdehat5CO_yiaIYDI92e8ewHX2YXlar-3cUc9ivp6OsS0d-5H-x-ptySL1oj-dmgqhMlH3tihPi_auVTnRPGShIygzbvlFlJM4IZparAGLIRhJuMaV-mm7ojoDs9IzOkkijjtkjShi-CIwGG7n5e8EQ1J5plgcXMU2jpfFB8oZkDnkd5t_otA-KS7kimAgBAcO6JRk81Z5jzNKzgNnkR6KyTcfLCN7Myj1pbXDUFFBuBZl4JIPGngUxgJRsKE1Y56DY_jIpiYYIqA6wjLrWVHanI8Bf4Q7ZekZlio7_EeAmFf3hyL45OiUNX5P5V-iRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961db740f8.mp4?token=YCgVc0cfyUNUB3jzcbzEXojdehat5CO_yiaIYDI92e8ewHX2YXlar-3cUc9ivp6OsS0d-5H-x-ptySL1oj-dmgqhMlH3tihPi_auVTnRPGShIygzbvlFlJM4IZparAGLIRhJuMaV-mm7ojoDs9IzOkkijjtkjShi-CIwGG7n5e8EQ1J5plgcXMU2jpfFB8oZkDnkd5t_otA-KS7kimAgBAcO6JRk81Z5jzNKzgNnkR6KyTcfLCN7Myj1pbXDUFFBuBZl4JIPGngUxgJRsKE1Y56DY_jIpiYYIqA6wjLrWVHanI8Bf4Q7ZekZlio7_EeAmFf3hyL45OiUNX5P5V-iRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه ناوگان پنجم در استان چهاردهم ایران (بحرین) در حال سوختن است‌‌
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/670034" target="_blank">📅 09:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDm3OOGsWyKUweK8Fb0tWoP-LsnDhdYdxt1S0yNFI1_EwAC3COUkr3QNa9PbtSKcljI8CcYaz44HHgPLWHvvlbIXTxNmXvy7saeZky3kIolZJgdzEfmhdVpyHxoXCyMHUEY9XY259P7SQlRst3AQ_ZEWRzwi2brT6OrBhMRmTbC-31Rehwbvoyh2JGepzyYhrcYv6xQac9KeaurTk6mULTJakKoooS62cG6nw6EmqiR_hio20d1QZWfCBDQbZl40QUVO7u8kC1BfXfq8IMeXxwN2FMGV60aTNhVTYr_Yz1hYtERx2jDbbjNTYJXJYhMncHtsUgMOjAT7am2zqmIkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخشش تیم ملی المپیاد فیزیک ایران در کلمبیا
🔹
تیم ملی المپیاد فیزیک جمهوری اسلامی ایران ایران در پنجاه‌وششمین دوره المپیاد جهانی فیزیک (IPhO ۲۰۲۶) در کلمبیا موفق به کسب ۳ نشان طلا و ۲ نشان نقره شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/670030" target="_blank">📅 09:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای اکسیوس: عراقچی پیشنهاد جدید عمان را به تهران برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/670029" target="_blank">📅 09:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670028">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTYTNc1qLtosNG0ysmHbV_G_vn6vLe_VwLhxfYPhTvsy1NY9s5TjPsKNFsYm9yfYIrs_3YQYhDGB69xrm-GpBaROSoOA3kAeZJaK1t8mBEnGZi_Fqwu0MNdUiF_lEnqReaqzwp-qGM3vKRW5-QaCCobCr4jflqaCtJFdXp9algLr7--yhMS7KDcAUp_KTIx6fLwDBIpmVlJHoVpBSUPFJxlh439BUh5Ikm4Tem5Z4bIj4l7awYzU_VmyDjnolxClqA_TqjxFW9W3Y4lo7-gkDyXopaHiM-J72NGN4HiMz_d4QRbWrRuhPvCgyp8xhrOEU8cE20F0tao3Lo8b3RfP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه منتظری ویلا ارزون شه تا بخری، هیچوقت صاحب ویلا نمیشی!
🏠
با فایل‌های متنوع زمین، ویلا و کلبه سوئیسی، با هر بودجه‌ای می‌تونی سرمایه‌گذاری کنی.
💰
📈
🔷
با اقساط بدون بهره
🔷
🔹
معاوضه با خودرو، دلار، طلا و…
🔹
همین حالا تماس بگیر
⬅️
خانم رونما 09126227033
وارد کانال ویلا شمال شو!
🤝
https://t.me/+np4AG_H23D4yZWM0</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/670028" target="_blank">📅 09:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670026">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
یک منطقه نظامی در خنداب هدف پرتابه‌های دشمن قرار گرفت
🔹
معاون سیاسی، امنیتی و اجتماعی استانداری مرکزی از هدف قرار گرفتن یک منطقه نظامی در شهرستان خنداب توسط پرتاب‌های دشمن در صبح امروز (یکشنبه) خبر داد.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/670026" target="_blank">📅 09:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54687295a.mp4?token=rHA52MWTVMnncsfXdBCGdO0iTk7sBH9UZ_ZZBwvWyoWlkYKeTLtVqXMKOqy_2yV-0dZ3deoYWovZA4DrQ4ahVuxledJH2cht7IchztQcHoxJOmO6Qe0RVX6Kv3Z8GIEDWxdic3j1NPVfqiWVVYwBOH1PywUEMVFVq1pjyaXNKQP5sQ8IIoVRE6vhatGLipC4PNP6zkKXARhG5tDXRfmsLRYAuFZuKOmPplZOsQ5skutj6PU3vNb6mWloBppg7lW1r-CMNgevwin3gND_gFOh5e-gn-uftsVUL4AFHhCSb-LfIQjRGGrzDk32_2MJ4i8S_On1lhCWEKrFqZ_vPZR6fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54687295a.mp4?token=rHA52MWTVMnncsfXdBCGdO0iTk7sBH9UZ_ZZBwvWyoWlkYKeTLtVqXMKOqy_2yV-0dZ3deoYWovZA4DrQ4ahVuxledJH2cht7IchztQcHoxJOmO6Qe0RVX6Kv3Z8GIEDWxdic3j1NPVfqiWVVYwBOH1PywUEMVFVq1pjyaXNKQP5sQ8IIoVRE6vhatGLipC4PNP6zkKXARhG5tDXRfmsLRYAuFZuKOmPplZOsQ5skutj6PU3vNb6mWloBppg7lW1r-CMNgevwin3gND_gFOh5e-gn-uftsVUL4AFHhCSb-LfIQjRGGrzDk32_2MJ4i8S_On1lhCWEKrFqZ_vPZR6fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه ناوگان پنجم در استان چهاردهم ایران (بحرین) در حال سوختن است‌‌
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/670023" target="_blank">📅 08:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670021">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZf4VVy6b56ynEsZsYw08oFDJICVPob7Z49D5_ldSTnWvVAmjY-sPGiYh6BG-TnzlwKbZj1_n6YClf0jFzcqiYY2O1XyUIHekW_Ioc7osnG8NLSsmi5ozBOoOKqAGu80AxX1qSAerWXdez0tvfiQklE1pjzPUOVoVy60Sk924sZEi0SUTS8owtqc6K8HCpDszYjOSGXPYCOdo5KqWqHZy9Xuy2DwG8NCBVOmLGz4Glcrt-P94IMhAssvY7UI0kjQawkAW0eMdpwX8xW8vI4-mBOl2k67kqQVd37YhusfImLETIALladFO_07PrM57LD4CWD8l4YSakWIVULjiZTYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیر سابق قطر درگذشت
🔹
دیوان قطری اعلام کرد که شیخ حمد بن خلیفه آل ثانی، امیر سابق، درگذشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/670021" target="_blank">📅 08:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670018">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ea758fdb.mp4?token=DPSTNd3Ne9dZtjwzBi6PBmeNnSKgZvIVYriMlfSINfkWPBzbmUMYpOVSHhB9XfwrG83zoWcZEoBRoFWPHjbvoQP3_DCmEyMsnxjb41SSqgYzw08Eu4s7OzOWxTmTzpWIJef3y1qrXqJCFYchuZRnhz3uLF5Iy4P3ZZkACNgSFwdc7_wbsRaApbo0BZQM3PCmsnXmn-PjBfYa3qtLYuHqy6R1zwy0Rds-PsG8oFl81SuVjgGZjBQxIgxE4tb7FvtG4exnWG0LuKWg7kbOJ4QD11KrVcDs1uVoBcZFrVEwkXqrQQ4MXdrkUzGcXdbjX2HaVV-GMPnW2PwU4JPbvFniiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ea758fdb.mp4?token=DPSTNd3Ne9dZtjwzBi6PBmeNnSKgZvIVYriMlfSINfkWPBzbmUMYpOVSHhB9XfwrG83zoWcZEoBRoFWPHjbvoQP3_DCmEyMsnxjb41SSqgYzw08Eu4s7OzOWxTmTzpWIJef3y1qrXqJCFYchuZRnhz3uLF5Iy4P3ZZkACNgSFwdc7_wbsRaApbo0BZQM3PCmsnXmn-PjBfYa3qtLYuHqy6R1zwy0Rds-PsG8oFl81SuVjgGZjBQxIgxE4tb7FvtG4exnWG0LuKWg7kbOJ4QD11KrVcDs1uVoBcZFrVEwkXqrQQ4MXdrkUzGcXdbjX2HaVV-GMPnW2PwU4JPbvFniiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدون وسیله شکم و بدن‌ات رو فرم بده
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/670018" target="_blank">📅 08:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670017">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069e8a600e.mp4?token=ET7w4YGdL_lnnA_orIri3SfIDB6Q4MwfZbb7iOIkmtz8ekNGFlhH_heUl4VnUZ56GT4QOBfNks9EFfAJtTkg0rCvpUBUN7FylWJRlaYj0OMWpnCAQrIXT0UMoDDOrbXWfvr7yCo5bXaJx4qnnBSR3MKV_1vBTj9jZifal9pFVUZ-IZiwfLZiDIxqAQHiY-XVZPNo_aAhwx-att7d3afQ2fOA4VLTU9ckO-rhrDMfwE6vKHuH16EdxRrcXJBMI1hMCpmvBGwkSZCN-VodoryqaadoaNY4yUPvzgOGlkHIUHrGMfL4ER4rVcv7huum0mM-75yVuYT_m_jYlb_OfJVApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069e8a600e.mp4?token=ET7w4YGdL_lnnA_orIri3SfIDB6Q4MwfZbb7iOIkmtz8ekNGFlhH_heUl4VnUZ56GT4QOBfNks9EFfAJtTkg0rCvpUBUN7FylWJRlaYj0OMWpnCAQrIXT0UMoDDOrbXWfvr7yCo5bXaJx4qnnBSR3MKV_1vBTj9jZifal9pFVUZ-IZiwfLZiDIxqAQHiY-XVZPNo_aAhwx-att7d3afQ2fOA4VLTU9ckO-rhrDMfwE6vKHuH16EdxRrcXJBMI1hMCpmvBGwkSZCN-VodoryqaadoaNY4yUPvzgOGlkHIUHrGMfL4ER4rVcv7huum0mM-75yVuYT_m_jYlb_OfJVApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم آرژانتین به سوئیس/ آرژانتین در مسیر تاریخ‌سازی، سوئیس را به خانه فرستاد و حریف انگلیس در نیمه‌نهایی شد
🇦🇷
3️⃣
🏆
1️⃣
🇨🇭
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/670017" target="_blank">📅 08:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ناوهای آمریکا از ترس موشکهای ایران عقب‌نشینی کردند؛ فرماندهان پنتاگون دستور فرار صادر کردند
فاکس نیوز:
🔹
فرمانده ارتش و هگست در حال دستور برای عقب نشینی ناوهای آمریکا هستند تا مورد حملات موشکی قرار نگیرند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/670014" target="_blank">📅 08:19 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
