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
<img src="https://cdn1.telesco.pe/file/ThMm7mV2Z_JSD2afdUqOSZa_CY9PqEl7FAKX8LaOP1Gvyp2dXAqZsfqJIez1qUswGMC-Uefh4t22gAlZJP00fFxqvVNGeHPlj8ySTfPIEtgphsyaR6fgwf2OHAdj-WrgWLB_a8Rekiek3D77dHQoL3_rxbERTT85EViJbb1VFl0wmS0pkMwZKbjor6u2cShUE-PctwhPN1jZuraBZWY4j7j6YPZyNvX5IWmJ9bqJXUFAw2ILZUg2SzIyY6jEqoaAmJczejkUQTiQMQl95USLF-zpIOfUCBrcDjXtqkXuBI-JwwnPKM2GvR2wuqL_e_nbC7Kl3KSPr39FtbAXPanxlg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFrAO0QOB2yBlo21STeP2qYNilCK3v--VHEjrj-gQfnTqTPz5H20f0oPMuSuiqsoK9AdOQ-Qlle4eycaOiAZKG2_fojcvhRF2xriFlw66jHL4IWyZXZGD4RUbdOKKpSFaBzbNP--SCfKh8B4qz3Uy5n3wCb74rMh7LSm_AIOqrPXu1v5yxu_eYlCwWtdxilaG1DKGMOTp1hgobn1ePOgbwrLRYq9HvyjNhWnbQ3POkNfDCxoI7NfojqqOf7kelWmt0Cn4UURMsJ0giFonkb1qKlcNsLxrYIqHxVWOqac_txnuHVJEui20P2lJAXQdeKdCbUKKjNvoVuJsj7U11YLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZHTWSswehntN8gW_bzvZN2gFpIe19pcqlK2hMf8pAiUAeqviL8t90NdBdTbqIovxXVKQ3DfyBZ3dn2JyiRNsrPJqV-_0rZkq3Oa5F-9GcUVjSXATGw_QlJrxcQBLTRuwTUylN3ub0nIs6u9WTAqVvA_fvGZ18Mk87Nx3czXCtBQ566is0apQ8ya1S07BnmkIb2hkB8v8JAH3KqtojbyWiAIa10eESN94MxCu-DJot1qd-WSSrMJP-_c1qtuJUCMtvc5xClorWSNU146PIj8T0IW4YTUEBPv1PcYkpwd7aiR5mhXZ01PaPjYcn3XkOiKc7fvJBEFpEnud4kdTqNbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5Qtbl2FdMBLT-cRtzc4fY8zzfKXWFcQPbiiw7lk8ygoyTBDtavDuf_yEsNI-gQ39d24WPOLRKAZreDIs69uBJXy83tvQJNtMQmffjuzz5Nrrfb4oll79MVLHiKLE84Z3ZyWVuzHWw8JsgCQojJNNWPfKwpwxDiiTfDMPhddQxZ6ZWmBAViGn-TDZAcL0LiSfveBn5mVmYcNnDp1DIxkcH3Wi0ib3q7HGLljf8XQtaSRGoiVWYaHL8CZ8bApfUQsjrrpFTHnWvhnRZ_ecdbNbZ0xOjPxYnb8wQpHAeDo1NdGhp9l6l2LGdaYtM4FOyI4J3RgwcPiQwfgcndJL0a9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjvsZa6mzHPC1vjyN_9T355u8-nT0SCJEjPN1MDBWyhpySRYtZTqBCn1aouu18EVAYRlJqj2t1d_7XIZkrjjofAyI63_A6mWhros6hT4bnD1L0xT9u3pQNpuNt78-NT9CXsDRIJzxJGCixmVu4zyu7xJTRUc3UDT8VVWnVA5sVRP7HxHDtUn5qxyGKl5ESZBmvPbBzmwKKh5ImUDOe-yokGhnXUGyfgjo-NSouOqTZHgv5PYT_DjXdA_uIepYe5om1mQmsPxfaDq-4k2jWM5AYGfSOIlyDgit8UF98BRg03T24x3G52py6SoE_CJxn4_k-OzDK_k-K6E6p7o9VfeHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4z5piu8UNjkoRS1rTBv_KO7-4yQ5w5qd5bbQhTlio9c4ct2pxOV6AdALdHEHbcOl1EfRxkP_MY5-cWITQHMBl-RmKKE91NpmfTGLXr2XKLWI12tMMpFlvD-vnTVtcO0sK6sp0L360150FY1wIFmfNHLdnkT9fGZXZAnDm-TzbWfoWUL-v22EfGG21TQcnrf4pIlvBuGYobe9oC3pcDiJ67kpoIb6-KXJJRn7r17ojd17Q5u-Yg16iEzQWBBzrLpD1fM3-wwZW7-T1IjblWr9Vf4JfP1-9093CKs-lHCyq0X6Y3b6an6TKlralK0zL0iuF6mqT4lI2-lvfuntWCq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUM8OZaOhtglbVN1ekZ69p8k9Vs4hdCVnVgJiY0_rP53fuyI91GNtyXZj1TmhlsJ6pQTcbbJt4mItxwCzG0uHxRQg9j2t9uc4BDhOBr00fcOU9U3ZlP3cgteSPwIUSqjzJXZBrcD2qludIt8Z3ki8kj7lCXEyNGHS5_qO0hf1JING0Y6PyjFTdL7pBYoU4S8d9Xeeyl7JKNeL1MQ14Un3Ez7EajMuYNvek2g8fIL2vbbs91KVHU7DVI1vu9Q2AyrP1VsPA4OwQk8wIIZNw7WMqI4erk5u8XPA0PV91S65p0R75bWahRNfYyKH2DCPpfqUMytgH3ZUm_gPsxQTcO-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=g9KWtDn2f-6G20PgKO0c4cqYECm7Fh-eHBxSeQEdtW5ju0WE8vrDtX-LT_ZSFJg7WYrCSzZMOxhbQTC7OSXRKIx7UZTSqmnAtN-iHl3a6JIt3WOy62odKElGY9YN8uC8CjggOj3tvEzsECgtjENEP0S9szVAdjQKQ-ZgzEtIB59Z4flEeHq3x2spSSDJiYMqZNv02zD9Bn5sgKb05tKx6OEqUr7t94Rg7zjWMRJYOqhhIoxWcsJ5it1LfPQZxuoIWnwm-pcvH4UQdqmsquTmprquQZIVzkNqFib9JcJaQ02k0LUhKhW5fPbebUUiVah_eBD3UB0GkLiWLAt6hkyoh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=g9KWtDn2f-6G20PgKO0c4cqYECm7Fh-eHBxSeQEdtW5ju0WE8vrDtX-LT_ZSFJg7WYrCSzZMOxhbQTC7OSXRKIx7UZTSqmnAtN-iHl3a6JIt3WOy62odKElGY9YN8uC8CjggOj3tvEzsECgtjENEP0S9szVAdjQKQ-ZgzEtIB59Z4flEeHq3x2spSSDJiYMqZNv02zD9Bn5sgKb05tKx6OEqUr7t94Rg7zjWMRJYOqhhIoxWcsJ5it1LfPQZxuoIWnwm-pcvH4UQdqmsquTmprquQZIVzkNqFib9JcJaQ02k0LUhKhW5fPbebUUiVah_eBD3UB0GkLiWLAt6hkyoh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=s-bPaQaRIiBT30FUFvb58iF9cLbhn9qPulk4iGYKpcqQfyB2f8U-OpY_cZDy6IVk0manc9gt9J75yDQwIGnB33j_PtYXinY9XyeX0_1vuuKyFREqxna2_HktYFx35viUXjKdZ7r8blWhkgKl1cGG875Kef66p8ehMd0GKqMgFzOYLGOk7DYUiel7D_Cr3d27ypZ1Ru_lWkYYpCW_SWQZlC3tuIU2aNiBIp-wuyLPPa5yFv7Wek-A0g19GRj91Jgu3naxx_w5py71Wdo_n1fIR9oNFvQg1R-cd6WPyAnMDQYo6OPdM0xQVMdI5L4rrcV5-ar8USxs46Uk66EEpalnHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=s-bPaQaRIiBT30FUFvb58iF9cLbhn9qPulk4iGYKpcqQfyB2f8U-OpY_cZDy6IVk0manc9gt9J75yDQwIGnB33j_PtYXinY9XyeX0_1vuuKyFREqxna2_HktYFx35viUXjKdZ7r8blWhkgKl1cGG875Kef66p8ehMd0GKqMgFzOYLGOk7DYUiel7D_Cr3d27ypZ1Ru_lWkYYpCW_SWQZlC3tuIU2aNiBIp-wuyLPPa5yFv7Wek-A0g19GRj91Jgu3naxx_w5py71Wdo_n1fIR9oNFvQg1R-cd6WPyAnMDQYo6OPdM0xQVMdI5L4rrcV5-ar8USxs46Uk66EEpalnHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vGfnIbtIEfdHOYt5tw6Z56aHNleMWBHPiG1NYMxHQAd1GhAaTDEFCBe5MGoge3jU9PtJgXO7PThKy2_fZ254Ip-2ic0jP_HkNp6CtosgTZ7sFJWvTPTucxU0MU77p4-O51ClAL38PsFEf_HdgKu64xzgVk9CP9tQrBFERWRuo83foSeTuXY7Jvv31EtV95X5xRkJxjjWr4fftp2sbE-SwvQgbIU8_QWTBOBTS92s1PrabfV5aX8yHVGIxL776Ov-ljm7mb4MFEFzkoCcADeD5i_lTyrcmV10nvXhdR_wwHyzqpQ6RhlOi-e4-C51q72cajwwrfSJl2UuGzE2oQ-WWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Liskw4X6heR0KiZWrb5kLaDksfJANIYoKCmry69xya6GioRyZ0ijhfBsuC_kyTRqMcfnhNquDPFESjgIS2wj59wHX2O4fsoEbCBSs9x94occ_I8pRlQe2McIpf5wPZYvYpJ6XtqUcHcU782kT6XpY37hz0zDmE3e637Ct_dyBBNInt1iLJQph63G1uyR0vxpsvHNSSnlUriDHnViWK21noxILxk-VaTIcx2R6ZeJOPhf7E-VULEN22aey68W6276vdTPZb4xpRGC9DRj16YJ6_VgAKAqzHOFXJbBM8diJid08DaqxScmyylWtf55Ib6CS5utoPDUYAeiu-v27uldrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ky0SjJLUUEvH3Cg2if3AuvTPIQxCZZCxqctvqfkUiUt_oBQVPiR-0w5_pO0AbQj0EMBKrma0B9XwTuTbjrrdrdG3JbUB7toergoECMDpz8j0xO4vZiT1eHU0e0iqnZT2x_-Eigcio7ycqD4U-KTZW-uynu7yiwAzGrUiHYjitkn4K_AtRz3gBZdX_a_jZjUrMjKZ0MYkVgrymn1OSsxRAWWjQaaACZv39GZ60VW_aMj87ZbvjWi824o9fd7CLI2RhhT9F7wOjdiETL6WwGQuODpW6gRCwqve-P8S6-VK0JB1M8QMSkdXBu775Cph8PVGFbtOM5GKcdrk0w41jybukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=ky0SjJLUUEvH3Cg2if3AuvTPIQxCZZCxqctvqfkUiUt_oBQVPiR-0w5_pO0AbQj0EMBKrma0B9XwTuTbjrrdrdG3JbUB7toergoECMDpz8j0xO4vZiT1eHU0e0iqnZT2x_-Eigcio7ycqD4U-KTZW-uynu7yiwAzGrUiHYjitkn4K_AtRz3gBZdX_a_jZjUrMjKZ0MYkVgrymn1OSsxRAWWjQaaACZv39GZ60VW_aMj87ZbvjWi824o9fd7CLI2RhhT9F7wOjdiETL6WwGQuODpW6gRCwqve-P8S6-VK0JB1M8QMSkdXBu775Cph8PVGFbtOM5GKcdrk0w41jybukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektABnLtMbqZJjlcjxYpH9ZyM4yIaAlGJyvQ12kVasOu5GWd704TAEVYoCL22hEJWk-9VnB4HfIr_GvHnWJVaYWFytaIC5MBKNV4kDD5FABzHfbJRKlXBxxM65q0kKUbmxOzdglypj2xaPRQx3TnXVyNVZb3SpHrue3M7rZOax3NVUj1WpWR8BOAa3Xj55J4jdjUMqQgdjHu9GUJJmYZc3oo2OaMMLxv3hTQLs1wT_ZLyJNDD_KvVSNy7GcYjz5pygwmYdJ2n32x2DvVVM8KvZo5boxYtc67Veoo8I_Fw7vAzLDOhHDyoZRw4aS1IjHEXJOVsyfE_vesyCllxttFHJ3EI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektABnLtMbqZJjlcjxYpH9ZyM4yIaAlGJyvQ12kVasOu5GWd704TAEVYoCL22hEJWk-9VnB4HfIr_GvHnWJVaYWFytaIC5MBKNV4kDD5FABzHfbJRKlXBxxM65q0kKUbmxOzdglypj2xaPRQx3TnXVyNVZb3SpHrue3M7rZOax3NVUj1WpWR8BOAa3Xj55J4jdjUMqQgdjHu9GUJJmYZc3oo2OaMMLxv3hTQLs1wT_ZLyJNDD_KvVSNy7GcYjz5pygwmYdJ2n32x2DvVVM8KvZo5boxYtc67Veoo8I_Fw7vAzLDOhHDyoZRw4aS1IjHEXJOVsyfE_vesyCllxttFHJ3EI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sP98shhdu0oBaQbTo_jdJCVklW7H1rV7sYv76Oggq6hALIZ7Qnu8RKvaqaexL4_N7PNFxfDoNy_BmXHggu6vFNipTnNfo_d8W0AckEtC6nYc2liAZ06oWl62d6KsqHpQEo762Z4QxHYJK9ss2ZbNq2hdUNxT5KXthE60RGyBsfnxTaX-_KuRcG7SnLt4kqooV7ELmREGMKYfG7omtvPfMwe22e2UBSb2BGUf1jKLpuerEaTPotAuo5n79YddloJ9aLx6lL3OQypXSCbqY_COWyKiFpaaM-ARGMdNoQZt_20o5c6E7YtqSO5z9tv1IDgMIiXU9xhDG92IwcvRThUqzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c1j-kGjSDWOf_fRVkfzI18xTx8GlRAKAa4QOqppw52bBw6K2L4ai3zHRoZghE9rbEdg53C4juNKgV9rlL0esyBRzx7JADrameJgf1e9xEd9wQyPi9YHV4zAkFgvM3qKg4J2dtPRb2syZ6BTxUgUx8Q5BUQe6HGIKLtPZkf5n9JguXjAec1KxbEO7Ff28B49Ahh-INJYlNdC0VbGx4apELOAms3dcAOATGLUg7Zq4RLZIo4zSMFaB9ULpcIMDx2vSsdvXbYflDHngRgIALUnY1WJ9J_M3F2pLrmfEa2bbrj034rnsgzd0RncUTg8gLENgSvWMIy9C_NcpwJtx9PJtvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dEvK7BOl7T6CHEuYbGSZiuo-WWdS_Wd-WnAgExX8HlMQ2CBomanjAHf1SvHmH0J2b55SPZvqST4r-02lq-V-WYBDNJ43R6bfd0BX-q4iFmpQUeJV1DtiK7vHOI_9cosUzalmAPv4SkkJnrQ8CYd40yAkmQFKJKBcU5TPrIe26_-C9deFCRLcr0ppAmux4hBlpxQmI7U6YjE35nQfBgB-JE77InF4L91Qe72M5a3hGTr6UeLHzUVzQOSQ8ucnAePjIBsRQPIUZg14QlADxWohpkWRhz7oOwOne8XFxDzm3He6etRcbHWkzIBIPsIOBlHIQJj9FuzZ1wLguPpNTarf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fIoNV-B5oC3D6zVh_zQdxG9-tkm6uRu2A4TpiLqETNeVyxTG8KLPRvSSqeYEANbotYkaP5TxO_8rvkwyd3MhP8L_oHwVe5DvCvrHvykzIRCC88lZ-MN64kYLCPnSS4gd0AlV_aOff4c1FMsSaI5X7GWh96PGTY1tU_Y6OqdpiZqikqUQOgjbP1cZVXl_Hj6XLmg-KKfSjChLEECojEE7Wq7koPNMOYEx6oPtpYwMzUm2XVJaGknP99EuenmvMAcNLjK6UHiP1YuljcgihjXP4y5Sri-AHLU5Hs77-YJXl_gGBtGNuLR5C73fLx8wqnQ3ZHjjUZnE80pK4mAHoiAUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OA0maPFl-LlS-m9x3ZtL57lFIMi6yfWpD5FNK69oNbHJi1qzJ-p64Cg0BBITkIqotak4INtQ9AAxviyV2Xb3YycnCPWvuT1BDLGIwUm62HY2pJHcIks6zvJpIQ3PH_4MaPSWfcidGIs-TyxMK1LZ7oEqqpl7gDMY6Mv3Q50r3rOznajWCu5pqgDMzLjRrcJazsRrLyh8kttgLRTR4OulPX8fqAzP3f-vVgeTu0DDfbC8Pu-F5rwkQ-NwPoT_zEoPPeqglXyqq0riBIKaLFpv1xxAlI8vKwpPN4RDinxVZnbvGy_s2zfc1I68b4NLkDups-38Wcs23dujMoMas54wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QDSbgZ8fBH_uehoFFP7aNqIiP8BOdPVPDC4o1WteC88LRs5VCKtGNd_xBJZYGCy-HSromtlHL4KFMdSrWNbKj0802dn48-t59VNgYbLMDO1UhJvYB0_kFvRTw8Uy3yrDn_z3kooRjR5EgnyqOV1h-d0OR5Iq4wB5k_ml4Y290RBRoAsWCI4T-5QB6tsUuFZWVh3SUauc3GdsrpkHeZ5auPN-3LRsogVGfA82URI5Jm0mkBEGFpiJ0qRjIdDoM-szo10rK9fJ0v3YEwoxJTTiAAHI_gAEFKNxudE7NCC462mQKp9DmUgBAPO-hFLG-hQrQzFEZVza89e3LaaF26iqOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_IOZ5WP9rwGpDR0nE2Gmsw1AsDS9bgnSgEnVzSj0AmlLm9acR5YUa_hz2qXhZBghlPxz0VIeZuZfz0tFACvHQxIu9XHq98cFX4DHK127ts8swuQ4Yl5-vOD7h1jTowz8QpilMxTktZaRIBe-_lWivZgEIoUiePEnC_V4RD3pv6Tk_kNVxxXbcjL3_la3jUcXRyr_uzZ1kmZs0VnQCyyxFtuIgDxYsnVbS2E4A2gWuCHZZr-2CzZOItdiUd3lkOd96m8j5wtDdOH5BudlRgUUzNVkYhTVSEWqED4CM6s5sZuu9qEF-_QgwxVbDmys0O1N7ml3FzViMJLMtKYbYHlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RlaDRTfczAIRYF8wfIfHnHjeIH8DWLklKnREJQrWQB-LkOnLQFmcYS30zBFcPoaQLlP2Y2npMrdPvYxcHGDEhiRE0fPMwCaA_niNBQYrzGpX9xug0l76pghuqWMrE-SGAhjhANNVV-8TWd3rGtxSg0E7thzre511opk8wgMlCic1EEI5iDP61oEB0bzP70YvR5SkHe9s13Zb2LJZ6ux2dGohX4z00pKCmRHcRiylsqrYKrEZ8_nfXGmpPzv5dIf6QfZWTeYM12ssk3VlGTP8gHGiYvSOlc14DEaXSxn7PMxjr8F1IU5WBxiTthKxzsOx1JF-z3WzzMkv0rrANv9Azg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jbJbR3JTAyGotArCeDR6kHBWczeutOulsgtobhDg5z8EZW9XOTdx-UCKM0SXBrPIT51w-9CbsQTv_apfNKaFH9d_eApZNd76FmdX18uWdnyb7RvK5wy2aPY9KHFk7DrUmgJ_94-zYWj8SJKGCRj253SnijfmOi5MGvTCIB0f3iVcQznCj5k60BMy-00cWVWgAsNCXszbsQ3L2Wb--lDbnto-thmf5jQUZwhHiJgt20Eall8VwAf-HubP87SumIqNxgSZbNUfnrzp-53Od7c5Zog-z6MnH1w2C2lkEPF-iE5kK9cqSYq6TJNmZY-nZ_q7DkG3IHqEAtKiKgM5QnedFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_4hFW3JrM8mNX6buYbKSa6sWdXn7e5ilgClHhQQOTym1V2VQKOt49ROAViPPYGGBACezYP8O-bPUg00HAtYEnHliCVQOUZFTfkwXsWfl07gWVMukqIs9Eg2bJQhojp5LY32wmEjAbEwRNHOp7uyCfSiQVLngDFGOi0ndESh5UOr3qGvXPeh07a6ZfcA1YyZrAzPpeeSVln1PU7phPIO63YIA0WN6Z91EXAS4DtClmSU6tgUGXuP5DSrbp94agVBQOphw1XW071AYK3-JIxhIF5Y3dvWNB2sdl1TiDEqAFpbEc9v2hl_cQlkNAFKaKcu32TXfV9u894ki4LKnrI_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLddkLkedtbBR8J91ZYDW1_T5ntcamllpTnLYdd1lS3Z7-NAGXDzJa2mMp1XPvz6hGmnL_RappvV9DLa7W79DDfnxVXL32x4uTilTwTP9lqBynMvYMy1Db6oc-K2XZtcfHkrppVsQS6G8DlDM88cTKeTOFaXq9VBGgB-v2NMSacU_6pRe_-VapRsIy-jAbEzS7Ou9-cknNa5ZlVvvAhgyqDSFTQJXNsH1YFUblzyCq9Tj-MGCN9-XWL4eiwwSYVLuoKh1BDWRE2DHx7VXtuHY8LJHpqPVmHW9Xxq0fk6iRRLGzLClUENwZHyzntunLxYoSyafJhG2_pE-1VbSq2iLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HohxHc6tHUJCWJk8rleTyqognOdkI39_DpT94tP1jBKXIp8gVW_ZGN6BA7KWU9kErgjheygrG_bJUSCQS-eMHFB1OQ681XHhdOpI4HAsJMUtkhehDtVfoe8Z2GfjV3s6KIyY88EctUjr6AxaT9Ta3-aGFFsCIEGeDZZ5t05VD3PsMP7pEDLtsybCGltF4nUnySLPaOG7_Ktx1yRSo2rkBrGhtHZXH9T0Ocvf1gjMdu42D635SmlA5rrqnaG6qf0UqMsKRiYl7CLLPDr9wwBfIBuQOA0DsnfOcJFvLMKcT2_WlGm2sXzixCTjaktDcv5Jru2GLHr6woHwKrXhfQ4pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RIeBZbATdIEamjzmp7TG_q1XK4LokUowmUPQ6TEyndOzx0yK8zVXlbk6iiBf1y2psCh2KGhpBGUBYeElVlJBOdiwn4pzHIDIjrkx8FquI1PDvX96Rh7r9twAqhRL8P2U3U7wETPO0xAaBgLbuw8CpSYoF8m8CaHwxi1vd3oUlDOf1_4O-RMiO5zlznJlN_TXP0ugUQddwrF4KyAK0uqnQ_rfMsTppvJ8MXh_BjRxY0RGXpXuhFgh83cplUkO_Jk2U3f9KEqvIytOKNdVOKdSKbRGYSACnDWGM47AZ8MzqIMf88Mbj5zhSugI1AEvLdmyBoOdQpq2gqD_a5cBhEcnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sCwe2LmSsHtFTuphrba_b2ABhLsXGGiEJMxGNyUVrqk3nPQaFu0QeE8LQiRaCwY3A733yGqMMx_alZYtuMYVWs93CuDq1zxCTO249L2-vxxuVBdKhBXkzsyFjJrolrR4PUsEp9vYjXrvtEoJVvnsZpDYtCbc1V_zB14eFbEr1vZBUvb3CsGknbKczgq8YC6WMlsIZvduYpfDDYwNIZ-qM4FJvtC6yIL29PFOstm08ZcSZZUpM4Z2xOJtfiuyNUVssi2Dp4RlinNa_X94x-yhH8kAbIQPqqRFVgL4De8DcbjGXRQ2s2GpEbO3OqQGdCo09mnfZ1RCzM_yXlsHBR5K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qBDx6vdpcjljH42CTEEIKxE4LpFYAI8HECaG5ycOoGUfREdbXK062-mSukr_yAuY1DH3hykjpAnZjSuwu1S7oTi8g4B052yMobpCmJOWPnOl5SKcjx0JIEI2afhRfE4qvwiDGfYV2tvPq18Jgf01Dvcfw4SZ-IbZG6MMfIF2a_MevDQipsVu8stfhtuHUnnLPcogoltK_tfijKQdcokvrjZwIxoeyJd7tccUZ0csa8uKocK7c4wqM8L3NIAoSQZBzFNdC6GyDPocvyVtbMguRYWfjqcf8fTA5vVYdoe84mDVJym-waO5VcnLoLYRkaixYaEnRGBVHuqt4B_JGtiuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNhoAPeMnsFWnQV_pQ1VCvUYyE4YsGZmMhLVbugOpECzopUWv8dHVZDkdf7I6pAkywxr1-x9e5jF9WpOrvIVdsanjHz7UyfzFI2Kl2Kj7SAjeL4GP3cPXK49lHwbwgWCC9iS8bS8knKQGlM-67i4K-zua6iYs8Od9MX9BC2N3iNobMbYMbxEnqPvkW49wy-G4zxCrXQH7Vg1_7lYau75L0psZLaxoiAEazN9LVIVf0OP1JerWnRdF7lVx7Mrl07CEHqCJ3BxhENBvIxYbxXqRFDGAS1svP-ICoz_3z8ldw-bUrtUB90nkgb4YZYZwDxR41k6R7mZ6J-39E2v49Tkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HifwzLAptJZL3mr4DrbOwa7lfmNXQM9VtHucQ3JYaNWxfcwKB-ZIS_DEhYNYr3YbxFfkwF-HJF1sSCFHIJNVc4SxIlEZQxLMS2juAK6DF8KhHSuHnoKtZIpy8ZziYB5MQVG2zJcaOJcf7vhg7cL0RT3Gh9XM1cooidqCc4w1Ep3eRmCykHWlnE6w44vG57yp564S0mX2wehnDyRsiZ54M7f8eqRUPFocTk3xwdQWibaUMYVJ9iS708NHglH8Uoagthx0yPiodEs0U5xrsf333HW-5Oj3J1Zyff3iCPowecf_G-sWFFPbKz-CXgT2ox_kmw-eRrhEjaiOKMRy5YY95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=d3J0TXa8gDmccFE5ffWdxRkMWVk9-j_C5wimSyytV2CeEi0yJJAXkgmyFXIZbm_1WzSm8FGr9JoJaDJFBeiNz8n1r5meumZPyYM6YYQCPY9xmJ8VeKYIayF0og1uR5QTXhii-PXIgUeMY2lxE-vbYxioyKPiGu-Vc5ojFwyyaQzDCv44HIVf8f6TLKSTrxd-AYO7jQgYv_Ui0o6-KBkfMy-lVeO7-NhyCUiaoCieoJ51Y_DldtKbnLNVNtlsLl04HxWg6QrWMx6FYeXcvE2a9svBTgTmE0_SfTKwHh2xD5vvVSWdRYSFYcDEgnIna9EpifZtoqxnT8NH1NW9mzJfgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=d3J0TXa8gDmccFE5ffWdxRkMWVk9-j_C5wimSyytV2CeEi0yJJAXkgmyFXIZbm_1WzSm8FGr9JoJaDJFBeiNz8n1r5meumZPyYM6YYQCPY9xmJ8VeKYIayF0og1uR5QTXhii-PXIgUeMY2lxE-vbYxioyKPiGu-Vc5ojFwyyaQzDCv44HIVf8f6TLKSTrxd-AYO7jQgYv_Ui0o6-KBkfMy-lVeO7-NhyCUiaoCieoJ51Y_DldtKbnLNVNtlsLl04HxWg6QrWMx6FYeXcvE2a9svBTgTmE0_SfTKwHh2xD5vvVSWdRYSFYcDEgnIna9EpifZtoqxnT8NH1NW9mzJfgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ts4it4KKsubhlLDoN_FZO7Nr2GjEoPy3hZbxm9mBHFY7ix7zqeLJvEoYi_lo8Rvn5Uouee3Sq1iFMhTn2aAvD3vu23JISLnwDDeQOnydEg84NOeTwCfHgtpTdLCn7BEgZwxp6K1Z6XpEn8sy-BHLhAm8UY0cQSDOS9fe7ByDALkVxHGctNoDDfoJCA99VZQ05xQ-tyKxpEMJoHlR9MVNxFcgPpSdJUomTRxKCbzXVlQ6-v3wHyzpB274Gxb-u5QDn0AZFuxOEWsvcNNo4kAZw2k8m7J5JBgbOskazWZ2EgqX6jaCApqsKBA8WIlN37KzZUoOjiOnmjZH0eZcwFDvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/swSidVAMm2LNB4GnUucQ9Iz0jPFmw_EGYmswOV9PqUjxUl8Gv6be-OdHi3qTccT2LepeD4KRK-PpzKsBSWsTJiNqaQjZ_Hfi4BI351ETtwPHepclmzWxBlOELemkp2rRRUXSSjq72l6wU5xXv_VFgYdKnMej1IRIvun48PJYSt1lmCfp7p2GEqaKJDaT0K8Ok04FRIKiPmiW4WjrhUzqW4T9tBxSHuidNC3liI1CRKA4UxYiSRNqGI2SIiqXdPjtoq04WjfE5EIs8Em5y3QQEGr9dcd7S4qdHLgzGVqcnfVo8cjfBD6cqZx2yZEug95ZBAo7lUzcyrWRxgGfoXnWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AacLt_Z-77A3LTS8YvI1fPreQEfzvNYruHM4DoA6IBqMGBT7no6lEpxi33nxx9BnMHaMlpc_Fg2U4iSupFXJevivbK8-vHuKU72B88xObRrNYbgtWLBRGCcnQrlY9uu1eZcVZsb-WsWY_ZjioZ8Bn003bSNFn35ynA4HkQEq1Bktof3y79GEZ3Tnjz0lVDd6IqoFDjdbrvawgJF2PUfvnMNSwPmqzZzftIJPNERbv38juuVonDhNCrPVIT4KKm_Po77O1CjaAWOeEG7MmwEPYHg-kdffKensULpezJdszL7rqjT-Dl9SLqFbC872sqJaAujyMIhIpFljft8KliBjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=ai0j7z5om478lZ7wcPZwuMzB7p-dh0vvrbQQGZHEhSaI_xCEHSW5NmXGbagHZla7tiEMWYQX1wwUeGrKlUqUgz89--Ri8IZLz0LaEb2-S-6DH0dkQJF1iuEP73ALr07W5p3s6Vq64foICHfn-8q_w3q4TWyRTlGo0ubmouKKo2gDczAVeLrHGo5DM-EMFkQpWUIInSD4yC2Gk9yy2d5QJPW8fHLS9hXaIk-8doQBscNnNB_Ir-bFmQwU6Ci2w9hwrFxwbaO1Jg67QzAluS07ccxg6dFtdUPbsHDlWU7FEWox5ntAYsEn2aU5faV6N_4dWUCwrZLeRMsYV-zZU-V0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=ai0j7z5om478lZ7wcPZwuMzB7p-dh0vvrbQQGZHEhSaI_xCEHSW5NmXGbagHZla7tiEMWYQX1wwUeGrKlUqUgz89--Ri8IZLz0LaEb2-S-6DH0dkQJF1iuEP73ALr07W5p3s6Vq64foICHfn-8q_w3q4TWyRTlGo0ubmouKKo2gDczAVeLrHGo5DM-EMFkQpWUIInSD4yC2Gk9yy2d5QJPW8fHLS9hXaIk-8doQBscNnNB_Ir-bFmQwU6Ci2w9hwrFxwbaO1Jg67QzAluS07ccxg6dFtdUPbsHDlWU7FEWox5ntAYsEn2aU5faV6N_4dWUCwrZLeRMsYV-zZU-V0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBujk2XLFKdbFohVojz7ghmrbxurX7NjihT7SS25fSgCmnGgjdDJ1CyRVMGVLP5RhkqoRfCLEtPJOoblPuEJOXxEgq6gQQK0Bx7nXTudC8xIyL7rktYa1-6ZJlMixORsyoQhCM9Z2XAGd7qJKv-afKKY7iAw0i2p6_FmJgxQvujuZZt7s4CHjnk_cPb1A5T9TUBJZQ4XrPe0nvDXDfu_ZCKg1YiBspDILSKhgqpeDDafNVv7ksp3-KV88aRs3pOWdge-DBmCELGgLvdnIvvov3TZMzYzkbsj4JV3h3mumceNw0NRKCZsn1Ppl9ORxCxoTfzzhXIpZzplcq819TEe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6s58OHVJq80bzM5jkAL17A2-lrrsrQ35_T6ofPw6qgexJgdgR7RnbhD-OlglmbnQhmUxHMDjwR3OhGr0MTQvXMcskRgqh2xJiUUelSnBm4zQ07fHfHkQzseLTzo_K5P_zfEGJ2PdKPa540QqUF_ZAayVEgHeP30Ev_u1UIEXqZFdhm3RvF2xC07F3kmMNwBznb_-W2GiJC-W8_R9opZl38u1jO5w8BBUuA01JT3-KAOlIZhLP7MXeUGSDA6BZU3jREtBh-7z0UVnCJ4PeChsXWoWpcVNbSsE-PnEO9m0nDqSlJm6dbhxSXQxBNsR4ZWzt6cQJuBnG2DyD-1667WUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f1hpvU3N1JJnnYMmequGDro9drVY_YexxYRTQEvJhVtkvz5L4G9d7uzBEOJHUk4TD53C-d2ELv5KyI69CG6ajnF4378n7VFXw4-0kkDd0s0jvvJ0Ptfbju8F9V89k6p2xnx1kUJVW4h0nHGP5DsDFhGT5AGSnPdOc4iKil1ijT6SBs9DfEKknxaW53wAxamLvL3LAm2lZdjFt9dM_GVQ4MSH0NYvXvi7quWmmAkj4KRIAa-va-EnvH9Q1GIAhwFLUVJkODc9DHVs_WSI1L_l6iBUSjUkjY7kEnBZss0xyDq_9mbqVAtNVMmAAofSaoIti6zggCN-k2_0A_zPZg3-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gFT6TJdqbP0GUpBj_do4PtzUIj6ph8ptsWF9cmFuMTzzphRrz3mtZBT3ODpzS2lZMQEkZfrF-gI6Y1w80LtUMwY-KkA6bpyGYSjse95_GqeMkqZuFw92plytAYh76Ghm2rkowyJhywN75zOQC883lhc5yqADy7KRua1jEGuiFDCMFBW0VlSj8jWF7K5R8rvM-tbdBYIkOXRGDRkLGXnSoja3iUWaggS-13fdSidsMglaMsmKckk2Aomx7EFssuLHMfGg35ba7Z86LpIKy054A-0F1uzq2RbaYInmkB2W0093TtyjfR8-b_H5KBmqnTBUKibNjv0s16a4xdMYZmI1cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVy7wvWIj-u6WpgaTCoXOqA2-56Luz7Es1rNAmOCRy-FIQvaICwF1hvsD0lM7Dg6xKAKb9naMyE5M2kp3xYm4TJnawX7GXkt01RhiGv9SRJ8K3fZ110DZYsfXRI2QOyMyNbfHkaWOG869x569F7k0S1p7jEq7JbnES2IM2OSzMxsGefDLIp3tELUbnh6WaTH6328tZzHfz0jPorkA_9IsuCY3MY3ccoP4T6YRazNMLzKznLtpMebcaIVEPysNHq8Ci7VL2nFVuNyIespzRDscGd2Fx4y-n71XFQ2l5OCQi_hShy-Jb4Y8h5ATWoM6XyCl3fZ27YAqWvSzNaypXtsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XhNfiYyfc2oqpegBa5BGuTQgo1RZalF3_j6GnkwH_5xd6klBHkiMdA1zxjDlrAIfTDi1FFG6ga2VINSO9OOKPrvYDZSgI2EkJIRCE62F8W-niReC5wOU1Fw8w2JHCarpZsAcQINCPARtyPB6yJhOvBKh80wLKVOZaD9sdVaSxtMZtn6okSj8DkyKBxJqmNqrWm7s3VDj2hXvHKtcLn4k6IQhecV81k-KEg9uyfKNliT8HURiySo_mpwQNSk0VmJ0dZeKkoOj1Kry_AAG6knNb90C8Kp6TSaJmf47j7mF7y4QvE2jZ8HDKtxYIPNMHigcfh1s6BCqbDxkLCR1g1Y-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=h6ZewGVA9RCBziPG5TqwNk7IxGbAwfh5YIx20ySCUZkvi_XZjPic7-DfN5DJBLCj__U7KCrGo0rMB6SLvInx3DXa-MJ3V6eFG0DBalUg6zHqS4fNAJYTFZaGCB9YFj4lLOFjFu1una4O5DWXWKfYGajaBZSOsg2rqLRTi6SevOSfNXw8AA2Ao8TA-SUtayKCnOKIuVeenIhCUFk85hNb2PBic7zUr5lWHA7_McYpW6tJLyRJ6qT_Jv8jlGGZkDOqmWJ2QFwbjkST6xz44C21WeY_E0HUZwMY9w76VQT3xuMTzQo1JpLRiZAZ27w0a32yIpCnB0-BbAPYQXwXCd-zpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=h6ZewGVA9RCBziPG5TqwNk7IxGbAwfh5YIx20ySCUZkvi_XZjPic7-DfN5DJBLCj__U7KCrGo0rMB6SLvInx3DXa-MJ3V6eFG0DBalUg6zHqS4fNAJYTFZaGCB9YFj4lLOFjFu1una4O5DWXWKfYGajaBZSOsg2rqLRTi6SevOSfNXw8AA2Ao8TA-SUtayKCnOKIuVeenIhCUFk85hNb2PBic7zUr5lWHA7_McYpW6tJLyRJ6qT_Jv8jlGGZkDOqmWJ2QFwbjkST6xz44C21WeY_E0HUZwMY9w76VQT3xuMTzQo1JpLRiZAZ27w0a32yIpCnB0-BbAPYQXwXCd-zpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHQyrAp0h7SxNnANXETu6znOhCRDEKje0AVrYqo7NqVKx0KFKZDQ64BjfOLOQM1SdOmC_jmRu1fEDCFD8eRRBglPDK9fs4aNwCpdVpKu2aQXP27DCgLDE3rE95HbzeiT8-jtRGtkyMJPHT2AULqbIQ-UeB4S7ae0MHamtyahK-iwZTj8NHigV0kUCi8E0iWuFmF2uWCMjPMSL1r7ladYo1HmpqIqdOLa0drNbSJYwPSTqZa2YXq8wKt4ySOeNnOz84LQHpJjFymKWqGB9DIJkNxYXf_z_WI8L5SH2yb0a1Bb4ckJkgNpYv-HoU_L_kW45x8dmg5-MDC4Tcmz1FY1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u17KEYO-W_HnKESWuICxhb5DSRUERNN7fTzjVisgZpHssTwbwjaatY4plt68vpiS4WcHcuuK2rtjaHWxM7oc0CxoIGA5klnnRbH22OmzbobDnSCb5GxsgnYHpzyqdHSjL5WgkQUJGqTIDo8HHlDSz6wYNxWyMehb-w2fJqNMrzFVZ_vgk8bJz3qToS4ejF_9BLi72HlmXqH6YbHmsltLkE8goSakKNnvBk7iruirfpIG4M5ioggkhQUZIjD7wGLZRTOKFyPcy1k5_4Pz7ZKK8JuFwc2M2EH5m1vhtyeT6jmg4u_0VD5e4e1OVsC3r0abtsqCf0Gs61bNFHXfUkrZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BXtzjQTIACjF-XT1hjkIliDZejOyg3DoMOOJyMGm-NqWIsxFZn66aTeU0ghTi484xdmlChTkLB3iXb49mi-LFT8x2ETduB-gdumILmFTyM5-ffrL7rKQCFv_n7MOt9J92iLATpYpgVc_ERtJ7nMxKgQVf-N-7R7zZmiSeFK6YdGnseQn3b2qUWkhomiiVTCqN-7ex7TiYB4UpQml3Z4l6eEqACfrfvDSaK7e-FQfN98ePoCcwJAU1WArhuHnXQY6959fHIFzI0Tb2IOwr1JUxawML23Xzx6FusWuug-2OcviVZHa1KTECyMaqiIcxjiGttnUTYk0-11E-sMY2K_3hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPWeSs_jcEaNaUrWQMg3hZxxk6X8k20PFfC7X0g8fU_TWQMElS9Q-p9goOiU-h75G4ZxhIeGNbCv4VFFeukpWNPo3q-bQd2CYtP47DlA4K2_nQnJzOwauU7LRS2OoupcgVcarlgqARvmyeQabxzVx3hbdb8ARlWBlFMhrha7RW9-v-Q0DoERF6ZrkzrzY37sMyt6erg2QnaPktiFVNpAtBEpTWVDeURNx5a7M02XZSBzja_Bn0nNURf1JumapfcBQIpMMqvNrwNOW0gOqhkZjl6Zc4p-dd8cGBSP88eE_w9Rji4cEFtAo3oqT39xODabuMF6BQPi7Mld5WcBTx_x4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfTIkjSKgyhkeY09pgtFuFIcyfmrBT-gucoPICsWgGwN6eh9p3CmTlOjviKFHoJBAEUv1WhnnLF4C4JGNPz7AWlMJJmSS_GteoOAuUea-5XlxRj_AjRmB9UYI7eGp5P43fr9e9RVLki4qYaLCBZ3ylVRHcHfLqoYPCs3gRjBhx6FD4hi0WI1AJE0052AeqFk62a_QFXnXU8rUzdgTtKYQfaEudnnNXMqWrFKxciL937IpT76w7hLidkCNcyT7xB9dsxR6F-5N-jBduToGvhjNFTdqYeBYb3SWktY4i19mKnCZgPk1hblCRB1DUGy91B4_-o8C19ez5-NCgmhOi4sUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KgIDtauzc94DDWTEbb69d_p5chvah1zePQkKRi9VSLkDXszhYQ93TK0Y8S-3hkBeNjgxu8PMFJZdrG3oNa-253Tzx38HAKFT3Yle2Q5HkNMaYaBGtrrNqrifW1g5RqBLJJxejtK0bb2WJ8DpVA0YYQ-c1HXD3fu9qPwbRxlOpqneB0bhnIJppr5ci-kLKw-QfIXZpaGzq9tgbDRGRiawwdGXhUC3SyrW7k4WvfU2It5W4SesjJsETwmWvGDUpfQw5e8wAK77zOuzYTLuQ5p65tKke3rNq3kGMAHXVRXpKXMH40fQ0-UvB13EdQ5XxuihpmEj3QnzOfqgHdIkRfG1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hyf6EQDIqJ7iJ7I8Mm4-6yrcv0nRehdxJa-F8nDYZYwqDSZ9tb-V3eKVw6OM8KTCxLJ0BBYp_C1tB728F_zfbuzxZOKZWD2GC3o6fEUNs4Yj1qmXdQOGY3brhCcXaoIJ2T5srjXrs6lBfBxDg4KCAOmSGOlKAv0a6t_Kw_ehEV5vKrMXUKmkq4n428JfHTFsLhw4PwWxz7qvbRkCDCJlaegB1ZSplaaHuS9TjTdt5T_ElY7h7uDq7xxhkDxTxPaGlgHAxnrkvuUQIT6Y_IuZgBVTaGU-w3XziHD6979KvKW50RSES3a8oT9kQ7-F7M85p8GMuC4ZU8_f0gzvO49ulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QehoARqosTSollWlBJg4QjFSwrt69j2_5mpSlLo1RRb_5nVJPkhJK6DZrQPmCuEs8GN0hzwNR9eWErV0YLT5PiyoROL44fQWK7y2gY9BZzsfxEonE0x3EEsJyOQa9I9BXpifU5eoTHOMtGWYguh_fGzfVvvcaMpax1NdhUFMJ4CsddsGzCCuHcRWD9t-gZTpU_QJ8FhKidZ7hYx5R9WlLG0g9yrmgW3DZgLBu1uu2PDgrRGWjsiYhbxuTNJK77kSoPWTXX9acneqBGckMz55yI4FcwSdqcmuMS_U1WtiBa_WHiagj4njpMWCxIl-mUpGKppkiesg8QkBb9Y2Cw4rYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=aVegX1Phem2sw2gq4OEcORItFJxaDAvNIRY7QLhf4KcBGlnsLGGnZ6O90QdXinxuZYaZRp6s8JKkedDaX7s7cJF4x-RVb8q0TQmEej9qCmqcitbQrUyr65mWQTLHNKY1bcuJqJl_1i3CSHxvy9Hv2N-uALcL_K42GhC8d8qJg5RExOefSZHzWkSkUFbNAFXzZ8v6yA_vxswEWUxRYN_DJESdjrp0yifBX4sOCCJYE_js5pyvTKC-UWXcK1_oGY-1TqjuY5Fm0nGCj8hGrwk-kWIGUShzLGxYQyz2yyOuPRxqAQ3BcSBMHJiRJCqqneg1KwMJ6EMXOVYRNoaC9uhqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=aVegX1Phem2sw2gq4OEcORItFJxaDAvNIRY7QLhf4KcBGlnsLGGnZ6O90QdXinxuZYaZRp6s8JKkedDaX7s7cJF4x-RVb8q0TQmEej9qCmqcitbQrUyr65mWQTLHNKY1bcuJqJl_1i3CSHxvy9Hv2N-uALcL_K42GhC8d8qJg5RExOefSZHzWkSkUFbNAFXzZ8v6yA_vxswEWUxRYN_DJESdjrp0yifBX4sOCCJYE_js5pyvTKC-UWXcK1_oGY-1TqjuY5Fm0nGCj8hGrwk-kWIGUShzLGxYQyz2yyOuPRxqAQ3BcSBMHJiRJCqqneg1KwMJ6EMXOVYRNoaC9uhqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D2_1zhwK5EhnAeqy71z9BiXCwqCnIXnqH_sn8iLbozt5pr9yxqPPza_Ev-kj4K5loy8XiS_v3q9U33vNF5SJaIHxug6mn64K5ZVvOd7nDEfNDitYdy4zvTTH20zTXZOjxW1Y1JGE7L9BtfcQSV3e18XwLWsrAgw95MoIm4rBsvjjf2SM7HE2n_EELWSRVSsXbeg8ivE9925uO9hEQi_rxf3Io2dshWgutlpilo22oR8nxVJ38UMvj_8XnlmyHpbNZYtN30nnQPuACWq4xYY1jy11qJ-dYn09TZO0Jh_6N5SY0d1Q7CMIZEBpiR91qwkjKyeriMYX8bKMlW6vNOFB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mLeXGKGW8pSaslgZj0Rueb_0mR4d8ERT6BGOcd15R9wiHB-yYm8D11jLLvPv1IA3-mCLc-RiHBkSpk-RS-_SxUm72MF2WlnpZBk3Vvb4fzuTvOtjX77xPFN8adVlIFpKxWlDa-AieKZRcmMWK4stZ2ZAGBzZL91WyidC0rp3Y6-gUgXPmnOffTreNrhQ6DfplbvIu2kS3iOMtYLGvT_wmJop6QAzLihzQgWgTLbFYa83u6apu-Q7TQ2u7X_iXI6DcnhFyYAfNoJyEV7h7yL0RZprKBKDikYipnnoJBJ7DC-kEB0FNRDiC0mLiK__MJ9AKikDd4oWkreGFeweU_XlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVvZHL10xah1F3Nwzd6oEwy2pD92PKmYLM-_SJtt8yoKz4Y5IDZ2JJHDoO_xEWcCOXt57aAAEvsSnPeuJk8RCPD2xNGGT1hXCTGPgn7SHkzClVz7w5ktvX38G5tD2e_5u-a0clfe10ZyrhBE2ybJCYv7Dxsmy5eiIcoo6lCAlV9_E3-3fAMuH7lFe858TRv7hbRdRdny9NZQaLlKZ1DK1mUV4-WeRxD7dTcsnZXv8IpWc7sWdWFBtWr2EkSlQesWOA6TVj6eb3t1_qvzU_9fYDjQq3OaLo23zohcFRbW7bCsraeiyDvYpGWiaoiHeStIgPro16hx9-5BICj-6VGHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k79636ipACxQ7vgMpJ4eNzTOX9vznFjywy6Lx1yJrCn7hzgrr4gLhRtdompuJKNwnxrHZBlixQG737vwv2_RM7h0ykIN0HUa0depDUTpOFuuMR_HRBdctOofK-NY5ygS-OX_-dDe2UmYeRJ-HciqdbOrov_RhZfc6R025dVMreewv9jvZa93s7udyT828XzvwRnJSiuBGIHqCYy1h5Wu_pfvch6AZZo1wMISr3QMQtZ8tbblWm9rJtWwzdPmDCO63YjlWwFip5IBpkcNxw9lCid3DIZF6SfuX6h7gcKj5LTk8gpinA1ToDnkuae0JzYO6nDuTcCwg6qYhCSE4JPpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtjZXoLtZgsTorx_rb0LXP7ltD2XtH1qTWNFLPkimf-PIIPTE3YLkYExR-ZLTGlShqGwUWtlJgqVrtBugG6FN4I9BjtAmFCVRN0fnTr8xYfYQxa_Pi9k4QzX58fP5lomrVI9WYxp7iRX77q9dImQHKWwBFfDH8DKMZQH8VFI1VTd26tddBu3Uur0pZvIGEqOZfDgAurJZ2B_S7_3IE0xyUfNU-GG-iLI-GgSFzfrv1yv0tELMe8NPO3BMm5XheSGAPxKwz9wmfql0j8434BE0nGZUYZk5VctwT5FcJm0RhCm00NodnQFKtK2aM3JL_YugId-D9uBOQeCHUixIPMtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ofIX33i77Y0C1XPdPlOYyNWi04HxGUopQ3lNqZNkSyE32h_MMAUP9hkM5JwNPtK17Erbnb8ihvbJHFPEppO_ihnoQ1UO2BbsvhIOtil5UE_8pL_V7f4ZY-gtkNtYdWOKubnXYuniaijv8HxvJNSZ_gKarMmiMbYolJGPRwrWAVgIdwMiS_DB5VfOpf5s-vULCjXSlCpbv-3wesnP8hVvLyr9h-KFPXR_NZKkT_Fy60lifJ5MocN1UOPORy-kjjdOBoY0KRip_WnsJPTa0QSsXloAVhuVBCL894rzguiwMEpgcVqRNAHSFNAT-OtISOxai_0ugMc1FDf5WD9_WkpXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b0eEXdKG33oAtOC7LNdUrgXdVKmDy3OOLNvJMlp_aUFqclRICqHSOIr4mGpx5Mre_Jqr_sut7HxSnb6G9lCm_kNmnaNi2gNk6o6FwJl6S9COWad52MJ93R0NCDEDHj_YWFlbgqLlNoIy-OSouPcMq4ssmlwdQ_gOLfdHd087gV5dDHAP9tVwo9LFa5YCei6vlI4mUjWkhJhOpdeo8PWteLiJrkxF7hhvpy-lnnntjeVdEJjsOk1rH4kw5jU7HghywEbA5rg8s5Ea6IoGv3ofuoWlOCDpw__YVoL_x2tYE_1ATOinSW7FB2dSvYiPYYL3xg-VwOTfw-gYZBtG6knefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
