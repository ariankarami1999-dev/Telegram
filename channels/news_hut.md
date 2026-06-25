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
<img src="https://cdn4.telesco.pe/file/AE87toM8i7I9Ik1m3PaE6sNXKVe3IRgfBmbi12Bb4NiikBVO8P3-lUz3eKg4XT15Ou3140QyTohdD_np1ZuiaGpf5-ljR30M9-N-nPwN2Pjlmb42z3JogbkAM8cvdQLziDvBZmim1rYzk5umJp4UQZJtmwWQ2M0pdxQLEdOD7mgojhHtKTyde_zUXWeeGRkIYjBCcsTfwODpJkk0Z3a4T5-sUVRegbcSKF9Z2RG0G7IcBp3YH4voAytJO8Vjjmc6_6ynvy6VXyEuusMso3AjmKOKWZBywJXFLUojiU0ngNNUI3sCHghz5U4Xu0tFmk9tbyxHCMoXRPyZDGim97q_2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 21:39:50</div>
<hr>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm2dEeQh4y_skKjM6wcngDG1C3Sx3amBxupjkJggt70mQz3C87wPfFs2uBumnrMEGbRuvXSoN7l_wKJ1PU41F58xvHafyb0PYsPGQPcD1RFcWZBfCOXRw6vRMd8vElH5wVAwVu6ZXHQx32_ALO7IDQEnqDSC2oaX5l7YwgFbBLKhDkOis7vq34m75r-OirT2OXXG_KqQdXTPzRPNiMAkpOKl-U9PR5nWMaXwoCGH2yCsRXslap9HAqDxlFw7Tuv5UEML0MIm1GV18hpgkVRLDmP3Hl1sNCKPe-gYXLMU3y9VBcxKw9skFnOMhX6pf75rbqwn0Lg7ZasgrBYON-WtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0J4m7ZtyuWxj8PMAdFOSR21Y1e--yjrgtV_VEOMLZ6qxTxYN5MlqAzXoOnbZrtySATY2ekmgbquDGE31pz64zZQ1xH2G-jqptmLaQiQN3PPygLUQok7LD3YcywAtGpw7KYsosoE4CPpu_CCnwtFpWB8AW0Q5WrON4eUlXwCjz-rHdOPI3j5S8F9c3vKESup1wQLxZycCgszD0ACYlB3fmTtAxspMTmYHNZg6Ak52evG6xW9K6XJzN3yl5b_h1uoTqJh4yaukfFNswRKvKcV50dATNvUraOAZ-HCIky6p_MojGgF3EOP2NYtzT300yIqW7se2FYyspVnkjTNFONvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwJmv_LX_PH9Wt5x7I4FtLznHpbeW0mQpU8A-Thzfpwvl4keth9dMp2KGYVg7bffiry4hc_2jKo87G1vCOKts-TOKaa9GoO0VKgpZUUkPDvNB48DTmlcmDuyvtUpGBFhW4shZvkgR0rfaxjQ3V6c9R8P0elnphSLiCKXc3I0xI40JwnUxuOqfmiWRft5g7V0hxEIFdjHEHuwVzrSRyJmaJur8dlKRQxTFoooPWf1dK_PlCpt095GH2N0zHZC_EwvQo8FlFyQsRkbEr8z8cvgsaSJqGz4xshfMIfm2y1wHVG0O0Xro-D8OocGd7pChNWDuwfJLwAQvMwi4V9ZsvCYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44UMwe8q28-Q-74uWtaP9m5w__GCj3Ww9kHgjiIC3AkfJ7CyxAl4HIRuAnEcRiRUBug1HDGlLLeCzlUlk6AV-PS595ZR-GZWDKzN-NjXwBVl_d4OUO4nDg-2VB2b4324kI0Z9MJpUH_6anTjhEoJMsqJEYIAsPpIZ1Za2jeYih8tJ1DkK5xjpLEV0ZMC1VTfXz_YYU7fDK_YD8f718NDWN3-muN4ZZ3xdXto2fcdiC8LFVkqz_nboxKeX24dp5MowKHIm7mgyzRL9PgFrXFm7Wg4igr7zhjwRNfReqQBUyOS7hFlvO5owzjlkoNxr_BCxfuMDumMlU8imPW6F9F7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9aANO2Rp94H8_pHpOZD1OWzEquun0J1w1KPfUkLywkaOM2ad9Z5BfC-rHcLCwc8kgvNMSGESoraTu6vIyTNZ3uteyA-POYR5EbghfQtD_k1VpgK-AeIngy9U12aRAJzdodlpMSLr7pYdVsLQ9aru9E7CwcIPYtEDawqoFbTNjEMBZJTUU_l_2XjReMGnI6RAmJMHqxpACdwbVdoZObedPN2ypUzV4A0Rq3PLv97ULb3ixi8S4qkE2Z0Yyz2ZfuUiue7Q-bXX1p2Ohb-62gw6JZHF4Rv-C3uqnLiBksZxJiq1kYcuO_g82RHW_Cp7R1v_eRNNXdCbYFqnlGgPZWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ6praqAha_MBkP65yUkrEm0NDEHf-w-hwTOqXynpVQWId-ECFXV0LLaYegWfNVSHUDWkxJRYEHj7N8gFukJ4u2MBFOYhko2b0UZMQaqZi2YlWkjP4vG0ctFbIubsWBHZwX70UglUX-kibrLuh_QK42Q729HP4vKsrrbkRrUpxEa3AcpcJFH4SMxVIKs8LmtgzIcqnrydAlFxL4l5UjqakNWUVdniOYUxdrPlvnruESood_klGSO3Lfw6QnocfOiKQiGsNdLLvfGGfbrMcCp8vW2UAYS-tBp9dh9bYq56pukMeYmeG1HmtRZgDsC3zAdENd1sHjT6nzbWXmQ0N_Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K30xs3ZTn23nz0dITGwVfHrF8RqJPQiEmvRPou8SMslr9ukPTeWUpsAWuq0_k8VnMdm6PN1E5Hy6LKvy8pORRi2IJIJiqqHDvT9gFWIALQRl4UARH8n4k3KrDsVtF9TdQLyv01QDnZUUNQAyPEm5fNX4BE6jA7TD0BxoQLgHIIpFQ87UfK4_BfkC8lcFpByV7lcWbd5CVMlQOFa0QC25bp2QNGLqFUfx8IK81PfBpS5m-XNWzQoTH2RHAatVAWVQR2gSlzcegOuukbJmVV7zdGfb9dHNcinjfpDO8s2-A8O5P7H7rJ6aF-Hrh3PHQaVnvbhwwUaNTLqvTWrjWhV_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksv8ucyY7cqxMjW4uDN_eW4l5Ng2YImpSqJPuco_l-hounYGsZ9uYNfKDxL9tlnFzxuRdv85by9rU8EKvUeMiW7cNxzGYR9GBjHC9IyKnxNdelw6WZpATnRmERm-Tl6KRYIKXaFw6eyIxoqmsM37z9YADNNToxla5R_bWunTMih_lqAyDHZaTbbhlLigKL0dxmilXRlynzKeTmroAu-h3KKBpgwbVNaaASrObFXQYF597c2pUd0_uAIjQS0RGUsliCOc2kfHgjKVHs4SHf3PJcXKEa7A_pdmmdGFQVV1chSuaJgfAdFiqtiFutz852K-EoImEEJcRcizv7fTtwLOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=h6kBrE2L0a0hiRzYQ08GjuWOZbuSthoZNvQFarnXcucW41VNZkfuWI2JnOIh01E2CkszgvV68DFUKmYFBEIr3eUbQpzn2yIgwrIfPHn4_dAo2n-FUZZmZsYsRw8QOwti3hNl-_5Hr-VMLDHMI7ZZYwR5o9lQNE4eV2dz60ehistFuaILsmuyouqsmhIaslprF1LcibclgimNz-w0XtG1fOQBNcno4Ugx1aY2znu0xW52ld3hVvN60PHoxWPQm1Aia59kP9wAy8iEY-fZVTYFGFHs78O3s4DDWHToWBaVwtFuxf619-WQjzo82lziMpILdLRGlkMqCtIlkkFIjb3osg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=h6kBrE2L0a0hiRzYQ08GjuWOZbuSthoZNvQFarnXcucW41VNZkfuWI2JnOIh01E2CkszgvV68DFUKmYFBEIr3eUbQpzn2yIgwrIfPHn4_dAo2n-FUZZmZsYsRw8QOwti3hNl-_5Hr-VMLDHMI7ZZYwR5o9lQNE4eV2dz60ehistFuaILsmuyouqsmhIaslprF1LcibclgimNz-w0XtG1fOQBNcno4Ugx1aY2znu0xW52ld3hVvN60PHoxWPQm1Aia59kP9wAy8iEY-fZVTYFGFHs78O3s4DDWHToWBaVwtFuxf619-WQjzo82lziMpILdLRGlkMqCtIlkkFIjb3osg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf31zo14BBvwkajbYQN3K8aEdrJtVCCzCtlJbNdi2fkpbSqIpQ8S6OCh_wNk3W9cvc8hI460kISIw6ric-2sUy-CymZrnAjWx7ZtDzlFI0x6ll--XmX9i1zDqJq9Ftd1UoTttKnPkUUofTWw-vP6-SWivlRMKQAxN1TO-HNZw91-5sazyXpU5vhtwqnmPhS3yvBl82UFqdooVxcdWML1dhGJr6JJmpQCtN_5teifNEDvBw-968_K3UtH9py70sXGodIwqNA2Z0My5OZbIeKExD6wLpk8evFgTVx_NCWidyiw433ylR5ntz9--b8i8U9JRvEyQj1xMCpkjzSviMsiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=j27jQj7IoWaCZsFT-k7a0yAjvCjm6aQQCLJMUK7Bf7kZbhfgydPXJw6iUcozMIjzue_PSsA1d2rl6LHJ1QXFh-SEs-avJwcaszOnmMn0FxBSiALtrdkH7f4D6XuZ4wQb7PhEJoJTF3gm0SRB9OmF2dtnZpQmjjvZ703cb5FTyXCcFYKzhJArN1EjXK2ZWxg22I69c8id6VpQ84O1fNqPKxvZ9NVEJl89H6EP4dbtTa0jw8rTsXjfFKEyDIF8OGSkzgM3p6NNL72iHAog76BQWWOujVEG0CVs-ECWYT8RToln6n0fQn0iZnl24-6kM_LI_Nd0jN5foLTaMkdWpLpIIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=j27jQj7IoWaCZsFT-k7a0yAjvCjm6aQQCLJMUK7Bf7kZbhfgydPXJw6iUcozMIjzue_PSsA1d2rl6LHJ1QXFh-SEs-avJwcaszOnmMn0FxBSiALtrdkH7f4D6XuZ4wQb7PhEJoJTF3gm0SRB9OmF2dtnZpQmjjvZ703cb5FTyXCcFYKzhJArN1EjXK2ZWxg22I69c8id6VpQ84O1fNqPKxvZ9NVEJl89H6EP4dbtTa0jw8rTsXjfFKEyDIF8OGSkzgM3p6NNL72iHAog76BQWWOujVEG0CVs-ECWYT8RToln6n0fQn0iZnl24-6kM_LI_Nd0jN5foLTaMkdWpLpIIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=cM-Dxb-AbwCkO1lFihNy30cR55QtNRiwNxLdp1VmRrtDQ2wYDE7FJpm4u7JPSLEzmciq1ImJQBlI3BrDS08_pQn7lzZs3PdoT1e5FNuG5vuUslV40it-Ovg-kUzMAXHvjljg2vupy-rYWXGMFvvwASOMzvvXvblY6JPzcz3IWM29jeOI4Dip2zTLMau4qHBIkG9aSzyRqVVW379_s0kn-T8I59yeUcW6s4bpsx16UmAK1XqAHNi-fRB5vdDpS8Qt-o84GVyGPoMvAwgi_aAbrqOzC7g6fvsbWwC9-4gjvoFljSa-qv0278cAxVV9clyFEdA3uAY38Jysh8og4Q8yFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=cM-Dxb-AbwCkO1lFihNy30cR55QtNRiwNxLdp1VmRrtDQ2wYDE7FJpm4u7JPSLEzmciq1ImJQBlI3BrDS08_pQn7lzZs3PdoT1e5FNuG5vuUslV40it-Ovg-kUzMAXHvjljg2vupy-rYWXGMFvvwASOMzvvXvblY6JPzcz3IWM29jeOI4Dip2zTLMau4qHBIkG9aSzyRqVVW379_s0kn-T8I59yeUcW6s4bpsx16UmAK1XqAHNi-fRB5vdDpS8Qt-o84GVyGPoMvAwgi_aAbrqOzC7g6fvsbWwC9-4gjvoFljSa-qv0278cAxVV9clyFEdA3uAY38Jysh8og4Q8yFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrmBlKEmCt_Thd9gG27F2ykuwU6DKJOvrLIJC_OVoYq_Fk2jmZZJCI5lVhJVxxNRUxxHZc1mcg8wvk8sRjA50V-GjOT1g1hDr31AReDUKwap4KIF9XBBjD4VWjhG28kFANqls2bo6_0TSmW3RHM0BujlId-aK1aW-s_KPkEugvw6qDngr2MM6dv6oxjacl0yNLkaoI9obbkWAvLAbCTl3y983BJQ3USOc7Otc1cq_dTt8fCmwMveGc2o21Yk5aTywRxhnLiCGiHeVJYmIuiJLOnjmGzqzUJgWOQSuJugHWU6_2DrmutQ9zaLt8NbAwQHPOYQ-JI9fpoHcqNCqh5epw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=WDquXOMtR5ohPIHqFNzIG2kCUD_LksUSWo5BCYemMqXVY4djXquPkAK-6DZESkpBuAsE_4J7MRnQzphjz6IclEtjBLDI7tjUWnT3n1zoZyXth8k_8xLRWvEv3x-1wxSSAVRoO3WkoPhE5_IJAXc3JpbC5heQWQsJlzQ_nbQl-rd_q1YYnHz0Iu2fZbmwwYk2rAvIbAjoMajuYMg0AxFaybkoqYe8OsDhPtTa0qcwnHP9XAHSokg09i4v7HpPKYpbEfIkVdlmiGLzL-OMuoTyneN4nSiMrVZumM32yFLGADeKSppcd72MDiXYbT9e22Z4A8osTjdyRQZlZW4ppI97Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=WDquXOMtR5ohPIHqFNzIG2kCUD_LksUSWo5BCYemMqXVY4djXquPkAK-6DZESkpBuAsE_4J7MRnQzphjz6IclEtjBLDI7tjUWnT3n1zoZyXth8k_8xLRWvEv3x-1wxSSAVRoO3WkoPhE5_IJAXc3JpbC5heQWQsJlzQ_nbQl-rd_q1YYnHz0Iu2fZbmwwYk2rAvIbAjoMajuYMg0AxFaybkoqYe8OsDhPtTa0qcwnHP9XAHSokg09i4v7HpPKYpbEfIkVdlmiGLzL-OMuoTyneN4nSiMrVZumM32yFLGADeKSppcd72MDiXYbT9e22Z4A8osTjdyRQZlZW4ppI97Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=swKbjdVdcnJ72ZVxh2bqQMh2lByVOntZmxQVf3shJGrgg5XNAsRUrH8RZ6-OVskcO8OFrU01Xe0tBM0bmevAskaaGrE1BJV_bsGIsbk1BJKu7tSk8UAC7teCEhZrAM5-JBOh__PzRJWk1v1dbu_9Yb3tlkrWipVck2RDkwoK_WlrRRYEMBb7OUkce8zIIFcqbpB16s3RPkxaowJ5DlaQXIz0uTpAru1tQ3WPUMfuts9QfXFSD5fshDLy37B9Jxkpke7CLkYovNdouTq3DrO9bAstdjeZsKZqII0uNhsQfF9LqjRBPbxQtOj66JcWttJwzyqnWNmZl_94m85sW12VEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=swKbjdVdcnJ72ZVxh2bqQMh2lByVOntZmxQVf3shJGrgg5XNAsRUrH8RZ6-OVskcO8OFrU01Xe0tBM0bmevAskaaGrE1BJV_bsGIsbk1BJKu7tSk8UAC7teCEhZrAM5-JBOh__PzRJWk1v1dbu_9Yb3tlkrWipVck2RDkwoK_WlrRRYEMBb7OUkce8zIIFcqbpB16s3RPkxaowJ5DlaQXIz0uTpAru1tQ3WPUMfuts9QfXFSD5fshDLy37B9Jxkpke7CLkYovNdouTq3DrO9bAstdjeZsKZqII0uNhsQfF9LqjRBPbxQtOj66JcWttJwzyqnWNmZl_94m85sW12VEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=rRPvn3xc6wB82i4Zk4u7fYLnn9H4_96xVbPrCvz7d7mCFTQAXk92VzZ5w-RFYaQWzyoZO11T04E-ZGFnbvNnObMoeizke_7YDzANSXQKT9kY0mTj2MrEU-vMaN6709D72-_snxCuour3r2eO_bscrMAhvBRjRZ_tbWoCZuLey8bcInQOqtcI6MdOyNeq5BGxdEoCV2ycK6ALLGVJmuvBM2AQ1N7GuuVaN0OhegDkwKsZotTskGZwMDZbpzsl-ESTOHtHLVY_LB5Fa0PJ67-Bsf1uqy2PuTGg0eegh-9igMDcHDBXyl2u7tgj0bR8uKBAVyNQwXZuDu3uEtjE-Er6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=rRPvn3xc6wB82i4Zk4u7fYLnn9H4_96xVbPrCvz7d7mCFTQAXk92VzZ5w-RFYaQWzyoZO11T04E-ZGFnbvNnObMoeizke_7YDzANSXQKT9kY0mTj2MrEU-vMaN6709D72-_snxCuour3r2eO_bscrMAhvBRjRZ_tbWoCZuLey8bcInQOqtcI6MdOyNeq5BGxdEoCV2ycK6ALLGVJmuvBM2AQ1N7GuuVaN0OhegDkwKsZotTskGZwMDZbpzsl-ESTOHtHLVY_LB5Fa0PJ67-Bsf1uqy2PuTGg0eegh-9igMDcHDBXyl2u7tgj0bR8uKBAVyNQwXZuDu3uEtjE-Er6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghjvTXGYa0udhTUWnpbumiX_jOPyUPSpygqivEBYb-aJox8tDKpqjmGNRgXGcAfkk6Ha0wQxdo0xaCmsnhv-nhlo92yAXJrSM5CeiUhTjRxVTKarH8VfrcrDCWz5KRqPl-NXjh8EB8vSZzIcHFA7_PX4bwPG366gQdRcZw2kKEd5uA3G7_a1GGcSdcZTIiWk-lyj4m-8NoXRCclYsPM5lExt-SLaA_U85LOHmJWMdIiaPrQvq2qAbClo1-tS3Gg2-0Tw38Xjzi08s2BGGHNktHqPnsv0sk818zv25ukKzdkA3JzCDNy9vbkyBQtUhPb963vItK5xXDG6E3N9uLelByVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghjvTXGYa0udhTUWnpbumiX_jOPyUPSpygqivEBYb-aJox8tDKpqjmGNRgXGcAfkk6Ha0wQxdo0xaCmsnhv-nhlo92yAXJrSM5CeiUhTjRxVTKarH8VfrcrDCWz5KRqPl-NXjh8EB8vSZzIcHFA7_PX4bwPG366gQdRcZw2kKEd5uA3G7_a1GGcSdcZTIiWk-lyj4m-8NoXRCclYsPM5lExt-SLaA_U85LOHmJWMdIiaPrQvq2qAbClo1-tS3Gg2-0Tw38Xjzi08s2BGGHNktHqPnsv0sk818zv25ukKzdkA3JzCDNy9vbkyBQtUhPb963vItK5xXDG6E3N9uLelByVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=nozRYLnHuOcJbGlM9pqKkVykjxPEt4ifIqMCmwL2t-1ePKeqFuRRxJGrzlJohXddWKwfihAf36lMG-auEu6uq9KI-uhCX7lBRCFxYzdX4BYcflKyhEai687IAwndOCxtgEUkw3NSUN4b_lIkm-OiPLJa29uo93EKQXI2oMMznZAWKI89Gmk1u2A25iO19-6eBEYapzi2rGz0Y9NA_xVdpNtZxbCu4f7w8dmaG5oyqGUq2e3_47EAuprFOhOCm_7RA4v2tHHZNLiyYmu6RNQ6ciSs1mt3PYLu7z5xfIoi8mEGJimBJTNEsA-rJgm67Q4t5ZH9JaAwUtPqgQ5Lfn6KYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=nozRYLnHuOcJbGlM9pqKkVykjxPEt4ifIqMCmwL2t-1ePKeqFuRRxJGrzlJohXddWKwfihAf36lMG-auEu6uq9KI-uhCX7lBRCFxYzdX4BYcflKyhEai687IAwndOCxtgEUkw3NSUN4b_lIkm-OiPLJa29uo93EKQXI2oMMznZAWKI89Gmk1u2A25iO19-6eBEYapzi2rGz0Y9NA_xVdpNtZxbCu4f7w8dmaG5oyqGUq2e3_47EAuprFOhOCm_7RA4v2tHHZNLiyYmu6RNQ6ciSs1mt3PYLu7z5xfIoi8mEGJimBJTNEsA-rJgm67Q4t5ZH9JaAwUtPqgQ5Lfn6KYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVaJLvGAl3DMspMR8Dw8wMCjDR2FZnhwZuJOE6rmyQpvOZOCWsOATv9th9ceKOYlCHWhBRNiYwcxQvDKxwfmeS8VfpYFhCiKAOk7xU7qHxGzxmVV20YXV8nqeSmr_2aEgtb86B4IRP5epFtTm3iYbZrbCkhiGVPQozRX2WtoLUhO62sJstTeoI1hbQ8ggMxcbbDTaK0yWbCSmNuyaJmCZOmcZfZF5UcaeFhNWapqlbHL_92MUWzPBI2JaI2HThn3n0ecjJRq93YP-2MR4jumqrcUIBB7bvllTxbk2Xw3SPyitd1KtUaf5qeuXeCICahUcyJOr_qTo4xaXEIwkQ68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QMhOgyKWln4KI01RyQ2wjKOMBAT5IYB9XpHirGgMlmDMdb1I1_0H9zpLhg0zDVqztafC99v8Umh0lq1A5aPCNMJuSwmPkIrGU8Wf1Q0fHNW8QbUW8QNSxxQ5dMXpoLS4sjWkwVW8h-Yu1GOALfRRmfrQGglqjXprEpQ6WpxRfnGlJxwAsxshvq8La712GPpA1KiDyKSyIZXkD-G5QSznZclHLV0MAB_NPUqmQ3eR24WcmuSvyyKkVZ4MIYjledHlRH5_gKWIiV2lTTYRSvzGQFBUUqhumM3jCEiAF6DXEvUYJT4yNx3hhZk1X_8l92xIu6Pm6Gu3uFtXfz_KOJsdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=XzXUhC-CB-N5q9zQuCk-KjtSzpqQ3Aq19r0jM3kvZF500n_gXuWOyu3X0QRBmhfHTxbaV_BwzDm1hvVUxtTbWWAYPrxdUoua1WPIDLqfXCtnQpypK3TUjjjFDTiAcdNXHJFJ8pw0roBALQJ4TehgPnUnGQUSQ_HS10nuxe4cSRlkCvKbcFwTVsaP7_J99Xh2njm0FzINr6nxxYds8Cg8EtAieETucUoMpVzSlTQJpVZpfE24egWOPO5zBDjb6MPmszQcGvTb64c5Uj2Bkg0DPKqvFXGSJyKRG_j87fxv7Z21tnNmNVvHUnopiQvxSC8nS5OPISrVG40REAgES2DvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=XzXUhC-CB-N5q9zQuCk-KjtSzpqQ3Aq19r0jM3kvZF500n_gXuWOyu3X0QRBmhfHTxbaV_BwzDm1hvVUxtTbWWAYPrxdUoua1WPIDLqfXCtnQpypK3TUjjjFDTiAcdNXHJFJ8pw0roBALQJ4TehgPnUnGQUSQ_HS10nuxe4cSRlkCvKbcFwTVsaP7_J99Xh2njm0FzINr6nxxYds8Cg8EtAieETucUoMpVzSlTQJpVZpfE24egWOPO5zBDjb6MPmszQcGvTb64c5Uj2Bkg0DPKqvFXGSJyKRG_j87fxv7Z21tnNmNVvHUnopiQvxSC8nS5OPISrVG40REAgES2DvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=Nj_y9CbwmRh9U3vyEsXn0FVXrJSOcdAxVdtQyusaoBJ-kRK4tNcoJmGvU3_sX9JMUki_46zegXVEu3sa8XB_4tKPHjWzP2cx1FbpS3Onu3Sn8gDkfzrVbJAghQwstZc3o2nP1ioDXWsLl9W516cxUq2aOzRFMKT2hYLj05Qb2l2ZFMts_ZX9m3a3BwlyoKtkIn6YMcbP_6W0_SL5RQrSLDZoc6RYsC5A09vgmFaiRVpzcP0wwc3miQ0sOG0lSUOMgJ45uCZ-RfNXrNNBS3cun_jVH_ab46Exn3nU_ma0KlKlC03ZlKiLdytbIaEWUDOr5fhp2Fixz5DSLGb7Xyf6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=Nj_y9CbwmRh9U3vyEsXn0FVXrJSOcdAxVdtQyusaoBJ-kRK4tNcoJmGvU3_sX9JMUki_46zegXVEu3sa8XB_4tKPHjWzP2cx1FbpS3Onu3Sn8gDkfzrVbJAghQwstZc3o2nP1ioDXWsLl9W516cxUq2aOzRFMKT2hYLj05Qb2l2ZFMts_ZX9m3a3BwlyoKtkIn6YMcbP_6W0_SL5RQrSLDZoc6RYsC5A09vgmFaiRVpzcP0wwc3miQ0sOG0lSUOMgJ45uCZ-RfNXrNNBS3cun_jVH_ab46Exn3nU_ma0KlKlC03ZlKiLdytbIaEWUDOr5fhp2Fixz5DSLGb7Xyf6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=oCZ8ZUSLe17PIWEcRi2u5jFhT19C64biWn4XzF0D8LJdl30zBTaT2xXf-MQ6x7y4sjVydfExvVxPjbEdkIM-dC2cgtU_tG0tI3PmUDGfCGqxNPbO9fqpAXOP15fY9-psZJUeg7MBE1qZNRaGrJvD6wUvr9GqSz3Lcki3o6WaFrLqT6Q3_yP3y4HW7IeAi9djmEMuWhAr3sOhgRecuNTcuTJRJnEea4UM5gHuHlEHAa6M3OMUK4rWN3njtwL8YAzWubaKlbkc9TCL3tEYSWl4JbKiq-FA0wHblYdx49yBAy9RWxeC-EMccxdhrKC7jl2Ia_WV9KCUaCuiM8TjjFS94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=oCZ8ZUSLe17PIWEcRi2u5jFhT19C64biWn4XzF0D8LJdl30zBTaT2xXf-MQ6x7y4sjVydfExvVxPjbEdkIM-dC2cgtU_tG0tI3PmUDGfCGqxNPbO9fqpAXOP15fY9-psZJUeg7MBE1qZNRaGrJvD6wUvr9GqSz3Lcki3o6WaFrLqT6Q3_yP3y4HW7IeAi9djmEMuWhAr3sOhgRecuNTcuTJRJnEea4UM5gHuHlEHAa6M3OMUK4rWN3njtwL8YAzWubaKlbkc9TCL3tEYSWl4JbKiq-FA0wHblYdx49yBAy9RWxeC-EMccxdhrKC7jl2Ia_WV9KCUaCuiM8TjjFS94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=gFglQ_kLT2nmqeMctaHBIYImgMcFJUeiAWPjcx4JUJ--Y4LXpA0gIiblroz0urcBUnsGqLz_skf9BqQGMieOXyGkufyEstOt81WyfXQpWf_gffzlU8Urvf80xJxe-SCwWq5fosLPkCu5lg87JvasespbbNOhyfv-MU7ayHFvTftxJSpusAtsHGzj7rquDXbGL5rbGBAZ33z4qJ5ZvPmCxeZY7VFClxYlKO3vGo625ophPLt7KyH37xCtVBL9cCAomMqprCeZPBlVlxcZUAdorjsZLi5JlF73TcQ_WOQsOdT48nxDl1crXMruhcG_QyNR6GSN2WLCwIlyhtUK29-mGYkuvTSCJYAhGTEHVYNtzJOw_2K_H-bK5SyBEyB1RiF20lQq3srwr1ARk4aO21KlvR0ZRxNPYUZBuM8hYXOCVINwYIqs_qbrDMxqzrMU_5S2Yw_NdqMBvSo0IbR6iwHytT1KltOZ-hgn4A98cDbsXZVqM_eLdjUepaT4bBCO2yKigrPi6UqYz6YfvJYbjVateOfz0myRSWFjgyaGeHeX0jn5pzxzyCfmyF0WiFVtJQMr2IBlOk0q-0KM4RpmKynK5i-ITFBPx67KwqjEXhvxgSrBKOCY58_8WmPONDDlo1pjJV4IbbYOSHNeL6fgmuEsZicyNjQgCFlyer-g2V_upog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=gFglQ_kLT2nmqeMctaHBIYImgMcFJUeiAWPjcx4JUJ--Y4LXpA0gIiblroz0urcBUnsGqLz_skf9BqQGMieOXyGkufyEstOt81WyfXQpWf_gffzlU8Urvf80xJxe-SCwWq5fosLPkCu5lg87JvasespbbNOhyfv-MU7ayHFvTftxJSpusAtsHGzj7rquDXbGL5rbGBAZ33z4qJ5ZvPmCxeZY7VFClxYlKO3vGo625ophPLt7KyH37xCtVBL9cCAomMqprCeZPBlVlxcZUAdorjsZLi5JlF73TcQ_WOQsOdT48nxDl1crXMruhcG_QyNR6GSN2WLCwIlyhtUK29-mGYkuvTSCJYAhGTEHVYNtzJOw_2K_H-bK5SyBEyB1RiF20lQq3srwr1ARk4aO21KlvR0ZRxNPYUZBuM8hYXOCVINwYIqs_qbrDMxqzrMU_5S2Yw_NdqMBvSo0IbR6iwHytT1KltOZ-hgn4A98cDbsXZVqM_eLdjUepaT4bBCO2yKigrPi6UqYz6YfvJYbjVateOfz0myRSWFjgyaGeHeX0jn5pzxzyCfmyF0WiFVtJQMr2IBlOk0q-0KM4RpmKynK5i-ITFBPx67KwqjEXhvxgSrBKOCY58_8WmPONDDlo1pjJV4IbbYOSHNeL6fgmuEsZicyNjQgCFlyer-g2V_upog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLyR5LdwW-KrKfJoE4bKo4w09R-3uMUlx4IhrwwQwIp6-1R1AHXzJdoE3DDKBPcke5bURSH7tfH-CcJ0Dt5etzDrdpDewl91j0jP9SB2yrafNw4Y6-8FVMUMKD9-1vebOj9obrHYtX7ZlEcOXdiGWgfDgfFePhCnVxx9OHs3ElZTJ73YprICUoda2CC1khfcXVlu17GV5lufWNqfUWN2TlLdSpu3wdzF6P4wq4nfNGFypzNEefUXFN0RedkmoGzOyGdWpQ4Z4p2zKt7h6bzCn2RQpbhKSVrxOMRE_5pjGP5wyjFBxfZL-6tKCbfS3GJpJbxFKBTdcxbOjDKvYmnaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BYHMob6285KmAALkmOgPY7bx2V6TUV34JbOX7M9RmgX-r9uQ1TbUiG-KXBGkC_NPgolS3TYVLTw_Oz1pc8vge6WSR-I1Lvmvs6gUqelIDGNaaeUn8mnK7-jJWaaXQgOvpF_c_GfrP1W1TIR_5wHZF8RuLbTCUgHC-egVce940EIJj66pCDwrSgZPjkKgji5S35EsQFFHyF1mSxylpYGGuh2xd2vMEyxUP28wvD5OS0ITQBkRE2hluUCVqjbcOuxyhiYA4NI9FTn45RUZb6aDZGaCISJJErEEKp0Zus_u9LJcB2_nxad32AqdU03aPAxn5zshVT7EP6HT0k9aQbInAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=MRj75UxbbrX0U-GYE2Y2gZNGsUWe9mUH_z3P7Av3Yo9GvfhT1Nsjz2ZHE0ADHWQWNN7oFLIYdBYf5IHkjbX42kSrojW3sMvSMJ5DzoBURd4vk8Nq_q9g40KZkFUsZYFh0P5v7N98L1zqCZRnaPEwt6pMSCxhtCnEkt3Df0bj8-Dika6oQgzrNrGvaOQzY0j2NhJClJ8Ooq4WHq-8-4S_FHNbYVwbKjJXFiJlOm5F6dNJnJnKp1xXPofIhdgmkH_Tci79mrAenIlBlMJmuJ3QBToBo464SEdhq9gEKhT8PnEJGV4Qm1uoj0elFxKHf1mhtuX9o8KJ1XAm8o7up4mbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=MRj75UxbbrX0U-GYE2Y2gZNGsUWe9mUH_z3P7Av3Yo9GvfhT1Nsjz2ZHE0ADHWQWNN7oFLIYdBYf5IHkjbX42kSrojW3sMvSMJ5DzoBURd4vk8Nq_q9g40KZkFUsZYFh0P5v7N98L1zqCZRnaPEwt6pMSCxhtCnEkt3Df0bj8-Dika6oQgzrNrGvaOQzY0j2NhJClJ8Ooq4WHq-8-4S_FHNbYVwbKjJXFiJlOm5F6dNJnJnKp1xXPofIhdgmkH_Tci79mrAenIlBlMJmuJ3QBToBo464SEdhq9gEKhT8PnEJGV4Qm1uoj0elFxKHf1mhtuX9o8KJ1XAm8o7up4mbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=qPkXMgZxVrasQAIkd5jEnEFf34HopPzUaIXS1b7Bf40c4RvOt6PpRNdRlP3hCwD7xInvtOWoT1odq2elesTpOxaKH9s699PhRnJ54gkMyyf9ZMIrot5BoarOdwK51ZUxJ4-LH5wqJ7sRMpJQ9Wuu__F_AiZO3Z74-AytEYw-2YdFYr2DeH4x7rCsradfzGhDwWmUm5kvjZmxZHQqO-f9KOPWWcZ5lD1ecGfd7OUa9qE6U_WbzTwP-CkqLc7_sRMeyPmfKYAqqm7jeWR2DulYuT3OmiGspsEkOSvDYkuEzR6kHuVfWCsJYliOO2N72NNlqtolk4PK71n_TA_FLvPcng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=qPkXMgZxVrasQAIkd5jEnEFf34HopPzUaIXS1b7Bf40c4RvOt6PpRNdRlP3hCwD7xInvtOWoT1odq2elesTpOxaKH9s699PhRnJ54gkMyyf9ZMIrot5BoarOdwK51ZUxJ4-LH5wqJ7sRMpJQ9Wuu__F_AiZO3Z74-AytEYw-2YdFYr2DeH4x7rCsradfzGhDwWmUm5kvjZmxZHQqO-f9KOPWWcZ5lD1ecGfd7OUa9qE6U_WbzTwP-CkqLc7_sRMeyPmfKYAqqm7jeWR2DulYuT3OmiGspsEkOSvDYkuEzR6kHuVfWCsJYliOO2N72NNlqtolk4PK71n_TA_FLvPcng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN7uGYsz7IOQwrIVXwYKFUecHm5DEIYuKVBoexPqm6IZNeYHGRqGNodx25MgAw4xIJEBhLzbQTVB_IS-BE_ZTXnK94ATFIzVDzI2YUilaveRZy33ifUDNcyLgsLS23c591pgZNAAsypSEzS4J3FGDLsh-GSdng9NzGUIxFcJPajNmShk4mFO1FLs-68H9fFFNeIxmoWhiskl1oqdLQvWWB-cN3F1aAg87Vdjl46OtW4Iq97at6HiSwLhsSxYmWLHhzLaIuKpSnmFdHaR7EcHflI9pJCsQFG4XwSDqaxxufIZlguDnM8tm9OT-6grZf5nIjoJ7R7B95f1q1rgAQs1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=i3O7WvzqxEV8GPmUF4xQS5vkaFs1Shpg52vJwEZwni-9HsKpBtZ-6JTnMHA4WmZ5HgYbs6rU9UHToTlkuoTOQHDJgMK_BrfQwqHlFWCrdrIJ-XEdyttrE55TvvWE1-ToLEP2thyZQ3LHJi1pgFlx6kXIY3cljnOaogKGVOdwJ8Q6q4WiaNJnbAsLNBOis2CiUHwBbFmql1S9jo9Ve_zQV-0pcLpF9sBl-ElZAjOoHmurdfHNf7Xrscsw-AbLDSsTYEJBJqXz5hhXBMwUW3QpXj4WpD2oXHixa9MAW1M5MZav_Ms6uNs7xaieXkUnylxfzh8OO4XsLxheWyzv1Wo7ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=i3O7WvzqxEV8GPmUF4xQS5vkaFs1Shpg52vJwEZwni-9HsKpBtZ-6JTnMHA4WmZ5HgYbs6rU9UHToTlkuoTOQHDJgMK_BrfQwqHlFWCrdrIJ-XEdyttrE55TvvWE1-ToLEP2thyZQ3LHJi1pgFlx6kXIY3cljnOaogKGVOdwJ8Q6q4WiaNJnbAsLNBOis2CiUHwBbFmql1S9jo9Ve_zQV-0pcLpF9sBl-ElZAjOoHmurdfHNf7Xrscsw-AbLDSsTYEJBJqXz5hhXBMwUW3QpXj4WpD2oXHixa9MAW1M5MZav_Ms6uNs7xaieXkUnylxfzh8OO4XsLxheWyzv1Wo7ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=g4JfdLKQI1mM2vEElBon6ppZkvSNzhBTlxUp9eR03RNz9ghoHUcxWE7VdMYeEX9UpNgv3MKLPz1UaCZZFDkFNvYzLrvOdMo0F5LlraAQpfbsUnQHnX_QX5Fav_p7uW94y5E3swzcM-wyxcDWan9QZaCWquciXfiUEGveSZZTMINchFFioBec5R3QheMkFe5GLWzqIkb4_bYT3YkMgoATiIlgzsTMEDWnwXFfBnpXiiCABq8J_xvh5pJ6BK_1jllvbmL-oMb3SGjM1KM23_LDxADFQbDKUKGC80hqRt1Sd2j4TqOcK4_rRlbrSrMN34eA59vIZIume93uXTot2nT9PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=g4JfdLKQI1mM2vEElBon6ppZkvSNzhBTlxUp9eR03RNz9ghoHUcxWE7VdMYeEX9UpNgv3MKLPz1UaCZZFDkFNvYzLrvOdMo0F5LlraAQpfbsUnQHnX_QX5Fav_p7uW94y5E3swzcM-wyxcDWan9QZaCWquciXfiUEGveSZZTMINchFFioBec5R3QheMkFe5GLWzqIkb4_bYT3YkMgoATiIlgzsTMEDWnwXFfBnpXiiCABq8J_xvh5pJ6BK_1jllvbmL-oMb3SGjM1KM23_LDxADFQbDKUKGC80hqRt1Sd2j4TqOcK4_rRlbrSrMN34eA59vIZIume93uXTot2nT9PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=TOfiRU7sZ8FfHvOEK2Ds_AURwUFOOJqEtFz_O3ie2nyy3ZCST22j_nNV7sx4t0CXAHsTFySGcuAUSHxVFAaRklsPq3eQpeSAgoy4ti7Wbv9AoACMT9DYFN-Ks5NmhzS0vnxTxu6dXAgxlf9rmmkizr7OjNGXYM-uDz6ggeGx7DTrGfFYto_o62Epxu8QoBSJX3LaMnj17hSZlxR3yvlXQTv439Z0FIagdHHBPuzdMWGiRQaOIrrW5WxOD3x5WMV9C21707kqHv74rBSJPBFW0l5TLlpjvd5-nyJtpo0ahBRQ7mv-OhI5KzglCKewA16Ot9AAVJOjV_cfC2dfKoMytg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=TOfiRU7sZ8FfHvOEK2Ds_AURwUFOOJqEtFz_O3ie2nyy3ZCST22j_nNV7sx4t0CXAHsTFySGcuAUSHxVFAaRklsPq3eQpeSAgoy4ti7Wbv9AoACMT9DYFN-Ks5NmhzS0vnxTxu6dXAgxlf9rmmkizr7OjNGXYM-uDz6ggeGx7DTrGfFYto_o62Epxu8QoBSJX3LaMnj17hSZlxR3yvlXQTv439Z0FIagdHHBPuzdMWGiRQaOIrrW5WxOD3x5WMV9C21707kqHv74rBSJPBFW0l5TLlpjvd5-nyJtpo0ahBRQ7mv-OhI5KzglCKewA16Ot9AAVJOjV_cfC2dfKoMytg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=jaJ0ZlsbvXPZx0T3j9OPejIoI6Kmextb5OAANwOYPBWA70ak4lhKfiLNkXvJJZjSWp1_ziJ5l8HDnpCMFkNyCibBCr76XNknsigluKKN9UhjL94gy8YStxjuVgmh3VTBORMIuUuJPNyE8d_SpvyUhiNLs64l3a5jSMQ8pbhIRKIyUie0PQ4Why0WesRrA26icl0rIYL2qlRTSqKCcJdnetvuxhlYqhaySzzQM0HARoU0_gwEa1T4CdsLukHtWup2M10sivd3Ubf8SLnYu_hIXVhRoDc8r3VN87yC0Ol2aVqjd5Z3dWzYPCGWz_m4EWLwCoJK6dMWAiRXJ2oa9F2T9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=jaJ0ZlsbvXPZx0T3j9OPejIoI6Kmextb5OAANwOYPBWA70ak4lhKfiLNkXvJJZjSWp1_ziJ5l8HDnpCMFkNyCibBCr76XNknsigluKKN9UhjL94gy8YStxjuVgmh3VTBORMIuUuJPNyE8d_SpvyUhiNLs64l3a5jSMQ8pbhIRKIyUie0PQ4Why0WesRrA26icl0rIYL2qlRTSqKCcJdnetvuxhlYqhaySzzQM0HARoU0_gwEa1T4CdsLukHtWup2M10sivd3Ubf8SLnYu_hIXVhRoDc8r3VN87yC0Ol2aVqjd5Z3dWzYPCGWz_m4EWLwCoJK6dMWAiRXJ2oa9F2T9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=voJNcPggfzkmsb7HkW6SPcGvAujZsSX0ygTwCSNT1DgzX3oLlMwW9dSEyAQaW8CZ7eZV0eFCMSN37jXx2QfJviA_quLFbR4hSJSjepXYb_2tJMU-UmteSVoJDHYjFxhpIb0bIHmetLfGZHrHlhwWqWCbr0TVH9f0KW3RQzdbWIDKD1GEs7zaw5hRrWMKuvToSpBE1RVHyR-cBtM3u1NG1VmM7cZVTU2bKaR-CvF6rihdoXMobVQeSpvK0yS9gmTT9fYrVUASat5UNDOmGJtEVL5wcYVB7Kc_a3kpFgOfPjMyeeBMi2dex-1O5Ee8Kt8eQuT-FdTocs_AOUHC_Uc8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=voJNcPggfzkmsb7HkW6SPcGvAujZsSX0ygTwCSNT1DgzX3oLlMwW9dSEyAQaW8CZ7eZV0eFCMSN37jXx2QfJviA_quLFbR4hSJSjepXYb_2tJMU-UmteSVoJDHYjFxhpIb0bIHmetLfGZHrHlhwWqWCbr0TVH9f0KW3RQzdbWIDKD1GEs7zaw5hRrWMKuvToSpBE1RVHyR-cBtM3u1NG1VmM7cZVTU2bKaR-CvF6rihdoXMobVQeSpvK0yS9gmTT9fYrVUASat5UNDOmGJtEVL5wcYVB7Kc_a3kpFgOfPjMyeeBMi2dex-1O5Ee8Kt8eQuT-FdTocs_AOUHC_Uc8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=LvoEyuVSdUucm2NXRP1yRPPc4fma4Z0jk4kGTs--wPRtw_3TyTtd_gU6sSYY7cRMUWW4QYLgOIhlQ6q0v4JpRNXhZL3HwGopTbPaHIpU5s9_-6-Zi907l1PCfP_UcqhiEZVURcDfBKy8d4RnpJcd-aE3RoYMnK2Wdyt2bEb3Dh176eK7Dtu84P1SXXXMRORmRe_MBRVYC45747DT9dKvI4W8j2Ct6EHlBsFAHnCBXMP2qFCZKu3nYUExRhBe8l7FHPhPsqxk9xNFe5Mw2y4QE_gMeLzsVGV0FTo6VuiqIhzElxZKU7TO9r6Pjpy9Pp3rTMjRNRbfkVUyQhqL2_509w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=LvoEyuVSdUucm2NXRP1yRPPc4fma4Z0jk4kGTs--wPRtw_3TyTtd_gU6sSYY7cRMUWW4QYLgOIhlQ6q0v4JpRNXhZL3HwGopTbPaHIpU5s9_-6-Zi907l1PCfP_UcqhiEZVURcDfBKy8d4RnpJcd-aE3RoYMnK2Wdyt2bEb3Dh176eK7Dtu84P1SXXXMRORmRe_MBRVYC45747DT9dKvI4W8j2Ct6EHlBsFAHnCBXMP2qFCZKu3nYUExRhBe8l7FHPhPsqxk9xNFe5Mw2y4QE_gMeLzsVGV0FTo6VuiqIhzElxZKU7TO9r6Pjpy9Pp3rTMjRNRbfkVUyQhqL2_509w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=W4TQGN81yGAggRHS0IWfJ4p7L_BTkPcaf7CA2kNKk58HyZ1-xIqU0KeM2c-DBaqGyyu8GSqTu8Ls-dJFuBDMJjyhQfkQRVcYSS2WvyM0GDdhvUzzh3B1Bz6DaG_VgNVHEbHoQelmVMGMFZujUz7wBN2zbVnU4SXAdiWgIwvs4HYSZ1LpY24xvY4YzbxGgiaFb0A1ac3UZVjUk0_pgte6SWKbyrip0HCSvd0gCgWIxlQWReE2zqdmijAj-eIc-NVhr-zCNHH1zuocISDdgWIJ3A-2TNEktG90qP2Rltp3Jaih5XA1-ZTOhF2M98EcRDQvv9eIKVo8ihLEacYYSE0pq3OD1yTxTMmVHcQ9ZJu_YGIgpJMp45w562TyONlX09R30KcRBszFn9Js6QsAiLDsOiWXAQP67V1a28mF3dpvRQvBlvwEFNmm68vb5Lkfw4Lt93Tfgs4FnXxW7FJ56l4wUwKkPLkh8x9v4h9sMGj8254gtVh053mHnZM_-hgdMq1gyP5plBAic3LlRDkz_R6hOByi7UqpwgvR9O7VgUR99cPEIlWgUp-70hbysDuN8JCaq6Jlp8Woo81Ng2Rv_pZo0pu-eD2ofa-e9g8sniEoTzu8z1mgTrCEa56cjwyEQJ8rXHB_wFqL59zeJUHChifCHaj4yzUHzvbbtlolvZEp3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=W4TQGN81yGAggRHS0IWfJ4p7L_BTkPcaf7CA2kNKk58HyZ1-xIqU0KeM2c-DBaqGyyu8GSqTu8Ls-dJFuBDMJjyhQfkQRVcYSS2WvyM0GDdhvUzzh3B1Bz6DaG_VgNVHEbHoQelmVMGMFZujUz7wBN2zbVnU4SXAdiWgIwvs4HYSZ1LpY24xvY4YzbxGgiaFb0A1ac3UZVjUk0_pgte6SWKbyrip0HCSvd0gCgWIxlQWReE2zqdmijAj-eIc-NVhr-zCNHH1zuocISDdgWIJ3A-2TNEktG90qP2Rltp3Jaih5XA1-ZTOhF2M98EcRDQvv9eIKVo8ihLEacYYSE0pq3OD1yTxTMmVHcQ9ZJu_YGIgpJMp45w562TyONlX09R30KcRBszFn9Js6QsAiLDsOiWXAQP67V1a28mF3dpvRQvBlvwEFNmm68vb5Lkfw4Lt93Tfgs4FnXxW7FJ56l4wUwKkPLkh8x9v4h9sMGj8254gtVh053mHnZM_-hgdMq1gyP5plBAic3LlRDkz_R6hOByi7UqpwgvR9O7VgUR99cPEIlWgUp-70hbysDuN8JCaq6Jlp8Woo81Ng2Rv_pZo0pu-eD2ofa-e9g8sniEoTzu8z1mgTrCEa56cjwyEQJ8rXHB_wFqL59zeJUHChifCHaj4yzUHzvbbtlolvZEp3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUZ8yheUy329juuif91WRukFon-Ln2FFR9rCtS1eebGuZGIsKm1Jw4uf93X7bvzQKdprMWUVbSl0qviwItmZic7jHdR7EWzlNPWC0_98JE5Db_KNSdagBU6MwuyJ4q_MGxD1-2SXlM4PO0FZhHLgMEClEtyyAqRzjUXQfXJh6MOxbhPYRSQkcoZHRoPrQXZhUhUxn4Ht4AmHOmqwJNeOR195kFo2c3b8G2ikGZmzD9Kcx29K0ZqpK6KpfGDEnezpmz2oH4UYZH5kPnp-i7Q58yL6hLMVAa26TIAYuLgMBiUflyGpyUwy8XrX12iRsFhKw8U7WZwHQZUlPqBBc6Qorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=qtgA2j6Jp3lQ5xnhNs3FJylCbdXZO6zFc57QWGNaEbjRccNO9XRo1CupBUiUFZV_TTFYRgsdX-ycF0ToHUGT9q8IsGbAfmTPIPZGotSv18IxPONEzP3ymJDvMuXIhB9FcppmlsQgKnZfdFwQsG8D__1bKhJJWrVENzZXqKel7l2bIYJCV0_Vu9OWI1ScRdLpJ1UJjpptdCX3naKxG86UbzHGTjZIdwdCL12Txmsqrvik8jU3iPVKrePd0NYUUy7bVN9izlqTm9rKfUIkH3BPpf23pdPUCC06iQUL1iAymb0dUS0HFVS9AmI1THFU0rNGWguQFnFUWFLnjruocUubLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=qtgA2j6Jp3lQ5xnhNs3FJylCbdXZO6zFc57QWGNaEbjRccNO9XRo1CupBUiUFZV_TTFYRgsdX-ycF0ToHUGT9q8IsGbAfmTPIPZGotSv18IxPONEzP3ymJDvMuXIhB9FcppmlsQgKnZfdFwQsG8D__1bKhJJWrVENzZXqKel7l2bIYJCV0_Vu9OWI1ScRdLpJ1UJjpptdCX3naKxG86UbzHGTjZIdwdCL12Txmsqrvik8jU3iPVKrePd0NYUUy7bVN9izlqTm9rKfUIkH3BPpf23pdPUCC06iQUL1iAymb0dUS0HFVS9AmI1THFU0rNGWguQFnFUWFLnjruocUubLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=EGqz1M-487_NZpzEGbs8rIMoNogM0HHhAR1_p7HHKtd5Kq8yRcakvdK-yUwDzL_WRlLBK4SSZUJFb7TIRYXdKpvk7MZwZSdi48WSGAJHyKnIZ8SJy6DeOTPQrUlepyze-469cApu5pRS1Pj6vW7DJy6shbGdN0RndE2X6cwHg0jgkPpBouvzCMuF1h-wWkPEeKd0BM0lK8Ipg2h9G0gJXXkKnTKOKOWn7yiGanU4Y1Na28oda-azEzjqA0PKNPTSDLRGqZm7furnqnb7BT3XO6Sk6OuqfrIRQgiWYRNaoxMxhV_sfW4n4TyHJ_W6Sk03cdyDO4O4Vv0OBWr2FYORsAa7QMn49uNvTC-I21F6_5ogLIrVa3rGWyUZYaX8hIcpCncG-yRu0J2zb_mgVvo3Izs2eVYrpt92gCtOhTpwTAU0QBhB_G2c6mXews8SgbyVKd9ITHzPHcCpfM2aMPOUJHzUGQSLuOWrxWFk9MspcF7pOnmfjoPEnpC_gJ8UhPaz-AidS6owxum-39gAc_x81w1TKO7ewJ7quM62-77qxEaEv6ScVz8ayof9EWKLETGs-RdMTA09YWdm9j_q04DFFNWrrUqSkKVhLGJyV4dQptOjZyELmr8ycPWixlz1KGhW4rG_iCyPZIFl5tNCy0XIfTQ_6I8rS7gZcYavrEfrAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=EGqz1M-487_NZpzEGbs8rIMoNogM0HHhAR1_p7HHKtd5Kq8yRcakvdK-yUwDzL_WRlLBK4SSZUJFb7TIRYXdKpvk7MZwZSdi48WSGAJHyKnIZ8SJy6DeOTPQrUlepyze-469cApu5pRS1Pj6vW7DJy6shbGdN0RndE2X6cwHg0jgkPpBouvzCMuF1h-wWkPEeKd0BM0lK8Ipg2h9G0gJXXkKnTKOKOWn7yiGanU4Y1Na28oda-azEzjqA0PKNPTSDLRGqZm7furnqnb7BT3XO6Sk6OuqfrIRQgiWYRNaoxMxhV_sfW4n4TyHJ_W6Sk03cdyDO4O4Vv0OBWr2FYORsAa7QMn49uNvTC-I21F6_5ogLIrVa3rGWyUZYaX8hIcpCncG-yRu0J2zb_mgVvo3Izs2eVYrpt92gCtOhTpwTAU0QBhB_G2c6mXews8SgbyVKd9ITHzPHcCpfM2aMPOUJHzUGQSLuOWrxWFk9MspcF7pOnmfjoPEnpC_gJ8UhPaz-AidS6owxum-39gAc_x81w1TKO7ewJ7quM62-77qxEaEv6ScVz8ayof9EWKLETGs-RdMTA09YWdm9j_q04DFFNWrrUqSkKVhLGJyV4dQptOjZyELmr8ycPWixlz1KGhW4rG_iCyPZIFl5tNCy0XIfTQ_6I8rS7gZcYavrEfrAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=iIfT24Ox_BMtwHbgQi5dHGSAFn4QqMRGo4G6zD9VCO3L032NNB1OV_uXYMBkkmyQnrgRn-9YzKEkjmmU_YOW-zLhafgu9C0ZUBwAtspNPwd6W-YMZ6MKSsuILp8kuPrq03bINoDgrI2yKylybqID38LNLggonMEprq58e-ZPoJaDV8V-njCv_w57raLca0RV0B6EdprkNM8EtA1_gd2WWIQXdQJyJax1WV_Rs5AnK1pbC1Qet68TOnFHWyjCE1ap-tHHcX_mU-b96Lc3QSQLDpGsOWMYmXcQZ6oxIJxMPZlAqj18yEa4C0dclbwS5TGsHpI1tjLt1xGYmQWNzO8czQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=iIfT24Ox_BMtwHbgQi5dHGSAFn4QqMRGo4G6zD9VCO3L032NNB1OV_uXYMBkkmyQnrgRn-9YzKEkjmmU_YOW-zLhafgu9C0ZUBwAtspNPwd6W-YMZ6MKSsuILp8kuPrq03bINoDgrI2yKylybqID38LNLggonMEprq58e-ZPoJaDV8V-njCv_w57raLca0RV0B6EdprkNM8EtA1_gd2WWIQXdQJyJax1WV_Rs5AnK1pbC1Qet68TOnFHWyjCE1ap-tHHcX_mU-b96Lc3QSQLDpGsOWMYmXcQZ6oxIJxMPZlAqj18yEa4C0dclbwS5TGsHpI1tjLt1xGYmQWNzO8czQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=SnkIS5IixG6x5Mcej89x_Sa0KofC9GsydF7XqCiQA7Hf4ADJGAnKSWLgk66LRVxsJvwf-I7naAQ-pA1RqMtjrCZnvjOEMBUsZJR_FhjCXyngty5g76bEqK6mm39PXHn51ft3C1gGJi7Lh1fPPCW_8Y2FwJO84oZFHCyTtMwtDKFIPWy0tEww0ws766PkjxoYv9dp5-3ZN-ffTASSj1uFnyNRnMuNqEDRqSbgW1HXkdWmLOwEWswwN_H8U4MewLUNS1dawihkKWVTr2yrbSO8eFK_JfMuVlFBRoKMzPteJbgczEvZfExwlGAS72tgrPFIqgm0uLaX256LRh4-TAOuyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=SnkIS5IixG6x5Mcej89x_Sa0KofC9GsydF7XqCiQA7Hf4ADJGAnKSWLgk66LRVxsJvwf-I7naAQ-pA1RqMtjrCZnvjOEMBUsZJR_FhjCXyngty5g76bEqK6mm39PXHn51ft3C1gGJi7Lh1fPPCW_8Y2FwJO84oZFHCyTtMwtDKFIPWy0tEww0ws766PkjxoYv9dp5-3ZN-ffTASSj1uFnyNRnMuNqEDRqSbgW1HXkdWmLOwEWswwN_H8U4MewLUNS1dawihkKWVTr2yrbSO8eFK_JfMuVlFBRoKMzPteJbgczEvZfExwlGAS72tgrPFIqgm0uLaX256LRh4-TAOuyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=i9tGfXWnevhrUtQISZ1oXIKuz_4c50ms7m1OT2i2XEHLWLtxg_2Jtm7ZQw6qaUeLLog2x40om_tlBJTMkk5ADnb-MxgEGKFenN8otZuCFCZfGIbhaCS39nNnmWYxM4qSeNNSp8muNFbziNq-vj3a7L8tZGFX8XQ5Uqa0evrwn_z7VbEaTsges__d0RbEjAbJiR1QWdcQapyhg1JGdynD0MGQ7bFPDlhCksU21A4okGyJf97_UYhKBkht-34jRI68WEaf-yYh5odLOzG1eTULQmxv_03pZMYKr4QjZWAJlL4z2RbaWDHjlBQH0eyitXOaHeuSdBLnkySK2bQkiaS3nw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=i9tGfXWnevhrUtQISZ1oXIKuz_4c50ms7m1OT2i2XEHLWLtxg_2Jtm7ZQw6qaUeLLog2x40om_tlBJTMkk5ADnb-MxgEGKFenN8otZuCFCZfGIbhaCS39nNnmWYxM4qSeNNSp8muNFbziNq-vj3a7L8tZGFX8XQ5Uqa0evrwn_z7VbEaTsges__d0RbEjAbJiR1QWdcQapyhg1JGdynD0MGQ7bFPDlhCksU21A4okGyJf97_UYhKBkht-34jRI68WEaf-yYh5odLOzG1eTULQmxv_03pZMYKr4QjZWAJlL4z2RbaWDHjlBQH0eyitXOaHeuSdBLnkySK2bQkiaS3nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=jFk83KnpfnvpqjSV6vQpNX4e2BfYj7FmY3tzEjMYqvdz8cAqFwXHLh6Ie6djYxLfqNOMvd0gaVZC9sn5EbzHWlYDAcgLrgW1TN_hwbiVM-QE-3ZkK3Pqa0pn4qOoThw-rJPqPlVZvmum9cWJidzARGXILrphh3a5pGqBvpFWYYW4nxWyQ5VVDWFqI7ObrcGEDKMqDT3AJQ-lHslYH2k1RFcnVXu8uLsOr1hv_CQ4OrzGsyinmW7B3sBhWbArrWmNZbziRFa3KReA_227B-7EXNgQttJVei6yr2rwD7_nzZY0z4Ns98D-7Wd2eiZ2Qma_R82gKBWKBQczXWiarNEyJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=jFk83KnpfnvpqjSV6vQpNX4e2BfYj7FmY3tzEjMYqvdz8cAqFwXHLh6Ie6djYxLfqNOMvd0gaVZC9sn5EbzHWlYDAcgLrgW1TN_hwbiVM-QE-3ZkK3Pqa0pn4qOoThw-rJPqPlVZvmum9cWJidzARGXILrphh3a5pGqBvpFWYYW4nxWyQ5VVDWFqI7ObrcGEDKMqDT3AJQ-lHslYH2k1RFcnVXu8uLsOr1hv_CQ4OrzGsyinmW7B3sBhWbArrWmNZbziRFa3KReA_227B-7EXNgQttJVei6yr2rwD7_nzZY0z4Ns98D-7Wd2eiZ2Qma_R82gKBWKBQczXWiarNEyJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIDmwos1gw-WHT1xlim1E3b9Ach4uoimqSaXoMCltH_UmpI7S1jILd4IkM8_QEvSb2u-WvT-bh96rC9B54t3iWLesaA_AKK5kLnaBJCxVokcgThL8wjbSf-OoU07v3g_aFNrOkV5k0Rh-YBrL3xi57Mw2Vep-lLjLV7SSoM956JACNId45de4IXmWGSnflrWazdXoGTqOXXF-utOXe-C9w0ANApD7-K8ekiii6ugVfHskIxkgZ1Wo6vNATxTWplQOcaIFU4tt4-gVac9mHPa8Fb04liHfX8ek1WNxvQdzXkiGuV9R7EB1aiW7MxQ5VnMtxcieEMD-CGejFMBX34fMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrbmdgJW1TVD6DbvatBd1ocLZ6AHypNZlVwd3ZhXqO3IlAlpcY7G2Y0hxebRj2F4Vq43Xl9Cgi5GBw6C87HFop9CbfOCIsvHYYy-6cu3At-tJf3FITZN3I0OfllEwuTpc62f6pCgZMGQ2fJg3ZTIEjOPGJq44uyFzFdtkyLoUxod72yxdRruczyFZqSA7rbsunRuZusorEBevW19ZDuYn9unQDMFvtGfR9vkbayz7jw_HHta3wDmx0TkoiMx5RoDFdc3ZOAmrlMCBhipmI67N---sLexhafiqpZsXYBxfaS2dnyt3JX3cA-oxkdSO4-KpvsTnGBXDFNVNX3mvvZNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=hUTfF9OIv-q8kVEIgtkJ0gdjDAIcptxl7zw7MNR1NAYu-I3-ia3mRIYEkSicKI_gl2wdUVbjDSYAuEA4S_Q6TPzObLJdSCJBOKN5McI7VY8aVLDnYfkmcR5Pydd6MlBmDwZLr6OehABFEbjir5tWaQgWBrZdMtxjSka1zlYteMSo3tRnR1WmhlLTplHsgSqnvtPr_BxUloqU6E4CDzO0-pNGqoYSItR6mwd5uDHeypKoxK3A5wNVVtaZYsTmyeF7wddeEsWe5h_v9ST4fvgO0AXKbNQmX23Q_2Fa1cMY92CMX3-QfS7-dEVgdJiE88iPte8NhQn24E_kzjm8PbeC-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=hUTfF9OIv-q8kVEIgtkJ0gdjDAIcptxl7zw7MNR1NAYu-I3-ia3mRIYEkSicKI_gl2wdUVbjDSYAuEA4S_Q6TPzObLJdSCJBOKN5McI7VY8aVLDnYfkmcR5Pydd6MlBmDwZLr6OehABFEbjir5tWaQgWBrZdMtxjSka1zlYteMSo3tRnR1WmhlLTplHsgSqnvtPr_BxUloqU6E4CDzO0-pNGqoYSItR6mwd5uDHeypKoxK3A5wNVVtaZYsTmyeF7wddeEsWe5h_v9ST4fvgO0AXKbNQmX23Q_2Fa1cMY92CMX3-QfS7-dEVgdJiE88iPte8NhQn24E_kzjm8PbeC-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmcIf0NYD1SQx24OTUSQaftm3S-kKbx1r7vdDUzkOJnFqXtIjPyUg88lvXqFOhck3MvrVqJu8C4ub5qKNYluDVHHMnWdVLJ6LPNF7jcTXYzv-0RI2tcONjgiouDG4Y3VIonPrPCIiBebZBl0DqsgZINIe9nWRQ6nRUqJawDcpELibWLPzaM1z_DG9cJvouQ3mPrLZ2f54pQZznvtUQ_-ZsbAuf5bG5Sere1PiDquiMfd7w_5dMgEqL4pP9SKVUJQ0_4jSo2HBbSm_ohlsNJn98KtmqP2AvUEl4cjLINpRECk_zfUKLP7WdhuDWu26L3Qm0U5JZRDYM05T6n8sIbY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=GyBt96bF8lOkJ1e4QXIfnW2s3gB1_E1EBTAJszw9DamK5sgtSLaXpaE45X5HlNrs7Dzdo6rXRuMqqupyuYwjPNiLpnnbs2GqpEv4cauvAEe7hDbIO4pHY6FTRca8MjlQJlcdyZp8_KnNEs2xcMYQQO7ZLkIbvY1LgHs7uSmUUjODlODOEDwFCy4abr70c-7ykuPs0a9TY4nRWywUNnFbK4g2VHC69rp8lYewbKjeOkiDESG4S41bWJfqa0tkW1NeOpqYCxlma-ETT_CoAilctw1SlgSFZI1IrdBttTsP4-a61xGmuTq_ynjKsl5IfNkQT73GMjmKarV2eZp02_D_kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=GyBt96bF8lOkJ1e4QXIfnW2s3gB1_E1EBTAJszw9DamK5sgtSLaXpaE45X5HlNrs7Dzdo6rXRuMqqupyuYwjPNiLpnnbs2GqpEv4cauvAEe7hDbIO4pHY6FTRca8MjlQJlcdyZp8_KnNEs2xcMYQQO7ZLkIbvY1LgHs7uSmUUjODlODOEDwFCy4abr70c-7ykuPs0a9TY4nRWywUNnFbK4g2VHC69rp8lYewbKjeOkiDESG4S41bWJfqa0tkW1NeOpqYCxlma-ETT_CoAilctw1SlgSFZI1IrdBttTsP4-a61xGmuTq_ynjKsl5IfNkQT73GMjmKarV2eZp02_D_kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=a8UhXJZOkAI63YYtl8iLKN9V6Wh2vjlXlXr0lCx7D2EM44zz-qa2jEaUoE5aVfMYPax40zSOTmsiLg475DUjJ1pw89aE-lANI9Av5kas5JqA5vP-tAsedAV9JacrlISQ82IryoLRWKITSvn3hTAkNrTkcLcQgocCOY-YBkbI91Qiu3DAEQGgBH3v_lbEF59m2ukWxi4fe-lHmnKJ9itbYg-7I_rWZzHsjU1yTYdvGJW0wwd1zqA_yT37PleoYDMqe7g5Y5fUGSwsA8Qq7RiRON6kxX0BlpUXKF0NchZAMkTM88PMtu44iYleWArLUTTTNjWjAHEJY3wqRZDGq1UKXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=a8UhXJZOkAI63YYtl8iLKN9V6Wh2vjlXlXr0lCx7D2EM44zz-qa2jEaUoE5aVfMYPax40zSOTmsiLg475DUjJ1pw89aE-lANI9Av5kas5JqA5vP-tAsedAV9JacrlISQ82IryoLRWKITSvn3hTAkNrTkcLcQgocCOY-YBkbI91Qiu3DAEQGgBH3v_lbEF59m2ukWxi4fe-lHmnKJ9itbYg-7I_rWZzHsjU1yTYdvGJW0wwd1zqA_yT37PleoYDMqe7g5Y5fUGSwsA8Qq7RiRON6kxX0BlpUXKF0NchZAMkTM88PMtu44iYleWArLUTTTNjWjAHEJY3wqRZDGq1UKXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=nabwyp4LDi9QpnfzwPba5oftSVKCsC2KnSb5eULwqL2NAekNMP8ml92JUtLd6E6xPwk4OkTWN7P3bkaHyHSA6sSHJI1AIWC4c-7g6KdTgpOdywW9_e0y5G4M4F6yDcQT-hF2ondrUL3KpXcVIZXBliolshEavP1EcWf0I_SkkiNyq9BqmQxcBtBg4TEKyUnznVOXtKGLl5pRqvRgvJz5Rxf1dfCHBnVGae3voK_VhKdurNLLSER0iuCc0VrTJl5Y4_2vv0vp90PLKaQ0VHfaAopQCsvPkI4dxIquw96Jow3ISVsVCMkzLTSR9ZWSGOSw9nZppNL6nOK9f4XfUo8lSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=nabwyp4LDi9QpnfzwPba5oftSVKCsC2KnSb5eULwqL2NAekNMP8ml92JUtLd6E6xPwk4OkTWN7P3bkaHyHSA6sSHJI1AIWC4c-7g6KdTgpOdywW9_e0y5G4M4F6yDcQT-hF2ondrUL3KpXcVIZXBliolshEavP1EcWf0I_SkkiNyq9BqmQxcBtBg4TEKyUnznVOXtKGLl5pRqvRgvJz5Rxf1dfCHBnVGae3voK_VhKdurNLLSER0iuCc0VrTJl5Y4_2vv0vp90PLKaQ0VHfaAopQCsvPkI4dxIquw96Jow3ISVsVCMkzLTSR9ZWSGOSw9nZppNL6nOK9f4XfUo8lSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=rBDIa3Fvwu8wueWFgVovHNxFMtYYSzmyW_7G9HMaaV1bMpZuiQp1JRDZ5t3zKHT8op01nXk1G-OnBpHhCARsYh0ZO-qx2IKAohQo1JwEmO1EVKIfYPXvVXYTEp1juQx0ILkg2d9YiDrSwncPQrH2ydAhSrnzn81nN4pMgp0LH4v6x6acGCfs553at6_SI4mL2zm_shWas43RWsoh8tQYyiFZk18sfQ8OB6IdIZV5IaZtUiwbxVQT18piiBcT_7GxPazz0ev3unr71Mcm8S-qUCkGFMj1m9Ar0MsaEA5vSzzjiy86SfE3FxFTsiYyk8ldg9QWhGUQEkrto_xTnEoj-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=rBDIa3Fvwu8wueWFgVovHNxFMtYYSzmyW_7G9HMaaV1bMpZuiQp1JRDZ5t3zKHT8op01nXk1G-OnBpHhCARsYh0ZO-qx2IKAohQo1JwEmO1EVKIfYPXvVXYTEp1juQx0ILkg2d9YiDrSwncPQrH2ydAhSrnzn81nN4pMgp0LH4v6x6acGCfs553at6_SI4mL2zm_shWas43RWsoh8tQYyiFZk18sfQ8OB6IdIZV5IaZtUiwbxVQT18piiBcT_7GxPazz0ev3unr71Mcm8S-qUCkGFMj1m9Ar0MsaEA5vSzzjiy86SfE3FxFTsiYyk8ldg9QWhGUQEkrto_xTnEoj-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=GflSOwQzT_qp9IUXo0VjwhSO7aIsQE0G0FMJAJFfI2NdXsPC6cCcn2wFpKJX3_B75zhk1VP1vERZdG3deBNXnIDt20JEOk4grMGmQEGtunpgti-gTBEkUiooFN5B9b9wCJqQOiCgBf3ClzOSbkcNXAG4dcxmqzxcQBrw8hq5d1nvCfVRn3O43f0NdaPshipOGIOoghu1W0QALS6aWm3FZpyFmDssYzXu6KUwmjrc8BpLDwplercDdsOP4DD3gV6hSFuyEtEtLyGaWqWvgZIp8WbOIdM109a7gl5K632bSVPWaCcS6MTypxf43JdXF8FZcOWpjWQq5C7BrqmXboAfeD3DXIedqqrbw_1Kx6qKNT8pMrPgECsyhRKvQCpQjWD6W8f5DXhepP6w5AMPnyradknJD-RfPBXY8MhFA7P6yBYW23UoJ9inQckxcgXHDNhXy0z4t79UR0ofQk5x5k82BwbhZoEQqAoZgSdcHLkP-V3NJItfo9kZVhmorWr-XsKjIBn3rc3Jy1snockIliVlvlx4mAzI6rtJU64QJo-6W8mZaCw18mkJBQ3dSeRKsd_0Q66YPJFu89DMFufZL1xmcgpfiN11ewU1n3InugrvNzUKoEOQ2VBcj62kPqab1VuuiQjyReLNKriQyjLOCbFLeMaedfu417S9z8A_rTLw-U0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=GflSOwQzT_qp9IUXo0VjwhSO7aIsQE0G0FMJAJFfI2NdXsPC6cCcn2wFpKJX3_B75zhk1VP1vERZdG3deBNXnIDt20JEOk4grMGmQEGtunpgti-gTBEkUiooFN5B9b9wCJqQOiCgBf3ClzOSbkcNXAG4dcxmqzxcQBrw8hq5d1nvCfVRn3O43f0NdaPshipOGIOoghu1W0QALS6aWm3FZpyFmDssYzXu6KUwmjrc8BpLDwplercDdsOP4DD3gV6hSFuyEtEtLyGaWqWvgZIp8WbOIdM109a7gl5K632bSVPWaCcS6MTypxf43JdXF8FZcOWpjWQq5C7BrqmXboAfeD3DXIedqqrbw_1Kx6qKNT8pMrPgECsyhRKvQCpQjWD6W8f5DXhepP6w5AMPnyradknJD-RfPBXY8MhFA7P6yBYW23UoJ9inQckxcgXHDNhXy0z4t79UR0ofQk5x5k82BwbhZoEQqAoZgSdcHLkP-V3NJItfo9kZVhmorWr-XsKjIBn3rc3Jy1snockIliVlvlx4mAzI6rtJU64QJo-6W8mZaCw18mkJBQ3dSeRKsd_0Q66YPJFu89DMFufZL1xmcgpfiN11ewU1n3InugrvNzUKoEOQ2VBcj62kPqab1VuuiQjyReLNKriQyjLOCbFLeMaedfu417S9z8A_rTLw-U0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=i-mn-gPG5pYUR6HZYCZ0TPFp_4T2cfmNXlQkpYXlMY3T_2PbabCnu62llzPf3aAfqLLtGg4s69Au5G1xEDHGQGBoeMpK_S_LsBpRR0N93vN3Db4HJuY2dETlzB9sPWywEZbILG7X6Hf_Gk5s-TGdfVOUde7nIY1gmz5bnhU1L1Jj05lD8jj5kcuCB4XUIh4WKI83ruMehAk2GKEr0Y0bAVf8O40aB0IhhL7CPcRPmQSRmefLY78qB7452eBcvIcWBtKOpX-YrTqkZEQM1zVsfREjM0D7h1MIEbqebr3JSbAomxGL7kOEljZqKyh-MPDe77BTwbQUeKSgYMPRKsPdkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=i-mn-gPG5pYUR6HZYCZ0TPFp_4T2cfmNXlQkpYXlMY3T_2PbabCnu62llzPf3aAfqLLtGg4s69Au5G1xEDHGQGBoeMpK_S_LsBpRR0N93vN3Db4HJuY2dETlzB9sPWywEZbILG7X6Hf_Gk5s-TGdfVOUde7nIY1gmz5bnhU1L1Jj05lD8jj5kcuCB4XUIh4WKI83ruMehAk2GKEr0Y0bAVf8O40aB0IhhL7CPcRPmQSRmefLY78qB7452eBcvIcWBtKOpX-YrTqkZEQM1zVsfREjM0D7h1MIEbqebr3JSbAomxGL7kOEljZqKyh-MPDe77BTwbQUeKSgYMPRKsPdkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=tqjAhx_jH4GKGc1Wl0si09L5BBeT61aRk4nYDz2XBaIA84wNU39oMYgWNPxMpDskLtRPvUsxfvdjHlXpYVhOc20PRbGOuOTZLO476Wz3TS1KiS6ej6L6KHdvnU8tkUtKf10J0FY84cfZGgoFkHVHh6-gfn01jzx80E3dCPURR9q4H694c3qrEKDVxQQqup3_lMtPnnncwtkNDiCkxhLk9fhvYoVr1-E4duIfhwWXJA9slNat0o80OKqCkvpqGfQ6bjbP3yoXCT8f_ly4wdquqJDdHUCYeQakdtX4UqCd1JHVEf6yUclp3F-cFheqIOW9Meizgl0SNCpcgheDCCkh-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=tqjAhx_jH4GKGc1Wl0si09L5BBeT61aRk4nYDz2XBaIA84wNU39oMYgWNPxMpDskLtRPvUsxfvdjHlXpYVhOc20PRbGOuOTZLO476Wz3TS1KiS6ej6L6KHdvnU8tkUtKf10J0FY84cfZGgoFkHVHh6-gfn01jzx80E3dCPURR9q4H694c3qrEKDVxQQqup3_lMtPnnncwtkNDiCkxhLk9fhvYoVr1-E4duIfhwWXJA9slNat0o80OKqCkvpqGfQ6bjbP3yoXCT8f_ly4wdquqJDdHUCYeQakdtX4UqCd1JHVEf6yUclp3F-cFheqIOW9Meizgl0SNCpcgheDCCkh-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ux0M8XcO3GoQ1xIeCMG3etdPXf88kXYuXDym6TZXkYN7XerQ_p5COFefDHS8ygsZ00GuyCeH4DUpfdIzCzgVHW1JP9QiBMmhP1NHNFlhaT_unMgLAqGrntgv339sk3VdYGmmeCAOOqSnk8pvJwugDwus1cPBFo-P1vHvtAgRGime1dm9X9aLJDs87wSClx_9SxfQ0jZVKAk5DdzfEDRgZI2PwOamwalk6qc4ycVI-LS_nqyVaLeh4HDcZTZonTWeiW_G4_VBCQjMLtpqea0mBctJ4uiY3ygSueui-6HzG8aU8XYQKJJoNbuNO_Vp-GS1ckfRAx3C-40q_nHArRKf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=ux0M8XcO3GoQ1xIeCMG3etdPXf88kXYuXDym6TZXkYN7XerQ_p5COFefDHS8ygsZ00GuyCeH4DUpfdIzCzgVHW1JP9QiBMmhP1NHNFlhaT_unMgLAqGrntgv339sk3VdYGmmeCAOOqSnk8pvJwugDwus1cPBFo-P1vHvtAgRGime1dm9X9aLJDs87wSClx_9SxfQ0jZVKAk5DdzfEDRgZI2PwOamwalk6qc4ycVI-LS_nqyVaLeh4HDcZTZonTWeiW_G4_VBCQjMLtpqea0mBctJ4uiY3ygSueui-6HzG8aU8XYQKJJoNbuNO_Vp-GS1ckfRAx3C-40q_nHArRKf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X21SUO6fTodYLRIFaMpLPnddQnI1PBz2MBWVnac0up_YjM_XKQmK1zstHJBcy0HIrqhDN66_SFY7E68oz6YFQGhijAOA9tFqQ_Yych9MsaRu6lSAB2KJicMTAS7pCRJUg24gMT1rEhm-1wS8Xu8dr6uyvzDzccMIZschVLFSQN2KN9WZF7tjspkveVjlUglN_jK-D27eHvuOlVKeCKB54ABVUXBS45bvS4bb3aJMMavhQiHMiSxQu4zCugVHRe25LsZr5TXzpahSvpelFDl3B_W6t-1pFxrnxTy7vXJ_vxhW5QnK6DaZykNVEh_wBlFIxC8ExpRnaXF_MRnkvLiZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=uko2__zbwL0NnEs1t2NxbbpipvQeQOg0frgdChT41xgQT376ASotOT0f2vm0Sxgmo9taacqL4fvPieJVGfCiULU9Qs8gdxL2lsB3sqQv1ruozS6zn2H2jt-8FIOjhM2RV_xjqCfqTwFqnPVZBX7bHUe_xYGyLzOilg6fitstI1KYzbEwBWSR6h_r7Up01kqAi1X_yWy1zQJ5Ht7SxNNWv13eGdeJxIClylkFXW3XAg8gLowOo_3RtxUbu7MV0rDtbbvB1Yjd1w2DKW1KMGXycnNtgMbBUSsSDlOTbHNb7CCnZI38HWoYaSK4GLPKis2_b636XCKydJ38XKrWv6xR8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=uko2__zbwL0NnEs1t2NxbbpipvQeQOg0frgdChT41xgQT376ASotOT0f2vm0Sxgmo9taacqL4fvPieJVGfCiULU9Qs8gdxL2lsB3sqQv1ruozS6zn2H2jt-8FIOjhM2RV_xjqCfqTwFqnPVZBX7bHUe_xYGyLzOilg6fitstI1KYzbEwBWSR6h_r7Up01kqAi1X_yWy1zQJ5Ht7SxNNWv13eGdeJxIClylkFXW3XAg8gLowOo_3RtxUbu7MV0rDtbbvB1Yjd1w2DKW1KMGXycnNtgMbBUSsSDlOTbHNb7CCnZI38HWoYaSK4GLPKis2_b636XCKydJ38XKrWv6xR8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=XPUzDtTv3GIb8nsGUvhXIvXqIacN2_nMi_QioguETXmy2Q3FvcqXMOxbHFMx3hIBNolmPg0FJ2xNPWb-mCjEkqegnNyIQ1a2YApEnWzJIpe5mfhQ3aG6ypD9YguVjqGRjbyelHS_mbVqEpJwhNrWjDl7eiikW9dQb6q8kehEILrkdzmVRuZ3AFM28cTEXaiSLrXeGmLAQ6JgqNzE5J0mmnTTl9KkpmjLOpF__SeZO28EqRvxA8AkFMG8C4oSwalpAHLmmWEuNZPC9gJaDjLwFGYko0vvKGW1UsalpMpSfT4WpOhrglsC9PQBkWfP3TpCNqWpTsvac7lguV-XskiuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=XPUzDtTv3GIb8nsGUvhXIvXqIacN2_nMi_QioguETXmy2Q3FvcqXMOxbHFMx3hIBNolmPg0FJ2xNPWb-mCjEkqegnNyIQ1a2YApEnWzJIpe5mfhQ3aG6ypD9YguVjqGRjbyelHS_mbVqEpJwhNrWjDl7eiikW9dQb6q8kehEILrkdzmVRuZ3AFM28cTEXaiSLrXeGmLAQ6JgqNzE5J0mmnTTl9KkpmjLOpF__SeZO28EqRvxA8AkFMG8C4oSwalpAHLmmWEuNZPC9gJaDjLwFGYko0vvKGW1UsalpMpSfT4WpOhrglsC9PQBkWfP3TpCNqWpTsvac7lguV-XskiuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=EFhaWvq6B2f8yl0q3YQrdQeFWkSEfCjsdtgW00m_cX8Jfu7BNsqWqfeP3r6q1jAIx9WtdiAGezUOT1SR7gB5JJNXwtOLYrUDAZXQlWZJ7ts3TYVLa_Z9fLXSl2BoSKMwP2Alh5nQzGlpdaIRASTgNAcfEjh_kw8OzTVwvoSNWedJsNQ0b8RFoJCXXJQZ7qGNgXM-0xo5c0Y1ERoSET8lPLDCvj3L7HBFd19VbOX2M_EVaNKP6bVjLmx1YLkYA3q7Pzcn0RmrBEcb1fXj6WqdAf36sBufH6HeKz_ZNW_e8QoCOLO6AKYcSRee15tWTLxv6CEj5wvAKVycARJlfIGXYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=EFhaWvq6B2f8yl0q3YQrdQeFWkSEfCjsdtgW00m_cX8Jfu7BNsqWqfeP3r6q1jAIx9WtdiAGezUOT1SR7gB5JJNXwtOLYrUDAZXQlWZJ7ts3TYVLa_Z9fLXSl2BoSKMwP2Alh5nQzGlpdaIRASTgNAcfEjh_kw8OzTVwvoSNWedJsNQ0b8RFoJCXXJQZ7qGNgXM-0xo5c0Y1ERoSET8lPLDCvj3L7HBFd19VbOX2M_EVaNKP6bVjLmx1YLkYA3q7Pzcn0RmrBEcb1fXj6WqdAf36sBufH6HeKz_ZNW_e8QoCOLO6AKYcSRee15tWTLxv6CEj5wvAKVycARJlfIGXYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=TIGtM4PvKY2BmhhePqPc8-tUEsruAMmLQN2SyFB8gchz4IAoItAvORdg66MaqoQqDpv81RhhJ44lqjAG8I5QW7wuJFjdidvEdfPQs2clFA5C7NGlXMKVV6w6dYiKoWIik6No2GnMF041hvHWRyrYhB7rB9FlLrTst4yRE7CpwH1uCEu7TDRBUHRzaVoII7P8UQ_H-wyTGjWf_MIu0ZCAZNM5vFTnklDcm2DRE9q0yrjOpU0Le5aFE5T3U7URE823h9ykVHK6ECVwjKwMfJjFeES0-FW5vdY8wejumEMxpm3UTWqzcXZH06rQwLxuwLDdJs4DNJXq_unzDbqHyou_ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=TIGtM4PvKY2BmhhePqPc8-tUEsruAMmLQN2SyFB8gchz4IAoItAvORdg66MaqoQqDpv81RhhJ44lqjAG8I5QW7wuJFjdidvEdfPQs2clFA5C7NGlXMKVV6w6dYiKoWIik6No2GnMF041hvHWRyrYhB7rB9FlLrTst4yRE7CpwH1uCEu7TDRBUHRzaVoII7P8UQ_H-wyTGjWf_MIu0ZCAZNM5vFTnklDcm2DRE9q0yrjOpU0Le5aFE5T3U7URE823h9ykVHK6ECVwjKwMfJjFeES0-FW5vdY8wejumEMxpm3UTWqzcXZH06rQwLxuwLDdJs4DNJXq_unzDbqHyou_ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=bn1_pfzfabDvxVMsFZ3iNejmVIOvENaXegkmogtLxfLMb5qPFF-_louVYjEW0S7_L0JOsq8o-SiVTbjX687DpDeQKUH65qXfefnoVqqpHHee_xWS_T8UB76m7kVFP0AcPzBJFQSa_InpRsiZ8Ka0eNOTIenbnxiZgUB73F8VZNSxfUnc7--cUuSVSWbuocRs_d6OhfbuwTxiW5Tb9G0uTySFsVIaKVEQT-spXRhFBwP9YphqHuIOZnK-DtxdmyGZUTKctvASXCevmm4CSbM56ovRr1JLlAKfYrsHG6ZKFvZizGojj38D7f-nY_wi9fx1r-bXDMfx6MjViTmt5WXntA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=bn1_pfzfabDvxVMsFZ3iNejmVIOvENaXegkmogtLxfLMb5qPFF-_louVYjEW0S7_L0JOsq8o-SiVTbjX687DpDeQKUH65qXfefnoVqqpHHee_xWS_T8UB76m7kVFP0AcPzBJFQSa_InpRsiZ8Ka0eNOTIenbnxiZgUB73F8VZNSxfUnc7--cUuSVSWbuocRs_d6OhfbuwTxiW5Tb9G0uTySFsVIaKVEQT-spXRhFBwP9YphqHuIOZnK-DtxdmyGZUTKctvASXCevmm4CSbM56ovRr1JLlAKfYrsHG6ZKFvZizGojj38D7f-nY_wi9fx1r-bXDMfx6MjViTmt5WXntA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=c-TxCEkRzaXV78d7a5z7Hw_nydutD2fcsyXxz7IrCkCydB-Aw8wciS5zg2u0GWcyjy8h3LiMdd98IVWgtQcQj9g2fRLG6l5ULKQTG3NGEMxUs_GTF4_K_b_-SbbRjx2YGTOrMQ-9MZCrpUxfTQ4eQ0zuAoV9yclVX4wdoFAS9Skp7uVFr41w2IUcWNkwmSco3d7TF5GLEHXMnxvZ2OZ4r7DRkwLtHUFZJLUncBWWxMeRFvnCoY1ioVCUEJtWs7Z5eLEgnSN5_i7CR6qWtEKvUP0txPXA9g9XWPli0i1GwIAwlUR4kZKk1BG6zHMDSCQ5gNEc-dttUp_diwr74PFo7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=c-TxCEkRzaXV78d7a5z7Hw_nydutD2fcsyXxz7IrCkCydB-Aw8wciS5zg2u0GWcyjy8h3LiMdd98IVWgtQcQj9g2fRLG6l5ULKQTG3NGEMxUs_GTF4_K_b_-SbbRjx2YGTOrMQ-9MZCrpUxfTQ4eQ0zuAoV9yclVX4wdoFAS9Skp7uVFr41w2IUcWNkwmSco3d7TF5GLEHXMnxvZ2OZ4r7DRkwLtHUFZJLUncBWWxMeRFvnCoY1ioVCUEJtWs7Z5eLEgnSN5_i7CR6qWtEKvUP0txPXA9g9XWPli0i1GwIAwlUR4kZKk1BG6zHMDSCQ5gNEc-dttUp_diwr74PFo7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=EVk9o0FC39ZURjGV1HFd-_BgUnAqRT8z3zGRYz4QDNsLaVKVamraqzLA-NOaKijbNtqS_IJ0y7oNI05vIyk6_9ZsOSG1kitQllBlBqEO7soICJRkPsdC99sh5Ynxdl6DrCDUQ8fvziuBeOaFSCdbYCK1WyOPcq21FN62gLmg75oOCtIZ1VOvNEGRtRWf21K9rGOoTYG066jSGOEC9pSvw1Y8nm7C5LPExvRv3R2NZxJTFlpBGwgTkVazBFDC0vBa5uMLOreiIda-RHbFNIOcWUSlzMB9K_O81lENTXkTN5mEpnppX1Rn1N9feiUwS_47-PijO7lRYKeCdATRgBqLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=EVk9o0FC39ZURjGV1HFd-_BgUnAqRT8z3zGRYz4QDNsLaVKVamraqzLA-NOaKijbNtqS_IJ0y7oNI05vIyk6_9ZsOSG1kitQllBlBqEO7soICJRkPsdC99sh5Ynxdl6DrCDUQ8fvziuBeOaFSCdbYCK1WyOPcq21FN62gLmg75oOCtIZ1VOvNEGRtRWf21K9rGOoTYG066jSGOEC9pSvw1Y8nm7C5LPExvRv3R2NZxJTFlpBGwgTkVazBFDC0vBa5uMLOreiIda-RHbFNIOcWUSlzMB9K_O81lENTXkTN5mEpnppX1Rn1N9feiUwS_47-PijO7lRYKeCdATRgBqLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=HqiXFgrw7vshKQv3L1VXjibyYfGjI5wRGM_4DP8WmYBNq2mfb-OOYwOOlpQRXJ2zAIVH-vkv9ax_2zBITDLFkqvbHVISE7i2wWIFdhWdhbljtNG70pBu9-_itLQpzVMj8lDwB5hHXNzY-XcWXqTxXEov1YE2KCWDyRlNYOAorNbRgSDRRZi9CqLOwwo_jF_zDHBHuZLYZGAMDym_tTjJMq4YMkBTw_6o4EH9avPV_t_mFKoJgwNUPNpaCbUw1kwxEUjAJULVpbfTddZMeSYBtkDQ9jZoNbMUbH-i2Z1wuxCZlCu3NRVPrN-WEO2hj45noM7m9umO3q1YE1emNGqwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=HqiXFgrw7vshKQv3L1VXjibyYfGjI5wRGM_4DP8WmYBNq2mfb-OOYwOOlpQRXJ2zAIVH-vkv9ax_2zBITDLFkqvbHVISE7i2wWIFdhWdhbljtNG70pBu9-_itLQpzVMj8lDwB5hHXNzY-XcWXqTxXEov1YE2KCWDyRlNYOAorNbRgSDRRZi9CqLOwwo_jF_zDHBHuZLYZGAMDym_tTjJMq4YMkBTw_6o4EH9avPV_t_mFKoJgwNUPNpaCbUw1kwxEUjAJULVpbfTddZMeSYBtkDQ9jZoNbMUbH-i2Z1wuxCZlCu3NRVPrN-WEO2hj45noM7m9umO3q1YE1emNGqwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=DrRltzLgcVb6730u-pjciqjeclVpeqdBNAukX4j_9wWsGuRu-5hJLr4JbTnvz4J1kzwVNcNopRTh9GLpO2QfnEm2jgzAjd_y8V2vTcO4teT5HvUsGzVUqbAyZt1eoo-0zLpAuDzl7hC7HDY0k2n6NDVbCxwvGw-ohaXpBxvDY5y6yZ7YvhU_EngJk7JI1kdSwZmdagy-n5vwKvBcNQIIWkOq0ocyT290rPQS6Ff2NJ95uD14QOJRrYId2F0uIXbmkthOCPBNFcav4Qfww4fTWFgXQDUg80NqNUQREvqudjQexR4d2W7skM6UJUJ1XVmuKCTJKILBM1b9eljubaTLAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=DrRltzLgcVb6730u-pjciqjeclVpeqdBNAukX4j_9wWsGuRu-5hJLr4JbTnvz4J1kzwVNcNopRTh9GLpO2QfnEm2jgzAjd_y8V2vTcO4teT5HvUsGzVUqbAyZt1eoo-0zLpAuDzl7hC7HDY0k2n6NDVbCxwvGw-ohaXpBxvDY5y6yZ7YvhU_EngJk7JI1kdSwZmdagy-n5vwKvBcNQIIWkOq0ocyT290rPQS6Ff2NJ95uD14QOJRrYId2F0uIXbmkthOCPBNFcav4Qfww4fTWFgXQDUg80NqNUQREvqudjQexR4d2W7skM6UJUJ1XVmuKCTJKILBM1b9eljubaTLAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=V6_GHeLnsYV_ll4IW34q4M9K14mJ43zIqF46kUWYfEVPkF6DnIY0-ZYkX4x6zNqTtfWWuqGSdF74VeFbj2cmTy3cRpC92nOaONOYx-6lYSZz6PIdSKCiVOXxX7JcrgIeWSTB7trGuviHH01sXCzBdyjOmXLMAxgIrcWPmhKKb_HLlztJPiVzo0Q3RDhtV7t2BYnpwu9GfytVK5CGILfbA7pvtbBqerIILbzGeRbIiAwS3BeqIxUnYXQ5MsMMT-dy0FblplizVwAnMkSgvz4qhcLOKQ1ipF19HSQr3HyvHewC7XRIUA6R4Nej44PhtDvK_Z966q6fx0mnEZq2eV6POg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=V6_GHeLnsYV_ll4IW34q4M9K14mJ43zIqF46kUWYfEVPkF6DnIY0-ZYkX4x6zNqTtfWWuqGSdF74VeFbj2cmTy3cRpC92nOaONOYx-6lYSZz6PIdSKCiVOXxX7JcrgIeWSTB7trGuviHH01sXCzBdyjOmXLMAxgIrcWPmhKKb_HLlztJPiVzo0Q3RDhtV7t2BYnpwu9GfytVK5CGILfbA7pvtbBqerIILbzGeRbIiAwS3BeqIxUnYXQ5MsMMT-dy0FblplizVwAnMkSgvz4qhcLOKQ1ipF19HSQr3HyvHewC7XRIUA6R4Nej44PhtDvK_Z966q6fx0mnEZq2eV6POg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=poeVOoetinhP8G8RZIHTU8CIMVBjohel5QRIJFrMoWenL5yZ_Ibvy-gr17jExzaqNWyyfmdln260pWl1GzEqchzoJFumyAEtN6jSHZEUWpBqwjydPn_rzj9zXaioqE8EOcXjG4LdsXumxGMOJa76GBFhJ2Z0ZJqRQNak6az-54eR6FC9IlCLBHR7D70bTDSg1s_5D4SN-EfjslSeaHJwZKJj3uq2fgsYHZjjyZRKdft8T27cV_Lla85xCX4wudGznE4ie9NamUwSOI8DjxMKe75cr8YT_gI-QkbCOdy0k2ZyUuXqHslpgGCbVfDpcqf-zW3ONHghAfZSW70JTLa3Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=poeVOoetinhP8G8RZIHTU8CIMVBjohel5QRIJFrMoWenL5yZ_Ibvy-gr17jExzaqNWyyfmdln260pWl1GzEqchzoJFumyAEtN6jSHZEUWpBqwjydPn_rzj9zXaioqE8EOcXjG4LdsXumxGMOJa76GBFhJ2Z0ZJqRQNak6az-54eR6FC9IlCLBHR7D70bTDSg1s_5D4SN-EfjslSeaHJwZKJj3uq2fgsYHZjjyZRKdft8T27cV_Lla85xCX4wudGznE4ie9NamUwSOI8DjxMKe75cr8YT_gI-QkbCOdy0k2ZyUuXqHslpgGCbVfDpcqf-zW3ONHghAfZSW70JTLa3Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGAf_Zphl0AvVR2dBwVT4sNF7YHZ5tg9Tsatkulk5huAvUOywPXqIhVxOJD0Bvr3wOS2ChUNAfhAAPXyLZFtARdKKikadaitEWcrdd4hqoul0CvE0fuXe-Pkk59ZoLXqzuSzCtcPybbIMGv6GQkwKCY10AUMGlNDwxeKAo5FbhLR5x-A159KcvWcKXkkxHdqphcq91vVZBFshJAej9g5d-gXoIEepOYsJ36cgb60_tjiO3C01SJI89JR56B2Jm8owJnEYSK3EyPHjxvh1ka9ZbPLkqCy00DfMvY1WXbOLtfs1mXw-YM5cSCtYeXSxYV_ryMqew9XHT69OYFU8swIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqTYbib9AN8jgN6WVyNFQ8vfC9Xv5k555u6fjP9DfJ-KPVHlxINtnP8heSDQzyZo0EhXTT1gjERUVoqMfqc3gNgw9yGSORgvMD5wFfx4J-1gCmRtdSamBynI1zw4GFNBmAL0C0vStXJwK5e4Oc32upWieCqlMfqzRT0ARIvHw7f9BCuHEK7pK9P4jtnAZaZYkkJQJt9ULgwd45gSCMJgMQmQ7eQvHXKM10z0dDH3Ptq9qCSxQt_mo_b-e9XdWHp2RZ0TJLnv1WrmsC5HCZYLIicpKp7HEo3vDS_8Mc9xn3COcn7NbuiKsrz6pZGjG344I2lffWGDt5VJ87ehHpd_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Qwx3G9aWVPRL3WaG4ZpyhL0EV3LTdB2YYECafj7z9xZBMIR3exNHQwj3bTDzKh4CEaoFm5M5leR8ObryoC1XK6RoGUp_85Ag_WypkpE94xoD4LLj9QJdc85ToxwDrHFGJMWSXdXXG7ne6_ObXdLe3PfDHnpGxLUQFe26rns0ZG-UUx-zHT3cpBHVex0V6hZ03mzLfSqdC7uGnBUAFfWsh7GQ-V2iJ9cF9tZRbp2OCfb9G-MLGyKSs0rHVaDwqpVkDioevkIxGyA8YzYTYw5DfG1Ch-4faCVnjnS7XXGsa5yqJKS8xbex-ZJx2i2rmKCEwfFhiemqrZkWolvPo4aRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=Qwx3G9aWVPRL3WaG4ZpyhL0EV3LTdB2YYECafj7z9xZBMIR3exNHQwj3bTDzKh4CEaoFm5M5leR8ObryoC1XK6RoGUp_85Ag_WypkpE94xoD4LLj9QJdc85ToxwDrHFGJMWSXdXXG7ne6_ObXdLe3PfDHnpGxLUQFe26rns0ZG-UUx-zHT3cpBHVex0V6hZ03mzLfSqdC7uGnBUAFfWsh7GQ-V2iJ9cF9tZRbp2OCfb9G-MLGyKSs0rHVaDwqpVkDioevkIxGyA8YzYTYw5DfG1Ch-4faCVnjnS7XXGsa5yqJKS8xbex-ZJx2i2rmKCEwfFhiemqrZkWolvPo4aRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=DfNOn3muWLuHqp4KWdxcBFgmqKRgDZrFgU7qsNdmuXEnD4XEojDyt4HI2buSXy2cxL_60iOz6T3G8BPAJCnqpJmBaFehvBv-NO-dRs1MlsvQb6RRnX_PZoRuVXTgBMntTQ7NL7Y3ec9nkFEQ-313RRzMX-_IB8eXCTcUh95feLQV9wu3-KAeGmTIrlVezTjpoYbJxfaF7vrE5ZE0caZXv0TYyy2kprkXCJ1IjG8Gm2LLm9DjTsd1U21R_8orjr-Uo1qYs9Yzq5qssjczbe5Fa0_VMFUz_0_cnO6i-ugS5ldTuVZTbDDb5a7BjLCW-gqLC2npj-FO6B54yvbDnRiyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=DfNOn3muWLuHqp4KWdxcBFgmqKRgDZrFgU7qsNdmuXEnD4XEojDyt4HI2buSXy2cxL_60iOz6T3G8BPAJCnqpJmBaFehvBv-NO-dRs1MlsvQb6RRnX_PZoRuVXTgBMntTQ7NL7Y3ec9nkFEQ-313RRzMX-_IB8eXCTcUh95feLQV9wu3-KAeGmTIrlVezTjpoYbJxfaF7vrE5ZE0caZXv0TYyy2kprkXCJ1IjG8Gm2LLm9DjTsd1U21R_8orjr-Uo1qYs9Yzq5qssjczbe5Fa0_VMFUz_0_cnO6i-ugS5ldTuVZTbDDb5a7BjLCW-gqLC2npj-FO6B54yvbDnRiyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=WTXfys9utTBvsANe-yK3HD_3DE4LVu3uhB3LbZL6R0Vi-PIDMCI7inmo1Hd6StClBULAwuw4p4jvf1Q1IbWIH-QJFccZ6B8Pr6bFgJJTV5D4NtviNSjDuLmxA7vd3gf9jzf19U2Ehmv7VtOX1uMslRIRsNfi4q6KggNL8zIQThn5fqx3oCXnnluThiLBIu2-2H98oMVWMbMsDvxjPAOnaf0zSBzHkj7zdZSgptceNpbnwGm9yMmae48x9L_FFm7V2oojK6-43rqOR1dbEGAfC-5ZbCUbqe0McTNeJNsOiUO7s7nyRy71wCJLTo9BN3R13DiWJWTEXik254Pv8blWMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=WTXfys9utTBvsANe-yK3HD_3DE4LVu3uhB3LbZL6R0Vi-PIDMCI7inmo1Hd6StClBULAwuw4p4jvf1Q1IbWIH-QJFccZ6B8Pr6bFgJJTV5D4NtviNSjDuLmxA7vd3gf9jzf19U2Ehmv7VtOX1uMslRIRsNfi4q6KggNL8zIQThn5fqx3oCXnnluThiLBIu2-2H98oMVWMbMsDvxjPAOnaf0zSBzHkj7zdZSgptceNpbnwGm9yMmae48x9L_FFm7V2oojK6-43rqOR1dbEGAfC-5ZbCUbqe0McTNeJNsOiUO7s7nyRy71wCJLTo9BN3R13DiWJWTEXik254Pv8blWMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=D3lNMfUh2qsJ7Rkrj_10DSZiEmoa6zXSQoKGQToDsYeXzfcBmhq84ZDWGCDsKNI5fEJwDhBm2AdZ2ZGoeH3yvwLFGGwQqR0kUD_uRLLVVeu3FKh-we_2Neb--gQg9f7nki56HXDXb41Nv3hFCLlKksCgGOXbSNu5bCkXdx8rZ9OtBmqdlEY3X8nGl-Jg-gqQzNZxa5rGEGiDeDVcINN_2fHexxVbh8s8rGY7irkiHIG3dRPL-6gvc3_cPYXuTJnz4oxKlFN2Qm7XAqSs7nDWOjNS8W0GRphveo4gZMnDbMh2TCWo2P19jDOZ9KrLmeQ4P043se7QCGMePFuuSFWsIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=D3lNMfUh2qsJ7Rkrj_10DSZiEmoa6zXSQoKGQToDsYeXzfcBmhq84ZDWGCDsKNI5fEJwDhBm2AdZ2ZGoeH3yvwLFGGwQqR0kUD_uRLLVVeu3FKh-we_2Neb--gQg9f7nki56HXDXb41Nv3hFCLlKksCgGOXbSNu5bCkXdx8rZ9OtBmqdlEY3X8nGl-Jg-gqQzNZxa5rGEGiDeDVcINN_2fHexxVbh8s8rGY7irkiHIG3dRPL-6gvc3_cPYXuTJnz4oxKlFN2Qm7XAqSs7nDWOjNS8W0GRphveo4gZMnDbMh2TCWo2P19jDOZ9KrLmeQ4P043se7QCGMePFuuSFWsIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWp4od3kcJs8f7ULsQOWq_zxRNXZY4i3J2PJazXiyK7yETbZPiAlJ3YOar1pjwjFPC3rWYirJFrTF9QrIjiSogG5gnDAUgyjm7Ir-RGgYmnE-Qw9AdcDNFUY-gCe3NtMutRKf9Pl9ZXc7UNVYKaiGkWjvYnbx7pXizW1qMUTh7atRvuhqHLDkkAP79bPjZzwIw9ktpzlKSFnhprNwOlrdZRv14W_5fKctoEoyUiiIosxn9iieOPj8zcTy7QGgyP9xj3dMjSuIviBJvH8A7bZaaXZRJe9jekMVTXp_ts8o-aeQtwuw7n_8VbU7FYt-oP6zfW0wi-ysFPWroIhvF7msg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
