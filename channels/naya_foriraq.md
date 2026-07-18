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
<img src="https://cdn4.telesco.pe/file/QxZbwXXNeCBFvbuyWenAKyN9JyRxVk26L8PFhBRc-8LpVMUA57E9mORtsWLNoEvF9MRMVKH827V63AGFDexNKslURKAKGvLJoWYErF1NOIiq7-dKzPR6nwFbwzIVJMe1otcqwDPQr7gbUpml3R-g6wi2n4hkjvY1cO6lmdexow2hCeZI_de641Fq-hGck-5wByAA_MHenfzi_XqVyOHHIPTuMOxFZELLAIYu5Fn4kdus7MQ5xLKDWsmkfJFcVd3eEiuuvFi4HX8K0uSJVSuY1Us3NDqfjciUUpzsyG3b6KXIWN4yOu7Lley3PW_M2vPuxAujPIk2kANE53N-Jv_Q_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 12:13:28</div>
<hr>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/naya_foriraq/83889" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/naya_foriraq/83888" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b01d4738a0.mp4?token=MfCPPOHd2eWHDDbtUMRgd3ZeKUcldkX96sTwuxXcXtwKWXBBIU2X_whekT4Lm6UuO3YuW4jWDVT3uFRfce4ZoixzU8r98sqdmRjHaoNOcKLc1N-2ffUsrnv8b7c1BoCUuE8mR00BZLhq9n27GrOob6FCJ6jXrxeeBC4pkECCNBFo2xuo2RkG3umTtxcmmIesh9ptlOOVXHiJRd94qJktTrI5_va6emnKhcd3K8bz1UMsmxO1OUqdj_QaH-_RmX70Kvzgf-iLQrAsKTD711OnfMaQHM4kcGfyRqnkm-y1hZ-8IHvCPQUnDAa5LC4qz5RB5nDlQ-w0MO1jkj1LFZQUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b01d4738a0.mp4?token=MfCPPOHd2eWHDDbtUMRgd3ZeKUcldkX96sTwuxXcXtwKWXBBIU2X_whekT4Lm6UuO3YuW4jWDVT3uFRfce4ZoixzU8r98sqdmRjHaoNOcKLc1N-2ffUsrnv8b7c1BoCUuE8mR00BZLhq9n27GrOob6FCJ6jXrxeeBC4pkECCNBFo2xuo2RkG3umTtxcmmIesh9ptlOOVXHiJRd94qJktTrI5_va6emnKhcd3K8bz1UMsmxO1OUqdj_QaH-_RmX70Kvzgf-iLQrAsKTD711OnfMaQHM4kcGfyRqnkm-y1hZ-8IHvCPQUnDAa5LC4qz5RB5nDlQ-w0MO1jkj1LFZQUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇵🇸
🇮🇷
شظايا صواريخ الباترويت الأمريكية تساقطت البارحة بشكل عشوائي مما جعلها تتحول إلى مصادر دمار لمنازل المواطنين الكويتين</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/naya_foriraq/83887" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
الخارجية الأمريكية : وننصح الأمريكيين بإعادة النظر في السفر إلى الشرق الأوسط .</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/naya_foriraq/83886" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
🇮🇷
مراسل نايا: دوي الانفجارات في مدينة مهران ناتج عن تفجير ذخائر حربية</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/naya_foriraq/83885" target="_blank">📅 11:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني موجهاً رسالة للشعب الأردني والجنود.
أيها الشعب الأردني الكريم والجنود الأشاوس؛
كما أدهشت استمرار تواجد الشعب الإيراني في الشوارع لمدة 140 يومًا لدعم الثورة الإسلامية العالم، فإن استمرار ردود أفعال مقاتلي الإسلام، التي تواكبها معونات إلهية وتحقق نجاحًا حاسمًا، قد أذهل العدو وأدخله في حالة من الارتباك والهزيمة، ودفعته إلى الانسحاب من ساحة المعركة واللجوء إلى جرائم حرب وعمليات غير إنسانية ضد المراكز والمؤسسات المدنية.
الجيش الأمريكي القاتل للأطفال يحاول إخفاء هزيمته في الحرب المباشرة مع قواتنا المسلحة من خلال مهاجمة المستشفيات والجسور والسكك الحديدية والموانئ والمطارات وقتل المدنيين.
في فجر اليوم، ردًا على أعمال الشر التي ارتكبها العدو الأمريكي الليلة الماضية، أطلق مقاتلو القوة الجوية التابعة لحرس الثورة الإسلامية عملية "نصر 2" تحت شعار "يا أبو الفضل العباس (ع)"، حيث شنوا هجومًا صاروخيًا وطائرات مسيرة مكثفًا ومتزامنًا على مواقع طائرات مقاتلة ومنصة إطلاق كبيرة في قاعدة أمريكية في الأزرق بالأردن، مما أدى إلى تدمير كامل على الأقل طائرتين وثلاث طائرات أمريكية، وإلحاق أضرار جسيمة بعدد آخر منها.
الآن، حان دوركم أيها الشعب الأردني الكريم والجنود الأشاوس. وفقًا لفتاوى جميع علماء الإسلام من جميع المذاهب والطوائف، فإن الجنود الكافرين المهاجمين للأراضي الإسلامية دمهم مباح.
الآن، الجيش الأمريكي الذي دم القتلة، والذي قتل مئات الآلاف من المسلمين في أفغانستان، ومئات الآلاف من المسلمين في العراق، والآلاف من المسلمين في إيران، واليمن، ولبنان، وليبيا، والسودان، والفلبين، وفلسطين، هم في متناول أيديكم، وتقتضي واجباتكم الدينية والإنسانية أن تقضوا عليهم بأي وسيلة، وأن تطهروا الأرض المقدسة الأردن من قتلة المسلمين الأبرياء.</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/naya_foriraq/83884" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edc485f93.mp4?token=s4p5j0Hg7fDTJViotbcAgdDQ5lMucyR2CG0uBXsSE2IKW4ZIEHBKbUeboeUd3RmDmJS96o_4av5yIB1fykIkXH0TbNDnngu3NPnCRUEpH9pSIc6AfNndPkXCxO7CDR1xyLNtm13gMxHeue1P1uFl3B0G58cZousOvxFm7LjlaeYnjECs5_KZH6ZoX57TUZxKaRnGZINgq9724eiGqdySO6eNwu1tqCW9b6ezinYnNCculZ9XaDkJD8T5d0_udcWRHKha28apSbJYxgwBMkyxqnb5Lbe6tpQvYdt25Vp59V2RaEq1XniAbnggPV48X4jJwDjH-1nmuqCiQI0E7XHrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edc485f93.mp4?token=s4p5j0Hg7fDTJViotbcAgdDQ5lMucyR2CG0uBXsSE2IKW4ZIEHBKbUeboeUd3RmDmJS96o_4av5yIB1fykIkXH0TbNDnngu3NPnCRUEpH9pSIc6AfNndPkXCxO7CDR1xyLNtm13gMxHeue1P1uFl3B0G58cZousOvxFm7LjlaeYnjECs5_KZH6ZoX57TUZxKaRnGZINgq9724eiGqdySO6eNwu1tqCW9b6ezinYnNCculZ9XaDkJD8T5d0_udcWRHKha28apSbJYxgwBMkyxqnb5Lbe6tpQvYdt25Vp59V2RaEq1XniAbnggPV48X4jJwDjH-1nmuqCiQI0E7XHrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🙃
تعرضت مخازن عملاق التسوق الروسي شركة وايلد بيري الروسية لهجوم بمسيرة أوكرانية في العاصمة الروسية موسكو ، تشتد الهجمات الاوكرانية مدعومة من بريطانيا وألمانيا وفرنسا على موسكو بسبب تجنب موسكو المواجهة بين تلك الدول او الضربات الخجولة على تيار البندريين في كييف</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/83883" target="_blank">📅 11:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaNib9A_9y9DNyuFRAHIO6vCLvVm6Ki4skcanEfNMVYsTVV3xYSEhtr9vO18W1VEPlAOxTie44n5oyj9sh-hytlX1DckyY73qyOrplq_FHU71tVbkDMlEiu-6dgx539HlwVpNuMxzYsNI45gneTmjUGZAOlu41ZR0dntMmZY7LIc-szLED9bF7umKqnJzhCHWDG0nhWgRIzUIY1v-AoScfeArN-fXfg7V_knKEtr_n76ii__7o-n7YLyQ6IQkUzk-OUzYhPxMb98xXAH_0-6G2ZyAoNzVmIQYUjdc1zX4NB2ocOIZBPpGFFd6DaM4TpEOU6Np_GHxqP99I29CHR_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لليوم الثاني على التوالي
الكويت تطلق حملة ترشيد الطاقة بسبب الهجمات الإيرانية</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/83882" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83881" target="_blank">📅 11:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تصاعد أعمدة الدخان من الموقع الأمريكي المستهدف في الكويت.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/83880" target="_blank">📅 11:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇱
🇺🇸
السفارة الأميركية في الكيان المحتل تصدر تحذيراً من السفر إلى إسرائيل والمنطقة بسبب "التوترات الشديدة" في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83879" target="_blank">📅 11:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انقطاع الماء عن اجزاء من الكويت</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83878" target="_blank">📅 11:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c6693056.mp4?token=ie5qwieRuWpYm2uPKk-ltPlelIFIiLby5RxtFDN52pvB7cx3H_k6tnr2ZAzHiFGq-fFkwe8MeXyLWdNM7cMa9Lo_94sFzCSvjQeNkBDKjH9tOODatQnvIOaI80djAUVptyYiNq4bhZq_fQXEOy1aQIhXN87EhyIgQNfI8lXJRCOQ2Nb0mPCd6-wMlNR0V5X8aRhyxPaTh_lAuw4n3ygteCqh6BJbLM75Zrp5cyx7P_EKFOAm-EgaeOhkdrfVSg94t84hatFQz4-aA8siBb2RY192l45na4j3BP4v-LihBHkUKmn0fwnFOoC6GsQ7XDgPYl9wlueyqUXDVIsBCbNyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c6693056.mp4?token=ie5qwieRuWpYm2uPKk-ltPlelIFIiLby5RxtFDN52pvB7cx3H_k6tnr2ZAzHiFGq-fFkwe8MeXyLWdNM7cMa9Lo_94sFzCSvjQeNkBDKjH9tOODatQnvIOaI80djAUVptyYiNq4bhZq_fQXEOy1aQIhXN87EhyIgQNfI8lXJRCOQ2Nb0mPCd6-wMlNR0V5X8aRhyxPaTh_lAuw4n3ygteCqh6BJbLM75Zrp5cyx7P_EKFOAm-EgaeOhkdrfVSg94t84hatFQz4-aA8siBb2RY192l45na4j3BP4v-LihBHkUKmn0fwnFOoC6GsQ7XDgPYl9wlueyqUXDVIsBCbNyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز سماء كريات شمونة شمال الكيان المحتل جراء إطلاق صواريخ من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/83877" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83876" target="_blank">📅 10:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83875">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/83875" target="_blank">📅 10:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83873">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vngtqY7bZ6tRuhgwdzgcrjc1YvS_-_i1UPg8qRcBtCUpRApNOvUjbI3UC7rtLAIs3oVdvrccE5bcNjG1XfrFEMlzo3HnwYnfWtP5rszG-GT1VIcfBBnADqKcO-1mevL9qiYRpTHB4YI3OY5Nocpc1anw703VPZU8x8SYzKz3SownSieMAgA9jY7wgThH2wQQRdbkfEmMuJ0toWPKjWdg0bWHjU5kAaArOVQ60LENm785JfH6o4PN4CaXM365lFVD2pvtUUWgMuBrzrgBoyCzS0ZAPQECvarCsUte8qwav4j9DoQ0SuPuE01HI_zhANZpqMrma8SKtNClc1-nVdvV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQIIM3lnLsB8d5VdHBEZnjz5qF2dwgCOD2WIcse7Wy9hURhsnqGPdVwgo8KDCTABYALWbH4o14DPoB_tCcY1R0RI07pxwi6C5j6Np-etNawTj70M9Z8_IlOr8fFLUYpqu7IBQX12igFlAi_LDODla-mkEUGXK6CbCQH28BUV3UlGwV2qgXV7PO2bT-8_F7qAzw93gGHAYoCdaGn5sw3wPlLLmMa1OBBW7ULwI_2DrpeFmoTxewkVhwCCvhlrd6SSsXoJ27K_zHW9Ud58MHpMGlEAJAH8jrlawpoVA7UBAIe8TiEo9QcqkERCqZNOMnEA5f-oa0_p1tyX_c8jGrS0aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هناك احتمال كبير أن تكون طائرة أمريكية أخرى من طراز MQ-9 Reaper قد دُمرت في الهجوم الصاروخي الباليستي الإيراني الأخير على قاعدة موفق السلطي الجوية في الأردن.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/83873" target="_blank">📅 10:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83872">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/83872" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83871">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83871" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83870">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏الكهرباء الكويتية: هجوم جديد استهدف محطة أخرى للكهرباء وتحلية المياه صباح اليوم</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83870" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83869">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b66fe6ee.mp4?token=BrxqwSr69uJsJK4p30oH8to7PK80Xltn2RTvDS8vq2qT2-I2lc5Umh33rzgulQh8kUIHfPT6-9t_dB9vO--zR_0Q3XDs8jno0bP_qEwVmFrcG6c2s-JiGZYkPGDm7puD5HYgKb3RVQPQunF5y9VQz_OsfHmMocwJu2ajfgKFaCj2r0GBocVeAotwRKlvuqHNlg_kHChK5HYIxRrTIWc90N3GAjwsKPE2qITnLaZ1bl-q0un3iDsQqhl8f_XvY-AbEAirPyYTMdKFOB55AtM7KFy4gpTSGeZYoGNcY3LqqRzUpEfWDAzYdNLZY-HBm4Vlks2q_YyW213ZDf3-KkmqgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b66fe6ee.mp4?token=BrxqwSr69uJsJK4p30oH8to7PK80Xltn2RTvDS8vq2qT2-I2lc5Umh33rzgulQh8kUIHfPT6-9t_dB9vO--zR_0Q3XDs8jno0bP_qEwVmFrcG6c2s-JiGZYkPGDm7puD5HYgKb3RVQPQunF5y9VQz_OsfHmMocwJu2ajfgKFaCj2r0GBocVeAotwRKlvuqHNlg_kHChK5HYIxRrTIWc90N3GAjwsKPE2qITnLaZ1bl-q0un3iDsQqhl8f_XvY-AbEAirPyYTMdKFOB55AtM7KFy4gpTSGeZYoGNcY3LqqRzUpEfWDAzYdNLZY-HBm4Vlks2q_YyW213ZDf3-KkmqgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي صافرات الإنذار في الكويت دون توقف</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83869" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83868">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzCnbLGm25B3hyKvC1PHfsD26iujS0kIe1nGcXn7-jcJ9h_Mdv3M3XBG7ngistF4-UJORWhbzA8shIN7YKtEs3wJRvFVmEXpsS3ILbyEFGTQcppdvLHoX6fQUJqShGjVKYJRpTTOU8BrmJOs-dtK9YIe14q4HBKIcizz65ITvk-GI7PQLEd7YbcdHmbVfTeUOsfpuNxYIx-IaYlmZNbZ_g7rv3d5jfqDxVjn-g8Egc_I1hfU9J4fR8It118cyzQyb1rJ0ocTe-syiv6XuXqvpUjiGm15rphsJP6JdjVymb7JVTOWV1VLKNwdn4vWevW7KMS2S1u-5qAY4cIWS0653Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت الان تشتعل بفضل الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/83868" target="_blank">📅 09:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83867">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">إطلاق صاروخي جديد من إيران</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83867" target="_blank">📅 09:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83866">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83866" target="_blank">📅 09:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83865">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738e610a18.mp4?token=r3GOQFPO6gKX_1eC8OnJnAvXeqL_HOk5l5Bo4I-a7N98G18XIlpI5cOg61hvcU0lOeB2S9_rbNAecZYtD2wsdd-KQLocuMKeMaPAXCLPznQGsVATsAIrLceGN7YA-4kuVBSWZfNSFw-Mih_fdxSfmTczsigoLNqRiufMNrK8rLj79FBw9eEROBBzNM_xIQ-YWd6ueOVpqcVCYJT4GQBWKa36e9W7ThiqsL7S3QhXoHuAfIaM11Azfa3QTiU1aeizHYFHB2QZXTGoFMJDkynU-5jo4y0FrObuIQhkHxjtsPuJbascDkAngStVAetl0-Z3oY8P7IeborEtU4Ho3VrM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738e610a18.mp4?token=r3GOQFPO6gKX_1eC8OnJnAvXeqL_HOk5l5Bo4I-a7N98G18XIlpI5cOg61hvcU0lOeB2S9_rbNAecZYtD2wsdd-KQLocuMKeMaPAXCLPznQGsVATsAIrLceGN7YA-4kuVBSWZfNSFw-Mih_fdxSfmTczsigoLNqRiufMNrK8rLj79FBw9eEROBBzNM_xIQ-YWd6ueOVpqcVCYJT4GQBWKa36e9W7ThiqsL7S3QhXoHuAfIaM11Azfa3QTiU1aeizHYFHB2QZXTGoFMJDkynU-5jo4y0FrObuIQhkHxjtsPuJbascDkAngStVAetl0-Z3oY8P7IeborEtU4Ho3VrM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق كبيرة جراء سقوط صواريخ إيرانية داخل المواقع الأميركية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83865" target="_blank">📅 08:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83864">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/83864" target="_blank">📅 08:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83863">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83863" target="_blank">📅 08:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83862">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83862" target="_blank">📅 08:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83861">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83861" target="_blank">📅 08:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83860">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الخطوط الجوية الكويتية تعلن إعادة جدولة معظم رحلات الطيران بسبب إغلاق المجال الجوي الكويتي اليوم جراء القصف الإيراني</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83860" target="_blank">📅 08:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83859">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجارات جديدة تهز دويلة الكويت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/83859" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83858">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات جديدة تهز دويلة الكويت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83858" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83857">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات جديدة تهز دويلة الكويت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83857" target="_blank">📅 08:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الحرس الثوري الإيراني: في الموجة الأولى من عملية "نصر 2"، برمز مبارك "يا أبا الفضل العباس عليه السلام"، استهدفنا موقع تمركز وتجمع القوات المتجاوزة في مركز دعم القوات البرية التابع لهم في عريفجان، مما أدى إلى هلاك عدد منهم، وفي الوقت نفسه، قامت بإطلاق هجوم بطائرة مسيرة على رادار قاعدة علي السالم الأمريكية في الكويت، مما أدى إلى تدميره.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83856" target="_blank">📅 07:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/83855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83855" target="_blank">📅 07:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات تهز مدينة خرج السعودية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83854" target="_blank">📅 07:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d059d386b.mp4?token=IUeNOv0YIwN120zJVtH5Yap6nUIZ0mTvxiaZF3xzLAqrYpm7wFNuXjC2pXVeFGirEzINC4vRwajxz-7X44TNiVbCumht5F77QVctjoMdkqirlv-gJNZAvrz-iGFCqCnYIY3NclEHaXjsyPW3XMZZjvR-y-M2T212VgGTaN1EakYbemKlWPrWis-7ND-5V1o0NXGBoQMhbvC9Ds6wjv0PgbKEfnAcNhiQXoDInU2w3MF29OWGhA3AvEVMTd8TSUCHmDsS5GmWbUbNoxe8ApJtJFXbvbNdfI6Xs3PCBa6j-fLRit99dQ_M7ivSglpA49_VGnR43SlcuvFkkuA5ceECOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d059d386b.mp4?token=IUeNOv0YIwN120zJVtH5Yap6nUIZ0mTvxiaZF3xzLAqrYpm7wFNuXjC2pXVeFGirEzINC4vRwajxz-7X44TNiVbCumht5F77QVctjoMdkqirlv-gJNZAvrz-iGFCqCnYIY3NclEHaXjsyPW3XMZZjvR-y-M2T212VgGTaN1EakYbemKlWPrWis-7ND-5V1o0NXGBoQMhbvC9Ds6wjv0PgbKEfnAcNhiQXoDInU2w3MF29OWGhA3AvEVMTd8TSUCHmDsS5GmWbUbNoxe8ApJtJFXbvbNdfI6Xs3PCBa6j-fLRit99dQ_M7ivSglpA49_VGnR43SlcuvFkkuA5ceECOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار اثر الهجوم الجوي على الكويت</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83853" target="_blank">📅 07:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83852">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83852" target="_blank">📅 07:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83851">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83851" target="_blank">📅 07:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83850">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار اثر الهجوم الجوي على الكويت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83850" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83849">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83849" target="_blank">📅 07:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83848">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز الأردن من جديد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83848" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83847">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83847" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83846">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇹🇷
زلزال بقوة 5 درجات يهز مدينة ملاطية التركية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/83846" target="_blank">📅 07:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83845">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQZHc9R9g3poRW0HNeyWNcE1Uwk-a4y85jzYyPRD38uCsZtc5F115Z7ADBSmuAEV1rhBzkfZgU6yAzzMPt3l47z0k2op26Xjq7ukrYrDbab3EipB79G4VU7v9hwGY0eZEeafu85j-pf8uKI7Oqr__J37r4EkSnT1IvRdf-3X3rZCDbIMOCvfmGQSko2MCdOlXyJsnrqrcsAz8dYolHHSnnSdTQsHsv_oX0b9dfa5-PK6KWCFWyz66A87_LMvYFV3rcN_I6yPRFa-iflsk8e8koxS5tLGe8rth_bgCHnC9VwGXBQql26G7Mu-CWpgHJQuuddy3Y5kG_MTCchEVMdCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
طائرة الإنذار المبكر أمريكية تعود إلى قاعدة الأمير سلطان الجوية قبل قليل بعد مشاركتها في العدوان على إيران منذ 28 فبراير.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83845" target="_blank">📅 07:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83844">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هجوم صاروخي للمرة الرابعة منذ دقائق يستهدف البحرين</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/83844" target="_blank">📅 07:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83843" target="_blank">📅 07:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83842" target="_blank">📅 07:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83841">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83841" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83840">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83840" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83839">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.5 درجة على مقياس ريختر تضرب مدينة بندر خمیر في محافظة هرمزگان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83839" target="_blank">📅 07:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83838">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9s_W1TxxiFI9N7uDsVb_mz-fNUH6jQtR40qE3c-WfBIcym33JJK-tPUI9OpHHknsBSIk-MZ7uSbCM_Zkb7P52necGJ5LkdmfzTnzMYVc28oBcMLc5NtGJ-H1NonmjuzLzGXzeMaATYta4revdjdo2jk1uXNEcMYPzSoktP-cpSC2ebsT43jXzvPyOVhM2RtlTPZqKl-px-Kg43TfLe5fA2PCWXMzg1MWMPiLLohzLwlWJqwgRwbtvsxOVIk3YpT-ukS4NX_HRF-2SOtkVIFkfy-RGdV2A_YmIjeaWdhNKGMt1d9mXOXKc_SmWiFtYJsNTcapAJ_BzggZK_RSXEKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار تصاعد أعمدة الدخان في الكويت جراء الضربات الإيرانية الأخيرة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83838" target="_blank">📅 07:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca3d60dc1.mp4?token=smUDdXtFgGHpsAAavqS1V1CpKydEvYDuIP3ch5vN-EsVeS660D0a5BcJa4XHVO1Kp0gigfly3f3-aL-_TBeyNn7CivGVwGl3sUz2x7YQNAEIiEHT9jEpIpgDD46SNWS4277tQzEq7X8QV-hDcDC1hGr1s7XJz0UsuJQ7sqAEwnKWYf4pxumPJPH_JWTLZLb79C5nojBzsRyQ-Ewphm0cycUUu0HOMNdSB7b8RRm1VYKp5nlyC_MrfJ6Xvh5P9ECG_xKR0X6bPpFm6mUDTeffeViWi08wVrDSf8N0aIujGWxc1tv8Xtt1LAFqn9QfarRwPuJWjfJ7Q1TJZWo3n15ZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca3d60dc1.mp4?token=smUDdXtFgGHpsAAavqS1V1CpKydEvYDuIP3ch5vN-EsVeS660D0a5BcJa4XHVO1Kp0gigfly3f3-aL-_TBeyNn7CivGVwGl3sUz2x7YQNAEIiEHT9jEpIpgDD46SNWS4277tQzEq7X8QV-hDcDC1hGr1s7XJz0UsuJQ7sqAEwnKWYf4pxumPJPH_JWTLZLb79C5nojBzsRyQ-Ewphm0cycUUu0HOMNdSB7b8RRm1VYKp5nlyC_MrfJ6Xvh5P9ECG_xKR0X6bPpFm6mUDTeffeViWi08wVrDSf8N0aIujGWxc1tv8Xtt1LAFqn9QfarRwPuJWjfJ7Q1TJZWo3n15ZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من دويلة الكويت المطبعة باتجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83837" target="_blank">📅 07:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">إطلاق صواريخ من دويلة الكويت المطبعة باتجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/83836" target="_blank">📅 06:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سقوط مباشر للصواريخ الإيرانية داخل المصالح الأمريكية وانفجارات مستمرة فيها</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/83835" target="_blank">📅 06:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات مستمرة في سماء البحرين</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/83834" target="_blank">📅 06:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/072ab78971.mp4?token=cxjp59hzS16G7rrrcVkaC60-EFofvahNszDZ6RVN57PShvq64BMYL9UK6bBmIC6F7gd00OEmoYWxAl4-s8FysNSsb4GHke5xlyJE-py6QMj3NsjLraYzeqc9bS5XOiiQDieuatU5ToEk6NN61T8migAdlntsOfFgb-bxCYUmh0UDiRqXF0kUvAFoUxa_zGb1blNBqjMFVWpMxPPwo780aXYM0xm7m3tiu5f_K0RCyv3rSVFjEm5m3scGDAQwOPs9oZJv4JKY7cx6B0xO4snS3nh0rXyh2ZpLd4fC8ws3UEgmmr4ZMUnKwTunKuHL8hJCnG26D7GIHlaKHSDms1q7Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/072ab78971.mp4?token=cxjp59hzS16G7rrrcVkaC60-EFofvahNszDZ6RVN57PShvq64BMYL9UK6bBmIC6F7gd00OEmoYWxAl4-s8FysNSsb4GHke5xlyJE-py6QMj3NsjLraYzeqc9bS5XOiiQDieuatU5ToEk6NN61T8migAdlntsOfFgb-bxCYUmh0UDiRqXF0kUvAFoUxa_zGb1blNBqjMFVWpMxPPwo780aXYM0xm7m3tiu5f_K0RCyv3rSVFjEm5m3scGDAQwOPs9oZJv4JKY7cx6B0xO4snS3nh0rXyh2ZpLd4fC8ws3UEgmmr4ZMUnKwTunKuHL8hJCnG26D7GIHlaKHSDms1q7Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طائرات مروحية من نوع اباتشي في سماء البحرين</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/83833" target="_blank">📅 06:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83832">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات عنيفة جدا في سماء البحرين</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83832" target="_blank">📅 06:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات عنيفة جدا في سماء البحرين</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83831" target="_blank">📅 06:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83830">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cca7edcf2.mp4?token=BxQifaZ-rkNfy-qOuR-FP1aeN9Ryhd14WtxHwEXsDbucdXLLaPpA4-dd2TzIjsC-i3uq340RlN9fouYXyOkGw-MkrLMMoRhqBjCPCpMLeAcnJzOUXIMMGchB-MPtsaq-5CStBWqxgJ7Bfy5CXZ3KUreXwklmc_MvtIBYKhweMZ0PQGZERxeanOWiK0hr9-f8ARif4brSF8sepSKfgJ-uPk73PlILISPqkPGIvJ1kNbXOTR-t9ieIT-Gl5ZIUHzORmhD58Mi60Cy0VH4qAEw2elON3BmPFqqxcOQe7wktWv_zp-TUF-RbSwXQljjtkmI2bmrfAQjl6GYLCvpNk6mdhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cca7edcf2.mp4?token=BxQifaZ-rkNfy-qOuR-FP1aeN9Ryhd14WtxHwEXsDbucdXLLaPpA4-dd2TzIjsC-i3uq340RlN9fouYXyOkGw-MkrLMMoRhqBjCPCpMLeAcnJzOUXIMMGchB-MPtsaq-5CStBWqxgJ7Bfy5CXZ3KUreXwklmc_MvtIBYKhweMZ0PQGZERxeanOWiK0hr9-f8ARif4brSF8sepSKfgJ-uPk73PlILISPqkPGIvJ1kNbXOTR-t9ieIT-Gl5ZIUHzORmhD58Mi60Cy0VH4qAEw2elON3BmPFqqxcOQe7wktWv_zp-TUF-RbSwXQljjtkmI2bmrfAQjl6GYLCvpNk6mdhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">6 انفجارات سمعت الان في سماء البحرين</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/83830" target="_blank">📅 06:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83829">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">6 انفجارات سمعت الان في سماء البحرين</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83829" target="_blank">📅 06:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83828">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b76b8e936.mp4?token=YM86a9zSAAq8Zk5ReYiOejKJH5VsYAVxReQZtgaQLWwAFqAjLL1ud_q5vYcK9DvSKMiwfk462HkYGkmRV3XIV50V-UK7iZef0vS3nCmffyDlay1zJoa4CYiOxFLmjFQzcmJVd3bG1wzCFAfMwevd9kDZkkxd2Oj2amxxF5ysbZILSI6gPTbrLwnG4wBrk5nYoX8gOc3Y3pbLyaxWcGww7LGKwWVMA-wBZbbciFErHPpy-qo79kC3xfZWiXTvqdOpiUQyo6e4nMhG4xGSZI2g1aPtflqctapWV25sfkNCB99CHq5VqEB9L2HSUVMUIcoPMagaR4-hd1y1BkCY2TgHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b76b8e936.mp4?token=YM86a9zSAAq8Zk5ReYiOejKJH5VsYAVxReQZtgaQLWwAFqAjLL1ud_q5vYcK9DvSKMiwfk462HkYGkmRV3XIV50V-UK7iZef0vS3nCmffyDlay1zJoa4CYiOxFLmjFQzcmJVd3bG1wzCFAfMwevd9kDZkkxd2Oj2amxxF5ysbZILSI6gPTbrLwnG4wBrk5nYoX8gOc3Y3pbLyaxWcGww7LGKwWVMA-wBZbbciFErHPpy-qo79kC3xfZWiXTvqdOpiUQyo6e4nMhG4xGSZI2g1aPtflqctapWV25sfkNCB99CHq5VqEB9L2HSUVMUIcoPMagaR4-hd1y1BkCY2TgHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83828" target="_blank">📅 06:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83827">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/83827" target="_blank">📅 06:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/83826" target="_blank">📅 06:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83825">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeXRuMYMP5uywg4Ye43HYtamVtUGZ5SSrqcr-qX8XGvNtjAoya0iodIud4l9VzzpZwE8H8wJEKNa_y2Xyr6nQycp8SOuHCP-skJ-0FgRSZ5CRYY3smRH8DiMjaOTuXdQBiSCoZxNew1WkkSqeDyKjkz2mkoWQ3w-ZTrb6pf8bsQrCETbFTc21TpHMkh6NXAST9DDOMIzjL-DBVTTLSLqRg42eUpwShUMVpo7OlTNA_42KAQxrknrYkN0ZM7r9iq3WWAogpiq96yq19PbAp1y6ficCfJbW1G3UxQ6uFNLeqbkiXC-lTpaImZYcFifcvjMthSbFeqWSIy8l2vu2_nKAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/83825" target="_blank">📅 06:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjKdQZw2_d4fv1QRW_cES1aJjouH6qISHjP7ZQ5vYZn-hBXLrq8uw5udii08iLos1yWM0QEGAl9Drkyx-X3SL50cZ8nIZpvIBLZK8_S6YMeFu8bwY54L5cnMifUm1s2AIBtFVxcRHQpLkqaH2ilPGZ3W-9JYqrY1LI2EyiZpTa-OX7ShkzRa8mRBHgWZj8ENix_QYF4FRq1HuzDvKzMEtOnZMCJrNXO-6ymPnAM66SDyxhayVtXFn4NwkILP7BoNNtVjveJcSroE0_EbSMq9gGxF_rWGpt5PVFFu1dD7UfrCyMyOQNhDM20PYO9AMaPI-6mfd8uLIUX0AJjzPYoA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مصدر أردني لنايا: وقوع عدة إصابات في صفوف القوات الأمريكية نتيجة الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي بالأردن.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/83824" target="_blank">📅 06:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ecf7cdf9d.mp4?token=bpzTUHErAW2hYldVDKWmb3wXQQTVlT39sg8Biand3CCEvnO79N3fiPR0III8643tafs9iXcYPmr1lYjc2rpkLrzOKRIxDd-281wSo67Z_QmgKZwVyxZthrFqRA-mBPkS1jvEVEynBNF_yKlXPwfkzJrmXVpLyljuzk7Ly7CyY7GxbsrIljl0sUztyWmeZliBMDMPp9lFPEAgRnPI1wGFWskzRkwMt-Ib9yypVvIlGL3hUEs5OhxHX6gfFGBJcvM9pF_SZNwxjsRGnAJrJmxpUk3Jf73kOdFEiEQl0I1avip0WtNs0t-GZOmxwxZwNwmZBIDkVRqytYP9F2eUWbdYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ecf7cdf9d.mp4?token=bpzTUHErAW2hYldVDKWmb3wXQQTVlT39sg8Biand3CCEvnO79N3fiPR0III8643tafs9iXcYPmr1lYjc2rpkLrzOKRIxDd-281wSo67Z_QmgKZwVyxZthrFqRA-mBPkS1jvEVEynBNF_yKlXPwfkzJrmXVpLyljuzk7Ly7CyY7GxbsrIljl0sUztyWmeZliBMDMPp9lFPEAgRnPI1wGFWskzRkwMt-Ib9yypVvIlGL3hUEs5OhxHX6gfFGBJcvM9pF_SZNwxjsRGnAJrJmxpUk3Jf73kOdFEiEQl0I1avip0WtNs0t-GZOmxwxZwNwmZBIDkVRqytYP9F2eUWbdYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/83823" target="_blank">📅 06:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عدوان أمريكي على محيط ميناء جاسك في جنوب إيران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/83822" target="_blank">📅 06:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">لحظه اصابت موشک ایرانی به پایگاه آمریکایی موفق السلطی در اردن از زاویه‌ای دیگر.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/83821" target="_blank">📅 06:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله أكبر
موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83820" target="_blank">📅 05:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات في البحرين نتيجة هجوم إيراني بالصواريخ البالستية والطيران المسير الإنتحاري</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83819" target="_blank">📅 05:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز الكويت وصافرات الانذار تدوي مجدداً</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83818" target="_blank">📅 05:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09fc0cbfc9.mp4?token=Bjipqqbwgjlbmf15r-0ouiony96i23uBnGM1B_GiqYl8IZFuB-sOGjhJqpBMNnVs87P_nZJB6ELlIIKnxcEmEC_WsD3g3lW5-QDEIDB4iSKHCgPM6AyoksZtPMpUwtwL7vqqgaSkrWC73LeklV1AeCyaJbQAHht5IX_1wlGKlnO9j6OHyaf5NgqEQ1I-CqfRbN0jo9oT_xY2B2JwFeRvGRHS8JmwV5oDSOj6oXDhom9bh-XVJhF-ymkN5zMkO7QjhPjyVDRWrKFnRgNXWVpYSFblk0ZBFz2m4-JVo3s2SQ1iLOMENeMc1z0Fw3SIvGSPpRY5NVOB3t0RqsN6Sa50ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09fc0cbfc9.mp4?token=Bjipqqbwgjlbmf15r-0ouiony96i23uBnGM1B_GiqYl8IZFuB-sOGjhJqpBMNnVs87P_nZJB6ELlIIKnxcEmEC_WsD3g3lW5-QDEIDB4iSKHCgPM6AyoksZtPMpUwtwL7vqqgaSkrWC73LeklV1AeCyaJbQAHht5IX_1wlGKlnO9j6OHyaf5NgqEQ1I-CqfRbN0jo9oT_xY2B2JwFeRvGRHS8JmwV5oDSOj6oXDhom9bh-XVJhF-ymkN5zMkO7QjhPjyVDRWrKFnRgNXWVpYSFblk0ZBFz2m4-JVo3s2SQ1iLOMENeMc1z0Fw3SIvGSPpRY5NVOB3t0RqsN6Sa50ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
المسيرات الإنتحارية تشق طريقها نحو القواعد والأهداف الأمريكية في المنطقة</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83817" target="_blank">📅 05:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83816">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انفجارات تهز الكويت وصافرات الانذار تدوي مجدداً</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/83816" target="_blank">📅 05:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83815">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
الأقمار الصناعية تظهر إندلاع حريق كبير في قاعدة موفق السلطي الجوية الأمريكية في الأردن عقب إستهدافها بعدد من الصواريخ الإيرانية. يذكر أن القاعدة تستضيف قوات وطائرات أمريكية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83815" target="_blank">📅 05:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83814">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff98f4a6d.mp4?token=n9_WO6qnty7utHnmqC7tALSDtWwNUA9mneHGDdM7qZsFWdPANx6V4OuCXNbq97VX8qwJ02gT91_J3UgJkiazAcNBg98uYpqypSZ-Tvwg2tueIX_XotoZsRbg0KdVhR0kLh6vUUKkS9DsJxGkLS3JD3qRPcGI0-NihR4syZRcw9z6V9oQ6tHwvgCbI7qCaES95ToVWoiq_Ps0eU2QlVFwyMENeo3fY3UW8s--W-bLI-di3oY2kCAjmtpx_pe9UpbyDa9YHh_tDZIIuuIWxDRW-fg6grkDE1_yr35Uy4okDM3Q2zicGB7Usf8rNg594sm6UxuL5RwqbRVcRO2Q_-EkO1ma3JFMQFo23J5K55P2K8Z3C1UXhkjzBn5SwI3-LTroXLRncmjFMnVPjW69FWGiOwYf-pN14S1iJEHXUDU7TLuAOm_pLhNtF4SntSVtcETdWngMWEDtX308a-ffCZzaQQegH-gYbeMLHCwP6A0u6ctn8AuwqvzHsEXG3cvYXxZ3T_uXXFLoAqWK9Hexjaq_PEToa19rf8g41bBo5-BnMZVfmQ2t8ec1G4Qkg2F5XrDBkCWb_7NQbeYrFo29cSIFZzITZY9lPIett1NMSZfP_-Mo-osadiADJOIJt-GcI-N5xhdwOsV9vjuRjmR7aOzX643lEph64oR4UiyoIGxXglg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff98f4a6d.mp4?token=n9_WO6qnty7utHnmqC7tALSDtWwNUA9mneHGDdM7qZsFWdPANx6V4OuCXNbq97VX8qwJ02gT91_J3UgJkiazAcNBg98uYpqypSZ-Tvwg2tueIX_XotoZsRbg0KdVhR0kLh6vUUKkS9DsJxGkLS3JD3qRPcGI0-NihR4syZRcw9z6V9oQ6tHwvgCbI7qCaES95ToVWoiq_Ps0eU2QlVFwyMENeo3fY3UW8s--W-bLI-di3oY2kCAjmtpx_pe9UpbyDa9YHh_tDZIIuuIWxDRW-fg6grkDE1_yr35Uy4okDM3Q2zicGB7Usf8rNg594sm6UxuL5RwqbRVcRO2Q_-EkO1ma3JFMQFo23J5K55P2K8Z3C1UXhkjzBn5SwI3-LTroXLRncmjFMnVPjW69FWGiOwYf-pN14S1iJEHXUDU7TLuAOm_pLhNtF4SntSVtcETdWngMWEDtX308a-ffCZzaQQegH-gYbeMLHCwP6A0u6ctn8AuwqvzHsEXG3cvYXxZ3T_uXXFLoAqWK9Hexjaq_PEToa19rf8g41bBo5-BnMZVfmQ2t8ec1G4Qkg2F5XrDBkCWb_7NQbeYrFo29cSIFZzITZY9lPIett1NMSZfP_-Mo-osadiADJOIJt-GcI-N5xhdwOsV9vjuRjmR7aOzX643lEph64oR4UiyoIGxXglg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة مستمرة في الكويت</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/83814" target="_blank">📅 05:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الصواريخ الإيرانية تصل إلى الكويت والانفجارات تهز قاعدة علي السالم الجوية.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/83813" target="_blank">📅 05:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83812">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رشقة صاروخية إيرانية تنطلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/83812" target="_blank">📅 05:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/83811" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/83810" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oglB3nzbI0QjErkqDgOfsQ71HUixcKzfDtFbemd7jffXq-p1OMZXlBU4F1O9rMBwS6gYaaZzX5M2tRUH-Oiesuc_hD5cXl0VQLzFWxiZgr8Y2SHX03dy2hAsYNpBE3q2XkCpDZ4IwVFA-YalAx-7iLgClWtezw-02gnqtyRRLt10htsQrQvjJDp670Bj1lIq4EuahC57Isn7vNlZgwrVrozY7r8xG9XK1X9cLImrM7KwSEdNUoWzneorsWs-fMK6UEHG8V_9lztCLLOtsuHAa_DFgpoirDNN8WnKLUvL-drO3MpMMvM9VUEpuVg5qEHGgtAlJWIKjQzAvHGKbgkCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه اصابت موشک ایرانی به پایگاه آمریکایی موفق السلطی در اردن از زاویه‌ای دیگر.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/83809" target="_blank">📅 05:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56dc8ee8e.mp4?token=fHwZqdt8S3icvRQVWWXhTvLpK4jCp7h6m85WVontGoaGU8cNpMAAwOwwpjYwgxeDat09xEOVSqjyrhtkSmOiFrC4Yby_hYRT8RV3nDoXmWvU4PBBJLsnoCpQG8yjcPsalGCy5nssKwaW3XWERkJ_cObXyIPWNjves6vLWRPy_jZRXEEQOPo3voJTXcFhyb6jtCtFaJZBuo-HUTv-0RbS_sFr8zIoZnMkWPvF3bv2LzNlr3woggOIoCrAMP6IPvcNno33GJt9kihu0q-fNVbNy5gb18LRI3j_4QXVFw7u0kHJRSk3ug3TPsdgDQ2hXO1sKWkV6K0SsM1_CyzIZvSZIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56dc8ee8e.mp4?token=fHwZqdt8S3icvRQVWWXhTvLpK4jCp7h6m85WVontGoaGU8cNpMAAwOwwpjYwgxeDat09xEOVSqjyrhtkSmOiFrC4Yby_hYRT8RV3nDoXmWvU4PBBJLsnoCpQG8yjcPsalGCy5nssKwaW3XWERkJ_cObXyIPWNjves6vLWRPy_jZRXEEQOPo3voJTXcFhyb6jtCtFaJZBuo-HUTv-0RbS_sFr8zIoZnMkWPvF3bv2LzNlr3woggOIoCrAMP6IPvcNno33GJt9kihu0q-fNVbNy5gb18LRI3j_4QXVFw7u0kHJRSk3ug3TPsdgDQ2hXO1sKWkV6K0SsM1_CyzIZvSZIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
تامبا، فلوريدا - أنهت القوات الأمريكية الليلة السابعة على التوالي من الغارات الجوية على إيران في 17 يوليو/تموز الساعة 9:30 مساءً بتوقيت شرق الولايات المتحدة.
استهدفت القيادة المركزية الأمريكية (سنتكوم) مواقع مراقبة، وبنية تحتية لوجستية عسكرية، ومخازن أسلحة تحت الأرض، وقدرات بحرية. واستخدمت القوات الأمريكية طائرات مقاتلة، وطائرات مسيرة، وسفن حربية، بالإضافة إلى أصول أخرى.
وتواصل سنتكوم محاسبة إيران بتوجيه من القائد الأعلى للقوات المسلحة، مع فرض حصار بحري كامل على الموانئ الإيرانية.
وينتشر أكثر من 50 ألف جندي أمريكي في جميع أنحاء الشرق الأوسط، وهم على أهبة الاستعداد وجاهزون للقتال.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/83808" target="_blank">📅 05:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">إطلاق صواريخ من الأراضي الكويتية تجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/83807" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">إنفجارات عنيفة و‏دوي صفارات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83806" target="_blank">📅 04:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">إنفجارات عنيفة و‏دوي صفارات الإنذار في البحرين</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83805" target="_blank">📅 04:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6d561a6a.mp4?token=RykcnyfxybzqoRRAlESjyi0S3hOA8UVJRlRnHuCvo6yk_S1MnUDypF52HwBVI-PLYTFxWNvzCNHfFUsnDxzm-vUE-I2MtDTWDkW0ABXKX-VUXoPFaYPPcGWBHymbwoXK84ey120EpD_W7xIO9V29iC-Ls8HbafUWMOr4lYTwXGUJR2pFFbT9DhMwJnG4mt4AxlQkzXFcALd4aEhP1XfkS780e2xCU2OZx3DOvqOH1ROgtmO7Pe3isWQzeV3v_x1y1tLvT32WSxtjoTDI3F9byVMizfGtmiZkhk-rkkoANme8f1cZYOyl1gtS_e5CQTMeg35kN1KZTBZvbVM8d45PVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6d561a6a.mp4?token=RykcnyfxybzqoRRAlESjyi0S3hOA8UVJRlRnHuCvo6yk_S1MnUDypF52HwBVI-PLYTFxWNvzCNHfFUsnDxzm-vUE-I2MtDTWDkW0ABXKX-VUXoPFaYPPcGWBHymbwoXK84ey120EpD_W7xIO9V29iC-Ls8HbafUWMOr4lYTwXGUJR2pFFbT9DhMwJnG4mt4AxlQkzXFcALd4aEhP1XfkS780e2xCU2OZx3DOvqOH1ROgtmO7Pe3isWQzeV3v_x1y1tLvT32WSxtjoTDI3F9byVMizfGtmiZkhk-rkkoANme8f1cZYOyl1gtS_e5CQTMeg35kN1KZTBZvbVM8d45PVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من الأراضي الكويتية تجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83804" target="_blank">📅 04:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عدوان أمريكي على محيط ميناء جاسك في جنوب إيران.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/83803" target="_blank">📅 04:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f084436.mp4?token=f6MyuPFqdd_XwpR58YPJYBF9xEcbhcoCuHl7icCGSL1qM2f9wkZbSUJdQ4h9cTw82J4S9mVkVYWbcYghjJM08Z99bCzwtR7iMni92iDU8fByAG0819aKK3Awxf7gMvEhdAIxGZmQNOhzXU_1nG6Y_jAGQnQfyxd2aTn8-QRUSOOd_RVF_kUUiMlm5GywLmnn6bcQNj3Y8t4TMjVFtUzFO1xtCU7VUCg_wDtolp4Qw-dFwJDqc_kxP-0FwgtSmh6_ZHMTiKlnxNnJEGFPdUeyqDCb8du7DcCR8kEV4VNr2lB1DDpobIrwyWDNpaBVIQrWN-pUMiMRXZYHmkP1BBBajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f084436.mp4?token=f6MyuPFqdd_XwpR58YPJYBF9xEcbhcoCuHl7icCGSL1qM2f9wkZbSUJdQ4h9cTw82J4S9mVkVYWbcYghjJM08Z99bCzwtR7iMni92iDU8fByAG0819aKK3Awxf7gMvEhdAIxGZmQNOhzXU_1nG6Y_jAGQnQfyxd2aTn8-QRUSOOd_RVF_kUUiMlm5GywLmnn6bcQNj3Y8t4TMjVFtUzFO1xtCU7VUCg_wDtolp4Qw-dFwJDqc_kxP-0FwgtSmh6_ZHMTiKlnxNnJEGFPdUeyqDCb8du7DcCR8kEV4VNr2lB1DDpobIrwyWDNpaBVIQrWN-pUMiMRXZYHmkP1BBBajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من إيران نحو القواعد والأهداف الأمريكية في المنطقة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83802" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7e23eb44.mp4?token=gJguCDP-Vzn3jhccuEJoob8IA_1YP2XdNYYORMcPw-cFOInUj5yLFcD_REBC8r8GA2S9sXuowjskhZm-NJZ4HCCMdqXc9lRCkPvRgW5FpnWxAjMcI6iZgSCHzob7VrVKy0NcIglJkdtzT9kN6L1U82zXlMPtyumVraRAPiG6GnJBWTAOU4VaUyPYHQ3v5IQK4cWmgXzFCoRjw0qvz3uhJ6GKsGim6M4AgQD5m-LrEdZRSCWi7EWTUMRXD8NvDzkD53h_sSXqCS_sneYOz-CridBo23YbtY1XNIq_DwEdp-vHcpXxcZDQzuy5q14lUi3mdoSpXXsMdmkd6ZtnjufWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7e23eb44.mp4?token=gJguCDP-Vzn3jhccuEJoob8IA_1YP2XdNYYORMcPw-cFOInUj5yLFcD_REBC8r8GA2S9sXuowjskhZm-NJZ4HCCMdqXc9lRCkPvRgW5FpnWxAjMcI6iZgSCHzob7VrVKy0NcIglJkdtzT9kN6L1U82zXlMPtyumVraRAPiG6GnJBWTAOU4VaUyPYHQ3v5IQK4cWmgXzFCoRjw0qvz3uhJ6GKsGim6M4AgQD5m-LrEdZRSCWi7EWTUMRXD8NvDzkD53h_sSXqCS_sneYOz-CridBo23YbtY1XNIq_DwEdp-vHcpXxcZDQzuy5q14lUi3mdoSpXXsMdmkd6ZtnjufWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  من الهجوم الصاروخي العنيف الذي دك القاعدة الأمريكية في الأردن وسط فشل تام لمنظومة الباتريوت.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83801" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات في بندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83800" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxG6J-G0Fvb_JVGHIWfHnyeKsW1CkOO6ZqX8dg6DLWbzSN2_QT49g_zRtoSpR2gLRksU8USsBgJLM4Mr2gnqhEh_SQIIeTUcv0lZiWx3HM_oPkAdIco_vf4S4QWeNnv_oYn2yuVjpYDwwD4V2m6kBC-QLT3MS7JhqEDaR_OVFFQUhASpnq-vWso2ou5mTFH6hB_pnh9ok7gHw2Puj_MmJ1Hy-FMpkvbt8hJ30V0rOrX8TkdCOfNZmYi-DoWb9mmPQYgMJhVf1dizKDmr5WuD8sOQD-HhTjhJl-QICCnbncKsT5uK6-yj7giEfxJjGQcPeCHDN4CxM6xtYErTI_NezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83799" target="_blank">📅 03:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83798" target="_blank">📅 03:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83797" target="_blank">📅 03:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1009bdb1ce.mp4?token=UCtcxHbiHO9kWdnIais0rU7E021DK7xKMfJu8Vb9VNFKA0A56wgNvpNZfbyLIEq3YwE4M_Lrcst-kHXY7XD881p0bN8kVUD5xnNY6PBAVXKEoyJrnnTcn5yMm5reqZqnMBYtKUO2ZstoUc1m-Qxjf5B5YlKxrauzB88RkMjXQ3kNKBROtfOtWyP_McHXL1YaigotrDndvT2fiwYYzfsKs9BwYxhtjf3YYebvzmalylSGwnMQa7vtKSAo7eb1gMHEcCDJM3HsjxpJyGd4Z1h4UKMK0vU1ZCHy1UVMCG2LDkHHIf1AQ2WWQ_hlu0tHaQuNhwOg0vDGHEDCHHFBTPqjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1009bdb1ce.mp4?token=UCtcxHbiHO9kWdnIais0rU7E021DK7xKMfJu8Vb9VNFKA0A56wgNvpNZfbyLIEq3YwE4M_Lrcst-kHXY7XD881p0bN8kVUD5xnNY6PBAVXKEoyJrnnTcn5yMm5reqZqnMBYtKUO2ZstoUc1m-Qxjf5B5YlKxrauzB88RkMjXQ3kNKBROtfOtWyP_McHXL1YaigotrDndvT2fiwYYzfsKs9BwYxhtjf3YYebvzmalylSGwnMQa7vtKSAo7eb1gMHEcCDJM3HsjxpJyGd4Z1h4UKMK0vU1ZCHy1UVMCG2LDkHHIf1AQ2WWQ_hlu0tHaQuNhwOg0vDGHEDCHHFBTPqjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر أردني لنايا: لم يتم صد أو إعتراض أي صاروخ إيراني خلال الموجة الصاروخية الأخيرة التي أطلقت نحو القواعد الأمريكية وجميعها أصابت الأهداف بشكل مباشر.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83796" target="_blank">📅 03:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">إستهداف قواعد الأمريكان في الأردن من زاوية أخرى</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83795" target="_blank">📅 03:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nycoItEXpgrMds4hE9uNvrJDjgVES0vNQCwC1-1FHsTkePsDwaM4-jreFJoOYTT7luvtuNvzjoq45OfxRlbkR8kvIJcHzWszNXoDBM3QMll8DsA_MVjHqQ-5BmrdiiaKX3Sp12xtDE00wtq78wyARl6GgOVrZtNSlz-eYzS6ufPavmnMm1zFLB3nufvk5LfcVbi1LsMHVOK52vQvJJtGs4XiERzWbQfc9HKB9_GgWPOm51WVEOmcXEtsNmpDYkQkKFWFUN0T7kFJkwwUK1zaDqmwyf1rrsqxQZWVjXVnmb5qXp05h6jwXONSe9VjSGfPV_YyQFZMl8isgdfc4e2eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83794" target="_blank">📅 03:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9785ba849.mp4?token=p3Nv3CESx5EpjglcaujkmIf08YpcVq42Jk4s-XhuKk88ABVPD-1w3KzI7h7aMkmEJRvMg0Mv28gUdhk_qWiK4nWPVct2tSO3-yOYO1h-cfhoZL8Phd3qBTtHPhE9JiPEpiqIio8Qbkth6SL81O1vtw1ma8TgrxmQrUu4equNSXUiSGHBbr9-xwmjLkK7omTd0xSfmhjXuykknonPtMreEYnuBjszJWPIJvBU_5PiKQLrJCYJLcvV7hwgXfEkSqnP8kmEkT7KMZpAPTbxY6rnoosTFNGSIhntSuVCmzkuVSXeLvfmDh9votS6GsG5m_3TTEGh_LRAdVkk9FaMVKIA3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9785ba849.mp4?token=p3Nv3CESx5EpjglcaujkmIf08YpcVq42Jk4s-XhuKk88ABVPD-1w3KzI7h7aMkmEJRvMg0Mv28gUdhk_qWiK4nWPVct2tSO3-yOYO1h-cfhoZL8Phd3qBTtHPhE9JiPEpiqIio8Qbkth6SL81O1vtw1ma8TgrxmQrUu4equNSXUiSGHBbr9-xwmjLkK7omTd0xSfmhjXuykknonPtMreEYnuBjszJWPIJvBU_5PiKQLrJCYJLcvV7hwgXfEkSqnP8kmEkT7KMZpAPTbxY6rnoosTFNGSIhntSuVCmzkuVSXeLvfmDh9votS6GsG5m_3TTEGh_LRAdVkk9FaMVKIA3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تمر بسلام نحو القواعد الأمريكية في الأردن وتصيبها بدقة وبشكل مباشر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83793" target="_blank">📅 03:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b58dee1b.mp4?token=SUpqWJ8JgkEs56j-6p9xw4g2GBZ0nU1B8sanHN23BSYtvobSBXNdBBsNcfVLjXYWt28-8IXyUi1nZKAqmFT9QXpGjhAo8m1SProgXsBS7uglhoqpJx0PCF-ZEhp_QWsZBYw_qGqlyFH_-LNChktg0md6UAUIm5PBHD42TQByVdJ1Ejd1gU4rkSB-vkgTajCFnsJlErIwwgioEzEe42crSm_-sLxZxAbyxT0aSCL5KliQcLzVa2btfhRrWLWV9HOw4gUg99fHxQn5rXt3_b9dFxcM5sImPYJca05z89uEO9Bw1IsgkFkqAqjI7vP7XBkWxwhrWQIuloU9sxSv_6dOnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b58dee1b.mp4?token=SUpqWJ8JgkEs56j-6p9xw4g2GBZ0nU1B8sanHN23BSYtvobSBXNdBBsNcfVLjXYWt28-8IXyUi1nZKAqmFT9QXpGjhAo8m1SProgXsBS7uglhoqpJx0PCF-ZEhp_QWsZBYw_qGqlyFH_-LNChktg0md6UAUIm5PBHD42TQByVdJ1Ejd1gU4rkSB-vkgTajCFnsJlErIwwgioEzEe42crSm_-sLxZxAbyxT0aSCL5KliQcLzVa2btfhRrWLWV9HOw4gUg99fHxQn5rXt3_b9dFxcM5sImPYJca05z89uEO9Bw1IsgkFkqAqjI7vP7XBkWxwhrWQIuloU9sxSv_6dOnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تنقض على قاعدة موفق السلطي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83792" target="_blank">📅 03:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a287fd1d97.mp4?token=N8-P-r7PXPqMaqTlmVOG-G4RVqWANNTd1wq0QDiQQpJfcg2hpmcH0l5GyfbuG3W7EC_vWlmms8YAMLge5ZUxtrI9ZSCgj4vMuZv7aUAWH5W0t1X9voORnqhNVUAmwqkKohS7iWthibnm8wsXf23c054QyXaFxy0U2iUvelDWTIaZRFLokTBChYJTa2nI8VjTLclAdZxT8WTkikHZq9WPnKvQIkd2VtkWOaK4cjr9QzE1_P9Ztt25nlBpkH6gfXA8vwxJ2LFKsx2L1Ac0vHKaxsICoAIQpA3Oaj4XPG_DbfFkNBxmMZCigZIZb_bBl5GwiKv9ocNg9DfNEG9sMd8zKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a287fd1d97.mp4?token=N8-P-r7PXPqMaqTlmVOG-G4RVqWANNTd1wq0QDiQQpJfcg2hpmcH0l5GyfbuG3W7EC_vWlmms8YAMLge5ZUxtrI9ZSCgj4vMuZv7aUAWH5W0t1X9voORnqhNVUAmwqkKohS7iWthibnm8wsXf23c054QyXaFxy0U2iUvelDWTIaZRFLokTBChYJTa2nI8VjTLclAdZxT8WTkikHZq9WPnKvQIkd2VtkWOaK4cjr9QzE1_P9Ztt25nlBpkH6gfXA8vwxJ2LFKsx2L1Ac0vHKaxsICoAIQpA3Oaj4XPG_DbfFkNBxmMZCigZIZb_bBl5GwiKv9ocNg9DfNEG9sMd8zKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
قبل ساعات، استهدفت طائرات مسيرة تابعة للجيش، في المرحلة الرابعة عشرة من عملية "صاعقة"، مخزن ذخيرة تابع للجيش الأمريكي المتجاوز في معسكر العدي، والمباني التابعة لقيادة هذا الجيش القاتل، ومخازن الذخيرة في قاعدة علي السالم، وعدد من نقاط الاتصال في الكويت.
🔻
يعتبر معسكر العدي أحد المراكز الهامة لدعم وإعادة تنظيم القوات الأمريكية، كما تعتبر قاعدة علي السالم واحدة من أكبر المراكز لدعم وتنسيق العمليات الجوية الأمريكية في منطقة الخليج العربي.
🔻
وفي إطار هذه الهجمات، استهدفت أيضًا خزانات الوقود التابعة للجيش المتجاوز في قاعدة الأزرق في الأردن بواسطة طائرات مسيرة تابعة للجيش.
🔻
أصبحت قاعدة الأزرق الجوية في الأردن، نظرًا لموقعها وبنيتها التحتية ونشر المعدات العسكرية الحديثة والاستثمارات الضخمة الأمريكية، قاعدة حيوية للولايات المتحدة، تلعب دورًا رئيسيًا في السيطرة على المنطقة والعمليات العسكرية في غرب آسيا.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83791" target="_blank">📅 03:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83790" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83789">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عدوان أمريكي غاشم على جزيرة لارك جنوبي إيران.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/83789" target="_blank">📅 03:13 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
