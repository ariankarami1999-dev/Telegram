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
<img src="https://cdn4.telesco.pe/file/LFjUXjGtxS8fkyn-rrH9VkjAP-S19_DuHEw8tHEDJbh7p4yC3jfK-27DGJGhyCqBi-j7NRcGuDwzsC7C6Lc8F27AmEnSVmVY58xr8h0-ntG9ySfbOVzQBs8K2yiCAvmBrelOxE5NIV8_Wx7ImrHaSabhHe_XmrArfJbhR6LlBtgiwoJC92RoXMxwkkdts_LVGtZrthUaqH2C2YthOV6InPCnmKrGqFsaEG09asYI0lfaWzfJ3kgmuEM1E2-iE3X-YniK66P7hBH0_4BYFNZ52LwhQP8BJOHdbsPvVcX7DN4Sb9XHvrTevALv9rh9A5m-YYX_4S8-oXj66du_sjeDjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 201K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-80896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RN_rz7pu4QuWu3p1_K7Li2lxJ9eYwlrH5OqGtQa3UX9afuNFq1K4eQslypcLlm64C41Z9dNQZGBPgSeGONKG8kaWZNOH7gtn_nGMUyU35nqXCO1WHrflRPy-UY1dE6v0sFk0C0KT-j23lQtDVDiWI3kocVOMMqBUWeP-vO28xnsGHcI0-vncg_0DWPIkHY_tIkFQ0WHostUqUFFXwElIAVXIoCrEjJvb9FsyxJ7vNClzljfFJDsdpcn8m2q2wcI3s4eER1uTED7GtHtUH-XtbW8nQ4xt5XJGOTarOHdi2yGeAKE47WVCwaWjVSa4RxKEotyzyMnPqsQVXH0chw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه :
نقشه دانش آموزان برای تعویق شکست خورد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/funhiphop/80896" target="_blank">📅 16:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80894">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arTgiMrd3ig3jXzTMltebUl7aWLy-Z5xuIwrZd48qrEoOjUl4eZVlojlAemzh0UXnXqXj4oHKXoA8JO4aX3g0LSdeH17KLn9vzNBZyjXV7R5wMlks6C6GDAmsr2vvM8WOIZrY9ttVJDOLn1Jkxoph7cp4aAic3rdiW2Emcsm-jB1B0wI2JQnm1nUMeFTdJPZPEU8rYIjKQBeJJaVbbxSm8CoGciv1S9FO5lWe3TCA13kkfGKnWzFVEopVyyfRni1qCEci9K_qCHwPaO__AgK88QDAs6UyfOCyVmNARIvDeCx2MwIxC0B_fKBZ0mKt78OwKz_SY1ObvL8L-6AVaW2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpeIoukAenjbhO3EqXywgMmp65ktJGA8kSoZmqLWFNUZJ68CrO-D_G4FDPu488-NECN9jPSCdxt1bxenH0Spzq9J-GqQEnMb81r5wY0w2uYjrKTv1OyKIXVL0rth6mfW_a-hasD8jdQdhw9VzEmNJNXZuaY7Fspu73axWg8gcdSsOFNLAi-TGidMJdpTdsKm5_sFzFN7NrlVnPjm7qtEGq1UbFaK0FTPcfnpgHsNdbdniPc78knBEYU7yLGtdr8XmQU6b19BG6XbqPkxgqblss3zLHHSXfKBQLhnjZTVv3BRvc7gfeN_Pbk2jrta2sixevaEKoxmZYOhECLNnuvJFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دکی و صدف در حال عشق و حال با پولای ویناک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/funhiphop/80894" target="_blank">📅 16:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80893">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHU32VYQGK79HIhGwUahiQMypSm-JT-FYaM2C67e2vSY2hOh_IvSeT3_aX9KpYm4_2MqpCKFzdaHOSaKKNN0qJThzOv8PdIi3XlEproqQJ4FjNLtivJpIgF-ztcM8nuwyvQlTFmI4zS9Asy5Mokdja84wQNHLCzBXak_RE14bTnWkVsCXeH0wJ4iXEP0pIfYf74HVEGNptPU8TDb00qF4SqMTsIoehZVPcKrAOMmD2274N0cXZYWVFBf5eiSZPjm8Hbgh_MQIrBDzoVa5CGp1OwYrA9ZigMthZ8URfpHcIDCP6IuGF7qbjG6YafBiWNg84FBiUn0gWd-wWK52QBpDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/80893" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80892">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یکی رو گوشی این رپرا کیبورد فارسی نصب کنه تا گوشیو نکردم تو کونشون نچسبارو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/80892" target="_blank">📅 15:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80891">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیروزی دیگر برای جبهه مقاومت، حوثی های یمن محاصره دریایی علیه خاندان کثیف و نجس آل سعود رو شروع کردند، به امید آزادی هر چه سریعتر عربستان از دامان خاندان کثیف آل سعود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/funhiphop/80891" target="_blank">📅 15:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80890">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_d5UrS3G2_qj27QD_T_37haVNuI3A3lyhhIq7mkF13mda9vfVEwmb4nKDHpLQ8Jptf3jeWpEzZrO2EZfI9_DXVrm14cvUs5T_t8srBvFvAawNhfeZopHar97UIJGyUgXSt8fHlP_t1-Lm8T5DdXaldsO7Mbm75zKHdLsA2KWy0c7p2AtWA1tHWrpQ7_5Fv9dcBqY-qVB0UJgUD034n92F3aD5EkoxM80s327P-SldnnWFX_kMa6qN8IWO1eYxekvao7_gn3yQGMKc-cnhV6IjBpvRRmE7Vw8-xWIHYW1CD4gD5KVC4-SqM35OIJNgh1EFPKUNx0BVus64upxSaThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/80890" target="_blank">📅 15:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80889">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaH-chSWxTIj80vfbscZ0XZyJjqjeaQ-0enb4Qv2_-6fXDxh_r3wX1USlzMruyvhUI-rQyXRFJPNP-Bw4JFIBmShGvj6bqSXyFcmKIEqN7fw0MVrPC-96nHJhNMcBvT0b8jz8y97TbvJEwESgS_Slof8OZcM74C4-iTg2jU5C09c_4a6TlrAVBkYb09TdWYM_9_pqURZ_WgtzMK_kTfxaBQc3yBon-eNB7f--t7yMiYEI8f-uIe69LcTyypnzgnO7zXyWZ8KN8XpXYYM1BpVLVwnic4qrXgIu5nq2TU2vrM0jJPBNZWQ1_MkKndPwiveBv4_rCLbK263VxMpWq0OUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیجی جان بر کف فران تورس، گل پیروزی جبهه مقاومت را به تیم کفر و استکبار زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/80889" target="_blank">📅 15:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rplo6zwwTf7HHiCvnPpIvjhJusV4kNZt9V6mVbWOWztd54oz-V29HTnnwO1YGY_BcTCtnFmYanRVR-CAc0mJvLgp9UjIVniwakt8A-n-xg-PnVtGbx0khEeDVvB0-qhzYjhi_CntHgM_7Y86XZEM431PriCWrOnjM2-fNDICHxcQ027jaOIE6F0LMRWjqA3jl4D84B4wyZVWifU8PzI4Fh_6XKwMR_YdQApSEVQMANvJR04OVHpAWTzqhey03i2nACXrKOT6lnERz9Bxfq6npaPdFdzAYS1A_I1y8CkukrJTXy9umYb_LJRsXVIc0mnd-AkIQ01ZgXqLuWhlfOyLiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین همینجا بازیو باخت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/80888" target="_blank">📅 15:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد پس</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/funhiphop/80887" target="_blank">📅 14:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80885">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اصلا وایب خوبی نداشت امسال</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/80885" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80884">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آقا من هنوز سیر نشدم، از اول برگذار کنید جام جهانی رو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/80884" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80883">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N53EgiBQraGuh4dOAgIJnoqKkOKTX20F98evSAVb3mQTGHI5bnG2PIz6QShMr8SvKJ_2w79bgs-dF-PcurmytCcq1TeCKUYH2OLPFA26deGu7-pYtubERSUUdQ-L3QVLZ5tqgj5qUsvhnlcS6PlZqio2E5tSt35_bNMV8f6dmyMLJ4hyPkxZX7jbooDPb8BghIWKziQiKhV5nVDEnhGbOSr0AVxECB7IwUFeiAW25l-3tvwk9sKjFw0K1LG12cv72Jt5PtE5UyjSD-5bO-wbz2ehEsi2WQ1yG4mv9UTM9yfXD0TfkyWPCvEzP-Z87HvpYNpCH9zwMJU82Bx57geL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فواید رابطه با اسب.
#بخوانیم_و_بدانیم
#اطلاعات_عمومی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80883" target="_blank">📅 14:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عه ۲۰۰ کا شدیم</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/80880" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei7F8GGOKrYtaqoVU0vtGN1-opwzZnKcVCsoREZGr89OFIQy3DhEW_K5tGHSJMltPmTUpmufOBuKrAKLLqJOGFsYYOvU5gYCPwrL9IcagLwB1ZlKlhRq4uDMT3xxNOl2JkjFB08LwGveHmZDnokvUFeV5fsrBFao0WoRdOBoJnX9VcqHwru_jTPm-vmFgo00Uk9gqZc5QWAUA2MeFOOdPZIg7nwQqO3fhmmgXhIg6mJmnucLSHnSDeA2obABoUcsWKKytI-Cxu7Ijj7ClY4aj8VOloP__WMCUyndicD1UdxRSgXWhtkydUS1jffklo76dFE8s46qFVy6zmaWQ9JSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یامال باحال ترین اتفاق این جام جهانی بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80879" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80878">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسرائیل هیوم: نتانیاهو امروز بعد از ظهر جلسه‌ای اضطراری با هیئت وزیران امنیتی خود درباره ایران برگزار خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80878" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80876">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUGXGCZyRHRqmGa2zZ-g2CsOiR3vB6DFrRevaUwGnMMV3u5gkc6IFc4i1LMBUR-U6usDqN9597-J-V9TnVHEGB30FqRQNNlPrmgnEZKFxNWDH-kYcLWFFqTWnmP2v813ZJ4PTvSzzEaDsYmRfgT4crWcHOd3I7AdogOfxAtERuZ6Z1VaSXkquoMabsYeUCOjASY45GGJrGwpl5ngOZSi2ZZIMlt_4D68U9PsP3eXaI6R1SrXQI2AoLdEgTztbtCUhorBBPz3xEqu-Elb-lrwM-l4m_n45bTCiXAKwNcQA5AWEORkDyJIuHKBUXASL3L8uaYgfzg8R2aZTBwcLxCssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i09wwmrH9q0-csQctoyL7pbAjqCLnonXdeXhjQByMFYnW7VztKSiKHiUMp9bEZwI6yWltUtcLsd-s4g4felaehd_AOrn5t_yA0n7s2V4Q3-MZ9rKXWHKwdi7G9mUVhKuv0quZmb2MdkmNtTbPJvkJwghO8cvMGBXT-XKW5vvCmth3BQVKwE2617lG97_yKVMczcogKox7bDWtIqZLTUVA8QErRS6fUfn4P0yvA4fNko_K-VoJnltl696qLsYmS8w4K4LBinp64OpvoC013WPoP963rusrgC1s3rRCfEO1HnG754zgoYg1-p9VrYap1HLJaUqrkZCUJj2S0VUyRillQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا اجازه؟ امروز میخواستید امتحان بگیرید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80876" target="_blank">📅 13:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80875">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYYt20FeaAmnUbcAFOBmuIbOCCS3-_pHGjV7kMNEV8BZQkE0S7dNYdS4ZcXfNI38IX2gZZE4uGX2VM-3Ll77xNq4vqymhViFpbu7jqoLX7S4oivhMBYi3Q3lLu-TVxIbGaeaPCqU6Xe6k3tJ_atj2wXMv8ZtJrwGDlz8Zc1oNbys95MP0Rdjz2Z38Zo9EwwfojMIHXarChwDhnmQ8SuUwWTIXDHTeSQBtuzRJzWogAElxgjzuygs-KtQkM9pohAB7nr5oQFnjyohnydyYJOhCetJcimqp3hws3NP1cxpGYIlcOXPL3cB05tOIOso0qGJ0UVn6JAus-vibpyeDmfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟ این دستشو گذاشت جلو دهنش به ما فحش داد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80875" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80874">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDiLc3f_H-p8LpoJcSED9b8aWuougDcq60J80ng9C28kz6_0XDPgHgEHNSU7Zx3FOR8GnzAGgSqy3URGI5ZNf5Q_HIIBMqhROqNTRFRztZcII0-oke6E93Cd6WDdk9iEW3oPze6lonPjbhBYJYpkSzV7B4xS7pxyPEgLLmre9ea1t556WOyYY4pWwF8RgdeTFjpSr5L3UcwqfpiNOuy63KpXpAD_YUuIwX253TjytR20vIYFj26_Fr4-qccZJpo0h0OJ0X0DVcnT_VACLQ_G4wZ4Rs5aqWyygJ41Gy0c7y01PdzuSiYVWb3ndOeGAD4Xr6AkTwiuB4SYG-tb9Xeajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چشم های یامال احساس تنفر به ترامپ کودک کش را فریاد میزنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80874" target="_blank">📅 12:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80873">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Woi43lGZPTicqbBI8_f2LaHitBT7kH3-TEHMLE7PMoE70ZT7-cJrI-edsSO4UyUdRbOULPuFy3EdYgg4Me3zdaf1xMf0iEWRgYKulXNuKJfSPcM5CBrGqeH4Uvbqmua66n8Kk9LEqvDJZi2y3xh_xlNTji4FQAqWhMr7g0byxU9EfqxFd9RkGpqFVB6tu2cZqOSJ46Qe-H6Q0J6n_zW8W1SIgdiJe-076WrrDPEGYZ8DrHh4j4oDpx5nIX7TkHG8-E29Mjv2tBJYGbo-qNHKmfkHfCcY7N7SCDyporktI6XMN4brC6i0LItKN2f5LXA-g_YhmrqH7JtnNyaCdrYLdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک پزشکیان به اسپانیا بابت قهرمانی و افتخار آفرینی برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80873" target="_blank">📅 12:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80872">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدا هایی که شرق تهران میشنوید مربوط به خنثی سازی بمبه خوشحال نشید، امتحاناتون کنسل نمیشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80872" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80871">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf4UaRwIispU2vzrLXgcpztWM9N6BoyZSnYbhlApqsdVUB1YZSPFND4niNG283QpKBKwa2w-u5kMdZjQenlGPZ-2OidADVKsf9stmG9juW43-OrCT4DioSLmNWyppKxkUnBgIFSWFIbifG1GNzTBzwz8bs8DGKksPPwldw0gx-CI-HDEp7uk0HbVKDmge08L9eIZGgQ3so8IciZRE8jSaaDw62AnHQOonSjAPJxKme-xaPK67b_8O-itM5vya8qz4dcBAHRKGPk8KRRpDsF-cvnYI0YQwN2vrCGGNsIxRUfJP9eYcy38_g-Gem5uj__FOdH_1_3Rqn_zFP-Rdmj3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید عمو بیژن در کنار یکی از طرفداراش
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80871" target="_blank">📅 11:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80870">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az5GLdDfS8H4277cdbv5ILUf66fKudWK0COx2NgoIREad51fjr44TErvLKoFzBUz4cgEBtMKYCBW06UKLdVz5OOOYPz3inYeeN454JzEACEu2ubR8P4HuCf7dzBXb5nBg5pk2X1He--hXWLoazzXOV-DUNPkH9FzKtn56Rdm-Nf6tqjcQWxrwtXg8o3kMuTWrd1aanMlZekJYc_3Mer766SW_yzQL7-tmjK073pDfeyT6VUj-2dLgFAWMX431aqN1iKaR2947s2L3avcCfXUl-z2dw0x9mIHCXw7suoJyE4oQ2cBpO6JiYCbPFIV-Dq4LSYLlkX_wlfeDbirZQT92w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی این توپ طلا حق مسی یا امباپه بود کصکشا
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80870" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80869">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDWN9NHmiJG2879Lc-pVHWiORjQwLZ21dHaeC3nfMDlxu1qbyDtSh1WjwQxLXOt5PYmj8adkVyOvL-Qcld7prDm3JSopsO17cWbGltqhFUnQHWAc6VBMi7bzJmEhWZOQTtkFOTBwUEmHxLJz94JYHl1o6SA-mXmajlTkFRhaIKB1LMjUD4L9Z-8CS0cuTbv3exl_J4YvpmGcR_jP12POc0Ae1BOiXPJD775NOM_NlyI_sPn3jRsk2xidejxX7xZK0jcs9pykjwQYIjgLhatvdkBMywxI442u5l58fWF2FLPf-nWIOzUTpaXODr8twqrSvtEHxMj0CalDttzhu4rNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اسپورتینگ لیسبون
🇪🇺
-
🇫🇷
استراسبورگ
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۲:۴۵
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپورتینگ در ۸ بازی اخیر خود شکست نخورده است.
✅
استراسبورگ در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اسپورتینگ ۳.۱ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما بماند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r29
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80869" target="_blank">📅 11:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80868">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffy3GrnbDlxqFa33DTwEZ7lyip67Njxjo2xhdPWL1GyW9k8UBJBS-lI8KIXC2ayoStaB9triTom_dnK1qI2VXw88E7vP08AqEtkoHjc__EJ5qjM6WNAVIM4TlNIBch1qufUOA6fWTAWO4MXBE-acaAsnCmVVUjge9L6UX30WZsltnTXpspTMnm07vDg2yP7sfVeZVu0hpMj1azv8MmLQiUMWWw2wfZu4rPoLtP-mRG9lryrS4VUBQzgJmcReVnqwzbKKBNOHRdsE05AhIE6lbyYvoVBkC--XT0KznWH0vtr7WsfMcFrViw5lfglnrJsHyI0nvGH4ewH2ePN79TIX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80868" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80867">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVePdMRxYz7X2w_uJi7DtBKOxSYHaCVw31WtzPKhgvzPq1HxH1fId9RhBCRkUxooR91zD83N9w8xN1RqGJ792b7f5Z8YKBxL5ltGFXrzwsbz9ChtIoQq5IhfQMh71zd9fMKCtCRRdUvE02ueAn-7EoDlr_JAiGUaKWSKrY84NvzdLRgH-KhoTSHXGwTlIhLZ4ngeMQIQZdGb8fmf9PIB4yik19L0P_DOIZV_R0E2jvPLETCbvPTFaCXrtLov9dVcocJ7uRoZcx_mwnd6q80rSgUHFOgfNJ_hIV8nUE6DBNrzJlJ3zxQCK6V6VVvNBMNlvrMN-Au7_Mbk6fstfERvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس شوهرعمم بعد از ریدن به عکس های خونوادگی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80867" target="_blank">📅 10:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80866">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfMzcPMmyMvMIEPw2snZAISDXG35t1qaQa9NoMqMm4A4ko5bipTwoik5KV5HfEA2TY9LpM9D-5P7CwZfpNUL1iph4iCNOyl0oJ2OGGBwEm7pDCYgZxwpUbrVuQ7FcG5son74KADZZZU8D9yq8RjBBFYBl8hIcySc3oQov85hqvAu6dOHeS8UDgaeqlJwbF74P9pwmq1XrlOuyrbT7u4jvokNEanf3MELl3_AMHFIF8BzbkF3ptAmwxg3IcI_KjpocqL9PBKHjX2eEcMTUzbC2DGKyEzTfT9ly5otDxv06oclWxCWJ8I12rJxtDD47sapW7CQF5RaLJtT4N0bAd28nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۷ و ۱۸ دقیقه صبح تو کرمانشاه یه زلزله ۵.۷ ریشتری اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80866" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80865">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGU49Pihl_8Fd4atyQ-vkKpoQ4vZnXxaPoJRa4YWm6JSrMc3vLfNCQrjn4AqOlvdgq-UJiQAAFwk1jsPy_rlvm4vE3BUWIRbQnTCpcBabDQXXmOwrP50D6177UNv3rUW4KsuRHVhSbs7b747j44nJg6wpDGxu3u_wkNS1mL3u9-KKttbj5LICVyN0Z39zIuL4gOEo9CK2u_txCNIv622r1wMfqu-juR-WcNnTeib_NjgmNr5oESZj0GyFaVzckzl5wTjZjyuDId3tl1yij7Tb8WNfpH5KeVFTEMuI6e_RApFA481aCsH_i9vyvQAGy8sugRxxa4v7NBTSLquiPsxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکی Dior از استایل ایرانیای دهه شصت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80865" target="_blank">📅 09:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80861">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umBe_4zQ60ssGLPON2dDwPmi8t6ia8BEQmovQ82kHe0PhH1AjA4QIWzfWysT4jG_Pia6MeP1OCFYw962wr9OS9_0c_fqMzNsmiGLfJdSrFB09e7BZfYYj7rcWLxa7s5aslEMUE--xIOeapkQfxcPAG8ZYMzlNVSRN8KzM7ZKIMXclam10cSa6sK1_e1UWTQPqa_bHJ-J9Yi8MrHpwAf6bwtf5psOQdfrzaEQK_MOLTRS8jyfg8BCT4d2RkPgN2Msmm5fOFH6Wg6_lcmo9As5_Wjf4YOcDiKX-kQ-tLB7lo4yB77Ovi627e6fTPByF5iqpWH-7Ty8bW-rrHiS0JwQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام بار این سفر جذاب و فراموش نشدنی روی دوش تو بود
خسته نباشی مرد
🩵
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80861" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80859">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا که جام تموم شد، رونالدو جان تو کارتو کرده بودی، اون "i'm back" گفتنت برا چی بود آخه مرد مومن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80859" target="_blank">📅 02:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80858">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ آخر نزاشت تیم ملی اسپانیا یه عکس ملی بگیره تو همه عکسا هست کصکش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80858" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80857">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lf2DcImABFnNKnRA7T1pIjWsie8blA6CyLOheRcLxqC940DNSkdAO8Iuvuozol9RozP95YFogpMYbf248FkOuGT6vkXOb2cWlNEF-Tdxuqi9jbaykS3nDiDZRm_GoYqgC03XEM_WGTDIlbdNLryFuCNuHuJ2HUjQz_W03G3ialIy_jfXyURkBFSg1TyF1Qkwm45Rp9oWAhub87xjbJ2dNr-0hpxJ4A3LjSvyQMSRhPDm1HZF43yc73VaFzI3_ZsNV3FVb-Q5770zAaR4aou7gBukCbriMl-EfbVNDTuJf_GbuXhk39xMESVXTPnLq1xMimeeUCpGCscOJOO0iHMN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر خوشگل و کون بچه بودنت به ایران 2 هفته دیگه مهلت میدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80857" target="_blank">📅 02:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80856">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی دایی اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80856" target="_blank">📅 02:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80855">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب دیگه جام جهانی تموم شد ترامپ زنجنده حرکت کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80855" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80854">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بارسا بلد نیست سی ال بزنه چطوری جام جهانیو برد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80854" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80853">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپو یکی‌ بکشه کنار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80853" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80852">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szYvuaZmXFulkyPF2Yur8Eo9xoP9Ma40XC7WFFkkiyCL9S3ZzvhJnZjBARwX9DtcGzKVeKPkk-m9KF7l_nDBAF3gO_c5dHQmWWN4ihLN153pCHL0Y8CxCdFh0mvsBY9w0pGbg0wu6DxICSbKuwVulDCJHuC8394yZZLesoufmeE7HqOFcPwyrJGnX_ko9Epzu3rBuqjm6AUz1s2FRBqw0ymVdTZBnH5Q8R6wfDSs8jcXyrj-Q_PtC3YePPCPqwmh2naCwlclz4q2CCZdcGUTepOE7Md1xNTa6ymi8hmythgwxYMMYhFjDHWfCQSF8_pToZmWv9jbV7owWCHa6ZJSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80852" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80851">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رودری هم به عنوان بهترین بازیکن جام انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80851" target="_blank">📅 02:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80850">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اونای سیمون هم بهترین گلر جام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80850" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80849">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کوبارسی به عنوان بهترین بازیکن جوان تورنمت انتخاب شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80849" target="_blank">📅 02:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80848">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz8QsIwLTF18icYPPinTTah99pyH8n4yxsHIV2Jif3mp5kRCvl4XtewGkUi6nh85bMTVjc9w5Ph0BPCZJ09UtwQH1OKuTw8IJeg4By0tt8bk_Fa4jnoBIVBH_rCDcrMKV1cAO5tBeh9NI_lrL6TWftqUYOZxzjd6FgN_m-WQi_3XuMfI9Jjxr6GBKPXUETpiDykn3n9csklMReloe6--5T5efFxT374AHxI1pcoV6Y3rAOZXmnLEd3LX3whrvUj_KOit2brLntMXTcraoi86jRfrrTKZXezfP-NDBLGB8PcsKhzh9sO53v9nW1S3sETBBSkuvY33DM4y_zrrnHpp9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخاری دیگر برای جبهه مقاومت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80848" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80847">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd19SVdI57EzAAVGsbMzycrozv9H1KZ9HE7qpMHV9ZebfiBEBgIKNGdca7BoZY97DRsZpBWXaqdGgcR7bM1zEtjTmTtfZQzeoIKKLmUB-uqZlg83hErapP1_MRzBLTyNXVQ0HZQtpEgtjmirOIKqWwgeRHlJtvKh0AgWV2CweRzA1Sz90XbRJrPOYkJYMF_qOt9nEhyBanDJ_Jx26mGWSBWNVmzUXWKjn6ziLVbXaV5mqszHxRKM3E7rQZVfDCHulXWOBfYGZgmEIhJHxWIk8eN_b9KX7L6k87Lo4URHnq2ywv9wL2kUw1dXqcg0FJjxRKRST3M4Lshhgi1iYtcYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80847" target="_blank">📅 01:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80846">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی میشه این پیام بماند به یادگار  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80846" target="_blank">📅 01:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80843">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyFj7Sm0-jorZkI_SJasYTH_H031wLrHBvLJ_jncqHZaybcBrTfcPYFfYtLTrzM41c9Eql5qiK2ImWZfLhFTHy71SQw_v1N_EBptoSYJzbl6sLRKQvzlHvIVEVrT1EqgaFGLQNEIpNr7pgyn7XIJigdSSuX0VR4O0okj5ETERD3R0U7MYcuwQTMHNxLPnGpOT-JbtcVbzDi3R8sjNDXqOOCcSzKAen6P94HazU1KEM4dioQEFNEeex9kraHiAQy_YOjWusAXdoyGnEkwR9X_ItLNU4YbML3snbIc8_tKG-96L1FqBEH8Zi8cifCVUZ5pMUVZTIj_dqouVi-wN91oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/meXhywfIUbECGKMewL93uzlzkWzxlpP_3_BgFzdNOQO25ALPU5JA8_sngEY3vsAfVObDar7S1yVkedCTQHwLf97HhsmFIwPyM2agSPD1quT5phGQqkaakZilKCVLu0xSKZJps0l378BxyzAqMo_cc1usSG405hNnbsOJRxf5FfUBfVqI5BI7qQLtEaz5qxupDC26xPxqGmYfsh-wdrf-_7op12zJXLcDwG02iIYDbfL2aERv9lo63KwsOc-nkmk_faJWYs_fxO3vum4l-K5Y5ViLSBsMt-oNbJIeFCx4xwmsV_Bwl6yHZyo7mZQIBiOq_D2XAZUa0o48J16fN3qBGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پارادس چیکار گاوی بنده خدا داشت
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80843" target="_blank">📅 01:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80842">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خب بارسا فنا حالا وقتشه خیلی سوسکی پرچم آرژانتینو بردارید بجاش اسپانیا بزارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80842" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80841">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسپانیا آورده میگه ببر، صد بار گفتم فقط مصر و کیپ ورد و سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80841" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw-d04Lp8O-Xieh-x98RylahWIojWsrk8-M8geIH1BT9hU3HVxkBTlv90ueg8xTnxnteQYCNPJguXErtBXGdMA-qzGXwIu1sJoLPFQtHxnlgmBze477PCz6-kfW9MjNh_oih8s4tvrRUOPVrjipPFI-sNjkEwpUrio2lLtVxgaixMaiQt2GQyylsxLJaHff6XArOnLXAcY24HU2wt8EK4WdxgIPTD8wpUmCEBTWuQJD95w8EEW_z5pOs9vGPirjqnIydtpk2Dnx7XNhGEAL3HEAKqaI7qkBM16AofxaqCgMf2Qjep6vh0za4dTev5W3E6TvwbXIgxOH5Zw6sGkfCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟
این دستشو گذاشت جلو دهنش به ما فحش داد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80840" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دریک جان کیرم تو ناموست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80839" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لامین یه جام جهانی
مسی یه جام جهانی
رونالدو : I'm back
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80838" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80836">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txmTTrWpGOXIwr9dsN9OxwSSJ09B_qbKZMtMbNFlXoWEdtBAUaEgu92m7CpNussxSZ_pevOz7h8SOvkaRzAH63n757X_pc7s8W15smMD8dInFuDsqKZA98snomvn5pxT3SObOdsz0InsMigXOsj502UUq18H96e__q56Zbu1eQJdkaVtZ5bxNomHsKnR9dkPhL3v_8rZbqh5agGOghaL8LnJy6RipT8IcBmi81u7gvHgsJHSKqKendIRV4upf2F5Vxd7YsbmtfyY2hY8F7EaYFNgH8PIzL26tVYJSaJGWMUrEUTVtPTm_rz4tUDJLi_39ScR1bHGBc7BvfE8-5_c-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غروب یک سلطنت همراه شد با طلوع یک سلطنت دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80835">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=uX-cWMMMqWZpVGRiGdT67pBx4atbs3ArvrIAA4VZMcfJiO6n803Q57lhDRdsFAX0dnJy6TxlAdWtKxgiK-urUIQIy5m_SEc9HeNENukCzL3aRTXI-mT74y-X_KPaBaUOY52D5W4MuOlEv3f3CRhxdEzqnnwtNZ6__YXHamR3eTYwR7OReiEE3A9apiaTk4rMsgTcvzF6fG8pLgseLNgENU_uEPjWMS3CzfKoCxYDU_slBLN7rtZw9E4Bqmfex-u3wx-SO4OHsrp8kwlG6qzFfew9dysmgvPJyRFaEne7pbH6s1SRM_UG37BBcEuqx8_lMeP0-edmAxkYH5QEE7Q0lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=uX-cWMMMqWZpVGRiGdT67pBx4atbs3ArvrIAA4VZMcfJiO6n803Q57lhDRdsFAX0dnJy6TxlAdWtKxgiK-urUIQIy5m_SEc9HeNENukCzL3aRTXI-mT74y-X_KPaBaUOY52D5W4MuOlEv3f3CRhxdEzqnnwtNZ6__YXHamR3eTYwR7OReiEE3A9apiaTk4rMsgTcvzF6fG8pLgseLNgENU_uEPjWMS3CzfKoCxYDU_slBLN7rtZw9E4Bqmfex-u3wx-SO4OHsrp8kwlG6qzFfew9dysmgvPJyRFaEne7pbH6s1SRM_UG37BBcEuqx8_lMeP0-edmAxkYH5QEE7Q0lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80834">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJhFgsGPUJ5OtQhtwARQht0XGao1VIqFesB71jC-Puv3pYj4HOlCsucYxCGL-z8aaTxFS_EfbnuJbGYyC3J2Kgt1wZrwB4WdFFp5cAJalaZKb8TK_RbcVqOTAE8osAmZl4OVLtyA7ZOJBgtKmKL5565TynIz3PjJDanq7kikPDXeZl2HezLlFs1udFgHzVI-TY6ccy3DzInLFo2YjwD1UCvnjtN_9nB3SJZa3w2U0Kd9-AVgjbO1vo_EYptcOxKWP62lme01fIZRfuAxWuAiyOHUwBaA0bR9EmZMmO8eBiZVgYte49tP2r3JQWNCECruc_1BAVZa6sfo6r8M45prbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنا شما بدتر از ایناشو گذروندید اشکال نداره این چیزا
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80834" target="_blank">📅 01:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80833">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umrQAe1vZfvQfO4HB91GoNBmnrSvjG5P3DHQlKofpulp66dwSlNz_yz0Y-4gaa0JTi77egWmMGna9YkhLY4H4Bfv7-nGRCeOQSJf5Na4DFGaKF6Ic-MSzstDAHjLQF-tjYZcZVmKX2ZnAqlfq7Dfz8fbhDSH3NvSsJSdyaJKWG_Oj2gtEG0-rPfN4An516AvpPElAdmiJ7H5EtUHxLX6Q6jZ_JnfRq_sJk1N5ukqlHv1ESo2C2IHGcWxGmlupW8quE6N7MFShYE-yqn-o9bgdkyfnpzrjqxl-6i0uW5KyU2zxZ85StsLfYIFu2zuHcbP9o8-J7DvDcXFb8qnx32t_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80833" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80832">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اون وسط یکی زد ناموس گاوی رو گایید</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80832" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80831">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ریدم گاویو کشت پارادس</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80831" target="_blank">📅 01:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80830">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0ADuK2cpV__myRiHFO956BAcT2TGx9ogTB0HoH3WLxMACUUx5lLKmG0yWPqxn1pADduAtx4pnvMvZXv0-yIa00HY3CGPipBt-INhwEzDkOfP6ZCdfNhikV26SkEksOyLfV1QZCCfX-STJV8PsOPgVEmpKHHyQRBQEEiWjuGLCpspo-jVU7waMAyFLFmnxXDuwditEpqJ4Nur3hTD5jyxIx1USvgWu_4CAYb8hl4wNhB7qFGg00yPnxSDzjygQmhG9aLQYAmEwX-AE_MVvGViv2xcmQxMRwXunPXXWwQYZJHs3UjXqEua1cfEscjprGUGH3DRs3qIswIYCtz3m81Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80830" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80829">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">داداش یامال هم از باخت مسی ناراحته</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80829" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80828">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مسی چرا اینطوریه، وقتی میبرد گریه میکرد، الان باخته داره میخنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80828" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80827">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسپانیا قهرمان شه پرتغال میره جدول شانس مجدد که انقد خوشحالن رونالدو فنا؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80827" target="_blank">📅 01:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80825">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80825" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80824">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80824" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80819">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=OnCe2h4iIm1WQh5PZ2absC0NktFs-xDUVYkWWB2v45Z2eYbHJRGbl0ux88H8OFMdGlMmfoc5meZobZupHWEQUAuOAZrKzpysiBXGG_ABvqilkbRCP2DRg3Ycdc3nVrWLgICboZJJLrloMp19RJaUJkI6oxHYCUTyfhyFaHZuQ1p4mhNGDMIEvzODf0-8Ttn3DlP_90dLcWMEh3rCpLV-Bm-fbLrv9VAc-muahJ5Zuw7FyN_C84Ww4uJa3K0Lq-3UZpLGT-Pt7YJeWiVZwvCyabBiFr0P9ukpL6Xrl5IpWk4N_DV02R2_V_aYOnDmMef_NbrBRYA9TjE76qkY3ZUAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=OnCe2h4iIm1WQh5PZ2absC0NktFs-xDUVYkWWB2v45Z2eYbHJRGbl0ux88H8OFMdGlMmfoc5meZobZupHWEQUAuOAZrKzpysiBXGG_ABvqilkbRCP2DRg3Ycdc3nVrWLgICboZJJLrloMp19RJaUJkI6oxHYCUTyfhyFaHZuQ1p4mhNGDMIEvzODf0-8Ttn3DlP_90dLcWMEh3rCpLV-Bm-fbLrv9VAc-muahJ5Zuw7FyN_C84Ww4uJa3K0Lq-3UZpLGT-Pt7YJeWiVZwvCyabBiFr0P9ukpL6Xrl5IpWk4N_DV02R2_V_aYOnDmMef_NbrBRYA9TjE76qkY3ZUAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80819" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80815">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الان رونالدو فنا با مسی فنا رفیق میشن بر علیه یامال فنا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80815" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80813">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">لاپورتا تمدیدش کن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80813" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80811">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80811" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80810">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بابا یسال گذشته از شروع بازی، چرا تموم نمیشه</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80810" target="_blank">📅 01:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQPnm3DNUvhAphIk15MN6Zty112N6MGEDi9ueOCioR9FDepqgxI1zJmI3fHBE2ry5u3LwazwVOctGMqbAoTM2_AXNenv4slSZJzEHkyN6bEh1u4KtyOpXLpFxKyhbAK-8iVqNB2DSQmqmV90biHhv5VAxaSXBQeJw_gDQY-9THgHFkBrOH88veAOZZmcl9b_06UCAy6VeR2AwFxKkLXWi6ENxubyeCr_A-yuWKpIqzXp3BOSnfMxs56_YCYim-Uf7EeSEU-HPCVmEfiJJ8O4oIxIQ-xXRI8j8TAH12mtzZaUyethYuOEo0OGA3AD2vX_atIIkpG4Vax18r87DaovzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا حضرت سیمئونه و امام مورینیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80802" target="_blank">📅 00:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این تاکتیک آرژانتین بود ک بازی بره وقت های اضافه
حالا باید ببینیم چه نقشه ای داشتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80801" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbz0zdIa822iED1AyRx7vG5_5ig3RJ7c3B-hjpIcS7lYmLy9sZxJWcq9WtgXQGrVrWPFGzp5Ck4hwhrZ5KOV86-x8gn3fI2t3bFPzEUHGQGAk4fLpb3-y4DELqHWPxoE2LPYirEY8G3gzrcHge3urfC5dcT2u6Ju3-lTrz1mEQmUqG2GWxEpm4wuRG_iqdZxrN2EMUO_U2QXjowiD0Aiqj3Ahf_OyQ9_QKaquws4LaRv_o0nFD7MI2bP4CP182-1GEA1TByGKERKgdECFqQPkYIBcAqfdrFjF669RCNpjhmRzyzrkbYMa8vhAa2gwe1UCjFS49ZWLrDIdQS0QdeyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یه خطا ساده بود، نباید کارت میداد واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80800" target="_blank">📅 00:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مسی
😂
😂
😂</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80798" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80790">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چرا اسکالونی مسی رو نمیاره تو</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80790" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80787">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اولمو اژدهاتو صدا کن پارادسو بخوره</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80787" target="_blank">📅 23:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80784">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwNc5VG0h6SGRMc9WAqQjcfRZZOCwBgbuMmAspCMVVpjdNNhPTnS2mODgPVR9OV9S7-zDHfmW4rmbdBwUbX-XKISY2mnOMfevkZl-jTHD0I2yTs9A-XxXphNpuNZ83yFG0zf6z-2EUKgeyIHg6L8-0QBru5KoUdKim2Qs5DRWlIhbZtB4VXr0ejdgtjv0CttmlmVGy3lBo5w0w1yla8wh2L7u1eCs2FugxK7vCMKKp6jDzfeVFfaEu5AfYB-FhBIeu-Pd4pE5Z3CFZwr8K8Xs-dUUjTXgMmpnwbruXa7E7VwRCE6wjMx5Cpr3zcB5kiBApV_jiPvxN7xeYcHHEmLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایت عمو بیژن تو فینال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80784" target="_blank">📅 23:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80783">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پشمام رونالدو پاس گل داد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80783" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80782">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پشمام رونالدو پاس گل داد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80782" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80781">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نقش فروهر رو سینه اسپید از عمو بیژن بیشتر بود</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80781" target="_blank">📅 23:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80777">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عمو بیژن سیاهی لشکره که
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80777" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بیژن ای ایران بخوان</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80775" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیمه اول رو بیژن مرتضوی برد
#خلیج_فارس
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80774" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عمو بیژن بیا بنواز بشوره ببره این بازی رو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80773" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فن کدوم تیمید؟
اسپانیا
❤️‍🔥
آرژانتین
❤️
سایر
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80772" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من فقط منتظر اجرای بیژن و شکیرام.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80771" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تازه دارم میفهمم وقتی یامال تو تیم حریف باشه چقد زجر اوره، بمیرم براتون رئالیا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80769" target="_blank">📅 23:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-vNj1wBxSPLd8KGRedrzriRY9xi0YpT6CsO-yV7B45KftRUY2L6e-yT9OWNk3JZoLaUQB1ng-8k_baK5_drWksLclkc1CjHu8Fq5jgP_fkivDU8atZIvzY46Z_YlcIxvtCxjE6dmFAFeBeRKz0cuXnQbxPWyJeeUb3iBgRuEi-XM-uyQh7hKU455OO1Z3cgN5-L9Ysa80jBwQhqrIvCn9-wI9TuEdaLsQTkShNKy6e-b-wDG9EfXpnXfWayNTY31hl_IpLfOMZVA0QAepjdJbcQyRK_y31sDdK-Cn7XCXYle9ORkPtXETkiaDX85A4xONKwUyVuyCBh0vSl5qEl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو ببخشید به من گفتن امروز نزارم تکون بخوری</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80768" target="_blank">📅 22:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXvoAHkw_LtPcr0a73QS6_tgJ7LO5BGulPanif6lJelKyf2SPpzKIiJhO3p6GRPVS0yk0rEQEX8K4fuzvrws9YqkoHxYEabP3-CLi5G5B8qvDURHDSZLo2EXGngq15NW_lDhcupEFQnhIqoYMKjg85v8jmInyY9FBmlQmJ4ZR3_Z20OWylDu9PXATjaqHKbs_LmyMPCFgpY_fYBhK5puV91YaYz3mQbdG30BdSPeEJ8qQaDECj_hD8JPaYpvhDHTTFN6-4lkug828-yPkcxTaCNMyn26CDzzWZxDsEBA_duecVk0L7KwtUFxeXwmPurvoDReFzKhtlAYiCFtPcl6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم بروس بافر(گوینده یو اف سی) تیما رو معرفی کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80766" target="_blank">📅 22:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80764">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آرژانتینیا هم مثل ایتالیاییا با تمام وجودشون سرود ملی رو میخونن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80764" target="_blank">📅 22:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80762">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هرچقدر میخوام خودمو قانع کنم اسپانیا قهرمان شه برا بارسا خوبه بازم نمیتونم قبول کنم برد اسپانیا رو بخوام</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80762" target="_blank">📅 22:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80761">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان شما نمیتونید کاری کنید کسی که بچگیش مسی یا رونالدو رو دیده و عاشقش شده بفهمه اون یکی بهتر از این یکیه، حالا هی مثل کصخلا فکت و آمار از جام ها و موفقیت های فردی بیارید و روان خودتونو بگایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80761" target="_blank">📅 22:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80760">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0mdrYA6-QwfqJr-MK45Cb1YWtai3bxQupTfoyYb-wxxLnxb1w1Bbskk5waNHVtmTdByFO1Nxk5rxu0d2uUvrFiPU1-t2YMQ09Ts59MLY6IawC2UBqobWYQ8qRCwZv16pPaQ92PeqDQwZkxaMmnifu8hnlMBp_VYkF7yMIYRL9BVCwktAGwRoOBl9B4DDBWcJYCELNRLOoKn6stc02aI7gIWK3AW6HcRWUsK35tU9w5Fz1IuUhAc_51KvcERwwb3LLNDYmqFFXiECjGa7tgMkgjH-4qA_SPnIrdNaxJzWjuB-vuoZRrCTZReaoFfMM8eT8GrE4b0taPHMM6hcoOjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80760" target="_blank">📅 22:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80758">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSRNf0z4KwzF9oUuiXLKnVNQKze1QW0k4z3yWkpv39whNtmcMVL9hsozEVnA0vR1zK9-wimkZxlsKhjBpAJtP2KqYGU0VKisjavBcMDqcpaczl10IujT6jUt7Nss81C7RH9nWDHPlMGs6DuUO4Zw-z1v_gMKRvs1XVsE6KJPFGk9lrCP4AWo95ErUS_OQ7G6SgbklreYxRHqqNO2MKDYfiGJQx8hbENvclvBnr5x31KzN4PWmZthVj4aJOOOlsN6djRUeZvNCtXXIwfmQhVpCQYOMSfrCaBK2cyt8h_DIHOrnij3D4jAwBS_fHeD3P2T9H899jzt3MScvrLJOJOA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVkWWJh1vIhTzPo983ZwBEH_SYYQx2ggc7HGOb21LEdEEaiuUhj5CdoKfZIN6J0GDci73idWYKw3CbIRIwGw9IeNaNItsdkR-aCYqHmTA0TzgkmQNM46171vTPl6fcVsK1RbfV8mIAQW4vTV3yne0RTbNIWxelDuH2EepDYqY0HX9VbW7qkv5LND8_epfg6U0vvMqZBUVwNFkGYjCEuZZjxXzJ2_rCmXKTOQGj2dvu94B9C44dOhHQ2Ru64so4h2Z_2SFGpijXtncKBPlDf8spYZPmNkdFs4yIH2HZYijLmT8l6OsVJGBkt6Gbc1IbPs1hQRXvNox4kKQ7lysBCB1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسپید امشب با فروهر رفته تو استیج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80758" target="_blank">📅 21:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80756">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZsJskWOLuC_nNio6tUlcmknz2jr-Z49jn7fjqIjEBKCU7CzqrulFUKKBFAEE9C2PA58BUk7xAEGSz2Z38kk_95GvrwaPWPva2UepBCr3_L3EbdWC52k2SaocloJRZD-Sk8PmHoQcJ9rKgsEqEaFb-TwFBuawVIuPfJMZZ8zTMj2fYnmZCLUSWNkezX65-Booe24GkXcLoTBMWIMiRqgnui3c_UdCdGbXJcm1kT2-Ukuk2jM2KmMXEuYDM5f78OM8i2BwB_stipzDrwzWC9yxOK2i8fKH6QQwTGlW3A9wHJ_uPZ5TGZDFVUaCkHI_JuWtnewJTVChBwsMUQJTaUZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyMiD1zZN0pu1d426FPYktMNYV8NvzwyAJfNQbkUOm44N7d2pBHaA5xSRO_8MYnE0Mm9L44TGAob2Rd9KgkbVX-tPC5hwD4riZ8gvn-JwRdnD5aaCxIHo1ZsXzhua-oO33uQtCmFgKtz4spJaLOW21iOYBt-ztsmxIEmU_8Q1BSvrJJl6XNCZmYJ_TD8URr3UB0erXUx6HjWSI-id1pS2rbH8zbU4i4nISjMYbfHtOGRNrDhzQEB225fz71fGpXvNj_JnowuiF1Qf0a_abBRL9-6UIyB44Ksz-qTryM0prjiTllBLSrZh7fdp38pV69-hqYF3b6Tz1j-UBOBw2mUUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنده توپ طلارو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80756" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80755">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgkM-WbQEuTZp2xAQ2ljDfJdNA2fEcoxc2hcYUn9mYKup0yTogr6Or59BejPwRMik4bJ_As3vR2SProLJRH8lr7FQ8kCRNJfDcmnrRrPQovypv3cEhcTRMD7NylcUC32C6_OVbS7NHNZ5dnr7maRnT-MmdlNW98kKlZCJRBx1ClbkiDSjEPQx5O4-Z1zOAYvu4Sl4KoMLQai3SZ_jQyDoq8at9Cl-9m2OVSkw86xoaCbwhGTaO1I22plCyFI1FTB1rKKp13jzUoz_S3o1qsriYj48pt7PoTBjUgNst1m-5iAyx5d07VqC5BmLBE7jfkwwey9KA2Yd5yxXYIXX-QOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
🏆
فینال جام جهانی ۲۰۲۶
🏆
🕔
یکشنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در مرحله نیمه‌نهایی با یک نمایش مقتدرانه، با نتیجه دو بر صفر فرانسه را شکست داد.
- آرژانتین نیز در مرحله نیمه‌نهایی، در دیداری دراماتیک، شکست را با پیروزی ۲ بر ۱ مقابل انگلیس عوض کرد.
- برنده این دیدار، جام جهانی را بالای سر خواهد برد.
- آرژانتین در مسیر رسیدن به فینال نمایش‌های درخشانی ارائه کرده است، اما با توجه به ثبات و قدرت لاروخا، قهرمانی اسپانیا منطقی‌ترین گزینه است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g28
💻
@BetForward</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80755" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80754">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYnlFnLBrGmMkvCVmVhKIw9fRKaTBtz2lfJIDhouhvt66RMeDBTvky-NMjx2MIcXX-Fy_-sLKWlg4QxzdyxZ3wbTnhrjZEh6WWeL6KwIwxkPU0yG7jWxP4vLeayeHPME2jcacPL0hpDfgMXBzWSt-RFVyVCD7SfSG3XUCa7ifOfPFKgOYzxfsCwaraOtZEnTRV5JHKX-NT_koHiwIW-sTxkVFIRJz3EGBxaegS6fbGiBWGhKZCW5G26BJ9aaKxHTOtZvB8Uw3nBvagbBMY0p26TioAOaEK2ywJ5MYRsE8GUsYPQleJmg5qBslzQAUE62PYNkG3kLnKio1sXEFOS1iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مامان کریس جنر فوت شده بعد کیم کارداشیان اومده عکس پاهاشون رو گذاشته و میگه مامان بزرگم دوست داشت همه‌ی دنیا بدونن که پوست پاهاش جوون مونده.
پای مامان بزرگه MJ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80754" target="_blank">📅 21:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PniwEJekGPid_y6YrI_xNyIpDYd9LfiRmphvXHKkL5i-kwCEDzGyxwXiT1_XdXfVcuErECK8xDl7OpVuoGcGoo7uU86hWcpliYj-LmMQL9H_ctsvCiRO451nOwvenY6sQmhKGCy2g7v2_UjR6TiupdB6_a1e0Dax66fFawChQ-jJL-vUDAdEgkTbUwG-kFxUIvb1aJ7eZsyzysAmnXnk-0pvrJmNI3Y-uBA5kCfKHg7vMAH39jM6O68nE1rl4IXrjyzfEbhcVz4xltiGwOSdTnqndKudLABBk28bMgR5jBvFKYCF3lTJ9EXgrXLs7MCPIhG6YfWibsHYSAe4NG5HhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمت گرم این فینال رو هم برامون در بیار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80753" target="_blank">📅 21:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80751">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-poll">
<h4>📊 کی میبره؟</h4>
<ul>
<li>✓ پرتغال</li>
<li>✓ مکزیک</li>
</ul>
</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80751" target="_blank">📅 21:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80750">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJFDHa__xEPW8OuXyiT0K1MYuodX3dCv5bICx4ZKUm7GpQ7iRfAoKf-4kP3H3lu2LnzGbiHROsvz2VZwDOJmSzbl2Rvu3WEFKPBtc0i6AadqNlIxgoE5t6cOLX0c_XVOCA4GMlnUWzR-2R2QOAoYRtymQaGf4Y8AUAxWFCPxs_HuwUqw3DxGG7KFe5JfE7suruyGrl4oWwhltnkmioRAaDMbqVTOsqv5sAVRIJfhNGEXYO5DZ_PO3XxU4cj4inlWnBSefYtE56CxQfYsx2162x8SpQvAp9GKBkrZOLQGljyhO4qSxGN5nGXUz-l_ZcRtl-eQm-Cix06o_SO1cZQLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست رونالدینیو
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80750" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80749">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره  تا آخرین روز جام نگرانی و استرس داری  ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80749" target="_blank">📅 21:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80748">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره
تا آخرین روز جام نگرانی و استرس داری
ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/80748" target="_blank">📅 20:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80746">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">و رسیدیم به آخرین بازی مسی تو جام جهانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/80746" target="_blank">📅 20:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80745">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtzrx6EhKzRsd8sO1bM6QJdWJwn-fxxMtFyGvB2ae5JEDIVwy_ln-0txQapia4vvdu5Sx28kJLdFeMOntHZk8cDlMZOSMSCSAPb2b8oFIKU83tMssYy4KeGQc4aTh1jSUy9anfKQD5qAcpg4Y3TZlRKOyO-yLnstvYhuGX_ZlCgvxLwFsmiEJhJ-8DH0fZuxm1zMWPAGlWDNS2i2KjtG5YwbEYb2Mx3XAo-KulLwFCHPkHVNSqgeVt-Tnr7cxx5bmMwQ7zNCNVUDlZozbwVTFZ7lisMVJofACwBMimxAmGJLhOt_ACG2Mz25ZagKtr0TWrPa6vl9c4EbhFDLZ1k4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری فران از فناشون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80745" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80744">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترکیب دو تیم   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80744" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
