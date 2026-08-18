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
<img src="https://cdn5.telesco.pe/file/r2lH4ZFr8H4chZZ9tMIsPraTLvjab0fQixETX8G4meLDObWwMxf2HHw0OdmDsfpjoMA-fLVEF6wuacjyKNAYpVeqD-S18uUJlUj0kIPa6gvwO_9BibbYmnxtYOHPCMwyx735Ls3hLZWNMSxBl_Vqo45XSPJNXqH2mKN4oqZurRSLCsU9KT9tgy6ox_3fN9jD5uA2WU1FzvKD_mxDlKs2YZ99CLH3RBaW7qQjL6QrWgW3M5ArW8sd6HPzDpG8o5NffgkY86O0L42EIl3qow5lIqpX_8QjfHNy4DMcsZVWGOv6npuxjZxNZlKGUJBAtJMA9suF1b3AFYexfUYMkoLkiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 459K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 11:30:13</div>
<hr>

<div class="tg-post" id="msg-104020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7cbf260.mp4?token=Wgs8VQr4GVvG54aK6tHzxjflUEc7MQscAtqnAD3OlCh4hWCG29YdptvDFAPP3hLus-U_gAqyRCdd2-_4AG6IsyJPYmcLZxfjFd9I6prcxvPuc_JgIW_TgjwITp1fEKen3AsQFQ4EuNKquU0MoWrdw6RyTaGBHftF_u1OGeh-3OEBr4fCCSwulD6pyj_fHnDzOfOkumX-C_Go6_x8fqcFNMqf0bvLOngpc9JX_A4NSFMxyhBE3xbcpS1OjZVEMb4ZmechBorYMeIp_5oCO5mR1wjaUwonaFJY9mTneAUUrm1ktmWmGE72rYHvjM1Ixiud3UywxfhP6rTM0SXpY46l5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7cbf260.mp4?token=Wgs8VQr4GVvG54aK6tHzxjflUEc7MQscAtqnAD3OlCh4hWCG29YdptvDFAPP3hLus-U_gAqyRCdd2-_4AG6IsyJPYmcLZxfjFd9I6prcxvPuc_JgIW_TgjwITp1fEKen3AsQFQ4EuNKquU0MoWrdw6RyTaGBHftF_u1OGeh-3OEBr4fCCSwulD6pyj_fHnDzOfOkumX-C_Go6_x8fqcFNMqf0bvLOngpc9JX_A4NSFMxyhBE3xbcpS1OjZVEMb4ZmechBorYMeIp_5oCO5mR1wjaUwonaFJY9mTneAUUrm1ktmWmGE72rYHvjM1Ixiud3UywxfhP6rTM0SXpY46l5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
وقتی مجتبی‌حسینی سرمربی نساجی به بازیکن تیمش قوانین داوری رو یاد میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/Futball180TV/104020" target="_blank">📅 11:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104019">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwLHozMHjcB7Zjazmw_cngwrLf23SAG-cjLMNsoPFWRul6wHMzPR_twtu2FSD3fVRXVsxu5zans0pvkLRqDVyXWFuZQTuJiIjd06wuLH8HBtZbaxHXX4FTBdwa6fnn5EEGd6uLFJxwrwNpgeoQJ3lCiVSgMKr4GhMx5thJVk6tNjatRfRxLZuRnmmVLoXVOW0wlWfW0cBi0V7siKDLOmjfZzDWLe7BeHr2vQkyp9RnBXu9inMc0n1gY745uorHmR7nacmx81mBop967pW1PN26Hn_oB50GVP00cGxbv5A17dm_AjnwCc8X8bqpG-FtDZ0UzmttTrAlBJWyR6vX4PaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🚨
🇪🇸
جوتا جوردی :
🔻
آلوارز برای بارسا بازی خواهد کرد!
✅
بارسلونا از جذب خولیان آلوارز دست نمی‌کشه. آنها تا آخرین لحظه بازار نقل‌وانتقالات برای جذب او تلاش خواهند کرد. حتی اگر این انتقال تا آن زمان انجام نشود، ممکنه بارسا در ژانویه دوباره برای جذب او اقدام کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/104019" target="_blank">📅 10:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104018">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f82bbb56e.mp4?token=vrHbLVz4EYS8Gzi9QwddyMPuxqG8FrBVRe3S9PVW5tRgCGCsWMuDJVdp6ofpL4Il-9HVswo1B7nbPI7DbYinA4AbWaOGDwxSlaxYO93PLLS-RtrF7vSYcpefvEizG8nxzDLQKG6fDVUr0S-Wb9kLgfIY-BJ28VsP2ElmozBu_xdroeRW8tLc22SltqUVj9g_Hyj1DkV5qDfYksRCvks1mfW-Gz85hpYumGhbK6mYog2ob51GRwLUcuChgyhmWoWbQEQOwwFSUotfIwXgdBtlMk4gRljzJjBNiHu70qu94JiAi4E7ZS0UElF9tMcXdTaOxf7M4GlWLeQcsrQhfM8SKkSspDc3b7J33GGAIRjja71126VVkM5xFpvC-_nZStHDFCn6vCh4x0RkuuhR3WLCl__iwY_xjcrBd0tsVCr3nBwdnfuidA2z99FS2Hkle4Ctxq_cclPgZFSALJRE-WzAPNmTTHiGuKfs-6YTEZzbIOYe9-CZFshK6Gu4w0OPUQK3nTcYPBRp9Sw6eXdXW7qC9F2RamZK9qn5ZazW0IIijfaGfCRN_WarYwZijlORRrioWdGyEXpsLU_fHGTocnMttXvNPMslQFQVETqe9zirITEVY1X4n4aqltk0sciUNm6H27aJU26YJ7MDLiO_DgLH4sc_wKe6ewj6OO7lOr0aEn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f82bbb56e.mp4?token=vrHbLVz4EYS8Gzi9QwddyMPuxqG8FrBVRe3S9PVW5tRgCGCsWMuDJVdp6ofpL4Il-9HVswo1B7nbPI7DbYinA4AbWaOGDwxSlaxYO93PLLS-RtrF7vSYcpefvEizG8nxzDLQKG6fDVUr0S-Wb9kLgfIY-BJ28VsP2ElmozBu_xdroeRW8tLc22SltqUVj9g_Hyj1DkV5qDfYksRCvks1mfW-Gz85hpYumGhbK6mYog2ob51GRwLUcuChgyhmWoWbQEQOwwFSUotfIwXgdBtlMk4gRljzJjBNiHu70qu94JiAi4E7ZS0UElF9tMcXdTaOxf7M4GlWLeQcsrQhfM8SKkSspDc3b7J33GGAIRjja71126VVkM5xFpvC-_nZStHDFCn6vCh4x0RkuuhR3WLCl__iwY_xjcrBd0tsVCr3nBwdnfuidA2z99FS2Hkle4Ctxq_cclPgZFSALJRE-WzAPNmTTHiGuKfs-6YTEZzbIOYe9-CZFshK6Gu4w0OPUQK3nTcYPBRp9Sw6eXdXW7qC9F2RamZK9qn5ZazW0IIijfaGfCRN_WarYwZijlORRrioWdGyEXpsLU_fHGTocnMttXvNPMslQFQVETqe9zirITEVY1X4n4aqltk0sciUNm6H27aJU26YJ7MDLiO_DgLH4sc_wKe6ewj6OO7lOr0aEn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
ویدیویی در شبکه‌های اجتماعی منتشر شده که مرد سالخورده‌ای ایرانی را نشان می‌دهد که سه سال است هدف حملات پیاپی یک کلاغ است. او می‌گوید ماجرا از روزی شروع شد که جوجه‌کلاغی افتاده را نجات داد؛ از آن زمان کلاغ به محض دیدن او به سر و صورتش حمله می‌کند. حتی با پوشاندن صورت، او در امان نیست و کلاغ به افراد شبیه به او نیز حمله می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/104018" target="_blank">📅 10:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104017">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STdwBvMdQaZa1jCZBWu8hFHsb5My-l1L9z09oMnCUYSVmlw7pSbULPuNaTvWzXkx1mHQuDrohmpD99edpVEs8yD_3qpMSojUpiJROlxhiaxX-yuEkHJOJKednusIYjbeSzSnEgwFgTrR2D7td-BZDvpi9mnUJdcbN0tOp_EW3PoNCnYMKjjryb0F65qdBFjEkvdY4Bbj-iY6onQqw9SxTGeDvQA0r4BBp02Zq4Evi8MvP1oV_VJaHOxxFGhsRl3Vw0lmvfWtQs8Vqo-J_aQwYDYErzPCrNw0Ppt_rVSqtydP9Ymh9uLrEmS1PemqROF5iAhI1e5OLg4vKBDEm5oq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
تکمیل ۴ خرید از ۶ خرید احتمالی بارسلونا در فصل نقل‌وانتقالات؛ رویای کاتالان‌ها تکمیل میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/104017" target="_blank">📅 10:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104016">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxDWSTMEiYjPjW8kTHkjWB8KyqOy98D2NGxUIOWoZdXBIlVWIEn9PySNmX86NaYLCzIS0bFo6BJPVkyMtfYPl7qkV3mzQa_QMX-hzICHX-uC73jgMSGbiFP4d-hpjZMo_FsscTpuGUDlUEsuSIuBS6S_b-zUf5u8IAb7uFFY9mgqKPqcvLOu-DTYpgZjuu1_hjwWe__sPx68do_w_pS7oRbj0WpsT7FG9u1o0p6RjSChqt2-Yi-8SYd5m_Ex6Q3q83cKb8AL8aBiXU48zK62bcKzDi51L5xrfq_tmnB--dQ01GNH09ewG0U66IdwyUC9Ovfyt1lH0_ygSfQShfGKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
✅
🔵
نتایج قرعه‌کشی دور گروهی لیگ‌قهرمانان آسیا؛ گلگهر در گروه  B قرار گرفت
🔴
گروه A: الوحده امارات، نسف ازبکستان، الکویت کویت و الخادلیه بحرین
🔴
گروه B: الجزیره امارات، گل‌گهر ایران، المحرق بحرین و آرکاداغ ترکمنستان
🔴
گروه C: التعاون عربستان، الریان قطر، الفیصلی اردن و النهضه عمان
🔴
گروه D: الحسین اردن، الشرطه عراق، السیب عمان و بنگال شرقی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/104016" target="_blank">📅 10:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104015">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bade9483c.mp4?token=frrqveSIAXo-L8s6sthIdc4mVMhfGabUy9xMB0MAyTutR7FENVipyjHe5ZpgdBo8k-2PNEiKh1u2xXPnLhfMVyGnz3O9xl8Hh69mlgT6cNCD7dMOpKSyoH1K3iaDOMCoI81A_1qMMsdntxYUOa7JoDkzOIOO_DFnIZBvgwdbXiD08J2SqDR9YRe5gM_NTUHf371J65kx-OpUbLOGnr1e1IKQ3B15-OPeJUkvkiNuXc4mHXvXoybf8omkuGrIiL9swnIB-7bU2bi7dNEehxIOWSpm_nDHm89sCTaQP335hre2asUWpItjRpdIJAtBCWx9Eu53fyg7XoUPfELQcspSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bade9483c.mp4?token=frrqveSIAXo-L8s6sthIdc4mVMhfGabUy9xMB0MAyTutR7FENVipyjHe5ZpgdBo8k-2PNEiKh1u2xXPnLhfMVyGnz3O9xl8Hh69mlgT6cNCD7dMOpKSyoH1K3iaDOMCoI81A_1qMMsdntxYUOa7JoDkzOIOO_DFnIZBvgwdbXiD08J2SqDR9YRe5gM_NTUHf371J65kx-OpUbLOGnr1e1IKQ3B15-OPeJUkvkiNuXc4mHXvXoybf8omkuGrIiL9swnIB-7bU2bi7dNEehxIOWSpm_nDHm89sCTaQP335hre2asUWpItjRpdIJAtBCWx9Eu53fyg7XoUPfELQcspSYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇪🇸
نقل‌وانتقالات بارسلونا در یک‌دقیقه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/104015" target="_blank">📅 09:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104014">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1d68db4d.mp4?token=q7fiYjDJpgPYBTmwu02L2rG4dA4cMN6sU0nJyN4fuUGfIo9DjNfOdv2BaFyH132kq9Pj-SqROhbLJWBFIJDatAIy_sOb6xqhIphuFjWYhzaVicG7GlphJMeUl8c4rVRyRNWn3iJgSEVwZ7Oni6HLd4rLs-Q8KRp9NrdMaLDJY3hoAbVMQWKvJHmd_M0WDMNyZeQDgXFVp2V_69lGU_3ppnqPg7ODw4N_qaOEkGXh2QTzAaD8gYG9QDKDCZ-0RCvTc-THNH94CNGHd9K3u6JDvIpiU-YVk51BJZtIykWWYi6zOrhBuIqFOT5hB4p9ECFQk7xGrHIGSHuenvS2Tk61PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1d68db4d.mp4?token=q7fiYjDJpgPYBTmwu02L2rG4dA4cMN6sU0nJyN4fuUGfIo9DjNfOdv2BaFyH132kq9Pj-SqROhbLJWBFIJDatAIy_sOb6xqhIphuFjWYhzaVicG7GlphJMeUl8c4rVRyRNWn3iJgSEVwZ7Oni6HLd4rLs-Q8KRp9NrdMaLDJY3hoAbVMQWKvJHmd_M0WDMNyZeQDgXFVp2V_69lGU_3ppnqPg7ODw4N_qaOEkGXh2QTzAaD8gYG9QDKDCZ-0RCvTc-THNH94CNGHd9K3u6JDvIpiU-YVk51BJZtIykWWYi6zOrhBuIqFOT5hB4p9ECFQk7xGrHIGSHuenvS2Tk61PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ شوخی و خنده‌های بامزه مرحوم علی انصاریان وقتی استاد اسدی داشت خاطره میگفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/Futball180TV/104014" target="_blank">📅 09:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104013">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c7d0d9c01.mp4?token=YzWkr20DStJJmN8Pjn1-bP-vR_yGJA_j5DlYtL8frOUKz2eiVD4kQaOB6Evgd3izItHyOw5pfKvw8ETuZvkODygNky1O8XdTkhPX0QXswrKCTMw0EXcAv3omFklkYdQPovmHoPrf4RIsY2QuAiVy_z1eDy3K5hyhZlpOMUrL8FIlhTNcDG5jf7zrJkk3OcmZzgLb7XF6nNZL4v5CvyppNCVXUcPaF1FgJdsFmI7XUJRLiSU2I9lSt75YzpGuHFYt0JboZjevBXGl67D39Ph5-jArL0eIqnqpg0gVQlV_mzk8qZt2Km67XsaoYnBOsT9jrojvFTyibr-zSUmwZ_iIKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c7d0d9c01.mp4?token=YzWkr20DStJJmN8Pjn1-bP-vR_yGJA_j5DlYtL8frOUKz2eiVD4kQaOB6Evgd3izItHyOw5pfKvw8ETuZvkODygNky1O8XdTkhPX0QXswrKCTMw0EXcAv3omFklkYdQPovmHoPrf4RIsY2QuAiVy_z1eDy3K5hyhZlpOMUrL8FIlhTNcDG5jf7zrJkk3OcmZzgLb7XF6nNZL4v5CvyppNCVXUcPaF1FgJdsFmI7XUJRLiSU2I9lSt75YzpGuHFYt0JboZjevBXGl67D39Ph5-jArL0eIqnqpg0gVQlV_mzk8qZt2Km67XsaoYnBOsT9jrojvFTyibr-zSUmwZ_iIKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
افشاگری و ادعای جنجالی امیر حسین اصلانیان بازیکن سابق پرسپولیس
🎙
علی پروین سمت بازیکنان تیم پرسپولیس  پرستو می فرستاد تا از همه شون آتو داشته باشه  واسه روز مبادا
⁉️
مجری : از کیا آتو داشت ؟
➕
اصلانیان: از همه آتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/104013" target="_blank">📅 09:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104012">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab9f085ab.mp4?token=GGpUNn7VM4qvvman0iBt0x_hEbQKAmedpM4nOedNv7pDd9T6dqpVpdYJYlHrBkDbWsGjPXiYPgmQEaJdvgsqkRlVjNPMKUULqPMld0E6gMzoltLFSfQbHJH8kCVWCOtipgWpaq9v3CAPR9x38UWzgR6zdUcmYUl6vs5e9xTqLbSN5t6MmmWul4LeBSdfdMXpH7ub6hKx_otStNNZmMufdBZWomBuo0yZf2tH0Yocklz969TnaPI_oRGgxXXqOdBpCCI5cL8EYeZLXTZgBaTPLnvwI70Py0O1HKUCFRj2zBPJnbsB9l_xhFMqDmy3xApaberRIbXASQM7B59wDhWJFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab9f085ab.mp4?token=GGpUNn7VM4qvvman0iBt0x_hEbQKAmedpM4nOedNv7pDd9T6dqpVpdYJYlHrBkDbWsGjPXiYPgmQEaJdvgsqkRlVjNPMKUULqPMld0E6gMzoltLFSfQbHJH8kCVWCOtipgWpaq9v3CAPR9x38UWzgR6zdUcmYUl6vs5e9xTqLbSN5t6MmmWul4LeBSdfdMXpH7ub6hKx_otStNNZmMufdBZWomBuo0yZf2tH0Yocklz969TnaPI_oRGgxXXqOdBpCCI5cL8EYeZLXTZgBaTPLnvwI70Py0O1HKUCFRj2zBPJnbsB9l_xhFMqDmy3xApaberRIbXASQM7B59wDhWJFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
میرشاد ماجدی رئیس هیات فوتبال استان تهران: این که استقلال به عنوان تیم اول اعلام شده و جام نگرفته است تناقض دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104012" target="_blank">📅 07:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104011">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d4c307b5.mp4?token=gUjFWufYPedEmPoCp9TGWwNVjiAKd5qoxmDM8pSK4Vc0KsSHN_ZUTPUbwBeCImFVrfcJwAOH_0QCmlJANS0aDmsELlyWMwsODpeZQY60G9NzwqvGJLGn_NaoiG5yBstwJiA_o76OqoNLbN_tb2zOcTpUzkN22yWdog_nJH4ORRXWzyDTTTTAcrHt8H9kmptC2B82lmA0P2M8-hZLzbIFOFI_2zVwFSUqPfQC1chakkmBdraoySfWCipOS1BJ_i7DfR3p2-zc-005RPEJjzIedT1YxHLkoxBewfCj6Z2pMggel8j7Q3wsQ8T9jjuyDJeMGQiM91jW04uAoL9oPmA9xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d4c307b5.mp4?token=gUjFWufYPedEmPoCp9TGWwNVjiAKd5qoxmDM8pSK4Vc0KsSHN_ZUTPUbwBeCImFVrfcJwAOH_0QCmlJANS0aDmsELlyWMwsODpeZQY60G9NzwqvGJLGn_NaoiG5yBstwJiA_o76OqoNLbN_tb2zOcTpUzkN22yWdog_nJH4ORRXWzyDTTTTAcrHt8H9kmptC2B82lmA0P2M8-hZLzbIFOFI_2zVwFSUqPfQC1chakkmBdraoySfWCipOS1BJ_i7DfR3p2-zc-005RPEJjzIedT1YxHLkoxBewfCj6Z2pMggel8j7Q3wsQ8T9jjuyDJeMGQiM91jW04uAoL9oPmA9xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
🔥
انیمیشن جذاب و دیدنی حمید سحری از شرایط نقل‌وانتقالات این‌فصل بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/104011" target="_blank">📅 02:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104010">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f966553cd6.mp4?token=nnhmSLn_6ZEx9Rqge-i25zbPFgaeYLCJk1HjXLBFfVSKyVIQ8pVGOPugqcua36dpUkeV1V3l3_caFT-5EJQt9J9PoUSK9A1rD7rd_qs1AZDB9lsuWHkNH-wYn8wLP0Vc_5mvGs8lC-lfOcUaZQSVZ_qG_UXuE0fVF_rUn3vvZNqRa4h16vZLeTdKcGNJkhPhiEvR9f-k3zn1lMvjzdtFR63tE-aEmu-nY9POEFdbaewWiaoLVb5tIWxCvQZSn2Y4CTSDTu0ov6TIHmYmVSvKPgwgXUoN8PkVNFC6b3p6cHRdYjEpHqhEv3ZFCPHEGjmXh5K79X5nKIqtSUQdOag1cCK6_sRuS8n2aC-YGZx3ObZsX1gAZCTQwBB5DGbqDoWxtWwQwJw_qOA8F9CB-cwAVJ90Nuz9SYlEQpARYUG1Dy9dT83ev7nQl5Yj6EntuzohY5BnAB6qH9vYTdM4fRiPC6OtZ8ixidv5Vc_kaFzIljE9y5Iydwdgw_1aZMFjfXbwTXXvjCh2Uv9TtykhREc2obJM0IK6T9XIoE4EECtzxJLBQXnYygVFg5umwHwnTFZ2DlqaoOV1HSnjrarIdW12wxtSu-AKLGnvoI41F6auJEhvvxZI1UgG0R6Vn5SnBcYYEhMRzvxfRp_AZJTWqkIQVhOWrzwnxWHFQugyA1UHBMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f966553cd6.mp4?token=nnhmSLn_6ZEx9Rqge-i25zbPFgaeYLCJk1HjXLBFfVSKyVIQ8pVGOPugqcua36dpUkeV1V3l3_caFT-5EJQt9J9PoUSK9A1rD7rd_qs1AZDB9lsuWHkNH-wYn8wLP0Vc_5mvGs8lC-lfOcUaZQSVZ_qG_UXuE0fVF_rUn3vvZNqRa4h16vZLeTdKcGNJkhPhiEvR9f-k3zn1lMvjzdtFR63tE-aEmu-nY9POEFdbaewWiaoLVb5tIWxCvQZSn2Y4CTSDTu0ov6TIHmYmVSvKPgwgXUoN8PkVNFC6b3p6cHRdYjEpHqhEv3ZFCPHEGjmXh5K79X5nKIqtSUQdOag1cCK6_sRuS8n2aC-YGZx3ObZsX1gAZCTQwBB5DGbqDoWxtWwQwJw_qOA8F9CB-cwAVJ90Nuz9SYlEQpARYUG1Dy9dT83ev7nQl5Yj6EntuzohY5BnAB6qH9vYTdM4fRiPC6OtZ8ixidv5Vc_kaFzIljE9y5Iydwdgw_1aZMFjfXbwTXXvjCh2Uv9TtykhREc2obJM0IK6T9XIoE4EECtzxJLBQXnYygVFg5umwHwnTFZ2DlqaoOV1HSnjrarIdW12wxtSu-AKLGnvoI41F6auJEhvvxZI1UgG0R6Vn5SnBcYYEhMRzvxfRp_AZJTWqkIQVhOWrzwnxWHFQugyA1UHBMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
🇫🇷
دینو تاپمولر سرمربی لانس بعد قهرمانی دیشب: لانس یعنی همین. ما از هیچکس نمیترسیم و اینجا میتونیم هر تیمی رو ببریم.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104010" target="_blank">📅 01:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104008">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEGtcVbJtbYrZLPhRK-Krz3upieSyWGntM7FIxM4o9u7TAT0LFda2VFy4-wvd-4s2OBK1IiGOJe4-gblgtJT4losrzCYZz-rGLL5XIxaCndeNiAqx611R_yci6sZoQgVptIVcQBR6px6NzZRvteu3PVWM2yqLI9JobSp1w3R0EQ5mMK9bOFpExZnoOglk6wcAsuTMWuVtK_0UdKKYDzPa2s2s2ZAe6niGGu6Ywoq0aQgdausfyDBX3xHzjqbyxIsZ-yiVUu4B8asupCA2kx0J-v2lPELdFPIUtco52L-vPgRxpe_iu06GHmkuH_PiJoUCNrlq4XWOsiAlGiQxkGdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7ApCZarxo77EqZn3nhgKuLXsSLYcOR4Nv_VeSTnIfMpsdkH0vu_SC1uME9RAR-_zJ2ek5baeNEvZWpM50XLPL5iUV9vG9U-2SLJ3GYYCnRwLUbF0aBq6S2eF7nDljvkWikz_tg5H7Za5_bzNcSb3QajJqyFMKxURjRiUpJnyjeMM5pbQ2ZRLvQsLp6FlZO5mn-V6FKjOJ9_mIfTCZg9JJU6uC82YZR-XBHqqSh60V_kga1EbASboIJ-PcV6icwXFD0JPy0fXrH2UrBtfrHzgzGKFZLKprl9yLNkk8EQGbpaZWZ2L1EDjRAoTMf52R_L8mu2MmDx5MyCWXaolTBwDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤯
ساعت لاکچری رودری ، مدل
IWC Portugieser Perpetual Calendar
- بدنه از طلای ۱۸ عیار
- صفحه نقره‌ای
- بند چرمی تمساح قهوه‌ای تیره
- قطر ۴۴.۲ میلی‌متر
💵
قیمت:
۵۴٬۸۰۰
دلار ( ۱۰ میلیارد تومن )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104008" target="_blank">📅 01:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104007">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1Q5AGeEz6LkZw3FFzgj-EMClnKiwoG4QcfhDAt4UoiLMdgRqm1Pn1QY9SSse6F3P6DsNRMpHiLUzDjCO7sTXv59nuRRkkhL93xEK7H3CLTzFU0UHrpZUeQauN5E3Gv4S8t9USKV0ROFTaR8bHNsOykJX8POCgz5t8VsVTH34vLnPS-CNN_nP-OF2RgjX71zuC45fRcwrEaZbDcuY4t0e82lKMaXhp5iWCZOZZDNiLUBXhc0TdoAlyKYl7uCRpG1kji3wXrqwUFq3kD3lmnTrDt2ZXQsvJBDWMVa18NFpVlGgogG2_6sPok6ZEGYNz8Yzk256dHYKmG34MhqZdERWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
🇵🇹
پاولیدیس مهاجم وحشی بنفیکا امشب در برد هفت گله تیمش تونست طی ۷ دقیقه هتریک کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104007" target="_blank">📅 01:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104006">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7S2z3JadSITjbnf82eU4U6fxp-CPD1XxiAMJ_Rn7wHtX-H45JJ_-oB0BXFBmDN_4cFJio0X4MAhVZbQPJTS3feee-DBFHeSjUUBYg66av1gqvgomruNjqzC0Li0lKa2m_XEPIAvdjZ3ca_hW5nGm8LD23fGGkppYvediGoDGnbAdzc6ymXClGnYNrfLTe-1oRjUiiKn5cIrP_t6aTN0GwUIqUM1Hx0LpVzjbG0YOxuU-sqgitYE5YRU65mwxZpps3U55bDR_dgQycZ9o5gB5d-P8OtXWDYicKSvw45mmZnJP4korRnqRHd-ZUFveVhhWVTayZqiwWCSYWOXdNSBeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
با حکم علیرضا دبیر حجت‌الاسلام والمسلمین عباس فقیه سرپرست هیات کشتی استان بوشهر شد. دبیر درباره این انتصاب گفته که ایشان سوابق درخشانی در روایت پهلوانی‌های اهل‌بیت در منبر های خودش داره و قطعا به کشتی پهلوانی کشور کمک میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104006" target="_blank">📅 00:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104005">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🔵
خبر فوری روی آنتن زنده فوتبال برتر؛ AFC انتخاب استادیوم را از استقلال گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104005" target="_blank">📅 00:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104004">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a00c0468.mp4?token=JuR7ybbgdaD7KEPFeJ7hRwYurOGmmR-WTjBUgFMnrmQJ3xwmZNArAb-iH1fMNIV7u7FcRUY0OB9iY_R8BC5FqLKMseZNkra6m3u8XCyTNSXb-rEAkoBuF2EZVlkznK0yzuNF0mIZWIj4wb-vqQUVgOvzdXs4FqqOn_0mev9r82bO9FULmZMVC9V5GIiDe5u4-JkRc2-Fk2sOf446D60AWqvVRq1J5TAdQyHRxes7jGTMvFEtShU3zxJIcifWhq9s8NGpbDMOkM7JZfKckEtd0G2kwgmPucizNqCwlvYPaHCOYMwryWAA115kkqB8L0SoAuegQooRMvOsFl5MXDdjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a00c0468.mp4?token=JuR7ybbgdaD7KEPFeJ7hRwYurOGmmR-WTjBUgFMnrmQJ3xwmZNArAb-iH1fMNIV7u7FcRUY0OB9iY_R8BC5FqLKMseZNkra6m3u8XCyTNSXb-rEAkoBuF2EZVlkznK0yzuNF0mIZWIj4wb-vqQUVgOvzdXs4FqqOn_0mev9r82bO9FULmZMVC9V5GIiDe5u4-JkRc2-Fk2sOf446D60AWqvVRq1J5TAdQyHRxes7jGTMvFEtShU3zxJIcifWhq9s8NGpbDMOkM7JZfKckEtd0G2kwgmPucizNqCwlvYPaHCOYMwryWAA115kkqB8L0SoAuegQooRMvOsFl5MXDdjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😆
🇮🇷
ریدن رامین رضاییان به خودش از صدای انفجار ترقه هوادار فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104004" target="_blank">📅 00:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104003">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdaa9a811.mp4?token=pgFR63CmTYdNa4Cye9YRErYF59QlK8Ybne5uFUKomAUofsCOTbsZ0bI9C_JtE0ETdYZxyL2qNvb_sDlyT8TE69VKgQt1nqatfptCdez_ow4U1rjWLCp3JoKUPKlSUTX-WsXwkGCyaemxaNFAePR5CWaxQk1jajde0fufHBALc9q7VnzRQjf_UZ_qnnbvAflxJNzUCNJl-4xwP_5H8jyl0FDOKTrQ4v2lGHrGSQroO3ML4Kkvn7AY49zeWAZV8UXJRCMctdALH3kPKrQPVOCNklA7GME6J7mRyksqgyerZ5E2a_KXTjm1x3RBnj5_E78vv_gdxtcXWLZ1ot6QQ4wo54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdaa9a811.mp4?token=pgFR63CmTYdNa4Cye9YRErYF59QlK8Ybne5uFUKomAUofsCOTbsZ0bI9C_JtE0ETdYZxyL2qNvb_sDlyT8TE69VKgQt1nqatfptCdez_ow4U1rjWLCp3JoKUPKlSUTX-WsXwkGCyaemxaNFAePR5CWaxQk1jajde0fufHBALc9q7VnzRQjf_UZ_qnnbvAflxJNzUCNJl-4xwP_5H8jyl0FDOKTrQ4v2lGHrGSQroO3ML4Kkvn7AY49zeWAZV8UXJRCMctdALH3kPKrQPVOCNklA7GME6J7mRyksqgyerZ5E2a_KXTjm1x3RBnj5_E78vv_gdxtcXWLZ1ot6QQ4wo54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🔵
خبر فوری روی آنتن زنده فوتبال برتر؛
AFC انتخاب استادیوم را از استقلال گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104003" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104002">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104002" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104001">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ockknqpxqYl2vcb1kqVTp4xiDCeVm8aMoaL23GYgCw8qpX7lYaRJ1iCgQSkkswdfgKzMCk-lzkoWg8KyLdIJYOsbIGER77LFCzMlJQ7ya5ohTwZW5JObQ7jyR59NprYvN5-r3xyvVZI-G3qgm6IgPGm3iEtNgT-theRdgynR34Bu7lFIa63BVeEFfmgfSCwXE4wnVA2sQz7Zwo8Wh8a5TsTaesKDjoQef7uQxSm6Nad7tjtTS_uLOCdbDKPE5KhaP5jkLMBZ_tqV9h7vNLxSYbWrqSSEeO0hdcv4tWV4Ahm3KqaF5PdSKCL6U6KVGon1A08t99lazz7XFu0Nm2FKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=ockknqpxqYl2vcb1kqVTp4xiDCeVm8aMoaL23GYgCw8qpX7lYaRJ1iCgQSkkswdfgKzMCk-lzkoWg8KyLdIJYOsbIGER77LFCzMlJQ7ya5ohTwZW5JObQ7jyR59NprYvN5-r3xyvVZI-G3qgm6IgPGm3iEtNgT-theRdgynR34Bu7lFIa63BVeEFfmgfSCwXE4wnVA2sQz7Zwo8Wh8a5TsTaesKDjoQef7uQxSm6Nad7tjtTS_uLOCdbDKPE5KhaP5jkLMBZ_tqV9h7vNLxSYbWrqSSEeO0hdcv4tWV4Ahm3KqaF5PdSKCL6U6KVGon1A08t99lazz7XFu0Nm2FKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a26
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104001" target="_blank">📅 00:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104000">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b070f200.mp4?token=rI1-l87p9q3LXVQkMvye3_FSjNZNknxPY_22phATu_RxaKZrFmBu3D7Y2VoKms1-dvS2ruQhoRH__yCsBeWtwiCjAiknJYkJBYC33soS8EkWy3ccAGkSq_INzbwO-pVoWeGvsHbUPXso8w_oBE9DLnpLY0CxWY-7WACPMzFFnSRgpLfM0JVmeKQbreiDfenvqm4jQQiGByJlBZoMkCYQNZsCGXK6FDlbNeQswbDe6zauj0wBxwU0cZvr22EqJXALUoJD1X3U9lDAFLSao9An82BisOsq-sEK8TDJqmTDlMrIeYR-6XgLW-2PrBZnG4rloOoziPB7VoohDl9husZSJaaG-7K_m15rfIelOVTtl9UsrtCcorXRDWmIIOE0B-Y7TYsMvJN7AkThLpprlXzsESmb1rcLIdiMe8JMl-TaMOam3nVZVIbwElxKAl2By4JFia2N9FSBfwHHfoe7Yw9XFDCjsJqreJ_9x95n9avpLaUHhvgD6mi9HFBlJNsCRSNMUkV3YdFSWvnPXL92srbO9t7JvomGuTeepdsvsToH8tKiflqu4e1mFMuYQGhRHn3ZNY1ZzsqzszMeopywFm2YYXWmE0sQ7tchQz7sUaQ6slnacOuypoz_KaGl53YuY3bWnseNOpRmhyJRYT3srWHx1f9wWOvkr8GT9Hwm6KPc87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b070f200.mp4?token=rI1-l87p9q3LXVQkMvye3_FSjNZNknxPY_22phATu_RxaKZrFmBu3D7Y2VoKms1-dvS2ruQhoRH__yCsBeWtwiCjAiknJYkJBYC33soS8EkWy3ccAGkSq_INzbwO-pVoWeGvsHbUPXso8w_oBE9DLnpLY0CxWY-7WACPMzFFnSRgpLfM0JVmeKQbreiDfenvqm4jQQiGByJlBZoMkCYQNZsCGXK6FDlbNeQswbDe6zauj0wBxwU0cZvr22EqJXALUoJD1X3U9lDAFLSao9An82BisOsq-sEK8TDJqmTDlMrIeYR-6XgLW-2PrBZnG4rloOoziPB7VoohDl9husZSJaaG-7K_m15rfIelOVTtl9UsrtCcorXRDWmIIOE0B-Y7TYsMvJN7AkThLpprlXzsESmb1rcLIdiMe8JMl-TaMOam3nVZVIbwElxKAl2By4JFia2N9FSBfwHHfoe7Yw9XFDCjsJqreJ_9x95n9avpLaUHhvgD6mi9HFBlJNsCRSNMUkV3YdFSWvnPXL92srbO9t7JvomGuTeepdsvsToH8tKiflqu4e1mFMuYQGhRHn3ZNY1ZzsqzszMeopywFm2YYXWmE0sQ7tchQz7sUaQ6slnacOuypoz_KaGl53YuY3bWnseNOpRmhyJRYT3srWHx1f9wWOvkr8GT9Hwm6KPc87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
محمد محبی با انتشار پستی در صفحه شخصی خود از جدایی‌اش از روستوف خبر داد
. مقصد بعدی محبی احتمالا تیمی از کرواسی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104000" target="_blank">📅 23:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103999">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d25894916.mp4?token=WliCC2EuAASyapdT5DFEjXrx2pgRh_2L5lS9rlJL5aj4F9znEOSKV0cFlURFch0kET290GUfQoR6Rl94X7BT8TYGxwRq1cwhEO6N31XYFiY0vu0xGR1s5VlqiKDwpc3HOj6gR7efZKZu_vv5VWDGqnlojSWYP-NMmTjePI7f129hc4iBjdysuz2LUOPEnjIeefywWjJemIzrDEsugiu4l1ngoiwhJuPVhj60kNUSTg6EHi8IbeFt0qw3fLnvBWVRT3p9rhMQmc-X0-7IVmty62leZd1bMYfZy5IM0qCwOSRUXbl1WVU42yMXJNlkD8jFyDVpuZWI8NBNDOj_RPN0Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d25894916.mp4?token=WliCC2EuAASyapdT5DFEjXrx2pgRh_2L5lS9rlJL5aj4F9znEOSKV0cFlURFch0kET290GUfQoR6Rl94X7BT8TYGxwRq1cwhEO6N31XYFiY0vu0xGR1s5VlqiKDwpc3HOj6gR7efZKZu_vv5VWDGqnlojSWYP-NMmTjePI7f129hc4iBjdysuz2LUOPEnjIeefywWjJemIzrDEsugiu4l1ngoiwhJuPVhj60kNUSTg6EHi8IbeFt0qw3fLnvBWVRT3p9rhMQmc-X0-7IVmty62leZd1bMYfZy5IM0qCwOSRUXbl1WVU42yMXJNlkD8jFyDVpuZWI8NBNDOj_RPN0Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
میثاقی: افتضاحی که در تورنمنت 3جانبه به بار آمده تا الان ماست‌مالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103999" target="_blank">📅 23:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103998">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473efcace0.mp4?token=i1OczMvsJIV8iW_nEHQUO2qCghdIbluMqN3WoqpLUHEWNAOON7LWReIzuyHmt03w577nJKr7Xbe0Ov0lRUlwNvxd6SyK9SublYL0CmE5k2Xz9k_J-8g-_9th4cIViKsXDv525HdLeVVHv_y8MM7y--lnxNhij1wL59a9XPPDa91-FU4xUgTTyuFh4bGcg8uwZWyAmy0YAth1oI3ltnRABrIm7d8aWPC5HQ-rmhbaEAZM5W2PerdGoIQClojxqNQUxt869DD7OFIAqQKfDa2qVD_MfL9rDDOAkmpRkNUtx_OlGuq_SVLNHSvQiK6rFutSGku-nEeRAKikLo__WdYEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473efcace0.mp4?token=i1OczMvsJIV8iW_nEHQUO2qCghdIbluMqN3WoqpLUHEWNAOON7LWReIzuyHmt03w577nJKr7Xbe0Ov0lRUlwNvxd6SyK9SublYL0CmE5k2Xz9k_J-8g-_9th4cIViKsXDv525HdLeVVHv_y8MM7y--lnxNhij1wL59a9XPPDa91-FU4xUgTTyuFh4bGcg8uwZWyAmy0YAth1oI3ltnRABrIm7d8aWPC5HQ-rmhbaEAZM5W2PerdGoIQClojxqNQUxt869DD7OFIAqQKfDa2qVD_MfL9rDDOAkmpRkNUtx_OlGuq_SVLNHSvQiK6rFutSGku-nEeRAKikLo__WdYEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت کاندید اصلی توپ‌طلا در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103998" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103997">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همه محصولات زناشویی و بزرگسالان که پیدا کردنشون سخت شده یا ترجیح میدی با خیال راحت و محرمانه تهیه‌شون کنی، اینجا موجوده
😉
👇🏻
@luminooo_shup</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103997" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103996">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWOmap08PnZ8o7x7WfhYlwU1atkd3MfPR0oNzdMYXABG1Qm7C-dP5--oYxH2WvG-a-B1hPcdPpLTysJhQh939cbGneILGCsqoI46Npbnin7cXz059KWXeXU3yOQzVh5c6bhBSdmYqvdi1BVx8ChS61Dc6DuCr6N62tMkUlOyuGkN_F2DGNDl4QU-mqDVP-r3s-AaIDdu_JDunFA9-N6brnAXmnsNJ-GOmD8dNem478dhLDaiMUOl8mT2ZTzz__chZdCLTSslJzTSfhtOSPhhSgfshRANd23k8OStmuw_XIDf9ybWUkP9Fk95XQvwg3_VcIu-kBeJHEK2d2XfnHpesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
ریشته اختلافات نیمار و تیاگو مندز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103996" target="_blank">📅 22:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103995">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b498c41df.mp4?token=e0Gdnysm9aqun3t-B71mD4NGB93XRCJ92th2QIy1bldNiq9bJS5UBko-elxFHyn_PPNJXzLlOoRnKVzDiSavpF8k3hdgwAb9EzwpomoiHHw2FtaqkNzglhAS0oSc6BEi9ov4C_hjKfznXqRM6otny9pfZcBQ7Nv_YkUrfexWjdPqD_hHzu2PD3kau9KysmuqhTXQ87_FSL3jAJs9ReWJDAbeQMxFv1nGRPkb1ppQjHwdRjtFSxgKjzz8oQKKz2tHqn0Rmyi1QpTpmrlivCVF1ox2nDds50DIul4PpjCw3kJP4ATLl226uaqa-U2gzj5ft8pKiMvYznEToEdRTSWaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b498c41df.mp4?token=e0Gdnysm9aqun3t-B71mD4NGB93XRCJ92th2QIy1bldNiq9bJS5UBko-elxFHyn_PPNJXzLlOoRnKVzDiSavpF8k3hdgwAb9EzwpomoiHHw2FtaqkNzglhAS0oSc6BEi9ov4C_hjKfznXqRM6otny9pfZcBQ7Nv_YkUrfexWjdPqD_hHzu2PD3kau9KysmuqhTXQ87_FSL3jAJs9ReWJDAbeQMxFv1nGRPkb1ppQjHwdRjtFSxgKjzz8oQKKz2tHqn0Rmyi1QpTpmrlivCVF1ox2nDds50DIul4PpjCw3kJP4ATLl226uaqa-U2gzj5ft8pKiMvYznEToEdRTSWaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با شروع فصل جدید فوتبال گفتم یادی کنم از کمبود دستشویی در فوتبال ایران
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103995" target="_blank">📅 22:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103994">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEYEKYQN_Z7LPxgQBz5luQ_qOP_CwGZbFJ9c0WRA_1X2ZHILDKTHiVdJJ_jTdQ3ixSO_n-aDQZy_Fh4H7ReKcXWIJbI4PU53nICVB3YjuOW98kgy9CVHlnd8KaZdf06pmJ_2wBs0OYlsdoo97dGFFiMfX3c5DXIUgLN1-kxz37EBv_oz9_jT-WCahHOGPO32pMcLNb1RSdmZPWWJyTmbpYECEdb0dPGZ9hZRFpEc2DXVxVRER6vO66X3nc32Osmk1K0Gt4lhFsgfSpJe_tUGDbsK9hqZe-BMWpXA5Wkznohw-IGkXKyUjGPG3Du1nKzXpAUkYG-ZRbEZ0lXjv0eFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🔥
ورود رودری به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103994" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103993">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a3205803.mp4?token=Evsh3KfO_hcKhLLRbgNw-C0EZlbBnzzo46FjzV7MbMNbaFXV7Eac5qxsWSfmZrjESMHDkfUnqs3fj2cA0VBpmzKbpl7QXul9D-wbiyG0E_--peS6AzPcyvSYMSt9oPCbDBjxRD4v_SodwQwtHKYs4f70V0TUiBbzSSDy4NPqBH8btLWNvzBWJ9OmrSQjwB6EpdI_XTg3_3En9RzQnDp4pguEWUjF4rXRg0CDQN1Kr-qO6TWvbVADRWmmIsLYlybvz6RD7Q0uoCftOoLlGv8KK99EI870Nkn8mruRe8hEC58S2mytTLml47f36r9YNwBJGldZNAMsL09GYa1XfXq_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a3205803.mp4?token=Evsh3KfO_hcKhLLRbgNw-C0EZlbBnzzo46FjzV7MbMNbaFXV7Eac5qxsWSfmZrjESMHDkfUnqs3fj2cA0VBpmzKbpl7QXul9D-wbiyG0E_--peS6AzPcyvSYMSt9oPCbDBjxRD4v_SodwQwtHKYs4f70V0TUiBbzSSDy4NPqBH8btLWNvzBWJ9OmrSQjwB6EpdI_XTg3_3En9RzQnDp4pguEWUjF4rXRg0CDQN1Kr-qO6TWvbVADRWmmIsLYlybvz6RD7Q0uoCftOoLlGv8KK99EI870Nkn8mruRe8hEC58S2mytTLml47f36r9YNwBJGldZNAMsL09GYa1XfXq_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🔥
ورود رودری به بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103993" target="_blank">📅 21:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103992">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbda4c8e1e.mp4?token=RDGKeN6c73fyG0-REi9T9Q-aMT3u0aoj7iXTPeLtBcghJV2cpBccZLNWElNM1oHp6ho96QjXgOePGBmv72dL6mPoLcS95Q_zNGaPeXEf3lDtopRmOjv-sXijYnVDdrBzFmWmlFmMUhZEYBxOdJjJFcwj1mbpOM6X6Tb_DOtnN_HohH9mUHpDYlGoaVNT98rGyUoLUhN6PS6e2OZkU36Qy9wHN84EVXxEeva7JNq-wjSsvHdoweJnxz0k0yZUuoSrPEV2kQwiSxau53kFP6AOPQOYMd06Co0P9bBhLzIB9lKwUUUIy2LR1Ih01s0Z7TxCHxWkQTcWOFeKuX_ZtYR9THPt6NnmupGXyEAchyb0RfmC_NBlSO36WSLqPiUnfXRQ5VHuX6kibAKEGunLWhjl1uWdJOO1oDUqmQUoz8c76U1crrdCSBi2cSyZgWxAufQhZHNThKiiT7FrbGGu_d06I-gSWAAVXpSib1d31ge1_ScYUHBsIsXwKSjuril7ru0iOJJRe_nycOsxCtWAeKTuKo0rskI6ns5fUOmxXlwWkPEC_hGxhgORby4GUTuBhGab830HqgiyVUY6pdNQJt9UwEG75pXbR-myexbMJQMyzGp3MOThAV0VItDzLTdY0qM2QZysPPMFMlwVUBTMPAwJjrcUQg1VmyKcSLI3HEiNo_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbda4c8e1e.mp4?token=RDGKeN6c73fyG0-REi9T9Q-aMT3u0aoj7iXTPeLtBcghJV2cpBccZLNWElNM1oHp6ho96QjXgOePGBmv72dL6mPoLcS95Q_zNGaPeXEf3lDtopRmOjv-sXijYnVDdrBzFmWmlFmMUhZEYBxOdJjJFcwj1mbpOM6X6Tb_DOtnN_HohH9mUHpDYlGoaVNT98rGyUoLUhN6PS6e2OZkU36Qy9wHN84EVXxEeva7JNq-wjSsvHdoweJnxz0k0yZUuoSrPEV2kQwiSxau53kFP6AOPQOYMd06Co0P9bBhLzIB9lKwUUUIy2LR1Ih01s0Z7TxCHxWkQTcWOFeKuX_ZtYR9THPt6NnmupGXyEAchyb0RfmC_NBlSO36WSLqPiUnfXRQ5VHuX6kibAKEGunLWhjl1uWdJOO1oDUqmQUoz8c76U1crrdCSBi2cSyZgWxAufQhZHNThKiiT7FrbGGu_d06I-gSWAAVXpSib1d31ge1_ScYUHBsIsXwKSjuril7ru0iOJJRe_nycOsxCtWAeKTuKo0rskI6ns5fUOmxXlwWkPEC_hGxhgORby4GUTuBhGab830HqgiyVUY6pdNQJt9UwEG75pXbR-myexbMJQMyzGp3MOThAV0VItDzLTdY0qM2QZysPPMFMlwVUBTMPAwJjrcUQg1VmyKcSLI3HEiNo_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحنه عجیب از لیگ‌سری D فوتبال برزیل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103992" target="_blank">📅 21:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103991">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4baf3554a3.mp4?token=dzjW7N7HZnbt8I872tTwPKTNRPuuBieWE5rheAcf5g4CVwXror1yNiqf8j7X7M9yEH6dyKiCCiI3DsqsBSMNDGG-VkXy55E0y8tI-LzxcVyXOW1r_0Vp_YHdE-J02Th1N3h9SBC3Wb_zGtHPQQ0LUL_eN9SQhGrXgKZFUARyr_AxC8LueMNoDvGUZIJugqg7H8vtLDCe8pFZ_05P21SyO-WZLurdv3Vhb4Vpn7_ezzDargecoSBc9Xa7-AkXdBN2Hg1Ja0LRKidMoEed_5FfXfJlCFr0dVt8BujBHO76K3ngBwkFH3asVMfr66o6ZZhtN8FGhlmZJ3PvZVJZ3m_6YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4baf3554a3.mp4?token=dzjW7N7HZnbt8I872tTwPKTNRPuuBieWE5rheAcf5g4CVwXror1yNiqf8j7X7M9yEH6dyKiCCiI3DsqsBSMNDGG-VkXy55E0y8tI-LzxcVyXOW1r_0Vp_YHdE-J02Th1N3h9SBC3Wb_zGtHPQQ0LUL_eN9SQhGrXgKZFUARyr_AxC8LueMNoDvGUZIJugqg7H8vtLDCe8pFZ_05P21SyO-WZLurdv3Vhb4Vpn7_ezzDargecoSBc9Xa7-AkXdBN2Hg1Ja0LRKidMoEed_5FfXfJlCFr0dVt8BujBHO76K3ngBwkFH3asVMfr66o6ZZhtN8FGhlmZJ3PvZVJZ3m_6YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
خداداد عزیزی:علی دایی خود خواه است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103991" target="_blank">📅 21:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103990">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V798ceCrdGJcvPdI1sbVf53w4Hp2cbsgAQEHBiVOezOAGh4UrP1pMf0QBxGm_GVC2vBzonFCr1-AKY0Adkcs0yFDElabw3sk9uP5AIDMj4nryVQk91DtVSxeIXBPukWyD5rFovlGS8iZ5Z1czXNESnznnTZF2RamvehTJDiDDc8tGD8YbMwb-PtdlnBCMfi6GRm04eXc3nfncF-sL7kEuioKfjzUFkYesroAui86bgr_tvdoRf15UsrztBE0bkxol434WSaZpOi4ekPyzswRMPWI_weBkVjy5UuW-udFj4E7AGgnN-0PAVAceRjVmjJfZjKpYOb6kgcw8-Zr8_k1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
ارزشمند‌ترین بازیکنان فعلی رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103990" target="_blank">📅 21:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103989">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d07263cf3.mp4?token=miB7bVJLgVeHmJhflv8uBeKjm9SVwcVU0B4LtLNcAQHCrYR-CF0GVSB73hm_8diwpMoycWaj80HVlz2KPDHVY9G-k9QTi6LZImUzTsqSiTp97a7tODB0qKYU_-yuduYdvvBzmXQ3mQL3D-PVzehDdELr62Gon7hldD-bzn4NiRiZSZrxsObK8xMxhNuWZiid6EfkJFuQyH4UicZL_80B41Lpf_bwZ_CosunmpNWqDvmSLOMCAZOppecasgZQP_eG7gUf3RTPakkDVyXE1R0sXsghxf5M6OzG-t1n-WZ365MtYva_4CcIU6LsOPcRpNhNQDvAWBuyI3R289W4WC_NSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d07263cf3.mp4?token=miB7bVJLgVeHmJhflv8uBeKjm9SVwcVU0B4LtLNcAQHCrYR-CF0GVSB73hm_8diwpMoycWaj80HVlz2KPDHVY9G-k9QTi6LZImUzTsqSiTp97a7tODB0qKYU_-yuduYdvvBzmXQ3mQL3D-PVzehDdELr62Gon7hldD-bzn4NiRiZSZrxsObK8xMxhNuWZiid6EfkJFuQyH4UicZL_80B41Lpf_bwZ_CosunmpNWqDvmSLOMCAZOppecasgZQP_eG7gUf3RTPakkDVyXE1R0sXsghxf5M6OzG-t1n-WZ365MtYva_4CcIU6LsOPcRpNhNQDvAWBuyI3R289W4WC_NSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
خداداد عزیزی: دوستان قلعه‌نویی بعد از بردن ژاپن به من پیام دادند که دیدی میشه با سیستم علی‌اصغری هم ژاپن را برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103989" target="_blank">📅 20:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103988">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myhXpAFGmN4xVg1evta2HNiDEyZh7tk0FzB7WiIeRpw8nCWm7-H7NwzYWVDGpg3NjtjF-AmVN470XbF1_a9qq_2QKMfGdtW7dutBQYlgpnBknWdvJDqqnhpHZJAnEorL8KNPkiyK6D-MNiLzv3ke43LqcFWPHVYOFVl1E4PfluZkoBz6A71gn9v4cWDaZ18vaB8eFc28_VMvHeClO3k2UbCbKYZn3HeJ4Nr155TfmHlZApTQGpnCz_qgN3ouvExwVMliPR5RdaOqQ-S9zb3_EW1lcUXbFKQoLvW0xMDgmqa7CQvH6ryZlP4pi-FNV2fGcobdIUrl5jVCd2yLsu_oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
نخستین حضور دانیال‌ایری در تمرین پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103988" target="_blank">📅 20:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103987">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2WWHugav6wlEcTLrHurTZgq6wXvaZbvzFUv0napJBhUooE2z6fm5JJ2XlnOKGcQUdfOHSy0iV1e7Sb-NaIho93CAZrP4WADR6vH3l9H7KJQlKedj0_-fibHmvvvjqjyZecuxwYu_G3Xs9k3Hvw00CALK0OhsEbWk_60PzWgou-VZBC6ZUvBQf1qVPeB3DPLRglI-7N_DVtL9POxLgNJ5YHjJP2GrQqiTvoxXF1WKWUE0jg-X_ookscp4v18tnEL5F_pT6p28Jd6Ds366JM2ltShjbvONhfR4VerETnQ4mBxsNWaa98wMPoEVBOtz-jwcLJCRpvPGyLilM5niD-Jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
تیم فوتبال خاتون بم در نخستین دیدار خود در گروه E مرحله انتخابی لیگ قهرمانان زنان آسیا، زسکا دوشنبه را در شهر دوشنبه تاجیکستان با نتیجه سه بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103987" target="_blank">📅 20:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103986">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c623e2cb.mp4?token=lAlujt8PuuDHmp7lWxElIWE0DvCViVo7J_IJ6LWzWSKN2z7f4rpwyUy0dbq61WLoYcSU06Y-tQeEglRKGSWCfh5gXicV6b2GL1wJP-IUzJC6LK7G35Wypfg9bYwyDZ4AWzhUr7llNGyd5mBuv8S7YVzTwkuIJyTaWNPHo_uhgTvy7jJn1OHI3YshJo6-TGZwaDCzxH2Ahutormwvp1NOo0xdfJZta5-aLfnst-gwew9d727s7yQdUIA26Vq4c3fRMugeDsadsF23KwS3X9wUP0E686xZL0hl15RrpxSUEZjxUBK8N8o0g7KAthHPm9mHjpcB7KLdmuCSObi53w6QWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c623e2cb.mp4?token=lAlujt8PuuDHmp7lWxElIWE0DvCViVo7J_IJ6LWzWSKN2z7f4rpwyUy0dbq61WLoYcSU06Y-tQeEglRKGSWCfh5gXicV6b2GL1wJP-IUzJC6LK7G35Wypfg9bYwyDZ4AWzhUr7llNGyd5mBuv8S7YVzTwkuIJyTaWNPHo_uhgTvy7jJn1OHI3YshJo6-TGZwaDCzxH2Ahutormwvp1NOo0xdfJZta5-aLfnst-gwew9d727s7yQdUIA26Vq4c3fRMugeDsadsF23KwS3X9wUP0E686xZL0hl15RrpxSUEZjxUBK8N8o0g7KAthHPm9mHjpcB7KLdmuCSObi53w6QWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تمسخر مسی در استادیوم‌های کشور آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103986" target="_blank">📅 20:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103985">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7HXbST4KOypRwdmgf04C6H2z3R2-FjtjhKkdX2z6VZJpNpLe5_eWVLtG32pfUh6_qsmPRVm1acQ9CcQhUfoGffhIZSEba5Oh4-s4noSCvb_x0bnF2DbJtVJyhDzjrYcu8xW2mxE5oRxP2V-53YyGw3tz3fOKDAHxL093bf-pP34a10jJ5cTgsREll84ygRS8zb27BkhH-FvktshwGOrxdgijtYRuL8x4f9Nc-at5fm_Ce9mr7PVtYDuMmETL-e03L3V7AdPHBIf_5u9Zrp7gvdwac9-Y7DZ54aFu4qSG5dMvbYyR_aD7tfn_Vt9nUBJn6ap_MW7wkKqrDO0OuHehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
متئو مورتو(معتبر): احتمال موندن خولیان آلوارز در این فصل برای اتلتیکومادرید بسیار زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103985" target="_blank">📅 20:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103984">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4dihpDNGFFbGF2hwjHw3YO4RQgU754HksI3sYbCORW6jGs3wj2iuvTbPMZX4nV78-XlbVXV2VDqS37aMxdYrzVGQaKSLwHwRAk8QKCSAmKglY-IBrj5WvoRC9ibCQ8QnRO7IMxY8chG7tj5L8uXFCr-1si7PTsFt5bWW7kbBygOWyeokXeiYvEzmX3z4cB4ElYZLAc8fRQhHlq_XI0x8JYXrafo1uOlRuGVdmN14dEVVC8qNCbe5yYFnJUg8bLlrS2YzTxzkhzuH1TG6DkmpSpwbSRudqyDQTcGrKazpj7SXtUS4LlHFRNOCXrpgDhbcABjvQsu5_OktWIypf-UHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
😐
🔶
پشمااااتون بررریزه؛ دختر تهرانی با دندان هایش گوش دوست پسرش را از جا کند
🔴
حوادث رکنا: یک درگیری عجیب میان یک پسر جوان و دوست دخترش با آسیب شدید به گوش این پسر پایان یافت. به گزارش رکنا، این زوج پس از بروز اختلاف و مشاجره با یکدیگر درگیر شدند و در جریان این درگیری، دختر جوان گوش پسر را گاز گرفت و بخشی از گوش او را جدا کرد. شدت جراحت به حدی بود که پسر جوان برای دریافت خدمات درمانی به بیمارستان منتقل شد و تحت مداوا قرار گرفت.
🔴
نکته عجیب ماجرا این بود که دختر جوان پس از وقوع این اتفاق، خود نیز برای کمک به پسر جوان او را به بیمارستان رساند تا جراحت گوشش درمان و بخیه شود. جزئیات بیشتری درباره علت درگیری، محل وقوع حادثه و وضعیت فعلی پسر جوان منتشر نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103984" target="_blank">📅 19:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103983">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szE9xj1HBNJmCLyjeP3NKiD3bCxU8bQeIOYi-N2EtytY-QEN2KV1xgPwTXxZlWRLzBDyelaDN3pQONZXotJg2JEYPV3vjzniVOLdAjoUfRJLC_NkJYrG1F-9UmC3pPsq-GWgALT4PGpxIOqXBmD2VrOXpppHENqe96Rv8RTAxxW-5BejDRzuYXQD6_MyKtIyLy9mR_gwL7XMgeTM0QIc9fok5W7pHT8yzmEww9xEUNULnVanBlgZ-bgthUOTglXZyj3s8AwQPUccAw2sp7AtT3P97h7q5VTbgRfQFq-aMceGj3w_UBkkL06CfjsVn25QV3RGxdsJih7_tnc_Ao5uZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
رامین‌رضاییان تا ساعاتی دیگر با عقد قراردادی به فولاد خوزستان خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103983" target="_blank">📅 19:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103982">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xedmc63Sm67kMZKxLBwYnY7JUC1_dIg2ydmDCEqRfxQJHmXGQxN4427YQRpJQi_S4N7fCcgeoQ1tr_lrYkZAuL4wieX-OCf_tQ6YAYnWeGttsuMSY_jVU2t6cfApKipN0lIj6pR36-_Cuq-LdIWO-ISsjV-T28IvKjRMMVNrKVrtZ-wG9X5Us8BDumI9cRZEuZaJXTOFCOTtxWLzdREX8Dtg2by-ZZNsjT4dmXv3uMpmxkA51jn7qihemZ2WI2I2KgUIVNGTWJByL2B5ccDAB0UtFB9dAj6cusGOBf5ANeH9tbehl5x6EnsrWI2Am5lPxPxL60AZ9BxAkfL4fJxRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103982" target="_blank">📅 19:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103981">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF29MaWH2CCryKMSwVrduofoFNR84ugrYzVd30Egd6FhcaoA95QxvZWMpl4xGwa-g2idrh5Ae-Q4wZHJi7gAPkwBfHqsdRdG2GC186omfH6H9hD426Qrx2XfjSffhCIcNyWq8lALow1fTOGUQDm1lRwe7a_5IpH1f5fkD7w1JvhCrd-87FXu3Jsu9wukJ4HQUO79eciBJDBGxB2N4jF1rg21t2LFEA94FVKY9qCGC74INtYviVaeF2RKR2TEtCRSEi41x8u0BMIkKe5QEOyrg-_RaUInIjLl0hHrwW1FHrOBgPtj3oqGW5jx3erccAyeZa5EgKqmOSYoIiTvSKHKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
قرعه‌کشی فصل‌آینده لیگ‌نخبگان آسیا فردا ساعت ۱۱ صبح برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103981" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103980">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLnCPhQ0TMmB0AnARLhkKbtQ8O7euUFsMxy7j11Ts6fh8TMnNTnddeWGoCsYYpgSNiBlKS7RfpwvyczuKDp780tk6RPhB8Ea4lEycULVpqtpS0zODhtFdDpE6fsgGc3NUe1t8wL94UxbiBB81G5KRqkqVHihjpCbQgf2qX7bK4s9MOPiOyNpugQLMSz4j_WX0ReFelS7BZPRmobh-Zdt2lS-nWEx1vk6SJHYoGiEid_jMVkm6WjWj3ttIvG2mRhG8TwdyP4rZ-botvQD3Ez68jn2at1N7m0Jl6vgPx7H-oKCy-3-jiXT6sfFh5lahtUfUJ263o_r8Kr6qop8KyEEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز سه شنبه ۲۷ مرداد
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی در سایت بتگرام
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۱۰۰٪ بونوس رایگان اولین واریز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب بسیار سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103980" target="_blank">📅 19:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103979">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdOcHP1vEzBocvOuDFJNWHlNamgka1zbkxCfNm6x13L4gWE5zYLI9U6NEiIiayWm5cNE3SqJidGSkXAemzXBaWxSVdYbNODytihq0eC43uNl6oP15V75lzXk1AGD6eW-nu3QDuH_RvznKSNzjtjkIVQS-84qecH6DBE8ITdsrw96w4sGWAKfZX2-3kx6wRZf9Zx4Orub8i_J7U_Srfufk0GZJX3H-WRWQVOgu5KBZuy0ziNQXqf2OjVjR98mPFbEUXt7QvLte9nisJa30HHQ26z0jh902csIWquzhp4xIEPDrbCxH4IN39iA-W0Y-pUJ2zB1ZyVCoVjJ40FFpYxShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
رامین رضاییان داخل هواپیما: انتخابمو کردم بقیشو میسپارم به خدا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103979" target="_blank">📅 19:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103978">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868e8de9ba.mp4?token=Dhjomvw5xoMbT8VdZOHyqrS5NvssuZSypTklGLoqwLHLu7-_js1fnUwX2bzbYswJfOUwn11dbVYpaCfbATRnX53fQERSd2oq71oqzpeOKzLpSehOFzPlzur2GUIiQeZ4CGAfBeczezULpSXVYomkUVZjNDCV_YaejuyZJ4NqIz9l8Ue9nDupvyCkVefHPSwWfGKj_CzcK2nS0puqCqs4gOd8pqNCOZDNKTuuirF9gUcI_XEiJ3WNOLf9vzp1SuZftRGxHgRo0bj58fqYhwNr6k68_KhhoSpgZXCJJH4Nat39-Erl_zalVjrTG5ZsSS64er3qHQz3oYxahTvTdzdbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868e8de9ba.mp4?token=Dhjomvw5xoMbT8VdZOHyqrS5NvssuZSypTklGLoqwLHLu7-_js1fnUwX2bzbYswJfOUwn11dbVYpaCfbATRnX53fQERSd2oq71oqzpeOKzLpSehOFzPlzur2GUIiQeZ4CGAfBeczezULpSXVYomkUVZjNDCV_YaejuyZJ4NqIz9l8Ue9nDupvyCkVefHPSwWfGKj_CzcK2nS0puqCqs4gOd8pqNCOZDNKTuuirF9gUcI_XEiJ3WNOLf9vzp1SuZftRGxHgRo0bj58fqYhwNr6k68_KhhoSpgZXCJJH4Nat39-Erl_zalVjrTG5ZsSS64er3qHQz3oYxahTvTdzdbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نمایش درخشان آرائوخو در اولین بازی لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103978" target="_blank">📅 19:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103975">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TREh80RVrRXUy31jaaJXumVCgmiPFrrd1bFxnq-lA1V8q7cs0kwuaQCK2GovTFgp57m_N8MmV3IYzZrFikBkTGghle0Q-dKo3UOx5jBu5w1-o8FoMdrZT5NSJDHGBaQE0XU_K8bMCQWgsgBmD4FTp4sDJmUUvJ4utusGiw8vdn_9RjCgViu25Exg7ueocfdnwNnw_aKXe591qtvr9D68_bTZB9jh0DulNza0gvX5LnaL9bZh_qMpvqT20JYNsN6PgEZnQDOKoifBGU1nWxAeVnCX8SXrOhZXkbEwQuEHXU1WKPOYbxNAtjLPi2B3CJZ4MxPrimTbvqAhV3lZLTO-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmBoFaqyvAnRk54fAFLeVJbVOOkZ4PbfAoZezOBRgoa8cjLiIDxR8paOsi75AMllanJkkECjFmVw4cvCFu9c3gjTUgTfULc1x8fHhINA-O6zKDvwyV6OAUdsKNRKegqqJ6DYW3Lxw_N3t4ikJRdcdCRaqgx6kgy8sB0Xmj6lgV2BBAeZCN-0ZYeRZpm7WPFWvhSvHdMXpBAyCiOtrroFb8yXzlEd5JCyqc-DIomF0Qj9UOdG1T0fIxYzuUy5CuOTVINRfCLYeBy8uHj1DJ2r6bRKub-q1lXMcL6DvKZjPEhGTppQTPCkQxxIkpdafM1imOFg6ZX6nIVABwmm6FxJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3gbe5Zx2wzwEXEFr6TByKnQu2pdF1evfm1CjlvlyeXnWQy5VUtvH2bwy_GBE8CVcx6CA79d_NyVNj3N_BCqMQveKV8WlCDOry2FKi6nYDEVr-Q-cT_Fy72ZCYh6tUJAEkdwVOCZblm6LpLPTbXZrygzdmWsqnFymvbfgJ_8ItrGhxN1PLZ4VEVRHYyy99xiGOZYYwFcdssSUuY6-sL0DoZS4LUVqSv2jiUwRsZmKrhr8gfRbvFo014xb_-nPHqhd_1KdPOXuiwmFDaHe5iBTDoQaFPzo-uUbEHL822E1hJniKmxb3cK21pNilPSce4gz_efIPBdTiTSNKjQxp2Erw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
به‌طور رسمی: کیلیان امباپه و ارلینگ هالند، بالاترین رتبه‌بندی را در بازی FC 27 دارند!
⭐️
🎮
دمبله، ویتینیا، رودری، کین، اولیسه، پدری، یامال، بلینگهام و کورتوآ با امتیاز 90.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103975" target="_blank">📅 18:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103974">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20aeb6e887.mp4?token=slY82Elp-uHJMvgIP0pbA82rlKYnDO0eVCm8X-APu1RDBL6XmKJ7_SHoMNcf8VSJunTjSUKtIMRYmIo7Z471tq4N5hmImICKlIAxF25KbWS2xSnlXOvlTpM362K0snnCT5JKwX7UulGgep6igydUyz6l1JR6qGKzGVeGaCsgflvLNnCQ8sc2HUmSHHaFTUqhSXSz6IF5KrSgNCHdkxg387_tb60MS5IYxZF3YDHs4xsWZoZUGaS6pJNyVas4v4V7LHQ4gv8LTbM8yMxFfGefPsAAb2a7rj4QMqAFZ4_4eYOkQNb7Jwmwq6HDtWIT9k-OuN8nfGg1nOspd6ckqc5B7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20aeb6e887.mp4?token=slY82Elp-uHJMvgIP0pbA82rlKYnDO0eVCm8X-APu1RDBL6XmKJ7_SHoMNcf8VSJunTjSUKtIMRYmIo7Z471tq4N5hmImICKlIAxF25KbWS2xSnlXOvlTpM362K0snnCT5JKwX7UulGgep6igydUyz6l1JR6qGKzGVeGaCsgflvLNnCQ8sc2HUmSHHaFTUqhSXSz6IF5KrSgNCHdkxg387_tb60MS5IYxZF3YDHs4xsWZoZUGaS6pJNyVas4v4V7LHQ4gv8LTbM8yMxFfGefPsAAb2a7rj4QMqAFZ4_4eYOkQNb7Jwmwq6HDtWIT9k-OuN8nfGg1nOspd6ckqc5B7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال فصل رو با قهرمانی آغاز کرد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103974" target="_blank">📅 18:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103973">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bede2499.mp4?token=ZEEtJ29PhmUA59Mun87LMsW3zRi11aCX1V6Ziq2i6SUJe_xPZhUjMYcWoSRjpWtAzFF9ogNEst1jsnkGRtKN_GJ_4r8otRieq86eUTR5lARpy0iKw8KPabAot01yVKLJyWWws9tMNjnepHQ5pn7bJ6ahXDGd9ahd3fRhMykt72ozseMKRA_mzqXZpUTPEIrrhxXevki86zgHyA0t_n9QDnomzn7mYWdQA-yrkgGswYDiL7PcHKmUPniTVTEAU3oAkQZMl69aMI5IuYL_E04kKQuRZQvWL27brcZAE0CUV-kTjZ8DtXe5XDCBwXYQ5kBXhj9sSZRBKsDOi-ecwrELvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bede2499.mp4?token=ZEEtJ29PhmUA59Mun87LMsW3zRi11aCX1V6Ziq2i6SUJe_xPZhUjMYcWoSRjpWtAzFF9ogNEst1jsnkGRtKN_GJ_4r8otRieq86eUTR5lARpy0iKw8KPabAot01yVKLJyWWws9tMNjnepHQ5pn7bJ6ahXDGd9ahd3fRhMykt72ozseMKRA_mzqXZpUTPEIrrhxXevki86zgHyA0t_n9QDnomzn7mYWdQA-yrkgGswYDiL7PcHKmUPniTVTEAU3oAkQZMl69aMI5IuYL_E04kKQuRZQvWL27brcZAE0CUV-kTjZ8DtXe5XDCBwXYQ5kBXhj9sSZRBKsDOi-ecwrELvzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🇪🇸
کیلیان‌دیکتاتور به بازی‌های رئال‌ هم نفوذ کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103973" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">معتبرترین سایت بین المللی شرط بندی که به ایرانیا خدمات میده
✅
وقتش رسیده قید سایتا ایرانی بزنی و توی سایت بین المللی فعالیت کنی
⚠️
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103972" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djeMi0Wyyh82jzAaVbLjjXzh4lXx7mpJPUohuUPT-Kah-ligh-EeAErTle2wG9Jn_b7Gv0ipLBO-DRW6kUt1i5DJPEeLgsZlO_IPKPPEMnogbM2fcniXFPKRu2EmJFvZsLl7yXc-GC9vLHnaFbb6dFVDY4NJ5RBK6_69fyodWTdy74D77YR2w0IeDQCWjcCKwcuHhcXmQAEYjGqvVo2HwSNj-lB5zWS0lvj1-awB3NhPjwmWPE2t16_IOBYXvYy9cB1A2n9tjRSIDGsrAkqTVUVQuwXmIk_MfTeecc283bQf0xcR9cxsA0LBE5PyNUiEoygrKP539rCTDcEJXNEnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g26
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103971" target="_blank">📅 18:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۱۰ امتیازگیری زیبا در دوران حرفه‌ای استفن‌کری
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103970" target="_blank">📅 18:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed8d80e6a.mp4?token=s0wKtNc_x1Q30NTTIyYkDtx-xzHslJZZ8U6BvngFeP3AupDwB_UFV_tT8U_sALSaZLMVSWB7Ip2Q9KxcxVLwTNKKzaNmNTjgMghcqmwFJlYsqKmZ-8qxVrEELcCzxXAz05TVrNYXLQ0HdElGF7534OLCL8J8jmDnVKIOwd5vCs7JS3_AFTC7sno4apwLZwtAP0ktIc87llLAa0c3ZX5celVmMxhFOQVJXrYnP495me5x1JREDDDc-_ENAiiaUSPmCJlEzhf1sBRk0XuavfeAo0Hyey71WHmOpGK-U5Y6QsK1JLQ8GwZKeqqCwnoBFTyaLp4xFUY5ssUxGE2FjlXTGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed8d80e6a.mp4?token=s0wKtNc_x1Q30NTTIyYkDtx-xzHslJZZ8U6BvngFeP3AupDwB_UFV_tT8U_sALSaZLMVSWB7Ip2Q9KxcxVLwTNKKzaNmNTjgMghcqmwFJlYsqKmZ-8qxVrEELcCzxXAz05TVrNYXLQ0HdElGF7534OLCL8J8jmDnVKIOwd5vCs7JS3_AFTC7sno4apwLZwtAP0ktIc87llLAa0c3ZX5celVmMxhFOQVJXrYnP495me5x1JREDDDc-_ENAiiaUSPmCJlEzhf1sBRk0XuavfeAo0Hyey71WHmOpGK-U5Y6QsK1JLQ8GwZKeqqCwnoBFTyaLp4xFUY5ssUxGE2FjlXTGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
وینیسیوس نادان در بازی دیروز رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103969" target="_blank">📅 17:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103968">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPZa4aC7NL97bkMyAkJsRzy1OewUZHbkwgeaRty_j4N8yyHIjdzI--teWR4ri6gDHG2uQT31B46HF2b6u9CAGJC0zvPkyi74YSFNKDOXQLZzaaA2DR57VwNaIQtw-RhuZDslxfMle6PmNGJqHw00k0wvFWcRzbwla0ZvOOel22qeYHWQR8VltFo7BNibouc3wkq-4qb_Eink_rnWAVgDQXuYwfr02H86aXQ5uzLjRrE5T7hWbWOqZtsSPrgGCsQkIXqF8IIEYmtZCof9BaNB8RJIN8uuKQim-Bsail1v3hsDUkEHLt9xOXwoRjRWWepGBMWIin2lr2KFp_okSZv1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رومانو: رودری در پیامی خصوصی از فرمین‌ لوپز درخواست پوشیدن شماره ۱۶ رو داشته که با موافقت این بازیکن قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103968" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103967">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJDZlrKRMCwRqazxEKoRs51WWkb-zvVfywn2ShFQvPCetCEyC0-lu_QjyoIFIkQWe2rvKpmJOWCYftiV5PmYU_F7IsxjkCcmw6o8H85O_T6HX56k9pZmV1-A9dFMIRmNPUIAlYSH7ROKC8OoerLfvNTkdzmX6lkUmNp3kLEimeyaZuurKItAkYKuEc2jvmC8X0AQWgL8mRPEuJ5ilS5oBcYxChigQ5hT0-E4cPLwtqP4DmdXiZ8j0jXFqmSEgzNTFj8EA2HurwyoUm27wJOC4ngegZLSp4D1iHCJd-9vLc1tlVY0vvq-k1qT0NZTg-WZRnrsSDHn5S_N7z5x3-9AKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از موندو: مورینیو خواستار عقد قرارداد با زوبیمندی ستاره آرسنال شده. بعد پروژه شکست در جذب رودری، رئال‌مادرید هر طور شده این ستاره رو از آرسنال قراره بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103967" target="_blank">📅 17:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebf8f1007.mp4?token=JIm56kRyMwr7kT7P4-h3tkz3SyhDa-8nG1bwHJ8I000SF1xrYhC8ldjA3OdpEgZJZtRL2oMIXQHF_a38c0mezr2rghobB1c8y0PSZE5SNTB90FGxTxNJYJSKozRooCgPGSnNLeVceiwTsuOuNrA5nDTQLOeI_EBKk7G4u6jMp9fxfCgfpb_IhKAvxbrFtyf1zSQLvs23nH0XT3Tl9Kxn_X36e8xMWTeb2kERhYxbwH8xrh1JjG4Qj-GQcQZwPBenBa6OPqJOO-pLK3tLmZAPHIVvgA0BemjEvNPse6sivBhWBfmSjhoVQsNdJ_iGqnlYgcz_rFCh6P0ZZd_AaK-n7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebf8f1007.mp4?token=JIm56kRyMwr7kT7P4-h3tkz3SyhDa-8nG1bwHJ8I000SF1xrYhC8ldjA3OdpEgZJZtRL2oMIXQHF_a38c0mezr2rghobB1c8y0PSZE5SNTB90FGxTxNJYJSKozRooCgPGSnNLeVceiwTsuOuNrA5nDTQLOeI_EBKk7G4u6jMp9fxfCgfpb_IhKAvxbrFtyf1zSQLvs23nH0XT3Tl9Kxn_X36e8xMWTeb2kERhYxbwH8xrh1JjG4Qj-GQcQZwPBenBa6OPqJOO-pLK3tLmZAPHIVvgA0BemjEvNPse6sivBhWBfmSjhoVQsNdJ_iGqnlYgcz_rFCh6P0ZZd_AaK-n7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
🇪🇸
هایجک تاریخی لاپورتا از رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103966" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b51eb3cd2.mp4?token=gLMFINSLCIViYhfVUAScVlSgQ8e_GPd0_4cDma7cSO8tZNOqQwueZn02ZlPBxe4k9osqUh0DBwE0q8WWGx06wVIvNBEtEXLX-PinZFJBIh-GSxIamTsAzxufyRCA73m_0dfsSs9YE28JlhVZ5lPW_u_rsQ1IIx__F0GScGx4UO_q4BeJd3IUznYqfNxSYNfip8kqZqyNDUAfdEDYXKYsItqAdDXcKrc6xiUI2knirz61Q101-E2u2VBt6JHDM5LZvhzQnEslcA-_UBMImYggLvnKmRkrrwu2XJ_JvO7aM2EMZRx0XlwmBH2RffaU8aESParPCa4-_yZCYD73L0jonQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b51eb3cd2.mp4?token=gLMFINSLCIViYhfVUAScVlSgQ8e_GPd0_4cDma7cSO8tZNOqQwueZn02ZlPBxe4k9osqUh0DBwE0q8WWGx06wVIvNBEtEXLX-PinZFJBIh-GSxIamTsAzxufyRCA73m_0dfsSs9YE28JlhVZ5lPW_u_rsQ1IIx__F0GScGx4UO_q4BeJd3IUznYqfNxSYNfip8kqZqyNDUAfdEDYXKYsItqAdDXcKrc6xiUI2knirz61Q101-E2u2VBt6JHDM5LZvhzQnEslcA-_UBMImYggLvnKmRkrrwu2XJ_JvO7aM2EMZRx0XlwmBH2RffaU8aESParPCa4-_yZCYD73L0jonQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
بازیکن ۱۸ ساله و استعداد جدید بارسلونا رو مشاهده می‌کنید جناب جسی‌بسیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103965" target="_blank">📅 16:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca61d3191.mp4?token=oADdiz2g8UwAROzTeqy7JP8pTwuEg8zJEuphz5_peqs4QXmWBUGQCQeGzDzZG6nFQ8AY8XF2FxCauG3702t7rF_uzJD5NjRfMwcwBZxBDLrWE6YicW0dFUU37AepMPaaPHt_H7nbFpHp-LohlsqDywDxiiJH1aweGfWL0QnNirkbR4GX4zBhrB-wr6cWr6aYAL3I7OmwMia9XvWTAe292lFYS2ZOeETG5acQ-wT-rcvMLNcgdB5l7lPbcwISJDEMCwpWIJol-M8YQZxy_STaCzyKGyMXCY48ryjtvPNwaaZLaMA2tEzqt2FOlnAY01Bvp4vBNb2HmIvYB1SSoKDk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca61d3191.mp4?token=oADdiz2g8UwAROzTeqy7JP8pTwuEg8zJEuphz5_peqs4QXmWBUGQCQeGzDzZG6nFQ8AY8XF2FxCauG3702t7rF_uzJD5NjRfMwcwBZxBDLrWE6YicW0dFUU37AepMPaaPHt_H7nbFpHp-LohlsqDywDxiiJH1aweGfWL0QnNirkbR4GX4zBhrB-wr6cWr6aYAL3I7OmwMia9XvWTAe292lFYS2ZOeETG5acQ-wT-rcvMLNcgdB5l7lPbcwISJDEMCwpWIJol-M8YQZxy_STaCzyKGyMXCY48ryjtvPNwaaZLaMA2tEzqt2FOlnAY01Bvp4vBNb2HmIvYB1SSoKDk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار چادرملو: بخاطر ضربات پنالتی تورنمنت سه‌جانبه جلو گل‌گهر تلویزیون خودمو شکستم اما حالا سهمیه رو از ما گرفتن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103964" target="_blank">📅 15:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e6573bac.mp4?token=BO5szwKrKCidoqXKQ1YeuxofpbVOGE426wFgnyV1syBcFbRl26gldOc2_qKx1Ys4StxG66dLD5MUJRccn5_Dqbk2VE4UGe37VEqzGzoa6_EUAUPpocxK2zPTjXM3HuzqXGTMbXOdZd3fO_zR9Qih190CtYhvTDZJwbDlIMuJYqwjjGuDB7eQu6UWkxzlJOruSMmQfiWTSoreTRn63-Bsn0CurdrKLlmJ7GWZIKyyfymrhbT6Tch58iOXuM3fdNezffzwdn9M3C2D-y9gCBaZkL_BtzbM2EUMjf-x81b-scaSX9w5_jsCyEVIkxsajlAC12meVOtC7yWWzIAjMyphyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e6573bac.mp4?token=BO5szwKrKCidoqXKQ1YeuxofpbVOGE426wFgnyV1syBcFbRl26gldOc2_qKx1Ys4StxG66dLD5MUJRccn5_Dqbk2VE4UGe37VEqzGzoa6_EUAUPpocxK2zPTjXM3HuzqXGTMbXOdZd3fO_zR9Qih190CtYhvTDZJwbDlIMuJYqwjjGuDB7eQu6UWkxzlJOruSMmQfiWTSoreTRn63-Bsn0CurdrKLlmJ7GWZIKyyfymrhbT6Tch58iOXuM3fdNezffzwdn9M3C2D-y9gCBaZkL_BtzbM2EUMjf-x81b-scaSX9w5_jsCyEVIkxsajlAC12meVOtC7yWWzIAjMyphyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
کنعانی‌زادگان بعد بستن بازوبند کاپیتانی تیم پرسپولیس فاز دیکتاتوری امباپه گرفته
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103963" target="_blank">📅 15:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=ao23IXo-yqk5SJ9JnMZl4oFvM6i4mnYvwdL3mBSH3XRxFzYTgD-ieC9CcP_MskYWNQbBIOJJpC-SmKO5TYH6yoOI5IFv9jrqTxlybyVp7yX0PpaFknXTG6WbAj3IyNB0v6nk52cNG7MttbNfrcQCVHjpRCn9t-TOxO2R2pfd42KhMeZr8rkfh6GhHigWxpYodV01vhv6ofD2pmzxQghhRwhSl8Ftc8NQiYTjvmmrkOcLDCl_Em-JUvwyiLoBnSBXMH67dkZt74D1vacSjAmd9PRaEWCVwGTDLiQFi5VSuOgdiiELWGyTBPrjx_EtynZToFh7s2IGvO1iPUtPbfy9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358b452f1a.mp4?token=ao23IXo-yqk5SJ9JnMZl4oFvM6i4mnYvwdL3mBSH3XRxFzYTgD-ieC9CcP_MskYWNQbBIOJJpC-SmKO5TYH6yoOI5IFv9jrqTxlybyVp7yX0PpaFknXTG6WbAj3IyNB0v6nk52cNG7MttbNfrcQCVHjpRCn9t-TOxO2R2pfd42KhMeZr8rkfh6GhHigWxpYodV01vhv6ofD2pmzxQghhRwhSl8Ftc8NQiYTjvmmrkOcLDCl_Em-JUvwyiLoBnSBXMH67dkZt74D1vacSjAmd9PRaEWCVwGTDLiQFi5VSuOgdiiELWGyTBPrjx_EtynZToFh7s2IGvO1iPUtPbfy9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
خداداد عزیزی: دخترهامو زور نکردم روسری سرشون کنن. برام مهم نیست چی دربارم میگن، حکومتی بودم که بیکار نبودم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103962" target="_blank">📅 14:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQsv5_CqAPUAZ7H_n77jaw8C_R_gz-EWkNWh-JYMYoBHuCbTZ6Zy242vZHoxt34gzbWBKU7S6q9eCKYQw4wbnBCM8GruqY2l8Po-UnchLi-PWAc6gHzPggJOjuMEC4isl-GuFuzOLe0ShbfQu6kEc2G1Blg4pxT7c6rltHht_xHS8RhHSDRVUKzqvwCWHtwyHQYmsRg5DNmXkwKGLAWMEy-9UjHNGHgnWFNRyHbvl77qv1MZDnitDohtO5hZ7DwqEUqKhI8oThUlqtl-KVyryVy70U3DOzM9-vhW0dYZY1lE1ymEYmdI1lkbvqxEgT2gGYKm6Eps7Dfmer55RGAZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
👍
آغوش صمیمی کوین‌دیبروینه و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103961" target="_blank">📅 14:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLh_uO5SKRwV5O9CP_j_vtwnfPpnpoiSgOY49leKldo21K8v0c2X88Uvhi-PEFVdlAX_4uw20lEsm7v2uneyU2eFqVxEEpcp_oDHvtCz2et3_aLB7EcuL3DIk_PwlI8hNNO8Dag0ocd34EQLPIThkTl-EAGsbuSizWoMghN8I7quNWHjamoVElEgLiEiclLTe_lxsccqdZGeGyncLWw18JJjyRa_1UJ9vTvEV-340uN1KhhI_dPsp_xkxyn0SvUCg3QchHBG6Nml3o_Q9z0GH29JfuOwJBlO7cWUyIeOJ5MbW26rlwBYyFIImwuZadySfzxLS87ZsQhCz4KXS7vgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
افسانه، کریستیانو رونالدو، در مصاحبه‌ای با مجله ووگ درباره آینده‌اش صحبت کرد:
🔻
"کارها و فعالیت‌های زیادی در پیش دارم که به قدری زیاد هستند که نمی‌توانم فقط یک مورد را به شما بگویم. من برای همه چیز برنامه‌ریزی کرده‌ام."
🔻
"وقتی بازیکنان فوتبال از میادین خداحافظی می‌کنند، ممکن است یک خلأ بزرگ ایجاد شود، و شما باید وقت خود را با فعالیت‌های مختلف و برنامه‌ریزی‌شده پر کنید... نه فقط یک فعالیت."
🔻
"من آماده‌ام که بیشتر لذت ببرم، بیشتر سفر کنم و ورزش پدل را که خیلی دوست دارم، تماشا و بازی کنم. بنابراین، می‌خواهم به لذت بردن از دستاوردهایم ادامه دهم... و از دستاوردهایی که با هم به دست آوردیم. زیرا این ۲۵ سال، پر از فداکاری‌های روزمره بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103960" target="_blank">📅 14:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34552c022.mp4?token=vX0N99tdY2U1eabZSfbv3ldcenrgKtINJWBwbDWtjHTjlbdlhOu0obDL-m0S2gwtq26Iav6M6sAV2_3TB7cAaDRHLgjipfN_ug_1htUJBpn0u6cn-cl8QMPYWqcY1SG_EvV6Yc4Qm1mh8KsWOVcm3Mfe_6wGBwV9e7RMrthB_qtjiSmSEtvzSyMmfsl3zD-I9YiIk4xT321yZMYDnHHhMX7FoImF4XZu3VfVC7QV5Plslf6Af8HSy_yaoQqfU01yvIGMG6BKAaC-zMlUkGBaYh2M_sZ9-pfFLIxqOqD6cP2FXAYHtHK8Hpq4qieLfyVEFbaFE1lrvwpvCe8fpyPQdQx1u-0EUwgAwR60bv8QQSmL1eyXZjCYnqJ0eapUU1vPyaP0J3YOBw5nPCPcDZx1PZRRCQ2t79cGSwokECERzP03AFbHhFrBT6u9tF9RKZuGoH9aFX65ZMKwdBKmfSVXCKT_fVZPO0cxFXXTwGTyXrV4xQiq9LnSHiNp2RxqsOaAWH-PSg45dssIWKxiNmb1Om9jgNuWI1SqjcZoW-UWHLghkQeeojjb2irA2kFHyha0MWuA58r2JLSWKf590aFXFnfF-MgoSllnXscnODZ5FBsJq4sLsfGbs1VrEKscDndND5dEESQlK37MzW2KM5Mz1GdJ9lduwhZhGixcI7vRW4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34552c022.mp4?token=vX0N99tdY2U1eabZSfbv3ldcenrgKtINJWBwbDWtjHTjlbdlhOu0obDL-m0S2gwtq26Iav6M6sAV2_3TB7cAaDRHLgjipfN_ug_1htUJBpn0u6cn-cl8QMPYWqcY1SG_EvV6Yc4Qm1mh8KsWOVcm3Mfe_6wGBwV9e7RMrthB_qtjiSmSEtvzSyMmfsl3zD-I9YiIk4xT321yZMYDnHHhMX7FoImF4XZu3VfVC7QV5Plslf6Af8HSy_yaoQqfU01yvIGMG6BKAaC-zMlUkGBaYh2M_sZ9-pfFLIxqOqD6cP2FXAYHtHK8Hpq4qieLfyVEFbaFE1lrvwpvCe8fpyPQdQx1u-0EUwgAwR60bv8QQSmL1eyXZjCYnqJ0eapUU1vPyaP0J3YOBw5nPCPcDZx1PZRRCQ2t79cGSwokECERzP03AFbHhFrBT6u9tF9RKZuGoH9aFX65ZMKwdBKmfSVXCKT_fVZPO0cxFXXTwGTyXrV4xQiq9LnSHiNp2RxqsOaAWH-PSg45dssIWKxiNmb1Om9jgNuWI1SqjcZoW-UWHLghkQeeojjb2irA2kFHyha0MWuA58r2JLSWKf590aFXFnfF-MgoSllnXscnODZ5FBsJq4sLsfGbs1VrEKscDndND5dEESQlK37MzW2KM5Mz1GdJ9lduwhZhGixcI7vRW4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
۵ گل‌بخودی عجیب تاریخ لیگ‌برتر ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103959" target="_blank">📅 13:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d709f3b074.mp4?token=Qu4lXxMFUe4vFNXUSx5MNB-YlSMIFkWktFIFwr6B0KAvffKP20Fr5-wZQGAdsLX2q9PiaVMgVpKbvyykd4o3Rugo3WfLmZ2H88i52CEZrbwjSgbrbh2TKE2TdK4uNhzgJkbXbJOulqTbbmkCOOjzFl71x891YAITBA1HQGr43QZguj2Eu16kMHhP7Ewx-vjiOn9v8hHKE4Xe6_fniWmWMndN4WO8eK05HIQ1nBWGe75DQIO1qdApzw-l1zXQ96FhEXTetdZh4XmMZKMQUO9Tc30TS3RmNnhYcEuMlOO4iojinCzmZ0H6QMV9xxeMt6LFBMknF4INFIU6pGa3nwdNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d709f3b074.mp4?token=Qu4lXxMFUe4vFNXUSx5MNB-YlSMIFkWktFIFwr6B0KAvffKP20Fr5-wZQGAdsLX2q9PiaVMgVpKbvyykd4o3Rugo3WfLmZ2H88i52CEZrbwjSgbrbh2TKE2TdK4uNhzgJkbXbJOulqTbbmkCOOjzFl71x891YAITBA1HQGr43QZguj2Eu16kMHhP7Ewx-vjiOn9v8hHKE4Xe6_fniWmWMndN4WO8eK05HIQ1nBWGe75DQIO1qdApzw-l1zXQ96FhEXTetdZh4XmMZKMQUO9Tc30TS3RmNnhYcEuMlOO4iojinCzmZ0H6QMV9xxeMt6LFBMknF4INFIU6pGa3nwdNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بررسی واكنش‌های جنجالی به خوش و بش بازيكنان پرسپوليس با داور بازى پرسپوليس و شمس آذر دكتر بيژن حيدرى⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103958" target="_blank">📅 13:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAQQlfkluXsE8tl8Uqd9wE83va4Lpf-N1w12pTlTGY0R8kCzZsyyiMv04wDLF9MWZ2PFrwMw6djCFqm2lRmxXygeN3w3KX5-_VBAPtSyU-EzklAoMHcchPRUXXoo6w-HUFxdeNEXA_ki68LrFlf-lYX0tgRETHbxIt29LSyYVMgank6cPKTZDsMF_LBZ4nT44fl_g2Q9boJte_BsmLpIMDSkaM-jueOC_PlkTdzLJlSKGXPe_xwZbgoM84qE2joeq6HGG2_eaOt-QYkC9sOGwx61yE32B-B9i1VeVCIq_4h7fQaacbMtCRFb4Nq3xeq9zcbKyPF73ngKO9LyTrNLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین بازیکنان یک‌دهه اخیر لالیگا در هرفصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103957" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHm6fElWLKZSrPy4LnObSdo7J8omoco6UPUav3T3QYeL575YWEgJ7UvUD5SoD_RxVRXbeBG3F_0Kf2shZsIhUfceiftg1lnWgtL_Pl4LRErRyFtRwjIywZrky6irJpyW44o8Gf_Jfcm9fLqFlhfdV88zoDUjrMk05JfB1pj-YdAqB3jH51Kx41kYvvcjWllEgdpqSomk7jOtWigcljbzjzIt0ogHtWbOvC1uhf_MnV9QQu0CVuXYDfNrGEVLg9YTA4yE8yyKMgSxLRlvBZIa3g-Ip6-YaU7aoWreW0Mb7G75nLEIuqPLe3cc6keQ73wcv0Mt1VMhqtTt8yVf6RuACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامه فسخ دوم یاسر آسانی با استقلال رونمایی شد
نامه رسمی فسخ قرارداد یاسر آسانی با استقلال منتشر شد. بر اساس این نامه، این بازیکن پس از پایان مهلت تعیین‌شده برای پرداخت مطالباتش، قرارداد خود با باشگاه استقلال را به‌صورت یک‌طرفه و با ادعای «دلیل موجه» فسخ کرده است.
همچنین پرونده آسانی در پنل فیفا ثبت شده و شکایت او علیه استقلال در جریان است. آسانی در این پرونده مبلغ ۱.۶۵ میلیون دلار به‌عنوان مطالبات و غرامت درخواست کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103956" target="_blank">📅 12:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103955">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇪🇸
🤯
پشماتون فر بخوره که رئال‌مادرید حدود ۲۰۰ میلیون یورو از فروش بازیکنان ذخیره خودش در فصل‌گذشته تونسته درآمد کسب کنه!!
💸
60 میلیون یورو از انتقال نیکو باز
💸
40 میلیون یورو از انتقال گارسیا به فولام
💸
20 میلیون یورو از انتقال ویکتور مونوز به لیورپول
💸
15 میلیون یورو از انتقال ماریو به میلان
💸
15 میلیون یورو از انتقال رودریگز به بورنموث
💸
12.5 میلیون یورو از انتقال خیمنز به بورنموث
💸
10 میلیون یورو برای انتقال پالاسیوس به فولام
💸
10 میلیون یورو برای انتقال اورتگا به استراسبورگ
💸
8 میلیون یورو از انتقال ویکتور به فیورنتینا
💸
4 میلیون یورو از انتقال گارسیا به بتیس
💸
3.5 میلیون یورو از انتقال مارتین به ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103955" target="_blank">📅 12:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103954">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVibQqUuILAefmgYyN9-adXGGjMsAZTCfSdIC-bUuF6Dg8jEOe8OgoNTiTQCNswa3DNDxLxEskThXRwuRduGboQPWFQavibHPE16TLR8RhIdfYksPcLHoZC5ozBgkCOwHJgzmDWJhHwanOiARS5iHPTk81iolC1W-FhQt0ZhzNkC9yexqVgF4R1IKeFus0JCSGZBw00H9RTIFotIbaGqfzUAy-GBDu2mQYJNRRXujXL2RqzveNDVF2Ux99wMS8jMOZFoBrTcRg22bq-nCkLJrA7DolOwiFnpcHS03-bo5si9ucyKpfRV2N6MOmNRdOX4YmPYQMcFijK-7NLshT3p4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
پوستر تماشایی باشگاه استقلال برای تقابل فرداشب با نساجی مازندران در لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103954" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103953">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908dffe6e9.mp4?token=XJLS1iqTHOGwQk83g9ewh75adNNHEFTk1_q7yDgFXRnsEBIuKmY2nvwr-0fYA4cL7ZWYJe0YXrHDyuOe3BfzO_8550R639LbNbDAHU5100WS0PHoVmmCqHI9EHhZBdSFLzuCKQGSWagmTEJt3KK3ne3m2PXjxWNe-IeUr6EyvKWd3Qm4v_6kdromrZq6YOsEsUw0uKaHtxiyhn3I6xPBuR3qdR-Jx0d7wSVkyJYBXXJ-6TW95F_-IyY2zvAxL_HjMLYZHcojtUSWEin7C0Rmsz0uncEus4vXIF3D-vEVw27I1ZG3qGFow4r7GGwle0ujqY6PYi_6Tw0VT1Xuk7NRDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908dffe6e9.mp4?token=XJLS1iqTHOGwQk83g9ewh75adNNHEFTk1_q7yDgFXRnsEBIuKmY2nvwr-0fYA4cL7ZWYJe0YXrHDyuOe3BfzO_8550R639LbNbDAHU5100WS0PHoVmmCqHI9EHhZBdSFLzuCKQGSWagmTEJt3KK3ne3m2PXjxWNe-IeUr6EyvKWd3Qm4v_6kdromrZq6YOsEsUw0uKaHtxiyhn3I6xPBuR3qdR-Jx0d7wSVkyJYBXXJ-6TW95F_-IyY2zvAxL_HjMLYZHcojtUSWEin7C0Rmsz0uncEus4vXIF3D-vEVw27I1ZG3qGFow4r7GGwle0ujqY6PYi_6Tw0VT1Xuk7NRDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇮🇷
سهراب بختیاری‌زاده برای اینکه ریز برا استقلالیا بماله از مصاحبه‌های فرهاد مجیدی مایه میذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103953" target="_blank">📅 12:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103952">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9760c12668.mp4?token=s-voo9uuV60_iaOclKGICapu7GQGxEvjDYgvHuM1FcUc73aaoXFpwEBN7QhwqfCM_HRNzP2mw6StnaEPN6zyi9hV-Or_RUN2JKW3D4rT6y6HkbxZfB-CU296_uiOs1B3SnDmum3dadGOzidoHKsgBFlJQ8pLm1OkhM8h_LaJkt2J3u5Am7_sv_a4S24q7OjgvcUprHmOFxbtxz24YdCtdEFOqKbE4y51LUFFY90bQh9TU7Eix5fsjY59IF60L2rOcv23r9Pa6gJoZowYgBP-sgCwlD-tpKG8BXC0KwY4imTAcOsYTEtxkWLS0M04r9PKLgiyqYMse0QowGdpl9fHEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9760c12668.mp4?token=s-voo9uuV60_iaOclKGICapu7GQGxEvjDYgvHuM1FcUc73aaoXFpwEBN7QhwqfCM_HRNzP2mw6StnaEPN6zyi9hV-Or_RUN2JKW3D4rT6y6HkbxZfB-CU296_uiOs1B3SnDmum3dadGOzidoHKsgBFlJQ8pLm1OkhM8h_LaJkt2J3u5Am7_sv_a4S24q7OjgvcUprHmOFxbtxz24YdCtdEFOqKbE4y51LUFFY90bQh9TU7Eix5fsjY59IF60L2rOcv23r9Pa6gJoZowYgBP-sgCwlD-tpKG8BXC0KwY4imTAcOsYTEtxkWLS0M04r9PKLgiyqYMse0QowGdpl9fHEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تاجرنیا: اینکه من نتوانستم پنجره را باز کنم ربطی به کم‌توجهی من به تیم فوتبال استقلال ندارد
انتقادات نباید طوری باشد که من از کارهای خوبم در استقلال پشیمان شوم.
وکیل به من امید داد و من هم به هواداران. حالا اینکه پنجره باز نشده مقصر من نیستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103952" target="_blank">📅 12:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103951">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eecbdca57.mp4?token=cDU3rfnZirjSxvv7vU4oLJnrj6z1twl6DeVgmZaMjxeeeXwHpTVIKKhA3j-dykHydZ8JK2l_TJPRgb6-q1VjaNri2UYOtXIxQidDp5RFbeqk6j1i53uf6TOM1v4jU6LT9Vx5hUCHZRX2AmaqofKwIB0G5Ys7T2WWdWfJBlWXSn3YS9D5dkra_nXj12VKn8v19GLVQpd-z-wuP0tl0bk8JBMaeHXiMOQoN4lrbjW1qikdpdAUVKFtXNBYlcwH6BO6z4JTEshJf9D5dDptmFqE4Wg9vh3ED03bWfRccmU49sDetIrJ7wuw2cnu_phpwYBTwxVEK-8rirOGGdOTbrVdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eecbdca57.mp4?token=cDU3rfnZirjSxvv7vU4oLJnrj6z1twl6DeVgmZaMjxeeeXwHpTVIKKhA3j-dykHydZ8JK2l_TJPRgb6-q1VjaNri2UYOtXIxQidDp5RFbeqk6j1i53uf6TOM1v4jU6LT9Vx5hUCHZRX2AmaqofKwIB0G5Ys7T2WWdWfJBlWXSn3YS9D5dkra_nXj12VKn8v19GLVQpd-z-wuP0tl0bk8JBMaeHXiMOQoN4lrbjW1qikdpdAUVKFtXNBYlcwH6BO6z4JTEshJf9D5dDptmFqE4Wg9vh3ED03bWfRccmU49sDetIrJ7wuw2cnu_phpwYBTwxVEK-8rirOGGdOTbrVdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مارسکا بعد از شکست مقابل آرسنال: "من در کل همیشه نگرانم، حتی وقتی بازی‌ها رو می‌بریم؛ حالا تصور کن الان که بازی رو نبردیم چطوری‌ام."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103951" target="_blank">📅 11:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103950">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ba20e0a3.mp4?token=mGhmEQ2NemxpLZY--tTPAOXV35RgmJiS-dmycdHDfP_11aeNkvqWyRJSDOnzsgkyyUZdgasHuk_kXyWYoDAjC8pupmeNm0HTWYJBV6kI4O24gEvCJwjNqy59cwdT6zGZC_jZZt4m1_BtHetAtFy90mdFAwK0iTfNmD3XZKOKraS3AwSsV9LZX2K1oU3v95WKUCHrGZIamBw7G0GOI_5826p9CtbdoSgxk_pTs6kKXjNN3OQz62chZsBwNLV_9xbLGALq5BNmQuTvupNwiz93MikIAELsbu-HqdKJS5OSx9kGXfkAPumGP4SxrvK2gJP7481_COp7VGO7asmf8-1aL5gFB0laeXLgY8yJ132iW2dM9f1S1YYlz0ETLDmKRtVqJBfmwOQM7VvJufpTtwa3lNmuoJv4Ks7RDPJVTA5UGdhnOFyTGOTUKfJ2vgD8alxDVE6EI43wvegPzoilgUt5qGdHFq_jiTd0EH0A3uZfn4pjTPvIJwyI9qsI10MfWrLtkvjDbI9NTGm0edKaSvu-DAdV4p0mlSEEPl3vN7apykC_aoMe3Py5Z0wDOFqt2j3IOUNoXiYKWJmtNDgKcHHZC44XOK98N-GadIwjeWxI5aRUXNtZatADiH0ZEHhJ24glXu_N1FKgLnzAyB9jwomrOzrqQ22-q1A2rb8_IM8Ytoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ba20e0a3.mp4?token=mGhmEQ2NemxpLZY--tTPAOXV35RgmJiS-dmycdHDfP_11aeNkvqWyRJSDOnzsgkyyUZdgasHuk_kXyWYoDAjC8pupmeNm0HTWYJBV6kI4O24gEvCJwjNqy59cwdT6zGZC_jZZt4m1_BtHetAtFy90mdFAwK0iTfNmD3XZKOKraS3AwSsV9LZX2K1oU3v95WKUCHrGZIamBw7G0GOI_5826p9CtbdoSgxk_pTs6kKXjNN3OQz62chZsBwNLV_9xbLGALq5BNmQuTvupNwiz93MikIAELsbu-HqdKJS5OSx9kGXfkAPumGP4SxrvK2gJP7481_COp7VGO7asmf8-1aL5gFB0laeXLgY8yJ132iW2dM9f1S1YYlz0ETLDmKRtVqJBfmwOQM7VvJufpTtwa3lNmuoJv4Ks7RDPJVTA5UGdhnOFyTGOTUKfJ2vgD8alxDVE6EI43wvegPzoilgUt5qGdHFq_jiTd0EH0A3uZfn4pjTPvIJwyI9qsI10MfWrLtkvjDbI9NTGm0edKaSvu-DAdV4p0mlSEEPl3vN7apykC_aoMe3Py5Z0wDOFqt2j3IOUNoXiYKWJmtNDgKcHHZC44XOK98N-GadIwjeWxI5aRUXNtZatADiH0ZEHhJ24glXu_N1FKgLnzAyB9jwomrOzrqQ22-q1A2rb8_IM8Ytoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خداداد عزیزی: زندگی خیلی سختی رو گذروندم. با پدرم گچکاری میرفتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103950" target="_blank">📅 11:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103949">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9244a473.mp4?token=D4QDH78_Z8f4cyH_WQz5wzBSGlWJWMEpv526A2-u4D-4USe12dVvK5PJYUUWYGrEAagnX-fhJRZ-se4RmOU1XFolYZjYq_oF4U-sGtNVdZQ_Gdn_d6C0yZdWaJRx9BXQxPS7tI_-UZ-9YrjpwV4-BvqHKzBnCk_9e93sTu2Iwe9-PRIYYuqvzVw5BHVDbzvPl_3IsaT9-z_bqhznH2lNV9oyEkzoex39n5f70Ku8Ln31IwHktAi7dLvv3ajd2IGAARakGWU9yzjMDWNvhVryFMJKHO0dXAoAC46v_qwlQxgVCAMOV_3nzbf7n5vaUwjHXFyEjqteEMAKlBYFf7FqOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9244a473.mp4?token=D4QDH78_Z8f4cyH_WQz5wzBSGlWJWMEpv526A2-u4D-4USe12dVvK5PJYUUWYGrEAagnX-fhJRZ-se4RmOU1XFolYZjYq_oF4U-sGtNVdZQ_Gdn_d6C0yZdWaJRx9BXQxPS7tI_-UZ-9YrjpwV4-BvqHKzBnCk_9e93sTu2Iwe9-PRIYYuqvzVw5BHVDbzvPl_3IsaT9-z_bqhznH2lNV9oyEkzoex39n5f70Ku8Ln31IwHktAi7dLvv3ajd2IGAARakGWU9yzjMDWNvhVryFMJKHO0dXAoAC46v_qwlQxgVCAMOV_3nzbf7n5vaUwjHXFyEjqteEMAKlBYFf7FqOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✅
🇫🇷
هوادارای دیژون تو لیگ 2 فرانسه از این به بعد جای بلیت کاغذی باید شال با خودشون به ورزشگاه ببرن، تو هر شال یه تراشه الکتریکی وجود داره که حکم بلیت رو داره
تو پریمیرلیگ ایران هم تماشاگران از در و دیوار باید وارد ورزشگاه بشن تا هرکسی بتونه صندلی بهتری بشینه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103949" target="_blank">📅 11:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103948">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c1acd77e.mp4?token=KHZbsXSoRa2x20X9syy0VfsiH_I5qDguaplQQUZh5--33Rvr0T12Uo8l87yUgIomYI2UjioceiSSu02_TX5lCFQcNnR7nnZ0gMdjFHVrOaLvqsPMI8VerYxvQM-sHfCiNBO9V5xZuYlyobiN13Nxh9t3My-BFi2xS2rotMFIR1VNGsa5z6AvielL5kvgDjee3r5ZXeMsD9NAP1WBfoikXNbdTVsWr0sFu1eISF_o8uANMyMY75JpOg9B8seyoLlr3qUEi6hfkY1qULTj0iw6IBzD9ssuPRmGs3iOdgZAPYjseSXGi4DANeoTXtFdzjE-EuOGiUSaNOUjK3zmz7D23A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c1acd77e.mp4?token=KHZbsXSoRa2x20X9syy0VfsiH_I5qDguaplQQUZh5--33Rvr0T12Uo8l87yUgIomYI2UjioceiSSu02_TX5lCFQcNnR7nnZ0gMdjFHVrOaLvqsPMI8VerYxvQM-sHfCiNBO9V5xZuYlyobiN13Nxh9t3My-BFi2xS2rotMFIR1VNGsa5z6AvielL5kvgDjee3r5ZXeMsD9NAP1WBfoikXNbdTVsWr0sFu1eISF_o8uANMyMY75JpOg9B8seyoLlr3qUEi6hfkY1qULTj0iw6IBzD9ssuPRmGs3iOdgZAPYjseSXGi4DANeoTXtFdzjE-EuOGiUSaNOUjK3zmz7D23A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاکتیک جالب دیروز آرسنال مقابل سیتیزن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103948" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103947">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103947" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103947" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103946">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQrbm2WTwRyBP0BuZ7xkDM0EmUWDzOv6o5mJh02vYbvkrqj0VZc-Wzhwe366w_0LSRBMI2ZnXSpWBnMA1r7w-tPeJKCENLVZvD4cPJwjf8w4C_IlTCz01nJATJTgpjlAWX5tUHHBYP2knrsaWdd_vpy8Wkxlyu04U1IGdJcYHjpYREOw5Wb1SzxM4YKSCe3N5Lt43yQ7w4mjo21eSsQO5YRo7ptOBYOJQ_eEgb2I4sN11-VZcK1VEA3jDLZjdmw41gq9dAdottrCy85ASNut-yMMwCBtXDSrau-WwZ_r6fhpF44YandGt9mZf1KWLVwdMmsPupT0U8DYj-63LpCCGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r26
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103946" target="_blank">📅 11:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103945">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJUaONHreh5b-7ebOgXDqhfzj58tWvFSu2b5I4es9zOiK5_DOSdW0TrYFoI_vjH95lmkORz6N7QbH2UVSZowra9zEgQrzYunw4h93Baxo36DJKB3zIRZTRdnQuv5wkwNDlIb7skj3ujBmsVdORAlCcA1UKmOwmcgyeHyZ9Q813zOkxB2F9ci9OoO0qssvgORHBiqgfgRFoFAq_kRhIMV7ved87fjFO0YBqDq8hw3b-KWItT-oVoOy8RYPIscYtcOuqR8zc-aiTveKENlzTY9y_mkDUJirrPp9NaE_FeHDD9YjWXF42SZ7CZ4qFR9f031Hp5m3ofF4jtxgO_B5ds0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
رومانو: ویکاریو سنگربان تاتنهام به یوونتوس با قرارداد قرضی بدون بند خرید اجباری
HERE WE GO
✅
✅
✅
✅
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103945" target="_blank">📅 11:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103944">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f807afbf18.mp4?token=CtU_sU8KZUe9zxY_o4uIQ2BDNfcvivpUBiISgpCDjVr7V-VZd2D--P6HLMVG6c7eh4x70jdg1rAswT__t1NBlTKkmQrFVzR3E4a-FVwDNJ9CPI9rZ6wppgR4WFednoo48PxXFqtQUls_boPpwEbd_WoxMB8EBIbBekQCjheqbxABV35TtRGUQxUfDMcERZdSPpNiejAtysl8g55qwRIJhhdMHZiUHz5R3hG9AjtbN4hg93Y2zd0a-MfHseoCnVf-MjGNIDlYFwY9G38zq9RmByTVOZzm2j5Vvc2ZMxxObs3B1ySVXO690Vm0g8NqVyhv4i20iGQ-9i1ZQ8rai1w6_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f807afbf18.mp4?token=CtU_sU8KZUe9zxY_o4uIQ2BDNfcvivpUBiISgpCDjVr7V-VZd2D--P6HLMVG6c7eh4x70jdg1rAswT__t1NBlTKkmQrFVzR3E4a-FVwDNJ9CPI9rZ6wppgR4WFednoo48PxXFqtQUls_boPpwEbd_WoxMB8EBIbBekQCjheqbxABV35TtRGUQxUfDMcERZdSPpNiejAtysl8g55qwRIJhhdMHZiUHz5R3hG9AjtbN4hg93Y2zd0a-MfHseoCnVf-MjGNIDlYFwY9G38zq9RmByTVOZzm2j5Vvc2ZMxxObs3B1ySVXO690Vm0g8NqVyhv4i20iGQ-9i1ZQ8rai1w6_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚠️
‼️
دختره همچنان دست بردار رامین‌ رضاییان نیست: رامین‌رضاییان ازم خواست که عکسای لختی بدم بهش. دقیقا میخواست مشابه کارایی که جفری اپستین انجام می‌داد!! درخواست سکس با دوستام رو هم داشت! دعوتم کرد که باهاش برم پارتی و این چیزا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103944" target="_blank">📅 11:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103943">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkJx7hNHHfj6I0_Ld0cIw-rBQYkPRWq_N9FgTvH2VDJPiA22ixWOrs4YzGz20XI5sTtov4B_VCMGlZoVn-DutgHfnBw-ZcUfAk6en6urbZ9m33CHipCyyYfwkZOGGWn18qddnTG8x9VSVhzCo1cTfkNrNR9DLe2VNou4zxCR0r8Xjggs-OotQMeWv77MsrKlFLciegwf_Bqa0Ls2Q72rjFLYM4LaOfPxnYgkLOxCKFg1sbC9Div8u74G2ka_IeS5aMI6j_FJvhQixMXGdYQ6GL8JO79SCQxUqkuYa7nMvkK0WKDRjXV7d3C3r481SMT9Luy90oc0t-FYmW4IPy5msA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از شبکه الچرینگیتو: بارسلونا میخواد برای جذب گیوکرش از آرسنال اقدام کنه! گیوکرش گزینه جانشین فران‌تورس هست و هدف اصلی بارسلونا همچنان جذب خولیان آلوارزه
👀
❌
برخی منابع از معاوضه این بازیکن با ژول‌کونده خبر میدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103943" target="_blank">📅 10:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103942">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2151ad88d8.mp4?token=QWz5DKgeWLhwdR3mUwF4aCGMaEa3ijGenkAjEXIK7jQRK3W_ehV0GCk5yWS5gC7GZ3eXkjywNX7cnPq76rZ0K6iqKGdRMdK4Fp2qS2Ku9b0dUh68QIJVrynjOkL9feq5qXyDnLHwpCUk3Dl1rxFBsQjsV6W_lWCdukoGH9rK4N2vFMKfH1OW2tmurvlHV0FmRSS7nGvyVALjvuMvJxUL7RbOzyAnF4yxMeJmjhwam_0N2r33GrNEtaTusmRn79Sl-CelybEDjLMjCD0qRoQPclhdmQYSjxi7RvKYRyjLe4nYvljHrbBIExk8Tm56tW95aeNDgG4P9XhtIs0Xx_lwfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2151ad88d8.mp4?token=QWz5DKgeWLhwdR3mUwF4aCGMaEa3ijGenkAjEXIK7jQRK3W_ehV0GCk5yWS5gC7GZ3eXkjywNX7cnPq76rZ0K6iqKGdRMdK4Fp2qS2Ku9b0dUh68QIJVrynjOkL9feq5qXyDnLHwpCUk3Dl1rxFBsQjsV6W_lWCdukoGH9rK4N2vFMKfH1OW2tmurvlHV0FmRSS7nGvyVALjvuMvJxUL7RbOzyAnF4yxMeJmjhwam_0N2r33GrNEtaTusmRn79Sl-CelybEDjLMjCD0qRoQPclhdmQYSjxi7RvKYRyjLe4nYvljHrbBIExk8Tm56tW95aeNDgG4P9XhtIs0Xx_lwfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
خط‌حمله وحشی و حشری فصل‌آینده psg
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103942" target="_blank">📅 10:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103941">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpXInnyASpPF8-Guj7qt_p0WaTtPSIhz5J1MlqmRW1MfVL-gPFiVjFxpUoIbXPboktT-RCq0iq5yAI1ZmYkJ7sRqYgz5zlLXTFljKJscuiCwPUmngeQwBSGtdfL51G8LFfRZCEzxvESSTyRvzox561m7_oFWL-FnlFyCCrH8zqRfUsrKqcYVUa2J9fpy64rMIL8_uVFS1X2Qt-BHqrXcAkS3b-ZG58eHD4YSnfcuf-IxzOyj0Qp01EeObx8Ar_iXwnuXkb-K0BRMcnytOkrjKs1XJqvTebfcXPaIiMdUA2C1uaHLUvTQ7BLRm5vwk2ZuOJay1ZOm3BDotR3cLWAiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
🇮🇷
مهدی هاشم‌نژاد ستاره تراکتور بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103941" target="_blank">📅 10:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103940">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbe4bacfb.mp4?token=QUmpEWS7inoWl7us3x7jgX2N9jMANnySkZUkjeUpmN7CgQGZh3iRqY88kAJtPbN_7_a-JaV01YMTcRz0WpS2zAEl5zcAOSppkOG7VcWZwMhQwgRngC6zYLXyd0b-K3krNHq6V5db46lkJUtqTlb-V0buKPnZNTVBc8HxqaxPs2poBfOaXAxSMjImernduZe-jjice0knpX9GlQR4ur9-nYvZCe3UcheDvzw0Mwjbc-CYqMD5ixBu5xiZ7mLMWcPzE-_G5Qzwd8QIK6YOIKJAAcW7kEGhlbIzUSfSFWgzhjj0lPCUkrcQESGWHcPCjhUPO7HaroxnqpxfRaLVlbbPZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbe4bacfb.mp4?token=QUmpEWS7inoWl7us3x7jgX2N9jMANnySkZUkjeUpmN7CgQGZh3iRqY88kAJtPbN_7_a-JaV01YMTcRz0WpS2zAEl5zcAOSppkOG7VcWZwMhQwgRngC6zYLXyd0b-K3krNHq6V5db46lkJUtqTlb-V0buKPnZNTVBc8HxqaxPs2poBfOaXAxSMjImernduZe-jjice0knpX9GlQR4ur9-nYvZCe3UcheDvzw0Mwjbc-CYqMD5ixBu5xiZ7mLMWcPzE-_G5Qzwd8QIK6YOIKJAAcW7kEGhlbIzUSfSFWgzhjj0lPCUkrcQESGWHcPCjhUPO7HaroxnqpxfRaLVlbbPZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇩🇪
گرمازدگی جمال موسیالا در بازی اخیر بایرن که با خوش‌شانسی خطر رفع شد
درحالی‌که دمای هوا آلمان حین بازی ۳۰ درجه بوده! واکنش مردم جنوب با دمای ۶۰ درجه:
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103940" target="_blank">📅 10:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=T-CxlQ5qEVBJzfQqct4dz4S9Zn3zcbTEBe1nRDaLU9bLA5tiW0P-KXD3MGcmopt3hSx06M2Jjbs8gsjPiQUIAL5_6j7NfYF0RyiqRLrD1ArWrSp4fCblR9uEKMpdo9ytTRrZPKZMLFH4Kq99snPOuTSM4Mo1qumui0HxVEzeD0rZPXhUECJCkRWhK47QUwdtZ3LZI2GQ5oQUX_X_XilLXZGVyMDM9rgLPmXah623TpVokf7XXxRYEzmULHt9qmLmsd3hOBnPe82GXcCnClHn2ywzFgOrKlVog7w-A4fW4HYgF_rtxXBG3DqQAjGc5g8rN-uWqlEaNchkDbISsoV7AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1875da2c0.mp4?token=T-CxlQ5qEVBJzfQqct4dz4S9Zn3zcbTEBe1nRDaLU9bLA5tiW0P-KXD3MGcmopt3hSx06M2Jjbs8gsjPiQUIAL5_6j7NfYF0RyiqRLrD1ArWrSp4fCblR9uEKMpdo9ytTRrZPKZMLFH4Kq99snPOuTSM4Mo1qumui0HxVEzeD0rZPXhUECJCkRWhK47QUwdtZ3LZI2GQ5oQUX_X_XilLXZGVyMDM9rgLPmXah623TpVokf7XXxRYEzmULHt9qmLmsd3hOBnPe82GXcCnClHn2ywzFgOrKlVog7w-A4fW4HYgF_rtxXBG3DqQAjGc5g8rN-uWqlEaNchkDbISsoV7AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آنالیز فنی بازی هفته‌اول لیگ‌برتر میان شمس‌آذر - پرسپولیس توسط محمد تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103939" target="_blank">📅 09:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103938">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0698ccdb66.mp4?token=D2rtwtKPcmQ-3fJ_wXpUWogfXTa9te0lrHn5bvqTAVj-DqHfJ-TOngRtiGqxzkQRVRTRK0XJsqjtt-yM4YJASjusQ6ieoXNRj_AuZ6cDjVckyXjlBPHvuZvwSq2BLRRwWBrrVnSMPZAVZ8WnAJsosKX6y7jD53xhdQ_gVlX_q0SsYn-Sy7sT9kcuxNJFRlPgSkmI6YYm7RkssWKreB7vU-M5a7q3w7VSv_JAisJJvaYrZGbwGb4X-doQUlTGVwW_dIShlYCsWVud0THk73E8YoP5Ldv1VyjZCnSE7BT-w--WVuD7G5lWoH-JjUIjTztRyYvhJKFXe5I_QisukJMXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0698ccdb66.mp4?token=D2rtwtKPcmQ-3fJ_wXpUWogfXTa9te0lrHn5bvqTAVj-DqHfJ-TOngRtiGqxzkQRVRTRK0XJsqjtt-yM4YJASjusQ6ieoXNRj_AuZ6cDjVckyXjlBPHvuZvwSq2BLRRwWBrrVnSMPZAVZ8WnAJsosKX6y7jD53xhdQ_gVlX_q0SsYn-Sy7sT9kcuxNJFRlPgSkmI6YYm7RkssWKreB7vU-M5a7q3w7VSv_JAisJJvaYrZGbwGb4X-doQUlTGVwW_dIShlYCsWVud0THk73E8YoP5Ldv1VyjZCnSE7BT-w--WVuD7G5lWoH-JjUIjTztRyYvhJKFXe5I_QisukJMXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
دیشب تیاگو مندز تو بازی مقابل سانتوس این شکلی نیمار رو دایورت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103938" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103937">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r64E-p1Y0CbmyQaVNml7v_j7n_nmuuy5nk_UTCabJI58bGxIMs5JLkGgsJlYhEu2jSNKbVTeFYTgCulxT0-SaTq0A22WODuNkSGNLmVZdYPBpEYnCVMLtA4qcIA1XUM_jLAhZLz5e0ly4q85YBlkAIGRP14XOsoMl4KmYhgkpOJC7R_uOq35C1iKJK4E5FyBHPHmoo4ziIXBzvUvicyP2v4W_TK9bCVvrZ5k176dE1r1ybaRi_NAmiGB0BB-Ns_OhCtxT12hvvcNW6oFrYtw1cXNSMvCDXL9njGZJussg1vpcLFGpyDpr6CiXfo1xlwlwFuenmKVCSoup_H5R7dt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
سرمربیان بزرگی که در رده ملی فعالیت میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/103937" target="_blank">📅 09:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103936">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJJ5lxHm5R0881WJ8ILIRenbJWLDCN6kA2a1FSFts-Blr8fhfBliE6RVTqJmPMagUvNcZ6np2HS0jq1K8HIU4MOiNMXVeX72O0H1NOiFrD9oOaxps7a7BkCkTwWEc8emO8qivlzDMdRCBKFfneekYsrfsbDnvo2nsk-fFy4rd-gkcGE3DYrCgP1HrmunSVkE9aFUHzexiGbFcfPrk5itF0TSnLFhWGpeNPkGgizPjmWTsJ9ASIYoAutr7DLCNoKehNNVZSiCttmLgD5jbQDaLWKTLxvZen37aKyJNjM8Vx4R8xp5fQU5qI7uYcmbDNbxlasg4FIXyniZmUdP7ONBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از شبکه الچرینگیتو: بارسلونا میخواد برای جذب گیوکرش از آرسنال اقدام کنه! گیوکرش گزینه جانشین فران‌تورس هست و هدف اصلی بارسلونا همچنان جذب خولیان آلوارزه
👀
❌
برخی منابع از معاوضه این بازیکن با ژول‌کونده خبر میدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/103936" target="_blank">📅 02:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccba4b58f.mp4?token=udEDk7XiGy4-bKZf70hvLa7mdbMyTGhhwnNa5C6RCQqRF1h2ew6KFfApsjMxLmByamub423ikZaCAdz3Zj_wggMZXKicZYzp5pETwo5haRPlUxdkUkky5PhEiV9mB2qHAWCR3J4bbeUIDWFDMGtX_oKSc9lWqNdbreCnEwTfFibW423Df52L7sOzi2HRbKXCzjghIxTqB4eLVcowEF3DX0PB-YIlX-mA0qShiLb9cXPiVbknxKUYoy-TjiExdLZidCsOqCLNwJ1ftFbWtFmafbMKIbJ0x_savHiQw_K4tGswo4t4TLSG4dENIJxpQg-hrJC2PxhBsU4-950Bpoiz-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccba4b58f.mp4?token=udEDk7XiGy4-bKZf70hvLa7mdbMyTGhhwnNa5C6RCQqRF1h2ew6KFfApsjMxLmByamub423ikZaCAdz3Zj_wggMZXKicZYzp5pETwo5haRPlUxdkUkky5PhEiV9mB2qHAWCR3J4bbeUIDWFDMGtX_oKSc9lWqNdbreCnEwTfFibW423Df52L7sOzi2HRbKXCzjghIxTqB4eLVcowEF3DX0PB-YIlX-mA0qShiLb9cXPiVbknxKUYoy-TjiExdLZidCsOqCLNwJ1ftFbWtFmafbMKIbJ0x_savHiQw_K4tGswo4t4TLSG4dENIJxpQg-hrJC2PxhBsU4-950Bpoiz-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
💥
ویدیو جذاب از مراسم ازدواج رونالدو و جورجینا؛ حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/103935" target="_blank">📅 01:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103934">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPGLvHaJnOUYLwB0GRUI1mOK0WW5_QHaib-PGPXAFrp23bcpbZ9oPlKUKvj_j-hiJFpojmvBQacyUbwd7_COGOJDqGtuMQmQxSJFU-p70mj8HJmydLzgi4ucOrL2r6fAaKgvmbkjr85wY--G2qHGDoENwSa-6kuvE3Oa7ueNM3FK0ZEkq__JR8M2gjQZH_prynJV-JK1ulsZ023Q9ZWS11-jArsmvp8pK19e9NfdHlx5a9k_SQkgCyG32d0XG3hhWOFReKQBnYZN95jGIrXjOusidHmcoMdulDc1nXbwX_NcSBavtF4xJtlKyAkcLFlyA-cJyN0ZomlbIduT7oi6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
🇮🇷
باشگاه پرسپولیس: اورونوف هیچ درخواست خروجی نداده و شایعات منتشر شده در ساعات اخیر اساسا کذبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/103934" target="_blank">📅 01:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103933">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
🚨
🚨
🚨
نوید محمدزاده: قبلا هم از فلسطین حمایت کردم الان هم میکنم چون با اسرائیل حال نمیکنم. مارادونا و رونالدو اسطوره‌های زندگیمن و اوناهم طرف فلسطین بودن. من نه طرفدار حکومتم نه طرفدار شمام فقط طرفدار ایرانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/103933" target="_blank">📅 01:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103931">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6UoKLaMSiT2P-UzyzKnriNEiqGTubOnggvppXJadg-BBSDFoEvkjFEnalhmpWM8t6PBQlOJQAeqktFUpOux5hlQDMTcQTGFdL0XczLPcOk2ZzoJ9BSmJNDD7LoTv5LpSFKb60jJAypxPp1-1ySVISiRGKL08yp4eaI7-yVzYm5mqDHY6M7vOfcwG7o8heHEmlyH4A4_u14VXUZtaLMXMh5NShfz66F7MCZQJuzYO28FhM9TTdAPPpgOHL_xb-JEIAyGTbA7wQ_4zsZua9rPOhXTc96XLF0j22y0CVn2Tjq7atRZ0gtXbOTcx8lbhDaBtpcd6h2OtI7JD5T-EHZbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVUyd8tbVpse-6-8f1oFOMd7RqXgVyEhAhdt2GliWCKXt8U15dsigs6Ix7P_hb8eOu2nkikcPUXIPH4WNj2tYBY2blnGc0BBELdI4x1eZpF46P6k8RbMgRek9j-jneYggo7-hAGTTiRkjdyR7TEw68rZG0MkHLDC2fhS2Tw86yq-wgR_E66Y_Bq68h0ZHRvHGCTsSdM8knpec_IO_zak7kQw6pXCUvzN_IH1JRfojzhbpGpxV_eXvMwoTMC6cfiaiz5OEoETmYLnZFktBhV2JtIRuLfaY0pFByyG15XnXpejmyxYRDYxbm8QYTVxcyyaCOhoJoO1B0yq5FrzSqxM2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاپ قهرمانی در دستان بازیکنان لانس.
❤️
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103931" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103928">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMhaN-0JMozo3RAsmlj5_3PdoWgwWsnK7tnEWUyLw-UWyjshoJEIq0BSuoST8igyVTWc5j05TkxCUQJQMb7EzPb0wQFmf9OTkH-PxTTv6nNziKCYiY_6GmUkUnE5nOlze6uww4xoabz77O_FeG3lPG6dDpmcMomSWz91_w0Dw47xKaTv892gNcs_WjWRPv3bIdLbz7l3HZuD7XZAY6Sfvc-5hStr2uFfN5nDAZplVQ7skSa9xOSm6LRKcfFgsa9SrE8DZ57PRuNTV4uN416V0BbOByPZlLHyvggk3HgTrRLfyKbznD9naxD1rflsxwgcDG_Q8ysOCcPIlr3U-81nQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سوپرکاپ فوتبال فرانسه؛ ۹۰ دقیقه تلاش فوق‌العاده لانس برای قهرمانی؛ تیم وحشی انریکه مقابل حریفش آچمز شد و جام را از دست داد
⚽️
پاریس‌سن‌ژرمن 0 - 1 لانس
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/103928" target="_blank">📅 00:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103927">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0ba339f4.mp4?token=Sp-SmXciGBwsRvSsMCwCthXP8kkCG6BEwxjFLpNK1u3G1Ib7iOJ3YChYoQ2PjwmY2G6XBZTD0wpN-91RKnHGdYedSXuaO3EVgDliFqwW3InyJyucUNOzYpid-rQSH1E284kUyV0kO68h1reDLxt8rTkLVoSlgrXTdcLt0Hq40LAgTNMYw9bwKXc6bO7U-VuPDVNdkRQ8rMVwkhq7BG8ENXM8qnFtFdGaxz7uZfsTa9l-r6FsAQjMtwTVk9jLnilaNrHbWyo8DHLxIUJjU1nY1QVJzE3kOYCyXR_DH0QICTcXp3duR4QDl-dVcRULMsp1cqoWsYKpo-RR7LwpMe0pmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0ba339f4.mp4?token=Sp-SmXciGBwsRvSsMCwCthXP8kkCG6BEwxjFLpNK1u3G1Ib7iOJ3YChYoQ2PjwmY2G6XBZTD0wpN-91RKnHGdYedSXuaO3EVgDliFqwW3InyJyucUNOzYpid-rQSH1E284kUyV0kO68h1reDLxt8rTkLVoSlgrXTdcLt0Hq40LAgTNMYw9bwKXc6bO7U-VuPDVNdkRQ8rMVwkhq7BG8ENXM8qnFtFdGaxz7uZfsTa9l-r6FsAQjMtwTVk9jLnilaNrHbWyo8DHLxIUJjU1nY1QVJzE3kOYCyXR_DH0QICTcXp3duR4QDl-dVcRULMsp1cqoWsYKpo-RR7LwpMe0pmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
خلاصه که گنده‌گوزی آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103927" target="_blank">📅 23:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fefaf274f.mp4?token=rirIv0cZitkkgFjkIOlrQDPVpnMZu-ku52foQofYNdeRmV0yIRiQYMrhoNZoNXFvjMOQxlH-GrTgueR42YmcUeP8LEUyirZCRofy0E07ElFLCQ5YMwwK4bON2fCoYu-afcYmIEx8s3OplRM_xoXp2F2Sz47cn-i4D7G4cPLB1SySou2HUdzZ2edpEptWjU6P_3NBn2QblvnTZJpVwnM38lnUt015OGpDwvrvA6btmDY1B5Jupzglxv_H1mnh7Fisuk79-8ZapPttKSsUBezIOtLqQdLE6n0_QoX2coGVc-t4CWD5-ImuaqoL0MLOJcD7Nvz36AKpTeImIe-_fN80NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fefaf274f.mp4?token=rirIv0cZitkkgFjkIOlrQDPVpnMZu-ku52foQofYNdeRmV0yIRiQYMrhoNZoNXFvjMOQxlH-GrTgueR42YmcUeP8LEUyirZCRofy0E07ElFLCQ5YMwwK4bON2fCoYu-afcYmIEx8s3OplRM_xoXp2F2Sz47cn-i4D7G4cPLB1SySou2HUdzZ2edpEptWjU6P_3NBn2QblvnTZJpVwnM38lnUt015OGpDwvrvA6btmDY1B5Jupzglxv_H1mnh7Fisuk79-8ZapPttKSsUBezIOtLqQdLE6n0_QoX2coGVc-t4CWD5-ImuaqoL0MLOJcD7Nvz36AKpTeImIe-_fN80NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسوت اوزیل طی سه سال شفا گرفت
🔥
🤯
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103926" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8863db9835.mp4?token=T3eadWMv1yhpXpISnLFiMHlEjtbICSx4TE-48oQ9KvndbR3Fca-AIN2Got5WjDVL0TNYFUZzRVYrP5rr7eZr1m1Y7mBSLdQJMPhP0FmMQTq3SGPPks6v2AK52eL1oEIjskNHE4olzHo_WxsCqav0MxO2cLiyhB_laRQhsx9OHTazyme8rB7Cmu2yJFzHhrxVzWDtb6S6TD9PAiQ089wyAn2h76DfULOUcxXd-cYuxW056X5J_tDeteRwWs26trvjkoaKV_7vAQxXihG5Rf_r-CiIakCbikt3ky9eZJpPnXuUTLi4NmPDmYglTJuFvkTdStRwe8_IzxJEt8E0uwvEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8863db9835.mp4?token=T3eadWMv1yhpXpISnLFiMHlEjtbICSx4TE-48oQ9KvndbR3Fca-AIN2Got5WjDVL0TNYFUZzRVYrP5rr7eZr1m1Y7mBSLdQJMPhP0FmMQTq3SGPPks6v2AK52eL1oEIjskNHE4olzHo_WxsCqav0MxO2cLiyhB_laRQhsx9OHTazyme8rB7Cmu2yJFzHhrxVzWDtb6S6TD9PAiQ089wyAn2h76DfULOUcxXd-cYuxW056X5J_tDeteRwWs26trvjkoaKV_7vAQxXihG5Rf_r-CiIakCbikt3ky9eZJpPnXuUTLi4NmPDmYglTJuFvkTdStRwe8_IzxJEt8E0uwvEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیو وایرال شده از تفاوت رفتار جلالی پیش و پس از پیوستن به تیم‌فوتبال پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/103925" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4Cni4YK_bWEmxAmBevVB65bq6zJfgylC3G5KRo74L5JFxKfLyw9BU592gjp8Q2NQy8fOrXcsRBHEg76XzGWp9aQ4P_YZMj3Q85klkIIaAiySxODTLhbR0WHOFrN6_LjAv84oH0rK6bcvkr3YLrZ0h2T8jK88im3U9DBZvWUscBX9ZrVvPS0ZiLxAH6p3uVB2b77kX0ADXBCDLl6CqYrQN5hke-BQyvQoD-hBZBYoSxwekQ9hSxN7_j5ycjoAlBBsIAQNE0ZU-dWh98MHjtcx4zd7NuXsx_7-jtcE9XA7i8uXzH6w7hPdbaHVcrBDaW4j909OExwdP9rJa0SOw-QzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🗞
🇪🇸
پوستر دیدنی رسانه 433 برای رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/103924" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IT4HJ_sSmhSUnmVCOxqf8w7jS5c0XgNdlU58DsBGcPY2fHico-h0zT1xob4H-A92UeQRS4sCAcJ4IjimLQiyaICYbZPWBjqUxTrF8Mv6HzIxWCqPJTro06jCumPAy1ssgZQ33qGCBXfg4nSsUFwU-cPH_JJMo0JvlMAk9QekJ9iJKacX2Du3YcecwtI3ikp1-e9D3bC500DePys9P5scJSM8BXhlcz9Dzsgi4F4rcDy3tgnMGglLDtmkSpxjP1oPUiYq3U4GCaV1nVrvIWSIpvfQOWN2qXG1Y044SN-geuMhxfQI6OjgsSt7FKQuzCNPcNuTREHCRELwvhb55ThDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇪🇸
#فوووووری
از جرارد رومرو: رودری فردا دوشنبه وارد بارسلونا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/103923" target="_blank">📅 22:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOTdQyNAQp1q73TPBsLjk1CsQUtG0aeKFM4hE1JRfAYSItQuJVZl4WXsejPSa4IVSOi2KkfpfpYHNVTnwDW-o0j6y2_fAG1tHexxjCjEjtQnLzQgLiPngj6uoxFqzcpgKchpCujBMVxw8kD9oVx3Ww2cBHzusbOk0tptYK2ilSlpdeJla7RpqkRLyPtfoNPESIRdlwp2SvUgAYar_yr4f5fdFA3vpR_byLYT3c8vVJ90YY-7z9OIAVuEXLh7IujKvVCY2QwWaJe0IdLQVNW7CPBbBDI_63WkDrEqMHaPZrq4fwlBKMl23WTgGEVpQxQO7LIoircDZeEiS4MZKlc1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2/3 DONE
✅
👀
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/103922" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAYthsula4zGB5JOCM6y-U-8R5tPRIWro7-tFJjHmfaqS0eOss0EzT61J4iB7Bd0TUycXj7ffkT5_GT8gMq1uh60drGY0nBzIQhTKV0HyJPuLUDhs2ynVSa6Ktel1MsM7qUM1gSwdwuVdHQKWEH8fXfD7Gscc_XzU6FdII6cTqYxD5mwNTsnGatH8joPu9FLIDAgSYGBG20393Wa485BoVqrJMvXUkTS8oQHURnDDjJ1sHRFocScDwNSoALarqK1rKWUs_8vyzGUG2yCCUzvX-YYosKalaw1zrR_qGKDi1pVCJoexzelpGElnUEzWdm8tkIC-d-Fq46B4Yi2TyCpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو درباره بادمجون زیر چشمش: نگران نباشید از شوامنی مشت نخوردم. فقط یه شوت به صورتم خورد که اینجوری شد
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/103921" target="_blank">📅 22:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXKaD-tvuGgOUG_h3mLq1SiMewBix0eZb-wEtjXA_CTdQRF4V_qrBTlYN4Mu1gaby1IkoPCCZ7jb2Iz5g6zx9_o0T7BxraMj0go4xnE0TnR5ilD0-dz-mf80wcpRG-F101OZg8OVtICV_6F1Q1dG2dSqU1guM8JT9539qTnMsZNqu9xjBymAj51k2GnnWpqH9IXnen-f4n5gghxRF0PUgBeQF2PItES6ZqFTcL5rHoETXOvK5vgwo__T9QDeaqABj1TzJdl-cvNyD0tZ4QLEzR5Ugz_cMrATMdALDstxogV2N0EaIPzLe1Ux8JDdyTXLZY6CFOlWwjw116BCJQqWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از COPE:
✔️
🔴
💸
منچسترسیتی برای فروش رودری ۶۵ میلیون یورو ثابت + ۱۰ میلیون آپشن دریافت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/103920" target="_blank">📅 22:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoNiFnSK7jfLrpA4RGKfxM1_T2DBLmN4tDo0FtIu0NuVYxw38Vc2d88afvm2thw2Dlg7p6YpWurk-128TY3MM6ZuLimY10BFr_gMS7ZYxedavifw4b-UtUQQTlpmTPJA00teEyK2KgOY2RL5CZViaFmFn8T-YMsZzI4k_iO6sZzga_dJR0GTkXmfBYvIHvLQCjUWjRwOrYAOVMnDRlMCgV3a4jEETr63q-ZlCK7rLLoBDjMql_GyvolbJmvxQYVoJ2z3aPrD3NhgIRZ1c2gHE8PhPCH2kqCQITc8-jIYceaewrlCwYvWZ8wvnNuAssGcqU53rjHTFaabRYm6x9BbNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
بهترین خط هافبک جهان در بارسلونا
😐
🔥
🔥
✅
🇪🇸
۶ بازیکن اسپانیایی و یک‌بازیکن هلندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103919" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ0FVGnFvN3nKszqAfPJcU7-h4yoXCQ4xY78pO1D20kLJ8MqqPSi5gUuiHDkkESLAMZUwpAFriYNpSBmIxZQYRh6WWvGMDhNLLTUtOMAako5FJ9bHzogCiONZ4gK9GonS_QgDmfkitPjyuZCZRK0YRAs_p46kT9ngpPvM790YNTY5HAJ4rqdfHhzlUbT6cr8H9dfElIz3V4Llj8prO-bOBX36WTVfEGK8zEeBmyexFHStaa4ruBe_BD320QTd7J47WuKA2TwX-hQjrE_ABh43ieJXVSOMJH45czAKactRVgg5S83Ux3XMYcWWl0Jr6m4_e1tNKU7K6m-fnDn5LnMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🗞
🇪🇸
#فوووووری
از رومانو: رودری ستاره سیتیزن‌ها به بارسلونا
HERE WE GO
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103918" target="_blank">📅 22:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6s2fvua2QZmf_Ugs11xuE-I2g16fZhd8P_rXzpXAp29rKJzfQjkjWn1997_0nZFs0F2QkADmEQkVHlzO4hfBnL3wP_u5WGDwbk1rL0vDVHoLygHQygdIt3sZEXrj6V8-fKQBOuae8JQcCXzpRFlr1EgMcDpHbLl6qpDqCRLiWvjM5j0u-3WUh6AeDYw0PH32MCZRGZqVg2Be-gPu3iJHrL4SQIa5wNTwwBHeN6bE8JzMxppWau2BPvfKIp5FKYvgVT0AqdiMcyhplfgVonTrN-Ggt5_I3WLLYTJDRbxkJ5jzxggDqTYv2XM70UpVUZG-4tiAhgqtwIjf7LIymyW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرکاپ فرانسه؛ ترکیب پاریس مقابل لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103917" target="_blank">📅 21:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6285ff8281.mp4?token=Vy9ZdyRtTuDI2jM3r0KTrYMv5SPpcqJ4kkKgHv1U8PjO8PoiA09rWyS8hC7Ihv3CXD4G9lbUEn041v3BMsAfB0pONDlrg6XchS0zfK_0x1jrjIA66QpQXRXICkcJdi-aaYEa-0tiLh1y-f25g41qNsVkHBBE7lY98OM_mkd8HM5C0pBJgVZgLvE5kBWWTqEeFYOr8VQoMi_57kvsilUVTBs1Ou8Y9j1QjivhmP0drNPuXOJ5GsZm8F5pO8xKig3xrlzd_2Xg65sGyapjUkVwM8aY7lfHelq-_UV3YXgl8JHhPue3DSFj2zlTlPwX0a3xtdLslkkxF8t4mhAOsbG7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6285ff8281.mp4?token=Vy9ZdyRtTuDI2jM3r0KTrYMv5SPpcqJ4kkKgHv1U8PjO8PoiA09rWyS8hC7Ihv3CXD4G9lbUEn041v3BMsAfB0pONDlrg6XchS0zfK_0x1jrjIA66QpQXRXICkcJdi-aaYEa-0tiLh1y-f25g41qNsVkHBBE7lY98OM_mkd8HM5C0pBJgVZgLvE5kBWWTqEeFYOr8VQoMi_57kvsilUVTBs1Ou8Y9j1QjivhmP0drNPuXOJ5GsZm8F5pO8xKig3xrlzd_2Xg65sGyapjUkVwM8aY7lfHelq-_UV3YXgl8JHhPue3DSFj2zlTlPwX0a3xtdLslkkxF8t4mhAOsbG7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
اگه موقع اجرای انواع پرس سینه، بیشتر سرشانه و پشت بازوت درگیره و سینتو حس نمیکنی و به ناتوانی نمیرسه، زاویه دستت با تنت اشتباهه.
✅
هرچقدر به 90 درجه نزدیک ترباشه ، سرشانت درگیر تره. هرچقدر به صفر درجه نزدیک تر باشه ، پشت بازوت درگیر تره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103916" target="_blank">📅 21:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG4ZAOIyqrlgia_L7jlbgmskDvZjiaIwNpY2zmzGVvFxFPCrhWKFSLEWesEb5NJZpWkPkjWMmkxAV2AtQxk9rxLncsiavXx4M3RTqMSklWJZ4AH3G2F4aLYykNFQzT-vaj4zhS3PIfhtwaGUPW9lfFNCwE-H_TcQFf3hwbksn1XfxyqPWCmJNYIFsXyG69-_jguORi_c9axkLCmF5UJCd7-orS0G9OhQYUg0ikr_NKO3TIIaQtkDXZxjJYfM1fy2jTLwlhKUwzV-6x_vFS4NePuTKsQZuQCDbK_MtUwf9sw1Vbg-ykYpXHeptg--bnGXEdGSJq2jGA8WdzQsbRBlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇫🇷
اگر اتفاق خاصی رخ نده، پاریس فصل نقل و انتقالات رو با یک تراز مثبت 129 میلیون یورویی به پایان خواهد رساند.
🤯
🤯
🤯
🤯
🤯
🤯
بازیکنان جدید:
✅
فران تورس — 50 میلیون یورو
✅
ماگنِس آکلیوش — 50 میلیون یورو
✅
لوکاس دینیه — 7 میلیون یورو
بازیکنان خروجی:
❌
گونزالو راموس — 75 میلیون یورو
❌
کولو موآنی — 41 میلیون یورو
❌
کانگ لی — 40 میلیون یورو
⏳
بردلی بارکولا — بیش از 100 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103915" target="_blank">📅 21:10 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
