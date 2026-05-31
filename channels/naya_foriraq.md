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
<img src="https://cdn4.telesco.pe/file/YEs0ppM50J4b-QbKBobXa3t7WPx4BRZGTQIi4R9-t45ruDo4vijUBg3jUa-dq1KqzhIRfO6j1-PXbYacFdYC2XDOwCeIWJOmONXbo49Wh9UZ2wKZxJOvqAAGReY2ZGOpb6LImaZPD8sZ3tA5X8INrjyc8_010HjcOFh4wFmZFg6CmbU2-J2OgBbT1SSKqVQVhthtT3bmK3Q6t9r9l4lP3KWui6j3gPmco_rmTIYXLoy9aIktsQBDdo4uJH8JCGWOX31N2mgxr-iJJxdQJ4QqjrGfFwcrVwL8l0RwkPsbYihi1d6jMTL6bSAC5RZkOPnDxEnwSJsUhOxqBWkcAhkbGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 251K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 06:09:09</div>
<hr>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/laIUmw_aysHSzrQokjbnDWtqCLNqRWtBgqULYMtIGfZ4l_9R7H7tKda1oQu__cH6I0MJ4s8_ZBdD0Jol0u_kaUfuin9-e_G5R7pKNINeCmpSaQ1W0ztHT1QUM8_XGwyd1GVufgVxlYkHKfXeBd1vc9FHEiuOyMN6po9fzGfzoFJ5b0-nePnCZ5NIuhl_PFcUELS14zGdHSZVxHqp-t_idu0i1B8Kf7yY3t-FUJOCP96VCoSnYYJRmAoPjBHqIrB25QrD4Xhc17rOqI4KwmjYqx863vEHpYRDmUsDDNe5nJvQlniZQP6m6LM7lKUAe1_tHlfn7PFZaxb_g1hrprUCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSXdRW6U7cSAYTq9tR_z9lalj3v-vWxPnnTaH_Kfc8CUCPfAwVIM1UawXMTTvtPKkx_TYDqcLNwPLpexc4rI0A5OYamFTXKyGlwMvuFIFxxAadPuu2ld41lLF_t_cZqnUgEU2jcj8Jr3bJPXnfLdEKZcXMEDHb4oq990Ef1gyCslG-4Wrg702vcG4kcdS7GA6s0q5swt0m60jugcy4_ye3o7Pv79l9YM0UT5pUFcVo2XbHLewIIyDbqL2UagyDUymTPUEQVj1j9ZZEooq5Zbj3iZi3GUCif79f9UhSRr264PSqi1Xo78sFGkinOlgvNoCAvmVm0K5ZNMdibHL83qdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
🇮🇷
تعرضت طائرة التزود بالوقود KC-135 التابعة لسلاح الجو الأمريكي (الجناح الجوي لجيش ألاسكا) لأضرار من شظايا بسبب ضربة إيرانية في المملكة العربية السعودية.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/76480" target="_blank">📅 01:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
🌟
إصابة ضابطين إسرائيليين بجروح خطيرة إثر استهداف منزل في جنوب لبنان كان يتواجد فيه قائد فرقة بالجيش الإسرائيلي، في هجوم نفذه حزب الله.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76479" target="_blank">📅 00:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjPjFJsb2SNWogZ4hFDwvSZZT-r4kbdY0Qu05dk52SF-4Rc4cjUoLsQw6ZP1dBFdwCMMIr8wY2ht292A4RNa9IG0c9i8l4n95YUCEslZEJGj6L7RJgi1YI3l81jXT4BiyIFUhT-h8447yQ4AtPuLwTxrB0TGVcCsI1f9drzFGjdwexwe3UfIM_4w_XcuoO2FtgKtbSbswchB5MP7QVI1nnT0mxpWfhBJ8gxr-a9BAIrq-I1IBb6TKVzGSUcZQGqfBu7dsCwstFmMV6Yl5k2eY9wyeD7irL9ez7DHz0gFSMNelwzvvXP2NZIHfDZ7cb9g3yI8-r00JKclMvObsTG1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب:يجب أن يشرح أحدهم للبابا أن عمدة مدينة شيكاغو عديم الفائدة، وأن إيران لا يمكنها أن تمتلك سلاحًا نوويًا!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76478" target="_blank">📅 00:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
🌟
إصابة ضابطين إسرائيليين بجروح خطيرة إثر استهداف منزل في جنوب لبنان كان يتواجد فيه قائد فرقة بالجيش الإسرائيلي، في هجوم نفذه حزب الله.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76477" target="_blank">📅 00:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">أصابت طائرة مسيرة مبنى توربينات في محطة زابوريزهيا للطاقة النووية، محدثةً ثقباً في جداره. وقد طلبت الوكالة الدولية للطاقة الذرية الوصول إلى المبنى لمعاينة الأضرار.
‏رئيس الوكالة الدولية للطاقة الذرية رافائيل جروسي: الهجمات على المواقع النووية "تشبه اللعب بالنار".</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76476" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LufQKhMusjj0kVvV89ngcErO9L02Nl1CTJGU3bGRMtnzJdSxjHkrPGJwlBuoxzc-q5RUsvOUO4jvuRUMZ2Y2sQRM4I2czOoapo0oBwA0JofC6ECNL-0bv1fAReIvvyuFuyFmedHst92UzHZyjwoFRspuAfvEMEsqKBYONzCzQ0MoLBy9QY-jhAxZB_Ql1X1sXHTGNbhF8RZFLhCIVU9l-NzlWF-2b18KkFDMGTBNH0nV8rQy-2gSd_J4eknk80esKlqE8GULhsmg5PFFVmFJ46AOI_M9phTRyHQok0t1IBl14cj2k9e5-0_g_XJCzGI9QADUYypGwC_vgbNq0ZRh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:يجب أن يشرح أحدهم للبابا أن عمدة مدينة شيكاغو عديم الفائدة، وأن إيران لا يمكنها أن تمتلك سلاحًا نوويًا!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76475" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYDDcQTgNxMJ31OOO6LCVeL4btzYxh2KCBt6HDBZxSbV6E2YUovUpZdZhW75oGcd5BW2h_WkHFjHXs_7j2R99KDrEcQDGcOugdyDAy23yAYoqmH_3oHhlYrbVeM-51DNdyY6L2C4TDervh-J-a29GS1BRZCDhBIXWcgTbWvh0ElCYg7xqCgm6v1FBWPFb7DwaQHOhu7PH-yPlBpZXIaPx0HCGP5PHTS_DXh4Exo7EZXzJds1b9RRs0Nshwg09iu7jXk2tEVdT2b9X4crr6KqgnufOjJcQHaurYKa_YTr_1rLo_omXydVLPHT9xQ5IQ4FYITXaPc6SqXt5a6Ff313aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
شيخ عام عشيرة البو مرعي في محافظة الأنبار غربي العراق و رئيس لجنة الإعمار في مجلس محافظة الأنبار سابقا يشيد بمبادرة الزيدي لمحاربة الفساد ويعلن طوعيا لرئيس الوزراء للتعاون مع المجلس السياسي للنزاهة والرقابة لاسترداد المال العام خصوصا للخروقات التي حدثت بمحافظة الأنبار</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76474" target="_blank">📅 23:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
🌟
إصابة أربعة منتسبين من قوات الحشد الشعبي إثر انقلاب عجلة عسكرية في بادية السلمان بمحافظة المثنى جنوبي العراق.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76473" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🏴‍☠️
مشاهد تظهر تساقط الصواريخ التي اطلقها حزب الله على شواطئ نهاريا وهروب الصهاينة نحو الملاجئ.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76472" target="_blank">📅 23:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
رغم معاناة المواطنين في إقليم كردستان من نقص الخدمات وتردي الأوضاع المعيشية، أرسلت مؤسسة البارزاني الخيرية أكثر من 1000 شاحنة مساعدات إنسانية إلى محافظة دير الزور السورية، في خطوة وُصفت بأنها تأتي لكسب ودّ الجولاني، عقب ارتفاع منسوب مياه نهر الفرات نتيجة فتح تركيا سدودها.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76471" target="_blank">📅 22:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🙂
السؤال هو: من اين جاء الحلبوسي بـ500 الف دولار ليقدمها كهدية وما هي ثروته الكاملة اذن وما هو منصبه في الدولة ليكون هذه الثروة الطائلة وحتى لو كان لديه منصب هل راتبه يكفي لمنح فقط هدية بنصف مليون دولار وهل مهنة التجارة في الدهن الحر تجارة رابحة الى هذه الدرجة؟!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76470" target="_blank">📅 22:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
‏عقب الهجمات الصاروخية لحزب الله..  جيش الإحتلال الإسرائيلي يعلن عن تحديث سياسة الدفاع لقيادة الجبهة الداخلية ابتداءً من اليوم.  ‏وقف أنشطة التعليم في مناطق خط المواجهة على حدود لبنان.  ‏إغلاق الشواطئ أمام العامة في مناطق خط المواجهة على حدود لبنان.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76469" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76468">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475b6b42c5.mp4?token=Vn-_EXtP0JuNj27LuIt-zZCKzVGAj-BFjLUfyeFG10WYMPrhWMQcWB94Vs8y2ozTpiHZwYQujWRvIZ2aWXxl-xnBwPTwMcOuZ1JAYfl-8iAURLa13fCLxY6pjQMFqfOHxB3jixHUKu6CDLtu5dct_ufHNLMd1o7TpxU4XNcVDFl1td23xNuhUsWu_MIJI-zrM-O1l9n0uwi7ziNQThanGeSWkpqfLaQvCTtl01pwQrAB0m9WgkWkO4uffWFIVG5FSxRczEPjotV7jW-sPCkug-sK7sgOBwn1q6hAKzSQuu4U8a6uScJ5wHzaHnd6dDPSZB0EJC6Rwmwn9mbeJR3HMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475b6b42c5.mp4?token=Vn-_EXtP0JuNj27LuIt-zZCKzVGAj-BFjLUfyeFG10WYMPrhWMQcWB94Vs8y2ozTpiHZwYQujWRvIZ2aWXxl-xnBwPTwMcOuZ1JAYfl-8iAURLa13fCLxY6pjQMFqfOHxB3jixHUKu6CDLtu5dct_ufHNLMd1o7TpxU4XNcVDFl1td23xNuhUsWu_MIJI-zrM-O1l9n0uwi7ziNQThanGeSWkpqfLaQvCTtl01pwQrAB0m9WgkWkO4uffWFIVG5FSxRczEPjotV7jW-sPCkug-sK7sgOBwn1q6hAKzSQuu4U8a6uScJ5wHzaHnd6dDPSZB0EJC6Rwmwn9mbeJR3HMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سماع دوي انفجار كبير في جميع أنحاء بوسطن الأمريكية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76468" target="_blank">📅 22:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76467">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏴‍☠️
‏
عقب الهجمات الصاروخية لحزب الله..
جيش الإحتلال الإسرائيلي يعلن عن تحديث سياسة الدفاع لقيادة الجبهة الداخلية ابتداءً من اليوم.
‏وقف أنشطة التعليم في مناطق خط المواجهة على حدود لبنان.
‏إغلاق الشواطئ أمام العامة في مناطق خط المواجهة على حدود لبنان.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76467" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76466">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
سماع دوي انفجار كبير في جميع أنحاء بوسطن الأمريكية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76466" target="_blank">📅 22:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95bbb8a10a.mp4?token=vGU5V06wnnN3jKpAVC_Fg7mt89UN1pk2Xll_pyz7qdCM3fRKhlZmyp0UtSPX8RMy1iWIpCjXYYlVYCE6qDsz1I5gS1b-qYQi2l86jmBrWZqGzfM-c2GmG5o_7G6Yn5Prd2KeyvN1AMgVAFgQ2owQmcB2HZl00FR26FP2EZrb0T3zDHTKyye04N_ewX1fJB03T02iygzF2LT86mUIne7sgLLGzTTV2UxYlwzEK9rNHatKArbIL2EmC3rzBe0mYt3dcG4lX7w0frkJ5U-WT5O5bVXGdra3Piuofkm5bHJfszgT0Ia9jQlCb6uvUNAEF_6GzTXdWYsgCTb4w6knduUS9komnnBoiGwQAiC4pO9bsRdunOM0QxzkpwsyYIERVX57o4opXaxkVwB5bCENEIzNk-9ihxPjDhq7QMYbB1ahl4EeZVYOPIUYk1PD70K27gUvzqq_YkeS8RYZYom0Q5nxVO2iw2624G3i1qwpCIoY6cxozzPvRIymmNPjcoGXqgaxYWxk2JyNTq-8TUaQco9QnjL1jIyrlr-LBMBOLmlm5t4oVgdKtih7sJ9KZEde2Ve_UXrpY_KRqp1zR8AX-sR67K70qbCuKR6UkWDXaOQxMEj52ODKnnULzed1nJtBxZQttgBPCTJtT4kBiSC7CuU0GyjwbbnlsFceCOAFiOQeXBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95bbb8a10a.mp4?token=vGU5V06wnnN3jKpAVC_Fg7mt89UN1pk2Xll_pyz7qdCM3fRKhlZmyp0UtSPX8RMy1iWIpCjXYYlVYCE6qDsz1I5gS1b-qYQi2l86jmBrWZqGzfM-c2GmG5o_7G6Yn5Prd2KeyvN1AMgVAFgQ2owQmcB2HZl00FR26FP2EZrb0T3zDHTKyye04N_ewX1fJB03T02iygzF2LT86mUIne7sgLLGzTTV2UxYlwzEK9rNHatKArbIL2EmC3rzBe0mYt3dcG4lX7w0frkJ5U-WT5O5bVXGdra3Piuofkm5bHJfszgT0Ia9jQlCb6uvUNAEF_6GzTXdWYsgCTb4w6knduUS9komnnBoiGwQAiC4pO9bsRdunOM0QxzkpwsyYIERVX57o4opXaxkVwB5bCENEIzNk-9ihxPjDhq7QMYbB1ahl4EeZVYOPIUYk1PD70K27gUvzqq_YkeS8RYZYom0Q5nxVO2iw2624G3i1qwpCIoY6cxozzPvRIymmNPjcoGXqgaxYWxk2JyNTq-8TUaQco9QnjL1jIyrlr-LBMBOLmlm5t4oVgdKtih7sJ9KZEde2Ve_UXrpY_KRqp1zR8AX-sR67K70qbCuKR6UkWDXaOQxMEj52ODKnnULzed1nJtBxZQttgBPCTJtT4kBiSC7CuU0GyjwbbnlsFceCOAFiOQeXBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
المجرم الصهيوني بن غفير يدعو إلى إستهداف وتدمير الضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76465" target="_blank">📅 21:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2928afc4bf.mp4?token=Ez7BKGh0_mJ7qIZ-evu638yPZOTEh65ZCWsiEA7T4h5VdtjPo1WRAm9T0s7F64uVUvLHd1c-y2ZRuKHFi1Xj3WWuKJSFq17k5vnMV2KLZn_0MNM3N3dPH8G6Pi1g09md1_B8xvGCk7nbdCofHRq8eyQIVvUwIGHetUL_6qKWaQl42aqEjxCHXfMFm-6GJT6m64X0IifkFXJwu38vbJxN8iH53JPYiWU5D6X1XJpWCLxkNiPmgAcNCYCU3RgsXw_JpCu5CgQMnRdBHEKCBcWys3zXwvEcZxSzPBZ7K4SDvqABlKhECo6HO6blJKB3HeA0632p7p_MnyHpKDHwgpVXkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2928afc4bf.mp4?token=Ez7BKGh0_mJ7qIZ-evu638yPZOTEh65ZCWsiEA7T4h5VdtjPo1WRAm9T0s7F64uVUvLHd1c-y2ZRuKHFi1Xj3WWuKJSFq17k5vnMV2KLZn_0MNM3N3dPH8G6Pi1g09md1_B8xvGCk7nbdCofHRq8eyQIVvUwIGHetUL_6qKWaQl42aqEjxCHXfMFm-6GJT6m64X0IifkFXJwu38vbJxN8iH53JPYiWU5D6X1XJpWCLxkNiPmgAcNCYCU3RgsXw_JpCu5CgQMnRdBHEKCBcWys3zXwvEcZxSzPBZ7K4SDvqABlKhECo6HO6blJKB3HeA0632p7p_MnyHpKDHwgpVXkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من حرب رمضان..
مشاهد تظهر قصف عنيف للعدو الصهيوأمريكي على مدينة خرم آباد غربي إيران.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/76464" target="_blank">📅 21:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76463">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🌟
حزب الله ينشر:
תזכורת... שום "אזור בטחון" לא ימנע את הפעלתן</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76463" target="_blank">📅 21:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76462">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Rv5KNwtpyYZidu4VMW-47Y-3_AvEuUDE3oS6Fqj3NRbt4u23Jlo19eYbT8a_6kXIULAprishmClP6pXm6fLtBPyMdJI4Tk7Zq51UGshMfIERcfcOOy7y9w34MULdbevHYJHGQmAOCTaqAhx8jyVyK1q1hh2LbScULKNjmeFqv1zkcj3rXKZzkNUMMt6GomgDk1A_3H3NHwmrkIuzgwh5mGCFd9oIP8lyTjiyxTFBj34XcdIycZ6XiFnWVlLiVoXPn1rLp9AhLxJdPP2eOBj0jII5qAhtKo4oxicJXf7H4DHnCopgjpkpc60xgMv7eC44nLHTeT0NI8VZCFZ190ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية المحرمة دولياً على بلدة ارنون بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76462" target="_blank">📅 21:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
الجيش أعد خطة هجومية في عمق لبنان بانتظار موافقة المستوى السياسي.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76461" target="_blank">📅 20:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joB-DaJmFyvrHi0jNRPMwmJgrtgnUxH1gWiB_sHHOnS12xbxR1R2W8xL7bPvnwpYi7M05gug6U3rtrKJMLp78Lr_WP4vWcb6J6A86Y8xf7BksRqMYdCqeImW2jqRLJdnObtlDESHxXkmdQdsV04bYSAX6YmO7FY8thBlaWxmGz9muXxwBDHZwziYoyCNNX6hsaBQPRHLvzYM64F1oLqurhc1hpbll0RqvpuxJYwVbPtVN_0YCs7BaIx8hyCZ4zlNodVwgNUZCXRqAmRTeTTpVQIfihVv_Nir8aSE0AgIiejsPtqhyNGsR7PrvrKN_mQPm013MQ2AQ5nfisOdzVMCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: أفهم أن الفنانين يُعانون من "التوتر" فيما يتعلق بأدائهم يوم الأربعاء، لذا أفكر في جلب أكبر جاذبية في العالم، الرجل الذي يحصل على جمهور أكبر بكثير من إلفيس في ذروة مسيرته المهنية، ويفعل ذلك بدون غيتار، الرجل الذي يحب بلدنا أكثر من أي شخص آخر، والرجل…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76460" target="_blank">📅 20:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwwZdarpf1B3tCWzARb2GLObWIkxePSQKgJB1SgTJu1IqcsyejlZF6_9fdDCFmHuYafy13lNovED48sRvcJcl93qEFl57vnKgkfHir7o3cgI9XzBAs65JdOEdy6de4zP4KEUXOnGrhMKUODSIJ8e_ULhGFJgbkd_THYLxr-hrStsB6648gAE8MQTyzzPPn8BuLPgmahKWOTSGxJijJdUI-3tmSLAsOlqaNamjX_iKUhOy2ghCqLv21A1sSQZEgf2zFPoCDJrOGiZih4hTD_rikjO5dzINXeW9T55XnBXo6aUZlFauKvUo4xCTla_W6htc_DyCwwodhHHdewwHvfxkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
إصابات مباشرة لصواريخ حزب الله وإرتفاع أعمدة الدخان في كرمئيل ومحيطها بالشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76459" target="_blank">📅 20:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1775fa1285.mp4?token=dU-tF-qyZrXuItoYAfevKj6ih4RDObUSzSDCBmLOjYvLA2P66gpdGppaJkQhkesR6bJvmt-4yL-8MiWpKOLXM1tFFmNa1n_7msqBFGjVVZ-E4BOMcO_bNUQflLGfcoNc6KPBaMI5_zR4aI85jmWPu46YYiOX1OHNds9k0cpczOasFaMIz7szFejJIKJ_GILRCOHJwDV5Z7r3fV4iAl5p8PLgY3DSr12FpkXvpJIrX3kIFNHUS-smbaqcLzrX8pA8hL2OSg6M3Z4Esx5K04cUUvmbmMXCVUJm6qM9D21VQS1krjUuVBcTioWNVEopQAlHzSd4BbOYZC-DrndS_XrQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1775fa1285.mp4?token=dU-tF-qyZrXuItoYAfevKj6ih4RDObUSzSDCBmLOjYvLA2P66gpdGppaJkQhkesR6bJvmt-4yL-8MiWpKOLXM1tFFmNa1n_7msqBFGjVVZ-E4BOMcO_bNUQflLGfcoNc6KPBaMI5_zR4aI85jmWPu46YYiOX1OHNds9k0cpczOasFaMIz7szFejJIKJ_GILRCOHJwDV5Z7r3fV4iAl5p8PLgY3DSr12FpkXvpJIrX3kIFNHUS-smbaqcLzrX8pA8hL2OSg6M3Z4Esx5K04cUUvmbmMXCVUJm6qM9D21VQS1krjUuVBcTioWNVEopQAlHzSd4BbOYZC-DrndS_XrQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
صواريخ حزب الله تجتاح سماء الجليل الاعلى والدفاعات الصهيونية تحاول الاعتراض.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76458" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76457">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8de7f694.mp4?token=d1t43nH_TG4oLf1fITPpze68NaADQq2IeZMREBPLIO4K60vdwHqM5YRYdCURxt9L53oE-aiT5tb-icVlxDuxfXbu16zkfveH-F2JYyYlkYt-DPGxqj4lD2KSsRXuo7zQySNEMzkH5O6Ru7OkZ4unp68f54Mm59G5H_N8yMic1j55ZZHso3srql0ana72smn6Iw86wt7HH16Hi21tPAvFOrDAl5dO0s0A_k9PBXfaUK4K1TbT5EhkYzBq1kwvT5_YmB09qB-PdIk1jNYEhps0x2qtnXK4TQJ9ShUdLPD6O-0Xf5YiEsGZpwnIVfZpCBLoMUzXrcUG3URJqV2CkWmIYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8de7f694.mp4?token=d1t43nH_TG4oLf1fITPpze68NaADQq2IeZMREBPLIO4K60vdwHqM5YRYdCURxt9L53oE-aiT5tb-icVlxDuxfXbu16zkfveH-F2JYyYlkYt-DPGxqj4lD2KSsRXuo7zQySNEMzkH5O6Ru7OkZ4unp68f54Mm59G5H_N8yMic1j55ZZHso3srql0ana72smn6Iw86wt7HH16Hi21tPAvFOrDAl5dO0s0A_k9PBXfaUK4K1TbT5EhkYzBq1kwvT5_YmB09qB-PdIk1jNYEhps0x2qtnXK4TQJ9ShUdLPD6O-0Xf5YiEsGZpwnIVfZpCBLoMUzXrcUG3URJqV2CkWmIYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الجليل الاعلى المحتل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76457" target="_blank">📅 20:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e19000063.mp4?token=VWXA5Isz_uxH90KdeTYk7alaXUcukIA79HFHmO43OVhy86v6dh1lqK-1CT7uvmnrxatGiFFtCWUHeUtzcO0rkOn_dCA5um1ZNhncG7ERkUoY4WQVk-W_eFJs9KjdcrhcIpAd8zSmGPEpXZhb-qtstez_nOFmrDajawux8mWdzcXHt9dyalyQmgUfcNdEWeIyVKLMOwGzncnRL5JYD3QDzvXwwNYXqlyULN4PSOT3iAFPwjjEzY5gQWSh0TVvF6ofIi1DM3OCxIbaNvRSyukvI162z97LjaTGgqGCv5Z3XW-vq3JmjIg8SURuyMc5M91cG7RK6Fk3_7g8XqoIxmg_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e19000063.mp4?token=VWXA5Isz_uxH90KdeTYk7alaXUcukIA79HFHmO43OVhy86v6dh1lqK-1CT7uvmnrxatGiFFtCWUHeUtzcO0rkOn_dCA5um1ZNhncG7ERkUoY4WQVk-W_eFJs9KjdcrhcIpAd8zSmGPEpXZhb-qtstez_nOFmrDajawux8mWdzcXHt9dyalyQmgUfcNdEWeIyVKLMOwGzncnRL5JYD3QDzvXwwNYXqlyULN4PSOT3iAFPwjjEzY5gQWSh0TVvF6ofIi1DM3OCxIbaNvRSyukvI162z97LjaTGgqGCv5Z3XW-vq3JmjIg8SURuyMc5M91cG7RK6Fk3_7g8XqoIxmg_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إطلاق رشقة صاروخية من لبنان نحو عمق الجليل في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/76456" target="_blank">📅 20:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1Q3Qf0ZAaklF2-xwTKxv66W1YRlKaKemoIDHbZ9UFi9bY0BoL2rRHWw86R-UFNZGVkvUfTIlFckRIo0N2ZysEhU67j9Nc5SGmdAQVV1F9MYaaL1gK-QwFDEngimNLjNK5EsNo8uU6RQmnH5fVI3uqcIaDPjylKPjKcY_pxH7iw0gQCXsGB9GAB2WckhXON1ValhZsQfc3MZYUH6W8nijyYN3k5sPW1XUdMX4aKP5caNNcHkQ9RbkbKIayfpDpWcg0hd2SJMNR_95V1Dxx-btUo8JOkQ8_V2o8y6zq6_4IkssRCYGLo_8eQ7Dn3EGWUHgf2vPwb0msHOYPvdN1HaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أفهم أن الفنانين يُعانون من "التوتر" فيما يتعلق بأدائهم يوم الأربعاء، لذا أفكر في جلب أكبر جاذبية في العالم، الرجل الذي يحصل على جمهور أكبر بكثير من إلفيس في ذروة مسيرته المهنية، ويفعل ذلك بدون غيتار، الرجل الذي يحب بلدنا أكثر من أي شخص آخر، والرجل الذي يقول البعض إنه أعظم رئيس في التاريخ (THE GOAT!)، دونالد ج. ترامب، ليحل محل هؤلاء "الفنانين" ذوي الأجور المرتفعة والمستوى المتوسط، وإلقاء خطابًا رئيسيًا، محفزًا البلاد للأمام كما فعلت منذ أن أصبحت رئيسًا!
قبل عامين، كانت الولايات المتحدة "ميتة". الآن لدينا البلد "الأكثر سخونة" في أي مكان في العالم. لا أريد ما يسمى "الفنانين" الذين يحصلون على أموال أكثر من اللازم، والذين ليسوا سعداء. أريد فقط أن أكون محاطًا بأشخاص سعداء، وأشخاص أذكياء، وأشخاص ناجحين، وأشخاص يعرفون كيف يفوزون.
لذلك، بنسخة من هذه الحقيقة، أأمر ممثلي ببحث جدوى إقامة تجمع "أمريكا عادت" يوم الأربعاء، واشنطن العاصمة، في نفس الوقت ونفس المكان. فقط الوطنيين العظماء مدعوون - سيكون احتفالًا مجنونًا وجميلًا بأمريكا!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76455" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
إطلاق رشقة صاروخية من لبنان نحو عمق الجليل في الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/76454" target="_blank">📅 19:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇺🇸
‏
مسؤول أميركي:
إيقاف سفينة تجارية حاولت التوجه نحو ميناء إيراني ؛ ‏الناقلة "ليان ستار" تجاهلت تحذيرات قواتنا البحرية في خليج عمان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76453" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
25-05-2026
غرفة قيادة تابعة لجيش العدو الإسرائيلي في ثكنة أفيفيم على الحدود اللبنانيّة الجنوبيّة بمحلّقة أبابيل الانقضاضية.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76452" target="_blank">📅 19:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XruwmDb9-wYSm29Mfa54L-tM2BKEEWdOlbilPrg4IC3mXiFYBUC2PaDZdrG6yQ69o5B5sizk2X2NjVtZYQFzk_KN2R3vZd3gkktIdjkReXOaPXK4V6LG0_FZgg5BxhefKNu-xOwi8eeqXNA56-4g1037ai-hMrphwOzubBbv8sJ-NSh9KwqGq1hq0coHVDyvlH1bZ6_M6SoQ1nesSGMWiKLSEQ6B_7Irmr2LPVVGjgQ0l2vmuEc06F2BsC5L3MIQ9zjjEcZKEZImNHS9XYaQi05-iPCPiJBVn8wbY_7O35g4NwhUvj57A-i9jJ9b0vJ98D_koC-0Lq3s7FOAq5Lkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
قصف صهيوني بالقنابل الفسفورية المحرمة دولياً على بلدة ارنون بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76451" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
نظراً لأهمية سلامة هذا الممر المائي، يُشدد على ضرورة التزام جميع السفن، التجارية منها والناقلات، بالمرور عبر المسارات المحددة فقط، والحصول على تصريح من البحرية التابعة للحرس الثوري الإسلامي. وأي مخالفة لهذه اللوائح ستُعرّض أمن الملاحة للخطر الشديد. كما يُحذّر من أن أي عمل تقوم به السفن العسكرية للتدخل في إدارة مضيق هرمز أو تعطيل الملاحة سيُقابل بردود فعل عنيفة من القوات المسلحة للجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76450" target="_blank">📅 18:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76449">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وقوة عسكرية تابعة لجيش الإحتلال الإسرائيلي في بلدة زوطر الشرقية بجنوب لبنان بعدد من الصواريخ الموجهة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76449" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b701e99bcc.mp4?token=XMO4zNeXmsQolPcg64Uuft2rKiOt3dz0T8ovi8AX3A_9K0RDZ_suJKtJivwl712MdpudWDrM-k10CU4IpFqWpz9LClZ_2d83JEwoiia5OP95UIOibGmjsahPVxnIG_uJ4vtcErpT_H8fQOc8mO7QF4GoHdNtFsNmM0jmmKOE3x1xJaoFViGPlQDXVMkgG9bLXt36WaSzKP2qTqc5tbEibdXG54iidmQjxIUv4uqP1w8TgHQDl1ctgd-DhOOT3_8Ba3S9dOMm7ohZjuTwayAst-xDqiC-ViefKDzufOCx5trxoxnPqE26bXbuOmrdJJzqNtbQeLOIqSuI8f11mmNRTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b701e99bcc.mp4?token=XMO4zNeXmsQolPcg64Uuft2rKiOt3dz0T8ovi8AX3A_9K0RDZ_suJKtJivwl712MdpudWDrM-k10CU4IpFqWpz9LClZ_2d83JEwoiia5OP95UIOibGmjsahPVxnIG_uJ4vtcErpT_H8fQOc8mO7QF4GoHdNtFsNmM0jmmKOE3x1xJaoFViGPlQDXVMkgG9bLXt36WaSzKP2qTqc5tbEibdXG54iidmQjxIUv4uqP1w8TgHQDl1ctgd-DhOOT3_8Ba3S9dOMm7ohZjuTwayAst-xDqiC-ViefKDzufOCx5trxoxnPqE26bXbuOmrdJJzqNtbQeLOIqSuI8f11mmNRTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد تظهر تساقط الصواريخ التي اطلقها حزب الله على شواطئ نهاريا وهروب الصهاينة نحو الملاجئ.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76448" target="_blank">📅 18:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وقوة عسكرية تابعة لجيش الإحتلال الإسرائيلي في بلدة زوطر الشرقية بجنوب لبنان بعدد من الصواريخ الموجهة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76447" target="_blank">📅 18:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ecb8455d.mp4?token=KAbryvOy2N1tbrmKqrSpISI5ir7iu5IoFwXC09aroORmxy0II6p1NfMXtk2ShFxX4CPWCU_THKlm0IWb9CyUKG6LjkNeocCSz-fpaKndG2gnMk_M_FaDoPZeqIdAMQN8DwfJYcHMKic1rG6Sy2zbhWM2h9gy2NF_Kwz9oYN5ctVb0FNB9S0ubg37wz7xhe85ab_bQVJ9Y7T4mSUxcfDQFF7XJSqC-dAb-7GnbaX0OASCBjcElyMrPHb3Ntz4XHd3qOrWgTTsd-XXcGJ5zsEYQVzfeB6KvifTjIi-5HJs5lzo0HKliPOcayYrR8qwJfQCaUkQ9UWlAD0zquEMB_7774WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ecb8455d.mp4?token=KAbryvOy2N1tbrmKqrSpISI5ir7iu5IoFwXC09aroORmxy0II6p1NfMXtk2ShFxX4CPWCU_THKlm0IWb9CyUKG6LjkNeocCSz-fpaKndG2gnMk_M_FaDoPZeqIdAMQN8DwfJYcHMKic1rG6Sy2zbhWM2h9gy2NF_Kwz9oYN5ctVb0FNB9S0ubg37wz7xhe85ab_bQVJ9Y7T4mSUxcfDQFF7XJSqC-dAb-7GnbaX0OASCBjcElyMrPHb3Ntz4XHd3qOrWgTTsd-XXcGJ5zsEYQVzfeB6KvifTjIi-5HJs5lzo0HKliPOcayYrR8qwJfQCaUkQ9UWlAD0zquEMB_7774WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
في الوقت الذي تنتشر فيه صور قادة إقليم كردستان في شوارع المحافظات العراقية بكل حرية، مُنع مواطن من دخول محافظة دهوك شمالي العراق بسبب وضعه صورًا للشهيد السيد علي الخامنئي والشهيد أبي مهدي المهندس على مركبته.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76446" target="_blank">📅 18:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5e397810.mp4?token=Fdyi-YEPU2X2Eeo2ZT5EMqcceXdecRgFS0t6dlXzWlhLTV_9u8yP55saNwloqoHzvSPHvlNlNSr8fasdVeAer3mp7zg5-jPznldpInPpslYUv76k4izvndzogeUG7pxt0E72ssQ_oo1tB8CyDUIDfdivLKZczVMcF8IJFIGZ8u9My3Vx0IKsr0l4K_cObt8RQhxaU-tcWsLjLvan_rrw4mgBS3W7rjHXvTAe3h_BbzyHboGQUikWcgzyy27gMBFq_Lj44uACVkxH95kifXZZtNYUsLngAZAEZ_FEU07lUeW4VHAxUY_iece68LtzKgXNjYgBgoYwHZcA7RmL-fjY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5e397810.mp4?token=Fdyi-YEPU2X2Eeo2ZT5EMqcceXdecRgFS0t6dlXzWlhLTV_9u8yP55saNwloqoHzvSPHvlNlNSr8fasdVeAer3mp7zg5-jPznldpInPpslYUv76k4izvndzogeUG7pxt0E72ssQ_oo1tB8CyDUIDfdivLKZczVMcF8IJFIGZ8u9My3Vx0IKsr0l4K_cObt8RQhxaU-tcWsLjLvan_rrw4mgBS3W7rjHXvTAe3h_BbzyHboGQUikWcgzyy27gMBFq_Lj44uACVkxH95kifXZZtNYUsLngAZAEZ_FEU07lUeW4VHAxUY_iece68LtzKgXNjYgBgoYwHZcA7RmL-fjY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
مشاهد تظهر تساقط الصواريخ التي اطلقها حزب الله على شواطئ نهاريا وهروب الصهاينة نحو الملاجئ.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76445" target="_blank">📅 17:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjA-gkJ0ssI6uwazmpzkhTZ34kKku-NRLh4Px8MD4MzhSimZYFg5EeLkOrBIuBtabOk15Jv0pfAQla-wOHDiOjjw9oynHdj8twX18_75OsHxxotXzc6H8h9O1bK4vCFeuIQd0TYAlOHQQyf_PK-_jq7S0Ko--WTgvWGY0rRteztYEbjiWjlvNf3Ao9KnyLSJ_9EANdBbxUpvKzA7HhGpiJw_4BRzsENBGuuqHGn3PJg_UYThxw1KMdelRMBbO04sSehkGYcU6zPg-NGVwGkZtYs13xKs7rAidEw65taDsgISz4z9YYZuLZEnh_2fHuX6z2ob7WjK8c2YZ47jeQ8xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول خطوة عملية
لضم سرايا السلام للقوات الامنية ؛ الزيدي يلتقي ابو دعاء وتحسين الحميداوي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76444" target="_blank">📅 16:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1476d1a303.mp4?token=WuQlhQPik4__UUfVWuURgb1YzMBS5JgkmdGc4CqVbSChUNbGOei7xpzRA6avzYbzA0qv31Npf6E3eATfvPICkrfmTPi-3UEzpFZ6ewagISjUy41kJ2_Is-pBfioUbHsv9Q-HR1Fe0HsnIZvGc8ZLSWW62a0z8fG9nlPxVwlk_XPVfJUUOKmdX0L9MSu3bdqZbSLcB-vXqc8Q7o7YWMvQT_ZgHhPkpiWROwp2CnMk-G9oYu8seq_3PGi_qIZqe7uIl6B8y2VMDosvvj3GffrHTWGLLgYJE3Kj4mrvciIuPUzKM0ji9HioPvg2IhXSv7YJtACIj_6Agb5jiG3VXcl6SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1476d1a303.mp4?token=WuQlhQPik4__UUfVWuURgb1YzMBS5JgkmdGc4CqVbSChUNbGOei7xpzRA6avzYbzA0qv31Npf6E3eATfvPICkrfmTPi-3UEzpFZ6ewagISjUy41kJ2_Is-pBfioUbHsv9Q-HR1Fe0HsnIZvGc8ZLSWW62a0z8fG9nlPxVwlk_XPVfJUUOKmdX0L9MSu3bdqZbSLcB-vXqc8Q7o7YWMvQT_ZgHhPkpiWROwp2CnMk-G9oYu8seq_3PGi_qIZqe7uIl6B8y2VMDosvvj3GffrHTWGLLgYJE3Kj4mrvciIuPUzKM0ji9HioPvg2IhXSv7YJtACIj_6Agb5jiG3VXcl6SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
انفجار طائرة بدون طيار اطلقها حزب الله قرب مستوطنة المطلة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76443" target="_blank">📅 15:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇱🇧
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 27-05-2026 تجمّع آليات وجنود جيش العدو الإسرائيلي على أطراف بلدة زوطر الشرقية جنوبيّ لبنان بالصواريخ والقذائف المدفعيّة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76442" target="_blank">📅 15:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
طيران حربي يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76441" target="_blank">📅 15:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
‏
مركز الأمن البحري العماني:
نحث السفن على توخي الحذر إثر رصد جسم عائم يشتبه بأنه لغم غرب منطقة المرور في هرمز.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76440" target="_blank">📅 15:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#بالوثيقة
🌟
الاتحاد العراقي لكرة القدم يتهم رئيس الاتحاد السابق عدنان درجال بسرقة (500) الف دولار اهداها الحلبوسي للاعبين بعد التأهل لكأس العالم.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76439" target="_blank">📅 15:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTfpOnfLnGQ21U9V57jJhlHzTGeq2TQFABig-Hx8UdbsStGdsf1pmjMOLKh35BnbK9OK1vdzjV6fMT4ZUu02mPfooCOjZKlbZQhqGyItV35W9B6_yDqzCipiEx5QTgRVy4nWBn6WmXwWgxFwQ_WJ0apuRj0Ll6P9Iu7zgOr7m2Fxk0Sxeu3l08Ss9uW2f9IBD-jL8d-Pp703XtYO3KA3yXsyw9sMdyTlBUTUtf-rZjy537xIIn7xnA9k1WQLOBKz4FVExOiBBOJ1FD1pq07lK8o1seFeRmMIVZuM0JuIHpjKoVDudA9wx0SSt2C3taDntOAZEn7unQ0Vy0WmUuBBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76438" target="_blank">📅 15:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmboelBtp4tlx7kjR7Xle3Lk00PkebTk6br9Aaicw_a2C7G2-FwzeJa-xiD418VFbt-VtXj9jk_26zuQTi_G-9mtmje-3te-CXZAK_45c5geqFYle1UQ9IVwna9ON75tTowJAg0OlYPBTj8JAByYmnywxmlfEINWe0k5MVHyQ98rkK3UHxbpcGxFKuqWXBUwtUoDSlqLxinj6EtYYTsF96Gsjed2gTOUGO1sSjWwPW6yZErmZfCA6-vbIwbdV_ffDLvcoJBBDz4h6-4kEmqYx4786VOOEhL1jDst7Omi72luo8HYep28kIHNRoyYP9gzTTyWdL-6Lhcq2wriYO-JqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
فوز المرشح يونس محمود لرئاسة الاتحاد العراقي لكرة القدم.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76436" target="_blank">📅 15:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو:
انفجرت محلّقة مفخخة في منطقة عسكرية في منطقة شوميراه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/76435" target="_blank">📅 14:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76434">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76434" target="_blank">📅 14:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76433">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇦
زيلينسكي:
الجيش الأوكراني يضرب منشأة النفط الروسية في أرمافير، على بعد 500 كم من الحدود الأوكرانية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/76433" target="_blank">📅 14:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76432">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGJT5y10f7_SKFnPHrV5Z7lg7L12HnlLGvDsS2zKkeB3C9QPLjDvjbHZCMd-2hx7IXaa8eX51D9ovg2BJKt6RxvMtj5vOSd1xMOoxc6sgthfuvU9XYII-u555HyMXDDiG1x8aE3Bzt8w34bb80wmkGAPttAGWN2ROLkb5D3cRsgAfm6LBh5LPLpgTMPAGMtkFmduWTK5VfnDPjAU27oM1Qup5OqSGkbq9P4y8TB1vVOtp6C_5741rXgS-kUBq_9YElvxzHBQQAd4n7wuUYUX4kjbQZDgJ6VZlZv9BOVSVTuA3IHfMao2f_y2o7JvetdcJIE8OCvsxbu_zQb9TkiEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوة خاصة تعتقل "عدنان محمد حمود الجميلي" وكيل وزارة النفط العراقية ومدير عام مصافي بيجي بتهم فساد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76432" target="_blank">📅 14:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
انفجار محلّقة مفخخة قبل قليل داخل موقع عسكري مواجه لمستوطنة شلومي بالجليل الغربي وفي جنوب لبنان منذ ساعات الصباح هاجمت 5 محلّقات مفخخة
قوات الجيش الإسرائيلي
.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76430" target="_blank">📅 13:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
🇹🇷
اشتباكات عند الحدود الايرانية التركية بين القوات المسلحة الايرانية وارهابيين ؛ مقتل 2 إرهابيين وإصابة أخرين.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76429" target="_blank">📅 13:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📰
صحيفة المونيتور عن مصدر استخباراتي إسرائيلي رفيع المستوى: كانت خطة إطاحة النظام الإيراني بالتعاون مع الكرد شاملة ومفصلة، الأميركيون كانوا على دراية تامة بالخطة لأنهم تلقوا إحاطة شاملة. الكرد كانوا متحمسين لتنفيذ العملية لكن واشنطن أوقفتها في اللحظة الأخيرة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/76428" target="_blank">📅 13:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76427">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📰
صحيفة المونيتور عن مصدر استخباراتي إسرائيلي رفيع المستوى:
كانت خطة إطاحة النظام الإيراني بالتعاون مع الكرد شاملة ومفصلة، الأميركيون كانوا على دراية تامة بالخطة لأنهم تلقوا إحاطة شاملة. الكرد كانوا متحمسين لتنفيذ العملية لكن واشنطن أوقفتها في اللحظة الأخيرة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76427" target="_blank">📅 13:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚔️
كتائب حزب الله : نرحب بكل خطوة يتخذها "  الأخوة غير المنخرطين "   بحصر السلاح بيد الدولة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76426" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76425">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚔️
كتائب حزب الله : نرحب بكل خطوة يتخذها
"  الأخوة غير المنخرطين "
بحصر السلاح بيد الدولة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76425" target="_blank">📅 13:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مجاهد العساف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtVgZEt6fZyDpVFNppngpvn6c5OmZNqS4sr1C5yEmTJpKMIaXU0KH9hYS261tVSqG4hbgMw5uj-Erlw45bgWjXvLbHbUFX0d32aSRxn_faSjMsiyB_KFDVGcIAcp3xC8qNloVospVBvEL5TxKl3KzcuU4ETq3MMFQzxXXhjAzJFPGTYI7UQ2frO3fOW0JKSR8vJokaSWfYFgxA53nFQ937ZBYxI8T0uDzGXE5PEoS3mljbt4mII1QxAeOYgDJwRxeVnaCMVR2994Zxgm0fzwzmv9T_IUMzIaUsBTOGu87jh-7o4FOy-ICTnFbygHF5_2Cz6Uk3hgKtpTyQ_-ABYtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/76424" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76423">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfa76d18e.mp4?token=eKvO5S9ozoViL0BFaK3UtM1pfZ5A5FAbYQ2cOCtfDRO3zQ53sTzAr5yhWchyE41VG_oAl_3l3xCdFAvmKfs92EqTfuLmOnZaiIlzQvMEEWmI6w4rZSwdU4NAl6PugeUW4kzSnYDlk_LJ3NHab5TcmPjav0c986ZdfJuUFhjhhU5qYcfruXNgavdEJO0NHSUQM9ZZ09gPF5YDLWi7mQmQNwgF29MZUg7NIURnMGOFRaNkuyTN5WLCNJJVAO8UlzQOaDYAaId-9gXiETRRQB2RO0xMUmj7MMk21FIbNjOJwU7-zJsv5II0wpJhLZb7xn999_F2j32S1eekusKT0ngJClVn-HQKJPOKTZAaEDDjFUid2YBitLl8M17PYtUg6N5xurzHAzavnq10JmvL0fBkCLQylTxt6oSibeAJf0bMDbweA3rQUCEBgZmvTSr4H2M716zX5UO0IX4dTalk1LOqIS8JZWnd-ucDE6eO767sgM5htWOhkcn5n3a3xrMHbKV8sqTt2kuxanqZPB3rCaFPNflBP9QD-cflKizeqxdS0jAzILpOVuXgavVigsnoGYS1KTP2XIK_b02uld_y7Ew4nJQd8bmzrC8YD1jOxrcOgQBulqMgKZ-rv1bb0m2SxdWxE6Slp_bhyNpF_WByohpSuZIGuNouwy0tK1HRV6MnAbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfa76d18e.mp4?token=eKvO5S9ozoViL0BFaK3UtM1pfZ5A5FAbYQ2cOCtfDRO3zQ53sTzAr5yhWchyE41VG_oAl_3l3xCdFAvmKfs92EqTfuLmOnZaiIlzQvMEEWmI6w4rZSwdU4NAl6PugeUW4kzSnYDlk_LJ3NHab5TcmPjav0c986ZdfJuUFhjhhU5qYcfruXNgavdEJO0NHSUQM9ZZ09gPF5YDLWi7mQmQNwgF29MZUg7NIURnMGOFRaNkuyTN5WLCNJJVAO8UlzQOaDYAaId-9gXiETRRQB2RO0xMUmj7MMk21FIbNjOJwU7-zJsv5II0wpJhLZb7xn999_F2j32S1eekusKT0ngJClVn-HQKJPOKTZAaEDDjFUid2YBitLl8M17PYtUg6N5xurzHAzavnq10JmvL0fBkCLQylTxt6oSibeAJf0bMDbweA3rQUCEBgZmvTSr4H2M716zX5UO0IX4dTalk1LOqIS8JZWnd-ucDE6eO767sgM5htWOhkcn5n3a3xrMHbKV8sqTt2kuxanqZPB3rCaFPNflBP9QD-cflKizeqxdS0jAzILpOVuXgavVigsnoGYS1KTP2XIK_b02uld_y7Ew4nJQd8bmzrC8YD1jOxrcOgQBulqMgKZ-rv1bb0m2SxdWxE6Slp_bhyNpF_WByohpSuZIGuNouwy0tK1HRV6MnAbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
شنت قوات زلينسكي الأوكرانية مدعومة بمعلومات من استخبارات الناتو هجوماً على مطار تاغانروغ العسكري ليلاً، مما أدى إلى تدمير منظومة صواريخ إسكندر الباليستية وطائرتين من طراز Tu-142 على الأرض.
‏
تدمير طائرتين من طراز Tu-142 في ليلة واحدة، وهذا يمثل ضربة قوية لروسيا:
‏تُعدّ طائرة Tu-142 طائرة دورية بحرية ومضادة للغواصات تعود إلى الحقبة السوفيتية، وهي مشتقة من قاذفة القنابل Tu-95 Bear. وقد استخدمتها روسيا بشكل أساسي للاستطلاع البحري بعيد المدى، ودوريات مكافحة الغواصات لتتبع تحركات غواصات الناتو، وحمل طوربيدات قادرة على حمل رؤوس نووية في بعض الأحيان.
‏الحقيقة هي أن روسيا لم يتبق لديها سوى عدد قليل جدًا من هذه الطائرات. فقد تقلص أسطول طائرات Tu-142 على مدى سنوات دون وجود بديل حديث قيد الإنتاج.
﻿</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/76423" target="_blank">📅 12:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76422">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
حزب الله: مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 27-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة زوطر الشرقية جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/76422" target="_blank">📅 12:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76421">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81bb9767dc.mp4?token=XHCJhw9Xg68_9lW6b5Q9fd_07rCrYlu7avF2CPsR5BiRXiO3KRla1pFvMPVAKE5slBeQW_9Af66VPl_QQUtfpFqkJt8WxFLsotMCD-rRq0-a-lENTco-5h9aQYuVLX0Aet8uQz9-3RW4GeF7YGOjMTmc8AIxZqqFjtJAtv6sIPR5iqwKZmV51dr2Pxnng4XDfEeZvoxLHunHUhgZUEWlQi3sLqMmirPU71xP-whfNW8rIiibFs0ubcudjFwaHea9uL4Ra_KyGKN6p22-xhSYzOKRjzq5tzETUMOadp4T24-uP8_H1jTHk55LvpMIZm5RVns-esLRdv06VyGgQgFWjjaPHtqNALw5hz3ZFL4k5mJU5qve7DsBGxrXl7x-iXGNfyIDF7XZdH4S2Sr_fvrCRuF8wgRFhsHfv2lSkcMEQG3rvpaSCQ1szy9m4pObCtLJ743hNnahIsvNjYAebxzPuWideXsjYvH8_0hqDY5TYtAV8EPHabzen0SkIUrII5_xw2SV4NviBG_cL95uTrPsUZN-MovnUllzy3Opl-ZC2h9vV6LZOvNRJ8g16QMncXHs5pAu0EdtamVmceARi-naCpnaTR2GYMc_9XpdiUR0LrjwLvsvb8f3eY4TjHWMOXLbwpiAX_1PXK9J62DsCEKK6WYfw6SSGD9-D8glV4mFFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81bb9767dc.mp4?token=XHCJhw9Xg68_9lW6b5Q9fd_07rCrYlu7avF2CPsR5BiRXiO3KRla1pFvMPVAKE5slBeQW_9Af66VPl_QQUtfpFqkJt8WxFLsotMCD-rRq0-a-lENTco-5h9aQYuVLX0Aet8uQz9-3RW4GeF7YGOjMTmc8AIxZqqFjtJAtv6sIPR5iqwKZmV51dr2Pxnng4XDfEeZvoxLHunHUhgZUEWlQi3sLqMmirPU71xP-whfNW8rIiibFs0ubcudjFwaHea9uL4Ra_KyGKN6p22-xhSYzOKRjzq5tzETUMOadp4T24-uP8_H1jTHk55LvpMIZm5RVns-esLRdv06VyGgQgFWjjaPHtqNALw5hz3ZFL4k5mJU5qve7DsBGxrXl7x-iXGNfyIDF7XZdH4S2Sr_fvrCRuF8wgRFhsHfv2lSkcMEQG3rvpaSCQ1szy9m4pObCtLJ743hNnahIsvNjYAebxzPuWideXsjYvH8_0hqDY5TYtAV8EPHabzen0SkIUrII5_xw2SV4NviBG_cL95uTrPsUZN-MovnUllzy3Opl-ZC2h9vV6LZOvNRJ8g16QMncXHs5pAu0EdtamVmceARi-naCpnaTR2GYMc_9XpdiUR0LrjwLvsvb8f3eY4TjHWMOXLbwpiAX_1PXK9J62DsCEKK6WYfw6SSGD9-D8glV4mFFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
الانهيارات تصل إلى الحدود العراقية السورية.. انهيار جسر المراشدة _الباغوز بريف دير الزور الشرقي والمحاذية تماماً للعراق بسبب فيضان نهر الفرات.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76421" target="_blank">📅 12:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76420">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ول ستريت جورنال:
اشتكت السعودية للولايات المتحدة من أن هجمات الإمارات على إيران تزيد من خطر تعرض منشآت الطاقة الإقليمية لهجمات إيرانية. وطالبت السعودية الولايات المتحدة بالضغط على الإمارات لوقف الهجمات الانتقامية والانضمام إلى الجهود الدبلوماسية التي تبذلها دول المنطقة .</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/76420" target="_blank">📅 11:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇩🇪
إغلاق مطار ميونيخ في ألمانيا بعد رصد مسيّرة</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/76419" target="_blank">📅 11:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Homayoun Shajarian - Iran e Man (همایون شجریان و سهراب پورناظری…</div>
  <div class="tg-doc-extra">Melodifa</div>
</div>
<a href="https://t.me/naya_foriraq/76418" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#شاركها</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76418" target="_blank">📅 11:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
🇮🇷
أفادت وكالة بلومبيرغ بإصابة عدد من أفراد الجيش الأمريكي وتضرر طائرتين مسيرتين من طراز MQ-9 Reaper بشكل بالغ في قاعدة علي السالم الجوية الكويتية خلال هجوم إيراني وقع مطلع هذا الأسبوع. وذكرت القيادة المركزية الأمريكية (سنتكوم) أن الدفاعات الجوية الكويتية…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/76417" target="_blank">📅 11:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
🇮🇷
أفادت وكالة بلومبيرغ بإصابة عدد من أفراد الجيش الأمريكي وتضرر طائرتين مسيرتين من طراز MQ-9 Reaper بشكل بالغ في قاعدة علي السالم الجوية الكويتية خلال هجوم إيراني وقع مطلع هذا الأسبوع. وذكرت القيادة المركزية الأمريكية (سنتكوم) أن الدفاعات الجوية الكويتية اعترضت صاروخاً كان يستهدف القاعدة في 27 مايو/أيار، إلا أن بلومبيرغ أفادت بأن شظايا من الصاروخ المعترض أصابت القاعدة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76416" target="_blank">📅 11:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76415" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🌟
حزب الله: فجرنا مسيّرة إسرائيليّة من نوع "هرمز  450 - زيك" في أجواء بلدة زوطر الشرقيّة بصاروخ أرض جو.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76414" target="_blank">📅 11:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92fdb1ed99.mp4?token=WRIHGejPGx0i5iLtUpPL7iIlxkAemWoCINtZk3YyuF0ZNOfeb5pv1rcQz8Hr-caIZldoAk1T8vYGrdzQK94munqYg--7pJ5mrrFhtVuvUWR_YL6V9nm6wFiYRkXY3af36wc-lTeib6uej_zCcUF0oQSxnh7dsnumLrr2MdmTS_-qPaTf89XvUmNgh0e_wGoziT8JqJ_VcVADtC9NPPG_3x1WT48ervwGuonCiKP6_6-N9Ib0-d8OwM1thljcCbUsOtMG3mnBfsaBd_Tv8tPaJq0Ooi8NVxPnLbqFZgBMXGsIf2sgS9C14hkugqPtJpPs3LlW80q1D5r13dJ4dMZ4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92fdb1ed99.mp4?token=WRIHGejPGx0i5iLtUpPL7iIlxkAemWoCINtZk3YyuF0ZNOfeb5pv1rcQz8Hr-caIZldoAk1T8vYGrdzQK94munqYg--7pJ5mrrFhtVuvUWR_YL6V9nm6wFiYRkXY3af36wc-lTeib6uej_zCcUF0oQSxnh7dsnumLrr2MdmTS_-qPaTf89XvUmNgh0e_wGoziT8JqJ_VcVADtC9NPPG_3x1WT48ervwGuonCiKP6_6-N9Ib0-d8OwM1thljcCbUsOtMG3mnBfsaBd_Tv8tPaJq0Ooi8NVxPnLbqFZgBMXGsIf2sgS9C14hkugqPtJpPs3LlW80q1D5r13dJ4dMZ4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">" سيوف بيد الزيدي "
ارتياح شعبي كبير في الشارع العراقي بعد أغنية الفنان حاتم العراقي بأغنية تتغنى بدولة رئيس الوزراء والإنجازات العظيمة المتحققة و التي عبر عنها مراقبون على انها سمفونية او معلقة او تشبه بخارطة طريق للخروج من بوتقة الأزمة السياسية التي تمر بالبلاد على أمل ان يخرج المارد من القمقم ويرجع العراق يصدر الكهرباء لدول الجوار  …</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76413" target="_blank">📅 10:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1kcCRnL7kERow243II_d69GDZjt7BVLL9R14j5T_oR_utJNxbyW889zCC9jLBmJ8Wbdmkgeb7J8QFZnDukFLH0XhR303wFXcuiEsj4evJKB_IaJjevPNvUNBYCAdE3XB9N0q0Zqk3-F7xCu1EXz0bDRgZib_e9elVOMU6F4dIZhWOGdOl_jteJx6vTXsGuIVwLECpXM6X3gmJJ1IBcJQi8y941kFcyvKsMVH4kCR3GlPaWsaZ4sANnz2ZjgIAYzz9TCbQs9mFE373-49su284IwzFfdklK-ddFATpGZY96FRuKjXV7V-WKVfLueajQx3JszT5HuBzJP9wLmJy-2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏥
في حالة نادرة جداً.. ولادة طفل برأسين داخل مستشفى اليرموك بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76412" target="_blank">📅 10:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76409">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AST0mlXQUGx_l4KCITAecRMrN_E6b3zZmfkAMgN0LSQpAWm_9azkhRflHoQetLOeLzTIW5BLQeVu55pJwE2xYpPRwWi0INL4iOwBwy9EoaXBFJmMjDIHgg5E7htvvxFY2Zbr6nq8wNEDsYTHxNCZ8r-LVzUedzUguCIC5D3P76oVheXbjmsAWYKMzhMfB09cJnHnSk_uiiGDvvOq1SoXVXxbTlGOPY2J5se-Lx3iGurUpf0G-IlctKZSCYKSNGN_BRW6sW395MB5ekHmbmnQPvm8aZXqPnyk5FNSuD2h9dD09aQlKWw-SJX--QtCfjRoBcpJNflZsvxGVesTNzKL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQ_ZYyeYCvjfeG_X1Ty32EkaMB7-vWp-lvVZe1qiRF5wSVtfQQTQcV9Sj0WgkJTQBerz4mFy_7W6i1dYWxreGBmQeH5QmzwR6yKPAiXGRmyxU6q1zhMfh4QvUkGfVlDgeKmapvCFTnBsoDevXAQttFxHIVldyeSlD6JIRC9NXBnnkDVEQii-kUeOxs1wGz07nKrUthqvoUyk3AIp25Cziu_qlKBgjBJMbPKQROIq4Tpz8RkS_4ihvfqox_qJBaeox6zGowYgWwAOg-W2PNmk_-LgUqcxpTBkT_bAga9UADtqngGgxNPPmSTpwgVW_hwSgO7lKMS8qklFoVqm_urLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjDEASYKE58FZXjvHqbezIb9IWbFertCWFjM69s_CBiQzUy13Rrhafd7na-xUMimwhiaJNonnufaMmSbXTJpjr5xI63OLXW5pTZw5XoAeRxqKi7AU-AFHOKyyLjaTV94qeyV7L1RbsXjDVkWfdH8hHTYFmYRLYlY6EN_nHbI5IUO6wARw9lWAU0XPHrYNwFgY8qGJZ179OZ9U5aB4Ck_3WG641Kg7lXbYAFUFfo6WgPNm7syCnfyH28yY_DRUnjewwocne1rBvvWYWb7XRWtcVV6CdqSr1QFV3tLAWH88_oUyAkR-Vsgktm7go008Lq0pr72zRMfgk52mJ7xkPd4jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
أصدر البيت الأبيض أحدث تقرير للفحص البدني الذي خضع له ترامب.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/76409" target="_blank">📅 09:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23184ff86c.mp4?token=USnqjr9dXWjqD2i2nxEbr_9SGYY-vMM60T4cS7eOZ0fD6fgWiWw4DhuH8uTA8XH4OHgdXSjnenCPv_NXWLrp36YFcyk1EHryKm0AtUIj6nYlsx83OiS8-epuSMRMaV6plUXpp1U_3SL5MF__O7aKQRLk1e1m60_hoCzHqRLpC_jS5UDF91ulmqq_IxCwBucIkLGAUZIm6y0QjKyigE3LVCWOk8VuECPN5Y38gNfMYmwChk9xxh5RnG3OfLRdcEBGx77BKpV0yZx4ryw6v6JildjMe_bf225O2B8ZGshAfltxwCNvTvahfWspTeNiYcLI62Cpc1hRVY5qaZENyTqR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23184ff86c.mp4?token=USnqjr9dXWjqD2i2nxEbr_9SGYY-vMM60T4cS7eOZ0fD6fgWiWw4DhuH8uTA8XH4OHgdXSjnenCPv_NXWLrp36YFcyk1EHryKm0AtUIj6nYlsx83OiS8-epuSMRMaV6plUXpp1U_3SL5MF__O7aKQRLk1e1m60_hoCzHqRLpC_jS5UDF91ulmqq_IxCwBucIkLGAUZIm6y0QjKyigE3LVCWOk8VuECPN5Y38gNfMYmwChk9xxh5RnG3OfLRdcEBGx77BKpV0yZx4ryw6v6JildjMe_bf225O2B8ZGshAfltxwCNvTvahfWspTeNiYcLI62Cpc1hRVY5qaZENyTqR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو الإسرائيلي:  خلال الليل والصباح، تم تفعيل الإنذارات في 4 جولات في عدة مستوطنات بالشمال: كريات شمونة، المطلة، وهذا الصباح أطلق حزب الله أيضًا صواريخ أعمق إلى منطقة ميرون.  صاروخ أصاب مباشرة المركز التجاري في كريات شمونة.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76408" target="_blank">📅 09:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇷🇺
الخارجية الروسية: تم استدعاء السفير الروسي لدى أرمينيا إلى موسكو لإجراء مشاورات بشأن خطوات القيادة الأرمينية نحو التقارب مع الاتحاد الأوروبي.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76407" target="_blank">📅 09:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22015f29c4.mp4?token=L5-vOE5PsQR6fcyJAe7TtIKE6D3dYhtbaU_jn7XqnjpgjnO0hpxgpqv-hx4VGaExCQ3kFSa3Jart4I_fzk8IHVZQGzUMgt7DDOs4QZbgTvf0b9gTPffWKZ4GwGnTs0q_u681phn3hHP5lnDuov8v9W2Q_PHIfJgyUr6h2y-wv1QXnH6QO7U7Sn6ERKQnhbim1J9g-zbwJxVssfNuJBvRB7LTk8AZjVRU4K33h2PFEOQ0WxNDJIeNBBmwTZ3bNY723qf_YzCfRlXx2DEgySxNcHxGjW_Ye78bU2TIeNQORB2PCj4wPDsPT3eUAMNThl8DaOAQCp1eSChfaHVjWqSNzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22015f29c4.mp4?token=L5-vOE5PsQR6fcyJAe7TtIKE6D3dYhtbaU_jn7XqnjpgjnO0hpxgpqv-hx4VGaExCQ3kFSa3Jart4I_fzk8IHVZQGzUMgt7DDOs4QZbgTvf0b9gTPffWKZ4GwGnTs0q_u681phn3hHP5lnDuov8v9W2Q_PHIfJgyUr6h2y-wv1QXnH6QO7U7Sn6ERKQnhbim1J9g-zbwJxVssfNuJBvRB7LTk8AZjVRU4K33h2PFEOQ0WxNDJIeNBBmwTZ3bNY723qf_YzCfRlXx2DEgySxNcHxGjW_Ye78bU2TIeNQORB2PCj4wPDsPT3eUAMNThl8DaOAQCp1eSChfaHVjWqSNzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
إذاعة جيش العدو الإسرائيلي:
خلال الليل والصباح، تم تفعيل الإنذارات في 4 جولات في عدة مستوطنات بالشمال: كريات شمونة، المطلة، وهذا الصباح أطلق حزب الله أيضًا صواريخ أعمق إلى منطقة ميرون.
صاروخ أصاب مباشرة المركز التجاري في كريات شمونة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/76406" target="_blank">📅 09:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
أبلغت القيادة المركزية الأمريكية (CENTCOM) البحارة والطيارين في المنطقة الواقعة شمال شبه جزيرة مسندم (عُمان) في مضيق هرمز بأنشطة عسكرية خطيرة وشيكة لمعالجة الألغام الإيرانية، وذلك وفقًا لإشعار صادر عن مركز عمليات التجارة البحرية في المملكة المتحدة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76405" target="_blank">📅 02:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f96f0fa6.mp4?token=e2x9mf7y9tGHhHGdMhBvTzHrbGax6ivoiqzeYT0I2OMVSeWYlhMA9QskLOtl-QoNQq_ZVSS0m__z8ioJ2eNNgMm80ls4_4SW0e9ZKyAr2iPduAyRlOAjNBuLETpSBwIGUtgBZ61XY5c88KjWrum6hegGtoga2-RugaE-0t8II8qf5agHAYpI0ZN08D7aImVNl4FSrySClsDZTTalxK09RKq0oRoIAsNG3PwQ0E0osAyyfmFRBAujSeaOOTDNDWsNjlwcL52Vlr9wP6rBHZkmlsofOUEB6a4dawWeNv_G97gK6O-WpD2vfY7Rgx2Eyutt-do7kWZd40p84R5Rmj4i3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f96f0fa6.mp4?token=e2x9mf7y9tGHhHGdMhBvTzHrbGax6ivoiqzeYT0I2OMVSeWYlhMA9QskLOtl-QoNQq_ZVSS0m__z8ioJ2eNNgMm80ls4_4SW0e9ZKyAr2iPduAyRlOAjNBuLETpSBwIGUtgBZ61XY5c88KjWrum6hegGtoga2-RugaE-0t8II8qf5agHAYpI0ZN08D7aImVNl4FSrySClsDZTTalxK09RKq0oRoIAsNG3PwQ0E0osAyyfmFRBAujSeaOOTDNDWsNjlwcL52Vlr9wP6rBHZkmlsofOUEB6a4dawWeNv_G97gK6O-WpD2vfY7Rgx2Eyutt-do7kWZd40p84R5Rmj4i3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇹🇷
العراق وتركيا يتفاوضان على اتفاقية نفط جديدة قبل انتهاء عقد خط جيهان
- تجري مفاوضات للتوصل إلى اتفاقية جديدة لخط أنابيب النفط بين البلدين قبل انتهاء الاتفاقية الحالية في يوليو المقبل
- مساعٍ عراقية لتعزيز السيطرة الاتحادية على صادرات النفط وتقليص أي ترتيبات موازية مع إقليم كردستان.
- تتمسك الحكومة العراقية بأن تكون جميع صادرات النفط عبر شركة تسويق النفط العراقية (سومو) والخزانة الاتحادية، مستندة إلى حكم التحكيم الدولي الذي صدر لصالحها ضد تركيا عام 2023 بشأن صادرات نفط الإقليم.
- في المقابل، تسعى تركيا إلى توسيع الاستفادة من خط الأنابيب الذي تبلغ طاقته نحو 1.5 مليون برميل يومياً، عبر ربطه مستقبلاً بحقول الجنوب ضمن مشروع “طريق التنمية”، الذي يهدف إلى تحويله إلى ممر متكامل للطاقة والتجارة.
- تراهن بغداد على مشروع خط البصرة–الحديثة باعتباره العمود الفقري لمنظومة التصدير الشمالية، مع إبقاء خيارات التصدير عبر سوريا والأردن مفتوحة لتعزيز مرونة الصادرات العراقية وتقليل الاعتماد على مسار واحد.
- يرجح مراقبون أن ينتهي الاتفاق الجديد بإعادة تشغيل ميناء جيهان التركي كممر اتحادي خاضع لإدارة بغداد، مع استمرار استخدام بنية إقليم كردستان التحتية دون منحها استقلالاً تجارياً أو سياسياً في ملف تصدير النفط</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/76404" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسؤول أمريكي يزعم: الجنرال الأمريكي دونوفان، رئيس القيادة الجنوبية، التقى يوم الجمعة بقادة عسكريين كبار من كوبا بالقرب من قاعدة البحرية الأمريكية في خليج غوانتانامو</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/76403" target="_blank">📅 00:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvWMhYQ5_5ebYWVc8MAs31Z2kcIqtcjLZDtxu3MT38DPCwWhHNFVpLHyBco8ONrNycbaspyBrYmxdmPd3V_cc2wL0gGAYd617uVSJJu2V9t9LnsHoi0yt76Zc9xbMta759Dt-ZzV8oVEW2ZRkIPxmJnGlPIoyXtsHeeGSf-V3mspWJ2eBhZMSOiwGyogf2ZlxhnQacaGgQC2gPLlaPRLy9vdPoPpP3WfbwQYt4ISxYnr3Iq9yset5ewWX7RnyGxpXsExUEYJHxvI_uBKAxxfqTXfRLOdxK_4LiaFPHTrzvbaV8m0Dm9BWALEWoE4N-lISv6MMuVS42AIAyGU5AeA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: أصدرت تعليماتي إلى وزارة التجارة لإجراء تنسيق مع الكونغرس من أجل نقل والسيطرة على كامل مركز كينيدي.
بشكل صادم، حكم قاض عينه باراك حسين أوباما، كريستوفر كوبر، بأن مركز كينيدي، الذي كان سيغلق في أوائل يوليو للتجديدات والبناء على نطاق واسع بسبب سنوات من الإهمال والاضمحلال وسوء الصيانة، والذي كان من المقرر أن تحوله إدارة ترامب إلى أفضل منشأة من نوعها، في أي مكان في العالم، لا يسمح له بالإغلاق لهذه التجديدات، والتي لن يكون من الممكن القيام بها بشكل صحيح دون مثل هذا الإغلاق.
بالإضافة إلى ذلك، حكم القاضي كوبر بأن مجلس الأمناء البالغ عدده 36 عضوا، الذين صوتوا بالإجماع لإضافة اسم "ترامب" إلى مركز كينيدي السابق، مما يجعله مركز ترامب كينيدي، ليس له الحق في القيام بمثل هذه الإضافة، والاسم،
خسر مركز كينيدي، على مر السنين، قبل مشاركتنا منذ فترة وجيزة، مئات الملايين من الدولارات - في بعض الحالات، بما في ذلك وظائف البناء السخيفة التي تم إنجازها، أكثر من 100 مليون دولار سنويا. لقد كنت فخورا جدا بالاستيلاء على مؤسسة خاسرة، وتطلعت إلى جعلها فائزا عظيما ومرموقا لواشنطن العاصمة، وبالفعل الولايات المتحدة الأمريكية. لسوء الحظ، يفضل القاضي كوبر واليسار الراديكالي رؤيته يموت بدلا من أن يحوله الرئيس ترامب إلى شيء يمكن للجميع أن يفخروا به، كما فعلت، في كثير من الحالات، طوال حياتي، ومؤخرا، مع جميع الإنشاءات والتجديدات و"الإصلاحات" التي أكملناها مع وزارة الداخلية على الشلالات والنوافير والآثار وغيرها من الأشياء الجميلة التي أعادناها إلى الحياة في مكان آمن ومأمون الآن، بعد جريمة تسجيل الأرقام القياسية، واشنطن العاصمة، والتي تزدهر مثل، ربما، لم يسبق لها مثيل
لذلك، استنادا إلى حقيقة أن الديمقراطيين اليساريين الراديكاليين يهتمون بمعارضة رئيسك المفضل، ME، أكثر من إنقاذ مركز الفنون الأدائية المحتضر، والذي يفقد جميعه تقريبا مبالغ كبيرة من المال في جميع أنحاء البلاد، سنعمل مع الكونغرس لنقل هذه المؤسسة الفاشلة إليهم حتى يتمكنوا من اتخاذ قرار بشأن ما يجب فعله بها.
قدم القاضي كوبر عرضا تقديميا من قبل كبار خبراء البناء والتشييد حول مدى خطورة المبنى من الناحية الهيكلية، مع العوارض المتعفنة، ومناطق وقوف السيارات المعرضة للانهيار، ومختلف مشاكل الحياة والسلامة الأخرى، بالإضافة إلى حقيقة أنه يحتاج أيضا إلى تجديد كبير، من وجهة نظر جمالية، لكنه لم يكن "متأرجحا"، وقال إنه يريد أن يظل المبنى مفتوحا بشكل لا يصدق، وبالتالي خطير. يجب أن يخجل القاضي كوبر من نفسه! لا يمكنني التورط في وضع يسمح فيه للخطر على الجمهور بالازدهار على مرأى من الجميع ومفتوح. ما لم أكن حرا في فعل ما أفعله بشكل أفضل من أي شخص آخر، وأعيد هذه المؤسسة، جسديا وماليا وفنيا، ليس لدي أي اهتمام بمواصلة ما يمكن أن يكون رحلة ميؤوس منها إلى "لا تهبط أبدا". لم يكن هناك أبدا رئيس للولايات المتحدة عومل بشكل غير عادل من قبل المحاكم مثلي، ولكن لا بأس، سأستمر في القيام بما يعتبر، عملا رائعا لشعب بلدنا الرائع. لقد أوعزت إلى وزارة التجارة باتخاذ جميع الترتيبات اللازمة مع الكونغرس للسماح بالنقل الكامل والكامل لهذه المؤسسة، ومنحهم مسؤولية تشغيلها وصيانتها وإدارتها. شكرا لك على اهتمامك بهذه المسألة! الرئيس دونالد جي. ترامب</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/76402" target="_blank">📅 00:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مسؤول أمريكي يزعم:
الجنرال الأمريكي دونوفان، رئيس القيادة الجنوبية، التقى يوم الجمعة بقادة عسكريين كبار من كوبا بالقرب من قاعدة البحرية الأمريكية في خليج غوانتانامو</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76401" target="_blank">📅 00:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">إن بي سي عن مسؤولين أمريكيين:
الجيش الأمريكي لم يؤكد أن إيران زرعت ألغاما في مضيق هرمز رغم عمليات البحث</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/76400" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارة الخزانة الأمريكية: فرض عقوبات جديدة لمكافحة الإرهاب تشمل أفرادا وكيانات في إيران</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/76399" target="_blank">📅 23:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fb52f44c.mp4?token=jqHlfFyAOH_0t6aCf3WObyUFH_ro_jbgIJ6BCBHrXd21wPuuTXMFmIOQGvNJ8leDw07hkleamNL6k9UrQi6LTYYYfgYVGKqlOiBzWKjpFbmimHoX5KwOpdgeeiz5XnewcLoGP2f_NM8EIphQoo2S3361taafCZDsQgj9p4BW7cd9DYY0vo1kvkNiuflFOmASw64zQKZA3lPIix9Tu5uL7OfAEvyideepr6STOSCJogFtYAU7Hm2vfE0Cszu0i41Fm1JGSPEJRp-hbyFOaK7_zxV5N93w-HlWVYLgcHoiTZFhfZbcLPQ1YNKTXavOcUJS9X1WwyTLoGRoisDAbb-fWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fb52f44c.mp4?token=jqHlfFyAOH_0t6aCf3WObyUFH_ro_jbgIJ6BCBHrXd21wPuuTXMFmIOQGvNJ8leDw07hkleamNL6k9UrQi6LTYYYfgYVGKqlOiBzWKjpFbmimHoX5KwOpdgeeiz5XnewcLoGP2f_NM8EIphQoo2S3361taafCZDsQgj9p4BW7cd9DYY0vo1kvkNiuflFOmASw64zQKZA3lPIix9Tu5uL7OfAEvyideepr6STOSCJogFtYAU7Hm2vfE0Cszu0i41Fm1JGSPEJRp-hbyFOaK7_zxV5N93w-HlWVYLgcHoiTZFhfZbcLPQ1YNKTXavOcUJS9X1WwyTLoGRoisDAbb-fWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من مدينة العامرية في العاصمة بغداد.. ازمة في توفر البانزين تضرب مختلف مدن العراق</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/76398" target="_blank">📅 23:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزير الخزانة الأمريكي: سيتم رفع الحصار المفروض على إيران تدريجيًا.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76397" target="_blank">📅 23:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزير الخزانة الأمريكي:
سيتم رفع الحصار المفروض على إيران تدريجيًا.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76396" target="_blank">📅 23:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">📰
مسؤول إداري رفيع لنيويورك تايمز:
اجتماع ترامب في غرفة العمليات استمر نحو ساعتين، لم يتخذ ترامب قرارًا بشأن اتفاقية جديدة مع إيران.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76395" target="_blank">📅 22:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏وزير الداخلية الأميركي يقول ان اجتماع ترامب قد يخرج بأخبار مهمة للغاية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/76394" target="_blank">📅 22:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76393">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfd30ea590.mp4?token=grbuSupyHZd8rkoX1CNB1rX9aPsQwy4OUv515w9udE4H2Wv-GMXaHELWJTRMFIpGQnLI1B20mH_HKm-Wri-WXroDJgCUH_qXEsYHjrZabTFEWOjIlRkdIhQ6AdmV5MfBKQs8pTQpEOPTMYrWti07LgAxBDfCUq3xayhuJ_S-gIyajQ4ncoBtJ2Kr84zhdKQR3YlVPD0l0MPfSHdXDmiVUDlTBBWFrE9ZV0vCdLLS5HZB6AgYitGwO0cW8TZJWzPDl64wIplwkAmAypwBDAkFvplvHSEiiGFip9m4SmfbwXJA7LSr7eY8NCKqjwDmfrQjIYcrRov00MzhWTEOK4zdnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfd30ea590.mp4?token=grbuSupyHZd8rkoX1CNB1rX9aPsQwy4OUv515w9udE4H2Wv-GMXaHELWJTRMFIpGQnLI1B20mH_HKm-Wri-WXroDJgCUH_qXEsYHjrZabTFEWOjIlRkdIhQ6AdmV5MfBKQs8pTQpEOPTMYrWti07LgAxBDfCUq3xayhuJ_S-gIyajQ4ncoBtJ2Kr84zhdKQR3YlVPD0l0MPfSHdXDmiVUDlTBBWFrE9ZV0vCdLLS5HZB6AgYitGwO0cW8TZJWzPDl64wIplwkAmAypwBDAkFvplvHSEiiGFip9m4SmfbwXJA7LSr7eY8NCKqjwDmfrQjIYcrRov00MzhWTEOK4zdnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الدفاعات الجوية الإيرانية اشتبكت مع اجسام معادية في سماء جزيرة قشم وتمكنت من استهدافها واسقاطها.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/76393" target="_blank">📅 21:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76392">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed32016f8e.mp4?token=lVED7byheq8da3yZnk4W6MEN7FHGi4kyUI2l_XdXanR0rsFGrlX7kuo7uzOyuiXxHsM-Y70giloSmgzJh0qJBLpZGK3gU27YNuIHCSiLP_bXiVVmrknsRs7vPJDRPP-_d4StbPkGCfNkBeS3Jog7ht8i3IKesNwFLjTtF9jcupdZMsSYz1MuH4t2nMrweuUN51t71vPfzKijRShpeBMJ4Sk-94h9oGAgXiEFNJRjfyGZpv0txFi1xyGs8176BM1tApalfY7DRSqa6282Oht7zbhNNkdn8TLeBD67C0YlQuyIJ4Tp5XnLbZnYOrx-eCvduFLThb4L1Ek9ZYxNXVAltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed32016f8e.mp4?token=lVED7byheq8da3yZnk4W6MEN7FHGi4kyUI2l_XdXanR0rsFGrlX7kuo7uzOyuiXxHsM-Y70giloSmgzJh0qJBLpZGK3gU27YNuIHCSiLP_bXiVVmrknsRs7vPJDRPP-_d4StbPkGCfNkBeS3Jog7ht8i3IKesNwFLjTtF9jcupdZMsSYz1MuH4t2nMrweuUN51t71vPfzKijRShpeBMJ4Sk-94h9oGAgXiEFNJRjfyGZpv0txFi1xyGs8176BM1tApalfY7DRSqa6282Oht7zbhNNkdn8TLeBD67C0YlQuyIJ4Tp5XnLbZnYOrx-eCvduFLThb4L1Ek9ZYxNXVAltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
تفعيل الدفاعات الجوية الإيرانية في جزيرة قشم جنوبي البلاد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76392" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76391">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
تفعيل الدفاعات الجوية الإيرانية في جزيرة قشم جنوبي البلاد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/76391" target="_blank">📅 21:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXIdCo8YPkOZ9WGD_Ygzr1dU-OvVyb1uvus7XgY0w0yoY5bLBl46xBHZJ85hUpH3iERjSAylWdDaSyf-rVuwggIe5wrN04JV5K9NLKeG6KH0RihIisIJsoV426-oQmHUrm386R9ciKzY5le4-1-fXEXHS1Yyx891youK4I1VqFYZZyFAxZqBrzSjKOc-FY88p438QmsFcwCFfdx1-_5a6gBsAuJLpYV3xv_Wmy2aLrnO-RskKvxHpHHss6Wy63h-wb-4Q8WCldrVR8Xx2b2ZHicvoI5rZRTiSHeArv_EKa81UTZy26d6mxEZyzpeCsKlyfbnkelxRIumcDlPh7FY0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76390" target="_blank">📅 21:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EV5xx8PuLi7nmD7uEOHvGuDBEXNI6MDLWKdL-zyRG5YOrEfMccggP9aU3a9smOImY28m3y-SBkJI_vVqDNFQJumrxdC15tIOBx4JfCTMvvmItBBr62XJHmjXapa2_WldN0_2TWRdWBYhsObF6Xwd-FQT992qYyxHqSD4SukmwT0bTkRCT2ZZWjzZpSjiE3LTOxT0P8RC1Sm9yMkVBuh6UKoduWzKc87BLi9vcoFhXM1rlIPOy6rhroLweUKGvYoYyhbDEmtzDPv5ogKO02PieG62ftihahTBWK1Biwp0c_qAzke3fWYL98qRGQ6sCtqUaqgBSfy0siaV4zVMBUJzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-jOEVU36MCXRj5A5kvIozxb4l08uXjaM038nnvR-F28mKy3gkoK9cMjukniIhRnynZnOe1OJ4RO6ZRRdE7NuC4ql_cD5oMJ1FelaWtiiisUdIr9sPMScfqee2sW7c8lqalL-W5LsiiM3XOapGFHnHgawQ1FECrCbwdVPkkW8-sqEeDhCooIv5lKmUkr8zT2Y98_WcBrlXzPPCyL5L0mkrD14YFgE7ZUjTZFVV5X6NPRxyTBRrfm9XB5ajvb48gxaaIjNz0s3agewPe6C8FCivEWR-U9psPuP1SENn8Ba7QN2v3KHxqO4tmkgjlPDHuKp8dlxALkwxR1ThLznGwOjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
رصد نايا..
طائرة تابعة لسلاح الجو الأمريكي من طراز E-11A BACN  تحلِّق فوق العراق، وتحديداً فوق صحراء الأنبار، وخاصة الطريق الذي يربط الرمادي والرطبة بالقرب من الحدود العراقية السورية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/76388" target="_blank">📅 21:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geBw6xDGQ69VRecPmfWs8xp7ENXGpyqnXbt8uR2VaHzxpYCuFqWzQTG8mT3b2_r3WT5YZRi93rgsdkuMx7-NOrUDcEtUjOZgPopxUmtZUoZUc5zg6bEFrmGIMtOP9wFtaF4CnvKinZfbPj7zhMCXEAACg2UfiVRkyH3iZtI7s_Oj1sQdMdIh9dH071lzKcGyPedtslnnqohAN4x5CuHysx-ViEQnLuGiOa2b4c9CXZ_ze6EklpTpKH4QO0dmF6UmrjwTPsnFVp5JCaHKJaojKLVyg2ifcN9xj7AQyI9k7MxbjlX1FzBo1fuayeR9rsJlPLQJXXXaFK3LLpsH7LyMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
دبابات ميركافا أخرى تابعة لجيش الإحتلال الصهيوني تصيبها وتحرقها صواريخ ومسيرات حزب الله في جنوب لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76387" target="_blank">📅 21:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546ca50588.mp4?token=iE9bCprOTRk90k6H1SRoxTPmoZSm6rofhKUMDZRwygCmuBn0PX3UcO258err0AdAn_kXT2zDTFBWe6ZSeupkbEs8WCneCcoJAcFXGLcr9owqmA5RTSIzbHNyfNUlJyuOwA6kwoUVfNLOoFnHQIqAd4qsayFwEUXnJcUS7E25iGIEWcM8pSbwfv5RyaTCg8r5eqYSs53vxHUJ6cS-kbnxvk0wWhKW4yTiXQij_NiBK_eiZcuJLyxcyIRJZmDTWgN-JuquDNIKB41rjRslRewFTCCwzb0nvzd-KsbQsCo1JaVBvJChSTOwWOF0YoG5ToSXZeF27c5Y7YYZ-raODs9eXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546ca50588.mp4?token=iE9bCprOTRk90k6H1SRoxTPmoZSm6rofhKUMDZRwygCmuBn0PX3UcO258err0AdAn_kXT2zDTFBWe6ZSeupkbEs8WCneCcoJAcFXGLcr9owqmA5RTSIzbHNyfNUlJyuOwA6kwoUVfNLOoFnHQIqAd4qsayFwEUXnJcUS7E25iGIEWcM8pSbwfv5RyaTCg8r5eqYSs53vxHUJ6cS-kbnxvk0wWhKW4yTiXQij_NiBK_eiZcuJLyxcyIRJZmDTWgN-JuquDNIKB41rjRslRewFTCCwzb0nvzd-KsbQsCo1JaVBvJChSTOwWOF0YoG5ToSXZeF27c5Y7YYZ-raODs9eXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
🌟
🏴‍☠️
دبابات وآليات الجيش الإسرائيلي تحترق في بلدة يحمر بجنوب لبنان بعد دكها بالصواريخ الموجهة والمسيرات الإنقضاضية من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76386" target="_blank">📅 20:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: لقد ودعنا لغة "ينبغي" منذ 47 عاماً؛ لا يمكن لأي من الأطراف الغربية أن تتحدث بلغة "ينبغي" عند الحديث عن الجمهورية الإسلامية الإيرانية.  يجب أن نرى مصداقية رفع الحصار البحري أهو حقيقي أم مجرد تصريحات إعلامية.  نركز في هذه المرحلة على إنهاء…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76385" target="_blank">📅 20:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين: الاتفاق مع إيران سيتضمن وقفا لإطلاق النار في لبنان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76384" target="_blank">📅 20:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418eb7c1ed.mp4?token=P3nxVKPKz9FsjKtnTqm8LRmcgkyozfsnjABr3DfpQoxEQR6brJoqOhwR7oJB5ylIHl9kvPDYitaYNjoT7vpc0JWcbChznCezOeGh9gHIn0HquWUyiSoVGTrxDMMluludiBaHz6oaHKQCCobBD7J3iq0-TrxWK274Vx4IVkn4Ba4ioEGY7Ln12-Tp4hsx8FtrweHZPPMp3OdXlvIH080Xe9AiuxO9rNiQGavtx0Lzs2oNQyynoAzwhQkxLt4o1LmXCphMG0af_cDHXawfC6Gx-EaXHgWU750JYqu8s30ZtewjfGH3hCCx_dpxwFye4Dbkt6AKGvH_XTa0CQQJyt_dDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418eb7c1ed.mp4?token=P3nxVKPKz9FsjKtnTqm8LRmcgkyozfsnjABr3DfpQoxEQR6brJoqOhwR7oJB5ylIHl9kvPDYitaYNjoT7vpc0JWcbChznCezOeGh9gHIn0HquWUyiSoVGTrxDMMluludiBaHz6oaHKQCCobBD7J3iq0-TrxWK274Vx4IVkn4Ba4ioEGY7Ln12-Tp4hsx8FtrweHZPPMp3OdXlvIH080Xe9AiuxO9rNiQGavtx0Lzs2oNQyynoAzwhQkxLt4o1LmXCphMG0af_cDHXawfC6Gx-EaXHgWU750JYqu8s30ZtewjfGH3hCCx_dpxwFye4Dbkt6AKGvH_XTa0CQQJyt_dDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا في بلدتي يحمر الشقيف وتبّين بجنوب لبنان بواسطة صواريخ موجه من قبل حزب الله.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/76383" target="_blank">📅 20:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwM06i-lIlRh5O1LCEfIV6ZTPuqvA3TTqndZt7zy1BVC2sdNhwKpOnFBnaMY6rX0J9OyQUQkZKntOK2oqzkJ23SgNs3EDt-s3uiLALFUbfLEL0eU-LMEBwcNQxowaO1MgaaPWHgjOZh4RfBQIuTb9Ef4U2PJecwNcEqhqBnqMmi3-x-CCC6ohH3ziOPb0J26Jsd_8SCYn1lPoQV_THqYfOJWLF0IrziYs1HwtKMrX4SRHqRHm_VNycFUs5tB0BOm_8vPA5xfZcBJ_2xvOP3khxC2GVGa8W_4LW8-f8swu05LdgynKZzP_f8eV1PbCo6UnXPRjfUfV9lHcebfFqOv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
بين مايتحدث ترامب عن الحصار الفولاذي..
تانكر تركرز:
شهدت الأيام الأخيرة قيام ناقلات النفط بتحميل النفط الخام ومختلف المنتجات المكررة على طول الساحل الإيراني وفي المنشآت البحرية. واليوم (29) مايو /أيار (2026) ، نشهد تحميل ناقلة نفط عملاقة (VLCC) مليوني برميل من النفط الخام.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76382" target="_blank">📅 20:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: حتى هذه اللحظة، لم يتم التوصل إلى تفاهم نهائي بين إيران والولايات المتحدة.  ينبغي النظر إلى تصريحات دونالد ترامب، رئيس الحكومة الأمريكية الإرهابية، بشأن رفع الحصار البحري عن إيران بعين الشك، وبالطبع، إذا تم تنفيذ ذلك فعلياً، فلن يعني ذلك…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76381" target="_blank">📅 19:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الإسرائيلي في بلدة يحمر الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76380" target="_blank">📅 19:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
مصدر إيراني مطلع: إن تصريحات ترامب غير صحيحة.  يُعدّ أهمّ بنود الاتفاق هو الدفع الفوريّ لـ 12 مليار دولار من الأصول الإيرانية المُجمّدة، ووقف إطلاق النار الكامل في لبنان، وهو ما لم يذكره ترامب. وبحسب نصّ الاتفاق، يجب دفع هذا المبلغ فورًا، ولن تدخل إيران…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76379" target="_blank">📅 19:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇷🇺
بوتين:
الوضع في ساحة المعركة مع أوكرانيا يُشير إلى أن الحرب تقترب من نهايتها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76378" target="_blank">📅 19:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d5158ec0.mp4?token=fPEUAv3plPT7HHAhRtSxEBJRr1t7zGClNpEvRbJw4MN55Dp2sarS3VGsBlAl_ulgWoDIo51nrewlEwtRZCQLWuocBl611VctZxv_xgGnA9KS3OSxTtQrdzHKkBcvBKDkhexCkhap18P1hL-b9fiKD-Od5eL4qAKJ7YEKr_dAhsRvJYRITdt6vCxMr8feogGmaR6d2T-F8V2F8MbttO2H-XwmBxZRPiDttaIkuQeAaqsVbeCqufox5pLFD4_2xxwGU4GpB7SPtyjvySiney3syjQ-qy1g1leZFNE8YjvZWySnQJnegFrAV756o2upJzwLmrysQhVoyMgzG-Ja1MIwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d5158ec0.mp4?token=fPEUAv3plPT7HHAhRtSxEBJRr1t7zGClNpEvRbJw4MN55Dp2sarS3VGsBlAl_ulgWoDIo51nrewlEwtRZCQLWuocBl611VctZxv_xgGnA9KS3OSxTtQrdzHKkBcvBKDkhexCkhap18P1hL-b9fiKD-Od5eL4qAKJ7YEKr_dAhsRvJYRITdt6vCxMr8feogGmaR6d2T-F8V2F8MbttO2H-XwmBxZRPiDttaIkuQeAaqsVbeCqufox5pLFD4_2xxwGU4GpB7SPtyjvySiney3syjQ-qy1g1leZFNE8YjvZWySnQJnegFrAV756o2upJzwLmrysQhVoyMgzG-Ja1MIwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
وسط غضب شعبي في محافظة ديرالزور.. مواطن سوري يهاجم موكب الجولاني.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/76377" target="_blank">📅 19:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
ترامب: يجب على إيران أن توافق على عدم امتلاكها سلاحًا نوويًا أو قنبلة نووية. يجب فتح مضيق هرمز فورًا، دون رسوم، أمام حركة الملاحة البحرية غير المقيدة في كلا الاتجاهين. سيتم إزالة جميع الألغام المائية (القنابل)، إن وجدت (لقد أزلنا، عن طريق التفجير، العديد…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/76376" target="_blank">📅 19:15 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
