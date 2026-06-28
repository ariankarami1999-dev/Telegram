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
<img src="https://cdn4.telesco.pe/file/Ur25_Q7cGH1fH98uesEHtWqvITwn_ZSFBmx4flXlOVQKI2XknxuF1lt2pByp4xL15ZQgxy8nyXxxmZnEk7qDBnK4BCzHKSQanFBubfzZKtem_PTrq9weTvuehU2DDVZIVQ2dQqxZy-TtTZSkRLBVaR0qJp5BDx---nnu7T04MNzhSABhtD-0voz_K2tsL-LFk1UG6PtVdgM864P66QOvtCSi2-f9_Gc9RQTG5BEIvG0g_G03VzFS4bIgPqviVwhGnjueBPAtBrlJs75D3LlASRVVQKx5sk495F9V7z0i6e8FiAwLYlfVc7tGQDwOS9UxFEobRy9K1FK-B1p1JtNFAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 03:29:05</div>
<hr>

<div class="tg-post" id="msg-80114">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a323ca8867.mp4?token=kHgTciw6h3kwFzotYsTfjJQvCnjd4CeYblSNi32JgU8JiXZQrJZnBLHeeqn_tq1i_a7vHqLvAsZncTTw-zyte2horT4iYfeUwCOvq4xj6t2XvwwcyBKE09Rr3xAshV0OK33FLZoDsVruYOQ4gs24mt5e8fsKUp0Gg-60Onux6BSQxlW0NK4j0ocfMnLMNzfbuv2HoMWgRU2sVV_YLxh1JL0-AGRJfBR6liQbXRD2rlOPpGf4c4hjjVCb-Z-PhYbJP3s7PZckRV5iVS5ldPhDCVFuiE4NxqMloL_mR10Ymdow4a8r9hRpDszPG56GlBXLY9VnPqNqVyhOVYJGD7ao6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a323ca8867.mp4?token=kHgTciw6h3kwFzotYsTfjJQvCnjd4CeYblSNi32JgU8JiXZQrJZnBLHeeqn_tq1i_a7vHqLvAsZncTTw-zyte2horT4iYfeUwCOvq4xj6t2XvwwcyBKE09Rr3xAshV0OK33FLZoDsVruYOQ4gs24mt5e8fsKUp0Gg-60Onux6BSQxlW0NK4j0ocfMnLMNzfbuv2HoMWgRU2sVV_YLxh1JL0-AGRJfBR6liQbXRD2rlOPpGf4c4hjjVCb-Z-PhYbJP3s7PZckRV5iVS5ldPhDCVFuiE4NxqMloL_mR10Ymdow4a8r9hRpDszPG56GlBXLY9VnPqNqVyhOVYJGD7ao6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر امني لنايا: إن غلق المنطقة الخضراء في العاصمة بغداد يأتي لغرض تنفيذ ممارسة أمنية، ولا يرتبط بأي طارئ أو حدث استثنائي.</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/naya_foriraq/80114" target="_blank">📅 03:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80113">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجارات وصافرات الإنذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/naya_foriraq/80113" target="_blank">📅 03:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
قسم بالله
🔻
قسم بخدا
🔻
We swear by Allah
🔻
مونتاج نايا:
#شاركها</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/naya_foriraq/80111" target="_blank">📅 03:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
مصدر امني لنايا:
إن غلق المنطقة الخضراء في العاصمة بغداد يأتي لغرض تنفيذ ممارسة أمنية، ولا يرتبط بأي طارئ أو حدث استثنائي.</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/naya_foriraq/80110" target="_blank">📅 02:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egIMNQWpVswlepa9IWUNBWixAki5ZnBEgjAWu9GPXxzk9Gdh9HxLllKESxPw23gJceu4sInEa1FblYdCOwf9JFKMabtEo0RNPaten54VDGF8ADVi-cQY_VZt9Qvlg6lPjMUa9DtYPmDyV98Fep313sIdR1ftcwbVEaLvvQsNwmFB-1efAwiTP-_WEW8ir3M5GSReDRi1NDwIGoIBoIk5LILlryLIxqXZ9xIN7BQw-Wn9Y9sEBIH8FJFJDamtFZp0YjBIr4gTVumIKukZd4C0jIBWYkDBT_DWPV_7HSO5pH291cJZXkgAt0drpkomsP9ZEob3hGAIEOj4uAxOx8qZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامب
:
«شنت طائرات الولايات المتحدة غارات على مواقع تخزين الصواريخ والطائرات المسيّرة الإيرانية، ومواقع الرادار الساحلية، لانتهاكها اتفاق وقف إطلاق النار، مرة أخرى! من المحتمل جدًا ألا يتعلموا أبدًا! قد يأتي وقت نعجز فيه عن التحلي بالمنطق، وسنُجبر على إكمال المهمة التي بدأناها بنجاح عسكريًا. إذا حدث ذلك، فلن تبقى جمهورية إيران الإسلامية موجودة! الرئيس دونالد ترامب»</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/80109" target="_blank">📅 02:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1-Wc7bNYz29MU7UXuR8Mfmq2Ikl53Ai9RCfsXaUm8QtVY0H_uxHowaTE_AO-QXDYmAxpVg1Zj6NRdclpL8p-hn5qBbjQm6bW1IrGF9vGxOafSy7_GwWslQ57XhilGavv7w9Ahma1jebIJ2EH283e59g_6gCXuLBMFR2Uu9J5XwlnNGJXJ9NZQFEWEXhDL52YFlKzEsJ2AXN6Jsz4r0qdQc9wgxSwQEbh8Hz3-QX-MRnjzbeBkt0TsKsPp4TIoB7gt06uwzVjFaMKHPpfWrj35LR_FEaXR8woycAUPE0OZSC_3f-w5uVgsxPXgFmBjVBaRmRNmVZ7ikI139Lq65IOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏نشاط مكثف لسلاح الجو الأمريكي في الشرق الأوسط حالياً.
‏يوجد حاليًا حوالي 13 ناقلة وقود تحلق فوق عدة دول في المنطقة، وخاصة فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80108" target="_blank">📅 02:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
مسؤول أمريكي: أن الضربات الأمريكية على إيران "اكتملت".</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80107" target="_blank">📅 02:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
دوي انفجارات في ميناء لنگه وميناء كنگ جنوبي إيران</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80106" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
مسؤول اميركي: ردت إيران الليلة الماضية بشن هجمات على القوات الأمريكية في البحرين. وأسقطت القوات الأمريكية والبحرينية تسع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه، دون وقوع أضرار أو إصابات.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80105" target="_blank">📅 01:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
مسؤول اميركي: الجيش الأمريكي ينفذ جولة جديدة من الغارات الجوية على إيران الآن، رداً على قيام الحرس الثوري الإيراني باستهداف سفينة في مضيق هرمز في وقت سابق من اليوم. الضربة الأمريكية الحالية أكبر من التي وقعت الليلة الماضية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80104" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
مجددا سماع دوي إنفجارات في سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80103" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80102" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80101" target="_blank">📅 01:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80100" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewlbXsMlP6IwUlr_4xH72hP1mM4Bc_ZhJMTX7zZhjc7D4XWnRol8f00cyU_66c9_cAJCNfqjXf9ZNg5yT6AIYilLZheZU_O81lcyQ84oXlbkkPGZ72jih5xf7XzzO0y01GqZV53A3WvAMpXGlwLNo0mrtk8yjvWZsxJ4ixgFL-QD3Dyj9ih2cTZ8SPKZhgSedLu_KU-QFIhUTm04ugqTTGf2d_x8USjfD997VMjmVYhsg35zRGrTvxoH_GMtKfrprU3CP9qCiOwZLexa_eFVLv1eVUG5y3Y7CXrq0P1O5aDFYew491vjNXyTinTOt1e5PKxcjxIju2gL9MLPcRtplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اختارت الولايات المتحدة ناقلة نفط للتحقق مما إذا كان ممرها الملاحي في المياه العمانية لا يزال "آمناً".  كبش فداء
😂</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80099" target="_blank">📅 01:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
غارات تستهدف برج اتصالات في قرية طاهروي بمحافظة سيريك.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80098" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80097" target="_blank">📅 01:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80096" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇯🇵
زلزال بقوة 5.6 ريختر يضرب اليابان وأصدر علماء الزلازل تحذيراً من تسونامي.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80095" target="_blank">📅 00:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjrhFZWHvAyvGIBzN-O_VZ6--rNchViLYXVI4pq2XjYMwgQj3KAwonaIUzQQ_byYpe4UqhaWu9XTNQCYbn2Gx8f4Yj2hSeTWHAdRaIyjX9n479AdBp6p1vC99V8pfUgrJPH2c7wNjdu2-hwwpgHNMicJcLFqrmc24tGhEx9duWTsaysS5UAhAqChjjCKh2mr9s6c_9eGlpvZpld23HONB5FzAYPK63-6RnmAQOIGdAKu3RCEvXlnx77LpaTR8A85aQLiiFOqSDjMQRpv5cf2TGS1dDZp1dotLLOfi6Z0RZvpLHzjsaNvTzD9CR2j4fhowPtSSi--3C19_CNpogNy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عُثر على جثة أحد عناصر قوات البيشمركة التابعة لحزب حرية كردستان (PKK) ويُدعى سوران محمد زاده داخل أحد الفنادق في مدينة أربيل.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80094" target="_blank">📅 23:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQl0Ec32BeV1aAB2vCJdcGmjkqGFIt1PrizfwC07B161zz-JOO14Crn9lU0_LGt8NxKwMphmKqGgwWcj9Q7bOGNBVmgAuKj2VQbSYViga1Ev9cibf15AcQbeZK3ykybJ-zpXKLzM4oLlciIMHj4n-bKoFUpjMsnsr-LYZtInckBunvzDwZcmBAPY6_CzPuJE7hMGz8WekUTMY4dhqY9o9NtlonfYfLDBDFsOJ9tZjt4K4Wb-LrhyVBVBPHgcBwRuN518Sy4lZuJC9aEQ-w6rPWxc4dCv9JRULuSGPJ0SrM4qaMJnt3qBQGO63rfa2nh2AzR56w_ABceEkZEtyC-nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اختارت الولايات المتحدة ناقلة نفط للتحقق مما إذا كان ممرها الملاحي في المياه العمانية لا يزال "آمناً".
كبش فداء
😂</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80093" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
‏زلزال بقوة 5.6 يضرب سواحل أراغوا في فنزويلا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80092" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تحت عنوان: "قوموا لله"
🔻
تعلن الفعاليات الشعبية والوطنية العراقية إطلاق الوسم الخاص بتشييع السيد القائد الشهيد علي الخامنئي على مختلف منصات التواصل الاجتماعي وذلك بالتزامن مع قرب وصول جثمان الشهيد في دعوةٍ واسعة للمشاركة في التفاعل وإحياء هذه المناسبة عبر الفضاء الإلكتروني.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80091" target="_blank">📅 22:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtgE_wX3mHh2VJAUDKLvz2mggDzhssABmRmSTdBmk2MJ8bOfz_UA4ZNqgOBJDYHc2S1jPkb-YeSkrm0BfkY_dnL9AUoGX7m9-NM6Zcy0U_h3QbKdh_2Ab7pIPNBV-PdtG44-EuELpnAsY0H0nh-dAcXbZeahtfOwjY3TW2KuFYvpbC3JVbnmFQxQg97GiO9F3gb2U3bNu-5nxWisZqGI11LVgtQ_qxKtyX3xDJ_bIOYkH3PVkO8Vc9I2oix_VA1qkWOn83SsMHa-3HEtFxzpQZR4Y3tV7qb0ttyj1hI2J2gi7I3gYaxl52Hr9Gead2mCoYyJrb0KYRONtF1ly6TH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ينشر:
حمل العالم ثكيل
😆</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80090" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇷
🇮🇶
‏
الخارجية الإيرانية:
عراقجي يتوجه إلى العراق غدا</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80089" target="_blank">📅 22:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇫🇷
‏الإسعاف الفرنسي: 109 حالات وفاة في مدينة باريس لوحدها خلال 24 ساعة الماضية بسبب موجة الحر.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80088" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🌟
‏نتنياهو:  أشكر حكومة لبنان على ما أظهرته من شجاعة.  توصلنا لإطار تفاهمات يؤهلنا لإنهاء الصراع مع لبنان.   الاتفاق مع لبنان ضربة لإيران ومحورها.  إسرائيل ولبنان اتفقا على منطقتين أمنيتين لتجربة العمل على نزع سلاح حزب الله.   لن نترك المنطقة الأمنية في لبنان…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80087" target="_blank">📅 21:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dbc6b86e.mp4?token=B0I5dfn3uNBbNqHNZgXJyzTNqRJeTB7zpoN6Xae3CrVKb5RA9wyIO6JhT8y0CMBJ8wWb5cc21-0lOfwfj3pT4IT37IyIP2CG0f2oBtKLYny1gIs1v-CV9ugJ9wiqY0Lum8BO_fWO2z2scI4nd4gBXiqfwd5VAuo9BpvQng_RKcVluXL8u5_OaUl3fBBx_n0L8JeUgCanJTdvU9_91JZLy1O021Vy2kXnhGT7wzXyDoqHwNG7AFZp1Cfybdy8foX7R-gNSseeB0J68QmAbHmpZl-3Raripksnwd95On5IhCNY4AkqYk7E3F1RWsq7D1mf5GV3w5fHNoEtDSfithvbUA2iigB8L2qBl4RmraWS4lGFWhN82AMfUQMe5-feu0Eiq1grLZAxBseqvfHQx_Lr63VUjmHcb9q3X2WcSJFz3ypKRekonPR6enXHspNbURVvmIifpW7oMWIjXh_0tJtrN3pSVfzbHoZkSQJA-tYyU2F1fomXrgYABm8ZpjQ1KPwLWZqNkxlq-Np9Rb06hfzSTFIiBeQTImVg0yQH7FbnkP5LcSlImRwN7Q8ZGdPkERGNqzv4G-W3UMWy-LeTxMw3MDZTmYlMWfDPh3Y2JtKi_nfWqyAznrpmvBrBK7puaAxCM-s2dsse9ts9MOG3kuk5K8WN7QJDtAXhZlLFTNfZJeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dbc6b86e.mp4?token=B0I5dfn3uNBbNqHNZgXJyzTNqRJeTB7zpoN6Xae3CrVKb5RA9wyIO6JhT8y0CMBJ8wWb5cc21-0lOfwfj3pT4IT37IyIP2CG0f2oBtKLYny1gIs1v-CV9ugJ9wiqY0Lum8BO_fWO2z2scI4nd4gBXiqfwd5VAuo9BpvQng_RKcVluXL8u5_OaUl3fBBx_n0L8JeUgCanJTdvU9_91JZLy1O021Vy2kXnhGT7wzXyDoqHwNG7AFZp1Cfybdy8foX7R-gNSseeB0J68QmAbHmpZl-3Raripksnwd95On5IhCNY4AkqYk7E3F1RWsq7D1mf5GV3w5fHNoEtDSfithvbUA2iigB8L2qBl4RmraWS4lGFWhN82AMfUQMe5-feu0Eiq1grLZAxBseqvfHQx_Lr63VUjmHcb9q3X2WcSJFz3ypKRekonPR6enXHspNbURVvmIifpW7oMWIjXh_0tJtrN3pSVfzbHoZkSQJA-tYyU2F1fomXrgYABm8ZpjQ1KPwLWZqNkxlq-Np9Rb06hfzSTFIiBeQTImVg0yQH7FbnkP5LcSlImRwN7Q8ZGdPkERGNqzv4G-W3UMWy-LeTxMw3MDZTmYlMWfDPh3Y2JtKi_nfWqyAznrpmvBrBK7puaAxCM-s2dsse9ts9MOG3kuk5K8WN7QJDtAXhZlLFTNfZJeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏نتنياهو:  أشكر حكومة لبنان على ما أظهرته من شجاعة.  توصلنا لإطار تفاهمات يؤهلنا لإنهاء الصراع مع لبنان.   الاتفاق مع لبنان ضربة لإيران ومحورها.  إسرائيل ولبنان اتفقا على منطقتين أمنيتين لتجربة العمل على نزع سلاح حزب الله.   لن نترك المنطقة الأمنية في لبنان…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80086" target="_blank">📅 21:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6b672cd7.mp4?token=Q_8Fx7kmyQTapSqYPY5hbg1aBrgimVS_yCL6HjOh-UKuq6Yk5pz_IUngUGjnKi6rJOtAIcJ4Swz2Tg252Sl5lGmo24G56-pN8ZgQXFsPJ6kr9jH8wFPTJ3-Q25sW35SOKt2u3x7Jr8DgtPj7cDIpqCqyBeKaXWNLltTVL1orKeW6NCThhIqmYu8_IcZDoK8q34ORVqHKhsm-wkGA918szeY3a3y83dvp2khn_BAVhNaO5f5eFbjrHBIfj-oexIobD76pbYpJbNyCkIZZtSwVG5cJU50uYQ60B_9Vz6MGiUauUczUdSsKoaZReLCcbV7qDdFr0HJBrbHxFYvZdXGSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6b672cd7.mp4?token=Q_8Fx7kmyQTapSqYPY5hbg1aBrgimVS_yCL6HjOh-UKuq6Yk5pz_IUngUGjnKi6rJOtAIcJ4Swz2Tg252Sl5lGmo24G56-pN8ZgQXFsPJ6kr9jH8wFPTJ3-Q25sW35SOKt2u3x7Jr8DgtPj7cDIpqCqyBeKaXWNLltTVL1orKeW6NCThhIqmYu8_IcZDoK8q34ORVqHKhsm-wkGA918szeY3a3y83dvp2khn_BAVhNaO5f5eFbjrHBIfj-oexIobD76pbYpJbNyCkIZZtSwVG5cJU50uYQ60B_9Vz6MGiUauUczUdSsKoaZReLCcbV7qDdFr0HJBrbHxFYvZdXGSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
نتنياهو:
أشكر حكومة لبنان على ما أظهرته من شجاعة.
توصلنا لإطار تفاهمات يؤهلنا لإنهاء الصراع مع لبنان.
الاتفاق مع لبنان ضربة لإيران ومحورها.
إسرائيل ولبنان اتفقا على منطقتين أمنيتين لتجربة العمل على نزع سلاح حزب الله.
لن نترك المنطقة الأمنية في لبنان إلا بعد التأكد من نزع السلاح.
‏ندمر البنية التحتية العسكرية في المنطقة الأمنية بلبنان ولم ننته بعد.
الولايات المتحدة ولبنان وافقا على بقائنا في المنطقة الأمنية بجنوب لبنان.
شددت لقواتنا على حرية الحركة لصد أي تهديد في لبنان.
عارضت بشدة أي محاولة لفرض انسحاب علينا والآن الولايات المتحدة ولبنان يقولان لإيران إن هذا ليس شأنها.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80085" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
المكتب السياسي لحركة "أمل" اللبنانية: نؤكد موقفنا الرافض للمفاوضات المباشرة والاتفاق جاء غير متوازن ويكرس في معظم بنوده وقائع لمصلحة العدو على حساب المصلحة الوطنية وينطوي على مخاطر سياسية وسيادية ولا يمكن القبول به.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80084" target="_blank">📅 21:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-wO13-LSKfNufwcgJ-C9CkN4Hd_hVgrI2vHODKA5QCHTd_PYFBtO3oH07XcnhLVu7yW8hjpNCohgKWZSht-5x2F3erPiwxQKnZQZVJr3bOUIpE2TU0dRdnnTk0NrT9tLEs02HggEUKTTfp-0OcURW_acbJf7bkmXLv64a6BedsVUp6nIl--cRxiCH7fjJZTchK7wJLFej0QqCmqnG1YRss8C09lzg3JHfvd_aNrk5htPH4lY0WJK-Tkx-VXg3he1Gn233fmIdcVy8zeNk2p86GukK8gmEYU8C1vARTZ6Kj8QQHOE99j4g0zQzsTJAf3s6yNpYPXYr0u9BOb1-81pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
السيد مقتدى الصدر:
إلى هنا ولاينبغي السكوت عن الأداء المخجل للمنتخب العراقي في كأس العالم.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80083" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🌟
الإمارات تنعى جندي قتل بظروف غامضة.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80082" target="_blank">📅 19:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🌟
وزير الحرب الإسرائيلي:
إذا حاولت إيران الهجوم لمنع تنفيذ الاتفاق مع لبنان، سنتصرف بقوة كبيرة.
‏لن ننسحب من لبنان بما في ذلك مرتفعات الشقيف.
‏سنحافظ على حرية عمل قواتنا في جنوب لبنان.
‏الاتفاق مع لبنان يرسم لأول مرة واقعا جديدا أكثر أمنا لحدودنا الشمالية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80081" target="_blank">📅 19:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇱🇧
بيان سماحة الأمين العام لحزب الله الشيخ نعيم قاسم حول اتفاقية العار الإطار بين النظام اللبناني وكيان العدو الصهيوني:  1- أين أمانة السلطة اللبنانية ومسؤوليتها تجاه شعبها وحماية سيادة لبنان، والتي لم يعطها الوصي الأميركي وقف إطلاق النار، وعندما جاءها من محادثات…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80080" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">تشييع الولي
#قوموا_لله
#باید_برخاست
@
in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80079" target="_blank">📅 19:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn13aZGrJWj_KW5oj4aDwvvQoJuo1y0RIFsZpUfm390Lcvx1MXmjvwbHMRzjS0eEeiiJ8Ww77EdRQQ8_MxzM2B9voxEd9QfvV6n7GJhfDV3LKoEUk_WqQk6tGfKbhflw_bV4COhKCDB8hVzqn8YGlHAg3o0dYvYkMAoiovSZdm5SgxDKz6_O5bRcqUweYngp6KAmR5_bn8P9egxYHU73E9NPyZjr7iSUmW1ddsuoHb__UOeUT7HPKBETqP49RdaZ2-247vVzqcILghO-m052e7R5hLw4X62P_8_i0MRSyO2wZ8EBUJw_lrYFRcHv_Td7x9LAjLdoHpCK7nEK4XPubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
غارات للعدو الصهيوني على النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80078" target="_blank">📅 19:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c051e16298.mp4?token=Qaz8AEIUAyctp6fv4lceiKmGTXI6gfavnkDsEPR38LUOjK0RqGv9IjhM18CdrT4rkB88N0qkGcXNvZvWZ9xjHUT36B9_7Bxqeu75kUgNWZzipO92GJ3rA1Sact7ECp8W7tVhmUVU2IO8OESYGvfGX9Nqfn_DxWlabVmeOv3DsIHBrvIT-2xq5TcriN_wqozeImUnIvjYOBLVG5uceIjIcy_f_BknAoDwwlAN6jKC0EFafZEsY0jdZ4ZXtQrIo3Te14fAzWz-z9tPkph4swE5lmOk85EL0e8_lCuHDPcVUm0uFAp2XducXFYsG-JIvrQzgrM6UBoeWTy0pHz-_Dx_0i38DGmGZvV6OCN8dagLYYtiZFWLNznjPFtD45yZhfSTTEr8PLkxpnlevkdklH5Xx2q9lYcFgRpoINcjS2YzvLQZzU1KOkHw5ST-mXeRUEths0NeD7ZJ8Yi7I4RxEVMdxCHDsjVkztO85I2gSn7pjRscNBDAWgEUFNytnw9Mv4fr6HqgExr92QaqWp7Na7IniDX2fHixVsUmDpIsuCVnGTwjbaeQLG0umuasTkN1f287SWbIuSmqwIwCfgGlAZB3yYPqRO9b_4QB1QJ33e2Q-hbq18uY4QnBOmwlTCpkZTAfv7qGyab1k39M-nNGpAHKrL7UcDXdh7dhywJQDsh5Km8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c051e16298.mp4?token=Qaz8AEIUAyctp6fv4lceiKmGTXI6gfavnkDsEPR38LUOjK0RqGv9IjhM18CdrT4rkB88N0qkGcXNvZvWZ9xjHUT36B9_7Bxqeu75kUgNWZzipO92GJ3rA1Sact7ECp8W7tVhmUVU2IO8OESYGvfGX9Nqfn_DxWlabVmeOv3DsIHBrvIT-2xq5TcriN_wqozeImUnIvjYOBLVG5uceIjIcy_f_BknAoDwwlAN6jKC0EFafZEsY0jdZ4ZXtQrIo3Te14fAzWz-z9tPkph4swE5lmOk85EL0e8_lCuHDPcVUm0uFAp2XducXFYsG-JIvrQzgrM6UBoeWTy0pHz-_Dx_0i38DGmGZvV6OCN8dagLYYtiZFWLNznjPFtD45yZhfSTTEr8PLkxpnlevkdklH5Xx2q9lYcFgRpoINcjS2YzvLQZzU1KOkHw5ST-mXeRUEths0NeD7ZJ8Yi7I4RxEVMdxCHDsjVkztO85I2gSn7pjRscNBDAWgEUFNytnw9Mv4fr6HqgExr92QaqWp7Na7IniDX2fHixVsUmDpIsuCVnGTwjbaeQLG0umuasTkN1f287SWbIuSmqwIwCfgGlAZB3yYPqRO9b_4QB1QJ33e2Q-hbq18uY4QnBOmwlTCpkZTAfv7qGyab1k39M-nNGpAHKrL7UcDXdh7dhywJQDsh5Km8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
توثيق جديد يظهر لحظة دك موقع في البحرين بالصواريخ البالستية الإيرانية وفشل منظومة الباتريوت الدفاعية الأمريكية خلال أيام حرب رمضان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80077" target="_blank">📅 18:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCsOoysboZN9rvufzxfvWDtQQ3u-K-mL39ToIRksLhpgUtQuhgqMPkIzTujTrYZXyoLnEoKbgxp8Wso0egyYMZU3cZK2gSYvB94xb8bw6ktkq4c72d1i_73iQ590JJb69dG4-FwQTUMImjirlYMHg8Brq1qwPm3CB4iLv-BcmUlaZl1YytuA2UrFbPoomxAmoO7s_oTbYI12w1JpMsV7ybNpodfh312dcd-EcpbrkKaNsA6DQUeIujN8dAlD9fKvKjmQI49EWFzR6_x4x45vhmRqhcEbSvxh8ykPVdwfK0IzpDrfKwOmAavA1sRE8XpHZ3VbeIoHwHo2Nf9rMPXLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
غارات للعدو الصهيوني على النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80076" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80075">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b3f81696c.mp4?token=hzNpviGv4S2r378vFS2BpnTmIKhdslNJ-vOXW_4Z1jq4ku0AWewmCTwuw7tqGkDfmctPQvJCSwxpKrZMI4HOO03ewPRMGmNys9RGFsKsC1sFC2B6fQxwdOpgXToxqAXyGXn508HcUto5C33QksP6w0laDMjbY5TjAirXEuFQxWgzi7GmbMmAOHFrkHttDBn2dLikR6iff6WgMxjN_IlXm3GFa0SUhdDj9Qx8WBMeb8eK1TT2tX4rDs56OC0YFxT4QeSEQaJ6BeTPXDUjng70F24ubNJ7E4szTgSueuorh-KneiQrVg17hRKI5kJYkr0D0j61IfL1F27B9gpBDjAQWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b3f81696c.mp4?token=hzNpviGv4S2r378vFS2BpnTmIKhdslNJ-vOXW_4Z1jq4ku0AWewmCTwuw7tqGkDfmctPQvJCSwxpKrZMI4HOO03ewPRMGmNys9RGFsKsC1sFC2B6fQxwdOpgXToxqAXyGXn508HcUto5C33QksP6w0laDMjbY5TjAirXEuFQxWgzi7GmbMmAOHFrkHttDBn2dLikR6iff6WgMxjN_IlXm3GFa0SUhdDj9Qx8WBMeb8eK1TT2tX4rDs56OC0YFxT4QeSEQaJ6BeTPXDUjng70F24ubNJ7E4szTgSueuorh-KneiQrVg17hRKI5kJYkr0D0j61IfL1F27B9gpBDjAQWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع حريق وإرتفاع أعمدة الدخان في سفينة تجارية بالقرب من جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80075" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80074">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وول ستريت جورنال عن مسؤول أمريكي: مسيرة إيرانية أصابت ناقلة نفط كانت تحمل مليوني برميل من الخام قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80074" target="_blank">📅 18:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80073">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وول ستريت جورنال عن مسؤول أمريكي:
مسيرة إيرانية أصابت ناقلة نفط كانت تحمل مليوني برميل من الخام قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80073" target="_blank">📅 18:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80072">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">#قوموا_لله
إنتاجات نايا - أهالي خرنابات
جديد اضغط هنا</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80072" target="_blank">📅 18:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏زلزال بقوة 6.5 درجات يضرب أفغانستان</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80071" target="_blank">📅 17:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80070">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇫🇷
‏
الإسعاف الفرنسي:
109 حالات وفاة في مدينة باريس لوحدها خلال 24 ساعة الماضية بسبب موجة الحر.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80070" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80069">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80069" target="_blank">📅 16:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80068">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80068" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80067">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80067" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80066">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80066" target="_blank">📅 16:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80065">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80065" target="_blank">📅 16:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80062">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الاردن تهنئ النظام اللبناني بالاتفاق مع الكيان الصهيوني
التم المتعوس على خايب الرجا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80062" target="_blank">📅 16:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80061" target="_blank">📅 16:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">في خبر غير مهم
رئيس البرلمان العراقي هيبت الحلبوسي:
نرفض الاعتداءات الإيرانية التي تنتهك سيادة الدول العربية والإسلامية وتهدِّد أمنها واستقرارها</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80060" target="_blank">📅 16:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وسائل
اعلام:
‏ستعقد جولة المحادثات بين الولايات المتحدة وإيران في شهر يوليو في الدوحة.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80059" target="_blank">📅 15:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80057">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1bzkPYGbLogmvG03v3ARyFYBCThGSbLPN3XY3LJxNsC0LlMMD-JonVhXA8SXedfoQFdps_Er0f26aKHj40Pv5RXLSfUU4nkFyneVW5YGQZ2bVwAnQ4tJCvQfl9mRcV6PAhbeWFLyS7sMcWaoSNf9yXzQz8dNmu5KRwvBmMxEE6XpPcenpb_c4DPhORRVbxkqmrfQCpCuC6oQruSMIA8NyOAouYTeJosx4hozLsR5B8jlT4V4LT0pjO10t4kPe-I5CmOTmfcEgbdDosk_iWsJh3MXKqKJnkl0qNDaWLj1u_qXfrmdjeUs-HlUi_eNxaqnw6KhoznDyBO2O9MYXXiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط طائرة مسيرة مجهولة في النهروان جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80057" target="_blank">📅 15:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80056">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c12540e77.mp4?token=u3kkQDGiTNqWz7Gr_xOYfrowfgEC_6bvTt0hrrzYsl2--KwFnXei3mUeaPVgez5YdEvFL_E9sYGrTu1DkkYO1LqZDGMo46pU_vl966Ihs3aCksMY83CBD5AIkZiKDeyTpfS4JGLPtNamgQhqV3qNpvhZR7QRxzavfchWOytK9dEd0bxnXAXohYcALTgO3gYab7iWclg3biawqKT8oUUIx8gH0kOqspDr66skqCCiNnEaziZK-ihwKEa_eMHxKCVdonFABfeGgD3I5CX2ZtBOcXOWhPRUod69mwSB2APCKRHI9y4ASJGXM3bh4ba9AQ1CkQ92QRQpiZJl-cYwCnC-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c12540e77.mp4?token=u3kkQDGiTNqWz7Gr_xOYfrowfgEC_6bvTt0hrrzYsl2--KwFnXei3mUeaPVgez5YdEvFL_E9sYGrTu1DkkYO1LqZDGMo46pU_vl966Ihs3aCksMY83CBD5AIkZiKDeyTpfS4JGLPtNamgQhqV3qNpvhZR7QRxzavfchWOytK9dEd0bxnXAXohYcALTgO3gYab7iWclg3biawqKT8oUUIx8gH0kOqspDr66skqCCiNnEaziZK-ihwKEa_eMHxKCVdonFABfeGgD3I5CX2ZtBOcXOWhPRUod69mwSB2APCKRHI9y4ASJGXM3bh4ba9AQ1CkQ92QRQpiZJl-cYwCnC-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات صهيونية ترمي بالونات عليها منشورات باللغة العبرية على الحدود العراقية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80056" target="_blank">📅 15:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80054">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4jaKsRQcSrZ1_0SSzJhwUVWsT6FHOoBuvmQzatHKUls_7bDDmiQHOG2vI8VtXwnpZqyi8ZIVRkpyLGt7s2s_E5pjGD_SP4AVuPM2gbAmQZt-wGcgGOXZ8OnXbBT_mzXU3DdhpcMtFM2vRqfvzWrUkD55LMnJpXTf8Ins55Q5IOnLwAasNn6HqpqJDqjPtyQxf1bPxE4a1iYhMzQcobL4b7w4_kvTycCJNjCoPD1b4mfyjMygRV9YBfueCRlzz6hDJZBXKcjBboQRg9cSd7Y3NPE6KrY5tKQTfdDT2Y102UkoJCQUiH684DV3_M5ra7tXqi9ymioNI7TTuMgS-4YbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2sS_au2UjK92kqLCb830jROqkcB8hqFekdsapiuQATafIAEkBJNb8usyaRzE2qsJurKztHkLBjhDo55jBZHqnKT1tG2tDnDWMHx_7ykNKSRXKue0sdjqq6b1tFNAoxtluWnMn9YhLUff0fYATAojPBmLbHSKToTcAQMNnOtHLR5C-LxDe_BNwzc9E2BOg9SrP09Mr1psAO90o-ZrTjIGG6CV81D-7f6zHEdEW4uS5vqyZ91NR1OXUlpaU9wXSPwyq0R_aANDxEnBvh2ZnZRX-cYd3XR9XmajxX0xurMtyTm5x5iV6WCRP-YZROYrUMOAeJ95ZL-ouVSXSOAFizvcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طائرات صهيونية ترمي بالونات عليها منشورات باللغة العبرية على الحدود العراقية</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80054" target="_blank">📅 15:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80053">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سقوط طائرة مسيرة مجهولة في النهروان جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80053" target="_blank">📅 15:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSSqV6pHdr9T5DjxcC4BbxgxCMWrhenuS5O8aZqX3MjAjUByQv3oRA9y30t4YSaAkDxPeoFcc0ETRXz5f1r86ChKbMvQM3HJ0W5KbXE5atpulFRIW21rAp11SMJGvMlfOPSboej5yqXGLb3gVoKE3lUDePlJGmnQsaRs1w7Vw6vwiapJ4iRyP1-x2ID5Il58hfjcvJRQ_7G9-vjKUIAXRHeS4td3O5HCjgtBzJdBSgXqo9lPZpGOGe1JeTLao1qXEPXo61c2v2TFVvj7OA1669e1lxxaO2mAzRGfSvlfslkPL1ky1GttKPrahHtvlYpuNtCRt3kSb2EUi_K7q4sgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0UCDn21PctzUgTdwnoQVd-JfmsgXtW6RTFar3e6jobo0YOgk6X_VuNvlq79GAOGI9fXiysv5P5gJdk8KL1ogO2t5BQgjJtfjgxuU5A3O31uQ3QAKAFuIvp8Dho3RfuR0UrBrux9825Qd8oM5A0OC0jmExcWP6lSIanlqLRwtqbk57UQJQEdcV3I4cjVDnV0ILlReXCpkjaTTuek8C6XYT5nXIdlg4ndlUOfPcCrRapBsNsNRUrq-r30s8p2EY6oHoW4iBFgKS6HzDDVegO2X-Nu0mjVoF_LLzcoJQwHjEE-jSQdi2F6XusmN6hXp1b-XIfEmahGgZpPnZJmMMfwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhNjetBx7To6Hn0OBH0Go8hS3oKrP-xHbI_xyeaxTJz6kE783ulmokMSi5cjKwUubmCKrh7l4ECK2iIBEHEop-GLuEOsjxEXht8bwot49P0sRIiAy57yLKMVRKvI4_liBJ1C0khmSLMEH9DjF9mxT0YfEmGyQuc6bE1duLnmjVGKU_sjFkyDFXPOBXA4v3fAknpZX0YpUaQru1gZ8e6v2OVUmSBs5gSPf2AFXwMSNY_IOZqaU46vjqjbrCn4jKPfxWPSzCEoQFEpWfZD3N4JQBeurh4fCA-d_nDtHqyb4hAXTZCdA8WA01iTeOpw-z9L8Sy8btLCur8OLTmQtsGd6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دويلة الامارات تلغي وصف الهجمات الايرانية بـ"الارهابية".
الصواريخ جابت نتيجة
😄</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80050" target="_blank">📅 15:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80049">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📰
بلومبرغ:
رغم تلاشي المخاوف السابقة من تعطل آليات تزويد الطائرات بالوقود خلال موسم السفر الصيفي المزدحم، إلا أن الأزمة تثير تساؤلات حول سلسلة التوريد وموثوقية توفير الوقود لأكثر من 100 ألف رحلة جوية يوميًا على المدى الطويل.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80049" target="_blank">📅 15:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80048">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">#ترفيهي
هيأة الإعلام والاتصالات العراقية:
نذكر جميع القنوات التلفزيونية والمنصات الإلكترونية والمدوّنين والشخصيات الرياضية العامة بالتزاماتهم المهنية والقانونية عند تناول خروج المنتخب الوطني العراقي من بطولة كأس العالم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80048" target="_blank">📅 14:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80047">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اعلام العدو يتحدث عن حدث امني غير عادي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80047" target="_blank">📅 14:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80046">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اعلام العدو يتحدث عن حدث امني غير عادي</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80046" target="_blank">📅 14:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80045">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الاعلام الامريكي:
المزيد من السفن تسعى للحصول على تصاريح من إيران لعبور مضيق هرمز بعد أن تعرضت سفن غير مصرح لها لإطلاق نار تحذيري.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80045" target="_blank">📅 14:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80044">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guNtNWLnhd_mXWGAiefvbprt9bJgOdG4iiXqPkPfKqWK_YQQqlV3MAY_lq-hxZ7l9x16Nv7c1ejt384QldUUGdQe4rcdOwPkbuIqgjK--V1Pqq_lE78KTwklk14hXIYehUgji9shG148vP9lbDw4WpCXpWlqnUJ_pd8KFwX9Ao91ht4BMX-wxxBWeYk_g8j5-dPXWFXorkyYwLZ5dMBt-DM1qsHP21ubJQ3qfqZdVy1C1C18OHKYBYfGm0VrcLojIjZgjbw1DmVFfxR6wIMgDv8pR-6I_tlE4QR2G5zS07NODZLqI0UF-bY54RthimszxQ8-bColZY_sMVa0P8frbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مقتل ثلاثة نساء وشاب في مدينة الموصل شمالي العراق على يد شاب من دون معرفة الاسباب</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80044" target="_blank">📅 14:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80043">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe770_2xTF-tshBqqOO3jse3ZmoRytR4SiNKJN2CRnVOEjrChxiCPUJUV66cnyVAADq4zRcYiCnJO66zN2hIt5aw-H8CeLw4u44ccO2NKYkSxNRr5YzNnV-Sc90ZtPN4YvE3B5aAm-LFDT6x2UgIDHLWqTOoHZeyGXb_ZFVryEAigp8et2pnpdpv9p6Zxz_vdlqD4vGHx2WHA4dNavAtGjVX2OkKEsOzfGUWogEAqbOdju0N5xgKQjX-27pwsrrHplbG26ajnG93VtTxQgvnyREDdqy3GbNsW8v8BHM-mOWbbpWisXqSrc1_CMoDhTM8nj6rbJMSwPhXzlRokWi6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
محاولة اغتيال تطال استاذ جامعي في محافظة ديالى شرقي العراق</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80043" target="_blank">📅 14:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80042">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
ايران تعلن استئناف تسيير رحلات جوية إلى دبي ابتداءً من 30 حزيران الجاري</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80042" target="_blank">📅 13:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80041">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات عنيفة في سواحل عمان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80041" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80040">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80040" target="_blank">📅 13:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80039">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwYT9IOX4_eMvdNzrZJtg56iJla9NzHeW2nF2gs5zS3q4gFH9O4v5Rzbb8KK4jxWVMi_jneKHnesLrzIW3drm5bEX7V3gC9WYwNBnd3MCPhk8rTBFSleBM1Utgzs_VlwgC6AZWPoWCwaAOv6J7APmcis2JebOZQMZdXGSAIESh1Ic9T-P4NAvyBbItj0pOhGyJ4wn_6PiKVJihNTc1lR8r4rzLAwXchQUOKXyLjNbs5mMR_GcTg7cq5BCl9rNagWTs6o3Or4oPLtErqFeWcL4ywX-XARCqplB-MlHyQqKBEFm1g3AYqm0zo6QoM9XnnIqDBlTRU9-TpwvBeYnxk0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة في سواحل عمان</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80039" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80038">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات عنيفة في سواحل عمان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80038" target="_blank">📅 13:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80037">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇧🇭
البحرين تعلن تعرض أراضيها لاستهداف بعدد من المسيّرات الإيرانية فجر اليوم.
بالإضافة ‏لاحتفاظها بحق الرد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/80037" target="_blank">📅 12:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80036">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📰
رويترز: مسيّرة استهدفت معسكرا للمعارضة الكردية الإيرانية في محافظة أربيل شمال العراق .</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/80036" target="_blank">📅 11:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80035">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: الهجمات الأمريكية التي استهدفت منشآت المراقبة الساحلية انتهاك للبند الأول من مذكرة التفاهم
الكيان الصهيوني هاجم لبنان بالتنسيق مع واشنطن وهو أيضا انتهاك للبند الأول من مذكرة التفاهم</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/80035" target="_blank">📅 10:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80034">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">▫️
بيل ماهر: برنامج إيران النووي لم يُدمر.
🔻
جي دي فانس: ما هو الجزء الذي لم يُدمر؟
▫️
ماهر: لم ندخل إلى هناك. كان الأمر كله، يجب أن ندخل إلى هناك ونرى؛ وإلا فلن نفعل هذا.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80034" target="_blank">📅 09:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80033">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
المنتخب الإيراني يتعادل مع مصر بنتيجة 1_1</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/80033" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80032">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429833db62.mp4?token=TMnvdFome3gpPGcNmvCN5Jmx58G5Nr2tAn44XnMHQIxikcuzCAZ6m5wTA6yEp0e2iqgxHMxPcyHW_JBRYFAnSsF-R5exmi_pt2IfEnTTR1Xfb4bGu6voa3gDBV8Qw6X6-GatEYyF-leU0OoDaGyKse2RilWYR-sFbAaHT8LsUOZhD0KqLj64hGpw8qZrpXzhCKxlbjBS6talNa941_GvMjFe0AdmXrzaw6HkxyvGX2qx1EhJFFCnAYYJio4dFEzDC34yC4BSQ4mKJkSk3-XC3kwjb4Uy32xCQF6ajkLOIKqAw4fX6EbcuReZYbIcmDMLYuVSL5TUZh0xLJwliKWEnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429833db62.mp4?token=TMnvdFome3gpPGcNmvCN5Jmx58G5Nr2tAn44XnMHQIxikcuzCAZ6m5wTA6yEp0e2iqgxHMxPcyHW_JBRYFAnSsF-R5exmi_pt2IfEnTTR1Xfb4bGu6voa3gDBV8Qw6X6-GatEYyF-leU0OoDaGyKse2RilWYR-sFbAaHT8LsUOZhD0KqLj64hGpw8qZrpXzhCKxlbjBS6talNa941_GvMjFe0AdmXrzaw6HkxyvGX2qx1EhJFFCnAYYJio4dFEzDC34yC4BSQ4mKJkSk3-XC3kwjb4Uy32xCQF6ajkLOIKqAw4fX6EbcuReZYbIcmDMLYuVSL5TUZh0xLJwliKWEnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي 3 انفجارات في جزيرة سيريك، مقاطعة هرمزغان في إيران</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/80032" target="_blank">📅 05:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80031">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">المنتخب العراقي يتصدر مجموعته من الاسفل ويتوجه إلى قاعة سامراء  للعودة إلى البلاد</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/80031" target="_blank">📅 02:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80030">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">التلفزيون الإيراني: بحرية الحرس الثوري تستهدف عدة نقاط للعدو الأمريكي في المنطقة.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/80030" target="_blank">📅 01:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80029">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">التلفزيون الإيراني: العدوان الأمريكي طال جزيرة قشم ايضا</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/80029" target="_blank">📅 01:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80028">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تصاعد اعمدة الدخان من سيريك بعد انفجارات مجهولة.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/80028" target="_blank">📅 01:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80027">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فانس: سيؤدي العنف من إيران إلى ردة فعل قوية.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/80027" target="_blank">📅 01:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80026">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فانس: سيؤدي العنف من إيران إلى ردة فعل قوية.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/80026" target="_blank">📅 01:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80025">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
وكالة فارس الإيرانية:
الحرس الثوري لم يصدر بعد أي بيان بشأن هجمات اليوم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/80025" target="_blank">📅 01:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80024">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf3657c0e.mp4?token=U1OuWSQEkIP16cuhSAS6bKys5K0BegEfPRjcPevu0yYN8FI_3f7a-5Y1UQ3Op4N0LVhGrmwsAEXY07ceKpaOpvZrSjlyVjSr9IfGAJiBflrfBH0XjZV_9mHy2e08tKueKcCEHPryWPqToEdw8ru_0ySxZaYWrQuVRlhZZoNodV-iTXvDER1icnd0uI45LgG7kEN2uBjMXkxIXhLkomu1To9Lffshhb7uFKj2JINGEneMGYzmEhHRLeVQF3E2gl9N1eHERHB7FklsvshcRROjeg_c2hQnJWnqbpXlXLAr1VRLJA3wxf6MWJLD7qUWDK1alG0SVG66WlseWFZ-08ffDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf3657c0e.mp4?token=U1OuWSQEkIP16cuhSAS6bKys5K0BegEfPRjcPevu0yYN8FI_3f7a-5Y1UQ3Op4N0LVhGrmwsAEXY07ceKpaOpvZrSjlyVjSr9IfGAJiBflrfBH0XjZV_9mHy2e08tKueKcCEHPryWPqToEdw8ru_0ySxZaYWrQuVRlhZZoNodV-iTXvDER1icnd0uI45LgG7kEN2uBjMXkxIXhLkomu1To9Lffshhb7uFKj2JINGEneMGYzmEhHRLeVQF3E2gl9N1eHERHB7FklsvshcRROjeg_c2hQnJWnqbpXlXLAr1VRLJA3wxf6MWJLD7qUWDK1alG0SVG66WlseWFZ-08ffDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش اللبناني يطلق قنابل مسيلة للدموع لتفريق المحتجين عند طريق المطار</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/80024" target="_blank">📅 01:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80023">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKSbw1dDrC4fVVVQvqXNtjXWfxP9HZ2fORVdIUS8uYGxOGudvRcyicxCiEMspkzN_AmryekXVaxgWR1fmkJYOdFsOxUeFzbwkjd2KQ-MyxO9MZdxmfLvkbeXBUvuvWhz8bkx-OPrTlsVl4ctUECFoSc574fcfz0BDZ5rLxTwn9x-dU6XLjd3nteBpHW0aRiTfeVTBl1dtsVtBaXW762beCpcWhkjulWK6JQIRd_zsUqkQggNG-sC9M1B6kwELkhHr9TTJodiwzPbNJ1e9AwZsImYMTIYhqxLn1wIZD1pWDBoHfOhSRSW1TxYMzIlp4F4ZGtbl_LPIgQd_YAKIrUzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رئيس لجنة الامن القومي
الايرانية
ابراهيم عزيزي:
مرة أخرى، هاجمت الولايات المتحدة إيران في خضم المفاوضات. ‏أثبت الرئيس الأمريكي المهزوم مرة أخرى أنه لا يلتزم بمبادئ التفاوض ووقف إطلاق النار. ‏إن هذا الانتهاك غير الحكيم لوقف إطلاق النار من جانب الولايات المتحدة سيؤدي بالتأكيد، كما هو الحال دائماً، إلى تراجعهم وندمهم على ذلك.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/80023" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80022">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مسؤول أمريكي لفوكس نيوز: الضربات على أهداف إيرانية "مستمرة" الآن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/80022" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80021">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">إيران | الحرس الثوري الإيراني:
- نؤكد أن هذا العدوان لن يمر دون رد، وسنختار الزمان والمكان المناسبين
- نحذر من أن أي حماقة جديدة ستُقابل برد قاسٍ يُحطم أوهام المهاجمين في المنطقة</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80021" target="_blank">📅 00:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80020">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5d0dc8f5.mp4?token=vuZSzPJrN9jyX9h_yVkKSP_oFXOcqWNXYAP3ikZmcTsar4-Ye0GOWBC3ltNl5ER2gRL8v31ZEhJmEdhBDlZBR7_8lppw-4vQnFcXtRX4AvY5YKVlOXITUjV5Q4-PBhxytLfnw8vHYP7Ou5rxArUQFYwOyhV8W54SvLYDFEtsDD4ixGy2T9vKcgPzDxyRribO9YSyJ0KZform1-dNo4eRwLUTb00-khMC6TweYkAlOgyBb6Lp2xzQLkI27x9fi47fWAdAIK1IeFicjCin9unyHdxw2ZpWc_Lej--5b2EdC0ljhmVNiQLDs7QD7mcUa4T7DGrzkrfDMUQ-lqibLN9Uew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5d0dc8f5.mp4?token=vuZSzPJrN9jyX9h_yVkKSP_oFXOcqWNXYAP3ikZmcTsar4-Ye0GOWBC3ltNl5ER2gRL8v31ZEhJmEdhBDlZBR7_8lppw-4vQnFcXtRX4AvY5YKVlOXITUjV5Q4-PBhxytLfnw8vHYP7Ou5rxArUQFYwOyhV8W54SvLYDFEtsDD4ixGy2T9vKcgPzDxyRribO9YSyJ0KZform1-dNo4eRwLUTb00-khMC6TweYkAlOgyBb6Lp2xzQLkI27x9fi47fWAdAIK1IeFicjCin9unyHdxw2ZpWc_Lej--5b2EdC0ljhmVNiQLDs7QD7mcUa4T7DGrzkrfDMUQ-lqibLN9Uew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النظام اللبناني يرسل تحشيدات كبيرة للجيش الى طريق المطار في الضاحية الجنوبية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/80020" target="_blank">📅 00:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV-0oN2CW3cZHRe7FfzpzPj7-khSjPz--uV5ao_tn9OJ5-3u4PrG6Rl1VieFT2D3_ESA8BkBTh9RQb3KbuYqXt3NrIXRTX5GqMOQZnKUCk8Gd27u8b6aOPMgnPvmn8P8L9M4uhiUaN-bsz5aHJF-ey0tufkHsE77Au0sKqbaDqlQNIvWJUt1pP7J-y6Hkww7sjWH45PHsUHNedVX5KHoB1P0VcSmGnuknigFcnnbEFMhBboswxKuuqylfpueNN76gHqiJaovFd0y5F5sL_ZX-xNS-2LLXZcTmSxvnHpQ-abUc4X6f0I1O9gJulZDZn33nQFIu5qlOntfG8pZ36omsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط لطيران أمريكي غير مسبوق فوق البحرين الإمارات وعمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/80019" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1GUeKdVlE_kxKPnpjjVbBImRSKlOIJiq1M8Atn86QCDT-pLMyxpP4NkqotWJsVrK_FISZbFCI42Wz-DdwAWbH-tHrl32X82tDbLDcF3odDNrrOem6g0NzhlH9gxYhVwhYEre-_bcGnDJEzmIvMXweu0nQcaCtAKWUhX5UTFHEtDoCx5_3XrJUQzqbBBw2PpnP5PJOv5vBiSJz9nG68Xtvy2d37uGhFbY6TdafP2twHlesQkshZpttnbnou023mP0oelkKILax_Y3YIanDlkbJykHs7eY0JgCDb_EfiC5VVW_gItBlWPd3cH0u6nrYetZ6o7S6cqgxbKaeTYkRkSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاعد الغضب الشعبي في لبنان بعد اتفاقية النظام مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/80018" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgOm9kyMhH_rLYIYPYPquN2sKM9Hm5ADYef7G3pZz724cElMX0bqRepRcGJspkmxU_8CH6F3XpttcxxVM8I0MlX5wc_JeT2lF_9sWC4G0J7pgQ_bGdrYoQTlGWqAQ9dKfkfEOuwpoOYxLr9gQl4NtZuCJPCp9QRqGsUcBC_etSE01Zp1vHUy68VMOjPXnYcV_4dVnEMgGpdRsTyve1vxkeylaZ63pnI4nKijbkEFGsCpTraQM-Qo00RborUgAQxkdIdXu01lu-EOH5-SO-OrZOUMgaxTfsH0mIyn1PopRenPgevn1DdqDF4yep_BHVFTwScNxBM2b1fnWeTMbRQkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السنغال تسجل الهدف الخامس في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/80017" target="_blank">📅 00:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4eea0f59.mp4?token=NjK5ub52aFSZD27cL099g_TKE3IJGu9NIXrXJ9mPIydH9Te8Xo_P53HsR0nrOV69wiUsFF4NC9ZHrKbUjFCDlsClnhe6-gMUy8QnsJnOoibhUJU-keLI1WSw1P_9Gzbs7aXzC2TS5tEWAWUcEfAW9pxv2QdWdYMjmj4KoA4ygDJF2ZT_LKjABP0hnl7pEoWxuiY3_qe91R2nz2IaKuy0XRK1sRjEpt3amugcqa4K_-qUnFcHxGpUNZhzrCa-FitS7fGHRuduNT2S1ojluycvOc4MzjF-dItFWBje_3k0TYa7LC6qBbqwFTUxQLLpDBjlD0Bv4R6pd7Pb6HbmbvZ5mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4eea0f59.mp4?token=NjK5ub52aFSZD27cL099g_TKE3IJGu9NIXrXJ9mPIydH9Te8Xo_P53HsR0nrOV69wiUsFF4NC9ZHrKbUjFCDlsClnhe6-gMUy8QnsJnOoibhUJU-keLI1WSw1P_9Gzbs7aXzC2TS5tEWAWUcEfAW9pxv2QdWdYMjmj4KoA4ygDJF2ZT_LKjABP0hnl7pEoWxuiY3_qe91R2nz2IaKuy0XRK1sRjEpt3amugcqa4K_-qUnFcHxGpUNZhzrCa-FitS7fGHRuduNT2S1ojluycvOc4MzjF-dItFWBje_3k0TYa7LC6qBbqwFTUxQLLpDBjlD0Bv4R6pd7Pb6HbmbvZ5mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
الغضب يعم لبنان بعد توقيع النظام اللبناني اتفاقية مع الكيان الصهيوني</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/80016" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇮🇶
اعفاء مدير المخدرات في محافظة النجف من منصبه واعتقال عدد من الضباط والمنتسبين و ارسالهم لبغداد بعد عملية قبض كيدية بحق مواطن نجفي</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80015" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6017431c96.mp4?token=daG85vTNuXDwP26WnB6pVu6XXUYC-AedLnZWFBEipzfGXDonHEVil1FVnuxykRlXU_YylbKfRK3C2y6OrFkyTKi_4NyKoqDsUOg1iV-yembSpILUiDfEqwbKgyqll2Kn0Dc9BsDcKdNmiSckHbJQjNv9Lk8NSDxuJ551_VYng6op69yBoDc_TshYGSEjskO139_I93D-70EBnLIyxu5Fei1-6YDDkVNhKWZ1LByG4tCq5v-IRL3JVrC3jrxGrkSH7WXYsENBIpsCPDSLXcQ9fFd0NeDYVPprZrtjI7gNyPnrgl8Mz8ZRKIqq9-li4k_FfHcxlP8e06bgeaq3GbrOjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6017431c96.mp4?token=daG85vTNuXDwP26WnB6pVu6XXUYC-AedLnZWFBEipzfGXDonHEVil1FVnuxykRlXU_YylbKfRK3C2y6OrFkyTKi_4NyKoqDsUOg1iV-yembSpILUiDfEqwbKgyqll2Kn0Dc9BsDcKdNmiSckHbJQjNv9Lk8NSDxuJ551_VYng6op69yBoDc_TshYGSEjskO139_I93D-70EBnLIyxu5Fei1-6YDDkVNhKWZ1LByG4tCq5v-IRL3JVrC3jrxGrkSH7WXYsENBIpsCPDSLXcQ9fFd0NeDYVPprZrtjI7gNyPnrgl8Mz8ZRKIqq9-li4k_FfHcxlP8e06bgeaq3GbrOjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مشاهد للغضب الشعبي اللبناني في محيط السراي الحكومي في بيروت بعد الاتفاقية مع الكيان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80014" target="_blank">📅 00:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e30e9777d.mp4?token=BaJce8Ap2vodXhwGmbaIuKB_MgMNOSMItUxMbySzviuUjF4dbC4hZV3cTu98Ll_f9KdZ3caReklb17uAbNJmPL7F_bLFE8k-sAl6GBCL9KzzeL-6oImt_JyhGJXo-ePLQn7RoltBI7oC3ia8YNVZMCG4E3yO1EFAtw7_aQAd063LEKYp8wDgCxZ8rabw_wIBifXRJkyj_I_YYt6NB2MreX3-qoGSgPzgCUQCLdICH6XXWAJKbcUe9zSlCeUqr9Ko7YbSIhR08WEY1ZPhf-zrd14JpDuZFgvNmJW-gaU2iULyiApa51H-clgVG9UWrM8a2-drI9vu5b2BvJ3HVz-Nfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e30e9777d.mp4?token=BaJce8Ap2vodXhwGmbaIuKB_MgMNOSMItUxMbySzviuUjF4dbC4hZV3cTu98Ll_f9KdZ3caReklb17uAbNJmPL7F_bLFE8k-sAl6GBCL9KzzeL-6oImt_JyhGJXo-ePLQn7RoltBI7oC3ia8YNVZMCG4E3yO1EFAtw7_aQAd063LEKYp8wDgCxZ8rabw_wIBifXRJkyj_I_YYt6NB2MreX3-qoGSgPzgCUQCLdICH6XXWAJKbcUe9zSlCeUqr9Ko7YbSIhR08WEY1ZPhf-zrd14JpDuZFgvNmJW-gaU2iULyiApa51H-clgVG9UWrM8a2-drI9vu5b2BvJ3HVz-Nfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاصرة السراي الحكومي في بيروت بعد الاتفاقية بين النظام اللبناني والكيان الصهيوني</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/80013" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
امريكا تشن غارات على ايران.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/80012" target="_blank">📅 00:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80011">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">السنغال تسجل الهدف الرابع في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80011" target="_blank">📅 00:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7mNATI3o9RzdT5lKRydAh3IoU9vrKIWo5fdmBpafvzsguVLafvGCEIYf288_-KoXT0NgF4V089rUEbrfEjsJHImOnKCh9EK9lUTDNQIZg-pv7U3xARVcUEKljvPVH6YQMbkkDQJ1oDEf-_4vYmLhZGRUF4sSW8fY1esxtrSEcGKj-NFZTQfGpgdYpa8tVLmFFfkEdFspJeGH5j9owss8hNesY_RMLVFhGI5q5jtpahhxep2mlziBHN3YPB7uvRi1P-QK81cEL4HMwk-vZCWvPTTJuqwmBXMxMuZkESfBuPaliqRKKBeDGU_qfJN6MHSoTgg7_Gw2YrTJVpHPrQpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uufvo5sxEZOKqyIgmQUb1MNdUsJSYexZK_LGyG8Fr9_xEeofGoS2xJjS1PBsb_ozGH90y2Bs8nOKX4uWXjMFNq_YzjHxIW1T1XzhuvRocSVBsO1WSWm1UMnmMu1GBmVKHUK0U-wW2bjejHihqKAY8sRXREH2D7ToazgSU-fxYEgwrznY1EJSzZXsdcXMTixmSJIxeN9oewyYVG4_doCpSxcpBq6Rk1aq1eU_rYZJQEmIaFv5JL9J8IipDBvmXOna9F2ebrV6Ht9C_ubLb-myPjPMtjyeKW_-OqMd3aFLoihx-gMrWCAf0pe-tYxPpaBnWHHHc6ML8rsuMMnHsRECZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النص المبدئي للإتفاق بين لبنان والكيان:  ‎ تؤكد إسرائيل ولبنان حق كل دولة في الوجود بسلام، ورغبتهما المتبادلة في العيش بأمن كدولتين ذاتي سيادة ومتجاورتين. وتعلن إسرائيل ولبنان بموجب هذا الإطار نيتهما إنهاء النزاع بينهما بشكل نهائي، ومعالجة أسبابه الجذرية،…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/80009" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">السنغال تسجل الهدف الرابع في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80008" target="_blank">📅 00:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">السنغال تسجل الهدف الثالث في مرمى منتخبنا</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80007" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
