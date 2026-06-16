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
<img src="https://cdn4.telesco.pe/file/TpaV0ml2c3MIAnzTZVEg2sFKcvT_DAL42RO67qEmpHUk9w7cKVpVnicdTPAmqbNTgMelC7piRCRYvDjEONi_z0ghn8ttG9ReM4BOI2NhCca_mTUZDoEsRR29pi53BIKU5YN1tvPCtl1HkknLp7zuLoQw_7t3sMbYeUwAr_76_f9xACEru5uNth7yCmWkYaMG5FGwG8oQTmiOuZD2fEGTFkEwNiyX6SQhMpvduM4ZBw2j-0UXOpz7A0PZrtv1jmwMedpenXR8sAVaKZSnuSrg5fhN4DijJNZ7_O9cwnrPf50GYPbWWtRdrUXBoB39l5e75H5RPwX0mXaL6IPSbl3CWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXtk02OVHd3r-o89dz3Iu7eryjb9HDLqM4xGjFf5f-JE6I2uLobzwkkSSv81hp3N0T_kzP9akVj6jFO9O_BNTSpswlSkbirttJ-OJnfyjR2zrQpufUMECzp53CxaykxE0D_idueR5hGWz2P6tRy3Gz5lKK5Zs26DvHopkz7PG8GyvdSH1hH4ZPVIuaRO8yM9lzvE4zQxapsj0A-kSQdMnd_8Z-bXBipPYUjYKQ-FvxiOKuJUDxaPTW2GOweMGghaY-ARwL6pEJn9rcQsjj43XtZKFK6h4wm-SjGuLrqGznm2x3FrwCT9F39G7w_vpKyK9ZdwMlwPtfqXtj8_xhaFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be0lKh13Bt1L8CSRdvKq9CXbYtZTWI6TlLH-KqWAu_JtID1IVZXBzk1dJmFTnwJjt3ryAyjzZKeryKsMFx0sgRKSTPTLPoWVsCies-NEdg1EIjlvKohusHcaSoEKmT-N8fzD3EbuJNuq28F17lMw9DeyYp0-bpVu8Sbd28ETaBaO5V92Bat01bRMB_3wTaRU6l-bpbnaVYRQEFbBxPf3zoPyJ3VJQDSvj9J7YG0Znd68bOJqXXRQPiHXepJgCE4jsTXdZ9lhcOXl744D3YqszTMgsdRFKmJyguYn1GR8mamcqKVbNRt18y_0D3r6b8fsatxXomrQeaqnWKBtzexWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/funhiphop/78030" target="_blank">📅 14:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
@FunHipHop
| دونالد ترامپ</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/funhiphop/78029" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حکم اعدام جواد زمانی و ابوالفضل ساعدی از افراد اعتراضات دی ماه اجرا شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/78028" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حسینی با یزیدی صلح یکساعت نخواهد کرد؛ قالیباف و ونس توی مراسم امضا حضور دارن.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/funhiphop/78027" target="_blank">📅 12:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knlJC-mp2rUwrVwd_bZXR660zBhD4ZkMBg-Hgbn0bWZ2_AkXS-g8HelMsULyBD56RI8xsaBmnWufeYWZK_Bikc7sZK0yZZdzC7sYeBLzfs_mfC7DdK2nDayboQmX69uZGOOvlceVLYTzaMjLUoie6IvsGD8gfAhJ-cJ5bK6zkh9jF7ssSj1caGsSE7AJJi68JzcDTUzmKSiQ_oazn9kwh4aYPAMLTUHJM5xyuxzcrj3W1XOQhy7yGosy4gBKwQWXE5A7-sxQfamVy0RnqogPGIgMi5zZ-uBP3vUlaszcN54brsIVd3RC_WZzdt6D2hkVUMKEbfEUqTY4vSZZUbVvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیل باخت تیم نبود این اسطوره بود....
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78025" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/78024" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW5qxe3Lo_kMI-TdIHVLOoujiuI2HyXENB2t1kcrrf6_qd5tNTUQ_Hlm1R288PiX8dc9UwbM5Qbq9Gf1mHO4zJfIx6iKnVIjMNr4KJLE9V3E0b8Dz1Fjffuesw2NAW0rbqbi7R2IRJVKkrFZI3Qc0_vmHwSH__THztCWkQUPH27hok_4m5b4xW4HvEEcVUvzHTK5dkTuxzrIRP7e1K-OnqfxlGyLhrCo35qdhQf6anXbHAlj-7ROM-_2ukDNMmdAQhwJi9A8iLraKzS6FxuM-msSXnWmCaHuvznxgrvJ39UToJA7Q2zLRZFaSvnPx4HdVutEbjgPUGEvNe-6s3Z5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r26
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/78023" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بیرانوند: اون دو گلی که از خط دروازه رد شد متعلق به چین و پاکستان بود و عوارض داده بودن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/78022" target="_blank">📅 12:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بمب افکن بی پنجاه و دو آمریکا تو رزمایش سقوط کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/78021" target="_blank">📅 12:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">۲۰۱۸ بود ساعت ۵ صبح داشتم از گل خوردنا تیم ملی حرص میخوردم، ولی الان تازه از خواب بیدار شدم نتیجه رو دیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78020" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHgadWgVXamdpZ6v9-iFifUpyxB4r1qf7RWiAkzvCgT6AP1gTe9R6kWUF7c2vY9VJXUgPCJPYpuBgYROgQy9Y6CssD7_3ZUuNOje0HUoaA7WXNbpDogTQ3fcs_jlQKCEntsH881GR7Q-EINLcOt3y8Aydz8L057p16XxKb0uouzVtq2S1T7eIn098vmgqSuHrnsPqMhEwvqzQDEtE5VLtbekYsMbM3WOOKMWzIVvCym-0SWGULLHhIqcszfI81I9Eax_wWEKrKE5PI4tdJHBt_7oXhN0zDQ0SrgveABZoFx9XBy1XpYb_l9l-GZibNsGEOupYj9s9985h2bEzWr7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Playboi Carti
📌
I Am Music (Deluxe
)
📌
I Am Music
📌
Whole Lotta Red
📌
Die Lit
📌
Playboi Carti
📌
In Abundance
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78019" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbQ4v5fRpWaif8QGHxYbUIgkxnMTUwziDGFF1r_ZieOYLrIYP8Z2eKHoBW6w5AJepKi1jif6CWbyvoxh54c7C5Ju9mO6oN66SVg4D_M7CpeaZnBOSxJAnXsHO8JkuxHv8TXGAPYY14qDC72iROSWmzIeArn3eRJ1MZl6FGypmkVcJThPi4kreJOBZyB3B7VhAA0x0ZobIo33m_z2qT0b0cY8nATh0QrEPBo38IaJhpffcWKXpmeLOzlqkbKMSaY4VTFkr20LB5Xt1ww3xEFvU6ol4oDcK0qJaxyg6Met-A62fq6QMJHBLCMtxExdMPxp05t9KLmfYoBZn06xIRSydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgRw519GFBI5g8QeAi_nwNoUxQB-WUS655pPnV-qv-gK3mac0UGn2E6Iopg0v2sLyWU_NqB0sQjuG-8O15YHHp33v7XRju1rK8_S-egNzUCXd0jzXlkWvcRicCUWQDhIS0IyEDJD6gSCv5-OJVMtwdwAsGpa3a6yYOWesgdnQiCBOWNtQ8jJYF5z5n4Sgpy7Bv7JRvdzVZqCGl2gtuwkgO5pVipqfjMTfqhaQ-AtYnrRqc26lN80pNfz412KtFJuLGuEAw0FbROI5WSudA0XRxdGbx8IFZhTXGh8OhsLjqUiN8E-YrzuKfcq39TUar1fPy6QKl23kDZKCb7iD_uXfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78015" target="_blank">📅 08:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینو یادت باشه که همیشه تیم‌های مدعی قهرمانی جام جهانی، تو بازی اولشون ضعیف بازی می‌کنن که تاکتیکشون همون اول لو نره. صبر...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78013" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78012" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78011" target="_blank">📅 06:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2k2OOCG325fG6P48HzN7R7V1PhrvOc7NHQ4ofGx1NxXOisA-5n62APeAZACmuKzLjRGgzt6J_ZoGcEMMA0kLuEFmcmRCIiElXsQqLsQIS4EJAj5DYCypDkKCRwsiCevDcyrcau1psqrE818QsoszhQsKz_hrBm_sOgShfitLkByo3EV1xmKwIIu-LmO1P_KFsNFR8bF-E5NXHEqMpph1XEcMgEdK_HNL9AGCDF7Rj5FmTcVyglg7dmcksJzI6Lo_DWrnZfLns0jb5pwMJuX4LBDMx8LL8-e-Yu-qjYgg7l9L0S5yyuoTo6k40aF2xVDsVTILy3mHGMlkZnbZduakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گل برای جمهوری اسلامی
رامین رضائیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77990" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ولی شوتای قدوس>>>
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77989" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این چه کصخل بازی بود گلر نیوزلند دراورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77988" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">استایل بیرانوند دقیق مثل‌ بهتاش پایتخت شده وقتی ک سندروم میمون گرفته بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77985" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJtzVljtTyLVjX6PUxXi_-MN2_dp2uzi578EZbmaL_hCGnJeXNtte5nxfG9a63Ce7D8ENjugCLaagOq11GimpguDn4yR9pgrCpAwBRJn5_VM9Q18OfFTc3iDTi8bNkFLJ_hOTu3YTUT7CTotdHnzYuCiwQMcqUDfnc_rrTNLNeoKNGlP9VMfUbAwAi2qKu-Xd9kzRnZbKlPw2EgNLtglwhwwfRkbGJP9N9BaKMiqFXxLddruxdbZj17UNjLPVLNAEX24eEX77PgHUs9MxwxdxlB3pArH8SgOSPSMSqvJkWM3WQAZSSSWi8H9N6FajSQ4Y0Cl7kNRGSV8WAKgL_Nydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل خوردی ک جاکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77984" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عجب سوپر گلی زد نیوزیلند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77983" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :   • @TrollSporte  • @TrollSporte</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77981" target="_blank">📅 01:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXXiKH5jvMxKdaBt7sqaY60AEWUnL1jBTirwsIj0QkeJcfSqlihh-B4ay_NlfhLAxH7DWtjdkFT4NHSu6_PsVCr-buKI8cXCH6VjBPS2VIlGGE3yPFfquXjj5JuCgPqhcg4u-vZnHPR7jW6SvMpHP94-AZw80J8Di5AjLVlxoWoYix46IZ-J44edF7VzDxJpOJ-ljtj1AfB8Ij4WAJBSUaDDgDKiZIk0OB2EYuBXoZaK7r9gFQiBuuVuZBNKkeR9EF4A50ZnYLHMS7-PVycXz9vOI1x_MDIOgklBckSMTqVNOyMukRbqBmhLmQ-5ZtjwB7Ko8eEJKA9ADRoq9372Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77979" target="_blank">📅 00:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازی یک یک تموم شد
بهترین نتیجه برای نیوزلند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77977" target="_blank">📅 00:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محاصره دریایی رفع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77976" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.  - تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77972" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkqxsnw5HzgsVNlSQT0kh0PbPk9lC7V_cWwO6EbjxZ8IFVolZsXqK0xzehpDGeRlkaTgITQVIEYMPboazHw_slTdP1Icw2VS_jAN_fMe5aSO-LJh862mkTeNztzbP3AqjdiTMdhvep5Fd6MF-LA2apyfRtD_14yC09FpxxODxdwRdn080FvYUZ4b51wIUH6ZOA1EyvnQHw6ha8QIevdE4N7EMUZciUaHPVsooWfLktmxwkBXrfhOpxRRv7YQYZkCImsK-MtzfKIrc4aLSoTWrCwFfL65qmkkSvKDaFRse95-pXfjynTY2w3RZdCskOujuKmx5dn_2GR449bbRTdjGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن
وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.
- تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77971" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DECKFVdBB4qAAgs-xRDxU2-gOlQ28u7ruyCaREEj07PiK4nq0I6-kRq-l9BqNJvQUuIuyzmczR-aQrxV2_K8NvAzKmWZ08EZArUe_VH8MRyB-1Z_s2xN4wda18FT7uCd7q-o7L2eRrJv8YKo3sZF3WzZnhLzYbuDY6y1Mn4gyga9-XtmUFUN-uDX3RYZB_ugjdrShujQqTDVhWH4p5TLNK1pKy2xoSACIKLt8plJYPNtVJs-T9240PcIBG4bb4cGehJODa7_nb5h1gu_ce2GD3emYbyRwEoWYFweUw9m4x6U1ZudKHIpPxTB9dmACMr3ki2HTLS2ch2-3ABsBl-3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان یو واقعا کونیه پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77969" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCwNzqNfeQWWj-vO1p6wQf9W0CIyfokBItXdpGqXOlFFBLyLaeC4YlWbUsnaftJbNjL0i86KajtKj-cjlfvlxo67_oQfqExSugrKnggG1HsQcQPun0f7u8_s9ztnUQDnoxY6t452Rr8q4OQJkmF3yRSwr_4HDGUq-snfq65Qdbnshtyw2Tyu6d4gDGxk0T2208wjlm49StmVmPK5D30jq8JpOfPzYDEDu4U12rw7htRoUS6T8FReExtc9U3sP1j12bMqQvEkVpFqVcbeFYsD9FQNxdk4ocxAc3wB7xGBxYzNIg_ZjJltBx8bbn1_h-etLHfqviSk0TKJn6AT3Jzi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیکای قشنگتو بفرست باهم گوش کنیم.
🎵
🤍
گپ پلی لیستمون
🌓
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77968" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امام عاشورا برا مصر گل زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77967" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77966" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اسپانیا بدون یامال در حد پرتغال با رونالدوعه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77965" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کیپ ورد جلوی اسپانیا متوقف شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77964" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ریدن تو این بازی باعث میشه اسپانیا خیلی وحشی شه و بقیه رو بگاد و قهرمان شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77963" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peMFP3cNhE4FlxDEGiMxpJIsEsHpzjhQqNX7cK9oOLYXt9-C47D02WXVyYYuDhSRM49lB6DaMEtKawAt3XBRVmnrNX8wVjH2CV2iCEQ7bK4Yjplp_hGRiYqZq7gxfLUVMKf3xbcvTlZ9_bt0wOjbKovPR-vK8TnXRKvfiAbgjXbjE5GGgmw4cs2rlbO0QN5_bBV1vZt0CF63GgAw8nO9hqaGb1y6v-THwHOQ87DQnrOdfN1-J1gtUXfcZFgo_BZbyCH7M2qyQnl86Ys0K72wMmrUS5YSUQJt9ueS8oU5GLdr1YyZmNoTLFYipQtz6u9jPwgnEG0JbF_XqG-y8K5zfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه جدید باقر شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77961" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77960" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قهرمان جام جهانی ۲۰۲۶ خیلی ریدمان شروع کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77959" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77958" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فردوسی پور هویسن رو آورده برنامش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77956" target="_blank">📅 18:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsczY89Y9Hy53xyPZQS2HkiMpEBW3E0jEI1_0gg8zkRtPGk7yicipi8iPR9F2wLAHhB5qkvVdPYTvtK6nnOCdvDCyOqXLPATgc1WZn1J9Bt8ggEfjK7uaze1xtWl8Pp-CCDOIs0FoXoPgEP6qkxhCpWUl6SSbZAi1EQwfIekbLbAm1Ll6rL_Mqekr3qNm6l3lK9e7pTSprLmUp-Nc_pv7HvEC_l2kMThuwl-oEY9iqqSEOwWyZdZa-uUKDCu7horCDsbrak0T6Hjf_C9hMftW5f-24FCZG4OPApuG3yO-kKR8VH-aQOpFl4FsCNAmy_AH88IbMoiZuCI01uOVde6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGf7sowcSnMITIDaevIpji2HumYTZnGpynClWKU74T7Aua4VXbHJZ9vUAniG1AuQ-51_fnVWpue83I3tllBjAsPA89O82zOy9qVsvBFjb68bS2VyqXz3GFvM2ryGdOgHE6DBjxZXPyyVEDURsBVzfM1dOO9BGIBknt7-_OoNOKLYZEt3a7RR_qKe654QCvXx_31iVhLyX7z51UAKR_f--LqDnp8h26UtrcLOdY6a4S0aTXCkDY6Rl1JU48TE9qJKXE5xgSfHoqCVKKWTksg3smLPH_GZnMuKxCqNbdkWebbH9bDfjKr9zlyoViDAmddlXM46_hNaLV0cPHnJut0ExA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری شوهرش همزمان با استوری خودش رو میبینید، خداشاهده شوهرشو نبرده عروسی
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77954" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVmN7jgWLMk07fYA5A7sHUq6z9cMYj0gqihHGf_2cvqlF-eJrnsMHhVpyqkSXUc3sE12E4R5Uf4RoPXnOpazKIkGdisBAQvvRduhHbYb3dO-bqVVTBMTmLoYjqWa6NjI7AFNTjIoA0G2FLzu9NxmgrIpc3KkiCq22IJEZs_QyrBATj1v1WyOk5vNnAbuSd8J_2tz3sW9l9bjkRhK4bOT71mvVaFky_ZAng22rWhpCJOD9q3mjyJsj3o3PAk_PWaZweDofUzB9QDF8UPkARjaeRd8WydZnaJs5XK4pf11qwPxJ0GMPyjU_ysVwhErOEzKFiUW5KIS59tR0rcnkW7VPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77953" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77952" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD4oRjIOaWXkUofRlKvABjAfeRTT-gxNUArSq70VajGP9N_IQe5xgNSzvv4kqcXJT4BF-70LLbFsTBDy3Uj1s74boqFiIWY6hKifFwoPYysSjYJB8ovRYyNTdlBOEYDeVxLW2C571I9AbawHMFlEosnuFlAMDiJ5RlLf_rWiyMzEMvJoxOVs_hjwUfANxBJBJCM-JncHYufhJSVKVzOLIADZ-FaXqYRBdvEsUR4eEAX82T08WF5-w7WBIvdjatzAAgomJmpZopfJhhNbaJT88g-7BjzIyjaPAFdLrvj68O949Zwpe7fVrN5uHrHNVIPF3C1yDT2lXQrfs--n4X8nRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g25
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77951" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWfPd2eJgHUpYPRFEMurYtxsvWIZZ3dkJ7Bww5bFpzaK6Eig34QpPj6IQ5Zp0ZT0tO3F0FZDeVvtwOBJ6B2627lAw8mRpTpAcPyehkZf0H2ZCIHg38bb6UkNjxrb9YKolYsIcEOYX5RlNt4HSOc1ZOdnsUydY5QADFVWO7pl4luNAp6CjbOADknmtWeh3qa2R3P0g4M_kQWLeVesVVLH3jzlDPHAyJRiE2lKryQsyjvhhuDlk4dHdtuHYQLyVMGUV-7eDBMwGIvgVNLJSOuQamNM_gTS3KOcF-7yYBKpQkuBF2nfgjxtgdTD3QWpl5-13irYwMHYpy4RiE_9a8Tsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیکا بلوچی ۶۱ ساله
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77950" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy-ewuWb4zE9G_N9yAJ1DfZVp59l9bWRT7yCPjJL0AEe7JfoN7rJFpsCm_8q8r0H5qHolvyKb3C6imzERUSFPkXxjoZ65OMgzuUHlnswi_qgWBVJhoV_WgIpPK_FO1dkFga3w8kxYIUtfm1x4lO5w723CgkaiTXX-FyR22iNZh-w4Gs-CwLN3jYrNjLaK0DgtakFkXEkGm_YF4G1jTF5jXCgQoHZ_nTG7p4vMbjbD1KbsETk7wwIREyYDq8ecZozPi5svZLRofh5UKeFhtWx32x9hxGBySVjJNKubtazD9sRfuILeZb1PtsOd76J_Q7uRG_XbZhOW5qkeIrL1fz5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
ببخشید دیشب کم خندیده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77949" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZddD1wd7Vgt7eV0CCYc5YlKi6iirxQr8hHAdfU9BV_HTpY1d-rksj8N99uppSJus0Wd_YRM7m8rQMNvdwx9FSF_-a-7xKXNjZ2J7YDgX0wD1dwtYjgcl9OzoQLBlcdjTZodAl59G2ir_qr8WVLohOToqqrDnCxNU3Vt6qw51sWUgt0kNkF0uFqEMxteY2Tn2ivKrmEhbGWPleEjtWSdPu11FM-_hD6foecIOA3WG6kT6-1f25mNTTHZBn_aU7QJuKAnor55fYfALKh20TxR7e0HZFyEjPOFWKO0WlIkINvRSuQSeN-OLHStpaAo-_PyZt3rd2n3yvYE1JBTmbUsXOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو وصلی؟ نه انگار کانکت نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77948" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">در چه حالید دوستان؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77947" target="_blank">📅 13:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یعنی جدی ۳ روزه چارتا بانکو نتونستید درست کنید؟ بعد ادعاتون کون خرو پاره میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77946" target="_blank">📅 12:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzoi91qqq4-RUO95oSxyNQjw1qs98vWsAhLvsbTk1a1Zr7ZqafIuZy9FClJHYJkvkF5nVUTySSOk4Q0Qv-97q-SPzBhOYvIbdIh4DMH38_xUYXI3I-YJ9vPENqxQaqnA8gRchJhCT7FkXf1FCDTpQlzywuOTSFLZKNh-jA-ME4TaMQaYqfKQKm7CfNsx9yeYTdgrXI4w-4NkvIsK3QNohO2-TQ4jSeJnwXJYbQjgjHW5K9HqYuyKZzyHdtLRI37Msyn8VRtjIotnrkmxB51uaPJCSQu_PtJvfBIBBcMfg4cQGKE1wAsVlXP7kGdh8LCBtDCTRgR5QITNVFFgBatDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید آپارات چنل یوتوب داره؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77945" target="_blank">📅 12:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77944" target="_blank">📅 12:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">میترسم حرف بزنم رئال منم بخره</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77943" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=nMJ38pF0djIGyLb7s0OLDja0efCTTBtAfp9HODIlzehT6Ynk9-vnwNJ3gvYIbChzlDqjGt9jsQbbfYQLn4l2buhjgzK-uy1K2L1XKCEG5EzTw-i4PqFEi6L1DhfQnCg6rSGM_VPaUebR1vjQh5EOY4vrsFMy3eYgxL8ahjZGpVfiIophm_p8tlzk25b_rK31c24V46CqLK7FULJQCr5vKHSYlZt-UkZ99-0_3o5SQX6FBsfQ8MX0Y2O7tUx7DuLd2j1xyL7fIBx_0tuFdJyHPxm1esvblnnp985NKlHnujts_c0X0Z-UfJvELhtrElHeebBo48ITuqYNzlPn_h-wvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78832f0cf9.mp4?token=nMJ38pF0djIGyLb7s0OLDja0efCTTBtAfp9HODIlzehT6Ynk9-vnwNJ3gvYIbChzlDqjGt9jsQbbfYQLn4l2buhjgzK-uy1K2L1XKCEG5EzTw-i4PqFEi6L1DhfQnCg6rSGM_VPaUebR1vjQh5EOY4vrsFMy3eYgxL8ahjZGpVfiIophm_p8tlzk25b_rK31c24V46CqLK7FULJQCr5vKHSYlZt-UkZ99-0_3o5SQX6FBsfQ8MX0Y2O7tUx7DuLd2j1xyL7fIBx_0tuFdJyHPxm1esvblnnp985NKlHnujts_c0X0Z-UfJvELhtrElHeebBo48ITuqYNzlPn_h-wvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول یک قیام خونین رخ میده نتانیاهو و ترامپ وارد جنگ میشن رژیم جمهوری اسلامی رو میارن پای میز مذاکره اورانیوم و موشک و رهبران رو می‌گیرند دو دستگیر و تفرقه بین نظامیان و عرازشه و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته  - ۸ سال پیش پیش‌بینی های مانوک…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77942" target="_blank">📅 11:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77941" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دیگه زن مانوکو گاییدین هراتفاقی میوفته یه ربطی بهش میدن</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77940" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اول یک قیام خونین رخ میده
نتانیاهو و ترامپ وارد جنگ میشن
رژیم جمهوری اسلامی رو میارن پای میز مذاکره
اورانیوم و موشک و رهبران رو می‌گیرند
دو دستگیر و تفرقه بین نظامیان و عرازشه
و بعد سقوط با فروریختن رژیم از هویتش اتفاق میفته
- ۸ سال پیش
پیش‌بینی های مانوک خدابخشیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77939" target="_blank">📅 10:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77938">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مانوک ۸ سال پیش در رابطه با قهرمانی یک فرد ۴۰ ساله با لباس نارنجی صحبت کرده بود.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77938" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaPidh3gCacn5O3R9Q8xupkswnhHMKZZQiXhKkbi5Hlt-c67NSWtVkJ3bd69wT0Hssha8mZ7s7a95KDXbmzsBedatcpu3vbdUyDefoPvwAFmohtamM7Pd2Gy1onOd2Q00vZLb2r52v9eOter6qfh7SevDKJcV02AcfxY5uXRdCJ2R6-EwJZ_sPNkXRUiPJ_OP8ehacsPkA2dbET9Msg9C4Fm5-u4iel_BHyP4_EXR_KEPJVaPbZ1BNDeSqPbMy2mMKVLVs3lyU8lnTP387rfiv8WopkRnsO1TNuNf51n32OcnypeqQ4liMGTBc-jOBMAfh-mbjOGfQG0LsEKkcJrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که جاستین سر ایلیا آورد :
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77937" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77936" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYU9J5lannjznYBbO8DmwNNP5vui66ppyojjq7gajeD74Xo7gBnZfTtGYWTXTN1-pUpi8ua4uH_YsVq8qWJVrVs0mDI87hVhjbZxCdstFIPFqbTCpHZhlE7lx4U4c7C6U4uXhhwuTe66L7dp8zzSTUaE0Sc7HzcWUIDZdmS3yckre7ZwkY8GvmKGk7Om7LTDi4ZGxIdga5TEsdcTJDMwcVNskmpjzVfc5GmWKekqrm9MZcfgboUju-Gmtn98TPegsHr8EmuluhyDLTwZSBtF4CARFYxl0eDmUS4RQLov5SoBybzXzKvgD4N8lkb6Zsobl5ZyfSLOJJYbCR8w8iUyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r25
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77935" target="_blank">📅 10:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZEKyFLzgcIhrJtQJZW60GL3poAvh7Udrz-40avT5PXRHGY31A7md2iOYg7qJEOHvRG1yYsseu1JzcpOtLlMcKzSgX7_8XbdNl_5L3kdX7SqS85zMOau1EiwchXYiVMpDXglID-s-qsenV_LRr514EfISxzVUD_38pwcqjbeJuI7Z3t9SwLHDk8UR1-ZfoOTCkKNAQw2gpJoL_4J_GtH36UsdyuA6Eg_d6uF15wZ2ZR-dKuYuA9eyu6g9aB35yddLUhKdq66ROxbShLoLfkwpKsI2I5tiLgi22MsFtE1XwYeYZ--peyRixBcoYCA-mxJG7ZB1x5ORyv1AUdEhkjkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنده خدا یجوری داره آب می‌ره که انگار با سیناب رفت و آمد جدی داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77934" target="_blank">📅 09:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توپوریا مادرش گاییده شد و تو پایان راند 4 دیگه گفت نمیتونم ادامه بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77933" target="_blank">📅 08:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77932" target="_blank">📅 08:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1DxKMaCS6sKt8jCqm8q2YtcNR3Kdg-DtEEVI5JEvUX0ZUyvlk2p0Z_XiCT1q12KDDOqfqbR3asopJC3Cqd2aIJKLSFcrkZ7sylkUNJuU_HIc8zZnses-Wm7V0rC52H8veA8gwMQoY8Glb8keeHFItG1L1Q4tGfeuSupTmdX7cpYPvJ7VG5bU3tqZpqvkzTgoj4VHkEf3K2cItBl8peGbQbXRzrzk6pwWXTd-dQQ7rq2izMctnO9tti08V0sDlq22OjnuKOIZYu0iYxgA5AEkuJkhCCNd8w__ZF1cYkYHAznKqxOBH7fX9GJ6Zgcv6rZ4llVPA15lKoVEOVXcMRNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بنظرم تا نرسیده فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77931" target="_blank">📅 08:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گوزیدی داداش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77930" target="_blank">📅 07:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nv2H5ko8XugSKk0uNLa8sA__LlqoYj_FyHz8dwalOsGBGjJvDufHeKjs2rwBC6U2-MYGQyMaMLkoXYMdrtAHqJumF4otY-_LRTp6JRh1E8GlPyS905XiFbNDBe7LD_JkaezhNxzkOEo14piZ8J8GDt1I3ilLoAEFc7wyIVcmgOt_OptGWsadBFe_K0_7fcbJEdq1vM7vEBhkxuuQeF2ZtVrYWPJhUR7DP5tzCwyTIMjNL8zcJf7_gQHj9flfJUU3Gnx4HfG38bNOheKvW6p88BU8tX6nPjM6Q9tQGl_k7gQl-KKdGjpeSXTHwOYd1KCKsdOBVs0nFvelkk65QbCblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوزیدی داداش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77929" target="_blank">📅 07:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-nK36ymHuxXvDwIHeYY5FQnDPxgI3MtTsKjMCAMCWgfm9XRdxMDxH-xptADuoOqiAxJwfat0BVtz_5zAC0WBZe4FCBjHgzVV1G_OisFHpwtpTILji4prfThBi8ZhLCvmJfPw-vEfA8vBjTzoELnZ6xAwRT1C7WHXLVoTnF3n3gUD3_285QU88StOY_F2iaQcHagf5Zyypx2RXlAWY8l-_Dmoh6DN790z9j1PAXyayXqIEmGyvfEwBgejdb025SOp26v6Aes-O2-D3hCjzLu6X-Fwoap7BFDaBrVE9q-06JUGVhhtabmDPJLi4Ja6MLkHC5QF35AnQqGSboNlfRoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77926" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">از اینور هم خبرگزاری سوپر معتبر مهر هم شرایط ۱۴ گانه توافق رو از قول خودش منتشر کرد که اونا برا پوشش دادن زیادی خنده دارن خودتون تصور کنید بخندید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77925" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">با باز شدن تنگه پس از امضای معامله در روز جمعه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77924" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVZrERTAXr93q1QyvM_pc3Qb3yjGiHh_ERr2FDb_D2pF-eMIma9a5tsujey1K7Z-C8E-SIe0l_pUPnMc5LPicX2I1tIy0JPQ-eeJFsvyw7o5en_GfUO3irKhyyCGnoEemwdbUMOTYn9HEM35neYRkQSn7DU82JvbBkwaYD53_P6IodirqvdOaJx5ibn0XtRmqEGwpyNZaefAPIDn0W_jB0c2GxvFPKQeKFmNaxNBbi6hinfpjUYzvgZz8Bp6ioKtdj4ZQc9HM07hLNWd8j3qBmpDdzaC0nPg2xGYcu1qnTDL2HabWMOQiLQrHQkZKpgWo45JHk8iDo_a5BBD8TslBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این معامله بزرگ، صلح و امنیت را به کل منطقه خواهد آورد.
بسیاری از رؤسای جمهور تلاش کرده‌اند با ایران صلح کنند و همه قبل از من شکست خورده‌اند. (اوباما به کص ننت خندید)
رهبران منطقه برای اولین بار رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها در دستیابی به صلح واقعی کمک کند. (هنوزم داره می‌خنده خوب به صداش دقت کن)
با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77923" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فارس: ترامپ در ازای حمله نکردن ایران به اسرائیل، پیشنهاد خروج کامل اسرائیل از لبنان و رفع فوری محاصره دریایی (به جای رفع تدریجی آن) را به ایران داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77922" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ویویویویوی خبرگزاری Ynet به نقل از منابع آگاه:  ترامپ به ایران پیشنهاد لغو فوری محاصره دریایی در ازای عدم حمله به اسرائیل را داده است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77921" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=qAYWu6yOtAHVah9e16iysEunH37sGXmIcSi2WO7rbeo_BgBluNVQ5IQpSBrOuC1V-0GBatKtBH-ABlJfjj5vZPn6pQUq-GKMXbazOCnogzv1F0D5kfZ1CK__WlaM40ZuK7K9QIDCjeAI3R1pco4LRDYZ7NV_cx6rrrZjCxL1HiLOu5OjdWyshnEKfGgnrCB5uNRMe_1p5HZxhzEOhpo340IhIuHG_5j1slWLFOWDZx4mW89UPBhAPp47qy5lyE0aUvs4q42LzAEUlDiRTTWz5o3jgSAiBid3L3f5nmrxmPpEZ47-j53k789B5JX9rN3AuFXqSUnArTillT_6M2MUIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=qAYWu6yOtAHVah9e16iysEunH37sGXmIcSi2WO7rbeo_BgBluNVQ5IQpSBrOuC1V-0GBatKtBH-ABlJfjj5vZPn6pQUq-GKMXbazOCnogzv1F0D5kfZ1CK__WlaM40ZuK7K9QIDCjeAI3R1pco4LRDYZ7NV_cx6rrrZjCxL1HiLOu5OjdWyshnEKfGgnrCB5uNRMe_1p5HZxhzEOhpo340IhIuHG_5j1slWLFOWDZx4mW89UPBhAPp47qy5lyE0aUvs4q42LzAEUlDiRTTWz5o3jgSAiBid3L3f5nmrxmPpEZ47-j53k789B5JX9rN3AuFXqSUnArTillT_6M2MUIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچگاه علاقه‌ای به تغییر رژیم در ایران نداشته‌ام.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77920" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شهباز شریف: به توافق صلح دست یافتیم. جمعه امضاش می‌کنیم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد. پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77919" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این زیر یکم فوش بدید خودتونو خالی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77918" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6OZIFAZMvAfFq72M3oHXs7fPIG_q_Nz1cmTlxnWcKfegbpvdMcLAlKcrrMDZ26Xt4W4eDD6K4E4CPEdzB0xNKdsbv3Gx1uSgFjsCza7KHQJjsah7kCvrbGZQOJx6sXjJfuptdLuCQEId8ezkJltrfSjjt5D0DDn1g5CZ7jICpMtd62npIyI75dIyQ6UYIfDN8HnSMDSALFdYsS1pcya2mYC8PDEKYy_l3aRqvfJI2xqhjB3d9QCWicCd247SuopmKTErQ536YPT1TpFckM6C0nyPBsSR_DE_Sirxnn_8qUNiih0ky6kiobBefUNlDEeYO8Id_H5FeYazYxa0i-8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف: متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77917" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ژاپن گل مساوی رو زددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77916" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:  قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است، اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد. این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77915" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
