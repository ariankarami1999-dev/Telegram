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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 02:22:15</div>
<hr>

<div class="tg-post" id="msg-668158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
بر اساس گزارش‌‌های اولیه، حمله امشب رژیم تروریستی آمریکا در استان هرمزگان عمدتاً تأسیسات و موقعیت‌ هایی را هدف قرار داده که غیرنظامی‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/668158" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca00dc6e4.mp4?token=d6fMQoHIl-am9nS5Aw9QWfvU80LOlvlaY4MMIgEEqEwg5D8__yohrYOebOEfRAXSG1ps7-AKfBDH98POElGSPT7bKLl4tEbYtS6gbo4sDgr3yhVpLoUp2q2GLz1KFXCI0nG87BUchS7It0CLrtGrP2xNjzo02rONlnj59KjfZ4PFs4TTPChDYC7cKRL3CzVOsaEcZRXgz9U5fNfLIJUajcqFsraffG0bmCxHt7jfTXDXVPrI-FfceecUroCrzZRZIn0DB8i32pSy28LZ2RCRLQs_H2kaL0gwwLKSPOYrxVHKGR3lrGjY0--daeNl3zJPKg_ANAEMk8iw6mLypCKoSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca00dc6e4.mp4?token=d6fMQoHIl-am9nS5Aw9QWfvU80LOlvlaY4MMIgEEqEwg5D8__yohrYOebOEfRAXSG1ps7-AKfBDH98POElGSPT7bKLl4tEbYtS6gbo4sDgr3yhVpLoUp2q2GLz1KFXCI0nG87BUchS7It0CLrtGrP2xNjzo02rONlnj59KjfZ4PFs4TTPChDYC7cKRL3CzVOsaEcZRXgz9U5fNfLIJUajcqFsraffG0bmCxHt7jfTXDXVPrI-FfceecUroCrzZRZIn0DB8i32pSy28LZ2RCRLQs_H2kaL0gwwLKSPOYrxVHKGR3lrGjY0--daeNl3zJPKg_ANAEMk8iw6mLypCKoSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب منور توسط ارتش رژیم صهیونیستی بر فراز ارتفاعات «علی الطاهر» در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/668157" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668156">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
المیادین: توپخانه مستمر اسرائیل حومه نبطیه الفوقه و مفدون در جنوب لبنان را هدف قرار می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/668156" target="_blank">📅 02:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ستون دود بندرعباس ناشی از حملۀ دشمن به شناورهای صیادی مردم است
مدیر بنادر و دریانوردی شهید باهنر و شرق هرمزگان:
🔹
دود سیاه در پشت بازار ماهی فروشان بندرعباس ناشی از اصابت پرتابه های دشمن به اسکله صیادی بندرعباس و آتش گرفتن تعدادی از قایق های صیادی مردمی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/668155" target="_blank">📅 02:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85279956.mp4?token=NUsd_auz03zc2OoEfUyaZrz6hE8QbRxQ8omQyz74RFgAKbVB8UauZkj9byW5l0fFwMLQyaSxIahyqNA5U0mV9MyLFlDVI0drTM1yQFBn0crXwBZa_7BiIbF59Dxub2NzJ96osM8M5XcXRZhQtdTYz2vGl7fEAHwAa_1uAuSMkHB-17n50H662ceRtZ4ebWe86Sf6nfcpKKCcXMDR11BnWw5FitoQ-yTr5IGxoEVc8lZy6_dYhgWYbkcofHmmJ4aUSIHw16r0P6yVsvatmb8TrZ-FBxRUPrx_avyYXJuL1uquaBLSdNLjEdeJzGVAIAdW4fJBT0Iv6GMfZB-FojbIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85279956.mp4?token=NUsd_auz03zc2OoEfUyaZrz6hE8QbRxQ8omQyz74RFgAKbVB8UauZkj9byW5l0fFwMLQyaSxIahyqNA5U0mV9MyLFlDVI0drTM1yQFBn0crXwBZa_7BiIbF59Dxub2NzJ96osM8M5XcXRZhQtdTYz2vGl7fEAHwAa_1uAuSMkHB-17n50H662ceRtZ4ebWe86Sf6nfcpKKCcXMDR11BnWw5FitoQ-yTr5IGxoEVc8lZy6_dYhgWYbkcofHmmJ4aUSIHw16r0P6yVsvatmb8TrZ-FBxRUPrx_avyYXJuL1uquaBLSdNLjEdeJzGVAIAdW4fJBT0Iv6GMfZB-FojbIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای اطراف حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/668154" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668153">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
روزنامه صهیونیستی اسرائیل هیوم:
ایالات متحده به کشورهای خلیج فارس اطلاع داده است که باید برای پاسخ احتمالی ایران در ساعات آینده آماده باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668153" target="_blank">📅 02:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668151">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
خبرنگار صداو سیما در سیریک: دقایقی پیش، شنیده شدن دو انفجار دیگر در اسکله روستای زیارت شهرستان سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668151" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668150">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99baa6d07b.mp4?token=hnctG77R-th4bJU00Bvu4y16IIagFOOvEjE4Lkj98lRnVECwV5mKPIwaSe1D2olvrbVF7T5A-9i0VGQRxi0bhFglyB8YksN-XgyRpcqwBYoXPtxem3JAF-T_61CUrAP0d2CILJ5f2SV1ajJLkWKbuxC_cucIoKmil_qc6fDtYWWi0hjvzFBU2r4RnvTT8PXLhOMWPzq7TfIh9ZFzmHlds9doGc8HpFMqBoSINVBycBla5wj0p0vRLiaQeta48vhBPdoSG_76z32QeCjVCoyeNcAINV1WgWMVwOjJ0HX3rPX_JsAD8aTruhYQHnybD-Gv1Dkt_qp6Ve3yELRkwYkn_2Qb2n2wtTgLeIvDTSHW38VgEymquLdWUmOWLzpbKlrBxpu04UBIWwU6Hk2SPphKmw4_Hb1s0s8GYoA505IJ_QfqtSAjcM7nk54EmhR7RUUy3BlB6S8T7HWu0AWFoaDVC8Yn0sWIXq-EHTZInk0ooyOOOHJaJjvFrbAQkc3l1BSTbaPa0e-WKzvrCfzoGiynmTmxVMNxWhLnAHrQr_6Kknqa8QdHjcEGykNvz52u5J3naZnelbeHYZNAM1uk3_X5kOk0WTtXfM4LXIRgP7HRhamV6Do-w2DKOONAAEq_dDiEG1JEOaLt1gQ3OvlS3XghqN5Lg8ARkKhi1JN4iH7srZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99baa6d07b.mp4?token=hnctG77R-th4bJU00Bvu4y16IIagFOOvEjE4Lkj98lRnVECwV5mKPIwaSe1D2olvrbVF7T5A-9i0VGQRxi0bhFglyB8YksN-XgyRpcqwBYoXPtxem3JAF-T_61CUrAP0d2CILJ5f2SV1ajJLkWKbuxC_cucIoKmil_qc6fDtYWWi0hjvzFBU2r4RnvTT8PXLhOMWPzq7TfIh9ZFzmHlds9doGc8HpFMqBoSINVBycBla5wj0p0vRLiaQeta48vhBPdoSG_76z32QeCjVCoyeNcAINV1WgWMVwOjJ0HX3rPX_JsAD8aTruhYQHnybD-Gv1Dkt_qp6Ve3yELRkwYkn_2Qb2n2wtTgLeIvDTSHW38VgEymquLdWUmOWLzpbKlrBxpu04UBIWwU6Hk2SPphKmw4_Hb1s0s8GYoA505IJ_QfqtSAjcM7nk54EmhR7RUUy3BlB6S8T7HWu0AWFoaDVC8Yn0sWIXq-EHTZInk0ooyOOOHJaJjvFrbAQkc3l1BSTbaPa0e-WKzvrCfzoGiynmTmxVMNxWhLnAHrQr_6Kknqa8QdHjcEGykNvz52u5J3naZnelbeHYZNAM1uk3_X5kOk0WTtXfM4LXIRgP7HRhamV6Do-w2DKOONAAEq_dDiEG1JEOaLt1gQ3OvlS3XghqN5Lg8ARkKhi1JN4iH7srZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت عراقی‌ها به سمت حرم‌ امیرالمومنین چندساعت مانده به اقامه نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668150" target="_blank">📅 01:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668149">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای رسانه صهیونیستی اسرائیل هیوم به نقل از یک مقام ارشد آمریکایی: اگر ایران تلاش برای جلوگیری از عبور نفتکش‌ها از تنگه هرمز را متوقف نکند، آتش‌بس در خطر فروپاشی قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/668149" target="_blank">📅 01:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نیکلاس کریستوف ستون‌نویس نیویورک‌تایمز: به نظر می‌رسد جنگ ترامپ با ایران دوباره در حال ازسرگیری است
🔹
علاوه بر حملات هوایی، آمریکا لغو تحریم‌های نفتی علیه ایران را نیز پس گرفته است.
این موضوع صرفاً یک نوسان یا اتفاق گذرا نیست
، اما دست‌کم برای من هنوز مشخص نیست که
آیا ما به سمت یک جنگ تمام‌عیار بازمی‌گردیم یا وارد سایه‌ای تیره‌تر از منطقه خاکستریِ میان جنگ و صلح
خواهیم شد./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/668148" target="_blank">📅 01:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668147">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782ab0c59a.mp4?token=bfcTiurzzmi-cxym5z7-PojDowBUEB568u6__Q8zw_mtGOgQd9mKAnx7kaT0lnIzrP7aVFYYe3DuyOQQpg55YLlwVRo3zkHy_EUrAqJEs3i3SNwYel1xkX1RnPZp38W-pifFWCU3DorjIcDHJUm1dX3Vb_dDKHKIC2vTvsGug6Rgdl2uDrTt5ei04oFdGMDSxxDaEY9nPr41DnpTIciCgganXWIdl4p7iob3908sm4dmhBoRgxsMHNZAI7xMfdqeVlLcGsav9rXT8OLwi0P2pEW5bN8KzM-VLKLCfFELgiyGQAz7Wn3RyE03yLbvq17dYr3Upe6eG6LwVdnvFxQ3Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782ab0c59a.mp4?token=bfcTiurzzmi-cxym5z7-PojDowBUEB568u6__Q8zw_mtGOgQd9mKAnx7kaT0lnIzrP7aVFYYe3DuyOQQpg55YLlwVRo3zkHy_EUrAqJEs3i3SNwYel1xkX1RnPZp38W-pifFWCU3DorjIcDHJUm1dX3Vb_dDKHKIC2vTvsGug6Rgdl2uDrTt5ei04oFdGMDSxxDaEY9nPr41DnpTIciCgganXWIdl4p7iob3908sm4dmhBoRgxsMHNZAI7xMfdqeVlLcGsav9rXT8OLwi0P2pEW5bN8KzM-VLKLCfFELgiyGQAz7Wn3RyE03yLbvq17dYr3Upe6eG6LwVdnvFxQ3Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای حرم مطهر امیرالمومنین(ع) ساعاتی پیش از آغاز تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/668147" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
برق برخی مناطق در کویت و بحرین قطع شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/668146" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رسانه عبری کان‌نیوز: در آمریکا برای احتمال چندروز نبرد با جمهوری اسلامی آماده می‌شوند و این موضوع با کشورهای عربی خلیج‌فارس نیز درمیان گذاشته شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668145" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
استانداری هرمزگان: هیچ گزارش مصدوم غیرنظامی در حملات امشب دشمن آمریکایی تا این لحظه نداشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668144" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی به سی‌ان‌ان: این حملات «تنبیهی‌اند، نه متناسب» و فعلاً هم تا مدتی تمام نمی‌شود/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668143" target="_blank">📅 01:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHeRdzUX4dwAJ-ZZYarhyZjRbh7WjjGtdK-vkIX00oHKWea3FsQ3L9DBuORuaBZ1J-lkrQcYHWRJw7dNFw-ikBbHzTI1WhVst1wnI6w5dbl1UvJ57s8QtN7wZcqmrbz-mNWa7aR3tTqFnwYn1kBFFXv6PD5NXDV9uPwTua-hcnHR-VChTxuS0InhA4-ex8Jf7oQnjhta7VJn_KXa_nIVuRcESmh_UqhRV6hVuqI2s-pxyfs9A9fxSJA2avX7tKrsoU0irzxe2LO_98imUxzcUMwG6dJW6KZ9eid8lxbSB1KLqBEtKFOGYFMM3hNI7Bee35cJQ-VNdjqQKpiReMc4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشمن را به زانو در می‌آوریم
🔹
تصویر قابل توجه از آقای شهید ایران که بر تن جوانان عراقی نقش بسته است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668142" target="_blank">📅 01:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56dc51f77.mp4?token=bQhR0rnNsCBtOlRMSw_wldO0Ycw7d1wnwiUg4nLt3H00alqhMZcJtllrBnzvG-RotBsTTXoxuRDWBymGZ6DRaRoAv1DsB-MI49Dcvk3e55wpIu8FF04hfK2usWAXpdggB1jVB4IzLd8eNl2S17N4eAFHHPhCDRerdSbJsnO5gGAGP_iWfCyaAmU97LhMWSUjTzUQjW-rBvkqbEqHk_VkvGJ1SODM4iC73iGUeqIN-k-fnTxCy0X21LrN2AJEKMwnind6M3W8wQqF1BN43K8zdhPmhaF7fZCpQAyZPFv07Qs6IFNFWuqxP_JSFc5ESJzic7RFYyw3gBP7LIs6q6getLVkcL0bPiU7tizppQOLRrZ830mjIaQh7CeYxfPaEkbFEvqD98uC18h0A854o1DLEccgMi2Ae4cZrJGTzL-b6MvjjZY0wjdqFm3AcI2smZrl5xlcE4az2ER17hg2PvfbqCVleLWDFNy8JWFIuFyyclqzsQ4bKtzAe9lTxN7W3SMlTuz5RAHmijpH8n_gfQg1VBj9VNvgrd5zP2Xo0TAmPeSJbnkmsDb0pfkhpf7tsqrFAeMUezQElmRizrVYuqHu1RTQwMdjirn8_-7oMvmp0-bK9pcn_f66A_9Z0j8fDwVNFvSIY1iHFHWorMg9nOXmSVHPMNRk1SlH_Lv5WUlDwjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56dc51f77.mp4?token=bQhR0rnNsCBtOlRMSw_wldO0Ycw7d1wnwiUg4nLt3H00alqhMZcJtllrBnzvG-RotBsTTXoxuRDWBymGZ6DRaRoAv1DsB-MI49Dcvk3e55wpIu8FF04hfK2usWAXpdggB1jVB4IzLd8eNl2S17N4eAFHHPhCDRerdSbJsnO5gGAGP_iWfCyaAmU97LhMWSUjTzUQjW-rBvkqbEqHk_VkvGJ1SODM4iC73iGUeqIN-k-fnTxCy0X21LrN2AJEKMwnind6M3W8wQqF1BN43K8zdhPmhaF7fZCpQAyZPFv07Qs6IFNFWuqxP_JSFc5ESJzic7RFYyw3gBP7LIs6q6getLVkcL0bPiU7tizppQOLRrZ830mjIaQh7CeYxfPaEkbFEvqD98uC18h0A854o1DLEccgMi2Ae4cZrJGTzL-b6MvjjZY0wjdqFm3AcI2smZrl5xlcE4az2ER17hg2PvfbqCVleLWDFNy8JWFIuFyyclqzsQ4bKtzAe9lTxN7W3SMlTuz5RAHmijpH8n_gfQg1VBj9VNvgrd5zP2Xo0TAmPeSJbnkmsDb0pfkhpf7tsqrFAeMUezQElmRizrVYuqHu1RTQwMdjirn8_-7oMvmp0-bK9pcn_f66A_9Z0j8fDwVNFvSIY1iHFHWorMg9nOXmSVHPMNRk1SlH_Lv5WUlDwjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/668141" target="_blank">📅 01:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
دن لاموت خبرنگار واشنگتن‌پست گفت که حملات آمریکا علیه ایران احتمالاً برای چندین ساعت ادامه خواهد داشت./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/668140" target="_blank">📅 01:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حملات مجدد رژیم تروریستی آمریکا به استان هرمزگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668139" target="_blank">📅 01:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f3f14c10.mp4?token=FRrCtYdsJnNEWyrINo03PyFfMYpXw1bk-eCD86lXnVPKfjQB42-ZaSG_B72M0Soty_mvarYVL3jxvrrJeKHjj4rK7mGdJJddhR6AzgkKWA-CsUkFyLHTn4O8GrG1qdzwIt7SwTrVWbUYtJHjvuN6zYkDXvABTETPVjvKhwb5MQkSA1TUUIgd-sOqoVnJvOuLeaTiAf_DGj8Q85BjmVnUcBFsT6h0UAHui4h-bfrUBlcnJN2O7ZkwNPI2ryvX64Q3qNaKTgp2Qi6x6zx9-GUBBo-mZz2WMT3ktcfV_ocTFLFEJC5XXBKvwRtK_GuCX6b_HUG27gR3Ookqc2LSYE9-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f3f14c10.mp4?token=FRrCtYdsJnNEWyrINo03PyFfMYpXw1bk-eCD86lXnVPKfjQB42-ZaSG_B72M0Soty_mvarYVL3jxvrrJeKHjj4rK7mGdJJddhR6AzgkKWA-CsUkFyLHTn4O8GrG1qdzwIt7SwTrVWbUYtJHjvuN6zYkDXvABTETPVjvKhwb5MQkSA1TUUIgd-sOqoVnJvOuLeaTiAf_DGj8Q85BjmVnUcBFsT6h0UAHui4h-bfrUBlcnJN2O7ZkwNPI2ryvX64Q3qNaKTgp2Qi6x6zx9-GUBBo-mZz2WMT3ktcfV_ocTFLFEJC5XXBKvwRtK_GuCX6b_HUG27gR3Ookqc2LSYE9-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور پزشکیان و عراقچی در حرم امام علی(ع)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668137" target="_blank">📅 01:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668136">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: ستونی از آتش و دود دقایقی پیش در پشت بازار ماهی‌فروشان بندرعباس دیده شد
🔹
یکی از فرماندهان نظامی گفت محل دکل‌های مخابراتی شرق استان هرمزگان مجدد مورد اصابت قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668136" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668135">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سی‌ان‌ان: شدیدترین حملات به ایران از زمان امضای توافق آتش‌بس در فروردین تاکنون در حال وقوع است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668135" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668134">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d312260b09.mp4?token=sCs9cRk2gIt-CyDvMnk6L-p0WZ_wujvhaHRBIqctfPf2LZgicQl2vy1_ETZMlslihcEo--N6Pxjw9_ha8-swlQ3zlIs9UoL8kLtLtnXDS9sKuI5cy1B2rxCCJmkBq0zV1oUZEnAzK3VEqv1cI8YuajEcpDIYwqxniLJbqMNDFWGfnfcCf84v7UNnVP_iWoCDlKgeTciGhlnEO8vsVH3PUxjaJBr8uvQU7BxdeXSsy_EYQiJeGthzjNvLBeIUUCPI7UnKtN8AvLqFoE6ZqAkfiFdsHdhwcsCLjAtWMpsRDKwQ8hFgci83fPP25B3Y_wlLgozZxCyzuFQfRkyRhTRF7UR2Y3AqzR_keBBsXSp0B9WYoAx73Nn60RdacfSnWxJq955HoZiE_jHdsiXznHdTzRqjfi64ezAwwLqbMAnhn_6Ycyu0jOYAtNsDSs2eFQfM-LW-7-uodTrxND_C2hW5V9U2eqjoz1aqWSST5aSLOymAfK6M3zbkWDtp_v0I1GGMMGuy0x6XBJEeLNwLWw9eftpE6KV6xir3cg2mHyGuZukeYTetRv0s6WmKRYORkWhUcRqkp5qMeCevKzMRYa4HbE1XtOgUAaJDM2BjLCmrQ-phOEKrM5fx8Y38-cwxrzi_6Wz7RkMF4SqRrRxIJ4nSlWrCcyBAd3rob3nvQ8qKafg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d312260b09.mp4?token=sCs9cRk2gIt-CyDvMnk6L-p0WZ_wujvhaHRBIqctfPf2LZgicQl2vy1_ETZMlslihcEo--N6Pxjw9_ha8-swlQ3zlIs9UoL8kLtLtnXDS9sKuI5cy1B2rxCCJmkBq0zV1oUZEnAzK3VEqv1cI8YuajEcpDIYwqxniLJbqMNDFWGfnfcCf84v7UNnVP_iWoCDlKgeTciGhlnEO8vsVH3PUxjaJBr8uvQU7BxdeXSsy_EYQiJeGthzjNvLBeIUUCPI7UnKtN8AvLqFoE6ZqAkfiFdsHdhwcsCLjAtWMpsRDKwQ8hFgci83fPP25B3Y_wlLgozZxCyzuFQfRkyRhTRF7UR2Y3AqzR_keBBsXSp0B9WYoAx73Nn60RdacfSnWxJq955HoZiE_jHdsiXznHdTzRqjfi64ezAwwLqbMAnhn_6Ycyu0jOYAtNsDSs2eFQfM-LW-7-uodTrxND_C2hW5V9U2eqjoz1aqWSST5aSLOymAfK6M3zbkWDtp_v0I1GGMMGuy0x6XBJEeLNwLWw9eftpE6KV6xir3cg2mHyGuZukeYTetRv0s6WmKRYORkWhUcRqkp5qMeCevKzMRYa4HbE1XtOgUAaJDM2BjLCmrQ-phOEKrM5fx8Y38-cwxrzi_6Wz7RkMF4SqRrRxIJ4nSlWrCcyBAd3rob3nvQ8qKafg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چه اندوهِ سنگینی بر دل‌هایمان نشسته است!
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668134" target="_blank">📅 01:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668133">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc98386b9.mp4?token=XP0z4zo-5PnQJj3upPXw_at6gz26Qv9-Ube0I-_PaaGUuZQRVXt77j-KzvJRJ2Oj2QBHHkfjyv9HyfYa-6jcwEF-pM-_K34Z2sH-Ml0xAGsn6xduBEI-5puQ953YYws_7qcAzyEAOczq8Nv5WSwZzS2r2MJwAhemQ95o61egAYhBJ3Rnls-ne5IURG17Fkws0Wp7jE0mNGCzbrHSEqOza6rZzHhHhvKxca9QwZ7voU7ew8qfhfLprKzlA0SNCeOPRuA2_xSVN0O_0iJ_TrnA0k6Mljfhr7LPw2rrhVZK0nzWpY60E4D2OZOlOq2_IgnoRNliwplgdlJLoJmOem11Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc98386b9.mp4?token=XP0z4zo-5PnQJj3upPXw_at6gz26Qv9-Ube0I-_PaaGUuZQRVXt77j-KzvJRJ2Oj2QBHHkfjyv9HyfYa-6jcwEF-pM-_K34Z2sH-Ml0xAGsn6xduBEI-5puQ953YYws_7qcAzyEAOczq8Nv5WSwZzS2r2MJwAhemQ95o61egAYhBJ3Rnls-ne5IURG17Fkws0Wp7jE0mNGCzbrHSEqOza6rZzHhHhvKxca9QwZ7voU7ew8qfhfLprKzlA0SNCeOPRuA2_xSVN0O_0iJ_TrnA0k6Mljfhr7LPw2rrhVZK0nzWpY60E4D2OZOlOq2_IgnoRNliwplgdlJLoJmOem11Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودرو حامل پیکر مطهر رهبر شهید انقلاب به محوطه حرم مطهر امیرالمؤمنین امام علی (ع) رسید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668133" target="_blank">📅 01:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668132">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
‏نیویورک تایمز: در پی اعلام آغاز حملات ایالات متحده به ایران، قیمت نفت با افزایش ۶ درصدی به حدود ۷۶.۵ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668132" target="_blank">📅 01:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در سیریک: دقایقی پیش ۷ انفجار در بندر سیریک شنیده شد
🔹
این انفجارها مربوط به اصابت پرتابه به اسکله تجاری سیریک و اسکله صیادی روستای زیارت بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668131" target="_blank">📅 01:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در سیریک: دقایقی پیش ۷ انفجار در بندر سیریک شنیده شد
🔹
این انفجارها مربوط به اصابت پرتابه به اسکله تجاری سیریک و اسکله صیادی روستای زیارت بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668130" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668129">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68492ed60a.mp4?token=arfmLfFxWtiK1MovS6z8KNtIPDD-Xc0HBNY4jIQUg3WtOda3JRJD07uktEf9KaJmZEcK2E99zZdqgcnZFn9QPy9-tk4PTKe1OyZtCkbyZ5viw3QN-6Gbi0AC6WNA1H_ENRwc5IgWSzAfAK064eEMn_5SiasQkOHf4P4CRdSroCX1D7_ZPJ1GrZ4sxHptG5xaK_h57E4Rx5RCMb4XOzDbHIaKhaXxa9M4am_ziaJHukcbAEAlu4v76Pit8Z7F_WAF4bYTpzO3j9IXOUqPkxjkk4Ib0KanhPlacAqzb5NAmfUyN6mGYRQ8J_ym6SV2XwpEogPz3ohsAZUsIt9BMphDMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68492ed60a.mp4?token=arfmLfFxWtiK1MovS6z8KNtIPDD-Xc0HBNY4jIQUg3WtOda3JRJD07uktEf9KaJmZEcK2E99zZdqgcnZFn9QPy9-tk4PTKe1OyZtCkbyZ5viw3QN-6Gbi0AC6WNA1H_ENRwc5IgWSzAfAK064eEMn_5SiasQkOHf4P4CRdSroCX1D7_ZPJ1GrZ4sxHptG5xaK_h57E4Rx5RCMb4XOzDbHIaKhaXxa9M4am_ziaJHukcbAEAlu4v76Pit8Z7F_WAF4bYTpzO3j9IXOUqPkxjkk4Ib0KanhPlacAqzb5NAmfUyN6mGYRQ8J_ym6SV2XwpEogPz3ohsAZUsIt9BMphDMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از حملات بامدادی دشمن در بندرعباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/668129" target="_blank">📅 01:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668128">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: حملات سنتکام به ایران ادامه خواهد یافت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/668128" target="_blank">📅 01:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668127">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای آکسیوس: اهداف حمله امشب در ایران شامل سایت‌های موشک کروز ضد کشتی، سایت‌های پرتاب پهپاد، تأسیسات بندری و دیده‌بانی دریایی بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668127" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668126">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po-zI0OMUfmBBRGu6Y0n_7o1Tc2O-xqPmYenjnpXsu9yLCKh33IGppS_W4hRTWeS7YtHHN2VlwT4-xrJLOTA9Qb2H7q149PQ4Rjnzj8R1nAliEf62WVXYYW7_1DCVOsppbZOUcBifGIYsUWr6Sk7OAMRdLSeW8f8JtQZhnn2dwQd7n3QlTEAXIRMjNY8kUSc4LZElZ6DU4ELO8KASaBnciqL0UoAHhjjGobIjIYXpvrcu1la-IndgtJX6BlvoFn8Z9GasPLxr5ux8An7xUSB_szItVTqjMxtFTfXwGouBgKotr_eDU0-XX7r9eqQXI_ib0sB11DrOBIeN0Gw3WnLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: حملات سنتکام به ایران ادامه خواهد یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668126" target="_blank">📅 01:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668125">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای مجدد در حوالی قشم و سیریک
🔹
بامداد امروز (چهارشنبه)، منابع محلی از شنیده شدن صدای مجدد چند انفجار در حوالی شهرستان سیریک (۵ انفجار) و مناطقی از حوالی جزیره قشم خبر داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668125" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668124">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال به نقل از مقام‌های آمریکایی: ناوهای جنگی ایالات متحده همچنان در حالت آماده‌باش باقی مانده‌اند تا اگر دونالد ترامپ تصمیم بگیرد، محاصرهٔ بنادر ایران را دوباره برقرار کنند
/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668124" target="_blank">📅 01:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668120">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe18353a92.mp4?token=swolmDp0hTXQnMe1pRwkkfChADcD2FjuMgMoLNi_1x0V0bhS-cNkh9PWCoIurHhYOJXP6spTlk_KPymI0G5cpFYBPTZcoUGyiMmV5JOWtYBepdkVT4qz_IVCb3R_sh1ud57o7BrPeCNh4mKYaIcdLRJkrdwaUyR82lO0xj2Lj50AOOhnDGyGp6ugMiecwB0g3K37mJbt0megrBQJ5wCBZjiew-fNnUDg9uussJcjzJg0mcDch2olhXnkynpg9zj__2idX-XB3R3xZq8OhIyBJsR53BoXneXxOOSc5pElSRNb9HvkwdDlmQ5o077UA3D-PaWC1xgTbyMpKGMqIscuAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe18353a92.mp4?token=swolmDp0hTXQnMe1pRwkkfChADcD2FjuMgMoLNi_1x0V0bhS-cNkh9PWCoIurHhYOJXP6spTlk_KPymI0G5cpFYBPTZcoUGyiMmV5JOWtYBepdkVT4qz_IVCb3R_sh1ud57o7BrPeCNh4mKYaIcdLRJkrdwaUyR82lO0xj2Lj50AOOhnDGyGp6ugMiecwB0g3K37mJbt0megrBQJ5wCBZjiew-fNnUDg9uussJcjzJg0mcDch2olhXnkynpg9zj__2idX-XB3R3xZq8OhIyBJsR53BoXneXxOOSc5pElSRNb9HvkwdDlmQ5o077UA3D-PaWC1xgTbyMpKGMqIscuAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظر مردم، قبایل و نظامیان عراقی راجع به شهادت و تشییع پیکر رهبر شهید در گفتگو با خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668120" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668119">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
۶ پرتابه به محدوده اسکله طاهرویی و ۲ پرتابه به محدوده لنج ساری طاهرویی سیریک اصابت کرده است  بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3228642</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668119" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqaTQWpg_s2LBcDenOMIFIUMmk72sF7siSnu5BptcZ1-h6y1jH8gpEi0UD20EI0zlOjNhP5XDm8r8bqoJQ6Ou_SdUN-QGZ9SJW5tzw-hdLbXoxVy9p1_JYKyio3vHPODwVidYjdZmZIAEy8XSNc2Shgir9D4z2GcrfdDm4igEcXgZdekADtVFls5Bg6RnTDv05V6nOv2dRmc-7noHsTsLq0UKHazWhQ0z3WmeGzKBX97mGAwgZrN6P44sDr6A-0Wm_lbXDU8zMHBUmkQqLi8KqQ-Ifs_sAy0qFfQxPVDnxmI1AGI1vGHS0514SVy9UJyHxvoQLXAaV92fY8n4uhTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره نقض صریح بند ۱۰ یادداشت تفاهم اسلام‌آباد توسط آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668118" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تجاوز رژيم صهیونیستی به جنوب لبنان
🔹
منابع خبری از تجاوز هوایی رژیم صهیونیستی به شهرک بیت یاحون و منطقه واقع بین دو شهرک برعشیت و بیت یاحون خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668117" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در سیریک: دقایقی پیش صدای ۷ انفجار در محدوده روستای طاهرویی شهرستان سیریک شنیده شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/668116" target="_blank">📅 00:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqJGi3fSfjPQLd9QtK4xeV5-ZxPI58h9fwtoZgebTG0NGkl_MWkHK51ARDSMXPmojxceLs1alY39yD6ZNZXt3aa2VV89S_YN6cauVuf5nOfv-_G9R-UreJhpukdGcFWFhj10KTH4pgbtaj9Hvj_J9ZFpb3Kewc2nEB2IgA0OfftvdtB2qS6RKHE_zx8759Fo57POwerybPTH_0liTgOWnRi4LsZ-QV0bgTe6ohhtzLiPADliKD15SXRcCC_F-LCOEi-7yG2iB-3MU3cL-hIu7fbpx345mqz9fywhbrMk3LoOhZa1QEhQjgWHxnlOjKQWAbyLl_jabOsnCD2blrrihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند
🔹
حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668115" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668114">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در قشم: شنیده شدن ۶ انفجار در روستایی حوالی شهرستان قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/668114" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668113">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
در اولین ساعات بامداد چهارشنبه صدای انفجارهایی در  سیریک شنیده شده است
🔹
تا این لحظه هیچ مقام رسمی یا نهادهای نظامی و انتظامی منطقه ماهیت این صداها را تأیید یا تکذیب نکرده است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/668113" target="_blank">📅 00:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
دقایقی پیش مردم در حوالی سیریک و قشم صدای چند انفجار شنیدند
🔹
هنوز محل دقیق و منشأ این انفجارها مشخص نیست. اخبار تکمیلی متعاقبا اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/668112" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
آغاز حملات ارتش ایالات متحده به سیریک/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/668111" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668110">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مهر: صدای انفجار در قشم و بندرعباس هم شنیده شد @AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/668110" target="_blank">📅 00:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668109">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f82e9adf0.mp4?token=uremnGeC5c93lUPWzKdke2hu8hBTE7xPleyvl3DM8m694blJzJyUFwWuTjZXSENqIc94eouixbWA0q69xfD7pG2QQK8Ls_MCNuU1ZPvgdODmb6Q4QznV6Yv1mj_-wjA6jlpW0v4LMG93eGHQYflWsXdo9MXwkh5uCFLmb1S6BPdpPlaUnilKMLCn7rW09cw4_RZfWV_udaWqINppLwM6XWvO_hzbaneJz1lHivZqpJK3REd0JVbpnWQi-Top28JLVxVvJNDxV90P5POJmnyKQ9sOxaZ2YS4nBc-29xD1L3jJIbNy28hu7mVoix7t4Fj70ayjRLm_2fPfQ0Wm79YAPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f82e9adf0.mp4?token=uremnGeC5c93lUPWzKdke2hu8hBTE7xPleyvl3DM8m694blJzJyUFwWuTjZXSENqIc94eouixbWA0q69xfD7pG2QQK8Ls_MCNuU1ZPvgdODmb6Q4QznV6Yv1mj_-wjA6jlpW0v4LMG93eGHQYflWsXdo9MXwkh5uCFLmb1S6BPdpPlaUnilKMLCn7rW09cw4_RZfWV_udaWqINppLwM6XWvO_hzbaneJz1lHivZqpJK3REd0JVbpnWQi-Top28JLVxVvJNDxV90P5POJmnyKQ9sOxaZ2YS4nBc-29xD1L3jJIbNy28hu7mVoix7t4Fj70ayjRLm_2fPfQ0Wm79YAPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرفوری از یزله کربلایی‌ها در بین‌الحرمین حسینی به یاد رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/668109" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای بیش ۸ انفجار در سیریک خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668108" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
گزارش‌ها از شنیده شدن صدای بیش ۸ انفجار در سیریک خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668107" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac22428e7.mp4?token=Y1OuAHFemQuoSoqLRVWtF9FuD_P8CRsTbulvU5y3psrGSZCmsba3sBlSO3CN8ooXRBko3gfO1M885XBqSAnmAFwIdlrn5ROIBnCXLF_tcdAHlg5SlAgIIDv9MiXmkFN3r-6EE-qxgfbMUOXJxN17POCHe73_bZTFi6gGUHZk9NTfGOQgvNeDcVoGH3Nv5700YkZj3GMqj65UWxhIcdfmAeoiReNIM054HXO91Z7CRa7F5hmmmEHBz7kuIVqp1ju4Z3o8FEP2cHhHnzlVS34BU5Z1O8-9W8_nzgla3YQfRlCqLUCe6avlSv60MArocv80BQx8llYcfnwQreY8hNVpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac22428e7.mp4?token=Y1OuAHFemQuoSoqLRVWtF9FuD_P8CRsTbulvU5y3psrGSZCmsba3sBlSO3CN8ooXRBko3gfO1M885XBqSAnmAFwIdlrn5ROIBnCXLF_tcdAHlg5SlAgIIDv9MiXmkFN3r-6EE-qxgfbMUOXJxN17POCHe73_bZTFi6gGUHZk9NTfGOQgvNeDcVoGH3Nv5700YkZj3GMqj65UWxhIcdfmAeoiReNIM054HXO91Z7CRa7F5hmmmEHBz7kuIVqp1ju4Z3o8FEP2cHhHnzlVS34BU5Z1O8-9W8_nzgla3YQfRlCqLUCe6avlSv60MArocv80BQx8llYcfnwQreY8hNVpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون حضور مسعود پزشکیان رئیس جمهور کشورمان در حرم حضرت علی(ع)
🔹
بهنام توفیقی
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668106" target="_blank">📅 00:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12cc8100.mp4?token=oG2e9NC7MvSSn6V8xezji5j5Bk8nlN78QfjkwDS1_83o5kNpGdOzjS9vNVghHZBBJWGatbT-cNXLUs0bSHvYzufnkB3us4pn5Lno36w9bdt3sKGhcOFgz3Rl_LdGiLFFQnxxBRCNETa3VpbWAwEcdg8CL_7XLfJ_KWivwybSVr-U1M6t489cNreNqnGU3odvPS-ya1MFynHlTXeYRAKYTj7J5TV4UuREkF8JYqV3NCMkJeLOXrUGPKD6cXg6auPWLn0ZYRqYRBRU2Zs84qgIyo8MT5Al_4YBa2w8vd6skEGdXL0W__ToXYv1N7fE2SbaNmFuYhLZvP0krGzyLLaLFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12cc8100.mp4?token=oG2e9NC7MvSSn6V8xezji5j5Bk8nlN78QfjkwDS1_83o5kNpGdOzjS9vNVghHZBBJWGatbT-cNXLUs0bSHvYzufnkB3us4pn5Lno36w9bdt3sKGhcOFgz3Rl_LdGiLFFQnxxBRCNETa3VpbWAwEcdg8CL_7XLfJ_KWivwybSVr-U1M6t489cNreNqnGU3odvPS-ya1MFynHlTXeYRAKYTj7J5TV4UuREkF8JYqV3NCMkJeLOXrUGPKD6cXg6auPWLn0ZYRqYRBRU2Zs84qgIyo8MT5Al_4YBa2w8vd6skEGdXL0W__ToXYv1N7fE2SbaNmFuYhLZvP0krGzyLLaLFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ندای خونخواهی عراقی‌ها در بین‌الحرمین
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668105" target="_blank">📅 00:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9ade6e58e.mp4?token=UXQYrxrjLGYPwSd7Z1eYBbS-Bfvo_SFNeKgRfegAsv3xrcm-VthQ_uka1uA-Vf6W3Qq6CbVReqoxcckuNtBwxeIJqx9Co7UlFySHhRFlyAqAVRgZHexZpWXtmMSw7TaYXaK1M1fGuZLhaon74CF0E77Cduj3I7IOLTygFXrJwW2Qm_z49MwrLeg6dch2IUmUrq6SsKhQQplCzoJgRfpUoE-3SkXKxywwzhntQNL7c_nf0MuIy5D5IwM9u6P2IaPchimCbgTTkzKKI0gQEZOJgHSyPdoasktohl4S1cnTTpBNn0BH6u3dLLhOhqXaumRr3A_mr9l5A6vmYMXd-Ca6yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9ade6e58e.mp4?token=UXQYrxrjLGYPwSd7Z1eYBbS-Bfvo_SFNeKgRfegAsv3xrcm-VthQ_uka1uA-Vf6W3Qq6CbVReqoxcckuNtBwxeIJqx9Co7UlFySHhRFlyAqAVRgZHexZpWXtmMSw7TaYXaK1M1fGuZLhaon74CF0E77Cduj3I7IOLTygFXrJwW2Qm_z49MwrLeg6dch2IUmUrq6SsKhQQplCzoJgRfpUoE-3SkXKxywwzhntQNL7c_nf0MuIy5D5IwM9u6P2IaPchimCbgTTkzKKI0gQEZOJgHSyPdoasktohl4S1cnTTpBNn0BH6u3dLLhOhqXaumRr3A_mr9l5A6vmYMXd-Ca6yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عرض ارادت شهروندان ایرانی و عراقی در کربلای معلی به رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668102" target="_blank">📅 00:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668099">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
یک هواپیمای ترابری در مسیر کراچی پاکستان ناپدید شد  سازمان هوانوردی پاکستان:
🔹
یک فروند هواپیمای ترابری بوئینگ ۷۳۸ متعلق به یک شرکت خصوصی که از شارجه عازم پاکستان بود در مسیر بندر کراچی ناپدید شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668099" target="_blank">📅 00:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668098">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=QI-VWENplK90K280_d6JJGE2DH4YjWZbS6kvBDhy-oKqAzR8FQWd_yASYQ_ZH9wh5aJpPazIr-U-T7mt26lDuuHCIVeyiZsSDU-5ctbjTqbxs6mCeizahFpr2SDO04F3X4w9ZoLg61szYdriGB1HRKk6yev0fBtM-VO_0oAwqXdFJ9clzr_GDdkYmsNoNlogUt4Mqugf8N06gI-fwKkaRLDKCebvU_ijmvFrtwFtcxWyv0hoF_hxTNwqfMXh0Tpkguzdzy2IOXeDlwHCuHq1xNuCWQDzC_XxSd9FPiBTADuvrPdmFCpdVXh1PfLj_DOeo1ObAps6rtXJeF5oWnL8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce9bc8fdb.mp4?token=QI-VWENplK90K280_d6JJGE2DH4YjWZbS6kvBDhy-oKqAzR8FQWd_yASYQ_ZH9wh5aJpPazIr-U-T7mt26lDuuHCIVeyiZsSDU-5ctbjTqbxs6mCeizahFpr2SDO04F3X4w9ZoLg61szYdriGB1HRKk6yev0fBtM-VO_0oAwqXdFJ9clzr_GDdkYmsNoNlogUt4Mqugf8N06gI-fwKkaRLDKCebvU_ijmvFrtwFtcxWyv0hoF_hxTNwqfMXh0Tpkguzdzy2IOXeDlwHCuHq1xNuCWQDzC_XxSd9FPiBTADuvrPdmFCpdVXh1PfLj_DOeo1ObAps6rtXJeF5oWnL8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری عراقی‌ها در عتبات عالیات و دعا بر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668098" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec12a3d841.mp4?token=jOjKtr-RmxkTmRyWTYSj3THIVx6MuSJRb9SyPkH-zVYWBh9n3yo8zeRqgOQP3LSxCw_gJXjiJoKNnUvHFfm6HvIM-K79EHIkHLTB8I8ZAjjU3lihX_Ac8aQVx0Gv5KTgyNe3XOQsbN7SN3iq6xCiqk7oh1KRc19ujZb3j5tnLnAjGcbQnemxj_qrDEse8cJWDM7OvOnEa9fRPBw4IedurWqLbl8RVXHI0__WHJY_ZcJDVy8hpQIlKLSR9cm1IGxjk1-b0sGNMeB0IYTaaHCqTVTsLfUQZycDYSdmIiNTY_fnwF1-C1t3wWbnim3C2ztSZox6bA3sx2ykvknve-5lPkT28sQNX_3X8G5RvpwJbDLCl97qLiXNSNzK7kI9h8wf5K-I6havVZENkr7KLwgJHgQdxwcrglaiy1QHvYUsVdr1AtJRYYY_b7VpjIScV2hDg2lXWznAYzC1qJgIjNwLBuqfmRmnDfLP8T4u4UUePwtp7qt0VyYtwVNvxkTNe8JnG8NdK3hDWVhsCb2tYQigS6OQnRC9ZlaCcTkVnoiyGf07jRRrXt3HslcXsCVI0XWfJ-x1IrEuEIGNoxiEX5BU2eNzb_Rz_S9I78bb4L18Rl59sKPdhXT16mcuNHEIUMd4EE2WJbpkgaGcJUcTpLRwS1V2zRXiP4JEc7vd0tgVrGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec12a3d841.mp4?token=jOjKtr-RmxkTmRyWTYSj3THIVx6MuSJRb9SyPkH-zVYWBh9n3yo8zeRqgOQP3LSxCw_gJXjiJoKNnUvHFfm6HvIM-K79EHIkHLTB8I8ZAjjU3lihX_Ac8aQVx0Gv5KTgyNe3XOQsbN7SN3iq6xCiqk7oh1KRc19ujZb3j5tnLnAjGcbQnemxj_qrDEse8cJWDM7OvOnEa9fRPBw4IedurWqLbl8RVXHI0__WHJY_ZcJDVy8hpQIlKLSR9cm1IGxjk1-b0sGNMeB0IYTaaHCqTVTsLfUQZycDYSdmIiNTY_fnwF1-C1t3wWbnim3C2ztSZox6bA3sx2ykvknve-5lPkT28sQNX_3X8G5RvpwJbDLCl97qLiXNSNzK7kI9h8wf5K-I6havVZENkr7KLwgJHgQdxwcrglaiy1QHvYUsVdr1AtJRYYY_b7VpjIScV2hDg2lXWznAYzC1qJgIjNwLBuqfmRmnDfLP8T4u4UUePwtp7qt0VyYtwVNvxkTNe8JnG8NdK3hDWVhsCb2tYQigS6OQnRC9ZlaCcTkVnoiyGf07jRRrXt3HslcXsCVI0XWfJ-x1IrEuEIGNoxiEX5BU2eNzb_Rz_S9I78bb4L18Rl59sKPdhXT16mcuNHEIUMd4EE2WJbpkgaGcJUcTpLRwS1V2zRXiP4JEc7vd0tgVrGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای لبیک سیّد مجتبی، الموت لامریکا و کلّا کلّا آمریکا در حرم امیرالمؤمنین طنین‌انداز شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668097" target="_blank">📅 00:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H07cuglbveEfeyI3AaG6eLNhTMS7S1aa2gHg4ualCmlxMUngmvhLhuu9HX-iU5w43-jKyqO-63xu8SjtP58ly7jQDzw833GhWMIie1mEahAFX2Ncu4_YXAxIfYIqtm_0yCr_ue6P7J93xmR57iPMNCOBI5WSnsMFsIYBsrbTT-__zPOlpPVMsT--Ey5Pkpwbfo1L7z-qA93tfOTx_S0Ljwm094W8xmOATM6SW0UVVyjIWRAAGAT_tsQOpguFLg0lRPkhD0Lb1nSGKlWQd0PFxoQQK4bmkYHGCdP74CiNIxYYXVVFV_VfOCoYbCFEHIPTqjmI-hWcW7YMsmmg3FZcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت
بقائی به مناسبت ورود پیکر آقای شهید ایران به عراق
🔹
ای زائر حسین، این سفر بر تو مبارک باد؛که عمر فانی است، اما درِ حسین همواره به روی مشتاقان گشوده و چشم‌انتظار است. خوشا به حال قدم‌هایی که به سوی بارگاه او شتافتند؛ چرا که این گام‌ها، گام‌هایی هستند که تقدیر، خود آن‌ها را ثبت و ماندگار می‌کند.
🔹
سپاس از عراق، به پاس کرم و بزرگواری‌اش در میزبانی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668096" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBnRRLql0QGeGiS60K0W4qS1R12dJ6dKanWPQFtG2MMAfFKYmPT6FLvPox-JPZqdTvGDfKBptMOPNyHvQlgL5aBPFSbeZkWms13G3hthMA0LyHOp2WKYqtQw3huT6s8WdyHZnhI-f7f59wX8_eLqndcwe6avea0sggep9UWWCLek8csIoCJ3UMkFITn1nbqrqoBYEtnddmyxziCYouJfGQucJ_Ay1Hw04PhxyAUC48Ncel76SvQ1BOtZZmmN-jlgBp8oEjcGJTSIEW1TsebaESFVK2GsYlAZsYqVHAduDnA11mHw68UlewtrY1a97s2n0bxtzS7B-QkmlzVRV3Uq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور مسیحیان عراق برای استقبال از پیکر پاک رهبر شهید انقلاب  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/668095" target="_blank">📅 00:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
یک هواپیمای ترابری در مسیر کراچی پاکستان ناپدید شد
سازمان هوانوردی پاکستان:
🔹
یک فروند هواپیمای ترابری بوئینگ ۷۳۸ متعلق به یک شرکت خصوصی که از شارجه عازم پاکستان بود در مسیر بندر کراچی ناپدید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668094" target="_blank">📅 00:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=Ybtv4qF8YWO9H_AVMKnTbBxS7iHVePoeTGkQwxdhG8vjJUS29IuQOzIK3yD-KsClQsLztjc1B39irsL5u9LoP0SvEDvlawhfnwwGlYpc4RYZDrZ2r8Eaoz7o1BdLfXUfQ9-r3P_hvu7J6SRxo9wg2Rnr03y9fvlwONR1m7L378MysuqoaSg6Y5gK9umxOkZN8RjKsHx30U0AfDoOOKeVFyDN5KfnJ9_99TRf7x9MoXqKTCY25SLLyS9tzJPji_8u8t7tTldlJx--vgEzso5gMb1KIZBV4rDX6V1zg74Se773TL2855D2BEPN9WileklhjsuYJ1saQ95dOU76bmrL_UtVFlDiVixQOOzwwUcbOaREFP8_QqCeMCKukhB_w_05iqvNFCa5KfPWiUJi29sLDv-OX-IzQlfpKNEAkEMaG6T8gi7pdFTi3Op1YqZuEFxjesZ4ZopMWZGstF9Ld5M5h53jw6myIPt0LPsGYRHG_cO-ip5peps6EXQZlI8YVwTOP87TNo3wodV96FLVDUxys7e2SgNrfhHhKYspzCZ51goeWNizxq0ggG3UP_4myzU-8ivw2-UYKIjxW_KSu9lS86Pp-zAid5MRN8LXcUYS8MlLm9cdgaxP52WAxcSTSUCVnA7QGVxpuFYxKGoFZTztA0gLU28l2TAm51CDlgOFQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e1fa65d60.mp4?token=Ybtv4qF8YWO9H_AVMKnTbBxS7iHVePoeTGkQwxdhG8vjJUS29IuQOzIK3yD-KsClQsLztjc1B39irsL5u9LoP0SvEDvlawhfnwwGlYpc4RYZDrZ2r8Eaoz7o1BdLfXUfQ9-r3P_hvu7J6SRxo9wg2Rnr03y9fvlwONR1m7L378MysuqoaSg6Y5gK9umxOkZN8RjKsHx30U0AfDoOOKeVFyDN5KfnJ9_99TRf7x9MoXqKTCY25SLLyS9tzJPji_8u8t7tTldlJx--vgEzso5gMb1KIZBV4rDX6V1zg74Se773TL2855D2BEPN9WileklhjsuYJ1saQ95dOU76bmrL_UtVFlDiVixQOOzwwUcbOaREFP8_QqCeMCKukhB_w_05iqvNFCa5KfPWiUJi29sLDv-OX-IzQlfpKNEAkEMaG6T8gi7pdFTi3Op1YqZuEFxjesZ4ZopMWZGstF9Ld5M5h53jw6myIPt0LPsGYRHG_cO-ip5peps6EXQZlI8YVwTOP87TNo3wodV96FLVDUxys7e2SgNrfhHhKYspzCZ51goeWNizxq0ggG3UP_4myzU-8ivw2-UYKIjxW_KSu9lS86Pp-zAid5MRN8LXcUYS8MlLm9cdgaxP52WAxcSTSUCVnA7QGVxpuFYxKGoFZTztA0gLU28l2TAm51CDlgOFQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کودکان پاکستانی با عکس رهبر شهید در نجف سرود می‌خوانند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668093" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2U13gS85zEVhg2eGvXo5-kSBTodAzka8xB2n8mWbk_EC2ovOw6gg-jnOKHZh0juFg2q85S7YlqsTpbBc2R_fNHKzKKT0PUpViw6V1pzw_10iBpBHYvYS8jVTRmu4UwLpLf3Q1G-CPDRv6VOMqr21pCVwxcEAA5IEL3lnACQF8sgZh27Nr2qTt89_2BJ4BoK-VayPf-3t6UwE18Tol1ybm1UXfwe26Px_txdk83NmtzdXvvYzJoCyQSDuILZfCD9kL10DlO6DV93Vprw7cUpKLJXLDLD6zXfEgAarvL619l6RDHCVHb5yloY8YejuGayM50C52StKT8IjHS7CxDAdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668092" target="_blank">📅 00:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668091">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d15ba9f7.mp4?token=QolvRSUmMWJ5AJEkdmHqs_XlR9v90rJ42v0rRdTYN5KvhhO-7GyXLQeW3Sv3d97hxK9imcDWyv6uKhuX_V8rrH6nvWXZpYItsmUsjXpwPIwDfaenKo9C7LwiJdiIxoQJimiRPZRo01kNzwJ1bYgFq9dYq3xV1mq5TFrD3XDuBoqFz5lSi3sMsoTjtF978P3uQ0QRrbMakOfU24gWK7t-Kr44S_w_NqpCXPJDZozygq0wD6Jui5VYxLdwdF8yNqLfaNfCjQF7w7IraPJXUkkIgwaT495tqLaSPOyoflhC75tS8iIwYQw9HREEUbsoGT144pzc8dksp8XX3uDA0Mtsbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d15ba9f7.mp4?token=QolvRSUmMWJ5AJEkdmHqs_XlR9v90rJ42v0rRdTYN5KvhhO-7GyXLQeW3Sv3d97hxK9imcDWyv6uKhuX_V8rrH6nvWXZpYItsmUsjXpwPIwDfaenKo9C7LwiJdiIxoQJimiRPZRo01kNzwJ1bYgFq9dYq3xV1mq5TFrD3XDuBoqFz5lSi3sMsoTjtF978P3uQ0QRrbMakOfU24gWK7t-Kr44S_w_NqpCXPJDZozygq0wD6Jui5VYxLdwdF8yNqLfaNfCjQF7w7IraPJXUkkIgwaT495tqLaSPOyoflhC75tS8iIwYQw9HREEUbsoGT144pzc8dksp8XX3uDA0Mtsbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: هم انتقام مصداقی و هم انتقام از اشخاص باید صورت بگیرد
🔹
انتقام مصداقی به معنای خروج آمریکا از منطقه حتما باید صورت بپذیرد تا مسیر پیشرفت ما باز باشد.
🔹
اما به غیر از آن، ۲ قاتل رهبر شهید نباید از انتقام در بروند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668091" target="_blank">📅 23:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668090">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8lHotYaUVnT4vAuQ_y8l7BzkxHW1kEdhnGVAHeHO3usLbsRjUcVpNx0R_8vxwhUCzZVpgiMbYeWElH3yPPE1LsJ8_bi1-OSAGKQ5dHpRsfeIUlHprJIs52_dhDPVxItPOniRJdBSlY0E_fpKbaW2RCMCY-FuI_ABcCFYG7qPLiLAuOfSyW6WtENWshhOb_fBVQ4QyXHYSEL_MZtkJ0saA304-JJf1utuGnr_gzqd911hqdRN5Vi6HxdWtDSEdyTlGzPbwU4L9glUWdiViVGx3XcIdVYHFUd3s-qVPGBXd4oUCFl3IYWAL-z56gAAVdIIq8_rPYyZ09Vm7v-hdBCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شایعه رابطه لیونل مسی با گزارشگر زن بالا گرفت | همسر مسی وارد شد!
🔹
در حالی که طی ماه‌های اخیر شایعاتی درباره ارتباط احساسی لیونل مسی و خبرنگار مشهور آرژانتینی، سوفی مارتینز، در شبکه‌های اجتماعی منتشر شده بود، کاپیتان تیم ملی آرژانتین سرانجام با لحنی طنزآمیز به این گمانه‌زنی‌ها واکنش نشان داد و به آنها پایان داد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3228554</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668090" target="_blank">📅 23:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668089">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvKqZga4ajlYf2omcyvbAUuWVLw8ZPb1Zu7gkKznRaEpFpb8OJUkafzzpK-hDXVtuAqSipR9nT0aCH78064rcjyKN3-C1WbdQeWfiQom0M2xMkQFegSwgktxq8CzS4gRnUrcTBQbXEVd3TdG46au58_MwCx6_gbGu4ndKY4hmUxJSIk8s6SKrEg1hGD5xemEnw7_MMsrFZlCRLWet_PssnR0IqZEk5nGMsd7Mp0bpc8f0R2trTuOJuO7J9N25Djh6z3nJBJWS1EhcP7Y0ov490k212CYD0zQ7gsuOfFCDrqRdwETtdLeU2_iEfpX_aR6gpKdb8wf3zQ3462CJM46BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بی‌قراری عراقی‌ها در لحظه ورود پیکر مطهر رهبر شهید انقلاب اسلامی به فرودگاه نجف اشرف عراق #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668089" target="_blank">📅 23:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668088">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
خبرفوری| ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔹
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔹
به گزارش خبرگزاری رویترز، این مقام…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668088" target="_blank">📅 23:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668087">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec8c8a51d.mp4?token=pSMGyHQeCdO-sgGNCvHZJtHo_TZ9WplDddN5iD5XMSFb_n2mM3GV6eawHJdQc_LxYSkf4ky1keyd7hXWJNku_812C0Lz43oK_rvijwdR0ANrp3V4UakOwaNKHr7mLMW9iUnw_C9ZXhT1tHT4KzkTjKu7vrV1EhWDdnfa775CHHL2VrqxlAmelqiNK56zLMja-XNYDZC3wZC2Vl_swofPHCGl6DJGt2cpz7bIrW5SzrgQKG21xPMeWna0zWrsTslCLGt0JGHYN1wvcPRysh48NplGhRoDAAIAkiEzJhtJjOxIWEKoe7EPm3VfDy9cp1zJP4dAISG_UFDJsdKI5Q3Qew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec8c8a51d.mp4?token=pSMGyHQeCdO-sgGNCvHZJtHo_TZ9WplDddN5iD5XMSFb_n2mM3GV6eawHJdQc_LxYSkf4ky1keyd7hXWJNku_812C0Lz43oK_rvijwdR0ANrp3V4UakOwaNKHr7mLMW9iUnw_C9ZXhT1tHT4KzkTjKu7vrV1EhWDdnfa775CHHL2VrqxlAmelqiNK56zLMja-XNYDZC3wZC2Vl_swofPHCGl6DJGt2cpz7bIrW5SzrgQKG21xPMeWna0zWrsTslCLGt0JGHYN1wvcPRysh48NplGhRoDAAIAkiEzJhtJjOxIWEKoe7EPm3VfDy9cp1zJP4dAISG_UFDJsdKI5Q3Qew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از اولین لحظات ورود پیکر مطهر رهبر شهید انقلاب به فرودگاه نجف اشرف عراق #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668087" target="_blank">📅 23:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668086">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930cbd11b5.mp4?token=SVvLC3iLLfPxXXvwClZkev9e7YLsPcBS1wMuy6sCXmq55uYeyYav-AmuWSYqx3lZ09kz_sOqeYJQ1NJktxlyDnVnSKo-HDXeer7XBr6kJOs8T44b-Uvcg_MnG80145QKCrDxMCDLyIRnQVxeH6CUhE3BgaTevrN6CopFnUw3U6uA99p8QoXCYB8ftQYATLUSKbn4KbP4mopgiPRjyB4B2-dkqX21dkU5tpxNxYokYeSUwFs7o93kxbhF97GybA0KiYMirodAtlFx5cjHVQnJ-Yo_B5QZ5FxB2I59_jmcvIc1hqKCQE7FWAnKYUijG1HQU5u6DWO9OWnr5BQrdreE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930cbd11b5.mp4?token=SVvLC3iLLfPxXXvwClZkev9e7YLsPcBS1wMuy6sCXmq55uYeyYav-AmuWSYqx3lZ09kz_sOqeYJQ1NJktxlyDnVnSKo-HDXeer7XBr6kJOs8T44b-Uvcg_MnG80145QKCrDxMCDLyIRnQVxeH6CUhE3BgaTevrN6CopFnUw3U6uA99p8QoXCYB8ftQYATLUSKbn4KbP4mopgiPRjyB4B2-dkqX21dkU5tpxNxYokYeSUwFs7o93kxbhF97GybA0KiYMirodAtlFx5cjHVQnJ-Yo_B5QZ5FxB2I59_jmcvIc1hqKCQE7FWAnKYUijG1HQU5u6DWO9OWnr5BQrdreE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: دوستانی که مخالف مذاکره هستند صبر کنند؛ خود آمریکایی‌ها این مذاکرات را ازبین می‌برند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668086" target="_blank">📅 23:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed228eb93c.mp4?token=Q3KxUF6Z1q0G5usE7j1962OJNdv2_K49516DtBlULdZza_8gq3Zsa-wHTwNW0PRabEs5DO1lHl-bkyfirbFwziWpee6g_7nz1L83kkGrTi_-IizrfM5cLlmw0lBv9n-XLnGI4n9rgwKf2IcvISNM2chNQvndTD5E1J9wQoDcXipzMsqBNOKOQLEf42mgFzMnTFoS2Gq1ZMdS7vfSEvmPgmhtJimGajz-M0vpn0L1SElrcCGZHghNxkiLqDlQADx4t1v6WWEQ10EsnwHbGJsDbFQW-mvis6pJHB-6nD22NNlq1fE1dXg0pfkBTdTP-SffZQJ0_yN9a00ezWFUbKQKgD_7jAZ3CNKqS4QhPgLjrZ87bEi163dU4l_tvS0MOGFk2aTAq-DkMOIDr9hjmRrZMwhgXX05SRR_u2rI2qnCnWVONncvvhPJ9zgGPAVviEN6g2jSkNk0YpwPVdONyIr3cFff69aQ_wpzWRJUGGN_V4jsXz-zLUXPJUcBJsxf8vZuc_IIlh01u9TePHI8vvOlGOvPScADrqMLJYUQUILVInpU16-9M9LcBGVfrYncVSoj2rASVUGuvugkYBcj3DUjlcFFaeLrHGYA1sq_2t9Kuc8ikPA_6IwByqnmSx1BqX72xkfmO4IH5ALyByzVSnTn-uirglGmFY6jsEEzeL0ryo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed228eb93c.mp4?token=Q3KxUF6Z1q0G5usE7j1962OJNdv2_K49516DtBlULdZza_8gq3Zsa-wHTwNW0PRabEs5DO1lHl-bkyfirbFwziWpee6g_7nz1L83kkGrTi_-IizrfM5cLlmw0lBv9n-XLnGI4n9rgwKf2IcvISNM2chNQvndTD5E1J9wQoDcXipzMsqBNOKOQLEf42mgFzMnTFoS2Gq1ZMdS7vfSEvmPgmhtJimGajz-M0vpn0L1SElrcCGZHghNxkiLqDlQADx4t1v6WWEQ10EsnwHbGJsDbFQW-mvis6pJHB-6nD22NNlq1fE1dXg0pfkBTdTP-SffZQJ0_yN9a00ezWFUbKQKgD_7jAZ3CNKqS4QhPgLjrZ87bEi163dU4l_tvS0MOGFk2aTAq-DkMOIDr9hjmRrZMwhgXX05SRR_u2rI2qnCnWVONncvvhPJ9zgGPAVviEN6g2jSkNk0YpwPVdONyIr3cFff69aQ_wpzWRJUGGN_V4jsXz-zLUXPJUcBJsxf8vZuc_IIlh01u9TePHI8vvOlGOvPScADrqMLJYUQUILVInpU16-9M9LcBGVfrYncVSoj2rASVUGuvugkYBcj3DUjlcFFaeLrHGYA1sq_2t9Kuc8ikPA_6IwByqnmSx1BqX72xkfmO4IH5ALyByzVSnTn-uirglGmFY6jsEEzeL0ryo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از اولین لحظات ورود پیکر مطهر رهبر شهید انقلاب به فرودگاه نجف اشرف عراق #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668085" target="_blank">📅 23:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
واکنش سخنگوی دولت به حمله به پزشکیان و عراقچی در مراسم تشییع پیکر رهبر شهید: در چنین فضایی، هرگونه اقدام وحدت شکن خلاف مصالح ملی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668084" target="_blank">📅 23:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668083">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e8e5100e.mp4?token=N2vQbwrw3Bx3tRLn96vMQo7DuAW8lLIPMm_mLrH1Zz_gK_K8y_weSh_71sIqEgq3LESU9CI1QQhXKNVl49sI5xzUVZla4G1npoFaNy0gireIv6SjArk5xE3_4xbqbdZkjvfehR__6BR2kjnc_93F-CdmmosIX84eZXkwFSAoPNYoL7obbL3QX7MNIFmUSgT1W1-7p49NC--lZGlb8CeEbPxKk04j8nnvqecy5qLNv4NV7V1l0eSmj8i02RvLIlvYdgh8uhyOjbm35MvTSFzBdOQSQuiysKEB3C3M4zDNC9M2M7xTfK-kkqjJCHtwpo5GDzsUPSBEZ3Jy8dWCUCQ8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e8e5100e.mp4?token=N2vQbwrw3Bx3tRLn96vMQo7DuAW8lLIPMm_mLrH1Zz_gK_K8y_weSh_71sIqEgq3LESU9CI1QQhXKNVl49sI5xzUVZla4G1npoFaNy0gireIv6SjArk5xE3_4xbqbdZkjvfehR__6BR2kjnc_93F-CdmmosIX84eZXkwFSAoPNYoL7obbL3QX7MNIFmUSgT1W1-7p49NC--lZGlb8CeEbPxKk04j8nnvqecy5qLNv4NV7V1l0eSmj8i02RvLIlvYdgh8uhyOjbm35MvTSFzBdOQSQuiysKEB3C3M4zDNC9M2M7xTfK-kkqjJCHtwpo5GDzsUPSBEZ3Jy8dWCUCQ8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در و دیوار بازار کربلا هم رنگ و بوی وداع با آقای شهید ایران را گرفته
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/668083" target="_blank">📅 23:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668082">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8529fbe63c.mp4?token=F4dxebavSRJkJUnClmR6OjR1VGeJ59Je5f_QldJjrTwXXK5CNVrWOzyfYqnjeaqVdvKINMco1uMBuhqLpAjxYyK7Yge2hm7--qfTRV5J1B9LmYTfUITgxMCBUDKtdJDenvqzGzC_QZg_RVZ3n9tKZBLBbJYIlLSYHS82z_8mqP6LqIKkvLVL0tqIa7VrPRQtngDESnrLz_kEvT3Up-OZEthLf8dRA2FLcpz3aP9nCAeO8ggTE52AcZ3Lz5caEK5g4r47NrNb-Vnb6-GgdZyvSWrAo_DRu6kZwG7_D1HNqJ9hNO5cx1tbRC03eSkw5rT9lUYhfG1ZhK3xOyTT3NPiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8529fbe63c.mp4?token=F4dxebavSRJkJUnClmR6OjR1VGeJ59Je5f_QldJjrTwXXK5CNVrWOzyfYqnjeaqVdvKINMco1uMBuhqLpAjxYyK7Yge2hm7--qfTRV5J1B9LmYTfUITgxMCBUDKtdJDenvqzGzC_QZg_RVZ3n9tKZBLBbJYIlLSYHS82z_8mqP6LqIKkvLVL0tqIa7VrPRQtngDESnrLz_kEvT3Up-OZEthLf8dRA2FLcpz3aP9nCAeO8ggTE52AcZ3Lz5caEK5g4r47NrNb-Vnb6-GgdZyvSWrAo_DRu6kZwG7_D1HNqJ9hNO5cx1tbRC03eSkw5rT9lUYhfG1ZhK3xOyTT3NPiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد
🔹
پیش‌بینی می‌کنم مانند برجام، آمریکا در عمل امضای خودش را پاره خواهد کرد.
🔹
در جنوب تنگه هرمز آمریکا می‌خواهد حضور خود را تثبیت کند تا در نهایت ناوهای خود را عبور دهد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668082" target="_blank">📅 23:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668081">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece5de56b8.mp4?token=EQgAHy-pR4nNnYJZhzUgk7GPCfNFuvG8S9be6d5y5Psw6fX-vJ0u6a1Pp8uhx_8b80EXPC2Wo0WhkWyKxrx_9wCzJZbiXvnAAKdTjEYU8yt2vpJUUWW1hYfutlJAOq77rbn3Ytw_OOAG6bo-tiPB9o_vCZ_IihQGzLf-iFojy3RQ7yBDSQ3kR5ez97Aw7u7okLZ7hg0AYvUwGiS5msgtlTGsZUqB1qOxU54wIpK80EpLrLianSH1TTp_7wlmCvZmOqtaA_87aIfcCB52e1TmtriKCJEaQmhpTJ79npzbWFrWj1a42ITgu6fuFtBi79AaIZjyKMaKSV_9SF47MFJVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece5de56b8.mp4?token=EQgAHy-pR4nNnYJZhzUgk7GPCfNFuvG8S9be6d5y5Psw6fX-vJ0u6a1Pp8uhx_8b80EXPC2Wo0WhkWyKxrx_9wCzJZbiXvnAAKdTjEYU8yt2vpJUUWW1hYfutlJAOq77rbn3Ytw_OOAG6bo-tiPB9o_vCZ_IihQGzLf-iFojy3RQ7yBDSQ3kR5ez97Aw7u7okLZ7hg0AYvUwGiS5msgtlTGsZUqB1qOxU54wIpK80EpLrLianSH1TTp_7wlmCvZmOqtaA_87aIfcCB52e1TmtriKCJEaQmhpTJ79npzbWFrWj1a42ITgu6fuFtBi79AaIZjyKMaKSV_9SF47MFJVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد
🔹
پیش‌بینی می‌کنم مانند برجام، آمریکا در عمل امضای خودش را پاره خواهد کرد.
🔹
در جنوب تنگه هرمز آمریکا می‌خواهد حضور خود را تثبیت کند تا در نهایت ناوهای خود را عبور دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668081" target="_blank">📅 23:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668080">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d6e09e37.mp4?token=JJogTB12PqacoN5kENRqapgrGsIKSTKYr1DuZSnFn8FdEAFI9u4EDNwjWLMmZA57_7oc98o1c_ePMllZoP-pU-KWvmRp2uvMS-N0VuSVwLTshHjVCpw6P5PqfdlwMUGwkeHYgd3tZt8s4nIyX_TqILI4bOrvQY05-TonSAYe4-pxa7O8NHl6s0HjoXSNsaLKd_KHFka5qVRFBBtcqaNpvPkjQ3SssXR2IdwbtcTiprkiP4Ts-rzNdZ5OBdOj0uU4Cev571EYeNMm8ayRpc5SKHnRfeAZRKIXCh8tK-XjdhwcmjsmYY5DOwjEhCuvvWbz5ed8gl3C51a9Rq1QUShfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d6e09e37.mp4?token=JJogTB12PqacoN5kENRqapgrGsIKSTKYr1DuZSnFn8FdEAFI9u4EDNwjWLMmZA57_7oc98o1c_ePMllZoP-pU-KWvmRp2uvMS-N0VuSVwLTshHjVCpw6P5PqfdlwMUGwkeHYgd3tZt8s4nIyX_TqILI4bOrvQY05-TonSAYe4-pxa7O8NHl6s0HjoXSNsaLKd_KHFka5qVRFBBtcqaNpvPkjQ3SssXR2IdwbtcTiprkiP4Ts-rzNdZ5OBdOj0uU4Cev571EYeNMm8ayRpc5SKHnRfeAZRKIXCh8tK-XjdhwcmjsmYY5DOwjEhCuvvWbz5ed8gl3C51a9Rq1QUShfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقی‌ها پای هواپیما به استقبال رهبر شهید رفتند #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668080" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668079">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43f4fbf78.mp4?token=e6_j5Quo3KPU6upJO3WwR7FtaPSiZ4t_xuUI-IoJLyRzoa9hKSLC6iJNNJLucw1o8m4DC47mRqArxeoifaacx16XmFLmVI12AxgxyY12R12JlALZb2ioLViUikjlo72sPNc3BHZSOeJDLH-riSLPCeIUmcGoyl2KScPWJOCgl2Yp5erWmOduW7Oj2ibdLVtH-pwnSJjZKsGk5yUH7kKOoirwlL5a-BfXU1Dw8-o3PMMGPOBLhE5n9A1InO6lPsNx2Vvqf8cdR5qRFXBN48OMVaTd94wOp5FDO_8MRRrO_OYsij_7JMhg4Da2eysvfTE6zYTvs8JTO6F_6F-atflW2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43f4fbf78.mp4?token=e6_j5Quo3KPU6upJO3WwR7FtaPSiZ4t_xuUI-IoJLyRzoa9hKSLC6iJNNJLucw1o8m4DC47mRqArxeoifaacx16XmFLmVI12AxgxyY12R12JlALZb2ioLViUikjlo72sPNc3BHZSOeJDLH-riSLPCeIUmcGoyl2KScPWJOCgl2Yp5erWmOduW7Oj2ibdLVtH-pwnSJjZKsGk5yUH7kKOoirwlL5a-BfXU1Dw8-o3PMMGPOBLhE5n9A1InO6lPsNx2Vvqf8cdR5qRFXBN48OMVaTd94wOp5FDO_8MRRrO_OYsij_7JMhg4Da2eysvfTE6zYTvs8JTO6F_6F-atflW2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر به‌سوی حرم امیرالمومنین رهسپار شد #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668079" target="_blank">📅 23:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668077">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q62Gh07bexa03t9m70nsNIveJay4-HO5U9lqxSscC8nLG9YNXDd9dk8GPBvuINiKS7C2VjyAG2JojGmsYHOI0y9TrcyYnVzAOwH5Y8mYIpR8CUVQJ6UAEnkoXkWFgY6uCqENhxJ8iFyzm-jteP34ArH90eNxybJgBkkaXQDs3PSyNc5F102AZRCMy_3x2qMKjzalMiXajAbf3bI21ydMXGO_jmvrMndgJpoJ509CJ34sDADEhO2zylbTEIqUq6znbW3iOEsvtN6wf8SHOeCVw66f-MsiwweLXfC7398lVm-oynMhcf5oBVxXDtTpbUYy1oHqE--u40VLJlJQdm4UTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IkpJCLk066wqN7RXIga6ci9Vr25RZzVBQRcX3euC19AiD5boCgUbnXUnKXL7kJlYBt6lPsde6o4oyhnYu8inYLSdvnYQwvLT9AenOvCx3AwqiBiO8Lx-elvgAGTHrymZ6nNuOhXWlPZ2uJgz4nfyH6Sa3WP6Cbpwn__86g5S-dGGbEx4ZNdy506XWgamHxJJB_s93UGoFYZlbRmo5-PpFlYjk4HRUe78fqgVGddRIQtDoh5TfxYRCwx3mS4iaBhDDwOS9IhLzvRwcV-1mQurgBSHTZ5eatzoXAlD9Mc_SxHoZv4opOZT2-3CNvMVythFqRRTsEBh2hcAQ02yAYKH3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چاپلوسی اردوغان برای ترامپ؛
هتل ترامپ در آنکارا با پرچم‌های ترکیه، ایالات متحده و ناتو روشن شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668077" target="_blank">📅 23:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8923d543.mp4?token=jpWrbBqVQh-4P2mJwCcmCEx5SNkYWMdg0vevZoY4BSjQBaycPpAhl266zEPr7iShz3RlkS0zTLGkOHubb3ePWTtQvy38WpPMIbOEdSd-kYSTP6DREaMG4eUleU0LgmSI1ifS_-jQLXHmtri_jhz_VjFQVDUGQysSpC2X6zWDgbISM6UCH5G6SM2YRbYp2JnqPR0-du-SBh82pdZke1CCXZiLWFtLCnTFLEbkkd5BZpYVzbM_V24cOjamtnYnz0Ex-gGg7LQKNvEg0mZ3TcbrkhZ52R3nRlHyWinh1jv2ejgvWTX_YPynOiBgc8NZ5lwIKrOIrJFTE9eJ3nfvTFsCPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8923d543.mp4?token=jpWrbBqVQh-4P2mJwCcmCEx5SNkYWMdg0vevZoY4BSjQBaycPpAhl266zEPr7iShz3RlkS0zTLGkOHubb3ePWTtQvy38WpPMIbOEdSd-kYSTP6DREaMG4eUleU0LgmSI1ifS_-jQLXHmtri_jhz_VjFQVDUGQysSpC2X6zWDgbISM6UCH5G6SM2YRbYp2JnqPR0-du-SBh82pdZke1CCXZiLWFtLCnTFLEbkkd5BZpYVzbM_V24cOjamtnYnz0Ex-gGg7LQKNvEg0mZ3TcbrkhZ52R3nRlHyWinh1jv2ejgvWTX_YPynOiBgc8NZ5lwIKrOIrJFTE9eJ3nfvTFsCPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر مطهر به‌سوی حرم امیرالمومنین رهسپار شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668076" target="_blank">📅 23:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c7b59a28.mp4?token=I6Ko_D2QjjtksnlfP7YFp7RS7UL8IC_Rcv0p7Q6I2JfZgy8X5dJRBz4yppYigFCperZN3iWXxMHylibHn5fV1mHHPnbSR85hSoJK50msz-XT-9jcgCN1bxdjEY4yj57wVw99M9Vvw-ZKMdcK5JIRJwql30GS_mwrld49w3ZI4PLbJyErla_iwX0S--0oi5g08SkDyJ1rYgmEE-yUpwLqTmEK3nNMc3-HL8WCP99c5ooYl9xAAG8cPZqgKhBrzvDuaajOyMlfukNDhBdvM-4Qq_zbk_ojGzlpmFIICIzluE_l0HHRons1laiwKM2MCRvqJAxlAcSALAh44ybjlSg_vzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c7b59a28.mp4?token=I6Ko_D2QjjtksnlfP7YFp7RS7UL8IC_Rcv0p7Q6I2JfZgy8X5dJRBz4yppYigFCperZN3iWXxMHylibHn5fV1mHHPnbSR85hSoJK50msz-XT-9jcgCN1bxdjEY4yj57wVw99M9Vvw-ZKMdcK5JIRJwql30GS_mwrld49w3ZI4PLbJyErla_iwX0S--0oi5g08SkDyJ1rYgmEE-yUpwLqTmEK3nNMc3-HL8WCP99c5ooYl9xAAG8cPZqgKhBrzvDuaajOyMlfukNDhBdvM-4Qq_zbk_ojGzlpmFIICIzluE_l0HHRons1laiwKM2MCRvqJAxlAcSALAh44ybjlSg_vzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بامان الله، یا ولی الله...
🔹
هم‌اکنون؛ نوحه‌خوانی قطعه معروف «بامان الله» در جوار پیکر مطهر رهبر شهید انقلاب اسلامی در فرودگاه نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668075" target="_blank">📅 23:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
خبرفوری| ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔹
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔹
به گزارش خبرگزاری رویترز، این مقام…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668074" target="_blank">📅 23:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668073">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZG5BwA0Pu13zqNUXSD1R2mZT_e-yoDYPidcYSt0QQ3JybnCRgN-N0Iog_V7m7OlmanOJbOFyR1yUhcV3RlpXC9hwzF73b3WoSXXU6y3KKKowjH0ZUuJnKhNn4Wbc8KvlYGE5FsQRRtQ0Lht3p6HGGLpM0mHKIBid9dsitPki32MO9mxQA9E_u1leK4VAr_pQExPKKHTsY4RbykJSwA2SvQsKdTW6_r4zJb_Yn969Dzcc1TUEhobqMhNvunA17g8ZH13kAJAxtyy1e31vuzluALu8y_CREKVVTw5o41a8ZSht6D6s6g9Ndt4R3v78by5m7jeBLWu3QURJsi7rTc5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری دقایقی پیش مهران غفوریان برای آقای شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668073" target="_blank">📅 23:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668072">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc71f1c68.mp4?token=sp3gLYnWUlv4E_DBT-xnbJcxXsf4frmmPFNgZ9LZhHzz0VwUvNwbhUaBbKH7gKJMwQDJ5vDoTzW0o_URsefuxXZ1nN-Qq5LmLTaoOilgQzX4DgR6BN3Jt7TZW51IvBMKCJCvyy9qmAbNF5-3bYn1o7H6CY1a_RX-UwvJ-LdLbONBDZ0-v-fI18RqnpUP1rQixNFAP8sENoI8IIQhgrk4dJqkHFKu9JDZdjtwDnk36vbQRYzllzdDG-qwi8--zL4i1IaXp2Sk3NEXg72KU1QlQaAl3ncOnYClcSc1DxoQemEsSQNp63Kx1QsKX1P-8N32OGxxbzpcqUEwOV2cHPnL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc71f1c68.mp4?token=sp3gLYnWUlv4E_DBT-xnbJcxXsf4frmmPFNgZ9LZhHzz0VwUvNwbhUaBbKH7gKJMwQDJ5vDoTzW0o_URsefuxXZ1nN-Qq5LmLTaoOilgQzX4DgR6BN3Jt7TZW51IvBMKCJCvyy9qmAbNF5-3bYn1o7H6CY1a_RX-UwvJ-LdLbONBDZ0-v-fI18RqnpUP1rQixNFAP8sENoI8IIQhgrk4dJqkHFKu9JDZdjtwDnk36vbQRYzllzdDG-qwi8--zL4i1IaXp2Sk3NEXg72KU1QlQaAl3ncOnYClcSc1DxoQemEsSQNp63Kx1QsKX1P-8N32OGxxbzpcqUEwOV2cHPnL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل عزاداران برای قرائت فاتحه بر پیکر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668072" target="_blank">📅 23:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668071">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2b2478ed.mp4?token=rwpEPtcVCk70fofXPG-mT3JyDq0MmZgqKnQFbe-8A0QluBRdgvPPOPxh_UQO32y3Mhf_KlHiu_aspJnEPBAjDXBLBL6veTD7O1xKfg2qD9heyPyUGVtyJuptmnDR5qnbegyT2w4nHr5NAJPa3vAX0f9NsdRhlqxcOY4ae0xKzI41OGXZK35_--KLN7Y_hBguwzwFppukA9GVVz_YnKjmrO8A4u3c1n2yqTmsiNL8OLAx8gAY2j7X4kDSgR6gKXuhbYspdgNt6lSDyysHwkxZq5sj6lZ_gRBDz01HTSpTmVSyoJ4DgzcGVHyqAxHpNVUyGK2VkIMx5tJlsqkqKDvSmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2b2478ed.mp4?token=rwpEPtcVCk70fofXPG-mT3JyDq0MmZgqKnQFbe-8A0QluBRdgvPPOPxh_UQO32y3Mhf_KlHiu_aspJnEPBAjDXBLBL6veTD7O1xKfg2qD9heyPyUGVtyJuptmnDR5qnbegyT2w4nHr5NAJPa3vAX0f9NsdRhlqxcOY4ae0xKzI41OGXZK35_--KLN7Y_hBguwzwFppukA9GVVz_YnKjmrO8A4u3c1n2yqTmsiNL8OLAx8gAY2j7X4kDSgR6gKXuhbYspdgNt6lSDyysHwkxZq5sj6lZ_gRBDz01HTSpTmVSyoJ4DgzcGVHyqAxHpNVUyGK2VkIMx5tJlsqkqKDvSmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تسلیت و ادای احترام نخست‌وزیر عراق به فرزند ارشد رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668071" target="_blank">📅 23:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668070">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ان‌بی‌سی نیوز به نقل از یک مقام آمریکایی مدعی شد: ارتش ما امروز چندین پهپاد شلیک شده توسط ایران را سرنگون کرد
🔹
ایران دیشب با دو موشک که مسافت کوتاهی را با سرعت بالا طی کردند، به دو کشتی حمله کرد.
🔹
حملات ایران در ۱۲ ساعت گذشته تهاجمی و نقض مستقیم یادداشت…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668070" target="_blank">📅 22:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668069">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVSqrKWlA3uTR6rERKFh649jFIMio2o1vwFpA6Eabx_Ejd2aDKNzSHaMnPc_SfCk3apIH93hI0utZDG6-LQHjrqULUy4rhbjYCMwEbwXJtPNzR6AA9O0MH-lAiBTwsnn_PM2hD_Js2HfWKfmMmPqvMCQZPXevda_yVZkzaryPiHPIaAg03O9kaJMjjPCAIP0foAYeNMBgoM9CN5Uzc7x6Lp9cirF6qJ0B-bCdxMdCopXmyKi_XZoaqDTT_CdzmW5m8OpdiB0sBjRQKkreDmt4GQ0_do97g_FjRsCm4ksYdse2yMDmnFS-D8tJJGnj1SKDDxelKfhaEJnjNz3xIKdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: فریاد انتقام رهبر شهید به مطالبه‌ای بین‌المللی تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668069" target="_blank">📅 22:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668068">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
وَلَا تَحْسَبَنَّ الَّذِينَ قُتِلُوا فِي سَبِيلِ اللَّهِ أَمْوَاتًا بَلْ أَحْيَاءٌ عِنْدَ رَبِّهِمْ يُرْزَقُونَ
🔹
تلاوت آیاتی از قرآن مجید در جوار پیکر مطهر رهبر شهید انقلاب اسلامی در فرودگاه نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668068" target="_blank">📅 22:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668067">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-poll">
<h4>📊 نظر شما کدام نهاد عملکرد بهتری در جریان تشییع پیکر رهبر شهید ایران داشتند؟!</h4>
<ul>
<li>✓ سپاه تهران</li>
<li>✓ دولت (استانداری تهران)</li>
<li>✓ شهرداری تهران</li>
<li>✓ دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668067" target="_blank">📅 22:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668066">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17dcd76d55.mp4?token=QWkf70gEW93VGCurTAG1A1TRowBeIYrNiga3OzI23vofHEsmWhF04qZDc7ECqnaki7LVYyBDf4ajmufMJcusUMSIJOWhdhaFnqmYQ7c6fj1rKkCrZwyYUEsW_X5_6zwN7RiivGFYhVF4yy0NrqjQUwpkMfD6Kse8wCtg2gLd1_MkQcf4rqZetE13IPSbnAX0xlqTSvTe-0D_IbqfWH1QKvvbOBxZjWs_sXrrsryx9v-V4D3V7PcmlAfxBF6koNztUTUimtdczgP8E2KUkYNt6bvZzUc2oZ1ObmJQ6kPJ-FBe_tY8C9iUHPha21xDkn6wUp-OKZ24ZQuxLIOQjDJ3xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17dcd76d55.mp4?token=QWkf70gEW93VGCurTAG1A1TRowBeIYrNiga3OzI23vofHEsmWhF04qZDc7ECqnaki7LVYyBDf4ajmufMJcusUMSIJOWhdhaFnqmYQ7c6fj1rKkCrZwyYUEsW_X5_6zwN7RiivGFYhVF4yy0NrqjQUwpkMfD6Kse8wCtg2gLd1_MkQcf4rqZetE13IPSbnAX0xlqTSvTe-0D_IbqfWH1QKvvbOBxZjWs_sXrrsryx9v-V4D3V7PcmlAfxBF6koNztUTUimtdczgP8E2KUkYNt6bvZzUc2oZ1ObmJQ6kPJ-FBe_tY8C9iUHPha21xDkn6wUp-OKZ24ZQuxLIOQjDJ3xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام یگان رژه عراق به پیکر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668066" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668065">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da75bd9d0.mp4?token=K5XhKhIjFHPE6uZKf7YKXZIIF79CBj8Gp3WrI50UOB2YL3LA3txbMNojgncmr8gImZDWYuYymoaGkw6YZjYGsDAVe9QzpsRk2_EaKrBaXZ0zaSMhwQewkEsTl95CFA8eB_BbzqmDvRaEWHfQw1UphjKTI_xaESFn0NdP9V_osxNxYhezNQIhzeyf1KXU5RAlz62u3OyV965HxW057VYJB8ip9Bv3rNu1uEmLRTTsotIDISOWeOq5U6KvUcS3Z9uuUyuPSCPkzuH5beh0nRJXzijsws-hQHQbh5q94i2tARdGZJJemdqp_RXku_be0U7ARqSlTCD1nwo6St8pHfMIYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da75bd9d0.mp4?token=K5XhKhIjFHPE6uZKf7YKXZIIF79CBj8Gp3WrI50UOB2YL3LA3txbMNojgncmr8gImZDWYuYymoaGkw6YZjYGsDAVe9QzpsRk2_EaKrBaXZ0zaSMhwQewkEsTl95CFA8eB_BbzqmDvRaEWHfQw1UphjKTI_xaESFn0NdP9V_osxNxYhezNQIhzeyf1KXU5RAlz62u3OyV965HxW057VYJB8ip9Bv3rNu1uEmLRTTsotIDISOWeOq5U6KvUcS3Z9uuUyuPSCPkzuH5beh0nRJXzijsws-hQHQbh5q94i2tARdGZJJemdqp_RXku_be0U7ARqSlTCD1nwo6St8pHfMIYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی ماندگار از انتقال پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668065" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668064">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBHn8umhwEiOBF8OQs22zMD-WCqX-r1qlAum1s-G3NvaHdDFBpYbRX_J3qY4QVaTHtVd7KLkeG3TNC2iVen4efIgtyrq2SsISfFtTEMN1ZWdyAVy7utcUpHj-z4vRkiBWXsGmHtX_0H_r0S-6T48GLNykxglZcNAANEvMrzHohxBtqBilMB_gy7Q_KXFCcjypUrRnPIvCBAGRqIL8fwzO92iIjFKVIDYUpcFdDtFvRmoLkAfo99Xtyraw8utP2pmw5Btn778friylxotVipJOlMWoWIZ02MUU6hwuPXU3zt1aM8WYTwJHroBMYB7QyzZbs35JPVzgRtoSvdzuBXIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتصاب مهم در قلب بازرگانی نفت؛ پورابراهیم مجدداً سکان نیکو را در دست گرفت
🔹
علی‌اکبر پورابراهیم با حکم مدیرعامل شرکت ملی نفت ایران، بار دیگر به سرپرستی شرکت بازرگانی نفت ایران (NICO) منصوب شد؛ این تصمیم شایسته و در خور تقدیر از سوی وزارت نفت در شرایطی اتخاذ شده که با توجه به تداوم تحریم های ظالمانه،اصلاح ساختار و فرآیندهای مدیریتی برای تقویت صادرات و افزایش درآمدهای ارزی اقدامی اجتناب ناپذیر بوده است.
🔹
پورابراهیم پیش از این نیز در دولت‌های دوازدهم و سیزدهم مدیریت این حوزه را بر عهده داشت؛ دوره‌ای که با وجود تداوم تحریم‌ها، صادرات نفت ایران روندی رو به رشد را تجربه کرد. تجربه او در تجارت انرژی، شناخت بازارهای هدف و تسلط بر سازوکارهای فروش نفت، از مهم‌ترین ظرفیت‌های مدیریتی وی محسوب می‌شود.
🔹
کارشناسان معتقدند این انتصاب هوشمندانه در وزارت نفت می‌تواند آغاز اصلاح رویکردها در بازرگانی نفت و بازگشت به الگوهای موفق گذشته باشد؛ مسیری که با تکیه بر مدیریت حرفه‌ای و تجربه عملی، زمینه تقویت صادرات نفت، افزایش درآمدهای ارزی را فراهم می‌کند.
https://www.khabarfoori.com/fa/tiny/news-3228625
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668064" target="_blank">📅 22:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668063">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
از خبرهای پُربازدید امروز وبسایت خبرفوری غافل نمانید
🔹
🔹
این قسمت تنگه هرمز می تواند باعث جنگ مجدد ایران و آمریکا شود
👇
khabarfoori.com/fa/tiny/news-3228576
🔹
اصرار لندن بر روایت مشکوک امنیتی علیه تهران
👇
khabarfoori.com/fa/tiny/news-3228611
🔹
تنش در تنگه هرمز؛ از صبح امروز تاکنون 5 کشتی متخلف مورد هدف قرار گرفتند
👇
khabarfoori.com/fa/tiny/news-3228417
🔹
عروس های خانواده رهبر شهید چه کسانی هستند؟
👇
khabarfoori.com/fa/tiny/news-3228445
🔹
شایعه رابطه لیونل مسی با گزارشگر زن بالا گرفت | همسر مسی وارد شد!
👇
khabarfoori.com/fa/tiny/news-3228554
🔹
ویدئوهای جذاب را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668063" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668062">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
پس از لغو مجوز فروش نفت ایران توسط آمریکا قیمت نفت برنت از ۷۵ دلار به ازای هر بشکه فراتر رفت/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668062" target="_blank">📅 22:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668061">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e88968387f.mp4?token=WnON5RfQX6iiUpByk4bjciizofc8O5PavO53vs7s6ItCxBDjAfEJXLLmRuBO2jd944P7EViDLIkSFuOPZMqE2fK9qO3oIxTJ6r3Ea8fL42ladxblBQdCKcQrgTBhp9KRc806rc4eQLx8LiwNaQFBop8AcyFXNoS7kTvbvjAQCrkTrNet6UzU3ZERyynZ06eiCb8Rr0EOscEANA3lOQVA-S8rRsGukhw6WdINYl_L1ZxqpgnTPctuvaC_4GWqpzKvNhFYqemfjuygBn7Kqk3zxhXBhDdFGbX8UlPJxjTRnvP1dXNKtJ22t3ZuH1Mbd49duYy0mddMPZPekUZkS066PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e88968387f.mp4?token=WnON5RfQX6iiUpByk4bjciizofc8O5PavO53vs7s6ItCxBDjAfEJXLLmRuBO2jd944P7EViDLIkSFuOPZMqE2fK9qO3oIxTJ6r3Ea8fL42ladxblBQdCKcQrgTBhp9KRc806rc4eQLx8LiwNaQFBop8AcyFXNoS7kTvbvjAQCrkTrNet6UzU3ZERyynZ06eiCb8Rr0EOscEANA3lOQVA-S8rRsGukhw6WdINYl_L1ZxqpgnTPctuvaC_4GWqpzKvNhFYqemfjuygBn7Kqk3zxhXBhDdFGbX8UlPJxjTRnvP1dXNKtJ22t3ZuH1Mbd49duYy0mddMPZPekUZkS066PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مسئولین و فرزند ارشد رهبر شهید در عراق برای تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668061" target="_blank">📅 22:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668060">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw7G-EiJEsHbalNdPdwvDUpO4ndQ8AzvwhRw9E2qMkztea4ax4OQ0TyiUknGdVRELvxI1fv--q4bW91JqiKp0wpYmHaKZojKMKRqfl2JUV4YaCvPtei8yJQ56t60B9p9LKYy_lu3k-LcL_LUsI9EMbUVmbh4L6phKmxcWrA7lAZ_cbIKeJYpdS_mf8vRyGjHm26saFWibKqkpCqqvQeo_QWoO6c3ZzOVEvkqDnLJHaBgXIiPyd_E0gD1KG6JJEapB13y-8ytDrjXWnLdS59WDIwY8n8Z0DFyg_BVpYQS0EMkgTBfT1YGZ1xHA4IdQmos59rConkBZC40Ft0_ofE9EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری| ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔹
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔹
به گزارش خبرگزاری رویترز، این مقام…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668060" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668059">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZb-UU_k49XjDunRkhF40kRPdMgMNm5YzT3dDHrJBcbEGkjL-t6Pmv8BnTspXUGoel9io4l9jAA5pID4I_mHMnxjLA8LrhSvdI2I5yG1hVK2Iq8tPbeulDZ2lf0a_xqinXTUOL-Dgg6uQOnRykDS1u7zg4KSmktDqVsxwxcekAlyQkTLG5Gb7Yb030QnbOcliOp3vB_Q79bv-IBthcq_AoaM4onyJKCpst-Ek7d8Nesz4mu7iqlIi-5mlTKGrsVGKM2yiNxbjgU0t3LihwC4jMvlgaJ_tMYVk9RmqfLH7L-9Tj4_LW-g0mK94oJNwCEv8Zx60yWmKb4j0BeQLPMyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقی‌ها پای هواپیما به استقبال رهبر شهید رفتند #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/668059" target="_blank">📅 22:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668053">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hq_f3v9jeJo_MFqXyUpoOEbjJZNaJAHIJcQ76HLiKw4btMZsEOQnG4qMAFiGdIvFLysnEbWvmQ16zoEuUhNVsP5QSYx3uIRIrCncDpVcwW6AAR98Uzywgs-w5PdmLumrJb4prvF-KsyGJI3sTrZKWsa8kTB3PTdCWILe-gW772UCKAl6KHlM-NwjNy7SHkWVKCkd5CxD4fqLdwbGg_Zt6LNf4EcPSRooSsPAwIowwlqaGUbMkf3axMgfEAX6ee3cANJ3RPeGlUVi-ZoqmCa7afm60DPsCFW3Ni-8W9xbQHFSRb51RsLJTdBuyqRs-u9uIxXtE0UX7UZxyaLWh8j6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbXsNiY6Nyz36ds615HTCD9i9mESciAD5_rEXjoCPGmwrkXzzuHWlvEVGEx9dn4FPiwUfTf8c7kNFqmkHVX0tnUNzl38UGJ9xhVcXOY_QZX1jc-Hqk94Zt_Qo8S0TIB3hVLYfKtFno-WPUAziE5lbLYxpIzyS1D-_9VsJTrsDI3dPy6b50TPJHotko23uHwimoL9EMSU9xwq0bnSRLVbJsb3P7-jEz7ODGOm0ipgnkLJI7eteTBX25xas_VcQdyvzz0CYw5qjT2BlzXlpxBf2oM1Vsuw4WIlOz2AFR8sYIoztCwy2vvDmauhU6wsswunaNLk6EXaDeiy75eEQLxwNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/614415a478.mp4?token=nHh5kYilgfz4iNvG_R4ZvAxQxeX77C4QW4SahHRPMDMbFIdK0Hpghyn1mlwhnFoeoB8W12TQf8Qyl0U7Q4LIG9EDco-5DkUOhJ4p3dlk5h-TSi1zy8bEUr9gmltsNjzbCigR0i2zZvGCbZIAEoI2xyiHiEsSJpIKOfDKkWFyI9SL615JfNq2TUrQm1qhv8Tdye33xnbib6nGk1DmeeTsh_0jB4hh5-WGHZa_hbelRovfVirX3-TdUolh2_okhicDA3rQOWwkXwjil0tBE04qCRzZBYVVmi9V5X1_Cw6SXP9dgonuqvdrPcpkTvNGTVrvHP2RGhst7He-B2PAXNWoaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/614415a478.mp4?token=nHh5kYilgfz4iNvG_R4ZvAxQxeX77C4QW4SahHRPMDMbFIdK0Hpghyn1mlwhnFoeoB8W12TQf8Qyl0U7Q4LIG9EDco-5DkUOhJ4p3dlk5h-TSi1zy8bEUr9gmltsNjzbCigR0i2zZvGCbZIAEoI2xyiHiEsSJpIKOfDKkWFyI9SL615JfNq2TUrQm1qhv8Tdye33xnbib6nGk1DmeeTsh_0jB4hh5-WGHZa_hbelRovfVirX3-TdUolh2_okhicDA3rQOWwkXwjil0tBE04qCRzZBYVVmi9V5X1_Cw6SXP9dgonuqvdrPcpkTvNGTVrvHP2RGhst7He-B2PAXNWoaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرفوری از حال و هوای کربلا و شهروندان پیش از مراسم تشییع پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668053" target="_blank">📅 22:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668052">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
خبرفوری| ادعای مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند
🔹
یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
🔹
به گزارش خبرگزاری رویترز، این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668052" target="_blank">📅 22:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668051">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466a64f4ec.mp4?token=pElnbSKRGjhP-ja82FI2SErTL5SMHXrxjvj-YhJVtiVoKnSQ0Zv0m-KUMi18PjrAhoTJZ1VLMHBm50KCTOH4O7nqbgxii9bKHaGJ1JVL0oAJsCRT6VZ0xO-07FJqKY2QhglpXWlWfC0W3guD723Iz3WoofukuIpR_v5yf3Y7SuAJiZiwXMlSlTT6ViODcZfTjzaLcDt1AjCxqFPsSeq-aedhaxg6Ls5BiPm51mwdTERq2BcV7ePyGchcj3eFsBKI96bwpe5owuGT_EEoDBoWqZXjkq3-CkjFGW20VnfxW6773OGz2JHg6AYb2Hk11dOQp_mVOYa_I6sw4OYuUu-LNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466a64f4ec.mp4?token=pElnbSKRGjhP-ja82FI2SErTL5SMHXrxjvj-YhJVtiVoKnSQ0Zv0m-KUMi18PjrAhoTJZ1VLMHBm50KCTOH4O7nqbgxii9bKHaGJ1JVL0oAJsCRT6VZ0xO-07FJqKY2QhglpXWlWfC0W3guD723Iz3WoofukuIpR_v5yf3Y7SuAJiZiwXMlSlTT6ViODcZfTjzaLcDt1AjCxqFPsSeq-aedhaxg6Ls5BiPm51mwdTERq2BcV7ePyGchcj3eFsBKI96bwpe5owuGT_EEoDBoWqZXjkq3-CkjFGW20VnfxW6773OGz2JHg6AYb2Hk11dOQp_mVOYa_I6sw4OYuUu-LNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پیکر مطهر رهبر شهید انقلاب در نجف اشرف #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668051" target="_blank">📅 22:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668050">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a7e732b7.mp4?token=k235TeHcqgJ9FrwZ_UqAJ4ZzE6yIeU8sZxnVBDbkoE2FFAhKBU8VL42sCea375USxU-FlXunSY3thOuMWurGP87q8Plbk521QVdiPJfhh46j610vixd81bP5Mg4jOaW8CphAeGX0pGOju0gq3ut8RkdEaWPv7PnjXCuCbMqxB_IwiLn1uHoZHlxJvN6LjIDNUhycM5BVp53MEOscxTG_N--I1fWk_ieMIq-UclzFHH3EhTBTxXPunXFYTWybLqIyX4U_btATqLGaL5maRTpTa3IA7DkcMdpdQDzcj0kSmO7H8nt38PFdFFVYo_SY3okLOH_3xv2AG55kCONHEWwhUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a7e732b7.mp4?token=k235TeHcqgJ9FrwZ_UqAJ4ZzE6yIeU8sZxnVBDbkoE2FFAhKBU8VL42sCea375USxU-FlXunSY3thOuMWurGP87q8Plbk521QVdiPJfhh46j610vixd81bP5Mg4jOaW8CphAeGX0pGOju0gq3ut8RkdEaWPv7PnjXCuCbMqxB_IwiLn1uHoZHlxJvN6LjIDNUhycM5BVp53MEOscxTG_N--I1fWk_ieMIq-UclzFHH3EhTBTxXPunXFYTWybLqIyX4U_btATqLGaL5maRTpTa3IA7DkcMdpdQDzcj0kSmO7H8nt38PFdFFVYo_SY3okLOH_3xv2AG55kCONHEWwhUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پیکر مطهر رهبر شهید انقلاب در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/668050" target="_blank">📅 22:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668049">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d47c2cf17.mp4?token=aZoF1hu3qaoXpssjDb1lA7C_oyiJ0xQ-d29RuR0_30fZ8I3KOcGeGbZ2i5ymiEQr4vtD6wHegIrg80ck9yqjpN4TxdFAYlMaCeD48UA0WOpQbEeESli2a6Y0ov3TZIecG85ayD6EgHrsG6KzOCW3lGIHGlRTlpiVGG6gha1z040ZlZpUwmfVyd2dRNGFGj0G_5_dchSkEwRW_MuzKTdbv1Cdifl8nkHjVMNVPU9uX6arl9Fz33ekObf87VaNqTdUFAlZU9m030E_VQ82-CmAO58FDEkAZxgTtomOm2gdG64NoAY7N4Y9Vlsju645Mz9O5Tz_0R06RMcul9cWzafhNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d47c2cf17.mp4?token=aZoF1hu3qaoXpssjDb1lA7C_oyiJ0xQ-d29RuR0_30fZ8I3KOcGeGbZ2i5ymiEQr4vtD6wHegIrg80ck9yqjpN4TxdFAYlMaCeD48UA0WOpQbEeESli2a6Y0ov3TZIecG85ayD6EgHrsG6KzOCW3lGIHGlRTlpiVGG6gha1z040ZlZpUwmfVyd2dRNGFGj0G_5_dchSkEwRW_MuzKTdbv1Cdifl8nkHjVMNVPU9uX6arl9Fz33ekObf87VaNqTdUFAlZU9m030E_VQ82-CmAO58FDEkAZxgTtomOm2gdG64NoAY7N4Y9Vlsju645Mz9O5Tz_0R06RMcul9cWzafhNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال نخست‌وزیر عراق از پزشکیان در نجف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/668049" target="_blank">📅 22:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668048">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f2378b8f.mp4?token=BJ3KuGVkAuSJ4PrhIKnUDLo3F2DFXstoDiAiQs3C5z3IUr5YqFLQdqSSQR6IvH8G5tzRayVJsbUaU7RlNII9zeDopxBlnhxqmMaNIwB5dEH4mAsGkaxJsGR5k0Au-cdXjCw-isNRBo74-2pM6jrklP1t7jnVxxN5U2WAWm002Cl5cE0RmUzI8eNxvNgprgHeKu7njXuh82quTNDGjf_rqa4qxvhUYc_CRLNanCmCifvu2zwmrABGB6cXAvbh-Bkoe6bPkO-Aaeh7TnpQp4NF9JIF0xffAxZtNYZBRZ4UKQzl7IvEunPw1sTjr-ZH9BxliQ9099iTQQ1CNvZK9LKs-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f2378b8f.mp4?token=BJ3KuGVkAuSJ4PrhIKnUDLo3F2DFXstoDiAiQs3C5z3IUr5YqFLQdqSSQR6IvH8G5tzRayVJsbUaU7RlNII9zeDopxBlnhxqmMaNIwB5dEH4mAsGkaxJsGR5k0Au-cdXjCw-isNRBo74-2pM6jrklP1t7jnVxxN5U2WAWm002Cl5cE0RmUzI8eNxvNgprgHeKu7njXuh82quTNDGjf_rqa4qxvhUYc_CRLNanCmCifvu2zwmrABGB6cXAvbh-Bkoe6bPkO-Aaeh7TnpQp4NF9JIF0xffAxZtNYZBRZ4UKQzl7IvEunPw1sTjr-ZH9BxliQ9099iTQQ1CNvZK9LKs-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: توافق هسته‌ای ایران را احیا می‌کند، اما بعید می‌دانم محقق شود
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/668048" target="_blank">📅 22:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668047">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ff8ff04f.mp4?token=c5JvQq-Ff1UeUQeSK0k9Czj5XRKGqnVTkz901WTznP_j-LySPBeLNNh7R3aUyLw-MKqccbvbbz4dS7qSpm8NRfNOaEpN5wlxLuhNi49dRkd9YLH83tTHFKYC0rBGLda2EAwoMRotMCypPvM4FmuW5DHb8XyTEZIrU5CTCqgnG6gy7u-HCKIXnV8OBhQKnK_Nl8QcQy7DjGoXH-i2ovgwgEvlS9OW4pYE4Ivl61T7uKWtfCObewYoNxyTlMDCiQOu1EQ9wZyolZ8GJB1FKirL2JN5hWl5JN0kP0u2JQu8gQU0Et8jRbAgn67fOby1FvOn1ZXhkHCQei5AjDlXwLcsTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ff8ff04f.mp4?token=c5JvQq-Ff1UeUQeSK0k9Czj5XRKGqnVTkz901WTznP_j-LySPBeLNNh7R3aUyLw-MKqccbvbbz4dS7qSpm8NRfNOaEpN5wlxLuhNi49dRkd9YLH83tTHFKYC0rBGLda2EAwoMRotMCypPvM4FmuW5DHb8XyTEZIrU5CTCqgnG6gy7u-HCKIXnV8OBhQKnK_Nl8QcQy7DjGoXH-i2ovgwgEvlS9OW4pYE4Ivl61T7uKWtfCObewYoNxyTlMDCiQOu1EQ9wZyolZ8GJB1FKirL2JN5hWl5JN0kP0u2JQu8gQU0Et8jRbAgn67fOby1FvOn1ZXhkHCQei5AjDlXwLcsTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش ناموفق مکرون برای بوسیدن دست همسر رئیس‌جمهور ترکیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/668047" target="_blank">📅 22:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668038">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNTO9rYx7PFgWcNPV7gKGeSK907BS3wDIWvH34kvCbUXitai5nWLc3R-FPiMORe4JEPbxvs1HXBwEGhdvDu23j-_I0axeMzgfUPBdaAWKuK1bf951QtFSFxQIBDWcZeSIYSKUdMn1YTHlpCu6QK62Xis_yxRsZoOUDpYSYMQia4eoB3Jo2_W9rDPxvE11hYNvKjhCcJ9uqC9PeESr_S4CyAKiXYaRvlxm5o9-bzJyYZztmjdqkp48KRkmY_j9b5ETMt0N95l5Qkj4EPLKwtBvaQ6xG2tI7E0wBnIgEqaziAa0MvzYKN1kHksEZalYIH6OxfyzIClZiZlJQv8cEzfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV2kqXIcfPkGYbGcs4O9JceBQr95AEconLsnRGu6CKLcEu-wb1jyx-hEqPITG1wVZ9gmcUTooSLZgp_oXvxwdj2IeIFumlWX0Hiy_9YHne2KpEsqvZQM6-w6XFY4VZTfRPAKN7hpfJklJAm72AXIm_UWWiRlm9mXqhZgbUgnm4DSgTGugFrZgtvwj1V3WiPOvVPKx6KOWyMW0w2X8LbQRKQqNXTpI1m10kLVC2bWnLgUWCGUrduvTFb9lmqalTKSGXnRNSG_gZZBg2qEtUildB0UN7cEWLIbWrnXApMMKgYNVfvJWiMg6GuMHVb5WtfbCpz1NEJr8EHGji7Y8UIhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IKA_kS2IOCKMhSlpZdNNNGEp2SAinfSoZAi7RoTg9EV4aH4pydXoKymXK8Eg_Rlb42hsFQMmV3ldUfc7ebqku3oQutC60vWaNqzWyJsLJNC1ZpaHUqBgo5MyuquN1_3_iqQUp17EtOusyZYWXmQ5_xpc7sqCveFgkcbzURiukiDgYG8HiV1bVTL6dIaZ1gNwAKb3S5jMsjk9tWSyzziM6Gk1F3YjiZB5-dOOFo46fuO_-lF6IoHZShhC_hpu5Yvyn-7m94vw497m_0HvF4EmQZQgl4xMYcZNNAoULW2yUA6BKTltkZDhkfkOFoCX-8gBK5WZUrscsHe15Ee02vR8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYOzbkEwzSqvZOn4pQkqEtpVqAUL41QGXqVNmvq3fzoD93E35y7gPWnh6W_RDLCrXupVIhq4O1ddwDHqJf5vFj9BrA6rky_lzN2f0Z7b5664dboOCwRbUC-gMlixUkcl5v1pklpVgLbqqsugi3FK4TEvpqS03DH_B_msSvLgEo0QxYGbX9Ey7wuZQK0pekzAbFpPNOXb7odHSPO_w3sTZc0-cG5MBcbdW0FUTjTpTdaeOopUTiv0Shu_Dzr15A9fTO4YFNZdNYr9A9jQtviojM7UwzCZmvx_1Ya-FbMloCIcpZdTK41td3mVZ5qQlJ1V4TxYfndmhwfCRettqf9ZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6rNVcTfPTBL_8hIX7tcdgKBTqH7GhRBIR-q2q0SnpYQzWFgrXWh6ZHbUsjLKSna7M8FbcyKUkzgiqGJ06nPU_org81doCKRzZbjHne4_RQYyJi2p1NQjy1J3Od9zpE5va5alG-1ob6NnAWCFBymO3Dkd0w93mvEbedQL8mxG9oTzyqloz9idA7iXWZ_58mZDfZng5FuzN2bf26W5Wr7uhoBu54mhxCOFeRFAKqW7Y2mzePcYor5WfZXZWdeNjJFRykcidCkwN4Kt4seVxvqEDKq16tHJJ5dfg6pKtfeNxeUc5JIYo5fcKytIMXa9zjKlT_Pcuhc51b4Z6TbdqojCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77545ea37e.mp4?token=CohC1FSJT8vG8AINFeVPKvNBYXWVya-sCN9LLn8NHv6Al-U5q-zPQ41qh_iZIZJiI8CfvesQ484ZR9gBavlOOX5YDL5hy4xgV6PPnQPmjTNfaVQ1E85PxiR5DTpasPyxDzYZVnA-fR1giziGna8MTDUAoCAAtIi_G2PAiHdI5fI1AKi-SxpnicOmFa2FalpxISCsGcmd5pIvSBAGmK9APfh52q9EE2SQ3MRn85iLSxxt0k8RR5XIA55k18x90YzAYHJb0SJQcqm8XHbzWSKpA17gHvs0YDO55uPTff_5DJE7gO64ej1Jvk4QETA8xhJadcc_kf8w6w5bH73fnnrtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77545ea37e.mp4?token=CohC1FSJT8vG8AINFeVPKvNBYXWVya-sCN9LLn8NHv6Al-U5q-zPQ41qh_iZIZJiI8CfvesQ484ZR9gBavlOOX5YDL5hy4xgV6PPnQPmjTNfaVQ1E85PxiR5DTpasPyxDzYZVnA-fR1giziGna8MTDUAoCAAtIi_G2PAiHdI5fI1AKi-SxpnicOmFa2FalpxISCsGcmd5pIvSBAGmK9APfh52q9EE2SQ3MRn85iLSxxt0k8RR5XIA55k18x90YzAYHJb0SJQcqm8XHbzWSKpA17gHvs0YDO55uPTff_5DJE7gO64ej1Jvk4QETA8xhJadcc_kf8w6w5bH73fnnrtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه گزارشگر کروات به ترامپ: بلژیک پیروز شد، اما بیایید صبر کنیم. شاید فردا صبح که از خواب بیدار شویم، تماسی از کاخ سفید دریافت کنیم
🔹
دیروز ترامپ رسما اعتراف کرد او از فیفا خواسته تا کارت قرمز بازیکن آمریکا ملغی شود.  #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/668038" target="_blank">📅 22:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668037">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70aeb849f.mp4?token=dWREoCUc2xE6QcTtHRf2EputqZ2ifycJmutNUKEVpceOlbrwHcHVS2lUzYEPK7gwcLHfUHrhDoF4R7SsYkGtUY70a6Od3nQKwKQklOx0-NUpQsmK_QAx_-6JMNEt8pxRuOjceF_tS10LPzLVAsyATHjc6s7CSxixnnxe38s327h-zUKjVKB2u8czVHqVrTkyxPU7KAa31zsiN3Vp1gZ-CZk22INzwcCaAABfeuHPl1hDAUhrfa3O1nhCGOfjEypk-m3eP1TvTnN9qiXuuGyVBHr9KKVBtDyphVtfleXczZ_Ysk9w_XKFPVKIaxbBqvVMMgMppbXBX95D2cvINZMzOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70aeb849f.mp4?token=dWREoCUc2xE6QcTtHRf2EputqZ2ifycJmutNUKEVpceOlbrwHcHVS2lUzYEPK7gwcLHfUHrhDoF4R7SsYkGtUY70a6Od3nQKwKQklOx0-NUpQsmK_QAx_-6JMNEt8pxRuOjceF_tS10LPzLVAsyATHjc6s7CSxixnnxe38s327h-zUKjVKB2u8czVHqVrTkyxPU7KAa31zsiN3Vp1gZ-CZk22INzwcCaAABfeuHPl1hDAUhrfa3O1nhCGOfjEypk-m3eP1TvTnN9qiXuuGyVBHr9KKVBtDyphVtfleXczZ_Ysk9w_XKFPVKIaxbBqvVMMgMppbXBX95D2cvINZMzOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یحیی قاسم، عضو شورای فرهنگی انصارالله یمن: اتحاد میان ایران و یمن تضعیف نمی‌شود/ ارتباط مردم ایران و یمن ایمانی است و هردو ملت عاشق اهل‌بیت هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/668037" target="_blank">📅 22:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668036">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ترکیه می‌خواهد ایران را از معادله حذف کند
اندیشکده آمریکایی کوئینسی:
🔹
ترکیه با ترویج «کریدور میانی» (مسیر زمینی-ریلی-دریایی از چین به اروپا از طریق آسیای مرکزی، قفقاز و ترکیه) در پی حذف ایران از معادلات ترانزیتی است.
🔹
آمریکا نیز این کریدور را فرصتی برای تضعیف اهرم فشار تهران در تنگه هرمز می‌بیند، اما این تغییر مسیر می‌تواند ثبات خاورمیانه را متزلزل کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/668036" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
