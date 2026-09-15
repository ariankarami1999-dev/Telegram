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
<img src="https://cdn4.telesco.pe/file/lng4DGvryZJtooZpgi_BFwsGaqijfKz6qbrkFT6ZKvGHZOusPMmbqikRvgqHL68Wq_u7u2gTFH6CFNu6JRSzKVmkIYrzcqsCrc9yRoc-mLrQZbJ72vfPJHDjlZnXENP8x1MIH60R6OIXpqf9_Z9SVRj5RHO8EOVEUglZal8rrF1NEr4sOWYWzJLOX4ak6xVSb-v2hsm57_LOyqw2N8H_JhAfJyzwFbNitZ8zFH9RKIp9IOUUHhQkS9N2oBreiMtqerkQza4-_Z2TgSbA71BYqvDNYgMfViliQkwQAFeonWwzC8pAw0aEE6mnEYW9AgVaWqCxo-zDAF0QH9pVlPeoLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 09:48:57</div>
<hr>

<div class="tg-post" id="msg-90568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اعتداء سعودي على مديرية صعدة في اليمن العزيز</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/90568" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccu2pjwVwM9BFWoktBpMM2zLfUHUY7yNU_sWCEkFHcFRNC6PROnlgQcle_cmvhQGOVdVcB9uVX-0Z39yWpPxBgEw6TJ9QF1d8rCl26kuZj7I-_G32EdYV6qx80oJm9oW4v6kiL3SLfcRP2wmNRPPDVkNdbAQu2f1bQbVDngyXAkmkVs4ePBm-x7a1dQ8y11sINWF5BBZ11ZszArThpkvMQncPxeR59468F_pSNr-UeXZyTHVfK1K8Q36zBslUKJY9zf_x5m8Nm_kCaokYUOlAw6iEmqaeE2P0YLN9gP6HgXB_a_Nr52GZ55KLtE6NyTy3SEzlTYUbg7mO2r2ojBJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
البنتاغون عن عمليتها ضد ايران:  22‏ مليار دولار للذخائر المستهلكة، 7.4 مليار دولار من الالتزامات التراكمية، و3.7 مليار دولار في خسائر المعدات، لكنها لا تشمل إصلاحات البنية التحتية.  ‏أكثر من 50 طائرة تضررت أو دمرت حتى الآن.</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/naya_foriraq/90567" target="_blank">📅 09:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9F4iKVQ2Di87pPvKhHBa6I7YbdaQipT5jeWh10WpeotGiVzTxS1XnT1YPxhLrdtORKyOkrSsjWk43P1FzgOT63boH19xfSu98oqQl44uEcia3EohJtM52p3XQljrVVJ1rPeC5_1ClT6cVWINl6uzfxGCp48lTLHHtHTsqTDFif8lGf6g-VelvZb6KC4if31L0YdyGP-tWCV1AKqtg9ERLSPfDgCNGXmTd3t5O9BoZH7Kb-smQ713N57K_PafUQvOg5mdr4mipJDBAUos9EGTzbcgEJkHWWuxoWVa3IZKenSaNEL7S7JvbUoxkZSObU2Tjvh5oKjCbt8X9wXaRWFsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
الان توقف العمل بمطار أبها جنوب السعودية دون معرفة الأسباب والتفاصيل</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/naya_foriraq/90566" target="_blank">📅 09:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-N7E6wzs5K5WqSGK8d5h9-WXuNtxy9rUpmdn-vQ6HIbwkT-4PfXlpON7XuxTicIuHd8d1VDAWlu3BOaoa4uzAPvJvJWxstvXfZC85eZFAriZcTCyFXPp9dtTuJV0HrifPqB4S6Zva6OuXYawTp1m7oOFnJJLSvnTNbbUCcH8KPFVX0d3o4Dkt2LFmTcjEyAdWVFuKL14IyHmFb0LLoh8k64xO1fcmEf93boEuxgnMqqa7Xr1BFzEM18QfK2UWzMe9MbMsX2qCmdgwJDX6soemD986HGOlqQRqSlT2edo43efyY9weP_sN0CHGO0n3GHN82aOK0K0t8K-56OQYbC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
الان توقف العمل بمطار أبها جنوب السعودية دون معرفة الأسباب والتفاصيل</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/naya_foriraq/90565" target="_blank">📅 09:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات عنيفة تهز العاصمة الاوكرانية كييف</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/naya_foriraq/90564" target="_blank">📅 08:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله أكبر
🔻
الدفاعات الجوية التابعة للحرس الثوري تتمكن من رصد وإسقاط مسيرة أمريكية من طراز MQ1 في الأجواء الغربية لمضيق هرمز.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90563" target="_blank">📅 06:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJlmv6NKa_NuDPVts--ISD3PoOV1k4DOV8SOu7omdIj-GHclfsmMIx2roifFt-Ub4BpKyl4bT_NPddrUwvMZ7jU4cA3Btmf8ntdMG7cz_-ukfCRFM9baZVE_MCmQrPaBjqCnKF8E2wF3S3G_sl2TV54HlMmc5Fyj-9NWA8IYCzgzRPoZz5UG1tY1JmAPstt3U_nbTHR_oKyIhu4sVLwu9pJ5l0AYyqQLMA0kHMnl3ouEQEqVBqJw3EX0OCad_qQfGniB9_eknG07a69lWx9iAHN8JGOdIsaoNNH3lcSWZkqxqAgxJusDKNhg7Bno95VKSz-DF4_ucmTdeqFj9_hqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/90562" target="_blank">📅 06:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
وول ستريت جورنال:
تحذر شركات النفط الأمريكية من أن أزمة الوقود العالمية التي توقعتها نتيجة للإغلاق المطول لمضيق هرمز قد حانت الآن، حيث تتناقص المخزونات التجارية وتقترب الاحتياطيات الاستراتيجية من حدودها القصوى.
قال مايك ورث، الرئيس التنفيذي لشركة شيفرون، إن العديد من العوامل التي حمت الأسواق في البداية من حرب إيران قد استنفدت الآن.
تفاقمت الأوضاع بعد هجمات الطائرات بدون طيار من العراق، والتي أدت إلى تعطيل خط الأنابيب السعودي الذي يربط الشرق بالغرب إلى حد كبير، مما أدى إلى إزالة ما يقدر بـ 2.5 مليون برميل يوميًا من سوق يعاني بالفعل من القيود.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90561" target="_blank">📅 06:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
رويترز:
تراجع حركة المرور بمضيق هرمز عقب تصاعد الهجمات في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90560" target="_blank">📅 06:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90559" target="_blank">📅 05:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/90558" target="_blank">📅 05:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇸🇦
🇺🇸
🇾🇪
منظومة الباتريوت الأمريكية تفشل في صد الهجوم الصاروخي اليمني وإصابات مباشرة بالجملة في المدن السعودية.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90557" target="_blank">📅 05:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ1oheVibrluTYgxccbw_zGcOU_UlZW00axqbnO0dqX1Kdu0Two3WNWSmvPABCn0NHePE_XfBYjZ1notKsrnA32pJGSmsOJB6wNFy1iOu7rIQiJY-0D2nWWH4qAgwJvZU5oI3kodmFT3fDJ9bJdyWeZWzbqe3MRa9LWL4CZ_QDZunBsaVmzaKVb78Aumn-bCUNOXRsKFiGvBqKMgims5SLyRO4-YU1I77itwcQRp6HdbiK5ZjllAOthI2DPHMgJD-dMoKEhB67RsLb5gW4QiZawZO-QMKBHu7oHNox25ffv-661D13hdv5dIOY3PzpztqmvkimbpH6wqIUOgIxLD2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
الطيران المدني يترك أجواء جدة عقب الهجوم الصاروخي اليمني.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/90556" target="_blank">📅 05:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇦
🇺🇸
🇾🇪
منظومة الباتريوت الأمريكية تفشل في صد الهجوم الصاروخي اليمني وإصابات مباشرة بالجملة في المدن السعودية.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90555" target="_blank">📅 05:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات في الجدة السعودية جراء هجوم صاروخي يمني واسع.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90554" target="_blank">📅 05:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اصابة مباشرة في منشآت نفطية بجازان جنوبي السعودية.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90553" target="_blank">📅 05:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جازان تلتحق بالمدن التي يتم دكها في هذه الأثناء من قبل القوة الصاروخية اليمنية</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/90552" target="_blank">📅 05:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مدينة أبها تحت رحمة الصواريخ اليمنية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90551" target="_blank">📅 05:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90550" target="_blank">📅 05:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجارات في الجدة السعودية جراء هجوم صاروخي يمني واسع.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/90549" target="_blank">📅 05:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90548" target="_blank">📅 05:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هجوم صاروخي يمني يستهدف محافظتي ينبع والطائف في السعودية.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90547" target="_blank">📅 05:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
🇸🇦
سماع دوي إنفجار في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90546" target="_blank">📅 05:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
مجلس النواب الأمريكي:
تأجيل التصويت على قرار لسحب القوات الأمريكية من الأعمال القتالية مع إيران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/90545" target="_blank">📅 04:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
المحكمة العليا الأمريكية ترفض طلب ترامب بتقييد التصويت عبر البريد قبل انتخابات التجديد النصفي في نوفمبر.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/90544" target="_blank">📅 03:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇦
السعودية:
تعرضنا لقصف يمني بالصواريخ الباليستية والطائرات المسيرة في أبها وخميس مشيط والطائف؛ إصابة 13 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90543" target="_blank">📅 02:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYWhYliFRBAe1yj8dMGiPYnpkHBmuGaQgYPrZIWVypYqLZ0fywzOF-SbHdVKs4GT5G6jFb8Bp2oYkompPMP7zDzF0Up-3e17Pr8JYJM1glmgTpN83ro7_9AptABCC9uBm4DtH3l8gHvxBDzFKbaT2p7_UIxMI8oOpOW632TMg-v0jKNVf6qiwB1zl1x0HOjrDxFqSdACza5vL0JnVucvzSJ31wIr9rsgAzh6fsAt461eYM0QJ8FX54UYZHD0OvousUNAQjbwwaWcs_zj_-VgSsRL2RYO0CWUsSeQ7f4qnnxttuPvZANEwhWob6xjnf37NmlW8kxXp21Yyo_1SUNwvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشقة صواريخ يمنية تدك خميس مشيط وأبها جنوبي السعودية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90542" target="_blank">📅 01:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90541" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90540" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90539" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2GVxLTsQJibN4cQA9ETIeUg0jJ3pPKP9Y277_ZYJ1hlNx6E67iTllNfRy8DnuXHdiSrkfWUN-BbKljjl7HKhj7_oEppamSfqna6dEwhZuL8eT8k6a8MQXQszga4H20Am8-rOedPuEknNHrPrrolOrDm9Hu68aiDSgFkjz0ySpTBfati0mZYrIwLJOYlo-C_9LxXi8m_OyNFMOvyuWZqou-crLLmmGvcjD1KGqt8f1ms5DnHCgGemsi8W5S4QGhhaK0IGnVywEiG7rS3bDjfYEw10d8kpL_0Ds34g8H_nPzhSdjjQ7da2YplKYqb9BP_WBPtXuNLQHoAGsCJdZIVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
‏رشح ترامب الضابط الذي شارك بعدة عمليات ارهابية في العراق ويسلي هانت لمنصب سفير الولايات المتحدة لدى السعودية، وهو المنصب الذي سيشغل شاغراً منذ أن بدأ ترامب ولايته الثانية في يناير 2025.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90538" target="_blank">📅 01:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
‏تم إقلاع طائرات حربية تابعة لحلف الناتو في ليتوانيا بسبب احتمال وجود طائرة مسيرة بالقرب من فيلنيوس.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90537" target="_blank">📅 01:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
🇮🇷
البنتاغون عن عمليتها ضد ايران:
22‏ مليار دولار للذخائر المستهلكة، 7.4 مليار دولار من الالتزامات التراكمية، و3.7 مليار دولار في خسائر المعدات، لكنها لا تشمل إصلاحات البنية التحتية.
‏أكثر من 50 طائرة تضررت أو دمرت حتى الآن.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90536" target="_blank">📅 01:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90535" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇾🇪
🇸🇦
بسبب الضربات الموجعة للجيش اليمني:‏
تحويل الدراسة اليوم الثلاثاء إلى التعليم (عن بُعد) عبر منصة مدرستي، في كلٍ من: أبها، وخميس مشيط، وأحد رفيدة، ومحايل عسير، ورجال ألمع، وسراة عبيدة، والحرجة، والفرشة، والربوعة، وظهران الجنوب.
‏‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90534" target="_blank">📅 01:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
‏تم إقلاع طائرات حربية تابعة لحلف الناتو في ليتوانيا بسبب احتمال وجود طائرة مسيرة بالقرب من فيلنيوس.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90533" target="_blank">📅 00:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNGj2QZ68lyb8ZF4qKfbm3kyovJOVeT-Yvgu7I-MmRh9cdHFIbz63ct86CIgJZEoWaR38F9FSIN_Pl1Pq9SymQUOJBo61gDzDKbw8ZPmt_Qi-WdjWZ6HgnSLmEbGoyzhfUtKFP3blzqbRNL-leU94fhYo8xA6o1EdnQuJ8chQNUAoAvqm52NIHyfMA0ULn9pbqLrr8mhQEFlALDy2gSaaO6gM3k8F0Abtocv_RXy8A2euT-7Gv_CTUMzL2ocke1oF74YLqxGHOQUeMWu8BZNdaXCT0UZ0A8AohgXzgmTOy5-fc5ci9jobkGh135c7vk00oTlzIwaDhVPMEruMuhkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رضائي
: لا تنخدعوا بتصريحات الرئيس الأمريكي المتضاربة، من "لا مفاوضات" إلى "نحن مستعدون للحوار". لقد تغيرت المخاطر المتعلقة بالنفط والمضيق. ولن يوقف احتواء الأضرار ما هو قادم.
لا محادثات حتى يتم تلبية شروط إيران. انتهى!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90532" target="_blank">📅 00:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppSmj_a_T2wEF_vjpGLyz9uzkU72LOFad67bGaQ20SD0wI_zzTy_qBcsR9YTmXPsR217hDXnly3w7afQX68jEKsejRa0goFhxw2N9zBRlAIvjdpTQGGRwDSt2Hy7cN8mfZpIINh53d5h10t77QTnNyW_wCp79hJVLuL_hmqfD_KPT296Uy8JkAmh9keHDU6Xe8npp8UhugTLkfLKoLeOnEq-JKRR1eu_x9MM18w34ZAfzx-fPH9Ox6Fhjb2d1UKPCUXFbH1BcOC-jkUPuKe__EOhY6PUeRW5tUFSsWRaBQa21CqAwnLIzdaD6mqu0tlmQhb7DiY8ZHpv92gFy0NLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب
:
"إنّ من يقولون إنّ الذكاء الاصطناعي سيدمّر العالم، وإنّ مراكز البيانات تضرّ بأحيائكم، هم أنفسهم من قالوا، منذ وقتٍ قصير، إنّ العالم سينقرض بسبب "تغيّر المناخ". لم تنجح هذه الخدعة معهم قط، والآن ينتقلون إلى خدعة أخرى. هؤلاء ثوريون، لكنّهم ثوريون من أجل قضية شريرة وخبيثة. ستكتشفون قريبًا أنّهم يعملون لصالح أناس لا يضعون مصلحة الولايات المتحدة في اعتبارهم!: «أنا كاشف الخدع، وأنا الآن أفضح خدعة أخرى - أن الذكاء الاصطناعي سيستولي على العالم ويدمره، وأن الروبوتات ستغزو مدننا وتقضي علينا جميعًا! هذا أغرب حتى من خدعة روسيا، روسيا، روسيا، أو خدعة الاحتباس الحراري. شكرًا لاهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90531" target="_blank">📅 00:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇸🇦
‏توقف العمليات الجوية في مطار الملك فهد في الدمام.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90530" target="_blank">📅 00:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90529">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ed277d98.mp4?token=Y0T9LlaxnKMqBhSZ3GV11RFzZH-3YbAsQm7Ndfe1cbRJJeOcbdf4VehIRsGQDJDbySkXrn4ag-R0nNQL-zbnRJyVMwBHVAYlhKPl9QyQmfRoowzmKdjF6Tm0QmXvQfchQFNfXnb1Vm7eulC8MvuvBjPsLnazCGeL_PQXbvu58wRnuVgCfOZp9htjt3ZlWmLPQaxIEumqifSlPecSaQlvSBttr3fPJKY23KRqwuDazN90V7qn_oQ-whCBEh6LHKvo0G2RT7Kq4QON9m_RfEnAAiQqgUCz34MCd0YE-zVjbPuts5_CC6-vdrBEJ3LJJjIFIIFQOn_G5pRI8X3DrRKJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ed277d98.mp4?token=Y0T9LlaxnKMqBhSZ3GV11RFzZH-3YbAsQm7Ndfe1cbRJJeOcbdf4VehIRsGQDJDbySkXrn4ag-R0nNQL-zbnRJyVMwBHVAYlhKPl9QyQmfRoowzmKdjF6Tm0QmXvQfchQFNfXnb1Vm7eulC8MvuvBjPsLnazCGeL_PQXbvu58wRnuVgCfOZp9htjt3ZlWmLPQaxIEumqifSlPecSaQlvSBttr3fPJKY23KRqwuDazN90V7qn_oQ-whCBEh6LHKvo0G2RT7Kq4QON9m_RfEnAAiQqgUCz34MCd0YE-zVjbPuts5_CC6-vdrBEJ3LJJjIFIIFQOn_G5pRI8X3DrRKJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Kuwait , Bahrain, Jordan now</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90529" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90528">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
🇮🇷
طيران العدو الاميركي يستهدف عدة قوارب صيد في ميناب وارتقاء العديد من الضحايا المدنيين.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90528" target="_blank">📅 23:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90527">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الحرس الثوري يمارس هوايته باستهداف السفن الأمريكية في خليج فارس</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90527" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
مدير العلاقات العامة في مطارات محافظة خراسان الرضوية: رحلة شركة "سبهران" المتجهة من مشهد إلى كرمانشاه عادت إلى مطار مشهد بعد إقلاعها، بسبب عطل فني في محرك الطائرة، ونفذت هبوطًا اضطراريًا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90525" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">المركز الأوروبي المتوسطي لرصد الزلازل:
"زلزال بقوة 5.3 درجة على بعد حوالي 60 كم جنوب غرب كولومبيا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90524" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
🇮🇷
🇮🇶
الأمين العام لاتحاد الإذاعات والتلفزيونات الإسلامية الشيخ علي كريميان يشكر سيد حميد الحسيني على جهوده السابقة و مصادر لنايا تتحدث عن تعين السيد مضر البكاء بديلا عنه ..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90523" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇸🇦
🇾🇪
طائرات العدو السعودي تشن غارات على مديرية ذوباب وارتقاء ضحايا من المدنيين.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90522" target="_blank">📅 23:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت القوات المسلحة اليمنية قبل قليل من التصدي لتشكيلين قتاليين سعوديين في محافظة صعدة نوع "تايفون" و "F15" أقلعت من قاعدتي العدو السعودي الجويتين في خميس مشيط والطائف.
وتم التصدي لها بعدد من صواريخ الدفاع الجوي محلية الصنع وتم إجبارها على التراجع والعودة بفضل الله.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90521" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🇸🇦
🇮🇶
إعلام أمريكي :
خسر العالم ٥ مليون برميل يوميا نتيجة ضربت الفصائل العراقية على انابيب النفط السعودية .</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90520" target="_blank">📅 22:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2qBF15v9BquFtEHXvF_TfkMGr1ItyOVuaOA4uCwkDuxPY-_EMWWtbr3OH7lNLHSuqf-4WT3YoOnAbTYrrn8iX-X4x9jbLYc8mFWDDBK5DvHVDGXUN6qNAVYRWAlsTUgXL8zg2zKMS2vRxIsFU4Mmb3CF1ss6t2pGdfOi8QNF56XMI_m-z8cIqXOuBiSt6damUWraKhSLAg1XcQdkNdL-Vsr7ryElli8kf3hLCJlGQp4Ipm7Q7GBtWbDzQup2DQUmI-3Crp1pSSrFl68GGheqYqJgPqqY3PbsfD6wiIPSaO2D5GQS4cKUPw0YQjE0PrfABgd3iuhxh6NiUm-iyG0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحرس الثوري يمارس هوايته باستهداف السفن الأمريكية في خليج فارس</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90519" target="_blank">📅 22:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90518" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هجوم من أنصار الله على نجران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90517" target="_blank">📅 22:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90516" target="_blank">📅 22:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
🇮🇷
🇷🇺
🇺🇸
فرضت الولايات المتحدة عقوبات متعلقة بإيران على بنك VTB الروسي</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90515" target="_blank">📅 22:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏
🇷🇺
🏴‍☠️
زيلينسكي:
"نحن جميعًا نفهم: العقوبات ضد روسيا مهمة حقًا. هذا بالتأكيد ليس الوقت المناسب لرفع العقوبات، لإنقاذ الأوليغارشيين الروس منها، وبالتأكيد ليس الوقت المناسب لأوروبا لتقديم هدايا لروسيا. أوسمانوف، فريدمان، وشخصيات روسية أخرى مثلهم لم يقوموا بحركاتهم ضد الحرب حتى الآن. هذا ليس الوقت المناسب لأوروبا لتنسى ما يحدث. نحن بحاجة إلى عقوبات جديدة وأقوى – عقوبات لا يمكن لروسيا التكيف معها، بما في ذلك عقوبات مضادة للصواريخ الباليستية ضد كل إنتاج الصواريخ الباليستية الروسية، بالإضافة إلى عقوبات تقيد المالية الروسية. بعبارة أخرى، إجراءات تقيد الحرب. مشروع قانون العقوبات لليندسي غراهام لا يزال مشروع قانون، للأسف، وليس قانونًا. من المهم أن يصبح قانونًا. أشكر الجميع حول العالم الذين يدعمون هذا النهج ويعلمون أن القوة تعمل."</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90514" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQLq7EUqAEjgbYrAAmjeZUzumuC72ea1lHRQUW-ftR4VmsEgl3b-MlE_tMgnLzEDinCxX6tlt-K7Lqq_sBn-Qu17vz9vk4F2SsGgJPyNDMWgPdivnpOkJ_YyGPOFec7PPNSKY9iZbKi8fxzTiqsKz-EaNHb0ECisJa-87RMZddh0pVYNHeKScmkX-QItkGjFLsMUhpne0NVieGYNtEQ4qeZYM1lK2gasH54TOMFTBfEvMPRCBtlN7qgk-yxFSGn2wUQ4-Aq0LMYXFhdmomLTnZngfxBTOnZyDNw3dJJRuVNWgy6cgsw1V2fgLtTB84eji3Z23Kt1WtbQvQn5PtwXVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستشار الرئيس الإماراتي :
التحالف العربي انتهى مفعوله تحالف البحر الأحمر ولد ليموت
حلف مكة فص ملح ذاب عندما أزفت ساعة الحقيقة
مجلس التعاون الخليجي اخفق في تفعيل الدفاع الخليجي المشترك خلال العدوان الإيراني
التحالف مع امريكا لا يعول عليه
محور الاعتدال العربي اختفى
ما العمل؟</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90513" target="_blank">📅 21:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏
🇮🇷
استدعت موريتانيا سفير إيران وقدمت احتجاجاً على ما وصفته بأنه تصرفات لا تتفق مع الأعراف الدبلوماسية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90512" target="_blank">📅 21:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6a2f7e05.mp4?token=BdvlHyL90qdDclhpXc6DVOtAh5fG9-dpmBqwcPXwvvYfC9hDAR6z-eTIncjRoDpRXXm-EZAi8GuKpQ32GcFv0NkPWbZeXv5PqHNvyy9f3h7_D9F0nqnm1SQTXOS6fz-OpIa7T2IItHWQkGX6sN0DdLeW_q0YMH9wFsZX13okyH4vCBVMsrvl-sruF96KI0lSxhnnLS3YyowllfYKzXDUmqyVgfWXPxUF9wFo8fNT-vQDjTkxjdXn9rvjEu5cPLR3JKwJqk3GdaNNEs4Y2KTSLgZ__iU0mH5sIoj0kXOZ0LbyzQDFbXrwdr-c6nmjZYP9tQkdwGUv_ijnT7pfejG86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6a2f7e05.mp4?token=BdvlHyL90qdDclhpXc6DVOtAh5fG9-dpmBqwcPXwvvYfC9hDAR6z-eTIncjRoDpRXXm-EZAi8GuKpQ32GcFv0NkPWbZeXv5PqHNvyy9f3h7_D9F0nqnm1SQTXOS6fz-OpIa7T2IItHWQkGX6sN0DdLeW_q0YMH9wFsZX13okyH4vCBVMsrvl-sruF96KI0lSxhnnLS3YyowllfYKzXDUmqyVgfWXPxUF9wFo8fNT-vQDjTkxjdXn9rvjEu5cPLR3JKwJqk3GdaNNEs4Y2KTSLgZ__iU0mH5sIoj0kXOZ0LbyzQDFbXrwdr-c6nmjZYP9tQkdwGUv_ijnT7pfejG86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇶
🇸🇦
تضررت محطة ضخ أخرى تابعة لخط أنابيب النفط السعودي الشرقي الغربي جراء الهجمات الأخيرة. وسيستغرق إصلاحها واستئناف نقل النفط الخام أسابيع.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90511" target="_blank">📅 21:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇱
انفجار يهز الخليل المحتل بفلسطين المحتلة .</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90510" target="_blank">📅 21:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">للمرة المليون
‏
🇺🇸
🇮🇷
وزير الخزانة الأمريكي بيسينت: أطلقت وزارة الخزانة عملية "المنبوذ الاقتصادي" لقطع جميع خطوط الدعم المالي للنظام الإيراني ومموليه. لهذا السبب أصدرت دعوة جديدة للمبلغين عن مخالفات لتقديم معلومات حول أولئك الذين يسهلون الإرهاب الإيراني.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90509" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afdb4f1f7.mp4?token=VwSlzkro2zT7yov-dLG9IlmlxGiqueHJGM9dWpnqms17Z-ZNil7oatQYE2pD2-rfcUqagn1QxMyMo3-8ZFqOznDjW2v1uofd-JplKjm8tKOph3e07EZ6SVs8QulVl3ByHPX5idvNvzKUF2W4amEsw_kB_JW1SLg4XUPtQpbvnteG2D_AHgMmy5ULXbZolQRSqMDn3tPYKHtxZ2yi3clpczrYx10NLg4WNqQ1Dj3epcAglbNl3e6wbfJyYkfF883fMp4ujaaagpj-AeXmTv2LOOWDzl1vnhhq1XFlhtzFdbJhZH4ro8EpLAFyYM9_fhpxvshz9cZbWZf9T0jkgtUnAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afdb4f1f7.mp4?token=VwSlzkro2zT7yov-dLG9IlmlxGiqueHJGM9dWpnqms17Z-ZNil7oatQYE2pD2-rfcUqagn1QxMyMo3-8ZFqOznDjW2v1uofd-JplKjm8tKOph3e07EZ6SVs8QulVl3ByHPX5idvNvzKUF2W4amEsw_kB_JW1SLg4XUPtQpbvnteG2D_AHgMmy5ULXbZolQRSqMDn3tPYKHtxZ2yi3clpczrYx10NLg4WNqQ1Dj3epcAglbNl3e6wbfJyYkfF883fMp4ujaaagpj-AeXmTv2LOOWDzl1vnhhq1XFlhtzFdbJhZH4ro8EpLAFyYM9_fhpxvshz9cZbWZf9T0jkgtUnAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
تظاهرات في حلب
السورية
بسبب ارتفاع الأسعار والغلاء
؛ المتظاهرين يطالبون باسقط النظام
عوي ولالاك</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90508" target="_blank">📅 21:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owcKCxoJrFiElsBvdIzpP00if_ZCgjc4POxM26dmkRqYD8Jd4EhPs9SX66J19P-S3ALX5hfQ6cmdIjunacz5Iaap-zVXyd0O0nMi05yzTvTBDAOSFedCKQybGabdVqf9U_JfVitgT5dxX8louWQBVNqZYcgqeikZRbjvuNEdqzyrfhCrg0GHuHsHi1bPPwATm2W8ANem3HRT8fk-y5ER8Qs1wNSC9EMK3B-8u5bMwJKdwON74fEVOUuA0Gx_-V_nxBhOUzSJsFEYYZ6PfSJBPBUsfZLTsBdXDvgapvlrnRlEUyj7hELC81wWkIAzjG6vRFMxBKhUxVAMzJ8bmZW8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇺🇸
🇮🇶
طائرة تجسسية أمريكية دخلت اجواء العراق انطلقت من قاعدة خرج في السعودية ..</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90507" target="_blank">📅 20:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
🇸🇦
🇮🇱
🇾🇪
واللا العبري
: وفقاً لمصادر دبلوماسية، جرت اتصالات بين السعودية واسرائيل بوساطة أمريكية؛ وخلال هذه العملية، ساعدت إسرائيل في تحديد المواقع العسكرية للحوثيين وكشف نوايا الجماعة.
خادم الحرمين وكذا</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90506" target="_blank">📅 20:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🇺🇸
ترامب: دول العالم ستعوضنا بمجرد انتهاء هذا الصراع المفتعل</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90505" target="_blank">📅 20:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-hoFhOgCO8nDmZQAvnwbnjbgdxxvFOuo5ARHvB_rslXTBMG3W8ub8Rh_RKs84hUMFyh4MkaF-yrOJMfEM3qc-sD8R60h3XHTGKeVgNKS5OjUdodvR_pSn858LDuO-b0x4xKnyKyalNDgqsHbDFuLwTCJbbujjn5E-4t8_qqE4LfpQVDG2keI8fkdu01WfAq9QeQZQ8JwOUqnYj8bd4kvc70ScUda9EJYxDTZmSmEMiYojQh7AHl-4-WP9UDz5M61-3IyTNGFal9JaRD-dPOJavCbysZ9es2pqJo9L--irNz_Qnzd6p3wvDl2q1cAul_dLE3ICaYGnIdspTuLSZLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب يقول إن الولايات المتحدة تنتج أكثر من الأسلحة مما في أي وقت في التاريخ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90504" target="_blank">📅 19:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slRdgvGSRLRt3TZJL-Lv5-0zaSN5nX88i2MgIF3MXqdyGoKemfQEeDAuu1FbL3G0aOoFQfjoQKU8-Q2xyr1f6snSBYfVWIzEw0XPNx6Ux9gSIdcWXlx8IRLpXwzwCkXFejEYY3lYLceasNKaZO3pRgFM3uaxor97biKYb9R8d0QPYuHqQwh2hiNTk7P1fpNc-l7hv9DYxFMEN5-M8v45qxwUED4flAeBiqzsLpaaiFwSY2DsOYyhQfWv3Zny5r8ccyBFZE53uEj01-NgTp45fY541m9Br8VQaomYNADUoCpBr4JCWcSGQ4TeINnMz9TcUV_gbKO7CThIVV5haWrWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
🇸🇦
نشاط لطيران أمريكي تجسسي في سماء بادية السماوة وعلى الشريط الحدودي بين العراق والسعودية ؛ الطيران انطلق من قاعدة الأزرق استطلع ايضا سواحل الجمهورية الإسلامية في ايران</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90503" target="_blank">📅 19:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
🇮🇷
🇮🇶
الأمين العام لاتحاد الإذاعات والتلفزيونات الإسلامية الشيخ علي كريميان يشكر سيد حميد الحسيني على جهوده السابقة و مصادر لنايا تتحدث عن تعين السيد مضر البكاء بديلا عنه ..</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90502" target="_blank">📅 19:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">3 غارات سعودية على مدينة المخا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90501" target="_blank">📅 19:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب: إيران تريد إبرام صفقة. سأحدد ما إذا كنا سنتعامل مع إيران أم لا، وهذا شيء نحن منفتحون عليه.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90500" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامب: إيران تريد إبرام صفقة. سأحدد ما إذا كنا سنتعامل مع إيران أم لا، وهذا شيء نحن منفتحون عليه.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90499" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عدوان سعودي يستهدف جسر البرح بمديرية مقبنة وأنباء عن ضحايا من المواطنين</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90498" target="_blank">📅 19:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سماع دوي انفجارات في مدينة جابهار جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90497" target="_blank">📅 18:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇱
نتن ياهو:
حزب الله سيتعرض لضربات أشد إذا هاجم مرة أخرى.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90496" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
إغتيال أحد علماء الطائفة السنية في مدينة زاهدان جنوب شرق إيران على أيدي عناصر إرهابية تابعة للموساد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90495" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بعد رفض باكستان وتركيا وترامب التدخل..
بن سلمان يجري زيارة يوم غد الى مصر لطلب النجدة من السيسي وطلبا لتدخل الجيش المصري بحجة ان سيطرة انصار الله على باب المندب سوف يضر بقناة السويس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/90494" target="_blank">📅 18:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
إذا كان العدو السعودي يتصور أنه وبعد 300 غارة شنتها طائراته خلال 5 أيام سيبقى وضعه آمنا مستقرا فهو واهم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90493" target="_blank">📅 17:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تستهدف تجمعات للتحشيدات التابعة للعدو السعودي وتعزيزاته في صحراء الجوف شمال منطقة الكنائس.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90492" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية تستهدف تجمعات للتحشيدات التابعة للعدو السعودي وتعزيزاته في صحراء الجوف شمال منطقة الكنائس.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90491" target="_blank">📅 17:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
العراق يوقع مذكرة تفاهم مع شركة توتال الفرنسية للمرة الالف كون الـ999 مرة الماضية لم يلاحظها احد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/90490" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSjceiiGYIF_nyg6CqnpO-ODb1MwzB2UbVtzkxGoXIMIxWi6WiwqW5Zd2BtukE1BjYkOlSP11phLU3npNSzmyenx0WfHhIdMROE2lQiQecYZNOZCDoLNZ2eFGKGpWt5OdCW58r-jXe4hRbEJNkezDmC7lVFViJtALmV6gDBzWLzBCpURZYdj9nMiGuqA1_Jkzyv_dR5j7RbbiLzBMmaiqFm3BoewjnG7ufXtdIiMvvbvf_o1LcYSqPZqcA0hMd-Nxap0PZGHxaDbhEEs5ZGHPG2leyKVuBgKtz86GrnboJfvRb7aJvyTi2rVtOl9L8fQR1H_ar91ErTa_fqX7lX_cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط ترتفع الى 109 دولار للبرميل</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90489" target="_blank">📅 16:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مسؤولين سعوديين لوكالة أسوشيتد برس:
تعرضت خط أنابيب سعودية حيوية لنقل النفط لضربات وسيتم إيقافها عن العمل بشكل كامل لعدة أسابيع لإجراء الإصلاحات</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90488" target="_blank">📅 16:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba222bebd9.mp4?token=EfxbjJGma1cT2OspWGtveNzJK4Y5FL53PxDscXP6sygVwObLlnT1EMgLFNdKQgAD-_5NgK175PiHXZyResPKH77rKhmXPqou8NIQ_sKUTqq35UIA-6hAEKEjU1sWuhUb4vOR4uCfqShcOwywH5h90VZLM_OMYIlGVaDXxAxnVOuBO7pq4XjHM6hp78o7Y4tgUIKC9kCV-Lqx_GWivyTRlTPZqiaSPzjbyAvMK4oEB_dD5BGJvAkcnFZ74882c0Sd2UeJzM0iExo5Fj1fBsgOKnXQZclKK1W0c8AERNb4zqzp77ETvdnCXqOb85LsOK8bgpuz_3AOwYXduynGKfl0FhW1yzNkR5iG4oUHlQoK3Cc5YgrHE8QpmbVeqR7Lpk9OjQrn6v3STxl9cjdiKEAOmpOfK7vyS7GkB8RfAGp4HcHkyCEX8pxoBdQIPhdOO43Q3d2UBbBDwltjfns6eVsaZwZe_TUsxmv3_bkh0MxEWTkw-nsxusYW7WxTRPQZexMrZz5BOtdZk4pXMsiCswsPo35sBQ7BOJy6-CQq2PRYJvA40M2gep8TSjFjzDoxHb0gd1KkHpEu6Z7i7VRM_H6TFFhuiXQvdTlfo6pFA9ibyOUOrdTg6i_iue_bY1iO0xUg2pwjXROHVTSr2lXFxOYKt6kk6hgCpP9BKpVyfH0QgBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba222bebd9.mp4?token=EfxbjJGma1cT2OspWGtveNzJK4Y5FL53PxDscXP6sygVwObLlnT1EMgLFNdKQgAD-_5NgK175PiHXZyResPKH77rKhmXPqou8NIQ_sKUTqq35UIA-6hAEKEjU1sWuhUb4vOR4uCfqShcOwywH5h90VZLM_OMYIlGVaDXxAxnVOuBO7pq4XjHM6hp78o7Y4tgUIKC9kCV-Lqx_GWivyTRlTPZqiaSPzjbyAvMK4oEB_dD5BGJvAkcnFZ74882c0Sd2UeJzM0iExo5Fj1fBsgOKnXQZclKK1W0c8AERNb4zqzp77ETvdnCXqOb85LsOK8bgpuz_3AOwYXduynGKfl0FhW1yzNkR5iG4oUHlQoK3Cc5YgrHE8QpmbVeqR7Lpk9OjQrn6v3STxl9cjdiKEAOmpOfK7vyS7GkB8RfAGp4HcHkyCEX8pxoBdQIPhdOO43Q3d2UBbBDwltjfns6eVsaZwZe_TUsxmv3_bkh0MxEWTkw-nsxusYW7WxTRPQZexMrZz5BOtdZk4pXMsiCswsPo35sBQ7BOJy6-CQq2PRYJvA40M2gep8TSjFjzDoxHb0gd1KkHpEu6Z7i7VRM_H6TFFhuiXQvdTlfo6pFA9ibyOUOrdTg6i_iue_bY1iO0xUg2pwjXROHVTSr2lXFxOYKt6kk6hgCpP9BKpVyfH0QgBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتظاهرين السوريين يبدأون بمحاصرة المنافذ الحدودية والحقول النفطية احتجاجا على تردي الوضع الاقتصادي</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90487" target="_blank">📅 14:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صوت الانفجار في العقبة تم سماعه من ايلات</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90486" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجار يؤدي الى تسرب غاز الامونيا في المجمع الصناعي بالعقبة</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/90485" target="_blank">📅 13:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجار يؤدي الى تسرب غاز الامونيا في المجمع الصناعي بالعقبة</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90484" target="_blank">📅 13:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اخلاء ميناء العقبة بالكامل</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90483" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انباء عن انفجار في العقبة الاردنية</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90482" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انباء عن انفجار في العقبة الاردنية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90481" target="_blank">📅 13:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
هيئة النزاهة العراقية:
- السجن سبع سنوات بحقّ مدير عام شركة توزيع كهرباء الوسط عن جريمة الكسب غير المشروع
- قرابة (13) مليار دينار قيمة الكسب غير المشروع في أموال المدان
- الحكم ألزم المُدان بردّ (25.7) مليار دينار الذي يمثل قيمة الكسب غير المشروع والغرامة الماليَّة التي تعادلها</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/90480" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔻
تحطم طائرة خاصة في مطار مصراتة الليبي كانت ستقل أحد الشخصيات والسلطات تقرر اغلاق المجال الجوي</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90479" target="_blank">📅 12:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بن سلمان يستقبل قائد القيادة المركزية الأميركية لبحث ملف انهيار المرتزقة في اليمن وسبل انقاذ بن سلمان من الورطة التي وقع فيها</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/90478" target="_blank">📅 12:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رشقة صاروخية نحو خميس مشيط وأبها</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90477" target="_blank">📅 11:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90476" target="_blank">📅 11:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇸🇦
🇾🇪
القوات المسلحة اليمنية
​استهدفنا المرافق والبنى التحتية العسكرية من حظائر الطائرات الحربية والرادارات والمدرجات ومخازن التذخير في قاعدة الملك خالد الجوية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90475" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
🇨🇳
🇺🇸
الخارجية الصينية ردا على تقرير بشأن مساعدة كيانات صينية لإيران:
اتهامات لا أساس لها</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/90474" target="_blank">📅 11:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
🇺🇸
سقوط طائرة أمريكية MQ1 في سماء هرمز من قبل الحرس الثوري</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90473" target="_blank">📅 09:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpw9CsiJ1kUjijGiSyAEYM1wbfvCVa5wrk6ZM5yOqpke_tnM1XWw7FuWEdnARIXMoIcFJkiu1LaZTH9Cv5tABfO2dlppmIrRPXK0AL_7lfMM8mj3q-0Xg1_PhhNSKLhNmUmugHEoCfAKYLUhbOjeOzq28bArr-6hSZrhVrhkDC2qRpA3lq9KEhep1gjjJmhr8mb9hhX6IErtKUjzcXO9Gg8pw-kwZSfnGTVu39Ms529oGkRYYRdtmA6v7RL_PlgthHMdp6GXuxPypBd33Z_r2fAU381Jf3rjyiUQ1Z14oX73xeoN7u51lN5IIGpQrXoxXslIFT8TkTWykPWI4-ji7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
إعلام العدو:
مقتل جندي إسرائيلي خلال عملية عسكرية في جنوب لبنان.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/90472" target="_blank">📅 09:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇸🇦
أبها وخميس مشيط تحت رحمة الصواريخ والمسيرات الإنتحارية اليمنية.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/90471" target="_blank">📅 07:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇸🇦
إنفجارات جديدة تهز السعودية.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90470" target="_blank">📅 07:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇸🇦
إنفجارات جديدة تهز السعودية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90469" target="_blank">📅 07:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇸🇦
إغلاق المجال الجوي في مدينة أبها السعودية.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/90468" target="_blank">📅 07:00 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
