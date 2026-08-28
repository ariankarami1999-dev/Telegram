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
<img src="https://cdn4.telesco.pe/file/CGvn32ygBpzMVJUiNGt3bd1yWe5_UnTBWu2THQEO5JA3ljS1wqXVpRbbNF7uHzRf4mReuSBzcKqk--P32L6XAGxWcYzyCfV3kWp5JzXYbczCHFMIjIadyou9NEFGqXHhaaTSmiGtoFkzEsIBP1zI3xWdNxUzUrrv_Ybe9OY7JY5bxudMwCgxUtENMaJgqL-T4xW8TF7eGq3VrcFkmiHzohQvmlaS36-sKP3og545z7nrFIiJYdA9vjsqltD-LLIZfSV0ydIUMadOPFXdz2MVEcObtfZZ5EBvvjbylv0fxve9_Q39o8EJIgxIk_F-tpJ6pgjrVIGGUZQE2pnH47gIlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-139088">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=SaPloxJPlJoGltZDx22ZH23NYokWk6aKnMndTnS0b4BjqslftJowFZht3bA27bjTNlBgpFHLiIqo6f6oNqN2nqs3h8YdH2fb9-mYnD5kEz7NDgCx9bVTZuK6QvhlVfJ6hMl44aaA-4T9l_MP7DNo2Lk4NFEBvHZrQviH8KnmkxU3PtolzkKlUOKfD3_IoEhnWSx27-BZWclelxo0b0Cs1fLWRfGsb07PG7TSl4BSNv7_wjIaczObKg_qbpjcdCr7o1LCxpR3Na5T75D-vAowGswJFwImimMpvqsLqUUxkXLVN8z7U4V0gFz-l2ouWJSp9rof0WNtH-vSfbQyVOU7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=SaPloxJPlJoGltZDx22ZH23NYokWk6aKnMndTnS0b4BjqslftJowFZht3bA27bjTNlBgpFHLiIqo6f6oNqN2nqs3h8YdH2fb9-mYnD5kEz7NDgCx9bVTZuK6QvhlVfJ6hMl44aaA-4T9l_MP7DNo2Lk4NFEBvHZrQviH8KnmkxU3PtolzkKlUOKfD3_IoEhnWSx27-BZWclelxo0b0Cs1fLWRfGsb07PG7TSl4BSNv7_wjIaczObKg_qbpjcdCr7o1LCxpR3Na5T75D-vAowGswJFwImimMpvqsLqUUxkXLVN8z7U4V0gFz-l2ouWJSp9rof0WNtH-vSfbQyVOU7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار:واقعا از شکست پرسپولیس مقابل تراکتور ناراحت هستم اما این هجمه علیه ما طبیعی نیست. ما اینقدر در ۲ بازی اول خوب کار کردیم که رقبا ترسیده‌اند. احساس خطر کرده‌اند از بازی‌های خوب پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 455 · <a href="https://t.me/SorkhTimes/139088" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=M5XZgSGP_AiU1KZG_DjYYx8yTI39sD1aSZPJH8MAOJw8lQbnj3Md67ZXM9vML9dAEccRH-pYgSxi9AcA6QuLYPXesC2piRodRjvgXpMMeEclreAS0Lzb3SzIMo749zisA8oY-3zA6JjMpqzOXylaa5B46faj-jzkgdx1mMo8mP-5BfNucTug2uIxxPs9mVThQDaLpfWaD3h-M_Wa5PkFA5N7U8P5rbaxOeQeuX-wes1J8pVcmpiZj91AnrXJNnus46sv9U79Rgn_WlhgcNYxNYy_Q5cLh9VHv0Djqlj7eFj6tySEPmxC2eX83MNNtIV0QQmMt6262YKYAum044rbOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=M5XZgSGP_AiU1KZG_DjYYx8yTI39sD1aSZPJH8MAOJw8lQbnj3Md67ZXM9vML9dAEccRH-pYgSxi9AcA6QuLYPXesC2piRodRjvgXpMMeEclreAS0Lzb3SzIMo749zisA8oY-3zA6JjMpqzOXylaa5B46faj-jzkgdx1mMo8mP-5BfNucTug2uIxxPs9mVThQDaLpfWaD3h-M_Wa5PkFA5N7U8P5rbaxOeQeuX-wes1J8pVcmpiZj91AnrXJNnus46sv9U79Rgn_WlhgcNYxNYy_Q5cLh9VHv0Djqlj7eFj6tySEPmxC2eX83MNNtIV0QQmMt6262YKYAum044rbOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار سرمربی پرسپولیس:
🔹
ارونوف یکی از بازیکنان خوب تیم ماست اما دیر به تمرینات اضافه شده است. بحث مصدومیت ارونوف جدی
نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 514 · <a href="https://t.me/SorkhTimes/139087" target="_blank">📅 16:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=wAsB_qrAQ4K7znFwzH0xFMQHuxhihNR82XhZ4dc7369Ns6Za_lJGmuKnZ6dvu4ojOzx1rHKf84Dq3nstkiNmq8H63Kqib25j2JpEkrU4QixXctf-do1apNqI0c0azntJqE8pXEoq0lYXg8BS_kMITm1w5FNsnTeRU0gVBrXjfMjAa0QprzjKT1I0TcoQivZG05ta1Ggrkc4DIR3_qNH_C7SR7170M0uR4aTRqbeA5I4TeBjVYZJgazBXkldn0XHemjfVI_f4Q1qenSk1FbZx4p7ZY9Vpi65ADQxeWEn9wfXPs_CuqvbiilqUAHdLhm25hnyPDHwkqFeIi2K3iu5dfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=wAsB_qrAQ4K7znFwzH0xFMQHuxhihNR82XhZ4dc7369Ns6Za_lJGmuKnZ6dvu4ojOzx1rHKf84Dq3nstkiNmq8H63Kqib25j2JpEkrU4QixXctf-do1apNqI0c0azntJqE8pXEoq0lYXg8BS_kMITm1w5FNsnTeRU0gVBrXjfMjAa0QprzjKT1I0TcoQivZG05ta1Ggrkc4DIR3_qNH_C7SR7170M0uR4aTRqbeA5I4TeBjVYZJgazBXkldn0XHemjfVI_f4Q1qenSk1FbZx4p7ZY9Vpi65ADQxeWEn9wfXPs_CuqvbiilqUAHdLhm25hnyPDHwkqFeIi2K3iu5dfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار
:
❌
• وضعیت ابوالفضل جلالی بهتر شده است/ بازی فردا مقابل ملوان را فدای دربی نخواهیم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/SorkhTimes/139086" target="_blank">📅 16:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=GQpHMQwBK86ulCntAi2juqjziLDDEKr_MIaJRYisV9wYNE4E1pxDGy9J-NSpPqMb1Wootfn5kDD6f9rBTY9cGQei9WxGRgJYftPYTP6_xHGteToctL26aMFanxFeyvSv1c6Ry5dMVkiS5Q_cR-73pHKS42VkqF7lkQnUUL94JmkcPg2WS_3QanCHxVWjrSmbMvQm0yUkJpO0dl8a_HH-ub2NLV4zjYMhTjB97bPBbF07IxBJ8g24N0LcfvU1xrbiKG8oN72kiSrwJkfIJbZZxu8iZQfHuxJgJtImfjaT8xTEJpXc02u8jgteqw1Bw4W2QOiJ-tJvvfCU7SvVwDgHhJ7TJqAY21M3aV0hrqxrSJGBSfsta4UlM-Sj0TXRRETTZmJPgOZVAveP0tAYx3qammD4bpnNFBDdWehxC3BtPEOELamYA0iI6RBp64LAaa_KIEMLQiF9OSnkfMOZtzHMtW9G4hO0kZ4pwjSuE028uJI7Ys054VpgzAwT1dDwvkTxMdkPeTPkizfE6sQi9w3xuJXjc3isM6EJyM19Le9nNbvZXLV2RluoUj78AF2O1_AfsV2oioblhXvCMH56F4g6_J0-RTdUG0_6D2NJcB0UivDFfmyoKCuP-pJl36796MV3Gs7mWfpN3ALp-9WapEtj9Vs9V3eQMEC3bhQehVojMPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=GQpHMQwBK86ulCntAi2juqjziLDDEKr_MIaJRYisV9wYNE4E1pxDGy9J-NSpPqMb1Wootfn5kDD6f9rBTY9cGQei9WxGRgJYftPYTP6_xHGteToctL26aMFanxFeyvSv1c6Ry5dMVkiS5Q_cR-73pHKS42VkqF7lkQnUUL94JmkcPg2WS_3QanCHxVWjrSmbMvQm0yUkJpO0dl8a_HH-ub2NLV4zjYMhTjB97bPBbF07IxBJ8g24N0LcfvU1xrbiKG8oN72kiSrwJkfIJbZZxu8iZQfHuxJgJtImfjaT8xTEJpXc02u8jgteqw1Bw4W2QOiJ-tJvvfCU7SvVwDgHhJ7TJqAY21M3aV0hrqxrSJGBSfsta4UlM-Sj0TXRRETTZmJPgOZVAveP0tAYx3qammD4bpnNFBDdWehxC3BtPEOELamYA0iI6RBp64LAaa_KIEMLQiF9OSnkfMOZtzHMtW9G4hO0kZ4pwjSuE028uJI7Ys054VpgzAwT1dDwvkTxMdkPeTPkizfE6sQi9w3xuJXjc3isM6EJyM19Le9nNbvZXLV2RluoUj78AF2O1_AfsV2oioblhXvCMH56F4g6_J0-RTdUG0_6D2NJcB0UivDFfmyoKCuP-pJl36796MV3Gs7mWfpN3ALp-9WapEtj9Vs9V3eQMEC3bhQehVojMPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مازیار زارع سرمربی ملوان:
🚨
پرسپولیس پرمهره ترین تیم ایران است و کادرفنی خوبی دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/139085" target="_blank">📅 16:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/139084" target="_blank">📅 16:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/139083" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiksXz7dJWFEMAzOXhibjP7evJZMVbdW5SWDu2armvMmz00lXxqxqoJGySV2zJy0rb8GHk46HX6bgTHWpOZM8y6fy7Cwbf6PKPUx48PtYGygoqqo37xXNUfk4PhfwNg8ZVteG-08BmTlWh3XkbUSaBLq70H2i0DLMyl-3z_Zgeefmf2eT22dKqRtt47AB0wJvtn8oJkr9qEAQEJSXQKoeSnq_NHKEyHR88I_ujo1-S0j1bQhTVCHWs8gVmbES_C9bZ2jueseF6tJ5YR12kLagtFiL_pieF5dZuLLRgKRb_XixsP40Ewnaf0cxQ0bRD5IsWYG2_HXwjLjU3WkqNxnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/139082" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVvl7kwtAuGSnq__LoWqlHQj_KnooaUt8EGapg9fIzBifQpXazi6YaRuS5RW7Oi2DZZlSOCcozehaUkHexZXB1NLlt-3iBG-1Xq0ypvnj2rPLZzjIkRgyUVb9vpCk-OIy9-JPIGtxyp6lfLWBvk03x5QAWNi5WXMPtDPRCsDxjcEBBVLzF5aLbIkVqITdSl4mFk08_zPTUublAmbNbzsmgPFjNhWGANiLpT_0ywuzt0LSXuDPGd_BzrqzADFPTzp9rBktCS91YdbY_DF9Q4VlhWMEUCAtq11k9NnKyFft91PMcXax-jP5N9u2TXxpp2kJC1O-7GzQViELt-Qmv8yag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/SorkhTimes/139081" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCJU-q1QPpseGthmGcB11tE9DY4Mjf5GvknRQt3DeQteoFozYCbOq1082fIWxGwsOpYzIoE69e9YJuQb45hxIv_9cByjASKAOJ6DicWR2ta1vt0Y1uq_DFfL3q82KWJ_HP0nnZEfmYdeWGFmg6dxnJvurKHs_ht9J5WF5J2cFEEqgt16DHGlAHao880uzKfHS18Ugvw2DXnZ-tJi6xndNskkDsHCBqrnL_d_Zbl6WLdqy_W03BcOOU-cnpsFZDu5WFqn5qxzc4teGbFRPlTjiWdlgAnLPrSrsZFlBZ0qIj5i4Qn_YPlYn_SPhvAHXQb5Zf2Ua55D6eaxyb9tN8MiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💵
مهمترین بازیکنان آزاد ایران و ارزش آنها در ترانسفرمارکت تا این لحظه:
🔻
محمد محبی
- 2.5 میلیون یورو
😀
مجید حسینی
- 700 هزار یورو
🔻
رضا اسدی
-  500 هزار یورو
🔻
فراز امامعلی
- 450 هزار یورو
🔻
علی کریمی
- 350 هزار یورو
🔻
مهدی مهدی‌پور
- 350 هزار یورو
🔻
ایمان سلیمی
- 250 هزار یورو
🔻
امیر عابدزاده
- 200 هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/139080" target="_blank">📅 15:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkCnEBnTAsppRPUp65NB_T8Ww52ZOqjZvjoy1iMEmpUNTPkrCg8mpsi_MLgIiCnlleHH04IOq8fS-P_bLjYNLTkoJKW7tPzxD_TSq35K4xoNEy8Rk3AAxIFpWqz-OkLgLKHXRsIsneQ5bptZRsFMNStMSNVY4VLJ7j18Ks1EzfzZq7_sQM_GQId9Lx-jIv59IWlt0bq18-8Wy67y7tt_-8ShrKvOVK8CEiNE7HQhdcuP1w7I_ew9Ny47Lj5GQoHYjqGY73uzIZVy3eo6J7YBAZutkwobmm0QGKl-dz17BZGQzJp355u8hLCip53KMDknzrdwwno8Ox4pezOiAEsPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چادرملو برای فرار از روزهای سخت، امروز باید مقابل تراکتورِ آماده دست به کار بزرگی بزند؛ تراکتور با شروع قدرتمندش، برای حفظ روند خوب و اضافه کردن یک برد دیگر به کارنامه‌اش به میدان می‌آید.
[
چادرملو
🇮🇷
🆚
⚽
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/139079" target="_blank">📅 15:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❤️
فووووووووووووری
🔴
گفته میشه محمدحسین صادقی دیروز تو تمرین پرسپولیس با یک بازیکن درگیری لفظی داشته و توسط مهدی تارتار از تمرین پرسپولیس اخراج شده / هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/139078" target="_blank">📅 15:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/139076" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139075" target="_blank">📅 11:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
امید عالیشاه به علت مصدومیت چهار هفته از میادین دور خواهد بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139074" target="_blank">📅 11:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🔵
🔴
کشوری فرد دبیر سازمان لیگ فوتبال ایران:
🔴
سهمیه هواداران در دربی استقلال و پرسپولیس ۵۰-۵۰ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139073" target="_blank">📅 11:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
ادعای هفت ورزشی: محمدحسین صادقی به علت درگیری با دو بازیکن پرسپولیس از حضور در تمرینات منع شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139072" target="_blank">📅 11:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
مهدی تارتار سرمربی پرسپولیس، محمد حسین صادقی وینگر جوان خود را به صورت کامل از تیم کنار گذاشته است و هیچ قصدی برای استفاده از وی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139071" target="_blank">📅 10:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
هادی چوپان مستر المپیا را از دست داد
✔️
✔️
هادی چوپان، پس از غیرفعال شدن ویزای طلایی امارات و از دست دادن مصاحبه سفارت آمریکا، از حضور در مستر المپیا ۲۰۲۶ انصراف داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139070" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139069" target="_blank">📅 09:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود، فقط با یه کلیک!
📌
هنوز برای ورود، دنبال لینک و مسیرهای مختلف می‌گردی؟
📌
وقتشه راه ساده‌تر رو انتخاب کنی!
🔗
با مینی‌اپ رسمی اسپورت‌نود، همه‌چیز یکجا و آماده‌ست؛ ربات رو باز کن، وارد شو و مستقیم به امکانات اسپورت‌نود دسترسی داشته باش.
1⃣
-  بدون لینک‌های سرگردان
2⃣
-  بدون مراحل اضافه
3⃣
-  سریع، ساده و یکپارچه
🔗
مسیر ورودت رو کوتاه کن؛ اسپورت‌نود همینجاست:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
کانال رسمی اسپورت‌نود:
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139068" target="_blank">📅 01:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
تارتار با حضور بازیکنا در تیم ملی امید خارج از فیفادی مخالفت کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139067" target="_blank">📅 00:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚠️
یایا امپرور بعداز نتایج درخشانش تو عراق میخاد برگرده ایران…سپاهان هم یه نیم نگاهی بهش داره؛فورا باید اسپند دود کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139066" target="_blank">📅 00:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139065" target="_blank">📅 00:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✖️
✖️
بهمنی رییس سازمان لیگ: فکر نمی‌کنم بتوانیم به خاطر فشردگی بازی ها امسال جام حذفی برگزار کنیم
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139064" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًیــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًد۪ؔاٍؓ℘ًً</strong></div>
<div class="tg-text">تا میتونی اورنوف تشویق کنید و سرگیف اینا ستاره تیمند ارزو هرتیمی ک این بازیکن داشته باشند و ایری هم تشویق کنید روحیه اش برگرد</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139063" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🅼🅴🅷🅳🅸</strong></div>
<div class="tg-text">پاس هایی ک باکیچ میندازه رو هیچ بازیکنی نمیتونه تو پرسپولیس بندازه بعد کلا یارو رو نیمکته</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139062" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9qZyj6XPiT93WTdfeqVm2UsPzFaXwndj_rFqzP_GEfO08zQlmwqfWwUUNblokNlxozwK308UtSMIK4WDgpYqZQzAB6RoglnlOEOiT8q7vOKyXJnAZYft_youPIZzyrAy-WZLhFloKBfWx45EjaAyNsLr72xKPQ2cYqtafEKnNBrm513Ch4GBL2PzQb1JJezhGfufdbPWwSm42TY9fMDxpKpenGq51foR9UnNreG1HxVSvfLkDnZ_5n_d2KUVoqZzC_aQhkRa_JGCkgNpsQosKh6hN78Pv-5ASCCRXeIaTT6nBdKUFNQdkqdgfb7wYQaGy3QQ0jiQfqT5wsNEJPK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فارس:
⌛
مدیریت پرسپولیس تصمیمی برای تغییر در کادر فنی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139061" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=iReW0Pf-hE5SM5-Oa4F2h8JnGyRtr4-Q3Nt8eMrHijnrx84pUljAfxeKpJgTI7K-p3Ep98a8eV2AkVy7Xvu4uCPCOwyI_HLeLRaBQoU_VqrnatRkCBXVxkIXhq-IKPmQfufeQhW-X8ls2CZW5KXO8MpAqJu2LbH5T4C4fqOmfyZqPUI2NlOn-x4R8Y2chEyFY6fx2j2Wg3yocOXOU51i8VJI-WDDkdGMdilhWc2kXSGkpiCG57kSaTkdX9Vf1Bs5gsA2qMZHDYkYvLhlTuOrec_1jGx6ZOq_sEKvKCRAxFi0ng3GWlb-th1xsJ_6N8HooWyVuI72wQWAOiuDM8jYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=iReW0Pf-hE5SM5-Oa4F2h8JnGyRtr4-Q3Nt8eMrHijnrx84pUljAfxeKpJgTI7K-p3Ep98a8eV2AkVy7Xvu4uCPCOwyI_HLeLRaBQoU_VqrnatRkCBXVxkIXhq-IKPmQfufeQhW-X8ls2CZW5KXO8MpAqJu2LbH5T4C4fqOmfyZqPUI2NlOn-x4R8Y2chEyFY6fx2j2Wg3yocOXOU51i8VJI-WDDkdGMdilhWc2kXSGkpiCG57kSaTkdX9Vf1Bs5gsA2qMZHDYkYvLhlTuOrec_1jGx6ZOq_sEKvKCRAxFi0ng3GWlb-th1xsJ_6N8HooWyVuI72wQWAOiuDM8jYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139060" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139059" target="_blank">📅 00:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139058" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139057" target="_blank">📅 23:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
قدوسی: اورونوف تو بازی با ملوان هم روی نیمکته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139056" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139055" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔄
❌
اسماعیل کارتال با فنرباغچه در مجموع 3-2 تیم لیون رو تو فرانسه شکست داد و به لیگ قهرمانان اروپا صعود کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139054" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpP9C-zVuiFv7_iyNTW4ZjmUq6PNWl4RLkN6u9QpqhrShnaIRc0BsjfwessCTd5FQ8uKcIMOuyEHkLQ5V-39rSkoWcBglZWScJ2c44G48oJ01DBceL83l2b-ip5BD0-DzISKf4Ag5dpt4eIa8f10Zy49AfdP3DLSZtLOZuGseS66ZvGMe4ZO7EEXb_fb4lw0CrIdrXSdCkbVaDNm_4JIh2ckE2de4tLeQcTrvICopIugOxeK7ikSFBwFMSzgbStv7ySjvdwPf7JwTmNmB6tzjxb3cNFOSk9WVpuXLy3i3pMqxGH9HKngxbWTTfBUShf-ZorFl8gV4zGVFMkgycDirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
آبی‌ها آماده‌ی شکار؛ لوتون سد راه چلسی!
نبردی که می‌تونه از همون سوت اول بازی غافلگیرکننده باشه.
[
چلسی
🔹
🆚
🔹
لوتون
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139053" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139052" target="_blank">📅 22:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139051" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlXtowd-j8vmobaCvhL3m_nMFJlOZvMw4kD5bJnOIhlhH1q7xVdQHQdEKweexBWro2Ew8pkqDVd0Ny41ep0Jf7Lt3eLteOYh_eI2orxNc54iWozfJE5xtPLV21It7LmBFil6MQqHfyiR3RWogtnTKNKPbnJDVD6dQky6oKL3cuUq-jXfhkownyq05KBZ3DWoO9tzFDKF_pYyKyw2En53fRmjzFUhS5CmRpoQWy3el3pd4lanXVLKaqNK3FuE5rqxDj47FwSJ1QrJwHr60pxD3_1WM7S7SRXiPAjHXzyUuLFnsO_sz6SToS9eqbkuZs-2WOKSBeDVBdZy5-LFMrw7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139050" target="_blank">📅 22:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139049">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: فراز امامعلی مدنظر ما نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139049" target="_blank">📅 22:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
فراز امامعلی: پرسپولیس یکی از تیم‌هایی است که با من مذاکره کرد. اتفاقا به توافق نهایی هم رسیدیم و منتظرم ببینم جلسه عقد قرارداد برگزار خواهد شد یا نه
❌
❌
راجب پست‌هایی که توانایی بازی داره گفته: هم دفاع چپ بازی میکنم، هم وینگر چپ و هم مهاجم نوک
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139048" target="_blank">📅 21:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITAebf23ztyte-Mi66j0JoT25i0Jgfnzs7wDT8Ie-wPSMSpgMEFAr6dWjCZIHAYcUrESWOPodgra6VqBtGoNGdcglP6u5AVEOrpDLIyJ3tSF2INipLp8b-yghlbg4eHq2mhj1fOOfXEu6ncNN6RA7hSjddKGWPqUnugOeTEg4R7NDr88DzjBOn9pufyWAcxTlpiszN_T-g5Z-0cHESRhz-HCnXd9NbPNSWVQNyESrdfHIdWpGQyCcuka0BuNWYHDO9NKRrgrhy7erHpVA_81GrJhFa9scUSo7Fkkl6KgEp5iVna1DDaPPHL4BTh-XPR_Z7OxJC_6z8Xd7j02nDsMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسکواد پرسپولیس با ۲۶ بازیکن برای فصل پیش رو بسته شد
🟪
۳ گلر
🟪
۵ مدافع وسط
🟪
۲ دفاع راست
🟪
۲ دفاع چپ
🟪
۵ هافبک وسط
🟪
۳ وینگر چپ
🟪
۳ وینگر راست
🟪
۳ مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139047" target="_blank">📅 20:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139046" target="_blank">📅 18:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139045" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🔹
🔹
🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139044" target="_blank">📅 18:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✅
عادل فردوسی‌پور: فدراسیون لحظات آخر تصمیم گرفت سردار آزمون رو برگردونه و به جام‌جهانی ببرنش ولی یادشون افتاد اسمش تو لیست اولیه و ۵۵ نفره نبوده برا همین نمیتونن ببرنش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139043" target="_blank">📅 17:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
✔️
اورونوف و سرگیف هیچ مشکلی با تارتار ندارن/برنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139042" target="_blank">📅 17:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❤️
📊
نقل و انتقالات کامل پرسپولیس در فصل جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139041" target="_blank">📅 15:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
آقا کریم باقری به عنوان بزرگتر تیم این روزها خیلی حواسش به دانیال ایری هست و کلی با این بازیکن صحبت کرده تا روحیه اش رو برگردونه و داره کمکش میکنه تا اون اشتباه مقابل تراکتور رو فراموش کنه و بجنگه برای جبران اون اتفاق
🎙
امثال آقا کریم برای پرسپولیس نعمت…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139040" target="_blank">📅 15:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
❌
مصدومیت اوستن اورونوف جدی نیست و جای نگرانی وجود نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139039" target="_blank">📅 15:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIpPF1yROb_H-Fbj5W9GY38zyJxBDgr5xUXmk4_0Lydwmh3Y9GD48rc8AWaR2ayRfj3H1oK8_Y07JzOGoLDu9AlsM65BbrqDYfEcDmVq1YlFB6KBPjr8BCDvk5PF6JRBsoTzTRC3oBAkMLezlehJe4xu3vV2MQQhDmiweZmWQ7sCoiGC-r6DpzQduBue47TdqAhPm_PXoHy0EmJ8AQEUdqQOWhH2CBRYEAGPj0lRwJ0L-J7zt8ouJ7OrhUT_Ni1_iLB-whpIeEGLZqY6gXeVzTAiCEYq9B20yaIPnJZSG9tRSFnUI4s2V_mJ70zmDskgpdqiuj7PF_WXBVLaFN9kvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139038" target="_blank">📅 15:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP4j2CSAHQrAjJVMx6-KaU2WeG2hVZRgu4BEV40vpTnJ0SXpvEi9QN6POKOULCbGXIs57C_TCworqtFon46Z6s1GYBfL9Ju16z93li_nYhucSuAfzJBMW7NfR81BcKbCu6iF1IaFim1AuNaZs01aq9WvnULAeMxguGf047BRD095H96EY68XjaFNsZMPVJSIFi1iGwfEJ6you3CqeqLp27t2gysNpR99pj7WIUfIp2rxpBDWt3awetKhaxkfunI27jogkEOVhpY7azNMWSIX4uLanlhzsXRFDmmWHhAmhIN4F3tdKJN47IWaEcFfDzQqmQBVIFcEFKAhpKNuLfV3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
دو گزینه اصلی قضاوت در دربی 107
💢
کوپال ناظمی و موعود بنیادی‌فر، دو گزینه نهایی کمیته داوران برای قضاوت در دربی تهران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139037" target="_blank">📅 15:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139036">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
ویلای علی کریمی توسط قوه قضاییه مصادره شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139036" target="_blank">📅 14:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
✔️
مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139035" target="_blank">📅 14:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouDijEOY2GbAwlLKnnRDWFxVGr5x85v7piKdxp_fgJSBN3jXi98vpWcTc4bLsdKEQT_bhfmdkA8QWTpJTpF2GfJkx01Pc3GrekllQ2uFw3Ez0_unsHLFEH5x7uZNMuiNlDoBaa-uYD3tUTNBWwXw7KVD_D6zAk0KLiHle47dNva4s0uXA-ya2bURDhtA0DD_wLc2bI7tzxvTX3Hb97eo0J2A9lOq03xd2HDBCK7gHdRApTLWH0Rfl7NzKMbXOvMkUhFkZxSKYK1TPvc_EwtqiB58EAzVJfFHZzXYDqEsjVlf4vKqGboiX2HMdD_0ltuTBKKSqOWLrQsSXvuPFXotSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب در نیو‌کمپ؛ زورآزمایی آبی‌واناری‌ها با شیرهای باسک، بارسا به‌دنبال ادامه شروع قدرتمند، بیلبائو به‌دنبال شگفتی بزرگ مقابل کاتالان‌‌ها
[
بارسلونا
🔵
🆚
🔴
اتلتیک‌بیلبائو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139034" target="_blank">📅 14:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-5GflVZlGsNwMwP2gfnAHKeC0w7Ft3bsEzVZo42XtYhMzlVZ-7HGCrgMXMV1IxI0z5XcEjSduWFf2QpUeG-BJj_j7Kw0Sx9RNj7K6cQQPqX0p2WVOjSWbJPnIoZa2uehZnD2SBsiBh-_p0myczV93FG8QezXpWdc61eAmWXcwIhLAXIx0AGA8OMkoWIJ10H6yTh27cAGX-k4U2cB8y3D-l3le5YeioRjsW_5wHXHH71ohEMfMJEroqG44vrlvYPRABcgicdGFPGvifcUvVsfPg66AhFE-9REPAXBsUE_GiNcJAKmXuZ6cKWZk3J3OzoSUh1OQXKFm0snCbdtiB09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه پرسپولیس درآمد خود در مردادماه را ۴۶ میلیارد و ۴۰۰ میلیون تومان اعلام کرد که با احتساب این رقم، مجموع درآمدهای این باشگاه تا پایان مردادماه به ۸۴۱ میلیارد تومان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139033" target="_blank">📅 13:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
بلیت فروشی بازی پرسپولیس و ملوان شروع شد
http://footballeticket.ir
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139032" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139031">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
❗️
با اعلام ترانسفر مارکت؛ سروش رفیعی ، سرژ اوریه و ابوالفضل بابایی از پرسپولیس جدا شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139031" target="_blank">📅 11:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139030">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
فوری؛ فوتبالی: علیرضا بیرانوند هیچ راهی برای دور زدن سربازیش نداره و اگه تا آخر امشب با تراکتور فسخ نکنه نمیتونه در یک تیم لیگ برتری « ملوان، فجر» بازی کنه و باید بره لیگ یک و در نیروی زمینی بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139030" target="_blank">📅 11:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139029">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
یعقوب براجعه به صورت قرضی و با بند خرید ۵۰۰ هزار دلاری به نساجی پیوست
❌
امیرحسین طاهری به صورت قرضی به شمس اذر قزوین پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/139029" target="_blank">📅 09:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139028">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
وحید فاضلی:
❌
❌
متاسفانه ترکیب اولیه تیم مشکل داشت چون عمری مصدومیت داشت و نتونستیم از اول بزاریم تو زمین و تیکدری تاحالا دفاع چپ بازی نکرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/139028" target="_blank">📅 09:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139027">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
صبحی که هفته دیگه این موقع داریم درباره برد و باخت دربی حرف می‌زنیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139027" target="_blank">📅 09:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139026">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
📌
ورود سریع | مسیر ساده | دسترسی مستقیم
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/139026" target="_blank">📅 01:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhBuC3eDScgovcmAIZWDOeA9L-AjUba5jbZcDgtd6ct1AQezk7ZsUph3H81w2Szm9Oxa7Jn1MhjjeUktIjbDYhH1CyX_zniu2L0MQnH31JLsC6pFdI0_PM7mHRlYCv_7_gVYsKBq9DPmxHPxYZelsRkguE3Iky2nazqtSrlb5XC9VbkInDxyo1ajnIFWjzT284tqDw_buidPgMcDwxUrCDt2tM3yCIYW2-73KoI2uQCHIMwq3VRn1xgjGSUXd3rRBZIXS4ix7Hm_JUi6yTiw-E0t_DaAKRZqjaK0asEXWHaCfPaqZ-BQ2n7csZZslLAnhbcwqyMMJEvJn4hGRZa-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
عدنان کوستوویچ
فصل گذشته دستیار تارتار بود و این رزومه ایشونه، آقا مهدی چون توهم توطئه داشتن ایشونو گذاشته بودن کنز بچینه سر تمرین و اجازه نمیدادن تو مسائل فنی ورود بکنه
و به همین خاطر عدنان نیم فصل رفت ذوب آهن؛فقط خاستم بگم انشالله که خیره
👀
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/139025" target="_blank">📅 00:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW8_RVRIVZBlnP5ugayw5HXyqF1fVKKOnVGhZgUTqRJvdc7xFhcDzBR_nYVRfZBr1-qXBy3vhEaCUc2YgkASo11Ong2HYD-C2R15uXXFSGmYXwQiJm8bsqxCif7o1xyrThVTBxznv6U8QbL5G_kRR46grtwjGEnCElRhryGnSPeKOBufN_6mFKBkQrNMyM3Kmaz2lJYjMdDdyOSQQI9hNoossDzd4LFMwvY2P11dXg9ehCCO10NUuUKBAg2DdcpYAxkQd4LxYM3pFUHYFHB2ak5ALVXhMezntsMPswNvrRwXt64_eDqGR_-W4a7qyvOGG35LvWZQlWQ4cK2zPC-BFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📊
نقل و انتقالات کامل پرسپولیس در فصل جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/139023" target="_blank">📅 00:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🇹🇷
در هفته اول لیگ ترکیه، فنرباغچه با هدایت اسماعیل کارتال در برابر گنچلربیرلیغی با نتیجه 2 بر 1 شکست خورد !
❌
فقط باید اسی کارتال باشی با اون همه ستاره هفته اول ببازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139022" target="_blank">📅 00:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
پرسپولیس امکان جذب بازیکن خارجی ندارد چون ۵ خارجی دارد و  طبق قوانین جدید به شرطی می توانست خارجی جذب کند که با دو خارجی فسخ کتد.گرا و بیفوما هم مازاد بودند که با هیچ کدام شان توافق نشد و هر دو ماندنی شدند
❌
❌
در پست دفاع چپ که دغدغه اصلی تارتار است و هافبک…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139021" target="_blank">📅 00:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
پنجره نقل‌وانتقالات فوتبال ایران بسته شد
❌
پنجره نقل‌وانتقالات فوتبال ایران در ساعت 23:59 چهارشنبه 4 شهریور بسته شد و باشگاه‌ها دیگر امکان ثبت قرارداد با بازیکنان تحت قرارداد را در این پنجره نخواهند داشت.از این پس، تنها بازیکنان آزاد در صورت داشتن شرایط…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139020" target="_blank">📅 00:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAbZyJv23geWHwy5aZVEugnxTjBkLBjAhI5X9vpXzDkcHolsBrOVM3bLvNvpb1CiaB_EpzexB8MSsj8x6f1h812K3QfWJ4XzHQsoGwpL3-SIepDgKWD3cFPNY2kveOknMEIkDr37ScNtWnZFunQmP-uTtBXRaOHstH04GwvoXHJznmt8yGssNK5etvMb24p9TUdwZdOByZqfNnSmAfnMtVvvaX-1XT4DYo0AU_Zw13I0CRgshfrAPSTd22mSv1F-xbbGGWZmQ4UPAz-Aa4JklnjQhTYFhqD2jcdKQrN4ikoMrqgRxyjvQbNqx6C3ACOle5_Fzl9fxEvGE-Xd1J-Pgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🤩
استوری حدادی، مدیرعامل پرسپولیس برای حمایت از ایری و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139019" target="_blank">📅 00:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp-l_9HP7MpD5NEvvwN8-Zxzp6N1NKpurIdOoNlnDXRw7B5i-2PnwlexY8Ny_bcYZWOz57figdb0HKgay4LMivQxxApC_o3x56rAw5ONrK2_NsYHhCHh0dy3HjYKES67nqQ1zEqFyngQyQkHSa1AxQUHiKg2WQTBBL72AjfJj8XrFRcE2ZH1w6_0LQGWacuAFnnxGpz1lB1PgbypKRxUpAqgjJr_M0IFGf1E3O7aH-HUs5CT48TtX69uTA0j_CIEszB57ljr9-piw5-0UbCvQ6dLuy0NVNYkhOtJd4pW4-ebb3ayXPnBLgYhIxkUCq6hvPhgZM75NwnJu9i08JLEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پنجره نقل‌وانتقالات فوتبال ایران بسته شد
❌
پنجره نقل‌وانتقالات فوتبال ایران در ساعت 23:59 چهارشنبه 4 شهریور بسته شد و باشگاه‌ها دیگر امکان ثبت قرارداد با بازیکنان تحت قرارداد را در این پنجره نخواهند داشت.از این پس، تنها بازیکنان آزاد در صورت داشتن شرایط قانونی می‌توانند با تیم‌ها قرارداد امضا کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139018" target="_blank">📅 00:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
پرسپولیس از جذب ابوذر صفرزاده انصراف داد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139017" target="_blank">📅 23:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
محمد نوری چه فازی گرفته و صحبت های جالبی می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/139016" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‼️
وقتی میگیم پشت بازیکن جوان تیم باشید کفتارها در کمین هستند واسه این چیزا
✔️
✔️
سایت فوتبالی و چیا فوادی توی ۲۴ ساعت اخیر پنج تا پست پشت هم علیه دانیال ایری با کلید واژه مدافع ۱۰۰۰ میلیاردی کار کردن تا کمر بازیکن جوان پرسپولیس بشکنند
✔️
✔️
دشمنی این بیشرفا…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/139013" target="_blank">📅 23:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
🔴
تصاویری از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
❌
ویدیو عمق فاجعه رو به خوبی نشون میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/139012" target="_blank">📅 21:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139011">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
گرشاسبی، مدیرعامل فولاد: رامین رضاییان به فولاد علاقمند بود و در اتفاقی جالب به فولاد برگشت. قرارداد او هم زیر ۱۰۰ میلیارد تومان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/139011" target="_blank">📅 21:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139010">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی پرسپولیس به پایان رسید و این تیم دیگر بازیکنی جذب نخواهد کرد ...
📰
مهدی طاهرخانی خبرنگار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/139010" target="_blank">📅 21:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139009">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/bd751b7046.mp4?token=ZAceNfHF7tkGci-PP1_lqWOdf2x6XNqS2hT8a4lNOEfzGLA1bI5XCQPr9WFXMKZW0Byq2iILrmA0um_vykxiZGQ8daeseuJHgOFPRt2um4ygfw9iePh369zT2wmXBODsrPx9MjhBEO1ynfWak5c3vAc9Yuyobwz-NIhdWhAb8OEE_N3qc2DlS4k1cfSuKMXUOhNYhjjytVIprVFrkYZyzAhPJqpHCgaafYqWsQiEBw6q8Bp2OpQ6gwpGJ9AbvQlfT19c4cBCfs_w9wsWElDsdJszdskkrzIW4NbE07953ezr1UaZXKQopUz2MuI7PJHsO30f4jrtIph24Z8-5YiJ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/bd751b7046.mp4?token=ZAceNfHF7tkGci-PP1_lqWOdf2x6XNqS2hT8a4lNOEfzGLA1bI5XCQPr9WFXMKZW0Byq2iILrmA0um_vykxiZGQ8daeseuJHgOFPRt2um4ygfw9iePh369zT2wmXBODsrPx9MjhBEO1ynfWak5c3vAc9Yuyobwz-NIhdWhAb8OEE_N3qc2DlS4k1cfSuKMXUOhNYhjjytVIprVFrkYZyzAhPJqpHCgaafYqWsQiEBw6q8Bp2OpQ6gwpGJ9AbvQlfT19c4cBCfs_w9wsWElDsdJszdskkrzIW4NbE07953ezr1UaZXKQopUz2MuI7PJHsO30f4jrtIph24Z8-5YiJ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇲🇾
شهاب زاهدی تو بازی امشب جوهور دارالتعظیم تو لیگ مالزی برای تیم‌ش ۴ گل زد و در آخر ۹-۰ برنده شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/139009" target="_blank">📅 21:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139008">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=CJ6gnXEFbKQwjy_46PZMiMtKNc8u9Dml5eb-8dl3OWhWqSJdnPlJHetS-l8q0C5oW2EfAsT1z96ePbJJ0qorVCGeTZtRaNAztTUBdr__Z6PcQGxuTO8lVNFlQfexjQBxH31rGRiQiHZzvxkzHA9gzchFLD65BIu_biVeQOaNmHMF1s05JBvc4E_LabYXzk1f7hinWMtUszIggR0cBoiUg7Vks3M0KKtIYHfi0ZF_Qe3K-bcK3Xe1omwk7hCLdkrgI92iDlFwG0jvpDgSYk_wBjilp_jDNbK9Xyse7cxbjVdVXdDhj9kMjtoqYk8eGZ337kKOsuQUy03sPZ3GcnytSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98b3d3c67.mp4?token=CJ6gnXEFbKQwjy_46PZMiMtKNc8u9Dml5eb-8dl3OWhWqSJdnPlJHetS-l8q0C5oW2EfAsT1z96ePbJJ0qorVCGeTZtRaNAztTUBdr__Z6PcQGxuTO8lVNFlQfexjQBxH31rGRiQiHZzvxkzHA9gzchFLD65BIu_biVeQOaNmHMF1s05JBvc4E_LabYXzk1f7hinWMtUszIggR0cBoiUg7Vks3M0KKtIYHfi0ZF_Qe3K-bcK3Xe1omwk7hCLdkrgI92iDlFwG0jvpDgSYk_wBjilp_jDNbK9Xyse7cxbjVdVXdDhj9kMjtoqYk8eGZ337kKOsuQUy03sPZ3GcnytSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/139008" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139007">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
اسپورت عراق: یحیی گل محمدی به شدت به جذب محمدرضا سلیمانی که 18 ماه بود بازی نکرده بود علاقه‌مند و تاکید داشت بود و الان این بازیکن به علت عملکرد به شدت ضعیف‌ای چه از خودش نشون داده سران دهوک عراق میخوان در لیست خروج بزارنش ولی باید تمام قراردادش رو پرداخت…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139007" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139006">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=RhdE4d1xBSVnnYxY0dauduaHSBDjiRWAjM2Z3Vnf7Ksvfq3-4wxcwWp0AxnpwB1gpeAuzRnfFwGBu-SgjoQ6Znlg3jevwPHyetsdbr9PgRtB2a2IJ0TqYhR2SLyh-zm3l9dTZiyRf2jI7OzHeHV7CS0XNVnfSxj35rgllRYEMzazkFglB5ttuh54juUwKll1rljPo7SIYpbLUSs7612gRm5JLuGF737ASd7s4qvfknzoDF5Kb0rlqKY2ZQdVMEu51k1coTfGF44uyIejMpvU13INrGToS9oat479yHg0gpRf28zgloHNyk1KwpMsT2wOs-yknL8r8xG0DwBFZmuTOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a657a5ef3.mp4?token=RhdE4d1xBSVnnYxY0dauduaHSBDjiRWAjM2Z3Vnf7Ksvfq3-4wxcwWp0AxnpwB1gpeAuzRnfFwGBu-SgjoQ6Znlg3jevwPHyetsdbr9PgRtB2a2IJ0TqYhR2SLyh-zm3l9dTZiyRf2jI7OzHeHV7CS0XNVnfSxj35rgllRYEMzazkFglB5ttuh54juUwKll1rljPo7SIYpbLUSs7612gRm5JLuGF737ASd7s4qvfknzoDF5Kb0rlqKY2ZQdVMEu51k1coTfGF44uyIejMpvU13INrGToS9oat479yHg0gpRf28zgloHNyk1KwpMsT2wOs-yknL8r8xG0DwBFZmuTOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
شهردار تهران: قصد داریم 3 ورزشگاه 40 تا 100 هزار نفری در تهران احداث کنیم که شامل همۀ ورزش‌ها باشد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139006" target="_blank">📅 21:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139005">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139005" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139004">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#توجه
👎
❤️
دوستان تو این پنجره هیچ خرید جدیدی نداریم، به اسامی‌که دارن لینک میشن هیچ توجهی نکنید باشگاه الکی لیست رو با بازیکن های معمولی پر نمیکنه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139004" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139003">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود  ببین جیشده صدا چراغی هم در اومده چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139003" target="_blank">📅 20:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139000">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSaeid</strong></div>
<div class="tg-text">روز اولی که میخاستن این ترسو رو بکنن مربی همین چراغی مخالف بود
ببین جیشده صدا چراغی هم در اومده
چراغی جان نمیشه با این اقای دکتر حدادی  صحبت کنی این تارتار بخدا لایق دستیاری هم نیست  دیوونم کرده با این رفتارهای مسخره اش</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139000" target="_blank">📅 20:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138999">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب…</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138999" target="_blank">📅 20:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138998">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
🔴
باشگاه یک ماه در تلاش بود تارتار رو راضی بکنه به کادرفنی دستیار خارجی اضافه بشه اما هر بار تارتار مخالفت میکرد و بهانه تراشی میکرد، امروز دیگه به همه ثابت شد باید کادر فنی تیم تقویت بشه.
‼️
👤
آقای تارتار کلا بلد نیست با خارجی ها ارتباط بگیره و همینم موجب بروز مسائل حاشیه ای میشه، ایشون کلا توهم توطئه داره تو هر تیمی که بوده…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138998" target="_blank">📅 20:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138997">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
فووووووووووووری از آنا
🚨
مدیران باشگاه پرسپولیس از جذب ابوذر صفرزاده انصراف دادند و خبر مذاکرات مجدد با این بازیکن رو رد کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/138997" target="_blank">📅 20:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138996">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138996" target="_blank">📅 20:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138995">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
فوری و مهم
🗣
🗣
سازمان نظام وظیفه اعلام کرد قانون معافیت بازیکنان تا نیم‌فصل لغو شده است. بر اساس این تصمیم، علیرضا بیرانوند تنها تا ساعت ۲۴ امشب فرصت دارد قرارداد خود را فسخ کند؛ در غیر این صورت، او باید برای گذراندن دوران خدمت سربازی به تیم نیروی زمینی…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138995" target="_blank">📅 20:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
تلاش بیرانوند برای تعویق سربازی تا بهمن
🔹
علیرضا بیرانوند در تلاش است با استناد به مهلت قانونی یک‌ساله پس از فارغ‌التحصیلی مقطع کارشناسی ارشد، خدمت سربازی خود را تا بهمن‌ماه ۱۴۰۵ به تعویق بیندازد تا بتواند تا زمان برگزاری جام ملت‌های آسیا ۲۰۲۷ در تیم تراکتور…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138994" target="_blank">📅 20:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی پرسپولیس به پایان رسید و این تیم دیگر بازیکنی جذب نخواهد کرد ...
📰
مهدی طاهرخانی خبرنگار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138993" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/138992" target="_blank">📅 20:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YErDcaXUGpV9oejGQmxeWupCd7bPGjbonPNhoutaqRCmVTQyODHZGwUCxvy_274j98XROGNpfZ7bvdnezknptZqPS6AO8eWni3r5uGnj6YGGK5zBPOpzvZW-5fyx9DgSjXKNk4RGcOk2UvvGM4YGNBM9uJCWh6RW-Mk0bDCrgwB_UzSrTofxJNSqbW4Q11uTXnr8IfTXJWN3p72OqVqG46PIz4XUYbHjXyw2rpYeUo35V1K63pr-T_weMwWdbc2lSq6ImvbYLFaai6M9w6-KVjDALGjl9o9GbvMCEqH4CbkhurNgEd_Bl6dWS4TpIx1a2XDINIdbUgHR7oHWcYO8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لیون و فنرباغچه؛ جدال برای یک‌قدم بزرگ
دوتیم، یک شب حساس و پر از هیجان
کدوم تیم امشب صعود خواهد کرد؟
[
لیون
⚽️
🆚
⚽️
فنرباغچه
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138991" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138990">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138990" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138989">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138989" target="_blank">📅 16:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138988">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
جلسه مدیرعامل و سرمربی پرسپولیس برگزار شد
✔️
✔️
جلسه پیمان حدادی، مدیرعامل باشگاه پرسپولیس، با مهدی تارتار، سرمربی تیم، برگزار شد و در جریان آن آخرین شرایط تیم و همچنین برنامه‌های پیش‌رو مورد بحث و بررسی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138988" target="_blank">📅 16:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138987">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💢
💢
💢
طبق پیگیری ها، جلسه مدیران باشگاه پرسپولیس و مدیران باشگاه خیبر از دقایقی پیش آغاز شده است و تا ساعات دیگر احتمالا قرارداد صفرزاده با پرسپولیس امضا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138987" target="_blank">📅 16:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138986">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138986" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138985">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138985" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138984">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138984" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138983">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
ایجنت دنیل گرا:
✔️
«دنیل به قراردادش با پرسپولیس پایبند است و بعد از پشت سر گذاشتن مصدومیت، با تمام توان برمی‌گردد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/138983" target="_blank">📅 16:09 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
