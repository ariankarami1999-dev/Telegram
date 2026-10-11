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
<img src="https://cdn4.telesco.pe/file/QPDqdNK6_B69JK0GFe_xMSOaPkXXAY7bO3yekoNQsveZ8qva10AXwF6bBGa6SoxzX-ucHu6nFI83hnwYHea8PbR58iPyWQBFGF6RJ9NyxegVHZGLOwLWriwGR3NT18DNOgbd3V_T8_yGDIcE1AyJn3e_romHYbetIKa107iL5gwYEpz5yCD2q6TxXXaPu9QNKdCp0AxEsgx8lKdLuzfwEAmXsR2n-wtOyGXiKQy1KmVeMN9p7Kmv4GOvYMgh3MHwr_3TQmumq0DwRAC4aQcUfobuCy6RoAPM9VQUcDt9eHmpUPaunnAv-l1BC2EgHxLfMT1zNwbqsuTfpCQpJX0wqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-467727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d916f969ed.mp4?token=EuyxeEF1yDYtCPl_e4gTYQvJse3blddAPB4XFYXQ_fa84BAbHPlCLrXEkyCFnSVMsKvo8UOctNZOwhi5T-tt6BucRW-vjuXeXroQWffGRV4bT7hlHUgxr7-6vUCTFg5Vx83vHJpbr5GSvfcsOQkWB-PHSY5RhSAfkqtRWKY_D-eio5o5GFOEN9WmwvTsunx18PxiVuhe6kipoZnnVcf8kCKRDIsbrVXzBWSTN2Cft_Zvsz380ximDiw0HOkkFFKvoJYdeevP5Gyd3gqC5wXMzfuTSHNwhOAjMA8ps2SZw2PmNbtfcmCuy8MBaLmw0haqYbOumnCO_gZrWmpTAD4BdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d916f969ed.mp4?token=EuyxeEF1yDYtCPl_e4gTYQvJse3blddAPB4XFYXQ_fa84BAbHPlCLrXEkyCFnSVMsKvo8UOctNZOwhi5T-tt6BucRW-vjuXeXroQWffGRV4bT7hlHUgxr7-6vUCTFg5Vx83vHJpbr5GSvfcsOQkWB-PHSY5RhSAfkqtRWKY_D-eio5o5GFOEN9WmwvTsunx18PxiVuhe6kipoZnnVcf8kCKRDIsbrVXzBWSTN2Cft_Zvsz380ximDiw0HOkkFFKvoJYdeevP5Gyd3gqC5wXMzfuTSHNwhOAjMA8ps2SZw2PmNbtfcmCuy8MBaLmw0haqYbOumnCO_gZrWmpTAD4BdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: چند جوان بی‌تجربۀ سعودی توحش را بر سیاست عربستان غلبه دادند؛ این به ضررشان تمام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/farsna/467727" target="_blank">📅 16:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInp_a-vDeP1Y4qnsqfll2TjBVm8WTFTJUAxKtvNa9aObL-99C43fMRuJXG5nS9u9saBLH0BgIqx9FusfE15WLep_7HQ-jHGPUR0dPppQt8Ep9TebZGKEcxEl1KPRyAcrtRaOcOXb0IjwwATNVQ4CqCOiihd_M2CJOESRiT25nNo5pnKV7q4uuUz7sdQ8x_Snm41y5M_KzLKpzXnakosGVuU-gDLssB5rk2uAQjgkgtR6pjhjwOAaPmCiJ4dlh3kMuk69kUbvmN212OHP3Ezj3epxxxVJbebyOwrXFDGbghVgJnpFpMlSge1jxLa6xtJGHpmSHKJYtUQp9Y3XBprQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
همتی به بسنت: از قول ۲ هفته‌ای که برای فروپاشی اقتصاد ایران داده بودید ۵ روز بیشتر نمانده و من به شما می‌گویم که چنین اتفاقی هرگز نخواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/467726" target="_blank">📅 16:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467719">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XboHF2X3mecGTEF8tU_3IT0HmCSwQjqfcbbPdYsxvLwAS0-JFFKHXT0Y1wHZ1pYvH1G9sNa9dNz9o6vgoj5Lciaw3Uspw6wQu0XdI-XBqSxEpDNC1hHxZwGeSdiCAfbX76xQHYjI_yjKJgn6zZjSlSy7wNxQe1Vnz9PGh45394vexj9RB8KcHSXzfj9zVMUBldPe0gHaz3sSHQodeksj6GZscVuLqNCoFNqEJbFfJ_SVFDmtm5QWRDxCBOuqHhRwwyYiYGDNLijG0kJSIgYKD8dzS4etmrdJ5xfJeyFt2y9tJcSwpga5njygZ59xC9eWgtleeirP2k6VXyRLDkeIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oz-kXdpTVTQSt-E5E_tyJ-DoXyn1f_PTaFaB4ADzjdHe_AJ3fEywCeEK7-u3J-paEMw0q2j6nFkTqmc6LsfQmSImGigFdKNzCdVbfoOLCgPDmXWZJKBhBejRG2EcdapjXTWMX3h_89q4ALjOD5HSk7VlO9NiAB5cjNpE0R0vscaBzzgTOAMMP9WUevOmjObXdN4m98v0pMedaiG8Bu9mypVzdfNJez-n0PrTLHDcrMEedz5hrM7okW2PtCXfmERQwVbHxPZyVEKnll9FIn_lKGR8fPzTec-SgncdHq9K4lWlP2oNKc4y0_PIJvmad2lwmCZTono4WAdT_253PM9gGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHbLGTRfk1m4WVQeqq8u_dykrJVbZdjVQGgFVilwnvDZlbQDXbaPJjT6uBRdqS3hriwNMaDhTSI6f1i1KkZlTIPQ_MAYaPykRGK9jpLWydz1ms8m74nkqotWHoop8kT_8E-vXkz18AuJ8oZqaPIOXfmTkwsaYHQNuozp_JYzz1LmKthSfFrQkp8Zsa786J-K22fhN6F56usfVCIqP8wVWNlmXy4JYi3wNXf5i9i_iLIpC3552ia2ur6GTeHbJnwidlKGKzI4ulMd1SgAd16TrCVw222d7WBBGhEHccHXHG6VXW0CFlWbeYYJIyNNIF_KhBXyVp6vZqIYAkZPcATzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0Y-KbITwo2KURlYeWTfTnPfbGc-UnvtxeVGwRQXeAGxzACHV7elr4zbcLmrH_kzP52rYdGF5QK8ZBUQ01BfD-w5iT6jPUFIUIOWyt65_UmBO_CB0fpAMPDmY4HKh0tfDxNzMa-JuJuGewf8C5Yy9P2Qk5w5FATjNddzc2cbEVLhLhaw_pFmhUSbLMB1z-Pr9Bc50pxUhJu08o6Aw-XLr_GouAw2AciUSCFvJp5ltzKnq0vjmbxMwUxIOUAo9PaxLoa_dPx95gBhYNVODTCGoLLPhwaXbNvcmVXImQkGUaH8xkgkPwdIOQSiFxsuX3SBslvC3lvcWgYWYtbkTFAYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXdp82-oSGoWJIcfxSGicZMLv0_vfgEp_KOWQAegTeafLd73F1wDNpnEHv90FbZAZR7SrpVNRfSLIliDVn68fxf5ziGPAJzQVGk0MQ1nUZncdFrvhN8DxF_wjEmhdIhroNJZGl0tnHWGd8aTl759jWc03lJ7C15xK6evifzyRzRTWxPDdPPBtrWIzxBSLGKYIRr3-St1NBZMFqDDMnzmDqbVL1j7C3iN_c3QBbdYvlqfWk_5pnl56IEgj4P-zeeWbd2V981fd6HcZTaD0DbDcxTeHNnDGofs2APSrFBDA1UXuLi8tRzNAWexY8XthoW98sY-vfcFQfH7XRZNNpAfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoS9Zmim9D7AxnH5JnuB494TK24IyOymSaOJiM0jmwkfHKpydRNw7IGqS2ezvruxxYnSZVC0q0Ts6QGNxx56AcVSnHiSyP7N5qibkeRAAvd8pLa6ir11YNRml_43G0-4vNOnx-8fnmqg7avEeWvK56_rogqE14Ai3mAaZiJAINtLg_kQG3yCtnzdwCGSbvxSJ_SFzhVmPLxTzQcvPm8gLFYnVB0Ly9aSrgb1HssbEwl4HV5owPo2ko8x0k6eOtohFDbT_tMCDrlWk_gZT34c9Fe2DAjrBz96zt5q8hqAdYxaHO9vzTZpqE5u1_Y1GFZ5O2uKUxueN6e2BIbvuVCI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gumbp27uOAOoXDA884QDZ1TKq2szsN6B5qmCFUHSBWYWHl1g33rJ9kFDnU4N4NMiaJya5ZKEOL7kEOdVG0g9yDy4SpEX96i0XCXl-ODUFkrVHGwk-LHivogMjk-3SxtMSKQHUTq_NcqBWvR6UmpWP-5wD363VuT_4Afc_KLBCe0ilYbfqyfnev2SHNViK-OFJj5yblM5Zl9iZMCCDBqCRY41GFfovgn5rftHLAR8NsDWcnEyZx8TdI0FSs7fwOz_44-BAdcZ6dXm1EKQmog4InR1DZxDWrJRT-zFI4f86bsC8OE1nk9Tj8oDKYJ7W-4pYJC60z4w6G13SZRpyQXlgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع شهید حملۀ تروریستی زاهدان در حرم حضرت معصومه(س)
◾️
پیکر عباس آقایی از تکاوران نیروی انتظامی که در حادثۀ تروریستی زاهدان به شهادت رسید، در حرم حضرت معصومه (س) تشییع و در گلزار شهدای علی ابن جعفر(ع) قم دفن شد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/467719" target="_blank">📅 16:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467718">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHIduOieLOeZ_gX0J7dF0rCUNhrpr9Ue3EoBEpF_Sn4EOys4i_1bjLhvEc4_UJToAzTKuLQi9INrDkrVfgdj9yjk1uCk_0_3WEk5LFEiqQAOFcwqoA3P4LauRsH97LsfBV9qbLlqIGhHYj86AbxCbuDUu-uruehXOEBXZZVWfhxsh-dDYAM6y2SOhl1fmj7XrSrucdroCSXIKAdnbMwmDHODhP8jPkjgphkju3LILIUXmwor93gbYnR6opVC6AsS4y-PHGIybDqgSgjo_bzpr0fkU16g_XEETUexgoZJYaj1SY2txZ14vSn7UBk9xXyd7KzTVPwWWpw0s5rdP--vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
#نکته| فقط ۲۹ درصد موتورسواران از کلاه ایمنی استفاده می‌کنند.  @Farsna</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/467718" target="_blank">📅 16:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467717">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMDNODfNjqvHLHMGh3SvFffHEKfGCl_si6cZSF_Vr5lCH18WfUFHuK_Axob85srwwBTxjup18aWbl6oeimca4M445IHkQgltE9YJGqFprQ3bEZrMI-rH9xAJqAljXK5erp4bnZq_beNkYx3ZQPS_8FQ8vX6tHVq3EzT7cSvriMGslMyhkWtKVjD4ocyG9E56WnNmtkzqmlBtDeyviHbdpl9r7xN_4ONG-hBzjq6CJC2eEjM0djJp7VbiuycudkkGRrg9uflParYWL59aGz7sBZ55Cv_cZLJkExGx-NDkjUVklmsGRF_-DJpeAiHjHo90C-2SW61D-W-2OwgEBBj4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهر تخم‌مرغ راه‌اندازی می‌شود
🔹
مدیرکل امور دامی دفتر طیور وزارت کشاورزی: پروژهٔ شهر تخم‌مرغ که یکی‌از ۵ پروژهٔ برتر دنیا در این حوزه است با هدف ایجاد خط کامل فرآوری تخم‌مرغ درحال پیگیری است.
🔹
این ابرپروژه ظرفیت پوشش ۶۰ درصد تولید کشور را دارد و اجرای آن می‌تواند علاوه‌بر توسعهٔ صنایع تبدیلی و افزایش ارزش‌افزوده، بر تنظیم بازار داخلی نیز تأثیرگذار باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/467717" target="_blank">📅 16:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467716">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSG1g8EhUqVHDl2W29On3VYmZrr9261kRFTcxQdyunk_9_qOHqqoF5AsmWCrrsS1KU-VWDGtGRxu0kn-a75Btygx1qrQNubVMnH-XcwlAiawc4PxF12BMv3ktge7s0pyWOV6Zq3-zASFpof2740qsvRsN5K3SQyYmzZ6GmP4ZoXBIRvpv3lXuB8N94PPrcrg9VZQIMvCsU66aBrjCTZFDLfhqUK1URVnVnt74WRUDOlBe7zRHF7iusDTQiEwofhvwQTtBaU4XP_vRM07O3Y1WceJUxPnVHuhlLMq8A-EkB8DRXcp5HNVYwXgoX50QmYSi4_lsTJ0ObGCzTn7sOdicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد ۶ ماهه نفت پاسارگاد به ۱۸ همت رسید؛
✅
جهش ۱۱۲ درصدی صادرات بزرگترین تولیدکننده قیر ایران
🔶
شرکت نفت پاسارگاد، از شرکت‌های تابعه هلدینگ تاپیکو در شهریور ۱۴۰۵ با صادرات بیش از ۱۱۷ هزار تن انواع قیر، رشد ۱۱۲ درصدی را نسبت به مدت مشابه سال گذشته ثبت کرد.
🔶
به گزارش مدیریت روابط عمومی، برند و مسئولیت اجتماعی تاپیکو، مجموع صادرات شرکت نفت پاسارگاد در ۶ ماهه نخست سال ۱۴۰۵ به ۲۹۸ هزار تن رسید، این در حالی است که صادرات در ماه‌های خرداد و تیر به‌دلیل مشکل در تعیین ارزش گمرکی قیر تقریباً متوقف شده بود.
🔶
همچنین صادرات بزرگترین تولیدکننده قیر ایران در مرداد و شهریور در مجموع به ۲۰۰ هزار تن رسید که این میزان نسبت به مدت مشابه سال قبل ۶۱ درصد افزایش نشان می‌دهد.
🔶
براساس تازه‌ترین آمارها، مجموع درآمد نفت پاسارگاد در نیمه نخست سال ۱۴۰۵ با رشد ۴۷ درصدی نسبت به مدت مشابه در سال قبل به حدود ۱۸ هزار میلیارد تومان رسید.
@tappico1381</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/467716" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467715">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgxUoG0nNCBeCe8KM7UE7LbyhLCiIr7MmFe6ddA6wEEUAwInad2TOOUCwZ8Rz6_lvq9bnY-ZwkmlQ01QnKkGhQqoYXjmQD1JjhNxHFVclKfaRoI8yELVwIzxIZFr2sXkKuNmHSKs8ihFXrIYzwNhoPBFDjtnBVJ19Z1f5fOPJS8RfMKi3SCB0Wp164Uh1-ardKTe16Pd9q3n9RlFN_C0aaMVrDvnwL-8uybAssNXPFQ6MXmpASiViyDs_RZBAcDbvdRGnCasiSNr8W0XWl-BHE_4ChGur8vS2ICDuglWSYtF8m67p_qKkgBGsLxGYlYd6j2upj60Cug_jJj8BmlKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
برندگان کمپین خرید کارت هدیه بانک شهر معرفی شدند
⬅️
کمپین خرید کارت هدیه بانک شهر با استقبال گسترده مخاطبان به پایان رسید و برندگان این کمپین معرفی شدند.
⬅️
به گزارش روابط عمومی بانک شهر، در این کمپین، امکان خرید کارت هدیه از طریق شعب و پیشخوان‌های شهرنت بانک و همچنین خرید کارت هدیه دیجیتال از طریق برنامک آپ برای شهروندان و مشتریان شبکه بانکی فراهم شده بود.
⬅️
در پایان این کمپین، ۱۰۰۰ جایزه نقدی ۳۰ میلیون ریالی به خریداران کارت هدیه از تمامی بسترهای حضوری و غیرحضوری بانک، ۴۰۰ جایزه نقدی ۱۰۰ میلیون ریالی و همچنین ۵ دستگاه تلفن همراه پرچمدار به خریداران کارت هدیه دیجیتال از طریق برنامک «آپ» اختصاص یافت.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/farsna/467715" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467714">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/farsna/467714" target="_blank">📅 16:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467713">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f263b498ec.mp4?token=WpSl_d6UU-sI5W2yqxZ_oTfAXdRGbnDjC7B8zCzjjQvMlV7N5gAP4cYfNUjwtN7KNVI1GIaVLf_74Vfd1T_jGelE8nvN2kdOYW-CpzQSV1Lzj7OAIdo4-6oZzgsQMVtJiGrd8j2j-YWkv_GOUQYGZ-Uwr6Xur-Rrj_0vDCkLP80sN3OGBBT27YVavOtOovz2wjD11y-sLWjZvAXY5wySw89D51F7hqk54-OobDPfvT1iNThWpUGJgLNjUKZDFbzuYEhJthfZtLKSPmssv6aEl3TrYd6nl-xjbf3_LP8J8kMEn83Lyie-aZf7vETw10yO2sSh0ZZFCJdv6QuLw4QeTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f263b498ec.mp4?token=WpSl_d6UU-sI5W2yqxZ_oTfAXdRGbnDjC7B8zCzjjQvMlV7N5gAP4cYfNUjwtN7KNVI1GIaVLf_74Vfd1T_jGelE8nvN2kdOYW-CpzQSV1Lzj7OAIdo4-6oZzgsQMVtJiGrd8j2j-YWkv_GOUQYGZ-Uwr6Xur-Rrj_0vDCkLP80sN3OGBBT27YVavOtOovz2wjD11y-sLWjZvAXY5wySw89D51F7hqk54-OobDPfvT1iNThWpUGJgLNjUKZDFbzuYEhJthfZtLKSPmssv6aEl3TrYd6nl-xjbf3_LP8J8kMEn83Lyie-aZf7vETw10yO2sSh0ZZFCJdv6QuLw4QeTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ دوباره در حسرت نوبل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/467713" target="_blank">📅 16:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467712">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afJDBiIYAGsxRbYVN63Mx4Jz_TNOvVPINFGzVxsyWCatAnSvUD9zWihujyqerUr8DEYJjuysdZzGlq55GSFH6qpySXT5LZDw4_sX2vBX5GLxL8_5FFMtkTBp7PrQyz9bpSfGVbzU46UbG6PLc7_ycrQ00JVDIXVrruXDjQYNKPfUwEEXA2fboWtJn6iFIfSlVo_tVKj-nEDuUGC7L3SqMOpeikiQN1_hau0hCctt6rcLhRsv3ZQ3XzUuWyCuEsomlvRozGGJKIUuK5dAdAp2JlhB5uXFuq9QZZbnwymlzuWLMYzabDPv-OPfQenwfPcu-yktoHsizKTH-t2bTKowlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
انتشارات فارس؛ مرکز جامع کتب رسانه
، جایی برای کشف تازه‌ترین منابع دنیای رسانه و فناوری!
نزدیک به ۲ هزار عنوان از حدود ۷۰ ناشر؛ از رسانه و علوم شناختی تا هوش مصنوعی، همه در یک مقصد.
🚀
🔍
برای یادگیری، پژوهش یا پیدا کردن کتابی متفاوت، اینجا را از دست ندهید!
راه‌های تهیه کتاب:
‌
🛒
برای خرید آنلاین روی لینک کلیک کن
📱
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
📞
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🏢
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
‌
✅
انتشارات فارس مرکز جامع کتب رسانه</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/467712" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467711">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcOqddvGfCpkAYxkAep4pOTvWbT2bziaun-ZIeDXOzUzf9EarT7o-FV7DwIj0r5ugLblBgFnU5wqLIbdt2scbPzX-_zu3s1HAka63G9OWQDxvf-Ac06ZHowC8GbQG1khwTOA2BIZsJis9W1gBLbS_wxiaH8mG182fWh1knGUHvpmQWEXUaDXqDASV40a95mPYA0anSY_i1M6sY0GWS1gZKRsLCKCIOgCHtoi51Np0sdXxNP50Q-R_F3-6ZpK9PKzE2C4bizgiVp5xURf7qecNzNYS-24yOBkSlrthcDGOGASDQstJVrxGnkuUCcWuq5pUTleWoMhw022To9ALy8J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیادت نمایندگان رهبر انقلاب از آیت‌الله نوری همدانی
🔹
حجج‌اسلام والمسلمین رحیمیان، محمدی عراقی، محمدیان و حاج علی‌اکبری، بعدازظهر امروز با حضور در یکی از بیمارستان‌های تهران، ضمن ابلاغ سلام رهبر انقلاب به آیت‌الله نوری همدانی، از مراجع عظام تقلید، در جریان…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/467711" target="_blank">📅 15:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467710">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732a21f86a.mp4?token=KD2YPmvq1orXpptcAfGR2d28rYsYLF2Yx9OI4bEPYueS6nSAeVs5ISNeooH-SSGrq34C9ixpbIwfLZCRU-kM5iDKhYJOBy96rZ-EGMDH7UIa76DJjqV1GS8F6UIrc1C8VpMVjVRmTdkKDJAzp64God8B--S7fdHb4L2byyfnlFcULPPDh-B1yRaYb0TtGQb5A_6rMnS3mBvD67teJDn_wH7GZPKDWqWureQmLcVLS5jRN3-VbOS1A1rSUn-9Kwg_nJmkttbz6rKcgmA7IB_8WxvRW90eyMv5av00fcqRvZFVMR1C8ZnXEfdLXAJ4MqH4QaZsKeMYnUYadFsZNZW0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732a21f86a.mp4?token=KD2YPmvq1orXpptcAfGR2d28rYsYLF2Yx9OI4bEPYueS6nSAeVs5ISNeooH-SSGrq34C9ixpbIwfLZCRU-kM5iDKhYJOBy96rZ-EGMDH7UIa76DJjqV1GS8F6UIrc1C8VpMVjVRmTdkKDJAzp64God8B--S7fdHb4L2byyfnlFcULPPDh-B1yRaYb0TtGQb5A_6rMnS3mBvD67teJDn_wH7GZPKDWqWureQmLcVLS5jRN3-VbOS1A1rSUn-9Kwg_nJmkttbz6rKcgmA7IB_8WxvRW90eyMv5av00fcqRvZFVMR1C8ZnXEfdLXAJ4MqH4QaZsKeMYnUYadFsZNZW0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور کم‌نظیر مردم بیرجند در اجتماع بزرگ «جان‌فدایان ایران»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/467710" target="_blank">📅 15:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467708">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jr5RMyfCD0NN3KdUsxiEJF2oFGbEEKEoQg69NW5YhoxwZdgKcBIqOzbmON3ji99NkLOPoemzDHoIy82-h7NukZlFUv41Ti7-XRqGZi0FRJdALgJMAE1b4xisBDApqIuGnc2m0mhbh8obsWk3pxEKRsNaZMLDasI5PRrwfy_iQak2B1ET2eM5qerZDvpmfK1XQEAhi5OAm2S2N2OrDs7P1sFOj-uttq1wCoRABoel-CpHdN1K86n3RTv6cU0SB7z5Cdr5qd0Xl-hP34tSXK9bAf1DB_B5E08ixH6gKH1EJy-CH61xwXTfbVMvHVz3f8YUQ6ZWJsHIKkC-Q1CQahbgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3a90c45.mp4?token=G37ipfaYc1SIa9__bXQPJc7Bv8RdMG_kXcEUGi9O2Q7mjnsQ_MZrfap9xdUbnRowNc7GCvCZeR0QQxKz_sgUKav-_fIh1XdJu-CcFW48-RxWBweAN_FYv-5nvFcRzxwT4IdlNLKOifRmNwDoJKMaW56gKni4Hk0zybR2MA9bCHKZYoFMViTzDnR50NcWrXE34MxSu5M9q3RMOsd-6Gsw-TMguiG1uCr8J9UcMiMEJP48HyT-SsGVWPzb6JkGqXIDAoEy8nc4PqelSEK-wB4W2-stIO3LflA1UuJoHqpwRfPpEEjtzltg8dzZw7DzkNikYoJF6sNOqNJ5tXl0n7hL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3a90c45.mp4?token=G37ipfaYc1SIa9__bXQPJc7Bv8RdMG_kXcEUGi9O2Q7mjnsQ_MZrfap9xdUbnRowNc7GCvCZeR0QQxKz_sgUKav-_fIh1XdJu-CcFW48-RxWBweAN_FYv-5nvFcRzxwT4IdlNLKOifRmNwDoJKMaW56gKni4Hk0zybR2MA9bCHKZYoFMViTzDnR50NcWrXE34MxSu5M9q3RMOsd-6Gsw-TMguiG1uCr8J9UcMiMEJP48HyT-SsGVWPzb6JkGqXIDAoEy8nc4PqelSEK-wB4W2-stIO3LflA1UuJoHqpwRfPpEEjtzltg8dzZw7DzkNikYoJF6sNOqNJ5tXl0n7hL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع خبری از آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه خبر دادند.
🔹
برخی ماهواره‌های حرارتی هم یک آتش‌سوزی بزرگ در این منطقه را ثبت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/467708" target="_blank">📅 15:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467707">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b0995a8f.mp4?token=R_gzwzOdeW-3FHaWJOIFLgKFhRu38PW9HUPn_cIht7VyHNkPyqs8ol-Xu_9zLUckC6PBKQF4Wso-R70p5FlxXY0lZs2_yQosdp4F3GT4vdXYlxWZ_aBh0hdcdjdI_z2Nr_sCOIOblWKCc7ejYfsvNKSLo44VvdQWU98CbfRkTZcD9-KweejlMlZXlRoeU647j7s2z0hvjJ2BQm5e6FKhaio-hDEtp8I2DWyLzBkjTFpZ10M2gELk2GYm9jMYvY1j8MKVJ_8-1UXlcKf_fM4A5oNc9pZJwZblBTAYzeWDs7yHmCUTBkMVhyahhWaJ3GYvv_U9lp48mZ4-dK_g-PnMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b0995a8f.mp4?token=R_gzwzOdeW-3FHaWJOIFLgKFhRu38PW9HUPn_cIht7VyHNkPyqs8ol-Xu_9zLUckC6PBKQF4Wso-R70p5FlxXY0lZs2_yQosdp4F3GT4vdXYlxWZ_aBh0hdcdjdI_z2Nr_sCOIOblWKCc7ejYfsvNKSLo44VvdQWU98CbfRkTZcD9-KweejlMlZXlRoeU647j7s2z0hvjJ2BQm5e6FKhaio-hDEtp8I2DWyLzBkjTFpZ10M2gELk2GYm9jMYvY1j8MKVJ_8-1UXlcKf_fM4A5oNc9pZJwZblBTAYzeWDs7yHmCUTBkMVhyahhWaJ3GYvv_U9lp48mZ4-dK_g-PnMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استانداری گلستان: براثر سیل در مینودشت، مسیر ۱۴ روستا همچنان مسدود و برق ۱۹ روستا قطع است
🔹
مسیر گنبدکاووس به کلاله همچنان مسدود است. یک نفر فوت کرده و ۲ نفر مفقود شدند. @Farsna</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/467707" target="_blank">📅 15:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467706">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">علت فوت امید قانونی در خوانسار مشخص شد
🔹
رئیس‌ دادگستری اصفهان: امید قانونی در ۱۳ مهر حین توزیع و فروش مواد مخدر در روستای ارجنک خوانسار بازداشت شد.
🔹
این متهم ۲ روز بعد پس‌از انتقال به بازداشتگاه، ناگهان دچار ناراحتی معده و بیهوش شد که پس‌از اعزام به بیمارستان خوانسار، متأسفانه فوت کرد.
🔹
گزارش‌های اولیهٔ پزشکی قانونی حاکی از وجود بسته‌های مواد مخدر در معدهٔ متهم بوده است.
🔸
روز گذشته رسانه‌های ضدانقلاب مدعی فوت او در هنگام بازجویی شدند؛ این رسانه‌ها مدعی شدند علت بازداشت او نیز درگیری با نیرروهای بسیج بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/467706" target="_blank">📅 15:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467705">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524a2e3d5.mp4?token=AD8EFrkZEhpBHI8rsTIa2EE3w75smY05B1pPyJKFIAnYauwVGhe7g2c-6mMFgIOQBSKcWh_cneTtKsrPe2UzrxF9MNnkIeVexxbzT--IYyD88SksEkMVPMLH4ylc-L7ayxzInU3z6zQ1iQHrBYHqDSb6X3-5plmhXu9hXXmy4t5uI29dg7E6ufx4P3XzmZcJZINRMMjM8QFLf9DUiryyokFa0pR7sqYXlAcmXuqAA9yniiJhfJIIUnyIGNh-gTSd6BEx8bg_gA-7wK7UVjQi_GBMLzCkDK6Q1VetRr4gZT-TvaiFlcGjrUt-218CrtQLjAKGLnVubY_rtcRRQDiTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524a2e3d5.mp4?token=AD8EFrkZEhpBHI8rsTIa2EE3w75smY05B1pPyJKFIAnYauwVGhe7g2c-6mMFgIOQBSKcWh_cneTtKsrPe2UzrxF9MNnkIeVexxbzT--IYyD88SksEkMVPMLH4ylc-L7ayxzInU3z6zQ1iQHrBYHqDSb6X3-5plmhXu9hXXmy4t5uI29dg7E6ufx4P3XzmZcJZINRMMjM8QFLf9DUiryyokFa0pR7sqYXlAcmXuqAA9yniiJhfJIIUnyIGNh-gTSd6BEx8bg_gA-7wK7UVjQi_GBMLzCkDK6Q1VetRr4gZT-TvaiFlcGjrUt-218CrtQLjAKGLnVubY_rtcRRQDiTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کوله‌پشتی خونین آدرینا به رئیس‌جمهور رسید
🔹
فرامرز پگاه، پدر دانش‌آموز شهید آدرینا پگاه، از شهدای مدرسۀ میناب، در اقدامی نمادین و در قدردانی از مواضع قاطع رئیس‌جمهور در سازمان ملل، تنها یادگار باقی‌مانده از دختر هفت‌ساله‌اش، کوله‌پشتی آغشته به خون او را به پزشکیان تقدیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/467705" target="_blank">📅 15:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467704">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3UME_qwO8hdUXutrj1vCXcPSHy333Tx7RPO7Oy5goY6D_gjAWvpT6zHcBY0-pmKFSYSCq15TPzrYtOtT-t5yHME90ZaD5NhJbPgMnsayOUn700FvTyUGUg98eyL2I-k_lFkQj91ET3ozBpp8hO1tMyaiCm9gJ1LL2dkZvUGcRQPInSi0GamwbXMr99-Eo9gYqrloymIzokgKPR51Ix-vS0ohJ3htV1q0cqwYFRacf3mBewivAB4LF-KWq43jFZU8o834OnyV7kN9MrIEnL6GYotXYhVCrKO4O1usZb0MnEXEsAIH03Ze7Cs96-ETL_Yjb5Ux6p5liY69WeYvofTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۵ ریشتر در عمق ۲۰ کیلومتری، سرپل‌ذهاب کرمانشاه را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/467704" target="_blank">📅 15:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467703">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f1f7fd598.mp4?token=BISx9au7S396OpPek1G55Me5AnrbO1Kp4jCL1PLJRhsJK6_w_JK-KEKtv_nogGMNSLlxtuDBkBbFSW_YPyH7RWNM8mt2z6idi9MzguLrXzVlIleIExhL3jrESOE2ySwfRH2W-77mMZZ3MsPDzbcKKdvLCUGaL3D30AU7URPktoCKcyrnFEsOUv616969wwNagRF8tQnR2MGUbUPlY5p-062PtY2bgJO7cai37jFx3dDJwyUCeT9xYvLxHC9zJtZjFGC_h1V9kBcfXdqGmsmXfu1TxUM_e0uPYRM_q8qBd1bPO3fshz_PIBxWGtDa_jxZBMiHrjRZvotqFKiTfMHF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f1f7fd598.mp4?token=BISx9au7S396OpPek1G55Me5AnrbO1Kp4jCL1PLJRhsJK6_w_JK-KEKtv_nogGMNSLlxtuDBkBbFSW_YPyH7RWNM8mt2z6idi9MzguLrXzVlIleIExhL3jrESOE2ySwfRH2W-77mMZZ3MsPDzbcKKdvLCUGaL3D30AU7URPktoCKcyrnFEsOUv616969wwNagRF8tQnR2MGUbUPlY5p-062PtY2bgJO7cai37jFx3dDJwyUCeT9xYvLxHC9zJtZjFGC_h1V9kBcfXdqGmsmXfu1TxUM_e0uPYRM_q8qBd1bPO3fshz_PIBxWGtDa_jxZBMiHrjRZvotqFKiTfMHF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارندگی‌ها همچنان در سواحل جنوبی دریای خزر و شمالی‌شرقی کشور ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/467703" target="_blank">📅 15:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467702">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9dcbb0f2.mp4?token=m13hi4_sCTkn3GCAJuQ8U3AcIz5N0Bc6Ax5P2sJiE-F2a1J_lAHOsMQCfx05gUyn3Qko-XCc1AhC61Ys61XxVnxxsU0qknkRpTnSs-Hu80WXp5wqyJ_ZSVsnTqTmi1scoV9b9_BluiA2rhRZ3_L8zpiXVuy47eCtIjrkSgYPFptdhM0DF-k8f4MIWcI1nCUQ6PIAotphlxjL-TKb00u7_U-rrwBbC12kcxcqcTu_m6SDFpnXltuqMC99BQVtzCgbsS73XaHtDGT3xbWTj9HcW12oOHMKt_vgxfeApfHBeibvqu4LiCBYNC8NJnSISYB1oLJ6KkcL3-Mn2xl1nlLwcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9dcbb0f2.mp4?token=m13hi4_sCTkn3GCAJuQ8U3AcIz5N0Bc6Ax5P2sJiE-F2a1J_lAHOsMQCfx05gUyn3Qko-XCc1AhC61Ys61XxVnxxsU0qknkRpTnSs-Hu80WXp5wqyJ_ZSVsnTqTmi1scoV9b9_BluiA2rhRZ3_L8zpiXVuy47eCtIjrkSgYPFptdhM0DF-k8f4MIWcI1nCUQ6PIAotphlxjL-TKb00u7_U-rrwBbC12kcxcqcTu_m6SDFpnXltuqMC99BQVtzCgbsS73XaHtDGT3xbWTj9HcW12oOHMKt_vgxfeApfHBeibvqu4LiCBYNC8NJnSISYB1oLJ6KkcL3-Mn2xl1nlLwcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوپرنفتکش متخلف در تنگۀ هرمز درحال سوختن است  @Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/467702" target="_blank">📅 15:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467701">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1xixvxceK6F0J3v0OA5cpPrKm2CNx0MMu0wOM25UT49Df75LtW413VROD0Q5iSwLVdmomT8-V19eGBNT2LwTPCUezDyN-rVzGnP5Rc5sOaOdepDVMV2-8yUPxiRRLhhU1G9TMKUD2Z0BRoOmQF6SK9gQaKi_iLFgDa0TKO_WH1DadKoNa6PD5b5OxXu5PGjWuo5zx828iGzVR7M_YlzETKPcXGZc0feDLmqFVn8mBh1hna3YBE0Uq4QlOXzPg3MG5yyC15qiaaRmlnYFsYUvP_QQqG7DJeS0hG-FX8aJwRAUVXQt-GWyGmVJhYtx3dmGLa01eYjPOsHgxOyB5FKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تحلیلگر بین‌الملل نفتی: مجوز واشنگتن به روسیه یعنی تنگهٔ هرمز به این زودی‌ها باز نمی‌شود
🔹
ردیابی محموله‌های دریایی توسط هوش مصنوعی ویندوارد نشان می‌دهد که احتمالا نخستین محمولهٔ گازوئیل روسیه که به‌سمت ساحل شرقی آمریکا حرکت می‌کند تا ۷۲ ساعت دیگر به مقصد…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/467701" target="_blank">📅 14:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467700">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOtB6MKZQ5h2FEF9tH0rjrQ0iPtWzWwiO9i81i5aEbDbwBBOWntU7z2xELiU2pGN7VR0crFjiDXWqW_pq2YsMk_rGHhKrniYf4tSAupqHudKA7FwNs9xyEp0JGjBN19RsLGfGPCYiUoLm1MAf_KCTWhF4j-6B1Ivs1PSpe0pW-Rd2-dMJchzrt-9PY_gEfyiwj7CoZ6oa1g9uO7heUTfMO1UplUs3VxFqJqDGcUTjQ7VHV139vydKj8itkVwCR-Ctrh2M7iNxVukxfY0ouPAW6It_-dObakDDS6b44ohgDRLF7KUj5689S5teBzVoDaOzPXBerQg-BeQQR4PWgJ9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار مجدد یمن به فرودگاه‌ها و حریم هوایی عربستان
🔹
سخنگوی نیروهای مسلح یمن با هشدار دربارهٔ استفاده از فرودگاه‌ها و حریم هوایی عربستان اعلام کرد: این مناطق به‌استثنای فرودگاه‌های مکه و مدینه در معرض هدف‌قرارگرفتن و صحنهٔ عملیات نیروهای یمنی هستند.
🔹
سرتیپ…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/467700" target="_blank">📅 14:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467699">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268bcae3d8.mp4?token=fzkAfGNfyKj8sJ8FoJZ9I-FJxoNQiqi8viOPDYaitR4hz7hXN0KuH-ibXyldI5GLbfvGPLG-vM9gemRZIaua7sEahdAcOds2OVfWAUJ5YnyhoLuKeEPcd59PUfw1SbDa3elbX-n9du0ca3huuLE6WIzYEzo2wzWwzSFLAxSeIwopuaNV4HwaIVEdURuwiuJwykR8xstHEwb11JED7KFloNy2u1jOfmE9MJAPQ2gAIWM4dX1jDM7CzJHL9MQ9e3n391qI-Re3GeWW8HjNG8j9W5DhvYmQu5DUlxnKkb0I6l60UcAaWuB-hBRY82cjeMIDVcY5zmXM6cHy-i_z7fgDwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268bcae3d8.mp4?token=fzkAfGNfyKj8sJ8FoJZ9I-FJxoNQiqi8viOPDYaitR4hz7hXN0KuH-ibXyldI5GLbfvGPLG-vM9gemRZIaua7sEahdAcOds2OVfWAUJ5YnyhoLuKeEPcd59PUfw1SbDa3elbX-n9du0ca3huuLE6WIzYEzo2wzWwzSFLAxSeIwopuaNV4HwaIVEdURuwiuJwykR8xstHEwb11JED7KFloNy2u1jOfmE9MJAPQ2gAIWM4dX1jDM7CzJHL9MQ9e3n391qI-Re3GeWW8HjNG8j9W5DhvYmQu5DUlxnKkb0I6l60UcAaWuB-hBRY82cjeMIDVcY5zmXM6cHy-i_z7fgDwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار نخبگان و مشاهیر تهران با رئیس‌جمهور
🔹
پزشکیان: قدرت را در خدمت به مردم می‌دانیم، نه در زورگویی. نام‌آوران و نخبگان با قدرت بمانند و کشورشان را بسازند.
🔹
وظیفۀ ماست که تلاش مدال‌آوران را که در عرصۀ جهانی پرچم کشورمان را به اهتزاز درآورده‌اند، بی‌پاسخ…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/467699" target="_blank">📅 14:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEUUlLYd8vH-Rcw2KV_GxhK1DQppkRuT0-dOkTLPiEuyI6IzJ3EaLeGZ6iFvDZT4cp0yxGtJ2p-R_BhMA5_lX3cdoSaCKwmRDGMl85kZ5dnsXh7XOkUCIUiXUc_C23YAwcEsO7PX3k5-9F2RL_Ke3qmFFlD1V-mT_xjGSmBsfzi74gSeSwn7IWsZjjWRBURvL75Oihvg4DaDvj_1_V2j36KoJWM8jBVyRqrv14aywqCGeyTjYaVumtoMblK0G5kI3Das6saXf6kItQ3I1rMVn0Xqf-CmmooefxUFGJrmFryaYg7neCUrrB5ECPQCOBoOtq5Sb6ubRBJNZ_wEjwKCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3gSVFx6MN8O9x3_GpcurolPaJCMz6kcwnyPtUHhJWblVLU2dmbkAAra_KtIjhBJSzr8TaZoE59j8uihlSm739SMLlPzNJgBwzzBdp1kMt2Go1x-nPEJ8RqWd6ZEEcGETmhwWOh1_K3i9782g-u4JOSKeLIbGPt1WmJXhN0_Z4BsLnHzlHzpJa6yeHg7mRsBKfG_JBL1X7G8FfOb8Se4U1oD75iCjtPVFkljuAPNl9Gv8sqRLqaj0zwGOOHrK0DBbZYGP3mFqXnPH3rECCAopppr--_eH59uNk_8tSs69otzf_wTS8OCcYj30CnKZJxfJ8gUzebGM4b_uN73YW1tpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agZbbQiVfWzcBscOckbyesZFnUUODwE0tchX9HVgUUPYRndcK2K9I6ht9gOz7nRFN41wh6JOuH9-9OLDsIj40nuo_VOHPrQ3ibENi8OjpxfKZnSfv3vVUU1PkDhEHgVAgbwXG03Gxngr2FR-gWbIkVKLuOpOXhg8RYKL8fhFqjaGVSyYjkov0_qjGrTliVXiaTmN137suuLxQb4fFVtcBCprktJM3WZKB24V2p5jRfri6elYfmFOHHZvE4-qGdrGZNekwXEkYBfaV2TK9GpbmkcBCLk7i6FJMF7LhdVAPRj0pC2-SicKAI_ZukMFZ0lJAJl9rSzMFuipRC0fnx3_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHY_Gp1SvkC669y5y0qnoxLAfdTss5cyO58UQ1AAHUpgJ1JVcSgOalbkkIg3Oe7uoDRFLZ2y74C9-nmDJkEZryIW1FIaamUys3jSn6pipwZHYl-JjAnEJ7IBQJENq27YkQSNj41z-Hp0V94lGnoS_V7RkP1_8ftGAxOWqZDKPPGzH0xUMJst05fZ2oay7w0GfXHhqftUKkm-XYlxyMwTuM0KkASdok6iMoj4AhKMJcIQWXqHHYxRF-K7WHgfrGz-GJkoihh72EGhI1kJ01NTz0msOfmP4yoBFDjB7WEU3KGpDuRamcQldcfscGSQu-QuEBrCZQFOU-a2enmy3qzqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2HplVJUCSnK-cmWVo4jmmvXKHi_axHfR6MCMok6xSTqjWJqxF7z-8yRFEcL4BSB6HS_d2Nu4_CV1F5udkx3A60e-JZPDhiXZe6MDd-QzAl8vR6KlbaZtp6n08fc5XI5b0IQ6rO89_688k-uGsTUiFpcJ2s3tpvAYKnpEgjG3AKtWOG8KkJadnakzJH6qgE3SADw_p5sh5QKtGEQ2PYugwfH-AH5757iAm7of00s6A7Ie-nzBWedc83BiY9N9ODAuJsdJlzImAkev_ODO776nWjM9aUHqbqZNOuUxBeAQC4roC7yGvuQsjVVDGgbgedl0Y4gB4sxQIqrjq0Egw7pLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGJGW5O7tW-ph0UAIIqMdiVentfPXmhYH2cCjh3CGE_YkzjACqTA9MBSjiULJy4ZtE1xiOH1dgjjk3ST70eD86PXtSgH7wbLeXaSb6n9rvWqIGWcli02Fr_GacU9azTqTSBivhfm6OC2Xgzc47MoUiFn67Taw7C2WUG4kwp9euKuoue-P7m6Jplp_R9dHn_dvGyVQZrpbS88feXP7gwcb0995lIKwmU6CvfNYPUMpp4GJoh7eVKok-daN8GGO3BhCWgsgdRnBBMxvAzfc4M4_YYcZMqxv90bZFzdJ1NKvh7dnbu_uccZ-eGxW-yh-6PrIuoXqcVHOZENSAVegEXiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCzi9mBQLYSo1OWJvPyB89oKMe3XRCrhusXefQ04rJHA5MD1h8EKckbr-LUqeXXJ9zBWgj7I0slQOQtIaTE0qg4EykBoxOyVB3iOwUkVeIqtCWt-Kjhgiwp4BD8uGob9tM27U-bs4LxWv_9aKAfef-IlppiZ1rt2T8bapCohKms4Hh1-nyLsvj2dEbkC5WDkpKITgCTwaOxztuEAifwS400eowReM1tGVB8qnXVJSo4Bu59J4yUKhAdCD6rOYq3TXJzKpblHvaOkLiX4UcuFYu2DYIE2YCg7tGVKaiXs9vdQFwmXw98v0CvsKsQdA9ygLiiCit1K6-tVhCt9Nf8AEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همایش اکوساید؛ جنایت جنگی خاموش
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/467692" target="_blank">📅 14:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd521070c.mp4?token=aQXvT95PsjKvsc2fOs-QPq5QhTSrnnwRHK6HCYIP8O_coyESGRLxKefmR0zef7vbqJrs8QJ1pT-vhixOklL4Ym9wlSkSZYnpwSAFVnbXtmY-JCdfEvQ0dQLlN4lHVFPbLMxUyGhqmHjESrNagqg86z9yqVPO9Lm9jdw2bmF-yqlrXAbkbIVX_Sppr0k48JiLR-6EN5pfdlzuuBQjUsNG4tb4KYBl-RDxF9h2EjZT1a7tW5ZKC5YY0_8W25g9n4jHAy01SBwAw8f-wGHGoGVHPjdNg0zxM4LSY0YF7Lh3C5H50iYzU5Lz5JfsRhwtNWh9YWa_SwgK5SFRqwH8BYTCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd521070c.mp4?token=aQXvT95PsjKvsc2fOs-QPq5QhTSrnnwRHK6HCYIP8O_coyESGRLxKefmR0zef7vbqJrs8QJ1pT-vhixOklL4Ym9wlSkSZYnpwSAFVnbXtmY-JCdfEvQ0dQLlN4lHVFPbLMxUyGhqmHjESrNagqg86z9yqVPO9Lm9jdw2bmF-yqlrXAbkbIVX_Sppr0k48JiLR-6EN5pfdlzuuBQjUsNG4tb4KYBl-RDxF9h2EjZT1a7tW5ZKC5YY0_8W25g9n4jHAy01SBwAw8f-wGHGoGVHPjdNg0zxM4LSY0YF7Lh3C5H50iYzU5Lz5JfsRhwtNWh9YWa_SwgK5SFRqwH8BYTCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی: بانوان پرچم‌داران نبرد فرهنگی با غرب هستند
.
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/467691" target="_blank">📅 14:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b9c41785.mp4?token=FNrhrCL10rcQJEbGn6OqKZQzJlL46XzkkW55YhmMFumIGWUvuU7WBNG0nwtinv-rS2pBRG3Pf2EVnNJrVW-jbJXtfgluW58o1gfXhOvjWUcuz6oaK7BZGblUzjKNPG43ZyCG_-47hX46Pkj8ZkokSTMybUjHxx_a1WaaFiT1oQ7_R42Seev485orLMq9aN_61DeEktwyQS9Mdj322i20rh7Pt-CRnkMrtvZw_kz4qez7MF1VFY78jD5Brfh2aoQCrngmWls4_IeyKOciqfB-VveTP-l8WA9-N7VkoCbSsjyRpY1YKEbyosTXkcK6rzSadFYwtIQ4V9HlAm3tIRK7UkBJfridrfLXZC72lTW1McVQ364ZgrspavoETOZ_KyEhj8KdTib_zGC-CPtqWtW8VU53cjSNp8UOd3IDs7cGwnJhKip4luHv8jI9UEf45KsxPpiV-dgpspac7IHiuQv-VUVUV9Is5PsChelmj4Z_iGuefZSiA2fS9haJCWXFcGEITLlyumKcHPAopRnTYLha6p-BgLBRodrd7oHQdUv6Y6EcoGQhKhb2vpKde7y2IAW0dWRLwb1k4yQhSE7SYfzL61fLgWGtSZ-pH_SayeXDlGZpNjrse-QHlEzbDVEVv5TV-5oBrfCqFNX44Dfhz04xP6hDuJRaWQ_KtTiQjL6ESK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b9c41785.mp4?token=FNrhrCL10rcQJEbGn6OqKZQzJlL46XzkkW55YhmMFumIGWUvuU7WBNG0nwtinv-rS2pBRG3Pf2EVnNJrVW-jbJXtfgluW58o1gfXhOvjWUcuz6oaK7BZGblUzjKNPG43ZyCG_-47hX46Pkj8ZkokSTMybUjHxx_a1WaaFiT1oQ7_R42Seev485orLMq9aN_61DeEktwyQS9Mdj322i20rh7Pt-CRnkMrtvZw_kz4qez7MF1VFY78jD5Brfh2aoQCrngmWls4_IeyKOciqfB-VveTP-l8WA9-N7VkoCbSsjyRpY1YKEbyosTXkcK6rzSadFYwtIQ4V9HlAm3tIRK7UkBJfridrfLXZC72lTW1McVQ364ZgrspavoETOZ_KyEhj8KdTib_zGC-CPtqWtW8VU53cjSNp8UOd3IDs7cGwnJhKip4luHv8jI9UEf45KsxPpiV-dgpspac7IHiuQv-VUVUV9Is5PsChelmj4Z_iGuefZSiA2fS9haJCWXFcGEITLlyumKcHPAopRnTYLha6p-BgLBRodrd7oHQdUv6Y6EcoGQhKhb2vpKde7y2IAW0dWRLwb1k4yQhSE7SYfzL61fLgWGtSZ-pH_SayeXDlGZpNjrse-QHlEzbDVEVv5TV-5oBrfCqFNX44Dfhz04xP6hDuJRaWQ_KtTiQjL6ESK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تعطیلی فرودگاه ریاض ۲۴ ساعت دیگر تمدید شد
🔹
وبگاه «فلایت رادار» اعلام کرد که تعطیلی فرودگاه بین‌المللی ملک خالد در ریاض برای ۲۴ ساعت دیگر تمدید شده و این فرودگاه تا ساعت ۰۰:۳۰ بامداد فردا به‌وقت تهران بسته خواهد ماند. @Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/467690" target="_blank">📅 14:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3191d92d8.mp4?token=CVMX4S2B6H4d-E7id4rSDHbWCQpC6abOteHtiO-GLPTCEkmz92afAH4EHY-N9fWpcneJ7yulZo3RuIk2VsrRoMWzyskMosxmFKFzdD2jMTvlBrgUFPj6aE0Ccvu4_WDvGGU61eWXI4o7riE3Jtpc3t9LpYBa1PNanD4gmkPqD93izeFraR5GUrfsxK3X-KiD8q9pnP1Qv7McIZ1AVvFzVOKsEYh-klASdVd2fhC42DujXwKb9CGh4SJNnUrOR22eyXTgwKBl5E_y1PMQSZWo1aDife0oxiKm-vYCUQYYsjYZlYzvLrlsu_spOLGh-t1RY10Ibn-vMAfb_uXbd-PfDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3191d92d8.mp4?token=CVMX4S2B6H4d-E7id4rSDHbWCQpC6abOteHtiO-GLPTCEkmz92afAH4EHY-N9fWpcneJ7yulZo3RuIk2VsrRoMWzyskMosxmFKFzdD2jMTvlBrgUFPj6aE0Ccvu4_WDvGGU61eWXI4o7riE3Jtpc3t9LpYBa1PNanD4gmkPqD93izeFraR5GUrfsxK3X-KiD8q9pnP1Qv7McIZ1AVvFzVOKsEYh-klASdVd2fhC42DujXwKb9CGh4SJNnUrOR22eyXTgwKBl5E_y1PMQSZWo1aDife0oxiKm-vYCUQYYsjYZlYzvLrlsu_spOLGh-t1RY10Ibn-vMAfb_uXbd-PfDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی، معاون وزیر خارجه، در بازدید از مدرسهٔ میناب: درحال تشکیل پرونده‌های قابل‌پیگیری در محاکم خارجی هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/467689" target="_blank">📅 14:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab715d3df2.mp4?token=fKCMetIVO-3E0y6WCk6v9_nVAWjH8wfmfy52a5qFHj7X9lC1T8K-SLwuBOrjDrPxY55d7rTrPYR8qK0SYg7-IaCThxyONCs_IOyNtnC5y8aTotULAVHC7C7cxlCQbbV6ckpGgiN9Y22VItSNVFadL2LjEzA2ZWyEO-pxS_uRoG9XgYPb36BCiIwTIr3vJHWmryLs-YHaTVYzqKfakaFj2fYC9_yB7wdGNK-qRoBBC9FoeAryMTq1mTE6nPF9iwZdJSgUoG_AgeKqpaezkgUvyGVKI6npIOJe61u_I3PN9qXr6UuuHSKBEj_VcsOWzgnT0iXqBK3YjRFw8DwQKNBHRK8K8Lr3MJKgTMISZBNQTErHY_UaFK0boKy68ZL2AlTENzynO4yjECUQhVeInz0UpiFSHdB-mM8UJ8aCL5jnvbJC4mx1loGWmwOz6XVXCf1jfKHGz03zq69Tn4j8PXX12ygJ1D8LsOXD7Bna_1UurfEEPoJ3Lz_dPHjeyy2wowYBgmM38qSl3UaYvEinMsMzoPdGSAsWomt0T5in8_d296ryIv7u6OghZ2edglhMbdz5DkAqyZsBfjUwfwPlTnwysQkLg0GPttxvMxwRZbwQTsdniLvJxTILOoF6lft6U3y4F9KnyL0TF36fwJm-BfGLTVFKxdI8VoL9XHoBQNoxgug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab715d3df2.mp4?token=fKCMetIVO-3E0y6WCk6v9_nVAWjH8wfmfy52a5qFHj7X9lC1T8K-SLwuBOrjDrPxY55d7rTrPYR8qK0SYg7-IaCThxyONCs_IOyNtnC5y8aTotULAVHC7C7cxlCQbbV6ckpGgiN9Y22VItSNVFadL2LjEzA2ZWyEO-pxS_uRoG9XgYPb36BCiIwTIr3vJHWmryLs-YHaTVYzqKfakaFj2fYC9_yB7wdGNK-qRoBBC9FoeAryMTq1mTE6nPF9iwZdJSgUoG_AgeKqpaezkgUvyGVKI6npIOJe61u_I3PN9qXr6UuuHSKBEj_VcsOWzgnT0iXqBK3YjRFw8DwQKNBHRK8K8Lr3MJKgTMISZBNQTErHY_UaFK0boKy68ZL2AlTENzynO4yjECUQhVeInz0UpiFSHdB-mM8UJ8aCL5jnvbJC4mx1loGWmwOz6XVXCf1jfKHGz03zq69Tn4j8PXX12ygJ1D8LsOXD7Bna_1UurfEEPoJ3Lz_dPHjeyy2wowYBgmM38qSl3UaYvEinMsMzoPdGSAsWomt0T5in8_d296ryIv7u6OghZ2edglhMbdz5DkAqyZsBfjUwfwPlTnwysQkLg0GPttxvMxwRZbwQTsdniLvJxTILOoF6lft6U3y4F9KnyL0TF36fwJm-BfGLTVFKxdI8VoL9XHoBQNoxgug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم خطاب به وزیر خزانه‌داری آمریکا: قدمت آفتابه‌هایمان هم از تمدن شما بیشتر است.
@Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/467688" target="_blank">📅 14:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC4j5NMmSNIUyRETVVU1bXO_jPQhUx9rgjchZHwvhcyJp_EkrpNJcKvL_Rq37JaimmZ7q9V_o6ylRkzPOLKymDDaTnuqs1tYRvNjV44NktFTiNS0WloZUBZTz98cFEr-PuDe1QvRqErAENLvSqRf8FjGEhZF7GMjHaT1XjwX-YT5G-fEYU24vbNq79qtOfi5C6M3-hXQ2jwjqTpypX80goToFiU_9oxUGjYyaN4CDHFmdgJpQmo0gFu-wJNXSUSPWYJjEOd6CbYZOfQbIJiGH2hqiCgIfhX2pNcUpB38RsvJCqgobX2ieoeb3Mvw-SZEZrVY-nrrbi57Qyto0t9bOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غرق‌شدن قایق مهاجران در جیبوتی دست‌کم ۱۰۹ کشته به‌جا گذاشت
🔹
در پی غرق‌شدن یک قایق در سواحل جیبوتی، دست‌کم ۱۰۹ مهاجر از جمله ۱۵ کودک جان باختند و حدود ۱۱۶ نفر دیگر مفقود شدند. این قایق حامل ۳۵۰ نفر بود که تاکنون ۸۰ نفر از آن‌ها نجات یافته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/467687" target="_blank">📅 14:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTRFwYdXDDvoAUBC-qOk98RMXUHyJIrWqspCtCVgCIKx1AvVLyXPY4NGrBxoLMXi0Z3AT0pQIr3uEKgSwJnYSntCQ9FrfQrAWz8G3YanJkAidovakc2nT74EWmc2NchXgwlbF5qWalMjGO-q0kYUI47Bcp89VpID4MIV4yPTsLGEVxBhLWTs_NyLRPbbSRh4hQq1gfpXLg8-68otvSKWDFvZS5UaObII01-UUTplQefIP-6kE4hJq7uE8zBLTouhuyPyAH-I8RDl4vTJIMLZOcXM1QPIrUfQMr8BpueVWQIqXsTkG5OmYvH3sE-DWDRlLDq1b3ot5txfLPp5ZWkF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز تخصصی احیاء امر با همکاری اندیشکده هیئت برگزار می‌کند
🔹
اختتامیۀ سومین همایش علمی هیئت و آیین‌های مذهبی
🔹
با حضور مهمانان ویژه: آیت‌الله عابدینی، دکتر سعید عزیزی، حجت‌الاسلام محمد قمی، خانم دکتر ناظم‌بکائی،
دکتر انسیه خزعلی و با اجرای: نجم‌الدین شریعتی
🔹
۲۳ مهر مصادف با ولادت حضرت زینب (س)
🔹
مکان: مرکز همایش‌های بین‌المللی دانشگاه الزهرا
🔹
جهت ثبت‌نام به
تارنمای همایش
مراجعه نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/467686" target="_blank">📅 14:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8de2b8cf3.mp4?token=R98Fw_CrGsqVqm2nGBCrPb8CBMvJDnSEJAS3mztIr2J-ydcQNhOfmVjNMH1snpqCm1DZ511GJNZMP--TjW0Mc-os6b1OaSRNLDQD5QToPPUl8Bp3odeIdhhlzG-6nAi9bLMOcS46mlwz-96fzV79LTlozbzxfUUmALCdFrRaAD5ZufHvv1XjRJImdpBTyfz3QbIAU3SMTyfaDVrdId52ZEyJevQhyy6psg2OFZUpuDaL6ILxeJDdTyWU9zMMSnm2ycx_FGEoVEak68DZXuEtW_Qa5L3nIeNi8994Obrv6Hi8sQCJdrB6JK1iucc70gOGWgqPwv2gCyDQKISB_ThBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8de2b8cf3.mp4?token=R98Fw_CrGsqVqm2nGBCrPb8CBMvJDnSEJAS3mztIr2J-ydcQNhOfmVjNMH1snpqCm1DZ511GJNZMP--TjW0Mc-os6b1OaSRNLDQD5QToPPUl8Bp3odeIdhhlzG-6nAi9bLMOcS46mlwz-96fzV79LTlozbzxfUUmALCdFrRaAD5ZufHvv1XjRJImdpBTyfz3QbIAU3SMTyfaDVrdId52ZEyJevQhyy6psg2OFZUpuDaL6ILxeJDdTyWU9zMMSnm2ycx_FGEoVEak68DZXuEtW_Qa5L3nIeNi8994Obrv6Hi8sQCJdrB6JK1iucc70gOGWgqPwv2gCyDQKISB_ThBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فولاد مبارکه فراتر از صنعت، حامی افتخار و نشاط اجتماعی
فولاد مبارکه در سال ۱۴۰۴، با حمایت از باشگاه سپاهان، ورزش کارگری و خانواده بزرگ کارکنان، کارنامه‌ای پربار در عرصه ورزش به ثبت رساند؛ دستاوردهایی فراتر از تولید که در مسیر مسئولیت اجتماعی این مجموعه رقم خورد.
@farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/467685" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtU_f0YmGu4nhNg8J33gBYR_CEXTDoGeiI1jkcrjvFnzfF8rVMj8ezk_EKTvYJGTn5Ayx2xjrRZU-K7U5MRr5DNvfc5Y6T-XzgK6JZj9pLPMyf7fuF__mMTp4k3BL29f8XlOoKN0bJMkxV57Vkf8y4ACSffs2g-N074QSnZz9md4oXUwnBdaeisdgDTwShfWDud3FmZcgmg1pfh6fsF5d6dFc6eaNECDp6l0t6iw0oUgw31gyt6Dy_tqkPjGPzsXwEUGiydiB8ou-tNe3o6igqSf4ek65EORMGCFpXDX_guJ1rL7x2S-rzGoY5hBVXUDpLzH1fWBfmVnlAQhQ8zWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/467684" target="_blank">📅 14:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/467683" target="_blank">📅 14:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf490e3aa.mp4?token=rpNa2UrJq9VRbwWtFKar0snon0ESCbsZbRC4Xd0ZCeSgFwjvCj6NoiFJJOEP6DexEFxOpdIqrWHSxW2J4mW0CI3lzujnukRGhBeZxS3t9w5vyOWahxV3ysYNv3a-O55nVbkxovWTwQli0oNuB2KRM-4l2L1L7C_x2J4DQOicGxIbpINijRgD0rP54g_9Cp3igxhyBKHXzCwyhK6bP1tuY7ivZ0odG1wt9vscFGPtpkNORuOZxhQtLoESEcp1gNhEqwLQaRGyaWmuQCu-nBeG-SAC1iM2fTtirrq1z_ZqT9zOunPkgcawBP6s17dTiJE3D1gssULucBncJOMa-iRiFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf490e3aa.mp4?token=rpNa2UrJq9VRbwWtFKar0snon0ESCbsZbRC4Xd0ZCeSgFwjvCj6NoiFJJOEP6DexEFxOpdIqrWHSxW2J4mW0CI3lzujnukRGhBeZxS3t9w5vyOWahxV3ysYNv3a-O55nVbkxovWTwQli0oNuB2KRM-4l2L1L7C_x2J4DQOicGxIbpINijRgD0rP54g_9Cp3igxhyBKHXzCwyhK6bP1tuY7ivZ0odG1wt9vscFGPtpkNORuOZxhQtLoESEcp1gNhEqwLQaRGyaWmuQCu-nBeG-SAC1iM2fTtirrq1z_ZqT9zOunPkgcawBP6s17dTiJE3D1gssULucBncJOMa-iRiFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رویداد ملی «جامعۀ سلامت، مردم‌یار و مسجدمحور»
🔹
دوشنبه ۲۰ مهر مسجد جامع بقیه‌الله الاعظم( عج) سالن صدرا
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/467682" target="_blank">📅 14:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64de53cead.mp4?token=XorxQojwNt70YN8BFiAWcEBDCS_Fwuut5kNnYC60W9EQRwhqgx14qev8IbQrWLOW08Hxd-WHrspE8s4ZIyHvZ77GMjWKX6bp0kQkZojIkDFNk7SpZh7b3DF717M1ta-qjDueFyNkb8JJhug5ocO1VmfcwW3X22WfQtlEDGSm4aRQTeMXViDvUwpdIjxHMTw6UE83RVTTwcugAI5aXUIIRdz1m-BwxWW0gsyzVNCUjj8tXA9Fdq9CMYg6TNugPV66QKg7GlDJ6lzqL8QnNIkR9HqdgNSL-2DjxPdpEclLGqnDhR9rDxsEqSfZ3i233B8Oexp8ieFi7NaXssdt3drOnhr6dvRxV6dj7zUOTdzwCjJnY93YNR9ne3Kq0QDAE-wONSe9GIkNT2UlPK9vPhVwsFlF63WNTMQSYbSaghM1o_BGVL84NeksM8EIXRWrilfPKJcUx5YAYlzzy1ZxjBrsEkF81G45sIOWBFE7Psq3-YfuKHGKCrJZMbkOIAFBLEbdIRwXrOObIwJzXs6DTbljemz2k9fnYupCrVmX5P_66jumgHE9YoRSxBGXg9-gIB8PWXhfwbVI6ml12bQjtmKEP--ZYVN70N3JEwunOLxk1Bvu_Z0QBS3gtL3iQWnks6OMrf67FDRT9CYzOL85XCV7uzMB_8lbg6xButiWIwdzACY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64de53cead.mp4?token=XorxQojwNt70YN8BFiAWcEBDCS_Fwuut5kNnYC60W9EQRwhqgx14qev8IbQrWLOW08Hxd-WHrspE8s4ZIyHvZ77GMjWKX6bp0kQkZojIkDFNk7SpZh7b3DF717M1ta-qjDueFyNkb8JJhug5ocO1VmfcwW3X22WfQtlEDGSm4aRQTeMXViDvUwpdIjxHMTw6UE83RVTTwcugAI5aXUIIRdz1m-BwxWW0gsyzVNCUjj8tXA9Fdq9CMYg6TNugPV66QKg7GlDJ6lzqL8QnNIkR9HqdgNSL-2DjxPdpEclLGqnDhR9rDxsEqSfZ3i233B8Oexp8ieFi7NaXssdt3drOnhr6dvRxV6dj7zUOTdzwCjJnY93YNR9ne3Kq0QDAE-wONSe9GIkNT2UlPK9vPhVwsFlF63WNTMQSYbSaghM1o_BGVL84NeksM8EIXRWrilfPKJcUx5YAYlzzy1ZxjBrsEkF81G45sIOWBFE7Psq3-YfuKHGKCrJZMbkOIAFBLEbdIRwXrOObIwJzXs6DTbljemz2k9fnYupCrVmX5P_66jumgHE9YoRSxBGXg9-gIB8PWXhfwbVI6ml12bQjtmKEP--ZYVN70N3JEwunOLxk1Bvu_Z0QBS3gtL3iQWnks6OMrf67FDRT9CYzOL85XCV7uzMB_8lbg6xButiWIwdzACY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن مهرگان در غار باستانی کرفتوی کردستان برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/467681" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89fdfa620c.mp4?token=jQI3n6bojfp-VaRKXoerKoZWMIupSyShEbX6ICggE-NoJodupL1hJuIUnYqNIGBJGOLhuFi3ccFU99SYp7wGHjfo0JmrWQEyadK6G22v7-hIBq8lTjz3pgnzVe5d1TA_NRY5ly9BZQNfadH7v7wI9OrVDFPKbnRzHbP0B8jCwQ8-GV4LBceqaeDpOzaeZjhgFIp4l-e7oUlSVzCrATyY0lD2vpH9j8Zw8lYRlIxs5aVTM7QzN7xOF3EuAXriLvwz1g5MS7XOHDiSZAC8Cchh-ElubNH2klUBj8KrDEgBGJgmhowSqM0x43eyO6WIKMIc2qUWutcke6DIUTG_BBffVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89fdfa620c.mp4?token=jQI3n6bojfp-VaRKXoerKoZWMIupSyShEbX6ICggE-NoJodupL1hJuIUnYqNIGBJGOLhuFi3ccFU99SYp7wGHjfo0JmrWQEyadK6G22v7-hIBq8lTjz3pgnzVe5d1TA_NRY5ly9BZQNfadH7v7wI9OrVDFPKbnRzHbP0B8jCwQ8-GV4LBceqaeDpOzaeZjhgFIp4l-e7oUlSVzCrATyY0lD2vpH9j8Zw8lYRlIxs5aVTM7QzN7xOF3EuAXriLvwz1g5MS7XOHDiSZAC8Cchh-ElubNH2klUBj8KrDEgBGJgmhowSqM0x43eyO6WIKMIc2qUWutcke6DIUTG_BBffVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت مامور فراجا در حملۀ تروریستی در فاریاب کرمان
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/467680" target="_blank">📅 13:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b5d82a2f.mp4?token=SCkhA1p_S0QjmJne_fLlixcgOFLwn4BVANNPXO5fuM-K1RTVbz4YgylypEh_e9tfqrrLnQh5t9ZfQvSMtcCoS60wL3ilTeOiVuBguqGJVui7I6fnxzFKjpJB0or47ds9zgEkc99WarFmZTjrmQlJgpLTHjotoJIuCmaFXMw_ALQl7h2PzE1N-FTnfyVCF536y0cYiQQJ5A8jE1J6LgYgk2eUUaREpBG2RziH-UM7iVZvRva55eGmiGx2LJHI44rdVcdCsbK6RVHD1EN1dVykjXaJu_cCj5Hpgt-9LS5VFoDflMzgOj4E2B_3kheA1HmubsFzYBdwvHseZyfSrXPonw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b5d82a2f.mp4?token=SCkhA1p_S0QjmJne_fLlixcgOFLwn4BVANNPXO5fuM-K1RTVbz4YgylypEh_e9tfqrrLnQh5t9ZfQvSMtcCoS60wL3ilTeOiVuBguqGJVui7I6fnxzFKjpJB0or47ds9zgEkc99WarFmZTjrmQlJgpLTHjotoJIuCmaFXMw_ALQl7h2PzE1N-FTnfyVCF536y0cYiQQJ5A8jE1J6LgYgk2eUUaREpBG2RziH-UM7iVZvRva55eGmiGx2LJHI44rdVcdCsbK6RVHD1EN1dVykjXaJu_cCj5Hpgt-9LS5VFoDflMzgOj4E2B_3kheA1HmubsFzYBdwvHseZyfSrXPonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر میراث فرهنگی: عمر درختان سعدآباد بیش‌از آمریکاست
🔹
اگر قرار باشد در دنیای امروز از درخشش تمدنی سخن بگوییم، تمدن ایران به‌مثابه خورشیدی در تراز اول جهان می‌درخشد.
🔹
درختان چنار باغ‌موزه سعدآباد بیش‌از ۳۰۰ سال قدمت دارند و عمر آن‌ها از عمر حاکمیت آمریکا بیشتر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/467679" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گفت‌وگوی تلفنی پزشکیان با سلطان عمان
🔹
رئیس‌جمهور با قدردانی از تلاش‌های سلطان عمان و دولت این کشور در راستای تقویت صلح و ثبات منطقه‌ای، بر اهمیت تداوم رایزنی‌های دیپلماتیک، گسترش تعاملات سازنده و بهره‌گیری از ظرفیت‌های مشترک کشورهای منطقه برای تقویت تفاهم و همکاری تأکید کرد.
🔹
هیثم بن‌طارق بر رویکرد مستمر سلطنت عمان در حمایت از صلح، آرامش و ثبات در منطقه تأکید کرد و استمرار ارتباطات و رایزنی‌های نزدیک با جمهوری اسلامی ایران را از اولویت‌های این کشور برشمرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/467678" target="_blank">📅 13:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cts-9WKMCnTD3ps2ktAYlWBK6MgGE4ce_eL15mnb3Galo_ooPCVtq0ewvOfR7WQYZXYwihFokV3Q5bmvmZIsKdLWOnkC6PrnDctev-Wxgv_F3xNGtCs3-Gsl89kbfTYGSIbYVYkXMAsA2XceWDhJmb_ygOYAfzSEPAIxhxGtTSnV9CleCei9CKSwxaSDheplV0cnoPrI4Fwcq4e29KFG7_k-j6GD1Han7DExhwsltKt2CWHiHnBsgfmvTcdQaQaKKtINDWgHoX0dKKC5xPnXRSCU1UWWUE3uKiBPEuUm1sqJWSVnLucnZt9rblWv576UtNwSy9RrPr4eG79bU3wV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mabui5XJS9jRSfdyTLkAqIJVPvF5Kgep9hMQZhF63m0a8wH3AxD5oqr92PREfTwYRH7e56riDHMEtq-Uma38VbWr9-iwtSAZpadanu86q5OndImk2pMVDA4ke4v4F4gAUnKyC197w--4BvTvSYCurZ7O5ZRgGPFkg0QHKqS0vRT8C-fVeBfFmlZ8wwSLlnDtTn7ITnxZfRi5IfQAc_ohvD84ROBTPRKrw53Sh99X-70wH_0g7davhxknjdCP8QzTwwCfl70Q3BkL1apQ9J0hYcM6xp9f9JJRsCg6KpxkJn9snxDgw8Gabe3bV6Xau5yeTiKHsjMTMbOByyDsBj0p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckbFTlA9ywOnE3FFpB_30HKrr8-kVOqrCQgGL-qZ8GAE2XRya_5VENmQ8so7erlN2jYgzn21u1x6EOo6iSvhpf284ZYydWo3y2Rqx4lCNF6NVl3Itm-FR1ElEKTV9UDFcKn2ZFXrgTtPQ0PtCejlveBRGQQdP-yvMBrReaEbgRHxjhxX6lDHaCMwyifTaND4_Z22ye1peFP25GYpDABKrEv5ddoVE0pr1Pi4KgzL8YwGL6KO3aY6Xe2FEggq61UoMrIKBSTSkQ3mn_H35vTNNIvnvxDNUXbDvNeLe6PN76SZ8ay9rmguYIJQOnjvi09ANOwyu_Dl14YJj3NK2j45ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhVfa3mUPJTuJGjJR3VmEoTW_UceagUqDrySZYD6MyveTtVpEMwbfcZxtUVPRAu2t-7pp92k0ukmDzcL0h_YJEcUE0uIkSG9s2a-En77pvUCg9yvPHgnTcTSotl6KF3d-Tw89c0_S5k1clogP5i9zoJukn9lBUlSCiZI7RFWDsVmksJl_AywewmF7qJwOpan_EpW-ofJhlWAfb0Wlrf9WueoC6mnJv2M_TuD1WdtU_xuHz7nTaSp51kQt2GWidXSo0_k9bBSwSUzlCdsOxmYHFx1swNR1U2wGUVaQSZV5N1eAe2LsYLYOO8OqcmUdxVVz4c-66nrvyLq2vFyJfkowg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9TQhv31L0HOvBnzCAwipKPVDo1ZnPxDfIr-6aKTyBy9Y8QvzNGu1bTtDxAkygeYbTNxonCuoh7RVoPPBcBwFsSEOU6GWWx1kcVdF_HdLKV2q5LkA1HDt4YkXpDo01dMsIL9ZI29GTkd_8ZNq51AO-QpqE6yX0FrKedCtXrAUw0C1KI8kk-0nNr-nDjNdh7MvFpBLiMaiT4wNnsogZyOLXUJ61HkPRokJEZEdR5AITcZau1YjH0ACdjXE-QksJmc1nCuizUix6bKg4XqRPE9HUfgZNcwAH7-61PKGJcWj-IIWifEh_0Z5pRTTPn9H3-7jGP6KbVyAM8uNVceUK18NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jj8TR8Vt0Qo12traVw3obRu0w5_jjmb9wpec_CLAklWo7CqDiy4rZ8oXZEu7Gki1gWesn4gGRVwRA2mmNYDTeuomm3nWX-g5m5LXY2cQ1izO9uhGELMQ74G5LChBkIHWppkhOb0p-M1pnaiyFETTrRZjS1fhdzWv0R277LwBBXfxHj68JRVXZRWlS6KPT9gcc7nNZR1XBB6EyquqXWVGKaJlTW-9DZ3MdTFC9yXLuhSPTpNG98QmTzyzK9gPfFhFmBS9ft-KauY2f5fSL1-ufZdaVT-KpGtlYFbdFgDi_t6RUb-M4eGS2JIJJ6ALm1yQRNHidyJXinYtFnnMGKyQXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست سران قوا به‌میزبانی رئیس‌جمهور برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/467672" target="_blank">📅 13:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8976dbb0d7.mp4?token=fFM3CkHLifhfAlXfudQMSMaMDZwPTxSjq1CcbfBn9Ro0G8psW7fcvLIU9vaXvrAhfFkPF1_40j8WXTV2mZ3QJ1knxh0Bu-4arKY5xQPAGmeVr7E8kn4mCsrI7qECmBQT3876emu7WtK-PgqvGJnOrUmbv2L0t8QAmWIiBuutQjffO4bovrvEhOcmjlbHtQQ_MCfbGhPzrMhiiAh8AsrqwK6rW4r_BehIGazTfp89yE2zY4m7glHLGhV0R9TCOYNEEeNx8XPGCiY8TR3u4WzsE4OGTHtwn4RLp9Tomqv6GYPotkEj7ffn7Bi9unRZFd_zUwnlTiZhuOX_ozbe3UiAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8976dbb0d7.mp4?token=fFM3CkHLifhfAlXfudQMSMaMDZwPTxSjq1CcbfBn9Ro0G8psW7fcvLIU9vaXvrAhfFkPF1_40j8WXTV2mZ3QJ1knxh0Bu-4arKY5xQPAGmeVr7E8kn4mCsrI7qECmBQT3876emu7WtK-PgqvGJnOrUmbv2L0t8QAmWIiBuutQjffO4bovrvEhOcmjlbHtQQ_MCfbGhPzrMhiiAh8AsrqwK6rW4r_BehIGazTfp89yE2zY4m7glHLGhV0R9TCOYNEEeNx8XPGCiY8TR3u4WzsE4OGTHtwn4RLp9Tomqv6GYPotkEj7ffn7Bi9unRZFd_zUwnlTiZhuOX_ozbe3UiAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار سیاری: لازم باشد بازهم به شناورهای دشمن ضربه می‌زنیم
🔹
معاون هماهنگ‌کنندۀ ارتش: امکانات و توانمندی‌هایی داریم که در دنیا زبان‌زد خاص و عام است.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/467671" target="_blank">📅 12:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkHvXjGcjq-yAxU9kDz1NRt11fVwlsJHTVPp5fYRokaQ8-UORAlMVIcSWixNAVTeKXDzEAR2QKO-M4pg5_vhM3qRvIB4JsV-at70hqCEmdQiChR35sU3wb90cu6ZGEr-nZddmRELAr2AP5g8fAWjQs-XKoZqB5_ylOzMvT5SnJf__PeOjAkiaEg9ay5q98RyOeRS1hS8jhyjcLXaIt2WTD3LRCYKeOyldW9Py9wp-fVSsIyUPpTAE0WVQdbZ_i2K11sh95zOfxW8Q4kVTa0Jlby2plcyKOGyMw_T3Xrdp3vJUn1ybm35KF3n-MbQwYJYYZ0OHIrQh4OHSmSZWrn3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۳ هزار واحدی به ۸ میلیون و ۲۴۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/467670" target="_blank">📅 12:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467669">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYGd3I07hdsu6pbdTpEb6U8eEBVWStkZ1B4gMbCZmUasC96AG-mbT36c4bcTzl8VGmKnO-DC_XRt-Q4n_wf_ncPHsOxJqzptuWyiWnSwm6z6m9N5LQ6hCv3Mk68v00m4azGQOz-kBgUNzspL68rgmm8nlxUdkAKNK8Zvh1TSAn_GVi72LDJDdW91es6Jdkk4bRfwZ3UpBJ8eIs8208ZBOxyrTSTSVdOVpRKplt1SMqIE04in8nv_TvULW7roE8TypTP7a0J_z9ogAb_Naq13_SXxmYRV5zrjMB68Y4j0CPcTC-JAPAXbm35P6hbta4OUiiwreCxI_7hCQ-L6bNcAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ اعزام هیئت ویژه برای بررسی حادثۀ تروریستی زاهدان
🔹
وزیر کشور، درپی شهادت نصرت افتخاری، معاون فرهنگی و اجتماعی پلیس سیستان‌وبلوچستان، دستور اعزام هیئتی برای بررسی ابعاد حادثۀ تروریستی محور چشمه‌زیارت زاهدان را صادر کرد.
🔹
این هیئت مأمور شده است با هماهنگی…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/467669" target="_blank">📅 12:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4ce60454f.mp4?token=lWoPDukHIapvGB6ZZoH0a4BwtXP8EyaPlSGJ2SHIOcJCdDjsJKVlf5cgODV9qVBBFgx2RdW8NYOUfTRbBfK9swL_t4_QM3j8e-MgDoL28myBydI4cb-IEnC8aqK3lMdl2RExpXQfRooL-poK2xSxqHiPGeVYz0LOZtRXiFGIvzfg9kipqZlZov3VIdVnwprS93vRECNq_OctA2GiGoNO_F4QQyQgT6OgIU1WyAnaWJS28nu5LFR-TV6fxM5cHIrwrZExjl1pmXrFbt6Y5kaBOrj0UKMRVq44TdKPlbBROmqMk3CCh7sSHSKJgOl1rFsZf_4TlkWyNL5HindAyAK9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4ce60454f.mp4?token=lWoPDukHIapvGB6ZZoH0a4BwtXP8EyaPlSGJ2SHIOcJCdDjsJKVlf5cgODV9qVBBFgx2RdW8NYOUfTRbBfK9swL_t4_QM3j8e-MgDoL28myBydI4cb-IEnC8aqK3lMdl2RExpXQfRooL-poK2xSxqHiPGeVYz0LOZtRXiFGIvzfg9kipqZlZov3VIdVnwprS93vRECNq_OctA2GiGoNO_F4QQyQgT6OgIU1WyAnaWJS28nu5LFR-TV6fxM5cHIrwrZExjl1pmXrFbt6Y5kaBOrj0UKMRVq44TdKPlbBROmqMk3CCh7sSHSKJgOl1rFsZf_4TlkWyNL5HindAyAK9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تسلیم دسته‌جمعی مزدوران سعودی در یمن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/467668" target="_blank">📅 12:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f4d2d096.mp4?token=e20xGHQxi_gUXKWACVvBHuy9Mn8Vb2_g5jtSDvjASU7MQUd0xmQl1_Onk6PRKgMM9HGTwMmH87uxcaSZSZ8nUoZePfPf5waAjbtyAswvxKOEjc_1IXlsIAq6TUESy3QQqVDRc3001yNMhXm6nacrLMN33yaICJYwtEu2nfZh1wuxxsZITIPFABefecEVCG7S7l79b60yMkNfqINo7gviTlRoe-wY_pB03BoJKIEAFsoEHtxVRZyClPykc1g5aW9xCYAEuPjlP6cgmmCnxRX2874uJbPXFjqGgwl6WSUyxWa8N9p1LQJTGV0Hp7vBThByQ0NF0zECkPqaT5BKB_0hfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f4d2d096.mp4?token=e20xGHQxi_gUXKWACVvBHuy9Mn8Vb2_g5jtSDvjASU7MQUd0xmQl1_Onk6PRKgMM9HGTwMmH87uxcaSZSZ8nUoZePfPf5waAjbtyAswvxKOEjc_1IXlsIAq6TUESy3QQqVDRc3001yNMhXm6nacrLMN33yaICJYwtEu2nfZh1wuxxsZITIPFABefecEVCG7S7l79b60yMkNfqINo7gviTlRoe-wY_pB03BoJKIEAFsoEHtxVRZyClPykc1g5aW9xCYAEuPjlP6cgmmCnxRX2874uJbPXFjqGgwl6WSUyxWa8N9p1LQJTGV0Hp7vBThByQ0NF0zECkPqaT5BKB_0hfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استانداری گلستان: براثر سیل در مینودشت، مسیر ۱۴ روستا همچنان مسدود و برق ۱۹ روستا قطع است
🔹
مسیر گنبدکاووس به کلاله همچنان مسدود است. یک نفر فوت کرده و ۲ نفر مفقود شدند. @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/467667" target="_blank">📅 12:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌ اعتبار کالابرگ ۱۸ میلیون خانوار افزایش پیدا می‌کند
🔹
سازمان برنامه‌و‌بودجه: افزایش اعتبار کالابرگ برای حدود ۱۸ میلیون و ۳۰۰ هزار خانوار در دستورکار دولت قرار گرفته و متقاضیان واجد شرایط تا ساعت ۲۴ سه‌شنبه برای ثبت درخواست در پنجرهٔ خدمات دولت فرصت دارند.…</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/467666" target="_blank">📅 12:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bc3bacae2.mp4?token=ossFhPU8qAcfYXuxggnIaFZBidwCCthPr7FxsMBbFZEhU1Xl6EnT6WuhLNx_CQ3K_CZLd2pxbLvfIwK1YNk4DnF9jMm9tOsENR_Xu1NBSNGu67WUDRwocb2IKgZ2Dp3r1B7tt5C1q7hFqg5ckOAEHwlX2Qhj44FlR4VEbPsFKkeEfQ4W5v7EgjZWMMP6qAyt_BiQeYOTEyFtj1BiePIapfkcayMX2C_3G71QZ-SZ2Z9zIvGuE1elheU7Xula-URpuakkoSYRnblKsXOjXeGvga_-CEFQLodWoDcrZl7efJencqadNHNplXkjQ5m-xUudsPcnY8lq3flkPZSEY7BpcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bc3bacae2.mp4?token=ossFhPU8qAcfYXuxggnIaFZBidwCCthPr7FxsMBbFZEhU1Xl6EnT6WuhLNx_CQ3K_CZLd2pxbLvfIwK1YNk4DnF9jMm9tOsENR_Xu1NBSNGu67WUDRwocb2IKgZ2Dp3r1B7tt5C1q7hFqg5ckOAEHwlX2Qhj44FlR4VEbPsFKkeEfQ4W5v7EgjZWMMP6qAyt_BiQeYOTEyFtj1BiePIapfkcayMX2C_3G71QZ-SZ2Z9zIvGuE1elheU7Xula-URpuakkoSYRnblKsXOjXeGvga_-CEFQLodWoDcrZl7efJencqadNHNplXkjQ5m-xUudsPcnY8lq3flkPZSEY7BpcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوپرنفتکش متخلف در تنگۀ هرمز درحال سوختن است  @Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/467665" target="_blank">📅 11:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3e8aea3c.mp4?token=W-OlrlQpw_Dm0fKhLlQdNjokFp4irrk2yZKglUQACE83YrNdOv1lJ6EqYn22J4f2qljkABFILoKJg39kQC-3R79RfLqiRDEZlrhmR8uKMslCtXSZHKDFlS5ETTOFMUZPcQf8u_1SJi1HSGWZLpuq6zve_IDKytyWtNCXCuA4cI2bkdbxHxJ75sI-n6jjyb4yu7RqIgpjtXcI4WODpGPcLI1FcAtfgoSZeJ0e8SPfzCzkSUaLYqXomLUVWLv-lEArb1u_PoSWBqvGCCQWuiVP5Iw_HVWKMqcRhFUw4rC2fCNMP97O7cFFf1eV-iSFK40Lz8Iyi0Q0gziKJvbLv12URw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3e8aea3c.mp4?token=W-OlrlQpw_Dm0fKhLlQdNjokFp4irrk2yZKglUQACE83YrNdOv1lJ6EqYn22J4f2qljkABFILoKJg39kQC-3R79RfLqiRDEZlrhmR8uKMslCtXSZHKDFlS5ETTOFMUZPcQf8u_1SJi1HSGWZLpuq6zve_IDKytyWtNCXCuA4cI2bkdbxHxJ75sI-n6jjyb4yu7RqIgpjtXcI4WODpGPcLI1FcAtfgoSZeJ0e8SPfzCzkSUaLYqXomLUVWLv-lEArb1u_PoSWBqvGCCQWuiVP5Iw_HVWKMqcRhFUw4rC2fCNMP97O7cFFf1eV-iSFK40Lz8Iyi0Q0gziKJvbLv12URw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعداد کشته‌های سیل نپال به ۱۳۱۸ نفر رسید و جست‌وجو برای یافتن ۵۶۱۴ مفقود ادامه دارد.  @Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/467663" target="_blank">📅 11:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9tuuNZSufOancPM52G4emLeqOzoh5-dtKL1E2jaNGFDgAMm4v7UWFhPErrouCeIdDDBoryOGr2QXoYUHJRl9g-YaMBUo8hp86lpVFyh0AhnSj7NwZoMR6dNFh2pIN-l5K1yO5f_RvQhJyI3i4vu0hNKsu7WuBIZUK262bXu46fosSfvrKrDYo3DyZTpUiV-QIvRSoiRlJdW-uEuJ-pi17RJZ8x-C55kXIpSkP8SFE-R0sNftey_yDAM47SHWvlROr9vWIzt7v1YdX60OlsRONDx-jayQ3P1dyYRe1JTkSZy6HYwqotgCcSGDKG1sEeKAaXle4fKGQekFwr40RtAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلامی: چطور ممکن است وقتی خودمان فناوری هسته‌ای را به‌دست آورده‌ایم، آن را با فشار خارجی کنار بگذاریم
🔹
مقامات آمریکایی ایران را از تریبون سازمان ملل تهدید به حملهٔ هسته‌ای می‌کنند اما ملت ایران تسلیم نخواهد شد.
🔹
فناوری هسته‌ای، فناوری حیات‌بخش و نجات‌دهندهٔ جان انسان‌هاست؛ چه قانونی به کشورهای خارجی اجازه می‌دهد ما را از این فناوری محروم کنند؟!
🔹
طرح ۲۰ هزار مگاوات برق هسته‌ای را با قدرت ادامه می‌دهیم و ساخت‌وسازمان تعطیل نخواهد شد. نیروگاه اتمی بوشهر از لحاظ ایمنی و بهره‌وری جزو ۱۰ نیروگاه برتر دنیاست.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/467662" target="_blank">📅 11:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZbWesEjVz3V3O_USTKE36mC16K1xTU3ypgYX0O-mMvm0VUWi00Eq1sgpNEN2ALCyaAzl0_ojwPYiHCbHTcHgPHUJsG7iBejDCVGd4bcq52MNG0Y4fzJZut46n3pA5GQhGkz1pJ3dtuOHQMntI54utLkPRZuMX4dh6UlMGAEzk7U3lQNlJzP29H3owY_BPLA88j0sJFKzc-1D3E9GyM8eo0sycs7Ad4BizWGr8Q9MzRGWPOWD6hi5cxVSNdNX0DOhn9wiIQDoSVZ2oqqUPuuScq4QugNWz-TRvmIwcN7pcEiLe2WI_GrXFiqv-5xE90wfn_QONaK2HxemCl2y6uwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تعطیلی فرودگاه ریاض ۲۴ ساعت دیگر تمدید شد
🔹
وبگاه «فلایت رادار» اعلام کرد که تعطیلی فرودگاه بین‌المللی ملک خالد در ریاض برای ۲۴ ساعت دیگر تمدید شده و این فرودگاه تا ساعت ۰۰:۳۰ بامداد فردا به‌وقت تهران بسته خواهد ماند. @Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/467661" target="_blank">📅 11:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده دشمن در پاکدشت
🔹
سپاه استان تهران: تا ساعت ۱۴ امروز انهدام مهمات عمل‌نکرده دشمن آمریکایی-صهیونی در پاکدشت انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/467660" target="_blank">📅 11:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283eb4e2c8.mp4?token=pKMNvq24GIFTk-H6IWw95Q9gGn_aKXzC3WuPB4F2-jljWVVIaxz_cDLNJL5VRfmPsnpTRGV56iyiHkD1oW6PIr-DURb-2Yv8Hm98MhwRSNDV4UIIUJUUeLDAELcVKH4bSlHp-29iGFxP6oNth-0cF9_5HcSRNzVUjt_j0c-PYTgNhs5KF1nSVGNuG_ICjf_X7mEqH9EjcE2WgCYx-t_NyVq9Xzj3Iv7q0bKGOPCxC_y7ooFP6eBnyURwAQ1q3ZstRTjwAlHTXQw9hmUYMmo8o57ActT7-zXhzms0FnHWB7lBKfV4WxIZu7ZVrBNePWTLFwmonujr7FGEQoaslQXapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283eb4e2c8.mp4?token=pKMNvq24GIFTk-H6IWw95Q9gGn_aKXzC3WuPB4F2-jljWVVIaxz_cDLNJL5VRfmPsnpTRGV56iyiHkD1oW6PIr-DURb-2Yv8Hm98MhwRSNDV4UIIUJUUeLDAELcVKH4bSlHp-29iGFxP6oNth-0cF9_5HcSRNzVUjt_j0c-PYTgNhs5KF1nSVGNuG_ICjf_X7mEqH9EjcE2WgCYx-t_NyVq9Xzj3Iv7q0bKGOPCxC_y7ooFP6eBnyURwAQ1q3ZstRTjwAlHTXQw9hmUYMmo8o57ActT7-zXhzms0FnHWB7lBKfV4WxIZu7ZVrBNePWTLFwmonujr7FGEQoaslQXapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذوق‌زدگی و اشک یک کودک از دیدن رئیس‌جمهور در جشن لبخند وطن @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/467659" target="_blank">📅 11:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=LUE1RqJ2vf-RmFh_zPqTd8GJLcoxx6GcL5RdFMBHcNQ-TRHc2uGPNZ-r_6Yg0e2lojsHGhneaxj6nllENXuqUfLs-YeoyttyPbt4vRu645cx_AH7UfqzZ_BHKz8SM8ujCIMaRr_ypTdz9HQDOht87CoggcnVgFcRtWEcAuDwnnuAykkxeHGrIzINOLZtzmQKYdI7saCujSUqPDv0DDQVcsnUal3b6oTcq9UzTCEoLvmdZIX8wRC-vv2tNofVhH5-xnJgWv8QgI-vkNe2E6bHDfsp6A8BibUw0tLFjKfR3mVzjPDpCVo6MAeOkmJsjE1SndiD9QylK6hGHcCTCZdQBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=LUE1RqJ2vf-RmFh_zPqTd8GJLcoxx6GcL5RdFMBHcNQ-TRHc2uGPNZ-r_6Yg0e2lojsHGhneaxj6nllENXuqUfLs-YeoyttyPbt4vRu645cx_AH7UfqzZ_BHKz8SM8ujCIMaRr_ypTdz9HQDOht87CoggcnVgFcRtWEcAuDwnnuAykkxeHGrIzINOLZtzmQKYdI7saCujSUqPDv0DDQVcsnUal3b6oTcq9UzTCEoLvmdZIX8wRC-vv2tNofVhH5-xnJgWv8QgI-vkNe2E6bHDfsp6A8BibUw0tLFjKfR3mVzjPDpCVo6MAeOkmJsjE1SndiD9QylK6hGHcCTCZdQBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گپ‌و‌گفت صمیمی رئیس‌جمهور با دانش‌آموزان @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467658" target="_blank">📅 11:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de146792aa.mp4?token=p3lL_iSThgPqWy-nQkuYxT7quxV-Ey7s5Ib2DatCuRzTFfyYGfMhmWahcf3JyK0Eg5xB9cH29aa5K0TNtQo0epE3yZeK4dPfHAE3gPxXppqK8JFq_mCs70ZT-aN-nZ7HgidXAtoDFAq7QDTcVh97FUT5jR74PPioF7hI7Ux9qO6tIODAlVk0KkbCmPPlySAxjDTUNvkjO-j8V68KhUxxJOBU7w9GXK0zB8udzM3dwIq6HHISGpfQ1fV12KoZXknbi0svCzI0PfJZ_SC-B9WfhkrtdvuNSQ-K4pzvbUSbjBhw9tCGsiIvfw-i8hbc5k_2u5mK3VjU3vTJLSl7va7gvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de146792aa.mp4?token=p3lL_iSThgPqWy-nQkuYxT7quxV-Ey7s5Ib2DatCuRzTFfyYGfMhmWahcf3JyK0Eg5xB9cH29aa5K0TNtQo0epE3yZeK4dPfHAE3gPxXppqK8JFq_mCs70ZT-aN-nZ7HgidXAtoDFAq7QDTcVh97FUT5jR74PPioF7hI7Ux9qO6tIODAlVk0KkbCmPPlySAxjDTUNvkjO-j8V68KhUxxJOBU7w9GXK0zB8udzM3dwIq6HHISGpfQ1fV12KoZXknbi0svCzI0PfJZ_SC-B9WfhkrtdvuNSQ-K4pzvbUSbjBhw9tCGsiIvfw-i8hbc5k_2u5mK3VjU3vTJLSl7va7gvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گپ‌و‌گفت صمیمی رئیس‌جمهور با دانش‌آموزان
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/467657" target="_blank">📅 11:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwynAroNIdqywwDX1xLD3tZe7cveB2BQAVcTaljlwtjLHsOc4E64_6V2BlLGvNP0Cq04NRC-pcXdTxcoPGjOec9waSWvaIBal9ku6gvyUUn9t8LHmEV3Sx0q4i2_FJV4UGu-CDxLD0f0vf_M5PLHpPs2D902N1nHpr3IN62EmdUV-HCHUO7mQkidJj5GVYnwDNWu-3TuN5R257Ajr8NRFNFCJ8op9hcXZqFoeg-Mu8bsBqFkoMq5RpLFB_4Uhq7Z3jXXNGeMZf-uuEC5Tu_4MVZqI0PFy4qq5Q3TIJGcnCRCMKknKtIM8iRrc78_J4X9wYCpsM6QR-tLXciKsxIKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف محمولهٔ سلاح و مهمات از مسافر اتوبوس در اصفهان
🔹
فرمانده انتظامی بویین‌میاندشت: در بازرسی از یک اتوبوس، از یک مسافر ۴ کلت کمری، ۸ خشاب و حدود ۹۰ تیر جنگی کشف و متهم دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/467656" target="_blank">📅 10:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiQcp8HfvQl21YVcao9upZwKeLa1HVAWLNnMp0h207ANHH_I7gEHS31TNh7fjildj6PD_T1K8_HyPC78-0rt_BYFM9gZIvLYk5ILuL6jg8ji-erBzOOIfwZzVFG4gJ81YGCmy1JhTxC9h63b0TlyXzk-WSMfyiA-kJ2slMjWSUZKJ2l_Vh2GShkAL9keLX6UpGbYuAyRGvJXijO2nTeHLfOyy1_c2-u5fLlDsu5VmCgTkJGPdqiz2DFWquGfxCfgzdY0uhnVL0n5IMstK1w22hWBqHPgCHoOiglzeJH7e_RyEPEoPn_SdU7j1JpO5FQw3YkWsLbo92NCKaYSXDrtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرسپولیس با شکست صنعت‌نفت به ردۀ دوم جدول رفت  عکس: صادق نیک‌گستر @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/467655" target="_blank">📅 10:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دستگیری ۳ تروریست جیش‌الظلم در چابهار
🔹
طی اقدام مشترک اداره اطلاعات شهرستان چابهار، رزمندگان قرارگاه شهید فولادی و سپاه شهرستان چابهار، ۳ نفر از اعضا و مرتبطین گروهک تروریستی جیش‌الظلم در شهرستان چابهار و روستای درگس شهرستان دشتیاری دستگیر شدند.
🔹
خانۀ امن این گروهک تروریستی تجزیه‌طلب در منطقه عثمان‌آباد چابهار به‌همراه محموله سلاح و مهمات شامل یک قبضه سلاح m4، دو قبضه سلاح کلاشینکف به‌همراه مقادیری مهمات سلاح‌ m16 کشف گردید.
🔹
اقدام علیه پاسگاه‌های منطقه مانند باهوکلات و شیرگواز در دستور این تیم تروریستی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/467654" target="_blank">📅 10:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwSvSZm1vcCSjTuOvUST4lJjVpz_S90B6sWesURps6NZ38mtLVrP18VLwUKrQ39ARsiTzz3GRUuOA371wTOSRDLEfsRYhZ2dUsLp5MBIsmWsZi7bZwExK3fzyIgN3N5zWCfsc06vn7G555Xw9PtKE-7O29V42fle-sTfAKVGceRIsrqZ22SuYcSmQd2U8gpCb7mgEaUY1f6T1W_BcBwGLaFVzRznUM29uTRcJe9uj8z7qX0MW2aafCWCI4pb4sR1rHQGfLO14Ia8ITVTofwHskLBGsYyDkG-BTVY_QtrAdLLrEJ7dSdta6DTuuja5vRx2htsM3ufovKuamWLe6k1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبض آب ۳۰ میلیاردی برای یک مجتمع مسکونی در تهران
🔹
مدیرعامل آبفای تهران: گران‌ترین قبض صادرشده در سالیان اخیر، مبلغی نزدیک به ۳۰ میلیارد تومان برای یک مجتمع ۴۰ واحدی در شمال شهر تهران در یک دورهٔ تقریباً ۶ ماهه بوده است.
🔹
عمدهٔ مصرف نجومی این مجتمع به‌دلیل استفاده از چیلر جذبی بوده که طبق مقررات ملی ساختمان، استفاده از آن برای این نوع مصارف ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/467653" target="_blank">📅 10:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🎥
آغاز افزایش اعتبار کالابرگ از امروز
🔹
معاون وزارت رفاه: در مرحلهٔ اول، امروز حساب کالابرگ افراد تحت‌پوشش کمیته امداد و سازمان بهزیستی ۵۰۰ هزار تومان شارژ شد.
🔹
دولت برای افزایش رقم کالابرگ سایر اقشار آسیب‌پذیر غیر از کمیتهٔ امداد و بهزیستی با تأمین و تخصیص…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/467652" target="_blank">📅 10:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🖼
روبیو: یک آمریکایی در حملهٔ یمن به فرودگاه ریاض کشته شد
🔹
وزیر خارجهٔ آمریکا اعلام کرد که در حملهٔ دیروز یمن به فرودگاه بین‌المللی ملک خالد در ریاض، یک آمریکایی کشته شده است.
🔸
پیش‌تر سازمان هواپیمایی عربستان اعلام کرده بود که «در حمله به فرودگاه ملک خالد،…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/467651" target="_blank">📅 10:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467644">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-NR_9WhrCjzejPqYegPErL1X8LNwO5VkCTTPB_Mz4mlOoxWps95lL4znm-F689oSHsaaDPeUzCQo-vnruQdLgCsZ0WV3pB6AxnA_L9tXc06c9o4vDyrGf2pw_otrpibE4b5RRLmX6QwRL7GNGXOMnVNK-_V9HCm1qVDe6bsciblS81qSFgSlF2cO2GD-Jji9DFUzHXh2OdHVAju2N3L5n63cukjvH1P5aXBKVjNKT9BdBSZIfxvFV01B1643Ez1MAu90-_e3ssNcw8YUVAdM-bh2PGPoAUMu6JpotnXvw79Zz5olXQXc2tDsY2BYKHt6ISQBJcc4jh8XEYuWsvkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1EdU3bUl6KO9lC0J94POPdFRS1FxU1CGOcBdbr9ecv4g_cjNyyRf51gVLZ_Q8HDLqg7QmgqO6SiIZgLSjrhorwGmlKO2DaZBbp712ah8492eZLhnwJazm_vpVjlDMsvfDF9li5UzHAOWThhBUG3y6WUleGMexczbME7l5uCTNfBaGT_d_vRU7yaIjzAMpqhHXpjoDzoP9l2R7EoXq9pkY88GgUl5VgkN83YSwGZTJMHgJInFJsQm8YveGBTNqnSg7xRMmGLi-vASA5_Mnj0naKwQ941WXThyypu2EgxibIDfrZlnZD-G0Sqm9I8KurcJkT4SWGP87HjQRhhL9Iqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juHviaGYKcT0TSB98VEbfFP1VGRV-kXO5wHWrjk5nleU7dIencrq2xxP_4IA3RbbsD9QMHQIfyZ_d5qHunXffwhWj4EATZVEPWo6lHq2pAMyvH4aZFNmmHLQ-nEY5ssA7XRB2TdglRCcs1TaFKSs45w6Wo_UZHpHZPjyhTp7dCKsYJH9LtD8tlx4eqfHTqr8CPIgr_9A5tgu3Yy5ZHyb0_eW8ExwNM0xSeyTac-NA3KK0LPXfNAy1uSl0luih3jFgmzfCcM0l5_3s49kPR8tBKE1wYBuNakOLqxMw1Nn5waFACfeRiHGzgOAd6H34z33yHqCs6YA3xaN-_gUv1LlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hA1UKkvyqs49KNXga1GLEeCkihehrg9AclVO4TDiGuFNKG8i6gdrNIa-N9FtDX6wSMLhvUzU2cd22uhGWkyTds5Z6okLvvsIYWVy1F4GW53Mr3i3GIxnV0bxI2saW6ySDyII-Na1lrxqhSJC9tlY9P2XVRpHzDWH-HuZ9QeEgYsG9VCdxv5mumxWn0QujiIXR3gobuVo-Plhez9WByyf2EYb7JPQwQ2ynBiDnyaAds6AKHDTVvuXFBxB2-2bQjSzbNJfashB2CBgtviaLplzJAVpqWB4p-tXAxrVPf1XB_gNOUee3NO1nTJkyHOVT8a31n7YJdYKokn29P4KtDCm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnqaSD75ewqO4LRKluAemovFB1J1wLu2xXEn0V7shACyKd3nxIPOWo1hGLi4iWCsPKjKwTjdZDx8bwPFsllf7LtqdV3FXaIzzISzG1PsRTuFG7DPp0CZqRUH8ykSGq317TbiecWVIhKQFvZhkN1QJMURnKN39gNRZsJU81GeEBrhNeaYaTEJl48gtZt2toa3xFPey-ufrCNS1D4n5WrOCcaGBVEWbRp9ccQ-_bX-9RgIjhYaom_LAXnilzUgY8d3nieBru7byjirmv46WMTpAaXM7GWUAHdBReCkTwJULcLWTo3nKntiorMgzd_-NTMDBx-hbIkKaLYHOAMMn7ENwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q2bU85OkQxyIiDwuPZ_YUWToaixi4Rki3GNYabeNIDPkkabrX3zCtn6-tS0gSeTF_vj8lWk-sgicQT4mZb4E92Leh5lBimyevB9t-x6Teu5NWo1IfqkSqKsjBy84r_kdgwnpPHwQM7aUT_vAseWJsajQTt8IAdwFfq59vpiyzZ144iRWA2Z22fgVMED1RG_R6NNnzRw2-l3HM4rHIxh6Pmghp7n5vCu9i3N_1FtsXjGqa4IMcv46u_gP3kCxNXaikt6E0aXO2wVfnya-PCETsMubFkhfu6O5-1vNBQlUgbP9vloKR7goEQUoBQCpXpJBpA6e32H9M4ydZfUwqt6ATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ip3Wyp9WP5GzX6PdW7piy8rIFV9hSMUSK6_35acKNFNgdg8aMxDLnqaeLv74ScfZhhdK4W7dk_eahlZ3osCWR8JIM0IqO6Uu4LyQTle8U6a0MPZsUaDQgJzoMmf_XGgGXlmP5vNAr52jdu64Mk34Uk-NxU7WOIgSwsfpuNTYYlXcYHrRM1R4uXfYPy8SbambRMBjFwdTvZcM4RDm-XzZOKbMaO10CH1HmzSReAIo_MGjWQBi1Q6pI7nlRQJ9OunvHTjXWRW7UAZmA2j66DiPMg9AODUiFNPk3788cQ7Rr5Uflr5MwXsKSK8GuqBJ_5-YOHAVqYIPw8_wtvhQ14ZzMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: نخبه‌بودن کافی نیست
🔹
نخبه‌بودن کافی نیست؛ باید همت بلند داشته باشید و از سختی‌ها نهراسید، چراکه رسیدن به قله‌های موفقیت بدون تلاش و پشتکار ممکن نیست. امیدوار باشید، مصمم بمانید و بدانید که در این صورت به اهداف خود دست پیدا خواهید کرد.
🔹
اگر خودمان…</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/467644" target="_blank">📅 10:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467643">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL4TKg5lvD33u9R0iWHLgvplNYIpM-_u_vtI7P5iFYA8I80V2j-ZtJnjG1-g44oDhCfVnx_-dPU5Px__SURuDhPYZqU3HT9inojhS5FjQba80pZDKXo56bkJWx2OVoKHpK3OwNa6YO3ipIXzgpGiBGE3lfO0yMjzK8tK1CVnQMsHt7pw5VbHTm-K2rDGQn2zjipFDTMCrG8aqeJEI5quV0TYIL0VAr2X64lFWNzsFWv5SF9f-hFSXQC6nT7AeNnm-9clDY59IN6QpP7lqhjDNbMGFUKviPA-3GcBwVX60heIilCVb6l1SZvdP-9X9nchCTta2PHhGZyYVblr9gFB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تمامی موضوعات با نارضایتی روبه‌روست؛ ایران و اقتصاد در صدر
🔹
نتایج یک نظرسنجی جدید نشان می‌دهد که ترامپ در تمامی موضوعات مطرح شده در این نظرسنجی با نارضایتی رای‌دهندگان آمریکایی روبرو است و جنگ علیه ایران و مشکلات اقتصادی در صدر این نارضایتی‌ها قرار دارد.
🔹
بر اساس نظرسنجی فایننشال تایمز و شرکت پژوهشی فوکال‌دیتا، در حوزه تورم وضعیت برای ترامپ نامطلوب است و تنها حدود یک‌پنجم رأی‌دهندگان از عملکرد او رضایت دارند. افزایش هزینه‌های زندگی به یکی از نگرانی‌های اصلی رأی‌دهندگان تبدیل شده و جمهوری‌خواهان کنگره از رئیس‌جمهور خواسته‌اند اقدامات بیشتری برای پاسخ‌گویی به این نگرانی‌ها انجام دهد. در همین حال، حزب جمهوری‌خواه با افزایش تبلیغات انتخاباتی تلاش کرده است از نامزدهای خود در رقابت‌های نزدیک حمایت کند.
🔹
در موضوع ایران نیز میزان تأیید عملکرد ترامپ از ماه مه تاکنون بیش از هفت واحد درصد کاهش یافته و اکنون کمتر از یک‌چهارم رأی‌دهندگان از نحوه مدیریت این جنگ توسط رئیس‌جمهور حمایت می‌کنند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/467643" target="_blank">📅 10:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467642">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRZRX9MWzhVIYyiajveXn0JG0XxBde1C1jxyVb2wcYykY-9q7A4p7w5efOXolceJHdakdvypOMDuZKbn4sfAqD83JTyfCVt0wSeKwdIqoIFlsjhqUq3SBB9ZpYTSdVK6ZKOgps-rdsF5-AAEuYETV4QEDHmYQQqcLvmWR0WtWwMMY2qr6ooLjQerwlXInz8mUCSPb1mUKEK3I8yHc1DfMXxIAuOESO1TAzNaiWdKTEgLQXRLTZN2sYBLeBs_r6uuEpq1hZYIaKz-F_YAaqWuF10HQX3P18_immBgxcvJ4P4LEgbKWUotii0wBYEpaY1OiPyif43rhKp4PR9KdicCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: نخبه‌بودن کافی نیست
🔹
نخبه‌بودن کافی نیست؛ باید همت بلند داشته باشید و از سختی‌ها نهراسید، چراکه رسیدن به قله‌های موفقیت بدون تلاش و پشتکار ممکن نیست. امیدوار باشید، مصمم بمانید و بدانید که در این صورت به اهداف خود دست پیدا خواهید کرد.
🔹
اگر خودمان خود را تحریم نکنیم و اقدام به حذف گزینشی نکنیم، دشمن نمی‌تواند ما را حذف کند و یا به زانو درآورد. باید تلاش کنیم بستر مناسبی برای ظهور و بروز استعدادها و توانایی‌های همه جوانان مملکت فراهم کنیم.
🔹
نسبت به مردم و کشورم تعصب دارم و تا پای جان برای مردم کشورم ایستاده‌ام. نسبت به رشد و توسعه کشورم تعصب دارم و به‌هیچ‌وجه نمی‌توانم بپذیرم که کشورم از همسایگان و حتی سایر کشورهای جهان عقب‌تر باشد.
🔹
به‌دنبال این هستیم که از هوش مصنوعی برای آموزش دانش‌آموزان بهره بگیریم و کاری کنیم که معلم نقش یک «راهنما» را ایفا کند. در کنار آموزش علم، باید مهارت و باور خدمت به کشور و مردم را نیز در دانش‌آموزان پرورش دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/467642" target="_blank">📅 10:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467641">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a118ac3356.mp4?token=qr_kpzkh2PsWFvgrw10QQM_v_BZUstbhp9FNdJfG4-5xEOPJEQ4SCeCigPio9u-KyBV1XVKy53GjWzZlI6VaGFZbnokOg_hT4qTLCz6YaWpvqdJVT3Y6jL7m32A4T920xBY_EyiFM4sHRpLk4Zz4WpzRvA33IFH2xdZoYhKJpbGKRbaxaaMDG_gL79Ahw2_GRKWNaxW2iILqoaplvXjbU7lTuB8dP8W0EbS_1oZlfqEgKfE-lWhlTFv6RA2PT-1ZoSsdlZlX5kbzmxOy36USvlKM2PqL_X5vRivKhw5WtPKMFzw9BWrmWl8XiCMcZck8fT6JETCqqAf3y9zl2sVb5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a118ac3356.mp4?token=qr_kpzkh2PsWFvgrw10QQM_v_BZUstbhp9FNdJfG4-5xEOPJEQ4SCeCigPio9u-KyBV1XVKy53GjWzZlI6VaGFZbnokOg_hT4qTLCz6YaWpvqdJVT3Y6jL7m32A4T920xBY_EyiFM4sHRpLk4Zz4WpzRvA33IFH2xdZoYhKJpbGKRbaxaaMDG_gL79Ahw2_GRKWNaxW2iILqoaplvXjbU7lTuB8dP8W0EbS_1oZlfqEgKfE-lWhlTFv6RA2PT-1ZoSsdlZlX5kbzmxOy36USvlKM2PqL_X5vRivKhw5WtPKMFzw9BWrmWl8XiCMcZck8fT6JETCqqAf3y9zl2sVb5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب در شهرستان‌های گرمی و انگوت اردبیل
🔸
صبح امروز بارش شدید باران در شهرستان‌های گرمی و انگوت موجب جاری شدن سیلاب شد؛ آب‌گرفتگی منازل روستایی، تلف شدن احشام و آسیب به پل قدیمی زیوه از جمله خسارات وارده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/467641" target="_blank">📅 10:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467640">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHNOcZl1hhC6VJEV7_ZEpE4fdMXcNWeuCYrTLHON4T6I76KHuQZhAHdkIB3weqKhxlpS0YPaeMLJ9cjsZtBuXYxO2ekzaBVnIV0y8DuMWb20vS6iYSxsGG0KJ6Z_zD1-v_8U8hCxOrIbP6IWJHTyeb7Ao9saUU5GDEkOysz83MrmoNQOyFBr2ZjyE0ZJwwJJHtP-O6_ZS-IeW-IGLMhk1pXDsQ7s33zTdTV2FBuPFyW9U8ZrQJ0Y4IZXBjw6HRS63v3ys0rlKfx57yhcnKAgZrBX4uIF2hyiYOPsB8VSbRDfULaEMF8IJDrInU6ubMFQwFyyQBEIOW8QoOn0CJsF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای پیامک مالیاتی به مردم چه بود؟
🔹
سازمان امور مالیاتی: پیامک‌های جدید مالیاتی که برای برخی مؤدیان و شهروندان ارسال شده، با هدف بررسی اطلاعات معاملات ثبت‌شده به‌نام افراد صادر شده است.
🔹
اگر اطلاعات نمایش‌داده‌شده صحیح باشد، نیازی به اقدام دیگری نیست؛ اما افرادی که معامله یا اطلاعات درج‌شده را تأیید نمی‌کنند باید از همین بخش نسبت به رد اطلاعات اقدام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/467640" target="_blank">📅 09:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467639">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo4m76bdPVXq7ZC1xtkrQoZD3yS2KALgv4SKV-52Gtuc-GPmqgAPV1K65hj07u_4sHKvXsLHAtcyTwLxosXB09Jvo_HNn-artJcqnPI7XjNbmTQypXTnq_SSqFHP1PwmQ87NfwoM-nrgtGKqA81L-PMtPQDuGRDSwQULTqbrQctyfIRSOR90Drund7YKZnQg-8mZwFiLEWIaGqFERFZoPV-U665hzwkKo1gav1tI_7T3GPRKrTfzJdSjprTilnenxx7FaMDa26OmQsMq3gCYsCwnZ6_skv8QTUK_8253hoQTUFnfdT7Mq5KVKp_rVffS9s18v81o4CYFPFKCe7VlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمز نیمی از صادرات نفت کویت را بلعید
🔹
صادرات نفت خام کویت در شهریور ۱۴۰۵ با افت ۳۸ درصدی نسبت به مرداد به ۷۳۸ هزار بشکه در روز رسید؛ این رقم در مقایسه با شهریور سال گذشته ۴۷ درصد کاهش داشته است.
🔹
میانگین صادرات نفت کویت در ۹ ماه نخست سال ۲۰۲۶ نیز با افت ۴۶ درصدی به ۷۲۶ هزار بشکه در روز رسید؛ کاهشی که نشان‌دهندهٔ از دست رفتن نزدیک به نیمی از توان صادراتی این کشور است.
🔹
در این میان، صادرات به ویتنام ۶۸ درصد و به چین و کره جنوبی هرکدام ۶۴ درصد کاهش یافته؛ اما هند با رشد ۵۸ درصدی واردات، تنها مقصد بزرگ صادراتی کویت با افزایش خرید بوده است.
🔹
محدودیت‌های تنگهٔ هرمز، تنش‌های امنیتی و آسیب به زیرساخت‌های نفتی، چشم‌انداز صادرات کویت را با چالش جدی مواجه کرده و وابستگی این کشور به مسیر هرمز، آسیب‌پذیری اقتصاد آن را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/467639" target="_blank">📅 09:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467638">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sywr9UfA1Qp-1W9MilVJGzeLHvUK3fFCR_WLhqtz1nu98q-XqZxZXMQS5GlwWIozWR0bqJlnAr8xPO7BMVfGp-LjXp-TlJTXMUlN5d6gON1cVbXeYeeawSPwyIn1n2Y-IXajOI3flEMRPWiM6AG3Yi2Fy7L9GNXj9cG5DgfLzQo8wqp5lxyy4vnM1Igh4042UPduF1M-XsbVYd9r4vm3B5NkQlgFfJWoHFS3nqB0llFCsrFh9rzUkFB6w4C3zT-xcW1ZJOQk9y0Kr3NMD-CoBSvBeGFCyIM3GGXkzrtipurIW3fURKZvkkW3FdD5Vc0KBWnn_AriNYAH0C-ss-eimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌های جدید ارز در مرکز مبادله اعلام شد
🔹
دلار: ۱۷۸،۹۴۱ تومان
🔹
یورو: ۲۰۰،۴۴۲ تومان
🔹
درهم: ۴۸،۷۲۴ تومان
🔹
یوآن: ۲۶،۶۹۷ تومان
🔹
روبل: ۲،۱۰۷ تومان
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/467638" target="_blank">📅 09:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467637">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da0a6d2bd.mp4?token=OzHP2sNDtMDShys23sKRDPIP7idS3S-TFriXqCPUNhOvv5HSpwdtjSW-z_qXUCzcL9eQjy9-N8JVilsI8YUPh0rWPT3yi-3UjdtQYucIv3JsfftZ3cbs4ZFLuf0bDWTq0bnsowAk91o78y9G9Z2Qo9QyWNis6PnHZDsYcIht6zbcJcb9M7FfcW98hI9H5kld3_henhigF47CR39Byk0nIRl9P-JtRcDCOvKXQKZvEsuBNhUuGfmkh1jmflAIzPainGugBCqYwUOpkJ1mhqsomXFNB1CTD0IKy83ZVN6IZE6yoV5wfY6dfMcqtlnEnMKxbm2q7Uq6HakmrXIX1Y7dmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da0a6d2bd.mp4?token=OzHP2sNDtMDShys23sKRDPIP7idS3S-TFriXqCPUNhOvv5HSpwdtjSW-z_qXUCzcL9eQjy9-N8JVilsI8YUPh0rWPT3yi-3UjdtQYucIv3JsfftZ3cbs4ZFLuf0bDWTq0bnsowAk91o78y9G9Z2Qo9QyWNis6PnHZDsYcIht6zbcJcb9M7FfcW98hI9H5kld3_henhigF47CR39Byk0nIRl9P-JtRcDCOvKXQKZvEsuBNhUuGfmkh1jmflAIzPainGugBCqYwUOpkJ1mhqsomXFNB1CTD0IKy83ZVN6IZE6yoV5wfY6dfMcqtlnEnMKxbm2q7Uq6HakmrXIX1Y7dmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ فرماندار مینودشت: سیل، مسیرهای مواصلاتی ۳ روستای قلعه‌قافه، ساسنگ و چهل‌چای را به‌طور کامل مسدود کرد.
🔹
تمامی دستگاه‌های امدادی و خدمات‌رسان شهرستان در حالت آماده‌باش کامل قرار دارند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/467637" target="_blank">📅 09:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467636">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_X4TpxTxPXHfwxh-uelDbgjL-R5CZ_nKT1HvQ2x4wncKAuPd1geIiW3z8ivPcVycB3rdcEijXQe84ZqoAn38tZjcslsuiDIVfaxfaFKTEwaUOsl6emjfmLvQ-_oF3eacGA-RrDp5WFhsQEvHzYDIgVw5x5zK9T3rsVpGFTSNc0DfyiklvRrAOgJ4ZUSEBuTLkrHXdfS1hjWcyVXxCYbhhopZmuTUkfhG_suJAocZ0MkwkcyT40NA0wMY9YM0Qu2DuJxDGBimRelycSTtLHT3U4xrCbioAKAnowmt2CsyoY4qWpKejzG1FydGRYvnM4rdm4C1sDRsf90RZpiGWFoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/467636" target="_blank">📅 09:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467635">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZmPg0FAbzLt-lniKYWUpX4JQp-I6PdVwSNZnuU8KpptCf4DqbIoFFGJmpuZ3U5dM5gslY4nHDT3QAHOMd-_qAEOBWO9bS6sBfyJyEL5c1Gq3YaCxVFF5Fk2peNmNA0k970ekNS0FCRSA1BxHeWjDLqSQGpcrXs2NVGwn-BNOvTWdD25CA9v-qqMkS7NcNNHdrjB7cgQLxxfmYhr6TWj7_Ze_t0da4EXyMLD3jRJhRZfVyPXwiIXFq5MeczRQ9Jh1_o_BTkIEiWtUw1S1-wtHq4QQee-_1GSjAqAhOkWDCiU5l8_1KpEX-sJAjz2Em7rEPZtSBj7sqqR-FNRttTdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ۱۲ کشته و ۵۰ زخمی در حملهٔ موشکی یمن به فرودگاه ریاض
🔹
نیویورک تایمز به نقل از منابع آگاه اعلام کرد حملهٔ ارتش و انصارالله یمن به فرودگاه بین‌المللی پایتخت عربستان در روز شنبه، دست‌کم ۱۲ کشته و ۵۰ زخمی بر جای گذاشته است.
🔹
به گزارش نیویورک‌تایمز، این حمله…</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/467635" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467634">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در دزفول
🔹
فرمانداری دزفول خوزستان: از ساعت ۹ تا ۱۱ امروز، امحای مهمات عمل‌نکرده در برخی از نقاط شهرستان انجام خواهد شد؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/467634" target="_blank">📅 09:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467633">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7725050da.mp4?token=Bu4Mtxs9mUMqXS1Zxx4zldpYMHsFbj7jn31I_F1EypTYW0EtUMV_9giUBmmhdLYHorrOtWdFj25ywg0WzcdH9uvkm1MZDxkOd0Py07Q5tZLRqPbFI0hdkBTy1Fu4CohBmbLU_ZT02esGPcv6uJ7NgjkvuhyxsmOnWA5u8A6zjeH8PaiMaEXmy6PRoUjnxdIAN9lmejHIEzwFpAjhJcTQVFHEbAde7t_8kuklfs7S6Vht4b9yLHJ5jcMm_mI2cS0Icdu5m9cC1EPmcnrYCrkJdsFAiDh9hu7ZNBfZqV01AZBHRoTs3g3XQrCvAXuB8Bk6MlkUuuzMPeJQ4qI9C1MewQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7725050da.mp4?token=Bu4Mtxs9mUMqXS1Zxx4zldpYMHsFbj7jn31I_F1EypTYW0EtUMV_9giUBmmhdLYHorrOtWdFj25ywg0WzcdH9uvkm1MZDxkOd0Py07Q5tZLRqPbFI0hdkBTy1Fu4CohBmbLU_ZT02esGPcv6uJ7NgjkvuhyxsmOnWA5u8A6zjeH8PaiMaEXmy6PRoUjnxdIAN9lmejHIEzwFpAjhJcTQVFHEbAde7t_8kuklfs7S6Vht4b9yLHJ5jcMm_mI2cS0Icdu5m9cC1EPmcnrYCrkJdsFAiDh9hu7ZNBfZqV01AZBHRoTs3g3XQrCvAXuB8Bk6MlkUuuzMPeJQ4qI9C1MewQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۸ میلیون نفر در کشور هنوز ازدواج نکرده‌اند
🔹
مدیرکل دفتر برنامه‌ریزی وزارت ورزش و جوانان: حدود ۱۸ میلیون نفر از جمعیت کشور را دختران و پسرانی تشکیل می‌دهند که تاکنون ازدواج نکرده‌اند که از این تعداد، حدود ۱۰ میلیون نفر مرد و ۸ میلیون نفر زن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/467633" target="_blank">📅 09:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467632">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcs9VBxYLVMSlkiKhqJQlkmF_qJY4vxmjDEaZQ3AnC0D4f7C2Prf6k88OuENZ9fhsq0whkySgUmvhSiqMJanHcqyskCNuwSvEuYfYO4SdpBa1d73oFrlj42KCUXfB-_8XOrgyF-S8CKxaC-9Elr2v1qCGah9wm0QGY4rgfcAg17--xGz9G4Du2f276435FKqXt9wJbqHZRizjjT966IExx3ORCItSsmrpR1dT2u8ayWcK5Xm-9LrZabU-UisXtqQ9Wcp30Xn-rPPxmx6qmuMiitbuM6_RFNwnUDjM-9v8uGOVZPS1ZguyZNGL3_cSdVR4fPszxAOZ6ugYMfz_12azg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت نقدی هزینهٔ اسناد رسمی حذف شد
🔹
سخنگوی سازمان ثبت اسناد و املاک: هزینه‌های قانونی تنظیم سند رسمی باید صرفاً از طریق دستگاه کارت‌خوان مستقر در دفتر اسناد رسمی وصول شود و پرداخت این هزینه‌ها نیز باید با استفاده از کارت بانکی ذی‌نفع انجام گیرد.
🔹
پس‌از تأیید سند در سامانه، پیامکی حاوی جزئیات هزینه‌های پرداختی، شناسه و رمز تصدیق سند به شمارهٔ همراه ذی‌نفع ارسال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/467632" target="_blank">📅 09:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467624">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3fDeEnvv7BL-qEECLHUaLAEyqEjc_1Kyhw89FLozJtCxssCEtqpbSH3PPl6Sdj3XYb6gJJotMHa2So7AmRzubQAdBircYQCbWdVYR8PZTPO_LJGb7Xat2cQJ1ocduVTw6pCK1_77G-qHxVv71s9b1PetSDiKmGOLrvRpU17j8-4_UZuf67YiokY7noOCRqgNOLvrdLBNJLFm3DyafVemi-hZofQwKen9cz0p-6dkSq4KBOMBBVrOX8rjv9jbwQLZsPZbOcvObRUcJmiopFG2a0f4ResAeAs2Xk8JUkRw9P3-6lutoatkiVtFB-Ugn8lIiColV3I-hLnP8MuqlLoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم قصاص قاتل شهید احترامی اجرا شد
🔹
دادستان هرمزگان: پس از طی مراحل تحقیقات، دادرسی و صدور حکم و با انجام مرحله فرجام‌خواهی و تأیید حکم صادره در دیوان عالی کشور، حکم قصاص قاتل شهید رضا احترامی، مأمور یگان امداد فراجا اجرا شد.
🔹
اتهام وارده به محکوم علیه، مباشرت در قتل عمدی شهید رضا احترامی بوده است.
🔹
شهید ستوان سوم رضا احترامی، مأمور یگان امداد شهرستان بندرعباس در راستای مقابله بی‌امان با قاچاقچیان در درگیری با قاچاقچیان سوخت به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467624" target="_blank">📅 08:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467623">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19140f5c8f.mp4?token=hqlQEn_qTY4yX5W8aQHJFvu-4cqDL1gHBtv5H1tmHV8Ep7sDiFDmu0TpbN2yL0msdDyIfMEcfHs42FYof6Qg5t_LzDVeSqj9C6v1pQnRw_Li8qieL_0dwjhkJtNZ7V-HFNUv17v1iFzwuEO5nbXAlCDC69CcYLSnVIxUjM4rsHPyNA6ZJi8kU5bPj-3qXOsEe4fhbWAoAAAhG0WOO83rWGagtnttm1tvYL6dSl48WS6lVY02MnxGESB78vlbtRUNXMnFMjt9pec52ezg_hclwb5Qbkmvt__9PjCMDpid1XkRy-jCp4MEbE3th69Kpk1SQpWqMFAzhLRTNpPOuzOfrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19140f5c8f.mp4?token=hqlQEn_qTY4yX5W8aQHJFvu-4cqDL1gHBtv5H1tmHV8Ep7sDiFDmu0TpbN2yL0msdDyIfMEcfHs42FYof6Qg5t_LzDVeSqj9C6v1pQnRw_Li8qieL_0dwjhkJtNZ7V-HFNUv17v1iFzwuEO5nbXAlCDC69CcYLSnVIxUjM4rsHPyNA6ZJi8kU5bPj-3qXOsEe4fhbWAoAAAhG0WOO83rWGagtnttm1tvYL6dSl48WS6lVY02MnxGESB78vlbtRUNXMnFMjt9pec52ezg_hclwb5Qbkmvt__9PjCMDpid1XkRy-jCp4MEbE3th69Kpk1SQpWqMFAzhLRTNpPOuzOfrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام فرماندهٔ یگان‌های ویژهٔ فراجا به شهدای دانش‌آموز میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/467623" target="_blank">📅 07:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467622">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هوای قابل‌قبول پایتخت در دومین روز هفته
🔹
براساس اعلام شرکت کنترل کیفیت هوای تهران، میانگین کیفیت هوای پایتخت با عدد ۶۸ در شرایط «قابل قبول» است.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/467622" target="_blank">📅 07:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467621">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc0186084.mp4?token=lYl_4eU3axJksw38QmO6I6r1uzDYfbDvb8YrL729tu8O9f-b4ZpMfqK1KEY3ugSo1kik_DTXMo2yxDnrYea6P5jLYdleFRIX-Q83_Q0vNTlXqMk9UcLXoQSmhOatL-17sGb6V9_NNBY7uzVYLWEeni3i3RPi-UIwHaWzReOOEI4g_AfvF1ofO5bo68QTpyWieNMQvaZKzLwIM9Cn4cLmaWH1tKpL31R0N458DkbZNQd_Y4JtCaGAr04W58uFpIYO3lPJuMq7vY6INiIx3L3_wWPISkjE5EntzunPAW_5sPUf9B3kkYVIJtOUFjySaGf5AETGFqhE5XPKjLoj6eXKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc0186084.mp4?token=lYl_4eU3axJksw38QmO6I6r1uzDYfbDvb8YrL729tu8O9f-b4ZpMfqK1KEY3ugSo1kik_DTXMo2yxDnrYea6P5jLYdleFRIX-Q83_Q0vNTlXqMk9UcLXoQSmhOatL-17sGb6V9_NNBY7uzVYLWEeni3i3RPi-UIwHaWzReOOEI4g_AfvF1ofO5bo68QTpyWieNMQvaZKzLwIM9Cn4cLmaWH1tKpL31R0N458DkbZNQd_Y4JtCaGAr04W58uFpIYO3lPJuMq7vY6INiIx3L3_wWPISkjE5EntzunPAW_5sPUf9B3kkYVIJtOUFjySaGf5AETGFqhE5XPKjLoj6eXKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: این فوق‌العاده است؛ من می‌توانم احمقانه‌ترین حرف‌ها را بزنم، و شما تشویق می‌‌کنید!
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/467621" target="_blank">📅 07:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467620">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امروز، آخرین مهلت انتخاب رشتهٔ آزمون‌های سراسری و پذیرش دانشجو معلم
🔹
مهلت انتخاب رشتهٔ آزمون‌های سراسری و پذیرش دانشجو-معلم، و همچنین پذیرش براساس سوابق تحصیلی سال ۱۴۰۵، امروز یکشنبه به پایان می‌رسد.
🔹
متقاضیان تا ساعت ۲۴ امروز می‌توانند برای انتخاب رشته و یا ویرایش آن اقدام کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/467620" target="_blank">📅 07:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467619">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZfkeaNBsB0DQmSBiEjtiFF5URaFrEqMQdnw7f8M7CxT2gTaHnY9nteG6YNuJRUS5mY3VCD6PaVU_3feOLOoDC5PgKpsLsRheXBlUZQZndgyN_aAShkS2_SCILyUWhTsc0YgnpQRje0HzDU6vFeeRAgc_F8pUU_AwMvKRvd_TzdtBTT4mREsm3mUpGbroaf-RessF7vVSSUehouUjd2NAq0Jw_4QWrPtVKMTTlDV1Hd7KLGPgsaHqx4kcnLV4r9c7NocFs7v23z2qfuikrVm1OU_hYphyGhb-pxSLmj_mm9cNZ_zYo22fRUdo8eWMYnwq5U0IC6IjNmBJGAkeODwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکسن آنفلوآنزای رایگان برای گروه‌های هدف و بیماران خاص
🔹
علیرضا رئیسی، معاون وزیر بهداشت: قیمت عادی واکسن بین ۶۰۰ هزار تا یک میلیون تومان برآورد می‌شود؛ اما این واکسن برای گروه‌های هدف و بیماران خاص به‌صورت رایگان تأمین می‌شود.
🔹
اولویت اصلی واکسیناسیون شامل کادر درمان، مادران باردار و بیماران با بیماری‌های خاص و زمینه‌ای است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/467619" target="_blank">📅 07:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467618">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvScnsu8Rkzczrh6sDOsXhau2mnIwgjTqPmfN3mXLQSr-KZFXsMS7y074Mrx_YS7piJmFaTptOR3h04Hyr9G-wwGe7wmq8d4CWEphBMcmNN2P7cVBxN_BKw7e1O_6rdNZA7LPuOKU0Yubc0HpMxn4z4TdJR6NC69xj06zjlqQNF-Qq8niy_TvrJyOcgrcUsqj44uMe4JKZGeqV1VDWhe7_sId05ixp3Xg7jdjtJbHSNBLu0v3kdYTCbtkaJIshz21oqOIIIChq2rJFrir_rpxmLQCicikOl2pCN-CZauPG3lhOF4P_XaJM17rizvgoBtzLs5yMMM2h2cYxMT3uHfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیر خلاص بانک مرکزی به بساط خالی‌خوانی تراستی‌ها
خالی‌خوانی چیست؟
🔹
خالی‌خوانی تراستی‌ها به پدیده‌ای گفته می‌شد که واریز پول صادرات به بانک‌ اعلام می‌شده، اما پس از مراجعه برای استفاده از این پول، مشخص می‌شد هیچ انتقال مالی‌ای انجام نشده است.
🔹
زمستان سال گذشته میزان خالی‌خوانی تراستی‌ها به حدی رسید که دولت با کمبود دلار مواجه شد. این کمبود از عوامل تصمیم دولت برای حذف ارز ترجیحی به شمار می‌آید.
سازوکار جدید بانک مرکزی چیست؟
🔹
طبق طراحی جدید بانک مرکزی، تراستی‌ها ابتدا باید مبلغ مشخصی را منتقل و پس از تأیید کامل از سوی بانک مرکزی، مجوز جابه‌جایی مبالغ بالاتر را دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467618" target="_blank">📅 06:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467617">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxM23KCOB-KftzdQQvJ5v_K3CjEG-xr7kM35xPfzA5cQCdY8xaNxNI_HdE0ocFBl2i3zRAAUBaLRRXHfdmPWntr3920rX_1GyxELzlnPJmhN3483rJY3wNqjktpwhXVFJIt6VgXzCW1YhDEonK7WYisT8AaZyu8dlso5IeUmGkFGCvR7bROMra7myKFloFAPnMiPzF7V2ST55WY_hWaDYn4oQZRJLNzriD1GBfvcOCsPHk9N2JFdfjIsQV3xyM9-Xp4OAx-tq3ZJwz-hB1VR0LYxMvPgXQemWSlL-KaJzEeVk_lFUZ6zFWoj1znBK-GdgCS9X0Hd2NZYrL9OTuwlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نارنگی مازندران جان گرفت
🔹
جهاد کشاورزی مازندران: از ابتدای مهرماه تاکنون، ۳۶۵ محمولهٔ نارنگی به وزن ۷هزار و ۵۶۴ تن روانه بازارهای جهانی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467617" target="_blank">📅 06:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467616">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3d92785c.mp4?token=Kya278t4Td6J27iEj84t2zVX-FTol7Fw1lTIVDQDJ0GZB-z9u1jGq6TpPccx6PZOcPiJ0U7ofS-HAvSKE6TzmFE9vEFVGLdyvdCv63eSgItf8Q3cyzApeIOAaXHdm5TL1TpssL61P0BmbBSkdm8mgAiKyEnVXbvE9_smIxc85veMpob3OLv3vFyZRQYMn6SRL0qY06qao8y0ozI28K6_aryb5Z9HZl-3Vvjkd8bdLjJ8oBsxmmIPscq1Zm7mhurkEY8o8I-OOryfAxTtTgaEjHuTlicMUVtBQ3uJfVve6At_FSJXjUpHYvCmsL02xC3-aM4h97dsHgo6jO7RlCZfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3d92785c.mp4?token=Kya278t4Td6J27iEj84t2zVX-FTol7Fw1lTIVDQDJ0GZB-z9u1jGq6TpPccx6PZOcPiJ0U7ofS-HAvSKE6TzmFE9vEFVGLdyvdCv63eSgItf8Q3cyzApeIOAaXHdm5TL1TpssL61P0BmbBSkdm8mgAiKyEnVXbvE9_smIxc85veMpob3OLv3vFyZRQYMn6SRL0qY06qao8y0ozI28K6_aryb5Z9HZl-3Vvjkd8bdLjJ8oBsxmmIPscq1Zm7mhurkEY8o8I-OOryfAxTtTgaEjHuTlicMUVtBQ3uJfVve6At_FSJXjUpHYvCmsL02xC3-aM4h97dsHgo6jO7RlCZfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرگانی‌ها دیشب، زیر رگبار شدید باران هم میدانِ خیابان را ترک نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467616" target="_blank">📅 06:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467615">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il-080bMEIdBI42ykCYg6teEu47YiZCEdixe75rKgNHBY7qIB3Jt0D1wXOT_rY4VzJqaY9h_TbF4z3Tnkqx_pzHd2CL1dd0qsJZYwRCPebQp6drVfU6cEt_JdoPk93OlogT9wzPTnFo5kL0SY5Ov42ISJviFng3vG5PYggifKc3lKKn4L69KRvZUK0TPSrDX3S_gmuKP8ks7xi07j29EuNoCzaznabw5vhS9Dxl6Zdm77pIIjYNFDbVa-BGhtiZwfiHPfNxT60c8ABZs4IWv9wFTO8b5yKZeFzJ2wON8yCO_nsKmjjk_5eS0fdWUxDAZaRT-xo_h3wpNA_4TlSxkWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساحل مازندران به کجا می‌رود؟
🔹
خوشروان، پژوهشگر علوم دریایی: اگر روند کاهشی تراز آب که در حال حاضر حدود منفی ۲۹ متر است ادامه یابد، جغرافیای سواحل مازندران دست‌خوش تغییرات جبران‌ناپذیری خواهد شد.
🔹
مطالعات جدید نشان می‌دهند که افزایش دما و در نتیجه افزایش…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/467615" target="_blank">📅 05:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467614">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌یک فوتی و ۲ مفقودی در سیل استان گلستان
🔹
دانشگاه علوم پزشکی گلستان: براساس گزارش‌های اولیه، حادثهٔ سیل در برخی شهرستان‌ها از جمله مینودشت، تاکنون یک فوتی و ۲ مفقودی درپی داشته است. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/467614" target="_blank">📅 05:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467613">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5848447aea.mp4?token=g0_eKK_ha_Kd7Vecbvn85g7zC6q-1eYRDfHZxqqTx6HCRmjFGdHCJpKBwdROMe2-fZ6bhPG75FzFzNr9-pOlZc_IDQFhbp4B24Nr3Uj5x96aFDfgbn2JsPtztY7Jc10uKvePgIp5RDaN7oz5y95GJmgC4mCWgKjl7LlXIlzcLzUMGMpR8eRd1Z_sTUcxer2XYe1Ke1oGzoM9t9E4PNHx5cOMWkunmC0801Xar9MmeJajgM3MzkwhNvKk0M9Iv_aZm7j_XcHf9lis_85dDJfZO8rns9vss4oHqI0EcLkTyaCbSTLChTU0MlWnjfMQ88r0N-BGvcSdd0pvu-rzD8MZ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5848447aea.mp4?token=g0_eKK_ha_Kd7Vecbvn85g7zC6q-1eYRDfHZxqqTx6HCRmjFGdHCJpKBwdROMe2-fZ6bhPG75FzFzNr9-pOlZc_IDQFhbp4B24Nr3Uj5x96aFDfgbn2JsPtztY7Jc10uKvePgIp5RDaN7oz5y95GJmgC4mCWgKjl7LlXIlzcLzUMGMpR8eRd1Z_sTUcxer2XYe1Ke1oGzoM9t9E4PNHx5cOMWkunmC0801Xar9MmeJajgM3MzkwhNvKk0M9Iv_aZm7j_XcHf9lis_85dDJfZO8rns9vss4oHqI0EcLkTyaCbSTLChTU0MlWnjfMQ88r0N-BGvcSdd0pvu-rzD8MZ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مفقودی ۲ نفر در سیل مینودشت
🔹
هلال‌احمر گلستان: در پی وقوع سیلاب در مینودشت، ۲ نفر مفقود شدند. نیروهای امدادی درحال امدادرسانی در مناطق تحت تأثیر بارندگی هستند. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467613" target="_blank">📅 04:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2LNUlBdOdoS3BFLS6m5zOExzjZUGgfLFcuay1TQrlAq1akq03rpBB8NjjP0b4j-bq6Tc3yOFwzC-DSW5RnvRmZGiSS9QcVOH9jZzgbRPht1U7RseS-chCTgjpi71RjEgDC1QEKgkFklI8bcEJiRw9q5tf6lup6x8UMFpil0-Vy2gY558RA4IZvr29C4lGgpq7nG14PMRdcS2j2BmHyEWaOGuX3P8ZQU8q0SC-aKrBgH9ibBUsyzEh3rttD6Lway-WNB-hbRkNN5NIVPIEIcWTLllZ6kuOVo_V_-Rzv98iF3FcbpCyWHDg2f5eAk-AA_CX8nPtRo5DyQ_Lpf4nwKmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب پاکی ترامپ روی دست سعودی‌ها
🔹
در میانهٔ حرف و حدیث‌ها از ورود یا عدم ورود آمریکا برای کمک به عربستان، ترامپ به شکل غیرمستقیم آب پاکی را روی دستان سعودی‌ها ریخت و گفت که «آن‌ها خودشان می‌توانند از خودشان دفاع کنند».
🔹
در این میان خبرنگار از او پرسید که آیا آمریکا در این موضوع مداخله خواهد کرد، ترامپ نیز پاسخ روشنی به او نداد و صرفا گفت «خواهید دید چه می‌شود».
🔹
ترامپ همچنین حملات تلافی‌جویانهٔ یمنی‌ها به فرودگاه‌های عربستان را «وحشتناک» توصیف کرد و گفت که قرار است با محمدبن‌سلمان گفت‌وگو کند.
🔹
او مدعی شد که آمریکا همچنان با انصارالله یمن در ارتباط است و در این‌باره نیز گفت: «خواهیم دید چه خواهد شد».
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467612" target="_blank">📅 04:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGJ0lEr50lsN3-RjzBg7LCaPNK3aniqW6bYnRnXPnRBOI-_Am9JlQUaqxd_nzHPvtOULezkTnMDaR0atDZrznVEowdMXHULt-EuOb6c6UB8_kUwm-ss86fiT8hBwLqeSY_GDe--GDGuWfTj7NWNquhX4O1RaSl7XkZhCezq1Rmojz_w8bCYJQ7jiC_pSOKA2SG1vtdKAatpk6Or1ApOx2Rsb4V9tLSviir2EBMGHRGKEXUDpVJWaFYoo30fZ5NyZNHj7YhIC9S8CKobU7G62Ixk9jK8DO7c90i0OLRMSyqBlrt7Paahv05wT-HToLno27CcUavAcjNKhC-9rbj64OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنان و کودکان، ۶۰ درصد قربانیان حملات عربستان به یمن
🔹
وزارت بهداشت یمن اعلام کرد: در حملات عربستان از سوم سپتامبر تاکنون ۹۱ نفر به شهادت رسیده و ۱۶۸ نفر دیگر زخمی شده‌اند؛ زنان و کودکان ۶۰ درصد قربانیان این حملات را تشکیل می‌دهند.
🔸
دیده‌بان حقوق بشر نیز در گزارش‌های خود اعلام کرد، استفادهٔ ائتلاف سعودی از انواع بمب‌های خوشه‌ای ساخت آمریکا، انگلیس و برزیل را در استان‌های مختلف یمن ثبت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/467611" target="_blank">📅 04:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467609">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX3GlAv8f1RAvUVpl3W4f6LAPgGgCveCGYwcT1CNlvd-T53MddiYs0sZf_eW1fur6hnQsGIFuUEQ2ZrO0JPd-vqiGvhEsdCaEnBLxQZ5uT4ULq683FUFNOI8C7HAMYfFfgvLEhytE_I01z51P2rNwwfGU_NhWj9_F2M7uNV6uTY4JQWBSs_m68BY6K_7y1ZgXYBJPGrAwwAsKOTDDRQNiMOLWuQhPaICGUnMubsSAcJaWsjgWoyib3sfMRi3gMLT1_k9Yvrp_IF3mdxPWZdsnTlRLg0mUdLDyijfjAMzrcwW4mU-HcZnPH3nGrSYWmfzLiCK0XQAQckLCpjzyJe3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه داشتن کلیهٔ سالم را بدانید
🔹
سال‌هاست که تصور می‌شود ورزش کردن تنها برای تقویت قلب و عضلات است اما اکنون متخصصان متوجه شده‌اند که میدان اصلی نبرد برای سلامت کلیه‌ها در باشگاه‌های ورزشی است.
🔹
یک متخصص پزشکی ورزشی می‌گوید، ورزش می‌تواند به طرز چشمگیری سلامت کلیه‌ها را بهبود ببخشد اما یک اشتباه کوچک می‌تواند فاجعه به بار آورد.
🔹
ورزش منظم باعث می‌شود خون با سرعت و قدرت بیشتری در رگ‌ها حرکت کند و این جریان خون پرقدرت باعث می‌شود کلیه‌ها بتوانند سموم بدن را با کارایی بسیار بالایی از خون جدا کنند.
🔹
اما بسیاری از ورزشکاران و حتی افراد عادی در حین فعالیت‌های سنگین فراموش می‌کنند که بدن خود را با آب تامین کنند. این بی‌توجهی باعث می‌شود که کلیه‌ها تحت فشار بسیار شدیدی قرار گرفته و در بدترین حالت دچار آسیب‌های جبران‌ناپذیر شوند.
🔹
بنابراین اگر می‌خواهید از کلیه‌های خود محافظت کنید باید یاد بگیرید که چگونه بین شدت فعالیت و میزان آب مصرفی تعادل برقرار کنید تا ورزش به‌جای نجات دادن کلیه‌ها باعث از کار افتادن آن‌ها نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/467609" target="_blank">📅 03:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467608">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25c5e1505.mp4?token=dt2_OUj2Hqge7sqPRlKdcjzy26RZnfbvpAa1FlADT4VZmqCDiw-xt0tTvX2pnQsdQscoWK5V81ca9Pe1VcfXqqd51frrnkZ-5Ab33DLQ1Ozd3mo0z7FGkY-W2hi7ahWXv9OrMZmlVqRR7CsJbh-giB0FQeSp3-WozI3dOrH23FXrk35KFKy1SYiQ6AHm-SMkbxr6gEmFAsvwZMRPEjUKq4vvjRU87H4kybO96H1gp4G6r-1GLITSNcwIl51oBrSF0_NF72orKZAdUllcd_27JV3VFCm4qMhLluovNXpxh-fDEoD8Z_8QjsTspgzUrFrExa9ryyXpEeyihutVF3QEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25c5e1505.mp4?token=dt2_OUj2Hqge7sqPRlKdcjzy26RZnfbvpAa1FlADT4VZmqCDiw-xt0tTvX2pnQsdQscoWK5V81ca9Pe1VcfXqqd51frrnkZ-5Ab33DLQ1Ozd3mo0z7FGkY-W2hi7ahWXv9OrMZmlVqRR7CsJbh-giB0FQeSp3-WozI3dOrH23FXrk35KFKy1SYiQ6AHm-SMkbxr6gEmFAsvwZMRPEjUKq4vvjRU87H4kybO96H1gp4G6r-1GLITSNcwIl51oBrSF0_NF72orKZAdUllcd_27JV3VFCm4qMhLluovNXpxh-fDEoD8Z_8QjsTspgzUrFrExa9ryyXpEeyihutVF3QEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امام حسین(ع) کشتهٔ آیندهٔ مردمه
🎙
حجت‌الاسلام رمضانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/467608" target="_blank">📅 03:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467607">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiDWMtu6WFE5RQM9TH2nvuR1hI5wZerh29gLazRP1Tg6CutwqO40M9ocQQh6G70WyMVX3ALs016SR-0EoqWrBPKxlz85VzytwwUsacfg4FSrmgZUd_WhOXfF084V_aU33gpDlQgDVRGi0oMgem5tl9nifbZAT-Lc55hFKE80kQjauu4zPshNGgsAw5cZkuylKHsfjfEpVTEBJo9WpxeWgVbEJ-FvIx8nR617P_kvE9N_v_lAptejqYsgUw1mSRCkrDFpXMj9hkIPnOsFujTya69wbdqmY-krQ6zhIQbjqmXy79445Nu3b3uXR2eLVBgKirHn-Rb-MLea3qLIUMdZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها ملاک بهره‌مندی از طرح تورم صفر، سکونت در تهران است
🔹
زاکانی، شهردار تهران ضمن تکذیب محرومیت شهرستانی‌های ساکن تهران از طرح تورم صفر گفت: هر خانواری که در تهران باشد و براساس اطلاعات دریافتی از مراجع قانونی کشور سکونت آن در تهران احراز شود، مشمول این طرح خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/467607" target="_blank">📅 02:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467606">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عضو ارشد انصارالله: حملات به فرودگاه‌های عربستان، پاسخی به حملات علیه زیرساخت‌های غیرنظامی است
🔹
محمد البخیتی، عضو ارشد انصارالله یمن در گفت‌وگو با نیویورک تایمز درخصوص حملهٔ روز شنبه به فرودگاه ریاض گفت: این حمله در پاسخ به حملات عربستان، از جمله حمله به…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/467606" target="_blank">📅 02:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467605">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792cb9b11.mp4?token=RTT5w8GjE3x8eb3ZA3YkWSeqnKiWGnmVew217-QML-YJ6Jj33YqmqK9Z9LkxOswn2_a0U5lS0AGHKddY4qgG1szMBWdm2GLSZhzrxE6xESFvHXQmGLD5I9r_js1C3kmXUlQycd0hQy4YKyGksPzdGJMNH1RFIjf-rrqj_LspNUXvOujssHeaAFWv7kicRWX876-aX1W5Wzl5itP8g-PGBoY6i2sG2Ex2T4t5S75mtTz1hqngfMQ08KteMr1RPR6HjQuEbpHfOiunEfR34aarrxrJME50DWBcQ96jg7oJeBlBrQnPZoCtzk2ReFwzEw2o9DDBbTD2AWGsf0BfYu0iEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792cb9b11.mp4?token=RTT5w8GjE3x8eb3ZA3YkWSeqnKiWGnmVew217-QML-YJ6Jj33YqmqK9Z9LkxOswn2_a0U5lS0AGHKddY4qgG1szMBWdm2GLSZhzrxE6xESFvHXQmGLD5I9r_js1C3kmXUlQycd0hQy4YKyGksPzdGJMNH1RFIjf-rrqj_LspNUXvOujssHeaAFWv7kicRWX876-aX1W5Wzl5itP8g-PGBoY6i2sG2Ex2T4t5S75mtTz1hqngfMQ08KteMr1RPR6HjQuEbpHfOiunEfR34aarrxrJME50DWBcQ96jg7oJeBlBrQnPZoCtzk2ReFwzEw2o9DDBbTD2AWGsf0BfYu0iEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر رضوی و رواق دارالذکر، مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467605" target="_blank">📅 02:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467604">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
ترامپ: ما به زلنسکی گفتیم هرکاری می‌خواهی با روسیه بکن، اما به پالایشگاه‌هایش ضربه نزن اما او دقیقا همین کار را کرد
🔹
ما یک مشکل جهانی داریم و این مشکل ناشی از کمبود پالایشگاه‌های سوخت دیزل است. پس او چه می‌کند؟ می‌رود و به پالایشگاه‌ها حمله می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/467604" target="_blank">📅 02:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467603">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس:
یک فروند نفتکش در پی اصابت پرتابهٔ ناشناس در تنگهٔ هرمز دچار آتش‌سوزی شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467603" target="_blank">📅 01:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467602">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfYWC8xUtdCs1QA9KTmWbqOb5K1goT_Q_0c89Uie9ow7cznvw4yC6d8LwTLlLzitvKivQ3gnwH4FS8EjglhwdpCCUSkAAs4IkflvaU1Y7QsLUzK3wtQiaSbhzjNuMIeJ2hTOlbB9EGuIsvmS8gc6ZrywjuuPv4pkNpdy4hGWUVyB5cgZCUsvPw7lzgQwpgTu1fLfrOOBySRC_-kTY-kWOpKI-x1kWnu3lG12atQ2NbJcFgn57Mxffaf-i2iOAjbT9FNRs3hGV7c_-MHEyCeKLxFOpGY4FVD-NWcVy-KjbIawQjp9PpbHdci21-29ZI8sviqfox3V2Uf62kQs7Vjq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ۱۲ کشته و ۵۰ زخمی در حملهٔ موشکی یمن به فرودگاه ریاض
🔹
نیویورک تایمز به نقل از منابع آگاه اعلام کرد حملهٔ ارتش و انصارالله یمن به فرودگاه بین‌المللی پایتخت عربستان در روز شنبه، دست‌کم ۱۲ کشته و ۵۰ زخمی بر جای گذاشته است.
🔹
به گزارش نیویورک‌تایمز، این حمله…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467602" target="_blank">📅 01:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25361b78ac.mp4?token=Tn27L8-WtkkHPj_k5LF8naV7CVbFY_1UE7QbVx3fRWTT_dhg0TLOld5prNdFoIyW9W_4k-vVf2fVAZ_ulhv3NXC8OnrSatCEyUbtPQpkCaZx1wM2EOLttSQnpTkdi8hMIJo_HGcgsVawmbJpgHMDZ3xKl9oNiBuaxzxrwwc-usb275YOI6KhRSc9tctIJCr1emBJOuoouYSdpCevVe0jK-KYyzYs552pCUZWiPlpGcpPPjRN6-F2GOsWxnId110VAsP2yyUqpjBbgsSnsVg_iuj5QhdwxXlSrtHDcRgUtXOxAnEBL2S2m1AkmkNYGIRriV9XM1PAwktmibXSjZzHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25361b78ac.mp4?token=Tn27L8-WtkkHPj_k5LF8naV7CVbFY_1UE7QbVx3fRWTT_dhg0TLOld5prNdFoIyW9W_4k-vVf2fVAZ_ulhv3NXC8OnrSatCEyUbtPQpkCaZx1wM2EOLttSQnpTkdi8hMIJo_HGcgsVawmbJpgHMDZ3xKl9oNiBuaxzxrwwc-usb275YOI6KhRSc9tctIJCr1emBJOuoouYSdpCevVe0jK-KYyzYs552pCUZWiPlpGcpPPjRN6-F2GOsWxnId110VAsP2yyUqpjBbgsSnsVg_iuj5QhdwxXlSrtHDcRgUtXOxAnEBL2S2m1AkmkNYGIRriV9XM1PAwktmibXSjZzHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیپلمات آمریکایی: ایران ممکن است این‌بار حملۀ پیش‌دستانه کند
🔹
«آلن ایر» دیپلمات و عضو «مؤسسه خاورمیانه آمریکا: در جنگ میان ایران و آمریکا هر ۲ طرف امیدوارند با افزایش فشار، طرف مقابل را به عقب‌نشینی وادار کنند.
🔹
باتوجه به این‌که تهدیدی علیه موجودیت ایران وجود دارد، بعید است تهران از اهرم کنترل تنگه هرمز صرف‌نظر کند.
🔹
ایران هم ممکن است این‌بار دست به حمله پیش‌دستانه بزند، چون تاکنون ۲ بار غافلگیر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467601" target="_blank">📅 01:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/467600" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467594">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImNA6Nzq-xGNr-tsJpWuxLe01nC8YBDmc0bFcwD_W2iYLI9zieB8P5sq0T9DwrACOPDc04W6wXLeZUljsOiQg2U1cxYO2d2ly-tGj9DEqAsHElGBcRx5163jUDxdc73SOp3gynE0aFcsExjquRO5RDgno4ZouD8cL7KQHLlwvbvFlX1tGazRnuLqbuS9qa91i4m-4ZNFQu9u0oskTHpgKVwkyMoCjtRfqha0Zxr3-GCEa7HgMDcGp3F-p8nVvJJhrdA4pOFxOAniTQrp8y0R8NU54bNVYDqBtda0qGwO36JM2o2qOWM0-9RQOr8GOTg3ZfSiTo5DaJWGOd9tEtO8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWz6PTcMV9Gh5kBp4TDFEclekuF0VWpgAgk8-Eni_Dsry78PXHQSOyyL_9q29Jj-igOPlZ9p6F-kdstcQY4K5bWSTGrlV65kCDWPZEwSgPb0SMHQP0vDwwQFkCNLME1cfC9J1ZDqwEds1_bYolB7bn4EaeDNj1ptcb46CipLTSa21KTEB_SUuTkAy4rrmNNZH1Yyym0Y6e4mLJXP8egQdCDPcB4X8l6_kmG7T2VSBJu3xrVU4zzRl-rDcNGCI3IBqjfuBjKxc3zs73Y9bDrYbWjhFTcIdZHC60pgtpjhraJN69xJypZPjMIl30bkp9-e0LgYoSS_YqHX2T5IYgDZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tf0GIFwsDMxURZ1tCxUnWgoCBDwLgAZGUu3VrOzhOVxPWG0Qaf26-nHcn_UeEfW4uQ3ek7gXB6Dk9Wm7dYixHCrBvdr5s41L7uKjGVGI5mYb_-PEB59jE8UROryvWbcR_4MnqTmGDPzD0oTUxF5g4X0tB3ye_GVubeBv_L9zNRLKQ2rrG-o45dEq3I-bsiMltXD1T5mYx_eLlwbpn98fPAYmbd6fDmB9xohHB3ItUfqE6doBfMW5QmSdJ50rqVShgj3B_HFAxwcHzU4FW6Bl3lk9SHflU3eTtyJcTitjoL-K2gMqOGO6J563nfwD2OR0JRJGJqMk8LFAv3A3eKyE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2pQ0wPm1FJFk7gotmQg_gP4g5OxepZF0eGY18p-NqlXbk5pvuSTtSODGgdF-Ga7wi2X05XDJRgmkm9l4Lc43RNDdsFhsjH2DuvLCouG8OmRNoGSQkaDF_O_Mwq9dOkk1LhF6AmsR-TopIIZLbqNqLMfhYF4fq7Zsu2xID4iZA0MVar86M9amtoF-9UB6tybi4Bs_twsDC1vMiXByMAEa_J7uL-iWzx5n39ccJfU7H4nDPEdj5ALdQWHldm4KBMfUuyxRVFRX0LVpoq9z9JS0NN0acS7ApCFB33jIo3h1LxkNl4xj9WIZUFbrvYD1RVMIdqG1VhP4ZzT52JVADC6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpN9GXGb8TD3LimSSjYcQ71KIYmS4ul2fZDnVGdXnDm8cDHAtxgIVVCDc8VVY4-KFoHRiy7XSRszjaAw_WgJXzZ37bNgyw_4IoN5vySSV2rtIQX1MCJXFgVlxQvTvSFk2uBURlfLxSXhRYvrdTKqT4Ns3UQqHLnFDSwYb0gpf5rntg77mCgMi0ZUCeoYnNLrpAykK8maDqFOG9vHCNy20p_CCs4Ifjb7a8mFf5GUPiwepQsq6wnEYW4WmS8oVnq7sNhGCYZj-AWN13F_UnyTnmn3MM-Ug4xYHNo7G-jdJJHJXhtpofkx9QHmLIiqh_2-tfB3UJOLqNcEGBQMzqtncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjDiCcHKs3NhVyw7kphRwU7SOV9M35Rn6AWQCNi9apaFks0A7ZL0AxHkDAnI-itvdumvWB5kQRxrh-eX9_e9QaQi92V-OfacZRwn0yF8yRkCFteiYNskFoJ53v2qraq8dFUBaThExfERA4_y7CC4EZdTx_2FZ5J-P9dnN04i1w-XXpnVBaBiduKUuFWjfQ419n09cqeeCX-NA1aMlW-T_MQVHwhIpd-TIDKPjU6u6zAu5tPH3O4YozewwWos338zXR8oTwhf-qKH3RRctcEK98Clz7vUHl6uzp-eggdTnU8-XldREt12FqVPL1jgiGStdRNW9CxyPO2XsGNXZogFpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع شبانۀ مردم نازی‌آباد تهران
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467594" target="_blank">📅 01:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467593">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8ewKRl_Z5x7p3SGD8D6n6OE7ISXW3GKI1yPI3RyvOBIa_z7TPg28stXI-hkkXW5QpZewtayz-aO0Bg_h31kBYqIg8mlkL-id5kj6JHg3_sEKKwad65roj2w6poQvxHQoo5OXQtxYa_4STLpqDKnFDtDG9MtMA4mdwsfGd71Nr6SvXAEbR4GYTNCQViarf0OD_k1JtcUq14aIZobJb_02FpMpAniSNAtDl1XUldHTD2KZNNDIitIWu2n-_EsCRsswGNCm-ELMYYmFMJp0ZGUtLXc5W0bq78iBDmjYHlcF-m0a7LlKtu5_W_gaQOQTm-ljrED6IVSaLhpl0Zrht9zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی: بی‌عملی اروپا در قبال تحریم دیوان بین‌المللی کیفری و تهدید به برچیدن «آجر به آجر» آن از سوی آمریکا، همدستی در حمله به قانون و عدالت خواهد بود
🔹
سخنگوی وزارت امور خارجه در واکنش به تحریم‌های جدید آمریکا علیه دیوان بین‌المللی کیفری و تهدید به برچیدن آن: مارکو روبیو تهدید کرده است که اگر متحدان آمریکا دیوان بین‌المللی کیفری را مهار نکنند، واشنگتن آن را «آجر به آجر» برخواهد چید.
🔹
لطفا دههٔ ۱۹۳۰ را به یاد آورید: نظم بین‌المللی نه‌فقط در نتیجهٔ تجاوز، بلکه زمانی فرو می‌پاشد که استفاده از زور عادی‌سازی شود و جهان در قبال آن سکوت کند.
🔹
باید از اروپا پرسید: آیا ایستادن در کنار یک متحد به‌معنای دفاع از حقوق بین‌الملل و نظام هنجاری-نهادی پس از جنگ جهانی دوم است، یا همراهی با او در برچیدن آن‌ها؟!
🔹
اگر قانون و عدالت برای خشنود ساختن متحدی متجاوز و زورگو قربانی شود، سخن گفتن از حقوق بشر و نظم بین‌المللی مبتنی بر قواعد، چیزی جز شعاری توخالی نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/467593" target="_blank">📅 01:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467592">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMl8noEMuFHBaQe82b7N4QEhitRc45Q1n98RkGEedS4-kq4Hd53J3UPgW92dXMfZ9Nz-Ff6CvjT0dXOHwqv3qegnVimSXo2SUmMrNK-4QxQjd5DVuOKR08H8iknZsv1AIax_8CaWRygES-YfeIbjunl2sUZJponyMaiTWPIt2W75j38rsA-x2siPpN4rn-GFZaRLcTF_zslH2plhimIJVC1rQ0Gjxp1Zdl5OsxpCza-Mu31DY0lSB4ALE1HbQbaunnzOEQpp1Q93C9j_WZSpxcMn03hvayXQNvHpaFfOMNszIDUiVW0LMqDl9qGFvmJMLZdATXqB2vD6bumDZm8qAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بارش شدید باران و آب‌گرفتگی خیابان‌ها در گرگان   @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467592" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467591">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9fabbd35.mp4?token=VU0QD7fRcLTXuoj87PVVfGxyj2dHJGFPiOjzTC2WBoBUkLjvNSexz_Fw3TxFB3i5exprMXLk925OeDHz30ZKLV9AD-bMvcV5QxwRAEK2DS3GzqsHTXQHWkBVUmbl0xzp5A4f8pqVFfzBLT7xnX4sW_93OOoRHq52rD90me0hd5_eAXWDlNBtLhUiBvhqFBjpZGwSFWC73pTzjVymtuNiADgwwoXRs25qiYL42K7v_k09bqIqKcVifrfCig37e9E0hR_1YKAi7Nt6xaU6NiaHdE9ket_NeHVeFMWJXRRGGVtJ7UNYg2LeW4HKBshcEEUai32utF1vof0WIhFa9J9ICA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9fabbd35.mp4?token=VU0QD7fRcLTXuoj87PVVfGxyj2dHJGFPiOjzTC2WBoBUkLjvNSexz_Fw3TxFB3i5exprMXLk925OeDHz30ZKLV9AD-bMvcV5QxwRAEK2DS3GzqsHTXQHWkBVUmbl0xzp5A4f8pqVFfzBLT7xnX4sW_93OOoRHq52rD90me0hd5_eAXWDlNBtLhUiBvhqFBjpZGwSFWC73pTzjVymtuNiADgwwoXRs25qiYL42K7v_k09bqIqKcVifrfCig37e9E0hR_1YKAi7Nt6xaU6NiaHdE9ket_NeHVeFMWJXRRGGVtJ7UNYg2LeW4HKBshcEEUai32utF1vof0WIhFa9J9ICA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران و آب‌گرفتگی خیابان‌ها در گرگان
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/467591" target="_blank">📅 00:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467590">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌  فراخوان پزشکان از سراسر ریاض برای مدیریت وضعیت اضطراری
🔹
در پی حمله موشکی به فرودگاه ریاض، پزشکان به بیمارستان‌های سراسر ریاض فراخوانده شده‌اند تا یک وضعیت اضطراری جدی را مدیریت کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467590" target="_blank">📅 00:49 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
