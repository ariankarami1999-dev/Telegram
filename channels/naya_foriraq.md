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
<img src="https://cdn4.telesco.pe/file/g6lBR9zvbBkS3V9j5qjD_Y9V5HI633-tIq7TkpwbtOTWYSPRUDpYqC2HnBdvi2MKUkWzTwJq8DPfXSV32dfj_XprLxNO1_DeWhlyu5D0lFPttbArCe7IvQFAPVtDPAx1uZ-RBjFu6I2Ad7tQYzAsaMoAYUkwK_yMMFrtqwPRvHAaaawgEwNzW3K3kV2hju4qeTLQ30e9Y3_ml7JocGMYlN8xfTtI_zaVNiyOJYC38MVDfNygR2K7NlEDm_FQOSCAFo9f6XcQNqF6IoA9-mNT48WdT6gapntBpY-YCjNdxFU7g21sIUrOthJerTLSQXZmJPJoOd9vPq09ElMW_MDYuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 15:49:40</div>
<hr>

<div class="tg-post" id="msg-87828">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX78VDFaS_hykjcjZNBdZJ2Ri62S2Eq7M08ubXLLMVed_Dz4HkUI95jzSxqUneGd6aYc8vpWJr5PpMTI5pKl6a_We-_7vfQpM1dEbOQKYS7P29ggA1Xq0vmuUP2KAWCVYoEMsf7y5fe3jztHy3e5aXoLSsCTYJnrxpneGhqN_5uPiXQkGRuURTtKiFMeAnuc7-yL7qStquYaszFeqpHFrTC77TM2ctrC1TAOOKWJbMKaLxs_jRDUd_PpSlsMwxajeW0AGas67fD7jhdICHN7AVUl-Hpp18wYxsx4z0rFzdkJYvlvkdCElpv7NoIfRW7Y4Vr2-5vq1mOBaf78f6-tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشوراء الفرقة الخاصة
نار على أعداء العراق</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/naya_foriraq/87828" target="_blank">📅 15:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87827">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بدأ وقفة جماهيرية في محافظة بابل للتأكيد على رفض عودة الإرهاب الى جرف النصر</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/naya_foriraq/87827" target="_blank">📅 15:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87826">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLQzhhAV-7LULPFn97kq2S8qcs8gyyP9w23aKOSc-7tFvJ_iX7a_afFA8hcf6cJPOvhJmZXTcug1XdDy3bz-ePBdpK9038zz1X-NZ_DU1pe4Hzn7Gwz7ZtfJh6uNwLCuCWyqgDOWtTns0J_gSfBoy5TuzMSd8TdFpifyIHl07TKuCa5lxKlxYQ63_BFvO6jBnWglAkcVbDgtcBGavYPh4mQIR7mRfWGdG1hFcJ1op1g_gcI_2QbJu0h_TaVkuOl2bLM2Xz0jHeY_hsxpv-I-_PbPhoZ0Zc8p-lDKMYwAuht95OpVWW9JYcbvgiQI0DZdsdGX8bP2wBW1C16i4MfI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لولا دماء بلال الوحيلي و شيخ ياسر عاتي الكعبي
لكانت الجرف الان ولاية ارهابية داعشية سلفية ..
شكرا حميد</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/naya_foriraq/87826" target="_blank">📅 15:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87825">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏قصف مدفعي متبادل بين مرتزقة السعودية وانصار الله على جبهة كرش شمالي لحج</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/naya_foriraq/87825" target="_blank">📅 15:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87824">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">زلزال بقوة 6.9 درجة يضرب إندونيسيا، وهو الثاني في يوم واحد</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/87824" target="_blank">📅 14:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87823">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇺🇸
الامريكيين ينتجون فيديوهات دعائية بعد ساعات من تداول اخبار عن تعطل مراحيض حاملة الطائرات الأمريكية "لينكولن" واضطرار البحارة للسير في مياه الصرف الصحي على متنها وكيف كانوا يحصلون على طعام رديء. كل هذا دفع البعض إلى القفز من السفينة.</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/87823" target="_blank">📅 14:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87822">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">السفير التركي في سوريا: اردوغان مغرم بدمشق وسيزور سوريا نهاية العام ومتشوق للصلاة في الجامع الأموي</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/87822" target="_blank">📅 14:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87821">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
الحشد الشعبي جزء من القوات المسلحة وحصر السلاح يشمل الجهات غير المرتبطة بالمؤسسات الأمنية</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/87821" target="_blank">📅 14:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87820">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية: تمكنت القوات المسلحة _بفضل الله_ من استهداف تحشيدات وأسلحة تابعة  للعدو السعودي وزوارق حربية تابعة لأدواته ومرتزقته في منطقة المخا، وذلك بعدد كبير من الصواريخ  البالستية وكانت الإصابة دقيقة بفضل الله وقد أدت العملية إلى تدمير الزوارق…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/87820" target="_blank">📅 13:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87819">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roeWsZJkOEJbka4BS0DyCohzhQiVvHlXyRVSFBaPp3mQ6qnV-z-oHK-t76O9CuhdWxqTtmdQd9zpf-IIwt3JfPA-koy2MffcPP021ZgYhT9XWbTPO5n1FaLyts23MKPzkyRMnIIGCTyKzzlN0ya3tFBoEA601JYoNnLZA8JBKDCekLn1e9gW4GZPIu9iOI39xKntEcgJOJKcMEqaOqeAaHkixh8IuhvWPxotoXmXeALDRzEdrNbhU4L8qwZ4hAuJZYylEaBHX1wZ0ddX-NXcF1uGk1_kE1-burln_3sUin6NmnXyLpqj8Lksr05bT1GXKbsHHIs-a_3WCG0ICj2I-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مراقبون لنايا
تحويل الإعلام الرسمي إلى منصة تهديد ليس هيبة دولة بل عبث بالسلم الأهلي .. إذا كان المطلوب تطبيق القانون، فليُطبّق بالقانون لا بالوعيد من شاشة الدولة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87819" target="_blank">📅 12:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87818">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8hPak1GSsYCv9M_BVLGnFF7YbJiIrE7A3YPNKoKw8j4vPDFBbNBIoHG8I8-dt-9Umm12IiZ82JWAD8vFtNkj03E2GTv-NGeB29CxyewtrYyjQpMWP81HP4GyoW-G13er9sH-pJZafD0hjRQU3bqd1FpMlnSbvPqN0tno6BU7tgjqGM03f2I1YWw6Yf2BXgIoQo2M6J_Tobv9-LAVSiLg1M1bdtHv5onZjxYkDqm_0rXk7y00lNhGVvc7EoyTp01A0IAQGcwzjp515LmCD2V2X5Opg9Whewzk1GNdAZqovBv6RKYHqsMkmerezWXuLjHnbEhSh4x0WxJ1TIBJBjH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇱🇧
🇮🇱
إلى أنظار جوزف عون و نواف سلام..
عائلة كاملة إرتقت فجر اليوم جراء عدوان صهيوني غاشم على بلدة أنصار جنوبي لبنان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/87818" target="_blank">📅 12:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87817">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=BgYvonnUsvgqmneqiQTzDB_wuseEWlvIpqkfADI-Hziumcto6KahfLxIQPvI8kj0AuN4TNuKNGJqExtJpDDzU8fjV4FirfyVAMtKIXzVc0WnU19TLJ00xHc5DP95_PVLixAw6Acefly9AdNXUWXYwMal5cno66tL9XcYyjWdxR88H-O4lskl4hR4GKFGgDDGAnfEMO7DfKQC8LWDn_PUjew_m1L_P0lNdcHkPe3KP8KVP661GN_VuFg7yhCKSS_0VFDG0yPki5MqxcEkLlULHawJGBPvPMouy-VS-32gsoLLqAMLiUoAxLs9UbeZE6j63iF0tyfqYlqpufDpXTOj_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4aa482a54.mp4?token=BgYvonnUsvgqmneqiQTzDB_wuseEWlvIpqkfADI-Hziumcto6KahfLxIQPvI8kj0AuN4TNuKNGJqExtJpDDzU8fjV4FirfyVAMtKIXzVc0WnU19TLJ00xHc5DP95_PVLixAw6Acefly9AdNXUWXYwMal5cno66tL9XcYyjWdxR88H-O4lskl4hR4GKFGgDDGAnfEMO7DfKQC8LWDn_PUjew_m1L_P0lNdcHkPe3KP8KVP661GN_VuFg7yhCKSS_0VFDG0yPki5MqxcEkLlULHawJGBPvPMouy-VS-32gsoLLqAMLiUoAxLs9UbeZE6j63iF0tyfqYlqpufDpXTOj_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
إرتقاء شهداء وعدة إصابات جراء غارة وحشية من الطيران الصهيوني على منطقة مأهولة بالسكان في بلدة دير الزهراني جنوبي لبنان.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/87817" target="_blank">📅 12:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
رئيس السلطة القضائية الإيرانية:
لقد أثبتنا لترامب وتابعيه في الساحة العسكرية أن مضيق هرمز جزء لا يتجزأ من المياه الإقليمية والحدود الإيرانية، وأن أي مغامرة فيه ستقضي على أي قوة متجاوزة ومغامرة.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/87815" target="_blank">📅 11:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87814">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عدوان سعودي على محافظة صعدة اليمنية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87814" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87813">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=qgISVfznDhSNWgORKjYiY55-G2cjsnHPGlAlAKhmV6I5RhIgtdEZWNYTpGAx5yFAq6-As0gtyIzEp_sFzQDDWSlBYj5g-H0GwDlj_gk_gLJWEHJ7q0aeGT6Lhz5N_Xy_6YWL--ZazBC2ScLiUAjZNt_2xKTNJB_zs6oSIQ0QMzvYX3_BRCcYWc6gutwjbjWks2FVvYaSsAgGzFTmRU8XqKW99Rt4caIMtcYWAIFHau9LbDUv3kmm4tU3t330W_DbzJ9LjNEOPy586J-IX6BhGLRYl06JwQQwyF4yuERk7c5K1YRHXac2FG78G0bcZmBsooIiw7M2t_GSA3NzSmFr_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7000ddea94.mp4?token=qgISVfznDhSNWgORKjYiY55-G2cjsnHPGlAlAKhmV6I5RhIgtdEZWNYTpGAx5yFAq6-As0gtyIzEp_sFzQDDWSlBYj5g-H0GwDlj_gk_gLJWEHJ7q0aeGT6Lhz5N_Xy_6YWL--ZazBC2ScLiUAjZNt_2xKTNJB_zs6oSIQ0QMzvYX3_BRCcYWc6gutwjbjWks2FVvYaSsAgGzFTmRU8XqKW99Rt4caIMtcYWAIFHau9LbDUv3kmm4tU3t330W_DbzJ9LjNEOPy586J-IX6BhGLRYl06JwQQwyF4yuERk7c5K1YRHXac2FG78G0bcZmBsooIiw7M2t_GSA3NzSmFr_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مروحي يحلق بإستمرار في سماء محافظتي أربيل والسليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/87813" target="_blank">📅 10:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نيويورك تايمز:
هاجمت إيران في بداية الحرب القاعدة البحرية الأمريكية في البحرين، مما أدى إلى تعطيل مركز لوجستي رئيسي، وأجبر البحرية الأمريكية على الحصول على الإمدادات من جزيرة دييغو غارسيا، التي تبعد حوالي 3500 كيلومتر عن حاملات الطائرات العاملة بالقرب من إيران.
ساهمت مسار الإمداد الأطول في حدوث نقص وضغوط على متن السفينة الحربية الأمريكية "أبراهام لينكولن"، حيث قضى طاقمها المكون من 5000 بحار ما يقرب من تسعة أشهر في البحر دون توقف في أي ميناء.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/87812" target="_blank">📅 10:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87811">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية   نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/87811" target="_blank">📅 10:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87810">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7bBAzbXPZP2KluweEdb1_DYFpApUY0XWB-73kmMdsAr1ARwf1lfaBxH3G2EDKJSdkK_bfkxBEeqXZIb2j-kAR7-j_ZmJPSbjcw4lVfPMKMDCs8vjeLsfF2kv3dMRfa3TOvGHBJ-Jx4Qtj4hV-TLsqCqskjx0TEr1rFbiSyXABxJY_V3xZn5v0yfmF0TTydfZfSZatdDE_C1diJIdStoRGgPy2RVZOZDDqm_0IDzYl8z4CG9sTj2eHomUbcI5EHkl-98FS0pj8N-NkWH_rHcP8PT6iuXoijMovk8aDMhEAMx1CwxJ9qVjbE-7SG1adYP3F9e0ZKTG1ZXRmxAwpLrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
القناة الحكومية العراقية تهدد فصائل المقاومة العراقية
نشرت قناة العراقية الممولة من الحكومة العراقية فديو دعائي لاول مرة منذ عام ٢٠٠٣ تضمن لغة تهديد للفصائل المسلحة بالتزامن مع نهاية المهلة التي اطلقها توم بارك بخروج المزعوم للقوات الأميركية في العراق ومهلة الحكومة العراقية ايضا للفصائل بنزع السلاح ؛ المضحك ان القناة الحكومية استخدمت في الفديو طائرة MG 29 الروسية والتي تخضع للعقوبات وتفرض امريكا على العراق قرار بعدم اعادة تأهليها مع ٣٥٠ طائرة اخرى روسية الصنع تحولت لكتلة حديد بمطار التاجي بسبب الوصاية الأمريكية على العراق</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87810" target="_blank">📅 10:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hel6MBFM8WUx2yi9he7Qq2iyM6-l_OpYNzxIIkrRjY2GV0zF0KtzN_06YvYEmMB6b9KEAThuKTLmS6zA7PXV4aPKXy8qwbxpnUinKT6KrM6jxdt7HVifal5fBzPs4guW38L9j8pV_dlsbZkzCSjPTPuky4UqjprHIu8jJDl3HE9-5ESPvrGturSMQ3FzzrBuYVXyUsSRui_k7LGjlfEtmgH_4A4tIRBJ19p14tGHDDEGTUw0F3E_JwMzfyxoJpYiJZX9YkT8_58nBkuMP8k1xoKf_uSSSiP119plgqrBu0zt-N2NS9FtO8rFvG2QpdovZYQo1Kaa6yNA3xU4bhyuSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87809" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/87808" target="_blank">📅 09:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
القائم بأعمال وزير البحرية الأمريكي:
عالجنا عددا من حالات الصحة النفسية على الحاملة لينكولن.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87807" target="_blank">📅 01:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87806">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579ffff276.mp4?token=KJIe7CQ8dWLBQORKgv4u8s9ezrp8Oz-1-zPdzLzQIkpbNf0tgyR0YrwftZy0Trlzf7CmouUZd6HkjCcSa5gG7nwpujg7ZU9A54GekYL5hcJwPGwKfVBJ3nW9rPk_TlPUL9NWSqfMGok1l6_P-8_8-NKlhjqIrkwnsHbgn_a9nFhDQDM3a2qWUYN9G3c0Dx4Fy3ZFTAGmp-UlH1PmKHnZJ6zLbXndL2jDbPT_vZDzjUAtE0LbAveh8aIyxCfxu3aNz_bgqX8c85cWwxYzssEPmYdlgJPYpHSyJXL_gbgcejG3LMTjKjGt_gSSjfYI-YJvMFC1fMa7svkc0GVr06POXQAHWq4NSYgLLCm8KQtdCaiptWqY9DCM43N12Pt1aor1Xo7V27MesxRpUJuiDXKzd8bMJKdX5P7zfuZ2igMCyT0a177fqTunidEVBsrTUQ_k5Ms2ei6LvWXF7QIKXdBuAprQrPN2yH3DJDjOgEmcjh07yOEy3HlqZkAejtQdkQqofxLDiS1ghJCNlxWnX2gmqhycDQWVJoadbU_9T9E7v0YXeMWf6mMiqU2ffwkb_TZiDfNAH8JYHUqO18DCWLQb-U2KUkjtOTj_5OgURJZkullTnGNPw1wM-VQ3v4sibB1lFSm7gobPb_OEd5yQ3hKAsT8PJRHSYCWV-QPMPz8RUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579ffff276.mp4?token=KJIe7CQ8dWLBQORKgv4u8s9ezrp8Oz-1-zPdzLzQIkpbNf0tgyR0YrwftZy0Trlzf7CmouUZd6HkjCcSa5gG7nwpujg7ZU9A54GekYL5hcJwPGwKfVBJ3nW9rPk_TlPUL9NWSqfMGok1l6_P-8_8-NKlhjqIrkwnsHbgn_a9nFhDQDM3a2qWUYN9G3c0Dx4Fy3ZFTAGmp-UlH1PmKHnZJ6zLbXndL2jDbPT_vZDzjUAtE0LbAveh8aIyxCfxu3aNz_bgqX8c85cWwxYzssEPmYdlgJPYpHSyJXL_gbgcejG3LMTjKjGt_gSSjfYI-YJvMFC1fMa7svkc0GVr06POXQAHWq4NSYgLLCm8KQtdCaiptWqY9DCM43N12Pt1aor1Xo7V27MesxRpUJuiDXKzd8bMJKdX5P7zfuZ2igMCyT0a177fqTunidEVBsrTUQ_k5Ms2ei6LvWXF7QIKXdBuAprQrPN2yH3DJDjOgEmcjh07yOEy3HlqZkAejtQdkQqofxLDiS1ghJCNlxWnX2gmqhycDQWVJoadbU_9T9E7v0YXeMWf6mMiqU2ffwkb_TZiDfNAH8JYHUqO18DCWLQb-U2KUkjtOTj_5OgURJZkullTnGNPw1wM-VQ3v4sibB1lFSm7gobPb_OEd5yQ3hKAsT8PJRHSYCWV-QPMPz8RUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب عن إيران: كان لديهم 212 طائرة جميلة جدًا، بعضها تم شراؤها من الولايات المتحدة، وبشكل ذكي، في عهد أوباما. جميع طائراتهم اختفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87806" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87805">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6da41714.mp4?token=Ir8aYFuQcGALrA33RPLnx42v25xDiKtBSVwVEkG7GnG_Fd4WAFJrcrOlm5UT1kilCb_hxCjAQvRKeWirB5_xHa46uh10H-VWBP9Hdwcy_4mDPxapiDI1HHVoEyN66bXGb4aSgBAYrblqVziU3mQbcS38xdZcm5MDoOVD_o53xdxw4PqB2KoXIbDGyKYIXnowJti9GFktIa0dEHHxgDLMyr7Cfbeh85Voyx8c4W20ayy0vuFTrtL-xs7LecVh-S7QxvLlurs_KV6AWk6Z-9PNTrrmZplLUn8UoBTeM_D3-NSeCl-Fm1XUSmOpPuqto3e9gc4lJVNSJOcov6PlEAYo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6da41714.mp4?token=Ir8aYFuQcGALrA33RPLnx42v25xDiKtBSVwVEkG7GnG_Fd4WAFJrcrOlm5UT1kilCb_hxCjAQvRKeWirB5_xHa46uh10H-VWBP9Hdwcy_4mDPxapiDI1HHVoEyN66bXGb4aSgBAYrblqVziU3mQbcS38xdZcm5MDoOVD_o53xdxw4PqB2KoXIbDGyKYIXnowJti9GFktIa0dEHHxgDLMyr7Cfbeh85Voyx8c4W20ayy0vuFTrtL-xs7LecVh-S7QxvLlurs_KV6AWk6Z-9PNTrrmZplLUn8UoBTeM_D3-NSeCl-Fm1XUSmOpPuqto3e9gc4lJVNSJOcov6PlEAYo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87805" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87804">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏
الوضع بين الولايات المتحدة وإيران مستقر.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87804" target="_blank">📅 23:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87803">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87803" target="_blank">📅 23:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87802">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5DCliryMjwLImi9a_nycHOr2m2-7N98SioGVAYhFQqGyitgOFPFY0GULQuuzR-pH65nRnDq7zIaEE6iTC6t_jGzu0-MyB8M_M37wt1GeCe1wUwlPh7VByc5rmDlpNKWx85mN-79Prlz_f-54S12Gudjv7shaSeSW6HbLDXCAD6ADUQrWts2CChEIabPboAAClETGE5QWo9WfIxZRf_p3Qwjzg0NZ7fiAPBVESjPjxWcxXFzGaBtPB5qIqA6I3RT6pWghvaERJwOyuc95d1oQw5euuWiT-4wzfO5mNQYT4PSTz6_EgPdlF46SVMfRvSGxG-O0xrLrgKfVy0EJhbThWY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba96a06df0.mp4?token=M5P0fRWwEq80Qozd77taeeIbJWQbfnlXAu-CLm0zBBWOkV73FDHqB1fYKDX8hlk_0D8gW9LYJuhpLr94-JuqRiAzmvRFkwpQMsgMAmmSP8vnxxlQUVRNY1nHj_B91vi3L6cvpBttjVcFK_xdcZo4QnARBjTozC-gmaFTWdAh_TcUIQrZN5tssEeEYp7CvmNnrLp8AM7eD0veYlVD8nL1Z3dp2LKDSkDuSfIXXlsIeklz4qiV7qQYNzCdSxaI7lQ5xZgCnlNgvSiySdtVUzXrsoambaUInzfGxvIkjpqhDXBwJI7WZF3TG0SH1_s0L2rJohGOhUlB80Y1ENpfBkjz5DCliryMjwLImi9a_nycHOr2m2-7N98SioGVAYhFQqGyitgOFPFY0GULQuuzR-pH65nRnDq7zIaEE6iTC6t_jGzu0-MyB8M_M37wt1GeCe1wUwlPh7VByc5rmDlpNKWx85mN-79Prlz_f-54S12Gudjv7shaSeSW6HbLDXCAD6ADUQrWts2CChEIabPboAAClETGE5QWo9WfIxZRf_p3Qwjzg0NZ7fiAPBVESjPjxWcxXFzGaBtPB5qIqA6I3RT6pWghvaERJwOyuc95d1oQw5euuWiT-4wzfO5mNQYT4PSTz6_EgPdlF46SVMfRvSGxG-O0xrLrgKfVy0EJhbThWY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن إيران
: قريباً سأعلن مضيق هرمز أرضاً تابعة للولايات المتحدة، يجب أن نمنع إيران من مواصلة أنشطتها الحالية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87802" target="_blank">📅 23:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87801">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=ByLDQH-oVP57z6EK_GT4DEz81mSh9sI9XNAEtpKLK1R1rsaHLHBvYrw8q-seBqNf3m-iln-HquKvmKESRKQL2HzENtD3SGpX8IpHjS_dTvojz0ddUGfzbbL3ytet_voIXz8AYnEe7Ai14S1Jc5hd6EpTQsJXB53FpZmZbwUoebaGcC3Svvg_2CIN17Im9Kcjl5-kTMZVusuPpGgxw-VgHKEdED9P8ElgqBtbahwM77LDER8KVFpDxffAauxsp1NN7ycCxK1EackpcdGEpa0K0QDg4LKm_qa0Ie4vcctsc7KNFAxSar4jZwYhAUFpJTiqO8D09aD6xJanKhX18qaCPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ca3fdb17.mp4?token=ByLDQH-oVP57z6EK_GT4DEz81mSh9sI9XNAEtpKLK1R1rsaHLHBvYrw8q-seBqNf3m-iln-HquKvmKESRKQL2HzENtD3SGpX8IpHjS_dTvojz0ddUGfzbbL3ytet_voIXz8AYnEe7Ai14S1Jc5hd6EpTQsJXB53FpZmZbwUoebaGcC3Svvg_2CIN17Im9Kcjl5-kTMZVusuPpGgxw-VgHKEdED9P8ElgqBtbahwM77LDER8KVFpDxffAauxsp1NN7ycCxK1EackpcdGEpa0K0QDg4LKm_qa0Ie4vcctsc7KNFAxSar4jZwYhAUFpJTiqO8D09aD6xJanKhX18qaCPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
We are the king of Hormuz</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87801" target="_blank">📅 23:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87800">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
ترامب
: سأضرب إيران اقتصادياً بقوة .</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87800" target="_blank">📅 22:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87799">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇾🇪
مشاهد من احتراق السفينتين في المخا، بعدما تم استهدافهما من قبل أنصار الله.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87799" target="_blank">📅 22:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87798">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=TW-cIjnES-WRqckaY5LCAbrkuNxh5e1F5Bec4DeTDaEpFJNlnRbqO1Brp-uOiegSm_c4Xcc3RKT21g5hFulQwOnn9p4ie_5oon9SzXleKxcZQwfD9t7z1CojDeyEOr4UhDQecQMdEc6EIaJJ_Lp6_h55CH0uCf0bZUh2obj10encC6R1InsuIcqVwJVhTLjFarcfF79riXxAytXhq3iiTqyW0eb3xa6tRLO3-2gMk1k6W7k7xLwo-VCs5em3fk-mAXzDvPldJ1IXf4eupFKwBLusysB33TB3N6gBTeb-a7_ne9JZnkGDTpIICJK7XsZCM4FHwga3kI009cKbUBU5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e601d104f1.mp4?token=TW-cIjnES-WRqckaY5LCAbrkuNxh5e1F5Bec4DeTDaEpFJNlnRbqO1Brp-uOiegSm_c4Xcc3RKT21g5hFulQwOnn9p4ie_5oon9SzXleKxcZQwfD9t7z1CojDeyEOr4UhDQecQMdEc6EIaJJ_Lp6_h55CH0uCf0bZUh2obj10encC6R1InsuIcqVwJVhTLjFarcfF79riXxAytXhq3iiTqyW0eb3xa6tRLO3-2gMk1k6W7k7xLwo-VCs5em3fk-mAXzDvPldJ1IXf4eupFKwBLusysB33TB3N6gBTeb-a7_ne9JZnkGDTpIICJK7XsZCM4FHwga3kI009cKbUBU5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية استهدفت سفينتين كانتا راسيتين في ميناء المخا.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87798" target="_blank">📅 22:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87797">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تستهدف ميناء المخا من جديد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87797" target="_blank">📅 21:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87796">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=odC9ljotd-h_xOobshBiqGS8kPmqWPfvEf-WOlDEKBm1FGVGPRzEUM3sD7DucjzF5BbvZvn0zeghwVAdXeVCED0CfdCvurXkjTke57LJ7GUUJCTvY4aZaVF35BFHIoTb7ng_SqJeb6IWH5yipD7XJuvwu0xaFhlPuDfFzlC_GDqO136wpNLvQkpuZfW_aa5Aq-wo5qwwU-4KKS_4Klhl4rUmA6xlr7TVSy8GnGDdcE9Hj_epvMimV_I1IRwm-Q9aUAJ39S0uFWBO8xYPGqZQOyJdOxu2Ug87ebGOHVpvhYOwEpVU2xpvxHttr6cR8ZKmdfZaj5sbA2CjIDQChjmsMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789a1d80f8.mp4?token=odC9ljotd-h_xOobshBiqGS8kPmqWPfvEf-WOlDEKBm1FGVGPRzEUM3sD7DucjzF5BbvZvn0zeghwVAdXeVCED0CfdCvurXkjTke57LJ7GUUJCTvY4aZaVF35BFHIoTb7ng_SqJeb6IWH5yipD7XJuvwu0xaFhlPuDfFzlC_GDqO136wpNLvQkpuZfW_aa5Aq-wo5qwwU-4KKS_4Klhl4rUmA6xlr7TVSy8GnGDdcE9Hj_epvMimV_I1IRwm-Q9aUAJ39S0uFWBO8xYPGqZQOyJdOxu2Ug87ebGOHVpvhYOwEpVU2xpvxHttr6cR8ZKmdfZaj5sbA2CjIDQChjmsMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل
: أفراد عائلات أفراد الخدمة العسكريين قلقون بشأن الظروف على متن السفينة الحربية "لينكولن".
ترامب
: لا، هم ليسوا قلقين.
المراسل
: هل استمرت مهمة الانتشار لفترة طويلة جدًا؟
ترامب
: لا. لا. لا. لم تكن طويلة بما يكفي على الإطلاق.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87796" target="_blank">📅 20:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87795">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87795" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87794">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇱
الاعلام العبري
: أميركا وضعت فيتو على طلب إسرائيلي بقصف أهداف في سوريا.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87794" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87793">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
انصار الله اطلقو خمسة صواريخ  على ميناء المخا.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87793" target="_blank">📅 20:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87792">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
مشاهد جديدة لميناء المخا وهو يشتعل بفعل الصواريخ انصار الله.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87792" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87791">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=Y2KKiShXGRiSUljuN1a9oFfbQ5TxQF9A8HYbLrep3QrED8OiHC3Pf0wEGixSBDMs3y7jrJzL2J2ad1cQ7t0gTP5Q6TI8Y0iydJeeUBQUgl5EEbOT7Sh7ONv3HQy9wQCqNXv-Xelq0gHQfCEJo9PhjbzX5IRtFyKXzd8DekJThGObEsw96elI2DFmPHBTiPMVUS7jJlblCV7gHenXNyp11bdJeihimrOhu8sqSlk1sderT_VjxqSesjwD1pvh9vhHMqHQHbTbre00nH_mSKJwt_NXTOicZzS4DDFrVUzYvLgZNXL02qgdzNEythvWprpZmUy7TVckf40jpFdk_zDb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1341d9e0.mp4?token=Y2KKiShXGRiSUljuN1a9oFfbQ5TxQF9A8HYbLrep3QrED8OiHC3Pf0wEGixSBDMs3y7jrJzL2J2ad1cQ7t0gTP5Q6TI8Y0iydJeeUBQUgl5EEbOT7Sh7ONv3HQy9wQCqNXv-Xelq0gHQfCEJo9PhjbzX5IRtFyKXzd8DekJThGObEsw96elI2DFmPHBTiPMVUS7jJlblCV7gHenXNyp11bdJeihimrOhu8sqSlk1sderT_VjxqSesjwD1pvh9vhHMqHQHbTbre00nH_mSKJwt_NXTOicZzS4DDFrVUzYvLgZNXL02qgdzNEythvWprpZmUy7TVckf40jpFdk_zDb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
قصف صاروخي من انصار الله جديد يستهدف ميناء المخا</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87791" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87790">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87790" target="_blank">📅 20:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=I5M-bZz5e-30eoXTbmCR36IF7mHurGeGtJXiWIUnkvwQfFoWmW4dkKaUSfDRRMV3wAkHvOH1OH8jJtiBVc7TGRi6jcijme1ARtZlCi3bsuPyOd1co4QyOF6bWQ2-n5lVXh_9D4QrnudU4E3ZlhyOhXOTuYI868yKaQAOsa8o7DNXf-x3g4eRcePjhmkG68KWOIl2S93nSpkpL2Q96_GhXct2_DMcoUvZNIG56jbUgre4FKu0WCWQzJ41ohvtpnjhJbeGijn6kXe7Yoxtu4J218uAGxMz7azGPdj8L_1bgBAfSGI_xMoH6YTcbSCiT9Ramicc87YTFt_-JjlHDsbnqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefbba7708.mp4?token=I5M-bZz5e-30eoXTbmCR36IF7mHurGeGtJXiWIUnkvwQfFoWmW4dkKaUSfDRRMV3wAkHvOH1OH8jJtiBVc7TGRi6jcijme1ARtZlCi3bsuPyOd1co4QyOF6bWQ2-n5lVXh_9D4QrnudU4E3ZlhyOhXOTuYI868yKaQAOsa8o7DNXf-x3g4eRcePjhmkG68KWOIl2S93nSpkpL2Q96_GhXct2_DMcoUvZNIG56jbUgre4FKu0WCWQzJ41ohvtpnjhJbeGijn6kXe7Yoxtu4J218uAGxMz7azGPdj8L_1bgBAfSGI_xMoH6YTcbSCiT9Ramicc87YTFt_-JjlHDsbnqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
استهداف مباشر لميناء المخا معقل تمركز العصابات المنفلتة الغير شرعية في اليمن .</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87789" target="_blank">📅 19:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الشيخ نعيم قاسم:  - من يراهن على الاستسلام إنما يراهن على سراب ولا يعرف المقاومة جيداً بأنها تتحمل وتصبر هي وأهل المقاومة  - اتفاق الإطار الذي ذهبت إليه السلطة اللبنانية ليس لا اتفاقاً ولا إطاراً  - اتفاق الإطار هو إملاءات إسرائيلية بالحبر الإسرائيلي تُوقّع…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87788" target="_blank">📅 19:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87787" target="_blank">📅 19:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bci4xoPq2SeRL5vwo2x0Ax9SV_XZO0iOeTBWQcWlss5DsWMo1Q4ypAljTMNzZNCs2fqrWuGtp3my-84SKXde-RX3UF0Vwyems9fvxg2ZyXnN_id_7FHmx4AGC0gnjUf6QbQavkuYOrj-pUpDTNzNPXEHiPeHYEd7yei9NLaLBWNTp7XFs6yR3gERNJLeILL9YIU_T-aaNjkK7pOGujJc92x-d3dnu7XRTiQgWTa2D4hQcEKjbExIbyqp6fowoZ_kpDOaxXO-JoR4M4FhFFxxIMa_wc9j9bfJ_uH3E5W723mNXaBVOY1rvZVeAc3ENh9obLF-IZlnGH1hnRNfL6hmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇾🇪
وزارة الخارجية العراقية تلتقي ما يسمى بـ"السفير اليمني" التابع لمرتزقة السعودية وتعرب عن تضامن العراق مع الشعب اليمني خصوصاً في ظل تصاعد الأحداث بين أطراف النزاع وما نجم عنها من خسائر بشرية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87786" target="_blank">📅 19:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇶
الاستخبارات العراقية تلقي القبض على (23) أجنبياً حاولوا الدخول بصورة غير قانونية إلى البلاد عبر المياه الاقليمية العراقية وباستخدام الزوارق البحرية السريعة.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87785" target="_blank">📅 18:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVub8QdMzOTVGTCWOv1v7C4BcGM9cwYC5Jr732IDI-AXw5NeKOvd8JWTK_XFUzfW0qUer_Rq-K-UvElDbBR44nfgjMjfzziyfuheKyQXtTvlkkdz-oZBvpCRG8R4spx0v9gs4rNK6fJXswRPtJoI3MTTuuGheD6Y_Ot7L_PV3O7cYpG19N1BhACXY_CiM0gNvmjM36zRKf71xcHOLDJ9PRpfOvJQ6EpJyIgIub-FAMxB1W43zSv9amyWgnbA0g9qwhOzzx0HjgavyibeH7zp1UU3owrfe6xpZ0Tf4MYAXeluYquRG1pos0VD87bs-XfkCI9ZuDWbw5MFRzNZqV6JoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
طيران مسير مجهول يجوب منطقة البلديات في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87784" target="_blank">📅 18:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
شرطة البيئة العراقية تكتشف كهفاً في صحراء الأنبار، بداخله نهرٌ يحتوي على أسماكٍ نادرةٍ جداً عمياء بلا عيون.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87783" target="_blank">📅 18:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🌟
🇺🇸
‏محكمة الاستئناف الأمريكية تقرر ايقاف مشروع ترامب لانشاء قاعة الرقص في البيت الأبيض بكلفة 400 مليون دولار</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87782" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTviscKMSlmgIJpetp1dC8xQz8u7Wo5zASfAtO8DyuOKkS8Yo9CTjFRUfVhfRvBYhr3Ev9biKBRdTSS02MX4SAhRawY2rY67-P5hChEbVsseEhV-kSwoXl1GkeY5JS_WdkdDARflpXGux9jmd3dFuxyJK0ZqTNJlKb8aYQKP_Jx11LPRXoAiw9wxypt27ky6mj7_MV_m9A99jcsRR8WpiP4-v35kV5Sir81LkUf5ILPka_1SBN7xEf8r4rR9bh_h8IYAEp82mgDa5oxgGMbbDZclbPhTNv7_wJLV5t5Td_GT4tcE8aUisTySCJx_ESMrqJvBCkdiw02BUe9uStbOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
منصات التتبع:
شوهدت اليوم ناقلة نفط عملاقة تابعة للشركة الوطنية الإيرانية لناقلات النفط وهي تقوم بتحميل مليوني برميل من النفط الخام في رصيف أزارباد في جزيرة خارك بإيران. ‏رغم أن هذه أول عملية تحميل تُشاهد في الجزيرة منذ نهاية يوليو، إلا أن إيران واصلت تحميل ناقلات النفط في محطات أخرى. ومع ذلك، يبدو أن إنتاج إيران من النفط يتماشى تقريبًا مع إنتاج مصافي التكرير (الاستهلاك المحلي)، مما يعني أنها قد لا تحتاج إلى تصدير كميات كبيرة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/87781" target="_blank">📅 16:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3k15wsRvhtm6xU3p-jsscWwRK69ST2xhBjPkOZsNHc9geupworUE9ZPdwABeyoY5Z9SgL4LEa-bLmVKGFONl-sc95bAxTb94Or4Z6ayO26ppAAgcKb6WRjJ8jfIUh9GXMfNsvJbtMw3m2NZUhkAsZ_zoeolZQkIxZMxePDOpkDt4XmgRV6j5OvVKnhBYSMzxryHTNwVMDOKTBQUiGBhYvFTMRUe899B7n1Comz3VDeHuj7_Wd9z_dX-mziNzJFkkNCz1p_U34XT00OcezUYaNPhRhOEEDbIz5WAbDJKtWfz_g2b3QbqST2p-1P65frJeLwSnthuYT8F81-gNJDo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇺🇸
‏
ترامب:
لقد تعرض نصبنا التذكاري الجميل لحرب العالم الثانية للتخريب بالطلاء. لا توجد إهانة أكبر من هذه لأبطال أمريكا الذين ضحوا بحياتهم في الحرب العالمية الثانية. أولاً بركة المياه العاكسة، والآن هذا. نحن نتعقبهم! من أين يأتي هؤلاء المتوحشون؟</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87780" target="_blank">📅 16:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87779" target="_blank">📅 16:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزارة الخزانة الأمريكية: الولايات المتحدة ستفرض على إيران عزلة اقتصادية غير مسبوقة</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87778" target="_blank">📅 15:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
كلمة مرتقبة للأمين العام لحزب الله الشيخ نعيم قاسم اليوم الجمعة عند الساعة 18:30 بمناسبة ذكرى الانتصار يتناول فيها آخر التطورات.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87777" target="_blank">📅 15:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87776">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اكسيوس:  في الأسابيع الأولى من الحرب مع إيران، كان بعض أقرب مستشاري ترامب مقتنعين بأن ترامب سيدعم نتنياهو في الانتخابات.  في ذلك الوقت، كان ترامب يُطالب بشدة بالعفو عن نتنياهو لإنهاء محاكمته الجنائية.   لكن مع مرور الوقت وازدياد تعقيد الحرب، بدأت مصالح ترامب…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87776" target="_blank">📅 15:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📰
اكسيوس: تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87775" target="_blank">📅 15:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📰
اكسيوس:
تشير غالبية استطلاعات الرأي حاليًا إلى عدم فوز نتنياهو. الرئيس الأمريكي ومستشاروه يدركون ذلك. وحتى الآن، لم يُبدِ ترامب لنتنياهو الدعم العلني الذي يأمل في الحصول عليه، رغم تكرار سؤال الصحفيين له عن ذلك.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87774" target="_blank">📅 15:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87773" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87772" target="_blank">📅 14:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
‏
رئيس لجنة الإعلام الأمني العراقي:
التحقيقات مستمرة لتحديد مكان إطلاق المسيّرات باتجاه أربيل ولا مؤشرات على إطلاق المسيّرات باتجاه أربيل من داخل الأراضي العراقية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87771" target="_blank">📅 14:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87764">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFnq7AZIn_nTQn9CBRk8JJm_O1tupeFUKRnEFj3XvvJk3JVLbAS4ZSCHj9wXZ174g4VkHdt8mZi3TxaZzr-KlC2u3qGy1vh3TfuNgZNppk9wN__R3E50C0AfdRp5Q-VmsooTZwVmQiCA6XzlDuisWS4bIqIt9fqk8s1hx-_y2W9OhNQoEvv0rTUE60nC1aSCe5MzBHVUCSHI634pJGbOW7wIBXRivqpAgqKdCTs2bzgziar8ugzNJNHMwukyCvgBP1GwyOe3y9oV9PDrOcyxlExE78iwCXMA1vag5-mXggm2fSNDMgvsfiFZnWYst2ePVtBeZOZypvFKAK4IMIdaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfnyzzLYAlDLx_J9DiOJN6ukFTr-7FXIbrGHad-lR13hb0t7e0PKBDHJG_FRzypcg6Dq9dlZDmW9G7hpn-B0hDvNL8a2Gcg7ZaDkSh1smLOJ4EHNBhSMTtpY4jSH8uQFbA2w9P-4t_HP9Cuin2XisnVqL6lXAP_I0uXuFotspiSxHx7WPiyVM4HIwHrInHr2UjCEoL-yrxfTJ6le1Y6CY8BOm2P9fdyIP4-MWfvjl34FacNGeDf3Jw-WV5dM95-pPER3ui1-PrFM_VR7q3pWTKgQEAic4EEunF5HbAgQrdE5iLxGSbgHIambAo2JIRSZG0mysiwhi21o2Al_brq7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUWNsAbbgWI0eY6lWV-wt93Xsc_49iHX2PKyOIEzu7VF5KLnAt1Uw2cqX4l7XvqykxuMaykr46lTVXQ5eUksFPiFxBleES_W-FqAmlkwyzw1JTEZeYmE7LTXVdMv6qhsBCmsiOq_3KslxLBTs3V37BYCE4IHtBB48iDa4Kj2J0nxJ7ZStgM9EdYxXTxMpcUCmkCmerkXQvU655S9tdIsPOgmthctggP-jmClLECDdzMK4U89XxBJbT3LfTld2OHNHDeh4SEN_BP5zHxNobgOs5SWiDV8GoDwv1dvDWWL0QrUWttOvddfAW6tVpYEvt7lHqksOOpMBrEw8fPnyprTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2yRt1uXuozRIupElF3GdVWVZvSlsPIzbczDLp24n33o5hgglZJwYe8M6M17gFUSlyFIk-9BJCIXbBvzpitQQ9QXUcy8C9d6HOX18HZTb9l5Y7EoSYqIwkVT4jb8xqLlpVdBMiLKO9jp63jdG1uurG7KGjQZ55Crgt08xBtFeLQsEQAzuGPPK_z-M_xZ1iL31SIDkT33jHpppPigaoTr9oZrY_Bxwq9VUcdVcOXor0f6KC73fIUwZOXTWmlCgBcVSiogCGuoBelPkei8eK81wspuhR7xGzqijPh7tr2vrgbQi0c7Zc-VxCBY1TWlwsJ2NGZWU6bVH72hYCYiGf5M8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fx8kYnMaHgTcoui12q4m3m6vFQVM2Fd98YQhIfyS1CSsy0fQva0jtKBFODKUYgIbwa_jtLQRSHxbUhuxF6p0Encey7-DySO3-xxHqFUJmECbxwOLURo3v_HeWiNIyqPzJapx2A2B496n3LKmruCbLndNexQ7wjB5px_O43wYXVSM2lOqKkJHIwEr-gPRKITVrsxpX0dYbViLuaDQc4xDprqpbIzpROWXn2yuAdxRuta6O18vOyngk_pCprg7eo4FdqZMafZBGYbwTrKQBcXwYzPIF_UAOT1nnejcspgXTFd5Se9s2fHxaaSuJ1PNxAp06glCi1gPdYzXiEXSoqFXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvDiMVi2FNsKyV-VDYyURvhoj_bb1WVEl_50c716geCh_U7epaCUbvPcGj9-kPM0gt2y98j9jiPBL_cozqmT66vH9Wh8WFfZaibj37xNF-a81CXIZp-CgM0APT6rMTO2dJDssdsxtRb4m1aPy9lbhYwDm9rpqIhGx6bpV4QRV8wV89xuXV-vCZm2vrMAohEVGmXuOk_vBeePDyQCnRJhu8BYNyPWD0F8K379aJ_ZBEb4OHhdFuPJ7iJ6qeBN-SnBCLHV5_KOFZVDtm3VuupGvB5HKdo6MY4M4bAeAIRvVs-NZ4-gxImTcu12nrsbE9igJSuAsi2gi2iQUgLCY2790g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfpJaz2D1_K4MQcJWgZMxCDO6-4khfm58XHRfkV736EpV4l9bUOZqT-b60urmSDPwcn3-YCaTaWDVTQzW8ehHP5sqYJYUffAbzRsLRU_oW-2kDu5moJJUYwi7RPFNbICM-0OIFlBM0W3CbywMQpvopADPC3tfN8x-eGEjzovzPF_BlJ9xf9x3Woti8WnnvwvkCXcAOAuT2ylN5kTbSnNQE703rg1Ca9Y3MM_DzfGI-DzGOfjEFrhMs_TixxETtj_a05XuHSZszF6GfAg0F5H6aJMOsB63yRPAql9IHSLDxHBO9H0rE4uj_TxUX5OQ8fWg4IE9W9qy8Pg-VR61KU6EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
صور لطائرات مسيرة وطائرات مقاتلة أمريكية إسرائيلية تم تدميرها بواسطة
الدفاعات الجوية الايرانية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87764" target="_blank">📅 14:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87763">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مسلحين يهاجمون وزير الداخلية في إقليم بلوشستان الباكستاني في منطقة مستونغ.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87763" target="_blank">📅 14:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87762">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87762" target="_blank">📅 12:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87761">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي
لافروف:
لن يكون هناك هدنة في أوكرانيا. موسكو لا تنوي إيقاف العمليات القتالية على خط التماس الحالي.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87761" target="_blank">📅 12:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87760">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eggGijbe_lwXFmjG_nLh5J2A2NAPPb4bmNljQr4_XVfzM315hNHr9TFK5lOAgAt1grC4dq5hGdD70WPTGJdVvdlRj17WsdTcvJ-Tf0KzwJW1vSVdw6yGc5IATBNOHrceTbco0ENg4J0trhZZDanqvunelVdKv63pkvGGkbH3DdT8_Xe6cGNRPz1fYnlebR1N4EXNgL6pXD1rJUUsQvkYM4YDYzNSn7zqvGqp9o6pS2BjfUVYBygqJdUTE_8cRCc3pGKYhmq_yae2Ox9qJ3W1CIy3145ApHd_9mBS2t-ZuTudOS4AqS3f3ghbK057CZjJRGjaces-L6_xQhuJ5XSnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر
🔻
إستهداف سفينة "ناقلة نفط" في مياه مضيق هرمز والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87760" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87759">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الشؤون البرلمانية في مجلس النواب الإيراني:
تمت مراجعة مشروع "الإجراءات الاستراتيجية لتأمين مستقبل مضيق هرمز وخليج فارس" في لجنة الشؤون البرلمانية، وبعد الاستماع إلى الآراء، تم اعتماد مبادئه العامة.
أحد القرارات التي تم اتخاذها يتعلق بمنع مرور المعدات والمستلزمات التي تملكها الولايات المتحدة وإسرائيل والدول المعادية عبر مضيق هرمز؛ وذلك لأن هذه الدول استخدمت مضيق هرمز لتنفيذ أعمال عدائية ضد بلدنا، وارتكبت انتهاكات وهجمات غير أخلاقية ضد الشعب الإيراني.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87759" target="_blank">📅 11:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87758">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇷🇺
🇺🇦
وزارة الدفاع الروسية:
استهداف سفينتين كانتا ترافقان سفناً تحمل أسلحة إلى أوكرانيا.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87758" target="_blank">📅 09:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87757">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=nerv3MNwiW_MSDh0twG-5FBiB_YbI0uyqKQPlCK7MCDJ-WSR912lfHQe9BxIXNF_U6Oze2cIcTegx1LP1CGxnZm-0DFng64THgUPkaBoo3Yr8e4fUGyCzb9GzPCEvRpv-bBkzqq-rpuTJplB3681IFu8wf-eFzJCxBvjg0sV-BCGMpOi4SceklH_kgDpa_-Zb2rsL3ze2VV5P-_u9ZVMr9mOGedKO8FqqCL0YikGiAzlYkD7yY6EGiznEjaNzaunpqmeFJSc0QRs9Cm0YmHz59JNltpMdj5z0fGEnvtXVi1nQA1w4ZF_VIdIJ-FNJ7LIOu249Pm5qu52vE5HKdgAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed4908a7c.mp4?token=nerv3MNwiW_MSDh0twG-5FBiB_YbI0uyqKQPlCK7MCDJ-WSR912lfHQe9BxIXNF_U6Oze2cIcTegx1LP1CGxnZm-0DFng64THgUPkaBoo3Yr8e4fUGyCzb9GzPCEvRpv-bBkzqq-rpuTJplB3681IFu8wf-eFzJCxBvjg0sV-BCGMpOi4SceklH_kgDpa_-Zb2rsL3ze2VV5P-_u9ZVMr9mOGedKO8FqqCL0YikGiAzlYkD7yY6EGiznEjaNzaunpqmeFJSc0QRs9Cm0YmHz59JNltpMdj5z0fGEnvtXVi1nQA1w4ZF_VIdIJ-FNJ7LIOu249Pm5qu52vE5HKdgAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة انقضاض المسيرة الانتحارية والانفجار العنيف في مخبئ للقوات الأمريكية بمحافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87757" target="_blank">📅 03:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87756">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=FkAPmQQ_CLfJyoEqgv63-jsg4C1RnozxKS6VUpQpdzSYmZAY2nDuWs-FjWT17UIRKNsROV0kjcx1a1DpuueqQxBOxhL1yUJSsXiZn_3eI4SzFj3EB5PNSZSCMXFE-YfYHHeQ0cj4ZJhQEFeBCQUoV7W6yB_jWwutB3QjjSMMdXll8AUCE0cxQjK8EdRPZZT9lGwN3zA65ajdMR6K7F_RwGIV6TVDTXzgdstS4hCg2bsN8t0jRKO-9OsqujfD3boPw5L4pZIKOGU6r5Vj18tk22d8DVPQhbJDFJkEq8x0EIOm3vhBrqiKjbNaDwZokwb37pAJnzrCthTZTon0yvb_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb53d6775a.mp4?token=FkAPmQQ_CLfJyoEqgv63-jsg4C1RnozxKS6VUpQpdzSYmZAY2nDuWs-FjWT17UIRKNsROV0kjcx1a1DpuueqQxBOxhL1yUJSsXiZn_3eI4SzFj3EB5PNSZSCMXFE-YfYHHeQ0cj4ZJhQEFeBCQUoV7W6yB_jWwutB3QjjSMMdXll8AUCE0cxQjK8EdRPZZT9lGwN3zA65ajdMR6K7F_RwGIV6TVDTXzgdstS4hCg2bsN8t0jRKO-9OsqujfD3boPw5L4pZIKOGU6r5Vj18tk22d8DVPQhbJDFJkEq8x0EIOm3vhBrqiKjbNaDwZokwb37pAJnzrCthTZTon0yvb_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تشعل سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87756" target="_blank">📅 03:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87755">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=HGndCi50b3GJ2L6X2foolD6acR8v-xH9mgjn3faT56GA_edNFMUsgMRy-5K-Ze_HE2OT58jaf97qKhPtbJfAYg5zRF2DRNXAhutqWYn94qUs5eI-s6UzTF8HrrJGpEQfH484A1Abxiq7W5rPqVIEVA8lLCjSdC9bSQ9JEyX9fH6ShfubuPuDczfOJFk9jukVTZERIsVtkl9Ah2oyjfPxkgUHgaavMC8saXpDe_tm6EHBUur4S0uNAeI5Iw-xdtcg4H37J5D8sQvYEeXlIC32bV5chW6T7oWXrmoM0zV02gUNa6SFEf0NB43JT7d0NQKrm0h89iq0NypMt8S5_F3T7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe85afd9a.mp4?token=HGndCi50b3GJ2L6X2foolD6acR8v-xH9mgjn3faT56GA_edNFMUsgMRy-5K-Ze_HE2OT58jaf97qKhPtbJfAYg5zRF2DRNXAhutqWYn94qUs5eI-s6UzTF8HrrJGpEQfH484A1Abxiq7W5rPqVIEVA8lLCjSdC9bSQ9JEyX9fH6ShfubuPuDczfOJFk9jukVTZERIsVtkl9Ah2oyjfPxkgUHgaavMC8saXpDe_tm6EHBUur4S0uNAeI5Iw-xdtcg4H37J5D8sQvYEeXlIC32bV5chW6T7oWXrmoM0zV02gUNa6SFEf0NB43JT7d0NQKrm0h89iq0NypMt8S5_F3T7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  لحظة استهداف مخبئ للقوات الأمريكية في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87755" target="_blank">📅 03:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87752">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=m1krcd68IOsJJW9O--qk4_gnQxyGs_jMNu-Y2rQbQo_tW3IqJ2zR3WF0ftWRgkuRGrPGwjTC405UhRnTHC9q4mjMmpizgkoC9ZHMGFYPYlMNI3JQ3eZhbq848-GMHRFTPmLCTjTdAo_giOIOwskbRgWUuxxxlG5QoBmk6UB8NbOxUkNIpqRLUyprDH7Qj_WDhahl3gC6q5aervMASylIgz1hxpupMto4IVDYf8G9XbBjZpbKg03YqxmAOucQdpL0so7lKzNoD8xsgpGeLS9koeZzJmd5zvAHVbYArJycDQp0kUxQwZBK7ZD6SgRoOb1ulPV1I9KShRbv0qglCL4Owg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4fbc1059.mp4?token=m1krcd68IOsJJW9O--qk4_gnQxyGs_jMNu-Y2rQbQo_tW3IqJ2zR3WF0ftWRgkuRGrPGwjTC405UhRnTHC9q4mjMmpizgkoC9ZHMGFYPYlMNI3JQ3eZhbq848-GMHRFTPmLCTjTdAo_giOIOwskbRgWUuxxxlG5QoBmk6UB8NbOxUkNIpqRLUyprDH7Qj_WDhahl3gC6q5aervMASylIgz1hxpupMto4IVDYf8G9XbBjZpbKg03YqxmAOucQdpL0so7lKzNoD8xsgpGeLS9koeZzJmd5zvAHVbYArJycDQp0kUxQwZBK7ZD6SgRoOb1ulPV1I9KShRbv0qglCL4Owg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف فندق يتواجد بداخله عناصر من القوات الأمريكية في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87752" target="_blank">📅 03:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87751">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b228489921.mp4?token=NnUCFF-wfF7CAt8DY5usHDGaTizLxpyEdx3qL7YkwaGWMimodC8DScJroHcEIyv3RzV3KJWF4I02zS1ar9okcBdo29-ACGqTHJzMSxu1UuZlZcDTimkxrGKXCCFyaFqc2CvEl-qRNAG6J564rhga_knsHjyA_lv0_fTIaTv1Z8K2vkPCBMRZg3DeJkSspToh71U_KNwyBtzKSglSxrtDoHon-Rm4WZwe5A4nrqUfxh5WwBbPdFkHdJfVB3dN8xhRkdO7mQa_Gm806SwL4owj0ty17yIVJHZ8N6NsIHL7IW6rVJbt3ApebturQaH5WNyZ4FAADkuyS_zKtdJDCURPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b228489921.mp4?token=NnUCFF-wfF7CAt8DY5usHDGaTizLxpyEdx3qL7YkwaGWMimodC8DScJroHcEIyv3RzV3KJWF4I02zS1ar9okcBdo29-ACGqTHJzMSxu1UuZlZcDTimkxrGKXCCFyaFqc2CvEl-qRNAG6J564rhga_knsHjyA_lv0_fTIaTv1Z8K2vkPCBMRZg3DeJkSspToh71U_KNwyBtzKSglSxrtDoHon-Rm4WZwe5A4nrqUfxh5WwBbPdFkHdJfVB3dN8xhRkdO7mQa_Gm806SwL4owj0ty17yIVJHZ8N6NsIHL7IW6rVJbt3ApebturQaH5WNyZ4FAADkuyS_zKtdJDCURPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87751" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87750">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=XX_0z7TIhNCdseZVcUW-4rgIk5L08YAcRfqbBZOYZQNvtIPkRYFD1d8IBC96x1nGCDHcTcreuRUP0OC61JSrwn95FTZFchZ9q2WTY5CLHoLKlsE8syq5LQzOI_YiK_NdfBkqmMnLjLurJQGpvmDvxqHo191FMz92uAvQLbFvli9EzcHlOFV3fBmfbhNMkdLdriWZhdY3OcHrrrDCq2pfWpfBLRlgUysxHDOsRP4STf6Ux_iea_4qnYZdpHTsVtZS3-ZeFybggBLmUvzfF1IASn3kxGMMIvjT4ydnOtkKVqlUjyUcO8MDntaxXIl5cpl_ciMWrZ8oPq6RxJ9L1o5Ffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e85c067dbd.mp4?token=XX_0z7TIhNCdseZVcUW-4rgIk5L08YAcRfqbBZOYZQNvtIPkRYFD1d8IBC96x1nGCDHcTcreuRUP0OC61JSrwn95FTZFchZ9q2WTY5CLHoLKlsE8syq5LQzOI_YiK_NdfBkqmMnLjLurJQGpvmDvxqHo191FMz92uAvQLbFvli9EzcHlOFV3fBmfbhNMkdLdriWZhdY3OcHrrrDCq2pfWpfBLRlgUysxHDOsRP4STf6Ux_iea_4qnYZdpHTsVtZS3-ZeFybggBLmUvzfF1IASn3kxGMMIvjT4ydnOtkKVqlUjyUcO8MDntaxXIl5cpl_ciMWrZ8oPq6RxJ9L1o5Ffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف أمكان تواجد قوات أمريكية في أربيل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87750" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87749">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87749" target="_blank">📅 02:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87748">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87748" target="_blank">📅 02:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87747">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac3c86dbe.mp4?token=pky06GeKwXK_tM_1tTpAixB1IobXvKXjpzM5Lk5wLILfxqq9E68r7NcuvLfd4FLGmBo-XcsMmRZI98hwWdAHiiJUdOwHvBG97cD2VxOh0V5Isi4oKtfRmLWMCrDz6L1urx8Kgepd_frIFkx-IMEUWMsFnJ4Vp3kWScS8iE6Izdp1Cvx6PN-00at8KLfP3SlAyfVyrG2UawOz1s7nf-NvSwPVuTI0eDGSy22q_GrFhun_vcuCLgHMrKAvtcqnwS2Mro4pfy2_pO6_Lwc94dqP5bhgBBOHo7Tfc_k9sBCRVxXzq5qIZqDeAR2RWlOAdY7zncJejbWibkc3z_GGZSXKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac3c86dbe.mp4?token=pky06GeKwXK_tM_1tTpAixB1IobXvKXjpzM5Lk5wLILfxqq9E68r7NcuvLfd4FLGmBo-XcsMmRZI98hwWdAHiiJUdOwHvBG97cD2VxOh0V5Isi4oKtfRmLWMCrDz6L1urx8Kgepd_frIFkx-IMEUWMsFnJ4Vp3kWScS8iE6Izdp1Cvx6PN-00at8KLfP3SlAyfVyrG2UawOz1s7nf-NvSwPVuTI0eDGSy22q_GrFhun_vcuCLgHMrKAvtcqnwS2Mro4pfy2_pO6_Lwc94dqP5bhgBBOHo7Tfc_k9sBCRVxXzq5qIZqDeAR2RWlOAdY7zncJejbWibkc3z_GGZSXKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المسيرات الإنتحارية تشعل سماء أربيل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/87747" target="_blank">📅 02:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87746">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e026876dc.mp4?token=fP5QP2PX9-50z5Uvu3xdAMdAg6NLNom-BIjcXI1GcOFaPOZS2CwcNb4pnX4FEevU2fW6hYmTg4dngPgoaYtqjF5gdaW1TH0ovjI4luT8y48awYY4EmM-RuhzrkmIJxY1ihLt9_JzwGqne4ye6ZFwbk5Z46WoAnUvJG2kLzmjgHrBD0XzHPVy-M4REg1SJX-vFtjf2aXU2nxNCiutoFLVUXcptkAL1LagPlvhFoWLv19nE0MiEYT75E9PZ0yc1v6hZVPj4c40jKNgQvFU9GuS082SeOGmvDnijgrG-Q-6WoLOCcF3782xAjZr06ERpgDuiVZ6cTFr_4Cs7MZPa7ggnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e026876dc.mp4?token=fP5QP2PX9-50z5Uvu3xdAMdAg6NLNom-BIjcXI1GcOFaPOZS2CwcNb4pnX4FEevU2fW6hYmTg4dngPgoaYtqjF5gdaW1TH0ovjI4luT8y48awYY4EmM-RuhzrkmIJxY1ihLt9_JzwGqne4ye6ZFwbk5Z46WoAnUvJG2kLzmjgHrBD0XzHPVy-M4REg1SJX-vFtjf2aXU2nxNCiutoFLVUXcptkAL1LagPlvhFoWLv19nE0MiEYT75E9PZ0yc1v6hZVPj4c40jKNgQvFU9GuS082SeOGmvDnijgrG-Q-6WoLOCcF3782xAjZr06ERpgDuiVZ6cTFr_4Cs7MZPa7ggnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم عنيف بالطائرات المسيرة الإنتحارية يستهدف مواقع الانفصاليين في أربيل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87746" target="_blank">📅 02:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87745">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53b0dfcfc.mp4?token=Jo48jB8JbkJ6b1NJKhba5V-ZuQC_76dVR2PQtey9xRLjb8AQCqhoeXXX_T7HYD7vMqAzcMOfOZ3kFYRibcVCXcPl_XRU19bnNcWTmVbuTz3xSLqP9ET9wB_siX1u3OgZj0dgijrOIOdNEDJp9L8fDaMbE4OwZngKd5UU-lCc3uUVoNhzy8ONTPeacvFGphQyUMs0fDa2n4_6_wyYW_rVW_jdGqeDGDmAVXSVGwrYlomfzwrlB79DPMnZs_AC3LM6KaScPF6bBEOzEvLqLF23CcE8ZjSjJ3gJYpwUAmGAe7WDJ12shBx5JFiS1vAsaFb8eO1yDPFOjui08_FvVfs1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53b0dfcfc.mp4?token=Jo48jB8JbkJ6b1NJKhba5V-ZuQC_76dVR2PQtey9xRLjb8AQCqhoeXXX_T7HYD7vMqAzcMOfOZ3kFYRibcVCXcPl_XRU19bnNcWTmVbuTz3xSLqP9ET9wB_siX1u3OgZj0dgijrOIOdNEDJp9L8fDaMbE4OwZngKd5UU-lCc3uUVoNhzy8ONTPeacvFGphQyUMs0fDa2n4_6_wyYW_rVW_jdGqeDGDmAVXSVGwrYlomfzwrlB79DPMnZs_AC3LM6KaScPF6bBEOzEvLqLF23CcE8ZjSjJ3gJYpwUAmGAe7WDJ12shBx5JFiS1vAsaFb8eO1yDPFOjui08_FvVfs1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تستمر الانفجارات في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87745" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557c261eaa.mp4?token=fo8En8Fa7tTu3AHOPDs5rOGrcgt2I2SWHkWWNBcttGrJtNtUclC1JXGyAFTrWkynZIzdkb_bTh2weaNqcCY4Z2l7Erx2zpjPmMBqOolNPgXaSm70sIk4t20ZQujkm3H8DsnGm5xM2dgJ54Fd0g9Wmf130EQZZfuomc4KpEgU2gsh0RhEDs_HZK7E-LyLhQHQLTUXQGbtaNDeyVTllWQe9f9J2E8aJAPMJ9UfgEv_3OV_5mwOaJ9Y3oPpyTmNbv-TURAXmYBiVzI0VGlrr1HdEML3DYsCmy8PFJtN680ulh-UODz20dvV65AM8605PCrJFSNRHDd_oiLVuEpMiKS-ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557c261eaa.mp4?token=fo8En8Fa7tTu3AHOPDs5rOGrcgt2I2SWHkWWNBcttGrJtNtUclC1JXGyAFTrWkynZIzdkb_bTh2weaNqcCY4Z2l7Erx2zpjPmMBqOolNPgXaSm70sIk4t20ZQujkm3H8DsnGm5xM2dgJ54Fd0g9Wmf130EQZZfuomc4KpEgU2gsh0RhEDs_HZK7E-LyLhQHQLTUXQGbtaNDeyVTllWQe9f9J2E8aJAPMJ9UfgEv_3OV_5mwOaJ9Y3oPpyTmNbv-TURAXmYBiVzI0VGlrr1HdEML3DYsCmy8PFJtN680ulh-UODz20dvV65AM8605PCrJFSNRHDd_oiLVuEpMiKS-ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار طائرات مسيرة في التوجه نحو مقرات</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87744" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f1e06b63.mp4?token=kmZgjlpyssI_w4a8sPJkFPvneCTHe84UafbU_dlvpm6xwAELmL5u7Gjkoarltev20das5PtAQlTGCVO4AeQKo8E-dgJjahlnCDbd03rG5SR1gxBFT-yOoce_DfjYECDRdADJ3zZ4STkHLwOjzoA6kZs3rgQvDNxTV5pDxwJqY1cIkOvdrfgMzcrCDpvlFkJaZ3Cq6hY7iD_ufs2k3DcWXA6P5n3w1UvjPJgyYbKPnI9Yv510KuwrSFDQd-2TfXOZmul7hDiJWKbloab7yXhV6GH5C4SkhwCoXOU4KvRYArc6rqBl008TVTdl7gLGwaOAO8I9KxYVM0dxszINpeL7CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f1e06b63.mp4?token=kmZgjlpyssI_w4a8sPJkFPvneCTHe84UafbU_dlvpm6xwAELmL5u7Gjkoarltev20das5PtAQlTGCVO4AeQKo8E-dgJjahlnCDbd03rG5SR1gxBFT-yOoce_DfjYECDRdADJ3zZ4STkHLwOjzoA6kZs3rgQvDNxTV5pDxwJqY1cIkOvdrfgMzcrCDpvlFkJaZ3Cq6hY7iD_ufs2k3DcWXA6P5n3w1UvjPJgyYbKPnI9Yv510KuwrSFDQd-2TfXOZmul7hDiJWKbloab7yXhV6GH5C4SkhwCoXOU4KvRYArc6rqBl008TVTdl7gLGwaOAO8I9KxYVM0dxszINpeL7CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تستمر الانفجارات في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/87743" target="_blank">📅 02:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87742">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">استمرار طائرات مسيرة في التوجه نحو مقرات</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87742" target="_blank">📅 02:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87741">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee52060d77.mp4?token=B0QTWj7qBljvQlEp1PCyKM8ak0scFR6_KJ2PwBuRes4huQaiiNAvgMPwEbRM1sg6SnPb-EIsXPtNMmrpG1p5b0120E_K-wRgtFRZ-zv9Q_pnLyDsQbnKOkT1baa3XtSnxQuyOhkB18ZTX2Oqdbv3lLqkqvZ1W3LboHMN-X51hTLGEnHctoGhVJiFo8ST8qG-pkorH4ewsUEzecpA8TEyMzxGHRynG4wCrrKzGJnKA21KhLIk6Ln2nyBAo6FwIbx302mhPE0Q0HrvwaDxrq7IywDE4KlUPrBYDaahwCskIFAtxaYxSLgdD60ibsvP7FNcxuisYUfsmoND6S_1c598FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee52060d77.mp4?token=B0QTWj7qBljvQlEp1PCyKM8ak0scFR6_KJ2PwBuRes4huQaiiNAvgMPwEbRM1sg6SnPb-EIsXPtNMmrpG1p5b0120E_K-wRgtFRZ-zv9Q_pnLyDsQbnKOkT1baa3XtSnxQuyOhkB18ZTX2Oqdbv3lLqkqvZ1W3LboHMN-X51hTLGEnHctoGhVJiFo8ST8qG-pkorH4ewsUEzecpA8TEyMzxGHRynG4wCrrKzGJnKA21KhLIk6Ln2nyBAo6FwIbx302mhPE0Q0HrvwaDxrq7IywDE4KlUPrBYDaahwCskIFAtxaYxSLgdD60ibsvP7FNcxuisYUfsmoND6S_1c598FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متتالية في محافظة اربيل</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87741" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87740">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3518d796.mp4?token=Ttz1-eZLCr4hPuzGe38DoUvP2HAra5KI2XOq62fJ38RqjpWcuKQBOm3a07ZXNUFZZ9ca3s9iAed2haPteshJLZRB20_7W5PWkC_dp5cgeAdRY1qrU_ivxK9cxGocynHZ_BTsfuWp7arIY-6Wm7Wn2aVidRyIm1YwpsYs5wRmmNC5Bcfo31bXpvuOF38rkePl6-QNtTOzyl6sUAAtOoUadvEdNpGDsnxyb61HGGJMFUV5g6e_3XyABoJukVSg0Pu2cEkJMNIrRCO7i7Xdt54bAJhs2Ahj7hs8x5ldUmAJZygWw-FuPbArY9MTphMdXIx8wiukQYl4uSm12GCjSKDwmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3518d796.mp4?token=Ttz1-eZLCr4hPuzGe38DoUvP2HAra5KI2XOq62fJ38RqjpWcuKQBOm3a07ZXNUFZZ9ca3s9iAed2haPteshJLZRB20_7W5PWkC_dp5cgeAdRY1qrU_ivxK9cxGocynHZ_BTsfuWp7arIY-6Wm7Wn2aVidRyIm1YwpsYs5wRmmNC5Bcfo31bXpvuOF38rkePl6-QNtTOzyl6sUAAtOoUadvEdNpGDsnxyb61HGGJMFUV5g6e_3XyABoJukVSg0Pu2cEkJMNIrRCO7i7Xdt54bAJhs2Ahj7hs8x5ldUmAJZygWw-FuPbArY9MTphMdXIx8wiukQYl4uSm12GCjSKDwmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/87740" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87739">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">إنفجارات في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87739" target="_blank">📅 02:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87738">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
دعوة جماهيرية في محافظة بابل  ردًّا على محاولات إثارة الفتنة والتحريض الطائفي، ودفاعًا عن أمن المحافظة واستقرارها، تُنظَّم دعوة جماهيرية شعبية في محافظة بابل للتأكيد على رفض عودة الإرهاب والعنف، والحفاظ على الهدوء والأمن الذي شهدته المحافظة خلال الفترة…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87738" target="_blank">📅 02:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">زلزال في جمجمال وكركوك شمالي العراق</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87737" target="_blank">📅 02:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87736">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
دعوة جماهيرية في محافظة بابل
ردًّا على محاولات إثارة الفتنة والتحريض الطائفي، ودفاعًا عن أمن المحافظة واستقرارها، تُنظَّم دعوة جماهيرية شعبية في محافظة بابل للتأكيد على رفض عودة الإرهاب والعنف، والحفاظ على الهدوء والأمن الذي شهدته المحافظة خلال الفترة الماضية.
وتأتي هذه الدعوة في محافظة بابل التي عانت من أعنف المعارك ضد تنظيم داعش الإرهابي خلال عام 2014، وما خلّفته تلك المرحلة من مآسٍ وتضحيات كبيرة.
📍
المكان: بابل – المسيب، قرب سيطرة التحرير
🕒
الزمان: الساعة الثالثة ظهرًا
يدًا بيد من أجل أمن بابل واستقرارها، ورفضًا لكل خطاب يدعو إلى الفتنة والعنف والطائفية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87736" target="_blank">📅 01:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87734">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVyGmeiBPKkwEcyvfvBtm8mc75DwOKqmtHFs35pxruIwyJ0Arfhliubb3UoX5yWi4RcYH-Y8J5KC7Izkyr-H3_3b5QjunQUYEp4ckNRV7k_UQwwRQFD5wgo7adlTrbXFfRzFrp32IDrM8vwZ5A-Q6rFysqUOnih7dS3zO2dA9Fx4HVIrW1vyNiJ3l-V15cRgYm2pPgte4SD1inHw_vGR-jk39cs1xIHiz9u7rS2roTjoAA-dMQt1_t6O6pYJ9zjamkosLOZjaVmwSN-QXWO0PC28RvwUZwRTIjK54Mke3N_6PpzkBhF5cXEgs5_gH_vr59VwNigCkB8xOmsWztcr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsw5Wm4okqlPv00Q83PFk8AuFM12zVA6HTS0o2SEIzbIodotyVMTiX-haM27ycFTBSHkdeejcTzY62bL0ePHq_yCUAhOc7kk-S-I9y2SObKoHAASZMuNqnr2pBJd6Wo_zgPHluBlWw9Dmp-PLBc-Tz1g4ZoIEaJEcTq7bJ8YmUpUrF4Y6Ya62NcVkP9Targ23VFX_u3vWAi05D0mH633jplfh7MzloWL_GohT-BneRa0ezOshocT8n0NxR2rnhGkjD2H5-ir-O_zLPOhaIIWOqtnTnMjdWPgril-GNfbTIJqO_K71OmEI-0L35xcxE72J_zczo3cWDK7FE3HtAbTRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
إشادات شعبية في الأوساط الحشدية بمواقف مدير المكتب السياسي لمنظمة بدر، ودفاعه عن سلاح فصائل المقاومة العراقية.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87734" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
‏
وزارة الحرب الأميركية:
نراجع حاليا استراتيجيتنا النووية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87733" target="_blank">📅 01:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87732">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEnAD-yy15lobdckLK5LZtzSb6xX6xtPZ2xVkDLLepvLWXL2ipkH4YUywCJu1MDTEnEh8gzvL8UD4__8dUrnxHoc1wlixkXXDdTxKrri4mOk57AM_8_P0sKh4jYvB8_YUTjIfxoZICYm-KQ-Jeqz7egKAih1586DNzfgsT4P_cp_e9-KM-kXfjxZgb6y-dvnLpzu5lf6IDv9WbA5NMmGR-gUv9RVf40lyOPGRiELVXT1y12_8XILhlQEKumb28Jjbe1Z2sq9Z3I5zHiVOGi7-6WmX7uPYgHGO2_Q9LExjB0U7r6qqIJYFVSDt1JYtlhsaQYzFDD8CbQEU4EY5WxvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الأوساط الثقافية والسياسية والإعلامية العراقية ترحّب بتكليف الدكتور عباس العنبوري وكيلاً لوزارة الخارجية ..</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87732" target="_blank">📅 00:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87731">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شركة أدنوك الإماراتية:
تعرض سفينتين تابعتين لنا لهجوم أثناء عبورهما مضيق هرمز دون إصابات.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87731" target="_blank">📅 00:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87730">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
‏
نائب الرئيس الأمريكي فانس بشأن إيران:
هذا الأمر ينتهي بنا في موقف قوي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87730" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87729">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هجوم سيبراني استهدف منصة دائرة الضرائب الفرنسية</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87729" target="_blank">📅 23:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87728">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGu7FgDJ3MowM1Ryx-9cf7GHSRI7IVkr0W1Llwf9-tQa3Xh7JvVSp3J7m-Sm5xOt2rpZ7TdNCA1pcq6wb-4na7qonrRqrVIjj6MrNby6c6ZorOxov967DmWT0kCBxfe230nFwh2avSZuxFN0YdbuI0kLI2wFU64bcKw5cF4RixTSdIMASAfzg1_O2YCGK9ZzphTAEdl9GJWV3GAFIItrwSy8xc0LLOjOoowfd2aoi6tWlj92sFMmDnqs_pTM2dyS2-IVop3qyGuIM1WeyuAcAYC0GywHWgyB9l_-2Ba6LXXJHq9CarxB0YyCioeJ5vKdD3x60ELNGyRVIAZcsizHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
جرف النصر .. كعبة المنجز الأمني العراقي الحشداوي
دول إقليمية تريد عودة مثلث الموت ؛ دار استراحة المقاتلين العرب ؛ مضافات ما يسمى ولاية جنوب بغداد الارهابية ..</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87728" target="_blank">📅 23:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87727">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هجوم سيبراني استهدف منصة دائرة الضرائب الفرنسية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87727" target="_blank">📅 23:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87726">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
طيران حربي مجهول يحلق في سماء محافظات العراقية.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87726" target="_blank">📅 22:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87725">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e936a851a.mp4?token=TlKpchmVs8Yav8D9Gc6lr2619uVhyV4lvk510zM0JUGRzKVboMGBP1PKQDBeg5OV6OWhVbe0r1EGGp2bWf8M698XZu5hZVIbu_DvwYVUe3NHlBOaS614kVvCZY_yjT5egB6vjA9SE5NDcCurCpNEpGgA8_bFFH_ZyouJJrawdAUYrOyRy8u-F7SmibJbqzX8bd9Sc-DyVT_K0pBYTzs9qI0ZWCU_j1kFsoUdGjfCCi0HKhIf3TpV6FplUWo01P64EOrW8-Cc7FYOfsn4yZqdYjTxZS-BwbMbqxSVzjcPt77LV6TDkS2NB_4cLz0Gp3T5fFKYydxW_IMa4kYoixq9bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e936a851a.mp4?token=TlKpchmVs8Yav8D9Gc6lr2619uVhyV4lvk510zM0JUGRzKVboMGBP1PKQDBeg5OV6OWhVbe0r1EGGp2bWf8M698XZu5hZVIbu_DvwYVUe3NHlBOaS614kVvCZY_yjT5egB6vjA9SE5NDcCurCpNEpGgA8_bFFH_ZyouJJrawdAUYrOyRy8u-F7SmibJbqzX8bd9Sc-DyVT_K0pBYTzs9qI0ZWCU_j1kFsoUdGjfCCi0HKhIf3TpV6FplUWo01P64EOrW8-Cc7FYOfsn4yZqdYjTxZS-BwbMbqxSVzjcPt77LV6TDkS2NB_4cLz0Gp3T5fFKYydxW_IMa4kYoixq9bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد لصواريخ الباليستية التي تم اطلاقها من قبل انصار الله نحو الاهداف الحيوية في مناطق تمركز عصابات السعودية في اليمن.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87725" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87724">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKeNOeADKKo5jQdFNX706QLv9VaLEveIJb2IftX51dy9WusCt96tYfyG_PolXgc-0pHcO6L7xNwkM5c2Ce4Jrq1qPpyQGOIFFvpZMrPCA67cY6Ch8N5h8UsL6si_SlTUPzzGuPuyCytimm7xGrWQTxrxZjwGgub4-d___cZ48EboXR9sruM-nD0qBLvboheq-TirEHztjAKOyc1FLul5FtEYBPS253GvMzpk4azFUGrcR23n3BTP1TBQKpsXZnVVrKw7CXNFR86CxmA7T21tc3v3ZS4djWXk1_UhOd1gKNRSLNQUWhAeb4l9d9k-P7_BIHE8GWetXDQvO0dntUjqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/87724" target="_blank">📅 21:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87723">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irPdrK1K-CQ3BcJhdiHTEf4MncWxnzHUExFZhxnlxEJQ2uoLjggro6OD8JbTujnaHqMgjBRbw3YFZFLBjA9dyks9biF5t9fQsNj39eX5-CRhtOSTcINJLqFJBjT_AjTBl69wbDOJ4GAV6XsNyaRJu_trJaWPohhtuHE89mdwfy8QmtsgiVo9g4PqWJr6LmlwUFdVvml9Y-cbidtBezU1NczX9dtLxu8ZJV80usfNuIZ3MB1VMs4HSm1n3tKLhlyMu9HYWRFi5z9kCr5zY8Cq5AxnAFEKfLYdjfB9NkrNk7koIqVCLANJy7Hd3Q8XLpKrY3E-oZiyaX9mZQ26PnPWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تخوف جماهيري من عودة مضافات ولاية جنوب بغداد
حملة إعلامية مدعومة من دول إقليمية دعمت ظهور داعش إبان أعوام ٢٠١٤ تطالب بعود تسليم جرف النصر شمال بابل بيد الدواعش .</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87723" target="_blank">📅 21:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87722">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfLlkJCIuc_o2_htkCA0KEGrvNpeSZq68AYM_5vecyM5MXBvSVT-ZboTeUSfnSlXejk0Tc06AtIKCI_5djOAmiUoFVJ7HPa3lbTRtc_CSHT8RLxunVUrKtYkfHiUjOSq7Vs_NSoezyOpcTcNMnfYkQLlNz2wNybCJCpGGNuPad3Gmo4NatpMuw6G1kspmWLGA3khJElFV4DEEiDc667zyqUZAGBz2VXjS87VqkD5R6ZtdwOWrykH8_4le9p-RBBrTKf3fIjX2mN0SgsDXyLS3ipGhu_Wk8WGZb4xu2fZwg2Nbu8i3_1iVZik3dlFy7UiZsZMrt-pj_WoIso6x7WBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87722" target="_blank">📅 21:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87721">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇾🇪
انصار الله يستهدفون منشأة حيوية بالحريقية قرب باب المندب بصاروخين باليستيين.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87721" target="_blank">📅 21:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87720">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇱
‏
الاعلام العبري:
قائد سنتكوم أبلغ إسرائيل أن واشنطن قد تضطر لاستئناف الحرب "إذا لم يكن لديها خيار.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87720" target="_blank">📅 21:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87719">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=UYum9FoYg9MGMA6eBhHTnsStMRPRw3MA7KAk_DCdaUBv0c_1g1pLvf1RZfYUefpObR9MpNUz7naWIukpM6fxXWxLj5wICr5NZd8Oec_r_B7kXCbnmjMIUpeIv1-NRJAoQhpEXBkb-AR2bjRVs5E_tO5OQZO3PinpHRsIIG5Ki_6QlnHn9IlyIbMJxyyTQXayQQlabL9AULIBQZEQ7iRpXYMhhc1FHKId5d-jHwpa5S28gF1yl16RDj8SlrtE8_Xkj7St3EJhxFPl7QFapTyWrnzdQuLR1Qj66xttqKbJkV2VGu11fVaoCUGGjmyShxpUZcIXVwMKfy29nQLn5yRVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee43d192c.mp4?token=UYum9FoYg9MGMA6eBhHTnsStMRPRw3MA7KAk_DCdaUBv0c_1g1pLvf1RZfYUefpObR9MpNUz7naWIukpM6fxXWxLj5wICr5NZd8Oec_r_B7kXCbnmjMIUpeIv1-NRJAoQhpEXBkb-AR2bjRVs5E_tO5OQZO3PinpHRsIIG5Ki_6QlnHn9IlyIbMJxyyTQXayQQlabL9AULIBQZEQ7iRpXYMhhc1FHKId5d-jHwpa5S28gF1yl16RDj8SlrtE8_Xkj7St3EJhxFPl7QFapTyWrnzdQuLR1Qj66xttqKbJkV2VGu11fVaoCUGGjmyShxpUZcIXVwMKfy29nQLn5yRVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
السلاح الذي حرر امرلي والجرف وسامراء و بلد وصلاح الدين والأنبار حينما هرب الآخرين هو الحصن المنيع للشعب العراقي بوجه اي مخطط خارجي يستهدف الأمة العراقية ..</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87719" target="_blank">📅 20:43 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
