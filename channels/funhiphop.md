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
<img src="https://cdn4.telesco.pe/file/jThnqugnP8x18RGiS_zkUPZ-CIXnZyJ5E0U1Ttm48i-IQSMFu9UTNoprDPgFhFvFrJW2CuEQiun-GUIwGaGS38Bzi0MsWxFX8kPjukh8hYGWYkndBBDj261BmquOY7_OIpigXFxCDbMw1YbNlu-fGZN_yoy3Mf0zWgx-09ZTkKmRmhXVOeNPJ-CePag0DP-GSmC7E1PG5ifMJeQIbIpESvkN8wO7kS97XQ_tLiYewIJlRI6I06LbAfUendvENfNZDtpVHhnpHlW8L3m9o8mVjCX2rO8I8pCeKnn6rS8BFOu3lZaQz1AgDscaBFr1vNWncuXjpEhrbRv9H_HqGBbANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 23:39:52</div>
<hr>

<div class="tg-post" id="msg-78415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هوادارای بلژیک ممه هارو انداختن بیرون
😂
Download</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/funhiphop/78415" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQSyDIX-MGij956PvVtDsy4w6BwlSmd1nBKMhc1ADQ7xKWLJ0YssJQ_we5_pTsdPmPmEheEkvM94F8cGrl5Ktu2pDxx-n4J-IHW5YkIjabl5hkX9RoSDPcrGu0XaHUbUZPP4acmzz5HpzFac5lIGPP_1FCf9Q4LQdyGII0HQB-nSOXO6hY9uwOVseWGVk00obyZ4NlHBA2bSZmmSQMXMz2CZKOnLnfBQKLgq0XoLtsIJsmGEHoh5_lZf9pFeujqjdwNEJK4aEXJ2TZ-wcv8CTkHqNRcQQgwsFzF2GIr0h-HyDd68V6s3Qdcv_pTdwZ1qGxKkry2-JfHocCcSxIOxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر تماشاگر ایرانی
رشید مظاهری کجاست؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/78414" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/78412" target="_blank">📅 23:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دیبروینه سوپرگل میزنه و بلژیک میبره
بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/78410" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عباس قانع راجب شیر و خورشید: پرچماشون فیک باشه ولی دلشون با تیم ملی باشه اوکیه</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/funhiphop/78407" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/funhiphop/78406" target="_blank">📅 23:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">من کاملا فوتبالی از این تیم کیری بدم میاد</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/funhiphop/78404" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78403">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/78403" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آفساید شه کون میدم   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/78399" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آفساید شه کون میدم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/funhiphop/78397" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/funhiphop/78392" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/78390" target="_blank">📅 22:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78385">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بیرانوند همانند شهید تنگسیری ایستادگی کرد تا تنگه رو بسته نگه داره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/funhiphop/78385" target="_blank">📅 22:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بازی تیم مردمی بلژیک هم شروع شد
ببینیم چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/78382" target="_blank">📅 22:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو:
سال‌ها به ما می‌گفتند"نمی‌توانید به خاک ایران حمله کنید."
بله، می‌توانید عملیات‌های موساد انجام دهید. «ما هم عملیات‌های زیادی انجام دادیم، من هم تعداد زیادی را تایید کردم.» اما نمی‌توانید نیروی نظامی‌مان را به ایران بفرستید.
ما این را تغییر دادیم، ما خلبان‌های شجاع‌مان را به آسمان‌های ایران فرستادیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/78381" target="_blank">📅 22:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
رفقاااا نیم ساعت دیگه فوتبال ایران تو جام جهانی شروع میشه اگه میخوای بدون سانسور بازی ایران ، و دافای ایرانی تو ورزشگاه رو رو ببینی چنل فوتبالیمون بجوین عشق داداش که چاشنی جام جهانی همینجاس :  • @TrollSporte • @TrollSporte</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/funhiphop/78380" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddRwf2Bi0olF518yDfe0jwPd0VnHluOetZ9MX-0KPJvOotzt7eS9L4y2uUabVTyUYtmYaYQHFVr9XlUZ3b9Nnn55hC9E35ESxs7cAHPhXLwT7CmfCsTYY61n_ojT6e0Z7SMqqHfz-pFI2Xnd9cdbiU_3m7_dhu-Lo9BSyp941ajfEOTf0pUYs5CHH0Js71T9Ncnq5fkL5CHKR5Q-2I2pCmpZ633mDWzokS2jEkWXrKwzPK2fFHo30msdSYIV3BgDI_iso07zHgHF_smY5XEQZHG5Qmib_v9eS_RPIKSYKPM7gTbyqCuJqn9hCaXjKo91gtjFjM7SqVnSjDtKbvxnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رفقاااا نیم ساعت دیگه فوتبال ایران تو جام جهانی شروع میشه اگه میخوای بدون سانسور بازی ایران ، و دافای ایرانی تو ورزشگاه رو رو ببینی چنل فوتبالیمون بجوین عشق داداش که چاشنی جام جهانی همینجاس :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/78378" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzI61nHuUPbY1w0ZrDcACknVqNEVw12so70EA9bwvin990PBk9zCDoT3W7qSWHmQldMy_Nq5OwG_inBpKw0CdObd__OP_8L7RkSxc7BdLBCp5Q8czAosCkET1ZoSqY8KqQev-DE7SAuSozY3c_ptDgODLdKw5AwAMqLwvBHgN_CUAb4ZR1HI45XlOwXSFHhRKBblfvvNeU42Lw5DTHQUki_Fv_dZJdY0z4GzINL8nXFOG5bMTWeaVr0WJPanBr-FTkGcTekiEgP4QP_fq1gpJZOoC_ZP-OlIizlZ-4EXrYgZFJaVTNkUh37KhvjcnuEhY_fxgwDDOPpApp84uO58EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/78377" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رو برد مساوی ایران بزنید پولدار شید</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/78376" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5sZ5Qn9wOzJA2flSvYZxFSC8qotPGo6BguL72_1n8eXwGbNoyBE6vAb_vki5WptDSQ6beSLScezkOnX-D9v26xN1CnHNrt8E_bCan3J2OPR_OulRWqLdIDjftZmyybRQBYNBYn2hWt2bVmeN_UOEzUMcjdshyP7qybpJ0v-t8Y3rgNklXBRh9I_7znM85v7fD3EZ_jOzLAgdM4snkeIomRQseN1fjW6AoMy-znw6kicAv4dCkNmDYVkf0G2UAaVOwKIh-SGsHETGbn_Dy3Mm9r8Alc5oHyCjg2DSZbpFvyDmo6uRHPyd16GuJxwYH00XU9Zt4vEaYAh9RuYPyJzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال کاملا حجومی چیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/funhiphop/78375" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امضا میکنم که نعمتی امشب بهترین بازیکن از نظر ما میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/78373" target="_blank">📅 21:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZLwOCQ5ch74dtv5uPyeEvaE_pzwI20wY8Sjn3DbHW0U0ASxY8ZY4hsVHcygm-PdRcaN3a2o7NSReBXK9Bw0mQ17xR6IdnBOC9C4R1fDDgfVNqkB2NkCDORrTQDGsn_Rh8fpq0niz1CQ8F5bB0Y8m00wLLW9k_fSVVbBtK9xEAz6XyE_PfsEBJzH496cFY3GPrlVogEg0W8eVopsPNg0-qhlQJ2n3H5ElodTpGEfz-zh6-1olikmnK0d5taT-imgXD6CeG1KwGaoTK49MUuQ1GN1nNynPkod1bZTRikfWQWbWlMnJzxnT8tUPksUdFuFW5Wwvylwq7w-eSxtySvI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب مادرجنده ها اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/78372" target="_blank">📅 21:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW6MtQ3YSJXBaS0yZT1r18BFys9q1XXc30Z9ADq29z_NGb_Dx7uYJ4bK2CA0vqwSyuyy1G9cSj-3lCHx5k-mCiDVJS8khaMb9oaJyL-PHdykzDy4FmwPWEHExhFxpjir4hlX5DgR1aSIoqFWh10wW2cS2ZUbSkjml-lFPwipq928dwyTkrxRUDoEqYu0Wxx_CFXifujXuFCtXqcb2tkseMCI-CzJRJbsgGvY0cYdytesVukMzQNJmtVpu0sSc7Nf3tTybOuvXPA2JbTXU0r0T9Xf9LuLtcaiwlD7SCKK6goxZm0UzH5y0QaOlcw3kV3Ycjcyi7V0wJD-z1gv60Thbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم ۴۰۵
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/78371" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=gl3QhxYJlK-faJbT19ncUjOd9uN55zMRjjjiGEbjBobEex0n1VjtkSvLx07UTRgU-hKQ7PKLRn7v179ilLJtBuKf3n9jVhNZoEl1sPPI1JPRCcL_nmenqLvSzESpALjTfzHHnR8Kijq6R1je2Kh1mthd7XdXAEFI5--s2PaHvPmagS-_KFuPqcOxdJHwFAOOJCS3cVFQ35fsoHFVPRv3xc6PV75PEaHC7L1KybvXmPZ8PNwgktsvJrnXvzbgoM5UcC6MLLmm_1JfzY7d9QxDD_JBarVSr3-j-4Q2BWytWUdMXRwMO2uztbTMOTLeju3c_lwtiEjGKZBTmon19krJGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=gl3QhxYJlK-faJbT19ncUjOd9uN55zMRjjjiGEbjBobEex0n1VjtkSvLx07UTRgU-hKQ7PKLRn7v179ilLJtBuKf3n9jVhNZoEl1sPPI1JPRCcL_nmenqLvSzESpALjTfzHHnR8Kijq6R1je2Kh1mthd7XdXAEFI5--s2PaHvPmagS-_KFuPqcOxdJHwFAOOJCS3cVFQ35fsoHFVPRv3xc6PV75PEaHC7L1KybvXmPZ8PNwgktsvJrnXvzbgoM5UcC6MLLmm_1JfzY7d9QxDD_JBarVSr3-j-4Q2BWytWUdMXRwMO2uztbTMOTLeju3c_lwtiEjGKZBTmon19krJGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی رو برد یه تیم میبنده
بازیکنای تیم مقابل روز مسابقه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/78370" target="_blank">📅 20:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ریدم قالیباف: تهدید های ترامپ بکیرمونم نیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/78368" target="_blank">📅 20:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اویارزابال هم که به یامال  ایرانی پاس گل داد اصالتا اهل هراته و ریشه ی ایران باستان داره
هرات استان خونی خاکی ماست و به زودی به خاک مقدس ایران برمیگرده مثل اربیل و سلیمانیه و …
دو ایرانی اصیل کارو برای اسپانیایی های آریایی درآوردن
برادر برای برادر
❤️</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/78367" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آرژانتین به عربستان باخت و قهرمان شد
ولی اسپانیا داره به عربستان تجاوز میکنه
ینی قهرمانی اسپانیا منتفی شد ؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/78365" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مهد اسلام داره فرو میپاشه</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/78363" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMqSQE8jleRK93j0U4lU8uvn_jz-_dj32tkfTcKsdKA9ElLKZh3-r2m0Fa-6L3KUwaY-pzdkQyYVDNoEEGvPTRi1jhQfctasv1jlA7oMzQyJhQkWTHib7AKsL25v7_UF790UNijV4Zqid_abddEkKZSb90Y2IyTCuv6whgX3iquOeaaEwFDYSj_FuCyLPCFHD8Z29hmYPmo_pAskGwuqytGSXtZWK2FH85eeqR28o248r1DuKNtUXaqC9S2DgVIluGd0-aH1zs1C4bKkz0OCB7OxfICsPttvnnazAIEFtD8NTCk4FPn5Fcn80eLc50H--ZlGwbU78kS9UW52EVyPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
قالیباف: تهدید های ترامپ بکیرمونم نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/78362" target="_blank">📅 19:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو: تا هرزمان که لازم باشه برای حفظ شمال اسرائیل توی منطقه(جنوب لبنان) میمونیم و همچنین اجازه نمیدم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه.
ما از جنوب لبنان عقب نشینی نخواهیم کرد و هیچکس نمیتونه اینو تغییر بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/78359" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
عباس بیا بگو چیکار کردی چه سوپرایزی برامون داری از مذاکرات
ترامپ به فاکس نیوز:
شاید کنترل تنگه هرمز را بدست بیاوریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/78358" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کونکشا دیگه زمستونم که مدرسه و دانشگاه نرفتید، دیگه دلیلتون برا تابستون فن بودن چیه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/78357" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اووووو رامین رضاییان
🗣
🗣</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/78356" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQRvw4HWYRAIsxHzr4uG8N-j-l9jY8xl4jAk-SheRhst_cw3wBBtTtcLgvXpwQSjUtIUU4Fx2Cv9XRC6v1-8YUZWvL0ozDOPQF9EQEM2iQppyLjGduTSzRj4bBLHleXoWOJj48VNpS3ODyeRj1mA69gYNLPqryzGrGctVj6E0slK5Oxb50NsdxkLvscbx90x3EMOnkzZvfaW9Uie4Hj4JwLorSOPKDkXLwd8yuwzac3t8dgGHAsoumWohz-nLav5h9DKFVe5i5AVabYFnCMlLENIpMQVAV-dYVOTBq_JrOKt10xF95Sw_jj0Xey502V1H1pEAIuboE28lNBGcoHRgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در بازی آمریکا و استرالیا
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/78355" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/78354" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYEflhn_cIlW8tSnrrzqr6lFsIg6gcz8TDAQBsdrfzW3RfJjMRoOxOCho63IJw2Qd25o_GH0qGse0YtD29C0ouSmExssdpkJyCP_2GAV3aqoo5YM3XhdHJ7SJFQXyK03wmshpbTr5LoF_k9_Wr4zaFcC2vqdP_7WlvMydXtFKyV-GeNtmYVcCgY63xsCqfeMDC3ABS4j9Tw_aFVACgISlK22MN0AHFB14jajC0ntN7lMdf-EwBZqDoZMT54z2uFW9cIyQPstRr8QIrx7Z4FaRYqi4ijMAqjUcUd7UoAEvgfHQSidJ0x5cpOQW7evgusoPq7003XzTafaiiKUmNEw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
🅰
g31
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/78353" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تحلیل فوتبال با سامان ویلسون مثل تحلیل سیاست آمریکا با مرادویسیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/78352" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مطمئنم که سر مهریه به توافق نمیرسن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/78351" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:
به مذاکره‌کنندگان ایرانی در سوئیس گفتم اگر تنگه هرمز را ببندید ما بقیه کشورتان را هم تصرف خواهیم کرد و حتی کشوری نخواهید داشت که بتوانید به آن برگردید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78350" target="_blank">📅 17:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78349" target="_blank">📅 17:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91dac02670.mp4?token=QmCMbXL5V1X9qnfb2Qcvrt2P1Ugh5II6ZmbyemN8n203hLmqXEUXL-z3O6RwEz2T6F5R8OYPwLK-G7Wl8U4Ul-y7tUIaoRzyKb87JiAZOYuOC3BFmD6YZojfz32ZvtYXZf88TV-JgxQVL_he4pLTP-Jb-51la-bdjF13WCrzerq7lKhaH0jpQEKZ7UzLl-R6hAyjoZCXcHD1_-UXRRzDL9oAJRzWwPbYF0cD2mL0SChkByTpEfhgixps536pOdGDHxxFFnCjsR2HRkNeiS1thvNGrr26x8rCRjqhd_aQbGB7L6MZu_mdshMh0rzE6e-oehryoRfDuzM_SjzOjVrO1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91dac02670.mp4?token=QmCMbXL5V1X9qnfb2Qcvrt2P1Ugh5II6ZmbyemN8n203hLmqXEUXL-z3O6RwEz2T6F5R8OYPwLK-G7Wl8U4Ul-y7tUIaoRzyKb87JiAZOYuOC3BFmD6YZojfz32ZvtYXZf88TV-JgxQVL_he4pLTP-Jb-51la-bdjF13WCrzerq7lKhaH0jpQEKZ7UzLl-R6hAyjoZCXcHD1_-UXRRzDL9oAJRzWwPbYF0cD2mL0SChkByTpEfhgixps536pOdGDHxxFFnCjsR2HRkNeiS1thvNGrr26x8rCRjqhd_aQbGB7L6MZu_mdshMh0rzE6e-oehryoRfDuzM_SjzOjVrO1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس یجوری نگاه میکنه انگار اومده قرار دعوا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78348" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دیت جمهوری اسلامی و امریکا شروع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/78347" target="_blank">📅 17:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:
جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78346" target="_blank">📅 17:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVlHci3M0elQACSqjHricvKIf8B9RK7A3_fhI1dcpDDaPy5tBiXim3kpnXv7MQEmc0Wr9gJO4B8sNH7GtJzLNHp9uuCbwqtqLGA-nm36oJQEJ2wTOCDNU2xiRUtjBf494ERPInc-7JFOBkGgYG1Ozn2vM_51eY3n19PXOQY2phC6RO4RrbZZlhj_N_NlUSlVg2qESilZAaS5DoSW4j7utGuLeWqJn-UgvRI-nSYjGfkePQB0Vi0SKFcAG9PWtjq8TyX7Ipr9tkHgsU_hCoV-nsyWs21qrubZQHdmi8UoETQASg5T4mSvaBDkW0gCVRJlCpdDkapRwinqN4Jx2CSveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78345" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عباس دهنت سرویس سوئیس هم بگا دادی اخرش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78344" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=tIzZ6KFojpnLEJ1VAj-0bOmdcjlNGhUt9j5esKhzwTQGouYO2L7d6xVgpUzDrkGTMbUAqiR5mbD80fPL9RU39OpDhdyzt6HC8zwVyVGOjsDgjmmm8HE8-CNajckzffzpsaFtf4iWetKuzlGnCIl9e2UkXcVq78W-Q-h8QHfNj8UnOmegZQK_ujo6aVjXd6dNDZVr0DJBKLmT35BG9WXSPcWydMIqvLXDQ3lGu4NzxxZQa7NtHfj9Wq0T-kQQU2FGh5IaERTHbXPLBo5-28vLQApNFbf0-5kM8y6bhmUiHyOYwtVh3NgrPqU7Yw1j1UvscYOSPX2NTfEjaE51Y4BQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=tIzZ6KFojpnLEJ1VAj-0bOmdcjlNGhUt9j5esKhzwTQGouYO2L7d6xVgpUzDrkGTMbUAqiR5mbD80fPL9RU39OpDhdyzt6HC8zwVyVGOjsDgjmmm8HE8-CNajckzffzpsaFtf4iWetKuzlGnCIl9e2UkXcVq78W-Q-h8QHfNj8UnOmegZQK_ujo6aVjXd6dNDZVr0DJBKLmT35BG9WXSPcWydMIqvLXDQ3lGu4NzxxZQa7NtHfj9Wq0T-kQQU2FGh5IaERTHbXPLBo5-28vLQApNFbf0-5kM8y6bhmUiHyOYwtVh3NgrPqU7Yw1j1UvscYOSPX2NTfEjaE51Y4BQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوفون و نویر وقتی میبینن نیاز نبوده ۲۰ سال کون خودشونو پاره کنن و چارتا سیو جام جهانی کافی بوده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78343" target="_blank">📅 16:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پزشکیان:
نگرانم مردم ناراضی به خیابان بیان و اعتراض کنن. اون وقت ابهت ما فرو می‌ریزه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78341" target="_blank">📅 15:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگه برزیل با درخشش کونیا میتونه ۳.۰ ببره ما چرا با وجود اینهمه کونی و مادرجنده نمیتونیم کاری کنیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78340" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پزشکیان:
توافق رو گردن من نندازید، تمام فرمانده‌هان قرارگاه، سپاه، ارتش و امنیت در جلسه شورای امنیت ملی با توافق موافق بودن.
دیس به مجتبی خامنه ای؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78339" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان یه نکته ای بگم
مجتبی خامنه ای طبق بیانیه ای که داد گفت به اصرار پزشکیان این تفاهم نامه رو قبول کردم
نکته ای که وجود داره اینه که حکومت اگه یک درصد امیدوار بود که این مذاکرات نتیجه مثبتی براشون به همراه داره به هیچ وجه اعتبارش رو به پزشکیان نمیدادن
پس نتیجه میگیریم که این مذاکرات صرفا برای وقت خریدن هست نه توافق قطعی
ممنون از توجه شما به این موضوع
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78336" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مذاکرات تو سوئیس شرو شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78335" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه رپرایی با معروفیت کیرگوزی میکنن که سر جم ۵۰ هزار نفر نمیشناسنشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78334" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن    @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78333" target="_blank">📅 14:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ولی خب اسپانیا چون تجربه ندارن قهرمان نمیشهط آرژانتینم چون بیش از حد تجربه دارن(پیرن) نمیشه، تنها تیم معتدل انگلیسه که اونم لوزره</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78332" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هلند بوی دوباره کیر شدن تو فینال توسط اسپانیا میده</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78331" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ژنرال شماره دعانویستو بفرس
تروساد هم از ناحیه کتف بگا رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78330" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78329" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0Z4Ia0mBFbQoU4BiQIRct01srBKVsqlitBO3qVZB4hiBShUNJkymcEUIpySr8ACfyZsI0lKmyx4vR-MXYwhGqXP6cid_VFtx8lkXZs-3vQfdORlB5YvCuNMe3YkXByw7GL9L9oHZ1UELTOI3L5Qk2KSGelcMAUofxZFmaJ2QLURN7dM82_TwtCihDeBMAsXNxtu1I_P3hojfDNwofObkMSqiT7VBDzJfaY0CaW74kJN7NdCbq5hzuClcq69-1zMYZXlmD1jiTIHqaJ5-KWdOCOn_WZRTUje0S8Uf_d9znUGYWpga1C3uRsV-STRNyw4ug6PawTkKKBtvhXNupVhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم یکی از پر افتخارترین تیم های آسیا در بازی دیشب
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78328" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mupVnaddIFVAJ16xSw9fZG13oyg3YGLXrraekOHbCekSm8R1EvAuT05FLeW0vdwH40bOoTEnADBh2HWXAzjgsPoLCeykzdOVtCh6zqD861_GlhXjfuPA9HxT-PDGL3_0RxaNfQPUWbXyML3X64Fmr8WO3jebpvtPBGwkIJGq4rxUipTR77b995ZaI17-e0EiOJSrcnboqf9qt07qWVjfxiQvij16A4b5MNkCxi7HDbBS_XjX_3TVHGTt8IfdZmtF3Ajy-RA8xbfkSPnuYKvYNt4E52iBLkUqiMtzcsfVUZfJwQBctMPtIMx0AO_2dp6wKtQ93sblScSEcVcnZa065A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال توی یک تاکتیک پیشرفته رفته عکس بازیکنای بلژیک رو زده روی دیوار بازیکن های تیم ملی تا امشب بازیکنا تو زمین نتزسن.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78327" target="_blank">📅 11:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD5x86Kt2QUPg7j0zd7AYTkaFfvRoBXRELwG_OxowPidfAzzmCrPpTlQnT3LjpDtluD3E-_dOr0M_Eo6iiqlPRefdaKpJZX-VtnetPoFGQKFOlSGqO0zkhPD128eC5EjrHvX_QqQjedezDcm0GSwgHJLPako3bL2yTc_VA4QtB7eY3jF9j4jC0rKh3JkT38WIg9UNgdmPabRWp7_iLfJWulFHR3JmG7r8JbR6e84AfTwxOAniad4BUUeQrh1f9ybpMAgkCLZmw-Sicd5AVat1kdcgYmCT4Or0L0LsgxfgG-IOnt_ovW8pPM_4_2QrTwhPwu1u8FW9N8-BK4KFf0EVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم رونالدو از مسی بهتره، چون ممه های زنش بزرگترن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78326" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78325" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE_ZVdfveaVPY5mUWbQoxVZRchNJZ-BiuQObXuyfMlqUe8IPrLkmunlWYML3w2bR85q4YKrCEP1i1bJeNmF0mBKtDGq7wqR-YzhDI23r_KrkP47l_X3F_zZ8aPguNyG7r0dpMWD7NLFebb4jMjEH9L7D0INGPkvNcZ-TbDLF6GtL_J_cDU3ORNQSmBHo9JIKUqgAsSiLtHev0U5Sm9hLJJJWxseOeedUqt7H5GrzAIKITR8VZHUAWXF_gUcKdq7afrvuRFgT3z7KRI5AEk3ae-t8v19S2kjMmgC25XkNy2kbZ6nfOTw_BWz2DNOuNoa77Cm_Xb_YQ6URFU-cvSDR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهاد ویژه فقط برای بازی ایران
🇮🇷
- بلژیک
🇧🇪
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل مبلغ شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
R31
🅰
❤️
Winro
هوشمندانه بازی کن، برنده شو
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78324" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کارتون فوتبالیستا تازه داره رو ژاپن تاثیر میزاره</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78323" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این چرا جهانی شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78322" target="_blank">📅 09:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFRoLXNGSX2yZ32Svrh7mFGDhJb9brk2oQizSYckts9w0Xn0tb9m-nYiWWizkZtI8T3rsnIWV0jMi7hMXKVmuZsOMLfc0EjAbpWqg0FtujUahNBs3yG8Xq-nkUpToTKWbjlcltFGaATWLwid0txZRkGH1RTOz_h4PvGswd75lTDMAkpkxq66l1H3GrDFxYqVTs0Zhjz_iGw-K6RhH5OjM6KeG9nr_LWYFSbZ2qVgQOtSP4uY2_M4dfY2sLumLjHo0r5ZAr3zXVmMZ5AUUGukISO8S3U0KAZyXwmv1INt7t5c03VTtzum8lIhViuBszCtMUL9C2DrYHMT28maoDs8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چرا جهانی شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78321" target="_blank">📅 08:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عباسشون رسیدن سوییسا  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78320" target="_blank">📅 07:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0Jksk0Qif1n-DjasHaAFCQRiAIKA7GYgfcmcmCHR0KTzo8HMU7dZUkyn2IGcjq6M-JNyE7NRTXYr-3QYkh05t_NH1Jx8rzld2It14TsqUWi0t4FK5L-9Yr1uKbfQd7OIF-8jAknwkYZH_nJod9w73j0WwnXD_0bVJmObh-qpjhWtxipEtTB0n0566QXvUioK6hrX1HTIGJ9wwobnrXUCIQX7Gs8AYoOZ7qUb6h0LVc8lRXVkyozIYgiAst3eDb6dhOcNb-ROlv4msrHJTs1oq-UgOXXIsAdiaz-S3VtzkVQvN9nGTW8WMBnumXIVeuts7IclQbT9gk8i3eLxdCImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان ارتش اسرائیل یکی از گسترده ترین تونل های حزب الله رو کشف کرده که پول من و شما ده ها سال صرف ساختنش شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78318" target="_blank">📅 02:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCAdCvjMo4xq8kK7hkhbz7-tgRBVDt-k4zk3r8ob43rx3zcwuTIYj64VgMf0Z3qwPxPKC9uMTgZKGuAPIcCjyJR6KC1I7JiZuhYbpXL7XzThF4wfzbM6SSFa3NjRBKacq1CxgXurEBys02_isUaYX5HPTiLAZfejIG8k4wZETaqogibANdWo12IatmFVvjMX20WfBHuPNP0s1_cIa-JAc4fs7tsyODPM6JcMm-peVq6bgQGxeCSBpZ5pfEeBOau46Xsms7D0xJ1oGddsZ5ssQ2jmqgwDjcY9Ljn7A2W5Zk9n57YBjlGnA4RLJ15mdxpFVcss3IRaOsdfMAH1uj-3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Iranian power
❤️
👌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78317" target="_blank">📅 01:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حالا جدا از شوخی ترکیه خیلی به کرداشون ظلم میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78316" target="_blank">📅 01:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUP_Pw-jUNSGuRS3jU8sxuDILRGzf2mVotFSr1AaFA5gZX2kXj6_p-k7AiP3Wp8OZ_qDW8ll_9ZWpT6FdcXAW_fWPfij_amOEgYgK768g99KLaua_AbAoJBxsOGTvT-FINgZk2Bw-rKzWATRvrwew4oNDjU_nFUE054lreayDheww_fL1uxZC43ra0B9frJuzDo8CyOU07qHE0uTWulWGCBJxgzpf0cmThkQM0qyCi_9kxZ7asNf3id-7ijGEkjAdqUR7I4RVaH0VT1Ia6A8Q6b3zMzt9XIe0XpIiutsDe5M1QXOQlS4G3G3CBcPINTZxxdOi3w-9iU3Xw7zx9P21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴ کامبک تکمیل شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78315" target="_blank">📅 01:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه طهلیل بریم
آخرین بار ک آلمان به مرحله حذفی صعود کرده بود قهرمان شد
پس این سری هم قهرمان میشن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78314" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴
کامبک تکمیل شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78313" target="_blank">📅 01:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRZU6VBXrzvgFjmQZFM66rQL3VWox71997M1WtghKFjs5tcxvlfDyyFOugj3CnWBdaHK8xTVWHoZGegAHcPX1qm7h2sYsGq1jFZqgYTqZk0hZuh2U07RX3qkjuABIg2u89qY5B3I8wL4HD3FyWuWc69Rlfbxl3kEsuey7ENMvAO4muCHtgmROIVcsbPDDUrMtFMzIhGyax6k28iaYBIpVuygKwQ7QgcFOVgyT5J8p2QSBl8feZ9Viz8LJ14Elv8zPO3iJkqTRNHmvBX6kYDvrt-cj1xUn7VaCRDRNavR0ziQJnZqsQuOvESRqffrcJMP2eX_sI-WG-X3rXBTfO4kOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرینات قلعه نویی قبل بازی با بلژیک؛ رسانه های بلژیکی میگن لوکاکو هم از لیست بازی فردا خط خورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78312" target="_blank">📅 01:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آلمان تیم خوبیه ولی مثل تیمی ک اومده جام ببره بازی نمیکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78311" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آلمان اگه این بازی رو برینه عطشش برای ادامه تورنمت خیلی بیشتر میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78310" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فوتموب باعث میشه گل زدن تیما برام اسپویل شه، لذتشونو گرفته لعنتی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78309" target="_blank">📅 01:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78308" target="_blank">📅 00:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عباسشون رسیدن سوییسا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78307" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کیر نخست وزیر بریتانیا استعفا داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78306" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دوکو به دلیل عفونت تنفسی، رسما بازی مقابل ایران رو از دست داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78305" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">المان خورد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78304" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هلند تو این تورنمت همه رو سوپرایز میکنه
یا با قهرمانی یا با حذف مدعی های اصلی
این پیام بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78303" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گل پنجم برای هلند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78302" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سوئد یکی از گل هارو جبران کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78301" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حساب کنید ژاپن چقد سوپره که ازین هلند مساوی گرفت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78300" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله اکبر گل چهارم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78299" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گل سوم برای هلند
سوئد پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78298" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلر هلند عالی بوده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78297" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سوئد زد ولی رد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78296" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسرائیل آتش بس لبنانو که پذیرفت الان شروع کرده غزه رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78295" target="_blank">📅 20:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هلند گل دوم هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78294" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هلند گل اول رو زد به سوئد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78293" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzleW2nqmZXoK6zEb7IBM7b7jA_gQIlQdecy7kfRoJ2Sj7NeTRvkzjgkGw-MO17GSjO0vL115jiZXqZ5vUrveFnZsV-HtMKTbST8JA0oMkpImmkR5KqYfp0iEHBBwBKdAWu3pn25AApIPiPr6UFbgelH_QU8t_YQeKUdo66HEw-VNIhAj0TJ2KpKUaBpqqT0R2TMCVeOLS3cOzQJ49h87k8n657OhyJiF4gqX4LpOrd4sgKxvIHmFDUGypZQgy-kpYOoALAyRaFxAj8Ch17_eV5AFkdHBNScrHIwGGCyIOJGzQm33SSiBw-ytQ7iXRQ7QFwxjnZ4aVB7mi-l8S6iCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم با باخت امروز صبح از جام جهانی حذف شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78292" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNXIfQZQ9V0LJ9CP5YrqzAud4qyfOvyTPPPPuD-toaajeo58z5wSM3rRl2NF5fnjS5uNG380NrvBVcQMpA3Ap33jEWCeoO9-VK4cd2MsWsr2E539bngbRyU0cYGFxtnVcA5oQE2bTznepQMyiZPv8E-Op3g5KU86UR2-KJ_-CVBW48qPWzm6Jsp3RDr0xbAF2AxRwDxFuDxwXbakmgPuTFv2X9MrMElkra9FBtuJeZqVqgVe06GgGuQeDRDmaRZLiXRsOWucyczc_QB3yTwA4cBcwLIUd3Xe62ryyaHyJUyNv4vyzUjEjmVyWe4LBF_e7VLBI5Nk-GQwJSP_ws5Y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AevF0VJegeKgbydJJZMOPaiWpiGamAw2dnAhnfvLCNoPe-L_NYMmntSR3Li75exdZ5PFPlsuoYA0SPpfj5e9ruZXfeuU9dtXYI1SME1aYrN0VIKVE1IB08J2-IzfAvr72uzcoCfQkYsmOspfCdsoC5ZObFYtBAKQ9IifPk0QUbZw0nQW8Tid1gSVN7N22iwN4nVQnc5LqZL5ddRlkx3BVXZpZCngdDoxVgrLk6ppOfqVgwPTiRJM8FJCEIe0a9OpF1lYW7ApAWBkxgz7xPAhcCpk-v5626HTISurwlG_TUIrC26QOEWUlHBMlCb-MXTWg73VIhrHys-VIc2ocLyrzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78290" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4UjQTY0U7k0U-H0YQFTH8Xl9o7RQ3b4Le5M5fGyxOdBw-_HkuCbz3Gwz1KpGx6NTHjhtU_y3UnjqeDCqJuEAu3zkTPywNZH8GNfzLQ2MYajy7D9yPJgYwMG1j0KFnUhbkJiQd1K6YIfnZ_5boKGf7WB0qgf6GoA1CtdNnHimu9E54wuSd23YRAcC1GkI1Dvb_0N1fYjRWPxoefjf6Zh8m66xKo9B3IKX7rbdA1e1ZZWKJUw1vaCr0oinayWg11vBpFO7or59xiAjL56_x9iXeY6Y1HFvXR3HO2UYLIMwKICVyKSJuglWT8g6q6HJJvviHxlIi0MHaCTjJK78nHl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJW_qP3qJAVZ4SE6jP3rsMg4m-7mRH12gDe_K1fLqt4Plgjn9q58HLnOvLris-uxcuDzUfHI9OwouZNqV7V4ZGki8p-lwLAxIO63_eho4eTZPw9sb6plMnSqyEA0i0SgDw5Z0aYCrx7WdBzutGRdVnt_6LhG-hJGypqNXLdV_SmOIWvtke_wobdxS5WjFG93VaeLGfPMpHrtd7TDv11h75SNl84MvxSkTEHW2ep-ZK1oiFEtlB8RYQ1lLJioykRRwnM3KyFrKkgAq1QPPZ7Xv_GNv9ay2MHohO7tBgj2NkML64jD6YsupZabFhxeR-zNoBs1Wipee90hsBuMtr83yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78287" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvR8zv-IBWl0aNTZFJ3DaoeOqQ7QqYtYzPs5k-Kq_PdjcjQDEAh443OfrtX9-psqiers8atwSprCidUKKvnoqDci6Yydl5dN03aZ2RaJNnb-GOcn6yWhXx2PF2T92uoCIikzw1ZfVGVHA-Uhrvp9VWrl4ctKeA9XJARmutzv7tX-vokcE49rtnjd8VO6n-Fv6MswV9FDtlmY0wNjDhWZCqwgX9pTWS2fw8IHt1i5qdIPXDqGZ8WAYgtgOS2lhk4ccZQ58KwnsYWRDv74FIpr-lVK79-HQXTW-1hnXZW6R_sXNavSjCTqd7QlXI9v4XCUZMG7WbSn2mfTHU0hFhr0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
G30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGAjNeHV1mAirZXgNnqB-tjTylfN8C3b4BDhgTQJPiYpDFGbqaIhnEYsdxqC-ZRg2NolxT6JDExBbWw0dpdcEB1Gx7J5cWk6OE2ElvB8_LmPMSYJhsyfQch0pQytvqaKuOuQn1QeVhKbCpLqBdvHZ-ua99bKXBc0jQXAVCvuD2cdCn1-BmbxNhzMyqAemygq6bak4EY7maqhtgoKx4BkpbC7GaoWFYY1yiWZRglplNxjDVqfg2BAu0oo74W1QwpX8eDZDVH8V0XKr3UETUGEjDNCyIcT5BD0-Sv-thFkOSUmJW89pdRqRdSrWK8cCuTDh2pchtQ7z7O0G1g2qrfsaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKigD-UCuozxFDQs6zr8Wh4UTynYONEv3unAfNCCcSk8O81Mn99hwLWBy6JG7gCINToqzCwC-oOUCAHI5XtudwYagCEBae-HIxXvQJMYDQc4HG40kIVFrZ__-AJeHV5b0XDh1OS-jKCfBIQB_xyjaHsrsdHZv3yvXJ4zHqIA5oxg6f5UJdiZ14JzGKWJ8G_k-s-FbXoqtJAqhderHGEAu1pVec_MVYMDjWbplVEE9lFGZa6jMtxaFDpuLFxiVzugHoHehrfXM6lhAj2ncJg5fCOzu3BP6pWffE6c3evWJMcsiApkRVS0qNTehtZA_xNJrPlJjovUBco8OCvO2KaEIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
