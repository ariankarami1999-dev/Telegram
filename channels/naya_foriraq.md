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
<img src="https://cdn4.telesco.pe/file/fa_wDvOylGmB3rDkk1WpTJkxvA_vDux-MPCDPZfOkfKQJIlUYPOcRuXJmCieyHGh3oWXNfr4jGIVMVLuppsvlK7iCdqkcD4kjEDH4Q1mWao91Y-HaVCfFD6GiKcKn7mFW8W8KgObvyxPQuTZ00timZnhW9naMoP7RjvImgPqSsWgKZW4NMXO2GeDkvvMyfWusanh5xvfPtt38FD0t4bgdwTOh7q3AxGm7DS8ssyPWbZazTO3xMHevjiNJlo2KNo4qcF9IM9d0zlV1SmW2NZKClsDI33EpApdRCVhXj4Mi0Q9cJAtzZEBZOV18gnpOqj4t84RjLd-Xk22vOO8b3U31g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 12:48:11</div>
<hr>

<div class="tg-post" id="msg-88308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇾🇪
🇸🇦
مرتزقة السعودية:
الهجمات الحوثية أثرت على ميناء المخا وحركة الملاحة.</div>
<div class="tg-footer">👁️ 658 · <a href="https://t.me/naya_foriraq/88308" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
قائد لجنة البحث عن المفقودين الإيرانية:
الوضع الصحي للطيارين الإيرانيين في قطر ليس جيدًا.
مكان احتجاز الطيارين الإيرانيين في البحر لا يوفر الظروف المناسبة للحفاظ على صحتهم.
يجب على الحكومة القطرية نقل الأسرى الإيرانيين إلى اليابسة وإلى مستشفى مجهز في أقرب وقت ممكن.‏
ندعو الكويت إلى إجراء اتصال أولي بين الطيارين الإيرانيين وعائلاتهم.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/naya_foriraq/88307" target="_blank">📅 11:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88305">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇶
رئيس الجمهورية: هنالك تسهيل لبعض البواخر التي تحمل النفط العراقي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/naya_foriraq/88305" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88304">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية: إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/88304" target="_blank">📅 11:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88303">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
مراقبون يگولون تغريدة " لخ " أخرى إذا صح التعبير من ابو مجاهد العساف والجماعة حتى باميا للمواطنين بفرحة الزهره يوزعون .
النجباء مسوين شده يا ورد وزيارات وكذا على قادة الإطار التنسيقي مرتاحين لشوفة العامري حتى واحد منهم گال جنه يم هادي الكعبي مو العامري .
خبر " فصيل مسلم أشياء للقوات المسلحة العراقية و الأمريكان كانوا حاضرين للمشاهدة خبر حقيقي  " .</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/88303" target="_blank">📅 11:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88302">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
لا توافق بالآراء حول حرب إيران وحل أزمتها داخل البيت الأبيض.</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/naya_foriraq/88302" target="_blank">📅 11:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88301">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية:
إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/88301" target="_blank">📅 10:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
"توم باراك" بخصوص الشرق الأوسط:
أُرسل جميع الأنبياء إلى هذه المنطقة. ليس إلى منطقة البحر الكاريبي، ولا إلى أمريكا الجنوبية، ولا إلى أمريكا الشمالية. ‏"إذا لم يستطع الله نفسه حلها، وإذا لم يستطع الأنبياء حلها، فإن فكرة قدرتنا على حلها في العام ونصف العام القادمين تبدو ضئيلة للغاية."
توم باراك صار يكفر بعد فشله بحصر السلاح في لبنان والعراق واليمن وفتح مضيق هرمز
😆</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88300" target="_blank">📅 01:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي وإنفجارات كبيرة تهز العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88299" target="_blank">📅 01:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7xOY3XMa5JfXgI5fChmWrHv7LJxrGxAYrpoYvhR-pIJclmhjcvYty2PWY-UQwYU2TRPZBxd9XP_0syXPS6kkQXokIOyTLSSKrMv7vttzvra33Rfj2pTgL7XR40wXW-2-w133Aoe2aGATLvZhjkqLBpZ9Bz-UXPtuMTWv-BTA83CIkq94zMGsFcBXt0BKIk5KJjqDFU5oSyaRyCoxjoUE5EChjILWwsz8Ar5NJtJlxPuAwFCGr8E64i63eryj8M_Cj0RYHGrh7-xqsRsXqmywnS_7CqIZulJraBb86PkxPYfgNz8cf4fUccx1jt1aY4oKBzjGTfeEbejwT3kc4pv4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
طائرة مقاتلة من طراز إف-35 إيه لايتنينغ 2 تابعة لسلاح الجو الأمريكي تطلق نداء طوارئ على الرقم 7700 فوق الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/88298" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=uxNS0L8UuNvjXjnthcKpYPUxS2-n9T__JRdI2qfFROzGc26LYKfQh7qT1MOElSjYmVCYVNLEcx7PXks42FpxA59-0ad1OY-CJIWZ1J7tRBudx_37_I7W2_2kBYvZNGvtjeYHdGDlnQ6pXph0MAlJlUnp3nFjB0bGNkP9S1jRg2IqSM-h8KTatnsKPxx5380a62IMyVcNL7eenOY6HiD6g-sf8Mu8woGQzi5EyuMV68l9rmXxQkhWzBpdP7bpt5XkKbBkUYovz5TuSQgCKZRGCmjEw0UAKgHzykirNviGELwaBZ1yu2rKezyZPQmU7SFnlXiMHMOqxWYqQovG9xD-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=uxNS0L8UuNvjXjnthcKpYPUxS2-n9T__JRdI2qfFROzGc26LYKfQh7qT1MOElSjYmVCYVNLEcx7PXks42FpxA59-0ad1OY-CJIWZ1J7tRBudx_37_I7W2_2kBYvZNGvtjeYHdGDlnQ6pXph0MAlJlUnp3nFjB0bGNkP9S1jRg2IqSM-h8KTatnsKPxx5380a62IMyVcNL7eenOY6HiD6g-sf8Mu8woGQzi5EyuMV68l9rmXxQkhWzBpdP7bpt5XkKbBkUYovz5TuSQgCKZRGCmjEw0UAKgHzykirNviGELwaBZ1yu2rKezyZPQmU7SFnlXiMHMOqxWYqQovG9xD-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:  إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.  لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.  وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88297" target="_blank">📅 00:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=JiglLR-ulZi8ri3qCHksV4ST1TBIkgOTmZ-HMtyFjTNpDRiS4l4w5wlUzQcFCQtli6bbAfTSyctF6Nr4JCzOyHlgIB_667w0PQxUrZO-ArMDLh5rQfBYhbQAGdSyWFAqUxu8gnIk4L3ydNq6S9C1pBplqEfV8eG3wxBeBJVHQcddYZXKe32lyO5bJPfCZVHaDuhW_2GHNlN3Cp1V9mRkdMRUqAMHc5iXYHX7q24cw0NEtAcGvGQ2-OITpCLLSVSgwVqqLiMvcCtdtisgFEA0auraB_tcU5c6HQWUj8HmS4jUnANVxvaIVjVTN5z3qlzft5JQOUAf_xw9eOB3KqO9-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=JiglLR-ulZi8ri3qCHksV4ST1TBIkgOTmZ-HMtyFjTNpDRiS4l4w5wlUzQcFCQtli6bbAfTSyctF6Nr4JCzOyHlgIB_667w0PQxUrZO-ArMDLh5rQfBYhbQAGdSyWFAqUxu8gnIk4L3ydNq6S9C1pBplqEfV8eG3wxBeBJVHQcddYZXKe32lyO5bJPfCZVHaDuhW_2GHNlN3Cp1V9mRkdMRUqAMHc5iXYHX7q24cw0NEtAcGvGQ2-OITpCLLSVSgwVqqLiMvcCtdtisgFEA0auraB_tcU5c6HQWUj8HmS4jUnANVxvaIVjVTN5z3qlzft5JQOUAf_xw9eOB3KqO9-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب:
إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.
لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.
وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88296" target="_blank">📅 00:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV2X-5ZnPKuDeNMOUvx5zb7H0m4HEemuy4UR35oQW5eF9SwvWayjR7cBsQLQRc0foG1Fu5oFNiK3WB3PSyK9jh0K_ZWLVw17pVNeDxAj1XtttRBA6ndQGIVv3zZ78BjbXjJylTw-zBwrLJ64YHKGGnlIM9a3Y6YDvlHfKpFNtJZ5Mr_qR2jsGUNwK4-nkuy_jXfL5Q_Ti9oK-ixW6Lq1kCWX2THgBmj5fpbAikRrbw0coZM7hkeVP9oIkyxXnxLddSPLrJhfSdSeBmW6yU7q-lS6cdzPOcDUc6doQtQITC21GOjANWDiiuohxBWyoCrHgtTfkNUuMnplQ_u_HJv8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
نحن ممتنون لقرار المحكمة العليا الأمريكية.
المجمع العسكري/قاعة الاحتفالات الذي يتم بناؤه على الأراضي المقدسة للبيت الأبيض، وهو أمر بالغ الأهمية للأمن القومي، سيكون الأفضل على الإطلاق!
إنه شيء طالما رغب فيه الرؤساء على مدار 150 عامًا، وهو ما سعى إليه الجيش خلال المئة عام الماضية. قريبًا سيتحقق هذا المطلب!
الأعمال الإنشائية تتم ضمن الميزانية المحددة وبوتيرة أسرع من المخطط. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88295" target="_blank">📅 23:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGN-8h4tNmPo7hrz88NYY0s__X07YOzyIMFK034wM3SROynZNAGn9p1qzrVd4n4GL86GE89WG-P04YCl_KZvU319MHhcS8TnUTd2mtJXgVR4JTVMpUlljT01vwPXWPwJRd2278SXccZbVfy-tuUWiFKsl21GSTSQUP3V5tZcKQMXMqGz7uomtS1WkR8o1fYvPuvVYhSW4_O0NVfSLNl7MOnIssG8adpsjnx3nnf43z6ayXIoqV754obAC_ftc07S28nlpUoQk6FOfAAKaFMY-Xi6XB4ik8kcWZeC8vPYEYhcMrakNOY0jzLh1gqKAYNnh0xBS22fXdLG0H0jdBaqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
الطيران الحربي الإسرائيلي يشن غارات على مرتفعات علي الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88294" target="_blank">📅 23:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
الجنرال وحيدي:
لن يتوقف الأعداء أبداً عن إضمار الكراهية والتآمر ضد هذه الأمة العظيمة.
سيستمر تعزيز إنتاج منتجات الصناعات الدفاعية والعسكرية، بقيادة وزارة الدفاع وجهود القوات المسلحة، بذكاء وسرعة ودهاء أكبر مما كان عليه في الماضي.
هنأ القائد العام للحرس الثوري الإسلامي وزير الدفاع بالوكالة بمناسبة يوم الصناعات الدفاعية في البلاد، مؤكداً أن الحاجة إلى الاستمرار السريع في استراتيجية زيادة القوة الدفاعية والهجومية باعتبارها الحل الذكي والفعال الوحيد لعبور المراحل التاريخية الصعبة وتحييد مخططات العدو الحالية والمستقبلية أصبحت أكثر وضوحاً من أي وقت مضى.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88293" target="_blank">📅 22:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPx9xg63W7d919AAMLK2SFTmp04uIo7ASAtRqfbEixlpctrfYm0lsHs7kXTHVOrsh1wlyNplRfwa_rhbmVGeEVHlTx2e6fs6D_6YLtDiMuyQPQu_VrCoFFIVpM3VR2xsNHEpbLC4CCLshYhcYUubpw56p7O2x-_aiBxRi_SMqYGnz04N5bdGZgaIUm01IkciALcPq8wZcFOQ2fBlyWA3bnR2ZNdfyPmsYYlTVUT5STBN3-NG_xtIgkMNLt0A6f09ZyyaPTdB6DNVMlhKEcz5J3BDVuqgcTvwy8ypW5WB5eIwXDKOJPB-Z0yXryMvk5w406bwLGoQWd7aK4OZgWn42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تفرض بدر نفسها مجددا في العراق كعرابة لمحور المقاومة على مستوى المنطقة
العامري يلتقي حركة حماس في بغداد تحديدا القيادي أسامة حمدان .</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88292" target="_blank">📅 22:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So_q34JrRw0Bg5gKOosbDJOZeq-Yfk6eKwXbexrGjjPYgh7SgZeE4kuHtn1g1mFBBQG043UoF2_xL5NBbNq62qEvc7-f7qvRUxrcl6Vr7-mqwjVDfg587gyujrDJuDTBhNXqxyWw09DG6PIJHQD6jbP1BirVJO2lEx3sVj-xGK1NfbSQsXuxNnRfpAQodJnC3-REr0k8fAuK3rnR4KmQ4eAmVT0vDAQLuk1bugG1VzZabzNt7GF3DLwqiixX1HD2wVZ88ODmRThoTYf_5HzYlUiUtyBsWzI0QIG8hB-Aq3G1BPAVlRHIH4B_6BKqwTI64-LCyjN3riufTrB3Cn_ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار خام برنت ترتفع إلى 94.39 دولاراً للبرميل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88291" target="_blank">📅 22:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3rQkSt_ZC3FOVHHk_Q6IYTfJ-04Dk6SSVup1pIdkpbaaM1I2D3MHERoDeok_6rLwXifxkRsWNHmDRJSXOl7Ut9t1vdj8vPJ6qIGMe7xfMCpmMIbNfFG2RLfViDfY-jGfBsxiIoe4cEZjrwcWrTgNxb5b6Cx-h-ywIzUefUvNLqtFXgrEekOH97CROT2R5-V-8ZbABOjtibh368apTtACS8nMJ0sDeSsXf32erV_idGEW6wSEGheUkfRPYdUOSO16Y74COVUvq5l0iJ-wwEHbHN6f_OQbMwJKS-MoReJuqC7qygyZLfLf898PbXCMMW04syygwGFzfxkBJg0b85dVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السلاح عزة وكرامة ..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88290" target="_blank">📅 21:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
يودّ فرع توزيع كهرباء شمال البصرة إعلام مواطنينا الكرام في مناطق المعامل، جنوب قضاء الزبير وغرب البصرة، أن سبب انطفاء محطة المعامل يعود إلى خروج خط 33 ك.ف عن الخدمة نتيجة عارض فني.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88289" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
طيران مسير يجوب سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88288" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس النواب العراقي:
رئيس الشورى الإيراني ابلغنا بأنه سيبحث استثناء العراق من مضيق هرمز مع القيادات الإيرانية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88287" target="_blank">📅 20:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
نفت وزارة النفط العراقية ما تردد من اخبار في وكالات الأنباء الأجنبية والمحلية ، عن تصدير شحنات نفطية عبر السكك الحديد لايران ثم لتركيا.
واكدت الوزارة ان عمليات التصدير للنفط العراقية تتم وفق السياقات التي تعتمدها الوزارة وشركة تسويق النفط "سومو" ، ومن منافذ يتم الإعلان عنها مسبقاً .</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88286" target="_blank">📅 19:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URxB5I-aVSg74WFu2Vd6TveEN8_SgYPvX35qlhEJD9ryPCxQF_dsTqWTphbBSTEe9RilmxukgtmIYPFYdGGW8wLSM3J2Kbu7B62M4RUqnt4KdAIT3S0ApUrq-D1B3YW_5WzsMkhTd8RCsMUPvRTf_ppZDlG_-Z8vW9Ohs1kc_0HvvU_6Ty8tyLaZmECFa7TBcsm-PZ1W5YM9xgN-9UUCohUpaQn9tDD-d4aTTABHdA4-Mz4hRXhnJFWesgMtPj67FJ_wqxLLIb5EMvMm73tVFoTIftgp08qV99p2tgjqlon6SsRHlCEqdBsYtpR9bATBJcoJwmnRr2AKXDiB4dK2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
عراقجي:
قبل 14 عامًا: "أكثر العقوبات قسوة في التاريخ". فشلت.
‏قبل 8 سنوات: "أقصى ضغط". فشل.
‏قبل 5 أشهر: "استسلام غير مشروط". فشل.
‏اليوم: "أكثر عملية اقتصادية كارثية على الإطلاق". محكوم عليها بالفشل.
‏لقد شاهدنا هذا الفيلم من قبل. نفس المشكلة. لكن المتنمرين مختلفون.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88285" target="_blank">📅 18:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇶
تنويه:
تفجير مسيطر عليه في منطقة البو حداري قرب جسر الإمام علي (عليه السلام) في قضاء الكوفة في محافظة النجف الاشرف وذلك في تمام الساعة السادسة مساءً.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88284" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88280">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YarEO44w41aWL-ziPcKxbguN24UmXfQfIhC_W6EoDE8x78Ss83_7UAixcyqV9mow2hKPi12abEKlqXrm5jPrrYTcLSLWHFhjQJF50Prz_PhJjZFsDkMwUBLX9f5voaiNuPj2HvPZekpGogJOC4Eu2LM2mnHS-sUvuFlbbFxiB18nIBZQZClk5YgYg9_8DFSWJQL02MqK9wVzI1H1-ms4YlvVo8g8muuaTlTp3PMtRZt9a8UKBYMBKatRmkmEUs1gBaITeW57yL-po1JvR2zGSE8BgmwbupnaqMulKO3m6gfg1p3A6KZChgGK_utaEdPaw1g_VG8AYSwN-amQC1H2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEnWr4AyiXXbWs6Tvp6WeiLOfyfXuZjZa7nuRDQi4jIROJIFdVqZ24OiFbL7BQzgVH-FT-mpeCJ_0-AUrL6HVosTEhlM8svB3eLKwcHTGyTVgSp3wF8IjsvIos3C3CpESaE6WMYfohentQXDo2PdZGSOrOC_3Si85WtydljmTzOIhcrmpAiyYN315PBoRZKEhDkVVouac-Iz_6Nh43DPmUkJXr00YgIe0EMJ0gse7if-EyaZBt8xyNOoVmTg4VuYj628k4wzupOX0rIjKLyzXpmmfUIGN4tIHrPYdY2_whLQSPDWkblbVuAMd-OAiyzebq-g8q1EpXyww4nDxd_xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu87MCfZWhxrA5vm_bqTFV0Y32d9rDEpgyokSPUQyQE_Biyj8ZayprlEhzyHxbXdpgo6CwVH1jnihreiRStgvyj86zI5UonBt-3mBjx0Qst8G4Dx2D3tlBAsNp6nFh7j48JXNfu7EKaAiKv1A1Q-nGaWF9ZG3MlZn-wgoXXyILfR1mEvJdbO9U9vkE0pA1IAs3eJ81dTQAXUFFJeI-8mmePVDWFHfYIshW06RjcFEQLLCOlbfELHbXdfpKi__v1kj_Ztdi3mzfYmNp9KCjqJLToF8Qqu0NapqKDnNC84DEgNSK59O7bRHDcZfaesxIOQmpAVccNYMMQzbKMLLeOtew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pj2d3kD1bx7Vy_EfGetoDD8z7RQfTJgy-8ikTBEebAXv-pCwy3MruG1o-Q_FSsOHbqOTZbA6_MOaiE1SbowvJTAFWVXhg_4CUK4Kz38o6p6c-c2BaL8gb4clRAVm2mSQRzTeBZZsM7HwFUtIzb8-iDexivQL4s-XxMFeqPlg4dAGJZqBYusNipek7kjyw3C6BmuOAF-N2s5_fu9HQf4wNEuc2RUraJm2TjNrJsFyD0K8tWSsRFoY1dJPcqte22OpzgaGRwJ88kvtV3v_vBM_EBX94FOWZZYTzBd5XUiMB4zetSSkpg--2RNiJryrzf0IsWYcDYBoCkhHycXFDbVhzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الحريق في قسم الخدج وسط حالة من الذعر بين الكادر الطبي وأهالي الأطفال</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88280" target="_blank">📅 17:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88279">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انقطاع الكهرباء ‏عن ضاحية عبدالله السالم في الكويت بالكامل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88279" target="_blank">📅 17:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88278">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88278" target="_blank">📅 17:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88277">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/88277" target="_blank">📅 17:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88276">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq0cph5___I688UR7cyorEoP0DNbX0uuIVe1PVJtxcSbai1Q_EJ3rmyqeUlt-7zVlcECb4fwa2HppYsN8Pw5rZAbgEPhZUPPv3pe4FYp69WPcjtkM__f0uLHxxUZt1bQBPc37el1uWavXCUuLqwPiOa62yGQ9NeyRPuJonK2B9lzf0LQUlzHqWo8_Z7G3LYChuVCURD21UwdaPpekOhWBCH6hvO8azVX8ES0lL4XjRU1b4Ugvgcn0bEkpg4DopUkJc8Y9p0VX9AZd5ImV7kYhvDsCFhUeWIcl6UHpZGxt6ELugjgn57yV74Bxl9dUf3Jn0ZAEZkJwdvI9yLZC6uGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاقمار الصناعية:
لا تزال حوالي 3-4 طائرات تزويد بالوقود جواً تابعة لسلاح الجو الأمريكي مرئية في قاعدة العديد الجوية في قطر في صور الأقمار الصناعية التي تم التقاطها اليوم. كما عادت خمس طائرات نقل جوي من طراز C-17 غلوب ماستر تابعة للقوات الجوية الأميرية القطرية إلى القاعدة لأول مرة منذ 12 يوليو.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88276" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88275">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88275" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88274">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=IUdwXvNgLghaRde6oSojcafzfxdsehpeujsGBxYm9-IDOZmzDrokecNSXyMpVkiZFeZ17GaM16KgMFKq79OMC22TS9EfWK3iuWKnxt6FJoePxt9rXjmFPfT0CEDmr2i6dWBFwz9Cic5N7E16GHzsqUR_NLUCh3Y_3h60S9R0DrtBRuY8ZDMw59F2QtaUqzDCsPAYRP3_ZtJkBGmGDe_luu36wt62iy-qekD-D0IMmDyau0skfcJZP5A6uMP9QvYT5SYf1eqLECYBOYdgrrz1XiJDOF_XAEzWhAkhoPSkV-vqbTHd_sPd_-9N2lwqNXlmrDMm2Rt2cu4qmAHvrWeljA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=IUdwXvNgLghaRde6oSojcafzfxdsehpeujsGBxYm9-IDOZmzDrokecNSXyMpVkiZFeZ17GaM16KgMFKq79OMC22TS9EfWK3iuWKnxt6FJoePxt9rXjmFPfT0CEDmr2i6dWBFwz9Cic5N7E16GHzsqUR_NLUCh3Y_3h60S9R0DrtBRuY8ZDMw59F2QtaUqzDCsPAYRP3_ZtJkBGmGDe_luu36wt62iy-qekD-D0IMmDyau0skfcJZP5A6uMP9QvYT5SYf1eqLECYBOYdgrrz1XiJDOF_XAEzWhAkhoPSkV-vqbTHd_sPd_-9N2lwqNXlmrDMm2Rt2cu4qmAHvrWeljA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تزحفلي تزحفلي وفاتح ايدك</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88274" target="_blank">📅 16:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88273">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=MNQaKF2zhWtXtNZpnDaMANksrU0JjYMdVSM5LfkqVvVfXwyxq9GSNtkBNUq0VUbH11OM7Q08YmrwlE2PT8UKpZmvZKlRTGW7pQAvVyr-IjMqdNBb--Y7-nd6w3uOTd_O6aEccJ2-EotsC1zhLOmTosnkyBHB1eZbtHqt-nma5fnrEAjV6QvR3ykgRMeVQQuLRjGuIBbiRNutKUMWtReSdBCNX07_K1CW8N09-E09JtQd2Dm5RU0XpYiwVx6NOzcrWAyMG4owSfcLzaIBERJp8PpIuLi8n3bYBmxR8Ozh6tb6Qj3lUdvgGqqs0MiUIzq7ZqtiJTBxjKV372bLHtFCLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=MNQaKF2zhWtXtNZpnDaMANksrU0JjYMdVSM5LfkqVvVfXwyxq9GSNtkBNUq0VUbH11OM7Q08YmrwlE2PT8UKpZmvZKlRTGW7pQAvVyr-IjMqdNBb--Y7-nd6w3uOTd_O6aEccJ2-EotsC1zhLOmTosnkyBHB1eZbtHqt-nma5fnrEAjV6QvR3ykgRMeVQQuLRjGuIBbiRNutKUMWtReSdBCNX07_K1CW8N09-E09JtQd2Dm5RU0XpYiwVx6NOzcrWAyMG4owSfcLzaIBERJp8PpIuLi8n3bYBmxR8Ozh6tb6Qj3lUdvgGqqs0MiUIzq7ZqtiJTBxjKV372bLHtFCLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88273" target="_blank">📅 16:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88272">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/88272" target="_blank">📅 16:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88262">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/colVTOysFV-__hRt6OUbXQfRNyMOBfIBo2XvuHAixsyw4F01usEMh4tNo3h23dEPnhG0Fbv1QVq30oBGxIpvZUywoc-bT_OeQ5fImHdLi-l2fVUuJ0k2v86qE2yQNkdRy6__S89uVZbFeoW7UjdKLki2AW0SgB_2F1ynlsmrLocHTHeOCPTrkdHRH9Mz7sB1xRqG2dLUI3LMDue7P88x6nNml2Pj113vGakycNfuf0FSKegGIaMZX0KpwAMCj58CQcH7zTsrxvngXrfUWhjyrptOpL48lJ3WLQ27QAcnWELjHrr1ku9pr3ZzE2nlRfGdqbEME_9xSe4TTsei-YD1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqzC4CdzxBhv7jDTIOu6hpiaAFJWPGiasIDWCYZaE-UamdVH2QmE7xtSILcWiROLPMrs36WXHo-D3AjQb86CnkL2i_mK-qZncHbSmSCZr9g92luyK4YPZf4CXZX42uhS7nOPSDUU9q2F9NokDb3JWnuxQWIBlc0lb4tR3Wpm4U4e8D4wZcR0YqJ9NlpcnBvFQYnbMLfgqO3HsFRZCj4rQwRZY2rPU1mdR1n3JJ5CBYbW-z1RvghRG-VWP8Xg9AqBKCSrgVC8mVKbMs8i-EO8WHs3_3qiDEZi8ZFeD34nIuXb-WZW2RXuX4kuDr0NHcQJ_VklxW7tsqnjuQchWSilLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azeb4QOEDdbXrZ5GeA6LuhQPfaZ4R92pF96YYIu94GISI0ZKbjXnbpUObOlZi9ZapJSbjSGWEXKlpwNn3Ua9qqZCpNluW-AYXds7I7c1QLomewFuUA0FZNP7MecDEyx9omcq77ZVuPOwfruMzNCDf1aimjDIRVrb9rirFlhM7o3jyq2Jzon83GkhWUqungbqxX7DSbRNGlXkti_8Wygwz7ccQeHSgWEHVEppkSl6NEar5-6L9HABVP19ttGOCr5hpa5xLrW3QSXvJMzE7D3wnr4lcpz3HyS2VmFV3DNahmnv4AqDzD4NLTYiqKN2DacbgERWjRCQwcvj6dXyCiQ0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgTI0FT-9-k2I8MNWIYoXEN9sdEbVFUoxbHrFyq5EfVqN6dBwIZfCj_FS3gME2GWDah_Bv7k8m1_QQ5fdED01KzWv0JOY-tQWoo498dLVLO4B8xrE7MqBwFfnpx1392QUwXZlupNzP7lInXUs3bHm-KrX5ueby7f_ZHhc0Z_XS8HTPRz6zMDMWjerxd0bHzEbwsYj12meXJArqcxBGW6tW7Q9CGddffTQDo3yj2OcH0hx2gVh_8gHZqim-wwi-LJgXNuLTTaVMPU0D92KeS6SASy2iJyGB9qPGpCaWGSr9hz6R3eblZNQ51yP_Pkebws7hNDjOxj1OFGgdqX3mRCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QCFp-xM0kPUoI1nz3xOazHhpteNXVdLDJ3_QZKCPZGXvE7RPPqX7Ny2TL69C660hI521U28Q_LNpeY17yrMyfb5gZgY5ghYW4kQXCpWcUJs0DPL9dDLcwkvTVRK0PYrIQ2AX30uZVX18XG5IM0DrvtMl0k176Nqwn-PCOp-cqGGS0f-hsBhhnKqtQDUhACvClQAgMS9Z1B1uaEf74Pmez0R2iVSOWd40ejrW0BYkua242OKkDU8th1mf41Gm4H6W-AfWRrK6DzqzVTB3YbxpHVb6ZgAi1SfP7LFyTfixibHRsfm2WBRXBYF2Z2GvDZMoc3MDZP0THck3guahY8tUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_dRzw82YKAC4yeqyB7CYTtBxXbq3rAUiOUrkp5md57HZdJrbQoGaKVGfEtjcoba6661g5Z_g9WrKw0g8ZizXhZBQQky9IMuxOt5WPkCzmar-i5whBWluJhC3XKnrcqXNcmQKoJCfKRaMFGL4wTU5b3rUC8qXbjnRbjhB80d_2pR0OKWwUkI0pYJmEOKFK9WF0nT6l1aXDdrdSMYj_W3djAIi3_QmAzv6Uf3M0vPfzZoJ8oRzDWCAINvVQ2sp0ZOcPTcrRzuERDnRadU1ELg1UWkyW0z27PG4j5dhgZdyWMZXyPqRF14E2zjF7y-RwMBMJNCooTa4yZFR5JuiYzRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jl_ulylkBIvmj4aR4NcC0d5LV7YPx9d8h-iRUGb1D8kyOBjbpJuH9qNBK1KPw5Yki2a7Dkvvj-YUh-3gcG4VdlVOw-JQ_QGYVF1CnHxX18fR9dDfzjOlqMZrT2j2v-IJHBVGk-tudJ5TH4_SU-AwMNWWAoWn6POizz_ICbm8IGJKMzwO5RNWZbLbiE7UkgOzhbhqpAWAnwjGkMyxI68Kb_WLXY7CnGHhsMHNXI96n69ZnwA69kieGjLrbgqvXMEbnEhG7117XdzKUlCu15-wq-OhPXIQwVGv-t25s9aeqM7rS2SL4x--uipnykl4psc_NKMVBaOT3h1jCJFFY_kdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFGR2NkhVxdFZxnBIv5ljJE4blOf8OBDXRWCgQq0NZTOb33JWxCY9guhkIhLw08CaR8LQe2Uv98hnE3TH2bxbIyh-M2ckXz5gsnmFqUcLVOAZM-ArzTw2GBasa5OrSQpfpp8rWiwkea26jD1r8H9RmUUZuwP7xtcLh89uXczvV62fuQcyLHA3m_Yro3TyXJFSy96k6JYPFzal3gCHEiWp89LAPN0o1DhiEO_oyY-huJId8QohQkLu72sQ-1iurlfQTymfEPULQ4mV3SjNm8F4jvPvPZzcf9uRfVIfIrGpW7aDk7_5QAB4kY4_5yG3njefIQvnwzXKokh2bAQF8nHyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5BjmvCwpFox-zdMsQnXWT5TmyI0ifDjfQCu2I-1HfB7C9sa4FSVu0gG9wJ8enO_Z_0e0jte9zIdBvC9FiudfOO0oSCEOFPUtWMGALTmU4wJxJ_T7wHFa8FR-LdTEj-5QG0UX1eFcGGJbaV_cAmiuS-QRSZ--NrcmL-xuqKlefXq9zUCH6RkLJCaXViJ1gy4UTqsN4L4S07lLDaE9j08ib9i0noU9qx5JY0XxyOqmQf-m98QzR-FVexZihvs8UEH2ETVoRdy5taiXhVEPejKVTXGQrASKkOHJMMtM0xB18a1gcRCGSIyvg3fjCoobluxmRJU_NVeybRTtapt8L-Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHm_X4UGFVWUgYRNa5WDo1-YF6JtLSSjD86g_yUZVl57Vv42UWZ2ePsQmkVvkKEbKddavdNQ6f4b6qYPblVr7Mz29SM8PAZATXm8P0WohGqIULXYPkMX5xWhTLf6cLyRM6NEHOtR6azeF89cO1U-sgLUtwVkLQghzwpDa0XZHR67jaY8xX97Mk3slyPBh487NyORJFeKB3Q-d9TRcqG9JyoOTLBT1OFP5h2VuBxTfeMRCvsy5ETC7zi23xssc_Fyg2J_2S08QT5x5sYma3nD0WTLU0FDrCju151Czaz6YI5cNtvSKKRwNGbpiV_SAXCfoixHBuX2ScTdPQvwciJkVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية:
صور من استهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88262" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88261">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULQBNRIQKlLWxpfVXvh820uQVqADILx0VYlWxr12qoJ3hJ3uGiEZHnvUc5vXOPPQMH4XdDFYGAVXTPWk4xSCuJ3xbomV6jvBIjMx11BbHiVA9Uxni5O8ybe4ezcQqhcxMsHGfn9f0r1Bd8S_zUE7UHfGf6VmDAxophnJ2BYTvcQafqEfjJTJzYF1rJ-_7X_9UB6N3J1kos9epUHe87Oq0yY8g-rHpTWOIcbHA7C-YTjZ9hB-SgV6TmfWNHuRnmn6Xn139678ohQCkCxTFtfUytqJxqbOBR5hJUQk5crRWi8J0AS9MnkdEKxOTF8uGmgBfGEXW0OU25F-JSH9qwyWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اندلاع حريق هائل في مستودع بالمملكة العربية السعودية قرب الرياض منذ أيام، ويبدو أنه يتسع نطاقه باستمرار، حيث تجاوزت قوته 200 ميغاواط. ويحرق الحريق بشكل رئيسي الأخشاب ومواد أخرى.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88261" target="_blank">📅 16:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88260">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98553c859a.mp4?token=Xmpm4m3-xiUB6QL0uu8DoE0aYXSO_8MVyxBJ2jh78GodNQ_InWObA3wq0zGIEgmvTN3Y3WlJxDQ-ZK-1ExW38u4fgoxBZjjKWZI0iJqfprhy7PJ-RF_1vEmmdzsKDkdHxLEOt6ea0VGkTNELnMXsbBlv-AZ7smJEy-9z4BBGKFnZbanKYLo0GzEWDXWQiwvs6XiA1NYzXGajuIUF9CJ8nKD4eSPI9abpAtVvsS_NlhNhyNvYz_U-fqT-UtNDQcejZcEoJxnFp3llpjTdRg_Fs6vPzJBLYf1nr0dgqT8QgYxycrO7KLLeVLUTN7hSsrlJvja-CRduZKj9SjG41lPqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98553c859a.mp4?token=Xmpm4m3-xiUB6QL0uu8DoE0aYXSO_8MVyxBJ2jh78GodNQ_InWObA3wq0zGIEgmvTN3Y3WlJxDQ-ZK-1ExW38u4fgoxBZjjKWZI0iJqfprhy7PJ-RF_1vEmmdzsKDkdHxLEOt6ea0VGkTNELnMXsbBlv-AZ7smJEy-9z4BBGKFnZbanKYLo0GzEWDXWQiwvs6XiA1NYzXGajuIUF9CJ8nKD4eSPI9abpAtVvsS_NlhNhyNvYz_U-fqT-UtNDQcejZcEoJxnFp3llpjTdRg_Fs6vPzJBLYf1nr0dgqT8QgYxycrO7KLLeVLUTN7hSsrlJvja-CRduZKj9SjG41lPqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر أضرار جديدة في مصفاة جازان النفطية جنوب السعودية، وذلك عقب غارة جوية شنّها انصار الله بطائرة مسيّرة في أغسطس/آب. وتؤكد صور الأقمار الصناعية الجديدة أن خزاناً نفطياً ضخماً يقع عند خط عرض قد استُهدف، ما أدى إلى اشتعال النيران فيه.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88260" target="_blank">📅 16:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88259">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
تعرض موكب ابن السيد خضير المطروحي، قائد عملــيات نينوى في هيئة الحــشــد الشـــعبــي، إلى حـادث سير على طريق بغداد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88259" target="_blank">📅 15:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">في اول رد تركي على القصف قرب الحدود التركية.. ‏تركيا تصدر مذكرة توقيف دولية ضد نتنياهو بشأن أسطول غزة.
رد مزلزل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88258" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله
:
خرجت علينا الإدارة الأميركية يوم أمس، عبر وزارة الخزانة ووزارة الخارجية الأميركية، بادعاء أن حزب الله خاضع لسيطرة فيلق القدس، لتبرر من خلاله سبب إعادة إدراجه على لائحة العقوبات، في قرار ليس في حقيقته سوى حلقة ضمن سياسات الإدارات الأميركية المستمرة لاستهداف المقاومة ومجتمعها وبيئتها ومناصريها ومحاصرتهم والضغط عليهم سياسيًا وماليًا وأمنيًا، بهدف حماية أمن العدو الإسرائيلي وترسيخ احتلاله لجنوب لبنان وفتح الطريق أمامه لتنفيذ مشاريعه وأطماعه التوسعية في المنطقة.
إن هذا القرار القديم الجديد الصادر عن الخزانة الأميركية، يؤكد أن الإدارة الأميركية التي اعتادت استخدام العقوبات وسيلة لفرض سطوتها وإرادتها  على الدول والشعوب، ما زالت تتعامل مع لبنان من موقع الوصاية، وهي بدل أن تذهب إلى إلزام العدو الإسرائيلي بالانسحاب من جنوب لبنان ووقف اعتداءاته وتفجيره للمنازل وجرفه للحقول وقتل اللبنانيين، تذهب إلى حصار اللبنانيين وتعمل على تجريد لبنان من كل مرتكزات القوة، وهي بذلك تسعى إلى إحداث اضطرابات داخل لبنان وتحويل مسار المواجهة مع العدو الإسرائيلي إلى اتجاه آخر.
إن حزب الله لا ينتظر شهادةً على لبنانيته ووطنيته من أحد، فتضحيات آلاف الشهداء الذين قدموا أرواحهم من أجل لبنان وشعبه، والتاريخ الطويل من المقاومة ومواجهة الاحتلال والدفاع عن الأرض والسيادة، هي الشهادة الحقيقية على لبنانيته. وإن علاقتنا الوثيقة والأخوية بالجمهورية الإسلامية الإيرانية هي علاقة نعتز ونفتخر بها، لأنها وقفت مع لبنان ودعمته وآزرته لتحرير أرضه واستعادت سيادته وحقوقه، وبقيت إلى جانبه في كل المحطات والأزمات، وكانت من أولى الدول التي ساهمت في إعادة إعمار ما دمره العدوان الصهيوني إبان حرب تموز ٢٠٠٦.
إن الإدارة الأميركية لا تملك أي أهلية أخلاقية أو قانونية لتصنيف الآخرين ولتوزيع شهادات الوطنية عليهم، فسجلها الدموي الاجرامي من فيتنام إلى أفغانسان والعراق، ودعمها اللامتناهي للإبادة الجماعية في غزة، وتغطية جرائم العدو الإسرائيلي وما يرتكبه من قتل وتدمير في لبنان واليمن وسوريا، وعدوانها على الجمهورية الإسلامية الإيرانية، ودوسها كل القوانين والمواثيق الدولية، وضربها بعرض الحائط كل القيم الإنسانية والأخلاقية، وتحويلها العالم إلى شريعة غابة ينهش فيها القوي الضعيف، يجعلها في موقع أم الإرهاب في العالم، وينزع عنها أي حق في أن تنصب نفسها حكمًا على العالم وشعوبه.
إن كل تلك العقوبات والتصنيفات الظالمة لن تثنينا عن التمسك بخيار المقاومة وبحق لبنان واللبنانيين في الدفاع عن أرضهم وسيادتهم وثرواتهم، ولن تغيّر من حقيقة أن المقاومة كانت وما زالت وستبقى جزءًا أصيلًا من تاريخ لبنان وحاضره ومستقبله.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88257" target="_blank">📅 15:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
🇾🇪
الإعلام الحربي اليمني:
ترقبوا الساعة الرابعة عصرا مشاهد نوعية لاستهداف القوات المسلحة تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيّرة.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/88256" target="_blank">📅 14:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">استهداف منزل ضابط في وزارة الداخلية العراقية رفيع المستوى في منطقه الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88255" target="_blank">📅 14:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88253">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:  إغلاق مضيق هرمز يمثل تحدياً كبيراً.  العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.  جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88253" target="_blank">📅 11:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
إغلاق مضيق هرمز يمثل تحدياً كبيراً.
العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.
جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88252" target="_blank">📅 11:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔻
مؤسسة "سي آي إس":
أن الولايات المتحدة قد استهلكت حوالي نصف مخزونها من أنظمة الدفاع الصاروخي قبل الحرب، وأنها تمتلك الآن ما يقرب من 800 نظام "باتريوت"، بينما تنتج روسيا وحدها أكثر من 100 صاروخ باليستي في الشهر.
يتزايد تساؤل الحلفاء في أوروبا وآسيا والخليج عما إذا كانت واشنطن تمتلك القدرة والإرادة السياسية للدفاع عنهم في وقت واحد، وخاصة تايوان وحلف شمال الأطلسي.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88251" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
قائد هيئة الأركان العامة للقوات المسلحة الإيرانية "اللواء عبداللهي":
القوات المسلحة في الجمهورية الإسلامية الإيرانية، بفضل استعدادها الشامل والحديث في جميع المجالات البرية والبحرية والجوية والدفاع الجوي والفضاء والسيبرانية، ستواجه أي أخطاء حسابية وتهديدات تقليدية وجديدة من الأعداء بردود ثورية ومؤلمة ومدمرة.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88250" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=Jnx6bNNY6-PKgwbtoySjhP0jGXDoLs6iGH9HXvqZ64gfMYnxvUWHdVscfc5Znj4979oByBE-Yjvclf3JZuxot7mldS8uwFgsU7SC4L-rjVjaBdvD44G-VsdsSM-SuNAie6uPFI_5UJfI-8BKvYLFy4-I9jpUreR2OTxAVzoC6JAkGtbmrr-dcMcKxhCfKgK5DiU8RM-JyPhNwuPD4jtWKdPgJdhLx0RH1_TEVAYkDhU4dqBzdhs6QiJfvvqZp1ybF6okUFbYLJuDr_UhVPwjtjolAp51jLa-iyuizbsal8j6BPj6u4L_ixRlTmObbTfoYxSyEKf_oihH3oSrd7U0Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=Jnx6bNNY6-PKgwbtoySjhP0jGXDoLs6iGH9HXvqZ64gfMYnxvUWHdVscfc5Znj4979oByBE-Yjvclf3JZuxot7mldS8uwFgsU7SC4L-rjVjaBdvD44G-VsdsSM-SuNAie6uPFI_5UJfI-8BKvYLFy4-I9jpUreR2OTxAVzoC6JAkGtbmrr-dcMcKxhCfKgK5DiU8RM-JyPhNwuPD4jtWKdPgJdhLx0RH1_TEVAYkDhU4dqBzdhs6QiJfvvqZp1ybF6okUFbYLJuDr_UhVPwjtjolAp51jLa-iyuizbsal8j6BPj6u4L_ixRlTmObbTfoYxSyEKf_oihH3oSrd7U0Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس البرلمان الإيراني خلال زيارته لمرقد الشهيد القائد أبومهدي المهندس، يكرّم عوائل الشهداء الذين ارتقوا نتيجة العدوان السعودي الأميركي الغاشم على مقرات الحشدالشعبي.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88249" target="_blank">📅 10:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88248">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88248" target="_blank">📅 10:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88247">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.
#أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/88247" target="_blank">📅 10:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0ca47031.mp4?token=R-t9whcue2BZx2o2kqVdBC89YmktYn6pTAPuBiSKEPrvlEfSkiqpbFScB-c04DEeKOB6Nop6Evish3O32y1vi4RfLdgKc8vfcVc9umiL_6YbeKaGB5fnGSo_d1jx5SgR0nfNnJoUOkSsUAWyn0mmFp8yJ5BD6mswvIfDr7w0useEBo-04W6s0jDjOWY_V23IIgeWwaRi-3JlASEw3yzlVafpDQUMOhzlRTReLnpEX2NxesirygOmRsqnqwjNq6RrSVJwTjqEgdhL8TEZOC1v_zweMX14jtI1VpW4t_SNrZasbUnKL62aojRRGmCQhx665YxVlYYBsCBfpeTWyC-UPiCUXIHQ_-6Bct18ooX03b7fX-9ZEoIrBesLwYOsVexp9d2kmzlKD_G9gASSeym25j2wr88K9Oqr5rJM_5IthysW1d6ZRaDASoX6m5_36shwJpkUCwME-OrppIVov0jXSr1o8DYWwyZAPj2BVz4jHnoi_VKhvWhvbNYSqjvYFhZRUIGtWCBbwscmNLQnGRyP0XbS61nryD5H1WrjR5ffCc_DPw5RK8vTqu6XDkaBIwbEIFbHAaKvE-IAX6j5SWroqw6ZwTe22LsXpb5Q7NGpsf1jl_krqI2odWQunVZvYSEXOlKD3sRX9XWwHAsuDKg8v0p1BenCbLCbauCY-4788Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0ca47031.mp4?token=R-t9whcue2BZx2o2kqVdBC89YmktYn6pTAPuBiSKEPrvlEfSkiqpbFScB-c04DEeKOB6Nop6Evish3O32y1vi4RfLdgKc8vfcVc9umiL_6YbeKaGB5fnGSo_d1jx5SgR0nfNnJoUOkSsUAWyn0mmFp8yJ5BD6mswvIfDr7w0useEBo-04W6s0jDjOWY_V23IIgeWwaRi-3JlASEw3yzlVafpDQUMOhzlRTReLnpEX2NxesirygOmRsqnqwjNq6RrSVJwTjqEgdhL8TEZOC1v_zweMX14jtI1VpW4t_SNrZasbUnKL62aojRRGmCQhx665YxVlYYBsCBfpeTWyC-UPiCUXIHQ_-6Bct18ooX03b7fX-9ZEoIrBesLwYOsVexp9d2kmzlKD_G9gASSeym25j2wr88K9Oqr5rJM_5IthysW1d6ZRaDASoX6m5_36shwJpkUCwME-OrppIVov0jXSr1o8DYWwyZAPj2BVz4jHnoi_VKhvWhvbNYSqjvYFhZRUIGtWCBbwscmNLQnGRyP0XbS61nryD5H1WrjR5ffCc_DPw5RK8vTqu6XDkaBIwbEIFbHAaKvE-IAX6j5SWroqw6ZwTe22LsXpb5Q7NGpsf1jl_krqI2odWQunVZvYSEXOlKD3sRX9XWwHAsuDKg8v0p1BenCbLCbauCY-4788Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
جرف النصر للموت ما ننطيها
لقطات قليلة التداول تنشر لاول مرة تظهر جانب من استبسال كتائب حزب الله وسرايا الدفاع الشعبي في العراق بعمليات تحرير الناحية ومنطقة عزيز ويس والفاضلية بعد فتح ساتر ياحسين باتجاه قلب المنطقة .. اللقطات تظهر استخدام الصواريخ الارتجالية الأشتر وصواريخ ال 107 ما تعرف بالكاتيوشا و ضربات ايضا بصواريخ ال SPG 9 و ال 106 إلى جانب اشتباكات من مسافة صفر بالبنادق الخفيفة والمتوسطة .</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88246" target="_blank">📅 09:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇺🇸
ترمب
: لو كانت إيران قد امتلكت سلاحا نوويا لكانت استعملته ولقضت على إسرائيل وكل الشرق الأوسط ، لدى إيران بعض الصواريخ والمسيرات لكن قدرتهم على تصنيعها منخفضة للغاية مقارنة بما كانت عليه قبل 5 أشهر، إيران تحولت إلى قوة متسلطة في الشرق الأوسط تتنمر على الجميع.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88244" target="_blank">📅 02:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9042a34cec.mp4?token=EiSSfLgMRP1sfD_rnu9_0ykiNi40C64EzSLLcMxhfzivo_nIrU4KBfAQZez7FiEKNlUNErLxg0ZfqWILcVuhNuJJEq7DH_y0kM2-UdP-Bx_BFpVp5ws59jclHFQ_5Wy7eDEp4nYXHgDwkaNhF87ZVuwesBa4Q_ijpZ5OKSZ6LqNWW0AhX88S-qolq9RhKRBNsFCb_r36pRSltj2ruWCcMbNalZkD_RN_OprAoLAlKkPA_xRPTT1vYzBvwDyCHE6_G_kdg3ZLTXL4RC7xG9tOHyFIPzdWDYvXst0ctKpWBSOTW40iT20Ld2nNHzL2hedOkwsHcwGbrgX6Lof0XbSP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9042a34cec.mp4?token=EiSSfLgMRP1sfD_rnu9_0ykiNi40C64EzSLLcMxhfzivo_nIrU4KBfAQZez7FiEKNlUNErLxg0ZfqWILcVuhNuJJEq7DH_y0kM2-UdP-Bx_BFpVp5ws59jclHFQ_5Wy7eDEp4nYXHgDwkaNhF87ZVuwesBa4Q_ijpZ5OKSZ6LqNWW0AhX88S-qolq9RhKRBNsFCb_r36pRSltj2ruWCcMbNalZkD_RN_OprAoLAlKkPA_xRPTT1vYzBvwDyCHE6_G_kdg3ZLTXL4RC7xG9tOHyFIPzdWDYvXst0ctKpWBSOTW40iT20Ld2nNHzL2hedOkwsHcwGbrgX6Lof0XbSP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
سفير بريطانيا  لدى العراق عرفان صديق
▫️
‏نوجه رسالة الى الفصائل سلموا سلاحكم وستكونون أصدقائنا مثل احمد الشرع.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/88243" target="_blank">📅 00:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88242">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ربما يسمح بالنشر ..
🇮🇶
🇸🇾
🇸🇾</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/88242" target="_blank">📅 00:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px0Kef5vOBI-CepV3mUiAYlIgAGoP62m9GJp32kOgqkLG3PKCTtYhgnMC-x8_5p4dcHsP8YqBFdRe884JTieZhS9eHXNIP7QMvAgyb-NVPRWO1FuimocDOrF8WlJP_PVaU8cDVYVLGXeYS1p80DzPVR5Hj-JoIa7NVzVuadY4aQ6U78BUak6RUGaOrYAxd8vHBRF9VYLN0TcYZsXb8X4MZxmi1svpIbnFz8xY9eP5ML9moq3XlVMXnTrCUfDtHaKqXbeJhWmanc8YnphXZuenfrmjSrn3k4uAQHnOrtZXvCw2SGl8Hp11pZ8FPqmrOWIX8LzP7IJQLEqIBpYB3e-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
صور اقمار صناعية تظهر تضرر بشكل كبير في مصنع مواد بترو كيميائية في دبي بفعل احد ضربات الصاروخية الايرانية.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/88241" target="_blank">📅 23:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTdD5ywSzcPzjIll_lvJWTKwNeIudCGgdHS-hNYYQEw_WrIVEWqDsj2OgK5SGUWuIKqHfXCQqt8-lKeG92vJXlbx1POpLqa7k8BZlhqhnwJgEaH6l763-SRgv6RM4pOsv77zfCqQ7NM6ECloiGycLgJrSbVL_NSCMro4T1XNthJZQXoGeviouD5QDJhHgISAsAmxW6FRQPddBXdc4VeA5ko2OX0d6GnrKZIEq8YaY3lbeWnbe06qTm7I-CsIzgzrNcvPfJItiCRsrE_L5RJh3Rs-JO-RNkQF_unFGwITJnt75hSFLPZApdGJ0sJuF37Gnqp4OorbKbVE3p5w5Zldog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
مشکل، به‌طور خلاصه، تفاوت در سطح فرهنگی و علمی بود
پس از آن‌که آمریکا دموکراسی را برای عراق به ارمغان آورد، عراق بر مبنای قومیت و مذهب تقسیم شد؛ نتیجه‌ای طبیعی از سیاست استعماریِ «تفرقه بینداز و حکومت کن» و نوعی الگوبرداری از وضعیت لبنان. با این تفاوت که در عراق، رئیس‌جمهور کُرد است، نخست‌وزیر شیعه و رئیس پارلمان عربِ سنی.
مصیبت بزرگ‌تر این است که طبق آنچه گفته و نقل می‌شود، رئیس پارلمان رانندهٔ کامیون تریلی در مسیر الانبار–اردن بوده است. یعنی در همان زمانی که قالیباف هواپیماهای مسافربری را هدایت می‌کرد، این شخص مشغول رانندگی، تعویض روغن خودرو و تخلیهٔ بار بوده است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/88240" target="_blank">📅 23:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDlfxsXbxm2H1WViKSmErXcO4a3Yb91udzMGBtOTIN3qeJ87BpAoslinzpBHzvfLkIgsEdQuS1TbLlYWXOVIrqDiKbBQVi-XAQbCUUUJnIkeDayKePYQaxnQ3dUtAOLAxt6xMDXY3kdDop5BnSKNETD2NR-FJzu6bTzGZlHoNW4wx8PpXaDZgufGhztlbQS6F1-IlkYp7sgycxaRHyEwT5EimHKobcKRazhV3Th0x6oS6Dz7EZ-32_sC0cbowE_NaL20e0IWMCQvIfMR0u0gAvB_m27FtCVhJpheGLMpTl_sZiuRiFi5BiSkUv7s9hMD78VjHfqE-DdEwL7tTv2ezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربما يسمح بالنشر ..
🇮🇶
🇸🇾
🇸🇾</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/88239" target="_blank">📅 23:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba39abc2c2.mp4?token=CVgS1X8jOcNTe_eXT1H4OzWE3OTlKbfEGcdMpcEmoVyu8WdW3qrUK9osU3mbZXa43sknQL2HyKyAlYuLlwISxuQzS_u67X-vPOv6zChpQy8KzyE6N173kw6-0lTgF5dUX_WbaxpYnMmYJT1pnkkbmi-WNNQhXrNcYBvjTy919r65ezKX1k6hX2SN_MyMxhLwhlPazsmzD48DOO2W_9Ci22XdzuxdAOje3sLVtGteW0G7XA8fmvGk-UIM_YnxP9M9AkcJGb0LLIt7ExK5llqwHBFpNwtmfY06L_CtXJY4vy5F4ngiSoZR8UzQaLd3s6XuE-RKwhsGHdJ5zazDcTWn-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba39abc2c2.mp4?token=CVgS1X8jOcNTe_eXT1H4OzWE3OTlKbfEGcdMpcEmoVyu8WdW3qrUK9osU3mbZXa43sknQL2HyKyAlYuLlwISxuQzS_u67X-vPOv6zChpQy8KzyE6N173kw6-0lTgF5dUX_WbaxpYnMmYJT1pnkkbmi-WNNQhXrNcYBvjTy919r65ezKX1k6hX2SN_MyMxhLwhlPazsmzD48DOO2W_9Ci22XdzuxdAOje3sLVtGteW0G7XA8fmvGk-UIM_YnxP9M9AkcJGb0LLIt7ExK5llqwHBFpNwtmfY06L_CtXJY4vy5F4ngiSoZR8UzQaLd3s6XuE-RKwhsGHdJ5zazDcTWn-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ملانيا زوجة ترامب تظهر:
سمعت أنكم اشتقتم إليّ. ها أنا ذا.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88238" target="_blank">📅 23:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660318801d.mp4?token=WaefRa-vrABPe34OZOOHkJ9nPzWbgKmOBmRhgqKdc02tefqzE0u_jJnXLB3Tofxr3PSj-5VJA8Y3xYOu-bKhtqQXgqhq9JjZrHeMnmey635Me5UMR4wLNxx2L5S8LyqIT4D46pZTW7JsVsfdMT_qcVP2MqRA8_NxxkKlhBZAK0tdGXIPyG71AYyK9Kkok4sYtrvA5cVCcC6Mbcremj91HZJftXqTKeqeHap9dS0lgToylHYni912d6lMQiN_p2ONtGm0aCpCysTA9rVQY4j4stFDiUHqfPf7UohuqMDNP9YvqcetLYa_V3ZL1-W5CE4FraumV6NNaFUN3jZm_vNpjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660318801d.mp4?token=WaefRa-vrABPe34OZOOHkJ9nPzWbgKmOBmRhgqKdc02tefqzE0u_jJnXLB3Tofxr3PSj-5VJA8Y3xYOu-bKhtqQXgqhq9JjZrHeMnmey635Me5UMR4wLNxx2L5S8LyqIT4D46pZTW7JsVsfdMT_qcVP2MqRA8_NxxkKlhBZAK0tdGXIPyG71AYyK9Kkok4sYtrvA5cVCcC6Mbcremj91HZJftXqTKeqeHap9dS0lgToylHYni912d6lMQiN_p2ONtGm0aCpCysTA9rVQY4j4stFDiUHqfPf7UohuqMDNP9YvqcetLYa_V3ZL1-W5CE4FraumV6NNaFUN3jZm_vNpjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا   اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88237" target="_blank">📅 23:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🫡
أنا تحت راية أبا الفضل العباس
We will never forget Ya Abu Fathel</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88236" target="_blank">📅 22:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88235">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رويترز : قال مسؤولون كبار إن القوى الإقليمية لكرة القدم في العالم تناقش إمكانية طرح اقتراح بحجب الثقة عن رئيس الفيفا جياني إنفانتينو بعد أن أغضبهم بخططه لبيع حصة في كأس العالم لمستثمرين من القطاع الخاص</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/88235" target="_blank">📅 22:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88234">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
اشتباكات عنيفة شرق العاصمة بغداد في محاولة اعتقال احد قيادات جيش المهدي " ابو درع اللامي " .</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/88234" target="_blank">📅 22:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">زلزال قوي يضرب بيرو بدرجة ٦٫٨.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88233" target="_blank">📅 21:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا
اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/88232" target="_blank">📅 21:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇱
🇹🇷
الاعلام العبري:
المستوى الأمني أوصى بالتهدئة مع تركيا وعدم فتح جبهة إضافية.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/88231" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=Av9OAKgoOQcDQ0fY3s0GMZGwbjiuwJLvslQTc53y9NUDAswsPF5ThtoQqZM87cJpfdPor5pGeppw8C1qEnvGeM3oYjsr4VramdxBpLjDg5HQcoHAKeGhwXKRSyFDZJLIF9rY3ySjl_OYLRz1TTeT1KU9vcBxoyCMrUUpQdT9Y2en_XCgW5iPygxHeix9KhPqTNCPmFxUjKv9qIxY5Sri02nnhHrKshKoFxW-5BPULOK7LkfBPcFC-AMMXSxEPrzhpiSK6jhCN64699xrPd-8okZFAuiGbGQgyuPsYR1nGML9eE2Hd-l78iHjtcHF-SSPtIV33Zx20-18OXouYn0EIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=Av9OAKgoOQcDQ0fY3s0GMZGwbjiuwJLvslQTc53y9NUDAswsPF5ThtoQqZM87cJpfdPor5pGeppw8C1qEnvGeM3oYjsr4VramdxBpLjDg5HQcoHAKeGhwXKRSyFDZJLIF9rY3ySjl_OYLRz1TTeT1KU9vcBxoyCMrUUpQdT9Y2en_XCgW5iPygxHeix9KhPqTNCPmFxUjKv9qIxY5Sri02nnhHrKshKoFxW-5BPULOK7LkfBPcFC-AMMXSxEPrzhpiSK6jhCN64699xrPd-8okZFAuiGbGQgyuPsYR1nGML9eE2Hd-l78iHjtcHF-SSPtIV33Zx20-18OXouYn0EIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كثيف للقوات العسكرية على سريع القناة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/88229" target="_blank">📅 21:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=fVXTz9sUIA7TlzcQxZIkilVAlxKn10YHiDNzXZIIc5Ho6bnUOLjWJgPoLCArXvQm287W4IibbgmxGcn_Ervzy4l-vfbLQg0_-irtTDAEXurmyYP98dgnAvhyPS-0lyU3LT53VNCqKNe8KdInKVr_4Kx56nBfHWtJfhW0_Y34iCuupXqpvxfse64SZr1mL6wBri9ytq7trdiyj6DVHvzRjNm1EA3bgQwlnHZQQqL65vpRbudsthPihJJBbPe0agIESNajbLAMhdCyF-TyuBseo8-kbvPMbALvfyC0OJkY9LelvZ3-TRz_xBCxPoLwn2_nEuPkLdWgxcdnbUWC52LzYQkWMy9VnELDO7Fb-RCnB8ZGYpVjAFTMuNzmRfyJlprQ8EZzBkeiX-w-UVYtufsItFtvwxh8YYW3O2gjxg0bilxLAeyQT-UKWOsJlNZPrhYJLUlw8_eVui53WcI7jxgTYv58ssKC_xrhQD_ihIozCHxruDE31EfY7IRlmFafZ3K874w0JtgRiTuKvEp5t7IlHN9__008PJs7Tx1sPwiB27TmzGV87UEl-5ZsbItBz36ELyEFvvqGkZ9lA9R5jzrKXQY1ExZ1jBwoDthKD_PDMma2QpbaPlKHj9yEwXdq-m6EHUK-J3RHOCMSto9gaDJmdNGyXxK8QpSD6omR2aFPFcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=fVXTz9sUIA7TlzcQxZIkilVAlxKn10YHiDNzXZIIc5Ho6bnUOLjWJgPoLCArXvQm287W4IibbgmxGcn_Ervzy4l-vfbLQg0_-irtTDAEXurmyYP98dgnAvhyPS-0lyU3LT53VNCqKNe8KdInKVr_4Kx56nBfHWtJfhW0_Y34iCuupXqpvxfse64SZr1mL6wBri9ytq7trdiyj6DVHvzRjNm1EA3bgQwlnHZQQqL65vpRbudsthPihJJBbPe0agIESNajbLAMhdCyF-TyuBseo8-kbvPMbALvfyC0OJkY9LelvZ3-TRz_xBCxPoLwn2_nEuPkLdWgxcdnbUWC52LzYQkWMy9VnELDO7Fb-RCnB8ZGYpVjAFTMuNzmRfyJlprQ8EZzBkeiX-w-UVYtufsItFtvwxh8YYW3O2gjxg0bilxLAeyQT-UKWOsJlNZPrhYJLUlw8_eVui53WcI7jxgTYv58ssKC_xrhQD_ihIozCHxruDE31EfY7IRlmFafZ3K874w0JtgRiTuKvEp5t7IlHN9__008PJs7Tx1sPwiB27TmzGV87UEl-5ZsbItBz36ELyEFvvqGkZ9lA9R5jzrKXQY1ExZ1jBwoDthKD_PDMma2QpbaPlKHj9yEwXdq-m6EHUK-J3RHOCMSto9gaDJmdNGyXxK8QpSD6omR2aFPFcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
نتائج الحرب على إيران.. النفط يصل إلى 94 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88228" target="_blank">📅 20:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCSmnLJ5ssCvmREJLysGO1rK7Db75XpQ1ZBtrHNCKhEmo4kEThU4YvSkWOOiS5tr2gLAq_pjGwf6YyXXCrhDnLhkHhyKwz6zO8eUiF51yPf2dGOywn3YO4LGRtQoXX-SoRy8bbYvpeX_8b2CK8QMgtE5VXSw_a_b-Rjr2_INFdElwWchPQAT9h3VqXR8o2XTpmiCTwTc-E7Laa6nq8DpK97_SxLjLQecbmIX1akiB5Wpy_gH-D5v8f5qkQLehKn_D5h3Xn5EWpRzNezA6qx5avKkVj78NVbj2dGvH1HhUwwuCIBZtfg5tW2i0RV8O7JMTr4QwoztX4Cjzf8FUk3WIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور الإماراتي في العراق يرد على زيارة قاليباف بصورة فوتوشوب  من تجيب قاليباف من كبيسة</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/88227" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخزانة الأمريكي بيسنت بشأن إيران
: سنفرض أشد العقوبات في التاريخ، وسنسقط هذا النظام.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88226" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
🇮🇷
محمد باقر
قاليباف:
- كنا مع العراقيين أخوة وأصدقاء في أصعب الظروف.
- عمق الروابط بين العراق وإيران متجذرة في التاريخ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88225" target="_blank">📅 18:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88223">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUdHGGi0i0vTIShP7dUL-ZK4m0Nymnj9GzbClOsN3j_fMX29kC7IBpT_RtLnL2i20QY-UI8AIuyQAQTuUcuKsEVZBTeGZi7mrFG7sGlrFXxnnFnaS1OlX6jCIbqjrbPyn101HfWER4u29NtonAEZHWMABurmPG1BI7kogEbxcRG3esX0lRc3qQekPMimnh5r5MVTY10xkE0IIHwMpdvCXmoHoe8MPPuHZofRFZT11o4mUrM8V1qZ0eY-pr0XyWNjbaLeVEmC4eNpKDa0m8td1gUhSwFusph2Lg4zy77vcsbxLohUrCOol_UfOW-kSA6rmDf1jo6ofDYKwG3fZDjunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية:
تزامناً مع ذكرى انقلاب 28 مرداد 1332، أقدمت الحكومة الأمريكية على فرض عقوبات اقتصادية وتجارية واسعة النطاق على الشعب الإيراني. ويُعد هذا الإجراء دليلاً آخر على استمرار العداء والخصومة التي ينتهجها صانعو السياسات الأمريكيون تجاه الشعب الإيراني منذ 73 عاماً، كما يثبت الطبيعة المعادية للإنسانية والمخالفة للقانون والاستكبارية للحكومة الأمريكية.
ولا شك أن العقوبات الاقتصادية الأمريكية على إيران، والتي استهدفت الحقوق الإنسانية الأساسية للمواطنين الإيرانيين، تمثل مصداقاً لـ«الإرهاب الاقتصادي» و«الجريمة ضد الإنسانية»، وإن مرتكبي هذه العقوبات والآمرين بها يستحقون المحاكمة والعقاب بسبب ارتكابهم مثل هذه الجرائم الشنيعة.
إن هذه العقوبات، التي تأتي عقب الحروب المفروضة التي استمرت عاماً ونصف العام، وكذلك الحرب التي استمرت 12 يوماً مؤخراً بين الولايات المتحدة والكيان الصهيوني ضد إيران، وبعد فشلهم في تحقيق أهدافهم المتمثلة بإجبار الشعب الإيراني على الاستسلام أمام مطامعهم غير القانونية واللاإنسانية، تستهدف الجمهورية الإسلامية الإيرانية، لكنها لن تُحدث أدنى تأثير في عزم الإيرانيين على حماية استقلال إيران وعزتها وسيادتها الوطنية.
إن فرض العقوبات والضغط الاقتصادي هو الوجه الآخر للحرب والعدوان العسكري، وإدمان الولايات المتحدة المرضي على هذين الأسلوبين لم يعرّض السلام والأمن العالميين للتهديد فحسب، بل تسبب أيضاً في انحطاط أخلاقي غير مسبوق للحضارة الإنسانية. وبناءً على ذلك، فإن أي دولة تؤمن بمبادئ وأهداف ميثاق الأمم المتحدة، ومن بينها مبدأ احترام السيادة الوطنية للدول، لا يمكنها أن تبقى غير مبالية إزاء استمرار خرق الولايات المتحدة للقانون وممارستها العدوانية العلنية تجاه القواعد الأساسية للنظام الدولي.
إن إقدام الولايات المتحدة على الإعلان المثير عن العقوبات الجديدة، رغم أنه يُعد اعترافاً صريحاً بارتكاب جريمة ضد الإنسانية، يمثل استمراراً لسياسة سبق اختبارها وفشلت، وإن إعادة اختبارها مجدداً لن تؤدي بالتأكيد إلا إلى تكرار إخفاقات الماضي وفضيحة مصممي هذه السياسة ومنفذيها. وبطبيعة الحال، ستقع مسؤولية نتائج هذه السياسة وتبعاتها على عاتق الحكومة الأمريكية ومصمميها ومنفذيها.
وتؤكد وزارة الخارجية، مع إدانتها الشديدة لإقدام الولايات المتحدة على تشديد العقوبات غير القانونية والمعادية للإنسانية ضد الشعب الإيراني، أن الجمهورية الإسلامية الإيرانية ثابتة ومصممة على الدفاع عن أمنها ومصالحها الوطنية ومواجهة الهجمات والضغوط العسكرية والاقتصادية والسياسية والنفسية الأمريكية.
وستواصل الجمهورية الإسلامية الإيرانية، بالاعتماد على قدراتها المحلية، وبالنظر إلى تجارب سبعة عقود من المقاومة الشاملة في مواجهة سياسة الضغط الأقصى والعدوان العسكري والإرهاب الحكومي الأمريكي ضد إيران، استخدام جميع الأدوات والقدرات المتاحة لردع شرور العدو الأمريكي-الصهيوني وحماية المصالح الوطنية الإيرانية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88223" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88222">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نايا-NAYA</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/88222" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
مناشدة عبر بوت نايا:  نحن مجموعة من صناع المحتوى نناشد الهنود والباكستانيين بالانتقال من الرياض الى نجران. نحن من بعد الله نعتمد عليكم في توثيق الانفجارات والدك اليمني على رؤوس ال سعود ومصالحهم الاقتصادية. نرجو منكم النزوح الى نجران والجنوب خلال الفترة المقبلة…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88222" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88221">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يراقب المسؤولون الأمنيون الإسرائيليون الأتراك ليس فقط على البر، بل في المجال البحري أيضاً. ووفقاً للمصادر، تُرسل تركيا سفناً حربية إلى مناطق في الشرق الأوسط لم تتواجد فيها من قبل، وذلك لإظهار وجودها، وفي بعض الحالات على مقربة من السفن الحربية الإسرائيلية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88221" target="_blank">📅 18:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88220">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">القوات المسلحة اليمنية تنفذ عمليتين عسكريتين بطائرتين مسيرتين الأولى استهدفت هدفاً حساساً للعدو السعودي في مطار نجران والأخرى استهدفت أرامكو نجران وقد حققت العمليتان هدفيهما بنجاح ردا على انتهاك العدو السعودي لأجواء محافظة صعدة بطيرانه المسير</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88220" target="_blank">📅 17:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88219">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88219" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88218">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88218" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88217">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDye8s4aFQW9NTkjVmA4sEFDhxLbCQkjqQfTG7MtshkxH-3C-hTfyY0GZQCz7Qrna2dFFTpFPGY8EATszrBTToLbLMEFES9bZmlFEh23iiysNUSCXB1v9JrJgSl5gpxRH43ett9iojLTti5r9yAIaUs3QafD3_HGtNXUUCbqH6496Hz7C2Bnp1a4j2VbkWk00f8UNgZq7_VFzk8ELPuVDzVnxxsHpqX8ZhiQV-QLpVBW0wyOufMi1xMLxCm4P4_ndEUxitYWk8SbvenL5ayNdZ0U9Y-ARB6bQhbhgRn7DJhXpA9utTZi6KzKVSeBJotnI0G6-ZKU21c9OADbnMAN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تغلق الموقع الرئيس لشركة كورك في العاصمة بغداد وثلاثة مراكز مبيعات أخرى.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88217" target="_blank">📅 17:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88216">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وصول رئيس مجلس الشورى في الجمهورية الإسلامية الإيرانية السيد محمد باقر قاليباف والوفد المرافق له الى محافظة كربلاء المقدسة
🇮🇶
اخوتنا قدوتنا
🇮🇷</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88216" target="_blank">📅 16:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88215">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇶
قوة امنية تداهم مصرف الرافدين الحكومي فرع السعدون وسط العاصمة بغداد واعتقال موظفة كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88215" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88214">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKPlDQwFJoPZ20sGT7enlGYB0rTjsCD5VdckuB3dka2FMuvS3RuX9cEX_yKjmLOpz0LNMow9qNpZNFQn4Ue-WLWytqnrgqW5YWn5-YsfUIjvEBv_XxRR6U721DYScFqZoRTudrKHx3L5b8mfVvF6nZgONk7tsT-6iCZO8EmrX_w896QascwVnB-O3Hm1BkSu289ZJVxo_6vkAxUXOuSNHE0_mmEUY3IKIFV9Tv41K8a5l7pskvfU5Yp40CgONr6wN58LWY49LQlhxIG1mdgLGBURSSGj7CvsmRMgKpzm0xPeFiZQFyr2dnGuZi10GiMulUiR444StlRU99RuHKv5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور الإماراتي في العراق يرد على زيارة قاليباف بصورة فوتوشوب
من تجيب قاليباف من كبيسة</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88214" target="_blank">📅 13:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88213">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">السلام على أبا الفضل العباس</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/88213" target="_blank">📅 13:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88212">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/88212" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88212" target="_blank">📅 13:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88211">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=MSaFCQh1bHoBIX5Zv5psLPf2w2Eo6KkOuXuoPg68vX8S8EVwgkdaUA65QAvNHeniVwoPBtWjnsiWtl1rgn89OzlT9V0kMUOkyVCziMrJMH0pYb9CiVpgZ04WYeTYDi4VT0HIjkdonl9tAeeoQ2ns1eb7vSubUHd5AFnTad3YQas1UfHGxegLXZ022d0J0tn8n08SwZ6i1W-Ssb9EGXNEEM9OatfbIjWbcoeR_JObj8ER-lX6pY96n_jvTBLzg2PNw_LgWn2Lr1LDN3lyyEPyVz1rUvXXf7UQjX_ya6Z1zLPCOLnRQ_qsOISiCE0B2A_Hk92l1nHqebTPnE9YT9OFNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=MSaFCQh1bHoBIX5Zv5psLPf2w2Eo6KkOuXuoPg68vX8S8EVwgkdaUA65QAvNHeniVwoPBtWjnsiWtl1rgn89OzlT9V0kMUOkyVCziMrJMH0pYb9CiVpgZ04WYeTYDi4VT0HIjkdonl9tAeeoQ2ns1eb7vSubUHd5AFnTad3YQas1UfHGxegLXZ022d0J0tn8n08SwZ6i1W-Ssb9EGXNEEM9OatfbIjWbcoeR_JObj8ER-lX6pY96n_jvTBLzg2PNw_LgWn2Lr1LDN3lyyEPyVz1rUvXXf7UQjX_ya6Z1zLPCOLnRQ_qsOISiCE0B2A_Hk92l1nHqebTPnE9YT9OFNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88211" target="_blank">📅 13:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88210">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbpKjSNi7_SKwYP6ykCM6pxdoZUh8n_GEg0RfbyTZiE0uUUe0Xcu8pwxPh8pkSmEglE8MzeNykfyBSzDscEy7y5vfCZcncW0VVna_h4Ld_Es0skZ2q4qD1d6qm_8NLdph9GMK5i0VWut0a0hRPAoDnknpS8_3MumT8gbCPSdldBnOMjpq-cGkVJeMZtI2v_k8gMyRQ49BMlRDXi9Jzi7a3R5zEOgxJW24l3ifMzA1KoL8TbtrPQ2y9BFBbBe2hWSah3c0ID-VUZ0AAwgnydJgPmwie9qUh_sQ4VMlX_6zQp__kAAKM_hNhTzkVZOFmThPOhF2lKuYsoFteHGSJM34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
فالح الفياض: تغريدة المتحدث الامني باسم الكتـائب هي "رسائل خشنة"</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88210" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88209">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryT8sW8F96T8WvIJiujAbdvB-J4nW9vELZ2yp8N9llgbWxxX2WXAE7OZhwvUbMkneaRgJeV226OQ1GZ_E2SmpNwpBJjB7y0Kscr5gpLUsuFaxEDY8agU5NEO2EuVyhiRGA1uBaMGyln8-n-CCVbB6c79dznwLg-1Grt7dHVUoUJh9Q3Dklpq1AzjhXwZ-2Qe-BpR66Ww-tw2XVr4gjO5u7NVVJ8Zae0w1efWGp7At72aS0wHB78TFmtJNfKN87Y_5OEpS0xJZx4XtfKHLU8R4-TyJzeaR6XdsjxxQ8N3sN42Ty57U62hEyuoC2mRxy3Em-f4v5dc8VnvHQPnnq8LWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حدث امني قبالة السواحل اليمنية..
سفن صغيرة تقترب من حاملة نفط شرق المكلا في اليمن والأخيرة تطلق نداء إستغاثة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88209" target="_blank">📅 13:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvnNljssw8vRYo6Sg3DqvqRPiv2KTSVhRyOGbhN22FFVdWeyOSXBqviX0lFmtmCGafbZF3AY4N6f-r4Z06DgyVGyAtSEqYGEsyc7BFT1fjIzH_8X1W5CRNDOVppgK8YiI0GEZBGFagtKvND3HRLK0ffxdXPjH2ZmE4cziPiDBTIcR_wjUO9cf51UaZjJjng4n6AIwCtumXX8N1fAGWevt73xP6QE7E1FWY72dChRds4kisyCCMb-1Qf5TohT1jGs_p2w2JnPFxSmxprF6GnezPWtNv__XSjKiYBjF8AzIhv65ZkOerYfyXunki7udEaxb3FUY8H_y56bHCgEZ53urw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
إبراهيم عزيزي:
تحركاتكم تخضع لمراقبتنا الدقيقة.
أي خطأ في الحساب أو خطأ متكرر ستكون له عواقب وخيمة عليكم أكثر من ذي قبل.
أنهوا وجودكم المشؤوم في المنطقة قبل فوات الأوان، واستسلموا للنظام الإيراني الجديد في المنطقة.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88208" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
وزير الخارجية العماني: المرور الآمن عبر مضيق هرمز لا يمكن فصله عن استقرار أمن المنطقة.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88207" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
مع إستمرار التوتر في المنطقة وسيطرة إيران على مضيق هرمز.. أسعار النفط العالمية تحلق نحو 93 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88206" target="_blank">📅 12:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇹🇷
‏
الدفاع التركية:
لم يكن أي وفد عسكري تركي في مطار أبو الظهور قبل أو أثناء القصف الإسرائيلي.
على إسرائيل وقف الهجمات المتهورة والالتزام بالقانون الدولي من أجل الاستقرار في المنطقة.
تركيا تتعهد حماية سيادة سوريا وسلامة أراضيها.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88205" target="_blank">📅 12:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1579180dfb.mp4?token=QeWQfw94r6yv7Q1RVJHLox5ASkYBKw_cdcN4dvFARo6adTM1J1twlJ4xuOQqoqGNNtChei1atmoBZC9LYf0SQpnYaLWsvzgv59TQgGdbofMeAYoi6fR_wfuYx8G3c8dVZu1JZjGjwDPcZb0vOkkEwS3GHor9-v8EMU5GDemfTtwW2DVKacGko3zipcR8zwbbSTtCNZf3fC0iAsM58kW17W93U7DLAQOKXrm2Vy8IIKYBVdOOzmD0sCKFn5XWJZSFU3Dq1F-a4m_OHh2sWE_VZE9n4AgR58Gm5NQ4-8boEGYKPq_txiaX91VQI01y-9OHyABsqIos7IRlDCdJDHlP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1579180dfb.mp4?token=QeWQfw94r6yv7Q1RVJHLox5ASkYBKw_cdcN4dvFARo6adTM1J1twlJ4xuOQqoqGNNtChei1atmoBZC9LYf0SQpnYaLWsvzgv59TQgGdbofMeAYoi6fR_wfuYx8G3c8dVZu1JZjGjwDPcZb0vOkkEwS3GHor9-v8EMU5GDemfTtwW2DVKacGko3zipcR8zwbbSTtCNZf3fC0iAsM58kW17W93U7DLAQOKXrm2Vy8IIKYBVdOOzmD0sCKFn5XWJZSFU3Dq1F-a4m_OHh2sWE_VZE9n4AgR58Gm5NQ4-8boEGYKPq_txiaX91VQI01y-9OHyABsqIos7IRlDCdJDHlP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
العلاقات العامة لمصفاة النفط في طهران:
اعمدة الدخان في سماء طهران ناتجة عن حريق طال صهريجين لتعبئة ونقل المنتجات النفطية داخل محيط مصفاة النفط بالعاصمة طهران، ولايوجد أي حريق داخل المصفاة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88204" target="_blank">📅 11:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
الإعلام البريطاني:
قام مرتزق مدعوم من الإمارات العربية المتحدة، واسمه أبراهام غولان، بتنفيذ عملية مراقبة سرية في لندن عام 2016، استهدفت الناشط البريطاني العراقي أنس التكريتي، الذي كانت أبو ظبي تعتبره مرتبطًا بالإخوان المسلمين من خلال مؤسسته البحثية، مؤسسة قرطبة.
قام غولان، الذي نفذ سابقًا عمليات اغتيال في اليمن لصالح الإمارات العربية المتحدة، بجمع معلومات تفصيلية عن منزل التكريتي ومكانه للعمل وتحركاته، وناقش احتمال قتله.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88203" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88202">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAnsPbH_y8hxpRKqZ5OKBTGzLdZak0qIHMQRGDx_4-LgX-TWoMH0e4xG0GQKEddgtr7B83mThrx_CuYgpSbBW2c2BzKxLXrOoVrWzWpTJ0lXVXGGMqPZl66qmY4U9mZ_58mVB2CcIRNfe3HLqV380DT26M5v3PObHr3yMggQWNruJt7PH2dNE5kWsCLHzbkroNvt43VWsZHXuEzIzY-wJfthk4NvC-cyEaC2OYSfBAV_3JKcAkmz1BuX_CKG5PPWjWk9M3L4k3WPnGCLPvwViVViKLzeyEkWMjQjWmF3-J8jv4OcACEgeUPOXNqQTFWKFpS5V9TaGF6ZWopQgrMSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مع إستمرار التوتر في المنطقة وسيطرة إيران على مضيق هرمز..
أسعار النفط العالمية تحلق نحو 93 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88202" target="_blank">📅 10:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88201">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_5r1dphhD0icE6DJ6nUstOaEx8rZsfRGgIUYPToRmv5YCiBBpSr-laMt_0dyeR8lfnKHqdZyYlla4QMO89vcy45IzsABGFlTDevawmGWL6k3X7k9llnHyog6eNf4BvStelc0hHRZ9m_7AYrHPj2ucCewf-6RLsLoaU_cBphCkygX6aAEm_6HUYVS-1eOVGKx4gTpOlnRAVxRfq3jCJrvxjlV48-rHUwpo6N9sGgVPRKmsgyaGOGiKdNbk87d14tq4LK9VzBoyRqtDIsrFCjNA3ExhixbaNAasXYSOkFuYYFQMc1cEBIkYlFAHsFbVbXsrdLPhogLVyCaVkFfHfXQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس القضاء الأعلى القاضي فائق زيدان يستقبل رئيس مجلس الشورى الإسلامي الإيراني محمد باقر قاليباف.
#أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88201" target="_blank">📅 09:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88200">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDo4ONJ6WKGaIZee3LsElxtz9e8la5ikt5Msq_M-CRMfv9Y1bdYxC9Jt_BS9UM56ZcNGz9H633OQKZobl7jIOwPvObvuiuuaXjKhtOQga1EZKS3CRx0vUv8XDbi4pT2FS25mAd97ikqWXhe21NecQFJ56sOBqJVAZp27eabklHPO6f-PkLJL-QM2966GRb9oNsuwD7MOvYjw7O_I7MBbNPqflnZYfDNc7p7knyvw8tRPT4loU--y35kzA9kZzbLWyoOduiWUUiCczokvu21h3u4N2W2PIH0tOwSFWqyDheEwFqf_A2AIGXPxhAYSSfaVFVh6upfOX4mks8-7csZwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88200" target="_blank">📅 09:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHmS9tGJr7HVCGExxmqmB9rvS74JOs8dbwwk-2boycmHVE5Uxne3uwkQabTrqySMHiOexQfQGStxxw1S6q21NQjpGC1fdJrDZIPBzHoXlavwu2nXrwGSme2-bPeY50kK1JV3Pa4-gBjLeKcW8lhpCDcr0D8zJhRxuXJ3j8WFe5mCaWIrH34Xehz6ykL6tu9SXV03nt_OSosqVNXSGKjHjkqbfl9hiFkbu36mDCYiMZEAeKpVmRzg92AYzAbpsU6vfhO_LEguNuVHrDLU1PMoDolhQ9LtPvyhEDaqx1qEUs6la1ZJ3cJCfs4BU5Az9xCwI90XlsILdW8u8AjWHEgJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇹🇷
وزير الحرب الإسرائيلي "يسرائيل كاتس":
أردوغان يجر تركيا إلى مغامرات خطيرة في سوريا. لن تسمح إسرائيل لأي طرف بتهديد أمنها.
سيكون من الأفضل لأردوغان أن يواصل إلقاء خطابات جوفاء وخيالية ضد إسرائيل في البرلمان التركي، بدلاً من اختبار عزيمة إسرائيل على الدفاع عن نفسها.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/88199" target="_blank">📅 08:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88198">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب: لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/88198" target="_blank">📅 02:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88197">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGwuMqE9AaocaBTGzvxBFr91ncceK89OiTHItEe3qIR1Y5x4JJ3c0hPw2nvmMNJl2KjzMHT--WGXoOsPPT5c7-bON2uuUcAen-QPGbPTN-8g8cssqSvqX0YZ9nHYKT7-936P0K9NA93RVuimGO_lcdZbLzUcqF-W-Fzh6mujbARBHq4wCbjsDKRTtHzwHD76SMLKfHs7hjfKJD1fqqrvT_zd0Y1biFVvyfKi3ZqA8B-HYOVuiPKWPw2BZrMwZOKDJ-lGq9gJ-KewRRhAh3YVYS9QLPZ2vxkjf9I9qPcwMMohHkp97WsRiV4Bylzm7JvYeGj1DLf34rMGIWxxszTeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
لم يمنح أحد جمهورية إيران الإسلامية فرصة أكبر مني لعقد صفقة. وللأسف، فقد فشلوا في اغتنامها. لذلك، أعلن اليوم عن العملية الاقتصادية الأكثر سحقًا على الإطلاق ضد أي دولة! ستكون هذه حربًا اقتصادية وعزلة على نطاق غير مسبوق. لقد دُمر أسطولهم البحري، وقُضي على قواتهم الجوية، وأصبحت مصانعهم العسكرية ركامًا، وعملتهم لا قيمة لها، وبلادهم على وشك الانهيار. كما أعلن اليوم أن أي دولة تسمح لمؤسساتها المالية أو شركاتها أو مطاراتها أو كياناتها الحكومية بتقديم أي نوع من الدعم لإيران ستواجه عواقب اقتصادية وخيمة. تهريب النفط، وخطوط المقايضة، والتحويلات النقدية، ومكاتب الصرافة، وسجلات السفن، والشركات الوهمية - يجب أن يتوقف كل هذا الآن أنتم تعرفون أنفسكم. سيكون هذا يومًا حاسمًا اقتصاديًا، ونحن بحاجة إلى وقوف جميع حلفائنا إلى جانب الولايات المتحدة الأمريكية لعزل التهديد الإيراني وهزيمته. هؤلاء المجانين على وشك الانهيار، وهذه الإجراءات التاريخية ستشلّهم وتقضي على قدرتهم على بثّ الرعب في جميع أنحاء العالم. لن تمتلك إيران أبدًا سلاحًا نوويًا. شكرًا لكم على اهتمامكم بهذا الأمر</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/88197" target="_blank">📅 02:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88196">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇸🇾
تحليق طيران حربي وتفعيل دفاعات جوية في أجواء قاعدة كويرس العسكرية بمحافظة حلب السورية.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/88196" target="_blank">📅 01:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88195">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-4MO3RD6LfaJK6OhELEcUqVInszcmcm3PqgnVzbRg-LLoWLEeljsB9orS8yy5PX1TqJxGbQE3X4vLs3Zs9H9IoF3_0-t97I671mgFFr1s0I_y9wooQL43dkgR_q-5P4N_dpivZOXaKj8_40W_igMIAEF9TIvjnijz-noj_4Cfe9Jr8dxfqyfyeXpUWvju7s9Mcu29X9PHhZajpWZ5no8MCCu_YH2lBl54yDB-gjCnMlpvHONAAEzS039HVDWcJ27TO4wa_Upd3fqtWh105684SPJMDLkonKI0Boocyv3hMxRxr4r_9telGkD0jJG_uvbygtdIXWtA-q_Iwo7tfBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
اتفاقية منتصف المدة قادمة إلى دالاس، تكساس، في 9 و10 سبتمبر. سيكون تجمعا لم يسبق له مثيل - لا يصدق!
لأول مرة على الإطلاق، سيجتمع الجمهوريون من جميع أنحاء بلدنا العظيم في مؤتمر منتصف المدة للاحتفال بانتصاراتنا الهائلة ونجاحنا، وعرض مرشحينا المذهلين، والاستعداد لأهم انتخابات منتصف المدة في التاريخ. حركتنا أكبر وأفضل وأقوى من أي وقت مضى. لقد جعلنا أمريكا عظيمة مرة أخرى، وسنحتفل بهذا النجاح الهائل وغير المسبوق تماما! يحاول المجنون اليساري الراديكالي تدمير بلدنا، لكنهم فشلوا، ولن ينجحوا أبدا، ما لم نسمح بحدوث ذلك - ولن نفعل ذلك!
سنفوز بجوائز منتصف المدة، ونحمي بلدنا ونعتز به، ونجعله أعظم من أي وقت مضى. كن هناك، 9 و10 سبتمبر - لن يكون مثل أي شيء آخر. ستكون الموسيقى والإثارة وأهمية هذه الأمسية في مستويات لم يسبق لها مثيل في مؤتمر أو حدث سياسي. سأكون معك في كلتا الليلتين، وسأذهب. أراك في دالاس!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/88195" target="_blank">📅 01:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇱
‏بريطانيا تستدعي القائم بالأعمال الإسرائيلي بسبب المشروع الاستيطاني E1، وتعلن أنها ستفرض عقوبات ردا على التوسع الاستيطاني الإسرائيلي.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88193" target="_blank">📅 01:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88192">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇸🇾
‏
وزير خارجية الجولاني:
لم تكن هناك نية لإنشاء قاعدة تركية في مطار أبو الظهور.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/88192" target="_blank">📅 01:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88191">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
رئيس هيئة الحشد الشعبي السيد فالح الفياض:  المنطقة تواجه حالة من عدم الاستقرار واقتصاد سيء جراء الحرب الأمريكية الصهيونية، والجمهورية الإسلامية تعرضت لحرب شبه عالمية واستطاعت التماسك في مواجهة التحديات،تم استهداف الحشد الشعبي كوسيلة ضغط على فصائل المقاومة،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/88191" target="_blank">📅 00:42 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
