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
<img src="https://cdn4.telesco.pe/file/iPWQWdF9gImhvKyPevOeSYFxGjGXXb8G2mt_6z_dmyFC7IMMvvMn1qNI9PZjSgFQtCiv51QvB5T_lLVM21t65zCVIdqan2xapyWaMUqnnOVtSkPZx4p1Owt5x1XCN98EIb2rsZY-x2XwTjpttgWT-ozqJsJQtI_YWFiWAwMMZR4Q7jNgezdlpeo7XbrjcXSyRfQMVQ9aLOr801a8eUR-DhG90hYBRjtph643B84UVHJGG_BlkSSo7ahjLQ3W9wtXBOhmitCdwIBrDgy3pJW_m_IVTwqoNnrGqimLPLhAei9h4gqzZxKHgI4nCi4QFw0jKdtfGThsBTaNRloS7QRJhw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 15:56:47</div>
<hr>

<div class="tg-post" id="msg-456999">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc421912e.mp4?token=RFYVsRGFnJiw3KcunRn5QYrQChhG0TQ8KzI3ogrQaXW6avae1xd7B4tgo2VAJDVdfw8ofZ2kSZr7zBF8K3kpUMVCEQD-qSr_vZ4VnP_IxM7-xtVloCi-QRa5ulO66HelOooLW73PLNcauVPlTOeIWCYiTYdWK7p3oClBi1MiVQbrCpMyA1IqTfMpObK1I_rEcfd0hc1UM_PJ3hBzncawbIzHhnrKi8Kdq165IPhAZ_oGAt49alJip_lY4lCgqKMWSZAKbcWy4BmrMEph_UL6rJMCbwSZyTK0ZAs0L_ke1AtG5rsn1bNK87hurtLVRyconmWbTZJ4FJikG7CEO41nrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc421912e.mp4?token=RFYVsRGFnJiw3KcunRn5QYrQChhG0TQ8KzI3ogrQaXW6avae1xd7B4tgo2VAJDVdfw8ofZ2kSZr7zBF8K3kpUMVCEQD-qSr_vZ4VnP_IxM7-xtVloCi-QRa5ulO66HelOooLW73PLNcauVPlTOeIWCYiTYdWK7p3oClBi1MiVQbrCpMyA1IqTfMpObK1I_rEcfd0hc1UM_PJ3hBzncawbIzHhnrKi8Kdq165IPhAZ_oGAt49alJip_lY4lCgqKMWSZAKbcWy4BmrMEph_UL6rJMCbwSZyTK0ZAs0L_ke1AtG5rsn1bNK87hurtLVRyconmWbTZJ4FJikG7CEO41nrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظهوریان، نمایندهٔ مجلس: طرح آقای سقاب برای سال ۱۴۰۳ است و مختص ایشان نیست.
🔹
تنها تجربهٔ مشابه این طرح در ایران اتفاق افتاد که با شکست مواجه شد؛ این طرح در دنیا تجربهٔ موفقی نداشته است. @Farsna</div>
<div class="tg-footer">👁️ 30 · <a href="https://t.me/farsna/456999" target="_blank">📅 15:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456998">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_EEE2j5eTXS4-JxN6-jl28PtzCfl8jNJReX21LGB4VIN8ZXwYi8G2azVrGLeeiIYUMRIOQN8OoxC7UJZF4L_pmJcr6T14r_-6TmO4P7CzPIvcDKR_6kNZT2lgWhvoOSmlZB2IQSUQVCh0s2_IXGE91NCDvwmVOPNaht5ssQOt6TDmTixcEczJkJq-ARuO_qMz0FIBGMae5d445BJtkri4IyfhtWAAc9_Vz_EjTPtWoTxjv0Ahj6FFynWDDY04JjiIVt7jZOYw66YL4dCdp-9qAlo3CyjRWwIFNQbBMSnU6XgnX8LvL4oCLpp-5yGG6wcX90jckQZzY1u1ny2_HrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصوبه ۴۷۳ چیست؟</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/456998" target="_blank">📅 15:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456997">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f8c2df6c.mp4?token=HrrywQPZSVXNKATM_-BpXXcJ9tKxobe9SY2_uzNrHL7p9lMq4EDuKz21Lumz5qd577Gv1fgmGMsGCpCYINH6m5jwgxpBlbMzWdievHhgyU59xi15zc3ZivlwzMM97v444zXcIUtnc3iMI3jq0ouanOf8Ve-rX9wSJ5iUn5FDg7JjjTzsu3TNBA2xWiSorgeS1VtMKv-xml8VtScZUOrxBft05uOhnCaWe92tPgAVglaqTNPUrLydv5vPeMdRTuwYDdeoyLr2fCXOGZ4MeEo2ANkXNaOSbcdmzwMMGBOHJZz8qUlhmRzuQz3TTQcwRNZFXArCZlQajzxPaxPtU13KCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f8c2df6c.mp4?token=HrrywQPZSVXNKATM_-BpXXcJ9tKxobe9SY2_uzNrHL7p9lMq4EDuKz21Lumz5qd577Gv1fgmGMsGCpCYINH6m5jwgxpBlbMzWdievHhgyU59xi15zc3ZivlwzMM97v444zXcIUtnc3iMI3jq0ouanOf8Ve-rX9wSJ5iUn5FDg7JjjTzsu3TNBA2xWiSorgeS1VtMKv-xml8VtScZUOrxBft05uOhnCaWe92tPgAVglaqTNPUrLydv5vPeMdRTuwYDdeoyLr2fCXOGZ4MeEo2ANkXNaOSbcdmzwMMGBOHJZz8qUlhmRzuQz3TTQcwRNZFXArCZlQajzxPaxPtU13KCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظفریان، معاون مرکز پژوهش‌ها: ادعای کسری روزانه ۱۵ تا ۲۰ میلیون لیتر بنزین غلط است.
🔹
با افزایش تولید بنزین از ابتدای سال تقریبا در مرداد ۲ تا ۳ میلیون لیتر در روز کسری داشته‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farsna/456997" target="_blank">📅 15:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456996">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">واژگونی و آتش‌سوزی نیسان در شهرری ۲ قربانی گرفت
🔹
سخنگوی آتش‌نشانی تهران: پیش‌از ظهر امروز واژگونی آتش‌سوزی یک وانت نیسان در بزرگراه آوینی در ورودی شهرری، ۲ سرنشین خودرو در داخل کابین گرفتار شده بودند که نیروهای آتش‌نشانی همزمان با خاموش‌کردن آتش، عملیات نجات افراد محبوس را انجام دادند و آن‌ها را از خودرو خارج کردند.
🔹
پس‌از خارج‌کردن سرنشینان و تحویل آن‌ها به اورژانس، مشخص شد هر ۲ سرنشین که جوان هم بودند، به‌علت شدت سوختگی‌های وارده جان خود را از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/456996" target="_blank">📅 15:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp5fE85PFHuzap9N1gNYqDI-7iNtgZEjsO8wjboWU0kFtuVtL0Ghabm0oeP7tpaT-rctxXV6L9hitYGypB_3TD1vaQ2ncVhAgsvhRps0QE0cVkUT2AMVOfEJyETySLbfpXhUr2svze3jojetKc0Vd-qlO-v_i8JnZ4WCGppO6VCf5rdn7z7wa0topqC0FXHbWynXLHFguNiyhKMydGLlLDBRqn1cCmJhE6Ln7NJxKzH-FKeMo4beIW64u7BfGVDn9GE40rg636qCTFRKEQotKmt0m_B8K7ogmdPFqxb7hcnDlcPFVUQRG3zhbYkW0ZkBEHU2y7X2KqyWF9Hvs6EQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورشکستی یک پلتفرم فروش آنلاین طلا در نبود ناظر
🔹
پلیس فتا امروز اعلام کرد که یک پلتفرم فروش آنلاین طلا «به‌خاطر خالی‌فروشی ورشکست شد» و در حال حاضر با ۲۰۰ هزار کاربر فعالیت آن لغو شده است.
🔹
پیش از این کاربران فارس اعلام کرده بودند که
یک پلتفرم
خرید‌و‌فروش آنلاین طلا اجازۀ برداشت دارایی‌های آن‌ها را نمی‌دهد.
🔹
فعالیت پلتفرم‌های فروش آنلاین طلا بدون نهاد ناظر شروع شد اما در حال حاضر بانک مرکزی سامانه‌ای را برای نظارت پیش‌بینی کرده است. قرار است تمامی پلتفرم‌های فروش آنلاین طلا شهریور ماه به سامانۀ ناظر متصل شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/456994" target="_blank">📅 15:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=hjWQ7ymlpT3uoFfLe8JX0pirLHi7whZtX6Zux0Jjj48cZsulkHcjFf-eWssAX8ZCWq4UXN52WDF3Lm4-RtVzxg4vFmLnc3TkjR7nUpmCnUbFfsG6_s0exsCJwPvhtk9qkzISWsTFZEY6z2HHXFWujkxOBofUkqCz-urDvb80yiWQoKuhkEwq5a_mDrIG3C3txgjqgGPtFRorrfv7NTWNe3-zGOBKopjkmBH6F49YwtUb-0kaWnCZ1RuKr8RGybNvpQdBc7HRBuqxFE5gPR_A6bby0rI4anVJSWULLGfGFZtPIQ-r4n8Iwf-FQnuOi9h0yFJ9YcglkZiwwas84ZUaUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=hjWQ7ymlpT3uoFfLe8JX0pirLHi7whZtX6Zux0Jjj48cZsulkHcjFf-eWssAX8ZCWq4UXN52WDF3Lm4-RtVzxg4vFmLnc3TkjR7nUpmCnUbFfsG6_s0exsCJwPvhtk9qkzISWsTFZEY6z2HHXFWujkxOBofUkqCz-urDvb80yiWQoKuhkEwq5a_mDrIG3C3txgjqgGPtFRorrfv7NTWNe3-zGOBKopjkmBH6F49YwtUb-0kaWnCZ1RuKr8RGybNvpQdBc7HRBuqxFE5gPR_A6bby0rI4anVJSWULLGfGFZtPIQ-r4n8Iwf-FQnuOi9h0yFJ9YcglkZiwwas84ZUaUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
میزگرد زوایای پنهان طرح سقاب برای بنزین را هم‌اکنون در پخش زندۀ تلگرام و آپارات فارس ببینید.  @Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/456993" target="_blank">📅 15:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456992">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90fc52bf2.mp4?token=vso4TIHOWh7sYIB5bbYcPH66ngwq8MmV6uAMCAKB1lX8UF2TDzSeiOMptMY8pxqLWQBYsjPNbr6EJ8z8ctOQuVNeZ1uhhjaGK4_9ZvwZAyat6DUoUDkmqf80bnECSzdCxOiNC3CKy-S8xOKT3rf6WQKKWFPY_hTGKAwtPgT0lihJLpeooteXY036ny9Hz5G1khwPsPntUOj2BOwBFCK7k6VKBiX9O5gE33rrpLfFk5J32eD9VHcSLNBNziHe9wNB7VH4KJ_3AnYu9BQ0GXWeVUrkFrzrWy0iID9O0Sve7YzS_Zm1ADCC1RzP3qUnamWYmDJvCK1wg7dd9in306SA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90fc52bf2.mp4?token=vso4TIHOWh7sYIB5bbYcPH66ngwq8MmV6uAMCAKB1lX8UF2TDzSeiOMptMY8pxqLWQBYsjPNbr6EJ8z8ctOQuVNeZ1uhhjaGK4_9ZvwZAyat6DUoUDkmqf80bnECSzdCxOiNC3CKy-S8xOKT3rf6WQKKWFPY_hTGKAwtPgT0lihJLpeooteXY036ny9Hz5G1khwPsPntUOj2BOwBFCK7k6VKBiX9O5gE33rrpLfFk5J32eD9VHcSLNBNziHe9wNB7VH4KJ_3AnYu9BQ0GXWeVUrkFrzrWy0iID9O0Sve7YzS_Zm1ADCC1RzP3qUnamWYmDJvCK1wg7dd9in306SA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حنایی که دیگر رنگی ندارد
🔹
بعد از اینکه ترامپ، عمان را برای کنترل تنگه هرمز، تهدید به بمباران کرد، تحلیلگران و رسانه‌های آمریکایی گفتند، ترامپ آن‌قدر بلوف می‌زند که حتی عمانی‌ها هم چندان آنها را جدی نمی‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/456992" target="_blank">📅 15:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456991">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6047ef9a60.mp4?token=r4dFR4KzTjsIusTMERZE3bATZTeGL-chXBGrVD44dgPsDagsKxQ0miNFcp0e48_vxFrW59ZTWul_OF29vNTyIOJyXknOHgYBtkJBpAZju5Xx6Wtrv9LaF0D_XJxnYRlRgllAhnWDvyZ1xDAhR2-f-8blB7ZeZ1Pcr_F3Vh7GdxWeyK_fibkJe_lG1KoipQ3NwaoROZ_vkotvGE6ppOHRhycV9VUIzYKwDvFUGCcxJKgH9QJMmddKh1k5dn95h9-WgMHQPnMHKFPABvx6VGm70SCaRuv2XRpHLGdyJ2j9IBHSCgqaaG8O_jHuoiz4HGwQ_j6sTUYBUWFW5rgOr5XgO3Xal-vg1ElsMlcIqz8NCvnqDF3IN5XSBthsAJ4kiMAVb5VNjUcXNE9PtAFFr9n2jMN8bJs38Jrc9k-ARCEYeWmotsNjBnnHMbp2U-qCGR3_TEjSo9Md8v1hBAgkqhEgZ9xbPb-2Zofgr7LxhuLsmIC0b2Dfgy6oVfa0phphZpMXG4QfgNahAgm3EX_6P5tVnZWL2a0xVB8EstK4B5vzeMt_W0T-MjYTuhR0n73-YW4pGxTsedzSaHcwB5lI8LuiuoxlFXczYpD422p6_9UcZUPGCsxbjwFbfgi2X_aR1ESsrud9oUlJmvQ9OOTdxZLfnGiaBmRRVwdE62f-bp1Oth4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6047ef9a60.mp4?token=r4dFR4KzTjsIusTMERZE3bATZTeGL-chXBGrVD44dgPsDagsKxQ0miNFcp0e48_vxFrW59ZTWul_OF29vNTyIOJyXknOHgYBtkJBpAZju5Xx6Wtrv9LaF0D_XJxnYRlRgllAhnWDvyZ1xDAhR2-f-8blB7ZeZ1Pcr_F3Vh7GdxWeyK_fibkJe_lG1KoipQ3NwaoROZ_vkotvGE6ppOHRhycV9VUIzYKwDvFUGCcxJKgH9QJMmddKh1k5dn95h9-WgMHQPnMHKFPABvx6VGm70SCaRuv2XRpHLGdyJ2j9IBHSCgqaaG8O_jHuoiz4HGwQ_j6sTUYBUWFW5rgOr5XgO3Xal-vg1ElsMlcIqz8NCvnqDF3IN5XSBthsAJ4kiMAVb5VNjUcXNE9PtAFFr9n2jMN8bJs38Jrc9k-ARCEYeWmotsNjBnnHMbp2U-qCGR3_TEjSo9Md8v1hBAgkqhEgZ9xbPb-2Zofgr7LxhuLsmIC0b2Dfgy6oVfa0phphZpMXG4QfgNahAgm3EX_6P5tVnZWL2a0xVB8EstK4B5vzeMt_W0T-MjYTuhR0n73-YW4pGxTsedzSaHcwB5lI8LuiuoxlFXczYpD422p6_9UcZUPGCsxbjwFbfgi2X_aR1ESsrud9oUlJmvQ9OOTdxZLfnGiaBmRRVwdE62f-bp1Oth4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پویش ایران همدل به نیابت از رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/456991" target="_blank">📅 14:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456990">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ns0ngNzYkViUdIcpUvMbduBqcVCL77eLiqbXy6VpfMs-YERpUUwKvhUlkxH_DB3nsOkS4Jh19TB430kHZwf1ifWvr0ep3ahYRvoJhilkcYw-9LPLJH8Z3bYA8lsEnqtXWcqPvRSWQhMP6FGQHmEpawi1cQQzyfbFoKs4CzqIzBnTYYcQo_7bA7dmJaX0miODUwj9CpgjCj__Nz500U4iPHcWu402nVwlm_AIDM0w74veVTfYV_tUdIE4NdJLcm7RSp-I6m9GbRn7hlZjxTdz1mrqMU33Pk8CoSIx3b4geFeUpx-PKLWDt8J33knYGjTBUGm3UmiLEN8kkz2ZEwSJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
من در این مکان خطاب به این دو شهید عرض می‌کنم: ابومهدی و قاسم عزیز! ببینید ثمرۀ مجاهدت و خون پربرکت‌تان را.
🔹
بدانید که ما و همۀ باورمندان به مکتب شما در…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/456990" target="_blank">📅 14:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456988">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8iEWWPMZbDKckPlf9tVHTFkL1M3CS1mQQeqaFDhXGjpciUaRdV6_11z_FybWLx4kLq8FRW5jTYjvYpQmZe3QwGJ-17oqxnwi8zSjpfDbbxIcBhD0PRIObTktlo3iX_grdNb2tblqT85R4qymG-y2jj1vijKkKzP-QOSOFfz6i7Ulxwn5a0hUL9IO10uo5rlLy8NeDAvIPA4X0ZXWxy0IjqOxRBVZMVpI2rhGj5-86PaDzK6auxSO0wKdtKpngmo2pmwtnKLZO-_kZIpdKOYYJeFaeKo3OofoKjZPXc5AIdZtlaOmIFtBpqqySb5iKmDU_e3izQ4yegqSRmeNqlxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPjKWIG8I0wD7sPdiHrGUs62DI4wjjy9LE9ONlxiyFyDkKqNcc3m1rTK-o8GFfzcZfHmEiGaxsamxEng6DstHIrwV_JNGyIuacAWL-p5bCPREEOPCTqmCfGafxKvcT4lTsVjWdA6EW4C4pJfH7DCLndUuVMuWrk9hAE04COYaAFCyluctIYX8LrfahGaGGDrqQf3JVFrjnMb9K-KINUA5zFLIrm4Qijbfter8os2zEprQO6qaFhQ7PpX9yvUcXQw-cUSOYeiZgkAc2_O4Qv9JM0bnuuVlr4qDyDU95CjnHYYjtNJsx_Mltl9OR9-4V53Qr2Dzzx5LQzEn0vpUIOp6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر جنگ ترامپ زیر آتش تمسخر کاربران ایکس
🔹
افشاگری درباره مشکلات تدارکاتی ناو لینکلن و ادعای آسیب یا انهدام یک پایگاه مهم پشتیبانی آمریکا در حملات ایران، موجی از انتقاد و تمسخر کاربران آمریکایی علیه پیت هگزث، وزیر جنگ آمریکا، به راه انداخته است.
🔹
برخی کاربران، با اشاره به ادعای وارد شدن خسارت به پایگاه‌های آمریکا در جریان حملات ایران، هگزث را به پنهان‌کاری، بی‌کفایتی و سوءمدیریت جنگ متهم کرده‌اند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/456988" target="_blank">📅 14:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456987">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C16YMqX_Scq9lC_tSQGlaSTQoHCiYaq6sJrRKKmfuV5yQnQ_09yV9sTgVDgJkj7xgaPP0xC2c9p4DxT6IdmABqv_yPRNf6avyU8oCjsYhQA8HMGvUFLXT1SaVI3_Roau5fFB2tCQgGwdq1lJh7Zo4N1p-6OzhAg9cXVnAWnqZjbXM8aQsMhVuQvMPnWtcawbRYUgVQCUHCYPDSbQlT7Se0GWgG590oWx2WFPHxJ4yetMMUWen1xNZNdnlKqVmIbrA4Js4P-SXiTO3nhTK9uOQr9EU-SKGT9yu4XAlrNjyZsbMExYEHdm84W_rt9ry0lSEqePXcn565UdB4P-DafdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهرانی‌ها منتظر کاهش ۵ درجه‌ای دمای هوا باشند
🔹
هواشناسی تهران: با ورود سامانهٔ بارشی از عصر جمعه تا دوشنبهٔ هفتهٔ آینده و بارش‌های پراکنده در نیمهٔ شمالی استان، میانگین دمای هوا ۳ تا ۵ درجه‌ کاهش می‌یابد.
🔹
وزش باد شدید نیز در برخی ساعات از دیگر پیامدهای فعالیت این سامانه خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/456987" target="_blank">📅 14:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456986">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1faa4002b.mp4?token=o7E2A6XY9GaiJ3DODva9CeEIl4xsESFUQqWwyNHyA64EyhLy18mqorYqq-IBZaaKsCte-cGrQmfddXkSNJFoQJpt8jVd9Z7n-3LFYfFrShkwrX0R30Iiq-XNOeXciUCe68A0Y1D-HWGSfyrRVoAaE_jNXj20TEQUwCk3SAsb8hBaT2KD3pRw0-gcKg1aC1RfdDpvZKC-UbLk8AoxpxXgdnP7PHDcGRRQHLWHf4mMzjdNA7P6goDU4C0J3M1XNu_74sUINMwHaducZHbadyFacgrU79v0Oy6HdUSvek7hhh498I3CoCAtdyU_2Rgq5pbiLbMr68ySsi78xtyt6no1eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1faa4002b.mp4?token=o7E2A6XY9GaiJ3DODva9CeEIl4xsESFUQqWwyNHyA64EyhLy18mqorYqq-IBZaaKsCte-cGrQmfddXkSNJFoQJpt8jVd9Z7n-3LFYfFrShkwrX0R30Iiq-XNOeXciUCe68A0Y1D-HWGSfyrRVoAaE_jNXj20TEQUwCk3SAsb8hBaT2KD3pRw0-gcKg1aC1RfdDpvZKC-UbLk8AoxpxXgdnP7PHDcGRRQHLWHf4mMzjdNA7P6goDU4C0J3M1XNu_74sUINMwHaducZHbadyFacgrU79v0Oy6HdUSvek7hhh498I3CoCAtdyU_2Rgq5pbiLbMr68ySsi78xtyt6no1eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرگزاری فرانسه: تعداد کشته‌های زلزلهٔ ۷.۷ ریشتری اندونزی به ۲۰ نفر افزایش یافته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/456986" target="_blank">📅 14:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456985">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f286fec11c.mp4?token=po6JDMddRjLYyojh9EkZkdI2E89q9aLbnSzpp5xBNr1VH53twHDvxodto9NpssHawcl9dfIMIOpKegJA2gxZ-4dC2oc0-1tCWy6wrs0reo7a26xJVr9wSjhnIjfRgz9nN-EhhR8DmwmirxptKtx17EEbKnGSZh0M7RB7CROHYglyIVf6apmgMS6dZw_iHmHhsWoHivVfBVF4_avx2zrKmSMcNNbYgGwUBaBaLiSO-q-INJzkcr7nNB1jcZaUCcZPpzrd9hF2fGuHdCz2ZmZw-8sWMP0EexzV0mogR27jQae6zoSjvgBJDNOYGDZSuzD2KuRy5vXkfng5T6UTPyaZEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f286fec11c.mp4?token=po6JDMddRjLYyojh9EkZkdI2E89q9aLbnSzpp5xBNr1VH53twHDvxodto9NpssHawcl9dfIMIOpKegJA2gxZ-4dC2oc0-1tCWy6wrs0reo7a26xJVr9wSjhnIjfRgz9nN-EhhR8DmwmirxptKtx17EEbKnGSZh0M7RB7CROHYglyIVf6apmgMS6dZw_iHmHhsWoHivVfBVF4_avx2zrKmSMcNNbYgGwUBaBaLiSO-q-INJzkcr7nNB1jcZaUCcZPpzrd9hF2fGuHdCz2ZmZw-8sWMP0EexzV0mogR27jQae6zoSjvgBJDNOYGDZSuzD2KuRy5vXkfng5T6UTPyaZEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ معاون اول قوه‌قضائیه: تغییراتِ دستگاه قضا ادامه دارد
🔹
دادستان انتظامی قضات پس از بررسی گزینه‌های موجود ظرف همین هفته انتخاب می‌شود.
🔹
در دیوان‌عالی کشور نیز تغییراتی مدنظر است که پس از طی تشریفات قانونی اقدام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/456985" target="_blank">📅 14:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456984">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaFGVZTSEf83BqyqCLVXxJmnMqnOLKIjXHxgFAOz59uNrT4VlI6b6c4XyoosdAUyD5zgnsLsNmMt0Mxca5NzuoI2sTp8Y_hWCb-VZYj6_BXQaOvaDcgimRIsaPF6saeliALOMluDccMf1cFj6ds8Hwx-jmB1dmOI6tLOYK4LmmhAxvIPZnbkhAExobf-t9Ot2nNmfiVXn7-KdGHpStiCDjj1SfCXjpVPW7jhCt4Bt_lQD1mL3HQ7_c1zKEMYCsGQVZZciCPgDDSiY1fxDyKHgL16F30NKhobSVVzcCDobBt_wgWpa-uc21y-YofvxohMYoe3YLcdhuskJwkPwNpD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات فروش نفت به آسیا را کاهش داد
🔹
شرکت ملی نفت ابوظبی(ادنوک) درپی توقف تردد نفتکش‌ها در تنگهٔ هرمز، سهمیهٔ نفت صادراتی خود به مشتریان آسیایی از جمله چین، هند، ژاپن و کرهٔ جنوبی را برای ماه‌های آگوست و سپتامبر کاهش می‌دهد.
🔹
این کاهش بیش‌از روند معمول تابستانی اعلام شده و در شرایطی رخ می‌دهد که امارات به‌دلیل وابستگی به هرمز، با محدودیت جدی در صادرات نفت مواجه است.
🔹
براساس گزارش‌ها صادرات نفت امارات از حدود ۳.۵ تا ۴ میلیون بشکه در روز پیش‌از بحران، به‌حدود ۱.۵ میلیون بشکه کاهش یافته است.
🔹
حمله به چند نفتکش اماراتی و افزایش نگرانی مالکان کشتی‌ها نیز موجب شده ابوظبی سیاست صادراتی خود را بازنگری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/456984" target="_blank">📅 14:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NID0zgZQ_g8TVo4b5SMW8MNYA1Mky0KdAxk5RKpp35XAxAmcIFY_r780SYUkyvwmHpb95sxRoxJKYmbc7Pi1TlEaYyYgwFcJonC2ZbJGbJsQ3e9OIWyL-5pB-GgcaLGbAPPxiAEQU_pandvN1Gyn3ZaaaSJtIn3cGnz5M6PbS5FbQO4aAGtOXdZhmUTKfZa8WIQWlXGXHGzTjNvkq3WISE7Yh0QV2a1Z-Fx-8-PxqasA_Pnrflsm2FGH50JFpB_blZTmQJp5zNFwA1IDljtF9nSv5LZBvDKBelFUBI5FP3ajylMERdyNbzMKN0GR5GmfbcA1C49kfiNIoJVTUbEnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی بنزینی سقاب‌اصفهانی در توئیتر!
🔹
رئیس سازمان بهینه‌سازی در آستانهٔ تصمیم دولت دربارهٔ آیندهٔ بنزین، ۳ راهکار پیشنهادی را در شبکهٔ اجتماعی ایکس به نظرسنجی گذاشت.
🔹
این نظرسنجی پس‌از ۱۰ ساعت تنها حدود ۱۱ هزار مشارکت داشت که در مقایسه با جمعیت ایران…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/456983" target="_blank">📅 14:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">استقلال شهرآورد را به نقش‌جهان می‌برد؟
🔹
گزارشگر دیدار سپاهان و تراکتور گفته دبیر سازمان لیگ در ورزشگاه نقش‌جهان حضور دارد و دیدار استقلال و پرسپولیس ۱۱ شهریور، به‌احتمال فراوان در ورزشگاه نقش‌جهان اصفهان برگزار خواهد شد.
🔹
در این بازی استقلال میزبان است که…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/456981" target="_blank">📅 13:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ecfa62c1.mp4?token=Wo-uoIcpnfVd-f6f8_GNaPWc5yl1R8uNtCdbVjyc4S3Kp-De7zvEmQSc7jAO0NSuhn1N0a-9CMjaDD7BN1NgvzqdO23YV3-udYKYVgaFyabb-gIAT5kWCWeTKr4Z7B5sjpy_Y14jUqnhf619vTjuqQwqxlD_4J_Eusvj0X2tvLGkEUJZt1SoMhaTclhuJ9tI9OMTh9TozyTCAEuqOD9Z6wYDRuGgLj7WpHJGvojgKk-Gb_SsaSNaIfMwjmQCOjOckRocu0YaxRCA9Ll2l3aCiXv_5Jt8NXdUJCWL6wgauyFzw7YtYrhbKEfPEACVD6IAUr-tVm0WVdL_CGcselI0jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ecfa62c1.mp4?token=Wo-uoIcpnfVd-f6f8_GNaPWc5yl1R8uNtCdbVjyc4S3Kp-De7zvEmQSc7jAO0NSuhn1N0a-9CMjaDD7BN1NgvzqdO23YV3-udYKYVgaFyabb-gIAT5kWCWeTKr4Z7B5sjpy_Y14jUqnhf619vTjuqQwqxlD_4J_Eusvj0X2tvLGkEUJZt1SoMhaTclhuJ9tI9OMTh9TozyTCAEuqOD9Z6wYDRuGgLj7WpHJGvojgKk-Gb_SsaSNaIfMwjmQCOjOckRocu0YaxRCA9Ll2l3aCiXv_5Jt8NXdUJCWL6wgauyFzw7YtYrhbKEfPEACVD6IAUr-tVm0WVdL_CGcselI0jIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عامل حملهٔ تروریستی به دادگستری بهبهان که عضو منافقان بود دستگیر شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/456980" target="_blank">📅 13:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456979">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKNRBEf5AMKWpwaiM__J9T0ftHCnhajDidYGW84uBkSEZakN1al1y3TlSDnFQfXWm1wEpc2khpwRjiuZQ-egsXbz91lrZNaxBDq9limh-JulslbdUQJJf7PG5B5-1H35lhXABkhF5bLPX_7y7JSfvzYCJT-UP_Q2l-R3TAZFLDl8n7aGSqyEvmRLBX993supsz8LjpPI_-qw7sY2L7pZrmuKnS_rm9WY6EhkOGhdt7YYpZEyC-8_mRW0IroP8qkGbJytpoEJ25PB31Z3INXE7c9dur2PMC3Ibw1B8LO8d6CKD47S0VldXmyfvQ0BD5sTb187NwZUTIb7By9-5d1K6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌خبری از ۹ صیاد بندرلنگه‌ای پس از پنج روز
🔹
فرماندار بندرلنگه: ۹ صیاد بندرلنگه‌ای که پنج روز پیش با ۳ قایق جداگانه از اسکله بندرکنگ و اسکله گشه راهی دریا شده‌اند، تاکنون به خانه بازنگشته‌اند.
🔹
احتمال تمام شدن سوخت، نقص فنی شناور و یا گرفتار شدن در شرایط…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/456979" target="_blank">📅 13:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456978">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Iox4nPuyE1PFLJtOPCVU1eNSceQOubHJbPnZ0dtIImlgtNt8K3s35cAwbtoU2zdnT6NOp34zqaW4se_v2Xyzn7Vaz9V-buYD5A8Y-HjNNmSsGe1AFFVTrWULQ05T5u65DMzMY9iFVMQ8cFc0pEtxjf8q-tlu3HNYx7CxJPi68uRXJQY_2W21rFKcb1jszoLPJDgl_1jlnqhkrJtVn9Hu4bY8Zp7KRChM9oBM78_AVpL_YbK2UI3e2xc6XoK1iUvixNDG8NJWVHCjVWwE1bjC9ZXpI0LPMXqoIgDwvHTxJTSsqXkFw4kn_UxTzu1ljA1w25Bln1bojh1LcaE89Ptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز
ترانزیت ریلی نفت عراق به ترکیه و افغانستان از کرمانشاه
🔹
ترانزیت ریلی محصولات نفتی عراق به مقصد ترکیه و افغانستان از طریق راه‌آهن کرمانشاه با نخستین محمولهٔ ۵۰ هزار تنی آغاز شد.
🔹
معاون امور اقتصادی استانداری کرمانشاه در مراسم آغاز این ترانزیت گفت کرمانشاه با داشتن ۶ مرز با عراق می‌تواند به حلقهٔ اتصال شرق و غرب در تجارت منطقه‌ای تبدیل شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/456978" target="_blank">📅 13:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNj5ssiG0ZlekMFM2UFlwgkiBczQCXN3jT1SRnAnkWoQaNcM3oCfEvreJpTNougG7-2GnLk8An4pyXXyYc_RgpIcQc5dZhtArdnMhlTYfDCbwyF3oV-LZ6QTScLnLTRaqoQSwXNL0wmGkPO20EWyCkfU23tsCY3iIum_JQpzKei3Fb6p3VKBDvJjeWbFyIzgNQHCxlmcc4K4RxtU0rxxRXpPKXuxGt6fdlggi49ESrIe0bMsqIoE4KBaIyNxkE-8xZNWmenHKxOtJp5mKAQMQ8-Wht87KMl1uJzrXBqq8rmwGek0qCjbI9pT0B061hU6NNoCo47BjnJVjw-izg-RfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
پیام تبریک مدیرعامل بانک رفاه کارگران به مناسبت فرا رسیدن سالروز تأسیس این بانک
🖋
دکتر اسماعیل للـه‌گانی، مدیر عامل بانک رفاه کارگران در پیامی فرارسیدن بیست و هفتم مرداد ماه سالروز تاسیس این بانک را تبریک گفت.
🔹
در بخشی از این پیام آمده است، شصت‌ و شش سال حضور مستمر در عرصه اقتصادی کشور، برای بانک رفاه کارگران صرفاً یک سابقه تاریخی نیست؛ بلکه حاصل بیش از شش دهه خدمت، تجربه، اعتمادسازی و تلاش برای ایفای مسئولیت در قبال جامعه کار و تولید و پاسخگویی به نیازهای واقعی اقتصاد کشور است.
🔹
در این پیام تصریح شده است، بانک رفاه کارگران در این مسیر، همواره تلاش کرده است متناسب با تحولات اقتصادی، فناوری و نیازهای مشتریان، از یک بانک صرفاً خدمت‌رسان به مجموعه‌ای توانمند، رقابت‌پذیر و اثرگذار در نظام بانکی کشور تبدیل شود. افزایش سرمایه و ارتقای توان مالی، توسعه زیرساخت‌های بانکداری الکترونیک و خدمات نوین، تقویت ظرفیت‌های فناوری، طراحی و به‌کارگیری ابزارهای نوین تأمین مالی و حرکت به سوی روش‌های کارآمدتر و غیرتورمی در تأمین مالی، بخشی از این مسیر رو به پیشرفت است.
🔹
در ادامه این پیام خاطرنشان شده است، در شصت‌وششمین سالگرد تأسیس بانک رفاه کارگران، ضمن گرامیداشت این مسیر پرافتخار، از اعتماد و همراهی صاحبان سهام و تمامی ذی‌نفعان و همچنین تلاش صادقانه مدیران و کارکنان بانک در سراسر کشور قدردانی می‌کنم و امیدوارم با اتکا به این سرمایه ارزشمند و با تداوم رویکرد تحول‌گرا و نوآورانه، شاهد نقش‌آفرینی هرچه مؤثرتر بانک رفاه کارگران در خدمت به مردم، کار و تولید و پیشرفت اقتصادی کشور باشیم.
#دکتر_اسماعیل_للـه‌گانی
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/456977" target="_blank">📅 13:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6kYcDejaPX5Itbs2XDMT9nGbeAxIHkrF2Cat0qb1UUFCLWujAMVl_XLI9zUPZIGiex-x-4UxiiU8RxiOOUSxgVqBFwENHscuahHVUd7VZCIlV_Tp5weYOoB1DIwfE7zi1OfmpE2zVN6l7xqYVCeXkOs33C8m-AOgxA9H0RdyK4JnDI7hoh-TVqx5Gn3h6ulymIlzMiufS-Kxn5sDvfCBYgiDqCnwEV10ERZjdf-B3AY1r-Od2GXZ4UdwJND1efsyhLUIfJ3AUak1ONJv7Ah8I_MQ8kKQf0Ma7k3_Yl9Zlmu-Shn7h-qlG-d-gzVt-c2bcdeIUKW4pZiZ8gEoP5Gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرصت همکاری با گروه فناوری غذایی شهدآوران
🚨
پذیرش شریک توسعه بازار و نمایندگی انحصاری در شهرستان‌های سراسر کشور
🍯
سبد متنوع محصولات غذایی
📍
فعالیت انحصاری در محدوده تعیین‌شده
🤝
حمایت و پشتیبانی شرکت
📈
فرصت توسعه بازار و درآمد
اگر در حوزه فروش، پخش یا توزیع فعال هستید، با ما همراه شوید.
📞
09398260904 | 09103470429
شهدآوران؛ طبیعت، سلامت، نوآوری</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/456976" target="_blank">📅 13:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/456975" target="_blank">📅 13:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4BuBv742qL8lNoLEXRee33jpEgk56-gy7CT1GgTl8vIq0Kc3UH-QMtJL6xREdUSzRtzrvDLmKivIxy4QLXEh9JFOJOrWQfh5qOl5CXPD24KhObrM0oDePduOZ7gTVoU7-zpw0IF2RaIo8TzTUnizfQ_AdFLKW5daykub9JrhSRI9v8wVDNIrcqlwdOisNXu8Qi7ho6xhtJvIrbtCNDAbSNK-X0FwLJs0MREL39ZRv1L4X3PbLJm1eYvv3154OGMC06yXAF1wss8yUCJ-PnBbbtHdmp6Ji5EP7OM-GeowmBhfYol3YCFo-SxNr7LrnxwjXtLGXguyuf7NF0po2-2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش سهمیهٔ بنزین کرمانی‌ها به ۱۶۰ لیتر
🔹
شرکت ملی پخش فرآورده‌های نفتی کرمان: سهمیهٔ بنزین کارت سوخت شخصی شهروندان استان از ابتدای شهریور به ۱۶۰ لیتر افزایش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/456974" target="_blank">📅 13:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456971">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm8sEFWz1PPdJroyfn1J5-MfoiCQyMTSWLwlP-MLvKgDKAxvFYQXZTTH5ijBPPGRxiFbHemb-kWOTti-70Qa8fwO5WmVLPdRyUrM-R0nX_rTfx9PhD11yduptobvMlGbBJnFlmHmr5wIPbMpj9oParHSC9qiHoUnFisWWjkhtJDkEisxuptlgZ6V5gK1Q2RqHqcqRJH5FnWjrv9jiomFbHx0QJVH5-sVFdlH2si64tqz5WCcBrXb9nMoXJaaeqi9ZHP1dQShaTgpF-hIz3wlxFC_l0gamRwCimRk9OmKo2a3p689xYRFlgMdKeHH2WgMySLvMfC9E2AlQzG0dW1b9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJiq1mi9gD01iQYHdzI9lPPJBKzAsN68wraSX39AGCr5sLi4lqsIGjv4dosPeR30JxioDR0mDaDzAs_aGlZLeOPcXDchm907n_Yy5ePINcc0-ki0qLmy5dtkbrxQ-_FSXTkCd2xqgibtAjzpplcsQAAWSObK1bH56XZ8YxFRA2qGD3bxM5euI-DPPFp-hP7lxlv1d87O73i64ZA_A-70knZrkTWDEVkBjYbuE8LKwQRURckZbK-mxywF6v-O7ZO0vZCUY7fdd2s5ISNH9AM1nG4N-fB1cm5AJqZFeKwupuOYw0JdO5ZbtDH6tB2JF0L4iixxuGqvQzI_IV4ewDjNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snNgWoHU7cj8fhUq8tvvrPTkWNg89HYuJmdFMuCEWOw6jjDQ8CE66nrou8eNBqMQdVmGTMlUoYr92uUfFkaa05CxZEEzHlRim_7NOh0GfiS0rublA02BgsxCoad7Bsn3fpuvG9Tr5h1-b0ueOw58fKtkkN55JZAmFQAtAy9XDVjLJ2acKEnAbaBTwZ-GT_3_htdZOM_SjhfzcVbjJeT3S_E5_We0xp5v401-P2JTOqZKJievw2mhscHmK9KXmZhfT765aGtBWceDa58o7wx6LZqC3URv1yR5oR6pqh91otsLbsmI3FzoMhfnNh-oxfT_0nszcQUyr9YtSkw-v1xU4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
استقبال رئیس‌مجلس نمایندگان عراق از قالیباف در مقر مجلس   @Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/456971" target="_blank">📅 12:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456970">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TImsPh0jTRXxai0J7___tPBJEvZ5t0sOaFfECSjfSlujsIUXUOZGP_DqahGqvbYqVPnwymvYLKzKjOOKTRzpUBoBlzNTJZP8sHOnNRdgE-RLcc7GbkGEotjbbNs0Z7HZuKhzoshyzdfSKsBqJ7DfsR9d2fVlkmuSDmeBAfpnHMnsQAYW6zga1svIeHIDPQ4srrURv6aydURuzkU4_sqlebHsM0YWvD2SN8ryNydlsalQ30plWwNYVanui6LH7dY7l2w80cpwm76TQUlalakrZk3nH0Yg79JzsPAPCdukjkTz9nNeYDYHRmKhN8wIDEbztHoyIkP64DWQ9xFRYFnGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۵ هزار واحدی به ۵ میلیون و ۹۵۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/456970" target="_blank">📅 12:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456969">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2318efe0.mp4?token=fqhHRxxUzq6v62zlgIiL6kuXoRfFHkEw5mBqEH0OXc1gxsUZH7A9ri0OewHhyQxgTs84TRHM5q5eCMHbEEnlsdZ7tnr5Oo_EPH1rbrS-JmVQusAoblFA4EOHDDHJ4DzlgasPPRC-QDq7EczwmFdhHBy22GPbKev3kboPyKOI6NtvIN0yBh55y38hhQbpwpyL7g881zbC51zY2TBVAt12cvGK6Xn8-7sciOPpaSwXAsibRrvVduBaL0ekvQK8D7vOLJh-uxE1lJOvb-81ZSrRzBd8H1oGOMomhbRpG-L_r-g8ta4V7vi4VEtAalAT4MNOJEApzjMRF_DG_VAoI88ZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2318efe0.mp4?token=fqhHRxxUzq6v62zlgIiL6kuXoRfFHkEw5mBqEH0OXc1gxsUZH7A9ri0OewHhyQxgTs84TRHM5q5eCMHbEEnlsdZ7tnr5Oo_EPH1rbrS-JmVQusAoblFA4EOHDDHJ4DzlgasPPRC-QDq7EczwmFdhHBy22GPbKev3kboPyKOI6NtvIN0yBh55y38hhQbpwpyL7g881zbC51zY2TBVAt12cvGK6Xn8-7sciOPpaSwXAsibRrvVduBaL0ekvQK8D7vOLJh-uxE1lJOvb-81ZSrRzBd8H1oGOMomhbRpG-L_r-g8ta4V7vi4VEtAalAT4MNOJEApzjMRF_DG_VAoI88ZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: به‌عنوان یک مسئول خجالت‌زدۀ بازنشستگان هستم
🔹
نایب‌رئیس مجلس: برخی مدیران با گران‌سازی به‌دنبال عقب‌نشینی ایران مقابل آمریکا هستند.
🔹
در شرایط کنونی باید تمام پروژه‌ها و منابع کشور را با اولویت تأمین معیشت مردم تنظیم کنیم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/456969" target="_blank">📅 12:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456968">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UINI2aMzZlUWvu4NIXqbx-6HBI0Z3L8hZw8GelLWf8H95P9SZRi-r6sJPKLbOc4bZ8RoDw0WlCNiaf7JkVBKJjpjDgZQ51OTqSNDhIka0NuSpb3XpRTjtVs2G_QHdC4II-54rITj4k31u6B4sUcIT5_XkMhii9YvbQh-nsplEtq6Tq6IRtSwZ67HifRN94pfSHPEYr6r6ksfUuYj4QKQjhfCC97_wFbrG9skdmMJpXyKwHuTyK8mfsOAa3ir2KcMSmjzZwNpjuEuPiXxIvrleEhKaunFLNeZhABN_EAAQqvsZPxjG_BQgbKyL_PH9O3Ho1pcyMViFTubcMQ2wvt9CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حملۀ دوباره جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در سوریه
🔹
منابع عربی از حملۀ مجدد جنگنده‌های اسرائیلی به فرودگاه نظامی ابوالظهور در ۷۰ کیلومتری مرز سوریه در استان ادلب خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/456968" target="_blank">📅 12:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456967">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVn4wnPrzDknzh70N8_ZQpuFfl7GTdCUKUCccaWsgaJ7gBR6gf2sT-uiN7TQuw_NCNNxxC51F2XNPXdGKaPf_ppWu7PRje3JCvJAfybdTge_Cpv0L13gK56IcITuM9vF7WTxxg8L3CeImijDFQvrZ0isQeu4m-oTzonruN2f7XeZYNHRaTlsHqMqehVwGyvObs8TncMA-xcZkj-ICTd7pFUpImbIcFsshP1zbixuu0cM9f9G2RVQQOfMjEBQa8Iv-XEmpZog05EUOVo9VyynexKVgQT2O6RritJ9r7SURvES46N5o1korZJrDF84WRHEnTJPwTmZiZzeJFfxJC1Gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن بانک اهدافش علیه عربستان را گسترش می‌دهد
🔹
درحالی‌که یمن به اعمال محاصرهٔ دریایی بر کشتی‌رانی سعودی ادامه می‌دهد و در واکنش به تشدید تنش‌های نظامی، شریان نفت و بنادر را هدف قرار داده و تهدید کرده که رویارویی را به مراحل گسترده‌تری پیش خواهد برد، روزنامه «الأخبار» لبنان از منابع آگاه مطلع شد که نیروهای یمنی ده‌ها هدف حیاتی دیگر در جیزان و نجران را به بانک اهداف نظامی خود افزوده‌اند.
🔹
حملهٔ دیروز که به‌گفتهٔ یک منبع نظامی در صنعا با تعدادی پهپاد انجام شد و واکنشی به نقض حریم هوایی استان‌های صعده و حجه توسط عربستان بود، در چهارچوب سلسله‌عملیاتی صورت می‌گیرد که از ۲ هفته پیش آغاز شده و تأسیسات نفتی سعودی متعلق به شرکت «آرامکو» را از جیزان تا نجران هدف قرار داده است.
🔹
در همین راستا، منابع پیش‌بینی کردند که این عملیات در جنوب عربستان در دورهٔ پیش‌رو تشدید شود؛ امری که واکنشی به افزایش حملات توپخانه‌ای نیروهای سعودی به روستاهای مرزی در استان صعده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/456967" target="_blank">📅 12:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456966">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca9db56.mp4?token=Cb9f4SrBZ7bp-nPY_tFRud0eHOX3Y3xW2JZHq7fLqzNN7Afnt2rouqWNiPgV4J1d40TPar8ACg3r7HPcd44AWxpUhya2tjGtcs5TQ2RIGenI5NHNngoL5ckO8EbH0hDAv2QFvCnELrGCi8NAAkUIUUwUaUTvi-rrFTa-Xe8-r7dRCk1SygGdhcGUu3B66ahVPMmWGIZJtN4iKV6AOv4ZqTl1RFuHsijPMc3R7xEQ3tU8nmtwnKtkHzDeujJKwgVHtNrK828X8Szd2_3oEwpIePqXeHQFRP7DP5kRCSsSIrpL0yn2fv96EASRtRUkhsnzNLiYxFd1cIk332TAEEq4Dl2-dPmXyv3vVjctXbFuCC9ral_QIrpnF43AIhwxBgYNe23KIU619SCPaKBflLOaCiit6WyFBHQkErHHPdD8Pq3BDigqORaF73fYYZUjYONFY7AnO-7a3eqghYEtf2ljRVlwWwKmDOWdkTsbKAF_lRnhjh-A8o4acSb24plLO2_VfvrmCbL-sLzI0TvXdGGZ-wWZWjOlXSsUzSzk6xCY3jB_x72nt8J-4iDKLYQ6eJPPJAGPPTfrT-YG_kx7ibHjOFvUTStoROcWxsF2V02dDUZYdZzwpnaO7br4Told95M-EaW9VnM62ZDpr8BZP2BNBH-SKMVq2eL9ROJCW8zteuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca9db56.mp4?token=Cb9f4SrBZ7bp-nPY_tFRud0eHOX3Y3xW2JZHq7fLqzNN7Afnt2rouqWNiPgV4J1d40TPar8ACg3r7HPcd44AWxpUhya2tjGtcs5TQ2RIGenI5NHNngoL5ckO8EbH0hDAv2QFvCnELrGCi8NAAkUIUUwUaUTvi-rrFTa-Xe8-r7dRCk1SygGdhcGUu3B66ahVPMmWGIZJtN4iKV6AOv4ZqTl1RFuHsijPMc3R7xEQ3tU8nmtwnKtkHzDeujJKwgVHtNrK828X8Szd2_3oEwpIePqXeHQFRP7DP5kRCSsSIrpL0yn2fv96EASRtRUkhsnzNLiYxFd1cIk332TAEEq4Dl2-dPmXyv3vVjctXbFuCC9ral_QIrpnF43AIhwxBgYNe23KIU619SCPaKBflLOaCiit6WyFBHQkErHHPdD8Pq3BDigqORaF73fYYZUjYONFY7AnO-7a3eqghYEtf2ljRVlwWwKmDOWdkTsbKAF_lRnhjh-A8o4acSb24plLO2_VfvrmCbL-sLzI0TvXdGGZ-wWZWjOlXSsUzSzk6xCY3jB_x72nt8J-4iDKLYQ6eJPPJAGPPTfrT-YG_kx7ibHjOFvUTStoROcWxsF2V02dDUZYdZzwpnaO7br4Told95M-EaW9VnM62ZDpr8BZP2BNBH-SKMVq2eL9ROJCW8zteuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله مروی: مگر می‌توانیم از خون امام شهیدمان بگذریم و انتقام نگیریم؟!
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/456966" target="_blank">📅 12:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456965">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUWLhGBnlRHYRaXGxdpG4z2750UvE21zi21DJCQ1bALuXfPOQ6vJxYu25S7_rjbO08XCrCmqTGbKlvBhAVWNNw2smlLFCAWaToGT4PwDzklZ_hm14oGSDS2LaKrvkOuqw9WUWgMmoy85Ce7DX9hc0RVxg7X-4EISCpPLmtAj91CawxeX9oyDbG4PnnNGgD97H-b2-7GFONGXUg5SwMoQfrHkyXZxv1aa_n4G6twjII1a0YmfoOgarREjwHxRo7QdqN6vonVGsRPGsJbWdDKWmulzBVVUh0kRhjM8m5omgaucH3tJsPboeUTv5flrVKhxXW7rGUdZqw3WbbCjI72fhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار سرپرست وزارت دفاع با خانوادۀ شهدای جنگ رمضان
🔹
سردار ابن‌الرضا در آستانه روز صنعت دفاعی، با خانواده‌های شهیدان دکتر مظفری‌نیا، دکتر جبل‌عاملیان، دکتر کریمی راهجردی، دکتر ببری، محمدی و جعفری از شهدای وزارت دفاع در جنگ رمضان دیدار و گفت‌وگو کرد.
🔹
در این دیدار درجۀ سرلشکری شهید مظفری‌نیا و شهید جبل‌عاملیان و درجۀ سرتیپی شهید دکتر کریمی راهجردی که به تصویب فرمانده معظم کل قوا رسیده، به خانواده‌های این سه شهید اهدا شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/456965" target="_blank">📅 12:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456964">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=bxsW7PnVP0Hk7HDi7jGqEGPhzegl5Ba46kiOIOymxjTTm4IVJ8gTAHDifmUEvC1E5Ij3EekoorRnJEkQQQDV-6wAVVGJI5Fb914Gj45Vv8Hfgs4cuiyq2f_M1_cxV89FBbXkHCaZX5BWa5woT-WV9oLQBxsqBi0xZWeAtPl7l9htyAgQ4naVX7Wlis6laJ5uOAAKQojeyuxoTnG6aBLqY-KLYPY_6kN38jtrhQU5XmHAw4fcxYDBvZ0QxHrwgrJCSAsYSZtjxsgvQSW_gig4BFQ_RfSEPXG-gVGpHBFM-iSlg4K39rc9XQS311KYxZmqfccDN_J-w0gWZQnnYfswFiymEiA8YncFDZ-2Yfx_OynzNGta7OC-lFGlgTmFpqF5BKtrwbsBRGLhRoJCAKTzHXcYEA-pQPn3JLeXRPbwjjs-gVQLCUOS_4fRVUkhaLwWun2g8e9bG6Vpoz3YFtn91saSjjhg1eBDaa9eivUqnvvBun2yST9NKhx48gftDMQI09CfCigJ0qoszVlDiVvV0Uil1cU1NlLM04hbPWMS9o0x0DrzXfvp9foaw09aZ8RX44NkL7HyG7GWknsJcpJX9muQwWlFasaG9oOIelfwGOWbpK43kKoM2UVE14e-mDi9ifkJFS0UOWQqrBhpUHtoVQz_qj2KxSXgIAM4GQP-nLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=bxsW7PnVP0Hk7HDi7jGqEGPhzegl5Ba46kiOIOymxjTTm4IVJ8gTAHDifmUEvC1E5Ij3EekoorRnJEkQQQDV-6wAVVGJI5Fb914Gj45Vv8Hfgs4cuiyq2f_M1_cxV89FBbXkHCaZX5BWa5woT-WV9oLQBxsqBi0xZWeAtPl7l9htyAgQ4naVX7Wlis6laJ5uOAAKQojeyuxoTnG6aBLqY-KLYPY_6kN38jtrhQU5XmHAw4fcxYDBvZ0QxHrwgrJCSAsYSZtjxsgvQSW_gig4BFQ_RfSEPXG-gVGpHBFM-iSlg4K39rc9XQS311KYxZmqfccDN_J-w0gWZQnnYfswFiymEiA8YncFDZ-2Yfx_OynzNGta7OC-lFGlgTmFpqF5BKtrwbsBRGLhRoJCAKTzHXcYEA-pQPn3JLeXRPbwjjs-gVQLCUOS_4fRVUkhaLwWun2g8e9bG6Vpoz3YFtn91saSjjhg1eBDaa9eivUqnvvBun2yST9NKhx48gftDMQI09CfCigJ0qoszVlDiVvV0Uil1cU1NlLM04hbPWMS9o0x0DrzXfvp9foaw09aZ8RX44NkL7HyG7GWknsJcpJX9muQwWlFasaG9oOIelfwGOWbpK43kKoM2UVE14e-mDi9ifkJFS0UOWQqrBhpUHtoVQz_qj2KxSXgIAM4GQP-nLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسگاه پلیس ترکیه هدف پهپاد قرار گرفت
🔹
طبق گزارش رسانه‌های ترکیه‌ای یک ایستگاه پلیس در استان «ترابزون» که در ساحل دریای سیاه قرار دارد، هدف یک پهپاد قرار گرفت.
🔹
«ترکیه تودی» گزارش کرد که این حادثه دیشب در منطقهٔ آرسین رخ داده و تلفاتی نداشته است. فرماندار ترابزون هم پس‌از بازدید از محل حادثه گفت: «اطلاعات پس‌از تکمیل تحقیقات در مورد منشأ هواپیما ارائه خواهد شد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/456964" target="_blank">📅 12:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456963">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiljTbsKTV5U3hageZ0KHLlAZmaUZbmfNk20xhZXeyTiVdjv60IbGNTazVxr8f8o_pq56lrUVesNyI8YqArEV4m1oHHFhYqO77-AmqxcjhqVGGS18paojRn5-7JrkISZM2ItQTW8RLnG4TADGDceKo-WH2Y-n-CCxDA0MDoMt4PC1rf8J1CwKRMIhQi0P2Xh949CfjNGi_I7yrL3Ht3pcmUD2qt3PM09ObbEJUCSPW7vq03yGunXN1sewmMXl_pfnGvHd5H3fw1FiQLo_gzAJ3lVjW1TVR_zpZjaPuLiWFwu29Hvg2kpsREwHE1K6zj3kM_nkfDG7z0Cg12HPGKV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکسازی داده‌ها در دولت ترامپ؛ صدها پایگاه اطلاعاتی آمریکا ناپدید شد
🔹
دولت ترامپ در ۱۸ ماه گذشته دست‌کم ۲۸ مجموعه داده فدرال را به‌طور کامل حذف و ۳۳۸ مجموعه دیگر را تغییر داده است. این آمار بر اساس ردیاب جدید مؤسسه
DataIndex.us
به دست آمده که تغییرات داده‌های دولتی در بیش از ۶۰ نهاد فدرال را بررسی می‌کند.
🔹
بر اساس این گزارش، داده‌های حوزه سلامت بیشترین آسیب را دیده‌اند و حدود ۴۰ درصد از مجموعه‌های حذف یا تغییر‌یافته را تشکیل می‌دهند. بسیاری از این تغییرات پس از دستور اجرایی ترامپ درباره سیاست‌های مرتبط با جنسیت صورت گرفته و برخی نظرسنجی‌های مراکز کنترل و پیشگیری بیماری آمریکا، از جمله سامانه‌های مربوط به HIV، مرگ‌های خشونت‌آمیز و خشونت جنسی، دیگر اطلاعات مربوط به هویت جنسیتی افراد را جمع‌آوری نمی‌کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/456963" target="_blank">📅 11:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMIsDSrxwOWwclmuP-b-RF3f9HMBHPAjgYOXUhQxKMX_diwezhNSolXN-AYWttDXCn9qGKrkYoqwR9nbtY5I_SRqVWqY-YKLg0I_LbFhGZ_MulwbWHPX7f7gl4cMF72QviAqwWSuQ1iRbqMs4EJoUM621t17WhnxmfFBVnBg2j8dJQNGS0OSoBtDbg5FKzRDbT2u0FuV-I5RAkb-KnEVk5h3nNmazs37RCQ3knyAZS5wZdLcFZrd3N791tiDSvC2Tizk02tsJfj1kZE5Wxrxkw9Mo8dJa_mUq1eVP80Ik4UC0BcHf7yZWSfTEIsiimQ2g3WX3ItpI0XlO68Dv6JOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شفاف‌سازی ایرانسل در خصوص نحوه محاسبه مصرف بسته‌های اینترنت
ایرانسل در یک نشست خبری با انجام تست‌های عملی در حضور خبرنگاران، شایعه کسر چندبرابری حجم اینترنت بین‌الملل را تکذیب و نحوه محاسبه مصرف بر اساس تعرفه‌های مصوب رگولاتوری را تشریح و تأکید کرد که ضریب 2.7 مربوط به اعمال تخفیف برای ترافیک داخلی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/456962" target="_blank">📅 11:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آیین آغاز عملیات اجرایی ساختمان اتاق بازرگانی جلفا</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/456961" target="_blank">📅 11:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/456960" target="_blank">📅 11:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456959">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4iQ9httf_qkDKa64_RG5TEtkgjD5mlLTT3I2H1k1vrwT7EZtNkAvRhLz9yz1H8c7aakLbiN-cAw3t6vLABADHS2vLOGsi4Erryz-SVsRt0KBshgBiNPEDzo0wF5NP2msnks8npEmJFk9lE71zv9_uzPHf9ijrlj0pviHNTJAou951cTMlwuZ_w1vDZozQqUHqi6f62M8vetb0vzoI02M5qfFPM2PBNo1l2v-aJUuLKStExUNENVSfgQZ2H65X-xEfGTJok-mZOp0qLVF-Tr8xg4Ox7vortoCBg9UqMl0iaB0gnPY8HVll3CifbDOH_tNMb7GtvtpNcv2v58RQyPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق صنایع آب رفت
🔹
حداکثر تولید برق نیروگاه‌های صنایع تابستان امسال با افت ۳۳ درصدی، از ۴۴۶۸ مگاوات به ۳۰۵۲ مگاوات کاهش یافته است.
🔸
۱۴۱۶ مگاوات برق از دست‌رفته، ظرفیتی در مقیاس مصرف برق خانگی کلان‌شهری مانند تهران در اوج تابستان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/456959" target="_blank">📅 11:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIklSPvsnqlhF3XZSPUf2aY_btgF3iFX1i59Jm6-R0ZNFhhpMzV_QefeHvoKJkp4ZOxcDc6wgYFj3mNLbUzpRe2rXqxxDjeaCfXcEIF5BunpM5mA0V1V-9bUX6nBk2bjcQ86nTYjyJycNrQCOowPoxdBStoRuw1mCOIf4HiUu9ncUXmwE-KhwqCU3nuZS7Alc3lRsutlCCH_5xNX5iXMhg6Wf_0mbcIy-wCotBmtfolfEd0cog9UPruRkLjjhgjWtc4ouARCMgnk37Wa-ou0uvx1y-QJWq--3rXXx7elXTRKC9MQ8TM900fzvvamr1vaMkf5-9H0ptGsVVT4WpXtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4U81f6A0lWOvURx-psixl4ufNyEhSL8BQy9K44WzlZ6mNOjWMeVvNEuAYI7nG7TH6prPYjjySbnVHk9HiosAT4csEY6QY_OW4fd_Cpa4ONZKWCFwX1jznYe_esIn1riuwhr67DqcvJ9wzwN_P9BUmiing53PxnXqeZV_t3r6xBRdBgtpJoM_BKyCl73lNWdxQ06TzjUT75otdtesVYSFeOOHoFPRWVA71GkuMXWlgYSTBCBzwOku2qX6ZJ7z59w2xlrYfejxGFiIsjU0QBYfqvuFbQFWkQzkAmxytXlu0N-EYs-d-59tsFOU5KEGE9gdYLDMRM6fmy6TQqIlqjoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDNgxDXa8F8M1cTfRJVsuXFDhlbXO3f6ihncnFZ1CeRlV5wl2Z8HdDu41wbkcta_z4LVsEJsJR0JlDI58KMzL-v0ri6I8xuM0OUAEqfPn0opYEJF36ggE4sBY7_2BQPTHki28B_OS_axo2vQIH-PxCoRdZgINfMpYmUHcSNmbc5i8GK9v_7aqCoLbGCuL18L3aPWg6K4Yb-dbkuFqVfb6zrHjrFxNJN0CVvc-rmIlj6FOYGelj6V4oT7nMcVLoEfWr2fXtL0QDiGgj_PCS3kmQBrtoSeDtySiSVcRc6LeP5JBwq2xpdsVHkisJySvFLo6BWzeKUomke_CJLwqrXcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gP6ZK0Oeu25uS3g01rBNwbvjmudVOKoL39IekIqmJ5fV7h90Si-u1B4sdDc0MvlJrEJ5OZWpl2hbAn47z1MFIzoc2Nd9bJL84LP2ttVd00tPbHVL6ZDCM2cIlFEUQ9iwT15McSxeI6cnsOr37psY3H3ZXTc7AYdg4ViJPXX3-mhfjt80g6Wbg3PdHgPbcfutwhQyaTATzWJhe8cvxPuREA_209xaDYn-6XkQlAPeYNnqeahO6Tn0obn-_MmAwX7SDn0Uge8XuIwwYCfuPf6jKEArrXu_hybBwLjlj3evm8THStJjTbS98Wbyi9N4PkLGI-TWTPuBvKpRaOtDwZ9sTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قالیباف: اینجا نماد تقابل جبهۀ حق و باطل است
🔹
اینجا جایی است که دولت تروریست آمریکا به‌عنوان کانون اصلی جبهۀ باطل، زمانی که دید نمی‌تواند جلوی تقویت و گسترش جبهۀ مقاومت را بگیرد، دو تن از مردان بزرگ جبهۀ حق را ترور کرد.  @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/456955" target="_blank">📅 11:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456954">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌ روسای جدید دادگستری ۹ استان معرفی شدند
🔸
آذربایجان‌غربی: محمد علی‌نژاد
🔹
ایلام: جبار سپهری
🔸
لرستان: عمران علی‌محمدی
🔹
خراسان‌شمالی: مسلم محمدیاران
🔸
زنجان: محبوب افراسیاب
🔹
کهگیلویه‌وبویراحمد: محمدباقر نریمانی
🔸
چهارمحال‌وبختیاری: سیدحسین حسینی‌وردنجانی
🔹
کردستان:…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/456954" target="_blank">📅 11:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456953">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌معاون اول قوه‌قضائیه: در ۱۴ استان هم‌زمان جابه‌جایی و تغییرات مدیریتی درحال انجام است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/456953" target="_blank">📅 11:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456952">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCoJRn5MYeJdXAUPXfxUfgnyZoUfkytIDqnPBJGf97AnM-Yk5FQsiEIMi1vxltKWT2X0-9LAWsCPAAq_MEHLsDS2LZ2tW1KpmwdpDCKm-KxFFZC6uhie3fDS0qON873I3GMtqykw7UnMXxtmogJ94oPG6mAT4SKpzFWjQm78SbI88R3VrpLL7W-DCce8muTPd9FRQ5JO2c0y4X0jE_PXipsKKqtGZwYd_HvoAJvwzyQB3Ko4EzRrIgnFdfCe80_-fx2yr-wTwnrY-IPDdNhYWQWne5RYJGZjZwse64-LfZx2Ev1qC-Y9njZsky8rqRGkDVOsR2tBf-wdV1Fu9rwPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیران جدید دستگاه قضایی معرفی شدند
🔹
ناصر عتباتی، رئیس دادگستری استان تهران
🔹
حیدر آسیابی، رئیس سازمان زندان‌ها
🔹
اصغر جهانگیر، رئیس سازمان بازرسی کل کشور
🔹
علی دانش‌آرا، رئیس مرکز حفاظت و اطلاعات قوه‌قضا‌ئیه
🔹
نورالله سلطانی، معاون قضایی قوه‌قضائیه
🔹
امیری‌اصفهانی،…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/456952" target="_blank">📅 11:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14759aee2.mp4?token=bvyelO3NXLRolNZDxPQ_bMjOzM73ch9Pet7jBVDe8Gjf8gvQ9uS82vNbLOBG9WIhFyyiw3M_ORNcTrmmB_ObKreFrvyqL2AuEwyNFwwDQo16lG04BSovbxOLHmZCETUje8Zr2-Jk82kOn_64ERDYYPya8o_Bs6qhtG8kozCYhdCQ_vqwyShOy6ztYNxLMekN7yFVHhunrQf8dWEem6RnqMYundaZqlDgC8wndj5Rke1YLOFynlxbYvtKEfTL0sPda28lBjqYk3Fug73rZUZnORvDZtyOTSOS6CjyyTLvx_UZTjWbP5HlO6flebYDOHfj6-mz-Vm80CfjtNhEdsZLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14759aee2.mp4?token=bvyelO3NXLRolNZDxPQ_bMjOzM73ch9Pet7jBVDe8Gjf8gvQ9uS82vNbLOBG9WIhFyyiw3M_ORNcTrmmB_ObKreFrvyqL2AuEwyNFwwDQo16lG04BSovbxOLHmZCETUje8Zr2-Jk82kOn_64ERDYYPya8o_Bs6qhtG8kozCYhdCQ_vqwyShOy6ztYNxLMekN7yFVHhunrQf8dWEem6RnqMYundaZqlDgC8wndj5Rke1YLOFynlxbYvtKEfTL0sPda28lBjqYk3Fug73rZUZnORvDZtyOTSOS6CjyyTLvx_UZTjWbP5HlO6flebYDOHfj6-mz-Vm80CfjtNhEdsZLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری یک حیوان‌آزار در تالش
🔹
پلیس راهور فراجا: پس‌از انتشار فیلمی در فضای مجازی که در آن یک خودرو در تالش اقدام به کشیدن یک سگ کرده بود، رانندهٔ خودرو به مراجع قضایی معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/456951" target="_blank">📅 10:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456950">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
اژه‌ای: در دورهٔ جدید قوه‌قضائیه انتصابات جدید انجام خواهد شد
🔹
برخی از افراد دور همین میز ممکن است به‌دلیل ایجاد تحرک، جابه‌جا شوند.
🔹
شخصاً پیشنهادات افرادی در دستگاه‌هایی خارج از قوه‌قضاییه از جمله سپاه، وزارت اطلاعات و برخی مسئولان سابق در دستگاه قضایی…</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/456950" target="_blank">📅 10:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456949">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">منبع نزدیک به تیم مذاکره‌کننده ادعای کاخ سفید را رد کرد
🔹
درپی ادعای کاخ سفید مبنی‌بر لغو مذاکرات با ایران تا اطلاع ثانوی، یک منبع آگاه نزدیک به تیم مذاکره‌کننده در گفت‌وگو با فارس گفت: اساساً مذاکره مستقیمی میان ایران و آمریکا در جریان نبوده.
🔹
گفت‌وگو برای اعمال حاکمیت بر تنگۀ هرمز با کشور عمان برگزار شده. پس از نقض تفاهم‌نامۀ اسلام آباد از طرف آمریکا گفت‌وگوها با طرف آمریکایی متوقف شده و گفت‌وگوهای اخیر نیز با طرف‌ عمانی ارتباطی به آمریکا نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/456949" target="_blank">📅 10:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456948">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuSaV_QL-NVVJ0iQqax4VymhNgYjvjmCEYYsnClotboAA6oeWzjJJt3buEnJ-ZU136pZfuAcPTknPn8mclEUfEKQgyNiMi_7P9Fs7zJGwxmpVhPOYBszDVKYBTheL8iVzhtNR2wBC1xLHLLk2rypp4c93qXMOexXIqDg2yLpycjIlqrnG-97_3JpEm-y0NUt9DpUMZQ3OVcfm6MbFNUX_IDChUsZUn4qa5x9lD_dnFHC-_rkflrPZmYnfOzAzus9dXiZdwEPQ7f6fBWqeWFAvYaI_PnxIuPydW-DlRaSQA354PttY0GJGp4fhCs4TcC4VhyvBPlmM36nPZyp0AHHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصمیم جنجالی دولت برای سرنوشت جمعیت ایران
🔹
براساس اطلاعی که خبرنگار فارس کسب کرده، موضوع تغییر ساختار ستاد ملی جمعیت در دولت مطرح شده و قرار است این ستاد منحل و مأموریت‌های آن به مجموعه‌ای در دل معاونت «امور زنان و خانواده» ریاست‌جمهوری منتقل شود؛ موضوعی که در صورت نهایی‌شدن، می‌تواند جایگاه سیاست‌گذاری جمعیت در دولت را با تغییر جدی مواجه کند.
🔹
البته هنوز مصوبهٔ رسمی و علنی برای انحلال ستاد ملی جمعیت منتشر نشده و باید منتظر اعلام رسمی دولت ماند؛ اما اصل مطرح‌شدن چنین تغییری و برگزاری جلساتی در دولت، آن هم در شرایطی که کشور با یکی از جدی‌ترین بحران‌های جمعیتی خود مواجه است، پرسش‌های جدی ایجاد می‌کند.
🔹
چرا دقیقاً در زمانی که نرخ تولد به پایین‌ترین سطح رسیده و خطر سالمندی جمعیت هر روز جدی‌تر می‌شود، باید ساختار متولی جمعیت تغییر کند؟
🔹
ستاد ملی جمعیت براساس قانون حمایت از خانواده و جوانی جمعیت ایجاد شده و ریاست آن بر عهدهٔ رئیس‌جمهور است. ترکیب این ستاد هم نشان می‌دهد که قانون‌گذار، جمعیت را مسئله‌ای فرابخشی و ملی و حاکمیتی دانسته است؛ پس انتقال این مأموریت به یک مجموعهٔ محدودتر، بدون آنکه مشخص شود اختیار و قدرت هماهنگی با سایر دستگاه‌ها چگونه حفظ خواهد شد، می‌تواند تبعات جدی برای سیاست‌گذاری جمعیتی کشور داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/456948" target="_blank">📅 10:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456947">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKuu7bwz2c4Yg5vomdw-5gnA1_yPRW6F_uLPc127PwA09vdH1dwuga1cbziv_sNx8oO4nZfgQTn3rXbkk6K8ioIWL6ydirrG8aE4MwlescwyZUS88H4qdiH8JlqPiUJuTdhZlfbtyG6UGVxR57JWk0sMk-0lqj1rK64xU5Kd060yB7FfJ1F-4315-b9XAKbPlusQ2dQjMNrHvMEgmO34Z2KL8EbJwhplKZ2mID-WWAd9A46UvPu04GcKR4igP3toGJs3c4Oor9ZoDYasWms9r3S6ijHj9Io33g0L3F-Dfud1aY-re5-w3pAcydeQrcrw8sHvhaCs-5dn-7lIuN3s7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رالی صعودی نفت آغاز شد
🔹
هر بشکهٔ نفت خام برنت امروز به ۹۱ دلار و ۶ سنت رسید و نفت وست‌تگزاس اینترمدیت آمریکا ۸۵ دلار و ۳۱ سنت معامله شد.
🔹
نبود قطعیت دربارهٔ وضعیت هرمز و به‌صفر رسیدن تردد نفتکش‌ها در تنگه در هفتهٔ جاری همزمان با تداوم حملات به کشتی‌ها در دریای سرخ، مهم‌ترین عامل فشار بر بازار نفت در روزهای اخیر بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/456947" target="_blank">📅 10:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456946">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b698366e68.mp4?token=Qxphj4AMj4qKV8Cu_HvX9ef0Ec8jYPEnSdbMyGZ5c48wFYxcoSWL4cx9jGQCZo9hkG1TvTla80G4TYtYBnrB26XrE48pm-zr7m6b4MZJecHIB5c_kPPgSmfv_DrNcdUEB7cMFwAk229p-BB02KgBMK5kPCOg9dnUD68PQbiTQkXmhzsjis-RhDpjfSd7xEcvFpLSHyHeYTRJW8XEL06pTheWVlm86mS7ngWzVhIZwzGlAjud0iW1xmFtQzAKaBJASf6QhmOHArBREshs1P9gOzZ7DtVClot5plouvYhU0vkuDbTqOcyZZcleEiA_SGX1xdFrmN7_AcQ8scHNQrLKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b698366e68.mp4?token=Qxphj4AMj4qKV8Cu_HvX9ef0Ec8jYPEnSdbMyGZ5c48wFYxcoSWL4cx9jGQCZo9hkG1TvTla80G4TYtYBnrB26XrE48pm-zr7m6b4MZJecHIB5c_kPPgSmfv_DrNcdUEB7cMFwAk229p-BB02KgBMK5kPCOg9dnUD68PQbiTQkXmhzsjis-RhDpjfSd7xEcvFpLSHyHeYTRJW8XEL06pTheWVlm86mS7ngWzVhIZwzGlAjud0iW1xmFtQzAKaBJASf6QhmOHArBREshs1P9gOzZ7DtVClot5plouvYhU0vkuDbTqOcyZZcleEiA_SGX1xdFrmN7_AcQ8scHNQrLKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف خطاب به حاج قاسم و ابومهدی: بدانید که تا به نتیجه رساندن آرمان‌های شما از پا نخواهیم نشست
🔹
من در این مکان خطاب به این دو شهید عرض می‌کنم: ابومهدی و قاسم عزیز! ببینید ثمرۀ مجاهدت و خون پربرکت‌تان را.
🔹
بدانید که ما و همۀ باورمندان به مکتب شما در…</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/456946" target="_blank">📅 10:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456945">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60f37010a.mp4?token=QLK6NUsPJD5O33qJX5hp-urfC4z4KeiwutMKPCsPEwSGVGOb5r0ScwgLN2KJ-HJysc7ZSVWPYFxQr_FLEyG5bdEAnRbZG50KBE0V9O9Jsrxo3Fvvj6s3OqoUNt7IVOh-9USK0T92RHQw6EP8pEoO715o_ufGl5unDD80sDIJ7jVjMa0JwW5fxdfFv7ESZ-1NLOkRAiaBz6bOoOYgWt1Irh_e3ADeD2RdsYyEqn3Vg9KbhgNZ20qkUIwHHC11SciOolZrdycKDI_ZJNgMkfwu02NDMXeyj5cEnNPdGk-I10PHgCxiCpX6yFlqWaHYrrdadvBDwGy10PqGTXm7IsRMRRO5rmDfYei7egfqZ7UnEoI0_EWBh02fHyRTFdmjnleFgg7K2nSe2PavSy1bnmSSkhYI-pvLhovanZJxocwx8TFQN7wbfJU-hWm42ipw835ocUK5Uh1xPd1eedbpZOaoroYn4v6cPFpdiVygWN-8LCmaSRFdqbthS5IyZ2pbcNGT6_rHnieYhcamXmqKzPZGLAR1SaCiTABkIQ9Q8tknCOWZ5Vov8Ljtw1Ea59BgJ55NM89_jhNTmeLO28FCL50xTXakkuhZTCiaVJVuOFdTUrpPai6eZn9EU-eGkGqiUSUnMa3I5dU8rCqqoV7CmKdTVgEKqRfekwsJu6-aQs2UpzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60f37010a.mp4?token=QLK6NUsPJD5O33qJX5hp-urfC4z4KeiwutMKPCsPEwSGVGOb5r0ScwgLN2KJ-HJysc7ZSVWPYFxQr_FLEyG5bdEAnRbZG50KBE0V9O9Jsrxo3Fvvj6s3OqoUNt7IVOh-9USK0T92RHQw6EP8pEoO715o_ufGl5unDD80sDIJ7jVjMa0JwW5fxdfFv7ESZ-1NLOkRAiaBz6bOoOYgWt1Irh_e3ADeD2RdsYyEqn3Vg9KbhgNZ20qkUIwHHC11SciOolZrdycKDI_ZJNgMkfwu02NDMXeyj5cEnNPdGk-I10PHgCxiCpX6yFlqWaHYrrdadvBDwGy10PqGTXm7IsRMRRO5rmDfYei7egfqZ7UnEoI0_EWBh02fHyRTFdmjnleFgg7K2nSe2PavSy1bnmSSkhYI-pvLhovanZJxocwx8TFQN7wbfJU-hWm42ipw835ocUK5Uh1xPd1eedbpZOaoroYn4v6cPFpdiVygWN-8LCmaSRFdqbthS5IyZ2pbcNGT6_rHnieYhcamXmqKzPZGLAR1SaCiTABkIQ9Q8tknCOWZ5Vov8Ljtw1Ea59BgJ55NM89_jhNTmeLO28FCL50xTXakkuhZTCiaVJVuOFdTUrpPai6eZn9EU-eGkGqiUSUnMa3I5dU8rCqqoV7CmKdTVgEKqRfekwsJu6-aQs2UpzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویری از ناتوانی تجهیزات زرهی ارتش صهیونیستی در برابر پهپادها را منتشر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/456945" target="_blank">📅 10:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456944">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVwTU7GAcRWNuijulrTufhMAFaN3whYAaRCFVdQeQcsQxRF3N7av2x61MdSUDkl0Ptteti2vjwlh8a9uIta0ojvZCzvLeVYEGHtuH4bRfcN_-rpHKsAjI3Cnl12qDRGrregHmvRNeLSv16V2Exyua6wrqp8Miz-3-7hRuzgfqeYfaXOI_lWJzk8e6UqhdVm96wMX8CDybtWs2PV05-bgvBbdWA8azpBqepz79mO1O87bX7rfE45Poz40RRT72cK19y6IEJlwYDLMMnNZZLmUUIPJ6Az3YJZb4ZHn6G4f-Vl_wYGiEeauUj7bvwK9hjN3gYuJfyDhdZDN_sYXN0V9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژمانفر رئیس کمیسیون اصل ۹۰ مجلس ماند
🔹
در جلسۀ صحن علنی امروز مجلس، نصرالله پژمانفر با ۱۳۰ رای در ‌ِسمت رئیس کمیسیون اصل نود اجلاسیۀ سوم مجلس دوازدهم ابقا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/456944" target="_blank">📅 09:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456943">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۶ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/456943" target="_blank">📅 09:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456942">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2mTzGHfmicRFhCWZYPJVNOti79mztDUakB0NjOROz4k_685DFLnZqmKr5ghMZ4aIjomEZb_9heIeOgJw2XxPOnkNF8gHXPUjCh1pQNe0-i6vuHh7cOUAAZwB65G_1RBHBnviro4ULL7_dXRBbO5vGgTfs-UyzcBY7NwcKsp8e065KmiE39nfVQOVs8IweX6XugY6s0M7VrZwQA6iiR0cjsclxDLLtgwXsM0gisukH0fvXsAtTX2L1RUZGqTUFb6-V2ClrQ0v0qBFj3cFYi7PQwSPTf95eaqQJrtlRvhPgJjgtcxJKP_ZXcZJXmYnmQmcfGmPa_YbOVdakP89oHOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: چین دارد کانادا را تصاحب می‌کند
🔹
چین دارد به‌طور موفق و کامل کشور کانادا که زمانی بزرگ بود را به دست می‌گیرد. دیدن این اتفاق واقعاً ناراحت‌کننده است. فقط امیدوارم هاکی روی یخ را دیگر دست‌کاری نکنند! @Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/456942" target="_blank">📅 09:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456941">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=vQq-__c4xvb8bXDnn6bHA9fEgwL3StJYCu6Pf9DuCJm_APWxuL3YPX1VzQ_sh0lSmM5D65v9Aqnjr5aj1tmRYaiVV6yIf_rSFT1giHGUKIzs4aSq47Os-ibiunIENKVO_wB87POmyjbh2NLmYbW9n7r3aZaw74pUmHZlWzZ6drkTuDgjXZbZbSnAUESNiR9C2yGlxec4jhekfIxpBFim8fTp-iiRO8YlPgqBvPb0y-vehpXPOX5PxnM17t4xUhmVWrNCRzUvnXW8-kU5Fx_FKoSEEkb9AnfjsTFIFgZdEVvoz4KrqNRFqiANmoFiHak9qUr7xMvtm3OPbrwNEc0z4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa069a80.mp4?token=vQq-__c4xvb8bXDnn6bHA9fEgwL3StJYCu6Pf9DuCJm_APWxuL3YPX1VzQ_sh0lSmM5D65v9Aqnjr5aj1tmRYaiVV6yIf_rSFT1giHGUKIzs4aSq47Os-ibiunIENKVO_wB87POmyjbh2NLmYbW9n7r3aZaw74pUmHZlWzZ6drkTuDgjXZbZbSnAUESNiR9C2yGlxec4jhekfIxpBFim8fTp-iiRO8YlPgqBvPb0y-vehpXPOX5PxnM17t4xUhmVWrNCRzUvnXW8-kU5Fx_FKoSEEkb9AnfjsTFIFgZdEVvoz4KrqNRFqiANmoFiHak9qUr7xMvtm3OPbrwNEc0z4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ادای احترام قالیباف در محل شهادت حاج قاسم و ابومهدی در فرودگاه بغداد  @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/456941" target="_blank">📅 09:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456940">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe28ef4b47.mp4?token=jjhczC0kw6mw8iphoKshNpEUFmpZahd08PGBa19G0gKq-lcFlK7gI1Q2KpTbgzWeHmrgvdVeub8gh0jinGrvKiQ8GDAvpiwXumOI5-y9kHcQ4eMVNYmZVfuWG2KybuoFTN3URviSIvzZ_7ANLjgSyt7IvqyWe9c0tX17T5X36gf8WS59WNKr0WFF4fKdeP-U7GVJ9EY_lnNhSRUAtjiDwCmnXTk7nKESNT4JGJalunineLx3sxpf38KRJe04vcyxHlXDGdgrCK2pxonrHf3jIWB9v6jmgQwNjFNBSkOjwevN_HdDPqA9_HxYq0D-EiEMRXVKAkNk30lyyEEL2Hgrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe28ef4b47.mp4?token=jjhczC0kw6mw8iphoKshNpEUFmpZahd08PGBa19G0gKq-lcFlK7gI1Q2KpTbgzWeHmrgvdVeub8gh0jinGrvKiQ8GDAvpiwXumOI5-y9kHcQ4eMVNYmZVfuWG2KybuoFTN3URviSIvzZ_7ANLjgSyt7IvqyWe9c0tX17T5X36gf8WS59WNKr0WFF4fKdeP-U7GVJ9EY_lnNhSRUAtjiDwCmnXTk7nKESNT4JGJalunineLx3sxpf38KRJe04vcyxHlXDGdgrCK2pxonrHf3jIWB9v6jmgQwNjFNBSkOjwevN_HdDPqA9_HxYq0D-EiEMRXVKAkNk30lyyEEL2Hgrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان سنجش: در کنکور امسال ۶۵ درصد خانم‌ها و ۳۵ درصد آقایان شرکت کردند
🔹
امروز آخرین مهلت دریافت کارت کنکور است. آزمون فردا و پس‌فردا برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/456940" target="_blank">📅 09:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456939">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">محکومیت ۷.۵ هزار میلیاردی برای یکی از متهمان پرونده‌های کلان اقتصادی
🔹
رئیس دادگستری تهران: در راستای اجرای منویات رهبر شهید انقلاب و تاکیدات ریاست قوه قضاییه مبنی بر حفظ و صیانت از حقوق بیت‌المال و دقت مضاعف در رسیدگی به پرونده‌هایی که با منابع عمومی در ارتباط هستند، با قاطعیت و بدون اغماض در دستور کار قرار دارد.
🔹
کارگزاری بانک کشاورزی دادخواستی مبنی‌بر مطالبه ضرر و زیان ناشی از جرم علیه سعید جابری مطرح کرده بود که پس از صدور حکم اولیه مبنی‌بر بطلان دعوی در دادگاه بدوی، پرونده جهت رسیدگی دقیق‌تر به دادگاه تجدید نظر ارجاع شد.
🔹
دادگاه تجدید نظر با بررسی دقیق ابعاد پرونده و با عنایت به سوابق محکوم علیه در محاکم کیفری از جمله اخذ رشوه، تحصیل مال نامشروع و ابطال ضمانت نامه‌های بانکی، ضمن نقض رای بدوی، حکم به محکومیت نامبرده صادر کرد.
🔹
فرد مذکور به پرداخت مبلغ بیش از ۷۵ هزار میلیارد ریال محکوم گردید که این مبلغ با توجه به لزوم تعیین آن بر اساس شاخص اعلامی بانک مرکزی، در زمان اجرای حکم محاسبه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/456939" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456936">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKra7DQc1ZGXg81trWZuoswzPMfTe9nEQylQY3brx1NfqymbPmDubG1npvk2PVXjGFomI7BZZStfN0Ffzb3v_fwMa0cpKWbBWACLjJXaM5PoHC21sQbSKg9L4PnvpjCwZ7lrL2Do3jN_rPp5WPPfCQhFWus98iKe4Fl7EuoPVA8aF6NZAZjQ6ZzrPPxXXVvy2cAqEb37z2qNqrzlhCD6p_mUTNLRtoEM3S0WKO0GCgw3IVIn209ViCdUyR9EOk8TAXP6MVMqkXV2RoTcGZpJ_GqJjGC58SAo-vcK5sEoDB-PkTRP3SsS9_Rt1TL0Maf9Q1iqjUEvln2fisUfVfBUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2vtHlD0kPrbXhmn5w1I4M3i9W_gWusep3f5-KRdqQeF5Qwg9dndJqFTyVOeVMHePw2w_VChS70c0b0MbW_yrjZ_JmFoG1bfLMpCls8JVIcKzfozJQJt5rZmQakjYYmiFNJV03NgNIgje2xqVOd-sbH4_ZNctsn77FKDIrC_6-bfnsKzsy5jk_RSABk21QQE2XoppjVlkExliZm7gjJPGIgpGX8ZSNBrDqra6aFEMc3V7Cxwqjl0InlrR_okYBbWsjiIBJcL-E8GdQrVTq3enuEZsgr10Yr0msiJ6AnbnSvy0Rc3HFW19Z_xJyvAQx6eQhw3sLlbAcZSez0N1fg8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8zGB401EC02XwJdSsCEsr7aAsUlQAHoS7cILIgKLnpJatxuDNhLwjy-HpN8AUuCdsL6QxoGYtbi_uKcHhq5VUeGy1tuE51gWKmHz82cr-fwCPdcOJMVtAvAMAFqaZdz4EMG_k5j8jwClIakLOv2hhIO-dmBmXfWwt5woyWS15r-oBOVL7EKcA8qwlTDR_HTkSvimMArra07GcvH4R7wjR_sBxapQgrcqC2ZTusZ4a1v0La0SE-F6Mg75S16bAqhFURnnMOQmW40aJed6jkIVbZtO86iPFOgASHUkZhwDwkxrhhdV4hw-5323RekNuoZujztsvcFXvYuXA4yzoqGVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: شاهد نظم جديدی در آینده منطقه خواهیم بود
🔹
در سفر به عراق با شخصیت‌های بلندپایه مانند رئیس‌جمهور و تعدادی از شخصیت‌های اقتصادی و فرهنگی عراق هم ملاقات خواهیم کرد.
🔹
به نمایندگی از رهبر انقلاب در مراسم چهلمین روز تدفین امام شهیدمان در کربلا حضور خواهم…</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/456936" target="_blank">📅 09:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456935">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB-z1M_xZzhSy1_qNC9cwr0hsegDE88mCvvekC14CtewwzJQL1qD9ZGqPuDFextZw3NknuKwyw-uajKNk9eMpbsOmO2O3pIh__l1URgcb7eRSv9s0hvhS8HhDfWHh3vTbXfzAqOWjMjQzctx-nz5dejwBhQsRPiG-2BC3KsaIqxaeR0-hX6ydFBteOIP9SnbiZHyl1_cWXEBRYLmRIVgb2YjhGIi8g0yk167veWef95qJ06RrSJ324FfsT6Pfb44PZSk4vPoVD1zV-Gzz7AecR_E6K9jAsjpELTHp2Y-2vjxoW4qs2e-8xbFOa05pNyxinmyKucrl2AI8lFsk2nGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
هشدار رئیس ستادکل نیروهای مسلح در خصوص کمک به ارتش متجاوز آمریکا
🔹
سرلشکر عبداللهی: کشورهای حاشیۀ جنوبی خلیج فارس که با صدور بیانیه‌های مختلف اعلام می‌کنند اجازۀ استفادۀ آمریکا از سرزمین‌هایشان علیه ایران را نمی‌دهند، باید بدانند که چیزی از چشم ما پنهان نمی‌ماند.
🔹
این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.
🔹
هشدار می‌دهیم: هرگونه کمک و تسهیل‌گری به ارتش متجاوز آمریکا به منزلۀ مشارکت با نیروهای نظامی آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/456935" target="_blank">📅 09:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafae608c2.mp4?token=WJ-94JCorE9gPr-T2ZNPWxd_fkjdP9AoDuqL3QBNQdj2Xsghzp57IylzG_yqG9m7cktxFMztysBZGODYo60OYAZSlWYg6uudiOVm8e3IRq7PJIwtmhBnYcc98O1pLTPHIVcpcJ6BKp2YZmkl2B6lHkXDmq8nZtMNrCYtW1bb4HTDXh8JzluU3WCF8_tlmz5fFBNZs3bCGH_3zheMlvD4KgeBfQx6ugHA1TWPg6POF_Ufjf70qwkU4MJ3PvF6Vx2-zjLUkUKa3TsP4xU-YocMU1rnqm92G6dce98Axjl_l6kb25ywwvJ6MztpeOrJsm8cosfh6mUZ6S1xUjm8o-1SAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafae608c2.mp4?token=WJ-94JCorE9gPr-T2ZNPWxd_fkjdP9AoDuqL3QBNQdj2Xsghzp57IylzG_yqG9m7cktxFMztysBZGODYo60OYAZSlWYg6uudiOVm8e3IRq7PJIwtmhBnYcc98O1pLTPHIVcpcJ6BKp2YZmkl2B6lHkXDmq8nZtMNrCYtW1bb4HTDXh8JzluU3WCF8_tlmz5fFBNZs3bCGH_3zheMlvD4KgeBfQx6ugHA1TWPg6POF_Ufjf70qwkU4MJ3PvF6Vx2-zjLUkUKa3TsP4xU-YocMU1rnqm92G6dce98Axjl_l6kb25ywwvJ6MztpeOrJsm8cosfh6mUZ6S1xUjm8o-1SAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز توزیع کارت کنکور ۱۴۰۵
🔹
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت کنند.
🔹
آزمون تجربی صبح، هنر و زبان‌های خارجی بعدازظهر پنجشنبه ۲۹ مرداد، ریاضی، فنی و انسانی صبح جمعه ۳۰ مرداد برگزار خواهد شد.  @Farsna…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/456934" target="_blank">📅 09:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=IWPkf3OiWCfppHDNWPmav_1DRRc-mlZhUhJsmaIlKe-SEQN2OBDWCThrmhTw_10W1ywaly4qKIZ-uh-ZkhfO4C3bt2SVGSYuRowzbt3W9TgCDNzsEQbjs07nVnE5YxrlAcxvANqjoLXGXtlrivN7UvZdLFFLPwh_LfXV2Tp2SIhGY3Z7-QHCv6Ls3yJn25RSjVpYG_NtGmDwsoGYVRsczyHRrLj1vq4qAfqMYtGqWu85TjBsfMzP5Wye_u2GyM3mV_rYR494yJkJUKMyH9cFaKVhAXIbSpRh5VlyQP6jjDhldhIwxAzvt9J8WPKsOmi-NV-ZtIVxPP0wcBjA27FHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=IWPkf3OiWCfppHDNWPmav_1DRRc-mlZhUhJsmaIlKe-SEQN2OBDWCThrmhTw_10W1ywaly4qKIZ-uh-ZkhfO4C3bt2SVGSYuRowzbt3W9TgCDNzsEQbjs07nVnE5YxrlAcxvANqjoLXGXtlrivN7UvZdLFFLPwh_LfXV2Tp2SIhGY3Z7-QHCv6Ls3yJn25RSjVpYG_NtGmDwsoGYVRsczyHRrLj1vq4qAfqMYtGqWu85TjBsfMzP5Wye_u2GyM3mV_rYR494yJkJUKMyH9cFaKVhAXIbSpRh5VlyQP6jjDhldhIwxAzvt9J8WPKsOmi-NV-ZtIVxPP0wcBjA27FHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: به نظر می‌رسد از جمعه به‌بعد تهران دمای ۳۸ درجه به خود نبیند
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/456933" target="_blank">📅 08:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456932">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwukuWqxcpu0CDvSZ4UsbFYdfm74Ry5NvGdaq74mgZWCDcF9d3KGjBA1GJOT03-UvO1P0jElaOT8hGCIgoXjtL03NngHvT88yx9LCuYCGcuN3fdXu_jeQ2bVpBTdN7pruIld94b9TkjHMImQQ8-vaoujt5l-6En82EZa-pV-6kDjisXIznaHWoJl3shuGg66WXefs3zxey54K5lb63JMx2TzYiP_YddAyXN6BCbN-VTL6Tr8uikmJoUM-70VA5mPTrdnirpy3sep17fKsCjlAg2KZLUH7jBFnZwqXjT1mjl3B_alXC1BKZMAp7dHIQa6vxsJ0lDxcwC0eisYRZ_Tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف عازم عراق شد
🔹
رئیس‌مجلس با هدف گفت‌وگو دربارۀ تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا، تهران را به مقصد بغداد ترک کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/456932" target="_blank">📅 08:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456931">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlWjV9KBqiEpou_LcgCNEdgIfzN7C-qCwIY48tghfJ1f_eOWyzkQUU1uoerNgEoBqUEhrd4-Wkkq7N5_P_Ag9oQknglveUL8egTE8qdxrP2Xv1q7SQGDVzTMxLNRlwzNkZqV9KDgJsic6XQ8Csofo4JVd3Tz2hTT5vpqCYyRoZyLzZE5ARxGuVhdLOayIUADWptygE37lBqf6yGB1-0VK915XfH0hJds7vWz1BPMHTcYPidNsknBiKmHQgPVXt52oUG52j2ny7j9_77H4LKw0nD4j5XWEhtFlry-nCxylUGLeCGvo3KDif9enLs7W_rOcLvsHSaOERuxJMNK0Sl4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول نفت آمد؛ مخارج دلاری دولت تا دی‌ماه تامین شد
🔹
طبق اطلاعات کسب‌شده از وزارت نفت، ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفته است.
🔹
این رقم ۱.۵ برابر درآمد نفتی در ۴ ماه اول سال قبل است.
🔹
طبق روند بلندمدت هزینه‌های دلاری دولت، این رقم کفاف همۀ مخارج ارزی دولت از تیر تا دی‌ماه امسال را پشتیبانی می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456931" target="_blank">📅 08:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZcDBrGwT_fVD67TIBhEt8goZR8hgck6opbQCArOZJBffWnsoWZ3jVoc3A39N0xzYOSTCWiBxYzOmadXcSjOFoJsVKecYaWzncWtZxGJRubvkN2qU7BJiSOiKEeZfPbQoiXkKeCnemKHIA6rknd-fxUamQO82tpEvrz77Z46dPg6SNtM2SaWrFgGyB5LdCrvfL7V8PkeRBZQSrtLeDwnVcMeOK0L_sxSG0HGF9Ha8f1e2lZ5-hksnRMErQ-84XZLaiu5mo3rLFpfmvCcKR9oKFsClfWiulQv9NTDFaAXxrdE-CmKx2C4idCm-OylAfnyIldFXKMjAYMTY8AKAiJ8Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش توقیفی امارات در راه بندرعباس
🔹
براساس اطلاعات سایت‌های ردیابی کشتی‌ها، نفتکش توقیف‌شده در تنگۀ هرمز به سمت بندرعباس تغییر مسیر داد.
🔹
مقصد این نفتکش ابتدا بندرجبل‌علی تعیین شد اما حالا به سمت بندرعباس می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/456930" target="_blank">📅 07:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d41vgMQ0uVOHrON17QO3NyM5fO3Cfdw4vq60KmoA27MwtoI0oLBsxwntuh3PsyxqwuJ7z3x9MpeGH60KeCtl-CZ7bH0gM6yhPRDduPtvL2iihnKfM3FvrVM8HBkvXcJwyKEOnxnFCOrF4j7KSI9mwc71Xu4jxQy7CuPGMBUevoAagCulSdwOYaVOR5MN42DMWd9kyr9_1mFJflySOb0aV7mI5zBcwQ_bKe0neMmkQs_--DSviPTmrp1gYnn2Jhbm76TyKF5r0qwy_MOrb6bOsFthLGSHIyaGxm_Z0JzN6vjTYcYWlzfkCmadCDuhsJNzQuzQ6Tnu9qMG_LRA2bUPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف فردا به عراق می‌رود
🔹
رئیس‌مجلس با هدف گفت‌وگو دربارۀ تحولات منطقه، تقویت همکاری‌های راهبردی تهران و بغداد و بررسی راهکارهای مشترک برای کمک به برقراری ثبات و امنیت در غرب آسیا صبح فردا عازم عراق خواهد شد.   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/456928" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456927">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwnoXEsi47IVIrWmZBE8axp3AcGfl0zSw80fYEokeivliak70SXK5AYsvPXMejgOSWl4dnXYGLmI-RDfwk3pDMmu66oYbKHFDw5cygoNPvt6FdoF51JEbNQBXyoIpoXBG1CC9jK8BFeZ3kgQQR6OZ6fbzhi4qy_yJkIMJ0Sw0qcauiTwm9YL3GCNmXQNMob31GlvDARQ_XlWCvvjBv_hHrFiCD_G_eUZmcQ6RldxVPRZfUU3IosPAFSSSCGAOkO2DpiSLpBBQ5ddka3AH8cbM4_Iz4WRdeAwKqTFqDUE00WAc8jjTlMBGTzkHOQudjhjIJs014W7I8nosrDovLJLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: شواهد صریح از جمله بیان صریح زلنسکی نشان می‌دهد که حملهٔ اوکراین به کشتی ایرانی عمدی بوده
🔹
ما توضیحات مقامات اوکراینی را شنیده‌ایم و منتظریم که در عمل هم ادعایشان دربارهٔ غیرعمدبودن این جنایت را اثبات کنند؛ قطعاً هر اقدامی که لازم باشد…</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/456927" target="_blank">📅 07:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456926">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a4be700f.mp4?token=en1YWbsvQBMmMm3z6XVvmL_wt0ReiBIqQpvn_fHEFK3t5RcFvEfU4LZLdSFz9OYC7L04o7qiQC3uF5YMpajhPn0mv3mXiwxZ8eoaxRdM9MuBG3ppYyS4CwQkin1YgelR0C1hJlFmBKFwM5KZzU5Z9vPbEFgjglKMQN0QoolJIZyJNI8kow0-fi9UtA5NAP4REz85Ax8kFdIVL1DMoN0YUXG1kirUknC8XZC0H33uCba6OQHKVLYj-Z3eIZRRahqoxppvCf2OFSCyYO59czY1yU3wER1Ct_nVKCxNBSS5VJnrl_bLnAFplARo7DvxpJg85D2vGXZczVmXj_teVLp3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a4be700f.mp4?token=en1YWbsvQBMmMm3z6XVvmL_wt0ReiBIqQpvn_fHEFK3t5RcFvEfU4LZLdSFz9OYC7L04o7qiQC3uF5YMpajhPn0mv3mXiwxZ8eoaxRdM9MuBG3ppYyS4CwQkin1YgelR0C1hJlFmBKFwM5KZzU5Z9vPbEFgjglKMQN0QoolJIZyJNI8kow0-fi9UtA5NAP4REz85Ax8kFdIVL1DMoN0YUXG1kirUknC8XZC0H33uCba6OQHKVLYj-Z3eIZRRahqoxppvCf2OFSCyYO59czY1yU3wER1Ct_nVKCxNBSS5VJnrl_bLnAFplARo7DvxpJg85D2vGXZczVmXj_teVLp3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داروی کودکان در ایران پاستیلی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/456926" target="_blank">📅 04:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456925">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq16RNVEI2k6KdNGJXQ7u7_AKfhewNQizuvwXC61Dn-ZEnWQOmFeL2HDRNMK_SYPpptjRSu-4dEQYthoU8RiZO0V0kjxU3Es_qrldWDTEOLJxx6fsMcpQ0Q_cxhKknxXmUmk1UkhBz3Lix_kXDaJiCydpBNE7q9_u-MyLSxNO_7SxVrPBsI8u8iOR5pjphTTc79uMP4nN9rgq0KJ7VxM1MYVIloMym1PVxmN9QdfCpYiYz6hwGMmvcMbZYmJ7Ae9tZwCc5b5IQOr3849XN2TphKKSwWhM6YhAI4mWjO4Fz7dCMEj1Uw1y7L-jWJZQetkC1spXHEWeXAEC69kY6DjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
غریب‌آبادی: ملت ایران در برابر تحمیل و تهدید، محکم‌تر می‌ایستد
🔹
معاون بین‌الملل وزارت خارجه: کودتای ۲۸ مرداد، مداخلۀ مستقیم آمریکا و انگلیس در ارادۀ ملت ایران و حق تعیین سرنوشت آن بود. این تاریخ را نه می‌شود تطهیر کرد، نه فراموش. دخالت خارجی در سرنوشت یک ملت، نامش هرچه باشد، استعمار و تجاوز به حق حاکمیت مردم است.
🔹
نسل‌ها می‌گذرند، اما یک حقیقت تغییر نمی‌کند: کشوری که اختیار سرنوشتش را به بیگانه بسپارد، بهای سنگینی خواهد پرداخت. اما ایران امروز، سرنوشتش را خودش تعیین می‌کند؛ ملت ما در برابر فشار، عقب نمی‌نشیند و در برابر تحمیل و تهدید، محکم‌تر می‌ایستد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456925" target="_blank">📅 04:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456924">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaEOzaxrFDNxlY7BGgjTM1RpfEH8VE8sw1PbdroqLbmJ-tql1l2OarkgVrx4JVrYj9zHP59rUGXfoUvrsMD_HbkK5vCyNZ-2XQ54MEhul9DFwjfb4DN0-_ntaudbA_SO1RZ5ybzEN5IpJferqcNr9JXSyvHPRgc2a8lFXVyELXS4FkQfuSknDeyJRtpakx1bwTr0lKkobVlZL7ozP9cUJuJdSZUWd5H2IM8QHvCV7F1VfbM3TmWmc1O9iLFehlkCaucMANBT9nW1t7tNyfxQwAj1CJtuDoF_08qHnnAduE5-4i1LaY27fOPhJt7UjUmJIgy_z3EX20VbnwUCUyFxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز پست‌های اعصاب‌خردکن ایکس فاش شد
🔹
یک پژوهش جدید نشان می‌دهد الگوریتم شبکه اجتماعی ایکس ممکن است به‌جای نمایش محتوایی که کاربران واقعاً به آن علاقه دارند، پست‌هایی را تقویت کند که با ارزش‌ها و دیدگاه‌های آنها در تضاد است.
🔹
به زبان ساده‌تر، اگر کاربری با یک دیدگاه به‌شدت مخالف باشد، احتمال اینکه چنین محتوایی وارد فید او شود افزایش پیدا می‌کند.
🔹
یک پست توهین‌آمیز، افراطی یا خشم‌برانگیز ممکن است باعث شود کاربر به جای عبور از آن، وارد بحث شود و پاسخ بدهد. همین پاسخ می‌تواند از نگاه سیستم توصیه محتوا به‌عنوان یک سیگنال مهم تعامل ثبت شود.
🔹
به این ترتیب، چرخه‌ای شکل می‌گیرد که پژوهشگران آن را نوعی «حلقه بازخورد خشم» توصیف می‌کنند: کاربر محتوایی تحریک‌کننده می‌بیند، عصبانی می‌شود، به آن پاسخ می‌دهد، الگوریتم این رفتار را به‌عنوان نشانه‌ای از تعامل بالا ثبت می‌کند و سپس محتوای مشابه بیشتری در اختیار همان کاربر قرار می‌دهد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456924" target="_blank">📅 02:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0bd5a2c73.mp4?token=TLe616hiK8O06O9bNS6X6f9YI5MuljK19zDBCEgxLoNWAdSxzgdoFRxWPGoed9M7x53NQ2cZkONd3shWHESe5z8dOAUFTxIcZhtkcAbentgcSSMu3F6KynyvxldXCeVRwyF2VGSom40V1W74cdVIKXoAbjWWvRcmG9OxPKWGS_9EVv7RiIO4qu7fBqxlhTVil0OE40EAPFIEyAxu1MTUrDiJEysKHiJS7WHEd8k3r3giqeysQcR-zflOF-XN_eVvCllUQvO-71Q68WiNLxozMJe0d_MEsKv4jn8HGvB6WC02q4QNywJVzOJ-CZK8QSqnlwEkGQ_7wHWmmrPmfvYk7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0bd5a2c73.mp4?token=TLe616hiK8O06O9bNS6X6f9YI5MuljK19zDBCEgxLoNWAdSxzgdoFRxWPGoed9M7x53NQ2cZkONd3shWHESe5z8dOAUFTxIcZhtkcAbentgcSSMu3F6KynyvxldXCeVRwyF2VGSom40V1W74cdVIKXoAbjWWvRcmG9OxPKWGS_9EVv7RiIO4qu7fBqxlhTVil0OE40EAPFIEyAxu1MTUrDiJEysKHiJS7WHEd8k3r3giqeysQcR-zflOF-XN_eVvCllUQvO-71Q68WiNLxozMJe0d_MEsKv4jn8HGvB6WC02q4QNywJVzOJ-CZK8QSqnlwEkGQ_7wHWmmrPmfvYk7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قمی‌ها بیرق سرخ خون‌خواهی را به شب ۱۷۱ رساندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456923" target="_blank">📅 02:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456920">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hgYAgsWKt8jhSg5hy5qCm77jQMhHfu7BbbxInH2_uLhL8zFCO-TrIwwFQdwhmQZfU5RE93JRlNPHSPOZMjQEbYHZGFNc2xNTPOxhmIBMXl5v-mkUj_74dfjpbZ8K4o3XXHLzXSiCGqekyEMuqjpUNJo48xK-oAOuTgxc31wMAzV6fhb7WN5EbH4lqQovl5E6LMZhBGp-lYchkBGi531tAxrunLlJ-F0Vzwj-g5eegKQbKdv-XcvVCpWO6SKoeY31vWIeucJ2cLYqsOZLJob4SGG_Gmqi2D8BLhL_rFJMbiqzAJPJ4IBXp6hM3OUGeuxsFz0nFLO3rmHFjbAZUEUxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsDszFpqYseS4CR9YkjQ1Wbw2qcpvSGbVdWkYQdMLUsFnAFVe-sO8xcFBPVda_I8c7IPJz_s1Wo0tPEcwcgY9eR0zW-tDHsIGxo7XsDgiFEXFBfw8J6hWsX8EFmIT5S4qoZPALOvu9Koke1L5kXoUWrXeJXsFtwdRsAn7rqUscvAAjsYd6KAtWZEXsAnUF56M-bIpTwZIuOCoJ7Rn8xHtVEAirKLIlSoggTXJBH27YShqHZZUUzPF3Rd7tjFG4Qfbx1Iwu9DVM9inOHFHNmRxrr9P0HFGCptqegymZlQM_YVj5lgfJ5crmNDVaffjoXG-kRvCnX2AP6L9y-wxrBKHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9102233085.mp4?token=ev34MYn5WrP1zvdsx2a6JooM2uDAOuH8oViojJHO8ZdznnGs_JjLdPaMtO9nTaqi9aM-qL3PVcbNxNrPY1qcswD-ayagsmzlBDhbQtz8amKFWCuPvCrxe9fHksNUtVISmAsFmHwpREg3w-5M_xax0fpAcNDq3y63_8lQhn7aW2pB_63niGe8spMPEY8Bnbw6xtLCkcxU4cCYYpmUrXpvoF0Izo7v4PYtbJ9F7xt6acSIo40we6wb2mBkfTwuuiQ4wz0i-_qDOgrhvtMkpNL_AYmcDgcKhJ6Ru85EXDtLe-cZHm0_M53ZrG35UXWJQJMwNoI9VKYSP5C5SON7h-I_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9102233085.mp4?token=ev34MYn5WrP1zvdsx2a6JooM2uDAOuH8oViojJHO8ZdznnGs_JjLdPaMtO9nTaqi9aM-qL3PVcbNxNrPY1qcswD-ayagsmzlBDhbQtz8amKFWCuPvCrxe9fHksNUtVISmAsFmHwpREg3w-5M_xax0fpAcNDq3y63_8lQhn7aW2pB_63niGe8spMPEY8Bnbw6xtLCkcxU4cCYYpmUrXpvoF0Izo7v4PYtbJ9F7xt6acSIo40we6wb2mBkfTwuuiQ4wz0i-_qDOgrhvtMkpNL_AYmcDgcKhJ6Ru85EXDtLe-cZHm0_M53ZrG35UXWJQJMwNoI9VKYSP5C5SON7h-I_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🔹
شبکۀ «المیادین» بامداد چهارشنبه گزارش داد که جنگنده‌های رژیم صهیونیستی حملات هوایی شدیدی به مناطق مختلفی از جمله «نبطیه»، «علی الطاهر» و «کفر رمان» انجام دادند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456920" target="_blank">📅 01:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456919">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انحصار وراثت غیرحضوری و خودکار شد
🔹
ازین‌پس، برای متوفیانی که تاریخ ثبت فوت آن‌ها بعد از سوم مرداد ۱۴۰۴ باشد، نیازی به اقدام از سوی ذی‌نفعان برای صدور گواهی انحصار وراثت نیست و گواهی به‌صورت خودکار و حداکثر ظرف ۲۰ روز صادر می‌شود.
🔹
برای افرادی که تاریخ ثبت فوت آنها قبل از این تاریخ بوده، ذی‌نفعان باید از طریق سامانۀ «سهیم» درخواست خود را ثبت کنند و حداکثر پس از ۲۰ روز کاری با مراجعه به سامانۀ مربوط و انجام فرآیند پرداخت، گواهی را دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/456919" target="_blank">📅 01:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456918">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
وزارت دفاع امارات مدعی شد موشک‌هایی که ساعتی پیش به‌سوی این کشور شلیک شده ازسوی ایران بوده است. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/456918" target="_blank">📅 01:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456917">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9472fa504e.mp4?token=BnyPYdgnKsR8KQ7ZAoKtxHXqwkLipbKE3aYMHwjdQdCduOz-AYWojLKwtNMhzoU-bw0vF1TXI8wjiWQT_3n2VXQAaP9Xt6zFs9kdb25gOjZAQNHDKQFumNPrTvq5Un9qNwROeMfrsLuv2BljAJ0Bb498U9DdRUoTtuJn0FLTYpq0cKmMkDj9p7Y_-TlDWFVvVZpLno0_1MCkjcxM18cEUMTmwrUXRa1Z-MkP6QyqnXiJCJ3OMMHwxwsO1_OJbSAxYUw0nm8Y0QXW2yDVvMRk2mJi59YTsY33HEB6_WTZvYXHz1c3uwqe5N42rvBNQ1yoUg-3xCcDAb_CNatXOSIL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9472fa504e.mp4?token=BnyPYdgnKsR8KQ7ZAoKtxHXqwkLipbKE3aYMHwjdQdCduOz-AYWojLKwtNMhzoU-bw0vF1TXI8wjiWQT_3n2VXQAaP9Xt6zFs9kdb25gOjZAQNHDKQFumNPrTvq5Un9qNwROeMfrsLuv2BljAJ0Bb498U9DdRUoTtuJn0FLTYpq0cKmMkDj9p7Y_-TlDWFVvVZpLno0_1MCkjcxM18cEUMTmwrUXRa1Z-MkP6QyqnXiJCJ3OMMHwxwsO1_OJbSAxYUw0nm8Y0QXW2yDVvMRk2mJi59YTsY33HEB6_WTZvYXHz1c3uwqe5N42rvBNQ1yoUg-3xCcDAb_CNatXOSIL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیراز، ۱۷۱ شب ایستاده در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/456917" target="_blank">📅 00:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456916">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f570b23b8.mp4?token=g_c_xhS0-5EZpvqg4m-6la7m4hyv_mEYKZamQP2ll4SWxNytVvp5cKRP_Vyr1wHHkmgsBV8sc2F8yC0NzVqVmmaYwFGlYhUW59uhiRGJemd9BI8yIj2AfwAhhN4wtmZUuwD4gIgwJorGDgAPoqL6VuZayO9bfNc07M6Asuoko79LM5ByVbdMIJ2yUi_q2v4ozBAFhpmuCcXJ9lxauaKNozCytSC5CtKoq90D0_cX6xfx91L4xfMvi62BEiBMyPaPgiLm_fovul1qZgYph0z455i7-0th9jLrPvAU0ROwF_b8d4f6cmX865NUfyuQI9xB9Wf7sjIyILfMkr9seH0Nkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f570b23b8.mp4?token=g_c_xhS0-5EZpvqg4m-6la7m4hyv_mEYKZamQP2ll4SWxNytVvp5cKRP_Vyr1wHHkmgsBV8sc2F8yC0NzVqVmmaYwFGlYhUW59uhiRGJemd9BI8yIj2AfwAhhN4wtmZUuwD4gIgwJorGDgAPoqL6VuZayO9bfNc07M6Asuoko79LM5ByVbdMIJ2yUi_q2v4ozBAFhpmuCcXJ9lxauaKNozCytSC5CtKoq90D0_cX6xfx91L4xfMvi62BEiBMyPaPgiLm_fovul1qZgYph0z455i7-0th9jLrPvAU0ROwF_b8d4f6cmX865NUfyuQI9xB9Wf7sjIyILfMkr9seH0Nkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وعدۀ تازه مدیرعامل شرکت توسعه:
ورزشگاه آزادی آبان یا آذرماه آماده است.
@Sportfars</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/456916" target="_blank">📅 00:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456911">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJRTXaCgjEFxUwWAiT-U1iLJlwlj_yImoMPyzwmd66UcZ1qOvPwD1D2zQnOzi7n62r1IK7HVU5X0J5G8Qj1a0KUio13BBPq5j1vMR7GXVqutDU1RCgvONnjEK-B50FjfJLFZ6ZsYfDpYMy6YdyDjGgfH3g8memo-J0fhfL1Yz1JygRnUX5ZaKB00vpWZUr0Cd4c5PDw_YT_mIC2n4Sz9rkGwV60EExkGVydKYuhUGe5aCyuhP6HxOttc3ZSE8GKnG8fHiv8_sEb3-x3vyj6UUZeWIDuQpphobvigTXdB8jNh6WvTAMTIInfyuCBWwBdos-eEMCbcHLqS0IVJjrfhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gELNA6NtuD8xK-6na6HsR30PS3pcH8cz0PqL0T1Qr7CSMyZEwwAa6v2cykWKe7JIhCTYUhlp1AuEOVPW_lNlYssMfujc5f9VTgVVBt1y-nisfwi1Ve61xTR8rISv5XVbwArsTrU5W9W2kiv1mLHFC0XA5QOwjMDYnTbucL4epFTgOlcXnM8Gnke0NeXh0s_Pg106Yz0JB-_soBgV64TL9a3hbmXBhy1ALv5628ueKyi8JT3YjDmZrpBvwubjUakSCSRgjPvt-NADG0E0zD9kNZwNl9INX4mrZ6P8eY0ERcvps-yPYeaRXJZqXrLA9NC6uWT91S_5FsGtaNlho9cASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSJDRE8iBFql0WldVhkYCgN9S2sV9D-m9hX1CNMM5-SNIAS24ajCzO9MhI-eC0wME11Il37sN6scv06elKYxVXsBU0aBvH5etY1eFYN938_E2AZWzcP0WI1AbUqCzCdO44J9TGQpoklS2PkBWx1Yn7eQSvhOYT3RSANFLmIzqzCLxGfJv44ZSoYVp4PYYGFPFSJNwC3d-kCdNpgRUAqS6UCwTwKnUUS_fSKbGUAzPPU5P20kuPnsnjodIshtVt-bxRo9j8KBAHNrtW4WmF5XW6wumMgx4fK4EcOkWxDAhTuZ4VlqxW3RzJI7CilBwwrulwb0FT9xO6jZvclPYgMIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plYt2v8I3JqA5yZMZVOP3Fr7p6iNu-HQ2QpibGGT0xH16d7fRBINcnENVYmeVTiceRvYah-aN_kOHFPy1Kb_nX--lyTHAw1Sy3cjHBJxpAZDt51U1iv9CvP-Mpo1dGge8QYHQOxqTN3S_3B9eCxKVSdeDW7oFWNE26aoilUtWNcQvbMMLz_FEBOfPV5QnxZjPQmvQzd4lSvvPFEVmpS86eFBEb5AqlvpbSy3A86LnXUwVNP9hS1poLvaCLmiVEMrGf24K3dep9yEw_nUv1EYo9HQE0VRgU5ZMQD4mAoWYbDywnGB1qpGY6y5t5pw2_S5eziMw6-0ptoeTJz8HatGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5_1aqaBu4tjJYPnjsISPNRh9iuDoOt2zrSssOYETNEBfEDW6kx5NTaAzLAS7YRdHjMcojtWVDXAoKSobus7vW7H3ac4pYXhtkv_PrnyrjYOeswa7upl4oKf1-4zeAtB5rzJLHsVsfrNymBu5Eo_yu7TzpyOlByO_FFudu7p0JqwdWx07KSS1fsSQ0POvHkMis0PlqwFUSWP5SF0Bxx4-YSOE7nb1eUhenMx1uAS7D47STOiRX-pkf5ZGTmAC6C3SxKRfDWQcwQTKzOiGHpV-cgfjXea10Mnky0Xw9jSSruCYUCkbM8WhAuN0hp5mOpE0xexd2tTCsb56J3bq4wmnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۲۸ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456911" target="_blank">📅 00:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456901">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMA1DM8OXNGKJIY01jVGwM7s4OGlf2WO8N2TNZ8e761MDTUmwFguhnqCZfPpGy6Isl6X868rvLNJre-eUni1TPetS1vVHsqBHTXt1qjM0ygbhmTJRq5kgrFhs1_hB6XDpzbS_auXhychxQGTRghYSEIyn4rVf9hz2BO9VWND592A4Lo6wGMiXQh1a0MCFyMUCF7hIq4QRrld-tOVTqimZE4ZPH_29Q5RLqKyc-t6Q2X5LPdPngr8Zk3K86wRSJmF4zJfWOs1thwQ3ovJz_gkm8eiE-yX7b15tO54WCtTIK_omXxiq6wIBC8ClX5koB3GUBTN9_HvulmnVF3lgs2jlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ozuk1DdgyeUiWSAihrMdOO6UpTTVZMjNV7gOhrJXO5W9fQ5eHlGYcD2wcm4SLBp1ST-_SWIcmGxigowacWS0a5qMx-_WoiZHod-LRc3OAQ7bxLzzxeHswyoPVcrFpLr9t91MXsqL_C9z7AQz1uizSSGvT4htnbY7OLORxKbTA_2LM12DBYx_a9wJ0e9GwpTrF5aMAdeoJR2ziyWAEinUC5pSxuhAAOq1_3UabahQU6YIMFYgzCoIsIKyI24YtSYk4Dq672ILjkTmJ5r9dWEYkuOyF7i1UHMdqfnF-P1hGSyFA3hioHX_lnNsGo7r1EIBnKogCTGJac3aNLIYSDhjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKtD817WiaX8JmefJ0Qr3qxlx3_Jpp_pi773fy1AQ3JJ_qwFyrT6gI70VTOBHTrPjFBlE9KaCg2IK2-e8QIWUajqRHixbVc8xuyKsgjTugQlPBlTwUSRC09MKMiDpl47Lojqjuiep4T3MUf6rQSgBRlvkybEIG6w0UyBO0dgfkpAU84cQOicjL2pka4kHRiJ29naHf5j2ophUiwo1rNdwQN-rRGAFiA0ziOgoLT_G_0BkwnD9mr1YWzX9oiu-cWN8E2rL3iMuRtaIxCSB6f3OlsDzcLXQb7H_U7BBKl4Z_rXN2bWARu9YRZ7wpbv_qjNvTV7mU-2-NpnJzyhUU688Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9V3bqGATMjWXPGxlDHbBAhvT6CX1AQHrB5xSbrZvph57fJ7UCjp8OhEp0P0jLBIhbaLgAnZQYE_bKPAxk2dOlH_2lFgIVGMfoGpXr9NtLpHWSlxXYPtZp4sTU4K6y7HGIw-MhVe_-FDrs7vNXX_8ifzv_Vg0RQBGPtpAytgALUDppIT8kCumLsMXq7abaZF-AP0xzSJii3oBT_WTCcWrMsfX8Uxv_RkB5wtqWvhA_Wh6Ik13WKNJ3lbm3lxIXxrbc5YAUcg5jSBnTDa7XUCqZTnbeyK-n6RWqto_PBBnRXBrbxj0Z3TGAnGvhebpKLbIJIL3Djd0sVdxGN2ybsFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tu304-GH0YKvNb_aJN1agvveHTPChwFdKtvdoIN1SHMDO0I3wnPtSgd_Ib3HUz9xs-n8rsrqWQ4uSke8yMDNOQtLznzOL2HVOHdig2kyJpRe4sE__scR-nbQda0FR2glBbLL7B-UxQGH1CaOYZEAZEG-1YeTfItgOGu65oVDvUoufBIYYWB9RPO0u5N9_01do7YFT4BEUfCAtDhrDQGVskWdNZEIkB9SmIn4PtBeVdmHPmsyMqmgQR6wgr0eABQLX5ko0rVKHKL5o-spA8LYJqve8pZdOe771PVXXpQUhlCE6TxVNZxaVOmTtyJQCErCc2Ps7w9m8UVdnaMoKUmWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNqcutWY_FW-LO2p77LD1KnqmJgxGP3IWmDXG52xGlpYQBnw25eEVlDU55OUxaQEnqE5Dv-bBhEpv-s6x2S3HebJEE4-zhsi8A_cvlhbSkGdmsvAhwdP9PcvIXO09WmxGC7ZD1cR66x0Hrn4MlsxeNrnXHH-36H-LrRHtXITqCMKM55v7JKkyB32riTdmmj2XUuiWHvmC4h2LmApazDh69DtiRapxFIZpARm9uQo0OmReYZbxhf2zHJknB7YtNXHF3Qx8k71ELjy28WpV-Tg3UNLGTw0yeaQzcUz1eGpZaPOJ7oSPzRolJSWa44vpDOtinw7Z7JArk1N69gYcKoF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSeEDGYsZJapsOdinu1t3EYWalJ2eIp7_y3FILBKfhCt-11-rJZY8d_rJIAWQU-7yeqLzdOtJ_YXMC8KyI1doMvcO5BucIySY5TqRzSTxJrzWd94h1K7j_PteIkwJxEagneFKf7-YFyTOmYRmvaEiiqgaN9C3-VM-DBAztrQF5aUdTUA4puDeS-iIIl7I8mT6VchtxcqSIbRAK68AFRUGsVg3D5X8KhboptA-yxygG3swnbDE8ICNebHZdJVbTcvJ8iG-MXA2zhy7U7YHGOu4S8hG4Ra9BucAldDo0N6F2H8qTyAyj8lYPC4qhoyR-9lkmKYZybvZqqPk78sgt-iUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnUbMO7h_KHNMRAv3dYOyOhWcEZN2jXttrD0cqkroO7U8lhb52Nkig2ud9j8t7HdY0dO3pADBx8A1E3xzPwsavGQW4ZG3_6CiHDQNNkqrtwgxq3DAKIMiis1FglhVzJaCr4aulIHzaUkhLBzg95LFqaTBCmB6VO6F5dDXxjJ3iAiHb4UlV2C4IphUyiORmUC51xfZmsK-X9DINXPrq9-_Gr9BpMU1C3Kq704_uOuiKOl40AgYV9zJgDmqhzNqUNiCZjcPRrnUGe2Ex0IGu7F7K6XGCkR_VHlHs-Q8Am6Rxqsvt3ZTtmby_k8HI5CeIBTgMNiAczK-uM5_whc_Fgs7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LPPo31u_P5goWqvH89nAb1zJarc6ulaAfVLEJNZWSfAAGM24w2Td6eRRifgplUwUJGD8d7taQ7axe1YljpDP1sYEybfgqMUQJ_e2rArA0pls0Y6JWspYw5ken0hvSF3RLyvWujdWRswipSm206Ss7iLS3aInmV9VWH1GwYuwJxfNlY2mjU-asjFTkGqFMnCn0-iaPuL8_RiS89Afyz9oBzCqd5aTIdJoOQxDenslyIyjZ3LCSUDYDEih-MwYcMwYURw1lWJutNVkihaKz9CyHjnfoxne4TCqOVxB7f_PUL28IU5bIXSOQ3S_0o-3ZOgWp7VuMszM35zgbN2W_d2Mqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGz9n-GDcYZ0SfQNt3ngXWqvuqI-m_kMTYm6qOdXuOycIu4kyq_t5ALM8xl6MDU7wbvvsbAaKwOvcUqGifYx1jIiz6BSMdlhG0Ntz97pnvB4LX-Hs3fA8Tslh6kXzjk1uldfACumWSAnUlxjLqUtqbIZsGh5i60cg-Z4CT4pvQn_4z1rxX6Jyv-SyAmVxzQCr8kYPLsoJW-5616JEGERvrHhN8pfQcn_KVGlfRHe68uJS7roYoPk_WJbXtZBkPVcoM2JEMun4mvoNUET5np6idwXkCTXUkzk-LSh_QMcdL1GTwcpZ8lpkQdYDaIuIzQwjoPSS4cX9oTOi7lIq5quww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456901" target="_blank">📅 00:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456900">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgTE5H-jzPqODTuhk85-TVsq4S9iiiIGTKBnSBJejDf1O-tVcz4QJkF2EYbWEO1dgUh3k1Pn3KEz_oPNu03Tz08cvFnimNjuHyIqLWDklFGtcPjTohz5xdyIHoEsoKk4uKn5hsuJFjfdei47XqAeBj_aE9z1rE_QqICRB8ed5sHkXpyx9lctMiqciAcGwZg7MXm6mPyXVSmNUOX8Ie-58hEkm_koBsYsgCWS9ajjcWpUm0sDk4YGkj4YxK9bv6SE7hI-CwrHyYvRmQLxl9_vwsNTUBMGOIddnqIkp43QE17Rlsrwk8yyZyIdRZJnZR5OlKWaGZeMEAwSiIojlABczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی ادعای امارات ‌مبنی بر پرتاب موشک از سوی ایران را رد کرد
🔹
سخنگوی وزارت خارجه ادعای امارات مبنی بر پرتاب موشک از سوی ایران به سوی این کشور را کاملا مردود دانست و با ابراز تاسف از اتهام‌زنی به جمهوری اسلامی ایران، این رفتار را خلاف اصل حسن همجواری و مخل تلاش‌های جاری برای تقویت اعتماد بین کشورهای منطقه و جلوگیری از تشدید ناامنی در منطقه دانست.
🔹
بقائی از همه طرف‌های منطقه‌ای درخواست کرد با در نظرگرفتن پیچیدگی‌های موجود به دلیل شرارت‌های ادامه‌دار آمریکا و رژیم صهیونیستی علیه صلح و امنیت منطقه، به‌ویژه سابقۀ عملیات‌های متعدد پرچم دروغین، از اتهام‌زنی‌ بی‌اساس علیه جمهوری اسلامی ایران خودداری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456900" target="_blank">📅 00:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ملاقات سفیر ایران با ۴ ایرانی بازداشت شده در کویت
🔹
سفير ایران در كويت با چهار نفر از هموطنانمان ‌که سه ماه قبل بازداشت شده بودند ملاقات کرد، و در جريان سلامتی و آخرين وضعيت اين افراد قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456899" target="_blank">📅 00:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoV9GB95uz39L1Ks7jUikb76A3ohvyXpQXmZHUFYJFY_EpDExDXUIVXZFuxs2neJydBHbsUngVWgBC24c5PUF5bQXeVEsvgLWAlzeqfM_p0MYCPpF7CuhUd9KaspY3YxdHgOCZKGDIRp7eCEwemWGUUj_sApKXqRyXggqyjvJVWnzUmDjyljGvla1HUBVSjiYrO647AJBj7SIHkn_r3XIJxvuIFlROx_mdoFaioEtKWqD9tSieiSd9I_U6_-FeACPQ0k67iAHyqheTcY2n6b918_fpwJ1YZ6YR4fsbRznHelzLTlEnEfHuJtIX3kuLq-IhedLRHkt5ShteJOGTLVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دیری است زآشیانه جدا مانده‌ای «امین»
...
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/456898" target="_blank">📅 23:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb71618728.mp4?token=v_ObJL2nSiz0HoTIk9ek4CZZAl_V7-GQnq2cuFdNUy3T-dW-JLbaiH7V1TRvp3B1HotIUkNDjvdmfCUIrMmXh4M9-RsODTWhO2ip7iYlSQMgHwRYPjvz1b1qLcjCOM-3SavXZwStuwG5o01WZAHMJErOtWHEUM6xF9W-0dwDwjYExPp3Cvq24jT17hKh6wUa0Jm7yHayJWmJ0XA_ymCM7Vdr6pQxFVRi3SjXWnq7qhP_19wRXFflgjscpX_bt_svBa4EN3BFzHbkQaz-0xqrszVpxfiuBGVw5tdE7omdhWxV3ydHzrBErQKMYQb865im9b_tjZ1QPWynH56gOiB426vbu8mzM4QZOGkRStA37nz30Iqf8jQ05QizlHLs5iEY8LX7ZUXWgigNEAC65QMNOjzvQGP9yusT-t6QMHgO2LxK3cyR9nB83QMQiBlgsEFf9Kvg7HCQOLJZKhFirApIivVjEVhOcS9ILmQYQ2RgEv20hf5RodQEfqpdjixlRo3Slt5J_qe_mUS76xfcYX-ScCopZYrb4la3heY6OV5I41F2eXoh5e8EDFeZl7Ax82Mj1GkxgVhPttqfwKBuWUxq84aMWPlaX_SxDZPT_bKQV8PQT2iFjZzcHYLZGs34VNQIfiCKzF2CIUxc7PIB87WDtiSFXY_fSvWKFx2r_Z1YnTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb71618728.mp4?token=v_ObJL2nSiz0HoTIk9ek4CZZAl_V7-GQnq2cuFdNUy3T-dW-JLbaiH7V1TRvp3B1HotIUkNDjvdmfCUIrMmXh4M9-RsODTWhO2ip7iYlSQMgHwRYPjvz1b1qLcjCOM-3SavXZwStuwG5o01WZAHMJErOtWHEUM6xF9W-0dwDwjYExPp3Cvq24jT17hKh6wUa0Jm7yHayJWmJ0XA_ymCM7Vdr6pQxFVRi3SjXWnq7qhP_19wRXFflgjscpX_bt_svBa4EN3BFzHbkQaz-0xqrszVpxfiuBGVw5tdE7omdhWxV3ydHzrBErQKMYQb865im9b_tjZ1QPWynH56gOiB426vbu8mzM4QZOGkRStA37nz30Iqf8jQ05QizlHLs5iEY8LX7ZUXWgigNEAC65QMNOjzvQGP9yusT-t6QMHgO2LxK3cyR9nB83QMQiBlgsEFf9Kvg7HCQOLJZKhFirApIivVjEVhOcS9ILmQYQ2RgEv20hf5RodQEfqpdjixlRo3Slt5J_qe_mUS76xfcYX-ScCopZYrb4la3heY6OV5I41F2eXoh5e8EDFeZl7Ax82Mj1GkxgVhPttqfwKBuWUxq84aMWPlaX_SxDZPT_bKQV8PQT2iFjZzcHYLZGs34VNQIfiCKzF2CIUxc7PIB87WDtiSFXY_fSvWKFx2r_Z1YnTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیندگان دربارهٔ جنگ آمریکایی-صهیونی چه می‌گویند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456897" target="_blank">📅 23:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b223f152f.mp4?token=imRmvyDkjA1IaUwN-sgw88GgkE9Tbclm-Jnqf_JjO625ID6RFy-EOsvYrzZkSNLp9LVSwt7sKPzAKSf6JzZatCcq-rcZD1c1_coTXE-Q7144t-iM2eWUAS14UiFK_w6i2keVFa88-9ktG9JmhTcvFQg7vHbtbtNxgQQMXfmDfa0Pf7IWHQ7J3isiJF3Uw4ndof9cOj5TPfV6yOfNgKV4OryVyB_Nr4Zj8Uq7_cJsqe00bIqJDJJyVEbyYc3roU7zVltF_bz4yi6PLnOMa85iig54SuNmKT0vqyKhWTPUC507j--36KiQfVJy47e9PX9laLAUNq4PGFHNqTtq7F7m6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b223f152f.mp4?token=imRmvyDkjA1IaUwN-sgw88GgkE9Tbclm-Jnqf_JjO625ID6RFy-EOsvYrzZkSNLp9LVSwt7sKPzAKSf6JzZatCcq-rcZD1c1_coTXE-Q7144t-iM2eWUAS14UiFK_w6i2keVFa88-9ktG9JmhTcvFQg7vHbtbtNxgQQMXfmDfa0Pf7IWHQ7J3isiJF3Uw4ndof9cOj5TPfV6yOfNgKV4OryVyB_Nr4Zj8Uq7_cJsqe00bIqJDJJyVEbyYc3roU7zVltF_bz4yi6PLnOMa85iig54SuNmKT0vqyKhWTPUC507j--36KiQfVJy47e9PX9laLAUNq4PGFHNqTtq7F7m6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دارالشّفای آتش و آب است این سرای؛ سوز دل مرا به نمی التیام کن
🔸
حال‌و‌هوای مزار رهبر شهید انقلاب در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/456896" target="_blank">📅 23:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e6ad8a31.mp4?token=UsZJj4rLzNrK9ORz3-fBDSTwSA3D-YUhTd0mkYdnf3y5ZW_99yMtEk1EzsU2QvV03V4RlDpeXgcNkTwsT_SWTyOtOS-27Z_mq7oSL7b-lIr0LWQ6XTL1DH9L180I9JLTK7wO5ywendQVs-yMWrooj-D9DntDTic6_QUukc78LqbYuvYmo0MIKe1N7wHBLnlx9lqj9RWtjroq5JDLZnDH58BBnhNQAXE6NEN99MguU4uDCKRej_9yKu2rEywHlHrFbd59dEci9mvGHPOcDDcbzrlJTMFQK8CKbpSvb7NsTXLe1nNlmuR47if9mZQmGee_jCegtukbeYRIerIaPRLKkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e6ad8a31.mp4?token=UsZJj4rLzNrK9ORz3-fBDSTwSA3D-YUhTd0mkYdnf3y5ZW_99yMtEk1EzsU2QvV03V4RlDpeXgcNkTwsT_SWTyOtOS-27Z_mq7oSL7b-lIr0LWQ6XTL1DH9L180I9JLTK7wO5ywendQVs-yMWrooj-D9DntDTic6_QUukc78LqbYuvYmo0MIKe1N7wHBLnlx9lqj9RWtjroq5JDLZnDH58BBnhNQAXE6NEN99MguU4uDCKRej_9yKu2rEywHlHrFbd59dEci9mvGHPOcDDcbzrlJTMFQK8CKbpSvb7NsTXLe1nNlmuR47if9mZQmGee_jCegtukbeYRIerIaPRLKkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاوت نوستالژیک و معروف تیتراژ سریال یوسف پیامبر توسط استاد کریم منصوری در محفل اربعین قرآنی ترین رهبر جهان اسلام در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/456895" target="_blank">📅 23:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvkKXha0mDH_4uWpAwGHE3TP0WqXxhlPWS4ry-IVzNGkj9dt7jdvNnJSnA1DPNBjTzG6VLfteF-d5G6hboCMNj00SPDDUxjUFgDehngRUrMzuBbUOeGxuK5GHGw-TgrxemBSzN8GlqHm88Dn7pjBK-CW2X0utISTnn7oI8_9dHpNIsVkn-73WGiUVuM4t3QYGtSZufqPHrRq6cbheJ_izR5IZZiA0hfiVtofTa5BWfMlKkPgVDZOcIn1wMx-eejy94GGhD1SdAc3EclGqKUtNiO_ZtuBY29lQoQNv33kx06tuqFi8utFr2gTkCdXhf2Abg41XuH12AGWc-hJaD09jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس کمیسیون اقتصادی مجلس: روایت واقعی از چالش‌های اقتصادی نداریم
🔹
بزرگ‌نمایی صرف چالش‌های اقتصادی و نادیده‌انگاری فرصت‌ها» و «برخورد سیاسی با مسائل اقتصادی»، ۲ اشکال جدی در فضای تحلیل و روایت رسانه‌ای است.
🔸
روایت واقعی از چالش‌های اقتصادی نداریم.
🔸
مدیریت روانی جامعه در شرایط سخت تعیین‌کننده خواهد بود.
🔸
مولدسازی در کشور تعطیل است.
🔸
باید مدل جدیدی را برای اداره اقتصادی کشور خلق کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456894" target="_blank">📅 23:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456893">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454ca97fd3.mp4?token=O3PiEhE6-yYrAfpswo6RGDUrgG1PLMWKXh4qLzhzhrRFXgtm38qOxkDc8_Lh8dLQ2EfNEooHCY8pVRY6PAG1HW6z8uXiLauTvwhP5tRc_TXrfZU8rApigdMfY_46QTguZ8vEPJ_-YI0Tn1wIfgjUlNt8H9JoVqcqLBGVvVIGsFIBZUqyA4IZbaABVBFbii4x4d73B8J-3wGBg84Im-UBAW0c1DAnjFF83Z9szjS9OfkrRg8SJVlDFK0000oXzlXH6uigto61gG0_D3E_Q5hHGK6AsGDYERJ4LGDBkXDhhX5NLTHtLEHlGEp9HDBKKw1yGXdep69EpqYDp78YL0wpOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454ca97fd3.mp4?token=O3PiEhE6-yYrAfpswo6RGDUrgG1PLMWKXh4qLzhzhrRFXgtm38qOxkDc8_Lh8dLQ2EfNEooHCY8pVRY6PAG1HW6z8uXiLauTvwhP5tRc_TXrfZU8rApigdMfY_46QTguZ8vEPJ_-YI0Tn1wIfgjUlNt8H9JoVqcqLBGVvVIGsFIBZUqyA4IZbaABVBFbii4x4d73B8J-3wGBg84Im-UBAW0c1DAnjFF83Z9szjS9OfkrRg8SJVlDFK0000oXzlXH6uigto61gG0_D3E_Q5hHGK6AsGDYERJ4LGDBkXDhhX5NLTHtLEHlGEp9HDBKKw1yGXdep69EpqYDp78YL0wpOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندهٔ محیط‌زیست ایران در بریکس از خجالت اماراتی‌ها درآمد
🔹
خورسند، نمایندهٔ سازمان محیط‌زیست در اجلاس بریکس به سخنان وزیر امارات دربارهٔ حملات ایران به مواضع آمریکایی در امارات واکنش نشان داد.
🔹
او گفت: هر کشوری با میزبانی از متجاوز و زمینه‌سازی برای حمله به ایران، بدون تردید با عواقب عمل خود روبه‌رو خواهد شد.
🔹
هرکس بذر دشمنی با ایران را بکارد، سرانجام میوهٔ تلخ آن را درو خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456893" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456892">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
وزارت دفاع امارات مدعی شد موشک‌هایی که ساعتی پیش به‌سوی این کشور شلیک شده ازسوی ایران بوده است. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456892" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456891">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwO_0SZovPuPJ57oNC7MKj57Bgd0wT3vEqy5KP7npLIgio0cUeD6kxKULnE687jt9FccERiEHnbO8D1imvpYpKYnOMAAYuP20HVVK-1BAu9ICaO1_02q4Ip_0_k_fVKT00TcBotufv1gSTuIGGDJEJ42ZEtl6xlgsxIjIBnu2N9em7rkzmTIgukFRWQrfaRxAxsRBSt2EboXu8IFOqzc8qiseN23WtK5qaJKt9t7Zy1RDnQP_BkSGk5FYjvxgVGaBwpOn_Ea5TYm6UgVjn7CHPr0tMjvaV1UN5Yc2YlEMFj_kRvu30pTuKISJlPlDFVkiIKBZm8u_nbYLbClgZREYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام درحال تبدیل حساب‌های کاربری به وب‌سایت است
🔹
مدیرعامل تلگرام در حساب شخصی خود نوشت که تلگرام برای گرفتن دامنهٔ سطح بالای «.gram» درخواست داده است.
🔹
اگر این درخواست از سوی سازمان آیکان (ICANN) تأیید شود، حدود یک میلیارد کاربر تلگرام می‌توانند دامنهٔ شخصی خودشان را داشته باشند.
🔹
کاربران می‌توانند فقط با نوشتن یک جملهٔ ساده، وب‌سایت تعاملی خود را بسازند و این وب‌سایت‌ها روی سرورهای خود تلگرام میزبانی شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456891" target="_blank">📅 23:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456890">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96802d4300.mp4?token=WWWNOF5koXhWWqhZKJrpwDGu2QuW2iVk3Q-0Q_HmwNO2Tg5or-Tf2WmJUmE7MrcDk81CagCEQw74i8dZUFNUjVl0dJMbipalOjWNpa9825MAholHaBldjeRtUgu4T62CMjA90epyUeC7ZHix5nlkeIxaNVQgWeOxPiJ84bGLpBkYOQDHUy_Dd-EIOPqBHb-PH9sat9YReoZdwkAOFjnW9EUl42TjAL9dN0BTbT-MfGYGAaFarDJGDg3QDvB1dAu-sd9il623GIwv6lMPOjh4wPo9Hdn59jzOCwjaXGWTqSnP4MKT9OXux4DHq7lpy9bV3MH4OM_0CdICyGPAtGp7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96802d4300.mp4?token=WWWNOF5koXhWWqhZKJrpwDGu2QuW2iVk3Q-0Q_HmwNO2Tg5or-Tf2WmJUmE7MrcDk81CagCEQw74i8dZUFNUjVl0dJMbipalOjWNpa9825MAholHaBldjeRtUgu4T62CMjA90epyUeC7ZHix5nlkeIxaNVQgWeOxPiJ84bGLpBkYOQDHUy_Dd-EIOPqBHb-PH9sat9YReoZdwkAOFjnW9EUl42TjAL9dN0BTbT-MfGYGAaFarDJGDg3QDvB1dAu-sd9il623GIwv6lMPOjh4wPo9Hdn59jzOCwjaXGWTqSnP4MKT9OXux4DHq7lpy9bV3MH4OM_0CdICyGPAtGp7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کرمان در موج ۱۷۱ خون‌خواهی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456890" target="_blank">📅 23:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456889">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYQRyRYH6F6_O5q4TO1euYaYjID6ztuHDbTKMgbKDviSsI60ohMgROtuZmxwKORNzXVsbQSQ5RKyYAyqCJ5xxLKkpJ-E3eaXfYZaD0vm6Q6fIDnKLuGmj947Jw24VLBPXteTeDOsbThrelvjUO_bgEuAX1DzOEwlraGNvX8aXs4IJ4yuH3z8yLPBtAIwDUpfHJvLqtwNgesA-FQu2jTR0IQZ9YAB7Oq4eFvhwvnEbwWQTVWB2AlweeqexZN7_y5mWBCpCToR0ESNxfYqUl1fs5JXbwEjYWK-fagbgnf7_UwC00wtvw9SRJhsH6xrYHXm-sEnvNBNnRgXgU5Y-d-_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک کشتی در نزدیکی آب‌های یمن
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای کشتی در فاصله ۴۰ مایلی بندر المخا در استان تعز یمن خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456889" target="_blank">📅 23:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456888">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd8d42719.mp4?token=FijIKHz6TelEWVwfAMVtcg0rxGeZxHIXEWdlKfYuamUSZexV1XCuO4FFf7Y2Okoj74FFoeKDcYzCXBtBryh1H-kvgkelJ47QXwP_3-6oQaP06BctFyxmPlO7brNOApXXcShPl6qjS-jTMRugar3-Rc3QQN6gFZzhPLblAbFgeToSSuyz3qJZsAyOyjhAoGb8TKb62SZxfnsl2_tbAXknMexyd-QWFZ5z4yKoMukMC_DHDn5Uuv_epqGFRuBT1W3GfJj7dv13OZY3YW7sFNix1QxRxSM9IiYl1ih6abjnSvAgvkGg32BXnjzjXSXJlXYo1BmBXPETxiHpl2suCm6YMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd8d42719.mp4?token=FijIKHz6TelEWVwfAMVtcg0rxGeZxHIXEWdlKfYuamUSZexV1XCuO4FFf7Y2Okoj74FFoeKDcYzCXBtBryh1H-kvgkelJ47QXwP_3-6oQaP06BctFyxmPlO7brNOApXXcShPl6qjS-jTMRugar3-Rc3QQN6gFZzhPLblAbFgeToSSuyz3qJZsAyOyjhAoGb8TKb62SZxfnsl2_tbAXknMexyd-QWFZ5z4yKoMukMC_DHDn5Uuv_epqGFRuBT1W3GfJj7dv13OZY3YW7sFNix1QxRxSM9IiYl1ih6abjnSvAgvkGg32BXnjzjXSXJlXYo1BmBXPETxiHpl2suCm6YMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلامی به لبنان از بلندای بام ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456888" target="_blank">📅 22:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456887">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcOLwLkAqfedcHVhiZA0RNOECV4O8p-UgLcOvB613eW02GbQxNjd-e9qq6xsrweSnsK3ELXkt6VJdCzK7RQtLPu9J8lB39ySYUSXoV0waR6GNJhvMeU60-fJZGQjWyf0ObSB2YhQ5x5M2M6EWAwbiNmXnUq-qzol76YMHSLm_O0fQCNwlJMfFOyllmzUgSk_zoBiKThglqpUKu1kO0FPGgKO3tX4S2DNmvGZpZeyD9Jo9B0piRzcMKqNCWekMrY78JKKX0ibQbvvJkrpKA6LcAaTNhzJBa6vtRdEtJWER2No-zTDaYNrwuTVLg-IuiXuJ9OoaTJSWiHjVkB7pwo63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
به قعر خلیج فارس فرو خواهید رفت  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/456887" target="_blank">📅 22:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456886">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpG-KckVB7GSDPibJKBQxrnt86tmQncxHUzXqSoFanHtdUAgP9Gx5Jn5gwNXZSdEkQHJDQSyPTe-IjOu2MgkA-lwJXq2JsLn_lPqGQH60o2rNJA3JTjZ3ZEpevq8YkDDw-5qsb-9wLwARv9Rb3jzPWAoYZSxgOi7Y68J3kulaTjJrjKmuthrrBMTRrZ72XfmV7kJAfuLuPKY21QI7Tl_G4uKvLMKLhyzqVTE23FAAgpz-ZVQmYXdtN1UqmHCGCXu0PSBVQltMspZaJcqveYVV8v949nvVhDL2Wn8Cf3-XQeUu15SqTMBBsC5gLRVzQ44kMIIDVNCHutd8nkU76RJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علنی شدن شکاف میان ترامپ و ونس درباره ایران
🔹
ونس هفتهٔ گذشته در گفت‌وگو با فاکس‌نیوز گفت که اولویت نخست دولت در قبال ایران، پایین نگه‌ داشتن قیمت بنزین است و پس از آن، جلوگیری از دستیابی این کشور به سلاح هسته‌ای.
🔹
ترامپ روز دوشنبه در این باره نوشت: «هدف شمارهٔ یک این است و همیشه خواهد بود، اینکه ایران به هیچ‌وجه و به هیچ شکلی نتواند سلاح هسته‌ای داشته باشد.»
🔸
این شکاف نشان می‌دهد که این لحظات از نظر سیاسی برای ترامپ، ونس و حزب جمهوری‌خواه تا چه اندازه دشوار و پرچالش است.
🔸
نظرسنجی‌ها نشان می‌دهد که اقتصاد و قیمت‌ها از جمله قیمت بنزین، مهم‌ترین مسائل برای رأی‌دهندگان در آستانهٔ انتخابات میان‌دوره‌ای امسال هستند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456886" target="_blank">📅 22:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456885">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc1ee44735.mp4?token=AB3vU6rlFsPdbN0ELOBq3wHSkMfVMEiMHwy8bba590OCclrg272cRTslIf_pTlyIg7EJaukk7JaXwCOiZYcYHe6934-5lAmSCUMQ_o7rulqz8iJR3v7A05rZSyxlBgn1OnnBwfMfSCFdmrPEr84Aifu9IIV60LJM0A1SeZoqcEa6vLtRB-sfKeE6J3zFoSasjs8jxp9uvTCAPEoZY0fAsvOth4P2fkmzXJuGgXW0ogA6YCVqtSi_fzYqBhUdpA_FgglM1MSEdg40rSN_ZxJNYE44rB4gSfvQqRJII_Y7Y0sGUj077DjmX-TTA45clRNn1RZZgFrPkk0Ct2YWG5thaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc1ee44735.mp4?token=AB3vU6rlFsPdbN0ELOBq3wHSkMfVMEiMHwy8bba590OCclrg272cRTslIf_pTlyIg7EJaukk7JaXwCOiZYcYHe6934-5lAmSCUMQ_o7rulqz8iJR3v7A05rZSyxlBgn1OnnBwfMfSCFdmrPEr84Aifu9IIV60LJM0A1SeZoqcEa6vLtRB-sfKeE6J3zFoSasjs8jxp9uvTCAPEoZY0fAsvOth4P2fkmzXJuGgXW0ogA6YCVqtSi_fzYqBhUdpA_FgglM1MSEdg40rSN_ZxJNYE44rB4gSfvQqRJII_Y7Y0sGUj077DjmX-TTA45clRNn1RZZgFrPkk0Ct2YWG5thaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۱ شب حماسه و اقتدار مردم گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456885" target="_blank">📅 22:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456884">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd366c5a3.mp4?token=oVzIIitdC-EeBnjlHbdcaX-uB7zfGFSueTz2BitiBI_RvF8Czil0lzLAm_93mo4KwwPx5LEuXel3kLJ1qvwRvnNv95xi3Ngoa-Bm2iQ7kV4DzYvcoPKOb-GD8Ucu5SN25vGzC0d1uCEre2QQDjsGCGs4dmgOHpL17Yj5hMGUPVezjjgwW_-Q_7rBerRPH_JSDWitxs-Yhvk44aQp4PjCQ0nEt0bvCCJ__0M7KOn1duSsS2TCx8bqb19wGkAUpmBhRyZrOC2Zdmo6mzDJ6gYlPM9Z1P5tPaXEytSJ2YKHrVZJL8SpcAQaEEgbuc4LXyIqqprafTgdKDFSCkQVF8pBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd366c5a3.mp4?token=oVzIIitdC-EeBnjlHbdcaX-uB7zfGFSueTz2BitiBI_RvF8Czil0lzLAm_93mo4KwwPx5LEuXel3kLJ1qvwRvnNv95xi3Ngoa-Bm2iQ7kV4DzYvcoPKOb-GD8Ucu5SN25vGzC0d1uCEre2QQDjsGCGs4dmgOHpL17Yj5hMGUPVezjjgwW_-Q_7rBerRPH_JSDWitxs-Yhvk44aQp4PjCQ0nEt0bvCCJ__0M7KOn1duSsS2TCx8bqb19wGkAUpmBhRyZrOC2Zdmo6mzDJ6gYlPM9Z1P5tPaXEytSJ2YKHrVZJL8SpcAQaEEgbuc4LXyIqqprafTgdKDFSCkQVF8pBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۱ شب حضور مردم مراغه در رزمگاه شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456884" target="_blank">📅 22:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456883">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnFYlt5yMc_d8WM1X15Bn6-laywr4NBBrmx1vjLhdemV9EzalPPj8NZ7eWunEqNso7uixeuIOZgipT6PJaxT9wwqMiftBHmPaSn1r71WNEW_LVAtdSBe-1n7A3He6ZCSXyguHt6tAJszO9-Ci9g_FxU-Ws5TOqyYipUsgL2NGyL3N9d5B_Z82kqP9vTsLZUF9_FpZ8c-emVxMzAkrztRPnuYYD99W22bMZmAoGm7YTKZI2dkRZTe7w-ZlmQGsHwWmrjgwEFrdGsCMcbtC-foixrZo-SFvJErw4tw0kakWNC_WcDfpY5ATAHL3Gl5AKgWqRjhkSxatI_AdsJfYO_zTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم تراکتور به سپاهان توسط حسین‌زاده در دقیقۀ ۹۳
⚽️
سپاهان ۰ - ۲ تراکتور @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456883" target="_blank">📅 22:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456882">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17581cbfd2.mp4?token=N3k5Z39m85I6VqmNb1WTHnyXp4eESpFUbwlPn8K8G0otdA3fmbD5Mi1n2WVLa2Ra_pePyPI7n9NAGYQWoYZDzXPbdbWuwEbYsba6MM5tpB5R4pmGxxXVKliy24hpuNTgts822Syak_Swi6ZvUqleqwCQeGqARRCv_bSQII-0a-TQpWGfSQj-P3GZvO_WDIUUs2HUCdbjupRDvT8NIcA6S8dP5SAIVlj5fTN-bTu6WYMVYiZXRnnSYXH3y2tf6Rt7iM3KUT7Zchg99b4WveYPXajjVCA_t-5G6kQfihHsdTXPCuPdRbgBjSgoCSTiKLKwkBmkKDklJL5MwgBeEIzo2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17581cbfd2.mp4?token=N3k5Z39m85I6VqmNb1WTHnyXp4eESpFUbwlPn8K8G0otdA3fmbD5Mi1n2WVLa2Ra_pePyPI7n9NAGYQWoYZDzXPbdbWuwEbYsba6MM5tpB5R4pmGxxXVKliy24hpuNTgts822Syak_Swi6ZvUqleqwCQeGqARRCv_bSQII-0a-TQpWGfSQj-P3GZvO_WDIUUs2HUCdbjupRDvT8NIcA6S8dP5SAIVlj5fTN-bTu6WYMVYiZXRnnSYXH3y2tf6Rt7iM3KUT7Zchg99b4WveYPXajjVCA_t-5G6kQfihHsdTXPCuPdRbgBjSgoCSTiKLKwkBmkKDklJL5MwgBeEIzo2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول تراکتور به سپاهان توسط حسین‌زاده در دقیقۀ ۸۳ روی اشتباه حسینی
⚽️
سپاهان ۰ - ۱ تراکتور @Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/456882" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456881">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617832e930.mp4?token=sOGH4C6Klt180915Bydf3l8RghFrtvi8eHVmE5LQFoEQggCOXVWvpUGzbn4e7Hqxg5iPAGuC1Lb8ZNWIR1JWV1_hx29wCA3OjZlFfgg2TiwLZNOclOyRZYJIgTPAymN5tyiFP_xN44Tr6MoIB3TmdO1Bhg7BLiCAU_YlqUJrwC6osWtDsYHNJ_LLRUh4_6WPTL2luQOdycP8MFo1Pocvt92YFak2lA4bjQday2KhqhFpEn-_yZ_5mNYrj61eOn0N05xYVhPKxS6MmP52pAHHOuRdLqOXEHqvd9N2F-K7ljvE7A-FmVpQa6OdRPm_JhewJxSZwCgpekILrE7VwVpnoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617832e930.mp4?token=sOGH4C6Klt180915Bydf3l8RghFrtvi8eHVmE5LQFoEQggCOXVWvpUGzbn4e7Hqxg5iPAGuC1Lb8ZNWIR1JWV1_hx29wCA3OjZlFfgg2TiwLZNOclOyRZYJIgTPAymN5tyiFP_xN44Tr6MoIB3TmdO1Bhg7BLiCAU_YlqUJrwC6osWtDsYHNJ_LLRUh4_6WPTL2luQOdycP8MFo1Pocvt92YFak2lA4bjQday2KhqhFpEn-_yZ_5mNYrj61eOn0N05xYVhPKxS6MmP52pAHHOuRdLqOXEHqvd9N2F-K7ljvE7A-FmVpQa6OdRPm_JhewJxSZwCgpekILrE7VwVpnoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بیلبورد جنجالی در اسرائیل که در فضای مجازی سروصدا به‌پا کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/456881" target="_blank">📅 21:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456880">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ورود ۲ دیپلمات فرانسوی به ایران ممنوع شد
🔹
وزارت امورخارجه: با توجه به فعالیت‌های خلاف حقوق بین‌الملل ازسوی ۲ مامور شاغل در سفارت فرانسه در تهران، وزارت خارجه این ۲ مأمور را به‌عنوان عنصر نامطلوب می‌شناسد و ورود آن‌ها به ایران ممنوع خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/456880" target="_blank">📅 21:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456879">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b59b18635.mp4?token=o5MxRhhzsMt9maOtWUE9goXizIFUA0xy80AcL0jglDh5CVfu8TfSJFiGOu1vr9ZsX-0LGiQsUlPvBdc_aJn7XHrboA8IdKTVt_PuX9_BU3JGjRJ3JbKbVPDaZygbctwm0YXmoRkXLjGva51BEdgs1QvpURNojmXC-1X2p_Eq6M-bI12wPvRqQq2_glmva9HGGtCFjK39X7FD-GqFtSwyzIhG7sDyOR9Cw1qIlUMTPDXEP0FRO1O3hA3HAnEA7TS-iSZ-x_SooailVr8I95szQxd_3F80dEKsLWqCBGA4PymAk69Zd1tNNOr0CFUoQ36SsSHsdC6BXt63IsqwzKaoUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b59b18635.mp4?token=o5MxRhhzsMt9maOtWUE9goXizIFUA0xy80AcL0jglDh5CVfu8TfSJFiGOu1vr9ZsX-0LGiQsUlPvBdc_aJn7XHrboA8IdKTVt_PuX9_BU3JGjRJ3JbKbVPDaZygbctwm0YXmoRkXLjGva51BEdgs1QvpURNojmXC-1X2p_Eq6M-bI12wPvRqQq2_glmva9HGGtCFjK39X7FD-GqFtSwyzIhG7sDyOR9Cw1qIlUMTPDXEP0FRO1O3hA3HAnEA7TS-iSZ-x_SooailVr8I95szQxd_3F80dEKsLWqCBGA4PymAk69Zd1tNNOr0CFUoQ36SsSHsdC6BXt63IsqwzKaoUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول تراکتور به سپاهان توسط حسین‌زاده در دقیقۀ ۸۳ روی اشتباه حسینی
⚽️
سپاهان ۰ - ۱ تراکتور
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/456879" target="_blank">📅 21:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456878">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9312fbcde3.mp4?token=Zjn-NlMBlHHx1hMuCo4DfutJhDW3Ixmzj5k4WfSVwVMMkhCuUwQWkhdwMyk9RG8C3096tHFbfi2k-UpqxuwdF4dT6MlUOQJ7CZXMcjeL5Ov3gwuMug9P_T5PhH_j-kSO4vwhZK0j1rbUNRXwSL2BFY2Ei9Jp5_uCEenyKej6gxrisHo-A__PrOTZy_SVST9Mk1p9yXZ3fbLJUBFmFt1Z2qyU5em3dR1-9wm3JYQk_agoeel94eTZsShpkXbDmtdChy9l5AaLWyIDy9y2FnRtRIbeqP-x8HTzxqR7yRX2WWJk36OEH9ldZowq6AR99mLNZgK5jewtuH4z6Hioaqn5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9312fbcde3.mp4?token=Zjn-NlMBlHHx1hMuCo4DfutJhDW3Ixmzj5k4WfSVwVMMkhCuUwQWkhdwMyk9RG8C3096tHFbfi2k-UpqxuwdF4dT6MlUOQJ7CZXMcjeL5Ov3gwuMug9P_T5PhH_j-kSO4vwhZK0j1rbUNRXwSL2BFY2Ei9Jp5_uCEenyKej6gxrisHo-A__PrOTZy_SVST9Mk1p9yXZ3fbLJUBFmFt1Z2qyU5em3dR1-9wm3JYQk_agoeel94eTZsShpkXbDmtdChy9l5AaLWyIDy9y2FnRtRIbeqP-x8HTzxqR7yRX2WWJk36OEH9ldZowq6AR99mLNZgK5jewtuH4z6Hioaqn5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: ملاحظات ترافیکی هر مجموعهٔ پرمخاطب، به‌ویژه مراکز تجاری، باید پیش از ایجاد آن دیده شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/456878" target="_blank">📅 21:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIuYl1J8_Qku7CNkLj3jqRCdn2XJOL3Z5VbBA3pe9y-yvLdqt7QI4N5Qjiktiz_N9a8ujYv0hSblaLJazUrqcHYyv9Rvesx69ekSDd84GkvNAiYfd4ZwuOD-ssmyItJT75Jt-p3f1k24-8Bk_DCz0DubSIqwiOxJJpYTt1aKLLjLfYfrqHpD_XqFoH6dG6ei5Gj78bLC5Pd9Jsk0it5nSMnR8yq33E7mDpIA6KKMtl0JF-avIVZTB_ezkAk3wZYDI_jEmC_25ZyucPXxrM_wJ8sMldxXcWam_G5j7T8npq11LrroMkOwYzo9T1V8OgD45JPPfV2h5AvZP54J73hW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6rpjOgsFQaqNIMtoz8cMH6oFS93twZxsKl0sYf6aH6yuDZEiyL4djmK7XOObX84RNWL8c2qaVSigmffShQ56VV-NnJMaL11XNjoM7FMLduYYbErHJh_3Vo-ZwL66go6oyZo2U0Htixt1-0Nq_2gAeaRbEuemSMOD0A3147Hvy6mNQ8FFtDbkjGWySNe-c-lkuHoCWBTYBJvm9Z293e0bXC1vnqiriT-bu6nVOzXf37xCwNc63rwmT_sBy51prtijm4C3-MJoPGHCvh1KqkOELYUAEejlCKBrUcwv1jZrFj-3c6ZVoY5ouJ6CNcBuvJKs-hnP-wLJhKedQPDJkvQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsIXUewnFWKzMmKGva3A2rmRabThg25LPpbzyTpXB50l5-gfaFdM_jlGMupGPcF9Ypgaype3WKB4AWBuKdsheogHAC-LAaqLv1MqfaQn2nRJGnfg45jJpN0yoxtxQgAkG4mJcfBi9Vj1wePKGaAiEoi8e_5jmCBxA9hDFetaLTMJSnvZr-Obph_IOlJPU_0gxqNwFHxv7CxIjV_jUkiA6ALMJtZhF8yrGnI64sRe-4YYRV1UGkBf5S7C0iuyM795xrfSll_F8ozGk_9Z1Z5e8PW1SM37TBnpMekwthTWBV1rDRwYt_pSZqecg-QO0vq4G3Rw4qdQEBuJn5hgcS6ayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnPxqTTlG-RzyIX8kMAESzBN6JJlrsC1Q-9E6ecPz2Vqlog200lXIJhC1GwROm2KqPIpC01Y65LZH_X09sproWL9baej7gwIUiglaPmErC_YmW2UrPFJBPGfI9hgBaYJ3QNyUH-NVu2izGK4SlyG-ekBoqjSwDZTnmBFDVEfmrkCoKT6ZdOSeNNuCeOgQeNqNFhJWylrkOEHGr3h7_jiuA2CyCJJtecmkAjE9J3IBbG3HIYt_nLisl16c-jG13f2dAI6kEbtiBUGqfMyV4bt0tw5tTBxPu9cW9Bcn2vz3k9oV0eopvr9U2IJuyCvhrObJiJesOT5OeL1-qkw9gHwMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4VrY8Pr1Cn4taHUyWM_Lnl_60kpWyjms7Ms4R192TGGCpCSAFfoBlOUR9adrzKb1TmoYzQPnClNJ9V0Ij1EgZpapyoP0s22XmZybCeZfPa6-hV4mGQjvHh7uhjBjdUFceZyzZ2FIWmwAsoZ7rEH4b8UYBicwpI8ErEu2q4RFpvb-vk6JqQDCS2hE05XPjvaCZAGSCssS-Qxq6QseDbLNpzPx2HTfkmBNdOU8yMOLLndB80CmtWt9AiXzBL7EXghVmwoHZHlKI9vwzrHL8NhKwxFnnOYl01SOUh7t6q4W9KVVNcgeRoGCnZ_lwVFsC0h7XGiiO_0X2SLq_hdIr1wCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlCP3G-d29FI3aOS6DItxD1zaBPXLjC89rut1v4PpuuBwn-JurOr0CdMhCGryK-pV5ImHUalkyLTRq-nf1rXvtezKKqJCsfrdV9QKKIoU92RJ_qy52xypkN-sgVSO5aUd5jJOssxwrxtXIEmk6djYwVHbxZgYQwqQhsn9nKPIpU5AqyrSU27fmW85S5WwOoS8TiuB28IkhkP8-b1V6OMgGKrLSMIgG70T88hUcbumC-z4s9Vc8Iu3-I4SjBDFcdCKkDPIFsP5k4zpN-eXbPQoZbYUofI95ePUrlK23in0xRR904y2aIeHYJHRfSwLh6HbCiM2_NoP-iRsblzkvtgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jv495AUZEzgHBVCNGHJz_KocI_bnINsi8hIu5zo7HTLhJ2Z-GCaDBAMWyey27lqXm0eVN5LUMXMVtvBg02ALdnykYhQ_AdR8yp9YGw9QMIad0XQfIHe_29Ysjo0EaRULZZ6GR7QRWzZb1MCwyugiMZzLZ8TCZ_NIwyeEzjgFnmCw8DZqj3VOnBrqOBEgTb4HdT1bTwAC19lpBn701k_zKrJPtmsKqcdLstws_9r0W6Di5etzZ6gkXC0BOA3dSrF0kiHWfQKg3pPkTehVJwqkRf4Y_5l-_mbeeWLexqII_dfRLOBPH0Gr-bNlnYIOepgi03NLENXnStpZUYf_uBlkCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم چهلمین روز خاکسپاری رهبر شهید
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/456871" target="_blank">📅 21:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5663417d8.mp4?token=uVxWbyBkzmd-v9JddMnxpUfNNWj0APfsSGeVDZoy-pRVg-L58_OJnRrIQkcMTFIc6kFHVLyCITC-bnChYLwMUO6R60fxl5i0heTx5rggYkdX-Xdy1fe87utymmsTDfDAQ1bCg3i6fDZ6ysJA7iF7HnnvxMK8n6nUgiqJB7HbiWmZIkGZWhkVBRQdWMiquQn_Myd8hcLRhQyqh4UhP9K1BxmgKfsjXMhukiwDIAalNpcYb2PlXPWkzt2pXdRZfTjUycpXuD4pSNiVeDuaApTG9DGyuZf3iDVfO_FHbWOM7PFP7ZpjjnvWrrg7AHR2kza-HwzDP4qTZxAaitFoBVYlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5663417d8.mp4?token=uVxWbyBkzmd-v9JddMnxpUfNNWj0APfsSGeVDZoy-pRVg-L58_OJnRrIQkcMTFIc6kFHVLyCITC-bnChYLwMUO6R60fxl5i0heTx5rggYkdX-Xdy1fe87utymmsTDfDAQ1bCg3i6fDZ6ysJA7iF7HnnvxMK8n6nUgiqJB7HbiWmZIkGZWhkVBRQdWMiquQn_Myd8hcLRhQyqh4UhP9K1BxmgKfsjXMhukiwDIAalNpcYb2PlXPWkzt2pXdRZfTjUycpXuD4pSNiVeDuaApTG9DGyuZf3iDVfO_FHbWOM7PFP7ZpjjnvWrrg7AHR2kza-HwzDP4qTZxAaitFoBVYlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار دبیر شورای‌عالی امنیت ملی با خانوادۀ شهید لاریجانی  عکس: هادی ه‍یربدوش @Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/456870" target="_blank">📅 21:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456869">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91104304cd.mp4?token=MRsuFeJUKZ58eEeJtpJzUqk6xI72S-ZlYcBcNRIJXX_TyFPnmDhp2rJR1Es5T497xWZ1RQIa6sKGc3lG-HFxU-GJmibxlbd3bEMfR5NdUn15xjNlITckYed-vL7w_vKsq5s5BgGxZnG0Tn9-f-vlis1cWrHaBFUDF49DuLn9W2VRFcYAwCKncZge3IX6q4_ZmmBHAuGoCGvzebRmNMDPGmXbubbo6ey5EPOn8X4DMfrs6i-n1pFyBJGkHx9BqIjs9LyTf32Oh_6AoRnvqnicF2CvqQSKEowPjhE2HnFbdl35W64c0n_cLZ8_oh-tj5mpn90sv4Obcw09R5CJYeP6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91104304cd.mp4?token=MRsuFeJUKZ58eEeJtpJzUqk6xI72S-ZlYcBcNRIJXX_TyFPnmDhp2rJR1Es5T497xWZ1RQIa6sKGc3lG-HFxU-GJmibxlbd3bEMfR5NdUn15xjNlITckYed-vL7w_vKsq5s5BgGxZnG0Tn9-f-vlis1cWrHaBFUDF49DuLn9W2VRFcYAwCKncZge3IX6q4_ZmmBHAuGoCGvzebRmNMDPGmXbubbo6ey5EPOn8X4DMfrs6i-n1pFyBJGkHx9BqIjs9LyTf32Oh_6AoRnvqnicF2CvqQSKEowPjhE2HnFbdl35W64c0n_cLZ8_oh-tj5mpn90sv4Obcw09R5CJYeP6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: وزارت خارجه تابع دستورالعمل‌هاست
🔹
کار خودمان را براساس فکر و عقلانیت مجموعه نظام انجام دادیم. @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/456869" target="_blank">📅 21:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456868">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5IKO4pCbWqoUTiOQk0yY7fdtQEX7Gfoi2AIBgC2gKmX7Y7rpqkISlqxgrt2Q-abrGl51ppaBJ6Il20WrPfGufsVS9mjEs78hBfDqUL23JtOGBiEKOAlPFTtbealPDAOD9_QiLPGrhcElttWOUmVyw8-7z2U9ziXqhZPxxI-x3XS-8di6Zi_Cp1inX3NMY_SI6-8mMlE7yedO2QtqBrOxj2n3AExmyJBPz8UhyfadIY4Spx_48-XGa2YpBiq3aJIkTnBRTldqB9xrg5Ws5eZ3MHjhfrfPhuupMUWsR3tzP_uV4PP65sqfWp27J9eqLDlOChQnNDNd7FdsVaOa-KxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: رسانه دیگر «پیوست جنگ» نیست؛ خودِ میدان جنگ است
🔹
حجت‌الاسلام طائب: جنگ دیگر فقط در میدان‌های نظامی اتفاق نمی‌افتد. امروز میدان مواجهه، چندلایه و پیچیده است. یک تصویر، یک خبر، یک روایت و حتی یک سکوت می‌تواند بر ادراک میلیون‌ها انسان اثر بگذارد و مسیر شکل‌گیری افکار عمومی را تغییر دهد.
🔹
اگر تصویری ثبت نشود، روایتی گفته نشود و حقیقتی به‌موقع روایت نشود، میدان روایت در اختیار کسانی قرار می‌گیرد که می‌توانند واقعیت را آن‌گونه که می‌خواهند بازسازی کنند.
🔹
خبر می‌گوید چه اتفاقی افتاد؛ اما روایت می‌پرسد: چرا این اتفاق مهم است؟ چه معنایی دارد؟ چه درسی برای جامعه دارد و مردم در برابر آن چه نقشی دارند؟
🔹
رسانه زمانی می‌تواند مأموریت واقعی خود را انجام دهد که از «خبر» به «معنا» برسد؛ واقعیت را کشف کند، آن را درست روایت کند، به جامعه یاری برساند و نسبت خود را با آن واقعیت بشناسد. در این نقطه، رسانه از یک ابزار اطلاع‌رسانی به یکی از عناصر تولید قدرت ملی تبدیل می‌شود.
🔹
جنگ ممکن است در میدان نظامی متوقف شود، اما آثار آن در ذهن جامعه، اقتصاد، سیاست و رسانه ادامه پیدا می‌کند. پساجنگ، عرصه‌ای برای تبیین، تحلیل و ساختن آینده است. اگر واقعیت‌های این دوره درست روایت نشوند، امکان دارد روایت‌های ناقص، تحریف‌شده یا ناامیدکننده جایگزین حقیقت شوند.
🔹
رسانه باید بتواند واقعیت را کشف کند، حقیقت را روایت کند، تحریف را آشکار سازد، ابهام را کاهش دهد، اعتماد ایجاد کند، امید واقعی بسازد، تجربه‌ها را به دانش تبدیل کند و جامعه را برای نقش‌آفرینی آماده سازد.
🔹
رسانه‌ای که تنها خبر تولید می‌کند، بخشی از واقعیت را منتقل می‌کند؛ اما رسانه‌ای که بتواند میان واقعیت، تحلیل، اعتماد و کنش اجتماعی پیوند ایجاد کند، به یکی از زیرساخت‌های قدرت ملی تبدیل می‌شود.
🔹
شاید آینده جنگ‌های بزرگ، نه فقط با موشک و اقتصاد و دیپلماسی، بلکه با روایت‌هایی که در ذهن ملت‌ها ماندگار می‌شوند، شکل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/456868" target="_blank">📅 21:33 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
