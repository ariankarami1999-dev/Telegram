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
<img src="https://cdn4.telesco.pe/file/PfPTM9mKw1PJwmlnjabEUJ3Woe7WhauD6RB0LZEj1x04yxHEYV8gaTvQaZKcoKiBb8zgwsKWsABJdY1Q9JhpWsY5sKTaPhRRDPGOX82EItCkcuIMxGwlxqvWyXbGFYIpGUWTeDndnBJh4T-wHG0MZog7-_IFaHhK7t9BpwPPVP-zt5EMYpZleR7R_5bpHEl-oYZsW7aT0TKpPReymiR72unVY5t-H1C4c26yNlDxcD3CT8-J5bJ49TvFZXQbU7R8Cv1B62QJhl74vFPDWqiG6j5F7vh6d5jAaP7Q6WqpbfxDSibLZFZkj7jJUyBq5iSriXsPoUenZEuOzcZ3x7Rcpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-91766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4fab36c4.mp4?token=o88yzatncC47RprHxVLQsJ3oSoPvpz1txR6FOjTnMHcRPFTao7mF6D7jqIitRtOVnWIw-_Ir2tSZk_HVthAe_dpzuj7AvJnH4O_G5h8G44_BHqPKX4NS64t-GLX0YJoh7xiqJFNe2RcYFUhyQg-FNX90J02B8Y1PXirGAJZDKapjlTW3WMYVkF8C5l5EcguBEDd_AqygLfmI0-6DtHB42Yob2M5pGe0FwWPe9ET0nX7ew9Nc1_zs4W60d7mmI8WMowsIwP01B-LLVVCtSqonNadQeWzga5tGPhGPP5kPvZhAIVb-1YgbK1Hp-kM5-gF_kGshuZVLehFpRknDp-zvui7AZ9Yw-QptOfyMwTMC3ilsd16zwS7Vhiq6-LsM4VxHk51iH9ei88y3NaxL1A-4dCavg9BBCkqx2vuSkQiv7N-k0d3qLTF-V_dI224lT5oKiH6eU4fejzgIDW0WeKPQhW16fdfJc2MqWZu6coaTVQj-KTj-6jV-DXTX2_ISohghzxwWKYFi1_gIczujrn6o0AHJilCR05FUUpQK6q9NO8aMJmDL8rvkbZ34AwTqq1U5KJXLkzHCMKiyBuwp97QTmKTrtpNKMsa0JnNRBt9803DDkHdvkEqcrWqV_jKqxfax9oM6cvci8NTwEYzm2AvxL4vTOemuF0B0HnJPKXI1VI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4fab36c4.mp4?token=o88yzatncC47RprHxVLQsJ3oSoPvpz1txR6FOjTnMHcRPFTao7mF6D7jqIitRtOVnWIw-_Ir2tSZk_HVthAe_dpzuj7AvJnH4O_G5h8G44_BHqPKX4NS64t-GLX0YJoh7xiqJFNe2RcYFUhyQg-FNX90J02B8Y1PXirGAJZDKapjlTW3WMYVkF8C5l5EcguBEDd_AqygLfmI0-6DtHB42Yob2M5pGe0FwWPe9ET0nX7ew9Nc1_zs4W60d7mmI8WMowsIwP01B-LLVVCtSqonNadQeWzga5tGPhGPP5kPvZhAIVb-1YgbK1Hp-kM5-gF_kGshuZVLehFpRknDp-zvui7AZ9Yw-QptOfyMwTMC3ilsd16zwS7Vhiq6-LsM4VxHk51iH9ei88y3NaxL1A-4dCavg9BBCkqx2vuSkQiv7N-k0d3qLTF-V_dI224lT5oKiH6eU4fejzgIDW0WeKPQhW16fdfJc2MqWZu6coaTVQj-KTj-6jV-DXTX2_ISohghzxwWKYFi1_gIczujrn6o0AHJilCR05FUUpQK6q9NO8aMJmDL8rvkbZ34AwTqq1U5KJXLkzHCMKiyBuwp97QTmKTrtpNKMsa0JnNRBt9803DDkHdvkEqcrWqV_jKqxfax9oM6cvci8NTwEYzm2AvxL4vTOemuF0B0HnJPKXI1VI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
ترامب:
أصبح النفط الآن أقل تكلفة مما كان عليه في عهد إدارة بايدن.</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/naya_foriraq/91766" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
اليوم الأحد بتاريخ 27 سبتمبر 2026م وعند الساعة (11:00 صباحا) اتجه تشكيل حربي سعودي نوع "F15" من قاعدة خميس مشيط باتجاه محافظة تعز وشن غارتين على سوق تعز في مفرق ماوية عند الساعة (11:29صباحا) مرتكبا جريمة نكراء بحق المدنيين خلفت قرابة الــ50 ما بين شهيد وجريح كحصيلة أولية، ثم غادر أجواء تعز في تمام الساعة (11:37صباحا) متوجها إلى محافظة الجوف وشن أربع غارات على مديرية خب والشعب، ثم غادر محافظة الجوف عائدا إلى قاعدة خميس مشيط في السعودية عند الساعة (14:00).
إن هذه الدماء التي سُفكت ظلماً وعدواناً في سوق ماوية بمحافظة تعز ستكون عواقبها على المجرم السعودي وخيمة بإذن الله وقوته وما النصر إلا من عند الله.</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/naya_foriraq/91765" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91764">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
‏أجلت الشرطة منازل بالقرب من قاعدة فيرفورد الجوية التابعة لسلاح الجو الملكي البريطاني، وهي قاعدة جوية أمريكية في إنجلترا، وألقت القبض على عدد من الرجال للاشتباه في ارتكابهم جرائم تتعلق بالمتفجرات. وتستخدم القوات الأمريكية هذه القاعدة خلال الحرب مع إيران.</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/naya_foriraq/91764" target="_blank">📅 16:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نظام الجولاني يطلق سراح (59) سائقاً عراقياً</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/naya_foriraq/91763" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91762">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
إسقاط طائرة استطلاع مسلح نوع "كاريال" تابعة للعدو السعودي وذلك أثناء قيامها بأعمال عدائية في أجواء منطقة الطينة بمحافظة حجة، وتم إسقاطها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/91762" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91760">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c2d4b5e.mp4?token=Gh2k5ZdCdgFY4DNMDBPFF7nRUGeMufMBuQMII1UeUg5mrfUzSjfL82z5dRN0iRMpNfOJopTfGkB3ItrocAIHc71U1FWML6XF3xU081kMHclw3mOHaxp0ssZ9tT7zMpg8Tg2BCA0TSIMKYGJVFJLZmHx8UKwfqFKIb8l-OiDayyxsyDrscWAizAhGW9qBQqLKQSBsHlHk8IdqzJplkeW2Z9w5JNz98WOzPkLtFf5jEbxoOYjFl_-TR7Z_py8t-aWF5EKk0rwSl04ZrK2OR-f9gQsvk33FYqkwTk5hXO5oFHNxzybioGRzmtPbVWXpIZSMMBip-X4p3bE3KuVD5mo1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c2d4b5e.mp4?token=Gh2k5ZdCdgFY4DNMDBPFF7nRUGeMufMBuQMII1UeUg5mrfUzSjfL82z5dRN0iRMpNfOJopTfGkB3ItrocAIHc71U1FWML6XF3xU081kMHclw3mOHaxp0ssZ9tT7zMpg8Tg2BCA0TSIMKYGJVFJLZmHx8UKwfqFKIb8l-OiDayyxsyDrscWAizAhGW9qBQqLKQSBsHlHk8IdqzJplkeW2Z9w5JNz98WOzPkLtFf5jEbxoOYjFl_-TR7Z_py8t-aWF5EKk0rwSl04ZrK2OR-f9gQsvk33FYqkwTk5hXO5oFHNxzybioGRzmtPbVWXpIZSMMBip-X4p3bE3KuVD5mo1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارة الدفاع الافغانية:
عشرات المسلحين عبروا خط ديورند يوم أمس في منطقة كامديش بدعم باكستاني لكن قواتنا أحبطت الهجوم.</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/91760" target="_blank">📅 14:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91759">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaRsMtbO-pz7DtQvASNUrHqbd72AhyFpA3d_9peDliy158W2zA4fOmXo_57W_xdtjarIyK1_ipyZBPmKEMqosSE96qCSY-tfr9fnx5njWVfQ0OqxD4A6NtHORCuhQNImCe4ecporU3Aev29n6ASeKYSe3jhWSi7qSmR3E81_GiCHrHki7M0YdBa2Yyro4tfj-nu9po4mn6Cy52UWZTChKMEayV61THQq31Xk03UY1sGY210v3z01-znFnSYihwebt_E27Fz7vKhNLH6lBQmUGDkCyy-nAIzJuFPd6rsOjnDFAp9A4SPDQkalt3BYj9V0UF26wkion4bQXuQ3YskGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
السعودية تقرر تعليق الدراسة الحضورية في الرياض وتحويلها الى دراسة عن بعد بسبب هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/naya_foriraq/91759" target="_blank">📅 14:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91758">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مسرور البرزاني معلقا على الانسحاب الامريكي: نحن ضعفاء، ونتعرض للهجوم.. وأن تُترك الان وحدك دون اي نظام دفاعي مناسب، دعنا نقول، انه امر مخجل</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/91758" target="_blank">📅 14:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91757">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسرور البرزاني معلقا على الانسحاب الامريكي: نحن ضعفاء، ونتعرض للهجوم.. وأن تُترك الان وحدك دون اي نظام دفاعي مناسب، دعنا نقول، انه امر مخجل</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/91757" target="_blank">📅 14:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91756">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مشاهد للغواصة الأمريكية التي استولت عليها القوات البحرية التابعة للحرس الثوري في مضيق هرمز.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/91756" target="_blank">📅 14:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91755">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
🇺🇸
الحرس الثوري يستولي على الغواصة الثانية التابعة للجيش الإرهابي الأمريكي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/naya_foriraq/91755" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91754">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/91754" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91753">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/91753" target="_blank">📅 14:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91752">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4EeRuOE45dgiigV8V-We7eW2VUE-OW62CfX2hQjfM3LUdu145cEFqcFcrHXXbLcYSk59OHGwnMzeowt0f7kvpj17zefg7gB4CcfyjnfZlm4Mp2Wdxi8NqIIqC_zYpDMubDXUN5u85f3mabNsZ2XxcsWWppgWmk67vikHSamn7Fatsrd-9UALGmLqPeSTOSZR4MTKkwhsHpkyTKjUEMQR2nrdpNXukXaQ8VRjEo-Vtjk7hU8FfULJ_eGpZVgDAYo7VDD4gviSB_ggJNU5QNfr-VX5zOKjbZNwDbqP-kYqXmKPLa0zGrc0MShQgLL0vMVrUjTYj4ejoGNBsJEA56Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جماهير النجف الاشرف تدعو لوقفة احتجاجية عند باب دخول مطار النجف الاشرف الدولي يوم غد عند الساعة الخامسة عصرا لاستنكار قرار منع هبوط الطائرات الايرانية في العراق.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/91752" target="_blank">📅 13:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91751">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
تبادلنا معلومات مع الجانب الالماني احبطت مخطط إرهابي في مدينة هامبورغ.
‏زودنا إسبانيا بأدلة أدت لتوقيف إرهابيين اثنين.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/91751" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91749">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAveeC3icZ_SUj208TkiUd-N829rZprlbrwHMGo1sxu0tgbpwaxy8PLvU8xJiH0Jq4936AMJblJ0KndzTZ9Y-ivJi6I8TNng8oPY-qPdXZrn7lHd4e9n1mZ8vH_--pdbxGy-hkf1i5IQqlwfbbY8WZy8j4drW8Z84E2RQ1OCH63CTyQaHgj_PsRVKT7IgeDJCn6f8A5TEJwMsKCYfwsqOX-zBH5S1GyOMgt2z_pLbMsjygZr_s2MqeQHuj2HKr5n7Jr7YSHn2VVlBET33-IIY-SXWTJJEVR6GLX4w1AqMejxE8eTX8eQ2fdpaaK9F0KXPVt7lOR8lG3Fda8WLzSeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMlrH_N8w-_ZA1Gpn_poc-dwD_kShEFM7y9Lz8hAOjDOy74eio3j7qIL0xODi0MhIz6bBL8AyZzNUh3m-FXXGdSipW01ngzf3pixy3W-zTWDxm-Uu-XfaH0Gy8GP-5g2_5SM7v3USTVAkPv8cuknYrAUaqJqMlh7FleFCRK0Iu1CqmQM4ORcQy1U20yQmShL8gmuBKJiCK7qZZSNY3XRuqFZ-SKgqJAhQ7TARsDkGVgZkUkdiU3Ir8XQEAgCmZ2JLYT13k8Y-0a1EiWEan4ugtXEQvyfRTvX9hYK696lWg9VLYZ2wByjAkB7dPeXK3-sRoj-VoJcF2wdPUwb_CJbdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇦
🇾🇪
الطيران الحربي السعودي شن عدة غارات على مناطق سكنية عقب إستهداف مواقع عسكرية تابعة لمرتزقته في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/91749" target="_blank">📅 13:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91748">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3c348627.mp4?token=ZlB4HscPTQS6vGJ2XpgDZZMu0km8eDy8Q54tTKweBvHzWxPFVhZ_cJdHZy6_XrO9ULmVwDqlwmOMNVCB0ajww3EY1RVBfxLar7fkZZ713gnMchfzj8R_BeOU3AxxqHcGU3b4b4AqXWIC0tEwSNZ8mmv2jvXcGJwSvvyfTcOUrNfzHN7viH1IfRSHx8CZbeX5URABpfFWswFnnlbfufiogQavCOQeeYsztXf0fcW0lWeJrpSKuNht6z8kH42nyRsCd9WTW5QfPGRx4l_b1-Dcym7-PqFFqAkYNN-ne6ThtAmM6ycnqkVF_szvEj04-4TIwg-VFOMqOJn3sddNFtvJ7oseuj5Tk-U1bCFxKaVOVYSs_RPkAkIH5VKiyBK6EwEVIJNGY4Bm0hGqIettGC8iqaSc-hnzUjwXw9KN5xlzcvrZpwnqzqzN1TQF-NMHEv3lpz6GEcZkPbALkQxz7z5YQ04w3kJkleMgxSolOkg1gnM6myGop-zt0cwtMpvwsamvKHq0tRSZatK6ZY9L0Q0wuLhT2_joj2XOKSbZyg41KSF1qBkIAcefWuCoiE0HfZW_pUA28h-WsRj6hi4X44vnoAUEs3Kf87jRSF-6UZuPx9WruD_ysEfQ48vqXug-yy1SFTMQvNprFZYgHrv_R6W7aGh6vi-hIOrouPKbnUZOC4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3c348627.mp4?token=ZlB4HscPTQS6vGJ2XpgDZZMu0km8eDy8Q54tTKweBvHzWxPFVhZ_cJdHZy6_XrO9ULmVwDqlwmOMNVCB0ajww3EY1RVBfxLar7fkZZ713gnMchfzj8R_BeOU3AxxqHcGU3b4b4AqXWIC0tEwSNZ8mmv2jvXcGJwSvvyfTcOUrNfzHN7viH1IfRSHx8CZbeX5URABpfFWswFnnlbfufiogQavCOQeeYsztXf0fcW0lWeJrpSKuNht6z8kH42nyRsCd9WTW5QfPGRx4l_b1-Dcym7-PqFFqAkYNN-ne6ThtAmM6ycnqkVF_szvEj04-4TIwg-VFOMqOJn3sddNFtvJ7oseuj5Tk-U1bCFxKaVOVYSs_RPkAkIH5VKiyBK6EwEVIJNGY4Bm0hGqIettGC8iqaSc-hnzUjwXw9KN5xlzcvrZpwnqzqzN1TQF-NMHEv3lpz6GEcZkPbALkQxz7z5YQ04w3kJkleMgxSolOkg1gnM6myGop-zt0cwtMpvwsamvKHq0tRSZatK6ZY9L0Q0wuLhT2_joj2XOKSbZyg41KSF1qBkIAcefWuCoiE0HfZW_pUA28h-WsRj6hi4X44vnoAUEs3Kf87jRSF-6UZuPx9WruD_ysEfQ48vqXug-yy1SFTMQvNprFZYgHrv_R6W7aGh6vi-hIOrouPKbnUZOC4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من العدوان السعودي الغاشم  على مناطق سكنية ومحلات تجارية في محافظة تعز</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/naya_foriraq/91748" target="_blank">📅 13:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91747">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e43b98bab.mp4?token=oJjGEuoyg1o6F52ZiqBU963xzZH_DsEhsKmhDIew1YUFHw1ulrQYJ0ymZNj6-vpAmVf1Iuu88tlSbCyQEvgzwRaapEagYyegtwZdwHZfldAiNYpWumSxoiFBBhYdnR-t5pONTM8MWMh_BMQ_CLQdcNbsEpajCI70WY4WmbkcFgJ7s_zrL8TvV4Yj9FCtgV3K_-Vby7w342T02RSRSb4YZkMD9bUrh5fW-ZIFrjS9Yd7LD8tSz7dLqjM0sYv7NQ1ePiOWaxDwXuebwAfDCjWc35lz5U1oDjfh0t_wHtL-KG8x0r6Woth0MT5vpqOgypPUFkdZsCE_ZgW5wnwfMbQ1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e43b98bab.mp4?token=oJjGEuoyg1o6F52ZiqBU963xzZH_DsEhsKmhDIew1YUFHw1ulrQYJ0ymZNj6-vpAmVf1Iuu88tlSbCyQEvgzwRaapEagYyegtwZdwHZfldAiNYpWumSxoiFBBhYdnR-t5pONTM8MWMh_BMQ_CLQdcNbsEpajCI70WY4WmbkcFgJ7s_zrL8TvV4Yj9FCtgV3K_-Vby7w342T02RSRSb4YZkMD9bUrh5fW-ZIFrjS9Yd7LD8tSz7dLqjM0sYv7NQ1ePiOWaxDwXuebwAfDCjWc35lz5U1oDjfh0t_wHtL-KG8x0r6Woth0MT5vpqOgypPUFkdZsCE_ZgW5wnwfMbQ1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
سلسلة غارات سعودية على مناطق سكنية في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/91747" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91746">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1922d2a68.mp4?token=oLTkGYFFZ8SNBByghNiNsxZTLFrL2t6oEQrXtQr5YJg_B5oGpBM5X4QDVATyfA0ubvj3t9QLdL4zw6XKJZbeqlXfzr2h4hlO78Wz30AkWnTrOW4a8pK789NdRSlEEJD8xWh_7JcORH-KG-AX5D7w-wDJyI96nO_sPYQtFpDfUEznHKnu_yo8YxpBHwA2C3J7ISE9lWgzbWd3ZWXoduQqVm9LtcLz8XolQbZU8xaT-q3RjZYeyXi3Rk2aRUKd6Ajvj1iLy2aUXnnXiA4G4kqnl-O7xD6XBTW0gCGpeoJzHnbm7VZr33KsVidQkr99B4JDrElgsfLzCzRzEpX-asY-E5fjyET27m2vxY2khCJF_zV4bolW3K0N7DbjYJ8TkYVtQAXZVDRHM5nbFvaT9yTehKGWYfiM0HD0a1Fy3HAFwEm2xUbhYdEraCze2a0_kv3AxHXWK18zwvcizRuQ02_xHn_jiboPA-OO-H7XXYZX24FZ8aw8sPGJHkl6xV5ky62aWV97isQ_6neSUYzA4yLk-3vNazOeylxAomVCenfsQH3hwPe7x4iS-AHWWxlSuzKBuKSbjZGE1aFNcgxIuU7I81sdZ7z0fU_-ElrqmdnS2xnA5meWBC0vRM2USvGsCIhVKpDKaHbfmFSwONl9JHufmihi5xPsbhWsexoJ6xHKH6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1922d2a68.mp4?token=oLTkGYFFZ8SNBByghNiNsxZTLFrL2t6oEQrXtQr5YJg_B5oGpBM5X4QDVATyfA0ubvj3t9QLdL4zw6XKJZbeqlXfzr2h4hlO78Wz30AkWnTrOW4a8pK789NdRSlEEJD8xWh_7JcORH-KG-AX5D7w-wDJyI96nO_sPYQtFpDfUEznHKnu_yo8YxpBHwA2C3J7ISE9lWgzbWd3ZWXoduQqVm9LtcLz8XolQbZU8xaT-q3RjZYeyXi3Rk2aRUKd6Ajvj1iLy2aUXnnXiA4G4kqnl-O7xD6XBTW0gCGpeoJzHnbm7VZr33KsVidQkr99B4JDrElgsfLzCzRzEpX-asY-E5fjyET27m2vxY2khCJF_zV4bolW3K0N7DbjYJ8TkYVtQAXZVDRHM5nbFvaT9yTehKGWYfiM0HD0a1Fy3HAFwEm2xUbhYdEraCze2a0_kv3AxHXWK18zwvcizRuQ02_xHn_jiboPA-OO-H7XXYZX24FZ8aw8sPGJHkl6xV5ky62aWV97isQ_6neSUYzA4yLk-3vNazOeylxAomVCenfsQH3hwPe7x4iS-AHWWxlSuzKBuKSbjZGE1aFNcgxIuU7I81sdZ7z0fU_-ElrqmdnS2xnA5meWBC0vRM2USvGsCIhVKpDKaHbfmFSwONl9JHufmihi5xPsbhWsexoJ6xHKH6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
رداً على إستهداف مرتزقتها.. الطيران السعودي يشن عدة غارات على مناطق سكنية ومحلات تجارية في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/91746" target="_blank">📅 13:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91745">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b73c6fa19.mp4?token=NTNcr_OP1u3qeYZCDuntLxWmYmKBF1_gTpLTPJqqtrC_duC9APjfcS80Ij8JPph8X1SRrg_YzKeBej-uB-YW20_iaTw9nZiZM14KAZNrqCIGk2IOdQKlqSx01vJtHBPV4S9vhiAPoyUUYvY4G4YCHFoWWONJ1FOPQoQ2Lw9eJhdnXXIK0C6Ad2dcvz_nWsd_wg6PApX5tGjD8SixUVW3oQNwxmYqjHEvKiCaS-AGyXnipkqT10D49HlqDyjMmuY7Ed3ZlkWrH2rpQRnUFqpLFrX8Cffmx9lcrLq6IDKHhRNglN5cbmOXZ0DUYo2f92QEc-iMrvxYTI5ZnpCq8csDTHzdVLvMkl97FSD16eZcc-MsmwUPkfTFUproFQjrXnaLlB5Eazg52pMieMwTm1oZ1U21RkShnCYZvrlaRI0tCJXQBqo79Y3XfgotMIQCGQ4m6Qq5H6UlsybxiyPqW_zcEBrGzWHXYGO_rCa1SDjdk1jaXrtuQQWbAV6fr4o7fFTPK0G5lPU8V6CalJYxpdavXexUTWkHa6RxclEwWAZlvUtNqNmjXVDx3mLzIEGROjtBGc7PGwb37-ymg2ecziKlpdrl_HfHs7WBVR1BY3E6CpRvH5Cy5dbXUNVJf-Kjz6008q3ia6dEXQWU7psBA7xGNa2qkU4XvhbX75yEV0J4GHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b73c6fa19.mp4?token=NTNcr_OP1u3qeYZCDuntLxWmYmKBF1_gTpLTPJqqtrC_duC9APjfcS80Ij8JPph8X1SRrg_YzKeBej-uB-YW20_iaTw9nZiZM14KAZNrqCIGk2IOdQKlqSx01vJtHBPV4S9vhiAPoyUUYvY4G4YCHFoWWONJ1FOPQoQ2Lw9eJhdnXXIK0C6Ad2dcvz_nWsd_wg6PApX5tGjD8SixUVW3oQNwxmYqjHEvKiCaS-AGyXnipkqT10D49HlqDyjMmuY7Ed3ZlkWrH2rpQRnUFqpLFrX8Cffmx9lcrLq6IDKHhRNglN5cbmOXZ0DUYo2f92QEc-iMrvxYTI5ZnpCq8csDTHzdVLvMkl97FSD16eZcc-MsmwUPkfTFUproFQjrXnaLlB5Eazg52pMieMwTm1oZ1U21RkShnCYZvrlaRI0tCJXQBqo79Y3XfgotMIQCGQ4m6Qq5H6UlsybxiyPqW_zcEBrGzWHXYGO_rCa1SDjdk1jaXrtuQQWbAV6fr4o7fFTPK0G5lPU8V6CalJYxpdavXexUTWkHa6RxclEwWAZlvUtNqNmjXVDx3mLzIEGROjtBGc7PGwb37-ymg2ecziKlpdrl_HfHs7WBVR1BY3E6CpRvH5Cy5dbXUNVJf-Kjz6008q3ia6dEXQWU7psBA7xGNa2qkU4XvhbX75yEV0J4GHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية في منطقة هان بمحافظة تعز.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/91745" target="_blank">📅 13:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية في منطقة هان بمحافظة تعز.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/91744" target="_blank">📅 12:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
وزارة الدفاع الأفغانية:
مقتل 28 مقاتلا بعد عبورهم من باكستان إلى شرق أفغانستان.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/91743" target="_blank">📅 12:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91742" target="_blank">📅 12:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
‏أجلت الشرطة منازل بالقرب من قاعدة فيرفورد الجوية التابعة لسلاح الجو الملكي البريطاني، وهي قاعدة جوية أمريكية في إنجلترا، وألقت القبض على عدد من الرجال للاشتباه في ارتكابهم جرائم تتعلق بالمتفجرات. وتستخدم القوات الأمريكية هذه القاعدة خلال الحرب مع إيران.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91741" target="_blank">📅 11:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
قائد الجيش الإيراني:
الحرب لم تنتهِ؛ وعلى العدو المعتدي أن يستعد لتلقي ضربات قوية.
إذا كان هناك عدم أمن في المنطقة، فسيكون هذا عدم الأمان للجميع.
لقد رأيتم أن التعاون مع الولايات المتحدة لا يخلق الأمن. الأمن في المنطقة يكمن داخل المنطقة وبأيدي دول المنطقة.
لن يتحقق الأمن في المنطقة إلا بإزالة الولايات المتحدة والتخلص منها، وكذلك من إسرائيل، من المنطقة، وهذا الأمر ليس ببعيد.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91740" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91739" target="_blank">📅 11:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91738" target="_blank">📅 11:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba0e6879a.mp4?token=M0Iv1bYMAuaAXUZNZrV2kYh5Evo2QIih2pv-DV0o0crnZb--mg9p6eKbkENdoV53ylnk7Ve030OiCdcy-aU6wpePu2y1l9T7Zm1feW1Ih82TlsP8PXxMd0TFBiHfMRt40UjPSEtiQA64XSpteEyq7OHOCQQbUEazqpeBVKRy0Hd14nLeGbkPirTkt2eAvcXkjV7VlM2vEg2qVQzHHJpF1JTEBvfnFWsLoQ328bFOUqdKfcZEdmOfHInl3lyVPYTtajHXdhzSahxg7YH2xglg_Mf4LTff0YlhTj2Hsr0Rl2yjTpCwcywifBR2aHpj3GYKY4Q96PbFEj1B2RHcJd0s6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba0e6879a.mp4?token=M0Iv1bYMAuaAXUZNZrV2kYh5Evo2QIih2pv-DV0o0crnZb--mg9p6eKbkENdoV53ylnk7Ve030OiCdcy-aU6wpePu2y1l9T7Zm1feW1Ih82TlsP8PXxMd0TFBiHfMRt40UjPSEtiQA64XSpteEyq7OHOCQQbUEazqpeBVKRy0Hd14nLeGbkPirTkt2eAvcXkjV7VlM2vEg2qVQzHHJpF1JTEBvfnFWsLoQ328bFOUqdKfcZEdmOfHInl3lyVPYTtajHXdhzSahxg7YH2xglg_Mf4LTff0YlhTj2Hsr0Rl2yjTpCwcywifBR2aHpj3GYKY4Q96PbFEj1B2RHcJd0s6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
على الرغم من الحصار الجوي الظالم..
رحلات الإقلاع من مطار الإمام الخميني بالعاصمة الإيرانية طهران تتم وفقًا للجدول الزمني المحدد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91737" target="_blank">📅 11:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
الشرطة البريطانية:
حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.
اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.
إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91736" target="_blank">📅 11:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي في هذه الأثناء يتسبب بإنفجارات عنيفة وسط العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91735" target="_blank">📅 10:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي يزعم:
إطلاق مسيرة انتحارية من قبل حزب الله نحو قواتنا في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91734" target="_blank">📅 09:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني:
يجب على إسرائيل الذهاب إلى الحرب في الضفة الغربية كما فعلنا في غزة.
يجب ضم جنوب لبنان والأراضي التي يسيطر عليها الجيش الإسرائيلي في غزة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91733" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=UQXkzdMgSl9xmHONCYcCI6jFLPl-tmlUw9EgxAOIyeHq77Zm8bA0OckrWii40szjONHxT-nZfQTw0JjkbCaJrSmLyIriTiLX24nq0oD67dcRPpvX-xZwcLIOFqYJT7DchXhKRwpbl62CQdD_Fbqk5uk3FaFJyWh6DQK49djCyPVecfsorgS_9jV6i681CAcedvc2Co_2l3ijjARLpO-8hrDDS17uvmBeN3_6CYjfkwq6pCLH_bBZiSgfCVJ8edZn4aZqIJyIBuw7ZnRirBpRvUhhHvFDgYKpejWq107-Q28edOiuJ5MzI3SD5s7b2ulerZw0yVArFqwpeP7voWPZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=UQXkzdMgSl9xmHONCYcCI6jFLPl-tmlUw9EgxAOIyeHq77Zm8bA0OckrWii40szjONHxT-nZfQTw0JjkbCaJrSmLyIriTiLX24nq0oD67dcRPpvX-xZwcLIOFqYJT7DchXhKRwpbl62CQdD_Fbqk5uk3FaFJyWh6DQK49djCyPVecfsorgS_9jV6i681CAcedvc2Co_2l3ijjARLpO-8hrDDS17uvmBeN3_6CYjfkwq6pCLH_bBZiSgfCVJ8edZn4aZqIJyIBuw7ZnRirBpRvUhhHvFDgYKpejWq107-Q28edOiuJ5MzI3SD5s7b2ulerZw0yVArFqwpeP7voWPZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اللاعب زيدان اقبال: الكويتيين يطلقون تعليقات عنصرية، أنا أفوز، إذا أحتفل. هذا شيء طبيعي. لا أعرف لماذا يأخذون الأمر بحساسية بالتأكيد سأحتفل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/91732" target="_blank">📅 04:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/91731" target="_blank">📅 03:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHsD4jA6IVDqVbrZcfZ6saWjup3Yr-m9egWVFiCOdOYyPO4wYpojq7P7GeBgzSv1_-ntr__BI59taaoGMe8LHvgfxF3z0hrj2PnTp3XvRsc0l8HnaDLPMFh54gnvj2N9-jXbk3u8q8VDzCaRUVOPQjMWe9VJYQMW4ulpzXPOW6XGiiODZzRozJNphe0jojsaSDDtqhyiZFdpKONEv-A6T6TXvLgZ-sUmFwWhwhGD4N_tO3yeMwX7ZSEWKBWmaGI5Bw2ob2eQU9HFn-SUujvQdFME3714jG1kCv4aYDzvsN61ag5y-fqW5DgAU-CUsClwneWn1YU0iaSBrRWKZpvTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/91730" target="_blank">📅 02:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=QJDdDqTqPfdz4AaeYOWa-PtXjme8WcmHrNTyidle6Xbn89O-IBvGE2lJUI6ilcEC16qlrF2xrw5iKUxQyQN_nVzl6QyxbTOL08SQOJUHoS3FM-MAW_AhJfdMlA2UndxDxiLfh8G6oc8fQ8Xow3Pbz-iNCewUbbutXZs_BbmIxA3U0lB7dSlzfovpJQQTbrDdM2zplfmRvYdu8ZNByj0zWFw0_I7ji65WPXA82vscJhIrfPhMjcdiKWfMhzZe9L__BfSV3-u3JkJh1oST_eFZa3FMPNvJ-Gv3RJXb85FRmCzSFrQKQVQqw9dN67NC7dwIJoZPAmCdw6WlB4r1wD1mNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=QJDdDqTqPfdz4AaeYOWa-PtXjme8WcmHrNTyidle6Xbn89O-IBvGE2lJUI6ilcEC16qlrF2xrw5iKUxQyQN_nVzl6QyxbTOL08SQOJUHoS3FM-MAW_AhJfdMlA2UndxDxiLfh8G6oc8fQ8Xow3Pbz-iNCewUbbutXZs_BbmIxA3U0lB7dSlzfovpJQQTbrDdM2zplfmRvYdu8ZNByj0zWFw0_I7ji65WPXA82vscJhIrfPhMjcdiKWfMhzZe9L__BfSV3-u3JkJh1oST_eFZa3FMPNvJ-Gv3RJXb85FRmCzSFrQKQVQqw9dN67NC7dwIJoZPAmCdw6WlB4r1wD1mNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫡
هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ
@Naya_Press</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/91729" target="_blank">📅 02:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
🇺🇸
اصوات انفجارات لم تعرف طبيعتها قرب قشم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/91728" target="_blank">📅 01:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي:
أعلنت وزارة الدفاع الأمريكية عن وجود معلومات استخباراتية محددة وموثوقة تشير إلى وجود تهديد لقاعدة سلاح الجو الملكي في فيرفورد، وقد رفعت مستوى الحماية الأمنية للقاعدة (FPCON) إلى أعلى مستوى، وهو مستوى "دلتا".</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/91727" target="_blank">📅 01:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
🇺🇸
اصوات انفجارات لم تعرف طبيعتها قرب قشم</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/91726" target="_blank">📅 00:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c050b97ca.mp4?token=GT6DRU7bpPjVOFpxtcg1oG7XhQJ2EyXzgb8QGLzDUTulwjD0stvnHBLEo1ZDwpvOtt85hNDFrORdmb4xLH_TWjqEjaFcYyL6ijU-TPbEH0_uY-nXKye1KGircWYjXeRLQx0BaZkhRO1dc38FWvxqORnMvZkvYEVtCyNw7FGWC3FzM7uca6J_ty9md-fIkh1kDWKyLA-GBM5IacBlBOUCQsrGaZZiXVoj39HH91KRNaEm3MZltMH2bP7639Npdm5fVl1tOFwjPjDdlILaYiRo6OUDQtEmf9G7gAwdIGfKw0SaQYcAEFd4q1xnCwPgtKdtyvGf38DPFiMQivznc5vbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c050b97ca.mp4?token=GT6DRU7bpPjVOFpxtcg1oG7XhQJ2EyXzgb8QGLzDUTulwjD0stvnHBLEo1ZDwpvOtt85hNDFrORdmb4xLH_TWjqEjaFcYyL6ijU-TPbEH0_uY-nXKye1KGircWYjXeRLQx0BaZkhRO1dc38FWvxqORnMvZkvYEVtCyNw7FGWC3FzM7uca6J_ty9md-fIkh1kDWKyLA-GBM5IacBlBOUCQsrGaZZiXVoj39HH91KRNaEm3MZltMH2bP7639Npdm5fVl1tOFwjPjDdlILaYiRo6OUDQtEmf9G7gAwdIGfKw0SaQYcAEFd4q1xnCwPgtKdtyvGf38DPFiMQivznc5vbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
تغطية قناة نايا للاحتجاجات في محافظة البصرة جنوبي العراق رفضًا لتشديد الخناق على الجمهورية الإسلامية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/91725" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يقرر تعطيل الدوام الرسمي في مؤسسات الدولة ابتداءً من يوم الأربعاء المصادف 30 أيلول ولغاية يوم السبت 3 تشرين الأول المقبل، احتفاءً (بأيام السيادة) لجمهورية العراق.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/91724" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ffae4249.mp4?token=m7e7vx4v07aBaqaOT_JXbiTfd_2nEA0SHJvLuQl3aX0rYaFJgUzm-jijdagvVqIuqbKLN2O3t2_o_CwnEjxD_DRR6ooHNA6MWoCKbEV_AIs3W08TOv_pmMSYrubSfE940g6-DSHBWXHrxiIzSbioZT3TNmtAk5bmZHXg-SH225HPwV_KONlwBrQH8uKYf5UNLxjedoLdMRiyFqEL3osClNNbwWEEWjjYti-w2Isercq9xPFtphtPIAvMGdsspLQ7GTcrF95sN4Pwp1yJSfLz_oeTcduwjdN67zrWwK7K5USBpDA4HbeE8Bk1aLK85I5Kcl4tZOXa9W-bwRIzDL2jrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ffae4249.mp4?token=m7e7vx4v07aBaqaOT_JXbiTfd_2nEA0SHJvLuQl3aX0rYaFJgUzm-jijdagvVqIuqbKLN2O3t2_o_CwnEjxD_DRR6ooHNA6MWoCKbEV_AIs3W08TOv_pmMSYrubSfE940g6-DSHBWXHrxiIzSbioZT3TNmtAk5bmZHXg-SH225HPwV_KONlwBrQH8uKYf5UNLxjedoLdMRiyFqEL3osClNNbwWEEWjjYti-w2Isercq9xPFtphtPIAvMGdsspLQ7GTcrF95sN4Pwp1yJSfLz_oeTcduwjdN67zrWwK7K5USBpDA4HbeE8Bk1aLK85I5Kcl4tZOXa9W-bwRIzDL2jrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تغطية قناة الميادين اللبنانية للاحتجاجات التي خرجت في العراق تنديدا باغلاق حركة الطيران المدني مع الجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91723" target="_blank">📅 23:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
🇮🇶
الشيخ محسن الاراكي:
بسم الله الرحمن الرحيم
قال تعالى:  والذين كفروا اولياهم الطاغوت
ان ما قامت به الحكومة العراقية من سد الطريق أمام زوار أمير المؤمنين والامام الحسين الشهيد جعلت من الحكومة العراقية الحالية ذيلاً ذليلاً من ذيول الطاغوت الامريكي شأنها شأن ساير الطواغيت الذين حكموا العراق مما يسلبها كل مقومات الشرعية الدينيهة وعلى هذا فاإن اصرت هذه الحكومة على سياستها الطاغوتية وانصياعها المطلق للطاغوت الامريكي فهي كسائر الانظمة الجائرة الطاغوتية ويترتب عليها كل احكام الطاغوت ويحرم على المسلمين التعامل معها كنظام شرعي بل حكمها حكم النظام الاموي وما شاكله من الانظمة المعادية لرسول الله صلى الله عليه واله واهل بيته الطاهرين عليهم الصلاة والسلام والحكام الطواغيت الذين يجب اجتناب التعامل معهم كما قال سبحانه وتعالى ولقد بعثنا في كل امة رسولاً أن اعبدوا الله واجتنبوا الطاغوت فمنهم من هدى الله ومنهم من حقت عليه الضلالة فسيروا في الارض فانظروا كيف كان عاقبه المكذبين.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/91722" target="_blank">📅 23:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153b76ec5b.mp4?token=oYwhYyrgPYyOG53EG-B9ZsHnFLol65KDKvOWsDmH2FOVt1LBRZRMM056gqwULDN0eM5hdwSYDXz0HsTQ6cpeBAUiGz8H4XY4BLnnLsJz0hyg8j1M6oQ2h95dIpCWufu_8uUx0JZ66QNEbx6Klijr82Xc-vznbujta8h0PKgigALSOzBUgShBdnZzlytYJb46CLxilKLY9MdPBPYryfptkX5tr8WjeIoyo6wi1GVJahhl86TKyWeSe4y302mGmvGZrVkyN4_0OCUkjzBOv0Rf7IoiCXStv87mTQzalf6ymRmoiJ7xrubzQe2WQGWadC6NiY7PtOgeFocVqv4AGHQaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153b76ec5b.mp4?token=oYwhYyrgPYyOG53EG-B9ZsHnFLol65KDKvOWsDmH2FOVt1LBRZRMM056gqwULDN0eM5hdwSYDXz0HsTQ6cpeBAUiGz8H4XY4BLnnLsJz0hyg8j1M6oQ2h95dIpCWufu_8uUx0JZ66QNEbx6Klijr82Xc-vznbujta8h0PKgigALSOzBUgShBdnZzlytYJb46CLxilKLY9MdPBPYryfptkX5tr8WjeIoyo6wi1GVJahhl86TKyWeSe4y302mGmvGZrVkyN4_0OCUkjzBOv0Rf7IoiCXStv87mTQzalf6ymRmoiJ7xrubzQe2WQGWadC6NiY7PtOgeFocVqv4AGHQaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/91721" target="_blank">📅 22:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003d924fe5.mp4?token=LF1kLXzKdb5CQ4c9dkD0UFAMpzmIZD4LyutHsTNlzUMzjl6vBXQw41IPEHPKxJbP0mYnL82DuUN-A8jhnQowzjhWSFTG3fYTq_VnZSF3WUE_a78YBJ1epEC9FK9F6uAw5WfOyYihDimQchE7uSQHczPopF3GRpl1iugzYQRv1iavA7ZWbjHt--9khFteFMno0Gn2UDX5gdPuqs8ZaP0uwmfMwrrBAveoXkWlDt7qRH4AcwOEjHWjIzraYcUi5wO3c4Y_DAQ0Nzw1_BMa1eTu8wqtV5jQQSGEErxPqEA3iwJkkB69H-U9yDc7xxdq41QmGNOHhhKcPSUJPaCogv7l2EdO78yggZAn5qJ4MhFIYriyicq9mohQbTFwV9lmiM1kzoYEBPnYmywid-_nbjqwB7jrai2x05YL63NKZsxsMyjW-rbY8r2RvlRuyqQNDJZQOOiGbCCdJvD-TldHepjtOmSl7-1_NNXNxh8zU6uWzjzZAZh-htmxDrZnQiRHFKdbCvwza-EKvPOwwPmui6WSAaw5PrxT759AHvV0d2UkgmKLByJ7DB5aNP4YtJq9vO5EIwl9kvPTVzvaaO6Cmo0--6dXQa1G7mHA5yRIY0sN_fiiyBRZf1-Dnj-Y3L8AGn9-ExELR-WMpeml-CZs2J_kYgmRYTxmSe04HgKbL6KjXv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003d924fe5.mp4?token=LF1kLXzKdb5CQ4c9dkD0UFAMpzmIZD4LyutHsTNlzUMzjl6vBXQw41IPEHPKxJbP0mYnL82DuUN-A8jhnQowzjhWSFTG3fYTq_VnZSF3WUE_a78YBJ1epEC9FK9F6uAw5WfOyYihDimQchE7uSQHczPopF3GRpl1iugzYQRv1iavA7ZWbjHt--9khFteFMno0Gn2UDX5gdPuqs8ZaP0uwmfMwrrBAveoXkWlDt7qRH4AcwOEjHWjIzraYcUi5wO3c4Y_DAQ0Nzw1_BMa1eTu8wqtV5jQQSGEErxPqEA3iwJkkB69H-U9yDc7xxdq41QmGNOHhhKcPSUJPaCogv7l2EdO78yggZAn5qJ4MhFIYriyicq9mohQbTFwV9lmiM1kzoYEBPnYmywid-_nbjqwB7jrai2x05YL63NKZsxsMyjW-rbY8r2RvlRuyqQNDJZQOOiGbCCdJvD-TldHepjtOmSl7-1_NNXNxh8zU6uWzjzZAZh-htmxDrZnQiRHFKdbCvwza-EKvPOwwPmui6WSAaw5PrxT759AHvV0d2UkgmKLByJ7DB5aNP4YtJq9vO5EIwl9kvPTVzvaaO6Cmo0--6dXQa1G7mHA5yRIY0sN_fiiyBRZf1-Dnj-Y3L8AGn9-ExELR-WMpeml-CZs2J_kYgmRYTxmSe04HgKbL6KjXv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من جانب المليشيات الموالية للسعودية للصواريخ الجوالة التابعة للقوات المسلحة اليمنية وهي تتجول فوقهم تتنتضر اللحظة المناسبة لكي تنقض عليها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/91720" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امر مستغرب جدا   لا موقف """جدي """ عملي معلن من قادة الإطار التنسيقي الشيعي حول ما يجري بمطار النجف ؛ الإطار هو الذي  أتى بالحكومة ؛ و لا نريد تغريدات لكون البيانات لا تغني ولا تسمن     والعتب الأكبر على من نحسن الظن بهم الشيخ همام حمودي ؛ السيد هادي العامري…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91719" target="_blank">📅 22:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
أنباء أولية تشير إلى غياب عدد من لاعبي المنتخب العراقي عن المباراة المقبلة إثر الاعتداء الذي تعرضوا له.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/91718" target="_blank">📅 22:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db08d7c938.mp4?token=T0wN0FBRVr2DUN99_hRfskHT2rQxQRBtIH5I0IQaXvhVUeDIY1iJpfKSMWDzeaTnRSW_xGd_VtJxscFuc7LWAoA18agy0_mZ_lgfyppqxlU4aP1A7J9RbIVRCWJp8PhGmeyS07ZSDvwIJuQprZ5TayRGLi0rqD_T0PkC1L3GyKKkzBwsE8inEHhn4M2ezmT5yN5FIjro--962IOZrlzGivWJLHuUlK15OMr5ZkbR5j690NhE9nzRQKn9o53vdJFjWgB2j9OBKnHblFi9PjXjJFLORZE3UJF_ckwfFRnSXXAuQp8qptc2pEeICE-Nsv0rPh7KsUigeB_DlpUEeo8qwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db08d7c938.mp4?token=T0wN0FBRVr2DUN99_hRfskHT2rQxQRBtIH5I0IQaXvhVUeDIY1iJpfKSMWDzeaTnRSW_xGd_VtJxscFuc7LWAoA18agy0_mZ_lgfyppqxlU4aP1A7J9RbIVRCWJp8PhGmeyS07ZSDvwIJuQprZ5TayRGLi0rqD_T0PkC1L3GyKKkzBwsE8inEHhn4M2ezmT5yN5FIjro--962IOZrlzGivWJLHuUlK15OMr5ZkbR5j690NhE9nzRQKn9o53vdJFjWgB2j9OBKnHblFi9PjXjJFLORZE3UJF_ckwfFRnSXXAuQp8qptc2pEeICE-Nsv0rPh7KsUigeB_DlpUEeo8qwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/91717" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecfe6219e.mp4?token=A8lv6887qgw1-VNdtWQ973a75rpux2gw6hTaDI1NyqwJoccdzWjQ2MTAfOdOfUNNU8xRFjPhLb4x2RyOCuRBS6F_FjOreZSKLASaSP7vGrjtByqcjh1bujgSn4xrSsH6LKJwIY4Wmd5PmwAng7QPmBEYZpP2IPGD9fpYAcnpqoJkZyBTHgbN0zFW2sAye-HnBX5SrVpK-FRkUFS-cIIUYRIC4mZKaCu3tin2RujsAyVLS2To9qLmrVml9iGsGdzO4_PGYRRzUkb4_OGZYe6wlzNcowGPH76O7bdds1IygICHBwMDK_i9qxLCQ0cXjIWB3hM88WsofBKKrjlxQg-hEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecfe6219e.mp4?token=A8lv6887qgw1-VNdtWQ973a75rpux2gw6hTaDI1NyqwJoccdzWjQ2MTAfOdOfUNNU8xRFjPhLb4x2RyOCuRBS6F_FjOreZSKLASaSP7vGrjtByqcjh1bujgSn4xrSsH6LKJwIY4Wmd5PmwAng7QPmBEYZpP2IPGD9fpYAcnpqoJkZyBTHgbN0zFW2sAye-HnBX5SrVpK-FRkUFS-cIIUYRIC4mZKaCu3tin2RujsAyVLS2To9qLmrVml9iGsGdzO4_PGYRRzUkb4_OGZYe6wlzNcowGPH76O7bdds1IygICHBwMDK_i9qxLCQ0cXjIWB3hM88WsofBKKrjlxQg-hEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91716" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91715" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رمي قناني المياه وتمزيق ملابس المنتخب العراقي على ايدي المنتخب الكويتي وكادره الفني  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91714" target="_blank">📅 22:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab243b15e.mp4?token=q4PFEzpm0xx6jH5rfgRSSLTXtHiS8HcdNogvfjtvsl-yFU4hh7-YEunYMxqszNa9Xp7v-tBsFdaH1svphpEQWiO343TgIT_0-8YupTegtU-MMPskSiH5av2jffDFeY33C7W9Grh12JTbc75kmaus95YIWBazgI9KzUe6vPZwMIX3gYyD21LfyoItWjeY5AScBE_10dXNhWzwJnJu-gDchkupfUaasR-hKuEoqPjqIg0GRYpllJAxXhBDsHfWYf7hmleDRK35ItD1hFWWIoU5CPbTtvaC6o0v4BFYABKTCHgT89xV7alAXazk5OityJDfjp0mSBw3dHpK1-u8PtCh8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab243b15e.mp4?token=q4PFEzpm0xx6jH5rfgRSSLTXtHiS8HcdNogvfjtvsl-yFU4hh7-YEunYMxqszNa9Xp7v-tBsFdaH1svphpEQWiO343TgIT_0-8YupTegtU-MMPskSiH5av2jffDFeY33C7W9Grh12JTbc75kmaus95YIWBazgI9KzUe6vPZwMIX3gYyD21LfyoItWjeY5AScBE_10dXNhWzwJnJu-gDchkupfUaasR-hKuEoqPjqIg0GRYpllJAxXhBDsHfWYf7hmleDRK35ItD1hFWWIoU5CPbTtvaC6o0v4BFYABKTCHgT89xV7alAXazk5OityJDfjp0mSBw3dHpK1-u8PtCh8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الاستفزازات التي قامو بها لاعبين المنتخب الكويتي للجماهير العراقية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/91713" target="_blank">📅 22:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ع المطار يالكويتي  …</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91712" target="_blank">📅 22:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odM1C9xbO4RDoitAMaKP1HqYPRa9hOfOxvNIWMSaJrYSDQtE6JdO4Zbvy8FqCtyggYZw752mBsk-AFdYT5jgBMt_P3LVy3Zw_HmggMXkpkhYvb3wQjng4mIMwq1SHfTnLrv8XoCtuM2kRul-zC7sYs2Bdv4FlH5AFQp785RWAJllcbKiuj8M6AheZfTYO2eQguy8rh-eIP7p7eecFRcj_Rfrdx7wEsS7pVsG8WgxJhsmbUAUuGZfNxwjMLH03_9sJMvkeB7pJRJnAulJXMyVKSy26GPKTjt2mh-2DOYcoiQwDSZD4sF61xLjJosUirvy2mlIzH8nc_HAk7mvA0xKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91710" target="_blank">📅 22:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CinKssWy_m7c30-HYtx1wuaNVgpRIvIJ03LMhwfLp3LAzolx-oxBSrluf_80SUe7sQesYspZ6DJS073ASnRw-6bVw_MrISqUh_mzQ8eRld8GZiErEriTm-UrSdjgfr1C-T2TtdCozLgI7gmzJLS5K-NySSU2AUfGmWlLFgVfAhAbGeTHnF2RcE_j0p3h8yLBQdDKNafCnBZQtBOGPgFzrahzzxFr-dwbi899W45AIOpAidXpTmiRRLR1XBM5fbjDT5HccdODEUUnJZYaVPkhcaE_ovJr6cKiupomUc7HGw8hGSZCVXKKu3wwDs0BgVNcu0mqX1HriaxxZPW_fW7F8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91709" target="_blank">📅 22:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e722e77e90.mp4?token=b9gIocH6TOaEZTEDnA8Qxx1R8KYEIaKpdS8BnZfDhzsJUKgxRz9d1_R_nI_o9SADNhIwUQ2ERU6FABUUCu29W29ZQEuM56AQQC2rn2MayHPXIUkETs4r0nfoZ85VtBy6C9SwfJyQISk2Mo4uj1dwymcqcxGLK-1WqYuxKQhcjqrnpeN00VcLTfDOsrD2DQED4QhwIvGj2zSlbuKpdJ2592C2FhKallJePReiZ_hG857Anvuf6tAwtjFMYTax0Y0DLNW6S7nbeQXvRXI48CqFrx-Z12He9TwRNtuR9GnbII6SNxP_5uhWRAOZQ433FHZze5MFSOZXsr3UCz373Qn8aHtDGdGxcs5U2qku-Sfq24-xX9FHjAmHKaWxuxtMDB27bmsgx0QIEj9eBqnePAVUmpsb_IdvDQILKn3C_fdPFVBRGCZow4k-lf0uLx0Tlj_BKuuOe_0ccm3GmF8-wWmJ7BAeV-OQnH_makbmawyuUZUnpWO3t-h-GA-6OCpBE6CMSttEb3hHuOfw0j5fFfDXKUWfKMR7Qpxqs7-Fw2G_ssSw3MbkQwNN6GozsrRwqj_j0zsDQ_LOtRyxOWsgSc0SuyhYTKofJXPXsf1e-8xXULmoqgRo2dJd_Auh0slZG_cSrSv_yJVw9ReFww2HDi2m11MzoTREMaUrehkyF3FHiLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e722e77e90.mp4?token=b9gIocH6TOaEZTEDnA8Qxx1R8KYEIaKpdS8BnZfDhzsJUKgxRz9d1_R_nI_o9SADNhIwUQ2ERU6FABUUCu29W29ZQEuM56AQQC2rn2MayHPXIUkETs4r0nfoZ85VtBy6C9SwfJyQISk2Mo4uj1dwymcqcxGLK-1WqYuxKQhcjqrnpeN00VcLTfDOsrD2DQED4QhwIvGj2zSlbuKpdJ2592C2FhKallJePReiZ_hG857Anvuf6tAwtjFMYTax0Y0DLNW6S7nbeQXvRXI48CqFrx-Z12He9TwRNtuR9GnbII6SNxP_5uhWRAOZQ433FHZze5MFSOZXsr3UCz373Qn8aHtDGdGxcs5U2qku-Sfq24-xX9FHjAmHKaWxuxtMDB27bmsgx0QIEj9eBqnePAVUmpsb_IdvDQILKn3C_fdPFVBRGCZow4k-lf0uLx0Tlj_BKuuOe_0ccm3GmF8-wWmJ7BAeV-OQnH_makbmawyuUZUnpWO3t-h-GA-6OCpBE6CMSttEb3hHuOfw0j5fFfDXKUWfKMR7Qpxqs7-Fw2G_ssSw3MbkQwNN6GozsrRwqj_j0zsDQ_LOtRyxOWsgSc0SuyhYTKofJXPXsf1e-8xXULmoqgRo2dJd_Auh0slZG_cSrSv_yJVw9ReFww2HDi2m11MzoTREMaUrehkyF3FHiLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد ممارسته حقه في الاحتفال... المنتخب العراقي يتعرض للضرب من قبل الجماهير والكادر الفني الكويتي خلال بطولة كأس الخليج في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91708" target="_blank">📅 22:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
بعد ممارسته حقه في الاحتفال... المنتخب العراقي يتعرض للضرب من قبل الجماهير والكادر الفني الكويتي خلال بطولة كأس الخليج في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91707" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية: توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91706" target="_blank">📅 22:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371f04e10f.mp4?token=bNt55NAVtqta-CpGNKsdnQqEQK6SqA5Dnk5a1zrYN1uN_7b5x8ROmBylUWcamUE9vOY8gqQ-C738nGqjqobM41hpLF7pJgdw975he02WRFbbJqpWAQKIrXJFd1RUJw-ue2dKE_fTFm-ajAFEBnlHj6aN-159UjpLzwfVvMVZDkmhQJctJSj3pzcnyT93M3IZW4kmDjHBkhpY1QGRWT_z7lhNlzMB83xyyENz5QI2IXr0sm0JcJEBZeQYx4GfJhhIIb0Zyml2s1ZAUgfXNsJ3528UdpyznPd3cOBfb_4Gr-d-G2QjHRVua36kPEdjKUU4b8-Sa2V9h5NBE6R11Rw6lzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371f04e10f.mp4?token=bNt55NAVtqta-CpGNKsdnQqEQK6SqA5Dnk5a1zrYN1uN_7b5x8ROmBylUWcamUE9vOY8gqQ-C738nGqjqobM41hpLF7pJgdw975he02WRFbbJqpWAQKIrXJFd1RUJw-ue2dKE_fTFm-ajAFEBnlHj6aN-159UjpLzwfVvMVZDkmhQJctJSj3pzcnyT93M3IZW4kmDjHBkhpY1QGRWT_z7lhNlzMB83xyyENz5QI2IXr0sm0JcJEBZeQYx4GfJhhIIb0Zyml2s1ZAUgfXNsJ3528UdpyznPd3cOBfb_4Gr-d-G2QjHRVua36kPEdjKUU4b8-Sa2V9h5NBE6R11Rw6lzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
العراق يهزم الكويت بثلاثة أهداف لهدفين في خليجي 27.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91705" target="_blank">📅 22:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpRKi63_SDKe71SKbdpbLeDSlDDInjs_4rZjxjTDK9j7NvxhuU5JfQHtOGh8EQ92pTkdQSYpfuOKQ2qzDtrWawSzz2pWIxdeimhf-z7xP6A5izzGxpk3BCBJvMriwHh4Fmw3DDdxpHHaUnL6ewcJoNxmeA7SZ4C8iKm4ruQlnoayqgBF467iksjG98FzpI3eLnA7GJR7PAAQ16zvn4gDh7bkbNyz84npsOh0cdqq4UuDHKgNTabEgWC7jIHxvuRzPsZthxc5XKTWdUD0IzxW5M_Wrbvz5LHYzwXK33VIIudf20h21n9sw3jjRSSIKYBjd5476nwR6fgtAAIBUEyn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب العراقي احمد شهيد:
جمع تواقيع نيابية لعقد جلسة طارئة بحضور رئيس مجلس الوزراء.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91704" target="_blank">📅 21:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
العراق يهزم الكويت بثلاثة أهداف لهدفين في خليجي 27.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91703" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
ابراهيم عزيزي:
نطالب الإطار التنسيقي في العراق الذي انتخب الزيدي وأن يضبط سلوك الحكومة ويرفض الانصياع للإملاءات الأميركية ، فصائل المقاومة في العراق تعرف واجباتها إزاء محاولات الاستجابة للإملاءات الأميركية بما يتنافى مع إرادة الشعب. أي بلد يتعاون مع عدو إيران ويقدم له إمكانات فإن من حق إيران الرد عليه وهذا حق مشروع.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91702" target="_blank">📅 21:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇷🇺
🔻
‏وزير خارجية ألمانيا أثناء لقاء لافروف: العودة لعلاقة بناءة مع روسيا ممكنة.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/91701" target="_blank">📅 21:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAsoa5arxX-9K2IhMXilUqSKG6ob6mYpban7Me4tRCWCq_hNE9YafSVIzR8Pe7bURirdSW52ZnJsXFiwfXh1BXd0P_N7y01ZBa6q9Ia46yxPtvQ13nnc6VwZeJAmKtAN9_uu-WC5_gT9qrLtYT1LmC7x7WkT2DEa6FEJq2masHIQEVS3ymErBPhUn_sd8lOS_HI6YlbD1_QcXdymNi_Xm3kRFC2HsEDpYPdXm7Wy9wzLUtxlhkTirrud1WkkBglTKbKmTL0AIg41sHEzO35LgRRa-r6yRtlBn3jsW6rXPzsGARtAQEsLHbvnj5hbka5ERjPxJm6YrrdCHML4eJQ0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
تيار الحكمة الوطني يصرح:
إن العلاقات العراقية–الإيرانية علاقات مهمة ومتينة، تستند إلى جوار ومصالح ومشتركات واسعة، ومن هذا المنطلق نأمل أن تكثف الحكومة العراقية من جهودها واتصالاتها الدبلوماسية لإيجاد المعالجات لهذا الملف، بما يحفظ سيادة العراق والتزاماته ومصالحه.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91700" target="_blank">📅 20:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
المتحدث باسم الحكومة العراقية
: رئيس الوزراء  توصل إلى تفاهمات مع الولايات المتحدة لضمان استمرار إرسال شحنات الدولار النقدي إلى العراق، ومن المقرر وصول شحنة جديدة خلال الأيام القادمة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91699" target="_blank">📅 20:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3ykn_z7Ix3OKyqZeQcSWZRBQ5mGzaD8MCrGqOEiBWzVEEHpcfiAiRsB0uWxmPbIjrVc5_VDsZTllmMljAjclUDDlMge0KtcdyAC83KbYWssGng4hDrGJRQ3roxHyKLjHCJ9H2VAYb1jE7TdyPq_D56o60oNRon0-KyOyvYvLk78EM0ppXbA9gMcmuKmojj73h7QxEiNvyOFit4pzx9jX7W9PYP33GlQiZg4G4QodXSmq2kdhf4jb_OYkeeI2oRSlR4_jXalLnztcncG8_IFIBWDvdz0wMQ3_N-RBycb_8kFvo85_xWNwZyYUO4-nGudbqEgfjBaZ59WxLwsqXbgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
كتلة دعم الدولة النيابية:
القرار العراقي يجب أن يصدر من بغداد لا من أي عاصمة أخرى.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/91698" target="_blank">📅 20:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇸🇦
‏
وزير الخارجية السعودي:
ندين اعتداءات الحوثيين وتهديدهم للأمن، ندعم الحكومة العراقية في ملف حصر السلاح بيد الدولة، ندعم سيادة العراق وأمنه ونشدد على ألا تكون أراضيه منطلقا للاعتداء على الدول المجاورة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91697" target="_blank">📅 20:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: ‏
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 27 غارة جوية من خلال طائرات "F15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، استهدفت الأعيان المدنية من جسور وطرقات وغيرها فى محافظات تعز ومأرب وصعدة وعمران وإب وحجة.
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1059 غارةً وصاروخاً.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91696" target="_blank">📅 19:48 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇷🇺
‏لافروف: روسيا مستعدة للمساهمة في تحقيق الاستقرار بمنطقة مضيق هرمز.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91695" target="_blank">📅 19:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي: نؤكد على ضرورة أن ترفع الولايات المتحدة حصارها المفروض على كوبا، وأن ترفع جميع القيود المفروضة على التجارة مع كوبا.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91694" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91693">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b190934d58.mp4?token=PgRqGF9VMevHjazcJvIY0Cil3yVC2IqaMk8UnRqAZQls-psPo4Ezl22iXAQM7hTq1XB882Imu8eLPvGzeqqIT59KsP93kWQLCuK9cdMUneM8cP4W4eG83x6wQZeFhmcpRNsP5Tz2lBrPwjy69yfFL313xlEeJu3d92fxVs8BvTUvvzUo725QJx01vHEgtjZnWrbz-08dLo2OvVXaMgkfsTS1PYhjEfx_DpjpECFHAdALEqUS3h9_zYiubcckWM6MjceC84iRTJlEsoGzKm_3BMGFcJA8FVj6ogKBJLxbvNXoQ8vX13wkKgV50Chj5Du1hR8QRGB_sMsJPrv7yA1Z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b190934d58.mp4?token=PgRqGF9VMevHjazcJvIY0Cil3yVC2IqaMk8UnRqAZQls-psPo4Ezl22iXAQM7hTq1XB882Imu8eLPvGzeqqIT59KsP93kWQLCuK9cdMUneM8cP4W4eG83x6wQZeFhmcpRNsP5Tz2lBrPwjy69yfFL313xlEeJu3d92fxVs8BvTUvvzUo725QJx01vHEgtjZnWrbz-08dLo2OvVXaMgkfsTS1PYhjEfx_DpjpECFHAdALEqUS3h9_zYiubcckWM6MjceC84iRTJlEsoGzKm_3BMGFcJA8FVj6ogKBJLxbvNXoQ8vX13wkKgV50Chj5Du1hR8QRGB_sMsJPrv7yA1Z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: هل تخططون لعمل عسكري ضد كوبا؟ وردت تقارير تفيد بتفعيل قوات احتياطية، ربما لمواجهة كوبا.  ‏ترامب: أقول إننا وكوبا سنتوصل إلى اتفاق. لا أعتقد أننا سنحتاج إلى الجيش. فريق شيكاغو كابز يعاني من تراجع حاد. نريد مساعدة كوبا. نريد أن نفتح كوبا أمام شعبنا.  ht…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91693" target="_blank">📅 19:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d52808a7c.mp4?token=bPUweYiRa5WVWJd31vmho6MqTlnEeQUxhed9faculL-53JwsLGYrxJ_bBtFA98S8Hi0N9738qgFmx9xWc1zykR_KUluOUYh6ekvkSgz1p0ywQOOC5sP75rb9S4cwJCsTJCIdhL52QlSL_8EGqKexd2BBHLY77rqniIW2kQKo8L_gqvZhfWc386b1Hr84GsYnr7xb5sGJ-JGp2pL98RCpmWs9wQCsIjsJlDUs8VJMz6REK5GCiTwtrrPMK70y9giB_vH4sVhTWCA3Yg4iM9EKAqA6y_HkWbFF-EDyhDteRgXAXrM_7OCimfFiWL6np6n8CEtC6Rk5tN4vnZjfbThiMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d52808a7c.mp4?token=bPUweYiRa5WVWJd31vmho6MqTlnEeQUxhed9faculL-53JwsLGYrxJ_bBtFA98S8Hi0N9738qgFmx9xWc1zykR_KUluOUYh6ekvkSgz1p0ywQOOC5sP75rb9S4cwJCsTJCIdhL52QlSL_8EGqKexd2BBHLY77rqniIW2kQKo8L_gqvZhfWc386b1Hr84GsYnr7xb5sGJ-JGp2pL98RCpmWs9wQCsIjsJlDUs8VJMz6REK5GCiTwtrrPMK70y9giB_vH4sVhTWCA3Yg4iM9EKAqA6y_HkWbFF-EDyhDteRgXAXrM_7OCimfFiWL6np6n8CEtC6Rk5tN4vnZjfbThiMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي:
نؤكد على ضرورة إطلاق سراح مادورو وزوجته على الفور.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91692" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇶
انطلاق مباراة منتخبنا الوطني أمام الكويت في بطولة كأس الخليج.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91691" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIM1-xJeJfnI7EoR3SxhcRvjFY7T_AH3MsUGpGep3hcTD7fMpJK95CDZ0x4HmZsp3XAUpuHBLEwvDn2PF4b5GLY8P096x8djABI7a70Dzf3oNBaO05k0rNpadlzymGtZz_9l3z0f6_Fj4UejiRuBsDvZ9SGcc7CK1qTevvKGdZeNax0SzgmbmLIll4AePb2CwDNgDGARSsO1RNlc2ETEXnvWoAECWhb02Je8KpZ4GnX_kFuR6CDJiRmCCH_UVOt6rsV-0tnUGQqVH8nSOu_s1N_VqojLVHZGLYMsP8A3xVU8blxNaVcfUOB3hBWlqvzpRw-BbNda6xBV5e2dUrLI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
محافظة البصرة تتحضر للنزول إلى الشوارع احتفالًا بخروج قوات الاحتلال من الأراضي العراقية في يوم 30\\9.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91690" target="_blank">📅 19:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مشاهد من الوقفات الاحتجاجية في محافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/91689" target="_blank">📅 19:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇷🇺
🔻
‏
وزير خارجية ألمانيا أثناء لقاء لافروف:
العودة لعلاقة بناءة مع روسيا ممكنة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91688" target="_blank">📅 19:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
مؤسسة النفط الليبية: توقف وحدة في مصفاة الزاوية بسبب إغلاق مسلحين لصمام على خط "الشرارة".</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91687" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇾🇪
🇸🇦
بعد الضربات الموجعة ‏استعانت شركة أرامكو السعودية بشركة إيفركور لتقديم المشورة بشأن خطط إعادة الهيكلة التي يمكن أن تؤدي إلى إنشاء قسم غاز مستقل وتمهيد الطريق لطرح عام أولي محتمل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91686" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de7c72618.mp4?token=eTDyFCanXg1F-g4-tRo9PLkjdmXK5FZ1wWLTNv9SccgVQDP-QUJZmE-0mHMK5SVWDAf758Y3ZLxvK4gSzLTEdrQabbbT6MWONEq9BN09RRPi0K5r45PWwdMQxkyFocd85Ny9koylm_flCPaZO8GTF5ZE5tl7tCMogD3PLelxRM6ihneMMe6ncEvYwUtiOu8KuitIgsIIr_uAjQXrIkNzi5kQhqnWwbX6a62W5X81okMd7mmar5THNZ2dWjRJ3EkQJeNZcbBQXz-a76DLBUsg6yNIa5BpVA8dbhwLf7WCPT6GEMqCeJKVR3GfqX5n02nrWWEi9atKdXf9SD7UFg_txA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de7c72618.mp4?token=eTDyFCanXg1F-g4-tRo9PLkjdmXK5FZ1wWLTNv9SccgVQDP-QUJZmE-0mHMK5SVWDAf758Y3ZLxvK4gSzLTEdrQabbbT6MWONEq9BN09RRPi0K5r45PWwdMQxkyFocd85Ny9koylm_flCPaZO8GTF5ZE5tl7tCMogD3PLelxRM6ihneMMe6ncEvYwUtiOu8KuitIgsIIr_uAjQXrIkNzi5kQhqnWwbX6a62W5X81okMd7mmar5THNZ2dWjRJ3EkQJeNZcbBQXz-a76DLBUsg6yNIa5BpVA8dbhwLf7WCPT6GEMqCeJKVR3GfqX5n02nrWWEi9atKdXf9SD7UFg_txA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: قوات الاحتياط بالجيش الأمريكي تضع الأسس لعمل عسكري محتمل حول كوبا.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91685" target="_blank">📅 18:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3552d477f.mp4?token=H4m6iLfUaPDz7ig69J31lKkaTmvULm6ZmGFlWaXOZtmhm8Lg2rEcL2tuyjSqtQxrWOSizSNgq26Liym24Y50hMAFMn816zCZ7NY-zisp4CevGwnaYCrEMLs_ZicZBm8v3XUQA2b2Y89sUBccdOK5CPblj1ByoROXKey6TS4xpoZ4ebTb-Sh3xIxZwItkNuGU3XrHIZ6JVIzKpP-ro6iDJ44bnMtEhH-87iD6hrOqfDQju2DjyV1IDOn7VrjHVdNSkqV4_3m4Kjw0fTqBOJcCNi7YyjtTZXO-lpW3McwRHijIATipnJarNSxi6dfu4a9INXy0hxDVoE1F_H31TgZGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3552d477f.mp4?token=H4m6iLfUaPDz7ig69J31lKkaTmvULm6ZmGFlWaXOZtmhm8Lg2rEcL2tuyjSqtQxrWOSizSNgq26Liym24Y50hMAFMn816zCZ7NY-zisp4CevGwnaYCrEMLs_ZicZBm8v3XUQA2b2Y89sUBccdOK5CPblj1ByoROXKey6TS4xpoZ4ebTb-Sh3xIxZwItkNuGU3XrHIZ6JVIzKpP-ro6iDJ44bnMtEhH-87iD6hrOqfDQju2DjyV1IDOn7VrjHVdNSkqV4_3m4Kjw0fTqBOJcCNi7YyjtTZXO-lpW3McwRHijIATipnJarNSxi6dfu4a9INXy0hxDVoE1F_H31TgZGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س:
قال باراك أوباما للتو "إذا وضعتم النساء في مناصب قيادية في كل حكومة لمدة عامين، فسيكون الوضع أفضل". هل تصدق ذلك؟
‏
ترامب
: هذا سخيف. أنا أحب النساء. أعتقد أنهن رائعات. لكن يا له من تصريح سخيف!
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91684" target="_blank">📅 18:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الطيران الشراعي يرفع في سماء العاصمة العراقية بغداد صورة شهيدنا الاقدس سماحة السيد حسن نصرالله في ذكرى شهادته</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91683" target="_blank">📅 18:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇷🇺
ماريا زاخاروفا أن الجانب الألماني طلب عقد اجتماع بين وزير الخارجية الألماني وسيرغي لافروف</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91682" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91681">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=VQ68AX22NoMAudfn-GQ2lp2iH888xQQrEyYUGE8a7uA2wKeN7LwVqJYtwYfD8iWNgM7LCjdZCOxy5q-vVBrq36DUIoJUOIrEaksp6W3O1WHczfK-N96pi4fvb2-YoQYEwT-2M6z_Y4RBmNKIR7SmQHRocP5Yg-62Mq-yHcGn6ckygVjoQlSHupdzn4mJvqYWOCmQXAOn8DzxfkytTsYKnLLME0kqNzsBSV_15KlKbgXTxREgn1J1kJmPNLj8rKavZSlmrOhBvZd3zBOBnur3Roua6WdHjTvScA-Hu-GMDWAL0z3wBEtjtqxcfPBUxCXJXeTgjLkMOr0bJWN-RMIC9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da57ede6e8.mp4?token=VQ68AX22NoMAudfn-GQ2lp2iH888xQQrEyYUGE8a7uA2wKeN7LwVqJYtwYfD8iWNgM7LCjdZCOxy5q-vVBrq36DUIoJUOIrEaksp6W3O1WHczfK-N96pi4fvb2-YoQYEwT-2M6z_Y4RBmNKIR7SmQHRocP5Yg-62Mq-yHcGn6ckygVjoQlSHupdzn4mJvqYWOCmQXAOn8DzxfkytTsYKnLLME0kqNzsBSV_15KlKbgXTxREgn1J1kJmPNLj8rKavZSlmrOhBvZd3zBOBnur3Roua6WdHjTvScA-Hu-GMDWAL0z3wBEtjtqxcfPBUxCXJXeTgjLkMOr0bJWN-RMIC9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لقد كان لقائي بالزيدي رائعاً.. إنه رجل رائع وصديق جيد لي. لقد دعمته، أليس كذلك؟ أعني لقد دعمته، رئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91681" target="_blank">📅 18:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامب:
لقد كان لقائي بالزيدي رائعاً.. إنه رجل رائع وصديق جيد لي. لقد دعمته، أليس كذلك؟ أعني لقد دعمته، رئيس الوزراء العراقي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91680" target="_blank">📅 17:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
🇮🇷
السفير الإيراني في بغداد محمد كاظم آل صادق:
من المحتمل إعلان قرار جديد قريباً بشأن الرحلات الجوية إلى العراق. نحن على تواصل مع المسؤولين العراقيين وقد قُدمت مقترحات في هذا الشأن.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91679" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامب: ارفض المقترح الايراني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91678" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91677">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91677" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91677" target="_blank">📅 17:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91676">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMes6fHu4JUqNnBm_yNErWQ6mmaqWmmB8bFRHVkdfDt37XWs6wx3OS2ZUh0RYJaOQb1pBGWYwCZblXYUTaZZO6P1ulRBGCafQrtE4VExacRjnILozHcPFc-JDQhb2u90iShVIbcUM26L9Z54SMpQw3VdB-a3U6QyurVlbivqbii3invVt7dkd_KDYBBpTQ6WVXS5kDa1prRxKBuBGAltHalx63jmw1eAo25VJreGYxYftyuqK8yMy8c1c03GeUMxdSrMUWS_LpjmieDUFk5lovWnMe12Fots8a2F608cFjiMAb1GqsXVMKqWtbEdOq_ZeFm18X1zvIhpvufHUxc93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي: العراق ليس ولايةً أمريكية ومطاراته ليست ملكاً للخزانة الأمريكية وقراره لا يحتاج إلى استثناء من أحد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91676" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91675">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامب: ارفض المقترح الايراني.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91675" target="_blank">📅 17:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91674">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dbf96a66.mp4?token=X6Bxp8ySqVss2bKHhMEKI73ld8DZ0wU3nG5D8pCWaO9orELx17bqu7g57fDpEkORItGs20wUo_Hei9RJFRWwzia_CUV5Qc9km8Fq6Krh7N8bJmivGFULp3EGe-o5X-480Hpfn_lVhy7hzfAslhn6e0RE--GUjL-Lw7SbL9Nn_anxl6ElCWUQ9AMpjEp1v2nFM_UH2Pryzde639gswl2uOYqGNNThXTYihgXPNLOgWquiniP4hldfH9hEDbZWj4839bvOeEXxTh0c-Rr8QAxsFe9C7gLU85E0WO4pugXtKjjtdrmTmOGyVeLskAnRZ69niir7Yycm2mudxHxLI0zSzDcK4N9faBfy3bxSVHhYNLBagyxduq1xZkqSeG5dREI9KqBAjnbtv4-VYj09ix8nekN3PnH3KSSJKEDl40QmIlB9lh7YEtIatnWcTlWDQtyg38L98JDpzwPS6EIO-4LF8lcDeoBwD0kNKSf8HkcGNdeCPF0YaY07aIDW4y0JVRxL14aMgrREEVALlGTBTANuoINGh83K1_-BnDGuVUfbuNhp6As54AFKPYJ-UQHIzwJeNfDvqGRFmdL9PlpTpgjDduv09b0X-R65VeubvKTV0TMXEIdMwx7dXVqS2ycq8am0cVNI0D3922j8xawp3ipu6qh3xJgwCJ6uF9ONRQ-ZNoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dbf96a66.mp4?token=X6Bxp8ySqVss2bKHhMEKI73ld8DZ0wU3nG5D8pCWaO9orELx17bqu7g57fDpEkORItGs20wUo_Hei9RJFRWwzia_CUV5Qc9km8Fq6Krh7N8bJmivGFULp3EGe-o5X-480Hpfn_lVhy7hzfAslhn6e0RE--GUjL-Lw7SbL9Nn_anxl6ElCWUQ9AMpjEp1v2nFM_UH2Pryzde639gswl2uOYqGNNThXTYihgXPNLOgWquiniP4hldfH9hEDbZWj4839bvOeEXxTh0c-Rr8QAxsFe9C7gLU85E0WO4pugXtKjjtdrmTmOGyVeLskAnRZ69niir7Yycm2mudxHxLI0zSzDcK4N9faBfy3bxSVHhYNLBagyxduq1xZkqSeG5dREI9KqBAjnbtv4-VYj09ix8nekN3PnH3KSSJKEDl40QmIlB9lh7YEtIatnWcTlWDQtyg38L98JDpzwPS6EIO-4LF8lcDeoBwD0kNKSf8HkcGNdeCPF0YaY07aIDW4y0JVRxL14aMgrREEVALlGTBTANuoINGh83K1_-BnDGuVUfbuNhp6As54AFKPYJ-UQHIzwJeNfDvqGRFmdL9PlpTpgjDduv09b0X-R65VeubvKTV0TMXEIdMwx7dXVqS2ycq8am0cVNI0D3922j8xawp3ipu6qh3xJgwCJ6uF9ONRQ-ZNoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غضب شعبي عراقي في محافظة البصرة بسبب حصار الحكومة العراقية للجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91674" target="_blank">📅 17:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91673">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مشاهد من محافظة البصرة خلال الاحتجاجات ضد الحصار الجائر ضد الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91673" target="_blank">📅 17:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91672">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c94d716d.mp4?token=l6jb5ToYQqayRQLyif2vbjb2m5ovz3_pHx9Z79fiDxXM4Thddd3EoU0SYEskBQOvyOGI4cbr_8Qh6pBzuUl_skbrJjBN5pYq-nqKueagNNtLTeLj7Jk-F20PLc4IXRy4afSF1w5e-epkQc__Qh5IolwwLQPWmxqcVm9QEo3Te-AnEpsxwBft7NLTY_Ko0hFsCr-_xPWv2VL7B1iY3r2s-_VetGaGjljPYSHwtOm45pNY9GOlLoxXdASjeu7SkJU7kjpNSz18XKKPJEzI1Fqf1NDfjgFgI7Ia2JUt0lO2C5UGS6x_0FRAhJ2thIet0Mc62keZ6gSMVHBlosZrYIF_NXCVcGxy24gKm6xF4dpD9JPrIZlZ-2_cdmuipFoBJp1qL66LNoOERxVlUvDRhmZrwz0UFboxZopiLyInWrD-Hi35wrOC7Goce9qNabIha9Si4iNrspEnyriJpY7Fya1X09Z4pfnW5vJ7Fvitt-nBZrlt1OQtMOmATZ7jTc37loOnqDogzRnKFiW7HU6V9lIubsdoRqdZXkcMV3pyogd8ED_WTCAWxrjcx3jZneK0sUxiAj00k8CjR2qHolRaSxjSWkBXUU4cIRQUjTofhL6zaNNVaTlzkWL2Yvvuz2vbE_4xln2qsSKEPKKlELvDQb4UZK2tf8pGXpZBq86XLyNBFF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c94d716d.mp4?token=l6jb5ToYQqayRQLyif2vbjb2m5ovz3_pHx9Z79fiDxXM4Thddd3EoU0SYEskBQOvyOGI4cbr_8Qh6pBzuUl_skbrJjBN5pYq-nqKueagNNtLTeLj7Jk-F20PLc4IXRy4afSF1w5e-epkQc__Qh5IolwwLQPWmxqcVm9QEo3Te-AnEpsxwBft7NLTY_Ko0hFsCr-_xPWv2VL7B1iY3r2s-_VetGaGjljPYSHwtOm45pNY9GOlLoxXdASjeu7SkJU7kjpNSz18XKKPJEzI1Fqf1NDfjgFgI7Ia2JUt0lO2C5UGS6x_0FRAhJ2thIet0Mc62keZ6gSMVHBlosZrYIF_NXCVcGxy24gKm6xF4dpD9JPrIZlZ-2_cdmuipFoBJp1qL66LNoOERxVlUvDRhmZrwz0UFboxZopiLyInWrD-Hi35wrOC7Goce9qNabIha9Si4iNrspEnyriJpY7Fya1X09Z4pfnW5vJ7Fvitt-nBZrlt1OQtMOmATZ7jTc37loOnqDogzRnKFiW7HU6V9lIubsdoRqdZXkcMV3pyogd8ED_WTCAWxrjcx3jZneK0sUxiAj00k8CjR2qHolRaSxjSWkBXUU4cIRQUjTofhL6zaNNVaTlzkWL2Yvvuz2vbE_4xln2qsSKEPKKlELvDQb4UZK2tf8pGXpZBq86XLyNBFF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بغداد تنتفض ضد الحصار على الجمهورية الاسلامية في ايران</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91672" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91671">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e8cf94bf.mp4?token=U84XPCbv23aba47sEB-R9PnkLkO77KenHPoA9Qur5vx3HbUjipViBr05Kw6EGVQYsbNgx-303Q8MfjuCIBdHMXOTJUM8OKgJ5q043AVa8mGd_TZUnvs8ldV_oipkkSivs0192GUpr7um_x1YfIaYBWFbBMdhChg7VDmsU0qO6PQYmxFB14G1q98tBC8_3Y_ILQsuv0uzh2jF8Ckxahxot75C236hvJyq7x2HYhdXj9wlgerhANqTdJ3EClbXgUHp0_i-932__xfyIqUzLGhmfFLdFGf6JHiSG25-WXxq6IBGxBt52rKjo9kN0mUx8c1JFYxjxMaS_eFbQvSQneIAUoJ6pjQtbGnPdNGcVr1hgQ-AjQDrQDwdNNcvc6eeYsdQuDRxIV0CSKINRh2JnqNcQqgaM2pCnlXAzFoYrGClIKVZegMAz6UtX7rgO79P2nLrv_7d7qQHxtY25-vETqFl5K4JQ0aAAtEzED5OgCd-vgHiKbK4IKhX0P5pQso_UvY3xZUqA5eZp5wv-PGYSGvxpIOPCTVDd0hTmidYGZd9QAz8FOGtBcC6A0fP8viVYSu8FLR_YZhU6DbVwoTh5S7-ZcEsioYE7bzTRZYgIl-J-w09m0sjnR6iW1_jFIBCTMrMasWdtXb6AK4HfUX52dSrIT1DUBtn5MB_UNrxrZiq4B4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e8cf94bf.mp4?token=U84XPCbv23aba47sEB-R9PnkLkO77KenHPoA9Qur5vx3HbUjipViBr05Kw6EGVQYsbNgx-303Q8MfjuCIBdHMXOTJUM8OKgJ5q043AVa8mGd_TZUnvs8ldV_oipkkSivs0192GUpr7um_x1YfIaYBWFbBMdhChg7VDmsU0qO6PQYmxFB14G1q98tBC8_3Y_ILQsuv0uzh2jF8Ckxahxot75C236hvJyq7x2HYhdXj9wlgerhANqTdJ3EClbXgUHp0_i-932__xfyIqUzLGhmfFLdFGf6JHiSG25-WXxq6IBGxBt52rKjo9kN0mUx8c1JFYxjxMaS_eFbQvSQneIAUoJ6pjQtbGnPdNGcVr1hgQ-AjQDrQDwdNNcvc6eeYsdQuDRxIV0CSKINRh2JnqNcQqgaM2pCnlXAzFoYrGClIKVZegMAz6UtX7rgO79P2nLrv_7d7qQHxtY25-vETqFl5K4JQ0aAAtEzED5OgCd-vgHiKbK4IKhX0P5pQso_UvY3xZUqA5eZp5wv-PGYSGvxpIOPCTVDd0hTmidYGZd9QAz8FOGtBcC6A0fP8viVYSu8FLR_YZhU6DbVwoTh5S7-ZcEsioYE7bzTRZYgIl-J-w09m0sjnR6iW1_jFIBCTMrMasWdtXb6AK4HfUX52dSrIT1DUBtn5MB_UNrxrZiq4B4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ التجمعات الشعبية في محافظة البصرة احتجاجا عن خضوع العراق للاملاءات الامريكية وحظر الطيران بين العراق وايران</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91671" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91670">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة   بداية كورنيش جهة التعليمي   استعدووووا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91670" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91669">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1be51000.mp4?token=C38gMc6m-skkgR516bn9_hQqUtAPtvjzpgLjSAzkOpNo50fNBvNcjJ37BNDWpiLuur8pU8wZCMumL5m88uK1IUzv4qsSTvArf3Wh2UMF7lLF7vRN0xVH_DYjYApHD_uSdJqWW4inwf_jVhkGOlML09vTEjx_vIqNgZhDIsqnwly8XpslxzU-4lX2E74LRQEmMOEyHaD-iGWvsfAVAbvCvh4OzksGYbOESvdkqMKkw1x2Azm3CFD32CVPI9F58HmEc7Q8-OG95KQVYMDmxGqepbFbzMmz7rWXd4gcQ5MULQMa_6-XeQAVatEQQprADeLoSQ-MsGhCdRxLIamIjWdqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1be51000.mp4?token=C38gMc6m-skkgR516bn9_hQqUtAPtvjzpgLjSAzkOpNo50fNBvNcjJ37BNDWpiLuur8pU8wZCMumL5m88uK1IUzv4qsSTvArf3Wh2UMF7lLF7vRN0xVH_DYjYApHD_uSdJqWW4inwf_jVhkGOlML09vTEjx_vIqNgZhDIsqnwly8XpslxzU-4lX2E74LRQEmMOEyHaD-iGWvsfAVAbvCvh4OzksGYbOESvdkqMKkw1x2Azm3CFD32CVPI9F58HmEc7Q8-OG95KQVYMDmxGqepbFbzMmz7rWXd4gcQ5MULQMa_6-XeQAVatEQQprADeLoSQ-MsGhCdRxLIamIjWdqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">البصرة ام الشهداء  تقول كلمتها عند الرابعة   بداية كورنيش جهة التعليمي   استعدووووا</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91669" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91668">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B50jF5PYJnNtUN2VSFlb5xDL1hJNVzhI8SELR04zVuUOZFGmhA1YmbCr24uzkMiDWcV1qIyy5E7uEcuyrh-Isbzr8BTzRnIZDsDUz2dDArp98HcUaA-YvTbbDkVNeb5R5jMT0wMWrbbmTTxwOeTs0RjpglIylughqqqgwu-SJ1iPp3ogaOll8h7dc789Dkiyd-6N5UI3WBR0517XhW8QMddIB_xgsgNYQn7rUKa8sEo-7lQ5C1JW02OK4WYIZgQVGVxAOs07kXUyuyS4SgB-DA2fGct9scjv0fAlc7-hbbGhJy344zSDGidxj95saBhj3EedtXu3nbF3RJBynSccyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشركة العراقية المتحدة لخدمات المطارات والمناولة الارضية المحدودة المختلطة:
لم نتسلم أي توجيه حكومي رسمي يتناول حماية مصالح الشركة وأموال مساهميها. وعليه، وما لم يردنا توجيه حكومي رسمي يوفر الضمانات والحماية الكافية من التبعات الناشئة عن إعلان وزارة الخزانة الأميركية مكتب مراقبة الأصول الأجنبية OFAC الصادر بتاريخ 8 أيلول 2026 وذلك قبل التاريخ المذكور، فإن الشركة تأسف لاضطرارها إلى تعليق تقديم خدماتها اعتباراً من 2026/9/23 لشركات الطيران الإيرانية المدرجة في ذلك الإعلان. وكما أوضحنا في كتابنا المرقم 1855 ، فإن أي تعليق من هذا القبيل إنما يرجع كلياً إلى موانع حوكمة قانونية ومصرفية دولية قاهرة وخارجة عن إرادتنا، وليس إلى أي قرار تجاري من جانبنا، ونؤكد التحفظ الوارد في ذلك الكتاب.
إن الغرض من التعليق هو حصراً حماية الشركة وأموال مساهميها، بما في ذلك المساهم الحكومي، من أي تبعات قانونية أو مالية أو رقابية أو تشغيلية محتملة، ويأتي ضمن مسؤوليات إدارة الشركة في صون مصالحها وضمان الامتثال لمتطلبات العقوبات ذات الصلة. كما أن التعليق يقتصر حصراً على الجهات المدرجة في إعلان 8 أيلول 2026، ولا يمس بأي حال من الأحوال خدماتنا المقدمة لبقية شركات الطيران، ولا سلامة وانسيابية حركة الطيران المدني في مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91668" target="_blank">📅 16:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91667">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">العامري: نهيب بالحكومة لعدم الاستجابة بهذا القرار الظالم</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91667" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بدأ كلمة العامري في ساحة التحرير</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91666" target="_blank">📅 16:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بدأ كلمة العامري في ساحة التحرير</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91665" target="_blank">📅 16:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2695180475.mp4?token=Vnx6YvEmW-Nk_Apbnxj5OyIOhB2NNckTzm48R6IJ1e6e553MqBp-vx21c9_YQXJpOjmlzbQMaitCHsanpNQn_sBHf374BRyesjKr3Zzc-JtkqIBn8MZYh9PccSjCEtOPnt3lJ-Mv0miNXDFdlE4OXBIFdrEaixuGmjOZG80MIqPPvLP6smh3MbSw-tXrEk5Q2cMEy1EkLjrSCH8nc_I081OF-ahf0Peq5D41QOt9k9Z-1LH8Coz2vhbLZjUnEY5HmUmDCjXxq9fcgFrKUEZKAX7jx3u1ZrQk3Mow9E3XBJz62Qt7mRCfzIJDc2lozPbRY8CYHeR_l5Qb8oIfoQNlc4gKudzKSiNwdrxhyeO6-bPEtL2UfAw5JOMgJhH27EIWb7LSZ8JWL6DzIGcp4nuII6mozbJUFq0_hpGw_fdwfNjQe79cD5vgu0O5-EaMpMuRYan76NWb-qJPHl8xMAajIXKXHpRodM9BQ3lLaAmSOtcIUdjk9h-NIC0anhogYlZaibYYuo7WboFYjX_OjPRTNo5ko1qRbfMBTROsb5GVWkKj5O6cinXFVWIEDCoMVdzVP87RCZnFq1TqnSnmaH-kihlLNPyCY2inFmXliZU2NC8qJGusn8Bc8vrivzB6dnh6Rsnj9tY7Yt3Yq5m1KCNEu0MH6Gyvp3CVScuGA3LCkSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2695180475.mp4?token=Vnx6YvEmW-Nk_Apbnxj5OyIOhB2NNckTzm48R6IJ1e6e553MqBp-vx21c9_YQXJpOjmlzbQMaitCHsanpNQn_sBHf374BRyesjKr3Zzc-JtkqIBn8MZYh9PccSjCEtOPnt3lJ-Mv0miNXDFdlE4OXBIFdrEaixuGmjOZG80MIqPPvLP6smh3MbSw-tXrEk5Q2cMEy1EkLjrSCH8nc_I081OF-ahf0Peq5D41QOt9k9Z-1LH8Coz2vhbLZjUnEY5HmUmDCjXxq9fcgFrKUEZKAX7jx3u1ZrQk3Mow9E3XBJz62Qt7mRCfzIJDc2lozPbRY8CYHeR_l5Qb8oIfoQNlc4gKudzKSiNwdrxhyeO6-bPEtL2UfAw5JOMgJhH27EIWb7LSZ8JWL6DzIGcp4nuII6mozbJUFq0_hpGw_fdwfNjQe79cD5vgu0O5-EaMpMuRYan76NWb-qJPHl8xMAajIXKXHpRodM9BQ3lLaAmSOtcIUdjk9h-NIC0anhogYlZaibYYuo7WboFYjX_OjPRTNo5ko1qRbfMBTROsb5GVWkKj5O6cinXFVWIEDCoMVdzVP87RCZnFq1TqnSnmaH-kihlLNPyCY2inFmXliZU2NC8qJGusn8Bc8vrivzB6dnh6Rsnj9tY7Yt3Yq5m1KCNEu0MH6Gyvp3CVScuGA3LCkSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدوا   العامري سيغسل عار الإطار بعد قليل</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91664" target="_blank">📅 16:42 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
