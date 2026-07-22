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
<img src="https://cdn4.telesco.pe/file/o_lRHE93BO-BlXU0ssO8OVadZk5JJ1iT6FJx8IG_jDOxv6BrHMN_IKNS3M4PVHLrhC_ii9g3fHJQsaU0mz-3na3bmzBg8v27AXbi_sWrSuXYqP6kbgaUdwlCyypdZldJdH46Uf0tHdIcNAB1oj1lxMQFtDlfikZyqhFXr8f_RfX3kzvclz0ghXR9PjlvOG6jXBgVokiKxeCi1dh0-Zhs9I8NOWJF4c-Bi-J0MTHHMRwgLG_5_mUtp9QObz8vz_g-vq3-IWufFmoE-C8x16VeKvtpv_OTi9SyFwS3VK5COuUovUFxrgPMFD9HwKqLmDcuj_JcwKk_S85TBj9lGutaCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 205K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 15:40:06</div>
<hr>

<div class="tg-post" id="msg-81055">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/funhiphop/81055" target="_blank">📅 15:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81054">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCdp2pqY_NhZY40ddFZpRMZLpwiLX53zdVOeQvGSLfXOXj863jGWsosb1aoUFlbOWulo4RzqdisTObXZ8StOW0G7FVs_VSf4Og6sSJBoupfMTaaql4-LJIisQzvIZJXFyKai043CJxlUsDuo7kGP92mJa5Qs0Mo-legHP5fgj9QgxtzQ5n37pT-dDEndeDe7aPyUT8KV41BZOJDqNsREN-x1eLkIhouPHhuTVvFy0E53bIcngRl-aW_ohKf4lUd_OEni1OOX3ehYLMp-agbyBspQ6XU7_1NroaTb3Gs3VKExS1ZktgI5sFVdmjlnYK9wGE2BldBKtctl6npFqDxxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/81054" target="_blank">📅 15:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81053">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سپاه: اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌ کننده‌ ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/81053" target="_blank">📅 14:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81052">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امتحانتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/81052" target="_blank">📅 14:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81051">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">توضیحات مراد ویسی در مورد فالو کردن عراقچی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/81051" target="_blank">📅 13:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81050">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/funhiphop/81050" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81049">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">لیونل مسی بعد ناکامی تو جام جهانی اینفانتینو رو آنفالو کرد دلیلشم به خودش مربوطه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/81049" target="_blank">📅 13:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81048">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhzX-q4EIoNJ_S5hvA_Xm14xQKut_t5LCof4TcXvWkTYGL-zhpmwMNFdQd_3NwpLEfUwCWO4LTQj0i8jWu_jV1QJQybZb0TegxGumo9EiDCElu6DyNpCFptiTCSXSZ4LuMiIQNdDVmUZ5bq1ZniumCzU6_UDMJ-vZKCnChKab-LA1-LeOwrtlgc8_XhBAc1Rvs983zx8sq7QW1dECpjtRZBuF53BmaiRk8VtgQdBnlpSx0g45r5uheJWIjNJeFBVa99OHkmIo6xsVkhhX3IeO1vsjX7GiSoJsuISD96RA7TUbm8HyuNgs7vRaeAFLlV8VTI8vBqi6-DtJjbj1dobYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا من در سطحی نیستم که راجب این موجودات نازنین نظر بدم ولی ناموسا سینک جای بچه نگه داشتن نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81048" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81047">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcrVq4XaNLm6M2jjbPvcDldvj7OaQYp_GLDf2-SbYCx6qK4fMgnSrCT369EE0e5QfljJ1J7N5O-MVMPFnU6bIIID1jGYpX_HE-MDGy-E2RnWk5mJZdJ2GKNokbJNxfe8AS2alf9q-Abj3Y1936sY4bLkjJSYXaY1am-CripptiyO-yMxfF7BOGATgLmXuqOSCrz_M31O08sOep6zs0l4XD0hfwSbPPLErass9CPjLEN5j6yVtK1txqBjj9E-E9CzJEVyuFC7bL_7rVRB_HqwWfy47FSGw1A9tXcd5HvxC6YiuM9_VcqrVy0wwTjC19GsnHL8R7Es8i2O2DZOLwdXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
هوش مصنوعی را وارد پیش‌بینی‌های خود کنید
🎲
🔥
دستیار هوشمند بت‌فوروارد با بررسی داده‌ها، آمار و اطلاعات مسابقات، مسیر تحلیل را برای شما سریع‌ و ساده‌تر می‌کند تا انتخاب‌های خود را با دید دقیق‌تری ثبت کنید.
🎯
تحلیل مسابقات با کمک هوش مصنوعی
📊
بررسی آمار و داده‌های مهم بازی
💬
گفت‌وگو با AI و دریافت تحلیل حرفه‌ای
🛠
ساخت پیش‌بینی با ابزار پیش‌بینی‌ساز
⚡️
ثبت انتخاب‌ها تنها با یک کلیک
👍
هیجان پیش‌بینی ورزشی، این‌بار در کنار قدرت هوش مصنوعی
⏩
مسابقات را بررسی و تحلیل کنید و پیش‌بینی خود را هوشمندانه‌تر ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r31
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/81047" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81046">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/81046" target="_blank">📅 12:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81045">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قبل اون قضیه نجات خلبانا میگفتن نیرو های آمریکایی خایه ورود به ایران ندارن بیان سلاخی میشن و فلان
الان میگن خایه اومدن دارن ولی خایه موندن ندارن، بمونن سلاخی میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/81045" target="_blank">📅 11:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81044">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ویناک چند روزه به دکی نگفته پول منو بده دارم نگرانش میشم</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81044" target="_blank">📅 11:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81043">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سپاه صبح ها نمیزاره عربا بخوابن آمریکا شبا نمیزاره ما بخوابیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81043" target="_blank">📅 11:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81042">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو دنیایی که ملت با سهراب ام‌جی لاتیشو پر میکنن دیگه این که فران تورس جام جهانی داره و رونالدو نه چیز عجیبی نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81042" target="_blank">📅 10:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81041">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81041" target="_blank">📅 09:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81038">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81038" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81037">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">همین بین که شماها مثل سگ استرس امتحان دارید رفتم سنگک گرفتم دارم املت میخورم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81037" target="_blank">📅 07:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81036">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ولی بیدار کردن پدافندا الکی نبود، حس میکنم امروز صب یه تیزر از اتفاقات فردا بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81036" target="_blank">📅 07:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام اعلام کرد عملیات امشبش تموم شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81035" target="_blank">📅 04:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تسنیم: دشمن اومده رو آسمون تهران ولی جایی رو نزده و فقط صدای پدافند میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81029" target="_blank">📅 03:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دانش آموزا بگیرید بخوابید فردا امتحانا برقراره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81028" target="_blank">📅 03:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نصف این گزارش های انفجاری که میزنن فیکه، تا الان پنج تا انفجار برای شرق تهران زدن ولی هنوز خبری جز صدای پدافند نشده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81027" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ginza</div>
  <div class="tg-doc-extra">J Balvin</div>
</div>
<a href="https://t.me/funhiphop/81026" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کوبارسی اینو بعد قهرمان جهان شدنش گوش میداد من وسط بمباران
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81026" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81025" target="_blank">📅 03:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZahra</strong></div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81024" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پس خبری نیست، جنگنده اومده بود پدافند فعال نمیشد.
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81023" target="_blank">📅 03:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81022">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صدا پدافند در شرق تهران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81022" target="_blank">📅 03:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81021">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شبای خاورمیانه واقعا ی حال دیگه ای داره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81021" target="_blank">📅 03:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81020">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شین: انفجارهای عظیم (حداقل ۵ انفجار) در مجتمع پارچین، شرق تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81020" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81019">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=tXGrbc2fscYFku5yW40rWBposkbcq76JTkApm3kgwNi0Om0GV7VM1Mzx2VkfGljLCZVaRsnX0AuQXJ8usEsc8BXIUEWlQHfXk3Y8Wkv16Q3KSFvD1iVQoZzr_b53mu4T0raj_16sw1PzUarAgyQjZ66iP1hOg1Ef-8kmbVcC7UMCk5ZNeysrtSzR-oVgxMpVSnDnlM7VnGH3WW5-PwV2ASw5apGuTZkNgli4iQbz9ITaLPUk4BWrSva5gqhUAjUljD2mLQ6o0ys6SJw8EqPTbtrKPaipcyRRpM3PJ-5-Fpk2utC4We6QxhtcK2bBp4dVl1oqu5533jHbARWItlMhooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=tXGrbc2fscYFku5yW40rWBposkbcq76JTkApm3kgwNi0Om0GV7VM1Mzx2VkfGljLCZVaRsnX0AuQXJ8usEsc8BXIUEWlQHfXk3Y8Wkv16Q3KSFvD1iVQoZzr_b53mu4T0raj_16sw1PzUarAgyQjZ66iP1hOg1Ef-8kmbVcC7UMCk5ZNeysrtSzR-oVgxMpVSnDnlM7VnGH3WW5-PwV2ASw5apGuTZkNgli4iQbz9ITaLPUk4BWrSva5gqhUAjUljD2mLQ6o0ys6SJw8EqPTbtrKPaipcyRRpM3PJ-5-Fpk2utC4We6QxhtcK2bBp4dVl1oqu5533jHbARWItlMhooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه بیدبلند،ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81019" target="_blank">📅 03:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81018">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام از ساعت ۷ عصر به وقت شرق آمریکا (۰۲:۳۰ بامداد به وقت تهران) برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند، با هدف تضعیف توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81018" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81017">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=m0ywslTMqeEAr8Q1ZGPNmGgafKN7BlWPZWxarVpy8ydpEjqQ3VBHqAr09GtKCP6x7pnKphgKpRiHGICBoppEO0-Wm96ta1VnabJAqpnwpmPn9eYGWkx_fFHe8NpPbmF0B6rxKGO07t37PbmqG0kQ34ykIvVZXytesI_UO6Z1lOg-UFwmgY3Tdb_K8eQlw30kStaEpDRV2B0NhadODiA7JFhgAMTejn_rzJkZnIa_3U8SaqkiMMJn252D5c_6vhCNc3Pqa9VMWCSHm-BcNyU8xzwOUnaOsibDhaJMKLgJGcxWab7CBj0AhtSRQWS2Gr9VeY2eOfnyk-L0cUhpYm6_Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=m0ywslTMqeEAr8Q1ZGPNmGgafKN7BlWPZWxarVpy8ydpEjqQ3VBHqAr09GtKCP6x7pnKphgKpRiHGICBoppEO0-Wm96ta1VnabJAqpnwpmPn9eYGWkx_fFHe8NpPbmF0B6rxKGO07t37PbmqG0kQ34ykIvVZXytesI_UO6Z1lOg-UFwmgY3Tdb_K8eQlw30kStaEpDRV2B0NhadODiA7JFhgAMTejn_rzJkZnIa_3U8SaqkiMMJn252D5c_6vhCNc3Pqa9VMWCSHm-BcNyU8xzwOUnaOsibDhaJMKLgJGcxWab7CBj0AhtSRQWS2Gr9VeY2eOfnyk-L0cUhpYm6_Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81017" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81016">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار مهیب در بانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81016" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81015">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فعالیت پدافند هوایی در سوهانک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81015" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81014">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=IwjHdJYXkZwDSBk7a1FqeP5FIYWtPxKTEwE0LWRi6go3tyq5cOpex7rQzPkCXwlDVlKtaJNraSsF_S9e_uUCQxp0_zH14NDd4DFQuIiRl97fbhstzUwVWc8jtKY-qydf4SpBGC-hPG3c2X_V_rEwbu7GLZx6IGmVTVALpAvSuQIy8I34ndNWbp6Q2UGMBelSZTkF-DHExetPoJ0N5snoxrYmX4J80zWbBx_fUB1UeiGGv9fWZm9BdhxVzx6FWGwbufOT5l7G2VddV04q7Cf4_CpUWNdOBRzEsToVrnKtD-D30trouTm8vZzHp6pipRBpZpPOn6ozMcvPKleIvbTYDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=IwjHdJYXkZwDSBk7a1FqeP5FIYWtPxKTEwE0LWRi6go3tyq5cOpex7rQzPkCXwlDVlKtaJNraSsF_S9e_uUCQxp0_zH14NDd4DFQuIiRl97fbhstzUwVWc8jtKY-qydf4SpBGC-hPG3c2X_V_rEwbu7GLZx6IGmVTVALpAvSuQIy8I34ndNWbp6Q2UGMBelSZTkF-DHExetPoJ0N5snoxrYmX4J80zWbBx_fUB1UeiGGv9fWZm9BdhxVzx6FWGwbufOT5l7G2VddV04q7Cf4_CpUWNdOBRzEsToVrnKtD-D30trouTm8vZzHp6pipRBpZpPOn6ozMcvPKleIvbTYDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81014" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81013">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تایید نشده انفجار تو نارمک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81013" target="_blank">📅 02:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81012">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۵ انفجار مهیب دیگر در بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81012" target="_blank">📅 02:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شین: ۶ انفجار در بندر ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81011" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81010">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چندین انفجار تو تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81010" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81009">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نت شمام کیری شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81009" target="_blank">📅 02:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81008">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تایید نشده
انفجار تو نارمک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81008" target="_blank">📅 02:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81007">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به گزارش نیویورک پست، دونالد ترامپ، رئیس‌جمهور آمریکا، خواسته است که جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، به عنوان دبیرکل بعدی سازمان ملل متحد منصوب شود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81007" target="_blank">📅 01:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81006">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81006" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81005">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چرا باید یه کوه اسمش کلنگ باشه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81005" target="_blank">📅 00:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81004">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اقا جدی انگار تو کلنگ خبریه
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکای جنایتکار مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است
-اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81004" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81003">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به سیکتیر (۳۱ تیر) آخرین روز ماه تیر رسیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81003" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81002">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد. در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81002" target="_blank">📅 23:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81001">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-fBlMcUd5zLLMOcAyFvd2OBXAg3_DRMhMPln-rQXviqMpGOWOGSS3OINRMTvBBRUjL0ugh1wNpA0K95iUrouTPL3pDbM7bMv1xVX4OnVptWX2UsD47u38W4i5jOurZRZaQ_hcv-i1AwKlt-2pExugI7FVDTc73DMD9LswWR4yuYc3n9foeWNQDQMBArLeHmpE8nW8D1MdJTTqq0ahHQyQWv0aLpr5FVU3uX3uYRF47SvegiG42WVGs3vl5w8kySPjX9h9dn9qVD4Cg7q_hphJ2i1pgQxAFMz1Q5hBiG2OEK2NM1eVBbJbzJJFJolZIdtPGVwe-XqloTqwNHWntQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۵  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81001" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n1uYE8fjBe9VqM3MEIqe9B0rRD-r1Gk2ZOVBzRJcSytIUzxOl1CGoWDaWsS83gcNN2KW9zpqRdHU0lL-WOcyoeVCEIj-HIOWEAFQVnGfDfmeInrIp0GCSgEKKCHCKwxQQJjVLVPzUylscJEqMKgVppeLNedj-amob-LPYJADJpSX-HeEsCSa_9_C8xtk-1mDz-pjTvPo_LTbOizSR82DSkhtLXQPlNWWNdei0N-OeudpO2q773b6W1bAUBRj4fEh6raOs6SGFP2rRGJfumwDHlNTrHeo4lNoI7x8IpT8VAhzfYW0ULlEfgeGhlD-EWwKOMs3ZICzE_29dkgpKKtGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0Qg1bMp9X069LNSHGPQINL2R3g3skWynDQxuQJZOJk3A8Dk3L-b2KQyxY9WrPbspJKFFoTmdve15_g2FUqeadQBGR95uosDw9lUsa6Wr41Bg2Jc91ShCMApgb70xJcQvHloS-ealc9StmEeu2tBqC14HyBm7uflaaf06R3iU1887N79HcjldlMfvQ4YFWjKm9Pm5RsGLacWGUd5rUS_ZpzqqyGJPQWp9x6ndunWJWusfC05zjfLdevCrw2IGM59ILnLppE4gmm0o0ef-Yqabvw10ldTzA7-WS_82aeiNPtm_D7vMfUEgOb9hqwq6vaL0Rq1TYg3B3j_bthWo6QdMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد.
در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80999" target="_blank">📅 22:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جدی این یکی بخدا عی ماخارنا ماخارنا بعضی رسانه ها میگن سپاه سفارت اسرائیلو تو بحرین زده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80998" target="_blank">📅 22:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هشتمین روز اعتصاب غذای گسترده زندانیان در قرلحصار در اعتراض به اعدامها هم سپری شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80997" target="_blank">📅 22:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این دفعه بخدا عی ماخارنا ماخارنا ماخارنا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80996" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80994">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrmNbG2YG6dcw4u0Hf4tXLfM1UDp7fJEbqFt0PB0dqjX6wzb7UIb_pTSNbt96AG7p04cPI1fU6EEayomN84bGfYHjdzy3MS-H9-j-8UHfbjaTGrmzFUm10a8HSIDO_L5C_7fnTjPXgCkZSiwI4CuEr8LxUlcGNEc6bB6GhgZ-KGeO3Uj4OCTa9TvRzEzAMj8OjvxV_yE5HcOwedvMPs60QGFUUvpiApWJ6svem_OBYjAPi424uSUMQ31u6UrSSvK1SCj_9pzKPDal5YDoK0vwewdwNcMF3fTaEgyTIKR6Wxa9clzzn6PaMgF3rIyf9ZrLfvl8_EmwWdNuCa1aPuCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxEVjGVAVtj3yFxsTuG77cXulPT6sy_LQz_ni8BecNIG7X2L6YPutFDAT8fUSxx1uDQd7NxxB0Im2CrgZ1qvK81RKXI0bGJCXny4sLMTRSDnssprW_q1OFTZCOVRA4GC_2UWeFhyN0JFqh5hXPe2smnVGnq1zAPbhiL7G5PFJb6OPJZ7VU_oATfeGa3WBC3QfXhE6IFxfLKaTZzzbXINxO2SsG18VgMnqW33I81WiSrrk2oOrG5LMnZ331SS_AfME31QOXZ3AQsfZu9BvYCadc8nPxe7ezGC_yr_6pVEGV6u4jct2eyvOC74JlALGqjk0ZEk5B9zRbL_macmn9tViA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینی چرا این شکلی شده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80994" target="_blank">📅 21:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80993">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ گفته تاسیسات هسته ای ایران تو کوه کلنگ رو میخواد بمبارون کنه، برای بمبارون کردن این تاسیسات حداقل چیزی حدود ۱۲ تا بمب سنگرشکن لازمه، خارکصه میخواد چیکار کنه خدا میدونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80993" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80992">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بمب افکن های B1 آمریکا از بریتانیا بلند شدن به سمت مقصد نامعلوم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80992" target="_blank">📅 21:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80991">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W88BRXIu8tDQCD5N_80hC5ht82QxU_JeytO71Hgj1jNIT4Lf_ReWzx2ojurvkQTkIhsgvDceh4IztVms7GhV99_Dqj3V8d5BXGUQFdb-W21Tgs3n7hpjDnC8ZsSv7jM6VCbTqEEflxGIK-aA6MGBVmkiSVfZyeYKCvjlS-jCZVnIDCvtyQ32vbykFPsI4af0yaHc8THQgniUuCDdShlwm_r_BXb4Dt5ttDmfEFXnGdY_yvQkgaT0LdD1bU5uYQQiuVXm48QMADFoRTLk4WxcUvTA70wuZ3F2qv7XnXyN6n8flJzXN2udmFZYFuhHVOmo1Wn8nZiNdHiviCr4GGtIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80991" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAu7FUWrflHUrXQ_lY2pxTfmv75dABP-hJqzU6nVsOlvhv6EzzaZJD5XalWhHNSvo3Wlsm7-CyNhDzSQcf4ecyub1JZY6nyFvuWw5H_r4P2Y3dpu9HglMkI0uDq49XvhJu02_W-NjpB_YXlWBUQapPMX9ztMOFlQJqyrZLDdPBLGelMVMEND4IrEJuXJntyunamKg43JmwbraxIPwyFSvXAhcfLxucnZw4QMkzcTAvz-HjFX7OWROsvmyWX_NA635BjdUXgx7FMUCItPJVTR359Ly7wzldRg_T1rMkjcuvqnn1Jkj5xNDH4a1zojLwzzvKiby5jhwP9AkKn4AgQbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUyYkyitZ-ezDJvfweN4ptRa7fFNdqchGGZ6Z3QVZPxk1zwfVY-mIsK8PRf1_O9tQ_0QD3gwfFkrqHTrWX6Us60to3JS_f-WGpaYlqEcPxrctdLH216UNmuNibeEsRDRf7egV9o6XFvTKO1DtGzR9n3gQJrMbAtJfk865hm16YhI9m7yUUisvxMDVvN4woqC387dyJgoKW8MG__X62GDl4bYvjvKbucJ3jnXbqaNo8dxURb3pmv3wlFOacJR72XCf62HFtJE97FpMuY55A7WV6Iusu5ixsfrkt-7zDtdnm2Ex6NYdtXSS--zJfTbcf_la4jVjcknSsVgz1YAuXwqQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری verse خانمی انگلیسی که با خودش ازدواج کرده بود، از خودش طلاق گرفت چون تو رابطه به توافق نرسید و احساس تنهایی میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80989" target="_blank">📅 20:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=Ttre1-xSt1X6tCIr90lhQT5U8WyBfRR1S-HZwDOfBkWYWUJKEHFxlZro1XHRGe7_DUOgov-X7N1PaaqNYdbmOhpqWqP62r5SdAwQhCNVLBhpuannBETF06DmLguTlEgVgHzGJ7qOGR9_HadWJEcNWFCtN43Bi09BcScnJ9azFgYLag99mkj7_OsFZ7D3Ue-Ocg5fClQUftWHHf6TyhLAt8r89XjRmMaMiAz5BOzKGGV94JrqJ9N_CJvRFMxSZ3MC5M2WFjXWQgAtTm4HxWwDekvGhMlIZlIywFXgFza1T1QUFPT8Fanu8xFOfbFncNUe8jd5C9o3DneGxD-CDZ_3cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=Ttre1-xSt1X6tCIr90lhQT5U8WyBfRR1S-HZwDOfBkWYWUJKEHFxlZro1XHRGe7_DUOgov-X7N1PaaqNYdbmOhpqWqP62r5SdAwQhCNVLBhpuannBETF06DmLguTlEgVgHzGJ7qOGR9_HadWJEcNWFCtN43Bi09BcScnJ9azFgYLag99mkj7_OsFZ7D3Ue-Ocg5fClQUftWHHf6TyhLAt8r89XjRmMaMiAz5BOzKGGV94JrqJ9N_CJvRFMxSZ3MC5M2WFjXWQgAtTm4HxWwDekvGhMlIZlIywFXgFza1T1QUFPT8Fanu8xFOfbFncNUe8jd5C9o3DneGxD-CDZ_3cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80988" target="_blank">📅 19:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro  پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان ‌
🌀
2 کاربره | 149 هزار تومان
🌀
3 کاربره | 199 هزار تومان  پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80987" target="_blank">📅 19:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRetro Channel</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3-sEZGZD9ZXQ1YI-up1fTwbMCifzJWS1RXMyP684HhlYOTI36iEzKCjZ8WzSgJSXf3waAE8d-VjHv0frnQ9SRegtuyh739OFLcmEXg3c5-JPzdM6M7HK0Dv_pT27rDHNZEvultOGex_wsip0SvuM7WQ7RM0fD0i1HAx3_nQCkjiIeMW9Xe1J8i7NNXbpd0JR8VWdZRT2u5Olr3MQKJgVv9tjVP1Ot7u7Ok1C9j9JVw_G7zQf2ZpGya7-0MswpNyzpXGIREwzYZH9NMS2IlLUEsAWg1FVk9hgzq5S-PDjrllTcMtw5Y7ss3nwo5N9uScMrjkTyi_ifgtLkDAmUUvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro
پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان
‌
🌀
2 کاربره |
149 هزار تومان
🌀
3 کاربره |
199 هزار تومان
پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110 هزار تومان
🌀
100 گیگ | 175 هزار تومان
پلن حجمی
1️⃣
ماهه VIP :
🌀
5 گیگ | 35 هزار تومان
🌀
10 گیگ | 60 هزار تومان
🌀
20 گیگ | 100 هزار تومان
🌀
50 گیگ | 200 هزار تومان
🌀
100 گیگ | 350 هزار تومان
تمامی پلن ها دارای تست رایگان میباشند.
⚡
پلن های حجمی بدون محدود کاربر هستند.
♾
مولتی لوکیشن
💸
پشتیبانی
7️⃣
/
4️⃣
2️⃣
🏪
⭐
با تهیه یک اشتراک Retro، به اینترنت آزاد و بدون محدودیت دسترسی خواهید داشت.
⭐
خرید
|
کانال
|
پشتیبانی</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80986" target="_blank">📅 19:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80983">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uboXJqMtiNAqbR6VbOuS_OPD3rD1Xy39Pq1MKaQzsnwJA6OqxNIt1YN0Pk83JDI9nDIKApg3djeFK_OVryMQrOT1W5ZjD_C_pJUOCL8z4TCqY9gEXE-c9ZOF0SvtXWnuXQgv0L835DXU8IhVbSjlSe8OzR6ZozbSQrERe_Jn-jyxn0WSRHBrMHYdKZHHAmXnwznS74Jv3iig5ublNV5cDOFIA1TU7yqtvu8wmw2dRM7xsuzwUXXym5SEwmNahRSjI7B_-jkgkfpoTWAANzqHGhYIV2408sNHyIeg0kbJKRaWTjEXzxGj72RoivE-WnNNLk0zWx71OdBh10vt5VB_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quKYZELNA1fxdSSmnFgXCePbAlQV2r_jHNG6KbGLmbyau6esorrbuvT9AOE2wnosbpCksFQr6yurJvbzxWVwJgKCjM1G06jFYfeOjXCq8oxRvZeq2vSAL-IMJbW_4acw9qDnn2gTOTmVoRPgmdDIUpElhpi9zjt599SMyG6-4iiuptx-n4fRYQEqzwaA5Moe5thyYSbDs9XO6r-RJVj1wKsEbhpRTFoZghk2gv51Xn967n46x0rx1BHccdbtCCrwOOMhlkz4jzdqTo2fBPN-NJsI_Rs_SCghUcdbqy2_RtbOg5eDlTpuHguR6xv9JBud0Rj_Isc_4Yr9iOmxcYBtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPmnCocZ2PuWEvR-8KkQpjbHBnzlIRRsptblm_e8fxfecSAmE8BlBviPuy59hTeJZp1XaRakYj5hqxQc88OTUW_lFpTgspQWJy6jTsU0ofyl5rLOm3ve4bsc5k3GsFE_apwZ18hqTP-_UV-Sux_gWjKDQ7wa_dUWrrP8gt-p31MjoNijoZJPF-6abeBmCgKbN9sv1_Mnb8-P6dRBl26daiaYjjzzBvYovbrugQUYLX5jyhugxA6tOFdirKLdRrYE11SVbnzAj0Z-q_f1dPKf6Wbpn2upeOiw8d_0T--fvSb0NTmjcaji7UlHeFQDQoxgzK5u3lenevP7eJk9Ew2nLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فعلا عکسا ربکا رو ببیند تا من برم و برگردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80983" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80982">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=WhP6ZZ8_dxrwzRVOoDIfRPOLOUF914phy3hzpRXtUzzjFEGjPPGgunGMlGST-Nj15dRBDDHnLAUohw7nR3tBJHzRWrfMMeB9_ibuwvuvHwSX2iiCdB2-Zf9p2uvCaDs9yqyTxPcDpTDxGsgfMH5MlvYFiwCkfvcz24ZQnaU7412YRVDb2uBN7ox2cXplxOBt35lM0rERF-W5_8up0ClCcT2WOPZBnAxetOA9boM7YvBGwP8tXxVlOGotfQO5Smi66tLH9vj9AgI68Bx_iLyON9c-ZRem1ihXpVburENbTvr0Qx4nFcyrTn84qPKtLoJKIpStVZp8BOc_F7WJa_gtmLdhLXK_GzDR0zWNbGcB2Tz0E1rHo_-rbq8rIfM7hIUQNb8VBhBeAh8Dr6rGrSoJJflynw01iyThevWrgvqwjNjNQ9WgcVO-k8f-zAXNeZIkND4hZtpDULItSMgDi-eiaI6wjlMQIi8vpHbHtcVGTQodduFcS_z4nj5QRTQN_fq_YcVqGkUVvbB7V3rJv2YeNzL8AP-uGV61u-UxFKdwXjnf0GMr4yxzvKYsggbr3T8I_QOD8NmmUEcfOgk0WnL-Qt9TKWAhmYBhiaS4H-eiTjinCGsDIUD5w3PtP9XyNw00c7c4R4WgcpyqvMj-BN7f_DNQ8yKHnsNSCC2CYEszjbc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=WhP6ZZ8_dxrwzRVOoDIfRPOLOUF914phy3hzpRXtUzzjFEGjPPGgunGMlGST-Nj15dRBDDHnLAUohw7nR3tBJHzRWrfMMeB9_ibuwvuvHwSX2iiCdB2-Zf9p2uvCaDs9yqyTxPcDpTDxGsgfMH5MlvYFiwCkfvcz24ZQnaU7412YRVDb2uBN7ox2cXplxOBt35lM0rERF-W5_8up0ClCcT2WOPZBnAxetOA9boM7YvBGwP8tXxVlOGotfQO5Smi66tLH9vj9AgI68Bx_iLyON9c-ZRem1ihXpVburENbTvr0Qx4nFcyrTn84qPKtLoJKIpStVZp8BOc_F7WJa_gtmLdhLXK_GzDR0zWNbGcB2Tz0E1rHo_-rbq8rIfM7hIUQNb8VBhBeAh8Dr6rGrSoJJflynw01iyThevWrgvqwjNjNQ9WgcVO-k8f-zAXNeZIkND4hZtpDULItSMgDi-eiaI6wjlMQIi8vpHbHtcVGTQodduFcS_z4nj5QRTQN_fq_YcVqGkUVvbB7V3rJv2YeNzL8AP-uGV61u-UxFKdwXjnf0GMr4yxzvKYsggbr3T8I_QOD8NmmUEcfOgk0WnL-Qt9TKWAhmYBhiaS4H-eiTjinCGsDIUD5w3PtP9XyNw00c7c4R4WgcpyqvMj-BN7f_DNQ8yKHnsNSCC2CYEszjbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80982" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80981">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqpszViuBltNzGJTp7te_hdwMrY7brAyMCcTDfplPtXEjJaGAG17YQCI4gQhRIvkNvoAmWPe8eNcuP4xjpykolxabh26AiHSO-3wNUF24oxgH6L4qInd5cEqKF_hDhmvoFYFc85HD6_sY6_P3H12iA-yErWpunnj5-h8EqkSxLYV7TP8m6EGQ5occrF8kdJba0z3uWgbZRbPJvoNx1nKKQNuJuBADDFWPbayD7rI9N7pLFy84PaxVR-nkTGPIQDG7XbfsaO15apkwh-Mn6WAy-8qpUse4qAZktVMPgfL-EeSpWDE5uA1FBPzQ05XItAQHxaajd_bJZAKtrUUoMt8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی جبهه مقاومت شعبه اروپا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80981" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80980">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV1EUidGn_m8RA3UyIW8sIEBjNBRBI9QwGjOrfXp02KxRiMfwkbjgwgqyQikkUiMmYNPJs41GGdDVKMGEcSFpOPUWF-lxZKYTUklJtWqSs3isoLp0AQ8ZS57xBeZrORw79XtWQ6Z7rwaUIXr_vBHubwPxzVqqGYAmLEixmA7nnwZOohp8v5xJjVzUcstaBRPPqTTPlRkSV3qogEECEcWiAB1gVBeggpQEDGpB5qHkNN6RVGrMtdvcD8urx92hOu7aSTeLGpce7NTc8qdZzxebBEcaKid9ls8bs2cBaZFSYRR_IhJ4u3qwuwtP96dolYLui1oLBDJN8sCKUBh1GUaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز پنج هزار دلاری بلک‌جک زنده
🃏
🔥
با ثبت پیش‌بینی حداقل ۵۰٫۰۰۰ ریالی در بازی بلک‌جک زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۵ هزار دلاری بت فوروارد دریافت کنید. در صورتی که جزو ۵۰ نفر برتر تورنمنت باشید بر اساس رتبه تا سقف ۲۰ میلیون ریال هدیه نقدی به شما تعلق خواهد گرفت.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BLN
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g30
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80980" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b79960724.mp4?token=S94K5n6zRUVQAHCrwly1a039jsp7EvU_Z-5BT2ddwzxNOWm_dNQ7AjYNG4Gw65AjRhNtKWGMc1tNszG-I6nq438l97Hc2x19FjoSWbn0IyixuqJ2KZjmuvO3lGH_2eTSCJKDCffEB10HOdOvbhILwnkhlYgYZ-aoH5Ln-s3L3oRAuml5X_NABuvCsX27aMv2K4ygSAzZVIkPbP6UtOlQ65G39XwBHMWoG-xDgtdC_aqFEXLHD-SepQfaakMOjbelW7D0FKLiiUm0MsMo8DwRen6yV7JNpGZ02dbEfo63oZTizJIGrTkbZznKDLUVycRT1bx-qpD_mcFv9ejUS3IvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b79960724.mp4?token=S94K5n6zRUVQAHCrwly1a039jsp7EvU_Z-5BT2ddwzxNOWm_dNQ7AjYNG4Gw65AjRhNtKWGMc1tNszG-I6nq438l97Hc2x19FjoSWbn0IyixuqJ2KZjmuvO3lGH_2eTSCJKDCffEB10HOdOvbhILwnkhlYgYZ-aoH5Ln-s3L3oRAuml5X_NABuvCsX27aMv2K4ygSAzZVIkPbP6UtOlQ65G39XwBHMWoG-xDgtdC_aqFEXLHD-SepQfaakMOjbelW7D0FKLiiUm0MsMo8DwRen6yV7JNpGZ02dbEfo63oZTizJIGrTkbZznKDLUVycRT1bx-qpD_mcFv9ejUS3IvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو جشن قهرمانی اسپانیا یرمی پینو رو اینطوری معرفی کردند:
قبلنا بهش میگفتند کریس رونالدو ولی فرقشون اینه که پینو جام جهانی برده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80978" target="_blank">📅 18:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80977">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](𝙼𝚎𝚑𝚍𝚒)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPy-b2MDhr_W2MS9H2am4uhzmAhDMEF4v4hD_LhGFpQIPK6NzlAUVo3KRJv-Mau7R_QaXrwnHvo3bOq6PdIb9fdRYFnPOSbS5fGsLoGKH4gBJkopYrWCQQdldDhMKeOKA03EaEaGJNcexy1HLPdHuU1mA7HQA5jjzUZtFyFxjTZqcInt-AkaMbeqVg_y9vjuvXCsTR4BG3iSbJ5H0Le7BmbnGDw6FhqXfPZRdsOw1VBIMIkhpDzLz59h-WHf3GyxjLpZC4KHsXi0AVHiT8PEd2G2Dw4pix9SpHh2EDOk2fiZdjcGI3d7tuR73X_NvbvRbhSXqSYWqG1Q-xGfznvVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف نبود</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80977" target="_blank">📅 18:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80975">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بگردید کارنامه منو تو چنل پیدا کنید، قبل امتحانا یسر نگاش کنید امید به زندگی بگیرید</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80975" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امتحاناتون چطور میگذره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80974" target="_blank">📅 18:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب دیگه چخبر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80970" target="_blank">📅 17:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80965" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80964" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عادل با شرف
❤️</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80963" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ما کی باشیم نظر بدیم اصلا، ولش کن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80962" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80961">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80961" target="_blank">📅 17:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80960">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80960" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80959">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJfcsWr3v6AXJE5PSHzckp64df8d8hpGPebR265bARy7Cp61-dnTCAFgOtXH-x6NmGT8UrHq9qVWTtyCZdI3wOcVuf4U1svwH4CFoUFvyGNnaRPAAX4VGblY9fYEzmHTbpbqlA2PF-rfb_H4h_s3_pzUDBBzIUahCEGfsGaZOw70PUh9GMxvkf-dnDrH7bICRCgqdCszERaOgPcTRusAtPppQnPv7F-XkMqSMEtP2roGdx2E12pBCkjR0joziTlvFIHC6Yd26TG9H1NpZxo0-i2bTmf6ptHNuQkzb0a8YhJMlzNcWsMUDQni33cY5jUYG09dUdVqDINkwb59zmQecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80959" target="_blank">📅 16:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDZHLrRQMEVKHNLKDBKpe_YzXpim2ypz26-eHi7s9Ew8Zh9f8HEpN-yEg3iOGSYm-cASTCPhA0WfwwkRcrVVnkUh9Gz4NSH23NVhVu87AgSd1vS__ZrfpbgY1O8AVO-R-qwOfUof4R2z6siy2mwXcamL1lcIIkyAKx9L2m-LvVRDd5gSO3OpplmfVSaGVqpG_Dq3O2DDV97j90K8pr8uFfxrCZD5e9zIJjyYmCwzMVTdMkyxJ449J76LckdsNDJyTjwIIUQL_UJvf_f0894nAEFIXfhEQtjgP4K7anfRKVZuKnIuy5jijepuut8sQ6kxSIB0gGVpI9Y-8-aZ674yZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم ناجی و تتویی که خیلی وقت پیش از چشماش زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80958" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80957">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انقدر هوا گرمه که هر روز از دیروز آدم پخته تری میشم.
پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80957" target="_blank">📅 16:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80955">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80955" target="_blank">📅 15:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بارسا لاپورتو گرفت</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80954" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جرزوالم پست: ترامپ پیشنهاد قطر و پاکستان برای آتش بس ده روز با ایران را رد کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80953" target="_blank">📅 15:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80952" target="_blank">📅 14:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=bLwtJtQrqrzO7RQbWdjwb8iBdVA4SsZsIaLUVxe4KSBKD2xS_Ult9CSNXqoF_aSTC1RgkrlQeSg7z5nqQSxS1eN_awA5pDI93Ao80p-H4pdixKbuS1pNgrelrG7JmUpdpk15kYKkw-o8Lja9o9YwSvbG6cU4waQ6jdVf7pryQOy4Ztwu0qCtDT78Ps8VcNR42NKayZFy_l-attyqbESPckPRB_Yla1uopa0kdBxBI5kxFamXaoUK_nKAarTFtYfAl7VyUCHfwe7Vlkevttz8Fak0wQ6mNEy7NU2xXbEgtJ5ta5pW5JS98kpxFcA5YfpIszNdeREHXdBDkmI3ui4ttw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=bLwtJtQrqrzO7RQbWdjwb8iBdVA4SsZsIaLUVxe4KSBKD2xS_Ult9CSNXqoF_aSTC1RgkrlQeSg7z5nqQSxS1eN_awA5pDI93Ao80p-H4pdixKbuS1pNgrelrG7JmUpdpk15kYKkw-o8Lja9o9YwSvbG6cU4waQ6jdVf7pryQOy4Ztwu0qCtDT78Ps8VcNR42NKayZFy_l-attyqbESPckPRB_Yla1uopa0kdBxBI5kxFamXaoUK_nKAarTFtYfAl7VyUCHfwe7Vlkevttz8Fak0wQ6mNEy7NU2xXbEgtJ5ta5pW5JS98kpxFcA5YfpIszNdeREHXdBDkmI3ui4ttw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80951" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قاطی "همون همیشگی" امشب یه همون همیشگی دیگه هم هست و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80950" target="_blank">📅 14:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80949" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80948" target="_blank">📅 13:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkYIRiWYNooXdQH5Uge10oiEwSFbJ_1JgZwt8KneFGkVa6jZTlL5KBDZUayCVH7ouk4YODLi6cyMAoWMzS6BdVOA8BYoKvnU0y3yfmTalspC_L3OihNpLgPRFNIeDOS_DLBno4eAOo3WQcZ6asXIKMTEjl02ZOE_hr-qkKK12l8JwM0Fan24p7jnwJuthuJOm1pcC64oPDRD8hMyxcPiLwxPv98auXEZLcotNN8nj4gTQ_x2dISxCB5WIr4mhJ-3LwLdom0rqbh2Rirf9F2-1PGpgZDn13n3xApdpTdpKzQGa3E82KmewHQIqOqxRwkOExn-oqf5luTbNLw_aDs6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید چه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80947" target="_blank">📅 13:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شات جدید یاس.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80946" target="_blank">📅 13:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شات جدید یاس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80945" target="_blank">📅 12:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGloriø</strong></div>
<div class="tg-text">رنگ پوست رو میخوای چیکار کنی داداش؟</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80944" target="_blank">📅 11:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOqhOXPSbd9xOnPpOvpDb6uHsK49tObX52AN3I58N9_x6y89SHK49rSv0H1fXT2DoXZo3saH9hJavSUDVGfVV6Ja2Nw3LyYuysL7Bbk3664n5FpDvGnKqkb6niDSU7xVOHHaOKeffHGoZikQ1MFAdvta6S3ynurgaJ9jjbxVVeY__Adrr0to0GUkneiSlBr8IHdMjC1Y0LoO7I_hELWGQJpHE0WqV-NTF0GHOwJFXFMBhu1k7YgL-GJmZLDdSAcLM7Yc4rcAJDFhvTUNdKuWGWB1elz0OCzxRa8qvDaePHfKEWs_GLhm5kRkLuGGkCdQATJy8mbKxHtFSr3yiaGxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی، فقط همینو بگم وینیسیوس رفته عمل زیبایی انجام داده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80943" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eac4416dc.mp4?token=vzKJHgJqdwog64mDhLL9Ulu4545hZ3ZOqoOe7kh9k9CTUbWO_pOkHUrnQSnz_xsgjuq0QtClMR1dcyP1BwWHJfQvi_sQk4nx_D9vYhF4xVJZ1-1F5zmQdzTxN6VoKDBNlnQukXAiGGYndwqSpyccQioW3aomq9_IdxiDJmfrk1v9hxZMvuYfox6pl4SG8JY-0ioulFwWM_ShZjf0PIIPAnuaYJAXpw86oyeRuAROjfN1cDvJ_peafHREwqvRt1qGxi3oZtVpgwY8b-HIFlvnDLukR_Wfc6ZZ5jjXJikRQZXqDUOKixtS74J3JY8zLzh_Dh_WOmN-xaHXf56Gi9-_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eac4416dc.mp4?token=vzKJHgJqdwog64mDhLL9Ulu4545hZ3ZOqoOe7kh9k9CTUbWO_pOkHUrnQSnz_xsgjuq0QtClMR1dcyP1BwWHJfQvi_sQk4nx_D9vYhF4xVJZ1-1F5zmQdzTxN6VoKDBNlnQukXAiGGYndwqSpyccQioW3aomq9_IdxiDJmfrk1v9hxZMvuYfox6pl4SG8JY-0ioulFwWM_ShZjf0PIIPAnuaYJAXpw86oyeRuAROjfN1cDvJ_peafHREwqvRt1qGxi3oZtVpgwY8b-HIFlvnDLukR_Wfc6ZZ5jjXJikRQZXqDUOKixtS74J3JY8zLzh_Dh_WOmN-xaHXf56Gi9-_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی عذر می‌خوام بابت تاخیر ولی سلام صبح زیباتون بخیر. 7
اجرای جدید پروردگار و غول ادبیات فارسی.
❤️
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80942" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcsuP5H-HfhRpxpgbhu1ehHVJXlxN7p6M2hnBZhTKZmhNUU20a7baNQG17ZziuQsmmtOMUlsqmkxLh2NOQ2N-ozxXqcoM-Z36SZHtQlHlfax3KxR8PnRegOB1r41wYU0iliPlmHa6Z5Uks_URqUrGsAF17M3iXPzWsdhorX9ezU1ppR1z2QHHhCYgHDLs0Ya3Q00tyCVrb4Xgx4fIxWVVN5WjADgtBq-kpPr5P_xF6CqQ-Adm2vMLcLrsnVK4wqrHjM9g-jOlcVwMefCkH8k-Ljdp6Ecep7DRAjeqaHhecc9fePwEJYH0Qt6QEdiNvzt_Cc129qvYQ3Z_kRwTcl8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز پنج هزار دلاری بلک‌جک زنده
🃏
🔥
با ثبت پیش‌بینی حداقل ۵۰٫۰۰۰ ریالی در بازی بلک‌جک زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۵ هزار دلاری بت فوروارد دریافت کنید. در صورتی که جزو ۵۰ نفر برتر تورنمنت باشید بر اساس رتبه تا سقف ۲۰ میلیون ریال هدیه نقدی به شما تعلق خواهد گرفت.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BLN
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
29
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80941" target="_blank">📅 10:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80939">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هووففف عجب امتحان عربی زبان قرآن سختی بود.
احساس می‌کنم تازه عمق جمله‌ی عرب هر چه باشد مرا دشمن است رو درک کردم.
@FunHipHop</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80939" target="_blank">📅 10:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80938">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUfhZ4_BeKsGvoBQqNpA3KpJNVw_jKCXHDcOHJBTN2pSq62X2IToDRGCuu8W8f2fw1npSYsUi3Fk8hNpDzWspLsxTNC-O3wRTtj4sLEWzSthgIS9C0aRJ7T2Cc5xYRu-pJAQ9X7HQrzM6VKBXRYrmL6jbm_OGN6piPWE6N0X8LN06Kn0c6OhPfHyS2ht7ASw9vlP4DF_pm78p6HyCi_WtPs06Z4_brvxwet3Tm3YTvRqpk8-x4-l5-Ns_6jgeU-S24IB1Cdz8kjzn2IZNhu8C-husVL4_6qaNlHlc_92alGX8mrG8YuUK1FbDta_iaLYrkb7jzHPbX1SJCA8saJABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند سوخت رسان به همراه چندین جنگنده و بمب‌افکن حامل میز و صندلی‌های بسیار بزرگ برای برگزاری مراسم تاجگذاری محمد سامتینگ شاه در حال حرکت به سمت خاورمیانه هستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80938" target="_blank">📅 10:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srKJ4SPk0Il_YMhycZ0bKAhCcKMo3md_jBRRN1wH9dB6G_kgQFkpa3Ex5TldnrNPkQhJrCX5sbcHkPaYG9G1cnVvuf-pc8P8gJwMawRUwZXlqs9is2LhcUXOxobhafrIk_W1pQuQxCznM16O68lYDIFqEg-qtga8hPSfnQcand-lbKLTth-FV1A-0jgf1MRaFHaJFGHGZRop9mVGU71sSgv3XTL9LSEhaXsxUfnUEbEA-gNhaL0i1tdCx5j0ii6nRHfj5gPFE-hfDGi2R9r13m1Vc29kltIffxpp8igHOYEAn5bvq-1qoQVZVs5mKAAK0kJuhlMouZByB6RlwpTHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی چیکار کردی ایکس هم دیگ سالم نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80937" target="_blank">📅 08:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZB3gsLUI3_I_C5n-Pa9DzhzlHNYkPrvkrM2WQKh8wEs2PuuUfzfig1gqedk9w-pLhIYPBrPHN1o3WTv4spgp_-ZNiIGnItuiIetSi7OqFFBtn2_3Yw1T8506-xWNiYUT-Qtqpj20rwWzku71vL2MqiqgACv9xqAbsbJpb0BbVbKLp0QZpMxWsS_Z9aYNCHzTrGA2Fc9AcbLoa-_CJHcdK6JceHRPzbKze48YjvH5LE0mwjC9GkKVxAgwRvh8dTTWdDuVAcPRZovNGxVvlVp7yPaj5vGpcPaMT5u9lNgS4Hu4DMT7l5sV9FMr7w96aAurGv5nLaYxmLGI3OIgVV7_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vv9YspZXoKKY731kT_rtMoGk8Qc-DNR1guYw1ty3SyH8-0JTcGoGpcQVNsUiN0PGTnZUH0TCHQO82MoKwO2qX2xhIyHso6Td7793_NXJPwDEnUbtrkn2LUrczQ-s02HLJF84BDzQYWtGbROyslLLT8zzG-QFFLskKd7_aruSCtGn-Z4pEp1h4pSBzlNAXUCzSjNq4Tof48of4NiRD8XeoKttqHvWtx2UUmdbuyaWF3OLybijFh1BfFysK5sNMzUpCr7OXwTUlqKtpuN4sbLpscQVOkYeb3kE8vfXGqYoMvI8sXfGKBoIal6uej5OEE4Gy5SOTwrlsRcBMiHoGE5r0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنده به عنوان ادمین یه رسانه شرقی در برابر رسانه های غربی می ایستم تا حق ملت بزرگ تورک خورده نشه
✊🏿
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80935" target="_blank">📅 07:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3oa9OkHIBC-7K5J_yFoKdKykYLGQHpcx2N-EDMQyzIA9PKcTV0EwuH-E3d_IcPyBUtNebffjyw1nKcBzrszH2EoIg45SiwCs11FY4ezoDIGDP9AcOEcL2v-cL3nSF6W1UWb44PKCjg3YdXnxgI0W4hp6BZsFQiVZ-WSPSCQe9xym5wzhVmW2_MJW-WsFO4owN2ycoSNFsxZ5iZhCv1jBlYLVR8Nidzg9OLKYoUJ-es5eGQ_xkNwidQxshNIUk3rtcZX6zCFDAw5F12_Xux7hbIOJBT29h54pcN4W6gSLfaPctUeNzNcG2oi7tVzvmy_7EVZXQuuSA6ivpr7vPh4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا دید دیگه کار از هشدار به آمریکایی‌های ساکن ایران یا خاورمیانه گذشته، یه هشدار امنیتی جهانی برا تمام آمریکایی تو سراسر جهان به دلیل «افزایش تنش در خاورمیانه» صادر کرد و بهشون گفت مراقب خودتون باشید خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80934" target="_blank">📅 05:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmA9oFrJBJmYIlnt9_cgBArChdELaQkaDBMzzayIAtB4VSZ0URVlzYh3SebbKyVJtoU7I5F3pfjtw9eGE_ljR3NDFhHECvguReLWnGTxz8MB9j0SWMGOEmzYrieN6vWoOk5sDMIbYU16bz-JT0HRb4WgFIcVPTIfP-JFZcmi7ndKk4SDAHmzeWN5xhHRm9ZjCcgh7WWWYqL28iL0oog-3-2nX2eaytAtbMBPGNf3Vrvhnqt8CGueImTXG6Z7SVGJy37bwUXFb2avz95E-zd4RP_dHUYVaO47OeixDlyOtRLzU3SzRDqF1DmlId6Bv3KLc53vw1VuxPnA_E8_7xWP-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری ترامپ از ایفانتینو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80933" target="_blank">📅 03:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چرا قبل مهاجرت کسی نگفت که خارجی ها چیزی به نام تعارف ندارن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80932" target="_blank">📅 02:17 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
