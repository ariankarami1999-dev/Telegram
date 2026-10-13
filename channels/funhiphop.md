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
<img src="https://cdn4.telesco.pe/file/YCYF6kahegkRptXgtw0mdFGZx3gwxwrDy6DPdFJFZLR-RJPN3_9nYncmuLf6mdmqnc-7neShtQT9BdnNpePFoBzggWROH6IZ7XVe8aGOjJlFoU3jVd7bPB9pE-BQIZYVXHWRw-2CfodRl5JPGwa5b9pNsa4ncegA3_GMO4wgWxj1HP3s3EAK5BurS7AxyYBc1btEYlxIi-f5rUhr2mosbtXFpAznzcPpJHpizHAK2hpDHhn6iGnGoJt1AGR4vHJye8ZC3YkhWrTsmVeP98ELnmDYXSAOMXNq2TxXKUhOPcJZ6ttTpyO9a6L0kBucPo4M2htAfxAspUUWv8OlmLXm4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 269K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-84779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=JZj_A6BX7OMrVtdno19ppcIdq38QFXe4HivTG-G_WekIAComJFwI8c9edZMLJ91rwnBNtEG2RBFqrgqgP_pKCUm7hnB1dwheHoGPurtohIADuX43E61oSWbTPTpA_HXT-DqLKY_jFaWInDKB_R0T-NoFDTyRyXU_7a-tUSx41FU9lxvjc2Mm8BZXhPDofouFph424R6Ss9v7HqGHKSZKocuVi5M-FtzdUHHJYGrAjcRi0zqzEs85RLwc_Hjqy8_DVEG1TBravCuNAm-GCasTmCi5u9f5UbUuFBjxWGseUKXAw2KWjTxWkCvE_z7KocBykri_qhdwCDN1LDJHAa1YkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=JZj_A6BX7OMrVtdno19ppcIdq38QFXe4HivTG-G_WekIAComJFwI8c9edZMLJ91rwnBNtEG2RBFqrgqgP_pKCUm7hnB1dwheHoGPurtohIADuX43E61oSWbTPTpA_HXT-DqLKY_jFaWInDKB_R0T-NoFDTyRyXU_7a-tUSx41FU9lxvjc2Mm8BZXhPDofouFph424R6Ss9v7HqGHKSZKocuVi5M-FtzdUHHJYGrAjcRi0zqzEs85RLwc_Hjqy8_DVEG1TBravCuNAm-GCasTmCi5u9f5UbUuFBjxWGseUKXAw2KWjTxWkCvE_z7KocBykri_qhdwCDN1LDJHAa1YkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست یه خانوم از اثار کتک خوردنش و 10 هزار کامنت این شکلی...
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/funhiphop/84779" target="_blank">📅 15:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi</strong></div>
<div class="tg-text">بنظرت لیگ دانش آموزان بلاروس پخش زنده داره؟</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/84778" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مرگ دختر جوان در ژاپن بر اثر سقوط یک زن از طبقه یازدهم
زنی ۲۹ ساله که قصد خودکشی داشت، از طبقه یازدهم یک ساختمان به پایین پرید و روی دختری رهگذر سقوط کرد دختر جوان جان باخت، اما این زن زنده ماند؛ گفته می‌شود این زن به اعدام محکوم خواهد شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/funhiphop/84777" target="_blank">📅 14:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کل مصاحبه گلزار فقط اونجاش که گفت اینایی که پولدارن ولی مثلا برا مردمی بودن به خودشون نمیرسن و درویشی زندگی میکنن کسخلن
تا خود صبح باهاش موافقم، کصکش پول زندگی خوب داری چته مثل کیرخر زندگی میکنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/84776" target="_blank">📅 12:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=syvbqVqfODQ978MGkzxzQpHtgLAqZyTBgPJVR83xBOuva7eYAvyoUep5uHnTsdxVpEaHOqhly5TSDO1RkJ0_fhrMzBKNP3AK4nwaCuim2Tc0zIRx5G3rJZNw0EQ-9aZ9OmIEV-LbXN7yWBJ_MfyQjlVKejwkI90UboUNtr8HV-JgBju7g6mBNMFK4-rjLvRU6swwWdF_I5pbr9wxDhfWDHJUo10hVQEUsmcdWXHXPQmXB69U2Ox4PxTnS-aYF31uDw8M-wkm6YQAznAW9U4WtaRJYeFsrygq-RrMexkKzXOwOvpptp6mdzEyV-zGHyeDcRD7thM1iaEMTKaHivt6VYDtQJ6g-JIrX7NIgEehNaJYTYa56MiGyQPJwBdIFDrb-1Z6kyO83gNY8tkBfIpmyBzuZMEX4OxYuYn6BDFf4Xw_o9tHSxB9B93QycAPIGg2aA249wWwoVe2oryMy_RVJufvd6xb-A0yIp0fKodnXG4jhNV_J7R7diYNlS_B7e_TuRTseUOwtTHVBGxdBtoilOlwpLBFZRWBRBkY87Ntnjc9FaicPCPMJuTVblZMAX7vDFjTTLP6yfELuv3363_z4Q3bfA9URjt_7r3ScOzBs8wm82MOg_nl6wiuWy7Aev1tpW8OQCrdXur2PvQVRTlRAY-JzEm2-zVjhIXQFveW7qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=syvbqVqfODQ978MGkzxzQpHtgLAqZyTBgPJVR83xBOuva7eYAvyoUep5uHnTsdxVpEaHOqhly5TSDO1RkJ0_fhrMzBKNP3AK4nwaCuim2Tc0zIRx5G3rJZNw0EQ-9aZ9OmIEV-LbXN7yWBJ_MfyQjlVKejwkI90UboUNtr8HV-JgBju7g6mBNMFK4-rjLvRU6swwWdF_I5pbr9wxDhfWDHJUo10hVQEUsmcdWXHXPQmXB69U2Ox4PxTnS-aYF31uDw8M-wkm6YQAznAW9U4WtaRJYeFsrygq-RrMexkKzXOwOvpptp6mdzEyV-zGHyeDcRD7thM1iaEMTKaHivt6VYDtQJ6g-JIrX7NIgEehNaJYTYa56MiGyQPJwBdIFDrb-1Z6kyO83gNY8tkBfIpmyBzuZMEX4OxYuYn6BDFf4Xw_o9tHSxB9B93QycAPIGg2aA249wWwoVe2oryMy_RVJufvd6xb-A0yIp0fKodnXG4jhNV_J7R7diYNlS_B7e_TuRTseUOwtTHVBGxdBtoilOlwpLBFZRWBRBkY87Ntnjc9FaicPCPMJuTVblZMAX7vDFjTTLP6yfELuv3363_z4Q3bfA9URjt_7r3ScOzBs8wm82MOg_nl6wiuWy7Aev1tpW8OQCrdXur2PvQVRTlRAY-JzEm2-zVjhIXQFveW7qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فنای گالاتاسرای دیشب جلو هتل بارسا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/84775" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یعنی هنوز ایرانی ای وجود داره که فیسبوک استفاده کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/84774" target="_blank">📅 11:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84773">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗺𝗶𝗻</strong></div>
<div class="tg-text">ما سیاه پوستیم((((؛
همونایی که…
بغض نمیذاره حرف بزنم
حرف دلته؟
خب حمایت کن سیاه پوستا به حمایت نیاز دارن((((؛</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/84773" target="_blank">📅 11:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84772">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">من دقت کردم از وقتی فوتبالیست های خوب دنیا سیاه پوستا شدن برکت از این ورزش رفته، چرا انقدر عمر حرفه ای ورزشتون تو فوتبال کوتاهه شما سیه چرده ها، ملت هنوز با مسی و رونالدویی که تو لیگای پرت دنیا بازی میکنن کری میخونن واسه هم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/84772" target="_blank">📅 11:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84771">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=vJ3Eg0sivltrADLb4N141pnRFO73K89pv-eTYraqf0p-G0bEwrvLDjSZEWc3Rg_pQ0GnmD0vq1NLtt6l-jkwf24THPU8WOhBLrt3CcCnCXs-pkUDq0gjymSUlntAKjtZ3rzjogo5D6F1G1GbMkxB7_R-agmTPI8a8qzGfQubBt1uznRtF-L7j3PFs2_1PPdiQ0VijApQtILcVxH8mwnJzbV7PQ5UauZYx3h2fRbevcnO3UGm7rrM9GlrjDLq64EWe-LO_JnTBOHFxT1dF2z0Qwue1xR_KmBxZ0n2EiJKGnDXjGCKP34RLH8VAz6LgPWR0-95Ut71jh_0iBvk5WcTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=vJ3Eg0sivltrADLb4N141pnRFO73K89pv-eTYraqf0p-G0bEwrvLDjSZEWc3Rg_pQ0GnmD0vq1NLtt6l-jkwf24THPU8WOhBLrt3CcCnCXs-pkUDq0gjymSUlntAKjtZ3rzjogo5D6F1G1GbMkxB7_R-agmTPI8a8qzGfQubBt1uznRtF-L7j3PFs2_1PPdiQ0VijApQtILcVxH8mwnJzbV7PQ5UauZYx3h2fRbevcnO3UGm7rrM9GlrjDLq64EWe-LO_JnTBOHFxT1dF2z0Qwue1xR_KmBxZ0n2EiJKGnDXjGCKP34RLH8VAz6LgPWR0-95Ut71jh_0iBvk5WcTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ ام «گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، تو فلسطین چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند . البته ساختمان چندان بلندی هم ندارند ولی از آنجا به پایین پرتتان می‌کنند. با این‌ حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/84771" target="_blank">📅 11:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84770">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBgI3aZbFGuwlSB3dD4mHRhyyW54KWdhhT-1TiktvqEHpyHmhvK7dklK425wSajhTUVu2irz7UF0YhyMoh3zAQD-RnqFHHlKll9gO249Jestbk_DmjXJvxfpTLyQ_s1NCB5b908fMQFW7T_YrzO0leYn19QH7MPBcE9EArNKI7wnbRVPdIQ_IPEoXgUOo2HRD-OjjpuJ8dUDllX6EJYT7W6cvcgRyz3r0l6QfQ7nLpZ79PBmBQAYFcL2UArgqABXsYPhFk9T62uNG98BjauPzpb-4TlSA80k4cuS2RDoyF7rwFQa6rBVZZ0et5_2fVxIR9iOk8msFIrZRcll7uQvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت دیوار پر شده از آگهی فروش سبدهای گل دخترهایی که به مناسبت روز دختر، جعبه گل هدیه گرفته‌اند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/84770" target="_blank">📅 10:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84769">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84769" target="_blank">📅 10:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=XAHXQeib4gfQgPM6OGquyETAOvnPrnEN4wZGIpxiX6lK1L1Ac_D-QFw2vc46OoVssPNKCN6L7XEBt4zBKpKRfMmFpmVAavChUEi74-X0eGJefWnIyF2ih0ui61j4NgZN8lmJ5OTHV3ygmlASMrtpVWfULzRJcxEpmj3agk75F-XJz7y7csZk_ztY6DA_N8QOY2vqa5xMc8ALj4PsYZG72RB0W9sbVXzEtO1nGJ8SfE28waMhDjG93leJyD15jW5XQpcVQfyFBfmpdOhgbpdUfkfHQlcuD-ENMPfSkR0C9cBD4IzGFLDl64BGiWhbLlB2hgefAxmExvKbw3Cc6h9GGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=XAHXQeib4gfQgPM6OGquyETAOvnPrnEN4wZGIpxiX6lK1L1Ac_D-QFw2vc46OoVssPNKCN6L7XEBt4zBKpKRfMmFpmVAavChUEi74-X0eGJefWnIyF2ih0ui61j4NgZN8lmJ5OTHV3ygmlASMrtpVWfULzRJcxEpmj3agk75F-XJz7y7csZk_ztY6DA_N8QOY2vqa5xMc8ALj4PsYZG72RB0W9sbVXzEtO1nGJ8SfE28waMhDjG93leJyD15jW5XQpcVQfyFBfmpdOhgbpdUfkfHQlcuD-ENMPfSkR0C9cBD4IzGFLDl64BGiWhbLlB2hgefAxmExvKbw3Cc6h9GGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل مسی اسرائیلی نباشیم
☝️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/84768" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5hXEQQTiYbv9DD73xSwijX8TSEk1IYHrygmxlQeUb_zDw0kxSHYUTqMpepRY8ucts6vpyWLSKnZBOfIRwhtOIypuEoAq1zGnlUVMrECw0bolcx1k73vUIqC9gyU5andipASrjrs01MIcrLyvAsx87IGrXQ69yMhq8gQo7YwaLq1mwzt4933LLtpCrOfsyIylTfS7fau-yghlHo7nGejci963ybff7F1_MeZPzYgLlWQp75Q2uSuajDS1-KxdHSXbN5DcVFYleaOpA6FXuQX2vRuI4rLoiLU71p4Sxx_GzzRzJ_j4UVlp-ON0nvSq_tZZAtBPqkdwnVgJ962rnFo3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/84767" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=jM5Sn17kF9zPyJxb-u4nfCJcbj9L-okFaeIpRJdxgwzRTfgmFnQaFMpOjMIi6tKxQ0kfXX8M9egFEjFLNxIcETwxac6okz_vCUXWsNU_9nPMn7keFsT9r_bSkVL9dqOB4kuH5Ek4KD5ALPRnxR50Bt8ZOXRK-ExcZRYIfLr5T_gw712Z8o-8b2YNWI9F0s6XURlXUs8v8J0IMG6GqQP2QE6fGNt5Q5iGDmFFRVecQtYJuixOMo4ahJNrIgh8u8_JM9KUpRIrURzAitVDe1no8RDH7o5XjcVsxXh8Ocforuy2lpChiSHrTYOoKQVU1TmzkThwZ1UirUFDUqOxUOf9WBqhySzcsa0ASfUyhW4qislRzqDoxP6PEVMvSLOeGS2WOhHkLXXNmKg25i88-AKMkNam0aHycabF2HKrr1ZWXu9x6XJBfnQd5MTJXN4JvNFhdcQvL3C7lzi7q0lMjQi10HmMRD7XsyFQGrLMIy1YS3gLQwVtPyKIEBmaOARLUByP_3AdsbuD_Y71HcUFZE1D5TNoqpdQo1M-ivGAZ2DWjryaK3mbetICyV832oK_kJZU5tGk1R3PcZz979t84FwEOkm8MV1S8FmVWN9Dikie_Z_rE12ervpbbX2E6gGgtN3FG9SA9ukUMDvAIdKnI2RzC5kr8y186ZxKUjulR99H_ZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=jM5Sn17kF9zPyJxb-u4nfCJcbj9L-okFaeIpRJdxgwzRTfgmFnQaFMpOjMIi6tKxQ0kfXX8M9egFEjFLNxIcETwxac6okz_vCUXWsNU_9nPMn7keFsT9r_bSkVL9dqOB4kuH5Ek4KD5ALPRnxR50Bt8ZOXRK-ExcZRYIfLr5T_gw712Z8o-8b2YNWI9F0s6XURlXUs8v8J0IMG6GqQP2QE6fGNt5Q5iGDmFFRVecQtYJuixOMo4ahJNrIgh8u8_JM9KUpRIrURzAitVDe1no8RDH7o5XjcVsxXh8Ocforuy2lpChiSHrTYOoKQVU1TmzkThwZ1UirUFDUqOxUOf9WBqhySzcsa0ASfUyhW4qislRzqDoxP6PEVMvSLOeGS2WOhHkLXXNmKg25i88-AKMkNam0aHycabF2HKrr1ZWXu9x6XJBfnQd5MTJXN4JvNFhdcQvL3C7lzi7q0lMjQi10HmMRD7XsyFQGrLMIy1YS3gLQwVtPyKIEBmaOARLUByP_3AdsbuD_Y71HcUFZE1D5TNoqpdQo1M-ivGAZ2DWjryaK3mbetICyV832oK_kJZU5tGk1R3PcZz979t84FwEOkm8MV1S8FmVWN9Dikie_Z_rE12ervpbbX2E6gGgtN3FG9SA9ukUMDvAIdKnI2RzC5kr8y186ZxKUjulR99H_ZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه بادیگاردا این یارو رپره میگفتن خلوت کنید آقای بولینه و نمیذاشتن طرف نزدیک بشه، دو هفته مغزمون گاییده نمیشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/84766" target="_blank">📅 08:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84764">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=IKNVdPYzelSnG83ivVcmssfmplvcLucruiecnFgWvWA1csZtDF6Yltiwnw1ndSdLu5HgPV631hNE3BglhfXYH_tC0M4_Pl28vaadT5PvlS1gRIZ8LTRGCLpl-loDOXqPUVvYVIySCNNpQmjWNLgqq5SdVWViC-ebrL-fWaGaUHeFybEJJST5kGVTmevV4YXNDPRX4kq99PicF5iDIGLFJGv69MQj2cjHeBzb64EHHS6qRkdOp-X6txZGG0nkwH5br6eSsHm7XV0NojcWiu2wVPeT4ABDti5rxVS_y22NuiqilvvEG_pqST8HGnBw9zl5_1ivC_6UbnK5PsuzEormBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=IKNVdPYzelSnG83ivVcmssfmplvcLucruiecnFgWvWA1csZtDF6Yltiwnw1ndSdLu5HgPV631hNE3BglhfXYH_tC0M4_Pl28vaadT5PvlS1gRIZ8LTRGCLpl-loDOXqPUVvYVIySCNNpQmjWNLgqq5SdVWViC-ebrL-fWaGaUHeFybEJJST5kGVTmevV4YXNDPRX4kq99PicF5iDIGLFJGv69MQj2cjHeBzb64EHHS6qRkdOp-X6txZGG0nkwH5br6eSsHm7XV0NojcWiu2wVPeT4ABDti5rxVS_y22NuiqilvvEG_pqST8HGnBw9zl5_1ivC_6UbnK5PsuzEormBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورکا حسابی خایه کردن از بارسلونا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84764" target="_blank">📅 07:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84763">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=Odfn0UO5MS38s2sMxNheRFFHMQxs0MaWXL2MZf9V8jqSZOTqtuJ3THAYhzG7G9_u0auHdeHuPLfC0_ykLmMR47Y_G7qKFa5s664vd8Xv04wrAIbaAH6cmoQETnKxFDTtwXxhu4nHysF64lL4nb2c9bD3vvamjF2oi4zDqm3Pu_Cx_6K89yHXpK90JCnrHev5F5Q0fN_apgXtkXhULsaObSfw3XJ40hC81C5vfF5WX3OWkdWjwz7tQKGkwiFtHdDi5Aow0DI52eyPT7sflT3BvkEB4EN09e1p6JAzW0cEEwHz0JW-gX0ebVQSUnAxVmrcYW7l3gPUOsmJk2SMBdC_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=Odfn0UO5MS38s2sMxNheRFFHMQxs0MaWXL2MZf9V8jqSZOTqtuJ3THAYhzG7G9_u0auHdeHuPLfC0_ykLmMR47Y_G7qKFa5s664vd8Xv04wrAIbaAH6cmoQETnKxFDTtwXxhu4nHysF64lL4nb2c9bD3vvamjF2oi4zDqm3Pu_Cx_6K89yHXpK90JCnrHev5F5Q0fN_apgXtkXhULsaObSfw3XJ40hC81C5vfF5WX3OWkdWjwz7tQKGkwiFtHdDi5Aow0DI52eyPT7sflT3BvkEB4EN09e1p6JAzW0cEEwHz0JW-gX0ebVQSUnAxVmrcYW7l3gPUOsmJk2SMBdC_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثال عملی سخت کار نکن هوشمندانه کار کن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84763" target="_blank">📅 01:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfFGYPbEWdmsL2TE159qX8Xg6Almi4RdJtI4T_RKa7OP5Tm0IDeSdrmckRBXgteK_wRCxlwiuWDRGrMEEO0UHqmVmhbg119Kl6eyrE5XUo5KsQJbYyJsE1xvScln8U8miiAYBcU20hZb0vrzUxw6qMPEWabcFGHQYTWBsfkgDy2wHPr_C3T2hLpvMN6SHYDoCVOj9VeGkg5chXWMSP9AQGXlD1b9LlopNOs27L8UaE7MHUUtIfRjbX-9GkVe9H0p9mKq7xnuiYefIzrhL53YjPu-nf0EqV5h6TYI_zYUeqUsS086_ou6VAAkCsGVrASrBi6C71z6qemNtxVml0GzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84762" target="_blank">📅 00:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خدابیامرز نقشش تو سریال اینطوری بود که اگه اون لحظه جلو آدم سبز میشد تیکه تیکه اش میکردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84761" target="_blank">📅 00:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYRarFE4BdUPk0ipA3hx37K0rG8Ev6r1lOfBxzWj8wExf8BfLWUHt1-MaJabj8yW8R2EYTQI6Z95MhtmNKP6F60ntqAESs_Yz8hfIXJkPVvRxYx5zuEWUjQJub4t6Vy3VEKrgYqRrrbYHzdZ9p2pK7txHcWXmW1DHUFfTSFmJfGY5WG3gnPHXNaaXfp36cOnk71BfYiyQW3DZ46dsJlRgdj5f7IS3U7h3Rxz4-ht7r7bIBbDbxHCjyXwLqhI5hoJirL7uimXHErYcyKxm-gQ1p4uedyeUdfVYYmyd2J6cE5HDV621IjajPaTYuppZLS4ISmRGw_LLT85pol5gQDXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84760" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga5v2YzNvtyuarrCgQeTAujZGC8p5KH-3P3Pd1YmF5FZ5jfwgXpfunU2PF4dGQ2Dj0fkPDRuIrWye33o9voMImy51mbZrgX5QOs3ZR4tHyd4u6IlUTXiuNXXB0G8xzd72LWmkuWRWo3Fyd3qZ8j7ILivdxOfMxQXq8WKO4DqzK6OLXb3_d7amwxgDO4gX1Gylkj6wBKN1ghNb8cXz-ZLA26RvJNDgXZiOBOCPxweMrc3estyb-LHp88yyDJB4RXt5l7TuAM_dj5CQfb6gARD_OgShEjKOeN5okA3WpkoC0kL2XVOnLiRar8avpjmgiqWsem2h5Tmd9PMh_JawSKPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داشتم زیر استرس جون میدادم حاجی</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84757" target="_blank">📅 23:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFcYqhrQzHGzjyPL5E4G7L5gszpDW1gpgwg5obs414H8TF34_TIQtLYIydPHz14NQgHQloS5kfsZDH3B3rG6P3kCepnbHtRmhsa83VyvGnLi3BUjytZjuFpoEv2DEVXYqS1KM0BPNRGKh7uqWUj1y6tHH1LfE5QJ7rJVpVEYul9R8Aqc0KVn986Y7rArTIZts6DJFo9hHocRsHB09Y0d_M2j9_2dKcLw41jY0IroIw7siWB0FSirAdSFAeVfNoO7hFnDtYOktqwm-9BGbmW7Iu_vhhzE4pbtJsyfzK4sYwLys8jTgTrziYOv6WmRVOxiISU8ovRG0shsuj16SPwFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید فدایی و شاپور و رفیقشون ارین بختیاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84756" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حبیب کیرتو بخورم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84755" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjHLwldZLoZXOIn3k7MNcZxXXaRCpurE4Z1Oblle-HD4Tiw034N4VE6NeaZ7lyoYqfUHAMGP1qQWRiQv-Gc-g1qz-UnUmnsMQgK_gZT1ivldH2pGei-10UQOANwEY2kINeeZBMj3ZhTRiijRhW6WjEl5gpNYsMyH8t8QzuIs5af_zuSSumyUcsJ70oTv9bkZRyj5eQ4mbHOueZ30REOC4xe3psSygfmrjrjh5I8C8Jg3sY2KcbME8aWQ4fNHrVUCc4xQ7WbcCHZzN25a5OPcB9o2jAy0FO-Fbrdammqo3pNFj356CywNZgnPdG8aVkTSyDyjm3jQRhagHDuvEAqBbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه رو
😂
😂</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84754" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هنوزم نمیتونم درک کنم چرا هلدینگ دو میلیون دلار داد این سعید دالگخیزان رو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84751" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz3wQ_1J6KT_1g19Cmj5zITNENZg5ZsfHgfqiwJwu56rcbbzG20hSG4GkhdnpjSwJg1JY23a2Xezee7E9G3s8XI76Du2J2Rgz6DrCWjAPmq3GxPd3AzVlsRtdE6SeZJ3xANbW7zYWXuYt--cT-djK_SJxB4QUiBIm2kwQxRNN6Xm-eDiRTMiKmiJo7FtpLwQn6M0Euqoj4FBioeh0emN3Eg4iOLd65LJVRSx4EOkhU3uaavEBnpezWMW1VvwjhuV4yGvVBGG3u0adYAcD1DkS2I3smZKuaos3bkuMdIasf5ENKTXIiGC--XzHyM2ouuLwDXIgHDQjHX-G0qFBZq4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84750" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84749" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940390f975.mp4?token=BH80c1SR2mrPDuAsNH3DLBEJJCZusp95__CHB3qjcznEQ8OmXfDsvnEp9_PF8hADXC760_7mCeoyTd_FXStGqMvxZ3KqzSQ-EEUdfl9ZRkTGNyOpWs_xYZmL8yHR2o6cufu3i2-TvIFDJ3y9SEClE_821Q7s0p7l-_J0iyelv2yHNFrZiIPnR459YHwFdmqX_yPBu5upvbxZXpykqWWowT8r12-vQzT3yfBLgpg9JJV3R4zw3AwcdDSoBvWrxS_iuemXxVb86g1as3C3ZB2mGWUFk4fenIuFX4AoqO6BheNT7l0L7lW9UIyaUzFUTeb4zpYKfI_Nn3mEmGFL7LaGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940390f975.mp4?token=BH80c1SR2mrPDuAsNH3DLBEJJCZusp95__CHB3qjcznEQ8OmXfDsvnEp9_PF8hADXC760_7mCeoyTd_FXStGqMvxZ3KqzSQ-EEUdfl9ZRkTGNyOpWs_xYZmL8yHR2o6cufu3i2-TvIFDJ3y9SEClE_821Q7s0p7l-_J0iyelv2yHNFrZiIPnR459YHwFdmqX_yPBu5upvbxZXpykqWWowT8r12-vQzT3yfBLgpg9JJV3R4zw3AwcdDSoBvWrxS_iuemXxVb86g1as3C3ZB2mGWUFk4fenIuFX4AoqO6BheNT7l0L7lW9UIyaUzFUTeb4zpYKfI_Nn3mEmGFL7LaGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84746" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=qiGl9UQgwqRTne91SmxENyoUzsPti2AKjGNMI_PMqe5woQPr4duoWR-Md35cX9jLog1YnL0M1z1cmsnFAVbc6ZSXG3a5qDLtYBrc0_gs_l8zWDXmox_2HbZ17tgcvNoVTOhBJgrRY7zNZpxuNltPNnNi2-MaRp9K2JC0tcN_3c9ojvcTSYJFLwDxIknFLZsZVSt6KnYs5jevDITlq4OZBuoW7AeUwaxvCya-M4sy-Zb4Bm2olamwaUMBbShWSbiuSJ_BJ1FSqVUmChcth0fjhCWvAeK0BVttEsL7816ojz5RxbuwjaDuVSgWgC-HrHvzCAGWE9-jqNwwu95X8w5xWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=qiGl9UQgwqRTne91SmxENyoUzsPti2AKjGNMI_PMqe5woQPr4duoWR-Md35cX9jLog1YnL0M1z1cmsnFAVbc6ZSXG3a5qDLtYBrc0_gs_l8zWDXmox_2HbZ17tgcvNoVTOhBJgrRY7zNZpxuNltPNnNi2-MaRp9K2JC0tcN_3c9ojvcTSYJFLwDxIknFLZsZVSt6KnYs5jevDITlq4OZBuoW7AeUwaxvCya-M4sy-Zb4Bm2olamwaUMBbShWSbiuSJ_BJ1FSqVUmChcth0fjhCWvAeK0BVttEsL7816ojz5RxbuwjaDuVSgWgC-HrHvzCAGWE9-jqNwwu95X8w5xWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر بخاطر آژیر خط امنیتی (احتمال حمله حوثی ها به ریاض) به تعویق افتاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84745" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بازی پرسپولیس الهلال بخاطر حملات موشکی حوثی های یمن به عربستان لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84744" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ناموسا آسانی حقش لیگ ایران نیست</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84743" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">استقلال یه بازیکن داره اسمش احمدی عه، یه بازی قبل دربی رفت سال پیش مصدوم شد، ساپینتو میگفت به دربی میرسه، یسال گذشته هنوز مصدومه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84740" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آسانی نیست استقلال در سطح تیم سالن بچه محلای ما بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84737" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بازی استقلال تو آسیا شروع شد...
گزارش لایو با چاقال اسپورت
🤣
🤣
👇
@Chaghalsport</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84735" target="_blank">📅 21:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooolgGaCpMVPC6ir1lzIYtxnHG5Csx8U-Ynd68RjaH2jjdLTV1d91E4lBFyCwoT3wDWwfJgQ9AJLi4QlvD2CzMtQA_-Mj05I_i_v6dDb2bVJKaLtBUfbYtLQ7tkAxMgezFrvMXSODAw4Br0-9wmbhqubB4HH6VuTaUq058AenN3VItnhBmJakcgyM6Zq3ylYsoz-ODrFk_4AQqehe2Y9k7Itg_uRq6ItknSIksn1Fp2U-9X-afcsb7SRC2h2J_gO2et3y_S8xTo1maECx9d1wJ-p4Q2oL8NoxQBNZ0ixwiqQlURJ0AfTyW42JxnSnAnEPPWoTsozWMONtDLTrqKTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پرسپولیس برای بازی امشبش جلو النصر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84734" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=pCsgZddXF6ZK24tLfXUZXqD6gbxcnmaSJcwwsxTb472R7xblBVWpP0wT-r0N8S26LL6IfAwr6mX0jrIYPUIC58_zbYGphVlrmcve_otmU70yI8z02k26OJj1y8fzXlFX8d2g094ig7YR18e0q23UKgNwraOVV1XaJ_7BSnZwjaKKlg9KrRe4kbpl4Y7GOlIfH_wLW9IuB7NtTj7H8LLBgdMZOZtoQWCIijlDDY9XNvdkr6ESEdIAn0Tutsnt7EcOrNSaS9YKrWUHvnNWEaqFChSHcfdR96QgRkNcyrVdFY5MRMiiFNGXaJIHEpCBnoV6x-FjPumMUcV1P5bc517wIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=pCsgZddXF6ZK24tLfXUZXqD6gbxcnmaSJcwwsxTb472R7xblBVWpP0wT-r0N8S26LL6IfAwr6mX0jrIYPUIC58_zbYGphVlrmcve_otmU70yI8z02k26OJj1y8fzXlFX8d2g094ig7YR18e0q23UKgNwraOVV1XaJ_7BSnZwjaKKlg9KrRe4kbpl4Y7GOlIfH_wLW9IuB7NtTj7H8LLBgdMZOZtoQWCIijlDDY9XNvdkr6ESEdIAn0Tutsnt7EcOrNSaS9YKrWUHvnNWEaqFChSHcfdR96QgRkNcyrVdFY5MRMiiFNGXaJIHEpCBnoV6x-FjPumMUcV1P5bc517wIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا چیکارش دارید خودش دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84733" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8hGFxw9zpmD1VQpy6ftP-MvN7hyVJRXQVP5DxqSS3CoZFib2Gwxg_4_ie8oJEcxA5FVmuDaHaVQG8YUJy-hKgNSQqqDmLP_D1LDvsoFyZBWDpi3YBNpvUgkhSOs7eCSbygLeHVnDycDMjKrGGLbYjwSNw6KwaZ2txL6O8O38jAwQVSXAQncp8jT476_oG2VA_ZEJzU5Ig0qaa57FH5QCqkWR1bhzbcOjdG0Hv7-VIMhI3gM64C3iH9Btl5Z9C4ogedHQDm32A9sE9JM2Dep50-iiiB19bR-jWiNu6X8ETJDFOIwOzLbUaaK9VbaqgMoSkkpq2mpbwABhYDxBMsFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=aEhfcFXBUwIPagRUJHpIABQcILTPLJcLX3k4GGB3svuw6ncqoOR71DiRhWhLvL687oZbxaBkXUl7RFftBsvIWc913_PoAjK3FFKNAECNsng65NYKzDIJVcqTVIuyaobJ8OI3BKNcsd1Z4pDBjlw7ZMtMLA1iAfj38mvkwZ2S_F-UpdGiEGjn5aH_HlZVCrlvgFW8-fqeIahG5SUwVgQCQy_t4zJ7LJyax-Ih3gNjPuLKWaJBx0o0sQ0JGx09gTQbe3U2k2eZJ50_tQw9QwjIXzX3PqFsn2LMLG518c3Zwt0u8z8bjXpSg9iGeZU4C7JMxbQG5-yayJMwtraV-mccAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=aEhfcFXBUwIPagRUJHpIABQcILTPLJcLX3k4GGB3svuw6ncqoOR71DiRhWhLvL687oZbxaBkXUl7RFftBsvIWc913_PoAjK3FFKNAECNsng65NYKzDIJVcqTVIuyaobJ8OI3BKNcsd1Z4pDBjlw7ZMtMLA1iAfj38mvkwZ2S_F-UpdGiEGjn5aH_HlZVCrlvgFW8-fqeIahG5SUwVgQCQy_t4zJ7LJyax-Ih3gNjPuLKWaJBx0o0sQ0JGx09gTQbe3U2k2eZJ50_tQw9QwjIXzX3PqFsn2LMLG518c3Zwt0u8z8bjXpSg9iGeZU4C7JMxbQG5-yayJMwtraV-mccAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF4I5fMK8uI3-xFnvFxInbRYG8B1DmSNYCS4GsFXc6Dccg6aODLZpC2RW_iUrlgH627rD97CBP8uds_JeRbmtKaWvwsHlpTDat1OhxNklUCjIXYeH3u3SF5JioSbn8IhRvBPRmIZZ0pFH7C-4miUu-TkctTBha2gZ23s0n0lcPgnyV7e7B71SIJlIlwFoFwHUTkaFI6heDG3zXrX76Qb3lgBGuDhlbMhrhN38ZB5EMS6Nbb2y7RZVieMlC96YrzM79oDnx3wtGvKZ7VV8j-Ju6C-eptQrjbOZ1Rc2bh1l4OCZn8BcC5uYhqePVpVGiLwt6EdfQLfuGi101qemF-zJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نخست‌وزیر بریتانیا: حمله به پایگاه RAF فیرفورد تقریبا به‌طور قطع به دستور سپاه پاسداران انجام شده است.
اندی برنهام اعلام کرد:
«می‌توانم تایید کنم که ارزیابی ما نشان می‌دهد این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریبا به‌طور قطع به دستور سپاه پاسداران انقلاب اسلامی انجام شده است.
ما چنین تهدیدهایی در خاک خود را تحمل نخواهیم کرد. با استفاده جمهوری اسلامی از شبکه‌های مجرمانه مقابله خواهیم کرد و از تمام اختیارات خود برای هدف قرار دادن این شبکه‌ها و منابع مالی آنها استفاده می‌کنیم.
تحریم‌های بیشتری اعمال خواهیم کرد تا توانایی جمهوری اسلامی و سپاه پاسداران برای آسیب رساندن به ما را محدود کنیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84727" target="_blank">📅 18:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شین: پرتاب دو موشک بالستیک از یزد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84726" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jasm4MYJdCHBQsBArMuIj7tuMZZyTdhuH1pkowlbGJbzVPDFfG9aaafKrcV9x5bae8Czmb0OxxNDLQfLnkm6vEcEM26zzD0h3BjAjqfZrT_iPsoc8cjv4Mkei6cnXsIxVNykYcEtfL5f810qiwPz_zWvpBdB80_5p1vcI3pHRmeJjbkzrQ5t-9r0qteqDg7nHKpQgN4gGQTojpRXJLicE5Cg-xpXmwsO5AD0cNAI6YB67aQw3sDEurzza0mtyjTqwLsSCUBuhpRQK_yXMsTfEYBp7kuxU4oRZuxRzkuM-KNpn7GPZKNfI5vAC-h2EsUBZL9Bi44IqucCsZP--g4hAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LT5yZnW5jXXpa3PI4OkXoqHyIPVPiWQHdSW3Vnx0cH73fdi31MTdvUFnT65Rs5I_4SmXRyiNpDCY3GpijY2uAtMpFN_Pc-GZJtWYfyUoK-quqgvcZtB1VGYrblM29CGw4kI5Td-GutzsS3jcnyJQ7CR-J7JJIQV3CixZBHF0pIWoTSsJIa__0qwmxgSwwWUN-TKcng027bBnhimufYbfxlE--y-PzcqS32lFZDEacfKCs6C-5yFw108f0nwty4OrQhwqi-xv78t5IHKMGznoQfWqTvCSvbjFEIGFCkqWFpNh1D-FgPVk9J6VQIdAJwu9bYjW3MB4K73tP3Hwfh8vtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84724" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=caaz9h4hINLcbsPDn4nyImn2qM12WwRuFgWr9XfEnLB30Fv-sbIVLgDg4JWt0uIG4tRyjaWKOmX1fvRw051zhYuq8k8FAwQ0N7KsP8NcCqslgBaMhOv1qB95cCGQK8kMdJElAgBT6MPaGcbGQt75RPjmCF9AbzTivBvJUSzyiBNWnSsv0dgR925KuTN-YKkzHJuTXuBcPjb7WSMdi_2GxmJZM1gaEBYi3gozj_tM-PBLE0xS4QV3E50UXoDwSdxeN9e3pJqqbTE-k1IBCb-XQKZp9UIW6uRUHVV8JuTm4KUDqZi2M0otwrPNgmzHxKxUlI9TWO8pykYhxHwQRW_1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=caaz9h4hINLcbsPDn4nyImn2qM12WwRuFgWr9XfEnLB30Fv-sbIVLgDg4JWt0uIG4tRyjaWKOmX1fvRw051zhYuq8k8FAwQ0N7KsP8NcCqslgBaMhOv1qB95cCGQK8kMdJElAgBT6MPaGcbGQt75RPjmCF9AbzTivBvJUSzyiBNWnSsv0dgR925KuTN-YKkzHJuTXuBcPjb7WSMdi_2GxmJZM1gaEBYi3gozj_tM-PBLE0xS4QV3E50UXoDwSdxeN9e3pJqqbTE-k1IBCb-XQKZp9UIW6uRUHVV8JuTm4KUDqZi2M0otwrPNgmzHxKxUlI9TWO8pykYhxHwQRW_1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ی نفر تو ارومیه اومده واسه ی مسیر نزدیک اسنپ بگیره بعد اسنپ رفته بخاطر ۱۰۰ هزارتومن یه راننده از ساری فرستاده، راننده و مسافر هر دو پشماشون ریخته:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84723" target="_blank">📅 16:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mycI2s-cQnC_wRVKjlrIp6pnbT2sVcRIsQG6fCSljzU_zMZCD_MaW7CmmjvszLfurZneI5LovbhOtaPhQ8Cnme7emIe7A-3idlsWor7dyuS3kzIe2lPMkRzTEgoxJ7Rd52_LOQT2wylxmj8luoJbHXUXEqZeljJD2b4bY0IayF-TBm3C73jl4ZFY004JgNZIdpPlezNT2CYgW-SW3QKsk9h2aiD6dadFcdPbqJXB1nLYfDtyoE8FjMVB9_SlOnRWefUo3ID9PkfsvB1Jym-gzJSUj2bBASQk5ddi3YsMMaJo24qAu80NmIuyHEeAH_EuJzJfXqhP-Lxw5b5MIvlc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84722" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=LRF_PI544T1CKDTPZtDHqUm4E85npEssKPsX-8vPFzepLMIL4EJMQcFoKO-IIwNYRXe4SlLdv5ePSKGoIv5VwM8Ljb6usrPLG8YNOPLejKH8XL2Q7OPnyai-XhTSP6HzCsHIvk2lZjChT5ao1Nf-lXpD1hh_StQBNhjtx7BNXgqNv-D5DBFbAkSGNkskp5eVBzq1qD9Ez1nqj_hrmT8xYd1EyPSGjMGStAUAkcKPWjdNlxdxanf1SuCgE1W6H3QHLpak4Zkrg3nBg8VFj9IVczGcpGBHc8EoPJ7w1RSi8yT47GB22WjkyfNf8VfBAednbPZl651QgWo0_exfbEdzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=LRF_PI544T1CKDTPZtDHqUm4E85npEssKPsX-8vPFzepLMIL4EJMQcFoKO-IIwNYRXe4SlLdv5ePSKGoIv5VwM8Ljb6usrPLG8YNOPLejKH8XL2Q7OPnyai-XhTSP6HzCsHIvk2lZjChT5ao1Nf-lXpD1hh_StQBNhjtx7BNXgqNv-D5DBFbAkSGNkskp5eVBzq1qD9Ez1nqj_hrmT8xYd1EyPSGjMGStAUAkcKPWjdNlxdxanf1SuCgE1W6H3QHLpak4Zkrg3nBg8VFj9IVczGcpGBHc8EoPJ7w1RSi8yT47GB22WjkyfNf8VfBAednbPZl651QgWo0_exfbEdzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین حرفه ای کماندو ها و نوپو تو سنندج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84721" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84720" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پزشکیان : داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟ باید برای حل این موضوعات چاره‌ اندیشی کنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84719" target="_blank">📅 11:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQI47pNvT1c9HhpSjvdmv48lIn0ezn7kji4MuEdaGYnFNUAbvnQgsnqOpsiprytdWSsEsWYJXtegKs2z8twUEgzbJDBDCodA8NYAM-939spipmrJAoFec5DNS19WnmN6m1dgy7vnK2fqe0v7fDPjb2FCGiSuQFSP3D1-74phtK6hxljqnU8YiJrwigN8sUjo2hIosHVlXd48BN8AZn_fSFnnLAfkUr-VVDXVWnf8e9ZmoXR1EQoJ0xCqwBcwtqCop5-UVpZ8uECO-7wt_1U8YaKKJyVuUGu290k4Ha_gwH0ldvthVgPFphS-F-tTdyXQuOGJsqzpjEx5iCrXwQwW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=E_NTLULE7i2A9ptbczUk8JNHmAJ_5prkiCvQgjK6OHspmMMU7yMO8pKqc9epi9PcyokkbXFdVD-rM6T6zUcVMqvrACBX35t-ZceqQ_CCR8xvdcFeXMlqdjAL5Ae4pet1i6ME4r8jmyd9NPKvCht6TsEVslTIevs6oiQK8ullWM6UG74i2nSrvpRQWwX7JMk1Nwi-IfMNpUg-JQoQXtacJNbGxi62s6Z_SitDJPvZp_1xsCYjuR3l7Cw_AnvIe_RLE7SxQl3uNi0mhTQ-IsYsAGkkjtqq_QQheDbvenQZJYkhz0B3FjKREZ1nZSKTUGIp0m2H0I6NkRzAwMhktyeE9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=E_NTLULE7i2A9ptbczUk8JNHmAJ_5prkiCvQgjK6OHspmMMU7yMO8pKqc9epi9PcyokkbXFdVD-rM6T6zUcVMqvrACBX35t-ZceqQ_CCR8xvdcFeXMlqdjAL5Ae4pet1i6ME4r8jmyd9NPKvCht6TsEVslTIevs6oiQK8ullWM6UG74i2nSrvpRQWwX7JMk1Nwi-IfMNpUg-JQoQXtacJNbGxi62s6Z_SitDJPvZp_1xsCYjuR3l7Cw_AnvIe_RLE7SxQl3uNi0mhTQ-IsYsAGkkjtqq_QQheDbvenQZJYkhz0B3FjKREZ1nZSKTUGIp0m2H0I6NkRzAwMhktyeE9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnFMIYfyP4qsOR7HEfGDMnr3YEE9ZqTyugmDQXj0pbdDjajQ8_xl5vWBLfo4Dk2SDsXG4sVapH3OskkDEQuj2qT0KR_C2SsilRoADSJa1BBeNh64lj8USxPiXGXxBFlhQVJPUW7-ox0HDKY-c5_Ky-5XkOqIeN-KxZ2d1g7d8Prv8dhZsJ0h_rKLjBb5N4mnnbAg_8TulKtXUlL1YyJ2iuica-sOsIkSzshIpf4ytOrxMlykuTyb4AwObsCkDOHP3iR0GarUMCrE_s01KL2YY5L7FIHWOmxHf8saihvVpKR-u6tRGHqIDqqMgtgU0zg31vxv6Ld1KsKBw4tx4l-Q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=jBuAK8R0aYOU_3iesj43egJ6sEmtQMurG2qk-BoijoAWs5h6paqmP87yHiDHNgaTJ8sELzXKSPnpMIgKFqt5kM65xYIPYKu61KmN1dCjR8kXH5K14FchBJifip-dHig1oNVzrYgzFI9LYJWer5y7wJoN2I688UPFm4MzuVl4zPUuy8znA3e8adSs1T4aTx3qPFsvVrBqyn4OmdPZ0-YRgyr6YJuQh4paGI0Jck2ZGnLhfzKDnH92LD3mGjbZyuHzhWxiPJsUNuiO8Wnh8ARoNbpiwOyUzfyp-ZbelwF2TyrjwuJka9M_WAFDkZgaRhbjkka5New2DSBAsyY_KtsY0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=jBuAK8R0aYOU_3iesj43egJ6sEmtQMurG2qk-BoijoAWs5h6paqmP87yHiDHNgaTJ8sELzXKSPnpMIgKFqt5kM65xYIPYKu61KmN1dCjR8kXH5K14FchBJifip-dHig1oNVzrYgzFI9LYJWer5y7wJoN2I688UPFm4MzuVl4zPUuy8znA3e8adSs1T4aTx3qPFsvVrBqyn4OmdPZ0-YRgyr6YJuQh4paGI0Jck2ZGnLhfzKDnH92LD3mGjbZyuHzhWxiPJsUNuiO8Wnh8ARoNbpiwOyUzfyp-ZbelwF2TyrjwuJka9M_WAFDkZgaRhbjkka5New2DSBAsyY_KtsY0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORDLu4M9IQ0mOJYXFgD2QaBvXRfreOSVncJTQCNPAiDecDCCum3Nfvh6WvsUKdvrHQfslOpqrC_aGEly-3ebiauptMiE9-fpcKyvlWz7LUF2y2QDz2fCGazQVnV2PVegfBEgtA9wUgvQjDfjyodEIZUo022YPR1HqBr3KyN1UZllPC7wf0wg8rII3aTDpKAN346FSZrDo8d5e4DOQq_ttx7FVY_rZIJVPY8TUXlrVr5VtyG56M7dXJqGAGKt78bDS2Tc3QIGhzWKgfBi99jmJnHRGdWNhVOUdUCqVlRitfl_MLgvcbn8oVRNRo0Vkc0g0evDNGEiCq3nuCQ8RlXghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JePlCChHIh3Wl0Lm7-iwy9tJDJTziB90Yr0E1px0gce7tSLTkyXhZnDQCPe-OGGiuhRudsOMfUqGKx0CNh7p4dY93lNQwajgenN5jIWat8OX7_9lndJjXHMTVkvsIHI9MmaWebOCJ9lyruO43akXRkTBhTowK1Z4NL6IyuPI_prijLVVctA2JQoYh0N9BT0StasdW6C8ZCJuKFyuds0uajsEfRXlHJT4SElwmXm-9jYxQXj_qyg9vrBjARn-jaa8gOtuh-Sd1IvcMBx236lfAbRL23aaUtWA_5MZ5zciXsNs8uOpwtdZRRoUYfTlWUyXL4THMeD3qbJo8iEXLaglaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCOg9s8T-amkfKHo7eHzCv7xjtXDUucmnTsGAl3HqAU0_dsdFHockbXlu-4zsbc89np3vbewAnqnS47FqSS3z0Np5G7CmbGT6D11k4lf5pMxk-SEP-ryIE89KU4shJpU2MyUScpWNqg1KIEu-hbn_0NBbq7yr8es5tGO8EtiIycQUznyGLuKzZGaQJdXHJ7vFrZohjfF4xcy4bOls99SCBjZDBizXcbEmGiYqLltDClyknwmaAzHo8104huANd7bB6qiFpML68NaddE2dyaPM7_CCkdEeza9cF_SpHpzSk9HaGBa0kutopkrnKqkmndGDXltjyb3kx2mHHrqi-0BpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9pkV9PCy9KxYWEpha-OntxZDe1L48aEgz7dC828wya1ro1NcARH01sb12jFctJX8nvXrNZ2w1CdH8xvYwILmq15i4OmZGb9slKxGgtD6LVMTkKKVup65yfhdoloYknT6sldi4tca8jTe9sSuGwRarHu6Ag1iy81-_WL6CUCkGT_2ecLRco6aF8nz8UGocO-3RhtHTsbomHaRU8lDT25kC7FpvDzGU1Ads9kPHuSeuto2Z2QGi4FxaY8WOB6GrvPhIMa7hOtx1nmMnDIKmzKOYn0EHrBUKNDzzBQH_44jCj-QkP3VwoEVtDdRveqjjUquXz5fXzKzaVO7NpGDFsfIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOXy8IkSJig10TxqP7kkeppHSR_BYVzhpVIPvjEvxIGS5-T1sbGSu1Z5O9KY-TBc5qODy426RsLmeD7emei9LMUFJAieTCbSyuD1uktbmVhh3oToyPBBINPu0IBFSp8QSY2jqpxEcP4gx9AO5FvzqxMP2wFxglOugG_LAMcpD7x69-OaOpqC645pomfqMgdjFJogMLUcK3nkYufwZIy_inexKsLHv-2nlQrRYO61G-CKmnx7XErq6fJWJbG1wyBg0jao9PVD1yPs_VCRlUtB-kQThxO6chjALStXbc63djeNObBvSqogxY9lgojU5_SxMPPow6kpVNjMLq-Znib5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=SWQ82EA8eNR1egGK6lHMTXeQwZx1u7v6srjmybvIbvqtan78ALUDZwr4zLpQU0szjIgqRBWonZl40fA1G98U2camjaf9C2qltILsAzncWPDW_qaI1YSK5W6vWmyMO0lJ_R4VeXIgvwOrbFYpIAZIG8Tg7RjmcYgvDBst0DeREv2F19zqaYH_6I9FgCIIaxSXaexY5YmYpVjQUGdvHH_fptVxzDQbl3l_Z00aeHvzxU-5lxSmKG_HAyrY7339JY3QiCE0mJLggVa4-ax5NWfMUIagb3L9IF6uEZkbwKtQERMFBpMAYTX_DRCNO9lWFD8AtdkTGBsNKwq4UFKmkEWV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=SWQ82EA8eNR1egGK6lHMTXeQwZx1u7v6srjmybvIbvqtan78ALUDZwr4zLpQU0szjIgqRBWonZl40fA1G98U2camjaf9C2qltILsAzncWPDW_qaI1YSK5W6vWmyMO0lJ_R4VeXIgvwOrbFYpIAZIG8Tg7RjmcYgvDBst0DeREv2F19zqaYH_6I9FgCIIaxSXaexY5YmYpVjQUGdvHH_fptVxzDQbl3l_Z00aeHvzxU-5lxSmKG_HAyrY7339JY3QiCE0mJLggVa4-ax5NWfMUIagb3L9IF6uEZkbwKtQERMFBpMAYTX_DRCNO9lWFD8AtdkTGBsNKwq4UFKmkEWV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMDgcNN3KaJMxalOdJ2dMYg9YqLLIvf_zmtwwmynkKX_UyK2JkgahkfZlu9Uhky1EdWTdkAmwMNKZyGUuLE8dQ_Fzh_-84YXL2XgsbGsHMGKlkye4XeoVTb2oROOuCiWyTGrkAYukH91FrPUuo32UbRYLQ36VXIndCFAhye234VLtYXsUUGio-kOqBPkwlSI5Frp5JM0ezu8v60OsUIVj_SfXQRSLEr8u-1aqovXY7eUjZo9za9qITQss9vGFe4-XA635aHGnzU8t3vF44fqQr0YwWxQ9Q1bxNHQ5Qh7QIGNiHLVu7p0gbhp9eceNfXUadnq5TmOwBIoTBJeDwABFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEgYjTbRwNd9Ioxswyv75A582k_wXsjlrPxZfCwe2gD7dKN036P4kOhd2pVihtYb3yKu6tGUtqXZe1DEmYy5Uku3zUhCVuAPLZ8wSAZDKtcbriwO94NuBtjWRCgqp6yVQtcxrvCrV1e0EvnzQmC5-IUIsF2NYwS3O3TR3ICNSAimuYZa2Yxhle2F5VCQnrioY8NOBFVTO1U0CpLdDAdSMXWImS8dztvFis-M02aT0PPWEXBTjM3hDEUrTOf13i617QN-P0uFtwSzS2n64aDoOUZsGnItM9LaqziLXLuSG7SHsZ235EnzlIcUd6Q3JE1GiUgaLEVh-HGzP15fBcZGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=pQHbPWwlw_BfJti3pILzxBsi-hCd0GVZR9KSnS2Cu3RgMTPoJS71pHcHUYTFbo6WuG39yTcWY8peZSnyHBUeSRExCgkSj0NdaaOBetSfReGK0suZbvqbE3A10cpR6CASPJeMLpgXbBZeynfRzNV2FzzXrGysum0YUkpMMt69OUu0ij3y7wEZmrSRMRJYo0EUl_oJ1-Dnq96rpCkMrCcYKg0OwOrbTxO9_x7yu2psSYjGXFDFHRYzI1MwBfHWggVARgpuIK-L9YZaHnXfLykqZHDCrl0_vtHKYyK7OpAIJBq-ez8lZJejmLNAxO5HHUhrzG9jr_vaBKO5h_sr5Xz70w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=pQHbPWwlw_BfJti3pILzxBsi-hCd0GVZR9KSnS2Cu3RgMTPoJS71pHcHUYTFbo6WuG39yTcWY8peZSnyHBUeSRExCgkSj0NdaaOBetSfReGK0suZbvqbE3A10cpR6CASPJeMLpgXbBZeynfRzNV2FzzXrGysum0YUkpMMt69OUu0ij3y7wEZmrSRMRJYo0EUl_oJ1-Dnq96rpCkMrCcYKg0OwOrbTxO9_x7yu2psSYjGXFDFHRYzI1MwBfHWggVARgpuIK-L9YZaHnXfLykqZHDCrl0_vtHKYyK7OpAIJBq-ez8lZJejmLNAxO5HHUhrzG9jr_vaBKO5h_sr5Xz70w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcs7LfRlVQQ3TNZSpCsG07uyyiGACQTOR7GORjT9QKrOf17JZTqS52wanOSgqu7_gB2Ndjj7W3WhJFKVmrKU93xGA02E9lc483Qriw8LRafl6D_lcCGd7Kj4eMsXaoA5h1n2ugMbkooh9c3lvw1k3LQInMlx_bdP-Ot1fYlArCgbPH_JPMKQSBo0_H3sUvEiGHWwgql33nkqm6R7kabYH0gIypCc6jkC8U7P-Nb8Wxn2I6VJjco0xRGydHSF1sEczB6qgvwC0Xj5jZqDIN8y30-fUQswZd-ozkNDU-eJM3OaaT2ohdniTW-1QJkCwrD_tw8XdFq1jJocEiTaf82AvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZVABghdEWoKhQxGS08gFuY9g2HDJ6igvsyvJoHYNlGmaMXHa08QZ18OP_FzNi_BTG1WycPHwqVwpCg1zeaIoVaXbnLgwUfowjbtBQTbBD6wGE_QUrYQYqwGh2rXc0E0Qq29fhsXc044Y0-zkr4rzsAwN4nLo9mP_yc_h4WQks-o5Ot-HCR14IgE-LSkhzLlBkoMSzJGNQqU9rwRmCkm0ctyp98IpfvnnGyuJVJcMZeaC3sn9yLLBAt7_b-HGC6BsqcwNAhGD2iFXzafFgNi3g5VRNtFGZxXY8XZcee0Rcu5zv46EpuMLsBuZeulwSc6R0wpwWwWwYL5cD_tXLpDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJT1dODQ5dTWV9w0ryd3BWveJKpgK7-2EtqaGVb7cJgFhKEeKYigiNWmFaiU1M-TEw7b6-d0WhDQoOojYMxklawg7Ws9tc2R_V277sKJBB07zTv0Eem3h9f2z95-cCvQd2MEjmVIHpzxhSz8QYpckeE6QxTuWP6cQBljXEks8JfsjlaKFs9QYxF0O7l1oCA2FONQEvKriYZlpic1qL8l4jflZI9dhiXqm-JcKJQv3-gRqTQoymqExGBGThWxVyj3qKPYIrjLJtYMl7AaM0qmEzSvwEwgvUMlIHzdhN2wh7Ce03uDIBCpNPcamHE5dKIUZd-avGEeprnDe-CSRkpXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=IH5qzjVdh2vIm9H9NVbBcw_eSKuBYnotc5FTHSRiZCSB4J_L_pmaj67oN4cokEvJmNL_Y7Q_hv2DmgFkHobhtGJDHl_p8ohZc_DN310JDARl-Gjx0j9hdspctjvarfhPweOP5TnCzmb0qGOB2jtFvw-saFoZeFBhFeGwZrDpqIZnFQHpJth_zkpvJipH3aLpN-o8Or-w9LVRiDfBUPNRi38Ad4KoTD0RG7c6sUNnwzU56aoYoqKeo3-Z9NdSLeR-yJ3Pp5Vf4qZq7pkffzfhB-ewNXJKVq8cajLKw8mEUESgdEdzpjsQRqDnF_o9NOB2aw6UNFqeePUndc1gls1q6E4-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=IH5qzjVdh2vIm9H9NVbBcw_eSKuBYnotc5FTHSRiZCSB4J_L_pmaj67oN4cokEvJmNL_Y7Q_hv2DmgFkHobhtGJDHl_p8ohZc_DN310JDARl-Gjx0j9hdspctjvarfhPweOP5TnCzmb0qGOB2jtFvw-saFoZeFBhFeGwZrDpqIZnFQHpJth_zkpvJipH3aLpN-o8Or-w9LVRiDfBUPNRi38Ad4KoTD0RG7c6sUNnwzU56aoYoqKeo3-Z9NdSLeR-yJ3Pp5Vf4qZq7pkffzfhB-ewNXJKVq8cajLKw8mEUESgdEdzpjsQRqDnF_o9NOB2aw6UNFqeePUndc1gls1q6E4-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdZ4X5Old6pr5Tcq4QYfYuhMVsWxpv5n8Yf224bIvqBOOuMUQofNpddsleo1m4AycGUmjB4fExODrDJFglmZw7LB7KZXOzWCvbl7uvoAfat5jQRGks2N70nWV6l3x0aMppaUxDY6ERQzbC_mRUdpjODhVM9iUtkfjDeYz767BdFcxjaLSc3ky5Y3Zc5652N3_Zk4_jmsimepMlh1o8MsOcV_kDxm1XoRdvF7D-z5iQM75zKYuY_fuP5jXF5GNzxyNXERPPM_CIzMZ72GnQcLopfmI-y-XOBYksVY_4wFwN8TGI93Goum8JJDr1obOHqPfeMJcs9gVumFSIMZVZl_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kq635_j4xQboaM7yDnwr7tq3e9YJvphVUalIg_OvMBOFEHoEvmk0EKSe45ilX_2vSGc3mo9WUlTjokFNejDijILiVCOXC8W0WW8c_CJdvz0DTl3EmNgJZRJJB4GM9cv2lNQnGfybWvt5Lnl19E5MTEn6i0-BIy0ZvaktiDkFxjVFLJ5MzYdZcm4m4u8aST81YYo9dczqaA4oEnEz8fJtS8TwQXe9KguH6VmZNdFZqlw25dSSMivSMO-_F8ctkDx8rXAlRUzTMIlXSjvl0XVUMvYmNflz_tPEnnPPRF-LHqr4xtIONohbdwxTaWt0ERiEBAhFhOl86KqtfCeJBAhs3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKPVdXr864iP8XhJ8nrTmB2bBTaBiJJ-GkoHiMcjS3Kn2L-Gg0FSA5JbPRJwFzSayRVodnJjPxkL6rtJ78XffsPwW2bM82KQpSR_pS4ceVsJG5GoUe0Wj0B1zZlGjToGN-qnD6YiPHU0Y47FYl1nDVKCTxP-2QC4qrISRHR7zHYpa8qMRljIns2INp3ANB1JKHJl326eMhziPJEZCHBBsCXwzG_iQf8deEmMU1XuwsOCStj6eg4G3FnH12HnEhQq7CExDcctjMdcd_Lgjm-TibkceVyI49hXB2FfPJeI40SyxoOjjKanj-0MxozCzBbQkC32Le0igCScxXb-yYQzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIZFqklQ58NaEyc022SpLqlvJM7uGKQzVxqsh5r3b5Jr7kUKEU3p7boEHDMUQD2LkWGyG5RJLni53YUWK0M72fr7Ql89_ILROo6B2AIFAtrpnTn7EMPmoZwvxcqB3Mb2plqdwFe3t3TlDuvZWRqWlPCacncdIZspNrrmZSqWz4nmKwI-ceHm09rNgJySHUl7FWyjmXR5XEYN9wpLfVIx603feF_1euxysKVnpnNlWYCTGkeYzz5zstPls4gMoR7LarsR3NMcbPEgqjoWnd2wcAINwyWp_mP8Cb6Rlm6z5klNz0cuzaTkXEOIq_MtLBmacIrVxco8gaWTVONiConruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_sdh-DqDu2yT3FfdPw0xg81ZX2QTBTXynmprkcASRuV-ix3J22jgOVpYsv2R8coXCGtz_yuZquOddyNqQAW7m1utzvkyyMXLcxzfPOkz4FR9wbDLflB12xaHbxGcwwTiIRHxXce9XcTwXOJdHPeS3CVgUqxK4Pz-HBXPsEu0pegjN73k7XIFAriI3957SBotDb3fRcPiaMRE2C5kk6Q5PJ9Q_fJJoz6NVyGmpYhytyYas93VmbDnZMu5Ne4MfLw_825d-N2aWF2Nj4X56i3WCO-ljP3knPAjO7U3bfNw-9rGxsn6K7theEI38dZdKQ2OQOlIGb6WevVFECK4Od3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdV1nW0Kd79kcTdKYxy1wEVF_4VNEujS2XRQnVEAKdkiQt9pIz1yDXvCm3HcplLgQpYVm0GHHprCKFUBmkCQiL3_3fLV6UexW42IlOOTdBMkQ2u9jeKG5GJIpz4ebGABrMuaVcQvfQqrvd_Mv6ya7jOsAczsWuZOfhvwRDnYvMzPb2ygfpZhOUq5HiFa4ciXVXVzA-jGUeJh-N7Y6ZSg_VO6WxisCqYqVP4cZhFgrdVEnd5hJygV5hndTV3Qi1W05f9BBQbORRHCGwYwrT97UWtpfH-6b6tLB2g1mmHjkKANoGnTZfGFH_psq-oRI9t79xmxhSS8rX8QpVvYYrbzZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=LedM9ZzGa5yqG1B_dFKj9I9MAitl1VlJP-hhhVk5oVcgUbBZgGxWPHRzU3KaIzs6KPssu-dfk7n2ULTsBtV6-ruRpM64_yerlnAFIoApk_V-w8otQx1iuT_oE-bjUu1hK-HNyZxNhWZ3-EWLfsxCGMoeTV9h_3T7zpFGoCvvhi88omVZ5luvRgdmBrBt9A-7uXVcgCpuePz8yLkplANeYDg7PIzfltycP5wShm1A4wrvqOK74_etHLtaTlpwBExvyp4f_inSwuiau9CCY6GxhMyxSCHm-0HP6YN6c__8B87S8HXnEbubIlgUkcDOpcyCo20NOt_nT875ev1yCGptew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=LedM9ZzGa5yqG1B_dFKj9I9MAitl1VlJP-hhhVk5oVcgUbBZgGxWPHRzU3KaIzs6KPssu-dfk7n2ULTsBtV6-ruRpM64_yerlnAFIoApk_V-w8otQx1iuT_oE-bjUu1hK-HNyZxNhWZ3-EWLfsxCGMoeTV9h_3T7zpFGoCvvhi88omVZ5luvRgdmBrBt9A-7uXVcgCpuePz8yLkplANeYDg7PIzfltycP5wShm1A4wrvqOK74_etHLtaTlpwBExvyp4f_inSwuiau9CCY6GxhMyxSCHm-0HP6YN6c__8B87S8HXnEbubIlgUkcDOpcyCo20NOt_nT875ev1yCGptew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEadbF50Kvnlia8kTmeS1xrY7htbzEtkmi473lWfsFxgIAYXVCQCWzmLa5SQbRyiNFJQW4OqIz0hE4njsS6H3arGRNqbx6XwxwgZUC4PXsmLtJ8s3x77RcpFcpLIRZd_QdBWHThlVkcllO71Gvz6Yucs8NI1ewTJTKB9JXhcMRtRLbDZw-6BQkQYSO81RtvXEkgzUUS7mzbOtFFZaF5Xypl2-yQgGkEY_Rz0FP2A3V4Zdfp1Rs53-CJXlcofo7W15x7eQe6ApC_zniFWodjd38F38Kr1o830wmGFLSbaxFodwCepcgc1kNFx4UDOrXMzSmJu_GSW-bbAkqYATEeERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijrPdo7Fbkf3bkyLpSiBvfuEpOltlygEGerIXeE7FaxihiCvxCbifzypeCtrVLEHgBpAkY3UI84WPy3uOAEOPu5Nwa8aYkckpNEIjtmCPp2Hho6We-OwyyveJCtE5dIcp2BmcZJ_3I0NVkKBRBJZmEHT8w252rmt07c71HzBszEVw1thWPNj9Zgddx2O1GfehO24ivx3h0bH6VET2U3Go28to_WFKgi-MiJJDwcbFHB31dLAzaOXCHt9jZQ_hNBng6NQuyjKc58p1FaKItAlLpA0Y8SiBs3tL1-fbHayBR8KHt2Ew8Oz7f_0rps5mgilCQjG5o-oiI1LbNjr4_-ezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=fgmC7YmYJw7yR8p57JPjTobKRttTtVfFxBEXsoJjoxcqQgTgSW5BHIfzpcGxg93BZG_wE6Tr_0iSwE2cVSWxw_gAQ3lNXsJpHITcKWAwSgdr2hY-vAxK7Yx9hbhxrrrlhD1wMNTnjy5-UFalhVN57-XFv8SwnR0IYJPK8ci58oCSgkbD7EqMPiWWpoguf0wwBZzAgR35Lt2dfT-aUjg7IXDK2HUyjqpAGL9jKWfLnavEhbcQPpdsdcjllKgRLohJLOpYRfSbhHxgf05YXXCq0FyKyXFHPaLCRfq6MTqqg53RH3ROib9NiraNWSHpA-ciJYeZNbtXHfPo811rTeCHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=fgmC7YmYJw7yR8p57JPjTobKRttTtVfFxBEXsoJjoxcqQgTgSW5BHIfzpcGxg93BZG_wE6Tr_0iSwE2cVSWxw_gAQ3lNXsJpHITcKWAwSgdr2hY-vAxK7Yx9hbhxrrrlhD1wMNTnjy5-UFalhVN57-XFv8SwnR0IYJPK8ci58oCSgkbD7EqMPiWWpoguf0wwBZzAgR35Lt2dfT-aUjg7IXDK2HUyjqpAGL9jKWfLnavEhbcQPpdsdcjllKgRLohJLOpYRfSbhHxgf05YXXCq0FyKyXFHPaLCRfq6MTqqg53RH3ROib9NiraNWSHpA-ciJYeZNbtXHfPo811rTeCHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pybc5wpmsA-bbAe1esvw20QMBlpKGhJaLVbE5wZ0GfT0hYdX2xLCO2970kloSvgrcmqyALAtjVxTPblp2mVS7iHzfYNsU94-qlQftjUifb4hoGlV790jn3CrgTdzrty3AGmu3sy8JhhnlT30dWETCWXiZp0iBgisJbkflH745ozm7Vj7fDUX10alZ2HvhHBNq95ilK3GtaFu_0RuN-GtFmszM8Zma1WqBKBDvhKUqSe7in8b6ZIGJj0ak_3k1oM43oOcmHAW-_vJYYwseyo4WVkNM4bUwtpWzvlXM4k4glDC8L6b8QbZoffPTvf90AL3YruKIYN2dbmiWV-KJkOPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=ih_SKCa38vQODV8jfNPzL8fs0NrIoCzk7xp7IgNFxKaSGNYjXEH8xLdE2yl7ZwYmc_NRK1e42wEY1pCxh_xufI9b4q7hYsTLhCQIjdcCH_bFrU9qCmeK_KNJDkpMwtQkr3dTHEeq1WLGxE5x7h0RbF8GUv8aHE3Suf2gHufbqrviWFakZCGQKH3cMVg-TghQ5gTT4Br8AHcu8KITrXHdVW8ow25mShUOvHWlZjhGJnn4LXegsni-_jRr9tHlktIgPebOfopN4w7SQAtAwBT9Ta8dSvzXqZaXVS6DnO5S_Hkk9fMaiTc4HZ48gVFWkSY95dh0KxUWMAABhjbU67IRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=ih_SKCa38vQODV8jfNPzL8fs0NrIoCzk7xp7IgNFxKaSGNYjXEH8xLdE2yl7ZwYmc_NRK1e42wEY1pCxh_xufI9b4q7hYsTLhCQIjdcCH_bFrU9qCmeK_KNJDkpMwtQkr3dTHEeq1WLGxE5x7h0RbF8GUv8aHE3Suf2gHufbqrviWFakZCGQKH3cMVg-TghQ5gTT4Br8AHcu8KITrXHdVW8ow25mShUOvHWlZjhGJnn4LXegsni-_jRr9tHlktIgPebOfopN4w7SQAtAwBT9Ta8dSvzXqZaXVS6DnO5S_Hkk9fMaiTc4HZ48gVFWkSY95dh0KxUWMAABhjbU67IRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-7XFsJTmCshuQbVlKW1zD9l7xhJ86tvhGUlaNrRBj89LVzQl0PsS7n3GIAkIDyhcfCSGR0mNjq_SEHmgNPGYrW3cc1lGAEzvoDc7u87lYzH_95t6FT5LuQ2maBAg30QgRguBFhH13HcGnXG3-auC25nE4DviXxn7pddmWdCZFsUyjlEqlJsE9qkKD46lcAPg7jIpcUdmyC6_A3iH5Pzo7OZj3W4SMRgcqzsoL6UBwlpwn_XNvG4VOkEY9Kq1fYwMMu18GF_IM5AokSFV1KgS3Bs53Pq9s-nlwiUWw9e74GJLYiF1DacYRsef6jAS24LbQEMswZHxz5vj1-rECRNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrbGSpoXfythHCoZBJC-IATTggDaA8sSYJHUCUFF6JaSmcCNz50Dm08YyPV3hrsglyZFUt5BelHwatvP8EPqEjHpVrFTiEiOu4CrJvnI_JXgvSnVdmiJhDDSI_YSSMVcS9RuH1e4rLcyFLvzMTApgEFHYupINUlKAxx2rgqIVtgZHFPdWrxUKa5GcFL1dpaNPImFx9OQNWS_aiNB3VROMleMn6epixoxcCD_rDOPmGmkIPt1aApECy0GaU5ESArjlqJSKFB3wXQAxhAkY_gdS4wDOwUX4eH5RyNfalRZiLxKoeVyzp3WnPKaIc15ouJ0KHIJuURfEOV7i1u1_cIEsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVZ5Lo68Dwo6Bs1q4tNhyMmqDhEvhC2s62qoNyfrEcsI_ZSBUJrmEtrFohzGjTUMdiHr21PuClf1RdCyDVLSzL60FWvdstj1ZDLjMEsYpAyx2B9Eoe5Xf4E_AzAvgX9kUR-qgPsgU9KLm5vSNjSzIx5JJa5hDmb34J9FReCjtRlpwRwXBOCWR0BOAlzFza_viEp_0LTjVh2s0C7E6yMtM3YQCxMmW8mOEM3L9gxSgfwPdi7983E5rZV8ev4SNZOq1BSms98YqAN6RMw8dCcobWXdTCES68sINPknz_MtYYvbrWzXRvLsKHWtHUiVemOSoy3DYnsTaVXqjUnZVXpkNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_tmonF4gLCNWpRQk8gWb0VFEB5QXaKIwAfzAZvNF_M3xk4oAN5VpAciPSIiq8qLubsXCRsx1jcKw1kyTlkrflNm9X6leet1th74TP3_9nUyzP93t5E_H6baY8jlpHOgu5Rv9DvVpYx9PsIc8PPhX_QL71sGiKzW8ffglwXVVDE8j-RlNuyw6s9910rxfuR6fujIyr3Qw9A3DFoen78lulvoeC8XHa7m4tncH_34_iIfcU5E0AhJDWmaw-DjIDL_gF7KJjEe5DtdmF_xh2MXY1xMVj9yE8vnaL605uvJvcqKTt4XWBerQgnxlB37f2Ki09A4UGeG1KqfOGQZKrxc6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3A2BpG5Y4vUq4pB33Qbt0Gp0rX7MqtmxyrPfGHB3mOxcmu-ckNPasycbOtt__2PewooKuw2ybQjoNK7_jPvM8eWigPndSPnmhDsEFv-mhYydiN5xFnpaIG92T7rMFpWnS0R7ybRPJGtizia0S1x1VLYiUGaW7YVh7TVnrr8EurVUOwe7D33U4PAuTFeBB2NG_ohOni37r8tZg6RyEQldDFe0rF-E7sSl-cDdcjjEPOB7rYp5BGZjAZfmYDbfiv-usPMctzfxPLRfHgpjJtOUcpHw6Uf1XaKbsR23ieGVW-afHK7_EZ6cZrgxVnD1WC2NsuBRhDKlD2ya1Quy7G8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=hONcx0OO1ICMui004Abm5KqsIS1IiO-V0Wohioj7VcFX0AqrdScdydXIEJjVx_HqoKa-6vHvCW3cfJ6I2mHgx06_eo0_u-5OQMdnBxLYKNHyHJkjInAjpmr9z3cqzjXRMRlmBUmvUdroBdRPZdYVsCg6HEl-UcI_BdlTKRDEbhw5IMvTGUE1j6UqAu0nWamNXMZPL0Lq98afnONh8Lr8RlI4lxjx0vvBCmf__KSofEPjwmYrrDjBM5Br7KbojytO-ExMUaQIQ-M_h5DHehgpDHW9qmFygXbfBBd7iPpLzMEm4nJXbmongeWEO0thAF_1nPCDIUYL9-NcS7GhnRXPkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=hONcx0OO1ICMui004Abm5KqsIS1IiO-V0Wohioj7VcFX0AqrdScdydXIEJjVx_HqoKa-6vHvCW3cfJ6I2mHgx06_eo0_u-5OQMdnBxLYKNHyHJkjInAjpmr9z3cqzjXRMRlmBUmvUdroBdRPZdYVsCg6HEl-UcI_BdlTKRDEbhw5IMvTGUE1j6UqAu0nWamNXMZPL0Lq98afnONh8Lr8RlI4lxjx0vvBCmf__KSofEPjwmYrrDjBM5Br7KbojytO-ExMUaQIQ-M_h5DHehgpDHW9qmFygXbfBBd7iPpLzMEm4nJXbmongeWEO0thAF_1nPCDIUYL9-NcS7GhnRXPkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=oAK9JZhrD7b6R7mhcNZydR3duDAQTwsZDgBZAB0tKIFgaaoU5pWcIdtVZ3pP8cu7YS-QrlvXDWo7bfIztoN3lMweP-eLhlsN4l4xwy9em2ttNofzMJN_w3KLGGkJMPY4f77FipAMP-3agRVKB3qhRRMsJ4Mm5HqQPZtIlzUx7g5ZsjP_iuhg6yk6JXiNvx1Yxz5X4UhPsS4W2aZeG0rgM-XJlBELiSb3SkeUXXzzpzyTqLSaLoNZLziw1fiwbz0QvUWF2zVFixr2brQx1oN3VdYOXw8hSN0Tq9HJHq64aX-daMD7AwsJRN4wT-dVyvneSCmeRkoylM8Ts9NHypzehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=oAK9JZhrD7b6R7mhcNZydR3duDAQTwsZDgBZAB0tKIFgaaoU5pWcIdtVZ3pP8cu7YS-QrlvXDWo7bfIztoN3lMweP-eLhlsN4l4xwy9em2ttNofzMJN_w3KLGGkJMPY4f77FipAMP-3agRVKB3qhRRMsJ4Mm5HqQPZtIlzUx7g5ZsjP_iuhg6yk6JXiNvx1Yxz5X4UhPsS4W2aZeG0rgM-XJlBELiSb3SkeUXXzzpzyTqLSaLoNZLziw1fiwbz0QvUWF2zVFixr2brQx1oN3VdYOXw8hSN0Tq9HJHq64aX-daMD7AwsJRN4wT-dVyvneSCmeRkoylM8Ts9NHypzehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
