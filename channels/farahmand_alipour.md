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
<img src="https://cdn4.telesco.pe/file/L6eANzg5E2ope30iE-H-ULCvd7G7wVWIzTloBYNqXcmq7zn-BobyVwCd0ZwAclmZtL_4gOq305cOK_MNfXllWc9Ghw-N5A-7QcSViJlWV32TqHyeaEgq8bzSO_VEmRmyYqaAbOdW_vCzZ-JcIb07rKRQLOFSjUuM5iS6zvwXmoMvJua5fn0wrpvSzoQ9IMvMi_pwZhmhqxKiIlhITFeABtp7aJT7qOuu73bYRJCtsrv958Q73_FuX_29Ohm1VrCwbsH7Y0Y0jWezT3ftlakOfIwZMVPTN-iDEDm_jFnCuG7Yl3sQV64eReV09A-6N68B1MZWsFNVBiZk5FFidrM78g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pialK1hk9HI2hstF9Bak8n6E24Whj9d9TY9oqsM3ZlOChJO8T5JClSiGEx8sM0ZbkgaSwZBljwne77_rkVaL6PG5maf9dsvVkCtEQFGzZxJRNExnNymIeaWCEGUxXjWjilHElaLgnKLYUeomOau7iUIkkYQG33exnYnW1j8rs0ps684fIcLFqje48DeOMgmFnN6HJtS-wXS2EjFto_rl5NEyOypP3nuWUE7GT9p_onMyz6SklOvuaBO1zmnlFqM6GJB5147mvItjtD2nJ367wB3yXDM9JirmJ-Zxo5B_IULXWHik0eA545yCEjx9aX-O4MD9uTuJBqDbjdBNzZVm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=GBbnwk_3cWViMDxug05O_NFc8GT1jGBNsh0sPfbmjcP8OZe0m9t-U3pERAlYi05wZu8XkLeBACG2HWN33A7zzpweQQldIxwJJ-BT3gpAleL6PywJrQ8Ag_pytiw-EmX_R8Yh3ZTFfPRMByOxgL5EGIhNfBTgYgB-FHOufVc4NWlr9VGtrjl42nS3QqxcO7UtNsoeFGceSlGB-gnaqkRI35XwF38g26NTfsjCCqQethEiZnRKzTbBzzFl99RXEF44hMOLiwQDFeFcBL11Yv1Oohfj7X8-VIt60zkYVt_ATJKtn6cqHwNF0Lv56VUcGEbzCfAcHAKTO0lBp50-8cA22ZdNHWJo6gEiQ2yd9YIGcXxzeh8CQgusZj-YKTwa3kmtd30kON0xFumeTPzn5qAZOAHl0Z4VEbeK0v_kERvDfewH1JBMYS3qEv_1qPwjan_dCp2fcRvnEIaOkfDdDZgR7ufxEXXXwSvgJHVzv3VKJ984PzC2GUlM3E8reAxaWwbmrjgEsotOhcsLb3llhPbO1Vcg3-5JqzEo0FptjtfdG2r9qpkuIh36O5O6B3uiIheY5tTAGqjHawYapeZaMxZapDJ2gyyWYecKIrXA6N6ZnhoMXdZRhfuaOIvNk0kxYPMZ2Y7JpH3bg2wXq70VYxcvWR7P1SvDZ0LGhcIk49OnMl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=GBbnwk_3cWViMDxug05O_NFc8GT1jGBNsh0sPfbmjcP8OZe0m9t-U3pERAlYi05wZu8XkLeBACG2HWN33A7zzpweQQldIxwJJ-BT3gpAleL6PywJrQ8Ag_pytiw-EmX_R8Yh3ZTFfPRMByOxgL5EGIhNfBTgYgB-FHOufVc4NWlr9VGtrjl42nS3QqxcO7UtNsoeFGceSlGB-gnaqkRI35XwF38g26NTfsjCCqQethEiZnRKzTbBzzFl99RXEF44hMOLiwQDFeFcBL11Yv1Oohfj7X8-VIt60zkYVt_ATJKtn6cqHwNF0Lv56VUcGEbzCfAcHAKTO0lBp50-8cA22ZdNHWJo6gEiQ2yd9YIGcXxzeh8CQgusZj-YKTwa3kmtd30kON0xFumeTPzn5qAZOAHl0Z4VEbeK0v_kERvDfewH1JBMYS3qEv_1qPwjan_dCp2fcRvnEIaOkfDdDZgR7ufxEXXXwSvgJHVzv3VKJ984PzC2GUlM3E8reAxaWwbmrjgEsotOhcsLb3llhPbO1Vcg3-5JqzEo0FptjtfdG2r9qpkuIh36O5O6B3uiIheY5tTAGqjHawYapeZaMxZapDJ2gyyWYecKIrXA6N6ZnhoMXdZRhfuaOIvNk0kxYPMZ2Y7JpH3bg2wXq70VYxcvWR7P1SvDZ0LGhcIk49OnMl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePD7R4akJNHgtADoLLrEGmggcBlHSCWonPMhTvzps1rXUU5QHyOhW7AEJU-wsoCKCUkneA0rIVGxQdV09hWNvoY_TGlJ5JscAuvtZwx_FjQPBCNolGMx4uy_2miPHn3C0he8F-Gdy5AhkwXxOAByaQgsQ6GpjfFXJ4p_LDkiDMTeeIU7FewLD761zzIK_nzdyGFUILhJoniqmXXl9-JDzIa8tRb9z7d-WDIwbk4RDxJ302fMiZ5dqD3kwvZ6QpD9-bgN2Xcb8y5ApKiAcjQ1GStsDV-1ajjMCVLCx40W1Q92zkQk43Tf-lPU9Wl2idMzPSEFegspk8Z5VfDYGxnJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahTgi4jsNM3S9IweY50s1VBGNfoHpiiZlJ1GG4UftA0KGr1gEJy8J-zr4MhwZ-xKyLYgzPjYRgkxJgtuXDJCLQYxnqjIsn6yowDqYlu7yIpsWs93Z5j-MppWVYNi8GMJOdoZUwlM-cSJHRx2JWfmljPzCP6Y7_8Mxf-yGHtVHEZWj0zfPgXUZc4Oe8QlqmovLr-ViaaCaqSe-U0ZoO4S2VTwtWyVXVxBnz3hdD7_r28_ydLtBIATwbt6qFTAlD_8jyV19w0aJzIN4o8ep0ZMIaiwXTfojX8gmDD66CPQP_35DRgUUfe0oDfTavWdnVLieTvkCe8yQYqlN3ctkyt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4fKtz9aVfS6J92jL69gAiGDLK-hG0_m_Du9Y2aq_OjI1YQUEsBqRGdm1rNOwFBZFWpQY1Qyvm18NDHceTCKgn5vRB_LWiExThmh8TkQ6f7cGwXIc-aV7YhrQUYgHJT6rRXHehEP-aosnmcK9z2Bvv71pt_Xo4wx00bpAcrgZJtPo7wcpRaT8tHOmL_hxZpB0EDZQiw6kS8u-hyX6BX-wc7CEDlEXqBbjNbOh0PP3ONGn0L_dX2hQCxkjgB4lBpL_qw7WhyPdfJ4-hxX9AGeowUnGHk2_5FwgXo1P50MSQ-8AyaqOF8R8aKCDxqcaNOzABPwBgoofO7RS3isGG6oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4HqklxJfku_mrrXqYQ1CIzBAaSAdMXnTBy2XWgsIZ8NLZpYhdYtn_0Ffil2ADCLPv5yaEQLKbn-1vkJRDS4nQJNYSdsJlnh_ev36mChCgcKMggsMDhaNSi_KyKQA5p675Mf9Pd3eDlUTcCJJrjAuHhTqAeN2sodFUvihxE92uuUigBTsTgyrn7CVmuUPICvqDNITQBDMw6q1IbVqcI929Dg08qTsuwE_3iEWeC3HwJWisRYmWud7z_-PoUxJEERLLbI7p2ycV6DFRuL4e_u_n1Xqj6u52voOKN9gn3d6a6uSPSnCmJZRekX9_iU6-6Fx0FKaWuLy2XRmpe9_Gjn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSh8XnVVJtqMeqBeoxSdMkzBP_9sBj26r_9c7BS5O8G50pjkEuePFJQs5eo_jZGjkFvKIoU3A7UhkGeML7_jHBDPg7_jYGZ8Ufy7LCfo_XN9HuwXrMHjrtDPwGs9MXLshAfn4KYhEYO1kIxBEObAKUfhEELYFiUPtJNNpWvfY7gOV2twztQrUqAcD94kxPXcBt7xKe_WTsTodQSqcx_OCm-dqyBoLnjbODXdqhZ1NK9XYaf7iuuLbOcDMECGn7ObWNXsGTAjXWhYWia_4xk0U5IylXiR64mEu7ObKRNND4F2k1Nyn2c7_NBzdCsKHWDQdngLx7rizzeCc7pYRja47g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUgyRuPHGfoBzNjz_qKV2ynpKmsOiKaDYcjLsTVVo8MQI0VqP0uRnyqfoDbmHADBRSVMQW4krTK4Avt-bHYhBn3rwQvEhCMMOtwm73H_EyzxX3MXo_oAPoAcWF9qC_BFuzFWVirrGe4HQo_6dMxdgLWM_a5IdPyFqbYBTYhaFko-G-mvJentcqXn3qnUR_ponLAuvlw2c95RnsorSuEJNWnNyy661Ev3OrnCSin44VR7goG6AYs5sI3PSZuTVo7Uk0Jmo0M7gcn95z0TJRJzJ-ZCqX3A68VmAQ_k1Updg-20aWhVXplP9t7TSeBQIPFMJWD_MzcE6B0-YLijBu3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m46TuP3PAp490yyTC_6e09TgZAx8XWoRcMECmbj6fcvYVRoeicLLevldZpWfnzBzyY4woizHV0xqr0FG4zfqtSoOZ4iLdrOrkLOXw79rp_1EZd-PyPvlw-0GqVJLZlQIvtRaRAMTlUHkVpbIKdfjXT42CvmUxKyPNp7YQa8L7gtI2aImBYzy3FM05CHdDZYei0B5Mf2meSKimT_160ytU_tTh0L9vL94IdqjyTmeMsUl_ybzBXveR2O3rEnX-aanuHjlN2dKwdIN0t_58qagDMn90noEcYuBuMa-vjw3PZRd6kUVBZk5DXPoVX_JBnNQm6gHPWbx69tyAohLzN79fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Q8TLDuR_9QfuBYQ9kFOZUJZSNNfY6iKlb_uq4V-tJ0L1L4fdEIiZkZMEOUM8QbLIzgV_ArVmNLkgxWfXOuAmKXsvn0dXmsz5TsKzjjubDKlmcfp09brXBBkEeZpjwbDisiuX_8AeJ2ZENVP6TKyTb3X-IRkPoDoUos2wOXZp_JbZnyJgrs_vWbNoE_KbYsqJtmrSQDToNNbYvg08nNAI8ALFq2OkFE4X6zJDAD8ZaoUdzEBjPlrBKSCXGXkNPJhb42rRQsSOI3e6hrP0sdwPYlxFr06TRyXXLq1rGd6irUNI57YGRXCboWl3Q5lOW-3QKHNCydQuFSUlFTWw00j6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Q8TLDuR_9QfuBYQ9kFOZUJZSNNfY6iKlb_uq4V-tJ0L1L4fdEIiZkZMEOUM8QbLIzgV_ArVmNLkgxWfXOuAmKXsvn0dXmsz5TsKzjjubDKlmcfp09brXBBkEeZpjwbDisiuX_8AeJ2ZENVP6TKyTb3X-IRkPoDoUos2wOXZp_JbZnyJgrs_vWbNoE_KbYsqJtmrSQDToNNbYvg08nNAI8ALFq2OkFE4X6zJDAD8ZaoUdzEBjPlrBKSCXGXkNPJhb42rRQsSOI3e6hrP0sdwPYlxFr06TRyXXLq1rGd6irUNI57YGRXCboWl3Q5lOW-3QKHNCydQuFSUlFTWw00j6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VbTSEL0KEGOq4JKiz2dNuodS1tatNKABjZVSCPzus3UiUe_pwpn796JAeVzpnc-9e0DFUT287ZbwnEIk5Ke30dVQVOCywf_7xE7pA1DpxKUH3_uWkJ9o9fSw2izgRqZ-pLF8pSmVEnnaZ-cD1YM3lZ7m2mkaDdP2fpeJLzridHdxc6LwEsRv5VoLfx71rko5CwJ-jrrYZWTL2dcgia-ZFUWEHVjIuDdQ9q1Nn3CzuGeWyeELNj8oqzv487WrcDJ-lIJZFci_0bq7eyrOjFsMHfw4a0T_kt8KPMMsZhIfBgMlfOpGSObQkyuJhAhi2tUxbe50cgQYMn8XAbFnwzpWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VbTSEL0KEGOq4JKiz2dNuodS1tatNKABjZVSCPzus3UiUe_pwpn796JAeVzpnc-9e0DFUT287ZbwnEIk5Ke30dVQVOCywf_7xE7pA1DpxKUH3_uWkJ9o9fSw2izgRqZ-pLF8pSmVEnnaZ-cD1YM3lZ7m2mkaDdP2fpeJLzridHdxc6LwEsRv5VoLfx71rko5CwJ-jrrYZWTL2dcgia-ZFUWEHVjIuDdQ9q1Nn3CzuGeWyeELNj8oqzv487WrcDJ-lIJZFci_0bq7eyrOjFsMHfw4a0T_kt8KPMMsZhIfBgMlfOpGSObQkyuJhAhi2tUxbe50cgQYMn8XAbFnwzpWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=YQ9jhX0V4au9-TB6KT3K4pvFzY1tcwrxAtDJX0NqILQbptdycHmCb8LXgP-sHrDVWXo1FKFTm3yjypmszMUmG8idcz28hg5ZqQa2cMbj32rSuAQpr9Od2XXxA1ye7t6jBG02-A5kQK0Txv6JEvcZRV60r8meCJWZ1ToZePNeah8h4jWC80J3dRYv-8g_dpq7KzJZbSrzCsbg5hFEAw64Dnvrr6ER61ezDTbialkyVzquQR4BkqDVkhfiJZyKLjfq0lq6pW_DYXmIX2P0nh6uN3ltkvkjlGd67urc5Q1z-Lv8_aozFZke9mlU91wZwQYxnr6IWyyp66b-BU0o9NhGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=YQ9jhX0V4au9-TB6KT3K4pvFzY1tcwrxAtDJX0NqILQbptdycHmCb8LXgP-sHrDVWXo1FKFTm3yjypmszMUmG8idcz28hg5ZqQa2cMbj32rSuAQpr9Od2XXxA1ye7t6jBG02-A5kQK0Txv6JEvcZRV60r8meCJWZ1ToZePNeah8h4jWC80J3dRYv-8g_dpq7KzJZbSrzCsbg5hFEAw64Dnvrr6ER61ezDTbialkyVzquQR4BkqDVkhfiJZyKLjfq0lq6pW_DYXmIX2P0nh6uN3ltkvkjlGd67urc5Q1z-Lv8_aozFZke9mlU91wZwQYxnr6IWyyp66b-BU0o9NhGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-4utLnC0vn9T_cJEj_gr5lkZIrySIBL8l9JUXN8-NUQAMdI1AhsUfcuYRyCxfkg7_HpMIVF2V_4N0CUwi4CKIHr_HVZro2E55GipR_Kf_7K-pd698twgnunPv0DS6pkl1uv8iWgCUMbWhbIZPVl4k-serSV3VT4BzhEr0JSPNHd4jz-nhs7sJwps8fg5b5Y8OgkS9QxADJjIyKl9ZrzT82_41yXqfK2gp9O_AsIZVsnQtcnXzUz2phLRg33sozycvVxdUjfsMbrfhPtJOJTop5H0LlbbFKEKNhr3U3DieVJ3yNnAgXIJxyWcmh5tE5BY4mPTFQrbMtjbJygOep_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=biW8_AUWUbGRNbAVD-6BkeqYQeZPJ9YJixY4HCSUuoVegWm74Te2I2e0bD7m25b3ATE0GReEcxaqvy4TIZT58ZslinMzLlpTxM-hgopDGOggoTWRiiCsV8pYhDSHk7VwFAi3VkXTRy1niJIn5BnJ0FMdaLohsIUe9n2q_OaJCitL57JVfEv4gbpIeOWUTIANB-el7BepaEt-eSGHuEwkAWZBkUarU_PN8pU_OiPWZu9mVgneYCZrUsqMhTTSigvbQNsWeFmzC0dZNQJ02AdZGXiQGtOFOXKWa8-DHIclS_L_a7nE3FQ4m0Wwmu_6UYgCsrXH9nFpfJQ2YpAtB8CmKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=biW8_AUWUbGRNbAVD-6BkeqYQeZPJ9YJixY4HCSUuoVegWm74Te2I2e0bD7m25b3ATE0GReEcxaqvy4TIZT58ZslinMzLlpTxM-hgopDGOggoTWRiiCsV8pYhDSHk7VwFAi3VkXTRy1niJIn5BnJ0FMdaLohsIUe9n2q_OaJCitL57JVfEv4gbpIeOWUTIANB-el7BepaEt-eSGHuEwkAWZBkUarU_PN8pU_OiPWZu9mVgneYCZrUsqMhTTSigvbQNsWeFmzC0dZNQJ02AdZGXiQGtOFOXKWa8-DHIclS_L_a7nE3FQ4m0Wwmu_6UYgCsrXH9nFpfJQ2YpAtB8CmKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrZfSGxq-DlYIAGS5WHG7dZ6g-ieMOhzuGWb5ILTNhYVb1g1ZZUJR45QdKku61n2STsYQGzpOApdJMb4DmGU8BCXvr3YfL4WA2WJyM_zmm1sW9x3U3bziDfW_gJ8rSbhLu34aZa6QTKCnKW3i8D6hMbKSGXpFzz2_zTdW5RZe-SjHf9KqYGHhaK69QM-2FEod1W9qneq4SP6ZE76mvBZ2Z4Y6_AgDZHds_8lswa94AWg7NthXvJfcdo-tnZolAbtdEe2cRxmaTozQi9685DKPYtaPtrdk4rSC5t37X4kQJLOQWBZ-c__qemL6uvjly477AljYLRxCGcC3_0V6NvfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahXl0UIEsm6XW7spbrpApm0gdhOhuPLM4tBj0EoQx1F1QDyS98UPSzRjdbPYuQXMdBmqrzJCdvHrv9ZbNRywcfzLxwow2ujMYncUE7hrzZ5zaWhgLvwJ7k60RbCXhGvJixGPnPOutEeYgQe_6cHrJBG4pLkv10MJkTd_Ljsl5u0ndyuWep8etx2d6qp9o-763aA0w_PSWJ9k-m035kvC2Bu0xObIdxOj5Mea-bFNwFCGDMCcRQlOKysjpBxQb1crpui0ECxx5N17gjqPqClodVaaa_PK9w70hciLYSyqKkyJZuUlNjEtsR_Z0-QDVycyeJx0K7OzQkcr6O6MtvFFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Y8U8B4K0XfiYOU95LY-7vRNFehn_6Sa-W8vXdjAnmeKhfMcXypXaY_lQLlViW_0_0g65zOW4AZu_nx0r-6aJLshHO6HNdqrNq8J9-5EUPkNxdrpsBI_YiTTEK8qgvtXGnFXH89BGjvoy7EyskRR3Bg2yYUViqvSWjqLRAPdAI_mM46NI3N4eEQ31_6UVcdlSAWl2c5V4h6CCYNrQsCQ6mDsWAbYBUVSxsAjofucywtECKQipS0An7647agjwA_OwJYVON25yjCuqiYM91m9wCaV_9jU6QK_1FX9SukOKscWZR0f7vFhx8dQ7oLG1ENpT9KHZ1E-weNRQzcfr9VsUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Y8U8B4K0XfiYOU95LY-7vRNFehn_6Sa-W8vXdjAnmeKhfMcXypXaY_lQLlViW_0_0g65zOW4AZu_nx0r-6aJLshHO6HNdqrNq8J9-5EUPkNxdrpsBI_YiTTEK8qgvtXGnFXH89BGjvoy7EyskRR3Bg2yYUViqvSWjqLRAPdAI_mM46NI3N4eEQ31_6UVcdlSAWl2c5V4h6CCYNrQsCQ6mDsWAbYBUVSxsAjofucywtECKQipS0An7647agjwA_OwJYVON25yjCuqiYM91m9wCaV_9jU6QK_1FX9SukOKscWZR0f7vFhx8dQ7oLG1ENpT9KHZ1E-weNRQzcfr9VsUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lO1foepZVKkaJA-CRRe06Mbv2a8Q3N--eAiJ7uorxB0Zw4ToLhXs_7Rs5GXPsKBPJzVkFB7Zoa6HYv-iiYyDkNt8R_0tvTk30NORHpLHegFZbhSAXV7gbcvOIlm-DPYxNtL8XFtEoop4oWMhoFxTrp2hlIzEsn-h7K4slAohkIxYLHgTS-fvOyilNwRy1HISiaOxj3Vt9ZS6BvkxTX8BJJUchXvYCvkYxmobjcdl6jAth2tkpGUNAhSCF7z5jYsTnWnYX8H_6kZPRPh1ONrzz7QzvxJv4WwAFqfDhHSldNQYmihVSsziMOl_j28Utpt_P98qG9yYJaKBGIfIePYJ9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lO1foepZVKkaJA-CRRe06Mbv2a8Q3N--eAiJ7uorxB0Zw4ToLhXs_7Rs5GXPsKBPJzVkFB7Zoa6HYv-iiYyDkNt8R_0tvTk30NORHpLHegFZbhSAXV7gbcvOIlm-DPYxNtL8XFtEoop4oWMhoFxTrp2hlIzEsn-h7K4slAohkIxYLHgTS-fvOyilNwRy1HISiaOxj3Vt9ZS6BvkxTX8BJJUchXvYCvkYxmobjcdl6jAth2tkpGUNAhSCF7z5jYsTnWnYX8H_6kZPRPh1ONrzz7QzvxJv4WwAFqfDhHSldNQYmihVSsziMOl_j28Utpt_P98qG9yYJaKBGIfIePYJ9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=YIBckw7KOuzfJNyreRb5VOJbdRzsSfVwq0RqfbIfLkK9OFnJCEWQ6Eca-vLP6Mhn8FsL3Ib2slWrD6ZhDprQsbnb7SurroomWvCtxdrKhJVSGwadGxXqVyiosCVyYzGv6XKA8A0ZxDt9Rj1nQcchS4QgsabUEQpKKVlzxSYjRtfIUH-48BsoC-O_UnHqzCem2dbHJGS5Ywrbge2glOXJO8mVaU0keX6WS8Sbv9_-hvQ3ArJ-7JLmBNJAdEoSpuRnzFe5OcOHWsveg8_PYWQ0CHSiQZvoFd1VeoPBUMhOq7LRpfWUnPXvve8ZwR9P-X9JvsFx2Flt5e7rCs6y7cUiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=YIBckw7KOuzfJNyreRb5VOJbdRzsSfVwq0RqfbIfLkK9OFnJCEWQ6Eca-vLP6Mhn8FsL3Ib2slWrD6ZhDprQsbnb7SurroomWvCtxdrKhJVSGwadGxXqVyiosCVyYzGv6XKA8A0ZxDt9Rj1nQcchS4QgsabUEQpKKVlzxSYjRtfIUH-48BsoC-O_UnHqzCem2dbHJGS5Ywrbge2glOXJO8mVaU0keX6WS8Sbv9_-hvQ3ArJ-7JLmBNJAdEoSpuRnzFe5OcOHWsveg8_PYWQ0CHSiQZvoFd1VeoPBUMhOq7LRpfWUnPXvve8ZwR9P-X9JvsFx2Flt5e7rCs6y7cUiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2q-KbLJtiz1R2fTz1EpIuTZqCBRCg49a_EJBC5VjA9h4cDRKs8qoF_SeSyHReA6uRft4v7XxD5ZDqrnvj0Mg5T4tGdInwP6Jyboygdajf-H8v4Cq5Bu-5l9GOoFgZr9H-y8vFCTqqSISX2J-ZO7J8MN93eNWAFGv-I_--nIijYwxJUFyk4I8opGqiVwv32_zNgZJWv3lu4YCL9BTb66zayjP2FCgHPIAKZVtQdNtPJd_tG1i90a1cQzpRKFrko1vam4-UR8Oorm60ClkvG00IaUofXf0XBnq4jbkf-shev-YpT4fS1NCVheuPmn3yRT4rs6rBSnEvsU8lMPncEKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=pc0KRpKzU1_Jy7b7uVg6bdMfgnXLWAF35WzDX9L4i7NmTephpaI5hnwH80-HHjjy0ra9Fn4Flpf_Ocmv_0uhAimpSrFuZIkScR3X-vkiV8k3d2U634dZ_3nXBXu36PGSIFppCKzcSouWXmtVjEnFYLaIE-G_eYis8aw9A6KeC2jGYeb90CI3HM-JGlOpF7j_tgOktwkRVq836nen30zyuQJdMODFU88iFrc4Sqqdm6YOsWl3oMZwpiOGXTykjXQUSYf-46WexQRzyJziNRJSfMa09OIJ9YA_jAMSDp2EWvde5UH-EKpxPTvf05bSGypq7nR5nHWD_SAPBa6gsiBsFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=pc0KRpKzU1_Jy7b7uVg6bdMfgnXLWAF35WzDX9L4i7NmTephpaI5hnwH80-HHjjy0ra9Fn4Flpf_Ocmv_0uhAimpSrFuZIkScR3X-vkiV8k3d2U634dZ_3nXBXu36PGSIFppCKzcSouWXmtVjEnFYLaIE-G_eYis8aw9A6KeC2jGYeb90CI3HM-JGlOpF7j_tgOktwkRVq836nen30zyuQJdMODFU88iFrc4Sqqdm6YOsWl3oMZwpiOGXTykjXQUSYf-46WexQRzyJziNRJSfMa09OIJ9YA_jAMSDp2EWvde5UH-EKpxPTvf05bSGypq7nR5nHWD_SAPBa6gsiBsFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=ILYYKVeuD7aEucfSkv11POzFnTR6yTWSlp4p0FLHTEAIR9spjFWGaLycPZiPUj4AyFOaRqzHCD0R2aIWXZyKV8a_ZnSoTZWtg-wCRunr8PyiBPal9jcK_v-_YMSj19baB_j0gHP_PCoLM8r4LNJ3gQn4TKwYuqxQxALcM6zY-ei6ZFOeSpi4jkK8CknCHBXsSoKRWjjX6uy4evFvEXyiRGbY9kDp_EEyYpQBBj2FLcV-JnH_tJH9aHN4OKdDIdMbeyJg19jAAInBs0XUMODOQ9xjw95HKciniuHr76EMU7q_fuX2GDp3Tid2bsE15PnF6mEAv7BN99Kb_74OysjBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=ILYYKVeuD7aEucfSkv11POzFnTR6yTWSlp4p0FLHTEAIR9spjFWGaLycPZiPUj4AyFOaRqzHCD0R2aIWXZyKV8a_ZnSoTZWtg-wCRunr8PyiBPal9jcK_v-_YMSj19baB_j0gHP_PCoLM8r4LNJ3gQn4TKwYuqxQxALcM6zY-ei6ZFOeSpi4jkK8CknCHBXsSoKRWjjX6uy4evFvEXyiRGbY9kDp_EEyYpQBBj2FLcV-JnH_tJH9aHN4OKdDIdMbeyJg19jAAInBs0XUMODOQ9xjw95HKciniuHr76EMU7q_fuX2GDp3Tid2bsE15PnF6mEAv7BN99Kb_74OysjBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=q_lAJxCUQcVye72d1iWb_-KZPH8tywGHNhnqXNnEMTNHgSjt-CxhqRNP9F9EOFGOOFSNfAROjqALCiN8-lwFMD_q16CHMLTSip4KArpRduEtxAMS-qvXJ3EDXRlK22aaBeO6Kp-xKh38KnnPdziAsgRwiaNFarpCGsmm6AT9pxH2nAyfNJkND4Dx05tADw1YsKax-1u-jdtiBhGl9dzsfAaHYNpJ0hXD1pTYcqux5LRUJUk-ooiAyzLWm_MiF3mAfxWV3CojTUQfneNSGFR4QNXKVsb0gWsO664PzPFFtq9yXPzxeAOqiqsIN7yd3Ej0dkwZROgCvsT4mCTfYrP4fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=q_lAJxCUQcVye72d1iWb_-KZPH8tywGHNhnqXNnEMTNHgSjt-CxhqRNP9F9EOFGOOFSNfAROjqALCiN8-lwFMD_q16CHMLTSip4KArpRduEtxAMS-qvXJ3EDXRlK22aaBeO6Kp-xKh38KnnPdziAsgRwiaNFarpCGsmm6AT9pxH2nAyfNJkND4Dx05tADw1YsKax-1u-jdtiBhGl9dzsfAaHYNpJ0hXD1pTYcqux5LRUJUk-ooiAyzLWm_MiF3mAfxWV3CojTUQfneNSGFR4QNXKVsb0gWsO664PzPFFtq9yXPzxeAOqiqsIN7yd3Ej0dkwZROgCvsT4mCTfYrP4fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=j5BY-IQ2I23CzLRm7mqzzs9XVKPL204TIt9-LaFM7_tw3c6TJ73ha5RMZGQ1vwzvmFJctkPNfAU3KIrQ_bHvHAZYEfuUpgWd-uyq2U9iDjs0I5FtbBq-IjBEQDX4pAGSsf76Owwl9KSY9R3pLWRhZ2w0ANvspkwA4Zw8HflL_SMxpAfxgTZ1nqCEFpzMOvs6gaCQ7_WBU18nhPz13_wgCZuCzpf1MvnQWtIn727vyz2PPDQVrUMM5K0tVyec_6xlz7pg_j4lOiGBIVa0Zdo6jLNrT64JSrNa4BKB_sWNAXyMGXxAKPPtcYkpqv1ZBW5MO-WVY-YVHML7lNK0_M_1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=j5BY-IQ2I23CzLRm7mqzzs9XVKPL204TIt9-LaFM7_tw3c6TJ73ha5RMZGQ1vwzvmFJctkPNfAU3KIrQ_bHvHAZYEfuUpgWd-uyq2U9iDjs0I5FtbBq-IjBEQDX4pAGSsf76Owwl9KSY9R3pLWRhZ2w0ANvspkwA4Zw8HflL_SMxpAfxgTZ1nqCEFpzMOvs6gaCQ7_WBU18nhPz13_wgCZuCzpf1MvnQWtIn727vyz2PPDQVrUMM5K0tVyec_6xlz7pg_j4lOiGBIVa0Zdo6jLNrT64JSrNa4BKB_sWNAXyMGXxAKPPtcYkpqv1ZBW5MO-WVY-YVHML7lNK0_M_1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRoUswMsrmJv82esQtWrCx2ezouKBR4WnvUPq6GvotlAM4IJ-je7Xt5X-WiUnKP1SyuOhIqrvsG_uAkkDqfH_4X9VoFtqYVIH_9RrLM5eMV0PUIMhoNFRKa8e-p6uDZBV3qxSKwSXxQLq8ziIMbfqdlSN0P1unYeZ_fqSUoCUsggIgOOvVUM8eeQG-hQpDkcOTRWzcBPrTyH_NOuOmh5NjRBaR8MAC27wsH3j6-h8ld5YHEfkXlmSWkZr-L2atNDZ7-t3Tl-y1ZbBxRf1uYFqz_T0yfQJIXTKQJ7SMxExhD2xYEU0kHSBa9VtjNdhAN1Hjuxs3cj2CZEEWVxFP_R6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=D7jbFUvxc5Pw6QaeGnx2PfSVOZ3UxmKj9lGKn5UieWsT-QmqcD2Ip80NjsdDt09ngLim1B-FFq3IOh_O_50FRcHxVOd-5hp2nqkFGNivcq0PGFIKZIw_ZUbMU-UouMNRlvcSaCa268F81jIWa0Evw3bsD7spGI4MTx5cONeCBq0WCtvxVBeC6qL53UpBVYGk_SLDa5xri9E4R373WalNoCHNkrnn2NFXKR6s_2W30sOyA-55yZwfTWLgs__pbreXmDBio71EfdzAo_26iY3HaH-oMujP-ViF2HiSnEbn5DAKS_73SfgInhxQW9JFw2zvnnZ__lyJoIDTENpD21mk5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=D7jbFUvxc5Pw6QaeGnx2PfSVOZ3UxmKj9lGKn5UieWsT-QmqcD2Ip80NjsdDt09ngLim1B-FFq3IOh_O_50FRcHxVOd-5hp2nqkFGNivcq0PGFIKZIw_ZUbMU-UouMNRlvcSaCa268F81jIWa0Evw3bsD7spGI4MTx5cONeCBq0WCtvxVBeC6qL53UpBVYGk_SLDa5xri9E4R373WalNoCHNkrnn2NFXKR6s_2W30sOyA-55yZwfTWLgs__pbreXmDBio71EfdzAo_26iY3HaH-oMujP-ViF2HiSnEbn5DAKS_73SfgInhxQW9JFw2zvnnZ__lyJoIDTENpD21mk5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=m2X_p0FddkYsxz_mEoqDdcYjFI2LmcOg_JTBZvtPHi9N408CTJHJ0t0VVAnMv5rvDfvGn2DSaBvfQ47406qG_LYwl0X8JytoqAEoPMPiAZHdBRVcIYc5xaA-kbszoHeev3cFVjsfGdFWmAUxZNQR8MwCDODyWc_7bgLvV8ldaCQXYxZ-NOJCpfy_uF7bN0niFPqGzUE7h3Gc1YlXrHRKh6YQydQDPzIm7CjMqsKp6Gitan0bB-Elz0elSfiQZTWSnUX6TDtrKZ4phsz5zo2jUQb0qQXwItnPn-u4Ciw5suGYsSOKTRgwM5s8zC3pa2Pjf3yFkxRtNzrOXQdjS6fVTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=m2X_p0FddkYsxz_mEoqDdcYjFI2LmcOg_JTBZvtPHi9N408CTJHJ0t0VVAnMv5rvDfvGn2DSaBvfQ47406qG_LYwl0X8JytoqAEoPMPiAZHdBRVcIYc5xaA-kbszoHeev3cFVjsfGdFWmAUxZNQR8MwCDODyWc_7bgLvV8ldaCQXYxZ-NOJCpfy_uF7bN0niFPqGzUE7h3Gc1YlXrHRKh6YQydQDPzIm7CjMqsKp6Gitan0bB-Elz0elSfiQZTWSnUX6TDtrKZ4phsz5zo2jUQb0qQXwItnPn-u4Ciw5suGYsSOKTRgwM5s8zC3pa2Pjf3yFkxRtNzrOXQdjS6fVTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvtKgXCdfmLO5mb7nUp6MbtLMkWR0lxnhMvZhflo5fZPITBWzZ3EclkWb_FIW2xxLXL-kMEVCwFpTPQuZxueIkS20mp3weQ_GLdHi4Yu_Zux8Kq1SnATMXB3pbFZxlxq-rEh2_FkocryynB5gRAm3noLcRRnGazGAcL68zCSLg3PfvvERr_P-iiqolwGnqu88zR38lK7A_GG32qGNDfC2HIZT90R53qZti0WYhzAjXQWlQoAuX_ZzVM7yERO6zRFkkLxCYtKbVmkiNhXoemG4KY7HvioVem17epuTmD4h9nV64OxrRcqXU6ugVUY4UjOmOUMEZQkDtyjSpmo64RHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=GXipnaPbGx_x28tNgYxcQk38-6yq-qt7Ldom6TIk8pc67WTR3WQ25XfukYxrxiJz8b5KaePlTOF87kT6tcQHlm41UJmJ5P4MTwod_BBeZ3UdHb4-ULnXmr2v-xo-PR-S2Eh8nSP9gHrJppC23fYAIMaeSLk_FDkKtZFTz2bn08nxztiUpUOfHjpOPost0dM_C82VgyDXrhSVAUmulMpzboJviQ6rBoHE7l4e8OSuE1rWjFKpWxAQi6SDb-XON8HHmiRWSucBR3-Vuk7glZWc6pq5oYtT8j0bzteiBL31onl2NW2gLeHD_cgJqIAdvo4-mYw7KvOyO-NEA4vvxOO0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=GXipnaPbGx_x28tNgYxcQk38-6yq-qt7Ldom6TIk8pc67WTR3WQ25XfukYxrxiJz8b5KaePlTOF87kT6tcQHlm41UJmJ5P4MTwod_BBeZ3UdHb4-ULnXmr2v-xo-PR-S2Eh8nSP9gHrJppC23fYAIMaeSLk_FDkKtZFTz2bn08nxztiUpUOfHjpOPost0dM_C82VgyDXrhSVAUmulMpzboJviQ6rBoHE7l4e8OSuE1rWjFKpWxAQi6SDb-XON8HHmiRWSucBR3-Vuk7glZWc6pq5oYtT8j0bzteiBL31onl2NW2gLeHD_cgJqIAdvo4-mYw7KvOyO-NEA4vvxOO0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=osYbfPTToYGoM5UPZEaHBAKKcHpXhdt2N3fSSA-3HnFyb4rlT0eT7yHy411SMvT14yYLfogeFCwXpudzp2ly5cyVaSevU-pNx15JF3dASQ-cddgazurzvv7yIWUr1obFaJLvbpFs9LjUyi14M4vWRkHdooS3r_yrC6Y4d6CEF-Afscjdt9LcstBbpIqKyUQn5ehpNN3ar9iORWD9KOUunoNlsgkgOv6UbyXCT-TjVCbyiP6SaLoU8ufK5iWLVRvUQVQv0b7nbsP0kxymbgoAF5-IsSRsbUUuCOGJe-QngPHcF73C3HE6uWfGmTb4NEJmoHXdIu0uh60Re_4EfPDB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=osYbfPTToYGoM5UPZEaHBAKKcHpXhdt2N3fSSA-3HnFyb4rlT0eT7yHy411SMvT14yYLfogeFCwXpudzp2ly5cyVaSevU-pNx15JF3dASQ-cddgazurzvv7yIWUr1obFaJLvbpFs9LjUyi14M4vWRkHdooS3r_yrC6Y4d6CEF-Afscjdt9LcstBbpIqKyUQn5ehpNN3ar9iORWD9KOUunoNlsgkgOv6UbyXCT-TjVCbyiP6SaLoU8ufK5iWLVRvUQVQv0b7nbsP0kxymbgoAF5-IsSRsbUUuCOGJe-QngPHcF73C3HE6uWfGmTb4NEJmoHXdIu0uh60Re_4EfPDB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=jD0MOjuUhxE3iUgjj_hrAYlgmFP6vS71TanVmbltyDaO-2iml4qGEktgUChw5wLPgt488LpWwSbW5AND4p0etuWwEYxFEFmou7HcnWXF6M5K-G5WSzn4uXAEcw0mntlr3kXtnWXFSewXejrUQC13Hh6w0i-4m8GhdN2flx51flfQB-9KP6mJ6PbioRYzcnxMO062mo84doqQ479f0pDbS2yBgUE6xPeQEpjoxmq-lT5Rcddpg-bUwYymjjn2KIFOWc9NRQ6Q_BYIu5AyMpJ9qRFIuyBKAM230NcqTGjbv5k508bpuPF9wga8oTI9GWGIzjDnrAQ1gQ8kTdDB9i463zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=jD0MOjuUhxE3iUgjj_hrAYlgmFP6vS71TanVmbltyDaO-2iml4qGEktgUChw5wLPgt488LpWwSbW5AND4p0etuWwEYxFEFmou7HcnWXF6M5K-G5WSzn4uXAEcw0mntlr3kXtnWXFSewXejrUQC13Hh6w0i-4m8GhdN2flx51flfQB-9KP6mJ6PbioRYzcnxMO062mo84doqQ479f0pDbS2yBgUE6xPeQEpjoxmq-lT5Rcddpg-bUwYymjjn2KIFOWc9NRQ6Q_BYIu5AyMpJ9qRFIuyBKAM230NcqTGjbv5k508bpuPF9wga8oTI9GWGIzjDnrAQ1gQ8kTdDB9i463zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFnPcViDHcs34NUO3NnzJ4Ux9ZmaqTqaJi8ujqxwUzGWkDLprmsM89z47EmQK0CMplpQFqcHRD1Ti9HXmgW2qT5BSUWJpzG72RMzB2kqW2DpC24Vbk0ISedyF3AwcdzinwlSHQ-GKxjnHnypRQFUOZcz2wqzxhO4hIFNHvhABxXx7iuBDGvSEQw8t0L2BsHINOdhQrT_ffx7Ipo_Oi4V9M8s4NI6OpDerOjrvdiGL6sXnSEWABC0VD8Tx3iEoPf-aXkEkr4kaK_iXCdj4nbFyFucxLNsO15zLmaXOO6BHNXlt-XDa2eYl7xHy-jb_vAFVFEwF3gseeCJGXgPj92TBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxjDGJ16oCmho3Wj0seEWlf0YxJNSFgJLSIxP8wN8ipvfefFcnOwrdtoTqvRe87OEQB2HMkH_dKKi787XnDZFxX1G2ZVNy0E5BvhJp9zIFM-6zW33dE6c49vh6GxAM4KC31yU5Hw8A4I0fln1GiIAjJRDWPMDFztfRMMrIhUoryYGy5uKKLMv5WgmsG88ff9QmhRGLCEF4uBdx_p599fl_Nsbup_RojLcH2MViDh0oAHTXOwou-UG3vTyiPxg7GO7HFj8MBWKAiYmifTaBKhASY-_5QlWjAwY9gXBspF4biCwAUflghqK75JXKY4siMjeRxiMQF50UDdZZzFtuW_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GaIluQR9UhssTum_J6wZzClG7-1nhiN7qeyxmWVUN6ONLodvfyLn3ahU91vXcO4e_o54cf4f9zXlCgTLA9kBp2M1p-1Mf3405cQYNoaqKdJJ1X9eUMfIkHeJtmile2ID1-SnOSHmyCplfQ59ta0i-IjaraNwmNz6P8xFeIeatrj4QTnEUEIIjUqNq_kHNs4RRpISuwlyq5GZWw-mY38bRYQgGkTC4nsEgW4GDvsvFmrWZLnzdOTO2GVEe2GEysnpz_lwwDTE41--OUGGu2pytlY0H6RwfwUHZY1F_MiNnImzKCOiYGqQHUDhoT_Ce5PhADhfAOm_9dnWTz8HWsWOfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=VhbPod3fFsFxBVYTDzK_832vG2K6mTlDScCC3oP5rosyse8HrRsUrRH3o-XiznGY0twhjo6x4R_-GTw5NhCZkh0a0trAkZHmWORem0XTWJo0dDvoyYxzuRbPeMS8nJohabQUp1y6UsAYwptdjqqukdqTrTj2Nb4_39wHvL6y5giQnY_lmH0-gwXFC_Fu2yxS2n1wQVTnsc5DXsEELMZALXO6h-7s9O2zjbnU97-eXV89UxNT6z1Gl8L5hsaKGZe_atRUl01bpPf7JVVYiuEKmAg8znwczDD_44qc09OFbAuMKpp_z9GOt_3dPalMzWm2jucJB0aIDgsjysJzSyQ2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=VhbPod3fFsFxBVYTDzK_832vG2K6mTlDScCC3oP5rosyse8HrRsUrRH3o-XiznGY0twhjo6x4R_-GTw5NhCZkh0a0trAkZHmWORem0XTWJo0dDvoyYxzuRbPeMS8nJohabQUp1y6UsAYwptdjqqukdqTrTj2Nb4_39wHvL6y5giQnY_lmH0-gwXFC_Fu2yxS2n1wQVTnsc5DXsEELMZALXO6h-7s9O2zjbnU97-eXV89UxNT6z1Gl8L5hsaKGZe_atRUl01bpPf7JVVYiuEKmAg8znwczDD_44qc09OFbAuMKpp_z9GOt_3dPalMzWm2jucJB0aIDgsjysJzSyQ2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUEKb5VddPG-jtv6_4qXTPYxbfXD2v5C9miqPUsUwNvPEKqQtgvuikU5Pz1tFeUJEpLL8mqfxIi2RW1o8e_RaUF1T3pUl1ox8jQ5QS087GHoGtdaVsQju8yVfonvMwyge3dx8Rj-Oa9jozN1CiD3duQFI8zGvZMpZLz4YiGcog0zUsziO1vuncU2LvJ5zjamwgqCHDbfCD1ZbW7NiuMJ8LVR3QKDrJHk8ykUJFe4lZ3ctgB3tnSjwMkJY46YyESKiqw5sIrTf0I0s6sTsKfXkB9sCaBmIT6eOVKBzjXZzSIKObDl5eD81eh0Vtnv63eqyP9_J4J7676Jymx55F7iNe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUEKb5VddPG-jtv6_4qXTPYxbfXD2v5C9miqPUsUwNvPEKqQtgvuikU5Pz1tFeUJEpLL8mqfxIi2RW1o8e_RaUF1T3pUl1ox8jQ5QS087GHoGtdaVsQju8yVfonvMwyge3dx8Rj-Oa9jozN1CiD3duQFI8zGvZMpZLz4YiGcog0zUsziO1vuncU2LvJ5zjamwgqCHDbfCD1ZbW7NiuMJ8LVR3QKDrJHk8ykUJFe4lZ3ctgB3tnSjwMkJY46YyESKiqw5sIrTf0I0s6sTsKfXkB9sCaBmIT6eOVKBzjXZzSIKObDl5eD81eh0Vtnv63eqyP9_J4J7676Jymx55F7iNe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=M4dcz4HkeerckBy3-s5OGdnoHAEfqv-ziBh0jbjAgDWMqJUhwZZicAcnav34MIMr3pZhtp0WH08XXtVGTXccDHW9ty2slN6cCtNJmabTqmOAqfF2Q9WoRYCrxwiweR54XJA_uzMF_YxTNp4Mf98i0EJuRybgdPeAiIPW2vcllo4K_PLlIbQPqv3tjaJWd98XNcedJGrQvl8etbB0wnKn9Nliy5RdNEgxnTRmNf-NyiY1yy7Qp3H6Br0YdBJT71O_ziDtvmkkrGA85fRsFuGtvNBUVyouV4cb6Ds60KL5BWkSJYmGhi1CSf9A5vJ8h5-KJZNK_3FYDHrE21uI3WGUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=M4dcz4HkeerckBy3-s5OGdnoHAEfqv-ziBh0jbjAgDWMqJUhwZZicAcnav34MIMr3pZhtp0WH08XXtVGTXccDHW9ty2slN6cCtNJmabTqmOAqfF2Q9WoRYCrxwiweR54XJA_uzMF_YxTNp4Mf98i0EJuRybgdPeAiIPW2vcllo4K_PLlIbQPqv3tjaJWd98XNcedJGrQvl8etbB0wnKn9Nliy5RdNEgxnTRmNf-NyiY1yy7Qp3H6Br0YdBJT71O_ziDtvmkkrGA85fRsFuGtvNBUVyouV4cb6Ds60KL5BWkSJYmGhi1CSf9A5vJ8h5-KJZNK_3FYDHrE21uI3WGUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_lTPLEHmCCnaMtreoTuIvkQJKQsw3DrhR4OJlGTR14ATXiF7JsYj6asjyS58o9VLQ7RdLId9KSbfil36CwJLd9athmUsCwNRaU0UbHBBCj3ylSHfjXc-jb4zmydRluMdltJp661zUSoBpGZHuygK36B-t60sh-9vyWfpbByjA9cGRICt4GzgvbkqZ-9z0GXwEwJ-pxy6q3bl2HaApW5R2VptQxmPDtCM6a8xWvQc6LFgN_koXrGO9hTITePkkGjKs5wuIusKLCnpXFYQ9INlYznHRO2qMeQUOXCR0WdAuGnHfD54Rqvs4ymzuuZFeujqBlzACfDHx84yOXpbvWisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTkpb7dj1MAuH4_rJg2apMT_crBXKtrLWegvKUrE66aXCSQhGk5XavSqQrHuD0Hg5H4afgjEG9CiVHUJkN0nqa5erjq1SB7IvcIjKE2kDnOZGAMffNrehzIxXIAVuB2zFCdDvqEHhfZrFIVCyA-1m0ysL8vL-uNLpjxIyLA7zOwhbpgloJSgSrtgCEBUr2G4ApFfTqpgiKtmDHYWfrBuPVZaaCp_tFBjQcb17zjM7FqPxUADURPBSrTJ5qllsWyha3PzxVN1Gsod9jK2ECJmAUwmv5eJXi5Vw4jscizW2QwViFJy26CyfrE9fJfJCOp-i--UC0QWvOkXwvoaifxqlsSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTkpb7dj1MAuH4_rJg2apMT_crBXKtrLWegvKUrE66aXCSQhGk5XavSqQrHuD0Hg5H4afgjEG9CiVHUJkN0nqa5erjq1SB7IvcIjKE2kDnOZGAMffNrehzIxXIAVuB2zFCdDvqEHhfZrFIVCyA-1m0ysL8vL-uNLpjxIyLA7zOwhbpgloJSgSrtgCEBUr2G4ApFfTqpgiKtmDHYWfrBuPVZaaCp_tFBjQcb17zjM7FqPxUADURPBSrTJ5qllsWyha3PzxVN1Gsod9jK2ECJmAUwmv5eJXi5Vw4jscizW2QwViFJy26CyfrE9fJfJCOp-i--UC0QWvOkXwvoaifxqlsSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS6HIcdR3kelaqA823OjfSmBcoQeONf3siL0kIOSYF5u3Y8kLaeaefTS-rJDQEMbZyPuGSbpB4h21vCBvJfVniiJ_3WGzYbTMEiOm6zn5uySzZ0kuBBCmyjt9PSFoB9Bb06SYAw0Rs_QVc4RDOoMCLwbK27KWPh4pHrTz6TDJ-PXK3Af-GvWDu72VRhFS2vpycKMdFmHYpEBvcbMQorgIQhPX32mKsMW9iNM9O-KAPl0H_MmWjMA99A1_Osh-dgHyH_utyrO1UYvf9Bp-I6KuZRgLSDA8hupKhvxT6RfdAKKgCbnGJb8gxLC1hBiGcq8DlG7gz7aOS_TLQ0tqdcjrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=VaI8Mf4B6duDHFKvW9rqj0T3BpYPgrlNPsHPGbSHR-XME7mNvYldx1H2EpoOfPRjk7eiQjfZppbDpAtBi_NzWs6rh1KgghgMGsQu_Bb6cVm_MFG19xpac9w-8M-kM7jk9fEa3SycNkkDSK-A6RTMTMt3vuZKfokXKrRGQDK4yRx7PsFaGTr1eC-Kz7k8NmhhNrIqwR-GABGRyO66BJB8CLHMBSgGMMYUIEcP2GySABkpw2pAgKRXOt2jkn1NB_O8QN2iAKzVYzOiRfVTFi-4lvrLKQN547hv6CVEXnSht4hJMhw6V5bLomc26ejL7wIYr7fP2Y4iLsqdMJwSpl8oIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=VaI8Mf4B6duDHFKvW9rqj0T3BpYPgrlNPsHPGbSHR-XME7mNvYldx1H2EpoOfPRjk7eiQjfZppbDpAtBi_NzWs6rh1KgghgMGsQu_Bb6cVm_MFG19xpac9w-8M-kM7jk9fEa3SycNkkDSK-A6RTMTMt3vuZKfokXKrRGQDK4yRx7PsFaGTr1eC-Kz7k8NmhhNrIqwR-GABGRyO66BJB8CLHMBSgGMMYUIEcP2GySABkpw2pAgKRXOt2jkn1NB_O8QN2iAKzVYzOiRfVTFi-4lvrLKQN547hv6CVEXnSht4hJMhw6V5bLomc26ejL7wIYr7fP2Y4iLsqdMJwSpl8oIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=f8GreLCcU7idMXk5KjMVYmS-I0II5m8bJHp5ZPcSxXpQuMm-ti3gzsNt63Z8Oizyban6mHZW0RBqUpYihtla3CuRYMmMjY5HEMWsKGdTuy3DyA2ax-2J5LTa2wLttEPRfkjVsSKYP1xx5QW2ZIHPR8xL8q6LGEgj9XTB2l_YZ2KeQLw8tNcOqWpbRKeMEv54DE5FqLM-UZvfc210OC0D68z9vC__d2TxowkUjMhYqRjtAi4vWYwMZfGSBshWVFht00Td2LNztid0D9yN6ddQB8yrawra8N2zLzS_HWnFxk_td7IZRPRFGCcfp_6gD4BVD9FmzVPJLbzdMw9lHFU8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=f8GreLCcU7idMXk5KjMVYmS-I0II5m8bJHp5ZPcSxXpQuMm-ti3gzsNt63Z8Oizyban6mHZW0RBqUpYihtla3CuRYMmMjY5HEMWsKGdTuy3DyA2ax-2J5LTa2wLttEPRfkjVsSKYP1xx5QW2ZIHPR8xL8q6LGEgj9XTB2l_YZ2KeQLw8tNcOqWpbRKeMEv54DE5FqLM-UZvfc210OC0D68z9vC__d2TxowkUjMhYqRjtAi4vWYwMZfGSBshWVFht00Td2LNztid0D9yN6ddQB8yrawra8N2zLzS_HWnFxk_td7IZRPRFGCcfp_6gD4BVD9FmzVPJLbzdMw9lHFU8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Y4vQdfzfjv0DaiYbgluCJ05DTPtHgV4Ri383n95u1KlEBo-x5QbAUP3_XbYYUxBuEOzAYlya87B9ef5fHMJobEmIFxqt4UK9jf7bcl6c1-WTXjjbbC9LLVAtDOXdW5kLKRQmBkvqZoNmdNxF-OzSqbshDVdLkQkNCskEznDJBlrfqRevQEWCFAWJC5x0Rf0bNVmDn5ZYC2fs5m6cyPAkONVmUjOOjnNkcizroyRFfLzP0A96w8j3CjrxlZmlowduKFDGJ-1G_qWzLf3UF3AgCCwHiDSgpwEMqA-m-fgY0bLGLppo9KOXfC0NwqDM_MOPvbn6riaPjEJuIfWZHizU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Y4vQdfzfjv0DaiYbgluCJ05DTPtHgV4Ri383n95u1KlEBo-x5QbAUP3_XbYYUxBuEOzAYlya87B9ef5fHMJobEmIFxqt4UK9jf7bcl6c1-WTXjjbbC9LLVAtDOXdW5kLKRQmBkvqZoNmdNxF-OzSqbshDVdLkQkNCskEznDJBlrfqRevQEWCFAWJC5x0Rf0bNVmDn5ZYC2fs5m6cyPAkONVmUjOOjnNkcizroyRFfLzP0A96w8j3CjrxlZmlowduKFDGJ-1G_qWzLf3UF3AgCCwHiDSgpwEMqA-m-fgY0bLGLppo9KOXfC0NwqDM_MOPvbn6riaPjEJuIfWZHizU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvEw4RFVY67m-ihr7BjOn3u4whocr7uG7z1gsla143H_59BYC1DJghYpc8Gzq-tXCk7ArhHFrkYYPLJqcApBZeRYDYuwOGSKuIScU2OaD9Eh1agakZLHWashp5mV8j9DyzpZMwXFO3WcPdvP3iuqWmt93nIv4B5jMMoEIYRLwDB6CPbp9stYyvXieY159Lfdhjamqy7EK1MlyGyMY7nWgkren_DkVWhYGwmii7D01TQzdE_Jf6FaQPfOGkthTDjwOojArUx-Whpd9ChiVLcp8wDGa0zx0wvPQgpdL9X-X1khpMl98eI4nHPpgiwAthcRBWC2YniC5KGob3yEqyyJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G__iDVWbvvPlOBVRoB5Y4LWU4ez0kWyV5SHlM6GWgjy4ihJXF00WZT_xe1pjSfCovX5a09QSryc1nIS2MCKV-j8ilxu8EpAnTiW8q3IUUTKMmnbRHRHP_-7vSyyq5e9YMdbYoHWo4Fx4sE-ans95_99F_QrLi24DAxNesW03lLHHdZYskoYdSIvswhgcp6ql-fvAvJpxofGK39I4VgG686JEvC1D-81a7C-SxeWv8u2h5N6Sr_YKWiOKJsSz9DHK1LOg-iSEmX8ohBFWoPGQeKoHvnXNiXGWYdUvj6jTSmgTEkN5vDTDdVWp1hlqrij1DDA85Ijedr798934tS2GSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=en9XfyZt4DG7utZnwilscRTCFBnPy5_BChMWlJGek4Rw5Rfz59bG-Fe-nVB7pgFA1R-FDGXZPw4KYqyuV6J9UZZH4XRTmGblBBy3kU3i2g0hnOBQLyvIXra-5FJK8jT-3u0yB2Fa4JOC-CQAs4UrMhIYsmeDqj_z97bzyOI9usGLsTnQUNsrrBF4q8F2VKaA8r0lN_Z-uL9PcHhTsS6M3ONPNwZ5i41_bitDQQN1tZROyd6oD4PZT6C3os-ZHfsx7fxx5gPP2_o5EfewJTI09YC5Vrqfsaud_qoQpVaXUkqPevoKQrpZAomLh9NFfxzeGOK5twHJLwrc0p4MDOkNbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=en9XfyZt4DG7utZnwilscRTCFBnPy5_BChMWlJGek4Rw5Rfz59bG-Fe-nVB7pgFA1R-FDGXZPw4KYqyuV6J9UZZH4XRTmGblBBy3kU3i2g0hnOBQLyvIXra-5FJK8jT-3u0yB2Fa4JOC-CQAs4UrMhIYsmeDqj_z97bzyOI9usGLsTnQUNsrrBF4q8F2VKaA8r0lN_Z-uL9PcHhTsS6M3ONPNwZ5i41_bitDQQN1tZROyd6oD4PZT6C3os-ZHfsx7fxx5gPP2_o5EfewJTI09YC5Vrqfsaud_qoQpVaXUkqPevoKQrpZAomLh9NFfxzeGOK5twHJLwrc0p4MDOkNbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8PO8Of6Fs4mLMuYXmfRHFKGLvPKrmJGLs9J36VL_lG3QwVVNv7JnntxaFYPiGGbDk0IVQ79OGZkG6YxYt_bq-gdUTOiXalkped5EmPCROoOR853DQBu8qtSfZGif05BWV2HpQ8KaPZHCfG5D2yxYJYSjlyG-RLTMla_5XFk7VRbpi1DTWp6Z2ATS-BKW9zKt3qDuvw9XDtYtHOyEeAiwgWSDZqVyF-M7abyp4ex6hAO1kyE3p84I7wY-7wNPu-oEbUnCTbqGGjfN5RHRqxFApqscsaegrD0B-X4li7_I2obS7CmyDoCiayPZFgoEs6G8LsqYC1tLiMvhKKyxAFzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv6PTlkStnOzjh7ePGvPB4IGoNd0W-0KAwinVqGSQeIl2bd52FfGHR1GU9Kae-Ce3MEI2Elmnj7xb-hDXjpPhhirqK-C388huip0UlcWlJXIpwWVSET7b4QOPSGncMeoEe7IV_zsbh8q8ZZj9eQcu3ecu3vMSbNIRNQdDmZJQoH8ngUwxyy94nUKbsDMtbFnuCn_1z8rSBwhACUHo_2gp56PM8NA59-w-vng3b0R2x77Y6fsj4kvCu5oo6_d5VFcUjcDs0RDvRHXZ1I0WnlR6VUFPUR5m6Ts2WoOXJZf3EPPPcTqjT2G5AUB7fzlifuhUbQ5r9-SKSDW3ppNNVOFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=SfEq7dzvpiec_ZNssaxwGRoZs8P1W4cHEnJ_hd9ZASVUOTvc2mJggE3LG4eGEsO7KUeE6YuP_uoLll1N8-WsMiLdFPj_rp-9o8Kh7e4f_GQUt496bNHljK-g21pobR-PvF9f8fw7ojC19Cxx85BEUcy5fQghx_b83BISfKDC6KNb5QM2K_UTTnNdTuNPNVNW9988m-L0uwqYv2bpE3um66TfaDgVFf6VwdUGD3ehZk_BCI6nUkZPjaxH6GaSb2fG9D_ix5n16IgcYcva9dxWWjpRVJWsOC_jYr5CBBHuOnemxjou2YqGXnL6rkuKeWsq0O31M9Mm0Q5p4hRFsUU_-ZtnM30GVHIxLcRk0ILC9jeMNeF-RWQzYonp1AC1paOeNzkQOMqXUR2J1Kg4Igi_j8D5VN9HUGNm-T86jUdmJfnX1g2J6fDLnvFLPCaN8cbPg2UOhZAwayZ5ApwpcM8dzFn8zJJz_NrcYrehzAxJ608FeEkKC3gqCxlL60n80B0HFw4lTowQnxL3aIojZy3IXXHfpJW5OZj5Mb8t4VjmUwFUhHNm2iOsjPQGegNFpbDhLmazVXNLGtTWg-PK0B-mhzluk5YKzEMK_w76OsSc5xqc47To-dkGl75QGPqkDiEbjWsMJP8CCuHK-mLkN8HAfpCxa1tQErRZX0PpVywaOhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=SfEq7dzvpiec_ZNssaxwGRoZs8P1W4cHEnJ_hd9ZASVUOTvc2mJggE3LG4eGEsO7KUeE6YuP_uoLll1N8-WsMiLdFPj_rp-9o8Kh7e4f_GQUt496bNHljK-g21pobR-PvF9f8fw7ojC19Cxx85BEUcy5fQghx_b83BISfKDC6KNb5QM2K_UTTnNdTuNPNVNW9988m-L0uwqYv2bpE3um66TfaDgVFf6VwdUGD3ehZk_BCI6nUkZPjaxH6GaSb2fG9D_ix5n16IgcYcva9dxWWjpRVJWsOC_jYr5CBBHuOnemxjou2YqGXnL6rkuKeWsq0O31M9Mm0Q5p4hRFsUU_-ZtnM30GVHIxLcRk0ILC9jeMNeF-RWQzYonp1AC1paOeNzkQOMqXUR2J1Kg4Igi_j8D5VN9HUGNm-T86jUdmJfnX1g2J6fDLnvFLPCaN8cbPg2UOhZAwayZ5ApwpcM8dzFn8zJJz_NrcYrehzAxJ608FeEkKC3gqCxlL60n80B0HFw4lTowQnxL3aIojZy3IXXHfpJW5OZj5Mb8t4VjmUwFUhHNm2iOsjPQGegNFpbDhLmazVXNLGtTWg-PK0B-mhzluk5YKzEMK_w76OsSc5xqc47To-dkGl75QGPqkDiEbjWsMJP8CCuHK-mLkN8HAfpCxa1tQErRZX0PpVywaOhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETpoO4Qb6FKxQpD2HmF0JCNmT6qdifaebOq14numjCkqk8qPLAqCB02l-lQ_qn4mov-UbDvca0cOn5b8FKqB4i40wcpCU-LNQxrssI0DsIwq9W5Heo9-zh-ySdq2kYV3bWWLdz8VVAxC_ehLoR2ZMgzCtmBSYHsF9GNCbk845jygh-qz4RZkqIBrSiGh0qIKLqCxLzdMPNoqJzJQU4qYpD1d9Ssz_DpTUZgnHhLCkmOrX1elyZc7e0rOf7oyALLB3ubx4TmlXp-knObcx-T1L7x2WrO9ftOFW0fZYLbCMtOtR6U3GTDrp6t1poe3Hecna7Gt1OBzjrbw4ECsoZVpy9wI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETpoO4Qb6FKxQpD2HmF0JCNmT6qdifaebOq14numjCkqk8qPLAqCB02l-lQ_qn4mov-UbDvca0cOn5b8FKqB4i40wcpCU-LNQxrssI0DsIwq9W5Heo9-zh-ySdq2kYV3bWWLdz8VVAxC_ehLoR2ZMgzCtmBSYHsF9GNCbk845jygh-qz4RZkqIBrSiGh0qIKLqCxLzdMPNoqJzJQU4qYpD1d9Ssz_DpTUZgnHhLCkmOrX1elyZc7e0rOf7oyALLB3ubx4TmlXp-knObcx-T1L7x2WrO9ftOFW0fZYLbCMtOtR6U3GTDrp6t1poe3Hecna7Gt1OBzjrbw4ECsoZVpy9wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=uHKSRNHpQg1VMp4mqvvJ51gkB5UKVoWqKBLGLVM_9fAsme2KacI1Cj4_k7YKSA__96iJnXSghENS0rSZ-Bsqwi3CiSaCXfx-GTksu67LtBpx1uIiuKttvlw-YwTRqgs1xC3YUceGZrmLHMk9GypXa1SFU_n085QsrHy7_TtpnapkKyPchOg5yJ2d2-LybAvJyQKwZWyX_HN5SEyyoKlVp4Lcf52yQJam5jPT-IIBJqD__og1hfknBMp5CXh7e6Pe5S85Z-Zpz6mLWrZK1Olfgi91iLKKFKw3XW6clglj4Pf5sRuE_f52SkJURTq-0mXvka-YcNuSL09CNJ1_7dcFV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=uHKSRNHpQg1VMp4mqvvJ51gkB5UKVoWqKBLGLVM_9fAsme2KacI1Cj4_k7YKSA__96iJnXSghENS0rSZ-Bsqwi3CiSaCXfx-GTksu67LtBpx1uIiuKttvlw-YwTRqgs1xC3YUceGZrmLHMk9GypXa1SFU_n085QsrHy7_TtpnapkKyPchOg5yJ2d2-LybAvJyQKwZWyX_HN5SEyyoKlVp4Lcf52yQJam5jPT-IIBJqD__og1hfknBMp5CXh7e6Pe5S85Z-Zpz6mLWrZK1Olfgi91iLKKFKw3XW6clglj4Pf5sRuE_f52SkJURTq-0mXvka-YcNuSL09CNJ1_7dcFV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=mR0K0-Fyh6cc-svCVl98TcIiUFKx-bc8iIxDqjZghlpB9-iCwhsCvaWN7Ga62QF1f0r20z6d1yknmJXOZYfuNNPRUDaVr1feYKYNEAkvuL_RdoVn1mACCvhFQP98rnHjY5sB0kl1k8tnhrcJNkuRtfRW1XrLClSuMLciUjp-eFor8m0Iag-2OlmsZqGZ7789SpvMg6MdqvlWejuWVxZT7ux4TGUVDGdTgqfle3vdDDnzg9JIuvYPuc7Au0LGZCo1ZHK9FuyPry4dacCzUP39-Pco8_jvUeDVmQVSj0YwGxEBkWgl2M1DrnMp_fQNP0TmydhmSEZ_2NIPjdZ3VJjXdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=mR0K0-Fyh6cc-svCVl98TcIiUFKx-bc8iIxDqjZghlpB9-iCwhsCvaWN7Ga62QF1f0r20z6d1yknmJXOZYfuNNPRUDaVr1feYKYNEAkvuL_RdoVn1mACCvhFQP98rnHjY5sB0kl1k8tnhrcJNkuRtfRW1XrLClSuMLciUjp-eFor8m0Iag-2OlmsZqGZ7789SpvMg6MdqvlWejuWVxZT7ux4TGUVDGdTgqfle3vdDDnzg9JIuvYPuc7Au0LGZCo1ZHK9FuyPry4dacCzUP39-Pco8_jvUeDVmQVSj0YwGxEBkWgl2M1DrnMp_fQNP0TmydhmSEZ_2NIPjdZ3VJjXdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnlvK7L4cWPEmAGOoWm3_QW00-t0NL51j6iBcEpJUuEQlL9IKpCdvtfJxzLKp-_ivGZ0zfRNj9bhbUfp7QDdgl_WawhBgxNpbeNCuxJ8utFlDH0RUA7me9zeOcd7dVB4BmjdC910NkBcUKmBjqZuhQcGLcDYq1fkSNicVGpklGQxjh0XLAsasqztDW7_i8gPnMoWGVyw_B331l6xIiooR0Ji2DRC5-KStCZIuIa8h-VKIP5ZU1KCfStEuHHEIeqqBXsMusg9lCYqEsqplGdYwgK3jdIhBEyXmyNwaDMmiYRlnGBdhWBOewq34AYrLMPXAwXLTkQee2WJngc0GfbRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpG-SqMeUIGfGNwI49hEaWqLkJCHhNK2f16LiYRiBk2SnVml8TpujMJp0RS__Fvkmnfz49hjRwTVWHyKadQi5eVm6xOZD6ujg0evlk9kx4FnYGp1iAbCQNi26DfWICoBglpyCvgchcBFnl2rbpSbFSpxeChIeuvrsU_EPztdXdt9RncVUDM3ETJcIM3bqoef2kRRr4shWd3yQ3ZFQ_X7hdpuNFWygPAlrXHvFe8VsTOEIhIX38_n6onPs6hxCKMcVZIJPciTTmKlN6AHMPDDiHY7gFP0xOih0ctlYWMrVa3u9fMhZPOl3TFuinApd1jKItmqfPcmSXqFRyNZKpCLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTidnuE0s5m4hUsD8QUe8StrnXwaWv9l-ssN-tCZ35W-UdBWNppgcgr0Y2mRyEJOJowSM-kQtUwKTWqxiSDtvZvWEOAxsuA3LKuPH10g9RIbfWFDHHi4xn9SQ9ls5nd6RWXyqEtapDEwAyk88B-tXkP4ZeRmLZL-q40wP36lqddXRodf9yjRDmuCC_yRBhhGswnG3HuSOwpIOWPftVfk0sNSlmTd-VPWUBeVVVlO9wyvRBk_4Nwz7H_yeJPyL3VTs130CA5U_23U06JEyMjgtyD_fgcvWf-v3PTDXIci1Ts-dUSAdCyQwePhPGF4GglOMeti3GMdz3Ct3FBwa9T1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFayHeZB5aaY5_ZBvXHqkkVHYSIJgRPLUmJGArL2uE76EH8f97hj3TxyccxeYTbjHBP6EoFrrdQ3b9ReUoqhF0eh9wwc0fT-bq2XZBzMubsb26y_XGOOCIuWMgr1e7tbxnSL-R_4CJDS5a0AugNAksZDHx_pRtFsqASUTvWSACKhUY6DZpd3Zrvq3PddrA7p0d5VWyXTKwr70pDpiccUIiq5U1H4a8MIC4YQkpkcb3luXceRu1AHA8I7cQ505jXjNPUyyc9vHUNTFTlb-B7hXVxdTwbGmDtyZI-pBzAKonshYlK8Qc2YQ7deClR784hTvrwjOOCbjYC-DLAGDAXTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2f3bG-OBs8uYO0bp6NAfTSzZ0udohJ3_30a1XVVzf14YWKgLxcwzSLkps9Gou2zrIDoKDwEfklGzF7AXMWFaQUBvOLkjOfg-CghI460krUnAvHowGJIAISN7H5za1TAqbi16_U3TRMvIsTSvgVj8KhU-wCb6n37nlFM9HprfPLM1AN2aq2b6SwabNowmx9axVoKAaRq_MYlboFMkQZqxL3QWuJM1YwNF7WUvcUKfBiPbjSjki78Vzk4-V51h22L2_JA-R8fj1gqlurOg5SMqYUXrSRwfn26Bfl2IcZ8OYLtcndd2-0-v_0JwAhJdcS4jXpK1r0eYWzw1Xc7PPs27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=l4fCtb1QlXZPMyuzREZB4vQzukxfpuD_bBkXle5j-7bEpzdVKVyMxAc8FDXgjdEGVTHbchCr0bUZ-xiqdyVlU6hszGrDLcehxXZiRr5RzuhaH-DP2-SUXf1Y81xiTlLlQqop9TOxWRdlJ6qxko90td03SIMoXlBN1yrBf3Lum95rP8-6wAUZYTG-A4s6QwUWuTRIlBbfd8Rs8mWs_s-1eJ_OhwTf4yd0J-FUrv2Bul2SdcfXrg_ciidQhehanHPApJ6hvue_WoMXq3U9QCbVrTR-_QpBs7z0_I8l4y8n8RGjAoDf84Xe6KUd7FfH4gO4RQYFmXpyhp4HGA6gkvl4ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=l4fCtb1QlXZPMyuzREZB4vQzukxfpuD_bBkXle5j-7bEpzdVKVyMxAc8FDXgjdEGVTHbchCr0bUZ-xiqdyVlU6hszGrDLcehxXZiRr5RzuhaH-DP2-SUXf1Y81xiTlLlQqop9TOxWRdlJ6qxko90td03SIMoXlBN1yrBf3Lum95rP8-6wAUZYTG-A4s6QwUWuTRIlBbfd8Rs8mWs_s-1eJ_OhwTf4yd0J-FUrv2Bul2SdcfXrg_ciidQhehanHPApJ6hvue_WoMXq3U9QCbVrTR-_QpBs7z0_I8l4y8n8RGjAoDf84Xe6KUd7FfH4gO4RQYFmXpyhp4HGA6gkvl4ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=N4iVJkRqL6UyqJ9yc3Jz-fnWzqgj7-NPsVSHcD-msNq5CL_Gf_3HX-8jVLgL3HdH0w2GxkTF1xuP8g5xKTBLdykbMKJMC9I1FQONnR8LcM9G_HuMsjZysFu1eynMo7iiTHGhug6opqjhUbXvmf0x2c03c56_CkLHycRvqiN5Mew5xitWI8iWWiGQyM2qIpDeMOaviRQwrGzFOueXLQvCAo00NhcAphlT3vZ1O-ZE8LQh1IBjppvRPk-gQ_PPL4LM7Tm2GjOj7EV5gN7qWAMfzISDCgo0vOw_HE-2fjUUUrclI3tN6FAjYG_r8K0glzPQrz2bdMdeGobcd8fN86HaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=N4iVJkRqL6UyqJ9yc3Jz-fnWzqgj7-NPsVSHcD-msNq5CL_Gf_3HX-8jVLgL3HdH0w2GxkTF1xuP8g5xKTBLdykbMKJMC9I1FQONnR8LcM9G_HuMsjZysFu1eynMo7iiTHGhug6opqjhUbXvmf0x2c03c56_CkLHycRvqiN5Mew5xitWI8iWWiGQyM2qIpDeMOaviRQwrGzFOueXLQvCAo00NhcAphlT3vZ1O-ZE8LQh1IBjppvRPk-gQ_PPL4LM7Tm2GjOj7EV5gN7qWAMfzISDCgo0vOw_HE-2fjUUUrclI3tN6FAjYG_r8K0glzPQrz2bdMdeGobcd8fN86HaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpREVkfiGI-r4OKgm2_ajuf158xcRvs5XRcn2i9CSUdFaR6Lvujxt5aKR-R6jcq1JRHLkdd7dtL5scgeSJQHyWyFj2xg4NT_0PGPI9Lo3FHihnXb6MZkCf76V_peSJF9fPQSVim2eZm0zsKuGCM2YMZjkEcz2MVDtktYCvVQnxCV-6ktS2BXms0XXgAC9CD7vZhAL_uSj6LmHVyq8JkTagywDVkrdSPata6zdNlHyJFqgg1loIYQ9ODcyhk8yzeGDn8GWu89oD8416B0E5PvLUWvoLaw-z94hVyfZjw6hhEOJoNLivg6M2izmDveibEPlpDmsfwfFtVJ4hhZdEmbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjDpBa0GUdI5rVhP6dPiLt84anA272b-Z5VQp0ciyPIJoLTasl6YcCYL4nW1lUNpNrJfcVU6A27_ghgZb2pmRWc9Gw5AyRYDBLb071c0oKMkw76J6oxYUIHnjoLIqOs5zInM93A9QBIyufmYBPFUaBLDXqyn-3N8agMpjZdvhLzmjHmNL9cf7fCS6vym9yxDhg6ndWp3Bz070lYd78kdFMjYxYMiP_AwmHTmwuXs8Aq3x2-RGvks-RlOtXiXin4X-ifcvHc-K1PiAnrrB7gJZ2BLkj3NfIuPM7CDfV8VkTCxS1Y4r_E_p5dNvSEXLaGE4uP-tdHdShMi0jnRIOwCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=kTfPrriFESanNd5x16hilzOtLeyfn6uyX25xDCzR1MqVCww68_DPI2taxwUMiIPOhANzv317TwzmI09EpvauGh8NvhkBRQZfbzsmlkLm_c5PJAGA5QY4A1VOGsrMHpEYIIaIyLSEGHMlS19s6sUQZkU1mqaWF_-UvEoLc3JF6iFJmh2jNnFDY43uFvTcnS8pwweBbhKMU5sHh83bUX5mgQIXvBBTk5yq3jqeuCgKr_msmW75R8Afx77CCjiMKzDlKWldtONNmFxzRpnSwq8HuF43jnm7DJyaLgQ_Vqm-0bufNeNc0_TNAe7lKvMz_oizZRQhDruQXkdRj75xt4jACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=kTfPrriFESanNd5x16hilzOtLeyfn6uyX25xDCzR1MqVCww68_DPI2taxwUMiIPOhANzv317TwzmI09EpvauGh8NvhkBRQZfbzsmlkLm_c5PJAGA5QY4A1VOGsrMHpEYIIaIyLSEGHMlS19s6sUQZkU1mqaWF_-UvEoLc3JF6iFJmh2jNnFDY43uFvTcnS8pwweBbhKMU5sHh83bUX5mgQIXvBBTk5yq3jqeuCgKr_msmW75R8Afx77CCjiMKzDlKWldtONNmFxzRpnSwq8HuF43jnm7DJyaLgQ_Vqm-0bufNeNc0_TNAe7lKvMz_oizZRQhDruQXkdRj75xt4jACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=kZ3gMC6X6XW24oswQiHFfazPo0qNX7gA80vbB2pcuO5UznVAnU05Ywt_biuPdIJv1S1nIi3zDQgAuElqwFRs2FH1xvHlbSY8oON_V4xmligOzJYJluoqK2aSFEC4bHB1l0JtcyoKaj8RqDzgQxYuzeuWV6lbsGpomdBazsksIiP4xw_5Pqktadm_BSa0DTPgYvVd8ZCUFaHP8qRpeV6-Qhzz79UEaYqAJRsDFMtHPU2eazuQdXqqs8BfFQSMY_GEjspPPckZPz0H5700KK9Q-MGYti6OsLprZXze1k1x6I9W_MWFPQKduhkHeSE9xxnZTz-hTNcvC3v8XNG9Zp2_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=kZ3gMC6X6XW24oswQiHFfazPo0qNX7gA80vbB2pcuO5UznVAnU05Ywt_biuPdIJv1S1nIi3zDQgAuElqwFRs2FH1xvHlbSY8oON_V4xmligOzJYJluoqK2aSFEC4bHB1l0JtcyoKaj8RqDzgQxYuzeuWV6lbsGpomdBazsksIiP4xw_5Pqktadm_BSa0DTPgYvVd8ZCUFaHP8qRpeV6-Qhzz79UEaYqAJRsDFMtHPU2eazuQdXqqs8BfFQSMY_GEjspPPckZPz0H5700KK9Q-MGYti6OsLprZXze1k1x6I9W_MWFPQKduhkHeSE9xxnZTz-hTNcvC3v8XNG9Zp2_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ZDFd2F4N3q3KZhIY_ZzdcH_dynyiZbo66VFXGwZwtm0mnPQFRhtNNpLpl3g-JHsEwa2Bo4B6hhjvgDjqk87KeRoOY0MlxtB7vGz9t8Pm3Q22a2guge-K8CFeH6uVWniSVuKFeb-VS7MftWyVKyhGN0Ox8_4XPedAQQq3VUfJ1c5xLHNfTXvWXUGEyWWLVkdYBqFB0xU56o6nTkSOj1Q8Fer-yH_2CW4uh5vQWUVxStSoDCfhp2HSeuYKDpc0yrpg7WMnQaH8lyx9CCXWLr8Ha4j5D6QNwUWEpUf-PxSFWhLH1120NLrjISaL0jcWPt83JBXcMgJ8Q6pcks_7ZWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1drfwuv3D6bJ5Gc8DyduAEzoptPyS_vZ9KOQkcPRVoWrMY0FRN5KPNhtLEeBR8l5Pqf0fsX0DRH5yPS4hQ-HP5Y8eKdRjD1a2DTcLwGmFGF_xgEs2RqUytcYSe4g_RwEkBu9kxf1By7-7dBV6wPCpnaZ0h2ESs30HeN5Z323JcUy8YsTfk04fDa3Y9FN7kSpJVwKvXajEX_HYq165DgsD5P5f28GHX8BaxzgqOwqg819rosRahZ-cTcty0ct8Ty0MXdGadVsS_3KSeRtD40_6JBZG3Rs-bgLvKhl_N9kJixwKXitRUbOwO5GylR6HX11Ebyh1ShvMeQV7-7jNCmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VdLUbANmaZ1QYXrTk5N9a64gBFGAoMCTK5i_XrWiNHE1lJi2ID_CK3NWewhtC5QRmNaj41LPz9s5Ycu5dt86Nc3j4obBGKD2psooe_6Q3Y22s7t0IfBCoy_5aId4neFKkohue6bO2LUmmAsAx7670m1aQSAjNIEgTAIMdT6lFkb0KBa-ja84jWFPfDoahK8bzYV_NxO3evW0jiGOOJsgr8QFXy5XdFgxPsZ2i5jQAG7EfeOV5UGMkf9vXz-S083BKvLP5S0Dj1w5bR1FgQ5k3RCOtcxgBpA3cyti1LPE97hgQtRlIj6QwtJzbzlWSn9ZfY5-DbmlNwMT6aWRq0aKLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=b09SZsU8oKmgc3npUmXfsHW4_2dMpeKV74onxAykup2OHuGiMU0IQlT8odJVCmuNmmQmg7b9W-c-zEA77d58KOkaJ1ziy12S0wJ5zGOXqXrqGrQqk3TfSwAA540jFeI9xhxdq7EAonJPLVzKuQhQ-fanG1zEdjlhBHgVoolZSLsq_GR4QTtYXL8KMlfCDchQq3KU2aRhAtWQr_RiPEKLDhPP9WlDCU9ap4cGqx5xng2pOgxJgECtf9FI12FQ6IECMiAiu4dQE1529jvCWb5uhY2co_e2UL9cGQvJzKI4Da-urOjaHLI7dpMOKyPnT5UXuAnZTfTGahxKpAvmn5IRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=b09SZsU8oKmgc3npUmXfsHW4_2dMpeKV74onxAykup2OHuGiMU0IQlT8odJVCmuNmmQmg7b9W-c-zEA77d58KOkaJ1ziy12S0wJ5zGOXqXrqGrQqk3TfSwAA540jFeI9xhxdq7EAonJPLVzKuQhQ-fanG1zEdjlhBHgVoolZSLsq_GR4QTtYXL8KMlfCDchQq3KU2aRhAtWQr_RiPEKLDhPP9WlDCU9ap4cGqx5xng2pOgxJgECtf9FI12FQ6IECMiAiu4dQE1529jvCWb5uhY2co_e2UL9cGQvJzKI4Da-urOjaHLI7dpMOKyPnT5UXuAnZTfTGahxKpAvmn5IRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEw6pWmAfx2CpLZiw5oB7-5eHBQsjqOSzAP5Clj7QPEIW4N3ZVxvZ6XwDpCc0_bLwef3t-QyjZtMrnlq4o39Ey0EneUnTkSr_1nhQLTMzQ1j2ZgsyQf2W_9I27oOGNlv_U5tHUK6HN_k7TpkJoc0PH_oMcFFGtzJ5WV1cN1C5jf0GK4-N6blkb8-uJJRPUkqTiek3-jGU9EygyhQwmJUzsMV0uj7sxmijFP8rognzlfWTzMiFTDceFS11QzPUMC0xmdL1eDt-jBnnbFZO63jNEfp08ZdCL_ztmShHQGGFnKMN1F2LBGBEuUfuR81Jy9mZVXrFptzpeGvgRispCYFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STDhdyc79FEgR-zBLnRVSBz1TRIOftuHI-PEW4zZPLyjZO8Ykzgvfr661dXlzPSZk7KCt842j7XozP44q37VN_IwsPQoSB4ztXo3WfIiXPhFaL6LRYOI-YfQy2xE3RUWb530eOR_H2eC9h6XU0eS3G6dXgjcKJ5VkHHqhbl8Y95YYL-c6nIZD3yv35PfSP1E6xJIpzuyevHhZYjgNsu6E8WtV7tVOIwjruEFqJRHgwbfpVe1kVLEBa3-LvM-G806wjOEmvg4gVgreUUnfH8v5EU5jUdW3Z8xYI5rs2XTL_RmG7VvgplwVkBqViMdn6Q1FEV3vbljC8udSPmPPKIzLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dULfnqe2hwYIutAES6WB3byto045WOgNVNsdMtt6CjPgAFdqOnhqS3an20sD732ZNrqfySOCz5vPj6walcoe5-rCyl4DTbmfiGsfeJ1Naicksvzq6C7whNWDvU4a8Bf80v3STI7mOSg4MlCogdvF669WOiLzgyqCwVhWzGNp4pM4KdgX-1u9eNAqKXdQZEYU5nSgKB1UVaamUUsAySChxwrYodjhlH-QRO1zEOD23KUVGuByW-m3khpS_XCLouC40PrMCFsVxblMqAA0SIXrGGZbKVIShgAJZUYjMeg4FNroBPo14NJ1NGzC018eUVBJWU9AdvHfOD7HlozM_g-2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXXJjld_ulb5ghK7U6NZx2PyuY01nKsnQ9LRcJsVAIaCPxtaKnyqAbOc-3uujhAVXxCSX2KscHC_J212TU8utitPgZyVMp66UF6nDj_dvGm3SO0BPDWEgOoIcwxcUDeKVppWX4_g5o1avyH1hF4EMEbC7e_61qVUfJ5oLwDXYf34pL6jS0SabkjopLxl_RDuYsD3QEH47Yqpdt8eXAB1Ea4HVybTjE40AOz_zoDKgkEXNvK_2jqJW4nnql5NyXMkccNZznol3_tev4uEfiyheHryfHNKIRpjbmgzqFfExu106PvFvmILrwTCBrAa1mLwtEmbaoQnOa1ZkK5vU2Wy3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=uRdO3PJmKM5OyW4YHvLHXwmwleFQGvGgSKzyu2-IFbOJnZ30JVYT9sABVa-i4aEce8fOxGwiR7oWPOppPTxDShoHjiKHlhZUkYfIQF4dyI8ctUNotBu5eQj09OiepAuvtqnoV-vMH7n1lsO_QdUFKzjNgSdRXise9E9BJ8pxE0LLkaUTZ2Z3QVmFE9UKSFH7HfZ0Pi0UAatPzunCIOXN2hw1I9wDh29WS3keI7ou3A2cEr5VDtvar6ZUZzWmxR-r66I9x9umSUDHZW4aXiHj4pXNIzSKUg7lOqqTsri1IMkhvkN8KGUwIXiVmQikwhFgIpnqgKtnOO79a59Iq6N2Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=uRdO3PJmKM5OyW4YHvLHXwmwleFQGvGgSKzyu2-IFbOJnZ30JVYT9sABVa-i4aEce8fOxGwiR7oWPOppPTxDShoHjiKHlhZUkYfIQF4dyI8ctUNotBu5eQj09OiepAuvtqnoV-vMH7n1lsO_QdUFKzjNgSdRXise9E9BJ8pxE0LLkaUTZ2Z3QVmFE9UKSFH7HfZ0Pi0UAatPzunCIOXN2hw1I9wDh29WS3keI7ou3A2cEr5VDtvar6ZUZzWmxR-r66I9x9umSUDHZW4aXiHj4pXNIzSKUg7lOqqTsri1IMkhvkN8KGUwIXiVmQikwhFgIpnqgKtnOO79a59Iq6N2Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKKrDjsgQDl1603t0NXDug0J8YZJqRXw8taxi6qHbX1EhB28s_64gksCVg0qnixFL9TskelxLGnZIBFCUwvSEnn34ApNIVZGie7PNRJC6LBt9I2rHVdLHEZC7aHGsEIKJuVFs6rrzu-HMh36rdINwtZhmIH7jKvSGvSGnNUnFEZ_AB_uZI9XRItZkmyducqME3omNqowtqSTVKNpoqURqP5b-iuSEJrlI3DVIj3kwJ8OQvohZ_9wiYl7S8-OhIwYPOlcLJyCfE1Pbul01MIBL-TR9-eq-TB0yaxFybMfJwOewKnkdcJ7ZGURMcsHmwAvynLr7J8wwcs2TIjirDW1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obFBj_tgr3YJnb3d37lswcPHfqQUdNHuk5bg5ix-C_Qd8oEjxtO9c0_y3Br5MubjqnIqXyytrMNvwozLifoYePMTtIqNVyyKXo7qz2FmHfMMnS3fyTLfDx-RZNVrtR0q49uLSALGOh-Ah8ky64VnOXIYD2v3eQBrkrS1uN_dfPHsBPn5Qu4__xOlS0XG2Wh4GtPlL3x-Tj-UBp448ajaQyXvn3dZI8VmHl4wMmYg_u173btTAvPIB4T-f4Dox-OZYDT6N05l7icUfgudGIGxgssq9NE4Zug-t6NeCViKpdLYsA-TudUFYFOAf0bTRMmSwSJyooZwW8JrrLMHC26T_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpT_9tgj8CA3uFonV25eake7asG_JjVXZOeLuB8_ChdGz7kPMhYi1cPMyi4BL82dMXENsVGYDCqlcuImuyBoTPJvt47ZkcK6kj50ItZL4JE0faYSXRDM_Vs8x-Sud3uPwtFexUITdhtLTQIyAs9Dl30EMfuEsCEVmKProRUhXZIKil3ivMDhnsEbioxzVjxv-MeZdvX9gy-yLcpZ7OwtUgD-sIiNgD7kPW_pqY7dUT_KIZUzQW_2I6nSGkXrs3G3WjK1ps46kKsvKZvVRLyLsg92tD6iV42ArL8XeoiqZlcTxNQytUpItmIGpIFvXxiLxefyXinbS-GbTFpEgEdKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=vXEl0r7kX5mmA2zWgtIbdzCXP_G0JeFHhp6tOCVAgEk3udiQnbvgQ7MH0yUYZt__uIZsrTEIRmxuch16WhALj5SzcCSnGmT0LOlcaV_lx2io_s-LFCMUBoXWJFaX0PtZ5c69-TQqNmVedT1bgMnzmX_cNPdz4cSwnz7T1OfeWDr7m3x8gJuZ0ZPUcC1bBvs4_KLfzoBSqcwon7TbWms4JmaeV4qPYuhgkO5lBRc7zqj_KAutQn_uPlfk6ABvA23F6FjylNCeUjhz5OhdmNoN7jBDu-zmXOQyRtH3BxttrrDy1n0ytAZim8i_KfpiyY1IN-5k6DooJelXo01IO-hXQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=vXEl0r7kX5mmA2zWgtIbdzCXP_G0JeFHhp6tOCVAgEk3udiQnbvgQ7MH0yUYZt__uIZsrTEIRmxuch16WhALj5SzcCSnGmT0LOlcaV_lx2io_s-LFCMUBoXWJFaX0PtZ5c69-TQqNmVedT1bgMnzmX_cNPdz4cSwnz7T1OfeWDr7m3x8gJuZ0ZPUcC1bBvs4_KLfzoBSqcwon7TbWms4JmaeV4qPYuhgkO5lBRc7zqj_KAutQn_uPlfk6ABvA23F6FjylNCeUjhz5OhdmNoN7jBDu-zmXOQyRtH3BxttrrDy1n0ytAZim8i_KfpiyY1IN-5k6DooJelXo01IO-hXQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=nireyQYfrbRhh5KtyRzEhtcTHkcLVImCtfQiLfQpX1f1uDTNEyDak0H4kb0OAQ-NpNfYmpAuTi8WwPAONGlHOkREBlPRKVglHByGM6X61XZE0KaRzdHdnDw0CUeqaVAVrKRWFkMmWGRMCqXSs5i9vZKXTj_Yxcq1TKD77uDpqm6jqDcyu-ICKTtNwEht97ys1X4dsK7VJrEaSyyPRxYttCgSMsSAIkIewa7CMcan3u0qwhqKU73VZE_K5A060GVUICE_trxbCrjgMjpFPzb-iwuQR4YQkUchFwe5JmvwWshaFyappNMzVZdCYtJEnhaddX-YGzUy-J29G_6MNm1xFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=nireyQYfrbRhh5KtyRzEhtcTHkcLVImCtfQiLfQpX1f1uDTNEyDak0H4kb0OAQ-NpNfYmpAuTi8WwPAONGlHOkREBlPRKVglHByGM6X61XZE0KaRzdHdnDw0CUeqaVAVrKRWFkMmWGRMCqXSs5i9vZKXTj_Yxcq1TKD77uDpqm6jqDcyu-ICKTtNwEht97ys1X4dsK7VJrEaSyyPRxYttCgSMsSAIkIewa7CMcan3u0qwhqKU73VZE_K5A060GVUICE_trxbCrjgMjpFPzb-iwuQR4YQkUchFwe5JmvwWshaFyappNMzVZdCYtJEnhaddX-YGzUy-J29G_6MNm1xFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
