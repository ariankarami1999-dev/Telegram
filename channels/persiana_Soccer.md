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
<img src="https://cdn4.telesco.pe/file/NEwEOtXVRnM25X7oeN1yB0uP41Bm_ANuJU5A-gIf13FrCUR_BLWpReLslQvvL7NigZ4Gk9R7HJeWxVOHEr14VhA1bupLYCBPQkA54lvaNnwxedW5xwCCu2_4u441gUqXVjOwLFVGsyOEfNCk7d_tn3lNb7-KrnF3NRrA3zxeBPeUWfMrO54zxQoFZuSH4fi2G73ofwbKENvcBEDRExM3UnkVla2UzafcEwZEMpYExbr_MNmVwXv5QtpleVLYCqoVFDWt8Qr8bX9h8X5Dvq8WzOvd2TViZSnLHA51sHQ1nMvRytkBGDgs9q1PQuhi1HZPN9jNQNBHCeTjT2lKRdH_aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 198K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 15:25:22</div>
<hr>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyG5n-iWYWHz2J3e_Hc7c_XskWjZ66m6ziiRvkzyA0YwmKWI7PfRJFjPeNE2U5XxPSfbfWiPwfsgotN3w62nfjoe5mSauGwvrYBjpE8TW-Yj5xXo14yN3a8zXU0AD_cM95HJll5IUObzxh8kQIaNCVCAe3C4trFUzpOhJp9i1HdgbBL1YuH2CC1UeGfQ2BDQ6tM_jGXN7zLSp9JCF6zTrX8RBFkvPkNAplHyzBNFhK8wRFeRt4FfLA4nM1FpyH9DADwO2vIlauZy1ZMhm0FjnMN-65u_u4u0tMLf4JF-4y5jpF6zavkQn8ceifMIrpK67JE5EDYlCmUDev2RNC9-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3SJOWz4dgk9KfxwYUjXk6f_sGaV0z5Vn6sYSS4blbG0vEvG1iYf0CkJCAbnkqaKwPw2Ce6fYL-BfGrHRREVJ-OkPUxqJkdNsnVy5mdNQgZWvlZ2OrgflnuHfc1G2Lm5LwAhDkGENCFORdkpV-S8aDkhi4pjMSUjKybkBbDCabaE0TBl7oNtetbTwv-9taPLQu__dmABHMtm36ZhIs0P0ZHWO5mBPsaAXKrjAD7NYk57Z0VpddKrg3dQr8FkMNrpxrCaaMB3JG906n1woKEkFX5GNF2r-_BQklIpSQjY_DO_sWIGDrZ7jIwx81xKut8_WXLxBR7eNd6FzTiyW4uJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4LeNLp1GQ82MZsYVidbo-Z1F-4fOct7_suEFflxnRbXsJt-zofDeCJ_RFwyUTut8lYNDL1-xkeGStnzmJCC897CTROUG_PlSpsQiQ8nrigy-3kXU5cMx5Kqmi92QSvMkQiZ2GaVZIEbpyyN1vSe8IyE2vM9igUA_DHhE_tPFHQdSKr8mzFDYpCu_XNiwNrzp1B1p4MVDosnyIyJrBgdGeTw9Y_RJGbZs2XocI-_i1e2VusjEWz7whQOvWLZO6-DGRPm1lButANOqLOkW1B3M4tuircQjQ-DIm4CcsR8bUpgDPxCHVaoaGYYeQdvhFqCOqahkGyWdBWPRJ74ipLycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPd1I8eGPqX7cvNcabqS2Aox4MAdwOiTx9MHAP3r-JWWDiBPzLJyLmyVv79XTwAb1kdYVnp1NdAou2X0IuDGWfOf6NpVQgo4AUrY7I-ITRoIlwixIWPd-izZ4Jq-1NwOlkuI4IMreDrrsg8h7ZV7rQk2rV93Tw6TBx20O9BCVTrybCtsODV6LL6d2ZGfA6-KDbfDb32QgsBqL90Dky4e8XEwDKBZkGWd-JdXxpMAb0uw_9irwndvnLW3yE7J_fKYbP7nv9u5lInd_ssfBd8Y7TOV4WYi4ft11E4KeuipLB_Ksh-TzPjaRcot4aosxpBO2o_sNNakBbX0mwUZZyge8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXnPGBzBV-NzfXUZrwk-JIfEV9ExdrEALYKuRKDtDzO7NdphCRlGGa1hUt_JBrrOaLZT9NRbyhiF9oDAtArIuhZGpEmlqfSrJuC9PtAtj5NsS-sCh7_fSVecK-6y5DVM72w7eCRL5ihQslNrk24ukNiWmb6t_gqQYOgNsQkjI2jdclBazJwDW6rOKpyK65_4q0WbPqVII3rdUx-koLCBdk-T-WEqKlsaXa-CvXK5sCUSPaOWG-OIXbxPTV9bxTaqNXzmNyH9qFKFYLnoGYR4khWjZAUzblyCptILoXQJW-ANFaJN5C_3ON-Lfl0rksHz9WgMBpC3UzpCZrdZMgkdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22254">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRFVAYGmWi3a1eesJRbhL5BdUv3mrqwkBVrfn2BC_JMET3w8LM8rEYmn4k69FRFtNPM02bGDEBMwhRGtyakczNnscZoKRVEBRlXBY1OTqMea_cnyoNYFtBlFkkXt8GTLgMHKpSSxU6753LHA2VDIbP8XGrbvkIODAj1EvlCxtt6ynlb1UFoRpF1Gjggtd2JabgOgEIEqeUZCMGIdESubPRisoWnrNnYZyL3HQkUzaV0lmJInLnicPyiIo-K8_w4A3Jl_GaaU-aleUrCzsdlnUhrC__oameQ_be-_lWwk44xIyfD1LCx3vTM2OSJ77yjIrO2rAdX08-b3Tq_DGrQWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
امشب
#شانست
رو امتحان کن:
⚠️
همین الان عضو شو و 500 هزارتومان جایزه بگیر و بازی های l اروپایی رو
#رایگان
پیشبینی کن(بدون نیاز به واریز
🤩
)
😮
تنهاسایتی که‌باعضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a2
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/persiana_Soccer/22254" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3-2pooQ5_XBUIVG1yFVcbxPgmy9WQAfUsIXnbvymJVIaTCH0-q-i7m4TIIh4MikmTbgyxRpH3XE268JMeNl8XHNde503n-00hw4n_naRxCLENuGLIJ4lYFjaiopYNu31U-cOoT50N1Tbp7YS851gs33ek0QBsIxvHx114BTS93T1jam49QH46-UZCNUTQDqZuKJCrOVF_LjJHWS1rO9BuvUPC8QjNP5_DCtXgenm5It16F6XMiGyH905bBXwsdYKFP0HWVsZpg1G-e_hMUnfd3VARDcM0uZZy8j7tbQVKLBLUmrIxqjmuFwRxPswO8zymXfLdOsx5UTybUHnK987Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0t_3SmphGbpN_PKwcNN-KtBeurCXR9rbYjSnPHfxdoQozZ-W--P-3fEmR7mKTSGisUMaZcC2jNO6kRzDVm_TikwWN6n3mIIz_uzrOF2i7BKpU8Q6GttI6OK7PDSjL-YLVNlEOcM5uzyHKIOR-h-BGt8j5K3f02G3QFhS0prrVDJ7clT4Iwm8qKY8qzICPblY5IHuH1LQRCiKgqBtQkvCb-Kqxq7bfCj8oyjY91edRrBCnZuUjb3X9TOYeeyqTVTUEVyyE3zCoOAYb9vJt2oFAHADrl53gM5lxPtmpeubcidClFHuwtcOs6pv_Qf2ptptzvpssUIxxJ_lb6PzA70qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTxyK3o2e5C-0z0EGN2bRAOrf6sjeoOD4UPv6qfCkuoSJ8WVCibgMMoKAstodnLUkyM56vvGM19ReZB2qYdbUXv2SQrdvs_gH95tBSpc6KxKERWw6_fxrSSAedqEuIf3H3CEETc5dAqFInp5LBWsLDGVnYBW-yOQ3vqkL-dQHxuKnIKjJGmtTV3qZOdfn7CcaaOh9taEwdQeielaIe2ZcqB7fVpwmExCtWqNFuR-aaG1CKIhFarXlRergBGB6mi18O6yvWequkPVfoguKomVPVhlZyZCC2VZpg9krkaeekg8MwehOoiWb08wvMO_PhH1xB-bXgPsYCuRymB25DFz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aclk6r7Fp5OTjOC24oGlm_7PeJ7yVTqO3EKGFQLoqeB7xI1h4VTgwEJ04UDVZwm3uUHIc6HNkH7V2eB1r9VQs6oAUOc5YoK37fPlz-xvHL_6gpDTtgZPguTt30iUheZTVsTjL8z8--zd89_QOLU6MR631m-2ldR7kihrOem4Jttt_l2vFS9xqxAjVA-Hs0FLiFRTOqHgGdSeSR88aAATdMkE2IazUOYn7kuVhzR29k4Hl5X9DtSpZVd0ZAKjoc2e7HL4si_j-DIcdaGS6ZNvEp0vLga-kX5dyl1qcC6Rad1cpCFKcn5yCaw5oVWscrfKDwJCCY0kflprNxfF3s_zMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrtxX3FZ9ivxfc7jxd351GvB3FefXYgYXSU5WXsYsxUzSprVQvrqnqfYEaXp2u5VEHxd-DRdRe5r-YYoVlJlD3mFDtqATm4YiYVOJcgQBJpOMVydjaqWyaZAMqfTT7onLG1VPz3uZCLxfP2JtdBTBv6alLU0FBqZII70Q2QmSWzN5aqE5kUo3wNfAcjX3bvSFbCAzKMM-bhVf-OryZ1eJyeNqTVisB3u2zBxI8CERQMH0STgtvjVAyeEZGXKcpY-Cw-ijvmUQTxCvJOnYh0A0sdpPNFNhCq8Wi5_9H98YjioIjOP8OV4tfcRr-C4IMWmZz8GXKkGKpmOBR1k_FdWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8YQQszUoYzFSu4dOA5Q8xha25QbeQLnnm8r52C-KytrlaY4FdW-udiQzCULfNfNQALj-gJjxSDkJtlbpaQMk80NADXrvnWLTXPlFdgI1zrri8X0T1P_lXMpThU9eoX19DTTYiPoYlrNAjubbqzJRkAF8T__ggJ6TqEfwplFYdwqToqdWaXWw5CGzXq7J47SHOPepsWFB0PI0xkZKsAS8uBqokK2OhS8rQ49X7LTgf5KciCHUwKGjEo1RQt8rfqYgpX_yWZZNmLeYJbKLYUyVkA6gMUgKtxL7iqr4kY4ohLyWczyC2Kw1zfJfz4lR7qxnmg72v8N1byJPuE18voxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7QKJlp7UmH7NE8RskMht3bTHv8sdnEcLALUowPGCbFXQqM2VwrZHKMSdTV3r5Na8mruNCNu5pBEOU9kEzx_v9qyOHJmvXMJIIhnGoTfFjPdInkXFxnGcpF7yUuErhSO0Fhb3NctCHjLZsaAQMkHADKh8UKhuVoRDtoI5JPrMgC86EoRQC39F1Zxw4rcv198vJSasJ1biti_N0l6UGybzMRC0_NE2NOh-_JD7I9eCT9yurztG5a0g4UVaH07_6ZJMS-7a7hQHQ0XBLdztnx0HzYsdw-03J7Fr_LXZxEFgydyuTgYDi2Lz3hB01boCZaMOR0SY32CuSqerm9tNbjAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfyto_CWiqKMnlqFVzm9kKGRRQgdX12Zn0RPKY3AuZUEFDhexXbJZa6ox25TT2Xbj6UzZn1202C2YMohvUpEKOmV1uj2UpB0feMyoHWPLZXzLNRqqy0PPv25M98stV-fBtKvH9IW0DhBe3tUmAbeI5pYBEZQRqb822hcHgepNqdqtRJXgQPYG8zE-9MNKu6MlhoYza1YKdfHUcGMx1yPIEs-qJF9IGJlo-hSp5chtuNJ8-03Jq8iO0vGMSuwuv3NuqXTIrR0w-E5lkdWswrN05qAMbKEuirggRH_nbw3IPdl4pB1RdpG6r5NbuvVTR4CPwcV99rPPhJBxbcaM_Ao7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=u-O9-01EtuxYh1oiLIqHjglRTJ2djDgGuucFieeccJoQ_D1kTsI8xTw425zEuwohSZqlh2ztrHHddwFDFgjBY9psTn4fBgB2DFFqQdmdxVh673JEHqGH7bX4IT2GD0FsEgCviaOROUTbQcp1VJds-a1yjLYlKD1NhO_EECJsU4qMmQxMSl-GkvcBF6WQ3Z7eeYrgGOgGcLW7qcxMOcUCy2kdZGmUC4NEDGYDYpA6C6v-16qbppFtNQ0MKO-6g8WnovvniGZyqVEqHkisacu85Xdk6V3V36vUWFBngD5dhul8Jf2aIzRBqFuBZsX_bcyhaG8g0a9tk5JJ3lci3crm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuWK_MJGyya90dKu9jl4xK337fVPM4EGIUlg_HjjD9MpA4uSF-5trAYexxah79NaMItmjpeQpwXxSPB5FF9bQPZOnWgyA7tYaOE3DKVdKv4D-4-1ado9KxpZn3z0ubnZ6jEjxqtFnTk1z6WQ2orCHlk4fSp590DBxzeRyFIvn6CxEU9I3yv7Kug_yIrsDRXgL_YzM2fS5tAlXHKOkGPC7v4aPR5rF0g-9_zTr5CcqPqycOlX-j2U0E8nFDAlceS_W-dih-MmK6Kj2uW-RToMBlbFKBMLpP4TyLH2UrrqlNGTKqdyJWWOvIcWV3D7kwjYRkpcRKamc61L1XJX9_4Siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNl22DaIrKwxr8DIAT5wpem9fk4lq-CtYyFvu69O_wlaog1PqxkrjviMo8HmmgFLHfwkfki1H54Z2QIUJqs0OzCX4B6DbYi0v140O57UxYQApywX4L0-L8S9KRS13hrjW__469OzrsPJj7ebH8OuU99OkRp1xUaiV7OYaSWFa1huhtKPuC0ylRHS3TV4JPxMK0PlgBCNZbynGdXdHqxK0QMaGZxxVOL0bLydBjxkVtatmXdfav7e2VfJ_GnFQJBCtIhxcEjF_WPC9bSSmw09DeJGg71_X8A2mfihUABu346C7g4oTN_vFrISPVPpBjxSZmjgO57KXEsupX8ZQwQoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTR9zByjpfz7NQBnCUeYYVkTU2j229qJ4nc8wYFVZbCH-g0PrJaD8-EFfLbIorp83dRVmqWHBd3Joz09tUv244W2dpxTTwltXu3Z7IRolB87V84Aj5oEDrsggGUQKZibTLdVn3TQA5-bkTEesTSVRsXPV1v6LH-tGU6TELiw5U-KtotVhPO6gNpf8N9wuqiywGH7BvLjji9dbyDvonr-C7KPw53Zwkz3cTeagCXedxf3A1-SdwZo16KpwlqxOSGyl7d9sg9_T7oCAjJggp8U2Bwl63b8A--X0jgGxwKyOKGXlTqlZE4KU7gVYbzG2-V-uEjustvGitdthCXGu32uAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDGI-H1CSoMuDCl1wGvrbdcd6Mao5AkH4UkaPdPLjUOlLkm980I3IiFrxSA3OI__y_8vYV3jG4_fAnlwLwEZVEqoRca97gi0XSn8wm7l73kTvY-1YA6e4wWNi75_EiI_vEeB9MEIWm2vRbprsUFcjiT_j6Cy7j1o743cC4mGsw-QEv51G_sDzqF7qsoJH5jaGuQGiZva684ue9fgonBfB6Ll2FYGqQY2R9Axw17RtrfNR4I-gCVSAkpHc0cg_3mo01xmLM6SgeXxwRougTXTXHc2NiFOts0ZqtNHbprDV0uy6gEPbB2RdyLujwSAK7rZlmYz4sAPePBPo5AkAYpOlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v60yYL-0O-dOu0WUNU-o_0yN3ZzaUiyHZHUbbpO5OgA4jPFsdCxCw-_slGRo4yPPAGqXOdljGx8JRsA5jKKr9DfqDEHPwFK_OSz6sfjNNM-OMMtQ6U0lU_0LSFxWsAfoJS9uGKF6YdTYSX1ipnIaxHk3orEfkSzPStO3Jen5Mvgfd3ZOG10Dn7yBZqHMkf_um6JF3_cOVYRHkGeTsFNDA81vsg3RCRwR5qR0ukR5GapJGkcan5wlz1ro9tEneNL_KcHz-NY-SIlXjMGKVc4cJVdHtzapb7A5eALW0LKHdRWuodEk4jUv8636DigP28CQ1NaXHEewiJHJoh2H1gkxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D936Vmo1T5nnnQqHCcBQZOYVSJq0UbONp4HtXpg-pZ1XUmDCAUjCrrPcO6T7X1aw1IJAyISym7Jdq16i5NxRK4OX7wGMFCJ4jO_C7gFlrI57IFlgiJPZGI6BzX3Y2Ss9qscKP0Q7LV4-I2Mzbucfei6-FS6LXvI39rGP0nPUO1ztGZjoMJLb1evIzNFDaKB3Tw-BgOeumM3Qk4JRClzPK1cvNE0tDnFMS8Y0MHYHSgeGKIFjdVegAnS1MFnW5zkZB7RloNDG3TuvQnSIdEJSz_2Txb2yv_8_aBnJDlTIUpvXs54YhkfMNMV2zPcQdSkMLfq_Pvr2oGMiY4yo1W0uww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IemI7owHlvDnZi7UOFKIPpI7VeNDHakn0RtDmPh1qCVEgNXxTCkela4nCLEN3s3v_s1Ds1sh8KjuEl8LDcMyaSLm0zIASf0fGzUxYv16TsZ_CcWC82PKNFTE4YIyBkQ__-7FjJFvmbj38rBWR0lQ6At4KqAhw4DQypNDn8iKX3s0-CPwDRfgNC4rV0gfssWdlD9Y7EgOlxt6l23-O8-CNX7hHnCyo-npVsIoOTcUrUlg8qjR_Y7pBl5X4j4bwfWdVPWaAVQ5A4QLrf9TFAX9P1u1e7jK3HIXGCpgULI2Ti6SR2n2688KH78vMI0s4rlAj7IAwFPhsQGgnBXfPMQzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVbcLv7SOpsDvvoe5oY5EK4Nclu7hIpyKZHPPuYe9J7gQRWrQqLCgN82M4pTcBLYI62ZDTNlAwWsk1xF1GjO5c6QYSASbISvhCns7EETG-hoEPkCYi_DZufrrd_cQkP5DTbwVC_wNasbaQom6TrBsn06oDLUn5Xz2_6VdfQXcX8bq9cRyzi2AgcnqKKSZfPPnHnouSP86Jnb6DGVdKveK_VDdsY0lZwbEFbaPmDqugFAmDey9eBGu6-ktFRniOixSXUr5zAvzqn9-XHisSbWl-d6cC_nJ6wRdfB3Z6SLdL_8AWdo6_ByjUBzse99WXnk8CTsWjk5OrtCmQoUUu5Pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKQvntl20nE6h97qqexfRh_kVo8soO2i32PtUq0ORaOOj-aqWUiLbeBufNH0UstsuWtB6u6sJglQpZ0T0BCLOTNEfmjX3mkp7zCBxyCinKmkrCPwDPZPQCYtssNQScdN21_XOijC2kB5q5l3_ds2_kCzz1uG19bhvHmOuKuEjmU0YCyQHVONG5-bbKHWfwJ2iWFkZkpa3djzcVCMb55ebPrIT7r1P5WJb0vLNr1Ui5OOJ8pETfok91cRiIc4Awl7kGvKhuKtwdXtFoAd57EUm1D5jEjw5iH-n0_0LV8ScmuCz35g22E1lbd_bh3l6NKsGFpfAjvwNeRak7pu6dBiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg9qW4y48huyUN-ZArffxVdgSnn9wuignLEHWtHxdiiHbE2x66SNZG76cJjpSUcnCxbgLIxnuR3MhjpPAjN05uZXcyt8Poz524886969VM6fbuWxc3-B-K1kEsEPAoLdii5olDJELwcT--0Sxu-rfjiTKC2uZSL1gxXbbchRxtor9joSsi4WGSvuRdFnHFyrx2rbLyICcetAiPZmHE83L-82wNmuT6JgYNpjOBv0RqDGFGsWSS9wjzA4wltSfiohy5EQtuoyqEjDYhR5xxu5FTfSuAkDLekkEBlv4ksmDO1WoHawE5Lv1JvJbpP9grTdHSCiB4k8JZDIdqvNcAn9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9vWlh-NiJ2V27d4voq-TIV8USRY8QHvvr5tiZEy5dMpixhF8NSJ4hHO1BQsppvAIB-rL3Ch7dIKtNZuAy65og9jAcKlQYXH6dc1VggZmIhBfhwxIV7cCg_SFRs-uOC76BhpZULA1bLk1iR8PssgGqE6EIl1DEJUi31zS0yewB8LSTsMAt1SKwwzJwcB1zOGdiLR_Q_VpOL1bvtV5Dv2Zyr3qgk6ZAtJoUmH4KB_fmwfBELBIIDoO1ecDX3SMUl0xIb2f-cVicebEcY2xybu8rpG_jzQ6WltvphiQD-_xQnHQeiYu4jNOjpx3vmL8lkZg3XbkZgW0hhIROcVvu_moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kR75JIKLJGEKY-oriwEAMxYnotvvBudN246Rd6VQDKRFqpXG4y51NaCnPE00-6LZZ4EHYqOF-dED6oHl2gSbWyQL5DTeIxYbtGjzQ8QFp-PMszC5s4vY7OBgeDesuN3snPQcjSiu2fJc_6mADNhHGdYVwvQ7PTS4us8QtrZffEFEFMdKv8lVFbdAyuipuT14skjaXaSdFDbzII8eZHPvUe79ftObph_HxlXLnnV4LF2Lmf0g4X0E48OKLutPMvunz0U3W7_GWqUe0xhwrHLS9zFzoGAX5wSPVfvu9aE79GbjcagykGxMzje0dgFaw4UtE7nkX6s_5LMSTBGg_UQgIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XK_C7SJ42JghW3K9nKUU6W2JNHNXc28e6eiUjYvzrnFlzTv8W_EmwIlOg5x6EkNnFKplNEsG3NytwtQ0a09Xo_IMEdRZvf7RlawfJlJbyrLzDyyRwCdDunuZedVdRW5aIJtx8N70FSdkuct5oh6xB3zKgxHFMHRJWSBO7kVhmKGNo0aKOlgW6yXqng7e2y1y0awYwF5HIDbhechF0xn83UGM6WjE804kIL4JoBAF99ZQokcugGlHXXI6D_gaM2O8gyeYmbI3wG3KVCj4p8DsawNQ3qpVQYjkgBcMt2DJWFLgV0PwViBugvoa9BzX_g6zVCKUJ40xMOyVht40DpWbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhkbiOw9m7eerNfQ0ppZO6njGOQfamfIH8tHbT7YO-DK0UdAWIsA4Df2Woezi4q1WtgxVmXSNQpCVJsR0sbGNbjPMVv9WoCdEcB85p-zYAcFZ5th-MNJBwfRAkmCnOPGDJDIxA5PkFrFQ7kr7_efyl_yME5VMX0NTgnWdMDj1R4GjCDpyTC1gvqtJNQeAtFlrRG91w9ZR-za0is3jTBLdIfLSBo3DCUOeotpc3yQgiuMDodvo9BfCYWIqlllNbOABV1vlMWPPn6OOVW2DgmtjIt_beMpH5O9yrxfvkNW_FOP__PkHiq-jW-otP0887OS8wzqr_SlA7_dZYaxXvJHJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z64h6LzPrN5K_ZnaLf-iz3CVQWJPlfUMm7Xn1tYS3b2yygTPHINiTfX5fhdw4X12rqwIg89khtyKItFCG1Q-b5d1fJBaplxfGikfCWA6eN24bSwxCfxnR1Tg4OR1WLR7cjPdN_JIy8IkKgxv4a3LhfGuGIHAhaTkVe63IbWJpfdOdlfwGR_5JwOl3DT6csRtNBOVaIzACvyf_bU3wTY0l_xXpOtUXy-g1rVkcBxy_dA2Q34fMcl8MfNA9jP7ZOI6t2fVigFhsCn1nVHwq5yfpqb0SufYyFGemUL1iC9GdSmHVeIbdaCCb_oXQzyeKhcI1FJNqU5DzU36fnuD8-ujJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4BD5SMuyOXvCBDz5pHnLylelfjqNpPx3pHSDtE7bxbmKomhwZ_r1Ca8L9Nih4MY_9HUyba936v0-vdU_pY9b8zR7JnLxRSJ_lcYbaYpkSbiAaPHZBB2Hd-BY2kCBObgIcBFxwQBv358tOkiMiB_9uYMB34TrEb_Jmr9qPdMIejx_yC8llmrNT7AVGUYfb0dqNLANt8SWvl6JLZn2P7fDrI51R44ynj475S7pdFwAMAdDwtbmwsg4UtI6EP9a0eGdZF-sy-jlGpUVGaM-ZxxOPF_AvqXW-Luby0A830FU3oWQePawu25obDxqc4m0ZsMjb9No6HAwGVx1UEYSEJuhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibEuigihRvhLCQxhPRDehoPXRjq-obi7S8bq0JH4H5Q9R9zydnOk6kLwPKI2r4-Izzf-IFN-KkbbPNATAX4skHnpFUCN4EDQpJJkDNuIwjJLs7XmNp1X14SK-SUnahwMQb6p_VEVzx0PR5aOi-DXgAuINp6iAZzvk_H5EiSEZsNGTOvcPhvBgw7EUSx9ph3PRV9eUBUjghJvn1IjuSe_GHlwTMqiIe7Cf9umDmOaepDzn-_MkMiYDjFRxMRkwsXph4X6D8KWWOvpykYYRZw5OB1sKRLjy3naAa3r5vC1N9WMr4k2CWvyVeF82C8Lr97lCGQMWFQ1Q7ME7NRSDKtsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZfYEeYGQBg0elc9o8lfkjTC3Kbr0ob-Fyhtmd1Edu0VCE7R73FVuV6A-phRm1s4Jghfa9eurW-hiQk0fCcSIfsxNIQvQHCcGPSMFYKt2yyyOf3eHsEVm4JYFgA0M0kcP_2oBx441s7Lh5VYIAotTCFyRpErk0rPXk8mtPEU6eW_V62G1JVvSpWVlJHDY1-sMPAusSm8QfLBEwVmVigRF_idy-aJ1OIcFglmsnyrE9hfK8S9Q49TRYzRqqd6ZHFXNyc0OZBe1c9Tfsm5QBxKP5h4j9jgD-lvhG2SmngDTI_nG8rwvP-lzCkzbjQoEp1xzZOjhnVIj2ZRmCkiCKS9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=W-VOODP3V9mY26BUouzn1Jb_H2JYjRgH39XOITggCzrLM_to1ux-vBnSQ-EzFXLOTi2NnQDKdAvcSACc2-6KjhVJ-q89Xp6hzxRB5ULRvhSRZzn__50CACt8xUmID9dz4JRqgDWVxVMsiaP1WHoz4_q65qKw99PT07A6TVdmmwgQN_KaZwSwfI0o1Lz1OqIE2bihEwfNjoR9laltv2k2Xj4PkS1bQtcyeNjq3ZuZan_f7xsJ-B6vAVvqngJtg1wCBJG8c1-kTlOezXkUlpokBQJ8WlAGc3NA6M53Qy1x3Q6rOAFP-lZZ5JBFmFJNydpnkBWT5yIfXib0JaxLicMeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=W-VOODP3V9mY26BUouzn1Jb_H2JYjRgH39XOITggCzrLM_to1ux-vBnSQ-EzFXLOTi2NnQDKdAvcSACc2-6KjhVJ-q89Xp6hzxRB5ULRvhSRZzn__50CACt8xUmID9dz4JRqgDWVxVMsiaP1WHoz4_q65qKw99PT07A6TVdmmwgQN_KaZwSwfI0o1Lz1OqIE2bihEwfNjoR9laltv2k2Xj4PkS1bQtcyeNjq3ZuZan_f7xsJ-B6vAVvqngJtg1wCBJG8c1-kTlOezXkUlpokBQJ8WlAGc3NA6M53Qy1x3Q6rOAFP-lZZ5JBFmFJNydpnkBWT5yIfXib0JaxLicMeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=D777osqJN6zK0EsQw_84wpt055GCRx07TjXRns3HfOUVh-InpdOwNorukSQfYilb5yTdqK9YjCznUOIKidZjqNHsw-PTvr2fnL7Q4WnQrSnLDLgMR7W4UU-KtwgM_RPgdcMVG0n-arDqlZgwTMpgZuCz7-YvthbckVfb2gBCLt_ctou50sV8u9tg54lOLRpgO9gflEOJWc_bLDXdrwGwwGdF1dY2Cxm5-hDQ8mP_37X8JzCVuT1-kfBy6oRInx43-8HA9RkqwCD7Opu82CuHx6bID2f1f0CYxsKZvnyx8whIEzp85Po9kRs1xKPi1VwSJjjnqE7X5SRHg_HJN4UHyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=D777osqJN6zK0EsQw_84wpt055GCRx07TjXRns3HfOUVh-InpdOwNorukSQfYilb5yTdqK9YjCznUOIKidZjqNHsw-PTvr2fnL7Q4WnQrSnLDLgMR7W4UU-KtwgM_RPgdcMVG0n-arDqlZgwTMpgZuCz7-YvthbckVfb2gBCLt_ctou50sV8u9tg54lOLRpgO9gflEOJWc_bLDXdrwGwwGdF1dY2Cxm5-hDQ8mP_37X8JzCVuT1-kfBy6oRInx43-8HA9RkqwCD7Opu82CuHx6bID2f1f0CYxsKZvnyx8whIEzp85Po9kRs1xKPi1VwSJjjnqE7X5SRHg_HJN4UHyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLrJEKyUqnlXFwLaWnxHWfFAnk8WTcRsNKjAMLgHDP4uX3U4A6KrGgZ4XcT2iw0I0anj06Gh15-9Fe0GEbgBG8YHvMKYCUsx0xSEMlGrgCmMaZk5SNwN2N1L93Dg7nulG26-JI3B5bH1-zib53cOm9XoDcBHAtjExaxPhoksBm5QMbMMT5cwMUq7JjdzdVsT6__6v3XLoXZbqC8ngmO0efp16UVy2qRXaOXSu8O2YgxlKMMf2xJht9d1rEG7UnrRaj1fHXUI3xOJiJtzLKfrXLEaoxc-tj20qfbM2kxJe3pMFUAKBe9WDt8H3bY1MMv7lTBEm8KjbYPkdXFyV3tX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUwkyoQWyBOMd8Ai9ZqiEJSuaZNEdxnQZF20b8MRXCobImub4x_20tVFQ5CuozL3Qn3UrMPnnEj3Rs-KYc71wsnFbB1bXyXmLw7GB84s9Jod7I1u44DcyFWzNERqKuM0JlgddyzEbXcJh117hlnXBBFKxMi9uUNQUkNprxpYTLAQhGRWqRuN2RUzJ1xAFxfC7uSTYN9BvkHhHAoZlV8xtHFqUff9wW6pJhhSn7Ifm44yK45sqr_0hQvdzud87ItaAwdeHgQLY8LhNnrjatARIZTXO-gFxlKv5B7y1ar8RYVJo9RVPAVhZ_B7KnVhHcpsJBj2RGgg8JKia0bS-M2xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaalwxmjwLUgulnbliAE64iL9T_kBEzHBSU8Pww0rQQLBSCPmHTQZhZ-b7tGR9pq6XTvdNVN_zDMAgXXOKaJzVG06cSWsPubl2Ng94GRwEFANDJmOrvqbI9lSb1y_0Rve22OXjfKuKn6nsE1HjkElW-8KIywaPrYgJzv9uP4edV7qX299aykj-AQR27B3dpyZHp5E21D2zr4aIvnBaKbKiNLsHLTKD43E6m4TAWvepUqHYMMKTLQNbck79eoKlNGIPMoYEcWbyRdv0wUFwHWjZUd0nAvu0_F_HRrgC_5zGjmj3OqG_bD4m07tTyRGVI0eHTe5tG4wwlzxcl59eDNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvFXX_DLD4dwR2y_IPNNfViZbH7i_bSRRnJ8fXS5pOAdE8NLZGmz7uwPf35Xdn-U0pFjgJWLlv7GsKwrnu1X5aH838w-G_heZFMU0RRV5M4HxCsA9AJLLrW4tmVpRV1NAEWGn8XGCUdQgB9D2_co9Ix2UQTG-EwwZvtO3BsTNcAjN6JHk2mru8rRDuUn4mPMh5jvI5689Iqnbz-MaanWrncDmwxV8tWHZ97cYIQtCGaFM9Sx_T_P9PmDhiPxAjCQ_fy0Lkcepxgkp-T1uUDVeM5isngHll_iHlCrcqU1CQY57Ok9nbu8PGgv_POoWKVHKk6hK39CbITRE4rcdaxfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q97QrRXkXY4h3mZ0iIGM_1AazpiUB5H7JvZN3DF2xxQJX4Vdpb3iS37stLlFZCj8wmhBa4f1cI_imTI7ZHDfUlXblB2RzdWentwQX0R6yK7ohFlRRR9IzXgH3BZXXuI5H988tYiWltVXyqXbImFx83rBcv4ihhlRNN0_G5RtNiRYBzMhOAg1_xwPUvVgSJeevhpIDvw8lI4j6TKKqWDLHUOo5PkjM5s8VprENglBzI3fBhfp3mZb2hqMHRj7VfYI5Z5obDj6rTj0jtIVyZ_G3g7BgiCtI47A7dbfnrea1xSEbVbsY0yalMi5tDxd_rU7URlS5bSP2udBMKt8tZ9r_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQa5S-MpkW4vpR6_N6E4gp7EvwKbd91L-TunAByCB_UTagG96GVvdGCOn_3t1ejTDSU1TWu4_A1M4zY6MHZPgBcsNCD1dY5r_ncU2TLnt7MnkfQSdLqIKSuUxeYBSLHda63gxKpXiOr9KoBKZWgjVOWLhzoeksr6fu4PeM96nG-p4vKfE9eCXr2mefayLC6x4ANTwcfgxOdaR-unSIYE4X0nu4MlrmQ02tSQhd5eXUlncWJOT_ngnewdqyUYe3p4dNQsp96Psy1NYZJhtO9QnVKVe-4rTDzuv5381_JGmVzB4tQc_fD_hSFIhLGPeVps98KAjMiSB_MNvbuZ257bRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzRXXBdgPZEJVSjpznmHiawO0IIXaWJWP1SQfm3yNhxMmFv4xaBhmfXq0nEYqkQrVxqjRt1t9dTd7D9SSMUSxP1pnOp8Q0mOh-JVqfY4C-dmzSl7pJp9jHp6URgmcdCbX97hVPJHM9ftw3lsxuNzZCv3qhGsV8gW6cK8JXXsxuhsbah5dFYkmNoN3xdUbILZr41QSHA14gF9ETTn5qBBj268gYFTTCHN86KJ62V3PbyoSVFdbM_0hp-3sOmo5DRn7IxxDRpDh3nIX9OHwl8UuWv0xy6BlIAJKI2zCGiHTrYOom8lWxNKUyXIc4Isl10ydSobjJmcg2cFVgebQaZc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaFqXOLJ7zWvf9q-R67XS3NN4UH5kyLHjVMZZ0eWO1tyiNwkVlNSLHzoegOPxCr1HGNzLt1_HnFAEmw8njpTR1Afigk4N1TZl_AF7T_-hYRpcyfNjNHKiNz-VrrsGPS-1gQvGB_0iZyBaaOMZKXSwQ4l86LByKxDT3yY6zyBE3S_EtNkTadTr2xfde8y-c_4aZz7H6Wbe1boup8lEOvf9rSMzQW472WKTTlO7-ytNs3MYpchMbiZqaSzoHrsJrzADpwZ1XhrSjs_ZFJ_eI-0UKtFxQTwfjWG1ghbz3WymH7rhMZECIius5d56ygiRCDnuHCrE9J9UlmrxaauPPGdAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmgSwTLwbcng3XURwAxyWgOyBAOokZyr0UPPnvpk7gIG6GrpIK2jUeAbmaR_c5TZTn_vFoDKmizB29JqiZmqVllbwtqqUxNCkgUXVBbo--Hi-q61dwurYicxLlbPq0P1HaMK9lt11ZztgkGhqgxLy4_vy0GZ99ODSe89DwLgyVJDcYydg9JPY3ZhPAZ4K3yY85Yx8cfrh_iJW16t0BkwA34v14tAVDYerMBWovlnWS9H35YXRfWMkaIl9AdXKvr15xQIG1TaVY1c6vg755NVz6vnq2Jy_ZCSyC4_6P_4iuiH9wtiKJcPSKwwSOygl2xmxxugD9LSjt-UODi04WwOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-Qq_vqmEhDrypt35rjJFW-zBNwwpYXc6uaImze8ZXXGiZQTLYTjgcWNARGjKi9nlA_vCWDMy9fe-ZWMLTKQI__utJ8JvmiCW385E462s_Voe0-HqnPUT0chKuyi0NJYvlJ0pei-aIrLhz_igEw3U8UjL176j7ZURujwl2sM8OWoEDSIxpJCneTpLpMChM-3zUhsgxCuHG__whwCHkiZwSaKHgxcP-haSBEM1eUpFlO8WlDgS9MlJ8aFcG6lEtJlZ3Uoh95DUSzVPpzUwn8P8D0VpLcH8m3fbfBcygAf_PP4AMltajq-sZ6Q_G4h9r81sn_TzuOGAnVJWnvDWKvwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXs37_hMcwP-AAEjSYKe2WYfbHSNCSGQVsH798GsCMuOPn9qpZbodZCQYhsYKsoU5BMeuoNrjsR1DaIejflvdHvTlLEw3tZ55Bc0zK6y7MfOTkEYA4iUzVv27d5BwRuxxedEexIvG9LTWB9phrSegPpGrXzW21kU-oykea0Bt3X-GzYTP-eMleztVn6we9wobioxKg4fOb-mj74gEilYSq9REMv_nJAXGPS24Kao2ckQnWGRgiG9Gm6g4Put1qy3nuo9zWXaFLt6IKMbMNub2Lv2LpR5-KlgCJMGilQQmL96jYQM_3ouJfYl-1U7k3ucI6NXqNHeKamv-o1Wgqbcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5xq44KfpoCUQAkxSt8MY_lGsFQDcjUXe2ZrChiN6T2nR8Wlkv1vAChIZe-BfU6HKItAhgitnhdmWVawSK475a4CNmxnUgfT_9l0b9WTQQsdSV5WKPYvX63c3sXMiN_NrynPjj9UlITavi8oU0sq5J12DpgazUuM-rUNIM-P59zi5n0acBgNBuRurk36pF_hrvx4L6LqSd5tal4koVVvsNFDyUi3cSvZP1zOWozHQiMgxgUU6nMoDjztH7KLaV5IKgZGSQnvWG-mE8LODNf8n9Bw7pvtiLy8vxAGqrIG_hFUAp-uMTHSWlFtrnfO08ifuJ3bh7TbyhMWPEblWuguLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSKuRNJsGTyCi9dMmFCRdOBKWrvKQZtm3bsAt6Ha4g4teN0VtP6FZXBUUSMtlSw1SvUUX2rTWxgJwR6UeQvD9vtfmuLduZJLbO96itoimefDKK9hr84fx6cdoslkvJ9RJbYCL9gStIYYFvBg6uS9qcc4Wzr-K5MvC4uVYTUNbpk-DifeI2XPh-3Km2Uoga1k_DGF_lBbODEAoQm6TKIqYv7K6uV0HO7K4CIQRsawroHbOni6mNdWbTwYjcMEwsM9O5L8fU1HSzGFHvBpgMV7iqgyOBG24ZdlEEkMeJQY6qhn0cF3KrWYuCUSpJwcBVb1Vu9_TVl2_DNKId4v0spNXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3c-eEcrzciWspcBRG_RZZmRB5lg1tcvYFFZA8hhA4EaiRfIdUVwqbBNq5pUJLhEUHHa2NQ5QEGiUEnkgo4IBiQXvS8SpIInEYOkaXV-pyvPnseFtyc_5t2w_2HqKnaTwzWObSZ7MQJrgH7sILqpg4IsL1-YhurvAJ0YaIcd72BNpWdChAqJRO4j1wj7M_2aDcHfSukf1o6-5_nXl-8An1dV2EiZPyKeD6VEU5u48h8vjsrbbxdVrZSnyvLzPR7SYmYG3cfPhe5tQdMhf2Yc8L3ZB4zvyWV9ikzU6ZiyWSoCIbfJW8Vc6-XL9wS5LtYCy6YiSfaOFNMZ5I5GVD5SiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxFstElK5OGcB2YnJ_lW-KXJab9lf63F0tHjONmsEc9Fibv_7vINFDXnSD55gFBAlnY0kcq_e_tb1oZETvWibJA0O2iyV7iFlAKRk4cOI_lqN4AB2uPWp7lE8sKQMQQFnp-kofj7NdlRpf3I-QMQ9djXW6UqISoUqmpWWVDLHwHKioce03fZ2FLf6wYDmY_faGDQRWE4aCPROmUCy1u1NF1DT3M5kCMxjvgVXyuaC2f8M7HKp5RvVbWLQVaB30_592mS_IwrHct09asgdaL728kvzCIaPBxRZvKwl66Tv7GiKigB7iQls9BpLax_anbdTTcJigyY7BWsfq7DwLo1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpqzBXU0-eECqP9L8bijibGJVY6Zf_Lx1UN8eCbhTH0ZXk5hlNP5kwhMdPKDWcsEaq2_XGlf9GLStiVyu9t1GfaKBraV_3dz8FhpDJxFP8-4N3LN-jehWP6iRC2D8o5XsSNvn_RjoP45z24Re33DyLuFvneIGsO21349Gn6IP4A5i2lLV3gQb4y7MUkCO4UUp0Q3OKpckAkRht2RoCp2D-SI9dBi5XfuBJPl820SMymdJ97aLXqNAkXAHgDB9d4CdL0bKIVHfudYqtBqSf2SA59TF3LWQrV-sAJQTyUNnk1getpPGj8tmmEkezrNuR4i1kFDV2Ipdg3v0QBea1fheA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwqF76q_mbdRkg2ekfaMsMdBS2UxvuzxZKvBXq2df__ys00Xz-WoY-xUJycU74ShS_NtVnxHq4KwMtHy89e1pOqmqm-43u-1jQmKhNxTHXGoIPzsUbDoC34xHdDHNGGb1htPtSdZVF3htLmbngK9pH1Lo0xzA-9vD5j5g9G0SY4RoI0EE4wt0ogLS8r9uj9uhU6CnOAqbBqXObbbNlySFT5qCRaohfbxzR4zm8MpHDDgsK7x6PK9i8hllN-4bAWnm0O-lXDYhCAWmvAknoc3pgv40yddLX9c3Bzdpeyr71ckXrHVncsB6V2EivIOWOpmjHczVh2DXSmlGg9Na8qI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIbEGlHedb3DrjUQZSM_TFp7C1BOQspDb5mH7v5vItQ-0zUkkvCegg6vATkzQYAy5fUu2fSHkkqCAtXYk7MDD3cOL3MHUuVQP62y_qTqbEPIQhx3f48xu26gR9QlX_F6BHBTsg3JJ4ENhpuu8rlD_uJ38B3T5aDtuoPCocBt3Ew0aVJEdSFz2faPWByrOexhkaciteRzih0BnQwWHyIz0yID3w78hEw7GAN0rvyqM-s-lKX6513TpGXYMCTC-2eg3lAzwho5H3sshV_NFnTkm_HRsb-_1V40Kv5kMnvDj5no7RozK1hONYvztqOyJgreS_Ma-JKrRXsHh92dC8_EtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLD0H0nLhiTNacyHnVn-ChJ-mLE6uivh6e6jDcIomYswbdUvrjJLZ2gH0WFf1rqZNcZ41McNDx2zOj6nbigwhXHe2b9RhO2sHvRLcBWKG832LMOKJc6zl-mgXu-d5oGdvWRBmvRD3Fy5hliyakfjXm3iZXjrLY0OB-5Wl9Jb2mnV0PzQYq0zj_8DqlHHmYbviP_rE5c8f_6Sokf-T_w_57K1Ystz9-CuoEiNvGaL5xJpWHbuZt0-LLfe9ZwVO_1REanveiDG6UxUzp1dasxxpUCSPF63FRjoPMQAYRC4u0fUezCjPaQb4_AxTBYDtPYQTcoinmYsABCfk3SVagK8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfcnvzeMMWWGguyeIRdWn9vTWQYhHV6FCKhOEUbopKtayMTDyP2sHTEPzoX4UWkJh-kUmJNL0R6mdKYb5EZ0rlB5_5a7YT-OHpybvhECWpaTC33ywMkLpNFbDaMzSBPdwbnQbiGLhor8M4k2-Lo1pxATNQ7SLI2dVrDWpSQRm8W34_LzwxNZyoFTT8EpZmfEGFynKY4PUWOFKu9NdpjkP3N6acyUfADlRHkDBut0cHTcU0_HzzQ6MHYzljCfh481dQwTRgoNqzwy8gwODFdXT-2Ce7bHpF4ugcp3tSJV5uUX-rRASe5Q5e9UqteTb73d8sPpPrLL1hJPg_OHMrlnFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=Z7njOvr1lWnIVptdq9jy-wrYQniWLmyHDNlZnl82pfz5oNk--9v6KJhPlqaBv5XwTxDBQk79h9642LDKZcrfTS3OyKtbJ_rsaTXjk7PBRmql11hqBPmlm83f6kfF4r9RHvNZoYcZtPpcmRiPiSQycrvK1q2Doc_9SK9gw1EPZGsnEZebtTlRR9w1LcWNjtUtKbusMd3DsFVlJe0fzLi5mhi8KWUH-llWgYIQeYI8fn0fR4P7xQOprnqpkeO5eUg50dhZ60UmfZiihUFKf0zeQJNQi9_06vlB6L2kibIhVulk7P48u09ifd_RDrxOBRymrfFhO1oSDSc7bQDRDbLgow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=Z7njOvr1lWnIVptdq9jy-wrYQniWLmyHDNlZnl82pfz5oNk--9v6KJhPlqaBv5XwTxDBQk79h9642LDKZcrfTS3OyKtbJ_rsaTXjk7PBRmql11hqBPmlm83f6kfF4r9RHvNZoYcZtPpcmRiPiSQycrvK1q2Doc_9SK9gw1EPZGsnEZebtTlRR9w1LcWNjtUtKbusMd3DsFVlJe0fzLi5mhi8KWUH-llWgYIQeYI8fn0fR4P7xQOprnqpkeO5eUg50dhZ60UmfZiihUFKf0zeQJNQi9_06vlB6L2kibIhVulk7P48u09ifd_RDrxOBRymrfFhO1oSDSc7bQDRDbLgow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewQ8Q3qCOQi1WVi2GlaaobOLq6ae55PQB8KhX7pZhODVKIC20gIUtvTpUKVI9zsIh9UiDuapqoGcXaaYDfVOjjWTc7nnntrsx4yaj3zgNLWzKUkhBupT8FM8RMWFSVrCQSr8pg9Xh4p8T5SsVqAbvSPVG7zu1zWv_9Nut4E0hS0YdUEcFQixbM9ERscKhqP1GOmETSZo8CGWCtFq2w7Vaevd172eTdCalJYBGcs2fGE9dVmEHYEoMpt_6yXFczH4GVggPpXIR-2qUz-lInazPbWYF1DieKA8ebNtoZTJ1SGLCs1mo1KQAI95Ij1EHzYd_CFyJ4fowDwEkRtoa0Db3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBlMisIPO-_8OKwbjNJQrITmlULVh5NrNNLMOF43VgkUpzow5Btx7USj2OoS7g4Q2nA7UQYW2e_2DX6KiW2Wr3R1niDiLzO5_LSN7Sqv0yDMnq03j-a3PemPtdgDUF_5cG03up0RwX9NRDxjh3OWyRmnh9wgheGR6eV8HJK3KY1VkKfwCwQkEMuxjA0M7R0ErhC-cTBD6pmVyWbHC7bkQa0DfBn9KptCwx77C5ns6xTVludc7M4xXabJQPZMU7-o9E6rjJ833ffTgv3CuF5LaYQyD0xZlzcY1ihFSRubWPjrSfCkNAI-DTuqlcUDVXBXrQC6VcWjTualKVDkdGth3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHo819s7hMXebMluHEh50UyadS6QVG1k4ZZKc2Src_OXHoNJmcFloS7DMim-rXI_lEU7WwIlMPquFxVjpQpFm_k6U8WvOV8U2jXMgtspeYNXCHCeLfKeMYWDFuWpFumbrCg2HmyShAbR8c5_AUfQF2Q5EdrX7H-2CcdWUGvoOB98AaosfXFuSps7POMQKkd9fzH1NND8FA3T_lwEFwVm17GK20OWKl2oIvR0urMz_qVeKPZUsK32ZQ9SPx4Y9jFMH_4acWu_Q6Wx9Mng53FhZBPWkgQJYrTfVdVGJgaOIC0GJQH9XfJriaNHqJolIYem6ezz0E54a779wO4DHuf34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Whwxl37Y7PsOId8KRnBzfsNVHGPuQXy9mwm0ZqAy2t62eMnTx9hfTYGQQuga6SJnjzl46XkNG-joOM1Bp_YmNPDpNu-RImP5gXZ0_PqrN8jaBAiGy-FkSy4gpeM_qjiQYsuO1ZQCSLSSuSUfoymSqf72UFKYTQHl76F48TdBL2r7f3xFqCVIRVWtvP15IJ37YpzRym2MM0IgLW-e4SJkBKXbQOupiXvy8f3GF_wdq2o7DrjNLD1lRAhtncOI-rWmAHcikFXZwKfhnZ_tft22VOpGN2R_y0ig1i_QcQLoI5giKgY0R1rXTlrhaDu5Nk8HofnaDP9veeU7B_fJ9N1zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFjTRQbwxq-PSZBK_9iAcO83YT5auvGfAb9mzxuesPHKFz960uBxfjMYGg_H8kn6CWe5TGDQmhIRpCUbnRWwT_D3r9F16PEnmVGtUVzL9VTZdw1MOns2rk0P8otilVcpSpcSS2nuCqxiM3hIiumLpTZIXM9lGMWr5LKZgdF23RD7Pqw0bJMlOEQenEJDXeGvs1ubY9iOZa0eUD5pMWYBg9fXMhSIKjHlf9RuKGDpUhwtXQYBghLU9vhXBUz-Al6bmZYHFhxzduqIm4ji5SWO4UyQMN-gsC8aWdhtY5aBuHPRJJpCmaCSMyLqOWdkDugIM2jVGfHsBGlaZjdW_GWT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hkpg--EOD9eUK5fND9ADHTssP-lYIIrhsrxBGQZgsse83PXlT9u8jilJetFZsyg-MI1Z1zJ9UDOx2vM7GLQy0kei7ytsuFS1vyM9trWuA4WswAkN8V_jcw6qG_Od1vu_seFyDmrA89Y4lk99CatZlP1ttIj1f1hb4ydt07UE-zys4iDtxNNmDyLZbhanSVlJLTPljZnq0q90g2tX3oFalHwwL1tNkuejdEgYiPhLUVG98qgPmB0LTqW2xNzBP_CkYjo-vFN3oy2vXUwzPyJ1OdkxxlGKuyDPPpRuMy1ncDLtOeY4jU2SGTleVzX1PqdPF4Hc4NtxsmSAfR8fyoKGgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igUEzBse1lWQVbQkVG_I720KXnJ1R1g93KwmQQ7Mc4jq9KyioXdia_FN784UdSSI2Fi3fXnC7st6rAQKCnektnHsneb0XQ7441LVqOSC60WMqUKAzRBGkOhhilC3w5MGOoHI1KRjyetNtoTzVRHlg3MyiDJ-RJtjHPmV-1cxv74g-XkgchlY7SPdEpsrewN00li__85OaVZIgrfO1eubDPGz8nHmdjUyLg-bIV8KIFURU2U4QwKZyuDf7Wk9uEq3eA6aRNX9rcIU3iwlDHBoRjn1zbmjxDgnh1IACGpdGqFchN5n89wOzdxkRuPBqAP-dCRj800BvMqnyIr2f6IF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDQ3vkNlOvglyLOHVYbWUOh-WQ41r80K_MGVs7egolD9TIUdVP4iP3s-gz-Rtuwxyjvcbo6RaGzK1XX_L4AaTVBOCr8-9DiYBFckm3LrfrMxMct2NlpS6jNf4egUi6hmjbTfC7y7NOc_otSn5_JIo_671LuC9Z37zNOvNU08LmRVpJF1xqHQKEPtZT9cwr-wOHnBGn5qEv67jMqyg7vfy0VTx05-qKKOmWVXlfPG3EskAjNEVmOXBTjhx2POJmwhf5OP334NxX7tOjn0In9SGnchmMR-SCIce8dWc9mPX4Iu_8rJJU2UMzi_0iCYzOqUCMnXX8RLSa7_8mzD8Utywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMAqb32VMb8Z1_MtzIgMkbiW7a4S7ejbb-o2Q2ye0bBOScD3B5N6tHDXA8KYP6mVNsnT3BWD4Dyacf8VG4Oy2BRvch18qsZ-0A8hvGMsYJDjWunLblksOvJjvG7AyeulFy2Oq70gNIpyaCtyltq33ZOY_LRnH2Ueuu1cN_i6sLS3D6zwVBw2tag1BoZq7PGhTM_4b-FrZbbjUse7qREEjWWss2pMc0EILpjde6H7WRk1hYU-xnmTgID--qXXzW52HHrFqUDKvgoPMHDvsNkfL2Hc_34LOLNkCVb7VmrhFXBLclEExK1hmqqIg_tsMNjQIN719u0fCx7-NDCFM_LYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbDX0qS6iwHjyMJbatf4Mmhlq_AC3EAEp8FfgARJHNCNRa3lrdGLPXd1EkcmMGGrncdcNl02zXD_VfthcImmashpehzQgDzmT0n0ANv6zuAL_urLG1Jt7wsrCU828XR7gS76MqaeMSiWsvJBSBy86_KCyB-VZH0A06rOdt1YHsRbjr42rwFMPQjOUPTsTVplfc7MSSK9WoSR-79mQqdc9hQMp6xhB19BAomH-JiK_EnMupi6YmkdSRQCGESYwjP1KeovBxDDsZt7wYhv6pA-1tkskhmkWZdpSb5eMs3FlaKEEp4ksvEPhzmlmotqyo_DkN30vp-QzFOHdZYaqdv8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c08W2umHA2NnUctOKfVkSws_TfliQimwWPtjopFRjGgBfAt00t3OAYtpeQoBAuOhI2coFHKKGg88mg8NKga9k9uCWcgBPBgFpu6_411rtUqYBGf2ccGkd6YGLmnOBP5ax3HlSrDlie0dQ5OguWpxbj7DYpag7FgeHf9jPdbxedYcGrDOxKzmq7ycWr8KPnMt30UzgbKk4-eZO_IO8Kx-fpzF02b0asnk7x1kigjORaGBkFIj_6PTwQE5aSMTjJUwdGiPJ6G2-3vwRvUsKN-_ZL2sNGkCkIGQd-bTRTSJjCML1SaZIRdA9gYR66eRlojOrRRS-f09VCteeQ2iPj7IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=YYKoPpab7N4gB0HEIopYyihTnMPV5nPStEjUY97Vh-BdviqKRch6MnFcnG19uI4LF2DFUdSBopbv7CgJqUdYLexcDakPSK_bWlzp7JvqEbNbyVKCi6STNFy0BKrjOvkm5iHebwLSlPnDw5sNLt4r7dd1JxY64IGfEmosO-Y2a5SBGQSu1Mx8Qast-QhAhO_L5rJ-I4LsJB2t80i17YN4ho-3ean96FL0BK4XjMlZZ6aIoD92K4ISTAOLyaGp-gGT1S6ptIzVm3VuKRL4LJAyzXbq6Huz6dwdHeFSiinyf5E2pNOMC4rxRBoC79_BdEzZqa-g5kqnRvgEOMQqmlr6qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=YYKoPpab7N4gB0HEIopYyihTnMPV5nPStEjUY97Vh-BdviqKRch6MnFcnG19uI4LF2DFUdSBopbv7CgJqUdYLexcDakPSK_bWlzp7JvqEbNbyVKCi6STNFy0BKrjOvkm5iHebwLSlPnDw5sNLt4r7dd1JxY64IGfEmosO-Y2a5SBGQSu1Mx8Qast-QhAhO_L5rJ-I4LsJB2t80i17YN4ho-3ean96FL0BK4XjMlZZ6aIoD92K4ISTAOLyaGp-gGT1S6ptIzVm3VuKRL4LJAyzXbq6Huz6dwdHeFSiinyf5E2pNOMC4rxRBoC79_BdEzZqa-g5kqnRvgEOMQqmlr6qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8AYEHZlBZSLuYw0KnPOOf8o2UFrnCbrQ2OsthNpaSWpNjyA2ifs03cAdIcY0PsE-cEWRxtIi6gIPL1w7nmIQJ3FG9mmBog2HLTab6ApFlp2POHetP5V1bVrB74zTdUOZprHhsfyA6OVb8OOgjzlVF8tqlctu6-prD5sZxLiSXZaBqdj3WIef_e2ZqiAmi8gs2rdAj8Cig-4KWVNtvkqTl_oHEnkGS9LRuRGMAOMtfzA9NxgX9n0pqlnD3UYTroI1fOKoNpGvdwx1maT3xqlqGeVtndihQ5vhBV-EXtthfn2cX8x_kS8q_UavwEgyLgQvzuKyQyOHgv0vy0G9yRH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss5gZZg0NAuNETXfjtu67-qSo69qD4JRAKTYKIbm-ypL36kVoDKYa4iDX0Kq-z6QtDjxXuzqABQVD2fNa48DlnJDQlVu8cRS7XM7nHK0IpuImrTlaBMsfSnzlkpwncs4tU8CqRYDAHBIIuLysEUbqLtIbE1qUj8d2fk8kznWarYk5BIjP13FMjWhwvyQ1gnJLoP0ka_A3REDxWQ9VLlfQzphoK53CnVJubiqYZZ1oeah0Ua7u2kvYNLIj0c2gf3nZXoo3CsCKdbkDh_xmNnFQZA8-rV6Vv07ujHozWN2QMaluOQ-gx3L_GjKQ4jqKZBIn_98x3aavnmpVx7qv5qhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffU8zKuBJV7VlwgmyACsQ0BdpOp2aIvr8_b7nJX9mSTP10cQfP-uqnUu-fqirthfHOKON_rxFsJyzLq5f3T-dC8Hc8RPJ6UOyDXvz1QBkfgNmifvDvoyWCxdN_-srJGicu16G_RVZGWWoH8-lKiAazsoLfz6h3J0zQ3VW0y5mVI4-CFDZuZGZgOmHkgu84WX8KQgRdm86g9EorWUavcfyWzkg5MaGpMY1UD9sp3enJm2X5NuQMflatZtnU9NonQu0Gl7ofR0S3nwv3regnBxaCBuuthQCNCTgDWcnOiKNdWaj_qgNMCEh07RSabqUS0o1hODWzjmxDZdu4yvIi-OZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am7x4vEJAIlMxxuI20iqXgxo-Cqbgz1CQTI-bPvx0_cgnLZvseqCuV0lXMZjoTqW90zRSMfZM1iapKIgcHQdY8NEzwNtL75PXQoJ-eGShP-fPxAsOlJBWxD2fMqL9-VSthNbMpg472UMCj1Vhs-oJptjOAd67O2r2maEyZ6wG1Y0pFMWQKCXQ1xnvRcJ-sZJy_k2vDQKQEhXfgu_FmoKBTK9L7Ti-JBSA5L0VhB9U7jdqDwrJek6WWj2ALyUxmwYBX3j04PzF82zwE3-m0h0HhWlmhmwYW8Q4t4l58AuauT7AfkfB6CU1IZqzKlaPmqctdFYaw2Ty6Ez8QZWSfwbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjsRlfdRG6w8laX3UBWb7QlGVI2jofdUYPFNU2dMpTBF6ERobruMyVixts_iT9IRQHnuj6NHmMJSQ4vRJsfKper3qP1cWJMU87A41VRSMJRWkKnemz5MkZc5MXcENNFkh_JAX0neLk9GAN1UadwXVEA6JduhC6QbI11pZgTdJzdoCR1nthiN2H4IAhh7EgN9wJ-XlXga6zTDh_Fdjw9W9tluoGALGdCNObk7x8dLOgSC3j-mSf3R40THoE7QfsYKlrm_rGAeK6Q1wXfu4kxRd3To8felhESigsWCF6MqbkKR1PvTmd51uVwvi57pIQnbjpExilwL_tngZmPQH1Jy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTKufz_yLxDWxP3dNdi9_jpGYsdgJL9wwaBfHw1AuPOQxLM9TUyxEQD-94diDIzGzE067m_jXpvo2fCUg6WNLWFnUT2WQE5XomoSXVjPrJfS_ruq7yGQ6oiOEVA98lXVS5bVjH9ui3N5wl-zK1451iwlTFOHFjcicyDnlioDv9OjdHRxECDS0xyB4kCPHdhwRBhnqRRjGWhWl7-52hNtlSs6FW0n1132YZkGn0lskjyTIDr__9VeGZA2AiQdRB_elrTI2KU3bWXd3xEhCDG8SgVlH7KaQ0icLBSvAz7RpnINNXsLhZX2F5hVByQ8kpvu28n14FhWfbId8sBi5sppOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VciMXMlaw7YOR6dNx94XqjhNxubZQ67B58GwJdy4MSVajkdi8ozkLGNq_7k67w3fHxxSdw544uREoL1SbG5ta3BFpni9SXM_JDBdwM8QvG9WeZvhbZFB06lY79iv1of03ca99bpF38YZLoG8561yXTmI5InzCroeU8rAHmNlroFWp0QyYJ8Gm1aj7AbWUt0iwXQcVzJ56hsxUNYXsdpuaPJ12tRxnD_aCunukpZ18gitnEtZBR4b7sRciAZMuGV5atgmhzt9Zwd58WjQ-6PW-S6lw3dKoH8SDQfqt7eIY0xvXQwg2ffK-nH-8XaX3VURO_yWLnh7HGHqEAbsw_VoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9Y717uGvZLnbCiYW5J-D02tDG4lohygUpVnkzeNRbYpXZRwbStSDGn8DZK94rK9ovYJVuzPJYX5ApJcclro3mGDGZWylIdi_Dl1gyW6-ln0kqUxPOhMCaxNFjuPw3gQKngTAYgfMHgL-sh2TLvw3SNeUOwMA9Yh38pYcZJxykcGzBelXqc50yNSSBlE0H8luaK6gQVILjrPB6UXxzePy7dRqXFkB96GvoLCJ9Gz84rFBUzFvPMvX_ONj99317nKfeIQcGBSsHLtbOmDDxAWP8CqRzna1XbX87JG-xkggEsBfivCLrUgbh_pku69AhTEApuIy2vFmdJqKc2X6JtVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx56E8Gkylr_XPioIM7yUFpzn9EjPxHo2enXuRIAjh9WB_2GZ43lt5jbnqUycprKAY9i-lwKhjzWoKQA74UQG8xZ3SbPV1xBDpXbQaElm0vZfv9ByixYz9wehIINXzD_JOs23vfsV6fE-IJEpGBc8x5uiHlyGo7fPYL_fkZn9xiCVk0-JRD_dgPZFHsL6m4TqhmUID6xmmzuiiU5mGuuKaHEGRcGE8ojpH_f_Px4zi0s6JyIavWPJOnXpX9gctXNB09WGxssavlLbi64L2s0kiB1HDV1sYiZX3uKn8z2VLsyf4tX3PFF7LolTSytS-j1jCg6lbo7kWcjSwQ__ThEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=MUs3pdaiyNh4qiL9e48iIiOPzZZul7lsF1FVo-VrdjBz73Suw6UCyQDq7uUAGjCW1JJYxA-OLsbC0Yzq1X-RrvnXX__KfubTzQl0ncwIUXoZIMBzsoagDscZ4zWtHdvYn7QVo4ay9EMZBA65RVyH5rlNLrOE5sbF2lkbNhwGKlfmDsS9eI5qZT8Oqhxf7Wqtte8_i1jym-AUPmOe-S-la6N_Jl1NkReB4D6KKRJsH6ZqngofGwYQqDDCSiILHeNFllHA3LbrokC25bNPFFySKnbcEJP78SUxHkffeXFz1QB1pnY-X7dn2-BiecffaitaniJsNC7vOjxY9m2iN6KJ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=MUs3pdaiyNh4qiL9e48iIiOPzZZul7lsF1FVo-VrdjBz73Suw6UCyQDq7uUAGjCW1JJYxA-OLsbC0Yzq1X-RrvnXX__KfubTzQl0ncwIUXoZIMBzsoagDscZ4zWtHdvYn7QVo4ay9EMZBA65RVyH5rlNLrOE5sbF2lkbNhwGKlfmDsS9eI5qZT8Oqhxf7Wqtte8_i1jym-AUPmOe-S-la6N_Jl1NkReB4D6KKRJsH6ZqngofGwYQqDDCSiILHeNFllHA3LbrokC25bNPFFySKnbcEJP78SUxHkffeXFz1QB1pnY-X7dn2-BiecffaitaniJsNC7vOjxY9m2iN6KJ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=PVbFtk01G2FvZMDiE18dTSe7vNHHKZ27X0U9Qk9Sdu_ZIoYq_FbijlBQBPDj6UHJsUwXpOluFSTGG1M5u_yxxCHYge2PhyuDGFmey-T29ZPEz3sa4SX3yEgu_FiiDh2phP2b-LIf88_IoVfNd8PWgAMHlo5LJWV0TOhUUixSlpmJ_pWA_J87A3EmFVY8GXUzD0OnRuolVwDybJBZkJbQNsmdj3-p8Vm-PJyiFO7DFM4BkGNnWXuk-6pZa515spK30KnGfoaohSxTV6TRDKhwtRRvW5M0Ac6Sd5HmRFjNc12fxhQCKK8MIHiJCHSIucgLki7U2-KHgRKTJ4FEZ3jFRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=PVbFtk01G2FvZMDiE18dTSe7vNHHKZ27X0U9Qk9Sdu_ZIoYq_FbijlBQBPDj6UHJsUwXpOluFSTGG1M5u_yxxCHYge2PhyuDGFmey-T29ZPEz3sa4SX3yEgu_FiiDh2phP2b-LIf88_IoVfNd8PWgAMHlo5LJWV0TOhUUixSlpmJ_pWA_J87A3EmFVY8GXUzD0OnRuolVwDybJBZkJbQNsmdj3-p8Vm-PJyiFO7DFM4BkGNnWXuk-6pZa515spK30KnGfoaohSxTV6TRDKhwtRRvW5M0Ac6Sd5HmRFjNc12fxhQCKK8MIHiJCHSIucgLki7U2-KHgRKTJ4FEZ3jFRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slM9KLTKR_sxC3pvxIwpwuNESkJJja2W5rb1nBToGw8ZPn6zwPOLRPmqnjHDj8RL5khp8npcgRDMzRIxHkqloOAfKTmoMTEmB4e2Z8SvWKtI7gdMLaap6vnkOouhMi10w7nH9vp2XP7_xB8lg4JJzj0Hcuay3It93N3T520J2gh2FhQoWGAyT0yaKaFXZ0w_LCbjN3cJtj3vLrGp_ZX6MJMpStv-K2t05smfDK0qJL8qxp6x2-dBKhqsFNA1urYtKfMLqUdqLHQ6UQRFEAdBXZiKgm7RXl_miydb0dyDtDTQ_0bRzmbWeX-TiS9iDxl9T1SUX3w0sgCpDNPURh8O5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7ZjizHsljIOfc7IA0f5FmvN3s23_p_f5sFQ8MkZeSq_olCX7M_J7lt1JgCsZwxiRJIeSGu7ZHLQv0cC3wdqbQbZ257P2_iKmFS7KaiuLDSzVcbucuaeSxEPBPnCrhIlUIBpd0ooQtdA6perGZzqUnLdxxxycRqvdObiNEK7IxNgIQk44BvQtYmIVr35UHTdqTaWyMoKv27Glar-gjGGOjsLehyQyrbdc_KspvDhB9dV7u42INH_fd5UOsNA2y-NpQh0uU81i6rOFiFgBKiiBUF03_LVbEA9LcKvGmVCHK9pqhzsTVymYhrHQvg5dqlb5AFhe8v29A9GJxtHP9TZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga0arctoGMMcgpECZ-n78XXC7HrIFCUCClBXkUVxyq5tVHkSEP_p8FH5yJY6vHJe95yuPWP--re2fwc6J6UmzjpZymxap4FiPZQG1rs3CDMCyeU-6ZEYZ5EJ_2Kk-_zo2v4FTRfMF7owoGeKwbNiJY55nggF9O4HtC_kbw9cRKoLmpZgvjF2pKWUIHXnB0DPU3w_vifFJrJklbambmbF4iMEJg5mOjX1hl046D68ckoRkNbzn1T-K0LJowoLWAJNXY1H0Ev-2r8UUZLEq0a52SLcOdTRwMFXkGlJpMut8HgboJ_m_vNF4N6IuaLOebF9eeAzD13EKuX4dE-YJ0LHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dsn8XomINOPGq2mJ7pN_bX_VKSF0xbFo4uTUj6TbqGvsbV4OG9B-qENR09nQ9Nem9fjUNYQDxxbD9wEkx13Wz7le8yrry0Zn0pSd_1j20mUlPam-AAe5esh8qtYFmSGHlC82HQ5F3hCXU9UIZkPVJKfbpwyQj1xIHzCbEFwHf9qreoCD0241srQlYFX54gcLyjtQXLpQ2nr97uOdQ_RWWwX7TXl2cN8x4leZ6ZeJIYT_Bd7kfA7tBmOUy3q9QvBNL-HgIIyKwtldz7eLeDm_E1vM-2vzdXfOyYbPcxH6Cj3saar44r2ASuFE40ARGJOc92szbW6m6cLVyO27Gd0EIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3mGwNdVjYVyNuj2mzbD0N-hC1NbySbbFdRUWjeocry_86XZd9ZH3KElLyB2Ttpf0ep9L3i7VATz5J6HsrIfjA0Cv0f896H5AJEfxuxs5UBZbnNp2kzDXRz_zAovgBGS0nVda-hi__l3I5G0KTyuUoMODc0UpPxRG9Gjs-bo9vtlSTnTGunD7TXfTi24kcH-5hJYHTRZZcDNt0x01idzKD_RNrN9Lp7mEuvKERb3HJxj605AAhqRu5juKNuj9bd4WyrDQ4cT4_fkWAzRo30FT-OjAIgQeMdu3iOIH7PqN5zKxPdBw2aIKf29Q7oG4cKvWLYmWgzgiQXmIM41oBdMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbGzU5AH-DySa_0vOxF4RwwTlprY2qdmmp30A1yeNoHP7rmUXa3x3j9-uX927EX92CepumTpsrCrMniLOZrRShNgZZ8F3ZsG2O82k6ePXXs80mnAMs9kCoaJ4GdhbqMbdcSVgtr7XsxboyYTHGiur-ltYmoN2BA7XQvLorKKWxSWmHBZhFms3bEHd12T1FdgZOQb-SpvUMHkkXyHnUPZOCzXqFRyWsYke4LNFywt1phBJ9pvdrgkIsqaMolFyEhe1wYwYShXkWJwKmiWw3lRwTyOQMoiZJPxwS23Vutq6ejcWOpbh9Mkx-V81iHlH6RhYFun9xxzGuiuyR71lRFt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psBzqBW4hxktGgjTWvaJJlaklRol26c5cvv8joVKV1C0o-kH9rZg6eJHw889XGNq2Oq3p26_4wReVAI3NFBTWNnOSgqf30UBK51zxLn-ej9WI5sCwabf8rcCYzYjR2GMHBun0KO0rf9qbZ9TAkaCGgIeeRccjr4AyLtTqJqKkBr2Lctksp1Wubxip9V61zLAzBAzRIoGXcrP7UVKaj_DAASLmYW50wAph3fSLm1Bi0EUP0_eM_q2II7-JPrtsDxnlCRcSXI25GIulrzX-JBL7SfO8tRuAjeEvhHIKEkX7wegD3u75IuMEcRICrutMy8W_Ez1oGhUu9TVTjVNyyA5ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYTFJ8RW5V_yjugbru5gDeS3JX-m8R3fyE6E53R72YM9QViVvNOuxt2vQ51xRFwb5oio0MGKups5st3iAIQ519ESqG5g1pPDb5MuWDRQ1rRUrRK3v-eQ8PztRIzUqSWgVHvC1DdCZpKHYIq0k1sFq9WWPy7zb6a3PF-9s_pnYOzLDq74hmZHkYu86N0jFJLk34AiulZNQ9trqb7EvgH-61BpQO-ZBqAms82guMb5PTJyUOm1FDwZYxDo1EM5pavKcgZj9o_dQtHDBT26q1E4LgjvwbienwhJUCg-ArUlPb5X4GIhRUhpPQ3HC25mmh2pXdckfCjTkqTcSxouq9Tsyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrnDZxFFZfCQcOgfCcXLWO7OQPcOfWcSnKImGXxWl08R9tYZyrXjO4wTRGqGakKScM6-XUNqVGtWgbOiYy7TLYrr_FFnfVyWDJ28o0tnV-NyCcpV7tICPxbwvHmjSFJJcAhGuJn-PBVteMFBQVV9tptPhKD8wn_1OEj_AX0ndfzwbSeAxe5Y9DS28jRKtezidLgGE6oJbay8vLyDvViWuXc90xrlPBeCOcegKFo5qJ1TX3i-53Cy4JjMKDWQTIFuQ6cgiJvyKHNguVozkgOxWoS0HQ-8pWgHNqRheSFucT3pbdQ3s77qTBrnpidjF3YLXart_8uatICEHH17IpLMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRKh1c2xhMDTMmdGmi5QGzMqcZRLrf7iWv3tiYUS0jrJT2cvNu6wxIb17lXXlMitlP-vB-LJVCerbFmLVkTrkY1evah0Hp3MVI8BCjHTTgbY8D7P-9Jvv21NldIDouyGZMb5lyKHlKbtK5AyImuzzf8BDORPJejQJ9g54VoPHzxCk-QtPcmn5549m7WYaX7k06sfe9pVKY8RubuPmsdqHbHMSp2kxryE5c4LhInL-CtCWV506kApTJbFX1mavk0qkQDchQlrOB90ETX1ByhQec06uwD8P4lFqUZk4xBQiYJgO_vzpcg-x9gKMEF_fOvnVN1_4-f3t1TmCI18oXV4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioWsgvrOx6SZdY5IvrfYuIFfTk-W8Yt6n44DxlRd3EraFrXLMF-E5mt4htcUJfWPgEm5xEz3yobBGi-WLG8t28wrDySDOz-yBumleqh5jdavrOTcJ4u2jumaLxgUIRZRherYOnu7WxvEa-Gn2KxEZej3qlKymr9mdfs2t-hP3HIyrKK-NlCpk88X5rJf9kpipox4ka5FgIeqdDLKO7NuGIPrUjMKI1i66bP4UQTxsu9ixu_KkZYbKp5w1PPWn65I7oIZWsfncEyzv67V8tXr08mBmUCnwjCkE2Mzzikhi78ZAEcyvxlIw_z-1lTVWlq5wZQbDelNOQQqgzmtyuWJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLnc-kXU0WGYt9N5I2ZG12K9Mf6peMR_dbgqTUN634FYhU-f2QRxvv-g72UFrm_pW1OUFEHcCKrCT_bl1Z_Invx_fcSRe87aKfWuH-3UfOYz9RDSGSFONJOhlXD-2CSBfywDX5x80IywHO4oPB49b3_-BZfFB-oFVeJ0ISJ4gB6YVzoRBpBIKPWIIv1q_Gkpm-Db2Yvjs1JK3GAo_idu3kLQ10kzug0lVzRNHKRAOLTmUM5AaQ9kDygkXvLvfG2ZHsAMpzHtFOJWJ9WbcMpF-gtdYnKf8s0ajyslzhj_Iyh6QM6_P11Y1THujy3ZGnlEPqSkHnJMpN1S9YEnWrBwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r99MPoWPaULrdoU330l-HWn4y8hOwTg5FtXv_vNhZRdqoLezL21Jt4EvvxJaNzcW8JwEI-bmFsdzKHZ9BmdnKrAsvYYow25zIzGIxGtSXbya0-SKO3ewqMra5WA0MB3RO39PnUrxZsY4rbL-rjc6utOsgSmkwHRgkD8J27U3CkjaDsMNxTCHvQnF2o17q_TiMepg_Lza-CXRPRrYi0t4p2ycz1c_D3ZkXxs2pPqS8CkAKgZQoEKhpCRV7ac1F1znsqMp61yVNaiNur-vBBoW58HnQMVo90LuO1uvOTzzea_CFx-LE_bfioikSOh_xybG7W4-UQ00-G8A4j4Pggypeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLlzRdTZ6lbqpI6vPX1LClVOFJlGdpafiqKUA86NtUpMG0YV4xVhHn0SlVxeBwEStnwW05vxXNeC83rWqpTm9K76loZ2uaU-RZFgmb8RPTu5SNnNhOAzvBCUw6NdnL8aEMwhzrZpDTRPszT7QlsTN1FadehFU_cNCEyH1SvBsFxEaXNo48Rwy-5bq5WgqfefDNaWDG0nfhJhavOpWs-4Y7YV8f35NjceMUtipWm-MePmLcKMjbuYnV6q8sl3gc135Y70Vf7rPgrVfRE9gzXFJ-olWk2au2_pC1hY8YS85KEDsxrUkR51CWSn-s15J3eWsyhyC7cZTx8ZJPRVaY3aUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcH2WGwt-kf8aoQEE-_gASPCYzl-jiumhJ9ReUQUJWp6hb4PxkXeP7UA0vl1_Chv5PvFCx7jNRw81FLezz8IFh_smKgacodCtiDDX1AJKwtghWW4WtRCz6afUk_nw5Z8I65CQ5niWqdvPqG1K_ORDHJMwuicZtJ3g4BlhX6fdtwgxS36vHKvE_AnedkXjVN5Jua0Gh8bgsEXM7zoWXOXSa99kgjmlnrYho1OSvxU7zBvB6Job945SezNnKljyQT2XaCAusslZGusBoIZ0KIiNvkSjiKNbvAcuYSnq5q6HwK0pASKezTuJEqQHvsMlZlfAN39zfh3yHUMEQ0_0xJvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aff968_sois9K1byOhJ_mbQgzUb54dKmHXCUI-irJhvrxaHEwr4kIqwGbyi78ewqhEzjIEsrxiJ3gowDkL-KLEly3LUCGVmHIMXABZFQCH05FSxpnzZ9A0F7eg5BSII_MoVOBpfId0bmgS-h-RKh9APjkSlTHQjlG5PvOtTFt8kxAcp9Q4MbmhssvCExIg7d1O2MLeVOkh2Wh_2MyQ-9Rp7S8_9UD05hRSnYrTh98E1SjBseQpH4RfbLJsurcJSybxU8hsylmwJUBY3R5lPBJiGIn7KiqZ08eDrfm67lGCe9qpBBtZxQI2ot6Werx-_ClAKJp_QYnYbbs33ZaXGKOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8xyCQ-1zO0E50HhMdJ3zIdB-OJu70DWkj_UqaxBmozltXrEwkkeuR-oS-GKDkB0Z-Ze9lkFA5xG0JTV05kmN7WvBXlkFGFtY-VbzKpOACLMC1Ht_8UoNKYgyqeKGKW_GszWe847fMWep24Sa8dyGRoABIzrw_xidIawC94F894yLuLvCAUJPDe77c6eKy31Ar7k8BnRM8Pgalwnnrc33NL6DVchkyA6XlxG9OzVRMWSZBq4hXxxN2BvEJ-_tpK2SeqeLfI5EGv7QedBW4lCe9dHEGyrkTYeXIUM7ft1zrM17Eex3k9OKvZvLElBZfO-2fdyVZokKs4XojMr_pEaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM-ZMgIbu5R04h1EWRZLzdDgqfP5MhzxoGkXAWgpr5bu0cbL6LePfgK4898BgrfFhH4qeX1rz9ajFSy0Eo8xJf_U-1-CnHznor_1GYSjuG4iDdcLh1JD-cY5h-qu9vsiZcL5RHlJzEqgsqNzTYHUJUHtL6kRbqik0yWJ-JCugBkaniMbPAzxumudsWRvoeWcqzongEvSGepBfKqAHbyukbVlewvay_VKUVhQQ9CeFRER-jJ7cE4_NnT4JnHD5-5jNDXTD4z4ZsFG1hHuvrzMfwj5TnS9EGWYqaRbSr30rAA9BVRwMgGIALW0U2GwAKlfc0QAu_At9AJ-9KRpDxCKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrxTlk9W-bBT7CSVPgI07HFF2MEmmy3cR2I5LeE9Oj-FO24jAVZHX_IN-lKm_DmFvBi0IavdM5ERi2X7NIjtvt4zvC9C8T1R7lbVfeuYjbT5vKlhsI97Ijt8K1hdNFi1uIjCMNIfoDUvupgTQRs9eOFos1kWYATkhIfTT-NZrg3p1-suavThhNv2r4jFmmJcBpdKjniYwz2y8EkAKm_fh8qJO1iMFjRck_atf4gs2ln2f5EFiaa0aPFweb1-SBSpF1oW7BKxuG0tu_2ybymwJgKSZcUHpxofoNYNXQMkoD_pcBDQXsPxWSQp9zFGgKsVPG5VbBq10mwp7FIzwkO3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdLqAH1T-AoTHWM8vfIEQjfkrVpO1vDXxVKOZSZhLxaOqMusoqgzIvBa5Y4jNpWxyCqcctcJ7H1fovIjVssPrlupG5nEJo8lF-uZrdtUYgL_-eb1qo7PCDB6jpwXlP6Z8JQf0vWr5SbdkTcTT3ndtVlRwVktuZ2zcYN7cgBe7X7jJGejgjPbHRhRLSAEP7St5rttyaSGQXXT86CZxzInDZpQrufZ1T0kJeo2GbDZ4sqsuHVEZCO2yjAA4zHI0xhj6BpcKClCK3CcN7H1Hv-up0XMfMMAhT2g2aQQc_Dq-_66hq-sgw5n2rEyxFtn4njPZp1S6rqAOp-aUJo_i7aDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPfIZad6Ill1GruSaPXh-_WE_pxLP5yWTnrCMlID6e32Q9uhuKHhccptAdO65nXyr3zJ89f_Z9pblr187CQJ_MCkxhro1weHPm-vTVSCdaplnEdgnP6JdWGFS_ogOSpypRJnLCKpcLM4VqfJdp03YH2BiG520lzUcvWJeH7HP6_aCZjZHg9ohj093ztoI0k9lzUefUPJqXPVFD2pgj5J3if_Vqb4TSmcxaUWAVI9dRDJDX3tgN2yNZ-Ngl43_L39OjcE0CCcd9XmrxIBP4F2EtkBcgAAEoqwBjUKl3T7eJ5XUY9FaRw8YTzx2ASM2iin9t4RSAcs7KG4AyAdNT1YMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMA1HTRezq7bIB5MycWVFJ2rNP3pnaV-t8c9BK_JR3sRaFcksPJOWGNQippi5yZC-4PQ6PLALOwoScf5bJ6AxPp-BAGE8NqqtDGDvOVWvkt0f9fnhf3pC5C9T0FWYel4B3L9Ul4emPJsLrEQaQNckfE67_CWXx96ewHpUsKc0dnCB_2LTU1VpxWbYDP0k_JAJnDIA3g-zMFi5ASCRlAcKPfV-wXXVxSkVR45YD9gGKbMGDh4tpG0ThzFaEHktJFmzN-1P5Vyvatuwt6JXTiEzJawQN9SrHjF-20SdK9vikO2VKuhgtlvZOse1dOd78QUAZwkoWdqyVWojbU9id_T4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
