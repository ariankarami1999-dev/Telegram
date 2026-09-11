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
<img src="https://cdn4.telesco.pe/file/PADA92dWzcoVkG2MMFL-kV6JCddL1Xa518iWoi1j6RWPNZE2nxq_1glLQdbswKQpVVr1zsxMhGh3FM5yeLd4wyn5rgSdeUJzeBOwYM-bt2AcCjpasmG9wKWIUUNN_JqD_volbI1ie6tqdafsE8tbndpDo_FGuEZFJey9BWOg74-_HP-prIWT-aBfl3mwbb7HVpZ1HWc61TeX8Fk2_1BZe7omBTtLp0dnLRHUQJLCIz_QDfFMCbOsF5_pd5vDU4ar4XDw3NTpAzIjFfBB1QaIXQgI256CWnIv-Jv_Kw6fmXI70J8viLFOMJnx1RgzH4pgFD5L0N_Z3aCpJgZbnNQjaQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 09:45:45</div>
<hr>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pEfshKPhUeOYiXOAoShl4NqZ-y81MO_Y7oUz0tkTOsUHPAoZ7e8bJiwiMnfBtHdgyKjjtMTmKvK5smoh8dQXAGwTnR_vfh8Od_uf4vv567qByA29yYujhMVaB-twQCBcyzmBYnhpNjiqFTIYTFkE3vna1svylgCQqUIWc_D4xxyKVq-PUtYkl3Ds4lTyKgndm4o85c_1TjaTfEBR_3IrLzVetbMdUyvsXRN8B-tN1HmNFCl-BClMGMo2PMJE5u_9jRpxeu8uxyQMZh1IxvSAA1cG-AgNAdCwaQ_SDADBFIHBos0Ejg_SBv7f0klamHqQIwk7iJUI42NMQTkWq7Nh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=pEfshKPhUeOYiXOAoShl4NqZ-y81MO_Y7oUz0tkTOsUHPAoZ7e8bJiwiMnfBtHdgyKjjtMTmKvK5smoh8dQXAGwTnR_vfh8Od_uf4vv567qByA29yYujhMVaB-twQCBcyzmBYnhpNjiqFTIYTFkE3vna1svylgCQqUIWc_D4xxyKVq-PUtYkl3Ds4lTyKgndm4o85c_1TjaTfEBR_3IrLzVetbMdUyvsXRN8B-tN1HmNFCl-BClMGMo2PMJE5u_9jRpxeu8uxyQMZh1IxvSAA1cG-AgNAdCwaQ_SDADBFIHBos0Ejg_SBv7f0klamHqQIwk7iJUI42NMQTkWq7Nh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZbeoRQ1rpl74-annyCplLOeMaaQm9FbkOfph933nQ05me9RghIF3WzF-CN-CUrKvrADxZ1eB9cO1BHGVnZwD1bked90K1M-cNh8Seh8WEFnUSWmFfNJoQtIkhF0n18WMRrUPZRsx1fzOs6D9ln6hwI4oRee8X6iBI_H6GbB3BMhE9VkzTg_D4Yt5JxLFq1h9wPjfEgtoWK5JKrMNun6xrCB80i4zHUHXFbV-qRzydL-mIhxL5aCkMJhYQscqIsqEizfqJg8OGvU3nQ0w8iXLgVrEaQAa-gZ_ekBl1Y2Vc2TOA-XD8PV-bXCAb3uBiRXyqG2A-bwblbZLJ-SXJ5v-Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ZbeoRQ1rpl74-annyCplLOeMaaQm9FbkOfph933nQ05me9RghIF3WzF-CN-CUrKvrADxZ1eB9cO1BHGVnZwD1bked90K1M-cNh8Seh8WEFnUSWmFfNJoQtIkhF0n18WMRrUPZRsx1fzOs6D9ln6hwI4oRee8X6iBI_H6GbB3BMhE9VkzTg_D4Yt5JxLFq1h9wPjfEgtoWK5JKrMNun6xrCB80i4zHUHXFbV-qRzydL-mIhxL5aCkMJhYQscqIsqEizfqJg8OGvU3nQ0w8iXLgVrEaQAa-gZ_ekBl1Y2Vc2TOA-XD8PV-bXCAb3uBiRXyqG2A-bwblbZLJ-SXJ5v-Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Ec2Uz5HtP61JMu5Ud-_Kqwa6paD84jmozTUhmBQI7yPFscRF7W7DqsNb-9qqTNe7yH3kSyj5R0YAuE1oO7-3f6hmd-5HdFuVAKbspYe8kNSkCf7C0NE-TzAfU6zIQuf5YlLbZCX5bY_W72p63sP3I0cqQdwpEr8cbpPHPEpwGV3Rm3jnIMiIZydMDU8XJ9q66rngF012Px8mbTCuWDHtjzWXa8u29my-eTkthuIWrwjsufZRAwDFiPzx8pxjyv-z9tU7nkSy-BWQI63BabWMOKVWBUAe3Mv-znCo4gGGIgscSuwA5HSkIt16Pv9fh8CNZswMCXILf6041C-lSRXlHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Ec2Uz5HtP61JMu5Ud-_Kqwa6paD84jmozTUhmBQI7yPFscRF7W7DqsNb-9qqTNe7yH3kSyj5R0YAuE1oO7-3f6hmd-5HdFuVAKbspYe8kNSkCf7C0NE-TzAfU6zIQuf5YlLbZCX5bY_W72p63sP3I0cqQdwpEr8cbpPHPEpwGV3Rm3jnIMiIZydMDU8XJ9q66rngF012Px8mbTCuWDHtjzWXa8u29my-eTkthuIWrwjsufZRAwDFiPzx8pxjyv-z9tU7nkSy-BWQI63BabWMOKVWBUAe3Mv-znCo4gGGIgscSuwA5HSkIt16Pv9fh8CNZswMCXILf6041C-lSRXlHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jG7_krJUwxhmHLfRqeYzVhQI5saXpHa2qNRkaosR1uZq0XuPJu9EJeYymsOJK1Zh3jZUNu56vhI4d4g-NbIH4dXosXtGW9pgPSHN2Giiwdsb24xqEnoJ6tLEZwUSwOPXueGSdUjFNPmvrMwFWXNhPochcaSOIu4VX2W0nUbSIUkngcPl12f9vfi2cj2naUiN0TmpmltzRqL4patywI4v190JiqFbEi9-Ef8nVfy4oFnE5h-DPHsA97z3skLLNHsEZxxrzRxTdpReiFrL4um2ItXVsC1j5NaZa91BlTbUIttAMcRpcE_Rr5bvyuRWqvmtMQ878Enk5KSyPB3iACv2uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=jG7_krJUwxhmHLfRqeYzVhQI5saXpHa2qNRkaosR1uZq0XuPJu9EJeYymsOJK1Zh3jZUNu56vhI4d4g-NbIH4dXosXtGW9pgPSHN2Giiwdsb24xqEnoJ6tLEZwUSwOPXueGSdUjFNPmvrMwFWXNhPochcaSOIu4VX2W0nUbSIUkngcPl12f9vfi2cj2naUiN0TmpmltzRqL4patywI4v190JiqFbEi9-Ef8nVfy4oFnE5h-DPHsA97z3skLLNHsEZxxrzRxTdpReiFrL4um2ItXVsC1j5NaZa91BlTbUIttAMcRpcE_Rr5bvyuRWqvmtMQ878Enk5KSyPB3iACv2uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WF7LcbinBGMWFTE2OpauLPOMEB7TjHx-uYM9l-q3dOlJKf4a4Ratm-XaXMvinpI0dz0xCR2GkPBh0GAYOeA6ebOzAQVHuU5QEF3p6iDJ--WKiVpi32aAWxuMc1ieEdPknkXnji3Nk3JMsVxL9Ht9zbtLfkHq6T-jqVQa7foo-MGna0uK-i1AqE7buRYh7pIHX-3N4zy0rI2TtoxZt_h90su7LD3msX7t5_suB-W_Y00zv-jr_9Dy_0ztm-kdsW9M_qMd41rJKnKYOO-4bo4rTW0AWdUnmqyzrPWrHl9JyDoiZD1MRryvUWLvS4fAAEDKHy9pn9XA8HyyUpcX-Wrp_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WF7LcbinBGMWFTE2OpauLPOMEB7TjHx-uYM9l-q3dOlJKf4a4Ratm-XaXMvinpI0dz0xCR2GkPBh0GAYOeA6ebOzAQVHuU5QEF3p6iDJ--WKiVpi32aAWxuMc1ieEdPknkXnji3Nk3JMsVxL9Ht9zbtLfkHq6T-jqVQa7foo-MGna0uK-i1AqE7buRYh7pIHX-3N4zy0rI2TtoxZt_h90su7LD3msX7t5_suB-W_Y00zv-jr_9Dy_0ztm-kdsW9M_qMd41rJKnKYOO-4bo4rTW0AWdUnmqyzrPWrHl9JyDoiZD1MRryvUWLvS4fAAEDKHy9pn9XA8HyyUpcX-Wrp_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0oBrXt_6lCiYrIvM3CWsUTWuxfDUW4J0z6G59N9tqNRK_UYGp16m51FZtVb85CngRTdtkQkv96HPbGJp6-VFaTw36QjDU6vmgfPF7bwS9DaqT7wHmUl54PPGEexsoVKdKAEhE8XOzIqtmUvEehuu6a1haCoq6FFa238Qh8CLYAZBNk19aqUHcXgexFt5nHNplyYrGzAaqJ45lF64dU2zJOOiBkjYcSU77aIpMWm8vZYhSRbu0JlrtBzJYOETnfLUcw-n_4meOttVoNvluKnnc8P6smjncsBDM1hCbB3PTuqkHsMiKKpHVN69nqwEpcgPC9gMTsyZ-Qn2eRoXEJ6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fQkG6mrm29iUQt9ZKrofCJrg5BmIzT7qJH_LgVeN0FsjxZvvQRFrgti-VvYDnvajoPRaKnouPwyaDTR53rQUktdLIikRZXgBo6V2tQjorEs2KR1VMYy4i-bzzRnv97RYojm9gMMYeVrYhGZ4Ve1zJn1r9FJG9JZct7qCzgmrm45bfijljIrV2YlJXv9pxC0hJj8Y2j4dMBEGjnse_joCLXDytJPYJdC3nSAydJsNPZDDOBsRmmVLsPEMTZe7SiYv747_liPHcWt72WVtyonZWo0n8H_KvgJEczEf1ni0Ms5w3bRggWQPHfmR_6jab3jBMbIAH9-juEmVAM2AenU1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fQkG6mrm29iUQt9ZKrofCJrg5BmIzT7qJH_LgVeN0FsjxZvvQRFrgti-VvYDnvajoPRaKnouPwyaDTR53rQUktdLIikRZXgBo6V2tQjorEs2KR1VMYy4i-bzzRnv97RYojm9gMMYeVrYhGZ4Ve1zJn1r9FJG9JZct7qCzgmrm45bfijljIrV2YlJXv9pxC0hJj8Y2j4dMBEGjnse_joCLXDytJPYJdC3nSAydJsNPZDDOBsRmmVLsPEMTZe7SiYv747_liPHcWt72WVtyonZWo0n8H_KvgJEczEf1ni0Ms5w3bRggWQPHfmR_6jab3jBMbIAH9-juEmVAM2AenU1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Rx4MLvkFBEcRTneBo1b_-NcEM57KPsn2rbLnkfPupZGNXbIWBdSiIf4LsQIl52dttwz18YUjhD5pXFp0PBO81kGKiSaSKM0cwH40_swzqX_m26z8lUEugqcfTHf-cbvTjGfZm-sx32rOQ4yLMuFdNx1pFuykXPiwOlFnYoBokx1Ut9JejX70TtRT3-txK6nXoeqjH4QufdE4yHMV5XS-c_SrQwMj82lPL6HwXV-7ERqNVPQf0pbd1Babt_tNpPpErK_aA2TozzsHO88COkIeEjy-X6i_9kBNogLpPUFCguQRU-M4MAxPtCG-zazunGUcBUsKtInEYEyn0oyNyVAsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Rx4MLvkFBEcRTneBo1b_-NcEM57KPsn2rbLnkfPupZGNXbIWBdSiIf4LsQIl52dttwz18YUjhD5pXFp0PBO81kGKiSaSKM0cwH40_swzqX_m26z8lUEugqcfTHf-cbvTjGfZm-sx32rOQ4yLMuFdNx1pFuykXPiwOlFnYoBokx1Ut9JejX70TtRT3-txK6nXoeqjH4QufdE4yHMV5XS-c_SrQwMj82lPL6HwXV-7ERqNVPQf0pbd1Babt_tNpPpErK_aA2TozzsHO88COkIeEjy-X6i_9kBNogLpPUFCguQRU-M4MAxPtCG-zazunGUcBUsKtInEYEyn0oyNyVAsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhLRdJt_SoNEWmdZR0EBKtJXWYO8h_61bL5Ds9OuAb-h4WeqLs2p6uHCyLsS972Ai2tDCxsODqteRW-v2TDbeQst-oBRSFjzrFourMMXx79Kd_0iJuYPJUqpSJ77BR_stWsJK-678g8UnXHHVru8HOagv1ucl4Ic1mJ_JNzvZ4-3CLLU2BnyeohTWENEcHXXL-LpWuT4LwJcDedP_B9Njn0yG5qtJRQ8BVVYOuXJrcP57ZLd5acdO-RDm45SKEq1N1AUWRIDnmRcRVFl074RKrxBiH7aps0BGqqzohw39Bt8OsG8Yu2cMpR7ToTBfHD8tnEFIfRFToq49rr3U-AXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Lp2owU9-4FFKlWjcGiFB40L6gfVxD-paBMQ9NHWBgrp2UYWorNHkV5NeHTqKButK8_DSXhwxKij_f6ZMuBG_9s4EtAT40l_w2u7H0nihQZvo5uONV29OpZ27QTPaqbFDKMDs0hHYbVWC4Ffh2l43kbYYJLSw0ByGVDkoj3r-TkL8E0viPYNUvIb-tO_hHg0ArDo9qU1wxG_JWn20EZwLpQ2AWMhchnQ1X4uxzpJ7F_YTpF8DXua8D47A25cHDFjR9XYaYKQ7m5wd9NfSxhisFe-j4CDoat75igJquR0fylZfEIP7qU4WV4thj7qA5oEKf19lCxlyrya78zDKwJiPTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Lp2owU9-4FFKlWjcGiFB40L6gfVxD-paBMQ9NHWBgrp2UYWorNHkV5NeHTqKButK8_DSXhwxKij_f6ZMuBG_9s4EtAT40l_w2u7H0nihQZvo5uONV29OpZ27QTPaqbFDKMDs0hHYbVWC4Ffh2l43kbYYJLSw0ByGVDkoj3r-TkL8E0viPYNUvIb-tO_hHg0ArDo9qU1wxG_JWn20EZwLpQ2AWMhchnQ1X4uxzpJ7F_YTpF8DXua8D47A25cHDFjR9XYaYKQ7m5wd9NfSxhisFe-j4CDoat75igJquR0fylZfEIP7qU4WV4thj7qA5oEKf19lCxlyrya78zDKwJiPTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SFny1EV0pLB7td35-R4uvuwk0qgez3cPcXiPXNMSMIHjLHSgui_TB-Qg5VDb-Rvze0NSPThdssKA06h9iEBvsm1pK6PZAxKBVhGCBugCJq4zFhlSinoXVW2cvEWuDnPkegaNAqmOcq1MAm_1NRYKlmkMz2zjbPl8v5iRdt8HM6XcuVyOUAuyqOPGPQJAT2v0BEXDS6ZS8ybtDbUgm0HIS4b2UBgRPKnDIM5Y3l-Sp_M9pxmXdC2LcLpQFFIpkFl_9pqi_xNb07sO12kpRJ_0xegyVzIgCVX-t_9F14DyZjAVXzSFtz8Pfksztr8RFqNfMRnrXknkLeZWOCUsRrMd5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SFny1EV0pLB7td35-R4uvuwk0qgez3cPcXiPXNMSMIHjLHSgui_TB-Qg5VDb-Rvze0NSPThdssKA06h9iEBvsm1pK6PZAxKBVhGCBugCJq4zFhlSinoXVW2cvEWuDnPkegaNAqmOcq1MAm_1NRYKlmkMz2zjbPl8v5iRdt8HM6XcuVyOUAuyqOPGPQJAT2v0BEXDS6ZS8ybtDbUgm0HIS4b2UBgRPKnDIM5Y3l-Sp_M9pxmXdC2LcLpQFFIpkFl_9pqi_xNb07sO12kpRJ_0xegyVzIgCVX-t_9F14DyZjAVXzSFtz8Pfksztr8RFqNfMRnrXknkLeZWOCUsRrMd5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EueTBuooCvwrY2vJWGheBKARvS4U0e4RjQ5XUI3XFJ51_rTa1W6mDVUaZDz_aCvZIf3X7E5GRiSzXDBP1HR3OnoQMJmgSt6Ms3D8tj3cyYBHqBTU8Xs9k9Lv9_nfiIFFPERk9WlkzWzYJGrWR_7ga14EPIbhPaUFLXRh1hIGrz8_Jqk1MI6_0X7HkeZq91rNLJAgiVuH0oY6VahS10My3z7nxxY25S9mRWhxHZ6pOTjH6yWA-68SIIHCSRsVJ6guAUN1WB9q6-NZ7CBCftW8uFd6MNtbPAEVZ47dkaxWhBg28x1JAfSESfOIeyiTcJCHZO0FQJbfJdsveJlk95UJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-Ar6sCX37U0o1Jnx7--I5kqmQhmoKVALNiwRQdCxsnBbIWAOMNoY7VbEAY-50fgDBq3lRdxg4gHrJnf8_cwE2JzH83JCFk-4NG7qibfNFHubQnEpR-YuAEhFLTSIbDSQNh9f6999H8qxJWIRbOFFRYLB3Xbk-cwZ8xk63cByWi2rPDBQU8dpqXUArPs9ki-o1f-Em1t1E3sQckWN45UV7ExRXvSmGIjovngHv42jV8Mpa-WDolmwN41jqqU_MBoNDk5iXiJwtOpOWouJ1rHmhOaN9a2U7-kZpHI7o1Hy5hE5OYamJyJcROXeiWJz22JHqJOfMF3oTUERXNc39qGQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DJUnRoWTXgphggZthZcC0Zf8kW68J9VUFoy3d3TTgMi5pOEfv-CVkTN6QTxW3XuoNF35OYgwD3K4iMLlHA9tFo1EILJSuT6BbmtJiluBebSzRgrleDrBzqBc-AqHjwxANZOz1HMxVwhCqWUxg88cS9gHJuRdXBI5i-WMcaDU0as1XXDSuH_-eekLf0GPvq3gwIAyhyZiKSnA8X6UctYRi4snhpu9bEtvUd98uwd0FO7gdqxukcuhVLXqgVqKoQW4rqIsxiK-0KTRRNGmLxgmHqA4qX4WJLNVJ5b4Tu_2JZCZnZPR1jGyYRycL1VP_DL8s26Ex0YstuK7aY-2xukuRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DJUnRoWTXgphggZthZcC0Zf8kW68J9VUFoy3d3TTgMi5pOEfv-CVkTN6QTxW3XuoNF35OYgwD3K4iMLlHA9tFo1EILJSuT6BbmtJiluBebSzRgrleDrBzqBc-AqHjwxANZOz1HMxVwhCqWUxg88cS9gHJuRdXBI5i-WMcaDU0as1XXDSuH_-eekLf0GPvq3gwIAyhyZiKSnA8X6UctYRi4snhpu9bEtvUd98uwd0FO7gdqxukcuhVLXqgVqKoQW4rqIsxiK-0KTRRNGmLxgmHqA4qX4WJLNVJ5b4Tu_2JZCZnZPR1jGyYRycL1VP_DL8s26Ex0YstuK7aY-2xukuRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmwYwSxLQD1g7BM8MkzCM_QATzx2xcdNZQVFkBwiQ4LsKuGHCfuHV_B7h1SRwcbt6YuF3u5-dtBzf5Yw4vrSJZwGrE-9wycf1gFNOt99gvievyT8jVZsC8Xc0sMozi5Q-rRm3Rj_4jHu7aKQg5CA8bS3qi9l-L1WK6zjyHvEjPvnbx5agOaUaQVzw6Qvt_QcKlXZELC39ivrzrIB973x-E37CkFDib7cq2qM5Z5GmS1h9FwVxZQN2oXyNuM85sZkUhsoZHLgyl1QGjKd46DfyNBG4ffCaRChUAQfxPLtih_aVQzYS_eqrQV2eoxfyxJ-TOOG_0dIvlC5djlzmiNVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ksbhiu9ABNbem22xPgBXxK-vNPCX2qBofXi_wTOle062TyXvkUfAALebsjFUtOdojiM29hSnM10uAgPzqVnov9a61JAI1n5vHtHmnOBKHSFGw6GyfC87VGe1EgYV_WVhn9nbkn73qSAIlas8n_DfC8B01l4sJy6-a7zJRM_cxi7cN2FXd9EPGhII6cr5kB36Qnar--UaT02PsvRxXzJnltUO1RMtcnM1d-j_bkuKW3Q6cdAo1be9h4fj9PfjDfNsVKWdbfJeYjW1_s2wbBPQYNAYVKUW6a1S6jh7HJLoFK7pR5jhkqMXw5NfNpPZ77EofJmvgZRTveB5Yp1gsYKrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJK10Zz0pn0cIFmK1WLDtWuspLemgvUjHYW6e6NMeBMqexABRaTgj3exxekVam-EzNW0R0SNWAxWKDWKU2Fh7DwdwiJPtWyxaixbMt9iXND6ijBCiKXe4tt-PH6A6t7VmfcJ-nGixmcWXV1tjmmgLGD1-j07vuB1dsJNxm1fh0ZS2iW5DqNRxE8075AcOiNjTVrzpylRAZ_CiKk7wIrnZjLBPKyg4V8y_pb9e9YKEpmMnw4T55wIsJJO6GCYw48GalU6eFLhTajUuMEHiUzVBxPB3rWnVuL8BducsU2EnfNAn7r1oQGCbTEh1fQtitDni3bbce7YbBLiGDLXUijeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rETAhiMVA2hh7zN8Gs1_2vw1taZN_M6zD9d-SNdw--h2G-HLKYH91TMgiCJ79JnlJn5KoPquGBbmRuU5H1vxwPo-k3MNAcsLzlqEFVpyLiHwufB-aqmSmOhQAXLHrhjq8PXiQkIhukayCirEthOKNOGFi1xrMUiNcK0cvs5kUyDT6jaKEaD-_RxylzEa77UGgWRueF-OiQXh-yS4f8UZyVb-C1AAzgSM_qVUY9lUzDwmAt-fGfqXZDXddjk5uzFGvYYFjRarjDFy-U2USOaSoD4PkSBqfjNb3XEv9cCnsousTflXf_AJxRJPG8Y0cNrwxgsv_aL-Nm1FydYpii4fPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rETAhiMVA2hh7zN8Gs1_2vw1taZN_M6zD9d-SNdw--h2G-HLKYH91TMgiCJ79JnlJn5KoPquGBbmRuU5H1vxwPo-k3MNAcsLzlqEFVpyLiHwufB-aqmSmOhQAXLHrhjq8PXiQkIhukayCirEthOKNOGFi1xrMUiNcK0cvs5kUyDT6jaKEaD-_RxylzEa77UGgWRueF-OiQXh-yS4f8UZyVb-C1AAzgSM_qVUY9lUzDwmAt-fGfqXZDXddjk5uzFGvYYFjRarjDFy-U2USOaSoD4PkSBqfjNb3XEv9cCnsousTflXf_AJxRJPG8Y0cNrwxgsv_aL-Nm1FydYpii4fPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JC-oOCrD50DNiNzmvgbTNzkSmBcEkTt5821TOtl0cJtaLWTxSNhOZ4st0iOJ2amJSVAmMlRtbcmX-24-kZegTYixmq_hYtqJjy2oPjmmbVsNQ8sgJNVIlk3uc0Z9OQUPQo8EEt7yOJj1hB-HbglmGxFIB4FjQuo4CSfRNbj8Nci9Eo1tm1nRuz-emyEmrmA-7HiwiwObSUt3CjmssMfjevMooaTi5n2oCcjtHqRhShbkTQvjazPiSD9IdWVfIcHdTruPkKkXvb7Ll62dmXTp3uJmIrI1RWUC1S_Ul7-HekSuUyUf5qeqA__zaYLNVhwnGpd9v-TAD5oVnB_68dwRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JC-oOCrD50DNiNzmvgbTNzkSmBcEkTt5821TOtl0cJtaLWTxSNhOZ4st0iOJ2amJSVAmMlRtbcmX-24-kZegTYixmq_hYtqJjy2oPjmmbVsNQ8sgJNVIlk3uc0Z9OQUPQo8EEt7yOJj1hB-HbglmGxFIB4FjQuo4CSfRNbj8Nci9Eo1tm1nRuz-emyEmrmA-7HiwiwObSUt3CjmssMfjevMooaTi5n2oCcjtHqRhShbkTQvjazPiSD9IdWVfIcHdTruPkKkXvb7Ll62dmXTp3uJmIrI1RWUC1S_Ul7-HekSuUyUf5qeqA__zaYLNVhwnGpd9v-TAD5oVnB_68dwRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=akvlj65n0hLE3Z4nSd5KE-o1ZvCPMZU--xSnKKqWLmZefW-edNRKZ69WO4xoS_K0uLMa5-ejroec7GsqOLsrKeqobOhSxvLZZhguMjr38cLUlMXgOOTYo3wrJh5L1ay3xk6ztUdJbuksNy200Ctks9RXdWfSGATcYDvlN7ceuXcYeRIsA_i6sjJ5RJG3eWeuNTI5BNlpnIWSwNTgF8fbrxcq5KWL1fecJU3zRRxMAhHtmrfAqzo3xBcScMpk-MQ4MD5g9yPjEyzraV1JRCxWdhcv5Sr55BCdxn92NKW9G0Ag_89LuJNqAuuLa1B_lc5_MMey3LL-nYfvJepoaSMUCTiMKF_Qd9fiRTPCdJS51XjsJ0NQt2Re1agDeNSW4IsYjsSSeRb7W6DA0A7e4FzrpK2QHC4VvHQccYgdp_s1pBDEcUyZpwFlCIOW9mr1DGq42YByfHVTXCPpssQRf6MzB5B1gjjrBUdLCWJBAaLduYXgGqP0sJ7leaMRoPuyCF6azBRLDhZkZN8KYyJDQYA-_ad_CLbsB6eGRaQQwSnG8DyuXeeEBPfEo5MDtByJPkA1bZ3M53hX67b4FpUtCpPr5hUHGoUwDGH6XyTF3p8NdAOQp7aapwAode9u_ezpwjPkKe4EYfLzCLtpmUu0ImM9Eal7dV1HhM8vRsiCQJWn3X8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=akvlj65n0hLE3Z4nSd5KE-o1ZvCPMZU--xSnKKqWLmZefW-edNRKZ69WO4xoS_K0uLMa5-ejroec7GsqOLsrKeqobOhSxvLZZhguMjr38cLUlMXgOOTYo3wrJh5L1ay3xk6ztUdJbuksNy200Ctks9RXdWfSGATcYDvlN7ceuXcYeRIsA_i6sjJ5RJG3eWeuNTI5BNlpnIWSwNTgF8fbrxcq5KWL1fecJU3zRRxMAhHtmrfAqzo3xBcScMpk-MQ4MD5g9yPjEyzraV1JRCxWdhcv5Sr55BCdxn92NKW9G0Ag_89LuJNqAuuLa1B_lc5_MMey3LL-nYfvJepoaSMUCTiMKF_Qd9fiRTPCdJS51XjsJ0NQt2Re1agDeNSW4IsYjsSSeRb7W6DA0A7e4FzrpK2QHC4VvHQccYgdp_s1pBDEcUyZpwFlCIOW9mr1DGq42YByfHVTXCPpssQRf6MzB5B1gjjrBUdLCWJBAaLduYXgGqP0sJ7leaMRoPuyCF6azBRLDhZkZN8KYyJDQYA-_ad_CLbsB6eGRaQQwSnG8DyuXeeEBPfEo5MDtByJPkA1bZ3M53hX67b4FpUtCpPr5hUHGoUwDGH6XyTF3p8NdAOQp7aapwAode9u_ezpwjPkKe4EYfLzCLtpmUu0ImM9Eal7dV1HhM8vRsiCQJWn3X8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=iMGtURzRC75tj_SwVcGzJ1KgGgSG1WkXVox5dhVuh57wvCkN_KOZx7g24HuS4L9ZBYTpV2E-_gdELv9duKWm617nm5JQ502-4LGQf27Jcs9Tq4EHt8SB_OIRnicRLZx3FcIdCvVg0VfWALllwMVZeJRIxItebVzkqpsp6oURphdAtH0Q97_YUqMJIDu7lei157iH7TWkeBNoMX3Aex4d44nLHF68HM0OUHKprUqn6llTpDINZU114ToAGwmrxY_j2ldfB2HRysox85JktSyihS-KszgAe1xPyTZuBexUFW8dVzu0Cgvt-8QcjirWAPK532O7JWi27PX7TPil5OPDpF4CZA1IVKyiwVCElrSh5sD6OWiv0NI2kl9q9rU9NWz_W7yGOuWrSZx7KGQLv5HkI1l9PHQ3dQBFpdf9nFBQazffYF5t_76JJoUkOjYtBlChFKRE63woq4FBjui4nAt2ThrGkJ_izuduqo1yhWkDtt777Pg3rMe4lh357k26nROmuDfEdikZn-qaj926gG9-7rR-lkrKx32kBACMMDYtWVn0O2kY_oeJvUS4chrKWplZtIG75SU8vwVkq5Ai7ZgNgv6hbJa5P_XWbJVKveg9EMg9OSK9Q1xQ0dOQzqBlbJ3S2SUf8SxZQA6zcE96RXs1oK1pMsdAvDY2t-IgL__qu4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=iMGtURzRC75tj_SwVcGzJ1KgGgSG1WkXVox5dhVuh57wvCkN_KOZx7g24HuS4L9ZBYTpV2E-_gdELv9duKWm617nm5JQ502-4LGQf27Jcs9Tq4EHt8SB_OIRnicRLZx3FcIdCvVg0VfWALllwMVZeJRIxItebVzkqpsp6oURphdAtH0Q97_YUqMJIDu7lei157iH7TWkeBNoMX3Aex4d44nLHF68HM0OUHKprUqn6llTpDINZU114ToAGwmrxY_j2ldfB2HRysox85JktSyihS-KszgAe1xPyTZuBexUFW8dVzu0Cgvt-8QcjirWAPK532O7JWi27PX7TPil5OPDpF4CZA1IVKyiwVCElrSh5sD6OWiv0NI2kl9q9rU9NWz_W7yGOuWrSZx7KGQLv5HkI1l9PHQ3dQBFpdf9nFBQazffYF5t_76JJoUkOjYtBlChFKRE63woq4FBjui4nAt2ThrGkJ_izuduqo1yhWkDtt777Pg3rMe4lh357k26nROmuDfEdikZn-qaj926gG9-7rR-lkrKx32kBACMMDYtWVn0O2kY_oeJvUS4chrKWplZtIG75SU8vwVkq5Ai7ZgNgv6hbJa5P_XWbJVKveg9EMg9OSK9Q1xQ0dOQzqBlbJ3S2SUf8SxZQA6zcE96RXs1oK1pMsdAvDY2t-IgL__qu4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uvvs568QtPkWKWOcpUuIij08NXksRj1hbpmlZhaccWBLFM6nlfaTMJVsN07AceYj_grTc92y0jR8SxDs3BJ5UChPRuiCmnAHbSy_dylx9hQe6qxn7YUNHBJp7WExfVoKs0Swdl8pwlh0-sgpli2lWfPAqV1m1_sBbbIK57QBuVN3DsE37CYLy8T2DHENuEsJHkvrDkaFQftGrOOmvsuuj4BI1AM9kYpfPb4tYuclp_cwC3WitYUT1kIOPRakKBYxBvic6GvByhuolRPiwPxKi1ZfNsOzd2h-fjM1Gf9XUqbdauzIX5HdQN4A7YjhaZaMPvnJQxkcavEMl2hyQjccmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uvvs568QtPkWKWOcpUuIij08NXksRj1hbpmlZhaccWBLFM6nlfaTMJVsN07AceYj_grTc92y0jR8SxDs3BJ5UChPRuiCmnAHbSy_dylx9hQe6qxn7YUNHBJp7WExfVoKs0Swdl8pwlh0-sgpli2lWfPAqV1m1_sBbbIK57QBuVN3DsE37CYLy8T2DHENuEsJHkvrDkaFQftGrOOmvsuuj4BI1AM9kYpfPb4tYuclp_cwC3WitYUT1kIOPRakKBYxBvic6GvByhuolRPiwPxKi1ZfNsOzd2h-fjM1Gf9XUqbdauzIX5HdQN4A7YjhaZaMPvnJQxkcavEMl2hyQjccmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA8QLJN-M4_4Q9WI2yJtRiUds5nppBJboLebTX6LmICOBlyuYwjkzeYWDunMD17EZ27GfqRBOnMnWOzL01KOeoudkR1SLEckl44VVqec3VjVbHAzgtwuu_wiS9jJHTG5-pAXSRLb2g7SqH9LBqt1_QfZ8Wh_zvA9k2NDgeUk002oJySdtJ_uGf1LTVtSQ9-Q4zm9u07CjPMiF26A0dKYa_3a2ABy9pKolgtqvwyNPjSXmgJ_5aMDUzOVdQS6EUU2ICbNS3NQN7oTQfFscXc9-WR3JWXKN17pEfDmXdoJdXeXZgERROX3xxFo2htj9RvGOZZuGWPIgXf_66CeMcWbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=BcnJbKLwioVS0xCHfU3FiCAtY6fSpufSwiqCq46m5n4B7scAJ0DtduekGg0WcDCEssNPM0zc1bxYlE3SPEyNSl4YF_qT-kForLZ1Iojn9WaLn4okzvr-d7jT_WH2lCN7tiTNigdifOm8YOLrHnzmb5E8KKLFEEspWBi0FsAP6S13pga3d-8bnMlcOwc9RwquGXGXdZcN6ZhNwHnkdqeQM1NmEe1yz2Otx2btxx4lq3sUYdDgErKopSs1YCHOZTwRcvnqUfvdBTdcQ5P4iMDajuIZJKUC5xnbPIWY-BCJCNBAKR8eVPBT4wCai5x2WQZrfjGUaDDkBrDk_REPQfusWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=BcnJbKLwioVS0xCHfU3FiCAtY6fSpufSwiqCq46m5n4B7scAJ0DtduekGg0WcDCEssNPM0zc1bxYlE3SPEyNSl4YF_qT-kForLZ1Iojn9WaLn4okzvr-d7jT_WH2lCN7tiTNigdifOm8YOLrHnzmb5E8KKLFEEspWBi0FsAP6S13pga3d-8bnMlcOwc9RwquGXGXdZcN6ZhNwHnkdqeQM1NmEe1yz2Otx2btxx4lq3sUYdDgErKopSs1YCHOZTwRcvnqUfvdBTdcQ5P4iMDajuIZJKUC5xnbPIWY-BCJCNBAKR8eVPBT4wCai5x2WQZrfjGUaDDkBrDk_REPQfusWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=FKiGol33oCTQ3ePr8P39KydWAc6f5gWii2UzdBwVoIRom1wHM5AJTGg9Tjzi5aszJCd8_ZAnUMrymTMGBFU8jUOt8_fVQ8uHOMNCXxuJoPylpXaGDbpSLK1TcpC3IOGX8LCwMCJQQrRyRIR8r7lRhICApdnl9gsbHTpq5D06jy1WkWAwpPSceOpuiFkKKPGm8swmuNBE8l56gzwkpZTFttdh-KWvR4rJW3zKOVv6pxrE1bJzfuRjuCumEDt1br8Af8vmh4PiGbHOEVUXHE6TNfcsHb3jXvDVdNNUU2opdhzOkc4SLh9eUckRwVLOPB7IPG1btTJqEeYs32_cbuu2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=FKiGol33oCTQ3ePr8P39KydWAc6f5gWii2UzdBwVoIRom1wHM5AJTGg9Tjzi5aszJCd8_ZAnUMrymTMGBFU8jUOt8_fVQ8uHOMNCXxuJoPylpXaGDbpSLK1TcpC3IOGX8LCwMCJQQrRyRIR8r7lRhICApdnl9gsbHTpq5D06jy1WkWAwpPSceOpuiFkKKPGm8swmuNBE8l56gzwkpZTFttdh-KWvR4rJW3zKOVv6pxrE1bJzfuRjuCumEDt1br8Af8vmh4PiGbHOEVUXHE6TNfcsHb3jXvDVdNNUU2opdhzOkc4SLh9eUckRwVLOPB7IPG1btTJqEeYs32_cbuu2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ4INwb_9eVIfVgpveGVNKmztQ5k0TUYMmYnb00bJ92-aWHfaxZ1isvhYRnSYnUthxCYkKQeoVC7r_ZfLrZTEArfznmaJPgbKtwH8sTQyG9-dU-O1B5rSwDn2aoAvLypHSqpXhqFTaB21I3hPpfUvQ14_TI3qTDZEcPDua9Lx5oYW8ZtwjLMkiecTfHY4FFUS_Uv_Pc5fXoSgmtdrKuVN49gjEKqNFFobG99NtzMG6nlUFJZFMbrEjAuL6P8txgsmevLy1H0i5z73jv89aswJ0aLlsl_eO2xK-xrv6y4wyU1CIfIg3_DUHcsenpwqP-sttCwir45z6TrVzbTfr9W6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJqeDIts_h5ToP1_adc8S_2Waj4ITR_7MUTIGXF30YfOyU3UKKtBYr0vYWbopO44tf0SW2KOR7g2PaeCuHZzWEu0W0nu29Rimt2TEl0AptjXf7DKPtG1HerMw6iOtRy3TJw_nw3ktk-KyXLVEwJmwYRELGIQIzrQiO05gU42HeP0TlKnpA_CpPsckuFDtFiPOM7YURXD3FSBlHqO93B4z-YgXVtMsuUpvNNVLsukGHXKalQRqDUgrx7IdFWOLGhAHFoK_L0THxXpQ2s5u7jwbU0H_LT6I7WifRfGUlNIgK_MUe5Z53cd7wonpyEssld6wQC6x_6dh3btnVKioVIlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbaRWFc8sLeAuO4JjzSrzSWdjD1XNY5uURpYUUw2aBM_xTNMgUYPHeW65KcsdAuLi3UTu6IYJ_y-1YVxqYsG8yuT1NQrZczNcihBDgX7TzHmc0170naIViRxRl2ri3ikQlQy778neGWkUdSKFh2HHOoyd9WUfJxK5IvIh7yUMMv_7zWJv4hBvthhX486RPAUZPqjcB--Y_rpkS9QP10BlhAJqZLXodpNI1RJabirHRXZpBIpFjjrR2hXaVu6PIS-iA2VIAQopkxBT2FSAuVTrRnFC2kQIAdD7TeM3GVBHADcJS3pAzhYz5F4pZhIykXZEohlTDL2EVlOj_bA_Odr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVFohCK3ci7H8Y5QnQf-nrBxgoujUgBvuqXVchXxZ1CWD_glx3thqnVTQdUrpj2JjqQzRVJkT5EVXH2pPapKQ5rewXi1V-oF1_DmFwz6qYgwk7SoNl9JvRlmrKOgmQbsVBBECMnXiHxlCYarD8Cfxi9K_5VOZMFE5itxmHHO9233q1ELrGClw72y_JtPU60Hf_DooN0DfF5nB-WAj_HHnVaQ1iFVCHm9e82x459EbGRXS43vvdenZxatYDI1GgfPNMn-ohkGy3wrQaWQ2aOZbYzQ6kx8ANbD2Tsrxx-WM-YNMHUgM6LFFMh7D40VefTSo7uXghuM-gYXqrnlSlws4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8L4XiyL8s9z33d0j3PpBoSlJ4KJSZH4gy9CmGFKxb42i3-OLbTy336sdt-EOeuCZOoQu9ApotjDyS20fZM3BENZqwhlpYpcj4igRyTW4c4rdOqvlcRR_K0N3ZiZ4O5yp2XRVkcBtlH6tP5HxF9I1A98vLL3EQjm4HCV-MZgdLXXOFtHum1_je56oPs4cTJX_5oinxF_GncsSLtvWkHq1XTmFZ2eXF7xcMCsaRBLiOh5n3ocH0csGXHHHQP8_mQjVtpPmH29xQrRtAJlhQQCBkWNpVnsYu07Ewv9LFaEOMwfiZQtTnMib30B0cc7nxNdf7SqB4qy9OXWWDPXgTkwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYahaMcSxRhmDPpdACyqSAqVMBRoBl4r8kw_oyhFGqT54vWwSr_zTm60PoWggvr7CJujHX0YDvW943gU0CXkGyw2QjS2Vq3WqXSFKieQ7C3bS2ip7q1Ry96B5kKXj5b-Shu3BwCwj4GKURC22b55n5teBiSwAX_4XatINvOTLe2OxrjnUmcYcq3PPwmjhxK_QmzXF3-jmqthqrqK4cSSHNrIMfOslULTrQLwtnZ0v4DH-UNvFCH_vm-8uL4q0Px9igiycuqRmhmKtbQxRT7-_E6WgwF8fO1F-svX4QA88hlVzNU5Fc5l6Kleng9smUMLVYn2hhM978zgGZHwFDtq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFCncvsnlIFY_ZZWxjSvKcCXCaQD1Cs9TZnW_DyKNKxVHq3gT58Vkt5jaLTNyEsB0QuZep9BqlGCnrbBk_z5UlNE6xvaneCukVsuZFG_yl-IVrb4dOgiSbXWgAfsMWum9ouQfoi9ySffQCOpT9CMj11Qv7zfynHOUU50exB3cCOXsNkQSuXDgbtOnfFw_gXY3WsISNs0gl9FkS-KfJoJrQzIr2XQi7jo7nte4jQN0r9qmv8aolBWBPhZNOQ9R-kYsnLWo18OSr4T_VVnj-jpx6KShIEyVtCGYKF8VLO0AWAbgCvWtgIQ6HPgsRr6qwnz7yEHNBy3oedAe7esN9aqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npebOxhcWMJdm2oT9kTj0YbN3ZdD39QQVoF7DYDkPCFeI5gK-6CAyAInjeU_kWbZXHymylQbyJbW_AncqPze-9Pa2zudnJewSIGxmrnuKZf7ASoSYXefA-FztvjHrHVfAIhrelQUSHyWhhC_bBBsjf4Sv8DIVBUjvMyoQ_0zy99YdnbjqgKOfhs4Q_WqwHqqukV7xcMT5uWBDXIDVTMz7Vso-4VY3APT0tTGMLWA6jI3JhGs0v28QEAfClKLL6qklD5Iyx7U6ZcoSvUUavcQzzNexO5uUa7mfdIgOJPMyDJmP2i0SF4xRMdaGZuuIi_eoS7gJ_mbVvMNH_KVF7332A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwH076-AYyvX6YJ8cDFUHfk23Op5FPxuHpave_csuzENad_cRMw3ea3N3VVygGF6j-RTGzss_3AQiflYaL4h5_cB5i_5ZcyxlohvdQasO_utchzw5mTElZB4i8_vVSZCr0lbEZIdEDonMBw-ZnEIvOo5Ae909qA93666D6GVJ4nkVlEjhGkfyiDdBtSfA_bmg65M8sSW-zX2qNngHC3PBZ-SEXuU0z03jHl_AtYlQ2Io3_r0tHvaNva6epYs5ukfiuSQIv1c3_35DVJQCoUnEbboas9g9mwFoEsPjgBucI-6pSoJeKTQF6zCww7LLzZ_JNyw_sWViXq0qICgC_MUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTf93Adi-MiL5RQK68mBjts9xcxijRY4twUzxSCxZbCMZZVXcNYmRDe0A_A17qnMLjd2qdnFRaY1cJ-KkaUOjV53QKL-V_ckSHFeWK9SACRQ7N3c9ujUX-oEc0dnC8gj0fez5Vat5c4nGK89LNmJtq76a5tNEZcSGJaS-Vx-S7aXpmlKk9-Gn22ZfA6L9Iyj-P5kaZJOQ67LFJQa7ItiXxZvJnHBNHA8-7MRTYLVy2qb6vMUrZ3svX09Gz-SHHZFrWKtN8-YRGQFajzDJCDo6YiogVlfy1iF2nMsOggE6VYyssPeaouWI9Ho-EWlGu5uduSUqT8_H4IFvkiV4pqirA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ALreyFGZf_hNxQUdHafqGuNg6OPSJkCIFly2Vjtvq5m5xhzlAhxuGriL504wM-PiG2tC57Lcvdf3WOsGE6pl4zXhmtZy5Ki15in6yYhFuZEmCC8jXB8R-8elK3LpAZ7OdQ2NDRCv2qSgU3Pt7gKh1vicpAntcp1Lk7gnU7THyNio1soBdwoh60z5AgeDUGwiO598kyxf_dmI-5WHHG4ploqrPIS1j1o4IpcVJChheM1KOG88o48YfwNUdxhlku5YVR-gm7zGq0l_zOG1gCU3JOxIqmo8MftxKcP5rUjmf7Dosg-IjRqiT56w4zbUmR_HuvaCDJ3Q92ph5pRy6dqVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ALreyFGZf_hNxQUdHafqGuNg6OPSJkCIFly2Vjtvq5m5xhzlAhxuGriL504wM-PiG2tC57Lcvdf3WOsGE6pl4zXhmtZy5Ki15in6yYhFuZEmCC8jXB8R-8elK3LpAZ7OdQ2NDRCv2qSgU3Pt7gKh1vicpAntcp1Lk7gnU7THyNio1soBdwoh60z5AgeDUGwiO598kyxf_dmI-5WHHG4ploqrPIS1j1o4IpcVJChheM1KOG88o48YfwNUdxhlku5YVR-gm7zGq0l_zOG1gCU3JOxIqmo8MftxKcP5rUjmf7Dosg-IjRqiT56w4zbUmR_HuvaCDJ3Q92ph5pRy6dqVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR2D42YACD1KXbtTaoNFV9j4v94XAAgXnG1ybs51KfYOotYKSFh1zOyLaGIKp80cVPtJAj6XjJtLyNK5rip9vCFjaiuTPhWbhpzR3ggYgkA4BimUslWn5QCgKOQfVar2KG-w_01kEqkk9XZZQOS-1eayAVEjG0QI5BVgfi7xEcAqfO2xNVr_qgqdeb9PbraBarp8XqW8-A8JmFE9qZk16BryitYN93ip24GgJ_cLzpKEBA7hriEgY_vUayNKun7gYSFYygr17bRXJkXdwfw5yq1OdYY2C0uUR-ixrmvNaDtAwPGDzK-26vsg9Ia4Khozq9MV0DkjkgeTBGo6NQy_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHXdDJzcgf80jwfN88Bp12tHYKPCWy66_25bRYdCRZ9HVpgV0L-7ZTsPZTzACQq9sQF32bKCpau1I4ozSdDa1u5VGda1AzwrMMAtMjxiyN6jr6EkYQiCp56e2T0E7xmcTd9ce--7TWFlY7I1bhyQOPlAe3_6VUlZ8-0hbEXJIoXNtS0PYD2nZSSdtN80n4hatWXxQSshADfImNT5gPaxg_tOLoui7UEstBrpJ_7zARAzVRyukXsYre7l3tlTZnmNdleGRbZIrEPuvFjMu4_bUS8BgB98UDSTVyenlzwGCd6nwMH5BPaTINEIgCk-5_THNL7JUsEZyiQXmxtRco-Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WQtm5Lp1QZCW6zCBlFVHYmkpLUmsdMrWlOCyq-7Z-ms8rKP5B43leZPq-95OTnI0WTbfoxWq5KJZmSRZUVjHYvELghg9TKB8D3w_dVVtrYEJP66KwsFKpP9sgwtktF7OR80trZ0A5tJSLlstOFjiZwoF2RRKGXBYQUfGtmcgj1ENYgGOHdPRShRzpK1AfANa0zp41YoZeJKznlWRmzIniG-aRIrUci_vvJ9-S9tQEImeru5XWZCgXpXfW3QI73451duHUENFqpVoofAC0UFN_Ac7nsE_5tfRlGdBNxyXnk7Ap6EKDrCQJFSi0gSPwjqY-914f8Fzc_-wXbo3SlJIbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=WQtm5Lp1QZCW6zCBlFVHYmkpLUmsdMrWlOCyq-7Z-ms8rKP5B43leZPq-95OTnI0WTbfoxWq5KJZmSRZUVjHYvELghg9TKB8D3w_dVVtrYEJP66KwsFKpP9sgwtktF7OR80trZ0A5tJSLlstOFjiZwoF2RRKGXBYQUfGtmcgj1ENYgGOHdPRShRzpK1AfANa0zp41YoZeJKznlWRmzIniG-aRIrUci_vvJ9-S9tQEImeru5XWZCgXpXfW3QI73451duHUENFqpVoofAC0UFN_Ac7nsE_5tfRlGdBNxyXnk7Ap6EKDrCQJFSi0gSPwjqY-914f8Fzc_-wXbo3SlJIbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=vBBIS6uEiXiM3_L-rKgmmtnOOsnupgxvvIEc_3RubzoplQPkOh1wXeiRxqs49_djHwZ4vV82FRAH2nZBBrImCchTBWWLL874trp1XiqsXGlid1UBPIVBI9hM8UNahnoBST-cm-v6WsvHa9zjYPBntNz99nlaBGxQHpWcUtWhdt7walUxY0ooDf8YHX-w_FlN2A7fYmAXvW5ugrkgw6IZENYDrAqZ2uUQw_5Fx1uAW18t26P543PQISrHwOoE7chw-nhc-awbw4-zdPbfEOGBmW4ZFvHuHY1D5MUNtS-xzeve--Oj9FiwWy-DOppAl6ytTnhpcZARqw6BWYizIL8nXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=vBBIS6uEiXiM3_L-rKgmmtnOOsnupgxvvIEc_3RubzoplQPkOh1wXeiRxqs49_djHwZ4vV82FRAH2nZBBrImCchTBWWLL874trp1XiqsXGlid1UBPIVBI9hM8UNahnoBST-cm-v6WsvHa9zjYPBntNz99nlaBGxQHpWcUtWhdt7walUxY0ooDf8YHX-w_FlN2A7fYmAXvW5ugrkgw6IZENYDrAqZ2uUQw_5Fx1uAW18t26P543PQISrHwOoE7chw-nhc-awbw4-zdPbfEOGBmW4ZFvHuHY1D5MUNtS-xzeve--Oj9FiwWy-DOppAl6ytTnhpcZARqw6BWYizIL8nXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLmM340jVqMXyLOSMcSzuZaAu5LUrMHltogwx4tVbPn0QHjdCcBn6Vis1UvExllbj7ut2LAynBmr58jMzwMZC7a5awpGVUONVmtUdchQEqRpVV79PndCWac99q1eJCpxoRqcGQ89liRYJyBvNiGOJvVK7kk_jmfXCYpPnUaYrrdc8v3Lz1sNnMoQFZ-d6WHyd9wFJBWllYhr_Nvy_mzxKPT5bIl75EWmu1tXwIzQF1WQD_vHmKvKomH7Ryt-GEYq0pDG1p-I1t5tnasNejWV5adZR1omYsB5L3JM265V8q7rpT0JVg_y2J7wfWqH42gsWjBW75cGp5UVZWluJHIqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhiIawTGR6rAOLU8HloMoq4isbFwFGjQU-UOPMLWtbTCyPZlmneepPR4hoNnKSz_tysNvq4q_Q4EeMCTNxkAH3zMazcXPxPjExYojR7YPhFpdAjD9J5guRtUtJuc3Ini6dRdYlq3mzCPQiZNvt0avQRhFmcKsGikkYOemAZU1op8XZXfGz75Jzj_K4PIdSB_1X9GWutZGt2PhbEtE3fNnDtgXRQ-dlYfuAAKzWZTkMI6eBGodaTLjDNb_eCtjhoo-wBr4tBQIq7XWaPB4Z4Cc0KcMrTEVeWaRCzxB1NCYCxtqJSFmrkahJQbFc8My1Ak0ZSxqPkEeUfyMvVpWZCOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRZB2vCLMNQ6fHtaB34fy-Vg4X-EE2TCazlj4AKV5o7Yx6cQ2qufzkpZQKkagt3ujFpcuT_lWzNoLxg258QiqxiRwnlLDdtrVHWQ65n58Vyaz7-DL7oW2YvCjx3w8sx0Cd0-s-QpXXkRaHB6iqHd9cg7j78g_lg-_2zK8RBEiWPR-55CagWcV6gaDUJ3KB4GXmXgKvnGF92LMuqLY_QkvQ6fFyUE1qykZ5Q5mC8F9va1smK9I15IH4mspdrktTh23U_grQnl05ujluQw0MDHpi9Hm0chQZi59hzybwCh-orsH2dgx4__bDmCz_se4CTdlkBWgnnOUFh3CwJMjeuEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2AMBP1ElLQ22dOKZbr9-CBoxrN_RqEFlZsCZKwTtJ6y4rj_7Xl7ywEf9JJOvWEtvWzroIxb_k4S1apXyi62C_B_xQRASODI8d1FRL_1o_MkvutCAPbbEs9wAlBciAa464i5AzeWJfW8RNU-LIlPmbScORLlsuYQS89dbELD_0wKdX4qCh9MNLTIi48y56qnnLSDTcgT4pzg2AgfqYJpZEQxIKYOoDVzpP3emdop492ctUpvayCoHc4z97hHNzDMG1SdBxEhHwqtsPED8GZUMb10ZynFMQQjwfAr29tf3EfUpO0hjV9GEN1IiKth2b96zOOA2nApseXntFlS5KodjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwSvHKHMOvbzaqmfb1ukZHmSpcwN90mC5YrZqzcvRfFW1XBjNan2oKbBNwESgJ0qX69hdX5Qle02JzwFED-heza0Qc97vR7VLYFPJGrVsHlJ4Db8DX9MxmmxJhzsv5eJzJVgZkeN-EBetB3sllEe61dIEmm-OrjyywXoz8wehGjr3BMJjHbq7VjocUmp0feNuYmPVCbe1qnUtWkWJYMx0DNPiyw3xKf1x9AW4UOAefPo-RRWtCIFM0SRSK9nPnUIsQVKos1GeWsC2ge3EiDZaEoTLT7txFcdi7hiOyNcOjrSFUHVuFXxDveyWmHH94d-_C-enYRx_xqnGgPE2w8xkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTsOmUu8SR9y27nzgtVgjJZFs7pcz5MjPgK0uGf3PlvAkx46oLLwzs67hTXznSn35wsxKvgFn4-0oOuyZLhoZMwxsg7AfDOZqLjz-3YFIWFO1Zu5CWfRHfyAc2QF5qgbA88D9qFxW1oCNIUS45ma5Ioc57lqKcbwUIstqgCPKqFs9NH-iYf7fDe4gmDe2G5lUpVg2dHc5jtVO4Np8U7HnizAShDOlKLIF--NxfozoxOPqFWPV1aglyS9US7GXlXl9F7CaUYpgoPj44AMzsyQZzKz2Vna-2TZXZ-SJ2CelERPwuZfbBTYCYy9tfLSwWDper25YszoN_zCHt6on6Z7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGjnCHVXbka6BXO3nASfOcuA2Rh9l1-OswyuPfZD9DuWt9kggViEMh6F-dbbyXSULnvA_5qBMGZcUfXy7-f5AbcSSQVkr8il6Jy4sV-jZ28EhcZnlhT777cZ5i8Uts65Q2Q8F7dGJvejUYMADzTwZYsnbShQHyAZDQvxwfsLkTCd2wXlyM2fSayNcbMj9jz6e3fAcn-xg7yqqHoo1POUO0lbwU7Q1HdAjiuk5ffLLJcxyW3EuY6ftxcbXxoRT31Pk5mg__bmZ-HTNPrFT0wfkraBXGKpnnkkw7JUPc9tFlW8OGUDXJhQiPjvJByBpEJSiItqTl6qEA0Fp09xCV37AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWFdSllK721o5NOLSOhTcf--wastqXA3284MKIdqPFaLHoEhtDuutzF9leKOL-shHdaW2eVX-O0SidRBKYVS-xMin9NIwGOA5Yel_phU4ElP_3kTEbnWSkU_7QaUCjk-CnpOyZkiab15FgQ3ux_gv7IncD5NGC01f0qAqHBVwZ8Rjok5lCqpvNhBz6FfREJs9hquww-udBC_zCyZE8IczK_ZooVx96zz80zKKoZLyNO8K10WEK3y8q1Z6c_EtXPqgH0-4CIfkeU3laS_OG7MYMVhDQ5VMvE1UdgPjgW39LPl_K8jYW07nb6D3niebuvkPtWE5TOqdVsf5c_ZF9uDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nYAnoP4fU5Nn8994Vpl5q_qJAlu--ttk_4j2eCzibaApPENFjrgy_W79A2DcpaZr_YAMwvx0lwv9d3A7Xa8MSOpGog39t0_gtNc1Z22GcdCYgTZgdiTTMw3mM4W0Bkq2CbbrsbKG4MhKaZ1LZ7qEjyLltlPoThWw6oX92ksIb2G5ugKZudO7h0w24N7zrKRwjjTjYh2uRk1VPjyuaaTqsdyfQ6J0MN3XCQSssulu0GBp9NUfkUScscrNAErX13pS_duYvI5AY72tTGzUKSpyjqJTcGYaPAseXXL6batCUVCZ33mO90LYf4TdAD0DOjFNgEbB-1sZgb48ZXtTxdMXrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nYAnoP4fU5Nn8994Vpl5q_qJAlu--ttk_4j2eCzibaApPENFjrgy_W79A2DcpaZr_YAMwvx0lwv9d3A7Xa8MSOpGog39t0_gtNc1Z22GcdCYgTZgdiTTMw3mM4W0Bkq2CbbrsbKG4MhKaZ1LZ7qEjyLltlPoThWw6oX92ksIb2G5ugKZudO7h0w24N7zrKRwjjTjYh2uRk1VPjyuaaTqsdyfQ6J0MN3XCQSssulu0GBp9NUfkUScscrNAErX13pS_duYvI5AY72tTGzUKSpyjqJTcGYaPAseXXL6batCUVCZ33mO90LYf4TdAD0DOjFNgEbB-1sZgb48ZXtTxdMXrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7lHuaZmFDfCDZwdDHvrolF34zyR1qF7_NCzaxrP6q6u_BCfquJnlrQeKt5XIXbm8pgIc9QG-rGzxbiNCi-MGtiDZv2gk8A-bz74ERw0tvfhXvRS4y7coLnGlT7TG7XLSe8OsWEROYuebPxEnTbEeo5fXlAtOpbW6VCNUrcxE11M_10unZxdV-u_jvLDuqy3j-n5S6T4EvHYc-IyJwebt0HwRrwRMtFeH-rjKK9VJ_Nhrr1NtAqHaYDTImDhRWMEUQL3NiiEIyHmjEb3RQAGnE1zZW-eSwbtZwxumQ1EDMBy8UR2SH2j4fvCX-S5FcF7BUFYa16vgaSd0PjZ4_8o6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=HSt3X5Y4sTVV46fJjf2vetMx0nHt9WLYNzjTWJz8lmzZw7a8EJU2jUiFoFB6As8ugcSCUecWgNNCRMzd9AYpuVXFG3s7RcHNy6H4apuo9vw6sQaCa6g2LweFH3rX76c6uazSwZyYsTWmhkauUaRxAxsaofldZIrnLCi4C36D9ivulSRxhodz1Td1rsHeREeipIxfglJ3aYj6v81zDuvIIy3YD6ZutmfKZJuaY4RUhiKtnv44o6JXgamYuVJ1aDck5jtIUluz3c2lEbzS0Epj8SSVA6vyLI30mUPUhaSNY8EjgrXtJfnvxim2r0LydErlI34P4hCxluqeAV0wsAyqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=HSt3X5Y4sTVV46fJjf2vetMx0nHt9WLYNzjTWJz8lmzZw7a8EJU2jUiFoFB6As8ugcSCUecWgNNCRMzd9AYpuVXFG3s7RcHNy6H4apuo9vw6sQaCa6g2LweFH3rX76c6uazSwZyYsTWmhkauUaRxAxsaofldZIrnLCi4C36D9ivulSRxhodz1Td1rsHeREeipIxfglJ3aYj6v81zDuvIIy3YD6ZutmfKZJuaY4RUhiKtnv44o6JXgamYuVJ1aDck5jtIUluz3c2lEbzS0Epj8SSVA6vyLI30mUPUhaSNY8EjgrXtJfnvxim2r0LydErlI34P4hCxluqeAV0wsAyqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=jG9nKVI0QPKyXVd05HqAB-9mFj2tSj3dXDOxeZuJ3eUGi6aH0YBSj3HEjZIVDirR5TyRYXNpI8Hc4_-Y1ABC63ggyvODmrX3mdkfqmWG3xBSBBbqtd4JFYBhGwToWIalojdn8-hEY3WB1MFb5QBLHJhbpnAydRXxrVOreJKUAOcMlyAro8KLEWp34nnRDOX8BarwsjlqFPfTZ_ukpLvaiGNqrdCRkWSKTqaMCQFvlBe5P9x5h7gGFxH1eyH_f_9b2cSQfakg6wCpaDUzm_710DyZXfh1pdu4ebjmaKML5V_TvcHbdV8c3Wg3E2SdxhltxMtypfbZNBrN-eXTIaak3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=jG9nKVI0QPKyXVd05HqAB-9mFj2tSj3dXDOxeZuJ3eUGi6aH0YBSj3HEjZIVDirR5TyRYXNpI8Hc4_-Y1ABC63ggyvODmrX3mdkfqmWG3xBSBBbqtd4JFYBhGwToWIalojdn8-hEY3WB1MFb5QBLHJhbpnAydRXxrVOreJKUAOcMlyAro8KLEWp34nnRDOX8BarwsjlqFPfTZ_ukpLvaiGNqrdCRkWSKTqaMCQFvlBe5P9x5h7gGFxH1eyH_f_9b2cSQfakg6wCpaDUzm_710DyZXfh1pdu4ebjmaKML5V_TvcHbdV8c3Wg3E2SdxhltxMtypfbZNBrN-eXTIaak3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swo6y1vwMfRonjxlo9d4B81dNeby2vnBr4mMjTsy5HoE-9tEPK3WP9gMHAK6XZ_y1Pa-Z26-1DZnaKg5GYa3fzRiQxAIgjzNXIuJAO7RWe_MSpcPskgkpQybtBBZjIPZxrg_u4PiKHJevUtksCMt0sJsABX2K-g5Q5JAvvs58NsCriCJoUja-gLzHbp5ULSBAaO2R8x_yUrHfQ83THcQWjO6HGu7YPbL0YNSFZ4milyQavb-HjciljcGK2pLdDncXSshlg8AA_ECvV5actLmWkWIsAtslHEklGL5HsK5SGAeUnbOaenfp4po2t_HEw1-JXBNtcbMLarfnRxEXnK14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7aFP2oE7oRUxI33KSgv-t7_dARtc502uCnGF_VCzx285I6PYt-CLzGBcxXVBNQSlVwVu0Eu0jeCsV6MhnHkvvpPc-7AD0DYzrP18pkbdQZ_y95dYXtlDSsXLT8TbGDlrkT_ZOL6i_etm-ANY_ZK6ZAAjAGgDDUuA3xFjUzKEEnpJsbHec3hodO4zroZ1uD74lCSgY3tTPtntJx3z02D4L_pbJTTGHXI2nvzlp5TnELpsrHIyvs76665bGn60a6p8gyjcgiZJsMI8VUJmI7XTJySj8MQRQlTEuJd_3GBpT66CcZNaegv3QPHAAjPaznWbS3EpgiTYYtqtpW51WOGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=jl_cflDu0R2p4V97FrjvHe5-L90WU4StorxtE1fejDYyPpneRCFlmMyHde6T6-NFme2-lGXn4qBjFbyEM-Bb1d65lfBJmEMtE6SG8VYJjcOZK5IZlP9sDTYreB9p7on2CeupOCrNMqd7d_Ijr1xFNld1JAfcNbpW-bWIfRlMDqVjF2eAE4-cG9m89vPyZ3pjO32Fof5dm7hhhsQ2edCV2q-_2mopaZ4uzKFwotDhuPjhFj59XPvwR-kJPBGuVXtpmpen_MSiSmh7PteA-_Rc9t1KUKn295k83p1tBhWqz2joe7BE4fSN-xYGwxC9NOsE_ohoyRmFYuUsAEPd9rhKCkysJZy4vgr92MH7hMFepbywq4-hKhf11BDtM8vzHuGmktAf9RPJj_HyC-zuDL3vv3JgJsvDzYdE2sGVIxKF_C2rHMBilea6djbhjHEZ0lBi5KptgtrQQ2UxFrUxli6eabhaktVGqPsvi4MUADsPYT8zqNRoOdBv2Vb62ux2mj_6ensxKj8WzrAHfEeq2SFfV6RuSSwN4HYFDN4WXsaQAsgzcgp8NR-uxkqc7lbIXxLIBICjN-mXdyMQ33prhO3Yjzqog658omNKUWOedxFm5TDvAIuudo5XbUaKT_bW1JMtHySFRx1XQKWFl0eOD8j0uoQFXE5WqwIrIspHEU4LAzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=jl_cflDu0R2p4V97FrjvHe5-L90WU4StorxtE1fejDYyPpneRCFlmMyHde6T6-NFme2-lGXn4qBjFbyEM-Bb1d65lfBJmEMtE6SG8VYJjcOZK5IZlP9sDTYreB9p7on2CeupOCrNMqd7d_Ijr1xFNld1JAfcNbpW-bWIfRlMDqVjF2eAE4-cG9m89vPyZ3pjO32Fof5dm7hhhsQ2edCV2q-_2mopaZ4uzKFwotDhuPjhFj59XPvwR-kJPBGuVXtpmpen_MSiSmh7PteA-_Rc9t1KUKn295k83p1tBhWqz2joe7BE4fSN-xYGwxC9NOsE_ohoyRmFYuUsAEPd9rhKCkysJZy4vgr92MH7hMFepbywq4-hKhf11BDtM8vzHuGmktAf9RPJj_HyC-zuDL3vv3JgJsvDzYdE2sGVIxKF_C2rHMBilea6djbhjHEZ0lBi5KptgtrQQ2UxFrUxli6eabhaktVGqPsvi4MUADsPYT8zqNRoOdBv2Vb62ux2mj_6ensxKj8WzrAHfEeq2SFfV6RuSSwN4HYFDN4WXsaQAsgzcgp8NR-uxkqc7lbIXxLIBICjN-mXdyMQ33prhO3Yjzqog658omNKUWOedxFm5TDvAIuudo5XbUaKT_bW1JMtHySFRx1XQKWFl0eOD8j0uoQFXE5WqwIrIspHEU4LAzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOtRoVD4HLhfNw9VAk2k6hROxuv-v1uemLi8aMzmpayrfH6miiuN3j72Uk-h2jfhuI4Nr4wnL9PLSJM7ZzjDfruEQqBGFRQ80fdniK4f9rDpF9pQ58vamMonPaHYu94IHJrNEU9-emgRh6yDbjUDBMBwqmj-vcm2us11LsX-GuIm-voURS2XoUFglwh-SWIqeCweLnhO4U89lQ9vLFsawzVbIOWuAnOV--6LN6ndKxMfBSwzThaPC4aCMFiA-oVnwf_WV8s7mLmaC36Z1AWqLvpiPbAPozZlv3vAF99OcMn1Gv9hgi-ImPVTWCqr70rHc2xK_v57IeXfMKWalElNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=cETmQVx5hfIiKWRpMw17b_Mo1rK07xVti8IB1opUFZaGT5w0IBZ9fZdHMcV1tALVYfG62ON2NmYRIMG6xHH7N9nIgkGddViZrrjYRvkeK9f9S50FAbPAaJg2CI6KWK8z28YwJ_tOnvpwDJwGkjCO_8ZGZM7BCD0MNnDJb57MHsenr-yypkuwKW3GYfKh4eK5y2zkVdoYxcv6ON2KGoVhUedeovK7YCuD0L_kzEh03x0WweKjSsgdnLNYP55m8vMEWpQbtDJQ55e6H8BAEu5lv7Ski7vNV-Li0BXfXJJJQUA-zNtjRdhhuOcIxw1g3-qxA1ysbiUeIVDzQufQisb-T478fk3oOkS1_vGb9463F1rQg3JeFdJFhv6WVV25GP5-cX4MryQUKp-0mJJORKxarRxZmHt9bt5s70YeEiBjsQ2j8vk9E3Bl0r33II1hj27VZOptzsYjSqzAru_otifeT9-G2XLB2f1DYIh2ALFu3pgu9tVnsBwfsEZUhnCgiMbIthtPMdgJ_XOYc46hXgESHDrDzlJf3t4LsvzwBAFLWAQF1fJ7wjjO_nkX5nH-7TA54089fX3TytJDhYboYPVKP2ghMz3a92r10lvVmfLw4czHDRmPCXSsPMRoMrXiEno6AQwdjO-XA8moQgASOpIqU9p-QXXewTOu4lgMPIUNRG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=cETmQVx5hfIiKWRpMw17b_Mo1rK07xVti8IB1opUFZaGT5w0IBZ9fZdHMcV1tALVYfG62ON2NmYRIMG6xHH7N9nIgkGddViZrrjYRvkeK9f9S50FAbPAaJg2CI6KWK8z28YwJ_tOnvpwDJwGkjCO_8ZGZM7BCD0MNnDJb57MHsenr-yypkuwKW3GYfKh4eK5y2zkVdoYxcv6ON2KGoVhUedeovK7YCuD0L_kzEh03x0WweKjSsgdnLNYP55m8vMEWpQbtDJQ55e6H8BAEu5lv7Ski7vNV-Li0BXfXJJJQUA-zNtjRdhhuOcIxw1g3-qxA1ysbiUeIVDzQufQisb-T478fk3oOkS1_vGb9463F1rQg3JeFdJFhv6WVV25GP5-cX4MryQUKp-0mJJORKxarRxZmHt9bt5s70YeEiBjsQ2j8vk9E3Bl0r33II1hj27VZOptzsYjSqzAru_otifeT9-G2XLB2f1DYIh2ALFu3pgu9tVnsBwfsEZUhnCgiMbIthtPMdgJ_XOYc46hXgESHDrDzlJf3t4LsvzwBAFLWAQF1fJ7wjjO_nkX5nH-7TA54089fX3TytJDhYboYPVKP2ghMz3a92r10lvVmfLw4czHDRmPCXSsPMRoMrXiEno6AQwdjO-XA8moQgASOpIqU9p-QXXewTOu4lgMPIUNRG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1UNCd3bD-AkHf7GnpVrhaEulfNMKWue_fZ4dgtbHhSiPwLzvgrRlDzBsEOHFXrJ2M14ew7c5vGsAtwMR3zu0wrf_QJ0Ug1YwmGl7pAOrPY9H_VJaZ3JjhX_M24rCeXDeXGr-rqvgCtnWvXTx3Xjx1ljNYU8_e7u4_G8HJWw75nRUAwrr_n8ZKHkWim-YE6qDs3eQbaWiJj6dwvXsSRYfAthgwMHwcI6wNsY9PBrFNT4PkdrEAIzov_wumQc4it_1GCf6YBkg4Hfcf1E8LtJVQ4y5n2xuPtgKSiyZayKdWIRacewmdVErUhZ9TDwSsf1_ppzcIhpeneic1zcUpAkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfu2mRwresICJL1fbRfwngHXPJ5bQGdd83V3Bn10F3PpHiqJwbtM8vjjscBaSGS-2En1oPeMeEBNWlEjgOwGqNJj7Hhf7k43F6nqAyASEugojM1zogy9i5Oh6LEWcL3xBB-NV9Ohf8CC6Z-m4wgRXd0LG01R5yiQm_hSHk0fiB3PYtd8k01zvJzxOHxmAnHtvw5MRZ0awQtpL6jqNFu9bMfsMFk0xF6rfa5bTLC7rMnKS7uPtIlNLYjKJ9Yu65GXFcWG7Hpzb5yEoa76vsq6yIso49kn_8Lno7kbU6-Sbnvmi24jZlivj2INVbAWz-lX26G-YCDgaVgpwA7KRRHIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyXJhhnAVajpyQ2m9Ete8ve8JH01dKQ7Cd68McT8-CKQaZcYMR5ZCutHBkJPNc1hwfLTPEuoLNocGYYSJzlnRUhUavYWEEyAThFP-SPkGei63QGym7-tIckpIkNFhoAyS0JqAVKFNLGwCwJbgFPs-Va66vLkMzL9l7M0l67cOiLwhXzVnGQuclaFeWSmLlpnQp-DqE6grwugwRyIb8leYwCjRXUhk_BV9ZNxN5OvWmTdh4CFshKvtz2gIRPlUYkAyseBGrR8AgaejpWGho2KCGWXytc13R3lbZrz8wxPUhTDRVzokqCGjhwJtEn-k6x-fa2cmeeugBPL24sQgOtzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHwlTM-aa00J8ZBxpMvhJw5ZShvSInWzDPXnioraUCKEsMpH9U993o_11ioBsfQzNbfj8ybjbRLX-IzA0WQx9kOci00DBWHwN-dZ_P79GM6gmrcPMMkZElcFkBuY_p4ISY6halZAbYvrMa1Yiq3EOW_x3t-onb4p4Is-_dbdxJvIFr5AX3y0QckacEGa10Qpq87o01cATI4w5mb2tHEkZjCYi9FESbGIxqpsAIbs7pC1ULdmSInVa_CfNKPBE0NDpKMRwPZP4Ko2_3HRl6s3RL48MY9JrB87TWRmiB_b-lwN_42STFhW2d6QMZCf6QlnNyvZ_5HOZlnKEQQTK1p8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJXoilxZGxZQPjBhtBQujqEmrsI41R5Wk7g_HEaNMus6I7ENVpeUE9V71OcBfGmUF2zWgtEH3snbP6I2aCNIEGrTOS8X1_kRdb4nFOzDcsneZoyTzsAs6vVeOQUpZtt_JDQUaC6Ifg6SqNcIKLyHbXyk3UcI5n6KmHGdy5cuSWXUqnJ6EFAqL3hiF8_olmn5GII43uaagxnDeruQKwCy0_CoNqH0iYtjhDnfDTaeObfSJbPRESUhOsFnsfSZ2UC60nfqp9L36gVmFMG_5qjwcri05J9jTcYDctYoKx7ZCbMKxougwNbOxcEszSdwIHzAjMusT4hDhox1ipRLOzW-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J92ZBrjh4RbIlkNJruhmWR9gZarB1Pi8Im0Eo02XJKjh6JqHW4SbNJBw8kcbiAFCQtkl9EdrCi7jGTOnXREDoUCsf6GUfD6KThUdvFC_mLkWolyFtF4_P0NVh_63A8qv-POfh2J21PCj1LckVLHOqDBCp4thP5rVW7tCyaj0N79H9unaN4UY93k9vl1EJo1PVzCgqsRwaMox4712FjrgVg8BRiZw-I84LWqq3LSK5FMdXeD4PRUU-phPknCCVH0iS3W3DKGbxJ-hqjTGtB7qaLSLgjfuSTgRDJtNW43p5cj2lBXQmV_krsGVU379BYlVM5fa65dmSZmrSXUoV2q6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRlXaj4k8hxx0CjnP2AdMNbC2co5vQ7dKYmf3FZTrGSLBSYPYbWiSgzpk57e8ktn8iznK42P5rKIv8SMEl5R4_jQ54I5J9yWVCJmiXcSljAM69PCthSlgZ-bj-T6o60LZnkJlxC3juoxnXzCZ0RPrEK43AE6Dv6EjsPvZBzg-sU2kP2E3PAIaoCWs0O1gEiiXVtgg50hCo_gKJ11ZEYvG_WfNi-_w77Yxb2hTD7TT6d-YbLKdtvrp15MgCHMZFzpkm-iju2DopKIqfo8i1qtiKaBXH7YR30JxDJmZ8anN-kH00QcQpusQb1lhbdWUoj8Y_PbRNKmlY2fAmEIZDx9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQG_OJVIQxM6c2_a0yHCZ_FvLv21jXvqPZNQMVUTrSudKVYQHuru8Nx58Q6QtMC9GqA4Z11xIu5Cg3r_JGoy2OnBKJxOiV0Xlbz0INHnAVAIS9HxupI8Zhfcr2xV2zvooF8vpTIn6SrHrJ4OrrTAE6YevGeKe6yBMtZPMRbvmW7eDJfA-mdL-9_a7klCYUrdwHUGa2O-2lneOl8VkSm5cEz1u0RMiCwX2PKw-04vVUwAonG4QdlrNMpJdCZTCNWXz2VL7zj3khU-cA6tqoyZAVbd0Qa_paugdNeQBdi42OsD47nQNHzm0OxgWYU0v6BfDmGO0Sxiv4Z07upIi7nLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKGRklSe29Ypmb-X-34p3gyyWrUAemNeU-o_vhe8iXnKh59NJ7c4QoqwZbG-rV_w7nyYaAmytP6gp-ESDLSP7LbmkIeQaNmW73Y7C8afqchvCnLDkYQLs8p4pMAsxDc0epD17IRKgWhxDTSRjrmz4oFIEtd-mA2MBoJgMhvDY5GiJppKYMyADCSCZvMTXYeOw10yTeO1cU4y4jHrPYx5TXGjDBEPRN4BCGa2ZnknQXVJeNRIt4ARzcI96-l3KkmXgK1E_UZE3JUZkTJFzMFtqKCdCflBA4srB89w4Dl2GERnBNzRP_Cjq-sVeFseXWTK_0IeDcYxxawQIXwic0oBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
