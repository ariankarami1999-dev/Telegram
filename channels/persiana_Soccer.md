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
<img src="https://cdn4.telesco.pe/file/n1pOccFqBAwEGxZOe1vG5LSZqG0ZazPMcnoiVpVD3Hw9rvDfnWeDOd06NgkD56J7bxtL1XDgMPYTX6xtPNH7CfBaGjbP3AHcbwMwdptlA79GIzwWpL5v5s3HT-_0Eo1b-bjy6O7FuwMYrtmxLLmg8pRMGhunVLBqLh160IEnCbwQt06Jw8VAiRI2CXD06w1FK4ry4Sddl7xZJWgldZjlewVZFHD1azdOl05s2Yl3QUedUE4vhnTpIRET7lo-y-qCIKPSazZPSaxdkX_Na2QDeLisPVb7hiAv-TtmgLBpYKIXY66PmcWoVN3AGOUumTDp6l-Yqyfbzk18Ihl3Wgmp1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 313K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGb2liRYMckM8JKVYXW89ksRKPBUILPzcteOpkwelfL1-kFER-rL8KghnP9Wcz8SQ9RXsoYJFntl59W0sr0V6LqjddiQGkRmO-y5MQa0k8ux8FxQecBg1RNfnieeo2wjx6T0a2KVUxEGQmTqu-OV7qj6a6tF1UeXsROcFL4rlKj5ZruKxw4EoBbkuzry-fVOCVJQ8qshYrfxnUe69T_t4fny42JH-zh66DsOHHBDZfEU-VKkVPBQR3nNYEgu8fCfY6KKme-PcTtcP4FhxK5qLvJlXx2kGJA7XOo-tOH7Qz644iQ2CfA4jLdRYJUj5bxEel39BBnGEMYlR9dtGL9QCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشگاه آزادی از هفته چهارم لیگ برتر در فصل جدید دردسترس خواهدبود و استقلال و پرسپولیس بازی‌های خانگی خود را دیگه اونجا برگزار میکنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24044" target="_blank">📅 09:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAHynf0CQyurmErvkH-XUv_gYXTT1ta0sDzWtI8ewyGNnAW1qPsgdIcBmg93aeZ0Mr_mWZmixDrZ7GFyik0hywG1bpn_ISeP8cVfenVjQWh2s1htN0ZS_DB-SQLrzLhASl8jjK57_JhAeYAAbtlDOxrRSKy5Oqr6vxe6DYtitrrHqPXLRWinNF4-1ocEy0x2YjqK_vj_He99c9ivwO8PTuo-Iz3OfqW_2XLQ5H34JQ1rsEXd28dEQR6nWw935sAq_vujJ4jEh8HqFuva9WLY5FcBHR3xhEuyWJpV1NbtZB-GdkrMBgs-s6-lj-nB9i0FRHksGy7FHIzOTtMHc1ltcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/24043" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbGEOIKIArKtQuMXyD4WJuLoosSYJtx2Wp1tOAg3ySavNmWu0PXJjOUnw6bdev3KDXQCvAootMHzE0QpHhTa4AwcgOz5pyNbciWSTRqIdITwCi_rUv-aA54ZNqIYOVoDs-whbFuckBlVu_zOVyQN1A2nbfX5xxVb2_oqAlOmBYTjiSCZULDZ_R4ayhIr0ZIxpIRYYcaRDBMcrzucYn3PTI7L_gZwXJu-KtDA2I9yMlwE5IQbhm9MoxPvGm2YAw6hXwQprHrC7QOd2pkOxc3lYNerEhCk1kUEJtiPOs4WUIrjnU2IPcL_SSZLoexuPxOsgK2J47Z-PqxANi3O0NEUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24042" target="_blank">📅 03:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0ALhM-q4F7VI6tXIHVNXe9EVf1RCLBqjA9Q2I62KiXAzzEFpUk1OF-MOSNOcgkCLRXSEts3K9IwsSxiusCJjgmJMBsPtLkXmwWLxAPq9jjLQR_5MAcssJgnCjd691kW5gWZSdyMtjKUHmdS6e-c3U7ZZXPPOEsG_9A0FCJHm5Q3Sy3BLRYn0VGc5QW5G0vQeeZdNR4peYJ_AVF6ghEJSaBJEDfLtim85s_YMHPSgsCf0c1qxDfXcXOC84HMGKHPfChk8Qkd4vHC_7SReNFJLV4ppG4oZxmLR0PYXdeq5jRLDkLexy62-iKhBSA7haoxrwyx4C8xg7UZihqy_QZgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24041" target="_blank">📅 03:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/24040" target="_blank">📅 02:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=aeVXUoKVxETEJU0sbQnp6QI9bXqQGru8zcr1MbphMsTfh8aMhoLvbbPOYVW853vWav0fZb6j440CEVMWvrrheTRdj4OYLn9ncuFnfq5IxBNE_7a2_voRDoG8OO9PfkDURRbQOZABWh7QVYeOsnUIwf_jobjEe8HAEggYZhe7YPd8smHGVYE42BRlZEQ2AJKzi9nNpaCX7UK2iHDfugqTeaL5qNl80B4TEq7ezdAv4GQo2B04je_zsYu-gk_dU2NQ6ouo9tDKT2KH2vxcRTZigDRFDfhNW59DlqmCeaK-_9sLfuCjzxzIWVB1byGUSpyDKOPlHocXV4MIYJUb-jVW5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=aeVXUoKVxETEJU0sbQnp6QI9bXqQGru8zcr1MbphMsTfh8aMhoLvbbPOYVW853vWav0fZb6j440CEVMWvrrheTRdj4OYLn9ncuFnfq5IxBNE_7a2_voRDoG8OO9PfkDURRbQOZABWh7QVYeOsnUIwf_jobjEe8HAEggYZhe7YPd8smHGVYE42BRlZEQ2AJKzi9nNpaCX7UK2iHDfugqTeaL5qNl80B4TEq7ezdAv4GQo2B04je_zsYu-gk_dU2NQ6ouo9tDKT2KH2vxcRTZigDRFDfhNW59DlqmCeaK-_9sLfuCjzxzIWVB1byGUSpyDKOPlHocXV4MIYJUb-jVW5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/24039" target="_blank">📅 02:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBTM3wwlGhQrtYFriP11Ya-WEgtxmOJ0luJTDG2Hp-rP79eR7JYMUmri9CAhADruqdgFVlLFkSyP45Fs03n9by9MAIILDRBLwNxvZz7efQlkJu6RBqxj3v1mIX_vcn58HY7KiBQy2G_pu9P5wdt61tdRaY2_tQLEbsx6VcF3rihbeUQmqMmzZLeZCeEUV8TSezmzRYBRcUf728Mud_JvtWDx_z_USnQ4yl1FcGE-ut7j6wM1lUw6mC8U5h0FqGCRy1M1jDjT2zqO3niiqnmhU9seLCJ2dJule_3Nlj-Yym-QnfTKEa4SshhsBatEhUeeBnxRxYmwxZa71NmwyQrJsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24037" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfxXeya6rhxBerr4tGY_HwO-4PM0ErOt9fELLzvbo9azRbtWme4jIaar4GOKM_EftDs6zvCUp_y4ZZJ3Xhk7oSO9Vy_2k7kfD18HKH-c8C9tS9qvaWwpaCp1trDMInRrfhKnoGVnLKSmlXLc8vKowooSLNV09EY73OaIBKBk3hcZxo6uY2mBXYxIxnW-fso3zwhchhx4cfy1OPM417pRJMKbkXukIVjq7c70J2M5ZauLJbwtUCyz7Io5c_2YTGtDx-9mZXq5f-7A6JTnJpB_ipR1z2W00Yiv1GCCKujeTnbPbfzJnKzKEBRPLJ3lLboHI8_3zrpGifZlkAULGOsfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24036" target="_blank">📅 01:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=he7bLiysfvyrHJqmJvxxOrZz4vPQYurHJikHcT_qXq9eFaFUgcWHcM30AkL_zxEZFWlPXTv4dDtYBksaqk8waR_aIqbaJRivNoCS0F5b6QGSpoGOJcv9CIN0OJcjWJcmBr6ZviYNV8xHAPdyYywD0QttmZEKPmI3bNJmeJhastgFVRuXAG9iYH1mUCQ3I4uWMBzMiWtVzBAY2TF2r4BQoQHXrq7tN3QqPRhRposmpS7-HR7g5DkMii93BHpa3UA77htQR6MaYaHtqtID_0UI0SLq7hpMPBFZuNCcBCQ95d-0NqQsL2uhutLtoM4lYPx5OQ0lGTJkwiKCe8jjxBAQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=he7bLiysfvyrHJqmJvxxOrZz4vPQYurHJikHcT_qXq9eFaFUgcWHcM30AkL_zxEZFWlPXTv4dDtYBksaqk8waR_aIqbaJRivNoCS0F5b6QGSpoGOJcv9CIN0OJcjWJcmBr6ZviYNV8xHAPdyYywD0QttmZEKPmI3bNJmeJhastgFVRuXAG9iYH1mUCQ3I4uWMBzMiWtVzBAY2TF2r4BQoQHXrq7tN3QqPRhRposmpS7-HR7g5DkMii93BHpa3UA77htQR6MaYaHtqtID_0UI0SLq7hpMPBFZuNCcBCQ95d-0NqQsL2uhutLtoM4lYPx5OQ0lGTJkwiKCe8jjxBAQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24035" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd1eVXM7OF1I72uvVGwM4jHD30w-6VoWCf7eXOstSDJricxTJXE2E5nBbEgi9kM7rqVHVMzUhuSKmnZyJ_8qhqN3vZNRgwi2qdQx4DTfYpQoFVnlhaj-GZoiCAf8fJKRCCfc55RtpA_NIKJS7EcZnSNUNBwfa0GFIVq6UFYKnqTHwzNNIbFrfIcGB065giyAze-1tGh_szfjA31mnbY_GhwYzKxH96-iU0QqinTXYztf59Ukttsm-xmahvtlccfZIsQAF2C8RGRRorPVRDSwVKiYfanLRnkdf6ul8oyXGvOjQHcKP6YzKmIHwJ4XV6ShqLIZSrzdDYwhsyFPD5H_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازنبردتماشایی یاران مسی با شاگردان رانگنیک تا جدال فرانسوی‌ها مقابل عراق
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24034" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xut-WmmB2V42eDa4uRjudubo8QlT7-VoDYud6A9giqrpNvsv2qaTtKJteWyJJNrqATLjwgceHK-qLu1sNKFklcqOwF2ZsecP9SJ2pTRjOzOguqsXuAwM5JVpkLMt8VKdpb77BITSCiiXyy0QtSzkugC-R6Ssg4XIqdJRZIFR9oaEjTjTJxF4m3xQdnn5BlJIPykMT5DO6bUCgSIEAFNtFp8N8GAlj9QLzsVPT1wReIVArL-CDVaI4mCG2GJ3w7alitHvPyCcO_5rv3HE52F1aR5qeq1h_Gzkj5vn65Zz1XSA3rUHbo0WTAdkAoV1UmFVkRIIPko_SFOhhi63FahiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از برتری ژاپن و اسپانیا تا توقف بدون‌گل بلژیکی‌ها در جدال با یاران قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/24033" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCY_vApnW1ayR3AVPGz_fQoLLqbssKve-yz0i20K3rgXyb7DUMacdf1OH65JzPHjPtq7O1Yi8VEx_PC4yOknBlLnvmrLMqCGfeFH1wiX0itzrhybd2Rxhn0gmvWnOJrshYJawhmANDSmoZRv7XHTwUmrOCp30-ZusCzU2DoAAZWyiAFpUuMRDfCGIaeuB9y2XaD9Ic7spEhJgii8N2VkIZ-tNfEWesM-IP_-2iZooS5exvMhfVEk6E8BRWs3WGhhXsSSJvGrjQRqNok2y70rtklB4Q26Nzgi_Lx6EJ5om4yBZQd69OKjhmgAPH4QhuBxuhT1uKaCX0fdyAqPV0pwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا a31
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24032" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24030">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال: بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24030" target="_blank">📅 01:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQGjXLVMo99Hh9dzqGQc3hYKW1CRQ-oO14AuDnHmZvPdHIEuKOesqqoxssGgGswTX7qg3giCz_vqNdpdzd6fk04XzOcXhWZzXdutEIOTU2GtkP89yRiUbQR-zoQClkYSpuC18GSoNSObyLjNHYqEwULfn7HXPsMWviOB0yw1o5rJQFI2R5E03mXwWgyPJMSGT264P7AnnggUnXLlcEsXhQjEnQkI6nXcf3TiqHRAll9t0BXgfQhCV16fhYNsjvnGrX_AWc3MQCYv_5JUmUvdo8IVoaqp3yPUT3Ray7C4QWzv7oEgQLQIG6MZ2viGWtxHAU9-lUzVUaUCACLLXX01Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24029" target="_blank">📅 00:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSthk7jnKtPoNB0hqhDl4eC2tu2v97eQvwdYEJlwU0rDNtQ_trbehlgSz0C7912Chq_X9g8CvpWkNVKeSwOw_KQ3PypVenIO3fwBXjZTaF1_Q_zSa3pSL5tlSo4uUaAtx_jhqp-qXZZ-0HFgTvLCuQSwlLFFaLa20X7IlORhXIta54eC8tE0v0sG8m7LkqlLfAZ_4UZK3Ggu_aH2LccCeFi1JgCFg4-hhfHpTttVyvEq6u6C8SqsuXYoyFctPQHOuE-ZwI8_VVvlqzjAGYf7gZNCkketjG9V8i-jgVXTKsZR1ZHOtw8oWHpOki2JdhkelV9fVl8vN0hLI7plKlc4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24028" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8-yrOtaOn_BAJwErm00_V4T6fIB4OFgLBGLC4DXMKFVFACVvBMbpY2c1GamV8lYMv7z1azQoFjm_xwz3oErdjov7cnPzwg2ZvmQaKRAQnW8fQ04zHnfkp1p5miw4KFjSv0kXjy9sntXg4B_4i8Gp57zMKWDQ5fvWBuYL_PHRU4Dps6dOW1cLRdTKydxeueSLbs6hlbsWYQHLBhK32rFLujGvQ-YCKAbF9ivgAQEDT2QqoTlNOqnmdqG3U3ztWSCgCQ0ZXLfKaNqYbSzcBKD1OGUGJmxCzkKqKcVEpyGNZmIXtAf_DzG0MuEwyaKoyFE6CQlo2AjCW8TH2f_X2mSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یک واکنش دیدنی دیگر از بیرانوند که دروازه تیم ایران را از فروپاشی نجات داد؛ تمجید رسانه تاچ‌ لاین انگلیس از دروازه‌بان ایران: علی بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24027" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سیو عجیب و غریب و استثنایی علیرضا بیرانوند که میتونه کاندید بهترین سیو جام جهانی 2026 بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24026" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94db339245.mp4?token=MyrudlKgLRNofOv58K94VaL5UCT84CeqHncLrdes4Qb6DjFmbFaYgJbjDPEPu4c0cBb9vkmNkyM38yqQjeFIjTp7ot_t8eQDWXrLfQE1JJO1RUopqolyNpiB5n1UgHvS5I1AXdvKPgBXAns6dp-6DkBXXkmSCMS3UZqNixDWROlKGEtZbh-Yd-aq3itfcob78PNE6g7ITAk3PjPn_Y43PYeVM7z7bBA1v4UpJmmD0j55hUMUBUQ46EqIoXGdhfnlzrn3ZP7xbx3w77u58C4CYYNheHeJcCorPDw85--p9a34N_41lFPSqoFm4X3uzOYf9RnHahLFqCGl5NpWJJdeRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94db339245.mp4?token=MyrudlKgLRNofOv58K94VaL5UCT84CeqHncLrdes4Qb6DjFmbFaYgJbjDPEPu4c0cBb9vkmNkyM38yqQjeFIjTp7ot_t8eQDWXrLfQE1JJO1RUopqolyNpiB5n1UgHvS5I1AXdvKPgBXAns6dp-6DkBXXkmSCMS3UZqNixDWROlKGEtZbh-Yd-aq3itfcob78PNE6g7ITAk3PjPn_Y43PYeVM7z7bBA1v4UpJmmD0j55hUMUBUQ46EqIoXGdhfnlzrn3ZP7xbx3w77u58C4CYYNheHeJcCorPDw85--p9a34N_41lFPSqoFm4X3uzOYf9RnHahLFqCGl5NpWJJdeRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نمرات بازیکنان ایران
🆚
بلژیک در پایان نیمه اول بازی؛ علی بیرو دومین بازیکن برتر زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24025" target="_blank">📅 00:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3wkFRVkqH53mcQZXWYGwXxPSfbqob86661dnQTNkE_YT46CA54SwiHe3GIhyrGxzYnQxuuTkwuZOL6y8UP7FyVuUsvbkCk7roQ5cAdbf-8iWmCshOLpqGyZbLYzWM_RVe5EyPLaTUO-UqQ-5u2Ss9b1HEUSVqPpmvK_Sv1P6ZfOHM9R1eytpB7JriS5EATan0FUVU--evX6Yp-ycX5TcSLAu63eZHfB9xRa8XVIgnr1qBGpQRDN_kMHB1Doc3ANzGihfVcmzPnJnTLBm6R1hSdKX8hllt0GhUrkXJevuf4GKIdHmQoqOiAzsnUmirwb5cUFWNYUaymIfvw0cLO7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6bhAp_T_TwEweUZSlV7VAWOfv6H8BwueXhuFL0csQiWN8C3DMviJHxRTlC4-1aC91T5Reob_Htdbbz19rLUSoENAxQUelTaSBKIoJOtgV1N07J-UAlXd-0y1JebmCKflaKjAylMSKqzxNJC6ANKHQpoSBBeo3yltRBSVJzgQH9thxlUuOyAF7aLOiUOQfsfl9MfO9V0PfOAE01VNogKNY5-0Us74tJlxWs-7zjS_g9ZS5c8ZxofXmLEZMgBRevCt3M-H7CqszbBe-rG9zJA2TrYtCNu78IHdRi9irJZnzN2B2l6gPOSpb4Wurzbo9qalfosHpibENiNS3cOWhiboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نیمه اول دیدار امشب دوتیم ایران
🆚
بلژیک در هفته دوم رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24023" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUiWelg0YhRalCbBH4aAy9bEeTKLj6Kef4lxeWS66MNZPYLn0w1-7D4eIw__eG1ijliQ6xbCygRbDaMONGEuZGAx2WghP3ZGLySjQqOxD-u0U96SnZpl-OqNuYPTmd999ANtpCuhuOLUArU5u7402vib3irgzUkWFyQxBPNuDx3YWA06gXuZUCSXcDMz6E043UeutoM_7lQufVf0LTSJzXbQL05dHrVLIzOxdeQgVQyeeRBpRqwPMGSdmpmvjHuvi7D3YE6CmtV8JOtijmjXEbvKf2LQODoaxb3ok0FUUWrzNROJrxhYgO7e2-daxM9WC5gxHdla-7x1JZQBt55DMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی این تاکتیک تیم کومان در جام جهانی 2022 که منجر به گل شد رو برای شاگرداش گذاشته اما غافل‌ازاینکه‌باسن طارمی توافساید بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24022" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=e_yuVDcAqjnxjdBpLMWbx-rC0L1wVcPhkIkIyTep16o59ctKTemduSNbgMUWOyZy6dXM1sKDsMvaZv3aIFkSymEWRGkAkRMkVNBWe8IGb6lFktq9otJvaQvs27X5geiAurvxh_7_rzSdd759Ewv0W8wkZkTgSfC3Oe6xRnjvF5ZwbcLOmPJuIQDwz54JaSk_Bz4VtZkAv95rznxkcUg8bFCaI0QmLqKk0qauSvgZKyol1NufdynVLX5fpXq6srIe4LHtluikqiJzkXr3Xw1fUfYB_JWrAgLM5I-S32WWTIfwlWHTs3TwUtUyvMQAq7q8bzKQ8I6vIV_xyU728L-FCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=e_yuVDcAqjnxjdBpLMWbx-rC0L1wVcPhkIkIyTep16o59ctKTemduSNbgMUWOyZy6dXM1sKDsMvaZv3aIFkSymEWRGkAkRMkVNBWe8IGb6lFktq9otJvaQvs27X5geiAurvxh_7_rzSdd759Ewv0W8wkZkTgSfC3Oe6xRnjvF5ZwbcLOmPJuIQDwz54JaSk_Bz4VtZkAv95rznxkcUg8bFCaI0QmLqKk0qauSvgZKyol1NufdynVLX5fpXq6srIe4LHtluikqiJzkXr3Xw1fUfYB_JWrAgLM5I-S32WWTIfwlWHTs3TwUtUyvMQAq7q8bzKQ8I6vIV_xyU728L-FCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24021" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=ffb9DYXpA4V9u90BjHBReJ-kkeQ7wu1JpGaNv3hr5Le8f_uExFQLZbvxEC3_B6cj4XVApO1B-_BcqRksgoDUCCsX1YV2dOFz6n8zjYO3FIsnR3S0iO2xnuYgI5XvGcpkMyDiB7wwNavKnvUiMS9m0Op0GNTfF0KBs77OEf1n15Nw8vhNyiNuOqbanD6cyt5qArzNycPLQ9FfaZeEXIVOOEq7Xag7bJFtXRP5i9qX7DwW1zQJxujsP7sWwKbywu4ajYHdP-KserFkpzIlTeQ9ZlwaYK9-3TV_pk6YOE_Y64mQXRJdk_Q4ZQLQiafRe6P6W5sv38UwKIGmzNQipQV6dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=ffb9DYXpA4V9u90BjHBReJ-kkeQ7wu1JpGaNv3hr5Le8f_uExFQLZbvxEC3_B6cj4XVApO1B-_BcqRksgoDUCCsX1YV2dOFz6n8zjYO3FIsnR3S0iO2xnuYgI5XvGcpkMyDiB7wwNavKnvUiMS9m0Op0GNTfF0KBs77OEf1n15Nw8vhNyiNuOqbanD6cyt5qArzNycPLQ9FfaZeEXIVOOEq7Xag7bJFtXRP5i9qX7DwW1zQJxujsP7sWwKbywu4ajYHdP-KserFkpzIlTeQ9ZlwaYK9-3TV_pk6YOE_Y64mQXRJdk_Q4ZQLQiafRe6P6W5sv38UwKIGmzNQipQV6dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24020" target="_blank">📅 22:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBGU5a0snQbhRM0KtuFeNYOvNg05mzvLqM24LJqR_ab3xUvfA_36CPuqoI1Fxn-NQkouvcErHGCnd12_rNGczNoCDB0dHFcPcC0lTSSkUL69IesbjlXbvHUxka82ROsiufs5l_eWQ2Frc69XAZiMaIz1jvKtMX0nlNmao9gSLebHRr0flfH5bCuQUtNrLs9w-EOERsoMn6m08QDMpz6B9nrQd5127H-GZm2M7iBqqzlbkcWZ7afld8MZ885xgps7chNOhPtLKwNrDNYhgJHpjCFJvuASMIpU4EY9MAFXhbp2yVI4vMPXtzqygEVju7KdU2IfaOv3ve4ThVd9kXKh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
شماتیک‌ترکیب‌بلژیک‌برای بازی امشب با ایران؛ درحالی روملو لوکاکو و تروسارد به بازی رسیدند که سرمربی بلژیک گفته بود ناراحتی دارند و احتمالا در ترکیب‌ نیستن. احتمالا خواسته به ژنرال رکب بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24019" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0QlP3oOS0D7oIhzR0keP6ZOMBtqVUWETSWqFPhomV2be5IOOHu5Lwq5NiAqJOenjffC1V0QDsqErOxFOjUThAsNhANVTJwNZzENwwc3JkDRqgGmuwTz4304-dhxhFpXbBeD0S_W_8ZevGeGcimzNwMrhx-fPC00MGeUYIK9o307mIAOYJSHK3fm0wkXkWG4Ah_tLNHV3Tr6sQVmuT2ITejh8oDrBGkK1TtTPH5ZSzRhbxIifL6-459HKItl8hl7g2LBNEjXTgdCu2NtsBTaO0n9dg2d6QIRSkOtZvY-QvFlza4AiQViMlN0E9TniZI90HiA763gvYx4lax5Z6eTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیمان حدادی مدیرعامل تیم پرسپولیس: تا پس‌فردا بین اوسمارویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24018" target="_blank">📅 22:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7HFIEPaO-nKaHseCCWKj7n92ZMsmYlytdxSScSfZroVGFqcKOrd-eZfUw63DOOzQDyXgEBLU1P5HoiawF6uSox_XSk_fjFsEVB3XTkqFlo27nliswcs3cz7DP1zUFweYbujBrevT-8650_lPpNk8JHOtyg5tPxGthK3GXG-jZIlb0ydP_7Agz8dpPaYpbQ38a2vjzTl0t2jV8Jozm48dAKll3qiRqFHDDCt7Sc2_8Z0TtaufXk2kMaIsYWU66ks0V0GKkjcPOvBYzbaM5KFRqaNDqnIKGbc3uDIbNsmrQrZ1UemlCM14vIBom-J8XGdz_f4q1SnYCExrvDgTFvaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24017" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24016">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24016" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24015">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYYpeX_lebxeIkXxAnUbYyx1fmWRoTB4zTC_i3xANbl2wOfjeWyzDXqgMM_ZTFQKy1vU_e9hjBVuz5Tjc1PV42rjA55ehDhv7PFx3iqrRDBMzW-bbA5r8YWZ9Nzi6HTrI1YbiEwfoITpAl9D_v5ddLFQR5i5adBIp3Tl24mOcnmLlWoPr6rBRnzUb54FgpMbiu9rYlgU3OmOxDKLakDtbrJ80UsrnWbrix_kURvQsdxxop30KsT8w4kUIYp-DUChxB31mnBBZu2sT-OT8YdA_9zfqXxmM-WP_CknyN6Bed57HZv-DdI2jPRLEkXOadYSKJBUEVleSlIw0XY8PpQsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24015" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24014">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Umor9EBgvm9pjfw7FTGz0a36oSnfk8Ne07Sml_q4OJEuDb2fNTLA9-jUSMRnA9NgY0EBrsl6rFhRAtC0cVBrcN4-ctiq6yGz1HnD0pSRTO_nrOvrKeCQxMlJ3LNfN22TUctCAmBL734Y_ehUSPELE-BuQGfdB89IsiufD8JEw9GYOyQUyXmLbTLlktGsmaYrqPLzDqzd5CpACJ31yDuqN9vVgmySIHaJ1D68CXSrK-cYkzHoucuUq_HrGGAr7sotxOyaakZQchG8IjY2E11KfU-9kPJ75h8NHOb84dK1_8SLOUSQ5C07gGlDqJEOu6UGYgkOkD36_EH8jwuLfQkNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24014" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCuxntEmz6IaGhZy_WpeUhUkjJr6LHLQHKo7lgPAqyt7GEEg_KY3knIK6lYQ9NyWPd01tLkV2VQUJG3KQHbf12IpnkPSHPoMrMl6re7MVNiCMh8UJ9-ekTsdRq2dVzKEhGfw5XOY6NlrSERLoh8JWCRgmoCrvc5uZCh_alwe1iQGqnXKg360nGMdn6FYZGd7OFmF-skTJliGEo1MVdPfRb8c2T3Ye7XJxJ-nC7Go6fBWFoLaZ9TD_xVfXNl6hBUyddM2-jHlQL7Ws85GxYlACnb-oEvCkNTkTf2ZO1qckOdFt8R9ylvBFJm0NoaKPL3ZGEF--kqImKzI5e4Xj3Uj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24013" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB1udph1k94GfgQzNd-1ETHwOUps4qVw4HnBZBXstEK_3B-k4mrRyMEpm3GEXCy_MwPPWF55n_8Y5zJyY2Gf9vZ9oSsBux9Anr5YX1n2NmA1VhHdktIk2AYMRISzL2VSHyS-cqdD_eO8dp98J32pxKaEN_Rk0D8tIaryzjEI_tqaJFTbn6u6N8VedzYPbih3E_aDg9YJNoMqKS-tkZbUhvxZapp-NXVCcTm-HOokt-Y-idWGHkqtjYiZunqaiZY4Rxg75JcYHmfdr7kBa3BTl91LAR7U0-THsni2rqK2iXqK-ljnQ4EOs57gMGEFUuqimYFIXvp2YqOCcvc5atj_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026
؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24012" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24011">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxxPZzaHIYU4Yp-d-fN6K_3DquGY89GquBF3XHz6DqCzUVn5iRz5p9KVwwsFawvVc485jmQEjwak9MzUXVdgK4BSEWfihzv-YRC4EZsf1JmwVwT7QHRbSQ95fv3AjZwax-UvqZ1Z9K0j8WLjQfIFTU8N6iOYRKb1H8R8TUujJDYJ_ZCRLN5dzpDMaeaifXZ7z37m4anI6cQ1bd4Caw92zbPBfdZ9vu59GMsjE1lmOvlghQSYLKmOVKs_50daEBTt5ne0-n4fsW2xsz5Ix7J3Ad87aqi2GRsKnDOQ38Scr4Ny2LQg09lGkltWXssPHJIJSaeaUY9msPdBbx7WtFMi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24011" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24010">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQWDxkM7M6osnTpyOf4VnrqUfzeo1HoZodumUv9P2eLWSUDZgGhY-0-yfAONMYafJmKbzvjON6Tc7oAUbu2ww91pVJT806y3e_mk36Ii7aHCFCgvwtn10cOW8F1sDvp1sY9HTQZUm4uzmB4gk7HQiXPrBkSaxcYYnIUqPZSIGl3wqeOgVCyeH5QROs8KZJBm48mSY-clpNv8efQBwmZZAoC9xN8b7doNhSexsBOBFSGLHnK41ymnuEwwoDrkkTQ0oj_qLDKcLFFuGlIfQGf_3-Bib8NMV5X_kPgkHZE8ptjVN1zcGfPxcyQoiyWC7Cl5Gzsoj5eQQcXEEdHqBKJPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🇮🇷
یوز ایرانی vs
🇧🇪
شیطان اروپا
🔥
تاریخ‌سازی ایران یا بازگشت قدرت بلژیک
📅
۳۱ شهریور
⏰
۲۲:۳۰
🇮🇷
ایران در ۷ حضور جام جهانی هنوز به مرحله حذفی نرسیده، اما این دوره یکی از بهترین فرصت‌های تاریخش برای صعود است.
🇧🇪
بلژیک پس از حذف غیرمنتظره در دوره قبل، به دنبال بازگشت به جمع مدعیان فوتبال جهان است.
🏆
یک نبرد سرنوشت‌ساز؛ آغاز یک تاریخ جدید یا احیای قدرت غول اروپا
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24010" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YptYxQpyCTfb9qgOkdid2FaQrFb2bajWwZ7qnqGCzdyokkGlJ_BkTeEQ_q_fXm6GVDPPyTS9ncGT1icCh4kBx9-Adn8Lp8mZvySXAarXix_nzX2-rjen480Qc6ZZqWhfLyezL79njR16pGwOt15qqDyxjii_OT41HlTtBvZO9wvXrjsilgk-TGhX3gDlz8P3_NdE5EaIhSW8OPbADajYkK4AzSehoxxZ1VuuTyH967f1hjByMqSevM0jkhI-I61j-Med1P-iCDKa9kbEgdXzaoUFTFsj7E-nenYXeaj14v-cbL6Joka0zrFS67WKyolTMmffjwDqiTswK5_XMIJojg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛همانطورکه‌بعنوان اولین رسانه خبر ازمذاکرات محمد دانشگر با باشگاه تراکتور دادیم و صبح نیز درباره پیشنهاد مالی این بازیکن خبر دادیم دقایقی قبل تراکتور موافقت خود را با این آفر اعلام کرد و دانشگر به زودی راهی دفتر محمدرضا زنوزی خواهد شد تا قرارداد دوساله…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24009" target="_blank">📅 20:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1kPqlIpzBM2__TlNOoBd2dx1HrN9vPIW-6XiNngZ_iTjj8qZjW2dUXICXaeAePDiy_OW0tDqNiPduNxpkhzTbIJ-xFoxs79kZPChq-ia0Kmf0VtxFfYzHcKc5JDUOMXFGL6ZFYkMyTawbq3GP5S3-GLayQea9T1QoOcFSOEpB2Iz4BIK7pQsKCEHT9cN50nNUevg9YETJ_kJc31DT9RV8NqCMnALvqoTobKAcbuXxQylLbAt3ED24UVBZGP07dLQfwXulebBpCll_lduYVi-Lj72H0f1Te6381imVi1z-iadBNIrKbKi9GiauN2T5UPPLAUnhnROEZQjdZSrDOGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24008" target="_blank">📅 20:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQAMTRMGZA4keuta0DNO79CBVm5dPwrV8sWDZk-Czro7V_Ole_7Nba5_O4h8-4xWVicmRGp6GtfDp2SwPJnnuFUjZNMPdMaPrp_JIsVZGUs-Z0jrefNmDAtZ-saK0inN9jQJuUcspTkcKavMWftGzP4OdrcgrkSNfGGQ6_YUZCLlJpA7hOfK96j8kWVj8iTKm1KsAvO8PYXVaHVeOPOXghfq5KLWIaEFsgxNixyoJ5pVSqLEGz8Byv0Y_X6cKsVWuJeQmq0J28qTBVDvDrZ-up788QDQouw-baZbkBZxEU3y8Xdoq4-8J0B9LA9Ak8C_rG9Zm3zA6SOQEStJ1wohpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24007" target="_blank">📅 20:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgugLWVA1TdBNSStulWb7UjTEQrc8rOU4OpNAmNMzZAv4gJoP2M4Lw7TzN-Mog2Dra54k-wuUbjKHpbuyhHmWj1Cx4htyW6y7B6cco2DZ1CopSj7qR8MDPwQj0hRJlXgblIfT68JWfkiCK35zT0MkZZwzthi465c9yi1XNbDFARQQk61V3KFhftRjTgbbVlb6AYEzE7pVcspMyUCNLf2JVi8Nu9Fmnb_qhzP9y_wdtpieMqptSjnG-EGbczEPVvfSz8Xn_2pYjtXfmFk7hzTYwXZcg0W9WEtiiHTbt3tohK5be8jeGvCVchCFE8mLWO5dTzplK3Vh2cBztJNbms5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ جلسه‌مدیران باشگاه پرسپولیس با اسکوچیچ و نماینده‌اش‌دقایقی قبل‌درترکیه به پایان رسید. پیگیری خواهیم کرد نتیجه جلسه رو تا پایان امشب بعد بازی ایران اطلاع رسانی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24005" target="_blank">📅 19:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6vKndgG6MM37n4l6CqvNAurFNM72Tx48CjR_CSQddGFg8g02hR7FjAO3my-a_C4d6fP3uTtrisO6jTWVKfdr_yXe568CcYhiSRLjAqnqWSa7iREpjZuCQ-xmLGHrew14SzVl0IgnrOtpayrlbO05ej7Sq6acuKnHsDPKX5UdO44jVi7MrOdMkn_0Snq3DNDayCZp2l4oKIzmSvrwE0jVZTnV6S-V6ZkzNW3UQPQxIgtBFUrTcNN6hSgVJzEB3Q2KkJisrSMDiYECkKnYpBN1Nyd2Pq-9-W4DqeSyk0izF7Uf4KE-OwUoY2HZdmHbHJHrQrbuY6VgbyNqp0QSAqi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد دانشگر در مذاکرات خود را بامدیران‌باشگاه‌تراکتور برای دو فصل حضور در این تیم خواستار 190 میلیارد تومان ناقابل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24004" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jkmmTvnJbIRzXZ9V8yufufg3PajpRGBS---G_BGlA4n9xilxhet5hILrMLekGr67nt3ybfNFacmK0XRMScNnlUHBsA49EPIAZEv8_l1SCidi89ZULo-9Oct0edMl5wD92XwrSIQCUBTuURpFG_d7CKljb-vUb2L2Ckl2yUEB3LbT6xO34E3sPu4rnw_brB3ru0DOk1HmEm73V0B7tb_ah6WZrquloGzGd0-MZr5NKk0jagN9fFYKaolhVdu8Hhkj7iQSuhjoy44BfM3aMeTU4_dOjzCNm_qx-js1CEjQ0WxKsE6hnptK23dNLHMQT6261MxqumM7lL0daY17hzbH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
کشور نروژ اعلام کرده هر کی تو روز عرضه بازی GTA6، بچه بدنیا بیاره، یه‌نسخه‌رایگان از بازی بهش میدن. وقتی‌نمونده اگه نسخه رایگان میخوای، همین الان پستوبفرست‌براش تاکارای اداری‌شو انجام بدین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24003" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24002">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4tKu1n58qvh81MoaEV3RiiN73sv9O8QTMeh2nQG2N2IHT9UaeLqQwrnCWtzg5Et_RgptYvA03AH0lLoWUZrStm1-tRT-oYYxcLMm6dysRQtG8oJDkU5pTYdfgWusd1o7UpP7eGWn7BA-yLgP4ZwhRa9KeffSzQnzPdSFqwiwrPpMHfZzwZsD-I0kWOciNERxRbRFrIeUkCZeNq5QQmiwCx8ZNpcIGBCLM2vWwFy9pzp0GYDfX-p-v-90SjmFIrA-F0HJpdwVUaClElOFvxJtMdgSnBvY099dR0X4elCHWsft9f3p5zJgkcd-Xq8QmgcAMRi0WnyEC2N0PoAoV85JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
بامعرفی‌هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این‌پاداش‌پول‌نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا g31
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24002" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWsnnb6RI3zDbtRODklkeD_oDEv52Id44kMgeyWdL9dOG_K0Y8MCag7oyT5Yff6mp2MfLaz2V0g2MUsvDBLNMlU9DkdPlK548Wm24JNaBYX6T4W8BfAIxDPgWECjP5xH_cVi0arA7YO78cOj4YzdhyXG26s2HJEVqIbseWiX4uebufuvTVRMiKhGHCkzn3qZBoBYA_iCgjKtJFIMgZCD-man4fuv00sTLaZ79gIgLMItA2UX_9v_2SZZQTomTw1ucLGhHrp_9tABLTw-szSrfv9hMVgB6M5hG7JjtI_9HMPBZLNy2m5DaxKrEhCZx2ZRBAbSFRvYTWvuuaYqHNNhig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانی</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24001" target="_blank">📅 18:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG-5Bw9oAN3VOHaPPxEBnmqV_CImbhKhfKvi_CDk8B0fC4A85FyZjO7KriTmsmB5zuITim3t-nphX5YQt1XjJ_DL6NPBJfmpm2dz4Of9OGy0Wk34ndCTVRAoA8SKHzPd9uLgZOjCuQpb7vny2FPBJru5qlkQ2A_0OdnABWqP9ulgQXfEqjhyIBXFwDfBF2G2oS9d6pcb6YE6CNtQSY7BlmLZL2T19Oo_EnoVsOXa46I1EIFYY8EY-Lv_1wvPr19OnVhcO0BWaRP-GZFb1wUh5HHExWPmBUMql6nEv2NuG_N5y2CQGJR6xB-Rm5B2QLkDOrrNQRa52BaTmcF_WVmhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24000" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=tL_4VDh4k3IObQ_jyxXnLmci-kzqfv2yCaxXDhz31CAByem2BEC_96mDV7gr5hhzzRsWWerN5gP_rFK-SBHLNJiGVb5dMX_3E4VjNRN_Fax34qCqMfVjaGXtZOQaWO_ZxSi2R61sUrYfIbYsbI77qAdoaeT1c9SE3lyuKydIp997WJC_x9l_Vkhz07C4nsDwqQA25NFk2B0rSktUE5RgCx9FbJylSUMq_qcDySIcnc9LGlzrolV6oiKu8FI6BdzmyY2gvrqXaDUsurAfA8wUOU1fHXLjaffDU8QnWyactV6djAb88-hE8vB8V1ndXgdhq80Kc3wxzRzotlHe3XD2Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=tL_4VDh4k3IObQ_jyxXnLmci-kzqfv2yCaxXDhz31CAByem2BEC_96mDV7gr5hhzzRsWWerN5gP_rFK-SBHLNJiGVb5dMX_3E4VjNRN_Fax34qCqMfVjaGXtZOQaWO_ZxSi2R61sUrYfIbYsbI77qAdoaeT1c9SE3lyuKydIp997WJC_x9l_Vkhz07C4nsDwqQA25NFk2B0rSktUE5RgCx9FbJylSUMq_qcDySIcnc9LGlzrolV6oiKu8FI6BdzmyY2gvrqXaDUsurAfA8wUOU1fHXLjaffDU8QnWyactV6djAb88-hE8vB8V1ndXgdhq80Kc3wxzRzotlHe3XD2Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعدِضربه‌موزی‌شکل؛ و حالا ضربه پنبه‌ای
😕
😂
رونمایی سرهنگ علیفر از دیگر نوع ضربه در فوتبال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23999" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLw7tRCiA34Z53npyIbruRCAPXaB-Qa88r3k4n5dtOzUtbMkbhnI1gsCuQFSADWRJnvFm9nyhUSnv7eFNwH4DDaMXgtciND3O2Fp9NQbgqsd9kzvknED52a9PVW1nIH2ueMKalJJXm15qtSC7fiRjhhA3oLpJP-LRqEWW9ZqT5a58iU6yW8refQhGv5UOUtG1rOySq1kwFGGybRKac9nZtRqqjKx9c9GYGtpD6yUjFgzT5JBqSW-4MgswpyuGNaLWSAvdiWQf9FK1P0hgW9UUdYy2zAq2WHyl6lm6KHbfo0qlEVxvI-LUXHsn4FFChN5MiMFcnTrcbl1PipH4u5oJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23998" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug6vogopIbhNqAYjc-zOIxsNBiWP6Tbc2Qpg1_lJG0H9b7-JzM4G4uPkCgyshv2fk5p1H9BSBfPWo6vEPoLD_EYc0XvIU3kyl0pR45enU6Rujo35Pi-bpvdHARQA97_pxRuk8rztWtYDmv47TREIlf2R-cD8sVSl9ZEvMb0tkCnrP5riCNLrC-m4sBhlQM7YjLA38Tx3Do7KPLetYoqsqLAxrY25b2Z1xltGNyN_j0VYrpsOvOtGk4wQXcjIXQRgIRhz0I7fz9K369tONfc_SoA9pOQx-jGHFUHl6tRVPigt5ASmhPVzTPdTEnn_oL1Ryo9VJ_2V0kFdsG2kUqy9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23997" target="_blank">📅 17:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQir_6GEV1gpNzxzHMd3-LFgYUaxNp9bgQrBl3m6L-s4QUip7UJoabkWrVkPCpNBWyrw2yBf9POLLhx73QquFhZ1clYEv5jiuH-41ymb0r2Zsq0jK1lNw2IplqOdbN4WeedSs1RIM-rcOVM336oQ0mJlyiqqEUPFJDys9doGZhV18eGlK8VsgLOseEazRxHf19sVAQ2Cdi5IT-0lTdL9v3dItdMdxmz9r0HGh0PUJkIubDRHdEhVUBGNAP6qfxow1O7zTwUKCRX7u-SweuXP-P9Rg8ZOutqdAu2FTwVQdq8MG0zlDR_DH6fhZdvnb2A8i6XsUZ9UjFcPifdL13fsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛
رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23996" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlUXFXRTCZGWFOfkQG1eMMxrm8gkXr2PwsJ46bcxF4jLVKvyNpfIbHI0Vc46LzZYcy9-SxjqJtsr9Og3WM07V8jSvFIBz6mnVO5C8zdpKsrDzeaW-zUk_RQYcKC065BNMV4LUSMnfbi1S5Prl9WmD35uRHFjVPXtu7hJ1qR2WBQQtlol5cN6RNHAsWfj4v_jb-aCuOW1wkAblqRIzJvs3BeJ-Dt30XrkcSAm1IKAX_kx-i7l3EuZOZ0Ud6CAU1_5RDhP9fAdQ17ALES5heL6e1Xi0uQ-VoDo3Ju0S7vuvOan9l4kD1FL-M3gutIsKzrQqFpku6FiW6n5LCjk-CBN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23995" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1N616fbdVmnzzseFgvu2n5cPjGlizCWazq1de1KZG8dr-VVDrymqZpnl0REBci45b_2e-MI2nsokwJqlnNCsmnId72_p4nIBjqD6GsLE0PZPYYMF56pzmjBi7r3JWmfcoCEWvm8YK4wZarVwC30SSrE5kzDvgyo-DXCMnazapIcFM2rKJdQ8GbklEy7UGCRyRyfTHbaj46GvS2tzczSwXGOXHd0kAdkPl-SuZUya3JtnqgPNX9P6xFGdL7qbBIcnGFixGVKdmF6dA8yvm9SuJafnAkN9GAqTQoWYlzV-ckyNSULu6BtOlOGpJCQwBJYm_fervBTwpBfCiE5eEix5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ: باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23994" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=HUF0w8xIGLAA6330ru9JMNwuCHYAreS9yu7mcFRrClymGzVQbaKJho-l6YQ-78pqrhqPeoOZXZTZ1iBHnmItRyVGxrbWUu_rw1iRGjL2xuiso2CwCQefFUtRVAH3WrI12G4H9TK5yUDb-6aSdjMz1nfzHLhlrKzBTLYjgFpwjc_NhEcOvhZWoRmFJbwAsa_26fSqhNzCYtoAKfVkwLmg_BhKzNosnf7Ubf1nAV0mT7jQgxsFdH-PK84eXjZORC8zk9ajbsWwb72j6ahPS53vh_ITSg7u2k8GygUnxJKPzIs1zRdiEiBHwIQJ3MAIeySQKe_wbj_DdHjGIUYn4zwc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=HUF0w8xIGLAA6330ru9JMNwuCHYAreS9yu7mcFRrClymGzVQbaKJho-l6YQ-78pqrhqPeoOZXZTZ1iBHnmItRyVGxrbWUu_rw1iRGjL2xuiso2CwCQefFUtRVAH3WrI12G4H9TK5yUDb-6aSdjMz1nfzHLhlrKzBTLYjgFpwjc_NhEcOvhZWoRmFJbwAsa_26fSqhNzCYtoAKfVkwLmg_BhKzNosnf7Ubf1nAV0mT7jQgxsFdH-PK84eXjZORC8zk9ajbsWwb72j6ahPS53vh_ITSg7u2k8GygUnxJKPzIs1zRdiEiBHwIQJ3MAIeySQKe_wbj_DdHjGIUYn4zwc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باز هم ژاپن و باز هم ماجرای عبور کردن یا نکردن تمام توپ از تمام خط؛ توپی که بصورت میلی متری از روی خط دروازه برگشت داده شد یادآور وضعیتیه که این تیم چهار سال قبل مقابل تیم اسپانیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23993" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23992">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuWO4QBIn8piKxdlBwryzEkk73S-5NXorVN_g56kGr_nd3FZQqjDFeR_qDt3aW6h_pD1fpdAhTmd4gjU1gusA4ySbjrjS4TdPK4UKDNeHP2qv9Lp7VpNYnPlTeIQiVs2Y3jaIEshL6hfqZsRtuBSkgK-UdzCdRn-AYy6rsbRwuKris8ejvX504fKiIUPjanMiJEVKWPIo3HPNUa6u3Zcvm-YAsi0liAbE87Tq8mzybo1PW8BdjC39yEnuhhdtv8AYNKYOKM8wL3KM_eZEk8WsN7BEi8cSDTBQUAkjhsimPlCXCkZnpL0Ifo4T3K8gKm7cRTSXvnNerl38hL-B7sLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا رئیس هیات‌مدیره آبی‌پوشان اعلام کرده که فعالیت‌نقل‌وانتقالاتی خود را شروع کنند و دغدغه پنجره رونداشته باشند فیفا بزودی‌پنجره روباز میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23992" target="_blank">📅 17:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23991">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=LCZVdtpuAH2MUci9z1Q0w6QSDa-F65p3r1ER4-Y2uG3zjmC0dWPZnnHTPH4w-84JWlTRiIo5uyCndEkkr4LYUKQs9Wlppbs0IChkBrhaGCLtipdln_FtdurZLrttMHlwuV0RVGbVjehqMo7cGzC1DIGg5_n2mMKKXydO9znxIiZDEmc78XvoQ8BOf1uQFkq9PXMC10P0BeKtVgl7MSPiFoC4bPMT9rO-FUAZf-1inSiSxTstRUbUlmPn3zRKLRbgvU5jXHMP5pZasnUOuLHtBhtX27T1BtJbMIfkC8m7mM-TlSaFdQbOJ0x23ZZYoLJuhvPfym3sXBbHFwkmTRSUiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=LCZVdtpuAH2MUci9z1Q0w6QSDa-F65p3r1ER4-Y2uG3zjmC0dWPZnnHTPH4w-84JWlTRiIo5uyCndEkkr4LYUKQs9Wlppbs0IChkBrhaGCLtipdln_FtdurZLrttMHlwuV0RVGbVjehqMo7cGzC1DIGg5_n2mMKKXydO9znxIiZDEmc78XvoQ8BOf1uQFkq9PXMC10P0BeKtVgl7MSPiFoC4bPMT9rO-FUAZf-1inSiSxTstRUbUlmPn3zRKLRbgvU5jXHMP5pZasnUOuLHtBhtX27T1BtJbMIfkC8m7mM-TlSaFdQbOJ0x23ZZYoLJuhvPfym3sXBbHFwkmTRSUiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهنت سرویس ابوطالب
؛ فیروز کریمی‌ رو دعوت کرده گذاشته رو دورتند آخرشم خدافظی کرد و تموم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23991" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23990">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3qaxn9Kj6T_SEh3QI881GfZee97oILLJhr9uTpNB86EwfZoSsS7ZornEPLMYziT_syACUEg2UY9W4F1z4Il9icethf8qUQwgb1uIXkgIlMgTEd0Vwj2xWJGetBVdl36CzV173KisJKZSijpaOTb8fHk-iwW1HyQyaHvQvyb62Dh8WTsT-y4QvGsL7iU0Kf3foR6MIS_kOgOhovSp5oWPz6xd9LTzku8_fH5NzsK-bJxiE3-bj5xOcZWbz0KPpvKUDBGX0RTJeqeNcQcwsc8soPNfUXoacqffSVSLsBBxpSg12WahMT8894yYQAfM8NUB2AT3u6hjEYfK0zTTxoqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ:
باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها به روش‌قدیمی‌ برگردیم که ترجیح ما نیست‌ اما مطمئنا چیزیه که می‌تواند اتفاق بیفتد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23990" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=OjssWLsuaFMTLV9Mb2cZFa6ea2WT0fAN2leFxpj5IO4UNgseMVzys8xLqv0hkRbpWjx9UtqtZVlxHJLK_ElLpgitoE7EcMM_sk5wWTLkmRO4GqKZzc1gpUSEKO4NDl7lS725n1CBP__MOSmv0PyqWBAwMdMB_GaPVOOnE08rwW4dbLhdMXAGhb0cFaO8Cg5AdVc2cSY3njZtzGEJOZVXOA9h_3P0_X9EEN26FyjRHdf7ExqnOE0NuIsZoT9eQeiclcX7cltPIZ1tnzQujTqgofsRr9vEBivJqqnZwAZwCqT8jeqKy96VmpSrPisU18412BiPYp1OAFoWhjQFkqds0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=OjssWLsuaFMTLV9Mb2cZFa6ea2WT0fAN2leFxpj5IO4UNgseMVzys8xLqv0hkRbpWjx9UtqtZVlxHJLK_ElLpgitoE7EcMM_sk5wWTLkmRO4GqKZzc1gpUSEKO4NDl7lS725n1CBP__MOSmv0PyqWBAwMdMB_GaPVOOnE08rwW4dbLhdMXAGhb0cFaO8Cg5AdVc2cSY3njZtzGEJOZVXOA9h_3P0_X9EEN26FyjRHdf7ExqnOE0NuIsZoT9eQeiclcX7cltPIZ1tnzQujTqgofsRr9vEBivJqqnZwAZwCqT8jeqKy96VmpSrPisU18412BiPYp1OAFoWhjQFkqds0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساعت‌داوربازی پاراگوئه دزدیده شد!
در جریان یک مسابقه‌فوتبال درپاراگوئه یکی از بازیکنان، ساعت هوشمندداور راکه درگیرودار نیمه اول بر زمین افتاده بود، برداشت‌به‌مچ‌خود بست و  در نهایتاز زمین خارج شد.  بااین‌حال در نیمه دوم ساعت دوباره به مچ داور بازگشته بود، اما نحوه پس گرفتن آن مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23989" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpehE7gVD72gc_GC3TnrRPazBjYyavhVsQ6NaAZuXdq7yL3JY9nFwft0c6O938gnpWG65yZTF42TIFvUYFiqUFbU5Dzk8FFD_VScEvPVLsvuV8rWzaAL1YZ6fBRTA_oZz6j6-9I4D3DN5ncu0fk2KALSkj4hhhUNzYoZc3enVvR8OPOFcH_IKJ6vSF6BFKfexC5hk_0Zs5RFnfKJDwBL5au1D1lQYNHawa2EwVCR49KieElvHLF2YIFZkQPFe4w95n90qoYfoeWVdV37BdOXwndhHJOKcO7MNHgKifsbUDMxdk3muwG_Y5gMKJJb1VOMwvotOVvM99-ggEisCtVQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23988" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMPD7fh0jspeCwwRO3YfI5P1t4xtbeeFZwnCZuFudJP0VWiy5T_9jlb7W4Ja_mQ9Ooti9_ssqeylJCQj3G12bePb1ytLfaGq-a9g_1OVVeSZt7i22opJjlpZeNRq4JBTur4g4R8KLP1mdqwa_7b_kRdP74UzZdRfdGSA1T14gaN8Rx1utIUHlT76rkMNjUJ1-y4FiiR7zrUDorujoFn8DbpUWlX_94q-4gq6BjjSWqNG004aZu9tqD3WQo-UK06VRkZBLQrrQs0Ti1-z3lgT7fvg7ybpwLVLSwb04dlJpnpttQpvNBYh_l-I8uPJb0u5gmHECbgapRvethwpU7P8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌قدیمی کوکوریا در سال 2019: حاضرم موهام رو که علاقه زیادی بهشون دارم از ته بزنم ولی هیچوقت تحت هیچ شرایطی به رئال مادرید نروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23987" target="_blank">📅 15:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=Uzr3IrTfID43fkLZHxFKxLuo3lE1NGwIlqFFAHee6wK48wF07XvHISPen_pPd0A_2jr6NAL2NG_goR-rt4ioMK0KW2fkzEMmKmdxR50Ix9dvv9uQF1YepQnGr62LfmOEGZE35DN9oR1dS4IrvzzyKJxAxFavwt1pIVt0gMcaqfY04I7vwT6ssMjjWmmOwqdC05KJBVcVSNqMzMzdtTTtbY2zs4wONP_QoK62u3Xain2tvqQFx_CseA4YUsuIiy3PZKqkGcIO4j04JVAl1Ywsc4zTGARx8UT6SGTPYnzF9e-bgsA-LFSNnKGehp87319-_pTRSd4E0GZGwe_fvZKyMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر: از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23986" target="_blank">📅 15:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TR4AUYA1_4F2YJX3jrL4-4KhnroW9sW_WzYM_O6C8d6xs8ZoW7uhQ7JKuOIIgACUY5MehGkKsiyVQQ7FPY3JOuBqtLh1Qq67RQ4NkG61_WFyedaMMznV7HJTXKs-PbVCR515HEpQopZzZbgytfuUCeYLeowWmjQnOiE_ctrM_Pnu62Wu68nV4_6cDg-_l058ZfAy4Jqc3cPtPZiy2jav-eal8xCVkaOMijk1h7Vn8riJvy_8cHu9qRxD7WW_7pjdImY53FuCrmqOyEtA4RP4T4oeEl9dAvcf5YJt5qDhiaboWw1Ig4FYuai2gbarzdorEO2ZJPhnB1muSO3FzKdlcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ آتش بازی سامورائی ها مقابل شاگردان هروه رنار + جدول رده بندی گروه F در پایان هفته دوم رقابت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23985" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=WKmhXB1u7QkBZQLBlmQb737RCuIVMWs4NwEhFWYOfQZ35VbHUYXnhKpkeol7NRJjARh-oXAQpu34KWCfGjIwUtjtPNI3uKmaCJ8wxeDd1W-2cnIjZtOPp0jWxCg-3DLAnYxozfhYVrU3wJ6a4iToaUcEO7Z-FOBkD9gkD2PD7p9aPDc0UnzlBcrQIrShlb4BwQh7jt4qNnP928uYkqY6HNQ7h1OluAiGmqoag20_AW3qwOj1b1OM3jja9AbbWbMpoBGh3GWkgM5cXB58qzvpEQo9otVl0KEtlltOB1naQYYSRQXGi3ITJr1A1x5m4Ks-OryWGph7gOdZmh9HAp_Y8Y5ecCaHNQB8dsGVHSppgFznjxJYeKZDeX_xnutWVrGFzuBgyiiVkfdQvi4X3Uoqyj7bcCCmOmsbYmo3sfQXaT5P6vNBKfw15XokzGv-z_tsfNr1O2-KrCZVgiWG6WUhdvsdZlZutk8N6j2b_eDfGVtQjqAD-MYvYGeUixFViEHN6wRdGuTYVgb8w5wlYz21FJ95VvwfMom0JfkxeT8MWTvAQAOPOQMgSSLyvzUhniA91Z_dDXFsWZQqHztGtqfAwBufISrEMBOg35SI_CITHpJOPwNSZddTxa1blNDPZA8Ocaylz0ZMM6GQ_KyZTXPexAePf4_CmSbLir3A2l3a4_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرمصدوم‌شدن‌کورتوا کذب‌محضه‌اسکای اسپورت همچین‌خبری روکارنکرده ولی باتوجه به فعالیت‌های دعانویس ژنرال‌ممکنه‌یک‌ساعت دیگه خبر بیا کورتوا و دیبروینه سر صبحونه کینه های قدیمی رو دوباره کشیدن وسط و سر دختر دعواشون شد و گارسیا به دلیل‌مسائل اخلاقی‌اونارو ازبازی‌کنار گذاشت. ویدیو بازکنید متوجه منظورمون از کینه قدیمی میشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23984" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=Vgi8G-EzbqhA43rBiPpcQmMAdzvS25Dymi5vEz7qnaLYxPIzeW242lhcRkmMmbIqfv6Xl3uqb2tB5uCwrT7II01IGa4UNrZyAsqCtNYqVsxGEbU6MN6HwJ3AfyV5Nik-darAmzqOyameVUN1_0wfvDMHKWCVIvd5OzgBu0lbYiXz_4UUyn7LMrxO2R5775Fzj_oCy3pBu9Yvdsc5X32NgWZEj0dILhd9NKO4GVCv86lJUIW5sUdq-q97KVCQ0R6SObH6jOtawiuHvVJO_e_jmUkrIALm7s2ytdaLsGFaufSzfFpU-Emu6PD8GytgmTt9QdXdzwcOiWhYYy0F_xYWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23983" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=RzIk7bmcBUP_ZGbJEjrLrW1p-TOEp_zoXtMIBekqikabo_uPod4aVh9qvwZsOsVlEdVkCM3teCgnjxxIjfxJlI0NYU-5baGDb7XPXYGliWh7pS3SzmNaBuTZQp-_ydxBqXBROpJMmWvlUPmPIk75uPkUDYWEoWPWJFZ_gNlwbs3D-VqnnNmq_fDU46hTVheOGyUccQ1C4k53qa8-GBjXLrLk8wXqrQ1cQ2RNGzgJs2UEhWbQfF6z83yI8RuPg-bFfZiQZ3NPhNwAWQ3fyk6kzYrLkkszr66Decnu_oeWFjX4xAYk9Ko9T6WSssH3eNKl9-X0f0LRxuALg7nPsM0kqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
50 ثانیه از دیوانه کردن خداداد عزیزی توسط جواد خیابانی در ویژه‌برنامه‌روزای‌اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23982" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFvRA2Wcb2NNkrOhMoFHR664ongzcI7kIZ-pawYut_U1PIxgvILtxbsQbNdu2JaiDoHzdLv5ej5eqOistFC50QwyDS7cwk_uBobiLAf77lKxygIXlW4FlHG5qsByW3GI5iqdFsq_hKUaeO4AQvyP0fPcqNFBvyJBv-9nqL7tDGJP5aMGnhueIc8kGjSZZx7JOZVoBpK5lIkzJlKZAUMqPfMISPql7hHuluP_UbA0sZNXvstHy8VBTHbj07pIwgKTlX39qmZsSHmVegT1rrOxvBZ6CFEOJZZyf_0Vl0-Hal-pfHYxKPnfukcujIdIlLm4aFfxW63cZtAl0MmRAlHNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌ بختیاری‌زاده سرمربی جدید استقلال امروز صبح باحضور در ساختمان این باشگاه قراردادش رو با آبی پوشان پایتخت به مدت دو فصل امضاکرد. بختیاری‌زاده‌درباره تقویت کادرفنی و جذب بازیکنان مدنظر نیز گفتگویی مفصل با تاجرنیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23981" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krz7LPik4lGdTLE1zYLYshhDZ_rvZmb6YZT6xhX90XI6wZzIVqS9l-HMnbclsFrP1bdYV3eL2MHsR6iM8-Cc87apG6z0xMh5jXXZBCi5VgdOUVuri9KsGNxE1y9J9_tI4zoDXlPp5dyvHZlLtSPy8jr6Liz2-5w_4hnVzu_T--eAQ6Rl4KsduV-NGuXPHJO6e6dDlJ8zcDgrsHYNf6QQnFnNJcK-IU3rNI_uJOtTAbDvN09iBePgLpi5b1JjjA5gKUaRcJcEx0dxTtVjRTP8beR3IGmWOWmOF9doGR-ESw1xzmsuftqCKfU94CFcrvOB9O-KakBvA0U-0jCKKthO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23980" target="_blank">📅 14:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nESqrOxQS1v58VqVpcF9gZIDGu5jGzHSjisDBvXHFGnQV8IjSpGzEEMuTIa6xbG3ghR_M5Ol1peNq4YzJX6W9qwdnqP9rGUT9ayxc9JhCtFQDbtXwo5eylvo3WCmJsW7_M54f_CD0J2bWzZBC8XPLWbcPQrn_Dsjc0B3ry56UOL2vSdZyvWr9zqBLejvtW4NLQoIo6ecR08oEKG_vVs1o3SS8ho8njttlAGsxbnfLVLkASYRXEimOTNTzm9y-Vnwk46p3I9qOX8uxBgd0RKgWd04KQuaplxLEN7FaDSMdLoPogWNOOGVG7AO3GNEcyNYiiWOrJCKJyfr94122A-4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23979" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=hubq86CscdPLOig7FcAjDTsiStumoBdY2TCxrUiD5HSnXnenoxGfsyuNGsksnJuqkyExeGISSSoPwXrEVGhdFqyjALY0r_jIJ_OpfMgBraWQTtIrMnhP6g2FSGGwzGd-LyWxdYL1GiuaYqT_zLVTjfyMxenRHMPHqM-1eFoxv10Tl_uOUIy8S_YRxM2uzLvI3pCZCQaH3tGDDXBIKzW7x4g71AnjJxbwcQ2G8SbCK78iy7eQQb11ibm7gKCg3gpYWWXJkdpMt5XsNNZofONv_SkLcjXNNTwK0OlC3gKBjfMVu0tv6M5wHzGNIvFqxNRAnkpNleDXTXM8cMrBvtmb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هاجیمه موریاسو سرمربی تیم ملی ژاپن با دیدن هری کین کاپیتان تیم ملی انگلیس فورا تبدیل به یکی از هواداراش میشه و باهاش سلفی میگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23978" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8WBOsB4QpPqpGfyKUJ7ABXYTWD0HxpG-TPP1HH9uxgOmHVgh0IZicxlbSal0llJLl6RGd4rg3fAaMqSk2G6mLGKAjPOu5pC-wBmzHn6Ry0cIgWdeg9hqhQxAMt1xCJ8M7WDJVZeiBO5VtIXEcynEoGHP0VuZvmrXshE8V9x7geuifZsDPznO-sWLv1XIKwlgjkptIWePj9Ws3q7iaUvCf3Ib5kONfmp8HUC_Q8jRTyAqRpNWo6Uc9QkP2SaEyfPohQucG6Ab6LAp708vQOic5dUB34CiyoWqWBxC2i_tr2ityMiEP3DYBPQnY88IYew2fWgx4XkdPyu6QAnmH2WLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه‌رسمی‌تیم‌ملی‌بلژیک: آقای قلعه نویی عزیز دعانویست‌رو از تیم بکش‌بیرون‌. ما اصلا با شما بازی نمیکنیم سه امتیاز بازی‌برای‌شما. تک تک بازیکنانمون رو به دلیل مصدومیت داریم از دست میدیم.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23977" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGr2AO-3puRbQ-APZ6wZ4wT29u6WZQ_E88a-c4oVkTswasnV920zWKZsrM_9us6XJLv0YZ_z6uK5vZowQRjjbgnKnEAnc2TqxT-nHf3FY1SkQk58dSm4WcTi9MIi0dnmV87BVusNV6peoWGJiVXzYBsOFxzFg42h9qfUt55kU5hplIOmLCILETmvjPlwn8ODB5s_PhVK_KZ3NeEZeRx3LNaxWO9mrEZLUCPLULf-fG9lrO3wKzMu3D0R9IeMwHo1NMMM5RYqq-KbvxWTkcRThdKgFesYN65aRXS3uzkcCTg5rHiPUtt3DKRFgER7woYZiDCME4kTXVWbt-8jzZ9RKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ مگه‌میشه؟! رسانه‌معتبر اسپورت بلژیک گفته لئاندرو ترسارد ازناحیه‌کتف‌احساس دردمیکنه و ممکنه دربازی‌امشب‌مقابل ایران فیکس به میدان نره. پزشکان بلژیک در تلاشن او رو به این بازی برسونند. تروسارد جانشین جرمی دوکو مصدوم شده بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23976" target="_blank">📅 13:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tizu5hK7fOUkzjLexAFvcH7vrkcDXhFm3Y-H7uC7wX1DtIZ98wgcNmbwd9khxEPWGqMBaIm4McqCbOpy0ThuG-mvy_q8MgpZ1I8YQ_RSlXiHy_2uYSv6usSoVrLh5QxPVnKJOXb9QLYaK9p-KMIhrBHqAfc_Mp37HXmgeaRa5E-5XowI8gAkFrUdT5YUqelIVr7CCoV72H_ju2Ec-cw9D7AkBxVkSn88Akk6loKi1OikTbK-ywpG0auEzAe7MfQ57JZByoll8MVvuHNXEXKrEfmJC5pieiEONe2TNG0y5x4kE5ZgGUgBQiz-tnqUAg-yePR1w8CcJzcDkNWg-meHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌پرشیاناازباشگاه پرسپولیس؛ امروز ساعت 14:00 جلسه نهایی مدیر عامل باشگاه پرسپولیس بادراگان‌اسکوچیچ و نماینده‌اش در ترکیه برگزار خواهد شد. باتوجه به مذاکرات مثبت روزهای اخیر انتظار میرود امروز قرارداد رسمی بین طرفین امضا شود و اسکوچیچ بزودی راهی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23975" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZHXcRry9YOSkayzbod96NuVt44UirNrTxyuPPeAsJUOatEO8T4LTDFYTBmFCu7-9aLBN6PdlHHGBCnw20W1j-dCcr7NNOmyu7zd4UspTsmo4D5pxKWcV4gSt8FJa9BGE9XNqlCzeCY5OrFFEPRdrNi0ppsYrsnSfsi1XwaaANu_s-xn4nLe9oXn63u2v_LzcnGE3M70wbBfxCTuWCstG2BzMiPCB_YU40p-GoDVeXHvZGT21RFZyVnvlMFuPJknvxnqraBQ3eWVUFuASAv1k7QGEEsMWLk-57M1WOIQlVDJ1ZCxMmMLD9hNci-BvtQSn609f6flpO-5MhKyXX6yUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانا؛ با اعلام فدراسیون فوتبال رقابت‌های‌فصل‌اینده‌لیگ‌برتر 18 تیمی خواهد بود. هیچ تیمی سقوط نخواهد کرد و دو تیم از لیگ ازادگان نیز به رقابت های لیگ برتر خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23974" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=SmVVNjp0g1M-EUS30eKaAttygDK7i5qfnqtwVxLH7dG23tX6vcebLHPbBxUJmDPHdtY7qGPOmkIYLWSsMLuTzgTykuFQiQYiX_-duLi6tJpbWiNMaRavkW9dcPGkGhFUR2r_fyHx1acpJoNDq8D5Zf0a5leQ-17mjfex6PiBp2Is3rioZAJ8kMr3XF6wo4Yz9WkA7lxBHDr7_e0LLHTQ_ZV3te--Mb2oSGQYy1aUuMz42O26ezk8hoTDI-kwTxRkhKpJKq6b9YBfjeXiin5SSMDawKF-M8BlmNKjduj1ik19G8hXlClpC9CTmm-yNV6RXuJSuxaVccVSstBiqzQHWnqk2paAsK2bpI9qeKHmtVCgRU42ER_JH9hssXHTF9E3a7sJlL8Id0w7lFsII3hwRdWx3UJzFSG61VNM-swrwhzM-7_2sEFwqydgdCG25mwqItxjJrRInMuBZnPf_MiMSYtXL2-2_grmDKlGEy-F0TmmmfAKEx7m5WRxWY-DjYZk02YpaHwWaZIMCRmFxW14BdKkOLZk9LYzip2xurJ98gekeJfjEUxgAqTjEO0E16GiGbhh79ckp72q8tLiawayN2l0SMHkRZeWUrmPevMm6WFlIQJfSTkNq1zfc44iyfSBxtBkyUZl3WjfM062gm1QbIWEGzdiCUvhz_rzWRWNBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=SmVVNjp0g1M-EUS30eKaAttygDK7i5qfnqtwVxLH7dG23tX6vcebLHPbBxUJmDPHdtY7qGPOmkIYLWSsMLuTzgTykuFQiQYiX_-duLi6tJpbWiNMaRavkW9dcPGkGhFUR2r_fyHx1acpJoNDq8D5Zf0a5leQ-17mjfex6PiBp2Is3rioZAJ8kMr3XF6wo4Yz9WkA7lxBHDr7_e0LLHTQ_ZV3te--Mb2oSGQYy1aUuMz42O26ezk8hoTDI-kwTxRkhKpJKq6b9YBfjeXiin5SSMDawKF-M8BlmNKjduj1ik19G8hXlClpC9CTmm-yNV6RXuJSuxaVccVSstBiqzQHWnqk2paAsK2bpI9qeKHmtVCgRU42ER_JH9hssXHTF9E3a7sJlL8Id0w7lFsII3hwRdWx3UJzFSG61VNM-swrwhzM-7_2sEFwqydgdCG25mwqItxjJrRInMuBZnPf_MiMSYtXL2-2_grmDKlGEy-F0TmmmfAKEx7m5WRxWY-DjYZk02YpaHwWaZIMCRmFxW14BdKkOLZk9LYzip2xurJ98gekeJfjEUxgAqTjEO0E16GiGbhh79ckp72q8tLiawayN2l0SMHkRZeWUrmPevMm6WFlIQJfSTkNq1zfc44iyfSBxtBkyUZl3WjfM062gm1QbIWEGzdiCUvhz_rzWRWNBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ماجرای جالب آشنا شدن اوسمار ویرا سرمربی فعلی سرخ‌ها باسنگربان برزیل‌ و لیورپول؛
پسربچه هفت‌ساله‌وتپلی‌که حالا یکی از بهترین‌های دنیا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23973" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLm1iF8HSEcLdl2i_TJDuNTDcJL2KnZpc97ry2bgXVcekwpyeETQwNSrGLL_SV7nSG_TjDw-yaomZRdjtgc4kTmaQr3e1tEwL5S4teLGEvc8JLrSbpR2E_JuOZ-c_4CeKqoKphtdvk7Baizn0CpiWxEUCxFK80AvqzougnifrNi0nYAPrGu3yRmvoW8m4TFOwoB4lnwLOBN3dSK3YB1fpUdpvJO8EnQfwTHpKvYRcF4KFvjusqtZhm-yeqc_DGlNDzJNkwR5iBJmGtuTp3yM7t8-fcGwpTa0EAFdcTlEevrpIk2ziZjld5TmB_2JZfE6nMIkoUH3yRm8VEN8-CJNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکوردداران‌کمترین‌درصد مالکیت توپ در یک بازی جام جهانی؛
پاراگوئه با مالکیت ۲۱ درصدی در بازی با ترکیه، در رده هفتم کمترین میزان مالکیت توپ در یک بازی جام جهانی قرار گرفت.
‼️
ایران با ۳ بازی، تنها تیمیه که بیش از یک بار در جدول کمترین میزان مالکیت توپ قرار گرفته است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23972" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJTnP7zdP33z_VmBBDSGjDVrgbhx32bVftzrIVjySxoLcid67jXNOxkbyOq03Z6qPZSNNhauF8V29pJG81ZZs0oDrxvyzmAax5pLy_tbWt8GhWDbXVwvFJeFiUdsVqH5aBd00qtCts35QdNmc-5IYgtorKrtLcDEFFpZVMGhdoMIKJ4UtIz5FQ56rvQZt1R9HBP2NzqOA0b39k_f2eV23mMHZXbi84aB8l19ClA4y7x-XTnQAfxY5Av4QDtCWcL0JqoZgrOZy3vEqWNy8uBHbiHqjsrgH5fz3DeZ9d_L_iyIMFhci_lKxSpwoP3PTTfV5MgMd-bTilgueLz3znkSYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
فوق‌ستاره‌های‌فوتبال‌جهان بابیشترین تعداد فالور در اینستاگرام؛ کریس رونالدو با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23971" target="_blank">📅 12:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR3BOMYtUzYgVl7awv_8v44AXWftPj7H-MScmcFAzR5HaXjfL1RdmJkvtEeErMqcJjpLDPz-yRm9--iCA-bUd7P6JwK7FRN1MTeJuH7b6WZA2FHkrMcxGsAQ88h6qtSc-umPmG4L7i6A8ff6T4B33zz-3kJCmGv7pqxga1tstSuFyGPIM6Z2F20D0eJBAl442j8l13Vcg0jObe8eiNTqmZt6mPyPYO5_-3dvNYcbqpHR6LMN1FbFKmFfylVAQvQq5sAJGNcfvzmT4pGbZzcwN3vmaXj8PzAXH8Otte3B3NA33ohU4NwGZmCOBXHfAMaK9U70Ogmri4NEwfF7iT7mTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23970" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23969">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d78439566.mp4?token=T_XjMIwpN7TH1rLDnb4KsCqds_DpBtBQ4ccBh0j7Kr_hxlyp04Y9npJeyu83DThKYaPI898HoEhsnaonxCN1bzVWT7M-Kz3x55guWaEzpRYGist1hkYR_-L0Gu_RQCxU9e_W8WT3Y2Q_k_Fq2aeDo5FVu-HUFrZ5F-FzrERIPGwfMsSp6Mxn55JTcjvlycsEwm11Y2pdHyjLiBAxtZDsGfvDb3EGaxjZLfP3fLDI5L6Y8PDTf6BLf-ZlyjLiYSpOVqAFCUHui8yAgtNQVTSn_haO1WcimqaRe33VkG9JKLfH3-gdbZRVqouse01902hTpmJXTYJOPxxMUkEygjJWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d78439566.mp4?token=T_XjMIwpN7TH1rLDnb4KsCqds_DpBtBQ4ccBh0j7Kr_hxlyp04Y9npJeyu83DThKYaPI898HoEhsnaonxCN1bzVWT7M-Kz3x55guWaEzpRYGist1hkYR_-L0Gu_RQCxU9e_W8WT3Y2Q_k_Fq2aeDo5FVu-HUFrZ5F-FzrERIPGwfMsSp6Mxn55JTcjvlycsEwm11Y2pdHyjLiBAxtZDsGfvDb3EGaxjZLfP3fLDI5L6Y8PDTf6BLf-ZlyjLiYSpOVqAFCUHui8yAgtNQVTSn_haO1WcimqaRe33VkG9JKLfH3-gdbZRVqouse01902hTpmJXTYJOPxxMUkEygjJWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇪
بااعلام‌‌رسانه‌های‌بلژیکی‌؛روملو لوکاکو دیگر ستاره خط حمله تیم ملی بلژیک به دلیل مصدومیت جزئی در بازی‌ امشب‌مقابل تیم ایران فیکس نخواهد بود و احتمالا این مسابقه رو از دست خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23969" target="_blank">📅 11:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23968">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد
؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23968" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23967">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c204841a.mp4?token=jQzkPDK7ueomQgTlV-Dmke6CnJMiNDY_4xGNikna3VSv6f_ooskHLLodAuoy5LZI6lrs1NFZSofDLlBYuGQj7_ox6BzkJLVptrBl17TPKucKFX7bqpEPe_AzXq2keWgKa6ww-vKP4qxf7ieSpEkILc6lTJYzq--SJDpUtlXKJ0xIgTNEnpPkC8hyeJidnIm6V6uPrmxOxL2fDFf4Yw6xG28SX7zFZrOJP4CTqgjh6-vTgL0fUkEkUk1xr6IWcT3KU9YWtiGL6WNdGKEpljWqnYS3KcdtY1ZqIDSOGvStQ97RuttXOopG2XCK9KRKA57KJa4hbE25iHYOCh4ueafbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c204841a.mp4?token=jQzkPDK7ueomQgTlV-Dmke6CnJMiNDY_4xGNikna3VSv6f_ooskHLLodAuoy5LZI6lrs1NFZSofDLlBYuGQj7_ox6BzkJLVptrBl17TPKucKFX7bqpEPe_AzXq2keWgKa6ww-vKP4qxf7ieSpEkILc6lTJYzq--SJDpUtlXKJ0xIgTNEnpPkC8hyeJidnIm6V6uPrmxOxL2fDFf4Yw6xG28SX7zFZrOJP4CTqgjh6-vTgL0fUkEkUk1xr6IWcT3KU9YWtiGL6WNdGKEpljWqnYS3KcdtY1ZqIDSOGvStQ97RuttXOopG2XCK9KRKA57KJa4hbE25iHYOCh4ueafbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فیروزکریمی‌کارشناس‌ویژه برنامه جام جهانی:
خانم‌های ایرانی می‌توانند داور بشوند. حامی بانوان هستم‌. داوری بانوان از رانندگیشون خیلی بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23967" target="_blank">📅 11:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23965">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wyr8d2f3YB6Au5jaBP_uO3hm4TM9FIeW1Mhr4tJ33NvLeqRBnUQjMPZOL2EPaNiXq735e-BrFHqWQOVUMNnmykn4Y8QZ6EFb47W8714tA7tVvSaROkupVF03Vnlooe9YFa_Vkzx-N6W-5JjTU4Eqk8hCs4TtLiDsHVe-YudmIWV4E65qLBtHxxjggfug6k6VM94MiyfmYhMeHUCJ_hS_4-z48eBwCVCe7rBZLf0snXt8au5iJceNiuXOQQeSsKuuQHLESRipiQ0SOlKVLIX9OBJqRbyTzdHhzjWCLPZYxhi4ZCgu0611vnxIjbWLTYozk88GS6Iew71x3AiW-GcQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
طبق ادعای رسانه‌های بلژیکی؛ گویا روملو لوکاکو ستاره تیم ملی بلژیک نیز دیدار امشب مقابل ایران رو به دلیل مصدومیت جزئی از دست داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23965" target="_blank">📅 11:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23964">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIgZsA_mTWr0cQFyT1o5vSVkSIz7I4KK4w05mWwav8yx5I8MYncoD9EGaTht9TXBCuqkFlP4-W6hgGl5N2PsS2U0wP3zGsxV70ExfnlQcYV_KO1TlvUMJVB4XDrXxgxGj9OfnL1hj5g-Io_gpxSAseBTpTtji9MfBuabAIAYfXUy2CT5a8ilGjkAU8RqBn8N7GKOnB6_Dgdz3rUfkJhL77w7sr470J5rnvNxE_7CEzVvzYfhHxR7wxdLJPoAP1rvEYdpk_xHZ8f_EsgtnrUmRsbAffrnaDxc-Q5fCowkivF6_2wC7ZH8zoCducTX0abUWRJ3KC4PuydGPP4oMervMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23964" target="_blank">📅 11:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmoF5PCVO356RsZgPwXY3QK3ybKUEzi31H72KNpp8j79a6XhOHPMfMb4JxtHt4Bcekc_S2di02Fh9Uk4PrQiDqFvfLwIb-MNWW8l3JggHivFni93W-E4bjBscQ3tvIR9kHTglDuZqqmy4bI7hf4tSfH7NyW2XuP7Zhc3vtmEyh263nzTz0A5TWlEeYJr4JshA4KTST26gJ2B3eYfRgqoB1exoqmjX1eYg_RfIqTJkFnilo7Z150NJycznU0ev97KD9i2v-8gaEqCCKKqcAixUP81ZrfrevA9M88yaIJxsdiIt8OFOajalDFM9ryRMWHyJhhhOwMB0QpDv4umQtbwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛باشگاه استقلال امروز با وکیل‌ایتالیایی‌خود تماس گرفته که این وکیل به باشگاه اعلام‌کرده‌است که نهایتا تا پایان هفته اینده فیفا پنجره نقل و انتقالاتی آبی‌ها رو باز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23963" target="_blank">📅 10:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23962">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bsN2EGRdzt_Dv3QE0D78Q4eYRWOnRU36S2gp7pWgGvr51nOLIOFoh5DzWHoyCkn3OMhJaEoUMQD0VyK2CHfHYcjAvRGWQYuJsca8dPsRymKCiNWu6p5aS24aRFaAHC0Q42wt5JGce9XHayk1bFPb15Gd4pJy_BZAtmQ4_syuPhn_xyJT1YxK0J7fp7B9JAvVikHw2wfY-ufUTRXqn-drOZWvc9XwmGallVuehqMfYzrBxPA5ZxZ4JlxCs7KzL_HjaYeajl_zgD-RrYn3JS_0lVsvbr0w4jKkfBO3f0cKmsL51prUoyRwAnjC7TazQzv5kv0weALK1tcRGivjBvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرچم‌باشگاه استقلال تهران درحاشیه بازی امشب دو تیم آلمان
🆚
ساحل عاج در جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23962" target="_blank">📅 10:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23961">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQTDBXGwyt7Lilv9tmReBmU9S9QgybUIjTfK6ciXpLoILgCngI75qOsvQ3Ltu4YwyNxmHyn_teq2Je6_BJKwDWvC4uYS2eji68zP5rHeWTp6EppSATq1Dwy-bqNgVPbgVV16edG82_4lBDW0Z_eQTQBcG_A5rXtx1o8HKqPPybuS2Opc__M-4q6EPv23-bHvleJXXcanLTVD7_3GoMSr09Dz1hib-BLuTn7wjM9qkpA79MHObanXcDZ2NCJdENNQ5Pq4kuNNP77nbMUzyUYkAl3-etpl_F6sqQBuRZUUkkjVg1PmJYU5dqAS3OpLOVUeDWIpUi8tQbxdaBc3otlLLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار پیروزی تیم‌های‌ملی‌آسیایی درادوار مختلف رقابت های جام جهانی؛ کره جنوبی فعلا در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23961" target="_blank">📅 10:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23959">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=QCefCO_7oq9LkN7NA3kzXbaStI6mq7n2T5bJnAJlA81w5pnVHNqzXkQv38oKBPIB7in3Lka7BMiU2HOM-naBXZqC_IeaKV_tv_5GUn4CgJi65JuvWJ023_tPEQpm-wZdDQK1JM7a292rUt5p1FRz3SjAWE7VS46E_Kh7uef82f_NJNC651hiShrfbwnlh5fyrNLLmb-jO1-bPH7ycjaCxBwp9Tkb6Ff75Rqb6e3icJW6msKnQr5e_VMEtXqrY90GfRg0gafE7thBM5U1YAWMCWcX-QjrFKijUYDaap2boBoH7HlA8V47o32QFklbsqlyk3M9Zdsdf16jv-OethwUqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=QCefCO_7oq9LkN7NA3kzXbaStI6mq7n2T5bJnAJlA81w5pnVHNqzXkQv38oKBPIB7in3Lka7BMiU2HOM-naBXZqC_IeaKV_tv_5GUn4CgJi65JuvWJ023_tPEQpm-wZdDQK1JM7a292rUt5p1FRz3SjAWE7VS46E_Kh7uef82f_NJNC651hiShrfbwnlh5fyrNLLmb-jO1-bPH7ycjaCxBwp9Tkb6Ff75Rqb6e3icJW6msKnQr5e_VMEtXqrY90GfRg0gafE7thBM5U1YAWMCWcX-QjrFKijUYDaap2boBoH7HlA8V47o32QFklbsqlyk3M9Zdsdf16jv-OethwUqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر:
از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23959" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLys4fEAsLjEmmLr7QgMddVRvK0P-MBRGJvLrQHyRUPmE1D12waOr7B9Gx3aXjnJuEVQnAcsyW8pa1pwLSilXUIVJ1qzqL3SEQjuG9pzp54a7E2zNfkyArnr7AkCB8VjFZQ76Ju1zelBalm7g6wp5gm5uv6LtZLwSjY1UblI523zcNWaAEzvuZF8VniMEI0cwzq2Tt22cZydwxJhnYBEX1F_3_ZysONVVsU5Rd3aGu3l72Y6oEdF61uqW9yIjHdIVrZz4a9WiTOHm58tpto2EauP7gUe3K9h5-ungrI3_gHot4lGd0D8RSvVlRWmEWwLPqtgDTY8nfjqO6iPJ8n0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWKGJh46mF7cfILnN-4ase15MZJrkyIp8a7WgIzeLPzcQ2RhdGZLFch9LwpZcKFYL4cKRcEPBsEBRqEVKyXz1VIfZUirmxC8_55H8KBA7UoTOD8wSAN0aAxU4TsZcOrKNswEvM25_qxsAuRDmjlfW5-JD7cKKBo-SQOmim2iUKTp1Qp0OXCHQ5wgkcLCCuaSqO2jGrHd7vws37MApaU7AwLnCYy_Zw-mZ2Ku4QWJ-72bBQ9lgR8ZCGLqwhFzVPYi9m-FayEgvtYTItKYPGqyjAYKc79mM6yjj6f22d-yXb1OafW1vGr9nB-vj2Fjf88GdQZXZd65tA-5w-MO0Clxgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23957" target="_blank">📅 09:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTac2nI1E3B2Ul2zLCNLNEJpPM6EPCoyWRECzrZQpxSG3kQuzbywadFnEkAY5B7V5EhbADTxhvNFSPkc6dBHupFyewbYc2zNhHGKT-vngQrwv28gu8bAU1-cdiLCNlVMop5ZAZNpIOSp0QlMaRhq6LCneDAVi5EnZY0apgyWX_fiYFAb6NHR-DOouYnGKjVcSay3f8XMjgKs_HVILz8cUTx2PQH9z2wLOBZHNq3EfSAUw9ufuS4Zsly4VF2vTDm_Su3XUPLz4gWc7GTgqMwePN5M3uGwNUnhsuNg3-DE2YF8UrV_M8SKfTRWjm6l5gZ6KmLZ2_RNZ4w5Fk0yn7ulVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی‌تیم‌بلژیک:
مهدی طارمی، سامان قدوس و رامین رضاییان بهترین بازیکنان تیم ایرانند. رضاییان اگه 25 سالش میبود الان در یکی از بهترین‌های تیم‌های اروپایی میتونست بازی کنه‌‌. چند تااز بازی‌های او رو دیدم فوق العاده بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23956" target="_blank">📅 09:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvQ8kjivefkVqZ5hlrlGtGjwsfmClCwoeZSojlpbJ-avYIwqqBCnmjYNBUWTS1f0oKiWpNgru0jMSyZOKVIz-mudTlB7J55hUdOFhVtwjmduH1_sRlchvFdKaHuD66mKF7MvFC8k-dqYrh2cd6Pap6MHwzJ346y3vZaG_2nR8aSu2mgcAH26J95dgsAGISqWT2kXuf7moun7zxzHO5WC5eCU0h4W-qLbYwAe2N13czSN7UWpPnrWxpG-PFy-uo-awKppMbbLgtTCe4k081gYZJlb_y9NZyhqCdzkWwgkgL_JWUohozFOO8i-nfT2YqomtqaCzUKJNFmeIwH64MbCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL4FcC-nWkWb306KvSlGiO0ceiwnT23p7C_KA9GM6uKhbbsLLaWAhnbpuG-eBj9CGzXaVebkrcqEjCsGR8Bf-dCuNv8bPO4EJU68A2lzWlvgIUwa6QjSLrZKx9YNuEIZIqclwgJ9xyOkHUqAwnSVL_IHKqgbYOtcMjUTR3TT0gB7vV12rif_G0kavkyRoInmUkvjfWjSc_yEIgcqzYxRNvwBFvsm_jdWnbIKkLMOzhv8PrkpBAm_McZkBvWwDuOJ4EAHJZOI_g_RSKlSoSX7UxXvr6qoAw8KYXbHxaFLXV_QSdUg3KXRqp1egc1usKhsZUqid-SaijKD0EZyAKbMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trUl3KlzUkCusQEK6SpD47F_BvI7iRsTb0DlQyHB4ZWHP3sjQV7Xw1IavZ9-J9dmMA_ox2CIdZ_b8rGM_EkKZDU3__9S_PIJHF_0x66_JeQJk-ENH8eN7CRmzCJqCd-5z1VyOyzKMCd13XvkrW5YnWr45qTtlo6rYLEz1swJYEvLz8VMSMIwUL3Yzbuvex5n5cFXqjxQ2UJWSjiQ3WdMLmvMqA2DXZ3eT8hdBCzuwY3Lib9Py4lMjK9-ChmDdVVmyI6HqTCg0SP3EE9wfE9qKUecqvhorO8ppbPJx707FU1pEci54dopNeUgWkuxvu4DduquO4Qf4WamH3Ebth-akQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nysWsHJI-QAqmzAOETrlnsaK_Px516J6o8K4NS4gu-Vl1L4LCElrPubmvJsN6TsHoyecTu--qJ_5k1oRiaAlT8jawH6mHCQQiDmOYV_WpCmSXe_FKpPvYNpm1H6WXccAMn3997U8lzLHNMsWNAwzX-FFr25HKGgkJ-PDYuzNK0JG72-3ykt1XJVpHqQazp9R5U0a43RLUuMiclZCb4OqGfrUpU7hqvT2aea1oYUa7URgi7o16qKzPKC7mRSc-36QvYcsTVjwLq5P_8VY-guZqQl5yowqxYHcr4IJuvLPS1TWtDnkv4ML2UBH3Rtht7f3RTmx86eOSDIwT9iBA6Otzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=orw2115mhko5L8wJgjUF6SycDZ9h9KHBFBAP23fZXwWPzTDTfIrqXTnL09t98VHdbdWizFjkufiEPFPSw1FmVx7f2ewKDAd03wxe9L0pxvwjl07qhikyL1399gpgvR1SYGqXIlTU1lCCQIjSlX--4kmnzbhI_JZamgWRsrMttOcL6qsfFPmCvwE1_5c3nvXVx8H3OiTPHkGWI3-I3N3B00_oG7eBySgD3Q21w1EqEBLHkQ0oEgH14H58u_8KG3mvZlGVM0AslKAFIQ3Q5RXDL0EX1w5z4JEfPjzB5-ToxYgb9m4YoBw84MVhl5C7irgaF3-f31ZvZ420i_Nm96w_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=orw2115mhko5L8wJgjUF6SycDZ9h9KHBFBAP23fZXwWPzTDTfIrqXTnL09t98VHdbdWizFjkufiEPFPSw1FmVx7f2ewKDAd03wxe9L0pxvwjl07qhikyL1399gpgvR1SYGqXIlTU1lCCQIjSlX--4kmnzbhI_JZamgWRsrMttOcL6qsfFPmCvwE1_5c3nvXVx8H3OiTPHkGWI3-I3N3B00_oG7eBySgD3Q21w1EqEBLHkQ0oEgH14H58u_8KG3mvZlGVM0AslKAFIQ3Q5RXDL0EX1w5z4JEfPjzB5-ToxYgb9m4YoBw84MVhl5C7irgaF3-f31ZvZ420i_Nm96w_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl0rbAugnt-4M2HE5fFWz03XrHpxpE_E2RcNkuCpR7Q01DbkUC0gbqnW2FQzhflqwgWo6AsbkTEhnNrSkJomXAaGrHW4CromAxbcRcb6Iww8Z7qaVZpYFvKXRs8Xp4pUunGWBPkhDsf-qkJ6tuXEx8fzjgGXy8i1Ztqik6zd5aOfw17PzU-v8Ve5N6L1QBYWtH_T7Lv5eGDfYT41obOX5tRHtXeEkhWPuhwFdMrLgvn4NGMp4PQC0ziXHcGUSVhwOKEojNNNOaeGz57Nav-76NItbUc_yl4llo1XJZyfxXZdX5uVwINd9lfRmNrRFH-ekwaOXtPeoWx2VdNn0265nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌ گل‌گهر به مدیران استقلال اعلام کرده با دریافت20میلیاردتومان‌رضایت‌نامه پوریا شهر آبادی مهاجم جوان این تیم رو آبی‌ها صادر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23950" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5SDqopyf-xL0WK9mq7UIpnwrs6R1im3XLdfiD1NqI1Bm-9_1chYf8qQYFEtsZ09IDKXQPyS3d62chhihrJehmWp1chM5y0QWvVimaK2xvh7IFSMlxP0j3zn1jg5WK3YthpRpbkooKmKKKgIm2Blun7pG7ti4HW7IlAuV3S1Bsi6KreLPK2022i20nR44m3tLy12qdCLc6JzCoAtkQnRZxhoQ8s7UFbZIddtiHXkN79h6bVIE8g-JzJdFqqVco0iE4_EBPeynmcZLGwQDMwn6MPgFCzysFGaIfy7FFzYCI5U1rDhiNiNKnfnLxJ9FvZ1pflPeCZ_fdR5or5Sw-gczdl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5SDqopyf-xL0WK9mq7UIpnwrs6R1im3XLdfiD1NqI1Bm-9_1chYf8qQYFEtsZ09IDKXQPyS3d62chhihrJehmWp1chM5y0QWvVimaK2xvh7IFSMlxP0j3zn1jg5WK3YthpRpbkooKmKKKgIm2Blun7pG7ti4HW7IlAuV3S1Bsi6KreLPK2022i20nR44m3tLy12qdCLc6JzCoAtkQnRZxhoQ8s7UFbZIddtiHXkN79h6bVIE8g-JzJdFqqVco0iE4_EBPeynmcZLGwQDMwn6MPgFCzysFGaIfy7FFzYCI5U1rDhiNiNKnfnLxJ9FvZ1pflPeCZ_fdR5or5Sw-gczdl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23948" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnrGwsmttL3BEFnKeOMh3w57lXazVKmOntqpB3gu11lEiD564EYXFEBZlIvwptB2uDYIo-a-ItQI4WmJxEPtOl4B1CTFE0adc1IU23qfcg-iMTLOwUp_NT6CDpGnCqZKWaZsogtGsaX7lAb3-G8a5DRbM9ojz5CsXBd8TrUewf0xvTy_Sx1XnDcUtUh6BWVEfykH5tcIW4RJVnD4NIfYnyP7TNj221w0NhX6UyhRU3RxsZyQE8R80632qZllGfNh6nZsvekmigdG-ibi-Z7Uqwh1X92aXcAWDqzPKJoOC4pIU2NfmQQ7ADcfiCOrfslHSgZr9blYRrpgNKX4kNBhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
گل امشب تیم آلمان به ساحل عاج: ندیم امیری بازیکن اصالتا افغان پاس‌گل داد. دنیز اونداف بازیکن اصالتا کُردگل‌زد. اونداف در دقیقه 60 به زمین اومد و8دیقه بعدش گل مساوی رو به ساحل‌عاجی‌ ها زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23947" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu620gl4MQa59zbadNE8kyGeN9qx-wnhe4indwCLfUW6B1VqsCMczQgBtWlEy1cRdpgRdNj7CYPYYjcGdobSU_AxrhBRGWcXzNg217QU-ARXQ39bNOXs7rZw4lGdM_15pNptp5Br1KU4AdeIj-ZZIA0g3LVCnhaOeCuvcky-G0TTbEXcuvnAVFUJ65bdiMoIsexHgV6Gez5GKWGNNo-0w3NpJSCIP7LLfGXGHulOiUp0Or_RoqTyc5YkW_54isVoTWWp1sysrTN7e8Y6veJl3mUgn0ROojKUMbuy9A8qZSfmgCM37o8WcPtMYk3XD0nK-VZzMGTxKTFd_uy6xo1VEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23946" target="_blank">📅 01:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur0bfMMsUyRaJYT1rPPfMmUkbfI41rX1nYktOurNwoAtKBMVNRgRocVxGz6ecHKpXXN4I9moweOOA_BlG-NFwNBtZAb1cx0z9z5FMkX_MQhCEG9x_NiZBIgPl1p5xBq4SbV1zOnCzk1w4-8urIlyK95DjW94IhpvIZvGUImVfc41SGsSghNv-fdA5Dl9rK1YLQP91Q_NImPzPhcj7mJ-GWqB2HdX2mKSgb31nSFiDxKeAO4aRV8qfBo3-ja68A0XXDO7ubJIEExEsrZquggDaQemkupYBAXAazUbEGYsg8WK7BhpAnZEoo6FWTXy_UT1n9I3SesJ6bugpQFiayD6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی سرمربی‌تیم ایران به این شکل نشون داده که ساعت رولکسش رو پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23945" target="_blank">📅 01:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=Gxq4QVshBPV4RdVzBpOY_aH8kNsfFDYQzhgSm3HM77b3fD85USEETDQBgV-s7eciPk4NUk1rc39-2CP79Oa_ERlA7wtmHggcP9M9Re5hJIZqmzZtvFBMrqMBmclykOW3ga5TjPwWDGAQqF4oRM945d8h7p2gZgQmc1C5YZgRJf3VAYrQhyVvvdRtW8vDXAgVkWoUUhAaUMw0GljJl0FlQmvU3TrG0fcmQX1BIC12t7c7srC_vULZFwfOLSSfhef-MvRwVdCADtEoqhMZnm9nq67LffwZyPfufLjks6jeoVxi9pd1-TCpEDFTJw03AjhCsXrMKoLor1c2Muoufx-aXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=Gxq4QVshBPV4RdVzBpOY_aH8kNsfFDYQzhgSm3HM77b3fD85USEETDQBgV-s7eciPk4NUk1rc39-2CP79Oa_ERlA7wtmHggcP9M9Re5hJIZqmzZtvFBMrqMBmclykOW3ga5TjPwWDGAQqF4oRM945d8h7p2gZgQmc1C5YZgRJf3VAYrQhyVvvdRtW8vDXAgVkWoUUhAaUMw0GljJl0FlQmvU3TrG0fcmQX1BIC12t7c7srC_vULZFwfOLSSfhef-MvRwVdCADtEoqhMZnm9nq67LffwZyPfufLjks6jeoVxi9pd1-TCpEDFTJw03AjhCsXrMKoLor1c2Muoufx-aXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزهای اخیر شایعه شده بود ساعت ژنرال فوتبال ایران دزیده شده که عکسای رسیدن تیم به لس‌آنجلس نشون میده‌که‌خداروشکر این خبر کذبه.ساعت‌امیرخان
🟰
خط قرمز مردم ایران
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23944" target="_blank">📅 01:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rvd8BBAB9Cs4baF90z-7_OcPqJi0IHvrCFcKvtL5kTHjXE8yaupZBj8XvI15C2MUhPptRwkrHpQcaGRr1bo8YvZwE8K0mJ4C7y-c8P3cZQPW3j-JThIOB8vnL_F4XibvL_Bm1ZL99l8B8huuc7GYcgPTDOVQn-10rP5dPA2fgNJcakR9Qtm0w8gLpOqlus6xsnFfPlzRNOC6RwmKWQEXVyHYs1GR_TAEM_0N4UNsx-VwXQEgT8IGS-Lc0l7_7CgXmn7nOQdgF1V8G4EjnSyR0Xdy46Wn_kEpOwdjvWoJbMcdNWu0Rm-9OigZRDgOIH4p9RoM9jmgNW9aoz_2lT37Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23943" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhV4zZzFZAvgNmtyXU-UGEfz47VDpZNH0N8gH7YMbuc__60xjUgpaH94LThUvN1kt8ukhI4F8Bin9Gr9pGyGmziw4rJMGe24v0nqBN3iXGRkj_jzIAEaTkaXdfn8bZRXL2hywnmPu5ukgm2v0L5Pki9bR-H-XQwQiiXFwPgrKEBisHFvvaTHLnQZ_SFesGLIHUugco6pfmDjLTDzxS7WZ6YZO6d_wMG1RutfiN324Gx3v5aw8MEHJW6qq1cZ_sDS5nxxzcAHIClkSdunkr9yR7oQAXT5QAiz4fw7OksHcbFt-52hl-6l5M7bWhTLQ1v3x6OeTyBtm5BZdDSw_IMtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مهدی‌ گودرزی ستاره‌ جوان تیم خیبر امروز از طریق نماینده اش آمادگی خود را برای پیوستن به تیم پرسپولیس در نیم فصل اعلام کرده و درصورت‌توافق دوباشگاه‌این‌انتقال انجام خواهد شد. احتمال اینکه فخریان راهی خیبر شود نیز زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23942" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=ZAxz5BpGHrpGxEp24G_MNoK0SBXhe_WFKViuVHiMimefds2vZ5jh4T1dFTgIkUmG4co6Otvy6GVb75iIejy8MJsiSh5dNUZ0XE1w4ZAp3TrXXkXboeqsVnAXQfIM6qHqpICzGsNAbrQ4k9Bs6PW560BD7c39Fxwfn3Tygo8piG3nXjFOviTZY50125NbY2dhY-ETqFLilwjJUqaBuUiQi41XuJh6oGiabuqyH8UzOqW_ne5Bj_UoRXE5nW1rWm8ubDczwZO6uuzXNkvVrI65LHcxhbLsFJdUeQ82MPNn4plgUaDB-fveulKkdn_N1Hyqdc6twgsWI6tPiA-jym60sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=ZAxz5BpGHrpGxEp24G_MNoK0SBXhe_WFKViuVHiMimefds2vZ5jh4T1dFTgIkUmG4co6Otvy6GVb75iIejy8MJsiSh5dNUZ0XE1w4ZAp3TrXXkXboeqsVnAXQfIM6qHqpICzGsNAbrQ4k9Bs6PW560BD7c39Fxwfn3Tygo8piG3nXjFOviTZY50125NbY2dhY-ETqFLilwjJUqaBuUiQi41XuJh6oGiabuqyH8UzOqW_ne5Bj_UoRXE5nW1rWm8ubDczwZO6uuzXNkvVrI65LHcxhbLsFJdUeQ82MPNn4plgUaDB-fveulKkdn_N1Hyqdc6twgsWI6tPiA-jym60sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqvogyI-RBMn8f8FNyERZP1gW_jKx4Ja3Z7pr6OwbyPN_Cjbea2tift8X7eEc7u_0I9DSikzzbMaffjKlGAjoLFaf6SJCP4W3_F-oU9SEyPcleeJYFGNLf7_RpfPRp6A4JrspNR9RXXWkIblOkARSKeHXpK2HehEOaFy1r8XzEsOMZeOIhkEug7yLeGsggWPPXMuYWYULsoawUnc55U12Eo12kUTi9AlHpBD5eS3VnBlqQQ5WS1PIGQX9zFQxeWmMacCluyec4p39WCXvTOXj7MCxSp-nhoPtgS6iZskKR9P8HYIW7EpP0_xi2DoFogtkRZMtPBuXVEBbLaUQgFj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCmcNBqK0ny-PEznhU0qn-WX643lhX4PzOoVdpUmjkN6lFwXSbM5yQj03LgpObH0CFghG3qUHDcPNkYlh0qqNsDMnsxsZEvgXgZwabN7lqOzENIiCX2LM39Ka5vvPb4K4vhorPVB_Qvyv0_6Nkdu8XgFy7qkohNEZOkrzxDpofltElWNISejSmlFSpLIsHeEKX8kuW5tFtRXAyc-EPUvPwE7kQjvqzY8HUoXGm7TLikjU7DQEIOqsYFuBB8t64WqHA_6mjtepfHaE1Xz1Ml5VYTqcjrAvASrATY8a2sQHnKT1rSolMph_Iyu8KoUuQnaPrggQ_dR4Ur_L5TOqmso-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az3iGQvin3V55s5-1rSs9FjV2yQvvixOawbRmn-Z-bxTIgxECfHQESBK_3AsdgSWZtxc7nCw6kRwNOs6aBuKikJcJNgja9Ahz0RQAY8Wwu8AMACQCf8Bl8acY33kohdfsRrUSo9u5VdCBE6fhQ26dAi-_VfFeW7YRyT--gvYLGCqnaMhqEVWQer8XPYGll2nK1Ainc-YKllTN9tnaT5wQrMYapEbH_quVvmflOrI20cpKMcPbMtDu9ZQElHCXGabugVS2XMiKqQICiUhzq67iAq5THPbATLL8xbX3qe-MaSV3h6SvRiCOYUP7z9glbjUlIdRELUwKXZcooSeO00BDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GikElSbhQ2OdfEVjTR_3J9mJze81BR3yc7uCqNlgzuK2M6jEGT3ZU062gcUe34t_tvLaTBwjENRqjgnTc7yTsQaB99JnR7kC_O2Kv9tWEvoP9CLygO1flPEjPLGAvhjbZ7dHqIOdFmPtc6ulCo54nZtxIX8O9OOD1s6260ogS8MSmov7D04hKSSboksaZx34LcuuLcJkFKwsDPdKVFIvd979WkPBK8cKE5KJ1a3rzu2ryBdHFg0Su1S4TH-L7lGe9A1os6HEJqVO6EVtdmIDbmDI7ijS4k0YvCRNxOAnbUgOdVvrvacb5XT8UJaLEZz_XNbpLEX6bSp1mKFYWj2-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
