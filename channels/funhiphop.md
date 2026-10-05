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
<img src="https://cdn4.telesco.pe/file/NlHAZyd9NCZDrVw83oZaD4_YzoVnhUR1jhqj5cts6LQEH1SoORVD_PU2BV7vu4nKUiKdiLxXPz9DYWldUcOCXk1Yo_K4WNjTa0XaRJu-Gaad2pcVYzB8kORn1BuAguHCN7CMc1SfeS3pMgC6huY4uZghn4wkoLCPU-7LAy_PCbmY8xZh1JhJpY58P9dCXQctV_9eJpPNcBmZW_heoKdDMGhx8xTia78JdrTx-4JxBKmPi-8cMcKD6XNlhvRecTN1FUCtw_0e79rAfQUemmO1Ku320sEeoOQotWolcyL2gf3xwfpDf75lIvmxpKpBpyloqfHSChW4Nxz2mCc8Kq0k6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 258K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-84427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ve1KBUC564SpUBqaWRGq7cV61_0OT2FO8HKuhnewUOLLbC8-iggepPpNpJkspTiXctEzb93IbaA1JbT1U9t3BFaAhOh5LCgsO4GFfOmZelILdaGpHwgLYJ4quLzvNIQ5-djXCOk0kSP7WIz3d8VgwqART7DC4xO2Qouifb3y1gZghWupVYxeafWHVM6Mn0a0ZGmi3Ridru_D1m6q-FbgSG76bsxxMPO1aEhgqK1SnjhY6DR_cFIN1ENlkGWrUP5Osaw_9ORjtvv51iByol3AxnapJ19Yf2qEUf9SCXSgywuFV325yUdPQdP7RdFcein52iYmz0m3xJLfvOTUcTvm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vRlbcHfk9ppagbx6SMPvnUrMV51v-jHDziNOs6DIH1CWCtekO6RNtWJiuMrMtp5pwDrkf0VcRif6ss8QlJAwuBSM5tdqaBkWeLDnqSgRVKkGjO2rXooAtYLxo7nOxIIIuuYo9JMprLkOXlg1HrDlm9xst5kJD_Fd3mfwowj-lR8TOgCt9Cl88VNV39ZDvRRCeAO-iX8tgLozLoPuIZyE1RzzvbcnHjkD777zx5G83o3GyEoHy0vTzwy3f0ej7SmqPqWyGaKeDqYjLQTK8YJemSz3IZ5PlsIgzz-5GwrejTXaQBv07XN5i7LvLssO73SyrqO6C5vySiQw-fUkiQ-1cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صرافی ایرانی omp finix که امتیاز رسمی و تایید شده ای داره، پول مردم رو بالا کشیده و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده و مردم رفتن جلو قوه قضائیه دست به اعتراض زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/funhiphop/84427" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">علیرضا رئیسی ۲۱ ساله و علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شدند.
قبلا علیرضا سپاهی بخاطر از حال رفتن موقع اجرای حکم اعدامش راهی بیمارستان شد که متاسفانه خوب میشه و حکمش مجدد اجرا میشه.
علیرضا سپاهی با دختری که دوسش داشته شب قبل اجرای حکم باهاش ازدواج میکنه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/84426" target="_blank">📅 11:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL63Hw1Q5spZhBQyt6Y0R2hxbWE9AUtl9rK4PbFcQY36okqKipV9YJQl5DLzBHlTyo8wckJRnhnMH9YgHJP_H4cnFmMOK21ALOAKspwW4RYQGVMDMWX1bWLEBA0M3puVpw41QjwlPRmeuUWJrXeHFmykBuBPx-nvPZe5zn-KOkUwEhqLTkhlcdfq_a0MWCT-8yxdYrJnnwl8igHb-QgSuUQg3GavgddiOJCPUCVyTWpgxf1h0-WB8UPXFoWLPj16brmdIZJOFYRLCK6eu-0ygciJctaOJbHpZxP8NyuKDZYOXmnpjLFWD8M24waN_Wcq2nccH6gbrWaipqKszTzaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84425" target="_blank">📅 03:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فدوی: قیمت گازوئیل تو اروپا 2 یورو شده که یعنی 700هزار تومن
ما اینجا 10 هزار تومن پول بنزین میدیم که حتی یک دلار هم نمیشه و اصلا متوجه نمیشیم گازوئیل لیتری 2 یورویی یعنی چی
حتی با اینکه قیمت ما سه نرخی هست بازم کمتره به یه دلار هم نمیرسه
این شرایط قیمت ها بخاطر ابهت نیرو های نظامی جمهوری اسلامیه که بوجود اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84424" target="_blank">📅 00:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84423">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تو رسانه های اسرائیلی قراره بزنن
تو رسانه های آمریکایی قرار نیست بزنن
تو رسانه های ایرانی "زدن" که میگن چی هست؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84423" target="_blank">📅 00:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84422">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بمب افکن های B1 آمریکای که برای انجام عملیات تو بریتانیا مستقر شده بودن برگشتن آمریکا
ناو جورج بوش هم رفت تایلند استراحت
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84422" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84421">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=TO7F2gMyCFA4DGlize8MEWmEMKSa5QWYitXvRvMfpFSdPaq2mZmAX0AYgJh5F-qiqUNyDWJEslWjI1heM_JkTV44AOWL1sGGOGCIjULhHsM9pWjePnSxQ_pOw17oHtMUQuX4_Qf_C2E5WlF0aARXy7sYvus5YMyBHyg0emSU1ZBLvZxeNVOItPPVWxMeYWPSHFdUCxqcoN4u5AcIiG5J2CxvRvax8-nBh8cdrAROEwkGgn2RnoraRUzc4HdMR4YLCo_d-RKBe-7AKnHQY0aGlulpzd-POilbs9FjIITgwgrLG6hyHKYUneGI4ECNiCIHeQiDVLbtiWN0Olby68GN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=TO7F2gMyCFA4DGlize8MEWmEMKSa5QWYitXvRvMfpFSdPaq2mZmAX0AYgJh5F-qiqUNyDWJEslWjI1heM_JkTV44AOWL1sGGOGCIjULhHsM9pWjePnSxQ_pOw17oHtMUQuX4_Qf_C2E5WlF0aARXy7sYvus5YMyBHyg0emSU1ZBLvZxeNVOItPPVWxMeYWPSHFdUCxqcoN4u5AcIiG5J2CxvRvax8-nBh8cdrAROEwkGgn2RnoraRUzc4HdMR4YLCo_d-RKBe-7AKnHQY0aGlulpzd-POilbs9FjIITgwgrLG6hyHKYUneGI4ECNiCIHeQiDVLbtiWN0Olby68GN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه همجنسگرایان
🏳️‍🌈
طرفدار فلسطین
🇵🇸
تو فرانسه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84421" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84419">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=BxbP5jvIj0FoD-IXsXvdDCFbvyaCNjGPmn75Ij3wc4NCT3ITleT1T1HjEUceHa0w7poXNooBvHOxp0E3cviM4ohxBg0mLCPkzGLiOFmj5Ka7d98jIA0bxW4JIFbuCxo38Kc-kTjCTPgxiZCOoK6wazVnm7xd8lGJs5t8xUinqbm7MB6ISuCuwYxXlCgpa1ayP6Ah4TU52WNYDINSRuUTIPvIjIUnoN0XCUzPyz2mzZ2r4n2y8NOj3LlPwhr26hXGQTzMUL7_oWV8W93B2hkYQkHOOpSN2KUrk-_hywmo61ZmtJmATJcCmcuIOh1_etUHxmKfEBmg0ylv1LKB_Sk8PiL43Fd-ou5jIaBysrr8xpkeehD1beITRKZaWcx09roatayi4sLswvsrib3T-He8jxjbTjqBy8RUDnSbrNOXfd433qafeZgypgS_LjFzlYB8Ybash8ahqGwsV9QiLX8VgCEmZCOyTzF2G-xyPNq98WiEAoVmMMFDQxKLtFub06b2S3MOtDGqwfIPqG9i_WKjalflP1VtcFyjYE1nV6tyf2T4hEXhxQReP33i0K8yTSDcFphVAIx8aDP0Rr9TbS8mNQm3J_MCIpVs1sFpgRia6iTqdTgyemtYH0W_iu2j4pASQk9m3aqfk61YE6OV5jLpxKa7Ip-rMeBCRK1eXEZr9tk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=BxbP5jvIj0FoD-IXsXvdDCFbvyaCNjGPmn75Ij3wc4NCT3ITleT1T1HjEUceHa0w7poXNooBvHOxp0E3cviM4ohxBg0mLCPkzGLiOFmj5Ka7d98jIA0bxW4JIFbuCxo38Kc-kTjCTPgxiZCOoK6wazVnm7xd8lGJs5t8xUinqbm7MB6ISuCuwYxXlCgpa1ayP6Ah4TU52WNYDINSRuUTIPvIjIUnoN0XCUzPyz2mzZ2r4n2y8NOj3LlPwhr26hXGQTzMUL7_oWV8W93B2hkYQkHOOpSN2KUrk-_hywmo61ZmtJmATJcCmcuIOh1_etUHxmKfEBmg0ylv1LKB_Sk8PiL43Fd-ou5jIaBysrr8xpkeehD1beITRKZaWcx09roatayi4sLswvsrib3T-He8jxjbTjqBy8RUDnSbrNOXfd433qafeZgypgS_LjFzlYB8Ybash8ahqGwsV9QiLX8VgCEmZCOyTzF2G-xyPNq98WiEAoVmMMFDQxKLtFub06b2S3MOtDGqwfIPqG9i_WKjalflP1VtcFyjYE1nV6tyf2T4hEXhxQReP33i0K8yTSDcFphVAIx8aDP0Rr9TbS8mNQm3J_MCIpVs1sFpgRia6iTqdTgyemtYH0W_iu2j4pASQk9m3aqfk61YE6OV5jLpxKa7Ip-rMeBCRK1eXEZr9tk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیدا این بابا بولد شده حرفاش شبیه شیما کاتوزیان نیست؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84419" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84418">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Chera?</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84418" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84418" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84417">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR_XRa0_eBeHjHzN6_3VGG0_3RWlQTTnAjr0JshgP7M_nnEPreBOwAeDOHNJOB-wZc08h0PJ6tfsLDHgt7jUUlDAtCxsplhe12MgpnfmsT-kXffqTdyrVjyVNWtTWSAEMRO5QbYJa_9B1AwDlhQ-vOV5p0qpI94GiJB-3NSTdobamyhTEDFjmE0CPv5CcRCiGTbZMrUq2TaQqtf9xuMZC56QRS7R_qP_qVHKEe5RPTN2DOEetVp35H5SOL02LxpSEwgFV2z1b1GvCWMF2ttsWxiptwPDVkLhYJ5BVgCUf8NX7HlmW05OEtA4kQV48QJZCiY1vi5Jvv41Hwa7vl66uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
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
👎</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84417" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وزیر نفت جمهوری اسلامی استعفا داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84416" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDaYLv12BYM9N-F1fr_8mUhLvpUa766jKJi2w2RsKthlqRFuEtiH2tN8_bLnpaZYIh8WdMG59VXqA5JoTfMnPiHZ5AuKfNnB_HnffAUZAIq70FDL2QWh4rbQ_htkrVvAKgnsfDxFtcy6PCAOljqAB1Ee8PQ9bEL_17F-DKsEgx6b-qJ2pPWnrAe94Ibxhbp1O2L3BmkBVh2vBVlLfPwRW0dVpxao8L5nitI-kH8bt-j8lX2yVRuuIXNVPCUE2QKs_FLfgPLA0CyFKoqKaJCe_MEJIlvo3M-qcBbzB-PrVtJVZtzBso3O6UMabbOr0iLORlaTFUkljmicJpQ8okuxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و کاگان به اسم «هالیوودی» منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84415" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti9uP5_BrCXGxzMrb8byHsjkLh61KYpE0zTiYvM4-IfUe50adjxnofT2oGWdcmZebRPeybFW0v2VpZahTh7SOWYDJiwDeFBh2tfqZv4BghXyMHLEDLwmiF14FL2iyNT7z-XsJs4QQAL0RrmCqfFyMM0bgZy_Rympvq6kgkBU6rxb1fVPdOCYQOSygOMYWGiV3XKpSJobpKi6l4Hr_Mr4j1a8RpjZ-d87qiiGVMq4DpBaGmBIk38-taH2ZgQkQ-kkL7Juk7XkkpGZFGjhDjzMs4v4FNXsTXJJDh9pZOMLMYJrQOf-UZu34t1zxPfE9FgmP3XsUknUa6WE1WkQkrwgQA.jpg" alt="photo" loading="lazy"/></div>
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
G12
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84414" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbMhFCtArXY_qHrNE8YtPivllAWNyVEB5ZxKetk4iPuNikLED1bhGRy-BJJSGg6Rw9YKKhs7MdpdhyI4t30yUQSs47IQTFRw9QTmHpZ8jlUVbeAoHT3TSL6LTQRwwWO8P9N2tEXm7yne-UKVEXKCYn2XFjUbOa5bGFIl1WkpNb9XBrMYTU_EPX10qtd3mvcJkYVVCUca4FzA5GGnaKtwQyCHJ13ePIIzJQmUG1IiC3R3TVojA5yEKFzZaTxKJRA0aGe-7vPaZe02luBiJOecBWWKptiFCVfFAV3MYTuotatbEP1hZedAWvvHbzy7wHLc77w_qiKV4hW2c3fRfdC-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاد کلیپ های دوران بچگی میوفتم توش میگفتن من از اینده اومدم و ماشین ها پرواز میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84411" target="_blank">📅 19:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تهشم داداشم جوکویچ پیر سگ مچ زورف رو‌ خوابوند</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84410" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84409" target="_blank">📅 17:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84408" target="_blank">📅 17:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqfdUHeNE8l6ydPDwQ4jH63nxpZKzvJdZ7pVD2Eyhb5q_vCBaLRp7u7yhEkLRha2_f_FvMSzvABzDlMtBPEezB7y6lmPE8pBreitZIQnHp8kmU1s0C4-w26wXOK6swk5Epjefou2n9SNelAEUMPWt7v21hqDSdjnGM-65G7pbOYNah5sa8brJ3wAOBiIqUZzApZVVYHV4XvVP3w_IIMBlspBU1w8Q6zx5ah3Zlc4uZa9na3-cWeZbd_WOFzFHDvcLr4xLHBPISjBlRGATC04pogD-U9whBkNrhk8AoTYWDu00AwbN95W5ijdYwYZXdBjOX7MVO3TICVu1pLKhDVXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام "هاها" ریلیز شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84407" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=YJ-zhvNL2IFPBZj7YwoLq23SKsNqPEDdOzCLp81j5EktrKq4Ccv_g0xiqlQwPhx1ar7QovlZB9IMVQxNfJHVzCFHih35Es78l0Iuo2Yw5tR9eF10jWUyf-FSzRaJVdXklK0un3bNZxy2AGRf2tSFgW__OcJvZgGHyNJEI3COsvY3SgK9UiZSkvkN5OEbsPMLOWra3DTmUxz-_BNxUNWH7h4Hh6G6eqzcctWkoJGWNyACz4cbJWQ0cOO70nKsdfVXuva_yvPmoAlDkKwIr-LizK_lRQW0Z305iCN3chb2uZW7VcNZN6HMi3ILW5BoDS1CUswFAS4FkiwgPRo7HlcKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=YJ-zhvNL2IFPBZj7YwoLq23SKsNqPEDdOzCLp81j5EktrKq4Ccv_g0xiqlQwPhx1ar7QovlZB9IMVQxNfJHVzCFHih35Es78l0Iuo2Yw5tR9eF10jWUyf-FSzRaJVdXklK0un3bNZxy2AGRf2tSFgW__OcJvZgGHyNJEI3COsvY3SgK9UiZSkvkN5OEbsPMLOWra3DTmUxz-_BNxUNWH7h4Hh6G6eqzcctWkoJGWNyACz4cbJWQ0cOO70nKsdfVXuva_yvPmoAlDkKwIr-LizK_lRQW0Z305iCN3chb2uZW7VcNZN6HMi3ILW5BoDS1CUswFAS4FkiwgPRo7HlcKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عالی بودی حاج اقا
یه آخوند یه ایده به سرش رسیده که رزمندگان رو به موشک ببندیم و در اسرائیل هلی‌ برن کنیم.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84406" target="_blank">📅 17:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuzY3A6xmNdV6DQ73afOSKwlYSfxOl3pNejFX-w3QuDxICqqdBLZxUI7UP5eRXZcFUpMwdTKzDmv8mm7Y9thXrT9aHO4EyhzXAh-Qdp-0LWBCCc1B_LobCcE4xrxw1tZ8y71YJMQ00wA0wFAKtyvJsPvMhDfxCiPPhd6rPPrWwI0k8sE0tyokgat4FmdS3e9orp37Kg4TAb_uqUQrtpFo4LwlZ3L74ABG8L5WG622qs248K2y1fRhWigbUbZphsHJZDAqBKAGZbtAYmMjkAfwH9UZE2aoQh8PFVlP5j7plbUciPhSXUo1U-9SHD5Pbr9rr0cHI0WPAx-EKgT7jhNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کل زحمتامون بگا رفت، تازه تو ویدیو هم میگه امیرمحمد افتخار ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84405" target="_blank">📅 16:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=ECSx5KwJWdTVquU0KQup8j32OhJ0gIF3HCyTQELw5QEPUkpFEGJtM0bCF-TRV4JsLTvZdBa4bGXH56egZBvvZDDknuaVSUpmRVSvo85INytiv1sEyxX2LXkAYuWMYb3O_dQHWl3106pW9BGH7WZN2mH6K-uMWm-w7TUrBNNfr1vZTeNd2HNLOdBFMS4v4LLxc61y5M11CpOdontu3iAFLIaA8meV0vk4MMXiJXArZHPjr1GTrAIxa-3DwThux0Zy1vNQbENcmLHIOt7lspc1yEpGGR6ochcqrDrvG1f-EpBI7p0J4lCsMpxfQxrLOJT2-TQPNbgPPjnftD60LbyhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=ECSx5KwJWdTVquU0KQup8j32OhJ0gIF3HCyTQELw5QEPUkpFEGJtM0bCF-TRV4JsLTvZdBa4bGXH56egZBvvZDDknuaVSUpmRVSvo85INytiv1sEyxX2LXkAYuWMYb3O_dQHWl3106pW9BGH7WZN2mH6K-uMWm-w7TUrBNNfr1vZTeNd2HNLOdBFMS4v4LLxc61y5M11CpOdontu3iAFLIaA8meV0vk4MMXiJXArZHPjr1GTrAIxa-3DwThux0Zy1vNQbENcmLHIOt7lspc1yEpGGR6ochcqrDrvG1f-EpBI7p0J4lCsMpxfQxrLOJT2-TQPNbgPPjnftD60LbyhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها شاهکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84404" target="_blank">📅 16:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=Zx5xwCHgG9pCvcUY6gUIHJITF0w4P0fdJkub_mVld5MaZAqPNLAtAV7vAy3v_-gQ2iUvOrEpKqAg5PAdFtX-lSYkEAaS42sMoIarx6ZYm7dv1wjs3xFa_IKVummuumb7nztWSLeEVQUCEiUXfSYtkeA9-VfPyvU1uDg-w2ctdzKLbJLbQaFYn6lK8xUrLgr5h6TiLqM5WMfNW_UV7S5RU_hANjKsOI0_XPb76moc3Pum1s9mf2aS_T7dFKm8L8GlHUpBcMNvJPrhvIFUgALFB6nm_4dACWeV6c7wMlH1W5-898B1gIWoStheMNaP_9Z_ButQ-8NhfxfJMmwMo9FHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=Zx5xwCHgG9pCvcUY6gUIHJITF0w4P0fdJkub_mVld5MaZAqPNLAtAV7vAy3v_-gQ2iUvOrEpKqAg5PAdFtX-lSYkEAaS42sMoIarx6ZYm7dv1wjs3xFa_IKVummuumb7nztWSLeEVQUCEiUXfSYtkeA9-VfPyvU1uDg-w2ctdzKLbJLbQaFYn6lK8xUrLgr5h6TiLqM5WMfNW_UV7S5RU_hANjKsOI0_XPb76moc3Pum1s9mf2aS_T7dFKm8L8GlHUpBcMNvJPrhvIFUgALFB6nm_4dACWeV6c7wMlH1W5-898B1gIWoStheMNaP_9Z_ButQ-8NhfxfJMmwMo9FHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواشناسی یه بالن فرستاده هوا یه سری نگهبان معدن فکر کردن پهپاد آمریکاییه با برنو زدنش.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84403" target="_blank">📅 14:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84402">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ERdmM8nm8AaqfSv-YdQYmXV5L845uf2mUIA1MUE_OQ6RrY9jZj7Y33MXY3JrcvhBZhX5kz76Y6CBtsfMSo8WLNR5_i6I2zQairVOywSphm-n1vdeoD9WYroh56KU6T3XsaaIlRdhhPr2s0Zpy2jDg8DlxwEUmlh6Do56y8MYKnE9OK-Za8Yj8Mu3oeeUieNvXoB0VSz47vKcXiyE5JEneEVC9pcc34xbcBSxUMM5IZPsiNcIIfrcWXi_1D9h34RwlkDUwgGIGimvbQ2BasEIUXkPaD6K9sSYlyVg0RwG6rhbHlYejEzVA2p1Mw20NzUezKJgzX1gv7ounl6Cfk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی تو ایران هروز شوکه ات میکنه...
دو خواهرزاده، نسل دایی ‌شون رو منقرض کردن!
چند روز پیش تو خیابون آتشکده اصفهان، یه مرد میره به طبقه بالایی‌شون که خواهرش اونجا بود، میگه صدای سگ‌ تون ما رو اذیت می‌کنه.
ولی اونجا اوضاع بد پیش می‌ره و دو خواهرزاده (متین 29 ساله و مرتضی 35 ساله)، داییِ خودشون رو با چاقو زخمی میکنن.
دایی چند روز بعد میره ازشون شکایت میکنه و این دونفر هم به بهونه گرفتنِ رضایت، وارد خونه دایی‌شون میشن و اونجا انقدر بهش چاقو میزنن که کارشو تموم میکنن.
تو همون حین، زن‌دایی به همراه دو بچه‌اش (پرسان 6 ساله و پرهام 12 ساله) از راه میرسن، این دو جانی، زن‌دایی رو خفه میکنن و اون دوتا بچه رو هم با چاقو، می‌کُشن!
در ادامه هر چهار جنازه رو به بالا پشت‌بوم‌ می‌برن و سعی میکنن با ریختنِ آهک، این داستان رو مخفی کنن ولی نهایتا پلیس متوجه میشه و دستگیرشون میکنه
.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84402" target="_blank">📅 14:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84401">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">قیاسی سهیل پرنک رو دعوت کرده برنامه اش، سهیلم با همسرش رفته، اونجا گفتن باید یه اسکارفی چیزی بندازه رو سرش بعنوان حجاب، سهیلم قبول نکرده و نذاشته برنامه رو ضبط کنن و زده بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84401" target="_blank">📅 13:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84400">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Winter Is Coming
بابک زنجانی: زمستان سخت در راهه، اما برای ایران، احتمالا یخ بزنیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84400" target="_blank">📅 13:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXFXkWLTHzyjppzyTuO9Vix9Yef_cmcWrBqD8xoaMLmFygLMUDTGrPrxmHvqZpFSLLTNWjedkSZtisEGhYpvpstzSJaUQW30CWJLf3hbzoG56H9QSyiI_lEiaa6idYgtQ44XOOwNPC4tpurwwa3BomICrkxpDbDw3judEQzwaBOmYr1a5hrujrwmSZOviRur0erv4Te7qslvli4mhwzMfwVMDCIyC91-Dk-yD0K3yWczZmGNCb5sjtVBKLQmmGdOEz5wUsPcKxBnjt6X8dEiAhw-SfuUE1tP0l-zRw05PbrPxoMX1APYYRKBV9hQLiWn5bsohlwiiF8ott9M-pp-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظهرت بخیر ایرانی
-دلار:۲۷۲
-طلا: ۲۶۶۰۰
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84398" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84397">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=L4E5HXLJoWWZ-v8_YSt46aMSG2xfBhIauW8NHUaUKuS3QDmo-FASKZYZBRWHDybar9bKeUK0fKKevIvyPrD-ASkWyENBsI75Xl4w5FtZeocWw1S0lySMs61EEUg5rAROhoiV6x6XkNobiqqJPr6GTOkP3VtyJu12pWdCPZl4RyBum2WIY0uKXlPLs1h0isA0I6fnC_g8174Qhq-bGT5zP-gJsT_J4rqWl8K5FhD_6HM4R3_NDDTFaq6Zhn7ax215hrrmtxl2CQ0mFhB1keAB5bulZRdsZabIs3BuozDKqZ_GtKrEpchVUJLxH4fdcDnnUBumg71pJYpKGmySkyYiFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=L4E5HXLJoWWZ-v8_YSt46aMSG2xfBhIauW8NHUaUKuS3QDmo-FASKZYZBRWHDybar9bKeUK0fKKevIvyPrD-ASkWyENBsI75Xl4w5FtZeocWw1S0lySMs61EEUg5rAROhoiV6x6XkNobiqqJPr6GTOkP3VtyJu12pWdCPZl4RyBum2WIY0uKXlPLs1h0isA0I6fnC_g8174Qhq-bGT5zP-gJsT_J4rqWl8K5FhD_6HM4R3_NDDTFaq6Zhn7ax215hrrmtxl2CQ0mFhB1keAB5bulZRdsZabIs3BuozDKqZ_GtKrEpchVUJLxH4fdcDnnUBumg71pJYpKGmySkyYiFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84397" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84396">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCfykZCtPtxhqF-6suX66C6n-qg0kF4Rz83rCE6wZF9uGRzT_8ggFFuvgzyShhkqKCFNZsAqc5nInJyU9XJZlYkMVjBCSutE1f7ZwczqUhRc2KRPIRWwum9VNr6VZ9uv7l8rPgEFCQSKw0Ja_F1zJyFhAyfh-QL1U6EREwPkVP22ewklVU3-4SqiLH-93JwluoUTPy66-XfC5orEeqmtYAdl23MrNb9_gbh72tEHdIY4gSvloC2XCi8VhrbaDK2nVLhW9tRS_vuDuTutwWcngSQoLiJHxNhMIs6-KfMEf8GCx7kJUPHkUbKK_NhtdvC8Bem3uTRXWzoLDteoPAAefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
روزمون دراماتیک شروع شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84396" target="_blank">📅 12:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84395">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYR3F8PozcTGr7dDFARI8Jqz41DwtynAshlmZRdHChF8ZiuJsnnnQZXIA9_fR4XoBoznqtiibqbtARPlAWoqhKfvh67Zs42zi-t2PFEXlm0nUZidMWYoslLosjdRdIKH5LU-jROUSTxxge1Gg1-vkUTcOvyzhwtz-2jhTVJ3FNrpvDBYcnUJW5dYxBl_uuQ1kZvE_Tylbw2HtyAT0de51ReI9aaAN2i6w-gxgMf_4AIKcaPa9S52BZf2BEiH0VZYlur_6PWl9LWTEBva2UzvMgDwOkWmvbQ7bn8WogInk8WZPjAyqPo8-L4xv4G2SfvN4esB_72vNPPHo0tdG8_HmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشین جدید ایرانخودرو به نام 207 elite
قراره از این به بعد اینو فرو کنن به ملت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84395" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84394">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84394" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84393">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW8rqQQ24e2QMCfyEjGF2Xdoi6LRQR1Uami6S7bJi5Jx7RyoGTzzWQjcVZK1KeUOQuIDcjq8FHs3ua_axczRbfouMblmDnKow0E-OH8HJakDVVSxcqxFj1utPZyevCwoBXgWVl7_IyCSxGZvcnNfmnRG8zlkP_hHtMTweoAYDHalPPP1qdsE_waItuibPiNIYjPpyj3eh8bYJCV71sEMJQTFlUimV3WFWc3kL0Kv_fuAN3FeW9U75m4-KNze0SN0jQQLCgzJ-JkfTl0lPtDtzqldURzf08fKPa-lWFYfsTBO_H0ujPwWV0TG3Jqac0cVM-oKK4IgtE4ZCmSUz582kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R12
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84393" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84392">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=GXHX4qgxe-5e1FwUuu-ujdGhv6mzBJh40RU6YmsHfN9iHFsTXsYGGD1f5AN-8Fddb5Gn1-ZBfbTh0AM4tPHVuwiLsZEz4TrrL-D6HXbxL28fq192z1hXrtYu8c6kDvDz1RUegM0iI6tosHvxl5gi6a4w7jhpeJ5-DjvbjhKjpLayDLWIY-t8hteb1R9jdhWEFiCVIMZ_da9oNY1IcP1M3TEBjOCmkIcOturh4dxiwOo7_GrC4BrxwEmM3Lk3pHmIpQwxs6cYd1Tr5inZZAkvCqUIyK3E8Ml1kquBM9xIn8P4ept-0p0M1FXFOqg7UsylXq8LX70TYALHg2B-WR3gKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=GXHX4qgxe-5e1FwUuu-ujdGhv6mzBJh40RU6YmsHfN9iHFsTXsYGGD1f5AN-8Fddb5Gn1-ZBfbTh0AM4tPHVuwiLsZEz4TrrL-D6HXbxL28fq192z1hXrtYu8c6kDvDz1RUegM0iI6tosHvxl5gi6a4w7jhpeJ5-DjvbjhKjpLayDLWIY-t8hteb1R9jdhWEFiCVIMZ_da9oNY1IcP1M3TEBjOCmkIcOturh4dxiwOo7_GrC4BrxwEmM3Lk3pHmIpQwxs6cYd1Tr5inZZAkvCqUIyK3E8Ml1kquBM9xIn8P4ept-0p0M1FXFOqg7UsylXq8LX70TYALHg2B-WR3gKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتش سوزی در پاساژ خلیج فارس عسلویه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84392" target="_blank">📅 11:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پاشید برید مدرسه بدبختا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84389" target="_blank">📅 06:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc2q_N66ECWaRwq6f6w8SWMXww5VWm6g2IffvTv6LQ0WxKYP3jrlJaqyzRP_J0OZtUIEfHT7wskLI1ofOGnzXu9eaFqrYXSMbwwpEtt3HNi2NXjJHgsUzH2NjE9Zt6YhA7DV0CbQ77Q73ZRGnKwD72jnA6xXrYct2-MKFhWtnWT1m3i69-hjph2UXwis7O2PJBziMsCCx0JzmWhFIBiDc0Oa4mSW9fW9sdLcda-r9tTia4Wk8fUc7Su87ZbbUL27_8KjLlo1pACxySSQJc7pDJQL6MG4yTHB-QCldXis7DrBAddo2qGb9G9kOihMMmDbsdId9gC9FRHgdv4M_NaqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۷ دقیقه نگاه کردم اخرشم نبوسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84388" target="_blank">📅 02:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZL0NNtB07LXRK_LobKHo6XNI8csjAL719eQrhHZQzWpEdTfcX1YJmUMJ72xfOLss-JdPWaNqCwpv0WVZX-Gbtgjua3W8rGEAGUVhdp2SJRXQ8Rn38ARjV5ZcqBc95YON9fD0Vahcm2mYX5haeG9X7FRPICQNJs8e7XbFmnowyiCbqXzVed4Qb-j4l6_EfjxPZ1Wkl3U7xAtt3Lvugw32kGKo7KCP-juLjYoYHI46ZAx88t8EkL5JZsOCYfUtwxMGOxZ2OLaEKy4fBJQe2oFPCbZnzA1s9NDx5yKnOvEjhICQg5FNViZ_GaweCbE9XhEPO-qMkExpusuVf6dYW6eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84387" target="_blank">📅 01:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=Gj1CuhvJBUo-964m0QWIZc8iGCMKhp0jotdkveN0QvP1Y3Bwvf-iNctbK5p04vwBX8RjtPxC7zQnBpq5Tc77SBMdsV9-haru8z58Imkusx8hpAKpYGzbVu9__dm3VVenz_m2AvhUmnkjDruoaPOf0tcfC5lwRrtPkwlwfNBDo-Bi7DjZg-ToRAxiJcb60w5sFGczllod0DyY-ph76q9451beyYQ7JdbG691jDbifiz6SFWh1TOzwcHTASpLoTkmEajhYQO4Zd_nyzNxMT79Ohm-vA8uJgqIT9mkwcNbVKvISZmqPYqXZeUgBcjV0u8fsyptt_fx2rQnJpmSadTJACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=Gj1CuhvJBUo-964m0QWIZc8iGCMKhp0jotdkveN0QvP1Y3Bwvf-iNctbK5p04vwBX8RjtPxC7zQnBpq5Tc77SBMdsV9-haru8z58Imkusx8hpAKpYGzbVu9__dm3VVenz_m2AvhUmnkjDruoaPOf0tcfC5lwRrtPkwlwfNBDo-Bi7DjZg-ToRAxiJcb60w5sFGczllod0DyY-ph76q9451beyYQ7JdbG691jDbifiz6SFWh1TOzwcHTASpLoTkmEajhYQO4Zd_nyzNxMT79Ohm-vA8uJgqIT9mkwcNbVKvISZmqPYqXZeUgBcjV0u8fsyptt_fx2rQnJpmSadTJACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رعد و برق خورد به نوک برج میلاد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84386" target="_blank">📅 00:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پزشکیان: نوک قله ایم و نزاشتیم فشار اقتصادی رو مردم حس بشه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84385" target="_blank">📅 23:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=esBDRengup6bVAOBYOaE2rz1t8b4IKqEqfiARtcnxPNs3k-GU3Z3wcTsfE1b0lVOyeWYzpuTiFyT7P3pQxR_kD7_FWYxmrFPXviFT1u462pBwgkthAbgclmepScdgnBRels4FCYCAXwZS89qUx9-080wyCNqGkAh0jMWF-mwTZE2LLeLZD6KniZqpMD2tqcIaQsEGYdr5NUhH_LRypOx4BeNjEWBqj9aBIF9as3Vn9D0tofPXxTXHxqinWp62DlTrWPTmPwlBFsnPInYMW5wvazeha6RYZSE0Xwt5EAI2lY7ifw9HnRkCkB_Rn9QZSLci5scXWoFzFqvDVswIoRESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=esBDRengup6bVAOBYOaE2rz1t8b4IKqEqfiARtcnxPNs3k-GU3Z3wcTsfE1b0lVOyeWYzpuTiFyT7P3pQxR_kD7_FWYxmrFPXviFT1u462pBwgkthAbgclmepScdgnBRels4FCYCAXwZS89qUx9-080wyCNqGkAh0jMWF-mwTZE2LLeLZD6KniZqpMD2tqcIaQsEGYdr5NUhH_LRypOx4BeNjEWBqj9aBIF9as3Vn9D0tofPXxTXHxqinWp62DlTrWPTmPwlBFsnPInYMW5wvazeha6RYZSE0Xwt5EAI2lY7ifw9HnRkCkB_Rn9QZSLci5scXWoFzFqvDVswIoRESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر بیژن‌ مرتضوی: به جای نفرت‌پراکنی بیاید کمک کنید ما بتونیم از پس عکس گرفتنای مردم بر بیایم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84384" target="_blank">📅 23:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84383">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">توپ طلارو واس یامال اماده کنید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84383" target="_blank">📅 22:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گورودن با اینا حرف بزن نزنن بعدیو</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84382" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsQPc86PQ_M2VP1ZDV1J3XNaP6HCP0yxVyUrpfvlkuTQG_DL_MYU1l5f8Ed4WkIeWPTuN129f48qnzK_W9a_m1wuo61FUlz2nwBI3G-wxpGCBKysJpwPU0k71_KXmCMY40KWAHVWpa2XvG3xnjNmL_cihawILWX3Ru6E_MNatqs6XursNWXlb0RJr2gp368HqujfkwZrm-f7zz_Mp42bxtNb415ViKZK5FD7Dp_qWxw4HWA4XsoNSgH5yH4xClTHb4Qum6db79SI5adQBNfMwnLER-DYqoE-1l_KKTNsjWge5mKPt7Gbt06zNOU86Nqo-6-5-VRgU-EhhKXvVsZqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
پ.ن: بیت بالایی شو هم کونم نمیکشه ترجمه کنم تورکای عزیز تو کامنتا خودتون کارشو انحام بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84381" target="_blank">📅 20:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بلینگهام داداش لوییز انریکه رو میشناسی؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84380" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK3H2sFCbg4Uj6t-Xqk4AF-XoCtyBfuuvBos8CMKZ8QPrgPYWPZ-uYAV_yJ8LtFzN758i27V7SNaxocDrQxWLC8C8dxWhDaEXMzPP51xdMHHCYG3SKcgfQcBrO9xpt4hqUB17w_tSGtNP_J546dY-Cr_WEJxHNJpXh3CkROoZNaBGXDs9u_ivirZOraScN5g5mtYOMvyxoaKyW3ZPFqm69J4pT5Y6XYJDL2f6474BdOsdqqx2rZCgcrqUEellwkbWiRMRezSvDesebQCsO_fCJxIKwM9xTGfTjbxeK1FSQYq9sXIt_KPBPCkdYn8GYlWu7PN-x0EXENFVZ3olT9J0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84379" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترکوندی شیر
به دستور بانک مرکزی، نمایش نمودار قیمت تتر در صرافی‌ها متوقف شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84378" target="_blank">📅 19:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=PdJUYtfX1YsNaBNlZt24yubD_Ny4di6Oluy5BVOcHK4CdVvj21qzQjAUemOX16dofEVwUj8XdriBn-kSZncGoCbA6sh2TgHGvpjpltSyutDTcS3Xv5hgrkgXsgn0cDeXDtnhZqR1MfLeOjFC2KLbeQahXg1uDBdgVjf9jMX3W5BFJCRkJAAjzmuH0G_Ilc5xb9LHnJUWVY7EcaRAAGwuGjkrhpy54aVfCNRQ-2FKIeBwDYcUJltdjJWoPUh87N-IlF2G3zhtW2pTn0guV3MTy2G-Io3bvQhGLEYrOeSS414OQD5Ge0D2FdcgGknbKziukLvb1Qr81h-MUEovGMte4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=PdJUYtfX1YsNaBNlZt24yubD_Ny4di6Oluy5BVOcHK4CdVvj21qzQjAUemOX16dofEVwUj8XdriBn-kSZncGoCbA6sh2TgHGvpjpltSyutDTcS3Xv5hgrkgXsgn0cDeXDtnhZqR1MfLeOjFC2KLbeQahXg1uDBdgVjf9jMX3W5BFJCRkJAAjzmuH0G_Ilc5xb9LHnJUWVY7EcaRAAGwuGjkrhpy54aVfCNRQ-2FKIeBwDYcUJltdjJWoPUh87N-IlF2G3zhtW2pTn0guV3MTy2G-Io3bvQhGLEYrOeSS414OQD5Ge0D2FdcgGknbKziukLvb1Qr81h-MUEovGMte4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چرا هرچی خز بازی در میاره بازم جذابه، خسته شو دیگه کصکش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84377" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حالا سریع و خشن هیچی، باز خداروشکر از دوره ای که ملت با سری فیلمای یوری بویکا فاز میگرفتن رد شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84376" target="_blank">📅 18:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIzfK0n7E7p8DzYY9g7hStcKupFk0KNRa_ut4Avfa6nnAjd13YFyENYwgI5cNHTDS5LUqiZqUk_0ku9kbrvH0X8yeVx3iIgxOhp6aMyF2Sovsn8HueDtg5Vi2drZlMFZawk2tXF_X3E7fhO6_7WCQ3ogU0Fqv3V7HjWo9crWjRDVplEIlKE9cE6Cnug13is3YlJOKV8897KnsLeKjpXqfXYll4x0QKsnznYWHe5l5eiJPafUpenFtp7Rd79wcjnhDXAWts8GSgIVXC52zd8J88WMwtY_PIZ6W4w94V8nMakupuOkTk_53u8qtoozvmFqKRWjxp-QT5Xw6Ms7vYybVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شید ناموسا
سریال سریع و خشن در دست ساخته و ۲۰۲۸ منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84375" target="_blank">📅 18:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84374">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=HDMGHzQ6-A4D2pgV5CcVjbGpn6nrsE6t7EKA7sWixKwiq1v7KU9L4ZVbo0zr-HnIDGy30eE5DG2kPVd-2CRScrcnhEzZpGdsBmNltMQR8QY8SmnCeH0SzuxZMxWKcS4m08HPBJPdyX47vCJ8Bpvlums35-OeBU4QCX86r6-H5KbYu2zZzYfRm-2dlNUZA2tkZ9a0dGvBsrSpCAGCX6_78U34ODQlnTMZ5kocuJU_eCFLZFyYjR_Bukr2ynJvTtw54cys46uL4KK_7kXQD4-lzVj9s9D9aD9xDVNkc-qxm1YTqh6Y-gkLbM9yOm5TTJnAhWVvcEEXstiaqQ5lyGbNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=HDMGHzQ6-A4D2pgV5CcVjbGpn6nrsE6t7EKA7sWixKwiq1v7KU9L4ZVbo0zr-HnIDGy30eE5DG2kPVd-2CRScrcnhEzZpGdsBmNltMQR8QY8SmnCeH0SzuxZMxWKcS4m08HPBJPdyX47vCJ8Bpvlums35-OeBU4QCX86r6-H5KbYu2zZzYfRm-2dlNUZA2tkZ9a0dGvBsrSpCAGCX6_78U34ODQlnTMZ5kocuJU_eCFLZFyYjR_Bukr2ynJvTtw54cys46uL4KK_7kXQD4-lzVj9s9D9aD9xDVNkc-qxm1YTqh6Y-gkLbM9yOm5TTJnAhWVvcEEXstiaqQ5lyGbNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دست این پیجای ادیت اینستاگرام
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84374" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84373">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">روسیه: به زودی میزنیم پایتخت اوکراین رو کص باز میکنیم(
چند ساله میخوان این کارو بکنن
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84373" target="_blank">📅 18:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3mb3KWLQX2UCnvfL43k-oaq3vMSMjoJHv96SFW3C0mFgP87RmtNGLl-4dvdGzOurzJTyU2WFm21p2D2x6R6OX1V2PV63dT0yEmBlCR6tZS_x6nTHAz8Ha0YzZJGdouwlQGuEC2JI3h_os3uahQxAuIZgMtpAxLsYPwfNDyIYanCixhqmXDhEvN9XykUYLQRjT5Vv0rI8pkmua7EPDLhsSKSscI6StUWVnxER84_AOI_MGJzoPcI7NgpeQDPzI2rz1W5rvqqMiZrxD6YayNbVNDd4MoH10MQKiX-mq_DQ671s5NVdSL-mvpbceUeAqcYpxjlNoZ8xMMwQ-49YaooRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا منم با این تصویر موافقم، به نظرم قاف باید برگرده به خیابونای تهران یکم جنس اعلا بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84372" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84369">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عجب هواییه پسر، امیدوارم عشقتون تو این هوا بهتون زنگ بزنه بگه ما به درد هم نمیخوریم خدافظ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84369" target="_blank">📅 17:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/favbmyuyhd6cwmsv2YZW3Tc718OscSJnj5PLKBs5OdlDezm_vZhlZLhKXjwAZv1C_XLDzdZZQeHbd96sYxu3iXP-lpPKxqqkJK3VbWq-8-E3kuBuOwf3KQ0LOKzNVnTjahbFsfmUPkuUWGD0BH8F_CV5DtuJEs7M2PmpFAzIlHGB9ggUvX2BDOdmsrrEAzoCMkoQBDYoSA5R2-y1ZTWkjOE-Pd0Hp45sx4f7kPkjJdJsMsSNBtuZ1oP2oYAqF4aEPfLJ0cNeOIWIlrnXYRb8B7Tc2s7GherEqWldiALm_QpzpOCb-zlq7zjvvMTfAdr_GDYsQgN40pSilmOBBxK2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال the gentlemen پیشنهاد میکنم ببینید فصل هم ۲ تازه اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84368" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگه مصاحبه فرهنگیان دعوت شدید همین الان بلاکشون کنید، بعدن میفهمید چرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84367" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این میمای کنکور چرا آپدیت نمیشه، هرسال موقع اعلام نتایج همین میم ها تکرار میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84366" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84365" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84364">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsnOZaXMW17k_iRS2eWmeWwarXDuamUNbOE9rv8iFYyXIF6_ApMjVhh6AV5o_kCu_T0gtrGbyJbd4CL3qSQsMBDo4ZZMhQPJ54nJXRYTFcHM1lKnrk76jgg7bfE-322JOgfY16R4nzDIBXZyuzitzTDozwOPZ7QIhXdlO5Knr5_HJwkoEP6S9O3A-kA3BKG57rEWb9AoaaXJLdC3B6HmLNE7TwsWR7nO0b2wvmDIUmpqSqa4uGV7yGaLImjDT9-WybKeVB0FSarQRqY9izeKFmduIGqPw2vcBX6Eei_KACDjmLu63gWL7qmeN8L4C3O5leGkbazyAnM3sMuvZMpdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84364" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4bxEE7MCksZeGDzONU7fzv7WQLng3tv-8t0fCgflS9oFfmEGhvN-ApDHzx-88uvJ5SxYx86n11JK9BGHkUdvqsdWHQXsFtQWeuPuvqBf5QRRjTZX3cBDuQyUnPU0AXKML2r5f8Vt0eULW59qqLyVh6UnFocFfbfX0pFqSBvAWVoTc5byDW9JdpYFnKMwYXaVBoT-V81OLXB4ljk8pYUVXCCcqJHwqOrZ6fjTPLcJv3vhSGtl04usXvI2y7jBYyti6N2om7hwHP_YjuY9aft3AGLmx1F42IEbWiNfRtlbVkbC3aMp-2Nw3C093T2tuX08WwQCwItt7Vmn6bqcHwN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84361" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTileKhersuk🐻</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3FYKETILLzbZDNuFFbLqZvEDyxvdtdddkf8ockmD8Kus7-HD9aFyn1GhjxgQcZxNZlU5a7JQMiRsfdqxguPKVvd9t9L5ho_IYsBWDNZy8uUhoTCoYlFZFW9xYI9bEClx080I3x4BHuy0KW6yX-zW9_e2PesssCK_865z1Vghu-lNt7Fi05PWvOMeJgHXoKlSHtBTZFWR0C44tSKQxEgcjs_I0S4cSP0WbJBas8BcFZqurjOGvsWHtniomYpMfOXlMP2sGJ79vuwqeMCK2Tf9-MTK-1PmZrQ7lWCus9LaHTMPNMbdmPF1bflNWH0PCn6L_ULQgyGZJ0A7sZhmb_u9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر خوب</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84360" target="_blank">📅 16:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتایج کنکور اومد
بفرستید ببینم چه تپه ای فتح کردید</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84359" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جردن های تولید اسلامشهر که مسخرشون میکردیم هم دیگه زیر ۴ تومن پیدا نمیشه، های کپی ها هم شده ۱۵ تومن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84358" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بسنت اومد گفت تو دوماه آینده دلار ۳۰۰ هزار تومن میشه، همتی در جوابش گفت آمریکا هیچ گوهی نمیتونه بخوره
حالا دیگه خودتون حدس بزنید تونست بخوره یا نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84355" target="_blank">📅 15:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوستان استرستون برا کنکور رو درک نمیکنم
کنکور فقط قراره انتخاب کنه یه بی سواد بیکار باشید یا یه با سواد بیکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84354" target="_blank">📅 14:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VbWl5ogXqfPY80KWqGgsIYhhHXZPPVFrio16dbY1OGO_3R6c5DL6Z7yQjNR08k2a7fPTdqrl9SfUX0bg4TvJJ14g0QnythK6RZuREjyKTr-hHmV6SIZmujwWXQd2jWVZQeunTfEDTqBVa1WBAs3nawEBuoC65Le374NqWNqllv5dx0MshkSlixT0AQxqYf9h7jN_KEQSK5z98LlKKw4ekHBkvcWl8X-OHAWGdamS4RKN1yLyg7vnA6eAouf2_OzgLrWFTBD7IrOIXXjx84AN3inPqMgymFK4ohX7WxYud9mvg1icQnQV54EJ4pRD7NIg-_iy8ZPNsz_ppcuFrci1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنشنال یه گزارش جنجالی منتشر کرده که میگه یه جاسوس موساد به اسم «مهدی نادری جهرمی» وارد دانشگاه امام صادق میشه.
بعد از یه مدت وارد سیستم حکومت میشه و انقد خودشو حامی حکومت نشون میده که بهش اعتماد میکنن و نفوذش بیشتر میشه.
انقد توی فسادهای حکومت و مالی دست پیدا می‌کنه که دیگه از موساد پول نمی‌گرفته و حتی بهشون کمک مالی هم می‌کرده!
حتی توی یه مورد به یکی از نمایندگان مجلس ۳۰۰ سکه رشوه داده!
طرف توی انفجار کارخونه موشکی ملارد، شنود فرمانده‌ های سپاه و نابودی برنامه‌ هسته‌ای دست داشته و در نهایت از ایران فرار کرده‌.
و یکی از مدیران اصلی برنامه معروف هفت هشتاد بوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84353" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هروقت میرم اینستا میفهمم نسل چهاری ها بیشتر استعدادشون تو بلاگری بوده، شانسی رپر شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84352" target="_blank">📅 12:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیگا ها و فلسطین فن ها فرانسه رو دارن بگا میدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84351" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7ucWmGcOA2TLTiy5h7heGtSpejHt3n9U5Sf7a-9oUAE9InVAP5Fa5m19xqkaKIjt-5OwNQ_JH8PQ3zEYAw29QGb0Cdr7eSgQ-LfF-LOCf0m56IDpXFuW_m6DOa6LW4GeaSas6xcQ2arAzn5b3L-JNLA_a4x1eMsRensGmrXrHw0ZAifxQRh0hZUDbXF1PxesWF4_XK6HMldN1gE1yd9m4S-9BnBmOa5DbJA3iSnumwSBMZHbztCLTB9xpbqJuWQKln65J8DtrWKt5q22gwDzHymm8C1G28qrp9_ys901nQthXSJvut8JDiH0pC8hKnm20GZAM4NhEOJdqmA6jfagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا کیرم تو این اکسپلور
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84350" target="_blank">📅 09:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=TpkX6csqbr7kowcuTeZYxZblprewlBuxRAfXIcU6mH83BtkmWzujkRqj2dLYqvFF7hIAEZFyF-RpoDF8Ew1_WREpHUjRyhvO_uryiYowS3-ld1IzhtDnvXNQeFa_TK88DsHOfNoZcd1nN-dWpEXvnJ5GmoKMDquVrfImcXUt43Z63BI9xao24Q3aR-UhRLEZ9qvHHOOoV8tW97krQhJC361v2xSrxe-8vyBjPGTbGyHVBnHRYPYQEDivPAnlJ87UgtFNMevW8w83Woefofs-dAy87_R6SoGRBT_XhqmNmaRWBouApEhc9lZN23_iOOuthbWJRAVG-X0hcxO03A5vQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=TpkX6csqbr7kowcuTeZYxZblprewlBuxRAfXIcU6mH83BtkmWzujkRqj2dLYqvFF7hIAEZFyF-RpoDF8Ew1_WREpHUjRyhvO_uryiYowS3-ld1IzhtDnvXNQeFa_TK88DsHOfNoZcd1nN-dWpEXvnJ5GmoKMDquVrfImcXUt43Z63BI9xao24Q3aR-UhRLEZ9qvHHOOoV8tW97krQhJC361v2xSrxe-8vyBjPGTbGyHVBnHRYPYQEDivPAnlJ87UgtFNMevW8w83Woefofs-dAy87_R6SoGRBT_XhqmNmaRWBouApEhc9lZN23_iOOuthbWJRAVG-X0hcxO03A5vQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش هایی از آموزشای جنگیری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84349" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84346">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=W7YDfWxl1QQ-b8TUDVtWQnI7pVBIP6U-_VsNN9I9ZjUKA11fyuRU0WUftixkQ_ES-zn1U3Gn2ijs4nhqNBSRD5po0905fgdBdSMwlDSNXeT_y-bt8XYx8LLs42DqE7MrLqqRdwMGaJZkN0leMe9FsuisrP_3WHGgvReWqBLW07xxAf0wwsmZaRczA3lXXMYeI9KyBy3pcCLn-_mjRty4x0LbQVnBlJP3_QSOcngZrSu4r8OJRWhjL9_OiANTIxOPkmEFqbZIF9nhRoVFoji5InevprvqBvT7_fC2ov2GFtThkhXiRWeKta_b5hVn6H9e18ENIVgJ85yiFCBaX6S96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=W7YDfWxl1QQ-b8TUDVtWQnI7pVBIP6U-_VsNN9I9ZjUKA11fyuRU0WUftixkQ_ES-zn1U3Gn2ijs4nhqNBSRD5po0905fgdBdSMwlDSNXeT_y-bt8XYx8LLs42DqE7MrLqqRdwMGaJZkN0leMe9FsuisrP_3WHGgvReWqBLW07xxAf0wwsmZaRczA3lXXMYeI9KyBy3pcCLn-_mjRty4x0LbQVnBlJP3_QSOcngZrSu4r8OJRWhjL9_OiANTIxOPkmEFqbZIF9nhRoVFoji5InevprvqBvT7_fC2ov2GFtThkhXiRWeKta_b5hVn6H9e18ENIVgJ85yiFCBaX6S96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز خوش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84346" target="_blank">📅 08:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r362JzawRQiYb9ci6l_0qMfNiRqO4e7jfFfrqB9VBSsYgOv5OghCdUK2C4wDymmfQmD-XD98KPBqj2LcwoJeC6QUCj09F94j0V2UPFiLNrokeU3-ha58SZSQQeLJmELjvZ6nf7VznSY4PE95KMDi334lfRmqsBjaI2c5xID8yz_F38_B3C1z7uBniCXoqxCT3KQO2dM3DM3XPfQ--3zQ6sJ03rbVYfVGRrpwb7coPDgcWtFZkuJj3mO_k64GVsQrZ5dz77oV_nZ__z3_HIGlOMiiT-4HV5orzTEwOam5vmachzEk-M3M_nlNPbPO_JQ05kwTugE5W2wptlb7Eocl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84345" target="_blank">📅 01:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84344">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF36AfSplYAqeThYuFv1P_aZ3sDrcmEStZHxZX00MNxZI_m11zVMMi26WDgCTwizFIH7xbtklk0ZnY3kLj2zXK7_c4QLHRAMobJdvDChZt2RY05OfjGZExZbkrf5pt0W1U9jA3h4AUaD1izgB_KJu_oXG2fj6SQOFjGQsDD8rz_xRUjZbRgOiVJfvrDj1fHVtulIR5zqQlIIaOoUy52dC1VKnHIMUO5GU5nMdFp777inL_4GMRaiANXo5A8EiZ449CftCQL5lr3QnjQ4QnmaNsxNkFI4LgELBBgmX2CsEacdgYF6zdIcbypkQDmGiDgpH7uSmKpZDZcfRrOepxu6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Batman: Iran knight
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84344" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84343">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=CDdPpBwPVf9LZw8WYd5xCEOgqFHX5BTCrQ8zj3LxsoWyROHiBHDHUfx-gX8hNTh9fhaZYRkJyAARw66vSdRRcjtCCSjP3L2vFRWSXQwopzPkngvmh_pEQqXrPd8DrDrXDfoHLdS7dyrma13hn9sX6Zc5H5dYlUaScrxPnBHiWV3CvV0ud8vtyjmpKPhUA7Vp8haTb3PxTQIUof_vmVozqgSnvcwPz1eR0GC1Dn3xn_C5y9jfqmibnG1n_hKlEWA2iAdrfo57YOK3-vc4G-2W-ZoGo0Y8znob64r50i1E0hny03rAWiKk6yd3nc_LR1G-1nAGtC8bvIn5bkWvkr8kYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=CDdPpBwPVf9LZw8WYd5xCEOgqFHX5BTCrQ8zj3LxsoWyROHiBHDHUfx-gX8hNTh9fhaZYRkJyAARw66vSdRRcjtCCSjP3L2vFRWSXQwopzPkngvmh_pEQqXrPd8DrDrXDfoHLdS7dyrma13hn9sX6Zc5H5dYlUaScrxPnBHiWV3CvV0ud8vtyjmpKPhUA7Vp8haTb3PxTQIUof_vmVozqgSnvcwPz1eR0GC1Dn3xn_C5y9jfqmibnG1n_hKlEWA2iAdrfo57YOK3-vc4G-2W-ZoGo0Y8znob64r50i1E0hny03rAWiKk6yd3nc_LR1G-1nAGtC8bvIn5bkWvkr8kYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کمتر دیده شده از رپرای رپفارسی که ریلز با مضمون پول رپه منتشر میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84343" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84342">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgBMHvAaOmYNP5nSOfmxa7o7RevZWVyCFeilhyq5Pk5ACGm2R6eWPfqeu-VJGMC2Yk99y6KilVAdKGgi-rOImoTLQc_x5fAmVcNGNWGETZTAtl1-rwoJSKQhfcsXoRVK-c65Nw3saJeq30KUKjrtXjdmb3C6wqkHBoNdHgEvWWueqUCwHy7PHWevFLUUA6aNUjeWpYlM7Zkqf1p-7J_qE9qtNoSYAr84tgDzAhGgwSaCCRE6VCUymtuIwDXzLfmqMXWOx2nLFOkzRSdrycMO-S5HpWn0EAyLAJR31Fx67_F27Is9sR73IwXcEmmwWyuQUV57jf81f0LUyXXhXa15yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
جهانی شدیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84342" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84341">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چه عجب آقا دانیال تصمیم گرفت بعد ۵ سال یه موزیک خوب بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84341" target="_blank">📅 20:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84340">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84340" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84339">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ufx-lA3U_w2_jnB-eNejj9WSOm4WbmIqpB7_st18CXbHbmz1O7DekO121NWIBDGybtqmf0Vd-wI-d6OiTuSwK2ps549Yxbx336ndAbgSfTjE1uQr5GpHCDJUiPYpNvV9RBTVxCDyEaqvxV8d6MGRQBfbo-fSG6NSjox4pyxvlcZentozVLAchxYTcyuRswGZdryzbB4Ytq2Vkl59wn6zB9BxhAFvM6J-RVQE2s30DTu8wGlC7azcVgWeKxVGouxBfRjs67INWapVukf_U3_1l7AuUIX7ida0LxZ7Ej0KHaioK-E9bAKDEpHygLe-X-8rPVlmIzcRqWGCGkjSuZAW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84339" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84337">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg8aEHw5VcruLRqLfPWmQdD2Z6lw1jtQ0hsJSMPZbqXnWSWp-kGqu02inyhEIrxnodh7DsRhPhd63yhMIAxElYDnW1o9hrhdegh65_TVwYvnDR36rz4XjDojZGdIQ3jpftgJ77IhNyoOQXZo1o2LugHGZ8nwVC8rWknv18qnRkC6l6Skgk3QtuIS1y9HRmR3gSgWtNaAa-YuQBdhT005azffN7r0qfideqke6sW4YcjTs-Nkm387as6LIOpkbQ3SRXX9Zt4CsmH-WWh3LDZfidKk8_NIS_7zDqQXj9z_YygRXEYLX-muOLjleFI_p06mzX80pIYeCzS48kGMsuuEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=p1H8zNseYil4hVXB3Cw0Zd21beCqn6BmLP1jh-AF9A054FmXew144C8s1FB5vR_KqFMYSY2jyeqQ6sriDNHKL4me5gRM1y00UGZcKNEZeVmiPCg0PizZNcPqKNFbMrlbHFqgrudsn4cA9uj4hXyuNhAr35R4bn-Op8NJpJI3D4uJMlB4_MlfcCy5GffWrNovuhjYsx1zv-MFOY4zTd2uh-9_JQadQnm0SSgycmhQlJMC8Ro_grhOEvvIwrQlyeUpxHS0OZL8eZpPP4dSw6qhUtFct_dxV6FSoNrj-EkLJRvUMKta9nEx7hrnGiyTTI8B3gW0oGIglTFfp6TLL5uqWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=p1H8zNseYil4hVXB3Cw0Zd21beCqn6BmLP1jh-AF9A054FmXew144C8s1FB5vR_KqFMYSY2jyeqQ6sriDNHKL4me5gRM1y00UGZcKNEZeVmiPCg0PizZNcPqKNFbMrlbHFqgrudsn4cA9uj4hXyuNhAr35R4bn-Op8NJpJI3D4uJMlB4_MlfcCy5GffWrNovuhjYsx1zv-MFOY4zTd2uh-9_JQadQnm0SSgycmhQlJMC8Ro_grhOEvvIwrQlyeUpxHS0OZL8eZpPP4dSw6qhUtFct_dxV6FSoNrj-EkLJRvUMKta9nEx7hrnGiyTTI8B3gW0oGIglTFfp6TLL5uqWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها یاسو دیدید چقد متواضع و خاکیه؟
یاس:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84337" target="_blank">📅 20:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84336">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26448031d.mp4?token=M0sqTYNQR4TqFgj173TO_UYwdNUEiaabkX9kZy1hhekZRtxoIFKLinAbcS1wsPQQWryKGRhuDsMT8edtDzvAjKMQFTK5BfCErefsMBed5GXnAiDlOZTwb5IhK6sWnHEMgTUeAGPvve6uKEFk1EqdIDuKe4M3jMaNB4TGydmRotWlsLrp5iDba4ZuW1_k5MXKn6sAxHBfcEqMYY5To1F_CBIv7_FiKVicvzajOE8otfjpAHRySdnQovRnfJvnGshJ7v9zdzxNDZq6nsZ4o_Hujtz9KLSsklwxMKB2GiwfEtA838ahaMLRsJvmQyjds_m--DJohWsiFWb1FtsiK2xEzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26448031d.mp4?token=M0sqTYNQR4TqFgj173TO_UYwdNUEiaabkX9kZy1hhekZRtxoIFKLinAbcS1wsPQQWryKGRhuDsMT8edtDzvAjKMQFTK5BfCErefsMBed5GXnAiDlOZTwb5IhK6sWnHEMgTUeAGPvve6uKEFk1EqdIDuKe4M3jMaNB4TGydmRotWlsLrp5iDba4ZuW1_k5MXKn6sAxHBfcEqMYY5To1F_CBIv7_FiKVicvzajOE8otfjpAHRySdnQovRnfJvnGshJ7v9zdzxNDZq6nsZ4o_Hujtz9KLSsklwxMKB2GiwfEtA838ahaMLRsJvmQyjds_m--DJohWsiFWb1FtsiK2xEzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برام سواله یمنی ها دنبال چی میگردن که با اسلحه ها کاری ندارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84336" target="_blank">📅 19:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84332">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سلطان حمید رسایی را آزاد کنید حمید رسایی را آزاد کنید رسایی را آزاد کنید را آزاد کنید آزاد کنید کنید  آزاد کنید را آزاد کنید رسایی را آزاد کنید حمید رسایی را آزاد کنید سلطان حمید رسایی را آزاد کنید  #سلطان_آزاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84332" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فان ژوله غیر فان ترین شوی فانیه که تو زندگیم دیدم</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84331" target="_blank">📅 19:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPYRleZnlgbgpOqeftAzAerW3a05thzf0OU7xyths61bXpUWF7Y5-0wmzWngMTg_iorV18YrFJ2l3PVT6GfwqhCBDLAKyTfn32yRvAe8Dc8Flfr3EoGqeygBWwUXg3gYW9nwfWFt35qD9L_4JB7QmSTvyexXweEh62v45R9yLhho9f-xtafdtHXe0SttKW7bakmuwpGVIM-k73-ydWfHv-PSdnMJ1cLR7ZP2M-JmY4zVvBhXahkj9dG5gPsUPXhCwBwSppLLIfnKW0Zb2QcmKi8rKDLQ1MDCIS7N2er0AZ3vKSEezvvj6P7lBZ8UvRkk3KbQsJI2RaSIyeulfs_gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران حتی تو معروف کردن کصشراشم پسرفت کرده پسر، از این رسیدیم به امیرمحمد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84330" target="_blank">📅 19:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84328">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVeoDLYN5_nZFqDYxmO3lHZFMSBWjzFX6I4tOEuAxqKifnd6pGQaSzN_qA9I9jGYmMHZDakpuu1558_AvrW46KzHI-T1kn1R3UrqOt6ME8yCLutS_lgpJd5pSGOpK0MK-lp_7JQpeKQEMUR43a1hg922N_aIyUGTJDaqe69ihG2fyPsducjIECuAGosL61Vf3AlIrKDgZDhOFD5YBrGbSCdRsDFbJULTQCS2DHgNCFEthU_jTCdeitwLxNM0sp5WUjl01jL0Ynpv7BxIfMbo69d6lUeekfKgRB0KyZlHSOt8ZeuRIY7_z-GA44YOLnUzP9hEybTLSZIFbvGApuHc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWLdDGZ5UazsnM0s0e-ed9VHvtA57YqQWN3dsHNRXKzcWVY1Z1U-iBJfjjEHBuIS3TWRWmsP0KtlnGx-1OcKzu9DiZioyczPzoOnY8qWJQYpQaQU2Cy3z0XmoUPhGBLA83yaBenozT9oWfnnkVE-ygHXMT09V5RYD4IUeFqHNpSvjroIMk0JFXM9wuIqwOTKcmbOaN0xpJe8dTOHZp98l-eua1PgR4q8b616Se27SEhSCxWYXmHwupqf2_3u7drGXWY0aWcDDBuqyqRqbjXV-KH2Vn-T1SIcR2Ra4qcsC4J_MEnU5IxVlaNnUtN2cs9gBFlNa8FSYK4QyxtFe8EH8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترند جدید اینستا اینطوریه که دخترا دارن کامنتای کلیشه ای و کصشر پسرا زیر پستاشونو متقابلاً برمیگردونن به پسرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84328" target="_blank">📅 18:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چرسی: شایع اون تایم برنامه گنگ گوه میخورد که من اطلاع نداشتم برنامه قراره از فیلمو پخش بشه، اشتباه کردیم ولی همه اطلاع داشتیم که ضیا داره با اون پلتفرم حرف میزنه که از اونجا پخش کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84326" target="_blank">📅 17:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84325">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=lKHXR0ph0hPs8111bT6FhkeeqniPbfFJlYwzCFej0g8eOh2eEpvC21dQvBMI_EKZLt8Z6w54T9GQc2PXNK5f-zp2pPQjHcS0UvavCRK4fendewnyRHEPy8qzmsOs0Vke3qC6Kz_1vbU8LlOgS9PbCMyJfvkx0cJA5OV50z4injMAXp1gZGfCsrbVC6pXy6zzIlLmojNBUMfioTpJynzJQelsS9QncMmVVt8iQ5hT1Gdk50u0W-82Py-iiqp98Cw4oWxMOQRgA1pUf1_lNuxu5wFeF-_7OooXy6hRaNnhQkDYGLl_M8fSdeeeGkZYTgtvVZcvZKDmJY2jfcteAhaf9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=lKHXR0ph0hPs8111bT6FhkeeqniPbfFJlYwzCFej0g8eOh2eEpvC21dQvBMI_EKZLt8Z6w54T9GQc2PXNK5f-zp2pPQjHcS0UvavCRK4fendewnyRHEPy8qzmsOs0Vke3qC6Kz_1vbU8LlOgS9PbCMyJfvkx0cJA5OV50z4injMAXp1gZGfCsrbVC6pXy6zzIlLmojNBUMfioTpJynzJQelsS9QncMmVVt8iQ5hT1Gdk50u0W-82Py-iiqp98Cw4oWxMOQRgA1pUf1_lNuxu5wFeF-_7OooXy6hRaNnhQkDYGLl_M8fSdeeeGkZYTgtvVZcvZKDmJY2jfcteAhaf9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی خدا لعنتت گنه بیماریت واگیر دار بود فک کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84325" target="_blank">📅 17:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یعنی این گیر دادنای امیرحسین قیاسی به مهموناش برا ازدواج کردن اتفاقیه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84324" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دلار 260.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84323" target="_blank">📅 15:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84322">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84322" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84321">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شماهم جدیدا ترجیح میدید یه سریال کصشر و آبکی ببینید که صرفا زمان بگذره و دیگه دلتون نمیخواد سریال های طولانی و با محتوا ببینید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84321" target="_blank">📅 14:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84320">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUOwKLkrxUv2N0WRydaBtfMSN-dUk84ED1zyGElAXYpEi68GWpEE4C14yPhzJhR42mfZlb0gY9AlHSCKKSxOC9BaQQKX8T4D3e3NJ0a17Lu-K0ZiOK7vs8L18F1NrPe7Q2Pt6K24JO037W6io9Su8bY--SlXqqalGgqnjvVLCyRlq9K3m60TfvGutlS07MOKH7iDM25H6ATG6cAIQWSkeA_J82mQLoRHCaskTZ8gGUxKr-COKsxueJwYrmqHfjC1XsMpBYqkMoCM7rnzg8bJ6b4I6TvP1Lgm2zv_Nzcpx-zFLtgF0uKeu-yNgFTZutABHCAhKD7wn8Lt6likChcMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا بعد این که کریر همو گاییدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84320" target="_blank">📅 13:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4_HJLO-hX77owKLLpDjMQZ1tBJFz00fIWijOuY4vw52fVT11wJFu6o6ZKjeZ9WgF0NHB_UQ9qvCvUfUwbE1rjIeUVCviLBFqfuvJxSs9azoa6f0w7L2sFr5FPxY3NEj0M3n3O1ZI4GcpfiZ_UBJhKEtiYqfA5b6xifL5YOYgKnGEd6kgZFjugjTCZf23BkZnDikA0lkITTVrpG88aUQf5S2mDemMGy76Hnr2Mprix-wDddAK6_uorESxzWSPoReDz1AoF22oN94HeT80o_H_7ywEcxupoxz2ru8ZG7Y80ik8wyS4ArMG4qPi8842081LJ6herEjSUE327JQLNXA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداروشکر داره عادی سازی میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84318" target="_blank">📅 13:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=vD_su60Tev5vCu3NkzCL2AMpOQQgd6448OJIhNc2iwcQLi82UxJbnV_subaXs0-iFEsvQXM_Cyio46sNl5k3CI53kqYF60NM8hOhwzyHQeExuCU3wU3HIjzvBJgAecITjLe5b-gh8m6M_QG-ejzxf7Fpy9X2YCmt8S8mGZEE1MFwWH53AqUP9P3pozDo9R5Zm_JJpTe9HVtfo_ryON6twPdelX-nioSDqLjTkJOxARBLl4AK368R-jyJ7YMW07na6UE10_2hJ7r6-HUgMPxOuSEq0V7k7H_6OQKYUfJEHVo_Wf0dtgdgEJ0NhLflXjAJqo4cXLbmVnrGUtAOoIMq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=vD_su60Tev5vCu3NkzCL2AMpOQQgd6448OJIhNc2iwcQLi82UxJbnV_subaXs0-iFEsvQXM_Cyio46sNl5k3CI53kqYF60NM8hOhwzyHQeExuCU3wU3HIjzvBJgAecITjLe5b-gh8m6M_QG-ejzxf7Fpy9X2YCmt8S8mGZEE1MFwWH53AqUP9P3pozDo9R5Zm_JJpTe9HVtfo_ryON6twPdelX-nioSDqLjTkJOxARBLl4AK368R-jyJ7YMW07na6UE10_2hJ7r6-HUgMPxOuSEq0V7k7H_6OQKYUfJEHVo_Wf0dtgdgEJ0NhLflXjAJqo4cXLbmVnrGUtAOoIMq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر ایرانی وقتی میره رو کار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84317" target="_blank">📅 13:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=ULOSEKbRKFiU9KgXwVQCVivwKvYKoOBs4TvjwFHM31vxyuSVXU6ej5Si3Gfg_9ehS6EIco9zIIuebW23ntPW648RIv6UbxDOgjho6nRPadAG2l-sbD8B8dlcooacWiltlF7pCjLf4K-SO7TO_8oS6KgmD6RH84B6EFhQ8-nHJoTUSH5kCKwDFqDfXac0ZBROYi-CMwOjyrrhJ-h9qbYSj0oGawK9ckOdRAkbghvkEGQ089D90AeHJ8l_S5hinZtkrcP6jDOj9OmZJz4rSBHWbBJRqcMcirHPMrMqIG9JO4bjQJx1C2CHOuh_NSjF_enmTDMJ4lpfJ-Kq6oyTi0mrfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=ULOSEKbRKFiU9KgXwVQCVivwKvYKoOBs4TvjwFHM31vxyuSVXU6ej5Si3Gfg_9ehS6EIco9zIIuebW23ntPW648RIv6UbxDOgjho6nRPadAG2l-sbD8B8dlcooacWiltlF7pCjLf4K-SO7TO_8oS6KgmD6RH84B6EFhQ8-nHJoTUSH5kCKwDFqDfXac0ZBROYi-CMwOjyrrhJ-h9qbYSj0oGawK9ckOdRAkbghvkEGQ089D90AeHJ8l_S5hinZtkrcP6jDOj9OmZJz4rSBHWbBJRqcMcirHPMrMqIG9JO4bjQJx1C2CHOuh_NSjF_enmTDMJ4lpfJ-Kq6oyTi0mrfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقریبا هروز تو شهر های مرزی درگیری مسلحانه شکل میگیره و سپاه اینطوری یه خونه تیمی رو با rpg ترکوند.
امروز تو درگیری ها حداقل ۵ نیروی قدس-فاطمیون کشته شدن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84316" target="_blank">📅 12:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e0832652.mp4?token=ENdxYg4Fsua5g6xxABxD83dW44tYXcc6XBIX8miH3huKo5HZsYiYhfyAQFOoHAq7P32FnjGIM4JhXjC_dilHqAOTxyhzTkmDG5718FW0oArpahsV-mNTwE6ZgRJ3XKek86nEvRtNIEOZ_s1cpPHxYiDzUX4-CANOF8dI3EyKLVRMeVhMzXT-N5sfG1rAhoPoOsRaGBwp_ag6WsSMJPEhDkyVS8GyQyLi0jfILOPrhwzu0LSUxJGMT3H-VZr7lFx0UN9Ad4Bz-EDHr8-vNeGZEXnGdI4yitpAR53c4RxHjnKoValdi0vC8bmECaWrMqTLumrw7kFiRA3juiJhia1JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e0832652.mp4?token=ENdxYg4Fsua5g6xxABxD83dW44tYXcc6XBIX8miH3huKo5HZsYiYhfyAQFOoHAq7P32FnjGIM4JhXjC_dilHqAOTxyhzTkmDG5718FW0oArpahsV-mNTwE6ZgRJ3XKek86nEvRtNIEOZ_s1cpPHxYiDzUX4-CANOF8dI3EyKLVRMeVhMzXT-N5sfG1rAhoPoOsRaGBwp_ag6WsSMJPEhDkyVS8GyQyLi0jfILOPrhwzu0LSUxJGMT3H-VZr7lFx0UN9Ad4Bz-EDHr8-vNeGZEXnGdI4yitpAR53c4RxHjnKoValdi0vC8bmECaWrMqTLumrw7kFiRA3juiJhia1JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پورعلی : مجتبی خامنه ای شبا به صورت ناشناس تو تجمعات شرکت میکنه. دوشب قبل نیم ساعت اینجا بود.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84315" target="_blank">📅 11:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=FDCY3_IK9oye05ntZgh6vfSeXSDzAteHSbQpAVTwFiAOqWKbPYcXTp8Co5x0QJ49WlRMMGKVMxBGkrVQWjzE0bQs1OypUZZZ5aRywBGJk2uQEMdbqRHaHl2hD_HPSJj9eoTL6wpoMHwMmSBxQfiDNGhoVxHiMI7M9z1bsVQtNsteH4S4nkqw8yzkn4ioB7iZ3N5_kvheJrMEazGiJY4Nb4rnMBQeEuYjG8_HSjgiLs547WHkhob4iPX_Ezvur_DvWgMHgNYb09KIRnM_xGZpCl0OYH_tX-2tioVmJZmMtwAUrCuJEyhoBxktief8j9Q5gqO1moxaSYoqmwipj-RRCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=FDCY3_IK9oye05ntZgh6vfSeXSDzAteHSbQpAVTwFiAOqWKbPYcXTp8Co5x0QJ49WlRMMGKVMxBGkrVQWjzE0bQs1OypUZZZ5aRywBGJk2uQEMdbqRHaHl2hD_HPSJj9eoTL6wpoMHwMmSBxQfiDNGhoVxHiMI7M9z1bsVQtNsteH4S4nkqw8yzkn4ioB7iZ3N5_kvheJrMEazGiJY4Nb4rnMBQeEuYjG8_HSjgiLs547WHkhob4iPX_Ezvur_DvWgMHgNYb09KIRnM_xGZpCl0OYH_tX-2tioVmJZmMtwAUrCuJEyhoBxktief8j9Q5gqO1moxaSYoqmwipj-RRCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84314" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=VQNATp8xf-SNYr5QbxJEMVi02hJu8xTIV0VYTQK4HlDEud5XZJMbEKcmoVtrlyXBuuqh_h7wi6-kOqhmyFiu2tM6t-YO8_9Tu3nrbER0Bp2jRbNCJW0FBQsFKvFhOMdgaHrBVJPgLrrW_blOBlaU1j1R_iOriED6TGSWJdWhGb2SEVHaSGYKhFoK5_gGB_USBU5yy2RmAaG7iq9O0bg3VjTQlgGqDEiqscW7PMn8YIbLcMQppnq0GbqMx0fDZu03adNh-dO7oSslAWsoB3VmfoADHMKNPfC2t8-UQtDSJ0WQwnA2ckdDbpf_rqtalf9ak18oQABrtjsDti0A7WGf5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=VQNATp8xf-SNYr5QbxJEMVi02hJu8xTIV0VYTQK4HlDEud5XZJMbEKcmoVtrlyXBuuqh_h7wi6-kOqhmyFiu2tM6t-YO8_9Tu3nrbER0Bp2jRbNCJW0FBQsFKvFhOMdgaHrBVJPgLrrW_blOBlaU1j1R_iOriED6TGSWJdWhGb2SEVHaSGYKhFoK5_gGB_USBU5yy2RmAaG7iq9O0bg3VjTQlgGqDEiqscW7PMn8YIbLcMQppnq0GbqMx0fDZu03adNh-dO7oSslAWsoB3VmfoADHMKNPfC2t8-UQtDSJ0WQwnA2ckdDbpf_rqtalf9ak18oQABrtjsDti0A7WGf5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رپرای جدید تا حالا واسه زلزله های مخرب تاریخ مملکت خوندن؟ نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84311" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=G3XwcogXYSY9BhvY_rieuAXjOiNe5jHS1CxXbE_HZbtUh0rAMAJ2ZFM0lrn8wCIgAoUmXqysG37IdoyFdodUnMeKy2FJeRObz4LbLE9jGGB_sIHucFoYbKwtUcKSzE6ry-md2-uxF2o6G0dZeFBPz1ALCf_dwTh1mVNJYH-oEblnMqrLoVgSm7PjRk7gsDAUy3AMmSDdnss7RUIR1db517IpwzOGJHwp3MZ_7j_Bt4XwMcRGYzN5S0q58ykaEpiBSzLndlVeR403ULF6ENY8pXVrelyDMGjB_KJHdGEPPpwXoeYrIjJMl5pqMSta92n5avk_zSoc2_QfWc0oCr3ExiijArWIuQZkS9fDS7rbJ7ua-OtBxXTXQ7Py5Yf1qLnYl2mhWVEeH_Ez8ykd6ZsPnG_-pTXpAE6HqbVe2KN_t3u6RlJFuVAjPboa9a96rJS8G9SVQxoy4bWYzp46h1wo7yDj1Ro4aEkbjikvsnAmbHpSODmTUL_yHCbg4BSdmHS-alnuR90NHGu2hRRYxJbudtEUP10jjFDRPOrK3dUnwZHgQKp4_krNLn5tKvBojfTEIriSErcnVhzOp9EHKIO2F_aXNVmfbNYAyedNjTHv0CfY6yEXXXsUdK6wwI1k0P9ecJL64eh7kfhQlRdvshdvqZ9YOY7TkbCbPQO0WCsrV5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=G3XwcogXYSY9BhvY_rieuAXjOiNe5jHS1CxXbE_HZbtUh0rAMAJ2ZFM0lrn8wCIgAoUmXqysG37IdoyFdodUnMeKy2FJeRObz4LbLE9jGGB_sIHucFoYbKwtUcKSzE6ry-md2-uxF2o6G0dZeFBPz1ALCf_dwTh1mVNJYH-oEblnMqrLoVgSm7PjRk7gsDAUy3AMmSDdnss7RUIR1db517IpwzOGJHwp3MZ_7j_Bt4XwMcRGYzN5S0q58ykaEpiBSzLndlVeR403ULF6ENY8pXVrelyDMGjB_KJHdGEPPpwXoeYrIjJMl5pqMSta92n5avk_zSoc2_QfWc0oCr3ExiijArWIuQZkS9fDS7rbJ7ua-OtBxXTXQ7Py5Yf1qLnYl2mhWVEeH_Ez8ykd6ZsPnG_-pTXpAE6HqbVe2KN_t3u6RlJFuVAjPboa9a96rJS8G9SVQxoy4bWYzp46h1wo7yDj1Ro4aEkbjikvsnAmbHpSODmTUL_yHCbg4BSdmHS-alnuR90NHGu2hRRYxJbudtEUP10jjFDRPOrK3dUnwZHgQKp4_krNLn5tKvBojfTEIriSErcnVhzOp9EHKIO2F_aXNVmfbNYAyedNjTHv0CfY6yEXXXsUdK6wwI1k0P9ecJL64eh7kfhQlRdvshdvqZ9YOY7TkbCbPQO0WCsrV5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا لحظه آخر منتظر بودم بزنن زیر خنده بگن جدی این کصشرا رو میپوشید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84310" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337199248a.mp4?token=gNby23B8e9z5kBBcv_FO7-Cz1hu5LcMB-1IpPCekO2WLSBDL2x71xN4qhZZAMC5I7Uh2usH3lQsBclnPVamYY9j8AxLJhp08odVCOqD8JM_T0Uiji5bE0mG94wKOH0mEaVZlwcTw5vS2HSZCHVXV083uqWIpe2lU6JMXjm9YEBpFobcb6YCY5-ARtuMtNeHdC-t1AtqbIfOq4WE0jdG_iTXlynPevZr7NphyMc0XASlAsDDIADx-qHq2lGwo-SMXi6Cef_4LlM_zK_YmuxtnhhQIkXt8yQlJls3vEuZv2MlC3l-52oeJqJMWNCfgP7iiuTpK4ektfdzhMbDqPmqPsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337199248a.mp4?token=gNby23B8e9z5kBBcv_FO7-Cz1hu5LcMB-1IpPCekO2WLSBDL2x71xN4qhZZAMC5I7Uh2usH3lQsBclnPVamYY9j8AxLJhp08odVCOqD8JM_T0Uiji5bE0mG94wKOH0mEaVZlwcTw5vS2HSZCHVXV083uqWIpe2lU6JMXjm9YEBpFobcb6YCY5-ARtuMtNeHdC-t1AtqbIfOq4WE0jdG_iTXlynPevZr7NphyMc0XASlAsDDIADx-qHq2lGwo-SMXi6Cef_4LlM_zK_YmuxtnhhQIkXt8yQlJls3vEuZv2MlC3l-52oeJqJMWNCfgP7iiuTpK4ektfdzhMbDqPmqPsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمدی شاخر : (شاهکار+فاخر)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84309" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=TKbvVTiwae_47RT79FOaiDIuKASIIeAxORD8BzAAOqrk4r8TS_srIqnKzQGbJVi4swHfcwqD8ClpxDyZCakP7BvodqzUPq7pd6RcI2eYtFO4gr6HcC4ge-NuHoESEoKTqvyzClMQ1rjwdAsnDUnvdbFKjzV2T-PcPsQeLBzU1XfzfMWKrHAHG-kuxTXtF5uZvp2aVKKOg4tB5MSEwrJCcce7BEwswnDePkaTf93znx8HHtH4BoYGIRrpjkT6yaWNNSouourssRIS2F7u_Zngaraiiq8SBkN4irnKqx7zDz6O74UioGDWEVtb9Ui8rBpo_pm_t-n_GG0Z9p4aFh7Sow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=TKbvVTiwae_47RT79FOaiDIuKASIIeAxORD8BzAAOqrk4r8TS_srIqnKzQGbJVi4swHfcwqD8ClpxDyZCakP7BvodqzUPq7pd6RcI2eYtFO4gr6HcC4ge-NuHoESEoKTqvyzClMQ1rjwdAsnDUnvdbFKjzV2T-PcPsQeLBzU1XfzfMWKrHAHG-kuxTXtF5uZvp2aVKKOg4tB5MSEwrJCcce7BEwswnDePkaTf93znx8HHtH4BoYGIRrpjkT6yaWNNSouourssRIS2F7u_Zngaraiiq8SBkN4irnKqx7zDz6O74UioGDWEVtb9Ui8rBpo_pm_t-n_GG0Z9p4aFh7Sow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84306" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=Sj0j50h_V9o8ikoLfybEhELh5h1f5bhw9JOKG7ybXIAz8jj_R7z5TRBbmhvibtKyaqV-VsOi9dUdfMoanub0COFBhyxBQCcKiYNF18X4qfOF8WPN0gRTJppDm97E5zo8fqbpXZjvShmGOKh2IrNoPveD5oY0od0CO4AuJqGb26tplmgQPWrDSa85xA-ZpxjXQ5MIhrueCMk5wf5z4N9opbxzcpMOcWW0l5gn6BGvTKqSx8JN_E23A3TdZybcfPINzAN-sgz875aLnUnMlfICm5App2ucybx0Oq_sYXGuIuRlqGnwDAszf3K6b1t68w8G5cpOIEnCJIK_w8_BVfqXUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=Sj0j50h_V9o8ikoLfybEhELh5h1f5bhw9JOKG7ybXIAz8jj_R7z5TRBbmhvibtKyaqV-VsOi9dUdfMoanub0COFBhyxBQCcKiYNF18X4qfOF8WPN0gRTJppDm97E5zo8fqbpXZjvShmGOKh2IrNoPveD5oY0od0CO4AuJqGb26tplmgQPWrDSa85xA-ZpxjXQ5MIhrueCMk5wf5z4N9opbxzcpMOcWW0l5gn6BGvTKqSx8JN_E23A3TdZybcfPINzAN-sgz875aLnUnMlfICm5App2ucybx0Oq_sYXGuIuRlqGnwDAszf3K6b1t68w8G5cpOIEnCJIK_w8_BVfqXUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84305" target="_blank">📅 00:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kabIVSSC_9XyXDbVHKZmYmlHEZzYPYRqKql55-wI4TMbiKksNngW8kZdKSNpbNKHjV5MmF5bUCS9p4QY03HxD0vf81yQpUH2rPCwPa1_EQ6hpzCpn19YJbl2JWhJfIsu4DGeGVxrw76XpapJiCjpWaPumbIF5TKwM-oUdl_IOnpN2KJvetbFBZvY_iqwCkrAjWJNaQOCkMZcm2wpO1_llMZOAYut5jX5cRVWE_V9LTLREX9VzW4od6oCSAWZmYVNNy8jiOHacGboxNbGL_81_Av_SNTe7oOsu8D_rJaMxomFF5-7xzCGRbBUo53QYY4XLzip_PyqQvK1uFygKuCxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا دیدید بدون رونالدو هیچی نیستید؟ رونالدو بود دفاع میکرد دوتا نخورید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84304" target="_blank">📅 00:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دقایقی پیش وزارت خزانه‌داری آمریکا شرکت های ایران‌خودرو، ایران‌خودرو دیزل، سایپا، پارس‌خودرو، زامیاد، هپکو، راه‌آهن ملی ایران و شرکت قطارهای مسافری رجا را در فهرست تحریم های سراسری خود قرار داد و اعلام کرد بیش از 30 درصد درآمد صادراتی ایران را هدف قرار داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84302" target="_blank">📅 22:05 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
