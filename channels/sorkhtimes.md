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
<img src="https://cdn4.telesco.pe/file/Ct3vlM5ZkRlciPe6X46QAEjK6Yif7oItDdqsjlBRqr2L-_ViRb4XD77L_OHh_-b-J4pLMb8uF8TKKm8ktQIwvQDPPXgYM9ILTWLXzIucH-a8pjqnKfVK_9HaBcpVghPqTP8OLmzbGhOAlelXofyutbjgJJWylribDuBbHvb_XqUh_iq-tt1jFbTgZR8jzb2MWUe2zI4o9A7tnEbtMstPkjFZvnUEmpECOLm0NivQixJLZv8ymoYQFUI76q3gK6KLah-znfSOr2znsohrOTs9FYHusODzE3XF5wr3sdYq2dufqOHMAyZUvshSfW_QNGVag509WBDfHCvMFuumg5PNTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 00:57:33</div>
<hr>

<div class="tg-post" id="msg-139924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 455 · <a href="https://t.me/SorkhTimes/139924" target="_blank">📅 00:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139923">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
تارتار قصد داره که به اورونوف تایم بیشتری بازی بده تا اعتماد به نفس رفته این بازیکن برگرده و این بازیکن رو دوباره احیا کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 548 · <a href="https://t.me/SorkhTimes/139923" target="_blank">📅 00:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139922">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎦
تحلیل مدعیان اصلی قهرمانی در لیگ از نگاه وحید هاشمیان؛ شانس اول قهرمانی به نظرم پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SorkhTimes/139922" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139921">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
براساس گزارش منابع خبری، مسعود پزشکیان با درخواست زنوزی بدنبال حل مشکل سربازی علیرضا بیرانوند تا پایان جام ملت‌های آسیا است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/139921" target="_blank">📅 23:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139920">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=DZE4M9xaRhL6IJGVzOBkipizsY5OtGxW2Bvoo1ETuxvsYeWl7ookK2Me_u2de2KBDGyE9k7qWvL0pfX0ndInxcSc7LaKNEsujaEeJlj6mI_SGPiC1gWbeXSD7k9BrVCYZk6UiGGSUVZIxTAQULp8CTYZGB9NFg4oFurvHvQkexZ1IlisKMKmfFJisBMT0DkENOWAYjlK97ZOg1NKz0GRDzjcUljT9cZnoTUBgS-38KlDwkjxR3S6X-3novtxP9NS3xW8rIrI12ECz2J3xQA4el2SrsbAjVRcnPrMKEicHjmZUtBF7jJMc_xWrYL5KyN3vIOVm9E_rU8V5zZp9qTY3rnlwt15QX-BEuCtdVNu2sWpNMeoShxyuUkb5HxaGjseL-GtKZVwxayarI8kSdDYulDdr7w8nBrpThSI4_lu2uv515LErkfEZKSZAsMtwD9qe5Lsx_f1qaNPGFjTTxI7YOQ6erQdwJK_DlkFopXisMEJ4Kthg4uQqxymHfTPH6OafXKuA8EemtSzwlRuVbFXgYFu9OxBzgG67jzfsFuSJdSSm597lD2cFNQRpb8iKlJjSB1xTUJ3RdoE6ppifcMc9LKV3zd1N-bJMRxj3ZbuCj4wB7AvVvncOTP_-8NfW6CGZ65jGRFBDdyufHEmbdl14RDP8bprgfFikx32uy2QCKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=DZE4M9xaRhL6IJGVzOBkipizsY5OtGxW2Bvoo1ETuxvsYeWl7ookK2Me_u2de2KBDGyE9k7qWvL0pfX0ndInxcSc7LaKNEsujaEeJlj6mI_SGPiC1gWbeXSD7k9BrVCYZk6UiGGSUVZIxTAQULp8CTYZGB9NFg4oFurvHvQkexZ1IlisKMKmfFJisBMT0DkENOWAYjlK97ZOg1NKz0GRDzjcUljT9cZnoTUBgS-38KlDwkjxR3S6X-3novtxP9NS3xW8rIrI12ECz2J3xQA4el2SrsbAjVRcnPrMKEicHjmZUtBF7jJMc_xWrYL5KyN3vIOVm9E_rU8V5zZp9qTY3rnlwt15QX-BEuCtdVNu2sWpNMeoShxyuUkb5HxaGjseL-GtKZVwxayarI8kSdDYulDdr7w8nBrpThSI4_lu2uv515LErkfEZKSZAsMtwD9qe5Lsx_f1qaNPGFjTTxI7YOQ6erQdwJK_DlkFopXisMEJ4Kthg4uQqxymHfTPH6OafXKuA8EemtSzwlRuVbFXgYFu9OxBzgG67jzfsFuSJdSSm597lD2cFNQRpb8iKlJjSB1xTUJ3RdoE6ppifcMc9LKV3zd1N-bJMRxj3ZbuCj4wB7AvVvncOTP_-8NfW6CGZ65jGRFBDdyufHEmbdl14RDP8bprgfFikx32uy2QCKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/139920" target="_blank">📅 23:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=IlPv9dRWAt1UmVObQ_XNSDPGtL2j7AFHDWiDcSou8bv9yfb6g-wgcEwABW-OqieBkp62DV8K-KRk1alVLDekx4DoqmS30N3K1ialWyC4LOLOzDIPCn9el8oTkartnAb0Q6OZHb8-TNoGrIaEn_OfDjHI0fe1vyfUn9eBPDrgi4W8rJRGyyumF_2Tbtboo_OFAflI9hyPN85R3h_u2XIaaq4LoUCQzWgfxJ8zpgyxefcd2cakDfOjKcP9AlbYcSSza7qdwsV5fpC7Wabb7pMMmjPqlYJIdviqW0j6f929GQGE1dz6GXI38t98rZNWOZOmpzCcFDL0TNIh9wp3X9ZYymAohGxGHYN8SGDCDCgJrhDueknbxZAp7O7VHfdGHcON5UiFQJkFZBdsg9U6ZEWlr8PP-7QToo81lBILxbk6Hj3zEiUve_VynAhwPaSBC6F1LlEKKaLDiap-s5Cny-2zfJftkF8Fy2u8jWErNzlNkntMfYoryZxy8HeKsZicj01wbUWS1yQQRi81zq4kIa59ZrPc7v13JnCHDl1EYEssJsqB137ZZurK4pycbBdisjGduxR3eGEC9h8rzvq7NuzVhe4LJ_6YDy0kC8s0VeaLrqof8cUdQyZg4VoevUctwiUj_8yabLboDEYaj7gvEAuJExLNfodbqbcBXKq6bWmwOm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b780a05a54.mp4?token=IlPv9dRWAt1UmVObQ_XNSDPGtL2j7AFHDWiDcSou8bv9yfb6g-wgcEwABW-OqieBkp62DV8K-KRk1alVLDekx4DoqmS30N3K1ialWyC4LOLOzDIPCn9el8oTkartnAb0Q6OZHb8-TNoGrIaEn_OfDjHI0fe1vyfUn9eBPDrgi4W8rJRGyyumF_2Tbtboo_OFAflI9hyPN85R3h_u2XIaaq4LoUCQzWgfxJ8zpgyxefcd2cakDfOjKcP9AlbYcSSza7qdwsV5fpC7Wabb7pMMmjPqlYJIdviqW0j6f929GQGE1dz6GXI38t98rZNWOZOmpzCcFDL0TNIh9wp3X9ZYymAohGxGHYN8SGDCDCgJrhDueknbxZAp7O7VHfdGHcON5UiFQJkFZBdsg9U6ZEWlr8PP-7QToo81lBILxbk6Hj3zEiUve_VynAhwPaSBC6F1LlEKKaLDiap-s5Cny-2zfJftkF8Fy2u8jWErNzlNkntMfYoryZxy8HeKsZicj01wbUWS1yQQRi81zq4kIa59ZrPc7v13JnCHDl1EYEssJsqB137ZZurK4pycbBdisjGduxR3eGEC9h8rzvq7NuzVhe4LJ_6YDy0kC8s0VeaLrqof8cUdQyZg4VoevUctwiUj_8yabLboDEYaj7gvEAuJExLNfodbqbcBXKq6bWmwOm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚽️
❤️
🎙
انتقادهای تند وحید هاشمیان از مدیریت پرسپولیس: وقتی سرمربی دارید چرا به او احترام نمی‌گذارید و رسما اعلام می کنید که دنبال سرمربی دیگری هستید؟ همین می شود که بازیکن هم به سرمربی احترام نمی‌گذارد
🔴
همین جریان و اتفاق را هم برای اوسمار ایجاد کردند و این رفتار اصلا حرفه ای نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/139918" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=fqSgNPmeJXf8PPVj-kQSVjGy6dNKCLA9uJDUn5YcAB9BXb2GYyPZqJA3yzXIjY_YmC2VVQvQBDgrE55htw5fUx3Kt_rzMyRS9_0tsmZr-ItbDZXiuYozYXxnzBqI6StAKldFO52ecPPu0Y1Fzz1D0Z5rarFsiAokvu975eVviFHh_r8WfeR9YcpiJoExPfunKfpZxD02pFTTj5Dgu5yAYTyUmS2Fa9tuwJDJhp5dS8dJwZCzgtUtbNBmbEVwWazMbc2mFqTqejPmd4qiHNDFC3kQ089NrG42vpMFA6n5mC5ijyRTwyAz61eQdIPOrGg7gDGFsaRPvGjaWxv34yLa-WMuDTiswDHeNuAgTOPTX27PfWCTprUbqEYr8HVaGB1g5OP7IhoNZ7Bae7z2XXGQyPbaaViy6URph0f6okoLXWZKJLfC2JnbR1ifufgKark0pFH1qUoNR2YMmtzCzhiYOcU3YDYmoQYToXbqpnXTKbkEXrJb5YAvQI-JNGMHTZ1eNrCDnjSLU_hFXko-I-Am2ciPlGAYAjh9_7l9EqbyOonrLhCwV3aDscQ-D35yDFGz8-hH5WJsJODQnSGng_oWA_4t7biJG3H1s6toWjo8RU9vDy2FqaxJUaHpg6k4MODo4fwoHX6hLgKYfGmOeH4JueZGCOB5NhKkZynYWUj16Lc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c45fdbb36.mp4?token=fqSgNPmeJXf8PPVj-kQSVjGy6dNKCLA9uJDUn5YcAB9BXb2GYyPZqJA3yzXIjY_YmC2VVQvQBDgrE55htw5fUx3Kt_rzMyRS9_0tsmZr-ItbDZXiuYozYXxnzBqI6StAKldFO52ecPPu0Y1Fzz1D0Z5rarFsiAokvu975eVviFHh_r8WfeR9YcpiJoExPfunKfpZxD02pFTTj5Dgu5yAYTyUmS2Fa9tuwJDJhp5dS8dJwZCzgtUtbNBmbEVwWazMbc2mFqTqejPmd4qiHNDFC3kQ089NrG42vpMFA6n5mC5ijyRTwyAz61eQdIPOrGg7gDGFsaRPvGjaWxv34yLa-WMuDTiswDHeNuAgTOPTX27PfWCTprUbqEYr8HVaGB1g5OP7IhoNZ7Bae7z2XXGQyPbaaViy6URph0f6okoLXWZKJLfC2JnbR1ifufgKark0pFH1qUoNR2YMmtzCzhiYOcU3YDYmoQYToXbqpnXTKbkEXrJb5YAvQI-JNGMHTZ1eNrCDnjSLU_hFXko-I-Am2ciPlGAYAjh9_7l9EqbyOonrLhCwV3aDscQ-D35yDFGz8-hH5WJsJODQnSGng_oWA_4t7biJG3H1s6toWjo8RU9vDy2FqaxJUaHpg6k4MODo4fwoHX6hLgKYfGmOeH4JueZGCOB5NhKkZynYWUj16Lc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
❌
گلایه وحید هاشمیان از احمدی و مدیریت اسپانسر اصلی پرسپولیس؛ صحبتهای او حرفه ای نبود
🔻
احمدی گفت که هاشمیان نبود دورسون و امیری را رد می کرد و این حرف در رسانه حرفه ای نبود و میتوانست شخصا با خودم صحبت کند/ صحبتهای او فرار از مسئولیت بود و در شان یک مدیر نبود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/139917" target="_blank">📅 23:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/139916" target="_blank">📅 22:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
روشنک :
✔️
✔️
باشگاه‌هایی مثل سپاهان، آلومینیوم و.. به ما اعلام کردند که اگر هفته هفتم را برگزار کنیم نمی‌توانند بازیکن در اختیار تیم امید قرار دهند.
✔️
✔️
فقط پرسپولیس درخواستی برای لغو بازی‌اش در هفته هشتم نداشت.
✔️
✔️
نمی دانم سازمان لیگ چه گناهی مرتکب…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/139915" target="_blank">📅 22:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j80qXwjKEWBqfa1LpAJs5PTHkAdW5HdfsGuaONKZPRiO_t59LEnExsxNL32PzA_08n0LUai3H3nFkQPTl9S0uGqEfPC6O7o995hXNKSe6-JNH7rhbZY3P1VL1PpxGooXUzz-dPoNiQBU9Bs91J2RrnFTaLZjlp_zy6LI1mZiKtu4dwmRF6-06pwmphWeHIhaB7F-bgbV6Kw0iE5UY4DuC5Q0d46F2VJMqK1b_VIUe7494RFaZPpwombag5YYZ3Dr8PAZrB_oAehqyMru3RWUAwnjqLYbOO6VRnJpbm6D7g0t33H4Es42ZvEZ8s14cX1sxo9glMLGkAMbzxGlTqXmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با وجود لغو دیدار برابر خیبر خرم‌آباد، پرسپولیس امروز هم طبق برنامه تمرین کرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/139914" target="_blank">📅 22:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=uWDmg2R-PkKQYAdlTaUFIb8OV6uaKKj--dB_SivC4bcpXAZvrPlkeqPfdnwQwcjwbiO0OHSITVxyqvxQbGEFx7JWjpl2zNV4L0PRE6UhWB_J-JWT_pRPzybpndmXNb70nH-ZeJYjSvOSCsUzKQrrK6stCCyPT1j-ez8Yf75NvpYm2BIe_lakfAv_vXfmqUKVr6fPUfxZYRHPqgoOYwqfm5H_tTJCjMPVE1EHlQsl0jW509GjKgYLWHiIBRZ7WQ3FTaEklgwghsvoxG4j0YYIM5TRfjyXG-mmKk8NvcOdD6vAE7JplaLe1RwXbw85fhgigXawk8G5t6S92P-SGjrPqDJ86CGYECM_Na72GeDz40nqV6oGURCdpsl_Obz356xfNBZNKCVtfVzJdc0M_7_gYlEjNV_I9ds8zBTSdZqwySvH_xek3t2Zem2lr1NKANu4ovNQncIGVzYZQVsMAXYIsepU_Sco2WmorCMaeyCco6_K2NUWDgJzIWDRxE3OEXgQiFSYxjmi_8zMFAp-VCqJSmyX5FvVxGJ9dLcJm8I2kYocDPXNKxMPwuFO2Oqd3o1T_gCxFfc4eKKuNGHvfN-4CBtQ166scAkyg1vNZfBUwfdSWxqP525iyi08pLiWOK1D8-rvno25PfjL8rFpvLqP67JJM7C5xLThogT6kcswvw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b227fb7993.mp4?token=uWDmg2R-PkKQYAdlTaUFIb8OV6uaKKj--dB_SivC4bcpXAZvrPlkeqPfdnwQwcjwbiO0OHSITVxyqvxQbGEFx7JWjpl2zNV4L0PRE6UhWB_J-JWT_pRPzybpndmXNb70nH-ZeJYjSvOSCsUzKQrrK6stCCyPT1j-ez8Yf75NvpYm2BIe_lakfAv_vXfmqUKVr6fPUfxZYRHPqgoOYwqfm5H_tTJCjMPVE1EHlQsl0jW509GjKgYLWHiIBRZ7WQ3FTaEklgwghsvoxG4j0YYIM5TRfjyXG-mmKk8NvcOdD6vAE7JplaLe1RwXbw85fhgigXawk8G5t6S92P-SGjrPqDJ86CGYECM_Na72GeDz40nqV6oGURCdpsl_Obz356xfNBZNKCVtfVzJdc0M_7_gYlEjNV_I9ds8zBTSdZqwySvH_xek3t2Zem2lr1NKANu4ovNQncIGVzYZQVsMAXYIsepU_Sco2WmorCMaeyCco6_K2NUWDgJzIWDRxE3OEXgQiFSYxjmi_8zMFAp-VCqJSmyX5FvVxGJ9dLcJm8I2kYocDPXNKxMPwuFO2Oqd3o1T_gCxFfc4eKKuNGHvfN-4CBtQ166scAkyg1vNZfBUwfdSWxqP525iyi08pLiWOK1D8-rvno25PfjL8rFpvLqP67JJM7C5xLThogT6kcswvw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
به مناسبت خداحافظی گولسیانی، یادی کنیم از گلش به مس تو دقایق پایانی که باعث قهرمانی پرسپولیس شد و باسن خیلی از کیسه کشارو سوزوند
❤️
🔥
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139913" target="_blank">📅 21:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
فراز کمالوند، سرمربی تیم خیبر: الان که پرسپولیسی مخالف لغو که سه ماه پیش اصرار داشت تورنمنت 3 جانبه برگزار شود، در حالی که همه مخالف بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139912" target="_blank">📅 20:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤩
🤩
🤩
🤩
🤩
🤩
💬
گولسیانی:
⭐️
من تو تیمهای زیادی بازی کردم ولی یه تیم هست که وقتی یه بار داخلش بازی کنی و بدرخشی، دیگه از قلبت بیرون نمیره. نمیدونم چرا ولی وقتی یه بار تو پرسپولیس بدرخشی دیگه پرسپولیس میشه عضوی از خونوادت. من رو نخواستن ولی من تا ابد عاشق پرسپولیس…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139911" target="_blank">📅 20:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFeZzTaZ99wg4nQxW3oMYe2Wgf-YOn5V1lNY8GOSfofe9gJhJrt7JNPNfvW5JMFMjqjONNV6HhZLyWqT1fBSynKCE7Viky2I80MVRMqcFELHzmgrxC6KFY6c_Gu0iuPXV_1b0afJR0bgvqVsxRYuPCewdqzBLLgs8wa4qxSEQFiK28Zd2ZcnOxc5xhRHNuMQv332X38ZcOGP9vqawl6_z-lVzFNp_p5gpdjZJRNXMRZZDl2U2Y7216v6rsBoGQIKujeMAB9Rh7709i6BzfB2NMHKImXvvDHKckaC9R21Hgr-KWoKuXsvMT-YkIiAzY2AR_S8zckkavI0Syc9LcbE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽
سالاری از پست مشاوره مدیرعامل پرسپولیس استعفا داد.
🔻
محمد رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال که چندی قبل به عنوان مشاور پیمان حدادی مدیرعامل پرسپولیس انتخاب شده بود از این سمت استعفا کرده است.
🔻
سالاری به توصیه مهدی تاج رئیس فدراسیون فوتبال برای توسعه رده های پایه و کمک به فوتبال از تاریخ اول شهریور در پیامی به حدادی اعلام کرده که دیگر به عنوان مشاور او فعالیت نخواهد کرد و از این سمت استعفا داده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/139910" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
فراز کمالوند سرمربی خیبر: سازمان لیگ تصمیم بسیار درستی گرفته است که بازی‌ ما با پرسپولیس را لغو کرده است/ من نمی دانم سر و صدای دوستان برای چیست؟
☹️
☹️
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/139909" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
فراز کمالوند سرمربی خیبر در گفتگو با ورزش سه:
🗣
باشگاه پرسپولیس ابوذر صفرزاده را از ما خواسته و ما گفتیم در شرایطی این بازیکن را می‌دهیم که حسین ابرقویی را بگیریم. همچنان هم در حال مذاکره هستیم و به نتیجه نرسیده‌ایم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/139908" target="_blank">📅 20:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arGDh_jfFVhBX2vqG8RVR6xdY73Bcz7onUsYzXMWxD1V7tDG_UZHCt_LdmIZYhNlhOz8dLzNurN3ncKRym_muajPVBVsgTYAAzs8YX3NQgyFLzaZ3gsML2Gs4iSfdfXtXxX6kDaYpQBsgiaXNx1daYFQu3-qDrFZmA8RXm-Xc7L1NOP3IM5O4HEKHtjGLly4Zp_c8Gwp4N3j7THLvCcDe5q7wcRiXMQJ6J05twhZ6vvqcori-95aSlwzmAudL7XmeV4D6klWAnQtWfiLj5yiLOAmqgy0iyImssKepP6G5j0m8tEDYnt1ETNWCP1tSDVG_7N5K3RzOOkPIZaC65o8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبردی نزدیک و تاکتیکی؛ والنسیا با تکیه بر امتیاز میزبانی به‌دنبال فشار بیشتر است و سویا امیدوار به استفاده از فضاهای دفاعی حریف و ضربه در ضدحملات؛ دیداری که می‌تواند تا دقایق پایانی کاملاً پایاپای دنبال شود.
[
سویا
🔴
🆚
⚪️
والنسیا
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/139907" target="_blank">📅 19:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139906" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUTR3T3cCUqBipph6nIsspCa2BUQaOc6ia6iOQvWvfLHaPsQPQmxwwKQtkIABStPr3fFWE77Wb_R9fVM6258k_0q8cchHI0vxojzfIQiYiRbthfnOCCG3IJOlgoRC-ZOGpECmaQPlXqiTgz_uA6lRiwL4F9eLNTPyEzHmvuWASOwH6w-IFo3DLlZkovqUS5JYDMoA3MvJIvrmG0sLWGJ61_kbxTBi6SHGwdwHTcP8SJQyR5JdAvCOAb-bo8BngfF9A-uv6CCxcrGFe8wyud1Q7e6v64Wkt2ZpEUo-MZSZ8CGVOLSdHDhB9WIGNpDC7PCQ25KpfBxADz3qz3Rm2lPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139905" target="_blank">📅 18:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139904" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139903">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
مهدی تارتار بزودی و بعد از بازگشت دنیل گرا به تمرینات درباره‌ی ادامه‌ی همکاری با او نظر میده/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139903" target="_blank">📅 17:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139902">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139902" target="_blank">📅 16:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATQaLdt8XcnymJwJl4XAE903qiffVXUP3JCIdk717kPtAPHKsbFuiO5K0zgS8j2dkAsWPSG7ynfo6or6TCkX7rn6OrzLyOVa3LqW7FkPCaHQxPiv3DvrD5R65a7YwKo1N9647TRFVerFAcaIaYgEGNiCYfTYdYO1jNyWX0h7xw3sFyg2_XLK4aiqWJrdAjN_gF4yt5sMG-nPagj57sF3Fhxb5JNY6bmjWbCEC45aRfKg6pInzsmNyt_BEMGRP2xvxSS3IlbT9hh7Z0iH35t1JoY-UlTg6NuXj3HW8aU8Zwb3_49aBCy7i_nrd_9gGXwCIgNDgaPfNBoBkgzMpc3WlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
پوریا شهرآبادی ۱۵۵ دقیقه ۲ گل
✔️
شهریار مغانلو ۶ بازی فیکس ۴۶۰ دقیقه ؛ ۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139901" target="_blank">📅 16:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139900" target="_blank">📅 16:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139899" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
🧤
علیرضا بیرانوند نتوانست کلین شیت های خود را ادامه دهد تا رکورد هشت کلین‌شیت متوالی پیام نیازمند در لیگ نوزدهم، دست‌نخورده باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139898" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
فووووووووووووری
✔️
اسماعیل کارتال سرمربی فنرباغچه پس از مساوی مقابل رم در هفته لیگ قهرمانان اروپا از سمت خود استعفا داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139897" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
✔️
مصدومیت یاسر آسانی از ناحیه فسخ غیرقانونی قرارداد و غیرقانونی بازی کردن وی برای این تیم هستش و بعد از بازی با السد خوب میشه
🔄
🔄
این مصدومیت در لیگ مملکت با کمک فدراسیون برطرف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139896" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139895" target="_blank">📅 15:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJJ1VhEc365UPSOyYZ-C8xSg89HSYgw9VGupjtIdO8F9yD0ZLvQQVJiX_DY80GUlNF_xD0u93pG6OfUZtNKD7-DPSgLOnED5lDLJGnqS9kOroYJcEy9ssfibSRV5VDb4_g5QuDNeanvdluOgDQMwaY2r2uMQoQEi9_xDeJfNWLgsfEWLvvPsiwTJRMKW8DXRRkac0WUbkq9rCuL0YCWe4THH0huOD--rOkIvUwTf3zG9vB4BXRncfGvSF18sE6qSFCj5pZ4dFeO7LNdfjeZqChOMWyjjfs7_9HeuJbiWEWV67wc9rUEbQEQ-QeUUaxPVemIhHM-3K9D6ktS1gvMWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139894" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoRhJ_HJYPUfE_gVKdbPswyR4oPzCg8lXKtkHT3JlBYfm4QVl0TY04lCeMSU2wUBkirGYpkD7ay_02mmOxJQ8FwsQZgK8t9zqsdrAlS1yBkhbEe1so4HdS9hU-CmPHDxEHhA5y_1zKeFh5AYZ-QE3mhbDV5kTWOUvIpRAqvSpflaaUoaVXF25yZ1uUOEXzIokjeYPmrIlTujUP7sIeHzgsguns5I-qoRfbS_O3dq4GI5j8vhc5yKR9j7LI9VV7I-7ustBis1SUUz9jh-K5Jt1g7ws_0cwMzKV3G6U__L28vZR5nvV83KAM6q51_lkIwSg_knPHtDnUyChDvaIdq4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان نیز پیشنهاداتی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139893" target="_blank">📅 13:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
جباری: اورونوف قطعا مورد اعتماد ماست نیاز به زمان داشت تا با تفکرات تارتار هماهنگ بشه ما هم وقتی دیدیم پیشرفت کرده برای تشویق فیکسش کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139892" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139891">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⬇
علوی سخنگوی فدراسیون فوتبال: پرسپولیس دوست داشت بازی‌اش لغو نشود؟ باید بگویم از آن طرف خیبر درخواست داشت که بازی‌‌اش لغو شود
✔️
✔️
خیبر فقط یک ملی‌پوش داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139891" target="_blank">📅 11:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139890">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDR4bucjfNCH6969Xqj8DrJbQGJwMFlF8JCX7diQa03VJzKhFt7hoEad0XDAQJPNEmybYM17bMtn2HQJPb-zIvfugvAowDKhDK-z_6OD1k3jlHCYG7Rm7goLS4l7meByX4KP5LaPwy4PAOZ9g8sbjMV1CjvZUxXC_x2ztNJ2dsgwmaMluBd5shmqqRK6PKm0zFRuLf738Vo30jWOvN3cFcdNwaPy7snZ-9z_kQgydctSF64MKpjnjuEfu1feVHicIlDpbDdi-lEULxo60IjrbPmtyZ2Q4uC-qesjZp-gYJdKllAPO-w4ijJkF3uzVcmJ4xnK2sT8JkGj8i-tp9cfCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
از دیروز و با آغاز دور جدید تمرینات پویا اسمی مدافع وسط 17 ساله که همراه تیم ملی جوانان در ویتنام حضور داشت در تمرینات پرسپولیس حاضر شد و اکنون پرسپولیس سه مدافع آماده برای جانشینی محمدمهدی زارع در بازی با خیبر ( در صورت برگزاری ) در اختیار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139890" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139889">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139889" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139888">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
آسانی مصدوم شده یا از ترس شکایت جلوی السد نمی‌خوایید بازی کنه؟ ///اعظمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139888" target="_blank">📅 11:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139887" target="_blank">📅 11:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
۵۷۲ دقیقه مقاومت بیرانوند برابر رقبا
✔️
✔️
علیرضا بیرانوند از آغاز فصل در ۵ بازی، ۵ کلین‌شیت پیاپی را توانسته است به‌ثبت برساند؛ اتفاق ویژه آن‌که بیرو در آخرین بازی فصل گذشته تراکتور در لیگ‌برتر مقابل گل‌گهر هم توانست دروازه‌اش را بسته نگه دارد تا ۶ کلین‌شیت…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139886" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
رضا جباری مربی پرسپولیس :
✔️
من با علیپور صحبت کردم و قول گرفتم که بتواند امسال آقای گلی لیگ برتر را به دست بیاورد و این مقام را تقدیم به خانواده‌اش و هواداران پرسپولیس کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139885" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139884" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=ioAVIaiOOsAFYI8fsW2yViIQ20dbrhbjtBFfD4AnB-Wq7Gg5eMFcvV5VgNg8xxy1W5ffHcSSlriohlsCT7SrMWzsrhDbej2YTOi95fj97MURANu06upgGeFyHvC4CXYl7KAbP0Fr8p-s91zaNGACEMWWPDyJBw0-PlODfsPh1ghv-LeVth1QouosTNCmN_6X4jr3Ilb2e10Dk-iDDODFp-hPvwY78E7DU98UsQhICLCXKJPxMb3-H5glomDLuDGfuX3xlM9IHhj_trLddPiCF016_u2BrKnA2NxRgZJ-gdjQ-GF2Uw2ZzuwBPy6cPRbpLInf0it62_IbOU0QZQG0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b893ef9367.mp4?token=ioAVIaiOOsAFYI8fsW2yViIQ20dbrhbjtBFfD4AnB-Wq7Gg5eMFcvV5VgNg8xxy1W5ffHcSSlriohlsCT7SrMWzsrhDbej2YTOi95fj97MURANu06upgGeFyHvC4CXYl7KAbP0Fr8p-s91zaNGACEMWWPDyJBw0-PlODfsPh1ghv-LeVth1QouosTNCmN_6X4jr3Ilb2e10Dk-iDDODFp-hPvwY78E7DU98UsQhICLCXKJPxMb3-H5glomDLuDGfuX3xlM9IHhj_trLddPiCF016_u2BrKnA2NxRgZJ-gdjQ-GF2Uw2ZzuwBPy6cPRbpLInf0it62_IbOU0QZQG0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حردانی: آقا سهراب جواب تماس هامو نمی‌ده
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139883" target="_blank">📅 10:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139882" target="_blank">📅 10:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139881" target="_blank">📅 09:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R13O5ZoJOM85FxC9WjztdsLmP5ei5TVdd8vGd4PWxoApfdpgb-fbjI0_Kkc_sx0cfWeEmR5kPQW1L4UVgvnZujwWRiE5qWvz212WKAmPYBOsL9T1KJg4BEBYw8gCAKl2V8CvCclqr8Fo_xwHe7WVE2NLGD48baStvyWmInC3lNUT0KQgQK-DCIf2wMjsRTHo9xKXvJyl39ahJC4Ilk9DFUFPTESZfqp-YlwbvM1BAKoBXm9_W8MDoFZMAhuuQ9_QAVikW9KHbZZnExOt8RghZ8c3rRbs02zFnQk3I9bRp81jqbsVHwFT0nVHc8gmc0kzRC5cCbdemEijljLKBdQoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سابالانکا مقابل پگولا؛ قدرت سابالانکا برابر بازی حساب‌شده پگولا. ریباکینا در تقابل با گاف؛ نبرد سرویس‌های سنگین با سرعت و دفاع. دوئل‌هایی نزدیک که تمرکز در امتیازهای حساس تعیین‌کننده است.
🎾
Sabalenka -
🎾
Pegula
🎾
Coco Gauff -
🎾
Rybakina
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژ خودتو انجام بده و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139880" target="_blank">📅 01:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139879" target="_blank">📅 00:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139878">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=rI8mUW2K9HWJ8LElr3WkExH9eL1yEP5JOetzCWe3FyV_tCiBn3CO2agOAK492f39Ri7JIGbNvsCmHeKhXNUpMedXuzR06KEZ-mAKjAZOR6GbpgdwY8hoUiMYIiaV3gycYy8Ebi3Wh3Ua82RwZDJsTEQHyEJQnRUdTabJRxDP7MjHHihfdPBoIJ5DlvejYn3AC7yulijA5hoT6ze3EnmXNKbErvl4kAP0u1Z4TZi6ZnSQPtiP3LJF-RDPMfqWcOs3vlMVKhjwyOyuO1ZBQCpO36vlwEqZQkuGwkuH475SbEsGOWfGUZ0IsBJiR7r1Z663rp6Pn0wbau4h-HepCBYsczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7d8a9c3c.mp4?token=rI8mUW2K9HWJ8LElr3WkExH9eL1yEP5JOetzCWe3FyV_tCiBn3CO2agOAK492f39Ri7JIGbNvsCmHeKhXNUpMedXuzR06KEZ-mAKjAZOR6GbpgdwY8hoUiMYIiaV3gycYy8Ebi3Wh3Ua82RwZDJsTEQHyEJQnRUdTabJRxDP7MjHHihfdPBoIJ5DlvejYn3AC7yulijA5hoT6ze3EnmXNKbErvl4kAP0u1Z4TZi6ZnSQPtiP3LJF-RDPMfqWcOs3vlMVKhjwyOyuO1ZBQCpO36vlwEqZQkuGwkuH475SbEsGOWfGUZ0IsBJiR7r1Z663rp6Pn0wbau4h-HepCBYsczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
دقیقه 95 بازی استقلال و پیکان، یاسر آسانی به یکباره بعد از سوت پایان بازی مصدوم شد تا شایعاتی مبنی بر مصدومیت تعمدی برای عدم بازی در لیگ نخبگان به اوج خود برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139878" target="_blank">📅 00:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139877">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139877" target="_blank">📅 00:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139876">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luTqVNkaJ3L0phwAKs1277pULUBjiz5m2EZRAF5tTtZiwt9akGTLB5_Xyqet-hj53bainwkG5a0vZbfssqInHpa4q-XxnMIHLBvWP0sRwj0gcaHDnMYj4ABUYaF3LVe-vya54Tn2sOCC7wueWfYZumOUkCqhWKnDjQBCAzK3S3nxfESMzvHq6tmuPXQsVOlgvhazElIZrKT2H6ygyubAAKA5lGeQBzC4b3haHv0TMCltbOOU5ozBNcYfj5Tr7akLWH2XU63nLW5jKI3FP2RfpFgMOAkbm1FVcer6CNapVx2wCFtAjz8AHoBvLg-czw39dZwn1TBrohgrSY2dll8wPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
جدول لیگ بعد از بازیهای امروز
پرسپولیس با برد خیبر می‌تونست به صدر بره ولی آقایان رنگی تصمیم گرفتن خودسر بازیها رو به تعویق بندازن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139876" target="_blank">📅 00:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🗣
🗣
ورزش سه: یاسر آسانی به علت مصدومیت دیدار برابر السد قطر رو از دست داد
‼️
السد قبلا اعلام کرده بود آسانی بازی کنه می‌ره شکایت می‌کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139875" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139874" target="_blank">📅 23:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
#منهای_پرسپولیس
✔️
✔️
استقلال ۴ روز دیگه با السد بازی داره و السد تو پنج بازی اخیرش دو بار حریفش رو شیش تایی کرده به بار چهارتایی و یه بار سه تایی فقط خدا به دادت برسه استقلال :)
✔️
✔️
شما فقط مراقب باش دوباره خاطرات العین و الوصل رو تکرار نکنی قهرمانی…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139873" target="_blank">📅 23:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139872" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHyuwPKooIRlowkQBU-SemvIDynT8Jm7xKf8NCRXofmfWoSvY64ma2uqiYRNQom09m-4tCsVSO6fUPJ5HZzIJkOQY64nkjckUM4zVGLuAXVtAgQOsvsOSUcjtB2XEFln1fwGWfkJoGKCUmhT0LN3mjSBm2jxg7sH-xpsma3EBMTMrvYOOjo69uYE9WmUFSM4Kgxjod5RWGwinMBDbXE7GdwMXsf8veRna2EX7N2m8zarKgMMpvUoPZRqvHkuCe0aBy9FDvS347O152R6lb4kIXCSsBN9dr1mhlCv_ol4XyMvoJ6UPJPg8mdwZcP3oYIdRt6Udm1-2ca7tAharyHdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پس میگفتید که استقلال خوزستان ضعیف بود که ما چهارتا زدیم؟
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139871" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
✔️
اتهام بزرگ خداداد: فدراسیون پول آپدیت VARهای لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139870" target="_blank">📅 23:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
خداداد طلبکار هم شد
❌
❌
بعد از فحاشی ناموسی و اظهارات بی شرمانه به امید عالیشاه، سرپرست تراکتور:
❌
❌
دارم میرم مشهد به یک زمین چمن سر بزنم؛ فردا از باشگاه گل‌گهر کسی ویس منو ضبط کرد در جریان باشید/ پسر بده فوتبال ایران هستم؛ شما خوبید  «سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139869" target="_blank">📅 23:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139868">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
بازگشا :
❌
سازمان لیگ بهمون گفت بازی بخاطر یک ملی پوش خیبر لغو شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139868" target="_blank">📅 23:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139867">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139867" target="_blank">📅 23:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139866">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdRIO2j0ZYY5zgc1E58dkU5iOIqKSl07aRVhoOAggcrDTyiNn_taaorFMn7VTmpig7xFNI4N6VKKr8GjeFM6FMg0ZKZev3dK24dG-mMSacSMNgyAQi2dhU-yBTuDNrg214KOGlFRdVBx6lqCChy6SYSLqId5P-fMHSkI0wlOKXb0k0JG45CLV5pK8wqOju9ZTBQGCxfdZ_koEsTYJfrD6PKX1nAgV_JAnjdBCmC-ZtkwO3MW0gw262PgO3NSWeS7TJOPIyyoDWZt6YQGpl8vS1guBovWCYyM3ujSH_OsmqG1enQ-AdcydU6rl5-QcMJzJ02z8N_isx5lbo7FgYm4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
روحیه بازیکنا که عالیه امیدوارم در نهایت بازی با خیبر برگزار بشه بهترین فرصت برای گرفتن سه امتیاز و رفتن به صدر جدول
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139866" target="_blank">📅 23:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139865">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: تصمیم لغو بازی از طرف خود سازمان لیگ گرفته شد و برای ما عجیب است که چرا دیدار تیمی که فقط یک بازیکن در اردوی امید دارد، لغو شده است.
✔️
✔️
تمرینات و برنامه‌ریزی پرسپولیس همچنان بر اساس برگزاری بازی با خیبر ادامه دارد.  «سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139865" target="_blank">📅 23:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139864">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
⚪️
⚪️
⚪️
⚪️
❌
⚪️
⚪️
⚪️
⚪️
⚪️
⚪️
لعنت به بی برقی ...برق نداشتیم شرمنده نبودم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139864" target="_blank">📅 23:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139863">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoPC12S-soF-gV5oFr2X3Hl0oIP7XJnhTPKAMwUNW_xRvbc9hQcTEiub6XNMELTTN7MwK82xI5yWynnnA7i8DijpM_HhNDB28q35SgCuQtm8CpUrOrsm0ylEXuTWt8IUHDHTkvWnriZADgjkkRykTbN8TnV_ofiQPHIWbCX2C_RvHQX4WtYh3WbtKEhiyBib2jCYYw6jtjFRwpY7Alfkm4ieiOgvHDznKiUwamSneGDu6bDVNKa6yHQwmJEWQLf0zPcTX_SrX3en6dyl2iQ77RdhpO2xgGymmFyL2yNvJ3EpoaiJksuK7a1ErI06hwVy5CGEcvA5eH0Rdl7GssZknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Bayern -
🟡
Bodo Glimt
⏰
Tonight 22:30
🏟
Allianz Arena
🔵
بایرن در برابر بودوگلیمت؛ بایرن برای جبران لغزش‌های اخیر به دنبال یک نمایش مقتدرانه است، بودوگلیمت اما با فوتبال جسورانه می‌تواند دقایقی دردسرساز شود. با این حال، اگر بایرن از همان ابتدا ریتم همیشگی‌اش را تحمیل کند، مقاومت نروژی‌ها خیلی سخت دوام می‌آورد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139863" target="_blank">📅 21:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139862">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139862" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139861">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
سهیمه پنالتی کیسه واریز شد...
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139861" target="_blank">📅 20:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
تارتار:سازمان لیگ بیجا کرده بازی مارو لغو کرده...ما هیچ درخواستی برای تعویق بازی نداریم و میخوایم بازی کنیم...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139860" target="_blank">📅 18:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139859" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139858" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139857" target="_blank">📅 17:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139856" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139855">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139855" target="_blank">📅 16:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139854" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139853" target="_blank">📅 15:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139852" target="_blank">📅 15:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139851" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139850" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
با اعلام سازمان لیگ، ۴ دیدار از هفته هفتم لیگ لغو و زمان جدید برگزاری آنها متعاقباً اعلام خواهد شد.
✔️
ذوب‌آهن - سپاهان
✔️
خیبر - پرسپولیس
✔️
ملوان - فولاد
✔️
فجر سپاسی - آلومینیوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139849" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔔
🔔
فووووووووری
🚨
مهدی تارتار با لغو بازی با خیبر مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139848" target="_blank">📅 14:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR3-Cs-Jj2mlG2qi1sm9jfsxXb6mND86UHG1Kffbu_zD_tzXMu9oxk9vcIPKbJk4r15pHlgt1CYe4v6huYXb5ikyFrCTQoKcnqC-O5IzAmyqmc7i9OafpveW27xMOoQ6lnDETzVLr9wiOi6y9tbMtlsnaAnTckS1yVpJwHn2Xc_FhEQOWX--iIIHFedy8YJsk7cLNqErYASLtiyoLwiBxV6Zr6iVV3Qsz0y8HZJK7MPvpJjZNefH3_-Pkk7hXVachdvXVDel8CkvnmziRi80UwFJQDHgjehGh1-GuUWkzNxv8cEiq3Fve2opi5d3mPf5f0ai9gzWU1PRRutw5kNZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مونیخ؛ بایرن آماده‌ی شکار بودوگلیمیت!
⚽️
بایرن با مالکیت و فشار هجومی بالا، شانس اول این دیدار است؛ اما بودوگلیمیت نشان داده مقابل تیم‌های بزرگ با جسارت بازی می‌کند.
انتظار می‌رود بایرن از همان ابتدا برای گل زودهنگام فشار بیاورد و برتری کیفی‌اش را به نتیجه تبدیل کند.
[
بایرن‌مونیخ
⚽️
🆚
🇳🇴
بودوگلمیت
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139847" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
پرسپولیس-خیبر فعلاً طبق برنامه
🔺
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر ارائه نکرده، با توجه به شرایط موجود، این دیدار طبق برنامه قرار است یکشنبه برگزار شود، مگر اینکه در ادامه تصمیم جدیدی در این خصوص اتخاذ شود  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139846" target="_blank">📅 12:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
یحیی گل‌محمدی: فکر نمی‌کردم لوکادیا روزی در جام جهانی مقابل آلمان بازی کند/ او یک بازیکن حرفه‌ای بود/ از روزی که در تمرینات حاضر شد مربیان از نوع تمرینات‌ش راضی بودند/انگیزه زیادی از خودش نشان داد/ لوکادیا یک مهاجم شش‌دانگ در محوطه جریمه بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139845" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139844" target="_blank">📅 12:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139843" target="_blank">📅 11:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❤️
علی علیپور:
🇮🇷
🇮🇷
واقعاً افتخار بزرگیه که اسمم کنار علی آقا پروین، اسطوره بزرگ پرسپولیس قرار بگیره. خوشحالم که با کمک همه هم‌تیمی‌هام تو این سال‌ها تونستم تعداد گل‌هام رو به 96 برسونم  ﻿
🔴
ولی حتماً از قول من بنویسید که میراث، رکوردها و افتخارات علی آقا…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139842" target="_blank">📅 11:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139841" target="_blank">📅 11:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
عبدالله ویسی بعد از باخت مقابل پرسپولیس، از سرمربیگری ذوب‌آهن استعفا داد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139840" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
سازمان لیگ به باشگاه اطلاع داده اگه میخواین میتونید طبق قانون بازی تون مقابل خیبر لغو کنید و بازی نکنید حالا قراره تارتار امروز تصمیم نهایشو بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139839" target="_blank">📅 09:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139838" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139837" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDiuvbqoMTW-lvfET2ja3rI3A3DxpsiTI-WCNgjKUvvYMRSvX8lI8WowjdyykrY4UjZ9yexKZYsj-zbJiCgD9okBXea3_bT_lv5AagRRPe6giKspT-EpTyz0ap1098t_PMiW9b7ElW2AHS_wGqOMfY51kuvJsMme5yA422QF2zmYuzXT8B7HFXNK1yXiH5ghvFI1p3cLAgLKflAT8bLUJLDyNHAVEIZYfPNaYbnqoELjHnkeS5SujaZCfN702OArD06unp1JyOkl8r8LmuP2-Khl8rivMACtlm1xl2VsuPt8grGYhD_LcmEoznuOuGxgIKzRD8e2TJVNQ7MAOYMSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139836" target="_blank">📅 09:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3r8s-xv4XBpGo058yCAXW4PL-nyLybHV_qJvitA4G8rbdoOlI8gXkRE7PrpKqevMvjnusjTCGVr0JPbsQe6nY0_muKM01cuUoE33_n_pISxRDSazDqNrZcu_HSFZT_xoaD6EtMSFQVpgcnAjhThBcApW_7r_EE3Nb-xCnkNMaOO-Qa68ooU6x6S5N05JCMIr_7Ja-SOjqMQQNI251DkIb0cqzsNenTFO3ICK0OuKNRgx4e78Ib2rvTGJ26xt6YVk89Ia-vqKaUzVYBYR6U-3Ua621oMN-ZKAj8kmcPblft4a2CMeQT1VLat5lA9sACvjOquuomBJUnKXQa6Gy4ARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال قدرت با جاه‌طلبی در یواس اوپن
[
الکساندر زورف
🆚
بوتیک فان دِ زاندشولپ
]
⏰
بامداد پنجشنبه ساعت
۰۳:۰۰
🎾
زورف با اتکا به سرویس قدرتمند و عمق ضربات از انتهای زمین، دست بالاتر را دارد؛ مخصوصاً اگر بتواند رالی‌ها را کنترل کند.
زندشولپ اما با سرویس و بازی مستقیم می‌تواند ست‌های نزدیک و تای‌بریک بسازد و زورف را تحت فشار بگذارد. با توجه به فرم اخیر زورف در US Open، کفه ترازو به سمت زورف است.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139835" target="_blank">📅 01:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139834" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
احتمال لغو چند دیدار از هفته هفتم لیگ برتر
✔️
برخی باشگاه‌ها از جمله سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند و به‌این‌ترتیب احتمال دارد برخی از مسابقات هفته هفتم در روزهای شنبه و یکشنبه لغو شود.
✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139833" target="_blank">📅 00:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139832" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=AspaC95Hu4fN9RouSRq1YJE5rzEwIpEHbeXFaq1QcpkQuAJamxEzAceJNOlPizVLNNOI2Cp-kpq7Lk0bjxRqXnxmpBfadO1ov82mFhwd9BD6UpB0Lv1I6KrBNt9Jo_ox7S6b07K0E0DM_YHKKLqtIfNNzm3d32Yov6f_Y9SC9AWWSdTevoiTfemF4uM0yrgo1joqsZNnXegQXjUqZxEp6eMaKzXrmYoRqTUDPGq3nvOkJiZ1y_f3PUN4KAM7vHPGQG1UFoLoPuMEeqZqem3AddVvvmXP810bc8LPKOsTxDwa6uQeV7Drsmt7XCNEbili61jJzqtyGDfSc5y08a33hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=AspaC95Hu4fN9RouSRq1YJE5rzEwIpEHbeXFaq1QcpkQuAJamxEzAceJNOlPizVLNNOI2Cp-kpq7Lk0bjxRqXnxmpBfadO1ov82mFhwd9BD6UpB0Lv1I6KrBNt9Jo_ox7S6b07K0E0DM_YHKKLqtIfNNzm3d32Yov6f_Y9SC9AWWSdTevoiTfemF4uM0yrgo1joqsZNnXegQXjUqZxEp6eMaKzXrmYoRqTUDPGq3nvOkJiZ1y_f3PUN4KAM7vHPGQG1UFoLoPuMEeqZqem3AddVvvmXP810bc8LPKOsTxDwa6uQeV7Drsmt7XCNEbili61jJzqtyGDfSc5y08a33hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.»
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139831" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=tyQZr9TaOLy7gOFBIFcF_d_czbcCydh95QBg6oxqjq7BgHRuL3RqmuBGBeyWAIf8v9VojtUBrjYwBJ4nCsJEZyXxPUfAmCAfWhxUyJX9FCsO5vJPfjuGPZa6l_VEWnt9ZWNzgbeRIZyuozpa_gezH3Q4Ap0NsJumv0XxsF6tUNJMSGXPRAaMXa1NSmi1xkdwjO4SX1wt7Pwr1djrHUFSYLNITtdc71gehc5nS_uuYpRgUH4a2uds9bqtpzaOslaF4XEpaXCvtyBiXQekVA2Zgb8v6VFYc_pufrPcC9yQo8efwZA3sVGCd9MP4ogST33V7FB5-1FlzwKcitE45F8wGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=tyQZr9TaOLy7gOFBIFcF_d_czbcCydh95QBg6oxqjq7BgHRuL3RqmuBGBeyWAIf8v9VojtUBrjYwBJ4nCsJEZyXxPUfAmCAfWhxUyJX9FCsO5vJPfjuGPZa6l_VEWnt9ZWNzgbeRIZyuozpa_gezH3Q4Ap0NsJumv0XxsF6tUNJMSGXPRAaMXa1NSmi1xkdwjO4SX1wt7Pwr1djrHUFSYLNITtdc71gehc5nS_uuYpRgUH4a2uds9bqtpzaOslaF4XEpaXCvtyBiXQekVA2Zgb8v6VFYc_pufrPcC9yQo8efwZA3sVGCd9MP4ogST33V7FB5-1FlzwKcitE45F8wGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139830" target="_blank">📅 00:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
پزشکیان پیگیر حل مشکل آزمون برای همراهی تیم ملی
🚨
مسعود پزشکیان، شخصا پی‌گیر رفع موانع بازگشت سردار آزمون به تیم‌ ملی شده و به احتمال فراوان مشکل آزمون برای همراهی تیم‌ملی در جام‌ملت‌های آسیا حل خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139829" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139828" target="_blank">📅 23:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139827" target="_blank">📅 22:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
برانکو: هر روز به بازیکنان می‌گفتم پرسپولیس بزرگ است و نباید معمولی باشید
❌
❌
به شاگردانم که مربیان بزرگی شده‌اند افتخار می‌کنم
❌
بدترین روز زندگی‌ام، روز از دست دادن جام مقابل استقلال خوزستان بود
❌
❌
اگر به عقب برگردم باز هم پرسپولیس را انتخاب می‌کنم
❌
می…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139826" target="_blank">📅 22:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
❌
با اعلام کفاشیان، جام فصل قبل به کیسه‌کشا داده نمیشه و باید برگردون تو غار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139825" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139824" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
