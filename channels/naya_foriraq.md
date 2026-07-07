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
<img src="https://cdn4.telesco.pe/file/CCWQH8JdQhBiELSG3Gt8eck_LSfys4AU2S6FDvPLF6mPK--70lCupGG8V5WPwPQQat7kMkR_UrhGR_AwFDixaVj-QpWdsJdXMsuip243LRcz-0_EWEQ-7iw5JwQpFdzUP9W2-EL_Lc-mVJUucRNOdWHNGm8_tlw--wn5sh6JDbIyLmbwe3ux7UrJrJ7g3i3or-D-GILtrDIMLPNCh4veEQyzX9AfY8PTOOYzrRW8jsRx6wmZob9o6I55CJs71FNu1wx55Ljcn4nUwu8s5SSgru85qusRgNxWNJOI42QdYXNxhEi3RYnPrB708v1k57E5-kYBSyrxTmnWc60FYdscIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-81319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏العراق يرفع إنتاج النفط من حقلي غرب القرنة 1 والرميلة إلى طاقتهما الإنتاجية الكاملة</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/naya_foriraq/81319" target="_blank">📅 14:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gt1bOvl4Tkq5NkMJKqlg0J_g6rf2GZXN45e4haqT-OpaSXa2_6GHJN3d3vgHg10HL1KbsnMWbrvvQ0WK-0IUUN5RSACy5g_EkItSiKRc8SMKL-XJjWVKN5BXjZxlrAFCQBwahIiE8T-0wXrkZqvBurQyo4eNf7GsWegyVkpNNJNXFGNOQjSNQDmwYAwzI3YqA1dp1QZIL9ZcfvTXXvRPN1cHd2ny4cu3ZaVi3FvklQrX-ck6qsNiiNtXrnSSOctBNdPlr3itNVDERXWntifCnK8elmpzKp2-jnNciz2SIFi_LstKOg-KHla45jDOL3rsTCdQuHbLG3QBYVFg0CPqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9xVXQ3xLFzy8fjXSNVpajmKYnpfKXrp_c9gqlvV9rYDmMZ0Xltk0JmnVmWPDoFZGAHfCFmINjL0kERJgzgaRB0uYIYO4zdnBBnDAWEC3nqyB92urbu38jBGj4GJvuXK9Af35P7fupq4lFHQt3UlPQPyitht6QC3Rt7_LrZHg3CXgnh9Rm0w6is0aIAeiw54J98fnzh_ikp3UGERSMS7L9GHPmRWB2WN1AzN3D6stl_jRXy35vy1RRRMIUvyKzZBxsOqTprj6ZHBlMuL2fVOvHcILcCbBbhZH03Tm3PlYp3pL8DVKxbDIQb5CLerp4LZ35ryQBSCqgz3S91LsIyDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6EHHeEwhQNoIwHznEyoNYwIaWanuOqj4no8imXouggOiDn-U6HZ6nuh3ur6zyOGq58FnfIy95SFaVGUG72lgxrcflEQNq5wYWirYF3hko1PxyD2BS6pNuyOjhnG7oxq_KbN6d0B25H723tjwPfvhrclMDHJUwVSlyFiSZOLBMqq1F8o6w-iux-Osmpz70Vgz0Rr0zb4cGg3V2TkTxZRoLvg29qoItpTPDrLDESWYh6YtrgudPuaXbz8N_QR8zGFFUj-iQ04FbCRekNPfPLiWN9eRp0nCkmkwvrBpxD1saoA-OR5qjwnQUJAax4PpECOoMMtIoRAFgswYdjk0g3S7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئيس أركان هيئة الحشد الشعبي يترأس اجتماعا موسعا في كربلاء المقدسة لبحث آخر الاستعدادات الخاصة بمراسم تشييع السيد الشهيد الخامنئي
ترأس رئيس أركان هيئة الحشد الشعبي السيد عبد العزيز المحمداوي اجتماع موسع عُقد في مقر قيادة عمليات كربلاء المقدسة للجيش، إلى جانب مدير مكتب رئيس مجلس الوزراء ونائب قائد العمليات المشتركة، وبحضور عدد من القيادات الأمنية والعسكرية، لبحث آخر الاستعدادات المتعلقة بمراسم تشييع جثمان اية الله العظمى السيد الشهيد علي الخامنئي (قدس سره).
وشهد الاجتماع مناقشة الخطط الأمنية والتنظيمية الخاصة بالمراسم، وآليات التنسيق بين مختلف الأجهزة الأمنية والعسكرية، بما يضمن انسيابية تنفيذ الواجبات الموكلة إليها، والحفاظ على الأمن والنظام العام خلال فترة التشييع.
وأكد المشاركون أهمية توحيد الجهود وتكامل الأدوار بين جميع الجهات المعنية، ومواصلة الاستعدادات الميدانية واللوجستية لإنجاح مراسم التشييع وفق الخطط المرسومة، وبما يحقق أعلى درجات الأمن والتنظيم.</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/naya_foriraq/81316" target="_blank">📅 14:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جيش الاحتلال التركي يسيطر على قمة جبل غارا الواقع شمال شرق محافظة دهوك في اقليم كردستان العراق بعد قيام حزب العمال الكردستاني باخلائها وتسليمها سلميا لجيش الاحتلال التركي</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/naya_foriraq/81315" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-mQqvAwXDD-kEFziOnILLdONhy_UGtE8bwF4IYGVvSIV48x8BZwNUbT6T2k5N7MNkGjy2d3MoiV1QTABUYXHwacxThon23K4u_RTKRBbaAh6gHZHlTDw6XlcLM4-cEK9_q1oOrOT4Vi6ivZPaKurPpmdwV4egoSQmHwcCXvOJY1gwGukrt3_Fh1f1Z8ykq1nlP6U9fbqtNoaYb0QkyF0WMvLcUBiAXpzx0N5id2BcYlOUqh-vTzC0qVYcDL4G8_IENOv0QvYRQkTSBQtFRt9KRdjAT7VK3TXc-KBZqXOaYPdtGKmF7_hlhwsQUpn31dDfjS3nv8-AnFwCmxpraepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
تستمر إيران بتجنيد الشعب العراقي لصناعة جواسيس جدد مقابل مبالغ مالية من 25 الف إلى نصف مليون دولار واكيد حبباااااا بالعرائق.</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/naya_foriraq/81314" target="_blank">📅 13:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5KqtxQpvLRE3z_U7RupOWsZ57jgaTWexFJtCcNsNHuOhEQxyfXzPhUgGsOcYjOA-tIkyKrTZkHDX4gzccwtiT8seGj1-IVXe5KJa6Po22A6gv-SQO0b-GemPrC5tAZFiIZ_2tgnKlQIkAY46g7jqDrZjxtTD0uizNfR6jvnXBNLQLx6lCxhQYW8A7D5SrwYgj8S3bVZILto1WnPn8hp5UfhPPkE38l65WEVOt_Y-SBZ_sS_Ojz94PSnmgicaXm6PsUBRCso0czEwBXKuP3Nm2Ok9Mr3NcGVk_VGvgYh15cJl4w2C94XtDlrCp50e_1HXfA0qofTAyGr9-R-JMmf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس اللواء "إسماعيل قاآني":
المطالبة بتشييع جثمان قائد الثورة الإسلامية الشهيد، والتخطيط المكثف لهذا الحدث التاريخي من قبل الحكومة والشعب العراقي، يظهر لجميع العالم عمق الروابط الروحية بين الأمتين العظيمتين، العراق وإيران.
دعم سماحة القائد الأعلى للشهيد للشعب العراقي الكبير، ومشاركة المرجعية الدينية الموقرة، أدى إلى خوض الشهيد سليماني معركة إلى جانب الشباب العراقي الشجاع ضد تنظيم داعش وأمريكا المعتدية، حتى ارتكب ترامب الجريمة بقتل البطل الذي يمثل الأمتين، إلى جانب القائد الأعلى لحشد الشعب، أبو مهدي المهندس.
تشييع جثمان الإمام الشهيد في العراق، على غرار تشييع جثمان الشهيدين سليماني وأبو مهدي، سيعزز تماسك قبضة الأمتين في مواجهة الفتن الأمريكية، ويسلط الضوء على خط الدم الذي يربط بينهما.</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/naya_foriraq/81313" target="_blank">📅 13:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2f00bb9a.mp4?token=rvoPmQeKgI2kfwWKPjHO5H7Y6CdRp2XPxETKqLSH4uvrg5kfyDlMUlhm6OcbZgOqpkr8NPVYhsYOl1AcCrR2f-6shPLUt43x9KAjxGT2SiJPJJU7xZauScxoI4Q6s6J648wSvb0KagaCBEZF2ZoF-WS2zmi_QpNuM6F5oUijoQpJhJoCZobmk08SUOTmbwnBvCX_DGZDg7RgA1scgSBuPErdMzOCjswL1J2OjUQKhSFP49F_Lt_fh1WSOp_EKkfRTTYOPPXQRlY7GJUXMIDSCgG2GE9u83FRdYHd5iS0pDzh3mUk5_9HomKc5FsD1gllA4dyOcnvy3XHy0J6WtwnVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2f00bb9a.mp4?token=rvoPmQeKgI2kfwWKPjHO5H7Y6CdRp2XPxETKqLSH4uvrg5kfyDlMUlhm6OcbZgOqpkr8NPVYhsYOl1AcCrR2f-6shPLUt43x9KAjxGT2SiJPJJU7xZauScxoI4Q6s6J648wSvb0KagaCBEZF2ZoF-WS2zmi_QpNuM6F5oUijoQpJhJoCZobmk08SUOTmbwnBvCX_DGZDg7RgA1scgSBuPErdMzOCjswL1J2OjUQKhSFP49F_Lt_fh1WSOp_EKkfRTTYOPPXQRlY7GJUXMIDSCgG2GE9u83FRdYHd5iS0pDzh3mUk5_9HomKc5FsD1gllA4dyOcnvy3XHy0J6WtwnVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
انفجار مجهول بالقرب من سجن “الكم الصيني” في مدينة الشدادي جنوب محافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/81312" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
🇮🇶
التلفزيون الإيراني: سيصل جثمان القائد الشهيد إلى العراق اليوم، وسيُشيع غدًا ابتداءً من الساعة 6 صباحًا في النجف الأشرف، وفي فترة ما بعد الظهر بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/81311" target="_blank">📅 12:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
سيل بشري كبير يحيط بالجثامين الطاهرة خلال مراسيم التشييع التي انطلقت من مسجد جمكران وصولاً إلى حرم السيدة المعصومة (عليها السلام) بمدينة قم المقدسة.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/81310" target="_blank">📅 12:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81309">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8966c8cc3.mp4?token=e_sRDRJLpOsNE9YCVe6CBILaK4Q9fCKKifYgtdpUXJepp4pdKk-jGEM5GaLoW-NXby-iBbKrjOgT2HxO92hh64UuMdXX2Hj5H3XOxEfelkkBeVAInm8MjYU5ZQ3Og_IZMXvjmz0ZbePsMSDXTG1Kl_dpH5JHI1a4FE9nD21Vg2DQtiKJI3vplZ3Lbuk7FdYQDvbH-BGCyNgHNYEh48SzzF2_GpckvXAJE_e9zTYRK6jW3NMCy15ZMwcgbXkdAZmRYNj8-mKWQt4vzDduQPNIfm3pKb9rA_ocwd24JQ0ltt-MoUPsXpCWoxLDFbL1BOoswtSbzQJfN8HNZuewiqo8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8966c8cc3.mp4?token=e_sRDRJLpOsNE9YCVe6CBILaK4Q9fCKKifYgtdpUXJepp4pdKk-jGEM5GaLoW-NXby-iBbKrjOgT2HxO92hh64UuMdXX2Hj5H3XOxEfelkkBeVAInm8MjYU5ZQ3Og_IZMXvjmz0ZbePsMSDXTG1Kl_dpH5JHI1a4FE9nD21Vg2DQtiKJI3vplZ3Lbuk7FdYQDvbH-BGCyNgHNYEh48SzzF2_GpckvXAJE_e9zTYRK6jW3NMCy15ZMwcgbXkdAZmRYNj8-mKWQt4vzDduQPNIfm3pKb9rA_ocwd24JQ0ltt-MoUPsXpCWoxLDFbL1BOoswtSbzQJfN8HNZuewiqo8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 قتلى و 18 إصابة من عناصر الجولاني بينهم معاون وزير السياحة "فرج القشقوش" جراء عدة تفجيرات طالت العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/81309" target="_blank">📅 12:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">4 قتلى من عناصر الجولاني كحصيلة أولية</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/naya_foriraq/81308" target="_blank">📅 11:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbe2b156b.mp4?token=MmfegoGc-mQXb90mft44NrfMrAH2795YyiJFj6SWKGn9vIfNriwG_fkuYanN2zkNfa4ihrWxHO1ug6-j5lEFrMkB181-9H1rxfBjYcvtxzrX0eQQ9RUNSebvyR22y1XvbV8jxCN8zST-88gtiD6Mx8HDHlEd0RftknQfRhLoXZTPuBCyy4mb_lQHxzAUZjUt7Z7HPmCtyXUzPTN5fgHQs00KZK9oNOQ8iz104UPqTNGaYzg5MeSy40krKgFER5oI8WmFuJv1PM5J9ngJiuPyvF97btj_RxFA-cKjj1sl2EJ-h7YiPDXYq64NuVsKSaGajJwqHHXyixjAafG8imL35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbe2b156b.mp4?token=MmfegoGc-mQXb90mft44NrfMrAH2795YyiJFj6SWKGn9vIfNriwG_fkuYanN2zkNfa4ihrWxHO1ug6-j5lEFrMkB181-9H1rxfBjYcvtxzrX0eQQ9RUNSebvyR22y1XvbV8jxCN8zST-88gtiD6Mx8HDHlEd0RftknQfRhLoXZTPuBCyy4mb_lQHxzAUZjUt7Z7HPmCtyXUzPTN5fgHQs00KZK9oNOQ8iz104UPqTNGaYzg5MeSy40krKgFER5oI8WmFuJv1PM5J9ngJiuPyvF97btj_RxFA-cKjj1sl2EJ-h7YiPDXYq64NuVsKSaGajJwqHHXyixjAafG8imL35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر مرور موكب الرئيس الفرنسي ماكرون بالقرب من مكان الإنفجار في العاصمة السورية دمشق قبل حدوثه بدقائق.</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/naya_foriraq/81307" target="_blank">📅 11:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced0fc60cf.mp4?token=VbD-FWZ6DuinPzOaBpDK4Wc-eEsexu5IYNoaYjP84ujTpPaCs7AtfQPCmBxk8IMwi4v57iMm8XIIcVMnTCOrj9jkDaU9FIg8LsJwyeu0FSXln4Nohk8fl7IegensPVEKJyO0MoRer8OMazkqn6ZV4LL8MYQtx3gWqEB6RDfbOCNWFozqz2rdCVCk0djEzhEXbhn7Ed_iz-SLlGlcuD8JntLy3Q4Zqw9HUVG6zX9mWjr3_8LCdBWnNbmYac5_VjiXhWKsPBQb9AH0gRcUM_MYi-AXfBd4tGlV4UOVUohq96mn-_SglE2IkdYvzS-N41exIxf_HIUrYFLQN7qCCRAX53EULpiNwjAf8b0j80xT1DNzTNuoztRh84D9IQwkdBVPzIcgUzPdmkn1DU2UmGaMu3KaeHN_tUFZpJs5P8Whuhuz-qLClAYUiJXc_gMQXfow6WKhhn02yJxQKJxodaUnEmrbh0Muhxc4lR525AvVYwfkzGB3D6uRCM__C6qH8eQpm8eKp5xS4tpNiomlz9jFXpCNP_gqAZSeDahpCo6-Ides_CgnfdJopXJj6yRxjESYyZUmjuzZl18uvfOx_-vM2MZJPSXmVezQO55kZN5SBwPyFOd7SaaxMRWlU6-35vA1ZR4s8vsdGXayqPqtAAHA_Llu27ieyDeXuOAYzuGMKsc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced0fc60cf.mp4?token=VbD-FWZ6DuinPzOaBpDK4Wc-eEsexu5IYNoaYjP84ujTpPaCs7AtfQPCmBxk8IMwi4v57iMm8XIIcVMnTCOrj9jkDaU9FIg8LsJwyeu0FSXln4Nohk8fl7IegensPVEKJyO0MoRer8OMazkqn6ZV4LL8MYQtx3gWqEB6RDfbOCNWFozqz2rdCVCk0djEzhEXbhn7Ed_iz-SLlGlcuD8JntLy3Q4Zqw9HUVG6zX9mWjr3_8LCdBWnNbmYac5_VjiXhWKsPBQb9AH0gRcUM_MYi-AXfBd4tGlV4UOVUohq96mn-_SglE2IkdYvzS-N41exIxf_HIUrYFLQN7qCCRAX53EULpiNwjAf8b0j80xT1DNzTNuoztRh84D9IQwkdBVPzIcgUzPdmkn1DU2UmGaMu3KaeHN_tUFZpJs5P8Whuhuz-qLClAYUiJXc_gMQXfow6WKhhn02yJxQKJxodaUnEmrbh0Muhxc4lR525AvVYwfkzGB3D6uRCM__C6qH8eQpm8eKp5xS4tpNiomlz9jFXpCNP_gqAZSeDahpCo6-Ides_CgnfdJopXJj6yRxjESYyZUmjuzZl18uvfOx_-vM2MZJPSXmVezQO55kZN5SBwPyFOd7SaaxMRWlU6-35vA1ZR4s8vsdGXayqPqtAAHA_Llu27ieyDeXuOAYzuGMKsc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق جديد يظهر لحظة الإنفجار الثاني في العاصمة دمشق بالقرب من محل إقامة الرئيس الفرنسي ماكرون</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/naya_foriraq/81306" target="_blank">📅 11:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsqeDZmDNzTC9cxgxNKncP_hzJXcryIdNnCHa00P04fBVeK62ry4BC-hWBk7PBVBf2RXq9-4w0XL7N54WktZKsoekIttnh07PjFa75F7sbnsVWCqB-qXd_SNimB9tefK6QtNudWBAKJTfGNvm7J_Gkdxd_8-9vYV94qmzHBRJ8QP7AqvW_oMujdlFrLCQjIHn9071qT4tXkQ7LlMI0AY6l0DxMr1JrN_hcG7qnDwj4PMtfyS1jpFTBeFhKMpOto6-WjJvR02YQovnp2cjg2s1tv1in00IVSy53XOBYLcijCGi1gTTYqByatlU2v6fK9TMCJnDPUE8UCe85rBlH-pRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توثيق جديد يظهر لحظة الإنفجار الثاني في العاصمة دمشق بالقرب من محل إقامة الرئيس الفرنسي ماكرون</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/naya_foriraq/81305" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2fa73c82.mp4?token=VvtzaUrSczPzhZTbtR7L6Z1fYe_5uVsH7ulocBOWVOk3anHfRlyvip92hfZ93DSbNEspnnlfiiw7QhSq_-6epBsNq0ygijr67y2HAkfIE5b3Q9dB8NYljjFPuVzr7qiAGWoIrFtu-6fpOfkGmAE2tVNwJJWgseJue5mupikSewETZHsKfR3kZ00kY1T2QqEh2pxN8dtaxzZ66IY7LdjnheTljc9OdganU7JAWQ_DJLWjcIBeKXg3Yc9Qngbzo1HtvWKf2pxE3fi4oL7yJnTZUthl0f54i12xZg0x-v44Tg6pPtU6Emn2G_sxwbToIJf-fRb53kdq07-LXY7olVxcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2fa73c82.mp4?token=VvtzaUrSczPzhZTbtR7L6Z1fYe_5uVsH7ulocBOWVOk3anHfRlyvip92hfZ93DSbNEspnnlfiiw7QhSq_-6epBsNq0ygijr67y2HAkfIE5b3Q9dB8NYljjFPuVzr7qiAGWoIrFtu-6fpOfkGmAE2tVNwJJWgseJue5mupikSewETZHsKfR3kZ00kY1T2QqEh2pxN8dtaxzZ66IY7LdjnheTljc9OdganU7JAWQ_DJLWjcIBeKXg3Yc9Qngbzo1HtvWKf2pxE3fi4oL7yJnTZUthl0f54i12xZg0x-v44Tg6pPtU6Emn2G_sxwbToIJf-fRb53kdq07-LXY7olVxcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 قتلى من عناصر الجولاني كحصيلة أولية</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/81304" target="_blank">📅 11:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
مصادر لنايا: يعتقد أن المنفذين هم من جهاز الأمن العام كون المنطقة تم إغلاقها منذ يوم أمس بسبب زيارة ماكرون ؛ حيث يضم حهاز الأمن العام عناصر من تنظيمات النصرة وداعـSh التكفيرية.</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/naya_foriraq/81303" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/81302" target="_blank">📅 11:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
مصادر لنايا: يعتقد أن المنفذين هم من جهاز الأمن العام كون المنطقة تم إغلاقها منذ يوم أمس بسبب زيارة ماكرون ؛ حيث يضم حهاز الأمن العام عناصر من تنظيمات النصرة وداعـSh التكفيرية.</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/81301" target="_blank">📅 11:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81300">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c2d1ac86.mp4?token=RaTUJf9NgOOmvk_jTvqPcK0g2hGmxgczaXigHC0ET0EMIOGeMHCzfKKT5CQr7X-cTS9dDLt6MUTMyp3UUcBc5OBJC_dg9EfUHJ6hcPKlyLjGjbyBTS-r50WJ1A-kbINlfnOwizJC8Sjjzqi2nvF2a3OJzNSanbR54xDaTTuCgHyUGNKvS2H7AqkkCHzo4qBLr6OTrfwDWmPVD_NSsJZhvSHjvDT0WNm64qPvAbstSfjbeaiDto0mkfONjRgALIpT0cP9I4FiRiq3kPpHwsqapiQzHwZr-ZXMXPX7wK0xjnSAJoGRwG7rNeWv1-e7tlBMH6nqqVfE_1DJVvPnBh7frA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c2d1ac86.mp4?token=RaTUJf9NgOOmvk_jTvqPcK0g2hGmxgczaXigHC0ET0EMIOGeMHCzfKKT5CQr7X-cTS9dDLt6MUTMyp3UUcBc5OBJC_dg9EfUHJ6hcPKlyLjGjbyBTS-r50WJ1A-kbINlfnOwizJC8Sjjzqi2nvF2a3OJzNSanbR54xDaTTuCgHyUGNKvS2H7AqkkCHzo4qBLr6OTrfwDWmPVD_NSsJZhvSHjvDT0WNm64qPvAbstSfjbeaiDto0mkfONjRgALIpT0cP9I4FiRiq3kPpHwsqapiQzHwZr-ZXMXPX7wK0xjnSAJoGRwG7rNeWv1-e7tlBMH6nqqVfE_1DJVvPnBh7frA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضع الرئيس ماكرون لا يزال مجهول حتى اللحظة</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/naya_foriraq/81300" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لحظة حدوث الانفجار في دمشق</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/81299" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1453202c0.mp4?token=bwB8-htGx8pueF5m_89v7xR_MLZkdj61nSECVC8kh5WosxxRFiOL3_w1HbR9izIN0vpt086wJzE7IKULSeo9AhOR4r6_ZOUSGJ5NGTotq0jKGs1ANrF7MkMuZQFOut78gaVmn09tFeKeyn-epBsKN_pDFJjdoKSrUDa3s8vCAe-yOqU0Xr4Hj4i45ZWjEDYV1j1Gm6yjbpdY0gEzkpP_uUCiM8PEz1FShdM-qWMswMoqiW9lITwXIDr7FW2_iubRGo-e1X3zcZG6ef0WU0dzRzpYknvm60lIOrK1Krc4_rwCzEI73kKi8Q35gkWyFD99qJNi6LTyG9lCAG7d22lGvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1453202c0.mp4?token=bwB8-htGx8pueF5m_89v7xR_MLZkdj61nSECVC8kh5WosxxRFiOL3_w1HbR9izIN0vpt086wJzE7IKULSeo9AhOR4r6_ZOUSGJ5NGTotq0jKGs1ANrF7MkMuZQFOut78gaVmn09tFeKeyn-epBsKN_pDFJjdoKSrUDa3s8vCAe-yOqU0Xr4Hj4i45ZWjEDYV1j1Gm6yjbpdY0gEzkpP_uUCiM8PEz1FShdM-qWMswMoqiW9lITwXIDr7FW2_iubRGo-e1X3zcZG6ef0WU0dzRzpYknvm60lIOrK1Krc4_rwCzEI73kKi8Q35gkWyFD99qJNi6LTyG9lCAG7d22lGvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاع المدني يستيقظ ويتوجه إلى موقع الانفجار بعد أكثر من نصف ساعة</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/naya_foriraq/81298" target="_blank">📅 11:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06afd021bc.mp4?token=UCVc2oln-Ok96HHfhfYtRjHGbeoJryj-ljqZ9SS2nhFlKea49wgc7l__0QWckPZMLfADeR4efL6gAWpMRGIwVwpePnyAW-YMww0uEY6ms3C2pEP-1KLa2_qcThOYlFoSbpBkZ1T9CHiw8HaQvK3tEJ7rw_vHHsbriOj5YlyNR-_S5dbEvuZB3y1fPgninc1tKUHJNRqGQGjG0Q8-42sLQhRl412gpnPfzlK_EBamwPJfTBTZfz9P_ANK3AWneIYx9MpjgN0vI-Z0r0ctjQ6tOCBQcYbAvlxnTwVvh_J0_WXcG29gLEa4crLd4wq05yfoWyEZOlE3UqdcQPsgqMnt3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06afd021bc.mp4?token=UCVc2oln-Ok96HHfhfYtRjHGbeoJryj-ljqZ9SS2nhFlKea49wgc7l__0QWckPZMLfADeR4efL6gAWpMRGIwVwpePnyAW-YMww0uEY6ms3C2pEP-1KLa2_qcThOYlFoSbpBkZ1T9CHiw8HaQvK3tEJ7rw_vHHsbriOj5YlyNR-_S5dbEvuZB3y1fPgninc1tKUHJNRqGQGjG0Q8-42sLQhRl412gpnPfzlK_EBamwPJfTBTZfz9P_ANK3AWneIYx9MpjgN0vI-Z0r0ctjQ6tOCBQcYbAvlxnTwVvh_J0_WXcG29gLEa4crLd4wq05yfoWyEZOlE3UqdcQPsgqMnt3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة مفخخة في دمشق بالقرب من اقامة الرئيس الفرنسي</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/naya_foriraq/81297" target="_blank">📅 11:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6428c1e9ac.mp4?token=DJHp7zZ5zJ3vEilrtxkytIFh6mgl8sbyFP05E9t1u6qSYLsVFZ5jnQ9OOOxcs-1HvPSLrH2nP3Ng5SKHxO0ql1ZLV25M0N2y0It9p4HYrlp3m0l8zNsjGic__xd9Xg0FWTvODyF6LHbmD-zB6ST53mDikTF1_-leFJUoe0k3n-jJ1pvq6wn0ldAPJG-jEjcfDb411MJhgvws1emiZcwckodClHaWHwK6uPU7WdScYYNf8JoIsByd5-9Qgxysa3ZUHGK9uVzam_R4RKjZD63JNTZorEcpKr60bJZXA2YzZXFS6ijeYqU6fUT0gDhvA550P1YH_xfa5M1i2_Im_Blk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6428c1e9ac.mp4?token=DJHp7zZ5zJ3vEilrtxkytIFh6mgl8sbyFP05E9t1u6qSYLsVFZ5jnQ9OOOxcs-1HvPSLrH2nP3Ng5SKHxO0ql1ZLV25M0N2y0It9p4HYrlp3m0l8zNsjGic__xd9Xg0FWTvODyF6LHbmD-zB6ST53mDikTF1_-leFJUoe0k3n-jJ1pvq6wn0ldAPJG-jEjcfDb411MJhgvws1emiZcwckodClHaWHwK6uPU7WdScYYNf8JoIsByd5-9Qgxysa3ZUHGK9uVzam_R4RKjZD63JNTZorEcpKr60bJZXA2YzZXFS6ijeYqU6fUT0gDhvA550P1YH_xfa5M1i2_Im_Blk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجار طال باص نقل لوزارة السياحة قرب فندق الفورسيزن.</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/naya_foriraq/81295" target="_blank">📅 11:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجار عجلة مفخخة في دمشق بالقرب من اقامة الرئيس الفرنسي</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/naya_foriraq/81294" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4f2e76af.mp4?token=TgCo34HWxx61hupq2g4ioMVXL1fUcVltga8cTjhSF2xOwt4KglfhMTwXnCfJ__aIkc9cYa2uOBMOtr3xJuqYFh5GtkxrbkLR4xrZf2X1-Qi5CjnFs1YYuDeuQTN1BhIJ2laopJdy1yMmJCnGdrt_MvWmTxA4lSZ3eX50f5_MCY7D_XQ_kOdPNk0HA475k6Qu6rOGzKr6jRWu2tfqEP9T9odja7rGkIbGvHGKa3t4PGPteNRGlRenaWOJ2Y8YyhKt6O0iV7nzMznZKiJH8OXBneqeBqRrieRMFRziySfd8rZcKADI-arnJL7RqliqGovt3Vo6Y8Erzz7zD6a5q5zn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4f2e76af.mp4?token=TgCo34HWxx61hupq2g4ioMVXL1fUcVltga8cTjhSF2xOwt4KglfhMTwXnCfJ__aIkc9cYa2uOBMOtr3xJuqYFh5GtkxrbkLR4xrZf2X1-Qi5CjnFs1YYuDeuQTN1BhIJ2laopJdy1yMmJCnGdrt_MvWmTxA4lSZ3eX50f5_MCY7D_XQ_kOdPNk0HA475k6Qu6rOGzKr6jRWu2tfqEP9T9odja7rGkIbGvHGKa3t4PGPteNRGlRenaWOJ2Y8YyhKt6O0iV7nzMznZKiJH8OXBneqeBqRrieRMFRziySfd8rZcKADI-arnJL7RqliqGovt3Vo6Y8Erzz7zD6a5q5zn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضع الرئيس ماكرون لا يزال مجهول حتى اللحظة</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/naya_foriraq/81293" target="_blank">📅 11:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/naya_foriraq/81292" target="_blank">📅 11:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7ZHTexC_w9GA9ZjiZQhKKGqKk0q--hYNka-ePm_GKxRRCGhwBtfWnP7sJ9PKiiQbLhGNiEBs1o9JHdnJuyaDX3q4w9UKLwkAlDcpCYw8i3RM3m16dON_6bHxKh4JpTAM4ircAkUhS0QHnAPUSA7mAftUoOpUr8Wi48Lm0f95ANZ6yX0KQHrE2XWADVmYtPbNV_Rvr4CETj3ySgXU_j8hp1w9Pq3aB4cA0Mtli1FuH7W6D2kXXI10AmZQma680tmiUwVcRu9NYhQNgXbR4EErzFr_n5AlkuwPcCNgFaworCxiLe2sB-mgObvENvbz5lTWi56hO4HLBdAmOcacm9heA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من فندق إقامة ماكرون</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/81291" target="_blank">📅 11:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/272c8263d3.mp4?token=Nr3z6IjoWWgXzeuH4vhWkNuGEPqN4OIzPdHAVGf9s9uBzLivcPbbVC8GQcyhNVbZalF7-lGlIbCH_LwRpEUCY7tDHRn0wcuct9KxDH9tKiomPCILFTybjaE0miukJFHyztlFDAMIOmflKfVzvRWbaGzIyCWetjBk7pDzaDfrnK--A0rUOez75HO1f3aD8lRoTIyZy_yC1t31sh5oP9p4HgUNgWei2n3kD908-6oVytYLQMPJAfTiQmZ3xpf7Nl4_ckxBrTzCTuquTHo6rQ3kHpMu_M0KDUsiqa6Zo9v40rXFyagJn1hJ1Ob-DwSXPXDpEpmZDz8418ZA6rMux87qrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/272c8263d3.mp4?token=Nr3z6IjoWWgXzeuH4vhWkNuGEPqN4OIzPdHAVGf9s9uBzLivcPbbVC8GQcyhNVbZalF7-lGlIbCH_LwRpEUCY7tDHRn0wcuct9KxDH9tKiomPCILFTybjaE0miukJFHyztlFDAMIOmflKfVzvRWbaGzIyCWetjBk7pDzaDfrnK--A0rUOez75HO1f3aD8lRoTIyZy_yC1t31sh5oP9p4HgUNgWei2n3kD908-6oVytYLQMPJAfTiQmZ3xpf7Nl4_ckxBrTzCTuquTHo6rQ3kHpMu_M0KDUsiqa6Zo9v40rXFyagJn1hJ1Ob-DwSXPXDpEpmZDz8418ZA6rMux87qrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من فندق إقامة ماكرون</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/81290" target="_blank">📅 11:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b4513462.mp4?token=EjoAn0Tpq-7WYv-lVTeNIqmOU7NxnDY9iVToTGEng2jJGMeUL2XO8NYzq7lRcmYNFo5U_qpFGrPr87Qs7qknbmITStSxQrUNcnUwIB4bj4IQHY5M71QsP84a0PXEL1vcHmsWzsST0njpJb2GkIStUkihOwWYRKqVzXPmPO4J0KBqpD36XMhKQaQ2BUxIrp_TY-p07YwHFy2LPjLcF8CJTrqm6aZUGb75CU60s6C4zNmNWrKj8qawvY6KOWAnH4glNn7ycU02KNVq7kh1hpZNMngMPCAv4HLw_R9J3e2w2GA6hKSZtc6ZACfH5nCPcmPnJWInyysO-208-WdoctmrfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b4513462.mp4?token=EjoAn0Tpq-7WYv-lVTeNIqmOU7NxnDY9iVToTGEng2jJGMeUL2XO8NYzq7lRcmYNFo5U_qpFGrPr87Qs7qknbmITStSxQrUNcnUwIB4bj4IQHY5M71QsP84a0PXEL1vcHmsWzsST0njpJb2GkIStUkihOwWYRKqVzXPmPO4J0KBqpD36XMhKQaQ2BUxIrp_TY-p07YwHFy2LPjLcF8CJTrqm6aZUGb75CU60s6C4zNmNWrKj8qawvY6KOWAnH4glNn7ycU02KNVq7kh1hpZNMngMPCAv4HLw_R9J3e2w2GA6hKSZtc6ZACfH5nCPcmPnJWInyysO-208-WdoctmrfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الانفجارات التي هزت العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/naya_foriraq/81289" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5ykCLCdgSaVWfiDElGLIYXX23xBK3oS_wIOeuVpn8YA60hqyirhWqQqc7QofH2rDLFCAVXYbsLkiS1bKmveDwsOnX259vmcDvH5bX0dPU8QevM2nNPF-qGTj17j-GfbwAol7-sYVu19RdE4A_QTehIoxzeWoPYQN8EX4ssm-8nt9Shev_Fpt4fcEMc4uqOH2-QD97x_KsD7xJGy3szbi4dW4AKxx68_VACx-lqulqs2FCjvus-Rpj0eZinF9TGhue_BZaCo2QGSVRdjgBsXqjWu5LQYGn3xlD5WYn6HSMpu3HtKx8rn-329OLkrs5gI8cEyqfJG4TprzQAhcmpO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الانفجارات التي هزت العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/81288" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tK_8b-3GyV4H1myL7KzdVatwbMPPYF5cQ3XhKvjEUKAWJDnVtQK5_WTfNuB_nfZQ3zBawqc5n7bT9gNaYhWnQmq1tyUd9USqg8sQ7uXfjL6CiSQy-TYMjTGv6ioJab5fpaWaK2q2kCAjYtUBRt7ZtsSoMSLvesk03x2rSSmrGHPYpg6CFsuyOTudRuE5o6nUfTQIMpaimr8T6alFk7huQVIiRrNT0XUA7ZYofeH0r8SZCjLLXRSkS8Xqzdrrex5nAyCc2lSlq2AjcCjKRAZgLtDgEjUjNn8E6qSrJA2WJsEd4Bzjheb9Z4pXLnOPOgAHg46_7XGT7QCpQ_ZUBpmPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQh_K4JZP0BDOH1H5EbsLm4qyY3n42xG1aeOmyNyyik6hdpudiI-rmqnp7d8lfC4txC9KsphjvsAqBgHSNlg42aJuOROzlUv_5PNvmTkW-Nt7ef5ZoTdePDQ7EKOpYK2RxTHCtrjC0RPLlqySYlnStx8hD9en1aknEZXHPkrqxfLvAHq4D6ym-fmnmpmra1KAjRPlvSzpRtKW9KiG9vaaZdOSoQsXKTEHEEku-lpIku7XsXj06wRaf4VQiCrQegWREkwtoLJBbwd4eJ4_Iz3b00gzR2QwmxpWHqB630-FOvJ0htNKUqDbjTDZaeki-7bi0wvEf7-anKAeClHQm8SsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاعد اعمدة الدخان عقب انفجار عنيف في دمشق</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/naya_foriraq/81286" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae08954e6.mp4?token=OP2Aca2IZ_cCZc0a2CjUiIsSVxCG_omOe4EUF6FU4bmuuv1_IVKkROlbsZ4ftSOm_p36tLI7n0sCp1LHHvr3MgCxj250uZl4tUf4TVlGYFQqw2IHnE6pbCftnQLok_AFOojKaFmTNYnjTmSD-aBN-fC4Oz0IzY8wuYarsQb40_0-6mE4iqYBXz_WQ03SA38ACE4GdbBDAsePERvkI6MRDZv8LQ9zAu4e4eVHQX2-CS3aOd9GwxXd0jiy-4_OQ-3G1CpYeRf5v2h0BMUgO8JNMkmQHPrDLi4aRDH-elgu24jlrzpG6vVtlBcMYs7x4X_sn-0afk26m0U5IPzYe_y7gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae08954e6.mp4?token=OP2Aca2IZ_cCZc0a2CjUiIsSVxCG_omOe4EUF6FU4bmuuv1_IVKkROlbsZ4ftSOm_p36tLI7n0sCp1LHHvr3MgCxj250uZl4tUf4TVlGYFQqw2IHnE6pbCftnQLok_AFOojKaFmTNYnjTmSD-aBN-fC4Oz0IzY8wuYarsQb40_0-6mE4iqYBXz_WQ03SA38ACE4GdbBDAsePERvkI6MRDZv8LQ9zAu4e4eVHQX2-CS3aOd9GwxXd0jiy-4_OQ-3G1CpYeRf5v2h0BMUgO8JNMkmQHPrDLi4aRDH-elgu24jlrzpG6vVtlBcMYs7x4X_sn-0afk26m0U5IPzYe_y7gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجار قرب فندق الفورسيزن الذي يعد أشهر فنادق دمشق ؛ تزامناً مع زيارة ماكرون إلى دمشق.</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/81285" target="_blank">📅 10:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/naya_foriraq/81284" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81283">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/81283" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81282">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOIiTbAOh3XfDTb9lpii4rbb-ws5tP3StHF4KN54kMhjfEEk4w-0eAm6i2eTbwBRPtM4k9hnlA94yAMygAQ_agEoGGi6c55NoscFsD6Z7yytY7TujpA_3bgtJJG9EX41Sbge9v4WPcw0BaTmmgRTSlzVkofYaneXBes1mjTSsQRRhMJ8G69qGSut3z_41pmmYFCEVFD2Nxq9uKhVCFoPmGBX09Iu2Syf2H6lY_uV8V23YYGuhof7DhVkMit4k-1bR-GYY7YCEAfxj08j1jZcDksf08WXYyAY-_IhxM_CW41MibGl9CO_6MsRh7s5_qIb2dBwmseBUTmQ3PGxM_L8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/81282" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81281">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5i3CK9BEa28EzIYXSsIl2I6sPdiWBeRqYO1krfOrwSnkweyuj6aCz8bAi9ZWRP-UvLIIsa2-I7eei4Vnhur2NEI2JTgY6Uo7ZJWbFT18RAulGZLangek7lREgT8GlX36yzCeF2iUmKxlIEqkyEaoSwjtrOnOuRCriwCwttVPepYhs5zK7wcR4jbPqaggBgA1YC2TOWG9cv8YOXHPIRKm-yyCu56BBdbFe8AtKr69hbaBkkFQUjoFuHEcvX52h5qBYXZe-xEYFFn8T4iDEPHcxUMQdkW0fxvGbwiCE_S_vFywksZuozt4JgNXcDuDn81J3XaMlxbrY7XFIhsqYll_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلم الغراوي الكلف
يواصل موكب المقاومة الإسلامية في العراق – حركة أنصار الله الأوفياء في مدينة قم المقدسة قرب مسجد جمكران تقديم خدماته للمعزين والوافدين والمشاركين في مراسم تشييع الإمام الشهيد السيد علي الخامنئي “قدس الله سره الشريف”، في إطار الجهود اللوجستية والخدمية المتواصلة لخدمة المشاركين في هذا الحدث التاريخي.
#قوموا_لله
#تشييع_إمام_المستضعفين
#قائد_الوفاء_وشهيد_الأمة
#أنصار_الله_الأوفياء</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/81281" target="_blank">📅 09:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81280">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37a9d384b9.mp4?token=nCVB5AZGS-tQWdvpqnsVz2dMUej8F9D9o8WMEmMzVFFSetBJYP5aCSRX5LIHYVFoPo0fcQnlaubbf2No3NkmwKFBHAlCFwpUUQbl361QddkP6wTvj34MnkA-l1SdsU7HhdoQAfb2lo2ygETClDXN9oscUXT5KEO0KL3DvX_AHKwKvow-YrdPHV3-9P68R4nxJQbGZPo3_0rhhMS3EopQQYIfPByJGeXmXnE-NWdDCk5JJvaHMLPvtcqWW414Oy4wIPJjh2NIytDV9BIONKzRPpylveNdEAv3LRlGLTpx11qN-X7nKm6Urx3MD1R5U07kQFGNDxXyhEHkVUXRb5KWmz0I8H4tMAUmnR_7cyCyBnq42CB21QocNDuVDLOeo01I3NLAeX5q_TOaRb4Lue-qCoDrBVx-garRTqFmgXQYCKBjjQSf4wtOj205YeaMJjcBBAVC3X0NBm2OgYUa6tBHvtbuKGZvXqW2daYfuxIJInA54NRkyD_2ZS66L5HIvFXgtosm2RwwvxZWPzVXTaCnnOw_E8IoOIvoVcGwHr1Rvmf0YXM4QaLm0Ldoen9D7k8IqJshkQM7QdfS0ZW5rY_EHokxfVbPQ13izuy9HXAEBWTDECCOFa66q5f3Ivg8lai_J3iR8ilvtr8KXtzzXLrc6U_5YcTTpgC6vLtG0hMjWf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37a9d384b9.mp4?token=nCVB5AZGS-tQWdvpqnsVz2dMUej8F9D9o8WMEmMzVFFSetBJYP5aCSRX5LIHYVFoPo0fcQnlaubbf2No3NkmwKFBHAlCFwpUUQbl361QddkP6wTvj34MnkA-l1SdsU7HhdoQAfb2lo2ygETClDXN9oscUXT5KEO0KL3DvX_AHKwKvow-YrdPHV3-9P68R4nxJQbGZPo3_0rhhMS3EopQQYIfPByJGeXmXnE-NWdDCk5JJvaHMLPvtcqWW414Oy4wIPJjh2NIytDV9BIONKzRPpylveNdEAv3LRlGLTpx11qN-X7nKm6Urx3MD1R5U07kQFGNDxXyhEHkVUXRb5KWmz0I8H4tMAUmnR_7cyCyBnq42CB21QocNDuVDLOeo01I3NLAeX5q_TOaRb4Lue-qCoDrBVx-garRTqFmgXQYCKBjjQSf4wtOj205YeaMJjcBBAVC3X0NBm2OgYUa6tBHvtbuKGZvXqW2daYfuxIJInA54NRkyD_2ZS66L5HIvFXgtosm2RwwvxZWPzVXTaCnnOw_E8IoOIvoVcGwHr1Rvmf0YXM4QaLm0Ldoen9D7k8IqJshkQM7QdfS0ZW5rY_EHokxfVbPQ13izuy9HXAEBWTDECCOFa66q5f3Ivg8lai_J3iR8ilvtr8KXtzzXLrc6U_5YcTTpgC6vLtG0hMjWf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بين جموع المشيعين، تسير الجثامين الطاهرة نحو حرم السيدة المعصومة عليها السلام للزيارة والوداع الأخير.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/81280" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81279">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CirxSVA_F17tNnPBfESL9d49vbTdTsZZikicbWCYPoOvXH7ij20KiOC1LNGT3sissQwFm0W4AqUspbYDZXb6Z579edweTdloMQQOHrOk4vyQrUmJsJHmfUi-PttLP6jO_RsPy9a4gnIwGK6bhJOB97NyEChy2vnaf2HXZQ2xzXxtVMQ9DXdLU7g63o2Z69PyoUCjyKlS6g_GAAKWgZsUuPKuhQuPEkWEqBjzy2-Vfuv6cM0P9bLn9UlVZJpFVPLoP1H0Al4QoQdsemdjsarq6Q5Bk1sviUpHDNBqh3U2KYi4JcSjTPTn_UjZ-yaaIx4X4k2If8D7cmaI3GtWNXzfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
ملايين الإيرانيين الأشاوس اجتمعوا بتوحيد وتآلف لتقديم الاحترام لسماحة آية الله العظمى السيد الخامنئي وإرثه الدائم. لا هم ولا قواتنا المسلحة الشجاعة تخشى أي تهديد.
المادة 13 من مذكرة التفاهم واضحة وصريحة تمامًا: طالما استمرت التهديدات ضد إيران، لن تبدأ المفاوضات للوصول إلى اتفاق نهائي. التزموا بما وقعتم عليه.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/81279" target="_blank">📅 08:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81278">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3b3b1551.mp4?token=t84o-28sUeiCuDYfJoFaTQaetj_Ll2z_FmHnCLWZ6BQ7dp8jncEu1x-UMweNaFME9SvnEIoArmxI7QmnkrKYEjCGwYgVFbbxkNKL5nHLYt-5gZs50l8ksGgXJJI1jLatTI4JUcHlvPAF-y3acgGE8ZeLtxan8mnVLP00Yb-o3HSpkkqSirZMBfkj5KaPX9_uIh4Orazyex-2HsowKogeggmZG6Jy8XwBqW2eROuQiOh9vyjW1wLRb7BdjrLCXUf1fal9FrhM_0EHMVeeUpCQJSJGtQWNl6uB9-YJRXFE73zyodXnxZ6giIALr44kpbFr3Wajrq2ksGsRbOTaZyhUzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3b3b1551.mp4?token=t84o-28sUeiCuDYfJoFaTQaetj_Ll2z_FmHnCLWZ6BQ7dp8jncEu1x-UMweNaFME9SvnEIoArmxI7QmnkrKYEjCGwYgVFbbxkNKL5nHLYt-5gZs50l8ksGgXJJI1jLatTI4JUcHlvPAF-y3acgGE8ZeLtxan8mnVLP00Yb-o3HSpkkqSirZMBfkj5KaPX9_uIh4Orazyex-2HsowKogeggmZG6Jy8XwBqW2eROuQiOh9vyjW1wLRb7BdjrLCXUf1fal9FrhM_0EHMVeeUpCQJSJGtQWNl6uB9-YJRXFE73zyodXnxZ6giIALr44kpbFr3Wajrq2ksGsRbOTaZyhUzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إنطلاق العجلة التي تحمل جثمان الإمام الشهيد وعائلته الشهداء من مسجد جمكران نحو حرم السيدة فاطمة المعصومة عليها السلام.</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/81278" target="_blank">📅 08:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d93c095a.mp4?token=ltoJNsEkyh0JfFKwZGXJi3GN-9YEhJCDI8nGhREZWr727PDmP4t3Imr29mGwxIwPN56jnxp-munJYQue5-v6pcJzog27yikpn1xGCpXPQgKo89BygOBdw2UXVwlEmMMM8zBGsvUFrkrYFbL7Y-356yYneTWrDLxiuF4yeDY92cxAty1tDVnRSBLNQ4IsSTJ-L3zydrkra8OPYYCLTRzNRzByO9--rkUQPy73wrnw7fvE77vTgmxxy9rhssffAsvE9km49tlK2bBBet2ElLBn67tg6Tx4wZydNT0GM01uCQp1jB_rhTxwBbTxOzeJT-kDqYIPIYjPZ324Q7X3cj3gVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d93c095a.mp4?token=ltoJNsEkyh0JfFKwZGXJi3GN-9YEhJCDI8nGhREZWr727PDmP4t3Imr29mGwxIwPN56jnxp-munJYQue5-v6pcJzog27yikpn1xGCpXPQgKo89BygOBdw2UXVwlEmMMM8zBGsvUFrkrYFbL7Y-356yYneTWrDLxiuF4yeDY92cxAty1tDVnRSBLNQ4IsSTJ-L3zydrkra8OPYYCLTRzNRzByO9--rkUQPy73wrnw7fvE77vTgmxxy9rhssffAsvE9km49tlK2bBBet2ElLBn67tg6Tx4wZydNT0GM01uCQp1jB_rhTxwBbTxOzeJT-kDqYIPIYjPZ324Q7X3cj3gVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد جوية تظهر عظمة الحضور الجماهيري الكبير في مراسم تشييع جثمان القائد الشهيد للثورة الإسلامية في مدينة قم المقدسة.</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/81277" target="_blank">📅 08:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdae077c38.mp4?token=FU6TFOtIMZxXXPaQt7-muTufE8viIkdW0IYd_ef4wENwwzi7nQD48OJK5BLPnPFO_pfi0Rv-PpdFI7UFCyj0mdYcrjUJ2LrFAtpVAnF0wIP1R2OYLL8keLho35dkrCbDULmaTuAhAwfqzxTxjxabQqsFlKlJMQqDALTZ3SpMIK8OBIfM7CP9BRrJCHzdPIeOKBx-7H5IrdGEqAabs0nwVN50OYrOSyn91LE-P46BvAloeynDXHglUIIq1w8kQpaKN4Pyys0nFMp1yiIeOY9C7eBiEcNyUxFBd9YCTkKY4Om0z8-t_h6TmMoL42SP15PdCaWXPpJpl0xvbFyuKjcZUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdae077c38.mp4?token=FU6TFOtIMZxXXPaQt7-muTufE8viIkdW0IYd_ef4wENwwzi7nQD48OJK5BLPnPFO_pfi0Rv-PpdFI7UFCyj0mdYcrjUJ2LrFAtpVAnF0wIP1R2OYLL8keLho35dkrCbDULmaTuAhAwfqzxTxjxabQqsFlKlJMQqDALTZ3SpMIK8OBIfM7CP9BRrJCHzdPIeOKBx-7H5IrdGEqAabs0nwVN50OYrOSyn91LE-P46BvAloeynDXHglUIIq1w8kQpaKN4Pyys0nFMp1yiIeOY9C7eBiEcNyUxFBd9YCTkKY4Om0z8-t_h6TmMoL42SP15PdCaWXPpJpl0xvbFyuKjcZUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
ترامب نحن سنقتلك.. لافتة ترفع على أيدي المشيعين في مسجد جمكران بمدينة قم المقدسة.</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/naya_foriraq/81276" target="_blank">📅 06:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e484095f8.mp4?token=nuylt-F63x7xFq-SzU7vsMQsI4Tc1m0Qlcb4YQ3C3CYenKSMImGtlXexXhCgWUGADZAnNYbDxoEiCkUfRgzOOENOokQYwrWwABNxxUmkiJmwtYVF1K92QHeAKhTScA_209zMmqkcJBBeM5-4fTxW_4tgCnY6FDrugRi5tGPvAYtdifgTyt8x0Xw6F3AJNwhox6tRVpcVz1oZqwHs24QxBF0-nvKz4xyvgKk-oyj9n32hGTlJrLaf-28dyG1Oo_IeyvwdiFbxsmC2T6vH0sHga4xYFOoTHTaoGbD5-b764UfHtM00u8uvjyeBOr8tpo-hIlrnyLcoXK4FFWOKy8sd3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e484095f8.mp4?token=nuylt-F63x7xFq-SzU7vsMQsI4Tc1m0Qlcb4YQ3C3CYenKSMImGtlXexXhCgWUGADZAnNYbDxoEiCkUfRgzOOENOokQYwrWwABNxxUmkiJmwtYVF1K92QHeAKhTScA_209zMmqkcJBBeM5-4fTxW_4tgCnY6FDrugRi5tGPvAYtdifgTyt8x0Xw6F3AJNwhox6tRVpcVz1oZqwHs24QxBF0-nvKz4xyvgKk-oyj9n32hGTlJrLaf-28dyG1Oo_IeyvwdiFbxsmC2T6vH0sHga4xYFOoTHTaoGbD5-b764UfHtM00u8uvjyeBOr8tpo-hIlrnyLcoXK4FFWOKy8sd3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أللهم إنه نزل مجاهداً موحداً أللهم أللهم أللهم إنه نزل عندك شهیداً أللهم إنه نزل عندك قتیلاً للإسلام</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/81275" target="_blank">📅 06:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0207b9fb.mp4?token=jF7x2_prZepd_jRgh2OLysTu8ySAmor0_bFMQwNLHckOmtgrZv9_TjFrerm7JI1sVRfjeqpm1SWsX2Zb01UOW7DTsoWz30BIXKRRMjV7mPi47h98_Aae9jmiBWj6a_WL8b8RgqaDBGCW8zHe0_X05hHJP0SW-jw0o8IYCAvnsNjsDZvyT4UaHAM3WCOr6eaIJ1DTKv9rF1Iz-RbN_27OS01fyU5vlHoduqL4kzjSpWE6zBTIsvpFqMrb-KvNqHpvgjQeW0W5eLNHLoJbzUTYIqxUIR2Jli3Hm-PBGs6Sgirhs_acnFUxQVds2JzqjF4f1XHIvFMIHx5XSBJpCZPa8g4NQvxlnddg_aMl2uC3xsJii3F6pr5p70fmrvjtNyq30ZqSK1pmg1XYzm68JeDd2YvHMKmOGnoG1FePmvYgq5B899Xjv8VqCW7Zi3i_znN6wvg7ckDtr9Xll_GDelYGIvc8j8dT-wjzHVQe0Q6xkSfsMdoqgrd3GPwsmhs9dGQLRWLxtCIJ0OoUINY-ECC4kudpAy50b-ZNhXrKgqVn1cODzZdVX4lVaXn1uKDY1TR4R6NWLqcAK8EPspzyA9_5GXwe7T5tTv08SW6EMqFtC9IWyUVW9i-YW39b-s1urIpl7rUpUEinVvSCDNRNCoijq2GbunK0xur0MVCoK70_nDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0207b9fb.mp4?token=jF7x2_prZepd_jRgh2OLysTu8ySAmor0_bFMQwNLHckOmtgrZv9_TjFrerm7JI1sVRfjeqpm1SWsX2Zb01UOW7DTsoWz30BIXKRRMjV7mPi47h98_Aae9jmiBWj6a_WL8b8RgqaDBGCW8zHe0_X05hHJP0SW-jw0o8IYCAvnsNjsDZvyT4UaHAM3WCOr6eaIJ1DTKv9rF1Iz-RbN_27OS01fyU5vlHoduqL4kzjSpWE6zBTIsvpFqMrb-KvNqHpvgjQeW0W5eLNHLoJbzUTYIqxUIR2Jli3Hm-PBGs6Sgirhs_acnFUxQVds2JzqjF4f1XHIvFMIHx5XSBJpCZPa8g4NQvxlnddg_aMl2uC3xsJii3F6pr5p70fmrvjtNyq30ZqSK1pmg1XYzm68JeDd2YvHMKmOGnoG1FePmvYgq5B899Xjv8VqCW7Zi3i_znN6wvg7ckDtr9Xll_GDelYGIvc8j8dT-wjzHVQe0Q6xkSfsMdoqgrd3GPwsmhs9dGQLRWLxtCIJ0OoUINY-ECC4kudpAy50b-ZNhXrKgqVn1cODzZdVX4lVaXn1uKDY1TR4R6NWLqcAK8EPspzyA9_5GXwe7T5tTv08SW6EMqFtC9IWyUVW9i-YW39b-s1urIpl7rUpUEinVvSCDNRNCoijq2GbunK0xur0MVCoK70_nDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد إنتهاء صلاة الجنازة، تهيئة الجثامين الطاهرة لبدء مراسيم التشييع.</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/81274" target="_blank">📅 06:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53c7294818.mp4?token=F1SX7fTaxoKq1wdTbTZGhKaEKL8ejuR9ILAnrIU6xiu2pnkfYSRsgl4H2lcEjyTbImUt1h4XG5TnOZ8LkiORk12IXfYCMJn16q4COdGxsvQvwUxDoayQYMZ0vRLvVycCtWSKIttiup6YqDKq1HTvKDYMlt_MBspZs_LzZE3P4svSMkW6GP3IehYE6QoPEXAriqZtcNWhnUAPZUAdUwfATIR4q7HZ96BOTqS1UqYvyTl25r-85k1CMFDC85i9qwGJCxtOdAUiYb5MyZy09JaCoOVmSFkNJcxPqoTTnk7Y6YwZecMkKHXWI2kPHMzvLHxfCqWAmybTzMuvYcg1azvLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53c7294818.mp4?token=F1SX7fTaxoKq1wdTbTZGhKaEKL8ejuR9ILAnrIU6xiu2pnkfYSRsgl4H2lcEjyTbImUt1h4XG5TnOZ8LkiORk12IXfYCMJn16q4COdGxsvQvwUxDoayQYMZ0vRLvVycCtWSKIttiup6YqDKq1HTvKDYMlt_MBspZs_LzZE3P4svSMkW6GP3IehYE6QoPEXAriqZtcNWhnUAPZUAdUwfATIR4q7HZ96BOTqS1UqYvyTl25r-85k1CMFDC85i9qwGJCxtOdAUiYb5MyZy09JaCoOVmSFkNJcxPqoTTnk7Y6YwZecMkKHXWI2kPHMzvLHxfCqWAmybTzMuvYcg1azvLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء إقامة صلاة الجنازة على الجثامين الطاهرة في مسجد جمكران بمدينة قم المقدسة.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/81273" target="_blank">📅 06:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263627e13d.mp4?token=Y-BxClHc84ODm2dZ8eE50337XSHg3MSpGamt-h66JzOnxOAep6XZUTITNdJF5z_hRGJqYQRitu6t-iWfyZb-p762oTfCAE6jwtE-ArSceIGFXYLm_764ClPP3rzXA7lLpwzHPKEhrXRYGlS1kKBVPeoIt25tSFmT_RKMpE-_nW8rJGY41cpBTMhTNNK5A44PsWyhwbLu0P6rK7NuOegHAqyQsaXWAhhPoTaNUwzwScHpt6pOZELwszF0wBoZy_JeFsetzCcf6BsGLLUGQdhvVofxu87elMBQaQPzJy0RrHA96dLS5fzBVhGTfnHsdysJpeRp5IEUqgwwilPX6aolZ1KQBN15jGqjImYYs-IM9SPbqmQSH9hyFdxbge_2M56vwSII2Hikub6JO4Scg2eMRbqwjFM-GwoVP-MhzV_J1IsL-jOdk2HHfkjxvWBYWQbnxOHguwXa4ulfEg3-qdNCDvzpBMSwS6j32YljXuDUJPHyCh6dyNjjjBV3zDV2G3mofUHt73bKEHgDVvq6JgUcuiiDTRwChDcVIe0wc3jPVXuBsB2rcxVJiCkNjDOBQwu6qzPEchLMAY2ylT1GZZLvWHjKdo1nysc3g-oae48s75om1TK5owRdBTXfahZYPjwnpea-9dIENa_lmJ2WZ9MWEgYkydLFbSPnzP82CDVLKeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263627e13d.mp4?token=Y-BxClHc84ODm2dZ8eE50337XSHg3MSpGamt-h66JzOnxOAep6XZUTITNdJF5z_hRGJqYQRitu6t-iWfyZb-p762oTfCAE6jwtE-ArSceIGFXYLm_764ClPP3rzXA7lLpwzHPKEhrXRYGlS1kKBVPeoIt25tSFmT_RKMpE-_nW8rJGY41cpBTMhTNNK5A44PsWyhwbLu0P6rK7NuOegHAqyQsaXWAhhPoTaNUwzwScHpt6pOZELwszF0wBoZy_JeFsetzCcf6BsGLLUGQdhvVofxu87elMBQaQPzJy0RrHA96dLS5fzBVhGTfnHsdysJpeRp5IEUqgwwilPX6aolZ1KQBN15jGqjImYYs-IM9SPbqmQSH9hyFdxbge_2M56vwSII2Hikub6JO4Scg2eMRbqwjFM-GwoVP-MhzV_J1IsL-jOdk2HHfkjxvWBYWQbnxOHguwXa4ulfEg3-qdNCDvzpBMSwS6j32YljXuDUJPHyCh6dyNjjjBV3zDV2G3mofUHt73bKEHgDVvq6JgUcuiiDTRwChDcVIe0wc3jPVXuBsB2rcxVJiCkNjDOBQwu6qzPEchLMAY2ylT1GZZLvWHjKdo1nysc3g-oae48s75om1TK5owRdBTXfahZYPjwnpea-9dIENa_lmJ2WZ9MWEgYkydLFbSPnzP82CDVLKeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نقل الجثامين الطاهرة لإقامة صلاة الجنازة عليها.</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/naya_foriraq/81272" target="_blank">📅 06:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca74538d96.mp4?token=Z4nNWlVa5H8CH46VOwgg3tE7f6rBevmI3Zhg4Y3vzH4me988OS8Tg_S0ZVKk4-a-BfenUCvdFcEJtjo_82ujhG9zx0zu3hp2jLGCJZv8fNkTEnlsx1ixPzBB8MQn1_Thtq-7mRwQLWj3athXGQTcOghU0E01LiF3fhPBKQQYYuZT0qGlTKPrXoCgAY4UC8bv6UXQE7tfIRP6sI9b1tela9u7gVp6FJ1NkYCHcHkGj7tH_g4mFAGfGk4JvCu7zjJbjSpQfvhWtNBFrqKCxqSFu0YoQ6zNq_QeUni6XywIsIm_c0FDP10YVk5MupOeRVISMMIHaj0_obOytnkfDWrmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca74538d96.mp4?token=Z4nNWlVa5H8CH46VOwgg3tE7f6rBevmI3Zhg4Y3vzH4me988OS8Tg_S0ZVKk4-a-BfenUCvdFcEJtjo_82ujhG9zx0zu3hp2jLGCJZv8fNkTEnlsx1ixPzBB8MQn1_Thtq-7mRwQLWj3athXGQTcOghU0E01LiF3fhPBKQQYYuZT0qGlTKPrXoCgAY4UC8bv6UXQE7tfIRP6sI9b1tela9u7gVp6FJ1NkYCHcHkGj7tH_g4mFAGfGk4JvCu7zjJbjSpQfvhWtNBFrqKCxqSFu0YoQ6zNq_QeUni6XywIsIm_c0FDP10YVk5MupOeRVISMMIHaj0_obOytnkfDWrmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاوة سورة الفاتحة والوداع الأخير من قبل آية الله جوادي الأملي على جثمان الإمام الشهيد وعائلته.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/81271" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10275b957.mp4?token=uyKKlTI7nPqaF3g-gG399BdWdxmVgnKOFZKGSdi8cdpzdlOfrVgr-H6TCOxQXAKdzpilcem5odua6ojZkLVwQIMqi51x_yL2oOdp1eIaahSny41rws06gdyFo1LlPv4CLOSsRxTadnjQNv_Ge_a-mpssETCOAIytUgEKn3k-thOUbBx81iw0xCkbWGvGwyALwN5gsGBFzP0SaUQKgA1SRVskTVk7gKxMnW9JaX1alnrdOSEBu0s1agQPDHfi5BAYTmyVPsFu191vKXM7fV_6vz8K2AkbYkWUvVc5RPm_3RaXdXBaUm_XFKxmhVc2EgdvhAThkU-rtRZPiaqvX1r8UmHWR6ozsmF8Vfglc4MEMcNWJN3c11VUhCVN92hUYQ2v34uDp--2yZHpr48bnbKgbzjXt7C7TRV9xWVoElSR5pogZovsl-rwkonliNBNHIZfXxHnRHRGysufMhFjQL_hxblputA3TYQGnMygLZzdL_bmO5dHqGKoqtiSFb6aFIOq5lOpHoLj7XrW2a5MiiplxakuByE2RJjLCe5UJbBhBg4JMLvRZ-1qY-4XMkdvCE5RZMgzkodAkhglUZGo4gwvvfqwWCsS3yYQzVTk3SyIZ2TWSi_yYm1LiXLfZ2VRX9k0_eMXLD8_fgBHae9QX6HOxpguqEx0AIcy6EWEMDONMeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10275b957.mp4?token=uyKKlTI7nPqaF3g-gG399BdWdxmVgnKOFZKGSdi8cdpzdlOfrVgr-H6TCOxQXAKdzpilcem5odua6ojZkLVwQIMqi51x_yL2oOdp1eIaahSny41rws06gdyFo1LlPv4CLOSsRxTadnjQNv_Ge_a-mpssETCOAIytUgEKn3k-thOUbBx81iw0xCkbWGvGwyALwN5gsGBFzP0SaUQKgA1SRVskTVk7gKxMnW9JaX1alnrdOSEBu0s1agQPDHfi5BAYTmyVPsFu191vKXM7fV_6vz8K2AkbYkWUvVc5RPm_3RaXdXBaUm_XFKxmhVc2EgdvhAThkU-rtRZPiaqvX1r8UmHWR6ozsmF8Vfglc4MEMcNWJN3c11VUhCVN92hUYQ2v34uDp--2yZHpr48bnbKgbzjXt7C7TRV9xWVoElSR5pogZovsl-rwkonliNBNHIZfXxHnRHRGysufMhFjQL_hxblputA3TYQGnMygLZzdL_bmO5dHqGKoqtiSFb6aFIOq5lOpHoLj7XrW2a5MiiplxakuByE2RJjLCe5UJbBhBg4JMLvRZ-1qY-4XMkdvCE5RZMgzkodAkhglUZGo4gwvvfqwWCsS3yYQzVTk3SyIZ2TWSi_yYm1LiXLfZ2VRX9k0_eMXLD8_fgBHae9QX6HOxpguqEx0AIcy6EWEMDONMeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والد "الطفلة زهراء" حفيدة الإمام الشهيد ذات "14 شهر" من العمر يودع جثمانها الطاهر في مسجد جمكران.</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/81270" target="_blank">📅 05:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f7cdd0bd.mp4?token=p26k_4READTMLnlHW4oiRbJbCWDb62BZnbP14FMyVVGRTFqCSGw8IFd_fX5-bJa3oi1d1v6nmfcHbk9FlTQfzsBJRq4N6bMVs7BGPFvXKPhHErrf2b5klBEqt-YgMrwvNTWzPa18BaLUXUOJSg70ohkn4wBDG0ZU9vnz9L6ovEfJp1XyK6W0lKlFml6J6hUHodkTqAOmH36MHJ7ochD5YFBlB1PaFfW0NdXZubBKKtvbsnpuKnSuVPA1ALsVXUuEgRSfywZQIohvAvgUxoj-SPhLHEBmxSN7JwRqp7lIQzM6hnGP350xEkGEWMjbOcG7oSNMA5-tWUT7ArZzYYInIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f7cdd0bd.mp4?token=p26k_4READTMLnlHW4oiRbJbCWDb62BZnbP14FMyVVGRTFqCSGw8IFd_fX5-bJa3oi1d1v6nmfcHbk9FlTQfzsBJRq4N6bMVs7BGPFvXKPhHErrf2b5klBEqt-YgMrwvNTWzPa18BaLUXUOJSg70ohkn4wBDG0ZU9vnz9L6ovEfJp1XyK6W0lKlFml6J6hUHodkTqAOmH36MHJ7ochD5YFBlB1PaFfW0NdXZubBKKtvbsnpuKnSuVPA1ALsVXUuEgRSfywZQIohvAvgUxoj-SPhLHEBmxSN7JwRqp7lIQzM6hnGP350xEkGEWMjbOcG7oSNMA5-tWUT7ArZzYYInIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وصول جثمان الشهيد القائد السيد علي الخامنئي وشهداء عائلته إلى مسجد جمكران المقدس، لتوديع محبيه وإقامة الصلاة على جثمانه.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/81269" target="_blank">📅 05:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f013a31a88.mp4?token=HLImmC3q7dIcmuDItF8nd_ei1gJzruV_hYclDVddqMVcL9Abhu7Vxf-_zYaTfotkAtTTieKvMqM1C1HCZQrmhlH66aURL4KWMdLDxVGtIF-fvrVD7Rj6tHnb9X2e8SvWsI_woYaj0Y7x4ckVGa45bsTKTPDSglCpFR7jAJz_vS45rVryMdM2P5bduICkxcdXnZUKhyJ7wzG4tqrhS0OEnBZAhEx1pRveaV42bkV1AEH8zP9dvy5qHAUK12FYi0SjPCVt0Cx8CWZ2uz7a73pOdo0w3SxNPGhz4vFraxYINdr8cxkhKzDrtaX2ljO45KSXoClzXfqdwSbjCLrjeZYqVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f013a31a88.mp4?token=HLImmC3q7dIcmuDItF8nd_ei1gJzruV_hYclDVddqMVcL9Abhu7Vxf-_zYaTfotkAtTTieKvMqM1C1HCZQrmhlH66aURL4KWMdLDxVGtIF-fvrVD7Rj6tHnb9X2e8SvWsI_woYaj0Y7x4ckVGa45bsTKTPDSglCpFR7jAJz_vS45rVryMdM2P5bduICkxcdXnZUKhyJ7wzG4tqrhS0OEnBZAhEx1pRveaV42bkV1AEH8zP9dvy5qHAUK12FYi0SjPCVt0Cx8CWZ2uz7a73pOdo0w3SxNPGhz4vFraxYINdr8cxkhKzDrtaX2ljO45KSXoClzXfqdwSbjCLrjeZYqVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بعد مليونية طهران.. حشود غفيرة تملأ مسجد جمكران بمدينة قم المقدسة ومحيطه وجميع الطرق المؤدية إليه للمشاركة بمراسيم تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/81268" target="_blank">📅 05:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏ترامب: تحدثت مع إنفانتينو، رئيس الفيفا، بشأن البطاقة الحمراء، من غير العدل أن يقوم الاتحاد الدولي لكرة القدم باستبعاد أحد أفضل لاعبي الولايات المتحدة.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81267" target="_blank">📅 05:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d490004edc.mp4?token=CH8zx3Hd8B2C09YMLilAivliWczheVP4X0hJh2F-TmyD9MkrRA6N2i4sL69L_mXTPyx6OfzlsoXCGMWyKpbiUASODNnlq_V6JYRi58UVD7UFWzE5aXOqJI1IucQhfWZBQjtgq33ckQJ7FkfLuy6hP8a-mhVa8Vg1aNhygX_HT0KHzkE_V10mt4dQ-5dixShfyR_oI-qsGSU0bShaFnQku-hR49Bnlx8lKXRmDERNE7JD7yHalx1O3lBG7St_ZDiAFpCKxDL1wfAqczFBnDL8TxDFZ0YcbGCxJENiPS0xQVEWZQKWPjuj97VOcGf2nnEF652gQ2dmJz6JWiogMNqiURPKei3VYGs8Ncup2UiE-eVcXnmARVXptEiLQXCEKI377Fa6DAdbrNjjJ-LKqx7kHV5e6KZuF63WJ2ly8gReol9sO85ffp1BRSqW7CP0Ns9fz7Q_7frmNgMyl82Ce_SWRFzq4nvMLrvf7WxOq6eAMVh4YVat3HetyqEIKZ6tAKXFdmSSOMH6mKCfnGFx_YLjTcID88WYSlPCqQroL8Yak81qIWYGmdICsvpn0op4SDJfD9msaIPdySWBWsd_AtsuZWKIdHAXeiMzjCXic3-kTDWLoi-qJc4llVtnbkjiBn78NAlx0jnyBm1VGJUUsa21oibu5aplRJoTrJsnKpH1g6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d490004edc.mp4?token=CH8zx3Hd8B2C09YMLilAivliWczheVP4X0hJh2F-TmyD9MkrRA6N2i4sL69L_mXTPyx6OfzlsoXCGMWyKpbiUASODNnlq_V6JYRi58UVD7UFWzE5aXOqJI1IucQhfWZBQjtgq33ckQJ7FkfLuy6hP8a-mhVa8Vg1aNhygX_HT0KHzkE_V10mt4dQ-5dixShfyR_oI-qsGSU0bShaFnQku-hR49Bnlx8lKXRmDERNE7JD7yHalx1O3lBG7St_ZDiAFpCKxDL1wfAqczFBnDL8TxDFZ0YcbGCxJENiPS0xQVEWZQKWPjuj97VOcGf2nnEF652gQ2dmJz6JWiogMNqiURPKei3VYGs8Ncup2UiE-eVcXnmARVXptEiLQXCEKI377Fa6DAdbrNjjJ-LKqx7kHV5e6KZuF63WJ2ly8gReol9sO85ffp1BRSqW7CP0Ns9fz7Q_7frmNgMyl82Ce_SWRFzq4nvMLrvf7WxOq6eAMVh4YVat3HetyqEIKZ6tAKXFdmSSOMH6mKCfnGFx_YLjTcID88WYSlPCqQroL8Yak81qIWYGmdICsvpn0op4SDJfD9msaIPdySWBWsd_AtsuZWKIdHAXeiMzjCXic3-kTDWLoi-qJc4llVtnbkjiBn78NAlx0jnyBm1VGJUUsa21oibu5aplRJoTrJsnKpH1g6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بعد مليونية طهران..
حشود غفيرة تملأ مسجد جمكران بمدينة قم المقدسة ومحيطه وجميع الطرق المؤدية إليه للمشاركة بمراسيم تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81266" target="_blank">📅 05:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
مسؤول أمريكي:
سفينتان تجاريتان تعرضتا لضربة من الحرس الثوري وأصيبتا بأضرار جسيمة دون وقوع إصابات.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81265" target="_blank">📅 04:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
‏واشنطن تعرب عن "قلقها البالغ" إزاء التجربة الصينية لصاروخ استراتيجي.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81264" target="_blank">📅 03:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔻
‏الإطار التنسيقي يجدد الدعوة إلى المشاركة الجماهيرية الواسعة في تشييع الشهيد السيد علي الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81263" target="_blank">📅 00:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v8qcJFhrob-2ZY3kdgWrw5s-Hl6kRySddYSyAoOF7xlsWsy1Sfe_EPVUZKp7mPhnLLguMO-69n_HMCoSbuEeYJQP6tlosEOcHiV3yONd1rxM2NkrvFpOTRov9qF150Dr_mHLCf972CT3hQ-8FDxCwjM4BXB71n2szjP6gr6q_YbD4ysoVf93jaw_gsSBH6jb0e1Nfk4QPj5DHGTrissdwcDvs0K7UgtPmyXl9rhF78fA7Fnw0zITyEBvc5XwuxI3LIG4YueL6BHWiDoHnnLDCn9y9rGURrCU77w5xc0ZSr_hHqWreFEw4PVrXFF9pyE-6pySuqLiaaXyDycNkn8_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROVK5LQS1jA_qK7_LJNaxCg4GjyRwKaeE6G29p2jTakRY7zS8JeUoJmMidUv-kGNLbJe3U3iDi5vH1UXL8M0PNqXN6S09YE7HWiYR4t2-YUlaE96x2oTA22AUMlOJ60Hul_zCrGq_B41gLIbVWV0MV6aWHeEjMQCH8D06FPOcd3ZKk8XJITtuQ2lYIAbNwAkRWvtcmYgB5tSKuAZF71ZXnOqolaxJOx-iO69BoaAighK9l8D2zLXt60ld3xingPMAm5yUtk8kUCIz6UngZQ7mP7VVP5Hj2edihbDT1WvMHne6oHHUNKG9hEp5oKQ_sCWsdpQlSlpza2bybCibTjlJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlqWQxEg6flx3ZHWnyCVGXrtMOONVvhbN_lMh6g0HIoyrnqPtW83rraJrV24RcWTfshf5Fm1EEemstQFa4KdTPHInxXVhJMboGBp27G3hbOYyqHrV70HVFK-RCFt2HjvU88M8A4HaSQw_2ssgf9n7bx53JoyfNBzbJ6S5IHvbl4GQM0h68s6QJMQL0_zqt_yNG2ZI8aqrYW93C6bsxNuw8I3jBBgJ62iGD5kl77-zw7sQ5FWDzOyGeYbjJrRHit5ijnc8RvhGFe2CXKBq-XriphoSsKBQ_s_4CQiNk1h8-Z7BbIzQgq_FqpmPsluF_rnGIOTQWwzd1AshAQU0RZ6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mb1RVeG7N81DNd3i__uUFFntkszuF4BiUFMSC3uj6YExUDbKGbkhqKy3a2TwDhc6GVPHnXQzEzfuCubN73Dt0z-0SH1joHXKNkpmDWzw71skqVRKFPVozs7B3MFQ_8kBHEREiXa7zAigi0SVrtzYZRyPXXq64KVMiBZpvULGpRGLUDUqfA10kdb7BRslPATBAMUH6aUOjkmMZ-CcV21Nwh2u1DMhX1zEpEYHO0JkicJzz8ooDO-O498hKIxLHNuVrDa0X69YEtumZT7qNNWxQhFxTmUs4-ayLXj8nzA-dpEIbLvwLqvFH7vMDo889-O6aE1ZawOFkNc6iBONmpsb7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
تواصل مواكب الحشد الشعبي تقديم خدماتها للمعزّين في العاصمة طهران.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/81258" target="_blank">📅 00:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29b0ce560.mp4?token=h_Sqd9jy22mZKBySMWmEFn5EClnlw6WAhQVVxcbdOl-zRqHTK8yTVy1P1m1dVdRvFHOuJ7QQYrN590dhmuhLQch4NEFH1e9791qB10rfc7BSAK3_4aPgXwxqQtvIEIx6FWJlhUoCtPaLbx2t4qvL-WQOEzmyHigiKK0d1iLlpzsBe_8Ok7uaLw4tTJCK4d91YRg4ST2eQgyGHuY2KZ9C7cAjU91xI03ae-6TmPp0ij3uk3JPQHFbAjU-ZNCa85vtn7tn8NAfNA7n7vT2M8cnWepvfnndNuutKaAcHyvLlM-TtMnEQaWvleDiOpqzViZ8LJ4pC2Qj6O-IvYRIVcYi_7ugcPN6m8tJn6wPGEaEFLZt6PnXG7taHmqE60Qk3Lp_t3RGnto6ncYbUg4xY_vQ2trR3zc1-NYG5JE8YULji8Hdka48-VQzdXCPpvwCkfcimHSm3U5x-T38JQwogogXCjVVFcthri085zbNTecuzVqRt3d8K4Q_-UeJN65rJI3sSl03Jjh5eID1tF5azT1bWH4bzgs2Kjvqd2ViRDxypDUAiNLRKZRhoafzhfIGxPRHCmpaPjDAfra4sgCjho7JXb4t4_V7PqRfoKQk1f5VLfQg7EjSZCCOTyvSHPC_Pe_MfZ0CSOMnXXJSK99vj90WShQkO3gFEGtLzdcrG6HBch0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29b0ce560.mp4?token=h_Sqd9jy22mZKBySMWmEFn5EClnlw6WAhQVVxcbdOl-zRqHTK8yTVy1P1m1dVdRvFHOuJ7QQYrN590dhmuhLQch4NEFH1e9791qB10rfc7BSAK3_4aPgXwxqQtvIEIx6FWJlhUoCtPaLbx2t4qvL-WQOEzmyHigiKK0d1iLlpzsBe_8Ok7uaLw4tTJCK4d91YRg4ST2eQgyGHuY2KZ9C7cAjU91xI03ae-6TmPp0ij3uk3JPQHFbAjU-ZNCa85vtn7tn8NAfNA7n7vT2M8cnWepvfnndNuutKaAcHyvLlM-TtMnEQaWvleDiOpqzViZ8LJ4pC2Qj6O-IvYRIVcYi_7ugcPN6m8tJn6wPGEaEFLZt6PnXG7taHmqE60Qk3Lp_t3RGnto6ncYbUg4xY_vQ2trR3zc1-NYG5JE8YULji8Hdka48-VQzdXCPpvwCkfcimHSm3U5x-T38JQwogogXCjVVFcthri085zbNTecuzVqRt3d8K4Q_-UeJN65rJI3sSl03Jjh5eID1tF5azT1bWH4bzgs2Kjvqd2ViRDxypDUAiNLRKZRhoafzhfIGxPRHCmpaPjDAfra4sgCjho7JXb4t4_V7PqRfoKQk1f5VLfQg7EjSZCCOTyvSHPC_Pe_MfZ0CSOMnXXJSK99vj90WShQkO3gFEGtLzdcrG6HBch0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بدأ نصب خيام المواكب الحسينية في كربلاء المقدسة تحضيرا لاستقبال ملايين المعزيين باستشهاد الولي الفقيه الامام الخامنئي(رضوان الله عليه).</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/81257" target="_blank">📅 23:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81256">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ffa92b16.mp4?token=EQFccqEZP8mOjZ7NYqggaGoV9ceS2ueoFb2TYiduVQRUWqRnVXoufE9sPhTlyMcAqAuwXwp_XSaAzbHujrFGnw0FsXb6MKf11VkXAk6gGhxPIVvqxFddIPdploVAODMVCGT3J2qTqzj1GebFzsvn78DiuXYjvZ8Jpt4T3npHcD5EngHMnPh57OitqzdaKaD6xIE-jSGSdyxqQ5J1WYNZgLyoMlA_Yy9TpHbjbijXPazQUGjhRIF0CmA3RdJcx4tvkzhQ_yOgddT-adyR1uV1X2Yvv88qs4mqFPuZ2uYKKwZnxRJOUjksf7iUHKQPcBFFCzNzAFFZ6-xgmPlqhLhfr3A3-DbuZmufyq5ki-g6sgRyqMDZSZGb9bWSUDP5DjsW3wIJUWQCDssbhJga39Pj7gWBdnt4BX6YUnIInIk18nZr2rfBR_-KqQEJW4-4OPOnk8hhh5mQj-4dzB7RmKXVChbO6jn1yKENuVr87clr6mpuzW6OBE1aBbK1uGK3LNDb1gJ_zZ-cXFjINNZN1KhfUFq_OjIXInf6Oo-YPB8MM32Mv1KkOqNt2K1r-J7OTfdbniiPPz0U6dbkyp6F5mE21FtftD7eSUt6g4RT4FPZ9iUSb8IvZBssogPDuFp8kCB76PJTTgXLH0WeeYEe11K4eVpO8LEq8yPfl7yYr3VEEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ffa92b16.mp4?token=EQFccqEZP8mOjZ7NYqggaGoV9ceS2ueoFb2TYiduVQRUWqRnVXoufE9sPhTlyMcAqAuwXwp_XSaAzbHujrFGnw0FsXb6MKf11VkXAk6gGhxPIVvqxFddIPdploVAODMVCGT3J2qTqzj1GebFzsvn78DiuXYjvZ8Jpt4T3npHcD5EngHMnPh57OitqzdaKaD6xIE-jSGSdyxqQ5J1WYNZgLyoMlA_Yy9TpHbjbijXPazQUGjhRIF0CmA3RdJcx4tvkzhQ_yOgddT-adyR1uV1X2Yvv88qs4mqFPuZ2uYKKwZnxRJOUjksf7iUHKQPcBFFCzNzAFFZ6-xgmPlqhLhfr3A3-DbuZmufyq5ki-g6sgRyqMDZSZGb9bWSUDP5DjsW3wIJUWQCDssbhJga39Pj7gWBdnt4BX6YUnIInIk18nZr2rfBR_-KqQEJW4-4OPOnk8hhh5mQj-4dzB7RmKXVChbO6jn1yKENuVr87clr6mpuzW6OBE1aBbK1uGK3LNDb1gJ_zZ-cXFjINNZN1KhfUFq_OjIXInf6Oo-YPB8MM32Mv1KkOqNt2K1r-J7OTfdbniiPPz0U6dbkyp6F5mE21FtftD7eSUt6g4RT4FPZ9iUSb8IvZBssogPDuFp8kCB76PJTTgXLH0WeeYEe11K4eVpO8LEq8yPfl7yYr3VEEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استنفار القوات الأمنية في محافظة النجف الأشرف قبل يوم من وصول جثمان السيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/81256" target="_blank">📅 23:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81255">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
محافظة كربلاء المقدسة تعطل الدوام الرسمي في دوائر المحافظة يوم الاربعاء لافساح المجال لأهالي كربلاء المقدسة من المشاركة في مراسم استقبال وتشييع الشهيد المرشد الأعلى للجمهورية الإسلامية الإيرانية اية الله العظمى السيد علي الخامنئي(قدس)</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81255" target="_blank">📅 23:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c715d310e2.mp4?token=gtsLQUiagApuoOyluy4YmVtlug45gMmulinctl94-qyYFhDlKj-k8DOHjriDoHePUrEI578NVUafbAZ6tSu_GHodW04nFyMVoi7h_rK-LVxWyfVLHC86AXEt3XHqdnri6w9Zv3fZ43tY3SiN6moT15fJSgvZtfi_F4gq9OILSknImbxoqx7S88DEiOHh8QszoNn3iVyEsvVfrCn4uvyNTLZdh6Cm5xHVW4qP1JTirC9OPw7a1WfH3iMm7ev62ao9WTir9ZbSjVaWy6mFPMn9_x1KJINA5OSdbF18lSHkWcoq621i5qeVxK_hk_FCUt7ExYcpv0MZIao48jKHlDHnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c715d310e2.mp4?token=gtsLQUiagApuoOyluy4YmVtlug45gMmulinctl94-qyYFhDlKj-k8DOHjriDoHePUrEI578NVUafbAZ6tSu_GHodW04nFyMVoi7h_rK-LVxWyfVLHC86AXEt3XHqdnri6w9Zv3fZ43tY3SiN6moT15fJSgvZtfi_F4gq9OILSknImbxoqx7S88DEiOHh8QszoNn3iVyEsvVfrCn4uvyNTLZdh6Cm5xHVW4qP1JTirC9OPw7a1WfH3iMm7ev62ao9WTir9ZbSjVaWy6mFPMn9_x1KJINA5OSdbF18lSHkWcoq621i5qeVxK_hk_FCUt7ExYcpv0MZIao48jKHlDHnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء مراسم التوديع لجثمان الإمام الشهيد في مسجد جمكران</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81254" target="_blank">📅 23:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
محافظة النجف الاشرف تعطل ليوم الأربعاء بمناسبة مراسم تشييع سماحة آية الله العظمى السيد علي الخامنئي(قدس سره).</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81253" target="_blank">📅 22:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4f292302.mp4?token=W5AJG9z8_UUEcaMnLd9pmmLl3h-1Y5YniMNg56g1KT07tphNlHY56axL-xEYThLykqCy7DNrDTOb5WkBrAnqYDpmRWM3o19W2coBxnCyYYDj2Oo7Xhb07B5-dtnCZb8xt5QKqiYbMTTDgTYUZRnM7u7rSjPkgfxB1zVZv9MHRS8s9MSYnW8PhbjKE6WxLYB0rXJPIHXX3XEe-kXS3aedmfFUJ1VhZPHu8xtUECNM6cMDr1av0c10UzU1ie-FB_CG9ktfENjpQwG7KFHwIBkI1VgI79LaQosSXoE4aPwk21sMAZXgt31cOq_vf_YXKuaFmDQ35tUkoVJPacxRKh2pPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4f292302.mp4?token=W5AJG9z8_UUEcaMnLd9pmmLl3h-1Y5YniMNg56g1KT07tphNlHY56axL-xEYThLykqCy7DNrDTOb5WkBrAnqYDpmRWM3o19W2coBxnCyYYDj2Oo7Xhb07B5-dtnCZb8xt5QKqiYbMTTDgTYUZRnM7u7rSjPkgfxB1zVZv9MHRS8s9MSYnW8PhbjKE6WxLYB0rXJPIHXX3XEe-kXS3aedmfFUJ1VhZPHu8xtUECNM6cMDr1av0c10UzU1ie-FB_CG9ktfENjpQwG7KFHwIBkI1VgI79LaQosSXoE4aPwk21sMAZXgt31cOq_vf_YXKuaFmDQ35tUkoVJPacxRKh2pPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أهالي محافظة قم يتجمهرون بانتظار تشييع النعوش الطاهرة للسيد الشهيد علي الخامنئي وعائلته.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81252" target="_blank">📅 22:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
محافظة ميسان تخصص أكثر من (120) حافلة لنقل المشاركين إلى محافظتي النجف الأشرف وكربلاء المقدسة ذهاباً وإياباً مجاناً.
▫️
سيكون التجمع يوم غدٍ الثلاثاء في تمام الساعة الثالثة ظهراً أمام مبنى ديوان محافظة ميسان على أن يكون موعد الانطلاق الساعة الخامسة عصراً.
﻿</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81251" target="_blank">📅 22:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38afce1093.mp4?token=Q2qPDACQBP1A9XuIKKsabC8jNBUYTkOEt_1Wvil2AuU4ZA3JAYZ5w4yeZS1s6c1XYhO-uBf0W9Q7aMcl7A__1nPGLRzHMiUSFmha3YDNQY9x2VIY0PPO47YZYptYqb3FsdEZOM8urGLix-VrQfcxITbH27nOifb9usDSzcWsY1HI-2NMgi6e8ISc3wkWeiclbcixMJMb_wLCOYDxshCo85ciHytydcNoxLpehDKT8MdzUUtmD67FA6FMVudMFFKzTscPFDeE_7sUbExqmNveVzhtqPwC8Y_jGj6vlhtmP8FFIqVpGhNTV28V5gEkD0BX80aWUf94qrHWtIYwY1p1AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38afce1093.mp4?token=Q2qPDACQBP1A9XuIKKsabC8jNBUYTkOEt_1Wvil2AuU4ZA3JAYZ5w4yeZS1s6c1XYhO-uBf0W9Q7aMcl7A__1nPGLRzHMiUSFmha3YDNQY9x2VIY0PPO47YZYptYqb3FsdEZOM8urGLix-VrQfcxITbH27nOifb9usDSzcWsY1HI-2NMgi6e8ISc3wkWeiclbcixMJMb_wLCOYDxshCo85ciHytydcNoxLpehDKT8MdzUUtmD67FA6FMVudMFFKzTscPFDeE_7sUbExqmNveVzhtqPwC8Y_jGj6vlhtmP8FFIqVpGhNTV28V5gEkD0BX80aWUf94qrHWtIYwY1p1AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سائق الشاحنة عراقي الجنسية يفقد حياته على الأراضي السورية نتيجة انفجار شاحنته أثناء نقل النفط</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81250" target="_blank">📅 22:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81249">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_QHYOgxaXjQoYOm3FxuKGB7aW-VNswHO3kIOSUaIRalf44B91QtXwzXqoJJyiVusqxoLFj_kx-OrxV6KxCjIDl8UKTxJ9KWNXABXopXYgnURTT07rYpzTL8-8KOD-R1vZ4Y53VJEyVSapUQUlkU0uf2iD8SDkluxwj0AfOhyhP_ELNcB9stzzIkuFsq-rw5SBNaySvjK6sjhFUekng_LXj5PfYYEbAS30AFGDgDJOey1rmmcWzG7CrDwVbN8OZjuHU8eZhkq1guCc2mHHki0K1kn2bAdSC7KHdxAekWfvXh8NwguJB9U1cE9AyBdx59rMX--Vr1Lkj_0pT4tVEZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الصهاريج العراقية التي تدخل الأراضي السورية في خطر حقيقي وفي حالة شبه يومية انفجار صهريج نفط عراقي على طريق حمص طرطوس.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81249" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81248">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f5055980.mp4?token=BctxaBt2d0soup2l0C7Zb3k-wCWqDnauk3Knzy9ENQiZ-fpPLlyGaescH21pBWuktiMEMpCJeXW7NMFdJVrNbPOsKN2CJAzyQP5wqpQb_mIRZdkkQUYY7jUe0qU3dlNqK7gtcIpK4RiSTf2zthpb8U3aPOBamSCKDuA5fnY5HYXE1nlHVWWslEltAyyvUHnVBFqsPc0PKQaRNV9bBOyJBe-8xMwq4gNxV8YUUDvKmbcIRLguraO8wiBTO7lhDPVrDMb8AA2YlHHYBcCAt5YrM1RNm390rgXIVntaMR6ZZr90nMuy98CXC51CpF873FVg8TE7Wv5lknh_d9cgQpljrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f5055980.mp4?token=BctxaBt2d0soup2l0C7Zb3k-wCWqDnauk3Knzy9ENQiZ-fpPLlyGaescH21pBWuktiMEMpCJeXW7NMFdJVrNbPOsKN2CJAzyQP5wqpQb_mIRZdkkQUYY7jUe0qU3dlNqK7gtcIpK4RiSTf2zthpb8U3aPOBamSCKDuA5fnY5HYXE1nlHVWWslEltAyyvUHnVBFqsPc0PKQaRNV9bBOyJBe-8xMwq4gNxV8YUUDvKmbcIRLguraO8wiBTO7lhDPVrDMb8AA2YlHHYBcCAt5YrM1RNm390rgXIVntaMR6ZZr90nMuy98CXC51CpF873FVg8TE7Wv5lknh_d9cgQpljrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الصهاريج العراقية التي تدخل الأراضي السورية في خطر حقيقي وفي حالة شبه يومية انفجار صهريج نفط عراقي على طريق حمص طرطوس.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81248" target="_blank">📅 21:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81247">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovd01rUJjkuOwB00GzVsBY_dR5pYhNH10ncUCLvAIkgHZbxk7SGNKWq4QjE8_dfRXf_UH38HXw_EdmHMkXJAolrT04GqUCRN4-uDGJ4gLGb31HnbysI3YsvaktE3unwGBVBxtqhK5vnW3csScvZprhfVLZoiRfmH_PQdrTRvatra0sNP4ServDiuvWVbKEQFSPF6VGhR13VxCbivdZ0YrTKsdDQIvBzX30eX7EJGEg30Qa8KteSkGKgPBB9OEnv1Wg3MSZV6g7Oc-dHtULZe-kKLgpBImZTxKStY984IJCvOI9lSxk4Ipc0Mcpw9fI8RBAy653jXdDqRDGmg1gzCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سمح بالنشر.. الشيخ المجاهد الشجاع أكرم الكعبي دام رعبه يشرف على عملية تحضير صاروخ جمال ١٠ المجنح من عائلة كروز</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81247" target="_blank">📅 20:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ظهور سماحة الامين العام الشيخ المجاهد أكرم الكعبي دام نصره وهو يطلق بيده صاروخ جمال 10 ثأراً للإمام الشهيد  انا نايا عندي كل الخفايا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81246" target="_blank">📅 20:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81245">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e74022703.mp4?token=ueEMZ4KmiJw5wxOxfs8ctnpwDSE9o0q9pdOwbCkSZcVDJDdKWHkmgaUB46g2d7RiGJk9Ftr09VhFFxrBR9KrPcJNCX5ffjtDe1-5D98bTTi3t1Ohlpl-UXFTlcPaaNPd-NMuzUzp6fQ9qTrXIhac2Uyy7htsRYhhzJsgEQprGz1QbzAn2ewnDi2oH7B7Jhg7kxAcL7iIF3nyyKhiwBgifPtjXoqw1sriU7RvXOBU3yaBPMelyL2nu6wWVbPxDFPulZ1yY53-lQ2R9tn0rUO1H5w1JfgCcw-scZRndYYvbg2Uy23ZJmyx_-pgKpOENSGG9eve4Pd0BS3AaiTZM89zGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e74022703.mp4?token=ueEMZ4KmiJw5wxOxfs8ctnpwDSE9o0q9pdOwbCkSZcVDJDdKWHkmgaUB46g2d7RiGJk9Ftr09VhFFxrBR9KrPcJNCX5ffjtDe1-5D98bTTi3t1Ohlpl-UXFTlcPaaNPd-NMuzUzp6fQ9qTrXIhac2Uyy7htsRYhhzJsgEQprGz1QbzAn2ewnDi2oH7B7Jhg7kxAcL7iIF3nyyKhiwBgifPtjXoqw1sriU7RvXOBU3yaBPMelyL2nu6wWVbPxDFPulZ1yY53-lQ2R9tn0rUO1H5w1JfgCcw-scZRndYYvbg2Uy23ZJmyx_-pgKpOENSGG9eve4Pd0BS3AaiTZM89zGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يا لثارات السيد علي الخامنئي  السلام على الفارس العراقي</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/81245" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81244" target="_blank">📅 20:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنون - NOON</strong></div>
<div class="tg-text">أوبريت “أهل الإباء”
إلى الروح الخالدة للسيد الولي الشهيد الإمام علي الخامنئي (رضوان الله عليه)، وفاءً لنهج العزة والإباء، وتجديدًا للعهد على مواصلة طريق التضحية والثبات.
#كنا_ومازلنا_مقاومة
#كونوا_احرارا
ً
#
قوموا_لله</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81243" target="_blank">📅 20:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81242">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
العتبة العباسية المقدّسة تكمل خطتها لمراسم تشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81242" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3df93ff3.mp4?token=vNwI3np4M8zAsxospLoH0CCfL1nR5497e2TJQvN7NcfmAuKrlM3wLVFDz94pauPwwPX36kIL4fSKP6mBOFNhf_72kfCJiDC33XPsmOCS6FD_XSndi_Q6A8ASSDTxBYCfu9u6aMfVU7ntlcTuYbaf6N2DEl0_j0pYem2FeXVWNdBsrkXt8I2pXBuoK2SRzUrdXXTKIfz7D_Afp01HXPIcGm9uFNl6OURFfoUcV6H1obhH0--N4m_uzVStS5HTglsSU51KRRv1P9YLGc4P6JePlvZNdoGiSLL-jSVe7TYQYvMKICbo0h7cr8tXY5oU0GIzvGivZ7_aMmjHbFH4fZ4GQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3df93ff3.mp4?token=vNwI3np4M8zAsxospLoH0CCfL1nR5497e2TJQvN7NcfmAuKrlM3wLVFDz94pauPwwPX36kIL4fSKP6mBOFNhf_72kfCJiDC33XPsmOCS6FD_XSndi_Q6A8ASSDTxBYCfu9u6aMfVU7ntlcTuYbaf6N2DEl0_j0pYem2FeXVWNdBsrkXt8I2pXBuoK2SRzUrdXXTKIfz7D_Afp01HXPIcGm9uFNl6OURFfoUcV6H1obhH0--N4m_uzVStS5HTglsSU51KRRv1P9YLGc4P6JePlvZNdoGiSLL-jSVe7TYQYvMKICbo0h7cr8tXY5oU0GIzvGivZ7_aMmjHbFH4fZ4GQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المواكب الخدمية لكتائب سيد الشهداء تنتشر في شوارع الجمهورية الإسلامية في إيران لتشارك العزاء قولا وفعلا وعملا كيف لا و هاشم الحاج ابو الاء كان يقود المعركة من الأرض في أيام رمضان مطلقا اطارهم و سياستهم العرجاء ؛</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81241" target="_blank">📅 20:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81240">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHCa7UMRG6LOde6RV2gXS5ISAnroPSM7q7O8Z8S9UZiQ6wpFCqJaracg3jcMMFOGQq3eTgQsZo_e9mKsn74F97QH14joKwuGWUVPy4GNrT-sW3kzezjtaFZG0MKag63Og8u1Q6JdgsVc2Jh4cHXcDwRaXXy7ThxS3Kh8Oa_MIES4Fngg1AAYy2bi_yAqR8adBo62od4jhZKOazZkoxLWO8-qTBIqmKcRuxn_m076CWvjuQH2O984g_DBBgxFb0g6zMcAqt4sTU9LpAgi1oyrr-c2qkyZw3umkmgtqLgDeWSgqq1R5HEUg_cFcaPeCdo3NPy-vrI_5HfXidw4s4Js1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا لثارات السيد علي الخامنئي  السلام على الفارس العراقي</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81240" target="_blank">📅 20:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81239">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏الرئاسة الفرنسية: يجب ضبط الحدود اللبنانية السورية لحرمان حزب الله من تدفق أي مواد غير مشروعة</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81239" target="_blank">📅 20:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81238">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/81238" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81238" target="_blank">📅 20:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81237">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">يا
لثارات السيد علي الخامنئي
السلام على الفارس العراقي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81237" target="_blank">📅 20:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81236">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXSsSrP9PNE8UlyNGWbJ9KF29RjEq7PqsKtTq4qHhJ_6TdKDNpP7_TBozi8-ya_M1EPA-IfSoU--GxOTmVumrUBN3193To06ojPbfZ_YQM4s4IHCYIUDK-NyqseYmQE1rdzN0UKjtExLoRL9jmGPM1epdMObbv7u-iVvBRhcH9Tul6GxLLXrCHe36ce9b-B-y2tU0-awTBsbW-UcU43gtzgyVDNHneotWrExFJbYPvsvQuyx7W1qZQ_bakK1Lr6SaI-HE47DWPfPs1sRGcmxdpRKx-ToJNJNBQGjhMwhu3rXl0GuD7srZWjK2XWEaZUUlDXwjBqPnf9boFLpPayLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
🇷🇺
الجيش الأوكراني يعلن مقتل أربعة من أفراد طاقم طائرة هليكوبتر من طراز Mi-8 بعد تحطم الطائرة أثناء اعتراض طائرات بدون طيار روسية في منطقة بولتافا في 30 يونيو.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81236" target="_blank">📅 19:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81235">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📍
النجف الأشرف:
المدينة تستعد لإستقبال سماحة السيد المستطاب ( رض )
#قوموا_لله
🏴
#باید_برخاست</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81235" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81234">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">20260706_211431.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/naya_foriraq/81234" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#بالوثائق_للتأريخ
🇮🇶
🇮🇷
أعضاء مجلس النواب تقدموا بطلب رسمي إلى قائد الثورة الإسلامية السيد مجتبى الخامنئي لإقامة مراسيم تشييع جثمان والده الشهيد السيد علي الخامنئي (رضوان الله عليه) على أرض العراق العظيم؛ وتعاهده على مواصلة السير على نهج الإمام الشهيد والتمسك بالمقاومة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81234" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81233">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoDsR2ENY4shWkorg5SsuqY6AyzS6LmV_7DD7uzwQCZScmRy-F-MqMIBL1owDz_WqfSe_QViqYtWknhvWthTEwvaG7AtaUniwgglorTP9FXRe23LFII-HqGJYTRbUSfkRLZLXnCCXF_4r1MGMU532AzwZpxxo3-D-nIooWt3ORBlHf4QCmldfKy0RQmatnojT1JHdNzce83sWulanPrLYVsu99C-vgps7PRlxeK45XC1kSZuY4WV0i6GKI4GAyueQ5uMHTe1jNSzvv3ift9Kq9t01E2bhT7ZWn10AKDpeIQzdUa1wcPOa1_0SeJi1-zm_DzGDCYyc3JbcppqLeCbJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسماعيل بقائي: ‏
اليوم، ودّع الإيرانيون في العاصمة الإيرانية قائداً عظيماً، قائداً قلّما شهدنا مثله في عصرنا. وخلال هذا الوداع الفريد، انطلقت الأدعية من الشفاه، وامتدت النظرات إلى الأفق، وكأن التاريخ توقف للحظة ليقلب صفحة أخرى في سجله.
‏لقد رحل شخص مبارك، لكن ما تركه وراءه هو أكثر من مجرد اسم وعصر: إرث من الثقة بالنفس، ورغبة في الكرامة، والاستقلال، والوطنية، ومقاومة عاصفة الأحداث.
‏تحتضن الأرض الأجساد، لكن الأفكار التي تدعو الأمة إلى الثقة بالنفس، وحماية الاستقلال، والمثابرة على طريق المثل العليا لا تتلاشى مع مرور الزمن.
‏إذا غادرت شجرة السرو الحديقة، فإنها تترك وراءها تقليداً بالوقوف شامخة من أجل الشتلات التي تتبعها؛ والبذرة التي تسقط في التربة ستنبت من جديد ببراعم جديدة في ضمير الأحرار، وهذا إرث لن يمحوه غبار السنين.
‏لأن الاستشهاد لا يُنشئ حكومة في العالم.
‏يعرف عشاق أجنحة الدجاج أنهم على حافة الهاوية.
‏على الرغم من أنه ليس من المعتاد حمل شمعة أمام العدو،
‏نحن نبحث عن قائد السيف ذي الدم الحار.
‏صائب</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81233" target="_blank">📅 19:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81232">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏ترامب: مضيق هرمز الشهير، لم يسمع به أحد من قبل، لكنه آلة لجني الأموال الضخمة، سأخبركم بشيء</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81232" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81231">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5df5b7d88.mp4?token=DMGlAzXL7vFtTG_txTnC5OjilhYAtVBU2svCZTIa-4c8UZ4P8bJD98EXPGbgnl5L_q814zX-W0QV7MwK4WMhNPs2Urpv-ikrVwHEFQ9M9sB5ZfVePnysfAp0SMDWbJhhB3kbtDcEUwlEoXsE0Qj8wN1Hx8s2_LeNQ0tzg8Lq5LLZlDmnhgp95OUV61Rd6pdDyt4QTzBVJV-iTkyVTG40KReMY7V4jhMxhUp90cAxw2S8LlCxt1ZQvHruyCW_deS1TXJjYvVy822O-vacRoPOwNvhYMO7ct-S6Aan3uYLZMBNQJh32tNvBxRiSR7WHsFXi9HNG0a9WFCbk3CJ13QlFSL1Lgcz7L_OPjTIMU_yvAOodEvoeDnAPu2jJA6bZAQocqE7f9gWHhWy-nfTrpcD_crRewCdrkHTq7aXqa7pCuRVbO0Y4594cjf_TEjIltXQRNeOcugsbVAMjMAuXVpQyoJdbVP4ZZg7dAOGET_oZsDO5pujcL-JX8xVgEqv0fm9RJObXD9H9tpix9MLbj0-9mLgyN-d16qkUyoZe7xF9OBXcKHx0gGilMx9ymiNPZ1UMGhsGLPkg2rNBwMeWCSZbccOSpsx_940C3mOI-elwMeUeTVVAGcYSFSz475Gzmo_GqtAERV_FvR8prg8bnfSq5jbnQjpX7ewpZYV1FOgCKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5df5b7d88.mp4?token=DMGlAzXL7vFtTG_txTnC5OjilhYAtVBU2svCZTIa-4c8UZ4P8bJD98EXPGbgnl5L_q814zX-W0QV7MwK4WMhNPs2Urpv-ikrVwHEFQ9M9sB5ZfVePnysfAp0SMDWbJhhB3kbtDcEUwlEoXsE0Qj8wN1Hx8s2_LeNQ0tzg8Lq5LLZlDmnhgp95OUV61Rd6pdDyt4QTzBVJV-iTkyVTG40KReMY7V4jhMxhUp90cAxw2S8LlCxt1ZQvHruyCW_deS1TXJjYvVy822O-vacRoPOwNvhYMO7ct-S6Aan3uYLZMBNQJh32tNvBxRiSR7WHsFXi9HNG0a9WFCbk3CJ13QlFSL1Lgcz7L_OPjTIMU_yvAOodEvoeDnAPu2jJA6bZAQocqE7f9gWHhWy-nfTrpcD_crRewCdrkHTq7aXqa7pCuRVbO0Y4594cjf_TEjIltXQRNeOcugsbVAMjMAuXVpQyoJdbVP4ZZg7dAOGET_oZsDO5pujcL-JX8xVgEqv0fm9RJObXD9H9tpix9MLbj0-9mLgyN-d16qkUyoZe7xF9OBXcKHx0gGilMx9ymiNPZ1UMGhsGLPkg2rNBwMeWCSZbccOSpsx_940C3mOI-elwMeUeTVVAGcYSFSz475Gzmo_GqtAERV_FvR8prg8bnfSq5jbnQjpX7ewpZYV1FOgCKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
تطور جديد غير مسبوق تشهده سوريا في ظل حكم نظام الجولاني الإرهابي.. انتشار مرض الإيدز في بنوك الدم السورية بعد تبرع عدد من المواطنين النازحين إلى دمشق من إدلب ودير الزور وغيرها.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81231" target="_blank">📅 19:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81230">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
محافظة سمنان الإيرانية تعطل الدوام الرسمي يومي الثلاثاء والأربعاء تزامناً مع مراسم توديع واستقبال الشهيد القائد الثوري.
▫️
تعطيل محافظة مازندران يوم الثلاثاء</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81230" target="_blank">📅 19:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81229">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8928abb69f.mp4?token=PbI3u1n4bPOIj_S0y9Y8kQtu266Lp6Hg3zZ8ZWHQZAAKmfaDUgsK0EV_TSmsp29HKiKz1A60Mm4A7EaKRT58RcWleDLr9ingrgW4lH10WDfPtkMSuSWBlpv1Rr4ZEvsMnhMjn8cf9L8f6bAt2fNv17M_WaM3Xs6ZiHeXXjN2nafnULUSLqBT2k-xszTdsKTACKE9RKlZgrUEAb5zVGYIne1szTbSSypkmCwXoh9nwC91mcuJh-oNca_ROIZNkTGrqV6IKc2nIFYcsf72__y7rBdb0dq2lg9q6CrK5vGCMI4ICAriBpjIWIomM4PGyrW44rXkrGoqaSUd_xEVNcdPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8928abb69f.mp4?token=PbI3u1n4bPOIj_S0y9Y8kQtu266Lp6Hg3zZ8ZWHQZAAKmfaDUgsK0EV_TSmsp29HKiKz1A60Mm4A7EaKRT58RcWleDLr9ingrgW4lH10WDfPtkMSuSWBlpv1Rr4ZEvsMnhMjn8cf9L8f6bAt2fNv17M_WaM3Xs6ZiHeXXjN2nafnULUSLqBT2k-xszTdsKTACKE9RKlZgrUEAb5zVGYIne1szTbSSypkmCwXoh9nwC91mcuJh-oNca_ROIZNkTGrqV6IKc2nIFYcsf72__y7rBdb0dq2lg9q6CrK5vGCMI4ICAriBpjIWIomM4PGyrW44rXkrGoqaSUd_xEVNcdPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ناقلات جند صهيونية تتوغل في منطقة حوض اليرموك بريف درعا جنوب سوريا بعد سيطرتها على معظم مناطق ريف درعا.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81229" target="_blank">📅 18:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b83f2717.mp4?token=ixcd8jSoKB3rbfkKJ-frzOaHqFd82lH2wCuKH8zh3mQxeE2MT2hlLGb5h37MBt7kK0KzTWh8I6v2RLflza7PJl-XgOcRR8beKX_wUY4rNY77_TmrRbcp4PHtHeLu0ZQM0Rv66nKUb3HwZu4RN8bfUl2bvDqM7bFyqGztXpYneBlTsMlPPH_mXfTSSO74ikn1ENnZQDLJwMck_htZW2TD4uqxxzE7bB8n-Wc7tWDnamLJ-v3Zxr18vhzs0lU7bD3Q_zGg_iK694hrEYduRpxSi1Zbr4Y_IHzOwB2Gk_NpYy8Tdtd0r2HKNIqmQ4mnObm3QJwWJF7Qg2I_i3-4cAr0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b83f2717.mp4?token=ixcd8jSoKB3rbfkKJ-frzOaHqFd82lH2wCuKH8zh3mQxeE2MT2hlLGb5h37MBt7kK0KzTWh8I6v2RLflza7PJl-XgOcRR8beKX_wUY4rNY77_TmrRbcp4PHtHeLu0ZQM0Rv66nKUb3HwZu4RN8bfUl2bvDqM7bFyqGztXpYneBlTsMlPPH_mXfTSSO74ikn1ENnZQDLJwMck_htZW2TD4uqxxzE7bB8n-Wc7tWDnamLJ-v3Zxr18vhzs0lU7bD3Q_zGg_iK694hrEYduRpxSi1Zbr4Y_IHzOwB2Gk_NpYy8Tdtd0r2HKNIqmQ4mnObm3QJwWJF7Qg2I_i3-4cAr0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشادة كلامية داخل البرلمان العراقي ونائب يطالب رئيس البرلمان بالاعتذار بعد وصفه البرلمان بـ"الروضة".</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81228" target="_blank">📅 18:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81227">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة:  - سيشارك أكثر من (3000) إعلامي عراقي وعربي وأجنبي في تغطية مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره).  - ستتولى (2500) كاميرا و(23) مركز بث مباشر تغطية مراسم تشييع السيد الشهيد آية الله العظمى…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81227" target="_blank">📅 17:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81226">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: سيشارك (751) موكباً في مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره) في النجف الأشرف وكربلاء المقدسة، والعدد مرشح للزيادة.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81226" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81225">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e74d73728.mp4?token=ofY9WKWbvvrUuzB6tZ3y4zhdv9zARIq6ar4MBuZdkMxADr0851PnyhPiwO2U2JRy7ww32rZBasYL21js78H-s-qQfoyV9fMyijrp-DJiR6NualbSuF6q3yM3OnqsvzM9pS1X1gdDait-6NP8xGXredR9GAegtIcTgsDdPGiZJCyrmgbfrh1JwESvYLG9CtwGhNcbe33i_BanZQtk80Bjh-bS9MncO33tLtv4o4NILVguH-Et4RV773frvjwuCr-YFCb4Hpn_W51vLA2n3VaVeWrV0gNXGz3fwpPyshPKE6gXL0hOhPa66Zf-E4xyjUPFw7dJUJM1KS2QW1vf_0Mghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e74d73728.mp4?token=ofY9WKWbvvrUuzB6tZ3y4zhdv9zARIq6ar4MBuZdkMxADr0851PnyhPiwO2U2JRy7ww32rZBasYL21js78H-s-qQfoyV9fMyijrp-DJiR6NualbSuF6q3yM3OnqsvzM9pS1X1gdDait-6NP8xGXredR9GAegtIcTgsDdPGiZJCyrmgbfrh1JwESvYLG9CtwGhNcbe33i_BanZQtk80Bjh-bS9MncO33tLtv4o4NILVguH-Et4RV773frvjwuCr-YFCb4Hpn_W51vLA2n3VaVeWrV0gNXGz3fwpPyshPKE6gXL0hOhPa66Zf-E4xyjUPFw7dJUJM1KS2QW1vf_0Mghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: تحدثت مع إنفانتينو، رئيس الفيفا، بشأن البطاقة الحمراء، من غير العدل أن يقوم الاتحاد الدولي لكرة القدم باستبعاد أحد أفضل لاعبي الولايات المتحدة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81225" target="_blank">📅 17:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81224">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامب بعد هزيمته: أفضل الوصول إلى اتفاق لأنني لا أريد الإضرار بـ91 مليون إنسان  مو جنت تهدد بـ"محو ايران وحضارتها"
😄</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81224" target="_blank">📅 17:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81223">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: يمتد خط سير مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره) في كربلاء المقدسة لمسافة (5.8) كيلومتر.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81223" target="_blank">📅 17:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81222">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: يبلغ طول خط سير تشييع السيد الشهيد الخامنئي في النجف الأشرف 6 كيلومترات</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81222" target="_blank">📅 17:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81221">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: اكثر من 600 اعلامي عربي واجنبي سيشارك تغطية مراسم التشييع</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81221" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81220">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: الدرونات ممنوعة وسيتم التشويش عليها</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81220" target="_blank">📅 17:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81219">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: الدرونات ممنوعة وسيتم التشويش عليها</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81219" target="_blank">📅 17:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81218">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب: أنا لست مهتمًا بتغيير النظام في ايران</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81218" target="_blank">📅 17:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامب: أنا لست مهتمًا بتغيير النظام في ايران</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81217" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64db71377.mp4?token=F7U7taMNzpNQ7p26fnhOqVfBhOzWvxm_pJhUPG_oQsYA80S_pDOTO29qJ32IQjSy3xliZk75XTHwITUnv_dvodrEgLOHeSfr1NvvZcdULsHsgPo6KJ0pW1hlR7aVxV6YCZm6MCbO68YZhI_P2vJG1UyKE8Xs3t_IFBi6CjCRnm0aTVJV-joAEYGf0I8KIjlIZOCFAxbSpBUmY6Rq1tpigJfHqm1m_o2OZIjEwunux78dNZ8EFo5DY1SWQHYVMUih2BAV9EKCWz5QiuMk8b7u4TZoozk7FrtekDwXyViV51xnmKrQ0ZqFfaZ59VkOIZrvEPDu_-_eq7caID-9IJ79Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64db71377.mp4?token=F7U7taMNzpNQ7p26fnhOqVfBhOzWvxm_pJhUPG_oQsYA80S_pDOTO29qJ32IQjSy3xliZk75XTHwITUnv_dvodrEgLOHeSfr1NvvZcdULsHsgPo6KJ0pW1hlR7aVxV6YCZm6MCbO68YZhI_P2vJG1UyKE8Xs3t_IFBi6CjCRnm0aTVJV-joAEYGf0I8KIjlIZOCFAxbSpBUmY6Rq1tpigJfHqm1m_o2OZIjEwunux78dNZ8EFo5DY1SWQHYVMUih2BAV9EKCWz5QiuMk8b7u4TZoozk7FrtekDwXyViV51xnmKrQ0ZqFfaZ59VkOIZrvEPDu_-_eq7caID-9IJ79Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب:
الرئيس بوتين يريد إنهاء الحرب الآن، نقترب من النهاية أكثر مما يدرك الناس</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81216" target="_blank">📅 17:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
إضعاف إيران يفتح الباب أمام اتفاقيات سلام جديدة على غرار اتفاقيات أبراهام.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81215" target="_blank">📅 17:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">#ترفيهي
🌟
‏ترامب يقول الامريكيين "اخرجوا واشتروا اجهزة ديل" بسبب تبرع شركة ديل بمبالغ لحسابه الخاص.
ابو جنة فرع واشنطن</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81214" target="_blank">📅 17:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f395cb56.mp4?token=vWcSqZW7bHUb1HD8U0Ns5z9PXvafydkOWu1pVKh2rOhXG1zB0_B03-gwnU6Cm_TsRjgO8CyP9C3rVFXK3kucPa-pHOxd6RgYunsZjmTUqCfIwdmpwhrq0EvThzzgHnNFQINFPI6kLO1x2fLVFP9HyGl8Rb5FF1Tgrk-bqv84ZWrmpknsn_7KHFKPfzQd0UbIlnt7QYZWOwWln8jJ2DOq6KKo21qRHkeHl5o12zBarnS_8ggeHmbXed4gRDfNsjCvbVpI7t3kTzN95prUQUgQaVtRxd8IP6PhL9ojgeUN7iBDnsGznhE520r0YbbJZsE07eyMF1Hmbd45Dn8yOLyBOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f395cb56.mp4?token=vWcSqZW7bHUb1HD8U0Ns5z9PXvafydkOWu1pVKh2rOhXG1zB0_B03-gwnU6Cm_TsRjgO8CyP9C3rVFXK3kucPa-pHOxd6RgYunsZjmTUqCfIwdmpwhrq0EvThzzgHnNFQINFPI6kLO1x2fLVFP9HyGl8Rb5FF1Tgrk-bqv84ZWrmpknsn_7KHFKPfzQd0UbIlnt7QYZWOwWln8jJ2DOq6KKo21qRHkeHl5o12zBarnS_8ggeHmbXed4gRDfNsjCvbVpI7t3kTzN95prUQUgQaVtRxd8IP6PhL9ojgeUN7iBDnsGznhE520r0YbbJZsE07eyMF1Hmbd45Dn8yOLyBOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تقوم بقتل شاب عبر بث مباشر بحجة "الغيرة على العرض" ويلاحظ في نهاية الفيديو سبهم للذات الالهية بعد تنفيذهم عملية القتل.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/81213" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSEX9JHJaYL6gaa4vUkG_KEn8ecnAPRY1YvXxtrQTBFeaKuP4fJETZNbKWguCJWHXixz2wfPcd03hTubr2DZ7inac50iUQOLtXWZOo_ZpDO78f6wP9I8qcOOZrwXtwPix4k-a55IUTY2kfara0YiEopgKi9Jb81O8xW4eFwwD4UVvYpF18YyGu6z0YIal5nWMsyMKl73X0CsIMEjyLk38sC6OeCs-4kTKFQ2iScw8HOqGozfKAUC4s29rZIAz0vUCCgAP0CdrjbAWnZt0KCkndbd97pz9rE79INAaKdCwasnG7xL2PzC83QzFhIdpjmX3Fzdo33kwHkBXj-aRNQQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البيت الابيض يقر ان الغاء البطاقة الحمراء من اللاعب الامريكي جاءت بسبب ضغوط من ترامب على الفيفا !
لا يابة السياسة مالها علاقة بالرياضة</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81212" target="_blank">📅 16:43 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
