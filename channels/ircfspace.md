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
<img src="https://cdn1.telesco.pe/file/m3N26jRdNK7oYAJdpZfdVpPR0GC9giGnJVidlMLnfeLzgN0gR4Pfy6fsFqP0BFVH-EUZngp34CMa6KFL4MVN9CEGGHrsW9AsHtL1AkhGJzJ2PIQFGOoiXvkO4v7a2SjO1BPEAM7flYkga2zTNveCmDcZzJtKkigoJGDiYWpQ4hz6x0j0Exd4yix1iHp5TDftYK8Bsb0e4fSnkZBnnP0nf_ExRdFeMNliiGXB-FPGYVV49MbEAyW3w0qylwFv8KBZrlEPqgrGOYAG7TeJ1Anb1yWUO3fKuFFlMtC6HhBnorQQOQX5QnWMfyaf7f71K9vsz7hA2WorL4GlXgR_GggP-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 97.5K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 23:41:06</div>
<hr>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bP2cKnx4n0kN8J7x5dbhwoPUoFxgBFJ9LrEeZhdL-knSGPMjhcvXtf5MuLdGKK5FgInfoiX1zuW4oTwhcifplbm-2QfCubLuAyb6ZavPqUqiZH-YU__Q5MEXyb7mB9MkAvYP8oo_MRc7lNBFsqiue6cNTIjFjYJnXg72dC8tfJUBlK0M0gu17m1Wi_PiWc6qr1CIOFyinNAHSe4I6F980Dwtt6NGTVsM2LN_9h5NaJf-zDHYbim2zAAGLBBTjH-qIIoYKicA2rrm3Gmp2yQ95UYbvUEtdPPwcz-NPxZcW3RIOWhDpEYIy_j1p_rTfF_qCxr1FkkBo71YMTc8xH2niA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BrCv1y3AMXsMrVJHNwGgr2nLJ_I--rdsLAAbnIRqQ6GVpx3aB2vftxodubkVDM8NS_zx6hJt3xNdlzbw7g5XkieBeswbspQh75fzg8ui-KXhGgINve3Wk4239pCdyMh8f7Jw7XqenTwlpMS4vNFoyjcGeNKLlaDmTCUNAZGAdLfkL4D28ZoNiRIZnXiKnmpsxidLOwNmNDID0nkaJKsXY3DnmLt85e_9eeRHXwgeBaZ6uuXr3wKDOukR0PnoJLfG3E_xp_R7aYPk4_EDhxCVXwMkUm-HXj4oPsvd9uUdSAmjq20lqxd3bRWJLG1dMq2Uyqxpl8LY1ECkPEIz78cJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nJsLLru91VEkBHHJr5wGAKooLmuE-R4qz_su9IOfJtccXb6aTmwKlWi1Rzr4OsRaQPsrseq8y2E_42q-en-HftYVM9cKG6WVFlcX4rLfiCZXevHUeuox6yxkykjcYKxhpA_qSxo7tY_rhKYZcNWDqfYeg81kRy05feTz9JWvi82crCQLYrZ03Vga5zXqFMPFM3JNgbjzic7vP6ahuJTf3h-sZ-6p49nJc-keNs1UdYph6cCty0Iv1zru9qRyDDg89Wu_v76TkeRYvgbK0ijLLUibnddJuxEFGRo4uvjdjBz8uebzPTjEZBwWCm3YzyHs03r25SL5XV5GgtpcGyDWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WEk5pcvz1xOWN1r5Wgu4iVrmKB3Wkn-exgDGg5MEprQPvIKGQoglMOAwN_yzHQvEVB1ImBDs1E_kpY-rdc65QDtDrRniVjEDJy_v1PnGgDhB5apYe8xfRhbVEGiXG-NRX8It-ps2eE3j0fyNzIP9thy3UrE-IIbJhX0QPPaFpmXHULpOfE_jdCshxYNEF4hW4HVSYmhdS3CMlWXk1VIO-HyTcGWvNvwGkSy0z9I5HcnCbarEyZ_EwBKywQzFnw7PEfBrgOAPeMIcSJ-Crbz_VnVo4lrl8IomhXw-SICv1SCeBIOATf7EV5VZrqOoS4CPGTN0vR-thzftaJitzjaqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eH5ZzqTTc107JVWolwz47-2q54kn9QW3-y8yw7-unF0nNdT4aGXbtrfGpXmvFTO5UVkwSUzwXUld3Gsz_uN0JlL5XTDEAnAqvcmRcILbRAxsu8MQJklNRVPc2Uk_sjph0-z1icguCWlRdHYBHNzsslXG4V0pVilQ3z_cUMnh6ND22BV4rLQiz5Yq9bR1pKkdbuUCP3gugyH3sE4qwcWtE_vmW3nO8q-pS8NYr5QBt97JqxxzRUD7DJRQ5h2nRdpQkwNN0Mj0w_aotkIAV_6khb_VHZMjHBAFH1subb5--CqA2DmqulbHYxuLD-SraxahuGyDtgmOPoSJmc8W14uxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oyyVRqzqSOYqiCVPyoGaCzYnT9kpI7XI6GyPiLvZoEd_vQd2gXuNpmrhq-n8yVbKwa-25saI5dRENX4ySHVU3V5iAJ-MGPFITFHVI2owPxQz2HK9kiaD4mZTTi-RT6OTH7XdWwFow-ylmviUCxsGLlx_ciAomv4P3yVJY_ZobNqFHLUdF0DJy2BbqlLbTjsT1YHIGMi9ajUt13_1aOVdqY0Dslw8iMeYBAFCJutmWhidDih-Cnd3xa0kKaMBeBG_IOxBUihhoNhfVZpUH0OyZ2IgyLtr3QH42nPUrcQddt6tct3zKEeCPQet3fpCOP6Oug8e-zuU2wX0UPDXoNe3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MSl7GwO80iNFYHToZi650TDN5rqmdL-zPBWYFlgYSsE9FhKu-5z5vz_l1VGuQMOLACSnwbkGAxOqkr6NRHdEqifrhVHp4vdltC5dEPh-3xWgYIr8GDSd4R-Bd44JCPe5QUJBUbLB2qOJQo7wItnpLFqzquM8ul1IEsDLUCrNqx_CAUUDBSfylhGbM6zNpS6pGR7-PHKWD3LQMaeFXP0uMW0P2X62H8DIVy5RHn2V2ccffNzAH-0i2TLyRhkE_q_R8gXo4Bze_pUUyZxQYjkuShIXU-oLBNiYJq_zhfTbqmH_X0tGYZMjjAHn_k0W5pqxeOl1bLUjJ9uy0VshGIorBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LrHf3RCHYxwFWfQuMFWcrdJvsa2uS_tSx9iDc9kHMNOWAz8Ln0WiP-u3hP1hoh7S0pjxVI4DJ8c_mV8DtwZBZ0Zk4zgaipoOJhN1ufSIzm97Xv0zy9kek1KeXze9_55ouS2DsmCSEBH8AEMDejIrCDvZ7WQt9N4ROTT6H8ukpRYIeZgJwkZ7plG4hkn_JA4UGqy7T01VDrAxjAmVvvEy-1q9ARrJ4E4tC77WJU4z-1v-NXuyfF82x9-SW_X-ErKr4H0WRl4-7OGz0pDnwvPg4HnH3h-h8tmfHM_TJ1k2DYZ1nW603uG13VHjHUppU-QCCQJ98N1s04sqzfDU5UrkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ECqzosGVT9cnotdjukxmBb4WkIQ8BDce8NXK5hjZ0cXIx-aKseSALkw0X2Wta33wBCmOcLMxjwI6PRWIJDAJpJMXP7pi_oLsxeJo1BwQmq_xkNTXlV7FIpQyAnQO62rYy-26-28kBrMtbtpsXf2q7-7EYNnLXInW-j24PQs6mpOVLK6owlu3WqNCA6vUBWp_rdt9MDk1SXhD1FQyMR9y89gY0GsfgPnnp9wIzufW_9yyveIKG71dwQvacgZZ4JLE3R8SAZelQAN07aHjdHbsoch_5qQmeZt2FodA7RRTz4bgObWUPS2Xw109q3iE_gtsyRSUXBP9i1b2ZSnoOGSyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qiuq9dDERf2FMbq7TLyNBfoPTmgwSa09L_wanW8msYWR2bXHKYD6_8su1NaYFSL5Gk7gCXcRLoX6xFW0eSGUqKkCvWetX_tPJsnySJp08ypMtwVWDh6I2YYa4QKOWYWRy7R7rbGW-ABEboqA0GscvSLT2qzDmFUKYT1IbyiVBwhij9ggWKLMYcI1_FBOmhtL4ZTOTou4V4SKsM4btA46LWmxxveq1_WcQ6eBUA9kOQxRptoKzh-Qo-App4JBHi92swW9ywLVlYAOdRDQpO8vxlpCM2LJd_cHWGZGH4rasiDuWo3WB4W5FjlldA5vRzZBphCjesCn-Thftz1VL8At_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1fomiPiCuz1AbTjOLhjwWzGNLWU-sw7-qzvtySnU5xFwC-IkJuMd05rYNFCTqTnM17FynXVnRhUvS0KJr8UxXS8L0xQPj9vyv1iCr5kNyViqSjoeY6fBRXOAfjHJsiHC3SgXhIg7u1SiaBDnekgWsO5G4k0BSVavHTyR-ixuIqnWQp7ISHRmNITzmYIigIfgYrxYmf-1lIzk8XxXO8WvQLzdgCBrpcodh1X1KkiXcdtpIRw5-JzDYfKBRsxRzniMwU1B741J0vhZ5t9ZzHQdWhfkr6fAcsxZqUpSwOWNzCO-OLZEQKti8Q-yDKHOL2U9MA5FBQgtX-eHHCdyH3AoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dqjampxtG00xJdo8zsMOrf1n51NLAbGtv7DdRnWrPlo8ft1ea__kbLFgtk_DRLvLX2z707M7pXvUd7e8UKqd1fvgoxeeRSX_tsS1Ov6v1kkDo4bMEfr8SAZZ21qpUkJUtRg2EDfLKoVHhiIzzIDqCf3gvK1XeAbx2wesp_sxbx0KdI0Nt2VqmtqxYTCbIOAB-ooq8DPsmt5V8ALkZ_YpvMSvB1n75s_2o534Y8hYhoKE9c0pi-6ZUfWAZrtyfLWgeKzcNDJN7QgwfEGmv4yZeM2fHewLy69EtaPraM28Y57Wtp_lWy6yM0m6AjjW82vwoCsqGd6ZK2m5bfRDUBJu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWanE-kDb3c2ntGvaMZu53UePRuIZLPx--PYLadNZGXgVYkBVMrvsnnUwhvXddRGY7EUETWocynhKTnW_wBJwuar0-JAXbr2ms4xFsCMmg9do-Zn_5cwjOYtbly7h8ttmx0n67UEoSHZUn5cQ8jYL-lju9M8QSXDHY1KSxMMhJ7_pvQVue592ss_VpGxHTRWNA8-0a7WF5psAP6LZwyGYgqGUmgKYtEpIAlPwrux36ke1IbEgQQDd3vl8HA-bw618rDJKJwYcGA2wFtxcHNEVckMghM8gpmfnIpVgPLcazYfxbo9kQQ9mJ5TrWQEZrSdtLQznOt4cqQ2RIoVx_0cwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/II0MczzeogXTKoKTQRKGYzi4s854VBTImCEg8VRjscZGCiwzy1L3KABBMm2_0awlW_QkLOQr_Hzrs5iAwOFKAVBPvmJqdmEVhRJ_jl8YuV1bS6TImY-WHp7DwuGpz7Krq6txfdv63ZhWHQTGHRCLaXrysHRCa2itb29wAnhDwFvdW1GXSyIc_-_OYyjjdZEGiG3OE_gmJJoEse0kHm1QMEQR7COZ0S4gIMD8u7pZepn3tDiBAObUVhLfJlSk-c1s7IeDs6cjb_jdAOn1lCXOusf6UelUfErIigHg0maSTzrG5Y8gR9Fc81RnpMza_RCZP5Lo2BFyL8iOpBEYV9_W9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EtjgFM7sIFVHrx0UwHq4OdZ_tXCiC0VBhzrMldMCgzAQXI4t5AyHfohLRskorCkY-DLL-sNWJ42AOnq1Nit2Fqqk1PSpAwNYWSLnGwI8yJjF7Pr6BsQfSeE2O-daAj6MEM8lMVAF7I3UDxtpCmxFH7m3_p8HQK6tgQBMq8eepLO2Wm_T7tbHWxV5D-dGUrOWrlbRIURXl4T8VeD3eTu9zgjDQ1p9rNFOV-bG8yax0VDhuVUxrh2Tn9WbS9r6CxmDUMcOYOD3lO_SO2VMyogzTcOnc7pf0MvMMDsOlJ_YF7KmT91d9wdxtSCB80taaRN9kQkcWzkzk3vnzdGPLzu8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CNtrC_7YsMtyW6__aoZ08F-Cgy_3t6G4T-0UjAlwheQyr1I3hZy3tIOECvl0dKCel6nR_YL2StNLxZfvmK9GlgL8jkCwGIdoHxRfDNkFskPY5XchknYK48pjlCgxO5c_IoTw8GScSwZnTI_Iu-E9Tyv_L5hfSQuv28iXczAA_mDbGR-7eAOFrAatNMN67VxXWT2Ug4foYI8Ao8l8awo3i9myCQ2E4GKV0J1MV04Z6nSCVCdCBNzSOGBUjk_uqCEt2Qx5MKH1sz6Bjthf8_Ke-3nYwWwtSZoojP53bfzpN9yJBeAnkaZZWRd9X0IKSrbpKPJTWFfRR7EiAQ2cI-VMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSeuOvmLDytD3U8GvWfhDxc6WTRPi4VZyR8Nad5Q06hN7Ad83duDh7uMa800z5X_rZl85gbucHJdvuP-slrpWdq-CIalRmt93YSbzgM7ipeQfiGWN5oWzJdcGV80YbxBUP9_Rv1_cedhqRCC9q8mjQZXy48jJBDOIX1b4Qx_vnSNTUOf_4zXW5rirHjY8_XSEbbRMZm79HXdsbl-3r1ciKHWnYpN0Lga4prLbRxLidmkKHRVLhxlK7SnhBmC9trtVPH_Pg4x5Qujci9lBD_R3asoSczEMWmBWYtcgOOaHT5E52ZJknPvHzhcNS0M14_sukeRCRUIX6lVL09Ld6ec6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UM0pkixIHv4DXKRliAKT8Qpm6I3NI7MKMrGS4dfE9KW2_9lBUdSVb_tJ-a8SLQwn2bPs8SGIQZo24usho0tp_6Zd1kGLwhxzKSkDMGM2WXqrgnKygzP2MaQlt8_LWuO1-lYALv7sI9lyFphSMQy98UkFnWwMuDGcjsKc62sOG2ut60Rn7aOIKYtUIGi0tl9WxhrHQUvEqcrRVJ2O0X1bzL6hfh8wTwKtYr5qByxHo0T9ByW_Zz-IReRELCcVoSRQ-iv7dj27hoDFErQwoMwHm0kUfK1Hm8SEm66v3j64S_gX4Ku6Mfv7gGVFNd_MV5n5i8UajjYG3IG3lQ9DuRAtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDU4xASFtqHA3uFnoogueAV7omyFOGDWS6gO_7Rq-ORgFwpN_uZEkReJUtmmtEmvyaSc2qkBsFfiUtyaWEbkyVfj86VgtIu4exbrf6jV1XEwKzksuXcuEG1KYkmACiD8_Hu9hzy5d7Ysy-TMcGI5WKxlznLIMPSJosSQY2y2J_7KsIJ_2kzsUg1fqU4H-kPowFK9kXNN7LJx48kK5vLyJMZOJye4r1AIoLVvljX1UTl7tglUomidRmNeGI7ovdzNTurULx5NxOjN5rgYhWnqE6WNBEZVsX99-jnvc3ioZEWVkx02ly2261BFvZA9rKyBi-fxlk2NracMcrjZOHb3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c4etQ3scffvzw46anGCX5fKponcoSt6dsNSshj4Nc83apzYj8p6am_82TeeHzv8GmDZ3QxguIFL5YSOlVTDYAxA1VySBONNIY8zZCSFIkarr2HIUmgRLhjp0g9BcC2nDmASJV72WFBpmVF0344_iSwCxPb5KfMJwjggsNRNMiWnJ_UpJK9Kvr3LqOpGeCMuR63KEX-gVdVtYWLQUUVK77wIvYyjQM6oeJ7puhedG4vGKYaSU5geeJbMcqbf-ZjEzKXKSgxOVo5i01Fz0ktckonOTIJWCcgvGp7c2JD-cgMqd26JEPyI7zLhTkGeIHrwmNBA8Ts30iNPx6ac_nYp-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VcKzX2iPN4kZIb9Ms0V-wOay5m0hwVvty3eGTXkfyQjbeiSfykRxUdhtnybTnXFSArzORzgj80TjiwtW7pTnQ4qPahT3TAD8tNMB-j9aCKhJKrwfV4x9s7NkB8eLbJvzRn1VfRPiYIeOF70Ikcb-lB4j_HomouYyV31VaV-CLEWxzRqS-Jg2GC_EqkQlk7JWZQnsi7Pb9WYI7moMOsG57Qt7WUG04O3P7IX-YlBMzgltuFQ8O14NMJLPJTn4kiGVhxWtzKxSPq3ejFtYMXlgdf7Q_ipRvMGGTWcv3QEv1lLVUjuVTpiLbIqWpSuvBwyxqG4SIVmSrmFqsIXU8kLvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BxRALsW9IpKWTCvGQL_KISeX7SQptSDspam1u78DPZ40QpKyV65171kWp36Ovx_eDeu5sRl3bD5jHud8CT4qYkVDPWQy-ln8Kl0qVWPf676fpOwrPykhTCGZn9encxxRWlnVusQgs7sUHxTT5beq3oleI-tlxWYn4sxd9bV8GY6AnCi9iWFJKsE0oDgK5G5zg9KqHV4WxGmm2NuN0S0GHEQnfHt_P3JCW25g4JO0gCRoH8uVw6o0GYxpkiy86y4vLkcrFD3rba7wclgatQML7pH9lGuDp6FOgRwAAZ2vjDC2N-D4r7HpQOMkb7EYmZc8DgH22_GdN0Faq24rzIJC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MrW_KEAqNnsnK5h-6LI7n7yqEwjukdbYbEem1WFgjI08gYGmuEhdiNuL1jTT4qCO3n36m_W1EUVEJXtk2ZjTpm_04J4nRuU8VV7_GJAnDmxzHIULk5zt2reieoFHIq5g_SgFm0oQ26v-pBNjOYO-wcTFGN15pzMq3pkQq7ZAn0zRHdDWJrPvPxH_8QDZa2kCEuVpwmHCce-uKwlqUm9Vr02ehwLA5HG0qhrryJqa-qyamiMcbsobq05qJpIEH4JGJeMdFdJY-DFK9AilTRo-rjKla6Si6-Wr02yTzxUeDrSejLWoTRW7_bUbaS9gb32uCd9FdOKM3zmulzE9ZFusbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K7L6OCy-OaFUp-rNAGIHt9QfeAnJRZAhm5mR-TvFRE4HY_0XowmS9f9dVuMlnObYtEraR78HdIn9hTj7zLQr3ujTc66ivwVhocUx7cflDnMz0xvInSzg7oTHEy4LN-YOSV3dlmiB78fGvSNGqwYQUUaYDULmyv75mMm6jZb5TKXubroKJXT5wrHQZ3lWWyzMUoYP2MaI6irP_lKEi1Wyeb-7AZ-LvDYyW2WKpt9lzbwkGpOXBbzpj1RuU-hjeoOB4GmeINTuHK1k4zaRp-DMvZki4leaRsZEwVXXe38otanIxEt4reJU4Efqf1kUVme4LKG8P7DLkrQoHqa8jrFIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mEHD1ZJXTuNPYFgb6Vj45EFZ5aurtQ8mZVSlH3SZfzGESXfX0cXG4C9lbxZ6mT0gpPflDTvYFfcHhLSD4loFDDE5DFfwhauHR06HR_sU3-wIVydtGsuscfbHwSUuH1rWqvAohen6XdyAt9ngjI-XTn0cUOixX8sTE69wb4lw56Y518hWVAyH0O9y_sT-gTfWzfDB9c0_v31ad1H1hbe8htgARax3e6KVWbRalHw4PlovTBPScjaPuLAIl6DdDipnYTsvqQkCYRlODVG5V3oP1bnf5EsIweDfHAEia_m5w0y3wT7aLMvH3YTMCHWTB9JVxvLQfrqwP_gOBUmoDTL_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nAiZJwvFi49UYshykSeLWSyykm8KfcaebWLqUd99Nbot5MHyu8Vrwsavy6FdbjaZCTUsfXg-oeQbw-PUGaLVho800G4Z5f7kDjIYDnnjuEEGBtJsvH9x1LxNsM97efc6mqSg4q5q7RlucaqVma9hCOsm_wbYOfQ6W-jWKS6gUoK1MYfMwBf4bwKHaG_9EF4Xldf6uydP7HLIbYP65NiSRb1V45jdK6tT1CVl_TzZN0lxNoPuLLIVXUZx9t1ROjoOjgsReruY9iR1PClhVwbodOlNRNTqy9IctHVyDue0_GOxRygXx_IdYOD22-C88tF_navSGI7cQjEukXAcpxOhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaVPOmCS24ujJwGIn2Xg9brSAl89drFNAyFkvQxtJaZ4pR2BoSf8P83_kI1seX01dGTMPe37B4e27d8xWhEdLsJVtycFl3lRMTqk4QJOTr9AbgYFoDK2MzGrtoVm7z9cntioH_Fn9juGAQemN46GEL95xk44zg9wjodrbsiJbDebvKiYMIl1yLsKgF6vXd92xIBE93NLvSTrfaDT2njAP-hV5wiizg2M_JP1qavvO_cam4GzXXSLitY_OcXd43Kj4Zp4Z2OmxPy6gpeubPyBHyIreUETuPMV3Q8bMZSK3d4tYPggKZIzksOYHLtRdMH1gC_uyhr_GQjYo_NAWYXJ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p_mfaLjTzo6NVIC1_TAsCw91vp4kueSkHEX0IduMIVfmXYk-UlhsJKpvLCBUqgmeWUy7g-K-zQkISri6Q2spDxBDvE4h5KPTm0vB1GmDEYUMDusmBf3R1TBsmmt6a0OGva2OGCAso-qJN1MYUnqYSFsYdDyVmZU6iS81z7geCKR1OxmtvjgWbvyaFSiaOBWucNqV3WhWCCS_JrSxyDrvuZDVvele9OodQ6vJcf515z2dhcIblfBSkQSBOWWlVidAgVh3XIVmWQqJPG1uXn9u6wkXdKjzwSCARuNNTQEE4ABHAgZhhQpW833KtS5xTGbQn9rcBFIoro8tdu8b6UrgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3ibO0Vefy-6m-50ndl2OWk3X_MopNqCKwSOIfP6xlhdRN6Y-K4KzUJHJCxvk7DYtZK-Y4vpJVa-3pPvZYYSPOohkDfLb01rZM2woWVxK8RNxEqI80iqR6Ezsgbu5StXfTZDKaXfM8D9oOrb7yjnv-bhEUW5w0Jpz8oV3z44vVnlpk2mR-1X43bsPrXYWMUc0JKKn2J1BEJXMACL9l9iNfqeiJL1gf2Gmui1OzkyJh55tqFEIGoRW9HEqo1f_KS0f7J8JqQzzz4_bRuyy2SAzryXOmpuCrKXj7E7W6vDQN5Hitq1OCYGSSoPegCQjw54HN_PxdFXrVHwrl4JfT-0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DICtn1medogTZAhvdvV-jiOtKDfcSTteUFhaTamuI0ZGWvzI6zg8gshdz6qlUZUcc9jUL15PtCnAqxNrUVWwMHi8Xij-K-4eBc3hdDumROL_2L4Om6Tz6pKwm5F92qi7DT_cP36OIEWM0IyWTUHTMYAmSRGhwIiVtZYY7LrGIwHVvkpVLssNctq49lam4jY16AfUWkDctfU52NdArXz9qG4JtZmhs0264KYO3K41aFMefjfLxy-fEiEXQf3m6QPNY8aanniqzOrNyDamvx-haO1JmQaderjgn_GPwqkQSNK0Js4szUkoOPE0ZaGlOHSXwhamUpJrmN8Ek4d9QUmgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DK7fO0luly7mETLGPMhrzxEwcX_A_O9D2OTKRr2FgU5uo6GuHXvavyCZOx9rArIO5LAe2XcCyF0KanAi8eyEltTX3qL5vfRsLfQq69wM25glz4ikWzCJV9Nh-WsutEyWzxd6xbvAJT5k_u7KJAqLkQ1gFI7Wlm47Wj-6IIKWqK66YQXGWu1EuvWihnWmeRxmt4oPFAJNpnQT8CvLRN4zlEL_K8OBaJM3cXDQEZxmS2lsQffj1PiuJORYuYTd7u5Ee00a1F8xSdfW6FTlbD_mr_KJaojT-pZLk0uCIAjJ-EEdgpx0s30Vrk3ySbTdExSwNj5ECHVz8zEwE3ollEaO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJixFGFXh5keYsiDMoKLhNzdXTngSMX4zIO1xeGnTWA277s5xef_--vfj_zmtVvHj3GA5dy-248jDZbOOne7lgLrRAzU6IADTG3j5xscwtLYG9v8pgP45GI1cs8dQe7RuoTH3L6IRahAxogBEQPvpdruOwgb70wLxtif81ZUDN5aWIAsYIDX6-fM2v4noUjiuQ1m2Har7scIHI7jtT82Xxk05DL-A0wm7NMjT56GE2P0mjECTEjDaSFZXNEseyUS6GHxL2EkLRZQfm2E-vQY8C3g-KEL92rLoJGtmQJieHPY3N0sG9escXh4Xx_mmDHAU3_2x-7EKF4ryXoPd2RmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaR2YV2i5jf_U0b6PRh5EdnqBeQo63wRu676km6ZW2TYXw8GQqiM8CUYCVi1W_CJ5lpZgEqOx6Z4mZdn4RMfyioYk-hS4XYUcuOU1aivi99BWFD89Av8AvGrCmSlW9h6xZUTi9PDlecaqqK2EQqRJrNR6r4QF8I5sKuK3sr246j8bKGrLP-F6IA3_9RBUF3ZVAOCc0zwVoEwyQXcHp8grzkJqS3UMojmtVGbO0oH9byXE6qUb21dR6Kq8ihNOIpkQZMGUvMr5LtcI3sgv-YqVhGb_RdphjH2IalDBV5X23y9eQbYC3yLkVQP4lWawABBgHDVVHTKaU7nqBUu0Tp-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S_rRHOaAhkopnaO0ubBffVnmGPIkLvbxtVltvbyLIeQHuJAzf_IwyqpJkgrwEgkeESJQsbBy9Mt22YKtuY7cK-qIlM0eZ7eZFk-pSD90CvOIgEvcBmSN_NbcgeuKwbS0xKyVe06BmWv5aekibb-3Dex71-psEQCCabMAIGsT6EXUSUp6Rtp2QJI7VG32Spe1Ew2YS3gl91LtJKO5tW-M2D6-Cpe5A_CsGm-Yunls4O8bFQZMptgUHbERY-ZZMieC78Zl0j3I7UX8xnMpYNfluprE1hMN2EUPjmcXcSntdPxQFN6wQ463SHQ39rgqkUG9AMFZzrp2xs_bAgphAVRLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AU8jFRWnGDBtrlb-8RILnNoZdZwo5tu-Ow_Za80YTroiHmmzjoIX8pb-S34kHyaoNUDQdaAPSb8AmX3DxaE_ZR_IfeWlnOYP-VbByiXdbDoVXkDFFQXkOyP_rytyBdjv3gX01kZ7wGz67DadHAs2xFXWfA2jjedXqchz3CyjBvoS4giA-Ce2eG2VF0b9fr2_1Mr0f7C_jpcjEdCYjWs05tZv4rWN0m7nvHFbPwy5G0hMvdcc1lq2zhIIrxfX_1eiLols1F9UGOvjZrYeNDNobeLvEKF5_WAU8v-NDUwy9KjSBm_TiNXzBPwci4FYGgc4W0vBnVd2Sham8uk88IgSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGH6KsUhn_ds2o8_Z9exh2RvXjIeTnLkcn8ANH9r-2hCDgxXA2OyaTXlA2UGOgcLYe4I1r6blh7Q7O4pUPJ_o1BQ6E7uPocf9GXxcFpRmbXNnmeHW4SNShhB-LStZRNK_frAVd4g1JtSv9iHmRRXX7uSAyZGEmsxDEiaVt2go1tPk89d7RNM2p5te4uKxSAJvoa0kjteLWj8c_-ICNgGzMJpUhsJNatnQt-0Ar65V37t0uF2Fzk6HjuwKcuKGdHH3dq3c5O7qTZEPdFdnY8KdpBe2fYdGAYR2WZ1s4OaKSoYtupHIzDGmv_gnew9mCpr1TCNqUw9-bXMqbtDhULMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bh_bVN41JxWfNnvsDxZDkNDl1i_U96CywXPYkpqGXsTPX1vZ4FBOjxX1fjbicmvlv2zBKlfolCnw4PNIIsmzv4Ud2pY1Vkr6Ll0_hXFhvmx5yb5Aey3S5fdiBs73NcozBQwOybnr5xkxUIvCVxPrG8pURvBMkLQQJ5Pyk-Vw5kQwCIIoC6rnnF9RgK5RBypxKyKvhNzHmt63UGXMn9oPCFWVOmA9lvTAY9CVFZ_8tFkW5RDTL6mYBsnmmTv15QDZ5axb5oOWuSr6-LefYLjpbGF0bS9X23SBxgPlPN-uD-RKd_i6rwHuc4bV369yGUw6TfdNGH2OXYmRNjvwIjUnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCz9XCRtquQLXsZd7Nwj7SVFYQbzUcilhEt9wWa5Ckw50ys1OIzxrYJAg4iCY5yG2l2MdlL0eVeZFIp3arr0r9a_IZOMQZ2ok-XZUPIl8BGdMwnPVJ1iHNP8vImRYfmia64xcDkTcoFGADI8tmXimBMAxNLtFRluD2knoW8PDlV0fBjfRh-eX_-pJ5LGVku0InK1WQqBV5A-vM6UOgv98P-HC-8fCw-f5oyLLYPkwQ6rLqSOQo-agq3_jpS96ONr7xRY9ZS4XNDmNpsUMcKInMISMk4-USH0aobdGGNjKL4lxEyub6fLf8vCxssaKwXiRxC_7f7CX14_sU79zvDV6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q8DlJ1PHmwUdMDVDOv2Bc--nr-bqPQGwk6zJC4D181y2x0f7lF1XG_Xb60if1tR3fWQXT17Oii9I5oh0x8ISPg9JkCnnGDgKknAS68BSdl8fa9zMke7ImNJqr0YrOqgujL1IEoK5Sjy97Wt6yhIdu2o3iH0lcQE93ZTF5qRH8l-Ax0lT7IQJblqfz3ti_Rh_3ydY-R_ZM6nKVVo9m_4zk46dK5ZtZ-xs-beWA60xK3VxbX2E4XoNVkFLFtmYAHhbAjUFMhXYOGWmGRiItd7fkMcghsZQQeWTlwePaXE5CQTVUBiZomuFM-CGkqP7-r62Uti7vivCXpQlcx7QsyHKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QgQXUVf1erl_VMmMxvTXMEuhqc_XId7XaPphVjRG6SsU42q9TlrJQLau_LxoFaonuG4C5lmbXWRKd6MmB09Ft98zaLNKACYKZnqXrA2ndEDQwHD_aa1wlDyv7SjaLJE0TRGh53dM2z_5M1Zck65WcvehejAoIvY8IQ3_5FL1NwRtbF6U7KWVPXNIlIvZ53yU5qO6b7xmT383an7lxvrZi5gca1RxB6U8Ka5bxns4dRxn3vCJ2rDp2bOQ-9RdQ8Ar2qv9m3b5ACIPitQMy_WVoU1Nk3wjaBzybGczFMZmNc6ovYf4T91evBzSpIiE70_Pzc-b4Q0OlTwxw9TbVvpkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L8ByU-nLGkes9rn9zhPFz2ugg5n0Rwet-O_HnWFPE98COKq88UIFO1nk096jQKkK7EhvIS9d8UO27N6ZErSTH6_n1VmM1LaPUKQFAO_JC_yVUQdjV9lWacLYxzb-OMwaax3TU4g1IphJV_UecZeCvF23YwoGMqbbchLM8DqbtrP9Fx4NJtJdUOI5faU75YNeZ4_o1dGiXrmSZiuJgCZkqCt6smXHMDDhBsoiRx5PIxvz7Hqmiv3RbQwiL3Xs2f6kGes8ipWiKiMp7u0eb53NZP5EchxkMySBZVESSNqmwNBaQQ-TxqoFBEDurtXJOqzD42S1lRfaHzJa-GgVJQoppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kpj9kewL1amV78AI4gsNaAQ__nzyvOgTxtnoBZcbuo-gMSqRSR81bq0ubEyOjhIC_nNusFel900qB33l3k_GWCNu8cPmU-EK2P_hPlBkhhyb-WNrGd83Y_AR6k_-pYa6jnmQkOIoAQsEV96zWag3eSUONMmALm_Dm1BQ5sCECuB3eEDaB1NfmBf4xqNDhKJ_efYkH3E93h_7GrWxc7yn7xoDczM-N_0Yj6ajLXc8_fWOHICw0MNMTlezKvQhFx3ItyjyNVaZx45NSt0AgyyK2QZxCKbRww2q9ZPZLsShpQ3ApzqGUtN5JZWIhS1cQBG5U5Z172xPx8iBzRD8vziVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BSwrz6oDif6u2yBV5vcUsWF0hMZYLai3NS4lU8E5bnc2mIaFngx4uBKJuZxDzcNRZgvWQ9pfiIvkg2mog6BHbM90FRVuw0D1ByhlTG353wgMgE3uK2s4fa4VbO2YPiBp9T0gF0Mb73jLr3sxfGxbIz3R5ZlIcJ3aFg6M6tmHR1m1kQLvMnlTd2XI2-oUhKFqnp9OWVbnyCNPEZV0ZvX_W5WEIddeVb3kiIXC_J_PCpJ53wVyF8ljPLdRaBBnrYKlZh71r7ujdTv7vnmUSPIxin1Hu2EGBk4DUtA83RisZevFltxJnYXprqHfJO72Dlmaz0XgEnzZifmMo9yZZqG0vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CK56CyMhFvVAAgBnxhcQmFbcfGNM8iB9tSfU65X2UFgG5gioqZPeFRXoIuXDD-DAFdRvDCE8hdMWcQX8ztCx_keGofiuDmsULlyteRYrAVSTrjBMZnM17DaMrXIKwyHH4UGBlDzlIuJK3yaTM3nWm84OWXFJ8xkxqmkre80D0HPeB0FPihe0wt_xW5nHOAYJvM0HUR_g0854cbXuc0OcQxkzUDuau6qfVbp05uUV7QsZxwGDazjtFARxdScfw07irm5NwOhuShfJG267HhQyQ7BKRkPphRrFD3uEGV6snHKaF-5_1VsqO5bZANgzmJpJvPI-ai7-h10KrvGJxq6NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpbpC-GoZ3ReW4DssN6y4-uxyG6VSDbNbvyLs5EZ29eeU4XduO8IjjOQCRa4Apo0zrSpIuFD0nZR4_xC5wPNq1Xk9cSd6w1VsoKl2O2X6sXSwr_-SEKLjSsZxf-qwOtizs6vuytG6m0nlGxzhQHtC3Z6Y3trX2prpmVXzJUY8gzWikofDDZrNSmckNZl77ym9h1s5EjSvMn-So0hgdIlGnP4iypPx0uTr1Q9qhvwGVWTR55glDVUPTy-eTY_w_Srd4x24zqP8lL3sEe3FearQvh85YqvmUveY0hHWgpr3-f2y5v3PVuLbzcqyGjF5xBjdYG-boaDO8jmME4GsPTkjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N6y1brU5SfQdu-BIKv2epa-LZwAIqFFUYC3Dkiv8xIABdOEEUl35BR_QM61S-Kw2RWAj9YcicFaxjhLcVWMj8RDEeFgDWKqWD2iE_tq4gax5wfALDUl6Xvbax5CBn-5rz_AAMQvkmLl-1JZafWNLia78wUUBrVSn5uIt-YSe0IfQ9ZveH1TG8DwoEsD8GQtKQhcw4BfIeW9w2NA1SmhN-kfWy9VsyYGAnNJzj4qA0Rf8Imluz9LZY7a89A7XXtK2ENXbPqXBEuQoGNf5Bz-7tau-7O2PE3ys2glTlwMKcjsByqI80eQkKE5mUQgwhLu8fXoR22SF3ARCqcdwZuNQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uzyju3K8r5sBdRmKf8t1zPOgefiG-f6hhn1w0km6d-0naA7f32nlBXNn68tlpCoeDq3jPB_1YiHjQEBW-bWXpmMMbbERxFCmpS1PsBg9poLaEU6SSLDW1GDrhFoXNU6eYDrtWioh1ywoJOLNbPiLf3E7-MbRCXMVw2coZx-IBaVYHQYwm817KYJc4I6zg-WvyWFtZKQhUepzjbflFhYifK_EzazPnwBuQWSRhzVGb4aWyPAaEODTlyugA28YTDXBpNHOFTZIygPHMZY-7A4hfTfdO4KK0eAbb7JA_IeXiyaO5e-vwzbyUauXJjAQuH64n8QczMGEqHQZx1jfw7dSgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XfgsXU2m-NdSRZ-DPnlVeQ0C5S_UGhiUxvXgeVgIAdsJ-h0PrVkgCMTL3kOuQyw4LBsxb5ARDJ1Yi5ypUEhABjkJA8HHKS_AEKezzQxJQbwa8amOd-gCA5ogbmOR7VGXbFzDWgo1zmxWoG98Ba2v0WWdIi5AQkePb9GRMDpqU0vzI2H1QjyeA4YZqS2n6vydueTludjYDESfDZn7JKF5EzLypziCWMEq2j5S66_FIPg1u8vPsYdP_yGBb1g1zPF_u9-Iy10fMZBfGvpJ2aMMpPlGO6PHkkHg4hRWhvHMdO1KI7F38M-OYEFHGyjIkQNLyrabCkd_PgCWq9dVigd2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VNYIFoOx2lWdjo4whAXYa8IjrQUDmOwBCHpXAMvKJ9mOkHash1ZrNBitGmGy6rfO3eA-H0oq3jvA7bxPqt0oV_bJhRDjvrsskBd58OXK2R-bsECsMlpWuu_pWt1BinQq7V0u9ctvkC-OpVZogdB13-JcH87kbHDucfvulGS8IKsU7Y4N4EfbDVWyrzkZkVNeS4keTUn1dQQNP4eRRjGA40-5wvWjNABctBkYrsas70sCVtAJPid-QYX6rquvwcIkr99mg-0ZnFHPa0kqD7bieioAM_UM8aW6xPH91tsLf4t891fDtlIa3awrYj2gePnw9xwn9HI0JIlfFW5ks9D0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ExQhxb0hQgpSLV5D5NuwYzw9PCrBHizixTOGQGWJ-bhNC0IUsKTz8fo26CaG7Jb43VVoNdZca4t9UzeuPVUd5KdH3i-PZWUVi30XiAiyyGXuJWsf-82B86Vz2ywKvT9jYvGnmfgd33nRYrzDMbdflHAsu90XFRB2nNmq8qFEqabhy5JhNMoKcHTB2o3MEIxzjNAPzuCAO6h6TMoq-VD1S4r6xMsLTFhdgDNw6wDJ_uGzaIVLQAPci1Sle7nlXg_XDaax2rDAAOYjJ3SxvEjc-ofxM5wxNDPzRPJPUaCPusAbx_-wazIUztOa9N_PW2E4pouEjig9qJN9Jbm19sjmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U7_R45RzQaiG-6w5xOMgpUNAIFWvxhOarqgLUwTHUoSqoh6JAbtSDZ2d48NdXvq0jiZnz-V6TLQb-_HA9xHagx8OrXaCZZvpJxkA49daP50omxl9HV_7aJd2e_Uz4RS8zGvQQhhZuVTHhPFaGN16j65CWhZUQn7J8E_kSMvP3Cqn3OyElymDKxc-XZybU8yjUJNgMK0in02zVGkvaBbp3wO-DEj8S7h6Zi7WIfW6Tw5lpFrn0J2wZsvIRs365bPDsdnYrc7Hg64560zem_8efc75fh5-XVmA6gyVWLdgnISXJ3H492_tVx8g1_Zbw1YclWnbJWK-BvvjpRQxta2sGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T8gmwoAbZQTAPj5bDtN8nqSORA2vSJUpRGzfq6jsyI3mmY0Xzn0CMznPhRPaFHjMmuwfmiaiseOWJ9mFzYdu0k5k0tpVaH4D41UDVNgBOBX391ChPtlS9oWRGKkU23KD7UAfY7HbJlEQuwBrZ26nM0OjLJmXeoDjuoHV57BMYVxFPwjJi6lya5I57-KI9oDu5a2ckPxBMWdveNd-QRlpmnABLSw34NQ0GwLcbyUKhm3_XxfkKxL5jqDfH8tIp8OZ4vH2_SsTWfD2IFeNKHa0GHl-FPdgOCT8DfYn9JmrbwSjBd1l--GkUrytHSxY4Tx_B3OSFiA6eZp0M0vod2sbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2451">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کاربران میگن "ظاهرا" دسترسی دیتاسنترهای داخلی به اینترنت داره برقرار میشه. فکر کنم هنوز از اون زمانبندی که نامسئولان قطع‌ارتباطات گفته بودن "بازگشت اینترنت درحال تکمیل شدنه" چند دقیقه باقیمونده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2451" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2450">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LkpcA6A4Kq2oyiylZhYWM2t9s_hv8UHyKy1gjy6_UnzcmhCQuLn1MpkozYe0lpCh8Ie3_3LUq1-ODUgYjmBZH750ZmmOoqJgdKmm-clEOlurak-Xmcuj3CFwHH6tcMqT2tvnNYJiDtqcxy4WmjIpQxYcLnSr0_XuFiyc0eq6RiwTeq5X8mWv026AbgN9qY8dJU_pzTNuoYz9XQTEI67pY0huZy1Qjk5N7Fy5j20neHZnNJzUbt72J7hkEfHCisFywXx_hnKYBUxMpVvMBIOTAiMOI00okRWNkJ8-lTxnnKI7730muxRPADp0fBXSbRDzawOsQHif5SsRi3VO6TYWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما تنگه را مفت ندادیم، زندگی یک ملت را مفت دادیم. سال‌هاست حرص و ناکارآمدی‌تان را «سیاست‌گذاری» نامیدید، ماشین قراضه را ده برابر فروختید و گفتید حمایت از تولیدملی، اینترنت را خفه کردید و گفتید «مدیریت»، فقر را گردن تحریم انداختید در حالی که رانت و انحصار رگ‌های مردم را بریده بود. جوانی را به مهاجرت، کسب‌وکار را به «تاب‌آوری»، آینده را به سکوت فروختید. اگر چیزی واقعاً مفت رفته، نه تنگه هرمز، نه یک وجب خاک؛ عمر مردم، آرزوهایشان و فردای سوخته‌شان بوده. این صورت‌حساب واقعی است.
©
rassssoo
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/ircfspace/2450" target="_blank">📅 08:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2449">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این اختلال GPS بخصوص در مناطق مرکزی شهر تهران برای چیست؟
داداش طرف اومد نقطه زنی کرد و رفت و تمام شد. الان GPS رو مختل کردید که چی بشه؟ ملت اونجا سرگردون و گم بشن؟
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2449" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2448">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJWNDn3iyyKSd5dy-U2QPpH5k2LOD_-zamhg8wWb8U2mr3AMTfYSHlolAMntv3RmOHA6Fd6WNw2GB9VuAlHHgo2Pmr1220g8E2j0UhH2J0kSet4QmLSHEmG4NKz7cKryVyRewLu0dpAn_8NDQB1a9n03AotSKzNi-2A6U_SDFAsmbgfTFRHw_Z4L-bYxgf_MbdXt3n4KJe2rZPdPjRNNnwQm4nc37ycu-oONLCzRyRej2SxfOVamGTTPXb_tySHWzXS7CCD6pIK9uxo3CRXTUzFZUfXwG8eibQSaF6zPlQhN6zqP3yYpPX02EEfcMTnHMRYyNCnE4LNdWxRSEee-EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه CandyTunnel یک ابزار متن‌باز و رایگان برای ایجاد تانل روی سرورهای لینوکسی هست، که با استفاده از تکنیک‌هایی مثل تغییر و پنهان‌سازی آدرس IP، رمزنگاری ترافیک، بازیابی بسته‌های ازدست‌رفته و روش‌های مختلف عبور از فیلترینگ، تلاش می‌کنه ارتباط کاربران رو شبیه ترافیک عادی شبکه جلوه بده.
این ابزار از پروتکل‌های انتقال مختلفی مثل UDP، ICMP، Proto58، TCP، QUIC، IPIP و GRE پشتیبانی می‌کنه.
👉
github.com/AmiRCandy/CandyTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2448" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2447">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vh4le5hDk1hi1Ed1sItIuKcjQHwTMm0nZUTTWqNxVpVbBid3tX0Kd4YFiWAPylRi5HJGYKBA6Fqzk8icnPwmsJ9PVrUAkc0AAyQehvyKdsQU2MlKcTN45b8GDrjqa_jv5SdRjMElJlWgblgoq2yGQARPQnKtZkYL6P4yG-tlbMdH-fk-SYagRaRPE-uUhFLzewI7TlrwH7CiWpn1dQf-8yxQ0TkseB-y8IsF-nkkxhestke0gm5bSG-zv1QtEvt0FmmzUaS30U9Uq0q19se3X1l1qUNvgcydbg71ogbEUhe6hvWWMSb-it6-GOPu3Vcz-dZ0-z9-8k839JxU3lLt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Config Converter یک وب‌اپلیکیشن متن‌باز هست، که ۳ ابزار پرکاربرد مبدل V2Ray، مبدل WireGuard و مبدل Clash/Sing-box رو در یک محیط یکپارچه گردآوری کرده.
این ابزار امکان دریافت مستقیم کانفیگ‌ها از لینک‌های سابسکریپشن رو فراهم می‌کنه و ورودی‌های Raw، Base64 و JSON رو با تشخیص خودکار فرمت، پشتیبانی کرده. همینطور کاربران میتونن بصورت گروهی آی‌پی، دامنه یا پورت تمامی کانفیگ‌هارو ویرایش بزنن.
👉
darknessshade.github.io/Config-Converter
💡
github.com/DarknessShade/Config-Converter
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2447" target="_blank">📅 08:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2446">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fmpn1TwKx8kGla7oSFSQSUA_hdOKryHSYMveFJuvEFhAl0-EakFuTYn-TUxiMytE3gEbiazdnSbN_6ZMgvod9FiAHc7dMWOkZprbYB9t91SGSKI_77pX-vsHWyAdXMaMox4P4LCOYMLfl2g10tjlTGIS7W6-6jesXZnlhFJLvQ6wLt1GQgXESXjjenpZPDeacm57CBwOv4n5kWj1cIiOUyGGz6vCqnC1A_E9UIE8A0yGnDx2o_p0QiEz2EkG36xmvzuUl3Hr4NBoUA-WfPeQKX6I69_7DshU0rKBhbyJVh_Ok4Hl9e0Xq7zuchIY5JA7OlQwuyvRiA8O0CO7SKY4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند. در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2446" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2445">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lKQjPYXTifdilmhTBk83QcacgfoZ8R4oJvLAXVsN3Shf14BGZq_XDK0R_ndmuCDtyKoXlHJkLRFppAyOoj9qrgwj0GTUciPAcYbXAwLcDit6cIlRZRK0Po55iAnC9LNwQ-22E8l2LC5geAA7xXKeGcjjnA_X-T8oUXGO9HiQCo3VFr4OjHrwLmPbIS2lqIyTsuHfM7LHhGCOE-1amWDztEnylQpMq3awx7A_slO4gAjWsqzIb0jobzG3Bpq2mqctpi25KFl9o3tMqTj5EylR5kLi9EbRo3E59xqYR4jl041S3ArBWfZvxEeKqHjNnT9gHmPkVFHhCLgIUDfX7sxysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه NipoVPN یه ابزار پروکسی سبک و قدرتمنده که درخواست‌های واقعی HTTP رو بین ترافیک عادی وب مخفی می‌کنه. این پروژه با معماری Agent-Server کار می‌کنه؛ یعنی برای استفاده ازش، اول باید هسته رو روی یه سرور راه‌اندازی کنین و بعد کلاینت‌ها به اون وصل بشن. در حال حاضر هم کلاینت رسمی اندرویدش به‌صورت متن‌باز و رایگان منتشر شده.
👉
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2445" target="_blank">📅 08:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2444">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXUqRW6wdiBgxbMnsC054Ba5_tbXwJNs7HyiaoM4U4uHDy_Jf_wqlO0NYA1lx0jeT67HR1zWe01d0FtMI1Atvr3SoKHHYqhIjNHhjHEQYiayEHPuWlKx4ye_QOyEDmFEGy6cQBPSW6iephNzXAZCRNxxVkwDz2gFEia0_xM99Z5Jf-zsZKtEa57w2ON90xn1kEA_FxEggYMWQVJVOWNx4LctRrOtu3xzOhl5M-AR2C8ud9NPKMPp4ceGkoPCeE9_QxT99Hv8F8X7OvtY_CGlXwEIZYp2S1wdgQJNX9ZztSPDghhAcjCP6J0aPSyT5a2jjPAt36D-rQqgKXEwKSJbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ InviZible Pro در بروزرسانی‌های اخیر نسخه بتا، با اضافه کردن Tor Snowflake و پشتیبانی از پل‌های DNSTT، قابلیت‌های ضد سانسور خودش رو برای عبور از محدودیت‌های اینترنت گسترش داده ...
👉
github.com/Gedsh/InviZible/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2444" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2443">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پاول دورف، مدیرعامل تلگرام در واکنش به محدودسازی استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال در بریتانیا گفته: این ممنوعیت فقط اونهارو بیشتر در معرض خطر قرار میده و کودکان به استفاده از VPNها روی میارن، که در نتیجه به محتوای غیرقانونی و به‌مراتب خطرناک‌تری دسترسی پیدا می‌کنن. برای مثال هم به استفاده بالای فیلترشکن در روسیه و ایران اشاره کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2443" target="_blank">📅 08:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2442">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از میان ۴ بانکی که اختلال برایشان پیش آمده، ۳ بانک در بستر ایران‌اکسس فعالیت می‌کنند و دسترسی مستقیم به اینترنت ندارند. یعنی هیچ ارتباطی بین آن اختلال‌ها و وصل شدن اینترنت نیست.
©
emirhussein_rz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2442" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mSdYm6yzBJuNSVnyDeS7vIdCyW28eVbO4NdDNUhuJ9gFoN0l_lNL0k2KyIv3FLA0sdarApqU5id7Upnq-8RrA8S89zPxYA5RakrbWVCKPY_2NvpUBTrGoA6m8m0f8P4JLcxXOOh0Y5tMtv9_BFpIhIvd197IadrZyJHXcwOz47I_RNreTfFjuhWXO64E6WQfjqvnenYip4jxsgD4gN5ZC5pbVsEDGBA-fW8plrq26hvjE0LuC5jUKXM8OhFJusbrtUXZyIECdZSvCKxKsjr3kGR8H8e7CotcIqETKr7GdbFIqdwWwN2gbo6PZobvPXutBDM8mHCcJb7E-rFY8Jp-AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویروس زارع‌پور به هندوستان رسید؟
دولت هند اعلام کرد که دسترسی به تلگرام رو در هند تا اول تیر مسدود کرده، چون از این پلتفرم برای کلاهبرداری از داوطلبان شرکت‌کننده در آزمون ورودی پزشکی استفاده شده. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2441" target="_blank">📅 08:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gUksd6mHb-15bvUgLBYrAD1oKHJji8ahMB8oEE0fzAs4GmBK_ncu87FhMxDVt5Ubzj1vJor-BeLLy0BuCYS5PkQADRBPm44nKmdZbC9IjqmeTuF02noYJxgrXi_LvnvduMW68UqDvnpWrXw3vNyDpI1dgKS56YqUIpLeUyKo-pvLNSx7MQUy7eGNRf3IRNzrQZf2yswM2tiUGFhmSM0zCIkns2tOm6RTmONg9qRCKg-ldKJgYFmjb_hr7zlQKAz06sqaNsXs844mRGv9cQV68jXYwlKFipKXcqxMa8-zJkH3AScLz-XTEbMqpJAMOfEvtbtE7HKn60AgPd2d2CaCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ سیمرغ یک کلاینت VPN متن‌باز و رایگان برای اندروید هست، که با پشتیبانی از کانفیگ‌های XRAY، پروفایل‌های NipoVPN و موتور اختصاصی MSP، تلاش می‌کنه بهترین مسیر اتصال رو با کمترین پیچیدگی در اختیار کاربر قرار بده.
اسکن هوشمند آیپی، انتخاب خودکار کانفیگ سالم، پشتیبانی از کانفیگ‌های ServerLess، پروکسی محلی، ذخیره IPهای تمیز، بررسی سلامت کانفیگ‌ها و ... از جمله امکانات این برنامه هستند.
👉
github.com/rezakhosh78/SIMORGH/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2440" target="_blank">📅 20:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">با وجود ادعای رفع مشکل قطعی و اختلال در خدمات ۴ بانک بزرگ دولتی، این اختلال‌ها برای سومین روز متوالی ادامه دارد. نیما اکبرپور، کارشناس فناوری، معتقد است طولانی شدن روند بازیابی، نشان‌دهنده ناکارآمدی سامانه‌های پشتیبان است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2439" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=RhJQcYxHWBN29EGfy_7Cjn2ZtVe9Y3O0zKuvxcbszgeoABIchzEWl96_q8K-sNG2BYcZB-4mlTRuKDoNtts2t7KoDNFQFOEqhJqELpzQhqjb6njLz8u1gQVeile7wVp7EhPVyGBJ0WyRVvmIGbSUb5t-np9n9KWR7RcDTP7MElwKQ5LjYe2mm7_UWwOe0Fb7lrtgn3cyuvAsad5cmVhGauYi6PakqGKiNU9P9y7eBWbxiPuhMwWMpU_WoDjihzrJ51zPSXwg4cqjvLXLXUj_7W66oTP5YDOMPD-8Q2-1tcoVwxBGq3tWSkStThm4anQTKZtdQy4EJpMTSKvjr8s4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=RhJQcYxHWBN29EGfy_7Cjn2ZtVe9Y3O0zKuvxcbszgeoABIchzEWl96_q8K-sNG2BYcZB-4mlTRuKDoNtts2t7KoDNFQFOEqhJqELpzQhqjb6njLz8u1gQVeile7wVp7EhPVyGBJ0WyRVvmIGbSUb5t-np9n9KWR7RcDTP7MElwKQ5LjYe2mm7_UWwOe0Fb7lrtgn3cyuvAsad5cmVhGauYi6PakqGKiNU9P9y7eBWbxiPuhMwWMpU_WoDjihzrJ51zPSXwg4cqjvLXLXUj_7W66oTP5YDOMPD-8Q2-1tcoVwxBGq3tWSkStThm4anQTKZtdQy4EJpMTSKvjr8s4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانفینگ
😄
©
miladiels
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2438" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در پی تجمع مخالفان توافق ایران و آمریکا، خبرهایی از اختلال در
#ملانت
و پیامرسان‌های رانتی منتشر شد. خواهشاً اینترانت ملی رو قطع نکنین؛ عده‌ای اگر مدت کوتاهی از پروپاگاندا و خوراک تبلیغاتی حکومت محروم بشن، ممکنه ناخواسته شروع کنن به فکر کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2437" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2436">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فاجعه یعنی اینکه اول حمله سایبری رو تکذیب کردن، اما بعدش بصورت رسمی تایید شد. الانم نشت اطلاعات مشتریان رو تکذیب کردن، احتمالا چون قبلا هرچی بوده و نبوده پابلیک شده!
شورای هماهنگی بانک‌های دولتی، اعلام کرد: به پیرو اختلال پیش‌آمده در سامانه‌های ۴ بانک ملی، تجارت، صادرات و توسعه صادرات، تیم‌های فنی بلافاصله پس از شناسایی نشانه‌های غیرعادی، اقدامات پیشگیرانه و حفاظتی لازم را برای صیانت از داده‌های مشتریان و زیرساخت‌های بانکی کشور به اجرا گذاشتند. بررسی‌ها نشان می‌دهد حمله سایبری محدود به چهار بانک بوده و هیچ نشت اطلاعاتی رخ نداده است./ انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/ircfspace/2436" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ایرانسل و همراه‌اول با گذاشتن ضریب روی بسته‌های بین‌الملل قشنگ
عَنِ
دزدی رو در آوردن. گِل بگیرن در اون وزارت ارتباطات و سازمان حمایت از مصرف‌کننده رو، که دزدی اینقدر راحت و علنی شده. البته چیز دیگه‌ای هم نباید انتظار داشت، یه مشت دزد دور هم جمع شدین!
©
Mohsen_935
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/ircfspace/2435" target="_blank">📅 17:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nPow8wOWsTs9f0993gCUodLLIXSyq7gHcaNtiCSTP10MoNO_k9T3bXHMrsSHsKillmC5wqB4birRQzVLCTIWdxtgZKM23Jun_JMBjZd6HL6p-2LObSpIiz59Otd3b-1nHL_bOtLY5TgUxCgh3WpKJARlflxDzBAbCWIM1tvMnF2wbPzq8fyOsjgPLSLOHY-ed-knq0Mi4PifaeZDC4Gqu4hPb4mYkUXiqgiXLvdRwjgY__FIj0-6HcPncoSMzjw-xymVz5g4FEDlbSUimhEnn83cu_aHD6i0m9jOQCfZ7bnZAk7LVeuhOxURaJVAAP1YKmaneuL5oWEGomNNJprXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دنبال بروز مشکل در ارائه خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات از صبح امروز، پیگیری‌ها نشان می‌دهد عامل اختلال بروز مشکلات زیرساختی در شرکت ملی خدمات انفورماتیک بوده و ارتباطی با حمله سایبری ندارد.
البته تاکنون زمان دقیقی برای رفع کامل اختلال اعلام نشده است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/ircfspace/2434" target="_blank">📅 17:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hc4lTepMpljxP3atHN0i0mkslL1knHOr8Y2dYyB2X5ersh6nOXSkASC18e34wxM8HpwnpFL7dwrP0u1Iya0O8dRb73dT5_efaEOrVNWRihXFcNVI2-1Iu8mRay2Dm5e04GECAScu3Sb6IEgqptwpO45jirY0afMJ6W0nZLmqFZDpUOfeud71x-tF3kPSTY4IRXGeAvtq_4nH_zUUzeK3ZG2AGIDBBhDoolRfLtP-IFbzgcSCcejPq07comc0A1Od39DyKnQw7QvIJ8hrUFh-wv5eU1dY8RBrx_c3nrMF5xmr-HItE10EhmywjsnrlKhPsX0KjQJBh-Q2siVohsfCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اعلام کرد پس از دریافت گزارشی درباره فعالیت ده‌ها کانال یوتیوب مرتبط با اشخاص و نهادهای تحریم‌شده ایرانی، علیه برخی از حساب‌های ناقض سیاست‌های خود اقدام اجرایی انجام داده است. این شرکت جزئیاتی درباره تعداد کانال‌های مشمول این اقدام یا نوع محدودیت اعمال‌شده منتشر نکرده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2433" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HxChYNpE6JdQJ9N7mODqhZ8OT4ouDfZukY5NeTNkgL7T5D0zw2UAbVJP0anPH5dJzZqTHvRgXEtwEeN-KjQsZWDrM1kBVxyy6TGu-T1pBoc97OIkeY8MTUP-Y6_FMk71vUkUCIbM349Z9ezw1i62U5ludVEyu8t1apCv5LGt9jUvfzBOp8GG9Wppm8Mnoz0etSLLGXW79uMv0a9izrdl88FvpQOnb9cVXtQmcaNCpLKkx-9s4AF1BZmU5gZylwceeEzjkcYxu3Q70wylcK7RMrHPDqXClfvhg-QdqdRKZyLU9Jcp3bzxYOKIWHEptO6xSN0gAuObcr4bJyJOVZKhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی، وزیر قطع‌ارتباطات اعلام کرد پیش از بازگشایی اینترنت حجم ترافیک استارلینک با کل ترافیک اینترنت کشور برابری می‌کرد. او همچنین طرح وایت‌لیست اینترنت را برای جمعیت ۹۰ میلیونی ایران غیرعملی و غیرقابل اجرا دانست و گفت به آنکه ایده‌اش را مطرح کرده بود گفتم ماستت را بخور. /یورونیوز
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/ircfspace/2432" target="_blank">📅 08:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2430">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f8mk6cdkIY70cu2PhRFXhELaK6-T2pQGW6EN5V5nibsnZTBcFzgg5hiRPaA-_q3_glWFhjsfogcKRnPGBF6MgvwZiCd8zsZIwgFAWTwHCLPAACV5b91bq7CRDN0281QIaWSzFeMs9VOhL7LFA5ncX7hKLVnRk15YWEMFbxpT_NivpuOF2gbR6RbbWJ-Yo0KY8Gnj75ofkuYH2nq8ayqu7iQhQVLSIIwZIvs76H_64oYQFvEid3ciQ4_ldy2Bbprj0rg6cufh09dMHR5guhoP2Eo8ffyObKMfrCC5NvKj9vo_ofJYpdbcW2y1K8pgdoJWpziOz25_Nbp5-WXBDPSCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌دنبال توافق‌نامه‌ای که در اردیبهشت میان شرکت ارتباطات زیرساخت ایران و آذربایجان برای توسعه ترانزیت داده و زیرساخت ارتباطی به امضا رسید، بخشی از داده‌های ترافیک اینترنت ایران به اپراتور Delta Telecom در آذربایجان منتقل شد.
داده‌های موجود نشان می‌دهد که آذربایجان در مدتی کوتاه از رده چهل‌وچهارم مصرف ChatGPT در جهان به رده سوم رسیده، که انتقال ترافیک اینترنت ایران از مسیر یک اپراتور آذربایجانی این اتفاق را رقم زده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/ircfspace/2430" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2429">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور گفته "نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه".
از اونجایی که دولت کلاً هیچ‌کاره هست، نگرانیم بیشتر شد!
😒
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/ircfspace/2429" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2428">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYOjB4UyuZibSnNYKPoz_VCEuSjxN1HrhFnowace_7Z79Xm4A6I9nL11CkyK3DQSzPaa9_pEjPD9QcpvcJm0uvjI01Ir8jT6mDp5bVXdophWMmElUPjaM4-1wbiMBOzOPdVYrj5NUb9x6_wXgz2det9_FU6DkGZPpBqrGRI0AkSw8a-t5ooxyz3V385iWAxVTmoYqKQNBYOHD6HfRblnRJmS7n0oaFvfvz16AXq6VLh3tuMqarD5JJ9oXhpO6_P-gWbe1UcJi9jkeC_L23vT2t3kqz5yVEEnk_8l01SqKLjQpoJ0cYGPxWryYo5uAT25JyaK3nfyWdPH8jsIDZm7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان pyWarp که برای ویندوز، لینوکس و مک ارائه شده، ۹ مسیر اتصال به وارپ (با انتخاب گزینه Auto در Protocol) چک میشه و در نهایت اگر اتصال امکان‌پذیر باشه، بهترین رو انتخاب میکنه.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/ircfspace/2428" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2427">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هنوز موشک‌ها توی آسمونن و به زمین اصابت نکردن، پهنای باند رو کاهش دادن و گزارش کاربران از کندی اینترنت و افزایش اختلال‌ها حکایت داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/ircfspace/2427" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
