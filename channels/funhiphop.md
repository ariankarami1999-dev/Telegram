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
<img src="https://cdn4.telesco.pe/file/oUgmBj3vJh4rP-RssZh4ouOyeV4EjuIKhHmK5-MCDX-lD46_FrrJ50-aUiT_w6yS4b7e1g-Yy13VtNTNZ6fFf3WqxQ06yKR4CJlATgD3fTXQ-cNikAkES35Sqohhk_Inh5irqSvhg1N65tYgS9e6Ht1CJ6GcmCBJ2j_re4lHPN6XyX67YVNTMgWIBbYN3giZCNht0mrLBPMKs-Te33l892eDE7Zk_jmfb02Id5Y65uMrrRPKkRJ0KwnGz4YVxVnwgY9GhkQPyuejMIoIAkQnv5VJTlDl6jy4QjmIvEV6wWT92ubArA-lfLP2KE90WdRS-r1GYRDEcVdH6BWTC7w-Ag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 253K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 09:47:03</div>
<hr>

<div class="tg-post" id="msg-84028">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0DwIbn69Uec1M_oHxdH3o4sultwbw_syhKVzg39FuTTIeOo_NxtmcR8yggz0BY9cIwYSJsbGa1Jqvnhoi7lesjlCHDwKyhe6P5gs4iXqkul7eCN-2w4We8K3ylXL9QlnULleAApb6Wec6CCebLGuJCJgZTcOunofA65viQ6DY-PC7T0OEAEtcht0fRDv-nX40EhQagHmenzJOAMrELrNhXxr3otfse0Fq3i1dnk6NC_OO2R6_DC_6GtLPU7aScttZID9chrXwa1T23Y1u7Ia1j8Ov9JPoxwNNOLSxRzNk8RkUNiZ16f0aPNUdMJZwzGuK0ekojTnhmm7_Pwqo0y0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌همه‌چیز من این فیلم رو واقعا دوست داشتم.
الان با چه رویی برم دوباره ببینمش و به بقیه بگم سلیقه‌م با بیگ‌شگی یکیه؟
(اگه مشکلی ندارید فیلمی که می‌بینید رو شاه مشهد دوستش داشته‌ باشه و هنوز این شاهکار فرا بشری رو ندیدید، همین امروز ببینیدش؛
اسمش: Léon: The Professional)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/84028" target="_blank">📅 05:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=d61hVKhevTHEbj0rc5ALR-PUMbm5RF88BylcESCTjwRJMxb85cQfP2GNPK0aNRtQr0nQPqMj4-e9D7qVv7ST1nIstiUs8FIr0U2ebA5OmxVSe6bOMCxW6StQap0IQw5W9CMkKnXUwlgNj3SoKzSG1Dt1HSf0aITy4G1EBAQEQE4LeoQ03LCY_CU7Qd1944DJs-w_PWt-QTEdeLQI0SFFKhTH_NzTVHC5-ktTIzy2V4djTqCcu0pisXqxflIvtfoMOTGxJL8jiWDphrOilnPI6E7GuFGYMHD5pakDFZzybDR6jV8OxzbdJLufKv7oIAyfSCk_13PFy3eZfvAOt1Mjwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=d61hVKhevTHEbj0rc5ALR-PUMbm5RF88BylcESCTjwRJMxb85cQfP2GNPK0aNRtQr0nQPqMj4-e9D7qVv7ST1nIstiUs8FIr0U2ebA5OmxVSe6bOMCxW6StQap0IQw5W9CMkKnXUwlgNj3SoKzSG1Dt1HSf0aITy4G1EBAQEQE4LeoQ03LCY_CU7Qd1944DJs-w_PWt-QTEdeLQI0SFFKhTH_NzTVHC5-ktTIzy2V4djTqCcu0pisXqxflIvtfoMOTGxJL8jiWDphrOilnPI6E7GuFGYMHD5pakDFZzybDR6jV8OxzbdJLufKv7oIAyfSCk_13PFy3eZfvAOt1Mjwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/funhiphop/84027" target="_blank">📅 04:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr67x7lHRG1ie1ZKY32I6CI2r-HhzOEncY1GXkP4-l2OqRTzjgt8sE4xc2i4EFqvFNJYW3Ch7HmKHCmray3VFQC-cYLDGFxhrt7xoATVHW2JCRtcHYOgHe85ZrX_nYQkoL-L_VjhxTEJP2kX96-AqYK29zztDeACqIiumqn65HzjrcNeggglECtRLPO2zLzHB2IczpT6JigAk7rSxYsv5JoJco8FlxsUO9nPWzJuxNPU1IxHEASl-7DCADA0oiinb1D8Nwc1GTUqAm6mniNk9wIWvkAkYZ6rdgmYloPa1-RW2KX9a2U3BBkHa95zTYTzbDWvXc9vZyqMczSTKMB0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/84026" target="_blank">📅 03:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پزشکیان: ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود. آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند. من عمیقاً…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/84025" target="_blank">📅 02:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d939cba.mp4?token=paQTDzGPQi3NgddDzYL36R--1frLlnRx31ciIYF9Fvxz_XjFJdiDsuXNLjU5AhYi8XA5iEdfnRlWb1BSjXju4Uh32GLdpYRPHnj7z0PPAuw1B5KbPAGX2xOwrUIOWqDJPTUHcQwOe2yaWIM6iB1D_sNnUGlOMFy0D3q3XBk4e0VkrCmtKh94yJeaEBNSjizgPAHQ6kJ0Rqq3mR9WzBgBOlYKB72mwMmnhtfwU0lkckfVsSJ7U0r1c-2gFqBbletlR-U4WiZ90kKv8hBaoulQTOrBHke-uDwO5mmgq4bpmujfjfSJ3E5VSPleWW4t2Q3WWZvILUy82skTaGTR2YgM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d939cba.mp4?token=paQTDzGPQi3NgddDzYL36R--1frLlnRx31ciIYF9Fvxz_XjFJdiDsuXNLjU5AhYi8XA5iEdfnRlWb1BSjXju4Uh32GLdpYRPHnj7z0PPAuw1B5KbPAGX2xOwrUIOWqDJPTUHcQwOe2yaWIM6iB1D_sNnUGlOMFy0D3q3XBk4e0VkrCmtKh94yJeaEBNSjizgPAHQ6kJ0Rqq3mR9WzBgBOlYKB72mwMmnhtfwU0lkckfVsSJ7U0r1c-2gFqBbletlR-U4WiZ90kKv8hBaoulQTOrBHke-uDwO5mmgq4bpmujfjfSJ3E5VSPleWW4t2Q3WWZvILUy82skTaGTR2YgM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود.
آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند.
من عمیقاً باور دارم که انسان‌ها نباید باعث مرگ یکدیگر شوند.
ما باید موجودات برگزیده آفرینش باشیم.
وقتی می‌توانیم مسائل را از طریق گفتگو حل کنیم، نباید به خشونت و کشتار متوسل شویم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/84024" target="_blank">📅 02:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=QcvBxsCWqL7oxbU3dW_drpohvTLzVZJY6v7PiMETw6nr_ZKDlBOhLXQj6Fl-laAvZvuV8EPa7DmlbwUzxy1LHxoaab1CubJ2WUDJ7d9N7_aRoi7smARW-DHwxgbitRoLdt6pslw90OG_4MCHHWZ2dvhWQS99_0UP2n2sLhMoUBoB9sdPViU9QIVIMWj9yznGRzS-m9GIfRKRABOQuWppZRicEJ_IulZd-KjU0y0yj4fe-Y9mY2HdBsCXAAJARbYU_XpIW1V5sTIlSV7W0fpaAyM-ZGrKxDvASljPOeTX520KSKP7WUG0zcOShGoVQe4AL79rC2tFPJm4ToMFh_rDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=QcvBxsCWqL7oxbU3dW_drpohvTLzVZJY6v7PiMETw6nr_ZKDlBOhLXQj6Fl-laAvZvuV8EPa7DmlbwUzxy1LHxoaab1CubJ2WUDJ7d9N7_aRoi7smARW-DHwxgbitRoLdt6pslw90OG_4MCHHWZ2dvhWQS99_0UP2n2sLhMoUBoB9sdPViU9QIVIMWj9yznGRzS-m9GIfRKRABOQuWppZRicEJ_IulZd-KjU0y0yj4fe-Y9mY2HdBsCXAAJARbYU_XpIW1V5sTIlSV7W0fpaAyM-ZGrKxDvASljPOeTX520KSKP7WUG0zcOShGoVQe4AL79rC2tFPJm4ToMFh_rDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما هرگز به مردم خودمان حمله نخواهیم کرد.
مجری فاکس:
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدرسه میناب حمله کرد؟
مجری:
در تاریخ‌های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
پزشکیان:
خیر به هیچ وجه اینگونه نبود، آنها همه تروریست‌های مسلح شده توسط آمریکا موساد یا کردها بودند که به قصد سرنگونی و ایجاد آشوب می‌خواستند کاری کنند و فکر می‌کردند ۳ روزه کار این نظام و کشور تمام می‌شود اما ما مقاومت کردیم و نگذاشتیم اینگونه شود.
آنها مردم عادی نبودند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/84023" target="_blank">📅 02:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مجری فاکس ‌نیوز: آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟ پزشکیان: هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.  اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم. اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست…</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/84022" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5add83729.mp4?token=TCnjTTNmC6Gb9R1aybA_6kj4Wbl455PoEJm-R7M41fbIpL0PVKtzGszxGBLAJGd3pDXDT9zmQD0EAIhBausGSkjOLu2PIQXNo5FvA4Hab5dgzWfG1JhNUb7OYBGpqWmtANHDvTn2qv9vw1Bdr0Oi_7ZmjTvrnlEkT5O4V3FjuBKqyPnIZVjbmT97ISSwPcFUB3n-gHhFznn3j40jSO3H1TpVfeVp5Q4YmuGmxrBAOVUZllSwy2jCJUbpvRkrG1PjdBYIZSGuw7qkac0d393I_Uku0mMQdrYm5Nf91pYge3SUuXSfh-1-C7XN1xVVQfR9Sn6SyfTxvwG5ofNaI0mY-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5add83729.mp4?token=TCnjTTNmC6Gb9R1aybA_6kj4Wbl455PoEJm-R7M41fbIpL0PVKtzGszxGBLAJGd3pDXDT9zmQD0EAIhBausGSkjOLu2PIQXNo5FvA4Hab5dgzWfG1JhNUb7OYBGpqWmtANHDvTn2qv9vw1Bdr0Oi_7ZmjTvrnlEkT5O4V3FjuBKqyPnIZVjbmT97ISSwPcFUB3n-gHhFznn3j40jSO3H1TpVfeVp5Q4YmuGmxrBAOVUZllSwy2jCJUbpvRkrG1PjdBYIZSGuw7qkac0d393I_Uku0mMQdrYm5Nf91pYge3SUuXSfh-1-C7XN1xVVQfR9Sn6SyfTxvwG5ofNaI0mY-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس ‌نیوز:
آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟
پزشکیان:
هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.
اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم.
اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست و قانون کاری انجام دهد، این امری متفاوت است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/84021" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پرزیدنت پزشکیان یه مصاحبه تصویری هم با فاکس نیوز کرده که الان پخش شده و با دیدنش می‌تونم به جرعت بگم که حجم و سطح طنز پرزیدنت ما، قابل قیاس با هیچ پرزیدنتی تو تاریخ بشریت نیست.
واقعا الکی نیست که چهارم شدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/84020" target="_blank">📅 01:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جمهوری کلمبیا اعلام کرد که روابط دیپلماتیک خود را با جمهوری اسلامی قطع می‌کند. این تصمیم به دلیل ادعاهایی مبنی بر ارتباط رژیم ایران با گروه‌های تروریستی و قاچاقچیان مواد مخدر در سطح بین‌المللی، نقض حقوق بشر، مسدود کردن تنگه هرمز و همچنین جلوگیری از بازرسی‌های آژانس بین‌المللی انرژی اتمی از برنامه هسته‌ای این کشور اتخاذ شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/84019" target="_blank">📅 01:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIErs6xcp6clzlDD9WJS_N8K5onNNyqoeClWwvdcKh05JvuEY-Wc_4_NvI-bloCJnbtpWURv0eOS-jAZJK0sVilQjZDKb4_tCO4gOzOxKj1nyHjYZHFX_0g3X_5kYZrHyd5JGgKUoF59eUzZQGzb9zSc7y71wT40ovtwBTv12f99_dssSw3fcD4TVRyUt29IImLtHe9aVF78VkqKYuO2yAwHKsRIs0cyvC5kTv12srvCFTjlZggGZnBUO_y28-Y0cRMW71gx7fVAiEIL0fdbSMSwyzWpqo2hKB-_W-fja_3ubDPKrdsGuN4tM4gKR8_nJHV9vvuSamczNTlujm0fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت مسعود پزشکیان در مصاحبه با NBC News:
ما به هیچ وجه قصد ترور ترامپ و یا هیچ یک از
اعضای خانواده‌ش
رو نداشتیم و این پروپاگاندای یهودی‌هاست.
برخلاف
ادعای روبیو
، ما اصلا دوست نداریم جنگ رو تا انتخابات میان‌دوره‌ای آمریکا کش بدیم چون هر چی زودتر تموم شده بهتره.
ما هنوزم به توافق اسلام‌آباد معتقدیم و امیدواریم آمریکا هر چه زودتر و قبل از انتخابات، جنگ رو پایان بده و به این توافق برگرده تا ما هم بتونیم بهش برگردیم.
ما آماده‌ایم دسترسی کامل نظارت بر سایت‌های هسته‌ای‌مون رو فورا بعد از اتمام جنگ به نهادهای نظارتی بدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84018" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=VrRgfPdkWYzX7xsgOuZ3xhYxl4SNtaSlhyZZ9vzbnhCT49nSHzVXLL_gaDhh_hzraiV3clAH5wqlD8eM8rnN7VUwDrm7budXm3FLTVLTdI0TVFaQxnwTvIyoOypWDIrkvynUIxsQ-PhubvGcGGAsRB97BT9pX_UbXzQqJ1OBflJdtTf4i1Hp2LyfK-SUTtmP9W_TO-1GlgSQwTYszSsfy8AS-ORZqwmjjROA5yuTfeKrA2WsqasZ9r-lT0Oa6GA-tYGceb0D-4RJbTZRkAb1x4QDT7aHfSuyT440LRyKKxipiHzc9NEVXrXyxWskyPffaC-A8F_V03EsT000d6skuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=VrRgfPdkWYzX7xsgOuZ3xhYxl4SNtaSlhyZZ9vzbnhCT49nSHzVXLL_gaDhh_hzraiV3clAH5wqlD8eM8rnN7VUwDrm7budXm3FLTVLTdI0TVFaQxnwTvIyoOypWDIrkvynUIxsQ-PhubvGcGGAsRB97BT9pX_UbXzQqJ1OBflJdtTf4i1Hp2LyfK-SUTtmP9W_TO-1GlgSQwTYszSsfy8AS-ORZqwmjjROA5yuTfeKrA2WsqasZ9r-lT0Oa6GA-tYGceb0D-4RJbTZRkAb1x4QDT7aHfSuyT440LRyKKxipiHzc9NEVXrXyxWskyPffaC-A8F_V03EsT000d6skuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده‌ی اسرائیل تو سازمان ملل اون استارلینک نتانیاهو رو برد پیش نماینده‌ی ایران تو سازمان ملل و خواست بهش کادو بده که بیاره ایران اما نماینده‌ی ایران قبولش نکرد.
💔
نماینده‌ی اسرائیل در سازمان ملل: 1
پوریا عرب: 28929853059-
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84017" target="_blank">📅 01:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو یدونه دیش استارلینک اورده بود با خودش، به دبیر سالن داد و گفت بدیدش به نماینده های ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84016" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=Y2O7hbANx0qYLl5awHUXtnHUTK_l66riqvcMLfpo0zGDu1Hij1MoIc-zAOWJJHZvRebxTpBgSHyI-ufcQGj6ugnK6Ww5b_xi7ssvpQBmhqxa3nzopHxI8xRQlGpYxWYyy3_ampkLzFrRE7y9ZF9yJ0gG61yqbqDz-lqnl-kbJD6CyUZNQNsdge7rN4AF3zC6MnM4SqbF7yzZdIi2SYY-Izkk-GIvAlhDquQA6w7YI6kFD1fgR-85fJGOjb7SL-YWL_wMNhiS7RS50NzwY2RXhK4J0bbTmcJ6g8BLRp-_QIGXXtxD8KAhIGifMWnlwMtAYDLvivVI2AFJpa5IFHbMS4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=Y2O7hbANx0qYLl5awHUXtnHUTK_l66riqvcMLfpo0zGDu1Hij1MoIc-zAOWJJHZvRebxTpBgSHyI-ufcQGj6ugnK6Ww5b_xi7ssvpQBmhqxa3nzopHxI8xRQlGpYxWYyy3_ampkLzFrRE7y9ZF9yJ0gG61yqbqDz-lqnl-kbJD6CyUZNQNsdge7rN4AF3zC6MnM4SqbF7yzZdIi2SYY-Izkk-GIvAlhDquQA6w7YI6kFD1fgR-85fJGOjb7SL-YWL_wMNhiS7RS50NzwY2RXhK4J0bbTmcJ6g8BLRp-_QIGXXtxD8KAhIGifMWnlwMtAYDLvivVI2AFJpa5IFHbMS4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره پروپاگانداهای علیه اسرائیل:
🔺️
می‌خواهم چند سوال از شما بپرسم؛ کدام رژیم نسل‌کشی، یک میلیون دوز واکسن فلج اطفال را به جمعیت دشمن (غزه) تزریق می‌کند؟
🔺️
کدام رژیم نسل‌کشی، توزیع 2 میلیون تن مواد غذایی را به غزه امکان‌پذیر می‌سازد؟ این یعنی یک تن غذا برای هر نفرز متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84015" target="_blank">📅 22:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=EKx2UUoVodF7SA9mWMXssF0__yxRfy20rX8IwYIk9yasrRb764yPH4DD-4l2D1MM4o-rtz03Wld2Xv6JBHcYC_EwXbZyw4tfzB15WOzb3bjn48bKcOYPVfo8zG3FSLGbWHqW9p4q9nOHBMcVkMH-qim89G-ZByyEGVsiF8e8SaRjvZaKBU84xSjn4CVgnO0xkJC-3PKwnMDdWUQ8B8dKJEqBwXO6AWYzX-Zevk4mDmk3bLLePScRqQrLaziWlXOZ918_ACqQoBkW6uCEcny0nizKdBAtfPlXhGifj32bD7h6Ougtt-WUSn7xIu_smV-asEfLdTQ1ax0DwsRQjtqcdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=EKx2UUoVodF7SA9mWMXssF0__yxRfy20rX8IwYIk9yasrRb764yPH4DD-4l2D1MM4o-rtz03Wld2Xv6JBHcYC_EwXbZyw4tfzB15WOzb3bjn48bKcOYPVfo8zG3FSLGbWHqW9p4q9nOHBMcVkMH-qim89G-ZByyEGVsiF8e8SaRjvZaKBU84xSjn4CVgnO0xkJC-3PKwnMDdWUQ8B8dKJEqBwXO6AWYzX-Zevk4mDmk3bLLePScRqQrLaziWlXOZ918_ACqQoBkW6uCEcny0nizKdBAtfPlXhGifj32bD7h6Ougtt-WUSn7xIu_smV-asEfLdTQ1ax0DwsRQjtqcdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره جنگ غزه:
🔺️
در حالی که حماس تمام تلاش خود را برای قرار دادن غیرنظامیان فلسطینی در معرض خطر انجام داد که اغلب با استفاده از زور و تهدید صورت میگرفت، اسرائیل تمام تلاش خود را برای دور نگه داشتن آن‌ها از خطر انجام داد.
🔺️
ما میلیون‌ها پیامک برای هشدار دادن به غیرنظامیان برای ترک مناطق درگیری ارسال کردیم؛ ما میلیون‌ها تماس تلفنی برقرار کردیم و میلیون‌ها برگه اطلاع‌رسانی درباره حملات پخش کردیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84014" target="_blank">📅 22:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتانیاهوی جنایتکار بد در ادامه‌ی سخنان زشتش:
می‌خواهم خبرهای خوبی را به شما بدهم.
اینجا فقط مسئله زمان است که چه زمان این اتفاق شگفت‌انگیز در ایران رخ خواهد داد.
قدرت مردم، قدرت حاکمان را سرنگون خواهد کرد!
می‌خواهم شما با دقت به حرف‌های من گوش دهید. یک روز، و ممکن است این روز خیلی دور نباشد، مردم ایران آزاد خواهند شد.
رژیم قتل‌عام آن‌ها، با دروغ‌هایش، با فسادش و با ظلمش سرنگون خواهد شد.
این رژیم شیطانی سقوط خواهد کرد، و همه ما در آن روز جشن خواهیم گرفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84013" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=jJ8rIjSHUogkHex0mXSUR2iaOlU6MWz-lZ9mb2DfZPecD6Xj6YMKfPgBHXbozDIFBKBOVjpHumh6hghLKajUXnf_TuRXtlUA8TxxzGE4xbznoIugcM4cofksu3nbEFSzQsv5MZOQ_HK_vWPq3hUOeVAaASv5yTqbo0iwgDJsU4O4_kvXTKcKOLAjRpWC-iLZrxjiM2ZzzWBvOJmgW_A6hs5eCil6s_iXu9lJQNsSO9HpYvCXYIdeul6nj9mxWqnfDsqCt9Cn_2EzeKN0v9AldnHu6l5AhLVmyQXjRCT4BJ0nbtA5PJ4R-BKuEcWoCdyFvc_KOeNCP8mCs5m1HaHxiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=jJ8rIjSHUogkHex0mXSUR2iaOlU6MWz-lZ9mb2DfZPecD6Xj6YMKfPgBHXbozDIFBKBOVjpHumh6hghLKajUXnf_TuRXtlUA8TxxzGE4xbznoIugcM4cofksu3nbEFSzQsv5MZOQ_HK_vWPq3hUOeVAaASv5yTqbo0iwgDJsU4O4_kvXTKcKOLAjRpWC-iLZrxjiM2ZzzWBvOJmgW_A6hs5eCil6s_iXu9lJQNsSO9HpYvCXYIdeul6nj9mxWqnfDsqCt9Cn_2EzeKN0v9AldnHu6l5AhLVmyQXjRCT4BJ0nbtA5PJ4R-BKuEcWoCdyFvc_KOeNCP8mCs5m1HaHxiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی نتانیاهوی جنایتکار بد در مجمع سازمان ملل:
از آنهایی که اکنون (به نشانه اعتراض به وضعیت حماس و غزه) سالن را ترک کرده‌اند یک سوال دارم:
شما کجا بودید وقتی که ظالمان ایرانی، دهها هزار شهروند غیر مسلح ایرانی را به قتل رساندند و سلاخی کردند؟
وقتی که آن‌ها هزاران نفر از خود مردمشان را به قتل رساندند و سلاخی کردند، شما کجا بودید و چه کردید؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84012" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlq89OGSSJgiyccqpyPMLnhy5q_k4bx9nXZaP-gVzXwms8BK5d3fcxNzPakAobApLhF1FKs9WVREqYXzBaBx_2fNQRzdNDv976h-mXWngUUGs-7swToDkdfpRs2BifAee-Hl2fxk-5-gIvD9NJQr_IWoGAVH59voM-ikKqrkGkd7T2FGoyCORz8lpTg8R7oQFSP09D_DfNSTZ67dldGlE6wuBxZ4WG7Ulbkf7GM42NTPq-4uSTbUMcSrm-NopeMpT82U00JkOyaxQo0fT8k1a0SjWWPGUVuG4mMZa7Kin_crU7SXA-BeZ3ugX0r9jnmllS8MHfwN5s-i91yjhhOfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84011" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84010" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84009" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSAcO6QF19lG8MpZxR6qfa_jvuqtvtWzURGOOYB0olcmSTm1SDSTzR5Q9TIJpp2JcjAYIptt2XTyskgWxxXeuR2pPRmguAjhJGjGFbPNpamqt9XC7iOX-9hF4l5enqkbHOqwUnZMGB9K_QXZpwaGlaz3YZWHugxVB2p_avor8_t8z16sCH52LRqGXPTFHsFaALM6py2QG5SyveV237fWZ5ZDDW07cXVcDAxis3DKIW9qqf7kqD1J0byXA3MKk5inm-uaR8ykqSDiZI9-I8otRbC0ctocEFSeFZTxyBR0c6NI8KjoQMn67a0NO2Kx3Hd3SLFexkGg6bLIULB_8-gVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
تیم ایرانی به رهبری دکتر عراقچی تو نیویورک دارن با آمریکایی‌ها روی یک توافق که جنگ رو کامل
(با بمباران اتمی)
پایان می‌ده مذاکره‌ی سنگین می‌کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84008" target="_blank">📅 20:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد. SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84007" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpI5wcuulK0nByXtuosT0b4T5PtBpmVfuuXbsbeSFdW8Jml-8hFb8U8NkQtFBgd5TmuRIt3y9EQcWiuJliVjb91zfE3_BHuN_jMjwzMmcmn_swaGdjVeGbsb7zs0arj7cMUn85SoPFexnHUdK5MvICGAV5uyaM89pMhGbw8fBcER13olD4sd3-iOIuACFSmWptXcsmHMbp4J9w3Po27BTbFjw8FaaoKtMrFVE_FBnY_ju8cP0QGtSxZG-fMIlVoATRxLxAzHSz4jwIXleqvLPNNzBmMIh_VCZBaQ7uFk0q4Lxn0lHMZAmR9fu--L1M7gqU6ceSmhtLNd4R6vmwR1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84006" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcIXseBqlxpAcVPkm72tkx8nqRzCI-otHetNO3IU69-VzveTUf0F2Wv7zr77gXlotI91iNLw21iTYFbmvQQMzw0WALmmsPXFvxAHTj4BiyiHSdDxoTvlhKXXeG3l27cstsV1E8wpVGbmrZuFK2uEq2fmf-qw4anCOlR1TAPVLtex7F90iRQgKLCGxLp7dDq2QJOI_7clkVg1kTVMUKPoLLC5-_GG1rQ93OD5RiqndbTk-z7InY-DXQ-H2pnKCHok2Pbedb-f8MCZfWMSqwH9WcOwh_asR7ZOP76hN9_3Wq2eEQbounVeplgzCanL39gPeofirF4LunpPx7U63GjyKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امیر محمد یک خواننده ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84005" target="_blank">📅 19:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtu1TtMhDFxaIPtqTMo1dZcSP1giQn9Z7EQQ5JN-8PoICaQrrc1HcIXnMqp_pIilSZlDoFxYS5ofkucD39AOxRe7cUeZewGLGoHqaDZ_4W7uvkrY0Md93WuAjbc_h9x_GxjvYav5WNJo6K4A3eZBPTE4W7pKVo3tVyC74EZdohDiGFqzaDWPqDa4et1Qeea_4AxW9m6whaD_scOcVB-L8khO05rBPXvc1xpJ-3mChTwJz8D5a0Vqs2saADktmkSvft4Qa85fcqHod6VVD5FyW1x-dJRXn5JgAiDf7MKtKLddOIuGb71VeID32FmyceDUbn_N-kEpihbf8_CDX9q7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران جذاب ژنرال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84004" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETR7YWqxkJ_MQAd6nBibk2qOYeXq_jKb9iGhQsJEnhtdN5_XKaN2zalRXOLsLWQvFn2mE7pK3fsCZ0qp0cg0u9EEx-hsxXnWBGV3TQfR3jFVfDGA46KA-S-aQrtHGjLbCTIw5EnO5MxxURddTW7hy6rLmc7U-GCzcIDxc7DJco41GrA237JxXWCNw8_byd48DPSQQ-Cxx-riJn5MOAR4LtF0cr38bK4RbXQnSlyHlRxYTs0zXB1EIA4bXlTbLgF4X16EV56qdWnbnpWpoQDXIPIrDT3mVuFT-97k8qOXS_Rfs_C0YPpwgAY0zhArvU9SZI7jyZ5AaMm9WPjGOd3bcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G2
🅰
🛒
ورود به سایت
👇
✅
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84003" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=fnI0hO72arWdQ_KIQqg3tPLLb9Y7rJRMEmffhukMNRtxCMvLxRFsWZSM58ja9EwXxIytlY2kpIJTj8ct0Fp1A9lHig7Eev_7BFBOn5-us8ca5tHB4zjg4yzZWPbuS93aGYM9nqzcGKWnvEYZgB4uyQwwWqZ0p3KVAXfyeBvlzmpPhzp0EefSHRA2CZjQXvCAYtZfVawYm5AzrVcaKFsi3GegarH2Qr-L--Ju03Atvp5yYvUwXzJjG8vMDMIMu2aJ8aqKWmMWW1CxSaaAcfOLApK2UyAtd1p5pWMwmn6WfbMio8QnW15ao3SSnQfSVDiqBz3Hll8QtaKMqhfqVLCHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=fnI0hO72arWdQ_KIQqg3tPLLb9Y7rJRMEmffhukMNRtxCMvLxRFsWZSM58ja9EwXxIytlY2kpIJTj8ct0Fp1A9lHig7Eev_7BFBOn5-us8ca5tHB4zjg4yzZWPbuS93aGYM9nqzcGKWnvEYZgB4uyQwwWqZ0p3KVAXfyeBvlzmpPhzp0EefSHRA2CZjQXvCAYtZfVawYm5AzrVcaKFsi3GegarH2Qr-L--Ju03Atvp5yYvUwXzJjG8vMDMIMu2aJ8aqKWmMWW1CxSaaAcfOLApK2UyAtd1p5pWMwmn6WfbMio8QnW15ao3SSnQfSVDiqBz3Hll8QtaKMqhfqVLCHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند مشت زد تو صورت بازیکن ازبکستان تا نشون بده مشکل اعصاب روان داره و نباید بره سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84002" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84001" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84000" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urkHPnmpNmEN6zWpMlBWF6EsC1bdJ8egd6N67lOHIFsqsYc2G-8thvXvcGiw5QKVAYgn1hZ4k7vy-MWlZq1Io-WgtfVRRacgTeLoAgOUb4TGWeCSZ8k-tH8CG9Qy8TcE4bu2-2b1JzUkbfgMg9SGogLCTavCqyIHuiXFkc9dJ5P9GWlqJjqQZihr858Zg8V3JpKWXoykoP_xaLuPdSdHfwfT4qgMAKmoV4wAg2F64nc6EkuQmBC5AoIHJQBOIbt04-ptRK2azDmfoHJXDWYzHeXaOQ7PDeLg5BslwbCxrPxUvp5WIzpqQwZH7y3PClkEigg4lFhu0jeAkQJfKZtQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسی به هیچ وجه
ترامپ:
دیروز در فرودگاه با رئیس‌جمهور شی دیدار کردم و به‌نظر میرسه قوی، سرحال و آماده‌ست؛ بهتر از همیشه. بانوی اول شی هم، مثل همیشه، زیباست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83999" target="_blank">📅 16:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شاید باورتون نشه ولی کوروش تو چنلش هنوز با پوتک درگیره</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83998" target="_blank">📅 16:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9H0iB9JShfI4WwbnYY7QEpc6pG1hU_W9_kodM5OI-kWKmFaiEHQXlUXhM5BzPwVJNSo0ambmcA2KJTKlgoVF-jMRdMFgxRJADr3UiN4LuKdj3iGpFKOy_erctMPiaq8CO8o3L5-zO56hsX26UDYr-cRo4mSo6emSkV0__CG34gO2MlqmMIMHcURJxYuWAr76FTVb01uX_chDqmQKcsgILppjCCy1WmavlwZyuDFSMyj-GJdvCDuEwOb5VlXyxVDoWKedLhbcIfa7UbcW4CaTRFKdscAnwSN1ORzq1_lpw0prQncnLgE0MYvStbyOwo6gc7D5iDPRDyztSTWMHGrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اینا تو وان حموم خونشون ناخدا بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83997" target="_blank">📅 15:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA83rTCSfETzKN3yA6puB9h21sHTIPlSo_FlP6AqK-VfG9KGxAUvaJP3yXzqUL7zLTd6uWNulzomMex8yU0YTUfWo7DPPOOrTZCPt3OikGcbd-LVGyygCVhx680yEc4PC3cDLUlrZA5tjgQb6KKPe_RP1QA1iVkcAHK__C56LMdkJyjCdJSOaGcXq-pIHpL4sh6_dPRgn9vWv8voKbzss_zAXmAYgK9qQj05ZuidFzwBdunvziI9RP896MLRVs8xoJ2AdH_FiDIp_ez2guE_E14igCdIhNHYXBTrawBbNmgj1DiQ1dBpTEom6-DtG_Sr_UEoHrNcyA5pwnNMSd--Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد به سلامتی به کدوم سمت انسانیت عازم هستید؟
حموم؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83996" target="_blank">📅 15:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پس پزشکیان کی قراره بیاد بگه گور بابای دنیا ما رفتیم بمب اتم بسازیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83995" target="_blank">📅 14:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=heVYicZBEbg9dWOLNvHGycyAeEAqIQ-xf6i-bXmRD0OQFXjTdG5O73sUGh9hdPNOdfX1dwrBlSEetzzne_H0R0QkuLwDCl9kGXfEmBwm5sIFci_pTYAg-QhjEtlg1Iys8IV9vEDtPrk16n3C5x1HkrJPi7LldW_kbrK9-BV0OxubTo6HHiYH0WccAmh9Se2B3ka5-WWLzS35XhU6cu4TLa5M0t5mhnFqeaBYYsX2whO95QtLB1Gf7P_dKkwDletHvk442EGFJubikxcpE7jkUrJVmrfxHSwgeXtHu7-_qP7itdIJRUFvvCxQUxkwudgupMJnmHVOrGpU00Lq6zWkVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=heVYicZBEbg9dWOLNvHGycyAeEAqIQ-xf6i-bXmRD0OQFXjTdG5O73sUGh9hdPNOdfX1dwrBlSEetzzne_H0R0QkuLwDCl9kGXfEmBwm5sIFci_pTYAg-QhjEtlg1Iys8IV9vEDtPrk16n3C5x1HkrJPi7LldW_kbrK9-BV0OxubTo6HHiYH0WccAmh9Se2B3ka5-WWLzS35XhU6cu4TLa5M0t5mhnFqeaBYYsX2whO95QtLB1Gf7P_dKkwDletHvk442EGFJubikxcpE7jkUrJVmrfxHSwgeXtHu7-_qP7itdIJRUFvvCxQUxkwudgupMJnmHVOrGpU00Lq6zWkVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور هائیتی یه ایرانی درون داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83994" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسکات بسنت: نمیدانم نمایندگان ایران در نیویورک چگونه قرار است به ایران بازگردند.
پ‌ن: منظورش اینه هواپیما های ایران تحریم شدن و اجازه خروج از ایران ندارن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83993" target="_blank">📅 13:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">باورم نمیشه برا یه سریال نگاه کردن مجبورم ۱۰ تا چنل صیغه یابی جوین بشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83992" target="_blank">📅 13:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=FsFldtDLvo1U7segK_Rg2XymQPHpJAmsRqXROBjzQqDQOyAt06svS75i88qcsf6v02Dx-SVsamRiOo1VtB_sHnFB4fKTm6aquz7EHZwks8G2ALrkK1TT-dcHeHqaP09E1NB-t-11XeaGyq6a-Eb-uQFp4QTJBBObPMhjpGN9UHEUec_TaebzaWQmtznu_CTbHveHc6d2ojH3QhBGdDvFanlREGEKKIZaifseLCQPUZT5pkk6fHyuMAm2KqEPIeYhwTPPvPVz0KjBc-BHV7mx-h6BaDRQmx4ZXCjkqo08AmmXWW0EWDRYaKuRLfhdcq4W2nLDbQLBtCtTAdjHnvNNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=FsFldtDLvo1U7segK_Rg2XymQPHpJAmsRqXROBjzQqDQOyAt06svS75i88qcsf6v02Dx-SVsamRiOo1VtB_sHnFB4fKTm6aquz7EHZwks8G2ALrkK1TT-dcHeHqaP09E1NB-t-11XeaGyq6a-Eb-uQFp4QTJBBObPMhjpGN9UHEUec_TaebzaWQmtznu_CTbHveHc6d2ojH3QhBGdDvFanlREGEKKIZaifseLCQPUZT5pkk6fHyuMAm2KqEPIeYhwTPPvPVz0KjBc-BHV7mx-h6BaDRQmx4ZXCjkqo08AmmXWW0EWDRYaKuRLfhdcq4W2nLDbQLBtCtTAdjHnvNNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83990" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نارنگی برا پولداراس ما فقط سرما میخوریم
🤙
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83989" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804d882599.mp4?token=qYB0ms0usfNtUzWVXN-Pk9nkGuNiWtOuTfQH1CPCka1n5FYbi85YGyWCwZWI4cYRKj2sWt1zYeWY2hkGzgIy7lTDo6VDSm1wzj5XgnOvX2GchoGdyTpsgXz20ZMhGKGvrmxNaI5iVE-or4iYgB6by0vp9js1aB9etwepGO7LxYTJyoujMf8Qp_Vbvq7HSroCvh5ytJJxfSy2-BVlCKeWn46d1wC8micj0gSxgGQdqDrgej4N-tcDQfQWXCEdW6908itScWL5u3WzqdlHLrLMLUKSZ1qvTRzi8QvIf32XONHGJyEYXzBk0h72Ac5615PRYiCUbHODvJg1_5fo_sUkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804d882599.mp4?token=qYB0ms0usfNtUzWVXN-Pk9nkGuNiWtOuTfQH1CPCka1n5FYbi85YGyWCwZWI4cYRKj2sWt1zYeWY2hkGzgIy7lTDo6VDSm1wzj5XgnOvX2GchoGdyTpsgXz20ZMhGKGvrmxNaI5iVE-or4iYgB6by0vp9js1aB9etwepGO7LxYTJyoujMf8Qp_Vbvq7HSroCvh5ytJJxfSy2-BVlCKeWn46d1wC8micj0gSxgGQdqDrgej4N-tcDQfQWXCEdW6908itScWL5u3WzqdlHLrLMLUKSZ1qvTRzi8QvIf32XONHGJyEYXzBk0h72Ac5615PRYiCUbHODvJg1_5fo_sUkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شی جی پینگ همیشه یه نگاییدم خاصی تو نگاهشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83988" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrLx1Q0mydHwYrRpCjQNavxEjXal9TbLu2U6czPqHmvyc0Az5Zt1jmLL7ysbs7zlFloI2zEqEOBAGyKhAWN7n8CVG5ytoO2Il9KsxFRt82B4DwZ4zinZHQpWXxwTuwe76ZOkmA4sUeWxP5lbOlxv-84Q9GgEx5et_gPjQWDeX98EWUyasNdvL_Yb54zBQ8FjwU0V-14nbP2pRDF0Xlr8jX3Yv4TKRDhBPQcA-klufmUM8mrQ1fE30SRhJYfF2JxojO8aHXYcQmpBuq9AQ2lCxfCzKjbOzgDKWqrjCyNxeWxADCQseeKN24xw3Cf_CNnH1YgKmHXze05JY1Ot4eBXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
نروژ - دانمارک
⏰
ساعت ۲۲:۰۰
🌎
📲
پرتغال - ولز
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R2
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83987" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2YVqTxm4VgUjzDcEWmm2ceOZePjyvoBveAL8yxleGFkozK7_HeRM5NMcNx4qFqyDja0vk7OZKWXs2v4ySMZIi33bf46XdWkNTDbi5ng1rnBgvAZXuwG1EvHPIlFq3XxGdQCmL5Qg8myIKQh9gS0WlBQIAxAdWC4RPesXjVRsSzQAwnBMR5Cvl8gVdJ_Kq4hls2RzoTja274uYm8hixGfFEXGTuvqilujCm3AW2NBnynKMigTNHk3q4L3EiJG6cXyMQBTL9mxHJ4zQu_2139zCmZ5dIQ6y36Pl2gQWWomvsCgHDyly4jIL9qACujtuCz9fPAxVHt2zJtUri79dU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش شبکه خبر از اول مهر و بازگشایی مدارس:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83986" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSGgDkarG7G3S4tBDOTSyG8ifytznygsrtU-UOBl0MYC7VROhp9S_6e39otrWdyLb4O_GApBz13yUa498ix-nODR8XvTT-C8I0ILGLmfNYv5kgGQ3ZfwL_N6TiHtVAPQ4UK9Z8yOKQN7opBXJq91iVTJq6WURWYG0yG394U35-VDUx2TLNz-yEsYqKEhfWjS9vvfUA3R64mTvJOqPnVA7d8hX0ANqyLHC_baB2YjaSs6HjOobKQSC21aJWOHOd7towtqWhSkm-Q_2KCCNOwoeAoN6ZgYe1UomXy9_jZIJ9aM2tzfu3yvaCx424hlGEM0eJxB2O2l0B6vE8OvE7jL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلورمو از این کصشرایی که با هوش مصنوعی چند قسمتی درست میکنن نجات بدید
مخصوصا از کچالو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83985" target="_blank">📅 09:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWscC0oLjmYqwddq4VhIIgzwQYuqo4bjQkFjpuEHicr6dMB53DktJtD47btPLVVvD-nNFFnhpI0-xxyEdQ1PQk_9QKMCDHE7l8wrRT-X30jWoqx0ke4AMh3bV0ditmJFGy0uRPQ6KUlIhOKk41DLZG1FLfI2MfxNRAneGB4S3TOXyDau7wUUvSPJ-S2RDzu9V5h8JcR1i0nsYgnPggqLORqn8q-F-l5QeoMbX8Ih63Cl7OX02qSuZZJugxZYxLLo1v0Lo9sTQfDweprDqd3FOKAb2t_CaBGFMqUYzPftkVX8shHu7_mk5XQIvXj-EVOEivAhah5AAnUas35TM_oYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83984" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hACKCFtKgrwH9Nv63wmsIr-kufFC_ocyFR09wm3r__W6r2oo2QW8xnVWdjjDKZ0nVbhAhUJ7_BBubKsyXdifUdNXsF74yiYkvBpy79Gfi4nzI2Tk31Pe73frCUWOmJZO7RFzDA1148TYfq9nGd9TowTo6kTQ3_iamTLaiDjgw_0ZP86kzbf3t_TVo0HK0_ZlI77S9Wr5H6kKrOlc1hcQvt0GhEJK8mv6NHaHxueq0N0t1crbbPwcgQdOHUrOhaocjrMqQZUk14os82zpqZuDsSliJ2L_SMwthK2atLGWTWngsYwfKLMjOT3VvywQY20IrVkytrVBnE8BvpM7LuhOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید پسر شایع
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83983" target="_blank">📅 23:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83982" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83981" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83980" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj26psyZwQjVYjgOmlUMlqXPP8ESiZTr-uT6gRY47xgwawUXi5mogC2JDp3SgF4oTnRgs0TgD8FdsvtEGCuSRRFHSSfgD4L0UEb2rRgdHJ0g5Fk8Tkjdb0vRHiw71X50UXsxAvf8_WRX2SazSTFqzmHwLD_EpQnYi7DezUfJOyz8BDYBrTxJdsH5NJDzR3fR9x0BGvZ6_C-4Deu1THUe710pBJu5Jv1hlqWUXFxf9RtGTohST6OuBrbPpZF0jWrMa14jN3sbj5St7wJuxwbROMsTUx6yWm9lmFF8uTBiBpPL9W9619BcUyKXwSPRk7yyFIAZ-nul6RLGUP7JRGMOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83979" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=nj1-9y5zIs6DKB7XND9XYPcOlJ_ZkVA6tzHZSfiXFqaT2FQ6BHNgdKUXmx84UJ93Hj2flOibrmeCL9Zt-W6Nmg8WKOWbOL8m-ClJgHm3nDJukrxfjBke40YvMt1bXvRMPEVyVJ2DyfMp4ATzL9FZyhokkwPkDDw-p1HLc1MBYfM396XFDScn32h4nRd-1KvrxzxCJ1xW1_Vc4FOU10YMa79CdyzVLuJc68nX5lg9iMmd5nP1fGDCRykSL-2LzMS1cg9kHiPXuFpTWXyg5VFutU22W2njgy0t4niPWaQjkqJvQ_bF_kWUc-VNJnS99IKAF1DGJ4gLtf4nBkoY1qb3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=nj1-9y5zIs6DKB7XND9XYPcOlJ_ZkVA6tzHZSfiXFqaT2FQ6BHNgdKUXmx84UJ93Hj2flOibrmeCL9Zt-W6Nmg8WKOWbOL8m-ClJgHm3nDJukrxfjBke40YvMt1bXvRMPEVyVJ2DyfMp4ATzL9FZyhokkwPkDDw-p1HLc1MBYfM396XFDScn32h4nRd-1KvrxzxCJ1xW1_Vc4FOU10YMa79CdyzVLuJc68nX5lg9iMmd5nP1fGDCRykSL-2LzMS1cg9kHiPXuFpTWXyg5VFutU22W2njgy0t4niPWaQjkqJvQ_bF_kWUc-VNJnS99IKAF1DGJ4gLtf4nBkoY1qb3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83978" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83975">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQxZc01ozsPQv_g5HaRayYhaIsx9Zdv2gRzP12GNjHgjbeen-CwiZjXGOZ1pDJ-LBU5nYtYUJaqhMRqCbMntfvZl_aMP_XUEK2s76NlPIW0uBnyjNWZHU87YIzaBA5z7TXeHTuOuotP9Nj04dhiaYSkN0GWiV5nO3eniGO2BgjZ47bO9OhnN0wRypqYq-5KegU-LnIMvinoTDQrM4uIl0LTRliaRiq1sHY5v2s8QjBMCj_Ve6VslvnuAIPw9V5RVOfYSfVb25F2k0C53UcqWXtuPif3tExbIQswZJm9EsoH4XC4bNsGFy9iKBDfLYizNHkVNnPwYKPMBBM1LQYSbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی دو روز شکل آدم بود باز طاقت نیاورد ریش‌هاش رو بگا داد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83975" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83974">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=Jy4VF6yGepfAlqaF1A_oW7gveEO_or9qsO1hP6-c87mJC6HPVsLXiUucFsbTwNsm6Vysh5KOYR0pTWoPFjWrpYySrokgRWOhzpBTfzdAtpyZLyV2p-GIGAYSR0enNWFjodUfVG4m2OLcRUvgC5uSPff0UpbzEYQAULY7cOPUIGiCD00T_h8Yyts4J0PPAyhKmq1zqPQIRu2nuOKY60sMy8HYyQG1CbbrptNbw0NpiblksNX0oFJIX_rNcM7JJyYDqfbAp6_Vd1zDbEUofwXrB7LSsWuKG4dbaXtOfx_6LTuTuaBP7JZxlU7cRPjipmj_Dpc7BkCuXgV2BndkF9zR-I6Q8sR03_ta-qemPemstYhdZIz6NL4-FcShJzq8bqDazrzpCiZLPeJ6ClHrwdH_GPfcHM8aUJ4osQuAKKAjweJ6nXcRl60NcyjXJy9tkrQpE8Qpyk3pVz1q3z3EIIrbc-UaoBQ2bh7F3WPbAneCQQfSPdR94CuDr1aktDeppabuf-SLPmPLH7U7Mn_-Yki1010RiJlYqB34wfiKiEG4fTm529IBq3zVx8OaWL4DWGXURpX9eF6WpEAMc2Nnb7ywIUPRwjLAZZDGic1erUmgKdFSfAHasZ9trsMxYpCi6a8KUhWZp4I9VxWLNs2JA4Q8qXn3DyPyclVFo4mpzTcvooY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=Jy4VF6yGepfAlqaF1A_oW7gveEO_or9qsO1hP6-c87mJC6HPVsLXiUucFsbTwNsm6Vysh5KOYR0pTWoPFjWrpYySrokgRWOhzpBTfzdAtpyZLyV2p-GIGAYSR0enNWFjodUfVG4m2OLcRUvgC5uSPff0UpbzEYQAULY7cOPUIGiCD00T_h8Yyts4J0PPAyhKmq1zqPQIRu2nuOKY60sMy8HYyQG1CbbrptNbw0NpiblksNX0oFJIX_rNcM7JJyYDqfbAp6_Vd1zDbEUofwXrB7LSsWuKG4dbaXtOfx_6LTuTuaBP7JZxlU7cRPjipmj_Dpc7BkCuXgV2BndkF9zR-I6Q8sR03_ta-qemPemstYhdZIz6NL4-FcShJzq8bqDazrzpCiZLPeJ6ClHrwdH_GPfcHM8aUJ4osQuAKKAjweJ6nXcRl60NcyjXJy9tkrQpE8Qpyk3pVz1q3z3EIIrbc-UaoBQ2bh7F3WPbAneCQQfSPdR94CuDr1aktDeppabuf-SLPmPLH7U7Mn_-Yki1010RiJlYqB34wfiKiEG4fTm529IBq3zVx8OaWL4DWGXURpX9eF6WpEAMc2Nnb7ywIUPRwjLAZZDGic1erUmgKdFSfAHasZ9trsMxYpCi6a8KUhWZp4I9VxWLNs2JA4Q8qXn3DyPyclVFo4mpzTcvooY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب رو بیت کاگان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83974" target="_blank">📅 20:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83973">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3bGTZDxWBxfMhuzpULZEgRzYUOy5Sr6SvRDCLMTj_Fea3ugaAjmKgHKNzyohc5aqpv6ruA1zJupAQDgqCcLLJ8AlCxlIClPVYCmrOjUHUMKxytk2kKjS_jC6XZcWfo_zK-BVx9qr1Bc-Pq0mrVRwxM3tdYwjzF4EcpYv94B0QPXOu8cwBzXJwDJXyHWzIxY3twEwpFAhNDUAQ_tcFQxLqUWs88qzaqO-kRNklZD1gMM8Z7GXoqGSo-i-gR-9w0TV0J4FulZMxzCFEVQyGyPCmrYrBREaszsZqF_9Fy833QXdt7_nHbISCcEDJE3eNa3Aw6A5kl2TnfEiDT0TTnfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف:
رئیس‌جمهور پزشکیان فقط از طرف یک دولت صحبت نکرد؛ بلکه صدای یک تمدن ۳۰۰۰ ساله بود. او صدای قدرتمند شجاعت، مقاومت و قدرت جمهوری اسلامی ایران بود.
زنده باد ملت سربلند و مقاوم ایران.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83973" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83972">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83972" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=jhkl-_yiOm6akuZ5PC0nxjZuhjZvMIrxHDqFW4fhGOd3AhKycdQBmjza8cV-RWt0Oai92oSUqmp_ARxrrT15Bc8lln76Lux7RUUOOrNqs9fgc7OZO-MFcJq2dBPA77p9MVwzGXsTX2Mg5sl7N9zhZE4pd_YgMCtopvJXTd5sd1H16Weyy2QkEpT-maZLJvZkrKrCbVyS1BQtZBdA01FuzYI7j_2advSroUX-vKTZ1cimoGDZR0XzH82V4JFPlFT3VCNhf51hOh2TZym6H2hkG9zFBRLPjvK3Xju9ZMdnr7MAcwFhBrZgXBQ4nAXffvLk7AAoLefSdq0Dhnu_LblJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=jhkl-_yiOm6akuZ5PC0nxjZuhjZvMIrxHDqFW4fhGOd3AhKycdQBmjza8cV-RWt0Oai92oSUqmp_ARxrrT15Bc8lln76Lux7RUUOOrNqs9fgc7OZO-MFcJq2dBPA77p9MVwzGXsTX2Mg5sl7N9zhZE4pd_YgMCtopvJXTd5sd1H16Weyy2QkEpT-maZLJvZkrKrCbVyS1BQtZBdA01FuzYI7j_2advSroUX-vKTZ1cimoGDZR0XzH82V4JFPlFT3VCNhf51hOh2TZym6H2hkG9zFBRLPjvK3Xju9ZMdnr7MAcwFhBrZgXBQ4nAXffvLk7AAoLefSdq0Dhnu_LblJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
من فکر کنم تاکتیک ایرانی‌ها اینه که منتظرن چون فکر می‌کنن تو انتخابات آینده دموکرات ها پیروز میشن و اگه پیروز بشن دیگه ترامپ مجبوره بیخیال ایران بشه و از جنگ خارج بشه.
و خب جواب من اینه که خ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83970" target="_blank">📅 19:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تسنیم:
عراقچی دیروز خودسرانه و بدون اطلاع دادن به نهادهای مربوطه و مجتبی خامنه‌ای، زنگ زده به ویتکاف و باهاش لاس زده و مذاکره تکنیکی کرده و برا همین باید توبیخ شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83969" target="_blank">📅 19:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83968">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حین سخنرانی پزشکیان، نماینده‌های:
1. ایالات متحده آمریکا
2. بریتانیا
3. آلمان
4. فرانسه
5. اسرائیل
6. سوریه
7. لبنان
8. عربستان
9. مصر
10. امارات
11. الجزایر
12. لهستان
13. سوئد
14. دانمارک
15. کانادا
16. ژاپن
17. جمهوری آذربایجان
18. مالزی
19. نیوزیلند
20. استرالیا
21. جمهوری خلق کنگو
22. اکوادور
23. قبرس
24. ایسلند
25. مکزیک
سالن مجمع‌بین‌المللی‌سازمان‌ملل رو ترک کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83968" target="_blank">📅 18:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83967" target="_blank">📅 18:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=twbsH7dvc3qwU4qcm4gzAYRWjTwqsPkIq2obCOwVbUqDRJ_WMHVjwHpiTLqY9Xse_u4bo-PqjezBbfCA05ncXUJuaa3eqa1NMIHeAaf6gFx5a0vGn5L2_yEJYECMnoXHhX7SpURtGTG9zJD9GrAzlVi20ZUWkUuBtbMX227nEWFQp595P-2BN3egqhWTwCT92xTN5CpYa2owgOECg5VzfU_rQuH49ZPsyWZKurbfjZ5kTC0rfVvER1EfrirAgtN0eUk3KxZ_HWSlMeESlwE5PwP7KGGaQj8eGxGm77YbNefm9jjyTKi5fFhOBdLmr8r7w35zpT_XiiCYXDNtOavinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=twbsH7dvc3qwU4qcm4gzAYRWjTwqsPkIq2obCOwVbUqDRJ_WMHVjwHpiTLqY9Xse_u4bo-PqjezBbfCA05ncXUJuaa3eqa1NMIHeAaf6gFx5a0vGn5L2_yEJYECMnoXHhX7SpURtGTG9zJD9GrAzlVi20ZUWkUuBtbMX227nEWFQp595P-2BN3egqhWTwCT92xTN5CpYa2owgOECg5VzfU_rQuH49ZPsyWZKurbfjZ5kTC0rfVvER1EfrirAgtN0eUk3KxZ_HWSlMeESlwE5PwP7KGGaQj8eGxGm77YbNefm9jjyTKi5fFhOBdLmr8r7w35zpT_XiiCYXDNtOavinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت آمریکایی در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخنرانی می‌کرد، سالن را ترک کرد.
این درحالی است که نماینده ایران زمان سخنرانی ترامپ محل را ترک نکرده بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83966" target="_blank">📅 18:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn2m681HABPJB24bl1JQeZyiDToKW9xa7rKxbDRPsiNgpe2BMGD3lPX96XkmyAk-_9wtWueXL-dydUjsEtDAK7frEssXuQ-WIM5Ig0r1DZ9trAXVFZP07D9JXIgLjI9b1FA9JsBAuSuSm-r6WvJ2Su80tU72OpJFKvaUhZcwx6iQi8t6OwiYqZSNPGgYnXqbMCrbkYP1XZV30wpsHsxVUztthH_3i2sFpi93n1pxIPz6dCZBRFUNnz6GJozB2WvClbbLHAvb6qMhPndR13VkxVevCNrOq7ypfivL7C8vFoDDwksUi_2FcMB7IzGoS9GZR3ctF0-moLHB-oOzvRvuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83965" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGHdDjDQM2abMGKaAprg-cliTt297RfmAJVXNV02oib5DpVPhMzNfc7Q3hp6XlklIh0dLWe21EiwfQ6T8A4n9bb0VXS6fr9vm0ybJ-ftJ5yhMpcuyTN63YUPK2fxiPcagbov_dq-zl36-hRskDnaV227-XQd63D7VZfyjiwnnfpNxNrozg0yQ6GxAsbc9FEAGxtvl6OEnIvqs210yKHcNwchzPopT40p5YmhzNcG9JeJ6ueW9XP5uRgSuTtTv75kC19Prgl7KPWOr0G-tBu0d6hcO366U6Cg-X49T-RHB-3cs5140NgfxMNs5ZSImFocOkZkhnn5PxUEeMIRFnEfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار کوروش از فناش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83964" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تو سراوان باز بین نیروی های نظامی و افراد مسلح ناشناس درگیری شروع شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83963" target="_blank">📅 16:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🕸🕷</strong></div>
<div class="tg-text">اقا تر بزنه ابرو ی مملکت میره</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83962" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWD-mFvDDYq8aZYQHMMpJSidqm4J2UyLBcw3hYvQ1OXvqhtsmmScUr4mKnlhP9peEswLmHx3kRAO3LK9kWn5gpCaMqG-XbmLsqd-xe-04DnUQ14WpafCPD9nk0CWpayrHzindEAPAZ6J17wrm05HFm597s1kptFCTKSMvecmYUA_hkC8bDhZv_DehcETVB8NlUJlKUgV_HQwePXAg7E6IYnKkLNGgvTzfv7YFmqOKtQST1TB9q9GNBERzUIg3I1_7mbScOgWURrK4DNJPh5IDvdZOd2iujjFdkPvljYSIsUZkFYnR46En0vuP4OpzyC6B_WGI7iQTjCs7vCzkgLI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بترکونی رئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83961" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کوروش وانتونز:
به زودی یه برنامه یوتیوبی میزنم که هیچکس دیگه نخواد چنل پوتک رو دنبال کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83960" target="_blank">📅 14:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استاد خوش چشم تحلیلگر ارشد صداسیما: کیری قوی ایم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83959" target="_blank">📅 13:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شرکت کننده های عشق ابدی قشنگ ۲۰۰.۳۰۰ سال وسطن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83958" target="_blank">📅 13:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83955">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spYebKs-kY7KdhIImP8dUyT9FwiwAuIs0xlbv8o8nT2kkzSjvD_rSZ2xOQz2zMot-WpZzJMgeqE9RFvPK9dkvcQBBjCcwnWvI-Rhbt1GXbIxVzwASUTuDQDP0OV0lz8vClNKjKNY_SJ4vV89bhhkbFTLM3lFxnLzDovCM_Q2CqoQL6sadSc4FUlmPaiAr-lPEdph2xZUe61i9H9O3mAvBS9bJMmWdcS0Hvx4bt1cFs1zy6R-Cu_euAQ5W0Boxc_FMacQk6ix2z1NcPitkOwGKxWS8lYfCItp3GaWpJLoeU3-fAIrYcg5zLI-iJHAqY0FvGRQug9jKBzMY_YefD69Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو حالتی هستیم که تورم به ۱۵۰ درصد رسیده، محاصره شدیم و هیچی وارد و خارج نمیشه و داریم بگا میریم، به دلیل بگا رفتن پالایشگاه ها و پتروشیمی ها و کارخونه های فولاد بعضی اجناس تولید داخلی حتی ده برابر شده، تو پمپ بنزین ها باید دوساعت صف وایسیم که ۲۰ لیتر بنزنین بدن بهمون
و تو این شرایط دغدغه‌های ذهنی ویدا سادات:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83955" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83953">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odeHX-OG4R2S1ZE4eQvFeNV6yHMmXkXLBBMKIZkXOmgLuaY2OmEvVAAxXBb9z-SeG2bzp-gGtdpK_DZI-8M4Nb9KTjqLBJLiJWy2CUTJ2MLP3Ovp1s2qsytOkXC8mH2VR2AAneAAkw_m9ciV2PZ_U_gmDjRqm6XWZve2F1Dkw11nPIufe4lbh9_f_JLLUtZ3sPpUvNZ-wOAm4EK_caKphvrZLM5w2mQJec-Fo5spVK1_3ElKRqEijZEbtCxCwfzME23MCQ9dxzv6axMKiRxQkYfQu4moGGVYeKB7hjXg6fO0jsvgNXs-xHN_Ff6om0-X1PRvUn4W7iuD2CqKcNU-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان بیژن بودا، از خلبانان نیروی هوایی شاهنشاهی ایران و از اعضای خانواده نیروی هوایی، درگذشت
او سابقه پرواز با دو جنگنده F-4 Phantom II و F-14 Tomcat را در کارنامه خود داشت و از خلبانان باتجربه این دو جنگنده به شمار می‌رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83953" target="_blank">📅 09:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83952">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اونی که امروز نمیره عقل نداره، بچه زرنگ امروز میره با معلما رفیق میشه از شنبه دیگه نمیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83952" target="_blank">📅 09:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83951">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مدرسه چطوره</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83951" target="_blank">📅 08:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFYBlnBTekDkyi5lUb_8DahKGQ3lz06pVdJsbdmm3UFXvV4gjrkxLhwyvRJeJaxn0X-r_8Wgy3rXvGyG4eHvp7iNVILxqvlESVtrt9N3huq-VMTta1CAJ1Vz9g4Ejvhz96OQMI_faHGOGQi7s4QmVOfw3AoGeFGvlqHd5M58ZCDADPN7vf_S_4IlsdvowMjDZwlhwrtlbyY7k4S75dWJ2DRZ6j3bDF-HPqgw7zxu8CEqPJERLIJ5-LzaczbaIS8PvTOpXf85rcFBB79BVnsF0q9_nm6lxH1kDp8aBIvW_-BSm7mIrwpgNCypP-EmFbo6jAl9HakX-mQKLQxJJ-cwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نیویورک بگید مسعود اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83950" target="_blank">📅 03:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83949">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آخجون ویلسون دوباره مست کرده</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83949" target="_blank">📅 01:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر پسر عموی مهدی چیکارا میکنه سپاه یه موشک ول داد سمت یه کشتی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83948" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044b34344.mp4?token=BWVHUVXvf04sXm1dcpnqCURiPiLyPHQp3KdFzfNG068VBgssepGlvKRHywfoh7eWkfLXc1WaVx5Cutr-doQhaTvdL1gKQ23JDcVKXu7i3aBH0lSdpZqamnEkMs1Jc6IDUTxSYkXUoXoPwIrfSzTZV0exUh9U0YduAt_dKBGgIEYfFLtiEuImZasNWSZzygToEMYsq1dNa_TWJuVHWno3CWQoyekuBmfDYf68ee7R5GUXS1mp1xaeTSt3mJilzYrqVH-H_1h9k71xi22uca3H-qsDBHD9m_aMYb9O3GSZuTASYzTKDN5U6tdPhHoMjXDSq0ft8LYVIeWyuWIBmdPpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044b34344.mp4?token=BWVHUVXvf04sXm1dcpnqCURiPiLyPHQp3KdFzfNG068VBgssepGlvKRHywfoh7eWkfLXc1WaVx5Cutr-doQhaTvdL1gKQ23JDcVKXu7i3aBH0lSdpZqamnEkMs1Jc6IDUTxSYkXUoXoPwIrfSzTZV0exUh9U0YduAt_dKBGgIEYfFLtiEuImZasNWSZzygToEMYsq1dNa_TWJuVHWno3CWQoyekuBmfDYf68ee7R5GUXS1mp1xaeTSt3mJilzYrqVH-H_1h9k71xi22uca3H-qsDBHD9m_aMYb9O3GSZuTASYzTKDN5U6tdPhHoMjXDSq0ft8LYVIeWyuWIBmdPpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یعنی کیرم تو این زندگی ای که من میکنم
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/funhiphop/83947" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ناموسا بعد از بیف وانتونز با پوتک هروقت چنل کوروشو باز میکنم یه کصشری به پوتک انداخته، بس کن کولی خسته شدیم</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83946" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eckJPW6Q2OoRwF_k_ANulDF6drqqvbEeSZFniOB6I5CoaIMKcy7w5SvaiChEDuytjHZuBdO2d_Xftw5nsgm2wTne-ECwxB_RmKlbEKg1FWEg5mcGHO8vjTK8KNjJeMC5VFs7ND-78kfApJJU8cWQqyc3veKhI1HilIw1xUctJ34tSU5M8ei8ZXE119KEQcBDibmKgszGE2d8vKMtn5Gfy0VnWj_wE8VXWTrb8mIh38xDtiQIUGvl1tEALXsltAlvcIIR1j3uptwDMYECHdXUM4kqxDZGEDtAsXZf6LqvvTovi3LrDK6xpUm0hHIFNkeuRu3wrvut_lvd4cOXJ6F6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_91tvszToxKrxK-ma7UR5evMAHMEK3BsyzT7BEIx2A8CTGfZfnrIlXlVC0g5WJIOTYoMBEmkYLl7xY-KjMtzW32_Xxv0Rdx1BT7xaxJmpO0XzVZUaXnR0Uh-amtLlrHTFevNRidnSUa07lSBw4kEveFgM34LlLq1robHnp5tw0MYvtS_Jf-nKlwJ0rsBZmSrvyKSBGWTUgTISxqAmNHs5d0M9bJK8lSoft2_TxOjdnXqhm19fGThgOUxX0KfDIg_Tne4ACex03MiZUFfcggNWZTs4epyVZDtnQSbok6bIkn-Xl45bLcJJ1qvDF23rDY5PQaqU8srGwvAxu8qM2hLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پول دونیته ها حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83944" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=egj15TXfgzkSOQj8ely0Hw2KmpsGeNXIWx83KBUZS0gNSgFU8AEi8L-z6rRFlhK9UVKS5gkntZJPYjgXmHrNu1moEmRYs4tNTJjsXOeLdH6FeGAz24pbsI2gtQu8HSV9Hx3pRShMP0uUL6Ks1scqcOjvVkp582yN58sHT5Zjy1g8UR0DnY3hFovEvI2ToV52V2BPVf9Jcf2R61HyKlcFwe-1RbqszjNbj9o94ku0PhvAvU0E5F49ibvFmA8nUfh9j_x1VFAMBivbBXkLcKMjlNghWBIigKRQERi8uSnt7Dr26sQd9IcxIz6SiZ-rjsz4vMCwa2mzrWOOFQEXcwF9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=egj15TXfgzkSOQj8ely0Hw2KmpsGeNXIWx83KBUZS0gNSgFU8AEi8L-z6rRFlhK9UVKS5gkntZJPYjgXmHrNu1moEmRYs4tNTJjsXOeLdH6FeGAz24pbsI2gtQu8HSV9Hx3pRShMP0uUL6Ks1scqcOjvVkp582yN58sHT5Zjy1g8UR0DnY3hFovEvI2ToV52V2BPVf9Jcf2R61HyKlcFwe-1RbqszjNbj9o94ku0PhvAvU0E5F49ibvFmA8nUfh9j_x1VFAMBivbBXkLcKMjlNghWBIigKRQERi8uSnt7Dr26sQd9IcxIz6SiZ-rjsz4vMCwa2mzrWOOFQEXcwF9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکارو یادشونه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83943" target="_blank">📅 23:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRapBadVpn - فیلترشکن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mym-Y2sXbxDA5tCnMy2g_yAYiDOly6w0sxkCvv6s58XIrtbmY6-bmezVn6eHM40hzIDLgi_hl8rijIvzxLxNf0vV7UgjMh6efkVl9zyEUkK_yvKEZow3nXQEofJmRFADmGLMhgf4AdLF_fsxGUBrirBJ_itO6LkOC4c7pAf7vDKi9Ak-qcH3yDqCp96tmh9SnxMW6diRLehmn-71L9G_fuvjcQVtj6YJFwLWMj9XHLJiBQLUYj7SQHbcrp5JeI4q6DY7FMbTvpO6xJYjJtOuIc9YruihMwBeG6WYBl3AjJHMWsJ_tJYM4hssOxak4lOLSfebMavuipz0hqdqGI4zxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
وصل شدن آسونه؛ خوب وصل موندن مهمه!
اگه از قطعی‌های پشت‌سرهم، سرعت پایین و عوض کردن مداوم VPN خسته شدی،
RapBaad VPN
رو امتحان کن.
🌍
سرورهای متنوع جهانی
🚀
اتصال سریع و پایدار
🔒
امنیت بالا
📡
پینگ پایین
💻
پشتیبانی 24/7
🔥
بسته‌ها از
۴ تا ۱۰۰ گیگ
💵
هر گیگ فقط زیر
۴,۰۰۰ تومان
و مهم‌تر از همه؟
لازم نیست به تعریف ما اعتماد کنی
😏
اول تست رایگان بگیر، کیفیتشو ببین، بعد خرید کن.
👇
ورود و دریافت تست از لینک زیر
🔺
@RAPBAADVPN_BOT - Test
🔺
@RAPBAADVPN_BOT - Test</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83941" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83939" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83938" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83937" target="_blank">📅 21:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83936">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8382999db1.mp4?token=ta7sxz-nujo92yDWbZFDcnaIjV5jAQTWLEjE77mhyc7gO4YsPXKgEC_aUc69LWCbW7m-UH5bSeHUTNwl3IWgf6O1fZkSTRmhNHnYP3a4UZHp_jZX1u8oAC6XpxSIqoghNBS38Ja3i-7v2uvzvj1NVYUQJVSgqYmQYeiYbmlWQl9ICL8oEw1vCCiV1sDUNpmiBjAMZ1PtwRtPqzVUcj-bk5GSH_RE8eTpS_f0r7_xIrMXWFP8cF7H1L9CR_jZsuLTKcPj3m_7lKIw_8USnvL_v8MhBix2D7Dow23qB0GwPqBksiRGlU0ivTnHs4RORDXrH5g0frSTR6Y-Yru2V7iG2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8382999db1.mp4?token=ta7sxz-nujo92yDWbZFDcnaIjV5jAQTWLEjE77mhyc7gO4YsPXKgEC_aUc69LWCbW7m-UH5bSeHUTNwl3IWgf6O1fZkSTRmhNHnYP3a4UZHp_jZX1u8oAC6XpxSIqoghNBS38Ja3i-7v2uvzvj1NVYUQJVSgqYmQYeiYbmlWQl9ICL8oEw1vCCiV1sDUNpmiBjAMZ1PtwRtPqzVUcj-bk5GSH_RE8eTpS_f0r7_xIrMXWFP8cF7H1L9CR_jZsuLTKcPj3m_7lKIw_8USnvL_v8MhBix2D7Dow23qB0GwPqBksiRGlU0ivTnHs4RORDXrH5g0frSTR6Y-Yru2V7iG2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو سرحال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83936" target="_blank">📅 21:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان تروخدا شوخیاتون با باز شدن مدرسه رو تموم کنید، اینا انقد تعطیل بودن الان از خداشونه مدرسه باز بشه چند روز برن مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83935" target="_blank">📅 19:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سالی یه بار یه خبر میاد که یه زندانی حکمش اعدام بوده بعد از چند سال عفو خورده و آزاد شده، بعد از آزادی از ذوقش سکته کرده مرده، نمیدونم چرا این خبر هر سال داره تکرار میشه، بس.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83934" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کی فکرشو میکرد یه روزی نتانیاهو، پزشکیان، ترامپ و رضاپهلوی همزمان تو نیویورک باشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83933" target="_blank">📅 18:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=HNh9u5snFYQGUwl7rDznytJRYwajuA8kCK3ajc2qA6-dCr-AtQPGG4BSAfrdHnhFynlmX1jLC_zLZT7nd8p1c_jJ6QYBLaKDmyn0AeEQgavbEPCjnmnVTkorbRrkL_WRyt-z7BksThmwVRW2VPpYb3GYfs74lhc_QwZPN1SeJmYk0W-58_1ju1SDAEdGX3cAAX5ux2B4e9fmHvRCoCA3Js-2E-gHXDQ_8L3tHQxnZpNWcsP0FYkaFTp6ZdRKdy9Fbq6A7fMK-V22NsxjgLUvssWZ4daOBFz5wp-OmC9QhkZEuFLWznkGdMHnuvFA5q31zx2O7izIX3YwhC1pDGsVUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074aaa2a17.mp4?token=HNh9u5snFYQGUwl7rDznytJRYwajuA8kCK3ajc2qA6-dCr-AtQPGG4BSAfrdHnhFynlmX1jLC_zLZT7nd8p1c_jJ6QYBLaKDmyn0AeEQgavbEPCjnmnVTkorbRrkL_WRyt-z7BksThmwVRW2VPpYb3GYfs74lhc_QwZPN1SeJmYk0W-58_1ju1SDAEdGX3cAAX5ux2B4e9fmHvRCoCA3Js-2E-gHXDQ_8L3tHQxnZpNWcsP0FYkaFTp6ZdRKdy9Fbq6A7fMK-V22NsxjgLUvssWZ4daOBFz5wp-OmC9QhkZEuFLWznkGdMHnuvFA5q31zx2O7izIX3YwhC1pDGsVUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برا کی ویدیو میگیری مشتی فنای تو ماماناشون گوشی‌شون رو هفته پیش گرفتن ازشون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83932" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83931" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه سوالی که هرچند وقت یبار میاد تو ذهنم اینه که کوتینیو چطوری دلش اومد هفتمی و هشتمی رو بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83929" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9SirWlcXBESUpjggAHnmJSxNBhO1kR7t5bpDpe-7oGhpk3BLFYXMR4KkzrFNjivSZFPavXJAgMi3QIcuTvCjJrFrstPKZ4C59dhq52mpsgWRpFTDyHGubcbt9mFFva49brl_YAQrO16BVJzA__9H3nVMFIbBWe8fmJlFqfeKgjfl68imtpDaYmm1xGm-7FCHylsWwFCkl6YR9pgTVqmS2AKcuSG1olm2x-7fFn18SEfFPdXKSKNhNA7inSVsszSx8v-PvBWOWV7wONwGsIoBdktQEBJJ28oJg8D6eK9zfgQjd-B6vXNpM1YHh9Zwu11Decb6wPefw3GlLkIyaaF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین خاطره ای که از جوونیت یادمه با حسین خاک تو ماشین بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83928" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83927" target="_blank">📅 15:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwqS02HXfrdo7WS8vVF5kIs-R3XEiarTLMJPQfU08A9HrIxeycDV8jnvUY7GuDDHeI48GhcOFybBJ5uLIff_BcdwVhv3REm5GPaS-SJW2UglFoc7zX68gTR-G6vXF0szOvkhD2FhpUspG5S0V5LtkWe1F6VxZFk3C6Atkvu_ZwRWaqBoWfU5MHWSPwMDegCaxJNzMNMLHnntgDYeLo0pWf7cAU2tnMbUsaAcf7wtVj8jAzjtji-jV9h4r-Z1Laa2LN2nVOG8aag1y_X-ywXnApI08e1ML1v8vcJEMt5z01lanZuAOXVuOpXqcViCWdWvscp8SvFS_XErL3kZtbnJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون اینایی که تو صف تلفن زندانن پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83926" target="_blank">📅 15:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شهریور ۱۳۵۹؛ روز آغاز تجاوز عراق به ایران
ساعت ۱۳:۳۰ روز ۳۱ شهریور ۱۳۵۹، عراق با حمله گسترده هوایی و زمینی، تجاوز به خاک ایران را آغاز کرد. ایرانیان در دفاع از سرزمین خود ایستادند تا ایران به دست ارتش متجاوز عراق نیفتد؛ جنگی که پس از نزدیک به هشت سال، با برقراری آتش‌بس در ۲۰ اوت ۱۹۸۸ / ۲۹ مرداد ۱۳۶۷ متوقف شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83925" target="_blank">📅 13:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بکیرم
ماکه پول نداریم سفر داخلیشم با هواپیما بریم
🤣</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83924" target="_blank">📅 13:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">از فردا محاصره هوایی هم شروع میشه و هیچ هواپیمایی از ایران حق خروج از کشور و هیچ هواپیمایی حق ورود به ایران رو نداره
احتمالا بعد عملی شدن این بزودی محاصره زمینی هم شروع میشه و کلا زندانی میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83923" target="_blank">📅 13:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83922" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83921" target="_blank">📅 12:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مسعود رفت نیویورک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83920" target="_blank">📅 11:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=lGl_9QC_FDGsllb8dk2en07y5HcuYviRVgqmCY0NldbJIm45z2Ryq9yge4VlCXG2b2-gkFGySDgSM-1JqbnTCVNfXQoCSXM2Z9IO1fLKC5DDrZl4zooAuseLhxn5BXKybU0j6hQwadOPI8WwW4darok3wE7Cj7pTJfZgyHkxAiTI20kGL9wgXkGBvrQypcRvOVwNB0LvgXIaQIvP6RdRez71XapDKcTlQ7L2wAMx2Ehs2nU3t54OSwqoVm0ENUZuwVWxJIpdndzDqykFXV1PJCjNoSnYMJZLKfMVG-W3CPuoqff2QqeJXUhfLgiDm_5OkF1ppundEtCsypx_yBv6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0578733e6.mp4?token=lGl_9QC_FDGsllb8dk2en07y5HcuYviRVgqmCY0NldbJIm45z2Ryq9yge4VlCXG2b2-gkFGySDgSM-1JqbnTCVNfXQoCSXM2Z9IO1fLKC5DDrZl4zooAuseLhxn5BXKybU0j6hQwadOPI8WwW4darok3wE7Cj7pTJfZgyHkxAiTI20kGL9wgXkGBvrQypcRvOVwNB0LvgXIaQIvP6RdRez71XapDKcTlQ7L2wAMx2Ehs2nU3t54OSwqoVm0ENUZuwVWxJIpdndzDqykFXV1PJCjNoSnYMJZLKfMVG-W3CPuoqff2QqeJXUhfLgiDm_5OkF1ppundEtCsypx_yBv6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی تو تا الان همچین استعدادی داشتی اون کصشرارو میخوندی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83919" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83918" target="_blank">📅 11:41 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
