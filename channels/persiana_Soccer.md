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
<img src="https://cdn4.telesco.pe/file/VO2cJssef4P2YPvaPMVzTiAtFQHSriiDGMxFTmSqxnAysmVrTFqLS82a1pREDNLYYqTTU0wwixHQuNdNsj-GqwgIZ5OOSKr4W72I2bDqs_xPQqrt0NwrWBmEQ7wjYiPK6v7GfWjI0cnMPAWJrpdIrPRaMiyLrG3_z-AYfsUdjGszLGAx-esScgEeJYeL_CctM7nCKAlp6aqwFEENC2ufXofmfq32_0I7U66sMjxWWlWD9Jc2BVyX8CtR-JwGISGgQ-t70eDF1eezQ7851htifW2A3FegzVlsjoi4LhYQdPhxXMZcgI0l4Kuk84V7nE4HdvjPe9pAEpv_3BAKnLkLkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 512K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 12:13:28</div>
<hr>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gx_QqqqWiIoBaIP9zlW63Q9KgWxOuOGG1zbo5EtuQabaaH0OfLoZsKx_VcMuloMQs963GLRXOADYMF8cM1wAcxoqeq8StHw61i-fgg8mrZH8SWRYShZJIDLF5gMDscx5FqYzXnjkHguWNdEdqfGAIrHUHtQ6T7S7gNyUoN8oxqkWJU7nIH2PZvpAOt_KCzJN-vpY2j_VP548W8PaG3Hw5u0IYEkjXwTsW4HFQcDs4uSXv2WVYWGh7JwSaR_GHXgCVE0VnX2BuwWDST_9JKoCKduAbf7K9EuqZfiLJzBtt3-K4LpSQalwg_17JdMS3R6cimS_hSGCunrht75ghaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKNdW_F3KqkzTcIo3C1-WM7f62OUNVKjmMFindwGwMRXG_Da2cm2o6Xm7q5-9aXiIUlqRbcFMxTTo1lSDmSjo_EQ_6aqMJ7zWbHqHKOAiZCcT68d7kPiax5ZEAWqtJeDfIoHyuDHppusckEktaT64odi59vDw4oHwpq6JZfqHJWS_zh7O2ffi9JvoKI5tdEXkoM5W06yHdREtu0gW0zwdBt-kpqYL48VigAypLAXsB-SQ9KbfTCDwMJpe-Ntauoh3aC0thbiuJ4gBPwQzhj8MrMR4UIjyMIK7x98aua1-EAXSFar9H-ROS29WKTN0gs7tUyWUE5tdRM65qEVR0PnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6mHlD_svdZJkjH_OHuGoU6DCKql7aqP1PM451Rm2VvyDq0VW2_0Pij2vsdtDF-Hq_HVz5ip45eHSatvzffEkQ9u53ywOVxsPjIQThqFKIjjw-gYnS7WvImC4xND1-x4TgYxwG8yCX7UUVhpLoE0hoabVSdrOv9y8I7Sty7WbyWxf8rSaSFldfFNpG_SuBBkGJDgn6mM-9UBVjEUPYd9XiCoxpqVqQH6RXGldN645FU0lf1hVWduFKqIqWD59lfES-djn-1LN9Qm_8WJ2e9FaRN53YX86EEQWS7ouVA7jPPlraamMC9iLFXZu4OzqDWiIqXmu0iUMLo60bg1CnSixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwI6XqoeL7xi0vk-ZAW687-dWSIRw-2WWjV__ft3hg7anvDhz02JHZQirZsVDV2CgAL47iNU3OTYFodOuyjo7QLju5CjvxffpmXHwkBK7w754dB0yBuzwxfAnATRjUr4qSjHRzgdh_EwjIl5kFiPKZQfG7_RGZpywJS6FB8HRzdtjjY8rBAGUFVJLkLOpdZfH6TM2GqGklTfi1mh7Zq_R5NPYIjsauQj9vxOk8X7nQb0nCpSUBg0nbQcG7HCeP_VgG-7LSbGNb9o2e1KTLnmm1YUNGn2iTu6tZlTey-Nentpdvl96RKuF3nKm5B0qmzuQKNhKjfJ7BjNVdS4JCLamQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZVuuOr7fEuWh-p5WCn4C705BhE5pcz0iAJ_RmR0HK5sgLxgJgBIlw1Lj46Qg_YFAB-2I-_jCxWtvpZMrBDQsXozmMLob9NCL8lAor2K2RVGn-49Is_MQHfm_ynBz3mTpurXbc-LY_hT9CN6eMN55MIUyBBUwnI20GU94Rzq1165dortjoS_dcxgYxJa2IUsaiT8fvHnb41npD3DuCsl6gnDW5wo303hn9Rc6EQNcqA2xZanjOlAvgVPa3z2XUNLot1MsCkwmC-0D_WHFbLsPrnEKAd3XIDHGr29cP3NUUYzVFI8xGBApQ7VJcvWXZJ5mD4xYT8RI796OryVNJgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdCv-1SYJvM-X9-VWHQWkAh7iDBcwMQcZz2iVNsksP9Cx8ssg9Ez6H_Ol5Ebv1K1bDoz--55Oxe5gzdrCE9z9ZuCXb7KvUUGLzbgDv9-kQl9nBytLwg7Qs8ozz_c9pb0HMRs0QXBgGHvbuxTBMfA-Ai1xIwA6kFMV8ypvm3lVppQrMnPidfRTJCfOqw4WFu2KkmMtSM_BOS7NTZ6SrTUyZMPdyh2sFYI62TilhTaGrDezrScOO_rkPO3HP9tDvwb8rf2t4y7wnu3dbok-VhBsrpDMY7MLhFsBQqEdk4XiOzsd1Mw5Wxtc3EQinzS0wVPcv0fjo1bYUKxTxrDq8s1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGNyUBPLP50kfBtnMzTpuImekYJen1q3J7RScCP7mcgnstCRFprR9nAYR8R3IK10yRebufCsS2dNi5SILG0jKQPwaC5IYX49OkuM05hPak5ktbG0ZdgF9Nu67NZsvtkCAPASQSA95pXHeaHZ45XntZ9UQcdB_InczFGLOpWcHbhrHIY37EW-hMR0ZNBNkOjiy6oReYVzXT6yM4POVIfpdJy3IlttMxu0cu0wI_FKSBqC_DeiHIu3XAULGKcvn0lJJThm3XQmfIb6Qdvknaw0x3sj-Hy37s5fzPpN-HZeTONwBBqtIPZH06mGI4400ocSm7AAz6eJrBGdi-mUGGKd4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=lYgVwGGNZ0TbO26RB8ChTRfY-e3H7s21FYCY3cJKNmxKp4GClBYK_u3BX2vZlyfG7Yv3rZmG9ubW5NfNZjsm9P9SGNHWzZcjs-ZWqi1njD8mT5Hb8Jw4hik9ihAtGBYjbgFO_1TT4vUShh6o0Zet1MJwTFANlkhYnAopMXnED4iJQSnvNzX8ER1mykOf6UEm7iDzFUox47q56MqsMS9M9SnwB2p0CWUSBvQg91WrBbSO2bZUpZQhJ6swrlREI8useAtTS5dwiqi-ahLxa_mQo69bj5-sTQaajUO1anixdZFnEziPuAyrmu5QMhzriKXcZJ0wKdniWxSRkKmVEmnEig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=lYgVwGGNZ0TbO26RB8ChTRfY-e3H7s21FYCY3cJKNmxKp4GClBYK_u3BX2vZlyfG7Yv3rZmG9ubW5NfNZjsm9P9SGNHWzZcjs-ZWqi1njD8mT5Hb8Jw4hik9ihAtGBYjbgFO_1TT4vUShh6o0Zet1MJwTFANlkhYnAopMXnED4iJQSnvNzX8ER1mykOf6UEm7iDzFUox47q56MqsMS9M9SnwB2p0CWUSBvQg91WrBbSO2bZUpZQhJ6swrlREI8useAtTS5dwiqi-ahLxa_mQo69bj5-sTQaajUO1anixdZFnEziPuAyrmu5QMhzriKXcZJ0wKdniWxSRkKmVEmnEig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZz7LTCxOoPh-FBOkWmE_ILss53q_hCqrJCZaOUo9mZ8zTDHlAH7Q1x810H8fNI7ED4wv36-jXPai9oilyElNZ1Yx0ke8vZG8pM6N2qBohLgf45WnWwEl5USEgTZroEPR1QphYrYmzlE26xYXtCK-Srz3fRpfnvKrSw7bSfvuZT9a5GXQVIqRZqeDDJJmkDw8ya7L5trlcAQDnuxalSuCGQSU7DlI9d6Q50833AQxb8rufVrskaVGAk10_3XlZZa4voOcZfTDIxCeN3lwPEyDqljCgbkOugPSx28l1mSQO7civWKc2lGJAaYAwI6PKEjn_4O71TX2ji4ZsgC-Eeffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr27
📩
@winro_io</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/25966" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-BnDUvRqosati5qeGkQYx2Gpy8JlXTRxG-7lv0eKKB8iLXAygK2tUaBioCDA3WagbpaAjPcyDaaHA7qPFu3elV75hyIHw_b81rIP1RZtiiDK-rBPHCxlfnxLPw14_Pl3bHmCBUy2EeLpeAQj12TcJvlTwkBwnyoOSpohY3XacpBurFWtEjT3more-gB7_3TCWHL8njOAtzeOBLarmNtCNd8t4feuakHsh18stH7kvvUaL16R2oqQrVtHAmXo7KTJ0YcIWXRghSDQ6xumRK-5MtFKGWBLAxYWifserP2xM_n1vFnWCD3r1HsKIgv__CUWCa6LCsL44YtGw1iB-TUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlYlHb8XzvaIxsL9w2Va7XnpRwbTrw4q6AsgE35qKQQu0dczO4guMhDa8h7DxsflH_va7TKlbKuLCCrgTSYG84dsie90KJTC6zHe-3nUD9LU7xHDOYjR5Uc2o5YSL1te9H7eGp5i_dxqaO9hNtIRFzFQf4KRlsEKgZLIne-b-RVKPgC2Dv-GBE1_ZDpOY7naE_sloQjf7T8AxVLYhTqBkvLSNJ1cbQoDS9YJD2p7ZyhEC8rF5PtYmmdO6VLmOyPbBhjIW2eBDqG0rv_a9d1xbvNbMQS9ZIBRHOPBArrPSLB4E4WbdzVKQRNbK2kLg-asGOWWL5OOjaZjnxyajBmLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CVINnQB8jN-qwQLBGb7mEaAmZAFfha6Ubbs83KNCS4gE9h4gk2MlWb9SWlHFoH7dWZZnRhVaxDaPnUyUj250Gw8xKo3XVLnAgf2F30KJ1ze4AFJqEx3FvOQjdHXlPEKUcTXTzjfVApkEP9kKxknS73lVQ7PdBgiAlKlQbYSSPqjfDVRaHNAs90wNqHq4Y6fa_X2DrR19g9CbkP5FDqpVhiokPh04qvflSYoehy5SEGMEE9XsiddHbWYTTsbISaRkXE7jjv2gj3wGOTOxOJkvVO8uJyL3cMki4n7wJU6rp9AbfA_cEffW9PssqP0lKinwRCP7iMHp7S-avv661pqWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=CVINnQB8jN-qwQLBGb7mEaAmZAFfha6Ubbs83KNCS4gE9h4gk2MlWb9SWlHFoH7dWZZnRhVaxDaPnUyUj250Gw8xKo3XVLnAgf2F30KJ1ze4AFJqEx3FvOQjdHXlPEKUcTXTzjfVApkEP9kKxknS73lVQ7PdBgiAlKlQbYSSPqjfDVRaHNAs90wNqHq4Y6fa_X2DrR19g9CbkP5FDqpVhiokPh04qvflSYoehy5SEGMEE9XsiddHbWYTTsbISaRkXE7jjv2gj3wGOTOxOJkvVO8uJyL3cMki4n7wJU6rp9AbfA_cEffW9PssqP0lKinwRCP7iMHp7S-avv661pqWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR5gai1hTYJeZ_I4cj948nsmRGLoxiUgFfqEjt2m1sxSu2q4lHho9IOtCoQNRhM4fkKxNlKv0eG9JQM_x2C8pKwkAgIpgXza_EqDV2-hOJEWBhSlEVU__XE48as8mhw4JVvyhYI-ccoE46XUfSEI0Y0SiumI3T1gxZ-s3E1vf_El0GCqm5t2DYuC5CCvXRSHa6k1NhzfXRASaKkzai8PpNPpQVy1JUDwVxOYITIEjEiQB1xpPgDumaNzTHSClt-LUveZREltZOteViQD32S9mw_w7NdHizMjLqU9MsF9qLImErIJJ8pCzGJKFwg4Uox7hrACywWgsEQ64BNtgFKVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnaGoTXz5BGXyRW7sa-hiYhMj-Y8LUcGH8HdlKdw2nrcFl_IO8cCxdR64EVVjRV5A9KRXC-_QFkE938_-lYE1PXxgXOLquoDsK2GhbhlVlUXwEMehZacZcjaBhAyZcegUDAqYnXdqxZyFRiSQed6jhR0dyyDOfI2thoZk9ZiBFvZBHpce_K7EFsh2_cGQT3JVbIO5su5L8VWVGsFzZ1DE0yXKh6off9cSvppX-oPUm10mbAeqvNcJFQv2lkOtdcQZX3GRKT0UP7juSS_nFNsUY9RVd5gAuCLlSW66L8RcKJj79XZcy-Q410LQN1q1f4ncgvizh7ew1QwUqM44F15-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui8_R_KVkR8b7OyOC5Rq397-Xi6IrS46Kkr__9GpV8mmkNZ_JbfD9XMLAE27ma77O2JvlSz-4FHZv6FZ8UC9guB9YBFFYJOnYeC4Ap1TrMpNlpe5tckjm9sJfkgZh7vkSmqUElyuLlAhV_E7im0SC_CIKjByqd7P5KWK8KGRI8IJAw-7v2l2Nm84u_vL0qOTvQPX3PxtXpM8jehJy099hKLVItFiv29e4dtr7i1z2MJBYa4jBohdLauvpEuzw1wFKuVufsZcc41gnKTIaAbjBK1UMYmhXYCqfjlTgB-qoAYG1pGXhP0K7yKkYiQ93D2uhvyUmINUR21D__vZpDpGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVwuYRNa6cnT9zFQIrLlPMUbGR9nuDDTM9lJ5WYB6glM8Zjuazz0LggCb9OLlUtlsqBD-yvXsrWk3ywlqxRQb0EnLWihjQcD3CjLyqI8IpaNxVPcx3JnnnBPug15LW_dEHTyK9u4oVrYF05eCA6d0vg4owAp45f5fLJy4PHeGJjD0wdL54wQm7tw5-K-HLc0yblApF6OG1quM7ykHGl9yx5MHd2Xyoc55ym77ViBK5wmm25-4gJALHWe-Trq_z7ro6BCbyaYFyq_sL67tFqhbYMa8Dz9MLKACYqKHrQHDwB8wUt2In56K_xBLZTD5CK7GLi2IpwX7gphAlW5ytLd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=L-CAvaouRl_gyHUD231Q4IdNK9txi0BYahhvUsIlByyaBgI_41UluqAdhCuHYsp06D709RpZhfkl-AR9XJ0Xq7OIeNqBqnGnC5RJb8QY-yXt6IWECCM_s3zY6qL_6RIPLy4x6-hTVecdwylJkFou0m9hhUdwVRGYCzRnAeI6_eZ0ToelGLAfUeIJPftlFQRRGpY0RIs2HFmOB72Oth6DaPO_iFXkwZn4i2qf86MXoMDE-hS4oB-b2nRbyjpPjNWFvJbPi1FMHJrvpJcDv_PRhZ9CEirKRS04SYqy-lHgGt5ErYK4LbS3qMvUXlLEWOnquq4CyY3gL6OHUDTmXSuUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=L-CAvaouRl_gyHUD231Q4IdNK9txi0BYahhvUsIlByyaBgI_41UluqAdhCuHYsp06D709RpZhfkl-AR9XJ0Xq7OIeNqBqnGnC5RJb8QY-yXt6IWECCM_s3zY6qL_6RIPLy4x6-hTVecdwylJkFou0m9hhUdwVRGYCzRnAeI6_eZ0ToelGLAfUeIJPftlFQRRGpY0RIs2HFmOB72Oth6DaPO_iFXkwZn4i2qf86MXoMDE-hS4oB-b2nRbyjpPjNWFvJbPi1FMHJrvpJcDv_PRhZ9CEirKRS04SYqy-lHgGt5ErYK4LbS3qMvUXlLEWOnquq4CyY3gL6OHUDTmXSuUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-p75RkpeshXIgRwnFibdqKjSKEaMpyqdr1sYoh1uf0KKj-4kKRl7Lvaa5vBKZYzAORxLSJFX_TT3uX6Dv9o6qbZCeMVJqi4uoVDSOfBW_09gjDOZBD9VowE-58bgh4oWfEhXf3WzbHn68dGtCievgOC8knJLsfvFuZXuUEC3lYI29yCLTZ5F5rX29BW1dzRu-AhYIm8CfHsefCyiiYRyjWm-3WOOIyoIcc3Wz7B6XqS01bQcgrGc8C9udjft1mGlsTTK-hPbAh91M9hJ8CH71cqZDGWvqMWEKoLiDS8BbJzLklKnG82fO4jqYePcX2nib6M4kGBsbJjewNMxPlw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvXZVcM6POZolmrDd9b7HeQx3TZnG_s6iZfOjvDpyUdtIkMbje4hhnMRUy_VYCtq3ijWKAZlXX64pqXtom62X7wIfrliJONLPjz8tC-c5iMv9uqzHS-Drcm9m4-qUMAVKXys_UvAfPBfSk9DhAuQssT3Y0A3QSzV8jbjZqdOly_JELig1PEU47Q7_sfEb13vPUMEurxWqqUBEQgo1ced4BqIKPBOQ75Ro-4dm8vAudRQgFZGvjQIHt-bTAKd3v0hkdd-3jB0l6PRd3q9w-tnIDMs-RuLbTaJkfPnKzofwlTuCCL19XJ7jsLKYWbufafo3ErcZwRuJ0B8cmLEPSRgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eke00M23YA83nOZLmZT_azxkg5sl1IlOf1GGszyzysK_EHrIjhrBuajxt1e5jaSrb6Si4hctkMr7fB9iQNQFlGqNCzYCzexXivWxh7kDE_Z9iA3I9IwxCNDPQLCrP7mCpRnLBo6nLhxTDY1XXZ6tjSERauYf4ng95rL6mTQj8_GFN9o4PH7qnWbV_OE-GQ7TVUWmI-GdrjHfi_b7uSexMEfkm3Q5Ak-mguYqCgtBV1eB5G9Qb50FRyOFUcVMIQZFzRUGkYS0u3Dcm5SPChZHRl-dq8AA1AGdMuCZwmlbLcY23xAx7sHCXWIGkaJbNX6HIv01mjkca8gPV1j6vyvcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBdYO6xkIu0S9-9hoGCl1iSbuk-8ELDB1f3eXTmk0b7HbsUzvjaYh7VMbnJnvo5JDI_PVnwPg7BAgf-rSjJ_oai_dl5TezvVomr--Nw3pBH9EOoAM82af4zykWLRu7cTcIrrZ9mXo9rdaUCtT_QObg-V4Yxn-F1RJbtedjHoe83RRY4_T2UqHdRwKihY8se2HsEEnjQI0y3X6MnatkPd7zu_YknYVMNI89d0iDDCjXxnvg44-79KVUEF-98HhamoSZiLXiJWUdAvYHeyBGFZen92oNep-faYfWwkeYKN7HRsaUixScXCwYKFj4gPxNkhuDcw2LKLcLMlCLTwxegmeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnj_-Ip6k_d1N-yK0aICcTD4ibHn-jmEfMixGi8AABUaOGJjIze6MpY_hk-ReSgp2a5BuN5b2o0Fr4gtTcUlCV_DnweO7TjPsK0E6-9yBwz4v5BEMoAaRUwW_gjxXZU_H5QALkbgXOEXFuLf1eY7w_IUp6gR65d7DPgSItJFbl1fFBTQGEESPdMRJzoihqztabJqXksG-nRDUO0bDtJbgw05gRSPmVJZWwKEHMxfQqUpbz1lTzuF8RIWA69lTxRM_Li0whJhR-B3OG8O3avO2tzLNBxeM8pX65NLHMuHwx4N8Gu0DF8m0LmA1Ba0VirJKmGkJYnGfiT1WxfVfQE6dgMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=dhpy-PIZ0om8OJtF909Qt0QXVlYuAHdpZZ-GJmU9ETcN46hRIQHY17soal68wiKtrqhET26CDyyuL7awgkbhWRYcQwx24hC4CaLZ0_D0kxcVPgp5_Qy3uyVZwEwRkAEwRVt_LnptpvyaPugn2c7bgDttEeAxUVwWJrydMZS81q0DMItl_yJZQGW8Q5_bzo3rn0eCRDxxMqPajpoHNF3GsaUsdFnsL3LMBPbivsnQ8s3jGHesi7X2KRSOc2W3HKRI2fNJAQS7vj4DVJCHqS6kKtd3NeDnIl8H6BksMCihTkIJunk2Hl0_CfkQkNvgDFiH4vMK2Do2OQkMxkYbxD304LzrkZiziSSIwQPfpk1xwPPRmfqEYOuhcUCI77pdiapkAvz6j-8Qs7zvnR2LNf2CCV9Oz824KBAfVjJAa1xwdmNQWVGwQlx5EAVDz2Y-f36GKf53qQmNT9AXoF-Wda3L8mKN_IopZnRa-BI4-02Td5hBJ63C394Ps_CnfmD9H4M6drp6VZRjq-m-jT0SSzmt2a1PQD12FNWqbq7xDoOtGK0O5_icZL4pqBehQOWdeqJKsYS3tc4oftsO1gRxvaPAQJzFdfFLZUhkPgVzu3R3x6ryqzCCVdzqyry1IeOjQB5Cg0UcuaxFqnTm4IVHet43uFCXOXoqetRW4Q82qCvHk-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFMVF7wnsC8SoOJct_qLDYECpVXTcwyDXCUwWeqyWQfmYPNxuZ8r5aXiZVnonBvTGJPbbxVcnGlfEuPHF3dEVt97vQE-DOb0BOVBoGcflpjSdyhNauGgtwMILmyDW-yZYprfAOi6ySyXWWYGLguvQIOF_tsr9kdejmftzleePf0jEFEcHNLRP79oAJEo_3xmUccGXdOfLqieHGQ4wmy_bcVPciBbAtHIDcFpkzP2teQ3Xtks3xeYoOS_DBYrATZ9dfi6fPnstslRTXE8-H-A9ZqXEtNQtD_VjanTcV6Q8ryxB7QFbiUntOa4o7AhBqV80o7PuINFFhAVhG85KWWWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=COxPGB-_094Xnv0QBzi-CUZ3COOJPVHthAvDaoing1Ild7aIws-2fVQ_eBVrq8EjCiWcHhgiTvx8TaaPerwZJHmUrRXW4MwJUVxOIeUL6in4eViMJqu_7KSx-2xCl2H3qH9trHJB7MIhHWmF2PJMKMP_oAqCslPIODheXl_eozeRP9hUwxLRSsmjVaZp4PpVkLA-3uL3R3MxfUB-jOSP1FQJGGVXU_x4uicTcFlJbKiLW1eBKa9dczEb0jVLCA1-OqUEisiAI6-sTftt9QSXbOW-Jj0-aG5JoKJZ3Kb-_mcJxCSZVwjxP3QRacOLGJgtG8dgeGMPCiID47tNbLgjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZOWNuNt3nc78RZ1rQyC0plUZVwDtr6IHvuggIeTfYI2BZ5QU8EYjKyrabCkxOnz54KKNr_jQaqL0efKxm6L0uaiu8BaRzVq2rhETMU17Dpj4s0eB3J_VH0LQdrfIooGMb3eTdnQVNy3sreffAFLK5r_XAeIzGtQDL8Jhn7EG0WzaQXvqbmFMzm7c0lJM0dkhy4VU8sdZZaSBWrhIHwicKxIxF9mxhNz9W_U5q7I5x6HqDtubHF83ZOu6eRjKJ8uJtIIO2udbbJJux3GEdNgaG0HdZpdEM2uX1p9HmYOI4ZCA7mtMqrB9xdo-FUfv9Jy7w3K7UFf-CSm3d3wU4loLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=nasEjlqWmp0cEd-CpbGqbV88mdOLbA4W8SGFyxolA_Jw841u3OiaKcJs3FWSfNNoREyGVeIzfvBKXcZ49ZkPEt3sUTCatpt7_95S9SFu6pLuAoFDdNwogutGsun8g2dMhjNTcBJq2eMXty_BBTUKIMuQ4AxxabQUGYWxQZlMnbHXhi5LhSdfxgP99AvPWRL5mHQCo_-E5Le8-rkrfHsDSsJ7veIJFBsv3v01Lic6upsxMBK2DdgpXz569CUkVWn1V5a8nV0EtG8oglL1I_db9qD0RE1JOUyNbki53N9cm5XQ1ONplj2lOpNodGoMsy3opyEkdoroYW06SeBGCeoAhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=nasEjlqWmp0cEd-CpbGqbV88mdOLbA4W8SGFyxolA_Jw841u3OiaKcJs3FWSfNNoREyGVeIzfvBKXcZ49ZkPEt3sUTCatpt7_95S9SFu6pLuAoFDdNwogutGsun8g2dMhjNTcBJq2eMXty_BBTUKIMuQ4AxxabQUGYWxQZlMnbHXhi5LhSdfxgP99AvPWRL5mHQCo_-E5Le8-rkrfHsDSsJ7veIJFBsv3v01Lic6upsxMBK2DdgpXz569CUkVWn1V5a8nV0EtG8oglL1I_db9qD0RE1JOUyNbki53N9cm5XQ1ONplj2lOpNodGoMsy3opyEkdoroYW06SeBGCeoAhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMjhljuRqavQoh4h0qkuQmrfkfZMHFEhq-mj2jGvczhrD7SHOYBcbsEfEEST9TkyG14sSwiZ_XJKPt_itvYCbHtHsXmCYyDlpqzGVpBSe6NMYl0PpNva55rNozystNncz1Xh5Pc1nmTiTFZz5nIubs08BdFD6AAJHdHW7A1yMAGhKbx_5KpyvUQSl05iVQLY6-nCln4m8eWxiuEBiFji2eqgmb1y6S7Y4Ec7eyUSEwM-j3nIy8SxnPmqkR6yTcmr18m8ifr-PITgp6eaYhi6WwPWscHyhsOFVFu1oS12nHrjkZZbYGq4GKWJjbAmTfTygPiJcypbMPFqfBz-al6bLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP7nv4Tueogqdx1A82Z7HK1-jpnjfmL2jIF9WXrcTbKINEavFSf-B8SGdeK5Is9cG4pqhYOygUWvxnOiYxddQDil4MWhTp4aBTG0nf4e8yS8hMCkn5DbE2Nf38O5Qn6PXQK2bLcms27vBdiqKNZ7smJDrvRSBPyj6vApvQDg3A3MhKFR0yK4HQtNMwO2gjMZ_3bhYB7_7raTq8y1azhVCu-ZkYRICoUOONOgrhYO2iTwZsCR7NylO1Wk5Tdlq8nFPM981DEDX2OM9uDzlawoK98fTZLzaWt48XVaaoGT2ich7TW4drpOiOPsgLeYefMgi5x2ZnGN0YX5PrdjyrFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25944">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT4GR775Lf9IvKuBnYXUVrd0kmwe1Wg3P9SH6QgH0ftxiWxBwgivzygaRanQ4kXnDdQgOpbzbpGO1T9KjEhBEmphn1KFSW24jRrelpcsFMRtyrDDw1IeR8e7yYFO71CnHw5Nd_hfjn-wnVvQOq_odFTRrLDgwHB64UpSKzEIkjSxzQ6aqwFSswKyj-t4dkWIQfldfedmUOuyxJuuOAowxqnih-zG88hzIdnq18IZc6alFl837bghChZ-VWinvZO9Sld827yZmjd7PSqyPo_faTsgpIKyMFHaSLvCzisYvcGSRiGQcGIhwdlLwFyrFG-xamFACa6BzIDsXqNgeuEZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25944" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=YjWCGHlEjb_OzKIq7XgaDRlq5qJkwyyPMycx2pvod2KKveSmfmXll9lGpXxpgADElTgqJP5rUWKl-Rc6cpHtZJqttRf5xkhLcYudQEQeRGjWHRiswK9rE0bh9xIF8aSuZIkNMWq2BtJFrPijjQzpKz8kKsCrIFv5v7mDRi5uNHYfI9hzg6wELepjsm1HmLA0yGMo7KVpoHXsiqAm3wy8FWXfNtj6quOdT0jTot-pg8ns6Bh4WNTQtZuUlCUf709ItHZp5PiIUSd4lWHu_sXQ6F4XENlkAUeWvBIl3tzu8n4ch6V2nirq6nsPnTBDMvx56ZKtRp598il6sjMmqh9mrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=XPbjooFk4s4OafuKYG0hjrJmCEIvgDITFDrmQhAmjrM8fX69kcdq3Tg0uNALlhWaKRxyDFfK5UBdEpc5wFvSlxTXWV4XoIxvPy0lEbe38gc_WyAtF0zSC9XUVT8f4UneUzPKuvzokbGN6IW3jk9doXQhD3z8zYaLWsDsoNrqjapw8hEqBwJ0S50QTTu029JujOzWjk5Ov5FI87EWjWVl3EBPu-srnLmhpWgqnNv2ic_OkDtrTRlu1jftQ3IsZDCcjDEBMtYMMJy-8pKD7TC4UZHk_WKEZIgGbx1De98qtvb21ZIQkrL966ZkWJ_v-Ly5p44_XeemusTKysInMWgPxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=XPbjooFk4s4OafuKYG0hjrJmCEIvgDITFDrmQhAmjrM8fX69kcdq3Tg0uNALlhWaKRxyDFfK5UBdEpc5wFvSlxTXWV4XoIxvPy0lEbe38gc_WyAtF0zSC9XUVT8f4UneUzPKuvzokbGN6IW3jk9doXQhD3z8zYaLWsDsoNrqjapw8hEqBwJ0S50QTTu029JujOzWjk5Ov5FI87EWjWVl3EBPu-srnLmhpWgqnNv2ic_OkDtrTRlu1jftQ3IsZDCcjDEBMtYMMJy-8pKD7TC4UZHk_WKEZIgGbx1De98qtvb21ZIQkrL966ZkWJ_v-Ly5p44_XeemusTKysInMWgPxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alGRWVYmul9sl1JYPSbTelcIFebyte3XqVP1yRg1LiYzahXATGMfunxtXQkorDLPVcR0Cg-KAmFZLSle8MSLV0JP9ee41qLzIevhlxxPzL-8ngvgzhXdmyE4OTA9GNYGgofb0syarORTp8hj3dQDhqHmhXk707f0OcfeEcbBy98Bs01IW56WosPUMbD2dYJitWcDNf93dIRVU8f46wGLXhGKqCTMXF5ptirf7ZhnmkyM-6OwWdWdELN8Rqo9Xki98IEnyHOEI3o4pz0p_pJVsonPsnLDw-HNLcX4_L3dga5KURnCMO1H80C1G5bzzhtapwSHS3DWJSqLEWKavlCQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=tR1J4BNyqoCzVv-b0YH4NFhHRGn1TsV0CBnWHZGAApLVjf0wGuONrqn1ExO8GPW-NG-KocgQLe5xWAv-IgCNVe6kNI50C7SK1hdGYfRf92x6JAZbm4BUKH836lAOeOxZ5WjNGQJdu9bMk_7j9JPhUrldgrQqs4335CSEKzqElW60K1ez1Dk-KoLlN0g8hPA2tjW7GJNnh5jrxVm6gGtK488HVY3TEdzcf2kCurHCaTJpjuN1dC24PBYenWGScNOz13mDOr_ZUIpLmNsbDsbu40eG6b8ml4dxKdhuz6bTdEFIf6suvVAMTkGDFj6S25b--zeVihaeMbCQQv8vi9mNQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYOQoqh91OzBBEa5WEYFpWDA1JnklQai7fwysym28koUT9KzOXQIHcKZqoN_DGepMleNKW09Zv0_n2VqMph9cZFad7lOhOgXmsVyVrirAj_3gIW6WOi-j4x_lwS2sewDNGs641wC723JHmdERMWvc228h4X861tHypRtNGDQG9xWi10LIY0UMREfG5sN-CbtFQE2GJTECrGkdKzGD9GGc0pUTT4m3ar9j_119NRXCKz6PnHmbS4iuhpMLSqqLcYRnOQhBEEGllIzJKpnfVmXDXJhfBG-N2CpYUPv3scqg_hW_aU7h_YLqXwTILO7R7med_pMP0oOKYasfXnOgWGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBpnh50pdv0AA-2BCq_JG8__Mw-y_nulShVksAf6QV3bm8yIkXyJw_GwCrqDr5pgcvdSlctGctM90WDBZexo6o15aWYFPrTgf6YXTC-CFOJ2kf9-IETONoWJMEvBGhSJReGJOjKdVwShTOg_CSAkA9Ld7RIDRspPyNsgCQ1fnsTP31oFfO10jRnUqBkAcN1A5ApGEPzlqg6jutQTl82zb3SOXNvb8yH4drX17QUTTmNahz5NVMVPG18OPxHFEQPuNEa9zXULOedUJgQ9NY3M_6nuTLrKu-wY6Di0_LRfYiEbAKzF9Kt652T8wN9XONhy0FBBbk0QvWvbvhRYv94i9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO2r3JnomR_mhtIecxyEqox9QFGOjOu0oybw8pKQ-KquF5owpZRSB16CRxEh0iRLg1XcGbrwMqG4LvxXqdm61ednXdk8wjlnUkg-PcRXaxYPax6TrIF8qN366jfRRm7v1gXEWseL7PWsNGm7_OU7u98iXHAfQCJAApZRKdKivoqAfPDYafZ2Z5fYmOrdRMdpHqE20e2a0BZdMN8F5YF0evRT2X-gkv7akJuG_0X4EFHqfjjdzK0ywTbckAaTPiTxB-U-JKXDw6OPYCGwFSmUHryxzoYEo1ICC8Kvwxka0UcK0UczgC3qIv7nYcwx845-d25KuW2z849QvKYXKA4Esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGCM8gx2I5YZjUgJ2wkfJpyTK9Db3jM74ANKbGprHy8ssYVpKgXSi39G6Nq8d5o3zDClyfhkHcbbO8V6gsLC39buxD7KVPaEoA6eze0rPB5pjTDjjl19_acHgL_qHz9-SCTuQv2e77aQo-oTRj6zGaDuDoJM1xggFN2JNsFI2IsN6zAc4BQGE29Yw-qdB98Ly2dP3cIOw0yPzf93tzLF0-iByCXrS4bsuoRk_wyo8S_CLHDM_AQ84B5KzDm-l10vM7sxl3_UHVTrfnjjOBDokK9ERhGSfgT0L2nEvtz1m8_sTFNRa-0mesOaQg18TxMd0DglqYBKIitHHhslx4n92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nmrmr3esKoHcdHbDkrIWOjd_k6lHl0j7PL_wDJ0_HMZOLyxt6QZIRUXmQRmeAMSRW8zLSASwq90xWsMwz8pua1kylJbGdfcwifiSqXxOLANVIwTpdFMkkdahERN5zkITRsmUN6j_8Eu7Y1P-P4whOVcxAWPtf4lPAwYPaBTm0KLWGnEJ94BlWK6MZ_AHfs3Csxro2sFPSECYZPBCRlJK5EKmpMzaNTNaE4whZ5Yc3-7v49FDGulQqLB-Kk5Odr13yc0_IAI3wih57ytZZGLHua-hPXmcC9JcHgCTmrbW9UOiSHDw8Zsp0ahb9l2PJ78qMaA_7lq3Wcp66Vxk_9CCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5_KiiqH3LDUvuB6H2rcrakvbMMXzOp8vUbvteXh13K-tsoCTgEsHdgHKs5hYJwz5GW3LYxk3737Lmhm64fHM1ZrwCCyrV0AWByeZcrPcLXhyhBtd3siuX2zFJQj4OkmYMLPYjYtXSBpM9f6jutf9mNEvbswccf5E5Rb9m1WhB6bewTUt4dzZG8rrjMORHLZCbKUFSK1A0-LbU6keWR90NX9m3v1ts4lqQ-zcQH4yEfi-IoVHmMfnFv9m0Y_OjfmSdc8JpRDGR6V7HhYxGoA_ziF42yrn4hfyzW1ecYv3ipb8bSznnMbU7qkUuXrMbrUlb8JRdMTsMxbIjhb2RV1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=sjKiQ2LW61mYAObP_n8Ud4WlGoe0sRWXTd2B0rdzQvJw9jM9uougjZnUUU_SBvlMwa-Bz2yUpNaGFWvb3R1_xuLupfnvn5EwM7y17ioGEfuA_pqBxSA-8_4imWK1wNGsb3cdtlrdbehBUKhsk9yMuvZ4LJCMpBDVGMtSgvq1aWNWOZMc5yun3WvdfYLVbsBw0MirUS3c_i78Y7qvXdOlf-THQLIym453PLod3e65pcMEdt8EdM9CH4YRP9ajy5G8UBN3QzyRcZuYzUWCabgKWV8CZ4Z-GBxnlmBTuDG5Kfg3z3kzrfBshCfKZ7BGI0puTXSNC1RYyyHwt5ORxRP4m4gBj0h557XCHJ2y19RYyU22lZdoD49kQAmW5gPq8LTeunYdT0mYJrxRVYQLvt297blJG26xM3Znfks2IddPoM8Cz8vX33QUb5-Q1AIAXxhQPb5Mf-UuC_IkDUOpKZ0-a-vhxNdjY8SFiCRfW-b6pyrqCvBMPYrtFpktCxjbBl8bRIlSXGy8QpGPolvsraVKTjIgoz8XyFR6KbwIFqvtE3_ZYE_EJLEhDezHbszMZv1Gzv5vCcHRvpSuAXATcJ33dr51V31MCYVX5txTNgduZz5fJFmU53ODtMKak5AbtSKe5iq6_7CCUPD4CW7cE6iCBJVxKJTr6vOLMsLYr8DOvwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afb7_k6CXkNJeNl07Ulo6wIh5orl64yQ6Akakp9C9EVY2hwDdNDqjArQKvLdL0UCVcgTln7viitUmiJIyR9iJEnScCxcIG13qSkQv4vXYxYKVGAW36617_GGq3DsRHFL1Mc02Ir54TvRXtTHVnji-6lThYpRKZPukEo_Fal72AjO2YNROITuoGA49Al2OICOKVduf5ksYx7WHCHVQDOWBjauFkCiVfXGzC5VCmrdRGyQh7elco_rS4taUXdf8t9pm8BAGV7AEFyOxU0OpzpuE4yXkheK7nA9SVY2I-iPEfaQiY5FibC_5tV09BC8A-ZpSGtikMwZubUl5t__V_DSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP01oFeAbnTmJLwCZFh7SchKUT7J50p2hmHXWj36QTqsQlXoFv-RuO2e4X6CfbKfj3Uh5N34JFDfNB_2zKJOldajkXheJvbjlac8PYAkynOAiA5yXySVFq51pSXrqPrg97RJJhO9fjFf4IqkkayQsPMtL2JZUrLDZEON9NpT_PGjNnWaOgkyzxTK5BqRrFOo0GT8cNDWR6NJzT09avBW6HGVfOZxKq7x-ffX8FIi_R63EnaT7Aj4cgAIAyv50mzIjkrJcZvu7xRlFz_DynT0Kmm8d3q4LIkT2M2EY4NvybddIA1_uIjOn7RtVi8IFTW7r4THXX4MxIs6rseQO92AZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7fY2IyxUbOqvAtbULAUcWDY_EC1MiNoOzl_ANlgtH5t-yHk82gGwc5HehDKCHf4J1_NbPCwD-OK4dbwA-iZSpxE_JwiYx4wK-WgV6hRPBSyQXgx_Hhzy-j43UNXfjJ4IynjIqrUWhykmnfOfakLXD5JbgKVG8C4vGpd3IZh9gYfUw1Da31yQeZqvWz6ZPiGt3N1mAUt-PG7C3VW_jih0BnoSq4O6lvXDN0sta2J4revgEdqFQOM-G0UaXScowsLJf2RLX5S_NF-DzgA7UfnEsvp9IMH2dBm350p6o28zPywby5LVUTL-UTaQqzHhDLn8V92wq0VoY0K1PasJ1sgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI0srr2vFZFow2YTy5dTKO0gmaij848PMV6E-UF0QNESB5Hz1HMUdnYZEzYjcD2r5ujq7bK8BakYCNPXEy-n5YrbWho-EE6rcSBZ8Qmrjd1OVxbiUtjGMZkz958zZiMeu7U3u31cs23YgQCky-BcgH8TOFRze7IETfm0nIgwEtGn2jJYRubTA8EMbIoXbokvL0X6VSdqb4F4ocHhaobja48VFFn3HAY6heBQZyqx9Lk9CF03BFQ0oQ1JRPaNKV3Pm4D_L1Cvgy3m-kzhsZDRNs5KfAA2sFqYcjd0dmepCeTQTp6iOFp-D2zZui2I9UvNO3OdFUoVpAYV0uvWOPXWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOP6o-Lv8Zgwq04KvebkhRAczwmU22gRw4jiBLU9nw47VvAqKeLjMJxia-4r12qyPjwrdiYUuqY5aSm7_bo24wfi83Xl9LSxLepHxTLgQ4FYYtnbzRd42QqQ9xITMu0kEYYwiKpvCIJslElLkGotf43UG18y8h2MrYXlZa8DK4RmM_O8CXxOeC41SZSUbnilhhcDJAI23cAek2tHWelZxJKOTWfxrvZ9E2Ya63MNAOVdQ7Nvq0PLdUYlwATMb15NGIgxUmQEU-BnjEzJnSjCd18HaBf6aMFmthfq4gYzfjc3aai16dBoOL2uZpE7Du15OGrub5vWWzRT3zAtkXk0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm5Fm1tNQVZ3OqACJeOnC7Vi6zgrPlS32xKQTTMGQM41WIbgZaME7JYr5DIvsbnD8LrgHlGt5qhQR6Ehd6ea_8sGQ92of6MHZXbyGF1tTofHtZEkau6l-12kqd16HcyR4LLARw4a2CNTFCl3ZzZrUwopEW5HO3N5-NeTERZpYELngomwjir8SbMasVJs7Z5r4vioUbPwzw6MkoaZmUwlIpHNzB5xaRbvpPHZzMo5WnegZQ4JaLIB26MH3fIkO9WEhYe8YivgGULQc0NzVh_69JUAw625XUoPuxg21mebZodcsYxp3rxnXrTdWVYXDFmnFFg9iTnpx9M7ZOqmEvCKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM7H1EOu7NDwOy2R9VCJLuodvl_HZjrsNVQ__G25SXpJL0sD1YuVq3h9qQsQzkA8BYTQpFrn59UpIRS75kR2YRsIJlonooXCmnKSWp5tnPePGh1qkFWVrSUdj7L5wRW0RYl8CH7APZvoL2TqfkrgwMtmwk5Zmlvc1mVWqgeczvjXdyN-CsXUM1PkNCzdVxN_CIR73FLe3nY7vO2nFuA_A3agLsFlr71jUmzlJhvfkgb12gUOLLSIwWyQstgwcqflYd3bAbqNE35v0_lI0cPvXrFdPT_iZSH_Xf-oH7lju2Kqo9jWODCRE0X1Sjb5WrOYBllQVayFjTzghyx0Ru3tCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=PLrPS1n6pYq1qRde3eTvt76COKA3V9F7pG5IJm2S2uRnljQmRbvRVAYOpS_vU9kMFB1-LPmtw2_1S23zPH9shHPzbMRRz2_mkmViIJlkBwWY6ECUf5lLdK5Mda0gUV9s3ii5Mvwm6wHRE9LpVaLzeDJEEaq2HtDsU2YzXeb_Eg8Gz3Q4DSbDG0RZcFwH6yVpzNd9PyFqvCUBhjUYWGXbM457i-UGXI1tzoEH8Zypz6PICDuxw2aVNeDIoarsgQnxjU7DNV4CRexVQz8xASDXN_B-ddnP7jGGvcShZjY6JVIWcqfotgNuA6vbaGi9sKYbZiAdG7AU_AaJig_xTzQ6gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=PLrPS1n6pYq1qRde3eTvt76COKA3V9F7pG5IJm2S2uRnljQmRbvRVAYOpS_vU9kMFB1-LPmtw2_1S23zPH9shHPzbMRRz2_mkmViIJlkBwWY6ECUf5lLdK5Mda0gUV9s3ii5Mvwm6wHRE9LpVaLzeDJEEaq2HtDsU2YzXeb_Eg8Gz3Q4DSbDG0RZcFwH6yVpzNd9PyFqvCUBhjUYWGXbM457i-UGXI1tzoEH8Zypz6PICDuxw2aVNeDIoarsgQnxjU7DNV4CRexVQz8xASDXN_B-ddnP7jGGvcShZjY6JVIWcqfotgNuA6vbaGi9sKYbZiAdG7AU_AaJig_xTzQ6gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pegx1takiH69MJ_8AW5BrvEKzRA0vpPSO70Ujjzz2gP3AFNNCJwGbnqEwugC8fnrEVOtnGqzB_p9Wv6F4tDS25dvAnj3fCwugwyaygTPWOIGe7rQxfLmVWWVVcO1cp08O7HbTzsRYcssaFI-JNiOHqNJNpN9OcZJ6nbb3t2ObdUIsu8m3lizXhbJSzJ5Z5sTOlPQUcXOfpdQhzYIZJYMk9zENgEp1m3GSxKm_itenkAUOb_5beHc9nCsMBmAv_usVZMQyA-QTw9TcWXzUx77NXUQheY8hDEeEJvIZcJlTU1tl_d0hJd03FsQpUvb8cQae18Y2CpSLbZcHl-SS-f6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=bniJcGGL2YdCDiYQdg18V6qQnx4s_aZuDKJXuZvwtGpqZ2fiubV9VuCYHwWzTwtTeQnxVBkhASuYVQrFz7MRYKt87inIwmG-eHrQ-V95wkyHo6vI5WnWAOzcQJKULcczpz10iBnjOz96VcV-44w-uJ3aurEzuQsy19ZPH4ATPatQDZaiJ4tSpKj6_cXVYEtVMGgaMjRnoD5cDLcT5LJOfGqd7_YKdMM2V2TaSpqdp2MNHvP6f6NnqbwnZIA5UttpgZP78_YDJ6uhYfbADsWbcQ6Mwv_YvdWOL6AsUzATiSXgPIgKv8R95ZuAmpiyg0faqk6W0M6cMu6FeHlg8G4NzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=bniJcGGL2YdCDiYQdg18V6qQnx4s_aZuDKJXuZvwtGpqZ2fiubV9VuCYHwWzTwtTeQnxVBkhASuYVQrFz7MRYKt87inIwmG-eHrQ-V95wkyHo6vI5WnWAOzcQJKULcczpz10iBnjOz96VcV-44w-uJ3aurEzuQsy19ZPH4ATPatQDZaiJ4tSpKj6_cXVYEtVMGgaMjRnoD5cDLcT5LJOfGqd7_YKdMM2V2TaSpqdp2MNHvP6f6NnqbwnZIA5UttpgZP78_YDJ6uhYfbADsWbcQ6Mwv_YvdWOL6AsUzATiSXgPIgKv8R95ZuAmpiyg0faqk6W0M6cMu6FeHlg8G4NzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W83e66xzgq5eHYbGlR32nMRNtmzTTiOBpqs4ze60946Ly4zq7GLJIaEw1wJIDDF7i3zoP1BfTTwFZWvsw0XnemXB4aD7wAkRy3xeQlu78mQ8_fDWV9GSHmQuZEi-I2DKtCDaEFeCWN0kuWCwZDJf3yv8gr5Fo30jPEZjuoBYTXuaxM0HPL6S1PnH4Lyccgw6l26eGNYJiyOr4yAu8l-zzG_eILzxNXrON90-cUcRlYOfvoFpz5DO1bbYMw-JDMsVxigfmq445xC0Q3FsYCN__gyyInhhj4Pdrn20H4OMNZCSSSpLW9BeMPIV20d8vG35NYGqe-LWs323gzfXvLCUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyNNiNdg70YRNyoeUl0nNXbcuF08QZlN6wCUu6aR51JXB-su5AbEpnCrHV9ZHejtA8XdMojUB9uJHTye0iyVxEtzBwKdRcnmdOCNo5BqvPkt6mQ8SieOhy_dyixB9IJ7L_d6D5OmwcrrEox5yAobK8Fx8mvceICQMxI8NaD9o_xO7mbcFT5XGsxfixgukZTe4qn7gOxaKRe_crmSSlX5_x7V2SwE0-wsl83UZgBP9l1dbHwOviXZ2JuDe_1edLbZeiznlrv24XqBXjk_3zOggVqbkyD2R_DmGTi-_H3Gkb5gMHEabpCx0ret-sxw0j701flDPn8IYaSTwZJd81BElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI_tHrm-aWfihLzBIbaTxMIhCGWeecnxGCdM4UIGL34zxTXkWTqgASRd274IP4lc0XX9yTXZB1SwGQxdkLluSXTqJPzHERR-FaKdo9OMCSYH0mlShSk5i8flU7m7V7zt4pS7L3YfFmqsHMOFpwyGkyTGXPBjjCMQDD_7X3gVuPFkR31X-NZO0mMUvpWmFJClkqzHgLIM2D62bUTCJ2iqFWBCxlNUvhkcHX56yEQBh-yPatUJiw8pPiS5MoVSnBQ9NV8Ww6lLbQhNVvUmsqHvzL0U2ISwvD8K2yl5xN1Qk6ZGyUGwMswqLfu7Cg4cA3CEalvxkWY9ZS70JGV-9ln8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYUvtFewI61MU-5Lc9QY079hFS8_EVNh0T-rtVKDFeIv90hGBsE70gVt2EvCH1quFBWTac2jakP7htUB0qoZ0zmCcqg4n0xyBTLyfuOkesNhrkH1q27luagaUFyM8U2MGZo7LkFEWoRRJc2A_oTgN0PO7UcFU_OPr4TGSe1RBwr_QzwFv-qvcRO7AAl9hbicor2hxwunl_Of9SZOlhWeV2vOamkEroaWhmqvJTlRQcrUr-0zuMrueL7U_wa9-y6ETvZOn5jeuG2XIeGt2B9cRF8l4VX0AFXMYdpS0xJkZhNtrUpydo-pvpS0zhbG5zYcKTTj1ADNeLT1EGdpPAe9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrJWHnr-zhpiNGe8YtSBKJfceQMGeT2G7LZ-ClO3yMFjFkLYC6YKA_zeXWJDjKHuZc86Go9BAfzEl_EscdkDlU8hPSaxi_mctHd56XQXjWA6f8kY--q34T-dzbyOs2LZywKO-_z1tlWMs9j8ByNHeQEP7W8_TRUYhcmCO5OKBorU16BR6ysg4NUPKIaXYLxQXaKWWc4rNVfl92Xpapj2Fj38Qea-_ZA4NpsRCh7_r8Ut_46pK3QPqzeeV_8pSyjTigjAA8CltcFhIUcSta5EfW2rrVXEBkGK5zMrQShQhAe3FHe6AVpUjpEF69Uh8-tTNvAIwSawFLyxsZQuUPQYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=NWF7qV-QDo1vLMGr7D3nxf61O2aqJcnCBp5WE5RBek78Zwdl3iT3X367NQ_iOokR3YMA2hWI_hs0WSuG7LvXD1sO0zFJKiXC2VNqplCqDCSB-vbZo2bWo1cOgGAeJGwAkuN1zRQGobVpew99y-IjrMXvReaz5bXw7XzrVgSeUUnmbgxL4anBKhL4Z-mmwF2je3-4O7NOqJCatpfiKHdGMPCGy0TOaHQFe931WAQmnGHqQrzE1xwQ1KPuw38eI0hU9H1DkOUeLJ5_SmZDEqfUrHFJ6vgfLr7nxd5C1YvyBHhSBMHPj35i93X_XQ39XvRvvIIK8B-KyCRL86sbTWYwLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=NWF7qV-QDo1vLMGr7D3nxf61O2aqJcnCBp5WE5RBek78Zwdl3iT3X367NQ_iOokR3YMA2hWI_hs0WSuG7LvXD1sO0zFJKiXC2VNqplCqDCSB-vbZo2bWo1cOgGAeJGwAkuN1zRQGobVpew99y-IjrMXvReaz5bXw7XzrVgSeUUnmbgxL4anBKhL4Z-mmwF2je3-4O7NOqJCatpfiKHdGMPCGy0TOaHQFe931WAQmnGHqQrzE1xwQ1KPuw38eI0hU9H1DkOUeLJ5_SmZDEqfUrHFJ6vgfLr7nxd5C1YvyBHhSBMHPj35i93X_XQ39XvRvvIIK8B-KyCRL86sbTWYwLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=GUa5wmBhv93k03JuB2mh1_3kINfSiUt3sKLTB5eFjbU-GUQXDC0KkbE1IMq6gzMnwTbre-NZo4l74OsHI5gQcc9so3kBKcT62Fi0jfWnggbr2T0vvqbRHnv-HCQoX5cwPBSSDN2nSEsrYhVyF8HXCOWbmzfH-sniI_rMxdMb2YL6TP8PzSqMGrayHornvRaOI_eTXog1HltzatPsbrYJPAzdqytOAEkmBgyG0LhX65hg4OeeUANu-_wn1OLkVgWJCck0bP7g0EsGTHDc2BkcqC3mTx0RSHLlPP31FsXsNSXOu3zZoWYR1PttNcilJuxaDpyiWzvIQLQIprx3L7PnP1HVd_jlHCGwMDf5TnafFp66t7lGMJvwXg0qn8FmtI8GOIF8a73pGFWNVo46B-v-wIeUKoq4r6BCxBuGPQ_QXEVtF5ZA1Xgy8ZUaNKGYNq-OIFTkHtYiOCjeMSyT46Pwwkd2NNDKUrnpTkU3o3zwH6H9dkAwI4TyLuBivY_Or2I9z3PgqYEMGMvCSimvAEZm1PTM9VNDaUO75LbM4OIocVqacw4d3QaeQ9jn8K9qQF6eg8gVzzFHdwd56NUTaLPO8EPEoW3T1gu-FKMKObbZ6RXxrmvhVArkBxoRstL_EWaTBGKXdpWyhWsrptTmcFcW5CcDiafXsJk2oWOpVfh94Q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=GUa5wmBhv93k03JuB2mh1_3kINfSiUt3sKLTB5eFjbU-GUQXDC0KkbE1IMq6gzMnwTbre-NZo4l74OsHI5gQcc9so3kBKcT62Fi0jfWnggbr2T0vvqbRHnv-HCQoX5cwPBSSDN2nSEsrYhVyF8HXCOWbmzfH-sniI_rMxdMb2YL6TP8PzSqMGrayHornvRaOI_eTXog1HltzatPsbrYJPAzdqytOAEkmBgyG0LhX65hg4OeeUANu-_wn1OLkVgWJCck0bP7g0EsGTHDc2BkcqC3mTx0RSHLlPP31FsXsNSXOu3zZoWYR1PttNcilJuxaDpyiWzvIQLQIprx3L7PnP1HVd_jlHCGwMDf5TnafFp66t7lGMJvwXg0qn8FmtI8GOIF8a73pGFWNVo46B-v-wIeUKoq4r6BCxBuGPQ_QXEVtF5ZA1Xgy8ZUaNKGYNq-OIFTkHtYiOCjeMSyT46Pwwkd2NNDKUrnpTkU3o3zwH6H9dkAwI4TyLuBivY_Or2I9z3PgqYEMGMvCSimvAEZm1PTM9VNDaUO75LbM4OIocVqacw4d3QaeQ9jn8K9qQF6eg8gVzzFHdwd56NUTaLPO8EPEoW3T1gu-FKMKObbZ6RXxrmvhVArkBxoRstL_EWaTBGKXdpWyhWsrptTmcFcW5CcDiafXsJk2oWOpVfh94Q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsnlbTz4bc3kUvqL8X2t-KsqPbViJN2lnJJI7ZzfM_GlJspPHdxXBYJPTPUoLAmAy6Dk_MM_SCceDVYI1LGLSVGi0Fv-0o4QnMcY18dV3699SbObPX3hiatAaWRbBRLSI66_Qb8-Q16W2mCcyz0ZUkPo8VNAZg9SIbL8YZQoVhfnNK0qRuEmTKR4cJvBM3FK5Mwwy4KpKKVhqJ2hwYsdjE_0-pEEhsu3XGmG3ei16G8ZtaZ7s5pGqTE5JIndW74Rq9-Yw98Pd6I0cUPdmcDYgWPsFKkkSjpjY79aPR0Liwt8xm80uk0LnRrJMeEt-3Fj6OxvaiRr-2laIvPHPjMenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=PbyvuTWqREEdGZDz1Zy2h_HWLReOXg55XArAxbq1pPOoDGY-DMll3AAQ8VS70lBA0KIJEMEbXnCUDn0fg2lLWkPxDYiXf0wi5Y7WxZdZTJHcmXJj5rVuQU4w1A4m4VP0cKy8dXBUhg7GZ2YIbr4H6l5pA3V5rqfrX25KmjrN0xlOj_8ntiGswHZ1Wj0mhonKVuS6mYTfOsDd5mSgROR94TAAxa6WFNp8gwKc6DxjoNb4d4xeKK9kbymrW4j07tlbZ3ybao28DVeDp858ewQMpPSCaC6ClVMQ-MvhpK2I0OV8JXbKDHKN5ktcq-798brr8oRDAIiNPPiGdAYIJBoQPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=PbyvuTWqREEdGZDz1Zy2h_HWLReOXg55XArAxbq1pPOoDGY-DMll3AAQ8VS70lBA0KIJEMEbXnCUDn0fg2lLWkPxDYiXf0wi5Y7WxZdZTJHcmXJj5rVuQU4w1A4m4VP0cKy8dXBUhg7GZ2YIbr4H6l5pA3V5rqfrX25KmjrN0xlOj_8ntiGswHZ1Wj0mhonKVuS6mYTfOsDd5mSgROR94TAAxa6WFNp8gwKc6DxjoNb4d4xeKK9kbymrW4j07tlbZ3ybao28DVeDp858ewQMpPSCaC6ClVMQ-MvhpK2I0OV8JXbKDHKN5ktcq-798brr8oRDAIiNPPiGdAYIJBoQPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=R5YHn7FhQ5cvEH-1uZ6QZzkkvFbBfwGgQ1yxASelvOjUtdybjZmNKv44VNlcgLE9ouZ3EWNha9hAfTblDR682enUGTUtIzMZzpZas1Fi6eZ-jGJPtfJ9-Nc7720P5qYmrXVQv4yPNrtOOgFSrEkgRdwd9X85Fj7dsJLoLcN96LjRHib6ZozvsMSwvUYNNWtxADePoUz7SBg1iDKJ7AkGl726uip_u-OirAnmKAVXkPQRxepVVfvziuhoZhMYJxnyNQi136jBuX47nK0ZUWuZBg--n6rXwkU_wKJdCs2ho9Sz5Qd2MRw_Zort-BDoyTKEL7bcigpxO2uF0jCkXC6K5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=R5YHn7FhQ5cvEH-1uZ6QZzkkvFbBfwGgQ1yxASelvOjUtdybjZmNKv44VNlcgLE9ouZ3EWNha9hAfTblDR682enUGTUtIzMZzpZas1Fi6eZ-jGJPtfJ9-Nc7720P5qYmrXVQv4yPNrtOOgFSrEkgRdwd9X85Fj7dsJLoLcN96LjRHib6ZozvsMSwvUYNNWtxADePoUz7SBg1iDKJ7AkGl726uip_u-OirAnmKAVXkPQRxepVVfvziuhoZhMYJxnyNQi136jBuX47nK0ZUWuZBg--n6rXwkU_wKJdCs2ho9Sz5Qd2MRw_Zort-BDoyTKEL7bcigpxO2uF0jCkXC6K5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=OJIYlJ3f80B1MrOkzeSUJYwX1YhOvyoHnjhUVWndOnxb8Anx9koCNENtEAvr4z2-vxXrskVvMpdc6BC4AINKdZg13EpwJf-2vU2hkjlYL2tCX2WlBpBCy3ABsP5lvyt30LF01BW-Dnzhdg0Lblbi22TZdbelvprY6XfYke8_sM925MEErt4i7NEIVTRa388auNPwdobZWSFd0-X81yfKUlKGaFImdSwDvZvrbK9WZPAitvnWG8sumzUL2jlqBc6UKHYmAkzMgU_IWfPct82WWTHQSxsj6f3NhmnfV0fKocgjckNVABQcqPyUywKaQMUCla5xS4BySSpnTfz-O7B4snhgT0mLV0p-rwrlhUZwoH53foHPEr8Ld1X9FQjIZr5Tm6F6LimZQcS4ihzaQjoARhCHCtRk12XxXvqwtHWICCVhrHCYB3N6f7YyCKEECKo-qezZjc60mUVceFzfNCU2Gjfq-M3Ky_6oOljuCpCvyKBkdXoGdPYC8jAOwyHD06Q3T9Tq9gEdH-AhJbUZj5ilGQT9Qavnuhlb1-ks1KHPbBWLZ0td4J5wB3Qsq1bdR-hLaCa5x2R3amBA9TSuS4NrvTWfMzJ7ABB8taYr5AqtMQuTf18qkveItgJpoPM3-FKEaODd4SbaEtdeSrJucBocDf0sYQijKpfcb2w868Izle0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=OJIYlJ3f80B1MrOkzeSUJYwX1YhOvyoHnjhUVWndOnxb8Anx9koCNENtEAvr4z2-vxXrskVvMpdc6BC4AINKdZg13EpwJf-2vU2hkjlYL2tCX2WlBpBCy3ABsP5lvyt30LF01BW-Dnzhdg0Lblbi22TZdbelvprY6XfYke8_sM925MEErt4i7NEIVTRa388auNPwdobZWSFd0-X81yfKUlKGaFImdSwDvZvrbK9WZPAitvnWG8sumzUL2jlqBc6UKHYmAkzMgU_IWfPct82WWTHQSxsj6f3NhmnfV0fKocgjckNVABQcqPyUywKaQMUCla5xS4BySSpnTfz-O7B4snhgT0mLV0p-rwrlhUZwoH53foHPEr8Ld1X9FQjIZr5Tm6F6LimZQcS4ihzaQjoARhCHCtRk12XxXvqwtHWICCVhrHCYB3N6f7YyCKEECKo-qezZjc60mUVceFzfNCU2Gjfq-M3Ky_6oOljuCpCvyKBkdXoGdPYC8jAOwyHD06Q3T9Tq9gEdH-AhJbUZj5ilGQT9Qavnuhlb1-ks1KHPbBWLZ0td4J5wB3Qsq1bdR-hLaCa5x2R3amBA9TSuS4NrvTWfMzJ7ABB8taYr5AqtMQuTf18qkveItgJpoPM3-FKEaODd4SbaEtdeSrJucBocDf0sYQijKpfcb2w868Izle0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSnkYLAuyUH0S_C786sX3XsYji34MCTG17gGASx6XzQNvPsqzThYo5wHfenrawgOK6SossLlgxKgoWo4ISPXnfJh8uAZNIcZ1Mq4WVa3Pkdavg4cPDvxJ4TNJFqGHDocnHkfLAqHHGNzQC2iw1_JkpZbqjK-DfgUTK4mTVsInY5KFXuUlBzmM2KWcZQ6zxNR0B4tpMXI7HXmlsKcxr69Ble-9UIOOwpFcl1a23zhzCzIvyy7rH3a8bBDtG4YRDd2AP89uVpXccsoSX2dRd2r2OEjh1fIdwSMgkM1kQ9W_mlAWBwJo8vHpdQAhuYRuo90HEcED75ZScbp3X8ekLDSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=ToufxFp87NFWw_r-OtUrT9Lz5mwrRw89tXG2XQ3nf3ea8UBk8p829xQXc_Uz_seXBGm9hTSBjnUMogyWW4ZFSgCmENxYZgbho6pivO895qyfR5-JQM5EOSZNrQhSFSXBfXw0N0BsCkvOTzjb2p0nO14eFZd2OtojTnPyDzA5eYoLqG-bSsVfeszfDTygf5mcC5v5TmLZbmcSrHmNNus0rutY9jGpeveEb3pmYS65q2Rt7JbWYZkRIkTjeo4S6OgX4v74BVy51spXTtF8Q2DWmkIEtpar2Fugs51aEGkKDBOXb_KA8NAWSfmg5-yoXApGouMgZyLYWK5kYUegTOUcBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=ToufxFp87NFWw_r-OtUrT9Lz5mwrRw89tXG2XQ3nf3ea8UBk8p829xQXc_Uz_seXBGm9hTSBjnUMogyWW4ZFSgCmENxYZgbho6pivO895qyfR5-JQM5EOSZNrQhSFSXBfXw0N0BsCkvOTzjb2p0nO14eFZd2OtojTnPyDzA5eYoLqG-bSsVfeszfDTygf5mcC5v5TmLZbmcSrHmNNus0rutY9jGpeveEb3pmYS65q2Rt7JbWYZkRIkTjeo4S6OgX4v74BVy51spXTtF8Q2DWmkIEtpar2Fugs51aEGkKDBOXb_KA8NAWSfmg5-yoXApGouMgZyLYWK5kYUegTOUcBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=YHHYHauu6mmmSQwVwox9LvYDyJeKg_4O-rQTEffFkokOqWopz-g8EDzXYjFKUozD6VKLxF95VqCa9SntK2dj8IqB_lfKRAlcLOjreW5FNFLqGMPWHKOWMu3HPXtvVBDuZM2-K5x3nf4CZ77O12gHhHjway7R4aYaVMa9s_BQwhYLx9Pgqqe9VrCvMhTsC1-ghh88uDKzXySGX0s06WHeUJFqC6pboFhDRz148m2ZWFFjvOS4gdafSxbIlIZTAfD_mOIfEvR_6Fvi3EQywT1wE6RynAF-kVCyP5Ef9fVdSM_BPpC4_Nq0kVa4v8qG7rj0YtLJtPb6BBcG_A-7R15_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=YHHYHauu6mmmSQwVwox9LvYDyJeKg_4O-rQTEffFkokOqWopz-g8EDzXYjFKUozD6VKLxF95VqCa9SntK2dj8IqB_lfKRAlcLOjreW5FNFLqGMPWHKOWMu3HPXtvVBDuZM2-K5x3nf4CZ77O12gHhHjway7R4aYaVMa9s_BQwhYLx9Pgqqe9VrCvMhTsC1-ghh88uDKzXySGX0s06WHeUJFqC6pboFhDRz148m2ZWFFjvOS4gdafSxbIlIZTAfD_mOIfEvR_6Fvi3EQywT1wE6RynAF-kVCyP5Ef9fVdSM_BPpC4_Nq0kVa4v8qG7rj0YtLJtPb6BBcG_A-7R15_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7HToK1x8ZuRCdbB5xCS4MzSvp8FH-UzHX7zH1poLVkg9rYqjMh0M3vbn2mYA8ORmQAd0jQa7OquKCAMQdKUlkgh3PvtC_rO7aK-hUNZKl75I9pU86Ku99thU3HicIAAMgzqFioW8nHVbclXeUb9ArGHJP4XQ9e4vWhkpBxCT6PBZzZplThYpA74YDvWnEiUPR-1-TtUzVcwDpTI7OjB_N63K3EMJz8H3P8Fjzc8mKrOywDW-U_En30kbi_ZLPXwB_FufZuacFLqh2rKb1y3rBwvEVXHWka854UoC-E7QiWXae4_dU5QnJWytBPxwp76hogvgaTpfhILoIWALWdJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AidVofzG7uePC5GyBao88dP57DIO_9BvUSLotD4tgfB4GA-BFquPe5YYIN4IsASSksPdMUfuR-DdH5aMY3ZxpnIXaLykc8EB7aEK2LZ5uDtd66Pl_SGJ6o3KdTVhHojg8Di1tayvuAJrkvtEKOX8jEahQHIWYCZly5YI5wFa546dBBaa9J2vhUL97zPAiq2Rl_p4LShmuQuuIyrlnWW-gVXgODbIFl043BFDvHPrlWsAzLt_ubD8m6CZC0Cm_uvCijmLTOIHTO1KitsNBUCKbA_SJTKvrylubX8GReM1BPQ04K-j7Ft4-wqOgAE2wFW6lO_M6_Wdpo6YUjRubLYVTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5jM2J7y07iXn3xog704GBoBRv9-AqkNRQu82EhK0NTrsLnp3KwBuVF9VSqRtEha4DlgoeLA7ZKF93RvH3NnflLcHu65Yr6_t2QDt4sqDv3qrurds4eF8LFLntsEa6QSiOffmXQ6brDp4LUYUxUnnD8fCxNiyG45HsfiOZbMruJ65F33JmhHKHIx8Mt3mdKSCbuBDjhnP_WnYuOTc8mRVqB2LP2aN-_H2n6enaF9VIhAAbI-rRHl18ynnXvwftJu3RhqrnRAGBuDgSjO69lzt8ArEEz2NmQ7X-NmHynNJvS_icIQB0P77Vt9ux-qHTqEBUZFObpo--IEyg3Q8D2ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_CreX9b1E1E-7jbVwZ_57nxUg0EG8odeT216_vzDysfupaZFbJeJRvAvfsA6d5vObKl5mSD2GWvh6wJbnVCAc84Od794F4RaITsw6B3egJT5IiZEfsSMng1v0-b_gtTQ52pVG4EwaDTNjNT2v3HWLQcuJs8r7-VTazsSMUfsmxXbfg1Af0fcuGInOwnHdEUBjj-5yNpM5VCnRi5KjHJ5NlLzc-DIkz3MBOB4oOnnpU2O1Zx-seZeecyX3XC6OFkDt7Ao2CU0gcr6bbkT0h6GWLKUJINMIu7OBYKdNkXZ99X3eHL6hYJA5kzDAQdPzs51-Eef8WKAP_NcKXw0fr2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0UE_HmAMEJMxLSRHAMtO89S7QwMd7uM7ahaAqoSXS6gFD3mevgiUtluKEtouAylUGO2iTcU43VWXmjVlkTznXcXMnAiBTbL1jGpJ1CblAmOul96A1FhEm9VDPH5nTFL3PWu8DpMREfvYQZLP7aQnzcVgVr1-2lFdAH6S8pLEFCb6abpXz4SyuqyF8pf5GN6tekSobkmBcE_kEWXMqLiHbP8eX9uZbJ_-9nvescwebiWhHgTrPejM4rY5s3uMBaNcyrx3ggbV4diapNJ1xTOpWtIw5qOqKowe6IfEebbh00Cgi5GPjonvq_W_dlA2fUEYMgrUCZWun8uUNNW0Rl8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7uWsEV2eqcVP2xdKe949x2lBVTdIUcJg9QQCccw7KmL_CpHBaHbf2ANDHf8zyeovrZOIDx0PnRdSo2mlhMnF18SObuukSEUvTUeojV5G3LVvx8mZS2mkZBnxMzuiX9D-IjIPhT1Mk1jaCUhIta9FzDPM1rc5ocQRueF-qmpk3ZgQD3ozaHE-qJ1znxJ8RpJhqgjs_aComXnhIXnGo8ZjZ3QxJaIPPmgWsqCaC7xdAB6AkKsaltQASBa65Q7lY5sZ4J7GOmUJxpXDmmZKXy2z7pME8dQ2ruOO0NLS8IdPWH-wOPPKVEpB4dXpN-upNGgdXYWnoZfghHaerUn6Irtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=e2yWycHssJrBCFlOG16mnDvL_Hpqjh1OyGJVl_5OOlNlBj2J5plQ7F5xQxQnnZG3_uVLIxfrUCRgyn0Gkit8UhouD2a4Na-3AEDD6b35XdUD2QN-kivj27rNDow8w0GI1hh6Y_Dw5iDXveCRWaTtpHlOmXeUgAy4B1CSvBOqeThHFT1_8TlE6SzLGrb6v1N6kqJuDDY8o08irdeb1S-g5IcuPqBQo40p_ghavD8dxQkmTSEZzI0d5AtF_mFWFtwKvIAbC4XHL7PlLLXeINVsoxJWXtooTGZZhDw0e-ppP_WQP82dibNAEDHwbST5uWGxkQOan85yQZ6lErNRVeQGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=e2yWycHssJrBCFlOG16mnDvL_Hpqjh1OyGJVl_5OOlNlBj2J5plQ7F5xQxQnnZG3_uVLIxfrUCRgyn0Gkit8UhouD2a4Na-3AEDD6b35XdUD2QN-kivj27rNDow8w0GI1hh6Y_Dw5iDXveCRWaTtpHlOmXeUgAy4B1CSvBOqeThHFT1_8TlE6SzLGrb6v1N6kqJuDDY8o08irdeb1S-g5IcuPqBQo40p_ghavD8dxQkmTSEZzI0d5AtF_mFWFtwKvIAbC4XHL7PlLLXeINVsoxJWXtooTGZZhDw0e-ppP_WQP82dibNAEDHwbST5uWGxkQOan85yQZ6lErNRVeQGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5i9Vwovw4mzWwPbDQIVe4suvgFfz5CyITVZx7L06OryBU_baw7faiBfH4U31ruO9GkonL5Xp6NtemA0xwJu5fwAZIGYLCAcCxiUrO_tnk18NkTPOl_HCKTEhiEc0qEvV1fjajWPPJC2YNUyHxWYoXNOPUOG6Ab2PKKbwPhUpq0aqhvwqtNCgm-t-pGvO5lSEL0pcCdtDhvsAcMWwh3VBe5AfCCqSp2CANx9PZHzYo55iGHZ-BbkxOlVrfvZF8nFI96lSgPHuZk5eSM9szHqTCoh54KSHEd1nPeVXitATUgky1pzoOl_a4hWf-wTzc7Niq4FkVmNdtHmmopWynBngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1gBCERMXTt0qDDikaXt9y5RfQRY4PqSBLAxVUwegvNh1BNMNpXB5enSnb3h_Y3-qvpv5lcgDkB-XuQ2W0k-oGyhdyg_UOfXezXtrs9GTYN6_yItdq5pImP-UBnnk7SJgMfZGSrWgyut55sO23uYqs2bgUU33vr6H9DVe3RIIzfbp2lBFOuVkpKfbVTM_cP4I7r_DuUKmkdf0wXGv3uW6F-OFww34_uOenMdAr4deGsvi2skdJHlWcWnD7cZ-D6lu607Ee8wlMtRy-ZUA8Cm24cNmRD9Q4wmGBD_uObjqTQ_shlZHMsbx0b0J9RZY6O9kOrdzc-mHRgjRXm3sEPGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsRa69hCbUb7AcXVSejK_nAG11oyRkV0ybpy9M8J0Hzw_pZSVZtGSMswwJWjdszorAwHg37mD_gCLQ1LPEhK01DKwPmJdeU260xjIK4rwKFNzsaQn8cFlG3_6sUSDkHALvrvY33CzMbzGgBkqycY1hRzWBbfu7FTBoN5hcGkym-R7upGTdhYJn2r5CdaOgtuuvTNRPdTPIl9hkQRNnq2h_3wwzuX34UkLUWmLpRvAFpLwRoR2CSIJGElbENEKyP7FNTFb--q3Yfws4nFKF_QLWs60Eq8ZxxEEJkOyOxvFM12hVwUPGEaoXPhfvhIVGwgZN35gLc0x6Nsl8hJRVeOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jA6aj9_HMYp1d1NPjti24q1vyfnAtYv9Fi5chsdQs4egVainfsFMuPw8D4rF9PQXIFugbsdXK_Y0vo-37Yx6MDGvgzIrbFy4SmRgO0jExwx5GgQ4xvPT47thA0AptdbpJqg_unxHY2B2OAMLpZoaQHxSTvCvj858MrBGHcq1h5hROWLMnAUvFf2_59ocdsWXne5jMD5i8RII1JsMncrFlHfDKHyfJtwDzYhL2Uf9pO8XgIuzzJzpJC_8A7HirjurAtlMKZtVIoFTj7oCbIEgejiJ_2cj-Jpk0KUse-8okqM8lJLinacEnNDoqwzf3bgLEJes3lAvArCr74YeFJoKIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gja-mhLuAJzBawJEWQ2MPQN9RQmKv7Uwt462oaIBYnHEXAOTrnIUPFONjLLk0wlMgVXwHabX-oP0WvIWkVPl4acfY8hl7SSet8gVrVLmaBiXPJXKYe2luL7jXTyLbuegFdybBJwRheUkf-SCwaLLYd5tNeAwIMnS5ciAoLboil27yI4MASLbevjRiFVpkeGT90U88f01ILqpb7qJuPuqpKiT7uzdNx7fcw5U8ksjBlPTIPXtXyt11Zagk-noAMtJ5o_qvQ8qd21OL-B-dHBAhizZ387KDDJyz4kgaj-hIUN26dcmYbnKKbmv2ddYeIlzCOwkOT3WHTxdWqE3n_c3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsJqtfjgZ_dirUjU_z6O2MHbh6_tuCDMYiehXXNtCo6_-ZCczIfDqyvdSL2D95zcN3UR3moxHeVo3kCfqJCvSgoKndXd1H_ePsPgD8jnHKFMAzqfenireQK7hfxVQFDVLgX_ilkh5Kb2WCpPuXuW4CuE5r7Z6mMAyheNvSaeA0fBE6UIWVxyqBKIWjStfjMyX0pRglflEIzDR07XdQ_cRpOS1stHMLvKv-V6eIX75LibfZMpjuYnLFXnbQ7isVh_ip5d1uIvivCwpS_9A6uNBi3NlWcPjc2xrOidpoVvMGq52ZOVmUMknmkPnk1FlyikjZ-4HC-T638VGunVBzQJPjks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsJqtfjgZ_dirUjU_z6O2MHbh6_tuCDMYiehXXNtCo6_-ZCczIfDqyvdSL2D95zcN3UR3moxHeVo3kCfqJCvSgoKndXd1H_ePsPgD8jnHKFMAzqfenireQK7hfxVQFDVLgX_ilkh5Kb2WCpPuXuW4CuE5r7Z6mMAyheNvSaeA0fBE6UIWVxyqBKIWjStfjMyX0pRglflEIzDR07XdQ_cRpOS1stHMLvKv-V6eIX75LibfZMpjuYnLFXnbQ7isVh_ip5d1uIvivCwpS_9A6uNBi3NlWcPjc2xrOidpoVvMGq52ZOVmUMknmkPnk1FlyikjZ-4HC-T638VGunVBzQJPjks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPyL6QzreoW7ekN1NHOe4oIahwZrSYGC21OAE9uOWmepWnNmmcjYXUQGU2aob7N2fHhSbw6lCvhIk4QmF9blc90OkeGNB3t5_km_HyFEXc1lFSHaGLo4zsADXEBUWrKQwJ4ANNKrb_Q5tY3pzk1F2UWr_hsq_lw04JM2SFd8OYlhYwZI8RE1HvTNZ_4KB7a2H77l4AiMn5jpFWrT7NL6XBbC9WqKaDidIjNlXOUae_uxO3BY0lTzzX7W7G4JMCczfU2jb9eq-sBgQ4sy1enrJkTaiOy_ZDGLOeiaqlqb-Lta7zu_hfSaGihAR4UM4IHopAtrg7Ui0b8oDN5tP5RTDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6TICd69iraR-1DOqhY70QAwg0vpSc4F9TyEFTL9dO73hC3Uxh7M2Qlqb1c-ewHAjnRHNry_9rsBOWL7aEbcNEJo_KEcVIx5N3_wQ7B2m9LEFO6eVecEqcIGQvhbCew_Sh1vVYQ0FpZqIbS5B56FAFxGQwgHh21Pp7sCY4SdMOgNb_qsLoikagfYhdU-C_LJmu_mqFjjVyMOalO4mplN_SODMEDrKJkMtAiaj00QpCpB56hv-Lgn4bbtRDIpPVFqttfsbE4uTwu9mDOJUtMc_kc9RUhNb5jJ1wpfnm5bJ-psspFsHYkxfBEqtfOn9HxHtg47cr5xU0coxdDgij1cKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=BS0fg5JWqAVe1A7IYHylv2bWlAxWr4ObrP_qfSwdVBS5EKka-vliIgGUUgP32uCwSBnbvPy2-eC4umTYn4HoAXDNBkX6kz2dhIzBmBe7hvNNEBsMCvyU21noXu_H8arJvz6MrGtVK1qb6r2FmVjUdd2hF57V8hCPe5t1gGOnF4vkddcwUbuWRPqtR831mA0UiHg7u_ley6ongMkrGIg_5C6pJ0G-UsFohWRTPeedhxkyOPPsd-7q2KFcfQwEafriGIUmjx2Ec6KyjQnicFuiS8xjHqMGj0IQsK-SF_FMtO6AAWRoJLr4Tcm74L09wMUWtTbrpXZS41anRjb-yagqng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=BS0fg5JWqAVe1A7IYHylv2bWlAxWr4ObrP_qfSwdVBS5EKka-vliIgGUUgP32uCwSBnbvPy2-eC4umTYn4HoAXDNBkX6kz2dhIzBmBe7hvNNEBsMCvyU21noXu_H8arJvz6MrGtVK1qb6r2FmVjUdd2hF57V8hCPe5t1gGOnF4vkddcwUbuWRPqtR831mA0UiHg7u_ley6ongMkrGIg_5C6pJ0G-UsFohWRTPeedhxkyOPPsd-7q2KFcfQwEafriGIUmjx2Ec6KyjQnicFuiS8xjHqMGj0IQsK-SF_FMtO6AAWRoJLr4Tcm74L09wMUWtTbrpXZS41anRjb-yagqng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yx6EqZwwv9J9qkLYcmeR0OsbH3mjtNVbzK0Zi5Na-Zolm7HOA-ST5nJauZw0mRoX-beQFhxa5i4lIaILrNllU97ixVlTzqrlp6NrsU5efth0wYi71N-YHgqpBpDsF6JAQt1WboB5_zmYPFtKwV6perGh4mlt7KcsoRO32XpVT7IV7L_0jSBaHJ9eW6yYHTscnJ0KVFSJ7gARnYBcGjOn-ujdLPvRW5qkz6fbCSzEC-fH5g2WnBRzjKCOYrKZGZViWBb8dVUibEvVuX64grtogVPPO6eX04xlBR-IwDDa9DXnvyVrN5YvptE8XblwtIG288iiiO5oH40TnViSBGQ6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=t2wkkMUrylQlZjyyagrOqt3zGA8kH6gALY68ZPT7kmTMk-Va-voLU2Mvty-V0CwP9pYyuAfNaBhEjb0jqZcbjTGq29WWLZ1DgQpmFU2jVK-cD1viTc1RorPvdfG0u8aaOknDsNAR52-OPMjbe_cBQvXDfE0i3q3gTYmdpeBnHH1UBr4d7NRc2ku_q7P_ksYWfWBF1_26Sr9TY9d8mj46orbM-1oIPus9oj90ag9CaGvYDuwqF4l_xu_wKK104tEND646mUOY5zfzGr3VIbppkKuomdvL-K1Nh6P8xibXw34n1DBgC2hrkRbDEqiHcYm8cN4qFvPm2Ki1DUl9RRfVTL23SiUEFvbW7pXrf6jLjK7LEE3VPZzdKJ2_m8McNRxx_jUF5ug2em5MroeBY7E44inPxBVfwtJwEwHbaiqm9iDwoIiYbo51SAIi0V8mopBvVf8aPe0dDkoZ-U3Arzwr0oxZ3HB1tUtEBQF9uVTy7AdM8fRwOLCEE-SrNkmRIw51cIXQsiIFpfzYmiByuQ-t6ytAaYb0NcMDEV7O-SCOmnXB89mTK_0uW4UvJ46xMwtVewNUJ70Omg3A7K-CpAsvNO9Nyqcn6ff4qBgOREZ6kPNlp-x5Tar7hAU5k46YDwRxm8TnXrqzlUpZEZlsbVrAkcVxnF0tx99pQK1493L68f0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=t2wkkMUrylQlZjyyagrOqt3zGA8kH6gALY68ZPT7kmTMk-Va-voLU2Mvty-V0CwP9pYyuAfNaBhEjb0jqZcbjTGq29WWLZ1DgQpmFU2jVK-cD1viTc1RorPvdfG0u8aaOknDsNAR52-OPMjbe_cBQvXDfE0i3q3gTYmdpeBnHH1UBr4d7NRc2ku_q7P_ksYWfWBF1_26Sr9TY9d8mj46orbM-1oIPus9oj90ag9CaGvYDuwqF4l_xu_wKK104tEND646mUOY5zfzGr3VIbppkKuomdvL-K1Nh6P8xibXw34n1DBgC2hrkRbDEqiHcYm8cN4qFvPm2Ki1DUl9RRfVTL23SiUEFvbW7pXrf6jLjK7LEE3VPZzdKJ2_m8McNRxx_jUF5ug2em5MroeBY7E44inPxBVfwtJwEwHbaiqm9iDwoIiYbo51SAIi0V8mopBvVf8aPe0dDkoZ-U3Arzwr0oxZ3HB1tUtEBQF9uVTy7AdM8fRwOLCEE-SrNkmRIw51cIXQsiIFpfzYmiByuQ-t6ytAaYb0NcMDEV7O-SCOmnXB89mTK_0uW4UvJ46xMwtVewNUJ70Omg3A7K-CpAsvNO9Nyqcn6ff4qBgOREZ6kPNlp-x5Tar7hAU5k46YDwRxm8TnXrqzlUpZEZlsbVrAkcVxnF0tx99pQK1493L68f0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIQSh_XkZC8qnfLx6pXjH74g8Yx0DH4f5W6jcMQDfFn8ze9Ojtb4kt2-90Mq75kqu_owTPYTY9u2Fu9hzKX4LLJokvMFxJARXJaf5RjkI9mzY0ypgOJJbUgS9MffIOAmEbCM8jZcLxLLvYDKGhrXgoLR6Wm9ugQuCK2GtCuaY3WaER6NHLkkgY6E3h_JaxanN0Tez9_1Lp58HGNkW2DlMAy5N2yIU4QSB2x1AuhnLOIvJeZSA02J6fAOe83z_6Q1308l1ewLULTg3LeL5yI1nVdc5RY_WtVcK-xzR2Hpv0sk_Nc_p0XwkYBBX-HDWLWy2f07CbY-Gk9HNl58YyCCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuG9cush1XDI7PhY1GXEiB49JGk4Wy5sfqLij7gFHBx0__l9uFsIbs-Pdy4Dj4o3nV6gYJY6KZV4qYE_9q95VW6D9B94QBEPQL1ZqnAaEclnJm9onmLWPDzyU6thz-TIltla0vtB4bvGvlORU28CxgeMdXUBuLMti9OccgVnIRUkaXi2PvjMpEgP9XLqR0sHtKjrvRVgjz-9MsFKhoXVGK47vEOspjIIGQqsQDmT3Gk1Q6s85l38Zbmnz77xoqyQlLB49SDAKMSz0dFHJuh_xuYjtRkkHdXn4MxoLn49ckDc0tFFlsfZs4_HEuoFep4muRMK8Ab90nB4Q-yE-CgkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrGooCbpFrW-hZQlHYeC1QS2wXKKX4WLYeDSbJQig9z-VESEKX4hDV1if-onYDGOH_ibArwD9_chZKf8fbnL1-rSMHOjSk6_oSzROWR8k2dMctfLZHznLaHJBB1XkK2coB0LZs2wVgi-zYThLMdRL4KYozkovPg6gba-ZdMp9ng9t4mRy8wKQNBhri3qG_OHt0sut_EBbsvi0WWLHIUhGZfPdCfPuCizkWrGosnZUtHRA2h5Dnvg7e60Dd87ZFjNECsHHx3WInQhVaUt6TH8PDTqr-oP1oq980dEv5xxeQq-B8aCLnjiszjR8pMvyCiAhUa24BV77QNN4Tay0LxnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=P-YZs5hicSSbTpqcyZH7yufm2xz3adx10qMS3FihQ0QcVWnxjZl0jN56kwtyVaEp_6HTUEo3ZIVq1Sx9vv_fOPXbCzslemlhR__hwpNl2k8ECqSHp5dUPTf74hE6EK4pIAyxXHdxsS7jTcCjBJqUvaldVklfAOvslwNekroBeQgm8CMnL9uRi-gP6JSZkz7UVsve5dUu5XSJSrMIkXqgsbW6jg-9ANNxEiNTupu_z6aXHkg3WWUPKhkymKVwMPjYkG8YWt_I9m14bDyCagw2nK1g3iZZ8BpfquBJEOfFsxWwHSXZRXEs6zVOteUv9NSwpBfkb1gsJcXc2rxW3aj1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=P-YZs5hicSSbTpqcyZH7yufm2xz3adx10qMS3FihQ0QcVWnxjZl0jN56kwtyVaEp_6HTUEo3ZIVq1Sx9vv_fOPXbCzslemlhR__hwpNl2k8ECqSHp5dUPTf74hE6EK4pIAyxXHdxsS7jTcCjBJqUvaldVklfAOvslwNekroBeQgm8CMnL9uRi-gP6JSZkz7UVsve5dUu5XSJSrMIkXqgsbW6jg-9ANNxEiNTupu_z6aXHkg3WWUPKhkymKVwMPjYkG8YWt_I9m14bDyCagw2nK1g3iZZ8BpfquBJEOfFsxWwHSXZRXEs6zVOteUv9NSwpBfkb1gsJcXc2rxW3aj1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXLIXJsylE46zBPeUkK5t6o-8MMTnh6l8GiSgq2j_bMLijKh-bFr0pq4GzcOXhVkwB2GHvFty8qjt9JC_qXNpC70ESlzF7pzosHtyDABCye3AVljo4722ooM3-rbJR2E_QwNX-Q3ZZLrjxxn6Gc8x3Rpnzq0iscYHHNE3_lzBySr_MjZirGFd-HPR6xKnkxPWVExjwAX2gjN55H0dkWJ2rQGb7Ez72xMdJoTIww4PGKxfwDv0kbVLhsQQ9B57Mmfg2Q3KoS79B-HACEjlDcZqytUiR-wIOfZqq2_AD1ieiyiZC9evrPY6-DpmLRf9rPTNw3Af8MFgjYCLV0rX3lChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgelNKtsgVAa0CXWYeS-GvAUFlUm7s0-Sggk6Qsz4HrzYA7aSX376plU9DGUdRluWxJwj7-CY3vJMMjzx4VVt2Wpy5JxwNNQcYk2rcltJ_6vugEVxVvUjiVSC43y_8OJSUHBwlmh56Lyumhd04mh6P8sdtAekP9QJ-UoqawdfanCLnrCc93kIYGkYuSEI8Wjy3gmLVAx3sXqU3sofZWS_exD07gVwxtq71JnXmLJpSzBlYanrY9WKIfBVetXb-x5VhqCq2gTqMfg1WWKL1wWF3oULWVqY20ng5BxiTqYII6XIv7yHRO6fpL2FuQ7u78A-77jXMd1SbkEUY1QXj2DbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFsvH9mJQefS4OIrQDYLQoWfID5Qek_mxPb4hNjYkai3lxmA-c_OP7tY_6OtnuneuAXi-69W2SJXwwlN4Qzd6caeezwrI8hkYt9bnMAxGbs1MaJRr7G8cEPsUOHnB5qlax45G7N5uXiV3GQorrsMvzzOeMhmHEpiU_YHgtyD60oferV1fsLRtYZ5PHOu1FbtvKrHUuy2LT-EQvjzB11ZjRCrLQESO4uoNpC6LPBQvGWnapOmOzrW7MjDd8Tt3N1P0FEPDHVOoA6kc7bH2BAiwAAjlu6p6NJtymZ-LltutB8kvRjNud6pZYVLS3gq14JVHfQSLkBH8Yz8pClp22tDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=VK62M5i3mhY5FOoEKZYyNt6ysIh26dQOFlR0dPsG1hufR9XDXByo1FOfZJRqc0xJ7yBL1HpUOAG-RGBTrcX4NTCTv32mo9dipf1rCWATsK5T5ctx5FS7xekf434u8Me-33-dN4CazNWmVDXiQIzpl9IAL76ViqNVfUHRhTehlU-VPIwIwGa3NvJt62DZXd0Izlcpd2wRuKt04z5UNVBzQyAt1Yros9mJ2ukuuoYSTvMhv2oDSE1hHXhzXuGzxUGDgxBGZbLrAmiBDziGK2ig5l94AxNr_3ZMcyxi-39GtRDzlA_7SCLjviFNtMXVksn2UFecXk5RttKfAQoNUrGWrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=VK62M5i3mhY5FOoEKZYyNt6ysIh26dQOFlR0dPsG1hufR9XDXByo1FOfZJRqc0xJ7yBL1HpUOAG-RGBTrcX4NTCTv32mo9dipf1rCWATsK5T5ctx5FS7xekf434u8Me-33-dN4CazNWmVDXiQIzpl9IAL76ViqNVfUHRhTehlU-VPIwIwGa3NvJt62DZXd0Izlcpd2wRuKt04z5UNVBzQyAt1Yros9mJ2ukuuoYSTvMhv2oDSE1hHXhzXuGzxUGDgxBGZbLrAmiBDziGK2ig5l94AxNr_3ZMcyxi-39GtRDzlA_7SCLjviFNtMXVksn2UFecXk5RttKfAQoNUrGWrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu9c4ZF4_lQT2eLJNPnEZCCmRLBZmYW-m6uwxuplIo4QZt1l5v4ik8kj49QSSk2cEfcsAAfc5uQm2GeC3uT1rPpIQA8jADEq9ZjVTO83gVefvueFlSuDV1p9k1f6KOmtMgF_YXjto2CUulG0aFTQRMzWRiPyaGQL3IBxYXtSFwaEUu-Rz7s2nlqg81fZ6q7b0qr3XqYt9jfdyYN8Y-cST0EM3qtyFeRpPShuLBexjP7zF3xK4K3TzaCmi2BfvjgfxB4TcZPjEk60FK1CqI6Ed04Go2kWrA4tFnVrgq9zF8wGU1aCqlEMTIbu6yPm2ODew_HEjRuc23yPZ4exBaF_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMgLL7ay7iMw1P98HEXK-aXg5WqVfAn_faYRedu4fNJSpGWOWAQlifC0YmMv2pf6oMgewUOBTyDj0nGWyZfK3svaGlJCuTrNZAjDJ2gMgN3OQo09KAGr9DdjXvYkTjnBkkeCXmjugAiT4yqJ7bsq-KJ0Act5uh1kOn0ne6XflbR7YXE-7LjAmds2VgQcDyjbynSOtyM86Yzwj1W6Dj1Mo-3Xjjl-W38iMQKJ8qB9M7SqnvKDZMbezOgY27RL2DdlvbyresQDTiy7MPB_7Q9NPjMj9ri3VaKy6NiH_YRqbZISsmgTSjG8CfbPaMLnRoTUqgJeQr0GouvGgDpLbEZiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-PKgCeeR41sPvwS5dp2rO963ThQ7v2vjzpyKZOnH9MQWlvn4U5rBq97HIyVgFFFY0GqlGfq6wG6zwR1as9ZWwuzxnJE1--ULcMuzKjHUHzSO23x8E1cdwC15hcq0R9RoWjw6kbVWySqlinXaRtjjA1UcmgugrYeCI121ISNprxICpPBC5CdAs7-oYcND0IdVFcRD_dWQl2UTrOnbg7a_BO34aDk1q6IapwL-xe3frlb8KA0EFvN3xg5vOXZKIvP_Fsd1R_EWQZ2Pfxzf9tnXgdEhb_WPebfpyLmNtc5zotngObga2oFDsaMnJ7fpeyabIQ6wi8va4c-Z715nOCdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLfQQzuaILOl_ZYPTps8nawf-ra1hFhUnB5Jow3Ro_InJjJdJ_z1q8hqyHkuE0uyfe9SewnQJIsg_0-1R4Yv0lzOPs7x3r2btvFwaZFcpK88Z8BtqPDzZh2lUXfPlB6IxZXRHNbiuyjPAkOHgCNEsGi7IlKPM5DWmN_qSNBGlEjocziATFg4PNOZayhNAU-dx7q3wrwHzmHcGRPO40TNV2A4XB5s5TRA5KEL3_gRG6wxLxY4t3w-kTPEwUyloOuC8L8YRjrIpE1Pgju_Doa0tEEe2-ecxZGj6xDASJLQuBrvfhZviQIKYjZBqzT9SjEkgmECYQjEmZMYeO-Rq-gYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgFb4Z9pS0CcSUkywD8xFETn1IGATj64ouVivy37K06f7lUspOCdxOJsHnxmarQ_GqTXI0z1r_DJQ_24xlaqxZggfv_M8XrkatUJX1UtvwnIfzpcor7k1zW0U2kM2RXhzk_DvlPF52itpZ7IOHJ9pdWMSO49G0OBGVOXeYbsMw6UHlxRFCpDEKEaRAV3t0ehKd_imYDY3EfUbOt_gs09yo5aiT0Lhp142KHbDYb6ABgGdk8gOPljyK4tIjAXfchTcIQVQ0JIk8g9Um7xBpzrdWNuo_3bYSX9W1Xup84iKRi681AXrLiQMx3uLclfBm93-pFR-87iDQ8TMLjW6e1OMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o69d2bYdxmnn7zRQcOkcphlJi3VwihKSEFBXob1zcTqf3N-I0vCruygiky7CReAeZzoWNrUmvrkVv-5quGs9br80z6EC91C9HjcQ93_eyOJb2xi-0K-8EyvEVcUt7rRLl9MB7U1Jh2rvfawWQM4FGwq5C2nsiaL202HAI7sATBW_SgDRIs6_c_f35_zI9P--d8wp39wXd5vrbG-_8NxfzisPFWbARz1P6UWemz6WjywhQ0oiujl73f-Ke5VqyFbwM_hPZ734SPHP6Qr3C6_pKsPLoRtiAIAH-kReWPD1J_o-MUCxoYvNSgUNMa_VRUvuXfgHhpvh35LnAXL9gVpRhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfiiqDmoqWIneL_V7bTq0wlkMgK0sv_FXDSMPppS85_ZLDrAw-UKQZjyF-gmgwx0-AbdgTZaKhN7subZ8BIkcviwPEahK6CvSPpm8EDqtrTrN6oG-jMsWsKpk20F1_rX3nE7VD_UV-c1VM-EeAkmLg10vNat8S9GTReuSAu7QysOltoGgHsupk42R0K5apXVLBFvRpOyxaQFIwJqpvf7ljRdJ2pPW2P7-lN_8DRoxF75hCCNAPQGuIpQM743hcAwhnyblOLAW4K2BYECl2Sly2yIeQqcyuM2IMM7iaup0nkBvocx2EDnxj29rokB-gIfoPAqYE4iqLMHN1cCN7H5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
