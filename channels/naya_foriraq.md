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
<img src="https://cdn4.telesco.pe/file/rSAJnzovQOWwBShyF_UUYH62ory1JlnyCpjX8AqOQNdCc3WMwrllLHmckeRrfcDo7_VxDrGcMZtisT66MFJ_L9_jF_xjJ8iS80Ao_3qf8EKWg54PnE7CfqyWp1SS0cEt2Q4Wj2yuitpZ62l4CQkwy89sFyBnhlpJlmdNkKlZUmdWQ5C4j0jJc8EfjTfDcxydLTYD1XfaSoZofMcfo9UQ9YcIDzY4x0UnHpnOZageSsxIMqc87_SMlnT0Kqyv2z4c1k86M51VyPEHsy19LN1XpsrAQFS4xs634jdvhakKDxTZURDCw3G_HMC48yFIuFu9kNKeH_0molNrE4vZmenJ0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-80373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🌟
متداول:
القوات الأمنية تضبط 11 قارورة مملوءة بالأموال كانت مخبأة داخل منزل يعود لوكيل وزارة النفط الموقوف (عدنان الجميلي) في حي القضاة بمدينة تكريت مركز محافظة صلاح الدين شمالي العراق.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/naya_foriraq/80373" target="_blank">📅 13:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5XBu-Bcp2aCY_Gn2Q3xVa2Xgoqkk52fXwSam8_7D__LUpsVBS_vK2780hybOA1_50YYdbUxyZ7e22g4rc2zS9Ih8PYudUm0UL3lNxUo3Lwn71jXcCYI7y9lp9S5AwtJMQaGLPPuJR-a20gsm13iu1BcyD7JdH1torGFem7QduEIBvWtaE8MkzQp7b0N8JRNpKX0cxkjwpyrEnY_2r5HgHg7PA8Tp8N4uKH9X0RDLOnZplZq1bdxRgVK-FKcF3d5B3qF3FFCLw170PoYjvKtPsUYoJ-21XJaUpqa8yAyM1POlbQ-HEtq_76Xw3Rcd1-e3Acr7XL5ifs3-U3LuCE4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوات من جهاز مكافحة الارهاب العراقي تقتحم منزل في مجمع زيتون بمحافظة اربيل وتعتقل صاحب المنزل الذي يعتقد انه مسؤول حكومي</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/naya_foriraq/80372" target="_blank">📅 13:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🌟
القضاء العراقي يصدر
احكاماً بالسجن لمدة عشر سنوات بحق ثلاثة مدانين يعملون في ديوان محافظة ديالى اقدموا على اختلاس
مبالغ مالية مخصصة لتعويضات الشهداء والجرحى من خلال تنظيم 301 صك وهمي وتحويل الأموال من حساب التعويضات إلى حساب السلف التشغيلية الخاص بديوان المحافظة.</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/naya_foriraq/80371" target="_blank">📅 12:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24675f9dc6.mp4?token=L_KqvVQBLLnNX9sIEz9ArmMmfzGTM_5hLZQc89uLms67gh1RRYzltI7WOSoi7wcBNLJFP1G5p9970lce6Bt9hpw8hKRQtA_JfTOl4ExPu57na3pGFIBlfJoD_HYH4EERL6nwrXrbIEEY6KuEncpaCx443Ww7kPl_fvQbQ_438N4xGTAEiH1LHaEPYsNo_G3pgZZz9EiqraN6WQP5BsrAdjks7yKDmzwgOOwupIW8woE5PTPR1YBF7P7-2p4zvLYmG2rHCCw8DXuwelPdGMDbk9sc77fRXWBnRu2UZyBIwIwSg2eU9AX5vg5TscCg0heZ-q-n94YKn5o1dP7bC_0x-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24675f9dc6.mp4?token=L_KqvVQBLLnNX9sIEz9ArmMmfzGTM_5hLZQc89uLms67gh1RRYzltI7WOSoi7wcBNLJFP1G5p9970lce6Bt9hpw8hKRQtA_JfTOl4ExPu57na3pGFIBlfJoD_HYH4EERL6nwrXrbIEEY6KuEncpaCx443Ww7kPl_fvQbQ_438N4xGTAEiH1LHaEPYsNo_G3pgZZz9EiqraN6WQP5BsrAdjks7yKDmzwgOOwupIW8woE5PTPR1YBF7P7-2p4zvLYmG2rHCCw8DXuwelPdGMDbk9sc77fRXWBnRu2UZyBIwIwSg2eU9AX5vg5TscCg0heZ-q-n94YKn5o1dP7bC_0x-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عصابات الجولاني تعتقل عدد كبير من النساء الشيعيات في قرية المزرعة بريف حمص بسبب قيامهن بتصوير عمليات الهدم التي طالت القرية.</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/80370" target="_blank">📅 12:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في بافيه مقاطعة كرمانشاه الايرانية،شهيدين كحصيلة اولية من الحرس الثوري.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/naya_foriraq/80369" target="_blank">📅 12:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
مراسم تشييع جثمان قائد الثورة الشهيد السيد علي الخامنئي في العراق:
▫️
يصل الجثمان الطاهر للسيد الخامنئي وعائلته عصر يوم الثلاثاء المقبل الموافق 7 تموز، قادمةً من مدينة قم المقدسة إلى مطار بغداد الدولي
▫️
في مساء اليوم ذاته {الثلاثاء} يتجه الجثمان إلى مدينة…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/80368" target="_blank">📅 11:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f940aab8e8.mp4?token=fyB1x6jhgiC8tNDZ02-kuWCNCyw786UqT_jRzXrjffnzfNPIoBgy-qJSTd-Nqi3xHKp1IV4Z3caP8czvf68N8kdtYfyL6B3FJBLFPNO7ysRe_uEcu3AKU6l74pRSnoxHnQODhOxjgZNpY8jNcn7BErCrHittn0T1RirvPmmWZvPZ9HtG6BwEOH936rpL5VIfK_KQzAlnqeS1V76DFfB-U-sykULOzPOol3tccTzGfz445pBD2vvYjA-NtDsx3dqLIAjrMoVKh4g13Dt8gnxgbZ5ZjcRzHRfIypgJBYNT-BFemVxl5pQaSCMkuwNLQXkfVlp_HNuEtRwuUiMJBod_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f940aab8e8.mp4?token=fyB1x6jhgiC8tNDZ02-kuWCNCyw786UqT_jRzXrjffnzfNPIoBgy-qJSTd-Nqi3xHKp1IV4Z3caP8czvf68N8kdtYfyL6B3FJBLFPNO7ysRe_uEcu3AKU6l74pRSnoxHnQODhOxjgZNpY8jNcn7BErCrHittn0T1RirvPmmWZvPZ9HtG6BwEOH936rpL5VIfK_KQzAlnqeS1V76DFfB-U-sykULOzPOol3tccTzGfz445pBD2vvYjA-NtDsx3dqLIAjrMoVKh4g13Dt8gnxgbZ5ZjcRzHRfIypgJBYNT-BFemVxl5pQaSCMkuwNLQXkfVlp_HNuEtRwuUiMJBod_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مراسم تشييع جثمان قائد الثورة الشهيد السيد علي الخامنئي في العراق:
▫️
يصل الجثمان الطاهر للسيد الخامنئي وعائلته عصر يوم الثلاثاء المقبل الموافق 7 تموز، قادمةً من مدينة قم المقدسة إلى مطار بغداد الدولي
▫️
في مساء اليوم ذاته {الثلاثاء} يتجه الجثمان إلى مدينة الكاظمية المقدسة حيث تُقام مراسم التشييع الشعبي
▫️
في صباح يوم الأربعاء الموافق 8 تموز تبدأ مراسم التشييع الشعبي في كربلاء المقدسة
▫️
بعد عصر الأربعاء يتجه إلى النجف الأشرف حيث تُقام أولًا مراسم التشييع العلمائي في صحن السيدة فاطمة الزهراء (عليها السلام) تليها مراسم التشييع الشعبي انطلاقًا من الصحن المطهر وصولًا إلى ساحة الشهيدين الصدرين
▫️
بعد إنتهاء مراسم التشييع في النجف ينتقل الجثمان من مطار النجف إلى مشهد المقدّسة حيث يقام التشييع الأخير والدفن قرب ضريح الإمام الرضا {ع} يوم الخميس 9 تموز.</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/80367" target="_blank">📅 11:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d338d557b.mp4?token=GPXuC2QkJQu8_vwz1HgbGOLJFSqB4kH0wRI9VGtfrrmBTXJG1oEggSoL82dj7xdAZF1u2V072h883nmVtsad6QQh2PongSU6-ZffkKc5oof--n3P_4l7BVqM4TEqJnQD3G5O3g84qf3cKToYOkuPdxYH2EU8-tMr6CKUJDSx8RUfw4godWzuTySn2js68KP7lN8t92zWaKI-u65DYYOIwmYIkSkE7VbMoUrNwwXAycJqSofwZvgzKMHSei_WHb7LwP1JdnDJKicbEkwDlwipO-5yRpuaCqw4TknH-fFyHHKWuruGkflBsLVboEK1vBPNh1dKXLuYqfyp_8DxDaI7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d338d557b.mp4?token=GPXuC2QkJQu8_vwz1HgbGOLJFSqB4kH0wRI9VGtfrrmBTXJG1oEggSoL82dj7xdAZF1u2V072h883nmVtsad6QQh2PongSU6-ZffkKc5oof--n3P_4l7BVqM4TEqJnQD3G5O3g84qf3cKToYOkuPdxYH2EU8-tMr6CKUJDSx8RUfw4godWzuTySn2js68KP7lN8t92zWaKI-u65DYYOIwmYIkSkE7VbMoUrNwwXAycJqSofwZvgzKMHSei_WHb7LwP1JdnDJKicbEkwDlwipO-5yRpuaCqw4TknH-fFyHHKWuruGkflBsLVboEK1vBPNh1dKXLuYqfyp_8DxDaI7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اسرائيل تدبك في الجنوب السوري وعصابات الجولاني تهدم بيوت الشيعة وسط سوريا.. لليوم الثاني على التوالي تشهد قرية المزرعة الشيعية في مدينة حمص عمليات هدم واسعة لمنازل الطائفة الشيعية بهدف التهجير القسري وإخراجهم من بلدهم.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/80366" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80365">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a6b70b88.mp4?token=j82Z2VB5smTbYCSbez7WIpzKsspn8V9kREaWFCpbqYbKzlIifOgmQeOBwh46WotXnEtkVBREUw2cKeITdGi93rVKxC5ELeQcIiPHYHHEUZZH3wnhDbhOZXFYFx2-Fa9ht6RbwCYYcpC50Ao9CrNecBdd1irqJUviJA3Yb_nb5DUg7lXrGCjvM0IqkOvO5Grtainyob5bLDV2RHNmHxcfWrxj6z0bkqBJ0c0Kx_qC4EvRZVwWsI1iYlIzFS-zTxnS-ddyVomaEpSORIZCSSe_bJj3KFlo6QbhFtR1CuL7aqXpfP3G5oRt7Tyvq5TGIDnilE3mZwg2smWxkMDo3hnYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a6b70b88.mp4?token=j82Z2VB5smTbYCSbez7WIpzKsspn8V9kREaWFCpbqYbKzlIifOgmQeOBwh46WotXnEtkVBREUw2cKeITdGi93rVKxC5ELeQcIiPHYHHEUZZH3wnhDbhOZXFYFx2-Fa9ht6RbwCYYcpC50Ao9CrNecBdd1irqJUviJA3Yb_nb5DUg7lXrGCjvM0IqkOvO5Grtainyob5bLDV2RHNmHxcfWrxj6z0bkqBJ0c0Kx_qC4EvRZVwWsI1iYlIzFS-zTxnS-ddyVomaEpSORIZCSSe_bJj3KFlo6QbhFtR1CuL7aqXpfP3G5oRt7Tyvq5TGIDnilE3mZwg2smWxkMDo3hnYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تقوم بهدم جميع منازل قرية المزرعة الشيعية بريف حمص بالدبابات والجرافات وتوجه سكان القرية بالذهاب إلى إيران أو الضاحية.</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/80365" target="_blank">📅 11:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80364">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
ميناء أم قصر العراقي: استقبلنا 80 سفينة في حزيران بينها بواخر عملاقة</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/naya_foriraq/80364" target="_blank">📅 11:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80363">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5dfj3eJ28XNaWOqLlMrxTLuPNiHnaXjoUgaT8Nzif7zbBO1F5yYL8AUTwz1uE-3A8JjxNKrY0aG4tTsTpbP6FEdMGPJ8bFMXP8T63gcuEMyKF4g5PQcPjqU-VvorbWMX4vDXNUX0uHnyjIFWNH5zIRXuxBPVuPradsaMaYt7ktUZC9KRkabSHuhycLcnW8L_hXMLwVJa0vGm5DrZhrPNr4VsjVPXIGTVlXEeGKmLU71WEVxb0gg5ec5wLNWw8hZd89BK4oCEXgcf_TRgN-R9ubYZGLJsvGcp5IFKXgB36bNxao7P8BDTl242p2ir94u4XEGnAi6BOlFUMm36ozePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إعلام كردي: توحيد قوات البيشمركة شمال العراق ولم يعد هناك شيء باسم القوات السبعين والثمانين، وسيطلق عليها قيادة المنطقة الأولى والمنطقة الثانية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80363" target="_blank">📅 10:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80362">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
رئيس لجنة الأمن القومي بمجلس الشورى الإيراني: مضيق هرمز الاستراتيجي جزء لا يتجزأ من السيادة الوطنية الإيرانية وإدارته هي مسؤولية طهران وحدها.
لا تُضمن السيادة اللبنانية بنزع سلاح المقاومة بل بإنهاء الاحتلال والعدوان.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80362" target="_blank">📅 09:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80361">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeASh2Ka_pyNPeCTaD-lciGkZyOvZDBb-b_Y6bjV77MlG7PUIXTOQIIX-DamzqrBGs6EFJH0P5NNDhF6kVqOO3qSDGUTE5ZtSBK1kZh6fY4oed52Aa0VtU98uk4Rkd_kvWraVHsK1iEi4l3EIgjlEly_Mqb2jhr1rBe2dVgtJx3HbF5XWC56zjVXWZZ8vh_waQKMeYSazYt5hGtk57UWyAtJKlOjQZ_HhIiQ2TQurZguxCDXhjMgrE6LcHMwKnmjTz0s9QRCMK-8c5HcS3Y6pP6dIIaHj-sP4xzdfBLFsu7usKS0od1yRm1iOdep1WWEPb3bDs5JLWUyzopCFqBWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Despaseto</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/80361" target="_blank">📅 02:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80360">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في بافيه مقاطعة كرمانشاه الايرانية،شهيدين كحصيلة اولية من الحرس الثوري.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/80360" target="_blank">📅 01:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80359">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a452ae09.mp4?token=Cqzx-FjYC4gLlZ04vgSqbQdC8p94jyYkASXtGW-FjTvYoYQViRHHNjLfc1Go6Nvlk0nxTlJQ60hbzRrwLskE-3Um1IxJxt1qFFDraLLH5veBhgAVQgMYL452z4cM-T_WGqCJiqia3tZBV9U6kilPgkJGtaYsqND3Ma0kg0C3iEgMwmgFXsvReG5gsxMFz-sB1NvBa7KVEFokvXVdDW_JXaQZvd15hVQJG_6fEPqOVUTzD-oOg_hLCMy_u2nRY4qb1EKGlkOe62qcqhfDsUPL5i9BLz4DkZvEPk0bVrf1iuo78pi7L-dZB6I7d9EYS_Ek1UHYS7jM895liOGvtg7nmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a452ae09.mp4?token=Cqzx-FjYC4gLlZ04vgSqbQdC8p94jyYkASXtGW-FjTvYoYQViRHHNjLfc1Go6Nvlk0nxTlJQ60hbzRrwLskE-3Um1IxJxt1qFFDraLLH5veBhgAVQgMYL452z4cM-T_WGqCJiqia3tZBV9U6kilPgkJGtaYsqND3Ma0kg0C3iEgMwmgFXsvReG5gsxMFz-sB1NvBa7KVEFokvXVdDW_JXaQZvd15hVQJG_6fEPqOVUTzD-oOg_hLCMy_u2nRY4qb1EKGlkOe62qcqhfDsUPL5i9BLz4DkZvEPk0bVrf1iuo78pi7L-dZB6I7d9EYS_Ek1UHYS7jM895liOGvtg7nmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
توثيق من تجهيز موقع المصلى لاستقبال الجسد الطاهر للسيد علي الخامنئي، استعدادا لإقامة المراسيم جماهيرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/80359" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80358">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGFwHjBk-rxWrfAoGbNHN39IxOw6DZH8MbRBYjg3xVLLg69_uwN6pIUQVRl64ck4xDAtGLKgM81D7OWg6Ji27AMMWfr8l1kZEIIltqMrt-_SaxxOnYlCfLXqZFbClRnE6DNpgCHbM1EVAKN79Ui-Q-eOyN7K7dfAqpgmQSCjWH-hayxrDLVv_j1EgKu4tMiexjIcZa7gcn5m_nrBuiYJDJmCTs4jElxK0lq2Jb8_1-rAP9hR_SBBhKNGsa_JZn1qZ6C7cT_XxTIe2u1u_h6dewVCTrh-XyrF8UtoHGjOVJ88KknPE1Eyw8wW1LIZfvvfOmaYikagOmm-GkBRkJfpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وزارة الاتصالات العراقية:
الاتفاق مع شركة فايبر إكس على توفير الإنترنت المجاني على طريق بغداد - كربلاء خلال الزيارة الأربعينية.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/80358" target="_blank">📅 01:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80357">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
انفجار في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/80357" target="_blank">📅 00:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80356">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
انفجار في محافظة ميسان جنوبي العراق</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/80356" target="_blank">📅 00:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80355">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مداهمات في منطقة زيونة شرق العاصمة بغداد للمرة الثانية تطال منزل وكيل وزير النفط</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/80355" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80354">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔻
اندلاع اشتباكات مسلحة في قرية يارمجة بمحافظة كركوك، شمالي العراق، بين قوة مسلحة والجيش العراقي.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/80354" target="_blank">📅 00:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80353">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPBPOR2N9lR8UXkK48GZpLOuj4yE1DXZWsiNAv8vhabr9dTdBRvlgvjs87ofe9jPSrbDzOQlpz5DnFzKBEtmCjMH4m-JoVmQM3LvnYiPXMhzOTPAw5CFv-JgRjt3tWbzM6KfBzR9ElShfKTKLouDfwCcJJTITBWrgceBK2mj5jr723fbD2wU3C_JVnh7euObXOGulfz6IgRB-cc-lqabxjweoAZB8a_j43RSaKX_2pofpoaXYSCsiH-dsgIDMzophVjoILDQWBDolgGWzthAUtZygAe6LZcUE-i2z-uEjXTYTDe7MfYbbeVPrRw8Osi6QU3AYriXYmulT6mqJ95RSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
توثيق من تجهيز موقع المصلى لاستقبال الجسد الطاهر للسيد علي الخامنئي، استعدادا لإقامة المراسيم جماهيرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/80353" target="_blank">📅 00:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80351">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGkpZvt4FXfP2VBwP1jjIT67gKSOR3WPDsjA2wGHpXuQJ8KkWyiiwuk8eN24L7ua4bc83V-EDdq8et4ZsCqSPCldzDFhoAQ6GMbsZT1ncXv74ckBx3c-yWkoGERw6qt0yxMvbTAhP592-2CVdRaONqwlZJOmdS4s1Wfm5RhcDLQ6g0efSfJ16kUYSjiIxsInZlaHS0Dlcl6RseNxNxoYK2AMzbta2sROd-zvAeKAR5PB6QciCF9wQbQHBep5VtxnogCDf9QT43Mn5Pds7MPssLQiGMrDNrrA8TOhxEMKzBjOuLAM5AUCJYru5KiAxnPfOqUTqWXFmuyFjjV0rEbWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7da4bff7.mp4?token=B9CBUP3B078hiEIRgz3qeZYNbhXN8nqm8OP3thixDxncS6VHG5GWrZpc2e_NkbIzjMrXJKe8uTJzWvddwmaX1uh1aeOB1AmCHekxbxDk8qkyVE14lHWPKaLs5mz_JFv7VdnYB78F12ZhX8KPmG8HCJl7qn9dgoWuHw7kd1RgZXdTKCnrH8bGmuTp7geCLz865I6Y4kTA-lbrWgwzKT5_dV9hYEDqGmXMZ-CYVr-7nG8V3tDClok6m2GLI9wrcppsY8GN7jkYDMW9v5B-BiSAdNFQ7jtyEADz376bwlQp16f4cZCC5Id2XaVk5oEwxgYaUtw2z5VdjKf7LjW9X6jLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7da4bff7.mp4?token=B9CBUP3B078hiEIRgz3qeZYNbhXN8nqm8OP3thixDxncS6VHG5GWrZpc2e_NkbIzjMrXJKe8uTJzWvddwmaX1uh1aeOB1AmCHekxbxDk8qkyVE14lHWPKaLs5mz_JFv7VdnYB78F12ZhX8KPmG8HCJl7qn9dgoWuHw7kd1RgZXdTKCnrH8bGmuTp7geCLz865I6Y4kTA-lbrWgwzKT5_dV9hYEDqGmXMZ-CYVr-7nG8V3tDClok6m2GLI9wrcppsY8GN7jkYDMW9v5B-BiSAdNFQ7jtyEADz376bwlQp16f4cZCC5Id2XaVk5oEwxgYaUtw2z5VdjKf7LjW9X6jLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‏شرطة موناكو: انفجار كبير إثر عبوة ناسفة ثلاث ضحايا كحصيلة اولية.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80351" target="_blank">📅 00:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80350">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a4a7c7ec.mp4?token=j82OoIYc0T77C1h2OmY1k-iy6C6tcBSunLFrVoE88QTcckHqFKKB7XMpkdvqL7xzoY0fBxmqUgFWPscCDB3EOQFRmP8TOIqSkKCfvrMlJw71y2Nj-hSnEjHaTj4tYcy1KufTLz3fGUZ_4Y8QOO3acdQHt1e_F6O1j5Q14afndzHtUPvTqKWOk4Fle3XbiuP67VuB8lcJEynlntVf1trAk4laPbaxf7QrkZO4YGM0v1Wrn896X92w7HGixRlHptUHV_X3oP-erm-XYD8EX10DvtVpTMbjWPAEAZCnacCcwKt5K_IPrgwgEFcX_3ylO6B6hpbkeyBp_bWgLa5BfkPylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a4a7c7ec.mp4?token=j82OoIYc0T77C1h2OmY1k-iy6C6tcBSunLFrVoE88QTcckHqFKKB7XMpkdvqL7xzoY0fBxmqUgFWPscCDB3EOQFRmP8TOIqSkKCfvrMlJw71y2Nj-hSnEjHaTj4tYcy1KufTLz3fGUZ_4Y8QOO3acdQHt1e_F6O1j5Q14afndzHtUPvTqKWOk4Fle3XbiuP67VuB8lcJEynlntVf1trAk4laPbaxf7QrkZO4YGM0v1Wrn896X92w7HGixRlHptUHV_X3oP-erm-XYD8EX10DvtVpTMbjWPAEAZCnacCcwKt5K_IPrgwgEFcX_3ylO6B6hpbkeyBp_bWgLa5BfkPylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في الوقت الذي تلاحق به عصابات الجولاني الشيعة في حمص وتهدم بيوتهم وتهجرهم إلى الضاحية وطهران على قولهم.. جيش الاحتلال الإسرائيلي يبث مشاهد للرقص والدبكة من وسط المدن التي تدعي حكومة الجولاني أنها واقعة تحت سيطرتها.
نشوف اليوم ينزل بيان إدانة ولا تبع مبارح بيكفي
🙈</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80350" target="_blank">📅 00:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
‏
الرئيس الإيراني:
سنلتزم بمذكرة التفاهم إذا التزمت بها أميركا.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80349" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔻
‏
شرطة موناكو:
انفجار كبير إثر عبوة ناسفة ثلاث ضحايا كحصيلة اولية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/80348" target="_blank">📅 23:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80347">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba122719bb.mp4?token=FPfnebCxYEf1cpZ_lHeZ6nDDJhE6GjN7PReXvSU6jtSGQI3Oh3SFWizKjX_sf7OlpxMMm6AxhhSi_t5hITaQ1p7Pz77gfZMh75IbhmuoSgfqGegGypOlTEZBOCZrJ4Asha2OzkenEbtJnKWmKrqy6VlRoTpsdNDa7acbz1CMdaWwvcC0HRjeEMe6AGdWZWUM4PhwMQO28py6jdLrIkrFoBhj7l1ZXFAvwbkXQX0BL7a18BbT30FWwNnmALIh4IiWAX__sv6d8E-oZGRR0E6cyaT_hBLa_1e4Hzr8z05MO2unIfsC0cWhXHPsAaLhwGzScEMqMRthEvTDkQLQnzoumA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba122719bb.mp4?token=FPfnebCxYEf1cpZ_lHeZ6nDDJhE6GjN7PReXvSU6jtSGQI3Oh3SFWizKjX_sf7OlpxMMm6AxhhSi_t5hITaQ1p7Pz77gfZMh75IbhmuoSgfqGegGypOlTEZBOCZrJ4Asha2OzkenEbtJnKWmKrqy6VlRoTpsdNDa7acbz1CMdaWwvcC0HRjeEMe6AGdWZWUM4PhwMQO28py6jdLrIkrFoBhj7l1ZXFAvwbkXQX0BL7a18BbT30FWwNnmALIh4IiWAX__sv6d8E-oZGRR0E6cyaT_hBLa_1e4Hzr8z05MO2unIfsC0cWhXHPsAaLhwGzScEMqMRthEvTDkQLQnzoumA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
تحليق مكثف للطائرات المسيّرة في سماء العاصمة بغداد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80347" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ec5551c0.mp4?token=D6rIHKRO5RJLHuc37oO7EifmHKjJKhuKtgTVJlGpCb7FLfIyLRx0oaPgRh6InAdlIwLTP5mLCvlKmW116gw0UoqRsNLu7fdrzPG7Vbg7FkHVxSqu55e3lWIMJQZNSNcje9qZOXBVDGY3Nlirnf0Datm-9KuN5NhicJffM7UP1EvhkWEsijXernEUQPRa47v2QpoIZZQuFOV3jmQgOL1tWg_iSKRP-RF_MLQKIJsmKkjFOntbjsESZNYnbNux9N10Taig7-XJU4n8d7XPieRhZmMaCKLpqdhO-dBeUv7nqvWeQwxygUzHxOh2clVPkWLF1kso3Rfi-gI2RBuoFquA7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ec5551c0.mp4?token=D6rIHKRO5RJLHuc37oO7EifmHKjJKhuKtgTVJlGpCb7FLfIyLRx0oaPgRh6InAdlIwLTP5mLCvlKmW116gw0UoqRsNLu7fdrzPG7Vbg7FkHVxSqu55e3lWIMJQZNSNcje9qZOXBVDGY3Nlirnf0Datm-9KuN5NhicJffM7UP1EvhkWEsijXernEUQPRa47v2QpoIZZQuFOV3jmQgOL1tWg_iSKRP-RF_MLQKIJsmKkjFOntbjsESZNYnbNux9N10Taig7-XJU4n8d7XPieRhZmMaCKLpqdhO-dBeUv7nqvWeQwxygUzHxOh2clVPkWLF1kso3Rfi-gI2RBuoFquA7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد توثق دخول قوات الأمم المتحدة (UN) إلى قرية عابدين في ريف درعا.
جولاني وينك بدنا البانجان مجقجق باللبن
😂</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80346" target="_blank">📅 23:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔻
المحكمة الجنائية الدولية تفتح تحقيقًا مع مسؤولين كبار من الإمارات العربية المتحدة ودول مجاورة، بتهمة المساعدة والتحريض على ارتكاب جرائم وحشية في إقليم دارفور السوداني.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80345" target="_blank">📅 22:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
الإطار التنسيقي يدعو جماهيره إلى المشاركة الواسعة في تشييع الشهيد علي الخامنئي في الأراضي العراقية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80343" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
مسؤول أمريكي:
دورنا يشمل استخدام قوات أمريكية على الأرض في لبنان وإسرائيل
عون وينك السيادة عم تبكي
😫</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80342" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80338">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtcvaVL9DDn4HjaQRSnAmEMdZrRR7ULGGGjQa-7EJEbzvwyf_O7DSFoU4vlcM-C4OcACvkIMPW_wg68v1KebE1TIAcpL5FGrdcO3XT3gPO2nXznZgnfYAhIlhMeMQDbS0V4ZURnY2ajSRXzN9nO0kSNrBscBbH73gJtNplVlD6IBKiuhgSJMRYIW6VmP8in4iy3TkGA_s0DlS4zqBkWhy7VQpIVgUVhKIsLs7ujAL8FJCKBAMP3IcCpomHdy627mg5x6sjwa4-QXom9BVM2k_Zh247H4esb_I819pvC6aumO1Gcohn5NABgoLiBtlsMGUq-atVx62gLVmTHYnUgpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-oVArYeBarLigi1_AqN0si3Z_Ebmyiodn7qpXdJbiu2rgZ5Rel_oYIpeTuUP18zHSRQpQt6B2Y0ELBF3YkNicj17_lQfNcM5-sOT-y48IZeIUNpowmDmef7-2y8tZsScPbcgIqgSsq_hFdBAk1PIQxFrngrtCT30OauZ_dhofxf-MF4oKTkBcj-Is1CqbfBh9B1SE5HDPPUAjz0x6yVBX3V6iT_Pq2cRovwnZ0v-BgHafb-He5ge0gbuJhaXSF7DBYQ4PtH0SBpwHyPp2ASYNAHfZvzy2Wa-ET7lQfpvLCB32G7bt6Fqfh3D_9591OY3oDB2qd3ydJ7YcL6TYE0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUG_Av_A_fOu0NUOHJZA8clSDXWw0y2kknf169krx84zuW8dUbjID32P7JM7z2WTQE5-NpAJBH_fAgunG8yi5jXGhFAyjeEIp9KTYlW6KL6ern7kMPgH5qU4gHjVvuVeSy9cidvsT56OjI6SEf52Ep8QnzbqBXSxfGd_ZWF725-y37qHEZuftMc7cCI_MI8AFbQviGTBVtDuxxmSbLwd1IaaSohlCjdz_8n9SBXhYvWMyQeU9TBJ6ig2WtVZfv36bez0cORIGIAaGNkI_IxD7Wfby3-9RUiXX-jcXWg-6EpphuSmqRSB0UWXKMruCnCRaeU0lWAvnd06eC27DiG3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5768GxrEkr-z-k_UDuZ5OuXQmztnYUh9Dni4LivSESdfCzoACfHmdR31D60WEmKxsxZPjH9Z8aB9MNBPAZyTiLcuVaw6UOweHwKsQIZIChU0oFrvc7e86okE330CxkLU-417KjdROQVdIZmN2q6uyqRx6-U5YjNwaEHofAndQHH-jPvTCVsceHIxevPG16JaGgyS8Ihvp9lfb0doNjW--oyqqv5iAfADGtphddFblStekhc2E4cbjRs2LVbBcXATHo_nPHubHnUXrkYeyXUuajjF01HIeSRUkKePEWOH1SyEgDmWlGfgX7bo5v3j_Jz24z_3Ru0HhoO1Or6z4Qu1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى: التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/80338" target="_blank">📅 22:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
🔻
مجلس القضاء الأعلى:
التحقيقات مع وكيل وزير النفط لشؤون التوزيع تسفر عن ضبط 11 مليون دولار و4 مليارات دينار</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80337" target="_blank">📅 22:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي:  وفد خبراء إيراني يتوجه إلى الدوحة لمتابعة تنفيذ التفاهمات.  زيارة الممثلين الأمريكيين إلى قطر لا علاقة لها بزيارة الوفد الإيراني.  لن نعقد أي اجتماعات تفاوضية على أي مستوى مع الجانب الأمريكي في الأيام المقبلة.…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80336" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=SUsb6bbUOApoacbTImXxIJLI8EwmEi_kvw_wF6KQore3GVln6hp3PS9N4qzPnhUgQIvTZP959jx59htbyXWKLwc_xXLlyyzX_fg2Z6pj9dWKslm2VoibRMZlPq6719yigaWlUENe5RvMBbAuVrlCdyP_sO8OEVy7L_JIOT2g7qJcTY7d3caw-eMLJGVEuUE1xBpqhVtmtoYR9xqulRpjkXjRoSIV4sxdtdMn17VuxCE3e0XHhzgP-R8jnVZRo_KVQ7zym2EdOaviowANBrkNIhylLWnhOmSgP8-CNpjOVlEQsPhvGonHL52tV-z2HFg6xQOZK97BflNTQLU6Nfv_Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a3817a74.mp4?token=SUsb6bbUOApoacbTImXxIJLI8EwmEi_kvw_wF6KQore3GVln6hp3PS9N4qzPnhUgQIvTZP959jx59htbyXWKLwc_xXLlyyzX_fg2Z6pj9dWKslm2VoibRMZlPq6719yigaWlUENe5RvMBbAuVrlCdyP_sO8OEVy7L_JIOT2g7qJcTY7d3caw-eMLJGVEuUE1xBpqhVtmtoYR9xqulRpjkXjRoSIV4sxdtdMn17VuxCE3e0XHhzgP-R8jnVZRo_KVQ7zym2EdOaviowANBrkNIhylLWnhOmSgP8-CNpjOVlEQsPhvGonHL52tV-z2HFg6xQOZK97BflNTQLU6Nfv_Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
طيران مروحي يجوب سماء محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/80335" target="_blank">📅 21:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭐️
هجوم إرهابي يستهدف عجلة في مدينة سراوان بمحافظة بلوشستان الإيرانية ؛ إستشهاد شخص وإصابة أخر كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80334" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">البيت الأبيض: ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80333" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnl733bVDhXZFdH43FFPq9p_kCI2SP2QYiHjj_nc39SzbOuzOMwjpjDhVrnwI0YfgZk7fQesB-nPbreN5gkMs5yCpiqhgIoToQOaOuO0BxoEPhINU9kygM_anlZfBcSJZ02zdJt8Ng3VW8UNo2xXb9LPv7PFdLcVRYt5aDi8aN5HL4DSF2vzMcpkWgAPW7WCc6pI48wKs_a83ztgDyb7RbKCeimsHeB2AFvmXjRaM1-DzvLQib5-1gkrAPat4cjUakMdJmmyG3PQUHwPCwtIUMy8_McwPaIO9Rm35eVZLmkDroxfvyeFGHH4Nxk46BUn09Rn7c6MJe0oQgixLR6VGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
قيادة الحشد تبحث الاستعدادات للأربعينية ومراسم تشييع السيد الشهيد الخامنئي.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80332" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تحليق طيران مروحي إسرائيلي بأجواء عدة مناطق في حوض اليرموك.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80331" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اعلام العدو: تم تفجير عبوة ناسفة استهدفت مقر القيادة الميداني لنائب قائد لواء الكوماندوز في جنوب لبنان. هناك مصابان من جنود الاحتياط في الوحدة. أحدهما في حالة خطيرة، والآخر في حالة متوسطة، وقد جرى إجلاؤهما بواسطة مروحية.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/80330" target="_blank">📅 20:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80329">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية تحذر فرانسا:
إيران وحدها ستتولى عملية إزالة الألغام من مضيق هرمز بحسب مذكرة التفاهم.
لن تشاركنا أي دولة في نزع ألغام مضيق هرمز ولن نسمح بذلك من حيث المبدأ.
الوضع في مضيق هرمز حساس ومعقد وننصح فرنسا بشدة بعدم تعقيده باستفزازاتها.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/80329" target="_blank">📅 20:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80328">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/80328" target="_blank">📅 20:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80327">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
🇮🇷
مسؤول أمريكي:
أوضحنا لإيران أننا لن نفرج عن أموالها المجمدة إلا إذا تحقق تقدم في الملف النووي.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80327" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndWeowgaHO_7XA2b5ho0GpOflW-lQAb5B16_xSCefdchjoYARF2Voo4QRo9On2T4pbuyND6n0ICvJ9zxeeR0i2ycvxhJAGCABWs5-oMM_rsf0MNq5CY1ZFHwH9SdCP9Z3PwVUsZSPMlQSf3A9BnQqHxL0Smt0xYdhnIjyDdvF1s7EqVsiM-sHzV9RD3Uk7r2LBx760Yt8xSC1HyOa-errel48fvuC0Br32a1hl0FAHvHZsbzQBhzD8EfwiZ7Wwhfq4bOlBzmMF7oS6dimkoeKzC8WeLLQoB_e6nLceTCUzgoeO1ihkmX8ufY7-IW8_ZqZ_ozxn4Tla0joId5xLyeFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏ترامب:  «انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/80326" target="_blank">📅 18:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80325">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴‍☠️
وزير الحرب الاسرائيلي:
نتجهز لمعركة جديدة مع إيران في اي لحظة يمكن ان تحدث ولن ننسحب من لبنان.
اندلاع الحرب مجددا مع إيران قد يحصل إذا قرر ترمب أن المفاوضات استنفدت أو أن تهاجم إيران إسرائيل.
معادلة هجوم حزب الله على مستوطنات الشمال تساوي الهجوم في الضاحية لا تزال قائمة.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80325" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80324">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXvhifz-DJIwMPg5hjPSzHMppWeD623HDJWQjvEIXiIeSqPUtlx8qkxN2iMpQNH0RG7G52EA08HUzVegIocdSi9I0tpDaOwCaZQkWthkYaHOjRdxatHAzleJMvbxUbFuANPSA2AkKNjxzpNVPOeWhaQp8-PjyFdjOx3xhs1rHMYo90a7WhTK87yf0EJn0euCHpqDyhTckxLeF1-jYV7yuUfTGtzjaZWVFnfNgIzaWLhuouwlxTnhPCfstIi2Pms8btsS6rVPpc3PiT9CervrwgQDzB6l40rQTuh_wN3qrZpCVI115o3RF19Aqm-mMiJG9DHVBhQKxjpJrhrwHis3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
«انتصارٌ كبيرٌ قبل لحظاتٍ في المحكمة العليا، في قضية سلوتر، حيث تمّ تأكيد سلطة الرئيس في بلادنا لعزل مسؤولي السلطة التنفيذية والمعينين في الوكالات، أو الممثلين، بموجب المادة الثانية. لقد سعى رؤساء الولايات المتحدة إلى هذا القرار منذ زمنٍ طويل، ويعود تاريخه إلى ثلاثينيات القرن الماضي. إنه لشرفٌ عظيمٌ لي أن أكون الرئيس الحالي الذي حقق هذا الحكم التاريخي وغير المسبوق، وهو أحد أهم الأحكام التي صدرت على الإطلاق فيما يتعلق بصلاحيات الرئيس. شكرًا لكم على اهتمامكم بهذا الأمر!»</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80324" target="_blank">📅 18:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قد يغرد …</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80323" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
وزارة المواصلات القطرية:
حرصا على السلامة العامة، تهيب وزارة المواصلات بجميع ملاك ومستخدمي الوسائط البحرية، بما في ذلك قوارب النزهة، وقوارب الصيد، والدراجات المائية، وسائر الوسائط البحرية المماثلة، التوقف مؤقتا عن الإبحار وممارسة الأنشطة البحرية، اعتبارا من تاريخ صدور هذا التعميم وحتى إشعار آخر.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80322" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
العثور على جندي بالجيش الإسرائيلي مقتولاً في وسط البلاد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80321" target="_blank">📅 17:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزارة التربية العراقية تعلن استرداد أكثر من 73 مليون دينار لخزينة الدولة في صلاح الدين بعد متابعة دقيقة لملفات التقاطع الوظيفي</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/80320" target="_blank">📅 17:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رئيس الوزراء العراقي:
يوم 30 أيلول المقبل سيشهد خروج قوات التحالف بشكل كلي.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80319" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
احسان العوادي رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:  لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80318" target="_blank">📅 17:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🌟
احسان العوادي
رئيس اللجنة العليا لتنسيق مراسم تشييع قائد الثورة الإسلامية الشهيد في العراق:
لسماحة آية الله العظمى الإمام الخامنئي (قدس الله نفسه الزكية) مكانة رفيعة ومتميزة وقدم هذا القائد العظيم خدمات خالدة لأمن العراق وعزّته وللعالم الإسلامي، أنّ إقامة مراسم تشييع سماحته في العراق والعتبات المقدسة تمثّل شرفًا تاريخيًا للشعب العراقي، أنّ الحكومة والشعب العراقيين لن يدّخرا أي جهد لإقامة مراسم تليق بهذه المناسبة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80317" target="_blank">📅 17:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏وزير الحرب الصهيوني: الجيش اللبناني لن يتحول فجأة إلى أسود تهاجم حزب الله.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80316" target="_blank">📅 17:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0C-w0qQnSL2-29exCdmz7pqqMq1AzsaUnrBuej9vJHoSoUCwql2rkP_EXnTRE7yDoJOc3Sb3DCIls8HAuDwVph6dlvFakkaHF3lKqVgiMQ1-l6u9yjUWwzWJkB0yBB1PeM8Zn7eROLucJT3FvU5Vff683MNRZjxqG1KSPOXJjV6Af6_R8UfiduWvPi0j5bRXDB6KjsMoyFKzUvqupcbGnbkEAKbM3zipXGLI_OL0bZJI8n1vQG_uS8MLDbxKgUAv8YSkT6JvAC-YNPRQe1B8N_s8aPapqR-ByyKBGGg8Hrm-Az4SFfMm-quuaZ0tWcQAfGI0CZHCgeChme68-kT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزير الخارجية العراقي فؤاد حسين يلتقي الارهابي ابو محمد الجولاني</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80315" target="_blank">📅 16:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏وزير الحرب الصهيوني: حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80314" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
وزير الحرب الصهيوني:
حزب الله عزز وجوده في الجنوب بسبب ضغط ترمب على نتنياهو</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80313" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=gSt8guwwBpUERGboDqZ72n-IOhFttOl4JaMpvtq60xmWqP2hB4DnKgKu46iSR6LrYwcyfL5bkEqLqYfYVt1fNrMErUWj2JbhWT1bpc3Xl4-lDBQ6fad8-A4PsJw8yJhlVhQNhLBwNwDOFoRIkkSUdjbRbb13Q93N5FoREaQEK1sQLvPY-OI8syvqouwKcX7R6Y0rm_13K1uKjXHzargr6yWU-AzjN6DXAey1H1s6lu8VaviQWkNd7lKrFGEI-56kFD5Ap5h2uccoGe7_PM6lyklogB14Zy6JLK0Fj0z0nKK2vtulOZDwmp1CICHJbb-3wDzaHB9phimSi8FEqlnD1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760337d8fc.mp4?token=gSt8guwwBpUERGboDqZ72n-IOhFttOl4JaMpvtq60xmWqP2hB4DnKgKu46iSR6LrYwcyfL5bkEqLqYfYVt1fNrMErUWj2JbhWT1bpc3Xl4-lDBQ6fad8-A4PsJw8yJhlVhQNhLBwNwDOFoRIkkSUdjbRbb13Q93N5FoREaQEK1sQLvPY-OI8syvqouwKcX7R6Y0rm_13K1uKjXHzargr6yWU-AzjN6DXAey1H1s6lu8VaviQWkNd7lKrFGEI-56kFD5Ap5h2uccoGe7_PM6lyklogB14Zy6JLK0Fj0z0nKK2vtulOZDwmp1CICHJbb-3wDzaHB9phimSi8FEqlnD1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
حكومة الجولاني تقوم بهدم جميع منازل قرية المزرعة الشيعية بريف حمص بالدبابات والجرافات وتوجه سكان القرية بالذهاب إلى إيران أو الضاحية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80312" target="_blank">📅 16:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌟
🇮🇷
وزارة الخارجية العمانية:
عقدت اللجنة المشتركة العمانية الإيرانية اجتماعها الأول في مسقط بشأن مضيق هرمز لتبادل وجهات النظر حول إدارة المضيق مستقبلاً والمسائل ذات الصلة.
ناقش الجانبان سبل تعزيز التنسيق بشأن القضايا المتعلقة بمضيق هرمز بما يتوافق مع المصالح المشتركة للبلدين وسيادتهما، مؤكدين التزامهما بالقانون الدولي، واستكشاف أطر التعاون في مجالات الملاحة والخدمات البحرية، انطلاقاً من كونهما دولتين تتشاركان المضيق، وفي ضوء التفاهمات الثنائية والدولية القائمة.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80311" target="_blank">📅 16:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🏴‍☠️
زعيم المعارضة الصهيونية لابيد:
لن يشكل نتن ياهو حكومات في إسرائيل بعد الآن.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80310" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c356325e.mp4?token=DBzOwLpK3DLLp07bBvpsVI3dsZXpJjcF6Zt_WHrow3oHh48GjXmRS9OmlnYmI_rdSF0PLXv7H0W8Zauh7qV9H_eRfr3_gOZyxOFraXJlmVqhQZbC-qzFxWWoOvHTIPo4XbuJgJf76pLCW175SqMJ-eJ2HGJrp2XHqDmVETzIQNKHVG9tJtlIDJJiKwH5y7XuWCL5nqY6kHNkWOOOBi5Nwmi-G23I4U1f8a_Lj-zpj9as9Cr5Set16rggPUrmGbqKvEYYBCS8xgrU9RzU5FvLj-1BRUJlbuDfEKl6Mh0Rbbsc-UUnX8LGqBMI_IuFsDs7K44StyW0rYlFNNVZ7JJvfo7s3y08k9VWKId6ZcyXKMZIZhM_X3hR7gIzOnd97NI6Hee7z-xR5R2iwhDaoU6LMD_VESLPYXKKN-IqqLt7mvgWqP08Ix0xHYu-oLBO2SW3yWGkMm8H9pCy490i-frdU1nuOFewruJy76tqa0IQcPMJHak9dd9u5nriXRN2hazvNbUwxNqS8OOmRDxXE-PsPfIk7xnEENgp5VqjR_6vuuaUQt-uY_4X9hiESAYeRoKSHjfPYOmJzqyo7UCb7SQCIsxKIw0yb692q4I1EzdZFArIJYxM9NqyE968SU_aIXEkt5n7LerGWrOV0DypDlM3X_bJsV4S_tp_LZS_L3EAI6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c356325e.mp4?token=DBzOwLpK3DLLp07bBvpsVI3dsZXpJjcF6Zt_WHrow3oHh48GjXmRS9OmlnYmI_rdSF0PLXv7H0W8Zauh7qV9H_eRfr3_gOZyxOFraXJlmVqhQZbC-qzFxWWoOvHTIPo4XbuJgJf76pLCW175SqMJ-eJ2HGJrp2XHqDmVETzIQNKHVG9tJtlIDJJiKwH5y7XuWCL5nqY6kHNkWOOOBi5Nwmi-G23I4U1f8a_Lj-zpj9as9Cr5Set16rggPUrmGbqKvEYYBCS8xgrU9RzU5FvLj-1BRUJlbuDfEKl6Mh0Rbbsc-UUnX8LGqBMI_IuFsDs7K44StyW0rYlFNNVZ7JJvfo7s3y08k9VWKId6ZcyXKMZIZhM_X3hR7gIzOnd97NI6Hee7z-xR5R2iwhDaoU6LMD_VESLPYXKKN-IqqLt7mvgWqP08Ix0xHYu-oLBO2SW3yWGkMm8H9pCy490i-frdU1nuOFewruJy76tqa0IQcPMJHak9dd9u5nriXRN2hazvNbUwxNqS8OOmRDxXE-PsPfIk7xnEENgp5VqjR_6vuuaUQt-uY_4X9hiESAYeRoKSHjfPYOmJzqyo7UCb7SQCIsxKIw0yb692q4I1EzdZFArIJYxM9NqyE968SU_aIXEkt5n7LerGWrOV0DypDlM3X_bJsV4S_tp_LZS_L3EAI6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المحلل البحريني جعفر سلمان المقرب من العائلة الحاكمة الذي كان وقد وصف العراق بـ"جمهورية موز" يقول في لقاء انه لولا الامريكان لكان الخليج لقمة سائغة امام الجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80309" target="_blank">📅 16:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هيئة النزاهة العراقية: السجن لمدير عام الهيئة العامة للضرائب الأسبق وزوجته عن جريمة غسل الأموال. الحكم تضمن تغريمهما أكثر من (32) مليار دينار ومصادرة عقارات وأموال داخل العراق وخارجها ومصادرة (22) عقاراً في بغداد وتركيا باسم المدانة وبدلات إيجارها ومخشلات ذهبية عائدة لها ومصادرة الأموال المودعة في البنوك التركية والكويتية العائدة للمدانة</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80308" target="_blank">📅 16:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80306">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vHLNLpIk9SpYLrOdQqHkGKM72GdOiQoCqCo9wzfT6AunRQuN3ogRSy97DUrY7mo6oMgJyCRu4Z86xQOxQZzywKPF-rKURC6a2uZaUadD69juett0CVt03uYTYm7P1HzsvE2fnrdI3L6DLfuUnodlw9wgabko3-6ZiVV_pLLR_XPbON7st3HdDutI3imhZ9B40ypalsrKxwGImFgpFLqmdztbUuCUatJn9FzbC8CssVBJp0ctOOBxIOxVBwj0KJaxWKwXHgH8AKIfHpvhDTMbrIa8l6FFHRcK_bXIAWBlwU5GndjOKLLIpoxV0TqhuYu7ZOiMkMbl-CdK0GmlGQBzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-TLfnrQLDB4G8sulIFmd1cTtcwCzELdcABAihwXPK_raVbhuPAZhM1MB7LJfqmFb4aJjwij-1Y2Gdw0UHt0yUdmQsEUo02LTyxlZJVNp0yFbJyjuSksegynzoCOyAypN7mKgwlfch-hls9CNwOHDliLYHvGBiekL2uHSl5XFllyZ17tGQSsVE5nQZ_slllAz15eYGJsIXU2gD1caC1JBZm1O0kKw_5sPllcBr4MGM0-gPx7ONiY6ss14Pr_P1mItefHKFetTHVQbe6JIe_g23HbdkdHvzbh55Osd430uk6I7OwXcQid46Pj4DahGQm6wKmZqyqPELk9JQOZda42_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندلاع حريق داخل جامعة الانبار غربي العراق وفرق الدفاع المدني تستنفر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80306" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80305">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قوة امنية من بغداد تصل محافظة ذي قار للبحث عن رئيس لجنة توزيع الأراضي في المحافظة بعد ان وزع 1500 قطعة ارض مقابل اموال ثم ولاذ بالفرار</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80305" target="_blank">📅 15:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80304">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رئيس الوزراء العراقي: نسعى إلى آلية تقسيم مُنصفة ولا تجحف حق العراق والعراقيين في منظمة أوبك</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80304" target="_blank">📅 15:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80303">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">البيت الأبيض:
ويتكوف وكوشنر سيحضران في اجتماع الدوحة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80303" target="_blank">📅 15:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80302">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اعلام العدو: حزب الله استهدف مقر بداخله كبار ضباط الجيش الإسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80302" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80301">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏴‍☠️
اعلام العدو: حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80301" target="_blank">📅 15:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئيس الوزراء العراقي: زياراتنا المقبلة ستكون إلى تركيا وإيران والسعودية بعد واشنطن</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80300" target="_blank">📅 15:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80299">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇩🇪
الشرطة الألمانية:
مقتل خمسة أشخاص في إطلاق نار في ستاد، شمال ألمانيا.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80299" target="_blank">📅 15:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
حدث امني في جنوب لبنان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80298" target="_blank">📅 15:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
إطلاق رواتب مجاهدي هيئة الحشد الشعبي.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80297" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqBl71aoRGD8rJ9wqsWyFZ-dRWvUCM1z7XGbZUe1JkBRhhhYn5EpaibcRVVV2HkfJ1BF81cu21hsC8snhsDnuH1G_BjeMFL_VYmPrMH6Zen4i17uXgPkIsx9Ip8wSseFemeuErwUi0yWvAfclUXd9F9W_aNxRY4EcmewRKwKf4VXoi_1zmJBtCYYpsgp6zXefRvk-1XAACrm1ONdEK71f2lIq-1wBCwluzmhaoDOKp4UzT2a6rfLBmvPwHnmbLeYqz6z7kzfwrRKtEgpHr-4smxvE9NqsK9nZAJjZH7ikobPSTB3-QuBA4gz7ftzQYJBV8LPKoyp3qtN2Q_XXAZEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCmlh8ZWSHYcYwK8zNk2-YXDg0UP0LC-AHwvaq456dixxfbujgZfB5-sLR_MJ9AHbXl0-Dlh_BoszIYaGtFx6H3Mk53kStcpl99etwugCjnvrR6bELgu8t-KMiBd6OIk5sEHWnCvYKwqO6vA_OFPcp1Juw-5jXuEl2-UZPcEYBomH7kmNnayfr0VJNmrGRHG511bRCCYIW5AqhzcSaLqY3k66DUMmTMUdQch2W1aqgW2i3x-fQR4eSfiIk9GvLEZHHm7ZP9Lh2KbZj15-gTpz60fvKEFhZ7p1j_566RkfZnmTS9W7tSriptSkFGmONbi2r1B9u4uDwHObc55Uq_J_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تضرم النار في مقام الشيخ ناصر الحكيم التابع للطائفة العلوية في قرية العريضة بريف حمص الغربي.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80295" target="_blank">📅 15:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مصدر في هيئة النزاهة العراقية: النواب الثلاثة المعتقلين في أربيل ضُبطت بحوزتهم أثناء عملية الاعتقال مبالغ مالية تُقدر بـ10 ملايين دينار، إضافة إلى 15 قطعة سلاح متنوعة من بينها مسدسات وبنادق من نوع M4.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80294" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مصدر في هيئة النزاهة العراقية: النواب الثلاثة المعتقلين في أربيل ضُبطت بحوزتهم أثناء عملية الاعتقال مبالغ مالية تُقدر بـ10 ملايين دينار، إضافة إلى 15 قطعة سلاح متنوعة من بينها مسدسات وبنادق من نوع M4.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80293" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏴‍☠️
‏
إيدو نوردن، رئيس ديوان نتن ياهو:
‏ينبغي أن تكون هناك دولة واحدة بين نهر الأردن والبحر الأبيض المتوسط.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80292" target="_blank">📅 15:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnfLVRxv21D3mH2CX_4HzDIWZqiJ6Um2GHojORqCJ0W4bidVNMEEzlINeUpqjDFO-gM9yq8_dEPfEFT9soD9WRPbApMC_pphL4njaC4OTpXQgnnQzr9Ah3FkPwf_x1zacLU9gd_djZYe8kMYvUUQT2mQC7EfhTrn93hJ7y9Zo2aUJDFmAevBr6MV_lpHVv_Y41xnErhIn624TU5M2i4-Golk6tWm3MR_Iz43zPukfPoi5mQTm4F9XVQI00tPRzrstAHXJhUZ4LnP3FeH4EX9-wjmgeNJPnWHvzE7jhhIh6PC_WaLgUhUqX_qwW_eOUMYL0gpvZR59S7A4vvUBn7HTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
إيران طلبت عقد اجتماع. سيعقد غداً في الدوحة!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80291" target="_blank">📅 15:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
اطلق حزب الله صاروخ أرض-جو باتجاه طائرة مقاتلة تابعة لسلاح الجو</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80290" target="_blank">📅 14:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">المجلس الوزاري للاقتصاد في العراق يقرر تشكيل لجنة مشتركة برئاسة هيئة المنافذ الحدودية الاتحادية وممثلين عن الجهات المختصة في الحكومة الاتحادية والإقليم لغرض إجراء مسح كامل للشريط الحدودي وزيارة المعابر والمنافذ غير الرسمية في الإقليم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80289" target="_blank">📅 14:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d54f652a6.mp4?token=YMzoMK_VzgNKlX36krSkp-LpG03ZN5yd65Dhwco2tHXcRFPhlIrssiNsJaffLqhLT_MNMGel7VpDorIOHyr-mnai9tMzfMXXwVv9dRGZg3T0rc4av5LyNth4Z_FrZHNihAzgZ9iC01cR1ngJnl-MH0VgHbcp47eOCC8D6hqYSpSSkRv1MY8zNOu7bASboF-LMgpOMZi-gROmQzt0p1puAuvJQyjpeapvS9nsPR_BNmzdw5wbjLajylquzJnJbjuO7s0CkSP1CuvFsN8IUdL2UQhDpneZyy2BbxOGI0_a2KNIVoyRKpXXt08nFmJKM4h5GJ_D-cwPCYjTZJKnBOPwRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d54f652a6.mp4?token=YMzoMK_VzgNKlX36krSkp-LpG03ZN5yd65Dhwco2tHXcRFPhlIrssiNsJaffLqhLT_MNMGel7VpDorIOHyr-mnai9tMzfMXXwVv9dRGZg3T0rc4av5LyNth4Z_FrZHNihAzgZ9iC01cR1ngJnl-MH0VgHbcp47eOCC8D6hqYSpSSkRv1MY8zNOu7bASboF-LMgpOMZi-gROmQzt0p1puAuvJQyjpeapvS9nsPR_BNmzdw5wbjLajylquzJnJbjuO7s0CkSP1CuvFsN8IUdL2UQhDpneZyy2BbxOGI0_a2KNIVoyRKpXXt08nFmJKM4h5GJ_D-cwPCYjTZJKnBOPwRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من عزاء بني اسد والقبائل العراقية في كربلاء المقدسة في ذكرى دفن الاجساد الطاهرة بعد ثلاث ايام من واقعة الطف الاليمة</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80288" target="_blank">📅 14:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🌟
‏
ترامب:
أعلى نسب تأييد في استطلاعات الرأي على الإطلاق. حتى أعلى من يوم الانتخابات، 5 نوفمبر. هذا على الرغم من حقيقة أن إيران لن تمتلك سلاحاً نووياً!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80287" target="_blank">📅 14:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080fa0dd58.mp4?token=uB9R__JTx6TRPz5fGKuTcTpmVu9GrwDNulWNKeCyUBFWQzwasz4dts6LzZqLuFzGc6wD6mptu1WokGQ4TeSHCCdtcgUbyUmJlvb_eSAwr25Ms0dd67oIgoWR3YWrcO25ipENy6eCmiLzsySL4T340GaNmMaC1LEMuwpGnLQUYm3EWhPselRaqSsY19x6IhU7G-sqcXVeJeqflP4I6jIlQ-bYVt-XXFFbd2UxZKVg2-HYu3FU5NLKW9rnsFHvraurhmj_-EyBqAQ4XnKwQiHZ99Ni2ruY7k89tZiYoBk4PjPa2lqj__rKrn6sLH4m30oZitqRzWYSDkoW5LgUta72Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080fa0dd58.mp4?token=uB9R__JTx6TRPz5fGKuTcTpmVu9GrwDNulWNKeCyUBFWQzwasz4dts6LzZqLuFzGc6wD6mptu1WokGQ4TeSHCCdtcgUbyUmJlvb_eSAwr25Ms0dd67oIgoWR3YWrcO25ipENy6eCmiLzsySL4T340GaNmMaC1LEMuwpGnLQUYm3EWhPselRaqSsY19x6IhU7G-sqcXVeJeqflP4I6jIlQ-bYVt-XXFFbd2UxZKVg2-HYu3FU5NLKW9rnsFHvraurhmj_-EyBqAQ4XnKwQiHZ99Ni2ruY7k89tZiYoBk4PjPa2lqj__rKrn6sLH4m30oZitqRzWYSDkoW5LgUta72Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من مطار كركوك الدولي شمالي العراق وانباء عن حريق كبير في محيطه</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80286" target="_blank">📅 14:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: الاعترافات التي التي أدلى بها المتهمون تقود لشبكات أخرى على مستوى الأسماء والأموال، سردية مكافحة الفساد لا تشبه سابقاتها وحماية المال العام مسؤولية لا تتأثر بالأشخاص أو الظروف</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80285" target="_blank">📅 13:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: سيتم التعامل وفق القانون مع من يتخلف عن تسليم سلاحه قبل نهاية سبتمبر</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80284" target="_blank">📅 13:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: رئيس الوزراء وجه وزارة المالية بإنشاء حساب لإيداع الأموال المستردة من المتورطين بالكسب غير المشروع</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80283" target="_blank">📅 13:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80282">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: إلقاء القبض على 21 متهما متورطا في ملفات الفساد في عملية صولة الفجر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80282" target="_blank">📅 13:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80281">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية: إلقاء القبض على 21 متهما متورطا في ملفات الفساد في عملية صولة الفجر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/80281" target="_blank">📅 13:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
هيئة النزاهة العراقية: تمكنا من حجز كميات كبيرة من الأموال في الخارج</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/80280" target="_blank">📅 12:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80279">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a162cc92.mp4?token=nIUI8JdZubsBmvwZ6mDFrXIT-UV1LnIS7AuPxwu4DVN__Yh5E3zv18xuQJGkDZnEmFOh3rrBplnilZgycs9P2miqI8b9_r5JdMD0YJbVhdkEo_1tLp3YPvzuYM6UheTGporKz3EiMu_icM3gsE26KFiX6G0AR4ONRqc7HEtoZVI05q0ISJvCoC7hA5mACTbTJpkC6zqruUSkvJhpyK3lATotaJhzzBiVfOIq5Ch5LfVZgXzyrQTJPDdNRLQUjVHx1f7ZBql7INEQV6pqumY6Thw8rqs80NvyeadbDnwZrJCCwGkQrm-kaaUTSs1J_L5AEuXTmP3aSxnDYFnQgPMlsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a162cc92.mp4?token=nIUI8JdZubsBmvwZ6mDFrXIT-UV1LnIS7AuPxwu4DVN__Yh5E3zv18xuQJGkDZnEmFOh3rrBplnilZgycs9P2miqI8b9_r5JdMD0YJbVhdkEo_1tLp3YPvzuYM6UheTGporKz3EiMu_icM3gsE26KFiX6G0AR4ONRqc7HEtoZVI05q0ISJvCoC7hA5mACTbTJpkC6zqruUSkvJhpyK3lATotaJhzzBiVfOIq5Ch5LfVZgXzyrQTJPDdNRLQUjVHx1f7ZBql7INEQV6pqumY6Thw8rqs80NvyeadbDnwZrJCCwGkQrm-kaaUTSs1J_L5AEuXTmP3aSxnDYFnQgPMlsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوة أمنية من بغداد تقتحم بلدية بعقوبة بمحافظة ديالى وأنباء عن اعتقال موظفين ومهندسين من داخل البلدية.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80279" target="_blank">📅 12:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f80ffc4.mp4?token=D1uzfGcdI1JQ_-nX9uHsDKJzqwgaWNR6PJo-38pn0VsKx9CaFfjXjZIvKq8XAyiLb2LH_HgMUeuIGcApwlqSd07hUvAAk76CWPDiBs1I7n2CfgnnRRgU3fov5rKmxcaiC-370YNi7pQ3C8t8IDImitUbR6ces1B5C8qVuDCZpriDm22bV9bdSEij1OTnmpUaNjI1sePpehNRNdcErQC8T3xE-N8xn5QNAEeb7kh52oEGSy0wmZHxS4g6CVJB5aHkcVz3blN91fm-pibMPWvy1KJSLckBZObk0M4tukZsIvbPP3Z33LjWqLFQs-b4k8gup-giPMPPSAWfoQC6ihnmow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f80ffc4.mp4?token=D1uzfGcdI1JQ_-nX9uHsDKJzqwgaWNR6PJo-38pn0VsKx9CaFfjXjZIvKq8XAyiLb2LH_HgMUeuIGcApwlqSd07hUvAAk76CWPDiBs1I7n2CfgnnRRgU3fov5rKmxcaiC-370YNi7pQ3C8t8IDImitUbR6ces1B5C8qVuDCZpriDm22bV9bdSEij1OTnmpUaNjI1sePpehNRNdcErQC8T3xE-N8xn5QNAEeb7kh52oEGSy0wmZHxS4g6CVJB5aHkcVz3blN91fm-pibMPWvy1KJSLckBZObk0M4tukZsIvbPP3Z33LjWqLFQs-b4k8gup-giPMPPSAWfoQC6ihnmow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق ضخم جداً يلتهم معارض النهضة وسط العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/80277" target="_blank">📅 11:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBcKulIZiamFtm6dPINfqumnjcFtqNV0fEubFSfuFzfmigW87KCezBQHIUP9ZwILTJZ3JkVqM_JOPRzEon_gP9q8TjqUAw4niqko7IWjUkt9xquOEzGBlVP9MSo0Qxc_buCCYktW8cuBhFTZOXhToBDiw1sdP9BL1z3mdXsHQmjOYWSb1dXPRlPh0Q06IUjnmY_ljAYFKdukHZBqYtNDl9nHXlzw1IMbUs1rObqIypRgXFhPKZ0gQsOUcvpNWClHhpXwveWz9LQrt0a8Vrc7s3GbZGoEMvGxFxLtq7arw6EEyT5Ytf7qP6vWJvRwukrWMjwBqWldmNrJKIHWVE6lLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر يوجه آئمة صلاة الجمعة لوقفة سليمة يوم الجمعة ترفع فيها رايات الإمام الحسين وأعلام العراق دعماً لحملة الاعتقالات ضد الفاسدين في العراق.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/80276" target="_blank">📅 11:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3jlUm5M21lCDQhW-BMcQ5USWzHsuMEiib3srUkuPjsAc7p5iCjx0D7txjrmO34T4G72tmRKwe7Uq5RgqJyx1EfIXeDlZ4IKGRaGsD-BbbnVkbkLQ3icd1LfVz6gK_ejugl3IKoDekadw5EydJCTeilSNeyETFbY8JJ9lEWR8vnbUmno_sNRAG71iHHmrqkK6AUbPyeHmNGRWXs1XL_NJM_deHauzWI7CIScyh8jbqQsoOtYqMy8URa-JqMnHeU8T-vQGrxBKb2sXV1_oIofFqZBVriXtHlPq5M71tZoEretNcxswWIBfnRzv6VIvqi5_EmBhJGoXuBTbtxaJZr4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الجيش اللبناني يغلق طريق النبطية الفوقا ويمنع دخول الأهالي إليها بعد تكرار الاعتداءات الإسرائيلية حيث تعد هذه الخطوة أول خطة استراتيجية تم تطبيقها من قبل الحكومة اللبنانية لتحرير الجنوب.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/80275" target="_blank">📅 10:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c76cd22f.mp4?token=U6iPbFEAzVts0h62_OcwrIn0c7KXnmD6XppdIU9eDizaRr-ptghYRlg_F2e9cnxpQiyEPhHk1FUE8UA912ALE9tMOCrL6nCA8KaBjYXr1dUt9LlC8UWiZDKQVSnZL7pKGfuz2fxQVoqChUtWcK2NghwFqja2TJJ7HU6us5Dt9pgZ21vsZ0Z7UFCfPm9kpbeEexW-xEt-4gfWSafyVl8bJFVGudfpVwRcWpLYSNa569bSgXhpjMzwYMFlsWl72MwhPq0WI4aU8ZkN-g5m79o2jCctVcPMCxC2kGSdFXkJq0GkO9l6AyBheR9HSRDViinUMfD5mpO43HAvXd4W0TX_lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c76cd22f.mp4?token=U6iPbFEAzVts0h62_OcwrIn0c7KXnmD6XppdIU9eDizaRr-ptghYRlg_F2e9cnxpQiyEPhHk1FUE8UA912ALE9tMOCrL6nCA8KaBjYXr1dUt9LlC8UWiZDKQVSnZL7pKGfuz2fxQVoqChUtWcK2NghwFqja2TJJ7HU6us5Dt9pgZ21vsZ0Z7UFCfPm9kpbeEexW-xEt-4gfWSafyVl8bJFVGudfpVwRcWpLYSNa569bSgXhpjMzwYMFlsWl72MwhPq0WI4aU8ZkN-g5m79o2jCctVcPMCxC2kGSdFXkJq0GkO9l6AyBheR9HSRDViinUMfD5mpO43HAvXd4W0TX_lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوات أمنية تصل إلى محافظة كركوك شمال العراق لليوم الثاني على التوالي لتنفيذ عمليات الاعتقال بحق مسؤولين متهمين بقضايا الفساد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/80274" target="_blank">📅 10:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrgYlpEDF4WJVJY0BtgWq6hcLqonkBa4U1QpTghQpjuuYLbBCpXmMJqwcoiW8eKBLk681zIJWkNsrqGhly7LKCKhGP2VMqY5E6j6abS7plvaF5F3OeEbYLR4UMTDzNUqeQElJ7IHrFnymIGFAAHaZo69NMop6V-GlaFzK9Tosiou-6NuOF2UcowK2OrNV18p61RAofPbGdx3w8hi0T2as9s10x6OdhpEySGZ78bU60Tg8NZwfp-81oggiPafakzeC2QPacnh_IQhKS5QxJ-93nwY-FYlsEDxpEAE2tXbb-XR3iIHxXpgzNiBEfHh_Jdd-Uh9RSaPoqlc0_CN5vnnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القوات الامنية تضبط شخص بحوزته مليارين في سيطرة قضاء قلعة صالح بمحافظة ميسان جنوبي العراق.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/80273" target="_blank">📅 01:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
مجلس الوزراء يقر مبادرة المليون قطعة أرض سكنية كمشروع وطني لتوزيع الأراضي المخدومة على المستحقين في جميع المحافظات، باستثناء إقليم كردستان.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/80271" target="_blank">📅 01:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔻
رئاسة الوزراء العراقية: ما جرى من صولةٍ ضد الفساد هي مرحلة أولى، والوضع بات من غير الممكن السكوت عنه.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/80270" target="_blank">📅 01:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f416360a.mp4?token=rW1zQZ988q7vQ6DkAqVp4GGGLD5qYsK_oZn1iHzxzl2ijeAgoGuq8l0t3GvzIl-OaJwdiWQ2EDDD1CC1XFz_ZGZipNAkKk2EPQI8-Kzx8pP_ezNF8dmnpiwkClJel4n2d4OvgJ1PphHmU_ISJ7X3OoGa8gHgnmgutw_fLzELEyAGBcuKmol6UDF3EtKhmYgO68DiAGdYwlhRLOKDEeEuVU5KhlXea2fI1jqzGGDiaA-LL67SBHsMAQnVXR2w1hO-ituOYwuoc1ZsHU7LClPXIdyym3iM8TJxvPutQai-YCd1ZhZkDNMmuGh9Ymb-_IKx4cph92pmGQcj7X1qhGacgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f416360a.mp4?token=rW1zQZ988q7vQ6DkAqVp4GGGLD5qYsK_oZn1iHzxzl2ijeAgoGuq8l0t3GvzIl-OaJwdiWQ2EDDD1CC1XFz_ZGZipNAkKk2EPQI8-Kzx8pP_ezNF8dmnpiwkClJel4n2d4OvgJ1PphHmU_ISJ7X3OoGa8gHgnmgutw_fLzELEyAGBcuKmol6UDF3EtKhmYgO68DiAGdYwlhRLOKDEeEuVU5KhlXea2fI1jqzGGDiaA-LL67SBHsMAQnVXR2w1hO-ituOYwuoc1ZsHU7LClPXIdyym3iM8TJxvPutQai-YCd1ZhZkDNMmuGh9Ymb-_IKx4cph92pmGQcj7X1qhGacgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انتشار واسع للقوات الامنية في محافظة واسط العراقية.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/80269" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
رئاسة الوزراء العراقية:
ما جرى من صولةٍ ضد الفساد هي مرحلة أولى، والوضع بات من غير الممكن السكوت عنه.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/80268" target="_blank">📅 01:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
استمرار القصف العشوائي الصهيوني على قرية عابدين بمحافظة درعا السورية وسط نزوح معظم أهالي القرية.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/80267" target="_blank">📅 01:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
انباء متداولة عن انعقاد مؤتمر لهيئة النزاهة الاتحادية بعد قليل.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/80266" target="_blank">📅 00:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBwODkDxVSHbgD27XXH0zKmAxFh6gNkkfi-OjvlumtH0KgOdW3g3iAJbYUxfyTUGz5FfoYFqUKV0SQjft3MHXCy9LdXw8g13gfw4FKQJMuAcVSbyt68DkwfdYh8x9h7HgYfQ_xemTJVVK7Isw7Llcy_jz9skyUN_FcdLO-r3LwEKcOGe9h4x2MhikwlsdjmxtUeRxYnJ8cyYFgHsyeC2rmT6KtWERu89u3NfolGYqoOWk7kd75l7cZNzBJKFzMmA-SWx2fDFDoitl3wWa169DjVcCs9VBMK096OUb-A2Jv9dI91ZP7Jzh76bi_ThK_xDxTAgV0sFYfTs3mlwKo8N-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
انباء متداولة عن انعقاد مؤتمر لهيئة النزاهة الاتحادية بعد قليل.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/80265" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
