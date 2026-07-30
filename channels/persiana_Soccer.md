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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 16:59:30</div>
<hr>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ld94ilESsDqG4MfwlMjKWkRyFdR4Io3mxHVnX0E482NuEqIu7rZWmB7WG9uouvBNywXCOkQraqMmW6Q28-DYwyyqh6-tQH142stsrsAdYriTo5qoDjmzy25Ajk58oXvHmLcqob4eGWxXO6rRjXfEGUWBQ4uvmv7meVCpeXgz3_t55hBWqG2ArPR9TYD3xBJlDV62SHBWVubDpNsxi0WVh5bAqbVpkl1ekYXdyW8Mz3gK-TgM4OiM3DszfZoFjnSyFb2WdGbUrfvDiOUWZcAd-FiF0vzL5VFfnfKyK9Famea5qmdGAEUnrIbW-ohiIUCwfRKO3cpaMaZRnp_uFnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJUwjSWx7IxA64IMU_-N05J-3WFsKAS1TCwtxnPTATNtkyxXTECbxiPu-xtTCwa58hreidLMS1FhabYYp78hbVOMRolUvZX_4u3YhIvk8WA_HXsQWvk4tSfPA_KCc-ER72h_nFWAYSxlJ_5zcDgz6jEsNCYTrCSlBdAHaJVo5sMSlO2xi11ba6fnp-kIolx1-vATR8hf_sqo8I6qFAW3C2RRJnXuYUzq5wt0LyQa_WxjG_7T9BlxcgAI2vP9tCDBV3Hjvp70KDOVkJ6fKrV1leP61ObPh_llwQRhd5b3CYxxgHZH-WRIS9CBVUbMGpXdMud-1ISV7G3sxuIiC6ZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBXiVSnDKqMYhlnCCM3WhmCWu1dT0EXB3p3Wbw-EK2jV2f_0-cKt0vEKZ4xfmiu9VPSVhUjq-SaS-yG6e7gBIpB7IJeabMmtSNQzCsXGJeo8S5-K26fkToVQskkqdmAonss9GaFiGTiYbCHhM_PP92UG0RzDtT1nuf4oJDrE7RG0EMs8MsPabMfG0M9ypGWA5212DGp0wg0tDQ7FrNeZYhDohVFvvqjbQFBLdWkOmjWPuKhQUV3RcGeqwv8Z7nP8skwhCrRpe-3t3h192WUnUKeDRm12MLRPFcmykAyjtafgEsJda4Hj46dBDS_55Yjnc0h_RjaFOjE_iKq1KtMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7LhOHECopCBunuZXulm-XmUww9iv-6qDXYY9_40uBMP4tH9BLaEguQ8dsIqrh2XcOvs7dZqxd0Qhkz2ENw8Xvp0IKw5qnHTYqC-kmgXmBeQ6yY6y_xL5OFwhLfsIRWxBYE8LalIY2Tg9rDsUZUfuHmR4pGlea0vylHOSwF5tipNRJ_KpNjZ_I8YfvDXOVP31dbtSRAJ3IoUb4NSKCrUdnn5mrN_zUTR6j89dMu06txU0lRQFfIK7A7zScMBEd3QFj6MWewK5J7HuzTOBk5xunGUkeRREzUL4NtfSB15haXJLC3ospK5f2f_SglcTSBg7G_g8lnkhofl68BUITjCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZi6PF7VZJWzMFzkZKh1qn9FsssHnQ2Bqxhs04kqfD6nFywy--emJ3MFsuRAW4DV_8ARMPuXnRZ4npC7-tSqQWWL9OINw6-28wPVUb7HOB3cFyAHAhZEkOV8xidQ8m9EjoYvugoFeMsOQh0Qhe9rbf432EhQR5fIywhNsQwSRG3mfA5j0Ef7VmN_m6DlwsGYPimajwzJWoDhJMDJReUf_-j8AlXJeK1PNd7sXKr00QxmKAFWAEujgJ9lxuRwgtkayB1rTH5etuDayOD2JLEuM5-BAgDvPhW9Qz2ye3hTeCtRcZ-CzXixNM1HqCetFfMyDEJgwNzl53hFCbTL5zVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UikECKDFSrKlAb3urrHBCyT5tFNVx29R-tDqJ2lr-vgT1e4rDf09UWIzG99YRKVPD--hF7NZ7_r7DVO0kaG_Do-RJ842LTY6jRiEMlsqnn_3p4AFREQg1Z4Q5WFt9uG23j_HUtmqz7jwvpM-gMbf7Obkr1GK6jCF9jAcCORAggfW1zYxIab4qhZD2cW18PKtxHNO4HakPrYJtfBvvRVZRnVQ9KJ0PyQNsfHcfY0zqPEyXXoKJcOYsh7Q3zmiIBTmAtLfayRicuH1-PpxFRFMqo3wGP2MyAijWrV8Mw8O4XT7SUsO7IZQLQ7eqiR6hgkOfB9NeyX6350BN3gdKWJsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqXzCkLIMtXGKhY1O97RiCxHAooruwT1CcydwUKIGR7c4kzrrBavHDWbMtLLTzR2tzxQdWMZ0fWuHxP0y0pGK4coEfeeeO3F1aCMUvC-FIPU0-urBOZvPgulxdWVdxrv-hOSWdXYXEz2C_FoqTYBNn8dz5HVZuPH24nYC_WfPaa3XurURkApQHkOmC2a4efCI2NvJISFrd8anb1Mnx9VWdxYixmCeSrpPcfgHeVCgqmBiohzf2NF5xFxBhZSshqxXWWGYpIUntpXAqnzl1kT-xpGkIHn4BOEuhtryABfgPR7BPMWm6hrUQO7HQLFKMO4Xm-WswM-y4ZU7LvCDYmXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKLAlL-ExMUGqoAsMb5D-v1kRt4HxjhzSKljxcWCJZXjRFCBhlm2gqXHzfRlpwPVv6GohTe9mIG33ONT4D0gtlkaNQSs3EIn3ltzS58iQLY3vLb5oul18wZ9f2Bkh0KJ6Yv0OmOVV2raLhkcBhMFWjKuBQLarQsfQbeFTstkAqXsvk_BFv3Q-Y-Unhvl6LgBD5ikwuyXgBlPTs9nV1g_6LiJFaoM9xiOWpy2FPDr2dZvhfktSZrpmHtfaQ4UQ1NkvHlcAADss3my_qyyDIbNPUmHAFRxs8lEm3-DQDIZfgJcNY-ejKCmQR3AqMD0POElobLEcDL2zEM5E9cnso4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4HoJ6m5_qruuKxpO3Lnp1nyXDdFHOqijscSsCV1Z3cIJ_cO8Wyy2AQs7WmN4CHgcdcuCmTJWOSE1kLEQ-mHse6bdEttgohjXYmEOQ7O36WRDcpraF-K7rA3BioLgd_7DeKZNdz5phiBR33Bfp7QMOGc2JUHhdQ9tDEveP5oiY9ZefyOSJXr5wKzYYf14f2z_qo3NDshZnBAbiyFGwb8sVdK-n9u2WQn551aQOIlmBflamwosMULxmbT_feZL6gI0LxEWHaG3fsVXL0809h9hlqv167D_eZI-J7lbcWkgjDXIrJwJJeaeJJVRRSDXZgAiPLDGNM5e1O_OA7Dg099Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wie6JgANgoom_Avx6vLpS7p1oZ3mO80-tZKsFuHPjHewAKJa-do4LufBgpbrbsA5sNkmONJiWSsUgXkoQpQfEH8G9ZyjZ1xgssGcHLKtp3mmIO7lfmVPDQWECpVCETddFxIiSaNokaZ3I5I0tc1PcCqyJ14MM0J1clnpcmbZjTIggne1rg5XmjugCNX0QchUVY6Ev2gaoZ6K0edn7y2K-g0QBX-dNfLX1ayOEq7ecrofYmwh_IcO62T5nOded7QoieaeBX6qrQh0XQcH-oLq5dQDXQFd37q3iG1jrBnJ8yidc3EVmZ6tDTkM_H5MwCXBmmdjgzwsHWs5RA7mJwYy5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GswMRoobA8GYonPTH4oHbCoe6yezwLNzbhfFqwXfX87e1xwTNJ9ZppJBVNez2v8kMCmuvOJ4hxfA8QLz7AeUS4HzY9baqZch7YGGHUuRtMlwojURWya-4ahPILku56Rqy-ch-Qza6jIZLE-xc9PvSxlNb6KlMBlynb2EiVXnkUEkj4lsNK7wwG7jeUCzijdfGuX7T0EwkyYa50dsCHstLSN7EyYRL70aUd4v4mIgOYihDxLr8bhpLwK9BhOeCv-OgJQaiGLTgOEbUa7ZgV8TY4VGAQYqVihgYYpxZIth1e-g1tM_a_360iqpjH1asF-S3MWIyQvFcuEI8BQ9btD0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJmTNGFdA9fpcR1jWhaSfqZnSfHboihMhmR6TcmxB01FPHTyIM7yD7Y85Fqx8e5yHYFaOSlGUWnBSrUy_OYA4adXdoBA0RIZGt3gIA1uXnfivcfW0ZEiuj6rO_D78p27JWtsNiAF0js-ELF8Kr8extCa8ITjwZcJ4Sd8W0XAB84UA2EqJFXxSKlYGH8toeoFJKCDGiNaeAVQmnSGMmlN87CcZz4aMKBsvH2rbdxtlN-XhZw3KAMSI7JHoyluBrV0jt5KJil9yZuzMhIitou46ApVk3nEvdTY_IdjZ6v3bSFj57q5kA7Arw06NNq6iUaWKCXWBBHqSFAx_UnSx2fPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOiSCF02LdkNe7XeUEA2OX8-fI_9HdyCUxMvf-adhWYKxDYDzOv4g0s396P_Dxp9k_CRDGIAbG_K_fIuLMx-ps3JxqU6wvEvpyHfFM2WoVOkYvYZ2qRfoU7WN9jz8EslTQHHxzE57sdn0INz9DwNEaa4EfMv2x7sAoD-UVsIJLeO1i8HDl4uE7XquBKi1JwJv0BrNXMLOnDF1zgtrb6rbtLuQnaMxO-Xf5x-WfBGqG5RCdnZgOGBriPBSpgZ_bAjBicY5g7e8roM71C4ymBaQPlNiDmEC-AVeuHF74x5K_tnyoaJR8ZVNAvqIZb5IXDU5vypKsZSQuyuCCOwYr_i0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOxe1LFexCbOHlVa46EMKe3whmsUYawgjtFT2tnZ0H5u_SsCUIIeyZ9DwdSgvwgLwq8ccuDkTwfpeY2igQyRYbTv2kH-zgQrQ-u6QdZEqUnPT0inNnZjBlgmirQACuZ72H2Xk47gOkABq6Ho-Eq1mmuGoNPIi_YCa-q4ZhCzil7fDmSzFx54TMFqLuAN3npiFgMkmGemJwczSKi7JW4dHAVOyt8eZzCsk4WhxhTDuXvuyy0W7l1XjkkliyKr3hkYXu2WINXuHCFeJO4Ax_7pJtH2RnlG6E4mImtbvXjIKdwAHisI9fgDGldCfToDMxtdDoLwcXuXsmuwSQvrrgVIgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbR00GFTRWAt3QXqCJhSjEOMiBNkyuRXHx8Z2Ay1ZnOxvWhgGyU5aZD-GaZRWbOBs0mPSVgcy0Tmo0L2yCRlGPIlmDbpsp6nMQW78gK0FiXMB1uOl7mJeXZk17jidD7YWS8Ipv7gEBt5JL5O0m6qWFZyxFR_h4-aYwfjU5kqj1PiXP83PMo-jDQL5USA02D3mppjKtaiwK138yO_oF-vphHPkO6G2FHuF4885zUGsKu_LEPm83Qghbz0nYi8KrXLtHkKKk-prhuKbLuxndDH9wft9m4ndydh-JhltHEEDdjvBmue-9WSF8CPrzwsjemRWAcR0feVPVPK6K1Cl-RcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi-4SOOeMmEtmquHY5lqGqFJlbqG1N1rotZbFboVSDgjt6Z5bf2gNPVqGp8RnU3hedYUElT3bmyRMwJi48ZY3rN4usDjUdYKJVW82se5slxSgOp8JcSsbBye8iTjMZuN2ES1rsuOiWmEFRqi1QmDG301W3sFhloiSe2vTbiBwhQgEzG-Dg0e7QiUfCUTo486xMSbDyJReodhhrjtcAmzHzQR0d4oqW2pC3dDTSMjfeGg-YC9UKkZxXuxdSNL_3iTv1OD6PEDf7vc095YYpF2XG-Gp-JJdMjpKX0a44XAyuDYpgkzFl-bmRduz6FR1P4fJCJR7waQXEF4zZbKjSBCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEYuUktl0rcezwmTOJfF0NLqzkxLfKLLd_hSwkb4PjxZTRB8i82cyjbr2svo5rqybgRHaNwJ37svPvTFZgBwPm3nm0EaZIz0Ct7Yi21Q44-yCcqGKqYp1bPi-3wXKyurxihNPNEwRfpXMnodYo_s2_6-yfUDtZh514MXlirbSx3JoA0pVjG-RiPiC-AxuqVgxNh-oSNsKo-mtEVZ22X-tqXd8vzbI9duW-sKltZ8O22K6_b4_2tdRfxSUpngxXznqbGvdTfUS_NdxKMb9x4dFSIqEhjqOD3ATU2qmwS8Sduy3GxeCCYnVc8EJtVtxVHuKwVD3S0wUbeNDiVT19DN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWzOFoFdeadkCYEQBbuiMg2C-4Y2fAMF8BP7SQhpyZ7N7tubH4A3kZ9TqHEer3Yi-evVfK8-6drIARVWAzsCHAtUJSbJK-d3iSqOPSNDhgFGV4-4k9m01bRfqtOZxmWwlxIvP7pbGgXoNM974OnSw-0rXx9bdmIamEI5n63gWc7Dax7YMMau7XH-kZiXE1CqixXbssB_J8OXuZVf9ZLgq_JvRZUxW5BGjfmogLA3xBouuoU9fUoTgHPHXoDlOY-6f26ZnUa1a_DRzAbBWcsV8mnwl0O8nbGBzaWKSXpyiqiENUfhR2VmzZtmPcu6q4F3w-kPoENWU4Wk6w01d9ch5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=vCP-ieBm5Wn_O2UY14pa1caoKVLf1b0aRFsti-uHpbXyCzZAcE9ZdeHGqXoWiOey7hZ7GamzOYafkscnAG7whwQDkI_ulRkhAi4a7NROighibaffTKmq5YM6Gjpm_bpSoXzF2ZzLi7s_ANZWN5dMIPMvA-X_5mVV8_uWayoiwsIpD6jFyRWDrGIwOcIL0TZPzlgoIdyJUst01u-F9fGXkdLe_iDUJCdls6P9OzMIG3s5FbdAjvvfNAWHXvAmBZey1KX8uFvEIX6jjeK6JHfpEZLAhogLfmLmk0m7wm5tp_V5C1i-7Rkj2cme6V3iTOeKMokHVFtFJxzD2RhlGOjDXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=vCP-ieBm5Wn_O2UY14pa1caoKVLf1b0aRFsti-uHpbXyCzZAcE9ZdeHGqXoWiOey7hZ7GamzOYafkscnAG7whwQDkI_ulRkhAi4a7NROighibaffTKmq5YM6Gjpm_bpSoXzF2ZzLi7s_ANZWN5dMIPMvA-X_5mVV8_uWayoiwsIpD6jFyRWDrGIwOcIL0TZPzlgoIdyJUst01u-F9fGXkdLe_iDUJCdls6P9OzMIG3s5FbdAjvvfNAWHXvAmBZey1KX8uFvEIX6jjeK6JHfpEZLAhogLfmLmk0m7wm5tp_V5C1i-7Rkj2cme6V3iTOeKMokHVFtFJxzD2RhlGOjDXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vi4XN0x1Xi6DjFve86TYNWlJ_5YkwfzoxGtqQBVPXr1MmC70wxw_FOzMBL3IPuZvVPt9AkLYG-dcTbS8s-OnEyAWCAEy4Gn7DOC7-pIlfVR0_ij8Zkx0ZLrxfYt0I9iss45Yya_Dj4x5lvoLa3Wq0ZERhnonSdluxEr4pwFXCWQ_xWjP-vzrOZBXlADasVnFv0rGtS6EU-8Yq_1e7rg31e6ISzQww9-FZPHLYCJm82XncqHu5g9sUtAMI3rprs4vP07WKz-NvYWwKKudhXZnGFZ7N7Xr3U7BcOkBrWMrb2SC_fhKf-Ol08gYSf9miN5y3lL_byJygUUegEFvj0rvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjLu_Dk9zNzDFIk6sfgv5DMPPnXDy2nCwXQ8Bf8deH0LOQuVtxWEO-0MnMbbv1rhBWnVRLentVcfZnod-NRPFciD1_hGhJH5VOmw3W7oVt8ZcnRF1RZmfAWe5W_pDEI19YvCMg0ghwgTNx1btS0FYoqHtAnSxkVmNuSEzdddwNLX8feTqB9w5grmw6Atlw21T2qUUQaA2fmF7_d-7zIu97n3U2a78mdSFOotLmSU-lN1ilWUE71gOR0M1EXzjgq3ZJ3aqSp5f4iXfl4KmsBTIUheOKj4W5G-8KLuR84MptBMt5CtAC7HsvCGR8jEJIhBJUNm1TWmW3_sGQUXWbIXDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbbD0jQ7SRnTXClht8MXBNSNLRcGOwgVI7iggCJuTkH7JHhqN6JNRjOsrN6nG9AA_YjryeyuwwKlPfIPZS4QLOzksSyzT3kpQKYZODzmumgkE75xd35ZLlPpjmHNG4k-Yl-VggrY-gnERFS8nHRIehUzWOv-LCQT2l5z03Kzpz10yMsd0_gYDGFlFsSHpphN6PHjbpqMuhGxXUBiHnBgpo7IAL2eGTMpjGFHZG5hKyZbq3c3CQumVqG9WXC1VQX6Tw_87a-3U_vzumPjAUicLhY7WPJYotW3cpG5vKWTZFGs-6gbSg9ApKkOkX2el-SPjWp_Adbcfb4LU0UBAveWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzuqaTmM_RWXItmubiGwg-7NE4Lfy3j2tmV9TxQOAUbGK_-crqx8T3snNBEkCFGPFYbhc6zMVz8r58A1kQWlq2WRrISP9uLF-bx1w-gqcmIJWOVcVb7M4rlyyyRcCdBYlrJFQB9ENmPvpbJJXM5oHkEm14MAX0A9tTN9DLBOB_gl_pGmnb75U8Shdg_KfZkiO6tMVev6aKD3-fcyQ_eUO8HF1Yuo6GwH3Ow61lfJgFC6FVllZ2TCdJyIO9B9XkCa36KRa3Xk1-T3O2S1uNSjW9gAu8SOTdvcAGNqYP01M2qq35J6Sxo9awXLNvI6UMDgVQ0AvhIypAPkX_2k_FzuPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=uGm32J2TbHm7Qyx6U-FiL-UdrQmurKVSZTsaWeJPDvqlQKrAPPjvRkrkDJN4gZpjuoePVBZxw0dD5MgIKnsi0rRnOgxt0rkrdKmhLQBfXfcevNj6uKDmNqC-jZfI6IbZlmML1NHtWW-y1N_BPy8yu5aDcHNBch4SF4cz_e9KdpwtUsr8K4aP3zSOS8daHri_srmf9F3gQvrnpMpuuUJ9g1PgJCmQ00CS9RPkBA1bi7eCT3_hvlJPADWb7U3GagSJlancTnkdMgfqb1wNsdBfh6VSsE0kedEGTZJjdNOlmPXf1cyIvWThwf3oMKBfz2DRMRpBfBLgHfPCMK_NAEstrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=uGm32J2TbHm7Qyx6U-FiL-UdrQmurKVSZTsaWeJPDvqlQKrAPPjvRkrkDJN4gZpjuoePVBZxw0dD5MgIKnsi0rRnOgxt0rkrdKmhLQBfXfcevNj6uKDmNqC-jZfI6IbZlmML1NHtWW-y1N_BPy8yu5aDcHNBch4SF4cz_e9KdpwtUsr8K4aP3zSOS8daHri_srmf9F3gQvrnpMpuuUJ9g1PgJCmQ00CS9RPkBA1bi7eCT3_hvlJPADWb7U3GagSJlancTnkdMgfqb1wNsdBfh6VSsE0kedEGTZJjdNOlmPXf1cyIvWThwf3oMKBfz2DRMRpBfBLgHfPCMK_NAEstrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA4dII8JPLK7MJeBZyaRyq6gXtRkNvbYcvbGmIjX68eL_q5UlxR-uGQesBpOac6qN6VKe-1SSusJ2xctmZjGPCORsoc3qUT3rTqkwb_Tx0O-IVisNfwh1UWZ_DsQvWo1XDW_WYdGIVYNtJv9P73O3o7QGsiQ3gHusv1uPR_85llgENe3aoQRboHAkIwYNz2lvlvRrB0JuqsubPcgSDyIv5_p1bhOrNc5oDcHT5E6jZ0u2K-juOP6UzeVAkNmn2Yo2s8hZV7tgtywevmJtmNB6AUkI-fFQ0nuzK0VMstWXhIpCCfgOxx5WTE3t39n8fsaNulcXOPy0ohjdcH4xJ9yNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH67peGPQWY3M-ccNW_QHI2rlYFuo5bRnRoCHuR0-8CmGriTOCh027uAxnsFjuzXV9ICZL-YecUgzbHKmub55Nhu-R-0rpxpJNgYMwsetyDfLDRppAqYYgyluNC3zXNBKW353KJ4xd1cXo9ZtVHioYBsAjYQqq5Vq-Xb1vDPXigbMJG0-IohmWfo3BhEUzfnqWLQi6iT-RGnTx6bErVZVbtP_IIvnFCVoHd_PROcOYoiJ8d9mmGYJq3hO-qw3NROLj9eDq2rzXf9Emzciez4AGf_yHgESRlittjon4ZowkZN3XvEdAWRVulHZDUGR0Rl1k-y8QRG74WStR040IGtoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=mPT8SF_6GUUnBJKeJMqjO6PRyxKidz8KInDOlOn2NOGb3BlzLaQv7uFoS80G7nqexh4OpzrVg46ttOzvMp5k38-IyVOWsDkW5911SysE2WaqCPQScWi12ZLPm5TQOmHS8R2JpRJ0yReRkpNPUka15HuEO7452AQmRqj_AGYmJmvGCIXLG2CaXMHn8X7F-hxS59qXr2NHOqp2q9JE1GqiyFRZiwt08lZo7BGofIMV6Ug7RqKNxQmpZPHq2eHg7a49HCsEDqmkmnaW-tYPJ7YCam3VVhfYOATWjTU65XncJVdaMvGe10UyKXlxROv7gsQE4UL2TXQmemlngSxvPRqHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=mPT8SF_6GUUnBJKeJMqjO6PRyxKidz8KInDOlOn2NOGb3BlzLaQv7uFoS80G7nqexh4OpzrVg46ttOzvMp5k38-IyVOWsDkW5911SysE2WaqCPQScWi12ZLPm5TQOmHS8R2JpRJ0yReRkpNPUka15HuEO7452AQmRqj_AGYmJmvGCIXLG2CaXMHn8X7F-hxS59qXr2NHOqp2q9JE1GqiyFRZiwt08lZo7BGofIMV6Ug7RqKNxQmpZPHq2eHg7a49HCsEDqmkmnaW-tYPJ7YCam3VVhfYOATWjTU65XncJVdaMvGe10UyKXlxROv7gsQE4UL2TXQmemlngSxvPRqHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTwQTeDZFEgzR93qNWtLK1CrRHx9cpQNVasD8ep_IEqI9QTWC2LhvgZpFi1f9kZW7o_uVEe1rgfAI-KGNCycZCVBrV-9gRSoKej5bxP-LLVPXW7cyPYfN2_J7RxL2gv6rPn5KbBFe7HV_l6FTiRh7l0-Q8ZIJNKB-1Vz4d7wCSS4v_8aZ5GBcveE0QG6fv3l9lkN_lBKCSx2gPIPP0wDrK4-Do6kUYvI2kHfEyfijHeXyg0y8NHXALYQTEIUNZuAasIBSwXMkvGLlwurDk0Fo0dPahKGbmn7wgSZJBlxmmZotEspp1ufcxx-uoH8TSEkqCfQzLoaIVtZizBta1VhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTGiRBQnZ_PO0DmR2Gb6IBvMpOHsSdBcISDkqmx2PH-rAbEUmXoaTGdKz2CEQEabUswB22z1I55wGhD4NQoUqJ3pGsYUWt6rrCw3OGheGZ5mwTgx6v3pX_oe_5lexGjMZZVg7quplcgHRBWSGwz7ZB92MAkVYUf5WJngB523rskvtuIninN7u6vk8kcxiKyhkHmjVMwqzRqbQMHMAtU-aWFZIfMb5tGSLiVMS_-CgY2CTzP7ky1o5RbqLPoQa8bOkkfShh9WIxWm1mrL06CQdO79kWtnEHXs8yZ1NdCJvpts5KpiLEFmbQSAvM9KxM4DMXJNyrisdVYfogXc6AjCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_k3OuDXwYvttaWg1IfVEnUcBLR_L_GVZsu9uEd4tPQ7x2VqMukyFvQVLhvxIXGVWC71fZ_BB8LV-xXztY7y4VA3t3alqp2hbE6GPESy_9wrjil0ohLbC86sMEVHaJBdsgnZDIelREppJFmQE7K-5XlgXuf4sBLBrTw3hbGqEXNAmCVbA8FgBgbw43NVc3gLoV7eoBE8CBiaQWYlNudUWhkieq6EGjyEgV0uwvB36xD0v_B4iNtBRz_w9_XRQLgRAxW1SFCdC3m_vwYXtwNtB61iaP5Rionit6iReLBJYHn7gOhsZbCl1RRoo7_OOccTF7MdcBcP5ZGd3I_Zk7MJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSVP9H84YTvJV7AhI3oidIjD7bWWQVZxGDz1XQByVU66u8iXAHgG70yKr7h4JXHkXd1HHMmiLZrTsVpjENOVfEobV1lGFRcf0-22bLN9sDI78akhvpz2fuLT6ZooRnHpp_S8RNYpX1NC4fQLWWfEf9dNXHgnrmsTsaufqdA8_yh_A0Xmpc5RO0xjI7S33WN0gc-D1TsOjFEwuO_YX0kUbikj7AmB4naQDB5u_mRcEQ_ZSX4Kj-QLswyMHwlHThgRpGi9kRURgeLTL59EwYcWhovu5n1aG-Nvu5-SuZ31Rrl92tpgaR_nlBVaZENdwk1PP2GKfPbUGbXVqdVdgzv3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rer4RD2Rh-Bwwc2vExdpvndxYAhuV2TJeXcz7Z9rNMnIBURgI-dVmGvTD7Gr-DshQB6D2PqwZC5EVGvy5yAXu8G0RiYElWP7J6HBFWEQH_rg-FMQMN5KZNbxl3ce4SAu_U6dzAAEndjtaIX6uFC0VNe1WkjO7JkbBHcXetGf3BIgF5HTjrbdaQDRBZp1hblzdXXUbuGnCNCn4Qpd9xtYNW1BDx1ALqzYnj1vo2HAoI2umARBs-aPXKjlCTbskYcp9y7Vi-k4qG8IkNBip6mTf_DSeeR4aXRjn-de2vbn-uh5ltf0CdqOugwfbqvMCSC1ULdl5vgklJ_MxnzeJ64a4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=LZ3LTWJITOxbrvlRAsnAPWCmphl7yDTMa4uqY_sCO_9XkvRxYrvIEOBfFMU7hQ3siMcVYYiF70cQFlzC2-MqoBlqRa9ZrM4k9W2VOY1x1tmdCSwstjinN48fXPn-ANxP3gEe-6l_cNEKg8SIJUHIeWK9rv09MWrZtPIKQsRDS_7Lpr0hFt8Nob47WhcoFHhINkZTTinpbicJ7DYcAhPrtoACPxHw8dHNpvJ4F-V52QkdXyfmW428Wn4TPs7QXceGxIB-VjJooR_N82Vipa7Emy9xWGMOBWfHMdjk350v81VvX-VMq4SLxojZI4OpS-viKntdU-I6cxI7eH-XkXpXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=LZ3LTWJITOxbrvlRAsnAPWCmphl7yDTMa4uqY_sCO_9XkvRxYrvIEOBfFMU7hQ3siMcVYYiF70cQFlzC2-MqoBlqRa9ZrM4k9W2VOY1x1tmdCSwstjinN48fXPn-ANxP3gEe-6l_cNEKg8SIJUHIeWK9rv09MWrZtPIKQsRDS_7Lpr0hFt8Nob47WhcoFHhINkZTTinpbicJ7DYcAhPrtoACPxHw8dHNpvJ4F-V52QkdXyfmW428Wn4TPs7QXceGxIB-VjJooR_N82Vipa7Emy9xWGMOBWfHMdjk350v81VvX-VMq4SLxojZI4OpS-viKntdU-I6cxI7eH-XkXpXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5TYX7INnK6OEUn7e5mzlQMOPi-r7ro-7dYX3DI8uFXzehsWxqTVRmTLpcjc38uBERTjNupWzHxrYQq31QaGEwgpGfxvxoCIl9IjcVTWg93oSsROG7vDCXWtEGtRyqR9ZMx7HEHwpMvwlWLfjPfZgiLdKpiBPpRBCr6IT8CExnXjgqCfGsJJCKWxKCR6ByQvwCg4Y93iJiLtnBAvl2IGh3Dg29fTPYsbFg9fh5hPkmXbvLuGPSKfA4KrKa0ujdaiOlG13rr_rE4Ge2cUo86HQ6lthYsPUhesmnF6l-_b8ADOxMlaKdROWENHDClCyDPjZPbWyU8uxw-YKBl2crkk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej2nLQ2wPZMZsGUjuOMPR7x-eHz8lePxa50itQFhVhyzdLb0_QPP-J-bJEK6Zk5lou-oL8ewDvuW_IvfbxethAVs0qhRhQYesR2s6jeGVUpJ6Kz6gdhzy8DyDw3bHMP6oIvzCg2TQdmJ8Cjbyp_HB0hbrs4p4FargcFrZztufR7JxpZ81rWyfBOZCbf5E8EDxRP47xlz3coFlcwjPxf2XLrXWqeQuVf6LiBNgMnEZXAGUfuxquSXk8fpIpfU4Yx5_Box8d0AzPiUsf84lY2NP3uRKJcJOLuJE3YCGXl8e__52jQ1dUE0HKrGSTsrv4nrLe8Wd5wyGGLglHJr-GWUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=GfWtZD-Ebf5v1RKAQnaNJweatVV6vf_YWwhDZEXSfWnnmwILDlbF31R2LuP9kdrY5PSZ_dKEVFnJ57Z86U2LanBVLF8wRZv1xeZ6zq_K94STLtXCmmzVYiokHk-dxD9w4VSNDwCUQ7V7GHW2bHM9r8czFMWCvoHN7oNadDW0AKHI7uZaTZcrvv4lISDkFOC_czeRu7C8leYpFpL8NUC6s-SGOrV24XqnmS-BWY7dxcAjt7S5ANHicUgGfOmuXXY1f2mFybLKYO43SCRO7CYJeMsxZ7CTC9rZ6-u2COSvk-zwAOkmzXV1oxqF9EhN24ecsgpmLaySS6ehvy2JkcJ-Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=GfWtZD-Ebf5v1RKAQnaNJweatVV6vf_YWwhDZEXSfWnnmwILDlbF31R2LuP9kdrY5PSZ_dKEVFnJ57Z86U2LanBVLF8wRZv1xeZ6zq_K94STLtXCmmzVYiokHk-dxD9w4VSNDwCUQ7V7GHW2bHM9r8czFMWCvoHN7oNadDW0AKHI7uZaTZcrvv4lISDkFOC_czeRu7C8leYpFpL8NUC6s-SGOrV24XqnmS-BWY7dxcAjt7S5ANHicUgGfOmuXXY1f2mFybLKYO43SCRO7CYJeMsxZ7CTC9rZ6-u2COSvk-zwAOkmzXV1oxqF9EhN24ecsgpmLaySS6ehvy2JkcJ-Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Dz6-mcuuuh9Mp6TgGsfBtAiO2JAbMOavBz4FfGnjaYr4c4AGE84E9UcW-99qasREKgVsMWUtYP_CC-46MarXgog3mimLWt9hL7KgRpk2xzvawzunJBlXXnLbxqNfgJ4IEScsXKowE6zFXKEQVxhiNN4EsT6W0oJoUSupnbDPEWk_EVNFWXbOyWgugMKFpnQneez4PMU1KEEpd3JQqLufzyHscOgELEWCvS17eqmzDOVFNrVss62z8MhFBCPM-fdzbTCYy20peBuMEAGmop1oodhWLgDrY15f7PXju1eUMcRauVFMveC1WwrK7Zjg2-KQ7U8XohLQqzr_zAIaPG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3zFKZwwqNNlTGBe8Z6TNK86xCyeMhj6OWcVJWKXWuhWBGybM-OF_45CPizlXq9OA-L7vadFTvb91JDq7ogFX7ZOcaM8Ze5ngmpWqOZtBrmgUK3B-MTf2qAUZ5lDmEQ9PTGJDx8Bfnox1_UzmeKUVADmMR6_Wv-GBgnzNrCkAPcodyjBkC2jXKpuj03HeJhHky4uGljRgycavcHOVpU6QgnFbnlhDGKdgumVESC1Adu4tY9CRwoyjUpQ7wSJSR7EYAurroR7mvwctHpwrev4t7k7Gj588r4O75PPHOz9AviiorXED01TnGlr7kABh9cKhPyDXwKWUbjJqqS7PkQlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2Rfj_wM2cTHHJ2QmkNRune6v22-OxvKXgBI2LiQaDcXa5_EtFRjQa7yUX-39uNjDjlZ4dyWaKNlpaC7xV_C3wKkeFWs4--O2xOVy1cza9jZSYSbKXJTCElJklOXDE4mrCPCGF9XI9gw0JFVvXI7SVUnzFwECfJOAwYEP8lnCKwBxNZXEvuq_52PiSFZBN4-qImavYhPrD_kfRxEmJQEVoFisU01ELCk-AUAk1AkV6KjnaZBicPwr6hGe_-_vDCdpF4izUcTj0wQUgMI5rESDOwi040RcCS59swan7OIMLp89HVLVNXSUWRhNoz05YzQ6H-W0r8xqs63WZpuNScB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kP8kATp_rW3vsRJkfXD31TQvilua5BB1Xqn5tUcGm7Hb0LL3LiqFn9irX36PCqGPWBuBS7NxSsWw2C7_jP9UiFD9ajpi-nTGqrmLCFL_8lCqyB4ON42s9MchiP0w1deWlF9DnU2K9YoPwy0I8AnCDA2sGF3o3K_z7eCANL53fuxZGFAz5cIwzNVba_V8hJ0kUKsEHJTRFsHqczhXhyrXKfHBmzkNb89NnghcNA9mOZJfIIoB3yuXEAZw9_KazxUvOvxwekCZ5qpzFmHMAdHzChedKDeZcyODPtYIAOgunM1ESe_FJxOMVzypZQ_l_NOftDELdnVG5LIcFkAKvt49IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bovGi6MMs8D3Jr7zsGrC44UGREm_Ux0l3fFrmdcFTVnmDKCZjNid8XzKOsTIqgs_Rk3vkyGOU4YQy0LAdhjev0Ep0BaqDS7mvUtf16Bjun1gTNnTkMrI15BPiysR61pmMH-pQGTwww7pvQ4bAQytpoz-jnjS9flkt3Zfkccb7YjfdJIctZcztl1kU9MqQ7bijnuWPCuueX_6aTsuGqkH1qdJA2lTbiBYdel0aJt2D3djgLPHGT8eW9RSoXQS6oTxq1UVQHFYl_b5oYWjDsCW0vGJPQQjp2BM-4dJo5cKtxuPP9lFnxoRMSzI_xMU_vrVVG8htrohuv2gKqYab_q2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ScE5L0YCCz5K2nL8uhh3GNtXVGI64k6BUvJmUS5uxvYiNas5tr-FsUt2hHsuqRqVPInzdRMMIeW1i6W_DPcHnnB48TIivBYx-kjXqLp1ej5ojsqc0bvZm3jhrHcneHvJnzrRKzyl-AtyvQSg0ulBhVOrLjceub7BjNchhNtdzmIWDaQ5QfE3wWSag3MnF7ysX9MsLtblA3AQZ8mDumgbqzNPCILXUJcikJ6wDX7crlswmbN6cr20_NSP9f3u41l9LGnpxW7qPImTLFjEboQIiujZVebE7VNlQKB3OiLIH2ycXQ3nWE5zXPBURJC6P17IWcN-jNK6M9_ZiqI_J_XU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ScE5L0YCCz5K2nL8uhh3GNtXVGI64k6BUvJmUS5uxvYiNas5tr-FsUt2hHsuqRqVPInzdRMMIeW1i6W_DPcHnnB48TIivBYx-kjXqLp1ej5ojsqc0bvZm3jhrHcneHvJnzrRKzyl-AtyvQSg0ulBhVOrLjceub7BjNchhNtdzmIWDaQ5QfE3wWSag3MnF7ysX9MsLtblA3AQZ8mDumgbqzNPCILXUJcikJ6wDX7crlswmbN6cr20_NSP9f3u41l9LGnpxW7qPImTLFjEboQIiujZVebE7VNlQKB3OiLIH2ycXQ3nWE5zXPBURJC6P17IWcN-jNK6M9_ZiqI_J_XU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o963M50SqE1eBS9ZrCpO0WyCjEhUqWT5uEkkQPZylTfGw1CZQ9En9reHGrDsuT7jUqAVCEIFWWEODFEQP_DEA--mXkBMfOCOKUwWBrMSpaXJmer6u97_nrKZnkwdUk_q_ywyhbKN_7G2vg3_MfIaoDgJF0eg1rvjUK3xWmi8Cw-Rkv95-1tZRUGYbbaba9_5JbYl9AnzpEFitOVU2SspM1x0-1tGB_K_7B5lTINXZM9APJwXtt7755J32b_bTYPNd1a1h_sDtuDRRzMKtuXceAMd8n_0avMJf4-pCwIBksYR5m_yzes3d2yYh0uHhubTehDa89g1P-WHWoIR5CQqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCfCw9pSVz08RIJhadeevTsBzKGBoRF0jbLFZFCaFF0vlQrIH1juErHfXApwTqmYj2JqXX28bL2_FRZ3WpxLFwV_4nhQ-4TjdAoHI2icLdpTjvmCsE5noedMirlG5_4V_i60QYtBocjBcPFxuSsFIgUzKksCz4aYawtk8ykwLvqXADD6UBeKau4E4LWNlIrbEtQGL6XbG-JxXgfwOOvxU1iiHU5vl0d5YXf8s8yqoJQFHus2qG9P8vGSkuFlRWP026nwmY1Mwg6_gwlPxFH0B1WQcYIGILqb1BwpZKF_pamaXfR6WfFJpqzdY9juCEQSkbwS_9bDUpItj1yvPHbIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=bLMkpS0BOEiKbQg1zX4QJddoAV6XiGQolDq9QTzWge47_SWEFHIl3APIxubdthfwP95As3y93wF2WVAS9OadA2tJWAN4EVgD4oDlq1QPTNe7RGE_Z2W5vQc_lGAhTy_C8JphzsXDiKNwGPlT6GwRpHqCFkmWVzyqUcCs6811ly03bkKaEsdC68FC52iozLvC9iPMC5ZeXIRKFhdXM5JuW4LJEIi_uBO3Fp_J4FcsHmTluREq4kpeHYytEJOH6xs6iX5x7i5XMdvPoqJF7jojj5rbnZgpfC4nEmEiZRCmDveyL4Lz2j6FhjkngGu5IB_koOdmH_aaMJtg-xKnDaw_UItwB55yvli7GpBaQfd5EzHG7DAMufpucjLbfAjBYBAzPbf5yrCDPRteNNrW3PwFjqBSmGsCVXRCi4BP1J6uWuf9hkiYyJuec9h6uwgp-pgQ9Ujg3xRDqE_mOS9uW_130i5iLh87uRf_Gc441mGA9wyS7ownDxh28UyxQAVqQWymiV7Y56LH7tLVgrY-2wH99ZOzdyN5UIMcPPKxENkRg07oUdiTCREVxTlQHh05ljVaKaXu5RcabYcCjhbxFX0E5yUTV7RXv3Td54jwEacoJvjtn8w7MD3VcgwFCg78msgzmJ-VeRbaNH5zELgPxfXfH_zb-jF8SGM04lbIgjpdEZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=bLMkpS0BOEiKbQg1zX4QJddoAV6XiGQolDq9QTzWge47_SWEFHIl3APIxubdthfwP95As3y93wF2WVAS9OadA2tJWAN4EVgD4oDlq1QPTNe7RGE_Z2W5vQc_lGAhTy_C8JphzsXDiKNwGPlT6GwRpHqCFkmWVzyqUcCs6811ly03bkKaEsdC68FC52iozLvC9iPMC5ZeXIRKFhdXM5JuW4LJEIi_uBO3Fp_J4FcsHmTluREq4kpeHYytEJOH6xs6iX5x7i5XMdvPoqJF7jojj5rbnZgpfC4nEmEiZRCmDveyL4Lz2j6FhjkngGu5IB_koOdmH_aaMJtg-xKnDaw_UItwB55yvli7GpBaQfd5EzHG7DAMufpucjLbfAjBYBAzPbf5yrCDPRteNNrW3PwFjqBSmGsCVXRCi4BP1J6uWuf9hkiYyJuec9h6uwgp-pgQ9Ujg3xRDqE_mOS9uW_130i5iLh87uRf_Gc441mGA9wyS7ownDxh28UyxQAVqQWymiV7Y56LH7tLVgrY-2wH99ZOzdyN5UIMcPPKxENkRg07oUdiTCREVxTlQHh05ljVaKaXu5RcabYcCjhbxFX0E5yUTV7RXv3Td54jwEacoJvjtn8w7MD3VcgwFCg78msgzmJ-VeRbaNH5zELgPxfXfH_zb-jF8SGM04lbIgjpdEZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwkEu4ofRPHO_OXjxGa7kf2VZhMLcsnI01AcJjNsAnidCt5ukGoThod7poLzu2pGwwyJSft4YQw69uC9UMNzuDDVbyTb7-r0ckU9sGm6f3npXhZR_CcqjW0cjCTcjTzn6lt8JoYzhUE_TROSWemF9BtBDWaCvI3PtBG-OcszXRueTnyyKYkcrK_j85FZhmv8fTjyXxqVgMRNVQgSI4Pov5NPDd5ZoutRPbt8j9PzQS6EyKLoHBrhV__tcpLF7pCGP7_U0KJXYISW6uZJHXCNne5KM3QlJ7ZDpzh1c9b-qLMWoE9PR5EkfthTxKISVy0vctxMEm0hUCet_3MKvNpSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNxzbIGnysVB54vyqp2uJKjRrI7yTQkkP5nJ_1IhyvqIhKb2UpV_fC2B6gq2GjBd52k6k7sE_cVMsHHsIlYi0pSCJ0_LsCq5lhvQF2g3-bVVo6U3X4kcqmEeGJpa1EFsGbDuxbwKEpatpnc5A4Vem-wUnD8DGHKbGgvdTrH_box-S2mUGwZnLNbhy97TO4kvyVgyXYfkFyLKWKHurkitGU8XV7zEAVF_RYmpnKJ32YGHVR2XyYAdWUj3HUNE0YTvnxbZLH-oJmkYjtHpay5EceAbtE65YR3dMI7G-oMaxqhhteLjlqdYQ-p4w__9ka_YbJ_XXrurojq9mBhax08KtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=ijsV2piDrl_k7369URyqIyJFsr4C9pMpiCPr4sco_pXR1AOMjNgGKcAG7t2-RhHw-JMKXMbPlc9VYi1qxwWSGE_4T9BYnAYlvx0BqTJC6jvbhUP8WpxlSKNK6YYVUfS6Gi8c-sn7PwSO-5yLgGKDjeOpDL5-uN50HToZFZPYQ-71gJFhrXPsS1_y1EDZe6Kvvds83gI4bRWyESIyKrbHd3RRRi5P8S2TajnXZhmVQ1-XOlUeDI5B8LN1A_sZC-sIyWJ3ZLq7WBfltidAe7fXRok4e9taJgaOWqLJq_80CfXP9ADAAWA4fzsjbpXMLfTMPa7YBJ6CDf0riFvzd84M-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=ijsV2piDrl_k7369URyqIyJFsr4C9pMpiCPr4sco_pXR1AOMjNgGKcAG7t2-RhHw-JMKXMbPlc9VYi1qxwWSGE_4T9BYnAYlvx0BqTJC6jvbhUP8WpxlSKNK6YYVUfS6Gi8c-sn7PwSO-5yLgGKDjeOpDL5-uN50HToZFZPYQ-71gJFhrXPsS1_y1EDZe6Kvvds83gI4bRWyESIyKrbHd3RRRi5P8S2TajnXZhmVQ1-XOlUeDI5B8LN1A_sZC-sIyWJ3ZLq7WBfltidAe7fXRok4e9taJgaOWqLJq_80CfXP9ADAAWA4fzsjbpXMLfTMPa7YBJ6CDf0riFvzd84M-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=vT2YqMsbee9oawNQAG_6aPbIn2mf7C961YQSKMrb_zImKMXd1DHusKAqCWurHBWsxlk_KjXqIMiFpvhw9otFN8hZfrWMoTBN96bZiUxK80NI0w3gPEgNwFoJfQQ6NIDWf_ti5drE_JteZSN4NGja3bq08Rl4cGR9RIbSS2AK03br_Lz2aWvyaC-oVELiBdGzh101lA8ylV5olRBaczvn2ha6EFeX3xVZLAlMcbPEWL2hBW60vzI-nHOSORDyzEO6MyJzJiLWdQygwNIwqZBqSsoZyHNQhhnqQUE2O_3u5CWHQSVqboo5Lk9jBCLcf_PxYEsXfGnIlBFKVlLuzWAshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=vT2YqMsbee9oawNQAG_6aPbIn2mf7C961YQSKMrb_zImKMXd1DHusKAqCWurHBWsxlk_KjXqIMiFpvhw9otFN8hZfrWMoTBN96bZiUxK80NI0w3gPEgNwFoJfQQ6NIDWf_ti5drE_JteZSN4NGja3bq08Rl4cGR9RIbSS2AK03br_Lz2aWvyaC-oVELiBdGzh101lA8ylV5olRBaczvn2ha6EFeX3xVZLAlMcbPEWL2hBW60vzI-nHOSORDyzEO6MyJzJiLWdQygwNIwqZBqSsoZyHNQhhnqQUE2O_3u5CWHQSVqboo5Lk9jBCLcf_PxYEsXfGnIlBFKVlLuzWAshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7aNV7mAtejKpsLlF3L3jB5Un9k0w6zT4oQeasSIVGCcoRnSt506IQxWBg_KKMSqQKv9o2jkFVsmgigKpbtXAFrdc8Cg7Tlgol7sAx6D-q40y_G_Qwo9gmxIioMBYlf-8RmyGtTwZIB2VUebiUqTMa9Pq0BnQDOql0nhqnzDXxlUXRBt1V5JiFcz08DS4IMsGZqZq-bvTUpvGo_0mQPdXKHJGWuUO4xoYJjVKTJQd6DMt7fSapBoQXeCpXhfqsydLq_POS_LqOwm2eu2dvpv7MR9hKzV7QpqUiGi4S0Vea4uFxJM-OQUZEHISJLQw84D63EsT0eiMgrJME3iL2W2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq84tSKItw6sY16-FjTmvlsozeQ6M1aJKAadys_a0imhTYltox_VUTZq9hEtv_fV0xNEOC4EYqy5igrE5l852UWjKXtvKuYFYIY1tDpL3TMq6V8fraL51XkX3CrA7otyHiuhoB8KCh_W4jTUJSwbvZyrPX0lLHGs2Bi3M2x4WBqPV8-TdnZPMVuTM_ugYMlKMusfsHHZCnjoaZLjkyQJTA6sK5LEIxjihAYeK-_pmniVEEblPElIHTYkMqvG--VxabKgecUKHc3yAmi1MHEvcHm_09dUrLyWnhNi2BkFFcWLqLo1NRX95BgBBkfsPwlNzYop_TxL5dFuPiUbvXLWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSbMFhd1U5rGYwsgPHogSMr7BDVX5_5rIbf-0HtBMVxSPDw2fsrrS1xPrtJJ13MKyPaxiEcChhntZ5zKotuxUvXdWhlnXF1IvWswzOhLJXyn6vRHY8J86XvQOUTALVeh78OEZMShure9pKEGJ78XhtIkJ46e_m_WFuLqo62qrGF3ff63DSXMZBwnGZE3P1yO2xZwg-2ObJPkxHWT7aDy_Z_p74ZeI4V8KHDuUl2pE40lHFj9CPFOCAtvy4QlZvGIxb6GOsJZNCmAuF1Yh2OupBd2iWSOHynCJ4_6mR6-6-l14K-9Iv6Zm-O_QYsPUsPL7LQBIs7C65eLpv7SuR8jKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=nUsgVWetHCm-ehNBx3cYkA_IFcV563olQya_SWmRUd5zwokrdKSmC3eCfti2brNfk-txnbapvY7NuZbBVCY9TrZ0YmMWkQJ9Pe2qYU-igjwSnnk7B9S7c9ynM_3KQrI703fvwREhkcIdPGZwbNwom019_CAJECsuBbReuBq8AQy-puIosAUgxlbXEGsM10nOo90HyHxFPFl2wkZ0nmMPKgKVUJhOkOWOLceDBqVnvMDISit2qQRcuUtN1p1hadjmaBk4vIw3pvUBNzJYWaxX48ZkysCKnjfYIpxRdsZrnkS5VtDrfRivJQkL1-Joaqt71mpwEqA8fW8zqB3RVCSPww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=nUsgVWetHCm-ehNBx3cYkA_IFcV563olQya_SWmRUd5zwokrdKSmC3eCfti2brNfk-txnbapvY7NuZbBVCY9TrZ0YmMWkQJ9Pe2qYU-igjwSnnk7B9S7c9ynM_3KQrI703fvwREhkcIdPGZwbNwom019_CAJECsuBbReuBq8AQy-puIosAUgxlbXEGsM10nOo90HyHxFPFl2wkZ0nmMPKgKVUJhOkOWOLceDBqVnvMDISit2qQRcuUtN1p1hadjmaBk4vIw3pvUBNzJYWaxX48ZkysCKnjfYIpxRdsZrnkS5VtDrfRivJQkL1-Joaqt71mpwEqA8fW8zqB3RVCSPww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=rjdGe2AoVsmHohN4-iUadQ1dwKFsuIkYsnycDh40mSmNoN2jC_gJIjT5pEP0ntZ2bR6wCU1INP07kUoztAtu-qHP3pOxJKfLtokA-4YMDQ_P5d-bgfSwpcc9Qa4GQSrBQev65Bmruqa1zt7sC0-K1sPa4SLG1GyteBlmCN4epKUtfpg7S9_Vqz25c9gCz-golLBvX5S0w907HQdjP8Cb-bw1mZGEqSIjRJKJeqtggwbA7MEyWzGgSqYIwqNK1v5pSu3gbOb8mF6iTP1TrCYo8yVFPsJ5OGvCV-1SoBHTW5PXEvvPBKVMHr6TFTxAM4alUZJXbPzUFw7YFXgqvlBb1ofF6V33hBrTO4ZTUvLG7xZNuhtQeqLnXZ6PZGZnwcaioBbRWtWKL5hBk0dNL58fDjTdFfX3D75TAyyKHmK1Qz9ACyRGF1Oqdic6alm1E3FVvzTniE8m9IA-uE_m0J1FZU6s9Bp3r4pYWyPxso-qapAHeWrstNtMlubusYVGqDRTnkZnMS3sScyZjVlAK8X1if9JlvFEjKwkwQSPJQxD_VuKChypjOYgr9FCt2PN3KUcYo5kHDD_Tx7VAKHzG8ICKtm0Hn7FaESUgmu4cjuwhwtfTQfUIUWm9oltefTkgl-Q0tkNl06WAmaNVncDZ9rsPqsk3hKGk1mn1jODd07quFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=rjdGe2AoVsmHohN4-iUadQ1dwKFsuIkYsnycDh40mSmNoN2jC_gJIjT5pEP0ntZ2bR6wCU1INP07kUoztAtu-qHP3pOxJKfLtokA-4YMDQ_P5d-bgfSwpcc9Qa4GQSrBQev65Bmruqa1zt7sC0-K1sPa4SLG1GyteBlmCN4epKUtfpg7S9_Vqz25c9gCz-golLBvX5S0w907HQdjP8Cb-bw1mZGEqSIjRJKJeqtggwbA7MEyWzGgSqYIwqNK1v5pSu3gbOb8mF6iTP1TrCYo8yVFPsJ5OGvCV-1SoBHTW5PXEvvPBKVMHr6TFTxAM4alUZJXbPzUFw7YFXgqvlBb1ofF6V33hBrTO4ZTUvLG7xZNuhtQeqLnXZ6PZGZnwcaioBbRWtWKL5hBk0dNL58fDjTdFfX3D75TAyyKHmK1Qz9ACyRGF1Oqdic6alm1E3FVvzTniE8m9IA-uE_m0J1FZU6s9Bp3r4pYWyPxso-qapAHeWrstNtMlubusYVGqDRTnkZnMS3sScyZjVlAK8X1if9JlvFEjKwkwQSPJQxD_VuKChypjOYgr9FCt2PN3KUcYo5kHDD_Tx7VAKHzG8ICKtm0Hn7FaESUgmu4cjuwhwtfTQfUIUWm9oltefTkgl-Q0tkNl06WAmaNVncDZ9rsPqsk3hKGk1mn1jODd07quFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCwKDmOaMKp4zui9ul-nvRkzmzNwNaIbzHRVI-bVC5oHKw220Xx-yVYyLbCIPRyIKvkt8CvqFWS2Xpyx0lOJfsnBezdyLhr_XlV_v-9OrQe7AucAYJowJyOaq5GIrwqSW4TH9owoldDNMjGa7DwFz4RNsXhsHdBxr4T0eM0JdbJ8_aRTZ13zjVPL4FKCx3yINAdN1czx3uQeANnO1oQaBy8I8sI7a-07sXv_d8aWGMNwKQoqy_-6ajB2RZUmDjsNbEK3ZNNejwH9tN_4UV8p4yJ1P8hYBjro31H1NsUmzJBWgubHl6dsRHp3ueKIyAIKDa6lhUT8HrU2XiQP7IeHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh_PYgQ5HB_Wkc5Rxe7WBqiTpYyr5osn8gJzTvb1I4-RiLsCL_CfIn_KcAeHed2AaqdZf_90UJXa2ieAZ-DXjIN_MmwSP21jXT3xzGsndttuiFvQ-ZDbe09JA0W7sMXgjtKTgyZ-BtCGHKoY3d1J2FZZIuSjLBQtUmmgE-t8K6zDrQ7mwkE40iaZH0KTNf0HjrrE3VpOY8jB3jR0-7i7Ca6PzCIQdr529ftdokfrpSQ43-zM8NHPIDb6AFtjT0tKYcRn6wU2JiNeLr7S3KaWVDgvkZYs-oKKaQ05s7i6xUlU8QVc9DMsjvDR3lUq7yQRKYQ0d3hpH7bzuZtk7PCeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtkVTvI-VypzaF6HdzMf3kda54yupIMyD3LlE_QOG186_788kWNexAtA6cE1FjXOSrC2EpCarMYT5I-Ny88T2GkZ8yh2ALARfQBbUx6bFh-PD9wa5yaB_glbNPPjvhrUg6rxItA2xmi8zEVmWJGMM67fMpZ_eG4AwE6xLtgV3owqxskB-Fj9K6mhUWy5kwAMPXcIg6HaC8fmNRrI5YdRRSganngHtkJ5M1bwqInb9iN-NIsjEml24_c3RPl0VhvdalLtnGm99Z4LSsYfNN-1mT8ZcpGIBQvWqSZVf2PfNNrE9kPzQvEzedo0Go6hlYOwJyvl3MvQYe6cX776Gq5iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJO39BcTuaOACIlQ5Pt_LwoNk7oHnp8kzzFI9oiQD9PWXZVI4CdinWNSMPqtfuDFwtzNb5XuwA_0OCLkweDp5RbjuzUbiUvtGtdNtfzpp_L14Xa7O-4MgIRUtFBzjm5OuxkVY1bQEFzNsSLTjh0JYjA7g3d9yZd2uE-HCzbu3yAWQEl00AiXHk1Zb8m4qWJ-mlTAXm1dtC5ShqlyDS7E71fqR07b05BXopVej4o40cln0hoLAQ4Z2p7DyEDGaGRYGJo250tk2yQQ1HSysezJoTU77uWf4s3RanSLLJ3UVHO8WLqd7-6KVP93JlV4en3nc7fQsR41S4VOksn5lnzihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kegmhAeE7SeFlBJ15Tfu384opvKM9Bs2mz4XYu-PdKkxVPrhZRQHTlFQCR1_yodhNtO6pDUqISEADvFW2a_bLXhpKRER57QVqGjKaOgYT__5ep5tP14NTMWPRjglkINtLZqduMYdF1tr9vPhYrr6rZ3ANdWZ3PMz7FU_w3FSVBH5w6EykPuBqASlI86i6E_xVR1fxghbkJlySLt8a-kEkUSVCWyoqssmEebLKCw_CSJBsXViBfISmwUmNBGh7fJbbq4qTqsmu-81Oo6jYpVG1xaqYv-LZF4DMbvaXqeyjdcUy4cbGP164paAM1Zg21AUZMPLKBATjr4znQbLOlVx_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSwQ0vYbKiQBf_Z79PXyGNlH7gNiQR81ig0-PoXIWeTuh_JvBbe2ZWIV9a44FNemgkZubyuF7QQiQXiM1oQxoSLxNM2W6k0ieNc9_MY2AC5MDi1fIf4rUWlQvtvmY1vq4AiJSNShYtNHSv5BUKqQ7GJ5oBZ2alXdytTBweuf_P8ySr-95vzggaeQhUlz6FCx7Xd1FrMtk1zYrEWCNE-tpkvcBNPsK03USGfUWXskkJ7mLfJt1IIkwXenpGNg7WDtkzuyz2_wvJtRNUVOVwHkgkIvpZziYygz_rT3KEaItA8OzKwPldDExEDxm6VP77DK8m-QbIvDbdJvxvfVTMwSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqmuMvgMrNhqcFj410qCMUKOacuqpuM1_2RXx-CdbXN-dthuvJidDfY5hLTIi-ch6DUpAkWMK1QEX44yuKFiTpMlfHZbu7143CXHM2Y1oWpocadyf4hLEMkB_iZ1K5D8lBNPePxhUwMKfajzLkCKLddl6BxFw4P1M0TPr7JSCo370N6_e1vKEOvMJ5jlrCn2Be3pTgFcbM2myXkPDhIFTjeCtdIChZFWQJtCnjv4Orh9ESsk8UKnXaH8I-NPU034DjihrzMgwFzb52CPsH9A3xOk5dwj2Q89YxLMQHnjdKFspaWdTviQcsdE4mdE-HYS16BHKRKFD5fJnw96nDDEsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=pt-hSI5CZM1F3xZVJUEuC0_lMK5mT1JwjNCIPzXXkfP4TwHlFfD6VmHtXu3nXwT4bygW-fHBN8ysIwTbydVVscfizyHRFfH8Vd-PHYH_NjucuKMHifH8MszPO5Je498qeVjSV4uOFUb4cEPzdX46-NnuVBi0c5rITTihsx9XjBtpRNFkXpAHTLPlr3dNeuVbwIfkgEfQ4nMGSQBUyHFaKq6e6eX-Q3lslabbJQx1HW414w82OD8gB4CVVEgttkumU4QiKC87Ol3TFWD-SCLo4VPZcqQuTFsCeJDLjpesBc1wzb9bTTJKvHDmov8N5bGzvsKmxyz7RvptX3aRYLQK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=pt-hSI5CZM1F3xZVJUEuC0_lMK5mT1JwjNCIPzXXkfP4TwHlFfD6VmHtXu3nXwT4bygW-fHBN8ysIwTbydVVscfizyHRFfH8Vd-PHYH_NjucuKMHifH8MszPO5Je498qeVjSV4uOFUb4cEPzdX46-NnuVBi0c5rITTihsx9XjBtpRNFkXpAHTLPlr3dNeuVbwIfkgEfQ4nMGSQBUyHFaKq6e6eX-Q3lslabbJQx1HW414w82OD8gB4CVVEgttkumU4QiKC87Ol3TFWD-SCLo4VPZcqQuTFsCeJDLjpesBc1wzb9bTTJKvHDmov8N5bGzvsKmxyz7RvptX3aRYLQK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBc6ClfYovUtUfBKhHOIqnx_yGjxbaist6EJ4IqHT8SXt4ld5D9tQJfOzaj-bekEiuszLMALGkjGBw8eAJfD3E17s5QkxsIFjs0-YY341UbOHROgSb4PQYEW7k4UK-3laBCamI_xjoaM3MgNJSnuXfw4wTQiPfhuaxg4SRkX1byp5XNaeMYf4VhMJI5MIpKuzWOx6ugg7N9rILsPlf_6Y0m1ZR-E2HdqxZ0bXFc7JbnJnnQ5IWUNfFmUJdAhsZ2fbLRUQXNbiN6WNCuizqcMogqxP9R59zXyq7Dpzkcs5X820hae05emX_1pd5OzvES3QfJ_rijWNqYceFXbw_BpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLz72SpbaHlpE2k07HHtjQT5AftNqxIM9LCyx_k_KA6wrj92Oqsv_s6rKc9BV7M5sJHlzmmncnMo6OLMoI1lZeSTnuDWh3lewxU3U68rzPfzzVXJh8xIdL1ClbZBtwfIhtAK9EGxomfPqbBkjSKFkY73SyOJmqFvzoZA4W7iJckOzIns29P-YRJ86l6DRgwaHSbM_vCetKwBTJNmy6cEESwfGSdEA01ieTbo5oPnyja36Pt_RU2fCCww7zR7_4d6ANCa8iKfEiWRPlP6Jw2iQfsRtehRDdEQafsNX5mpvL1RUbLY6wbcV5oJSIlwUVJ-8usBk_ktC4VI0urQacZh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0IgP4eWgbl4xXKC-yw_7HiSrYhrC1Oq3NzZOMSBbb4KJlkWCuujXy7JvS8IlRRolDNWv0k7y3lP6gbDnHUP_IG9z0nImNhQb_5XIhRgmpxXnBQ340ENIGg0kCjQBNkm_W9SocLYTYvEiZzcrOYlB6UtDBER4kQMb4QUNaBFYk2OXog3VMr9BG3rsMApnWsvM6D8twgWWOm_HqEuQTALP_553DYGAuMGIEeYUiodOjpj5zDU6oxFsbXHNEBTh1DItBs562vtCiq9Eii27R5m4jDwOnYvEve0wiXE-TlTgfogM_p-0_NumyAXsxa4lEQBT45N7SwJ4KQEtPGRN7GWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-ebTO_YIs-eW4cuTETLenNsJOW6xucn05kXO9zP-r4I9YnubxxOiTfTj5xgLT-1JNOVsBkTCnnMaPmb8OUm05lPcSPxHxCoXrWK1czw3qAp1HHwZq5aFG9E4WcT_CTwQpS68UB11m95DXfNAhEVEhi6ZkBIrWy-IdoC1XoctvTSBXqTIcVtYica8ygGLfsu9nobvemBWoQKyxGmseNoyocycRU8i16C9bxAZlAgFOREyafwWLCXQOAxqvCh_zKjeIWluYRkYI1yijdXoRhRKQy5uB8hGd-5r7oPtrEKZuXmDHqq6bVjSC-Gntfw375PPNV86AMT9Yc6-OHQcIkGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=te9-XDwIBTIriT2tJkSASYjO1JoBaSX0RHEkic6WxVhfm0ieiSSK-4X_RDaJ2nrs090tIGwTLugAyuwQ6Ccep4AsEtvBcV8R2zhE2kJQe6V1xh1ugpEt3aypsnj9L9M75jFSkmQPjBM4tkIm1XZgHjEkvkFpitcAA2XJgWJmJmCO45XiOBguWrWh3grIzBjIa3GFlPWA-w_l7vMo1chMrl4wbCxaPbU2UxzQQIGKGOCSR6zJQJJve13DxS9KLiyX7kP20HFJ_ZSwjzDVzawlQE1leYyu6JxevjUQmtfyDroV1mjsOx-AKEvzcQTEt75jS4i8I5MDarOJU2Bdk-2CMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=te9-XDwIBTIriT2tJkSASYjO1JoBaSX0RHEkic6WxVhfm0ieiSSK-4X_RDaJ2nrs090tIGwTLugAyuwQ6Ccep4AsEtvBcV8R2zhE2kJQe6V1xh1ugpEt3aypsnj9L9M75jFSkmQPjBM4tkIm1XZgHjEkvkFpitcAA2XJgWJmJmCO45XiOBguWrWh3grIzBjIa3GFlPWA-w_l7vMo1chMrl4wbCxaPbU2UxzQQIGKGOCSR6zJQJJve13DxS9KLiyX7kP20HFJ_ZSwjzDVzawlQE1leYyu6JxevjUQmtfyDroV1mjsOx-AKEvzcQTEt75jS4i8I5MDarOJU2Bdk-2CMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvuFY63SqhwfTwzNCSxiyxQM_JUmfzvvgKcSBRj4RdJKGQSDSEnTHZ_-Z1VaWFp6Zpb7IY0xqIPQf18c4OSFElFgDiyJRhLgEUs_y2wgAS6vltWE52ZHe8MpgueGp8AQHNgTTg53LmH1Zr2dj2fOCu-sy6HXpdyGfbHlTThVaH7mmJS2rG1RYju9Bn2nLym0L-2NsWY9RsITesd6a_KfvzDqsaYeF-QIgI3hIskoFIy4y3lRChQM0ZN7khBcpMZAhyF4mL6SgYxZSZX1dEdY8BCzFRxryJTtW31EhUKA5o17P1Mj76ONfLWh8NBw9JqkwJOxfOys-ARUg2C97DjsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHz5h1SUmWv7MFA0vNFdbNaMqUbla1qHoL7pDro-SKYXEgULFMeJefMjXtfO7c2_dzBUQdG68lpTbrN0jeXmPKkpUqhSYPyca94iips2v01DfVf5U6TGbvn8Ful1ZE4XQUbwu-ygEw8m6M0XldrkUM0xnEg5ugz-E43ly9yZw3LMNaSwBrge3daRe1lwSARmlOuuR5EpaMqVaVh7xU07DIktDEKtwknGnPjSfnnoYJ5mmfEMxAijxXwjDwRMID_3TysGu4sT6ivUcfJXwFGecnq-AWkrLk1opAr093hyglTuoTjrjf_lZZkfm1SL2e7UwC7gi2MgzgRHoW_Fs8uBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC1A7t1ReATobfs4OfAQFm5X3zXF8IfBrtIh7TFK6ssnLUunNsOCvC3Ny15hHUGrgSiKtNOZ5DDgGYi9TDEsha0kVdkQYaMpOefGqfjGWFmD9-0WBeAaLVQyVqRoUB8WCdwD3i9kID03V2cim0h_g2M8nNOpXmk0NuWENf-CYyZE2MpO_Ls61l_fP7vfiqUJlupva3U_fNg6sBx7--zrxT31-b9FT-EF7Ik1ApULmaY-4prhtzHwup1--zyrgAvVw3yzOlytsBFI20tGDa59fmoZO1N7bqmwcOj_QSsZOmEVnKdOll_vMxGMJaDmcSJCsaQ8OpjgKX32yiVUU3auSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=pAFaKkvPSzp9M9u0qCUDSAJIZaQ7PzUONS2kQH8WQsZfSLgjRoBtjzlcB2P5GgrwnxJxKedG_yz3vVSVaets05DDv--jELtvB2z8mkZ6xK-Ic60-NVj0UEGkB8rk2FGpYiSkxUEiBpoaA92Q8PL9dywWa7rMMuCDjW0qjpJJI9zY43KL6HNwfzo66YQ0wWnCzAcsQZ02BXYCdaNeEzybDpfCtPLro5eCOQMtO1LtQdvi1fv9atczzCGPGdVQ6KGxGTMOL6O6V6CGK8pndbbiIfLMrhnzE5BGFmZg4KjEWqv2K0Rq8NIv8rEYcYqVdwGInksMvG71oz9EYB2tRaooOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=pAFaKkvPSzp9M9u0qCUDSAJIZaQ7PzUONS2kQH8WQsZfSLgjRoBtjzlcB2P5GgrwnxJxKedG_yz3vVSVaets05DDv--jELtvB2z8mkZ6xK-Ic60-NVj0UEGkB8rk2FGpYiSkxUEiBpoaA92Q8PL9dywWa7rMMuCDjW0qjpJJI9zY43KL6HNwfzo66YQ0wWnCzAcsQZ02BXYCdaNeEzybDpfCtPLro5eCOQMtO1LtQdvi1fv9atczzCGPGdVQ6KGxGTMOL6O6V6CGK8pndbbiIfLMrhnzE5BGFmZg4KjEWqv2K0Rq8NIv8rEYcYqVdwGInksMvG71oz9EYB2tRaooOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=uqVTXeC6OH11uTNeBZnx2kBBrLfy2f92v_Q49YKxERk2ul1kkjqoByi-qfMsJxUuQi6K8UPBu3Z_foxP54UY392o_uoejJR_zHUqVUjKyWWaHf77hkO42PBXePQVbA0zpK0nb9MWJs3D7G7UUtFlIK3xtC3xkY0yKJgie-sFdLcQ9NZ_YoI2Fk65MuyDKfu-OguhhYu951G1NbWyAuEMNPIlgftPFnYMiD-KhqoVbKSSabymvprTspj3YsFq1bXAME7qvT0fKngZOJDlukBEPylB6k8M-SYGuTswDCnlUZgN1lVUxaV1UU86N79bMEKEWJieADCwEW9VL5HNUxLDjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=uqVTXeC6OH11uTNeBZnx2kBBrLfy2f92v_Q49YKxERk2ul1kkjqoByi-qfMsJxUuQi6K8UPBu3Z_foxP54UY392o_uoejJR_zHUqVUjKyWWaHf77hkO42PBXePQVbA0zpK0nb9MWJs3D7G7UUtFlIK3xtC3xkY0yKJgie-sFdLcQ9NZ_YoI2Fk65MuyDKfu-OguhhYu951G1NbWyAuEMNPIlgftPFnYMiD-KhqoVbKSSabymvprTspj3YsFq1bXAME7qvT0fKngZOJDlukBEPylB6k8M-SYGuTswDCnlUZgN1lVUxaV1UU86N79bMEKEWJieADCwEW9VL5HNUxLDjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr7XZ2f2tMaY033WShcPo63A65B8_GWRKIy_k2ipDnKDoIjP4XtP6f8mIdKI7E0Fed_gqHc_xz88XrorbcuskWtoMo13Ohx8gQFFwK4RZLQenUB_2YH6fFt7CCkhkHD82cHr_4EuQl8vL7K85lxh6UEWL5pxRTooE5mObL2LAwTKm8slBEfrRXx56Hnr6weDItVadvzMOY8ILZGWNwr_YlaX1T2LikIfzEfBkGGKDqozk5sl_CTJBx0I43W3nnGDrK-sxKpRTfJ44NGgwiKyFTYXri1aUbxYM7YGLYV_RW5RRQ7UYw8BU3f3GZ-3p_SWdWI0edxHrf5-NLn8qKLlsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAiVmrLyuunBEZdGc_fmpebGy_QstJkzY6SU8bnFexq0n37fqmtYcFSIgeJ2L91kb-17pQLe6UmLOuByCNxOiJzAO71jp29lGqsbnpr6HK0H3c8dUewL8GIuFok9Ndw-kSuTmalaUn8bldqzUQlg7nGI95TqBnQd68hDq--gs5wEos0GiE6oX9hiPJMDYqGESPgQ4LZCDoSTaptDH54ewjycGJu052QZoI-5CfBbyC4mFXxOIIQdTbVHlZv3LX2T6PotIcPypBaa9-evUqEWEnP5xyr1nZM19CBxpOKAdwx1FTfbIsI5xA05wxh_TF1Su8Nw0OEuaXZCc5SCllIR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=kz5AJsikhDRcmf_uI3DmWSyYhNoFo2iv7GNhTTUIPBrsiQGKVOgoZVbXOU2KVPdHT8udKlcY_fr10WIa2-QgI_ieORTYDd3tee9ZpvMW3qwFtbTM4I23obe8dCV17-L5gWHd3drpOkuO-L2Qrv7rwMvEwvS3Qa_ZwCAcaBeHKQA0XiDDkrJuSmpFatA7iMtZajKvNdibaJ0B_bZGFR0nLM8DsUhYLff15L24UGgtWkiCfrb4IDJ40K_FCwcP4fVyvQx_1UqEcbVXWmXf7R4g-FACwPLwgzkmtVXx8IAfURtu0118C53eYhIWj4JL_-0ankfohdeRd-BS1SpcwDy_vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=kz5AJsikhDRcmf_uI3DmWSyYhNoFo2iv7GNhTTUIPBrsiQGKVOgoZVbXOU2KVPdHT8udKlcY_fr10WIa2-QgI_ieORTYDd3tee9ZpvMW3qwFtbTM4I23obe8dCV17-L5gWHd3drpOkuO-L2Qrv7rwMvEwvS3Qa_ZwCAcaBeHKQA0XiDDkrJuSmpFatA7iMtZajKvNdibaJ0B_bZGFR0nLM8DsUhYLff15L24UGgtWkiCfrb4IDJ40K_FCwcP4fVyvQx_1UqEcbVXWmXf7R4g-FACwPLwgzkmtVXx8IAfURtu0118C53eYhIWj4JL_-0ankfohdeRd-BS1SpcwDy_vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
